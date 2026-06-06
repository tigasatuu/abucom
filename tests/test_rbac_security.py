"""
Nama Modul: test_rbac_security.py
Deskripsi: Unit & Integration testing untuk validasi matriks RBAC Multi-Level.
           (Ref: Module Structure v1.2 Bab 11.3, ACM v1.2)
Author: Antigravity (STK-015)
Tanggal: 2026-06-07
"""

# 1. Standard Library
from unittest.mock import MagicMock, patch

# 2. Third-Party
import pytest

# 3. Local Modules
from middleware.rbac_guard import (
    check_menu_permission,
    get_visible_menus,
    require_role,
    RBAC_MATRIX,
    ACCESS_FULL,
    ACCESS_READ,
    ACCESS_INPUT,
    ACCESS_INPUT_READ,
    ACCESS_RTL,
    ACCESS_ESC,
    ACCESS_DENY
)
from middleware.auth_jwt import VALID_ROLES, Result


def test_rbac_matrix_completeness() -> None:
    """Menguji kelengkapan entry RBAC_MATRIX (tepat 44 entry)."""
    assert len(RBAC_MATRIX) == 44


def test_pemilik_has_full_access_all_menus() -> None:
    """Menguji bahwa peran 'pemilik' memiliki level akses FULL pada seluruh menu."""
    for menu_id in RBAC_MATRIX:
        assert check_menu_permission(menu_id, 'pemilik') == ACCESS_FULL


def test_default_deny_unknown_role() -> None:
    """Menguji Default Deny Policy: peran tidak dikenal mendapat ACCESS_DENY."""
    for menu_id in RBAC_MATRIX:
        assert check_menu_permission(menu_id, 'guest') == ACCESS_DENY
        assert check_menu_permission(menu_id, 'operator') == ACCESS_DENY


def test_kasir_denied_payroll() -> None:
    """Menguji bahwa kasir ditolak memproses gaji (MENU-M4-002)."""
    assert check_menu_permission('MENU-M4-002', 'kasir') == ACCESS_DENY


def test_gudang_denied_transaksi() -> None:
    """Menguji bahwa staf gudang ditolak mengakses menu transaksi (MENU-M1-001)."""
    assert check_menu_permission('MENU-M1-001', 'gudang') == ACCESS_DENY


def test_desainer_access_arsip_desain() -> None:
    """Menguji bahwa desainer memiliki akses FULL ke arsip desain (MENU-M5-002)."""
    assert check_menu_permission('MENU-M5-002', 'desainer') == ACCESS_FULL


def test_kepala_no_inheritance() -> None:
    """Menguji No Inheritance Policy: kepala_percetakan dilarang mengakses DP & Pelunasan (MENU-M1-003)."""
    assert check_menu_permission('MENU-M1-003', 'kepala_percetakan') == ACCESS_DENY


def test_fotocopy_print_rtl_access() -> None:
    """Menguji bahwa fotocopy_print memiliki level akses RTL untuk transaksi (MENU-M1-001)."""
    assert check_menu_permission('MENU-M1-001', 'fotocopy_print') == ACCESS_RTL


def test_get_visible_menus_kasir() -> None:
    """Menguji filter menu dinamis untuk peran kasir."""
    visible = get_visible_menus('kasir')
    # Pastikan USE CASE DASAR tidak masuk (sesuai filter MENU-M)
    for menu_id, label, level in visible:
        assert menu_id.startswith('MENU-M')
        assert level != ACCESS_DENY
        # Kasir tidak boleh melihat payroll (MENU-M4-002)
        assert menu_id != 'MENU-M4-002'


def test_get_visible_menus_pemilik_returns_all_modules() -> None:
    """Menguji filter menu dinamis untuk peran pemilik mengembalikan semua 40 menu modul."""
    visible = get_visible_menus('pemilik')
    assert len(visible) == 40 # 44 total - 4 base use cases


@patch('middleware.rbac_guard.validate_session_token')
@patch('middleware.rbac_guard._log_access_denied')
def test_require_role_decorator_allowed(mock_log, mock_validate) -> None:
    """Menguji dekorator require_role ketika akses diizinkan."""
    mock_validate.return_value = Result(True, {}, None)
    
    call_tracker = MagicMock()
    
    @require_role('MENU-M10-001')
    def dummy_func(session, access_level):
        call_tracker(access_level)
        return "SUCCESS"
        
    res = dummy_func({'role': 'pemilik'})
    assert res == "SUCCESS"
    call_tracker.assert_called_once_with(ACCESS_FULL)
    mock_log.assert_not_called()


@patch('middleware.rbac_guard.validate_session_token')
@patch('middleware.rbac_guard._log_access_denied')
def test_require_role_decorator_denied(mock_log, mock_validate) -> None:
    """Menguji dekorator require_role mencatatkan audit log dan menolak akses ketika role tidak berwenang."""
    mock_validate.return_value = Result(True, {}, None)
    
    call_tracker = MagicMock()
    
    @require_role('MENU-M10-001')
    def dummy_func(session, access_level):
        call_tracker()
        return "SUCCESS"
        
    session = {'role': 'kasir', 'user_id': 5, 'cabang_id': 1}
    res = dummy_func(session)
    
    assert isinstance(res, Result)
    assert res.is_success is False
    assert "ERR-AUTH-003" in res.error_msg
    call_tracker.assert_not_called()
    mock_log.assert_called_once_with(session, 'MENU-M10-001', 'kasir')
