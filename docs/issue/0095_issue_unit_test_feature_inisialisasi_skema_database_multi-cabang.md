---
judul      : Unit-Test Feature Inisialisasi Skema Database Multi-Cabang
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
prioritas  : 🟠 HIGH (Jaminan Kualitas — Validasi Fondasi Data Arsitektural)
status     : Open
assignee   : Claude Sonnet 4.6 (Thinking) — STK-004 (Deep Coding & Refactoring)
reviewer   : Gemini 3 Flash — STK-011 (Automated Reviewer & Debugger)
approver   : Junior Programmer — STK-000 (Owner & Release Manager)
tanggal    : 2026-06-04
estimasi   : 2-3 jam kerja fokus
branch     : `test/unit-test-init-database-schema`
---

# Issue — Unit-Test Feature Inisialisasi Skema Database Multi-Cabang

## 1. Ringkasan Issue

Issue ini bertujuan untuk mengimplementasikan **unit test komprehensif** terhadap seluruh fungsi yang ada di modul `db/db_connector.py` dan `db/schema_initializer.py` — yaitu modul fondasi infrastruktur database yang dibangun di Issue #0094. Unit test ini **WAJIB terisolasi penuh** dari koneksi database MySQL fisik menggunakan teknik **mocking** (`unittest.mock`), sehingga dapat dijalankan di environment manapun tanpa dependency server database.

Issue #0094 sebelumnya telah membuat file `tests/test_db_connection.py` yang berisi **integration test** (memerlukan koneksi database nyata). Issue ini **BERBEDA** — kita membuat **unit test murni** yang:
- Tidak memerlukan koneksi MySQL fisik
- Menggunakan `unittest.mock.patch` dan `MagicMock` untuk mengisolasi dependency eksternal
- Dapat dijalankan kapan saja, di mana saja, dengan hasil 100% deterministik
- Mencakup skenario positif, negatif/edge cases, dan validasi input secara lengkap

> ⚠️ **PERINGATAN ISOLASI**: Issue ini **HANYA** mengerjakan unit test. **JANGAN** memodifikasi kode sumber di `db/db_connector.py`, `db/schema_initializer.py`, `main.py`, atau file apapun di luar folder `tests/`. Pastikan pengerjaan issue ini **tidak menyenggol atau merusak** file, folder, atau feature lain yang sudah dibuat di issue sebelumnya (#0093 Scaffolding dan #0094 Feature Database).

> ⚠️ **PERINGATAN KUALITAS**: Seluruh fungsi test **WAJIB** selesai dan berfungsi penuh. **TIDAK BOLEH** ada fungsi test yang berisi `pass`, `TODO`, atau stub menggantung. Setiap skenario harus memiliki assertion yang jelas dan bermakna.

---

## 2. Persona AI yang Ditugaskan

**Persona**: `Senior Python Test Engineer & Database Mocking Specialist`

**Deskripsi Persona**: Kamu adalah seorang insinyur pengujian Python senior yang menguasai framework `pytest`, teknik mocking menggunakan `unittest.mock` (patch, MagicMock, PropertyMock, side_effect), isolasi unit test dari dependency I/O eksternal (database, filesystem), dan paradigma Functional Programming (FP) Python. Kamu bertanggung jawab untuk memvalidasi setiap cabang logika, setiap penanganan error, dan setiap edge case dari modul infrastruktur database AbuCom secara deterministik dan terisolasi.

**Sifat yang WAJIB dimiliki**:
- **Sangat Teliti terhadap Coverage**: Tidak melewatkan satupun fungsi, satupun cabang `if/else`, satupun handler `except`, atau satupun edge case dari modul target.
- **Patuh Standar FP & Coding Standard AbuCom**: Menggunakan NamedTuple, pure assertions, konvensi penamaan `test_<behavior_spesifik>()`, dan **tidak menggunakan class** di file test (kecuali jika diperlukan untuk grouping `pytest`).
- **Master Mocking**: Menggunakan `unittest.mock.patch` pada level yang tepat (`db.db_connector.mysql.connector`, bukan `mysql.connector` langsung) untuk memastikan isolasi yang benar.
- **Clean State Obsessive**: Setiap test function membersihkan/reset state modul-level (seperti `_connection_pool`) sebelum dan sesudah dijalankan menggunakan fixture `autouse`.
- **Tidak Tergesa-gesa**: Mengerjakan secara bertahap, memverifikasi setiap skenario sebelum lanjut ke skenario berikutnya.
- **Tidak Merusak**: Memastikan file-file yang sudah ada tidak termodifikasi secara tidak sengaja.

---

## 3. Dokumen Referensi Utama

Berikut adalah daftar dokumen SDLC dan file kode sumber yang menjadi **dasar utama (Source of Truth)** untuk pengerjaan issue ini. Baca dan ekstrak seluruh detail yang relevan dari setiap dokumen sebelum memulai implementasi.

| Prioritas | Dokumen Referensi | Path File | Bagian yang Relevan |
|:---------:|:------------------|:----------|:--------------------|
| **PRIMER** | Kode Sumber `db_connector.py` | `db/db_connector.py` | **SELURUH ISI FILE** — 4 fungsi (`create_connection_pool`, `get_db_connection`, `close_connection_pool`, `get_root_connection`), Result pattern, konstanta `MAX_RETRIES=3`, `RETRY_ERROR_CODES=(2006, 2013)`, variabel modul `_connection_pool` |
| **PRIMER** | Kode Sumber `schema_initializer.py` | `db/schema_initializer.py` | **SELURUH ISI FILE** — 5 fungsi (`split_sql_statements`, `read_sql_file`, `execute_schema_init`, `verify_schema_integrity`, `run_full_initialization`), konstanta `EXPECTED_TABLE_COUNT=28`, `EXPECTED_SEED_COUNTS` |
| **PRIMER** | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` | Bab 14 (Standar Pengujian: pytest, coverage ≥90%, konvensi penamaan `test_<behavior>()`, unit test deterministik terisolasi, mock NamedTuples), Bab 3 (Konvensi Penamaan snake_case), Bab 6.4 (Header Module Docstring), Bab 16 (10 Larangan Mutlak) |
| **PRIMER** | Test Plan v1.2 | `docs/sdlc/05_testing/01_test_plan.md` | Bab 3.1.1 (Unit Testing: pure functions, mock data, target coverage ≥90%), Bab 3.4 (Entry/Exit Criteria), Bab 10.3 (Database Testing `abucom_test_db`), Bab 11.3.1 (Framework pytest) |
| **SEKUNDER** | Issue #0094 (Feature Database) | `docs/issue/0094_issue_feature_inisialisasi_skema_database_multi-cabang.md` | Bab 4 (Rangkuman Detail Data: 28 tabel, seed counts, connection pool specs), Bab 7 (Instruksi Khusus: Result pattern, error handling, multi-statement SQL) |
| **SEKUNDER** | Integration Test Existing | `tests/test_db_connection.py` | Referensi **yang sudah ada** — jangan duplikasi, tapi pastikan unit test baru menutupi yang belum tercakup oleh integration test |
| **TERSIER** | System Architecture v1.2 | `docs/sdlc/03_design/03_system_architecture.md` | Bab 6.2 (Connection Pooling `abupool`, pool_size=5, retry 3x exponential backoff 2^n detik) |

> **Catatan Referensi**: File `narasi.txt` **TIDAK dibutuhkan** untuk issue unit test ini karena konteks bisnis tidak relevan terhadap pengujian teknis fungsi infrastruktur database.

---

## 4. Rangkuman Detail Data dari Dokumen Referensi

Berikut adalah **ekstraksi lengkap** seluruh detail teknis yang relevan untuk pengerjaan unit test ini:

### 4.1. Modul Target: `db/db_connector.py` (172 baris)

**Fungsi-fungsi yang harus ditest:**

| No | Nama Fungsi | Signature | Return Type | Dependency Eksternal |
|:--:|:------------|:----------|:------------|:---------------------|
| 1 | `create_connection_pool()` | `(host, port, user, password, database, pool_size=5, pool_name='abupool') -> Result` | `Result(is_success, data, error_msg)` | `mysql.connector.pooling.MySQLConnectionPool` |
| 2 | `get_db_connection()` | `(max_retries=3) -> Result` | `Result(is_success, data, error_msg)` | `_connection_pool.get_connection()`, `time.sleep()` |
| 3 | `close_connection_pool()` | `() -> Result` | `Result(is_success, data, error_msg)` | `_connection_pool._remove_connections()` |
| 4 | `get_root_connection()` | `(host, port, user, password) -> Result` | `Result(is_success, data, error_msg)` | `mysql.connector.connect()` |

**Konstanta dan variabel modul:**
- `MAX_RETRIES = 3`
- `RETRY_ERROR_CODES = (2006, 2013)`
- `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])`
- `_connection_pool = None` (variabel modul-level, mutable state)

**Cabang logika yang harus dicakup:**
- `create_connection_pool`: sukses → `mysql.connector.Error` → `Exception` umum
- `get_db_connection`: pool belum init → sukses → retry pada error 2006/2013 → non-retryable error → semua retry habis → Exception umum
- `close_connection_pool`: pool None → pool ada + `_remove_connections` berhasil → Exception saat closing
- `get_root_connection`: sukses → `mysql.connector.Error` → `Exception` umum

### 4.2. Modul Target: `db/schema_initializer.py` (453 baris)

**Fungsi-fungsi yang harus ditest:**

| No | Nama Fungsi | Signature | Return Type | Dependency Eksternal |
|:--:|:------------|:----------|:------------|:---------------------|
| 1 | `split_sql_statements()` | `(sql_content: str) -> list[str]` | `list[str]` | Tidak ada (pure function) |
| 2 | `read_sql_file()` | `(file_path: str) -> Result` | `Result(is_success, data, error_msg)` | `pathlib.Path`, file I/O |
| 3 | `execute_schema_init()` | `(root_connection, sql_statements) -> Result` | `Result(is_success, data, error_msg)` | `cursor.execute()`, `cursor.with_rows`, `cursor.fetchall()`, `cursor.nextset()` |
| 4 | `verify_schema_integrity()` | `(db_connection) -> Result` | `Result(is_success, data, error_msg)` | `cursor.execute('SHOW TABLES')`, `cursor.execute('SHOW INDEX')`, `cursor.execute('SELECT COUNT')` |
| 5 | `run_full_initialization()` | `(root_host, root_port, root_user, root_password, schema_file_path, app_db_name='abucom_db') -> Result` | `Result(is_success, data, error_msg)` | `mysql.connector.connect()`, `read_sql_file()`, `execute_schema_init()`, `bcrypt.gensalt()`, `bcrypt.hashpw()`, `verify_schema_integrity()` |

**Konstanta:**
- `EXPECTED_TABLE_COUNT = 28`
- `EXPECTED_SEED_COUNTS = {'cabang': 1, 'pengguna': 1, 'saldo_ppob': 2, 'saldo_ewallet': 6, 'system_configs': 13}`

### 4.3. Result Pattern (Konsisten di kedua modul)

```python
Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])

# Sukses: Result(True, <data>, None)
# Gagal:  Result(False, None, 'ERR-XXX-YYY: Pesan error')
```

### 4.4. Error Codes yang Digunakan

| Error Code | Konteks | Modul |
|:-----------|:--------|:------|
| `ERR-DB-001` | Gagal koneksi, gagal pool, gagal retry, gagal verifikasi | `db_connector.py`, `schema_initializer.py` |
| `ERR-FILE-003` | File SQL tidak ditemukan atau gagal dibaca | `schema_initializer.py` |
| `ERR-VAL-050` | Gagal generate bcrypt hash | `schema_initializer.py` |

### 4.5. Standar Testing dari Dokumen SDLC

Dari Coding Standard v1.2 Bab 14:
- **Framework**: `pytest==8.2.0` (sudah ada di `requirements.txt`)
- **Target Coverage**: ≥ 90% baris logika bisnis inti
- **Penamaan File Test**: `test_<modul_target>.py` di folder `tests/`
- **Penamaan Fungsi Test**: `test_<behavior_spesifik>()`
- **Isolasi**: Unit test **DILARANG** melakukan koneksi fisik database MySQL lokal. Uji data disuplai melalui mock NamedTuples
- **Deterministik**: Hasil test harus sama di setiap eksekusi, tidak tergantung environment

---

## 5. Batasan, Cakupan, dan Alur Pengerjaan

### 5.1. Cakupan Issue (Scope — Yang HARUS Dikerjakan)

- [ ] Membuat file baru `tests/test_unit_db_connector.py` — unit test terisolasi untuk seluruh fungsi di `db/db_connector.py`
- [ ] Membuat file baru `tests/test_unit_schema_initializer.py` — unit test terisolasi untuk seluruh fungsi di `db/schema_initializer.py`
- [ ] Memastikan seluruh skenario test berjalan PASSED tanpa koneksi database MySQL fisik
- [ ] Memastikan seluruh test dari issue sebelumnya (#0093 dan #0094) masih PASSED (tidak ada regresi)
- [ ] Mencapai coverage ≥ 90% pada kedua modul target

### 5.2. Di Luar Cakupan (Out-of-Scope — Yang TIDAK BOLEH Dikerjakan)

> ⚠️ **PERINGATAN**: Jangan melampaui batasan berikut. Fokus hanya pada unit test.

- ❌ Modifikasi file `db/db_connector.py` (kode sumber tidak boleh diubah)
- ❌ Modifikasi file `db/schema_initializer.py` (kode sumber tidak boleh diubah)
- ❌ Modifikasi file `tests/test_db_connection.py` (integration test yang sudah ada)
- ❌ Modifikasi file apapun di folder `docs/`, `cli/`, `logic/`, `middleware/`, `utils/`, `config/`, atau `exports/`
- ❌ Modifikasi `main.py`, `schema.sql`, `.env`, `.env.example`, `requirements.txt`
- ❌ Implementasi test untuk logika bisnis modul M.1 — M.10 (itu tugas issue terpisah)
- ❌ Setup database MySQL untuk testing (unit test TIDAK memerlukan database)

### 5.3. Prinsip Isolasi Test (Mocking Strategy)

> ⚠️ **KRITIS**: Unit test ini HARUS terisolasi penuh. Berikut strategi mocking yang WAJIB digunakan:

**Untuk `db/db_connector.py`:**
- Mock `mysql.connector.pooling.MySQLConnectionPool` → gunakan `@patch('db.db_connector.pooling.MySQLConnectionPool')`
- Mock `mysql.connector.connect` → gunakan `@patch('db.db_connector.mysql.connector.connect')`
- Mock `time.sleep` → gunakan `@patch('db.db_connector.time.sleep')` (agar test tidak menunggu retry delay)
- Reset `_connection_pool` → set `db.db_connector._connection_pool = None` di fixture `setUp`/`tearDown`

**Untuk `db/schema_initializer.py`:**
- Mock `mysql.connector.connect` → gunakan `@patch('db.schema_initializer.mysql.connector.connect')`
- Mock `bcrypt.gensalt` dan `bcrypt.hashpw` → gunakan `@patch('db.schema_initializer.bcrypt.hashpw')` dan `@patch('db.schema_initializer.bcrypt.gensalt')`
- Mock `read_sql_file` saat testing `run_full_initialization` → gunakan `@patch('db.schema_initializer.read_sql_file')`
- Mock `execute_schema_init` saat testing `run_full_initialization` → gunakan `@patch('db.schema_initializer.execute_schema_init')`
- Mock `verify_schema_integrity` saat testing `run_full_initialization` → gunakan `@patch('db.schema_initializer.verify_schema_integrity')`
- Mock file I/O → gunakan `@patch('builtins.open')` atau `@patch('db.schema_initializer.Path')` atau `tmp_path` fixture pytest

### 5.4. Prinsip Clean State (Reset Data Sebelum Setiap Test)

> ⚠️ **WAJIB**: Setiap skenario test HARUS melakukan pembersihan/reset data terlebih dahulu agar hasilnya konsisten.

```python
import db.db_connector as db_mod

@pytest.fixture(autouse=True)
def reset_connection_pool():
    """Reset variabel modul _connection_pool sebelum dan sesudah setiap test."""
    db_mod._connection_pool = None
    yield
    db_mod._connection_pool = None
```

Untuk `schema_initializer.py`, karena tidak ada state modul yang mutable, reset cukup dilakukan pada mock objects di dalam setiap test function.

### 5.5. Alur Pengerjaan (Workflow)

```
1. Baca & Pahami Referensi (Kode Sumber + SDLC)
         │
         v
2. Buat Branch: test/unit-test-init-database-schema
         │
         v
3. Buat file tests/test_unit_db_connector.py
   (unit test seluruh fungsi db_connector.py)
         │
         v
4. Buat file tests/test_unit_schema_initializer.py
   (unit test seluruh fungsi schema_initializer.py)
         │
         v
5. Jalankan seluruh test: pytest tests/ -v
   (pastikan SEMUA test PASSED termasuk test lama)
         │
         v
6. Jalankan coverage: coverage run -m pytest tests/ && coverage report
   (pastikan coverage ≥ 90% pada modul target)
         │
         v
7. Verifikasi Kelengkapan Akhir
         │
         v
8. Commit Atomis + Push
         │
         v
9. Quality Gate Review oleh Gemini 3 Flash (STK-011)
```

---

## 6. Instruksi Implementasi Detail (Low-Level Checklist)

### ⚙️ TAHAP 0 — Pembacaan dan Pemahaman Referensi

> **Tujuan**: Pastikan kamu memahami seluruh kode sumber yang akan ditest dan seluruh standar testing sebelum menulis satu baris kode pun.

- [ ] Baca file `db/db_connector.py` secara **keseluruhan (172 baris)**. Fokus pada:
  - [ ] Baris 1-27 — Header, import, konstanta (`MAX_RETRIES`, `RETRY_ERROR_CODES`), Result pattern, dan `_connection_pool`.
  - [ ] Baris 29-72 — Fungsi `create_connection_pool()`: pahami parameter, alur sukses (return pool di `Result.data`), penanganan `mysql.connector.Error`, dan `Exception` umum. Perhatikan bahwa fungsi ini mengubah `global _connection_pool`.
  - [ ] Baris 75-112 — Fungsi `get_db_connection()`: pahami pengecekan `_connection_pool is None`, loop retry `for attempt in range(1, max_retries + 1)`, penanganan error code 2006/2013 dengan `time.sleep(2**attempt)`, non-retryable error, dan fallback return setelah loop selesai.
  - [ ] Baris 115-132 — Fungsi `close_connection_pool()`: pahami pengecekan `_connection_pool is None`, pemanggilan `_remove_connections()` dengan `hasattr` check, dan reset `_connection_pool = None`.
  - [ ] Baris 135-172 — Fungsi `get_root_connection()`: pahami koneksi langsung non-pool, penanganan `mysql.connector.Error`, dan `Exception` umum.
- [ ] Baca file `db/schema_initializer.py` secara **keseluruhan (453 baris)**. Fokus pada:
  - [ ] Baris 1-35 — Header, import, konstanta `EXPECTED_TABLE_COUNT` dan `EXPECTED_SEED_COUNTS`.
  - [ ] Baris 38-117 — Fungsi `split_sql_statements()`: **pure function**, pahami state machine untuk parsing SQL (komentar baris `--`, komentar blok `/* */`, string literal `'...'` dan `"..."`, pemisahan berdasarkan `;`).
  - [ ] Baris 120-142 — Fungsi `read_sql_file()`: pahami penggunaan `pathlib.Path`, pengecekan `path.exists()`, pembacaan dengan `encoding='utf-8'`, pemanggilan `split_sql_statements()`, dan penanganan `FileNotFoundError` serta `Exception` umum.
  - [ ] Baris 145-192 — Fungsi `execute_schema_init()`: pahami iterasi statement-per-statement, `cursor.execute()`, penanganan `cursor.with_rows`, `cursor.nextset()`, akumulasi `success_count`/`failed_count`, dan return statistik.
  - [ ] Baris 195-273 — Fungsi `verify_schema_integrity()`: pahami 3 tahap verifikasi (jumlah tabel, composite index, seed data counts), penggunaan `SHOW TABLES`, `SHOW INDEX FROM <table>`, `SELECT COUNT(*) FROM <table>`, dan akumulasi error.
  - [ ] Baris 276-379 — Fungsi `run_full_initialization()`: pahami 6 tahap eksekusi (koneksi → baca SQL → eksekusi DDL → bcrypt hash → update password → verifikasi), penanganan kegagalan di setiap tahap, dan penutupan koneksi.
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` Bab 14. Fokus pada:
  - [ ] Bab 14.1 — Framework: `pytest` (bukan `unittest` class-based)
  - [ ] Bab 14.3 — Konvensi Penamaan: file `test_<modul>.py`, fungsi `test_<behavior>()`
  - [ ] Bab 14.4 — Unit Testing Pure Functions: terisolasi penuh, **DILARANG** koneksi database fisik, mock NamedTuples
  - [ ] Bab 14.5 — Integration Testing Database: gunakan `abucom_test_db`, rollback setelah test
- [ ] Baca file `tests/test_db_connection.py` untuk memahami apa yang sudah dicakup oleh integration test dan tidak perlu diduplikasi secara identik di unit test.

> 🚩 **PENTING**: Jika ada perbedaan antara kode sumber dan dokumen SDLC, **prioritaskan kode sumber** karena itu adalah implementasi aktual yang harus ditest.

---

### ⚙️ TAHAP 1 — Pembuatan Branch Git

- [ ] Pastikan kamu berada di branch yang sudah terbaru:
  ```bash
  git checkout develop
  git pull origin develop
  ```
- [ ] Buat branch baru sesuai konvensi Git Workflow:
  ```bash
  git checkout -b test/unit-test-init-database-schema
  ```

---

### ⚙️ TAHAP 2 — Pembuatan File `tests/test_unit_db_connector.py`

> **Tujuan**: Membuat unit test terisolasi (dengan mocking) untuk seluruh fungsi di `db/db_connector.py`.

- [ ] Buat file baru `tests/test_unit_db_connector.py`.
- [ ] Tulis **header module docstring** sesuai Coding Standard Bab 6.4:
  ```python
  """
  Nama Modul: test_unit_db_connector.py
  Deskripsi: Unit test terisolasi (mocked) untuk modul db/db_connector.py.
             Menguji seluruh fungsi connection pool factory, retry mechanism,
             dan koneksi root tanpa memerlukan koneksi database MySQL fisik.
  Author: [Nama AI / Programmer yang mengerjakan]
  Tanggal: 2026-06-04
  """
  ```
- [ ] Tulis blok import yang diperlukan:
  ```python
  import pytest
  from unittest.mock import patch, MagicMock, PropertyMock
  from collections import namedtuple

  import db.db_connector as db_mod
  from db.db_connector import (
      create_connection_pool,
      get_db_connection,
      close_connection_pool,
      get_root_connection,
      Result,
      MAX_RETRIES,
      RETRY_ERROR_CODES,
  )
  import mysql.connector
  ```
- [ ] Tulis fixture `autouse` untuk clean state:
  ```python
  @pytest.fixture(autouse=True)
  def reset_connection_pool():
      """Reset variabel modul _connection_pool sebelum dan sesudah setiap test.

      Memastikan setiap test dimulai dari clean state tanpa sisa pool
      dari test sebelumnya.
      """
      db_mod._connection_pool = None
      yield
      db_mod._connection_pool = None
  ```

#### 6.2.1. Skenario Test untuk `create_connection_pool()`

- [ ] **Test Positif — Pool berhasil dibuat dengan parameter valid**:
  ```
  Nama fungsi: test_create_connection_pool_sukses_dengan_parameter_valid()
  Setup: Mock MySQLConnectionPool agar return MagicMock tanpa error.
  Action: Panggil create_connection_pool(host='localhost', port=3306, user='app', password='pass', database='db').
  Assert:
    - result.is_success is True
    - result.data is not None (mock pool object)
    - result.error_msg is None
    - db_mod._connection_pool is not None (state modul ter-update)
    - MySQLConnectionPool dipanggil dengan parameter yang benar (pool_name='abupool', pool_size=5, pool_reset_session=True)
  ```

- [ ] **Test Positif — Pool berhasil dibuat dengan pool_size kustom**:
  ```
  Nama fungsi: test_create_connection_pool_sukses_dengan_pool_size_kustom()
  Setup: Mock MySQLConnectionPool agar return MagicMock tanpa error.
  Action: Panggil create_connection_pool(..., pool_size=10, pool_name='custom_pool').
  Assert:
    - result.is_success is True
    - MySQLConnectionPool dipanggil dengan pool_size=10 dan pool_name='custom_pool'
  ```

- [ ] **Test Negatif — Pool gagal karena mysql.connector.Error**:
  ```
  Nama fungsi: test_create_connection_pool_gagal_mysql_error()
  Setup: Mock MySQLConnectionPool agar raise mysql.connector.Error(errno=2003, msg='Connection refused').
  Action: Panggil create_connection_pool(host='invalid', port=9999, ...).
  Assert:
    - result.is_success is False
    - result.data is None
    - 'ERR-DB-001' in result.error_msg
    - '2003' in result.error_msg atau 'Connection refused' in result.error_msg
    - db_mod._connection_pool is None (state modul tidak ter-update)
  ```

- [ ] **Test Negatif — Pool gagal karena Exception umum**:
  ```
  Nama fungsi: test_create_connection_pool_gagal_exception_umum()
  Setup: Mock MySQLConnectionPool agar raise Exception('Unexpected error').
  Action: Panggil create_connection_pool(...).
  Assert:
    - result.is_success is False
    - result.data is None
    - 'ERR-DB-001' in result.error_msg
    - 'Unexpected error' in result.error_msg
  ```

#### 6.2.2. Skenario Test untuk `get_db_connection()`

- [ ] **Test Negatif — Pool belum diinisialisasi**:
  ```
  Nama fungsi: test_get_db_connection_gagal_pool_belum_init()
  Setup: Pastikan db_mod._connection_pool = None (dari fixture).
  Action: Panggil get_db_connection().
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
    - 'belum diinisialisasi' in result.error_msg
  ```

- [ ] **Test Positif — Koneksi berhasil diambil dari pool**:
  ```
  Nama fungsi: test_get_db_connection_sukses_dari_pool()
  Setup:
    - Buat mock_pool = MagicMock()
    - mock_pool.get_connection.return_value = MagicMock(spec=mysql.connector.MySQLConnection)
    - Set db_mod._connection_pool = mock_pool
  Action: Panggil get_db_connection().
  Assert:
    - result.is_success is True
    - result.data is not None
    - result.error_msg is None
    - mock_pool.get_connection.assert_called_once()
  ```

- [ ] **Test Positif — Retry berhasil setelah error retryable (error 2006)**:
  ```
  Nama fungsi: test_get_db_connection_retry_sukses_setelah_error_2006()
  Setup:
    - Buat mock_pool = MagicMock()
    - Buat mock_error = mysql.connector.Error(errno=2006, msg='Server has gone away')
    - mock_conn = MagicMock()
    - mock_pool.get_connection.side_effect = [mock_error, mock_conn]
    - Set db_mod._connection_pool = mock_pool
    - Mock time.sleep agar tidak menunggu
  Action: Panggil get_db_connection().
  Assert:
    - result.is_success is True
    - result.data is mock_conn
    - mock_pool.get_connection.call_count == 2
    - time.sleep dipanggil dengan 2**1 = 2 detik
  ```

- [ ] **Test Positif — Retry berhasil setelah error retryable (error 2013)**:
  ```
  Nama fungsi: test_get_db_connection_retry_sukses_setelah_error_2013()
  Setup:
    - mock_pool.get_connection.side_effect = [mysql.connector.Error(errno=2013, msg='Lost connection'), MagicMock()]
    - Set db_mod._connection_pool = mock_pool
    - Mock time.sleep
  Action: Panggil get_db_connection().
  Assert:
    - result.is_success is True
    - mock_pool.get_connection.call_count == 2
    - time.sleep dipanggil dengan 2 detik
  ```

- [ ] **Test Negatif — Semua retry habis (3 kali error retryable)**:
  ```
  Nama fungsi: test_get_db_connection_gagal_setelah_semua_retry_habis()
  Setup:
    - mock_pool.get_connection.side_effect = mysql.connector.Error(errno=2006, msg='Server has gone away')
    - Set db_mod._connection_pool = mock_pool
    - Mock time.sleep
  Action: Panggil get_db_connection().
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
    - mock_pool.get_connection.call_count == MAX_RETRIES (3)
    - time.sleep dipanggil 2 kali (attempt 1 dan 2, tidak di attempt 3 karena langsung return)
  ```

- [ ] **Test Negatif — Error non-retryable langsung gagal (bukan 2006/2013)**:
  ```
  Nama fungsi: test_get_db_connection_gagal_error_non_retryable()
  Setup:
    - mock_pool.get_connection.side_effect = mysql.connector.Error(errno=1045, msg='Access denied')
    - Set db_mod._connection_pool = mock_pool
  Action: Panggil get_db_connection().
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
    - '1045' in result.error_msg atau 'Access denied' in result.error_msg
    - mock_pool.get_connection.call_count == 1 (tidak ada retry)
  ```

- [ ] **Test Negatif — Exception umum saat get_connection**:
  ```
  Nama fungsi: test_get_db_connection_gagal_exception_umum()
  Setup:
    - mock_pool.get_connection.side_effect = Exception('Pool exhausted')
    - Set db_mod._connection_pool = mock_pool
  Action: Panggil get_db_connection().
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
    - 'Pool exhausted' in result.error_msg
  ```

- [ ] **Test Edge Case — Retry dengan max_retries kustom (misal 1)**:
  ```
  Nama fungsi: test_get_db_connection_retry_dengan_max_retries_kustom()
  Setup:
    - mock_pool.get_connection.side_effect = mysql.connector.Error(errno=2006, msg='Gone')
    - Set db_mod._connection_pool = mock_pool
    - Mock time.sleep
  Action: Panggil get_db_connection(max_retries=1).
  Assert:
    - result.is_success is False
    - mock_pool.get_connection.call_count == 1
  ```

- [ ] **Test Validasi — Exponential backoff timing yang benar**:
  ```
  Nama fungsi: test_get_db_connection_exponential_backoff_timing()
  Setup:
    - mock_pool.get_connection.side_effect = [
        mysql.connector.Error(errno=2006, msg='Gone'),
        mysql.connector.Error(errno=2006, msg='Gone'),
        MagicMock()
      ]
    - Set db_mod._connection_pool = mock_pool
    - Mock time.sleep
  Action: Panggil get_db_connection().
  Assert:
    - result.is_success is True
    - time.sleep dipanggil 2 kali
    - Panggilan pertama time.sleep(2) → 2^1
    - Panggilan kedua time.sleep(4) → 2^2
  ```

#### 6.2.3. Skenario Test untuk `close_connection_pool()`

- [ ] **Test Positif — Pool None, close langsung sukses**:
  ```
  Nama fungsi: test_close_connection_pool_sukses_saat_pool_none()
  Setup: Pastikan db_mod._connection_pool = None.
  Action: Panggil close_connection_pool().
  Assert:
    - result.is_success is True
    - result.data is None
    - result.error_msg is None
  ```

- [ ] **Test Positif — Pool ada, close berhasil**:
  ```
  Nama fungsi: test_close_connection_pool_sukses_saat_pool_ada()
  Setup:
    - mock_pool = MagicMock()
    - mock_pool._remove_connections = MagicMock()
    - Set db_mod._connection_pool = mock_pool
  Action: Panggil close_connection_pool().
  Assert:
    - result.is_success is True
    - mock_pool._remove_connections.assert_called_once()
    - db_mod._connection_pool is None (state modul ter-reset)
  ```

- [ ] **Test Edge Case — Pool ada tapi tanpa _remove_connections (hasattr=False)**:
  ```
  Nama fungsi: test_close_connection_pool_sukses_tanpa_remove_connections()
  Setup:
    - mock_pool = MagicMock(spec=[])  # spec kosong, tidak punya _remove_connections
    - Set db_mod._connection_pool = mock_pool
  Action: Panggil close_connection_pool().
  Assert:
    - result.is_success is True
    - db_mod._connection_pool is None
  ```

- [ ] **Test Negatif — Exception saat closing pool**:
  ```
  Nama fungsi: test_close_connection_pool_gagal_exception()
  Setup:
    - mock_pool = MagicMock()
    - mock_pool._remove_connections.side_effect = Exception('Cannot close')
    - Set db_mod._connection_pool = mock_pool
  Action: Panggil close_connection_pool().
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
    - 'Cannot close' in result.error_msg
  ```

#### 6.2.4. Skenario Test untuk `get_root_connection()`

- [ ] **Test Positif — Koneksi root berhasil**:
  ```
  Nama fungsi: test_get_root_connection_sukses()
  Setup: Mock mysql.connector.connect agar return MagicMock().
  Action: Panggil get_root_connection(host='localhost', port=3306, user='root', password='pass').
  Assert:
    - result.is_success is True
    - result.data is not None
    - result.error_msg is None
    - mysql.connector.connect dipanggil dengan parameter yang benar
  ```

- [ ] **Test Negatif — Koneksi root gagal karena mysql.connector.Error**:
  ```
  Nama fungsi: test_get_root_connection_gagal_mysql_error()
  Setup: Mock mysql.connector.connect agar raise mysql.connector.Error(errno=2003, msg='Refused').
  Action: Panggil get_root_connection(host='invalid', port=9999, user='root', password='pass').
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
    - 'Koneksi administratif gagal' in result.error_msg
  ```

- [ ] **Test Negatif — Koneksi root gagal karena Exception umum**:
  ```
  Nama fungsi: test_get_root_connection_gagal_exception_umum()
  Setup: Mock mysql.connector.connect agar raise Exception('Network unreachable').
  Action: Panggil get_root_connection(host='10.0.0.1', port=3306, user='root', password='pass').
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
    - 'Network unreachable' in result.error_msg
  ```

#### 6.2.5. Skenario Validasi Konstanta dan Struktur

- [ ] **Test Validasi — Konstanta MAX_RETRIES**:
  ```
  Nama fungsi: test_konstanta_max_retries()
  Assert: MAX_RETRIES == 3
  ```

- [ ] **Test Validasi — Konstanta RETRY_ERROR_CODES**:
  ```
  Nama fungsi: test_konstanta_retry_error_codes()
  Assert:
    - RETRY_ERROR_CODES == (2006, 2013)
    - 2006 in RETRY_ERROR_CODES
    - 2013 in RETRY_ERROR_CODES
  ```

- [ ] **Test Validasi — Result NamedTuple fields**:
  ```
  Nama fungsi: test_result_namedtuple_fields()
  Assert:
    - Result._fields == ('is_success', 'data', 'error_msg')
    - Result(True, 'data', None).is_success is True
    - Result(False, None, 'error').error_msg == 'error'
  ```

- [ ] **COMMIT ATOMIS TAHAP 2**:
  ```bash
  git add tests/test_unit_db_connector.py
  git commit -m "test(db): tambah unit test terisolasi untuk db_connector.py"
  ```

---

### ⚙️ TAHAP 3 — Pembuatan File `tests/test_unit_schema_initializer.py`

> **Tujuan**: Membuat unit test terisolasi (dengan mocking) untuk seluruh fungsi di `db/schema_initializer.py`.

- [ ] Buat file baru `tests/test_unit_schema_initializer.py`.
- [ ] Tulis **header module docstring** sesuai Coding Standard Bab 6.4:
  ```python
  """
  Nama Modul: test_unit_schema_initializer.py
  Deskripsi: Unit test terisolasi (mocked) untuk modul db/schema_initializer.py.
             Menguji seluruh fungsi parsing SQL, eksekusi schema DDL, verifikasi
             integritas, dan full initialization tanpa koneksi database MySQL fisik.
  Author: [Nama AI / Programmer yang mengerjakan]
  Tanggal: 2026-06-04
  """
  ```
- [ ] Tulis blok import yang diperlukan:
  ```python
  import pytest
  from unittest.mock import patch, MagicMock, mock_open
  from collections import namedtuple
  from pathlib import Path

  from db.schema_initializer import (
      split_sql_statements,
      read_sql_file,
      execute_schema_init,
      verify_schema_integrity,
      run_full_initialization,
      Result,
      EXPECTED_TABLE_COUNT,
      EXPECTED_SEED_COUNTS,
  )
  import mysql.connector
  ```

#### 6.3.1. Skenario Test untuk `split_sql_statements()` (Pure Function — Tidak Perlu Mock)

- [ ] **Test Positif — Parsing statement sederhana**:
  ```
  Nama fungsi: test_split_sql_statements_parsing_sederhana()
  Input: "CREATE TABLE a (id INT); INSERT INTO a VALUES (1);"
  Assert:
    - len(result) == 2
    - result[0] == 'CREATE TABLE a (id INT)'
    - result[1] == 'INSERT INTO a VALUES (1)'
  ```

- [ ] **Test Positif — Mengabaikan komentar baris (--)**:
  ```
  Nama fungsi: test_split_sql_statements_abaikan_komentar_baris()
  Input: "-- Ini komentar\nCREATE TABLE a (id INT);"
  Assert:
    - len(result) == 1
    - result[0] == 'CREATE TABLE a (id INT)'
  ```

- [ ] **Test Positif — Mengabaikan komentar baris (#)**:
  ```
  Nama fungsi: test_split_sql_statements_abaikan_komentar_hash()
  Input: "# Ini komentar hash\nCREATE TABLE a (id INT);"
  Assert:
    - len(result) == 1
    - 'CREATE TABLE' in result[0]
  ```

- [ ] **Test Positif — Mengabaikan komentar blok (/* */)**:
  ```
  Nama fungsi: test_split_sql_statements_abaikan_komentar_blok()
  Input: "/* Komentar blok\n multi-baris */\nCREATE TABLE a (id INT);"
  Assert:
    - len(result) == 1
    - 'CREATE TABLE' in result[0]
  ```

- [ ] **Test Positif — Tidak memecah semicolon di dalam string literal**:
  ```
  Nama fungsi: test_split_sql_statements_semicolon_dalam_string_literal()
  Input: "INSERT INTO a (nama) VALUES ('test;value');"
  Assert:
    - len(result) == 1
    - "test;value" in result[0]
  ```

- [ ] **Test Positif — Tidak memecah semicolon di dalam double-quoted string**:
  ```
  Nama fungsi: test_split_sql_statements_semicolon_dalam_double_quote()
  Input: 'INSERT INTO a (nama) VALUES ("test;value");'
  Assert:
    - len(result) == 1
    - 'test;value' in result[0]
  ```

- [ ] **Test Positif — Parsing multi-statement kompleks**:
  ```
  Nama fungsi: test_split_sql_statements_multi_statement_kompleks()
  Input: "SET NAMES utf8mb4;\n-- komentar\nCREATE TABLE a (id INT);\nINSERT INTO a VALUES (1);"
  Assert:
    - len(result) == 3
    - 'SET NAMES' in result[0]
    - 'CREATE TABLE' in result[1]
    - 'INSERT INTO' in result[2]
  ```

- [ ] **Test Edge Case — Input string kosong**:
  ```
  Nama fungsi: test_split_sql_statements_input_kosong()
  Input: ""
  Assert: len(result) == 0
  ```

- [ ] **Test Edge Case — Input hanya komentar**:
  ```
  Nama fungsi: test_split_sql_statements_hanya_komentar()
  Input: "-- komentar saja\n-- baris lagi"
  Assert: len(result) == 0
  ```

- [ ] **Test Edge Case — Statement tanpa trailing semicolon**:
  ```
  Nama fungsi: test_split_sql_statements_tanpa_trailing_semicolon()
  Input: "SELECT 1"
  Assert:
    - len(result) == 1
    - result[0] == 'SELECT 1'
  ```

- [ ] **Test Edge Case — Statement dengan whitespace berlebih**:
  ```
  Nama fungsi: test_split_sql_statements_whitespace_berlebih()
  Input: "  \n  CREATE TABLE a (id INT)  ;  \n  "
  Assert:
    - len(result) == 1
    - result[0].strip() == 'CREATE TABLE a (id INT)'
  ```

#### 6.3.2. Skenario Test untuk `read_sql_file()`

- [ ] **Test Positif — Berhasil membaca file SQL yang ada**:
  ```
  Nama fungsi: test_read_sql_file_sukses_file_valid()
  Setup: Gunakan tmp_path fixture pytest untuk membuat file .sql sementara berisi "CREATE TABLE test (id INT);"
  Action: Panggil read_sql_file(str(tmp_path / 'test.sql')).
  Assert:
    - result.is_success is True
    - len(result.data) >= 1
    - 'CREATE TABLE' in result.data[0]
    - result.error_msg is None
  ```

- [ ] **Test Negatif — File tidak ditemukan (path tidak ada)**:
  ```
  Nama fungsi: test_read_sql_file_gagal_file_tidak_ada()
  Action: Panggil read_sql_file('/path/tidak/ada/schema.sql').
  Assert:
    - result.is_success is False
    - 'ERR-FILE-003' in result.error_msg
    - result.data is None
  ```

- [ ] **Test Negatif — File ada tapi kosong**:
  ```
  Nama fungsi: test_read_sql_file_file_kosong()
  Setup: Buat file .sql kosong di tmp_path.
  Action: Panggil read_sql_file(str(tmp_path / 'empty.sql')).
  Assert:
    - result.is_success is True
    - len(result.data) == 0 (list kosong karena tidak ada statement)
  ```

- [ ] **Test Negatif — Exception saat membaca file (misal permission error)**:
  ```
  Nama fungsi: test_read_sql_file_gagal_exception_baca()
  Setup: Mock builtins.open agar raise PermissionError('Permission denied').
         Mock Path.exists() agar return True.
  Action: Panggil read_sql_file('protected_file.sql').
  Assert:
    - result.is_success is False
    - 'ERR-FILE-003' in result.error_msg
  ```

- [ ] **Test Positif — File SQL dengan encoding UTF-8 dan karakter khusus**:
  ```
  Nama fungsi: test_read_sql_file_utf8_karakter_khusus()
  Setup: Buat file .sql di tmp_path berisi "INSERT INTO cabang (nama) VALUES ('Toko Pusat Bandung — Cabang Utama');"
  Action: Panggil read_sql_file(str(tmp_path / 'utf8.sql')).
  Assert:
    - result.is_success is True
    - 'Bandung' in result.data[0]
  ```

#### 6.3.3. Skenario Test untuk `execute_schema_init()`

- [ ] **Test Positif — Semua statement berhasil dieksekusi**:
  ```
  Nama fungsi: test_execute_schema_init_semua_sukses()
  Setup:
    - mock_conn = MagicMock()
    - mock_cursor = MagicMock()
    - mock_conn.cursor.return_value = mock_cursor
    - mock_cursor.with_rows = False
    - mock_cursor.nextset.side_effect = mysql.connector.Error()
    - statements = ['CREATE TABLE a (id INT)', 'INSERT INTO a VALUES (1)']
  Action: Panggil execute_schema_init(mock_conn, statements).
  Assert:
    - result.is_success is True
    - result.data['success'] == 2
    - result.data['failed'] == 0
    - result.data['errors'] == []
    - result.error_msg is None
    - mock_cursor.execute.call_count == 2
  ```

- [ ] **Test Negatif — Sebagian statement gagal (mysql.connector.Error)**:
  ```
  Nama fungsi: test_execute_schema_init_sebagian_gagal_mysql_error()
  Setup:
    - mock_cursor.execute.side_effect = [None, mysql.connector.Error(errno=1050, msg='Table already exists'), None]
    - mock_cursor.with_rows = False
    - mock_cursor.nextset.side_effect = mysql.connector.Error()
    - statements = ['stmt1', 'stmt2', 'stmt3']
  Action: Panggil execute_schema_init(mock_conn, statements).
  Assert:
    - result.is_success is False
    - result.data['success'] == 2
    - result.data['failed'] == 1
    - len(result.data['errors']) == 1
    - 'Table already exists' in result.data['errors'][0]
  ```

- [ ] **Test Negatif — Statement gagal karena Exception umum**:
  ```
  Nama fungsi: test_execute_schema_init_gagal_exception_umum()
  Setup:
    - mock_cursor.execute.side_effect = Exception('Unexpected')
    - statements = ['bad_stmt']
  Action: Panggil execute_schema_init(mock_conn, statements).
  Assert:
    - result.is_success is False
    - result.data['failed'] == 1
    - len(result.data['errors']) == 1
  ```

- [ ] **Test Edge Case — Daftar statement kosong**:
  ```
  Nama fungsi: test_execute_schema_init_statement_kosong()
  Setup: statements = []
  Action: Panggil execute_schema_init(mock_conn, []).
  Assert:
    - result.is_success is True
    - result.data['success'] == 0
    - result.data['failed'] == 0
  ```

- [ ] **Test Edge Case — Statement berisi string whitespace only**:
  ```
  Nama fungsi: test_execute_schema_init_statement_whitespace()
  Setup: statements = ['   ', '\n\t']
  Action: Panggil execute_schema_init(mock_conn, statements).
  Assert:
    - result.is_success is True
    - result.data['success'] == 0 (statement kosong di-skip)
  ```

- [ ] **Test Positif — Statement dengan cursor.with_rows = True (ada result set)**:
  ```
  Nama fungsi: test_execute_schema_init_statement_dengan_result_set()
  Setup:
    - mock_cursor.with_rows diarahkan agar return True pada panggilan pertama
    - mock_cursor.fetchall.return_value = [('row1',)]
    - mock_cursor.nextset.return_value = False
    - statements = ['SHOW TABLES']
  Action: Panggil execute_schema_init(mock_conn, statements).
  Assert:
    - result.is_success is True
    - result.data['success'] == 1
    - mock_cursor.fetchall.assert_called()
  ```

#### 6.3.4. Skenario Test untuk `verify_schema_integrity()`

- [ ] **Test Positif — Skema valid sempurna (28 tabel, 4 index, seed data benar)**:
  ```
  Nama fungsi: test_verify_schema_integrity_skema_valid_sempurna()
  Setup:
    - mock_conn, mock_cursor = MagicMock(), MagicMock()
    - mock_conn.cursor.return_value = mock_cursor
    - SHOW TABLES: return 28 nama tabel (termasuk 'transaksi', 'absensi', 'antrian_kerja', 'barang', 'cabang', 'pengguna', 'saldo_ppob', 'saldo_ewallet', 'system_configs')
    - SHOW INDEX FROM transaksi: return rows yang mengandung 'idx_transaksi_tanggal_cabang'
    - SHOW INDEX FROM absensi: return rows yang mengandung 'idx_absensi_pengguna_tanggal'
    - SHOW INDEX FROM antrian_kerja: return rows yang mengandung 'idx_antrian_status_cabang'
    - SHOW INDEX FROM barang: return rows yang mengandung 'idx_barang_tipe_cabang'
    - SELECT COUNT(*) FROM cabang: return (1,)
    - SELECT COUNT(*) FROM pengguna: return (1,)
    - SELECT COUNT(*) FROM saldo_ppob: return (2,)
    - SELECT COUNT(*) FROM saldo_ewallet: return (6,)
    - SELECT COUNT(*) FROM system_configs: return (13,)
  Action: Panggil verify_schema_integrity(mock_conn).
  Assert:
    - result.is_success is True
    - result.data['tables'] == 28
    - result.data['indexes'] == 4
    - result.data['seeds']['cabang'] == 1
    - result.data['seeds']['pengguna'] == 1
    - result.data['seeds']['saldo_ppob'] == 2
    - result.data['seeds']['saldo_ewallet'] == 6
    - result.data['seeds']['system_configs'] == 13
  ```

- [ ] **Test Negatif — Jumlah tabel kurang dari 28**:
  ```
  Nama fungsi: test_verify_schema_integrity_tabel_kurang()
  Setup: SHOW TABLES return hanya 20 nama tabel.
  Assert:
    - result.is_success is False
    - result.data['tables'] == 20
    - 'tidak sesuai' in result.error_msg atau 'Diharapkan 28' in result.error_msg
  ```

- [ ] **Test Negatif — Composite index tidak ditemukan**:
  ```
  Nama fungsi: test_verify_schema_integrity_index_hilang()
  Setup: SHOW TABLES return 28 tabel, tapi SHOW INDEX FROM transaksi return rows tanpa 'idx_transaksi_tanggal_cabang'.
  Assert:
    - result.is_success is False
    - result.data['indexes'] < 4
    - 'idx_transaksi_tanggal_cabang' in result.error_msg
  ```

- [ ] **Test Negatif — Jumlah seed data tidak sesuai**:
  ```
  Nama fungsi: test_verify_schema_integrity_seed_data_salah()
  Setup: 28 tabel ada, 4 index ada, tapi SELECT COUNT(*) FROM system_configs return (10,) bukannya (13,).
  Assert:
    - result.is_success is False
    - result.data['seeds']['system_configs'] == 10
    - 'Diharapkan 13' in result.error_msg
  ```

- [ ] **Test Negatif — Tabel untuk verifikasi seed tidak ada**:
  ```
  Nama fungsi: test_verify_schema_integrity_tabel_seed_hilang()
  Setup: SHOW TABLES return 28 tabel tapi TIDAK mengandung 'system_configs'.
  Assert:
    - result.is_success is False
    - result.data['seeds']['system_configs'] == 0
    - 'tidak ditemukan' in result.error_msg
  ```

- [ ] **Test Negatif — mysql.connector.Error saat verifikasi**:
  ```
  Nama fungsi: test_verify_schema_integrity_gagal_mysql_error()
  Setup: mock_cursor.execute.side_effect = mysql.connector.Error(errno=1146, msg='Table not found').
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
  ```

- [ ] **Test Negatif — Exception umum saat verifikasi**:
  ```
  Nama fungsi: test_verify_schema_integrity_gagal_exception_umum()
  Setup: mock_cursor.execute.side_effect = Exception('Unexpected error').
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
  ```

#### 6.3.5. Skenario Test untuk `run_full_initialization()`

- [ ] **Test Positif — Inisialisasi lengkap berhasil (semua tahap sukses)**:
  ```
  Nama fungsi: test_run_full_initialization_sukses_lengkap()
  Setup:
    - Mock mysql.connector.connect → return mock_conn
    - Mock read_sql_file → return Result(True, ['stmt1', 'stmt2'], None)
    - Mock execute_schema_init → return Result(True, {'success': 2, 'failed': 0, 'errors': []}, None)
    - Mock bcrypt.gensalt → return b'$2b$12$salt'
    - Mock bcrypt.hashpw → return b'$2b$12$hashed'
    - mock_cursor.execute tanpa error
    - Mock verify_schema_integrity → return Result(True, {'tables': 28, 'indexes': 4, 'seeds': {...}}, None)
  Action: Panggil run_full_initialization('localhost', 3306, 'root', 'pass', 'schema.sql').
  Assert:
    - result.is_success is True
    - result.data is not None
    - 'init_stats' in result.data
    - 'verify_report' in result.data
    - mock_conn.close.assert_called()
  ```

- [ ] **Test Negatif — Gagal di tahap koneksi**:
  ```
  Nama fungsi: test_run_full_initialization_gagal_koneksi()
  Setup: Mock mysql.connector.connect → raise mysql.connector.Error(errno=2003, msg='Cannot connect').
  Action: Panggil run_full_initialization('invalid', 9999, 'root', 'pass', 'schema.sql').
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
  ```

- [ ] **Test Negatif — Gagal di tahap koneksi dengan Exception umum**:
  ```
  Nama fungsi: test_run_full_initialization_gagal_koneksi_exception()
  Setup: Mock mysql.connector.connect → raise Exception('DNS resolution failed').
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
  ```

- [ ] **Test Negatif — Gagal di tahap baca file SQL**:
  ```
  Nama fungsi: test_run_full_initialization_gagal_baca_sql()
  Setup:
    - Mock mysql.connector.connect → return mock_conn
    - Mock read_sql_file → return Result(False, None, 'ERR-FILE-003: Not found')
  Action: Panggil run_full_initialization('localhost', 3306, 'root', 'pass', '/invalid/path.sql').
  Assert:
    - result.is_success is False
    - 'ERR-FILE-003' in result.error_msg
    - mock_conn.close.assert_called() (koneksi harus ditutup meskipun gagal)
  ```

- [ ] **Test Negatif — Gagal di tahap eksekusi DDL**:
  ```
  Nama fungsi: test_run_full_initialization_gagal_eksekusi_ddl()
  Setup:
    - Mock koneksi sukses
    - Mock read_sql_file sukses
    - Mock execute_schema_init → return Result(False, {'success': 5, 'failed': 3, 'errors': ['err1']}, 'Ada kesalahan')
  Assert:
    - result.is_success is False
    - mock_conn.close.assert_called()
  ```

- [ ] **Test Negatif — Gagal di tahap bcrypt hash generation**:
  ```
  Nama fungsi: test_run_full_initialization_gagal_bcrypt_hash()
  Setup:
    - Mock koneksi, baca SQL, dan eksekusi DDL sukses
    - Mock bcrypt.gensalt → raise Exception('bcrypt error')
  Assert:
    - result.is_success is False
    - 'ERR-VAL-050' in result.error_msg
    - mock_conn.close.assert_called()
  ```

- [ ] **Test Negatif — Gagal di tahap update password (mysql.connector.Error)**:
  ```
  Nama fungsi: test_run_full_initialization_gagal_update_password_mysql_error()
  Setup:
    - Mock koneksi, baca SQL, eksekusi DDL, dan bcrypt sukses
    - mock_cursor.execute pada UPDATE → raise mysql.connector.Error(errno=1045, msg='Access denied')
  Assert:
    - result.is_success is False
    - 'ERR-DB-001' in result.error_msg
    - 'password pemilik' in result.error_msg
  ```

- [ ] **Test Negatif — Gagal di tahap verifikasi**:
  ```
  Nama fungsi: test_run_full_initialization_gagal_verifikasi()
  Setup:
    - Mock semua tahap sebelumnya sukses
    - Mock verify_schema_integrity → return Result(False, {'tables': 20}, 'Tabel kurang')
  Assert:
    - result.is_success is False
    - mock_conn.close.assert_called()
  ```

#### 6.3.6. Skenario Validasi Konstanta

- [ ] **Test Validasi — EXPECTED_TABLE_COUNT**:
  ```
  Nama fungsi: test_konstanta_expected_table_count()
  Assert: EXPECTED_TABLE_COUNT == 28
  ```

- [ ] **Test Validasi — EXPECTED_SEED_COUNTS**:
  ```
  Nama fungsi: test_konstanta_expected_seed_counts()
  Assert:
    - EXPECTED_SEED_COUNTS['cabang'] == 1
    - EXPECTED_SEED_COUNTS['pengguna'] == 1
    - EXPECTED_SEED_COUNTS['saldo_ppob'] == 2
    - EXPECTED_SEED_COUNTS['saldo_ewallet'] == 6
    - EXPECTED_SEED_COUNTS['system_configs'] == 13
    - len(EXPECTED_SEED_COUNTS) == 5
  ```

- [ ] **COMMIT ATOMIS TAHAP 3**:
  ```bash
  git add tests/test_unit_schema_initializer.py
  git commit -m "test(db): tambah unit test terisolasi untuk schema_initializer.py"
  ```

---

### ⚙️ TAHAP 4 — Verifikasi dan Eksekusi Test Suite

> **Tujuan**: Pastikan seluruh test berjalan PASSED dan coverage tercapai.

- [ ] Jalankan `python -m py_compile tests/test_unit_db_connector.py` — pastikan tidak ada error kompilasi.
- [ ] Jalankan `python -m py_compile tests/test_unit_schema_initializer.py` — pastikan tidak ada error kompilasi.
- [ ] Jalankan **seluruh** test suite untuk memastikan tidak ada regresi:
  ```bash
  pytest tests/ -v --tb=short
  ```
  Hasil yang diharapkan:
  - Seluruh test di `tests/test_unit_db_connector.py` → **PASSED**
  - Seluruh test di `tests/test_unit_schema_initializer.py` → **PASSED**
  - Seluruh test di `tests/test_db_connection.py` → **PASSED** atau **SKIPPED** (yang butuh DB)
  - Seluruh test dari scaffolding → **PASSED**
- [ ] Jalankan coverage report khusus untuk modul target:
  ```bash
  coverage run --source=db -m pytest tests/test_unit_db_connector.py tests/test_unit_schema_initializer.py -v
  coverage report -m --include="db/db_connector.py,db/schema_initializer.py"
  ```
  Hasil yang diharapkan:
  - Coverage `db/db_connector.py` ≥ **90%**
  - Coverage `db/schema_initializer.py` ≥ **90%** (bagian `if __name__ == '__main__'` boleh dikecualikan)

---

### ⚙️ TAHAP 5 — Verifikasi Kelengkapan Akhir

> **Tujuan**: Pastikan TIDAK ADA satupun file yang terlewat atau detail yang kurang.

- [ ] Verifikasi **checklist kelengkapan file** berikut:

**File Baru yang HARUS Ada:**
- [ ] `tests/test_unit_db_connector.py` — ada, berisi semua skenario test yang didefinisikan di Bab 6.2 (≥ 22 test functions)
- [ ] `tests/test_unit_schema_initializer.py` — ada, berisi semua skenario test yang didefinisikan di Bab 6.3 (≥ 30 test functions)

**File yang TIDAK BOLEH BERUBAH:**
- [ ] `db/db_connector.py` — **TIDAK BERUBAH**
- [ ] `db/schema_initializer.py` — **TIDAK BERUBAH**
- [ ] `db/__init__.py` — **TIDAK BERUBAH**
- [ ] `db/query_builder.py` — **TIDAK BERUBAH**
- [ ] `tests/test_db_connection.py` — **TIDAK BERUBAH**
- [ ] `tests/__init__.py` — **TIDAK BERUBAH**
- [ ] `tests/test_bom_hpp.py` — **TIDAK BERUBAH**
- [ ] `tests/test_rbac_security.py` — **TIDAK BERUBAH**
- [ ] `config/settings.py` — **TIDAK BERUBAH**
- [ ] `main.py` — **TIDAK BERUBAH**
- [ ] `schema.sql` — **TIDAK BERUBAH**
- [ ] `.env.example` — **TIDAK BERUBAH**
- [ ] `requirements.txt` — **TIDAK BERUBAH**
- [ ] Semua file di `cli/`, `logic/`, `middleware/`, `utils/`, `exports/`, `docs/` — **TIDAK BERUBAH**

---

### ⚙️ TAHAP 6 — Push dan Quality Gate

- [ ] Push seluruh commit ke server:
  ```bash
  git push origin test/unit-test-init-database-schema
  ```
- [ ] Picu review otomatis oleh Gemini 3 Flash (STK-011) untuk memverifikasi:
  - [ ] Seluruh file `.py` baru memiliki header module docstring.
  - [ ] Seluruh nama file dan folder menggunakan `snake_case`.
  - [ ] Seluruh fungsi test menggunakan konvensi `test_<behavior_spesifik>()`.
  - [ ] Tidak ada koneksi database fisik di file unit test baru.
  - [ ] Seluruh mock menggunakan `@patch` pada level yang benar (`db.db_connector.xxx`, bukan `mysql.connector` langsung).
  - [ ] Setiap test function memiliki docstring PEP 257.
  - [ ] Setiap test function memiliki type hints `-> None`.
  - [ ] Tidak ada fungsi test yang berisi `pass`, `TODO`, atau `# placeholder`.
  - [ ] File yang sudah ada dari issue sebelumnya **TIDAK TERSENTUH**.
  - [ ] Seluruh test dari scaffolding (#0093) dan feature (#0094) masih PASSED.
- [ ] Serahkan ke Junior Programmer (STK-000) untuk approval akhir.

---

## 7. Instruksi Khusus untuk Issue Ini

### 7.1. Aturan Penulisan Fungsi Test

Setiap **fungsi test baru** WAJIB mengikuti format ini:

```python
def test_<behavior_spesifik_snake_case>() -> None:
    """Deskripsi singkat apa yang diverifikasi oleh test ini.

    Skenario: [Positif/Negatif/Edge Case]
    Target: [Nama fungsi yang ditest]
    """
    # Arrange (Setup mock dan data)
    ...

    # Act (Eksekusi fungsi yang ditest)
    result = fungsi_yang_ditest(...)

    # Assert (Verifikasi hasil)
    assert result.is_success is True
    ...
```

### 7.2. Aturan Penggunaan Mock

1. **Gunakan `@patch` pada level modul yang benar**:
   - ✅ `@patch('db.db_connector.pooling.MySQLConnectionPool')`
   - ❌ `@patch('mysql.connector.pooling.MySQLConnectionPool')`

2. **Mock `time.sleep` agar test tidak lambat**:
   - ✅ `@patch('db.db_connector.time.sleep')`
   - Pada test retry, selalu mock `time.sleep` agar test tidak menunggu 2+4+8 detik.

3. **Gunakan `MagicMock` untuk objek koneksi dan cursor**:
   ```python
   mock_conn = MagicMock()
   mock_cursor = MagicMock()
   mock_conn.cursor.return_value = mock_cursor
   ```

4. **Gunakan `side_effect` untuk simulasi sequence of results atau errors**:
   ```python
   mock_cursor.execute.side_effect = [None, mysql.connector.Error(errno=1050, msg='Exists'), None]
   ```

5. **Untuk mysql.connector.Error, gunakan constructor yang tepat**:
   ```python
   # Cara yang benar membuat mock error MySQL
   error = mysql.connector.Error(msg='Connection refused', errno=2003)
   ```

### 7.3. Aturan Clean State

1. **WAJIB** reset `db_mod._connection_pool = None` sebelum DAN sesudah setiap test di `test_unit_db_connector.py`.
2. **WAJIB** menggunakan `@pytest.fixture(autouse=True)` untuk otomatis cleanup.
3. **JANGAN** bergantung pada urutan eksekusi test — setiap test harus independen.

### 7.4. Aturan Penggunaan `tmp_path` untuk File I/O Test

```python
def test_read_sql_file_sukses(tmp_path):
    """Menggunakan tmp_path fixture pytest untuk file sementara."""
    sql_file = tmp_path / 'test.sql'
    sql_file.write_text("CREATE TABLE a (id INT);", encoding='utf-8')
    result = read_sql_file(str(sql_file))
    assert result.is_success is True
```

### 7.5. Encoding File

- Semua file `.py` baru WAJIB menggunakan encoding **UTF-8**.
- Semua file `.py` baru WAJIB menggunakan line ending **LF** (sesuai `.gitattributes`).

---

## 8. Ringkasan Jumlah Skenario Test

| File Test | Fungsi Target | Positif | Negatif | Edge Case | Validasi | Total |
|:----------|:--------------|:-------:|:-------:|:---------:|:--------:|:-----:|
| `test_unit_db_connector.py` | `create_connection_pool` | 2 | 2 | 0 | 0 | **4** |
| `test_unit_db_connector.py` | `get_db_connection` | 3 | 3 | 2 | 1 | **9** |
| `test_unit_db_connector.py` | `close_connection_pool` | 2 | 1 | 1 | 0 | **4** |
| `test_unit_db_connector.py` | `get_root_connection` | 1 | 2 | 0 | 0 | **3** |
| `test_unit_db_connector.py` | Konstanta & Struktur | 0 | 0 | 0 | 3 | **3** |
| **Subtotal `db_connector`** | | **8** | **8** | **3** | **4** | **23** |
| `test_unit_schema_initializer.py` | `split_sql_statements` | 5 | 0 | 6 | 0 | **11** |
| `test_unit_schema_initializer.py` | `read_sql_file` | 2 | 2 | 1 | 0 | **5** |
| `test_unit_schema_initializer.py` | `execute_schema_init` | 2 | 2 | 2 | 0 | **6** |
| `test_unit_schema_initializer.py` | `verify_schema_integrity` | 1 | 4 | 0 | 0 | **5** |
| `test_unit_schema_initializer.py` | `run_full_initialization` | 1 | 5 | 0 | 0 | **6** |
| `test_unit_schema_initializer.py` | Konstanta | 0 | 0 | 0 | 2 | **2** |
| **Subtotal `schema_initializer`** | | **11** | **13** | **9** | **2** | **35** |
| **GRAND TOTAL** | | **19** | **21** | **12** | **6** | **58** |

---

## 9. Checklist Kualitas Akhir

Sebelum menandai issue ini sebagai **Done**, pastikan seluruh item berikut terpenuhi:

- [ ] **Kelengkapan File**: Kedua file test baru (`test_unit_db_connector.py`, `test_unit_schema_initializer.py`) telah dibuat.
- [ ] **Jumlah Test**: Minimal **58 fungsi test** tersebar di kedua file.
- [ ] **Tidak Ada Stub/TODO**: Seluruh fungsi test berisi kode lengkap dengan assertion bermakna, tidak ada `pass` atau `TODO`.
- [ ] **Isolasi Penuh**: Tidak ada satupun test yang melakukan koneksi database MySQL fisik — seluruhnya menggunakan mock.
- [ ] **Clean State**: Setiap test melakukan reset state sebelum dijalankan via fixture `autouse`.
- [ ] **Deterministik**: Seluruh test menghasilkan PASSED secara konsisten di setiap eksekusi.
- [ ] **Coverage Target**: Coverage ≥ 90% pada `db/db_connector.py` dan `db/schema_initializer.py` (kecuali blok `if __name__ == '__main__'`).
- [ ] **Konvensi Penamaan**: Seluruh nama file/folder baru menggunakan `snake_case`, fungsi test menggunakan `test_<behavior>()`.
- [ ] **Header Docstring**: Setiap file `.py` baru memiliki header module docstring PEP 257.
- [ ] **Type Hints**: Setiap fungsi test memiliki type hints `-> None`.
- [ ] **Docstring per Test**: Setiap fungsi test memiliki docstring yang menjelaskan skenario.
- [ ] **Tidak Ada Modifikasi File Lain**: Hanya folder `tests/` yang memiliki file baru, tidak ada file lain yang berubah.
- [ ] **Regresi**: `pytest tests/ -v` → Seluruh test dari scaffolding (#0093) dan feature (#0094) masih **PASSED** (tidak ada regresi).
- [ ] **Encoding UTF-8**: Seluruh file `.py` baru ber-encoding UTF-8.
- [ ] **Line Ending LF**: Seluruh file `.py` baru menggunakan LF (diatur oleh `.gitattributes`).
- [ ] **Compilable**: Seluruh file `.py` baru lolos `python -m py_compile` tanpa error.
- [ ] **Commit Rapi**: Setiap commit mengikuti Conventional Commits format `test(scope): deskripsi`.

---

## 10. Referensi Commit Message untuk Issue Ini

Berikut adalah daftar lengkap commit message yang harus digunakan (sesuai Conventional Commits dan Git Workflow Bab 5):

| Tahap | Commit Message |
|:-----:|:---------------|
| 2 | `test(db): tambah unit test terisolasi untuk db_connector.py` |
| 3 | `test(db): tambah unit test terisolasi untuk schema_initializer.py` |

---

*Issue ini dideklarasikan sebagai spesifikasi resmi unit test modul infrastruktur database multi-cabang proyek AbuCom. Dikerjakan oleh persona `Senior Python Test Engineer & Database Mocking Specialist`.*
