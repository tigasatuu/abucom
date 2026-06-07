"""
Nama Modul: test_unit_seed_data.py
Deskripsi: Unit test terisolasi (mocked) untuk modul db/seed_data.py.
           Menguji seluruh fungsi hashing password default, seeding data cabang,
           pengguna, saldo_ppob, saldo_ewallet, system_configs secara idempoten,
           verifikasi integritas, dan run_seed_all secara transaksional ACID.
Author: Antigravity
Tanggal: 2026-06-04
"""

# 1. Standard Library
from collections import namedtuple
from decimal import Decimal
from typing import Any
from unittest.mock import MagicMock, patch, call

# 2. Third-Party
import mysql.connector
import pytest

# 3. Local Modules
from db.seed_data import (
    generate_default_password_hash,
    seed_cabang_default,
    seed_pengguna_default,
    seed_saldo_ppob_default,
    seed_saldo_ewallet_default,
    seed_system_configs_default,
    seed_satuan_ukur_default,
    seed_konversi_satuan_default,
    verify_seed_integrity,
    run_seed_all,
    DEFAULT_CABANG_DATA,
    DEFAULT_PENGGUNA_DATA,
    DEFAULT_SALDO_PPOB_DATA,
    DEFAULT_SALDO_EWALLET_DATA,
    DEFAULT_SYSTEM_CONFIGS_DATA,
    EXPECTED_SEED_COUNTS,
    DEFAULT_PASSWORD,
    Result
)


def _make_mysql_error(errno: int, msg: str) -> mysql.connector.Error:
    """Helper untuk membuat mysql.connector.Error dengan errno dan msg."""
    err = mysql.connector.Error()
    err.errno = errno
    err.msg = msg
    return err


# ==============================================================================
# Uji generate_default_password_hash()
# ==============================================================================

def test_generate_default_password_hash_sukses() -> None:
    """Memverifikasi sukses generasi bcrypt hash untuk default password.

    Skenario: Positif
    Target: generate_default_password_hash
    """
    res = generate_default_password_hash(DEFAULT_PASSWORD)
    assert res.is_success is True
    assert res.data.startswith('$2b$12$')
    assert res.error_msg is None


def test_generate_default_password_hash_gagal_kosong() -> None:
    """Memverifikasi kegagalan generasi hash jika string password kosong.

    Skenario: Negatif
    Target: generate_default_password_hash
    """
    res = generate_default_password_hash("")
    assert res.is_success is False
    assert res.data is None
    assert "ERR-VAL-050" in res.error_msg


@patch('db.seed_data.bcrypt.gensalt')
def test_generate_default_password_hash_gagal_format_invalid(mock_gensalt) -> None:
    """Memverifikasi penanganan error jika hasil hash tidak dimulai dengan $2b$12$.

    Skenario: Negatif
    Target: generate_default_password_hash
    """
    # Force bcrypt to return a mock salt that triggers wrong prefix or force bcrypt failure
    mock_gensalt.return_value = b"$2a$10$fakesalt"
    res = generate_default_password_hash(DEFAULT_PASSWORD)
    assert res.is_success is False
    assert "ERR-VAL-050" in res.error_msg


@patch('db.seed_data.bcrypt.hashpw')
def test_generate_default_password_hash_exception(mock_hashpw) -> None:
    """Memverifikasi penanganan Exception umum di generate_default_password_hash.

    Skenario: Negatif
    Target: generate_default_password_hash
    """
    mock_hashpw.side_effect = RuntimeError("Bcrypt runtime crash")
    res = generate_default_password_hash(DEFAULT_PASSWORD)
    assert res.is_success is False
    assert "ERR-VAL-050" in res.error_msg
    assert "Bcrypt runtime crash" in res.error_msg


# ==============================================================================
# Uji seed_cabang_default()
# ==============================================================================

def test_seed_cabang_default_skip_jika_ada() -> None:
    """Memverifikasi bahwa seed cabang dilewati jika data cabang id=1 sudah ada (Idempotent).

    Skenario: Positif
    Target: seed_cabang_default
    """
    mock_cursor = MagicMock()
    # SELECT COUNT(*) -> returns 1
    mock_cursor.fetchone.return_value = (1,)

    res = seed_cabang_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 0
    mock_cursor.execute.assert_called_once_with("SELECT COUNT(*) FROM cabang WHERE id = %s", (1,))
    assert mock_cursor.execute.call_count == 1


def test_seed_cabang_default_insert_jika_kosong() -> None:
    """Memverifikasi bahwa data cabang default di-insert jika cabang id=1 belum ada.

    Skenario: Positif
    Target: seed_cabang_default
    """
    mock_cursor = MagicMock()
    # SELECT COUNT(*) -> returns 0
    mock_cursor.fetchone.return_value = (0,)

    res = seed_cabang_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 1
    mock_cursor.execute.assert_any_call("SELECT COUNT(*) FROM cabang WHERE id = %s", (1,))
    mock_cursor.execute.assert_any_call(
        "INSERT INTO cabang (id, nama_cabang, alamat, telp) VALUES (%s, %s, %s, %s)",
        DEFAULT_CABANG_DATA
    )


def test_seed_cabang_default_mysql_error() -> None:
    """Memverifikasi penanganan mysql.connector.Error saat seed cabang.

    Skenario: Negatif
    Target: seed_cabang_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.execute.side_effect = [None, _make_mysql_error(1064, "Syntax error")]

    res = seed_cabang_default(mock_cursor)
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg
    assert "1064" in res.error_msg


def test_seed_cabang_default_general_exception() -> None:
    """Memverifikasi penanganan Exception umum saat seed cabang.

    Skenario: Negatif
    Target: seed_cabang_default
    """
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = Exception("Fatal failure")

    res = seed_cabang_default(mock_cursor)
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg
    assert "Fatal failure" in res.error_msg


# ==============================================================================
# Uji seed_pengguna_default()
# ==============================================================================

def test_seed_pengguna_default_skip_jika_ada() -> None:
    """Memverifikasi bahwa seed pengguna dilewati jika data pemilik id=1 sudah ada.

    Skenario: Positif
    Target: seed_pengguna_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (1,)

    res = seed_pengguna_default(mock_cursor, "$2b$12$hashedpass")
    assert res.is_success is True
    assert res.data == 0
    mock_cursor.execute.assert_called_once_with("SELECT COUNT(*) FROM pengguna WHERE id = %s", (1,))


def test_seed_pengguna_default_insert_jika_kosong() -> None:
    """Memverifikasi data pengguna di-insert jika pengguna id=1 belum ada.

    Skenario: Positif
    Target: seed_pengguna_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)

    hash_val = "$2b$12$hashedpass"
    res = seed_pengguna_default(mock_cursor, hash_val)
    assert res.is_success is True
    assert res.data == 1
    mock_cursor.execute.assert_any_call("SELECT COUNT(*) FROM pengguna WHERE id = %s", (1,))
    expected_params = (
        DEFAULT_PENGGUNA_DATA[0],
        DEFAULT_PENGGUNA_DATA[1],
        DEFAULT_PENGGUNA_DATA[2],
        hash_val,
        DEFAULT_PENGGUNA_DATA[3],
        DEFAULT_PENGGUNA_DATA[4],
        None,
        DEFAULT_PENGGUNA_DATA[5]
    )
    mock_cursor.execute.assert_any_call(
        "INSERT INTO pengguna (id, nama_lengkap, username, password_hash, role, "
        "failed_login_attempts, locked_until, cabang_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        expected_params
    )


def test_seed_pengguna_default_mysql_error() -> None:
    """Memverifikasi penanganan mysql.connector.Error saat seed pengguna.

    Skenario: Negatif
    Target: seed_pengguna_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.execute.side_effect = [None, _make_mysql_error(1048, "Column cannot be null")]

    res = seed_pengguna_default(mock_cursor, "$2b$12$hash")
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg
    assert "1048" in res.error_msg


# ==============================================================================
# Uji seed_saldo_ppob_default()
# ==============================================================================

def test_seed_saldo_ppob_default_skip_jika_cukup() -> None:
    """Memverifikasi seed PPOB skip jika baris saldo_ppob di db >= 2.

    Skenario: Positif
    Target: seed_saldo_ppob_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (2,)

    res = seed_saldo_ppob_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 0
    mock_cursor.execute.assert_called_once_with("SELECT COUNT(*) FROM saldo_ppob")


def test_seed_saldo_ppob_default_insert_jika_kosong() -> None:
    """Memverifikasi data saldo PPOB di-insert jika tabel kosong/kurang.

    Skenario: Positif
    Target: seed_saldo_ppob_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.rowcount = 1  # simulate 1 row affected per execute

    res = seed_saldo_ppob_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 2
    mock_cursor.execute.assert_any_call("SELECT COUNT(*) FROM saldo_ppob")
    mock_cursor.execute.assert_any_call(
        "INSERT IGNORE INTO saldo_ppob (akun_tipe, saldo_terakhir, cabang_id) VALUES (%s, %s, %s)",
        DEFAULT_SALDO_PPOB_DATA[0]
    )
    mock_cursor.execute.assert_any_call(
        "INSERT IGNORE INTO saldo_ppob (akun_tipe, saldo_terakhir, cabang_id) VALUES (%s, %s, %s)",
        DEFAULT_SALDO_PPOB_DATA[1]
    )


def test_seed_saldo_ppob_default_mysql_error() -> None:
    """Memverifikasi penanganan mysql.connector.Error saat seed PPOB.

    Skenario: Negatif
    Target: seed_saldo_ppob_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.execute.side_effect = [None, _make_mysql_error(2006, "MySQL Gone Away")]

    res = seed_saldo_ppob_default(mock_cursor)
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg


# ==============================================================================
# Uji seed_saldo_ewallet_default()
# ==============================================================================

def test_seed_saldo_ewallet_default_skip_jika_cukup() -> None:
    """Memverifikasi seed e-wallet skip jika baris saldo_ewallet di db >= 6.

    Skenario: Positif
    Target: seed_saldo_ewallet_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (6,)

    res = seed_saldo_ewallet_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 0
    mock_cursor.execute.assert_called_once_with("SELECT COUNT(*) FROM saldo_ewallet")


def test_seed_saldo_ewallet_default_insert_jika_kosong() -> None:
    """Memverifikasi data saldo e-wallet di-insert jika tabel kosong/kurang.

    Skenario: Positif
    Target: seed_saldo_ewallet_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.rowcount = 1

    res = seed_saldo_ewallet_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 6
    mock_cursor.execute.assert_any_call("SELECT COUNT(*) FROM saldo_ewallet")
    assert mock_cursor.execute.call_count == 7  # 1 check + 6 inserts


def test_seed_saldo_ewallet_default_mysql_error() -> None:
    """Memverifikasi penanganan mysql.connector.Error saat seed e-wallet.

    Skenario: Negatif
    Target: seed_saldo_ewallet_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.execute.side_effect = [None, _make_mysql_error(1146, "Table not found")]

    res = seed_saldo_ewallet_default(mock_cursor)
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg


# ==============================================================================
# Uji seed_system_configs_default()
# ==============================================================================

def test_seed_system_configs_default_skip_jika_cukup() -> None:
    """Memverifikasi seed configs skip jika baris system_configs di db >= 13.

    Skenario: Positif
    Target: seed_system_configs_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (13,)

    res = seed_system_configs_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 0
    mock_cursor.execute.assert_called_once_with("SELECT COUNT(*) FROM system_configs")


def test_seed_system_configs_default_insert_jika_kosong() -> None:
    """Memverifikasi data system configs di-insert jika tabel kosong.

    Skenario: Positif
    Target: seed_system_configs_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.rowcount = 1

    res = seed_system_configs_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 13
    mock_cursor.execute.assert_any_call("SELECT COUNT(*) FROM system_configs")
    
    # Check that decimal is cast to string when passing to DB param bindings
    expected_row = DEFAULT_SYSTEM_CONFIGS_DATA[0]
    expected_params = (expected_row[0], str(expected_row[1]), expected_row[2], expected_row[3], expected_row[4])
    mock_cursor.execute.assert_any_call(
        "INSERT IGNORE INTO system_configs (parameter_key, parameter_value, "
        "tipe_data, deskripsi, cabang_id) VALUES (%s, %s, %s, %s, %s)",
        expected_params
    )


def test_seed_system_configs_default_mysql_error() -> None:
    """Memverifikasi penanganan mysql.connector.Error saat seed system configs.

    Skenario: Negatif
    Target: seed_system_configs_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.execute.side_effect = [None, _make_mysql_error(1048, "Null violation")]

    res = seed_system_configs_default(mock_cursor)
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg


# ==============================================================================
# Uji verify_seed_integrity()
# ==============================================================================

def test_verify_seed_integrity_valid_sempurna() -> None:
    """Memverifikasi integritas valid (semua counts sesuai, password hash bcrypt valid, unique keys).

    Skenario: Positif
    Target: verify_seed_integrity
    """
    mock_cursor = MagicMock()
    # fetchone returns counts: 1, 1, 2, 6, 13
    # then password_hash: '$2b$12$validbcrypt...'
    # then unique keys: 13
    mock_cursor.fetchone.side_effect = [
        (1,),  # cabang
        (1,),  # pengguna
        (2,),  # saldo_ppob
        (6,),  # saldo_ewallet
        (13,), # system_configs
        (16,), # satuan_ukur
        (10,), # konversi_satuan
        ('$2b$12$validbcryptsamplehashhere',),  # password_hash
        (13,)  # unique keys config
    ]

    res = verify_seed_integrity(mock_cursor)
    assert res.is_success is True
    assert res.data == EXPECTED_SEED_COUNTS
    assert res.error_msg is None


def test_verify_seed_integrity_mismatch_counts() -> None:
    """Memverifikasi deteksi mismatch counts data seed.

    Skenario: Negatif
    Target: verify_seed_integrity
    """
    mock_cursor = MagicMock()
    # system_configs return 10 instead of 13
    mock_cursor.fetchone.side_effect = [
        (1,),  # cabang
        (1,),  # pengguna
        (2,),  # saldo_ppob
        (6,),  # saldo_ewallet
        (10,), # system_configs (mismatch!)
        (16,), # satuan_ukur
        (10,), # konversi_satuan
        ('$2b$12$validhash',),
        (13,)
    ]

    res = verify_seed_integrity(mock_cursor)
    assert res.is_success is False
    assert "diharapkan 13 baris, ditemukan 10 baris" in res.error_msg


def test_verify_seed_integrity_mismatch_password_hash() -> None:
    """Memverifikasi deteksi format password hash invalid (bukan bcrypt cost 12).

    Skenario: Negatif
    Target: verify_seed_integrity
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.side_effect = [
        (1,), (1,), (2,), (6,), (13,), (16,), (10,),
        ('$2a$10$wrongprefixhash',),  # wrong prefix cost 10
        (13,)
    ]

    res = verify_seed_integrity(mock_cursor)
    assert res.is_success is False
    assert "bukan format bcrypt Cost 12 valid" in res.error_msg


def test_verify_seed_integrity_mismatch_unique_keys() -> None:
    """Memverifikasi deteksi duplikasi key config di system_configs.

    Skenario: Negatif
    Target: verify_seed_integrity
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.side_effect = [
        (1,), (1,), (2,), (6,), (13,), (16,), (10,),
        ('$2b$12$validhash',),
        (10,)  # only 10 unique keys instead of 13!
    ]

    res = verify_seed_integrity(mock_cursor)
    assert res.is_success is False
    assert "diharapkan 13 parameter unik" in res.error_msg


def test_verify_seed_integrity_no_user_found() -> None:
    """Memverifikasi error jika pengguna default id=1 tidak ditemukan.

    Skenario: Negatif
    Target: verify_seed_integrity
    """
    mock_cursor = MagicMock()
    # pengguna id=1 fetchone -> None
    mock_cursor.fetchone.side_effect = [
        (1,), (1,), (2,), (6,), (13,), (16,), (10,),
        None,  # no user row
        (13,)
    ]

    res = verify_seed_integrity(mock_cursor)
    assert res.is_success is False
    assert "akun pemilik default id = 1 tidak ditemukan" in res.error_msg


def test_verify_seed_integrity_mysql_error() -> None:
    """Memverifikasi penanganan mysql.connector.Error di verify_seed_integrity.

    Skenario: Negatif
    Target: verify_seed_integrity
    """
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = _make_mysql_error(2013, "Connection lost")

    res = verify_seed_integrity(mock_cursor)
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg
    assert "2013" in res.error_msg


# ==============================================================================
# Uji run_seed_all()
# ==============================================================================

@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
@patch('db.seed_data.seed_pengguna_default')
@patch('db.seed_data.seed_saldo_ppob_default')
@patch('db.seed_data.seed_saldo_ewallet_default')
@patch('db.seed_data.seed_system_configs_default')
@patch('db.seed_data.seed_satuan_ukur_default')
@patch('db.seed_data.seed_konversi_satuan_default')
@patch('db.seed_data.verify_seed_integrity')
def test_run_seed_all_sukses_komplit(
    mock_verify, mock_konversi, mock_satuan, mock_configs, mock_ewallet, mock_ppob, mock_pengguna, mock_cabang, mock_gen_hash
) -> None:
    """Memverifikasi alur penuh run_seed_all sukses komplit dengan commit transaksi.

    Skenario: Positif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_gen_hash.return_value = Result(True, "$2b$12$hashedpwd", None)
    mock_cabang.return_value = Result(True, 1, None)
    mock_pengguna.return_value = Result(True, 1, None)
    mock_ppob.return_value = Result(True, 2, None)
    mock_ewallet.return_value = Result(True, 6, None)
    mock_configs.return_value = Result(True, 13, None)
    mock_satuan.return_value = Result(True, 16, None)
    mock_konversi.return_value = Result(True, 10, None)
    mock_verify.return_value = Result(True, EXPECTED_SEED_COUNTS, None)

    res = run_seed_all(mock_conn)
    assert res.is_success is True
    assert res.data['cabang_inserted'] == 1
    assert res.data['satuan_ukur_inserted'] == 16
    assert res.data['konversi_satuan_inserted'] == 10
    assert res.data['report'] == EXPECTED_SEED_COUNTS
    assert res.error_msg is None

    mock_conn.start_transaction.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_conn.rollback.assert_not_called()
    mock_cursor.close.assert_called_once()


def test_run_seed_all_gagal_koneksi_none() -> None:
    """Memverifikasi penolakan run_seed_all jika connection parameter is None.

    Skenario: Negatif
    Target: run_seed_all
    """
    res = run_seed_all(None)
    assert res.is_success is False
    assert "Koneksi database tidak boleh None" in res.error_msg


@patch('db.seed_data.generate_default_password_hash')
def test_run_seed_all_gagal_gen_hash(mock_gen_hash) -> None:
    """Memverifikasi penghentian run_seed_all jika generate hash password default gagal.

    Skenario: Negatif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_gen_hash.return_value = Result(False, None, "ERR-VAL-050: Hash failure")

    res = run_seed_all(mock_conn)
    assert res.is_success is False
    assert "Hash failure" in res.error_msg
    mock_conn.cursor.assert_not_called()


@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
def test_run_seed_all_gagal_seed_cabang_dan_rollback(mock_cabang, mock_gen_hash) -> None:
    """Memverifikasi rollback transaksi jika seed cabang gagal di run_seed_all.

    Skenario: Negatif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_gen_hash.return_value = Result(True, "$2b$12$hashedpwd", None)
    mock_cabang.return_value = Result(False, None, "ERR-DB-SEED-001: Branch fail")

    res = run_seed_all(mock_conn)
    assert res.is_success is False
    assert "Branch fail" in res.error_msg
    mock_conn.start_transaction.assert_called_once()
    mock_conn.rollback.assert_called_once()
    mock_conn.commit.assert_not_called()
    mock_cursor.close.assert_called_once()


@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
@patch('db.seed_data.seed_pengguna_default')
def test_run_seed_all_gagal_seed_pengguna_dan_rollback(mock_pengguna, mock_cabang, mock_gen_hash) -> None:
    """Memverifikasi rollback transaksi jika seed pengguna gagal di run_seed_all.

    Skenario: Negatif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_gen_hash.return_value = Result(True, "$2b$12$hashedpwd", None)
    mock_cabang.return_value = Result(True, 1, None)
    mock_pengguna.return_value = Result(False, None, "ERR-DB-SEED-001: User fail")

    res = run_seed_all(mock_conn)
    assert res.is_success is False
    assert "User fail" in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_conn.commit.assert_not_called()


@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
@patch('db.seed_data.seed_pengguna_default')
@patch('db.seed_data.seed_saldo_ppob_default')
def test_run_seed_all_gagal_seed_ppob_dan_rollback(mock_ppob, mock_pengguna, mock_cabang, mock_gen_hash) -> None:
    """Memverifikasi rollback transaksi jika seed ppob gagal di run_seed_all.

    Skenario: Negatif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_gen_hash.return_value = Result(True, "$2b$12$hashedpwd", None)
    mock_cabang.return_value = Result(True, 1, None)
    mock_pengguna.return_value = Result(True, 1, None)
    mock_ppob.return_value = Result(False, None, "ERR-DB-SEED-001: PPOB fail")

    res = run_seed_all(mock_conn)
    assert res.is_success is False
    assert "PPOB fail" in res.error_msg
    mock_conn.rollback.assert_called_once()


@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
@patch('db.seed_data.seed_pengguna_default')
@patch('db.seed_data.seed_saldo_ppob_default')
@patch('db.seed_data.seed_saldo_ewallet_default')
def test_run_seed_all_gagal_seed_ewallet_dan_rollback(mock_ewallet, mock_ppob, mock_pengguna, mock_cabang, mock_gen_hash) -> None:
    """Memverifikasi rollback transaksi jika seed ewallet gagal di run_seed_all.

    Skenario: Negatif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_gen_hash.return_value = Result(True, "$2b$12$hashedpwd", None)
    mock_cabang.return_value = Result(True, 1, None)
    mock_pengguna.return_value = Result(True, 1, None)
    mock_ppob.return_value = Result(True, 2, None)
    mock_ewallet.return_value = Result(False, None, "ERR-DB-SEED-001: Ewallet fail")

    res = run_seed_all(mock_conn)
    assert res.is_success is False
    assert "Ewallet fail" in res.error_msg
    mock_conn.rollback.assert_called_once()


@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
@patch('db.seed_data.seed_pengguna_default')
@patch('db.seed_data.seed_saldo_ppob_default')
@patch('db.seed_data.seed_saldo_ewallet_default')
@patch('db.seed_data.seed_system_configs_default')
def test_run_seed_all_gagal_seed_configs_dan_rollback(mock_configs, mock_ewallet, mock_ppob, mock_pengguna, mock_cabang, mock_gen_hash) -> None:
    """Memverifikasi rollback transaksi jika seed configs gagal di run_seed_all.

    Skenario: Negatif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_gen_hash.return_value = Result(True, "$2b$12$hashedpwd", None)
    mock_cabang.return_value = Result(True, 1, None)
    mock_pengguna.return_value = Result(True, 1, None)
    mock_ppob.return_value = Result(True, 2, None)
    mock_ewallet.return_value = Result(True, 6, None)
    mock_configs.return_value = Result(False, None, "ERR-DB-SEED-001: Configs fail")

    res = run_seed_all(mock_conn)
    assert res.is_success is False
    assert "Configs fail" in res.error_msg
    mock_conn.rollback.assert_called_once()


@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
@patch('db.seed_data.seed_pengguna_default')
@patch('db.seed_data.seed_saldo_ppob_default')
@patch('db.seed_data.seed_saldo_ewallet_default')
@patch('db.seed_data.seed_system_configs_default')
@patch('db.seed_data.seed_satuan_ukur_default')
@patch('db.seed_data.seed_konversi_satuan_default')
@patch('db.seed_data.verify_seed_integrity')
def test_run_seed_all_gagal_verifikasi_dan_return_fail(
    mock_verify, mock_konversi, mock_satuan, mock_configs, mock_ewallet, mock_ppob, mock_pengguna, mock_cabang, mock_gen_hash
) -> None:
    """Memverifikasi pengembalian fail jika verifikasi pasca-commit gagal.

    Skenario: Negatif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_gen_hash.return_value = Result(True, "$2b$12$hashedpwd", None)
    mock_cabang.return_value = Result(True, 1, None)
    mock_pengguna.return_value = Result(True, 1, None)
    mock_ppob.return_value = Result(True, 2, None)
    mock_ewallet.return_value = Result(True, 6, None)
    mock_configs.return_value = Result(True, 13, None)
    mock_satuan.return_value = Result(True, 16, None)
    mock_konversi.return_value = Result(True, 10, None)
    mock_verify.return_value = Result(False, None, "Verification mismatch")

    res = run_seed_all(mock_conn)
    assert res.is_success is False
    assert "Verification mismatch" in res.error_msg
    mock_conn.commit.assert_called_once()


@patch('db.seed_data.generate_default_password_hash')
def test_run_seed_all_general_exception_handling(mock_gen_hash) -> None:
    """Memverifikasi penanganan exception umum di run_seed_all (memicu rollback).

    Skenario: Negatif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = RuntimeError("Cursor allocation crash")
    mock_gen_hash.return_value = Result(True, "$2b$12$hashed", None)

    res = run_seed_all(mock_conn)
    assert res.is_success is False
    assert "Cursor allocation crash" in res.error_msg
    mock_conn.rollback.assert_called_once()


# ==============================================================================
# Uji Konsistensi Konstanta
# ==============================================================================

def test_konstanta_konsistensi_dan_tipe() -> None:
    """Memverifikasi konsistensi jumlah baris dan tipe data pada konstanta seed data.

    Skenario: Positif
    Target: DEFAULT_constants
    """
    assert len(DEFAULT_SYSTEM_CONFIGS_DATA) == 13
    assert len(DEFAULT_SALDO_EWALLET_DATA) == 6
    assert len(DEFAULT_SALDO_PPOB_DATA) == 2
    assert EXPECTED_SEED_COUNTS['system_configs'] == 13
    assert EXPECTED_SEED_COUNTS['saldo_ewallet'] == 6
    assert EXPECTED_SEED_COUNTS['saldo_ppob'] == 2
    assert EXPECTED_SEED_COUNTS['cabang'] == 1
    assert EXPECTED_SEED_COUNTS['pengguna'] == 1

    # Check that system configs parameter values are Decimals (prior to casting to string for DML)
    for row in DEFAULT_SYSTEM_CONFIGS_DATA:
        assert isinstance(row[1], Decimal)
        assert row[2] == 'DECIMAL'

    # Check ewallet amounts
    for row in DEFAULT_SALDO_EWALLET_DATA:
        assert isinstance(row[1], Decimal)
        assert isinstance(row[2], Decimal)
        assert isinstance(row[3], Decimal)
        assert isinstance(row[4], Decimal)


@patch('db.seed_data.bcrypt.hashpw')
def test_generate_default_password_hash_wrong_prefix(mock_hashpw) -> None:
    """Memverifikasi kegagalan jika hash yang dihasilkan tidak berawalan $2b$12$."""
    mock_hashpw.return_value = b"$2a$10$invalidprefix"
    res = generate_default_password_hash(DEFAULT_PASSWORD)
    assert res.is_success is False
    assert "Format bcrypt hash yang dihasilkan tidak valid" in res.error_msg


def test_seed_pengguna_default_general_exception() -> None:
    """Memverifikasi penanganan exception umum pada seed_pengguna_default."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.execute.side_effect = [None, RuntimeError("General crash")]
    res = seed_pengguna_default(mock_cursor, "hash")
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg


def test_seed_saldo_ppob_default_general_exception() -> None:
    """Memverifikasi penanganan exception umum pada seed_saldo_ppob_default."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.execute.side_effect = RuntimeError("General crash")
    res = seed_saldo_ppob_default(mock_cursor)
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg


def test_seed_saldo_ewallet_default_general_exception() -> None:
    """Memverifikasi penanganan exception umum pada seed_saldo_ewallet_default."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.execute.side_effect = RuntimeError("General crash")
    res = seed_saldo_ewallet_default(mock_cursor)
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg


def test_seed_system_configs_default_general_exception() -> None:
    """Memverifikasi penanganan exception umum pada seed_system_configs_default."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.execute.side_effect = RuntimeError("General crash")
    res = seed_system_configs_default(mock_cursor)
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg


def test_verify_seed_integrity_general_exception() -> None:
    """Memverifikasi penanganan exception umum pada verify_seed_integrity."""
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = RuntimeError("General crash")
    res = verify_seed_integrity(mock_cursor)
    assert res.is_success is False
    assert "ERR-DB-SEED-001" in res.error_msg


@patch('db.seed_data.generate_default_password_hash')
def test_run_seed_all_mysql_error_in_transaction(mock_gen_hash) -> None:
    """Memverifikasi penanganan mysql error di tengah transaksi run_seed_all."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_gen_hash.return_value = Result(True, "$2b$12$hashed", None)
    mock_conn.start_transaction.side_effect = _make_mysql_error(2006, "MySQL Gone Away")
    res = run_seed_all(mock_conn)
    assert res.is_success is False
    assert "MySQL Gone Away" in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_cursor.close.assert_called_once()


@patch('db.seed_data.generate_default_password_hash')
def test_run_seed_all_rollback_exception_handling(mock_gen_hash) -> None:
    """Memverifikasi penanganan exception pada saat rollback di run_seed_all."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_gen_hash.return_value = Result(True, "$2b$12$hashed", None)
    mock_conn.start_transaction.side_effect = RuntimeError("Crash")
    mock_conn.rollback.side_effect = RuntimeError("Rollback crash")
    res = run_seed_all(mock_conn)
    assert res.is_success is False
    assert "Crash" in res.error_msg
    mock_conn.rollback.assert_called_once()
    mock_cursor.close.assert_called_once()


# ==============================================================================
# Skenario Test Tambahan — Issue #0097
# ==============================================================================

# ------------------------------------------------------------------------------
# GRUP A: generate_default_password_hash — Edge Cases Tambahan
# ------------------------------------------------------------------------------

def test_generate_default_password_hash_karakter_unicode() -> None:
    """Memverifikasi bahwa bcrypt mampu meng-hash password dengan karakter unicode/spesial.

    Skenario: Positif / Edge Case
    Target: generate_default_password_hash
    """
    res = generate_default_password_hash("P@$$wörd_日本語!#2026")
    assert res.is_success is True
    assert res.data.startswith('$2b$12$')
    assert res.error_msg is None
    assert len(res.data) >= 59


def test_generate_default_password_hash_panjang_72_bytes() -> None:
    """Memverifikasi bahwa bcrypt bekerja pada batas maksimum 72 bytes input.

    Skenario: Edge Case / Boundary
    Target: generate_default_password_hash
    """
    password_panjang = "A" * 72
    res = generate_default_password_hash(password_panjang)
    assert res.is_success is True
    assert res.data.startswith('$2b$12$')


def test_generate_default_password_hash_whitespace_only() -> None:
    """Memverifikasi bahwa whitespace-only dianggap password valid (karena pengecekan hanya if not password).

    Skenario: Edge Case
    Target: generate_default_password_hash
    """
    res = generate_default_password_hash("   ")
    assert res.is_success is True
    assert res.data.startswith('$2b$12$')


# ------------------------------------------------------------------------------
# GRUP B: seed_cabang_default — Edge Cases Tambahan
# ------------------------------------------------------------------------------

def test_seed_cabang_default_verifikasi_query_insert_exact() -> None:
    """Validasi keakuratan query SQL parameterized yang dikirim ke database untuk cabang default.

    Skenario: Validasi Input
    Target: seed_cabang_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)

    res = seed_cabang_default(mock_cursor)
    assert res.is_success is True
    assert mock_cursor.execute.call_count == 2
    mock_cursor.execute.assert_any_call("SELECT COUNT(*) FROM cabang WHERE id = %s", (1,))
    mock_cursor.execute.assert_any_call(
        "INSERT INTO cabang (id, nama_cabang, alamat, telp) VALUES (%s, %s, %s, %s)",
        DEFAULT_CABANG_DATA
    )
    assert DEFAULT_CABANG_DATA[0] == 1
    assert DEFAULT_CABANG_DATA[1] == 'Toko Pusat Bandung'
    assert '0227654321' in DEFAULT_CABANG_DATA


def test_seed_cabang_default_skip_return_data_nol() -> None:
    """Verifikasi idempoten dengan jumlah cabang di database lebih dari 1.

    Skenario: Positif
    Target: seed_cabang_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (5,)

    res = seed_cabang_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 0
    assert res.error_msg is None


# ------------------------------------------------------------------------------
# GRUP C: seed_pengguna_default — Edge Cases Tambahan
# ------------------------------------------------------------------------------

def test_seed_pengguna_default_verifikasi_urutan_params_insert() -> None:
    """Memastikan urutan kolom INSERT sesuai skema database dan locked_until diisi None.

    Skenario: Validasi Input
    Target: seed_pengguna_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    hash_val = "$2b$12$testHashSample1234567890"

    res = seed_pengguna_default(mock_cursor, hash_val)
    assert res.is_success is True

    assert mock_cursor.execute.call_count == 2
    calls = mock_cursor.execute.call_args_list
    insert_args = calls[1][0]
    query, params = insert_args
    assert params == (1, 'Pemilik Usaha AbuCom', 'pemilik', hash_val, 'pemilik', 0, None, 1)
    assert params[6] is None
    assert params[7] == 1


def test_seed_pengguna_default_hash_kosong_string() -> None:
    """Membuktikan seed_pengguna_default tidak memvalidasi format hash password.

    Skenario: Edge Case
    Target: seed_pengguna_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)

    res = seed_pengguna_default(mock_cursor, "")
    assert res.is_success is True
    assert res.data == 1


# ------------------------------------------------------------------------------
# GRUP D: seed_saldo_ppob_default — Edge Cases Tambahan
# ------------------------------------------------------------------------------

def test_seed_saldo_ppob_default_jumlah_execute_calls() -> None:
    """Memverifikasi jumlah query yang dieksekusi sesuai jumlah baris data saldo PPOB.

    Skenario: Validasi Input
    Target: seed_saldo_ppob_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.rowcount = 1

    res = seed_saldo_ppob_default(mock_cursor)
    assert res.is_success is True
    assert mock_cursor.execute.call_count == 3
    assert res.data == 2


def test_seed_saldo_ppob_default_skip_jika_partial_1() -> None:
    """Memverifikasi perilaku ketika data partial PPOB ada, fungsi tetap melakukan insert.

    Skenario: Edge Case / Boundary
    Target: seed_saldo_ppob_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (1,)
    mock_cursor.rowcount = 1

    res = seed_saldo_ppob_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 2


# ------------------------------------------------------------------------------
# GRUP E: seed_saldo_ewallet_default — Edge Cases Tambahan
# ------------------------------------------------------------------------------

def test_seed_saldo_ewallet_default_jumlah_execute_calls_detail() -> None:
    """Memverifikasi semua 6 akun e-wallet diinsert dengan query INSERT IGNORE yang benar.

    Skenario: Validasi Input
    Target: seed_saldo_ewallet_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.rowcount = 1

    res = seed_saldo_ewallet_default(mock_cursor)
    assert res.is_success is True
    assert mock_cursor.execute.call_count == 7

    calls = mock_cursor.execute.call_args_list[1:]
    for c in calls:
        query, params = c[0]
        assert "INSERT IGNORE INTO saldo_ewallet" in query
        assert "nama_ewallet, saldo_terakhir, biaya_admin_flat, biaya_admin_persen, limit_harian, cabang_id" in query
    assert res.data == 6


def test_seed_saldo_ewallet_default_verifikasi_nama_ewallet() -> None:
    """Memastikan seluruh 6 nama akun e-wallet terdaftar secara tepat.

    Skenario: Validasi Input
    Target: seed_saldo_ewallet_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.rowcount = 1

    seed_saldo_ewallet_default(mock_cursor)
    calls = mock_cursor.execute.call_args_list[1:]
    names = [c[0][1][0] for c in calls]
    assert names == ['Mandiri Agen', 'Dana', 'Gopay', 'LinkAja', 'ShopeePay', 'OVO']


def test_seed_saldo_ewallet_default_skip_jika_partial_5() -> None:
    """Boundary test — memverifikasi perilaku saat data saldo e-wallet mendekati threshold.

    Skenario: Edge Case / Boundary
    Target: seed_saldo_ewallet_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (5,)
    mock_cursor.rowcount = 1

    res = seed_saldo_ewallet_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 6


# ------------------------------------------------------------------------------
# GRUP F: seed_system_configs_default — Edge Cases Tambahan
# ------------------------------------------------------------------------------

def test_seed_system_configs_default_verifikasi_semua_parameter_keys() -> None:
    """Memastikan semua 13 parameter konfigurasi bisnis AbuCom terdaftar tanpa terlewat.

    Skenario: Validasi Input
    Target: seed_system_configs_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.rowcount = 1

    seed_system_configs_default(mock_cursor)
    calls = mock_cursor.execute.call_args_list[1:]
    keys = [c[0][1][0] for c in calls]
    expected_keys = [
        'target_laba_payroll',
        'porsi_gaji_laba',
        'limit_kasbon_staf',
        'threshold_saldo_ppob',
        'min_topup_ppob',
        'toleransi_selisih_kas',
        'poin_tier_1_rupiah',
        'poin_tier_2_rupiah',
        'poin_tier_3_rupiah',
        'poin_tier_4_rupiah',
        'threshold_pengeluaran',
        'umr_daerah',
        'dana_cadangan_darurat'
    ]
    assert keys == expected_keys
    assert len(keys) == 13


def test_seed_system_configs_default_decimal_cast_to_string() -> None:
    """Memastikan konversi Decimal ke string dilakukan sebelum query DML.

    Skenario: Validasi Input
    Target: seed_system_configs_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.rowcount = 1

    seed_system_configs_default(mock_cursor)
    calls = mock_cursor.execute.call_args_list[1:]
    for c in calls:
        query, params = c[0]
        val = params[1]
        assert isinstance(val, str)
        d_val = Decimal(val)
        assert isinstance(d_val, Decimal)

    params_by_key = {c[0][1][0]: c[0][1][1] for c in calls}
    assert params_by_key['target_laba_payroll'] == '15000000.0000'
    assert params_by_key['porsi_gaji_laba'] == '0.2500'


def test_seed_system_configs_default_tipe_data_selalu_decimal() -> None:
    """Memastikan semua baris default_system_configs bertipe data DECIMAL.

    Skenario: Validasi Input
    Target: DEFAULT_SYSTEM_CONFIGS_DATA
    """
    for row in DEFAULT_SYSTEM_CONFIGS_DATA:
        assert row[2] == 'DECIMAL'


def test_seed_system_configs_default_cabang_id_selalu_1() -> None:
    """Memastikan semua parameter configs default terikat ke cabang_id = 1.

    Skenario: Validasi Input
    Target: DEFAULT_SYSTEM_CONFIGS_DATA
    """
    for row in DEFAULT_SYSTEM_CONFIGS_DATA:
        assert row[4] == 1


def test_seed_system_configs_default_skip_jika_partial_12() -> None:
    """Boundary test — memverifikasi jika terdapat 12 baris configs, sistem tetap menginsert.

    Skenario: Edge Case / Boundary
    Target: seed_system_configs_default
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (12,)
    mock_cursor.rowcount = 1

    res = seed_system_configs_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 13


# ------------------------------------------------------------------------------
# GRUP G: verify_seed_integrity — Edge Cases Tambahan
# ------------------------------------------------------------------------------

def test_verify_seed_integrity_multiple_errors_combined() -> None:
    """Membuktikan fungsi verify_seed_integrity mengumpulkan semua error yang ditemukan.

    Skenario: Negatif
    Target: verify_seed_integrity
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.side_effect = [(0,), (0,), (0,), (0,), (0,), (0,), (0,), None, (0,)]

    res = verify_seed_integrity(mock_cursor)
    assert res.is_success is False
    assert "cabang" in res.error_msg
    assert "pengguna" in res.error_msg
    assert "akun pemilik default id = 1 tidak ditemukan" in res.error_msg


def test_verify_seed_integrity_report_dict_on_failure() -> None:
    """Verifikasi bahwa report dict dikembalikan meskipun terjadi kegagalan integritas.

    Skenario: Negatif
    Target: verify_seed_integrity
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.side_effect = [(1,), (1,), (2,), (6,), (10,), (16,), (10,), ('$2b$12$valid',), (13,)]

    res = verify_seed_integrity(mock_cursor)
    assert res.is_success is False
    assert res.data is not None
    assert res.data['system_configs'] == 10


def test_verify_seed_integrity_password_hash_kosong() -> None:
    """Verifikasi deteksi kegagalan integritas jika password hash bernilai string kosong.

    Skenario: Edge Case
    Target: verify_seed_integrity
    """
    mock_cursor = MagicMock()
    mock_cursor.fetchone.side_effect = [(1,), (1,), (2,), (6,), (13,), (16,), (10,), ('',), (13,)]

    res = verify_seed_integrity(mock_cursor)
    assert res.is_success is False
    assert "bcrypt Cost 12" in res.error_msg


# ------------------------------------------------------------------------------
# GRUP H: run_seed_all — Edge Cases Tambahan
# ------------------------------------------------------------------------------

@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
@patch('db.seed_data.seed_pengguna_default')
@patch('db.seed_data.seed_saldo_ppob_default')
@patch('db.seed_data.seed_saldo_ewallet_default')
@patch('db.seed_data.seed_system_configs_default')
@patch('db.seed_data.seed_satuan_ukur_default')
@patch('db.seed_data.seed_konversi_satuan_default')
@patch('db.seed_data.verify_seed_integrity')
def test_run_seed_all_urutan_pemanggilan_benar(
    mock_verify, mock_konversi, mock_satuan, mock_configs, mock_ewallet, mock_ppob, mock_pengguna, mock_cabang, mock_gen_hash
) -> None:
    """Memverifikasi seluruh fungsi sub-seed dipanggil sesuai urutan dependensi database yang benar.

    Skenario: Positif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_gen_hash.return_value = Result(True, "$2b$12$hashed", None)
    mock_cabang.return_value = Result(True, 1, None)
    mock_pengguna.return_value = Result(True, 1, None)
    mock_ppob.return_value = Result(True, 2, None)
    mock_ewallet.return_value = Result(True, 6, None)
    mock_configs.return_value = Result(True, 13, None)
    mock_satuan.return_value = Result(True, 16, None)
    mock_konversi.return_value = Result(True, 10, None)
    mock_verify.return_value = Result(True, EXPECTED_SEED_COUNTS, None)

    manager = MagicMock()
    manager.attach_mock(mock_gen_hash, 'gen_hash')
    manager.attach_mock(mock_cabang, 'cabang')
    manager.attach_mock(mock_pengguna, 'pengguna')
    manager.attach_mock(mock_ppob, 'ppob')
    manager.attach_mock(mock_ewallet, 'ewallet')
    manager.attach_mock(mock_configs, 'configs')
    manager.attach_mock(mock_satuan, 'satuan')
    manager.attach_mock(mock_konversi, 'konversi')
    manager.attach_mock(mock_verify, 'verify')

    res = run_seed_all(mock_conn)
    assert res.is_success is True

    calls = manager.mock_calls
    names = [c[0] for c in calls]
    sub_seed_names = [n for n in names if n in ('gen_hash', 'cabang', 'pengguna', 'ppob', 'ewallet', 'configs', 'satuan', 'konversi', 'verify')]
    assert sub_seed_names == ['gen_hash', 'cabang', 'pengguna', 'ppob', 'ewallet', 'configs', 'satuan', 'konversi', 'verify']


@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
@patch('db.seed_data.seed_pengguna_default')
@patch('db.seed_data.seed_saldo_ppob_default')
@patch('db.seed_data.seed_saldo_ewallet_default')
@patch('db.seed_data.seed_system_configs_default')
@patch('db.seed_data.seed_satuan_ukur_default')
@patch('db.seed_data.seed_konversi_satuan_default')
@patch('db.seed_data.verify_seed_integrity')
def test_run_seed_all_stats_dict_lengkap(
    mock_verify, mock_konversi, mock_satuan, mock_configs, mock_ewallet, mock_ppob, mock_pengguna, mock_cabang, mock_gen_hash
) -> None:
    """Memverifikasi bahwa stats dictionary hasil seeding lengkap dan akurat pada saat sukses.

    Skenario: Positif
    Target: run_seed_all
    """
    mock_conn = MagicMock()

    mock_gen_hash.return_value = Result(True, "$2b$12$hashed", None)
    mock_cabang.return_value = Result(True, 1, None)
    mock_pengguna.return_value = Result(True, 2, None)
    mock_ppob.return_value = Result(True, 3, None)
    mock_ewallet.return_value = Result(True, 4, None)
    mock_configs.return_value = Result(True, 5, None)
    mock_satuan.return_value = Result(True, 6, None)
    mock_konversi.return_value = Result(True, 7, None)
    mock_verify.return_value = Result(True, EXPECTED_SEED_COUNTS, None)

    res = run_seed_all(mock_conn)
    assert res.is_success is True
    assert res.data == {
        'cabang_inserted': 1,
        'pengguna_inserted': 2,
        'saldo_ppob_inserted': 3,
        'saldo_ewallet_inserted': 4,
        'system_configs_inserted': 5,
        'satuan_ukur_inserted': 6,
        'konversi_satuan_inserted': 7,
        'report': EXPECTED_SEED_COUNTS
    }
    assert len(res.data) == 8


@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
@patch('db.seed_data.seed_pengguna_default')
@patch('db.seed_data.seed_saldo_ppob_default')
@patch('db.seed_data.seed_saldo_ewallet_default')
@patch('db.seed_data.seed_system_configs_default')
@patch('db.seed_data.seed_satuan_ukur_default')
@patch('db.seed_data.seed_konversi_satuan_default')
def test_run_seed_all_cursor_close_saat_commit_error(
    mock_konversi, mock_satuan, mock_configs, mock_ewallet, mock_ppob, mock_pengguna, mock_cabang, mock_gen_hash
) -> None:
    """Memverifikasi bahwa cursor tetap ditutup dan transaksi di-rollback jika commit database error.

    Skenario: Negatif
    Target: run_seed_all
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    mock_gen_hash.return_value = Result(True, "$2b$12$hashedpwd", None)
    mock_cabang.return_value = Result(True, 1, None)
    mock_pengguna.return_value = Result(True, 1, None)
    mock_ppob.return_value = Result(True, 2, None)
    mock_ewallet.return_value = Result(True, 6, None)
    mock_configs.return_value = Result(True, 13, None)
    mock_satuan.return_value = Result(True, 16, None)
    mock_konversi.return_value = Result(True, 10, None)

    mock_conn.commit.side_effect = RuntimeError("Commit crash")

    res = run_seed_all(mock_conn)
    assert res.is_success is False
    mock_cursor.close.assert_called_once()
    mock_conn.rollback.assert_called_once()


@patch('db.seed_data.generate_default_password_hash')
@patch('db.seed_data.seed_cabang_default')
@patch('db.seed_data.seed_pengguna_default')
@patch('db.seed_data.seed_saldo_ppob_default')
@patch('db.seed_data.seed_saldo_ewallet_default')
@patch('db.seed_data.seed_system_configs_default')
@patch('db.seed_data.seed_satuan_ukur_default')
@patch('db.seed_data.seed_konversi_satuan_default')
@patch('db.seed_data.verify_seed_integrity')
def test_run_seed_all_idempoten_semua_data_sudah_ada(
    mock_verify, mock_konversi, mock_satuan, mock_configs, mock_ewallet, mock_ppob, mock_pengguna, mock_cabang, mock_gen_hash
) -> None:
    """Memverifikasi run_seed_all bersifat idempoten jika seluruh data seed sudah terisi lengkap di db.

    Skenario: Positif / Idempoten
    Target: run_seed_all
    """
    mock_conn = MagicMock()

    mock_gen_hash.return_value = Result(True, "$2b$12$hashedpwd", None)
    mock_cabang.return_value = Result(True, 0, None)
    mock_pengguna.return_value = Result(True, 0, None)
    mock_ppob.return_value = Result(True, 0, None)
    mock_ewallet.return_value = Result(True, 0, None)
    mock_configs.return_value = Result(True, 0, None)
    mock_satuan.return_value = Result(True, 0, None)
    mock_konversi.return_value = Result(True, 0, None)
    mock_verify.return_value = Result(True, EXPECTED_SEED_COUNTS, None)

    res = run_seed_all(mock_conn)
    assert res.is_success is True
    assert res.data['cabang_inserted'] == 0
    assert res.data['pengguna_inserted'] == 0
    assert res.data['saldo_ppob_inserted'] == 0
    assert res.data['saldo_ewallet_inserted'] == 0
    assert res.data['system_configs_inserted'] == 0
    assert res.data['satuan_ukur_inserted'] == 0
    assert res.data['konversi_satuan_inserted'] == 0


# ------------------------------------------------------------------------------
# GRUP I: Konstanta Data — Validasi Lanjutan
# ------------------------------------------------------------------------------

def test_konstanta_system_configs_presisi_4_digit_decimal() -> None:
    """Memverifikasi semua parameter nilai desimal system_configs memiliki presisi tepat 4 digit desimal.

    Skenario: Validasi Input
    Target: DEFAULT_SYSTEM_CONFIGS_DATA
    """
    for row in DEFAULT_SYSTEM_CONFIGS_DATA:
        val = row[1]
        parts = str(val).split('.')
        assert len(parts) == 2
        assert len(parts[1]) == 4


def test_konstanta_system_configs_nilai_bisnis_kritis() -> None:
    """Memverifikasi nilai parameter bisnis kritis sesuai dengan spesifikasi SRS.

    Skenario: Validasi Input
    Target: DEFAULT_SYSTEM_CONFIGS_DATA
    """
    d = {row[0]: row[1] for row in DEFAULT_SYSTEM_CONFIGS_DATA}
    assert d['target_laba_payroll'] == Decimal('15000000.0000')
    assert d['porsi_gaji_laba'] == Decimal('0.2500')
    assert d['toleransi_selisih_kas'] == Decimal('10000.0000')
    assert d['umr_daerah'] == Decimal('3200000.0000')
    assert d['threshold_pengeluaran'] == Decimal('500000.0000')
    assert d['poin_tier_1_rupiah'] == Decimal('500.0000')
    assert d['poin_tier_2_rupiah'] == Decimal('1500.0000')
    assert d['poin_tier_3_rupiah'] == Decimal('2500.0000')
    assert d['poin_tier_4_rupiah'] == Decimal('5000.0000')
    assert d['dana_cadangan_darurat'] == Decimal('4500000.0000')


def test_konstanta_default_cabang_data_lengkap() -> None:
    """Memverifikasi kelengkapan dan format data cabang default.

    Skenario: Validasi Input
    Target: DEFAULT_CABANG_DATA
    """
    assert len(DEFAULT_CABANG_DATA) == 4
    assert DEFAULT_CABANG_DATA[0] == 1
    assert isinstance(DEFAULT_CABANG_DATA[1], str)
    assert isinstance(DEFAULT_CABANG_DATA[2], str)
    assert isinstance(DEFAULT_CABANG_DATA[3], str)
    assert len(DEFAULT_CABANG_DATA[1]) > 0
    assert len(DEFAULT_CABANG_DATA[2]) > 0
    assert len(DEFAULT_CABANG_DATA[3]) > 0


def test_konstanta_default_pengguna_data_lengkap() -> None:
    """Memverifikasi kelengkapan data pengguna default untuk akun pemilik.

    Skenario: Validasi Input
    Target: DEFAULT_PENGGUNA_DATA
    """
    assert len(DEFAULT_PENGGUNA_DATA) == 6
    assert DEFAULT_PENGGUNA_DATA[0] == 1
    assert DEFAULT_PENGGUNA_DATA[2] == 'pemilik'
    assert DEFAULT_PENGGUNA_DATA[3] == 'pemilik'
    assert DEFAULT_PENGGUNA_DATA[4] == 0
    assert DEFAULT_PENGGUNA_DATA[5] == 1


def test_konstanta_saldo_ppob_nilai_dan_tipe() -> None:
    """Memverifikasi tipe akun dan nominal saldo awal PPOB sesuai kebutuhan bisnis.

    Skenario: Validasi Input
    Target: DEFAULT_SALDO_PPOB_DATA
    """
    assert len(DEFAULT_SALDO_PPOB_DATA) == 2
    assert DEFAULT_SALDO_PPOB_DATA[0][0] == 'Pulsa_Data'
    assert DEFAULT_SALDO_PPOB_DATA[1][0] == 'Token_Tagihan'
    assert DEFAULT_SALDO_PPOB_DATA[0][1] == Decimal('1000000.0000')
    assert DEFAULT_SALDO_PPOB_DATA[1][1] == Decimal('1500000.0000')
    assert DEFAULT_SALDO_PPOB_DATA[0][2] == 1
    assert DEFAULT_SALDO_PPOB_DATA[1][2] == 1


def test_konstanta_expected_seed_counts_total_dan_keys() -> None:
    """Memverifikasi keakuratan dictionary total baris yang diharapkan per tabel seed.

    Skenario: Validasi Input
    Target: EXPECTED_SEED_COUNTS
    """
    assert len(EXPECTED_SEED_COUNTS) == 7
    assert set(EXPECTED_SEED_COUNTS.keys()) == {'cabang', 'pengguna', 'saldo_ppob', 'saldo_ewallet', 'system_configs', 'satuan_ukur', 'konversi_satuan'}
    assert sum(EXPECTED_SEED_COUNTS.values()) == 49


def test_konstanta_default_password_valid() -> None:
    """Memverifikasi default password bertipe string dan tidak kosong.

    Skenario: Validasi Input
    Target: DEFAULT_PASSWORD
    """
    assert isinstance(DEFAULT_PASSWORD, str)
    assert len(DEFAULT_PASSWORD) > 0
    assert DEFAULT_PASSWORD == 'admin123'


def test_seed_satuan_ukur_default_skip_jika_cukup() -> None:
    """Memverifikasi seed satuan ukur dilewati jika data sudah terisi cukup."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (16,)
    res = seed_satuan_ukur_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 0


def test_seed_satuan_ukur_default_insert_jika_kosong() -> None:
    """Memverifikasi insert satuan ukur jika kosong."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.rowcount = 1
    res = seed_satuan_ukur_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 16


def test_seed_konversi_satuan_default_skip_jika_cukup() -> None:
    """Memverifikasi seed konversi dilewati jika data sudah terisi cukup."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (10,)
    res = seed_konversi_satuan_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 0


def test_seed_konversi_satuan_default_insert_jika_kosong() -> None:
    """Memverifikasi insert konversi jika kosong."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (0,)
    mock_cursor.fetchall.return_value = [
        (1, 'Rim'), (2, 'Lembar'), (3, 'Lusin'), (4, 'Pcs'),
        (5, 'Meter'), (6, 'Centimeter'), (7, 'Liter'), (8, 'Ml'),
        (9, 'Kg'), (10, 'Gram')
    ]
    mock_cursor.rowcount = 1
    res = seed_konversi_satuan_default(mock_cursor)
    assert res.is_success is True
    assert res.data == 10



