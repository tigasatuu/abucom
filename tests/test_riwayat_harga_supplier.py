"""
Nama Modul: test_riwayat_harga_supplier.py
Deskripsi: Unit testing deterministic terisolasi (tanpa koneksi DB riil)
           untuk fitur pencatatan dan pelacakan riwayat harga beli supplier.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-08
"""

import unittest
from unittest.mock import MagicMock, patch
from decimal import Decimal
from collections import namedtuple

from logic.bom_hpp import (
    validasi_input_harga_beli,
    proses_catat_riwayat_harga,
    ambil_komparasi_harga_supplier,
    cari_supplier_termurah,
    RiwayatHargaEntry
)
from db.query_builder import (
    insert_riwayat_harga_supplier,
    get_riwayat_harga_by_barang,
    get_supplier_termurah_by_barang,
    update_harga_beli_barang,
    check_barang_exists,
    check_supplier_exists,
    Result as DBResult
)

class TestRiwayatHargaSupplierLogic(unittest.TestCase):
    """Suite unit testing untuk logika bisnis riwayat harga supplier."""

    def test_validasi_input_harga_beli_valid(self):
        """Skenario Positif: Input harga beli desimal valid."""
        res = validasi_input_harga_beli(Decimal("45000.0000"))
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, Decimal("45000.0000"))
        self.assertIsNone(res.error_msg)

        res2 = validasi_input_harga_beli("40000")
        self.assertTrue(res2.is_success)
        self.assertEqual(res2.data, Decimal("40000.0000"))

    def test_validasi_input_harga_beli_nol_atau_negatif(self):
        """Skenario Negatif: Harga beli bernilai nol atau negatif."""
        res1 = validasi_input_harga_beli(Decimal("0.0000"))
        self.assertFalse(res1.is_success)
        self.assertIn("Harga beli harus berupa angka positif", res1.error_msg)

        res2 = validasi_input_harga_beli(Decimal("-150.0000"))
        self.assertFalse(res2.is_success)
        self.assertIn("Harga beli harus berupa angka positif", res2.error_msg)

    def test_validasi_input_harga_beli_overflow(self):
        """Skenario Negatif: Harga beli melebihi batas DECIMAL(15,4)."""
        res = validasi_input_harga_beli(Decimal("1000000000000000.0000")) # 16 digits
        self.assertFalse(res.is_success)
        self.assertIn("Harga beli melebihi batas maksimum", res.error_msg)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    @patch('db.query_builder.execute_acid_transaction')
    @patch('middleware.audit_logger.log_audit_trail')
    def test_proses_catat_riwayat_harga_sukses(
        self, mock_audit, mock_tx, mock_check_sup, mock_check_brg
    ):
        """Skenario Positif: Pencatatan riwayat harga sukses secara transaksional."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        
        # mock execute_acid_transaction returns tuple values (lastrowid, old_harga)
        mock_tx.return_value = DBResult(True, [12, Decimal('42000.0000')], None)
        mock_audit.return_value = DBResult(True, 99, None)

        mock_conn = MagicMock()
        res = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli=Decimal("40000.0000"),
            tanggal_pembelian="2026-06-08",
            cabang_id=1,
            db_connection=mock_conn,
            pengguna_id=1
        )

        self.assertTrue(res.is_success)
        self.assertEqual(res.data['last_insert_id'], 12)
        mock_tx.assert_called_once()
        self.assertEqual(mock_audit.call_count, 2)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    def test_proses_catat_riwayat_harga_barang_tidak_ada(self, mock_check_sup, mock_check_brg):
        """Skenario Negatif: ID barang tidak terdaftar."""
        mock_check_brg.return_value = False
        mock_conn = MagicMock()

        res = proses_catat_riwayat_harga(
            barang_id=999,
            supplier_id=5,
            harga_beli=Decimal("40000.0000"),
            tanggal_pembelian="2026-06-08",
            cabang_id=1,
            db_connection=mock_conn
        )
        self.assertFalse(res.is_success)
        self.assertIn("ID barang tidak terdaftar", res.error_msg)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    def test_proses_catat_riwayat_harga_supplier_tidak_ada(self, mock_check_sup, mock_check_brg):
        """Skenario Negatif: ID supplier tidak terdaftar."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = False
        mock_conn = MagicMock()

        res = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=999,
            harga_beli=Decimal("40000.0000"),
            tanggal_pembelian="2026-06-08",
            cabang_id=1,
            db_connection=mock_conn
        )
        self.assertFalse(res.is_success)
        self.assertIn("ID supplier tidak terdaftar", res.error_msg)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    def test_proses_catat_riwayat_harga_tanggal_invalid(self, mock_check_sup, mock_check_brg):
        """Skenario Negatif: Format tanggal tidak valid."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        mock_conn = MagicMock()

        res = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli=Decimal("40000.0000"),
            tanggal_pembelian="08-06-2026", # invalid format
            cabang_id=1,
            db_connection=mock_conn
        )
        self.assertFalse(res.is_success)
        self.assertIn("Format tanggal tidak valid", res.error_msg)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.get_riwayat_harga_by_barang')
    def test_ambil_komparasi_harga_supplier_sukses(self, mock_get_riwayat, mock_check_brg):
        """Skenario Positif: Mengambil daftar komparasi riwayat harga supplier sukses."""
        mock_check_brg.return_value = True
        mock_data = [
            {'id': 1, 'tanggal_pembelian': '2026-06-08', 'nama_supplier': 'Supplier A', 'harga_beli': Decimal('40000.0000'), 'supplier_id': 2},
            {'id': 2, 'tanggal_pembelian': '2026-06-01', 'nama_supplier': 'Supplier B', 'harga_beli': Decimal('42000.0000'), 'supplier_id': 3}
        ]
        mock_get_riwayat.return_value = DBResult(True, mock_data, None)

        mock_conn = MagicMock()
        res = ambil_komparasi_harga_supplier(102, 1, mock_conn)

        self.assertTrue(res.is_success)
        self.assertEqual(len(res.data), 2)
        self.assertIsInstance(res.data[0], RiwayatHargaEntry)
        self.assertEqual(res.data[0].nama_supplier, 'Supplier A')
        self.assertEqual(res.data[1].harga_beli, Decimal('42000.0000'))

    @patch('db.query_builder.get_supplier_termurah_by_barang')
    def test_cari_supplier_termurah_ditemukan(self, mock_termurah):
        """Skenario Positif: Supplier termurah ditemukan."""
        mock_row = {'supplier_id': 2, 'nama_supplier': 'Supplier A', 'harga_beli': Decimal('40000.0000'), 'tanggal_pembelian': '2026-06-08'}
        mock_termurah.return_value = DBResult(True, mock_row, None)

        mock_conn = MagicMock()
        res = cari_supplier_termurah(102, 1, mock_conn)

        self.assertTrue(res.is_success)
        self.assertIsNotNone(res.data)
        self.assertEqual(res.data.nama_supplier, 'Supplier A')
        self.assertEqual(res.data.harga_beli, Decimal('40000.0000'))

    @patch('db.query_builder.get_supplier_termurah_by_barang')
    def test_cari_supplier_termurah_tidak_ada(self, mock_termurah):
        """Skenario Positif: Tidak ada supplier/riwayat untuk barang tersebut."""
        mock_termurah.return_value = DBResult(True, None, None)

        mock_conn = MagicMock()
        res = cari_supplier_termurah(102, 1, mock_conn)

        self.assertTrue(res.is_success)
        self.assertIsNone(res.data)


if __name__ == '__main__':
    unittest.main()
