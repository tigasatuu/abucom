"""
Nama Modul: test_kelola_supplier.py
Deskripsi: Unit testing deterministic terisolasi penuh (tanpa koneksi DB riil)
           untuk fungsi validasi dan query builder data master supplier.
Author: Senior Python Backend Engineer & Data Master Specialist
Tanggal: 2026-06-08
"""

import unittest
from unittest.mock import MagicMock, patch
from collections import namedtuple

from logic.safety_validator import (
    validasi_data_supplier,
    validasi_supplier_id,
    Result as ValidationResult,
    ValidationStatus
)
from db.query_builder import (
    query_daftar_supplier,
    query_detail_supplier,
    query_insert_supplier,
    query_update_supplier,
    query_delete_supplier,
    query_cek_nama_supplier_duplikat,
    Result as DBResult
)

class TestKelolaSupplierValidator(unittest.TestCase):
    """Suite unit testing untuk fungsi-fungsi fungsional validasi supplier."""

    def test_validasi_data_supplier_valid(self):
        """Skenario Positif: Validasi data supplier lengkap dan valid."""
        raw_data = {
            'nama_supplier': 'CV. Maju Bersama',
            'alamat': 'Jl. Industri No. 45, Bandung',
            'telp': '08123456789',
            'email': 'contact@majubersama.com'
        }
        res = validasi_data_supplier(raw_data)
        self.assertTrue(res.is_success)
        self.assertIsNone(res.error_msg)
        self.assertEqual(res.data['nama_supplier'], 'CV. Maju Bersama')
        self.assertEqual(res.data['alamat'], 'Jl. Industri No. 45, Bandung')
        self.assertEqual(res.data['telp'], '08123456789')
        self.assertEqual(res.data['email'], 'contact@majubersama.com')

    def test_validasi_data_supplier_nama_kosong(self):
        """Skenario Negatif: Nama supplier kosong atau hanya spasi."""
        raw_data = {
            'nama_supplier': '   ',
            'alamat': 'Jl. Industri No. 45, Bandung',
            'telp': '08123456789',
            'email': 'contact@majubersama.com'
        }
        res = validasi_data_supplier(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("Nama supplier tidak boleh kosong", res.error_msg)

    def test_validasi_data_supplier_nama_terlalu_panjang(self):
        """Skenario Negatif: Nama supplier melebihi 100 karakter."""
        raw_data = {
            'nama_supplier': 'A' * 101,
            'alamat': 'Jl. Industri No. 45, Bandung',
            'telp': '08123456789',
            'email': 'contact@majubersama.com'
        }
        res = validasi_data_supplier(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("Nama supplier maksimal 100 karakter", res.error_msg)

    def test_validasi_data_supplier_alamat_kosong(self):
        """Skenario Negatif: Alamat supplier kosong."""
        raw_data = {
            'nama_supplier': 'CV. Maju Bersama',
            'alamat': '',
            'telp': '08123456789',
            'email': 'contact@majubersama.com'
        }
        res = validasi_data_supplier(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("Alamat supplier tidak boleh kosong", res.error_msg)

    def test_validasi_data_supplier_telp_kosong(self):
        """Skenario Negatif: Nomor telepon kosong."""
        raw_data = {
            'nama_supplier': 'CV. Maju Bersama',
            'alamat': 'Jl. Industri No. 45, Bandung',
            'telp': '   ',
            'email': 'contact@majubersama.com'
        }
        res = validasi_data_supplier(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("Nomor telepon supplier tidak boleh kosong", res.error_msg)

    def test_validasi_data_supplier_telp_terlalu_panjang(self):
        """Skenario Negatif: Nomor telepon melebihi 30 karakter."""
        raw_data = {
            'nama_supplier': 'CV. Maju Bersama',
            'alamat': 'Jl. Industri No. 45, Bandung',
            'telp': '1' * 31,
            'email': 'contact@majubersama.com'
        }
        res = validasi_data_supplier(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("Nomor telepon supplier maksimal 30 karakter", res.error_msg)

    def test_validasi_data_supplier_telp_format_invalid(self):
        """Skenario Negatif: Nomor telepon mengandung karakter selain angka/+/spasi/-."""
        raw_data = {
            'nama_supplier': 'CV. Maju Bersama',
            'alamat': 'Jl. Industri No. 45, Bandung',
            'telp': '0812-345-ABC',
            'email': 'contact@majubersama.com'
        }
        res = validasi_data_supplier(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("Format nomor telepon tidak valid", res.error_msg)

    def test_validasi_data_supplier_email_kosong(self):
        """Skenario Negatif: Email kosong."""
        raw_data = {
            'nama_supplier': 'CV. Maju Bersama',
            'alamat': 'Jl. Industri No. 45, Bandung',
            'telp': '08123456789',
            'email': ''
        }
        res = validasi_data_supplier(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("Email supplier tidak boleh kosong", res.error_msg)

    def test_validasi_data_supplier_email_terlalu_panjang(self):
        """Skenario Negatif: Email melebihi 100 karakter."""
        raw_data = {
            'nama_supplier': 'CV. Maju Bersama',
            'alamat': 'Jl. Industri No. 45, Bandung',
            'telp': '08123456789',
            'email': 'A' * 90 + '@example.com'  # 102 chars
        }
        res = validasi_data_supplier(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("Email supplier maksimal 100 karakter", res.error_msg)

    def test_validasi_data_supplier_email_format_invalid(self):
        """Skenario Negatif: Format email tidak valid."""
        raw_data = {
            'nama_supplier': 'CV. Maju Bersama',
            'alamat': 'Jl. Industri No. 45, Bandung',
            'telp': '08123456789',
            'email': 'majubersama.com'
        }
        res = validasi_data_supplier(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("Format email tidak valid", res.error_msg)

    def test_validasi_supplier_id_valid(self):
        """Skenario Positif: ID supplier valid (integer positif)."""
        res = validasi_supplier_id('12')
        self.assertTrue(res.is_valid)
        self.assertEqual(res.sanitized_data, 12)

    def test_validasi_supplier_id_invalid_string(self):
        """Skenario Negatif: ID supplier bukan numerik."""
        res = validasi_supplier_id('abc')
        self.assertFalse(res.is_valid)
        self.assertIn("ID supplier harus berupa angka bulat positif", res.error_msg)

    def test_validasi_supplier_id_negatif(self):
        """Skenario Negatif: ID supplier bernilai negatif."""
        res = validasi_supplier_id('-5')
        self.assertFalse(res.is_valid)
        self.assertIn("ID supplier harus berupa angka bulat positif", res.error_msg)


class TestKelolaSupplierQueries(unittest.TestCase):
    """Suite unit testing untuk fungsi-fungsi query builder supplier."""

    def test_query_daftar_supplier_kosong(self):
        """Skenario Positif: Mengambil daftar supplier ketika DB kosong."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_conn.cursor.return_value = mock_cursor

        res = query_daftar_supplier(mock_conn, cabang_id=1)
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, [])
        mock_cursor.execute.assert_called_once()

    def test_query_daftar_supplier_sukses(self):
        """Skenario Positif: Mengambil daftar supplier sukses."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_data = [{'id': 1, 'nama_supplier': 'Supplier A', 'alamat': 'Alamat A', 'telp': '123', 'email': 'a@b.com'}]
        mock_cursor.fetchall.return_value = mock_data
        mock_conn.cursor.return_value = mock_cursor

        res = query_daftar_supplier(mock_conn, cabang_id=1)
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, mock_data)

    def test_query_detail_supplier_ditemukan(self):
        """Skenario Positif: Mengambil detail supplier yang ditemukan."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_row = {'id': 1, 'nama_supplier': 'Supplier A', 'alamat': 'Alamat A', 'telp': '123', 'email': 'a@b.com', 'cabang_id': 1}
        mock_cursor.fetchone.return_value = mock_row
        mock_conn.cursor.return_value = mock_cursor

        res = query_detail_supplier(mock_conn, supplier_id=1, cabang_id=1)
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, mock_row)

    def test_query_detail_supplier_tidak_ditemukan(self):
        """Skenario Negatif: Mengambil detail supplier yang tidak terdaftar."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_conn.cursor.return_value = mock_cursor

        res = query_detail_supplier(mock_conn, supplier_id=99, cabang_id=1)
        self.assertFalse(res.is_success)
        self.assertIn("ERR-VAL-013", res.error_msg)

    def test_query_insert_supplier_sukses(self):
        """Skenario Positif: Penambahan supplier baru sukses."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.lastrowid = 42
        mock_conn.cursor.return_value = mock_cursor

        res = query_insert_supplier(mock_conn, 'Supplier Baru', 'Alamat Baru', '081', 'baru@sup.com', 1)
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, 42)
        mock_conn.commit.assert_called_once()

    def test_query_update_supplier_sukses(self):
        """Skenario Positif: Pembaruan data supplier sukses."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1
        mock_conn.cursor.return_value = mock_cursor

        res = query_update_supplier(mock_conn, 1, 'Nama Edit', 'Alamat Edit', '082', 'edit@sup.com', 1)
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, 1)
        mock_conn.commit.assert_called_once()

    def test_query_delete_supplier_sukses(self):
        """Skenario Positif: Penghapusan supplier sukses tanpa relasi utang aktif."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.side_effect = [{'count': 0}, None]
        mock_cursor.rowcount = 1
        mock_conn.cursor.return_value = mock_cursor

        res = query_delete_supplier(mock_conn, supplier_id=1, cabang_id=1)
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, 1)
        mock_conn.commit.assert_called_once()

    def test_query_delete_supplier_dengan_utang_aktif(self):
        """Skenario Negatif: Menolak penghapusan supplier jika ada utang aktif."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'count': 1}
        mock_conn.cursor.return_value = mock_cursor

        res = query_delete_supplier(mock_conn, supplier_id=1, cabang_id=1)
        self.assertFalse(res.is_success)
        self.assertIn("ERR-REL-136", res.error_msg)
        mock_conn.commit.assert_not_called()

    def test_query_cek_duplikat_nama_ada(self):
        """Skenario Positif: Cek duplikasi mengembalikan data jika nama sudah ada."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_row = {'id': 2, 'nama_supplier': 'Supplier A'}
        mock_cursor.fetchone.return_value = mock_row
        mock_conn.cursor.return_value = mock_cursor

        res = query_cek_nama_supplier_duplikat(mock_conn, 'Supplier A', cabang_id=1)
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, mock_row)

    def test_query_cek_duplikat_nama_tidak_ada(self):
        """Skenario Positif: Cek duplikasi mengembalikan None jika nama unik."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_conn.cursor.return_value = mock_cursor

        res = query_cek_nama_supplier_duplikat(mock_conn, 'Nama Unik', cabang_id=1)
        self.assertTrue(res.is_success)
        self.assertIsNone(res.data)


if __name__ == '__main__':
    unittest.main()
