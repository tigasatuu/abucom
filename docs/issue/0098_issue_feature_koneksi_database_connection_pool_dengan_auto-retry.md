---
judul      : Feature Koneksi Database Connection Pool dengan Auto-Retry
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
status     : Open
prioritas  : High (Infrastruktur Kritis — Fondasi Seluruh Modul M.1 s.d M.10)
tanggal    : 2026-06-04
penyusun   : Claude Opus 4.6 (Thinking) — STK-013
target     : db/db_connector.py, db/query_builder.py, db/__init__.py, config/settings.py, main.py, tests/test_db_connector.py
branch     : feature/db-connection-pool-retry
---

# Issue — Feature Koneksi Database Connection Pool dengan Auto-Retry

---

## 1. Persona Eksekutor

### 1.1. Identitas AI yang Ditugaskan
**Persona**: `Senior Backend Database Engineer & Connection Reliability Specialist`

Kamu adalah seorang Senior Backend Database Engineer yang berspesialisasi dalam infrastruktur koneksi database berskala enterprise. Kamu memiliki pengalaman mendalam dalam:
- Implementasi connection pooling MySQL menggunakan driver `mysql-connector-python`.
- Mekanisme retry otomatis dengan exponential backoff untuk jaringan LAN offline.
- Penerapan paradigma Functional Programming (FP) murni Python 3.14.2+ tanpa class/OOP.
- Penulisan kode yang patuh terhadap standar keamanan, presisi desimal, dan portabilitas Dual-OS.
- Penulisan unit testing dan integration testing yang deterministik.

### 1.2. Atribusi Commit
Gunakan atribusi berikut pada setiap commit:
```
Co-authored-by: Claude Sonnet 4.6 (STK-004)
```

### 1.3. Prinsip Kerja
- Kerjakan dengan **rapi, bersih, tidak tergesa-gesa, dan tidak buru-buru** agar hasilnya maksimal.
- Pastikan setiap baris kode **sudah final dan lengkap** sehingga tidak perlu dipertanyakan atau diinterupsi karena ada yang kurang.
- Jangan mengorbankan kualitas demi kecepatan.
- Jangan pernah menebak atau berhalusinasi terhadap data yang tidak ada — tandai dengan `# TODO: [DATA BELUM TERSEDIA]`.

---

## 2. Dokumen Referensi

### 2.1. File Referensi yang WAJIB Dibaca Sebelum Implementasi

Bacalah dan pahami seluruh file referensi berikut **sebelum** memulai implementasi. Ekstrak semua detail data yang relevan dari setiap dokumen.

| No | File Referensi | Path Relatif | Prioritas | Relevansi untuk Issue Ini |
|:---:|---|---|:---:|---|
| **R-01** | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` | **PRIMER** | Bab 2.2 (FP Murni), Bab 2.2.6 (Result Pattern), Bab 5 (Code Style), Bab 6 (Docstrings PEP 257), Bab 7 (Type Hints PEP 484), Bab 8.9 (Pola Connection Pooling & Retry), Bab 9 (SQL & Data Access), Bab 10.8 (System Logging), Bab 11.5 (Error Codes ERR-DB), Bab 14 (Testing), Bab 15 (Git Workflow) |
| **R-02** | System Architecture v1.2 | `docs/sdlc/03_design/03_system_architecture.md` | **PRIMER** | Bab 4.3.3 (Data Access Layer), Bab 6.2 (Connection Pooling & Retry Strategy), Bab 6.3 (ACID Transaction), Bab 12 (Risiko R-01: LAN failure) |
| **R-03** | Module Structure v1.2 | `docs/sdlc/04_implementation/03_module_structure.md` | **PRIMER** | Bab 6.2 (db/db_connector.py specification), Bab 6.3 (db/query_builder.py specification) |
| **R-04** | Git Workflow v1.2 | `docs/sdlc/04_implementation/04_git_workflow.md` | **SEKUNDER** | Bab 4 (Branch naming), Bab 5 (Commit convention), Bab 6 (Development workflow) |
| **R-05** | Test Plan v1.2 | `docs/sdlc/05_testing/01_test_plan.md` | **SEKUNDER** | Bab 7.1 (Connection Pooling & Retry test scenarios), Bab 7.2 (ACID Transaction test) |
| **R-06** | Environment Setup v1.1 | `docs/sdlc/04_implementation/02_environment_setup.md` | **TERSIER** | Setup `.env`, virtual environment, dependencies |
| **R-07** | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | **TERSIER** | Bab 6.5 (.env startup validation), System logging |

> [!IMPORTANT]
> File `docs/sdlc/narasi.txt` **tidak diperlukan** sebagai referensi utama untuk issue ini. Issue ini berfokus pada infrastruktur teknis database layer yang sudah terspesifikasi lengkap di dokumen SDLC di atas.

### 2.2. File Kode Sumber yang WAJIB Dibaca

| No | File Kode | Path Absolut | Status | Relevansi |
|:---:|---|---|:---:|---|
| **C-01** | db_connector.py | `db/db_connector.py` | Sudah Ada (Scaffolding) | File utama yang akan divalidasi dan disempurnakan |
| **C-02** | query_builder.py | `db/query_builder.py` | Sudah Ada (TODO) | File wrapper ACID transaction yang tergantung pada db_connector |
| **C-03** | db/__init__.py | `db/__init__.py` | Sudah Ada | File re-export yang harus diselaraskan |
| **C-04** | config/settings.py | `config/settings.py` | Sudah Ada | File konfigurasi yang menyuplai parameter koneksi |
| **C-05** | main.py | `main.py` | Sudah Ada | Entry point yang memanggil `create_connection_pool()` |
| **C-06** | .env.example | `.env.example` | Sudah Ada | Template variabel konfigurasi runtime |
| **C-07** | requirements.txt | `requirements.txt` | Sudah Ada | Daftar dependensi terkunci |

---

## 3. Rangkuman Data Relevan dari Dokumen Referensi

### 3.1. Spesifikasi Connection Pool (dari R-01 Bab 8.9 & R-02 Bab 6.2)

| Parameter | Nilai Standar | Sumber |
|---|---|---|
| Pool Name | `"abupool"` | R-01 Bab 8.9, R-02 Bab 6.2 |
| Pool Size | `5` (default) | R-01 Bab 8.9, R-02 Bab 6.2, C-04 (settings.py) |
| Pool Reset Session | `True` | C-01 (db_connector.py line 57) |
| Driver Library | `mysql-connector-python==8.4.0` | C-07 (requirements.txt) |
| Pool Class | `mysql.connector.pooling.MySQLConnectionPool` | R-01 Bab 9.5 |

### 3.2. Spesifikasi Retry Mechanism (dari R-01 Bab 8.9, Bab 9.6 & R-02 Bab 6.2)

| Parameter | Nilai Standar | Sumber |
|---|---|---|
| Maksimum Retry | **3 kali** | R-01 Bab 8.9, R-02 Bab 6.2 |
| Jeda Waktu | **Exponential Backoff: 2^attempt detik** | R-01 Bab 8.9 |
| Detail Interval | 2 detik → 4 detik → 8 detik | R-01 Bab 9.6 |
| Error Code Trigger | MySQL Error `2006` (Server gone away) | R-01 Bab 8.9, R-02 Bab 6.2 |
| Error Code Trigger | MySQL Error `2013` (Lost connection during query) | R-01 Bab 8.9, R-02 Bab 6.2 |
| Error Kode Aplikasi | `ERR-DB-001` (Koneksi pool gagal) | R-01 Bab 11.5 |

### 3.3. Spesifikasi ACID Transaction (dari R-01 Bab 8.8 & R-02 Bab 6.3)

| Parameter | Nilai Standar | Sumber |
|---|---|---|
| Engine Database | `InnoDB` (wajib) | R-02 Bab 6.3 |
| Isolation Level | `REPEATABLE READ` | R-02 Bab 6.3 |
| Pola Wrapper | Fungsional Result Pattern (commit/rollback) | R-01 Bab 8.8 |
| Error Kode TX | `ERR-DB-TX` | R-01 Bab 8.8 |

### 3.4. Spesifikasi Konfigurasi .env (dari C-04 & C-06)

| Variabel .env | Default Value | Tipe Python | Deskripsi |
|---|---|---|---|
| `DB_HOST` | `localhost` | `str` | IP statis server database LAN |
| `DB_PORT` | `3306` | `int` | Port MySQL default |
| `DB_USER` | `abucom_app` | `str` | Username limited database |
| `DB_PASSWORD` | (wajib diisi manual) | `str` | Password database |
| `DB_NAME` | `abucom_db` | `str` | Nama database target |
| `DB_POOL_SIZE` | `5` | `int` | Jumlah koneksi dalam pool |

### 3.5. Spesifikasi Coding Standard yang Harus Dipatuhi (dari R-01)

| Aturan | Detail | Referensi |
|---|---|---|
| Paradigma | Functional Programming murni — DILARANG menggunakan `class` | R-01 Bab 2.2.3 |
| Error Handling | Result Pattern `NamedTuple('Result', ['is_success', 'data', 'error_msg'])` | R-01 Bab 2.2.6 |
| Imutabilitas | Semua struktur data menggunakan `namedtuple` atau `frozen dataclass` | R-01 Bab 2.2.2 |
| Type Hints | Wajib PEP 484 lengkap (gunakan `list[...]`, bukan `typing.List`) | R-01 Bab 7 |
| Docstrings | Wajib PEP 257 Google Style (Args/Returns/Raises) | R-01 Bab 6 |
| String | Single quote untuk internal, double quote untuk display CLI & docstring | R-01 Bab 5.5 |
| Import Order | Standard → Third-Party → Local | R-01 Bab 5.4 |
| Penamaan Fungsi | `snake_case` verb_noun | R-01 Bab 3.2 |
| Penamaan Konstanta | `UPPER_SNAKE_CASE` | R-01 Bab 3.3 |
| Panjang Baris | Maksimal 120 karakter | R-01 Bab 5.3 |
| Indentasi | 4 spasi, dilarang Tab | R-01 Bab 5.2 |
| Header Module | Wajib ada header metadata (Nama Modul, Deskripsi, Author, Tanggal) | R-01 Bab 6.4 |
| Logging | Gunakan `logging` Python standard (console jika development, file jika production) | R-01 Bab 10.8 |
| Error Code | Format `ERR-[KATEGORI]-[NOMOR]` — Database: `ERR-DB` | R-01 Bab 11.5 |
| NULL Handling | `None` dari MySQL → handle eksplisit sebelum aritmatika | R-01 Bab 9.8 |
| Parameterized Query | Wajib `%s` placeholder, DILARANG f-string untuk SQL | R-01 Bab 9.1-9.2 |

### 3.6. Spesifikasi Testing yang Harus Dipenuhi (dari R-01 Bab 14 & R-05)

| Aturan | Detail | Referensi |
|---|---|---|
| Framework | `pytest` atau `unittest` | R-01 Bab 14.1 |
| Code Coverage | ≥ 90% untuk logika bisnis di `logic/` | R-01 Bab 14.2 |
| Penamaan File Test | `test_<modul_target>.py` di folder `tests/` | R-01 Bab 14.3 |
| Penamaan Fungsi Test | `test_<behavior_spesifik>()` | R-01 Bab 14.3 |
| Unit Test Pure | Deterministik, terisolasi, DILARANG koneksi fisik DB | R-01 Bab 14.4 |
| Integration Test | Gunakan database `abucom_test_db`, rollback setelah test | R-01 Bab 14.5 |

---

## 4. Batasan, Cakupan dan Alur Pengerjaan

### 4.1. Cakupan Pengerjaan (In-Scope)

Issue ini mencakup **HANYA** hal-hal berikut:
1. **Validasi dan penyempurnaan** file `db/db_connector.py` yang sudah ada (scaffolding).
2. **Implementasi penuh** file `db/query_builder.py` (saat ini masih TODO).
3. **Penyelarasan** file `db/__init__.py` agar re-export fungsi publik sudah sesuai.
4. **Verifikasi** integrasi dengan `config/settings.py` dan `main.py` yang sudah ada.
5. **Pembuatan** file test `tests/test_db_connector.py` untuk unit test dan integration test.

### 4.2. Di Luar Cakupan (Out-of-Scope)

> [!CAUTION]
> Issue ini **DILARANG KERAS** menyentuh atau memodifikasi file-file berikut:
> - `db/schema_initializer.py` — Modul inisialisasi schema (sudah ada dan berfungsi).
> - `db/seed_data.py` — Modul seed data (sudah ada dan berfungsi).
> - `config/settings.py` — **Jangan dimodifikasi** kecuali ada bug yang ditemukan (laporkan sebagai temuan).
> - `main.py` — **Jangan dimodifikasi** kecuali ada ketidaksesuaian panggilan fungsi (laporkan sebagai temuan).
> - File apapun di `cli/`, `logic/`, `middleware/`, `utils/` — **TIDAK BOLEH DISENTUH**.
> - File apapun di `docs/sdlc/` — **TIDAK BOLEH DISENTUH**.

### 4.3. Alur Pengerjaan (Execution Flow)

```
[1] Baca seluruh file referensi R-01 s.d R-07
        ↓
[2] Baca seluruh file kode C-01 s.d C-07
        ↓
[3] Ekstrak & rangkum data relevan
        ↓
[4] Validasi db/db_connector.py terhadap standar
        ↓
[5] Implementasi db/query_builder.py (dari TODO → implementasi penuh)
        ↓
[6] Selaraskan db/__init__.py
        ↓
[7] Verifikasi integrasi dengan main.py & settings.py
        ↓
[8] Buat tests/test_db_connector.py
        ↓
[9] Jalankan test suite & verifikasi coverage
        ↓
[10] Self-review terhadap 12 checklist Coding Standard
```

---

## 5. Instruksi Keamanan Feature (Non-Interference)

> [!WARNING]
> **Jaminan Non-Interference**: Pastikan implementasi issue ini TIDAK menyenggol atau merusak feature lain yang sudah ada. Lakukan verifikasi berikut:

- [ ] **Verifikasi-01**: Pastikan fungsi `get_root_connection()` di `db/db_connector.py` TIDAK dimodifikasi — fungsi ini digunakan oleh `schema_initializer.py`.
- [ ] **Verifikasi-02**: Pastikan `db/__init__.py` tetap meng-export `run_full_initialization` dan `verify_schema_integrity` dari `schema_initializer.py`.
- [ ] **Verifikasi-03**: Pastikan `db/__init__.py` tetap meng-export `run_seed_all` dan `verify_seed_integrity` dari `seed_data.py`.
- [ ] **Verifikasi-04**: Pastikan signature fungsi `create_connection_pool()` di `db/db_connector.py` TIDAK berubah — fungsi ini dipanggil oleh `main.py` line 55-62.
- [ ] **Verifikasi-05**: Pastikan `Result` NamedTuple yang dikembalikan oleh semua fungsi memiliki field `['is_success', 'data', 'error_msg']` — konsisten dengan yang sudah digunakan.
- [ ] **Verifikasi-06**: Setelah implementasi selesai, jalankan `python main.py` dan pastikan startup flow tidak error.

---

## 6. Checklist Implementasi Detail (Low-Level)

### FASE 1: Pembacaan dan Pemahaman (Research Phase)

> [!NOTE]
> Fase ini adalah fase membaca. DILARANG menulis atau memodifikasi kode apapun di fase ini.

- [ ] **1.1** Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — fokus pada Bab 2.2.6 (Result Pattern), Bab 8.8 (ACID Transaction Wrapper), Bab 8.9 (Connection Pooling & Retry), Bab 9 (SQL & Data Access), Bab 10.8 (System Logging).
- [ ] **1.2** Baca file `docs/sdlc/03_design/03_system_architecture.md` — fokus pada Bab 6.2 (Connection Pooling & Retry Strategy), Bab 6.3 (ACID Transaction), Bab 12 (Risiko R-01).
- [ ] **1.3** Baca file `docs/sdlc/04_implementation/03_module_structure.md` — fokus pada Bab 6 (Data Access Layer specification).
- [ ] **1.4** Baca file `db/db_connector.py` baris 1-172 secara keseluruhan.
- [ ] **1.5** Baca file `db/query_builder.py` baris 1-54 secara keseluruhan.
- [ ] **1.6** Baca file `db/__init__.py` baris 1-13 secara keseluruhan.
- [ ] **1.7** Baca file `config/settings.py` baris 1-84 secara keseluruhan.
- [ ] **1.8** Baca file `main.py` baris 1-82 secara keseluruhan.
- [ ] **1.9** Baca file `.env.example` baris 1-36 secara keseluruhan.
- [ ] **1.10** Baca file `requirements.txt` baris 1-10 secara keseluruhan.
- [ ] **1.11** Rangkum semua temuan — catat setiap inkonsistensi, data yang kosong, atau ketidaksesuaian antara dokumen referensi dan kode yang ada.

---

### FASE 2: Validasi dan Penyempurnaan `db/db_connector.py`

> [!NOTE]
> File ini sudah memiliki scaffolding yang cukup baik. Tugas kamu adalah memvalidasi dan menyempurnakan agar 100% sesuai standar SDLC.

#### 2.1. Validasi Struktur Header Module

- [ ] **2.1.1** Verifikasi header module sudah mengandung: `Nama Modul`, `Deskripsi`, `Author`, `Tanggal`. ✅ (Sudah ada di line 1-8)
- [ ] **2.1.2** Pastikan deskripsi header akurat menggambarkan fungsi modul — saat ini: `"Inisialisasi connection pool database MySQL lokal menggunakan driver mysql-connector-python. Implementasi retry otomatis dengan exponential backoff saat menangkap error MySQL 2006/2013."` ✅ (Sudah sesuai)

#### 2.2. Validasi Import dan Konstanta

- [ ] **2.2.1** Verifikasi urutan import sesuai standar: Standard Library → Third-Party → Local.
  - Saat ini: `time`, `logging`, `collections.namedtuple` (Standard) → `mysql.connector`, `mysql.connector.pooling` (Third-Party). ✅ Sudah benar.
- [ ] **2.2.2** Verifikasi konstanta menggunakan `UPPER_SNAKE_CASE`:
  - `MAX_RETRIES = 3` ✅
  - `RETRY_ERROR_CODES = (2006, 2013)` ✅
- [ ] **2.2.3** Verifikasi `Result` NamedTuple sudah sesuai pola standar:
  - `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])` ✅

#### 2.3. Validasi Fungsi `create_connection_pool()`

- [ ] **2.3.1** Verifikasi signature fungsi memiliki type hints lengkap PEP 484.
  - Saat ini: parameter sudah ter-typed, return type `-> Result` sudah ada. ✅
- [ ] **2.3.2** Verifikasi docstring sudah mengikuti PEP 257 Google Style (Args/Returns).
  - Saat ini sudah memiliki Args dan Returns. ✅
- [ ] **2.3.3** Verifikasi penggunaan `global _connection_pool` — ini diizinkan karena berada di Layer 3 (Data Access) dan bukan di Layer 2 (Business Logic).
  - **Catatan**: Penggunaan `global` di sini mengikuti pola "closure-like state" yang disebutkan di komentar line 25. ✅
- [ ] **2.3.4** Verifikasi parameter `pool_name` default value sudah sesuai: `'abupool'` ✅ (R-01 Bab 8.9).
- [ ] **2.3.5** Verifikasi parameter `pool_size` default value sudah sesuai: `5` ✅ (R-01 Bab 8.9).
- [ ] **2.3.6** Verifikasi `pool_reset_session=True` sudah ada. ✅
- [ ] **2.3.7** Verifikasi error handling mengembalikan `Result(False, None, error_msg)` bukan melempar exception. ✅
- [ ] **2.3.8** Verifikasi error code menggunakan format `ERR-DB-001`. ✅

#### 2.4. Validasi Fungsi `get_db_connection()`

- [ ] **2.4.1** Verifikasi mekanisme retry exponential backoff:
  - Loop `for attempt in range(1, max_retries + 1)` → melakukan 3 kali percobaan. ✅
  - Wait time = `2 ** attempt` → menghasilkan 2s, 4s, 8s. ✅ (Sesuai R-01 Bab 9.6)
  - Error codes trigger: `(2006, 2013)`. ✅
- [ ] **2.4.2** Verifikasi logging warning saat retry.
  - Saat ini menggunakan `_logger.warning()`. ✅
- [ ] **2.4.3** Verifikasi pengecekan pool `None` sebelum pengambilan koneksi. ✅ (line 88-89)
- [ ] **2.4.4** Verifikasi return value terakhir setelah semua retry gagal:
  - `Result(False, None, 'ERR-DB-001: ...')`. ✅

#### 2.5. Validasi Fungsi `close_connection_pool()`

- [ ] **2.5.1** Verifikasi fungsi mengembalikan `Result` pattern. ✅
- [ ] **2.5.2** Verifikasi fungsi menangani kasus pool sudah `None`. ✅ (line 122-123)
- [ ] **2.5.3** Verifikasi penggunaan `_remove_connections()` dengan `hasattr` safety check. ✅
- [ ] **2.5.4** Verifikasi `_connection_pool` di-set `None` setelah penutupan. ✅

#### 2.6. Validasi Fungsi `get_root_connection()`

- [ ] **2.6.1** Verifikasi fungsi ini TIDAK menggunakan connection pool (sesuai komentar di docstring). ✅
- [ ] **2.6.2** Verifikasi fungsi ini digunakan KHUSUS untuk DDL (schema initialization). ✅
- [ ] **2.6.3** **JANGAN MODIFIKASI** fungsi ini — sudah digunakan oleh `schema_initializer.py`.

#### 2.7. Penyempurnaan yang Diperlukan pada `db/db_connector.py`

- [ ] **2.7.1** Tambahkan konstanta `RETRY_BASE_SECONDS = 2` untuk kejelasan konfigurasi retry interval.
- [ ] **2.7.2** Tambahkan konstanta `POOL_EXHAUSTED_ERROR_CODE` atau penanganan eksplisit jika pool kehabisan koneksi (pool exhaustion).
- [ ] **2.7.3** Tambahkan fungsi `get_pool_status() -> Result` yang mengembalikan informasi pool aktif (nama pool, ukuran pool, status aktif/non-aktif) untuk kebutuhan debugging dan monitoring pada development mode.
  - Signature: `def get_pool_status() -> Result`
  - Return: `Result(True, {'pool_name': str, 'pool_size': int, 'is_active': bool}, None)`
- [ ] **2.7.4** Pastikan setiap `_logger.error()` menggunakan format yang konsisten:
  - Format: `f"ERR-DB-XXX: [Pesan deskriptif] (Detail Error: {error_detail})"`
- [ ] **2.7.5** Tambahkan docstring `Example:` pada setiap fungsi publik (sesuai template R-01 Bab 6.2).
- [ ] **2.7.6** Verifikasi bahwa `time.sleep()` di retry **tidak** memblokir thread utama secara fatal — tambahkan komentar penjelasan bahwa sistem ini single-threaded CLI sehingga blocking sleep bisa diterima.

---

### FASE 3: Implementasi Penuh `db/query_builder.py`

> [!IMPORTANT]
> File ini saat ini MASIH berisi TODO placeholder. Implementasikan secara PENUH sesuai spesifikasi di R-01 Bab 8.8, R-02 Bab 6.3, dan R-03 Bab 6.3.

#### 3.1. Struktur File

- [ ] **3.1.1** Tulis header module baru (PEP 257):
  ```python
  """
  Nama Modul: query_builder.py
  Deskripsi: Wrapper eksekusi query SQL aman terparameter (%s bindings)
             dan block penjamin atomik ACID transaksi InnoDB.
             Mendukung operasi SELECT, INSERT, UPDATE, DELETE dengan
             penanganan error fungsional Result Pattern.
  Author: [Nama AI Executor]
  Tanggal: [YYYY-MM-DD]
  """
  ```
- [ ] **3.1.2** Tulis import sesuai urutan standar:
  ```python
  # 1. Standard Library
  import logging
  from collections import namedtuple
  from typing import Callable, Any

  # 2. Third-Party
  import mysql.connector

  # 3. Local Modules
  from db.db_connector import get_db_connection
  ```
- [ ] **3.1.3** Definisikan `Result` NamedTuple:
  ```python
  Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
  ```
- [ ] **3.1.4** Definisikan logger modul:
  ```python
  _logger = logging.getLogger('abucom.db.query')
  ```

#### 3.2. Implementasi Fungsi `execute_query()`

- [ ] **3.2.1** Implementasikan fungsi `execute_query()` dengan spesifikasi berikut:
  - **Signature**:
    ```python
    def execute_query(
        db_connection,
        query: str,
        params: tuple | None = None,
        fetch_one: bool = False,
        fetch_all: bool = True
    ) -> Result:
    ```
  - **Deskripsi**: Mengeksekusi query SQL tunggal dengan parameterized bindings `%s`.
  - **Docstring**: Wajib PEP 257 Google Style lengkap (Args/Returns/Raises/Example).
  - **Logika Implementasi**:
    1. Buat `cursor = db_connection.cursor(dictionary=True)`.
    2. Eksekusi `cursor.execute(query, params)`.
    3. Jika query adalah SELECT (mengandung data yang di-fetch):
       - `fetch_one=True`: return `cursor.fetchone()`
       - `fetch_all=True`: return `cursor.fetchall()`
    4. Jika query adalah INSERT/UPDATE/DELETE:
       - Return `cursor.rowcount` sebagai data.
    5. Wrap semua error dalam `Result(False, None, error_msg)`.
    6. Pastikan cursor di-close di `finally` block.
  - **Error Handling**:
    - Tangkap `mysql.connector.Error` → `ERR-DB-002: Eksekusi query gagal`.
    - Tangkap `Exception` generik → `ERR-DB-002: Eksekusi query gagal (Error umum)`.
  - **DILARANG**: Menggunakan f-string untuk menyusun query SQL.

#### 3.3. Implementasi Fungsi `execute_acid_transaction()`

- [ ] **3.3.1** Implementasikan fungsi `execute_acid_transaction()` dengan spesifikasi berikut:
  - **Signature** (sudah ada, pertahankan):
    ```python
    def execute_acid_transaction(
        db_connection,
        operations: list[Callable[[Any], Any]]
    ) -> Result:
    ```
  - **Deskripsi**: Wrapper fungsional penjamin transaksi ACID rollback/commit InnoDB.
  - **Docstring**: Wajib PEP 257 Google Style lengkap.
  - **Logika Implementasi** (sesuai R-01 Bab 8.8):
    1. Buat `cursor = db_connection.cursor(dictionary=True)`.
    2. Panggil `db_connection.start_transaction()`.
    3. Iterasi `operations`: `results = [op(cursor) for op in operations]`.
    4. Panggil `db_connection.commit()`.
    5. Return `Result(True, results, None)`.
    6. Pada exception:
       - Panggil `db_connection.rollback()`.
       - Return `Result(False, None, f"ERR-DB-TX: Transaksi dibatalkan secara aman. Detail: {str(e)}")`.
    7. Pastikan cursor di-close di `finally` block.
  - **Logging**: Log `_logger.error()` saat rollback terjadi.

#### 3.4. Implementasi Fungsi `execute_insert()`

- [ ] **3.4.1** Implementasikan fungsi helper `execute_insert()`:
  - **Signature**:
    ```python
    def execute_insert(
        db_connection,
        query: str,
        params: tuple | None = None
    ) -> Result:
    ```
  - **Deskripsi**: Mengeksekusi INSERT query dan mengembalikan `lastrowid`.
  - **Logika**:
    1. Buat cursor, execute query dengan params.
    2. `db_connection.commit()`
    3. Return `Result(True, cursor.lastrowid, None)`.
    4. Pada error: rollback + return `Result(False, None, error_msg)`.

#### 3.5. Implementasi Fungsi `execute_many()`

- [ ] **3.5.1** Implementasikan fungsi `execute_many()` untuk bulk insert (CSV import):
  - **Signature**:
    ```python
    def execute_many(
        db_connection,
        query: str,
        data_list: list[tuple]
    ) -> Result:
    ```
  - **Deskripsi**: Mengeksekusi INSERT massal menggunakan `cursor.executemany()` untuk import CSV (sesuai R-01 Bab 9.4).
  - **Logika**:
    1. Buat cursor, execute `cursor.executemany(query, data_list)`.
    2. Commit dan return jumlah baris yang dimasukkan.
    3. Pada error: rollback + return error.

#### 3.6. Implementasi Fungsi `execute_with_retry()`

- [ ] **3.6.1** Implementasikan fungsi `execute_with_retry()` yang menggabungkan connection pool + retry + query execution:
  - **Signature**:
    ```python
    def execute_with_retry(
        query: str,
        params: tuple | None = None,
        fetch_one: bool = False,
        fetch_all: bool = True,
        max_retries: int = 3
    ) -> Result:
    ```
  - **Deskripsi**: Fungsi utama yang memanggil `get_db_connection()` dari pool, lalu menjalankan query. Jika koneksi gagal (error 2006/2013), retry akan dilakukan oleh `get_db_connection()`.
  - **Logika**:
    1. Panggil `get_db_connection(max_retries)` untuk mendapat koneksi dari pool.
    2. Jika gagal, langsung return error dari `get_db_connection()`.
    3. Jika berhasil, panggil `execute_query()` dengan koneksi yang didapat.
    4. **Pastikan koneksi di-return ke pool** setelah eksekusi: `conn.close()` di `finally`.

> [!CAUTION]
> **Penting**: `conn.close()` pada objek koneksi dari pool **TIDAK** menutup koneksi fisik, melainkan mengembalikan koneksi ke pool. Ini adalah perilaku standar dari `MySQLConnectionPool`. Jangan lupa memanggil `conn.close()` di `finally` block agar tidak terjadi connection leak.

---

### FASE 4: Penyelarasan `db/__init__.py`

- [ ] **4.1** Baca file `db/__init__.py` saat ini (C-03).
- [ ] **4.2** Verifikasi bahwa export berikut dari `db_connector.py` sudah ada:
  - `create_connection_pool` ✅
  - `get_db_connection` ✅
  - `close_connection_pool` ✅
- [ ] **4.3** Tambahkan export baru dari `db_connector.py` (jika ada fungsi baru):
  - `get_pool_status` (jika diimplementasikan di Fase 2.7.3)
- [ ] **4.4** Tambahkan export dari `query_builder.py`:
  - `execute_query`
  - `execute_acid_transaction`
  - `execute_insert`
  - `execute_many`
  - `execute_with_retry`
- [ ] **4.5** Verifikasi export existing TIDAK dihapus:
  - `run_full_initialization` dari `schema_initializer` ✅
  - `verify_schema_integrity` dari `schema_initializer` ✅
  - `run_seed_all` dari `seed_data` ✅
  - `verify_seed_integrity` dari `seed_data` ✅
- [ ] **4.6** Update header module `db/__init__.py` jika perlu.

---

### FASE 5: Verifikasi Integrasi

- [ ] **5.1** Verifikasi bahwa `main.py` line 55-62 memanggil `create_connection_pool()` dengan parameter yang sesuai dari `config.settings.py`. Pastikan parameter names cocok:
  - `host=config.db_host` ✅
  - `port=config.db_port` ✅
  - `user=config.db_user` ✅
  - `password=config.db_password` ✅
  - `database=config.db_name` ✅
  - `pool_size=config.db_pool_size` ✅
- [ ] **5.2** Verifikasi bahwa `main.py` line 77 memanggil `close_connection_pool()` untuk cleanup. ✅
- [ ] **5.3** Verifikasi bahwa `.env.example` sudah memiliki variabel `DB_POOL_SIZE=5`. ✅
- [ ] **5.4** Verifikasi bahwa `requirements.txt` sudah memiliki `mysql-connector-python==8.4.0`. ✅

---

### FASE 6: Pembuatan Test Suite `tests/test_db_connector.py`

> [!IMPORTANT]
> Test file ini harus mengcover fungsi-fungsi di `db/db_connector.py` dan `db/query_builder.py`. Ikuti spesifikasi R-01 Bab 14 dan R-05 Bab 7.1-7.2.

#### 6.1. Struktur File Test

- [ ] **6.1.1** Buat file baru: `tests/test_db_connector.py`
- [ ] **6.1.2** Tulis header module test:
  ```python
  """
  Nama Modul: test_db_connector.py
  Deskripsi: Unit testing dan integration testing untuk modul connection pool
             database (db/db_connector.py) dan query builder (db/query_builder.py).
             Mencakup pengujian retry mechanism exponential backoff,
             connection pooling, dan ACID transaction wrapper.
  Author: [Nama AI Executor]
  Tanggal: [YYYY-MM-DD]
  """
  ```

#### 6.2. Unit Test — Connection Pool (Pure/Mock)

- [ ] **6.2.1** Test `test_create_pool_sukses()`: Mock `MySQLConnectionPool` → verifikasi return `Result(True, pool_obj, None)`.
- [ ] **6.2.2** Test `test_create_pool_gagal_mysql_error()`: Mock `MySQLConnectionPool` raise `mysql.connector.Error` → verifikasi return `Result(False, None, 'ERR-DB-001: ...')`.
- [ ] **6.2.3** Test `test_create_pool_gagal_exception_umum()`: Mock raise `Exception` generik → verifikasi return `Result(False, None, 'ERR-DB-001: ...')`.
- [ ] **6.2.4** Test `test_get_connection_pool_belum_init()`: Pastikan `_connection_pool = None` → verifikasi return error `ERR-DB-001: Connection pool belum diinisialisasi.`
- [ ] **6.2.5** Test `test_get_connection_sukses()`: Mock pool.get_connection() → verifikasi return `Result(True, conn_obj, None)`.
- [ ] **6.2.6** Test `test_close_pool_sukses()`: Verifikasi pool di-close dan `_connection_pool` di-set `None`.
- [ ] **6.2.7** Test `test_close_pool_sudah_none()`: Verifikasi close pada pool yang sudah `None` return sukses tanpa error.

#### 6.3. Unit Test — Retry Mechanism (Pure/Mock)

- [ ] **6.3.1** Test `test_retry_koneksi_gagal_2006_lalu_sukses()`: Simulasikan error `2006` pada attempt 1, sukses pada attempt 2. Verifikasi retry terjadi dan koneksi berhasil.
- [ ] **6.3.2** Test `test_retry_koneksi_gagal_2013_tiga_kali()`: Simulasikan error `2013` pada semua 3 attempt. Verifikasi return error setelah semua retry habis.
- [ ] **6.3.3** Test `test_retry_interval_exponential_backoff()`: Mock `time.sleep()` → verifikasi dipanggil dengan argument `2`, `4` (untuk attempt 1 dan 2 dari 3 max).
- [ ] **6.3.4** Test `test_retry_error_non_retryable_langsung_gagal()`: Simulasikan error MySQL selain 2006/2013 (misalnya error `1045` auth failed) → verifikasi TIDAK ada retry, langsung return error.

#### 6.4. Unit Test — Query Builder (Pure/Mock)

- [ ] **6.4.1** Test `test_execute_query_select_sukses()`: Mock cursor → verifikasi `fetchall()` dipanggil dan data dikembalikan.
- [ ] **6.4.2** Test `test_execute_query_insert_sukses()`: Mock cursor → verifikasi `rowcount` dikembalikan.
- [ ] **6.4.3** Test `test_execute_query_error_handling()`: Mock cursor.execute() raise error → verifikasi return `Result(False, None, 'ERR-DB-002: ...')`.
- [ ] **6.4.4** Test `test_execute_acid_transaction_commit()`: Mock 3 operasi sukses → verifikasi `commit()` dipanggil dan `rollback()` TIDAK dipanggil.
- [ ] **6.4.5** Test `test_execute_acid_transaction_rollback()`: Mock operasi ke-2 gagal → verifikasi `rollback()` dipanggil dan `commit()` TIDAK dipanggil.
- [ ] **6.4.6** Test `test_execute_many_bulk_insert()`: Mock `executemany()` → verifikasi dipanggil dengan data list.
- [ ] **6.4.7** Test `test_execute_with_retry_connection_returned_to_pool()`: Verifikasi `conn.close()` selalu dipanggil di `finally` untuk mengembalikan koneksi ke pool.

#### 6.5. Integration Test (Opsional — Hanya Jika Database Tersedia)

- [ ] **6.5.1** Test `test_integration_pool_ke_mysql_server()`: Koneksi riil ke `abucom_test_db` → verifikasi pool berhasil dibuat dan koneksi bisa diambil.
- [ ] **6.5.2** Test `test_integration_acid_transaction_commit_dan_rollback()`: Insert + rollback → verifikasi data tidak tersimpan.

> [!NOTE]
> Integration test di atas memerlukan database `abucom_test_db` yang aktif. Tandai dengan `@pytest.mark.integration` agar bisa di-skip saat database tidak tersedia.

---

### FASE 7: Verifikasi Akhir dan Self-Review

#### 7.1. Jalankan Test Suite

- [ ] **7.1.1** Jalankan seluruh test:
  ```bash
  pytest tests/test_db_connector.py -v
  ```
- [ ] **7.1.2** Jalankan coverage:
  ```bash
  coverage run -m pytest tests/test_db_connector.py
  coverage report -m --include="db/*"
  ```
- [ ] **7.1.3** Verifikasi coverage ≥ 90% untuk `db/db_connector.py` dan `db/query_builder.py`.

#### 7.2. Self-Review Checklist Coding Standard (12 Poin)

Periksa SEMUA poin berikut bernilai **YA** sebelum menganggap implementasi selesai:

- [ ] **CS-01**: Seluruh logika di `db/` terbebas dari kata kunci `class` (murni fungsional)?
- [ ] **CS-02**: Semua fungsi publik memiliki Type Hints PEP 484 dan docstrings PEP 257 lengkap?
- [ ] **CS-03**: Tidak ada penggunaan `float` — semua nominal menggunakan `decimal.Decimal`? (N/A untuk modul ini — tetapi pastikan tidak ada float literal)
- [ ] **CS-04**: Semua query menggunakan parameterized `%s`, terbebas dari f-string SQL?
- [ ] **CS-05**: `execute_acid_transaction()` mengimplementasikan commit/rollback yang benar?
- [ ] **CS-06**: Tidak ada credentials hardcoded di file Python?
- [ ] **CS-07**: Path file (jika ada) menggunakan `pathlib`?
- [ ] **CS-08**: Tidak ada visual CLI code di module `db/` (layer 3 tidak boleh import `cli/`)?
- [ ] **CS-09**: Kode bisa berjalan di Windows 11 dan Linux Debian 12 tanpa modifikasi?
- [ ] **CS-10**: Dependensi terkunci di `requirements.txt`?
- [ ] **CS-11**: Code coverage test ≥ 90%?
- [ ] **CS-12**: Tidak ada data WhatsApp CRM di module ini? (N/A — tetapi verifikasi)

#### 7.3. Verifikasi Non-Interference Final

- [ ] **7.3.1** Jalankan `python main.py` — pastikan startup flow tidak error.
- [ ] **7.3.2** Pastikan `db/__init__.py` masih meng-export semua fungsi dari `schema_initializer.py` dan `seed_data.py`.
- [ ] **7.3.3** Pastikan tidak ada file di luar cakupan yang termodifikasi.

---

### FASE 8: Git Commit

- [ ] **8.1** Buat branch baru:
  ```bash
  git checkout main
  git pull origin main
  git checkout -b feature/db-connection-pool-retry
  ```
- [ ] **8.2** Commit perubahan secara atomis (pisahkan per layer):
  - Commit 1 (jika ada penyempurnaan di `db/db_connector.py`):
    ```bash
    git add db/db_connector.py
    git commit -m "refactor(db): sempurnakan connection pool dan retry mechanism db_connector"
    ```
  - Commit 2 (implementasi `db/query_builder.py`):
    ```bash
    git add db/query_builder.py
    git commit -m "feat(db): implementasi query builder ACID transaction wrapper"
    ```
  - Commit 3 (update `db/__init__.py`):
    ```bash
    git add db/__init__.py
    git commit -m "chore(db): tambah export query_builder di db/__init__"
    ```
  - Commit 4 (test suite):
    ```bash
    git add tests/test_db_connector.py
    git commit -m "test(db): tambah unit test connection pool retry dan query builder"
    ```

---

## 7. Penanganan Data Kosong / Tidak Tersedia

> [!WARNING]
> Jika selama implementasi ditemukan data yang kosong atau tidak tersedia di file referensi, **JANGAN menebak atau mengisi dengan asumsi**. Lakukan hal berikut:

1. Tandai dengan komentar: `# TODO: [DATA BELUM TERSEDIA] - Deskripsi data yang dibutuhkan`
2. Catat di bagian akhir commit message pada body section.
3. Laporkan dalam summary eksekusi issue ini.

### 7.1. Data yang Sudah Teridentifikasi Kosong/Belum Pasti

| No | Item | Status | Catatan |
|:---:|---|---|---|
| 1 | IP statis server produksi | Placeholder `10.10.10.10` di `.env.example` | Akan diisi saat instalasi fisik (bukan tanggung jawab issue ini) |
| 2 | Password database produksi | `YOUR_DB_PASSWORD_HERE` di `.env.example` | Akan diisi saat instalasi fisik |
| 3 | Konfigurasi retry khusus per-environment (dev vs prod) | Belum ada | **Rekomendasi**: Tambahkan variabel `DB_MAX_RETRIES` di `.env.example` — OPSIONAL, laporkan sebagai saran |

---

## 8. Instruksi Tambahan Spesifik untuk Issue Ini

### 8.1. Connection Leak Prevention (Khas Connection Pool)

> [!CAUTION]
> **Ini adalah masalah paling umum pada implementasi connection pool**. Setiap koneksi yang diambil dari pool WAJIB dikembalikan ke pool melalui `conn.close()`. Jika tidak, pool akan kehabisan koneksi (pool exhaustion) dan seluruh sistem akan freeze.

Pastikan SEMUA fungsi di `query_builder.py` yang memanggil `get_db_connection()` memiliki pola berikut:
```python
conn_result = get_db_connection()
if not conn_result.is_success:
    return conn_result  # Propagasi error

conn = conn_result.data
try:
    # ... operasi database ...
    return Result(True, data, None)
except Exception as e:
    return Result(False, None, error_msg)
finally:
    conn.close()  # WAJIB: Kembalikan koneksi ke pool
```

### 8.2. Thread Safety (Khas Connection Pool)

Meskipun AbuCom CLI bersifat single-threaded, connection pool dari `mysql-connector-python` sudah thread-safe secara bawaan. Tambahkan komentar di `db_connector.py` yang menjelaskan:
```python
# NOTE: MySQLConnectionPool dari mysql-connector-python sudah bersifat thread-safe.
# Pada sistem CLI single-threaded AbuCom, pool_size=5 menyediakan redundansi
# jika ada koneksi yang gagal di-close karena error tak terduga.
```

### 8.3. Graceful Degradation (Khas Auto-Retry)

Saat retry gagal sebanyak 3 kali, sistem harus memberikan pesan error yang jelas dan informatif ke layer di atasnya. **JANGAN** membuat program crash/exit di layer database. Biarkan layer presentasi (CLI) yang memutuskan apakah akan menampilkan error ke user atau mencoba aksi lain.

### 8.4. Logging Best Practices (Khas Database Layer)

- Level `DEBUG`: Detail query yang dieksekusi (HANYA di environment development).
- Level `WARNING`: Retry attempt koneksi yang sedang berlangsung.
- Level `ERROR`: Kegagalan fatal koneksi atau transaksi setelah semua retry habis.
- **DILARANG**: Logging password database, credentials, atau data sensitif pelanggan.

---

## 9. Kriteria Selesai (Definition of Done)

Issue #0098 dianggap **SELESAI** jika dan hanya jika SEMUA kriteria berikut terpenuhi:

- [ ] File `db/db_connector.py` sudah divalidasi dan disempurnakan sesuai standar SDLC.
- [ ] File `db/query_builder.py` sudah diimplementasikan secara PENUH (bukan TODO).
- [ ] File `db/__init__.py` sudah diselaraskan dengan export yang benar.
- [ ] File `tests/test_db_connector.py` sudah dibuat dan semua test PASS.
- [ ] Coverage `db/` ≥ 90%.
- [ ] Self-review 12 poin Coding Standard semuanya bernilai YA.
- [ ] Verifikasi non-interference LULUS semua 6 poin (Bab 5).
- [ ] `python main.py` berjalan tanpa error.
- [ ] Commit messages mengikuti Conventional Commits format.
- [ ] Tidak ada data yang di-hardcode atau dihalusinasi.

---

## 10. Referensi Dokumen

| No | Dokumen | Path Relatif |
|:---:|---|---|
| 1 | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` |
| 2 | System Architecture v1.2 | `docs/sdlc/03_design/03_system_architecture.md` |
| 3 | Module Structure v1.2 | `docs/sdlc/04_implementation/03_module_structure.md` |
| 4 | Git Workflow v1.2 | `docs/sdlc/04_implementation/04_git_workflow.md` |
| 5 | Test Plan v1.2 | `docs/sdlc/05_testing/01_test_plan.md` |
| 6 | Environment Setup v1.1 | `docs/sdlc/04_implementation/02_environment_setup.md` |
| 7 | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` |
