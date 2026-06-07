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
from middleware.rbac_guard import get_visible_menus, get_visible_modules, get_module_submenus, MODULE_NAMES
from utils.text_formatter import clear_terminal
from logic.safety_validator import sanitasi_input_cli


def render_dashboard(session_state: dict) -> None:
    """Merender panel ringkasan visual harian per peran aktif pengguna.

    (Ref: Module Structure Bab 4.2, CLI Flow Bab 4.3)

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
                except Exception:
                    pass
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
        info_text = f"Pengguna: {username} | Peran: {role} | Cabang: {cabang_id}"

        if HAS_RICH:
            _console.print(Panel(
                info_text,
                title=f"[bold magenta]{title_text}[/]",
                border_style="bold green",
                expand=False
            ))
            _console.print("Navigasi: Dashboard")
            _console.print()
            _console.print("[bold white]PILIHAN MODUL:[/]")
            
            # get visible modules
            visible_mods = get_visible_modules(role)
            for mod_key, mod_name in visible_mods:
                num = mod_key[1:]  # 'M1' -> '1', 'M10' -> '10'
                display_name = mod_name
                if display_name.startswith("Modul "):
                    display_name = display_name[len("Modul "):]
                _console.print(f"  [{num}] {display_name}")
                
            _console.print()
            _console.print("[bold white]AKSI:[/]")
            _console.print("  [P] Ubah Password")
            _console.print("  [0] Logout")
            _console.print("  [q] Keluar Aplikasi")
            _console.print()
        else:
            border = "═" * 60
            print(border)
            print(f"  {title_text}")
            print(f"  {info_text}")
            print(border)
            print("Navigasi: Dashboard")
            print()
            print("PILIHAN MODUL:")
            visible_mods = get_visible_modules(role)
            for mod_key, mod_name in visible_mods:
                num = mod_key[1:]
                display_name = mod_name
                if display_name.startswith("Modul "):
                    display_name = display_name[len("Modul "):]
                print(f"  [{num}] {display_name}")
            print()
            print("AKSI:")
            print("  [P] Ubah Password")
            print("  [0] Logout")
            print("  [q] Keluar Aplikasi")
            print()

        try:
            raw_pilihan = input("Pilih Menu [1-10 / P / 0 / q]: ")
            pilihan = sanitasi_input_cli(raw_pilihan).strip()
        except (EOFError, KeyboardInterrupt):
            graceful_exit(session_state)
            return

        if pilihan == '0':
            # Konfirmasi logout sesuai CLI Flow UC-042 langkah 2-3
            try:
                raw_konfirmasi = input("Apakah Anda yakin ingin logout? [Y/N]: ")
                konfirmasi = sanitasi_input_cli(raw_konfirmasi).strip().lower()
            except (EOFError, KeyboardInterrupt):
                konfirmasi = 'y'

            if konfirmasi != 'y':
                continue

            # Proses logout
            conn_res = get_db_connection()
            if conn_res.is_success:
                db_conn = conn_res.data
                try:
                    logout_user(session_state, db_conn)
                except Exception:
                    pass
                finally:
                    try:
                        db_conn.close()
                    except Exception:
                        pass

            session_state['user_id'] = None
            session_state['username'] = None
            session_state['role'] = None
            session_state['cabang_id'] = None
            session_state['token'] = None

            clear_terminal()

            success_msg = "✓ Anda telah berhasil logout secara aman."
            if HAS_RICH:
                _console.print(f"[bold green]{success_msg}[/]")
            else:
                print(success_msg)
            input("Tekan Enter untuk melanjutkan...")
            return

        elif pilihan.lower() == 'q':
            graceful_exit(session_state)
            return

        elif pilihan.upper() == 'P':
            form_ubah_password(session_state)

        else:
            # check if input is a valid visible module number
            try:
                val_idx = int(pilihan)
                mod_key = f"M{val_idx}"
                visible_mods = [m[0] for m in get_visible_modules(role)]
                if mod_key in visible_mods:
                    show_module_submenu(session_state, mod_key)
                else:
                    print(f"⛔ Pilihan '{pilihan}' tidak valid. Harap masukkan angka 1-10, P, 0, atau q.")
                    input("Tekan Enter untuk melanjutkan...")
            except ValueError:
                print(f"⛔ Pilihan '{pilihan}' tidak valid. Harap masukkan angka 1-10, P, 0, atau q.")
                input("Tekan Enter untuk melanjutkan...")

        if session_state.get('token') is None:
            return


def show_module_submenu(session_state: dict, module_key: str) -> None:
    """Menampilkan panel sub-menu dari modul tertentu.

    Args:
        session_state (dict): Status sesi aktif pengguna.
        module_key (str): Kunci modul (contoh: 'M1', 'M2').
    """
    from typing import Callable
    role = session_state.get('role', '')

    def make_navigation(current_path: str) -> Callable[[str], str]:
        def add_subpath(subpath: str) -> str:
            return f"{current_path} > {subpath}"
        return add_subpath

    add_subpath = make_navigation("Dashboard")

    while True:
        val_res = validate_session_token(session_state)
        if not val_res.is_success:
            return

        clear_terminal()

        mod_name = MODULE_NAMES.get(module_key, f"Modul {module_key}")
        display_mod_name = mod_name
        if display_mod_name.startswith("Modul "):
            display_mod_name = display_mod_name[len("Modul "):]

        breadcrumb_path = add_subpath(display_mod_name)
        submenus = get_module_submenus(module_key, role)
        if not submenus:
            print("⛔ ERR-AUTH-003: Anda tidak memiliki akses ke modul ini.")
            input("Tekan Enter untuk melanjutkan...")
            return

        title_text = mod_name

        if HAS_RICH:
            _console.print(Panel(
                breadcrumb_path,
                title=f"[bold green]{title_text}[/]",
                border_style="bold green",
                expand=False
            ))
            _console.print(f"Navigasi: {breadcrumb_path}")
            _console.print()
            _console.print("[bold white]SUB-MENU:[/]")
            for idx, (menu_id, label, level) in enumerate(submenus, start=1):
                level_indicator = f"[{level}]"
                _console.print(f"  [{idx}] {label} [bold green]{level_indicator}[/]")
            _console.print()
            _console.print("  [0] Kembali ke Dashboard")
            _console.print("  [q] Keluar Aplikasi")
            _console.print()
        else:
            border = "═" * 60
            print(border)
            print(f"  {title_text}")
            print(border)
            print(f"Navigasi: {breadcrumb_path}")
            print()
            print("SUB-MENU:")
            for idx, (menu_id, label, level) in enumerate(submenus, start=1):
                print(f"  [{idx}] {label} [{level}]")
            print()
            print("  [0] Kembali ke Dashboard")
            print("  [q] Keluar Aplikasi")
            print()

        try:
            raw_pilihan = input("Pilih Sub-Menu [1-N / 0 / q]: ")
            pilihan = sanitasi_input_cli(raw_pilihan).strip()
        except (EOFError, KeyboardInterrupt):
            graceful_exit(session_state)
            return

        if pilihan == '0':
            return
        elif pilihan.lower() == 'q':
            graceful_exit(session_state)
            return
        else:
            try:
                val_idx = int(pilihan)
                if 1 <= val_idx <= len(submenus):
                    selected_menu_id = submenus[val_idx - 1][0]
                    session_state = handle_navigation(session_state, selected_menu_id)
                else:
                    print(f"⛔ Pilihan '{pilihan}' tidak valid. Harap masukkan angka 1-{len(submenus)}, 0, atau q.")
                    input("Tekan Enter untuk melanjutkan...")
            except ValueError:
                print(f"⛔ Pilihan '{pilihan}' tidak valid. Harap masukkan angka.")
                input("Tekan Enter untuk melanjutkan...")

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
            except Exception:
                pass
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
    if menu_id.startswith('MENU-M1-') or menu_id.startswith('MENU-M8-'):
        from cli.menu_transaksi import show_menu_transaksi
        show_menu_transaksi(session_state)
    elif menu_id.startswith('MENU-M2-') or menu_id.startswith('MENU-M5-'):
        from cli.menu_inventaris import show_menu_inventaris
        show_menu_inventaris(session_state)
    elif menu_id.startswith('MENU-M3-'):
        from cli.menu_ppob_service import show_menu_ppob_service
        show_menu_ppob_service(session_state)
    elif menu_id.startswith('MENU-M4-') or menu_id.startswith('MENU-M6-'):
        from cli.menu_sdm_finansial import show_menu_sdm_finansial
        show_menu_sdm_finansial(session_state)
    elif menu_id.startswith('MENU-M7-'):
        print("[PLACEHOLDER] Menu belum diimplementasikan.")
        input("Tekan Enter untuk melanjutkan...")
    elif menu_id.startswith('MENU-M9-'):
        from cli.menu_laporan import show_menu_laporan
        show_menu_laporan(session_state)
    elif menu_id.startswith('MENU-M10-'):
        from cli.menu_configs import show_menu_configs
        show_menu_configs(session_state)
    else:
        print("[PLACEHOLDER] Menu belum diimplementasikan.")
        input("Tekan Enter untuk melanjutkan...")

    return session_state


def form_ubah_password(session_state: dict) -> None:
    """Formulir interaktif untuk mengubah kata sandi pengguna sendiri.

    (Ref: CLI Flow Bab 4.4, SRS-F-044)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    import getpass
    clear_terminal()

    breadcrumb_path = "Dashboard > Ubah Password"

    if HAS_RICH:
        _console.print(Panel(
            "[bold white]MENGUBAH PASSWORD AKUN[/]\n"
            "[blue]Dashboard > Ubah Password[/]",
            style="bold white",
            expand=False
        ))
        _console.print()
    else:
        border = "═" * 60
        print(border)
        print("  MENGUBAH PASSWORD AKUN")
        print(border)
        print(f"Navigasi: {breadcrumb_path}")
        print()

    try:
        password_lama = getpass.getpass("Masukkan Password Lama: ")
    except (EOFError, KeyboardInterrupt):
        return

    conn_res = get_db_connection()
    if not conn_res.is_success:
        print(f"⛔ ERR-DB-002: Koneksi database gagal: {conn_res.error_msg}")
        input("Tekan Enter untuk melanjutkan...")
        return

    db_conn = conn_res.data
    password_hash = None
    try:
        cursor = db_conn.cursor(dictionary=True)
        cursor.execute("SELECT password_hash FROM pengguna WHERE id = %s", (session_state['user_id'],))
        row = cursor.fetchone()
        cursor.close()
        if row:
            password_hash = row['password_hash']
    except Exception as e:
        print(f"⛔ ERR-DB-003: Terjadi kesalahan database: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")
        return
    finally:
        if not password_hash:
            try:
                db_conn.close()
            except Exception:
                pass

    from middleware.auth_jwt import verify_password, hash_password
    if not password_hash or not verify_password(password_lama, password_hash):
        try:
            db_conn.close()
        except Exception:
            pass
        print("⛔ ERR-AUTH-044: Otorisasi Gagal: Kata sandi lama yang Anda masukkan tidak valid!")
        input("Tekan Enter untuk melanjutkan...")
        return

    try:
        password_baru = getpass.getpass("Masukkan Password Baru: ")
        konfirmasi_password = getpass.getpass("Masukkan Kembali Password Baru: ")
    except (EOFError, KeyboardInterrupt):
        try:
            db_conn.close()
        except Exception:
            pass
        return

    if len(password_baru) < 8 or password_baru != konfirmasi_password:
        try:
            db_conn.close()
        except Exception:
            pass
        print("⛔ ERR-VAL-044: Konvalidasi Gagal: Kata sandi baru minimal harus 8 karakter dan bernilai cocok pada kedua input!")
        input("Tekan Enter untuk melanjutkan...")
        return

    hashed_baru = hash_password(password_baru)

    try:
        cursor = db_conn.cursor()
        cursor.execute("UPDATE pengguna SET password_hash = %s WHERE id = %s", (hashed_baru, session_state['user_id']))
        db_conn.commit()
        cursor.close()

        from middleware.audit_logger import log_audit_trail
        log_audit_trail(
            pengguna_id=session_state['user_id'],
            action_type='UPDATE',
            target_table='pengguna',
            old_val={'field': 'password_hash', 'note': '***REDACTED***'},
            new_val={'field': 'password_hash', 'note': '***REDACTED***'},
            cabang_id=session_state.get('cabang_id', 1),
            db_connection=db_conn
        )
    except Exception as e:
        print(f"⛔ ERR-DB-003: Gagal memperbarui password di database: {str(e)}")
        input("Tekan Enter untuk melanjutkan...")
        return
    finally:
        try:
            db_conn.close()
        except Exception:
            pass

    print("✓ Password berhasil diubah! Gunakan sandi baru Anda pada login berikutnya.")
    input("Tekan Enter untuk melanjutkan...")


def graceful_exit(session_state: dict) -> None:
    """Menghentikan aplikasi secara aman setelah membersihkan memori token JWT lokal.

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    conn_res = get_db_connection()
    if conn_res.is_success:
        db_conn = conn_res.data
        try:
            logout_user(session_state, db_conn)
        except Exception:
            pass
        finally:
            try:
                db_conn.close()
            except Exception:
                pass

    session_state['user_id'] = None
    session_state['username'] = None
    session_state['role'] = None
    session_state['cabang_id'] = None
    session_state['token'] = None

    clear_terminal()

    exit_msg = "Aplikasi dihentikan secara aman. Sampai jumpa!"
    if HAS_RICH:
        _console.print(f"[bold yellow]{exit_msg}[/]")
    else:
        print(exit_msg)
    sys.exit(0)

