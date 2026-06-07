"""
Nama Modul: safety_validator.py
Deskripsi: Logika bisnis sanitasi input CLI dan validasi kekuatan kata sandi.
           (Ref: Module Structure Bab 5.5)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import re
import datetime
from collections import namedtuple
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

# NamedTuple Definition
ValidationStatus = namedtuple('ValidationStatus', ['is_valid', 'sanitized_data', 'error_msg'])
SanitizedInput = namedtuple('SanitizedInput', ['is_valid', 'cleaned_value', 'error_msg'])


# ============================================================
# KONSTANTA LENGTH BOUNDS INPUT CLI
# (Ref: Security Design Bab 6.4 — Length Bounds Validation)
# (Ref: Database Schema DDL — VARCHAR constraint)
# ============================================================
MAX_USERNAME_LENGTH = 50
MAX_PASSWORD_LENGTH = 128
MAX_WHATSAPP_LENGTH = 20
MAX_NAMA_BARANG_LENGTH = 100
MAX_NAMA_PENGGUNA_LENGTH = 100
MAX_ALAMAT_LENGTH = 200
MAX_DESKRIPSI_LENGTH = 500
MAX_CATATAN_LENGTH = 500
MAX_GENERIC_INPUT_LENGTH = 255
MAX_KODE_LENGTH = 20
MAX_MEMO_LENGTH = 1000


def sanitasi_input_cli(raw_input: str) -> str:
    """Membuang karakter kontrol ASCII di bawah byte 0x20.

    Args:
        raw_input (str): String mentah dari input keyboard CLI.

    Returns:
        str: String yang sudah dibersihkan dari karakter kontrol.
    """
    return ''.join(char for char in raw_input if ord(char) >= 0x20)


def validasi_kekuatan_sandi(password: str) -> ValidationStatus:
    """Validasi kriteria sandi aman sesuai Security Design v1.2.

    Kriteria wajib:
    - Minimal 8 karakter.
    - Mengandung minimal 1 huruf besar (A-Z).
    - Mengandung minimal 1 huruf kecil (a-z).
    - Mengandung minimal 1 angka (0-9).
    - Mengandung minimal 1 karakter spesial (!@#$%^&*()_+-=[]{}|;':\",./<>?).

    Args:
        password (str): Kata sandi polos yang ingin divalidasi.

    Returns:
        ValidationStatus: NamedTuple berisi is_valid (bool), sanitized_data (str),
                          dan error_msg (str | None).

    Example:
        >>> validasi_kekuatan_sandi('SandiKuat123!')
        ValidationStatus(is_valid=True, sanitized_data='SandiKuat123!', error_msg=None)
        >>> validasi_kekuatan_sandi('lemah')
        ValidationStatus(is_valid=False, sanitized_data='lemah', error_msg='ERR-VAL-001: ...')
    """
    if not isinstance(password, str):
        return ValidationStatus(
            False,
            "",
            "ERR-VAL-001: Sandi Lemah: Tipe data password harus berupa string!"
        )
    errors: list[str] = []

    if len(password) < 8:
        errors.append('minimal 8 karakter')
    if not re.search(r'[A-Z]', password):
        errors.append('minimal 1 huruf besar (A-Z)')
    if not re.search(r'[a-z]', password):
        errors.append('minimal 1 huruf kecil (a-z)')
    if not re.search(r'[0-9]', password):
        errors.append('minimal 1 angka (0-9)')
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{}|;\':",./<>?]', password):
        errors.append('minimal 1 karakter spesial')

    if errors:
        detail = ', '.join(errors)
        return ValidationStatus(
            False,
            password,
            f'ERR-VAL-001: Sandi Lemah: Kata sandi harus memenuhi kriteria: {detail}!'
        )

    return ValidationStatus(True, password, None)


def validasi_panjang_input(raw_input: str, max_length: int, field_name: str) -> SanitizedInput:
    """Memvalidasi panjang input tidak melebihi batas maksimum field.

    (Ref: Security Design Bab 6.4 — Length Bounds Validation)

    Args:
        raw_input (str): String input yang sudah disanitasi karakter kontrol.
        max_length (int): Batas maksimum karakter yang diizinkan.
        field_name (str): Nama field untuk pesan error deskriptif.

    Returns:
        SanitizedInput: NamedTuple berisi is_valid (bool), cleaned_value (str),
                        dan error_msg (str | None).

    Example:
        >>> validasi_panjang_input('kasir_01', 50, 'username')
        SanitizedInput(is_valid=True, cleaned_value='kasir_01', error_msg=None)
        >>> validasi_panjang_input('x' * 51, 50, 'username')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-LEN: ...')
    """
    if not isinstance(raw_input, str):
        return SanitizedInput(
            False,
            "",
            f"ERR-VAL-LEN: Tipe data {field_name} harus berupa string!"
        )
    if len(raw_input) > max_length:
        return SanitizedInput(
            False,
            "",
            f"ERR-VAL-LEN: Input {field_name} melebihi batas maksimum {max_length} karakter!"
        )
    return SanitizedInput(True, raw_input, None)


def validasi_format_whatsapp(nomor_wa: str) -> SanitizedInput:
    """Memvalidasi format nomor WhatsApp Indonesia.

    (Ref: Security Design Bab 6.4 — Regex Format Validation)
    Format valid: Diawali '08', diikuti 8-11 digit angka.

    Args:
        nomor_wa (str): String nomor WhatsApp mentah.

    Returns:
        SanitizedInput: NamedTuple validasi format nomor WhatsApp.

    Example:
        >>> validasi_format_whatsapp('081234567890')
        SanitizedInput(is_valid=True, cleaned_value='081234567890', error_msg=None)
        >>> validasi_format_whatsapp('0812')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-WA: ...')
    """
    if not isinstance(nomor_wa, str):
        return SanitizedInput(
            False,
            "",
            "ERR-VAL-WA: Tipe data nomor WhatsApp harus berupa string!"
        )
    if not re.match(r'^08[0-9]{8,11}$', nomor_wa):
        return SanitizedInput(
            False,
            "",
            "ERR-VAL-WA: Format nomor WhatsApp tidak valid! Gunakan format 08xxxxxxxxxx (10-13 digit)."
        )
    return SanitizedInput(True, nomor_wa, None)


def validasi_format_tanggal(tanggal_str: str) -> SanitizedInput:
    """Memvalidasi format tanggal YYYY-MM-DD dan keabsahan kalender.

    (Ref: CLI Interaction Flow Bab 2.4 — Validasi Regex)

    Args:
        tanggal_str (str): String tanggal mentah dari input CLI.

    Returns:
        SanitizedInput: NamedTuple validasi format tanggal.

    Example:
        >>> validasi_format_tanggal('2026-05-29')
        SanitizedInput(is_valid=True, cleaned_value='2026-05-29', error_msg=None)
        >>> validasi_format_tanggal('2026-13-45')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-DATE: ...')
    """
    if not isinstance(tanggal_str, str):
        return SanitizedInput(
            False,
            "",
            "ERR-VAL-DATE: Tipe data tanggal harus berupa string!"
        )
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', tanggal_str):
        return SanitizedInput(
            False,
            "",
            "ERR-VAL-DATE: Format tanggal tidak valid! Gunakan format YYYY-MM-DD (contoh: 2026-01-31)."
        )
    try:
        datetime.datetime.strptime(tanggal_str, "%Y-%m-%d")
    except ValueError:
        return SanitizedInput(
            False,
            "",
            "ERR-VAL-DATE: Format tanggal tidak valid! Gunakan format YYYY-MM-DD (contoh: 2026-01-31)."
        )
    return SanitizedInput(True, tanggal_str, None)


def validasi_input_numerik_positif(raw_input: str, field_name: str) -> SanitizedInput:
    """Memvalidasi input sebagai bilangan bulat positif (integer > 0).

    (Ref: CLI Interaction Flow Bab 5.1 — Input ID Barang & Qty)

    Args:
        raw_input (str): String input mentah dari CLI.
        field_name (str): Nama field untuk pesan error deskriptif.

    Returns:
        SanitizedInput: NamedTuple validasi, cleaned_value berisi string angka.

    Example:
        >>> validasi_input_numerik_positif('102', 'ID Barang')
        SanitizedInput(is_valid=True, cleaned_value='102', error_msg=None)
        >>> validasi_input_numerik_positif('-5', 'ID Barang')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-NUM: ...')
    """
    if not isinstance(raw_input, str):
        return SanitizedInput(
            False,
            "",
            f"ERR-VAL-NUM: Tipe data {field_name} harus berupa string!"
        )
    try:
        val = int(raw_input)
        if val <= 0:
            raise ValueError()
    except ValueError:
        return SanitizedInput(
            False,
            "",
            f"ERR-VAL-NUM: Input {field_name} harus berupa angka bulat positif!"
        )
    return SanitizedInput(True, str(val), None)


def validasi_input_desimal_positif(raw_input: str, field_name: str) -> SanitizedInput:
    """Memvalidasi dan mengonversi input ke Decimal positif presisi 4 desimal.

    (Ref: CLI Interaction Flow Bab 2.4 — Fixed-Point Decimal)
    (Ref: Coding Standard Bab 2.4 — Decimal-First Policy)

    Args:
        raw_input (str): String input nominal dari CLI.
        field_name (str): Nama field untuk pesan error deskriptif.

    Returns:
        SanitizedInput: NamedTuple validasi, cleaned_value berisi string Decimal.

    Example:
        >>> validasi_input_desimal_positif('100000', 'Nominal Rupiah')
        SanitizedInput(is_valid=True, cleaned_value='100000.0000', error_msg=None)
        >>> validasi_input_desimal_positif('abc', 'Nominal Rupiah')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-DEC: ...')
    """
    if not isinstance(raw_input, str):
        return SanitizedInput(
            False,
            "",
            f"ERR-VAL-DEC: Tipe data {field_name} harus berupa string!"
        )
    try:
        if not raw_input.strip():
            raise ValueError()
        dec_val = Decimal(raw_input.strip()).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
        if dec_val <= 0:
            raise ValueError()
    except (ValueError, InvalidOperation):
        return SanitizedInput(
            False,
            "",
            f"ERR-VAL-DEC: Input {field_name} harus berupa angka desimal positif!"
        )
    return SanitizedInput(True, f"{dec_val:.4f}", None)


def validasi_konfirmasi_yn(raw_input: str) -> SanitizedInput:
    """Memvalidasi input konfirmasi biner Y/N (case-insensitive).

    (Ref: CLI Interaction Flow Bab 2.2 — Pola Konfirmasi Aksi Destruktif)

    Args:
        raw_input (str): String input konfirmasi dari CLI.

    Returns:
        SanitizedInput: NamedTuple validasi, cleaned_value berisi 'Y' atau 'N'.

    Example:
        >>> validasi_konfirmasi_yn('y')
        SanitizedInput(is_valid=True, cleaned_value='Y', error_msg=None)
        >>> validasi_konfirmasi_yn('maybe')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-YN: ...')
    """
    if not isinstance(raw_input, str):
        return SanitizedInput(
            False,
            "",
            "ERR-VAL-YN: Tipe data konfirmasi harus berupa string!"
        )
    cleaned = raw_input.strip().upper()
    if cleaned not in ('Y', 'N'):
        return SanitizedInput(
            False,
            "",
            "ERR-VAL-YN: Input konfirmasi tidak valid! Ketik Y atau N."
        )
    return SanitizedInput(True, cleaned, None)


def validasi_pilihan_menu(raw_input: str, min_val: int, max_val: int) -> SanitizedInput:
    """Memvalidasi input pilihan menu numerik dalam rentang yang diizinkan.

    (Ref: CLI Interaction Flow Bab 2.2 — Hotkey Numerik)

    Args:
        raw_input (str): String input pilihan menu dari CLI.
        min_val (int): Nilai minimum pilihan yang valid (biasanya 0).
        max_val (int): Nilai maksimum pilihan yang valid.

    Returns:
        SanitizedInput: NamedTuple validasi, cleaned_value berisi string angka.

    Example:
        >>> validasi_pilihan_menu('3', 0, 10)
        SanitizedInput(is_valid=True, cleaned_value='3', error_msg=None)
        >>> validasi_pilihan_menu('99', 0, 10)
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-MENU: ...')
    """
    if not isinstance(raw_input, str):
        return SanitizedInput(
            False,
            "",
            "ERR-VAL-MENU: Tipe data pilihan menu harus berupa string!"
        )
    try:
        val = int(raw_input)
        if not (min_val <= val <= max_val):
            raise ValueError()
    except ValueError:
        return SanitizedInput(
            False,
            "",
            f"ERR-VAL-MENU: Pilihan menu tidak valid! Masukkan angka {min_val}-{max_val}."
        )
    return SanitizedInput(True, str(val), None)


def sanitasi_dan_validasi_input(raw_input: str, max_length: int, field_name: str) -> SanitizedInput:
    """Menjalankan sanitasi karakter kontrol DAN validasi panjang input secara berurutan.

    Pipeline: raw_input → sanitasi_input_cli() → strip() → validasi_panjang_input()

    (Ref: Security Design Bab 6.4 — Defense in Depth Input Validation)

    Args:
        raw_input (str): String mentah dari input keyboard CLI.
        max_length (int): Batas maksimum karakter setelah sanitasi.
        field_name (str): Nama field untuk pesan error deskriptif.

    Returns:
        SanitizedInput: NamedTuple berisi hasil sanitasi dan validasi.

    Example:
        >>> sanitasi_dan_validasi_input('\\x1bNama Barang', 100, 'Nama Barang')
        SanitizedInput(is_valid=True, cleaned_value='Nama Barang', error_msg=None)
    """
    if not isinstance(raw_input, str):
        return SanitizedInput(
            False,
            "",
            f"ERR-VAL-LEN: Tipe data {field_name} harus berupa string!"
        )
    sanitized = sanitasi_input_cli(raw_input).strip()
    return validasi_panjang_input(sanitized, max_length, field_name)

