"""
Nama Modul: test_db_connector.py
Deskripsi: Unit testing dan integration testing untuk modul connection pool
           database (db/db_connector.py) dan query builder (db/query_builder.py).
           Mencakup pengujian retry mechanism exponential backoff,
           connection pooling, dan ACID transaction wrapper.
Author: Claude Sonnet 4.6 (STK-004)
Tanggal: 2026-06-04
"""

import time
import pytest
from unittest.mock import patch, MagicMock
import mysql.connector

# Import modules under test
import db.db_connector as db_conn_mod
from db.db_connector import (
    create_connection_pool,
    get_db_connection,
    close_connection_pool,
    get_root_connection,
    get_pool_status,
    Result,
    MAX_RETRIES,
    RETRY_ERROR_CODES,
    RETRY_BASE_SECONDS,
)
from db.query_builder import (
    execute_query,
    execute_acid_transaction,
    execute_insert,
    execute_many,
    execute_with_retry,
)


@pytest.fixture(autouse=True)
def reset_connection_pool():
    """Reset variabel modul _connection_pool sebelum dan sesudah setiap test."""
    db_conn_mod._connection_pool = None
    yield
    db_conn_mod._connection_pool = None


def _make_mysql_error(errno: int, msg: str) -> mysql.connector.Error:
    """Helper untuk membuat objek mysql.connector.Error."""
    err = mysql.connector.Error()
    err.errno = errno
    err.msg = msg
    return err


# ==============================================================================
# 6.2. Unit Test — Connection Pool (Pure/Mock)
# ==============================================================================

@patch('db.db_connector.pooling.MySQLConnectionPool')
def test_create_pool_sukses(mock_pool_cls) -> None:
    """Memverifikasi pembuatan connection pool sukses."""
    mock_pool_instance = MagicMock()
    mock_pool_cls.return_value = mock_pool_instance

    res = create_connection_pool(
        host='localhost',
        port=3306,
        user='app',
        password='pass',
        database='db'
    )

    assert res.is_success is True
    assert res.data is mock_pool_instance
    assert db_conn_mod._connection_pool is mock_pool_instance


@patch('db.db_connector.pooling.MySQLConnectionPool')
def test_create_pool_gagal_mysql_error(mock_pool_cls) -> None:
    """Memverifikasi kegagalan pembuatan pool karena MySQL error."""
    mysql_err = _make_mysql_error(2003, "Can't connect to MySQL server")
    mock_pool_cls.side_effect = mysql_err

    res = create_connection_pool(
        host='localhost',
        port=3306,
        user='app',
        password='pass',
        database='db'
    )

    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert '2003' in res.error_msg


@patch('db.db_connector.pooling.MySQLConnectionPool')
def test_create_pool_gagal_exception_umum(mock_pool_cls) -> None:
    """Memverifikasi kegagalan pembuatan pool karena Exception umum."""
    mock_pool_cls.side_effect = Exception("Unexpected config error")

    res = create_connection_pool(
        host='localhost',
        port=3306,
        user='app',
        password='pass',
        database='db'
    )

    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'Unexpected config error' in res.error_msg


def test_get_connection_pool_belum_init() -> None:
    """Memverifikasi error ketika mengambil koneksi sebelum pool diinisialisasi."""
    res = get_db_connection()
    assert res.is_success is False
    assert 'ERR-DB-001' in res.error_msg
    assert 'belum diinisialisasi' in res.error_msg


def test_get_connection_sukses() -> None:
    """Memverifikasi sukses mengambil koneksi dari pool."""
    mock_pool = MagicMock()
    mock_conn = MagicMock()
    mock_pool.get_connection.return_value = mock_conn
    db_conn_mod._connection_pool = mock_pool

    res = get_db_connection()
    assert res.is_success is True
    assert res.data is mock_conn
    mock_pool.get_connection.assert_called_once()


def test_close_pool_sukses() -> None:
    """Memverifikasi sukses menutup connection pool."""
    mock_pool = MagicMock()
    db_conn_mod._connection_pool = mock_pool

    res = close_connection_pool()
    assert res.is_success is True
    mock_pool._remove_connections.assert_called_once()
    assert db_conn_mod._connection_pool is None


def test_close_pool_sudah_none() -> None:
    """Memverifikasi sukses menutup pool ketika pool sudah None."""
    res = close_connection_pool()
    assert res.is_success is True
    assert db_conn_mod._connection_pool is None


def test_close_pool_gagal_exception() -> None:
    """Memverifikasi kegagalan penutupan pool karena exception."""
    mock_pool = MagicMock()
    mock_pool._remove_connections.side_effect = Exception("Cannot remove connections")
    db_conn_mod._connection_pool = mock_pool

    res = close_connection_pool()
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'Cannot remove connections' in res.error_msg
    # Pastikan pool tidak di-reset ke None jika terjadi Exception
    assert db_conn_mod._connection_pool is mock_pool


def test_get_pool_status_active() -> None:
    """Memverifikasi status pool ketika aktif."""
    mock_pool = MagicMock()
    mock_pool.pool_name = 'abupool'
    mock_pool.pool_size = 5
    db_conn_mod._connection_pool = mock_pool

    res = get_pool_status()
    assert res.is_success is True
    assert res.data['is_active'] is True
    assert res.data['pool_name'] == 'abupool'
    assert res.data['pool_size'] == 5


def test_get_pool_status_inactive() -> None:
    """Memverifikasi status pool ketika tidak aktif (None)."""
    res = get_pool_status()
    assert res.is_success is True
    assert res.data['is_active'] is False
    assert res.data['pool_name'] is None
    assert res.data['pool_size'] == 0


def test_get_pool_status_gagal_exception() -> None:
    """Memverifikasi kegagalan mendapatkan status pool karena exception."""
    class BadPool:
        @property
        def pool_name(self):
            raise RuntimeError("Bad pool name")
    db_conn_mod._connection_pool = BadPool()

    res = get_pool_status()
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'Bad pool name' in res.error_msg


# ==============================================================================
# 6.3. Unit Test — Retry Mechanism (Pure/Mock)
# ==============================================================================

@patch('db.db_connector.time.sleep')
def test_retry_koneksi_gagal_2006_lalu_sukses(mock_sleep) -> None:
    """Simulasi error 2006 pada attempt 1, sukses pada attempt 2."""
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(2006, "Server gone away")
    mock_conn = MagicMock()
    mock_pool.get_connection.side_effect = [mysql_err, mock_conn]
    db_conn_mod._connection_pool = mock_pool

    res = get_db_connection()
    assert res.is_success is True
    assert res.data is mock_conn
    assert mock_pool.get_connection.call_count == 2
    mock_sleep.assert_called_once_with(2)  # 2^1 = 2 detik


@patch('db.db_connector.time.sleep')
def test_retry_koneksi_gagal_2013_tiga_kali(mock_sleep) -> None:
    """Simulasi error 2013 pada ketiga percobaan."""
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(2013, "Lost connection during query")
    mock_pool.get_connection.side_effect = mysql_err
    db_conn_mod._connection_pool = mock_pool

    res = get_db_connection()
    assert res.is_success is False
    assert res.data is None
    assert mock_pool.get_connection.call_count == MAX_RETRIES
    assert mock_sleep.call_count == 2  # sleep dipanggil setelah attempt 1 (2s) dan 2 (4s)


@patch('db.db_connector.time.sleep')
def test_retry_interval_exponential_backoff(mock_sleep) -> None:
    """Memverifikasi interval wait time eksponensial (2^attempt)."""
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(2006, "Server gone away")
    mock_conn = MagicMock()
    mock_pool.get_connection.side_effect = [mysql_err, mysql_err, mock_conn]
    db_conn_mod._connection_pool = mock_pool

    res = get_db_connection()
    assert res.is_success is True
    assert res.data is mock_conn
    assert mock_sleep.call_count == 2
    mock_sleep.assert_any_call(2)  # RETRY_BASE_SECONDS ** 1
    mock_sleep.assert_any_call(4)  # RETRY_BASE_SECONDS ** 2


def test_retry_error_non_retryable_langsung_gagal() -> None:
    """Error auth (1045) langsung gagal tanpa retry."""
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(1045, "Access denied")
    mock_pool.get_connection.side_effect = mysql_err
    db_conn_mod._connection_pool = mock_pool

    res = get_db_connection()
    assert res.is_success is False
    assert mock_pool.get_connection.call_count == 1


def test_get_db_connection_gagal_exception_umum() -> None:
    """Memverifikasi kegagalan karena exception non-MySQL saat get_connection."""
    mock_pool = MagicMock()
    mock_pool.get_connection.side_effect = Exception("General connection issue")
    db_conn_mod._connection_pool = mock_pool

    res = get_db_connection()
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'General connection issue' in res.error_msg
    assert mock_pool.get_connection.call_count == 1


def test_get_db_connection_gagal_max_retries_nol() -> None:
    """Memverifikasi return kegagalan saat max_retries di-set ke 0."""
    mock_pool = MagicMock()
    db_conn_mod._connection_pool = mock_pool
    res = get_db_connection(max_retries=0)
    assert res.is_success is False
    assert 'ERR-DB-001: Gagal mengambil koneksi dari pool setelah semua retry.' in res.error_msg


# ==============================================================================
# Unit Test — Root Connection
# ==============================================================================

@patch('db.db_connector.mysql.connector.connect')
def test_get_root_connection_sukses(mock_connect) -> None:
    """Memverifikasi sukses mendapatkan koneksi root administratif."""
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn

    res = get_root_connection(
        host='localhost',
        port=3306,
        user='root',
        password='rootpassword'
    )

    assert res.is_success is True
    assert res.data is mock_conn
    mock_connect.assert_called_once_with(
        host='localhost',
        port=3306,
        user='root',
        password='rootpassword'
    )


@patch('db.db_connector.mysql.connector.connect')
def test_get_root_connection_gagal_mysql_error(mock_connect) -> None:
    """Memverifikasi kegagalan koneksi root karena MySQL error."""
    mysql_err = _make_mysql_error(2003, "Connection refused")
    mock_connect.side_effect = mysql_err

    res = get_root_connection(
        host='localhost',
        port=3306,
        user='root',
        password='rootpassword'
    )

    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert '2003' in res.error_msg


@patch('db.db_connector.mysql.connector.connect')
def test_get_root_connection_gagal_exception_umum(mock_connect) -> None:
    """Memverifikasi kegagalan koneksi root karena Exception umum."""
    mock_connect.side_effect = Exception("DNS Failure")

    res = get_root_connection(
        host='localhost',
        port=3306,
        user='root',
        password='rootpassword'
    )

    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'DNS Failure' in res.error_msg


# ==============================================================================
# 6.4. Unit Test — Query Builder (Pure/Mock)
# ==============================================================================

def test_execute_query_select_sukses() -> None:
    """Memverifikasi SELECT query mengembalikan dict data."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.description = ("id", "nama")  # Menandakan SELECT
    mock_cursor.fetchall.return_value = [{'id': 1, 'nama': 'Stempel Flash'}]
    mock_conn.cursor.return_value = mock_cursor

    res = execute_query(mock_conn, "SELECT * FROM barang")
    assert res.is_success is True
    assert len(res.data) == 1
    assert res.data[0]['nama'] == 'Stempel Flash'
    mock_cursor.execute.assert_called_once_with("SELECT * FROM barang", None)
    mock_cursor.close.assert_called_once()
    mock_conn.commit.assert_not_called()


def test_execute_query_select_fetch_one() -> None:
    """Memverifikasi SELECT query dengan fetch_one=True."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.description = ("id", "nama")
    mock_cursor.fetchone.return_value = {'id': 1, 'nama': 'Stempel Flash'}
    mock_conn.cursor.return_value = mock_cursor

    res = execute_query(mock_conn, "SELECT * FROM barang LIMIT 1", fetch_one=True)
    assert res.is_success is True
    assert res.data['id'] == 1
    mock_cursor.fetchone.assert_called_once()


def test_execute_query_select_no_fetch() -> None:
    """Memverifikasi SELECT query dengan fetch_one=False dan fetch_all=False."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.description = ("id", "nama")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_query(mock_conn, "SELECT * FROM barang", fetch_one=False, fetch_all=False)
    assert res.is_success is True
    assert res.data is None


def test_execute_query_insert_sukses() -> None:
    """Memverifikasi INSERT query via execute_query mengembalikan rowcount dan melakukan commit."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.description = None  # Menandakan non-SELECT
    mock_cursor.rowcount = 1
    mock_conn.cursor.return_value = mock_cursor

    res = execute_query(mock_conn, "INSERT INTO barang (nama) VALUES (%s)", ("Kertas A4",))
    assert res.is_success is True
    assert res.data == 1
    mock_cursor.execute.assert_called_once_with("INSERT INTO barang (nama) VALUES (%s)", ("Kertas A4",))
    mock_conn.commit.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_execute_query_error_handling() -> None:
    """Memverifikasi error handling pada execute_query."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = _make_mysql_error(1146, "Table 'abucom_db.nonexistent' doesn't exist")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_query(mock_conn, "SELECT * FROM nonexistent")
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-002' in res.error_msg
    assert '1146' in res.error_msg
    mock_cursor.close.assert_called_once()


def test_execute_query_general_exception() -> None:
    """Memverifikasi general exception handling pada execute_query."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = RuntimeError("Fatal parsing error")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_query(mock_conn, "SELECT 1")
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-002' in res.error_msg
    assert 'Fatal parsing error' in res.error_msg
    mock_cursor.close.assert_called_once()


def test_execute_acid_transaction_commit() -> None:
    """Memverifikasi commit pada execute_acid_transaction ketika semua operasi sukses."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    ops = [
        lambda cursor: cursor.execute("INSERT 1"),
        lambda cursor: cursor.execute("INSERT 2")
    ]

    res = execute_acid_transaction(mock_conn, ops)
    assert res.is_success is True
    assert len(res.data) == 2
    mock_conn.start_transaction.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_conn.rollback.assert_not_called()
    mock_cursor.close.assert_called_once()


def test_execute_acid_transaction_rollback() -> None:
    """Memverifikasi rollback pada execute_acid_transaction ketika salah satu operasi gagal."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    def op_gagal(cursor):
        raise ValueError("Gagal input data")

    ops = [
        lambda cursor: cursor.execute("INSERT 1"),
        op_gagal
    ]

    res = execute_acid_transaction(mock_conn, ops)
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-TX' in res.error_msg
    mock_conn.start_transaction.assert_called_once()
    mock_conn.rollback.assert_called_once()
    mock_conn.commit.assert_not_called()
    mock_cursor.close.assert_called_once()


def test_execute_acid_transaction_rollback_exception() -> None:
    """Memverifikasi handling jika rollback itu sendiri gagal."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.rollback.side_effect = RuntimeError("DBMS crash")

    def op_gagal(cursor):
        raise ValueError("Gagal input")

    res = execute_acid_transaction(mock_conn, [op_gagal])
    assert res.is_success is False
    assert 'ERR-DB-TX' in res.error_msg
    mock_conn.rollback.assert_called_once()


def test_execute_insert_sukses() -> None:
    """Memverifikasi execute_insert sukses."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.lastrowid = 100
    mock_conn.cursor.return_value = mock_cursor

    res = execute_insert(mock_conn, "INSERT INTO table VALUES (%s)", ("val",))
    assert res.is_success is True
    assert res.data == 100
    mock_conn.commit.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_execute_insert_gagal_mysql_error() -> None:
    """Memverifikasi execute_insert gagal karena mysql error dan rollback dijalankan."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = _make_mysql_error(1062, "Duplicate entry")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_insert(mock_conn, "INSERT INTO table VALUES (%s)", ("val",))
    assert res.is_success is False
    assert 'ERR-DB-002' in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_execute_insert_gagal_exception_umum() -> None:
    """Memverifikasi execute_insert gagal karena exception umum."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = Exception("Unexpected hardware glitch")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_insert(mock_conn, "INSERT INTO table VALUES (%s)", ("val",))
    assert res.is_success is False
    assert 'ERR-DB-002' in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_execute_insert_rollback_error_mysql() -> None:
    """Memverifikasi execute_insert ketika rollback gagal setelah mysql error."""
    mock_conn = MagicMock()
    mock_conn.rollback.side_effect = Exception("Rollback crashed")
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = _make_mysql_error(1062, "Duplicate")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_insert(mock_conn, "INSERT INTO table VALUES (%s)", ("val",))
    assert res.is_success is False
    assert 'ERR-DB-002' in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_execute_insert_rollback_error_general() -> None:
    """Memverifikasi execute_insert ketika rollback gagal setelah exception umum."""
    mock_conn = MagicMock()
    mock_conn.rollback.side_effect = Exception("Rollback crashed")
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = Exception("Fatal write error")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_insert(mock_conn, "INSERT INTO table VALUES (%s)", ("val",))
    assert res.is_success is False
    assert 'ERR-DB-002' in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_execute_many_bulk_insert() -> None:
    """Memverifikasi eksekusi execute_many sukses."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 3
    mock_conn.cursor.return_value = mock_cursor

    data = [("A",), ("B",), ("C",)]
    res = execute_many(mock_conn, "INSERT INTO t (col) VALUES (%s)", data)

    assert res.is_success is True
    assert res.data == 3
    mock_cursor.executemany.assert_called_once_with("INSERT INTO t (col) VALUES (%s)", data)
    mock_conn.commit.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_execute_many_gagal_mysql_error() -> None:
    """Memverifikasi execute_many gagal karena mysql error."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.executemany.side_effect = _make_mysql_error(1215, "Foreign key constraint failure")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_many(mock_conn, "INSERT INTO t (col) VALUES (%s)", [])
    assert res.is_success is False
    assert 'ERR-DB-002' in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_execute_many_gagal_exception_umum() -> None:
    """Memverifikasi execute_many gagal karena exception umum."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.executemany.side_effect = Exception("Bulk parse failed")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_many(mock_conn, "INSERT INTO t (col) VALUES (%s)", [])
    assert res.is_success is False
    assert 'ERR-DB-002' in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_execute_many_rollback_error_mysql() -> None:
    """Memverifikasi execute_many ketika rollback gagal setelah mysql error."""
    mock_conn = MagicMock()
    mock_conn.rollback.side_effect = Exception("Rollback crashed")
    mock_cursor = MagicMock()
    mock_cursor.executemany.side_effect = _make_mysql_error(1215, "Foreign key failure")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_many(mock_conn, "INSERT INTO t (col) VALUES (%s)", [])
    assert res.is_success is False
    assert 'ERR-DB-002' in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_execute_many_rollback_error_general() -> None:
    """Memverifikasi execute_many ketika rollback gagal setelah exception umum."""
    mock_conn = MagicMock()
    mock_conn.rollback.side_effect = Exception("Rollback crashed")
    mock_cursor = MagicMock()
    mock_cursor.executemany.side_effect = Exception("General bulk write failure")
    mock_conn.cursor.return_value = mock_cursor

    res = execute_many(mock_conn, "INSERT INTO t (col) VALUES (%s)", [])
    assert res.is_success is False
    assert 'ERR-DB-002' in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_cursor.close.assert_called_once()


@patch('db.query_builder.get_db_connection')
def test_execute_with_retry_connection_returned_to_pool(mock_get_conn) -> None:
    """Memverifikasi koneksi dikembalikan ke pool melalui close() di blok finally."""
    mock_conn = MagicMock()
    mock_get_conn.return_value = Result(True, mock_conn, None)

    mock_cursor = MagicMock()
    mock_cursor.description = ("col",)
    mock_cursor.fetchall.return_value = []
    mock_conn.cursor.return_value = mock_cursor

    res = execute_with_retry("SELECT 1")
    assert res.is_success is True
    # Pastikan koneksi ditutup (dikembalikan ke pool)
    mock_conn.close.assert_called_once()


@patch('db.query_builder.get_db_connection')
def test_execute_with_retry_koneksi_gagal(mock_get_conn) -> None:
    """Memverifikasi propagasi error ketika gagal mengambil koneksi database."""
    mock_get_conn.return_value = Result(False, None, "ERR-DB-001: Pool has crashed")

    res = execute_with_retry("SELECT 1")
    assert res.is_success is False
    assert "ERR-DB-001" in res.error_msg


@patch('db.query_builder.get_db_connection')
def test_execute_with_retry_pool_return_failure(mock_get_conn) -> None:
    """Memverifikasi exception ditangani ketika gagal menutup/mengembalikan koneksi ke pool."""
    mock_conn = MagicMock()
    mock_conn.close.side_effect = Exception("Pool full or socket issue")
    mock_get_conn.return_value = Result(True, mock_conn, None)

    mock_cursor = MagicMock()
    mock_cursor.description = ("col",)
    mock_cursor.fetchall.return_value = []
    mock_conn.cursor.return_value = mock_cursor

    res = execute_with_retry("SELECT 1")
    assert res.is_success is True  # Query-nya sendiri tetap sukses
    mock_conn.close.assert_called_once()
