"""
Nama Modul: test_whatsapp_encryption.py
Deskripsi: Unit testing komprehensif untuk fungsionalitas enkripsi dan dekripsi
           nomor WhatsApp pelanggan (utils/crypto.py).
           Memenuhi standar code coverage >= 90%.
"""

import pytest
from cryptography.fernet import Fernet, InvalidToken
from utils.crypto import encrypt_whatsapp_number, decrypt_whatsapp_number


@pytest.fixture
def fernet_key():
    """Fixture untuk menghasilkan Secret Key Fernet acak yang valid per test case."""
    return Fernet.generate_key().decode('utf-8')


# ==============================================================================
# A. SKENARIO POSITIF (Positive Cases)
# ==============================================================================

def test_encrypt_whatsapp_returns_valid_token(fernet_key):
    """Enkripsi: Nomor WhatsApp berformat standar string berhasil diubah menjadi bentuk token Fernet."""
    wa_number = "081234567890"
    encrypted = encrypt_whatsapp_number(wa_number, fernet_key)
    
    assert encrypted != ""
    assert isinstance(encrypted, str)
    # Token Fernet yang valid berupa string base64 dengan panjang minimal tertentu
    assert len(encrypted) > 50


def test_decrypt_token_returns_original_string(fernet_key):
    """Dekripsi: Pemulihan dari token Fernet (ciphertext) valid mengembalikan nilai awal string yang identik."""
    wa_number = "081234567890"
    encrypted = encrypt_whatsapp_number(wa_number, fernet_key)
    
    decrypted = decrypt_whatsapp_number(encrypted, fernet_key)
    assert decrypted == wa_number


def test_encryption_roundtrip_integrity(fernet_key):
    """Integritas Dua Arah: Data dari decrypt(encrypt(data)) == data."""
    wa_number = "6285678901234"
    encrypted = encrypt_whatsapp_number(wa_number, fernet_key)
    decrypted = decrypt_whatsapp_number(encrypted, fernet_key)
    assert decrypted == wa_number


# ==============================================================================
# B. SKENARIO NEGATIF & EDGE CASES (Negative/Edge Cases)
# ==============================================================================

def test_decrypt_invalid_token_returns_empty_string(fernet_key):
    """Invalid Token: Wrapper dekripsi terhadap token yang rusak/manipulasi mengembalikan string kosong."""
    # Korupsi token Fernet asal-asalan
    invalid_token = "bukan_token_fernet_yang_valid"
    decrypted = decrypt_whatsapp_number(invalid_token, fernet_key)
    assert decrypted == ""


def test_decrypt_tampered_token_raises_invalid_token_directly(fernet_key):
    """Invalid Token: Direct Fernet decrypt melempar InvalidToken jika token rusak/manipulasi."""
    wa_number = "081234567890"
    encrypted = encrypt_whatsapp_number(wa_number, fernet_key)
    
    # Manipulasi ciphertext di tengah
    tampered = encrypted[:20] + "XYZ" + encrypted[23:]
    
    # 1. Wrapper harus menangani dengan aman (mengembalikan "")
    assert decrypt_whatsapp_number(tampered, fernet_key) == ""
    
    # 2. Pustaka cryptography melempar InvalidToken jika dipanggil langsung
    with pytest.raises(InvalidToken):
        f = Fernet(fernet_key.encode('utf-8'))
        f.decrypt(tampered.encode('utf-8'))


def test_decrypt_with_wrong_key(fernet_key):
    """Wrong Key: Dekripsi menggunakan kunci berbeda mengembalikan "" pada wrapper dan raise InvalidToken langsung."""
    wa_number = "081234567890"
    encrypted = encrypt_whatsapp_number(wa_number, fernet_key)
    
    # Hasilkan kunci lain
    wrong_key = Fernet.generate_key().decode('utf-8')
    
    # 1. Wrapper
    decrypted = decrypt_whatsapp_number(encrypted, wrong_key)
    assert decrypted == ""
    
    # 2. Direct cryptography
    with pytest.raises(InvalidToken):
        f = Fernet(wrong_key.encode('utf-8'))
        f.decrypt(encrypted.encode('utf-8'))


def test_encrypt_decrypt_empty_string(fernet_key):
    """Empty String: Enkripsi pada string kosong menghasilkan ""."""
    encrypted = encrypt_whatsapp_number("", fernet_key)
    assert encrypted == ""
    
    decrypted = decrypt_whatsapp_number("", fernet_key)
    assert decrypted == ""


def test_boundary_length_short_and_long(fernet_key):
    """Boundary Length: Uji nomor WA yang sangat pendek ("123") dan panjang absurd (1000+ karakter)."""
    # Pendek
    wa_short = "123"
    enc_short = encrypt_whatsapp_number(wa_short, fernet_key)
    assert enc_short != ""
    assert decrypt_whatsapp_number(enc_short, fernet_key) == wa_short
    
    # Panjang absurd
    wa_long = "9" * 1500
    enc_long = encrypt_whatsapp_number(wa_long, fernet_key)
    assert enc_long != ""
    assert decrypt_whatsapp_number(enc_long, fernet_key) == wa_long


# ==============================================================================
# C. SKENARIO VALIDASI INPUT (Input Validation)
# ==============================================================================

def test_input_non_string_handled_gracefully(fernet_key):
    """Input bukan string: Parameter berupa int, list, atau dict ditangani dengan aman tanpa crash."""
    # Integer
    assert encrypt_whatsapp_number(1234567890, fernet_key) == ""
    assert decrypt_whatsapp_number(1234567890, fernet_key) == ""
    
    # List
    assert encrypt_whatsapp_number(["0812345"], fernet_key) == ""
    assert decrypt_whatsapp_number(["encrypted"], fernet_key) == ""

    # Dict
    assert encrypt_whatsapp_number({"wa": "0812"}, fernet_key) == ""
    assert decrypt_whatsapp_number({"wa": "enc"}, fernet_key) == ""


def test_input_none_handled_gracefully(fernet_key):
    """Input Null/NoneType: Parameter None ditangani dengan mengembalikan string kosong."""
    assert encrypt_whatsapp_number(None, fernet_key) == ""
    assert decrypt_whatsapp_number(None, fernet_key) == ""
    
    assert encrypt_whatsapp_number("081234567890", None) == ""
    assert decrypt_whatsapp_number("encrypted_token", None) == ""


def test_input_illegal_characters_retains_integrity(fernet_key):
    """Input karakter ilegal: Karakter spesial atau simbol berhasil dienkripsi dan didekripsi kembali utuh."""
    wa_special = "+62-812(345)678-90!@#$%"
    encrypted = encrypt_whatsapp_number(wa_special, fernet_key)
    assert encrypted != ""
    assert decrypt_whatsapp_number(encrypted, fernet_key) == wa_special
