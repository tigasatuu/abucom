"""
Nama Modul: rbac_guard.py
Deskripsi: Interceptor otorisasi akses menu CLI berbasis matriks peran RBAC Multi-Level.
             Mendefinisikan matriks akses 8 peran x 44 Menu + 4 Base Use Case.
             (Ref: ACM v1.2 Bab 4, Security Design v1.2 Bab 5, Module Structure v1.2 Bab 7.3)
Author: Antigravity (STK-015)
Tanggal: 2026-06-07
"""

from typing import Callable, Any
from functools import wraps
import inspect

# Import local
from middleware.auth_jwt import VALID_ROLES, Result, validate_session_token

# Konstanta Level Akses (Ref: ACM Bab 1.6)
ACCESS_FULL = 'FULL'
ACCESS_READ = 'READ'
ACCESS_INPUT = 'INPUT'
ACCESS_INPUT_READ = 'INPUT_READ'
ACCESS_RTL = 'RTL'
ACCESS_ESC = 'ESC'
ACCESS_DENY = 'DENY'

# Matriks RBAC Lengkap 8 Peran x 48 Menu (44 Use Case Modul + 4 Base)
# Sumber: ACM Bab 4.2 - 4.12
RBAC_MATRIX = {
    # === USE CASE DASAR ===
    'MENU-BASE-001': {role: ACCESS_FULL for role in VALID_ROLES},
    'MENU-BASE-002': {role: ACCESS_FULL for role in VALID_ROLES},
    'MENU-BASE-003': {role: ACCESS_FULL for role in VALID_ROLES},
    'MENU-BASE-004': {role: ACCESS_FULL for role in VALID_ROLES},

    # === MODUL M.1 — Transaksi & Kebijakan Harga ===
    'MENU-M1-001': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_READ,
        'pramuniaga': ACCESS_INPUT,
        'kasir': ACCESS_FULL,
        'fotocopy_print': ACCESS_RTL
    },
    'MENU-M1-002': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_READ,
        'pramuniaga': ACCESS_READ,
        'kasir': ACCESS_READ
    },
    'MENU-M1-003': {
        'pemilik': ACCESS_FULL,
        'kasir': ACCESS_FULL
    },
    'MENU-M1-004': {
        'pemilik': ACCESS_FULL,
        'kasir': ACCESS_ESC
    },
    'MENU-M1-005': {
        'pemilik': ACCESS_FULL
    },
    'MENU-M1-006': {
        'pemilik': ACCESS_FULL,
        'kasir': ACCESS_FULL
    },

    # === MODUL M.2 — Inventaris, BOM & Stock Opname ===
    'MENU-M2-001': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_FULL,
        'produksi_cetak': ACCESS_READ,
        'gudang': ACCESS_FULL
    },
    'MENU-M2-002': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_READ,
        'produksi_cetak': ACCESS_INPUT
    },
    'MENU-M2-003': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_READ,
        'produksi_cetak': ACCESS_INPUT
    },
    'MENU-M2-004': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_FULL,
        'produksi_cetak': ACCESS_INPUT,
        'gudang': ACCESS_INPUT
    },
    'MENU-M2-005': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_ESC,
        'gudang': ACCESS_INPUT
    },
    'MENU-M2-006': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_READ,
        'gudang': ACCESS_READ
    },
    'MENU-M2-007': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_READ,
        'gudang': ACCESS_READ
    },
    'MENU-M2-008': {
        'pemilik': ACCESS_FULL,
        'gudang': ACCESS_INPUT
    },
    'MENU-M2-009': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_FULL,
        'gudang': ACCESS_FULL
    },
    'MENU-M2-010': {
        'pemilik': ACCESS_FULL
    },

    # === MODUL M.3 — Layanan Keuangan, PPOB & Jasa Service ===
    'MENU-M3-001': {
        'pemilik': ACCESS_FULL,
        'kasir': ACCESS_INPUT_READ
    },
    'MENU-M3-002': {
        'pemilik': ACCESS_FULL,
        'kasir': ACCESS_READ
    },
    'MENU-M3-003': {
        'pemilik': ACCESS_FULL,
        'pramuniaga': ACCESS_INPUT,
        'kasir': ACCESS_FULL
    },

    # === MODUL M.4 — SDM, Penggajian & Poin Karyawan ===
    'MENU-M4-001': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_FULL,
        'pramuniaga': ACCESS_INPUT,
        'kasir': ACCESS_INPUT,
        'desainer': ACCESS_INPUT,
        'produksi_cetak': ACCESS_INPUT,
        'fotocopy_print': ACCESS_INPUT,
        'gudang': ACCESS_INPUT
    },
    'MENU-M4-002': {
        'pemilik': ACCESS_FULL
    },
    'MENU-M4-003': {
        'pemilik': ACCESS_FULL,
        'kasir': ACCESS_READ
    },
    'MENU-M4-004': {
        'pemilik': ACCESS_FULL
    },

    # === MODUL M.5 — Antrian & Pelacakan Desain ===
    'MENU-M5-001': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_FULL,
        'pramuniaga': ACCESS_INPUT,
        'kasir': ACCESS_INPUT,
        'desainer': ACCESS_INPUT,
        'produksi_cetak': ACCESS_INPUT
    },
    'MENU-M5-002': {
        'pemilik': ACCESS_FULL,
        'pramuniaga': ACCESS_READ,
        'desainer': ACCESS_FULL
    },
    'MENU-M5-003': {
        'pemilik': ACCESS_FULL,
        'pramuniaga': ACCESS_INPUT,
        'kasir': ACCESS_INPUT
    },

    # === MODUL M.6 — Pinjaman, Aset & Pengeluaran ===
    'MENU-M6-001': {
        'pemilik': ACCESS_FULL
    },
    'MENU-M6-002': {
        'pemilik': ACCESS_FULL
    },
    'MENU-M6-003': {
        'pemilik': ACCESS_FULL
    },
    'MENU-M6-004': {
        'pemilik': ACCESS_FULL
    },
    'MENU-M6-005': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_INPUT,
        'kasir': ACCESS_INPUT
    },

    # === MODUL M.7 — Keamanan, Audit Trail & Hak Akses ===
    'MENU-M7-001': {
        'pemilik': ACCESS_FULL
    },
    'MENU-M7-002': {
        'pemilik': ACCESS_FULL
    },
    'MENU-M7-003': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_ESC,
        'kasir': ACCESS_INPUT
    },
    'MENU-M7-004': {
        'pemilik': ACCESS_FULL,
        'kepala_percetakan': ACCESS_READ,
        'kasir': ACCESS_INPUT
    },
    'MENU-M7-005': {
        'pemilik': ACCESS_FULL
    },
    'MENU-M7-006': {
        'pemilik': ACCESS_FULL
    },

    # === MODUL M.8 — CRM Pelanggan ===
    'MENU-M8-001': {
        'pemilik': ACCESS_FULL,
        'pramuniaga': ACCESS_FULL,
        'kasir': ACCESS_FULL
    },

    # === MODUL M.9 — Skalabilitas Multi-Cabang ===
    'MENU-M9-001': {
        'pemilik': ACCESS_FULL
    },

    # === MODUL M.10 — Konfigurasi Sistem Runtime ===
    'MENU-M10-001': {
        'pemilik': ACCESS_FULL
    }
}

# Label visual menu untuk memetakan Menu ID ke bahasa Indonesia (Ref: ACM Bab 3.1)
MENU_LABELS = {
    'MENU-BASE-001': 'Melakukan Login',
    'MENU-BASE-002': 'Melakukan Logout',
    'MENU-BASE-003': 'Dashboard Utama',
    'MENU-BASE-004': 'Mengubah Password',
    'MENU-M1-001': 'Mencatat Transaksi Penjualan',
    'MENU-M1-002': 'Mengubah Skema Harga Otomatis',
    'MENU-M1-003': 'Mengelola DP & Pelunasan',
    'MENU-M1-004': 'Pembatalan & Retur',
    'MENU-M1-005': 'Margin per Produk',
    'MENU-M1-006': 'Ekspor Struk Thermal',
    'MENU-M2-001': 'Kelola Barang & UoM',
    'MENU-M2-002': 'Hitung HPP BOM Desimal',
    'MENU-M2-003': 'Mencatat Limbah',
    'MENU-M2-004': 'Sinkronisasi ATK Internal',
    'MENU-M2-005': 'Rekonsiliasi Stok',
    'MENU-M2-006': 'Prediksi Re-Order Stok',
    'MENU-M2-007': 'Price Tracking Supplier',
    'MENU-M2-008': 'Impor Data CSV',
    'MENU-M2-009': 'Kelola Supplier & Utang',
    'MENU-M2-010': 'Backup & Restore DB',
    'MENU-M3-001': 'Kelola Saldo PPOB',
    'MENU-M3-002': 'Akun Keuangan Terhemat',
    'MENU-M3-003': 'Transaksi Jasa Service',
    'MENU-M4-001': 'Kelola Absensi & Kasbon',
    'MENU-M4-002': 'Memproses Gaji',
    'MENU-M4-003': 'Poin Insentif Karyawan',
    'MENU-M4-004': 'Potongan Gaji Kasbon',
    'MENU-M5-001': 'Pelacakan Status Antrian',
    'MENU-M5-002': 'Mengelola Arsip Desain',
    'MENU-M5-003': 'Link WhatsApp Web',
    'MENU-M6-001': 'Pinjaman Modal',
    'MENU-M6-002': 'Laba/Rugi per Divisi',
    'MENU-M6-003': 'Alert Jatuh Tempo Utang',
    'MENU-M6-004': 'Depresiasi & Tabungan Aset',
    'MENU-M6-005': 'Pengeluaran Rutin & Tak Terduga',
    'MENU-M7-001': 'Akses RBAC CLI',
    'MENU-M7-002': 'Audit Log Trail JSON',
    'MENU-M7-003': 'Serah Terima Shift',
    'MENU-M7-004': 'Rekonsiliasi Kas',
    'MENU-M7-005': 'Fraud Detection',
    'MENU-M7-006': 'Setup Awal Wizard',
    'MENU-M8-001': 'Database CRM',
    'MENU-M9-001': 'Multi-Cabang',
    'MENU-M10-001': 'Parameter Runtime'
}


def check_menu_permission(menu_id: str, active_role: str) -> str:
    """Memeriksa level akses suatu peran terhadap Menu ID tertentu.

    Menerapkan Default Deny Policy (ACM Bab 6.7): jika peran tidak terdaftar
    pada matriks menu, akses ditolak secara otomatis.

    Args:
        menu_id (str): Kode identifikasi menu CLI (contoh: MENU-M1-001).
        active_role (str): Peran aktif dari sesi pengguna.

    Returns:
        str: Level akses (ACCESS_FULL, ACCESS_READ, dll.) atau ACCESS_DENY.
    """
    menu_permissions = RBAC_MATRIX.get(menu_id, {})
    return menu_permissions.get(active_role, ACCESS_DENY)


def require_role(menu_id: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator fungsional pembungkus fungsi menu CLI untuk proteksi akses.

    Alur pemeriksaan:
    1. Validasi keabsahan token JWT via validate_session_token().
    2. Cek otorisasi peran terhadap RBAC_MATRIX (Default Deny).
    3. Jika ditolak: catat audit trail ACCESS_DENIED, tampilkan ERR-AUTH-003.
    4. Jika diterima: eksekusi fungsi target dengan level akses.

    (Ref: Security Design v1.2 Bab 5.2, ACM v1.2 Bab 6.6 & 6.7)

    Args:
        menu_id (str): Kode identifikasi menu CLI yang diproteksi.

    Returns:
        Callable: Decorator fungsi pembungkus otorisasi.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(session_state: dict, *args: Any, **kwargs: Any) -> Any:
            # 1. Validasi token sesi JWT
            val_res = validate_session_token(session_state)
            if not val_res.is_success:
                print(f"⛔ {val_res.error_msg}")
                return Result(False, None, val_res.error_msg)

            # 2. Cek otorisasi menu berdasarkan peran
            active_role = session_state.get('role', 'guest')
            access_level = check_menu_permission(menu_id, active_role)

            if access_level == ACCESS_DENY:
                # 3. Catat audit trail pelanggaran keamanan
                _log_access_denied(session_state, menu_id, active_role)
                error_msg = "ERR-AUTH-003: Akses Ditolak: Hak Akses Pemilik Dibutuhkan!"
                print(f"⛔ {error_msg}")
                return Result(False, None, error_msg)

            # 4. Eksekusi fungsi target (pass access_level jika target mengharapkannya)
            sig = inspect.signature(func)
            if 'access_level' in sig.parameters:
                return func(session_state, *args, access_level=access_level, **kwargs)
            return func(session_state, *args, **kwargs)
        return wrapper
    return decorator


def _log_access_denied(session_state: dict, menu_id: str, active_role: str) -> None:
    """Mencatat insiden pelanggaran akses ke audit_logs via audit_logger.

    (Ref: ACM v1.2 Bab 6.6, Security Design v1.2 Bab 7.2)
    """
    import json
    from db.db_connector import get_db_connection
    from middleware.audit_logger import log_audit_trail

    user_id = session_state.get('user_id', 0)
    # Jika user_id bernilai None atau tidak diset, gunakan default 0 (guest)
    if user_id is None:
        user_id = 0
    cabang_id = session_state.get('cabang_id', 1)
    if cabang_id is None:
        cabang_id = 1
    old_val = {'attempted_menu': menu_id, 'role': active_role}
    new_val = {'status': 'ILLEGAL_ACCESS_PREVENTED', 'resolved_action': 'TERMINATED'}

    conn_res = get_db_connection()
    if conn_res.is_success:
        db_conn = conn_res.data
        try:
            log_audit_trail(
                pengguna_id=user_id,
                action_type='ACCESS_DENIED',
                target_table=menu_id,
                old_val=old_val,
                new_val=new_val,
                cabang_id=cabang_id,
                db_connection=db_conn
            )
        finally:
            try:
                db_conn.close()
            except Exception:
                pass


def verify_supervisor_escalation(
    supervisor_role: str,
    db_connection: Any
) -> Result:
    """Memverifikasi sandi supervisor (Pemilik/Kepala Percetakan) untuk eskalasi otorisasi.

    Digunakan saat operasi kritis yang membutuhkan kehadiran fisik supervisor
    untuk mengetik kata sandinya langsung di terminal.

    (Ref: ACM v1.2 Bab 6.1 & 6.2, Security Design v1.2 Bab 5.4 & 5.5)

    Args:
        supervisor_role (str): Peran supervisor target ('pemilik' atau 'kepala_percetakan').
        db_connection: Koneksi database aktif.

    Returns:
        Result: is_success=True jika sandi cocok, False jika tidak.
    """
    import getpass
    from middleware.auth_jwt import verify_password

    # Ambil password hash supervisor dari database
    cursor = db_connection.cursor(dictionary=True)
    query = "SELECT id, password_hash, cabang_id FROM pengguna WHERE role = %s LIMIT 1"
    cursor.execute(query, (supervisor_role,))
    supervisor = cursor.fetchone()
    cursor.close()

    if not supervisor:
        return Result(False, None, f"ERR-AUTH-003: Akun supervisor '{supervisor_role}' tidak ditemukan!")

    # Minta input sandi secara aman (karakter tersembunyi)
    print(f"\n🔐 Operasi ini memerlukan otorisasi {supervisor_role}.")
    password_input = getpass.getpass(f"Masukkan sandi {supervisor_role}: ")

    # Verifikasi sandi menggunakan bcrypt
    if verify_password(password_input, supervisor['password_hash']):
        return Result(True, {'supervisor_id': supervisor['id'], 'cabang_id': supervisor['cabang_id']}, None)
    else:
        if supervisor_role == 'pemilik':
            return Result(False, None, "ERR-AUTH-029: Verifikasi sandi Pemilik gagal. Pengeluaran besar dibatalkan!")
        else:
            return Result(False, None, "ERR-AUTH-003: Akses Ditolak: Sandi supervisor salah!")


def get_visible_menus(active_role: str) -> list[tuple[str, str, str]]:
    """Mengembalikan daftar menu yang terlihat oleh peran aktif untuk dashboard.

    Mengembalikan hanya menu yang peran aktif miliki akses selain DENY.
    Digunakan oleh cli/dashboard.py untuk memfilter tampilan menu.

    (Ref: ACM v1.2 Bab 4, Module Structure v1.2 Bab 4.2)

    Args:
        active_role (str): Peran aktif dari sesi pengguna.

    Returns:
        list[tuple[str, str, str]]: Daftar tuple (menu_id, nama_menu, level_akses).
    """
    visible = []
    # Filter menu-menu yang bukan USE CASE DASAR (dimulai dengan MENU-M) agar rapi di dashboard
    for menu_id, permissions in RBAC_MATRIX.items():
        if not menu_id.startswith('MENU-M'):
            continue
        access_level = permissions.get(active_role, ACCESS_DENY)
        if access_level != ACCESS_DENY:
            menu_label = MENU_LABELS.get(menu_id, menu_id)
            visible.append((menu_id, menu_label, access_level))
    return visible
