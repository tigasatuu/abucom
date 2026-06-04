"""
Nama Modul: settings.py
Deskripsi: Agregasi dan casting data bertipe aman dari file kredensial
           rahasia lokal .env menggunakan library python-dotenv.
           Menyediakan variabel konfigurasi sebagai read-only NamedTuple imutabel.
Author: Antigravity AI
Tanggal: 2026-06-04
"""

# 1. Standard Library
import logging
import os
import sys
from collections import namedtuple
from pathlib import Path

# 2. Third-Party
from dotenv import load_dotenv

# 3. Local Modules (Tidak ada untuk settings.py)

# Logger instansiasi untuk modul konfigurasi
_logger = logging.getLogger('abucom.config')

# Konstanta konfigurasi default
DEFAULT_DB_HOST = '10.10.10.10'
DEFAULT_DB_PORT = 3306
DEFAULT_DB_POOL_SIZE = 5
DEFAULT_JWT_LIFETIME = 28800
DEFAULT_PRINTER_WIDTH = 58

VALID_APP_ENVS = ('development', 'production')
VALID_PRINTER_WIDTHS = (58, 80)
REQUIRED_ENV_VARS = ('DB_PASSWORD', 'JWT_SECRET_KEY', 'FERNET_KEY', 'BACKUP_ZIP_PASSWORD')

# [DATA-KOSONG] Nilai default untuk DB_HOST tidak konsisten antara
# settings.py ('10.10.10.10') dan .env.example ('192.168.1.200').
# Perlu konfirmasi dari pemilik proyek untuk menentukan default yang benar.
# Saat ini menggunakan '10.10.10.10' sesuai kode existing.

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


def _safe_int_cast(value: str | None, default: int, var_name: str) -> int:
    """Melakukan casting string ke integer secara aman dengan fallback default.

    Args:
        value (str | None): Nilai string dari os.getenv().
        default (int): Nilai default jika casting gagal atau None.
        var_name (str): Nama variabel untuk pesan error.

    Returns:
        int: Nilai integer hasil casting atau default.

    Raises:
        SystemExit: Jika nilai tidak valid dan tidak bisa di-cast.
    """
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        _logger.error(
            f"ERR-FILE-003: Variabel {var_name} bernilai '{value}' bukan integer valid."
        )
        print(f"⛔ ERR-FILE-003: Variabel {var_name} bernilai '{value}' bukan integer valid di file .env.")
        sys.exit(1)


def _validate_int_range(value: int, min_val: int, max_val: int, var_name: str) -> int:
    """Memvalidasi nilai integer berada dalam rentang yang diizinkan.

    Args:
        value (int): Nilai integer yang akan divalidasi.
        min_val (int): Batas minimum (inklusif).
        max_val (int): Batas maksimum (inklusif).
        var_name (str): Nama variabel untuk pesan error.

    Returns:
        int: Nilai integer yang sudah tervalidasi.

    Raises:
        SystemExit: Jika nilai di luar rentang yang diizinkan.
    """
    if not (min_val <= value <= max_val):
        _logger.error(
            f"ERR-FILE-004: Variabel {var_name} bernilai {value}, di luar rentang {min_val}-{max_val}."
        )
        print(f"⛔ ERR-FILE-004: Variabel {var_name} bernilai {value}, di luar rentang {min_val}-{max_val}.")
        sys.exit(1)
    return value


def load_settings() -> AppConfig:
    """Memuat, memvalidasi, dan meng-cast seluruh variabel konfigurasi dari file .env.

    Fungsi ini melakukan 4 tahapan validasi berurutan:
    1. Memverifikasi keberadaan fisik file .env di root proyek.
    2. Memvalidasi variabel wajib tidak kosong dan tidak placeholder.
    3. Memvalidasi tipe data casting ke integer untuk variabel numerik.
    4. Memvalidasi rentang nilai untuk variabel tertentu.

    Returns:
        AppConfig: NamedTuple imutabel berisi seluruh 14 konfigurasi runtime.

    Raises:
        SystemExit: Jika file .env tidak ditemukan (ERR-FILE-001),
                    variabel wajib kosong (ERR-FILE-002),
                    tipe data tidak valid (ERR-FILE-003),
                    nilai di luar rentang (ERR-FILE-004),
                    atau APP_ENV tidak valid (ERR-FILE-005).

    Example:
        >>> config = load_settings()
        >>> config.app_env
        'development'
        >>> config.db_port
        3306
    """
    env_path = Path(__file__).parent.parent / '.env'

    if not env_path.exists():
        _logger.error(f"ERR-FILE-001: File .env tidak ditemukan di {env_path}.")
        print("⛔ ERR-FILE-001: File .env tidak ditemukan.")
        sys.exit(1)

    load_dotenv(dotenv_path=str(env_path), encoding='utf-8')

    # Validasi variabel wajib tidak boleh kosong / placeholder
    for var_name in REQUIRED_ENV_VARS:
        value = os.getenv(var_name, '')
        if not value or value.startswith('YOUR_'):
            _logger.error(f"ERR-FILE-002: Variabel {var_name} belum diisi di file .env.")
            print(f"⛔ ERR-FILE-002: Variabel {var_name} belum diisi di file .env.")
            sys.exit(1)

    # Validasi APP_ENV
    app_env = os.getenv('APP_ENV', 'production')
    if app_env not in VALID_APP_ENVS:
        _logger.error(
            f"ERR-FILE-005: APP_ENV bernilai '{app_env}', harus salah satu dari: {VALID_APP_ENVS}."
        )
        print(f"⛔ ERR-FILE-005: APP_ENV bernilai '{app_env}', harus 'development' atau 'production'.")
        sys.exit(1)

    # Casting & validasi range
    app_cabang_id = _safe_int_cast(os.getenv('APP_CABANG_ID'), 1, 'APP_CABANG_ID')
    db_host = os.getenv('DB_HOST', DEFAULT_DB_HOST)
    db_port = _safe_int_cast(os.getenv('DB_PORT'), DEFAULT_DB_PORT, 'DB_PORT')
    db_port = _validate_int_range(db_port, 1, 65535, 'DB_PORT')
    db_user = os.getenv('DB_USER', 'abucom_app')
    db_password = os.getenv('DB_PASSWORD', '')
    db_name = os.getenv('DB_NAME', 'abucom_db')
    db_pool_size = _safe_int_cast(os.getenv('DB_POOL_SIZE'), DEFAULT_DB_POOL_SIZE, 'DB_POOL_SIZE')
    db_pool_size = _validate_int_range(db_pool_size, 1, 100, 'DB_POOL_SIZE')
    jwt_secret_key = os.getenv('JWT_SECRET_KEY', '')
    jwt_lifetime_seconds = _safe_int_cast(
        os.getenv('JWT_LIFETIME_SECONDS'), DEFAULT_JWT_LIFETIME, 'JWT_LIFETIME_SECONDS'
    )
    # Validasi JWT lifetime positif
    if jwt_lifetime_seconds <= 0:
        _logger.error(
            f"ERR-FILE-004: Variabel JWT_LIFETIME_SECONDS bernilai {jwt_lifetime_seconds}, harus positif."
        )
        print(f"⛔ ERR-FILE-004: Variabel JWT_LIFETIME_SECONDS bernilai {jwt_lifetime_seconds}, harus positif.")
        sys.exit(1)

    fernet_key = os.getenv('FERNET_KEY', '')
    backup_zip_password = os.getenv('BACKUP_ZIP_PASSWORD', '')
    printer_port = os.getenv('PRINTER_PORT', 'COM1')
    printer_width_mm = _safe_int_cast(
        os.getenv('PRINTER_WIDTH_MM'), DEFAULT_PRINTER_WIDTH, 'PRINTER_WIDTH_MM'
    )

    # Validasi printer width
    if printer_width_mm not in VALID_PRINTER_WIDTHS:
        _logger.warning(
            f"PRINTER_WIDTH_MM bernilai {printer_width_mm}, bukan nilai standar {VALID_PRINTER_WIDTHS}. "
            f"Menggunakan default {DEFAULT_PRINTER_WIDTH}mm."
        )
        printer_width_mm = DEFAULT_PRINTER_WIDTH

    _logger.info(
        f"Konfigurasi berhasil dimuat dari {env_path}. "
        f"Lingkungan: {app_env}, Cabang ID: {app_cabang_id}, "
        f"Target DB: {db_name}@{db_host}:{db_port}"
    )

    return AppConfig(
        app_env=app_env,
        app_cabang_id=app_cabang_id,
        db_host=db_host,
        db_port=db_port,
        db_user=db_user,
        db_password=db_password,
        db_name=db_name,
        db_pool_size=db_pool_size,
        jwt_secret_key=jwt_secret_key,
        jwt_lifetime_seconds=jwt_lifetime_seconds,
        fernet_key=fernet_key,
        backup_zip_password=backup_zip_password,
        printer_port=printer_port,
        printer_width_mm=printer_width_mm,
    )

