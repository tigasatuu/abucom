"""
Nama Modul: test_ubah_password.py
Deskripsi: Test suite unit testing untuk fitur ubah password akun sendiri (UC-044).
Author: Antigravity (STK-015)
Tanggal: 2026-06-07
"""

import pytest
from unittest.mock import MagicMock, patch
from collections import namedtuple

from logic.pengguna import ubah_password_akun

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


@pytest.fixture
def dummy_session_state() -> dict:
    """Fixture untuk mensimulasikan session state aktif (dummy JWT claims)."""
    return {
        'token': 'dummy_jwt_token_claims_here',
        'user_id': 1,
        'username': 'pemilik_toko',
        'role': 'pemilik',
        'cabang_id': 1
    }


@pytest.fixture
def mock_db_conn():
    """Fixture untuk menyediakan mock db connection."""
    return MagicMock()


def test_ubah_password_sukses(mock_db_conn) -> None:
    """Skenario Positif: Password lama valid, password baru kuat dan sesuai policy, konfirmasi cocok."""
    from middleware.auth_jwt import hash_password
    
    password_lama = "SandiLama123!"
    old_hash = hash_password(password_lama)
    
    with patch('logic.pengguna.get_password_hash_by_id') as mock_get_hash, \
         patch('logic.pengguna.update_password_hash') as mock_update, \
         patch('middleware.audit_logger.log_audit_trail') as mock_audit:
        
        mock_get_hash.return_value = Result(True, old_hash, None)
        mock_update.return_value = Result(True, None, None)
        
        result = ubah_password_akun(
            user_id=1,
            password_lama=password_lama,
            password_baru="SandiBaru123!",
            konfirmasi_password="SandiBaru123!",
            cabang_id=1,
            db_conn=mock_db_conn
        )
        
        assert result.is_success is True
        assert result.data == {'action': 'PASSWORD_CHANGED'}
        assert result.error_msg is None
        
        # Asert get_password_hash_by_id dipanggil dengan parameter benar
        mock_get_hash.assert_called_once_with(1, mock_db_conn)
        
        # Asert update_password_hash dipanggil dengan user_id, hash baru, dan koneksi
        mock_update.assert_called_once()
        called_args = mock_update.call_args[0]
        assert called_args[0] == 1
        new_hash = called_args[1]
        
        # Pastikan hash baru adalah bcrypt valid (diawali dengan $2b$12$)
        assert isinstance(new_hash, str)
        assert new_hash.startswith('$2b$12$')
        assert called_args[2] == mock_db_conn
        
        # Asert audit log tercatat
        mock_audit.assert_called_once()


def test_ubah_password_gagal_sandi_lama_salah(mock_db_conn) -> None:
    """Skenario Negatif: Password lama tidak cocok dengan hash database (ERR-AUTH)."""
    from middleware.auth_jwt import hash_password
    old_hash = hash_password("SandiLama123!")
    
    with patch('logic.pengguna.get_password_hash_by_id') as mock_get_hash:
        mock_get_hash.return_value = Result(True, old_hash, None)
        
        result = ubah_password_akun(
            user_id=1,
            password_lama="SandiLamaSalah!",
            password_baru="SandiBaru123!",
            konfirmasi_password="SandiBaru123!",
            cabang_id=1,
            db_conn=mock_db_conn
        )
        
        assert result.is_success is False
        assert result.data is None
        assert "ERR-AUTH" in result.error_msg
        assert "Kata sandi lama yang Anda masukkan tidak valid" in result.error_msg


def test_ubah_password_gagal_konfirmasi_tidak_cocok(mock_db_conn) -> None:
    """Skenario Negatif: Konfirmasi password baru tidak cocok dengan password baru."""
    result = ubah_password_akun(
        user_id=1,
        password_lama="SandiLama123!",
        password_baru="SandiBaru123!",
        konfirmasi_password="SandiLainnya123!",
        cabang_id=1,
        db_conn=mock_db_conn
    )
    
    assert result.is_success is False
    assert result.data is None
    assert "ERR-VAL-044" in result.error_msg
    assert "cocok pada kedua input" in result.error_msg


def test_ubah_password_gagal_sandi_baru_sama_dengan_lama(mock_db_conn) -> None:
    """Skenario Negatif: Password baru sama dengan password lama."""
    from middleware.auth_jwt import hash_password
    old_hash = hash_password("SandiSama123!")
    
    with patch('logic.pengguna.get_password_hash_by_id') as mock_get_hash:
        mock_get_hash.return_value = Result(True, old_hash, None)
        
        result = ubah_password_akun(
            user_id=1,
            password_lama="SandiSama123!",
            password_baru="SandiSama123!",
            konfirmasi_password="SandiSama123!",
            cabang_id=1,
            db_conn=mock_db_conn
        )
        
        assert result.is_success is False
        assert result.data is None
        assert "ERR-VAL-044" in result.error_msg
        assert "tidak boleh sama dengan kata sandi lama" in result.error_msg


def test_ubah_password_gagal_input_kosong(mock_db_conn) -> None:
    """Validasi Input: String kosong, None, atau whitespace murni pada parameter input."""
    # Test cases untuk berbagai variasi input kosong/tidak valid
    empty_scenarios = [
        # (password_lama, password_baru, konfirmasi_password)
        ("", "SandiBaru123!", "SandiBaru123!"),
        ("SandiLama123!", "", ""),
        ("SandiLama123!", "SandiBaru123!", ""),
        ("   ", "SandiBaru123!", "SandiBaru123!"),
        ("SandiLama123!", "   ", "   "),
        (None, "SandiBaru123!", "SandiBaru123!"),
        ("SandiLama123!", None, "SandiBaru123!"),
        ("SandiLama123!", "SandiBaru123!", None),
    ]
    
    for old, new, confirm in empty_scenarios:
        result = ubah_password_akun(
            user_id=1,
            password_lama=old,
            password_baru=new,
            konfirmasi_password=confirm,
            cabang_id=1,
            db_conn=mock_db_conn
        )
        
        assert result.is_success is False
        assert result.data is None
        assert "ERR-VAL-044" in result.error_msg
        assert "tidak boleh kosong" in result.error_msg or "harus berupa teks/string" in result.error_msg


def test_ubah_password_gagal_panjang_minimal(mock_db_conn) -> None:
    """Validasi Input: Password baru kurang dari batas minimal karakter (< 8 karakter)."""
    result = ubah_password_akun(
        user_id=1,
        password_lama="SandiLama123!",
        password_baru="P@ss1",
        konfirmasi_password="P@ss1",
        cabang_id=1,
        db_conn=mock_db_conn
    )
    
    assert result.is_success is False
    assert result.data is None
    assert "ERR-VAL-044" in result.error_msg
    assert "minimal harus 8 karakter" in result.error_msg


def test_ubah_password_gagal_melebihi_batas_maksimal(mock_db_conn) -> None:
    """Validasi Input: Password baru melebihi limit batas logis normal (> 128 karakter)."""
    too_long_password = "A" * 129
    result = ubah_password_akun(
        user_id=1,
        password_lama="SandiLama123!",
        password_baru=too_long_password,
        konfirmasi_password=too_long_password,
        cabang_id=1,
        db_conn=mock_db_conn
    )
    
    assert result.is_success is False
    assert result.data is None
    assert "ERR-VAL-044" in result.error_msg
    assert "melebihi batas maksimum 128 karakter" in result.error_msg


def test_ubah_password_gagal_lemah(mock_db_conn) -> None:
    """Validasi Input: Password baru lemah (tidak memenuhi kriteria karakter)."""
    result = ubah_password_akun(
        user_id=1,
        password_lama="SandiLama123!",
        password_baru="lemahlemah",
        konfirmasi_password="lemahlemah",
        cabang_id=1,
        db_conn=mock_db_conn
    )
    
    assert result.is_success is False
    assert result.data is None
    assert "ERR-VAL-001" in result.error_msg
    assert "Sandi Lemah" in result.error_msg


def test_ubah_password_db_error(mock_db_conn) -> None:
    """Skenario Database Error: Terjadi error pada repository saat mengambil hash."""
    with patch('logic.pengguna.get_password_hash_by_id') as mock_get_hash:
        mock_get_hash.return_value = Result(False, None, 'ERR-DB-003: Database connection timeout')
        
        result = ubah_password_akun(
            user_id=1,
            password_lama="SandiLama123!",
            password_baru="SandiBaru123!",
            konfirmasi_password="SandiBaru123!",
            cabang_id=1,
            db_conn=mock_db_conn
        )
        
        assert result.is_success is False
        assert result.data is None
        assert "ERR-DB-003" in result.error_msg


def test_ubah_password_gagal_update_db_error(mock_db_conn) -> None:
    """Skenario Database Error: Terjadi error pada repository saat memperbarui hash."""
    from middleware.auth_jwt import hash_password
    old_hash = hash_password("SandiLama123!")
    
    with patch('logic.pengguna.get_password_hash_by_id') as mock_get_hash, \
         patch('logic.pengguna.update_password_hash') as mock_update:
        
        mock_get_hash.return_value = Result(True, old_hash, None)
        mock_update.return_value = Result(False, None, 'ERR-DB-004: Update failed')
        
        result = ubah_password_akun(
            user_id=1,
            password_lama="SandiLama123!",
            password_baru="SandiBaru123!",
            konfirmasi_password="SandiBaru123!",
            cabang_id=1,
            db_conn=mock_db_conn
        )
        
        assert result.is_success is False
        assert result.data is None
        assert "ERR-DB-004" in result.error_msg
