"""
Nama Modul: test_uom_converter.py
Deskripsi: Unit testing deterministic terisolasi penuh (tanpa koneksi DB riil)
           untuk fungsi konversi, faktor balik, validasi, dan pencarian jalur
           pada logic/uom_converter.py.
Author: Antigravity AI
Tanggal: 2026-06-08
"""

import unittest
from decimal import Decimal
from logic.uom_converter import (
    konversi_satuan,
    hitung_faktor_konversi_balik,
    validasi_data_satuan_ukur,
    validasi_data_konversi,
    cari_jalur_konversi,
    KonversiRecord
)


class TestUomConverterLogic(unittest.TestCase):
    """Suite unit testing untuk fungsi-fungsi fungsional uom_converter."""

    def test_konversi_satuan_sukses(self):
        """Skenario Positif: Konversi nilai dengan faktor desimal valid."""
        nilai = Decimal('2.5000')
        faktor = Decimal('500.0000')
        res = konversi_satuan(nilai, faktor)
        self.assertEqual(res, Decimal('1250.0000'))

    def test_konversi_satuan_tipe_float_error(self):
        """Skenario Negatif: Memicu TypeError jika menggunakan tipe float."""
        with self.assertRaises(TypeError):
            konversi_satuan(2.5, Decimal('500.0000'))
        with self.assertRaises(TypeError):
            konversi_satuan(Decimal('2.5000'), 500.0)

    def test_hitung_faktor_konversi_balik_sukses(self):
        """Skenario Positif: Menghitung faktor balik dari desimal valid."""
        res = hitung_faktor_konversi_balik(Decimal('500.0000'))
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, Decimal('0.0020'))

    def test_hitung_faktor_konversi_balik_nol_atau_negatif(self):
        """Skenario Negatif: Faktor nol atau negatif harus ditolak."""
        res1 = hitung_faktor_konversi_balik(Decimal('0.0000'))
        self.assertFalse(res1.is_success)
        self.assertIn("ERR-UOM-004", res1.error_msg)

        res2 = hitung_faktor_konversi_balik(Decimal('-1.5000'))
        self.assertFalse(res2.is_success)
        self.assertIn("ERR-UOM-004", res2.error_msg)

    def test_hitung_faktor_konversi_balik_float_error(self):
        """Skenario Negatif: Memicu error jika input berupa float."""
        res = hitung_faktor_konversi_balik(2.0)
        self.assertFalse(res.is_success)
        self.assertIn("ERR-VAL-050", res.error_msg)

    def test_validasi_data_satuan_ukur_sukses(self):
        """Skenario Positif: Validasi data satuan ukur lengkap dan valid."""
        raw_data = {
            'nama_satuan': 'Rim',
            'kategori_satuan': 'Kuantitas',
            'simbol': 'rim',
            'keterangan': 'Satuan rim kertas'
        }
        res = validasi_data_satuan_ukur(raw_data)
        self.assertTrue(res.is_success)
        self.assertIsNone(res.error_msg)
        self.assertEqual(res.data['nama_satuan'], 'Rim')
        self.assertEqual(res.data['kategori_satuan'], 'Kuantitas')

    def test_validasi_data_satuan_ukur_kosong(self):
        """Skenario Negatif: Nama satuan kosong atau missing."""
        res1 = validasi_data_satuan_ukur({'kategori_satuan': 'Kuantitas'})
        self.assertFalse(res1.is_success)
        self.assertIn("ERR-VAL-009", res1.error_msg)

        res2 = validasi_data_satuan_ukur({'nama_satuan': '  ', 'kategori_satuan': 'Kuantitas'})
        self.assertFalse(res2.is_success)
        self.assertIn("ERR-VAL-009", res2.error_msg)

    def test_validasi_data_satuan_ukur_nama_terlalu_panjang(self):
        """Skenario Negatif: Nama satuan melebihi 30 karakter."""
        res = validasi_data_satuan_ukur({
            'nama_satuan': 'A' * 31,
            'kategori_satuan': 'Kuantitas'
        })
        self.assertFalse(res.is_success)
        self.assertIn("maksimal 30 karakter", res.error_msg)

    def test_validasi_data_satuan_ukur_kategori_tidak_valid(self):
        """Skenario Negatif: Kategori satuan tidak dikenal."""
        res = validasi_data_satuan_ukur({
            'nama_satuan': 'Meter',
            'kategori_satuan': 'Suhu'
        })
        self.assertFalse(res.is_success)
        self.assertIn("Kategori satuan tidak valid", res.error_msg)

    def test_validasi_data_satuan_ukur_escape_illegal(self):
        """Skenario Negatif: Nama mengandung karakter escape ilegal."""
        res = validasi_data_satuan_ukur({
            'nama_satuan': 'Meter\nKustom',
            'kategori_satuan': 'Panjang'
        })
        self.assertFalse(res.is_success)
        self.assertIn("karakter escape ilegal", res.error_msg)

    def test_validasi_data_konversi_sukses(self):
        """Skenario Positif: Validasi data konversi valid."""
        raw_data = {
            'satuan_asal_id': '1',
            'satuan_tujuan_id': '2',
            'faktor_konversi': '500.0000'
        }
        res = validasi_data_konversi(raw_data)
        self.assertTrue(res.is_success)
        self.assertEqual(res.data['satuan_asal_id'], 1)
        self.assertEqual(res.data['satuan_tujuan_id'], 2)
        self.assertEqual(res.data['faktor_konversi'], Decimal('500.0000'))

    def test_validasi_data_konversi_satuan_sama(self):
        """Skenario Negatif: Menolak konversi antar satuan yang sama."""
        raw_data = {
            'satuan_asal_id': '1',
            'satuan_tujuan_id': '1',
            'faktor_konversi': '1.0000'
        }
        res = validasi_data_konversi(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("ERR-UOM-003", res.error_msg)

    def test_validasi_data_konversi_faktor_nol_atau_negatif(self):
        """Skenario Negatif: Menolak faktor konversi <= 0."""
        raw_data = {
            'satuan_asal_id': '1',
            'satuan_tujuan_id': '2',
            'faktor_konversi': '0.0000'
        }
        res = validasi_data_konversi(raw_data)
        self.assertFalse(res.is_success)
        self.assertIn("ERR-UOM-004", res.error_msg)

    def test_validasi_data_konversi_invalid_ids(self):
        """Skenario Negatif: Menolak ID non-numerik atau non-positif."""
        res1 = validasi_data_konversi({'satuan_asal_id': 'abc', 'satuan_tujuan_id': '2', 'faktor_konversi': '1.0'})
        self.assertFalse(res1.is_success)

        res2 = validasi_data_konversi({'satuan_asal_id': '-1', 'satuan_tujuan_id': '2', 'faktor_konversi': '1.0'})
        self.assertFalse(res2.is_success)

    def test_cari_jalur_konversi_sukses(self):
        """Skenario Positif: Menemukan jalur konversi langsung."""
        records = [
            KonversiRecord(id=1, satuan_asal='Rim', satuan_tujuan='Lembar', faktor_konversi=Decimal('500.0000')),
            KonversiRecord(id=2, satuan_asal='Lusin', satuan_tujuan='Pcs', faktor_konversi=Decimal('12.0000'))
        ]
        res = cari_jalur_konversi('Rim', 'Lembar', records)
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, Decimal('500.0000'))

    def test_cari_jalur_konversi_satuan_sama(self):
        """Skenario Positif: Konversi ke satuan yang sama bernilai 1.0."""
        res = cari_jalur_konversi('Rim', 'Rim', [])
        self.assertTrue(res.is_success)
        self.assertEqual(res.data, Decimal('1.0000'))

    def test_cari_jalur_konversi_tidak_ditemukan(self):
        """Skenario Negatif: Jalur konversi tidak terdaftar."""
        records = [
            KonversiRecord(id=1, satuan_asal='Rim', satuan_tujuan='Lembar', faktor_konversi=Decimal('500.0000'))
        ]
        res = cari_jalur_konversi('Rim', 'Pcs', records)
        self.assertFalse(res.is_success)
        self.assertIn("ERR-UOM-001", res.error_msg)


if __name__ == '__main__':
    unittest.main()
