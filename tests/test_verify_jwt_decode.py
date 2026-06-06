"""
Nama Modul: test_verify_jwt_decode.py
Deskripsi: Unit test untuk validasi dan dekode session token JWT,
           mencakup validasi kelengkapan payload, tipe data klaim,
           dan keabsahan role pengguna.
           (Ref: Issue #0112)
Author: Antigravity
Tanggal: 2026-06-06
"""

import datetime
import jwt
import pytest
from config.settings import AppConfig
from middleware.auth_jwt import (
    verify_jwt_session,
    validate_session_token
)

# Mock configurations settings for testing in isolation
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


@pytest.fixture
def mock_jwt_env(monkeypatch, mocker) -> AppConfig:
    """Fixture untuk mem-mocking settings dan environment secara deterministik."""
    monkeypatch.setenv("JWT_SECRET_KEY", MOCK_SETTINGS.jwt_secret_key)
    monkeypatch.setenv("JWT_LIFETIME_SECONDS", str(MOCK_SETTINGS.jwt_lifetime_seconds))
    mocker.patch('middleware.auth_jwt.load_settings', return_value=MOCK_SETTINGS)
    yield MOCK_SETTINGS


def _buat_token_kustom(payload: dict, secret_key: str) -> str:
    """Helper untuk membuat token JWT kustom dengan payload tertentu."""
    return jwt.encode(payload, secret_key, algorithm='HS256')


# =====================================================================
# 1. TEST VALIDASI KELENGKAPAN PAYLOAD
# =====================================================================

def test_verify_jwt_tolak_token_tanpa_klaim_user_id(mock_jwt_env: AppConfig) -> None:
    """Memastikan token tanpa klaim user_id ditolak."""
    payload = {
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


def test_verify_jwt_tolak_token_tanpa_klaim_username(mock_jwt_env: AppConfig) -> None:
    """Memastikan token tanpa klaim username ditolak."""
    payload = {
        'user_id': 1,
        'role': 'kasir',
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


def test_verify_jwt_tolak_token_tanpa_klaim_role(mock_jwt_env: AppConfig) -> None:
    """Memastikan token tanpa klaim role ditolak."""
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


def test_verify_jwt_tolak_token_tanpa_klaim_cabang_id(mock_jwt_env: AppConfig) -> None:
    """Memastikan token tanpa klaim cabang_id ditolak."""
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': 'kasir',
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


def test_verify_jwt_tolak_token_tanpa_klaim_exp(mock_jwt_env: AppConfig) -> None:
    """Memastikan token tanpa klaim exp ditolak."""
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': 1
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


# =====================================================================
# 2. TEST VALIDASI TIPE DATA KLAIM
# =====================================================================

def test_verify_jwt_tolak_user_id_string(mock_jwt_env: AppConfig) -> None:
    """Memastikan token dengan user_id bertipe string ditolak."""
    payload = {
        'user_id': '1',  # string, harusnya int
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


def test_verify_jwt_tolak_cabang_id_string(mock_jwt_env: AppConfig) -> None:
    """Memastikan token dengan cabang_id bertipe string ditolak."""
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': '1',  # string, harusnya int
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


def test_verify_jwt_tolak_role_integer(mock_jwt_env: AppConfig) -> None:
    """Memastikan token dengan role bertipe integer ditolak."""
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': 123,  # int, harusnya str
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


def test_verify_jwt_tolak_username_integer(mock_jwt_env: AppConfig) -> None:
    """Memastikan token dengan username bertipe integer ditolak."""
    payload = {
        'user_id': 1,
        'username': 123,  # int, harusnya str
        'role': 'kasir',
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


# =====================================================================
# 3. TEST VALIDASI ROLE TERHADAP DAFTAR VALID
# =====================================================================

def test_verify_jwt_tolak_role_tidak_valid(mock_jwt_env: AppConfig) -> None:
    """Memastikan token dengan role tidak valid (e.g. 'admin') ditolak."""
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': 'admin',  # Tidak ada di daftar 8 peran valid
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


def test_verify_jwt_tolak_role_kosong(mock_jwt_env: AppConfig) -> None:
    """Memastikan token dengan role berupa string kosong ditolak."""
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': '',
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None


def test_verify_jwt_terima_seluruh_8_role_valid(mock_jwt_env: AppConfig) -> None:
    """Memastikan seluruh 8 peran valid diterima tanpa kendala."""
    roles = [
        'pemilik',
        'kepala_percetakan',
        'pramuniaga',
        'kasir',
        'desainer',
        'produksi_cetak',
        'fotocopy_print',
        'gudang'
    ]
    for role in roles:
        payload = {
            'user_id': 1,
            'username': 'kasir_andi',
            'role': role,
            'cabang_id': 1,
            'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
        }
        token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
        result = verify_jwt_session(token)
        assert result is not None
        assert result['role'] == role


# =====================================================================
# 4. TEST TOKEN VALID (POSITIVE CASE)
# =====================================================================

def test_verify_jwt_token_valid_mengembalikan_payload_lengkap(mock_jwt_env: AppConfig) -> None:
    """Memastikan token yang valid mengembalikan dictionary payload yang lengkap."""
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is not None
    assert result['user_id'] == 1
    assert result['username'] == 'kasir_andi'
    assert result['role'] == 'kasir'
    assert result['cabang_id'] == 1
    assert 'exp' in result


# =====================================================================
# 5. TEST INTEGRASI DENGAN validate_session_token()
# =====================================================================

def test_validate_session_token_payload_tidak_lengkap_return_err_session_002(mock_jwt_env: AppConfig) -> None:
    """Memastikan token tanpa klaim lengkap menghasilkan Result gagal dengan ERR-SESSION-002."""
    payload = {
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    session_state = {'token': token, 'user_id': 1}
    result = validate_session_token(session_state)
    assert result.is_success is False
    assert result.data is None
    assert 'ERR-SESSION-002' in result.error_msg


def test_validate_session_token_role_tidak_valid_return_err_session_002(mock_jwt_env: AppConfig) -> None:
    """Memastikan token dengan role tidak valid menghasilkan Result gagal dengan ERR-SESSION-002."""
    payload = {
        'user_id': 1,
        'username': 'kasir_andi',
        'role': 'super_admin',  # invalid role
        'cabang_id': 1,
        'exp': int((datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)).timestamp())
    }
    token = _buat_token_kustom(payload, mock_jwt_env.jwt_secret_key)
    session_state = {'token': token, 'user_id': 1}
    result = validate_session_token(session_state)
    assert result.is_success is False
    assert result.data is None
    assert 'ERR-SESSION-002' in result.error_msg
