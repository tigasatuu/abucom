"""
Nama Modul: test_settings.py
Deskripsi: Unit testing untuk pembacaan konfigurasi settings.py.
Author: Antigravity AI
Tanggal: 2026-06-04
"""

import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from config.settings import (
    load_settings,
    _safe_int_cast,
    _validate_int_range,
    AppConfig,
)


def test_safe_int_cast_success() -> None:
    """Menguji casting integer yang sukses."""
    assert _safe_int_cast('123', 10, 'TEST_VAR') == 123
    assert _safe_int_cast(None, 10, 'TEST_VAR') == 10


def test_safe_int_cast_failure() -> None:
    """Menguji casting integer yang gagal memicu SystemExit."""
    with pytest.raises(SystemExit) as exc_info:
        _safe_int_cast('abc', 10, 'TEST_VAR')
    assert exc_info.value.code == 1


def test_validate_int_range_success() -> None:
    """Menguji validasi range yang sukses."""
    assert _validate_int_range(50, 1, 100, 'TEST_VAR') == 50


def test_validate_int_range_failure() -> None:
    """Menguji validasi range yang di luar batas memicu SystemExit."""
    with pytest.raises(SystemExit) as exc_info:
        _validate_int_range(150, 1, 100, 'TEST_VAR')
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
def test_load_settings_missing_env(mock_exists: MagicMock) -> None:
    """Menguji load_settings ketika berkas .env tidak ditemukan."""
    mock_exists.return_value = False
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_missing_required_vars(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings dengan variabel wajib tidak lengkap."""
    mock_exists.return_value = True

    # DB_PASSWORD kosong
    mock_getenv.side_effect = lambda key, default=None: {
        'DB_PASSWORD': '',
        'JWT_SECRET_KEY': 'some_key',
        'FERNET_KEY': 'fernet',
        'BACKUP_ZIP_PASSWORD': 'backup',
    }.get(key, default)

    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_placeholder_vars(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings dengan variabel yang masih placeholder."""
    mock_exists.return_value = True

    # DB_PASSWORD berisi placeholder
    mock_getenv.side_effect = lambda key, default=None: {
        'DB_PASSWORD': 'YOUR_DB_PASSWORD_HERE',
        'JWT_SECRET_KEY': 'some_key',
        'FERNET_KEY': 'fernet',
        'BACKUP_ZIP_PASSWORD': 'backup',
    }.get(key, default)

    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_invalid_app_env(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings dengan APP_ENV tidak valid."""
    mock_exists.return_value = True

    mock_getenv.side_effect = lambda key, default=None: {
        'DB_PASSWORD': 'password',
        'JWT_SECRET_KEY': 'some_key',
        'FERNET_KEY': 'fernet',
        'BACKUP_ZIP_PASSWORD': 'backup',
        'APP_ENV': 'staging',  # Invalid APP_ENV
    }.get(key, default)

    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_invalid_jwt_lifetime(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings dengan JWT_LIFETIME_SECONDS tidak valid (negatif)."""
    mock_exists.return_value = True

    mock_getenv.side_effect = lambda key, default=None: {
        'DB_PASSWORD': 'password',
        'JWT_SECRET_KEY': 'some_key',
        'FERNET_KEY': 'fernet',
        'BACKUP_ZIP_PASSWORD': 'backup',
        'APP_ENV': 'production',
        'JWT_LIFETIME_SECONDS': '-60',
    }.get(key, default)

    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_success(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses dengan konfigurasi standar."""
    mock_exists.return_value = True

    mock_values = {
        'APP_ENV': 'production',
        'APP_CABANG_ID': '2',
        'DB_HOST': '127.0.0.1',
        'DB_PORT': '3306',
        'DB_USER': 'test_user',
        'DB_PASSWORD': 'password',
        'DB_NAME': 'test_db',
        'DB_POOL_SIZE': '10',
        'JWT_SECRET_KEY': 'some_key',
        'JWT_LIFETIME_SECONDS': '3600',
        'FERNET_KEY': 'fernet',
        'BACKUP_ZIP_PASSWORD': 'backup',
        'PRINTER_PORT': 'COM2',
        'PRINTER_WIDTH_MM': '80',
    }

    mock_getenv.side_effect = lambda key, default=None: mock_values.get(key, default)

    config = load_settings()

    assert isinstance(config, AppConfig)
    assert config.app_env == 'production'
    assert config.app_cabang_id == 2
    assert config.db_host == '127.0.0.1'
    assert config.db_port == 3306
    assert config.db_user == 'test_user'
    assert config.db_password == 'password'
    assert config.db_name == 'test_db'
    assert config.db_pool_size == 10
    assert config.jwt_secret_key == 'some_key'
    assert config.jwt_lifetime_seconds == 3600
    assert config.fernet_key == 'fernet'
    assert config.backup_zip_password == 'backup'
    assert config.printer_port == 'COM2'
    assert config.printer_width_mm == 80


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_non_standard_printer_width(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings menggunakan default printer width jika printer_width_mm non-standar."""
    mock_exists.return_value = True

    mock_values = {
        'DB_PASSWORD': 'password',
        'JWT_SECRET_KEY': 'some_key',
        'FERNET_KEY': 'fernet',
        'BACKUP_ZIP_PASSWORD': 'backup',
        'PRINTER_WIDTH_MM': '100',  # Non-standard
    }

    mock_getenv.side_effect = lambda key, default=None: mock_values.get(key, default)

    config = load_settings()
    assert config.printer_width_mm == 58  # Fallback to default
