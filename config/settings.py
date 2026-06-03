"""
Nama Modul: settings.py
Deskripsi: Agregasi dan casting data bertipe aman dari file kredensial
           rahasia lokal .env menggunakan library python-dotenv.
           Menyediakan variabel konfigurasi sebagai read-only dictionary.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import os
import sys
from pathlib import Path
from collections import namedtuple

from dotenv import load_dotenv


# Konstanta konfigurasi default
DEFAULT_DB_HOST = '10.10.10.10'
DEFAULT_DB_PORT = 3306
DEFAULT_DB_POOL_SIZE = 5
DEFAULT_JWT_LIFETIME = 28800
DEFAULT_PRINTER_WIDTH = 58

# NamedTuple imutabel untuk konfigurasi runtime
AppConfig = namedtuple('AppConfig', [
    'app_env',
    'app_cabang_id',
    'db_host',
    'db_port',
    'db_user',
    'db_password',
    'db_name',
    'db_pool_size',
    'jwt_secret_key',
    'jwt_lifetime_seconds',
    'fernet_key',
    'backup_zip_password',
    'printer_port',
    'printer_width_mm',
])


def load_settings() -> AppConfig:
    """Memuat dan memvalidasi seluruh variabel konfigurasi dari file .env.

    Returns:
        AppConfig: NamedTuple imutabel berisi seluruh konfigurasi runtime.

    Raises:
        SystemExit: Jika file .env tidak ditemukan atau variabel wajib kosong.
    """
    env_path = Path(__file__).parent.parent / '.env'

    if not env_path.exists():
        print("⛔ ERR-FILE-001: File .env tidak ditemukan.")
        sys.exit(1)

    load_dotenv(dotenv_path=str(env_path))

    # Validasi variabel wajib tidak boleh kosong
    required_vars = ['DB_PASSWORD', 'JWT_SECRET_KEY', 'FERNET_KEY']
    for var_name in required_vars:
        if not os.getenv(var_name) or os.getenv(var_name, '').startswith('YOUR_'):
            print(f"⛔ ERR-FILE-002: Variabel {var_name} belum diisi di file .env.")
            sys.exit(1)

    return AppConfig(
        app_env=os.getenv('APP_ENV', 'development'),
        app_cabang_id=int(os.getenv('APP_CABANG_ID', '1')),
        db_host=os.getenv('DB_HOST', DEFAULT_DB_HOST),
        db_port=int(os.getenv('DB_PORT', str(DEFAULT_DB_PORT))),
        db_user=os.getenv('DB_USER', 'abucom_app'),
        db_password=os.getenv('DB_PASSWORD', ''),
        db_name=os.getenv('DB_NAME', 'abucom_db'),
        db_pool_size=int(os.getenv('DB_POOL_SIZE', str(DEFAULT_DB_POOL_SIZE))),
        jwt_secret_key=os.getenv('JWT_SECRET_KEY', ''),
        jwt_lifetime_seconds=int(os.getenv('JWT_LIFETIME_SECONDS', str(DEFAULT_JWT_LIFETIME))),
        fernet_key=os.getenv('FERNET_KEY', ''),
        backup_zip_password=os.getenv('BACKUP_ZIP_PASSWORD', ''),
        printer_port=os.getenv('PRINTER_PORT', 'COM1'),
        printer_width_mm=int(os.getenv('PRINTER_WIDTH_MM', str(DEFAULT_PRINTER_WIDTH))),
    )
