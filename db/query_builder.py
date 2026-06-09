"""
Nama Modul: query_builder.py
Deskripsi: Wrapper eksekusi query SQL aman terparameter (%s bindings)
           dan block penjamin atomik ACID transaksi InnoDB.
           Mendukung operasi SELECT, INSERT, UPDATE, DELETE dengan
           penanganan error fungsional Result Pattern.
Author: Claude Sonnet 4.6 (STK-004)
Tanggal: 2026-06-04
"""

# 1. Standard Library
import logging
from collections import namedtuple
from decimal import Decimal
from typing import Callable, Any

# 2. Third-Party
import mysql.connector

# 3. Local Modules
from db.db_connector import get_db_connection
from utils.crypto import decrypt_whatsapp_number

# Logger configuration
_logger = logging.getLogger('abucom.db.query')

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


def execute_query(
    db_connection,
    query: str,
    params: tuple | None = None,
    fetch_one: bool = False,
    fetch_all: bool = True
) -> Result:
    """Mengeksekusi query SQL tunggal dengan parameterized bindings %s.

    Args:
        db_connection: Objek koneksi database aktif dari pool.
        query (str): String query SQL dengan placeholder %s.
        params (tuple | None): Parameter binding untuk query.
        fetch_one (bool): Jika True, hanya mengambil baris pertama hasil SELECT.
        fetch_all (bool): Jika True, mengambil semua baris hasil SELECT (diabaikan jika fetch_one=True).

    Returns:
        Result: NamedTuple berisi status eksekusi query.

    Example:
        >>> conn = get_db_connection().data
        >>> execute_query(conn, "SELECT * FROM pengguna WHERE id = %s", (1,), fetch_one=True)
        Result(is_success=True, data={'id': 1, 'username': 'pemilik_toko'}, error_msg=None)
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(query, params)

        if cursor.description is not None:
            # Query menghasilkan data (SELECT, SHOW, DESCRIBE, dll.)
            if fetch_one:
                data = cursor.fetchone()
            elif fetch_all:
                data = cursor.fetchall()
            else:
                data = None
        else:
            # DML/DDL query (INSERT, UPDATE, DELETE, dll.) yang dieksekusi langsung
            db_connection.commit()
            data = cursor.rowcount

        return Result(True, data, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def execute_acid_transaction(
    db_connection,
    operations: list[Callable[[Any], Any]]
) -> Result:
    """Wrapper fungsional penjamin transaksi ACID rollback/commit InnoDB.

    Args:
        db_connection: Objek koneksi database aktif dari pool.
        operations (list[Callable]): Daftar fungsi operasi yang dieksekusi atomik.
                                     Setiap fungsi menerima satu parameter berupa objek cursor.

    Returns:
        Result: NamedTuple berisi status transaksi dan hasil operasi.

    Example:
        >>> def update_stok(cursor):
        ...     cursor.execute("UPDATE barang SET stok = stok - %s WHERE id = %s", (10, 1))
        ...     return cursor.rowcount
        >>> conn = get_db_connection().data
        >>> execute_acid_transaction(conn, [update_stok])
        Result(is_success=True, data=[1], error_msg=None)
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        db_connection.start_transaction()
        results = [op(cursor) for op in operations]
        db_connection.commit()
        return Result(True, results, None)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception as rollback_err:
            _logger.warning(f"Gagal melakukan rollback: {str(rollback_err)}")
        error_msg = f"ERR-DB-TX: Transaksi dibatalkan secara aman. Detail: {str(e)}"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def execute_insert(
    db_connection,
    query: str,
    params: tuple | None = None
) -> Result:
    """Mengeksekusi INSERT query dan mengembalikan lastrowid.

    Args:
        db_connection: Objek koneksi database aktif.
        query (str): Query INSERT SQL.
        params (tuple | None): Parameter binding untuk query.

    Returns:
        Result: NamedTuple berisi status dan ID baris terakhir (lastrowid).

    Example:
        >>> conn = get_db_connection().data
        >>> execute_insert(conn, "INSERT INTO cabang (nama) VALUES (%s)", ("Cabang Baru",))
        Result(is_success=True, data=2, error_msg=None)
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(query, params)
        db_connection.commit()
        return Result(True, cursor.lastrowid, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi INSERT gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi INSERT gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def execute_many(
    db_connection,
    query: str,
    data_list: list[tuple]
) -> Result:
    """Mengeksekusi INSERT massal menggunakan cursor.executemany().

    Args:
        db_connection: Objek koneksi database aktif.
        query (str): Query INSERT SQL dengan binding %s.
        data_list (list[tuple]): Daftar tuple data yang akan dimasukkan.

    Returns:
        Result: NamedTuple berisi status dan jumlah total baris yang dimasukkan.

    Example:
        >>> conn = get_db_connection().data
        >>> data = [("Barang A",), ("Barang B",)]
        >>> execute_many(conn, "INSERT INTO barang (nama) VALUES (%s)", data)
        Result(is_success=True, data=2, error_msg=None)
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.executemany(query, data_list)
        db_connection.commit()
        return Result(True, cursor.rowcount, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi bulk insert gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi bulk insert gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def execute_with_retry(
    query: str,
    params: tuple | None = None,
    fetch_one: bool = False,
    fetch_all: bool = True,
    max_retries: int = 3
) -> Result:
    """Mengeksekusi query database dengan retry otomatis pada koneksi pool.

    Args:
        query (str): Query SQL.
        params (tuple | None): Parameter query.
        fetch_one (bool): Ambil satu baris saja.
        fetch_all (bool): Ambil semua baris.
        max_retries (int): Maksimum percobaan koneksi.

    Returns:
        Result: NamedTuple berisi status dan hasil eksekusi.

    Example:
        >>> execute_with_retry("SELECT * FROM pengguna WHERE id = %s", (1,), fetch_one=True)
        Result(is_success=True, data={'id': 1, 'username': 'pemilik_toko'}, error_msg=None)
    """
    conn_res = get_db_connection(max_retries=max_retries)
    if not conn_res.is_success:
        return conn_res

    conn = conn_res.data
    try:
        return execute_query(
            db_connection=conn,
            query=query,
            params=params,
            fetch_one=fetch_one,
            fetch_all=fetch_all
        )
    finally:
        try:
            conn.close()  # Mengembalikan koneksi ke pool
        except Exception as e:
            _logger.warning(f"Gagal mengembalikan koneksi ke pool (Detail Error: {str(e)})")


def query_dashboard_pemilik(db_connection, cabang_id: int, tanggal: str) -> Result:
    """Mengambil data agregasi harian untuk dashboard pemilik.

    (Ref: UC-043 Skenario A — Dashboard Pemilik)

    Args:
        db_connection: Objek koneksi database aktif.
        cabang_id (int): ID cabang yang di-query.
        tanggal (str): Tanggal hari ini (YYYY-MM-DD).

    Returns:
        Result: NamedTuple berisi status dan dict data dashboard pemilik.
    """
    cursor = None
    try:
        from decimal import Decimal
        cursor = db_connection.cursor(dictionary=True)

        # a) Total pendapatan hari ini
        query_a = """
            SELECT COALESCE(SUM(total_bayar), 0) AS total_pendapatan
            FROM transaksi
            WHERE DATE(tanggal_transaksi) = %s
              AND status_pembayaran IN ('LUNAS','BELUM LUNAS')
              AND cabang_id = %s
        """
        cursor.execute(query_a, (tanggal, cabang_id))
        res_a = cursor.fetchone()
        total_pendapatan = Decimal(str(res_a['total_pendapatan'])) if res_a else Decimal('0.0000')

        # b) Total pengeluaran hari ini
        query_b = """
            SELECT COALESCE(SUM(nominal), 0) AS total_pengeluaran
            FROM pengeluaran
            WHERE tanggal_pengeluaran = %s AND cabang_id = %s
        """
        cursor.execute(query_b, (tanggal, cabang_id))
        res_b = cursor.fetchone()
        total_pengeluaran = Decimal(str(res_b['total_pengeluaran'])) if res_b else Decimal('0.0000')

        # c) Total kerugian limbah hari ini
        query_c = """
            SELECT COALESCE(SUM(kerugian_nominal), 0) AS total_limbah
            FROM limbah_produksi
            WHERE DATE(tanggal_pencatatan) = %s AND cabang_id = %s
        """
        cursor.execute(query_c, (tanggal, cabang_id))
        res_c = cursor.fetchone()
        total_limbah = Decimal(str(res_c['total_limbah'])) if res_c else Decimal('0.0000')

        # d) Jumlah transaksi per status pembayaran hari ini
        query_d = """
            SELECT status_pembayaran, COUNT(*) AS jumlah
            FROM transaksi
            WHERE DATE(tanggal_transaksi) = %s AND cabang_id = %s
            GROUP BY status_pembayaran
        """
        cursor.execute(query_d, (tanggal, cabang_id))
        status_transaksi = cursor.fetchall()

        # e) Alert jatuh tempo pinjaman bank (H-3)
        query_e = """
            SELECT tipe_bank, setoran_bulanan, tanggal_jatuh_tempo,
                   DATEDIFF(tanggal_jatuh_tempo, CURDATE()) AS sisa_hari
            FROM pinjaman_bank
            WHERE status_pinjaman = 'BELUM LUNAS'
              AND DATEDIFF(tanggal_jatuh_tempo, CURDATE()) <= 3
              AND DATEDIFF(tanggal_jatuh_tempo, CURDATE()) >= 0
              AND cabang_id = %s
        """
        cursor.execute(query_e, (cabang_id,))
        alert_bank = cursor.fetchall()

        # f) Alert jatuh tempo utang supplier (H-3)
        query_f = """
            SELECT s.nama_supplier, u.sisa_utang, u.tanggal_jatuh_tempo,
                   DATEDIFF(u.tanggal_jatuh_tempo, CURDATE()) AS sisa_hari
            FROM utang_supplier u
            JOIN supplier s ON u.supplier_id = s.id
            WHERE u.status_utang = 'BELUM LUNAS'
              AND DATEDIFF(u.tanggal_jatuh_tempo, CURDATE()) <= 3
              AND DATEDIFF(u.tanggal_jatuh_tempo, CURDATE()) >= 0
              AND u.cabang_id = %s
        """
        cursor.execute(query_f, (cabang_id,))
        alert_supplier = cursor.fetchall()

        # Konversi nominal decimal
        for item in alert_bank:
            item['setoran_bulanan'] = Decimal(str(item['setoran_bulanan']))
        for item in alert_supplier:
            item['sisa_utang'] = Decimal(str(item['sisa_utang']))

        data = {
            'total_pendapatan': total_pendapatan,
            'total_pengeluaran': total_pengeluaran,
            'total_limbah': total_limbah,
            'status_transaksi': status_transaksi,
            'alert_bank': alert_bank,
            'alert_supplier': alert_supplier
        }
        return Result(True, data, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard pemilik (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard pemilik (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_dashboard_kasir(db_connection, user_id: int, cabang_id: int, tanggal: str) -> Result:
    """Mengambil data ringkasan harian untuk dashboard kasir.

    (Ref: UC-043 Skenario B — Dashboard Kasir)

    Args:
        db_connection: Objek koneksi database aktif.
        user_id (int): ID pengguna kasir.
        cabang_id (int): ID cabang yang di-query.
        tanggal (str): Tanggal hari ini (YYYY-MM-DD).

    Returns:
        Result: NamedTuple berisi status dan dict data dashboard kasir.
    """
    cursor = None
    try:
        from decimal import Decimal
        cursor = db_connection.cursor(dictionary=True)

        # a) Jumlah & total transaksi shift aktif kasir hari ini
        query_a = """
            SELECT COUNT(*) AS jumlah_nota, COALESCE(SUM(total_bayar), 0) AS total_kas
            FROM transaksi
            WHERE kasir_id = %s AND DATE(tanggal_transaksi) = %s AND cabang_id = %s
        """
        cursor.execute(query_a, (user_id, tanggal, cabang_id))
        res_a = cursor.fetchone()
        jumlah_nota = res_a['jumlah_nota'] if res_a else 0
        total_kas = Decimal(str(res_a['total_kas'])) if res_a else Decimal('0.0000')

        # b) Jumlah invoice BELUM LUNAS (pesanan DP)
        query_b = """
            SELECT COUNT(*) AS jumlah_belum_lunas
            FROM transaksi
            WHERE status_pembayaran = 'BELUM LUNAS'
              AND DATE(tanggal_transaksi) = %s AND cabang_id = %s
        """
        cursor.execute(query_b, (tanggal, cabang_id))
        res_b = cursor.fetchone()
        jumlah_belum_lunas = res_b['jumlah_belum_lunas'] if res_b else 0

        # c) Saldo virtual PPOB (2 akun)
        query_c = """
            SELECT akun_tipe, saldo_terakhir
            FROM saldo_ppob WHERE cabang_id = %s
        """
        cursor.execute(query_c, (cabang_id,))
        saldo_ppob = cursor.fetchall()
        for item in saldo_ppob:
            item['saldo_terakhir'] = Decimal(str(item['saldo_terakhir']))

        data = {
            'jumlah_nota': jumlah_nota,
            'total_kas': total_kas,
            'jumlah_belum_lunas': jumlah_belum_lunas,
            'saldo_ppob': saldo_ppob
        }
        return Result(True, data, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard kasir (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard kasir (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_dashboard_operasional(db_connection, cabang_id: int) -> Result:
    """Mengambil data ringkasan harian untuk dashboard desainer/produksi.

    (Ref: UC-043 Skenario C — Dashboard Desainer/Produksi)

    Args:
        db_connection: Objek koneksi database aktif.
        cabang_id (int): ID cabang yang di-query.

    Returns:
        Result: NamedTuple berisi status dan dict data dashboard operasional.
    """
    cursor = None
    try:
        from decimal import Decimal
        cursor = db_connection.cursor(dictionary=True)

        # a) Jumlah antrian kerja per status
        query_a = """
            SELECT status_antrian, COUNT(*) AS jumlah
            FROM antrian_kerja WHERE cabang_id = %s
            GROUP BY status_antrian
        """
        cursor.execute(query_a, (cabang_id,))
        antrian = cursor.fetchall()

        # b) Alert stok bahan baku kritis
        query_b = """
            SELECT nama_barang, stok_saat_ini, satuan_uom
            FROM barang
            WHERE tipe_barang = 'Bahan_Baku'
              AND stok_saat_ini <= 5.0000
              AND cabang_id = %s
            ORDER BY stok_saat_ini ASC
            LIMIT 10
        """
        cursor.execute(query_b, (cabang_id,))
        stok_kritis = cursor.fetchall()
        for item in stok_kritis:
            item['stok_saat_ini'] = Decimal(str(item['stok_saat_ini']))

        data = {
            'antrian': antrian,
            'stok_kritis': stok_kritis
        }
        return Result(True, data, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard operasional (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard operasional (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_dashboard_kepala(db_connection, cabang_id: int, tanggal: str) -> Result:
    """Mengambil data ringkasan harian untuk dashboard kepala percetakan.

    Args:
        db_connection: Objek koneksi database aktif.
        cabang_id (int): ID cabang yang di-query.
        tanggal (str): Tanggal hari ini (YYYY-MM-DD).

    Returns:
        Result: NamedTuple berisi status dan dict data dashboard kepala.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)

        # a) Jumlah staf hadir hari ini
        query_a = """
            SELECT COUNT(*) AS jumlah_hadir
            FROM absensi
            WHERE tanggal = %s AND status_kehadiran = 'Hadir' AND cabang_id = %s
        """
        cursor.execute(query_a, (tanggal, cabang_id))
        res_a = cursor.fetchone()
        jumlah_hadir = res_a['jumlah_hadir'] if res_a else 0

        # b) Total staf terdaftar
        query_b = """
            SELECT COUNT(*) AS total_staf
            FROM pengguna WHERE cabang_id = %s AND role != 'pemilik'
        """
        cursor.execute(query_b, (cabang_id,))
        res_b = cursor.fetchone()
        total_staf = res_b['total_staf'] if res_b else 0

        # c) Draf stock opname pending approval
        query_c = """
            SELECT COUNT(*) AS draf_pending
            FROM stock_opname
            WHERE status_opname = 'DRAFT' AND cabang_id = %s
        """
        cursor.execute(query_c, (cabang_id,))
        res_c = cursor.fetchone()
        draf_pending = res_c['draf_pending'] if res_c else 0

        # d) Antrian kerja aktif
        query_d = """
            SELECT status_antrian, COUNT(*) AS jumlah
            FROM antrian_kerja WHERE cabang_id = %s
            GROUP BY status_antrian
        """
        cursor.execute(query_d, (cabang_id,))
        antrian = cursor.fetchall()

        data = {
            'jumlah_hadir': jumlah_hadir,
            'total_staf': total_staf,
            'draf_pending': draf_pending,
            'antrian': antrian
        }
        return Result(True, data, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard kepala (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard kepala (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_dashboard_gudang(db_connection, cabang_id: int) -> Result:
    """Mengambil data ringkasan harian untuk dashboard gudang.

    Args:
        db_connection: Objek koneksi database aktif.
        cabang_id (int): ID cabang yang di-query.

    Returns:
        Result: NamedTuple berisi status dan dict data dashboard gudang.
    """
    cursor = None
    try:
        from decimal import Decimal
        cursor = db_connection.cursor(dictionary=True)

        # a) Alert stok bahan baku kritis
        query_a = """
            SELECT nama_barang, stok_saat_ini, satuan_uom
            FROM barang
            WHERE tipe_barang = 'Bahan_Baku'
              AND stok_saat_ini <= 5.0000
              AND cabang_id = %s
            ORDER BY stok_saat_ini ASC
            LIMIT 10
        """
        cursor.execute(query_a, (cabang_id,))
        stok_kritis = cursor.fetchall()
        for item in stok_kritis:
            item['stok_saat_ini'] = Decimal(str(item['stok_saat_ini']))

        # b) Draf stock opname pending
        query_b = """
            SELECT COUNT(*) AS draf_pending
            FROM stock_opname
            WHERE status_opname = 'DRAFT' AND cabang_id = %s
        """
        cursor.execute(query_b, (cabang_id,))
        res_b = cursor.fetchone()
        draf_pending = res_b['draf_pending'] if res_b else 0

        # c) Utang supplier jatuh tempo (H-7)
        query_c = """
            SELECT s.nama_supplier, u.sisa_utang, u.tanggal_jatuh_tempo
            FROM utang_supplier u
            JOIN supplier s ON u.supplier_id = s.id
            WHERE u.status_utang = 'BELUM LUNAS'
              AND DATEDIFF(u.tanggal_jatuh_tempo, CURDATE()) <= 7
              AND u.cabang_id = %s
            ORDER BY u.tanggal_jatuh_tempo ASC
        """
        cursor.execute(query_c, (cabang_id,))
        utang_supplier = cursor.fetchall()
        for item in utang_supplier:
            item['sisa_utang'] = Decimal(str(item['sisa_utang']))

        data = {
            'stok_kritis': stok_kritis,
            'draf_pending': draf_pending,
            'utang_supplier': utang_supplier
        }
        return Result(True, data, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard gudang (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard gudang (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_dashboard_pramuniaga(db_connection, cabang_id: int) -> Result:
    """Mengambil data ringkasan harian untuk dashboard pramuniaga.

    Args:
        db_connection: Objek koneksi database aktif.
        cabang_id (int): ID cabang yang di-query.

    Returns:
        Result: NamedTuple berisi status dan dict data dashboard pramuniaga.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)

        query = """
            SELECT COUNT(*) AS jumlah_antri
            FROM antrian_kerja
            WHERE status_antrian = 'Antri' AND cabang_id = %s
        """
        cursor.execute(query, (cabang_id,))
        res = cursor.fetchone()
        jumlah_antri = res['jumlah_antri'] if res else 0

        data = {
            'jumlah_antri': jumlah_antri
        }
        return Result(True, data, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard pramuniaga (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard pramuniaga (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_dashboard_fotocopy(db_connection, user_id: int, cabang_id: int, tanggal: str) -> Result:
    """Mengambil data ringkasan harian untuk dashboard fotocopy_print.

    Args:
        db_connection: Objek koneksi database aktif.
        user_id (int): ID pengguna fotocopy_print.
        cabang_id (int): ID cabang yang di-query.
        tanggal (str): Tanggal hari ini (YYYY-MM-DD).

    Returns:
        Result: NamedTuple berisi status dan dict data dashboard fotocopy_print.
    """
    cursor = None
    try:
        from decimal import Decimal
        cursor = db_connection.cursor(dictionary=True)

        query = """
            SELECT COUNT(*) AS jumlah_nota, COALESCE(SUM(total_bayar), 0) AS total_kas
            FROM transaksi
            WHERE kasir_id = %s AND DATE(tanggal_transaksi) = %s AND cabang_id = %s
        """
        cursor.execute(query, (user_id, tanggal, cabang_id))
        res = cursor.fetchone()
        jumlah_nota = res['jumlah_nota'] if res else 0
        total_kas = Decimal(str(res['total_kas'])) if res else Decimal('0.0000')

        data = {
            'jumlah_nota': jumlah_nota,
            'total_kas': total_kas
        }
        return Result(True, data, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard fotocopy (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil data dashboard fotocopy (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_daftar_barang(
    db_connection,
    cabang_id: int,
    tipe_barang: str | None = None,
    keyword: str | None = None
) -> Result:
    """Mengambil daftar master barang dengan filter opsional.

    Args:
        db_connection: Objek koneksi database aktif dari pool.
        cabang_id (int): ID cabang untuk filter multi-branch.
        tipe_barang (str | None): Filter opsional 'Retail_ATK' atau 'Bahan_Baku'.
        keyword (str | None): Kata kunci pencarian parsial pada kolom nama_barang.

    Returns:
        Result: NamedTuple (is_success, data: list[dict], error_msg).
    """
    cursor = None
    try:
        from decimal import Decimal
        cursor = db_connection.cursor(dictionary=True)
        query = """
            SELECT id, nama_barang, tipe_barang, satuan_uom, stok_saat_ini,
                   harga_beli, harga_retail, harga_grosir, min_grosir, harga_mitra
            FROM barang
            WHERE cabang_id = %s
        """
        params = [cabang_id]
        if tipe_barang:
            query += " AND tipe_barang = %s"
            params.append(tipe_barang)
        if keyword:
            query += " AND nama_barang LIKE CONCAT('%', %s, '%')"
            params.append(keyword)
        
        query += " ORDER BY tipe_barang ASC, nama_barang ASC"
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()
        
        # Convert DECIMAL columns to Decimal
        for row in rows:
            for col in ['stok_saat_ini', 'harga_beli', 'harga_retail', 'harga_grosir', 'min_grosir', 'harga_mitra']:
                if row[col] is not None:
                    row[col] = Decimal(str(row[col]))
                    
        return Result(True, rows, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_detail_barang(
    db_connection,
    barang_id: int,
    cabang_id: int
) -> Result:
    """Mengambil detail lengkap satu barang beserta info BOM terkait.

    Args:
        db_connection: Objek koneksi database aktif.
        barang_id (int): ID barang yang akan ditampilkan.
        cabang_id (int): ID cabang untuk filter multi-branch.

    Returns:
        Result: NamedTuple (is_success, data: dict | None, error_msg).
    """
    cursor = None
    try:
        from decimal import Decimal
        cursor = db_connection.cursor(dictionary=True)
        query = """
            SELECT id, nama_barang, tipe_barang, satuan_uom, stok_saat_ini,
                   harga_beli, harga_retail, harga_grosir, min_grosir, harga_mitra,
                   created_at, updated_at
            FROM barang
            WHERE id = %s AND cabang_id = %s
        """
        cursor.execute(query, (barang_id, cabang_id))
        barang = cursor.fetchone()
        
        if not barang:
            return Result(True, None, None)
            
        for col in ['stok_saat_ini', 'harga_beli', 'harga_retail', 'harga_grosir', 'min_grosir', 'harga_mitra']:
            if barang[col] is not None:
                barang[col] = Decimal(str(barang[col]))
                
        # Query BOM Terkait
        query_bom = """
            SELECT bc.id, bc.bahan_baku_id, b.nama_barang AS nama_bahan,
                   bc.kuantitas_desimal, b.harga_beli, b.satuan_uom
            FROM bom_komposisi bc
            JOIN barang b ON bc.bahan_baku_id = b.id
            WHERE bc.barang_induk_id = %s AND bc.cabang_id = %s
        """
        cursor.execute(query_bom, (barang_id, cabang_id))
        bom_rows = cursor.fetchall()
        
        for row in bom_rows:
            if row['kuantitas_desimal'] is not None:
                row['kuantitas_desimal'] = Decimal(str(row['kuantitas_desimal']))
            if row['harga_beli'] is not None:
                row['harga_beli'] = Decimal(str(row['harga_beli']))
                
        return Result(True, {'barang': barang, 'bom_komponen': bom_rows}, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_insert_barang(
    db_connection,
    data_barang: dict
) -> Result:
    """Menyisipkan satu baris data barang baru ke tabel master.

    Args:
        db_connection: Objek koneksi database aktif.
        data_barang (dict): Dictionary berisi kolom-kolom barang.

    Returns:
        Result: NamedTuple (is_success, data: int (lastrowid), error_msg).
    """
    query = """
        INSERT INTO barang (
            nama_barang, tipe_barang, satuan_uom, stok_saat_ini,
            harga_beli, harga_retail, harga_grosir, min_grosir, harga_mitra, cabang_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        data_barang['nama_barang'],
        data_barang['tipe_barang'],
        data_barang['satuan_uom'],
        data_barang['stok_saat_ini'],
        data_barang['harga_beli'],
        data_barang['harga_retail'],
        data_barang['harga_grosir'],
        data_barang['min_grosir'],
        data_barang['harga_mitra'],
        data_barang['cabang_id']
    )
    return execute_insert(db_connection, query, params)


def query_update_barang(
    db_connection,
    barang_id: int,
    data_update: dict,
    cabang_id: int
) -> Result:
    """Memperbarui kolom-kolom master data barang yang sudah ada.

    Args:
        db_connection: Objek koneksi database aktif.
        barang_id (int): ID barang target update.
        data_update (dict): Dictionary berisi kolom yang diubah beserta nilai barunya.
        cabang_id (int): Filter multi-branch wajib pada klausa WHERE.

    Returns:
        Result: NamedTuple (is_success, data: int (rowcount), error_msg).
    """
    if not data_update:
        return Result(True, 0, None)
        
    set_clauses = []
    params = []
    for key, val in data_update.items():
        set_clauses.append(f"{key} = %s")
        params.append(val)
        
    query = f"UPDATE barang SET {', '.join(set_clauses)} WHERE id = %s AND cabang_id = %s"
    params.extend([barang_id, cabang_id])
    
    return execute_query(db_connection, query, tuple(params))


def query_delete_barang(
    db_connection,
    barang_id: int,
    cabang_id: int
) -> Result:
    """Menghapus satu baris barang dari tabel master.

    Args:
        db_connection: Objek koneksi database aktif.
        barang_id (int): ID barang yang akan dihapus.
        cabang_id (int): Filter multi-branch wajib pada klausa WHERE.

    Returns:
        Result: NamedTuple (is_success, data: int (rowcount), error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = "DELETE FROM barang WHERE id = %s AND cabang_id = %s"
        cursor.execute(query, (barang_id, cabang_id))
        db_connection.commit()
        return Result(True, cursor.rowcount, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        if e.errno == 1451:
            error_msg = "ERR-FK-005: Barang tidak dapat dihapus karena masih digunakan dalam formula BOM!"
        else:
            error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_cek_nama_barang_duplikat(
    db_connection,
    nama_barang: str,
    cabang_id: int,
    exclude_id: int | None = None
) -> Result:
    """Mengecek apakah nama barang sudah terdaftar di cabang yang sama.

    Args:
        db_connection: Objek koneksi database aktif.
        nama_barang (str): Nama barang yang akan dicek keunikannya.
        cabang_id (int): ID cabang untuk scope pengecekan.
        exclude_id (int | None): ID barang yang dikecualikan (untuk skenario update).

    Returns:
        Result: NamedTuple (is_success, data: bool (True jika duplikat), error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = "SELECT COUNT(*) AS cnt FROM barang WHERE nama_barang = %s AND cabang_id = %s"
        params = [nama_barang, cabang_id]
        if exclude_id is not None:
            query += " AND id != %s"
            params.append(exclude_id)
            
        cursor.execute(query, params)
        res = cursor.fetchone()
        count = res['cnt'] if res else 0
        return Result(True, count > 0, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


# --- SATUAN UKUR CRUD ---

def fetch_all_satuan_ukur(db_connection, cabang_id: int) -> Result:
    """Mengambil seluruh data master satuan ukur aktif untuk satu cabang."""
    query = """
        SELECT id, nama_satuan, kategori_satuan, simbol, keterangan, is_aktif
        FROM satuan_ukur
        WHERE cabang_id = %s AND is_aktif = TRUE
        ORDER BY kategori_satuan, nama_satuan
    """
    return execute_query(db_connection, query, (cabang_id,), fetch_all=True)


def fetch_satuan_ukur_by_id(db_connection, satuan_id: int, cabang_id: int) -> Result:
    """Mengambil satu record satuan ukur berdasarkan ID."""
    query = """
        SELECT id, nama_satuan, kategori_satuan, simbol, keterangan, is_aktif
        FROM satuan_ukur
        WHERE id = %s AND cabang_id = %s
    """
    return execute_query(db_connection, query, (satuan_id, cabang_id), fetch_one=True)


def fetch_satuan_ukur_by_nama(db_connection, nama_satuan: str, cabang_id: int) -> Result:
    """Mengambil satu record satuan ukur berdasarkan nama (untuk validasi duplikasi)."""
    query = """
        SELECT id, nama_satuan, kategori_satuan, simbol, keterangan, is_aktif
        FROM satuan_ukur
        WHERE nama_satuan = %s AND cabang_id = %s
    """
    return execute_query(db_connection, query, (nama_satuan, cabang_id), fetch_one=True)


def insert_satuan_ukur(db_connection, data: dict, cabang_id: int) -> Result:
    """Menyimpan satuan ukur baru ke database."""
    query = """
        INSERT INTO satuan_ukur (nama_satuan, kategori_satuan, simbol, keterangan, cabang_id)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (
        data['nama_satuan'],
        data['kategori_satuan'],
        data.get('simbol', ''),
        data.get('keterangan', ''),
        cabang_id
    )
    return execute_insert(db_connection, query, params)


def update_satuan_ukur(db_connection, satuan_id: int, data: dict, cabang_id: int) -> Result:
    """Memperbarui data satuan ukur yang sudah ada."""
    set_clauses = []
    params = []
    for key, val in data.items():
        set_clauses.append(f"{key} = %s")
        params.append(val)
    query = f"UPDATE satuan_ukur SET {', '.join(set_clauses)} WHERE id = %s AND cabang_id = %s"
    params.extend([satuan_id, cabang_id])
    return execute_query(db_connection, query, tuple(params))


def soft_delete_satuan_ukur(db_connection, satuan_id: int, cabang_id: int) -> Result:
    """Menonaktifkan satuan ukur (set is_aktif = FALSE). Cek dulu apakah masih dipakai di tabel barang."""
    check_query = """
        SELECT COUNT(*) AS cnt 
        FROM barang 
        WHERE satuan_uom = (SELECT nama_satuan FROM satuan_ukur WHERE id = %s) AND cabang_id = %s
    """
    check_res = execute_query(db_connection, check_query, (satuan_id, cabang_id), fetch_one=True)
    if not check_res.is_success:
        return check_res
    if check_res.data and check_res.data['cnt'] > 0:
        return Result(False, None, "ERR-UOM-005: Satuan tidak dapat dinonaktifkan karena masih digunakan")

    query = "UPDATE satuan_ukur SET is_aktif = FALSE WHERE id = %s AND cabang_id = %s"
    return execute_query(db_connection, query, (satuan_id, cabang_id))


# --- KONVERSI SATUAN CRUD ---

def fetch_all_konversi_satuan(db_connection, cabang_id: int) -> Result:
    """Mengambil seluruh aturan konversi dengan JOIN ke nama satuan."""
    query = """
        SELECT ks.id, ks.satuan_asal_id, ks.satuan_tujuan_id,
               sa.nama_satuan AS satuan_asal, st.nama_satuan AS satuan_tujuan, 
               ks.faktor_konversi
        FROM konversi_satuan ks
        JOIN satuan_ukur sa ON ks.satuan_asal_id = sa.id
        JOIN satuan_ukur st ON ks.satuan_tujuan_id = st.id
        WHERE ks.cabang_id = %s
        ORDER BY sa.nama_satuan, st.nama_satuan
    """
    res = execute_query(db_connection, query, (cabang_id,), fetch_all=True)
    if res.is_success and res.data:
        from decimal import Decimal
        for row in res.data:
            if row['faktor_konversi'] is not None:
                row['faktor_konversi'] = Decimal(str(row['faktor_konversi']))
    return res


def fetch_konversi_by_pasangan(db_connection, satuan_asal_id: int, satuan_tujuan_id: int, cabang_id: int) -> Result:
    """Mengambil faktor konversi antara dua satuan spesifik."""
    query = """
        SELECT id, satuan_asal_id, satuan_tujuan_id, faktor_konversi
        FROM konversi_satuan
        WHERE satuan_asal_id = %s AND satuan_tujuan_id = %s AND cabang_id = %s
    """
    res = execute_query(db_connection, query, (satuan_asal_id, satuan_tujuan_id, cabang_id), fetch_one=True)
    if res.is_success and res.data:
        from decimal import Decimal
        if res.data['faktor_konversi'] is not None:
            res.data['faktor_konversi'] = Decimal(str(res.data['faktor_konversi']))
    return res


def insert_konversi_satuan(db_connection, data: dict, cabang_id: int) -> Result:
    """Menyimpan aturan konversi baru. Otomatis buat konversi balik (inverse)."""
    satuan_asal_id = int(data['satuan_asal_id'])
    satuan_tujuan_id = int(data['satuan_tujuan_id'])
    
    from decimal import Decimal, ROUND_HALF_UP
    try:
        faktor_konversi = Decimal(str(data['faktor_konversi']))
        if faktor_konversi <= 0:
            return Result(False, None, "ERR-UOM-004: Faktor konversi harus lebih besar dari nol")
        faktor_balik = (Decimal('1') / faktor_konversi).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    except Exception as e:
        return Result(False, None, f"ERR-UOM-004: Faktor konversi tidak valid. {str(e)}")

    def op_insert_direct(cursor):
        query = """
            INSERT INTO konversi_satuan (satuan_asal_id, satuan_tujuan_id, faktor_konversi, cabang_id)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (satuan_asal_id, satuan_tujuan_id, faktor_konversi, cabang_id))
        return cursor.lastrowid

    def op_insert_inverse(cursor):
        query = """
            INSERT INTO konversi_satuan (satuan_asal_id, satuan_tujuan_id, faktor_konversi, cabang_id)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (satuan_tujuan_id, satuan_asal_id, faktor_balik, cabang_id))
        return cursor.lastrowid

    existing = fetch_konversi_by_pasangan(db_connection, satuan_asal_id, satuan_tujuan_id, cabang_id)
    if existing.is_success and existing.data:
        return Result(False, None, "ERR-UOM-006: Aturan konversi sudah ada untuk pasangan satuan ini")

    return execute_acid_transaction(db_connection, [op_insert_direct, op_insert_inverse])


def update_konversi_satuan(db_connection, konversi_id: int, faktor_baru: Decimal, cabang_id: int) -> Result:
    """Memperbarui faktor konversi yang sudah ada. Otomatis update konversi balik."""
    query_select = "SELECT satuan_asal_id, satuan_tujuan_id FROM konversi_satuan WHERE id = %s AND cabang_id = %s"
    res_select = execute_query(db_connection, query_select, (konversi_id, cabang_id), fetch_one=True)
    if not res_select.is_success or not res_select.data:
        return Result(False, None, "ERR-UOM-001: Konversi tidak ditemukan")

    satuan_asal_id = res_select.data['satuan_asal_id']
    satuan_tujuan_id = res_select.data['satuan_tujuan_id']

    from decimal import Decimal, ROUND_HALF_UP
    try:
        faktor_konversi = Decimal(str(faktor_baru))
        if faktor_konversi <= 0:
            return Result(False, None, "ERR-UOM-004: Faktor konversi harus lebih besar dari nol")
        faktor_balik = (Decimal('1') / faktor_konversi).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    except Exception as e:
        return Result(False, None, f"ERR-UOM-004: Faktor konversi tidak valid. {str(e)}")

    def op_update_direct(cursor):
        query = "UPDATE konversi_satuan SET faktor_konversi = %s WHERE id = %s AND cabang_id = %s"
        cursor.execute(query, (faktor_konversi, konversi_id, cabang_id))
        return cursor.rowcount

    def op_update_inverse(cursor):
        query = "UPDATE konversi_satuan SET faktor_konversi = %s WHERE satuan_asal_id = %s AND satuan_tujuan_id = %s AND cabang_id = %s"
        cursor.execute(query, (faktor_balik, satuan_tujuan_id, satuan_asal_id, cabang_id))
        return cursor.rowcount

    return execute_acid_transaction(db_connection, [op_update_direct, op_update_inverse])


def delete_konversi_satuan(db_connection, konversi_id: int, cabang_id: int) -> Result:
    """Menghapus aturan konversi (hard delete, beserta konversi baliknya)."""
    query_select = "SELECT satuan_asal_id, satuan_tujuan_id FROM konversi_satuan WHERE id = %s AND cabang_id = %s"
    res_select = execute_query(db_connection, query_select, (konversi_id, cabang_id), fetch_one=True)
    if not res_select.is_success or not res_select.data:
        return Result(False, None, "ERR-UOM-001: Konversi tidak ditemukan")

    satuan_asal_id = res_select.data['satuan_asal_id']
    satuan_tujuan_id = res_select.data['satuan_tujuan_id']

    def op_delete_direct(cursor):
        query = "DELETE FROM konversi_satuan WHERE id = %s AND cabang_id = %s"
        cursor.execute(query, (konversi_id, cabang_id))
        return cursor.rowcount

    def op_delete_inverse(cursor):
        query = "DELETE FROM konversi_satuan WHERE satuan_asal_id = %s AND satuan_tujuan_id = %s AND cabang_id = %s"
        cursor.execute(query, (satuan_tujuan_id, satuan_asal_id, cabang_id))
        return cursor.rowcount

    return execute_acid_transaction(db_connection, [op_delete_direct, op_delete_inverse])


def is_satuan_valid(db_connection, nama_satuan: str, cabang_id: int) -> bool:
    """Mengecek apakah nama satuan terdaftar dan aktif di master satuan_ukur."""
    query = "SELECT COUNT(*) AS cnt FROM satuan_ukur WHERE nama_satuan = %s AND cabang_id = %s AND is_aktif = TRUE"
    res = execute_query(db_connection, query, (nama_satuan, cabang_id), fetch_one=True)
    if res.is_success and res.data:
        return res.data['cnt'] > 0
    return False


def query_daftar_bom_by_induk(db_connection, barang_induk_id: int, cabang_id: int) -> Result:
    """Mengambil daftar komposisi BOM berdasarkan produk induk.

    Args:
        db_connection: Objek koneksi database aktif.
        barang_induk_id (int): ID barang induk.
        cabang_id (int): ID cabang filter.

    Returns:
        Result: NamedTuple (is_success, data: list[dict], error_msg).
    """
    cursor = None
    try:
        from decimal import Decimal
        cursor = db_connection.cursor(dictionary=True)
        query = """
            SELECT bc.id, bc.bahan_baku_id, b.nama_barang, b.satuan_uom, 
                   bc.kuantitas_desimal, b.harga_beli, b.stok_saat_ini,
                   bc.created_at, bc.updated_at
            FROM bom_komposisi bc
            JOIN barang b ON bc.bahan_baku_id = b.id
            WHERE bc.barang_induk_id = %s AND bc.cabang_id = %s
            ORDER BY bc.id ASC
        """
        cursor.execute(query, (barang_induk_id, cabang_id))
        rows = cursor.fetchall()
        for row in rows:
            for col in ['kuantitas_desimal', 'harga_beli', 'stok_saat_ini']:
                if row[col] is not None:
                    row[col] = Decimal(str(row[col]))
        return Result(True, rows, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil daftar BOM (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil daftar BOM (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_insert_bom_komponen(
    db_connection, 
    barang_induk_id: int, 
    bahan_baku_id: int, 
    kuantitas_desimal: Any, 
    cabang_id: int
) -> Result:
    """Menyisipkan komponen BOM baru ke database.

    Args:
        db_connection: Objek koneksi database aktif.
        barang_induk_id (int): ID barang induk.
        bahan_baku_id (int): ID bahan baku.
        kuantitas_desimal (Decimal): Kuantitas bahan baku.
        cabang_id (int): ID cabang.

    Returns:
        Result: NamedTuple (is_success, data: int (lastrowid), error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = """
            INSERT INTO bom_komposisi (barang_induk_id, bahan_baku_id, kuantitas_desimal, cabang_id)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (barang_induk_id, bahan_baku_id, kuantitas_desimal, cabang_id))
        db_connection.commit()
        return Result(True, cursor.lastrowid, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        if e.errno == 1062:
            error_msg = "ERR-BOM-001: Bahan baku ini sudah terdaftar dalam formula BOM produk ini!"
        else:
            error_msg = f"ERR-DB-007: Kegagalan database saat proses penyimpanan formula BOM! (MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-007: Kegagalan database saat proses penyimpanan formula BOM! (Detail: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_update_bom_kuantitas(db_connection, bom_id: int, kuantitas_baru: Any, cabang_id: int) -> Result:
    """Memperbarui kuantitas pemakaian desimal bahan baku dalam formula BOM.

    Args:
        db_connection: Objek koneksi database aktif.
        bom_id (int): ID baris komposisi BOM.
        kuantitas_baru (Decimal): Nilai kuantitas baru.
        cabang_id (int): ID cabang.

    Returns:
        Result: NamedTuple (is_success, data: int (bom_id), error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = """
            UPDATE bom_komposisi 
            SET kuantitas_desimal = %s 
            WHERE id = %s AND cabang_id = %s
        """
        cursor.execute(query, (kuantitas_baru, bom_id, cabang_id))
        if cursor.rowcount == 0:
            return Result(False, None, "ERR-BOM-002: Data komposisi BOM tidak ditemukan!")
        db_connection.commit()
        return Result(True, bom_id, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Gagal memperbarui kuantitas BOM (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Gagal memperbarui kuantitas BOM (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_delete_bom_komponen(db_connection, bom_id: int, cabang_id: int) -> Result:
    """Menghapus komponen bahan baku dari formula BOM.

    Args:
        db_connection: Objek koneksi database aktif.
        bom_id (int): ID baris komposisi BOM.
        cabang_id (int): ID cabang.

    Returns:
        Result: NamedTuple (is_success, data: int (bom_id), error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = """
            DELETE FROM bom_komposisi 
            WHERE id = %s AND cabang_id = %s
        """
        cursor.execute(query, (bom_id, cabang_id))
        if cursor.rowcount == 0:
            return Result(False, None, "ERR-BOM-003: Data komposisi BOM tidak ditemukan atau sudah dihapus!")
        db_connection.commit()
        return Result(True, bom_id, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Gagal menghapus komponen BOM (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Gagal menghapus komponen BOM (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_detail_bom_by_id(db_connection, bom_id: int, cabang_id: int) -> Result:
    """Mengambil detail satu baris komposisi BOM berdasarkan ID.

    Args:
        db_connection: Objek koneksi database aktif.
        bom_id (int): ID baris komposisi BOM.
        cabang_id (int): ID cabang.

    Returns:
        Result: NamedTuple (is_success, data: dict, error_msg).
    """
    cursor = None
    try:
        from decimal import Decimal
        cursor = db_connection.cursor(dictionary=True)
        query = """
            SELECT bc.id, bc.barang_induk_id, bc.bahan_baku_id, b.nama_barang, 
                   b.satuan_uom, bc.kuantitas_desimal, b.harga_beli,
                   bc.created_at, bc.updated_at
            FROM bom_komposisi bc
            JOIN barang b ON bc.bahan_baku_id = b.id
            WHERE bc.id = %s AND bc.cabang_id = %s
        """
        cursor.execute(query, (bom_id, cabang_id))
        row = cursor.fetchone()
        if not row:
            return Result(False, None, "ERR-BOM-002: Data komposisi BOM tidak ditemukan!")
        for col in ['kuantitas_desimal', 'harga_beli']:
            if row[col] is not None:
                row[col] = Decimal(str(row[col]))
        return Result(True, row, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil detail BOM (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil detail BOM (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_daftar_barang_bahan_baku(db_connection, cabang_id: int) -> Result:
    """Mengambil daftar master barang yang bertipe Bahan_Baku atau Retail_ATK.

    Args:
        db_connection: Objek koneksi database aktif.
        cabang_id (int): ID cabang.

    Returns:
        Result: NamedTuple (is_success, data: list[dict], error_msg).
    """
    cursor = None
    try:
        from decimal import Decimal
        cursor = db_connection.cursor(dictionary=True)
        query = """
            SELECT id, nama_barang, tipe_barang, satuan_uom, stok_saat_ini, harga_beli
            FROM barang
            WHERE cabang_id = %s AND tipe_barang IN ('Bahan_Baku', 'Retail_ATK')
            ORDER BY nama_barang ASC
        """
        cursor.execute(query, (cabang_id,))
        rows = cursor.fetchall()
        for row in rows:
            for col in ['stok_saat_ini', 'harga_beli']:
                if row[col] is not None:
                    row[col] = Decimal(str(row[col]))
        return Result(True, rows, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil daftar bahan baku (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil daftar bahan baku (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_validasi_barang_induk(db_connection, barang_induk_id: int, cabang_id: int) -> Result:
    """Memvalidasi barang induk produk kustom.

    Args:
        db_connection: Objek koneksi database aktif.
        barang_induk_id (int): ID barang induk.
        cabang_id (int): ID cabang.

    Returns:
        Result: NamedTuple (is_success, data: dict, error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = """
            SELECT id, nama_barang, tipe_barang 
            FROM barang 
            WHERE id = %s AND cabang_id = %s
        """
        cursor.execute(query, (barang_induk_id, cabang_id))
        row = cursor.fetchone()
        if not row:
            return Result(False, None, "ERR-VAL-008: Barang induk tidak ditemukan!")
        return Result(True, row, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal memvalidasi barang induk (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal memvalidasi barang induk (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_daftar_supplier(db_connection, cabang_id: int) -> Result:
    """Mengambil seluruh data supplier berdasarkan cabang.

    (Ref: Module Structure Bab 4.4, SRS-F-015)

    Args:
        db_connection: Koneksi database MySQL aktif.
        cabang_id (int): ID cabang filter.

    Returns:
        Result: NamedTuple berisi is_success, data (list[dict]), error_msg.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = (
            "SELECT id, nama_supplier, alamat, telp, email, created_at, updated_at "
            "FROM supplier "
            "WHERE cabang_id = %s "
            "ORDER BY nama_supplier ASC"
        )
        cursor.execute(query, (cabang_id,))
        rows = cursor.fetchall()
        return Result(True, rows if rows else [], None)
    except Exception as e:
        return Result(False, None, f"ERR-DB-136: Gagal mengambil daftar supplier. Detail: {str(e)}")
    finally:
        if cursor:
            cursor.close()


def query_detail_supplier(db_connection, supplier_id: int, cabang_id: int) -> Result:
    """Mengambil detail data supplier berdasarkan ID dan cabang.

    (Ref: Module Structure Bab 4.4, SRS-F-015, ERR-VAL-013)

    Args:
        db_connection: Koneksi database MySQL aktif.
        supplier_id (int): ID supplier.
        cabang_id (int): ID cabang filter.

    Returns:
        Result: NamedTuple berisi is_success, data (dict), error_msg.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = (
            "SELECT id, nama_supplier, alamat, telp, email, cabang_id, created_at, updated_at "
            "FROM supplier "
            "WHERE id = %s AND cabang_id = %s"
        )
        cursor.execute(query, (supplier_id, cabang_id))
        row = cursor.fetchone()
        if not row:
            return Result(False, None, "⛔ ERR-VAL-013: ID supplier tidak terdaftar di database master!")
        return Result(True, row, None)
    except Exception as e:
        return Result(False, None, f"ERR-DB-136: Gagal mengambil detail supplier. Detail: {str(e)}")
    finally:
        if cursor:
            cursor.close()


def query_insert_supplier(db_connection, nama_supplier: str, alamat: str, telp: str, email: str, cabang_id: int) -> Result:
    """Menambahkan data supplier baru.

    (Ref: Module Structure Bab 4.4, SRS-F-015)

    Args:
        db_connection: Koneksi database MySQL aktif.
        nama_supplier (str): Nama supplier.
        alamat (str): Alamat supplier.
        telp (str): Nomor telepon supplier.
        email (str): Email supplier.
        cabang_id (int): ID cabang pemilik data.

    Returns:
        Result: NamedTuple berisi is_success, data (int: last_insert_id), error_msg.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = (
            "INSERT INTO supplier (nama_supplier, alamat, telp, email, cabang_id) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(query, (nama_supplier, alamat, telp, email, cabang_id))
        db_connection.commit()
        last_id = cursor.lastrowid
        return Result(True, last_id, None)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        return Result(False, None, f"ERR-DB-136: Gagal menambahkan supplier baru. Detail: {str(e)}")
    finally:
        if cursor:
            cursor.close()


def query_update_supplier(db_connection, supplier_id: int, nama_supplier: str, alamat: str, telp: str, email: str, cabang_id: int) -> Result:
    """Memperbarui data supplier.

    (Ref: Module Structure Bab 4.4, SRS-F-015)

    Args:
        db_connection: Koneksi database MySQL aktif.
        supplier_id (int): ID supplier yang akan diedit.
        nama_supplier (str): Nama supplier baru.
        alamat (str): Alamat supplier baru.
        telp (str): Nomor telepon supplier baru.
        email (str): Email supplier baru.
        cabang_id (int): ID cabang pemilik data.

    Returns:
        Result: NamedTuple berisi is_success, data (int: rows_affected), error_msg.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = (
            "UPDATE supplier "
            "SET nama_supplier = %s, alamat = %s, telp = %s, email = %s "
            "WHERE id = %s AND cabang_id = %s"
        )
        cursor.execute(query, (nama_supplier, alamat, telp, email, supplier_id, cabang_id))
        db_connection.commit()
        rows_affected = cursor.rowcount
        return Result(True, rows_affected, None)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        return Result(False, None, f"ERR-DB-136: Gagal mengubah data supplier. Detail: {str(e)}")
    finally:
        if cursor:
            cursor.close()


def query_delete_supplier(db_connection, supplier_id: int, cabang_id: int) -> Result:
    """Menghapus data supplier secara permanen setelah memvalidasi relasi.

    (Ref: Module Structure Bab 4.4, SRS-F-015, ERR-REL-136)

    Args:
        db_connection: Koneksi database MySQL aktif.
        supplier_id (int): ID supplier yang akan dihapus.
        cabang_id (int): ID cabang pemilik data.

    Returns:
        Result: NamedTuple berisi is_success, data (int: rows_affected), error_msg.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        
        # 1. Cek relasi ke utang_supplier yang masih BELUM LUNAS
        query_check_utang = (
            "SELECT count "
            "FROM (SELECT COUNT(*) as count FROM utang_supplier WHERE supplier_id = %s AND cabang_id = %s AND status_utang = 'BELUM LUNAS') as t"
        )
        # Wait, the DDL has utang_supplier table. We can just run:
        query_check_utang = (
            "SELECT COUNT(*) as count "
            "FROM utang_supplier "
            "WHERE supplier_id = %s AND cabang_id = %s AND status_utang = 'BELUM LUNAS'"
        )
        cursor.execute(query_check_utang, (supplier_id, cabang_id))
        res_utang = cursor.fetchone()
        if res_utang and res_utang['count'] > 0:
            return Result(False, None, "⛔ ERR-REL-136: Supplier tidak dapat dihapus karena masih memiliki utang aktif yang belum lunas!")

        # 2. Cek relasi ke riwayat_harga_supplier (Warning, tapi izinkan delete)
        # Note: Tabel riwayat_harga_supplier mungkin belum ada di DDL, handle error jika table tidak ada.
        has_riwayat = False
        try:
            query_check_riwayat = (
                "SELECT COUNT(*) as count "
                "FROM riwayat_harga_supplier "
                "WHERE supplier_id = %s"
            )
            cursor.execute(query_check_riwayat, (supplier_id,))
            res_riwayat = cursor.fetchone()
            if res_riwayat and res_riwayat['count'] > 0:
                has_riwayat = True
        except Exception:
            pass
            
        # 3. Lakukan hard delete
        query_delete = "DELETE FROM supplier WHERE id = %s AND cabang_id = %s"
        cursor.execute(query_delete, (supplier_id, cabang_id))
        db_connection.commit()
        rows_affected = cursor.rowcount
        
        return Result(True, rows_affected, None)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        return Result(False, None, f"ERR-DB-136: Gagal menghapus supplier. Detail: {str(e)}")
    finally:
        if cursor:
            cursor.close()


def query_cek_nama_supplier_duplikat(db_connection, nama_supplier: str, cabang_id: int, exclude_id: int | None = None) -> Result:
    """Mengecek apakah nama supplier sudah terdaftar di cabang yang sama (case-insensitive).

    (Ref: Module Structure Bab 4.4, SRS-F-015)

    Args:
        db_connection: Koneksi database MySQL aktif.
        nama_supplier (str): Nama supplier yang dicek.
        cabang_id (int): ID cabang filter.
        exclude_id (int | None): ID supplier yang diabaikan (untuk edit).

    Returns:
        Result: NamedTuple berisi is_success, data (dict data supplier if duplicate, None otherwise), error_msg.
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        if exclude_id is not None:
            query = (
                "SELECT id, nama_supplier, alamat, telp, email, cabang_id "
                "FROM supplier "
                "WHERE LOWER(nama_supplier) = LOWER(%s) AND cabang_id = %s AND id != %s"
            )
            cursor.execute(query, (nama_supplier, cabang_id, exclude_id))
        else:
            query = (
                "SELECT id, nama_supplier, alamat, telp, email, cabang_id "
                "FROM supplier "
                "WHERE LOWER(nama_supplier) = LOWER(%s) AND cabang_id = %s"
            )
            cursor.execute(query, (nama_supplier, cabang_id))
        row = cursor.fetchone()
        return Result(True, row, None)
    except Exception as e:
        return Result(False, None, f"ERR-DB-136: Gagal mengecek duplikasi nama supplier. Detail: {str(e)}")
    finally:
        if cursor:
            cursor.close()


def insert_riwayat_harga_supplier(db_connection, data: dict) -> Result:
    """Menyimpan entri baru ke tabel riwayat_harga_supplier.

    Args:
        db_connection: Koneksi database aktif.
        data (dict): Dictionary data yang di-insert.
                     Berisi: barang_id, supplier_id, harga_beli, tanggal_pembelian, cabang_id.

    Returns:
        Result: Hasil eksekusi INSERT (lastrowid).
    """
    query = """
        INSERT INTO riwayat_harga_supplier
            (barang_id, supplier_id, harga_beli, tanggal_pembelian, cabang_id)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (
        data['barang_id'],
        data['supplier_id'],
        data['harga_beli'],
        data['tanggal_pembelian'],
        data['cabang_id']
    )
    return execute_insert(db_connection, query, params)


def get_riwayat_harga_by_barang(db_connection, barang_id: int, cabang_id: int) -> Result:
    """Mengambil kronologi harga beli historis barang dari seluruh supplier.

    Args:
        db_connection: Koneksi database aktif.
        barang_id (int): ID barang yang dilacak.
        cabang_id (int): ID cabang filter.

    Returns:
        Result: List dict data riwayat harga terurut tanggal terbaru DESC.
    """
    query = """
        SELECT
            r.id,
            r.tanggal_pembelian,
            s.nama_supplier,
            r.harga_beli,
            r.supplier_id
        FROM riwayat_harga_supplier r
        JOIN supplier s ON r.supplier_id = s.id
        WHERE r.barang_id = %s AND r.cabang_id = %s
        ORDER BY r.tanggal_pembelian DESC, r.created_at DESC
    """
    return execute_query(db_connection, query, (barang_id, cabang_id), fetch_all=True)


def get_supplier_termurah_by_barang(db_connection, barang_id: int, cabang_id: int) -> Result:
    """Mengambil rekomendasi supplier termurah berdasarkan pembelian terakhir.

    Args:
        db_connection: Koneksi database aktif.
        barang_id (int): ID barang.
        cabang_id (int): ID cabang.

    Returns:
        Result: Dict/row data supplier termurah atau None.
    """
    query = """
        SELECT
            s.id AS supplier_id,
            s.nama_supplier,
            r.harga_beli,
            r.tanggal_pembelian
        FROM riwayat_harga_supplier r
        JOIN supplier s ON r.supplier_id = s.id
        WHERE r.barang_id = %s
          AND r.cabang_id = %s
          AND r.tanggal_pembelian = (
              SELECT MAX(r2.tanggal_pembelian)
              FROM riwayat_harga_supplier r2
              WHERE r2.barang_id = r.barang_id
                AND r2.supplier_id = r.supplier_id
                AND r2.cabang_id = r.cabang_id
          )
        ORDER BY r.harga_beli ASC
        LIMIT 1
    """
    return execute_query(db_connection, query, (barang_id, cabang_id), fetch_one=True)


def update_harga_beli_barang(db_connection, barang_id: int, harga_beli_baru: Decimal) -> Result:
    """Mengupdate harga_beli standar pada tabel barang.

    Args:
        db_connection: Koneksi database aktif.
        barang_id (int): ID barang.
        harga_beli_baru (Decimal): Harga beli baru.

    Returns:
        Result: Hasil eksekusi UPDATE.
    """
    query = "UPDATE barang SET harga_beli = %s WHERE id = %s"
    return execute_query(db_connection, query, (harga_beli_baru, barang_id))


def check_barang_exists(db_connection, barang_id: int, cabang_id: int) -> bool:
    """Mengecek apakah ID barang terdaftar di cabang tertentu.

    Args:
        db_connection: Koneksi database aktif.
        barang_id (int): ID barang.
        cabang_id (int): ID cabang.

    Returns:
        bool: True jika barang ada, False jika tidak.
    """
    query = "SELECT COUNT(1) AS count FROM barang WHERE id = %s AND cabang_id = %s"
    res = execute_query(db_connection, query, (barang_id, cabang_id), fetch_one=True)
    if res.is_success and res.data:
        return res.data['count'] > 0
    return False


def check_supplier_exists(db_connection, supplier_id: int, cabang_id: int) -> bool:
    """Mengecek apakah ID supplier terdaftar di cabang tertentu.

    Args:
        db_connection: Koneksi database aktif.
        supplier_id (int): ID supplier.
        cabang_id (int): ID cabang.

    Returns:
        bool: True jika supplier ada, False jika tidak.
    """
    query = "SELECT COUNT(1) AS count FROM supplier WHERE id = %s AND cabang_id = %s"
    res = execute_query(db_connection, query, (supplier_id, cabang_id), fetch_one=True)
    if res.is_success and res.data:
        return res.data['count'] > 0
    return False


def insert_pelanggan_baru(
    db_connection,
    nama_pelanggan: str,
    whatsapp_encrypted: str,
    cabang_id: int
) -> Result:
    """Menyisipkan data pelanggan baru ke tabel pelanggan MySQL.

    (Ref: SRS-F-038, Schema DDL TABEL 03)

    Args:
        db_connection: Objek koneksi database aktif.
        nama_pelanggan (str): Nama pelanggan CRM.
        whatsapp_encrypted (str): Nomor WhatsApp terenkripsi Fernet.
        cabang_id (int): ID cabang pendaftaran.

    Returns:
        Result: Tuple (is_success, data=id_pelanggan_baru, error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor()
        query = (
            "INSERT INTO pelanggan (nama_pelanggan, whatsapp, cabang_id) "
            "VALUES (%s, %s, %s)"
        )
        cursor.execute(query, (nama_pelanggan, whatsapp_encrypted, cabang_id))
        db_connection.commit()
        last_id = cursor.lastrowid
        return Result(True, last_id, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        if e.errno == 1062:  # Duplicate entry
            # Cari nama pelanggan pemilik whatsapp ini
            nama_existing = "[Tidak Diketahui]"
            cursor_find = None
            try:
                cursor_find = db_connection.cursor()
                cursor_find.execute(
                    "SELECT nama_pelanggan FROM pelanggan WHERE whatsapp = %s AND cabang_id = %s",
                    (whatsapp_encrypted, cabang_id)
                )
                row = cursor_find.fetchone()
                if row:
                    nama_existing = row[0]
            except Exception:
                pass
            finally:
                if cursor_find:
                    try:
                        cursor_find.close()
                    except Exception:
                        pass
            
            return Result(
                False,
                None,
                f"⛔ ERR-CRM-036: Nomor WhatsApp sudah terdaftar atas nama pelanggan {nama_existing}!"
            )
        error_msg = f"ERR-DB-002: Eksekusi INSERT pelanggan gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi INSERT pelanggan gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def cari_pelanggan_by_whatsapp(
    db_connection,
    whatsapp_encrypted: str,
    cabang_id: int,
    fernet_key: str | None = None
) -> Result:
    """Mencari pelanggan berdasarkan nomor WhatsApp terenkripsi.

    (Ref: Security Design Bab 8.1 - Pencarian Terenkripsi)
    CATATAN: Pencarian dilakukan via dekripsi di memori karena Fernet
    menghasilkan ciphertext non-deterministik. Untuk skala > 10.000
    pelanggan, pertimbangkan menambah kolom whatsapp_hash (SHA-256)
    untuk pencarian O(1).

    Args:
        db_connection: Objek koneksi database aktif.
        whatsapp_encrypted (str): Nomor WhatsApp terenkripsi Fernet atau plaintext.
        cabang_id (int): ID cabang.
        fernet_key (str | None): Kunci enkripsi simetris Fernet 32-byte.

    Returns:
        Result: Tuple (is_success, data=dict_pelanggan|None, error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        
        # 1. Dapatkan target plaintext
        target_plain = ""
        if fernet_key:
            target_plain = decrypt_whatsapp_number(whatsapp_encrypted, fernet_key)
        if not target_plain:
            target_plain = whatsapp_encrypted
            
        # 2. Ambil seluruh data pelanggan di cabang ini
        query = (
            "SELECT id, nama_pelanggan, whatsapp, tanggal_terdaftar "
            "FROM pelanggan "
            "WHERE cabang_id = %s"
        )
        cursor.execute(query, (cabang_id,))
        rows = cursor.fetchall()
        
        # 3. Cocokkan di memori
        matched_row = None
        for row in rows:
            row_plain = ""
            if fernet_key:
                row_plain = decrypt_whatsapp_number(row['whatsapp'], fernet_key)
            if not row_plain:
                row_plain = row['whatsapp']
                
            if row_plain == target_plain:
                matched_row = row
                break
                
        return Result(True, matched_row, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Pencarian pelanggan gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Pencarian pelanggan gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def get_daftar_pelanggan(
    db_connection,
    cabang_id: int,
    limit: int = 50,
    offset: int = 0
) -> Result:
    """Mengambil daftar pelanggan CRM per cabang.

    Args:
        db_connection: Objek koneksi database aktif.
        cabang_id (int): ID cabang.
        limit (int): Jumlah maksimal data.
        offset (int): Offset data untuk paginasi.

    Returns:
        Result: Tuple (is_success, data=list[dict], error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = (
            "SELECT id, nama_pelanggan, whatsapp, tanggal_terdaftar "
            "FROM pelanggan "
            "WHERE cabang_id = %s "
            "ORDER BY id DESC "
            "LIMIT %s OFFSET %s"
        )
        cursor.execute(query, (cabang_id, limit, offset))
        rows = cursor.fetchall()
        return Result(True, rows, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil daftar pelanggan (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil daftar pelanggan (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def get_riwayat_transaksi_pelanggan(
    db_connection,
    pelanggan_id: int,
    cabang_id: int
) -> Result:
    """Mengambil riwayat transaksi terkait pelanggan CRM.

    Args:
        db_connection: Objek koneksi database aktif.
        pelanggan_id (int): ID pelanggan.
        cabang_id (int): ID cabang.

    Returns:
        Result: Tuple (is_success, data=list[dict], error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = (
            "SELECT id, no_invoice, tanggal_transaksi, total_bayar, "
            "status_pembayaran, tipe_pelanggan "
            "FROM transaksi "
            "WHERE pelanggan_id = %s AND cabang_id = %s "
            "ORDER BY tanggal_transaksi DESC "
            "LIMIT 20"
        )
        cursor.execute(query, (pelanggan_id, cabang_id))
        rows = cursor.fetchall()
        
        # Mengonversi total_bayar ke Decimal
        for row in rows:
            if row.get('total_bayar') is not None:
                row['total_bayar'] = Decimal(str(row['total_bayar']))
                
        return Result(True, rows, None)
    except mysql.connector.Error as e:
        error_msg = f"ERR-DB-002: Gagal mengambil riwayat transaksi (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        error_msg = f"ERR-DB-002: Gagal mengambil riwayat transaksi (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def update_pelanggan(
    db_connection,
    pelanggan_id: int,
    nama_pelanggan: str | None,
    whatsapp_encrypted: str | None,
    cabang_id: int
) -> Result:
    """Memperbarui data profil pelanggan CRM.

    Args:
        db_connection: Objek koneksi database aktif.
        pelanggan_id (int): ID pelanggan yang akan diperbarui.
        nama_pelanggan (str | None): Nama baru pelanggan.
        whatsapp_encrypted (str | None): WhatsApp baru terenkripsi.
        cabang_id (int): ID cabang.

    Returns:
        Result: Tuple (is_success, data=None, error_msg).
    """
    if nama_pelanggan is None and whatsapp_encrypted is None:
        return Result(True, None, None)

    cursor = None
    try:
        cursor = db_connection.cursor()
        
        updates = []
        params = []
        
        if nama_pelanggan is not None:
            updates.append("nama_pelanggan = %s")
            params.append(nama_pelanggan)
            
        if whatsapp_encrypted is not None:
            updates.append("whatsapp = %s")
            params.append(whatsapp_encrypted)
            
        params.extend([pelanggan_id, cabang_id])
        
        updates_str = ", ".join(updates)
        query = "UPDATE pelanggan SET " + updates_str + " WHERE id = %s AND cabang_id = %s"
        
        cursor.execute(query, tuple(params))
        db_connection.commit()
        return Result(True, None, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        if e.errno == 1062:  # Duplicate entry
            # Cari nama pelanggan pemilik whatsapp ini
            nama_existing = "[Tidak Diketahui]"
            cursor_find = None
            try:
                cursor_find = db_connection.cursor()
                cursor_find.execute(
                    "SELECT nama_pelanggan FROM pelanggan WHERE whatsapp = %s AND cabang_id = %s",
                    (whatsapp_encrypted, cabang_id)
                )
                row = cursor_find.fetchone()
                if row:
                    nama_existing = row[0]
            except Exception:
                pass
            finally:
                if cursor_find:
                    try:
                        cursor_find.close()
                    except Exception:
                        pass
            
            return Result(
                False,
                None,
                f"⛔ ERR-CRM-036: Nomor WhatsApp sudah terdaftar atas nama pelanggan {nama_existing}!"
            )
        error_msg = f"ERR-DB-002: Gagal memperbarui data pelanggan (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Gagal memperbarui data pelanggan (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()


def query_delete_pelanggan(
    db_connection,
    pelanggan_id: int,
    cabang_id: int
) -> Result:
    """Menghapus data pelanggan dari database CRM secara permanen (hard-delete).

    (Ref: Modul M.8, UU PDP No. 27/2022)

    Args:
        db_connection: Objek koneksi database aktif.
        pelanggan_id (int): ID pelanggan yang akan dihapus.
        cabang_id (int): Filter multi-branch wajib pada klausa WHERE.

    Returns:
        Result: NamedTuple (is_success, data: int (rowcount), error_msg).
    """
    cursor = None
    try:
        cursor = db_connection.cursor(dictionary=True)
        query = "DELETE FROM pelanggan WHERE id = %s AND cabang_id = %s"
        cursor.execute(query, (pelanggan_id, cabang_id))
        db_connection.commit()
        return Result(True, cursor.rowcount, None)
    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: MySQL Error {e.errno}: {e.msg})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        error_msg = f"ERR-DB-002: Eksekusi query gagal (Detail Error: {str(e)})"
        _logger.error(error_msg)
        return Result(False, None, error_msg)
    finally:
        if cursor:
            cursor.close()
