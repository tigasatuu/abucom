---
judul      : Unit Test Feature Koneksi Database Connection Pool dengan Auto-Retry
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
tanggal    : 2026-06-04
status     : Open
prioritas  : High
tipe       : Testing (Unit Test)
assignee   : Junior Programmer / LLM AI Model
estimasi   : 3-4 jam kerja
---

# Issue — Unit Test Feature Koneksi Database Connection Pool dengan Auto-Retry

---

## 1. Persona Pelaksana

Kamu adalah **Senior QA Engineer & Unit Test Specialist** yang bertanggung jawab penuh atas kualitas, keandalan, dan kelengkapan unit test untuk modul koneksi database AbuCom. Kamu memiliki keahlian mendalam dalam:

- **Functional Programming (FP) Python 3.14.2+** tanpa class/OOP di alur bisnis.
- **Unit testing terisolasi** menggunakan `pytest==8.2.0` dengan teknik mocking (`unittest.mock`).
- **Connection pooling** menggunakan `mysql-connector-python==8.4.0`.
- **Retry mechanism** dengan pola exponential backoff.
- **Result Pattern** (NamedTuple `Result(is_success, data, error_msg)`).
- **Standar kode AbuCom**: `snake_case` untuk fungsi/variabel, `PascalCase` untuk NamedTuple, docstring PEP 257 Google Style, type hints PEP 484.

Kamu **WAJIB** memastikan:
1. Setiap unit test **terisolasi penuh** — DILARANG melakukan koneksi fisik ke database MySQL.
2. Semua dependensi eksternal di-mock menggunakan `unittest.mock.patch` dan `MagicMock`.
3. Pengerjaan **TIDAK BOLEH** menyentuh, memodifikasi, atau merusak file manapun selain file test target.
4. Code coverage untuk modul target **WAJIB ≥ 90%** (diukur via `coverage==7.5.1`).

---

## 2. Dokumen Referensi SDLC

Sebelum memulai pengerjaan, kamu **WAJIB** membaca dan mengekstrak data relevan dari dokumen-dokumen berikut. Jangan lewatkan detail kecil apapun.

### 2.1. Daftar File Referensi Utama

| No | Dokumen | Path Relatif | Kepentingan |
|----|---------|-------------|-------------|
| 1 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | **PRIMER** — Aturan penamaan test, konvensi FP, Result Pattern, standar testing (Bab 14), connection pooling & retry (Bab 8.9, 9.5, 9.6) |
| 2 | **Test Plan v1.2** | `docs/sdlc/05_testing/01_test_plan.md` | **PRIMER** — Strategi unit testing (Bab 3.1.1), testing tools (Bab 11.3), skenario connection pooling & retry (Bab 7.1), kode error (Bab 12.4) |
| 3 | **Test Cases v1.2** | `docs/sdlc/05_testing/02_test_cases.md` | **SEKUNDER** — Skenario TC-INT-001 tentang connection pooling & retry mechanism |
| 4 | **Module Structure v1.2** | `docs/sdlc/04_implementation/03_module_structure.md` | **SEKUNDER** — Spesifikasi file `db/db_connector.py` (Bab 6.2) |
| 5 | **System Architecture v1.1** | `docs/sdlc/03_design/03_system_architecture.md` | **TERSIER** — Blueprint connection pool retry (Bab 6.2, 6.3) |

### 2.2. Rangkuman Data Teknis yang Harus Diekstrak dari Referensi

Baca setiap file di atas dan ekstrak serta rangkum informasi berikut secara spesifik:

- [ ] **Dari Coding Standard Bab 8.9**: Aturan connection pooling — `pool_name="abupool"`, `pool_size=5`, retry 3 kali, exponential backoff `2^attempt` detik (2s, 4s, 8s), MySQL error codes `2006` dan `2013`.
- [ ] **Dari Coding Standard Bab 9.5**: Inisialisasi pool menggunakan `mysql.connector.pooling.MySQLConnectionPool`.
- [ ] **Dari Coding Standard Bab 9.6**: Penanganan error database — tangkap kode error `2006`/`2013`, retry 3x exponential backoff sebelum program dibekukan aman.
- [ ] **Dari Coding Standard Bab 14.3**: Konvensi penamaan — file: `test_<modul_target>.py`, fungsi: `test_<behavior_spesifik>()`.
- [ ] **Dari Coding Standard Bab 14.4**: Unit test pure functions **WAJIB** deterministik, terisolasi penuh, **DILARANG** koneksi fisik database. Data disuplai via mock.
- [ ] **Dari Coding Standard Bab 2.2.6**: Pola Result Pattern — `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])`.
- [ ] **Dari Test Plan Bab 3.1.1**: Unit test menggunakan mock data structures (NamedTuple/Tuples), target code coverage ≥ 90%.
- [ ] **Dari Test Plan Bab 7.1**: Skenario connection pooling — simulasi 10 threads, pool_size=5 membatasi koneksi aktif, retry 3x exponential backoff saat koneksi terputus, error `ERR-DB-001`.
- [ ] **Dari Test Plan Bab 11.3.1**: Framework testing `pytest==8.2.1` (atau versi stabil terbaru di venv).
- [ ] **Dari Test Plan Bab 11.3.2**: Code coverage menggunakan `coverage==7.5.1`.
- [ ] **Dari Test Plan Bab 12.4**: Kode error `ERR-DB-001` — "Koneksi terputus. Penyimpanan transaksi dibatalkan!" untuk retry 3x limit.
- [ ] **Dari Module Structure Bab 6.2**: File `db/db_connector.py` — inisialisasi connection pool, retry automatic connection, exponential backoff, error `2006`/`2013`, SRS-F-ADD-03.

---

## 3. File Target dan Cakupan Pengerjaan

### 3.1. File Source Code yang Diuji (TIDAK BOLEH DIMODIFIKASI)

| File | Path | Deskripsi |
|------|------|-----------|
| `db_connector.py` | `db/db_connector.py` | Modul connection pool factory, retry mechanism exponential backoff, koneksi root DDL, dan pool status monitor |

### 3.2. Fungsi-Fungsi Publik yang WAJIB Dicakup Unit Test

Baca file `db/db_connector.py` dan identifikasi seluruh fungsi publik berikut:

| No | Nama Fungsi | Baris | Deskripsi Singkat |
|----|-------------|-------|-------------------|
| 1 | `create_connection_pool()` | L35-L88 | Membuat connection pool MySQL dengan parameter konfigurasi |
| 2 | `get_db_connection()` | L91-L136 | Mengambil koneksi dari pool dengan retry exponential backoff |
| 3 | `close_connection_pool()` | L139-L160 | Menutup dan membersihkan connection pool |
| 4 | `get_root_connection()` | L163-L208 | Membuat koneksi langsung (non-pool) untuk DDL |
| 5 | `get_pool_status()` | L211-L241 | Mengembalikan status informasi pool aktif |

### 3.3. Konstanta dan Struktur Data yang WAJIB Divalidasi

| Entitas | Nilai yang Diharapkan | Referensi |
|---------|----------------------|-----------|
| `MAX_RETRIES` | `3` | Coding Standard Bab 8.9 |
| `RETRY_BASE_SECONDS` | `2` | Coding Standard Bab 8.9 — interval `2^attempt` |
| `RETRY_ERROR_CODES` | `(2006, 2013)` | Coding Standard Bab 9.6 |
| `POOL_EXHAUSTED_ERROR_CODE` | `-1` | Internal module constant |
| `Result` | `namedtuple('Result', ['is_success', 'data', 'error_msg'])` | Coding Standard Bab 2.2.6 |
| `_connection_pool` | Variabel modul-level (awalnya `None`) | Internal state FP closure-like |

### 3.4. File Test Target (HANYA file ini yang boleh dibuat/dimodifikasi)

| File | Path | Status |
|------|------|--------|
| `test_unit_db_connector.py` | `tests/test_unit_db_connector.py` | **SUDAH ADA** — Validasi kelengkapan dan tambahkan skenario yang terlewat |

### 3.5. Folder Penyimpanan

Sesuai standar SDLC (Coding Standard Bab 4.1 & Bab 14.3, Module Structure Bab 12):
- **Lokasi file test**: `tests/test_unit_db_connector.py`
- **Dependency testing**: `pytest==8.2.0`, `coverage==7.5.1` (sudah tersedia di `requirements.txt`)

---

## 4. Batasan, Isolasi, dan Keamanan Pengerjaan

### 4.1. Batasan Pengerjaan

- [ ] **HANYA** mengerjakan file `tests/test_unit_db_connector.py`.
- [ ] **DILARANG** memodifikasi file `db/db_connector.py` atau file sumber manapun.
- [ ] **DILARANG** memodifikasi `db/__init__.py`, `requirements.txt`, atau file konfigurasi lain.
- [ ] **DILARANG** membuat file test baru di lokasi selain `tests/`.
- [ ] **DILARANG** menambah dependency baru tanpa justifikasi tertulis.

### 4.2. Isolasi dari Feature Lain

- [ ] Seluruh test **WAJIB** menggunakan mocking (`unittest.mock.patch`, `MagicMock`) untuk semua dependensi eksternal:
  - `mysql.connector.pooling.MySQLConnectionPool` → **MOCK**
  - `mysql.connector.connect` → **MOCK**
  - `mysql.connector.Error` → **MOCK** (buat helper untuk errno/msg)
  - `time.sleep` → **MOCK** (agar test tidak menunggu detik nyata)
- [ ] **DILARANG KERAS** melakukan koneksi fisik ke database MySQL (baik `abucom_db` maupun `abucom_test_db`).
- [ ] Setiap test harus berdiri sendiri (*independent*) — tidak bergantung pada urutan eksekusi test lain.
- [ ] Gunakan `pytest.fixture(autouse=True)` untuk reset state `_connection_pool` ke `None` sebelum DAN sesudah setiap test.

### 4.3. Kualitas Kelengkapan

- [ ] **TIDAK ADA** fungsi test yang berisi `pass`, `TODO`, atau kode placeholder yang menggantung.
- [ ] Setiap fungsi test **WAJIB** memiliki minimal 1 assertion yang bermakna.
- [ ] Setiap fungsi test **WAJIB** memiliki docstring PEP 257 yang menjelaskan: deskripsi, tipe skenario (Positif/Negatif/Edge Case), dan target fungsi.
- [ ] Code coverage modul `db/db_connector.py` **WAJIB ≥ 90%**.

---

## 5. Konvensi dan Standar Penulisan Test

### 5.1. Konvensi Penamaan

| Entitas | Format | Contoh |
|---------|--------|--------|
| File test | `test_unit_<modul>.py` | `test_unit_db_connector.py` |
| Fungsi test | `test_<nama_fungsi>_<behavior_spesifik>` | `test_create_connection_pool_sukses_dengan_parameter_valid` |
| Fixture | `snake_case` deskriptif | `reset_connection_pool` |
| Helper | `_<verb>_<noun>` (private) | `_make_mysql_error` |

### 5.2. Struktur Setiap Fungsi Test (Pola AAA)

Setiap fungsi test **WAJIB** mengikuti pola **Arrange-Act-Assert (AAA)**:

```python
def test_nama_fungsi_behavior_spesifik() -> None:
    """Deskripsi singkat apa yang diverifikasi.

    Skenario: Positif / Negatif / Edge Case / Validasi
    Target: nama_fungsi_yang_diuji
    """
    # Arrange — Siapkan data mock dan precondition
    mock_xxx = MagicMock()

    # Act — Jalankan fungsi yang diuji
    result = fungsi_yang_diuji(params)

    # Assert — Verifikasi hasil
    assert result.is_success is True
```

### 5.3. Konvensi Header File Test

```python
"""
Nama Modul: test_unit_db_connector.py
Deskripsi: Unit test terisolasi (mocked) untuk modul db/db_connector.py.
           Menguji seluruh fungsi connection pool factory, retry mechanism,
           dan koneksi root tanpa memerlukan koneksi database MySQL fisik.
Author: [Nama Pelaksana / AI Model]
Tanggal: [YYYY-MM-DD]
"""
```

### 5.4. Konvensi Import

Urutan import wajib mengikuti Coding Standard Bab 5.4.1:
1. Standard Library (`time`, `pytest`, `unittest.mock`)
2. Third-Party (`mysql.connector`)
3. Local Modules (`db.db_connector`)

### 5.5. Konvensi Error Handling dalam Test

- Gunakan helper function `_make_mysql_error(errno, msg)` untuk membuat objek `mysql.connector.Error` yang konsisten.
- Verifikasi bahwa setiap error mengandung prefix kode error `ERR-DB-001` sesuai katalog error Coding Standard Bab 11.5.
- Verifikasi pesan error mengandung detail yang informatif (errno, msg original).

### 5.6. Konvensi Clean State (Reset Data)

Setiap test **WAJIB** memiliki clean state melalui fixture berikut yang sudah auto-applied:

```python
@pytest.fixture(autouse=True)
def reset_connection_pool():
    """Reset variabel modul _connection_pool sebelum dan sesudah setiap test."""
    db_mod._connection_pool = None
    yield
    db_mod._connection_pool = None
```

Ini menjamin:
- Sebelum test: `_connection_pool = None` (clean state).
- Sesudah test: `_connection_pool = None` (teardown/cleanup).
- Tidak ada sisa state dari test sebelumnya yang bocor ke test berikutnya.

---

## 6. Skenario Test — Daftar Lengkap

### 6.1. Grup A: `create_connection_pool()` — Pembuatan Connection Pool

#### Skenario Positif (Happy Path)

- [ ] **A-POS-01**: `test_create_connection_pool_sukses_dengan_parameter_valid`
  - Mock `MySQLConnectionPool` agar mengembalikan instance pool.
  - Panggil `create_connection_pool(host='localhost', port=3306, user='app', password='pass', database='db')`.
  - **Assert**: `result.is_success is True`, `result.data` adalah mock pool instance, `result.error_msg is None`.
  - **Assert**: `db_mod._connection_pool` ter-set ke mock pool instance.
  - **Assert**: `MySQLConnectionPool` dipanggil dengan parameter benar (`pool_name='abupool'`, `pool_size=5`, `pool_reset_session=True`, dan parameter koneksi lainnya).

- [ ] **A-POS-02**: `test_create_connection_pool_sukses_dengan_pool_size_kustom`
  - Mock `MySQLConnectionPool`.
  - Panggil `create_connection_pool(..., pool_size=10, pool_name='custom_pool')`.
  - **Assert**: `result.is_success is True`.
  - **Assert**: `MySQLConnectionPool` dipanggil dengan `pool_size=10` dan `pool_name='custom_pool'`.

- [ ] **A-POS-03**: `test_create_connection_pool_sukses_dengan_port_kustom`
  - Mock `MySQLConnectionPool`.
  - Panggil `create_connection_pool(host='192.168.1.200', port=3307, ...)`.
  - **Assert**: `result.is_success is True`.
  - **Assert**: Parameter `port=3307` diteruskan ke `MySQLConnectionPool`.

#### Skenario Negatif (Unhappy Path)

- [ ] **A-NEG-01**: `test_create_connection_pool_gagal_mysql_error`
  - Mock `MySQLConnectionPool` untuk melempar `mysql.connector.Error` dengan `errno=2003`, `msg='Connection refused'`.
  - **Assert**: `result.is_success is False`, `result.data is None`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'` dan `'2003'` dan `'Connection refused'`.
  - **Assert**: `db_mod._connection_pool` tetap `None` (tidak ter-set ke pool yang gagal).

- [ ] **A-NEG-02**: `test_create_connection_pool_gagal_exception_umum`
  - Mock `MySQLConnectionPool` untuk melempar `Exception('Unexpected error')`.
  - **Assert**: `result.is_success is False`, `result.data is None`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'` dan `'Unexpected error'`.
  - **Assert**: `db_mod._connection_pool` tetap `None`.

- [ ] **A-NEG-03**: `test_create_connection_pool_gagal_host_invalid`
  - Mock `MySQLConnectionPool` untuk melempar `mysql.connector.Error` dengan `errno=2005`, `msg='Unknown MySQL server host'`.
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'`.

- [ ] **A-NEG-04**: `test_create_connection_pool_gagal_autentikasi_ditolak`
  - Mock `MySQLConnectionPool` untuk melempar `mysql.connector.Error` dengan `errno=1045`, `msg='Access denied for user'`.
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'` dan `'1045'`.

#### Validasi Input / Edge Cases

- [ ] **A-EDGE-01**: `test_create_connection_pool_pool_size_minimum_1`
  - Mock `MySQLConnectionPool`.
  - Panggil `create_connection_pool(..., pool_size=1)`.
  - **Assert**: `result.is_success is True`.
  - **Assert**: `MySQLConnectionPool` dipanggil dengan `pool_size=1`.

- [ ] **A-EDGE-02**: `test_create_connection_pool_overwrite_pool_yang_sudah_ada`
  - Set `db_mod._connection_pool = MagicMock()` (simulasi pool lama sudah ada).
  - Mock `MySQLConnectionPool` dan panggil `create_connection_pool(...)`.
  - **Assert**: `result.is_success is True`.
  - **Assert**: `db_mod._connection_pool` berubah ke pool baru (bukan pool lama).

---

### 6.2. Grup B: `get_db_connection()` — Pengambilan Koneksi dengan Retry

#### Skenario Positif (Happy Path)

- [ ] **B-POS-01**: `test_get_db_connection_sukses_dari_pool`
  - Set `db_mod._connection_pool` ke mock pool dengan `get_connection()` mengembalikan mock koneksi.
  - **Assert**: `result.is_success is True`, `result.data` adalah mock koneksi, `result.error_msg is None`.
  - **Assert**: `pool.get_connection()` dipanggil tepat 1 kali.

- [ ] **B-POS-02**: `test_get_db_connection_retry_sukses_setelah_error_2006`
  - Mock `time.sleep`.
  - Mock pool: `get_connection()` side_effect = [Error(2006), mock_conn].
  - **Assert**: `result.is_success is True`, `result.data` adalah `mock_conn`.
  - **Assert**: `get_connection()` dipanggil 2 kali.
  - **Assert**: `time.sleep` dipanggil dengan `2` (2^1 detik).

- [ ] **B-POS-03**: `test_get_db_connection_retry_sukses_setelah_error_2013`
  - Mock `time.sleep`.
  - Mock pool: `get_connection()` side_effect = [Error(2013), mock_conn].
  - **Assert**: `result.is_success is True`.
  - **Assert**: `get_connection()` dipanggil 2 kali.
  - **Assert**: `time.sleep` dipanggil dengan `2` (2^1 detik).

- [ ] **B-POS-04**: `test_get_db_connection_retry_sukses_setelah_dua_error_berturut`
  - Mock `time.sleep`.
  - Mock pool: `get_connection()` side_effect = [Error(2006), Error(2013), mock_conn].
  - **Assert**: `result.is_success is True`, `result.data` adalah `mock_conn`.
  - **Assert**: `get_connection()` dipanggil 3 kali.
  - **Assert**: `time.sleep` dipanggil 2 kali — pertama `sleep(2)`, kedua `sleep(4)`.

#### Skenario Negatif (Unhappy Path)

- [ ] **B-NEG-01**: `test_get_db_connection_gagal_pool_belum_init`
  - Pastikan `db_mod._connection_pool is None`.
  - **Assert**: `result.is_success is False`, `result.data is None`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'` dan `'belum diinisialisasi'`.

- [ ] **B-NEG-02**: `test_get_db_connection_gagal_setelah_semua_retry_habis`
  - Mock `time.sleep`.
  - Mock pool: `get_connection()` selalu melempar Error(2006).
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'`.
  - **Assert**: `get_connection()` dipanggil tepat `MAX_RETRIES` (3) kali.
  - **Assert**: `time.sleep` dipanggil 2 kali (`sleep(2)` dan `sleep(4)`), TIDAK dipanggil untuk attempt terakhir.

- [ ] **B-NEG-03**: `test_get_db_connection_gagal_error_non_retryable`
  - Mock pool: `get_connection()` melempar Error(1045, 'Access denied').
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'1045'` dan `'Access denied'`.
  - **Assert**: `get_connection()` dipanggil tepat 1 kali (TIDAK ada retry).

- [ ] **B-NEG-04**: `test_get_db_connection_gagal_exception_umum`
  - Mock pool: `get_connection()` melempar `Exception('Pool exhausted')`.
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'Pool exhausted'`.
  - **Assert**: `get_connection()` dipanggil tepat 1 kali (TIDAK ada retry untuk non-MySQL error).

- [ ] **B-NEG-05**: `test_get_db_connection_gagal_setelah_retry_error_2013_habis`
  - Mock `time.sleep`.
  - Mock pool: `get_connection()` selalu melempar Error(2013, 'Lost connection').
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'` dan `'Lost connection'`.
  - **Assert**: `get_connection()` dipanggil `MAX_RETRIES` kali.

#### Validasi Input / Edge Cases

- [ ] **B-EDGE-01**: `test_get_db_connection_retry_dengan_max_retries_kustom`
  - Mock `time.sleep`.
  - Mock pool: `get_connection()` selalu Error(2006).
  - Panggil `get_db_connection(max_retries=1)`.
  - **Assert**: `result.is_success is False`.
  - **Assert**: `get_connection()` dipanggil tepat 1 kali.
  - **Assert**: `time.sleep` TIDAK dipanggil (karena tidak ada retry setelah attempt terakhir).

- [ ] **B-EDGE-02**: `test_get_db_connection_gagal_max_retries_nol`
  - Mock pool.
  - Panggil `get_db_connection(max_retries=0)`.
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'Gagal mengambil koneksi dari pool setelah semua retry'`.
  - **Assert**: `pool.get_connection()` TIDAK pernah dipanggil.

- [ ] **B-EDGE-03**: `test_get_db_connection_exponential_backoff_timing`
  - Mock `time.sleep`.
  - Mock pool: `get_connection()` side_effect = [Error(2006), Error(2006), mock_conn].
  - **Assert**: `result.is_success is True`.
  - **Assert**: `time.sleep` dipanggil pertama dengan `2` (2^1), kedua dengan `4` (2^2).

- [ ] **B-EDGE-04**: `test_get_db_connection_retry_campuran_error_2006_dan_2013`
  - Mock `time.sleep`.
  - Mock pool: `get_connection()` side_effect = [Error(2006), Error(2013), mock_conn].
  - **Assert**: `result.is_success is True` (kedua error code retryable).
  - **Assert**: `get_connection()` dipanggil 3 kali.

- [ ] **B-EDGE-05**: `test_get_db_connection_max_retries_5_custom`
  - Mock `time.sleep`.
  - Mock pool: `get_connection()` side_effect = [Error(2006)] * 4 + [mock_conn].
  - Panggil `get_db_connection(max_retries=5)`.
  - **Assert**: `result.is_success is True`.
  - **Assert**: `get_connection()` dipanggil 5 kali.
  - **Assert**: `time.sleep` dipanggil 4 kali dengan interval: `2, 4, 8, 16`.

---

### 6.3. Grup C: `close_connection_pool()` — Penutupan Pool

#### Skenario Positif

- [ ] **C-POS-01**: `test_close_connection_pool_sukses_saat_pool_none`
  - `db_mod._connection_pool = None`.
  - **Assert**: `result.is_success is True`, `result.data is None`, `result.error_msg is None`.

- [ ] **C-POS-02**: `test_close_connection_pool_sukses_saat_pool_ada`
  - Set `db_mod._connection_pool = MagicMock()` (mock pool aktif).
  - **Assert**: `result.is_success is True`.
  - **Assert**: `mock_pool._remove_connections()` dipanggil sekali.
  - **Assert**: `db_mod._connection_pool is None` setelah close.

#### Skenario Negatif

- [ ] **C-NEG-01**: `test_close_connection_pool_gagal_exception`
  - Set mock pool dengan `_remove_connections()` melempar `Exception('Cannot remove')`.
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'` dan `'Cannot remove'`.
  - **Assert**: `db_mod._connection_pool` TIDAK di-reset ke None (pool tetap ada karena exception).

#### Edge Cases

- [ ] **C-EDGE-01**: `test_close_connection_pool_sukses_tanpa_remove_connections`
  - Set mock pool **tanpa** method `_remove_connections` (menggunakan `MagicMock(spec=[])`).
  - **Assert**: `result.is_success is True`.
  - **Assert**: `db_mod._connection_pool is None`.

- [ ] **C-EDGE-02**: `test_close_connection_pool_idempotent_panggilan_berulang`
  - Set `db_mod._connection_pool = MagicMock()`.
  - Panggil `close_connection_pool()` → assert sukses.
  - Panggil lagi `close_connection_pool()` → assert tetap sukses (idempotent).
  - **Assert**: Tidak ada exception di panggilan kedua.

---

### 6.4. Grup D: `get_root_connection()` — Koneksi Root Non-Pool

#### Skenario Positif

- [ ] **D-POS-01**: `test_get_root_connection_sukses`
  - Mock `mysql.connector.connect` mengembalikan mock koneksi.
  - Panggil `get_root_connection(host='localhost', port=3306, user='root', password='rootpass')`.
  - **Assert**: `result.is_success is True`, `result.data` adalah mock koneksi.
  - **Assert**: `mysql.connector.connect` dipanggil dengan parameter benar.

- [ ] **D-POS-02**: `test_get_root_connection_sukses_dengan_host_remote`
  - Mock `mysql.connector.connect`.
  - Panggil `get_root_connection(host='192.168.1.200', port=3306, user='root', password='pass')`.
  - **Assert**: `result.is_success is True`.
  - **Assert**: `mysql.connector.connect` dipanggil dengan `host='192.168.1.200'`.

#### Skenario Negatif

- [ ] **D-NEG-01**: `test_get_root_connection_gagal_mysql_error`
  - Mock `mysql.connector.connect` melempar `mysql.connector.Error(errno=2003, msg='Connection refused')`.
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'` dan `'Koneksi administratif gagal'` dan `'2003'`.

- [ ] **D-NEG-02**: `test_get_root_connection_gagal_exception_umum`
  - Mock `mysql.connector.connect` melempar `Exception('DNS Resolution Failure')`.
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'` dan `'DNS Resolution Failure'`.

- [ ] **D-NEG-03**: `test_get_root_connection_gagal_autentikasi_root_salah`
  - Mock `mysql.connector.connect` melempar `mysql.connector.Error(errno=1045, msg='Access denied for user root')`.
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'1045'`.

#### Validasi

- [ ] **D-VAL-01**: `test_get_root_connection_tidak_menggunakan_pool`
  - Mock `mysql.connector.connect`.
  - Panggil `get_root_connection(...)`.
  - **Assert**: `db_mod._connection_pool` tetap `None` (koneksi root TIDAK mempengaruhi pool).

---

### 6.5. Grup E: `get_pool_status()` — Status Pool

#### Skenario Positif

- [ ] **E-POS-01**: `test_get_pool_status_saat_pool_aktif`
  - Set `db_mod._connection_pool = MagicMock(pool_name='abupool', pool_size=5)`.
  - **Assert**: `result.is_success is True`.
  - **Assert**: `result.data` == `{'pool_name': 'abupool', 'pool_size': 5, 'is_active': True}`.

- [ ] **E-POS-02**: `test_get_pool_status_saat_pool_none`
  - Pastikan `db_mod._connection_pool is None`.
  - **Assert**: `result.is_success is True`.
  - **Assert**: `result.data` == `{'pool_name': None, 'pool_size': 0, 'is_active': False}`.

#### Skenario Negatif

- [ ] **E-NEG-01**: `test_get_pool_status_gagal_exception`
  - Set mock pool dengan `pool_name` property yang melempar exception.
  - **Assert**: `result.is_success is False`.
  - **Assert**: `result.error_msg` mengandung `'ERR-DB-001'`.

#### Edge Cases

- [ ] **E-EDGE-01**: `test_get_pool_status_pool_kustom_size`
  - Set `db_mod._connection_pool = MagicMock(pool_name='custom', pool_size=10)`.
  - **Assert**: `result.data['pool_name']` == `'custom'`.
  - **Assert**: `result.data['pool_size']` == `10`.

---

### 6.6. Grup F: Validasi Konstanta dan Struktur

- [ ] **F-VAL-01**: `test_konstanta_max_retries`
  - **Assert**: `MAX_RETRIES == 3`.

- [ ] **F-VAL-02**: `test_konstanta_retry_error_codes`
  - **Assert**: `RETRY_ERROR_CODES == (2006, 2013)`.
  - **Assert**: `2006 in RETRY_ERROR_CODES`.
  - **Assert**: `2013 in RETRY_ERROR_CODES`.

- [ ] **F-VAL-03**: `test_result_namedtuple_fields`
  - **Assert**: `Result._fields == ('is_success', 'data', 'error_msg')`.
  - Buat instance `Result(True, 'data', None)` dan `Result(False, None, 'error')`.
  - **Assert**: Kedua instance memiliki field yang benar.

- [ ] **F-VAL-04**: `test_konstanta_retry_base_seconds`
  - **Assert**: `RETRY_BASE_SECONDS == 2`.

- [ ] **F-VAL-05**: `test_konstanta_pool_exhausted_error_code`
  - **Assert**: `POOL_EXHAUSTED_ERROR_CODE == -1`.

- [ ] **F-VAL-06**: `test_initial_connection_pool_is_none`
  - Import ulang modul dan periksa.
  - **Assert**: setelah reset fixture, `db_mod._connection_pool is None`.

---

## 7. Ringkasan Total Skenario Test

| Grup | Fungsi Target | Positif | Negatif | Edge Case/Validasi | Total |
|------|--------------|---------|---------|-------------------|-------|
| **A** | `create_connection_pool()` | 3 | 4 | 2 | **9** |
| **B** | `get_db_connection()` | 4 | 5 | 5 | **14** |
| **C** | `close_connection_pool()` | 2 | 1 | 2 | **5** |
| **D** | `get_root_connection()` | 2 | 3 | 1 | **6** |
| **E** | `get_pool_status()` | 2 | 1 | 1 | **4** |
| **F** | Konstanta & Struktur | 0 | 0 | 6 | **6** |
| **TOTAL** | | **13** | **14** | **17** | **44** |

---

## 8. Checklist Tahapan Pengerjaan (Low-Level Step-by-Step)

### Fase 1: Persiapan dan Pembacaan Referensi

- [ ] **1.1** Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — Ekstrak aturan penamaan test (Bab 14.3), konvensi FP (Bab 2.2), Result Pattern (Bab 2.2.6), connection pooling & retry (Bab 8.9, 9.5, 9.6).
- [ ] **1.2** Baca file `docs/sdlc/05_testing/01_test_plan.md` — Ekstrak strategi unit testing (Bab 3.1.1), tools (Bab 11.3), skenario connection pooling (Bab 7.1), kode error (Bab 12.4).
- [ ] **1.3** Baca file `db/db_connector.py` — Pahami 100% implementasi setiap fungsi publik (5 fungsi), konstanta (4 konstanta), dan variabel modul-level (`_connection_pool`).
- [ ] **1.4** Baca file `tests/test_unit_db_connector.py` yang sudah ada — Catat skenario apa saja yang sudah tercakup dan mana yang belum.
- [ ] **1.5** Baca file `db/__init__.py` — Pastikan fungsi yang di-export sesuai.
- [ ] **1.6** Baca file `requirements.txt` — Konfirmasi `pytest==8.2.0` dan `coverage==7.5.1` sudah tersedia.

### Fase 2: Analisis Gap (Skenario yang Belum Tercakup)

- [ ] **2.1** Bandingkan daftar 44 skenario test di Bab 6 issue ini dengan skenario yang sudah ada di `tests/test_unit_db_connector.py`.
- [ ] **2.2** Identifikasi skenario yang **sudah tercakup** dan tandai sebagai `[x]`.
- [ ] **2.3** Identifikasi skenario yang **belum tercakup** dan buat daftar prioritas penambahan.
- [ ] **2.4** Pastikan semua skenario dari Bab 6 tercakup — tidak ada yang terlewat.

### Fase 3: Penulisan / Pembaruan Kode Test

- [ ] **3.1** Buka file `tests/test_unit_db_connector.py`.
- [ ] **3.2** Pastikan header file sesuai konvensi (Bab 5.3).
- [ ] **3.3** Pastikan import sesuai urutan (Bab 5.4).
- [ ] **3.4** Pastikan fixture `reset_connection_pool` dengan `autouse=True` ada dan benar (Bab 5.6).
- [ ] **3.5** Pastikan helper `_make_mysql_error` ada dan berfungsi benar.
- [ ] **3.6** Tulis/perbaiki skenario **Grup A** (create_connection_pool) — 9 test cases.
- [ ] **3.7** Tulis/perbaiki skenario **Grup B** (get_db_connection) — 14 test cases.
- [ ] **3.8** Tulis/perbaiki skenario **Grup C** (close_connection_pool) — 5 test cases.
- [ ] **3.9** Tulis/perbaiki skenario **Grup D** (get_root_connection) — 6 test cases.
- [ ] **3.10** Tulis/perbaiki skenario **Grup E** (get_pool_status) — 4 test cases.
- [ ] **3.11** Tulis/perbaiki skenario **Grup F** (Konstanta & Struktur) — 6 test cases.
- [ ] **3.12** Pastikan setiap fungsi test memiliki docstring PEP 257 lengkap.
- [ ] **3.13** Pastikan setiap fungsi test memiliki type hint return `-> None`.
- [ ] **3.14** Pastikan **TIDAK ADA** fungsi test dengan body `pass`, `TODO`, atau placeholder.

### Fase 4: Verifikasi dan Validasi

- [ ] **4.1** Jalankan seluruh test suite:
  ```bash
  python -m pytest tests/test_unit_db_connector.py -v --tb=short
  ```
- [ ] **4.2** Pastikan **SEMUA** test PASS (0 FAIL, 0 ERROR).
- [ ] **4.3** Jalankan pengukuran code coverage:
  ```bash
  python -m coverage run --source=db/db_connector -m pytest tests/test_unit_db_connector.py -v
  python -m coverage report -m
  ```
- [ ] **4.4** Pastikan coverage modul `db/db_connector.py` **≥ 90%**.
- [ ] **4.5** Jika coverage < 90%, identifikasi baris yang belum tercakup dan tambahkan test.
- [ ] **4.6** Jalankan ulang test untuk memastikan tidak ada regresi:
  ```bash
  python -m pytest tests/test_unit_db_connector.py -v --tb=short
  ```
- [ ] **4.7** Pastikan tidak ada test yang **skip**, **xfail**, atau **deselected** tanpa justifikasi.

### Fase 5: Validasi Akhir Kualitas

- [ ] **5.1** Review kembali setiap fungsi test — apakah docstring sudah lengkap?
- [ ] **5.2** Review kembali — apakah setiap assertion bermakna dan memverifikasi behavior yang benar?
- [ ] **5.3** Review kembali — apakah pola AAA (Arrange-Act-Assert) diikuti konsisten?
- [ ] **5.4** Review kembali — apakah tidak ada hardcoded value yang seharusnya dinamis?
- [ ] **5.5** Review kembali — apakah mock `time.sleep` digunakan di semua test retry (agar test tidak lambat)?
- [ ] **5.6** Review kembali — apakah fixture clean state (`reset_connection_pool`) berjalan benar?
- [ ] **5.7** Pastikan file test yang dihasilkan **HANYA** `tests/test_unit_db_connector.py`.
- [ ] **5.8** Pastikan **TIDAK ADA** file lain yang termodifikasi.

---

## 9. Contoh Implementasi Skenario Test Baru

Berikut contoh implementasi untuk skenario yang mungkin belum ada di file test existing. Gunakan ini sebagai template:

### Contoh A-NEG-03: Host Invalid

```python
@patch('db.db_connector.pooling.MySQLConnectionPool')
def test_create_connection_pool_gagal_host_invalid(mock_pool_cls) -> None:
    """Memverifikasi kegagalan pembuatan pool karena host MySQL tidak dikenali.

    Skenario: Negatif
    Target: create_connection_pool
    """
    # Arrange
    mysql_err = _make_mysql_error(2005, "Unknown MySQL server host")
    mock_pool_cls.side_effect = mysql_err

    # Act
    res = create_connection_pool(
        host='server.tidak.ada',
        port=3306,
        user='app',
        password='pass',
        database='db'
    )

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert '2005' in res.error_msg
    assert db_mod._connection_pool is None
```

### Contoh B-EDGE-05: Max Retries Kustom 5

```python
@patch('db.db_connector.time.sleep')
def test_get_db_connection_max_retries_5_custom(mock_sleep) -> None:
    """Memverifikasi retry dengan max_retries kustom 5, sukses di attempt ke-5.

    Skenario: Edge Case
    Target: get_db_connection
    """
    # Arrange
    mock_pool = MagicMock()
    mysql_err = _make_mysql_error(2006, "Server gone")
    mock_conn = MagicMock(spec=mysql.connector.MySQLConnection)
    mock_pool.get_connection.side_effect = [mysql_err] * 4 + [mock_conn]
    db_mod._connection_pool = mock_pool

    # Act
    res = get_db_connection(max_retries=5)

    # Assert
    assert res.is_success is True
    assert res.data is mock_conn
    assert mock_pool.get_connection.call_count == 5
    assert mock_sleep.call_count == 4
    # Interval: 2^1=2, 2^2=4, 2^3=8, 2^4=16
    mock_sleep.assert_any_call(2)
    mock_sleep.assert_any_call(4)
    mock_sleep.assert_any_call(8)
    mock_sleep.assert_any_call(16)
```

### Contoh C-EDGE-02: Idempotent Close

```python
def test_close_connection_pool_idempotent_panggilan_berulang() -> None:
    """Memverifikasi close_connection_pool bersifat idempotent (aman dipanggil berulang).

    Skenario: Edge Case
    Target: close_connection_pool
    """
    # Arrange
    mock_pool = MagicMock()
    db_mod._connection_pool = mock_pool

    # Act — panggilan pertama
    res1 = close_connection_pool()

    # Assert — panggilan pertama sukses
    assert res1.is_success is True
    assert db_mod._connection_pool is None

    # Act — panggilan kedua (pool sudah None)
    res2 = close_connection_pool()

    # Assert — panggilan kedua tetap sukses
    assert res2.is_success is True
    assert res2.error_msg is None
```

### Contoh E-NEG-01: Pool Status Exception

```python
def test_get_pool_status_gagal_exception() -> None:
    """Memverifikasi penanganan error saat membaca pool_name melempar exception.

    Skenario: Negatif
    Target: get_pool_status
    """
    # Arrange
    mock_pool = MagicMock()
    type(mock_pool).pool_name = PropertyMock(side_effect=Exception("Pool corrupted"))
    db_mod._connection_pool = mock_pool

    # Act
    res = get_pool_status()

    # Assert
    assert res.is_success is False
    assert res.data is None
    assert 'ERR-DB-001' in res.error_msg
    assert 'Pool corrupted' in res.error_msg
```

---

## 10. Perintah Eksekusi dan Verifikasi

### 10.1. Menjalankan Semua Test

```bash
# Dari root project (abucom/)
python -m pytest tests/test_unit_db_connector.py -v --tb=short
```

### 10.2. Menjalankan Test Spesifik

```bash
# Contoh menjalankan 1 test spesifik
python -m pytest tests/test_unit_db_connector.py::test_get_db_connection_retry_sukses_setelah_error_2006 -v
```

### 10.3. Mengukur Code Coverage

```bash
# Generate coverage report
python -m coverage run --source=db/db_connector -m pytest tests/test_unit_db_connector.py -v
python -m coverage report -m

# Target: db/db_connector.py harus ≥ 90%
```

### 10.4. Coverage dengan HTML Report (Opsional)

```bash
python -m coverage html
# Buka htmlcov/index.html di browser
```

---

## 11. Kriteria Selesai (Definition of Done)

Issue ini dianggap **SELESAI** jika dan hanya jika seluruh kriteria berikut terpenuhi:

- [ ] **11.1** File `tests/test_unit_db_connector.py` berisi minimal **44 fungsi test** yang mencakup seluruh skenario di Bab 6.
- [ ] **11.2** Seluruh **44 test PASS** tanpa ada FAIL atau ERROR.
- [ ] **11.3** Code coverage modul `db/db_connector.py` **≥ 90%** (diukur via `coverage.py`).
- [ ] **11.4** Setiap fungsi test memiliki docstring PEP 257 lengkap.
- [ ] **11.5** Setiap fungsi test mengikuti pola AAA (Arrange-Act-Assert).
- [ ] **11.6** Fixture `reset_connection_pool` (autouse) memastikan clean state sebelum dan sesudah setiap test.
- [ ] **11.7** `time.sleep` di-mock di semua test yang melibatkan retry (agar test cepat).
- [ ] **11.8** **TIDAK ADA** koneksi fisik ke database MySQL di seluruh test.
- [ ] **11.9** **TIDAK ADA** file lain yang termodifikasi selain `tests/test_unit_db_connector.py`.
- [ ] **11.10** **TIDAK ADA** fungsi test dengan body `pass`, `TODO`, atau placeholder.
- [ ] **11.11** Header file, import order, dan konvensi penamaan sesuai Coding Standard AbuCom.

---

## 12. Referensi Dokumen SDLC

| No | Dokumen | Path Relatif |
|----|---------|-------------|
| 1 | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` |
| 2 | Test Plan v1.2 | `docs/sdlc/05_testing/01_test_plan.md` |
| 3 | Test Cases v1.2 | `docs/sdlc/05_testing/02_test_cases.md` |
| 4 | Module Structure v1.2 | `docs/sdlc/04_implementation/03_module_structure.md` |
| 5 | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` |
| 6 | Source Code Target | `db/db_connector.py` |
| 7 | Existing Test File | `tests/test_unit_db_connector.py` |
| 8 | Dependencies | `requirements.txt` |
