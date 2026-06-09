"""
Nama Modul: test_crm_encryption.py
Deskripsi: Unit testing komprehensif untuk fitur kelola database pelanggan CRM terenkripsi.
           Memenuhi seluruh kriteria SDLC dan Bab 5.7/5.8 perlindungan data pribadi (UU PDP).
"""

import os
import re
import pytest
from unittest.mock import MagicMock, patch
from cryptography.fernet import Fernet, InvalidToken

from logic.safety_validator import validasi_nomor_whatsapp
from utils.crypto import encrypt_whatsapp_number, decrypt_whatsapp_number
from db.query_builder import insert_pelanggan_baru, query_delete_pelanggan, cari_pelanggan_by_whatsapp


@pytest.fixture
def dummy_fernet_key():
    """Fixture untuk menghasilkan kunci Fernet dummy statis yang valid."""
    return Fernet.generate_key().decode('utf-8')


@pytest.fixture
def clean_mock_env():
    """Fixture untuk me-reset state mock DB dan os.environ sebelum setiap test case."""
    old_environ = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(old_environ)


# ==============================================================================
# A. SKENARIO VALIDASI & SANITASI INPUT (WHATSAPP INDONESIA)
# ==============================================================================

def test_validate_whatsapp_format_valid():
    """Memastikan format nomor WhatsApp Indonesia yang valid berhasil disanitasi."""
    # Kasus 1: Format standar 628...
    res1 = validasi_nomor_whatsapp("6285678901234")
    assert res1.is_valid is True
    assert res1.sanitized_data == "6285678901234"
    assert res1.error_msg is None

    # Kasus 2: Format lokal 08... dikonversi ke 628...
    res2 = validasi_nomor_whatsapp("085678901234")
    assert res2.is_valid is True
    assert res2.sanitized_data == "6285678901234"

    # Kasus 3: Format internasional +628... dikonversi ke 628...
    res3 = validasi_nomor_whatsapp("+6285678901234")
    assert res3.is_valid is True
    assert res3.sanitized_data == "6285678901234"

    # Kasus 4: Format dengan spasi dan strip (-) berhasil dibersihkan
    res4 = validasi_nomor_whatsapp(" 0856 - 7890 - 1234 ")
    assert res4.is_valid is True
    assert res4.sanitized_data == "6285678901234"


def test_validate_whatsapp_format_invalid_length():
    """Memastikan penolakan terhadap nomor WhatsApp yang terlalu pendek atau terlalu panjang."""
    def validate_or_raise(num):
        res = validasi_nomor_whatsapp(num)
        if not res.is_valid:
            raise ValueError(res.error_msg)
        return res.sanitized_data

    # Kasus valid untuk coverage return statement
    assert validate_or_raise("085678901234") == "6285678901234"

    # Kasus 1: Terlaju pendek (< 10 digit)
    with pytest.raises(ValueError) as excinfo:
        validate_or_raise("62856")
    assert "ERR-VAL-036" in str(excinfo.value)

    # Kasus 2: Terlalu panjang (> 14 digit)
    with pytest.raises(ValueError) as excinfo:
        validate_or_raise("6285678901234567")
    assert "ERR-VAL-036" in str(excinfo.value)


def test_validate_whatsapp_format_invalid_chars():
    """Memastikan penolakan terhadap nomor WhatsApp yang mengandung karakter non-numerik selain '+'."""
    def validate_or_raise(num):
        res = validasi_nomor_whatsapp(num)
        if not res.is_valid:
            raise ValueError(res.error_msg)
        return res.sanitized_data

    # Kasus valid untuk coverage return statement
    assert validate_or_raise("085678901234") == "6285678901234"

    # Kasus 1: Mengandung karakter alfabet
    with pytest.raises(ValueError) as excinfo:
        validate_or_raise("62856abc1234")
    assert "ERR-VAL-036" in str(excinfo.value)

    # Kasus 2: None / Tipe data non-string
    with pytest.raises(ValueError) as excinfo:
        validate_or_raise(None)
    assert "ERR-VAL-036" in str(excinfo.value)


# ==============================================================================
# B. SKENARIO ENKRIPSI & DEKRIPSI (FERNET)
# ==============================================================================

def test_fernet_encryption_process(dummy_fernet_key):
    """Memastikan proses enkripsi mengubah nomor WhatsApp menjadi ciphertext yang berbeda."""
    wa_plaintext = "6285678901234"
    ciphertext = encrypt_whatsapp_number(wa_plaintext, dummy_fernet_key)
    
    assert ciphertext != ""
    assert ciphertext != wa_plaintext
    # Ciphertext Fernet biasanya berupa string base64 dengan panjang minimal tertentu
    assert len(ciphertext) > 50


def test_fernet_decryption_process(dummy_fernet_key):
    """Memastikan proses dekripsi mengembalikan ciphertext menjadi plaintext semula."""
    wa_plaintext = "6285678901234"
    ciphertext = encrypt_whatsapp_number(wa_plaintext, dummy_fernet_key)
    
    decrypted = decrypt_whatsapp_number(ciphertext, dummy_fernet_key)
    assert decrypted == wa_plaintext


def test_fernet_decryption_invalid_key_fails(dummy_fernet_key):
    """Memastikan dekripsi gagal dan menimbulkan InvalidToken jika kunci Fernet salah."""
    wa_plaintext = "6285678901234"
    ciphertext = encrypt_whatsapp_number(wa_plaintext, dummy_fernet_key)
    
    # Generate kunci lain yang berbeda
    wrong_key = Fernet.generate_key().decode('utf-8')
    
    # 1. Pastikan utilitas wrapper kita mengembalikan string kosong saat dekripsi gagal
    decrypted_via_wrapper = decrypt_whatsapp_number(ciphertext, wrong_key)
    assert decrypted_via_wrapper == ""
    
    # 2. Pastikan pustaka cryptography menaikkan InvalidToken jika dipanggil langsung
    with pytest.raises(InvalidToken):
        f = Fernet(wrong_key.encode('utf-8'))
        f.decrypt(ciphertext.encode('utf-8'))


# ==============================================================================
# C. SKENARIO ISOLASI DATABASE & PENGHAPUSAN PERMANEN (UU PDP)
# ==============================================================================

def test_register_customer_saves_encrypted_data(clean_mock_env, dummy_fernet_key):
    """Memverifikasi bahwa proses registrasi menyimpan nomor WhatsApp terenkripsi ke database."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_cursor.lastrowid = 100
    
    wa_plaintext = "6285678901234"
    wa_encrypted = encrypt_whatsapp_number(wa_plaintext, dummy_fernet_key)
    
    res = insert_pelanggan_baru(mock_conn, "Roni Wijaya", wa_encrypted, cabang_id=1)
    
    assert res.is_success is True
    assert res.data == 100
    assert res.error_msg is None
    
    # Pastikan query insert memanggil parameter yang berisi ciphertext, bukan plaintext
    mock_cursor.execute.assert_called_once()
    args, _ = mock_cursor.execute.call_args
    query, params = args
    
    assert "INSERT INTO pelanggan" in query
    assert "Roni Wijaya" in params
    assert wa_encrypted in params
    assert wa_plaintext not in params


def test_delete_customer_performs_hard_delete(clean_mock_env):
    """Memastikan penghapusan keanggotaan pelanggan memicu kueri DELETE secara fisik (hard-delete)."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.rowcount = 1
    
    res = query_delete_pelanggan(mock_conn, pelanggan_id=5, cabang_id=1)
    
    assert res.is_success is True
    assert res.data == 1
    assert res.error_msg is None
    
    # Pastikan kueri SQL menggunakan DELETE FROM (hard-delete), bukan UPDATE (soft-delete)
    mock_cursor.execute.assert_called_once()
    args, _ = mock_cursor.execute.call_args
    query, params = args
    
    assert "DELETE FROM pelanggan" in query
    assert "UPDATE" not in query
    assert params == (5, 1)


def test_delete_customer_not_found(clean_mock_env):
    """Memastikan fungsi hard-delete menangani kasus dengan aman jika ID pelanggan tidak ditemukan."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.rowcount = 0  # 0 baris terpengaruh
    
    res = query_delete_pelanggan(mock_conn, pelanggan_id=999, cabang_id=1)
    
    assert res.is_success is True
    assert res.data == 0
    assert res.error_msg is None


def test_cari_pelanggan_by_whatsapp_in_memory_match(dummy_fernet_key):
    """Memverifikasi pencarian in-memory matching pada cari_pelanggan_by_whatsapp."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    wa_plain = "6285678901234"
    wa_encrypted = encrypt_whatsapp_number(wa_plain, dummy_fernet_key)
    
    # Mock data returned by cursor.fetchall()
    wa_encrypted_db = encrypt_whatsapp_number(wa_plain, dummy_fernet_key)
    mock_cursor.fetchall.return_value = [
        {"id": 1, "nama_pelanggan": "Lain", "whatsapp": "some_other_encrypted", "tanggal_terdaftar": "2026-06-01"},
        {"id": 2, "nama_pelanggan": "Roni", "whatsapp": wa_encrypted_db, "tanggal_terdaftar": "2026-06-02"},
    ]
    
    # Test dengan kunci yang benar
    res = cari_pelanggan_by_whatsapp(mock_conn, wa_encrypted, cabang_id=1, fernet_key=dummy_fernet_key)
    assert res.is_success is True
    assert res.data is not None
    assert res.data["id"] == 2
    assert res.data["nama_pelanggan"] == "Roni"
    
    # Test dengan kunci yang salah (harus gagal mencocokkan)
    wrong_key = Fernet.generate_key().decode('utf-8')
    res_wrong = cari_pelanggan_by_whatsapp(mock_conn, wa_encrypted, cabang_id=1, fernet_key=wrong_key)
    assert res_wrong.is_success is True
    assert res_wrong.data is None


@patch('cli.menu_transaksi.query_delete_pelanggan')
@patch('cli.menu_transaksi.log_audit_trail')
@patch('cli.menu_transaksi.get_db_connection')
@patch('cli.menu_transaksi.execute_query')
def test_delete_customer_audit_log(mock_execute_query, mock_get_db_connection, mock_log_audit_trail, mock_query_delete_pelanggan, clean_mock_env, dummy_fernet_key):
    """Memverifikasi bahwa proses penghapusan pelanggan memicu log audit dengan format yang benar."""
    from cli.menu_transaksi import _form_hapus_pelanggan
    
    mock_conn = MagicMock()
    mock_get_db_connection.return_value.is_success = True
    mock_get_db_connection.return_value.data = mock_conn
    
    # Mock finding the customer
    mock_execute_query.return_value.is_success = True
    mock_execute_query.return_value.data = {
        "id": 5,
        "nama_pelanggan": "Roni",
        "whatsapp": encrypt_whatsapp_number("6285678901234", dummy_fernet_key),
        "tanggal_terdaftar": "2026-06-02"
    }
    
    # Mock deletion success
    mock_query_delete_pelanggan.return_value.is_success = True
    mock_query_delete_pelanggan.return_value.data = 1
    
    # Mock load_settings
    with patch('cli.menu_transaksi.load_settings') as mock_load_settings:
        mock_settings = MagicMock()
        mock_settings.fernet_key = dummy_fernet_key
        mock_load_settings.return_value = mock_settings
        
        # Mock inputs: ID, dan konfirmasi 'y'
        with patch('builtins.input', side_effect=["5", "y", ""]) as mock_input:
            session_state = {"role": "pemilik", "cabang_id": 1, "user_id": 10}
            _form_hapus_pelanggan(session_state)
            
            # Verify deletion called
            mock_query_delete_pelanggan.assert_called_once_with(mock_conn, 5, 1)
            
            # Verify log_audit_trail called
            mock_log_audit_trail.assert_called_once()
            _, kwargs = mock_log_audit_trail.call_args
            assert kwargs['pengguna_id'] == 10
            assert kwargs['action_type'] == 'DELETE'
            assert kwargs['target_table'] == 'pelanggan'
            assert kwargs['old_val']['nama_pelanggan'] == 'Roni'
            assert kwargs['old_val']['whatsapp'] == '[ENCRYPTED]'
            assert kwargs['new_val'] is None
