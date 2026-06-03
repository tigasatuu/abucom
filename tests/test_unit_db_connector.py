"""
Nama Modul: test_unit_db_connector.py
Deskripsi: Unit test terisolasi (mocked) untuk modul db/db_connector.py.
           Menguji seluruh fungsi connection pool factory, retry mechanism,
           dan koneksi root tanpa memerlukan koneksi database MySQL fisik.
Author: Antigravity AI
Tanggal: 2026-06-04
"""

import time
import pytest
from unittest.mock import patch, MagicMock, PropertyMock
from collections import namedtuple

import db.db_connector as db_mod
from db.db_connector import (
    create_connection_pool,
    get_db_connection,
    close_connection_pool,
    get_root_connection,
    Result,
    MAX_RETRIES,
    RETRY_ERROR_CODES,
)
import mysql.connector


@pytest.fixture(autouse=True)
def reset_connection_pool():
    """Reset variabel modul _connection_pool sebelum dan sesudah setiap test.

    Memastikan setiap test dimulai dari clean state tanpa sisa pool
    dari test sebelumnya.
    """
    db_mod._connection_pool = None
    yield
    db_mod._connection_pool = None


def _make_mysql_error(errno: int, msg: str) -> mysql.connector.Error:
    """Helper untuk membuat mysql.connector.Error dengan errno dan msg."""
    err = mysql.connector.Error()
    err.errno = errno
    err.msg = msg
    return err


# ==============================================================================
# Skenario Test untuk create_connection_pool()
# ==============================================================================

@patch('db.db_connector.pooling.MySQLConnectionPool')
def test_create_connection_pool_sukses_dengan_parameter_valid(mock_pool_cls) -> None:
    """Memverifikasi pembuatan connection pool dengan parameter valid.

    Skenario: Positif
    Target: create_connection_pool
    """
    # Arrange
    mock_pool_instance = MagicMock()
    mock_pool_cls.return_value = mock_pool_instance

    # Act
    res = create_connection_pool(
        host='localhost',
        port=3306,
        user='app',
        password='pass',
        database='db'
    )

    # Assert
    assert res.is_success is True
    assert res.data is mock_pool_instance
    assert res.error_msg is None
    assert db_mod._connection_pool is mock_pool_instance
    mock_pool_cls.assert_called_once_with(
        pool_name='abupool',
        pool_size=5,
        pool_reset_session=True,
        host='localhost',
        port=3306,
        user='app',
        password='pass',
        database='db'
    )


@patch('db.db_connector.pooling.MySQLConnectionPool')
def test_create_connection_pool_sukses_dengan_pool_size_kustom(mock_pool_cls) -> None:
    """Memverifikasi pembuatan connection pool dengan pool_size kustom.

    Skenario: Positif
    Target: create_connection_pool
    """
    # Arrange
    mock_pool_instance = MagicMock()
    mock_pool_cls.return_value = mock_pool_instance

    # Act
    res = create_connection_pool(
        host='localhost',
        port=3306,
        user='app',
        password='pass',
        database='db',
        pool_size=10,
        pool_name='custom_pool'
    )

    # Assert
    assert res.is_success is True
    assert res.data is mock_pool_instance
    mock_pool_cls.assert_called_once_with(
        pool_name='custom_pool',
        pool_size=10,
        pool_reset_session=True,
        host='localhost',
        port=3306,
        user='app',
        password='pass',
        database='db'
    )


@patch('db.db_connector.pooling.MySQLConnectionPool')
def test_create_connection_pool_gagal_mysql_error(mock_pool_cls) -> None:
    """Memverifikasi kegagalan pembuatan pool karena mysql.connector.Error.

    Skenario: Negatif
    Target: create_connection_pool
    """
    # Arrange
    mysql_err = _make_mysql_error(2003, "Connection refused")
    mock_pool_cls.side_effect = mysql_err

    # Act
    res = create_connection_pool(
        host='invalid',
        port=9999,
        user='app',
        password='pass',
        database='db'
    )

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert '2003' in res.error_msg
    assert 'Connection refused' in res.error_msg
    assert db_mod._connection_pool is None


@patch('db.db_connector.pooling.MySQLConnectionPool')
def test_create_connection_pool_gagal_exception_umum(mock_pool_cls) -> None:
    """Memverifikasi kegagalan pembuatan pool karena Exception umum.

    Skenario: Negatif
    Target: create_connection_pool
    """
    # Arrange
    mock_pool_cls.side_effect = Exception("Unexpected error")

    # Act
    res = create_connection_pool(
        host='localhost',
        port=3306,
        user='app',
        password='pass',
        database='db'
    )

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'Unexpected error' in res.error_msg
    assert db_mod._connection_pool is None


# ==============================================================================
# Skenario Test untuk get_db_connection()
# ==============================================================================

def test_get_db_connection_gagal_pool_belum_init() -> None:
    """Memverifikasi error ketika mengambil koneksi sebelum pool diinisialisasi.

    Skenario: Negatif
    Target: get_db_connection
    """
    # Arrange
    assert db_mod._connection_pool is None

    # Act
    res = get_db_connection()

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'belum diinisialisasi' in res.error_msg


def test_get_db_connection_sukses_dari_pool() -> None:
    """Memverifikasi pengambilan koneksi sukses dari pool.

    Skenario: Positif
    Target: get_db_connection
    """
    # Arrange
    mock_pool = MagicMock()
    mock_conn = MagicMock(spec=mysql.connector.MySQLConnection)
    mock_pool.get_connection.return_value = mock_conn
    db_mod._connection_pool = mock_pool

    # Act
    res = get_db_connection()

    # Assert
    assert res.is_success is True
    assert res.data is mock_conn
    assert res.error_msg is None
    mock_pool.get_connection.assert_called_once()


@patch('db.db_connector.time.sleep')
def test_get_db_connection_retry_sukses_setelah_error_2006(mock_sleep) -> None:
    """Memverifikasi retry sukses setelah error 2006 (Server gone away).

    Skenario: Positif / Retry
    Target: get_db_connection
    """
    # Arrange
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(2006, "Server has gone away")
    mock_conn = MagicMock(spec=mysql.connector.MySQLConnection)
    mock_pool.get_connection.side_effect = [mysql_err, mock_conn]
    db_mod._connection_pool = mock_pool

    # Act
    res = get_db_connection()

    # Assert
    assert res.is_success is True
    assert res.data is mock_conn
    assert mock_pool.get_connection.call_count == 2
    mock_sleep.assert_called_once_with(2)  # 2^1 = 2 detik


@patch('db.db_connector.time.sleep')
def test_get_db_connection_retry_sukses_setelah_error_2013(mock_sleep) -> None:
    """Memverifikasi retry sukses setelah error 2013 (Lost connection).

    Skenario: Positif / Retry
    Target: get_db_connection
    """
    # Arrange
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(2013, "Lost connection during query")
    mock_conn = MagicMock(spec=mysql.connector.MySQLConnection)
    mock_pool.get_connection.side_effect = [mysql_err, mock_conn]
    db_mod._connection_pool = mock_pool

    # Act
    res = get_db_connection()

    # Assert
    assert res.is_success is True
    assert res.data is mock_conn
    assert mock_pool.get_connection.call_count == 2
    mock_sleep.assert_called_once_with(2)  # 2^1 = 2 detik


@patch('db.db_connector.time.sleep')
def test_get_db_connection_gagal_setelah_semua_retry_habis(mock_sleep) -> None:
    """Memverifikasi kegagalan mengambil koneksi setelah semua retry habis.

    Skenario: Negatif / Retry
    Target: get_db_connection
    """
    # Arrange
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(2006, "Server has gone away")
    mock_pool.get_connection.side_effect = mysql_err  # Selalu error
    db_mod._connection_pool = mock_pool

    # Act
    res = get_db_connection()

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'Server has gone away' in res.error_msg
    assert mock_pool.get_connection.call_count == MAX_RETRIES

    # sleep dipanggil untuk attempt 1 (2s) dan 2 (4s), tapi tidak di 3 karena loop berakhir
    assert mock_sleep.call_count == 2
    mock_sleep.assert_any_call(2)
    mock_sleep.assert_any_call(4)


def test_get_db_connection_gagal_error_non_retryable() -> None:
    """Memverifikasi error non-retryable langsung gagal tanpa retry.

    Skenario: Negatif
    Target: get_db_connection
    """
    # Arrange
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(1045, "Access denied")
    mock_pool.get_connection.side_effect = mysql_err
    db_mod._connection_pool = mock_pool

    # Act
    res = get_db_connection()

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert '1045' in res.error_msg
    assert 'Access denied' in res.error_msg
    assert mock_pool.get_connection.call_count == 1  # Tidak ada retry


def test_get_db_connection_gagal_exception_umum() -> None:
    """Memverifikasi kegagalan karena exception non-MySQL saat get_connection.

    Skenario: Negatif
    Target: get_db_connection
    """
    # Arrange
    mock_pool = MagicMock()
    mock_pool.get_connection.side_effect = Exception("Pool exhausted")
    db_mod._connection_pool = mock_pool

    # Act
    res = get_db_connection()

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'Pool exhausted' in res.error_msg
    assert mock_pool.get_connection.call_count == 1  # Tidak ada retry


@patch('db.db_connector.time.sleep')
def test_get_db_connection_retry_dengan_max_retries_kustom(mock_sleep) -> None:
    """Memverifikasi retry dengan parameter max_retries kustom.

    Skenario: Edge Case
    Target: get_db_connection
    """
    # Arrange
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(2006, "Server gone")
    mock_pool.get_connection.side_effect = mysql_err
    db_mod._connection_pool = mock_pool

    # Act
    res = get_db_connection(max_retries=1)

    # Assert
    assert res.is_success is False
    assert mock_pool.get_connection.call_count == 1
    assert mock_sleep.call_count == 0


@patch('db.db_connector.time.sleep')
def test_get_db_connection_exponential_backoff_timing(mock_sleep) -> None:
    """Memverifikasi interval exponential backoff (2^attempt) yang tepat.

    Skenario: Validasi
    Target: get_db_connection
    """
    # Arrange
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(2006, "Server gone")
    mock_conn = MagicMock(spec=mysql.connector.MySQLConnection)
    mock_pool.get_connection.side_effect = [mysql_err, mysql_err, mock_conn]
    db_mod._connection_pool = mock_pool

    # Act
    res = get_db_connection()

    # Assert
    assert res.is_success is True
    assert res.data is mock_conn
    assert mock_pool.get_connection.call_count == 3
    assert mock_sleep.call_count == 2
    # Panggilan ke-1: 2^1 = 2 detik
    # Panggilan ke-2: 2^2 = 4 detik
    mock_sleep.assert_any_call(2)
    mock_sleep.assert_any_call(4)


def test_get_db_connection_gagal_max_retries_nol() -> None:
    """Memverifikasi kegagalan mengambil koneksi ketika max_retries bernilai 0.

    Skenario: Edge Case
    Target: get_db_connection
    """
    # Arrange
    mock_pool = MagicMock()
    db_mod._connection_pool = mock_pool

    # Act
    res = get_db_connection(max_retries=0)

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001: Gagal mengambil koneksi dari pool setelah semua retry.' in res.error_msg


# ==============================================================================
# Skenario Test untuk close_connection_pool()
# ==============================================================================

def test_close_connection_pool_sukses_saat_pool_none() -> None:
    """Memverifikasi sukses menutup pool ketika pool sudah None.

    Skenario: Positif
    Target: close_connection_pool
    """
    # Arrange
    db_mod._connection_pool = None

    # Act
    res = close_connection_pool()

    # Assert
    assert res.is_success is True
    assert res.data is None
    assert res.error_msg is None


def test_close_connection_pool_sukses_saat_pool_ada() -> None:
    """Memverifikasi sukses menutup pool dan meremove koneksi yang ada.

    Skenario: Positif
    Target: close_connection_pool
    """
    # Arrange
    mock_pool = MagicMock()
    db_mod._connection_pool = mock_pool

    # Act
    res = close_connection_pool()

    # Assert
    assert res.is_success is True
    assert res.data is None
    assert res.error_msg is None
    mock_pool._remove_connections.assert_called_once()
    assert db_mod._connection_pool is None


def test_close_connection_pool_sukses_tanpa_remove_connections() -> None:
    """Memverifikasi sukses menutup pool yang tidak memiliki method _remove_connections.

    Skenario: Edge Case
    Target: close_connection_pool
    """
    # Arrange
    # mock_pool dibuat tanpa method _remove_connections menggunakan spec
    mock_pool = MagicMock(spec=[])
    db_mod._connection_pool = mock_pool

    # Act
    res = close_connection_pool()

    # Assert
    assert res.is_success is True
    assert db_mod._connection_pool is None


def test_close_connection_pool_gagal_exception() -> None:
    """Memverifikasi kegagalan penutupan pool karena exception.

    Skenario: Negatif
    Target: close_connection_pool
    """
    # Arrange
    mock_pool = MagicMock()
    mock_pool._remove_connections.side_effect = Exception("Cannot remove connections")
    db_mod._connection_pool = mock_pool

    # Act
    res = close_connection_pool()

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'Cannot remove connections' in res.error_msg
    # Pastikan pool tidak di-reset ke None jika terjadi Exception
    assert db_mod._connection_pool is mock_pool


# ==============================================================================
# Skenario Test untuk get_root_connection()
# ==============================================================================

@patch('db.db_connector.mysql.connector.connect')
def test_get_root_connection_sukses(mock_connect) -> None:
    """Memverifikasi sukses mendapatkan koneksi root administratif.

    Skenario: Positif
    Target: get_root_connection
    """
    # Arrange
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn

    # Act
    res = get_root_connection(
        host='localhost',
        port=3306,
        user='root',
        password='rootpassword'
    )

    # Assert
    assert res.is_success is True
    assert res.data is mock_conn
    assert res.error_msg is None
    mock_connect.assert_called_once_with(
        host='localhost',
        port=3306,
        user='root',
        password='rootpassword'
    )


@patch('db.db_connector.mysql.connector.connect')
def test_get_root_connection_gagal_mysql_error(mock_connect) -> None:
    """Memverifikasi kegagalan koneksi root karena MySQL error.

    Skenario: Negatif
    Target: get_root_connection
    """
    # Arrange
    mysql_err = _make_mysql_error(2003, "Connection refused")
    mock_connect.side_effect = mysql_err

    # Act
    res = get_root_connection(
        host='invalid',
        port=9999,
        user='root',
        password='rootpassword'
    )

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'Koneksi administratif gagal' in res.error_msg
    assert '2003' in res.error_msg


@patch('db.db_connector.mysql.connector.connect')
def test_get_root_connection_gagal_exception_umum(mock_connect) -> None:
    """Memverifikasi kegagalan koneksi root karena Exception umum.

    Skenario: Negatif
    Target: get_root_connection
    """
    # Arrange
    mock_connect.side_effect = Exception("DNS Resolution Failure")

    # Act
    res = get_root_connection(
        host='localhost',
        port=3306,
        user='root',
        password='rootpassword'
    )

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'DNS Resolution Failure' in res.error_msg


# ==============================================================================
# Skenario Validasi Konstanta dan Struktur
# ==============================================================================

def test_konstanta_max_retries() -> None:
    """Memverifikasi nilai konstanta MAX_RETRIES.

    Skenario: Validasi
    Target: MAX_RETRIES
    """
    assert MAX_RETRIES == 3


def test_konstanta_retry_error_codes() -> None:
    """Memverifikasi nilai dan isi konstanta RETRY_ERROR_CODES.

    Skenario: Validasi
    Target: RETRY_ERROR_CODES
    """
    assert RETRY_ERROR_CODES == (2006, 2013)
    assert 2006 in RETRY_ERROR_CODES
    assert 2013 in RETRY_ERROR_CODES


def test_result_namedtuple_fields() -> None:
    """Memverifikasi struktur dan field dari NamedTuple Result.

    Skenario: Validasi
    Target: Result
    """
    assert Result._fields == ('is_success', 'data', 'error_msg')
    res_ok = Result(True, "some_data", None)
    assert res_ok.is_success is True
    assert res_ok.data == "some_data"
    assert res_ok.error_msg is None

    res_fail = Result(False, None, "error_occurred")
    assert res_fail.is_success is False
    assert res_fail.data is None
    assert res_fail.error_msg == "error_occurred"
