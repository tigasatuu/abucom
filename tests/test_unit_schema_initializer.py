"""
Nama Modul: test_unit_schema_initializer.py
Deskripsi: Unit test terisolasi (mocked) untuk modul db/schema_initializer.py.
           Menguji seluruh fungsi parsing SQL, eksekusi schema DDL, verifikasi
           integritas, dan full initialization tanpa koneksi database MySQL fisik.
Author: Antigravity AI
Tanggal: 2026-06-04
"""

import pytest
from unittest.mock import patch, MagicMock, mock_open
from pathlib import Path
import mysql.connector
import bcrypt

from db.schema_initializer import (
    split_sql_statements,
    read_sql_file,
    execute_schema_init,
    verify_schema_integrity,
    run_full_initialization,
    Result,
    EXPECTED_TABLE_COUNT,
    EXPECTED_SEED_COUNTS,
)


def _make_mysql_error(errno: int, msg: str) -> mysql.connector.Error:
    """Helper untuk membuat mysql.connector.Error dengan errno dan msg."""
    err = mysql.connector.Error()
    err.errno = errno
    err.msg = msg
    return err


class MockCursor:
    """Mock MySQL Cursor yang fleksibel untuk merespon query secara dinamis."""
    def __init__(self, table_count=30, missing_index=None, wrong_seed=None, missing_seed_table=None):
        self.last_query = None
        self.with_rows = False
        self.table_count = table_count
        self.missing_index = missing_index
        self.wrong_seed = wrong_seed
        self.missing_seed_table = missing_seed_table
        self.closed = False

    def execute(self, query, params=None):
        self.last_query = query

    def fetchall(self):
        if not self.last_query:
            return []
        
        if "SHOW TABLES" in self.last_query:
            # Generate daftar tabel
            tbl_list = [
                'transaksi', 'absensi', 'antrian_kerja', 'barang',
                'cabang', 'pengguna', 'saldo_ppob', 'saldo_ewallet', 'system_configs',
                'satuan_ukur', 'konversi_satuan'
            ]
            if self.missing_seed_table and self.missing_seed_table in tbl_list:
                tbl_list.remove(self.missing_seed_table)
                
            # Tambahkan dummy tables agar mencapai table_count
            current_len = len(tbl_list)
            for i in range(self.table_count - current_len):
                tbl_list.append(f"dummy_table_{i}")
            return [(t,) for t in tbl_list]
            
        elif "SHOW INDEX FROM" in self.last_query:
            if "transaksi" in self.last_query and self.missing_index != 'idx_transaksi_tanggal_cabang':
                return [('', '', 'idx_transaksi_tanggal_cabang')]
            elif "absensi" in self.last_query and self.missing_index != 'idx_absensi_pengguna_tanggal':
                return [('', '', 'idx_absensi_pengguna_tanggal')]
            elif "antrian_kerja" in self.last_query and self.missing_index != 'idx_antrian_status_cabang':
                return [('', '', 'idx_antrian_status_cabang')]
            elif "barang" in self.last_query and self.missing_index != 'idx_barang_tipe_cabang':
                return [('', '', 'idx_barang_tipe_cabang')]
            return []
            
        return []

    def fetchone(self):
        if not self.last_query:
            return (0,)
            
        if "SELECT COUNT(*)" in self.last_query:
            for table in EXPECTED_SEED_COUNTS:
                if f"FROM {table}" in self.last_query:
                    if self.wrong_seed and self.wrong_seed[0] == table:
                        return (self.wrong_seed[1],)
                    return (EXPECTED_SEED_COUNTS[table],)
        return (0,)

    def nextset(self):
        return False

    def close(self):
        self.closed = True


# ==============================================================================
# Skenario Test untuk split_sql_statements() (Pure Function)
# ==============================================================================

def test_split_sql_statements_parsing_sederhana() -> None:
    """Memverifikasi parsing statement SQL sederhana dengan semicolon.

    Skenario: Positif
    Target: split_sql_statements
    """
    sql = "CREATE TABLE a (id INT); INSERT INTO a VALUES (1);"
    res = split_sql_statements(sql)
    assert len(res) == 2
    assert res[0] == "CREATE TABLE a (id INT)"
    assert res[1] == "INSERT INTO a VALUES (1)"


def test_split_sql_statements_abaikan_komentar_baris() -> None:
    """Memverifikasi pengabaian komentar baris yang dimulai dengan `--`.

    Skenario: Positif
    Target: split_sql_statements
    """
    sql = "-- Ini komentar baris\nCREATE TABLE a (id INT);\n-- Komentar lagi"
    res = split_sql_statements(sql)
    assert len(res) == 1
    assert res[0] == "CREATE TABLE a (id INT)"


def test_split_sql_statements_abaikan_komentar_hash() -> None:
    """Memverifikasi pengabaian komentar baris yang dimulai dengan `#`.

    Skenario: Positif
    Target: split_sql_statements
    """
    sql = "# Ini komentar hash\nCREATE TABLE a (id INT);"
    res = split_sql_statements(sql)
    assert len(res) == 1
    assert res[0] == "CREATE TABLE a (id INT)"


def test_split_sql_statements_abaikan_komentar_blok() -> None:
    """Memverifikasi pengabaian komentar blok multiline `/* ... */`.

    Skenario: Positif
    Target: split_sql_statements
    """
    sql = "/* Komentar blok\n baris 2 */\nCREATE TABLE a (id INT);"
    res = split_sql_statements(sql)
    assert len(res) == 1
    assert res[0] == "CREATE TABLE a (id INT)"


def test_split_sql_statements_semicolon_dalam_string_literal() -> None:
    """Memverifikasi semicolon di dalam string literal kutip tunggal tidak memecah statement.

    Skenario: Positif
    Target: split_sql_statements
    """
    sql = "INSERT INTO a (nama) VALUES ('Toko; Utama');"
    res = split_sql_statements(sql)
    assert len(res) == 1
    assert res[0] == "INSERT INTO a (nama) VALUES ('Toko; Utama')"


def test_split_sql_statements_semicolon_dalam_double_quote() -> None:
    """Memverifikasi semicolon di dalam string literal kutip ganda tidak memecah statement.

    Skenario: Positif
    Target: split_sql_statements
    """
    sql = 'INSERT INTO a (nama) VALUES ("Toko; Utama");'
    res = split_sql_statements(sql)
    assert len(res) == 1
    assert res[0] == 'INSERT INTO a (nama) VALUES ("Toko; Utama")'


def test_split_sql_statements_multi_statement_kompleks() -> None:
    """Memverifikasi parsing dokumen SQL multi-statement yang kompleks.

    Skenario: Positif
    Target: split_sql_statements
    """
    sql = """
    SET NAMES utf8mb4;
    -- Komentar DDL
    CREATE TABLE cabang (
        id INT PRIMARY KEY # komentar inline
    );
    /* Seed data
    multiline */
    INSERT INTO cabang VALUES (1);
    """
    res = split_sql_statements(sql)
    assert len(res) == 3
    assert "SET NAMES utf8mb4" in res[0]
    assert "CREATE TABLE cabang" in res[1]
    assert "INSERT INTO cabang" in res[2]


def test_split_sql_statements_input_kosong() -> None:
    """Memverifikasi behavior ketika input SQL kosong.

    Skenario: Edge Case
    Target: split_sql_statements
    """
    res = split_sql_statements("")
    assert len(res) == 0


def test_split_sql_statements_hanya_komentar() -> None:
    """Memverifikasi behavior ketika input hanya berisi komentar.

    Skenario: Edge Case
    Target: split_sql_statements
    """
    sql = "-- komentar saja\n/* komentar blok saja */"
    res = split_sql_statements(sql)
    assert len(res) == 0


def test_split_sql_statements_tanpa_trailing_semicolon() -> None:
    """Memverifikasi behavior statement terakhir tanpa semicolon penutup.

    Skenario: Edge Case
    Target: split_sql_statements
    """
    sql = "SELECT 1"
    res = split_sql_statements(sql)
    assert len(res) == 1
    assert res[0] == "SELECT 1"


def test_split_sql_statements_whitespace_berlebih() -> None:
    """Memverifikasi pembersihan whitespace berlebih dari statement.

    Skenario: Edge Case
    Target: split_sql_statements
    """
    sql = "   \n   CREATE TABLE a (id INT)   ;   \n   "
    res = split_sql_statements(sql)
    assert len(res) == 1
    assert res[0] == "CREATE TABLE a (id INT)"


# ==============================================================================
# Skenario Test untuk read_sql_file()
# ==============================================================================

def test_read_sql_file_sukses_file_valid(tmp_path) -> None:
    """Memverifikasi pembacaan sukses file SQL dari path valid.

    Skenario: Positif
    Target: read_sql_file
    """
    # Arrange
    sql_file = tmp_path / "schema_test.sql"
    sql_file.write_text("CREATE TABLE test (id INT);", encoding='utf-8')

    # Act
    res = read_sql_file(str(sql_file))

    # Assert
    assert res.is_success is True
    assert len(res.data) == 1
    assert res.data[0] == "CREATE TABLE test (id INT)"
    assert res.error_msg is None


def test_read_sql_file_gagal_file_tidak_ada() -> None:
    """Memverifikasi penanganan error ketika file SQL tidak ditemukan.

    Skenario: Negatif
    Target: read_sql_file
    """
    # Act
    res = read_sql_file("/nonexistent/schema.sql")

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert "ERR-FILE-003" in res.error_msg
    assert "tidak ditemukan" in res.error_msg


def test_read_sql_file_file_kosong(tmp_path) -> None:
    """Memverifikasi hasil list kosong ketika membaca file SQL kosong.

    Skenario: Edge Case
    Target: read_sql_file
    """
    # Arrange
    sql_file = tmp_path / "empty.sql"
    sql_file.write_text("", encoding='utf-8')

    # Act
    res = read_sql_file(str(sql_file))

    # Assert
    assert res.is_success is True
    assert len(res.data) == 0


@patch('db.schema_initializer.Path.exists')
@patch('builtins.open')
def test_read_sql_file_gagal_exception_baca(mock_open_func, mock_exists) -> None:
    """Memverifikasi penanganan error Exception umum ketika membaca file SQL.

    Skenario: Negatif
    Target: read_sql_file
    """
    # Arrange
    mock_exists.return_value = True
    mock_open_func.side_effect = PermissionError("Permission denied")

    # Act
    res = read_sql_file("protected.sql")

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert "ERR-FILE-003" in res.error_msg
    assert "Gagal membaca file" in res.error_msg


def test_read_sql_file_utf8_karakter_khusus(tmp_path) -> None:
    """Memverifikasi pembacaan file SQL dengan encoding UTF-8 dan karakter khusus.

    Skenario: Positif
    Target: read_sql_file
    """
    # Arrange
    sql_file = tmp_path / "utf8.sql"
    sql_file.write_text("INSERT INTO cabang (nama) VALUES ('Bandung — Cabang Utama ✓');", encoding='utf-8')

    # Act
    res = read_sql_file(str(sql_file))

    # Assert
    assert res.is_success is True
    assert "Cabang Utama ✓" in res.data[0]


# ==============================================================================
# Skenario Test untuk execute_schema_init()
# ==============================================================================

def test_execute_schema_init_semua_sukses() -> None:
    """Memverifikasi sukses eksekusi seluruh statement SQL DDL.

    Skenario: Positif
    Target: execute_schema_init
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.with_rows = False
    mock_cursor.nextset.return_value = False
    statements = ["CREATE TABLE a (id INT)", "INSERT INTO a VALUES (1)"]

    # Act
    res = execute_schema_init(mock_conn, statements)

    # Assert
    assert res.is_success is True
    assert res.data['success'] == 2
    assert res.data['failed'] == 0
    assert len(res.data['errors']) == 0
    assert res.error_msg is None
    assert mock_cursor.execute.call_count == 2
    mock_cursor.close.assert_called_once()


def test_execute_schema_init_sebagian_gagal_mysql_error() -> None:
    """Memverifikasi penanganan error ketika sebagian statement gagal karena MySQL error.

    Skenario: Negatif
    Target: execute_schema_init
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.with_rows = False
    mock_cursor.nextset.return_value = False
    
    mysql_err = _make_mysql_error(1050, "Table already exists")
    mock_cursor.execute.side_effect = [None, mysql_err, None]
    statements = ["stmt1", "stmt2", "stmt3"]

    # Act
    res = execute_schema_init(mock_conn, statements)

    # Assert
    assert res.is_success is False
    assert res.data['success'] == 2
    assert res.data['failed'] == 1
    assert len(res.data['errors']) == 1
    assert "Table already exists" in res.data['errors'][0]
    assert "Inisialisasi selesai dengan 1 kesalahan." in res.error_msg


def test_execute_schema_init_gagal_exception_umum() -> None:
    """Memverifikasi penanganan error ketika statement gagal karena Exception umum.

    Skenario: Negatif
    Target: execute_schema_init
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = Exception("System error")
    mock_cursor.nextset.return_value = False
    statements = ["stmt_bad"]

    # Act
    res = execute_schema_init(mock_conn, statements)

    # Assert
    assert res.is_success is False
    assert res.data['success'] == 0
    assert res.data['failed'] == 1
    assert len(res.data['errors']) == 1
    assert "System error" in res.data['errors'][0]


def test_execute_schema_init_statement_kosong() -> None:
    """Memverifikasi statement kosong diabaikan dari eksekusi.

    Skenario: Edge Case
    Target: execute_schema_init
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.nextset.return_value = False
    statements = ["", "", "   "]

    # Act
    res = execute_schema_init(mock_conn, statements)

    # Assert
    assert res.is_success is True
    assert res.data['success'] == 0
    assert res.data['failed'] == 0
    assert mock_cursor.execute.call_count == 0


def test_execute_schema_init_statement_whitespace() -> None:
    """Memverifikasi statement hanya whitespace tidak dieksekusi.

    Skenario: Edge Case
    Target: execute_schema_init
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.nextset.return_value = False
    statements = ["\n\t", "SELECT 1"]

    # Act
    res = execute_schema_init(mock_conn, statements)

    # Assert
    assert res.is_success is True
    assert res.data['success'] == 1
    assert mock_cursor.execute.call_count == 1


def test_execute_schema_init_statement_dengan_result_set() -> None:
    """Memverifikasi pembersihan buffer cursor untuk query yang mengembalikan baris data.

    Skenario: Positif
    Target: execute_schema_init
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.with_rows = True
    mock_cursor.fetchall.return_value = [("row1",), ("row2",)]
    mock_cursor.nextset.side_effect = [True, False]
    statements = ["SHOW TABLES"]

    # Act
    res = execute_schema_init(mock_conn, statements)

    # Assert
    assert res.is_success is True
    assert res.data['success'] == 1
    assert mock_cursor.fetchall.call_count == 2  # Panggilan execute + nextset yang True


# ==============================================================================
# Skenario Test untuk verify_schema_integrity()
# ==============================================================================

def test_verify_schema_integrity_skema_valid_sempurna() -> None:
    """Memverifikasi integritas skema valid sempurna (30 tabel, 4 index, seed data pas).

    Skenario: Positif
    Target: verify_schema_integrity
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MockCursor(table_count=30)
    mock_conn.cursor.return_value = mock_cursor

    # Act
    res = verify_schema_integrity(mock_conn)

    # Assert
    assert res.is_success is True
    assert res.data['tables'] == 30
    assert res.data['indexes'] == 4
    assert res.data['seeds']['cabang'] == 1
    assert res.data['seeds']['pengguna'] == 1
    assert res.data['seeds']['saldo_ppob'] == 2
    assert res.data['seeds']['saldo_ewallet'] == 6
    assert res.data['seeds']['system_configs'] == 13
    assert res.data['seeds']['satuan_ukur'] == 16
    assert res.data['seeds']['konversi_satuan'] == 10
    assert res.error_msg is None
    assert mock_cursor.closed is True


def test_verify_schema_integrity_tabel_kurang() -> None:
    """Memverifikasi kegagalan verifikasi jika jumlah tabel kurang dari 28.

    Skenario: Negatif
    Target: verify_schema_integrity
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MockCursor(table_count=20)
    mock_conn.cursor.return_value = mock_cursor

    # Act
    res = verify_schema_integrity(mock_conn)

    # Assert
    assert res.is_success is False
    assert res.data['tables'] == 20
    assert "Jumlah tabel tidak sesuai" in res.error_msg


def test_verify_schema_integrity_index_hilang() -> None:
    """Memverifikasi kegagalan verifikasi jika composite index tidak lengkap.

    Skenario: Negatif
    Target: verify_schema_integrity
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MockCursor(table_count=30, missing_index='idx_transaksi_tanggal_cabang')
    mock_conn.cursor.return_value = mock_cursor

    # Act
    res = verify_schema_integrity(mock_conn)

    # Assert
    assert res.is_success is False
    assert res.data['indexes'] == 3
    assert "Index idx_transaksi_tanggal_cabang tidak ditemukan" in res.error_msg


def test_verify_schema_integrity_seed_data_salah() -> None:
    """Memverifikasi kegagalan verifikasi jika data seed tidak sesuai jumlahnya.

    Skenario: Negatif
    Target: verify_schema_integrity
    """
    # Arrange
    mock_conn = MagicMock()
    # system_configs diharapkan 13, di-mock bernilai 10
    mock_cursor = MockCursor(table_count=30, wrong_seed=('system_configs', 10))
    mock_conn.cursor.return_value = mock_cursor

    # Act
    res = verify_schema_integrity(mock_conn)

    # Assert
    assert res.is_success is False
    assert res.data['seeds']['system_configs'] == 10
    assert "Jumlah baris seed data di tabel system_configs tidak sesuai" in res.error_msg


def test_verify_schema_integrity_tabel_seed_hilang() -> None:
    """Memverifikasi kegagalan verifikasi jika tabel seed tidak ditemukan sama sekali.

    Skenario: Negatif
    Target: verify_schema_integrity
    """
    # Arrange
    mock_conn = MagicMock()
    # Hilangkan tabel 'system_configs' dari list
    mock_cursor = MockCursor(table_count=30, missing_seed_table='system_configs')
    mock_conn.cursor.return_value = mock_cursor

    # Act
    res = verify_schema_integrity(mock_conn)

    # Assert
    assert res.is_success is False
    assert res.data['seeds']['system_configs'] == 0
    assert "Tabel system_configs tidak ditemukan saat verifikasi seed data" in res.error_msg


def test_verify_schema_integrity_gagal_mysql_error() -> None:
    """Memverifikasi kegagalan verifikasi karena mysql.connector.Error saat eksekusi.

    Skenario: Negatif
    Target: verify_schema_integrity
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = _make_mysql_error(1146, "Table not found")

    # Act
    res = verify_schema_integrity(mock_conn)

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert "ERR-DB-001" in res.error_msg
    assert "1146" in res.error_msg
    mock_cursor.close.assert_called_once()


def test_verify_schema_integrity_gagal_exception_umum() -> None:
    """Memverifikasi kegagalan verifikasi karena Exception umum.

    Skenario: Negatif
    Target: verify_schema_integrity
    """
    # Arrange
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = Exception("General connection failure")

    # Act
    res = verify_schema_integrity(mock_conn)

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert "ERR-DB-001" in res.error_msg
    assert "General connection failure" in res.error_msg
    mock_cursor.close.assert_called_once()


# ==============================================================================
# Skenario Test untuk run_full_initialization()
# ==============================================================================

@patch('db.schema_initializer.mysql.connector.connect')
@patch('db.schema_initializer.read_sql_file')
@patch('db.schema_initializer.execute_schema_init')
@patch('db.schema_initializer.bcrypt.gensalt')
@patch('db.schema_initializer.bcrypt.hashpw')
@patch('db.schema_initializer.seed_satuan_ukur_default')
@patch('db.schema_initializer.seed_konversi_satuan_default')
@patch('db.schema_initializer.verify_schema_integrity')
def test_run_full_initialization_sukses_lengkap(
    mock_verify, mock_konversi, mock_satuan, mock_hashpw, mock_gensalt, mock_exec_init, mock_read_file, mock_connect
) -> None:
    """Memverifikasi inisialisasi lengkap sukses dari awal hingga akhir.

    Skenario: Positif
    Target: run_full_initialization
    """
    # Arrange
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_read_file.return_value = Result(True, ["stmt1", "stmt2"], None)
    mock_exec_init.return_value = Result(True, {'success': 2, 'failed': 0, 'errors': []}, None)
    
    mock_gensalt.return_value = b"$2b$12$salt"
    mock_hashpw.return_value = b"$2b$12$hashed"
    mock_satuan.return_value = Result(True, 16, None)
    mock_konversi.return_value = Result(True, 10, None)
    
    mock_verify.return_value = Result(True, {'tables': 30, 'indexes': 4, 'seeds': {}}, None)

    # Act
    res = run_full_initialization(
        root_host='localhost',
        root_port=3306,
        root_user='root',
        root_password='rootpassword',
        schema_file_path='schema.sql'
    )

    # Assert
    assert res.is_success is True
    assert res.data['init_stats']['success'] == 2
    assert res.data['verify_report']['tables'] == 30
    assert res.error_msg is None
    
    # Verifikasi chain calls
    mock_connect.assert_called_once_with(host='localhost', port=3306, user='root', password='rootpassword')
    mock_read_file.assert_called_once_with('schema.sql')
    mock_exec_init.assert_called_once_with(mock_conn, ["stmt1", "stmt2"])
    mock_gensalt.assert_called_once_with(rounds=12)
    mock_hashpw.assert_called_once_with(b'admin123', b"$2b$12$salt")
    
    # Check UPDATE password query
    mock_cursor.execute.assert_any_call("USE abucom_db")
    mock_cursor.execute.assert_any_call(
        "UPDATE pengguna SET password_hash = %s WHERE id = 1",
        ("$2b$12$hashed",)
    )
    mock_conn.commit.assert_called_once()
    mock_verify.assert_called_once_with(mock_conn)
    mock_conn.close.assert_called_once()


@patch('db.schema_initializer.mysql.connector.connect')
def test_run_full_initialization_gagal_koneksi(mock_connect) -> None:
    """Memverifikasi kegagalan inisialisasi pada tahap koneksi MySQL error.

    Skenario: Negatif
    Target: run_full_initialization
    """
    # Arrange
    mock_connect.side_effect = _make_mysql_error(2003, "Refused")

    # Act
    res = run_full_initialization('invalid', 9999, 'root', 'pass', 'schema.sql')

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert "ERR-DB-001" in res.error_msg
    assert "Koneksi gagal" in res.error_msg


@patch('db.schema_initializer.mysql.connector.connect')
def test_run_full_initialization_gagal_koneksi_exception(mock_connect) -> None:
    """Memverifikasi kegagalan inisialisasi pada tahap koneksi Exception umum.

    Skenario: Negatif
    Target: run_full_initialization
    """
    # Arrange
    mock_connect.side_effect = Exception("Timeout")

    # Act
    res = run_full_initialization('localhost', 3306, 'root', 'pass', 'schema.sql')

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert "ERR-DB-001" in res.error_msg
    assert "Timeout" in res.error_msg


@patch('db.schema_initializer.mysql.connector.connect')
@patch('db.schema_initializer.read_sql_file')
def test_run_full_initialization_gagal_baca_sql(mock_read_file, mock_connect) -> None:
    """Memverifikasi pembatalan inisialisasi dan penutupan koneksi jika baca SQL gagal.

    Skenario: Negatif
    Target: run_full_initialization
    """
    # Arrange
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    mock_read_file.return_value = Result(False, None, "ERR-FILE-003: Not found")

    # Act
    res = run_full_initialization('localhost', 3306, 'root', 'pass', 'schema.sql')

    # Assert
    assert res.is_success is False
    assert "ERR-FILE-003" in res.error_msg
    mock_conn.close.assert_called_once()


@patch('db.schema_initializer.mysql.connector.connect')
@patch('db.schema_initializer.read_sql_file')
@patch('db.schema_initializer.execute_schema_init')
def test_run_full_initialization_gagal_eksekusi_ddl(mock_exec_init, mock_read_file, mock_connect) -> None:
    """Memverifikasi pembatalan inisialisasi dan penutupan koneksi jika eksekusi DDL gagal.

    Skenario: Negatif
    Target: run_full_initialization
    """
    # Arrange
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    mock_read_file.return_value = Result(True, ["stmt1"], None)
    mock_exec_init.return_value = Result(False, {'success': 0, 'failed': 1}, "Inisialisasi selesai dengan kesalahan.")

    # Act
    res = run_full_initialization('localhost', 3306, 'root', 'pass', 'schema.sql')

    # Assert
    assert res.is_success is False
    assert "Inisialisasi selesai" in res.error_msg
    mock_conn.close.assert_called_once()


@patch('db.schema_initializer.mysql.connector.connect')
@patch('db.schema_initializer.read_sql_file')
@patch('db.schema_initializer.execute_schema_init')
@patch('db.schema_initializer.bcrypt.gensalt')
def test_run_full_initialization_gagal_bcrypt_hash(
    mock_gensalt, mock_exec_init, mock_read_file, mock_connect
) -> None:
    """Memverifikasi kegagalan inisialisasi pada tahap enkripsi bcrypt password default.

    Skenario: Negatif
    Target: run_full_initialization
    """
    # Arrange
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    mock_read_file.return_value = Result(True, ["stmt1"], None)
    mock_exec_init.return_value = Result(True, {'success': 1, 'failed': 0}, None)
    mock_gensalt.side_effect = Exception("Bcrypt library crash")

    # Act
    res = run_full_initialization('localhost', 3306, 'root', 'pass', 'schema.sql')

    # Assert
    assert res.is_success is False
    assert "ERR-VAL-050" in res.error_msg
    assert "Bcrypt library crash" in res.error_msg
    mock_conn.close.assert_called_once()


@patch('db.schema_initializer.mysql.connector.connect')
@patch('db.schema_initializer.read_sql_file')
@patch('db.schema_initializer.execute_schema_init')
@patch('db.schema_initializer.bcrypt.gensalt')
@patch('db.schema_initializer.bcrypt.hashpw')
def test_run_full_initialization_gagal_update_password_mysql_error(
    mock_hashpw, mock_gensalt, mock_exec_init, mock_read_file, mock_connect
) -> None:
    """Memverifikasi kegagalan inisialisasi ketika query update password melempar MySQL error.

    Skenario: Negatif
    Target: run_full_initialization
    """
    # Arrange
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_read_file.return_value = Result(True, ["stmt1"], None)
    mock_exec_init.return_value = Result(True, {'success': 1, 'failed': 0}, None)
    mock_gensalt.return_value = b"salt"
    mock_hashpw.return_value = b"hashed"
    
    mock_cursor.execute.side_effect = _make_mysql_error(1146, "Table pengguna doesn't exist")

    # Act
    res = run_full_initialization('localhost', 3306, 'root', 'pass', 'schema.sql')

    # Assert
    assert res.is_success is False
    assert "ERR-DB-001" in res.error_msg
    assert "Gagal memperbarui password pemilik" in res.error_msg
    assert mock_cursor.close.call_count == 2
    mock_conn.close.assert_called_once()


@patch('db.schema_initializer.mysql.connector.connect')
@patch('db.schema_initializer.read_sql_file')
@patch('db.schema_initializer.execute_schema_init')
@patch('db.schema_initializer.bcrypt.gensalt')
@patch('db.schema_initializer.bcrypt.hashpw')
def test_run_full_initialization_gagal_update_password_exception(
    mock_hashpw, mock_gensalt, mock_exec_init, mock_read_file, mock_connect
) -> None:
    """Memverifikasi kegagalan inisialisasi ketika query update password melempar Exception umum.

    Skenario: Negatif
    Target: run_full_initialization
    """
    # Arrange
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_read_file.return_value = Result(True, ["stmt1"], None)
    mock_exec_init.return_value = Result(True, {'success': 1, 'failed': 0}, None)
    mock_gensalt.return_value = b"salt"
    mock_hashpw.return_value = b"hashed"
    
    mock_cursor.execute.side_effect = Exception("System crash during update")

    # Act
    res = run_full_initialization('localhost', 3306, 'root', 'pass', 'schema.sql')

    # Assert
    assert res.is_success is False
    assert "ERR-DB-001" in res.error_msg
    assert "System crash during update" in res.error_msg
    assert mock_cursor.close.call_count == 2
    mock_conn.close.assert_called_once()


@patch('db.schema_initializer.mysql.connector.connect')
@patch('db.schema_initializer.read_sql_file')
@patch('db.schema_initializer.execute_schema_init')
@patch('db.schema_initializer.bcrypt.gensalt')
@patch('db.schema_initializer.bcrypt.hashpw')
@patch('db.schema_initializer.seed_satuan_ukur_default')
@patch('db.schema_initializer.seed_konversi_satuan_default')
@patch('db.schema_initializer.verify_schema_integrity')
def test_run_full_initialization_gagal_verifikasi(
    mock_verify, mock_konversi, mock_satuan, mock_hashpw, mock_gensalt, mock_exec_init, mock_read_file, mock_connect
) -> None:
    """Memverifikasi kegagalan inisialisasi jika tahap verifikasi akhir mendeteksi skema tidak valid.

    Skenario: Negatif
    Target: run_full_initialization
    """
    # Arrange
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_read_file.return_value = Result(True, ["stmt1"], None)
    mock_exec_init.return_value = Result(True, {'success': 1, 'failed': 0}, None)
    mock_gensalt.return_value = b"salt"
    mock_hashpw.return_value = b"hashed"
    mock_satuan.return_value = Result(True, 16, None)
    mock_konversi.return_value = Result(True, 10, None)
    
    mock_verify.return_value = Result(False, {'tables': 20}, "Verifikasi gagal: tabel kurang")

    # Act
    res = run_full_initialization('localhost', 3306, 'root', 'pass', 'schema.sql')

    # Assert
    assert res.is_success is False
    assert "Verifikasi gagal" in res.error_msg
    mock_conn.close.assert_called_once()


# ==============================================================================
# Skenario Validasi Konstanta
# ==============================================================================

def test_konstanta_expected_table_count() -> None:
    """Memverifikasi nilai konstanta EXPECTED_TABLE_COUNT.

    Skenario: Validasi
    Target: EXPECTED_TABLE_COUNT
    """
    assert EXPECTED_TABLE_COUNT == 30


def test_konstanta_expected_seed_counts() -> None:
    """Memverifikasi isi dan nilai dari konstanta EXPECTED_SEED_COUNTS.

    Skenario: Validasi
    Target: EXPECTED_SEED_COUNTS
    """
    assert len(EXPECTED_SEED_COUNTS) == 7
    assert EXPECTED_SEED_COUNTS['cabang'] == 1
    assert EXPECTED_SEED_COUNTS['pengguna'] == 1
    assert EXPECTED_SEED_COUNTS['saldo_ppob'] == 2
    assert EXPECTED_SEED_COUNTS['saldo_ewallet'] == 6
    assert EXPECTED_SEED_COUNTS['system_configs'] == 13
    assert EXPECTED_SEED_COUNTS['satuan_ukur'] == 16
    assert EXPECTED_SEED_COUNTS['konversi_satuan'] == 10


@patch('db.schema_initializer.Path.exists')
@patch('builtins.open')
def test_read_sql_file_file_not_found_error(mock_open_func, mock_exists) -> None:
    """Memverifikasi penanganan FileNotFoundError saat open file.

    Skenario: Negatif
    Target: read_sql_file
    """
    mock_exists.return_value = True
    mock_open_func.side_effect = FileNotFoundError()
    res = read_sql_file("missing.sql")
    assert res.is_success is False
    assert "tidak ditemukan" in res.error_msg


def test_execute_schema_init_nextset_error() -> None:
    """Memverifikasi penanganan mysql.connector.Error saat nextset.

    Skenario: Negatif / Edge Case
    Target: execute_schema_init
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.with_rows = True
    mock_cursor.fetchall.return_value = []
    mock_cursor.nextset.side_effect = _make_mysql_error(2000, "Buffer error")
    statements = ["SELECT 1"]
    res = execute_schema_init(mock_conn, statements)
    assert res.is_success is True
    assert res.data['success'] == 1


def test_verify_schema_integrity_tabel_index_hilang() -> None:
    """Memverifikasi kegagalan verifikasi jika tabel untuk composite index tidak ada.

    Skenario: Negatif / Edge Case
    Target: verify_schema_integrity
    """
    mock_conn = MagicMock()
    mock_cursor = MockCursor(table_count=30, missing_seed_table='transaksi')
    mock_conn.cursor.return_value = mock_cursor
    res = verify_schema_integrity(mock_conn)
    assert res.is_success is False
    assert "Tabel transaksi tidak ada untuk pemeriksaan index" in res.error_msg

