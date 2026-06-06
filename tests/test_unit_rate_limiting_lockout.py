"""
Nama Modul: test_unit_rate_limiting_lockout.py
Deskripsi: Pengujian fungsional unit untuk rate limiting login dengan lockout otomatis
           serta penanganan data kotor pada database.
           (Ref: Issue #0117)
Author: Antigravity
Tanggal: 2026-06-06
"""

import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from logic.auth_handler import login_user, Result


class MockDateTime(datetime):
    _fixed_now = None

    @classmethod
    def now(cls, tz=None):
        if cls._fixed_now is not None:
            if tz is not None:
                # Return static time with timezone if tz is provided
                return cls._fixed_now.replace(tzinfo=tz)
            return cls._fixed_now
        return datetime.now(tz)


@pytest.fixture(autouse=True)
def clean_state():
    MockDateTime._fixed_now = None
    yield
    patch.stopall()
    MockDateTime._fixed_now = None


@pytest.fixture(autouse=True)
def mock_bcrypt_cost_factor(monkeypatch):
    """Fixture untuk meminimalisasi cost factor bcrypt agar mempercepat unit test."""
    monkeypatch.setattr("middleware.auth_jwt.BCRYPT_COST_FACTOR", 4)


@pytest.fixture
def mock_db_conn():
    return MagicMock()


@pytest.fixture
def base_user_data():
    from middleware.auth_jwt import hash_password
    pw_hash = hash_password("ValidPassword123!")
    return {
        'id': 42,
        'nama_lengkap': 'Staf Kasir Teruji',
        'username': 'kasir_uji',
        'password_hash': pw_hash,
        'role': 'kasir',
        'failed_login_attempts': 0,
        'locked_until': None,
        'cabang_id': 1
    }


# ==============================================================================
# Fase B: Skenario Pengujian Positif (Positive Cases)
# ==============================================================================

def test_login_sukses_percobaan_pertama(mock_db_conn, base_user_data):
    """Skenario 1: Login sukses pada percobaan pertama (0 gagal sebelumnya)."""
    user_data = base_user_data.copy()
    user_data['failed_login_attempts'] = 0
    user_data['locked_until'] = None

    patch_get = patch('logic.auth_handler.get_pengguna_by_username', return_value=Result(True, user_data, None))
    patch_reset = patch('logic.auth_handler.reset_failed_login', return_value=Result(True, None, None))
    patch_jwt = patch('logic.auth_handler.create_jwt_session', return_value="mock_jwt_token")
    patch_audit = patch('logic.auth_handler.log_audit_trail')
    patch_verify = patch('logic.auth_handler.verify_password', return_value=True)

    mock_get = patch_get.start()
    mock_reset = patch_reset.start()
    mock_jwt = patch_jwt.start()
    mock_audit = patch_audit.start()
    mock_verify = patch_verify.start()

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    assert res.is_success is True
    assert res.error_msg is None
    assert res.data['token'] == "mock_jwt_token"
    mock_reset.assert_called_once_with(42, mock_db_conn)
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGIN_SUCCESS',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'SUCCESS'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_login_sukses_lockout_expired(mock_db_conn, base_user_data):
    """Skenario 2: Login sukses setelah masa durasi lockout kedaluwarsa (10 menit usai)."""
    T = datetime(2026, 6, 6, 12, 0, 0)
    MockDateTime._fixed_now = T

    user_data = base_user_data.copy()
    user_data['failed_login_attempts'] = 5
    user_data['locked_until'] = T - timedelta(minutes=10, seconds=1)

    patch_datetime = patch('logic.auth_handler.datetime.datetime', MockDateTime)
    patch_get = patch('logic.auth_handler.get_pengguna_by_username', return_value=Result(True, user_data, None))
    patch_reset = patch('logic.auth_handler.reset_failed_login', return_value=Result(True, None, None))
    patch_jwt = patch('logic.auth_handler.create_jwt_session', return_value="mock_jwt_token")
    patch_audit = patch('logic.auth_handler.log_audit_trail')
    patch_verify = patch('logic.auth_handler.verify_password', return_value=True)

    patch_datetime.start()
    mock_get = patch_get.start()
    mock_reset = patch_reset.start()
    mock_jwt = patch_jwt.start()
    mock_audit = patch_audit.start()
    mock_verify = patch_verify.start()

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    assert res.is_success is True
    assert res.error_msg is None
    mock_reset.assert_called_once_with(42, mock_db_conn)
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGIN_SUCCESS',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'SUCCESS'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


# ==============================================================================
# Fase C: Skenario Pengujian Negatif (Negative/Edge Cases)
# ==============================================================================

def test_login_gagal_wajar(mock_db_conn, base_user_data):
    """Skenario 3: Percobaan gagal wajar (Kegagalan ke-1 hingga ke-4)."""
    user_data = base_user_data.copy()
    user_data['failed_login_attempts'] = 2
    user_data['locked_until'] = None

    patch_get = patch('logic.auth_handler.get_pengguna_by_username', return_value=Result(True, user_data, None))
    patch_update = patch('logic.auth_handler.update_failed_login', return_value=Result(True, None, None))
    patch_audit = patch('logic.auth_handler.log_audit_trail')
    patch_verify = patch('logic.auth_handler.verify_password', return_value=False)

    mock_get = patch_get.start()
    mock_update = patch_update.start()
    mock_audit = patch_audit.start()
    mock_verify = patch_verify.start()

    res = login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!'
    mock_update.assert_called_once_with(42, 3, None, mock_db_conn)
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGIN_FAILED',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'FAILED'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_login_gagal_kelima_memicu_lockout(mock_db_conn, base_user_data):
    """Skenario 4: Menembus Batas Maksimal (Percobaan Gagal ke-5)."""
    T = datetime(2026, 6, 6, 12, 0, 0)
    MockDateTime._fixed_now = T

    user_data = base_user_data.copy()
    user_data['failed_login_attempts'] = 4
    user_data['locked_until'] = None

    patch_datetime = patch('logic.auth_handler.datetime.datetime', MockDateTime)
    patch_get = patch('logic.auth_handler.get_pengguna_by_username', return_value=Result(True, user_data, None))
    patch_update = patch('logic.auth_handler.update_failed_login', return_value=Result(True, None, None))
    patch_audit = patch('logic.auth_handler.log_audit_trail')
    patch_verify = patch('logic.auth_handler.verify_password', return_value=False)

    patch_datetime.start()
    mock_get = patch_get.start()
    mock_update = patch_update.start()
    mock_audit = patch_audit.start()
    mock_verify = patch_verify.start()

    res = login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'

    expected_lockout_time = T + timedelta(minutes=10)
    mock_update.assert_called_once_with(42, 5, expected_lockout_time, mock_db_conn)
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='ACCOUNT_LOCKOUT',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'LOCKED'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_login_ditolak_lockout_aktif_sandi_benar(mock_db_conn, base_user_data):
    """Skenario 5: Berusaha login di tengah masa lockout aktif, dengan sandi BENAR."""
    T = datetime(2026, 6, 6, 12, 0, 0)
    MockDateTime._fixed_now = T

    user_data = base_user_data.copy()
    user_data['failed_login_attempts'] = 5
    user_data['locked_until'] = T + timedelta(minutes=5)

    patch_datetime = patch('logic.auth_handler.datetime.datetime', MockDateTime)
    patch_get = patch('logic.auth_handler.get_pengguna_by_username', return_value=Result(True, user_data, None))
    patch_verify = patch('logic.auth_handler.verify_password', return_value=True)
    patch_update = patch('logic.auth_handler.update_failed_login')
    patch_audit = patch('logic.auth_handler.log_audit_trail')

    patch_datetime.start()
    mock_get = patch_get.start()
    mock_verify = patch_verify.start()
    mock_update = patch_update.start()
    mock_audit = patch_audit.start()

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'
    mock_verify.assert_not_called()
    mock_update.assert_not_called()
    mock_audit.assert_not_called()


def test_login_ditolak_lockout_aktif_sandi_salah(mock_db_conn, base_user_data):
    """Skenario 6: Berusaha login di tengah masa lockout aktif, dengan sandi SALAH."""
    T = datetime(2026, 6, 6, 12, 0, 0)
    MockDateTime._fixed_now = T

    user_data = base_user_data.copy()
    user_data['failed_login_attempts'] = 5
    user_data['locked_until'] = T + timedelta(minutes=5)

    patch_datetime = patch('logic.auth_handler.datetime.datetime', MockDateTime)
    patch_get = patch('logic.auth_handler.get_pengguna_by_username', return_value=Result(True, user_data, None))
    patch_verify = patch('logic.auth_handler.verify_password', return_value=False)
    patch_update = patch('logic.auth_handler.update_failed_login')
    patch_audit = patch('logic.auth_handler.log_audit_trail')

    patch_datetime.start()
    mock_get = patch_get.start()
    mock_verify = patch_verify.start()
    mock_update = patch_update.start()
    mock_audit = patch_audit.start()

    res = login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'
    mock_verify.assert_not_called()
    mock_update.assert_not_called()
    mock_audit.assert_not_called()


# ==============================================================================
# Fase D: Validasi Input (Input Validation Handling)
# ==============================================================================

@pytest.mark.parametrize("dirty_attempts", [None, ""])
def test_login_gagal_data_kotor_attempts(mock_db_conn, base_user_data, dirty_attempts):
    """Skenario 7: Data kotor pada akumulasi percobaan gagal (None atau string kosong)."""
    user_data = base_user_data.copy()
    user_data['failed_login_attempts'] = dirty_attempts
    user_data['locked_until'] = None

    patch_get = patch('logic.auth_handler.get_pengguna_by_username', return_value=Result(True, user_data, None))
    patch_update = patch('logic.auth_handler.update_failed_login', return_value=Result(True, None, None))
    patch_verify = patch('logic.auth_handler.verify_password', return_value=False)
    patch_audit = patch('logic.auth_handler.log_audit_trail')

    mock_get = patch_get.start()
    mock_update = patch_update.start()
    mock_verify = patch_verify.start()
    mock_audit = patch_audit.start()

    res = login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!'
    mock_update.assert_called_once_with(42, 1, None, mock_db_conn)


def test_login_ditolak_lockout_aktif_timezone_aware(mock_db_conn, base_user_data):
    """Skenario Tambahan: Lockout aktif dengan locked_until timezone-aware untuk coverage penuh."""
    from datetime import timezone
    T = datetime(2026, 6, 6, 12, 0, 0, tzinfo=timezone.utc)
    MockDateTime._fixed_now = T

    user_data = base_user_data.copy()
    user_data['failed_login_attempts'] = 5
    user_data['locked_until'] = T + timedelta(minutes=5)

    patch_datetime = patch('logic.auth_handler.datetime.datetime', MockDateTime)
    patch_get = patch('logic.auth_handler.get_pengguna_by_username', return_value=Result(True, user_data, None))
    patch_verify = patch('logic.auth_handler.verify_password', return_value=True)
    patch_update = patch('logic.auth_handler.update_failed_login')
    patch_audit = patch('logic.auth_handler.log_audit_trail')

    patch_datetime.start()
    mock_get = patch_get.start()
    mock_verify = patch_verify.start()
    mock_update = patch_update.start()
    mock_audit = patch_audit.start()

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'
    mock_verify.assert_not_called()
    mock_update.assert_not_called()
    mock_audit.assert_not_called()

