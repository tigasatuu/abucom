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
import pytest

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

    def setUp(self):
        """Mempersiapkan clean state sebelum setiap pengujian unit."""
        self.default_cabang_id = 1

    def tearDown(self):
        """Membersihkan mock state setelah pengujian unit selesai."""
        patch.stopall()

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
    def test_simpan_riwayat_harga_valid(
        self, mock_audit, mock_tx, mock_check_sup, mock_check_brg
    ):
        """Skenario Positif: Menyimpan data riwayat harga beli supplier baru dengan parameter input yang valid."""
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
    @patch('db.query_builder.get_riwayat_harga_by_barang')
    def test_ambil_riwayat_harga_berdasarkan_supplier(self, mock_get_riwayat, mock_check_brg):
        """Skenario Positif: Mengambil daftar/list riwayat harga beli berdasarkan ID_Supplier tertentu secara akurat."""
        mock_check_brg.return_value = True
        mock_data = [
            {'id': 1, 'tanggal_pembelian': '2026-06-08', 'nama_supplier': 'Supplier A', 'harga_beli': Decimal('40000.0000'), 'supplier_id': 5},
            {'id': 2, 'tanggal_pembelian': '2026-06-01', 'nama_supplier': 'Supplier B', 'harga_beli': Decimal('42000.0000'), 'supplier_id': 10}
        ]
        mock_get_riwayat.return_value = DBResult(True, mock_data, None)

        mock_conn = MagicMock()
        res = ambil_komparasi_harga_supplier(102, 1, mock_conn)

        self.assertTrue(res.is_success)
        self.assertEqual(len(res.data), 2)
        # Verifikasi bahwa kita bisa mencocokkan supplier_id tertentu secara akurat
        supplier_5_entries = [item for item in res.data if item.supplier_id == 5]
        self.assertEqual(len(supplier_5_entries), 1)
        self.assertEqual(supplier_5_entries[0].nama_supplier, 'Supplier A')
        self.assertEqual(supplier_5_entries[0].harga_beli, Decimal('40000.0000'))

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    @patch('db.query_builder.execute_acid_transaction')
    @patch('middleware.audit_logger.log_audit_trail')
    @patch('db.query_builder.get_riwayat_harga_by_barang')
    def test_proses_update_riwayat_harga_tercatat_lama(
        self, mock_get_riwayat, mock_audit, mock_tx, mock_check_sup, mock_check_brg
    ):
        """Skenario Positif: Menambahkan update riwayat harga baru ke supplier yang sudah ada, memastikan historical data utuh."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        mock_tx.return_value = DBResult(True, [13, Decimal('40000.0000')], None)
        mock_audit.return_value = DBResult(True, 99, None)

        mock_conn = MagicMock()
        res = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli=Decimal("38000.0000"),
            tanggal_pembelian="2026-06-09",
            cabang_id=1,
            db_connection=mock_conn
        )
        self.assertTrue(res.is_success)

        # Simulasikan database mengembalikan data riwayat lama dan baru untuk supplier 5
        mock_data = [
            {'id': 13, 'tanggal_pembelian': '2026-06-09', 'nama_supplier': 'Supplier A', 'harga_beli': Decimal('38000.0000'), 'supplier_id': 5},
            {'id': 1, 'tanggal_pembelian': '2026-06-08', 'nama_supplier': 'Supplier A', 'harga_beli': Decimal('40000.0000'), 'supplier_id': 5}
        ]
        mock_get_riwayat.return_value = DBResult(True, mock_data, None)

        res_comp = ambil_komparasi_harga_supplier(102, 1, mock_conn)
        self.assertTrue(res_comp.is_success)
        self.assertEqual(len(res_comp.data), 2)
        # Pastikan data terurut dan riwayat lama tetap ada
        self.assertEqual(res_comp.data[0].harga_beli, Decimal('38000.0000'))
        self.assertEqual(res_comp.data[1].harga_beli, Decimal('40000.0000'))
        self.assertEqual(res_comp.data[0].supplier_id, 5)
        self.assertEqual(res_comp.data[1].supplier_id, 5)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    def test_simpan_riwayat_harga_supplier_tidak_valid(self, mock_check_sup, mock_check_brg):
        """Skenario Negatif: Mencoba menyimpan riwayat harga dengan ID_Supplier yang tidak terdaftar/fiktif."""
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
    @patch('db.query_builder.get_riwayat_harga_by_barang')
    def test_ambil_riwayat_harga_supplier_tidak_ada_transaksi(self, mock_get_riwayat, mock_check_brg):
        """Skenario Negatif: Mengambil riwayat dari supplier/barang yang belum pernah memiliki transaksi/riwayat."""
        mock_check_brg.return_value = True
        mock_get_riwayat.return_value = DBResult(True, [], None) # database returns empty

        mock_conn = MagicMock()
        res = ambil_komparasi_harga_supplier(102, 1, mock_conn)
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, [])

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    def test_simpan_riwayat_harga_negatif_atau_nol(self, mock_check_sup, mock_check_brg):
        """Skenario Negatif: Menginput harga beli dengan nilai tidak wajar/ekstrem (0 atau negatif)."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        mock_conn = MagicMock()

        res_nol = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli=Decimal("0.0000"),
            tanggal_pembelian="2026-06-08",
            cabang_id=1,
            db_connection=mock_conn
        )
        self.assertFalse(res_nol.is_success)
        self.assertIn("Harga beli harus berupa angka positif", res_nol.error_msg)

        res_negatif = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli=Decimal("-500.0000"),
            tanggal_pembelian="2026-06-08",
            cabang_id=1,
            db_connection=mock_conn
        )
        self.assertFalse(res_negatif.is_success)
        self.assertIn("Harga beli harus berupa angka positif", res_negatif.error_msg)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    def test_simpan_riwayat_harga_ekstrem_overflow(self, mock_check_sup, mock_check_brg):
        """Skenario Negatif: Menginput harga beli melebihi batas maksimum database."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        mock_conn = MagicMock()

        res = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli=Decimal("1000000000000000.0000"), # 16 digits
            tanggal_pembelian="2026-06-08",
            cabang_id=1,
            db_connection=mock_conn
        )
        self.assertFalse(res.is_success)
        self.assertIn("Harga beli melebihi batas maksimum", res.error_msg)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    @patch('db.query_builder.execute_acid_transaction')
    def test_simpan_riwayat_error_internal_db(self, mock_tx, mock_check_sup, mock_check_brg):
        """Skenario Negatif: Menyimulasikan database/sistem gagal memproses (exception) menggunakan mocking."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        
        # Simulasikan exception fatal pada transaksi database
        mock_tx.side_effect = Exception("MySQL Connection Timeout")

        mock_conn = MagicMock()
        
        # Menggunakan pytest.raises untuk menangkap exception sesuai requirement
        with pytest.raises(Exception) as excinfo:
            proses_catat_riwayat_harga(
                barang_id=102,
                supplier_id=5,
                harga_beli=Decimal("40000.0000"),
                tanggal_pembelian="2026-06-08",
                cabang_id=1,
                db_connection=mock_conn
            )
        self.assertIn("MySQL Connection Timeout", str(excinfo.value))

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    def test_simpan_riwayat_tipe_data_salah(self, mock_check_sup, mock_check_brg):
        """Validasi Input: Menguji penyimpanan data dengan tipe data salah atau mandatory field None."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        mock_conn = MagicMock()

        # Harga beli diisi string non-numerik yang tidak bisa dikonversi ke Decimal
        res = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli="gratis",
            tanggal_pembelian="2026-06-08",
            cabang_id=1,
            db_connection=mock_conn
        )
        self.assertFalse(res.is_success)
        self.assertIn("Harga beli harus berupa angka desimal", res.error_msg)

        # Mandatory field (tanggal_pembelian) disuplai dengan None, memicu TypeError di strptime
        with pytest.raises(TypeError):
            proses_catat_riwayat_harga(
                barang_id=102,
                supplier_id=5,
                harga_beli=Decimal("40000.0000"),
                tanggal_pembelian=None,
                cabang_id=1,
                db_connection=mock_conn
            )

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
    def test_proses_catat_riwayat_harga_tanggal_invalid(self, mock_check_sup, mock_check_brg):
        """Skenario Negatif: Format tanggal tidak valid (bukan YYYY-MM-DD)."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        mock_conn = MagicMock()

        res = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli=Decimal("40000.0000"),
            tanggal_pembelian="08-06-2026", # format salah
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

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    @patch('middleware.audit_logger.log_audit_trail')
    def test_proses_catat_riwayat_harga_eksekusi_sql_internal(
        self, mock_audit, mock_check_sup, mock_check_brg
    ):
        """Menguji eksekusi query internal op_insert_riwayat dan op_update_barang_harga (tanpa mock execute_acid_transaction)."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        mock_audit.return_value = DBResult(True, 99, None)

        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.lastrowid = 15
        mock_cursor.fetchone.return_value = {'harga_beli': Decimal('42000.0000')}
        mock_conn.cursor.return_value = mock_cursor

        res = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli=Decimal("40000.0000"),
            tanggal_pembelian="2026-06-08",
            cabang_id=1,
            db_connection=mock_conn
        )

        self.assertTrue(res.is_success)
        self.assertEqual(res.data['last_insert_id'], 15)
        self.assertTrue(mock_cursor.execute.called)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    @patch('db.query_builder.execute_acid_transaction')
    def test_proses_catat_riwayat_harga_rollback_exception(
        self, mock_tx, mock_check_sup, mock_check_brg
    ):
        """Menguji penanganan exception saat rollback koneksi db."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        mock_tx.return_value = DBResult(True, [12, Decimal('42000.0000')], None)

        mock_conn = MagicMock()
        mock_conn.rollback.side_effect = Exception("Rollback crash")

        res = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli=Decimal("40000.0000"),
            tanggal_pembelian="2026-06-08",
            cabang_id=1,
            db_connection=mock_conn
        )
        self.assertTrue(res.is_success)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.check_supplier_exists')
    @patch('db.query_builder.execute_acid_transaction')
    def test_proses_catat_riwayat_harga_transaksi_gagal(
        self, mock_tx, mock_check_sup, mock_check_brg
    ):
        """Menguji kegagalan transaksi database (is_success=False) tanpa exception."""
        mock_check_brg.return_value = True
        mock_check_sup.return_value = True
        mock_tx.return_value = DBResult(False, None, "ERR-DB-TX: Transaction failed simulated")

        mock_conn = MagicMock()
        res = proses_catat_riwayat_harga(
            barang_id=102,
            supplier_id=5,
            harga_beli=Decimal("40000.0000"),
            tanggal_pembelian="2026-06-08",
            cabang_id=1,
            db_connection=mock_conn
        )
        self.assertFalse(res.is_success)
        self.assertEqual(res.error_msg, "ERR-DB-TX: Transaction failed simulated")

    @patch('db.query_builder.check_barang_exists')
    def test_ambil_komparasi_harga_supplier_barang_tidak_ada(self, mock_check_brg):
        """Skenario Negatif: Mengambil komparasi harga untuk barang yang tidak terdaftar."""
        mock_check_brg.return_value = False
        mock_conn = MagicMock()
        res = ambil_komparasi_harga_supplier(999, 1, mock_conn)
        self.assertFalse(res.is_success)
        self.assertIn("ID barang", res.error_msg)
        self.assertIn("tidak terdaftar", res.error_msg)

    @patch('db.query_builder.check_barang_exists')
    @patch('db.query_builder.get_riwayat_harga_by_barang')
    def test_ambil_komparasi_harga_supplier_db_gagal(self, mock_get_riwayat, mock_check_brg):
        """Skenario Negatif: Gagal mengambil komparasi harga karena error database."""
        mock_check_brg.return_value = True
        mock_get_riwayat.return_value = DBResult(False, None, "Database error")

        mock_conn = MagicMock()
        res = ambil_komparasi_harga_supplier(102, 1, mock_conn)
        self.assertFalse(res.is_success)
        self.assertEqual(res.error_msg, "Database error")

    @patch('db.query_builder.get_supplier_termurah_by_barang')
    def test_cari_supplier_termurah_db_gagal(self, mock_termurah):
        """Skenario Negatif: Gagal mencari supplier termurah karena error database."""
        mock_termurah.return_value = DBResult(False, None, "Database error")

        mock_conn = MagicMock()
        res = cari_supplier_termurah(102, 1, mock_conn)
        self.assertFalse(res.is_success)
        self.assertEqual(res.error_msg, "Database error")


if __name__ == '__main__':
    unittest.main()
