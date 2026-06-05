"""
Nama Modul: test_m10_runtime_config.py
Deskripsi: Unit testing fungsional murni terisolasi penuh untuk Modul M.10
           (Konfigurasi Parameter Bisnis Runtime Dinamis), menguji pemuatan,
           pembaruan, RBAC, dan validasi input batas parameter.
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
from cli.menu_configs import show_menu_configs, form_update_parameter


@pytest.fixture(autouse=True)
def clean_config_cache_state():
    """Fixture untuk mereset state _config_cache sebelum dan sesudah pengujian."""
    _config_cache.clear()
    # Inisialisasi data default awal
    _config_cache['umr_daerah'] = '4500000.0000'
    _config_cache['limit_opex'] = '5000000.0000'
    _config_cache['toleransi_kasir'] = '50000.0000'
    _config_cache['batas_hari_kasbon'] = '30'
    _config_cache['nama_toko'] = 'AbuCom Bandung'
    yield
    _config_cache.clear()


@pytest.fixture(autouse=True)
def mock_stdin_input():
    """Fixture untuk mem-mock builtins.input agar tidak memicu OSError saat pytest capturing."""
    with patch('builtins.input', return_value=''):
        yield



# ==============================================================================
# A. SKENARIO POSITIF (HAPPY PATH)
# ==============================================================================

def test_load_all_configs_happy_path() -> None:
    """A.1: Mampu memuat seluruh data dari database ke cache memori tanpa kesalahan format."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'parameter_key': 'umr_daerah', 'parameter_value': '4500000.0000', 'tipe_data': 'DECIMAL', 'deskripsi': 'UMR Daerah'},
        {'id': 2, 'parameter_key': 'limit_opex', 'parameter_value': '5000000.0000', 'tipe_data': 'DECIMAL', 'deskripsi': 'Limit OPEX'},
        {'id': 3, 'parameter_key': 'batas_hari_kasbon', 'parameter_value': '30', 'tipe_data': 'INTEGER', 'deskripsi': 'Batas Kasbon'},
        {'id': 4, 'parameter_key': 'nama_toko', 'parameter_value': 'AbuCom Bandung', 'tipe_data': 'VARCHAR', 'deskripsi': 'Nama Toko'}
    ]
    
    # Kosongkan cache terlebih dahulu untuk memverifikasi pemuatan
    _config_cache.clear()
    
    res = load_all_configs(mock_conn, cabang_id=1)
    
    assert res.is_success is True
    assert res.data == 4
    assert res.error_msg is None
    
    # Verifikasi cache terpopulasi dengan benar
    assert get_config_value('umr_daerah') == '4500000.0000'
    assert get_config_value('limit_opex') == '5000000.0000'
    assert get_config_value('batas_hari_kasbon') == '30'
    assert get_config_value('nama_toko') == 'AbuCom Bandung'


def test_update_config_value_happy_path() -> None:
    """A.2: Mampu memperbarui parameter bisnis spesifik dan memverifikasi nilainya kembali (tipe Decimal)."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    # Simulasi SELECT sebelum update
    mock_cursor.fetchone.return_value = {
        'parameter_key': 'umr_daerah',
        'parameter_value': '4500000.0000'
    }
    
    res = update_config_value(mock_conn, config_id=1, new_value='4800000.0000', cabang_id=1)
    
    assert res.is_success is True
    assert res.data['old_value'] == '4500000.0000'
    assert res.data['new_value'] == '4800000.0000'
    assert res.data['parameter_key'] == 'umr_daerah'
    
    # Pastikan database commit dipanggil
    mock_conn.commit.assert_called_once()
    
    # Verifikasi cache terupdate dan bisa diambil dalam format Decimal
    assert get_config_value('umr_daerah') == '4800000.0000'
    assert get_config_decimal('umr_daerah') == Decimal('4800000.0000')


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_form_update_parameter_confirm_no(mock_db, mock_console) -> None:
    """A.3: Mampu membatalkan update parameter ketika konfirmasi pengguna bernilai bukan 'Y' (misal 'N')."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    
    # Mock console inputs:
    # 1. Nilai baru: '4600000'
    # 2. Konfirmasi: 'N' (Tidak dilanjutkan)
    mock_console.input.side_effect = ['4600000', 'N']
    
    selected_config = ConfigParam(1, 'umr_daerah', '4500000.0000', 'DECIMAL', 'UMR Daerah')
    
    with patch('cli.menu_configs.update_config_value') as mock_update:
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, selected_config)
        
        # Pastikan fungsi update ke database TIDAK dijalankan
        mock_update.assert_not_called()
        
        # Pastikan cache tetap bernilai lama
        assert get_config_value('umr_daerah') == '4500000.0000'
        
        # Verifikasi pesan pembatalan dicetak
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("Perubahan dibatalkan." in arg for arg in printed_args)


# ==============================================================================
# B. SKENARIO NEGATIF (EDGE CASES & KEAMANAN)
# ==============================================================================

def test_rbac_check_menu_permission_configs() -> None:
    """B.1.1: Memverifikasi otorisasi matriks RBAC untuk menu konfigurasi M.10."""
    # Hanya pemilik yang boleh mengakses
    assert check_menu_permission('MENU-M10-001', 'pemilik') is True
    
    # Peran lain wajib ditolak
    assert check_menu_permission('MENU-M10-001', 'kasir') is False
    assert check_menu_permission('MENU-M10-001', 'gudang') is False
    assert check_menu_permission('MENU-M10-001', 'desainer') is False
    assert check_menu_permission('MENU-M10-001', 'operator') is False


def test_rbac_require_role_decorator_configs() -> None:
    """B.1.2: Memverifikasi dekorator require_role menghalangi fungsi akses menu M.10 bagi non-pemilik."""
    call_tracker = MagicMock()
    
    @require_role('MENU-M10-001')
    def test_target_function(session_state):
        call_tracker()
        return "AUTHORIZED"

    # Pemilik diizinkan masuk
    res_pemilik = test_target_function({'role': 'pemilik'})
    assert res_pemilik == "AUTHORIZED"
    assert call_tracker.call_count == 1
    
    # Kasir ditolak (fungsi mengembalikan None dan tidak dieksekusi)
    res_kasir = test_target_function({'role': 'kasir'})
    assert res_kasir is None
    assert call_tracker.call_count == 1  # call_count tidak bertambah


def test_update_config_value_unregistered_key() -> None:
    """B.2: Menguji percobaan update key konfigurasi yang tidak terdaftar di database."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    # Simulasi SELECT mengembalikan None (ID tidak terdaftar)
    mock_cursor.fetchone.return_value = None
    
    res = update_config_value(mock_conn, config_id=999, new_value='4800000.0000', cabang_id=1)
    
    assert res.is_success is False
    assert "ERR-DB-011" in res.error_msg
    assert "tidak ditemukan" in res.error_msg
    
    # Pastikan database rollback dipanggil dan commit tidak dipanggil
    mock_conn.rollback.assert_called_once()
    mock_conn.commit.assert_not_called()


def test_load_all_configs_database_exception() -> None:
    """B.3.1: Memastikan penanganan error internal saat database crash sewaktu load configs."""
    mock_conn = MagicMock()
    # Simulasi database terputus sewaktu kursor dibuat
    mock_conn.cursor.side_effect = Exception("Lost connection to MySQL server")
    
    res = load_all_configs(mock_conn, cabang_id=1)
    
    assert res.is_success is False
    assert "ERR-DB-010" in res.error_msg
    assert "Gagal memuat config" in res.error_msg


def test_update_config_value_database_exception() -> None:
    """B.3.2: Memastikan penanganan error internal saat database crash sewaktu update config."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    
    # Mengembalikan data row saat SELECT awal
    mock_cursor.fetchone.return_value = {
        'parameter_key': 'umr_daerah',
        'parameter_value': '4500000.0000'
    }
    # Simulasi kegagalan saat eksekusi UPDATE
    mock_cursor.execute.side_effect = [None, Exception("Deadlock detected")]
    
    res = update_config_value(mock_conn, config_id=1, new_value='4800000.0000', cabang_id=1)
    
    assert res.is_success is False
    assert "ERR-DB-011" in res.error_msg
    
    # Pastikan rollback dipanggil
    mock_conn.rollback.assert_called_once()


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_show_menu_configs_db_connection_fail(mock_db, mock_console) -> None:
    """B.3.3: Memastikan show_menu_configs tidak crash ketika koneksi database gagal."""
    mock_db.return_value = MagicMock(is_success=False, error_msg="Timeout")
    
    with patch('builtins.input', return_value=''):
        # Memanggil show_menu_configs, harus keluar dengan anggun
        show_menu_configs({'role': 'pemilik', 'cabang_id': 1})
        
        # Verifikasi pesan kesalahan dicetak ke layar
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("ERR-DB-002" in arg for arg in printed_args)


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_show_menu_configs_load_fail(mock_db, mock_console) -> None:
    """B.3.4: Memastikan show_menu_configs tidak crash ketika loading list configs dari DB gagal."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    
    with patch('cli.menu_configs.get_all_configs_list') as mock_get_list, \
         patch('builtins.input', return_value=''):
        
        mock_get_list.return_value = MagicMock(is_success=False, error_msg="ERR-DB-010 Mock Failure")
        
        # Memanggil menu, harus kembali anggun tanpa exception
        show_menu_configs({'role': 'pemilik', 'cabang_id': 1})
        
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("ERR-DB-010 Mock Failure" in arg for arg in printed_args)


# ==============================================================================
# C. SKENARIO VALIDASI INPUT (BOUNDARY VALIDATIONS)
# ==============================================================================

@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
@pytest.mark.parametrize("invalid_int_input", ["abc", "-10", "15.5", ""])
def test_form_update_parameter_invalid_integer(mock_db, mock_console, invalid_int_input) -> None:
    """C.1: Validasi menolak input non-integer, negatif, desimal, atau kosong untuk parameter bertipe INTEGER."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    mock_console.input.return_value = invalid_int_input
    
    selected_config = ConfigParam(4, 'batas_hari_kasbon', '30', 'INTEGER', 'Batas Hari Kasbon')
    
    with patch('cli.menu_configs.update_config_value') as mock_update:
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, selected_config)
        
        # Update database tidak boleh dipanggil
        mock_update.assert_not_called()
        
        # Pesan kesalahan input integer harus dicetak
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("harus diisi berupa angka bulat positif" in arg for arg in printed_args)


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
@pytest.mark.parametrize("invalid_dec_input", ["-500000", "-0.0001", "abc", ""])
def test_form_update_parameter_invalid_decimal(mock_db, mock_console, invalid_dec_input) -> None:
    """C.2: Validasi menolak nilai desimal negatif atau format salah untuk parameter bertipe DECIMAL (e.g. Limit OPEX / UMR) dengan ERR-VAL-038."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    mock_console.input.return_value = invalid_dec_input
    
    selected_config = ConfigParam(2, 'limit_opex', '5000000.0000', 'DECIMAL', 'Limit OPEX')
    
    with patch('cli.menu_configs.update_config_value') as mock_update:
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, selected_config)
        
        # Update database tidak boleh dipanggil
        mock_update.assert_not_called()
        
        # Harus memicu kesalahan spesifik ERR-VAL-038
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("ERR-VAL-038" in arg for arg in printed_args)


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_form_update_parameter_empty_varchar(mock_db, mock_console) -> None:
    """C.3: Validasi menolak input kosong untuk parameter bertipe VARCHAR (e.g. Nama Toko)."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    mock_console.input.return_value = ""  # string kosong
    
    selected_config = ConfigParam(5, 'nama_toko', 'AbuCom Bandung', 'VARCHAR', 'Nama Toko')
    
    with patch('cli.menu_configs.update_config_value') as mock_update:
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, selected_config)
        
        # Update database tidak boleh dipanggil
        mock_update.assert_not_called()
        
        # Pesan kesalahan input kosong harus dicetak
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("tidak boleh kosong" in arg for arg in printed_args)


# ==============================================================================
# TAMBAHAN CAKUPAN UNIT TEST LAIN (FALLBACKS & DETAILS)
# ==============================================================================

def test_get_config_decimal_fallback() -> None:
    """Memverifikasi bahwa get_config_decimal melakukan fallback dengan benar ketika key tidak ada atau format salah."""
    # Key tidak ditemukan
    assert get_config_decimal('nonexistent_key') == Decimal('0.0000')
    assert get_config_decimal('nonexistent_key', Decimal('100.0000')) == Decimal('100.0000')
    
    # Nilai bukan format desimal valid
    _config_cache['invalid_dec_key'] = 'not-a-number'
    assert get_config_decimal('invalid_dec_key') == Decimal('0.0000')
    assert get_config_decimal('invalid_dec_key', Decimal('15.0000')) == Decimal('15.0000')


def test_get_config_value_fallback() -> None:
    """Memverifikasi bahwa get_config_value melakukan fallback dengan benar ketika key tidak ada."""
    assert get_config_value('nonexistent_key') is None
    assert get_config_value('nonexistent_key', 'fallback_val') == 'fallback_val'


def test_get_all_configs_list_db_exception() -> None:
    """Memverifikasi get_all_configs_list mengembalikan error Result sewaktu database exception."""
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = Exception("DB Connection Lost")
    
    res = get_all_configs_list(mock_conn, cabang_id=1)
    
    assert res.is_success is False
    assert "ERR-DB-010" in res.error_msg


def test_get_all_configs_list_happy_path() -> None:
    """Memverifikasi get_all_configs_list mengembalikan daftar ConfigParam saat sukses."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'parameter_key': 'umr_daerah', 'parameter_value': '4500000.0000', 'tipe_data': 'DECIMAL', 'deskripsi': 'UMR Daerah'}
    ]
    res = get_all_configs_list(mock_conn, cabang_id=1)
    assert res.is_success is True
    assert len(res.data) == 1
    assert res.data[0].parameter_key == 'umr_daerah'


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_show_menu_configs_happy_path(mock_db, mock_console) -> None:
    """Memverifikasi show_menu_configs menampilkan tabel dan menanggapi opsi yang valid lalu keluar."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    
    # 2 parameter
    configs_list = [
        ConfigParam(1, 'umr_daerah', '4500000.0000', 'DECIMAL', 'UMR Daerah'),
        ConfigParam(2, 'limit_opex', '5000000.0000', 'DECIMAL', 'Limit OPEX')
    ]
    
    # Input opsi pertama '1' (masuk form), lalu '0' (keluar)
    mock_console.input.side_effect = ['1', '0']
    
    with patch('cli.menu_configs.get_all_configs_list') as mock_get_list, \
         patch('cli.menu_configs.form_update_parameter') as mock_form:
        
        mock_get_list.return_value = MagicMock(is_success=True, data=configs_list)
        
        show_menu_configs({'role': 'pemilik', 'cabang_id': 1})
        
        # form_update_parameter dipanggil sekali dengan config pertama
        mock_form.assert_called_once_with({'role': 'pemilik', 'cabang_id': 1}, configs_list[0])


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_show_menu_configs_invalid_options(mock_db, mock_console) -> None:
    """Memverifikasi show_menu_configs menangani input opsi tidak valid dan non-numerik."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    
    configs_list = [
        ConfigParam(1, 'umr_daerah', '4500000.0000', 'DECIMAL', 'UMR Daerah')
    ]
    
    # Input '99' (out of range), 'abc' (non-numeric), then '0' (exit)
    mock_console.input.side_effect = ['99', 'abc', '0']
    
    with patch('cli.menu_configs.get_all_configs_list') as mock_get_list:
        mock_get_list.return_value = MagicMock(is_success=True, data=configs_list)
        
        show_menu_configs({'role': 'pemilik', 'cabang_id': 1})
        
        # Cek console print memuat pesan input salah
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("Nomor opsi tidak valid" in arg for arg in printed_args)
        assert any("Harap masukkan angka" in arg for arg in printed_args)


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_show_menu_configs_empty_list(mock_db, mock_console) -> None:
    """Memverifikasi show_menu_configs keluar dengan anggun jika daftar parameter kosong."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    
    with patch('cli.menu_configs.get_all_configs_list') as mock_get_list:
        mock_get_list.return_value = MagicMock(is_success=True, data=[])
        
        show_menu_configs({'role': 'pemilik', 'cabang_id': 1})
        
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("Tidak ada parameter konfigurasi yang ditemukan." in arg for arg in printed_args)


@patch('cli.menu_configs._console')
def test_form_update_parameter_nil_config(mock_console) -> None:
    """Memverifikasi form_update_parameter menangani config is None."""
    form_update_parameter({'role': 'pemilik', 'cabang_id': 1}, None)
    printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
    assert any("Tidak ada parameter yang dipilih." in arg for arg in printed_args)


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_form_update_parameter_db_fail(mock_db, mock_console) -> None:
    """Memverifikasi form_update_parameter menangani koneksi database gagal."""
    mock_db.return_value = MagicMock(is_success=False, error_msg="DB Fail")
    config = ConfigParam(1, 'umr_daerah', '4500000.0000', 'DECIMAL', 'UMR Daerah')
    form_update_parameter({'role': 'pemilik', 'cabang_id': 1}, config)
    printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
    assert any("ERR-DB-002" in arg for arg in printed_args)


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_form_update_parameter_integer_success(mock_db, mock_console) -> None:
    """Memverifikasi pembaruan integer sukses."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    mock_console.input.side_effect = ['45', 'Y']
    
    config = ConfigParam(4, 'batas_hari_kasbon', '30', 'INTEGER', 'Batas Hari Kasbon')
    
    with patch('cli.menu_configs.update_config_value') as mock_update, \
         patch('cli.menu_configs.log_audit_trail') as mock_audit:
        mock_update.return_value = MagicMock(is_success=True)
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, config)
        mock_update.assert_called_once_with(mock_conn, 4, '45', 1)
        mock_audit.assert_called_once()


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_form_update_parameter_varchar_success(mock_db, mock_console) -> None:
    """Memverifikasi pembaruan varchar sukses."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    mock_console.input.side_effect = ['AbuCom Riau', 'Y']
    
    config = ConfigParam(5, 'nama_toko', 'AbuCom Bandung', 'VARCHAR', 'Nama Toko')
    
    with patch('cli.menu_configs.update_config_value') as mock_update, \
         patch('cli.menu_configs.log_audit_trail') as mock_audit:
        mock_update.return_value = MagicMock(is_success=True)
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, config)
        mock_update.assert_called_once_with(mock_conn, 5, 'AbuCom Riau', 1)
        mock_audit.assert_called_once()


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_form_update_parameter_db_update_fail(mock_db, mock_console) -> None:
    """Memverifikasi form_update_parameter menangani kegagalan update database."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    mock_console.input.side_effect = ['AbuCom Riau', 'Y']
    
    config = ConfigParam(5, 'nama_toko', 'AbuCom Bandung', 'VARCHAR', 'Nama Toko')
    
    with patch('cli.menu_configs.update_config_value') as mock_update:
        mock_update.return_value = MagicMock(is_success=False, error_msg="ERR-DB-011 Update Failed")
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, config)
        
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("ERR-DB-011 Update Failed" in arg for arg in printed_args)


@patch('cli.menu_configs._console')
@patch('cli.menu_configs.get_db_connection')
def test_form_update_parameter_decimal_formatting_large(mock_db, mock_console) -> None:
    """Memverifikasi format cetakan decimal bernilai besar."""
    mock_conn = MagicMock()
    mock_db.return_value = MagicMock(is_success=True, data=mock_conn)
    mock_console.input.side_effect = ['1500000.5', 'Y']
    
    config = ConfigParam(1, 'umr_daerah', '4500000.0000', 'DECIMAL', 'UMR Daerah')
    
    with patch('cli.menu_configs.update_config_value') as mock_update, \
         patch('cli.menu_configs.log_audit_trail'):
        mock_update.return_value = MagicMock(is_success=True)
        form_update_parameter({'user_id': 1, 'role': 'pemilik', 'cabang_id': 1}, config)
        
        printed_args = [str(call_args[0][0]) for call_args in mock_console.print.call_args_list if call_args[0]]
        assert any("Rp " in arg for arg in printed_args)

