"""
Nama Modul: test_audit_logger.py
Deskripsi: Unit testing untuk middleware/audit_logger.py.
Author: Antigravity AI
Tanggal: 2026-06-07
"""

import pytest
import json
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


def test_log_audit_trail_insert_success():
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.lastrowid = 42
    mock_db.cursor.return_value = mock_cursor

    res = log_audit_trail(
        pengguna_id=1,
        action_type='INSERT',
        target_table='barang',
        old_val=None,
        new_val={'id': 10, 'nama': 'Kertas A4'},
        cabang_id=1,
        db_connection=mock_db
    )

    assert res.is_success is True
    assert res.data == 42
    assert res.error_msg is None
    mock_cursor.execute.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_log_audit_trail_update_with_old_new_value():
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.lastrowid = 43
    mock_db.cursor.return_value = mock_cursor

    old_val = {'id': 10, 'harga': Decimal('5000')}
    new_val = {'id': 10, 'harga': Decimal('6000')}

    res = log_audit_trail(
        pengguna_id=2,
        action_type='UPDATE',
        target_table='barang',
        old_val=old_val,
        new_val=new_val,
        cabang_id=1,
        db_connection=mock_db
    )

    assert res.is_success is True
    assert res.data == 43
    args, kwargs = mock_cursor.execute.call_args
    query, params = args
    assert params[0] == 2
    assert params[1] == 'UPDATE'
    assert params[2] == 'barang'
    assert json.loads(params[3]) == {'id': 10, 'harga': 5000.0}
    assert json.loads(params[4]) == {'id': 10, 'harga': 6000.0}


def test_log_audit_trail_delete_old_value_only():
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    res = log_audit_trail(
        pengguna_id=1,
        action_type='DELETE',
        target_table='barang',
        old_val={'id': 5},
        new_val=None,
        cabang_id=1,
        db_connection=mock_db
    )

    assert res.is_success is True
    args, _ = mock_cursor.execute.call_args
    params = args[1]
    assert json.loads(params[3]) == {'id': 5}
    assert params[4] is None


def test_log_audit_trail_access_denied():
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    res = log_audit_trail(
        pengguna_id=3,
        action_type='ACCESS_DENIED',
        target_table='MENU-M4-002',
        old_val={'attempted_menu': 'MENU-M4-002', 'role': 'kasir'},
        new_val={'status': 'ILLEGAL_ACCESS_PREVENTED'},
        cabang_id=1,
        db_connection=mock_db
    )

    assert res.is_success is True
    args, _ = mock_cursor.execute.call_args
    params = args[1]
    assert params[1] == 'ACCESS_DENIED'
    assert params[2] == 'MENU-M4-002'


def test_log_audit_trail_invalid_action_type():
    mock_db = MagicMock()
    with pytest.raises(ValueError):
        log_audit_trail(
            pengguna_id=1,
            action_type='HACK',
            target_table='barang',
            old_val=None,
            new_val=None,
            cabang_id=1,
            db_connection=mock_db
        )


def test_log_audit_trail_db_error_handling():
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = Exception("MySQL error 1045")
    mock_db.cursor.return_value = mock_cursor

    res = log_audit_trail(
        pengguna_id=1,
        action_type='INSERT',
        target_table='barang',
        old_val=None,
        new_val=None,
        cabang_id=1,
        db_connection=mock_db
    )

    assert res.is_success is False
    assert "ERR-DB-002" in res.error_msg
    mock_cursor.close.assert_called_once()


def test_log_audit_trail_none_values():
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    res = log_audit_trail(
        pengguna_id=1,
        action_type='INSERT',
        target_table='barang',
        old_val=None,
        new_val=None,
        cabang_id=1,
        db_connection=mock_db
    )

    assert res.is_success is True
    args, _ = mock_cursor.execute.call_args
    params = args[1]
    assert params[3] is None
    assert params[4] is None


def test_log_audit_trail_decimal_serialization():
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    res = log_audit_trail(
        pengguna_id=1,
        action_type='INSERT',
        target_table='barang',
        old_val={'sisa_utang': Decimal('500000.0000')},
        new_val={'sisa_utang': Decimal('0.0000')},
        cabang_id=1,
        db_connection=mock_db
    )

    assert res.is_success is True
    args, _ = mock_cursor.execute.call_args
    params = args[1]
    assert json.loads(params[3]) == {'sisa_utang': 500000.0}
    assert json.loads(params[4]) == {'sisa_utang': 0.0}


def test_serialize_value_to_json_happy_path():
    data = {
        'id': 1,
        'nilai': Decimal('12345.6789'),
        'waktu': datetime(2026, 6, 7, 8, 30, 0),
        'tanggal': date(2026, 6, 7)
    }
    res = _serialize_value_to_json(data)
    parsed = json.loads(res)
    assert parsed['id'] == 1
    assert parsed['nilai'] == 12345.6789
    assert parsed['waktu'] == '2026-06-07T08:30:00'
    assert parsed['tanggal'] == '2026-06-07'


def test_serialize_value_to_json_none():
    assert _serialize_value_to_json(None) is None


def test_get_client_ip_returns_string():
    ip = get_client_ip()
    assert isinstance(ip, str)
    assert len(ip) > 0


def test_query_audit_logs_basic():
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
            'old_value': None,
            'new_value': '{"id": 1}',
            'ip_address': '127.0.0.1',
            'cabang_id': 1,
            'created_at': datetime(2026, 6, 7, 8, 0, 0),
            'updated_at': datetime(2026, 6, 7, 8, 0, 0)
        }
    ]

    res = query_audit_logs(mock_db, cabang_id=1)
    assert res.is_success is True
    assert len(res.data) == 1
    assert res.data[0]['new_value'] == {'id': 1}
    assert mock_cursor.close.called


def test_query_audit_logs_with_filters():
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []

    res = query_audit_logs(
        db_connection=mock_db,
        cabang_id=1,
        pengguna_id=2,
        action_type='UPDATE',
        target_table='barang',
        tanggal_mulai='2026-06-01',
        tanggal_akhir='2026-06-07',
        limit=50
    )

    assert res.is_success is True
    args, _ = mock_cursor.execute.call_args
    query, params = args
    assert "pengguna_id = %s" in query
    assert "action_type = %s" in query
    assert "target_table = %s" in query
    assert "action_timestamp >= %s" in query
    assert "action_timestamp <= %s" in query
    assert params == (1, 2, 'UPDATE', 'barang', '2026-06-01', '2026-06-07', 50)


def test_detect_fraud_anomalies_no_anomaly():
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []

    res = detect_fraud_anomalies(mock_db, cabang_id=1)
    assert res.is_success is True
    assert res.data['kas_anomalies'] == []
    assert res.data['retur_anomalies'] == []
    assert res.data['brute_force_anomalies'] == []


def test_purge_old_audit_logs_success():
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = (5,)

    with patch('middleware.audit_logger.log_audit_trail') as mock_log:
        mock_log.return_value = Result(True, 100, None)

        res = purge_old_audit_logs(mock_db, cabang_id=1, retention_months=12)
        assert res.is_success is True
        assert res.data['purged_count'] == 5
        mock_log.assert_called_once()
        assert mock_cursor.execute.call_count == 2
