"""
Nama Modul: audit_logger.py
Deskripsi: Middleware pencatatan audit trail terstruktur format JSON ke tabel
             audit_logs MySQL. Merekam old_value dan new_value untuk setiap
             modifikasi data sensitif (Modul M.7).
Author: Antigravity AI
Tanggal: 2026-06-07
"""

import json
import logging
import socket
import platform
from collections import namedtuple
from decimal import Decimal
from datetime import datetime, date
from typing import Any

_logger = logging.getLogger('abucom.middleware.audit_logger')

VALID_ACTION_TYPES = (
    'INSERT', 'UPDATE', 'DELETE', 'ACCESS_DENIED',
    'LOGIN_SUCCESS', 'LOGIN_FAILED', 'LOGOUT', 'ACCOUNT_LOCKOUT'
)

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


def _audit_json_serializer(obj: Any) -> Any:
    """Serializer kustom untuk json.dumps() agar mendukung Decimal dan datetime/date.

    Args:
        obj (Any): Objek yang akan diserialisasi.

    Returns:
        Any: Representasi yang kompatibel dengan JSON.

    Raises:
        TypeError: Jika tipe objek tidak diserialisasi.
    """
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Tipe {type(obj)} tidak bisa diserialisasi ke JSON")


def _serialize_value_to_json(value: dict | None) -> str | None:
    """Mengonversi dictionary Python ke string JSON.

    Args:
        value (dict | None): Dictionary data yang akan dikonversi.

    Returns:
        str | None: String JSON hasil konversi atau None jika input None.
    """
    if value is None:
        return None
    return json.dumps(value, default=_audit_json_serializer)


def get_client_ip() -> str:
    """Mengambil IP address terminal aktif secara lintas-OS.

    Returns:
        str: Alamat IP client.
    """
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        if ip_address.startswith('127.'):
            # Fallback untuk mendapatkan LAN IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                s.connect(('10.255.255.255', 1))
                ip_address = s.getsockname()[0]
            except Exception:
                pass
            finally:
                s.close()
        return ip_address
    except Exception:
        return '127.0.0.1'


def log_audit_trail(
    pengguna_id: int,
    action_type: str,
    target_table: str,
    old_val: dict | None,
    new_val: dict | None,
    cabang_id: int,
    db_connection: Any
) -> Result:
    """Menyimpan berkas log audit terstruktur JSON ke MySQL.

    Args:
        pengguna_id (int): ID pengguna yang melakukan perubahan.
        action_type (str): Jenis operasi ('INSERT', 'UPDATE', 'DELETE', 'ACCESS_DENIED',
                           'LOGIN_SUCCESS', 'LOGIN_FAILED', 'LOGOUT', 'ACCOUNT_LOCKOUT').
        target_table (str): Nama tabel database yang diubah atau menu yang diakses.
        old_val (dict | None): Keadaan data sebelum operasi (JSON).
        new_val (dict | None): Keadaan data setelah operasi (JSON).
        cabang_id (int): ID cabang tempat modifikasi dilakukan.
        db_connection: Koneksi database aktif.

    Returns:
        Result: is_success=True dengan data=lastrowid jika berhasil,
                is_success=False dengan error_msg jika gagal.

    Raises:
        ValueError: Jika action_type tidak valid.

    Example:
        >>> conn = get_db_connection().data
        >>> log_audit_trail(1, 'UPDATE', 'transaksi', {'id': 1}, {'id': 1, 'status': 'LUNAS'}, 1, conn)
        Result(is_success=True, data=123, error_msg=None)
    """
    if action_type not in VALID_ACTION_TYPES:
        raise ValueError(f"Action type '{action_type}' tidak valid.")

    cursor = None
    try:
        old_val_json = _serialize_value_to_json(old_val)
        new_val_json = _serialize_value_to_json(new_val)
        ip_address = get_client_ip()

        query = (
            "INSERT INTO audit_logs (pengguna_id, action_type, target_table, old_value, new_value, ip_address, cabang_id) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        cursor = db_connection.cursor()
        cursor.execute(query, (pengguna_id, action_type, target_table, old_val_json, new_val_json, ip_address, cabang_id))
        db_connection.commit()
        last_id = cursor.lastrowid
        _logger.info(f"Audit trail berhasil dicatat: {action_type} pada tabel/menu {target_table}")
        return Result(True, last_id, None)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mencatat audit trail ke database: {str(e)}"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_audit_logs(
    db_connection: Any,
    cabang_id: int,
    pengguna_id: int | None = None,
    action_type: str | None = None,
    target_table: str | None = None,
    tanggal_mulai: str | None = None,
    tanggal_akhir: str | None = None,
    limit: int = 100
) -> Result:
    """Membaca data log audit dengan filter granular.

    (Ref: Security Design Bab 7.5 & Module Structure Bab 7.4)

    Args:
        db_connection: Koneksi database aktif.
        cabang_id (int): ID cabang yang difilter.
        pengguna_id (int | None): ID pengguna pelaksana.
        action_type (str | None): Tipe aksi.
        target_table (str | None): Nama tabel/menu target.
        tanggal_mulai (str | None): Rentang tanggal mulai (YYYY-MM-DD atau YYYY-MM-DD HH:MM:SS).
        tanggal_akhir (str | None): Rentang tanggal akhir (YYYY-MM-DD atau YYYY-MM-DD HH:MM:SS).
        limit (int): Batas baris hasil query.

    Returns:
        Result: is_success=True dengan list[dict] data log jika berhasil,
                is_success=False dengan error_msg jika gagal.
    """
    cursor = None
    try:
        query = (
            "SELECT id, pengguna_id, action_timestamp, action_type, target_table, "
            "old_value, new_value, ip_address, cabang_id, created_at, updated_at "
            "FROM audit_logs WHERE cabang_id = %s"
        )
        params = [cabang_id]

        if pengguna_id is not None:
            query += " AND pengguna_id = %s"
            params.append(pengguna_id)

        if action_type is not None:
            query += " AND action_type = %s"
            params.append(action_type)

        if target_table is not None:
            query += " AND target_table = %s"
            params.append(target_table)

        if tanggal_mulai is not None:
            query += " AND action_timestamp >= %s"
            params.append(tanggal_mulai)

        if tanggal_akhir is not None:
            query += " AND action_timestamp <= %s"
            params.append(tanggal_akhir)

        query += " ORDER BY action_timestamp DESC LIMIT %s"
        params.append(limit)

        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(query, tuple(params))
        data = cursor.fetchall()

        for row in data:
            if isinstance(row.get('old_value'), str):
                try:
                    row['old_value'] = json.loads(row['old_value'])
                except Exception:
                    pass
            if isinstance(row.get('new_value'), str):
                try:
                    row['new_value'] = json.loads(row['new_value'])
                except Exception:
                    pass

        return Result(True, data, None)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal melakukan query audit logs: {str(e)}"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def detect_kas_anomaly(cursor: Any, cabang_id: int) -> list[dict]:
    """Mendeteksi anomali selisih kas rekonsiliasi: 3 shift berturut-turut selisih > Rp 10.000.

    Args:
        cursor: Objek cursor database.
        cabang_id (int): ID cabang yang difilter.

    Returns:
        list[dict]: Daftar detail anomali selisih kas.
    """
    query = (
        "SELECT id, kasir_keluar_id, timestamp_handover, selisih, status_handover "
        "FROM shift_handover WHERE cabang_id = %s "
        "ORDER BY timestamp_handover DESC LIMIT 3"
    )
    cursor.execute(query, (cabang_id,))
    rows = cursor.fetchall()
    if len(rows) == 3 and all(abs(Decimal(str(r['selisih']))) > Decimal('10000') for r in rows):
        return [
            {
                'id': r['id'],
                'kasir_keluar_id': r['kasir_keluar_id'],
                'timestamp_handover': r['timestamp_handover'].isoformat() if hasattr(r['timestamp_handover'], 'isoformat') else str(r['timestamp_handover']),
                'selisih': float(r['selisih']),
                'status_handover': r['status_handover']
            }
            for r in rows
        ]
    return []


def detect_retur_anomaly(cursor: Any, cabang_id: int) -> list[dict]:
    """Mendeteksi frekuensi retur abnormal: kasir dengan eskalasi retur > 5 kali dalam 7 hari.

    Args:
        cursor: Objek cursor database.
        cabang_id (int): ID cabang yang difilter.

    Returns:
        list[dict]: Daftar detail anomali retur kasir.
    """
    query = (
        "SELECT id, pengguna_id, new_value, action_timestamp "
        "FROM audit_logs "
        "WHERE action_type = 'UPDATE' "
        "  AND target_table = 'transaksi' "
        "  AND cabang_id = %s "
        "  AND action_timestamp >= DATE_SUB(NOW(), INTERVAL 7 DAY)"
    )
    cursor.execute(query, (cabang_id,))
    rows = cursor.fetchall()

    kasir_retur_counts = {}
    kasir_details = {}
    for r in rows:
        new_val = r['new_value']
        if isinstance(new_val, str):
            try:
                new_val = json.loads(new_val)
            except Exception:
                continue

        if isinstance(new_val, dict) and new_val.get('status_pembayaran') in ('RETUR', 'BATAL'):
            p_id = r['pengguna_id']
            kasir_retur_counts[p_id] = kasir_retur_counts.get(p_id, 0) + 1
            if p_id not in kasir_details:
                kasir_details[p_id] = []
            kasir_details[p_id].append({
                'log_id': r['id'],
                'action_timestamp': r['action_timestamp'].isoformat() if hasattr(r['action_timestamp'], 'isoformat') else str(r['action_timestamp']),
                'new_value': new_val
            })

    anomalies = []
    for p_id, count in kasir_retur_counts.items():
        if count > 5:
            anomalies.append({
                'pengguna_id': p_id,
                'total_retur': count,
                'logs': kasir_details[p_id]
            })
    return anomalies


def detect_login_brute_force(cursor: Any) -> list[dict]:
    """Mendeteksi brute force login: > 10 kali gagal login dari 1 IP dalam 1 jam.

    Args:
        cursor: Objek cursor database.

    Returns:
        list[dict]: Daftar detail anomali brute force login.
    """
    query = (
        "SELECT ip_address, COUNT(*) as failed_count "
        "FROM audit_logs "
        "WHERE action_type = 'LOGIN_FAILED' "
        "  AND action_timestamp >= DATE_SUB(NOW(), INTERVAL 1 HOUR) "
        "GROUP BY ip_address "
        "HAVING failed_count > 10"
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    return [
        {
            'ip_address': r['ip_address'],
            'failed_count': r['failed_count']
        }
        for r in rows
    ]


def detect_fraud_anomalies(db_connection: Any, cabang_id: int) -> Result:
    """Mendeteksi 3 pola anomali fraud dari database.

    (Ref: Security Design Bab 7.4)

    Args:
        db_connection: Koneksi database aktif.
        cabang_id (int): ID cabang yang difilter.

    Returns:
        Result: is_success=True dengan dictionary berisi detail anomali,
                is_success=False dengan error_msg jika gagal.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        kas_anomalies = detect_kas_anomaly(cursor, cabang_id)
        retur_anomalies = detect_retur_anomaly(cursor, cabang_id)
        brute_force_anomalies = detect_login_brute_force(cursor)

        anomalies = {
            'kas_anomalies': kas_anomalies,
            'retur_anomalies': retur_anomalies,
            'brute_force_anomalies': brute_force_anomalies
        }
        return Result(True, anomalies, None)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mendeteksi anomali fraud: {str(e)}"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def count_audit_logs(db_connection: Any, cabang_id: int) -> int:
    """Menghitung total baris audit_logs per cabang.

    Args:
        db_connection: Koneksi database aktif.
        cabang_id (int): ID cabang.

    Returns:
        int: Jumlah baris audit logs.
    """
    cursor = None
    try:
        cursor = db_connection.cursor()
        query = "SELECT COUNT(*) FROM audit_logs WHERE cabang_id = %s"
        cursor.execute(query, (cabang_id,))
        row = cursor.fetchone()
        return row[0] if row else 0
    except Exception as e:
        _logger.error(f"Gagal menghitung audit logs: {str(e)}")
        return 0
    finally:
        if cursor:
            cursor.close()


def purge_old_audit_logs(
    db_connection: Any,
    cabang_id: int,
    retention_months: int = 12
) -> Result:
    """Membersihkan log audit lama yang berumur lebih dari retention_months bulan.

    (Ref: Security Design Bab 7.5)

    Args:
        db_connection: Koneksi database aktif.
        cabang_id (int): ID cabang yang dibersihkan.
        retention_months (int): Masa retensi log dalam bulan (default 12 bulan).

    Returns:
        Result: is_success=True dengan dict berisi purged_count jika berhasil,
                is_success=False dengan error_msg jika gagal.
    """
    cursor = None
    try:
        cursor = db_connection.cursor()
        count_query = (
            "SELECT COUNT(*) FROM audit_logs "
            "WHERE cabang_id = %s "
            "  AND action_timestamp < DATE_SUB(NOW(), INTERVAL %s MONTH)"
        )
        cursor.execute(count_query, (cabang_id, retention_months))
        to_delete_count = cursor.fetchone()[0]

        old_val = {'retention_months': retention_months, 'status': 'ACTIVE'}
        new_val = {'purged_count': to_delete_count, 'status': 'PURGED'}

        meta_res = log_audit_trail(
            pengguna_id=1,
            action_type='DELETE',
            target_table='audit_logs',
            old_val=old_val,
            new_val=new_val,
            cabang_id=cabang_id,
            db_connection=db_connection
        )
        if not meta_res.is_success:
            _logger.warning(f"Gagal mencatat meta-audit untuk aktivitas purging: {meta_res.error_msg}")

        delete_query = (
            "DELETE FROM audit_logs "
            "WHERE cabang_id = %s "
            "  AND action_timestamp < DATE_SUB(NOW(), INTERVAL %s MONTH)"
        )
        cursor.execute(delete_query, (cabang_id, retention_months))
        db_connection.commit()

        _logger.info(f"Purging audit logs berhasil: menghapus {to_delete_count} baris logs lama.")
        return Result(True, {'purged_count': to_delete_count}, None)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal membersihkan logs lama: {str(e)}"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()
