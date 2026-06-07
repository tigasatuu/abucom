"""
Nama Modul: test_kelola_barang.py
Deskripsi: Unit testing deterministic terisolasi penuh (tanpa koneksi DB riil)
           untuk fungsi validasi, margin, dan audit payload pada logic/bom_hpp.py.
Author: Senior Python Backend Engineer & Inventory Management Specialist
Tanggal: 2026-06-07
"""

import unittest
from decimal import Decimal
import json

from logic.bom_hpp import (
    validasi_data_barang,
    hitung_margin_barang,
    buat_audit_payload_barang,
    hitung_biaya_komponen,
    hitung_hpp_produk,
    proses_pemotongan_stok,
    BOMKomponen
)


class TestKelolaBarangLogic(unittest.TestCase):
    """Suite unit testing untuk fungsi-fungsi fungsional kelola barang."""

    def test_validasi_retail_atk_sukses(self):
        """Skenario Positif: Validasi data Retail ATK yang lengkap dan valid."""
        raw_data = {
            'nama_barang': 'Kertas HVS A4 80gr',
            'tipe_barang': 'Retail_ATK',
            'satuan_uom': 'Rim',
            'stok_saat_ini': '15.5',
            'harga_beli': '45000',
            'harga_retail': '55000',
            'harga_grosir': '52000',
            'min_grosir': '5',
            'harga_mitra': '50000',
            'cabang_id': '1'
        }
        res = validasi_data_barang(raw_data)
        self.assertTrue(res.is_valid)
        self.assertIsNone(res.error_msg)
        cleaned = res.cleaned_data
        
        self.assertEqual(cleaned['nama_barang'], 'Kertas HVS A4 80gr')
        self.assertEqual(cleaned['tipe_barang'], 'Retail_ATK')
        self.assertEqual(cleaned['satuan_uom'], 'Rim')
        self.assertEqual(cleaned['stok_saat_ini'], Decimal('15.5000'))
        self.assertEqual(cleaned['harga_beli'], Decimal('45000.0000'))
        self.assertEqual(cleaned['harga_retail'], Decimal('55000.0000'))
        self.assertEqual(cleaned['harga_grosir'], Decimal('52000.0000'))
        self.assertEqual(cleaned['min_grosir'], Decimal('5.0000'))
        self.assertEqual(cleaned['harga_mitra'], Decimal('50000.0000'))
        self.assertEqual(cleaned['cabang_id'], 1)

    def test_validasi_bahan_baku_sukses(self):
        """Skenario Positif: Validasi Bahan Baku valid, auto-set harga retail/grosir/mitra = 0."""
        raw_data = {
            'nama_barang': 'Karet Stempel Runaflek',
            'tipe_barang': 'Bahan_Baku',
            'satuan_uom': 'Meter_Persegi',
            'stok_saat_ini': '2.4',
            'harga_beli': '120000',
            'cabang_id': '2'
        }
        res = validasi_data_barang(raw_data)
        self.assertTrue(res.is_valid)
        cleaned = res.cleaned_data
        
        self.assertEqual(cleaned['nama_barang'], 'Karet Stempel Runaflek')
        self.assertEqual(cleaned['tipe_barang'], 'Bahan_Baku')
        self.assertEqual(cleaned['stok_saat_ini'], Decimal('2.4000'))
        self.assertEqual(cleaned['harga_beli'], Decimal('120000.0000'))
        # Auto-set prices to 0
        self.assertEqual(cleaned['harga_retail'], Decimal('0.0000'))
        self.assertEqual(cleaned['harga_grosir'], Decimal('0.0000'))
        self.assertEqual(cleaned['harga_mitra'], Decimal('0.0000'))
        self.assertEqual(cleaned['min_grosir'], Decimal('1.0000'))
        self.assertEqual(cleaned['cabang_id'], 2)

    def test_validasi_nama_kosong(self):
        """Skenario Negatif: Nama barang kosong atau hanya spasi."""
        raw_data = {
            'nama_barang': '   ',
            'tipe_barang': 'Retail_ATK',
            'satuan_uom': 'Pcs',
            'stok_saat_ini': '10',
            'harga_beli': '1000',
            'harga_retail': '1500',
            'harga_grosir': '1300',
            'min_grosir': '10',
            'harga_mitra': '1200'
        }
        res = validasi_data_barang(raw_data)
        self.assertFalse(res.is_valid)
        self.assertIn("tidak boleh kosong", res.error_msg)

    def test_validasi_nama_terlalu_panjang(self):
        """Skenario Negatif: Nama barang melebihi 100 karakter."""
        raw_data = {
            'nama_barang': 'A' * 101,
            'tipe_barang': 'Retail_ATK',
            'satuan_uom': 'Pcs',
            'stok_saat_ini': '10',
            'harga_beli': '1000',
            'harga_retail': '1500',
            'harga_grosir': '1300',
            'min_grosir': '10',
            'harga_mitra': '1200'
        }
        res = validasi_data_barang(raw_data)
        self.assertFalse(res.is_valid)
        self.assertIn("maksimal 100 karakter", res.error_msg)

    def test_validasi_tipe_tidak_valid(self):
        """Skenario Negatif: Tipe barang bukan Retail_ATK atau Bahan_Baku."""
        raw_data = {
            'nama_barang': 'Barang A',
            'tipe_barang': 'Jasa_Cetak',
            'satuan_uom': 'Pcs',
            'stok_saat_ini': '10',
            'harga_beli': '1000'
        }
        res = validasi_data_barang(raw_data)
        self.assertFalse(res.is_valid)
        self.assertIn("Tipe barang harus", res.error_msg)

    def test_validasi_uom_tidak_valid(self):
        """Skenario Negatif: Satuan UoM tidak didukung."""
        raw_data = {
            'nama_barang': 'Barang A',
            'tipe_barang': 'Bahan_Baku',
            'satuan_uom': 'Kg',  # Tidak valid
            'stok_saat_ini': '10',
            'harga_beli': '1000'
        }
        res = validasi_data_barang(raw_data)
        self.assertFalse(res.is_valid)
        self.assertIn("Satuan UoM tidak valid", res.error_msg)

    def test_validasi_stok_negatif(self):
        """Skenario Negatif: Input stok bernilai negatif."""
        raw_data = {
            'nama_barang': 'Barang A',
            'tipe_barang': 'Bahan_Baku',
            'satuan_uom': 'Pcs',
            'stok_saat_ini': '-1.5',
            'harga_beli': '1000'
        }
        res = validasi_data_barang(raw_data)
        self.assertFalse(res.is_valid)
        self.assertIn("tidak boleh negatif", res.error_msg)

    def test_validasi_harga_beli_negatif(self):
        """Skenario Negatif: Input harga beli bernilai negatif."""
        raw_data = {
            'nama_barang': 'Barang A',
            'tipe_barang': 'Bahan_Baku',
            'satuan_uom': 'Pcs',
            'stok_saat_ini': '10',
            'harga_beli': '-500'
        }
        res = validasi_data_barang(raw_data)
        self.assertFalse(res.is_valid)
        self.assertIn("tidak boleh negatif", res.error_msg)

    def test_validasi_min_grosir_nol(self):
        """Skenario Negatif: Min grosir bernilai nol untuk Retail ATK."""
        raw_data = {
            'nama_barang': 'Barang A',
            'tipe_barang': 'Retail_ATK',
            'satuan_uom': 'Pcs',
            'stok_saat_ini': '10',
            'harga_beli': '1000',
            'harga_retail': '1500',
            'harga_grosir': '1300',
            'min_grosir': '0',
            'harga_mitra': '1200'
        }
        res = validasi_data_barang(raw_data)
        self.assertFalse(res.is_valid)
        self.assertIn("harus lebih besar dari nol", res.error_msg)

    def test_validasi_desimal_tidak_valid(self):
        """Skenario Negatif: Input kuantitas/harga berupa string non-numerik (ERR-VAL-009)."""
        raw_data = {
            'nama_barang': 'Barang A',
            'tipe_barang': 'Retail_ATK',
            'satuan_uom': 'Pcs',
            'stok_saat_ini': 'sepuluh',
            'harga_beli': '1000',
            'harga_retail': '1500',
            'harga_grosir': '1300',
            'min_grosir': '10',
            'harga_mitra': '1200'
        }
        res = validasi_data_barang(raw_data)
        self.assertFalse(res.is_valid)
        self.assertIn("ERR-VAL-009", res.error_msg)

    def test_hitung_margin_normal(self):
        """Skenario Positif: Perhitungan margin keuntungan kotor normal."""
        margin = hitung_margin_barang(Decimal('100.0000'), Decimal('60.0000'))
        self.assertEqual(margin, Decimal('40.00'))

    def test_hitung_margin_nol(self):
        """Skenario Positif: Perhitungan margin ketika harga jual sama dengan harga beli."""
        margin = hitung_margin_barang(Decimal('100.0000'), Decimal('100.0000'))
        self.assertEqual(margin, Decimal('0.00'))

    def test_hitung_margin_harga_jual_nol(self):
        """Skenario Positif: Mitigasi pembagian dengan nol ketika harga jual = 0."""
        margin = hitung_margin_barang(Decimal('0.0000'), Decimal('50.0000'))
        self.assertEqual(margin, Decimal('0.00'))

    def test_hitung_margin_rugi(self):
        """Skenario Positif: Margin negatif jika harga jual < harga beli (rugi)."""
        margin = hitung_margin_barang(Decimal('50.0000'), Decimal('80.0000'))
        self.assertEqual(margin, Decimal('-60.00'))

    def test_buat_audit_payload_insert(self):
        """Skenario Positif: Payload audit untuk INSERT (old_data is None)."""
        new_data = {
            'nama_barang': 'Barang Baru',
            'harga_beli': Decimal('1000.5000')
        }
        old_json, new_json = buat_audit_payload_barang('INSERT', None, new_data)
        self.assertEqual(old_json, 'null')
        self.assertIn('"nama_barang": "Barang Baru"', new_json)
        self.assertIn('"harga_beli": 1000.5', new_json) # Decimal dikonversi ke float

    def test_buat_audit_payload_delete(self):
        """Skenario Positif: Payload audit untuk DELETE (new_data is None)."""
        old_data = {
            'nama_barang': 'Barang Dihapus',
            'stok_saat_ini': Decimal('0.0000')
        }
        old_json, new_json = buat_audit_payload_barang('DELETE', old_data, None)
        self.assertEqual(new_json, 'null')
        self.assertIn('"nama_barang": "Barang Dihapus"', old_json)
        self.assertIn('"stok_saat_ini": 0.0', old_json)

    def test_buat_audit_payload_update(self):
        """Skenario Positif: Payload audit untuk UPDATE (keduanya terisi)."""
        old_data = {'harga_retail': Decimal('1000.0000')}
        new_data = {'harga_retail': Decimal('1200.0000')}
        old_json, new_json = buat_audit_payload_barang('UPDATE', old_data, new_data)
        
        old_dict = json.loads(old_json)
        new_dict = json.loads(new_json)
        self.assertEqual(old_dict['harga_retail'], 1000.0)
        self.assertEqual(new_dict['harga_retail'], 1200.0)

    def test_hitung_biaya_komponen_dan_hpp(self):
        """Skenario Positif: Perhitungan biaya komponen dan total HPP produk."""
        comp1 = BOMKomponen(bahan_baku_id=1, nama_barang='Bahan A', kuantitas=Decimal('2.5000'), harga_beli=Decimal('10000.0000'))
        comp2 = BOMKomponen(bahan_baku_id=2, nama_barang='Bahan B', kuantitas=Decimal('1.2500'), harga_beli=Decimal('20000.0000'))
        
        self.assertEqual(hitung_biaya_komponen(comp1.kuantitas, comp1.harga_beli), Decimal('25000.0000'))
        self.assertEqual(hitung_biaya_komponen(comp2.kuantitas, comp2.harga_beli), Decimal('25000.0000'))
        
        hpp = hitung_hpp_produk([comp1, comp2])
        self.assertEqual(hpp, Decimal('50000.0000'))

    def test_proses_pemotongan_stok_empty(self):
        """Skenario Positif: Memanggil proses pemotongan stok dengan komponen kosong."""
        from unittest.mock import MagicMock
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        
        res = proses_pemotongan_stok([], 1, mock_conn)
        self.assertTrue(res.is_success)
        self.assertFalse(res.data)
        self.assertIsNone(res.error_msg)
        
        mock_conn.start_transaction.assert_called_once()
        mock_conn.commit.assert_called_once()


    def test_validasi_data_barang_missing_nama_field(self):
        """Skenario Negatif: Key nama_barang tidak ada."""
        raw_data = {
            'tipe_barang': 'Retail_ATK',
            'satuan_uom': 'Pcs',
            'stok_saat_ini': '10',
            'harga_beli': '1000'
        }
        res = validasi_data_barang(raw_data)
        self.assertFalse(res.is_valid)
        self.assertIn("Nama barang wajib diisi", res.error_msg)

    def test_validasi_data_barang_empty_numeric_fields(self):
        """Skenario Negatif: Nilai stok atau harga kosong/null."""
        base_data = {
            'nama_barang': 'Barang A',
            'tipe_barang': 'Retail_ATK',
            'satuan_uom': 'Pcs',
            'stok_saat_ini': '',
            'harga_beli': '1000'
        }
        res = validasi_data_barang(base_data)
        self.assertFalse(res.is_valid)
        self.assertIn("Stok saat ini wajib diisi", res.error_msg)

    def test_validasi_data_barang_invalid_cabang_id(self):
        """Skenario Negatif: Cabang ID <= 0 atau non-integer."""
        base_data = {
            'nama_barang': 'Barang A',
            'tipe_barang': 'Retail_ATK',
            'satuan_uom': 'Pcs',
            'stok_saat_ini': '10',
            'harga_beli': '1000',
            'harga_retail': '1500',
            'harga_grosir': '1300',
            'min_grosir': '10',
            'harga_mitra': '1200',
            'cabang_id': '0'
        }
        res = validasi_data_barang(base_data)
        self.assertFalse(res.is_valid)
        self.assertIn("Cabang ID harus berupa integer positif", res.error_msg)
        
        base_data['cabang_id'] = 'abc'
        res = validasi_data_barang(base_data)
        self.assertFalse(res.is_valid)
        self.assertIn("Cabang ID harus berupa integer positif", res.error_msg)

    def test_validasi_data_barang_general_exception(self):
        """Skenario Negatif: Memicu exception umum (misal passing non-dict)."""
        res = validasi_data_barang("bukan_dict")
        self.assertFalse(res.is_valid)
        self.assertIn("Terjadi kesalahan validasi", res.error_msg)

    def test_convert_decimals_list(self):
        """Skenario Positif: Convert list berisi Decimal."""
        old_data = [{'value': Decimal('12.5000')}]
        old_json, _ = buat_audit_payload_barang('UPDATE', old_data, None)
        self.assertEqual(old_json, '[{"value": 12.5}]')


if __name__ == '__main__':
    unittest.main()
