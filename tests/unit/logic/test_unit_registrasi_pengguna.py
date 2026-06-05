"""
Nama Modul: test_unit_registrasi_pengguna.py
Deskripsi: Unit test suite untuk fitur registrasi akun pengguna dengan enkripsi
           bcrypt. Mencakup validasi input, hashing password, verifikasi password,
           validasi RBAC, operasi database (dengan mocking), dan orkestrasi
           fungsi registrasi pengguna secara end-to-end.
           (Ref: Coding Standard v1.2 Bab 14, Test Plan v1.2 Bab 3.1 & 5.1)
Author   : Antigravity (STK-015)
Tanggal  : 2026-06-06
"""

import sys
from pathlib import Path

# Memasukkan root direktori proyek ke prioritas teratas sys.path untuk mencegah shadowing paket logic
project_root = str(Path(__file__).resolve().parents[3])
if project_root in sys.path:
    sys.path.remove(project_root)
sys.path.insert(0, project_root)

# 1. Standard Library
import unittest
from collections import namedtuple
from unittest.mock import MagicMock, patch

# 2. Third-Party (tidak ada direct imports di module level)

# 3. Local Modules (diimport di dalam fungsi test masing-masing untuk isolasi)


# ===========================================================================
# KELAS 1: TestHashPassword
# ===========================================================================
class TestHashPassword(unittest.TestCase):
    """Pengujian untuk fungsi hash_password di middleware/auth_jwt.py."""

    def test_hash_password_menghasilkan_prefix_bcrypt_valid(self) -> None:
        """Verifikasi bahwa hash password menggunakan bcrypt cost factor 12 (diawali dengan prefix $2b$12$)."""
        from middleware.auth_jwt import hash_password
        result = hash_password('SandiKuat123!')
        self.assertTrue(result.startswith('$2b$12$'))

    def test_hash_password_salt_dinamis_menghasilkan_hash_berbeda(self) -> None:
        """Dua pemanggilan hash_password dengan sandi yang sama harus menghasilkan hash yang berbeda karena salt dinamis."""
        from middleware.auth_jwt import hash_password
        hash1 = hash_password('SamePass123!')
        hash2 = hash_password('SamePass123!')
        self.assertNotEqual(hash1, hash2)

    def test_hash_password_mengembalikan_tipe_string(self) -> None:
        """Verifikasi tipe data hasil kembalian hash_password adalah string (bukan bytes)."""
        from middleware.auth_jwt import hash_password
        result = hash_password('TestPassword123!')
        self.assertIsInstance(result, str)

    def test_hash_password_panjang_hash_tepat_60_karakter(self) -> None:
        """Verifikasi panjang hash bcrypt yang dihasilkan tepat 60 karakter."""
        from middleware.auth_jwt import hash_password
        result = hash_password('TestPassword123!')
        self.assertEqual(len(result), 60)

    def test_hash_password_password_sangat_panjang_tetap_berhasil(self) -> None:
        """Memastikan fungsi hash_password tidak crash dan tetap menghasilkan hash valid saat password sangat panjang (72+ karakter)."""
        from middleware.auth_jwt import hash_password
        long_password = 'A' * 72 + 'b1!'
        result = hash_password(long_password)
        self.assertTrue(result.startswith('$2b$12$'))

    def test_hash_password_password_kosong_tetap_menghasilkan_hash(self) -> None:
        """Memastikan hash_password tetap menghasilkan string hash bcrypt yang valid bahkan jika sandi polos berupa string kosong."""
        from middleware.auth_jwt import hash_password
        result = hash_password('')
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('$2b$'))


# ===========================================================================
# KELAS 2: TestVerifyPassword
# ===========================================================================
class TestVerifyPassword(unittest.TestCase):
    """Pengujian untuk fungsi verify_password di middleware/auth_jwt.py."""

    def test_verify_password_password_benar_mengembalikan_true(self) -> None:
        """Verifikasi password benar harus mengembalikan True."""
        from middleware.auth_jwt import hash_password, verify_password
        hashed = hash_password('PasswordBenar123!')
        result = verify_password('PasswordBenar123!', hashed)
        self.assertTrue(result)

    def test_verify_password_password_salah_mengembalikan_false(self) -> None:
        """Verifikasi password salah harus ditolak dan mengembalikan False."""
        from middleware.auth_jwt import hash_password, verify_password
        hashed = hash_password('PasswordBenar123!')
        result = verify_password('PasswordSalah456!', hashed)
        self.assertFalse(result)

    def test_verify_password_password_kosong_mengembalikan_false(self) -> None:
        """Verifikasi password kosong terhadap hash valid harus mengembalikan False."""
        from middleware.auth_jwt import hash_password, verify_password
        hashed = hash_password('PasswordBenar123!')
        result = verify_password('', hashed)
        self.assertFalse(result)

    def test_verify_password_case_sensitive_mengembalikan_false(self) -> None:
        """Verifikasi password bersifat case-sensitive, perbedaan huruf kapital harus mengembalikan False."""
        from middleware.auth_jwt import hash_password, verify_password
        hashed = hash_password('SandiKuat123!')
        result = verify_password('sandikuat123!', hashed)
        self.assertFalse(result)

    def test_verify_password_password_unicode_diverifikasi_benar(self) -> None:
        """Verifikasi password yang mengandung karakter Unicode/non-ASCII terverifikasi dengan benar."""
        from middleware.auth_jwt import hash_password, verify_password
        password_unicode = 'Sandi123!™'
        hashed = hash_password(password_unicode)
        result = verify_password(password_unicode, hashed)
        self.assertTrue(result)


# ===========================================================================
# KELAS 3: TestValidasiKekuatanSandi
# ===========================================================================
class TestValidasiKekuatanSandi(unittest.TestCase):
    """Pengujian untuk fungsi validasi_kekuatan_sandi di logic/safety_validator.py."""

    def test_validasi_sandi_password_kuat_lolos_semua_kriteria(self) -> None:
        """Sandi kuat yang memenuhi minimal 8 karakter, huruf besar, huruf kecil, angka, dan karakter spesial harus valid."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('SandiKuat123!')
        self.assertTrue(result.is_valid)
        self.assertIsNone(result.error_msg)
        self.assertEqual(result.sanitized_data, 'SandiKuat123!')

    def test_validasi_sandi_password_terlalu_pendek_ditolak(self) -> None:
        """Sandi dengan panjang kurang dari 8 karakter harus ditolak dengan kode ERR-VAL-001."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('Ab1!')
        self.assertFalse(result.is_valid)
        self.assertIn('ERR-VAL-001', result.error_msg)
        self.assertIn('8 karakter', result.error_msg)

    def test_validasi_sandi_tanpa_huruf_besar_ditolak(self) -> None:
        """Sandi tanpa huruf kapital harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('sandikuat123!')
        self.assertFalse(result.is_valid)
        self.assertIn('huruf besar', result.error_msg)

    def test_validasi_sandi_tanpa_huruf_kecil_ditolak(self) -> None:
        """Sandi tanpa huruf kecil harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('SANDIKUAT123!')
        self.assertFalse(result.is_valid)
        self.assertIn('huruf kecil', result.error_msg)

    def test_validasi_sandi_tanpa_angka_ditolak(self) -> None:
        """Sandi tanpa angka harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('SandiKuat!!!')
        self.assertFalse(result.is_valid)
        self.assertIn('angka', result.error_msg)

    def test_validasi_sandi_tanpa_karakter_spesial_ditolak(self) -> None:
        """Sandi tanpa karakter spesial harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('SandiKuat123')
        self.assertFalse(result.is_valid)
        self.assertIn('karakter spesial', result.error_msg)

    def test_validasi_sandi_tepat_8_karakter_lolos_batas_minimum(self) -> None:
        """Sandi dengan panjang tepat 8 karakter dan memenuhi 5 kriteria harus valid."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('Sd123!aB')
        self.assertTrue(result.is_valid)

    def test_validasi_sandi_7_karakter_gagal_batas_minimum(self) -> None:
        """Sandi dengan panjang 7 karakter harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('Sd12!aB')
        self.assertFalse(result.is_valid)
        self.assertIn('ERR-VAL-001', result.error_msg)

    def test_validasi_sandi_hanya_angka_ditolak(self) -> None:
        """Sandi yang hanya berisi angka harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('12345678')
        self.assertFalse(result.is_valid)
        self.assertIn('ERR-VAL-001', result.error_msg)

    def test_validasi_sandi_password_kosong_ditolak(self) -> None:
        """Sandi kosong harus ditolak."""
        from logic.safety_validator import validasi_kekuatan_sandi
        result = validasi_kekuatan_sandi('')
        self.assertFalse(result.is_valid)
        self.assertIn('ERR-VAL-001', result.error_msg)


# ===========================================================================
# KELAS 4: TestSantasiInputCli
# ===========================================================================
class TestSantasiInputCli(unittest.TestCase):
    """Pengujian untuk fungsi sanitasi_input_cli di logic/safety_validator.py."""

    def test_sanitasi_input_cli_input_normal_tidak_berubah(self) -> None:
        """Input teks normal tanpa karakter kontrol ASCII tidak boleh berubah."""
        from logic.safety_validator import sanitasi_input_cli
        result = sanitasi_input_cli('Budi Santoso')
        self.assertEqual(result, 'Budi Santoso')

    def test_sanitasi_input_cli_ansi_escape_code_dihapus(self) -> None:
        """Karakter ANSI Escape Code (byte di bawah 0x20, seperti \\x1b) wajib dihapus untuk proteksi visual terminal."""
        from logic.safety_validator import sanitasi_input_cli
        result = sanitasi_input_cli('\x1b[31mBarang Palsu')
        self.assertEqual(result, '[31mBarang Palsu')

    def test_sanitasi_input_cli_karakter_kontrol_null_dihapus(self) -> None:
        """Karakter kontrol NULL (\\x00) dan BELL (\\x07) harus dibuang dari string input."""
        from logic.safety_validator import sanitasi_input_cli
        result = sanitasi_input_cli('Nama\x00Barang\x07Test')
        self.assertEqual(result, 'NamaBarangTest')

    def test_sanitasi_input_cli_string_kosong_tetap_kosong(self) -> None:
        """String kosong yang disanitasi harus tetap menghasilkan string kosong."""
        from logic.safety_validator import sanitasi_input_cli
        result = sanitasi_input_cli('')
        self.assertEqual(result, '')

    def test_sanitasi_input_cli_semua_karakter_kontrol_menghasilkan_string_kosong(self) -> None:
        """Input yang hanya berisi karakter kontrol ASCII harus disanitasi menjadi string kosong."""
        from logic.safety_validator import sanitasi_input_cli
        result = sanitasi_input_cli('\x00\x01\x1b\x1f')
        self.assertEqual(result, '')


# ===========================================================================
# KELAS 5: TestValidasiRole
# ===========================================================================
class TestValidasiRole(unittest.TestCase):
    """Pengujian untuk fungsi validasi_role di logic/pengguna.py."""

    def test_validasi_role_kasir_diterima_sebagai_valid(self) -> None:
        """Verifikasi role 'kasir' diterima sebagai valid dan mengembalikan data lowercase."""
        from logic.pengguna import validasi_role
        result = validasi_role('kasir')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 'kasir')
        self.assertIsNone(result.error_msg)

    def test_validasi_role_uppercase_dinormalisasi_ke_lowercase(self) -> None:
        """Verifikasi role yang ditulis dengan huruf kapital dinormalisasi menjadi lowercase ('PEMILIK' -> 'pemilik')."""
        from logic.pengguna import validasi_role
        result = validasi_role('PEMILIK')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 'pemilik')

    def test_validasi_role_semua_8_role_rbac_valid_diterima(self) -> None:
        """Memastikan seluruh 8 role RBAC valid (pemilik, kasir, dll) diterima tanpa kecuali."""
        from logic.pengguna import validasi_role, VALID_ROLES
        for role in VALID_ROLES:
            result = validasi_role(role)
            self.assertTrue(result.is_success, f'Role {role} seharusnya diterima sebagai valid')

    def test_validasi_role_tidak_terdaftar_ditolak_dengan_error_code(self) -> None:
        """Verifikasi role di luar matriks RBAC ditolak dengan error ERR-VAL-002."""
        from logic.pengguna import validasi_role
        result = validasi_role('admin_palsu')
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-002', result.error_msg)
        self.assertIsNone(result.data)

    def test_validasi_role_string_kosong_ditolak(self) -> None:
        """Verifikasi input role berupa string kosong ditolak."""
        from logic.pengguna import validasi_role
        result = validasi_role('')
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-002', result.error_msg)

    def test_validasi_role_dengan_spasi_leading_trailing_dinormalisasi(self) -> None:
        """Verifikasi spasi tambahan di awal/akhir dibersihkan dan role tetap divalidasi."""
        from logic.pengguna import validasi_role
        result = validasi_role('  kasir  ')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 'kasir')


# ===========================================================================
# KELAS 6: TestValidasiNamaLengkap
# ===========================================================================
class TestValidasiNamaLengkap(unittest.TestCase):
    """Pengujian untuk fungsi validasi_nama_lengkap di logic/pengguna.py."""

    def test_validasi_nama_lengkap_nama_valid_diterima(self) -> None:
        """Nama lengkap valid harus diterima."""
        from logic.pengguna import validasi_nama_lengkap
        result = validasi_nama_lengkap('Budi Santoso')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 'Budi Santoso')

    def test_validasi_nama_lengkap_nama_kosong_ditolak_dengan_error_val_003(self) -> None:
        """Nama lengkap kosong atau hanya berisi spasi harus ditolak dengan error ERR-VAL-003."""
        from logic.pengguna import validasi_nama_lengkap
        result = validasi_nama_lengkap('   ')
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-003', result.error_msg)

    def test_validasi_nama_lengkap_nama_melebihi_100_karakter_ditolak(self) -> None:
        """Nama lengkap melebihi 100 karakter harus ditolak."""
        from logic.pengguna import validasi_nama_lengkap
        nama_panjang = 'A' * 101
        result = validasi_nama_lengkap(nama_panjang)
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-003', result.error_msg)

    def test_validasi_nama_lengkap_tepat_100_karakter_diterima(self) -> None:
        """Nama lengkap tepat 100 karakter harus diterima."""
        from logic.pengguna import validasi_nama_lengkap
        nama_100 = 'A' * 100
        result = validasi_nama_lengkap(nama_100)
        self.assertTrue(result.is_success)

    def test_validasi_nama_lengkap_101_karakter_ditolak(self) -> None:
        """Nama lengkap 101 karakter harus ditolak."""
        from logic.pengguna import validasi_nama_lengkap
        nama_101 = 'A' * 101
        result = validasi_nama_lengkap(nama_101)
        self.assertFalse(result.is_success)

    def test_validasi_nama_lengkap_whitespace_di_strip(self) -> None:
        """Spasi tambahan di awal/akhir nama lengkap harus dibersihkan secara otomatis."""
        from logic.pengguna import validasi_nama_lengkap
        result = validasi_nama_lengkap('  Budi Santoso  ')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 'Budi Santoso')


# ===========================================================================
# KELAS 7: TestValidasiUsername
# ===========================================================================
class TestValidasiUsername(unittest.TestCase):
    """Pengujian untuk fungsi validasi_username di logic/pengguna.py."""

    def test_validasi_username_format_valid_dengan_underscore_diterima(self) -> None:
        """Username berformat alfanumerik + underscore yang valid harus diterima."""
        from logic.pengguna import validasi_username
        result = validasi_username('kasir_02')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 'kasir_02')

    def test_validasi_username_uppercase_dinormalisasi_ke_lowercase(self) -> None:
        """Username dengan huruf besar dinormalisasi ke huruf kecil ('Kasir_02' -> 'kasir_02')."""
        from logic.pengguna import validasi_username
        result = validasi_username('Kasir_02')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 'kasir_02')

    def test_validasi_username_username_kosong_ditolak(self) -> None:
        """Username kosong harus ditolak dengan error ERR-VAL-004."""
        from logic.pengguna import validasi_username
        result = validasi_username('')
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-004', result.error_msg)

    def test_validasi_username_karakter_spesial_at_ditolak(self) -> None:
        """Username yang mengandung karakter khusus selain underscore (seperti @) harus ditolak."""
        from logic.pengguna import validasi_username
        result = validasi_username('kasir@02')
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-004', result.error_msg)

    def test_validasi_username_dengan_spasi_ditolak(self) -> None:
        """Username mengandung spasi harus ditolak."""
        from logic.pengguna import validasi_username
        result = validasi_username('kasir 02')
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-004', result.error_msg)

    def test_validasi_username_melebihi_50_karakter_ditolak(self) -> None:
        """Username dengan panjang melebihi 50 karakter harus ditolak."""
        from logic.pengguna import validasi_username
        username_panjang = 'a' * 51
        result = validasi_username(username_panjang)
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-004', result.error_msg)

    def test_validasi_username_tepat_50_karakter_diterima(self) -> None:
        """Username dengan panjang tepat 50 karakter harus diterima."""
        from logic.pengguna import validasi_username
        username_50 = 'a' * 50
        result = validasi_username(username_50)
        self.assertTrue(result.is_success)

    def test_validasi_username_hanya_angka_diterima(self) -> None:
        """Username yang hanya berisi angka adalah format valid dan harus diterima."""
        from logic.pengguna import validasi_username
        result = validasi_username('12345')
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, '12345')


# ===========================================================================
# KELAS 8: TestCekUsernameUnik
# ===========================================================================
class TestCekUsernameUnik(unittest.TestCase):
    """Pengujian untuk fungsi cek_username_unik di db/pengguna_repository.py."""

    def test_cek_username_unik_username_belum_ada_mengembalikan_sukses(self) -> None:
        """Verifikasi jika username belum ada di database, fungsi mengembalikan sukses."""
        from db.pengguna_repository import cek_username_unik
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'jumlah': 0}
        mock_conn.cursor.return_value = mock_cursor

        result = cek_username_unik('user_baru', mock_conn)
        self.assertTrue(result.is_success)
        self.assertIsNone(result.error_msg)
        mock_conn.cursor.assert_called_once_with(dictionary=True)
        mock_cursor.execute.assert_called_once()
        mock_cursor.close.assert_called_once()

    def test_cek_username_unik_username_duplikat_mengembalikan_gagal(self) -> None:
        """Verifikasi jika username sudah terdaftar, fungsi mengembalikan error ERR-DB-002."""
        from db.pengguna_repository import cek_username_unik
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'jumlah': 1}
        mock_conn.cursor.return_value = mock_cursor

        result = cek_username_unik('user_duplikat', mock_conn)
        self.assertFalse(result.is_success)
        self.assertIn('ERR-DB-002', result.error_msg)
        self.assertIsNone(result.data)

    def test_cek_username_unik_exception_database_ditangani_dengan_aman(self) -> None:
        """Memastikan jika cursor melempar Exception, error ditangkap aman dan mengembalikan ERR-DB-002."""
        from db.pengguna_repository import cek_username_unik
        mock_conn = MagicMock()
        mock_conn.cursor.side_effect = Exception('Database connection lost')

        result = cek_username_unik('user_error', mock_conn)
        self.assertFalse(result.is_success)
        self.assertIn('ERR-DB-002', result.error_msg)

    def test_cek_username_unik_query_menggunakan_parameterized_query(self) -> None:
        """Verifikasi bahwa eksekusi query SQL menggunakan parameterized placeholder (%s) terpisah dari variabel input."""
        from db.pengguna_repository import cek_username_unik
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'jumlah': 0}
        mock_conn.cursor.return_value = mock_cursor

        _ = cek_username_unik('test_user', mock_conn)
        call_args = mock_cursor.execute.call_args
        self.assertIn('%s', call_args[0][0])
        self.assertEqual(call_args[0][1], ('test_user',))


# ===========================================================================
# KELAS 9: TestInsertPengguna
# ===========================================================================
class TestInsertPengguna(unittest.TestCase):
    """Pengujian untuk fungsi insert_pengguna di db/pengguna_repository.py."""

    def test_insert_pengguna_berhasil_mengembalikan_id_pengguna_baru(self) -> None:
        """Penyisipan pengguna baru berhasil, mengembalikan ID baris database baru, serta memicu commit transaksi."""
        from db.pengguna_repository import insert_pengguna
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.lastrowid = 42
        mock_conn.cursor.return_value = mock_cursor

        result = insert_pengguna('Budi Santoso', 'budi_01', '$2b$12$hash...', 'kasir', 1, mock_conn)
        self.assertTrue(result.is_success)
        self.assertEqual(result.data, 42)
        self.assertIsNone(result.error_msg)
        mock_conn.start_transaction.assert_called_once()
        mock_conn.commit.assert_called_once()
        mock_cursor.close.assert_called_once()

    def test_insert_pengguna_exception_memicu_rollback_dan_gagal(self) -> None:
        """Exception pada saat eksekusi query penambahan harus memicu rollback transaksi demi integritas database."""
        from db.pengguna_repository import insert_pengguna
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception('Insert DB error')

        result = insert_pengguna('Budi', 'budi_01', 'hash', 'kasir', 1, mock_conn)
        self.assertFalse(result.is_success)
        self.assertIn('ERR-DB-002', result.error_msg)
        mock_conn.rollback.assert_called_once()
        mock_cursor.close.assert_called_once()

    def test_insert_pengguna_menginisialisasi_failed_login_dan_locked_until_ke_nilai_aman(self) -> None:
        """Memastikan field brute force protection ('failed_login_attempts' = 0 dan 'locked_until' = NULL) ikut disisipkan saat registrasi baru."""
        from db.pengguna_repository import insert_pengguna
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.lastrowid = 10
        mock_conn.cursor.return_value = mock_cursor

        _ = insert_pengguna('Budi', 'budi_01', 'hash', 'kasir', 1, mock_conn)
        call_args = mock_cursor.execute.call_args
        query_str = call_args[0][0]
        self.assertIn('failed_login_attempts', query_str)
        self.assertIn('locked_until', query_str)

    def test_insert_pengguna_query_menggunakan_parameterized_placeholder(self) -> None:
        """Verifikasi penyusunan insert query wajib menggunakan parameterized placeholders (%s) dan tidak menggunakan string formatting."""
        from db.pengguna_repository import insert_pengguna
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.lastrowid = 5
        mock_conn.cursor.return_value = mock_cursor

        _ = insert_pengguna('Sari', 'sari_01', 'bcrypt_hash', 'gudang', 2, mock_conn)
        call_args = mock_cursor.execute.call_args
        self.assertIn('%s', call_args[0][0])
        self.assertNotIn('sari_01', call_args[0][0])


# ===========================================================================
# KELAS 10: TestRegistrasiPengguna
# ===========================================================================
class TestRegistrasiPengguna(unittest.TestCase):
    """Pengujian untuk orkestrasi registrasi_pengguna di logic/pengguna.py."""

    def test_registrasi_pengguna_semua_input_valid_mengembalikan_sukses(self) -> None:
        """Registrasi sukses end-to-end dengan seluruh input valid, dan log audit tersimpan transaksional."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor

        with patch('logic.pengguna.cek_username_unik') as mock_cek, \
             patch('logic.pengguna.insert_pengguna') as mock_insert, \
             patch('logic.pengguna.hash_password') as mock_hash:

            ResultType = namedtuple('Result', ['is_success', 'data', 'error_msg'])
            mock_cek.return_value = ResultType(True, None, None)
            mock_insert.return_value = ResultType(True, 99, None)
            mock_hash.return_value = '$2b$12$mocked_hash'

            result = registrasi_pengguna(
                'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
                'kasir', 1, mock_conn, 1
            )
            self.assertTrue(result.is_success)
            self.assertEqual(result.data, 99)
            self.assertIsNone(result.error_msg)
            mock_cursor.execute.assert_called_once()  # Menyimpan audit log
            mock_conn.commit.assert_called_once()

    def test_registrasi_pengguna_nama_kosong_ditolak_sebelum_proses_lanjut(self) -> None:
        """Registrasi ditolak cepat (short-circuit) dengan error ERR-VAL-003 jika nama lengkap kosong."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            '', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
            'kasir', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-003', result.error_msg)

    def test_registrasi_pengguna_username_kosong_ditolak(self) -> None:
        """Registrasi ditolak jika username kosong."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            'Budi Santoso', '', 'SandiKuat123!', 'SandiKuat123!',
            'kasir', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-004', result.error_msg)

    def test_registrasi_pengguna_password_tidak_cocok_ditolak(self) -> None:
        """Registrasi ditolak dengan error ERR-VAL-005 jika sandi dan konfirmasi sandi tidak cocok."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            'Budi Santoso', 'budi_01', 'SandiKuat123!', 'BerbedaSandi456!',
            'kasir', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-005', result.error_msg)

    def test_registrasi_pengguna_password_lemah_ditolak(self) -> None:
        """Registrasi ditolak dengan error ERR-VAL-001 jika sandi tidak memenuhi kriteria kekuatan kata sandi aman."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            'Budi Santoso', 'budi_01', 'lemah', 'lemah',
            'kasir', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-001', result.error_msg)

    def test_registrasi_pengguna_role_tidak_valid_ditolak(self) -> None:
        """Registrasi ditolak dengan error ERR-VAL-002 jika peran RBAC tidak valid."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
            'superadmin', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-002', result.error_msg)

    def test_registrasi_pengguna_username_duplikat_ditolak(self) -> None:
        """Registrasi ditolak dengan error ERR-DB-002 jika username yang didaftarkan sudah terpakai di database."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()

        with patch('logic.pengguna.cek_username_unik') as mock_cek:
            ResultType = namedtuple('Result', ['is_success', 'data', 'error_msg'])
            mock_cek.return_value = ResultType(False, None, 'ERR-DB-002: Username Duplikat: ...')

            result = registrasi_pengguna(
                'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
                'kasir', 1, mock_conn, 1
            )
            self.assertFalse(result.is_success)
            self.assertIn('ERR-DB-002', result.error_msg)

    def test_registrasi_pengguna_insert_database_gagal_mengembalikan_error(self) -> None:
        """Registrasi ditolak jika penyisipan baris data pengguna baru gagal di level database access layer."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()

        with patch('logic.pengguna.cek_username_unik') as mock_cek, \
             patch('logic.pengguna.insert_pengguna') as mock_insert, \
             patch('logic.pengguna.hash_password') as mock_hash:

            ResultType = namedtuple('Result', ['is_success', 'data', 'error_msg'])
            mock_cek.return_value = ResultType(True, None, None)
            mock_insert.return_value = ResultType(False, None, 'ERR-DB-002: Gagal menyimpan data pengguna baru.')
            mock_hash.return_value = '$2b$12$mocked'

            result = registrasi_pengguna(
                'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
                'kasir', 1, mock_conn, 1
            )
            self.assertFalse(result.is_success)
            self.assertIn('ERR-DB-002', result.error_msg)

    def test_registrasi_pengguna_kegagalan_audit_log_tidak_membatalkan_registrasi(self) -> None:
        """Registrasi harus tetap berhasil (sukses) sekalipun pencatatan log audit mengalami kegagalan/exception."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.execute.side_effect = Exception('Audit log DB error')

        with patch('logic.pengguna.cek_username_unik') as mock_cek, \
             patch('logic.pengguna.insert_pengguna') as mock_insert, \
             patch('logic.pengguna.hash_password') as mock_hash:

            ResultType = namedtuple('Result', ['is_success', 'data', 'error_msg'])
            mock_cek.return_value = ResultType(True, None, None)
            mock_insert.return_value = ResultType(True, 77, None)
            mock_hash.return_value = 'mocked'

            result = registrasi_pengguna(
                'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
                'kasir', 1, mock_conn, 1
            )
            self.assertTrue(result.is_success)
            self.assertEqual(result.data, 77)

    def test_registrasi_pengguna_username_format_salah_ditolak(self) -> None:
        """Registrasi ditolak dengan error ERR-VAL-004 jika format username mengandung karakter tidak diizinkan."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()
        result = registrasi_pengguna(
            'Budi Santoso', 'budi@01', 'SandiKuat123!', 'SandiKuat123!',
            'kasir', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-004', result.error_msg)

    def test_registrasi_pengguna_nama_terlalu_panjang_ditolak(self) -> None:
        """Registrasi ditolak dengan error ERR-VAL-003 jika nama lengkap melampaui 100 karakter."""
        from logic.pengguna import registrasi_pengguna
        mock_conn = MagicMock()
        nama = 'B' * 101
        result = registrasi_pengguna(
            nama, 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
            'kasir', 1, mock_conn, 1
        )
        self.assertFalse(result.is_success)
        self.assertIn('ERR-VAL-003', result.error_msg)

    def test_registrasi_pengguna_semua_8_role_rbac_dapat_diregistrasikan(self) -> None:
        """Memastikan registrasi pengguna dengan seluruh 8 role RBAC yang valid dapat didaftarkan dengan sukses."""
        from logic.pengguna import registrasi_pengguna, VALID_ROLES
        
        for role in VALID_ROLES:
            mock_conn = MagicMock()
            mock_cursor = MagicMock()
            mock_conn.cursor.return_value = mock_cursor

            with patch('logic.pengguna.cek_username_unik') as mock_cek, \
                 patch('logic.pengguna.insert_pengguna') as mock_insert, \
                 patch('logic.pengguna.hash_password') as mock_hash:

                ResultType = namedtuple('Result', ['is_success', 'data', 'error_msg'])
                mock_cek.return_value = ResultType(True, None, None)
                mock_insert.return_value = ResultType(True, 123, None)
                mock_hash.return_value = 'mocked_hash'

                result = registrasi_pengguna(
                    'Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!',
                    role, 1, mock_conn, 1
                )
                self.assertTrue(result.is_success, f'Registrasi dengan role {role} seharusnya berhasil')


if __name__ == '__main__':
    unittest.main()
