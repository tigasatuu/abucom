"""
Nama Modul: pengguna_repository.py
Deskripsi: Operasi akses data (CRUD) untuk tabel 'pengguna' MySQL.
           Menggunakan parameterized queries (%s) dan ACID transaction.
           (Ref: Security Design v1.2 Bab 4.1 & Module Structure v1.1 Bab 5.5)
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

from collections import namedtuple
from typing import Any

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


def cek_username_unik(username: str, db_conn: Any) -> Result:
    """Memeriksa apakah username sudah terdaftar di tabel pengguna.

    Args:
        username (str): Username yang akan diperiksa keunikannya.
        db_conn: Objek koneksi database MySQL dari connection pool.

    Returns:
        Result: is_success=True jika username BELUM ada (unik),
                is_success=False jika username SUDAH ada atau terjadi error.

    Example:
        >>> cek_username_unik('kasir_baru', db_conn)
        Result(is_success=True, data=None, error_msg=None)
    """
    cursor = None
    try:
        cursor = db_conn.cursor(dictionary=True)
        query = "SELECT COUNT(*) AS jumlah FROM pengguna WHERE username = %s"
        cursor.execute(query, (username,))
        row = cursor.fetchone()

        if row and row['jumlah'] > 0:
            return Result(
                False,
                None,
                'ERR-DB-002: Username Duplikat: Username tersebut sudah terdaftar di database!'
            )
        return Result(True, None, None)
    except Exception as e:
        return Result(
            False,
            None,
            f'ERR-DB-002: Pelanggaran integritas basis data. Detail: {str(e)}'
        )
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass


def insert_pengguna(
    nama_lengkap: str,
    username: str,
    password_hash: str,
    role: str,
    cabang_id: int,
    db_conn: Any,
) -> Result:
    """Menyisipkan data pengguna baru ke tabel pengguna secara transaksional.

    Operasi dilakukan dalam blok ACID transaction (START TRANSACTION / COMMIT / ROLLBACK).
    Menggunakan parameterized query (%s) untuk pencegahan SQL injection.

    Args:
        nama_lengkap (str): Nama lengkap asli staf/karyawan (maks 100 karakter).
        username (str): Nama login unik staf (maks 50 karakter).
        password_hash (str): String hash bcrypt Cost 12 dari kata sandi.
        role (str): Peran RBAC staf (salah satu dari 8 nilai valid).
        cabang_id (int): ID cabang penempatan kerja staf.
        db_conn: Objek koneksi database MySQL dari connection pool.

    Returns:
        Result: is_success=True dengan data=id pengguna baru (int),
                is_success=False dengan error_msg jika gagal.

    Example:
        >>> insert_pengguna('Budi Santoso', 'kasir_02', '$2b$12$...', 'kasir', 1, db_conn)
        Result(is_success=True, data=2, error_msg=None)
    """
    cursor = None
    try:
        db_conn.start_transaction()
        cursor = db_conn.cursor()

        query_insert = """
            INSERT INTO pengguna
            (nama_lengkap, username, password_hash, role, failed_login_attempts, locked_until, cabang_id)
            VALUES (%s, %s, %s, %s, 0, NULL, %s)
        """
        cursor.execute(query_insert, (
            nama_lengkap,
            username,
            password_hash,
            role,
            cabang_id,
        ))

        new_id = cursor.lastrowid
        db_conn.commit()

        return Result(True, new_id, None)
    except Exception as e:
        try:
            db_conn.rollback()
        except Exception:
            pass
        return Result(
            False,
            None,
            f'ERR-DB-002: Gagal menyimpan data pengguna baru. Detail: {str(e)}'
        )
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass


def get_pengguna_by_username(username: str, db_conn: Any) -> Result:
    """Mengambil data kredensial pengguna dari tabel pengguna secara case-sensitive.

    Args:
        username (str): Username pengguna yang dicari.
        db_conn: Objek koneksi database MySQL.

    Returns:
        Result: is_success=True dengan data=dict data pengguna jika ditemukan,
                is_success=False dengan data=None jika tidak ditemukan,
                atau is_success=False dengan error_msg jika terjadi database error.
    """
    cursor = None
    try:
        cursor = db_conn.cursor(dictionary=True)
        query = """
            SELECT id, nama_lengkap, username, password_hash, role, failed_login_attempts, locked_until, cabang_id
            FROM pengguna
            WHERE BINARY username = %s
        """
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if not row:
            return Result(False, None, None)
        return Result(True, row, None)
    except Exception as e:
        return Result(
            False,
            None,
            f'ERR-DB-001: Kegagalan Database: Gagal mencari pengguna. Detail: {str(e)}'
        )
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass


def update_failed_login(user_id: int, new_attempts: int, locked_until_val: Any, db_conn: Any) -> Result:
    """Mencatat jumlah kegagalan login dan waktu lockout pengguna ke database secara transaksional.

    Args:
        user_id (int): ID pengguna yang akan di-update.
        new_attempts (int): Jumlah percobaan login gagal yang baru.
        locked_until_val (datetime.datetime | None): Waktu akun dikunci (lockout).
        db_conn: Objek koneksi database MySQL.

    Returns:
        Result: is_success=True jika berhasil,
                is_success=False dengan error_msg jika gagal.
    """
    cursor = None
    try:
        db_conn.start_transaction()
        cursor = db_conn.cursor()
        query = "UPDATE pengguna SET failed_login_attempts = %s, locked_until = %s WHERE id = %s"
        cursor.execute(query, (new_attempts, locked_until_val, user_id))
        db_conn.commit()
        return Result(True, None, None)
    except Exception as e:
        try:
            db_conn.rollback()
        except Exception:
            pass
        return Result(
            False,
            None,
            f'ERR-DB-002: Pelanggaran integritas basis data. Detail: {str(e)}'
        )
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass


def reset_failed_login(user_id: int, db_conn: Any) -> Result:
    """Me-reset failed login attempts menjadi 0 dan locked_until menjadi NULL secara transaksional.

    Args:
        user_id (int): ID pengguna yang akan di-reset.
        db_conn: Objek koneksi database MySQL.

    Returns:
        Result: is_success=True jika berhasil,
                is_success=False dengan error_msg jika gagal.
    """
    cursor = None
    try:
        db_conn.start_transaction()
        cursor = db_conn.cursor()
        query = "UPDATE pengguna SET failed_login_attempts = 0, locked_until = NULL WHERE id = %s"
        cursor.execute(query, (user_id,))
        db_conn.commit()
        return Result(True, None, None)
    except Exception as e:
        try:
            db_conn.rollback()
        except Exception:
            pass
        return Result(
            False,
            None,
            f'ERR-DB-002: Pelanggaran integritas basis data. Detail: {str(e)}'
        )
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass

