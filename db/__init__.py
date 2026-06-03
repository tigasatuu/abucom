"""
Nama Modul: db/__init__.py
Deskripsi: Package inisialisasi modul Data Access Layer AbuCom.
           Expose fungsi connection pooling dan query builder.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

from db.db_connector import create_connection_pool, get_db_connection, close_connection_pool
from db.schema_initializer import run_full_initialization, verify_schema_integrity
