"""
Nama Modul: test_financial_engine.py
Deskripsi: Unit testing untuk fungsi hitung_laba_bersih_harian
           pada logic/financial_engine.py.
Author: Antigravity
Tanggal: 2026-06-07
"""

from decimal import Decimal
from logic.financial_engine import hitung_laba_bersih_harian


def test_hitung_laba_bersih_harian_untung() -> None:
    """Memverifikasi perhitungan laba bersih harian yang menghasilkan keuntungan."""
    pendapatan = Decimal('1000000.0000')
    pengeluaran = Decimal('400000.0000')
    limbah = Decimal('50000.0000')
    
    laba = hitung_laba_bersih_harian(pendapatan, pengeluaran, limbah)
    assert laba == Decimal('550000.0000')


def test_hitung_laba_bersih_harian_rugi() -> None:
    """Memverifikasi perhitungan laba bersih harian yang menghasilkan kerugian."""
    pendapatan = Decimal('200000.0000')
    pengeluaran = Decimal('300000.0000')
    limbah = Decimal('50000.0000')
    
    laba = hitung_laba_bersih_harian(pendapatan, pengeluaran, limbah)
    assert laba == Decimal('-150000.0000')


def test_hitung_laba_bersih_harian_presisi_dan_rounding() -> None:
    """Memverifikasi penanganan presisi desimal dan pembulatan ROUND_HALF_UP."""
    pendapatan = Decimal('100.00005')
    pengeluaran = Decimal('50.00000')
    limbah = Decimal('10.00000')
    
    # (100.00005 - 50 - 10) = 40.00005. Rounded HAF_UP with 4 decimal places -> 40.0001
    laba = hitung_laba_bersih_harian(pendapatan, pengeluaran, limbah)
    assert laba == Decimal('40.0001')
