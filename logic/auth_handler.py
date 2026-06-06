"""
Nama Modul: auth_handler.py
Deskripsi: Handler logika bisnis autentikasi pengguna (login dan logout).
           (Ref: Security Design Bab 12.2 & CLI Flow Bab 4.1)
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

import datetime
from collections import namedtuple
from typing import Any

from logic.safety_validator import sanitasi_input_cli
from db.pengguna_repository import get_pengguna_by_username, update_failed_login, reset_failed_login
from middleware.auth_jwt import verify_password, create_jwt_session
from middleware.audit_logger import log_audit_trail

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


def login_user(username: str, password: str, db_conn: Any) -> Result:
    """Mengautentikasi pengguna berdasarkan username dan password bcrypt.

    Mendukung rate limiting brute-force, sesi JWT, dan pencatatan audit log.

    Args:
        username (str): Nama login pengguna staf.
        password (str): Kata sandi polos dari input.
        db_conn: Objek koneksi database aktif.

    Returns:
        Result: is_success=True dengan data=session_state dict jika sukses,
                is_success=False dengan error_msg jika gagal.
    """
    # 1. Sanitasi input username (buang karakter kontrol ASCII < \x20)
    username = sanitasi_input_cli(username).strip()
    if not username or len(username) > 50:
        return Result(False, None, 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!')

    # 2. Query user dari repository
    user_res = get_pengguna_by_username(username, db_conn)
    if not user_res.is_success or not user_res.data:
        # DB error atau user tidak ditemukan
        if user_res.error_msg:
            # Jika ada DB error, return error database
            return Result(False, None, user_res.error_msg)
        return Result(False, None, 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!')

    user = user_res.data

    # 3. Periksa lockout status
    now = datetime.datetime.now()
    if user['locked_until']:
        locked_until = user['locked_until']
        if locked_until.tzinfo is not None:
            now = datetime.datetime.now(datetime.timezone.utc)
        if locked_until > now:
            return Result(
                False,
                None,
                'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'
            )

    # 4. Verifikasi password bcrypt
    is_valid = verify_password(password, user['password_hash'])

    # 5. Jika password salah
    if not is_valid:
        raw_attempts = user.get('failed_login_attempts')
        if raw_attempts is None or raw_attempts == '':
            failed_attempts = 0
        else:
            try:
                failed_attempts = int(raw_attempts)
            except (ValueError, TypeError):
                failed_attempts = 0
        attempts = failed_attempts + 1
        if attempts >= 5:
            locked_until = datetime.datetime.now() + datetime.timedelta(minutes=10)
            update_failed_login(user['id'], 5, locked_until, db_conn)
            # Log audit trail ACCOUNT_LOCKOUT
            log_audit_trail(
                pengguna_id=user['id'],
                action_type='ACCOUNT_LOCKOUT',
                target_table='pengguna',
                old_val=None,
                new_val={'status': 'LOCKED'},
                cabang_id=user['cabang_id'],
                db_connection=db_conn
            )
            return Result(
                False,
                None,
                'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'
            )
        else:
            update_failed_login(user['id'], attempts, None, db_conn)
            # Log audit trail LOGIN_FAILED
            log_audit_trail(
                pengguna_id=user['id'],
                action_type='LOGIN_FAILED',
                target_table='pengguna',
                old_val=None,
                new_val={'status': 'FAILED'},
                cabang_id=user['cabang_id'],
                db_connection=db_conn
            )
            return Result(False, None, 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!')

    # 6. Jika password benar
    reset_failed_login(user['id'], db_conn)

    # Terbitkan token stateless session JWT HS256
    token = create_jwt_session(
        user_id=user['id'],
        username=user['username'],
        role=user['role'],
        cabang_id=user['cabang_id']
    )

    # Log audit trail LOGIN_SUCCESS
    log_audit_trail(
        pengguna_id=user['id'],
        action_type='LOGIN_SUCCESS',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'SUCCESS'},
        cabang_id=user['cabang_id'],
        db_connection=db_conn
    )

    session_state = {
        'user_id': user['id'],
        'username': user['username'],
        'role': user['role'],
        'cabang_id': user['cabang_id'],
        'token': token
    }
    return Result(True, session_state, None)


def logout_user(session_state: dict, db_conn: Any) -> Result:
    """Mengakhiri sesi pengguna (logout) dan mencatat aktivitasnya ke audit logs.

    Args:
        session_state (dict): Status sesi aktif pengguna.
        db_conn: Objek koneksi database aktif.

    Returns:
        Result: is_success=True jika berhasil.
    """
    log_audit_trail(
        pengguna_id=session_state['user_id'],
        action_type='LOGOUT',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'LOGOUT'},
        cabang_id=session_state['cabang_id'],
        db_connection=db_conn
    )
    return Result(True, None, None)
