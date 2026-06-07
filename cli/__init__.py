"""
Nama Modul: cli/__init__.py
Deskripsi: Package inisialisasi antarmuka terminal (Presentation Layer) AbuCom.
           (Ref: Module Structure Bab 4.1)
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

import getpass
import os
import platform
import sys

from db.db_connector import get_db_connection
from logic.auth_handler import login_user
from cli.dashboard import render_dashboard
from logic.safety_validator import sanitasi_input_cli, sanitasi_dan_validasi_input, MAX_USERNAME_LENGTH

# Check if rich library is available for advanced CLI UI
try:
    from rich.console import Console
    from rich.panel import Panel
    _console = Console()
    HAS_RICH = True
except ImportError:
    HAS_RICH = False


def clear_terminal() -> None:
    """Membersihkan layar terminal console secara lintas OS.

    (Ref: Coding Standard Bab 11.6)
    """
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def render_login_banner() -> None:
    """Merender banner login double line AbuCom."""
    title_text = "AbuCom — Sistem Manajemen Terpadu Usaha Percetakan"
    subtitle_text = "LOGIN SISTEM"
    
    if HAS_RICH:
        banner_content = f"[bold magenta]{title_text}[/]\n[bold yellow]{subtitle_text}[/]"
        _console.print(Panel(
            banner_content,
            expand=False,
            border_style="bold blue",
            title="[bold white]AbuCom CLI[/]",
            subtitle="[dim white]v1.0[/]"
        ))
    else:
        border = "═" * 58
        print(border)
        print(f"  {title_text}")
        print(f"                    {subtitle_text}")
        print(border)
    print()


def start_cli_app() -> None:
    """Memulai loop inisialisasi visual CLI dan mengarahkan ke menu login awal.

    (Ref: Module Structure Bab 4.1 & CLI Flow Bab 4.1)
    """
    # Force UTF-8 on Windows console
    if sys.platform.startswith('win'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            pass

    try:
        while True:
            clear_terminal()
            render_login_banner()

            print("Ketik 'q' di prompt username untuk keluar aplikasi.")
            print()

            # Minta input username
            try:
                raw_username = input("Username: ")
                val_res = sanitasi_dan_validasi_input(raw_username, MAX_USERNAME_LENGTH, "Username")
                if not val_res.is_valid:
                    if HAS_RICH:
                        _console.print(f"[bold red]⛔ {val_res.error_msg}[/]")
                    else:
                        print(f"⛔ {val_res.error_msg}")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                username = val_res.cleaned_value
            except (EOFError, KeyboardInterrupt):
                print()
                if HAS_RICH:
                    _console.print("[bold yellow]Aplikasi dihentikan secara aman. Sampai jumpa![/]")
                else:
                    print("Aplikasi dihentikan secara aman. Sampai jumpa!")
                break

            if not username:
                if HAS_RICH:
                    _console.print("[bold red]⛔ Username tidak boleh kosong![/]")
                else:
                    print("⛔ Username tidak boleh kosong!")
                input("Tekan Enter untuk melanjutkan...")
                continue

            if username.lower() == 'q':
                if HAS_RICH:
                    _console.print("[bold yellow]Aplikasi dihentikan secara aman. Sampai jumpa![/]")
                else:
                    print("Aplikasi dihentikan secara aman. Sampai jumpa!")
                break

            # Minta input password
            try:
                password = getpass.getpass("Password: ")
            except (EOFError, KeyboardInterrupt):
                print()
                if HAS_RICH:
                    _console.print("[bold yellow]Aplikasi dihentikan secara aman. Sampai jumpa![/]")
                else:
                    print("Aplikasi dihentikan secara aman. Sampai jumpa!")
                break

            # Ambil koneksi DB
            conn_res = get_db_connection()
            if not conn_res.is_success:
                error_msg = "⛔ ERR-DB-001: Kegagalan Database: Tidak dapat terhubung ke server database lokal. Harap hubungi administrator!"
                if HAS_RICH:
                    _console.print(f"[bold red]{error_msg}[/]")
                else:
                    print(error_msg)
                input("Tekan Enter untuk mencoba kembali...")
                continue

            db_conn = conn_res.data
            try:
                login_result = login_user(username, password, db_conn)
            except Exception as e:
                login_result = None
                print(f"Terjadi kesalahan tak terduga saat login: {str(e)}", file=sys.stderr)
            finally:
                try:
                    db_conn.close()
                except Exception:
                    pass

            if not login_result or not login_result.is_success:
                # Login gagal
                err_msg = login_result.error_msg if login_result else "⛔ ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!"
                # Ensure the display format starts with ⛔
                if not err_msg.startswith("⛔") and not err_msg.startswith("ERR-"):
                    err_msg = f"⛔ {err_msg}"
                
                if HAS_RICH:
                    _console.print(f"[bold red]{err_msg}[/]")
                else:
                    print(err_msg)
                input("Tekan Enter untuk melanjutkan...")
                continue

            # Login berhasil
            session_state = login_result.data
            success_msg = f"✓ Login Sukses! Selamat bekerja, {session_state['username']}."
            if HAS_RICH:
                _console.print(f"[bold green]{success_msg}[/]")
            else:
                print(success_msg)
            
            input("Tekan Enter untuk masuk ke dashboard...")

            # Buka Dashboard
            try:
                render_dashboard(session_state)
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print(f"Terjadi kesalahan saat merender dashboard: {str(e)}", file=sys.stderr)
            finally:
                # Pembersihan session_state
                session_state = {}
                print("Sesi berakhir. Kembali ke layar login.")
                input("Tekan Enter untuk melanjutkan...")

    except KeyboardInterrupt:
        print()
        if HAS_RICH:
            _console.print("[bold yellow]Aplikasi dihentikan secara aman. Sampai jumpa![/]")
        else:
            print("Aplikasi dihentikan secara aman. Sampai jumpa!")
