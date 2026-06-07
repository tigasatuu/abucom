"""
Nama Modul: tests/test_sanitasi_input.py
Deskripsi: Unit test komprehensif untuk sanitasi input CLI dan validasi keamanan.
           (Ref: Test Plan Bab 5.5 & Bab 5.3)
Author: Antigravity
Tanggal: 2026-06-07
"""

import pytest
import datetime
from collections import namedtuple
from decimal import Decimal
from logic.safety_validator import (
    sanitasi_input_cli,
    validasi_kekuatan_sandi,
    validasi_panjang_input,
    validasi_format_whatsapp,
    validasi_format_tanggal,
    validasi_input_numerik_positif,
    validasi_input_desimal_positif,
    validasi_konfirmasi_yn,
    validasi_pilihan_menu,
    sanitasi_dan_validasi_input,
    MAX_USERNAME_LENGTH,
    MAX_PASSWORD_LENGTH,
    MAX_WHATSAPP_LENGTH,
    MAX_NAMA_BARANG_LENGTH,
    MAX_NAMA_PENGGUNA_LENGTH,
    MAX_ALAMAT_LENGTH,
    MAX_DESKRIPSI_LENGTH,
    MAX_CATATAN_LENGTH,
    MAX_GENERIC_INPUT_LENGTH,
    MAX_KODE_LENGTH,
    MAX_MEMO_LENGTH
)

# =====================================================================
# TEST GROUP 1: sanitasi_input_cli()
# =====================================================================

def test_sanitasi_input_normal():
    assert sanitasi_input_cli("Admin_Kasir") == "Admin_Kasir"

def test_sanitasi_input_ansi_escape():
    # \x1b (ord 27) < 0x20, must be stripped, other characters preserved
    assert sanitasi_input_cli("\x1b[31mBarang Palsu") == "[31mBarang Palsu"

def test_sanitasi_input_null_byte():
    # \x00 (ord 0) < 0x20, must be stripped
    assert sanitasi_input_cli("Barang\x00Palsu") == "BarangPalsu"

def test_sanitasi_input_tab_newline():
    # \t (ord 9) and \n (ord 10) < 0x20, must be stripped
    assert sanitasi_input_cli("Barang\t\nPalsu") == "BarangPalsu"

def test_sanitasi_input_empty():
    assert sanitasi_input_cli("") == ""

def test_sanitasi_input_unicode_valid():
    # Unicode chars >= 0x20 must be preserved
    assert sanitasi_input_cli("Kertas HVS Ä4 — Premium") == "Kertas HVS Ä4 — Premium"

def test_sanitasi_input_sql_injection_string():
    # SQL injection characters >= 0x20 are preserved
    assert sanitasi_input_cli("' OR '1'='1") == "' OR '1'='1"


# =====================================================================
# TEST GROUP 2: validasi_kekuatan_sandi() (Fungsi Existing)
# =====================================================================

def test_kekuatan_sandi_valid():
    res = validasi_kekuatan_sandi("SandiKuat123!")
    assert res.is_valid is True
    assert res.sanitized_data == "SandiKuat123!"
    assert res.error_msg is None

def test_kekuatan_sandi_weak():
    res = validasi_kekuatan_sandi("lemah")
    assert res.is_valid is False
    assert "ERR-VAL-001" in res.error_msg
    assert "minimal 8 karakter" in res.error_msg


# =====================================================================
# TEST GROUP 3: validasi_panjang_input()
# =====================================================================

def test_panjang_input_valid():
    res = validasi_panjang_input("kasir_01", 50, "username")
    assert res.is_valid is True
    assert res.cleaned_value == "kasir_01"
    assert res.error_msg is None

def test_panjang_input_boundary_exact():
    val = "x" * 50
    res = validasi_panjang_input(val, 50, "username")
    assert res.is_valid is True
    assert res.cleaned_value == val
    assert res.error_msg is None

def test_panjang_input_exceeded():
    val = "x" * 51
    res = validasi_panjang_input(val, 50, "username")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-LEN" in res.error_msg
    assert "username" in res.error_msg
    assert "50" in res.error_msg

def test_panjang_input_empty():
    res = validasi_panjang_input("", 50, "username")
    assert res.is_valid is True
    assert res.cleaned_value == ""
    assert res.error_msg is None


# =====================================================================
# TEST GROUP 4: validasi_format_whatsapp()
# =====================================================================

def test_whatsapp_valid_10digit():
    res = validasi_format_whatsapp("0812345678")
    assert res.is_valid is True
    assert res.cleaned_value == "0812345678"
    assert res.error_msg is None

def test_whatsapp_valid_13digit():
    res = validasi_format_whatsapp("0812345678901")
    assert res.is_valid is True
    assert res.cleaned_value == "0812345678901"
    assert res.error_msg is None

def test_whatsapp_invalid_prefix():
    res = validasi_format_whatsapp("6281234567890")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-WA" in res.error_msg

def test_whatsapp_invalid_short():
    res = validasi_format_whatsapp("081234")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-WA" in res.error_msg

def test_whatsapp_invalid_alpha():
    res = validasi_format_whatsapp("08123abcde")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-WA" in res.error_msg

def test_whatsapp_empty():
    res = validasi_format_whatsapp("")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-WA" in res.error_msg


# =====================================================================
# TEST GROUP 5: validasi_format_tanggal()
# =====================================================================

def test_tanggal_valid():
    res = validasi_format_tanggal("2026-05-29")
    assert res.is_valid is True
    assert res.cleaned_value == "2026-05-29"
    assert res.error_msg is None

def test_tanggal_invalid_format():
    res = validasi_format_tanggal("29-05-2026")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-DATE" in res.error_msg

def test_tanggal_invalid_calendar():
    res = validasi_format_tanggal("2026-13-45")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-DATE" in res.error_msg

def test_tanggal_invalid_leap():
    res = validasi_format_tanggal("2025-02-29")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-DATE" in res.error_msg

def test_tanggal_empty():
    res = validasi_format_tanggal("")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-DATE" in res.error_msg


# =====================================================================
# TEST GROUP 6: validasi_input_numerik_positif()
# =====================================================================

def test_numerik_valid():
    res = validasi_input_numerik_positif("102", "ID Barang")
    assert res.is_valid is True
    assert res.cleaned_value == "102"
    assert res.error_msg is None

def test_numerik_zero():
    res = validasi_input_numerik_positif("0", "ID Barang")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-NUM" in res.error_msg

def test_numerik_negative():
    res = validasi_input_numerik_positif("-5", "ID Barang")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-NUM" in res.error_msg

def test_numerik_float():
    res = validasi_input_numerik_positif("3.14", "ID Barang")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-NUM" in res.error_msg

def test_numerik_alpha():
    res = validasi_input_numerik_positif("abc", "ID Barang")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-NUM" in res.error_msg


# =====================================================================
# TEST GROUP 7: validasi_input_desimal_positif()
# =====================================================================

def test_desimal_valid_integer():
    res = validasi_input_desimal_positif("100000", "Nominal Rupiah")
    assert res.is_valid is True
    assert res.cleaned_value == "100000.0000"
    assert res.error_msg is None

def test_desimal_valid_fraction():
    res = validasi_input_desimal_positif("0.0025", "Bahan Kuantitas")
    assert res.is_valid is True
    assert res.cleaned_value == "0.0025"
    assert res.error_msg is None

def test_desimal_zero():
    res = validasi_input_desimal_positif("0", "Nominal Rupiah")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-DEC" in res.error_msg

def test_desimal_negative():
    res = validasi_input_desimal_positif("-500", "Nominal Rupiah")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-DEC" in res.error_msg

def test_desimal_alpha():
    res = validasi_input_desimal_positif("abc", "Nominal Rupiah")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-DEC" in res.error_msg

def test_desimal_boundary_precision():
    res = validasi_input_desimal_positif("0.00005", "Nominal Rupiah")
    assert res.is_valid is True
    assert res.cleaned_value == "0.0001"
    assert res.error_msg is None


# =====================================================================
# TEST GROUP 8: validasi_konfirmasi_yn()
# =====================================================================

def test_yn_valid_y():
    res = validasi_konfirmasi_yn("y")
    assert res.is_valid is True
    assert res.cleaned_value == "Y"
    assert res.error_msg is None

def test_yn_valid_N():
    res = validasi_konfirmasi_yn("N")
    assert res.is_valid is True
    assert res.cleaned_value == "N"
    assert res.error_msg is None

def test_yn_invalid():
    res = validasi_konfirmasi_yn("maybe")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-YN" in res.error_msg

def test_yn_empty():
    res = validasi_konfirmasi_yn("")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-YN" in res.error_msg


# =====================================================================
# TEST GROUP 9: validasi_pilihan_menu()
# =====================================================================

def test_menu_valid():
    res = validasi_pilihan_menu("3", 0, 10)
    assert res.is_valid is True
    assert res.cleaned_value == "3"
    assert res.error_msg is None

def test_menu_zero():
    res = validasi_pilihan_menu("0", 0, 10)
    assert res.is_valid is True
    assert res.cleaned_value == "0"
    assert res.error_msg is None

def test_menu_out_of_range():
    res = validasi_pilihan_menu("99", 0, 10)
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-MENU" in res.error_msg

def test_menu_alpha():
    res = validasi_pilihan_menu("abc", 0, 10)
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-MENU" in res.error_msg


# =====================================================================
# TEST GROUP 10: sanitasi_dan_validasi_input()
# =====================================================================

def test_pipeline_normal():
    res = sanitasi_dan_validasi_input("Kasir_Utama", 50, "Username")
    assert res.is_valid is True
    assert res.cleaned_value == "Kasir_Utama"
    assert res.error_msg is None

def test_pipeline_control_chars():
    # \x1b is removed, then validated
    res = sanitasi_dan_validasi_input("\x1btest_user", 50, "Username")
    assert res.is_valid is True
    assert res.cleaned_value == "test_user"
    assert res.error_msg is None

def test_pipeline_too_long():
    res = sanitasi_dan_validasi_input("\x1b" + "x" * 51, 50, "Username")
    assert res.is_valid is False
    assert res.cleaned_value == ""
    assert "ERR-VAL-LEN" in res.error_msg


# ============================================================
# DATA GAP REPORT — Issue #0120
# ============================================================
# 1. MAX_LENGTH for 'alamat_supplier' and 'alamat' (cabang) is defined as TEXT in the database,
#    but we use MAX_ALAMAT_LENGTH = 200 for memory and CLI inputs.
# 2. The 'whatsapp' field in pelanggan table is VARCHAR(100) in MySQL to support encrypted values,
#    while the unencrypted raw input is validated against MAX_WHATSAPP_LENGTH = 20.
# 3. Validation rules (such as length bounds) for secondary fields like 'nama_unit',
#    'detail_kerusakan', and 'estimasi_biaya' are not explicitly specified in the SDLC requirements,
#    so standard values (e.g. MAX_NAMA_BARANG_LENGTH = 100 or MAX_DESKRIPSI_LENGTH = 500) are assumed.
# ============================================================
