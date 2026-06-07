"""
Nama Modul: dashboard.py
Deskripsi: Merender dashboard visual harian berdasarkan peran (role) pengguna.
           (Ref: Module Structure Bab 4.2)
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

import sys
from decimal import Decimal
from datetime import date

# Import third-party
try:
    from rich.console import Console
    from rich.panel import Panel
    _console = Console()
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False

# Import local
from db.db_connector import get_db_connection
from logic.auth_handler import logout_user
from middleware.auth_jwt import validate_session_token
from middleware.rbac_guard import get_visible_menus, get_visible_modules, get_module_submenus, MODULE_NAMES
from utils.text_formatter import clear_terminal
from logic.safety_validator import sanitasi_input_cli
from db.query_builder import (
    query_dashboard_pemilik,
    query_dashboard_kasir,
    query_dashboard_operasional,
    query_dashboard_kepala,
    query_dashboard_gudang,
    query_dashboard_pramuniaga,
    query_dashboard_fotocopy
)
from logic.financial_engine import hitung_laba_bersih_harian


def _format_rupiah(nominal: Decimal) -> str:
    """Format nominal Decimal ke string Rupiah dengan separator ribuan."""
    return f"Rp {nominal:,.4f}"


def _render_dashboard_pemilik(session_state: dict, db_conn, tanggal: str) -> None:
    res = query_dashboard_pemilik(db_conn, session_state.get('cabang_id', 1), tanggal)
    if not res.is_success:
        raise Exception(res.error_msg)
    data = res.data

    total_pendapatan = data['total_pendapatan']
    total_pengeluaran = data['total_pengeluaran']
    total_limbah = data['total_limbah']
    status_transaksi = data['status_transaksi']
    alert_bank = data['alert_bank']
    alert_supplier = data['alert_supplier']

    laba_bersih = hitung_laba_bersih_harian(total_pendapatan, total_pengeluaran, total_limbah)

    if laba_bersih >= 0:
        laba_text = f"[bold green]{_format_rupiah(laba_bersih)}[/]"
    else:
        laba_text = f"[bold red]RUGI {_format_rupiah(laba_bersih)}[/]"

    summary_lines = [
        f"💰 Total Pendapatan    : {_format_rupiah(total_pendapatan)}",
        f"💸 Total Pengeluaran   : {_format_rupiah(total_pengeluaran)}",
        f"🗑️ Kerugian Limbah     : {_format_rupiah(total_limbah)}",
        "────────────────────────────────────",
        f"📈 Estimasi Laba Bersih: {laba_text}"
    ]
    summary_content = "\n".join(summary_lines)

    headers = ["Status", "Jumlah"]
    table_rows = []
    status_map = {item['status_pembayaran']: item['jumlah'] for item in status_transaksi}
    for st in ['LUNAS', 'BELUM LUNAS', 'BATAL', 'RETUR']:
        table_rows.append([st, status_map.get(st, 0)])

    if HAS_TABULATE:
        table_str = tabulate(table_rows, headers=headers, tablefmt="grid")
    else:
        table_str = "┌──────────────┬────────┐\n"
        table_str += "│ Status       │ Jumlah │\n"
        table_str += "├──────────────┼────────┤\n"
        for st, count in table_rows:
            table_str += f"│ {st:<12} │ {count:>6} │\n"
        table_str += "└──────────────┴────────┘"

    alerts = []
    for item in alert_bank:
        tipe = item['tipe_bank']
        setoran = item['setoran_bulanan']
        tgl = item['tanggal_jatuh_tempo']
        sisa = item['sisa_hari']
        alerts.append(f"• {tipe} - Cicilan {_format_rupiah(setoran)}\n  Jatuh tempo: {tgl} ({sisa} hari lagi)")
    for item in alert_supplier:
        nama = item['nama_supplier']
        utang = item['sisa_utang']
        tgl = item['tanggal_jatuh_tempo']
        sisa = item['sisa_hari']
        alerts.append(f"• Supplier {nama} - Utang {_format_rupiah(utang)}\n  Jatuh tempo: {tgl} ({sisa} hari lagi)")

    if not alerts:
        alerts_str = "✓ Tidak ada utang jatuh tempo dalam 3 hari."
    else:
        alerts_str = "\n".join(alerts)

    if HAS_RICH:
        _console.print(Panel(
            summary_content,
            title=f"[bold magenta]📊 RINGKASAN HARIAN TOKO — {tanggal}[/]",
            border_style="bold blue",
            expand=False
        ))
        _console.print("[bold white]Status Transaksi Hari Ini:[/]")
        _console.print(table_str)
        _console.print()
        alert_style = "bold yellow" if alerts else "bold green"
        _console.print(Panel(
            alerts_str,
            title=f"[{alert_style}]⚠️ PERINGATAN JATUH TEMPO (H-3)[/]",
            border_style="yellow" if alerts else "green",
            expand=False
        ))
        _console.print()
    else:
        print(f"═══ 📊 RINGKASAN HARIAN TOKO — {tanggal} ═══")
        for line in summary_lines:
            clean_line = line.replace("[bold green]", "").replace("[/]", "").replace("[bold red]", "")
            print(f"  {clean_line}")
        print("──────────────────────────────────────────────────────")
        print("Status Transaksi Hari Ini:")
        print(table_str)
        print("──────────────────────────────────────────────────────")
        print("⚠️ PERINGATAN JATUH TEMPO (H-3):")
        print(alerts_str)
        print("══════════════════════════════════════════════════════")
        print()


def _render_dashboard_kasir(session_state: dict, db_conn, tanggal: str) -> None:
    res = query_dashboard_kasir(db_conn, session_state.get('user_id'), session_state.get('cabang_id', 1), tanggal)
    if not res.is_success:
        raise Exception(res.error_msg)
    data = res.data

    jumlah_nota = data['jumlah_nota']
    total_kas = data['total_kas']
    jumlah_belum_lunas = data['jumlah_belum_lunas']
    saldo_ppob = data['saldo_ppob']

    username = session_state.get('username', '')
    summary_lines = [
        f"Jumlah Nota Hari Ini   : {jumlah_nota} nota",
        f"Total Kas Masuk        : {_format_rupiah(total_kas)}"
    ]
    if jumlah_belum_lunas > 0:
        summary_lines.append(f"Invoice BELUM LUNAS    : {jumlah_belum_lunas} nota  [YELLOW]⚠️[/]" if HAS_RICH else f"Invoice BELUM LUNAS    : {jumlah_belum_lunas} nota  ⚠️")
    else:
        summary_lines.append(f"Invoice BELUM LUNAS    : {jumlah_belum_lunas} nota")

    summary_content = "\n".join(summary_lines)

    headers = ["Akun PPOB", "Saldo Terakhir"]
    table_rows = []
    ppob_map = {item['akun_tipe']: item['saldo_terakhir'] for item in saldo_ppob}
    
    accounts = [
        ('Pulsa_Data', 'Pulsa & Data'),
        ('Token_Tagihan', 'Token & Tagihan')
    ]
    
    warning_accounts = []
    for key, display_name in accounts:
        val = ppob_map.get(key, Decimal('0.0000'))
        val_str = _format_rupiah(val)
        if val < Decimal('150000.0000'):
            warning_accounts.append(display_name)
            val_str += " ⚠️"
        table_rows.append([display_name, val_str])

    if HAS_TABULATE:
        table_str = tabulate(table_rows, headers=headers, tablefmt="grid")
    else:
        table_str = "┌──────────────────┬────────────────────┐\n"
        table_str += "│ Akun PPOB        │ Saldo Terakhir     │\n"
        table_str += "├──────────────────┼────────────────────┤\n"
        for name, balance in table_rows:
            table_str += f"│ {name:<16} │ {balance:<18} │\n"
        table_str += "└──────────────────┴────────────────────┘"

    warning_str = ""
    if warning_accounts:
        names = ", ".join(warning_accounts)
        warning_str = f"⚠️ PERINGATAN: Saldo {names} < {_format_rupiah(Decimal('150000.0000'))}!"

    if HAS_RICH:
        _console.print(Panel(
            summary_content,
            title=f"[bold magenta]🧾 DASHBOARD KASIR — {username} — {tanggal}[/]",
            border_style="bold blue",
            expand=False
        ))
        _console.print("[bold white]Saldo PPOB:[/]")
        _console.print(table_str)
        if warning_str:
            _console.print(f"[bold yellow]{warning_str}[/]")
        _console.print()
    else:
        print(f"═══ 🧾 DASHBOARD KASIR — {username} — {tanggal} ═══")
        for line in summary_lines:
            print(f"  {line}")
        print("──────────────────────────────────────────────────────")
        print("Saldo PPOB:")
        print(table_str)
        if warning_str:
            print(warning_str)
        print("══════════════════════════════════════════════════════")
        print()


def _render_dashboard_operasional(session_state: dict, db_conn) -> None:
    res = query_dashboard_operasional(db_conn, session_state.get('cabang_id', 1))
    if not res.is_success:
        raise Exception(res.error_msg)
    data = res.data

    antrian = data['antrian']
    stok_kritis = data['stok_kritis']

    headers_a = ["Status Antrian", "Jumlah"]
    antrian_map = {item['status_antrian']: item['jumlah'] for item in antrian}
    table_rows_a = []
    for st in ['Antri', 'Proses Desain', 'Produksi', 'Selesai', 'Diambil']:
        table_rows_a.append([st, antrian_map.get(st, 0)])

    if HAS_TABULATE:
        table_str_a = tabulate(table_rows_a, headers=headers_a, tablefmt="grid")
    else:
        table_str_a = "┌──────────────────┬────────┐\n"
        table_str_a += "│ Status Antrian   │ Jumlah │\n"
        table_str_a += "├──────────────────┼────────┤\n"
        for st, count in table_rows_a:
            table_str_a += f"│ {st:<16} │ {count:>6} │\n"
        table_str_a += "└──────────────────┴────────┘"

    headers_s = ["Nama Barang", "Sisa", "Satuan"]
    table_rows_s = []
    for item in stok_kritis:
        stok_val = item['stok_saat_ini']
        table_rows_s.append([item['nama_barang'], f"{stok_val:,.4f}", item['satuan_uom']])

    if HAS_TABULATE:
        table_str_s = tabulate(table_rows_s, headers=headers_s, tablefmt="grid") if table_rows_s else "✓ Semua stok bahan baku aman."
    else:
        if table_rows_s:
            table_str_s = "┌────────────────────────┬──────────┬────────┐\n"
            table_str_s += "│ Nama Barang            │ Sisa     │ Satuan │\n"
            table_str_s += "├────────────────────────┼──────────┼────────┤\n"
            for name, sisa, unit in table_rows_s:
                table_str_s += f"│ {name:<22} │ {sisa:>8} │ {unit:<6} │\n"
            table_str_s += "└────────────────────────┴──────────┴────────┘"
        else:
            table_str_s = "✓ Semua stok bahan baku aman."

    username = session_state.get('username', '')
    tanggal = date.today().isoformat()

    if HAS_RICH:
        _console.print(Panel(
            f"Selamat bekerja, {username}!\nBerikut adalah status antrian cetak dan bahan baku.",
            title=f"[bold magenta]🏭 DASHBOARD OPERASIONAL — {username} — {tanggal}[/]",
            border_style="bold blue",
            expand=False
        ))
        _console.print("[bold white]Status Antrian Kerja:[/]")
        _console.print(table_str_a)
        _console.print()
        _console.print("[bold yellow]⚠️ Stok Bahan Baku KRITIS:[/]")
        _console.print(table_str_s)
        _console.print()
    else:
        print(f"═══ 🏭 DASHBOARD OPERASIONAL — {username} — {tanggal} ═══")
        print(f"Selamat bekerja, {username}!")
        print("Status Antrian Kerja:")
        print(table_str_a)
        print("──────────────────────────────────────────────────────")
        print("⚠️ Stok Bahan Baku KRITIS:")
        print(table_str_s)
        print("══════════════════════════════════════════════════════")
        print()


def _render_dashboard_kepala(session_state: dict, db_conn, tanggal: str) -> None:
    res = query_dashboard_kepala(db_conn, session_state.get('cabang_id', 1), tanggal)
    if not res.is_success:
        raise Exception(res.error_msg)
    data = res.data

    jumlah_hadir = data['jumlah_hadir']
    total_staf = data['total_staf']
    draf_pending = data['draf_pending']
    antrian = data['antrian']

    headers_a = ["Status Antrian", "Jumlah"]
    antrian_map = {item['status_antrian']: item['jumlah'] for item in antrian}
    table_rows_a = []
    for st in ['Antri', 'Proses Desain', 'Produksi', 'Selesai', 'Diambil']:
        table_rows_a.append([st, antrian_map.get(st, 0)])

    if HAS_TABULATE:
        table_str_a = tabulate(table_rows_a, headers=headers_a, tablefmt="grid")
    else:
        table_str_a = "┌──────────────────┬────────┐\n"
        table_str_a += "│ Status Antrian   │ Jumlah │\n"
        table_str_a += "├──────────────────┼────────┤\n"
        for st, count in table_rows_a:
            table_str_a += f"│ {st:<16} │ {count:>6} │\n"
        table_str_a += "└──────────────────┴────────┘"

    summary_lines = [
        f"Staf Hadir Hari Ini  : {jumlah_hadir} dari {total_staf} staf",
        f"Draf Stock Opname    : {draf_pending} draf pending approval"
    ]
    summary_content = "\n".join(summary_lines)
    username = session_state.get('username', '')

    if HAS_RICH:
        _console.print(Panel(
            summary_content,
            title=f"[bold magenta]👑 DASHBOARD SUPERVISOR — {username} — {tanggal}[/]",
            border_style="bold blue",
            expand=False
        ))
        _console.print("[bold white]Status Antrian Kerja Aktif:[/]")
        _console.print(table_str_a)
        _console.print()
    else:
        print(f"═══ 👑 DASHBOARD SUPERVISOR — {username} — {tanggal} ═══")
        for line in summary_lines:
            print(f"  {line}")
        print("──────────────────────────────────────────────────────")
        print("Status Antrian Kerja Aktif:")
        print(table_str_a)
        print("══════════════════════════════════════════════════════")
        print()


def _render_dashboard_gudang(session_state: dict, db_conn) -> None:
    res = query_dashboard_gudang(db_conn, session_state.get('cabang_id', 1))
    if not res.is_success:
        raise Exception(res.error_msg)
    data = res.data

    stok_kritis = data['stok_kritis']
    draf_pending = data['draf_pending']
    utang_supplier = data['utang_supplier']

    headers_s = ["Nama Barang", "Sisa", "Satuan"]
    table_rows_s = []
    for item in stok_kritis:
        stok_val = item['stok_saat_ini']
        table_rows_s.append([item['nama_barang'], f"{stok_val:,.4f}", item['satuan_uom']])

    if HAS_TABULATE:
        table_str_s = tabulate(table_rows_s, headers=headers_s, tablefmt="grid") if table_rows_s else "✓ Semua stok bahan baku aman."
    else:
        if table_rows_s:
            table_str_s = "┌────────────────────────┬──────────┬────────┐\n"
            table_str_s += "│ Nama Barang            │ Sisa     │ Satuan │\n"
            table_str_s += "├────────────────────────┼──────────┼────────┤\n"
            for name, sisa, unit in table_rows_s:
                table_str_s += f"│ {name:<22} │ {sisa:>8} │ {unit:<6} │\n"
            table_str_s += "└────────────────────────┴──────────┴────────┘"
        else:
            table_str_s = "✓ Semua stok bahan baku aman."

    headers_u = ["Nama Supplier", "Sisa Utang", "Jatuh Tempo"]
    table_rows_u = []
    for item in utang_supplier:
        table_rows_u.append([item['nama_supplier'], _format_rupiah(item['sisa_utang']), str(item['tanggal_jatuh_tempo'])])

    if HAS_TABULATE:
        table_str_u = tabulate(table_rows_u, headers=headers_u, tablefmt="grid") if table_rows_u else "✓ Tidak ada utang supplier jatuh tempo dalam 7 hari."
    else:
        if table_rows_u:
            table_str_u = "┌────────────────────────┬────────────────────┬────────────┐\n"
            table_str_u += "│ Nama Supplier          │ Sisa Utang         │ Jatuh Tempo│\n"
            table_str_u += "├────────────────────────┼────────────────────┼────────────┤\n"
            for name, utang, tgl in table_rows_u:
                table_str_u += f"│ {name:<22} │ {utang:<18} │ {tgl:<10} │\n"
            table_str_u += "└────────────────────────┴────────────────────┴────────────┘"
        else:
            table_str_u = "✓ Tidak ada utang supplier jatuh tempo dalam 7 hari."

    summary_lines = [
        f"Draf Stock Opname      : {draf_pending} draf pending approval"
    ]
    summary_content = "\n".join(summary_lines)

    username = session_state.get('username', '')
    tanggal = date.today().isoformat()

    if HAS_RICH:
        _console.print(Panel(
            summary_content,
            title=f"[bold magenta]📦 DASHBOARD GUDANG — {username} — {tanggal}[/]",
            border_style="bold blue",
            expand=False
        ))
        _console.print("[bold yellow]⚠️ Stok Bahan Baku KRITIS:[/]")
        _console.print(table_str_s)
        _console.print()
        _console.print("[bold red]⚠️ UTANG SUPPLIER DEKAT JATUH TEMPO (H-7):[/]")
        _console.print(table_str_u)
        _console.print()
    else:
        print(f"═══ 📦 DASHBOARD GUDANG — {username} — {tanggal} ═══")
        for line in summary_lines:
            print(f"  {line}")
        print("──────────────────────────────────────────────────────")
        print("⚠️ Stok Bahan Baku KRITIS:")
        print(table_str_s)
        print("──────────────────────────────────────────────────────")
        print("⚠️ UTANG SUPPLIER DEKAT JATUH TEMPO (H-7):")
        print(table_str_u)
        print("══════════════════════════════════════════════════════")
        print()


def _render_dashboard_pramuniaga(session_state: dict, db_conn) -> None:
    res = query_dashboard_pramuniaga(db_conn, session_state.get('cabang_id', 1))
    if not res.is_success:
        raise Exception(res.error_msg)
    data = res.data

    jumlah_antri = data['jumlah_antri']
    username = session_state.get('username', '')
    tanggal = date.today().isoformat()

    summary_lines = [
        "Selamat bekerja! Tetap ramah melayani pelanggan CRM.",
        f"Jumlah antrian pesanan masuk ('Antri'): {jumlah_antri} pekerjaan"
    ]
    summary_content = "\n".join(summary_lines)

    if HAS_RICH:
        _console.print(Panel(
            summary_content,
            title=f"[bold magenta]💁 DASHBOARD PRAMUNIAGA — {username} — {tanggal}[/]",
            border_style="bold blue",
            expand=False
        ))
        _console.print()
    else:
        print(f"═══ 💁 DASHBOARD PRAMUNIAGA — {username} — {tanggal} ═══")
        for line in summary_lines:
            print(f"  {line}")
        print("══════════════════════════════════════════════════════")
        print()


def _render_dashboard_fotocopy(session_state: dict, db_conn, tanggal: str) -> None:
    res = query_dashboard_fotocopy(db_conn, session_state.get('user_id'), session_state.get('cabang_id', 1), tanggal)
    if not res.is_success:
        raise Exception(res.error_msg)
    data = res.data

    jumlah_nota = data['jumlah_nota']
    total_kas = data['total_kas']
    username = session_state.get('username', '')

    summary_lines = [
        "Selamat bekerja! Layani fotokopi dan cetak retail cepat dengan teliti.",
        f"Jumlah Transaksi Hari Ini: {jumlah_nota} nota",
        f"Total Omset Fotocopy/Print: {_format_rupiah(total_kas)}"
    ]
    summary_content = "\n".join(summary_lines)

    if HAS_RICH:
        _console.print(Panel(
            summary_content,
            title=f"[bold magenta]🖨️ DASHBOARD FOTOCOPY & PRINT — {username} — {tanggal}[/]",
            border_style="bold blue",
            expand=False
        ))
        _console.print()
    else:
        print(f"═══ 🖨️ DASHBOARD FOTOCOPY & PRINT — {username} — {tanggal} ═══")
        for line in summary_lines:
            print(f"  {line}")
        print("══════════════════════════════════════════════════════")
        print()


def _render_summary_panels(session_state: dict) -> None:
    """Merender panel ringkasan visual harian per peran aktif pengguna.

    (Ref: UC-043)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    role = session_state.get('role', '')
    tanggal = date.today().isoformat()

    conn_res = get_db_connection()
    if not conn_res.is_success:
        warning_msg = f"⚠️ ERR-DB-003: Gagal memuat ringkasan dashboard (Detail: {conn_res.error_msg})"
        if HAS_RICH:
            _console.print(f"[bold yellow]{warning_msg}[/]")
        else:
            print(warning_msg)
        return

    db_conn = conn_res.data
    try:
        if role == 'pemilik':
            _render_dashboard_pemilik(session_state, db_conn, tanggal)
        elif role == 'kepala_percetakan':
            _render_dashboard_kepala(session_state, db_conn, tanggal)
        elif role == 'kasir':
            _render_dashboard_kasir(session_state, db_conn, tanggal)
        elif role in ('desainer', 'produksi_cetak'):
            _render_dashboard_operasional(session_state, db_conn)
        elif role == 'gudang':
            _render_dashboard_gudang(session_state, db_conn)
        elif role == 'pramuniaga':
            _render_dashboard_pramuniaga(session_state, db_conn)
        elif role == 'fotocopy_print':
            _render_dashboard_fotocopy(session_state, db_conn, tanggal)
        else:
            msg = "Selamat bekerja! Jalankan tugas dengan aman dan teliti."
            if HAS_RICH:
                _console.print(Panel(msg, title="[bold white]INFO[/]", border_style="bold blue", expand=False))
            else:
                print("═══ INFO ═══")
                print(msg)
                print("════════════")
    except Exception as e:
        warning_msg = f"⚠️ ERR-DB-003: Gagal memuat data ringkasan dashboard (Detail: {str(e)})"
        if HAS_RICH:
            _console.print(f"[bold yellow]{warning_msg}[/]")
        else:
            print(warning_msg)
    finally:
        try:
            db_conn.close()
        except Exception:
            pass


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
            _render_summary_panels(session_state)
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
            _render_summary_panels(session_state)
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

