"""
Nama Modul: pengguna.py
Deskripsi: Logika bisnis inti registrasi dan manajemen akun pengguna.
           Mengorkestrasi validasi input, hashing bcrypt, penyimpanan database,
           dan pencatatan audit log secara transaksional.
           (Ref: Security Design v1.2 Bab 4.1 & Access Control Matrix v1.1)
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

from collections import namedtuple
from typing import Any

from logic.safety_validator import validasi_kekuatan_sandi
from middleware.auth_jwt import hash_password
from db.pengguna_repository import (
    cek_username_unik,
    insert_pengguna,
    get_password_hash_by_id,
    update_password_hash,
)

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])

# Tuple imutabel 8 peran RBAC valid sesuai Access Control Matrix v1.1
VALID_ROLES: tuple[str, ...] = (
    'pemilik',
    'kepala_percetakan',
    'pramuniaga',
    'kasir',
    'desainer',
    'produksi_cetak',
    'fotocopy_print',
    'gudang',
)


def validasi_role(role: str) -> Result:
    """Memvalidasi apakah role yang diberikan termasuk dalam 8 peran RBAC valid.

    Args:
        role (str): Nama peran yang akan divalidasi.

    Returns:
        Result: is_success=True jika role valid, False jika tidak.

    Example:
        >>> validasi_role('kasir')
        Result(is_success=True, data='kasir', error_msg=None)
        >>> validasi_role('admin')
        Result(is_success=False, data=None, error_msg='ERR-VAL-002: ...')
    """
    role_lower = role.strip().lower()
    if role_lower not in VALID_ROLES:
        roles_str = ', '.join(VALID_ROLES)
        return Result(
            False,
            None,
            f'ERR-VAL-002: Role Tidak Valid: Role harus salah satu dari: {roles_str}!'
        )
    return Result(True, role_lower, None)


def validasi_nama_lengkap(nama: str) -> Result:
    """Memvalidasi nama lengkap pengguna (tidak kosong, maks 100 karakter).

    Args:
        nama (str): Nama lengkap yang akan divalidasi.

    Returns:
        Result: is_success=True jika nama valid, False jika tidak.

    Example:
        >>> validasi_nama_lengkap('Budi Santoso')
        Result(is_success=True, data='Budi Santoso', error_msg=None)
    """
    nama_stripped = nama.strip()
    if not nama_stripped:
        return Result(False, None, 'ERR-VAL-003: Nama Kosong: Nama lengkap tidak boleh kosong!')
    if len(nama_stripped) > 100:
        return Result(False, None, 'ERR-VAL-003: Nama Terlalu Panjang: Nama lengkap maksimal 100 karakter!')
    return Result(True, nama_stripped, None)


def validasi_username(username: str) -> Result:
    """Memvalidasi format username (tidak kosong, maks 50 karakter, alfanumerik + underscore).

    Args:
        username (str): Username yang akan divalidasi formatnya.

    Returns:
        Result: is_success=True jika format valid, False jika tidak.

    Example:
        >>> validasi_username('kasir_02')
        Result(is_success=True, data='kasir_02', error_msg=None)
    """
    username_stripped = username.strip().lower()
    if not username_stripped:
        return Result(False, None, 'ERR-VAL-004: Username Kosong: Username tidak boleh kosong!')
    if len(username_stripped) > 50:
        return Result(False, None, 'ERR-VAL-004: Username Terlalu Panjang: Username maksimal 50 karakter!')
    import re
    if not re.match(r'^[a-z0-9_]+$', username_stripped):
        return Result(
            False,
            None,
            'ERR-VAL-004: Format Username Salah: Username hanya boleh berisi huruf kecil, angka, dan underscore!'
        )
    return Result(True, username_stripped, None)


def registrasi_pengguna(
    nama_lengkap: str,
    username: str,
    password: str,
    konfirmasi_password: str,
    role: str,
    cabang_id: int,
    db_conn: Any,
    registrar_user_id: int,
) -> Result:
    """Mengorkestrasi proses registrasi akun pengguna baru secara lengkap.

    Alur eksekusi:
    1. Validasi nama lengkap (tidak kosong, maks 100 karakter).
    2. Validasi format username (alfanumerik + underscore, maks 50 karakter).
    3. Validasi kecocokan password dan konfirmasi password.
    4. Validasi kekuatan password (5 kriteria keamanan).
    5. Validasi role terhadap 8 peran RBAC valid.
    6. Periksa keunikan username di database.
    7. Hash password menggunakan bcrypt Cost Factor 12.
    8. Simpan data pengguna baru ke tabel `pengguna` (ACID).
    9. Catat aktivitas registrasi ke audit log dengan IP '10.10.10.10'.

    Args:
        nama_lengkap (str): Nama lengkap asli staf/karyawan.
        username (str): Nama login unik staf.
        password (str): Kata sandi polos dari input CLI.
        konfirmasi_password (str): Konfirmasi ulang kata sandi.
        role (str): Peran RBAC staf.
        cabang_id (int): ID cabang penempatan kerja staf.
        db_conn: Objek koneksi database MySQL dari connection pool.
        registrar_user_id (int): ID pengguna (pemilik) yang melakukan registrasi.

    Returns:
        Result: is_success=True dengan data=id pengguna baru (int),
                is_success=False dengan error_msg spesifik.

    Example:
        >>> registrasi_pengguna(
        ...     'Budi Santoso', 'kasir_02', 'SandiKuat123!', 'SandiKuat123!',
        ...     'kasir', 1, db_conn, 1
        ... )
        Result(is_success=True, data=2, error_msg=None)
    """
    # Langkah 1: Validasi nama lengkap
    nama_result = validasi_nama_lengkap(nama_lengkap)
    if not nama_result.is_success:
        return Result(False, None, nama_result.error_msg)

    # Langkah 2: Validasi format username
    username_result = validasi_username(username)
    if not username_result.is_success:
        return Result(False, None, username_result.error_msg)

    # Langkah 3: Validasi kecocokan password
    if password != konfirmasi_password:
        return Result(
            False,
            None,
            'ERR-VAL-005: Konfirmasi Gagal: Kata sandi dan konfirmasi kata sandi tidak cocok!'
        )

    # Langkah 4: Validasi kekuatan password
    strength_result = validasi_kekuatan_sandi(password)
    if not strength_result.is_valid:
        return Result(False, None, strength_result.error_msg)

    # Langkah 5: Validasi role RBAC
    role_result = validasi_role(role)
    if not role_result.is_success:
        return Result(False, None, role_result.error_msg)

    # Langkah 6: Periksa keunikan username di database
    unik_result = cek_username_unik(username_result.data, db_conn)
    if not unik_result.is_success:
        return Result(False, None, unik_result.error_msg)

    # Langkah 7: Hash password dengan bcrypt Cost Factor 12
    password_hashed = hash_password(password)

    # Langkah 8: Simpan data pengguna baru ke database (ACID)
    insert_result = insert_pengguna(
        nama_lengkap=nama_result.data,
        username=username_result.data,
        password_hash=password_hashed,
        role=role_result.data,
        cabang_id=cabang_id,
        db_conn=db_conn,
    )
    if not insert_result.is_success:
        return Result(False, None, insert_result.error_msg)

    new_user_id = insert_result.data

    # Langkah 9: Catat aktivitas registrasi ke audit log dengan IP '10.10.10.10'
    cursor = None
    try:
        cursor = db_conn.cursor()
        audit_query = """
            INSERT INTO audit_logs
            (pengguna_id, action_type, target_table, old_value, new_value, ip_address, cabang_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        import json
        new_value_json = json.dumps({
            'user_id': new_user_id,
            'username': username_result.data,
            'role': role_result.data,
            'cabang_id': cabang_id,
        })
        cursor.execute(audit_query, (
            registrar_user_id,
            'USER_REGISTERED',
            'pengguna',
            None,
            new_value_json,
            '10.10.10.10',
            cabang_id,
        ))
        db_conn.commit()
    except Exception:
        # Audit log gagal tidak membatalkan registrasi yang sudah berhasil
        pass
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass

    return Result(True, new_user_id, None)


def ubah_password_akun(
    user_id: int,
    password_lama: str,
    password_baru: str,
    konfirmasi_password: str,
    cabang_id: int,
    db_conn: Any,
) -> Result:
    """Mengorkestrasi proses pengubahan kata sandi akun pengguna sendiri.

    Alur eksekusi:
    1. Validasi kecocokan password baru dan konfirmasi password.
    2. Validasi kekuatan password baru (5 kriteria keamanan).
    3. Ambil password hash lama dari database.
    4. Verifikasi kecocokan password lama dengan hash database menggunakan bcrypt.
    5. Cek apakah password baru sama dengan password lama.
    6. Hash password baru menggunakan bcrypt Cost Factor 12.
    7. Perbarui password hash di database secara transaksional (ACID).
    8. Catat aktivitas pengubahan kata sandi ke audit log (redacted).

    Args:
        user_id (int): ID pengguna yang ingin mengubah password.
        password_lama (str): Password lama dalam bentuk teks polos.
        password_baru (str): Password baru dalam bentuk teks polos.
        konfirmasi_password (str): Konfirmasi kata sandi baru.
        cabang_id (int): ID cabang aktif pengguna.
        db_conn: Objek koneksi database MySQL.

    Returns:
        Result: is_success=True dengan data={'action': 'PASSWORD_CHANGED'},
                is_success=False dengan error_msg spesifik.

    Example:
        >>> ubah_password_akun(1, 'SandiLama123!', 'SandiBaru123!', 'SandiBaru123!', 1, db_conn)
        Result(is_success=True, data={'action': 'PASSWORD_CHANGED'}, error_msg=None)
    """
    from middleware.auth_jwt import verify_password, hash_password
    from middleware.audit_logger import log_audit_trail

    # Input Type and Presence Validations
    if not isinstance(password_lama, str) or not isinstance(password_baru, str) or not isinstance(konfirmasi_password, str):
        return Result(
            False,
            None,
            'ERR-VAL-044: Konvalidasi Gagal: Semua parameter input kata sandi harus berupa teks/string!'
        )

    if not password_lama.strip() or not password_baru.strip() or not konfirmasi_password.strip():
        return Result(
            False,
            None,
            'ERR-VAL-044: Konvalidasi Gagal: Input kata sandi tidak boleh kosong atau hanya berisi spasi!'
        )

    # Langkah 1: Validasi kecocokan password baru dan konfirmasi
    if len(password_baru) < 8 or password_baru != konfirmasi_password:
        return Result(
            False,
            None,
            'ERR-VAL-044: Konvalidasi Gagal: Kata sandi baru minimal harus 8 karakter '
            'dan bernilai cocok pada kedua input!'
        )

    if len(password_baru) > 128:
        return Result(
            False,
            None,
            'ERR-VAL-044: Konvalidasi Gagal: Kata sandi baru melebihi batas maksimum 128 karakter!'
        )

    # Langkah 2: Validasi kekuatan password baru
    strength_result = validasi_kekuatan_sandi(password_baru)
    if not strength_result.is_valid:
        return Result(False, None, strength_result.error_msg)

    # Langkah 3: Ambil hash password lama dari database
    hash_result = get_password_hash_by_id(user_id, db_conn)
    if not hash_result.is_success:
        return Result(False, None, hash_result.error_msg)

    # Langkah 4: Verifikasi password lama menggunakan bcrypt
    if not verify_password(password_lama, hash_result.data):
        return Result(
            False,
            None,
            'ERR-AUTH-044: Otorisasi Gagal: Kata sandi lama yang Anda masukkan tidak valid!'
        )

    # Langkah 5: Cek password baru tidak sama dengan password lama
    if password_lama == password_baru:
        return Result(
            False,
            None,
            'ERR-VAL-044: Konvalidasi Gagal: Kata sandi baru tidak boleh sama dengan kata sandi lama!'
        )

    # Langkah 6: Hash password baru dengan bcrypt Cost Factor 12
    new_hash = hash_password(password_baru)

    # Langkah 7: Simpan hash baru ke database via repository
    update_result = update_password_hash(user_id, new_hash, db_conn)
    if not update_result.is_success:
        return Result(False, None, update_result.error_msg)

    # Langkah 8: Catat audit trail
    log_audit_trail(
        pengguna_id=user_id,
        action_type='UPDATE',
        target_table='pengguna',
        old_val={'field': 'password_hash', 'note': '***REDACTED***'},
        new_val={'field': 'password_hash', 'note': '***REDACTED***'},
        cabang_id=cabang_id,
        db_connection=db_conn
    )

    return Result(True, {'action': 'PASSWORD_CHANGED'}, None)

