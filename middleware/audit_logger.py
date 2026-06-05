"""
Nama Modul: audit_logger.py
Deskripsi: Middleware perekaman audit trail terstruktur dalam format JSON.
           (Ref: Module Structure Bab 7.4)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import json
import logging
from typing import Any

_logger = logging.getLogger('abucom.middleware.audit_logger')


def log_audit_trail(
    pengguna_id: int,
    action_type: str,
    target_table: str,
    old_val: dict | None,
    new_val: dict | None,
    cabang_id: int,
    db_connection: Any
) -> None:
    """Mencatat aktivitas modifikasi data sensitif ke tabel audit_logs.

    Args:
        pengguna_id (int): ID pengguna yang melakukan perubahan.
        action_type (str): Jenis operasi (INSERT, UPDATE, DELETE).
        target_table (str): Nama tabel database yang diubah.
        old_val (dict | None): Keadaan data sebelum operasi (JSON).
        new_val (dict | None): Keadaan data setelah operasi (JSON).
        cabang_id (int): ID cabang tempat modifikasi dilakukan.
        db_connection: Koneksi database aktif.
    """
    cursor = None
    try:
        old_val_json = json.dumps(old_val) if old_val is not None else None
        new_val_json = json.dumps(new_val) if new_val is not None else None

        query = (
            "INSERT INTO audit_logs (pengguna_id, action_type, target_table, old_value, new_value, cabang_id) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        cursor = db_connection.cursor()
        cursor.execute(query, (pengguna_id, action_type, target_table, old_val_json, new_val_json, cabang_id))
        db_connection.commit()
    except Exception as e:
        _logger.error(f"Gagal mencatat audit trail ke database: {str(e)}")
    finally:
        if cursor:
            cursor.close()
