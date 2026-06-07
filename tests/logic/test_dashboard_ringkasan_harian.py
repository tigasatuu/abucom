"""
Nama Modul: test_dashboard_ringkasan_harian.py
Deskripsi: Unit testing terisolasi (mocked) untuk fitur Dashboard Ringkasan Harian per Role.
           (Ref: docs/issue/0127_issue_unit_test_feature_dashboard_ringkasan_harian_per_role.md)
Author: Antigravity
Tanggal: 2026-06-07
"""

import pytest
from decimal import Decimal
from datetime import date, timedelta
from unittest.mock import patch, MagicMock

# Import target modules
from middleware.auth_jwt import create_jwt_session, Result, validate_session_token
from cli.dashboard import (
    _render_summary_panels,
    _render_dashboard_pemilik,
    _render_dashboard_kepala,
    _render_dashboard_kasir,
    _render_dashboard_operasional,
    _render_dashboard_gudang,
    _render_dashboard_pramuniaga,
    _render_dashboard_fotocopy
)
from logic.financial_engine import hitung_laba_bersih_harian


def get_printed_text(mock_console, mock_print):
    """Helper to safely extract all text printed via Console and standard print, including Panel titles."""
    lines = []
    for call in mock_console.call_args_list:
        for arg in call[0]:
            if hasattr(arg, 'renderable'):
                lines.append(str(arg.renderable))
            if hasattr(arg, 'title') and arg.title is not None:
                lines.append(str(arg.title))
            lines.append(str(arg))
    for call in mock_print.call_args_list:
        for arg in call[0]:
            lines.append(str(arg))
    return "\n".join(lines)


@pytest.fixture
def clean_mock_data():
    """Fixture to ensure a clean state before each test scenario."""
    yield


@pytest.fixture
def clean_session():
    """Fixture to provide a clean structure for user session state."""
    return {
        'user_id': None,
        'username': None,
        'role': None,
        'cabang_id': None,
        'token': None
    }


# Sessions fixtures for all 8 roles
@pytest.fixture
def session_pemilik(clean_session):
    token = create_jwt_session(1, 'pemilik_user', 'pemilik', 1)
    clean_session.update({
        'user_id': 1,
        'username': 'pemilik_user',
        'role': 'pemilik',
        'cabang_id': 1,
        'token': token
    })
    return clean_session


@pytest.fixture
def session_kepala(clean_session):
    token = create_jwt_session(2, 'kepala_user', 'kepala_percetakan', 1)
    clean_session.update({
        'user_id': 2,
        'username': 'kepala_user',
        'role': 'kepala_percetakan',
        'cabang_id': 1,
        'token': token
    })
    return clean_session


@pytest.fixture
def session_kasir(clean_session):
    token = create_jwt_session(3, 'kasir_user', 'kasir', 1)
    clean_session.update({
        'user_id': 3,
        'username': 'kasir_user',
        'role': 'kasir',
        'cabang_id': 1,
        'token': token
    })
    return clean_session


@pytest.fixture
def session_desainer(clean_session):
    token = create_jwt_session(4, 'desainer_user', 'desainer', 1)
    clean_session.update({
        'user_id': 4,
        'username': 'desainer_user',
        'role': 'desainer',
        'cabang_id': 1,
        'token': token
    })
    return clean_session


@pytest.fixture
def session_produksi(clean_session):
    token = create_jwt_session(5, 'produksi_user', 'produksi_cetak', 1)
    clean_session.update({
        'user_id': 5,
        'username': 'produksi_user',
        'role': 'produksi_cetak',
        'cabang_id': 1,
        'token': token
    })
    return clean_session


@pytest.fixture
def session_fotocopy(clean_session):
    token = create_jwt_session(6, 'fotocopy_user', 'fotocopy_print', 1)
    clean_session.update({
        'user_id': 6,
        'username': 'fotocopy_user',
        'role': 'fotocopy_print',
        'cabang_id': 1,
        'token': token
    })
    return clean_session


@pytest.fixture
def session_gudang(clean_session):
    token = create_jwt_session(7, 'gudang_user', 'gudang', 1)
    clean_session.update({
        'user_id': 7,
        'username': 'gudang_user',
        'role': 'gudang',
        'cabang_id': 1,
        'token': token
    })
    return clean_session


@pytest.fixture
def session_pramuniaga(clean_session):
    token = create_jwt_session(8, 'pramuniaga_user', 'pramuniaga', 1)
    clean_session.update({
        'user_id': 8,
        'username': 'pramuniaga_user',
        'role': 'pramuniaga',
        'cabang_id': 1,
        'token': token
    })
    return clean_session


# =====================================================================
# A. POSITIVE SCENARIOS
# =====================================================================

@patch('cli.dashboard._console.print')
@patch('builtins.print')
@patch('cli.dashboard.query_dashboard_pemilik')
def test_dashboard_pemilik_sukses(mock_query, mock_print, mock_console, session_pemilik, clean_mock_data):
    """Verifikasi bahwa logika penyiapan data ringkasan harian pemilik berjalan sukses."""
    mock_data = {
        'total_pendapatan': Decimal('15000000.0000'),
        'total_pengeluaran': Decimal('5000000.0000'),
        'total_limbah': Decimal('500000.0000'),
        'status_transaksi': [
            {'status_pembayaran': 'LUNAS', 'jumlah': 10},
            {'status_pembayaran': 'BELUM LUNAS', 'jumlah': 5}
        ],
        'alert_bank': [
            {
                'tipe_bank': 'BRI',
                'setoran_bulanan': Decimal('2000000.0000'),
                'tanggal_jatuh_tempo': date.today() + timedelta(days=2),
                'sisa_hari': 2
            }
        ],
        'alert_supplier': [
            {
                'nama_supplier': 'Sentral ATK',
                'sisa_utang': Decimal('3000000.0000'),
                'tanggal_jatuh_tempo': date.today() + timedelta(days=1),
                'sisa_hari': 1
            }
        ]
    }
    mock_query.return_value = Result(True, mock_data, None)
    mock_conn = MagicMock()

    for has_rich in (True, False):
        mock_console.reset_mock()
        mock_print.reset_mock()
        with patch('cli.dashboard.HAS_RICH', has_rich):
            _render_dashboard_pemilik(session_pemilik, mock_conn, date.today().isoformat())

        printed = get_printed_text(mock_console, mock_print)

        assert "15,000,000.0000" in printed
        assert "5,000,000.0000" in printed
        assert "500,000.0000" in printed
        assert "9,500,000.0000" in printed  # Estimasi Laba Bersih = 15jt - 5jt - 0.5jt
        assert "BRI" in printed
        assert "Sentral ATK" in printed


@patch('cli.dashboard._console.print')
@patch('builtins.print')
@patch('cli.dashboard.query_dashboard_kepala')
def test_dashboard_kepala_percetakan_sukses(mock_query, mock_print, mock_console, session_kepala):
    """Verifikasi bahwa data dashboard kepala percetakan dirender dengan parameter yang terisi penuh."""
    mock_data = {
        'jumlah_hadir': 8,
        'total_staf': 10,
        'draf_pending': 3,
        'antrian': [
            {'status_antrian': 'Antri', 'jumlah': 2},
            {'status_antrian': 'Proses Desain', 'jumlah': 1}
        ]
    }
    mock_query.return_value = Result(True, mock_data, None)
    mock_conn = MagicMock()

    for has_rich in (True, False):
        mock_console.reset_mock()
        mock_print.reset_mock()
        with patch('cli.dashboard.HAS_RICH', has_rich):
            _render_dashboard_kepala(session_kepala, mock_conn, date.today().isoformat())

        printed = get_printed_text(mock_console, mock_print)

        assert "8 dari 10" in printed
        assert "3 draf pending" in printed
        assert "Antri" in printed
        assert "Proses Desain" in printed


@patch('cli.dashboard._console.print')
@patch('builtins.print')
@patch('cli.dashboard.query_dashboard_kasir')
def test_dashboard_kasir_sukses(mock_query, mock_print, mock_console, session_kasir):
    """Verifikasi dashboard kasir sukses menampilkan kas masuk, nota harian, dan alert PPOB."""
    mock_data = {
        'jumlah_nota': 15,
        'total_kas': Decimal('4500000.0000'),
        'jumlah_belum_lunas': 2,
        'saldo_ppob': [
            {'akun_tipe': 'Pulsa_Data', 'saldo_terakhir': Decimal('120000.0000')},  # < 150000 (warning)
            {'akun_tipe': 'Token_Tagihan', 'saldo_terakhir': Decimal('300000.0000')}
        ]
    }
    mock_query.return_value = Result(True, mock_data, None)
    mock_conn = MagicMock()

    for has_rich in (True, False):
        mock_console.reset_mock()
        mock_print.reset_mock()
        with patch('cli.dashboard.HAS_RICH', has_rich):
            _render_dashboard_kasir(session_kasir, mock_conn, date.today().isoformat())

        printed = get_printed_text(mock_console, mock_print)

        assert "15 nota" in printed
        assert "4,500,000.0000" in printed
        assert "2 nota" in printed
        assert "Pulsa & Data" in printed
        assert "⚠️" in printed or "Peringatan" in printed or "PERINGATAN" in printed


@patch('cli.dashboard._console.print')
@patch('builtins.print')
@patch('cli.dashboard.query_dashboard_operasional')
def test_dashboard_desainer_sukses(mock_query, mock_print, mock_console, session_desainer):
    """Verifikasi dashboard desainer sukses menampilkan antrian dan stok kritis."""
    mock_data = {
        'antrian': [
            {'status_antrian': 'Antri', 'jumlah': 5},
            {'status_antrian': 'Proses Desain', 'jumlah': 3}
        ],
        'stok_kritis': [
            {'nama_barang': 'Kertas A4', 'stok_saat_ini': Decimal('2.0000'), 'satuan_uom': 'Rim'}
        ]
    }
    mock_query.return_value = Result(True, mock_data, None)
    mock_conn = MagicMock()

    for has_rich in (True, False):
        mock_console.reset_mock()
        mock_print.reset_mock()
        with patch('cli.dashboard.HAS_RICH', has_rich):
            _render_dashboard_operasional(session_desainer, mock_conn)

        printed = get_printed_text(mock_console, mock_print)

        assert "desainer_user" in printed
        assert "Kertas A4" in printed
        assert "2" in printed  # tabulate / formatting representation
        assert "Proses Desain" in printed


@patch('cli.dashboard._console.print')
@patch('builtins.print')
@patch('cli.dashboard.query_dashboard_operasional')
def test_dashboard_produksi_cetak_sukses(mock_query, mock_print, mock_console, session_produksi):
    """Verifikasi dashboard produksi cetak sukses menampilkan antrian produksi."""
    mock_data = {
        'antrian': [
            {'status_antrian': 'Produksi', 'jumlah': 4}
        ],
        'stok_kritis': []
    }
    mock_query.return_value = Result(True, mock_data, None)
    mock_conn = MagicMock()

    for has_rich in (True, False):
        mock_console.reset_mock()
        mock_print.reset_mock()
        with patch('cli.dashboard.HAS_RICH', has_rich):
            _render_dashboard_operasional(session_produksi, mock_conn)

        printed = get_printed_text(mock_console, mock_print)

        assert "produksi_user" in printed
        assert "Produksi" in printed
        assert "aman" in printed.lower()


@patch('cli.dashboard._console.print')
@patch('builtins.print')
@patch('cli.dashboard.query_dashboard_fotocopy')
def test_dashboard_fotocopy_print_sukses(mock_query, mock_print, mock_console, session_fotocopy):
    """Verifikasi dashboard fotocopy & print menampilkan jumlah nota retail dan total kas masuk."""
    mock_data = {
        'jumlah_nota': 10,
        'total_kas': Decimal('250000.0000')
    }
    mock_query.return_value = Result(True, mock_data, None)
    mock_conn = MagicMock()

    for has_rich in (True, False):
        mock_console.reset_mock()
        mock_print.reset_mock()
        with patch('cli.dashboard.HAS_RICH', has_rich):
            _render_dashboard_fotocopy(session_fotocopy, mock_conn, date.today().isoformat())

        printed = get_printed_text(mock_console, mock_print)

        assert "fotocopy_user" in printed
        assert "10 nota" in printed
        assert "250,000.0000" in printed


@patch('cli.dashboard._console.print')
@patch('builtins.print')
@patch('cli.dashboard.query_dashboard_gudang')
def test_dashboard_gudang_sukses(mock_query, mock_print, mock_console, session_gudang):
    """Verifikasi dashboard gudang menampilkan data stock opname draft dan utang supplier."""
    mock_data = {
        'stok_kritis': [
            {'nama_barang': 'Tinta Hitam', 'stok_saat_ini': Decimal('1.5000'), 'satuan_uom': 'Botol'}
        ],
        'draf_pending': 4,
        'utang_supplier': [
            {
                'nama_supplier': 'Paper Indah',
                'sisa_utang': Decimal('1200000.0000'),
                'tanggal_jatuh_tempo': date.today() + timedelta(days=5)
            }
        ]
    }
    mock_query.return_value = Result(True, mock_data, None)
    mock_conn = MagicMock()

    for has_rich in (True, False):
        mock_console.reset_mock()
        mock_print.reset_mock()
        with patch('cli.dashboard.HAS_RICH', has_rich):
            _render_dashboard_gudang(session_gudang, mock_conn)

        printed = get_printed_text(mock_console, mock_print)

        assert "gudang_user" in printed
        assert "4 draf pending" in printed
        assert "Tinta Hitam" in printed
        assert "Paper Indah" in printed
        assert "1,200,000.0000" in printed


@patch('cli.dashboard._console.print')
@patch('builtins.print')
@patch('cli.dashboard.query_dashboard_pramuniaga')
def test_dashboard_teknisi_pramuniaga_sukses(mock_query, mock_print, mock_console, session_pramuniaga):
    """Verifikasi dashboard pramuniaga sukses menampilkan antrian awal ('Antri')."""
    mock_data = {
        'jumlah_antri': 6
    }
    mock_query.return_value = Result(True, mock_data, None)
    mock_conn = MagicMock()

    for has_rich in (True, False):
        mock_console.reset_mock()
        mock_print.reset_mock()
        with patch('cli.dashboard.HAS_RICH', has_rich):
            _render_dashboard_pramuniaga(session_pramuniaga, mock_conn)

        printed = get_printed_text(mock_console, mock_print)

        assert "pramuniaga_user" in printed
        assert "6 pekerjaan" in printed


# =====================================================================
# B. ZERO-STATE & ROUNDING
# =====================================================================

@patch('cli.dashboard._console.print')
@patch('builtins.print')
@patch('cli.dashboard.query_dashboard_pemilik')
def test_dashboard_transaksi_kosong(mock_query, mock_print, mock_console, session_pemilik):
    """Zero State: Verifikasi dashboard pemilik dengan 0 transaksi harian."""
    mock_data = {
        'total_pendapatan': Decimal('0.0000'),
        'total_pengeluaran': Decimal('0.0000'),
        'total_limbah': Decimal('0.0000'),
        'status_transaksi': [],
        'alert_bank': [],
        'alert_supplier': []
    }
    mock_query.return_value = Result(True, mock_data, None)
    mock_conn = MagicMock()

    for has_rich in (True, False):
        mock_console.reset_mock()
        mock_print.reset_mock()
        with patch('cli.dashboard.HAS_RICH', has_rich):
            _render_dashboard_pemilik(session_pemilik, mock_conn, date.today().isoformat())

        printed = get_printed_text(mock_console, mock_print)

        assert "Rp 0.0000" in printed or "0.0000" in printed


def test_dashboard_pembulatan_desimal_hpp():
    """Boundary/Rounding: Verifikasi pembulatan HPP / uang menggunakan ROUND_HALF_UP."""
    # Skenario pembulatan ke atas (0.00005 -> 0.0001)
    res_up = hitung_laba_bersih_harian(Decimal('100.00005'), Decimal('50.0000'), Decimal('10.0000'))
    assert res_up == Decimal('40.0001')

    # Skenario pembulatan ke bawah (0.00004 -> 0.0000)
    res_down = hitung_laba_bersih_harian(Decimal('100.00004'), Decimal('50.0000'), Decimal('10.0000'))
    assert res_down == Decimal('40.0000')


# =====================================================================
# C. NEGATIVE & EXCEPTION CASES
# =====================================================================

def test_dashboard_invalid_role(clean_session):
    """Negative: Verifikasi handling jika user menggunakan peran tidak sah."""
    # create_jwt_session dengan role 'anonim' (tidak ada di VALID_ROLES)
    token = create_jwt_session(99, 'guest_user', 'anonim', 1)
    clean_session.update({
        'user_id': 99,
        'username': 'guest_user',
        'role': 'anonim',
        'cabang_id': 1,
        'token': token
    })

    # validate_session_token harus mengembalikan error status ERR-SESSION-002
    res = validate_session_token(clean_session)
    assert res.is_success is False
    assert "ERR-SESSION-002" in res.error_msg

    # create_jwt_session memvalidasi input string kosong untuk role (melempar ValueError)
    with pytest.raises(ValueError):
        create_jwt_session(99, 'guest_user', '', 1)

    # Memanggil _render_summary_panels dengan role anonim
    mock_conn = MagicMock()
    with patch('cli.dashboard.get_db_connection', return_value=Result(True, mock_conn, None)), \
         patch('cli.dashboard._console.print') as mock_console, \
         patch('builtins.print') as mock_print:
        _render_summary_panels(clean_session)

        printed = get_printed_text(mock_console, mock_print)

        assert "Selamat bekerja! Jalankan tugas dengan aman dan teliti." in printed


@patch('cli.dashboard._console.print')
@patch('builtins.print')
def test_dashboard_database_mock_error(mock_print, mock_console, session_pemilik):
    """Exception: Verifikasi penanganan database error dari layer mock connection/fetch."""
    # Skenario 1: Gagal mendapatkan koneksi database
    with patch('cli.dashboard.get_db_connection', return_value=Result(False, None, "Connection timeout")):
        _render_summary_panels(session_pemilik)

    printed1 = get_printed_text(mock_console, mock_print)
    assert "ERR-DB-003" in printed1
    assert "Connection timeout" in printed1

    # Skenario 2: Query function mengembalikan status kegagalan (is_success=False)
    mock_conn = MagicMock()
    with patch('cli.dashboard.get_db_connection', return_value=Result(True, mock_conn, None)), \
         patch('cli.dashboard.query_dashboard_pemilik', return_value=Result(False, None, "Query timeout")):
        _render_summary_panels(session_pemilik)

    printed2 = get_printed_text(mock_console, mock_print)
    assert "ERR-DB-003" in printed2
    assert "Query timeout" in printed2
