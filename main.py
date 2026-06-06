"""
Nama Modul: main.py
Deskripsi: Entry point utama peluncuran aplikasi CLI AbuCom.
           Memvalidasi kelengkapan file .env, menginisialisasi koneksi database,
           dan meluncurkan antarmuka login terminal CLI.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import sys
import os
from pathlib import Path


def main() -> None:
    """Fungsi utama entry point aplikasi AbuCom CLI."""
    if sys.platform.startswith('win'):
        # Force UTF-8 encoding on Windows console to prevent UnicodeEncodeError with emojis
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            pass

    print("=" * 60)
    print("  AbuCom — Sistem Manajemen Terpadu Usaha Percetakan")
    print("=" * 60)
    print()

    # Tahap 1: Muat dan validasi konfigurasi dari .env
    from config.settings import load_settings
    config = load_settings()
    print(f'[INFO] Konfigurasi dimuat. Cabang ID: {config.app_cabang_id}')
    print(f'[INFO] Target database: {config.db_name}@{config.db_host}:{config.db_port}')

    # Tahap 3: Inisialisasi koneksi database pool
    from db.db_connector import create_connection_pool, close_connection_pool
    pool_result = create_connection_pool(
        host=config.db_host,
        port=config.db_port,
        user=config.db_user,
        password=config.db_password,
        database=config.db_name,
        pool_size=config.db_pool_size,
    )
    if not pool_result.is_success:
        print(f'⛔ {pool_result.error_msg}')
        print('   Pastikan MySQL Server aktif dan kredensial di .env sudah benar.')
        sys.exit(1)
    print('[INFO] Connection pool database berhasil diinisialisasi (abupool).')

    # Muat parameter runtime bisnis dari database ke cache memori lokal
    from db.db_connector import get_db_connection
    from db.config_cache import load_all_configs
    conn_res = get_db_connection()
    if not conn_res.is_success:
        print(f"⛔ {conn_res.error_msg}")
        sys.exit(1)
    db_connection = conn_res.data
    
    config_result = load_all_configs(db_connection, config.app_cabang_id)
    try:
        db_connection.close()  # Kembalikan koneksi ke pool
    except Exception:
        pass

    if not config_result.is_success:
        print(f"⛔ {config_result.error_msg}")
        sys.exit(1)
    print(f'[INFO] Config runtime: {config_result.data} parameter berhasil dimuat ke cache.')

    # Tahap 4: Peluncuran antarmuka CLI login
    from cli import start_cli_app
    print('[INFO] Meluncurkan antarmuka CLI login...')
    print()
    start_cli_app()

    # Cleanup: Tutup connection pool saat aplikasi ditutup
    close_connection_pool()


if __name__ == '__main__':
    main()
