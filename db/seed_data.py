"""
Nama Modul: seed_data.py
Deskripsi: Utilitas fungsional untuk seeding data default awal (bootstrapping)
           ke database MySQL AbuCom. Mencakup tabel cabang, pengguna, saldo_ppob,
           saldo_ewallet, dan system_configs. Bersifat idempoten dan transaksional ACID.
Author: Antigravity
Tanggal: 2026-06-04
"""

# 1. Standard Library
import logging
from collections import namedtuple
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

# 2. Third-Party
import bcrypt
import mysql.connector

# 3. Local Modules
# No local modules imported to prevent circular imports and keep database functions pure.

_logger = logging.getLogger('abucom.db.seed')

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])

DEFAULT_PASSWORD: str = 'admin123'

DEFAULT_CABANG_DATA: tuple[int, str, str, str] = (
    1,
    'Toko Pusat Bandung',
    'Jl. Raya Percetakan No. 45, RT 02/RW 03, Kecamatan Sukamaju, Kota Bandung, Jawa Barat, 40123',
    '0227654321'
)

DEFAULT_PENGGUNA_DATA: tuple[int, str, str, str, int, int] = (
    1,
    'Pemilik Usaha AbuCom',
    'pemilik',
    'pemilik',
    0,
    1
)

DEFAULT_SALDO_PPOB_DATA: tuple[tuple[str, Decimal, int], ...] = (
    ('Pulsa_Data', Decimal('1000000.0000'), 1),
    ('Token_Tagihan', Decimal('1500000.0000'), 1),
)

DEFAULT_SALDO_EWALLET_DATA: tuple[tuple[str, Decimal, Decimal, Decimal, Decimal, int], ...] = (
    ('Mandiri Agen', Decimal('2000000.0000'), Decimal('3000.0000'), Decimal('0.0000'), Decimal('50000000.0000'), 1),
    ('Dana', Decimal('1000000.0000'), Decimal('1000.0000'), Decimal('0.0000'), Decimal('10000000.0000'), 1),
    ('Gopay', Decimal('1000000.0000'), Decimal('1000.0000'), Decimal('0.0000'), Decimal('10000000.0000'), 1),
    ('LinkAja', Decimal('1000000.0000'), Decimal('1000.0000'), Decimal('0.0000'), Decimal('10000000.0000'), 1),
    ('ShopeePay', Decimal('1000000.0000'), Decimal('1000.0000'), Decimal('0.0000'), Decimal('10000000.0000'), 1),
    ('OVO', Decimal('1000000.0000'), Decimal('1000.0000'), Decimal('0.0000'), Decimal('10000000.0000'), 1),
)

DEFAULT_SYSTEM_CONFIGS_DATA: tuple[tuple[str, Decimal, str, str, int], ...] = (
    ('target_laba_payroll', Decimal('15000000.0000'), 'DECIMAL', 'Target laba bersih bulanan untuk skema gaji tetap (Skenario A Smart Payroll)', 1),
    ('porsi_gaji_laba', Decimal('0.2500'), 'DECIMAL', 'Persentase alokasi laba bersih untuk pool gaji karyawan (Skenario B Smart Payroll)', 1),
    ('limit_kasbon_staf', Decimal('1000000.0000'), 'DECIMAL', 'Pagu maksimal utang kasbon aktif kumulatif per staf', 1),
    ('threshold_saldo_ppob', Decimal('150000.0000'), 'DECIMAL', 'Batas saldo minimum PPOB yang memicu alert deposit', 1),
    ('min_topup_ppob', Decimal('500000.0000'), 'DECIMAL', 'Nominal minimum deposit topup saldo PPOB', 1),
    ('toleransi_selisih_kas', Decimal('10000.0000'), 'DECIMAL', 'Batas toleransi selisih kas kasir sebelum status ANOMALI', 1),
    ('poin_tier_1_rupiah', Decimal('500.0000'), 'DECIMAL', 'Nilai rupiah per poin insentif Tier 1 (transaksi mudah)', 1),
    ('poin_tier_2_rupiah', Decimal('1500.0000'), 'DECIMAL', 'Nilai rupiah per poin insentif Tier 2 (jasa dasar)', 1),
    ('poin_tier_3_rupiah', Decimal('2500.0000'), 'DECIMAL', 'Nilai rupiah per poin insentif Tier 3 (produk kustom)', 1),
    ('poin_tier_4_rupiah', Decimal('5000.0000'), 'DECIMAL', 'Nilai rupiah per poin insentif Tier 4 (pekerjaan berat/teknis)', 1),
    ('threshold_pengeluaran', Decimal('500000.0000'), 'DECIMAL', 'Batas nominal pengeluaran yang memerlukan otorisasi pemilik', 1),
    ('umr_daerah', Decimal('3200000.0000'), 'DECIMAL', 'Upah Minimum Regional daerah sebagai batas proteksi gaji minimum staf', 1),
    ('dana_cadangan_darurat', Decimal('4500000.0000'), 'DECIMAL', 'Cadangan kas darurat minimal yang harus dijaga di laci kasir', 1),
)

SEED_SATUAN_UKUR: list[tuple[str, str, str, str]] = [
    ('Pcs', 'Kuantitas', 'pcs', 'Satuan pieces/buah individual'),
    ('Lembar', 'Kuantitas', 'lbr', 'Satuan lembar kertas/bahan lembaran'),
    ('Rim', 'Kuantitas', 'rim', 'Satuan rim kertas (1 rim = 500 lembar)'),
    ('Buah', 'Kuantitas', 'bh', 'Satuan buah/unit barang'),
    ('Set', 'Kuantitas', 'set', 'Satuan set/paket lengkap'),
    ('Lusin', 'Kuantitas', 'lsn', 'Satuan lusin (1 lusin = 12 pcs)'),
    ('Meter', 'Panjang', 'm', 'Satuan panjang meter'),
    ('Centimeter', 'Panjang', 'cm', 'Satuan panjang centimeter'),
    ('Meter_Persegi', 'Luas', 'm²', 'Satuan luas meter persegi'),
    ('Ml', 'Volume', 'ml', 'Satuan volume mililiter'),
    ('Liter', 'Volume', 'L', 'Satuan volume liter'),
    ('Botol', 'Volume', 'btl', 'Satuan botol tinta/cairan'),
    ('Gram', 'Berat', 'g', 'Satuan berat gram'),
    ('Kg', 'Berat', 'kg', 'Satuan berat kilogram'),
    ('Roll', 'Kuantitas', 'roll', 'Satuan gulung/roll bahan'),
    ('Pack', 'Kuantitas', 'pack', 'Satuan kemasan pak'),
]

SEED_KONVERSI_SATUAN: list[tuple[str, str, Decimal]] = [
    ('Rim', 'Lembar', Decimal('500.0000')),
    ('Lusin', 'Pcs', Decimal('12.0000')),
    ('Meter', 'Centimeter', Decimal('100.0000')),
    ('Liter', 'Ml', Decimal('1000.0000')),
    ('Kg', 'Gram', Decimal('1000.0000')),
]

EXPECTED_SEED_COUNTS: dict[str, int] = {
    'cabang': 1,
    'pengguna': 1,
    'saldo_ppob': 2,
    'saldo_ewallet': 6,
    'system_configs': 13,
    'satuan_ukur': 16,
    'konversi_satuan': 10,
}


def generate_default_password_hash(password: str) -> Result:
    """Menghasilkan bcrypt hash satu arah dengan Cost Factor 12 dari password polos.

    Args:
        password (str): Password polos yang akan di-hash.

    Returns:
        Result: NamedTuple berisi status keberhasilan, hash string, atau pesan error.
    """
    try:
        if not password:
            return Result(False, None, 'ERR-VAL-050: Password tidak boleh kosong.')
        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
        if not hashed.startswith('$2b$12$'):
            return Result(False, None, 'ERR-VAL-050: Format bcrypt hash yang dihasilkan tidak valid.')
        return Result(True, hashed, None)
    except Exception as e:
        return Result(False, None, f'ERR-VAL-050: Gagal men-generate bcrypt password hash (Error: {str(e)})')


def seed_cabang_default(cursor: Any) -> Result:
    """Memasukkan data cabang default secara idempoten.

    Args:
        cursor (Any): Cursor database aktif yang berada dalam transaksi.

    Returns:
        Result: NamedTuple berisi status keberhasilan operasional.
    """
    try:
        cursor.execute("SELECT COUNT(*) FROM cabang WHERE id = %s", (DEFAULT_CABANG_DATA[0],))
        count = cursor.fetchone()[0]
        if count > 0:
            _logger.warning("Seed tabel cabang: data sudah ada, skip insert.")
            return Result(True, 0, None)

        query = "INSERT INTO cabang (id, nama_cabang, alamat, telp) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, DEFAULT_CABANG_DATA)
        _logger.info("Seed tabel cabang: 1 baris berhasil diinsert.")
        return Result(True, 1, None)
    except mysql.connector.Error as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel cabang (MySQL Error {e.errno}: {e.msg})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)
    except Exception as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel cabang (Error: {str(e)})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)


def seed_pengguna_default(cursor: Any, password_hash: str) -> Result:
    """Memasukkan data pengguna pemilik default secara idempoten.

    Args:
        cursor (Any): Cursor database aktif yang berada dalam transaksi.
        password_hash (str): Hash password bcrypt default yang sudah valid.

    Returns:
        Result: NamedTuple berisi status keberhasilan operasional.
    """
    try:
        cursor.execute("SELECT COUNT(*) FROM pengguna WHERE id = %s", (DEFAULT_PENGGUNA_DATA[0],))
        count = cursor.fetchone()[0]
        if count > 0:
            _logger.warning("Seed tabel pengguna: data sudah ada, skip insert.")
            return Result(True, 0, None)

        # DEFAULT_PENGGUNA_DATA: id, nama_lengkap, username, role, failed_login_attempts, cabang_id
        # locked_until diisi None
        query = (
            "INSERT INTO pengguna (id, nama_lengkap, username, password_hash, role, "
            "failed_login_attempts, locked_until, cabang_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        params = (
            DEFAULT_PENGGUNA_DATA[0],
            DEFAULT_PENGGUNA_DATA[1],
            DEFAULT_PENGGUNA_DATA[2],
            password_hash,
            DEFAULT_PENGGUNA_DATA[3],
            DEFAULT_PENGGUNA_DATA[4],
            None,
            DEFAULT_PENGGUNA_DATA[5]
        )
        cursor.execute(query, params)
        _logger.info("Seed tabel pengguna: 1 baris berhasil diinsert.")
        return Result(True, 1, None)
    except mysql.connector.Error as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel pengguna (MySQL Error {e.errno}: {e.msg})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)
    except Exception as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel pengguna (Error: {str(e)})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)


def seed_saldo_ppob_default(cursor: Any) -> Result:
    """Memasukkan data saldo PPOB default secara idempoten menggunakan INSERT IGNORE.

    Args:
        cursor (Any): Cursor database aktif yang berada dalam transaksi.

    Returns:
        Result: NamedTuple berisi status keberhasilan operasional dan baris terinsert.
    """
    try:
        cursor.execute("SELECT COUNT(*) FROM saldo_ppob")
        count = cursor.fetchone()[0]
        if count >= EXPECTED_SEED_COUNTS['saldo_ppob']:
            _logger.warning("Seed tabel saldo_ppob: data sudah ada, skip insert.")
            return Result(True, 0, None)

        inserted = 0
        query = "INSERT IGNORE INTO saldo_ppob (akun_tipe, saldo_terakhir, cabang_id) VALUES (%s, %s, %s)"
        for row in DEFAULT_SALDO_PPOB_DATA:
            cursor.execute(query, row)
            inserted += cursor.rowcount

        _logger.info(f"Seed tabel saldo_ppob: {inserted} baris berhasil diinsert.")
        return Result(True, inserted, None)
    except mysql.connector.Error as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel saldo_ppob (MySQL Error {e.errno}: {e.msg})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)
    except Exception as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel saldo_ppob (Error: {str(e)})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)


def seed_saldo_ewallet_default(cursor: Any) -> Result:
    """Memasukkan data saldo e-wallet default secara idempoten menggunakan INSERT IGNORE.

    Args:
        cursor (Any): Cursor database aktif yang berada dalam transaksi.

    Returns:
        Result: NamedTuple berisi status keberhasilan operasional dan baris terinsert.
    """
    try:
        cursor.execute("SELECT COUNT(*) FROM saldo_ewallet")
        count = cursor.fetchone()[0]
        if count >= EXPECTED_SEED_COUNTS['saldo_ewallet']:
            _logger.warning("Seed tabel saldo_ewallet: data sudah ada, skip insert.")
            return Result(True, 0, None)

        inserted = 0
        query = (
            "INSERT IGNORE INTO saldo_ewallet (nama_ewallet, saldo_terakhir, "
            "biaya_admin_flat, biaya_admin_persen, limit_harian, cabang_id) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        for row in DEFAULT_SALDO_EWALLET_DATA:
            cursor.execute(query, row)
            inserted += cursor.rowcount

        _logger.info(f"Seed tabel saldo_ewallet: {inserted} baris berhasil diinsert.")
        return Result(True, inserted, None)
    except mysql.connector.Error as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel saldo_ewallet (MySQL Error {e.errno}: {e.msg})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)
    except Exception as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel saldo_ewallet (Error: {str(e)})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)


def seed_system_configs_default(cursor: Any) -> Result:
    """Memasukkan data konfigurasi sistem default secara idempoten menggunakan INSERT IGNORE.

    Args:
        cursor (Any): Cursor database aktif yang berada dalam transaksi.

    Returns:
        Result: NamedTuple berisi status keberhasilan operasional dan baris terinsert.
    """
    try:
        cursor.execute("SELECT COUNT(*) FROM system_configs")
        count = cursor.fetchone()[0]
        if count >= EXPECTED_SEED_COUNTS['system_configs']:
            _logger.warning("Seed tabel system_configs: data sudah ada, skip insert.")
            return Result(True, 0, None)

        inserted = 0
        query = (
            "INSERT IGNORE INTO system_configs (parameter_key, parameter_value, "
            "tipe_data, deskripsi, cabang_id) VALUES (%s, %s, %s, %s, %s)"
        )
        for row in DEFAULT_SYSTEM_CONFIGS_DATA:
            # Cast parameter_value (Decimal) to string for parameter_value column
            params = (row[0], str(row[1]), row[2], row[3], row[4])
            cursor.execute(query, params)
            inserted += cursor.rowcount

        _logger.info(f"Seed tabel system_configs: {inserted} baris berhasil diinsert.")
        return Result(True, inserted, None)
    except mysql.connector.Error as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel system_configs (MySQL Error {e.errno}: {e.msg})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)
    except Exception as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel system_configs (Error: {str(e)})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)



def seed_satuan_ukur_default(cursor: Any) -> Result:
    """Memasukkan data satuan ukur default secara idempoten menggunakan INSERT IGNORE.

    Args:
        cursor (Any): Cursor database aktif yang berada dalam transaksi.

    Returns:
        Result: NamedTuple berisi status keberhasilan operasional dan baris terinsert.
    """
    try:
        cursor.execute("SELECT COUNT(*) FROM satuan_ukur")
        count = cursor.fetchone()[0]
        if count >= EXPECTED_SEED_COUNTS['satuan_ukur']:
            _logger.warning("Seed tabel satuan_ukur: data sudah ada, skip insert.")
            return Result(True, 0, None)

        inserted = 0
        query = (
            "INSERT IGNORE INTO satuan_ukur (nama_satuan, kategori_satuan, simbol, keterangan, cabang_id) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        for row in SEED_SATUAN_UKUR:
            cursor.execute(query, (row[0], row[1], row[2], row[3], 1))
            inserted += cursor.rowcount

        _logger.info(f"Seed tabel satuan_ukur: {inserted} baris berhasil diinsert.")
        return Result(True, inserted, None)
    except mysql.connector.Error as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel satuan_ukur (MySQL Error {e.errno}: {e.msg})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)
    except Exception as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel satuan_ukur (Error: {str(e)})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)


def seed_konversi_satuan_default(cursor: Any) -> Result:
    """Memasukkan data konversi satuan default secara idempoten menggunakan INSERT IGNORE.

    Args:
        cursor (Any): Cursor database aktif yang berada dalam transaksi.

    Returns:
        Result: NamedTuple berisi status keberhasilan operasional dan baris terinsert.
    """
    try:
        cursor.execute("SELECT COUNT(*) FROM konversi_satuan")
        count = cursor.fetchone()[0]
        if count >= EXPECTED_SEED_COUNTS['konversi_satuan']:
            _logger.warning("Seed tabel konversi_satuan: data sudah ada, skip insert.")
            return Result(True, 0, None)

        cursor.execute("SELECT id, nama_satuan FROM satuan_ukur WHERE is_aktif = TRUE")
        satuan_map = {row[1]: row[0] for row in cursor.fetchall()}

        inserted = 0
        query = (
            "INSERT IGNORE INTO konversi_satuan (satuan_asal_id, satuan_tujuan_id, faktor_konversi, cabang_id) "
            "VALUES (%s, %s, %s, %s)"
        )
        for row in SEED_KONVERSI_SATUAN:
            asal_name, tujuan_name, faktor = row
            asal_id = satuan_map.get(asal_name)
            tujuan_id = satuan_map.get(tujuan_name)
            if asal_id is None or tujuan_id is None:
                continue

            # Insert direct
            cursor.execute(query, (asal_id, tujuan_id, faktor, 1))
            inserted += cursor.rowcount

            # Insert inverse (konversi balik)
            faktor_balik = (Decimal('1') / faktor).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
            cursor.execute(query, (tujuan_id, asal_id, faktor_balik, 1))
            inserted += cursor.rowcount

        _logger.info(f"Seed tabel konversi_satuan: {inserted} baris berhasil diinsert.")
        return Result(True, inserted, None)
    except mysql.connector.Error as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel konversi_satuan (MySQL Error {e.errno}: {e.msg})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)
    except Exception as e:
        err_msg = f"ERR-DB-SEED-001: Gagal seed tabel konversi_satuan (Error: {str(e)})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)


def verify_seed_integrity(cursor: Any) -> Result:
    """Memverifikasi integritas dan kecocokan jumlah baris seed data setelah inisialisasi.

    Args:
        cursor (Any): Cursor database aktif.

    Returns:
        Result: NamedTuple berisi status validitas dan dict laporan aktual atau pesan error.
    """
    try:
        report = {}
        errors = []

        # 1. Verifikasi jumlah baris per tabel
        for table, expected in EXPECTED_SEED_COUNTS.items():
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            actual = cursor.fetchone()[0]
            report[table] = actual
            if actual != expected:
                errors.append(f"Tabel {table}: diharapkan {expected} baris, ditemukan {actual} baris.")

        # 2. Verifikasi format hash password pengguna default id 1
        cursor.execute("SELECT password_hash FROM pengguna WHERE id = 1")
        row = cursor.fetchone()
        if not row:
            errors.append("Tabel pengguna: akun pemilik default id = 1 tidak ditemukan.")
        else:
            pwd_hash = row[0]
            if not pwd_hash.startswith('$2b$12$'):
                errors.append("Tabel pengguna: password_hash akun pemilik bukan format bcrypt Cost 12 valid.")

        # 3. Verifikasi keunikan parameter key pada system_configs
        cursor.execute("SELECT COUNT(DISTINCT parameter_key) FROM system_configs")
        unique_keys = cursor.fetchone()[0]
        if unique_keys != EXPECTED_SEED_COUNTS['system_configs']:
            errors.append(
                f"Tabel system_configs: diharapkan {EXPECTED_SEED_COUNTS['system_configs']} parameter unik, "
                f"ditemukan {unique_keys}."
            )

        if errors:
            err_msg = f"Integritas seed data tidak valid: {'; '.join(errors)}"
            _logger.error(err_msg)
            return Result(False, report, err_msg)

        _logger.info("Integritas seed data terverifikasi 100% sukses.")
        return Result(True, report, None)
    except mysql.connector.Error as e:
        err_msg = f"ERR-DB-SEED-001: Verifikasi seed gagal (MySQL Error {e.errno}: {e.msg})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)
    except Exception as e:
        err_msg = f"ERR-DB-SEED-001: Verifikasi seed gagal (Error: {str(e)})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)


def run_seed_all(db_connection: Any) -> Result:
    """Fungsi pembungkus utama untuk menjalankan seluruh rangkaian seed data default secara transaksional ACID.

    Args:
        db_connection (Any): Koneksi database MySQL aktif yang valid.

    Returns:
        Result: NamedTuple berisi status keberhasilan dan laporan hasil akhir.
    """
    if db_connection is None:
        return Result(False, None, 'ERR-DB-SEED-001: Koneksi database tidak boleh None.')

    # 1. Generate bcrypt hash default password
    hash_res = generate_default_password_hash(DEFAULT_PASSWORD)
    if not hash_res.is_success:
        return hash_res
    password_hash = hash_res.data

    cursor = None
    try:
        cursor = db_connection.cursor()
        # 2. Mulai Transaksi ACID
        db_connection.start_transaction()

        # 3. Eksekusi fungsi seed sesuai urutan dependensi
        # Cabang
        res_cabang = seed_cabang_default(cursor)
        if not res_cabang.is_success:
            db_connection.rollback()
            cursor.close()
            return res_cabang

        # Pengguna
        res_pengguna = seed_pengguna_default(cursor, password_hash)
        if not res_pengguna.is_success:
            db_connection.rollback()
            cursor.close()
            return res_pengguna

        # Saldo PPOB
        res_ppob = seed_saldo_ppob_default(cursor)
        if not res_ppob.is_success:
            db_connection.rollback()
            cursor.close()
            return res_ppob

        # Saldo E-wallet
        res_ewallet = seed_saldo_ewallet_default(cursor)
        if not res_ewallet.is_success:
            db_connection.rollback()
            cursor.close()
            return res_ewallet

        # System Configs
        res_configs = seed_system_configs_default(cursor)
        if not res_configs.is_success:
            db_connection.rollback()
            cursor.close()
            return res_configs

        # Satuan Ukur
        res_satuan = seed_satuan_ukur_default(cursor)
        if not res_satuan.is_success:
            db_connection.rollback()
            cursor.close()
            return res_satuan

        # Konversi Satuan
        res_konversi = seed_konversi_satuan_default(cursor)
        if not res_konversi.is_success:
            db_connection.rollback()
            cursor.close()
            return res_konversi

        # 4. Commit Transaksi jika semua sub-seeding sukses
        db_connection.commit()

        # 5. Jalankan verifikasi pasca-commit
        verify_res = verify_seed_integrity(cursor)
        cursor.close()

        if not verify_res.is_success:
            return verify_res

        stats = {
            'cabang_inserted': res_cabang.data,
            'pengguna_inserted': res_pengguna.data,
            'saldo_ppob_inserted': res_ppob.data,
            'saldo_ewallet_inserted': res_ewallet.data,
            'system_configs_inserted': res_configs.data,
            'satuan_ukur_inserted': res_satuan.data,
            'konversi_satuan_inserted': res_konversi.data,
            'report': verify_res.data
        }
        return Result(True, stats, None)

    except mysql.connector.Error as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        if cursor:
            cursor.close()
        err_msg = f"ERR-DB-SEED-001: Proses seeding gagal (MySQL Error {e.errno}: {e.msg})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)
    except Exception as e:
        try:
            db_connection.rollback()
        except Exception:
            pass
        if cursor:
            cursor.close()
        err_msg = f"ERR-DB-SEED-001: Proses seeding gagal (Error: {str(e)})"
        _logger.error(err_msg)
        return Result(False, None, err_msg)
