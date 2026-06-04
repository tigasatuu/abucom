"""
Nama Modul: db_connector.py
Deskripsi: Inisialisasi connection pool database MySQL lokal menggunakan
           driver mysql-connector-python. Implementasi retry otomatis
           dengan exponential backoff saat menangkap error MySQL 2006/2013.
Author: Claude Sonnet 4.6 (STK-004)
Tanggal: 2026-06-03
"""

import time
import logging
from collections import namedtuple
import mysql.connector
from mysql.connector import pooling

# Logger configuration
_logger = logging.getLogger('abucom.db')

# Konstanta retry mechanism
MAX_RETRIES = 3
RETRY_BASE_SECONDS = 2
RETRY_ERROR_CODES = (2006, 2013)
POOL_EXHAUSTED_ERROR_CODE = -1

# NOTE: MySQLConnectionPool dari mysql-connector-python sudah bersifat thread-safe.
# Pada sistem CLI single-threaded AbuCom, pool_size=5 menyediakan redundansi
# jika ada koneksi yang gagal di-close karena error tak terduga.

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])

# Variabel modul-level untuk menyimpan referensi pool (FP: closure-like state)
_connection_pool = None


def create_connection_pool(
    host: str,
    port: int,
    user: str,
    password: str,
    database: str,
    pool_size: int = 5,
    pool_name: str = 'abupool'
) -> Result:
    """Membuat connection pool database MySQL lokal.

    Args:
        host (str): Alamat IP statis server database.
        port (int): Port database MySQL.
        user (str): Username database.
        password (str): Password database.
        database (str): Nama database target.
        pool_size (int): Jumlah koneksi dalam pool (default 5).
        pool_name (str): Nama identifikasi pool (default 'abupool').

    Returns:
        Result: NamedTuple berisi status koneksi pool.

    Example:
        >>> create_connection_pool(
        ...     host='localhost',
        ...     port=3306,
        ...     user='abucom_app',
        ...     password='password123',
        ...     database='abucom_db'
        ... )
        Result(is_success=True, data=<...>, error_msg=None)
    """
    global _connection_pool
    try:
        _connection_pool = pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        return Result(True, _connection_pool, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-001: Gagal menginisialisasi connection pool (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-001: Gagal menginisialisasi connection pool (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)


def get_db_connection(max_retries: int = MAX_RETRIES) -> Result:
    """Mengambil koneksi aktif dari pool dengan retry exponential backoff.

    Retry dilakukan 3 kali dengan interval RETRY_BASE_SECONDS^attempt detik (2s, 4s, 8s)
    saat menangkap MySQL error code 2006 atau 2013.

    Args:
        max_retries (int): Jumlah maksimum percobaan ulang (default 3).

    Returns:
        Result: NamedTuple berisi koneksi database atau pesan error.

    Example:
        >>> conn_res = get_db_connection()
        >>> if conn_res.is_success:
        ...     conn = conn_res.data
    """
    global _connection_pool
    if _connection_pool is None:
        return Result(False, None, 'ERR-DB-001: Connection pool belum diinisialisasi.')

    for attempt in range(1, max_retries + 1):
        try:
            conn = _connection_pool.get_connection()
            return Result(True, conn, None)
        except mysql.connector.Error as e:
            if e.errno in RETRY_ERROR_CODES:
                if attempt < max_retries:
                    wait_time = RETRY_BASE_SECONDS ** attempt
                    _logger.warning(
                        f"Koneksi terputus (Error {e.errno}). Mencoba ulang dalam {wait_time} detik..."
                    )
                    # NOTE: Sistem AbuCom CLI ini berjalan single-threaded pada client terminal kasir.
                    # Blocking sleep selama retry interval dapat diterima karena tidak memblokir
                    # operasi thread/user lain secara paralel.
                    time.sleep(wait_time)
                    continue
            error_msg = f"ERR-DB-001: Gagal mengambil koneksi dari pool (Detail Error: MySQL Error {e.errno}: {e.msg})"
            _logger.error(error_msg)
            return Result(False, None, error_msg)
        except Exception as e:
            error_msg = f"ERR-DB-001: Gagal mengambil koneksi dari pool (Detail Error: {str(e)})"
            _logger.error(error_msg)
            return Result(False, None, error_msg)

    return Result(False, None, 'ERR-DB-001: Gagal mengambil koneksi dari pool setelah semua retry.')


def close_connection_pool() -> Result:
    """Menutup connection pool database secara aman.

    Returns:
        Result: NamedTuple berisi status penutupan pool.

    Example:
        >>> close_connection_pool()
        Result(is_success=True, data=None, error_msg=None)
    """
    global _connection_pool
    if _connection_pool is None:
        return Result(True, None, None)
    try:
        if hasattr(_connection_pool, '_remove_connections'):
            _connection_pool._remove_connections()
        _connection_pool = None
        return Result(True, None, None)
    except Exception as e:
        error_msg = f"ERR-DB-001: Gagal menutup connection pool (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)


def get_root_connection(
    host: str,
    port: int,
    user: str,
    password: str
) -> Result:
    """Membuat koneksi langsung (non-pool) ke MySQL sebagai root untuk eksekusi DDL.

    Fungsi ini digunakan KHUSUS untuk inisialisasi schema awal
    yang memerlukan privilege CREATE/DROP TABLE.
    TIDAK menggunakan connection pool.

    Args:
        host (str): Alamat IP statis server database.
        port (int): Port database MySQL.
        user (str): Username root MySQL.
        password (str): Password root MySQL.

    Returns:
        Result: NamedTuple berisi koneksi root atau pesan error.

    Example:
        >>> get_root_connection(
        ...     host='localhost',
        ...     port=3306,
        ...     user='root',
        ...     password='rootpassword'
        ... )
        Result(is_success=True, data=<...>, error_msg=None)
    """
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password
        )
        return Result(True, conn, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-001: Koneksi administratif gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-001: Koneksi administratif gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)


def get_pool_status() -> Result:
    """Mengembalikan status informasi connection pool aktif.

    Fungsi ini digunakan untuk monitoring dan debugging status connection pool.

    Returns:
        Result: NamedTuple berisi status boolean sukses, dictionary status pool,
                dan pesan error jika ada.

    Example:
        >>> get_pool_status()
        Result(is_success=True, data={'pool_name': 'abupool', 'pool_size': 5, 'is_active': True}, error_msg=None)
    """
    global _connection_pool
    try:
        if _connection_pool is None:
            return Result(True, {
                'pool_name': None,
                'pool_size': 0,
                'is_active': False
            }, None)

        return Result(True, {
            'pool_name': _connection_pool.pool_name,
            'pool_size': _connection_pool.pool_size,
            'is_active': True
        }, None)
    except Exception as e:
        error_msg = f"ERR-DB-001: Gagal mendapatkan status connection pool (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
