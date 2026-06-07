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


# === FIXTURES & NEW SCENARIO TESTS ===

@pytest.fixture
def clean_session():
    """Fixture untuk membangun session_state bersih dan menjamin isolasi variabel."""
    session = {}
    yield session
    session.clear()


@patch('middleware.rbac_guard.validate_session_token')
@patch('middleware.rbac_guard._log_access_denied')
def test_pemilik_akses_kritis_diterima(mock_log, mock_validate, clean_session) -> None:
    """Skenario Positif: pemilik berhasil mengakses menu finansial kritis (MENU-M4-002)."""
    clean_session.update({'role': 'pemilik', 'user_id': 1, 'cabang_id': 1})
    mock_validate.return_value = Result(True, clean_session, None)
    
    @require_role('MENU-M4-002')
    def target_func(session):
        return "PAYROLL_COMPUTED"
        
    res = target_func(clean_session)
    assert res == "PAYROLL_COMPUTED"
    mock_log.assert_not_called()


@patch('middleware.rbac_guard.validate_session_token')
@patch('middleware.rbac_guard._log_access_denied')
def test_kasir_transaksi_normal_diterima(mock_log, mock_validate, clean_session) -> None:
    """Skenario Positif: kasir mengakses transaksi normal (MENU-M1-001) dengan level akses tepat."""
    clean_session.update({'role': 'kasir', 'user_id': 2, 'cabang_id': 1})
    mock_validate.return_value = Result(True, clean_session, None)
    
    @require_role('MENU-M1-001')
    def target_func(session, access_level):
        assert access_level == ACCESS_FULL
        return "TRANSACTION_SUCCESS"
        
    res = target_func(clean_session)
    assert res == "TRANSACTION_SUCCESS"
    mock_log.assert_not_called()


@patch('middleware.rbac_guard.validate_session_token')
@patch('middleware.rbac_guard._log_access_denied')
def test_desainer_ditolak_pada_menu_finansial(mock_log, mock_validate, clean_session) -> None:
    """Skenario Negatif: desainer dilarang mengakses margin produk (MENU-M1-005) dan menghasilkan ERR-AUTH-003."""
    clean_session.update({'role': 'desainer', 'user_id': 3, 'cabang_id': 1})
    mock_validate.return_value = Result(True, clean_session, None)
    
    @require_role('MENU-M1-005')
    def target_func(session):
        return "SUCCESS"
        
    with patch('builtins.print') as mock_print:
        res = target_func(clean_session)
        
    assert isinstance(res, Result)
    assert res.is_success is False
    assert "ERR-AUTH-003" in res.error_msg
    
    # Memastikan error tercetak di CLI terminal
    printed_any = False
    for call in mock_print.call_args_list:
        msg = call[0][0]
        if "ERR-AUTH-003" in msg:
            printed_any = True
            break
    assert printed_any, "Terminal tidak menampilkan ERR-AUTH-003"
    mock_log.assert_called_once_with(clean_session, 'MENU-M1-005', 'desainer')


@patch('middleware.rbac_guard.validate_session_token')
@patch('middleware.rbac_guard._log_access_denied')
def test_default_deny_policy_untuk_unrecognized_role(mock_log, mock_validate, clean_session) -> None:
    """Skenario Negatif: default deny policy memblokir session kotor (tanpa role atau role 'hacker')."""
    # 1. Tanpa role
    clean_session.update({'user_id': 99, 'cabang_id': 1})
    mock_validate.return_value = Result(True, clean_session, None)
    
    @require_role('MENU-M1-001')
    def target_func(session):
        return "OK"
        
    res = target_func(clean_session)
    assert isinstance(res, Result)
    assert res.is_success is False
    assert "ERR-AUTH-003" in res.error_msg
    
    # 2. Peran tidak dikenal ('hacker')
    clean_session.clear()
    clean_session.update({'role': 'hacker', 'user_id': 99, 'cabang_id': 1})
    
    res = target_func(clean_session)
    assert isinstance(res, Result)
    assert res.is_success is False
    assert "ERR-AUTH-003" in res.error_msg


def test_jwt_expiration_boundary_blocked() -> None:
    """Boundary Case: validasi JWT expired (timestamp melebihi 28800 detik) diblokir dengan ERR-SESSION-002."""
    import jwt
    import datetime
    from config.settings import load_settings
    from middleware.auth_jwt import validate_session_token
    
    settings = load_settings()
    secret_key = settings.jwt_secret_key
    
    # Membuat token expired (exp di masa lalu)
    expired_payload = {
        'user_id': 1,
        'username': 'pemilik_toko',
        'role': 'pemilik',
        'cabang_id': 1,
        'exp': datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=10)
    }
    expired_token = jwt.encode(expired_payload, secret_key, algorithm='HS256')
    
    session = {'token': expired_token}
    res = validate_session_token(session)
    
    assert res.is_success is False
    assert "ERR-SESSION-002" in res.error_msg


@patch('getpass.getpass')
def test_verify_supervisor_escalation_failure(mock_getpass) -> None:
    """Edge Case: pengujian eskalasi supervisor salah sandi menghasilkan error code spesifik."""
    from middleware.rbac_guard import verify_supervisor_escalation
    
    # Mock database connection & cursor
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    
    mock_cursor.fetchone.return_value = {
        'id': 1,
        'password_hash': '$2b$12$DummyHashStringForTestingOnly...',
        'cabang_id': 1
    }
    
    # 1. Sandi pemilik salah -> ERR-AUTH-029
    mock_getpass.return_value = 'SandiSalah'
    with patch('middleware.auth_jwt.verify_password', return_value=False):
        res_pemilik = verify_supervisor_escalation('pemilik', mock_db)
        
    assert res_pemilik.is_success is False
    assert "ERR-AUTH-029" in res_pemilik.error_msg
    
    # 2. Sandi kepala_percetakan salah -> ERR-AUTH-003
    mock_getpass.return_value = 'SandiSalah'
    with patch('middleware.auth_jwt.verify_password', return_value=False):
        res_kepala = verify_supervisor_escalation('kepala_percetakan', mock_db)
        
    assert res_kepala.is_success is False
    assert "ERR-AUTH-003" in res_kepala.error_msg


@patch('middleware.rbac_guard.validate_session_token')
@patch('middleware.rbac_guard._log_access_denied')
def test_session_state_immutability(mock_log, mock_validate, clean_session) -> None:
    """Edge Case: memastikan dictionary session_state tidak termutasi setelah melewati decorator."""
    clean_session.update({'role': 'pemilik', 'user_id': 1, 'cabang_id': 1})
    mock_validate.return_value = Result(True, clean_session, None)
    
    session_copy = clean_session.copy()
    
    @require_role('MENU-M4-002')
    def target_func(session):
        return "SUCCESS"
        
    target_func(clean_session)
    assert clean_session == session_copy


@patch('middleware.rbac_guard.validate_session_token')
@patch('db.db_connector.get_db_connection')
@patch('middleware.audit_logger.log_audit_trail')
def test_require_role_decorator_logs_audit_denied(mock_log_audit, mock_get_db, mock_validate, clean_session) -> None:
    """Keamanan DB: akses ditolak harus memicu log_audit_trail ter-mock dengan action_type='ACCESS_DENIED' tanpa query DB."""
    clean_session.update({'role': 'desainer', 'user_id': 5, 'cabang_id': 2})
    mock_validate.return_value = Result(True, clean_session, None)
    
    mock_conn = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    
    @require_role('MENU-M4-002')
    def target_func(session):
        return "SUCCESS"
        
    with patch('builtins.print'):
        target_func(clean_session)
        
    # Verifikasi argument pemanggilan audit trail
    mock_log_audit.assert_called_once()
    kwargs = mock_log_audit.call_args[1]
    assert kwargs['pengguna_id'] == 5
    assert kwargs['action_type'] == 'ACCESS_DENIED'
    assert kwargs['target_table'] == 'MENU-M4-002'
    assert kwargs['cabang_id'] == 2
    assert kwargs['db_connection'] == mock_conn
    mock_conn.close.assert_called_once()


@patch('middleware.rbac_guard.validate_session_token')
def test_require_role_decorator_session_token_invalid(mock_validate, clean_session) -> None:
    """Menguji dekorator require_role ketika token sesi tidak valid (ERR-SESSION-002)."""
    mock_validate.return_value = Result(False, None, "ERR-SESSION-002: Sesi login tidak sah/rusak. Harap login kembali!")
    
    @require_role('MENU-M1-001')
    def dummy_func(session):
        return "SUCCESS"
        
    with patch('builtins.print') as mock_print:
        res = dummy_func(clean_session)
        
    assert isinstance(res, Result)
    assert res.is_success is False
    assert "ERR-SESSION-002" in res.error_msg
    mock_print.assert_called_once()


def test_verify_supervisor_escalation_not_found() -> None:
    """Menguji verify_supervisor_escalation ketika supervisor tidak ditemukan di database."""
    from middleware.rbac_guard import verify_supervisor_escalation
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None  # Not found
    
    res = verify_supervisor_escalation('pemilik', mock_db)
    assert res.is_success is False
    assert "ERR-AUTH-003" in res.error_msg


@patch('getpass.getpass')
def test_verify_supervisor_escalation_success(mock_getpass) -> None:
    """Menguji verify_supervisor_escalation ketika otorisasi supervisor berhasil."""
    from middleware.rbac_guard import verify_supervisor_escalation
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {
        'id': 1,
        'password_hash': '$2b$12$Dummy...',
        'cabang_id': 1
    }
    mock_getpass.return_value = 'SandiBenar123'
    with patch('middleware.auth_jwt.verify_password', return_value=True):
        res = verify_supervisor_escalation('pemilik', mock_db)
        
    assert res.is_success is True
    assert res.data['supervisor_id'] == 1
    assert res.data['cabang_id'] == 1


@patch('db.db_connector.get_db_connection')
@patch('middleware.audit_logger.log_audit_trail')
def test_log_access_denied_none_user_and_cabang(mock_log_audit, mock_get_db, clean_session) -> None:
    """Menguji fungsi internal _log_access_denied saat user_id dan cabang_id bernilai None."""
    from middleware.rbac_guard import _log_access_denied
    
    clean_session.update({'user_id': None, 'cabang_id': None, 'role': 'desainer'})
    mock_conn = MagicMock()
    mock_get_db.return_value = Result(True, mock_conn, None)
    
    _log_access_denied(clean_session, 'MENU-M1-005', 'desainer')
    
    mock_log_audit.assert_called_once()
    kwargs = mock_log_audit.call_args[1]
    assert kwargs['pengguna_id'] == 0
    assert kwargs['cabang_id'] == 1
    mock_conn.close.assert_called_once()


def test_get_visible_modules_pemilik() -> None:
    """Menguji bahwa peran pemilik memiliki akses ke semua 10 modul."""
    from middleware.rbac_guard import get_visible_modules
    mods = get_visible_modules('pemilik')
    assert len(mods) == 10
    keys = [m[0] for m in mods]
    assert keys == ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10']


def test_get_visible_modules_kasir() -> None:
    """Menguji modul yang terlihat untuk peran kasir."""
    from middleware.rbac_guard import get_visible_modules
    mods = get_visible_modules('kasir')
    keys = [m[0] for m in mods]
    assert 'M1' in keys
    assert 'M2' not in keys  # Gudang only
    assert 'M10' not in keys  # Pemilik only (lockdown)


def test_get_module_submenus_m1_kasir() -> None:
    """Menguji filter sub-menu M1 untuk peran kasir."""
    from middleware.rbac_guard import get_module_submenus
    submenus = get_module_submenus('M1', 'kasir')
    menu_ids = [s[0] for s in submenus]
    assert 'MENU-M1-001' in menu_ids
    assert 'MENU-M1-003' in menu_ids
    assert 'MENU-M1-005' not in menu_ids  # Pemilik only


