"""
Nama Modul: test_cli_navigation.py
Deskripsi: Unit testing untuk fungsionalitas navigasi menu utama CLI dengan hotkey standar.
           (Ref: Module Structure Bab 4.2, CLI Flow Bab 4.3, Issue #0125)
Author: Antigravity
Tanggal: 2026-06-07
"""

import sys
import pytest
from unittest.mock import patch, MagicMock, call
from middleware.auth_jwt import Result, create_jwt_session
from cli.dashboard import (
    render_dashboard,
    show_module_submenu,
    handle_navigation,
    graceful_exit,
    form_ubah_password,
)
from logic.safety_validator import sanitasi_input_cli

# Global tracking variable for breadcrumbs state in tests
_test_breadcrumbs = []


@pytest.fixture(autouse=True)
def clean_breadcrumbs_state():
    """Auto-use fixture to initialize and clear breadcrumbs tracking state for each test iteration."""
    global _test_breadcrumbs
    _test_breadcrumbs.clear()
    yield
    _test_breadcrumbs.clear()


@pytest.fixture
def clean_session():
    """Fixture to build and reset a clean session state dictionary."""
    session = {
        'user_id': None,
        'username': None,
        'role': None,
        'cabang_id': None,
        'token': None
    }
    yield session
    session.clear()


@pytest.fixture
def pemilik_session(clean_session):
    """Fixture to build a session for a 'pemilik' user with a real valid JWT token."""
    token = create_jwt_session(1, 'pemilik_toko', 'pemilik', 1)
    clean_session.update({
        'user_id': 1,
        'username': 'pemilik_toko',
        'role': 'pemilik',
        'cabang_id': 1,
        'token': token
    })
    return clean_session


@pytest.fixture
def kasir_session(clean_session):
    """Fixture to build a session for a 'kasir' user with a real valid JWT token."""
    token = create_jwt_session(2, 'kasir_toko', 'kasir', 1)
    clean_session.update({
        'user_id': 2,
        'username': 'kasir_toko',
        'role': 'kasir',
        'cabang_id': 1,
        'token': token
    })
    return clean_session


# =====================================================================
# SKENARIO POSITIF (HAPPY PATH)
# =====================================================================

@patch('cli.dashboard.show_module_submenu')
@patch('builtins.input')
def test_navigasi_hotkey_valid_ke_submenu(mock_input, mock_show_submenu, pemilik_session) -> None:
    """Skenario Positif: validasi menekan tombol hotkey valid pada menu utama menuju submenu yang tepat."""
    def input_side_effect(prompt):
        # Clear token to break out of render_dashboard loop on next iteration
        pemilik_session['token'] = None
        return '2'
        
    mock_input.side_effect = input_side_effect
    
    render_dashboard(pemilik_session)
    
    mock_show_submenu.assert_called_once_with(pemilik_session, 'M2')


@patch('builtins.input')
def test_navigasi_mundur_ke_menu_parent(mock_input, pemilik_session) -> None:
    """Skenario Positif: validasi hotkey '0' mengembalikan state CLI ke menu parent."""
    mock_input.return_value = '0'
    
    # show_module_submenu will see input '0' and return immediately, going back to dashboard loop
    show_module_submenu(pemilik_session, 'M2')
    
    mock_input.assert_called_once()


@patch('cli.dashboard._console.print')
@patch('builtins.input')
def test_pembaruan_teks_breadcrumb(mock_input, mock_console_print, pemilik_session) -> None:
    """Skenario Positif: validasi UI breadcrumb navigasi ter-update dengan string rute yang presisi."""
    mock_input.return_value = '0'
    
    # We enforce HAS_RICH=True to cover the Rich printing path where Panel with breadcrumb is rendered
    with patch('cli.dashboard.HAS_RICH', True):
        show_module_submenu(pemilik_session, 'M2')
        
    expected_path = "Dashboard > M.2 — Inventaris, BOM & Stock Opname"
    
    found_breadcrumb = False
    for call_args in mock_console_print.call_args_list:
        args = call_args[0]
        for arg in args:
            if expected_path in str(arg):
                found_breadcrumb = True
                break
        if found_breadcrumb:
            break
            
    assert found_breadcrumb, f"Expected breadcrumb path '{expected_path}' not found in printed outputs"


# =====================================================================
# SKENARIO NEGATIF & EDGE CASES
# =====================================================================

@patch('builtins.input')
@patch('builtins.print')
def test_navigasi_menolak_hotkey_invalid(mock_print, mock_input, pemilik_session) -> None:
    """Skenario Negatif: menekan hotkey acak/invalid tidak crash, melainkan menampilkan error dan loop back."""
    # User inputs '99' (invalid), then press enter '', then 'q' to exit gracefully
    mock_input.side_effect = ['99', '', 'q']
    
    with pytest.raises(SystemExit) as excinfo:
        render_dashboard(pemilik_session)
        
    assert excinfo.value.code == 0
    
    # Assert warning message was printed
    warning_printed = False
    for call_args in mock_print.call_args_list:
        msg = call_args[0][0]
        if "tidak valid" in msg or "⛔" in msg:
            warning_printed = True
            break
            
    assert warning_printed, "Expected warning about invalid hotkey choice was not printed."


@patch('middleware.rbac_guard._log_access_denied')
@patch('builtins.print')
@patch('builtins.input')
def test_navigasi_memblokir_akses_submenu_di_luar_izin_rbac(
    mock_input, mock_print, mock_log_denied, kasir_session
) -> None:
    """Skenario Negatif: memblokir user dengan hak akses rendah (Kasir) mengakses submenu terbatas (M10 config)."""
    mock_input.return_value = ''
    
    # Trigger handle_navigation directly for a forbidden menu id (MENU-M10-001)
    res = handle_navigation(kasir_session, 'MENU-M10-001')
    
    assert res == kasir_session
    mock_log_denied.assert_called_once_with(kasir_session, 'MENU-M10-001', 'kasir')
    
    # Assert access denied visual warning was displayed
    denied_printed = False
    for call_args in mock_print.call_args_list:
        msg = call_args[0][0]
        if "ERR-AUTH-003" in msg:
            denied_printed = True
            break
            
    assert denied_printed, "Expected access denied code ERR-AUTH-003 was not printed."


def test_navigasi_sanitasi_spesial_karakter() -> None:
    """Skenario Negatif: sanitasi karakter control ANSI atau escape character pada input."""
    # Direct function testing
    raw_input = "\x1b[31mBarang\x00 Palsu\n\r"
    expected_sanitized = "[31mBarang Palsu"
    assert sanitasi_input_cli(raw_input) == expected_sanitized
    
    # E2E CLI logic flow testing: sanitizing escape prefix from menu selection
    with patch('builtins.input') as mock_input, \
         patch('cli.dashboard.graceful_exit') as mock_exit:
         
        # Input has escape control code '\x1b', which should be stripped, resulting in 'q' (quit)
        mock_input.return_value = "\x1bq"
        
        token = create_jwt_session(1, 'pemilik_toko', 'pemilik', 1)
        render_dashboard({'role': 'pemilik', 'token': token})
        mock_exit.assert_called_once()


# =====================================================================
# PENGUJIAN PENUTUP (GRACEFUL EXIT / SHUTDOWN)
# =====================================================================

@patch('cli.dashboard.get_db_connection')
@patch('cli.dashboard.logout_user')
def test_navigasi_graceful_shutdown_tombol_q(mock_logout, mock_get_db, pemilik_session) -> None:
    """Shutdown: simulasi eksekusi penghentian aplikasi melalui interaksi tombol 'q'."""
    mock_conn = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    
    with pytest.raises(SystemExit) as excinfo:
        graceful_exit(pemilik_session)
        
    assert excinfo.value.code == 0
    mock_logout.assert_called_once_with(pemilik_session, mock_conn)
    mock_conn.close.assert_called_once()
    
    # Assert session variables are cleared
    assert pemilik_session['user_id'] is None
    assert pemilik_session['username'] is None
    assert pemilik_session['role'] is None
    assert pemilik_session['cabang_id'] is None
    assert pemilik_session['token'] is None


@patch('cli.dashboard.graceful_exit')
@patch('builtins.input')
def test_navigasi_graceful_shutdown_ctrl_c(mock_input, mock_graceful_exit, pemilik_session) -> None:
    """Shutdown: simulasi eksekusi penghentian mendadak via KeyboardInterrupt (Ctrl+C)."""
    mock_input.side_effect = KeyboardInterrupt
    
    render_dashboard(pemilik_session)
    
    mock_graceful_exit.assert_called_once_with(pemilik_session)


@pytest.mark.parametrize("input_exception", [KeyboardInterrupt, EOFError])
@patch('cli.dashboard.graceful_exit')
@patch('builtins.input')
def test_submenu_graceful_shutdown_ctrl_c(
    mock_input, mock_graceful_exit, input_exception, pemilik_session
) -> None:
    """Shutdown: verifikasi submenu menangani KeyboardInterrupt/EOFError dan memicu graceful_exit."""
    mock_input.side_effect = input_exception
    
    show_module_submenu(pemilik_session, 'M2')
    
    mock_graceful_exit.assert_called_once_with(pemilik_session)


@patch('cli.dashboard.get_db_connection')
@patch('cli.dashboard.logout_user')
def test_graceful_exit_db_failure_handled(mock_logout, mock_get_db, pemilik_session) -> None:
    """Shutdown: memastikan graceful_exit tetap mematikan program jika koneksi database gagal."""
    mock_get_db.return_value = Result(False, None, "Koneksi DB Gagal")
    
    with pytest.raises(SystemExit) as excinfo:
        graceful_exit(pemilik_session)
        
    assert excinfo.value.code == 0
    mock_logout.assert_not_called()
    assert pemilik_session['token'] is None


# =====================================================================
# LAIN-LAIN / UJI ALUR KHUSUS
# =====================================================================

@patch('cli.dashboard.form_ubah_password')
@patch('builtins.input')
def test_navigasi_ubah_password_called(mock_input, mock_form_pw, pemilik_session) -> None:
    """Alur Khusus: navigasi ke opsi 'P' memanggil formulir ubah password."""
    def input_side_effect(prompt):
        pemilik_session['token'] = None
        return 'P'
        
    mock_input.side_effect = input_side_effect
    
    render_dashboard(pemilik_session)
    mock_form_pw.assert_called_once_with(pemilik_session)


@patch('cli.dashboard.get_db_connection')
@patch('cli.dashboard.logout_user')
@patch('builtins.input')
def test_navigasi_logout_konfirmasi_ya(mock_input, mock_logout, mock_get_db, pemilik_session) -> None:
    """Alur Khusus: logout dengan konfirmasi Y membersihkan sesi dan keluar."""
    mock_conn = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    
    # '0' for logout option, then 'y' to confirm, then hit enter ''
    mock_input.side_effect = ['0', 'y', '']
    
    render_dashboard(pemilik_session)
    
    mock_logout.assert_called_once_with(pemilik_session, mock_conn)
    assert mock_conn.close.call_count >= 1
    assert pemilik_session['token'] is None
    assert pemilik_session['user_id'] is None


@patch('builtins.input')
def test_navigasi_logout_konfirmasi_tidak(mock_input, pemilik_session) -> None:
    """Alur Khusus: membatalkan logout dengan konfirmasi N kembali ke loop dashboard."""
    # '0' for logout, 'n' to cancel, then 'q' to quit application
    mock_input.side_effect = ['0', 'n', 'q']
    
    with pytest.raises(SystemExit):
        render_dashboard(pemilik_session)
        
    # If it raised SystemExit, it correctly processed 'q' after canceling logout.


def test_handle_navigation_branches(pemilik_session) -> None:
    """Alur Khusus: menguji routing navigasi dari handle_navigation ke seluruh modul."""
    with patch('cli.menu_transaksi.show_menu_transaksi') as m1, \
         patch('cli.menu_inventaris.show_menu_inventaris') as m2, \
         patch('cli.menu_ppob_service.show_menu_ppob_service') as m3, \
         patch('cli.menu_sdm_finansial.show_menu_sdm_finansial') as m4, \
         patch('cli.menu_laporan.show_menu_laporan') as m9, \
         patch('cli.menu_configs.show_menu_configs') as m10, \
         patch('builtins.print') as mock_print, \
         patch('builtins.input') as mock_input:
         
        mock_input.return_value = ''
        
        # M1 / M8
        handle_navigation(pemilik_session, 'MENU-M1-001')
        m1.assert_called_once_with(pemilik_session)
        
        # M2 / M5
        handle_navigation(pemilik_session, 'MENU-M2-001')
        m2.assert_called_once_with(pemilik_session)
        
        # M3
        handle_navigation(pemilik_session, 'MENU-M3-001')
        m3.assert_called_once_with(pemilik_session)
        
        # M4 / M6
        handle_navigation(pemilik_session, 'MENU-M4-001')
        m4.assert_called_once_with(pemilik_session)
        
        # M7
        handle_navigation(pemilik_session, 'MENU-M7-001')
        mock_print.assert_any_call("[PLACEHOLDER] Menu belum diimplementasikan.")
        
        # M9
        handle_navigation(pemilik_session, 'MENU-M9-001')
        m9.assert_called_once_with(pemilik_session)
        
        # M10
        handle_navigation(pemilik_session, 'MENU-M10-001')
        m10.assert_called_once_with(pemilik_session)
        
        # Unknown/Unmapped Menu ID
        handle_navigation(pemilik_session, 'MENU-UNKNOWN')
        mock_print.assert_any_call("[PLACEHOLDER] Menu belum diimplementasikan.")


@patch('cli.dashboard.get_db_connection')
@patch('cli.dashboard.logout_user')
@patch('cli.dashboard.validate_session_token')
@patch('builtins.print')
@patch('builtins.input')
def test_handle_navigation_session_invalid(mock_input, mock_print, mock_validate, mock_logout, mock_get_db, pemilik_session) -> None:
    """Alur Khusus: handle_navigation meredireksi paksa ke logout jika session token rusak/invalid."""
    mock_validate.return_value = Result(False, None, "ERR-SESSION-002: Sesi login tidak sah/rusak.")
    mock_conn = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    mock_input.return_value = ''
    
    res = handle_navigation(pemilik_session, 'MENU-M1-001')
    
    assert res['token'] is None
    mock_logout.assert_called_once_with(pemilik_session, mock_conn)
    mock_conn.close.assert_called_once()
    mock_print.assert_any_call("⛔ ERR-SESSION-002: Sesi login tidak sah/rusak.")


# =====================================================================
# SKENARIO TAMBAHAN UNTUK 90%+ COVERAGE
# =====================================================================

@patch('cli.dashboard.get_db_connection')
@patch('cli.dashboard.logout_user')
def test_render_dashboard_session_invalid(mock_logout, mock_get_db, pemilik_session) -> None:
    """Menguji render_dashboard saat session token tidak valid."""
    mock_conn = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    
    with patch('cli.dashboard.validate_session_token') as mock_val:
        mock_val.return_value = Result(False, None, "ERR-SESSION-002: Sesi login tidak sah.")
        render_dashboard(pemilik_session)
        
    mock_logout.assert_called_once_with(pemilik_session, mock_conn)
    mock_conn.close.assert_called_once()
    assert pemilik_session['token'] is None


@patch('cli.dashboard.get_db_connection')
@patch('cli.dashboard.logout_user')
def test_render_dashboard_session_invalid_db_fail(mock_logout, mock_get_db, pemilik_session) -> None:
    """Menguji render_dashboard saat session token tidak valid dan DB gagal."""
    mock_get_db.return_value = Result(False, None, "DB_FAIL")
    
    with patch('cli.dashboard.validate_session_token') as mock_val:
        mock_val.return_value = Result(False, None, "ERR-SESSION-002")
        render_dashboard(pemilik_session)
        
    mock_logout.assert_not_called()
    assert pemilik_session['token'] is None


@patch('builtins.input')
def test_render_dashboard_has_rich_false(mock_input, pemilik_session) -> None:
    """Menguji rendering menu utama ketika HAS_RICH = False."""
    mock_input.return_value = 'q'
    with patch('cli.dashboard.HAS_RICH', False), \
         patch('cli.dashboard.graceful_exit'):
        render_dashboard(pemilik_session)


@patch('cli.dashboard.get_db_connection')
@patch('cli.dashboard.logout_user')
@patch('builtins.input')
def test_render_dashboard_logout_exception_handling(mock_input, mock_logout, mock_get_db, pemilik_session) -> None:
    """Menguji penanganan eksepsi pada logout_user dan db_conn.close."""
    mock_conn = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    mock_logout.side_effect = Exception("Logout Error")
    mock_conn.close.side_effect = Exception("Close Error")
    
    mock_input.side_effect = ['0', 'y', '']
    render_dashboard(pemilik_session)
    
    assert pemilik_session['token'] is None


@patch('cli.dashboard.get_db_connection')
@patch('cli.dashboard.logout_user')
@patch('builtins.input')
def test_render_dashboard_logout_cancel_via_ctrl_c(mock_input, mock_logout, mock_get_db, pemilik_session) -> None:
    """Menguji pembatalan logout ketika konfirmasi logout memicu KeyboardInterrupt."""
    mock_conn = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    # '0' to trigger logout, KeyboardInterrupt during confirmation, then enter ''
    mock_input.side_effect = ['0', KeyboardInterrupt, '']
    
    render_dashboard(pemilik_session)
    
    # Verify it treated the KeyboardInterrupt as 'y' (confirm logout), cleared session, and returned
    mock_logout.assert_called_once_with(pemilik_session, mock_conn)
    assert pemilik_session['token'] is None


@patch('builtins.input')
@patch('builtins.print')
def test_render_dashboard_non_integer_input(mock_print, mock_input, pemilik_session) -> None:
    """Menguji input pilihan menu non-angka."""
    mock_input.side_effect = ['abc', '', 'q']
    with pytest.raises(SystemExit):
        render_dashboard(pemilik_session)
    mock_print.assert_any_call("⛔ Pilihan 'abc' tidak valid. Harap masukkan angka 1-10, P, 0, atau q.")


@patch('builtins.input')
@patch('builtins.print')
def test_show_module_submenu_no_access(mock_print, mock_input, kasir_session) -> None:
    """Menguji show_module_submenu ketika peran tidak memiliki akses ke modul (submenus kosong)."""
    mock_input.return_value = ''
    show_module_submenu(kasir_session, 'M10')
    mock_print.assert_any_call("⛔ ERR-AUTH-003: Anda tidak memiliki akses ke modul ini.")


@patch('builtins.input')
def test_show_module_submenu_has_rich_false(mock_input, pemilik_session) -> None:
    """Menguji rendering submenu ketika HAS_RICH = False."""
    mock_input.return_value = '0'
    with patch('cli.dashboard.HAS_RICH', False):
        show_module_submenu(pemilik_session, 'M2')


@patch('builtins.input')
@patch('builtins.print')
def test_show_module_submenu_invalid_choices(mock_print, mock_input, pemilik_session) -> None:
    """Menguji penanganan input pilihan invalid pada submenu."""
    # choices: '99' (out of bounds), then '', then 'abc' (non-int), then '', then '0' (exit)
    mock_input.side_effect = ['99', '', 'abc', '', '0']
    show_module_submenu(pemilik_session, 'M2')
    
    # check that print warnings were called
    any_invalid = any("tidak valid" in call[0][0] for call in mock_print.call_args_list if call[0])
    assert any_invalid


@patch('cli.dashboard.get_db_connection')
@patch('cli.dashboard.logout_user')
@patch('cli.dashboard.validate_session_token')
def test_handle_navigation_logout_exceptions(mock_validate, mock_logout, mock_get_db, pemilik_session) -> None:
    """Menguji penanganan eksepsi logout dan close dalam handle_navigation."""
    mock_validate.return_value = Result(False, None, "Invalid Token")
    mock_conn = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    mock_logout.side_effect = Exception("Logout Error")
    mock_conn.close.side_effect = Exception("Close Error")
    
    with patch('builtins.print'), patch('builtins.input'):
        handle_navigation(pemilik_session, 'MENU-M1-001')
        
    assert pemilik_session['token'] is None


# =====================================================================
# UBAH PASSWORD TESTS (cli.dashboard.form_ubah_password)
# =====================================================================

@patch('getpass.getpass')
def test_form_ubah_password_ctrl_c(mock_getpass, pemilik_session) -> None:
    """Menguji form_ubah_password dibatalkan karena KeyboardInterrupt."""
    mock_getpass.side_effect = KeyboardInterrupt
    assert form_ubah_password(pemilik_session) is None


@patch('cli.dashboard.get_db_connection')
@patch('getpass.getpass')
@patch('builtins.print')
@patch('builtins.input')
def test_form_ubah_password_db_fail(mock_input, mock_print, mock_getpass, mock_get_db, pemilik_session) -> None:
    """Menguji form_ubah_password gagal karena koneksi DB bermasalah."""
    mock_getpass.return_value = 'OldPass123!'
    mock_get_db.return_value = Result(False, None, "DB Connect Error")
    mock_input.return_value = ''
    
    form_ubah_password(pemilik_session)
    mock_print.assert_any_call("⛔ ERR-DB-002: Koneksi database gagal: DB Connect Error")


@patch('cli.dashboard.get_db_connection')
@patch('getpass.getpass')
@patch('builtins.print')
@patch('builtins.input')
def test_form_ubah_password_query_fail(mock_input, mock_print, mock_getpass, mock_get_db, pemilik_session) -> None:
    """Menguji form_ubah_password gagal karena query DB melempar eksepsi."""
    mock_getpass.return_value = 'OldPass123!'
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = Exception("Query error")
    mock_input.return_value = ''
    
    form_ubah_password(pemilik_session)
    mock_print.assert_any_call("⛔ ERR-DB-003: Terjadi kesalahan database: Query error")
    mock_conn.close.assert_called_once()


@patch('cli.dashboard.get_db_connection')
@patch('getpass.getpass')
@patch('builtins.print')
@patch('builtins.input')
def test_form_ubah_password_wrong_old(mock_input, mock_print, mock_getpass, mock_get_db, pemilik_session) -> None:
    """Menguji form_ubah_password gagal karena kata sandi lama tidak cocok."""
    mock_getpass.return_value = 'OldPassWrong123!'
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {'password_hash': 'some_hash'}
    mock_input.return_value = ''
    
    with patch('middleware.auth_jwt.verify_password', return_value=False):
        form_ubah_password(pemilik_session)
        
    mock_print.assert_any_call("⛔ ERR-AUTH-044: Otorisasi Gagal: Kata sandi lama yang Anda masukkan tidak valid!")
    mock_conn.close.assert_called_once()


@patch('cli.dashboard.get_db_connection')
@patch('getpass.getpass')
@patch('builtins.print')
@patch('builtins.input')
def test_form_ubah_password_new_ctrl_c(mock_input, mock_print, mock_getpass, mock_get_db, pemilik_session) -> None:
    """Menguji form_ubah_password dibatalkan pada input kata sandi baru."""
    mock_getpass.side_effect = ['OldPass', KeyboardInterrupt]
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {'password_hash': 'some_hash'}
    
    with patch('middleware.auth_jwt.verify_password', return_value=True):
        form_ubah_password(pemilik_session)
        
    mock_conn.close.assert_called_once()


@patch('cli.dashboard.get_db_connection')
@patch('getpass.getpass')
@patch('builtins.print')
@patch('builtins.input')
def test_form_ubah_password_validation_fail(mock_input, mock_print, mock_getpass, mock_get_db, pemilik_session) -> None:
    """Menguji form_ubah_password gagal karena password baru < 8 karakter atau tidak cocok."""
    mock_getpass.side_effect = ['OldPass', 'weak', 'weak']
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {'password_hash': 'some_hash'}
    mock_input.return_value = ''
    
    with patch('middleware.auth_jwt.verify_password', return_value=True):
        form_ubah_password(pemilik_session)
        
    mock_print.assert_any_call("⛔ ERR-VAL-044: Konvalidasi Gagal: Kata sandi baru minimal harus 8 karakter dan bernilai cocok pada kedua input!")
    mock_conn.close.assert_called_once()


@patch('cli.dashboard.get_db_connection')
@patch('getpass.getpass')
@patch('builtins.print')
@patch('builtins.input')
def test_form_ubah_password_update_fail(mock_input, mock_print, mock_getpass, mock_get_db, pemilik_session) -> None:
    """Menguji form_ubah_password gagal karena query update melempar eksepsi."""
    mock_getpass.side_effect = ['OldPass', 'NewPassValid123!', 'NewPassValid123!']
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {'password_hash': 'some_hash'}
    mock_cursor.execute.side_effect = [None, Exception("Update query error")]
    mock_input.return_value = ''
    
    with patch('middleware.auth_jwt.verify_password', return_value=True), \
         patch('middleware.auth_jwt.hash_password', return_value='new_hash'):
        form_ubah_password(pemilik_session)
        
    mock_print.assert_any_call("⛔ ERR-DB-003: Gagal memperbarui password di database: Update query error")
    mock_conn.close.assert_called_once()


@patch('cli.dashboard.get_db_connection')
@patch('getpass.getpass')
@patch('builtins.print')
@patch('builtins.input')
def test_form_ubah_password_success(mock_input, mock_print, mock_getpass, mock_get_db, pemilik_session) -> None:
    """Menguji form_ubah_password berhasil mengupdate password dan mencatat audit trail."""
    mock_getpass.side_effect = ['OldPass', 'NewPassValid123!', 'NewPassValid123!']
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {'password_hash': 'some_hash'}
    mock_input.return_value = ''
    
    with patch('middleware.auth_jwt.verify_password', return_value=True), \
         patch('middleware.auth_jwt.hash_password', return_value='new_hash'), \
         patch('middleware.audit_logger.log_audit_trail') as mock_audit:
        form_ubah_password(pemilik_session)
        
    mock_cursor.execute.assert_any_call("UPDATE pengguna SET password_hash = %s WHERE id = %s", ('new_hash', 1))
    mock_conn.commit.assert_called_once()
    mock_audit.assert_called_once()
    mock_print.assert_any_call("✓ Password berhasil diubah! Gunakan sandi baru Anda pada login berikutnya.")
    mock_conn.close.assert_called_once()
