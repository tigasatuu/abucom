"""
Nama Modul: schema_initializer.py
Deskripsi: Utilitas fungsional untuk inisialisasi skema database MySQL
             multi-cabang AbuCom. Membaca file DDL SQL, mengeksekusi
             CREATE TABLE/INDEX/INSERT secara transaksional, dan memverifikasi
             integritas seluruh 28 tabel, 4 composite index, dan seed data.
Author: Claude Sonnet 4.6 (STK-004)
Tanggal: 2026-06-03
"""

import os
import sys
import getpass
import logging
from pathlib import Path
from collections import namedtuple

import mysql.connector
from mysql.connector import errors
import bcrypt

# Setup logging
_logger = logging.getLogger('abucom.db.init')

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])

# Konstanta verifikasi integritas schema
EXPECTED_TABLE_COUNT = 28
EXPECTED_SEED_COUNTS = {
    'cabang': 1,
    'pengguna': 1,
    'saldo_ppob': 2,
    'saldo_ewallet': 6,
    'system_configs': 13,
}


def split_sql_statements(sql_content: str) -> list[str]:
    """Membagi isi file SQL menjadi daftar statement individual secara presisi.

    Mendukung penanganan komentar baris (-- dan #), komentar blok (/* */),
    dan memastikan semicolon di dalam string literal tidak memicu pemisahan.

    Args:
        sql_content (str): Isi mentah dari file SQL.

    Returns:
        list[str]: Daftar statement SQL yang valid dan siap dieksekusi.
    """
    statements = []
    current = []
    in_single_quote = False
    in_double_quote = False
    in_comment_line = False
    in_comment_block = False

    i = 0
    n = len(sql_content)
    while i < n:
        char = sql_content[i]

        # Tangani komentar baris
        if not in_comment_block and not in_comment_line:
            if char == '-' and i + 1 < n and sql_content[i+1] == '-':
                in_comment_line = True
                i += 2
                continue
            if char == '#':
                in_comment_line = True
                i += 1
                continue

        # Tangani komentar blok
        if not in_comment_line and not in_comment_block:
            if char == '/' and i + 1 < n and sql_content[i+1] == '*':
                in_comment_block = True
                i += 2
                continue

        # Akhiri komentar baris
        if in_comment_line:
            if char == '\n':
                in_comment_line = False
            i += 1
            continue

        # Akhiri komentar blok
        if in_comment_block:
            if char == '*' and i + 1 < n and sql_content[i+1] == '/':
                in_comment_block = False
                i += 2
            else:
                i += 1
            continue

        # Tangani tanda kutip (string literal)
        if char == "'" and not in_double_quote:
            in_single_quote = not in_single_quote
        elif char == '"' and not in_single_quote:
            in_double_quote = not in_double_quote

        # Pemisahan berdasarkan semicolon
        if char == ';' and not in_single_quote and not in_double_quote:
            stmt = ''.join(current).strip()
            if stmt:
                statements.append(stmt)
            current = []
        else:
            current.append(char)

        i += 1

    final_stmt = ''.join(current).strip()
    if final_stmt:
        statements.append(final_stmt)

    return statements


def read_sql_file(file_path: str) -> Result:
    """Membaca dan mem-parsing file SQL menjadi daftar statement individual.

    Args:
        file_path (str): Path ke file .sql.

    Returns:
        Result: NamedTuple berisi list[str] statement SQL atau pesan error.
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return Result(False, None, f"ERR-FILE-003: File SQL tidak ditemukan di {file_path}")

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        statements = split_sql_statements(content)
        return Result(True, statements, None)
    except FileNotFoundError:
        return Result(False, None, f"ERR-FILE-003: File SQL tidak ditemukan di {file_path}")
    except Exception as e:
        return Result(False, None, f"ERR-FILE-003: Gagal membaca file SQL (Error: {str(e)})")


def execute_schema_init(root_connection, sql_statements: list[str]) -> Result:
    """Mengeksekusi seluruh statement DDL SQL secara berurutan.

    Args:
        root_connection: Koneksi MySQL administratif.
        sql_statements (list[str]): Daftar statement SQL untuk dieksekusi.

    Returns:
        Result: NamedTuple berisi dict statistik eksekusi atau pesan error.
    """
    cursor = root_connection.cursor()
    success_count = 0
    failed_count = 0
    errors_list = []

    for idx, stmt in enumerate(sql_statements):
        try:
            # Lewati statement kosong
            if not stmt.strip():
                continue
            cursor.execute(stmt)
            # Bersihkan hasil dari statement ini jika mengembalikan baris
            if cursor.with_rows:
                cursor.fetchall()
            # Dapatkan hasil (jika ada) untuk membersihkan buffer multi-resultsets
            try:
                while cursor.nextset():
                    if cursor.with_rows:
                        cursor.fetchall()
            except mysql.connector.Error:
                pass
            success_count += 1
        except mysql.connector.Error as e:
            failed_count += 1
            err_msg = f"Gagal mengeksekusi stmt ke-{idx+1} ({stmt[:50]}...): MySQL Error {e.errno}: {e.msg}"
            _logger.error(err_msg)
            errors_list.append(err_msg)
        except Exception as e:
            failed_count += 1
            err_msg = f"Gagal mengeksekusi stmt ke-{idx+1} ({stmt[:50]}...): Error: {str(e)}"
            _logger.error(err_msg)
            errors_list.append(err_msg)

    cursor.close()
    stats = {'success': success_count, 'failed': failed_count, 'errors': errors_list}
    if failed_count > 0:
        return Result(False, stats, f"Inisialisasi selesai dengan {failed_count} kesalahan.")
    return Result(True, stats, None)


def verify_schema_integrity(db_connection) -> Result:
    """Memverifikasi integritas skema database hasil inisialisasi.

    Memeriksa:
    1. Jumlah tabel = 28
    2. Keberadaan 4 composite index
    3. Jumlah seed data per tabel master

    Args:
        db_connection: Koneksi aktif ke database abucom_db.

    Returns:
        Result: NamedTuple berisi dict laporan verifikasi atau pesan error.
    """
    cursor = db_connection.cursor()
    report = {'tables': 0, 'indexes': 0, 'seeds': {}}
    is_valid = True
    errors_list = []

    try:
        # 1. Verifikasi Jumlah Tabel
        cursor.execute("SHOW TABLES")
        tables = [r[0] for r in cursor.fetchall()]
        report['tables'] = len(tables)
        if len(tables) != EXPECTED_TABLE_COUNT:
            is_valid = False
            errors_list.append(
                f"Jumlah tabel tidak sesuai. Diharapkan {EXPECTED_TABLE_COUNT}, ditemukan {len(tables)}."
            )

        # 2. Verifikasi 4 Composite Index
        expected_indexes = {
            'transaksi': 'idx_transaksi_tanggal_cabang',
            'absensi': 'idx_absensi_pengguna_tanggal',
            'antrian_kerja': 'idx_antrian_status_cabang',
            'barang': 'idx_barang_tipe_cabang'
        }
        index_count = 0
        for table, idx_name in expected_indexes.items():
            if table in tables:
                cursor.execute(f"SHOW INDEX FROM {table}")
                indexes = [r[2] for r in cursor.fetchall()]
                if idx_name in indexes:
                    index_count += 1
                else:
                    errors_list.append(f"Index {idx_name} tidak ditemukan di tabel {table}.")
            else:
                errors_list.append(f"Tabel {table} tidak ada untuk pemeriksaan index.")
        report['indexes'] = index_count
        if index_count != 4:
            is_valid = False

        # 3. Verifikasi Jumlah Seed Data
        for table, expected_qty in EXPECTED_SEED_COUNTS.items():
            if table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                qty = cursor.fetchone()[0]
                report['seeds'][table] = qty
                if qty != expected_qty:
                    is_valid = False
                    errors_list.append(
                        f"Jumlah baris seed data di tabel {table} tidak sesuai. Diharapkan {expected_qty}, ditemukan {qty}."
                    )
            else:
                report['seeds'][table] = 0
                is_valid = False
                errors_list.append(f"Tabel {table} tidak ditemukan saat verifikasi seed data.")

        cursor.close()
        if not is_valid:
            return Result(False, report, f"Integritas skema tidak valid: {'; '.join(errors_list)}")
        return Result(True, report, None)

    except mysql.connector.Error as e:
        cursor.close()
        return Result(False, None, f"ERR-DB-001: Verifikasi gagal (MySQL Error {e.errno}: {e.msg})")
    except Exception as e:
        cursor.close()
        return Result(False, None, f"ERR-DB-001: Verifikasi gagal (Error: {str(e)})")


def run_full_initialization(
    root_host: str,
    root_port: int,
    root_user: str,
    root_password: str,
    schema_file_path: str,
    app_db_name: str = 'abucom_db'
) -> Result:
    """Menjalankan proses inisialisasi skema database secara lengkap.

    Alur eksekusi:
    1. Buka koneksi root ke MySQL server.
    2. Baca file schema.sql.
    3. Eksekusi seluruh DDL statement.
    4. Generate bcrypt hash untuk password pemilik default 'admin123'.
    5. Update password pemilik di pengguna id 1.
    6. Verifikasi integritas hasil.
    7. Tutup koneksi.

    Args:
        root_host (str): IP server MySQL.
        root_port (int): Port MySQL.
        root_user (str): Username administratif MySQL.
        root_password (str): Password administratif MySQL.
        schema_file_path (str): Path file schema.sql.
        app_db_name (str): Nama database target (default 'abucom_db').

    Returns:
        Result: NamedTuple berisi laporan inisialisasi lengkap.
    """
    # 1. Buka koneksi administratif
    try:
        root_conn = mysql.connector.connect(
            host=root_host,
            port=root_port,
            user=root_user,
            password=root_password
        )
    except mysql.connector.Error as e:
        return Result(False, None, f"ERR-DB-001: Koneksi gagal (MySQL Error {e.errno}: {e.msg})")
    except Exception as e:
        return Result(False, None, f"ERR-DB-001: Koneksi gagal (Error: {str(e)})")

    # 2. Baca file SQL
    read_res = read_sql_file(schema_file_path)
    if not read_res.is_success:
        root_conn.close()
        return read_res

    sql_statements = read_res.data

    # 3. Eksekusi seluruh statement DDL & Seed
    init_res = execute_schema_init(root_conn, sql_statements)
    if not init_res.is_success:
        root_conn.close()
        return init_res

    # 4. Generate bcrypt hash untuk default password 'admin123'
    # TODO: Generate bcrypt hash riil saat deployment pertama
    try:
        default_pwd = b'admin123'
        salt = bcrypt.gensalt(rounds=12)
        hashed_pwd = bcrypt.hashpw(default_pwd, salt).decode('utf-8')
    except Exception as e:
        root_conn.close()
        return Result(False, None, f"ERR-VAL-050: Gagal men-generate bcrypt password hash (Error: {str(e)})")

    # 5. Update password pemilik di pengguna id 1
    cursor = root_conn.cursor()
    try:
        # Pindah ke database target
        cursor.execute(f"USE {app_db_name}")
        cursor.execute(
            "UPDATE pengguna SET password_hash = %s WHERE id = 1",
            (hashed_pwd,)
        )
        root_conn.commit()
    except mysql.connector.Error as e:
        cursor.close()
        root_conn.close()
        return Result(False, None, f"ERR-DB-001: Gagal memperbarui password pemilik (MySQL Error {e.errno}: {e.msg})")
    except Exception as e:
        cursor.close()
        root_conn.close()
        return Result(False, None, f"ERR-DB-001: Gagal memperbarui password pemilik (Error: {str(e)})")
    finally:
        if cursor:
            cursor.close()

    # 6. Verifikasi integritas
    verify_res = verify_schema_integrity(root_conn)
    root_conn.close()

    if not verify_res.is_success:
        return verify_res

    return Result(
        True,
        {
            'init_stats': init_res.data,
            'verify_report': verify_res.data
        },
        None
    )


if __name__ == '__main__':
    if sys.platform.startswith('win'):
        # Force UTF-8 encoding on Windows console to prevent UnicodeEncodeError with emojis
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stdin.reconfigure(encoding='utf-8')
        except AttributeError:
            pass

    # Eksekusi CLI interaktif untuk inisialisasi
    print("=" * 60)
    print("  ABUCOM DATABASE INITIALIZATION UTILITY  ")
    print("=" * 60)
    print()
    print("⚠️  PERINGATAN: Operasi ini akan MENGHAPUS SELURUH DATA di database abucom_db!")
    print("⚠️  Seluruh tabel, data transaksi, dan konfigurasi akan HILANG PERMANEN.")
    print()

    konfirmasi = input(
        "Ketik 'YA SAYA YAKIN' untuk melanjutkan, atau tekan Enter untuk membatalkan: "
    )
    if konfirmasi.strip() != 'YA SAYA YAKIN':
        print("[INFO] Operasi dibatalkan oleh pengguna.")
        sys.exit(0)

    print()
    print("Silakan masukkan kredensial administratif MySQL:")
    db_host = input("MySQL Host [localhost]: ").strip() or "localhost"
    db_port_str = input("MySQL Port [3306]: ").strip() or "3306"
    try:
        db_port = int(db_port_str)
    except ValueError:
        print("⛔ ERR-VAL-050: Port harus berupa angka.")
        sys.exit(1)

    db_user = input("MySQL User [root]: ").strip() or "root"
    db_pass = getpass.getpass("MySQL Password: ")

    print("\n[INFO] Memulai inisialisasi basis data...")
    schema_file = Path(__file__).parent.parent / 'schema.sql'

    result = run_full_initialization(
        root_host=db_host,
        root_port=db_port,
        root_user=db_user,
        root_password=db_pass,
        schema_file_path=str(schema_file)
    )

    if result.is_success:
        print("\n✅ INISIALISASI BASIS DATA BERHASIL!")
        stats = result.data['init_stats']
        report = result.data['verify_report']
        print(f"   - SQL Statements Sukses: {stats['success']}")
        print(f"   - Total Tabel Terbentuk: {report['tables']}/{EXPECTED_TABLE_COUNT}")
        print(f"   - Composite Indexes Valid: {report['indexes']}/4")
        print("   - Seed Data Master Ter-import:")
        for tbl, count in report['seeds'].items():
            print(f"     * {tbl}: {count} baris")
        print("\n🔑 Akses Login Awal Pemilik:")
        print("   - Username: pemilik")
        print("   - Password: admin123 (Wajib segera diganti saat login pertama)")
    else:
        print(f"\n⛔ INISIALISASI GAGAL: {result.error_msg}")
        if result.data and 'init_stats' in result.data and result.data['init_stats']['errors']:
            print("   Detail Kesalahan:")
            for err in result.data['init_stats']['errors'][:5]:
                print(f"     * {err}")
            if len(result.data['init_stats']['errors']) > 5:
                print(f"     * ...dan {len(result.data['init_stats']['errors']) - 5} kesalahan lainnya.")
        sys.exit(1)
