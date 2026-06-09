"""
Nama Modul: test_crm_crypto.py
Deskripsi: Unit testing deterministik untuk fungsi enkripsi/dekripsi WhatsApp CRM.
"""

import pytest
from cryptography.fernet import Fernet
from utils.crypto import encrypt_whatsapp_number, decrypt_whatsapp_number


def test_encrypt_decrypt_roundtrip():
    """Menguji enkripsi lalu dekripsi mengembalikan nilai asli."""
    key = Fernet.generate_key().decode('utf-8')
    wa_original = "6285678901234"
    
    encrypted = encrypt_whatsapp_number(wa_original, key)
    assert encrypted != wa_original
    assert len(encrypted) == 100
    
    decrypted = decrypt_whatsapp_number(encrypted, key)
    assert decrypted == wa_original


def test_encrypt_produces_different_output():
    """Menguji enkripsi nomor yang sama dua kali menghasilkan ciphertext yang berbeda."""
    key = Fernet.generate_key().decode('utf-8')
    wa = "6285678901234"
    
    enc1 = encrypt_whatsapp_number(wa, key)
    enc2 = encrypt_whatsapp_number(wa, key)
    
    assert enc1 != enc2  # Fernet menggunakan timestamp + IV acak
    assert len(enc1) == 100
    assert len(enc2) == 100


def test_decrypt_with_wrong_key():
    """Menguji dekripsi dengan kunci yang salah mengembalikan string kosong."""
    key1 = Fernet.generate_key().decode('utf-8')
    key2 = Fernet.generate_key().decode('utf-8')
    wa = "6285678901234"
    
    enc = encrypt_whatsapp_number(wa, key1)
    dec = decrypt_whatsapp_number(enc, key2)
    
    assert dec == ""


def test_encrypt_empty_string():
    """Menguji penanganan input string kosong."""
    key = Fernet.generate_key().decode('utf-8')
    assert encrypt_whatsapp_number("", key) == ""
    assert decrypt_whatsapp_number("", key) == ""


def test_encrypt_with_empty_key():
    """Menguji penanganan kunci Fernet kosong."""
    assert encrypt_whatsapp_number("6285678901234", "") == ""
    assert decrypt_whatsapp_number("kG6WfB1d_2fGzKx1W3UvM2T5P7R9S1Y_V4X_Z8A0B2C=", "") == ""


def test_encrypt_with_invalid_key_format():
    """Menguji format kunci Fernet tidak valid."""
    assert encrypt_whatsapp_number("6285678901234", "kunci_tidak_valid_32_bytes_bukan_base64!!!") == ""
    assert decrypt_whatsapp_number("some_encrypted_data", "kunci_tidak_valid_32_bytes_bukan_base64!!!") == ""


def test_encrypt_whatsapp_number_long():
    """Menguji nomor WA yang panjang (batas 20 karakter)."""
    key = Fernet.generate_key().decode('utf-8')
    wa_long = "12345678901234567890"  # 20 chars
    encrypted = encrypt_whatsapp_number(wa_long, key)
    assert encrypted != ""
    assert decrypt_whatsapp_number(encrypted, key) == wa_long


def test_encrypt_whatsapp_number_non_numeric():
    """Menguji enkripsi dengan karakter non-numerik (crypto layer harus tetap mengenkripsi)."""
    key = Fernet.generate_key().decode('utf-8')
    wa_non_num = "abc-1234_xyz!"
    encrypted = encrypt_whatsapp_number(wa_non_num, key)
    assert encrypted != ""
    assert decrypt_whatsapp_number(encrypted, key) == wa_non_num


def test_decrypt_corrupted_ciphertext():
    """Menguji dekripsi ciphertext yang rusak agar mengembalikan string kosong secara aman."""
    key = Fernet.generate_key().decode('utf-8')
    wa = "6285678901234"
    encrypted = encrypt_whatsapp_number(wa, key)
    
    # Korupsi ciphertext dengan mengganti beberapa karakter di tengah
    corrupted = encrypted[:20] + "xyz" + encrypted[23:]
    assert decrypt_whatsapp_number(corrupted, key) == ""


def test_encrypt_decrypt_multiple_roundtrips():
    """Menguji reliabilitas roundtrip dengan 100 nomor acak yang berbeda."""
    key = Fernet.generate_key().decode('utf-8')
    for i in range(100):
        wa = f"62856789{i:05d}"
        encrypted = encrypt_whatsapp_number(wa, key)
        assert encrypted != ""
        assert decrypt_whatsapp_number(encrypted, key) == wa
