"""
Nama Modul: test_db_connection.py
Deskripsi: Integration testing koneksi database MySQL dan verifikasi
           integritas skema 28 tabel multi-cabang AbuCom.
Author: Claude Sonnet 4.6 (STK-004)
Tanggal: 2026-06-03
"""

import os
from pathlib import Path
import pytest
import mysql.connector

from config.settings import load_settings
from db.db_connector import (
    create_connection_pool,
    get_db_connection,
    close_connection_pool,
    get_root_connection
)
from db.schema_initializer import (
    read_sql_file,
    verify_schema_integrity,
    EXPECTED_TABLE_COUNT,
    EXPECTED_SEED_COUNTS
)

# Load settings for testing
try:
    _config = load_settings()
    # Check if database is reachable
    _conn = mysql.connector.connect(
        host=_config.db_host,
        port=_config.db_port,
        user=_config.db_user,
        password=_config.db_password,
        database=_config.db_name
    )
    _conn.close()
    _db_available = True
except Exception:
    _db_available = False


@pytest.fixture(autouse=True)
def setup_teardown_pool() -> None:
    """Fixture to ensure connection pool is closed after each test."""
    yield
    close_connection_pool()


def test_read_sql_file_valid_path() -> None:
    """Memverifikasi pembacaan file SQL dengan path valid."""
    schema_path = Path(__file__).parent.parent / 'schema.sql'
    res = read_sql_file(str(schema_path))
    assert res.is_success is True
    assert len(res.data) > 0


def test_read_sql_file_invalid_path() -> None:
    """Memverifikasi penanganan error saat membaca file SQL dari path tidak valid."""
    res = read_sql_file('nonexistent_schema_file.sql')
    assert res.is_success is False
    assert 'ERR-FILE-003' in res.error_msg


@pytest.mark.skipif(not _db_available, reason="Database tidak tersedia")
def test_create_connection_pool_with_valid_config() -> None:
    """Memverifikasi pembuatan connection pool dengan konfigurasi valid."""
    res = create_connection_pool(
        host=_config.db_host,
        port=_config.db_port,
        user=_config.db_user,
        password=_config.db_password,
        database=_config.db_name,
        pool_size=_config.db_pool_size
    )
    assert res.is_success is True
    assert res.data is not None


def test_create_connection_pool_with_invalid_host() -> None:
    """Memverifikasi penanganan error pembuatan pool dengan host tidak valid."""
    # Use a dummy non-resolving IP/hostname or invalid port to trigger error
    res = create_connection_pool(
        host='192.0.2.1',  # Test/documentation dummy IP (no host)
        port=9999,
        user='invalid_user',
        password='invalid_password',
        database='invalid_db',
        pool_size=1
    )
    assert res.is_success is False
    assert 'ERR-DB-001' in res.error_msg


@pytest.mark.skipif(not _db_available, reason="Database tidak tersedia")
def test_get_db_connection_returns_active_connection() -> None:
    """Memverifikasi pengambilan koneksi aktif dari pool."""
    create_connection_pool(
        host=_config.db_host,
        port=_config.db_port,
        user=_config.db_user,
        password=_config.db_password,
        database=_config.db_name
    )
    res = get_db_connection()
    assert res.is_success is True
    conn = res.data
    assert conn.is_connected() is True
    conn.close()


@pytest.mark.skipif(not _db_available, reason="Database tidak tersedia")
def test_schema_has_28_tables() -> None:
    """Memverifikasi jumlah tabel hasil inisialisasi adalah 28."""
    conn = mysql.connector.connect(
        host=_config.db_host,
        port=_config.db_port,
        user=_config.db_user,
        password=_config.db_password,
        database=_config.db_name
    )
    res = verify_schema_integrity(conn)
    conn.close()
    assert res.is_success is True
    assert res.data['tables'] == EXPECTED_TABLE_COUNT


@pytest.mark.skipif(not _db_available, reason="Database tidak tersedia")
def test_seed_data_cabang_count() -> None:
    """Memverifikasi jumlah seed data cabang."""
    conn = mysql.connector.connect(
        host=_config.db_host,
        port=_config.db_port,
        user=_config.db_user,
        password=_config.db_password,
        database=_config.db_name
    )
    res = verify_schema_integrity(conn)
    conn.close()
    assert res.is_success is True
    assert res.data['seeds']['cabang'] == EXPECTED_SEED_COUNTS['cabang']


@pytest.mark.skipif(not _db_available, reason="Database tidak tersedia")
def test_seed_data_pengguna_count() -> None:
    """Memverifikasi jumlah seed data pengguna."""
    conn = mysql.connector.connect(
        host=_config.db_host,
        port=_config.db_port,
        user=_config.db_user,
        password=_config.db_password,
        database=_config.db_name
    )
    res = verify_schema_integrity(conn)
    conn.close()
    assert res.is_success is True
    assert res.data['seeds']['pengguna'] == EXPECTED_SEED_COUNTS['pengguna']


@pytest.mark.skipif(not _db_available, reason="Database tidak tersedia")
def test_seed_data_system_configs_count() -> None:
    """Memverifikasi jumlah seed data system_configs."""
    conn = mysql.connector.connect(
        host=_config.db_host,
        port=_config.db_port,
        user=_config.db_user,
        password=_config.db_password,
        database=_config.db_name
    )
    res = verify_schema_integrity(conn)
    conn.close()
    assert res.is_success is True
    assert res.data['seeds']['system_configs'] == EXPECTED_SEED_COUNTS['system_configs']


@pytest.mark.skipif(not _db_available, reason="Database tidak tersedia")
def test_composite_index_exists_on_transaksi() -> None:
    """Memverifikasi composite index pada tabel transaksi."""
    conn = mysql.connector.connect(
        host=_config.db_host,
        port=_config.db_port,
        user=_config.db_user,
        password=_config.db_password,
        database=_config.db_name
    )
    cursor = conn.cursor()
    cursor.execute("SHOW INDEX FROM transaksi")
    indexes = [r[2] for r in cursor.fetchall()]
    cursor.close()
    conn.close()
    assert 'idx_transaksi_tanggal_cabang' in indexes
