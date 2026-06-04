"""
Nama Modul: query_builder.py
Deskripsi: Wrapper eksekusi query SQL aman terparameter (%s bindings)
           dan block penjamin atomik ACID transaksi InnoDB.
           Mendukung operasi SELECT, INSERT, UPDATE, DELETE dengan
           penanganan error fungsional Result Pattern.
Author: Claude Sonnet 4.6 (STK-004)
Tanggal: 2026-06-04
"""

# 1. Standard Library
import logging
from collections import namedtuple
from typing import Callable, Any

# 2. Third-Party
import mysql.connector

# 3. Local Modules
from db.db_connector import get_db_connection

# Logger configuration
_logger = logging.getLogger('abucom.db.query')

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


def execute_query(
    db_connection,
    query: str,
    params: tuple | None = None,
    fetch_one: bool = False,
    fetch_all: bool = True
) -> Result:
    """Mengeksekusi query SQL tunggal dengan parameterized bindings %s.

    Args:
        db_connection: Objek koneksi database aktif dari pool.
        query (str): String query SQL dengan placeholder %s.
        params (tuple | None): Parameter binding untuk query.
        fetch_one (bool): Jika True, hanya mengambil baris pertama hasil SELECT.
        fetch_all (bool): Jika True, mengambil semua baris hasil SELECT (diabaikan jika fetch_one=True).

    Returns:
        Result: NamedTuple berisi status eksekusi query.

    Example:
        >>> conn = get_db_connection().data
        >>> execute_query(conn, "SELECT * FROM pengguna WHERE id = %s", (1,), fetch_one=True)
        Result(is_success=True, data={'id': 1, 'username': 'pemilik_toko'}, error_msg=None)
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(query, params)

        if cursor.description is not None:
            # Query menghasilkan data (SELECT, SHOW, DESCRIBE, dll.)
            if fetch_one:
                data = cursor.fetchone()
            elif fetch_all:
                data = cursor.fetchall()
            else:
                data = None
        else:
            # DML/DDL query (INSERT, UPDATE, DELETE, dll.) yang dieksekusi langsung
            db_connection.commit()
            data = cursor.rowcount

        return Result(True, data, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def execute_acid_transaction(
    db_connection,
    operations: list[Callable[[Any], Any]]
) -> Result:
    """Wrapper fungsional penjamin transaksi ACID rollback/commit InnoDB.

    Args:
        db_connection: Objek koneksi database aktif dari pool.
        operations (list[Callable]): Daftar fungsi operasi yang dieksekusi atomik.
                                     Setiap fungsi menerima satu parameter berupa objek cursor.

    Returns:
        Result: NamedTuple berisi status transaksi dan hasil operasi.

    Example:
        >>> def update_stok(cursor):
        ...     cursor.execute("UPDATE barang SET stok = stok - %s WHERE id = %s", (10, 1))
        ...     return cursor.rowcount
        >>> conn = get_db_connection().data
        >>> execute_acid_transaction(conn, [update_stok])
        Result(is_success=True, data=[1], error_msg=None)
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        db_connection.start_transaction()
        results = [op(cursor) for op in operations]
        db_connection.commit()
        return Result(True, results, None)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception as rollback_err:
            _logger.warning(f"Gagal melakukan rollback: {str(rollback_err)}")
        error_msg = f"ERR-DB-TX: Transaksi dibatalkan secara aman. Detail: {str(e)}"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def execute_insert(
    db_connection,
    query: str,
    params: tuple | None = None
) -> Result:
    """Mengeksekusi INSERT query dan mengembalikan lastrowid.

    Args:
        db_connection: Objek koneksi database aktif.
        query (str): Query INSERT SQL.
        params (tuple | None): Parameter binding untuk query.

    Returns:
        Result: NamedTuple berisi status dan ID baris terakhir (lastrowid).

    Example:
        >>> conn = get_db_connection().data
        >>> execute_insert(conn, "INSERT INTO cabang (nama) VALUES (%s)", ("Cabang Baru",))
        Result(is_success=True, data=2, error_msg=None)
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(query, params)
        db_connection.commit()
        return Result(True, cursor.lastrowid, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi INSERT gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi INSERT gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def execute_many(
    db_connection,
    query: str,
    data_list: list[tuple]
) -> Result:
    """Mengeksekusi INSERT massal menggunakan cursor.executemany().

    Args:
        db_connection: Objek koneksi database aktif.
        query (str): Query INSERT SQL dengan binding %s.
        data_list (list[tuple]): Daftar tuple data yang akan dimasukkan.

    Returns:
        Result: NamedTuple berisi status dan jumlah total baris yang dimasukkan.

    Example:
        >>> conn = get_db_connection().data
        >>> data = [("Barang A",), ("Barang B",)]
        >>> execute_many(conn, "INSERT INTO barang (nama) VALUES (%s)", data)
        Result(is_success=True, data=2, error_msg=None)
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.executemany(query, data_list)
        db_connection.commit()
        return Result(True, cursor.rowcount, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi bulk insert gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi bulk insert gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def execute_with_retry(
    query: str,
    params: tuple | None = None,
    fetch_one: bool = False,
    fetch_all: bool = True,
    max_retries: int = 3
) -> Result:
    """Mengeksekusi query database dengan retry otomatis pada koneksi pool.

    Args:
        query (str): Query SQL.
        params (tuple | None): Parameter query.
        fetch_one (bool): Ambil satu baris saja.
        fetch_all (bool): Ambil semua baris.
        max_retries (int): Maksimum percobaan koneksi.

    Returns:
        Result: NamedTuple berisi status dan hasil eksekusi.

    Example:
        >>> execute_with_retry("SELECT * FROM pengguna WHERE id = %s", (1,), fetch_one=True)
        Result(is_success=True, data={'id': 1, 'username': 'pemilik_toko'}, error_msg=None)
    """
    conn_res = get_db_connection(max_retries=max_retries)
    if not conn_res.is_success:
        return conn_res

    conn = conn_res.data
    try:
        return execute_query(
            db_connection=conn,
            query=query,
            params=params,
            fetch_one=fetch_one,
            fetch_all=fetch_all
        )
    finally:
        try:
            conn.close()  # Mengembalikan koneksi ke pool
        except Exception as e:
            _logger.warning(f"Gagal mengembalikan koneksi ke pool (Detail Error: {str(e)})")
