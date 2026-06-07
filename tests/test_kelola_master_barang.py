"""
Nama Modul: test_kelola_master_barang.py
Deskripsi: Unit testing otomatis berbasis pytest untuk fungsi kelola master barang retail,
           bahan baku, kalkulasi dimensi, dan pencegahan pembagian nol (ZeroDivisionError)
           pada logic/bom_hpp.py.
Author: Lead SDET AI
Tanggal: 2026-06-07
"""

import pytest
from decimal import Decimal
from collections import namedtuple

from logic.bom_hpp import (
    tambah_barang,
    hitung_dimensi_bahan_baku,
    hitung_rasio_harga_kuantitas,
    Result,
    BarangRecord
)


# Mock NamedTuple untuk status sesi pengguna guna isolasi pengujian
SessionStateMock = namedtuple('SessionStateMock', ['user_id', 'username', 'role', 'cabang_id'])


@pytest.fixture
def mock_session_state() -> SessionStateMock:
    """Fixture yang mengembalikan NamedTuple state session pengguna mock."""
    return SessionStateMock(
        user_id=1,
        username='pemilik_agus',
        role='pemilik',
        cabang_id=1
    )


@pytest.fixture
def fixture_data() -> dict:
    """Fixture yang mengembalikan dictionary data valid barang retail baru."""
    return {
        'nama_barang': 'Buku Tulis Sinar Dunia 38 Lembar',
        'tipe_barang': 'Retail_ATK',
        'satuan_uom': 'Pcs',
        'stok_saat_ini': '100.0000',
        'harga_beli': '2500.0000',
        'harga_retail': '3500.0000',
        'harga_grosir': '3200.0000',
        'min_grosir': '10.0000',
        'harga_mitra': '3000.0000',
        'cabang_id': '1'
    }


# =====================================================================
# SKENARIO POSITIF
# =====================================================================

def test_tambah_barang_retail_sukses(fixture_data: dict) -> None:
    """Skenario Positif: Berhasil memproses pembuatan barang retail baru dengan data yang valid."""
    result = tambah_barang(fixture_data)
    assert result.is_success is True
    assert result.error_msg is None
    assert isinstance(result.data, BarangRecord)
    assert result.data.nama_barang == 'Buku Tulis Sinar Dunia 38 Lembar'
    assert result.data.stok_saat_ini == Decimal('100.0000')
    assert result.data.harga_beli == Decimal('2500.0000')
    assert result.data.harga_retail == Decimal('3500.0000')


def test_kalkulasi_dimensi_bahan_baku_presisi() -> None:
    """Skenario Positif: Berhasil menghitung dimensi bahan baku (panjang x lebar) dengan presisi desimal."""
    # Skenario 15.4 desimal presisi: 1.2345 * 2.3456 = 2.8956432 -> dibulatkan ROUND_HALF_UP -> 2.8956
    panjang = Decimal('1.2345')
    lebar = Decimal('2.3456')
    hasil = hitung_dimensi_bahan_baku(panjang, lebar)
    assert hasil == Decimal('2.8956')

    # Skenario 2: Pembulatan ROUND_HALF_UP (2.50005 -> 2.5001)
    p2 = Decimal('1.0000')
    l2 = Decimal('2.50005')
    hasil2 = hitung_dimensi_bahan_baku(p2, l2)
    assert hasil2 == Decimal('2.5001')


# =====================================================================
# SKENARIO NEGATIF / EDGE CASES & BOUNDARY
# =====================================================================

def test_tambah_barang_harga_negatif_gagal() -> None:
    """Skenario Negatif: Sistem menolak penambahan barang apabila harga beli bernilai negatif."""
    invalid_data = {
        'nama_barang': 'Kertas Buffalo Hijau',
        'tipe_barang': 'Retail_ATK',
        'satuan_uom': 'Lembar',
        'stok_saat_ini': '50.0000',
        'harga_beli': '-1000.0000',  # Negatif
        'harga_retail': '1500.0000',
        'harga_grosir': '1300.0000',
        'min_grosir': '5.0000',
        'harga_mitra': '1200.0000',
        'cabang_id': '1'
    }
    result = tambah_barang(invalid_data)
    assert result.is_success is False
    assert result.data is None
    assert "ERR-VAL-009" in result.error_msg
    assert "tidak boleh negatif" in result.error_msg


def test_tambah_barang_kuantitas_negatif_gagal() -> None:
    """Skenario Negatif: Sistem menolak penambahan barang apabila kuantitas/stok bernilai negatif."""
    invalid_data = {
        'nama_barang': 'Kertas Buffalo Biru',
        'tipe_barang': 'Retail_ATK',
        'satuan_uom': 'Lembar',
        'stok_saat_ini': '-5.0000',  # Negatif
        'harga_beli': '1000.0000',
        'harga_retail': '1500.0000',
        'harga_grosir': '1300.0000',
        'min_grosir': '5.0000',
        'harga_mitra': '1200.0000',
        'cabang_id': '1'
    }
    result = tambah_barang(invalid_data)
    assert result.is_success is False
    assert "ERR-VAL-009" in result.error_msg
    assert "tidak boleh negatif" in result.error_msg


def test_tambah_barang_nama_kosong_gagal() -> None:
    """Skenario Negatif: Sistem menolak penambahan barang apabila nama barang kosong."""
    # Nama kosong (hanya whitespace)
    invalid_data = {
        'nama_barang': '   ',
        'tipe_barang': 'Retail_ATK',
        'satuan_uom': 'Pcs',
        'stok_saat_ini': '10.0000',
        'harga_beli': '1000.0000',
        'harga_retail': '1500.0000',
        'harga_grosir': '1300.0000',
        'min_grosir': '5.0000',
        'harga_mitra': '1200.0000',
        'cabang_id': '1'
    }
    result = tambah_barang(invalid_data)
    assert result.is_success is False
    assert "ERR-VAL-009" in result.error_msg
    assert "tidak boleh kosong" in result.error_msg

    # Key nama_barang None / tidak disuplai
    invalid_data_missing = invalid_data.copy()
    invalid_data_missing.pop('nama_barang')
    result_missing = tambah_barang(invalid_data_missing)
    assert result_missing.is_success is False
    assert "ERR-VAL-009" in result_missing.error_msg or "wajib diisi" in result_missing.error_msg


def test_validasi_pembagian_nol_bahan_baku() -> None:
    """Skenario Edge Case: Memastikan logika tidak melempar eksepsi ZeroDivisionError ketika qty bernilai 0.0000."""
    harga = Decimal('150000.0000')
    kuantitas = Decimal('0.0000')
    
    # Harus mengembalikan Result(is_success=False) dan pesan error penanganan yang aman
    result = hitung_rasio_harga_kuantitas(harga, kuantitas)
    assert result.is_success is False
    assert result.data is None
    assert "ERR-VAL-009" in result.error_msg
    assert "ZeroDivisionError prevented" in result.error_msg


# =====================================================================
# VALIDASI INPUT & KEPATUHAN TYPE HINTS / SECURE CODING
# =====================================================================

def test_tambah_barang_nama_escape_illegal_gagal() -> None:
    """Skenario Keamanan: Validasi input menolak karakter escape ilegal pada nama barang (ASCII < 0x20)."""
    invalid_data = {
        'nama_barang': 'Kertas\x1b[31m HVS A4',  # Mengandung escape ANSI
        'tipe_barang': 'Retail_ATK',
        'satuan_uom': 'Rim',
        'stok_saat_ini': '10.0000',
        'harga_beli': '45000.0000',
        'harga_retail': '55000.0000',
        'harga_grosir': '52000.0000',
        'min_grosir': '5.0000',
        'harga_mitra': '50000.0000',
        'cabang_id': '1'
    }
    result = tambah_barang(invalid_data)
    assert result.is_success is False
    assert "ERR-VAL-009" in result.error_msg
    assert "karakter escape ilegal" in result.error_msg


def test_tambah_barang_nama_terlalu_panjang_gagal() -> None:
    """Skenario Boundary: Validasi batas karakter (max_length) untuk field nama barang (> 100 karakter)."""
    nama_panjang = 'A' * 101
    invalid_data = {
        'nama_barang': nama_panjang,
        'tipe_barang': 'Retail_ATK',
        'satuan_uom': 'Rim',
        'stok_saat_ini': '10.0000',
        'harga_beli': '45000.0000',
        'harga_retail': '55000.0000',
        'harga_grosir': '52000.0000',
        'min_grosir': '5.0000',
        'harga_mitra': '50000.0000',
        'cabang_id': '1'
    }
    result = tambah_barang(invalid_data)
    assert result.is_success is False
    assert "ERR-VAL-009" in result.error_msg
    assert "maksimal 100 karakter" in result.error_msg


def test_tambah_barang_deskripsi_terlalu_panjang_gagal() -> None:
    """Skenario Boundary: Validasi batas karakter (max_length) untuk field deskripsi (> 500 karakter)."""
    deskripsi_panjang = 'D' * 501
    invalid_data = {
        'nama_barang': 'Kertas HVS',
        'tipe_barang': 'Retail_ATK',
        'satuan_uom': 'Rim',
        'stok_saat_ini': '10.0000',
        'harga_beli': '45000.0000',
        'harga_retail': '55000.0000',
        'harga_grosir': '52000.0000',
        'min_grosir': '5.0000',
        'harga_mitra': '50000.0000',
        'cabang_id': '1',
        'deskripsi': deskripsi_panjang
    }
    result = tambah_barang(invalid_data)
    assert result.is_success is False
    assert "ERR-VAL-009" in result.error_msg
    assert "Deskripsi barang melebihi batas" in result.error_msg


def test_tambah_barang_input_float_ditolak() -> None:
    """Skenario Keamanan Finansial: Memastikan argumen finansial tidak diinput menggunakan float."""
    # Uji harga_beli sebagai float
    invalid_data = {
        'nama_barang': 'Tinta Stempel',
        'tipe_barang': 'Retail_ATK',
        'satuan_uom': 'Ml',
        'stok_saat_ini': '50.0000',
        'harga_beli': 12000.5,  # float
        'harga_retail': '15000.0000',
        'harga_grosir': '14000.0000',
        'min_grosir': '5.0000',
        'harga_mitra': '13500.0000',
        'cabang_id': '1'
    }
    result = tambah_barang(invalid_data)
    assert result.is_success is False
    assert "ERR-VAL-050" in result.error_msg
    assert "tidak boleh menggunakan tipe data float" in result.error_msg

    # Uji stok_saat_ini sebagai float
    invalid_data2 = invalid_data.copy()
    invalid_data2['harga_beli'] = '12000.5000'
    invalid_data2['stok_saat_ini'] = 50.5  # float
    result2 = tambah_barang(invalid_data2)
    assert result2.is_success is False
    assert "ERR-VAL-050" in result2.error_msg


def test_hitung_dimensi_input_float_ditolak() -> None:
    """Skenario Keamanan Finansial: Memastikan hitung_dimensi_bahan_baku menolak float dan memicu TypeError."""
    with pytest.raises(TypeError) as excinfo:
        hitung_dimensi_bahan_baku(1.5, Decimal('2.0000'))  # type: ignore
    assert "tidak boleh diinput menggunakan tipe data float" in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo2:
        hitung_dimensi_bahan_baku(Decimal('1.5000'), 2.0)  # type: ignore
    assert "tidak boleh diinput menggunakan tipe data float" in str(excinfo2.value)


def test_hitung_dimensi_non_decimal_type_error() -> None:
    """Skenario Edge Case: Memastikan input string atau tipe non-desimal memicu TypeError."""
    with pytest.raises(TypeError):
        hitung_dimensi_bahan_baku("1.5000", Decimal('2.0000'))  # type: ignore


def test_hitung_dimensi_negatif_value_error() -> None:
    """Skenario Boundary: Memastikan input dimensi bernilai negatif memicu ValueError."""
    with pytest.raises(ValueError) as excinfo:
        hitung_dimensi_bahan_baku(Decimal('-1.5000'), Decimal('2.0000'))
    assert "tidak boleh bernilai negatif" in str(excinfo.value)


def test_hitung_rasio_input_float_ditolak() -> None:
    """Skenario Keamanan Finansial: Memastikan hitung_rasio_harga_kuantitas menolak float."""
    res = hitung_rasio_harga_kuantitas(100.5, Decimal('10.0000'))  # type: ignore
    assert res.is_success is False
    assert "ERR-VAL-050" in res.error_msg
    assert "tidak boleh menggunakan tipe data float" in res.error_msg

    res2 = hitung_rasio_harga_kuantitas(Decimal('100.5000'), 10.0)  # type: ignore
    assert res2.is_success is False
    assert "ERR-VAL-050" in res2.error_msg


def test_hitung_rasio_non_decimal_ditolak() -> None:
    """Skenario Edge Case: Memastikan tipe non-Decimal ditolak."""
    res = hitung_rasio_harga_kuantitas("100.5000", Decimal('10.0000'))  # type: ignore
    assert res.is_success is False
    assert "ERR-VAL-050" in res.error_msg
    assert "harus berupa tipe data Decimal" in res.error_msg


def test_hitung_rasio_negatif_gagal() -> None:
    """Skenario Boundary: Memastikan input bernilai negatif ditolak."""
    res = hitung_rasio_harga_kuantitas(Decimal('-100.0000'), Decimal('10.0000'))
    assert res.is_success is False
    assert "ERR-VAL-009" in res.error_msg
    assert "tidak boleh bernilai negatif" in res.error_msg

    res2 = hitung_rasio_harga_kuantitas(Decimal('100.0000'), Decimal('-10.0000'))
    assert res2.is_success is False
    assert "ERR-VAL-009" in res2.error_msg


def test_tambah_barang_non_dict_gagal() -> None:
    """Skenario Edge Case: Memastikan input data non-dictionary ditolak secara aman."""
    res = tambah_barang("bukan_dict")  # type: ignore
    assert res.is_success is False
    assert "ERR-VAL-009" in res.error_msg


def test_hitung_rasio_harga_kuantitas_sukses() -> None:
    """Skenario Positif: Perhitungan rasio harga dibagi kuantitas yang valid."""
    harga = Decimal('15000.0000')
    kuantitas = Decimal('5.0000')
    res = hitung_rasio_harga_kuantitas(harga, kuantitas)
    assert res.is_success is True
    assert res.data == Decimal('3000.0000')
    assert res.error_msg is None


def test_tambah_barang_harga_beli_non_numerik_gagal(fixture_data: dict) -> None:
    """Skenario Negatif: Input harga beli berupa string non-numerik."""
    invalid_data = fixture_data.copy()
    invalid_data['harga_beli'] = 'seribu'
    res = tambah_barang(invalid_data)
    assert res.is_success is False
    assert "ERR-VAL-009" in res.error_msg


def test_tambah_barang_retail_harga_retail_non_numerik_gagal(fixture_data: dict) -> None:
    """Skenario Negatif: Input harga retail berupa string non-numerik untuk barang retail."""
    invalid_data = fixture_data.copy()
    invalid_data['harga_retail'] = 'tiga ribu'
    res = tambah_barang(invalid_data)
    assert res.is_success is False
    assert "ERR-VAL-009" in res.error_msg

