"""
Nama Modul: text_formatter.py
Deskripsi: Utilitas pemformatan tampilan teks visual CLI dan struk belanja thermal.
           (Ref: Module Structure Bab 9.4)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import os
import platform


def clear_terminal() -> None:
    """Membersihkan layar terminal console secara lintas OS."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def format_thermal_nota(invoice_data: dict, lebar_kolom: int = 32) -> str:
    """Membuat pemformatan teks struk kasir printer thermal (58mm/80mm).

    Args:
        invoice_data (dict): Data transaksi penjualan dan rincian belanja.
        lebar_kolom (int): Lebar karakter baris nota (default 32 untuk 58mm).

    Returns:
        str: Output teks nota terformat rapi siap cetak.
    """
    # TODO: Implementasi formatting teks struk kasir thermal.
    return ""
