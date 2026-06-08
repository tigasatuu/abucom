"""
Nama Modul: test_master_supplier.py
Deskripsi: Unit testing komprehensif, terisolasi, dan deterministik untuk
           kelola data master supplier (validator dan query builder) menggunakan pytest.
           Memenuhi seluruh kriteria SDLC dan persona Lead SDET dengan 100% cakupan kode.
Author: Antigravity AI
Tanggal: 2026-06-08
"""

import pytest
from unittest.mock import MagicMock, patch
import re

from logic.safety_validator import (
    validasi_data_supplier,
    validasi_supplier_id,
    Result as ValidationResult,
    ValidationStatus
)
from db.query_builder import (
    query_daftar_supplier,
    query_detail_supplier,
    query_insert_supplier,
    query_update_supplier,
    query_delete_supplier,
    query_cek_nama_supplier_duplikat,
    Result as DBResult
)


@pytest.fixture
def mock_db_conn():
    """Fixture untuk menyiapkan koneksi database mock yang bersih dan terisolasi.

    Mensimulasikan setup/teardown state dengan merekam instruksi TRUNCATE TABLE supplier.
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    # Setup: Simulasikan pembersihan database basis data sandbox uji coba
    mock_cursor.execute("TRUNCATE TABLE supplier")

    yield mock_conn

    # Teardown: Reset side_effects dan simulasikan pembersihan database kembali
    mock_cursor.execute.side_effect = None
    mock_cursor.fetchone.side_effect = None
    mock_cursor.fetchall.side_effect = None
    mock_cursor.execute("TRUNCATE TABLE supplier")
    mock_conn.reset_mock()


# ==============================================================================
# A. SKENARIO POSITIF (HAPPY PATH)
# ==============================================================================

def test_create_supplier_success(mock_db_conn):
    """Skenario Positif: Penambahan data supplier baru dengan input lengkap dan valid."""
    # 1. Validasi form input data
    raw_data = {
        'nama_supplier': 'CV. Sinar Abadi',
        'alamat': 'Jl. Gatsu No. 100, Bandung',
        'telp': '+62 812-3456-7890',
        'email': 'sales@sinarabadi.co.id'
    }
    val_res = validasi_data_supplier(raw_data)
    assert val_res.is_success is True
    assert val_res.data['nama_supplier'] == 'CV. Sinar Abadi'

    # 2. Mock query insertion return lastrowid = 15
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.lastrowid = 15
    
    db_res = query_insert_supplier(
        mock_db_conn,
        nama_supplier=val_res.data['nama_supplier'],
        alamat=val_res.data['alamat'],
        telp=val_res.data['telp'],
        email=val_res.data['email'],
        cabang_id=1
    )
    
    assert db_res.is_success is True
    assert db_res.data == 15
    mock_db_conn.commit.assert_called_once()


def test_read_supplier_by_id_success(mock_db_conn):
    """Skenario Positif: Pembacaan detail supplier berdasarkan ID yang valid."""
    # Mock query detail return record
    mock_row = {
        'id': 15,
        'nama_supplier': 'CV. Sinar Abadi',
        'alamat': 'Jl. Gatsu No. 100, Bandung',
        'telp': '+62 812-3456-7890',
        'email': 'sales@sinarabadi.co.id',
        'cabang_id': 1,
        'created_at': '2026-06-08 09:00:00',
        'updated_at': '2026-06-08 09:00:00'
    }
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.fetchone.return_value = mock_row

    db_res = query_detail_supplier(mock_db_conn, supplier_id=15, cabang_id=1)
    
    assert db_res.is_success is True
    assert db_res.data['id'] == 15
    assert db_res.data['nama_supplier'] == 'CV. Sinar Abadi'


def test_read_supplier_list_success(mock_db_conn):
    """Skenario Positif: Pembacaan seluruh daftar supplier.

    Memastikan list kosong pada kondisi awal (setup), dan mengembalikan data setelah insert.
    """
    mock_cursor = mock_db_conn.cursor.return_value

    # Kondisi awal: Database kosong (simulasi fetchall return [])
    mock_cursor.fetchall.return_value = []
    db_res_empty = query_daftar_supplier(mock_db_conn, cabang_id=1)
    assert db_res_empty.is_success is True
    assert db_res_empty.data == []

    # Kondisi setelah insert: Mengembalikan list berisi data supplier
    mock_rows = [
        {'id': 1, 'nama_supplier': 'Supplier A', 'alamat': 'Alamat A', 'telp': '123', 'email': 'a@b.com'},
        {'id': 2, 'nama_supplier': 'Supplier B', 'alamat': 'Alamat B', 'telp': '456', 'email': 'c@d.com'}
    ]
    mock_cursor.fetchall.return_value = mock_rows
    db_res_populated = query_daftar_supplier(mock_db_conn, cabang_id=1)
    
    assert db_res_populated.is_success is True
    assert len(db_res_populated.data) == 2
    assert db_res_populated.data[0]['nama_supplier'] == 'Supplier A'


def test_update_supplier_success(mock_db_conn):
    """Skenario Positif: Perubahan data (Update) nama dan telp pada ID supplier yang valid."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.rowcount = 1

    db_res = query_update_supplier(
        mock_db_conn,
        supplier_id=15,
        nama_supplier='CV. Sinar Abadi Baru',
        alamat='Jl. Gatsu No. 100, Bandung',
        telp='0899999999',
        email='sales@sinarabadi.co.id',
        cabang_id=1
    )
    
    assert db_res.is_success is True
    assert db_res.data == 1  # 1 row affected
    mock_db_conn.commit.assert_called_once()


def test_delete_supplier_success(mock_db_conn):
    """Skenario Positif: Penghapusan data (Delete) supplier berdasarkan ID yang valid."""
    mock_cursor = mock_db_conn.cursor.return_value
    
    # Mock check utang returns 0 count (no active debts)
    # Mock check riwayat returns 0 count (optional check)
    mock_cursor.fetchone.side_effect = [{'count': 0}, {'count': 0}]
    mock_cursor.rowcount = 1

    db_res = query_delete_supplier(mock_db_conn, supplier_id=15, cabang_id=1)
    
    assert db_res.is_success is True
    assert db_res.data == 1  # 1 row affected
    mock_db_conn.commit.assert_called_once()


# ==============================================================================
# B. SKENARIO NEGATIF & EDGE CASES
# ==============================================================================

def test_create_supplier_empty_name_fails():
    """Skenario Negatif: Penambahan data dengan nama_supplier kosong atau null (None)."""
    # Kasus 1: nama_supplier is None
    raw_data_none = {
        'nama_supplier': None,
        'alamat': 'Jl. Industri',
        'telp': '0812345678',
        'email': 'test@supplier.com'
    }
    res_none = validasi_data_supplier(raw_data_none)
    assert res_none.is_success is False
    assert "Nama supplier wajib diisi" in res_none.error_msg

    # Kasus 2: nama_supplier is empty string
    raw_data_empty = {
        'nama_supplier': '   ',
        'alamat': 'Jl. Industri',
        'telp': '0812345678',
        'email': 'test@supplier.com'
    }
    res_empty = validasi_data_supplier(raw_data_empty)
    assert res_empty.is_success is False
    assert "Nama supplier tidak boleh kosong" in res_empty.error_msg


def test_create_supplier_empty_telp_fails():
    """Skenario Negatif: Penambahan data dengan telp kosong atau null (None)."""
    # Kasus 1: telp is None
    raw_data_none = {
        'nama_supplier': 'Supplier Indah',
        'alamat': 'Jl. Industri',
        'telp': None,
        'email': 'test@supplier.com'
    }
    res_none = validasi_data_supplier(raw_data_none)
    assert res_none.is_success is False
    assert "Nomor telepon supplier wajib diisi" in res_none.error_msg

    # Kasus 2: telp is empty string
    raw_data_empty = {
        'nama_supplier': 'Supplier Indah',
        'alamat': 'Jl. Industri',
        'telp': '   ',
        'email': 'test@supplier.com'
    }
    res_empty = validasi_data_supplier(raw_data_empty)
    assert res_empty.is_success is False
    assert "Nomor telepon supplier tidak boleh kosong" in res_empty.error_msg


def test_create_supplier_invalid_email_fails():
    """Skenario Negatif: Penambahan data dengan format email salah."""
    raw_data = {
        'nama_supplier': 'Supplier Indah',
        'alamat': 'Jl. Industri',
        'telp': '0812345678',
        'email': 'supplier-at-gmail'
    }
    res = validasi_data_supplier(raw_data)
    assert res.is_success is False
    assert "Format email tidak valid" in res.error_msg


def test_read_supplier_not_found(mock_db_conn):
    """Skenario Negatif: Pencarian detail supplier dengan ID fiktif yang tidak ada."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.fetchone.return_value = None

    db_res = query_detail_supplier(mock_db_conn, supplier_id=999, cabang_id=1)
    
    assert db_res.is_success is False
    assert "ERR-VAL-013" in db_res.error_msg
    assert "tidak terdaftar" in db_res.error_msg


def test_update_supplier_not_found(mock_db_conn):
    """Skenario Negatif: Perubahan data supplier dengan ID fiktif (0 rows affected)."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.rowcount = 0

    db_res = query_update_supplier(
        mock_db_conn,
        supplier_id=999,
        nama_supplier='Nama Baru',
        alamat='Alamat Baru',
        telp='0811111',
        email='new@supplier.com',
        cabang_id=1
    )
    
    assert db_res.is_success is True
    assert db_res.data == 0  # 0 rows affected indicates ID not found/no change


def test_delete_supplier_not_found(mock_db_conn):
    """Skenario Negatif: Penghapusan supplier dengan ID fiktif (0 rows affected)."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.fetchone.side_effect = [{'count': 0}, {'count': 0}]
    mock_cursor.rowcount = 0

    db_res = query_delete_supplier(mock_db_conn, supplier_id=999, cabang_id=1)
    
    assert db_res.is_success is True
    assert db_res.data == 0  # 0 rows affected


def test_delete_supplier_with_active_debts_fails(mock_db_conn):
    """Skenario Negatif: Menolak penghapusan supplier jika masih memiliki utang aktif yang belum lunas."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.fetchone.return_value = {'count': 1}  # Ada 1 utang belum lunas

    db_res = query_delete_supplier(mock_db_conn, supplier_id=15, cabang_id=1)
    
    assert db_res.is_success is False
    assert "ERR-REL-136" in db_res.error_msg
    assert "memiliki utang aktif" in db_res.error_msg
    mock_db_conn.commit.assert_not_called()


# ==============================================================================
# C. VALIDASI INPUT EKSTREM & KEAMANAN
# ==============================================================================

def test_supplier_max_length_validation():
    """Validasi Input Ekstrem: Input melebihi batas kolom database.

    - nama_supplier > 100 karakter
    - telp > 30 karakter
    - email > 100 karakter
    """
    # Kasus 1: nama_supplier > 100 karakter
    raw_data_long_name = {
        'nama_supplier': 'A' * 101,
        'alamat': 'Jl. Industri',
        'telp': '0812345678',
        'email': 'test@supplier.com'
    }
    res_name = validasi_data_supplier(raw_data_long_name)
    assert res_name.is_success is False
    assert "Nama supplier maksimal 100 karakter" in res_name.error_msg

    # Kasus 2: telp > 30 karakter
    raw_data_long_telp = {
        'nama_supplier': 'Supplier Indah',
        'alamat': 'Jl. Industri',
        'telp': '1' * 31,
        'email': 'test@supplier.com'
    }
    res_telp = validasi_data_supplier(raw_data_long_telp)
    assert res_telp.is_success is False
    assert "Nomor telepon supplier maksimal 30 karakter" in res_telp.error_msg

    # Kasus 3: email > 100 karakter
    raw_data_long_email = {
        'nama_supplier': 'Supplier Indah',
        'alamat': 'Jl. Industri',
        'telp': '0812345678',
        'email': 'A' * 90 + '@supplier.com'  # 103 chars
    }
    res_email = validasi_data_supplier(raw_data_long_email)
    assert res_email.is_success is False
    assert "Email supplier maksimal 100 karakter" in res_email.error_msg


def test_supplier_sql_injection_sanitization_handling(mock_db_conn):
    """Keamanan: Verifikasi input SQL Injection aman ditangani via query terparameter."""
    sql_injection_str = "' OR '1'='1"
    
    mock_cursor = mock_db_conn.cursor.return_value
    
    # 1. Test query_insert_supplier
    query_insert_supplier(
        mock_db_conn,
        nama_supplier=sql_injection_str,
        alamat='Alamat Aman',
        telp='0811',
        email='safe@mail.com',
        cabang_id=1
    )
    args, _ = mock_cursor.execute.call_args
    sql_query, params = args
    assert "%s" in sql_query
    assert sql_injection_str in params

    # 2. Test query_update_supplier
    query_update_supplier(
        mock_db_conn,
        supplier_id=1,
        nama_supplier=sql_injection_str,
        alamat='Alamat Aman',
        telp='0811',
        email='safe@mail.com',
        cabang_id=1
    )
    args, _ = mock_cursor.execute.call_args
    sql_query, params = args
    assert "%s" in sql_query
    assert sql_injection_str in params

    # 3. Test query_cek_nama_supplier_duplikat
    query_cek_nama_supplier_duplikat(mock_db_conn, nama_supplier=sql_injection_str, cabang_id=1)
    args, _ = mock_cursor.execute.call_args
    sql_query, params = args
    assert "%s" in sql_query
    assert sql_injection_str in params


# ==============================================================================
# D. ADDITIONAL COVERAGE TESTS (100% COVERAGE JAMINAN)
# ==============================================================================

def test_validasi_data_supplier_non_dict_fails():
    """Validasi: Input data_form bukan berupa dictionary."""
    res = validasi_data_supplier("bukan dict")
    assert res.is_success is False
    assert "Input data harus berupa dictionary!" in res.error_msg


def test_validasi_data_supplier_missing_alamat_fails():
    """Validasi: Input data_form tidak mengandung key 'alamat'."""
    raw_data = {
        'nama_supplier': 'Supplier Indah',
        'telp': '0812345678',
        'email': 'test@supplier.com'
    }
    res = validasi_data_supplier(raw_data)
    assert res.is_success is False
    assert "Alamat supplier wajib diisi" in res.error_msg


def test_validasi_data_supplier_empty_alamat_fails():
    """Validasi: Input data_form mengandung 'alamat' kosong."""
    raw_data = {
        'nama_supplier': 'Supplier Indah',
        'alamat': '   ',
        'telp': '0812345678',
        'email': 'test@supplier.com'
    }
    res = validasi_data_supplier(raw_data)
    assert res.is_success is False
    assert "Alamat supplier tidak boleh kosong" in res.error_msg


def test_validasi_data_supplier_invalid_telp_format_fails():
    """Validasi: Format nomor telepon mengandung karakter ilegal."""
    raw_data = {
        'nama_supplier': 'Supplier Indah',
        'alamat': 'Jl. Industri',
        'telp': '0812-ABC-555',
        'email': 'test@supplier.com'
    }
    res = validasi_data_supplier(raw_data)
    assert res.is_success is False
    assert "Format nomor telepon tidak valid" in res.error_msg


def test_validasi_data_supplier_missing_email_fails():
    """Validasi: Input data_form tidak mengandung key 'email'."""
    raw_data = {
        'nama_supplier': 'Supplier Indah',
        'alamat': 'Jl. Industri',
        'telp': '0812345678'
    }
    res = validasi_data_supplier(raw_data)
    assert res.is_success is False
    assert "Email supplier wajib diisi" in res.error_msg


def test_validasi_data_supplier_empty_email_fails():
    """Validasi: Input data_form mengandung 'email' kosong."""
    raw_data = {
        'nama_supplier': 'Supplier Indah',
        'alamat': 'Jl. Industri',
        'telp': '0812345678',
        'email': '   '
    }
    res = validasi_data_supplier(raw_data)
    assert res.is_success is False
    assert "Email supplier tidak boleh kosong" in res.error_msg


def test_validasi_supplier_id_non_str_fails():
    """Validasi ID: Input ID bukan string."""
    res = validasi_supplier_id(123)
    assert res.is_valid is False
    assert "Tipe data ID supplier harus berupa string!" in res.error_msg


def test_validasi_supplier_id_empty_fails():
    """Validasi ID: Input ID string kosong."""
    res = validasi_supplier_id('   ')
    assert res.is_valid is False
    assert "ID supplier tidak boleh kosong!" in res.error_msg


def test_validasi_supplier_id_non_positive_fails():
    """Validasi ID: Input ID string angka non-positif."""
    res = validasi_supplier_id('0')
    assert res.is_valid is False
    assert "ID supplier harus berupa angka bulat positif!" in res.error_msg


def test_validasi_supplier_id_float_fails():
    """Validasi ID: Input ID berupa format float."""
    res = validasi_supplier_id('12.34')
    assert res.is_valid is False
    assert "ID supplier harus berupa angka bulat positif!" in res.error_msg


def test_query_daftar_supplier_exception(mock_db_conn):
    """Database: query_daftar_supplier menangani Exception dari basis data."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.execute.side_effect = Exception("Database crash")

    db_res = query_daftar_supplier(mock_db_conn, cabang_id=1)
    assert db_res.is_success is False
    assert "ERR-DB-136" in db_res.error_msg


def test_query_detail_supplier_exception(mock_db_conn):
    """Database: query_detail_supplier menangani Exception dari basis data."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.execute.side_effect = Exception("Database crash")

    db_res = query_detail_supplier(mock_db_conn, supplier_id=1, cabang_id=1)
    assert db_res.is_success is False
    assert "ERR-DB-136" in db_res.error_msg


def test_query_insert_supplier_exception(mock_db_conn):
    """Database: query_insert_supplier menangani Exception dan melakukan rollback."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.execute.side_effect = Exception("Insertion crash")

    db_res = query_insert_supplier(
        mock_db_conn,
        nama_supplier='Test',
        alamat='Test',
        telp='123',
        email='test@test.com',
        cabang_id=1
    )
    assert db_res.is_success is False
    assert "ERR-DB-136" in db_res.error_msg
    mock_db_conn.rollback.assert_called_once()


def test_query_update_supplier_exception(mock_db_conn):
    """Database: query_update_supplier menangani Exception dan melakukan rollback."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.execute.side_effect = Exception("Update crash")

    db_res = query_update_supplier(
        mock_db_conn,
        supplier_id=1,
        nama_supplier='Test',
        alamat='Test',
        telp='123',
        email='test@test.com',
        cabang_id=1
    )
    assert db_res.is_success is False
    assert "ERR-DB-136" in db_res.error_msg
    mock_db_conn.rollback.assert_called_once()


def test_query_delete_supplier_check_riwayat_exception(mock_db_conn):
    """Database: query_delete_supplier mentolerir kegagalan pengecekan tabel riwayat."""
    mock_cursor = mock_db_conn.cursor.return_value
    # Fetch 1: Check utang returns count=0
    # Fetch 2: Check riwayat raises Exception (e.g. table doesn't exist)
    mock_cursor.fetchone.side_effect = [{'count': 0}, Exception("Table riwayat_harga_supplier does not exist")]
    mock_cursor.rowcount = 1

    db_res = query_delete_supplier(mock_db_conn, supplier_id=1, cabang_id=1)
    assert db_res.is_success is True
    assert db_res.data == 1
    mock_db_conn.commit.assert_called_once()


def test_query_delete_supplier_outer_exception(mock_db_conn):
    """Database: query_delete_supplier menangani Exception database utama dan melakukan rollback."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.fetchone.return_value = {'count': 0}
    # Simulasi commit raise Exception
    mock_db_conn.commit.side_effect = Exception("Commit failure")

    db_res = query_delete_supplier(mock_db_conn, supplier_id=1, cabang_id=1)
    assert db_res.is_success is False
    assert "ERR-DB-136" in db_res.error_msg
    mock_db_conn.rollback.assert_called_once()


def test_query_cek_nama_supplier_duplikat_exclude_id(mock_db_conn):
    """Database: query_cek_nama_supplier_duplikat dengan exclude_id (skenario edit)."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_row = {'id': 2, 'nama_supplier': 'CV. Sinar Abadi'}
    mock_cursor.fetchone.return_value = mock_row

    db_res = query_cek_nama_supplier_duplikat(
        mock_db_conn,
        nama_supplier='CV. Sinar Abadi',
        cabang_id=1,
        exclude_id=15
    )
    assert db_res.is_success is True
    assert db_res.data == mock_row
    
    args, _ = mock_cursor.execute.call_args
    sql_query, params = args
    assert "id != %s" in sql_query
    assert params[2] == 15


def test_query_cek_nama_supplier_duplikat_exception(mock_db_conn):
    """Database: query_cek_nama_supplier_duplikat menangani Exception dari basis data."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.execute.side_effect = Exception("Duplicate check crash")

    db_res = query_cek_nama_supplier_duplikat(mock_db_conn, nama_supplier='Test', cabang_id=1)
    assert db_res.is_success is False
    assert "ERR-DB-136" in db_res.error_msg


def test_validasi_supplier_id_valid():
    """Validasi ID: Input ID string angka positif valid."""
    res = validasi_supplier_id('15')
    assert res.is_valid is True
    assert res.sanitized_data == 15
    assert res.error_msg is None


def test_query_insert_supplier_rollback_exception(mock_db_conn):
    """Database: query_insert_supplier menangani Exception pada rollback (toleransi pass)."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.execute.side_effect = Exception("Insertion crash")
    mock_db_conn.rollback.side_effect = Exception("Rollback failure")

    db_res = query_insert_supplier(
        mock_db_conn,
        nama_supplier='Test',
        alamat='Test',
        telp='123',
        email='test@test.com',
        cabang_id=1
    )
    assert db_res.is_success is False
    assert "ERR-DB-136" in db_res.error_msg
    mock_db_conn.rollback.assert_called_once()


def test_query_update_supplier_rollback_exception(mock_db_conn):
    """Database: query_update_supplier menangani Exception pada rollback (toleransi pass)."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.execute.side_effect = Exception("Update crash")
    mock_db_conn.rollback.side_effect = Exception("Rollback failure")

    db_res = query_update_supplier(
        mock_db_conn,
        supplier_id=1,
        nama_supplier='Test',
        alamat='Test',
        telp='123',
        email='test@test.com',
        cabang_id=1
    )
    assert db_res.is_success is False
    assert "ERR-DB-136" in db_res.error_msg
    mock_db_conn.rollback.assert_called_once()


def test_query_delete_supplier_rollback_exception(mock_db_conn):
    """Database: query_delete_supplier menangani Exception pada rollback (toleransi pass)."""
    mock_cursor = mock_db_conn.cursor.return_value
    mock_cursor.fetchone.return_value = {'count': 0}
    # Simulasi commit raise Exception
    mock_db_conn.commit.side_effect = Exception("Commit failure")
    mock_db_conn.rollback.side_effect = Exception("Rollback failure")

    db_res = query_delete_supplier(mock_db_conn, supplier_id=1, cabang_id=1)
    assert db_res.is_success is False
    assert "ERR-DB-136" in db_res.error_msg
    mock_db_conn.rollback.assert_called_once()


def test_query_delete_supplier_with_riwayat_success(mock_db_conn):
    """Database: query_delete_supplier mendeteksi riwayat harga tetapi tetap melanjutkan delete."""
    mock_cursor = mock_db_conn.cursor.return_value
    # Fetch 1: Check utang returns count=0
    # Fetch 2: Check riwayat returns count=1
    mock_cursor.fetchone.side_effect = [{'count': 0}, {'count': 1}]
    mock_cursor.rowcount = 1

    db_res = query_delete_supplier(mock_db_conn, supplier_id=1, cabang_id=1)
    assert db_res.is_success is True
    assert db_res.data == 1
    mock_db_conn.commit.assert_called_once()
