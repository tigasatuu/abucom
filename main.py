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


def validate_env_file() -> bool:
    """Memvalidasi keberadaan file konfigurasi .env di root proyek.

    Returns:
        bool: True jika file .env ditemukan, False jika tidak.
    """
    env_path = Path(__file__).parent / '.env'
    if not env_path.exists():
        print("⛔ ERR-FILE-001: File .env tidak ditemukan di root proyek.")
        print("   Salin file .env.example menjadi .env dan lengkapi kredensial.")
        return False
    return True


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

    # Tahap 1: Validasi keberadaan file konfigurasi .env
    if not validate_env_file():
        sys.exit(1)

    # Tahap 2: Muat konfigurasi dari .env
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

    # Tahap 4: Peluncuran antarmuka CLI login
    # TODO: Implementasi pemanggilan cli/__init__.py -> start_cli_app()

    print("[INFO] Scaffolding berhasil. Modul belum diimplementasikan.")
    print("[INFO] Tekan Enter untuk keluar...")
    input()

    # Cleanup: Tutup connection pool saat aplikasi ditutup
    close_connection_pool()


if __name__ == '__main__':
    main()
