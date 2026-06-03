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
RETRY_ERROR_CODES = (2006, 2013)

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
        error_msg = f"ERR-DB-001: Gagal menginisialisasi connection pool (MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-001: Gagal menginisialisasi connection pool (Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)


def get_db_connection(max_retries: int = MAX_RETRIES) -> Result:
    """Mengambil koneksi aktif dari pool dengan retry exponential backoff.

    Retry dilakukan 3 kali dengan interval 2^attempt detik (2s, 4s, 8s)
    saat menangkap MySQL error code 2006 atau 2013.

    Args:
        max_retries (int): Jumlah maksimum percobaan ulang (default 3).

    Returns:
        Result: NamedTuple berisi koneksi database atau pesan error.
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
                    wait_time = 2 ** attempt
                    _logger.warning(
                        f"Koneksi terputus (Error {e.errno}). Mencoba ulang dalam {wait_time} detik..."
                    )
                    time.sleep(wait_time)
                    continue
            error_msg = f"ERR-DB-001: Gagal mengambil koneksi dari pool (MySQL Error {e.errno}: {e.msg})"
            _logger.error(error_msg)
            return Result(False, None, error_msg)
        except Exception as e:
            error_msg = f"ERR-DB-001: Gagal mengambil koneksi dari pool (Error: {str(e)})"
            _logger.error(error_msg)
            return Result(False, None, error_msg)

    return Result(False, None, 'ERR-DB-001: Gagal mengambil koneksi dari pool setelah semua retry.')


def close_connection_pool() -> Result:
    """Menutup connection pool database secara aman.

    Returns:
        Result: NamedTuple berisi status penutupan pool.
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
        error_msg = f"ERR-DB-001: Gagal menutup connection pool (Error: {str(e)})"
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
        error_msg = f"ERR-DB-001: Koneksi administratif gagal (MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-001: Koneksi administratif gagal (Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
