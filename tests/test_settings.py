"""
Nama Modul: test_settings.py
Deskripsi: Unit test terisolasi (mocked) untuk modul config/settings.py.
           Menguji seluruh fungsi pembacaan konfigurasi dotenv saat startup,
           termasuk validasi keberadaan file, variabel wajib, casting tipe data,
           validasi rentang nilai, dan pembentukan AppConfig imutabel.
Author: Antigravity AI
Tanggal: 2026-06-04
"""

# 1. Standard Library
import sys
from collections.abc import Generator
from pathlib import Path
from typing import Callable, Any
from unittest.mock import patch, MagicMock

# 2. Third-Party
import pytest

# 3. Local Modules
import config.settings as settings_mod
from config.settings import (
    load_settings,
    _safe_int_cast,
    _validate_int_range,
    AppConfig,
    REQUIRED_ENV_VARS,
    VALID_APP_ENVS,
    VALID_PRINTER_WIDTHS,
    DEFAULT_DB_HOST,
    DEFAULT_DB_PORT,
    DEFAULT_DB_POOL_SIZE,
    DEFAULT_JWT_LIFETIME,
    DEFAULT_PRINTER_WIDTH,
    MIN_JWT_KEY_LENGTH,
    MIN_BACKUP_PASSWORD_LENGTH,
)


@pytest.fixture(autouse=True)
def clean_env(monkeypatch: pytest.MonkeyPatch) -> Generator[None, None, None]:
    """Membersihkan environment variables sebelum setiap test.

    Memastikan setiap test dimulai dari clean state tanpa sisa
    environment variables dari test sebelumnya yang bisa mencemari
    hasil mock os.getenv.
    """
    for var in [
        'APP_ENV', 'APP_CABANG_ID', 'DB_HOST', 'DB_PORT',
        'DB_USER', 'DB_PASSWORD', 'DB_NAME', 'DB_POOL_SIZE',
        'JWT_SECRET_KEY', 'JWT_LIFETIME_SECONDS', 'FERNET_KEY',
        'BACKUP_ZIP_PASSWORD', 'PRINTER_PORT', 'PRINTER_WIDTH_MM',
    ]:
        monkeypatch.delenv(var, raising=False)
    yield


def _make_valid_env() -> dict[str, str]:
    """Mengembalikan dictionary environment variables yang valid dan lengkap.

    Returns:
        dict[str, str]: Kumpulan key-value env vars yang akan lolos semua validasi.
    """
    return {
        'APP_ENV': 'production',
        'APP_CABANG_ID': '2',
        'DB_HOST': '192.168.1.200',
        'DB_PORT': '3306',
        'DB_USER': 'abucom_app',
        'DB_PASSWORD': 'S3cureP@ssw0rd!',
        'DB_NAME': 'abucom_db',
        'DB_POOL_SIZE': '5',
        'JWT_SECRET_KEY': 'e837df26a91bb812b7a90f19c991f812cb71a9ee08311ab81ab65b1cd78201de',
        'JWT_LIFETIME_SECONDS': '28800',
        'FERNET_KEY': 'Z2VtaW5pYW50aWdyYXZpdHlzZWN1cmVjcm1rZXkyMDI=',
        'BACKUP_ZIP_PASSWORD': 'AES256EncryptBackup2026#',
        'PRINTER_PORT': 'COM1',
        'PRINTER_WIDTH_MM': '58',
    }


def _mock_getenv_from_dict(env_dict: dict[str, str]) -> Callable[[str, Any], Any]:
    """Membuat side_effect function untuk mock os.getenv dari dictionary.

    Args:
        env_dict (dict[str, str]): Dictionary berisi key-value environment variables.

    Returns:
        Callable[[str, Any], Any]: Fungsi side_effect yang kompatibel dengan os.getenv signature.
    """
    def _side_effect(key: str, default: Any = None) -> Any:
        return env_dict.get(key, default)
    return _side_effect


# ==============================================================================
# GRUP A: Test Konstanta dan Struktur Data (Validasi Input)
# ==============================================================================

def test_required_env_vars_berisi_empat_variabel_wajib() -> None:
    """Menguji konstanta REQUIRED_ENV_VARS berisi tepat 4 variabel wajib.

    Tipe: Validasi Input
    Target: REQUIRED_ENV_VARS
    """
    # Arrange & Act
    expected = ('DB_PASSWORD', 'JWT_SECRET_KEY', 'FERNET_KEY', 'BACKUP_ZIP_PASSWORD')

    # Assert
    assert REQUIRED_ENV_VARS == expected
    assert len(REQUIRED_ENV_VARS) == 4


def test_valid_app_envs_berisi_development_dan_production() -> None:
    """Menguji konstanta VALID_APP_ENVS berisi tepat 'development' dan 'production'.

    Tipe: Validasi Input
    Target: VALID_APP_ENVS
    """
    # Arrange & Act
    expected = ('development', 'production')

    # Assert
    assert VALID_APP_ENVS == expected


def test_valid_printer_widths_berisi_58_dan_80() -> None:
    """Menguji konstanta VALID_PRINTER_WIDTHS berisi tepat 58 dan 80.

    Tipe: Validasi Input
    Target: VALID_PRINTER_WIDTHS
    """
    # Arrange & Act
    expected = (58, 80)

    # Assert
    assert VALID_PRINTER_WIDTHS == expected


def test_default_konstanta_memiliki_nilai_yang_benar() -> None:
    """Menguji nilai default konstanta penunjang di modul.

    Tipe: Validasi Input
    Target: Konstanta Default
    """
    # Arrange, Act & Assert
    assert DEFAULT_DB_HOST == '10.10.10.10'
    assert DEFAULT_DB_PORT == 3306
    assert DEFAULT_DB_POOL_SIZE == 5
    assert DEFAULT_JWT_LIFETIME == 28800
    assert DEFAULT_PRINTER_WIDTH == 58


def test_appconfig_memiliki_14_field_yang_benar() -> None:
    """Menguji NamedTuple AppConfig memiliki tepat 14 field konfigurasi yang sesuai.

    Tipe: Validasi Input
    Target: AppConfig._fields
    """
    # Arrange
    expected_fields = (
        'app_env', 'app_cabang_id', 'db_host', 'db_port', 'db_user',
        'db_password', 'db_name', 'db_pool_size', 'jwt_secret_key',
        'jwt_lifetime_seconds', 'fernet_key', 'backup_zip_password',
        'printer_port', 'printer_width_mm'
    )

    # Act & Assert
    assert AppConfig._fields == expected_fields
    assert len(AppConfig._fields) == 14


def test_appconfig_bersifat_imutabel() -> None:
    """Menguji NamedTuple AppConfig bersifat imutabel dan menolak mutasi atribut.

    Tipe: Validasi Input
    Target: AppConfig Immutability
    """
    # Arrange
    config = AppConfig(
        app_env='production', app_cabang_id=1, db_host='localhost', db_port=3306,
        db_user='user', db_password='pwd', db_name='db', db_pool_size=5,
        jwt_secret_key='secret', jwt_lifetime_seconds=3600, fernet_key='fernet',
        backup_zip_password='zip', printer_port='COM1', printer_width_mm=58
    )

    # Act & Assert
    with pytest.raises(AttributeError):
        # type hint ignore untuk pengetesan runtime error
        config.app_env = 'development'  # type: ignore


# ==============================================================================
# GRUP B: Test _safe_int_cast() (7 Skenario)
# ==============================================================================

def test_safe_int_cast_sukses_string_integer_valid() -> None:
    """Menguji casting string integer yang valid mengembalikan nilai integer.

    Tipe: Positif
    Target: _safe_int_cast
    """
    # Arrange
    val = '123'

    # Act
    result = _safe_int_cast(val, 10, 'TEST_VAR')

    # Assert
    assert result == 123


def test_safe_int_cast_sukses_return_default_saat_none() -> None:
    """Menguji casting nilai None mengembalikan default value.

    Tipe: Positif
    Target: _safe_int_cast
    """
    # Arrange & Act
    result = _safe_int_cast(None, 42, 'TEST_VAR')

    # Assert
    assert result == 42


def test_safe_int_cast_sukses_string_negatif() -> None:
    """Menguji casting string integer negatif berhasil.

    Tipe: Positif
    Target: _safe_int_cast
    """
    # Arrange
    val = '-5'

    # Act
    result = _safe_int_cast(val, 10, 'TEST_VAR')

    # Assert
    assert result == -5


def test_safe_int_cast_sukses_string_nol() -> None:
    """Menguji casting string nol berhasil.

    Tipe: Positif
    Target: _safe_int_cast
    """
    # Arrange
    val = '0'

    # Act
    result = _safe_int_cast(val, 10, 'TEST_VAR')

    # Assert
    assert result == 0


def test_safe_int_cast_gagal_string_bukan_angka() -> None:
    """Menguji casting string non-numerik memicu SystemExit 1.

    Tipe: Negatif
    Target: _safe_int_cast
    """
    # Arrange, Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        _safe_int_cast('abc', 10, 'TEST_VAR')
    assert exc_info.value.code == 1


def test_safe_int_cast_gagal_string_float() -> None:
    """Menguji casting string desimal/float memicu SystemExit 1.

    Tipe: Negatif / Edge Case
    Target: _safe_int_cast
    """
    # Arrange, Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        _safe_int_cast('3.14', 10, 'DB_PORT')
    assert exc_info.value.code == 1


def test_safe_int_cast_gagal_string_kosong() -> None:
    """Menguji casting string kosong memicu SystemExit 1.

    Tipe: Negatif / Edge Case
    Target: _safe_int_cast
    """
    # Arrange, Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        _safe_int_cast('', 10, 'DB_PORT')
    assert exc_info.value.code == 1


# ==============================================================================
# GRUP C: Test _validate_int_range() (7 Skenario)
# ==============================================================================

def test_validate_int_range_sukses_nilai_di_tengah_rentang() -> None:
    """Menguji validasi nilai di tengah rentang yang diizinkan mengembalikan nilai tersebut.

    Tipe: Positif
    Target: _validate_int_range
    """
    # Arrange
    val = 50

    # Act
    result = _validate_int_range(val, 1, 100, 'TEST')

    # Assert
    assert result == 50


def test_validate_int_range_sukses_nilai_sama_dengan_batas_bawah() -> None:
    """Menguji validasi nilai batas bawah rentang (inklusif) sukses.

    Tipe: Edge Case (Boundary)
    Target: _validate_int_range
    """
    # Arrange
    val = 1

    # Act
    result = _validate_int_range(val, 1, 100, 'TEST')

    # Assert
    assert result == 1


def test_validate_int_range_sukses_nilai_sama_dengan_batas_atas() -> None:
    """Menguji validasi nilai batas atas rentang (inklusif) sukses.

    Tipe: Edge Case (Boundary)
    Target: _validate_int_range
    """
    # Arrange
    val = 100

    # Act
    result = _validate_int_range(val, 1, 100, 'TEST')

    # Assert
    assert result == 100


def test_validate_int_range_gagal_nilai_di_bawah_batas_minimum() -> None:
    """Menguji validasi nilai di bawah batas minimum memicu SystemExit 1.

    Tipe: Negatif
    Target: _validate_int_range
    """
    # Arrange, Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        _validate_int_range(0, 1, 100, 'DB_PORT')
    assert exc_info.value.code == 1


def test_validate_int_range_gagal_nilai_di_atas_batas_maksimum() -> None:
    """Menguji validasi nilai di atas batas maksimum memicu SystemExit 1.

    Tipe: Negatif
    Target: _validate_int_range
    """
    # Arrange, Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        _validate_int_range(101, 1, 100, 'DB_POOL_SIZE')
    assert exc_info.value.code == 1


def test_validate_int_range_gagal_nilai_negatif() -> None:
    """Menguji validasi nilai negatif di luar rentang port memicu SystemExit 1.

    Tipe: Negatif
    Target: _validate_int_range
    """
    # Arrange, Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        _validate_int_range(-10, 1, 65535, 'DB_PORT')
    assert exc_info.value.code == 1


def test_validate_int_range_sukses_nilai_batas_port_65535() -> None:
    """Menguji validasi batas maksimum port 65535 sukses.

    Tipe: Edge Case (Boundary)
    Target: _validate_int_range
    """
    # Arrange
    val = 65535

    # Act
    result = _validate_int_range(val, 1, 65535, 'DB_PORT')

    # Assert
    assert result == 65535


# ==============================================================================
# GRUP D: Test load_settings() — Tahap 1: Keberadaan File .env (3 Skenario)
# ==============================================================================

@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_file_env_tidak_ditemukan(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika file .env tidak ditemukan fisik.

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = False

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_memanggil_load_dotenv_saat_file_ada(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings memanggil load_dotenv dengan encoding utf-8 saat file .env ada.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    load_settings()

    # Assert
    mock_load_dotenv.assert_called_once()
    assert mock_load_dotenv.call_args[1]['encoding'] == 'utf-8'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_path_env_menunjuk_ke_root_proyek(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings menghitung path .env yang berujung ke root proyek (.env).

    Tipe: Validasi
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    load_settings()

    # Assert
    # Pastikan file .env diload dari root
    path_arg = mock_load_dotenv.call_args[1]['dotenv_path']
    assert path_arg.endswith('.env')


# ==============================================================================
# GRUP E: Test load_settings() — Tahap 2: Validasi Variabel Wajib (8 Skenario)
# ==============================================================================

@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_password_kosong(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_PASSWORD kosong.

    Tipe: Negatif
    Target: load_settings (Tahap 2)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PASSWORD'] = ''
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_jwt_secret_key_kosong(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika JWT_SECRET_KEY kosong.

    Tipe: Negatif
    Target: load_settings (Tahap 2)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['JWT_SECRET_KEY'] = ''
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_fernet_key_kosong(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika FERNET_KEY kosong.

    Tipe: Negatif
    Target: load_settings (Tahap 2)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['FERNET_KEY'] = ''
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_backup_zip_password_kosong(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika BACKUP_ZIP_PASSWORD kosong.

    Tipe: Negatif
    Target: load_settings (Tahap 2)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['BACKUP_ZIP_PASSWORD'] = ''
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_password_placeholder(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_PASSWORD mengandung placeholder.

    Tipe: Negatif
    Target: load_settings (Tahap 2)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PASSWORD'] = 'YOUR_DB_PASSWORD_HERE'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_jwt_secret_key_placeholder(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika JWT_SECRET_KEY mengandung placeholder.

    Tipe: Negatif
    Target: load_settings (Tahap 2)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['JWT_SECRET_KEY'] = 'YOUR_JWT_SECRET_KEY_HERE'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_fernet_key_placeholder(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika FERNET_KEY mengandung placeholder.

    Tipe: Negatif
    Target: load_settings (Tahap 2)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['FERNET_KEY'] = 'YOUR_FERNET_KEY_HERE'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_backup_zip_password_placeholder(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika BACKUP_ZIP_PASSWORD mengandung placeholder.

    Tipe: Negatif
    Target: load_settings (Tahap 2)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['BACKUP_ZIP_PASSWORD'] = 'YOUR_BACKUP_ZIP_PASSWORD_HERE'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


# ==============================================================================
# GRUP F: Test load_settings() — Tahap 3: Validasi APP_ENV (4 Skenario)
# ==============================================================================

@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_app_env_production(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat APP_ENV bernilai 'production'.

    Tipe: Positif
    Target: load_settings (Tahap 3)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'production'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.app_env == 'production'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_app_env_development(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat APP_ENV bernilai 'development'.

    Tipe: Positif
    Target: load_settings (Tahap 3)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'development'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.app_env == 'development'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_app_env_staging(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika APP_ENV bernilai 'staging' (tidak terdaftar).

    Tipe: Negatif
    Target: load_settings (Tahap 3)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'staging'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_app_env_string_acak(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika APP_ENV berisi string acak.

    Tipe: Negatif
    Target: load_settings (Tahap 3)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'testing'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


# ==============================================================================
# GRUP G: Test load_settings() — Tahap 4: Casting & Validasi Numerik (16 Skenario)
# ==============================================================================

# Sub-grup G1: DB_PORT (7 Skenario)

@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_db_port_valid(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat DB_PORT bernilai port valid.

    Tipe: Positif
    Target: load_settings (Tahap 4 - DB_PORT)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PORT'] = '3307'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_port == 3307


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_db_port_default_3306(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses menggunakan fallback default 3306 saat DB_PORT tidak ada.

    Tipe: Positif
    Target: load_settings (Tahap 4 - DB_PORT)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict.pop('DB_PORT', None)
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_port == 3306


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_port_bukan_angka(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_PORT diisi string non-angka.

    Tipe: Negatif
    Target: load_settings (Tahap 4 - DB_PORT)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PORT'] = 'abc'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_port_nol(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_PORT bernilai 0 (di luar rentang 1-65535).

    Tipe: Negatif
    Target: load_settings (Tahap 4 - DB_PORT)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PORT'] = '0'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_port_melebihi_65535(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_PORT melebihi batas 65535.

    Tipe: Negatif / Edge Case
    Target: load_settings (Tahap 4 - DB_PORT)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PORT'] = '70000'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_db_port_batas_atas_65535(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat DB_PORT bernilai tepat batas atas 65535.

    Tipe: Edge Case (Boundary)
    Target: load_settings (Tahap 4 - DB_PORT)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PORT'] = '65535'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_port == 65535


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_db_port_batas_bawah_1(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat DB_PORT bernilai tepat batas bawah 1.

    Tipe: Edge Case (Boundary)
    Target: load_settings (Tahap 4 - DB_PORT)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PORT'] = '1'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_port == 1


# Sub-grup G2: DB_POOL_SIZE (4 Skenario)

@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_db_pool_size_valid(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses dengan DB_POOL_SIZE valid.

    Tipe: Positif
    Target: load_settings (Tahap 4 - DB_POOL_SIZE)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_POOL_SIZE'] = '10'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_pool_size == 10


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_db_pool_size_default(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses menggunakan fallback default pool size saat kosong.

    Tipe: Positif
    Target: load_settings (Tahap 4 - DB_POOL_SIZE)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict.pop('DB_POOL_SIZE', None)
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_pool_size == 5


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_pool_size_nol(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_POOL_SIZE bernilai 0.

    Tipe: Negatif
    Target: load_settings (Tahap 4 - DB_POOL_SIZE)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_POOL_SIZE'] = '0'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_pool_size_melebihi_100(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_POOL_SIZE melebihi batas 100.

    Tipe: Negatif
    Target: load_settings (Tahap 4 - DB_POOL_SIZE)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_POOL_SIZE'] = '101'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


# Sub-grup G3: JWT_LIFETIME_SECONDS (4 Skenario)

@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_jwt_lifetime_valid(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses dengan JWT_LIFETIME_SECONDS valid.

    Tipe: Positif
    Target: load_settings (Tahap 4 - JWT_LIFETIME_SECONDS)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['JWT_LIFETIME_SECONDS'] = '3600'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.jwt_lifetime_seconds == 3600


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_jwt_lifetime_default_28800(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses dengan fallback default lifetime saat kosong.

    Tipe: Positif
    Target: load_settings (Tahap 4 - JWT_LIFETIME_SECONDS)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict.pop('JWT_LIFETIME_SECONDS', None)
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.jwt_lifetime_seconds == 28800


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_jwt_lifetime_negatif(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika JWT_LIFETIME_SECONDS bernilai negatif.

    Tipe: Negatif
    Target: load_settings (Tahap 4 - JWT_LIFETIME_SECONDS)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['JWT_LIFETIME_SECONDS'] = '-60'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_jwt_lifetime_nol(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika JWT_LIFETIME_SECONDS bernilai 0 (harus positif).

    Tipe: Negatif / Edge Case
    Target: load_settings (Tahap 4 - JWT_LIFETIME_SECONDS)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['JWT_LIFETIME_SECONDS'] = '0'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


# Sub-grup G4: PRINTER_WIDTH_MM (1 Skenario)

@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_printer_width_80mm(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses dengan PRINTER_WIDTH_MM bernilai 80.

    Tipe: Positif
    Target: load_settings (Tahap 4 - PRINTER_WIDTH_MM)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['PRINTER_WIDTH_MM'] = '80'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.printer_width_mm == 80


# ==============================================================================
# GRUP H: Test load_settings() — Printer Width Non-Standar & Fallback (3 Skenario)
# ==============================================================================

@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_printer_width_non_standar_fallback_ke_default(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings menggunakan default printer width jika diset non-standar (misal 100).

    Tipe: Edge Case
    Target: load_settings (Tahap 4 - PRINTER_WIDTH_MM Fallback)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['PRINTER_WIDTH_MM'] = '100'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.printer_width_mm == 58


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_printer_width_non_standar_32mm_fallback(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings menggunakan default printer width jika diset 32 (non-standar).

    Tipe: Edge Case
    Target: load_settings (Tahap 4 - PRINTER_WIDTH_MM Fallback)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['PRINTER_WIDTH_MM'] = '32'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.printer_width_mm == 58


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_printer_width_default_saat_tidak_diset(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses menggunakan default printer width jika variabel tidak ada.

    Tipe: Positif
    Target: load_settings (Tahap 4 - PRINTER_WIDTH_MM Fallback)
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict.pop('PRINTER_WIDTH_MM', None)
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.printer_width_mm == 58


# ==============================================================================
# GRUP I: Test load_settings() — Sukses Penuh & Default Values (5 Skenario)
# ==============================================================================

@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_semua_variabel_lengkap(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses memuat semua 14 variabel konfigurasi secara tepat.

    Tipe: Positif (Golden Path)
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.app_env == 'production'
    assert config.app_cabang_id == 2
    assert config.db_host == '192.168.1.200'
    assert config.db_port == 3306
    assert config.db_user == 'abucom_app'
    assert config.db_password == 'S3cureP@ssw0rd!'
    assert config.db_name == 'abucom_db'
    assert config.db_pool_size == 5
    assert config.jwt_secret_key == 'e837df26a91bb812b7a90f19c991f812cb71a9ee08311ab81ab65b1cd78201de'
    assert config.jwt_lifetime_seconds == 28800
    assert config.fernet_key == 'Z2VtaW5pYW50aWdyYXZpdHlzZWN1cmVjcm1rZXkyMDI='
    assert config.backup_zip_password == 'AES256EncryptBackup2026#'
    assert config.printer_port == 'COM1'
    assert config.printer_width_mm == 58


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_return_type_adalah_appconfig(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji hasil load_settings merupakan instansi AppConfig.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert isinstance(config, AppConfig)


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_menggunakan_default_values(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses memuat nilai default untuk variabel opsional yang kosong.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = {
        'DB_PASSWORD': 'SecurePassword!',
        'JWT_SECRET_KEY': 'SecretKey123_456_789_012_345_678_901',
        'FERNET_KEY': 'Z2VtaW5pYW50aWdyYXZpdHlzZWN1cmVjcm1rZXkyMDI=',
        'BACKUP_ZIP_PASSWORD': 'BackupPassword123'
    }
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.app_env == 'production'  # default os.getenv
    assert config.app_cabang_id == 1  # default _safe_int_cast
    assert config.db_host == '10.10.10.10'  # DEFAULT_DB_HOST
    assert config.db_port == 3306  # DEFAULT_DB_PORT
    assert config.db_user == 'abucom_app'  # default os.getenv
    assert config.db_name == 'abucom_db'  # default os.getenv
    assert config.db_pool_size == 5  # DEFAULT_DB_POOL_SIZE
    assert config.jwt_lifetime_seconds == 28800  # DEFAULT_JWT_LIFETIME
    assert config.printer_port == 'COM1'  # default os.getenv
    assert config.printer_width_mm == 58  # DEFAULT_PRINTER_WIDTH


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_app_cabang_id_default_1(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings mengisi APP_CABANG_ID ke default 1 jika tidak disediakan di env.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict.pop('APP_CABANG_ID', None)
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.app_cabang_id == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_app_cabang_id_custom(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings memuat custom APP_CABANG_ID secara benar.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_CABANG_ID'] = '5'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.app_cabang_id == 5


# ==============================================================================
# GRUP J: Test Tambahan — Edge Cases & Variasi (6 Skenario)
# ==============================================================================

@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_app_env_huruf_kapital(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika APP_ENV menggunakan huruf kapital (case-sensitive).

    Tipe: Negatif / Edge Case
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'Production'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_app_env_string_kosong(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika APP_ENV diisi string kosong.

    Tipe: Negatif / Edge Case
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = ''
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_port_negatif(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_PORT diisi nilai negatif.

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PORT'] = '-1'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_app_cabang_id_bukan_angka(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika APP_CABANG_ID diisi nilai non-angka.

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_CABANG_ID'] = 'cabang_a'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_db_host_default_saat_tidak_diset(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings memuat DEFAULT_DB_HOST jika DB_HOST tidak diset.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict.pop('DB_HOST', None)
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_host == '10.10.10.10'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_db_name_default_saat_tidak_diset(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings memuat default 'abucom_db' jika DB_NAME tidak diset.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict.pop('DB_NAME', None)
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_name == 'abucom_db'


# ==============================================================================
# GRUP K: Test Baru dari Issue #0102
# ==============================================================================

def test_validate_fernet_key_format_valid() -> None:
    """Menguji _validate_fernet_key dengan kunci Fernet yang valid.

    Tipe: Positif
    Target: _validate_fernet_key
    """
    from cryptography.fernet import Fernet
    valid_key = Fernet.generate_key().decode('utf-8')
    assert settings_mod._validate_fernet_key(valid_key) is True


def test_validate_fernet_key_format_tidak_valid() -> None:
    """Menguji _validate_fernet_key dengan kunci Fernet yang tidak valid.

    Tipe: Negatif
    Target: _validate_fernet_key
    """
    invalid_key = "kunci_tidak_valid_123"
    assert settings_mod._validate_fernet_key(invalid_key) is False


def test_validate_db_host_valid_ip_dan_hostname() -> None:
    """Menguji _validate_db_host dengan IP address dan hostname yang valid.

    Tipe: Positif
    Target: _validate_db_host
    """
    assert settings_mod._validate_db_host("192.168.1.200") is True
    assert settings_mod._validate_db_host("localhost") is True
    assert settings_mod._validate_db_host("db.abucom.local") is True
    assert settings_mod._validate_db_host("127.0.0.1") is True


def test_validate_db_host_tidak_valid() -> None:
    """Menguji _validate_db_host dengan string host yang tidak valid.

    Tipe: Negatif
    Target: _validate_db_host
    """
    assert settings_mod._validate_db_host("") is False
    assert settings_mod._validate_db_host("256.300.1.1") is False
    assert settings_mod._validate_db_host("invalid_host#name") is False
    assert settings_mod._validate_db_host("-host.com") is False


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_app_cabang_id_nol_atau_negatif(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika APP_CABANG_ID bernilai 0 atau negatif.

    Tipe: Negatif
    Target: load_settings
    """
    mock_exists.return_value = True

    # Skenario 1: Cabang ID = 0
    env_dict = _make_valid_env()
    env_dict['APP_CABANG_ID'] = '0'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1

    # Skenario 2: Cabang ID = -5
    env_dict = _make_valid_env()
    env_dict['APP_CABANG_ID'] = '-5'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_host_tidak_valid(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_HOST tidak valid.

    Tipe: Negatif
    Target: load_settings
    """
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_HOST'] = 'invalid_host#name'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_user_kosong(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_USER kosong.

    Tipe: Negatif
    Target: load_settings
    """
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_USER'] = ''
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_name_kosong(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_NAME kosong.

    Tipe: Negatif
    Target: load_settings
    """
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_NAME'] = ''
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_printer_port_kosong(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika PRINTER_PORT kosong.

    Tipe: Negatif
    Target: load_settings
    """
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['PRINTER_PORT'] = ''
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_fernet_key_tidak_valid(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika format FERNET_KEY tidak valid.

    Tipe: Negatif
    Target: load_settings
    """
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['FERNET_KEY'] = 'kunci_fernet_salah'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_jwt_secret_key_terlalu_pendek_dev_vs_prod(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji JWT_SECRET_KEY terlalu pendek di lingkungan dev (warning) dan prod (error).

    Tipe: Positif & Negatif
    Target: load_settings
    """
    mock_exists.return_value = True

    # Skenario 1: Dev mode (harus lolos meskipun key pendek)
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'development'
    env_dict['JWT_SECRET_KEY'] = 'short_key_123'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    config = load_settings()
    assert config.jwt_secret_key == 'short_key_123'

    # Skenario 2: Prod mode (harus gagal SystemExit karena key pendek)
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'production'
    env_dict['JWT_SECRET_KEY'] = 'short_key_123'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_backup_zip_password_terlalu_pendek_dev_vs_prod(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji BACKUP_ZIP_PASSWORD terlalu pendek di lingkungan dev (warning) dan prod (error).

    Tipe: Positif & Negatif
    Target: load_settings
    """
    mock_exists.return_value = True

    # Skenario 1: Dev mode (harus lolos meskipun password pendek)
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'development'
    env_dict['BACKUP_ZIP_PASSWORD'] = 'short'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    config = load_settings()
    assert config.backup_zip_password == 'short'

    # Skenario 2: Prod mode (harus gagal SystemExit karena password pendek)
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'production'
    env_dict['BACKUP_ZIP_PASSWORD'] = 'short'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


# ==============================================================================
# GRUP L: Skenario Baru Berdasarkan Issue #0103
# ==============================================================================

def test_min_jwt_key_length_bernilai_32() -> None:
    """Menguji konstanta MIN_JWT_KEY_LENGTH bernilai tepat 32.

    Tipe: Validasi
    Target: MIN_JWT_KEY_LENGTH
    """
    # Arrange & Act & Assert
    assert MIN_JWT_KEY_LENGTH == 32


def test_min_backup_password_length_bernilai_8() -> None:
    """Menguji konstanta MIN_BACKUP_PASSWORD_LENGTH bernilai tepat 8.

    Tipe: Validasi
    Target: MIN_BACKUP_PASSWORD_LENGTH
    """
    # Arrange & Act & Assert
    assert MIN_BACKUP_PASSWORD_LENGTH == 8


def test_safe_int_cast_sukses_string_besar() -> None:
    """Menguji casting string integer bernilai besar berhasil.

    Tipe: Positif
    Target: _safe_int_cast
    """
    # Arrange
    val = '999999'

    # Act
    result = _safe_int_cast(val, 10, 'TEST_VAR')

    # Assert
    assert result == 999999


def test_safe_int_cast_gagal_string_spasi() -> None:
    """Menguji casting string berisi spasi memicu SystemExit 1.

    Tipe: Edge Case
    Target: _safe_int_cast
    """
    # Arrange & Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        _safe_int_cast('  ', 10, 'TEST_VAR')
    assert exc_info.value.code == 1


def test_safe_int_cast_gagal_string_campuran() -> None:
    """Menguji casting string campuran huruf dan angka memicu SystemExit 1.

    Tipe: Edge Case
    Target: _safe_int_cast
    """
    # Arrange & Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        _safe_int_cast('12abc', 10, 'TEST_VAR')
    assert exc_info.value.code == 1


def test_safe_int_cast_dengan_errors_list_mengumpulkan_error() -> None:
    """Menguji casting aman dengan parameter errors list mengumpulkan pesan error tanpa keluar program.

    Tipe: Positif
    Target: _safe_int_cast
    """
    # Arrange
    errors: list[str] = []

    # Act
    result = _safe_int_cast('abc', 10, 'TEST_VAR', errors)

    # Assert
    assert result == 10
    assert len(errors) == 1
    assert 'ERR-FILE-003' in errors[0]


def test_safe_int_cast_dengan_errors_list_sukses_tidak_menambah() -> None:
    """Menguji casting aman sukses dengan parameter errors list tidak menambah error baru.

    Tipe: Positif
    Target: _safe_int_cast
    """
    # Arrange
    errors: list[str] = []

    # Act
    result = _safe_int_cast('10', 5, 'TEST_VAR', errors)

    # Assert
    assert result == 10
    assert len(errors) == 0


def test_validate_int_range_dengan_errors_list_mengumpulkan_error() -> None:
    """Menguji validasi rentang dengan parameter errors list mengumpulkan pesan error jika di luar rentang.

    Tipe: Positif
    Target: _validate_int_range
    """
    # Arrange
    errors: list[str] = []

    # Act
    result = _validate_int_range(0, 1, 100, 'TEST_VAR', errors)

    # Assert
    assert result == 0
    assert len(errors) == 1
    assert 'ERR-FILE-004' in errors[0]


def test_validate_int_range_dengan_errors_list_sukses_tidak_menambah() -> None:
    """Menguji validasi rentang dengan parameter errors list tidak menambah error jika berada di dalam rentang.

    Tipe: Positif
    Target: _validate_int_range
    """
    # Arrange
    errors: list[str] = []

    # Act
    result = _validate_int_range(50, 1, 100, 'TEST_VAR', errors)

    # Assert
    assert result == 50
    assert len(errors) == 0


def test_validate_fernet_key_string_kosong() -> None:
    """Menguji _validate_fernet_key dengan string kosong menghasilkan False.

    Tipe: Edge Case
    Target: _validate_fernet_key
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_fernet_key('') is False


def test_validate_fernet_key_string_base64_bukan_fernet() -> None:
    """Menguji _validate_fernet_key dengan string base64 valid tapi bukan kunci Fernet menghasilkan False.

    Tipe: Edge Case
    Target: _validate_fernet_key
    """
    # Arrange
    val = 'dGVzdDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5'

    # Act & Assert
    assert settings_mod._validate_fernet_key(val) is False


def test_validate_fernet_key_string_acak_panjang() -> None:
    """Menguji _validate_fernet_key dengan string acak sepanjang 44 karakter menghasilkan False.

    Tipe: Edge Case
    Target: _validate_fernet_key
    """
    # Arrange
    val = 'a' * 44

    # Act & Assert
    assert settings_mod._validate_fernet_key(val) is False


def test_validate_jwt_key_strength_valid_panjang_64_karakter() -> None:
    """Menguji _validate_jwt_key_strength dengan key panjang 64 karakter di production mengembalikan None.

    Tipe: Positif
    Target: _validate_jwt_key_strength
    """
    # Arrange
    key = 'e' * 64

    # Act
    result = settings_mod._validate_jwt_key_strength(key, 'production')

    # Assert
    assert result is None


def test_validate_jwt_key_strength_valid_tepat_32_karakter() -> None:
    """Menguji _validate_jwt_key_strength dengan key tepat 32 karakter di production mengembalikan None.

    Tipe: Boundary
    Target: _validate_jwt_key_strength
    """
    # Arrange
    key = 'e' * 32

    # Act
    result = settings_mod._validate_jwt_key_strength(key, 'production')

    # Assert
    assert result is None


def test_validate_jwt_key_strength_pendek_di_development() -> None:
    """Menguji _validate_jwt_key_strength dengan key pendek di development mengembalikan None (hanya warning).

    Tipe: Positif
    Target: _validate_jwt_key_strength
    """
    # Arrange
    key = 'short'

    # Act
    result = settings_mod._validate_jwt_key_strength(key, 'development')

    # Assert
    assert result is None


def test_validate_jwt_key_strength_pendek_di_production() -> None:
    """Menguji _validate_jwt_key_strength dengan key pendek di production menghasilkan error ERR-FILE-006.

    Tipe: Negatif
    Target: _validate_jwt_key_strength
    """
    # Arrange
    key = 'short'

    # Act
    result = settings_mod._validate_jwt_key_strength(key, 'production')

    # Assert
    assert result is not None
    assert 'ERR-FILE-006' in result


def test_validate_jwt_key_strength_31_karakter_di_production() -> None:
    """Menguji _validate_jwt_key_strength dengan key 31 karakter di production menghasilkan error ERR-FILE-006.

    Tipe: Boundary
    Target: _validate_jwt_key_strength
    """
    # Arrange
    key = 'e' * 31

    # Act
    result = settings_mod._validate_jwt_key_strength(key, 'production')

    # Assert
    assert result is not None
    assert 'ERR-FILE-006' in result


def test_validate_jwt_key_strength_1_karakter_di_production() -> None:
    """Menguji _validate_jwt_key_strength dengan key 1 karakter di production menghasilkan error ERR-FILE-006.

    Tipe: Edge Case
    Target: _validate_jwt_key_strength
    """
    # Arrange
    key = 'e'

    # Act
    result = settings_mod._validate_jwt_key_strength(key, 'production')

    # Assert
    assert result is not None
    assert 'ERR-FILE-006' in result


def test_validate_db_host_valid_ip_standar() -> None:
    """Menguji _validate_db_host dengan IP address standar mengembalikan True.

    Tipe: Positif
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('192.168.1.200') is True


def test_validate_db_host_valid_ip_localhost() -> None:
    """Menguji _validate_db_host dengan IP localhost mengembalikan True.

    Tipe: Positif
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('127.0.0.1') is True


def test_validate_db_host_valid_hostname_localhost() -> None:
    """Menguji _validate_db_host dengan hostname localhost mengembalikan True.

    Tipe: Positif
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('localhost') is True


def test_validate_db_host_valid_hostname_fqdn() -> None:
    """Menguji _validate_db_host dengan hostname FQDN mengembalikan True.

    Tipe: Positif
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('db.abucom.local') is True


def test_validate_db_host_valid_ip_batas_atas() -> None:
    """Menguji _validate_db_host dengan IP batas atas 255.255.255.255 mengembalikan True.

    Tipe: Boundary
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('255.255.255.255') is True


def test_validate_db_host_valid_ip_batas_bawah() -> None:
    """Menguji _validate_db_host dengan IP batas bawah 0.0.0.0 mengembalikan True.

    Tipe: Boundary
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('0.0.0.0') is True


def test_validate_db_host_invalid_string_kosong() -> None:
    """Menguji _validate_db_host dengan string kosong mengembalikan False.

    Tipe: Negatif
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('') is False


def test_validate_db_host_invalid_ip_oktet_256() -> None:
    """Menguji _validate_db_host dengan IP mengandung oktet 256/300 mengembalikan False.

    Tipe: Negatif
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('256.300.1.1') is False


def test_validate_db_host_invalid_karakter_khusus() -> None:
    """Menguji _validate_db_host dengan hostname mengandung karakter khusus mengembalikan False.

    Tipe: Negatif
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('invalid_host#name') is False


def test_validate_db_host_invalid_awalan_strip() -> None:
    """Menguji _validate_db_host dengan label diawali tanda hubung mengembalikan False.

    Tipe: Negatif
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('-host.com') is False


def test_validate_db_host_invalid_ip_3_oktet() -> None:
    """Menguji _validate_db_host dengan IP hanya 3 oktet mengembalikan False.

    Tipe: Edge Case
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('192.168.1') is False


def test_validate_db_host_invalid_ip_5_oktet() -> None:
    """Menguji _validate_db_host dengan IP memiliki 5 oktet mengembalikan False.

    Tipe: Edge Case
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('192.168.1.1.1') is False


def test_validate_db_host_invalid_ip_leading_zero() -> None:
    """Menguji _validate_db_host dengan IP oktet memiliki leading zero mengembalikan False.

    Tipe: Edge Case
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('192.168.01.200') is False


def test_validate_db_host_invalid_hostname_terlalu_panjang() -> None:
    """Menguji _validate_db_host dengan hostname melebihi 253 karakter mengembalikan False.

    Tipe: Edge Case
    Target: _validate_db_host
    """
    # Arrange
    val = 'a' * 254

    # Act & Assert
    assert settings_mod._validate_db_host(val) is False


def test_validate_db_host_invalid_label_lebih_63_karakter() -> None:
    """Menguji _validate_db_host dengan label hostname melebihi 63 karakter mengembalikan False.

    Tipe: Edge Case
    Target: _validate_db_host
    """
    # Arrange
    val = ('a' * 64) + '.com'

    # Act & Assert
    assert settings_mod._validate_db_host(val) is False


def test_validate_db_host_valid_hostname_trailing_dot() -> None:
    """Menguji _validate_db_host dengan hostname berakhiran titik mengembalikan True.

    Tipe: Edge Case
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('host.local.') is True


def test_validate_db_host_invalid_label_akhir_strip() -> None:
    """Menguji _validate_db_host dengan label diakhiri tanda hubung mengembalikan False.

    Tipe: Negatif
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('host-.com') is False


def test_validate_db_host_invalid_ip_negatif() -> None:
    """Menguji _validate_db_host dengan IP oktet bernilai negatif mengembalikan False.

    Tipe: Negatif
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('-1.0.0.1') is False


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_semua_variabel_wajib_kosong(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika semua 4 variabel wajib diset kosong.

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    for var in REQUIRED_ENV_VARS:
        env_dict[var] = ''
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_semua_variabel_wajib_placeholder(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika semua 4 variabel wajib bernilai placeholder.

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    for var in REQUIRED_ENV_VARS:
        env_dict[var] = f'YOUR_{var}_HERE'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_app_env_default_production(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings default APP_ENV ke 'production' jika tidak disediakan di env.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict.pop('APP_ENV', None)
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.app_env == 'production'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_app_env_spasi(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika APP_ENV diset '  production  ' (mengandung spasi).

    Tipe: Edge Case
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = '  production  '
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_db_pool_size_batas_bawah_1(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat DB_POOL_SIZE bernilai 1.

    Tipe: Boundary
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_POOL_SIZE'] = '1'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_pool_size == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_db_pool_size_batas_atas_100(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat DB_POOL_SIZE bernilai 100.

    Tipe: Boundary
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_POOL_SIZE'] = '100'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_pool_size == 100


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_jwt_lifetime_1_detik(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat JWT_LIFETIME_SECONDS bernilai 1.

    Tipe: Boundary
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['JWT_LIFETIME_SECONDS'] = '1'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.jwt_lifetime_seconds == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_printer_width_58mm(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat PRINTER_WIDTH_MM bernilai 58.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['PRINTER_WIDTH_MM'] = '58'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.printer_width_mm == 58


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_printer_width_negatif_fallback(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings fallback ke 58 jika PRINTER_WIDTH_MM bernilai negatif.

    Tipe: Edge Case
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['PRINTER_WIDTH_MM'] = '-1'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.printer_width_mm == 58


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_app_cabang_id_nol(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika APP_CABANG_ID bernilai 0.

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_CABANG_ID'] = '0'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_app_cabang_id_negatif(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika APP_CABANG_ID bernilai negatif.

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_CABANG_ID'] = '-5'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_jwt_secret_key_terlalu_pendek_dev_warning(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings warning saja jika JWT_SECRET_KEY terlalu pendek di development.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'development'
    env_dict['JWT_SECRET_KEY'] = 'short_key_123'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.jwt_secret_key == 'short_key_123'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_jwt_secret_key_terlalu_pendek_prod_error(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika JWT_SECRET_KEY terlalu pendek di production.

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'production'
    env_dict['JWT_SECRET_KEY'] = 'short_key_123'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_backup_zip_password_terlalu_pendek_dev_warning(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings warning saja jika BACKUP_ZIP_PASSWORD terlalu pendek di development.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'development'
    env_dict['BACKUP_ZIP_PASSWORD'] = 'short'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.backup_zip_password == 'short'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_backup_zip_password_terlalu_pendek_prod_error(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika BACKUP_ZIP_PASSWORD terlalu pendek di production.

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'production'
    env_dict['BACKUP_ZIP_PASSWORD'] = 'short'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_db_user_default_saat_tidak_diset(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings memuat default 'abucom_app' jika DB_USER tidak diset.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict.pop('DB_USER', None)
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_user == 'abucom_app'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_printer_port_default_saat_tidak_diset(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings memuat default 'COM1' jika PRINTER_PORT tidak diset.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict.pop('PRINTER_PORT', None)
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.printer_port == 'COM1'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_multi_error_teragregasi(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings mencetak semua error sekaligus (fail-aggregated) dan keluar.

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PASSWORD'] = ''  # error 1: kosong
    env_dict['APP_ENV'] = 'invalid_env'  # error 2: env invalid
    env_dict['DB_PORT'] = 'abc'  # error 3: non-numeric
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_db_password_lemah_warning_tidak_gagal(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings tetap sukses (hanya warning) jika DB_PASSWORD lemah tapi terisi.

    Tipe: Edge Case
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_PASSWORD'] = 'weak'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_password == 'weak'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_db_host_valid_ip_private(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat DB_HOST diisi IP privat valid.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_HOST'] = '10.10.10.10'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_host == '10.10.10.10'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_db_host_hostname(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses saat DB_HOST diisi hostname localhost.

    Tipe: Positif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_HOST'] = 'localhost'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.db_host == 'localhost'


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_gagal_db_host_ip_invalid_oktet(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings gagal jika DB_HOST diisi IP dengan oktet tidak valid (>255).

    Tipe: Negatif
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['DB_HOST'] = '999.0.0.1'
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        load_settings()
    assert exc_info.value.code == 1


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_jwt_key_tepat_32_karakter_prod(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses dengan JWT_SECRET_KEY tepat 32 karakter di production.

    Tipe: Boundary
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'production'
    env_dict['JWT_SECRET_KEY'] = 'k' * 32
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.jwt_secret_key == 'k' * 32


@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_load_settings_sukses_backup_password_tepat_8_karakter_prod(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    """Menguji load_settings sukses dengan BACKUP_ZIP_PASSWORD tepat 8 karakter di production.

    Tipe: Boundary
    Target: load_settings
    """
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    env_dict['APP_ENV'] = 'production'
    env_dict['BACKUP_ZIP_PASSWORD'] = 'p' * 8
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()

    # Assert
    assert config.backup_zip_password == 'p' * 8


def test_safe_int_cast_mode_agregasi_error_tidak_exit() -> None:
    """Menguji _safe_int_cast dalam mode agregasi (errors list diisi) tidak melakukan exit jika input invalid.

    Tipe: Positif
    Target: _safe_int_cast
    """
    # Arrange
    errors: list[str] = []

    # Act
    result = _safe_int_cast('xyz', 10, 'TEST_VAR', errors)

    # Assert
    assert result == 10
    assert len(errors) == 1
    assert 'ERR-FILE-003' in errors[0]


def test_validate_int_range_mode_agregasi_error_tidak_exit() -> None:
    """Menguji _validate_int_range dalam mode agregasi tidak melakukan exit jika input di luar rentang.

    Tipe: Positif
    Target: _validate_int_range
    """
    # Arrange
    errors: list[str] = []

    # Act
    result = _validate_int_range(0, 1, 100, 'TEST_VAR', errors)

    # Assert
    assert result == 0
    assert len(errors) == 1
    assert 'ERR-FILE-004' in errors[0]


def test_safe_int_cast_mode_langsung_exit_tanpa_errors_param() -> None:
    """Menguji _safe_int_cast melakukan exit langsung jika errors list bernilai None (default).

    Tipe: Negatif
    Target: _safe_int_cast
    """
    # Arrange, Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        _safe_int_cast('xyz', 10, 'TEST_VAR')
    assert exc_info.value.code == 1


def test_validate_int_range_mode_langsung_exit_tanpa_errors_param() -> None:
    """Menguji _validate_int_range melakukan exit langsung jika errors list bernilai None (default).

    Tipe: Negatif
    Target: _validate_int_range
    """
    # Arrange, Act & Assert
    with pytest.raises(SystemExit) as exc_info:
        _validate_int_range(0, 1, 100, 'TEST_VAR')
    assert exc_info.value.code == 1


def test_validate_db_host_invalid_ip_empty_oktet() -> None:
    """Menguji _validate_db_host dengan IP address yang memiliki oktet kosong (ValueError saat casting).

    Tipe: Edge Case
    Target: _validate_db_host
    """
    # Arrange & Act & Assert
    assert settings_mod._validate_db_host('192.168..1') is False


