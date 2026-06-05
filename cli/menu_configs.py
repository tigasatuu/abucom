"""
Nama Modul: menu_configs.py
Deskripsi: Antarmuka konfigurasi parameter sistem runtime untuk pemilik (absolute lockdown).
           (Ref: Module Structure Bab 4.7)
Author: Antigravity AI
Tanggal: 2026-06-05
"""

# 1. Standard Library
import os
import platform
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any

# 2. Third-Party
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# 3. Local Modules
from db.config_cache import get_all_configs_list, update_config_value
from db.db_connector import get_db_connection
from middleware.rbac_guard import require_role
from middleware.audit_logger import log_audit_trail

# Console instance
_console = Console()


def _clear_terminal() -> None:
    """Membersihkan layar terminal console secara lintas OS."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')


@require_role('MENU-M10-001')
def show_menu_configs(session_state: dict) -> None:
    """Menampilkan panel utama konfigurasi parameter sistem.

    (Ref: Module Structure Bab 4.7 - Modul M.10)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    db_conn_res = get_db_connection()
    if not db_conn_res.is_success:
        _console.print(f"[bold red]⛔ ERR-DB-002: Koneksi database gagal: {db_conn_res.error_msg}[/]")
        _console.print("[yellow]Tekan Enter untuk kembali...[/]")
        input()
        return

    db_connection = db_conn_res.data
    cabang_id = session_state.get('cabang_id', 1)

    while True:
        _clear_terminal()

        # Header path menu Config
        _console.print(Panel(
            "[bold white]M.10 PENGATURAN PARAMETER SISTEM RUNTIME[/]\n"
            "[blue]Dashboard > M.10 Config > Konfigurasi Parameter Runtime[/]",
            style="bold white",
            expand=False
        ))
        _console.print()

        # Ambil semua parameter
        res = get_all_configs_list(db_connection, cabang_id)
        if not res.is_success:
            _console.print(f"[bold red]⛔ {res.error_msg}[/]")
            _console.print("[yellow]Tekan Enter untuk kembali...[/]")
            input()
            return

        configs = res.data
        if not configs:
            _console.print("[yellow]Tidak ada parameter konfigurasi yang ditemukan.[/]")
            _console.print("[yellow]Tekan Enter untuk kembali...[/]")
            input()
            return

        # Render tabel parameter
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("No.", style="dim", width=4, justify="right")
        table.add_column("Parameter Key", style="cyan")
        table.add_column("Nilai Saat Ini", style="green", justify="right")
        table.add_column("Tipe Data", style="magenta")
        table.add_column("Deskripsi", style="white")

        for idx, config in enumerate(configs, start=1):
            val_str = config.parameter_value
            val_display = val_str
            
            if config.tipe_data == 'DECIMAL':
                try:
                    dec_val = Decimal(val_str)
                    if dec_val >= 1000:
                        s = f"{int(dec_val):,}" if dec_val == dec_val.to_integral_value() else f"{dec_val:,.4f}"
                        s = s.replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
                        if "," in s:
                            s = s.rstrip("0").rstrip(",")
                        val_display = f"Rp {s}"
                    else:
                        s = str(dec_val)
                        if "." in s:
                            s = s.rstrip("0").rstrip(".")
                            s = s.replace(".", ",")
                        val_display = s
                except (ValueError, InvalidOperation):
                    pass

            table.add_row(
                str(idx),
                config.parameter_key,
                val_display,
                config.tipe_data,
                config.deskripsi
            )

        _console.print(table)
        _console.print()

        pilihan = _console.input("[bold yellow]Masukkan nomor opsi parameter yang akan diubah [0-Kembali]: [/]").strip()

        if pilihan == '0':
            break

        try:
            pilihan_idx = int(pilihan)
            if 1 <= pilihan_idx <= len(configs):
                selected_config = configs[pilihan_idx - 1]
                form_update_parameter(session_state, selected_config)
            else:
                _console.print("[bold red]⛔ Input Salah: Nomor opsi tidak valid![/]")
                _console.print("[yellow]Tekan Enter untuk melanjutkan...[/]")
                input()
        except ValueError:
            _console.print("[bold red]⛔ Input Salah: Harap masukkan angka![/]")
            _console.print("[yellow]Tekan Enter untuk melanjutkan...[/]")
            input()


def form_update_parameter(session_state: dict, config: Any = None) -> None:
    """Formulir pembaruan parameter regulasi operasional toko.

    (Ref: Module Structure Bab 4.7 - Modul M.10)

    Args:
        session_state (dict): Status sesi aktif pengguna.
        config (ConfigParam, optional): Parameter yang dipilih untuk diubah.
    """
    if config is None:
        _console.print("[bold red]⛔ Error: Tidak ada parameter yang dipilih.[/]")
        _console.print("[yellow]Tekan Enter untuk kembali...[/]")
        input()
        return

    db_conn_res = get_db_connection()
    if not db_conn_res.is_success:
        _console.print(f"[bold red]⛔ ERR-DB-002: Koneksi database gagal: {db_conn_res.error_msg}[/]")
        _console.print("[yellow]Tekan Enter untuk kembali...[/]")
        input()
        return

    db_connection = db_conn_res.data
    cabang_id = session_state.get('cabang_id', 1)
    pengguna_id = session_state.get('user_id', 1)

    _console.print()
    _console.print(Panel(
        f"[bold white]Ubah Parameter:[/] {config.parameter_key}\n"
        f"[bold white]Deskripsi:[/] {config.deskripsi}\n"
        f"[bold white]Tipe Data:[/] {config.tipe_data}\n"
        f"[bold white]Nilai Lama:[/] {config.parameter_value}",
        style="blue",
        title="Form Update Parameter",
        expand=False
    ))

    new_val_input = _console.input(f"[bold yellow]Masukkan nilai baru untuk {config.deskripsi}: [/]").strip()

    # Validasi input berdasarkan tipe_data
    new_value_str = ""
    if config.tipe_data == 'DECIMAL':
        try:
            dec_val = Decimal(new_val_input)
            if dec_val < 0:
                raise ValueError()
            dec_val = dec_val.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
            new_value_str = str(dec_val)
        except (ValueError, InvalidOperation):
            _console.print("[bold red]⛔ ERR-VAL-038: Input Salah: Nilai parameter baru harus diisi berupa angka positif desimal![/]")
            _console.print("[yellow]Tekan Enter untuk kembali ke Daftar Parameter...[/]")
            input()
            return
    elif config.tipe_data == 'INTEGER':
        try:
            int_val = int(new_val_input)
            if int_val < 0:
                raise ValueError()
            new_value_str = str(int_val)
        except ValueError:
            _console.print("[bold red]⛔ Input Salah: Nilai parameter baru harus diisi berupa angka bulat positif![/]")
            _console.print("[yellow]Tekan Enter untuk kembali ke Daftar Parameter...[/]")
            input()
            return
    else:  # VARCHAR
        if not new_val_input:
            _console.print("[bold red]⛔ Input Salah: Nilai parameter baru tidak boleh kosong![/]")
            _console.print("[yellow]Tekan Enter untuk kembali ke Daftar Parameter...[/]")
            input()
            return
        new_value_str = new_val_input

    # Konfirmasi perubahan
    _console.print("\n[bold white]Konfirmasi perubahan parameter:[/]")
    _console.print(f"  Parameter  : {config.parameter_key}")
    _console.print(f"  Nilai Lama : {config.parameter_value}")
    _console.print(f"  Nilai Baru : {new_value_str}")

    confirm = _console.input("[bold yellow]Lanjutkan? [Y/N]: [/]").strip().upper()
    if confirm != 'Y':
        _console.print("[yellow]Perubahan dibatalkan.[/]")
        _console.print("[yellow]Tekan Enter untuk kembali ke Daftar Parameter...[/]")
        input()
        return

    # Eksekusi update
    res = update_config_value(db_connection, config.id, new_value_str, cabang_id)
    if res.is_success:
        formatted_val = new_value_str
        if config.tipe_data == 'DECIMAL':
            try:
                dec_new = Decimal(new_value_str)
                if dec_new >= 1000:
                    s_new = f"{int(dec_new):,}" if dec_new == dec_new.to_integral_value() else f"{dec_new:,.4f}"
                    s_new = s_new.replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
                    if "," in s_new:
                        s_new = s_new.rstrip("0").rstrip(",")
                    formatted_val = f"Rp {s_new}"
                else:
                    formatted_val = new_value_str
            except Exception:
                pass

        _console.print(f"[bold green]Konfigurasi Sukses! Parameter '{config.parameter_key}' diubah = {formatted_val}. Tersimpan di database.[/]")

        # Panggil audit logger
        old_val_dict = {'parameter_key': config.parameter_key, 'parameter_value': config.parameter_value}
        new_val_dict = {'parameter_key': config.parameter_key, 'parameter_value': new_value_str}
        log_audit_trail(
            pengguna_id=pengguna_id,
            action_type='UPDATE',
            target_table='system_configs',
            old_val=old_val_dict,
            new_val=new_val_dict,
            cabang_id=cabang_id,
            db_connection=db_connection
        )
    else:
        _console.print(f"[bold red]⛔ {res.error_msg}[/]")

    _console.print("[yellow]Tekan ENTER untuk kembali ke Daftar Parameter...[/]")
    input()
