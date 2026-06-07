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
    if isinstance(kuantitas, float) or isinstance(harga_beli_satuan, float):
        raise TypeError("Kuantitas dan harga beli tidak boleh menggunakan tipe data float!")
    if kuantitas < 0 or harga_beli_satuan < 0:
        raise ValueError("Kuantitas dan harga beli tidak boleh negatif!")
    return (kuantitas * harga_beli_satuan).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)


def hitung_hpp_produk(komponen_list: list[BOMKomponen]) -> Decimal:
    """Menjumlahkan secara deterministic biaya seluruh komponen penyusun.

    Args:
        komponen_list (list[BOMKomponen]): Daftar NamedTuple komponen bahan baku.

    Returns:
        Decimal: Hasil kalkulasi HPP produk percetakan.
    """
    if not komponen_list:
        raise ValueError("Daftar komponen BOM tidak boleh kosong!")
    total = Decimal('0.0000')
    for comp in komponen_list:
        if isinstance(comp.kuantitas, float) or isinstance(comp.harga_beli, float):
            raise TypeError("Kuantitas dan harga beli tidak boleh menggunakan tipe data float!")
        if comp.kuantitas < 0 or comp.harga_beli < 0:
            raise ValueError("Kuantitas dan harga beli tidak boleh negatif!")
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
    cursor = None
    stok_minus_detected = False
    try:
        cursor = db_connection.cursor()
        db_connection.start_transaction()
        
        for comp in komponen_list:
            # 1. Tarik stok saat ini dengan query terisolasi (Lock row via FOR UPDATE)
            cursor.execute(
                "SELECT stok_saat_ini FROM barang WHERE id = %s AND cabang_id = %s FOR UPDATE",
                (comp.bahan_baku_id, cabang_id)
            )
            row = cursor.fetchone()
            if not row:
                raise ValueError(f"Bahan baku ID {comp.bahan_baku_id} tidak ditemukan.")
                
            stok_sekarang = Decimal(str(row[0]))
            
            # Cek deteksi stok minus
            if stok_sekarang < comp.kuantitas:
                stok_minus_detected = True
                
            # 2. Update pemotongan stok di MySQL (mendukung angka negatif)
            cursor.execute(
                "UPDATE barang SET stok_saat_ini = stok_saat_ini - %s WHERE id = %s AND cabang_id = %s",
                (comp.kuantitas, comp.bahan_baku_id, cabang_id)
            )
            
            # 3. Log Audit Trail
            new_stok = stok_sekarang - comp.kuantitas
            old_val = f'{{"stok_saat_ini": {float(stok_sekarang)}}}'
            new_val = f'{{"stok_saat_ini": {float(new_stok)}}}'
            cursor.execute(
                "INSERT INTO audit_logs (pengguna_id, action_type, target_table, old_value, new_value, cabang_id) "
                "VALUES (1, 'UPDATE', 'barang', %s, %s, %s)",
                (old_val, new_val, cabang_id)
            )
            
        db_connection.commit()
        return Result(True, stok_minus_detected, None)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        return Result(False, None, f"ERR-DB-007: Gagal memotong stok bahan baku. Detail: {str(e)}")
    finally:
        if cursor:
            cursor.close()


def validasi_data_barang(data: dict, satuan_valid_list: list[str] | None = None) -> ValidationResult:
    """Fungsi murni untuk memvalidasi dan membersihkan data input barang baru/edit.

    Args:
        data (dict): Dictionary mentah dari input CLI yang belum divalidasi.
        satuan_valid_list (list[str] | None): Daftar satuan valid dari database (opsional).

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

        # 3. satuan_uom: wajib bernilai salah satu dari database/hardcoded list
        uom = data.get('satuan_uom')
        if satuan_valid_list is not None:
            if uom not in satuan_valid_list:
                return ValidationResult(False, None, "Satuan UoM tidak valid! Pilih dari daftar yang tersedia.")
        else:
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


def tambah_barang(data: dict) -> Result:
    """Logika bisnis murni untuk melakukan penambahan data master barang baru secara deterministik.

    Args:
        data (dict): Dictionary input mentah dari form pendaftaran barang.

    Returns:
        Result: Status keberhasilan operasi penambahan barang beserta record barang bersih.
    """
    if not isinstance(data, dict):
        return Result(False, None, "⛔ ERR-VAL-009: Input data harus berupa dictionary!")

    # 1. Pengecekan tipe data yang memastikan argumen finansial tidak diinput menggunakan float
    numeric_fields = ['stok_saat_ini', 'harga_beli', 'harga_retail', 'harga_grosir', 'min_grosir', 'harga_mitra']
    for field in numeric_fields:
        if field in data:
            val = data[field]
            if isinstance(val, float):
                return Result(
                    False,
                    None,
                    f"⛔ ERR-VAL-050: Argumen finansial/kuantitas '{field}' tidak boleh menggunakan tipe data float!"
                )

    # 2. Validasi input menolak karakter escape ilegal pada nama barang (ASCII < 0x20)
    nama = data.get('nama_barang')
    if nama is not None:
        nama_str = str(nama)
        if any(ord(char) < 0x20 for char in nama_str):
            return Result(
                False,
                None,
                "⛔ ERR-VAL-009: Nama barang tidak boleh mengandung karakter escape ilegal!"
            )
        # 3. Validasi batas karakter (max_length) untuk field nama
        if len(nama_str.strip()) == 0:
            return Result(
                False,
                None,
                "⛔ ERR-VAL-009: Nama barang tidak boleh kosong!"
            )
        if len(nama_str) > 100:
            return Result(
                False,
                None,
                "⛔ ERR-VAL-009: Nama barang maksimal 100 karakter!"
            )

    # Validasi deskripsi (jika disuplai)
    deskripsi = data.get('deskripsi')
    if deskripsi is not None:
        deskripsi_str = str(deskripsi)
        if len(deskripsi_str) > 500:
            return Result(
                False,
                None,
                "⛔ ERR-VAL-009: Deskripsi barang melebihi batas maksimum 500 karakter!"
            )

    # Panggil validator internal untuk verifikasi data lengkap
    val_res = validasi_data_barang(data)
    if not val_res.is_valid:
        err_msg = val_res.error_msg
        if "ERR-VAL" not in err_msg:
            err_msg = f"⛔ ERR-VAL-009: {err_msg}"
        return Result(False, None, err_msg)

    cleaned = val_res.cleaned_data
    record = BarangRecord(
        nama_barang=cleaned['nama_barang'],
        tipe_barang=cleaned['tipe_barang'],
        satuan_uom=cleaned['satuan_uom'],
        stok_saat_ini=cleaned['stok_saat_ini'],
        harga_beli=cleaned['harga_beli'],
        harga_retail=cleaned['harga_retail'],
        harga_grosir=cleaned['harga_grosir'],
        min_grosir=cleaned['min_grosir'],
        harga_mitra=cleaned['harga_mitra'],
        cabang_id=cleaned['cabang_id']
    )
    return Result(True, record, None)


def hitung_dimensi_bahan_baku(panjang: Decimal, lebar: Decimal) -> Decimal:
    """Menghitung total dimensi/luas bahan baku (panjang x lebar) dengan desimal presisi.

    Args:
        panjang (Decimal): Ukuran panjang bahan baku.
        lebar (Decimal): Ukuran lebar bahan baku.

    Returns:
        Decimal: Total luas permukaan bahan baku, dibulatkan ke 4 desimal (ROUND_HALF_UP).
    """
    if isinstance(panjang, float) or isinstance(lebar, float):
        raise TypeError("Dimensi tidak boleh diinput menggunakan tipe data float!")
    
    if not isinstance(panjang, Decimal) or not isinstance(lebar, Decimal):
        raise TypeError("Dimensi harus berupa Decimal!")

    if panjang < Decimal('0.0000') or lebar < Decimal('0.0000'):
        raise ValueError("Dimensi panjang dan lebar tidak boleh bernilai negatif!")

    luas = panjang * lebar
    return luas.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)


def hitung_rasio_harga_kuantitas(harga: Decimal, kuantitas: Decimal) -> Result:
    """Menghitung rasio harga dibagi kuantitas dengan mitigasi pembagian nol secara aman.

    Args:
        harga (Decimal): Nilai finansial harga.
        kuantitas (Decimal): Nilai volume/kuantitas barang.

    Returns:
        Result: Status keberhasilan beserta hasil rasio harga dibagi kuantitas.
    """
    if isinstance(harga, float) or isinstance(kuantitas, float):
        return Result(
            False,
            None,
            "⛔ ERR-VAL-050: Argumen finansial/kuantitas tidak boleh menggunakan tipe data float!"
        )

    if not isinstance(harga, Decimal) or not isinstance(kuantitas, Decimal):
        return Result(
            False,
            None,
            "⛔ ERR-VAL-050: Argumen finansial/kuantitas harus berupa tipe data Decimal!"
        )

    if harga < Decimal('0.0000') or kuantitas < Decimal('0.0000'):
        return Result(
            False,
            None,
            "⛔ ERR-VAL-009: Nominal harga dan kuantitas tidak boleh bernilai negatif!"
        )

    if kuantitas == Decimal('0.0000'):
        return Result(
            False,
            None,
            "⛔ ERR-VAL-009: Perhitungan rasio gagal karena kuantitas bernilai nol (ZeroDivisionError prevented)!"
        )

    rasio = harga / kuantitas
    return Result(True, rasio.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP), None)


def validasi_kuantitas_bom(kuantitas_raw: str) -> ValidationResult:
    """Memvalidasi kuantitas desimal untuk formula BOM.

    Args:
        kuantitas_raw (str): Input kuantitas mentah dari pengguna.

    Returns:
        ValidationResult: NamedTuple (is_valid, cleaned_data, error_msg).
    """
    if kuantitas_raw is None or str(kuantitas_raw).strip() == '':
        return ValidationResult(False, None, "⛔ ERR-VAL-007: Input kuantitas bahan baku tidak valid (harus angka desimal positif > 0)!")
    try:
        val = Decimal(str(kuantitas_raw).strip())
    except (ValueError, InvalidOperation):
        return ValidationResult(False, None, "⛔ ERR-VAL-007: Input kuantitas bahan baku tidak valid (harus angka desimal positif > 0)!")

    if val <= Decimal('0.0000'):
        return ValidationResult(False, None, "⛔ ERR-VAL-007: Input kuantitas bahan baku tidak valid (harus angka desimal positif > 0)!")

    cleaned = val.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    return ValidationResult(True, cleaned, None)


def validasi_bahan_baku_id(bahan_baku_id_raw: str) -> ValidationResult:
    """Memvalidasi ID bahan baku.

    Args:
        bahan_baku_id_raw (str): Input ID bahan baku mentah.

    Returns:
        ValidationResult: NamedTuple (is_valid, cleaned_data, error_msg).
    """
    if bahan_baku_id_raw is None or str(bahan_baku_id_raw).strip() == '':
        return ValidationResult(False, None, "⛔ ERR-VAL-008: ID bahan baku tidak valid!")
    try:
        val_str = str(bahan_baku_id_raw).strip()
        if '.' in val_str:
            return ValidationResult(False, None, "⛔ ERR-VAL-008: ID bahan baku tidak valid!")
        val = int(val_str)
    except ValueError:
        return ValidationResult(False, None, "⛔ ERR-VAL-008: ID bahan baku tidak valid!")

    if val <= 0:
        return ValidationResult(False, None, "⛔ ERR-VAL-008: ID bahan baku tidak valid!")

    return ValidationResult(True, val, None)


def buat_audit_payload_bom(
    action_type: str,
    old_data: dict | None,
    new_data: dict | None
) -> tuple[str, str]:
    """Fungsi murni untuk menyusun payload JSON audit trail perubahan data formula BOM.

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


