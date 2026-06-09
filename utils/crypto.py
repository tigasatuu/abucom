"""
Nama Modul: crypto.py
Deskripsi: Utilitas enkripsi simetris menggunakan Fernet Cryptography.
           Digunakan untuk perlindungan privasi data pelanggan (Nomor WhatsApp)
           memenuhi regulasi UU PDP No. 27/2022.
           (Ref: Security Design Bab 6.1)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""
# WARNING: Jika FERNET_KEY dirotasi, seluruh data whatsapp terenkripsi
# di tabel pelanggan harus di-re-enkripsi menggunakan utilitas migrasi.
# Lihat: Security Design Bab 6.5 — Kebijakan Rotasi Kredensial.

import logging
from cryptography.fernet import Fernet

_logger = logging.getLogger('abucom.utils.crypto')


def encrypt_whatsapp_number(wa_number: str, fernet_key: str) -> str:
    """Mengenkripsi nomor WhatsApp ke dalam format cipher text base64.

    (Ref: Security Design Bab 6.1 — UU PDP No. 27/2022)

    CATATAN: Validasi format nomor WA dilakukan di layer CLI
    (logic/safety_validator.py -> validasi_nomor_whatsapp)
    sebelum memanggil fungsi ini. Fungsi ini hanya bertanggung jawab
    atas operasi kriptografi, bukan validasi bisnis.

    Args:
        wa_number (str): Nomor WhatsApp pelanggan dalam teks polos.
        fernet_key (str): Kunci enkripsi simetris Fernet 32-byte.

    Returns:
        str: Hasil enkripsi berupa string base64 cipher text.
    """
    if not wa_number:
        return ""
    if not fernet_key:
        _logger.warning("Kunci Fernet kosong.")
        return ""
    try:
        f = Fernet(fernet_key.encode('utf-8'))
        encrypted = f.encrypt(wa_number.encode('utf-8'))
        return encrypted.decode('utf-8')
    except Exception as e:
        _logger.error(f"Gagal melakukan enkripsi WhatsApp: {str(e)}")
        return ""


def decrypt_whatsapp_number(encrypted_wa: str, fernet_key: str) -> str:
    """Mendekripsi cipher text base64 kembali ke nomor WhatsApp polos.

    (Ref: Security Design Bab 6.1 — UU PDP No. 27/2022)

    Args:
        encrypted_wa (str): Cipher text base64 dari nomor WhatsApp.
        fernet_key (str): Kunci enkripsi simetris Fernet 32-byte.

    Returns:
        str: Nomor WhatsApp asli dalam teks polos.
    """
    if not encrypted_wa:
        return ""
    if not fernet_key:
        _logger.warning("Kunci Fernet kosong.")
        return ""
    try:
        f = Fernet(fernet_key.encode('utf-8'))
        decrypted = f.decrypt(encrypted_wa.encode('utf-8'))
        return decrypted.decode('utf-8')
    except Exception as e:
        _logger.error(f"Gagal melakukan dekripsi WhatsApp: {str(e)}")
        return ""

