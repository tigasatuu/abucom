"""
Nama Modul: test_crm_validator.py
Deskripsi: Unit testing deterministik untuk validasi input CRM pelanggan.
"""

import pytest
from logic.safety_validator import validasi_nomor_whatsapp, validasi_nama_pelanggan


def test_validasi_wa_format_valid():
    """Input '6285678901234' harus valid."""
    res = validasi_nomor_whatsapp("6285678901234")
    assert res.is_valid is True
    assert res.sanitized_data == "6285678901234"
    assert res.error_msg is None


def test_validasi_wa_konversi_lokal():
    """Input '085678901234' harus dikonversi ke '6285678901234' dan valid."""
    res = validasi_nomor_whatsapp("085678901234")
    assert res.is_valid is True
    assert res.sanitized_data == "6285678901234"
    assert res.error_msg is None


def test_validasi_wa_format_plus62():
    """Input '+6285678901234' harus dikonversi ke '6285678901234' dan valid."""
    res = validasi_nomor_whatsapp("+6285678901234")
    assert res.is_valid is True
    assert res.sanitized_data == "6285678901234"
    assert res.error_msg is None


def test_validasi_wa_terlahu_pendek():
    """Input '62856' terlalu pendek dan harus invalid."""
    res = validasi_nomor_whatsapp("62856")
    assert res.is_valid is False
    assert "ERR-VAL-036" in res.error_msg


def test_validasi_wa_non_numerik():
    """Input dengan karakter non-numerik harus invalid."""
    res = validasi_nomor_whatsapp("628abcdefgh")
    assert res.is_valid is False
    assert "ERR-VAL-036" in res.error_msg


def test_validasi_wa_tidak_diawali_628():
    """Input yang tidak diawali '628' / '08' harus invalid."""
    res = validasi_nomor_whatsapp("6275678901234")
    assert res.is_valid is False
    assert "ERR-VAL-036" in res.error_msg


def test_validasi_nama_valid():
    """Input nama valid harus dikembalikan dalam title case."""
    res = validasi_nama_pelanggan("roni wijaya")
    assert res.is_valid is True
    assert res.sanitized_data == "Roni Wijaya"
    assert res.error_msg is None


def test_validasi_nama_terlalu_pendek():
    """Input nama 1 karakter harus invalid."""
    res = validasi_nama_pelanggan("R")
    assert res.is_valid is False
    assert "ERR-VAL-036" in res.error_msg


def test_validasi_nama_mengandung_angka():
    """Input nama yang mengandung angka harus invalid."""
    res = validasi_nama_pelanggan("Roni123")
    assert res.is_valid is False
    assert "ERR-VAL-036" in res.error_msg


def test_validasi_nama_strip_whitespace():
    """Input nama dengan leading/trailing spaces harus dibersihkan."""
    res = validasi_nama_pelanggan("  roni wijaya  ")
    assert res.is_valid is True
    assert res.sanitized_data == "Roni Wijaya"
    assert res.error_msg is None
