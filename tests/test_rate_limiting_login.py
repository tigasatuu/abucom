"""
Nama Modul: test_rate_limiting_login.py
Deskripsi: Unit testing komprehensif untuk fitur rate limiting login
           dan lockout otomatis (Issue #0116).
           (Ref: Security Design v1.2 Bab 4.3, Test Plan v1.1)
Author: Senior Security Backend Engineer
Tanggal: 2026-06-06
"""

import datetime
from typing import Any
from unittest.mock import MagicMock
import pytest

from logic.auth_handler import login_user, Result


@pytest.fixture(autouse=True)
def mock_bcrypt_cost_factor(monkeypatch: pytest.MonkeyPatch) -> None:
    """Fixture otomatis untuk meminimalkan cost factor bcrypt guna mempercepat pengujian."""
    monkeypatch.setattr("middleware.auth_jwt.BCRYPT_COST_FACTOR", 4)


@pytest.fixture
def mock_db_conn() -> MagicMock:
    """Fixture untuk menyiapkan mock koneksi database MySQL."""
    return MagicMock()


@pytest.fixture
def mock_user_data() -> dict[str, Any]:
    """Fixture untuk menyiapkan data pengguna tiruan dengan hash password bcrypt otentik."""
    from middleware.auth_jwt import hash_password
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


def test_login_sukses_reset_counter_dan_lockout(
    mocker: Any,
    mock_user_data: dict[str, Any],
    mock_db_conn: MagicMock
) -> None:
    """Test 1: Login sukses — password benar, counter dan lockout harus di-reset."""
    # Setup state: sebelumnya ada 3 kali kegagalan login
    mock_user_data['failed_login_attempts'] = 3
    mock_user_data['locked_until'] = None

    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_reset = mocker.patch('logic.auth_handler.reset_failed_login', return_value=Result(True, None, None))
    mock_jwt = mocker.patch('logic.auth_handler.create_jwt_session', return_value="mock_token_abc123")
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    # Assertions
    assert res.is_success is True
    assert res.error_msg is None
    assert res.data['token'] == 'mock_token_abc123'
    
    # Reset dipanggil untuk membersihkan counter
    mock_reset.assert_called_once_with(42, mock_db_conn)
    
    # Audit log LOGIN_SUCCESS dicatat
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGIN_SUCCESS',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'SUCCESS'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_login_gagal_percobaan_pertama(
    mocker: Any,
    mock_user_data: dict[str, Any],
    mock_db_conn: MagicMock
) -> None:
    """Test 2: Login gagal — password salah, percobaan pertama (counter 0 -> 1)."""
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_update = mocker.patch('logic.auth_handler.update_failed_login', return_value=Result(True, None, None))
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    res = login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!'
    
    # Counter diubah menjadi 1
    mock_update.assert_called_once_with(42, 1, None, mock_db_conn)
    
    # Audit log LOGIN_FAILED dicatat
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGIN_FAILED',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'FAILED'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_login_gagal_percobaan_keempat(
    mocker: Any,
    mock_user_data: dict[str, Any],
    mock_db_conn: MagicMock
) -> None:
    """Test 3: Login gagal — password salah, percobaan ke-4 (counter 3 -> 4)."""
    mock_user_data['failed_login_attempts'] = 3

    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_update = mocker.patch('logic.auth_handler.update_failed_login', return_value=Result(True, None, None))
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    res = login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!'
    
    # Counter diubah menjadi 4
    mock_update.assert_called_once_with(42, 4, None, mock_db_conn)
    
    # Audit log LOGIN_FAILED dicatat
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGIN_FAILED',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'FAILED'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_login_gagal_percobaan_kelima_memicu_lockout(
    mocker: Any,
    mock_user_data: dict[str, Any],
    mock_db_conn: MagicMock
) -> None:
    """Test 4: Login gagal — password salah, percobaan ke-5 (counter 4 -> 5, LOCKOUT TERPICU)."""
    mock_user_data['failed_login_attempts'] = 4

    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_update = mocker.patch('logic.auth_handler.update_failed_login', return_value=Result(True, None, None))
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    res = login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'
    
    # Verifikasi pemanggilan update status lockout
    mock_update.assert_called_once()
    args, _ = mock_update.call_args
    assert args[0] == 42  # user_id
    assert args[1] == 5   # attempts (maksimal lockout threshold)
    assert isinstance(args[2], datetime.datetime)  # locked_until timestamp
    
    # Audit log ACCOUNT_LOCKOUT dicatat
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='ACCOUNT_LOCKOUT',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'LOCKED'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_login_ditolak_lockout_masih_aktif(
    mocker: Any,
    mock_user_data: dict[str, Any],
    mock_db_conn: MagicMock
) -> None:
    """Test 5: Login ditolak — akun sedang terkunci (lockout masih aktif)."""
    # Mengunci akun sampai 10 menit ke depan
    mock_user_data['locked_until'] = datetime.datetime.now() + datetime.timedelta(minutes=10)
    mock_user_data['failed_login_attempts'] = 5

    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_verify = mocker.patch('logic.auth_handler.verify_password')
    mock_update = mocker.patch('logic.auth_handler.update_failed_login')
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!'
    
    # Password verification & DB writes must not be called
    mock_verify.assert_not_called()
    mock_update.assert_not_called()
    mock_audit.assert_not_called()


def test_login_sukses_lockout_sudah_expired(
    mocker: Any,
    mock_user_data: dict[str, Any],
    mock_db_conn: MagicMock
) -> None:
    """Test 6: Login sukses — lockout sudah expired (locked_until < now)."""
    # Lockout terjadi 11 menit lalu (sehingga sudah kadaluarsa)
    mock_user_data['locked_until'] = datetime.datetime.now() - datetime.timedelta(minutes=11)
    mock_user_data['failed_login_attempts'] = 5

    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_reset = mocker.patch('logic.auth_handler.reset_failed_login', return_value=Result(True, None, None))
    mock_jwt = mocker.patch('logic.auth_handler.create_jwt_session', return_value="mock_token_abc123")
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    assert res.is_success is True
    assert res.error_msg is None
    
    # Reset counter dan locked_until di database
    mock_reset.assert_called_once_with(42, mock_db_conn)
    
    # Audit log LOGIN_SUCCESS dicatat
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGIN_SUCCESS',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'SUCCESS'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_login_gagal_username_tidak_ditemukan(
    mocker: Any,
    mock_db_conn: MagicMock
) -> None:
    """Test 7: Login gagal — username tidak ditemukan (timing attack prevention)."""
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(False, None, None)
    )

    res = login_user('nonexistent_user', 'SomePassword123!', mock_db_conn)

    # Harus mengembalikan pesan error generic yang sama demi keamanan
    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!'


@pytest.mark.parametrize("invalid_username", [
    "",
    "   ",
])
def test_login_gagal_username_kosong_atau_whitespace(
    invalid_username: str,
    mock_db_conn: MagicMock
) -> None:
    """Test 8: Login gagal — username kosong atau hanya whitespace."""
    res = login_user(invalid_username, 'ValidPassword123!', mock_db_conn)
    
    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!'


def test_login_gagal_username_terlalu_panjang(
    mock_db_conn: MagicMock
) -> None:
    """Test 9: Login gagal — username melebihi batas panjang (> 50 karakter)."""
    long_username = "a" * 51
    res = login_user(long_username, 'ValidPassword123!', mock_db_conn)
    
    assert res.is_success is False
    assert res.error_msg == 'ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!'


def test_login_sukses_setelah_beberapa_kali_gagal(
    mocker: Any,
    mock_user_data: dict[str, Any],
    mock_db_conn: MagicMock
) -> None:
    """Test 10: Login sukses setelah beberapa kali gagal (counter > 0 lalu sukses)."""
    # Pengguna sebelumnya gagal 4 kali
    mock_user_data['failed_login_attempts'] = 4

    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_reset = mocker.patch('logic.auth_handler.reset_failed_login', return_value=Result(True, None, None))
    mock_jwt = mocker.patch('logic.auth_handler.create_jwt_session', return_value="mock_token_abc123")
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    assert res.is_success is True
    
    # reset_failed_login dipanggil untuk mengembalikan counter ke 0
    mock_reset.assert_called_once_with(42, mock_db_conn)


def test_login_gagal_database_error(
    mocker: Any,
    mock_db_conn: MagicMock
) -> None:
    """Test 11: Login gagal — database error saat query user."""
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(False, None, 'ERR-DB-001: Kegagalan Database')
    )

    res = login_user('kasir_uji', 'ValidPassword123!', mock_db_conn)

    assert res.is_success is False
    assert res.error_msg == 'ERR-DB-001: Kegagalan Database'


def test_login_sanitasi_username_ascii_kontrol(
    mocker: Any,
    mock_user_data: dict[str, Any],
    mock_db_conn: MagicMock
) -> None:
    """Test 12: Sanitasi input — username mengandung karakter kontrol ASCII."""
    # Username kotor mengandung escape character (\x1b)
    dirty_username = '\x1b[31mkasir_uji\x1b[0m'
    
    mock_get_pengguna = mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mocker.patch('logic.auth_handler.reset_failed_login', return_value=Result(True, None, None))
    mocker.patch('logic.auth_handler.create_jwt_session', return_value="mock_token_abc123")
    mocker.patch('logic.auth_handler.log_audit_trail')

    # Login harus memanggil db repository dengan username yang disanitasi
    # (\x1b dibuang, menyisakan [31mkasir_uji[0m)
    login_user(dirty_username, 'ValidPassword123!', mock_db_conn)
    
    mock_get_pengguna.assert_called_once_with('[31mkasir_uji[0m', mock_db_conn)


def test_login_audit_trail_format_json(
    mocker: Any,
    mock_user_data: dict[str, Any],
    mock_db_conn: MagicMock
) -> None:
    """Test 13: Audit trail — verifikasi format JSON pada old_value dan new_value."""
    mocker.patch(
        'logic.auth_handler.get_pengguna_by_username',
        return_value=Result(True, mock_user_data, None)
    )
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')

    # Skenario 1: LOGIN_FAILED
    login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)
    mock_audit.assert_called_with(
        pengguna_id=42,
        action_type='LOGIN_FAILED',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'FAILED'},
        cabang_id=1,
        db_connection=mock_db_conn
    )

    # Skenario 2: ACCOUNT_LOCKOUT (kegagalan ke-5)
    mock_user_data['failed_login_attempts'] = 4
    mocker.patch('logic.auth_handler.update_failed_login', return_value=Result(True, None, None))
    
    login_user('kasir_uji', 'WrongPassword123!', mock_db_conn)
    mock_audit.assert_called_with(
        pengguna_id=42,
        action_type='ACCOUNT_LOCKOUT',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'LOCKED'},
        cabang_id=1,
        db_connection=mock_db_conn
    )
