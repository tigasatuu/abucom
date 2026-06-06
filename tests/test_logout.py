"""
Nama Modul: test_logout.py
Deskripsi: Unit testing deterministik untuk logika logout pengguna dan pemutusan sesi JWT.
           Menguji skenario positif, validasi input, tipe data salah, dan kegagalan database pada audit trail.
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

from unittest.mock import MagicMock
import pytest
from logic.auth_handler import logout_user, Result


@pytest.fixture
def mock_db_conn():
    """Fixture untuk menyiapkan mock koneksi database."""
    return MagicMock()


def test_logout_user_sukses(mocker, mock_db_conn):
    """Menjamin logout dengan session_state valid berhasil dengan Result(is_success=True)."""
    mocker.patch('logic.auth_handler.log_audit_trail')
    session_state = {
        'user_id': 42,
        'username': 'kasir_uji',
        'role': 'kasir',
        'cabang_id': 1,
        'token': 'mock_token_123'
    }
    res = logout_user(session_state, mock_db_conn)
    assert res.is_success is True
    assert res.data is None
    assert res.error_msg is None


def test_logout_audit_trail_tercatat(mocker, mock_db_conn):
    """Memastikan fungsi pencatat log audit (log_audit_trail) dipanggil dengan tepat saat logout."""
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')
    session_state = {
        'user_id': 42,
        'username': 'kasir_uji',
        'role': 'kasir',
        'cabang_id': 1,
        'token': 'mock_token_123'
    }
    res = logout_user(session_state, mock_db_conn)
    assert res.is_success is True
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGOUT',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'LOGOUT'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_logout_session_kosong_atau_minimal(mocker, mock_db_conn):
    """Menguji jika data sesi yang diteruskan hanya berisi field wajib, memastikan tidak terjadi KeyError."""
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')
    session_state = {
        'user_id': 42,
        'cabang_id': 1
    }
    res = logout_user(session_state, mock_db_conn)
    assert res.is_success is True
    mock_audit.assert_called_once_with(
        pengguna_id=42,
        action_type='LOGOUT',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'LOGOUT'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_logout_user_dengan_session_state_minimal(mocker, mock_db_conn):
    """Alias/tambahan untuk memastikan kompatibilitas penamaan dengan test_logout_user_dengan_session_state_minimal."""
    test_logout_session_kosong_atau_minimal(mocker, mock_db_conn)


@pytest.mark.parametrize("invalid_session, expected_exception", [
    (None, TypeError),
    (12345, TypeError),
    ("invalid_string_session", TypeError),
])
def test_logout_session_state_invalid_type(invalid_session, expected_exception, mock_db_conn):
    """Menjamin error TypeError dilemparkan saat tipe data session_state tidak sesuai."""
    with pytest.raises(expected_exception):
        logout_user(invalid_session, mock_db_conn)


def test_logout_audit_trail_gagal_database_terganggu(mocker, mock_db_conn):
    """Menjamin logout tetap sukses meskipun database terganggu saat menulis audit trail.

    Audit logger menangani exception secara internal, sehingga logout_user() tidak boleh crash
    dan kursor database harus ditutup secara aman.
    """
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = Exception("DB Connection Lost")
    mock_db_conn.cursor.return_value = mock_cursor

    session_state = {
        'user_id': 42,
        'username': 'kasir_uji',
        'role': 'kasir',
        'cabang_id': 1,
        'token': 'mock_token'
    }

    res = logout_user(session_state, mock_db_conn)
    assert res.is_success is True
    # Pastikan cursor ditutup dengan benar di blok finally
    mock_cursor.close.assert_called_once()


def test_logout_user_audit_trail_gagal_database_terganggu(mocker, mock_db_conn):
    """Alias/tambahan untuk memastikan kompatibilitas penamaan dengan test_logout_user_audit_trail_gagal_database_terganggu."""
    test_logout_audit_trail_gagal_database_terganggu(mocker, mock_db_conn)
