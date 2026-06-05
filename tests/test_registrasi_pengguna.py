"""
Nama Modul: test_registrasi_pengguna.py
Deskripsi: Test suite unit testing untuk fitur registrasi akun pengguna
           dan enkripsi bcrypt. Mencakup validasi password, hashing,
           verifikasi, dan orkestrasi registrasi.
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

import unittest


class TestHashPassword(unittest.TestCase):
    """Test cases untuk fungsi hash_password() di middleware/auth_jwt.py."""

    def test_hash_returns_bcrypt_format(self) -> None:
        """Hash harus diawali prefix bcrypt '$2b$12$'."""
        from middleware.auth_jwt import hash_password
        result = hash_password('TestPassword123!')
        self.assertTrue(result.startswith('$2b$12$'))

    def test_hash_different_salt_each_call(self) -> None:
        """Dua panggilan hash untuk password sama harus menghasilkan hash berbeda (salt dinamis)."""
        from middleware.auth_jwt import hash_password
        hash1 = hash_password('SamePassword123!')
        hash2 = hash_password('SamePassword123!')
        self.assertNotEqual(hash1, hash2)

    def test_hash_returns_string_type(self) -> None:
        """Hash harus berupa string (bukan bytes)."""
        from middleware.auth_jwt import hash_password
        result = hash_password('TestPassword123!')
        self.assertIsInstance(result, str)

    def test_hash_length_valid(self) -> None:
        """Hash bcrypt harus memiliki panjang 60 karakter."""
        from middleware.auth_jwt import hash_password
        result = hash_password('TestPassword123!')
        self.assertEqual(len(result), 60)


class TestVerifyPassword(unittest.TestCase):
    """Test cases untuk fungsi verify_password() di middleware/auth_jwt.py."""

    def test_verify_correct_password(self) -> None:
        """Verifikasi password yang benar harus mengembalikan True."""
        from middleware.auth_jwt import hash_password, verify_password
        hashed = hash_password('CorrectPassword123!')
        self.assertTrue(verify_password('CorrectPassword123!', hashed))

    def test_verify_wrong_password(self) -> None:
        """Verifikasi password yang salah harus mengembalikan False."""
        from middleware.auth_jwt import hash_password, verify_password
        hashed = hash_password('CorrectPassword123!')
        self.assertFalse(verify_password('WrongPassword456!', hashed))

    def test_verify_empty_password(self) -> None:
        """Verifikasi password kosong terhadap hash valid harus mengembalikan False."""
        from middleware.auth_jwt import hash_password, verify_password
        hashed = hash_password('CorrectPassword123!')
        self.assertFalse(verify_password('', hashed))


class TestValidasiKekuatanSandi(unittest.TestCase):
    """Test cases untuk fungsi validasi_kekuatan_sandi() di logic/safety_validator.py."""

    def test_password_kuat_valid(self) -> None:
        """Password kuat yang memenuhi 5 kriteria harus lolos validasi."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('SandiKuat123!')
        self.assertTrue(result.is_valid)
        self.assertIsNone(result.error_msg)

    def test_password_terlalu_pendek(self) -> None:
        """Password kurang dari 8 karakter harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('Ab1!')
        self.assertFalse(result.is_valid)
        self.assertIn('ERR-VAL-001', result.error_msg)

    def test_password_tanpa_huruf_besar(self) -> None:
        """Password tanpa huruf besar harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('sandikuat123!')
        self.assertFalse(result.is_valid)
        self.assertIn('huruf besar', result.error_msg)

    def test_password_tanpa_huruf_kecil(self) -> None:
        """Password tanpa huruf kecil harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('SANDIKUAT123!')
        self.assertFalse(result.is_valid)
        self.assertIn('huruf kecil', result.error_msg)

    def test_password_tanpa_angka(self) -> None:
        """Password tanpa angka harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('SandiKuat!!!')
        self.assertFalse(result.is_valid)
        self.assertIn('angka', result.error_msg)

    def test_password_tanpa_karakter_spesial(self) -> None:
        """Password tanpa karakter spesial harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('SandiKuat123')
        self.assertFalse(result.is_valid)
        self.assertIn('karakter spesial', result.error_msg)


class TestValidasiRole(unittest.TestCase):
    """Test cases untuk fungsi validasi_role() di logic/pengguna.py."""

    def test_role_valid_kasir(self) -> None:
        """Role 'kasir' harus diterima sebagai valid."""
        from logic.pengguna import validasi_role
        result = validasi_role('kasir')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 'kasir')

    def test_role_valid_case_insensitive(self) -> None:
        """Role harus divalidasi secara case-insensitive."""
        from logic.pengguna import validasi_role
        result = validasi_role('PEMILIK')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 'pemilik')

    def test_role_invalid(self) -> None:
        """Role yang tidak terdaftar harus ditolak."""
        from logic.pengguna import validasi_role
        result = validasi_role('admin')
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-002', result.error_msg)

    def test_semua_8_role_valid(self) -> None:
        """Seluruh 8 role RBAC harus diterima sebagai valid."""
        from logic.pengguna import validasi_role, VALID_ROLES
        for role in VALID_ROLES:
            result = validasi_role(role)
            self.assertTrue(result.is_success, f'Role {role} seharusnya valid')


class TestValidasiNamaLengkap(unittest.TestCase):
    """Test cases untuk fungsi validasi_nama_lengkap() di logic/pengguna.py."""

    def test_nama_valid(self) -> None:
        from logic.pengguna import validasi_nama_lengkap
        result = validasi_nama_lengkap('Budi Santoso')
        self.assertTrue(result.is_success)

    def test_nama_kosong(self) -> None:
        from logic.pengguna import validasi_nama_lengkap
        result = validasi_nama_lengkap('   ')
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-003', result.error_msg)

    def test_nama_terlalu_panjang(self) -> None:
        from logic.pengguna import validasi_nama_lengkap
        result = validasi_nama_lengkap('A' * 101)
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-003', result.error_msg)


class TestValidasiUsername(unittest.TestCase):
    """Test cases untuk fungsi validasi_username() di logic/pengguna.py."""

    def test_username_valid(self) -> None:
        from logic.pengguna import validasi_username
        result = validasi_username('kasir_02')
        self.assertTrue(result.is_success)

    def test_username_kosong(self) -> None:
        from logic.pengguna import validasi_username
        result = validasi_username('')
        self.assertFalse(result.is_success)

    def test_username_karakter_spesial(self) -> None:
        from logic.pengguna import validasi_username
        result = validasi_username('kasir@02')
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-004', result.error_msg)

    def test_username_uppercase_dinormalisasi(self) -> None:
        from logic.pengguna import validasi_username
        result = validasi_username('Kasir_02')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 'kasir_02')


class TestCekUsernameUnik(unittest.TestCase):
    def test_username_is_unique(self) -> None:
        from db.pengguna_repository import cek_username_unik
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'jumlah': 0}
        mock_conn.cursor.return_value = mock_cursor

        result = cek_username_unik('unik_user', mock_conn)
        self.assertTrue(result.is_success)
        mock_conn.cursor.assert_called_once_with(dictionary=True)
        mock_cursor.execute.assert_called_once()
        mock_cursor.close.assert_called_once()

    def test_username_is_duplicate(self) -> None:
        from db.pengguna_repository import cek_username_unik
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'jumlah': 1}
        mock_conn.cursor.return_value = mock_cursor

        result = cek_username_unik('dupe_user', mock_conn)
        self.assertFalse(result.is_success)
        self.assertIn('ERR-DB-002', result.error_msg)

    def test_cek_username_exception(self) -> None:
        from db.pengguna_repository import cek_username_unik
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        mock_conn.cursor.side_effect = Exception('Database down')

        result = cek_username_unik('error_user', mock_conn)
        self.assertFalse(result.is_success)
        self.assertIn('ERR-DB-002', result.error_msg)


class TestInsertPengguna(unittest.TestCase):
    def test_insert_success(self) -> None:
        from db.pengguna_repository import insert_pengguna
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.lastrowid = 42
        mock_conn.cursor.return_value = mock_cursor

        result = insert_pengguna('Budi', 'budi_01', 'hashed_pass', 'kasir', 1, mock_conn)
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 42)
        mock_conn.start_transaction.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    def test_insert_exception(self) -> None:
        from db.pengguna_repository import insert_pengguna
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception('Insert error')

        result = insert_pengguna('Budi', 'budi_01', 'hashed_pass', 'kasir', 1, mock_conn)
        self.assertFalse(result.is_success)
        self.assertIn('ERR-DB-002', result.error_msg)
        mock_conn.rollback.assert_called_once()
        mock_cursor.close.assert_called_once()


class TestRegistrasiPengguna(unittest.TestCase):
    def test_registrasi_success(self) -> None:
        from logic.pengguna import registrasi_pengguna
        from unittest.mock import MagicMock, patch
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        with patch('logic.pengguna.cek_username_unik') as mock_cek, \
             patch('logic.pengguna.insert_pengguna') as mock_insert, \
             patch('logic.pengguna.hash_password') as mock_hash:
            
            from collections import namedtuple
            ResultType = namedtuple('Result', ['is_success', 'data', 'error_msg'])
            mock_cek.return_value = ResultType(True, None, None)
            mock_insert.return_value = ResultType(True, 123, None)
            mock_hash.return_value = 'mocked_bcrypt_hash'

            result = registrasi_pengguna(
                'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
                'kasir', 1, mock_conn, 1
            )
            self.assertTrue(result.is_success)
            self.assertEqual(result.data, 123)
            mock_cursor.execute.assert_called_once()  # audit log insert
            mock_conn.commit.assert_called_once()

    def test_registrasi_nama_kosong(self) -> None:
        from logic.pengguna import registrasi_pengguna
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            '', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
            'kasir', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-003', result.error_msg)

    def test_registrasi_username_kosong(self) -> None:
        from logic.pengguna import registrasi_pengguna
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            'Budi Santoso', '', 'SandiKuat123!', 'SandiKuat123!',
            'kasir', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-004', result.error_msg)

    def test_registrasi_password_mismatch(self) -> None:
        from logic.pengguna import registrasi_pengguna
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            'Budi Santoso', 'budi_01', 'SandiKuat123!', 'Mismatch123!',
            'kasir', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-005', result.error_msg)

    def test_registrasi_password_lemah(self) -> None:
        from logic.pengguna import registrasi_pengguna
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            'Budi Santoso', 'budi_01', 'lemah', 'lemah',
            'kasir', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-001', result.error_msg)

    def test_registrasi_role_tidak_valid(self) -> None:
        from logic.pengguna import registrasi_pengguna
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
            'admin_palsu', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-002', result.error_msg)

    def test_registrasi_username_duplikat(self) -> None:
        from logic.pengguna import registrasi_pengguna
        from unittest.mock import MagicMock, patch
        mock_conn = MagicMock()

        with patch('logic.pengguna.cek_username_unik') as mock_cek:
            from collections import namedtuple
            ResultType = namedtuple('Result', ['is_success', 'data', 'error_msg'])
            mock_cek.return_value = ResultType(False, None, 'ERR-DB-002: Username Duplikat: ...')

            result = registrasi_pengguna(
                'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
                'kasir', 1, mock_conn, 1
            )
            self.assertFalse(result.is_success)
            self.assertIn('ERR-DB-002', result.error_msg)

    def test_registrasi_insert_fail(self) -> None:
        from logic.pengguna import registrasi_pengguna
        from unittest.mock import MagicMock, patch
        mock_conn = MagicMock()

        with patch('logic.pengguna.cek_username_unik') as mock_cek, \
             patch('logic.pengguna.insert_pengguna') as mock_insert, \
             patch('logic.pengguna.hash_password') as mock_hash:
            
            from collections import namedtuple
            ResultType = namedtuple('Result', ['is_success', 'data', 'error_msg'])
            mock_cek.return_value = ResultType(True, None, None)
            mock_insert.return_value = ResultType(False, None, 'ERR-DB-002: Gagal menyimpan ...')
            mock_hash.return_value = 'mocked_bcrypt_hash'

            result = registrasi_pengguna(
                'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
                'kasir', 1, mock_conn, 1
            )
            self.assertFalse(result.is_success)
            self.assertIn('ERR-DB-002', result.error_msg)

    def test_registrasi_audit_log_fail_does_not_fail_registration(self) -> None:
        from logic.pengguna import registrasi_pengguna
        from unittest.mock import MagicMock, patch
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception('Audit log DB error')

        with patch('logic.pengguna.cek_username_unik') as mock_cek, \
             patch('logic.pengguna.insert_pengguna') as mock_insert, \
             patch('logic.pengguna.hash_password') as mock_hash:
            
            from collections import namedtuple
            ResultType = namedtuple('Result', ['is_success', 'data', 'error_msg'])
            mock_cek.return_value = ResultType(True, None, None)
            mock_insert.return_value = ResultType(True, 123, None)
            mock_hash.return_value = 'mocked_bcrypt_hash'

            result = registrasi_pengguna(
                'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
                'kasir', 1, mock_conn, 1
            )
            self.assertTrue(result.is_success)
            self.assertEqual(result.data, 123)


if __name__ == '__main__':
    unittest.main()
