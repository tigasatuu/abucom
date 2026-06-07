"""
Nama Modul: test_dashboard_queries.py
Deskripsi: Unit/Integration testing untuk fungsi query dashboard baru
           pada db/query_builder.py.
Author: Antigravity
Tanggal: 2026-06-07
"""

import pytest
import mysql.connector
from datetime import date
from config.settings import load_settings
from db.db_connector import get_db_connection, close_connection_pool
from db.query_builder import (
    query_dashboard_pemilik,
    query_dashboard_kasir,
    query_dashboard_operasional,
    query_dashboard_kepala,
    query_dashboard_gudang,
    query_dashboard_pramuniaga,
    query_dashboard_fotocopy
)

# Load settings for testing
try:
    _config = load_settings()
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


@pytest.mark.skipif(not _db_available, reason="Database tidak tersedia")
def test_dashboard_queries_success() -> None:
    """Memverifikasi bahwa seluruh fungsi query dashboard berhasil dieksekusi."""
    from db.db_connector import create_connection_pool
    create_connection_pool(
        host=_config.db_host,
        port=_config.db_port,
        user=_config.db_user,
        password=_config.db_password,
        database=_config.db_name
    )
    conn_res = get_db_connection()
    assert conn_res.is_success is True
    conn = conn_res.data
    
    tanggal_hari_ini = date.today().isoformat()
    cabang_id = 1
    user_id = 1 # Fallback valid user ID

    try:
        # 1. Pemilik
        res_pemilik = query_dashboard_pemilik(conn, cabang_id, tanggal_hari_ini)
        assert res_pemilik.is_success is True
        assert 'total_pendapatan' in res_pemilik.data
        assert 'total_pengeluaran' in res_pemilik.data
        assert 'total_limbah' in res_pemilik.data
        assert 'status_transaksi' in res_pemilik.data
        assert 'alert_bank' in res_pemilik.data
        assert 'alert_supplier' in res_pemilik.data

        # 2. Kasir
        res_kasir = query_dashboard_kasir(conn, user_id, cabang_id, tanggal_hari_ini)
        assert res_kasir.is_success is True
        assert 'jumlah_nota' in res_kasir.data
        assert 'total_kas' in res_kasir.data
        assert 'jumlah_belum_lunas' in res_kasir.data
        assert 'saldo_ppob' in res_kasir.data

        # 3. Operasional
        res_ops = query_dashboard_operasional(conn, cabang_id)
        assert res_ops.is_success is True
        assert 'antrian' in res_ops.data
        assert 'stok_kritis' in res_ops.data

        # 4. Kepala
        res_kepala = query_dashboard_kepala(conn, cabang_id, tanggal_hari_ini)
        assert res_kepala.is_success is True
        assert 'jumlah_hadir' in res_kepala.data
        assert 'total_staf' in res_kepala.data
        assert 'draf_pending' in res_kepala.data
        assert 'antrian' in res_kepala.data

        # 5. Gudang
        res_gudang = query_dashboard_gudang(conn, cabang_id)
        assert res_gudang.is_success is True
        assert 'stok_kritis' in res_gudang.data
        assert 'draf_pending' in res_gudang.data
        assert 'utang_supplier' in res_gudang.data

        # 6. Pramuniaga
        res_pramuniaga = query_dashboard_pramuniaga(conn, cabang_id)
        assert res_pramuniaga.is_success is True
        assert 'jumlah_antri' in res_pramuniaga.data

        # 7. Fotocopy
        res_fotocopy = query_dashboard_fotocopy(conn, user_id, cabang_id, tanggal_hari_ini)
        assert res_fotocopy.is_success is True
        assert 'jumlah_nota' in res_fotocopy.data
        assert 'total_kas' in res_fotocopy.data

    finally:
        conn.close()
