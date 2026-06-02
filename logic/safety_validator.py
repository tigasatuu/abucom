"""
Nama Modul: safety_validator.py
Deskripsi: Logika bisnis sanitasi input CLI dan validasi kekuatan kata sandi.
           (Ref: Module Structure Bab 5.5)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

from collections import namedtuple

# NamedTuple Definition
ValidationStatus = namedtuple('ValidationStatus', ['is_valid', 'sanitized_data', 'error_msg'])


def sanitasi_input_cli(raw_input: str) -> str:
    """Membuang karakter kontrol ASCII di bawah byte 0x20.

    Args:
        raw_input (str): String mentah dari input keyboard CLI.

    Returns:
        str: String yang sudah dibersihkan dari karakter kontrol.
    """
    return ''.join(char for char in raw_input if ord(char) >= 0x20)


def validasi_kekuatan_sandi(password: str) -> ValidationStatus:
    """Validasi kriteria sandi aman (min 8 karakter, uppercase, lowercase, numerik, spesial).

    Args:
        password (str): Kata sandi polos yang ingin divalidasi.

    Returns:
        ValidationStatus: Status validasi beserta pesan error jika tidak valid.
    """
    # TODO: Implementasi regex/kriteria validasi password kuat
    return ValidationStatus(False, password, 'ERR-VAL-001: Validasi sandi belum diimplementasikan.')
