"""
Nama Modul: auth_jwt.py
Deskripsi: Middleware keamanan otentikasi sesi berbasis JWT dan hashing bcrypt.
           (Ref: Security Design Bab 4.1 & Bab 4.2)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import datetime
from collections import namedtuple
import os

import bcrypt
import jwt

from config.settings import load_settings

# Konstanta Keamanan
BCRYPT_COST_FACTOR = 12
JWT_ALGORITHM = 'HS256'
Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


def hash_password(password_polos: str) -> str:
    """Mengenkripsi password polos menggunakan algoritma bcrypt.

    Menggunakan cost factor 12 sesuai Security Design v1.2 Bab 4.1.
    Salt 16-byte dinamis di-generate otomatis oleh bcrypt.gensalt().

    Args:
        password_polos (str): Password dalam bentuk teks polos.

    Returns:
        str: Hasil hash password berupa string UTF-8.

    Example:
        >>> result = hash_password('SandiKuat123!')
        >>> result.startswith('$2b$12$')
        True
    """
    # FIXME: Truncate password to 72 bytes to prevent ValueError in bcrypt >= 4.0.0
    password_bytes = password_polos.encode('utf-8')[:72]
    salt = bcrypt.gensalt(rounds=BCRYPT_COST_FACTOR)
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')


def verify_password(password_polos: str, password_hash: str) -> bool:
    """Memverifikasi keselarasan password polos dengan password hash.

    Menggunakan bcrypt.checkpw() untuk komparasi time-safe.

    Args:
        password_polos (str): Password dalam bentuk teks polos.
        password_hash (str): Password terenkripsi bcrypt dari database.

    Returns:
        bool: True jika password cocok, False jika tidak.

    Example:
        >>> hashed = hash_password('SandiKuat123!')
        >>> verify_password('SandiKuat123!', hashed)
        True
        >>> verify_password('SandiSalah', hashed)
        False
    """
    # FIXME: Truncate password to 72 bytes to prevent ValueError in bcrypt >= 4.0.0
    password_bytes = password_polos.encode('utf-8')[:72]
    return bcrypt.checkpw(
        password_bytes,
        password_hash.encode('utf-8')
    )


def create_jwt_session(user_id: int, username: str, role: str, cabang_id: int) -> str:
    """Membuat token stateless session JWT dengan tanda tangan HS256.

    Menggunakan secret key dan lifetime dari settings.
    (Catatan: Signature fungsi diubah untuk menambahkan parameter username).

    Args:
        user_id (int): ID pengguna unik dari database.
        username (str): Username pengguna.
        role (str): Peran pengguna untuk otorisasi menu.
        cabang_id (int): ID cabang aktif pengguna.

    Returns:
        str: Token JWT sebagai representasi sesi aktif.
    """
    if user_id is None or not username or not role or cabang_id is None:
        raise ValueError("Parameter esensial (user_id, username, role, cabang_id) tidak boleh kosong atau None")

    settings = load_settings()
    secret_key = settings.jwt_secret_key
    lifetime = settings.jwt_lifetime_seconds

    payload = {
        'user_id': user_id,
        'username': username,
        'role': role,
        'cabang_id': cabang_id,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=lifetime)
    }
    return jwt.encode(payload, secret_key, algorithm=JWT_ALGORITHM)


def verify_jwt_session(token: str) -> dict | None:
    """Memvalidasi token JWT dan mengembalikan klaim data sesi jika sah.

    Args:
        token (str): Token JWT dari sesi pengguna.

    Returns:
        dict | None: Dictionary data sesi jika valid, None jika kadaluwarsa/salah.
    """
    settings = load_settings()
    secret_key = settings.jwt_secret_key
    try:
        return jwt.decode(token, secret_key, algorithms=[JWT_ALGORITHM])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None


def validate_session_token(session_state: dict | None) -> Result:
    """Memvalidasi token JWT dari session state pengguna aktif.

    Fungsi guard terpusat yang dipanggil sebelum setiap operasi menu CLI.
    Memeriksa keberadaan token dan memverifikasi tanda tangan serta masa aktifnya.

    (Ref: Security Design Bab 4.2 & Coding Standard Bab 10.3)

    Args:
        session_state (dict | None): Dictionary sesi pengguna berisi kunci 'token'.

    Returns:
        Result: is_success=True dengan data=dict payload JWT jika valid,
                is_success=False dengan error_msg ERR-SESSION-001 jika token kosong,
                is_success=False dengan error_msg ERR-SESSION-002 jika token invalid/kadaluwarsa.

    Example:
        >>> session = {'token': 'valid_jwt_string', 'user_id': 1, 'role': 'kasir'}
        >>> result = validate_session_token(session)
        >>> result.is_success
        True
    """
    if not session_state or not isinstance(session_state, dict):
        return Result(
            False,
            None,
            'ERR-SESSION-001: Sesi login tidak ditemukan. Harap login terlebih dahulu!'
        )

    token = session_state.get('token')
    if not token:
        return Result(
            False,
            None,
            'ERR-SESSION-001: Sesi login tidak ditemukan. Harap login terlebih dahulu!'
        )

    payload = verify_jwt_session(token)
    if payload is None:
        return Result(
            False,
            None,
            'ERR-SESSION-002: Sesi login tidak sah/rusak. Harap login kembali!'
        )

    return Result(True, payload, None)
