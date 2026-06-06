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
from utils.text_formatter import clear_terminal


def render_dashboard(session_state: dict) -> None:
    """Merender panel ringkasan visual harian per peran aktif pengguna.

    (Ref: Module Structure Bab 4.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
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

        if HAS_RICH:
            _console.print(Panel(
                info_text,
                title=f"[bold green]{title_text}[/]",
                border_style="bold green",
                expand=False
            ))
            print()
            _console.print("[bold white]PILIHAN MENU:[/]")
            _console.print("  [0] Logout")
            print()
        else:
            border = "═" * 60
            print(border)
            print(f"  {title_text}")
            print(f"  {info_text}")
            print(border)
            print(" PILIHAN MENU:")
            print("  [0] Logout")
            print()

        try:
            pilihan = input("Pilih Menu: ").strip()
        except (EOFError, KeyboardInterrupt):
            pilihan = '0'

        if pilihan == '0':
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
            
            success_msg = "✓ Logout Berhasil! Sesi telah dihapus."
            if HAS_RICH:
                _console.print(f"[bold green]{success_msg}[/]")
            else:
                print(success_msg)
            input("Tekan Enter untuk melanjutkan...")
            return
        else:
            # Panggil handle_navigation
            session_state = handle_navigation(session_state, pilihan)
            # Jika token kedaluwarsa saat navigasi, loop berikutnya akan mendeteksi token=None dan return
            if session_state.get('token') is None:
                return


def handle_navigation(session_state: dict, pilihan: str) -> dict:
    """Menangani aksi routing navigasi hotkey keyboard dari dashboard.

    (Ref: Module Structure Bab 4.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
        pilihan (str): Karakter pilihan navigasi dari keyboard.

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

    # Karena sub-menu lain belum diimplementasikan di issue ini, tampilkan placeholder
    # dan kembali ke dashboard
    print(f"Pilihan '{pilihan}' tidak valid atau belum diimplementasikan.")
    input("Tekan Enter untuk melanjutkan...")
    return session_state
