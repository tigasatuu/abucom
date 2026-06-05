"""
Nama Modul: config_cache.py
Deskripsi: Modul Data Access Layer untuk membaca, menyimpan ke cache memori,
           dan memperbarui parameter regulasi bisnis runtime dari tabel
           database system_configs (Modul M.10).
Author: Antigravity AI
Tanggal: 2026-06-05
"""

# 1. Standard Library
import logging
from collections import namedtuple
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
from typing import Any

# 2. Third-Party (Tidak ada)

# 3. Local Modules
# (Diimpor secara internal jika diperlukan, atau tidak diperlukan jika menggunakan kursor langsung)

# Logger instansiasi
_logger = logging.getLogger('abucom.db.config_cache')

# NamedTuple definitions
ConfigParam = namedtuple('ConfigParam', [
    'id', 'parameter_key', 'parameter_value', 'tipe_data', 'deskripsi'
])

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])

# Cache memori lokal sesi — dictionary parameter_key -> parameter_value (string)
_config_cache: dict[str, str] = {}


def load_all_configs(db_connection: Any, cabang_id: int) -> Result:
    """Memuat seluruh parameter runtime dari tabel system_configs ke cache memori.

    Fungsi ini dipanggil SATU KALI saat startup program (main.py) setelah
    koneksi database berhasil. Seluruh baris parameter di-load ke dictionary
    _config_cache untuk diakses cepat oleh modul-modul konsumen.

    Args:
        db_connection: Koneksi database MySQL aktif dari pool.
        cabang_id (int): ID cabang aktif dari settings.

    Returns:
        Result: NamedTuple berisi status success/failure dan jumlah parameter dimuat.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = (
            "SELECT id, parameter_key, parameter_value, tipe_data, deskripsi "
            "FROM system_configs "
            "WHERE cabang_id = %s "
            "ORDER BY id ASC"
        )
        cursor.execute(query, (cabang_id,))
        rows = cursor.fetchall()
        
        _config_cache.clear()
        for row in rows:
            _config_cache[row['parameter_key']] = row['parameter_value']
            
        _logger.info(f"Config runtime: {len(_config_cache)} parameter berhasil dimuat ke cache.")
        return Result(True, len(_config_cache), None)
    except Exception as e:
        error_msg = f"ERR-DB-010: Gagal memuat config runtime: {str(e)}"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def get_config_value(key: str, default: str | None = None) -> str | None:
    """Mengambil nilai parameter runtime dari cache memori lokal.

    Args:
        key (str): Kunci parameter (e.g. 'target_laba_payroll').
        default (str | None): Nilai fallback jika key tidak ditemukan di cache.

    Returns:
        str | None: Nilai parameter sebagai string, atau default.
    """
    return _config_cache.get(key, default)


def get_config_decimal(key: str, default: Decimal = Decimal('0.0000')) -> Decimal:
    """Mengambil nilai parameter runtime dan meng-cast ke Decimal presisi 4.

    Args:
        key (str): Kunci parameter.
        default (Decimal): Nilai fallback Decimal jika key tidak ditemukan.

    Returns:
        Decimal: Nilai parameter ter-cast ke Decimal 4 desimal.
    """
    value = _config_cache.get(key)
    if value is None:
        return default
    try:
        return Decimal(value).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError):
        return default


def get_all_configs_list(db_connection: Any, cabang_id: int) -> Result:
    """Mengambil seluruh parameter runtime sebagai list of ConfigParam NamedTuple.

    Fungsi ini digunakan oleh cli/menu_configs.py untuk menampilkan tabel
    parameter ke layar pemilik secara visual.

    Args:
        db_connection: Koneksi database MySQL aktif.
        cabang_id (int): ID cabang aktif.

    Returns:
        Result: NamedTuple berisi list[ConfigParam] atau error.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = (
            "SELECT id, parameter_key, parameter_value, tipe_data, deskripsi "
            "FROM system_configs "
            "WHERE cabang_id = %s "
            "ORDER BY id ASC"
        )
        cursor.execute(query, (cabang_id,))
        rows = cursor.fetchall()
        list_config_params = [
            ConfigParam(
                id=row['id'],
                parameter_key=row['parameter_key'],
                parameter_value=row['parameter_value'],
                tipe_data=row['tipe_data'],
                deskripsi=row['deskripsi']
            )
            for row in rows
        ]
        return Result(True, list_config_params, None)
    except Exception as e:
        error_msg = f"ERR-DB-010: Gagal mengambil daftar config runtime: {str(e)}"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def update_config_value(db_connection: Any, config_id: int, new_value: str, cabang_id: int) -> Result:
    """Memperbarui nilai parameter di database dan sinkronisasi cache memori.

    Args:
        db_connection: Koneksi database MySQL aktif.
        config_id (int): ID baris parameter di tabel system_configs.
        new_value (str): Nilai baru parameter (sudah divalidasi).
        cabang_id (int): ID cabang aktif.

    Returns:
        Result: NamedTuple berisi status success/failure.
    """
    cursor = None
    try:
        db_connection.start_transaction()
        cursor = db_connection.cursor(dictionary=True)
        
        # SELECT sebelum update untuk mendapatkan old_value dan parameter_key
        select_query = (
            "SELECT parameter_key, parameter_value "
            "FROM system_configs "
            "WHERE id = %s AND cabang_id = %s"
        )
        cursor.execute(select_query, (config_id, cabang_id))
        row = cursor.fetchone()
        if not row:
            db_connection.rollback()
            return Result(False, None, f"ERR-DB-011: Config ID {config_id} tidak ditemukan untuk cabang {cabang_id}.")
            
        parameter_key = row['parameter_key']
        old_value = row['parameter_value']
        
        # UPDATE
        update_query = (
            "UPDATE system_configs "
            "SET parameter_value = %s "
            "WHERE id = %s AND cabang_id = %s"
        )
        cursor.execute(update_query, (new_value, config_id, cabang_id))
        
        db_connection.commit()
        
        # Perbarui cache memori lokal secara sinkron
        _config_cache[parameter_key] = new_value
        
        return Result(True, {'old_value': old_value, 'new_value': new_value, 'parameter_key': parameter_key}, None)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-011: Gagal update config: {str(e)}"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()
