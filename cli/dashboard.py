"""
Nama Modul: dashboard.py
Deskripsi: Merender dashboard visual harian berdasarkan peran (role) pengguna.
           (Ref: Module Structure Bab 4.2)
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

import sys

# Import third-party
try:
    from rich.console import Console
    from rich.panel import Panel
    _console = Console()
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

# Import local
from db.db_connector import get_db_connection
from logic.auth_handler import logout_user
from middleware.auth_jwt import validate_session_token
from middleware.rbac_guard import get_visible_menus
from utils.text_formatter import clear_terminal


# Map nama modul untuk pengelompokan menu visual (Ref: ACM Bab 3.1)
MODULE_NAMES = {
    'M1': 'Modul M.1 — Transaksi & Kebijakan Harga',
    'M2': 'Modul M.2 — Inventaris, BOM & Stock Opname',
    'M3': 'Modul M.3 — Layanan Keuangan, PPOB & Jasa Service',
    'M4': 'Modul M.4 — SDM, Penggajian & Poin Karyawan',
    'M5': 'Modul M.5 — Antrian & Pelacakan Desain',
    'M6': 'Modul M.6 — Pinjaman, Aset & Pengeluaran',
    'M7': 'Modul M.7 — Keamanan, Audit Trail & Hak Akses',
    'M8': 'Modul M.8 — CRM Pelanggan',
    'M9': 'Modul M.9 — Skalabilitas Multi-Cabang',
    'M10': 'Modul M.10 — Konfigurasi Sistem Runtime'
}


def render_dashboard(session_state: dict) -> None:
    """Merender panel ringkasan visual harian per peran aktif pengguna.

    (Ref: Module Structure Bab 4.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi mekanisme idle timeout 30 menit tanpa aktivitas keyboard
    # untuk memicu logout otomatis secara aman (Ref: Security Design Bab 4.4).
    while True:
        # 1. Validasi token sesi di awal setiap iterasi
        val_res = validate_session_token(session_state)
        if not val_res.is_success:
            print(f"⛔ {val_res.error_msg}")
            # Jalankan logout (audit trail)
            conn_res = get_db_connection()
            if conn_res.is_success:
                db_conn = conn_res.data
                try:
                    logout_user(session_state, db_conn)
                finally:
                    try:
                        db_conn.close()
                    except Exception:
                        pass
            # Hapus token JWT string dari dictionary session_state
            session_state['user_id'] = None
            session_state['username'] = None
            session_state['role'] = None
            session_state['cabang_id'] = None
            session_state['token'] = None
            return

        clear_terminal()

        # Render Dashboard Header
        username = session_state.get('username', '')
        role = session_state.get('role', '')
        cabang_id = session_state.get('cabang_id', '')

        title_text = "DASHBOARD UTAMA — AbuCom"
        info_text = f"Pengguna: {username} | Peran: {role} | Cabang ID: {cabang_id}"

        # Dapatkan menu-menu yang dapat diakses oleh peran aktif
        visible_menus = get_visible_menus(role)

        if HAS_RICH:
            _console.print(Panel(
                info_text,
                title=f"[bold green]{title_text}[/]",
                border_style="bold green",
                expand=False
            ))
            print()
            _console.print("[bold white]PILIHAN MENU:[/]")
            
            current_mod = None
            for idx, (menu_id, label, level) in enumerate(visible_menus, start=1):
                parts = menu_id.split('-')
                if len(parts) >= 2:
                    mod_key = parts[1]
                    if mod_key != current_mod:
                        current_mod = mod_key
                        mod_name = MODULE_NAMES.get(mod_key, f"Modul {mod_key}")
                        _console.print(f"\n[bold cyan]● {mod_name}[/]")
                
                level_indicator = f"[{level}]"
                _console.print(f"  [{idx}] {label} [bold green]{level_indicator}[/]")
                
            print()
            _console.print("  [0] Logout")
            print()
        else:
            border = "═" * 60
            print(border)
            print(f"  {title_text}")
            print(f"  {info_text}")
            print(border)
            print(" PILIHAN MENU:")
            
            current_mod = None
            for idx, (menu_id, label, level) in enumerate(visible_menus, start=1):
                parts = menu_id.split('-')
                if len(parts) >= 2:
                    mod_key = parts[1]
                    if mod_key != current_mod:
                        current_mod = mod_key
                        mod_name = MODULE_NAMES.get(mod_key, f"Modul {mod_key}")
                        print(f"\n● {mod_name}")
                
                print(f"  [{idx}] {label} [{level}]")
                
            print()
            print("  [0] Logout")
            print()

        try:
            pilihan = input("Pilih Menu: ").strip()
        except (EOFError, KeyboardInterrupt):
            pilihan = '0'

        if pilihan == '0':
            # Konfirmasi logout sesuai CLI Flow UC-042 langkah 2-3
            try:
                konfirmasi = input("Apakah Anda yakin ingin logout? [Y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                konfirmasi = 'y'  # Graceful exit → anggap logout

            if konfirmasi != 'y':
                # Pengguna membatalkan logout, kembali ke loop dashboard
                continue

            # Proses logout: catat audit trail ke database (best effort / fail-secure)
            conn_res = get_db_connection()
            if conn_res.is_success:
                db_conn = conn_res.data
                try:
                    logout_user(session_state, db_conn)
                finally:
                    try:
                        db_conn.close()
                    except Exception:
                        pass

            # Hapus token JWT string dari dictionary session_state secara permanen
            # (Ref: Security Design Bab 4.4 langkah 1)
            session_state['user_id'] = None
            session_state['username'] = None
            session_state['role'] = None
            session_state['cabang_id'] = None
            session_state['token'] = None

            # Bersihkan layar terminal (Ref: Security Design Bab 4.4 langkah 3)
            clear_terminal()

            # Tampilkan pesan sukses logout (Ref: CLI Flow Bab 4.2 langkah 5)
            success_msg = "✓ Anda telah berhasil logout secara aman."
            if HAS_RICH:
                _console.print(f"[bold green]{success_msg}[/]")
            else:
                print(success_msg)
            input("Tekan Enter untuk melanjutkan...")
            return
        else:
            # Cari menu_id berdasarkan pilihan indeks
            try:
                val_idx = int(pilihan)
                if 1 <= val_idx <= len(visible_menus):
                    menu_id = visible_menus[val_idx - 1][0]
                    # Panggil handle_navigation dengan menu_id
                    session_state = handle_navigation(session_state, menu_id)
                else:
                    print(f"⛔ Pilihan '{pilihan}' tidak valid.")
                    input("Tekan Enter untuk melanjutkan...")
            except ValueError:
                print(f"⛔ Pilihan '{pilihan}' tidak valid. Harap masukkan angka.")
                input("Tekan Enter untuk melanjutkan...")

            # Jika token kedaluwarsa saat navigasi, loop berikutnya akan mendeteksi token=None dan return
            if session_state.get('token') is None:
                return


def handle_navigation(session_state: dict, menu_id: str) -> dict:
    """Menangani aksi routing navigasi dari dashboard berdasarkan Menu ID.

    (Ref: Module Structure Bab 4.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
        menu_id (str): Kode identifikasi menu target.

    Returns:
        dict: Sesi terupdate setelah perpindahan navigasi.
    """
    val_res = validate_session_token(session_state)
    if not val_res.is_success:
        print(f"⛔ {val_res.error_msg}")
        conn_res = get_db_connection()
        if conn_res.is_success:
            db_conn = conn_res.data
            try:
                logout_user(session_state, db_conn)
            finally:
                try:
                    db_conn.close()
                except Exception:
                    pass
        # Null-kan session state
        session_state['user_id'] = None
        session_state['username'] = None
        session_state['role'] = None
        session_state['cabang_id'] = None
        session_state['token'] = None
        input("Tekan Enter untuk melanjutkan...")
        return session_state

    # Rute pemanggilan fungsi menu target
    if menu_id == 'MENU-M10-001':
        from cli.menu_configs import show_menu_configs
        show_menu_configs(session_state)
    else:
        # Tampilkan placeholder untuk menu yang belum diimplementasikan
        print("Menu ini belum diimplementasikan.")
        input("Tekan Enter untuk melanjutkan...")

    return session_state
