"""
Nama Modul: test_login_bcrypt.py
Deskripsi: Unit testing deterministik untuk logika login pengguna, logout, dan verifikasi password bcrypt.
           Menguji skenario positif, negatif, dan berbagai kasus batas (edge cases).
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

import datetime
from unittest.mock import MagicMock
import bcrypt
import pytest

from logic.auth_handler import login_user, Result


@pytest.fixture(autouse=True)
def mock_bcrypt_cost_factor(monkeypatch):
    """Fixture otomatis untuk meminimalkan cost factor bcrypt guna mempercepat pengujian."""
    monkeypatch.setattr("middleware.auth_jwt.BCRYPT_COST_FACTOR", 4)


@pytest.fixture
def mock_db_conn():
    """Fixture untuk menyiapkan mock koneksi database."""
    return MagicMock()


@pytest.fixture
def mock_user_data():
    """Fixture untuk menyiapkan data pengguna tiruan dengan hash password bcrypt otentik."""
    from middleware.auth_jwt import hash_password
    # Generate hash otentik menggunakan cost factor 4 yang sudah di-mock
    valid_password = "ValidPassword123!"
    pw_hash = hash_password(valid_password)
    
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


def test_login_berhasil_dengan_kredensial_valid(mocker, mock_user_data, mock_db_conn):
    """Menjamin login berhasil ketika username dan password valid disandingkan."""
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_reset = mocker.patch('logic.auth_handler.reset_failed_login', return_value=Result(True, None, None))
    mock_jwt = mocker.patch('logic.auth_handler.create_jwt_session', return_value="mock_token_abc123")
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    # Assertion hasil login
    assert res.is_success is True
    assert res.error_msg is None
    assert res.data['user_id'] == 42
    assert res.data['username'] == 'kasir_uji'
    assert res.data['role'] == 'kasir'
    assert res.data['cabang_id'] == 1
    assert res.data['token'] == 'mock_token_abc123'

    # Assertion parameter rahasia tidak bocor
    assert 'password_hash' not in res.data
    assert 'password' not in res.data

    # Assertion interaksi fungsi eksternal
    mock_reset.assert_called_once_with(42, mock_db_conn)
    mock_jwt.assert_called_once_with(user_id=42, username='kasir_uji', role='kasir', cabang_id=1)
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGIN_SUCCESS',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'SUCCESS'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_login_gagal_karena_password_salah(mocker, mock_user_data, mock_db_conn):
    """Menjamin login ditolak dengan error otentikasi saat password salah."""
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_update = mocker.patch('logic.auth_handler.update_failed_login', return_value=Result(True, None, None))
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    res = login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)

    # Assertion hasil kegagalan login
    assert res.is_success is False
    assert res.data is None
    assert res.error_msg == 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!'

    # Pembuktian update counter kegagalan (+1)
    mock_update.assert_called_once_with(42, 1, None, mock_db_conn)
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGIN_FAILED',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'FAILED'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_login_gagal_user_tidak_ditemukan(mocker, mock_db_conn):
    """Menjamin login ditolak dengan error otentikasi saat username tidak ditemukan di database."""
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(False, None, None)
    )

    res = login_user('nonexistent_user', 'SomePassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.data is None
    assert res.error_msg == 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!'


def test_login_gagal_database_error(mocker, mock_db_conn):
    """Menjamin error database dipropagasikan keluar dengan benar."""
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(False, None, 'ERR-DB-001: Kegagalan Database')
    )

    res = login_user('kasir_uji', 'SomePassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.data is None
    assert res.error_msg == 'ERR-DB-001: Kegagalan Database'


def test_login_gagal_karena_akun_terkunci(mocker, mock_user_data, mock_db_conn):
    """Menjamin login langsung ditolak jika akun masih dalam masa penangguhan lockout."""
    mock_user_data['locked_until'] = datetime.datetime.now() + datetime.timedelta(minutes=10)
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.data is None
    assert res.error_msg == 'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'


def test_login_gagal_karena_akun_terkunci_dengan_timezone(mocker, mock_user_data, mock_db_conn):
    """Menjamin login ditolak jika akun terkunci dengan timestamp ber-timezone (UTC)."""
    mock_user_data['locked_until'] = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.data is None
    assert res.error_msg == 'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'


def test_login_gagal_memicu_lockout_pada_percobaan_kelima(mocker, mock_user_data, mock_db_conn):
    """Menjamin akun terkunci otomatis selama 10 menit setelah 5 kali gagal login berturut-turut."""
    mock_user_data['failed_login_attempts'] = 4  # Percobaan ke-5
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_update = mocker.patch('logic.auth_handler.update_failed_login', return_value=Result(True, None, None))
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    res = login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'

    # Verifikasi update status lockout di database
    mock_update.assert_called_once()
    args, kwargs = mock_update.call_args
    assert args[0] == 42  # user_id
    assert args[1] == 5   # attempts
    assert isinstance(args[2], datetime.datetime)  # locked_until timestamp
    assert args[3] == mock_db_conn

    # Verifikasi audit log mencatat lockout
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='ACCOUNT_LOCKOUT',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'LOCKED'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


@pytest.mark.parametrize("invalid_username", [
    "",
    "   ",
    "A" * 51,  # Melebihi batas panjang kolom username (50)
])
def test_login_username_invalid_edge_cases(invalid_username, mock_db_conn):
    """Menjamin penolakan login saat username kosong atau terlalu panjang secara terstandarisasi."""
    res = login_user(invalid_username, "ValidPassword123!", mock_db_conn)
    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!'


@pytest.mark.parametrize("invalid_username, expected_exception", [
    (None, TypeError),
    (12345, TypeError),
])
def test_login_username_tipe_data_tidak_sesuai(invalid_username, expected_exception, mock_db_conn):
    """Menjamin error dilemparkan saat tipe data username tidak sesuai."""
    with pytest.raises(expected_exception):
        login_user(invalid_username, "ValidPassword123!", mock_db_conn)


@pytest.mark.parametrize("invalid_password, expected_exception", [
    (None, (TypeError, AttributeError)),
    (12345, (TypeError, AttributeError)),
])
def test_login_password_tipe_data_tidak_sesuai(mocker, mock_user_data, mock_db_conn, invalid_password, expected_exception):
    """Menjamin error dilemparkan saat tipe data password tidak sesuai."""
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    with pytest.raises(expected_exception):
        login_user('kasir_uji', invalid_password, mock_db_conn)


def test_login_password_melebihi_batas_internal_bcrypt_72_bytes(mocker, mock_db_conn):
    """Menjamin password panjang (>72 bytes) dipotong menjadi 72 bytes dan terverifikasi sukses."""
    from middleware.auth_jwt import hash_password
    
    # Buat password 80 karakter (melebihi 72 bytes limit)
    long_pwd = "A" * 80
    long_pwd_hash = hash_password(long_pwd)
    
    user_data = {
        'id': 42,
        'nama_lengkap': 'Staf Kasir Teruji',
        'username': 'kasir_uji',
        'password_hash': long_pwd_hash,
        'role': 'kasir',
        'failed_login_attempts': 0,
        'locked_until': None,
        'cabang_id': 1
    }

    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, user_data, None)
    )
    mocker.patch('logic.auth_handler.reset_failed_login', return_value=Result(True, None, None))
    mocker.patch('logic.auth_handler.create_jwt_session', return_value="mock_token_abc123")
    mocker.patch('logic.auth_handler.log_audit_trail')

    # Login dengan password 80 karakter penuh harus berhasil
    res = login_user('kasir_uji', long_pwd, mock_db_conn)
    assert res.is_success is True

    # Login dengan password 72 karakter pertama saja juga harus berhasil (menandakan pemotongan 72 bytes)
    res_truncated = login_user('kasir_uji', "A" * 72, mock_db_conn)
    assert res_truncated.is_success is True


def test_login_gagal_password_hash_database_rusak_atau_malformed(mocker, mock_user_data, mock_db_conn):
    """Menjamin ValueError dilemparkan oleh bcrypt jika hash di database rusak/malformed."""
    mock_user_data['password_hash'] = 'malformed_invalid_hash_string'
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )

    with pytest.raises(ValueError):
        login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)


