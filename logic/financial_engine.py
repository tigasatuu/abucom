"""
Nama Modul: financial_engine.py
Deskripsi: Logika bisnis depresiasi aset dan pemeriksaan batas pengeluaran (opex).
           (Ref: Module Structure Bab 5.4)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

from collections import namedtuple
from decimal import Decimal

# NamedTuple Definition
DepresiasiResult = namedtuple('DepresiasiResult', ['penyusutan_bulanan', 'akumulasi_penyusutan', 'nilai_buku'])


def hitung_penyusutan_garis_lurus(
    harga_perolehan: Decimal,
    nilai_residu: Decimal,
    masa_manfaat_bulan: int,
    bulan_berjalan: int
) -> DepresiasiResult:
    """Komputasi depresiasi aset tetap bulanan dengan metode garis lurus.

    Args:
        harga_perolehan (Decimal): Biaya pembelian awal aset.
        nilai_residu (Decimal): Estimasi nilai sisa di akhir masa manfaat.
        masa_manfaat_bulan (int): Total durasi manfaat dalam satuan bulan.
        bulan_berjalan (int): Masa bulan penyusutan yang sedang dihitung.

    Returns:
        DepresiasiResult: Rincian hasil depresiasi aset.
    """
    # TODO: Implementasi perhitungan depresiasi garis lurus
    return DepresiasiResult(Decimal('0.00'), Decimal('0.00'), Decimal('0.00'))


def verifikasi_limit_pengeluaran(nominal: Decimal, threshold_limit: Decimal) -> bool:
    """Memvalidasi jika nominal pengeluaran kasir memerlukan eskalasi sandi pemilik.

    Args:
        nominal (Decimal): Jumlah pengeluaran yang diajukan.
        threshold_limit (Decimal): Batas toleransi pengeluaran kasir (contoh: Rp 500.000).

    Returns:
        bool: True jika melebihi batas limit (perlu eskalasi), False jika tidak.
    """
    # TODO: Implementasi pengecekan threshold limit opex
    return False
