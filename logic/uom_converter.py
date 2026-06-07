"""
Nama Modul: uom_converter.py
Deskripsi: Berisi pure functions untuk konversi satuan ukur (Unit of Measure)
           dan validasi master satuan barang (Modul M.2).
Author: Senior Inventory Systems Engineer & Unit Conversion Specialist
Tanggal: 2026-06-08
"""

from collections import namedtuple
from decimal import Decimal, ROUND_HALF_UP

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
SatuanUkurRecord = namedtuple('SatuanUkurRecord', [
    'id', 'nama_satuan', 'kategori_satuan', 'simbol', 'keterangan', 'is_aktif'
])
KonversiRecord = namedtuple('KonversiRecord', [
    'id', 'satuan_asal', 'satuan_tujuan', 'faktor_konversi'
])
KonversiResult = namedtuple('KonversiResult', [
    'nilai_asal', 'satuan_asal', 'nilai_tujuan', 'satuan_tujuan', 'faktor_konversi'
])

# Domain nilai valid untuk kategori satuan
KATEGORI_SATUAN_VALID = [
    'Kuantitas',      # Pcs, Lembar, Rim, Buah, Unit
    'Panjang',        # Meter, Centimeter
    'Luas',           # Meter_Persegi, Centimeter_Persegi  
    'Volume',         # Liter, Mililiter, Ml
    'Berat',          # Kilogram, Gram, Kg
]


def konversi_satuan(
    nilai: Decimal, 
    faktor_konversi: Decimal
) -> Decimal:
    """Mengonversi nilai dari satuan asal ke satuan tujuan menggunakan faktor konversi.
    
    Formula: nilai_tujuan = nilai_asal * faktor_konversi
    
    Args:
        nilai (Decimal): Nilai kuantitas dalam satuan asal.
        faktor_konversi (Decimal): Faktor pengali konversi dari database.
    
    Returns:
        Decimal: Nilai kuantitas dalam satuan tujuan, presisi 4 desimal.
    """
    # Issue #0132
    if isinstance(nilai, float) or isinstance(faktor_konversi, float):
        raise TypeError("Argumen konversi tidak boleh menggunakan tipe data float!")
    if not isinstance(nilai, Decimal) or not isinstance(faktor_konversi, Decimal):
        raise TypeError("Argumen konversi harus berupa Decimal!")
    res = nilai * faktor_konversi
    return res.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)


def hitung_faktor_konversi_balik(faktor: Decimal) -> Result:
    """Menghitung faktor konversi kebalikan (inverse) secara aman.
    
    Formula: faktor_balik = 1 / faktor
    Mitigasi: Jika faktor <= 0, return error (prevent ZeroDivisionError).
    
    Args:
        faktor (Decimal): Faktor konversi asal.
    
    Returns:
        Result: Berisi faktor konversi balik atau pesan error.
    """
    # Issue #0132
    if isinstance(faktor, float):
        return Result(False, None, "⛔ ERR-VAL-050: Faktor tidak boleh menggunakan tipe data float!")
    if not isinstance(faktor, Decimal):
        return Result(False, None, "⛔ ERR-VAL-050: Faktor harus berupa Decimal!")
    if faktor <= Decimal('0.0000'):
        return Result(False, None, "ERR-UOM-004: Faktor konversi harus lebih besar dari nol")
    try:
        faktor_balik = (Decimal('1') / faktor).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
        return Result(True, faktor_balik, None)
    except Exception as e:
        return Result(False, None, f"Gagal menghitung faktor balik: {str(e)}")


def validasi_data_satuan_ukur(data: dict) -> Result:
    """Fungsi murni untuk memvalidasi input data satuan ukur baru.
    
    Validasi:
    - nama_satuan: wajib, tidak kosong, max 30 karakter, tanpa karakter escape ilegal
    - kategori_satuan: wajib, harus salah satu dari KATEGORI_SATUAN_VALID
    - simbol: opsional, max 10 karakter
    
    Args:
        data (dict): Dictionary input mentah dari form CLI.
    
    Returns:
        Result: Status validasi beserta data bersih.
    """
    # Issue #0132
    nama = data.get('nama_satuan')
    if nama is None:
        return Result(False, None, "⛔ ERR-VAL-009: Nama satuan wajib diisi!")
    nama = str(nama).strip()
    if not nama:
        return Result(False, None, "⛔ ERR-VAL-009: Nama satuan tidak boleh kosong!")
    if len(nama) > 30:
        return Result(False, None, "⛔ ERR-VAL-009: Nama satuan maksimal 30 karakter!")
    if any(ord(char) < 0x20 for char in nama):
        return Result(False, None, "⛔ ERR-VAL-009: Nama satuan tidak boleh mengandung karakter escape ilegal!")

    kategori = data.get('kategori_satuan')
    if kategori is None:
        return Result(False, None, "⛔ ERR-VAL-009: Kategori satuan wajib diisi!")
    kategori = str(kategori).strip()
    if kategori not in KATEGORI_SATUAN_VALID:
        return Result(False, None, "⛔ ERR-VAL-009: Kategori satuan tidak valid!")

    simbol = data.get('simbol', '')
    if simbol is not None:
        simbol = str(simbol).strip()
        if len(simbol) > 10:
            return Result(False, None, "⛔ ERR-VAL-009: Simbol maksimal 10 karakter!")

    keterangan = data.get('keterangan', '')
    if keterangan is not None:
        keterangan = str(keterangan).strip()

    cleaned_data = {
        'nama_satuan': nama,
        'kategori_satuan': kategori,
        'simbol': simbol,
        'keterangan': keterangan,
    }
    return Result(True, cleaned_data, None)


def validasi_data_konversi(data: dict) -> Result:
    """Fungsi murni untuk memvalidasi input data konversi satuan.
    
    Validasi:
    - satuan_asal_id: wajib, integer positif
    - satuan_tujuan_id: wajib, integer positif, tidak boleh sama dengan satuan_asal_id
    - faktor_konversi: wajib, Decimal positif > 0
    
    Args:
        data (dict): Dictionary input mentah dari form CLI.
    
    Returns:
        Result: Status validasi beserta data bersih.
    """
    # Issue #0132
    try:
        satuan_asal_id = int(str(data.get('satuan_asal_id', '')).strip())
        if satuan_asal_id <= 0:
            raise ValueError()
    except (ValueError, TypeError):
        return Result(False, None, "⛔ ERR-VAL-009: Satuan asal ID harus berupa integer positif!")

    try:
        satuan_tujuan_id = int(str(data.get('satuan_tujuan_id', '')).strip())
        if satuan_tujuan_id <= 0:
            raise ValueError()
    except (ValueError, TypeError):
        return Result(False, None, "⛔ ERR-VAL-009: Satuan tujuan ID harus berupa integer positif!")

    if satuan_asal_id == satuan_tujuan_id:
        return Result(False, None, "ERR-UOM-003: Konversi antar satuan yang sama tidak diizinkan")

    raw_faktor = data.get('faktor_konversi')
    if isinstance(raw_faktor, float):
        return Result(False, None, "⛔ ERR-VAL-050: Faktor konversi tidak boleh menggunakan tipe data float!")
    
    try:
        faktor_konversi = Decimal(str(raw_faktor).strip())
    except Exception:
        return Result(False, None, "⛔ ERR-VAL-009: Faktor konversi harus berupa angka desimal valid!")

    if faktor_konversi <= Decimal('0.0000'):
        return Result(False, None, "ERR-UOM-004: Faktor konversi harus lebih besar dari nol")

    cleaned_data = {
        'satuan_asal_id': satuan_asal_id,
        'satuan_tujuan_id': satuan_tujuan_id,
        'faktor_konversi': faktor_konversi.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    }
    return Result(True, cleaned_data, None)


def cari_jalur_konversi(
    satuan_asal: str, 
    satuan_tujuan: str, 
    daftar_konversi: list[KonversiRecord]
) -> Result:
    """Mencari faktor konversi langsung antara dua satuan dari daftar konversi.
    
    Args:
        satuan_asal (str): Nama satuan asal.
        satuan_tujuan (str): Nama satuan tujuan.
        daftar_konversi (list[KonversiRecord]): Seluruh aturan konversi dari DB.
    
    Returns:
        Result: Berisi faktor konversi atau error jika tidak ditemukan.
    """
    # Issue #0132
    if satuan_asal == satuan_tujuan:
        return Result(True, Decimal('1.0000'), None)
    for rec in daftar_konversi:
        if rec.satuan_asal == satuan_asal and rec.satuan_tujuan == satuan_tujuan:
            return Result(True, rec.faktor_konversi, None)
    return Result(False, None, "ERR-UOM-001: Jalur konversi tidak ditemukan.")
