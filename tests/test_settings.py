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
        'FERNET_KEY': 'Z2VtaW5pYW50aWdyYXZpdHlzZWN1cmVjcm1rZXkyMDI2',
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
    assert config.fernet_key == 'Z2VtaW5pYW50aWdyYXZpdHlzZWN1cmVjcm1rZXkyMDI2'
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
        'JWT_SECRET_KEY': 'SecretKey123',
        'FERNET_KEY': 'FernetKey123',
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
