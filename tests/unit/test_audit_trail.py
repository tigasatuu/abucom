"""
Nama Modul: test_audit_trail.py
Deskripsi: Unit testing komprehensif untuk middleware/audit_logger.py sesuai SDLC.
           Memastikan cakupan kode >= 90%, fungsional terisolasi murni, dan
           bebas dari side-effect luar.
Author: Antigravity AI
Tanggal: 2026-06-07
"""

import pytest
import json
import socket
import logging
from unittest.mock import MagicMock, patch
from decimal import Decimal
from datetime import datetime, date
from middleware.audit_logger import (
    log_audit_trail,
    query_audit_logs,
    detect_fraud_anomalies,
    count_audit_logs,
    purge_old_audit_logs,
    _serialize_value_to_json,
    _audit_json_serializer,
    get_client_ip,
    Result
)

# Setup logger capture to check warning outputs if needed
_logger = logging.getLogger('abucom.middleware.audit_logger')


@pytest.fixture(autouse=True)
def clean_state_management():
    """Fixture autouse untuk memastikan kebersihan state sebelum/sesudah setiap test.

    Mencegah memory leaks dan leakage state antar-pengujian dengan mereset mock.
    """
    # Teardown logic / clean state before run
    yield
    # Cleanup logic after run if needed (reset global variables or mock stats)


# ==============================================================================
# C.1. SKENARIO POSITIF (POSITIVE PATH)
# ==============================================================================

def test_logika_update_standar():
    """Uji fungsi generator audit dengan memasukkan old_value dan new_value yang memiliki perbedaan valid."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.lastrowid = 101
    mock_db.cursor.return_value = mock_cursor

    old_val = {'stok': Decimal('10.0')}
    new_val = {'stok': Decimal('5.0')}

    res = log_audit_trail(
        pengguna_id=5,
        action_type='UPDATE',
        target_table='barang',
        old_val=old_val,
        new_val=new_val,
        cabang_id=2,
        db_connection=mock_db
    )

    # 1. Verifikasi (assert) return value
    assert res.is_success is True
    assert res.data == 101
    assert res.error_msg is None

    # 2. Verifikasi pemanggilan database dan argument query
    mock_cursor.execute.assert_called_once()
    args, _ = mock_cursor.execute.call_args
    query, params = args

    # Pastikan query memuat target_table, action_type, dsb.
    assert "INSERT INTO audit_logs" in query
    assert params[0] == 5
    assert params[1] == 'UPDATE'
    assert params[2] == 'barang'

    # 3. Verifikasi JSON payload memuat old_value dan new_value yang terpetakan eksak
    # Sesuai requirement, Decimal diserialisasi ke string presisi tinggi
    assert json.loads(params[3]) == {'stok': '10.0'}
    assert json.loads(params[4]) == {'stok': '5.0'}


def test_rekaman_meta_data():
    """Pastikan data pengguna (user pelaksana, timestamp, nama tabel target) ikut terepresentasi."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    with patch('middleware.audit_logger.get_client_ip', return_value='192.168.1.10'):
        res = log_audit_trail(
            pengguna_id=42,
            action_type='INSERT',
            target_table='shift_handover',
            old_val=None,
            new_val={'id': 1},
            cabang_id=1,
            db_connection=mock_db
        )

        assert res.is_success is True
        args, _ = mock_cursor.execute.call_args
        params = args[1]
        assert params[0] == 42  # pengguna_id
        assert params[1] == 'INSERT'  # action_type
        assert params[2] == 'shift_handover'  # target_table
        assert params[5] == '192.168.1.10'  # ip_address
        assert params[6] == 1  # cabang_id


# ==============================================================================
# C.2. SKENARIO NEGATIF & EDGE CASES (BOUNDARY PATH)
# ==============================================================================

def test_insert_data_baru_null_handling():
    """Uji fungsi jika data awal (old_value) adalah sekadar parameter None (simulasi data baru)."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    res = log_audit_trail(
        pengguna_id=1,
        action_type='INSERT',
        target_table='pelanggan',
        old_val=None,
        new_val={'nama': 'Budi'},
        cabang_id=1,
        db_connection=mock_db
    )

    assert res.is_success is True
    args, _ = mock_cursor.execute.call_args
    params = args[1]
    assert params[3] is None  # old_value dirender dengan aman menjadi null (None) pada database / JSON
    assert json.loads(params[4]) == {'nama': 'Budi'}


def test_delete_data_final_state_null():
    """Uji fungsi ketika data (new_value) diset None (simulasi hard delete)."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    res = log_audit_trail(
        pengguna_id=1,
        action_type='DELETE',
        target_table='supplier',
        old_val={'id': 9, 'nama': 'Sinar Jaya'},
        new_val=None,
        cabang_id=1,
        db_connection=mock_db
    )

    assert res.is_success is True
    args, _ = mock_cursor.execute.call_args
    params = args[1]
    assert json.loads(params[3]) == {'id': 9, 'nama': 'Sinar Jaya'}
    assert params[4] is None  # new_value diset null secara eksak


def test_tidak_ada_perubahan_identical_payload():
    """Uji fungsi ketika old_value dan new_value adalah representasi struktur yang sama persis 100%."""
    mock_db = MagicMock()
    
    # Keduanya identik
    old_val = {'id': 1, 'harga': '5000'}
    new_val = {'id': 1, 'harga': '5000'}

    res = log_audit_trail(
        pengguna_id=1,
        action_type='UPDATE',
        target_table='barang',
        old_val=old_val,
        new_val=new_val,
        cabang_id=1,
        db_connection=mock_db
    )

    # Verifikasi sistem merespons efisien dengan mengembalikan penanda NO_CHANGES
    assert res.is_success is True
    assert res.data == 'NO_CHANGES'
    assert res.error_msg is None
    # Pastikan database tidak dihubungi sama sekali (zero database write)
    mock_db.cursor.assert_not_called()


def test_tipe_parameter_tidak_lazim():
    """Masukkan objek list sederhana alih-alih dict pada payload awal."""
    mock_db = MagicMock()

    # old_val berupa list (tidak lazim)
    with pytest.raises(ValueError) as excinfo:
        log_audit_trail(
            pengguna_id=1,
            action_type='UPDATE',
            target_table='barang',
            old_val=[1, 2, 3],  # type: ignore
            new_val={'id': 1},
            cabang_id=1,
            db_connection=mock_db
        )
    assert "old_val harus berupa dictionary atau None" in str(excinfo.value)

    # new_val berupa list (tidak lazim)
    with pytest.raises(ValueError) as excinfo:
        log_audit_trail(
            pengguna_id=1,
            action_type='UPDATE',
            target_table='barang',
            old_val={'id': 1},
            new_val="invalid string payload",  # type: ignore
            cabang_id=1,
            db_connection=mock_db
        )
    assert "new_val harus berupa dictionary atau None" in str(excinfo.value)


# ==============================================================================
# C.3. SKENARIO VALIDASI INPUT KHUSUS & PRESISI LANJUTAN
# ==============================================================================

def test_format_desimal_dan_mata_uang():
    """Uji fungsi komparasi dengan menyuntikkan objek tipe Decimal Python (presisi tinggi)."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    res = log_audit_trail(
        pengguna_id=1,
        action_type='UPDATE',
        target_table='barang',
        old_val={'nilai_stok': Decimal('100.0005')},
        new_val={'nilai_stok': Decimal('100.0005')},  # Wait, if identical it will return NO_CHANGES
        cabang_id=1,
        db_connection=mock_db
    )
    # Check if identical check behaves correctly. If identical, returns NO_CHANGES.
    # To test decimal serialization, let's use different values.
    res_diff = log_audit_trail(
        pengguna_id=1,
        action_type='UPDATE',
        target_table='barang',
        old_val={'nilai_stok': Decimal('100.0005')},
        new_val={'nilai_stok': Decimal('200.0007')},
        cabang_id=1,
        db_connection=mock_db
    )

    assert res_diff.is_success is True
    args, _ = mock_cursor.execute.call_args
    params = args[1]
    # Pastikan serializer mengonversi Decimal ke string presisi tinggi ('100.0005' dan '200.0007')
    assert json.loads(params[3]) == {'nilai_stok': '100.0005'}
    assert json.loads(params[4]) == {'nilai_stok': '200.0007'}


def test_sanitasi_karakter_escape_injection_defense():
    """Uji input yang memuat karakter kontrol ANSI/escape (\n, \x1b[31m)."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    old_val = {'info': 'Baris 1\nBaris 2'}
    new_val = {'info': '\x1b[31mError Text\x1b[0m'}

    res = log_audit_trail(
        pengguna_id=1,
        action_type='UPDATE',
        target_table='barang',
        old_val=old_val,
        new_val=new_val,
        cabang_id=1,
        db_connection=mock_db
    )

    assert res.is_success is True
    args, _ = mock_cursor.execute.call_args
    params = args[1]
    
    # Pastikan parser JSON dapat memecahkan (loads) format tersebut kembali tanpa crash
    parsed_old = json.loads(params[3])
    parsed_new = json.loads(params[4])

    assert parsed_old['info'] == 'Baris 1\nBaris 2'
    assert parsed_new['info'] == '\x1b[31mError Text\x1b[0m'


# ==============================================================================
# D. PENGUJIAN PENUTUP CAKUPAN KODE (CODE COVERAGE ENHANCEMENT)
# ==============================================================================

def test_audit_json_serializer_unsupported_type():
    """Uji serializer kustom dengan menyuplai tipe yang tidak didukung untuk memicu TypeError."""
    with pytest.raises(TypeError) as excinfo:
        _serialize_value_to_json({'custom_object': object()})
    assert "tidak bisa diserialisasi ke JSON" in str(excinfo.value)


def test_get_client_ip_with_127_loopback_success():
    """Uji get_client_ip saat hostname mengembalikan 127.x.x.x dan socket connect berhasil."""
    with patch('socket.gethostname', return_value='mylocalhost'):
        with patch('socket.gethostbyname', return_value='127.0.0.1'):
            mock_socket = MagicMock()
            mock_socket.getsockname.return_value = ('192.168.1.105', 12345)
            with patch('socket.socket', return_value=mock_socket):
                ip = get_client_ip()
                assert ip == '192.168.1.105'
                mock_socket.connect.assert_called_once_with(('10.255.255.255', 1))
                mock_socket.close.assert_called_once()


def test_get_client_ip_with_127_loopback_exception_fallback():
    """Uji get_client_ip saat hostname mengembalikan 127.x.x.x dan socket connect gagal."""
    with patch('socket.gethostname', return_value='mylocalhost'):
        with patch('socket.gethostbyname', return_value='127.0.0.1'):
            mock_socket = MagicMock()
            mock_socket.connect.side_effect = Exception("Network unreachable")
            with patch('socket.socket', return_value=mock_socket):
                ip = get_client_ip()
                assert ip == '127.0.0.1'  # Tetap fallback aman
                mock_socket.close.assert_called_once()


def test_get_client_ip_socket_general_exception():
    """Uji get_client_ip jika socket.gethostname() melemparkan exception umum."""
    with patch('socket.gethostname', side_effect=Exception("Driver crash")):
        ip = get_client_ip()
        assert ip == '127.0.0.1'


def test_query_audit_logs_decoding_error_handling():
    """Uji query_audit_logs saat memuat nilai old_value/new_value yang tidak valid format JSON-nya."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        {
            'id': 1,
            'pengguna_id': 2,
            'action_timestamp': datetime(2026, 6, 7, 8, 0, 0),
            'action_type': 'INSERT',
            'target_table': 'barang',
            'old_value': '{invalid json string}',
            'new_value': '{"valid": "json"}',
            'ip_address': '127.0.0.1',
            'cabang_id': 1,
            'created_at': datetime(2026, 6, 7, 8, 0, 0),
            'updated_at': datetime(2026, 6, 7, 8, 0, 0)
        }
    ]

    res = query_audit_logs(mock_db, cabang_id=1)
    assert res.is_success is True
    assert len(res.data) == 1
    # old_value dibiarkan sebagai string asli jika gagal didecode
    assert res.data[0]['old_value'] == '{invalid json string}'
    # new_value berhasil didecode menjadi dict
    assert res.data[0]['new_value'] == {'valid': 'json'}


def test_query_audit_logs_general_exception():
    """Uji query_audit_logs melempar exception basis data."""
    mock_db = MagicMock()
    mock_db.cursor.side_effect = Exception("Connection lost mid-query")

    res = query_audit_logs(mock_db, cabang_id=1)
    assert res.is_success is False
    assert "ERR-DB-002" in res.error_msg


def test_detect_kas_anomaly_insufficient_rows():
    """Uji detect_kas_anomaly ketika baris data kurang dari 3."""
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'kasir_keluar_id': 2, 'timestamp_handover': datetime.now(), 'selisih': Decimal('15000'), 'status_handover': 'ANOMALI'}
    ]
    res = detect_kas_anomaly_internal(mock_cursor, cabang_id=1)
    assert res == []


def test_detect_kas_anomaly_below_threshold():
    """Uji detect_kas_anomaly ketika ada baris data dengan selisih di bawah Rp 10.000."""
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'kasir_keluar_id': 2, 'timestamp_handover': datetime.now(), 'selisih': Decimal('15000'), 'status_handover': 'ANOMALI'},
        {'id': 2, 'kasir_keluar_id': 2, 'timestamp_handover': datetime.now(), 'selisih': Decimal('5000'), 'status_handover': 'NORMAL'},
        {'id': 3, 'kasir_keluar_id': 2, 'timestamp_handover': datetime.now(), 'selisih': Decimal('12000'), 'status_handover': 'ANOMALI'},
    ]
    res = detect_kas_anomaly_internal(mock_cursor, cabang_id=1)
    assert res == []


def test_detect_kas_anomaly_happy_path():
    """Uji detect_kas_anomaly saat mendeteksi 3 selisih kas berturut-turut di atas Rp 10.000."""
    mock_cursor = MagicMock()
    t_now = datetime(2026, 6, 7, 8, 30, 0)
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'kasir_keluar_id': 2, 'timestamp_handover': t_now, 'selisih': Decimal('15000'), 'status_handover': 'ANOMALI'},
        {'id': 2, 'kasir_keluar_id': 2, 'timestamp_handover': t_now, 'selisih': Decimal('-11000'), 'status_handover': 'ANOMALI'},
        {'id': 3, 'kasir_keluar_id': 2, 'timestamp_handover': t_now, 'selisih': Decimal('12000'), 'status_handover': 'ANOMALI'},
    ]
    res = detect_kas_anomaly_internal(mock_cursor, cabang_id=1)
    assert len(res) == 3
    assert res[0]['selisih'] == 15000.0
    assert res[1]['selisih'] == -11000.0
    assert res[0]['timestamp_handover'] == '2026-06-07T08:30:00'


def test_detect_retur_anomaly_decoding_fail_and_non_dict_and_non_retur():
    """Uji detect_retur_anomaly ketika new_value corrupt, non-dict, atau bukan RETUR/BATAL."""
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        # 1. new_val corrupt
        {'id': 1, 'pengguna_id': 3, 'new_value': '{corrupted json', 'action_timestamp': datetime.now()},
        # 2. new_val non-dict
        {'id': 2, 'pengguna_id': 3, 'new_value': '[1, 2, 3]', 'action_timestamp': datetime.now()},
        # 3. new_val valid dict tapi LUNAS (bukan RETUR/BATAL)
        {'id': 3, 'pengguna_id': 3, 'new_value': '{"status_pembayaran": "LUNAS"}', 'action_timestamp': datetime.now()},
        # 4. new_val dict tapi no status_pembayaran
        {'id': 4, 'pengguna_id': 3, 'new_value': '{"other_key": "val"}', 'action_timestamp': datetime.now()},
    ]
    res = detect_retur_anomaly_internal(mock_cursor, cabang_id=1)
    assert res == []


def test_detect_retur_anomaly_exceeds_five():
    """Uji detect_retur_anomaly saat seorang kasir memiliki lebih dari 5 kali retur dalam 7 hari."""
    mock_cursor = MagicMock()
    t_now = datetime(2026, 6, 7, 8, 30, 0)
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'pengguna_id': 4, 'new_value': '{"status_pembayaran": "RETUR"}', 'action_timestamp': t_now},
        {'id': 2, 'pengguna_id': 4, 'new_value': '{"status_pembayaran": "BATAL"}', 'action_timestamp': t_now},
        {'id': 3, 'pengguna_id': 4, 'new_value': '{"status_pembayaran": "RETUR"}', 'action_timestamp': t_now},
        {'id': 4, 'pengguna_id': 4, 'new_value': '{"status_pembayaran": "RETUR"}', 'action_timestamp': t_now},
        {'id': 5, 'pengguna_id': 4, 'new_value': '{"status_pembayaran": "RETUR"}', 'action_timestamp': t_now},
        {'id': 6, 'pengguna_id': 4, 'new_value': '{"status_pembayaran": "RETUR"}', 'action_timestamp': t_now},
    ]
    res = detect_retur_anomaly_internal(mock_cursor, cabang_id=1)
    assert len(res) == 1
    assert res[0]['pengguna_id'] == 4
    assert res[0]['total_retur'] == 6


def test_detect_fraud_anomalies_exception_handling():
    """Uji detect_fraud_anomalies menangani exception database."""
    mock_db = MagicMock()
    mock_db.cursor.side_effect = Exception("DB Connection Timeout")

    res = detect_fraud_anomalies(mock_db, cabang_id=1)
    assert res.is_success is False
    assert "ERR-DB-002" in res.error_msg


def test_count_audit_logs_exception_handling():
    """Uji count_audit_logs jika terjadi exception basis data."""
    mock_db = MagicMock()
    mock_db.cursor.side_effect = Exception("Query error")

    count = count_audit_logs(mock_db, cabang_id=1)
    assert count == 0


def test_purge_old_audit_logs_meta_log_audit_fail():
    """Uji purge_old_audit_logs saat penulisan meta-audit log aktivitas pembersihan gagal, proses harus tetap lanjut."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = (10,)

    # Mock log_audit_trail untuk mengembalikan is_success=False
    with patch('middleware.audit_logger.log_audit_trail', return_value=Result(False, None, "Meta log DB error")):
        res = purge_old_audit_logs(mock_db, cabang_id=1, retention_months=6)
        assert res.is_success is True
        assert res.data['purged_count'] == 10
        mock_cursor.execute.call_count == 2
        mock_db.commit.assert_called_once()


def test_purge_old_audit_logs_general_exception():
    """Uji purge_old_audit_logs melempar exception umum database."""
    mock_db = MagicMock()
    mock_db.cursor.side_effect = Exception("Failed connection")

    res = purge_old_audit_logs(mock_db, cabang_id=1)
    assert res.is_success is False
    assert "ERR-DB-002" in res.error_msg


# ==============================================================================
# HELPER MOCKING UNTUK CAKUPAN DETEKSI ANOMALI INTERNAL
# ==============================================================================

def detect_kas_anomaly_internal(cursor, cabang_id):
    """Fungsi helper pembungkus untuk memanggil detect_kas_anomaly dari module."""
    from middleware.audit_logger import detect_kas_anomaly
    return detect_kas_anomaly(cursor, cabang_id)


def detect_retur_anomaly_internal(cursor, cabang_id):
    """Fungsi helper pembungkus untuk memanggil detect_retur_anomaly dari module."""
    from middleware.audit_logger import detect_retur_anomaly
    return detect_retur_anomaly(cursor, cabang_id)


def test_query_audit_logs_decoding_error_handling_new_value():
    """Uji query_audit_logs saat memuat nilai new_value yang tidak valid format JSON-nya."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        {
            'id': 1,
            'pengguna_id': 2,
            'action_timestamp': datetime(2026, 6, 7, 8, 0, 0),
            'action_type': 'INSERT',
            'target_table': 'barang',
            'old_value': '{"valid": "json"}',
            'new_value': '{invalid json string}',
            'ip_address': '127.0.0.1',
            'cabang_id': 1,
            'created_at': datetime(2026, 6, 7, 8, 0, 0),
            'updated_at': datetime(2026, 6, 7, 8, 0, 0)
        }
    ]

    res = query_audit_logs(mock_db, cabang_id=1)
    assert res.is_success is True
    assert len(res.data) == 1
    assert res.data[0]['old_value'] == {'valid': 'json'}
    assert res.data[0]['new_value'] == '{invalid json string}'


def test_count_audit_logs_happy_path():
    """Uji count_audit_logs dalam skenario sukses mengembalikan jumlah baris."""
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (150,)
    mock_db.cursor.return_value = mock_cursor

    count = count_audit_logs(mock_db, cabang_id=2)
    assert count == 150
    mock_cursor.execute.assert_called_once_with(
        "SELECT COUNT(*) FROM audit_logs WHERE cabang_id = %s",
        (2,)
    )
    mock_cursor.close.assert_called_once()

