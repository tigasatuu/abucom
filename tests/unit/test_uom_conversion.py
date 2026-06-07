"""
Nama Modul: test_uom_conversion.py
Deskripsi: Unit testing komprehensif, terisolasi, dan deterministik untuk
           fungsi konversi satuan ukur dan validasi master UoM di uom_converter.py
           menggunakan pytest.
Author: Senior QA Automation Engineer & AI Testing Agent
Tanggal: 2026-06-08
"""

import pytest
from decimal import Decimal
from logic.uom_converter import (
    konversi_satuan,
    hitung_faktor_konversi_balik,
    validasi_data_satuan_ukur,
    validasi_data_konversi,
    cari_jalur_konversi,
    Result,
    KonversiRecord
)


@pytest.fixture
def fresh_uom_fixtures():
    """Fixture untuk mensimulasikan data UoM dan konversi dalam state yang bersih."""
    daftar_konversi = [
        KonversiRecord(id=1, satuan_asal="Rim", satuan_tujuan="Lembar", faktor_konversi=Decimal("500.0000")),
        KonversiRecord(id=2, satuan_asal="Liter", satuan_tujuan="Mililiter", faktor_konversi=Decimal("1000.0000")),
        KonversiRecord(id=3, satuan_asal="Meter_Persegi", satuan_tujuan="Centimeter_Persegi", faktor_konversi=Decimal("10000.0000")),
        KonversiRecord(id=4, satuan_asal="Karton", satuan_tujuan="Pcs", faktor_konversi=Decimal("24.0000")),
    ]
    return {
        "daftar_konversi": daftar_konversi
    }


# ==============================================================================
# A. SKENARIO POSITIF (HAPPY PATH)
# ==============================================================================

def test_uom_conversion_integer_valid():
    """Skenario Positif 1: Konversi satuan dengan rasio integer bulat."""
    # 1 Rim = 500 Lembar. Konversi 2 Rim -> 1000 Lembar
    res = konversi_satuan(Decimal("2.0000"), Decimal("500.0000"))
    assert res == Decimal("1000.0000")

    # 3 Karton = 72 Pcs
    res2 = konversi_satuan(Decimal("3"), Decimal("24"))
    assert res2 == Decimal("72.0000")


def test_uom_conversion_decimal_valid():
    """Skenario Positif 2: Konversi satuan dengan pecahan desimal standar."""
    # 0.5 Liter -> 500 Ml
    res = konversi_satuan(Decimal("0.5000"), Decimal("1000.0000"))
    assert res == Decimal("500.0000")

    # 1.5 Meter_Persegi -> 15000 Cm_Persegi
    res2 = konversi_satuan(Decimal("1.5000"), Decimal("10000.0000"))
    assert res2 == Decimal("15000.0000")


def test_uom_creation_valid():
    """Skenario Positif 3: Pembuatan/validasi objek data UoM baru dengan nama string yang valid."""
    raw_data = {
        "nama_satuan": "Meter Persegi",
        "kategori_satuan": "Luas",
        "simbol": "m2",
        "keterangan": "Satuan luas bahan cetak banner"
    }
    res = validasi_data_satuan_ukur(raw_data)
    assert res.is_success is True
    assert res.error_msg is None
    assert res.data["nama_satuan"] == "Meter Persegi"
    assert res.data["kategori_satuan"] == "Luas"
    assert res.data["simbol"] == "m2"
    assert res.data["keterangan"] == "Satuan luas bahan cetak banner"


def test_uom_conversion_multi_step(fresh_uom_fixtures):
    """Skenario Positif 4: Jalur konversi langsung atau ke unit yang sama."""
    records = fresh_uom_fixtures["daftar_konversi"]
    
    # Konversi ke unit yang sama (Rim -> Rim)
    res_same = cari_jalur_konversi("Rim", "Rim", records)
    assert res_same.is_success is True
    assert res_same.data == Decimal("1.0000")
    assert res_same.error_msg is None

    # Konversi langsung Rim -> Lembar
    res_direct = cari_jalur_konversi("Rim", "Lembar", records)
    assert res_direct.is_success is True
    assert res_direct.data == Decimal("500.0000")


# ==============================================================================
# B. SKENARIO NEGATIF / EDGE CASES
# ==============================================================================

def test_uom_conversion_extreme_decimal():
    """Skenario Negatif 1: Pengujian batas nilai desimal sangat kecil."""
    # Karet stempel flash diameter pemakaian: Decimal('0.0025')
    res = konversi_satuan(Decimal("10000"), Decimal("0.0025"))
    assert res == Decimal("25.0000")

    res2 = konversi_satuan(Decimal("0.0025"), Decimal("0.0025"))
    # 0.0025 * 0.0025 = 0.00000625 -> quantize(0.0001) -> 0.0000
    assert res2 == Decimal("0.0000")


def test_uom_conversion_overflow():
    """Skenario Negatif 2: Overflow batas atas / nilai masif mendekati limit keuangan."""
    masif = Decimal("99999999999.9999")
    res = konversi_satuan(masif, Decimal("1.0000"))
    assert res == masif

    # Check perkalian masif yang melebihi format quantize (apakah aman secara tipe data desimal)
    res_overflow = konversi_satuan(masif, Decimal("2.0000"))
    assert res_overflow == Decimal("199999999999.9998")


def test_uom_conversion_rounding():
    """Skenario Negatif 3: Jaminan akurasi pembulatan Round Half Up."""
    # 1.0000 * 0.00005 = 0.00005 -> ROUND_HALF_UP -> 0.0001
    res1 = konversi_satuan(Decimal("1.0000"), Decimal("0.00005"))
    assert res1 == Decimal("0.0001")

    # 1.0000 * 0.00004 = 0.00004 -> ROUND_HALF_UP -> 0.0000
    res2 = konversi_satuan(Decimal("1.0000"), Decimal("0.00004"))
    assert res2 == Decimal("0.0000")

    # hitung_faktor_konversi_balik(Decimal('3')) = 1 / 3 = 0.33333... -> 0.3333
    res_balik = hitung_faktor_konversi_balik(Decimal("3.0000"))
    assert res_balik.is_success is True
    assert res_balik.data == Decimal("0.3333")

    # hitung_faktor_konversi_balik(Decimal('1.5')) = 1 / 1.5 = 0.66666... -> 0.6667
    res_balik2 = hitung_faktor_konversi_balik(Decimal("1.5000"))
    assert res_balik2.is_success is True
    assert res_balik2.data == Decimal("0.6667")


def test_uom_conversion_division_by_zero():
    """Skenario Negatif 4: Penanganan pembagian dengan nol / proteksi faktor <= 0."""
    res = hitung_faktor_konversi_balik(Decimal("0.0000"))
    assert res.is_success is False
    assert "ERR-UOM-004" in res.error_msg

    res_neg = hitung_faktor_konversi_balik(Decimal("-1.5000"))
    assert res_neg.is_success is False
    assert "ERR-UOM-004" in res_neg.error_msg


# ==============================================================================
# C. VALIDASI INPUT (INPUT VALIDATION)
# ==============================================================================

def test_uom_invalid_string_input():
    """Validasi Input 1: Nama UoM kosong, None, atau escape karakter ilegal."""
    # None name
    res1 = validasi_data_satuan_ukur({"kategori_satuan": "Kuantitas"})
    assert res1.is_success is False
    assert "ERR-VAL-009" in res1.error_msg

    # Empty name
    res2 = validasi_data_satuan_ukur({"nama_satuan": "   ", "kategori_satuan": "Kuantitas"})
    assert res2.is_success is False
    assert "ERR-VAL-009" in res2.error_msg

    # Name too long > 30 chars
    res3 = validasi_data_satuan_ukur({"nama_satuan": "A" * 31, "kategori_satuan": "Kuantitas"})
    assert res3.is_success is False
    assert "ERR-VAL-009" in res3.error_msg

    # Control/Escape characters
    res4 = validasi_data_satuan_ukur({"nama_satuan": "Meter\nPersegi", "kategori_satuan": "Luas"})
    assert res4.is_success is False
    assert "ERR-VAL-009" in res4.error_msg

    # Invalid category
    res5 = validasi_data_satuan_ukur({"nama_satuan": "Meter", "kategori_satuan": "Suhu"})
    assert res5.is_success is False
    assert "ERR-VAL-009" in res5.error_msg


def test_uom_negative_quantity_input():
    """Validasi Input 2: Kuantitas / faktor konversi bernilai negatif atau nol."""
    # validasi_data_konversi dengan faktor <= 0
    raw_data_nol = {
        "satuan_asal_id": 1,
        "satuan_tujuan_id": 2,
        "faktor_konversi": Decimal("0.0000")
    }
    res_nol = validasi_data_konversi(raw_data_nol)
    assert res_nol.is_success is False
    assert "ERR-UOM-004" in res_nol.error_msg

    raw_data_negatif = {
        "satuan_asal_id": 1,
        "satuan_tujuan_id": 2,
        "faktor_konversi": Decimal("-5.2500")
    }
    res_neg = validasi_data_konversi(raw_data_negatif)
    assert res_neg.is_success is False
    assert "ERR-UOM-004" in res_neg.error_msg


def test_uom_validation_data_errors():
    """Validasi Input 3: Tipe data salah (float, string id invalid, unit yang sama)."""
    # 1. Float prevention
    with pytest.raises(TypeError) as exc1:
        konversi_satuan(1.5, Decimal("1.0000"))
    assert "tidak boleh menggunakan tipe data float" in str(exc1.value)

    with pytest.raises(TypeError) as exc2:
        konversi_satuan(Decimal("1.5000"), 1.0)
    assert "tidak boleh menggunakan tipe data float" in str(exc2.value)

    # 2. None or non-Decimal parameters
    with pytest.raises(TypeError) as exc3:
        konversi_satuan("1.5", Decimal("1.0000"))
    assert "harus berupa Decimal" in str(exc3.value)

    # 3. hitung_faktor_konversi_balik float prevention
    res_balik_float = hitung_faktor_konversi_balik(2.5)
    assert res_balik_float.is_success is False
    assert "ERR-VAL-050" in res_balik_float.error_msg

    res_balik_str = hitung_faktor_konversi_balik("2.5")
    assert res_balik_str.is_success is False
    assert "ERR-VAL-050" in res_balik_str.error_msg

    # 4. validasi_data_konversi float prevention
    raw_data_float = {
        "satuan_asal_id": 1,
        "satuan_tujuan_id": 2,
        "faktor_konversi": 2.5
    }
    res_float = validasi_data_konversi(raw_data_float)
    assert res_float.is_success is False
    assert "ERR-VAL-050" in res_float.error_msg

    # 5. Conversion between same unit IDs
    raw_data_same = {
        "satuan_asal_id": 1,
        "satuan_tujuan_id": 1,
        "faktor_konversi": Decimal("1.0000")
    }
    res_same = validasi_data_konversi(raw_data_same)
    assert res_same.is_success is False
    assert "ERR-UOM-003" in res_same.error_msg

    # 6. Invalid ID types
    raw_data_invalid_id = {
        "satuan_asal_id": "abc",
        "satuan_tujuan_id": 2,
        "faktor_konversi": Decimal("1.0000")
    }
    res_invalid_id = validasi_data_konversi(raw_data_invalid_id)
    assert res_invalid_id.is_success is False
    assert "ERR-VAL-009" in res_invalid_id.error_msg

    raw_data_negative_id = {
        "satuan_asal_id": 1,
        "satuan_tujuan_id": -2,
        "faktor_konversi": Decimal("1.0000")
    }
    res_negative_id = validasi_data_konversi(raw_data_negative_id)
    assert res_negative_id.is_success is False
    assert "ERR-VAL-009" in res_negative_id.error_msg


def test_cari_jalur_konversi_tidak_ditemukan(fresh_uom_fixtures):
    """Skenario Negatif 5: Pencarian jalur konversi tidak ditemukan."""
    records = fresh_uom_fixtures["daftar_konversi"]
    res = cari_jalur_konversi("Rim", "Mililiter", records)
    assert res.is_success is False
    assert "ERR-UOM-001" in res.error_msg


def test_validasi_data_satuan_ukur_missing_fields():
    """Validasi Input 4: Validasi data satuan ukur dengan missing fields."""
    # Kategori kosong
    res1 = validasi_data_satuan_ukur({"nama_satuan": "Rim"})
    assert res1.is_success is False
    assert "ERR-VAL-009" in res1.error_msg

    # Simbol terlalu panjang > 10 chars
    res2 = validasi_data_satuan_ukur({
        "nama_satuan": "Rim",
        "kategori_satuan": "Kuantitas",
        "simbol": "A" * 11
    })
    assert res2.is_success is False
    assert "ERR-VAL-009" in res2.error_msg


def test_validasi_data_konversi_invalid_faktor_format():
    """Validasi Input 5: Validasi data konversi dengan format faktor konversi tidak valid (bukan angka)."""
    raw_data = {
        "satuan_asal_id": 1,
        "satuan_tujuan_id": 2,
        "faktor_konversi": "bukan_angka"
    }
    res = validasi_data_konversi(raw_data)
    assert res.is_success is False
    assert "ERR-VAL-009" in res.error_msg


def test_validasi_data_konversi_sukses():
    """Skenario Positif: Validasi data konversi yang valid."""
    raw_data = {
        "satuan_asal_id": "1",
        "satuan_tujuan_id": "2",
        "faktor_konversi": "500.0000"
    }
    res = validasi_data_konversi(raw_data)
    assert res.is_success is True
    assert res.data["satuan_asal_id"] == 1
    assert res.data["satuan_tujuan_id"] == 2
    assert res.data["faktor_konversi"] == Decimal("500.0000")


def test_validasi_data_konversi_negative_asal_id():
    """Skenario Negatif: ID satuan asal bernilai negatif."""
    raw_data = {
        "satuan_asal_id": -1,
        "satuan_tujuan_id": 2,
        "faktor_konversi": "1.0000"
    }
    res = validasi_data_konversi(raw_data)
    assert res.is_success is False
    assert "ERR-VAL-009" in res.error_msg


def test_hitung_faktor_konversi_balik_exception():
    """Skenario Negatif: Simulasi exception umum saat menghitung faktor balik."""
    class BadDecimal(Decimal):
        def __rtruediv__(self, other):
            raise ValueError("Math error")
        def __truediv__(self, other):
            raise ValueError("Math error")

    bad_factor = BadDecimal("2.0000")
    res = hitung_faktor_konversi_balik(bad_factor)
    assert res.is_success is False
    assert "Gagal menghitung faktor balik: Math error" in res.error_msg


