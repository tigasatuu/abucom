"""
Nama Modul: test_config_cache.py
Deskripsi: Unit testing untuk modul config_cache.py, rbac_guard.py, and menu_configs.py.
Author: Antigravity AI
Tanggal: 2026-06-05
"""

# 1. Standard Library
from decimal import Decimal
from unittest.mock import MagicMock, patch

# 2. Third-Party
import pytest

# 3. Local Modules
from db.config_cache import (
    _config_cache,
    load_all_configs,
    get_config_value,
    get_config_decimal,
    get_all_configs_list,
    update_config_value,
    ConfigParam
)
from middleware.rbac_guard import require_role, check_menu_permission
from cli.menu_configs import form_update_parameter


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    # Setup: Clear cache and pre-populate for test cases
    _config_cache.clear()
    _config_cache['target_laba_payroll'] = '15000000.0000'
    _config_cache['porsi_gaji_laba'] = '0.2500'
    _config_cache['limit_kasbon_staf'] = '1000000.0000'
    
    with patch('middleware.rbac_guard.validate_session_token') as mock_val:
        from middleware.auth_jwt import Result
        mock_val.return_value = Result(True, {}, None)
        yield
        
    _config_cache.clear()


def test_get_config_decimal_valid() -> None:
    """Memverifikasi pengambilan nilai desimal valid dari cache."""
    val = get_config_decimal('target_laba_payroll')
    assert val == Decimal('15000000.0000')


def test_get_config_decimal_not_found() -> None:
    """Memverifikasi fallback ke default jika key tidak ada."""
    val = get_config_decimal('nonexistent_key')
    assert val == Decimal('0.0000')
    
    val_custom = get_config_decimal('nonexistent_key', Decimal('150.0000'))
    assert val_custom == Decimal('150.0000')


def test_get_config_value_valid() -> None:
    """Memverifikasi pengambilan nilai string valid dari cache."""
    val = get_config_value('limit_kasbon_staf')
    assert val == '1000000.0000'


def test_get_config_value_default() -> None:
    """Memverifikasi fallback ke default jika key tidak ada."""
    val = get_config_value('nonexistent', 'fallback')
    assert val == 'fallback'


def test_load_all_configs_success() -> None:
    """Memverifikasi load_all_configs mempopulasi cache dengan benar."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'parameter_key': 'target_laba_payroll', 'parameter_value': '15000000.0000', 'tipe_data': 'DECIMAL', 'deskripsi': 'Desc A'},
        {'id': 2, 'parameter_key': 'porsi_gaji_laba', 'parameter_value': '0.2500', 'tipe_data': 'DECIMAL', 'deskripsi': 'Desc B'}
    ]
    
    # Kosongkan cache untuk mengetes pemuatan ulang
    _config_cache.clear()
    
    res = load_all_configs(mock_conn, cabang_id=1)
    
    assert res.is_success is True
    assert res.data == 2
    assert _config_cache['target_laba_payroll'] == '15000000.0000'
    assert _config_cache['porsi_gaji_laba'] == '0.2500'


def test_load_all_configs_failure() -> None:
    """Memverifikasi penanganan error jika load_all_configs gagal."""
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = Exception("MySQL connection lost")
    
    res = load_all_configs(mock_conn, cabang_id=1)
    assert res.is_success is False
    assert "ERR-DB-010" in res.error_msg


def test_get_all_configs_list() -> None:
    """Memverifikasi fungsi pengambilan daftar kustom ConfigParam."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'parameter_key': 'target_laba_payroll', 'parameter_value': '15000000.0000', 'tipe_data': 'DECIMAL', 'deskripsi': 'Desc A'}
    ]
    
    res = get_all_configs_list(mock_conn, cabang_id=1)
    assert res.is_success is True
    assert len(res.data) == 1
    assert isinstance(res.data[0], ConfigParam)
    assert res.data[0].parameter_key == 'target_laba_payroll'


def test_update_config_value_success() -> None:
    """Memverifikasi keberhasilan pembaruan data dan cache secara sinkron."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_cursor.fetchone.return_value = {
        'parameter_key': 'target_laba_payroll',
        'parameter_value': '15000000.0000'
    }
    
    res = update_config_value(mock_conn, config_id=1, new_value='18000000.0000', cabang_id=1)
    
    assert res.is_success is True
    assert res.data['old_value'] == '15000000.0000'
    assert res.data['new_value'] == '18000000.0000'
    assert _config_cache['target_laba_payroll'] == '18000000.0000'
    mock_conn.commit.assert_called_once()


def test_update_config_value_failure() -> None:
    """Memverifikasi rollback dijalankan jika terjadi error database saat update."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_cursor.fetchone.return_value = {
        'parameter_key': 'target_laba_payroll',
        'parameter_value': '15000000.0000'
    }
    mock_cursor.execute.side_effect = [None, Exception("Deadlock occurred")]
    
    res = update_config_value(mock_conn, config_id=1, new_value='18000000.0000', cabang_id=1)
    
    assert res.is_success is False
    assert "ERR-DB-011" in res.error_msg
    mock_conn.rollback.assert_called_once()


# Validasi masukan desimal di menu_configs
@patch('builtins.input', return_value='')
@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_validate_decimal_input_valid(mock_db, mock_console, mock_input) -> None:
    """Simulasi input valid desimal positif."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    mock_console.input.side_effect = ['1200000', 'Y']  # input baru, konfirmasi Y
    
    selected_config = ConfigParam(1, 'limit_kasbon_staf', '1000000.0000', 'DECIMAL', 'Limit Kasbon Staf')
    
    with patch('cli.menu_configs.update_config_value') as mock_update, \
         patch('cli.menu_configs.log_audit_trail') as mock_audit:
         
        mock_update.return_value = MagicMock(is_success=True)
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, selected_config)
        
        mock_update.assert_called_once_with(mock_conn, 1, '1200000.0000', 1)
        mock_audit.assert_called_once()


@patch('builtins.input', return_value='')
@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_validate_decimal_input_negative(mock_db, mock_console, mock_input) -> None:
    """Simulasi input negatif desimal ditolak dengan ERR-VAL-038."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    mock_console.input.side_effect = ['-500']  # input negatif
    
    selected_config = ConfigParam(1, 'limit_kasbon_staf', '1000000.0000', 'DECIMAL', 'Limit Kasbon Staf')
    
    with patch('cli.menu_configs.update_config_value') as mock_update:
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, selected_config)
        mock_update.assert_not_called()
        
        # Pastikan error code ERR-VAL-038 dicetak ke console
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("ERR-VAL-038" in arg for arg in printed_args)


@patch('builtins.input', return_value='')
@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_validate_decimal_input_non_numeric(mock_db, mock_console, mock_input) -> None:
    """Simulasi input non-numerik (string) ditolak dengan ERR-VAL-038."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    mock_console.input.side_effect = ['abc']  # input non-numerik
    
    selected_config = ConfigParam(1, 'limit_kasbon_staf', '1000000.0000', 'DECIMAL', 'Limit Kasbon Staf')
    
    with patch('cli.menu_configs.update_config_value') as mock_update:
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, selected_config)
        mock_update.assert_not_called()
        
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("ERR-VAL-038" in arg for arg in printed_args)


# Uji pembatasan akses RBAC
def test_rbac_check_menu_permission() -> None:
    """Memverifikasi pemetaan peran pada matriks RBAC."""
    assert check_menu_permission('MENU-M10-001', 'pemilik') is True
    assert check_menu_permission('MENU-M10-001', 'kasir') is False
    assert check_menu_permission('MENU-M10-001', 'gudang') is False


def test_rbac_require_role_decorator() -> None:
    """Memverifikasi dekorator require_role menolak non-pemilik untuk menu M10."""
    call_tracker = MagicMock()
    
    @require_role('MENU-M10-001')
    def dummy_configs_function(session_state):
        call_tracker()
        return "SUCCESS"
        
    # Peran pemilik diizinkan
    res_pemilik = dummy_configs_function({'role': 'pemilik'})
    assert res_pemilik == "SUCCESS"
    assert call_tracker.call_count == 1
    
    # Peran kasir ditolak (returns None)
    res_kasir = dummy_configs_function({'role': 'kasir'})
    assert res_kasir is None
    assert call_tracker.call_count == 1  # tidak bertambah
