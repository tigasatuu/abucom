---
judul      : Unit-Test Feature Seed Data Default Cabang dan System Configs
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
tanggal    : 2026-06-04
status     : Open
prioritas  : High
modul      : db/seed_data.py → tests/test_unit_seed_data.py
penyusun   : Claude Opus 4.6 (Thinking) — Strategi Sistem & Keamanan
---

# Issue — Unit-Test Feature Seed Data Default Cabang dan System Configs

## 1. Persona Pelaksana

**Peran**: **Senior QA Engineer & Test Automation Specialist**

Kamu adalah seorang Senior QA Engineer yang bertanggung jawab untuk menulis, memvalidasi, dan mengeksekusi unit test secara menyeluruh untuk modul `db/seed_data.py` proyek AbuCom. Kamu memiliki keahlian mendalam di bidang:
- Python 3.14.2+ dengan paradigma **Functional Programming (FP) murni** — tanpa `class` di alur bisnis.
- Framework testing `pytest` dengan teknik **mocking** (`unittest.mock.MagicMock`, `patch`).
- Pola **Result Pattern** (`NamedTuple`) untuk error handling fungsional.
- Presisi desimal `Decimal(15,4)` dan pembulatan `ROUND_HALF_UP`.
- Standar keamanan bcrypt Cost Factor 12, dan konvensi kode error `ERR-XXX-YYY`.
- Prinsip pengujian **FIRST** (Fast, Isolated, Repeatable, Self-Validating, Timely).

**Instruksi Sikap**:
- Kerjakan secara **teliti, presisi, dan tanpa ambigu**.
- **Dilarang** meninggalkan kode dengan komentar `# TODO`, `# FIXME`, atau placeholder kosong.
- Setiap fungsi test **wajib** komplit, dapat dijalankan, dan menghasilkan assertion yang jelas.
- **Dilarang** melakukan koneksi fisik ke database MySQL. Seluruh interaksi database **wajib** di-mock menggunakan `MagicMock`.

---

## 2. Dokumen Referensi Utama

Bacalah dan ekstraklah seluruh detail yang relevan dari dokumen-dokumen berikut **sebelum** menulis satu baris kode pun:

| No | Dokumen Referensi | Path Relatif | Bagian yang Harus Diekstrak |
|----|-------------------|--------------|----------------------------|
| 1 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | Bab 2 (Prinsip FP: pure function, immutability, Result Pattern), Bab 3 (Konvensi Penamaan: `snake_case` fungsi, `PascalCase` NamedTuple), Bab 5 (Format kode PEP 8, max 120 char), Bab 6 (Docstring PEP 257 Google Style + header module), Bab 7 (Type Hints PEP 484), Bab 9 (Parameterized Query `%s`, `DECIMAL(15,4)` ↔ `decimal.Decimal`), Bab 10.2 (bcrypt Cost 12), Bab 14 (Testing Standards: konvensi `test_<modul>.py`, `test_<behavior>()`, coverage ≥ 90%, unit test terisolasi penuh dengan mock) |
| 2 | **Test Plan v1.2** | `docs/sdlc/05_testing/01_test_plan.md` | Bab 3.1.1 (Unit Testing: pure functions + mock NamedTuples, target coverage ≥ 90%), Bab 10.3 (Database `abucom_test_db` terisolasi), Bab 10.4 (Data Fixtures), Bab 11.3 (pytest 8.2.x + coverage 7.5.x), Bab 4.9-4.10 (Skenario M.9 Multi-Cabang `cabang_id` & M.10 System Configs) |
| 3 | **Test Cases v1.2** | `docs/sdlc/05_testing/02_test_cases.md` | Bab 1.7 (Konvensi ID: `TC-[MODUL]-[SKENARIO]-[URUT]`), Bab 3.2 (Prakondisi Global: seed.sql & schema.sql), Bab 3.4 (Entry/Exit Criteria), Bab 4.9-4.10 (Skenario M9 & M10) |
| 4 | **Source Module** | `db/seed_data.py` | Seluruh 449 baris: 8 fungsi publik (`generate_default_password_hash`, `seed_cabang_default`, `seed_pengguna_default`, `seed_saldo_ppob_default`, `seed_saldo_ewallet_default`, `seed_system_configs_default`, `verify_seed_integrity`, `run_seed_all`), 6 konstanta data (`DEFAULT_PASSWORD`, `DEFAULT_CABANG_DATA`, `DEFAULT_PENGGUNA_DATA`, `DEFAULT_SALDO_PPOB_DATA`, `DEFAULT_SALDO_EWALLET_DATA`, `DEFAULT_SYSTEM_CONFIGS_DATA`), 1 konstanta validasi (`EXPECTED_SEED_COUNTS`), 1 NamedTuple (`Result`) |
| 5 | **Existing Unit Test** | `tests/test_unit_seed_data.py` | Seluruh 904 baris: pelajari pola existing test untuk memahami konvensi mock, assertion, dan struktur yang sudah digunakan. **JANGAN duplikasi** test yang sudah ada — tambahkan yang belum ada. |

> **CATATAN**: File `docs/sdlc/narasi.txt` TIDAK diperlukan untuk issue ini karena cakupan bersifat teknis-internal (unit testing modul database seed), bukan narasi bisnis.

---

## 3. Rangkuman Detail Data dari Dokumen Referensi

### 3.1. Detail Modul Target (`db/seed_data.py`)

**NamedTuple Result Pattern:**
```python
Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
```

**Konstanta Data Default:**

| Konstanta | Tabel Target | Jumlah Baris | Detail Data |
|-----------|-------------|--------------|-------------|
| `DEFAULT_PASSWORD` | - | - | String `'admin123'` |
| `DEFAULT_CABANG_DATA` | `cabang` | 1 | `(1, 'Toko Pusat Bandung', 'Jl. Raya Percetakan No. 45, RT 02/RW 03, Kecamatan Sukamaju, Kota Bandung, Jawa Barat, 40123', '0227654321')` |
| `DEFAULT_PENGGUNA_DATA` | `pengguna` | 1 | `(1, 'Pemilik Usaha AbuCom', 'pemilik', 'pemilik', 0, 1)` — field: `id, nama_lengkap, username, role, failed_login_attempts, cabang_id` |
| `DEFAULT_SALDO_PPOB_DATA` | `saldo_ppob` | 2 | Tuple 2 baris: `('Pulsa_Data', Decimal('1000000.0000'), 1)` dan `('Token_Tagihan', Decimal('1500000.0000'), 1)` |
| `DEFAULT_SALDO_EWALLET_DATA` | `saldo_ewallet` | 6 | Tuple 6 baris: Mandiri Agen, Dana, Gopay, LinkAja, ShopeePay, OVO — masing-masing memiliki field `nama_ewallet, saldo_terakhir, biaya_admin_flat, biaya_admin_persen, limit_harian, cabang_id` |
| `DEFAULT_SYSTEM_CONFIGS_DATA` | `system_configs` | 13 | 13 parameter bisnis: `target_laba_payroll` (Rp 15.000.000), `porsi_gaji_laba` (25%), `limit_kasbon_staf` (Rp 1.000.000), `threshold_saldo_ppob` (Rp 150.000), `min_topup_ppob` (Rp 500.000), `toleransi_selisih_kas` (Rp 10.000), `poin_tier_1-4_rupiah` (Rp 500/1500/2500/5000), `threshold_pengeluaran` (Rp 500.000), `umr_daerah` (Rp 3.200.000), `dana_cadangan_darurat` (Rp 4.500.000) |
| `EXPECTED_SEED_COUNTS` | validasi | - | `{'cabang': 1, 'pengguna': 1, 'saldo_ppob': 2, 'saldo_ewallet': 6, 'system_configs': 13}` |

**Daftar 8 Fungsi Publik:**

| No | Fungsi | Parameter | Return | Error Code | Perilaku Idempoten |
|----|--------|-----------|--------|------------|-------------------|
| 1 | `generate_default_password_hash(password)` | `str` | `Result(is_success, hash_str, error_msg)` | `ERR-VAL-050` | N/A (pure function) |
| 2 | `seed_cabang_default(cursor)` | `Any` (mock cursor) | `Result(is_success, rows_inserted, error_msg)` | `ERR-DB-SEED-001` | Ya: skip jika `COUNT(*) > 0` pada `cabang WHERE id = 1` |
| 3 | `seed_pengguna_default(cursor, password_hash)` | `Any, str` | `Result(is_success, rows_inserted, error_msg)` | `ERR-DB-SEED-001` | Ya: skip jika `COUNT(*) > 0` pada `pengguna WHERE id = 1` |
| 4 | `seed_saldo_ppob_default(cursor)` | `Any` | `Result(is_success, rows_inserted, error_msg)` | `ERR-DB-SEED-001` | Ya: skip jika `COUNT(*) >= 2` pada `saldo_ppob` |
| 5 | `seed_saldo_ewallet_default(cursor)` | `Any` | `Result(is_success, rows_inserted, error_msg)` | `ERR-DB-SEED-001` | Ya: skip jika `COUNT(*) >= 6` pada `saldo_ewallet` |
| 6 | `seed_system_configs_default(cursor)` | `Any` | `Result(is_success, rows_inserted, error_msg)` | `ERR-DB-SEED-001` | Ya: skip jika `COUNT(*) >= 13` pada `system_configs` |
| 7 | `verify_seed_integrity(cursor)` | `Any` | `Result(is_success, report_dict/None, error_msg)` | `ERR-DB-SEED-001` | N/A (read-only verification) |
| 8 | `run_seed_all(db_connection)` | `Any` (mock connection) | `Result(is_success, stats_dict, error_msg)` | `ERR-DB-SEED-001` | Ya: orchestrator transaksional ACID |

### 3.2. Standar Testing dari Coding Standard v1.2

- **Bab 14.1**: Framework testing: `pytest` (bukan `unittest` runner).
- **Bab 14.2**: Target coverage ≥ 90% logika bisnis (`logic/` dan modul kritis lainnya).
- **Bab 14.3**: Nama file: `test_<modul_target>.py` di folder `tests/`. Nama fungsi: `test_<behavior_spesifik>()`.
- **Bab 14.4**: Unit test **WAJIB** terisolasi penuh, **DILARANG** koneksi fisik database. Mock via `MagicMock`.
- **Bab 2.2.6**: Result Pattern wajib: `Result(is_success, data, error_msg)`.
- **Bab 6.1-6.4**: Docstring PEP 257 Google Style + header module wajib.
- **Bab 7.1**: Type hints PEP 484 wajib pada semua fungsi publik.
- **Bab 5.3**: Batas panjang baris 120 karakter.
- **Bab 3.2**: Fungsi snake_case verb_noun.
- **Bab 5.5**: Single quote untuk string internal, double quote untuk display dan docstring.

### 3.3. Standar Testing dari Test Plan v1.2

- **Bab 3.1.1**: Unit testing target pure functions dengan mock NamedTuples.
- **Bab 10.3**: Database sandbox `abucom_test_db` — tetapi untuk unit test ini, gunakan **full mock** tanpa koneksi fisik.
- **Bab 10.4**: Data fixtures: 8 akun pengguna staf, master barang, dan parameter `system_configs`.
- **Bab 11.3.1**: Framework `pytest==8.2.x`.
- **Bab 11.3.2**: Pengukuran coverage `coverage==7.5.x`.

---

## 4. Batasan, Cakupan, dan Alur Pengerjaan

### 4.1. Cakupan (In-Scope)

Unit test ini **HANYA** mencakup:
1. Seluruh 8 fungsi publik di modul `db/seed_data.py`.
2. Seluruh 7 konstanta data publik di modul `db/seed_data.py`.
3. Validasi tipe data, jumlah baris, dan format nilai pada setiap konstanta.
4. Skenario positif (happy path), negatif (unhappy path / error handling), dan edge cases untuk setiap fungsi.
5. Verifikasi perilaku idempoten (skip insert jika data sudah ada).
6. Verifikasi transaksi ACID (commit pada sukses, rollback pada gagal).
7. Verifikasi error code `ERR-VAL-050` dan `ERR-DB-SEED-001`.

### 4.2. Luar Cakupan (Out-of-Scope)

- **DILARANG** menguji koneksi fisik database MySQL.
- **DILARANG** menguji modul lain (`db_connector.py`, `schema_initializer.py`, `query_builder.py`).
- **DILARANG** memodifikasi modul sumber `db/seed_data.py`.
- **DILARANG** menambahkan dependensi baru ke `requirements.txt`.
- **DILARANG** mengubah file test lainnya (`test_unit_db_connector.py`, `test_unit_schema_initializer.py`, dll).

### 4.3. Prinsip Isolasi

- Seluruh interaksi database di-mock menggunakan `unittest.mock.MagicMock`.
- Seluruh panggilan `bcrypt` yang membutuhkan waktu lama boleh di-mock via `@patch`.
- Setiap fungsi test **wajib** independen — tidak boleh bergantung pada hasil test lain.
- Setiap test **wajib** melakukan pembersihan/reset state mock sebelum eksekusi (clean state via fresh `MagicMock()` di setiap fungsi test).
- Gunakan pola `mock_cursor = MagicMock()` baru di **setiap** fungsi test, jangan pernah share mock antar test.

### 4.4. Alur Pengerjaan

```
┌──────────────────────────────────────────────────┐
│ 1. BACA dokumen referensi (Bab 2)                │
├──────────────────────────────────────────────────┤
│ 2. BACA source module db/seed_data.py (449 baris)│
├──────────────────────────────────────────────────┤
│ 3. BACA existing test (904 baris)                │
│    → identifikasi test yang SUDAH ADA            │
│    → identifikasi test yang BELUM ADA            │
├──────────────────────────────────────────────────┤
│ 4. TULIS test baru di tests/test_unit_seed_data.py│
│    → Tambahkan di BAWAH test existing            │
│    → Ikuti pola dan konvensi yang sudah ada      │
├──────────────────────────────────────────────────┤
│ 5. JALANKAN pytest untuk verifikasi              │
├──────────────────────────────────────────────────┤
│ 6. JALANKAN coverage untuk metrik                │
└──────────────────────────────────────────────────┘
```

---

## 5. Folder Penyimpanan dan Dependency

### 5.1. Lokasi File Test

| Item | Path |
|------|------|
| **File test target** | `tests/test_unit_seed_data.py` |
| **File module sumber** | `db/seed_data.py` |
| **Package init** | `tests/__init__.py` (sudah ada) |

### 5.2. Dependency Testing

| Library | Versi | Kegunaan |
|---------|-------|----------|
| `pytest` | `==8.2.0` | Framework test runner |
| `coverage` | `==7.5.1` | Pengukuran code coverage |
| `unittest.mock` | built-in | Mocking (`MagicMock`, `patch`) |
| `mysql-connector-python` | `==8.4.0` | Import `mysql.connector.Error` untuk mock exception |
| `bcrypt` | `==4.1.0` | Import untuk verifikasi hash format `$2b$12$` |
| `decimal` | built-in | `Decimal` untuk verifikasi presisi data |

### 5.3. Perintah Eksekusi

```bash
# Jalankan semua test di file target
python -m pytest tests/test_unit_seed_data.py -v

# Jalankan dengan coverage
python -m coverage run -m pytest tests/test_unit_seed_data.py -v
python -m coverage report --show-missing --include="db/seed_data.py"
```

---

## 6. Konvensi Penulisan Test

### 6.1. Header Module (Wajib)

```python
"""
Nama Modul: test_unit_seed_data.py
Deskripsi: Unit test terisolasi (mocked) untuk modul db/seed_data.py.
           Menguji seluruh fungsi hashing password default, seeding data cabang,
           pengguna, saldo_ppob, saldo_ewallet, system_configs secara idempoten,
           verifikasi integritas, dan run_seed_all secara transaksional ACID.
Author: [Nama Pengembang / AI Asisten]
Tanggal: [YYYY-MM-DD]
"""
```

### 6.2. Konvensi Penamaan Fungsi Test

Format: `test_<nama_fungsi_target>_<skenario_spesifik>()`

Contoh:
- `test_generate_default_password_hash_sukses()`
- `test_seed_cabang_default_skip_jika_ada()`
- `test_seed_system_configs_default_insert_semua_13_parameter()`
- `test_run_seed_all_rollback_saat_cabang_gagal()`

### 6.3. Konvensi Docstring Fungsi Test

Setiap fungsi test **WAJIB** memiliki docstring singkat yang berisi:
```python
def test_nama_fungsi_skenario() -> None:
    """Memverifikasi [perilaku yang diuji].

    Skenario: [Positif/Negatif/Edge Case]
    Target: [nama_fungsi_yang_diuji]
    """
```

### 6.4. Konvensi Import

```python
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
```

### 6.5. Pola Helper untuk MySQL Error

```python
def _make_mysql_error(errno: int, msg: str) -> mysql.connector.Error:
    """Helper untuk membuat mysql.connector.Error dengan errno dan msg."""
    err = mysql.connector.Error()
    err.errno = errno
    err.msg = msg
    return err
```

### 6.6. Pola Clean State per Test

Setiap fungsi test **WAJIB** membuat instance `MagicMock()` baru:
```python
def test_contoh() -> None:
    """..."""
    mock_cursor = MagicMock()       # ← fresh mock per test
    mock_cursor.fetchone.return_value = (0,)
    # ... rest of test
```

**DILARANG** menggunakan `@pytest.fixture` yang di-share antar test untuk mock cursor/connection karena bisa menimbulkan state leak.

---

## 7. Skenario Test — Daftar Lengkap

### 7.1. Inventarisasi Test Existing (SUDAH ADA — Jangan Duplikasi)

Berikut adalah test yang **sudah ada** di `tests/test_unit_seed_data.py` (904 baris). **JANGAN** menulis ulang test ini:

| No | Nama Fungsi Test | Skenario | Target |
|----|-----------------|----------|--------|
| 1 | `test_generate_default_password_hash_sukses` | Positif | `generate_default_password_hash` |
| 2 | `test_generate_default_password_hash_gagal_kosong` | Negatif | `generate_default_password_hash` |
| 3 | `test_generate_default_password_hash_gagal_format_invalid` | Negatif | `generate_default_password_hash` |
| 4 | `test_generate_default_password_hash_exception` | Negatif | `generate_default_password_hash` |
| 5 | `test_seed_cabang_default_skip_jika_ada` | Positif | `seed_cabang_default` |
| 6 | `test_seed_cabang_default_insert_jika_kosong` | Positif | `seed_cabang_default` |
| 7 | `test_seed_cabang_default_mysql_error` | Negatif | `seed_cabang_default` |
| 8 | `test_seed_cabang_default_general_exception` | Negatif | `seed_cabang_default` |
| 9 | `test_seed_pengguna_default_skip_jika_ada` | Positif | `seed_pengguna_default` |
| 10 | `test_seed_pengguna_default_insert_jika_kosong` | Positif | `seed_pengguna_default` |
| 11 | `test_seed_pengguna_default_mysql_error` | Negatif | `seed_pengguna_default` |
| 12 | `test_seed_saldo_ppob_default_skip_jika_cukup` | Positif | `seed_saldo_ppob_default` |
| 13 | `test_seed_saldo_ppob_default_insert_jika_kosong` | Positif | `seed_saldo_ppob_default` |
| 14 | `test_seed_saldo_ppob_default_mysql_error` | Negatif | `seed_saldo_ppob_default` |
| 15 | `test_seed_saldo_ewallet_default_skip_jika_cukup` | Positif | `seed_saldo_ewallet_default` |
| 16 | `test_seed_saldo_ewallet_default_insert_jika_kosong` | Positif | `seed_saldo_ewallet_default` |
| 17 | `test_seed_saldo_ewallet_default_mysql_error` | Negatif | `seed_saldo_ewallet_default` |
| 18 | `test_seed_system_configs_default_skip_jika_cukup` | Positif | `seed_system_configs_default` |
| 19 | `test_seed_system_configs_default_insert_jika_kosong` | Positif | `seed_system_configs_default` |
| 20 | `test_seed_system_configs_default_mysql_error` | Negatif | `seed_system_configs_default` |
| 21 | `test_verify_seed_integrity_valid_sempurna` | Positif | `verify_seed_integrity` |
| 22 | `test_verify_seed_integrity_mismatch_counts` | Negatif | `verify_seed_integrity` |
| 23 | `test_verify_seed_integrity_mismatch_password_hash` | Negatif | `verify_seed_integrity` |
| 24 | `test_verify_seed_integrity_mismatch_unique_keys` | Negatif | `verify_seed_integrity` |
| 25 | `test_verify_seed_integrity_no_user_found` | Negatif | `verify_seed_integrity` |
| 26 | `test_verify_seed_integrity_mysql_error` | Negatif | `verify_seed_integrity` |
| 27 | `test_run_seed_all_sukses_komplit` | Positif | `run_seed_all` |
| 28 | `test_run_seed_all_gagal_koneksi_none` | Negatif | `run_seed_all` |
| 29 | `test_run_seed_all_gagal_gen_hash` | Negatif | `run_seed_all` |
| 30 | `test_run_seed_all_gagal_seed_cabang_dan_rollback` | Negatif | `run_seed_all` |
| 31 | `test_run_seed_all_gagal_seed_pengguna_dan_rollback` | Negatif | `run_seed_all` |
| 32 | `test_run_seed_all_gagal_seed_ppob_dan_rollback` | Negatif | `run_seed_all` |
| 33 | `test_run_seed_all_gagal_seed_ewallet_dan_rollback` | Negatif | `run_seed_all` |
| 34 | `test_run_seed_all_gagal_seed_configs_dan_rollback` | Negatif | `run_seed_all` |
| 35 | `test_run_seed_all_gagal_verifikasi_dan_return_fail` | Negatif | `run_seed_all` |
| 36 | `test_run_seed_all_general_exception_handling` | Negatif | `run_seed_all` |
| 37 | `test_konstanta_konsistensi_dan_tipe` | Positif | Konstanta |
| 38 | `test_generate_default_password_hash_wrong_prefix` | Negatif | `generate_default_password_hash` |
| 39 | `test_seed_pengguna_default_general_exception` | Negatif | `seed_pengguna_default` |
| 40 | `test_seed_saldo_ppob_default_general_exception` | Negatif | `seed_saldo_ppob_default` |
| 41 | `test_seed_saldo_ewallet_default_general_exception` | Negatif | `seed_saldo_ewallet_default` |
| 42 | `test_seed_system_configs_default_general_exception` | Negatif | `seed_system_configs_default` |
| 43 | `test_verify_seed_integrity_general_exception` | Negatif | `verify_seed_integrity` |
| 44 | `test_run_seed_all_mysql_error_in_transaction` | Negatif | `run_seed_all` |
| 45 | `test_run_seed_all_rollback_exception_handling` | Negatif | `run_seed_all` |

### 7.2. Skenario Test BARU yang Wajib Ditambahkan

Berikut adalah skenario test **BARU** yang belum ada dan **WAJIB** ditambahkan. Setiap skenario ditulis dengan instruksi **langkah demi langkah** agar tidak ambigu:

---

#### GRUP A: generate_default_password_hash — Edge Cases Tambahan

**A1. Test: Password dengan karakter spesial unicode**
```
Nama  : test_generate_default_password_hash_karakter_unicode
Jenis : Positif / Edge Case
Target: generate_default_password_hash
Langkah:
  1. Panggil generate_default_password_hash("P@$$wörd_日本語!#2026")
  2. Assert res.is_success is True
  3. Assert res.data dimulai dengan '$2b$12$'
  4. Assert res.error_msg is None
  5. Assert panjang res.data >= 59 (standar panjang bcrypt hash)
Tujuan: Membuktikan bcrypt mampu meng-hash password dengan karakter unicode/spesial.
```

**A2. Test: Password sangat panjang (batas bcrypt 72 bytes)**
```
Nama  : test_generate_default_password_hash_panjang_72_bytes
Jenis : Edge Case / Boundary
Target: generate_default_password_hash
Langkah:
  1. Buat password_panjang = "A" * 72  (tepat 72 karakter ASCII = 72 bytes)
  2. Panggil generate_default_password_hash(password_panjang)
  3. Assert res.is_success is True
  4. Assert res.data dimulai dengan '$2b$12$'
Tujuan: Membuktikan bcrypt bekerja pada batas maksimum 72 bytes input.
```

**A3. Test: Password hanya whitespace**
```
Nama  : test_generate_default_password_hash_whitespace_only
Jenis : Edge Case
Target: generate_default_password_hash
Langkah:
  1. Panggil generate_default_password_hash("   ")  (3 spasi)
  2. Assert res.is_success is True  (whitespace adalah string non-kosong yang valid)
  3. Assert res.data dimulai dengan '$2b$12$'
Tujuan: Memastikan whitespace-only dianggap password valid (karena pengecekan hanya `if not password`).
```

---

#### GRUP B: seed_cabang_default — Edge Cases Tambahan

**B1. Test: Verifikasi exact SQL query dan parameter INSERT**
```
Nama  : test_seed_cabang_default_verifikasi_query_insert_exact
Jenis : Validasi Input
Target: seed_cabang_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (0,)
  3. Panggil seed_cabang_default(mock_cursor)
  4. Assert mock_cursor.execute dipanggil tepat 2 kali
  5. Assert panggilan pertama = ("SELECT COUNT(*) FROM cabang WHERE id = %s", (1,))
  6. Assert panggilan kedua = ("INSERT INTO cabang (id, nama_cabang, alamat, telp) VALUES (%s, %s, %s, %s)", DEFAULT_CABANG_DATA)
  7. Assert DEFAULT_CABANG_DATA[0] == 1 (verifikasi id cabang default)
  8. Assert DEFAULT_CABANG_DATA[1] == 'Toko Pusat Bandung' (nama cabang)
  9. Assert '0227654321' in DEFAULT_CABANG_DATA (telp)
Tujuan: Validasi keakuratan query SQL parameterized yang dikirim ke database.
```

**B2. Test: Verifikasi cabang skip return data = 0**
```
Nama  : test_seed_cabang_default_skip_return_data_nol
Jenis : Positif
Target: seed_cabang_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (5,)  (lebih dari 0, banyak cabang)
  3. Panggil res = seed_cabang_default(mock_cursor)
  4. Assert res.is_success is True
  5. Assert res.data == 0  (tidak ada insert karena sudah ada)
  6. Assert res.error_msg is None
Tujuan: Verifikasi idempoten dengan jumlah cabang lebih dari 1.
```

---

#### GRUP C: seed_pengguna_default — Edge Cases Tambahan

**C1. Test: Verifikasi exact parameter order untuk INSERT pengguna**
```
Nama  : test_seed_pengguna_default_verifikasi_urutan_params_insert
Jenis : Validasi Input
Target: seed_pengguna_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (0,)
  3. Buat hash_val = "$2b$12$testHashSample1234567890"
  4. Panggil res = seed_pengguna_default(mock_cursor, hash_val)
  5. Tangkap argumen panggilan kedua mock_cursor.execute
  6. Verifikasi params tuple urutan: (1, 'Pemilik Usaha AbuCom', 'pemilik', hash_val, 'pemilik', 0, None, 1)
  7. Assert posisi ke-6 (locked_until) is None
  8. Assert posisi ke-7 (cabang_id) == 1
Tujuan: Memastikan urutan kolom INSERT sesuai skema database dan locked_until diisi None.
```

**C2. Test: Verifikasi hash kosong string (bukan None)**
```
Nama  : test_seed_pengguna_default_hash_kosong_string
Jenis : Edge Case
Target: seed_pengguna_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (0,)
  3. Panggil res = seed_pengguna_default(mock_cursor, "")
  4. Assert res.is_success is True  (fungsi tidak memvalidasi hash, hanya melakukan insert)
  5. Assert res.data == 1
Tujuan: Membuktikan seed_pengguna_default tidak memvalidasi format hash — itu tanggung jawab generate_default_password_hash.
```

---

#### GRUP D: seed_saldo_ppob_default — Edge Cases Tambahan

**D1. Test: Verifikasi exact jumlah execute calls (1 check + 2 inserts)**
```
Nama  : test_seed_saldo_ppob_default_jumlah_execute_calls
Jenis : Validasi Input
Target: seed_saldo_ppob_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (0,)
  3. Set mock_cursor.rowcount = 1
  4. Panggil res = seed_saldo_ppob_default(mock_cursor)
  5. Assert mock_cursor.execute.call_count == 3  (1 SELECT COUNT + 2 INSERT)
  6. Assert res.data == 2
Tujuan: Memverifikasi jumlah query yang dieksekusi sesuai jumlah baris data.
```

**D2. Test: Verifikasi partial count (1 dari 2 sudah ada)**
```
Nama  : test_seed_saldo_ppob_default_skip_jika_partial_1
Jenis : Edge Case / Boundary
Target: seed_saldo_ppob_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (1,)  (ada 1, kurang dari 2)
  3. Set mock_cursor.rowcount = 1
  4. Panggil res = seed_saldo_ppob_default(mock_cursor)
  5. Assert res.is_success is True
  6. Assert res.data == 2  (tetap insert 2 karena menggunakan INSERT IGNORE)
Tujuan: Memverifikasi perilaku ketika data partial ada — fungsi tetap insert karena count < expected.
```

---

#### GRUP E: seed_saldo_ewallet_default — Edge Cases Tambahan

**E1. Test: Verifikasi exact jumlah execute calls (1 check + 6 inserts)**
```
Nama  : test_seed_saldo_ewallet_default_jumlah_execute_calls_detail
Jenis : Validasi Input
Target: seed_saldo_ewallet_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (0,)
  3. Set mock_cursor.rowcount = 1
  4. Panggil res = seed_saldo_ewallet_default(mock_cursor)
  5. Assert mock_cursor.execute.call_count == 7  (1 SELECT + 6 INSERT)
  6. Verifikasi bahwa setiap INSERT menggunakan query:
     "INSERT IGNORE INTO saldo_ewallet (nama_ewallet, saldo_terakhir, biaya_admin_flat, biaya_admin_persen, limit_harian, cabang_id) VALUES (%s, %s, %s, %s, %s, %s)"
  7. Assert res.data == 6
Tujuan: Memverifikasi semua 6 akun e-wallet diinsert dengan query yang benar.
```

**E2. Test: Verifikasi nama-nama ewallet yang diinsert**
```
Nama  : test_seed_saldo_ewallet_default_verifikasi_nama_ewallet
Jenis : Validasi Input
Target: seed_saldo_ewallet_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (0,)
  3. Set mock_cursor.rowcount = 1
  4. Panggil seed_saldo_ewallet_default(mock_cursor)
  5. Kumpulkan semua argumen panggilan execute (skip panggilan pertama SELECT)
  6. Ekstrak nama_ewallet dari parameter tuple indeks ke-0
  7. Assert daftar nama = ['Mandiri Agen', 'Dana', 'Gopay', 'LinkAja', 'ShopeePay', 'OVO']
Tujuan: Memastikan seluruh 6 akun e-wallet yang disebutkan di narasi bisnis terdaftar.
```

**E3. Test: Verifikasi partial count ewallet (5 dari 6)**
```
Nama  : test_seed_saldo_ewallet_default_skip_jika_partial_5
Jenis : Edge Case / Boundary
Target: seed_saldo_ewallet_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (5,)  (ada 5, kurang dari 6)
  3. Set mock_cursor.rowcount = 1
  4. Panggil res = seed_saldo_ewallet_default(mock_cursor)
  5. Assert res.is_success is True
  6. Assert res.data == 6  (tetap insert karena 5 < 6)
Tujuan: Boundary test — perilaku saat data mendekati tapi belum mencapai threshold.
```

---

#### GRUP F: seed_system_configs_default — Edge Cases Tambahan

**F1. Test: Verifikasi semua 13 parameter_key yang diinsert**
```
Nama  : test_seed_system_configs_default_verifikasi_semua_parameter_keys
Jenis : Validasi Input
Target: seed_system_configs_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (0,)
  3. Set mock_cursor.rowcount = 1
  4. Panggil seed_system_configs_default(mock_cursor)
  5. Kumpulkan semua argumen panggilan execute (skip SELECT pertama)
  6. Ekstrak parameter_key dari parameter tuple indeks ke-0
  7. Assert daftar keys mengandung TEPAT: [
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
  8. Assert panjang list == 13
Tujuan: Memastikan semua 13 parameter konfigurasi bisnis AbuCom terdaftar tanpa ada yang terlewat.
```

**F2. Test: Verifikasi Decimal di-cast ke string sebelum INSERT**
```
Nama  : test_seed_system_configs_default_decimal_cast_to_string
Jenis : Validasi Input
Target: seed_system_configs_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (0,)
  3. Set mock_cursor.rowcount = 1
  4. Panggil seed_system_configs_default(mock_cursor)
  5. Untuk SETIAP panggilan INSERT (skip panggilan SELECT pertama):
     a. Ambil parameter tuple
     b. Assert posisi ke-1 (parameter_value) bertipe str (bukan Decimal)
     c. Assert posisi ke-1 dapat di-parse kembali ke Decimal tanpa error
  6. Verifikasi spesifik: 'target_laba_payroll' → parameter_value == '15000000.0000'
  7. Verifikasi spesifik: 'porsi_gaji_laba' → parameter_value == '0.2500'
Tujuan: Memastikan konversi Decimal→str dilakukan sebelum query DML sesuai standar Coding Standard Bab 9.7.
```

**F3. Test: Verifikasi tipe_data kolom selalu 'DECIMAL'**
```
Nama  : test_seed_system_configs_default_tipe_data_selalu_decimal
Jenis : Validasi Input
Target: seed_system_configs_default
Langkah:
  1. Iterasi seluruh DEFAULT_SYSTEM_CONFIGS_DATA
  2. Untuk setiap row, assert row[2] == 'DECIMAL'
Tujuan: Memastikan semua config parameter bertipe DECIMAL konsisten.
```

**F4. Test: Verifikasi cabang_id selalu 1 untuk semua configs**
```
Nama  : test_seed_system_configs_default_cabang_id_selalu_1
Jenis : Validasi Input
Target: seed_system_configs_default
Langkah:
  1. Iterasi seluruh DEFAULT_SYSTEM_CONFIGS_DATA
  2. Untuk setiap row, assert row[4] == 1
Tujuan: Memastikan semua configs terikat ke cabang_id = 1 (Toko Pusat default, mendukung arsitektur Multi-Cabang M.9).
```

**F5. Test: Verifikasi boundary partial count (12 dari 13)**
```
Nama  : test_seed_system_configs_default_skip_jika_partial_12
Jenis : Edge Case / Boundary
Target: seed_system_configs_default
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set mock_cursor.fetchone.return_value = (12,)  (12 < 13)
  3. Set mock_cursor.rowcount = 1
  4. Panggil res = seed_system_configs_default(mock_cursor)
  5. Assert res.is_success is True
  6. Assert res.data == 13  (tetap insert karena 12 < 13)
Tujuan: Boundary test — 12 baris ada, 1 baris kurang.
```

---

#### GRUP G: verify_seed_integrity — Edge Cases Tambahan

**G1. Test: Verifikasi multiple mismatch errors dikumpulkan**
```
Nama  : test_verify_seed_integrity_multiple_errors_combined
Jenis : Negatif
Target: verify_seed_integrity
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set fetchone side_effect: [(0,), (0,), (0,), (0,), (0,), None, (0,)]
     — semua count = 0 (mismatch), user tidak ditemukan
  3. Panggil res = verify_seed_integrity(mock_cursor)
  4. Assert res.is_success is False
  5. Assert "cabang" in res.error_msg dan "pengguna" in res.error_msg
  6. Assert "akun pemilik default id = 1 tidak ditemukan" in res.error_msg
Tujuan: Membuktikan fungsi mengumpulkan SEMUA error, bukan berhenti di error pertama.
```

**G2. Test: Verifikasi report dict dikembalikan meskipun gagal**
```
Nama  : test_verify_seed_integrity_report_dict_on_failure
Jenis : Negatif
Target: verify_seed_integrity
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set fetchone side_effect: [(1,), (1,), (2,), (6,), (10,), ('$2b$12$valid',), (13,)]
     — system_configs 10 bukan 13
  3. Panggil res = verify_seed_integrity(mock_cursor)
  4. Assert res.is_success is False
  5. Assert res.data is not None (report dict masih dikembalikan)
  6. Assert res.data['system_configs'] == 10
Tujuan: Verifikasi bahwa report dict dikembalikan meskipun ada mismatch.
```

**G3. Test: Verifikasi password hash kosong string (bukan None)**
```
Nama  : test_verify_seed_integrity_password_hash_kosong
Jenis : Edge Case
Target: verify_seed_integrity
Langkah:
  1. Buat mock_cursor = MagicMock()
  2. Set fetchone side_effect: [(1,), (1,), (2,), (6,), (13,), ('',), (13,)]
     — password_hash empty string
  3. Panggil res = verify_seed_integrity(mock_cursor)
  4. Assert res.is_success is False
  5. Assert "bcrypt Cost 12" in res.error_msg
Tujuan: Verifikasi deteksi password hash kosong.
```

---

#### GRUP H: run_seed_all — Edge Cases Tambahan

**H1. Test: Verifikasi semua sub-seed dipanggil dalam urutan benar**
```
Nama  : test_run_seed_all_urutan_pemanggilan_benar
Jenis : Positif
Target: run_seed_all
Langkah:
  1. Mock semua 7 fungsi sub-seed + generate_hash
  2. Set semua return Result(True, ..., None)
  3. Panggil run_seed_all(mock_conn)
  4. Verifikasi urutan panggilan:
     a. generate_default_password_hash dipanggil PERTAMA
     b. seed_cabang_default dipanggil KEDUA
     c. seed_pengguna_default dipanggil KETIGA
     d. seed_saldo_ppob_default dipanggil KEEMPAT
     e. seed_saldo_ewallet_default dipanggil KELIMA
     f. seed_system_configs_default dipanggil KEENAM
     g. verify_seed_integrity dipanggil TERAKHIR (setelah commit)
Tujuan: Urutan dependensi kritis — cabang harus ada sebelum pengguna (foreign key).
```

**H2. Test: Verifikasi stats dict lengkap pada sukses**
```
Nama  : test_run_seed_all_stats_dict_lengkap
Jenis : Positif
Target: run_seed_all
Langkah:
  1. Mock semua sub-seed sukses
  2. Panggil res = run_seed_all(mock_conn)
  3. Assert res.data berisi semua key:
     - 'cabang_inserted'
     - 'pengguna_inserted'
     - 'saldo_ppob_inserted'
     - 'saldo_ewallet_inserted'
     - 'system_configs_inserted'
     - 'report'
  4. Assert len(res.data) == 6
Tujuan: Memastikan laporan statistik lengkap.
```

**H3. Test: Verifikasi cursor.close dipanggil meskipun commit error**
```
Nama  : test_run_seed_all_cursor_close_saat_commit_error
Jenis : Negatif
Target: run_seed_all
Langkah:
  1. Mock semua sub-seed sukses
  2. Set mock_conn.commit.side_effect = RuntimeError("Commit crash")
  3. Panggil res = run_seed_all(mock_conn)
  4. Assert res.is_success is False
  5. Assert mock_cursor.close.assert_called_once()
  6. Assert mock_conn.rollback.assert_called_once()
Tujuan: Resource cleanup — cursor harus ditutup meskipun commit gagal.
```

**H4. Test: Verifikasi idempoten — run_seed_all saat semua data sudah ada**
```
Nama  : test_run_seed_all_idempoten_semua_data_sudah_ada
Jenis : Positif / Idempoten
Target: run_seed_all
Langkah:
  1. Mock generate_hash → Result(True, "$2b$12$hashed", None)
  2. Mock semua sub-seed → Result(True, 0, None)  (semua return data=0 = skip)
  3. Mock verify → Result(True, EXPECTED_SEED_COUNTS, None)
  4. Panggil res = run_seed_all(mock_conn)
  5. Assert res.is_success is True
  6. Assert res.data['cabang_inserted'] == 0
  7. Assert res.data['pengguna_inserted'] == 0
  8. Assert res.data['saldo_ppob_inserted'] == 0
  9. Assert res.data['saldo_ewallet_inserted'] == 0
  10. Assert res.data['system_configs_inserted'] == 0
Tujuan: Membuktikan run_seed_all aman dijalankan berulang kali (idempoten).
```

---

#### GRUP I: Konstanta Data — Validasi Lanjutan

**I1. Test: Verifikasi nilai Decimal presisi 4 digit pada system_configs**
```
Nama  : test_konstanta_system_configs_presisi_4_digit_decimal
Jenis : Validasi Input
Target: DEFAULT_SYSTEM_CONFIGS_DATA
Langkah:
  1. Untuk setiap row di DEFAULT_SYSTEM_CONFIGS_DATA:
     a. Ambil value = row[1] (Decimal)
     b. Assert str(value) mengandung tepat 4 digit setelah titik desimal
     c. Contoh: '15000000.0000' → 4 digit setelah '.'
Tujuan: Memastikan presisi Decimal(15,4) konsisten sesuai standar database schema.
```

**I2. Test: Verifikasi nilai spesifik parameter bisnis kritis**
```
Nama  : test_konstanta_system_configs_nilai_bisnis_kritis
Jenis : Validasi Input
Target: DEFAULT_SYSTEM_CONFIGS_DATA
Langkah:
  1. Buat dict dari DEFAULT_SYSTEM_CONFIGS_DATA: {row[0]: row[1] for row in data}
  2. Assert dict['target_laba_payroll'] == Decimal('15000000.0000')
  3. Assert dict['porsi_gaji_laba'] == Decimal('0.2500')
  4. Assert dict['toleransi_selisih_kas'] == Decimal('10000.0000')
  5. Assert dict['umr_daerah'] == Decimal('3200000.0000')
  6. Assert dict['threshold_pengeluaran'] == Decimal('500000.0000')
  7. Assert dict['poin_tier_1_rupiah'] == Decimal('500.0000')
  8. Assert dict['poin_tier_2_rupiah'] == Decimal('1500.0000')
  9. Assert dict['poin_tier_3_rupiah'] == Decimal('2500.0000')
  10. Assert dict['poin_tier_4_rupiah'] == Decimal('5000.0000')
  11. Assert dict['dana_cadangan_darurat'] == Decimal('4500000.0000')
Tujuan: Memastikan parameter bisnis tidak berubah dari spesifikasi SRS dan narasi pemilik usaha.
```

**I3. Test: Verifikasi default cabang data lengkap**
```
Nama  : test_konstanta_default_cabang_data_lengkap
Jenis : Validasi Input
Target: DEFAULT_CABANG_DATA
Langkah:
  1. Assert len(DEFAULT_CABANG_DATA) == 4
  2. Assert DEFAULT_CABANG_DATA[0] == 1 (id)
  3. Assert isinstance(DEFAULT_CABANG_DATA[1], str) (nama_cabang)
  4. Assert isinstance(DEFAULT_CABANG_DATA[2], str) (alamat)
  5. Assert isinstance(DEFAULT_CABANG_DATA[3], str) (telp)
  6. Assert len(DEFAULT_CABANG_DATA[1]) > 0  (nama tidak kosong)
  7. Assert len(DEFAULT_CABANG_DATA[2]) > 0  (alamat tidak kosong)
  8. Assert len(DEFAULT_CABANG_DATA[3]) > 0  (telp tidak kosong)
Tujuan: Validasi kelengkapan dan tipe data cabang default.
```

**I4. Test: Verifikasi default pengguna data lengkap**
```
Nama  : test_konstanta_default_pengguna_data_lengkap
Jenis : Validasi Input
Target: DEFAULT_PENGGUNA_DATA
Langkah:
  1. Assert len(DEFAULT_PENGGUNA_DATA) == 6
  2. Assert DEFAULT_PENGGUNA_DATA[0] == 1 (id)
  3. Assert DEFAULT_PENGGUNA_DATA[2] == 'pemilik' (username)
  4. Assert DEFAULT_PENGGUNA_DATA[3] == 'pemilik' (role)
  5. Assert DEFAULT_PENGGUNA_DATA[4] == 0 (failed_login_attempts awal)
  6. Assert DEFAULT_PENGGUNA_DATA[5] == 1 (cabang_id referensi cabang default)
Tujuan: Validasi data pengguna default sesuai ACM — role pemilik memiliki hak akses penuh.
```

**I5. Test: Verifikasi saldo awal PPOB sesuai narasi bisnis**
```
Nama  : test_konstanta_saldo_ppob_nilai_dan_tipe
Jenis : Validasi Input
Target: DEFAULT_SALDO_PPOB_DATA
Langkah:
  1. Assert len(DEFAULT_SALDO_PPOB_DATA) == 2
  2. Assert DEFAULT_SALDO_PPOB_DATA[0][0] == 'Pulsa_Data'
  3. Assert DEFAULT_SALDO_PPOB_DATA[1][0] == 'Token_Tagihan'
  4. Assert DEFAULT_SALDO_PPOB_DATA[0][1] == Decimal('1000000.0000')
  5. Assert DEFAULT_SALDO_PPOB_DATA[1][1] == Decimal('1500000.0000')
  6. Assert DEFAULT_SALDO_PPOB_DATA[0][2] == 1  (cabang_id)
  7. Assert DEFAULT_SALDO_PPOB_DATA[1][2] == 1  (cabang_id)
Tujuan: Verifikasi 2 jenis akun PPOB (sesuai narasi: pulsa HP/data dan token/tagihan listrik).
```

**I6. Test: Verifikasi EXPECTED_SEED_COUNTS total**
```
Nama  : test_konstanta_expected_seed_counts_total_dan_keys
Jenis : Validasi Input
Target: EXPECTED_SEED_COUNTS
Langkah:
  1. Assert len(EXPECTED_SEED_COUNTS) == 5
  2. Assert set(EXPECTED_SEED_COUNTS.keys()) == {'cabang', 'pengguna', 'saldo_ppob', 'saldo_ewallet', 'system_configs'}
  3. Assert sum(EXPECTED_SEED_COUNTS.values()) == 23  (1+1+2+6+13)
Tujuan: Verifikasi kunci dan total baris yang diharapkan.
```

**I7. Test: Verifikasi DEFAULT_PASSWORD tidak kosong dan sesuai**
```
Nama  : test_konstanta_default_password_valid
Jenis : Validasi Input
Target: DEFAULT_PASSWORD
Langkah:
  1. Assert isinstance(DEFAULT_PASSWORD, str)
  2. Assert len(DEFAULT_PASSWORD) > 0
  3. Assert DEFAULT_PASSWORD == 'admin123'
Tujuan: Memastikan password default terdefinisi.
```

---

## 8. Low-Level Execution Checklist

Ikuti checklist di bawah ini **secara berurutan, langkah demi langkah**:

### Fase 1: Persiapan dan Pembacaan

- [ ] **1.1** Baca file `docs/sdlc/04_implementation/01_coding_standard.md` Bab 2, 3, 5, 6, 7, 9, 14. Ekstrak konvensi penamaan, docstring, type hints, dan aturan testing.
- [ ] **1.2** Baca file `docs/sdlc/05_testing/01_test_plan.md` Bab 3.1.1, 10.3, 10.4, 11.3. Ekstrak strategi unit test dan dependency.
- [ ] **1.3** Baca file `docs/sdlc/05_testing/02_test_cases.md` Bab 1.7, 3.2, 3.4. Ekstrak konvensi ID dan entry/exit criteria.
- [ ] **1.4** Baca file `db/seed_data.py` seluruhnya (449 baris). Pahami setiap fungsi, konstanta, dan flow control.
- [ ] **1.5** Baca file `tests/test_unit_seed_data.py` seluruhnya (904 baris). Identifikasi **45 test existing** yang tercantum di Bab 7.1.
- [ ] **1.6** Identifikasi **gap** — test apa saja yang belum ada berdasarkan Bab 7.2.

### Fase 2: Penulisan Test Baru

- [ ] **2.1** Buka file `tests/test_unit_seed_data.py`.
- [ ] **2.2** **JANGAN** mengubah header module, import, helper function, atau test yang sudah ada.
- [ ] **2.3** Posisikan cursor di **baris terakhir** file (setelah baris 904).
- [ ] **2.4** Tambahkan komentar separator section baru:
  ```python
  # ==============================================================================
  # Skenario Test Tambahan — Issue #0097
  # ==============================================================================
  ```
- [ ] **2.5** Tulis test GRUP A (3 test): `generate_default_password_hash` edge cases.
- [ ] **2.6** Tulis test GRUP B (2 test): `seed_cabang_default` edge cases.
- [ ] **2.7** Tulis test GRUP C (2 test): `seed_pengguna_default` edge cases.
- [ ] **2.8** Tulis test GRUP D (2 test): `seed_saldo_ppob_default` edge cases.
- [ ] **2.9** Tulis test GRUP E (3 test): `seed_saldo_ewallet_default` edge cases.
- [ ] **2.10** Tulis test GRUP F (5 test): `seed_system_configs_default` edge cases.
- [ ] **2.11** Tulis test GRUP G (3 test): `verify_seed_integrity` edge cases.
- [ ] **2.12** Tulis test GRUP H (4 test): `run_seed_all` edge cases.
- [ ] **2.13** Tulis test GRUP I (7 test): Konstanta data validasi.

### Fase 3: Validasi Kualitas Kode

- [ ] **3.1** Pastikan setiap fungsi test memiliki **docstring PEP 257** yang lengkap.
- [ ] **3.2** Pastikan setiap fungsi test memiliki **type hint return** `-> None`.
- [ ] **3.3** Pastikan **tidak ada** fungsi test yang berisi komentar `# TODO` atau `# FIXME`.
- [ ] **3.4** Pastikan **tidak ada** fungsi test yang kosong atau hanya berisi `pass`.
- [ ] **3.5** Pastikan setiap fungsi test menggunakan **MagicMock() baru** (clean state).
- [ ] **3.6** Pastikan panjang setiap baris **tidak melebihi 120 karakter**.
- [ ] **3.7** Pastikan import di atas file **tidak diubah** dari yang sudah ada.
- [ ] **3.8** Pastikan **tidak ada duplikasi** dengan 45 test existing di Bab 7.1.

### Fase 4: Eksekusi dan Verifikasi

- [ ] **4.1** Jalankan `python -m pytest tests/test_unit_seed_data.py -v` dari root proyek.
- [ ] **4.2** Pastikan **SELURUH test PASS** (0 FAIL, 0 ERROR).
- [ ] **4.3** Jalankan `python -m coverage run -m pytest tests/test_unit_seed_data.py -v`.
- [ ] **4.4** Jalankan `python -m coverage report --show-missing --include="db/seed_data.py"`.
- [ ] **4.5** Pastikan coverage modul `db/seed_data.py` ≥ 90%.
- [ ] **4.6** Jika ada test yang FAIL, analisis error message, perbaiki assertion, dan ulangi dari langkah 4.1.
- [ ] **4.7** Pastikan test baru **tidak merusak** test existing yang sebelumnya sudah PASS.

### Fase 5: Final Review

- [ ] **5.1** Hitung total fungsi test di file. Target: **45 existing + 31 baru = 76 fungsi test**.
- [ ] **5.2** Review ulang bahwa setiap skenario di Bab 7.2 sudah terwakili.
- [ ] **5.3** Verifikasi format konsisten dengan pola test existing (spacing, docstring, assertion style).
- [ ] **5.4** Commit dengan message: `test: tambah 31 skenario unit test seed data (Issue #0097)`.

---

## 9. Ringkasan Jumlah Test

| Kategori | Existing | Baru | Total |
|----------|:--------:|:----:|:-----:|
| `generate_default_password_hash` | 4 | 3 | **7** |
| `seed_cabang_default` | 4 | 2 | **6** |
| `seed_pengguna_default` | 3 | 2 | **5** |
| `seed_saldo_ppob_default` | 3 | 2 | **5** |
| `seed_saldo_ewallet_default` | 3 | 3 | **6** |
| `seed_system_configs_default` | 3 | 5 | **8** |
| `verify_seed_integrity` | 6 | 3 | **9** |
| `run_seed_all` | 9 | 4 | **13** |
| Konstanta | 1 | 7 | **8** |
| Lainnya (existing misc) | 9 | 0 | **9** |
| **TOTAL** | **45** | **31** | **76** |

### Distribusi Skenario Baru:

| Tipe Skenario | Jumlah |
|---------------|:------:|
| Positif (Happy Path) | 6 |
| Negatif (Unhappy Path) | 5 |
| Edge Case / Boundary | 9 |
| Validasi Input | 11 |
| **Total Baru** | **31** |

---

## 10. Catatan Tambahan dan Peringatan

### 10.1. Peringatan Anti-Halusinasi

- **JANGAN** mengarang nama fungsi yang tidak ada di `db/seed_data.py`. Hanya ada 8 fungsi publik yang tercantum di Bab 3.1.
- **JANGAN** mengarang nama konstanta yang tidak ada. Hanya ada 7 konstanta yang tercantum di Bab 3.1.
- **JANGAN** mengarang kode error baru. Hanya ada 2 kode error: `ERR-VAL-050` dan `ERR-DB-SEED-001`.
- **JANGAN** mengubah signature fungsi test yang sudah ada.
- **JANGAN** menambahkan pytest fixtures atau conftest.py — gunakan pola inline mock per fungsi sesuai pola existing.

### 10.2. Handling Error pada mysql.connector.Error

Gunakan helper `_make_mysql_error()` yang sudah ada:
```python
def _make_mysql_error(errno: int, msg: str) -> mysql.connector.Error:
    err = mysql.connector.Error()
    err.errno = errno
    err.msg = msg
    return err
```

### 10.3. Konvensi Assertion

Gunakan pola assertion yang konsisten:
```python
# Verifikasi Result Pattern
assert res.is_success is True    # Bukan == True
assert res.is_success is False   # Bukan == False
assert res.error_msg is None     # Bukan == None
assert "ERR-DB-SEED-001" in res.error_msg  # Substring check
```

### 10.4. Multi-Cabang Ready (M.9)

Semua seed data default terikat `cabang_id = 1`. Verifikasi ini di test konstanta untuk memastikan arsitektur multi-cabang siap:
```python
assert DEFAULT_CABANG_DATA[0] == 1
assert DEFAULT_PENGGUNA_DATA[5] == 1
```

---

## 11. Acceptance Criteria (Kriteria Penerimaan)

Issue ini dianggap **SELESAI** jika dan hanya jika:

- [ ] File `tests/test_unit_seed_data.py` berisi total **76 fungsi test** (45 existing + 31 baru).
- [ ] Seluruh **76 fungsi test PASS** tanpa error.
- [ ] Coverage modul `db/seed_data.py` **≥ 90%**.
- [ ] **Tidak ada** test existing yang menjadi FAIL akibat penambahan test baru.
- [ ] **Tidak ada** koneksi fisik database di seluruh test (full mock).
- [ ] **Tidak ada** kode dengan komentar `# TODO`, `# FIXME`, atau fungsi kosong.
- [ ] Seluruh fungsi test memiliki docstring dan type hint `-> None`.
- [ ] Format kode mematuhi PEP 8, max 120 karakter per baris.
