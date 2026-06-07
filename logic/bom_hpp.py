"""
Nama Modul: bom_hpp.py
Deskripsi: Logika bisnis perhitungan Bill of Materials (BOM) dan Harga Pokok Penjualan (HPP).
           (Ref: Module Structure Bab 5.2)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

from collections import namedtuple
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
from typing import Any

# NamedTuple Definition
BOMKomponen = namedtuple('BOMKomponen', ['bahan_baku_id', 'nama_barang', 'kuantitas', 'harga_beli'])
Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
BarangRecord = namedtuple('BarangRecord', [
    'nama_barang', 'tipe_barang', 'satuan_uom', 'stok_saat_ini',
    'harga_beli', 'harga_retail', 'harga_grosir', 'min_grosir',
    'harga_mitra', 'cabang_id'
])
ValidationResult = namedtuple('ValidationResult', [
    'is_valid', 'cleaned_data', 'error_msg'
])


def hitung_biaya_komponen(kuantitas: Decimal, harga_beli_satuan: Decimal) -> Decimal:
    """Mengalkulasikan nominal biaya komponen bahan desimal.

    Args:
        kuantitas (Decimal): Jumlah bahan baku yang digunakan.
        harga_beli_satuan (Decimal): Harga beli per satuan bahan baku.

    Returns:
        Decimal: Total biaya komponen dengan presisi desimal.
    """
    return (kuantitas * harga_beli_satuan).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)


def hitung_hpp_produk(komponen_list: list[BOMKomponen]) -> Decimal:
    """Menjumlahkan secara deterministic biaya seluruh komponen penyusun.

    Args:
        komponen_list (list[BOMKomponen]): Daftar NamedTuple komponen bahan baku.

    Returns:
        Decimal: Hasil kalkulasi HPP produk percetakan.
    """
    total = Decimal('0.0000')
    for comp in komponen_list:
        total += hitung_biaya_komponen(comp.kuantitas, comp.harga_beli)
    return total


def proses_pemotongan_stok(komponen_list: list[BOMKomponen], cabang_id: int, db_connection: Any) -> Result:
    """Eksekusi ACID transaction block MySQL untuk memotong stok desimal bahan baku.

    Args:
        komponen_list (list[BOMKomponen]): Daftar NamedTuple komponen yang dipotong.
        cabang_id (int): ID cabang lokasi perubahan stok.
        db_connection: Koneksi basis data aktif.

    Returns:
        Result: Status keberhasilan operasi pemotongan.
    """
    # TODO: Implementasi pemotongan stok bahan baku desimal
    return Result(False, None, 'ERR-LOGIC-001: Fitur pemotongan stok belum diimplementasikan.')


def validasi_data_barang(data: dict) -> ValidationResult:
    """Fungsi murni untuk memvalidasi dan membersihkan data input barang baru/edit.

    Args:
        data (dict): Dictionary mentah dari input CLI yang belum divalidasi.

    Returns:
        ValidationResult: NamedTuple berisi status validasi, data bersih, dan pesan error.
    """
    try:
        # 1. nama_barang: wajib diisi, tidak boleh kosong, maks 100 karakter
        nama = data.get('nama_barang')
        if nama is None:
            return ValidationResult(False, None, "Nama barang wajib diisi!")
        nama = str(nama).strip()
        if not nama:
            return ValidationResult(False, None, "Nama barang tidak boleh kosong!")
        if len(nama) > 100:
            return ValidationResult(False, None, "Nama barang maksimal 100 karakter!")

        # 2. tipe_barang: wajib bernilai 'Retail_ATK' atau 'Bahan_Baku'
        tipe = data.get('tipe_barang')
        if tipe not in ['Retail_ATK', 'Bahan_Baku']:
            return ValidationResult(False, None, "Tipe barang harus 'Retail_ATK' atau 'Bahan_Baku'!")

        # 3. satuan_uom: wajib bernilai salah satu dari ['Rim', 'Lembar', 'Pcs', 'Ml', 'Meter_Persegi']
        uom = data.get('satuan_uom')
        if uom not in ['Rim', 'Lembar', 'Pcs', 'Ml', 'Meter_Persegi']:
            return ValidationResult(False, None, "Satuan UoM tidak valid!")

        # Helper to parse and quantize decimal
        def parse_decimal(val_raw, field_name, check_positive=True, allow_zero=True):
            if val_raw is None or str(val_raw).strip() == '':
                raise ValueError(f"{field_name} wajib diisi!")
            try:
                dec = Decimal(str(val_raw).strip())
            except (ValueError, InvalidOperation):
                raise TypeError() # Raise TypeError to distinguish from normal ValueError
            
            dec_quantized = dec.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
            if check_positive:
                if allow_zero and dec_quantized < 0:
                    raise ValueError(f"{field_name} tidak boleh negatif!")
                elif not allow_zero and dec_quantized <= 0:
                    raise ValueError(f"{field_name} harus lebih besar dari nol!")
            return dec_quantized

        # 4. stok_saat_ini: wajib numerik desimal >= 0
        try:
            stok = parse_decimal(data.get('stok_saat_ini'), "Stok saat ini", check_positive=True, allow_zero=True)
        except TypeError:
            return ValidationResult(False, None, "⛔ ERR-VAL-009: Input kuantitas harus berupa angka desimal valid (contoh: 12.50)!")
        except ValueError as e:
            return ValidationResult(False, None, str(e))

        # 5. harga_beli: wajib numerik desimal >= 0
        try:
            harga_beli = parse_decimal(data.get('harga_beli'), "Harga beli", check_positive=True, allow_zero=True)
        except TypeError:
            return ValidationResult(False, None, "⛔ ERR-VAL-009: Input kuantitas harus berupa angka desimal valid (contoh: 12.50)!")
        except ValueError as e:
            return ValidationResult(False, None, str(e))

        # 6-9. Harga retail, grosir, mitra, min_grosir
        if tipe == 'Bahan_Baku':
            harga_retail = Decimal('0.0000')
            harga_grosir = Decimal('0.0000')
            harga_mitra = Decimal('0.0000')
            min_grosir = Decimal('1.0000')
        else:
            try:
                harga_retail = parse_decimal(data.get('harga_retail'), "Harga retail", check_positive=True, allow_zero=True)
                harga_grosir = parse_decimal(data.get('harga_grosir'), "Harga grosir", check_positive=True, allow_zero=True)
                harga_mitra = parse_decimal(data.get('harga_mitra'), "Harga mitra", check_positive=True, allow_zero=True)
                min_grosir = parse_decimal(data.get('min_grosir', '1.0000'), "Min grosir", check_positive=True, allow_zero=False)
            except TypeError:
                return ValidationResult(False, None, "⛔ ERR-VAL-009: Input kuantitas harus berupa angka desimal valid (contoh: 12.50)!")
            except ValueError as e:
                return ValidationResult(False, None, str(e))

        # 10. cabang_id: wajib integer
        try:
            cabang_id = int(str(data.get('cabang_id', 1)).strip())
            if cabang_id <= 0:
                raise ValueError()
        except ValueError:
            return ValidationResult(False, None, "Cabang ID harus berupa integer positif!")

        cleaned_data = {
            'nama_barang': nama,
            'tipe_barang': tipe,
            'satuan_uom': uom,
            'stok_saat_ini': stok,
            'harga_beli': harga_beli,
            'harga_retail': harga_retail,
            'harga_grosir': harga_grosir,
            'min_grosir': min_grosir,
            'harga_mitra': harga_mitra,
            'cabang_id': cabang_id
        }
        return ValidationResult(True, cleaned_data, None)

    except Exception as e:
        return ValidationResult(False, None, f"Terjadi kesalahan validasi: {str(e)}")


def _convert_decimals(obj: Any) -> Any:
    """Helper internal fungsional untuk mengonversi Decimal ke float untuk serialisasi JSON."""
    if isinstance(obj, dict):
        return {k: _convert_decimals(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_convert_decimals(x) for x in obj]
    elif isinstance(obj, Decimal):
        return float(obj)
    return obj


def buat_audit_payload_barang(
    action_type: str,
    old_data: dict | None,
    new_data: dict | None
) -> tuple[str, str]:
    """Fungsi murni untuk menyusun payload JSON audit trail perubahan data barang.

    Args:
        action_type (str): Tipe aksi ('INSERT', 'UPDATE', 'DELETE').
        old_data (dict | None): Data sebelum perubahan (None untuk INSERT).
        new_data (dict | None): Data setelah perubahan (None untuk DELETE).

    Returns:
        tuple[str, str]: (old_value_json, new_value_json) siap INSERT ke audit_logs.
    """
    import json
    
    old_converted = _convert_decimals(old_data) if old_data is not None else None
    new_converted = _convert_decimals(new_data) if new_data is not None else None
    
    old_json = json.dumps(old_converted) if old_converted is not None else 'null'
    new_json = json.dumps(new_converted) if new_converted is not None else 'null'
    
    return old_json, new_json


def hitung_margin_barang(harga_jual: Decimal, harga_beli: Decimal) -> Decimal:
    """Fungsi murni untuk menghitung persentase margin keuntungan kotor.

    Formula: Margin (%) = ((harga_jual - harga_beli) / harga_jual) * 100
    Mitigasi: Jika harga_jual == 0, return Decimal('0.00').

    Args:
        harga_jual (Decimal): Harga jual satuan (retail/grosir/mitra).
        harga_beli (Decimal): Harga pengadaan/beli dari supplier.

    Returns:
        Decimal: Persentase margin keuntungan, dibulatkan 2 desimal.
    """
    if harga_jual == Decimal('0.0000'):
        return Decimal('0.00')
    margin = ((harga_jual - harga_beli) / harga_jual) * 100
    return margin.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
