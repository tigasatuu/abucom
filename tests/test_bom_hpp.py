"""
Nama Modul: test_bom_hpp.py
Deskripsi: Unit testing deterministic terisolasi untuk fungsi kalkulasi
           HPP dan BOM desimal pada logic/bom_hpp.py.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import unittest
from decimal import Decimal
import json

from logic.bom_hpp import (
    validasi_kuantitas_bom,
    validasi_bahan_baku_id,
    buat_audit_payload_bom,
    hitung_biaya_komponen,
    hitung_hpp_produk,
    BOMKomponen
)


class TestBOMHPPLogic(unittest.TestCase):
    """Suite unit testing untuk logic BOM dan HPP."""

    def test_validasi_kuantitas_bom_valid(self):
        """Skenario Positif: Input kuantitas desimal valid."""
        res = validasi_kuantitas_bom("0.0500")
        self.assertTrue(res.is_valid)
        self.assertEqual(res.cleaned_data, Decimal("0.0500"))
        self.assertIsNone(res.error_msg)

        res2 = validasi_kuantitas_bom("1.0000")
        self.assertTrue(res2.is_valid)
        self.assertEqual(res2.cleaned_data, Decimal("1.0000"))

    def test_validasi_kuantitas_bom_nol(self):
        """Skenario Negatif: Kuantitas bernilai nol."""
        res = validasi_kuantitas_bom("0.0000")
        self.assertFalse(res.is_valid)
        self.assertIn("ERR-VAL-007", res.error_msg)

    def test_validasi_kuantitas_bom_negatif(self):
        """Skenario Negatif: Kuantitas bernilai negatif."""
        res = validasi_kuantitas_bom("-1.5")
        self.assertFalse(res.is_valid)
        self.assertIn("ERR-VAL-007", res.error_msg)

    def test_validasi_kuantitas_bom_non_numerik(self):
        """Skenario Negatif: Kuantitas berupa string non-numerik."""
        res = validasi_kuantitas_bom("abc")
        self.assertFalse(res.is_valid)
        self.assertIn("ERR-VAL-007", res.error_msg)

    def test_validasi_kuantitas_bom_kosong(self):
        """Skenario Negatif: Kuantitas kosong atau None."""
        res1 = validasi_kuantitas_bom("")
        self.assertFalse(res1.is_valid)
        
        res2 = validasi_kuantitas_bom(None)
        self.assertFalse(res2.is_valid)

    def test_validasi_bahan_baku_id_valid(self):
        """Skenario Positif: ID bahan baku valid."""
        res = validasi_bahan_baku_id("5")
        self.assertTrue(res.is_valid)
        self.assertEqual(res.cleaned_data, 5)

    def test_validasi_bahan_baku_id_nol(self):
        """Skenario Negatif: ID bahan baku bernilai nol."""
        res = validasi_bahan_baku_id("0")
        self.assertFalse(res.is_valid)
        self.assertIn("ERR-VAL-008", res.error_msg)

    def test_validasi_bahan_baku_id_negatif(self):
        """Skenario Negatif: ID bahan baku bernilai negatif."""
        res = validasi_bahan_baku_id("-1")
        self.assertFalse(res.is_valid)
        self.assertIn("ERR-VAL-008", res.error_msg)

    def test_validasi_bahan_baku_id_non_integer(self):
        """Skenario Negatif: ID bahan baku desimal atau string."""
        res1 = validasi_bahan_baku_id("1.5")
        self.assertFalse(res1.is_valid)
        
        res2 = validasi_bahan_baku_id("abc")
        self.assertFalse(res2.is_valid)

    def test_hitung_biaya_komponen(self):
        """Skenario Positif: Perhitungan biaya komponen presisi desimal."""
        # Karet flash: 0.0025 * 100000 = 250
        biaya1 = hitung_biaya_komponen(Decimal('0.0025'), Decimal('100000.0000'))
        self.assertEqual(biaya1, Decimal('250.0000'))

        # Gagang stempel: 1.0 * 4500 = 4500
        biaya2 = hitung_biaya_komponen(Decimal('1.0000'), Decimal('4500.0000'))
        self.assertEqual(biaya2, Decimal('4500.0000'))

        # Pembulatan ROUND_HALF_UP: 0.3333 * 100 = 33.3300
        biaya3 = hitung_biaya_komponen(Decimal('0.3333'), Decimal('100.0000'))
        self.assertEqual(biaya3, Decimal('33.3300'))

    def test_hitung_hpp_produk(self):
        """Skenario Positif: Perhitungan HPP total dari beberapa komponen."""
        comp1 = BOMKomponen(bahan_baku_id=5, nama_barang="Karet Flash", kuantitas=Decimal("0.0025"), harga_beli=Decimal("100000.00"))
        comp2 = BOMKomponen(bahan_baku_id=6, nama_barang="Gagang Stempel", kuantitas=Decimal("1.0000"), harga_beli=Decimal("4500.00"))
        
        hpp = hitung_hpp_produk([comp1, comp2])
        self.assertEqual(hpp, Decimal("4750.0000"))

        # Test empty list
        self.assertEqual(hitung_hpp_produk([]), Decimal("0.0000"))

    def test_buat_audit_payload_bom(self):
        """Skenario Positif: Format payload audit trail BOM JSON."""
        old_data = {"kuantitas_desimal": Decimal("0.0500")}
        new_data = {"kuantitas_desimal": Decimal("0.1000")}
        
        old_json, new_json = buat_audit_payload_bom("UPDATE", old_data, new_data)
        
        old_dict = json.loads(old_json)
        new_dict = json.loads(new_json)
        
        self.assertEqual(old_dict["kuantitas_desimal"], 0.05)
        self.assertEqual(new_dict["kuantitas_desimal"], 0.1)

        # Test insert (old is None)
        old_json_ins, new_json_ins = buat_audit_payload_bom("INSERT", None, new_data)
        self.assertEqual(old_json_ins, "null")
        self.assertEqual(json.loads(new_json_ins)["kuantitas_desimal"], 0.1)

    def test_proses_pemotongan_stok_sukses(self):
        """Skenario Positif: Pemotongan stok bahan baku sukses dengan stok mencukupi."""
        from unittest.mock import MagicMock
        from logic.bom_hpp import proses_pemotongan_stok
        
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        
        # Mock fetchone to return current stock: 10.0000
        mock_cursor.fetchone.return_value = [10.0000]
        
        comp = BOMKomponen(bahan_baku_id=5, nama_barang="Karet Flash", kuantitas=Decimal("2.5000"), harga_beli=Decimal("100.00"))
        
        res = proses_pemotongan_stok([comp], 1, mock_conn)
        
        self.assertTrue(res.is_success)
        self.assertFalse(res.data) # stok_minus_detected should be False
        self.assertIsNone(res.error_msg)
        
        # Verify SELECT query was called
        mock_cursor.execute.assert_any_call(
            "SELECT stok_saat_ini FROM barang WHERE id = %s AND cabang_id = %s FOR UPDATE",
            (5, 1)
        )
        # Verify UPDATE query was called
        mock_cursor.execute.assert_any_call(
            "UPDATE barang SET stok_saat_ini = stok_saat_ini - %s WHERE id = %s AND cabang_id = %s",
            (Decimal("2.5000"), 5, 1)
        )
        mock_conn.commit.assert_called_once()

    def test_proses_pemotongan_stok_negatif(self):
        """Skenario Positif (dengan alert): Pemotongan stok bahan baku sukses tetapi stok menjadi minus/negatif."""
        from unittest.mock import MagicMock
        from logic.bom_hpp import proses_pemotongan_stok
        
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        
        # Mock current stock: 1.0000 (less than quantity 2.5000)
        mock_cursor.fetchone.return_value = [1.0000]
        
        comp = BOMKomponen(bahan_baku_id=5, nama_barang="Karet Flash", kuantitas=Decimal("2.5000"), harga_beli=Decimal("100.00"))
        
        res = proses_pemotongan_stok([comp], 1, mock_conn)
        
        self.assertTrue(res.is_success)
        self.assertTrue(res.data) # stok_minus_detected should be True
        self.assertIsNone(res.error_msg)
        
        mock_conn.commit.assert_called_once()

    def test_proses_pemotongan_stok_error(self):
        """Skenario Negatif: Pemotongan gagal karena error database, harus memicu rollback."""
        from unittest.mock import MagicMock
        from logic.bom_hpp import proses_pemotongan_stok
        
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        
        # Trigger exception on execute
        mock_cursor.execute.side_effect = Exception("Database disk full")
        
        comp = BOMKomponen(bahan_baku_id=5, nama_barang="Karet Flash", kuantitas=Decimal("2.5000"), harga_beli=Decimal("100.00"))
        
        res = proses_pemotongan_stok([comp], 1, mock_conn)
        
        self.assertFalse(res.is_success)
        self.assertIn("Gagal memotong stok bahan baku", res.error_msg)
        
        mock_conn.rollback.assert_called_once()
        mock_conn.commit.assert_not_called()

