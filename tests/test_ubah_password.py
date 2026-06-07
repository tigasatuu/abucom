"""
Nama Modul: test_ubah_password.py
Deskripsi: Test suite unit testing untuk fitur ubah password akun sendiri (UC-044).
Author: Antigravity (STK-015)
Tanggal: 2026-06-07
"""

import unittest
from unittest.mock import MagicMock, patch
from collections import namedtuple

from logic.pengguna import ubah_password_akun

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


class TestUbahPasswordAkun(unittest.TestCase):
    """Test cases untuk fungsi ubah_password_akun() di logic/pengguna.py."""

    def test_ubah_password_sukses(self) -> None:
        """Password lama valid, password baru kuat dan berbeda dari password lama -> Result sukses."""
        mock_conn = MagicMock()

        with patch('logic.pengguna.get_password_hash_by_id') as mock_get_hash, \
             patch('middleware.auth_jwt.verify_password') as mock_verify, \
             patch('middleware.auth_jwt.hash_password') as mock_hash, \
             patch('logic.pengguna.update_password_hash') as mock_update, \
             patch('middleware.audit_logger.log_audit_trail') as mock_audit:

            mock_get_hash.return_value = Result(True, 'old_hashed_password', None)

            # mock_verify called twice:
            # 1. verify_password(password_lama, current_hash) -> True
            # 2. verify_password(password_baru, current_hash) -> False
            mock_verify.side_effect = [True, False]
            mock_hash.return_value = 'new_hashed_password'
            mock_update.return_value = Result(True, None, None)

            result = ubah_password_akun(
                user_id=1,
                password_lama='SandiLama123!',
                password_baru='SandiBaru123!',
                konfirmasi_password='SandiBaru123!',
                cabang_id=1,
                db_conn=mock_conn
            )

            self.assertTrue(result.is_success)
            self.assertEqual(result.data, {'action': 'PASSWORD_CHANGED'})
            mock_get_hash.assert_called_once_with(1, mock_conn)
            mock_update.assert_called_once_with(1, 'new_hashed_password', mock_conn)
            mock_audit.assert_called_once()

    def test_ubah_password_konfirmasi_tidak_cocok(self) -> None:
        """Password baru dan konfirmasi tidak cocok -> return ERR-VAL-044."""
        mock_conn = MagicMock()
        result = ubah_password_akun(
            user_id=1,
            password_lama='SandiLama123!',
            password_baru='SandiBaru123!',
            konfirmasi_password='MismatchedPassword123!',
            cabang_id=1,
            db_conn=mock_conn
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-044', result.error_msg)
        self.assertIn('cocok pada kedua input', result.error_msg)

    def test_ubah_password_lemah(self) -> None:
        """Password baru tidak memenuhi kriteria kekuatan -> return ERR-VAL-001 (dari safety_validator)."""
        mock_conn = MagicMock()
        result = ubah_password_akun(
            user_id=1,
            password_lama='SandiLama123!',
            password_baru='lemahlemah',
            konfirmasi_password='lemahlemah',
            cabang_id=1,
            db_conn=mock_conn
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-001', result.error_msg)
        self.assertIn('Sandi Lemah', result.error_msg)

    def test_ubah_password_lama_salah(self) -> None:
        """Password lama tidak cocok dengan hash di database -> return ERR-AUTH-044."""
        mock_conn = MagicMock()

        with patch('logic.pengguna.get_password_hash_by_id') as mock_get_hash, \
             patch('middleware.auth_jwt.verify_password') as mock_verify:

            mock_get_hash.return_value = Result(True, 'old_hashed_password', None)
            mock_verify.return_value = False  # verify_password(password_lama, current_hash) -> False

            result = ubah_password_akun(
                user_id=1,
                password_lama='SandiLamaSalah!',
                password_baru='SandiBaru123!',
                konfirmasi_password='SandiBaru123!',
                cabang_id=1,
                db_conn=mock_conn
            )

            self.assertFalse(result.is_success)
            self.assertIn('ERR-AUTH-044', result.error_msg)
            self.assertIn('Kata sandi lama yang Anda masukkan tidak valid!', result.error_msg)

    def test_ubah_password_sama_dengan_lama(self) -> None:
        """Password baru sama dengan password lama -> return ERR-VAL-044."""
        mock_conn = MagicMock()

        with patch('logic.pengguna.get_password_hash_by_id') as mock_get_hash, \
             patch('middleware.auth_jwt.verify_password') as mock_verify:

            mock_get_hash.return_value = Result(True, 'old_hashed_password', None)
            mock_verify.return_value = True  # verify_password(password_lama, current_hash) -> True

            result = ubah_password_akun(
                user_id=1,
                password_lama='SandiSama123!',
                password_baru='SandiSama123!',
                konfirmasi_password='SandiSama123!',
                cabang_id=1,
                db_conn=mock_conn
            )

            self.assertFalse(result.is_success)
            self.assertIn('ERR-VAL-044', result.error_msg)
            self.assertIn('tidak boleh sama dengan kata sandi lama', result.error_msg)

    def test_ubah_password_db_error(self) -> None:
        """Terjadi error database saat mengambil hash -> return error dari DB."""
        mock_conn = MagicMock()

        with patch('logic.pengguna.get_password_hash_by_id') as mock_get_hash:
            mock_get_hash.return_value = Result(False, None, 'ERR-DB-003: Database down')

            result = ubah_password_akun(
                user_id=1,
                password_lama='SandiLama123!',
                password_baru='SandiBaru123!',
                konfirmasi_password='SandiBaru123!',
                cabang_id=1,
                db_conn=mock_conn
            )

            self.assertFalse(result.is_success)
            self.assertEqual(result.error_msg, 'ERR-DB-003: Database down')


if __name__ == '__main__':
    unittest.main()
