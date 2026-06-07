"""
Nama Modul: menu_inventaris.py
Deskripsi: Antarmuka kelola stok, BOM, opname, supplier, antrian cetak, dan arsip desain.
           (Ref: Module Structure Bab 4.4)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import os
import platform
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from tabulate import tabulate

from db.db_connector import get_db_connection
from db.query_builder import (
    query_daftar_barang, query_detail_barang, query_insert_barang,
    query_update_barang, query_delete_barang, query_cek_nama_barang_duplikat
)
from logic.bom_hpp import validasi_data_barang, buat_audit_payload_barang, hitung_margin_barang
from logic.safety_validator import sanitasi_input_cli
from middleware.rbac_guard import require_role
from middleware.audit_logger import log_audit_trail

console = Console()


def _prompt_input(prompt_text: str) -> str:
    """Helper internal untuk mengambil input dari pengguna dan mensanitasinya."""
    raw = input(prompt_text)
    return sanitasi_input_cli(raw).strip()


def show_menu_inventaris(session_state: dict) -> None:
    """Menampilkan panel utama manajemen inventaris & antrian desain.

    (Ref: Module Structure Bab 4.4 - Modul M.2 & M.5)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    from middleware.rbac_guard import get_module_submenus
    
    role = session_state.get('role', '')
    
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        
        # Get visible submenus for M2 and M5
        submenus_m2 = get_module_submenus('M2', role)
        submenus_m5 = get_module_submenus('M5', role)
        submenus = submenus_m2 + submenus_m5
        
        if not submenus:
            console.print("⛔ ERR-AUTH-003: Anda tidak memiliki akses ke modul ini.", style="bold red")
            input("Tekan Enter untuk melanjutkan...")
            return

        # Breadcrumb panel
        console.print(Panel(
            "[bold white]MODUL M.2 & M.5 — INVENTARIS, BOM & ANTRIAN[/]\n"
            "[blue]Dashboard > Inventaris & Antrian[/]",
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
                if selected_menu_id == 'MENU-M2-001':
                    form_kelola_barang(session_state)
                elif selected_menu_id == 'MENU-M2-002':
                    form_komposisi_bom(session_state)
                elif selected_menu_id == 'MENU-M2-003':
                    form_mencatat_limbah(session_state)
                elif selected_menu_id == 'MENU-M2-005':
                    form_stock_opname(session_state)
                elif selected_menu_id == 'MENU-M2-008':
                    form_import_csv(session_state)
                elif selected_menu_id == 'MENU-M2-009':
                    form_kelola_supplier(session_state)
                elif selected_menu_id == 'MENU-M2-010':
                    trigger_backup_restore(session_state)
                elif selected_menu_id == 'MENU-M5-001':
                    form_job_tracking_antrian(session_state)
                elif selected_menu_id == 'MENU-M5-002':
                    form_arsip_desain(session_state)
                elif selected_menu_id == 'MENU-M5-003':
                    trigger_whatsapp_link(session_state)
                else:
                    print(f"[PLACEHOLDER] Menu '{submenus[val_idx - 1][1]}' belum diimplementasikan.")
                    input("Tekan Enter untuk melanjutkan...")
            else:
                print(f"⛔ Pilihan '{pilihan}' tidak valid. Harap masukkan angka 1-{len(submenus)}, 0, atau q.")
                input("Tekan Enter untuk melanjutkan...")
        except ValueError:
            print("⛔ Pilihan tidak valid. Harap masukkan angka.")
            input("Tekan Enter untuk melanjutkan...")


@require_role('MENU-M2-001')
def form_kelola_barang(session_state: dict) -> None:
    """Formulir kelola master data barang (stok & harga).

    (Ref: Module Structure Bab 4.4 - Modul M.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    role = session_state.get('role', '')
    is_read_only = role == 'produksi_cetak'
    
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        console.print(Panel(
            "[bold white]MANAJEMEN MASTER DATA BARANG[/]\n"
            "[blue]Dashboard > M.2 Inventaris > Kelola Barang[/]",
            style="bold white",
            expand=False
        ))
        console.print()
        console.print("  [1] Lihat Daftar Barang")
        console.print("  [2] Tambah Barang Baru")
        console.print("  [3] Ubah Data Barang")
        console.print("  [4] Hapus Barang")
        console.print("  [5] Lihat Detail Barang")
        console.print("  [0] Kembali ke Menu Inventaris")
        console.print()
        
        try:
            raw_pilihan = input("Pilihan Anda [0-5]: ")
            pilihan = sanitasi_input_cli(raw_pilihan).strip()
        except (EOFError, KeyboardInterrupt):
            return
            
        if pilihan == '0':
            return
            
        if pilihan == '1':
            _lihat_daftar_barang(session_state)
        elif pilihan == '2':
            if is_read_only:
                console.print("⛔ ERR-AUTH-003: Akses Ditolak: Peran Anda hanya diizinkan melihat data barang!", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
            else:
                _tambah_barang_baru(session_state)
        elif pilihan == '3':
            if is_read_only:
                console.print("⛔ ERR-AUTH-003: Akses Ditolak: Peran Anda hanya diizinkan melihat data barang!", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
            else:
                _ubah_data_barang(session_state)
        elif pilihan == '4':
            if is_read_only:
                console.print("⛔ ERR-AUTH-003: Akses Ditolak: Peran Anda hanya diizinkan melihat data barang!", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
            else:
                _hapus_barang(session_state)
        elif pilihan == '5':
            _lihat_detail_barang(session_state)
        else:
            console.print("⛔ Pilihan tidak valid. Harap masukkan angka 0-5.", style="bold red")
            input("Tekan Enter untuk melanjutkan...")


def _lihat_daftar_barang(session_state: dict) -> None:
    """Menampilkan tabel daftar master barang terformat tabulate."""
    cabang_id = session_state.get('cabang_id', 1)
    
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    console.print(Panel(
        "[bold white]DAFTAR MASTER BARANG[/]\n"
        "[blue]Dashboard > M.2 > Kelola Barang > Lihat Daftar Barang[/]",
        style="bold white",
        expand=False
    ))
    console.print()
    
    console.print("Filter Tipe Barang:")
    console.print("  [1] Semua")
    console.print("  [2] Retail ATK")
    console.print("  [3] Bahan Baku")
    raw_filter = _prompt_input("Pilihan Filter [1-3] [Enter=Semua]: ")
    
    tipe_barang = None
    if raw_filter == '2':
        tipe_barang = 'Retail_ATK'
    elif raw_filter == '3':
        tipe_barang = 'Bahan_Baku'
        
    keyword = _prompt_input("Cari nama barang (Enter=skip): ")
    if not keyword:
        keyword = None
        
    conn_res = get_db_connection()
    if not conn_res.is_success:
        console.print(f"⛔ {conn_res.error_msg}", style="bold red")
        input("Tekan Enter untuk melanjutkan...")
        return
    conn = conn_res.data
    
    try:
        db_res = query_daftar_barang(conn, cabang_id, tipe_barang, keyword)
        if not db_res.is_success:
            console.print(f"⛔ {db_res.error_msg}", style="bold red")
            input("Tekan Enter untuk melanjutkan...")
            return
            
        data = db_res.data
        if not data:
            console.print("[yellow]Tidak ada data barang ditemukan.[/]", style="bold yellow")
            input("Tekan Enter untuk melanjutkan...")
            return
            
        rows = []
        for idx, row in enumerate(data, start=1):
            stok_val = row['stok_saat_ini']
            if stok_val <= 0:
                stok_str = f"[bold red]{stok_val:,.4f}[/]"
            elif stok_val <= 5:
                stok_str = f"[bold yellow]{stok_val:,.4f}[/]"
            else:
                stok_str = f"{stok_val:,.4f}"
                
            rows.append([
                idx,
                row['id'],
                row['nama_barang'],
                row['tipe_barang'],
                row['satuan_uom'],
                stok_str,
                f"Rp {row['harga_beli']:,.4f}",
                f"Rp {row['harga_retail']:,.4f}",
                f"Rp {row['harga_grosir']:,.4f}",
                f"Rp {row['harga_mitra']:,.4f}"
            ])
            
        headers = ["No", "ID", "Nama Barang", "Tipe", "Satuan", "Stok", "H.Beli", "H.Retail", "H.Grosir", "H.Mitra"]
        table_str = tabulate(rows, headers=headers, tablefmt="grid")
        console.print(table_str)
        console.print()
        input("Tekan Enter untuk kembali...")
    finally:
        conn.close()


def _tambah_barang_baru(session_state: dict) -> None:
    """Formulir input tambah barang retail ATK atau bahan baku baru."""
    cabang_id = session_state.get('cabang_id', 1)
    user_id = session_state.get('user_id', 1)
    
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        console.print(Panel(
            "[bold white]TAMBAH BARANG BARU[/]\n"
            "[blue]Dashboard > M.2 > Kelola Barang > Tambah Barang Baru[/]",
            style="bold white",
            expand=False
        ))
        console.print()
        
        try:
            # 1. Tipe Barang
            console.print("Pilih Tipe Barang:")
            console.print("  [1] Retail ATK")
            console.print("  [2] Bahan Baku")
            console.print("  [0] Batal")
            raw_tipe = _prompt_input("Pilihan Anda [0-2]: ")
            if raw_tipe == '0':
                return
            elif raw_tipe == '1':
                tipe_barang = 'Retail_ATK'
            elif raw_tipe == '2':
                tipe_barang = 'Bahan_Baku'
            else:
                console.print("⛔ Pilihan tidak valid. Harap pilih 0-2.", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
                continue

            # 2. Nama Barang
            nama_barang = _prompt_input("Masukkan Nama Barang: ")
            if not nama_barang:
                console.print("⛔ Nama barang tidak boleh kosong!", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
                continue
                
            # 3. Satuan UoM
            console.print("Pilih Satuan UoM:")
            console.print("  [1] Rim")
            console.print("  [2] Lembar")
            console.print("  [3] Pcs")
            console.print("  [4] Ml")
            console.print("  [5] Meter Persegi")
            raw_uom = _prompt_input("Pilihan Anda [1-5]: ")
            uom_map = {'1': 'Rim', '2': 'Lembar', '3': 'Pcs', '4': 'Ml', '5': 'Meter_Persegi'}
            satuan_uom = uom_map.get(raw_uom)
            if not satuan_uom:
                console.print("⛔ Satuan UoM tidak valid.", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
                continue

            # 4. Stok Awal
            stok_raw = _prompt_input("Masukkan Stok Awal (contoh: 12.50): ")
            
            # 5. Harga Beli
            harga_beli_raw = _prompt_input("Masukkan Harga Beli / HPP: ")

            data_form = {
                'nama_barang': nama_barang,
                'tipe_barang': tipe_barang,
                'satuan_uom': satuan_uom,
                'stok_saat_ini': stok_raw,
                'harga_beli': harga_beli_raw,
                'cabang_id': cabang_id
            }

            # 6. Retail prices if Retail_ATK
            if tipe_barang == 'Retail_ATK':
                data_form['harga_retail'] = _prompt_input("Masukkan Harga Retail: ")
                data_form['harga_grosir'] = _prompt_input("Masukkan Harga Grosir: ")
                
                raw_min_grosir = _prompt_input("Masukkan Min Grosir [Enter=default 1.0000]: ")
                data_form['min_grosir'] = raw_min_grosir if raw_min_grosir else '1.0000'
                
                data_form['harga_mitra'] = _prompt_input("Masukkan Harga Mitra: ")
            else:
                data_form['harga_retail'] = '0.0000'
                data_form['harga_grosir'] = '0.0000'
                data_form['min_grosir'] = '1.0000'
                data_form['harga_mitra'] = '0.0000'

            # Panggil validasi logic layer
            val_res = validasi_data_barang(data_form)
            if not val_res.is_valid:
                console.print(f"{val_res.error_msg}", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
                continue
                
            cleaned = val_res.cleaned_data
            
            # Cek duplikasi nama
            conn_res = get_db_connection()
            if not conn_res.is_success:
                console.print(f"⛔ {conn_res.error_msg}", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
                return
            conn = conn_res.data
            
            try:
                dup_res = query_cek_nama_barang_duplikat(conn, cleaned['nama_barang'], cabang_id)
                if not dup_res.is_success:
                    console.print(f"⛔ {dup_res.error_msg}", style="bold red")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                if dup_res.data:
                    console.print(f"⛔ Nama barang '{cleaned['nama_barang']}' sudah terdaftar di cabang ini!", style="bold red")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                    
                # Tampilkan Ringkasan
                console.print()
                console.print(Panel(
                    f"[bold white]Ringkasan Barang Baru:[/]\n"
                    f"Nama Barang   : {cleaned['nama_barang']}\n"
                    f"Tipe Barang   : {cleaned['tipe_barang']}\n"
                    f"Satuan UoM    : {cleaned['satuan_uom']}\n"
                    f"Stok Awal     : {cleaned['stok_saat_ini']:,.4f}\n"
                    f"Harga Beli/HPP: Rp {cleaned['harga_beli']:,.4f}\n"
                    f"Harga Retail  : Rp {cleaned['harga_retail']:,.4f}\n"
                    f"Harga Grosir  : Rp {cleaned['harga_grosir']:,.4f} (Min: {cleaned['min_grosir']:,.4f})\n"
                    f"Harga Mitra   : Rp {cleaned['harga_mitra']:,.4f}",
                    title="Konfirmasi Tambah Barang",
                    expand=False
                ))
                
                raw_confirm = _prompt_input("Apakah data di atas sudah benar? [Y/N]: ")
                if raw_confirm.upper() == 'Y':
                    ins_res = query_insert_barang(conn, cleaned)
                    if not ins_res.is_success:
                        console.print(f"⛔ {ins_res.error_msg}", style="bold red")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                        
                    last_id = ins_res.data
                    
                    # Audit Trail
                    cleaned_with_id = {'id': last_id, **cleaned}
                    old_payload, new_payload = buat_audit_payload_barang('INSERT', None, cleaned_with_id)
                    
                    log_audit_trail(
                        pengguna_id=user_id,
                        action_type='INSERT',
                        target_table='barang',
                        old_val=None,
                        new_val=json.loads(new_payload),
                        cabang_id=cabang_id,
                        db_connection=conn
                    )
                    
                    console.print(f"[bold green]✓ Barang baru berhasil ditambahkan dengan ID {last_id}! Dimuat ke database.[/]")
                    input("Tekan Enter untuk melanjutkan...")
                    return
                else:
                    console.print("[yellow]Pendaftaran barang dibatalkan.[/]")
                    input("Tekan Enter untuk melanjutkan...")
                    return
            finally:
                conn.close()

        except (EOFError, KeyboardInterrupt):
            return


def _ubah_data_barang(session_state: dict) -> None:
    """Formulir edit master data barang yang sudah ada."""
    cabang_id = session_state.get('cabang_id', 1)
    user_id = session_state.get('user_id', 1)
    
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        console.print(Panel(
            "[bold white]UBAH DATA BARANG[/]\n"
            "[blue]Dashboard > M.2 > Kelola Barang > Ubah Data Barang[/]",
            style="bold white",
            expand=False
        ))
        console.print()
        
        try:
            raw_id = _prompt_input("Masukkan ID Barang yang akan diubah [0-Batal]: ")
            if raw_id == '0' or not raw_id:
                return
                
            try:
                barang_id = int(raw_id)
            except ValueError:
                console.print("⛔ ID barang harus berupa angka!", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
                continue
                
            conn_res = get_db_connection()
            if not conn_res.is_success:
                console.print(f"⛔ {conn_res.error_msg}", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
                return
            conn = conn_res.data
            
            try:
                detail_res = query_detail_barang(conn, barang_id, cabang_id)
                if not detail_res.is_success or not detail_res.data:
                    console.print("⛔ ERR-VAL-009: ID barang tidak ditemukan.", style="bold red")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                    
                barang = detail_res.data['barang']
                
                # Tampilkan data saat ini
                console.print(Panel(
                    f"Nama Barang   : {barang['nama_barang']}\n"
                    f"Tipe Barang   : {barang['tipe_barang']} (Read-Only)\n"
                    f"Satuan UoM    : {barang['satuan_uom']}\n"
                    f"Stok Saat Ini : {barang['stok_saat_ini']:,.4f}\n"
                    f"Harga Beli/HPP: Rp {barang['harga_beli']:,.4f}\n"
                    f"Harga Retail  : Rp {barang['harga_retail']:,.4f}\n"
                    f"Harga Grosir  : Rp {barang['harga_grosir']:,.4f} (Min: {barang['min_grosir']:,.4f})\n"
                    f"Harga Mitra   : Rp {barang['harga_mitra']:,.4f}",
                    title="Data Barang Saat Ini",
                    expand=False
                ))
                console.print()
                
                # Prompt fields
                # 1. Nama
                new_nama = _prompt_input(f"Nama Barang [Enter=tetap '{barang['nama_barang']}']: ")
                if not new_nama:
                    new_nama = barang['nama_barang']
                    
                # 2. Satuan
                console.print("Pilih Satuan UoM:")
                console.print("  [1] Rim")
                console.print("  [2] Lembar")
                console.print("  [3] Pcs")
                console.print("  [4] Ml")
                console.print("  [5] Meter Persegi")
                raw_uom = _prompt_input(f"Pilihan Anda [Enter=tetap '{barang['satuan_uom']}']: ")
                if raw_uom:
                    uom_map = {'1': 'Rim', '2': 'Lembar', '3': 'Pcs', '4': 'Ml', '5': 'Meter_Persegi'}
                    new_uom = uom_map.get(raw_uom)
                    if not new_uom:
                        console.print("⛔ Satuan UoM tidak valid.", style="bold red")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                else:
                    new_uom = barang['satuan_uom']
                    
                # 3. Stok
                new_stok_raw = _prompt_input(f"Stok [Enter=tetap {barang['stok_saat_ini']:,.4f}]: ")
                if not new_stok_raw:
                    new_stok_raw = str(barang['stok_saat_ini'])
                    
                # 4. Harga Beli
                new_harga_beli_raw = _prompt_input(f"Harga Beli / HPP [Enter=tetap Rp {barang['harga_beli']:,.4f}]: ")
                if not new_harga_beli_raw:
                    new_harga_beli_raw = str(barang['harga_beli'])
                    
                data_form = {
                    'nama_barang': new_nama,
                    'tipe_barang': barang['tipe_barang'],
                    'satuan_uom': new_uom,
                    'stok_saat_ini': new_stok_raw,
                    'harga_beli': new_harga_beli_raw,
                    'cabang_id': cabang_id
                }
                
                if barang['tipe_barang'] == 'Retail_ATK':
                    new_harga_retail_raw = _prompt_input(f"Harga Retail [Enter=tetap Rp {barang['harga_retail']:,.4f}]: ")
                    data_form['harga_retail'] = new_harga_retail_raw if new_harga_retail_raw else str(barang['harga_retail'])
                    
                    new_harga_grosir_raw = _prompt_input(f"Harga Grosir [Enter=tetap Rp {barang['harga_grosir']:,.4f}]: ")
                    data_form['harga_grosir'] = new_harga_grosir_raw if new_harga_grosir_raw else str(barang['harga_grosir'])
                    
                    new_min_grosir_raw = _prompt_input(f"Min Grosir [Enter=tetap {barang['min_grosir']:,.4f}]: ")
                    data_form['min_grosir'] = new_min_grosir_raw if new_min_grosir_raw else str(barang['min_grosir'])
                    
                    new_harga_mitra_raw = _prompt_input(f"Harga Mitra [Enter=tetap Rp {barang['harga_mitra']:,.4f}]: ")
                    data_form['harga_mitra'] = new_harga_mitra_raw if new_harga_mitra_raw else str(barang['harga_mitra'])
                else:
                    data_form['harga_retail'] = '0.0000'
                    data_form['harga_grosir'] = '0.0000'
                    data_form['min_grosir'] = '1.0000'
                    data_form['harga_mitra'] = '0.0000'
                    
                # Validasi
                val_res = validasi_data_barang(data_form)
                if not val_res.is_valid:
                    console.print(f"{val_res.error_msg}", style="bold red")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                    
                cleaned = val_res.cleaned_data
                
                # Cek duplikasi nama (jika nama diubah)
                if cleaned['nama_barang'].lower() != barang['nama_barang'].lower():
                    dup_res = query_cek_nama_barang_duplikat(conn, cleaned['nama_barang'], cabang_id, exclude_id=barang_id)
                    if not dup_res.is_success:
                        console.print(f"⛔ {dup_res.error_msg}", style="bold red")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                    if dup_res.data:
                        console.print(f"⛔ Nama barang '{cleaned['nama_barang']}' sudah terdaftar di cabang ini!", style="bold red")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                        
                # Cari perbedaan (diff)
                diff_lines = []
                data_update = {}
                
                fields_to_check = [
                    ('nama_barang', 'Nama Barang', False),
                    ('satuan_uom', 'Satuan UoM', False),
                    ('stok_saat_ini', 'Stok', True),
                    ('harga_beli', 'Harga Beli/HPP', True),
                    ('harga_retail', 'Harga Retail', True),
                    ('harga_grosir', 'Harga Grosir', True),
                    ('min_grosir', 'Min Grosir', True),
                    ('harga_mitra', 'Harga Mitra', True)
                ]
                
                for key, display_name, is_num in fields_to_check:
                    old_val = barang[key]
                    new_val = cleaned[key]
                    if old_val != new_val:
                        if is_num:
                            diff_lines.append(f"• {display_name}: {old_val:,.4f} -> {new_val:,.4f}")
                        else:
                            diff_lines.append(f"• {display_name}: '{old_val}' -> '{new_val}'")
                        data_update[key] = new_val
                        
                if not data_update:
                    console.print("[yellow]Tidak ada perubahan data yang dilakukan.[/]")
                    input("Tekan Enter untuk melanjutkan...")
                    return
                    
                # Tampilkan Diff
                console.print()
                console.print(Panel(
                    "\n".join(diff_lines),
                    title="Perubahan Data Barang",
                    style="yellow",
                    expand=False
                ))
                
                raw_confirm = _prompt_input("Simpan perubahan data barang? [Y/N]: ")
                if raw_confirm.upper() == 'Y':
                    upd_res = query_update_barang(conn, barang_id, data_update, cabang_id)
                    if not upd_res.is_success:
                        console.print(f"⛔ {upd_res.error_msg}", style="bold red")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                        
                    # Audit Trail
                    old_payload, new_payload = buat_audit_payload_barang('UPDATE', barang, cleaned)
                    log_audit_trail(
                        pengguna_id=user_id,
                        action_type='UPDATE',
                        target_table='barang',
                        old_val=json.loads(old_payload),
                        new_val=json.loads(new_payload),
                        cabang_id=cabang_id,
                        db_connection=conn
                    )
                    
                    console.print("[bold green]✓ Perubahan data barang berhasil disimpan ke database.[/]")
                    input("Tekan Enter untuk melanjutkan...")
                    return
                else:
                    console.print("[yellow]Perubahan data barang dibatalkan.[/]")
                    input("Tekan Enter untuk melanjutkan...")
                    return
            finally:
                conn.close()
                
        except (EOFError, KeyboardInterrupt):
            return


def _hapus_barang(session_state: dict) -> None:
    """Penghapusan barang dari master data."""
    cabang_id = session_state.get('cabang_id', 1)
    user_id = session_state.get('user_id', 1)
    
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        console.print(Panel(
            "[bold red]HAPUS DATA BARANG[/]\n"
            "[blue]Dashboard > M.2 > Kelola Barang > Hapus Barang[/]",
            style="bold red",
            expand=False
        ))
        console.print()
        
        try:
            raw_id = _prompt_input("Masukkan ID Barang yang akan dihapus [0-Batal]: ")
            if raw_id == '0' or not raw_id:
                return
                
            try:
                barang_id = int(raw_id)
            except ValueError:
                console.print("⛔ ID barang harus berupa angka!", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
                continue
                
            conn_res = get_db_connection()
            if not conn_res.is_success:
                console.print(f"⛔ {conn_res.error_msg}", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
                return
            conn = conn_res.data
            
            try:
                detail_res = query_detail_barang(conn, barang_id, cabang_id)
                if not detail_res.is_success or not detail_res.data:
                    console.print("⛔ ID barang tidak ditemukan.", style="bold red")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                    
                barang = detail_res.data['barang']
                
                # Tampilkan Warning
                console.print(Panel(
                    f"Nama Barang : {barang['nama_barang']}\n"
                    f"Tipe Barang : {barang['tipe_barang']}\n"
                    f"Stok        : {barang['stok_saat_ini']:,.4f} {barang['satuan_uom']}",
                    title="Barang yang Akan Dihapus",
                    expand=False
                ))
                console.print("[bold red]⚠️ PERINGATAN: Penghapusan data master barang bersifat PERMANEN![/]")
                
                raw_confirm = _prompt_input(f"Ketik nama barang '{barang['nama_barang']}' persis untuk konfirmasi hapus: ")
                if raw_confirm == barang['nama_barang']:
                    del_res = query_delete_barang(conn, barang_id, cabang_id)
                    if not del_res.is_success:
                        console.print(f"⛔ {del_res.error_msg}", style="bold red")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                        
                    # Audit Trail
                    old_payload, _ = buat_audit_payload_barang('DELETE', barang, None)
                    log_audit_trail(
                        pengguna_id=user_id,
                        action_type='DELETE',
                        target_table='barang',
                        old_val=json.loads(old_payload),
                        new_val=None,
                        cabang_id=cabang_id,
                        db_connection=conn
                    )
                    
                    console.print("[bold green]✓ Barang berhasil dihapus secara permanen dari database.[/]")
                    input("Tekan Enter untuk melanjutkan...")
                    return
                else:
                    console.print("[yellow]Nama barang tidak cocok. Penghapusan dibatalkan.[/]")
                    input("Tekan Enter untuk melanjutkan...")
                    return
            finally:
                conn.close()
                
        except (EOFError, KeyboardInterrupt):
            return


def _lihat_detail_barang(session_state: dict) -> None:
    """Menampilkan detail lengkap satu barang beserta info BOM."""
    cabang_id = session_state.get('cabang_id', 1)
    
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    console.print(Panel(
        "[bold white]DETAIL LENGKAP BARANG[/]\n"
        "[blue]Dashboard > M.2 > Kelola Barang > Detail Barang[/]",
        style="bold white",
        expand=False
    ))
    console.print()
    
    try:
        raw_id = _prompt_input("Masukkan ID Barang: ")
        if not raw_id:
            return
            
        try:
            barang_id = int(raw_id)
        except ValueError:
            console.print("⛔ ID barang harus berupa angka!", style="bold red")
            input("Tekan Enter untuk melanjutkan...")
            return
            
        conn_res = get_db_connection()
        if not conn_res.is_success:
            console.print(f"⛔ {conn_res.error_msg}", style="bold red")
            input("Tekan Enter untuk melanjutkan...")
            return
        conn = conn_res.data
        
        try:
            detail_res = query_detail_barang(conn, barang_id, cabang_id)
            if not detail_res.is_success or not detail_res.data:
                console.print("⛔ ID barang tidak ditemukan.", style="bold red")
                input("Tekan Enter untuk melanjutkan...")
                return
                
            data = detail_res.data
            barang = data['barang']
            bom_komponen = data['bom_komponen']
            
            stok_val = barang['stok_saat_ini']
            if stok_val <= 0:
                stok_display = f"[bold red]{stok_val:,.4f}[/]"
            elif stok_val <= 5:
                stok_display = f"[bold yellow]{stok_val:,.4f}[/]"
            else:
                stok_display = f"{stok_val:,.4f}"
                
            margin_val = hitung_margin_barang(barang['harga_retail'], barang['harga_beli'])
            
            console.print(Panel(
                f"ID Barang     : {barang['id']}\n"
                f"Nama Barang   : {barang['nama_barang']}\n"
                f"Tipe Barang   : {barang['tipe_barang']}\n"
                f"Satuan UoM    : {barang['satuan_uom']}\n"
                f"Stok Saat Ini : {stok_display}\n"
                f"Harga Beli/HPP: Rp {barang['harga_beli']:,.4f}\n"
                f"Harga Retail  : Rp {barang['harga_retail']:,.4f} (Margin: {margin_val:,.2f}%)\n"
                f"Harga Grosir  : Rp {barang['harga_grosir']:,.4f} (Min: {barang['min_grosir']:,.4f})\n"
                f"Harga Mitra   : Rp {barang['harga_mitra']:,.4f}\n"
                f"Tanggal Dibuat: {barang['created_at']}\n"
                f"Terakhir Ubah : {barang['updated_at']}",
                title=f"Detail Barang — {barang['nama_barang']}",
                expand=False
            ))
            
            if bom_komponen:
                console.print()
                console.print("[bold white]Daftar Komponen BOM (Bill of Materials):[/]")
                rows = []
                total_hpp = Decimal('0.0000')
                for idx, comp in enumerate(bom_komponen, start=1):
                    qty = comp['kuantitas_desimal']
                    h_beli = comp['harga_beli']
                    biaya = (qty * h_beli).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
                    total_hpp += biaya
                    rows.append([
                        idx,
                        comp['nama_bahan'],
                        comp['satuan_uom'],
                        f"{qty:,.4f}",
                        f"Rp {h_beli:,.4f}",
                        f"Rp {biaya:,.4f}"
                    ])
                rows.append([
                    "", "TOTAL HPP PRODUK", "", "", "", f"Rp {total_hpp:,.4f}"
                ])
                
                headers = ["No", "Bahan Baku", "Satuan", "Qty Pakai", "H.Beli", "Biaya Komponen"]
                table_str = tabulate(rows, headers=headers, tablefmt="grid")
                console.print(table_str)
                
            console.print()
            input("Tekan Enter untuk kembali...")
            
        finally:
            conn.close()
    except (EOFError, KeyboardInterrupt):
        return


def form_komposisi_bom(session_state: dict) -> None:
    """Formulir manajemen resep Bill of Materials (BOM) produk.

    (Ref: Module Structure Bab 4.4 - Modul M.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi form komposisi BOM
    print("[PLACEHOLDER] Menu belum diimplementasikan.")


def form_mencatat_limbah(session_state: dict) -> None:
    """Formulir pencatatan bahan baku terbuang (waste/gagal produksi).

    (Ref: Module Structure Bab 4.4 - Modul M.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi form pencatatan limbah
    print("[PLACEHOLDER] Menu belum diimplementasikan.")


def form_stock_opname(session_state: dict) -> None:
    """Formulir verifikasi fisik stok berkala.

    (Ref: Module Structure Bab 4.4 - Modul M.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi form stock opname
    print("[PLACEHOLDER] Menu belum diimplementasikan.")


def form_import_csv(session_state: dict) -> None:
    """Formulir migrasi/import data barang via berkas CSV.

    (Ref: Module Structure Bab 4.4 - Modul M.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi import data dari CSV
    print("[PLACEHOLDER] Menu belum diimplementasikan.")


def form_kelola_supplier(session_state: dict) -> None:
    """Formulir manajemen mitra supplier dan utang belanja tempo.

    (Ref: Module Structure Bab 4.4 - Modul M.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi form kelola supplier
    print("[PLACEHOLDER] Menu belum diimplementasikan.")


def trigger_backup_restore(session_state: dict) -> None:
    """Memicu pencadangan ZIP terenkripsi basis data secara langsung.

    (Ref: Module Structure Bab 4.4 - Modul M.2)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi trigger backup/restore database
    print("[PLACEHOLDER] Menu belum diimplementasikan.")


def form_job_tracking_antrian(session_state: dict) -> None:
    """Formulir pemantauan status antrian produksi kustom.

    (Ref: Module Structure Bab 4.4 - Modul M.5)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi form pelacakan antrian kerja
    print("[PLACEHOLDER] Menu belum diimplementasikan.")


def form_arsip_desain(session_state: dict) -> None:
    """Formulir lookup dan penyimpanan arsip file desain pelanggan.

    (Ref: Module Structure Bab 4.4 - Modul M.5)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi form arsip berkas desain
    print("[PLACEHOLDER] Menu belum diimplementasikan.")


def trigger_whatsapp_link(session_state: dict) -> None:
    """Memicu pembuatan tautan WhatsApp API untuk pelanggan.

    (Ref: Module Structure Bab 4.4 - Modul M.5)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # TODO: Implementasi trigger tautan WA Web
    print("[PLACEHOLDER] Menu belum diimplementasikan.")
