"""
Nama Modul: test_jwt_session.py
Deskripsi: Unit test untuk feature pembuatan dan validasi session token JWT.
           (Ref: Issue #0110)
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

import datetime
from unittest.mock import patch, MagicMock

import jwt
import pytest

from config.settings import AppConfig
from middleware.auth_jwt import (
    create_jwt_session,
    verify_jwt_session,
    validate_session_token,
    Result
)
from logic.auth_handler import login_user

# Mock configuration settings for testing in isolation
MOCK_SETTINGS = AppConfig(
    app_env='development',
    app_cabang_id=1,
    db_host='127.0.0.1',
    db_port=3306,
    db_user='test_user',
    db_password='test_password',
    db_name='test_db',
    db_pool_size=5,
    jwt_secret_key='test_secret_key_minimum_32_characters_long_123',
    jwt_lifetime_seconds=28800,  # 8 hours as per Security Design Bab 4.2
    fernet_key='test_fernet_key_placeholder',
    backup_zip_password='test_backup_password',
    printer_port='COM1',
    printer_width_mm=58
)


@patch('middleware.auth_jwt.load_settings')
def test_create_jwt_session_menghasilkan_token_string(mock_load_settings: MagicMock) -> None:
    """Memastikan create_jwt_session menghasilkan token berupa string.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    mock_load_settings.return_value = MOCK_SETTINGS
    token = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    assert isinstance(token, str)
    assert len(token) > 0


@patch('middleware.auth_jwt.load_settings')
def test_create_jwt_session_payload_mengandung_5_klaim(mock_load_settings: MagicMock) -> None:
    """Memastikan payload token JWT mengandung 5 klaim wajib.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    mock_load_settings.return_value = MOCK_SETTINGS
    token = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    decoded = jwt.decode(token, MOCK_SETTINGS.jwt_secret_key, algorithms=['HS256'])
    assert decoded['user_id'] == 1
    assert decoded['username'] == 'kasir_andi'
    assert decoded['role'] == 'kasir'
    assert decoded['cabang_id'] == 1
    assert 'exp' in decoded


@patch('middleware.auth_jwt.load_settings')
def test_create_jwt_session_exp_8_jam_dari_sekarang(mock_load_settings: MagicMock) -> None:
    """Memastikan exp claim pada token bernilai 8 jam dari waktu sekarang.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    mock_load_settings.return_value = MOCK_SETTINGS
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    token = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    decoded = jwt.decode(token, MOCK_SETTINGS.jwt_secret_key, algorithms=['HS256'])
    exp_time = datetime.datetime.fromtimestamp(decoded['exp'], datetime.timezone.utc)
    diff = exp_time - now_utc
    assert abs(diff.total_seconds() - 28800) < 10


@patch('middleware.auth_jwt.load_settings')
def test_create_jwt_session_algoritma_hs256(mock_load_settings: MagicMock) -> None:
    """Memastikan header algoritma JWT adalah HS256.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    mock_load_settings.return_value = MOCK_SETTINGS
    token = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    header = jwt.get_unverified_header(token)
    assert header['alg'] == 'HS256'


@patch('middleware.auth_jwt.load_settings')
def test_verify_jwt_session_token_valid_mengembalikan_dict(mock_load_settings: MagicMock) -> None:
    """Memastikan verify_jwt_session mengembalikan dict klaim jika token valid.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    mock_load_settings.return_value = MOCK_SETTINGS
    token = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    payload = verify_jwt_session(token)
    assert isinstance(payload, dict)
    assert payload['user_id'] == 1
    assert payload['username'] == 'kasir_andi'


@patch('middleware.auth_jwt.load_settings')
def test_verify_jwt_session_token_kadaluwarsa_mengembalikan_none(mock_load_settings: MagicMock) -> None:
    """Memastikan verify_jwt_session mengembalikan None jika token kadaluwarsa.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    # Menggunakan lifetime negatif agar token langsung kedaluwarsa saat terbit
    expired_settings = MOCK_SETTINGS._replace(jwt_lifetime_seconds=-10)
    mock_load_settings.return_value = expired_settings
    
    token = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    payload = verify_jwt_session(token)
    assert payload is None


@patch('middleware.auth_jwt.load_settings')
def test_verify_jwt_session_token_signature_salah_mengembalikan_none(mock_load_settings: MagicMock) -> None:
    """Memastikan verify_jwt_session mengembalikan None jika signature salah.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    # Menerbitkan token dengan secret key lain
    other_settings = MOCK_SETTINGS._replace(jwt_secret_key='secret_yang_berbeda_dan_panjang_sekali')
    mock_load_settings.return_value = other_settings
    token = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    
    # Verifikasi menggunakan settings dengan key asli
    mock_load_settings.return_value = MOCK_SETTINGS
    payload = verify_jwt_session(token)
    assert payload is None


@patch('middleware.auth_jwt.load_settings')
def test_verify_jwt_session_token_string_acak_mengembalikan_none(mock_load_settings: MagicMock) -> None:
    """Memastikan verify_jwt_session mengembalikan None jika token berupa string acak.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    mock_load_settings.return_value = MOCK_SETTINGS
    payload = verify_jwt_session('bukan.jwt.token')
    assert payload is None


@patch('middleware.auth_jwt.load_settings')
def test_validate_session_token_valid_mengembalikan_result_sukses(mock_load_settings: MagicMock) -> None:
    """Memastikan validate_session_token sukses untuk session state dengan token valid.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    mock_load_settings.return_value = MOCK_SETTINGS
    token = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    session = {'token': token, 'user_id': 1, 'role': 'kasir'}
    res = validate_session_token(session)
    assert res.is_success is True
    assert res.data['user_id'] == 1
    assert res.error_msg is None


def test_validate_session_token_tanpa_kunci_token_mengembalikan_err_session_001() -> None:
    """Memastikan validate_session_token gagal dengan ERR-SESSION-001 jika tidak ada key 'token'."""
    session = {'user_id': 1, 'role': 'kasir'}
    res = validate_session_token(session)
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-SESSION-001' in res.error_msg


def test_validate_session_token_session_none_mengembalikan_err_session_001() -> None:
    """Memastikan validate_session_token gagal dengan ERR-SESSION-001 jika session_state None."""
    res = validate_session_token(None)
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-SESSION-001' in res.error_msg


def test_validate_session_token_token_kosong_mengembalikan_err_session_001() -> None:
    """Memastikan validate_session_token gagal dengan ERR-SESSION-001 jika value token kosong."""
    session = {'token': '', 'user_id': 1}
    res = validate_session_token(session)
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-SESSION-001' in res.error_msg


@patch('middleware.auth_jwt.load_settings')
def test_validate_session_token_token_kadaluwarsa_mengembalikan_err_session_002(mock_load_settings: MagicMock) -> None:
    """Memastikan validate_session_token gagal dengan ERR-SESSION-002 jika token kedaluwarsa.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    expired_settings = MOCK_SETTINGS._replace(jwt_lifetime_seconds=-10)
    mock_load_settings.return_value = expired_settings
    token = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    
    mock_load_settings.return_value = MOCK_SETTINGS
    session = {'token': token, 'user_id': 1}
    res = validate_session_token(session)
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-SESSION-002' in res.error_msg


@patch('middleware.auth_jwt.load_settings')
def test_validate_session_token_token_invalid_mengembalikan_err_session_002(mock_load_settings: MagicMock) -> None:
    """Memastikan validate_session_token gagal dengan ERR-SESSION-002 jika token rusak.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings dari config.settings.
    """
    mock_load_settings.return_value = MOCK_SETTINGS
    session = {'token': 'invalid.token.signature', 'user_id': 1}
    res = validate_session_token(session)
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-SESSION-002' in res.error_msg


@patch('logic.auth_handler.log_audit_trail')
@patch('logic.auth_handler.reset_failed_login')
@patch('logic.auth_handler.get_pengguna_by_username')
@patch('logic.auth_handler.verify_password')
@patch('middleware.auth_jwt.load_settings')
def test_integrasi_login_menghasilkan_token_yang_bisa_diverifikasi(
    mock_load_settings: MagicMock,
    mock_verify_password: MagicMock,
    mock_get_pengguna: MagicMock,
    mock_reset_failed_login: MagicMock,
    mock_log_audit: MagicMock
) -> None:
    """Menguji integrasi login_user menghasilkan token yang valid dan dapat diverifikasi.

    Args:
        mock_load_settings (MagicMock): Mocking load_settings.
        mock_verify_password (MagicMock): Mocking verify_password.
        mock_get_pengguna (MagicMock): Mocking get_pengguna_by_username.
        mock_reset_failed_login (MagicMock): Mocking reset_failed_login.
        mock_log_audit (MagicMock): Mocking log_audit_trail.
    """
    mock_load_settings.return_value = MOCK_SETTINGS
    mock_verify_password.return_value = True
    
    # Mock return value dari database
    user_db_data = {
        'id': 3,
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': 1,
        'password_hash': '$2b$12$somehashedpasswordplaceholder',
        'locked_until': None,
        'failed_login_attempts': 0
    }
    
    # Import Result dari logic/auth_handler untuk standard tuple
    from logic.auth_handler import Result as AuthResult
    mock_get_pengguna.return_value = AuthResult(True, user_db_data, None)
    
    # Dummy database connection mock
    db_conn = MagicMock()
    
    login_res = login_user('kasir_andi', 'PasswordPolos123', db_conn)
    assert login_res.is_success is True
    session_state = login_res.data
    assert session_state['user_id'] == 3
    assert 'token' in session_state
    
    # Verifikasi token JWT yang diterbitkan saat login
    payload = verify_jwt_session(session_state['token'])
    assert payload is not None
    assert payload['user_id'] == 3
    assert payload['username'] == 'kasir_andi'
