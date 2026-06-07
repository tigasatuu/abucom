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

# Pola Penanganan Kesalahan: Result NamedTuple program AbuCom
Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


def to_result(val) -> Result:
    """Helper untuk memetakan hasil validasi ke NamedTuple Result."""
    is_success = getattr(val, 'is_valid', False)
    data = getattr(val, 'cleaned_value', getattr(val, 'sanitized_data', None))
    return Result(is_success=is_success, data=data, error_msg=val.error_msg)


@pytest.fixture(autouse=True)
def setup_clean_state() -> None:
    """Fixture untuk menjamin setiap skenario pengujian unit bersih dari residu state sebelumnya."""
    # Karena modul sanitasi menggunakan pure functions tanpa state global,
    # fixture ini memastikan isolasi deterministik.
    pass


# =====================================================================
# TEST GROUP 1: sanitasi_input_cli()
# =====================================================================

def test_sanitasi_input_normal() -> None:
    assert sanitasi_input_cli("Admin_Kasir") == "Admin_Kasir"


def test_sanitasi_input_ansi_escape() -> None:
    # \x1b (ord 27) < 0x20, must be stripped, other characters preserved
    assert sanitasi_input_cli("\x1b[31mBarang Palsu") == "[31mBarang Palsu"


def test_sanitasi_input_null_byte() -> None:
    # \x00 (ord 0) < 0x20, must be stripped
    assert sanitasi_input_cli("Barang\x00Palsu") == "BarangPalsu"


def test_sanitasi_input_tab_newline() -> None:
    # \t (ord 9) and \n (ord 10) < 0x20, must be stripped
    assert sanitasi_input_cli("Barang\t\nPalsu") == "BarangPalsu"


def test_sanitasi_input_empty() -> None:
    assert sanitasi_input_cli("") == ""


def test_sanitasi_input_unicode_valid() -> None:
    # Unicode chars >= 0x20 must be preserved
    assert sanitasi_input_cli("Kertas HVS Ä4 — Premium") == "Kertas HVS Ä4 — Premium"


def test_sanitasi_input_sql_injection_string() -> None:
    # SQL injection characters >= 0x20 are preserved
    assert sanitasi_input_cli("' OR '1'='1") == "' OR '1'='1"


def test_sanitasi_input_invalid_types() -> None:
    # sanitasi_input_cli expects a string and raises TypeError for other types
    with pytest.raises(TypeError):
        sanitasi_input_cli(None)
    with pytest.raises(TypeError):
        sanitasi_input_cli(123)  # type: ignore
    with pytest.raises(TypeError):
        sanitasi_input_cli(["test"])  # type: ignore


# =====================================================================
# TEST GROUP 2: validasi_kekuatan_sandi()
# =====================================================================

def test_kekuatan_sandi_valid() -> None:
    res = to_result(validasi_kekuatan_sandi("SandiKuat123!"))
    assert res == Result(is_success=True, data="SandiKuat123!", error_msg=None)


def test_kekuatan_sandi_lemah_panjang() -> None:
    res = to_result(validasi_kekuatan_sandi("lemah"))
    assert res.is_success is False
    assert "ERR-VAL-001" in res.error_msg
    assert "minimal 8 karakter" in res.error_msg


def test_kekuatan_sandi_tanpa_huruf_besar() -> None:
    res = to_result(validasi_kekuatan_sandi("sandikuat123!"))
    assert res.is_success is False
    assert "ERR-VAL-001" in res.error_msg
    assert "minimal 1 huruf besar" in res.error_msg


def test_kekuatan_sandi_tanpa_huruf_kecil() -> None:
    res = to_result(validasi_kekuatan_sandi("SANDIKUAT123!"))
    assert res.is_success is False
    assert "ERR-VAL-001" in res.error_msg
    assert "minimal 1 huruf kecil" in res.error_msg


def test_kekuatan_sandi_tanpa_angka() -> None:
    res = to_result(validasi_kekuatan_sandi("SandiKuat!!!"))
    assert res.is_success is False
    assert "ERR-VAL-001" in res.error_msg
    assert "minimal 1 angka" in res.error_msg


def test_kekuatan_sandi_tanpa_spesial() -> None:
    res = to_result(validasi_kekuatan_sandi("SandiKuat123"))
    assert res.is_success is False
    assert "ERR-VAL-001" in res.error_msg
    assert "minimal 1 karakter spesial" in res.error_msg


def test_kekuatan_sandi_tipe_salah() -> None:
    # Input None, int, list
    for val in (None, 12345678, ["password"]):
        res = to_result(validasi_kekuatan_sandi(val))
        assert res.is_success is False
        assert "ERR-VAL-001" in res.error_msg


# =====================================================================
# TEST GROUP 3: validasi_panjang_input()
# =====================================================================

def test_panjang_input_valid() -> None:
    res = to_result(validasi_panjang_input("kasir_01", 50, "username"))
    assert res == Result(is_success=True, data="kasir_01", error_msg=None)


def test_panjang_input_boundary_exact() -> None:
    val = "x" * 50
    res = to_result(validasi_panjang_input(val, 50, "username"))
    assert res == Result(is_success=True, data=val, error_msg=None)


def test_panjang_input_exceeded() -> None:
    val = "x" * 51
    res = to_result(validasi_panjang_input(val, 50, "username"))
    assert res == Result(is_success=False, data="", error_msg="ERR-VAL-LEN: Input username melebihi batas maksimum 50 karakter!")


def test_panjang_input_empty() -> None:
    res = to_result(validasi_panjang_input("", 50, "username"))
    assert res == Result(is_success=True, data="", error_msg=None)


def test_panjang_input_tipe_salah() -> None:
    for val in (None, 123, ["username"]):
        res = to_result(validasi_panjang_input(val, 50, "username"))
        assert res.is_success is False
        assert "ERR-VAL-LEN" in res.error_msg


# =====================================================================
# TEST GROUP 4: validasi_format_whatsapp()
# =====================================================================

def test_whatsapp_valid_10digit() -> None:
    res = to_result(validasi_format_whatsapp("0812345678"))
    assert res == Result(is_success=True, data="0812345678", error_msg=None)


def test_whatsapp_valid_13digit() -> None:
    res = to_result(validasi_format_whatsapp("0812345678901"))
    assert res == Result(is_success=True, data="0812345678901", error_msg=None)


def test_whatsapp_invalid_prefix() -> None:
    res = to_result(validasi_format_whatsapp("6281234567890"))
    assert res.is_success is False
    assert "ERR-VAL-WA" in res.error_msg


def test_whatsapp_invalid_short() -> None:
    res = to_result(validasi_format_whatsapp("081234"))
    assert res.is_success is False
    assert "ERR-VAL-WA" in res.error_msg


def test_whatsapp_invalid_alpha() -> None:
    res = to_result(validasi_format_whatsapp("08123abcde"))
    assert res.is_success is False
    assert "ERR-VAL-WA" in res.error_msg


def test_whatsapp_empty() -> None:
    res = to_result(validasi_format_whatsapp(""))
    assert res.is_success is False
    assert "ERR-VAL-WA" in res.error_msg


def test_whatsapp_tipe_salah() -> None:
    for val in (None, 81234567890, ["081234567890"]):
        res = to_result(validasi_format_whatsapp(val))
        assert res.is_success is False
        assert "ERR-VAL-WA" in res.error_msg


# =====================================================================
# TEST GROUP 5: validasi_format_tanggal()
# =====================================================================

def test_tanggal_valid() -> None:
    res = to_result(validasi_format_tanggal("2026-05-29"))
    assert res == Result(is_success=True, data="2026-05-29", error_msg=None)


def test_tanggal_invalid_format() -> None:
    res = to_result(validasi_format_tanggal("29-05-2026"))
    assert res.is_success is False
    assert "ERR-VAL-DATE" in res.error_msg


def test_tanggal_invalid_calendar() -> None:
    res = to_result(validasi_format_tanggal("2026-13-45"))
    assert res.is_success is False
    assert "ERR-VAL-DATE" in res.error_msg


def test_tanggal_invalid_leap() -> None:
    res = to_result(validasi_format_tanggal("2025-02-29"))
    assert res.is_success is False
    assert "ERR-VAL-DATE" in res.error_msg


def test_tanggal_empty() -> None:
    res = to_result(validasi_format_tanggal(""))
    assert res.is_success is False
    assert "ERR-VAL-DATE" in res.error_msg


def test_tanggal_tipe_salah() -> None:
    for val in (None, 20260529, ["2026-05-29"]):
        res = to_result(validasi_format_tanggal(val))
        assert res.is_success is False
        assert "ERR-VAL-DATE" in res.error_msg


# =====================================================================
# TEST GROUP 6: validasi_input_numerik_positif()
# =====================================================================

def test_numerik_valid() -> None:
    res = to_result(validasi_input_numerik_positif("102", "ID Barang"))
    assert res == Result(is_success=True, data="102", error_msg=None)


def test_numerik_zero() -> None:
    res = to_result(validasi_input_numerik_positif("0", "ID Barang"))
    assert res.is_success is False
    assert "ERR-VAL-NUM" in res.error_msg


def test_numerik_negative() -> None:
    res = to_result(validasi_input_numerik_positif("-5", "ID Barang"))
    assert res.is_success is False
    assert "ERR-VAL-NUM" in res.error_msg


def test_numerik_float() -> None:
    res = to_result(validasi_input_numerik_positif("3.14", "ID Barang"))
    assert res.is_success is False
    assert "ERR-VAL-NUM" in res.error_msg


def test_numerik_alpha() -> None:
    res = to_result(validasi_input_numerik_positif("abc", "ID Barang"))
    assert res.is_success is False
    assert "ERR-VAL-NUM" in res.error_msg


def test_numerik_empty() -> None:
    res = to_result(validasi_input_numerik_positif("", "ID Barang"))
    assert res.is_success is False
    assert "ERR-VAL-NUM" in res.error_msg


def test_numerik_tipe_salah() -> None:
    for val in (None, 102, [102]):
        res = to_result(validasi_input_numerik_positif(val, "ID Barang"))
        assert res.is_success is False
        assert "ERR-VAL-NUM" in res.error_msg


# =====================================================================
# TEST GROUP 7: validasi_input_desimal_positif()
# =====================================================================

def test_desimal_valid_integer() -> None:
    res = to_result(validasi_input_desimal_positif("100000", "Nominal Rupiah"))
    assert res == Result(is_success=True, data="100000.0000", error_msg=None)


def test_desimal_valid_fraction() -> None:
    res = to_result(validasi_input_desimal_positif("0.0025", "Bahan Kuantitas"))
    assert res == Result(is_success=True, data="0.0025", error_msg=None)


def test_desimal_zero() -> None:
    res = to_result(validasi_input_desimal_positif("0", "Nominal Rupiah"))
    assert res.is_success is False
    assert "ERR-VAL-DEC" in res.error_msg


def test_desimal_negative() -> None:
    res = to_result(validasi_input_desimal_positif("-500", "Nominal Rupiah"))
    assert res.is_success is False
    assert "ERR-VAL-DEC" in res.error_msg


def test_desimal_alpha() -> None:
    res = to_result(validasi_input_desimal_positif("abc", "Nominal Rupiah"))
    assert res.is_success is False
    assert "ERR-VAL-DEC" in res.error_msg


def test_desimal_boundary_precision() -> None:
    res = to_result(validasi_input_desimal_positif("0.00005", "Nominal Rupiah"))
    assert res == Result(is_success=True, data="0.0001", error_msg=None)


def test_desimal_empty() -> None:
    res = to_result(validasi_input_desimal_positif("", "Nominal Rupiah"))
    assert res.is_success is False
    assert "ERR-VAL-DEC" in res.error_msg


def test_desimal_whitespace() -> None:
    res = to_result(validasi_input_desimal_positif("   ", "Nominal Rupiah"))
    assert res.is_success is False
    assert "ERR-VAL-DEC" in res.error_msg


def test_desimal_tipe_salah() -> None:
    for val in (None, 100.0, [100.0]):
        res = to_result(validasi_input_desimal_positif(val, "Nominal Rupiah"))
        assert res.is_success is False
        assert "ERR-VAL-DEC" in res.error_msg


# =====================================================================
# TEST GROUP 8: validasi_konfirmasi_yn()
# =====================================================================

def test_yn_valid_y() -> None:
    res = to_result(validasi_konfirmasi_yn("y"))
    assert res == Result(is_success=True, data="Y", error_msg=None)


def test_yn_valid_N() -> None:
    res = to_result(validasi_konfirmasi_yn("N"))
    assert res == Result(is_success=True, data="N", error_msg=None)


def test_yn_invalid() -> None:
    res = to_result(validasi_konfirmasi_yn("maybe"))
    assert res.is_success is False
    assert "ERR-VAL-YN" in res.error_msg


def test_yn_empty() -> None:
    res = to_result(validasi_konfirmasi_yn(""))
    assert res.is_success is False
    assert "ERR-VAL-YN" in res.error_msg


def test_yn_tipe_salah() -> None:
    for val in (None, True, ["Y"]):
        res = to_result(validasi_konfirmasi_yn(val))
        assert res.is_success is False
        assert "ERR-VAL-YN" in res.error_msg


# =====================================================================
# TEST GROUP 9: validasi_pilihan_menu()
# =====================================================================

def test_menu_valid() -> None:
    res = to_result(validasi_pilihan_menu("3", 0, 10))
    assert res == Result(is_success=True, data="3", error_msg=None)


def test_menu_zero() -> None:
    res = to_result(validasi_pilihan_menu("0", 0, 10))
    assert res == Result(is_success=True, data="0", error_msg=None)


def test_menu_out_of_range() -> None:
    res = to_result(validasi_pilihan_menu("99", 0, 10))
    assert res.is_success is False
    assert "ERR-VAL-MENU" in res.error_msg


def test_menu_alpha() -> None:
    res = to_result(validasi_pilihan_menu("abc", 0, 10))
    assert res.is_success is False
    assert "ERR-VAL-MENU" in res.error_msg


def test_menu_empty() -> None:
    res = to_result(validasi_pilihan_menu("", 0, 10))
    assert res.is_success is False
    assert "ERR-VAL-MENU" in res.error_msg


def test_menu_tipe_salah() -> None:
    for val in (None, 3, [3]):
        res = to_result(validasi_pilihan_menu(val, 0, 10))
        assert res.is_success is False
        assert "ERR-VAL-MENU" in res.error_msg


# =====================================================================
# TEST GROUP 10: sanitasi_dan_validasi_input()
# =====================================================================

def test_pipeline_normal() -> None:
    res = to_result(sanitasi_dan_validasi_input("Kasir_Utama", 50, "Username"))
    assert res == Result(is_success=True, data="Kasir_Utama", error_msg=None)


def test_pipeline_control_chars() -> None:
    # \x1b is removed, then validated
    res = to_result(sanitasi_dan_validasi_input("\x1btest_user", 50, "Username"))
    assert res == Result(is_success=True, data="test_user", error_msg=None)


def test_pipeline_too_long() -> None:
    res = to_result(sanitasi_dan_validasi_input("\x1b" + "x" * 51, 50, "Username"))
    assert res == Result(is_success=False, data="", error_msg="ERR-VAL-LEN: Input Username melebihi batas maksimum 50 karakter!")


def test_pipeline_tipe_salah() -> None:
    for val in (None, 123456, ["Kasir"]):
        res = to_result(sanitasi_dan_validasi_input(val, 50, "Username"))
        assert res.is_success is False
        assert "ERR-VAL-LEN" in res.error_msg


# =====================================================================
# TEST GROUP 11: Security Target & Anti-SQL Injection
# =====================================================================

def test_ketika_input_injeksi_diberikan_maka_return_false_dan_err_val() -> None:
    """Memastikan payload SQL Injection yang dimasukkan ke field terformat ditolak secara aman."""
    payloads = [
        "' OR 1=1 --",
        "'; DROP TABLE pengguna;--",
        '" UNION SELECT * FROM--',
        "admin' --",
        "1' OR '1'='1"
    ]

    for payload in payloads:
        # 1. WhatsApp validation must reject SQL Injection
        res_wa = to_result(validasi_format_whatsapp(payload))
        assert res_wa.is_success is False
        assert "ERR-VAL-WA" in res_wa.error_msg

        # 2. Date validation must reject SQL Injection
        res_date = to_result(validasi_format_tanggal(payload))
        assert res_date.is_success is False
        assert "ERR-VAL-DATE" in res_date.error_msg

        # 3. Numeric validation must reject SQL Injection
        res_num = to_result(validasi_input_numerik_positif(payload, "ID Barang"))
        assert res_num.is_success is False
        assert "ERR-VAL-NUM" in res_num.error_msg

        # 4. Decimal validation must reject SQL Injection
        res_dec = to_result(validasi_input_desimal_positif(payload, "Nominal Rupiah"))
        assert res_dec.is_success is False
        assert "ERR-VAL-DEC" in res_dec.error_msg

        # 5. Y/N validation must reject SQL Injection
        res_yn = to_result(validasi_konfirmasi_yn(payload))
        assert res_yn.is_success is False
        assert "ERR-VAL-YN" in res_yn.error_msg

        # 6. Menu validation must reject SQL Injection
        res_menu = to_result(validasi_pilihan_menu(payload, 0, 10))
        assert res_menu.is_success is False
        assert "ERR-VAL-MENU" in res_menu.error_msg


def test_ketika_input_injeksi_pada_teks_biasa_maka_karakter_tetap_aman_terpreservasi() -> None:
    """Memastikan karakter SQL Injection dalam input teks umum tetap aman dipertahankan.

    Hal ini karena query SQL pada persistensi layer menggunakan parameterized queries (%s bindings),
    sehingga karakter ini tidak akan diterjemahkan sebagai perintah SQL.
    """
    payloads = [
        "' OR 1=1 --",
        "'; DROP TABLE pengguna;--",
        '" UNION SELECT * FROM--',
        "admin' --",
        "1' OR '1'='1"
    ]

    for payload in payloads:
        # sanitasi_input_cli must preserve character bytes >= 0x20
        cleaned = sanitasi_input_cli(payload)
        assert cleaned == payload

        # sanitasi_dan_validasi_input must preserve visual characters as long as it fits length bounds
        res = to_result(sanitasi_dan_validasi_input(payload, 100, "Catatan"))
        assert res == Result(is_success=True, data=payload, error_msg=None)
