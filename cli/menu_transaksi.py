"""
Nama Modul: menu_transaksi.py
Deskripsi: Antarmuka kasir penjualan retail, pesanan cetak kustom, DP, retur, dan CRM.
           (Ref: Module Structure Bab 4.3)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""


# 1. Standard Library
import os
import platform
import json
from decimal import Decimal

# 2. Third-Party
from rich.console import Console
from rich.panel import Panel
from tabulate import tabulate

# 3. Local Modules
from logic.safety_validator import sanitasi_input_cli, validasi_nama_pelanggan, validasi_nomor_whatsapp
from middleware.rbac_guard import require_role
from middleware.audit_logger import log_audit_trail
from db.db_connector import get_db_connection
from db.query_builder import (
    execute_query, insert_pelanggan_baru, cari_pelanggan_by_whatsapp,
    get_daftar_pelanggan, get_riwayat_transaksi_pelanggan, update_pelanggan
)
from config.settings import load_settings

console = Console()


def show_menu_transaksi(session_state: dict) -> None:
    """Menampilkan panel utama transaksi penjualan.

    (Ref: Module Structure Bab 4.3 - Modul M.1 & M.8)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    from middleware.rbac_guard import get_module_submenus
    role = session_state.get('role', '')

    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')

        # Get visible submenus for M1 and M8
        submenus_m1 = get_module_submenus('M1', role)
        submenus_m8 = get_module_submenus('M8', role)
        submenus = submenus_m1 + submenus_m8

        if not submenus:
            console.print("⛔ ERR-AUTH-003: Anda tidak memiliki akses ke modul ini.", style="bold red")
            input("Tekan Enter untuk melanjutkan...")
            return

        # Breadcrumb panel
        console.print(Panel(
            "[bold white]MODUL M.1 & M.8 — TRANSAKSI PENJUALAN & CRM[/]\n"
            "[blue]Dashboard > Transaksi & CRM[/]",
            style="bold white",
            expand=False
        ))
        console.print()
        console.print("[bold white]SUB-MENU LOKAL:[/]")

        for idx, (menu_id, label, level) in enumerate(submenus, start=1):
            console.print(f"  [{idx}] {label} [bold green][{level}][/]")

        console.print()
        console.print("  [0] Kembali ke Dashboard")
        console.print("  [q] Keluar Aplikasi")
        console.print()

        try:
            raw_pilihan = input("Pilih Sub-Menu [1-N / 0 / q]: ")
            pilihan = sanitasi_input_cli(raw_pilihan).strip()
        except (EOFError, KeyboardInterrupt):
            from cli.dashboard import graceful_exit
            graceful_exit(session_state)
            return

        if pilihan == '0':
            return
        elif pilihan.lower() == 'q':
            from cli.dashboard import graceful_exit
            graceful_exit(session_state)
            return

        try:
            val_idx = int(pilihan)
            if 1 <= val_idx <= len(submenus):
                selected_menu_id = submenus[val_idx - 1][0]
                if selected_menu_id == 'MENU-M1-001':
                    form_pencatatan_transaksi(session_state)
                elif selected_menu_id == 'MENU-M1-003':
                    form_dp_pelunasan(session_state)
                elif selected_menu_id == 'MENU-M1-004':
                    form_retur_pembatalan(session_state)
                elif selected_menu_id == 'MENU-M8-001':
                    form_crm_pelanggan(session_state)
                else:
                    print(f"[PLACEHOLDER] Menu '{submenus[val_idx - 1][1]}' belum diimplementasikan.")
                    input("Tekan Enter untuk melanjutkan...")
            else:
                print(f"⛔ Pilihan '{pilihan}' tidak valid. Harap masukkan angka 1-{len(submenus)}, 0, atau q.")
                input("Tekan Enter untuk melanjutkan...")
        except ValueError:
            print("⛔ Pilihan tidak valid. Harap masukkan angka.")
            input("Tekan Enter untuk melanjutkan...")


def form_pencatatan_transaksi(session_state: dict) -> None:
    """Formulir transaksi ATK retail or kustom cetak.

    (Ref: Module Structure Bab 4.3 - Modul M.1)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi formulir pencatatan transaksi
    print("[PLACEHOLDER] Menu belum diimplementasikan.")
    input("Tekan Enter untuk melanjutkan...")


def form_dp_pelunasan(session_state: dict) -> None:
    """Formulir pencatatan uang muka (DP) pesanan kustom.

    (Ref: Module Structure Bab 4.3 - Modul M.1)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi formulir DP/pelunasan
    print("[PLACEHOLDER] Menu belum diimplementasikan.")
    input("Tekan Enter untuk melanjutkan...")


def form_retur_pembatalan(session_state: dict) -> None:
    """Formulir pembatalan transaksi atau retur barang.

    (Ref: Module Structure Bab 4.3 - Modul M.1 & M.8)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi formulir retur/batal
    print("[PLACEHOLDER] Menu belum diimplementasikan.")
    input("Tekan Enter untuk melanjutkan...")


@require_role('MENU-M8-001')
def form_crm_pelanggan(session_state: dict) -> None:
    """Formulir registrasi dan kelola profil keanggotaan pelanggan CRM.

    (Ref: CLI Interaction Flow Bab 12.1, UC-038, MENU-M8-001)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')

        console.print(Panel(
            "[bold white]M.8 MANAJEMEN DATABASE PELANGGAN (CRM)[/]\n"
            "[blue]Dashboard > M.8 CRM > Database CRM[/]",
            style="bold white",
            expand=False
        ))
        console.print()
        console.print("  [1] Daftarkan Pelanggan Baru")
        console.print("  [2] Cari Riwayat Transaksi Pelanggan")
        console.print("  [3] Lihat Daftar Semua Pelanggan")
        console.print("  [4] Edit Data Pelanggan")
        console.print("  [0] Kembali ke Menu Transaksi")
        console.print()

        try:
            raw_pilihan = input("Pilihan Anda [0-4]: ")
            pilihan = sanitasi_input_cli(raw_pilihan).strip()
        except (EOFError, KeyboardInterrupt):
            return

        if pilihan == '0':
            return

        if pilihan == '1':
            _form_daftar_pelanggan_baru(session_state)
        elif pilihan == '2':
            _form_cari_riwayat_pelanggan(session_state)
        elif pilihan == '3':
            _form_lihat_daftar_pelanggan(session_state)
        elif pilihan == '4':
            _form_edit_pelanggan(session_state)
        else:
            console.print("⛔ Pilihan tidak valid. Harap masukkan angka 0-4.", style="bold red")
            input("Tekan Enter untuk melanjutkan...")


def _form_daftar_pelanggan_baru(session_state: dict) -> None:
    """Sub-menu: Daftarkan pelanggan baru ke database CRM terenkripsi.

    (Ref: CLI Interaction Flow Bab 12.1, UC-038)
    """
    os.system('cls' if platform.system() == 'Windows' else 'clear')

    console.print(Panel(
        "[bold white]DAFTAR PELANGGAN BARU[/]\n"
        "[blue]Dashboard > M.8 CRM > Database CRM > Daftar Baru[/]",
        style="bold white",
        expand=False
    ))
    console.print()

    # Load settings to get FERNET_KEY
    try:
        app_settings = load_settings()
        fernet_key = app_settings.fernet_key
    except Exception as e:
        console.print(f"⛔ Gagal memuat konfigurasi: {str(e)}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return

    cabang_id = session_state.get('cabang_id', 1)
    user_id = session_state.get('user_id', 1)

    # 1. Input Nama
    nama_raw = input("Nama Pelanggan: ")
    val_nama = validasi_nama_pelanggan(nama_raw)
    if not val_nama.is_valid:
        console.print(f"{val_nama.error_msg}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return

    # 2. Input WhatsApp
    wa_raw = input("Nomor WhatsApp: ")
    val_wa = validasi_nomor_whatsapp(wa_raw)
    if not val_wa.is_valid:
        console.print(f"{val_wa.error_msg}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return

    nama_sanitized = val_nama.sanitized_data
    wa_sanitized = val_wa.sanitized_data

    # 3. Enkripsi WhatsApp
    wa_encrypted = encrypt_whatsapp_number(wa_sanitized, fernet_key)
    if not wa_encrypted:
        console.print("⛔ ERR-CRM-CRYPTO: Gagal mengenkripsi nomor WhatsApp pelanggan!", style="bold red")
        input("Tekan Enter untuk kembali...")
        return

    # 4. Simpan ke database
    conn_res = get_db_connection()
    if not conn_res.is_success:
        console.print(f"⛔ {conn_res.error_msg}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return
    conn = conn_res.data

    try:
        db_res = insert_pelanggan_baru(conn, nama_sanitized, wa_encrypted, cabang_id)
        if not db_res.is_success:
            console.print(f"{db_res.error_msg}", style="bold red")
            input("Tekan Enter untuk kembali...")
            return

        new_pelanggan_id = db_res.data
        client_code = f"CRM-{new_pelanggan_id:03d}" if new_pelanggan_id < 1000 else f"CRM-{new_pelanggan_id}"

        # 5. Log Audit Trail
        log_audit_trail(
            pengguna_id=user_id,
            action_type='INSERT',
            target_table='pelanggan',
            old_val=None,
            new_val={'nama_pelanggan': nama_sanitized, 'whatsapp': '[ENCRYPTED]', 'cabang_id': cabang_id},
            cabang_id=cabang_id,
            db_connection=conn
        )

        console.print(f"[bold green]✓ Registrasi CRM Berhasil! ID Klien: {client_code}.[/]")
        console.print("[green]Data WhatsApp terenkripsi mematuhi UU PDP No. 27/2022.[/]")
        input("Tekan Enter untuk melanjutkan...")
    finally:
        try:
            conn.close()
        except Exception:
            pass


def _form_cari_riwayat_pelanggan(session_state: dict) -> None:
    """Sub-menu: Cari dan tampilkan riwayat transaksi pelanggan CRM."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

    console.print(Panel(
        "[bold white]CARI RIWAYAT TRANSAKSI PELANGGAN[/]\n"
        "[blue]Dashboard > M.8 CRM > Database CRM > Cari Riwayat[/]",
        style="bold white",
        expand=False
    ))
    console.print()

    # Load settings to get FERNET_KEY
    try:
        app_settings = load_settings()
        fernet_key = app_settings.fernet_key
    except Exception as e:
        console.print(f"⛔ Gagal memuat konfigurasi: {str(e)}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return

    cabang_id = session_state.get('cabang_id', 1)

    # 1. Input WhatsApp
    wa_raw = input("Nomor WhatsApp Pelanggan: ")
    val_wa = validasi_nomor_whatsapp(wa_raw)
    if not val_wa.is_valid:
        console.print(f"{val_wa.error_msg}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return

    wa_sanitized = val_wa.sanitized_data
    wa_encrypted = encrypt_whatsapp_number(wa_sanitized, fernet_key)

    # 2. Cari di database
    conn_res = get_db_connection()
    if not conn_res.is_success:
        console.print(f"⛔ {conn_res.error_msg}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return
    conn = conn_res.data

    try:
        db_res = cari_pelanggan_by_whatsapp(conn, wa_encrypted, cabang_id)
        if not db_res.is_success:
            console.print(f"⛔ {db_res.error_msg}", style="bold red")
            input("Tekan Enter untuk kembali...")
            return

        pelanggan = db_res.data
        if not pelanggan:
            console.print("[bold yellow]⚠️ Pelanggan dengan nomor WhatsApp tersebut tidak ditemukan.[/]")
            input("Tekan Enter untuk melanjutkan...")
            return

        # Dekripsi WA untuk ditampilkan
        wa_decrypted = decrypt_whatsapp_number(pelanggan['whatsapp'], fernet_key)
        client_code = f"CRM-{pelanggan['id']:03d}" if pelanggan['id'] < 1000 else f"CRM-{pelanggan['id']}"

        console.print(Panel(
            f"[bold white]ID Klien      :[/] {client_code}\n"
            f"[bold white]Nama Pelanggan:[/] {pelanggan['nama_pelanggan']}\n"
            f"[bold white]WhatsApp      :[/] {wa_decrypted}\n"
            f"[bold white]Tgl Terdaftar :[/] {pelanggan['tanggal_terdaftar']}",
            title="Profil Pelanggan",
            expand=False
        ))
        console.print()

        # 3. Ambil riwayat transaksi
        tx_res = get_riwayat_transaksi_pelanggan(conn, pelanggan['id'], cabang_id)
        if not tx_res.is_success:
            console.print(f"⛔ {tx_res.error_msg}", style="bold red")
            input("Tekan Enter untuk kembali...")
            return

        transactions = tx_res.data
        if not transactions:
            console.print("[yellow]Tidak ada riwayat transaksi untuk pelanggan ini.[/]")
            input("Tekan Enter untuk kembali...")
            return

        # 4. Render tabel transaksi
        headers = ["No.", "No. Invoice", "Tanggal", "Total Bayar", "Status", "Tipe"]
        table_rows = []
        for idx, tx in enumerate(transactions, start=1):
            total_bayar_str = f"Rp {tx['total_bayar']:,.4f}".replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
            if ",0000" in total_bayar_str:
                total_bayar_str = total_bayar_str.replace(",0000", "")
            table_rows.append([
                idx,
                tx['no_invoice'],
                tx['tanggal_transaksi'],
                total_bayar_str,
                tx['status_pembayaran'],
                tx['tipe_pelanggan']
            ])

        table_str = tabulate(table_rows, headers=headers, tablefmt="grid")
        console.print(table_str)
        console.print()
        input("Tekan Enter untuk kembali...")
    finally:
        try:
            conn.close()
        except Exception:
            pass


def _form_lihat_daftar_pelanggan(session_state: dict) -> None:
    """Sub-menu: Tampilkan daftar seluruh pelanggan CRM terdaftar."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

    console.print(Panel(
        "[bold white]DAFTAR SELURUH PELANGGAN CRM[/]\n"
        "[blue]Dashboard > M.8 CRM > Database CRM > Lihat Semua[/]",
        style="bold white",
        expand=False
    ))
    console.print()

    # Load settings to get FERNET_KEY
    try:
        app_settings = load_settings()
        fernet_key = app_settings.fernet_key
    except Exception as e:
        console.print(f"⛔ Gagal memuat konfigurasi: {str(e)}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return

    cabang_id = session_state.get('cabang_id', 1)

    conn_res = get_db_connection()
    if not conn_res.is_success:
        console.print(f"⛔ {conn_res.error_msg}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return
    conn = conn_res.data

    try:
        db_res = get_daftar_pelanggan(conn, cabang_id, limit=100)
        if not db_res.is_success:
            console.print(f"⛔ {db_res.error_msg}", style="bold red")
            input("Tekan Enter untuk kembali...")
            return

        customers = db_res.data
        if not customers:
            console.print("[yellow]Tidak ada pelanggan terdaftar di CRM cabang ini.[/]")
            input("Tekan Enter untuk kembali...")
            return

        headers = ["ID Klien", "Nama Pelanggan", "WhatsApp", "Tanggal Daftar"]
        table_rows = []
        for cust in customers:
            wa_decrypted = decrypt_whatsapp_number(cust['whatsapp'], fernet_key)
            client_code = f"CRM-{cust['id']:03d}" if cust['id'] < 1000 else f"CRM-{cust['id']}"
            table_rows.append([
                client_code,
                cust['nama_pelanggan'],
                wa_decrypted,
                cust['tanggal_terdaftar']
            ])

        table_str = tabulate(table_rows, headers=headers, tablefmt="grid")
        console.print(table_str)
        console.print()
        input("Tekan Enter untuk kembali...")
    finally:
        try:
            conn.close()
        except Exception:
            pass


def _form_edit_pelanggan(session_state: dict) -> None:
    """Sub-menu: Edit data nama atau WhatsApp pelanggan existing."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

    console.print(Panel(
        "[bold white]EDIT DATA PROFIL PELANGGAN[/]\n"
        "[blue]Dashboard > M.8 CRM > Database CRM > Edit Profil[/]",
        style="bold white",
        expand=False
    ))
    console.print()

    # Load settings to get FERNET_KEY
    try:
        app_settings = load_settings()
        fernet_key = app_settings.fernet_key
    except Exception as e:
        console.print(f"⛔ Gagal memuat konfigurasi: {str(e)}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return

    cabang_id = session_state.get('cabang_id', 1)
    user_id = session_state.get('user_id', 1)

    raw_id = input("Masukkan ID Pelanggan yang ingin diedit (misal: 54 atau CRM-054): ").strip()
    if not raw_id:
        return

    # Parse ID if starts with 'CRM-'
    parsed_id = raw_id
    if raw_id.upper().startswith("CRM-"):
        parsed_id = raw_id[4:]

    try:
        pelanggan_id = int(parsed_id)
    except ValueError:
        console.print("⛔ ID pelanggan harus berupa angka!", style="bold red")
        input("Tekan Enter untuk kembali...")
        return

    conn_res = get_db_connection()
    if not conn_res.is_success:
        console.print(f"⛔ {conn_res.error_msg}", style="bold red")
        input("Tekan Enter untuk kembali...")
        return
    conn = conn_res.data

    try:
        # 1. Fetch current data
        query = "SELECT id, nama_pelanggan, whatsapp, tanggal_terdaftar FROM pelanggan WHERE id = %s AND cabang_id = %s"
        cust_res = execute_query(conn, query, (pelanggan_id, cabang_id), fetch_one=True)
        if not cust_res.is_success or not cust_res.data:
            console.print("⛔ ID pelanggan tidak ditemukan di cabang ini.", style="bold red")
            input("Tekan Enter untuk kembali...")
            return

        cust = cust_res.data
        wa_decrypted = decrypt_whatsapp_number(cust['whatsapp'], fernet_key)

        console.print(Panel(
            f"Nama Pelanggan: {cust['nama_pelanggan']}\n"
            f"WhatsApp      : {wa_decrypted}",
            title="Data Pelanggan Saat Ini",
            expand=False
        ))
        console.print()

        # 2. Prompt for new values
        new_nama_raw = input(f"Nama Baru [Enter=tetap '{cust['nama_pelanggan']}']: ")
        new_wa_raw = input(f"WhatsApp Baru [Enter=tetap '{wa_decrypted}']: ")

        nama_to_update = None
        wa_encrypted_to_update = None

        if new_nama_raw:
            val_nama = validasi_nama_pelanggan(new_nama_raw)
            if not val_nama.is_valid:
                console.print(f"{val_nama.error_msg}", style="bold red")
                input("Tekan Enter untuk kembali...")
                return
            nama_to_update = val_nama.sanitized_data

        if new_wa_raw:
            val_wa = validasi_nomor_whatsapp(new_wa_raw)
            if not val_wa.is_valid:
                console.print(f"{val_wa.error_msg}", style="bold red")
                input("Tekan Enter untuk kembali...")
                return
            wa_encrypted_to_update = encrypt_whatsapp_number(val_wa.sanitized_data, fernet_key)

        if nama_to_update is None and wa_encrypted_to_update is None:
            console.print("[yellow]Tidak ada perubahan data yang dilakukan.[/]")
            input("Tekan Enter untuk kembali...")
            return

        # 3. Update database
        upd_res = update_pelanggan(conn, pelanggan_id, nama_to_update, wa_encrypted_to_update, cabang_id)
        if not upd_res.is_success:
            console.print(f"{upd_res.error_msg}", style="bold red")
            input("Tekan Enter untuk kembali...")
            return

        # 4. Log Audit Trail
        old_val_dict = {
            'nama_pelanggan': cust['nama_pelanggan'],
            'whatsapp': '[ENCRYPTED]',
            'cabang_id': cabang_id
        }
        new_val_dict = {
            'nama_pelanggan': nama_to_update if nama_to_update is not None else cust['nama_pelanggan'],
            'whatsapp': '[ENCRYPTED]',
            'cabang_id': cabang_id
        }
        log_audit_trail(
            pengguna_id=user_id,
            action_type='UPDATE',
            target_table='pelanggan',
            old_val=old_val_dict,
            new_val=new_val_dict,
            cabang_id=cabang_id,
            db_connection=conn
        )

        console.print("[bold green]✓ Perubahan data profil pelanggan berhasil disimpan.[/]")
        input("Tekan Enter untuk melanjutkan...")
    finally:
        try:
            conn.close()
        except Exception:
            pass

