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
import re
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

MIN_JWT_KEY_LENGTH = 32
MIN_BACKUP_PASSWORD_LENGTH = 8

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


def _validate_fernet_key(fernet_key: str) -> bool:
    """Memvalidasi apakah string FERNET_KEY valid sebagai kunci Fernet.

    Args:
        fernet_key (str): String kunci Fernet dari file .env.

    Returns:
        bool: True jika kunci valid, False jika tidak.
    """
    try:
        from cryptography.fernet import Fernet
        Fernet(fernet_key.encode('utf-8'))
        return True
    except Exception:
        return False


def _validate_jwt_key_strength(jwt_key: str, app_env: str) -> str | None:
    """Memvalidasi kekuatan kunci rahasia JWT.

    Args:
        jwt_key (str): Kunci rahasia JWT dari file .env.
        app_env (str): Lingkungan runtime aktif ('development' atau 'production').

    Returns:
        str | None: String pesan error jika tidak valid di lingkungan production,
                    atau None jika valid (atau hanya warning di development).
    """
    if len(jwt_key) < MIN_JWT_KEY_LENGTH:
        _logger.warning(
            f"JWT_SECRET_KEY terlalu pendek ({len(jwt_key)} karakter). "
            f"Minimum {MIN_JWT_KEY_LENGTH} karakter untuk keamanan optimal."
        )
        if app_env == 'production':
            # [DATA-KOSONG] ERR-FILE-006 belum ada di katalog resmi.
            return "ERR-FILE-006: JWT_SECRET_KEY terlalu pendek di lingkungan production."
    return None


def _validate_db_host(db_host: str) -> bool:
    """Memvalidasi apakah string DB_HOST merupakan IP address atau hostname yang valid.

    Args:
        db_host (str): String host database dari file .env.

    Returns:
        bool: True jika host valid, False jika tidak.
    """
    if not db_host:
        return False

    host = db_host.strip()

    # Cek format IP (jika hanya terdiri dari digit dan titik)
    if all(c.isdigit() or c == '.' for c in host):
        parts = host.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            try:
                val = int(part)
                if not (0 <= val <= 255) or (len(part) > 1 and part[0] == '0'):
                    return False
            except ValueError:
                return False
        return True

    # Cek format Hostname (RFC 1123)
    if len(host) > 253:
        return False

    # Remove trailing dot if present
    if host.endswith('.'):
        host = host[:-1]

    labels = host.split('.')
    for label in labels:
        if not label or len(label) > 63:
            return False
        if label.startswith('-') or label.endswith('-'):
            return False
        # Harus hanya berisi karakter alfanumerik dan tanda hubung
        if not re.match(r"^[a-zA-Z0-9-]+$", label):
            return False

    return True


def _safe_int_cast(value: str | None, default: int, var_name: str, errors: list[str] | None = None) -> int:
    """Melakukan casting string ke integer secara aman dengan fallback default.

    Args:
        value (str | None): Nilai string dari os.getenv().
        default (int): Nilai default jika casting gagal atau None.
        var_name (str): Nama variabel untuk pesan error.
        errors (list[str] | None): List untuk mengumpulkan pesan error jika menggunakan fail-aggregated.

    Returns:
        int: Nilai integer hasil casting atau default.

    Raises:
        SystemExit: Jika nilai tidak valid dan tidak bisa di-cast (hanya jika errors is None).
    """
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        msg = f"ERR-FILE-003: Variabel {var_name} bernilai '{value}' bukan integer valid di file .env."
        _logger.error(msg)
        if errors is None:
            print(f"⛔ {msg}")
            sys.exit(1)
        else:
            errors.append(msg)
        return default


def _validate_int_range(value: int, min_val: int, max_val: int, var_name: str, errors: list[str] | None = None) -> int:
    """Memvalidasi nilai integer berada dalam rentang yang diizinkan.

    Args:
        value (int): Nilai integer yang akan divalidasi.
        min_val (int): Batas minimum (inklusif).
        max_val (int): Batas maksimum (inklusif).
        var_name (str): Nama variabel untuk pesan error.
        errors (list[str] | None): List untuk mengumpulkan pesan error jika menggunakan fail-aggregated.

    Returns:
        int: Nilai integer yang sudah tervalidasi.

    Raises:
        SystemExit: Jika nilai di luar rentang yang diizinkan (hanya jika errors is None).
    """
    if not (min_val <= value <= max_val):
        msg = f"ERR-FILE-004: Variabel {var_name} bernilai {value}, di luar rentang {min_val}-{max_val}."
        _logger.error(msg)
        if errors is None:
            print(f"⛔ {msg}")
            sys.exit(1)
        else:
            errors.append(msg)
    return value


def load_settings() -> AppConfig:
    """Memuat, memvalidasi, dan meng-cast seluruh variabel konfigurasi dari file .env.

    Fungsi ini melakukan validasi teragregasi (fail-aggregated):
    1. Memverifikasi keberadaan fisik file .env di root proyek (fail-fast).
    2. Memvalidasi variabel wajib tidak kosong dan tidak placeholder.
    3. Memvalidasi tipe data casting ke integer untuk variabel numerik.
    4. Memvalidasi rentang nilai untuk variabel numerik.
    5. Memvalidasi format string dan kekuatan kunci (JWT, Fernet, backup password).

    Returns:
        AppConfig: NamedTuple imutabel berisi seluruh 14 konfigurasi runtime.

    Raises:
        SystemExit: Jika terdapat satu atau lebih kesalahan validasi konfigurasi.
    """
    env_path = Path(__file__).parent.parent / '.env'

    if not env_path.exists():
        _logger.error(f"ERR-FILE-001: File .env tidak ditemukan di {env_path}.")
        print("⛔ ERR-FILE-001: File .env tidak ditemukan.")
        sys.exit(1)

    load_dotenv(dotenv_path=str(env_path), encoding='utf-8')

    errors: list[str] = []

    # 1. Validasi variabel wajib tidak boleh kosong / placeholder
    for var_name in REQUIRED_ENV_VARS:
        value = os.getenv(var_name, '')
        if not value or value.startswith('YOUR_'):
            msg = f"ERR-FILE-002: Variabel {var_name} belum diisi di file .env."
            _logger.error(msg)
            errors.append(msg)

    # 2. Validasi APP_ENV
    app_env = os.getenv('APP_ENV', 'production')
    if app_env not in VALID_APP_ENVS:
        msg = f"ERR-FILE-005: APP_ENV bernilai '{app_env}', harus 'development' atau 'production'."
        _logger.error(msg)
        errors.append(msg)

    # 3. Casting numerik & validasi range
    app_cabang_id_raw = os.getenv('APP_CABANG_ID')
    app_cabang_id = _safe_int_cast(app_cabang_id_raw, 1, 'APP_CABANG_ID', errors)
    if app_cabang_id_raw is not None and app_cabang_id <= 0:
        msg = f"ERR-FILE-004: Variabel APP_CABANG_ID bernilai {app_cabang_id}, harus positif (> 0)."
        _logger.error(msg)
        errors.append(msg)

    db_port_raw = os.getenv('DB_PORT')
    db_port = _safe_int_cast(db_port_raw, DEFAULT_DB_PORT, 'DB_PORT', errors)
    if db_port_raw is not None:
        db_port = _validate_int_range(db_port, 1, 65535, 'DB_PORT', errors)

    db_pool_size_raw = os.getenv('DB_POOL_SIZE')
    db_pool_size = _safe_int_cast(db_pool_size_raw, DEFAULT_DB_POOL_SIZE, 'DB_POOL_SIZE', errors)
    if db_pool_size_raw is not None:
        db_pool_size = _validate_int_range(db_pool_size, 1, 100, 'DB_POOL_SIZE', errors)

    jwt_lifetime_raw = os.getenv('JWT_LIFETIME_SECONDS')
    jwt_lifetime_seconds = _safe_int_cast(jwt_lifetime_raw, DEFAULT_JWT_LIFETIME, 'JWT_LIFETIME_SECONDS', errors)
    if jwt_lifetime_raw is not None and jwt_lifetime_seconds <= 0:
        msg = f"ERR-FILE-004: Variabel JWT_LIFETIME_SECONDS bernilai {jwt_lifetime_seconds}, harus positif."
        _logger.error(msg)
        errors.append(msg)

    printer_width_raw = os.getenv('PRINTER_WIDTH_MM')
    printer_width_mm = _safe_int_cast(printer_width_raw, DEFAULT_PRINTER_WIDTH, 'PRINTER_WIDTH_MM', errors)
    if printer_width_raw is not None and printer_width_mm not in VALID_PRINTER_WIDTHS:
        _logger.warning(
            f"PRINTER_WIDTH_MM bernilai {printer_width_mm}, bukan nilai standar {VALID_PRINTER_WIDTHS}. "
            f"Menggunakan default {DEFAULT_PRINTER_WIDTH}mm."
        )
        printer_width_mm = DEFAULT_PRINTER_WIDTH

    # 4. Validasi format string dan kekuatan kunci
    db_host = os.getenv('DB_HOST', DEFAULT_DB_HOST)
    if db_host:
        if not _validate_db_host(db_host):
            # [DATA-KOSONG] ERR-FILE-008 belum ada di katalog resmi.
            msg = f"ERR-FILE-008: Variabel DB_HOST bernilai '{db_host}' bukan IP address atau hostname yang valid."
            _logger.error(msg)
            errors.append(msg)

    db_user = os.getenv('DB_USER', 'abucom_app')
    if not db_user:
        msg = f"ERR-FILE-002: Variabel DB_USER belum diisi di file .env."
        _logger.error(msg)
        errors.append(msg)

    db_name = os.getenv('DB_NAME', 'abucom_db')
    if not db_name:
        msg = f"ERR-FILE-002: Variabel DB_NAME belum diisi di file .env."
        _logger.error(msg)
        errors.append(msg)

    printer_port = os.getenv('PRINTER_PORT', 'COM1')
    if not printer_port:
        msg = f"ERR-FILE-002: Variabel PRINTER_PORT belum diisi di file .env."
        _logger.error(msg)
        errors.append(msg)

    # Validasi kekuatan JWT_SECRET_KEY
    jwt_secret_key = os.getenv('JWT_SECRET_KEY', '')
    if jwt_secret_key and not jwt_secret_key.startswith('YOUR_'):
        jwt_err = _validate_jwt_key_strength(jwt_secret_key, app_env)
        if jwt_err:
            errors.append(jwt_err)

    # Validasi format FERNET_KEY
    fernet_key = os.getenv('FERNET_KEY', '')
    if fernet_key and not fernet_key.startswith('YOUR_'):
        if not _validate_fernet_key(fernet_key):
            # [DATA-KOSONG] ERR-FILE-007 belum ada di katalog resmi.
            msg = f"ERR-FILE-007: Variabel FERNET_KEY bukan kunci Fernet yang valid."
            _logger.error(msg)
            errors.append(msg)

    # Validasi panjang BACKUP_ZIP_PASSWORD
    backup_zip_password = os.getenv('BACKUP_ZIP_PASSWORD', '')
    if backup_zip_password and not backup_zip_password.startswith('YOUR_'):
        if len(backup_zip_password) < MIN_BACKUP_PASSWORD_LENGTH:
            msg = f"ERR-FILE-004: Variabel BACKUP_ZIP_PASSWORD terlalu pendek, minimum {MIN_BACKUP_PASSWORD_LENGTH} karakter."
            _logger.warning(msg)
            if app_env == 'production':
                errors.append(msg)

    # Validasi kekuatan DB_PASSWORD (hanya warning)
    db_password = os.getenv('DB_PASSWORD', '')
    if db_password and not db_password.startswith('YOUR_'):
        if len(db_password) < 8 or not any(c.isdigit() for c in db_password) or not any(c.isalpha() for c in db_password):
            _logger.warning("DB_PASSWORD lemah. Disarankan menggunakan password minimal 8 karakter dengan kombinasi huruf dan angka.")

    # Jika ada error, cetak seluruhnya dan keluar
    if errors:
        for err in errors:
            print(f"⛔ {err}")
        sys.exit(1)

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

