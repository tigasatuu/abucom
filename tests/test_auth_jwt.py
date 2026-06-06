"""
Nama Modul: test_auth_jwt.py
Deskripsi: Unit testing komprehensif untuk fitur pembuatan, validasi,
           dan penanganan kedaluwarsa session token JWT saat login.
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

import datetime
import os
from unittest.mock import patch, MagicMock

import jwt
import pytest

from config.settings import AppConfig
from middleware.auth_jwt import (
    create_jwt_session,
    verify_jwt_session,
    validate_session_token,
    hash_password,
    verify_password
)
from logic.auth_handler import login_user, Result as AuthResult

# Mock configurations settings for testing in isolation
MOCK_SETTINGS: AppConfig = AppConfig(
    app_env='development',
    app_cabang_id=1,
    db_host='127.0.0.1',
    db_port=3306,
    db_user='dummy_user',
    db_password='dummy_password',
    db_name='dummy_db',
    db_pool_size=5,
    jwt_secret_key='dummy_secret_key_minimum_32_chars_12345',
    jwt_lifetime_seconds=3600,
    fernet_key='dummy_fernet_key_placeholder_1234567890=',
    backup_zip_password='dummy_backup_password',
    printer_port='COM1',
    printer_width_mm=58
)


@pytest.fixture
def mock_jwt_env(monkeypatch, mocker) -> AppConfig:
    """Fixture untuk mem-mocking settings dan environment secara deterministik.

    Membersihkan lingkungan dan memulihkan state setelah test selesai.
    """
    # Mengatur environment variable palsu
    monkeypatch.setenv("JWT_SECRET_KEY", MOCK_SETTINGS.jwt_secret_key)
    monkeypatch.setenv("JWT_LIFETIME_SECONDS", str(MOCK_SETTINGS.jwt_lifetime_seconds))
    monkeypatch.setenv("DB_PASSWORD", MOCK_SETTINGS.db_password)
    monkeypatch.setenv("FERNET_KEY", MOCK_SETTINGS.fernet_key)
    monkeypatch.setenv("BACKUP_ZIP_PASSWORD", MOCK_SETTINGS.backup_zip_password)

    # Patch load_settings di middleware/auth_jwt agar tidak membaca file .env asli
    mocker.patch('middleware.auth_jwt.load_settings', return_value=MOCK_SETTINGS)

    yield MOCK_SETTINGS


def test_generate_jwt_valid_credentials_sukses(mock_jwt_env: AppConfig) -> None:
    """Memastikan JWT token berbentuk tipe data str yang benar dan dikembalikan saat kredensial valid disuplai."""
    token: str = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    assert isinstance(token, str)
    assert len(token) > 0
    # Verifikasi struktur JWT yang dipisah titik (.) terdiri atas 3 bagian (Header, Payload, Signature)
    parts: list[str] = token.split('.')
    assert len(parts) == 3


def test_jwt_payload_contains_correct_claims(mock_jwt_env: AppConfig) -> None:
    """Memastikan hasil generate token berhasil di-decode ulang dan mengandung payload data mutlak."""
    user_id: int = 1
    username: str = 'kasir_andi'
    role: str = 'kasir'
    cabang_id: int = 1

    token: str = create_jwt_session(
        user_id=user_id,
        username=username,
        role=role,
        cabang_id=cabang_id
    )

    decoded: dict = jwt.decode(token, mock_jwt_env.jwt_secret_key, algorithms=['HS256'])
    assert decoded['user_id'] == user_id
    assert decoded['username'] == username
    assert decoded['role'] == role
    assert decoded['cabang_id'] == cabang_id
    assert 'exp' in decoded
    assert isinstance(decoded['exp'], int)


def test_generate_jwt_invalid_secret_key(mock_jwt_env: AppConfig) -> None:
    """Memastikan error/exception jenis jwt.exceptions.InvalidSignatureError terlempar ketika memverifikasi token yang ditandatangani oleh secret key yang salah/berbeda."""
    token: str = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )

    invalid_secret: str = 'wrong_secret_key_minimum_32_characters_123'
    with pytest.raises(jwt.exceptions.InvalidSignatureError):
        jwt.decode(token, invalid_secret, algorithms=['HS256'])


def test_jwt_token_expiration(mock_jwt_env: AppConfig) -> None:
    """Memastikan fungsionalitas batas waktu kedaluwarsa token benar-benar bekerja.

    Token harus expired setelah Time to Live (TTL) terlewati menggunakan teknik mock time.
    """
    token: str = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )

    # 1. Pastikan token awalnya valid
    payload: dict | None = verify_jwt_session(token)
    assert payload is not None

    # 2. Simulasikan waktu komputasi maju 2 jam (lebih besar dari 1 jam lifetime)
    future_time: datetime.datetime = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)

    class MockDateTime:
        @classmethod
        def now(cls, tz=None):
            return future_time

    # 3. Patch api_jwt.datetime agar decoding menggunakan waktu masa depan
    with patch('jwt.api_jwt.datetime', MockDateTime):
        # Memastikan exception ExpiredSignatureError terjadi saat decode langsung
        with pytest.raises(jwt.exceptions.ExpiredSignatureError):
            jwt.decode(token, mock_jwt_env.jwt_secret_key, algorithms=['HS256'])

        # Memastikan wrapper verify_jwt_session mengembalikan None
        expired_payload: dict | None = verify_jwt_session(token)
        assert expired_payload is None


def test_generate_jwt_with_missing_mandatory_payload(mock_jwt_env: AppConfig) -> None:
    """Memastikan pengujian menangkap error ValueError jika mencoba men-generate JWT namun terdapat parameter esensial yang bernilai None atau kosong."""
    # 1. Parameter role bernilai None
    with pytest.raises(ValueError) as exc_info:
        create_jwt_session(user_id=1, username='kasir_andi', role=None, cabang_id=1)
    assert "Parameter esensial" in str(exc_info.value)

    # 2. Parameter user_id bernilai None
    with pytest.raises(ValueError) as exc_info:
        create_jwt_session(user_id=None, username='kasir_andi', role='kasir', cabang_id=1)
    assert "Parameter esensial" in str(exc_info.value)

    # 3. Parameter username kosong
    with pytest.raises(ValueError) as exc_info:
        create_jwt_session(user_id=1, username='', role='kasir', cabang_id=1)
    assert "Parameter esensial" in str(exc_info.value)


def test_login_empty_input_returns_error(mocker, mock_jwt_env: AppConfig) -> None:
    """Memastikan skenario parameter kosong pada fungsi wrapper login berhasil digagalkan dengan error handling yang proper sebelum masuk ke proses enkripsi JWT."""
    db_conn: MagicMock = MagicMock()

    # Mock DB query user agar tidak dipanggil untuk test username kosong/None
    mock_get_user = mocker.patch('logic.auth_handler.get_pengguna_by_username')

    # 1. Test username kosong ("")
    res_username_empty: AuthResult = login_user("", "PasswordKuat123!", db_conn)
    assert res_username_empty.is_success is False
    assert res_username_empty.data is None
    assert "ERR-AUTH-001" in res_username_empty.error_msg
    mock_get_user.assert_not_called()

    # 2. Test username berupa spasi saja
    res_username_spaces: AuthResult = login_user("   ", "PasswordKuat123!", db_conn)
    assert res_username_spaces.is_success is False
    assert res_username_spaces.data is None
    assert "ERR-AUTH-001" in res_username_spaces.error_msg
    mock_get_user.assert_not_called()

    # 3. Test username bernilai None
    with pytest.raises(TypeError):
        login_user(None, "PasswordKuat123!", db_conn)
    mock_get_user.assert_not_called()

    # Setup mock user data di DB untuk pengujian password kosong
    mock_user = {
        'id': 1,
        'nama_lengkap': 'Kasir Andi',
        'username': 'kasir_andi',
        'password_hash': '$2b$12$somehashedpasswordplaceholder',
        'role': 'kasir',
        'failed_login_attempts': 0,
        'locked_until': None,
        'cabang_id': 1
    }
    mock_get_user.return_value = AuthResult(True, mock_user, None)
    
    def mock_verify_pw(pw_polos, pw_hash):
        if pw_polos is None:
            raise AttributeError("'NoneType' object has no attribute 'encode'")
        return False
        
    mocker.patch('logic.auth_handler.verify_password', side_effect=mock_verify_pw)
    mock_update_failed = mocker.patch('logic.auth_handler.update_failed_login')
    mock_log_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    # 4. Test password kosong ("")
    res_password_empty: AuthResult = login_user("kasir_andi", "", db_conn)
    assert res_password_empty.is_success is False
    assert res_password_empty.data is None
    assert "ERR-AUTH-001" in res_password_empty.error_msg

    # Memastikan update failed login dipanggil (artinya login digagalkan sebelum token JWT diterbitkan)
    mock_update_failed.assert_called_once()
    mock_log_audit.assert_called_once()

    # 5. Test password bernilai None
    with pytest.raises((TypeError, AttributeError)):
        login_user("kasir_andi", None, db_conn)


def test_hash_and_verify_password() -> None:
    """Memverifikasi fungsi hash_password dan verify_password dengan bcrypt."""
    pw = "SandiRahasia123!"
    hashed = hash_password(pw)
    assert isinstance(hashed, str)
    assert hashed != pw
    assert verify_password(pw, hashed) is True
    assert verify_password("SandiSalah", hashed) is False


def test_verify_jwt_session_missing_claims(mock_jwt_env: AppConfig) -> None:
    """Memastikan verify_jwt_session mengembalikan None jika salah satu klaim wajib absen."""
    secret = mock_jwt_env.jwt_secret_key
    base_payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': 1,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    
    # Hapus satu per satu klaim wajib
    for claim in ['user_id', 'username', 'role', 'cabang_id', 'exp']:
        payload = base_payload.copy()
        payload.pop(claim)
        token = jwt.encode(payload, secret, algorithm='HS256')
        assert verify_jwt_session(token) is None


def test_verify_jwt_session_invalid_claim_types(mock_jwt_env: AppConfig) -> None:
    """Memastikan verify_jwt_session mengembalikan None jika tipe data klaim tidak sesuai."""
    secret = mock_jwt_env.jwt_secret_key
    
    # 1. user_id bukan int
    payload = {
        'user_id': '1',  # string instead of int
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': 1,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, secret, algorithm='HS256')
    assert verify_jwt_session(token) is None

    # 2. username bukan str
    payload = {
        'user_id': 1,
        'username': 123,  # int instead of str
        'role': 'kasir',
        'cabang_id': 1,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, secret, algorithm='HS256')
    assert verify_jwt_session(token) is None

    # 3. role bukan str
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': True,  # bool instead of str
        'cabang_id': 1,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, secret, algorithm='HS256')
    assert verify_jwt_session(token) is None

    # 4. cabang_id bukan int
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': '1',  # string instead of int
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, secret, algorithm='HS256')
    assert verify_jwt_session(token) is None


def test_verify_jwt_session_invalid_role(mock_jwt_env: AppConfig) -> None:
    """Memastikan verify_jwt_session mengembalikan None jika peran tidak terdaftar dalam VALID_ROLES."""
    secret = mock_jwt_env.jwt_secret_key
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': 'admin_palsu',  # tidak ada di VALID_ROLES
        'cabang_id': 1,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, secret, algorithm='HS256')
    assert verify_jwt_session(token) is None


def test_validate_session_token_scenarios(mock_jwt_env: AppConfig) -> None:
    """Menguji berbagai skenario fungsi validate_session_token."""
    # Skenario 1: session_state None
    res = validate_session_token(None)
    assert res.is_success is False
    assert res.data is None
    assert "ERR-SESSION-001" in res.error_msg

    # Skenario 2: session_state bukan dict
    res = validate_session_token("bukan_dict")  # type: ignore
    assert res.is_success is False
    assert res.data is None
    assert "ERR-SESSION-001" in res.error_msg

    # Skenario 3: token tidak ada di session_state
    res = validate_session_token({'user_id': 1})
    assert res.is_success is False
    assert res.data is None
    assert "ERR-SESSION-001" in res.error_msg

    # Skenario 4: token kosong/None
    res = validate_session_token({'token': ''})
    assert res.is_success is False
    assert res.data is None
    assert "ERR-SESSION-001" in res.error_msg

    res = validate_session_token({'token': None})
    assert res.is_success is False
    assert res.data is None
    assert "ERR-SESSION-001" in res.error_msg

    # Skenario 5: token tidak valid (gagal verify_jwt_session)
    res = validate_session_token({'token': 'token.invalid.palsu'})
    assert res.is_success is False
    assert res.data is None
    assert "ERR-SESSION-002" in res.error_msg

    # Skenario 6: token valid (sukses)
    token = create_jwt_session(
        user_id=1,
        username='kasir_andi',
        role='kasir',
        cabang_id=1
    )
    res = validate_session_token({'token': token})
    assert res.is_success is True
    assert res.error_msg is None
    assert res.data['user_id'] == 1
    assert res.data['username'] == 'kasir_andi'
    assert res.data['role'] == 'kasir'
