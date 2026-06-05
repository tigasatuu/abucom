"""
Nama Modul: safety_validator.py
Deskripsi: Logika bisnis sanitasi input CLI dan validasi kekuatan kata sandi.
           (Ref: Module Structure Bab 5.5)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import re
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
