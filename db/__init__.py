"""
Nama Modul: db/__init__.py
Deskripsi: Package inisialisasi modul Data Access Layer AbuCom.
           Expose fungsi connection pooling dan query builder.
Author: Claude Sonnet 4.6 (STK-004)
Tanggal: 2026-06-04
"""

from db.db_connector import (
    create_connection_pool,
    get_db_connection,
    close_connection_pool,
    get_pool_status,
)
from db.query_builder import (
    execute_query,
    execute_acid_transaction,
    execute_insert,
    execute_many,
    execute_with_retry,
)
from db.schema_initializer import run_full_initialization, verify_schema_integrity
from db.seed_data import run_seed_all, verify_seed_integrity

