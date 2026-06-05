# Issue — Unit Test Feature: Validasi Kelengkapan Environment Variables

---
**proyek**     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
**tipe**       : Unit Testing — Feature Validasi Kelengkapan Environment Variables
**prioritas**  : High
**status**     : Open
**tanggal**    : 2026-06-05
**target file** : `tests/test_settings.py`
**modul target**: `config/settings.py`
**assignee**   : Junior Programmer / LLM AI Agent (Model Kecil/Murah)

---

## 0. Persona Pelaksana

**Kamu adalah `Senior QA Engineer & Python Unit Test Specialist`.**

Kamu memiliki keahlian mendalam dalam:
- Merancang dan mengimplementasikan unit test terisolasi penuh (mocked) menggunakan framework `pytest`.
- Memahami paradigma **Functional Programming (FP) murni** tanpa class di alur bisnis.
- Menguasai teknik mocking (`unittest.mock.patch`, `MagicMock`, `monkeypatch`) untuk mengisolasi dependensi I/O (file system, environment variables, library pihak ketiga).
- Memahami standar pengujian **deterministic**, **repeatable**, dan **clean state** untuk setiap skenario test.
- Memvalidasi kode terhadap standar keamanan `.env` (kunci JWT, Fernet, password strength) sesuai dokumen SDLC AbuCom.
- Menulis test function dengan konvensi penamaan `test_<behavior_spesifik>()` menggunakan format **Arrange-Act-Assert (AAA)**.
- Mengukur code coverage menggunakan `coverage.py` dengan target minimum **≥ 90%** pada logika bisnis inti.

Kamu bertanggung jawab penuh atas kelengkapan, kebenaran, dan isolasi seluruh unit test yang ditulis.

---

## 1. Dokumen Referensi Utama (Wajib Dibaca)

Sebelum memulai pengerjaan, **WAJIB** baca dan ekstrak seluruh detail yang relevan dari dokumen-dokumen SDLC berikut:

| No | Dokumen Referensi | Path Relatif | Prioritas | Alasan Relevansi |
|:---:|---|---|:---:|---|
| 1 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | **PRIMER** | Konvensi penamaan test file (`test_<modul>.py`), test function (`test_<behavior>()`), aturan unit testing pure functions, target code coverage ≥ 90%, larangan koneksi DB riil, Result pattern, type hints PEP 484, docstring PEP 257 Google Style, aturan import ordering. |
| 2 | **Environment Setup v1.2** | `docs/sdlc/04_implementation/02_environment_setup.md` | **PRIMER** | Template `.env.example` lengkap (14 variabel), struktur `AppConfig` NamedTuple, casting numerik, generasi JWT/Fernet key, connection pool config, validasi startup smoke test. |
| 3 | **Test Plan v1.2** | `docs/sdlc/05_testing/01_test_plan.md` | **PRIMER** | Strategi unit testing (Bab 3.1.1), pendekatan white-box testing, target coverage ≥ 90%, framework `pytest`, `coverage.py`, skenario pengujian terisolasi mock data. |
| 4 | **Module Structure v1.2** | `docs/sdlc/04_implementation/03_module_structure.md` | **SEKUNDER** | Spesifikasi file `config/settings.py` (Bab 8.2), daftar variabel dikelola, SRS-F-ADD-01 (Startup validation). |
| 5 | **Test Cases v1.2** | `docs/sdlc/05_testing/02_test_cases.md` | **SEKUNDER** | Format penulisan test case standar AbuCom, konvensi ID naming, entry/exit criteria. |

### 1.1. Rangkuman Detail dari Dokumen Referensi

Berikut adalah **seluruh detail teknis** yang telah diekstrak dari dokumen referensi di atas yang **spesifik dan relevan** untuk pengerjaan issue ini:

#### A. Dari Coding Standard (01_coding_standard.md)

- **Bab 14.1**: Framework testing wajib menggunakan `pytest` (atau `unittest`).
- **Bab 14.2**: Target code coverage ≥ 90% untuk logika bisnis inti di `logic/` (berlaku juga untuk `config/settings.py` sebagai modul kritis startup).
- **Bab 14.3**: Konvensi penamaan:
  - File test: `test_<modul_target>.py` → `test_settings.py`
  - Fungsi test: `test_<behavior_spesifik>()` → contoh: `test_load_settings_gagal_file_env_tidak_ditemukan()`
- **Bab 14.4**: Unit testing pure functions **WAJIB** bersifat deterministik, terisolasi penuh, dan **DILARANG** melakukan koneksi fisik database MySQL atau file system. Data uji disuplai melalui mock.
- **Bab 2.2.6**: Pola Result/Either pattern → `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])`.
- **Bab 3.2**: Fungsi menggunakan format `snake_case` (verb_noun).
- **Bab 5.4**: Urutan import: Standard Library → Third-Party → Local Modules.
- **Bab 5.5**: Single quote untuk string internal, double quote untuk docstring dan teks display.
- **Bab 6.2**: Docstring wajib format PEP 257 Google Style (Args/Returns/Raises).
- **Bab 7.2**: Type hints Python 3.14+ → gunakan `list[...]`, `dict[...]`, `str | None` (bukan `Optional`).
- **Bab 10.1**: Variabel `.env` wajib dicek kelengkapan saat startup. Jika file tidak ada → `ERR-FILE-001`. Jika variabel wajib kosong → `ERR-FILE-002`.
- **Bab 11.5**: Katalog error codes:
  - `ERR-FILE-001`: File .env tidak ditemukan.
  - `ERR-FILE-002`: Variabel wajib belum diisi.
  - `ERR-FILE-003`: Nilai variabel bukan integer valid.
  - `ERR-FILE-004`: Nilai variabel di luar rentang.
  - `ERR-FILE-005`: APP_ENV tidak valid.
  - `ERR-FILE-006`: JWT_SECRET_KEY terlalu pendek (production).
  - `ERR-FILE-007`: FERNET_KEY bukan kunci valid.
  - `ERR-FILE-008`: DB_HOST bukan IP/hostname valid.
- **Bab 15.3**: Commit message format: `test: <deskripsi singkat>`.

#### B. Dari Environment Setup (02_environment_setup.md)

- **Bab 8.1**: Struktur direktori standar → test file di `tests/test_settings.py`.
- **Bab 8.2.1**: Template `.env.example` berisi **14 variabel**:
  1. `APP_ENV` — `'production'` atau `'development'` (default: `'production'`).
  2. `APP_CABANG_ID` — Integer positif > 0 (default: `1`).
  3. `DB_HOST` — IP address atau hostname valid (default: `'10.10.10.10'`).
  4. `DB_PORT` — Integer rentang 1-65535 (default: `3306`).
  5. `DB_USER` — String non-kosong (default: `'abucom_app'`).
  6. `DB_PASSWORD` — **WAJIB** diisi, tidak boleh kosong atau placeholder `YOUR_*`.
  7. `DB_NAME` — String non-kosong (default: `'abucom_db'`).
  8. `DB_POOL_SIZE` — Integer rentang 1-100 (default: `5`).
  9. `JWT_SECRET_KEY` — **WAJIB** diisi, minimum 32 karakter di production.
  10. `JWT_LIFETIME_SECONDS` — Integer positif > 0 (default: `28800`).
  11. `FERNET_KEY` — **WAJIB** diisi, harus kunci Fernet base64 yang valid.
  12. `BACKUP_ZIP_PASSWORD` — **WAJIB** diisi, minimum 8 karakter di production.
  13. `PRINTER_PORT` — String non-kosong (default: `'COM1'`).
  14. `PRINTER_WIDTH_MM` — Integer, hanya `58` atau `80` valid (default: `58`).
- **Bab 8.4**: Standar presisi desimal `ROUND_HALF_UP` ke 4 digit (tidak relevan langsung, tapi untuk konsistensi casting).
- **Bab 8.7**: Connection pool inisialisasi menggunakan variabel dari `.env`.

#### C. Dari Test Plan (01_test_plan.md)

- **Bab 3.1.1**: Unit testing → cakupan fungsi logika bisnis murni (pure functions) terbebas dari efek samping I/O. Pendekatan deterministik menggunakan mock data structures (NamedTuple/Tuples).
- **Bab 3.3**: White-Box Testing untuk unit testing → memverifikasi jalur logika internal (control flow), penanganan exception handling, dan coverage persentase.
- **Bab 10.2**: Dependensi pengembangan: `pytest==8.2.0`, `coverage==7.5.1`.
- **Bab 2.1**: Modul Tambahan (Additional) mencantumkan: **Startup validation .env** sebagai fitur yang diuji (in-scope).

#### D. Konstanta dan Struktur Data di `config/settings.py`

Berikut adalah data konstanta dan struktur yang harus diuji (diekstrak dari source code `config/settings.py`):

```python
# Konstanta default
DEFAULT_DB_HOST = '10.10.10.10'
DEFAULT_DB_PORT = 3306
DEFAULT_DB_POOL_SIZE = 5
DEFAULT_JWT_LIFETIME = 28800
DEFAULT_PRINTER_WIDTH = 58

# Konstanta validasi
VALID_APP_ENVS = ('development', 'production')
VALID_PRINTER_WIDTHS = (58, 80)
REQUIRED_ENV_VARS = ('DB_PASSWORD', 'JWT_SECRET_KEY', 'FERNET_KEY', 'BACKUP_ZIP_PASSWORD')
MIN_JWT_KEY_LENGTH = 32
MIN_BACKUP_PASSWORD_LENGTH = 8

# NamedTuple imutabel (14 field)
AppConfig = namedtuple('AppConfig', [
    'app_env', 'app_cabang_id', 'db_host', 'db_port', 'db_user',
    'db_password', 'db_name', 'db_pool_size', 'jwt_secret_key',
    'jwt_lifetime_seconds', 'fernet_key', 'backup_zip_password',
    'printer_port', 'printer_width_mm',
])
```

Fungsi-fungsi yang harus di-cover oleh unit test:

| No | Fungsi | Akses | Deskripsi |
|:---:|---|:---:|---|
| 1 | `_validate_fernet_key(fernet_key)` | Private | Memvalidasi string Fernet key valid/tidak. |
| 2 | `_validate_jwt_key_strength(jwt_key, app_env)` | Private | Memvalidasi panjang JWT key ≥ 32 karakter. Warning di dev, error di prod. |
| 3 | `_validate_db_host(db_host)` | Private | Memvalidasi format IP address atau hostname RFC 1123. |
| 4 | `_safe_int_cast(value, default, var_name, errors)` | Private | Casting string ke integer aman dengan fallback default. |
| 5 | `_validate_int_range(value, min_val, max_val, var_name, errors)` | Private | Memvalidasi integer berada dalam rentang min-max. |
| 6 | `load_settings()` | Public | Fungsi utama: memuat, memvalidasi, dan meng-cast seluruh variabel konfigurasi dari `.env`. |

---

## 2. Batasan dan Cakupan Pengerjaan

### 2.1. Cakupan (In-Scope)
- [x] Menulis unit test **terisolasi penuh** (mocked) untuk modul `config/settings.py`.
- [x] Menguji **semua 6 fungsi** yang tercantum di tabel fungsi di atas.
- [x] Menguji **semua 14 variabel** environment beserta validasinya.
- [x] Menguji **semua jalur logika**: happy path, unhappy path, edge cases, boundary values.
- [x] Memastikan clean state sebelum setiap test (fixture `autouse`).
- [x] Memastikan isolasi penuh dari file system dan environment variables riil.

### 2.2. Di Luar Cakupan (Out-of-Scope)
- ❌ **DILARANG** mengubah atau memodifikasi kode source `config/settings.py`.
- ❌ **DILARANG** mengubah atau memodifikasi file lain di luar `tests/test_settings.py`.
- ❌ **DILARANG** melakukan koneksi fisik ke database MySQL.
- ❌ **DILARANG** membaca file `.env` riil dari file system.
- ❌ **DILARANG** menginstal dependency baru di luar `requirements.txt`.
- ❌ **DILARANG** menulis integration test (cakupan issue ini hanya unit test mocked).

### 2.3. Prinsip Isolasi
- Setiap test function **WAJIB** bersifat **deterministik** dan **repeatable** — hasil yang sama setiap kali dijalankan.
- Gunakan `@patch()` dari `unittest.mock` untuk mock:
  - `config.settings.Path.exists` → kontrol keberadaan file `.env`.
  - `config.settings.load_dotenv` → cegah pembacaan file `.env` riil.
  - `config.settings.os.getenv` → kontrol penuh nilai environment variables.
- Gunakan `monkeypatch.delenv()` melalui fixture `autouse` untuk membersihkan env vars sebelum tiap test.
- Gunakan fungsi helper `_make_valid_env()` untuk membuat dictionary env vars valid sebagai baseline.
- Gunakan fungsi helper `_mock_getenv_from_dict()` untuk membuat side_effect mock `os.getenv`.

---

## 3. Alur Pengerjaan (Step-by-Step)

### Tahap 1: Persiapan Sistem dan Pembacaan Referensi

- [ ] **1.1.** Baca dan pahami dokumen referensi utama berikut secara lengkap:
  - [ ] `docs/sdlc/04_implementation/01_coding_standard.md` — Bab 14 (Testing), Bab 2 (FP), Bab 3 (Naming), Bab 5-7 (Style, Docstring, Type Hints), Bab 10.1 (Secure Coding `.env`), Bab 11.5 (Error Codes).
  - [ ] `docs/sdlc/04_implementation/02_environment_setup.md` — Bab 8.2 (Template `.env.example`), Bab 8.1 (Struktur Direktori).
  - [ ] `docs/sdlc/05_testing/01_test_plan.md` — Bab 3.1.1 (Unit Testing), Bab 3.3 (White-Box), Bab 10.2 (Dependensi Testing).
- [ ] **1.2.** Baca dan pahami **seluruh** source code target modul:
  - [ ] `config/settings.py` — Pahami setiap fungsi, konstanta, alur validasi, dan error handling.
- [ ] **1.3.** Baca file `.env.example` untuk memahami template variabel.
- [ ] **1.4.** Baca file `requirements.txt` untuk memastikan `pytest==8.2.0` dan `coverage==7.5.1` tersedia.
- [ ] **1.5.** Baca file `tests/test_settings.py` yang **sudah ada** untuk memahami:
  - Pola mock dan fixture yang sudah digunakan.
  - Test cases yang **sudah ditulis** agar **tidak duplikat**.
  - Struktur pengelompokan GRUP (A-K) yang sudah ada.

### Tahap 2: Analisis Test Coverage Gap

- [ ] **2.1.** Jalankan test yang sudah ada untuk memastikan semuanya PASS:
  ```bash
  python -m pytest tests/test_settings.py -v
  ```
- [ ] **2.2.** Jalankan coverage report untuk mengidentifikasi baris kode yang **belum ter-cover**:
  ```bash
  python -m coverage run -m pytest tests/test_settings.py -v
  python -m coverage report -m --include=config/settings.py
  ```
- [ ] **2.3.** Catat nomor baris yang `Missing` dari coverage report.
- [ ] **2.4.** Identifikasi skenario test yang belum ada berdasarkan daftar skenario di **Bab 4** dokumen ini.

### Tahap 3: Implementasi Unit Test

- [ ] **3.1.** Buka file `tests/test_settings.py`.
- [ ] **3.2.** Tambahkan test baru **di bagian bawah file** (setelah GRUP K yang sudah ada), dalam GRUP baru bernama **GRUP L** dan seterusnya.
- [ ] **3.3.** Pastikan setiap test function baru mengikuti konvensi:
  - Nama: `test_<behavior_spesifik>()` menggunakan bahasa Indonesia deskriptif.
  - Docstring: Format PEP 257 Google Style dengan field `Tipe:` dan `Target:`.
  - Pola: **Arrange-Act-Assert (AAA)** dengan komentar pemisah.
  - Type hints: Return type `-> None`.
  - Decorator: `@patch(...)` untuk mock dependensi.
- [ ] **3.4.** Implementasikan **seluruh skenario test** dari Bab 4 yang belum ada di file existing.
- [ ] **3.5.** Pastikan **tidak ada** fungsi test yang menggantung (TODO/pass/placeholder). Setiap test harus complete dan executable.

### Tahap 4: Verifikasi dan Validasi

- [ ] **4.1.** Jalankan seluruh test suite dan pastikan **100% PASS**:
  ```bash
  python -m pytest tests/test_settings.py -v --tb=short
  ```
- [ ] **4.2.** Jalankan coverage report dan pastikan coverage `config/settings.py` mencapai **≥ 90%**:
  ```bash
  python -m coverage run -m pytest tests/test_settings.py -v
  python -m coverage report -m --include=config/settings.py
  ```
- [ ] **4.3.** Pastikan **tidak ada** test yang bersifat flaky (hasil berubah-ubah tiap run).
- [ ] **4.4.** Pastikan **tidak ada** test yang melakukan I/O riil (baca file `.env`, koneksi DB, akses network).
- [ ] **4.5.** Pastikan **tidak ada** test baru yang menyebabkan test lama gagal (regresi).
- [ ] **4.6.** Commit dengan pesan: `test: penambahan unit test validasi kelengkapan environment variables config/settings.py`

---

## 4. Daftar Skenario Test Lengkap

Berikut adalah **daftar lengkap skenario test** yang **WAJIB** ada di `tests/test_settings.py`. Periksa apakah masing-masing sudah ada di file existing. Jika **sudah ada**, tandai ✅ dan **jangan duplikat**. Jika **belum ada**, implementasikan.

> **PENTING**: Setiap test function WAJIB memulai dari **clean state** — fixture `autouse` `clean_env` yang sudah ada akan menghapus semua env vars sebelum tiap test. Jangan hapus atau modifikasi fixture ini.

---

### GRUP A: Validasi Konstanta dan Struktur Data (Validasi Input)

| No | Nama Skenario | Tipe | Deskripsi |
|:---:|---|:---:|---|
| A-01 | `test_required_env_vars_berisi_empat_variabel_wajib` | Validasi | Memastikan `REQUIRED_ENV_VARS` berisi tepat 4 variabel: `DB_PASSWORD`, `JWT_SECRET_KEY`, `FERNET_KEY`, `BACKUP_ZIP_PASSWORD`. |
| A-02 | `test_valid_app_envs_berisi_development_dan_production` | Validasi | Memastikan `VALID_APP_ENVS` berisi tepat `('development', 'production')`. |
| A-03 | `test_valid_printer_widths_berisi_58_dan_80` | Validasi | Memastikan `VALID_PRINTER_WIDTHS` berisi tepat `(58, 80)`. |
| A-04 | `test_default_konstanta_memiliki_nilai_yang_benar` | Validasi | Memastikan `DEFAULT_DB_HOST`, `DEFAULT_DB_PORT`, `DEFAULT_DB_POOL_SIZE`, `DEFAULT_JWT_LIFETIME`, `DEFAULT_PRINTER_WIDTH` sesuai spesifikasi. |
| A-05 | `test_appconfig_memiliki_14_field_yang_benar` | Validasi | Memastikan `AppConfig._fields` berisi tepat 14 field sesuai urutan. |
| A-06 | `test_appconfig_bersifat_imutabel` | Validasi | Memastikan `AppConfig` menolak mutasi atribut (`AttributeError`). |
| A-07 | `test_min_jwt_key_length_bernilai_32` | Validasi | Memastikan konstanta `MIN_JWT_KEY_LENGTH == 32`. |
| A-08 | `test_min_backup_password_length_bernilai_8` | Validasi | Memastikan konstanta `MIN_BACKUP_PASSWORD_LENGTH == 8`. |

---

### GRUP B: Test `_safe_int_cast()` (Skenario Positif, Negatif, Edge Case)

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| B-01 | `test_safe_int_cast_sukses_string_integer_valid` | Positif | Input `'123'`. | Return `123`. |
| B-02 | `test_safe_int_cast_sukses_return_default_saat_none` | Positif | Input `None`, default `42`. | Return `42`. |
| B-03 | `test_safe_int_cast_sukses_string_negatif` | Positif | Input `'-5'`. | Return `-5`. |
| B-04 | `test_safe_int_cast_sukses_string_nol` | Positif | Input `'0'`. | Return `0`. |
| B-05 | `test_safe_int_cast_sukses_string_besar` | Positif | Input `'999999'`. | Return `999999`. |
| B-06 | `test_safe_int_cast_gagal_string_bukan_angka` | Negatif | Input `'abc'`. | `SystemExit(1)`. |
| B-07 | `test_safe_int_cast_gagal_string_float` | Negatif | Input `'3.14'`. | `SystemExit(1)`. |
| B-08 | `test_safe_int_cast_gagal_string_kosong` | Negatif | Input `''`. | `SystemExit(1)`. |
| B-09 | `test_safe_int_cast_gagal_string_spasi` | Edge Case | Input `'  '`. | `SystemExit(1)`. |
| B-10 | `test_safe_int_cast_gagal_string_campuran` | Edge Case | Input `'12abc'`. | `SystemExit(1)`. |
| B-11 | `test_safe_int_cast_dengan_errors_list_mengumpulkan_error` | Positif | Input `'abc'` dengan `errors=[]`. | Error ditambahkan ke list, return default, **tidak** `SystemExit`. |
| B-12 | `test_safe_int_cast_dengan_errors_list_sukses_tidak_menambah` | Positif | Input `'10'` dengan `errors=[]`. | `errors` tetap kosong, return `10`. |

---

### GRUP C: Test `_validate_int_range()` (Skenario Positif, Negatif, Edge Case)

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| C-01 | `test_validate_int_range_sukses_nilai_di_tengah_rentang` | Positif | `50` dalam rentang `1-100`. | Return `50`. |
| C-02 | `test_validate_int_range_sukses_nilai_sama_dengan_batas_bawah` | Boundary | `1` dalam rentang `1-100`. | Return `1`. |
| C-03 | `test_validate_int_range_sukses_nilai_sama_dengan_batas_atas` | Boundary | `100` dalam rentang `1-100`. | Return `100`. |
| C-04 | `test_validate_int_range_gagal_nilai_di_bawah_batas_minimum` | Negatif | `0` dalam rentang `1-100`. | `SystemExit(1)`. |
| C-05 | `test_validate_int_range_gagal_nilai_di_atas_batas_maksimum` | Negatif | `101` dalam rentang `1-100`. | `SystemExit(1)`. |
| C-06 | `test_validate_int_range_gagal_nilai_negatif` | Negatif | `-10` dalam rentang `1-65535`. | `SystemExit(1)`. |
| C-07 | `test_validate_int_range_sukses_nilai_batas_port_65535` | Boundary | `65535` dalam rentang `1-65535`. | Return `65535`. |
| C-08 | `test_validate_int_range_dengan_errors_list_mengumpulkan_error` | Positif | `0` dalam rentang `1-100` dengan `errors=[]`. | Error ditambahkan ke list, **tidak** `SystemExit`. |
| C-09 | `test_validate_int_range_dengan_errors_list_sukses_tidak_menambah` | Positif | `50` dalam rentang `1-100` dengan `errors=[]`. | `errors` tetap kosong. |

---

### GRUP D: Test `_validate_fernet_key()` (Skenario Positif, Negatif, Edge Case)

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| D-01 | `test_validate_fernet_key_format_valid` | Positif | Gunakan `Fernet.generate_key()` yang valid. | Return `True`. |
| D-02 | `test_validate_fernet_key_format_tidak_valid` | Negatif | Input `'kunci_tidak_valid_123'`. | Return `False`. |
| D-03 | `test_validate_fernet_key_string_kosong` | Edge Case | Input `''`. | Return `False`. |
| D-04 | `test_validate_fernet_key_string_base64_bukan_fernet` | Edge Case | Input string base64 valid tapi bukan Fernet key (misal `'dGVzdDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5'`). | Return `False`. |
| D-05 | `test_validate_fernet_key_string_acak_panjang` | Edge Case | Input string acak 44 karakter non-base64. | Return `False`. |

---

### GRUP E: Test `_validate_jwt_key_strength()` (Skenario Positif, Negatif, Edge Case)

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| E-01 | `test_validate_jwt_key_strength_valid_panjang_64_karakter` | Positif | Key 64 karakter hex, `app_env='production'`. | Return `None` (no error). |
| E-02 | `test_validate_jwt_key_strength_valid_tepat_32_karakter` | Boundary | Key tepat 32 karakter, `app_env='production'`. | Return `None`. |
| E-03 | `test_validate_jwt_key_strength_pendek_di_development` | Positif | Key 10 karakter, `app_env='development'`. | Return `None` (warning only, no error). |
| E-04 | `test_validate_jwt_key_strength_pendek_di_production` | Negatif | Key 10 karakter, `app_env='production'`. | Return string error `ERR-FILE-006`. |
| E-05 | `test_validate_jwt_key_strength_31_karakter_di_production` | Boundary | Key 31 karakter (satu kurang dari minimum), `app_env='production'`. | Return string error `ERR-FILE-006`. |
| E-06 | `test_validate_jwt_key_strength_1_karakter_di_production` | Edge Case | Key 1 karakter, `app_env='production'`. | Return string error `ERR-FILE-006`. |

---

### GRUP F: Test `_validate_db_host()` (Skenario Positif, Negatif, Edge Case)

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| F-01 | `test_validate_db_host_valid_ip_standar` | Positif | Input `'192.168.1.200'`. | Return `True`. |
| F-02 | `test_validate_db_host_valid_ip_localhost` | Positif | Input `'127.0.0.1'`. | Return `True`. |
| F-03 | `test_validate_db_host_valid_hostname_localhost` | Positif | Input `'localhost'`. | Return `True`. |
| F-04 | `test_validate_db_host_valid_hostname_fqdn` | Positif | Input `'db.abucom.local'`. | Return `True`. |
| F-05 | `test_validate_db_host_valid_ip_batas_atas` | Boundary | Input `'255.255.255.255'`. | Return `True`. |
| F-06 | `test_validate_db_host_valid_ip_batas_bawah` | Boundary | Input `'0.0.0.0'`. | Return `True`. |
| F-07 | `test_validate_db_host_invalid_string_kosong` | Negatif | Input `''`. | Return `False`. |
| F-08 | `test_validate_db_host_invalid_ip_oktet_256` | Negatif | Input `'256.300.1.1'`. | Return `False`. |
| F-09 | `test_validate_db_host_invalid_karakter_khusus` | Negatif | Input `'invalid_host#name'`. | Return `False`. |
| F-10 | `test_validate_db_host_invalid_awalan_strip` | Negatif | Input `'-host.com'`. | Return `False`. |
| F-11 | `test_validate_db_host_invalid_ip_3_oktet` | Edge Case | Input `'192.168.1'`. | Return `False`. |
| F-12 | `test_validate_db_host_invalid_ip_5_oktet` | Edge Case | Input `'192.168.1.1.1'`. | Return `False`. |
| F-13 | `test_validate_db_host_invalid_ip_leading_zero` | Edge Case | Input `'192.168.01.200'`. | Return `False`. |
| F-14 | `test_validate_db_host_invalid_hostname_terlalu_panjang` | Edge Case | Hostname > 253 karakter. | Return `False`. |
| F-15 | `test_validate_db_host_invalid_label_lebih_63_karakter` | Edge Case | Label hostname > 63 karakter. | Return `False`. |
| F-16 | `test_validate_db_host_valid_hostname_trailing_dot` | Edge Case | Input `'host.local.'` (trailing dot). | Return `True`. |
| F-17 | `test_validate_db_host_invalid_label_akhir_strip` | Negatif | Input `'host-.com'`. | Return `False`. |
| F-18 | `test_validate_db_host_invalid_ip_negatif` | Negatif | Input `'-1.0.0.1'`. | Return `False`. |

---

### GRUP G: Test `load_settings()` — Keberadaan File .env

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| G-01 | `test_load_settings_gagal_file_env_tidak_ditemukan` | Negatif | `Path.exists` return `False`. | `SystemExit(1)`, pesan `ERR-FILE-001`. |
| G-02 | `test_load_settings_memanggil_load_dotenv_saat_file_ada` | Positif | Verifikasi `load_dotenv` dipanggil dengan `encoding='utf-8'`. | `load_dotenv.assert_called_once()`. |
| G-03 | `test_load_settings_path_env_menunjuk_ke_root_proyek` | Validasi | Verifikasi path `.env` berakhir dengan `.env`. | Path argument ends with `.env`. |

---

### GRUP H: Test `load_settings()` — Validasi Variabel Wajib (REQUIRED_ENV_VARS)

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| H-01 | `test_load_settings_gagal_db_password_kosong` | Negatif | `DB_PASSWORD=''`. | `SystemExit(1)`. |
| H-02 | `test_load_settings_gagal_jwt_secret_key_kosong` | Negatif | `JWT_SECRET_KEY=''`. | `SystemExit(1)`. |
| H-03 | `test_load_settings_gagal_fernet_key_kosong` | Negatif | `FERNET_KEY=''`. | `SystemExit(1)`. |
| H-04 | `test_load_settings_gagal_backup_zip_password_kosong` | Negatif | `BACKUP_ZIP_PASSWORD=''`. | `SystemExit(1)`. |
| H-05 | `test_load_settings_gagal_db_password_placeholder` | Negatif | `DB_PASSWORD='YOUR_DB_PASSWORD_HERE'`. | `SystemExit(1)`. |
| H-06 | `test_load_settings_gagal_jwt_secret_key_placeholder` | Negatif | `JWT_SECRET_KEY='YOUR_JWT_SECRET_KEY_HERE'`. | `SystemExit(1)`. |
| H-07 | `test_load_settings_gagal_fernet_key_placeholder` | Negatif | `FERNET_KEY='YOUR_FERNET_KEY_HERE'`. | `SystemExit(1)`. |
| H-08 | `test_load_settings_gagal_backup_zip_password_placeholder` | Negatif | `BACKUP_ZIP_PASSWORD='YOUR_BACKUP_ZIP_PASSWORD_HERE'`. | `SystemExit(1)`. |
| H-09 | `test_load_settings_gagal_semua_variabel_wajib_kosong` | Negatif | Semua 4 variabel wajib diset `''`. | `SystemExit(1)`, multi-error agregat. |
| H-10 | `test_load_settings_gagal_semua_variabel_wajib_placeholder` | Negatif | Semua 4 variabel wajib diset `'YOUR_*_HERE'`. | `SystemExit(1)`, multi-error agregat. |

---

### GRUP I: Test `load_settings()` — Validasi APP_ENV

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| I-01 | `test_load_settings_sukses_app_env_production` | Positif | `APP_ENV='production'`. | `config.app_env == 'production'`. |
| I-02 | `test_load_settings_sukses_app_env_development` | Positif | `APP_ENV='development'`. | `config.app_env == 'development'`. |
| I-03 | `test_load_settings_gagal_app_env_staging` | Negatif | `APP_ENV='staging'`. | `SystemExit(1)`. |
| I-04 | `test_load_settings_gagal_app_env_string_acak` | Negatif | `APP_ENV='testing'`. | `SystemExit(1)`. |
| I-05 | `test_load_settings_gagal_app_env_huruf_kapital` | Edge Case | `APP_ENV='Production'` (case-sensitive). | `SystemExit(1)`. |
| I-06 | `test_load_settings_gagal_app_env_string_kosong` | Edge Case | `APP_ENV=''`. | `SystemExit(1)`. |
| I-07 | `test_load_settings_app_env_default_production` | Positif | `APP_ENV` tidak diset (None). | Default ke `'production'`. |
| I-08 | `test_load_settings_gagal_app_env_spasi` | Edge Case | `APP_ENV='  production  '` (dengan spasi). | `SystemExit(1)` (tidak di-strip). |

---

### GRUP J: Test `load_settings()` — Casting & Validasi Numerik (DB_PORT, DB_POOL_SIZE, JWT_LIFETIME, PRINTER_WIDTH, APP_CABANG_ID)

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| **DB_PORT** | | | | |
| J-01 | `test_load_settings_sukses_db_port_valid` | Positif | `DB_PORT='3307'`. | `config.db_port == 3307`. |
| J-02 | `test_load_settings_sukses_db_port_default_3306` | Positif | `DB_PORT` tidak diset. | `config.db_port == 3306`. |
| J-03 | `test_load_settings_gagal_db_port_bukan_angka` | Negatif | `DB_PORT='abc'`. | `SystemExit(1)`. |
| J-04 | `test_load_settings_gagal_db_port_nol` | Negatif | `DB_PORT='0'`. | `SystemExit(1)`. |
| J-05 | `test_load_settings_gagal_db_port_melebihi_65535` | Negatif | `DB_PORT='70000'`. | `SystemExit(1)`. |
| J-06 | `test_load_settings_sukses_db_port_batas_atas_65535` | Boundary | `DB_PORT='65535'`. | `config.db_port == 65535`. |
| J-07 | `test_load_settings_sukses_db_port_batas_bawah_1` | Boundary | `DB_PORT='1'`. | `config.db_port == 1`. |
| J-08 | `test_load_settings_gagal_db_port_negatif` | Negatif | `DB_PORT='-1'`. | `SystemExit(1)`. |
| **DB_POOL_SIZE** | | | | |
| J-09 | `test_load_settings_sukses_db_pool_size_valid` | Positif | `DB_POOL_SIZE='10'`. | `config.db_pool_size == 10`. |
| J-10 | `test_load_settings_sukses_db_pool_size_default` | Positif | `DB_POOL_SIZE` tidak diset. | `config.db_pool_size == 5`. |
| J-11 | `test_load_settings_gagal_db_pool_size_nol` | Negatif | `DB_POOL_SIZE='0'`. | `SystemExit(1)`. |
| J-12 | `test_load_settings_gagal_db_pool_size_melebihi_100` | Negatif | `DB_POOL_SIZE='101'`. | `SystemExit(1)`. |
| J-13 | `test_load_settings_sukses_db_pool_size_batas_bawah_1` | Boundary | `DB_POOL_SIZE='1'`. | `config.db_pool_size == 1`. |
| J-14 | `test_load_settings_sukses_db_pool_size_batas_atas_100` | Boundary | `DB_POOL_SIZE='100'`. | `config.db_pool_size == 100`. |
| **JWT_LIFETIME_SECONDS** | | | | |
| J-15 | `test_load_settings_sukses_jwt_lifetime_valid` | Positif | `JWT_LIFETIME_SECONDS='3600'`. | `config.jwt_lifetime_seconds == 3600`. |
| J-16 | `test_load_settings_sukses_jwt_lifetime_default_28800` | Positif | `JWT_LIFETIME_SECONDS` tidak diset. | `config.jwt_lifetime_seconds == 28800`. |
| J-17 | `test_load_settings_gagal_jwt_lifetime_negatif` | Negatif | `JWT_LIFETIME_SECONDS='-60'`. | `SystemExit(1)`. |
| J-18 | `test_load_settings_gagal_jwt_lifetime_nol` | Negatif | `JWT_LIFETIME_SECONDS='0'`. | `SystemExit(1)`. |
| J-19 | `test_load_settings_sukses_jwt_lifetime_1_detik` | Boundary | `JWT_LIFETIME_SECONDS='1'`. | `config.jwt_lifetime_seconds == 1`. |
| **PRINTER_WIDTH_MM** | | | | |
| J-20 | `test_load_settings_sukses_printer_width_58mm` | Positif | `PRINTER_WIDTH_MM='58'`. | `config.printer_width_mm == 58`. |
| J-21 | `test_load_settings_sukses_printer_width_80mm` | Positif | `PRINTER_WIDTH_MM='80'`. | `config.printer_width_mm == 80`. |
| J-22 | `test_load_settings_printer_width_non_standar_fallback_ke_default` | Edge Case | `PRINTER_WIDTH_MM='100'`. | Fallback ke `58`. |
| J-23 | `test_load_settings_printer_width_non_standar_32mm_fallback` | Edge Case | `PRINTER_WIDTH_MM='32'`. | Fallback ke `58`. |
| J-24 | `test_load_settings_printer_width_default_saat_tidak_diset` | Positif | `PRINTER_WIDTH_MM` tidak diset. | `config.printer_width_mm == 58`. |
| J-25 | `test_load_settings_printer_width_negatif_fallback` | Edge Case | `PRINTER_WIDTH_MM='-1'`. | Fallback ke `58`. |
| **APP_CABANG_ID** | | | | |
| J-26 | `test_load_settings_sukses_app_cabang_id_custom` | Positif | `APP_CABANG_ID='5'`. | `config.app_cabang_id == 5`. |
| J-27 | `test_load_settings_sukses_app_cabang_id_default_1` | Positif | `APP_CABANG_ID` tidak diset. | `config.app_cabang_id == 1`. |
| J-28 | `test_load_settings_gagal_app_cabang_id_nol` | Negatif | `APP_CABANG_ID='0'`. | `SystemExit(1)`. |
| J-29 | `test_load_settings_gagal_app_cabang_id_negatif` | Negatif | `APP_CABANG_ID='-5'`. | `SystemExit(1)`. |
| J-30 | `test_load_settings_gagal_app_cabang_id_bukan_angka` | Negatif | `APP_CABANG_ID='cabang_a'`. | `SystemExit(1)`. |

---

### GRUP K: Test `load_settings()` — Validasi Format & Kekuatan Kunci

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| K-01 | `test_load_settings_gagal_fernet_key_tidak_valid` | Negatif | `FERNET_KEY='kunci_fernet_salah'`. | `SystemExit(1)`, error `ERR-FILE-007`. |
| K-02 | `test_load_settings_jwt_secret_key_terlalu_pendek_dev_warning` | Positif | Key 13 karakter, `APP_ENV='development'`. | Sukses (warning only, no exit). |
| K-03 | `test_load_settings_jwt_secret_key_terlalu_pendek_prod_error` | Negatif | Key 13 karakter, `APP_ENV='production'`. | `SystemExit(1)`, error `ERR-FILE-006`. |
| K-04 | `test_load_settings_backup_zip_password_terlalu_pendek_dev_warning` | Positif | Password 5 karakter, `APP_ENV='development'`. | Sukses (warning only). |
| K-05 | `test_load_settings_backup_zip_password_terlalu_pendek_prod_error` | Negatif | Password 5 karakter, `APP_ENV='production'`. | `SystemExit(1)`. |
| K-06 | `test_load_settings_gagal_db_host_tidak_valid` | Negatif | `DB_HOST='invalid_host#name'`. | `SystemExit(1)`, error `ERR-FILE-008`. |
| K-07 | `test_load_settings_gagal_db_user_kosong` | Negatif | `DB_USER=''`. | `SystemExit(1)`. |
| K-08 | `test_load_settings_gagal_db_name_kosong` | Negatif | `DB_NAME=''`. | `SystemExit(1)`. |
| K-09 | `test_load_settings_gagal_printer_port_kosong` | Negatif | `PRINTER_PORT=''`. | `SystemExit(1)`. |

---

### GRUP L: Test `load_settings()` — Golden Path & Return Value Lengkap

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| L-01 | `test_load_settings_sukses_semua_variabel_lengkap` | Positif (Golden Path) | Semua 14 variabel diisi valid dan lengkap. | Return `AppConfig` dengan semua 14 field sesuai input. |
| L-02 | `test_load_settings_sukses_return_type_adalah_appconfig` | Positif | Verifikasi return type. | `isinstance(config, AppConfig) == True`. |
| L-03 | `test_load_settings_sukses_menggunakan_default_values` | Positif | Hanya 4 variabel wajib diisi, sisanya default. | Default values sesuai konstanta. |
| L-04 | `test_load_settings_db_host_default_saat_tidak_diset` | Positif | `DB_HOST` tidak diset. | `config.db_host == '10.10.10.10'`. |
| L-05 | `test_load_settings_db_name_default_saat_tidak_diset` | Positif | `DB_NAME` tidak diset. | `config.db_name == 'abucom_db'`. |
| L-06 | `test_load_settings_db_user_default_saat_tidak_diset` | Positif | `DB_USER` tidak diset. | `config.db_user == 'abucom_app'`. |
| L-07 | `test_load_settings_printer_port_default_saat_tidak_diset` | Positif | `PRINTER_PORT` tidak diset. | `config.printer_port == 'COM1'`. |

---

### GRUP M: Test `load_settings()` — Validasi Agregat Error & Interaksi Antar-Variabel

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| M-01 | `test_load_settings_gagal_multi_error_teragregasi` | Negatif | Set beberapa error sekaligus (misal: `DB_PASSWORD` kosong + `APP_ENV` invalid + `DB_PORT` bukan angka). | `SystemExit(1)`, semua error dicetak (bukan berhenti di error pertama). |
| M-02 | `test_load_settings_db_password_lemah_warning_tidak_gagal` | Edge Case | `DB_PASSWORD='weak'` (lemah tapi terisi). | Sukses (hanya warning, tidak SystemExit). |
| M-03 | `test_load_settings_sukses_db_host_valid_ip_private` | Positif | `DB_HOST='10.10.10.10'`. | `config.db_host == '10.10.10.10'`. |
| M-04 | `test_load_settings_sukses_db_host_hostname` | Positif | `DB_HOST='localhost'`. | `config.db_host == 'localhost'`. |
| M-05 | `test_load_settings_gagal_db_host_ip_invalid_oktet` | Negatif | `DB_HOST='999.0.0.1'`. | `SystemExit(1)`. |
| M-06 | `test_load_settings_sukses_jwt_key_tepat_32_karakter_prod` | Boundary | JWT key tepat 32 karakter, `APP_ENV='production'`. | Sukses, tidak SystemExit. |
| M-07 | `test_load_settings_sukses_backup_password_tepat_8_karakter_prod` | Boundary | Backup password tepat 8 karakter, `APP_ENV='production'`. | Sukses. |

---

### GRUP N: Test `_safe_int_cast()` dan `_validate_int_range()` — Mode Error Aggregation

| No | Nama Skenario | Tipe | Deskripsi | Expected |
|:---:|---|:---:|---|---|
| N-01 | `test_safe_int_cast_mode_agregasi_error_tidak_exit` | Positif | Input invalid `'xyz'` dengan `errors=[]`. | `errors` berisi pesan error, return default, **bukan** SystemExit. |
| N-02 | `test_validate_int_range_mode_agregasi_error_tidak_exit` | Positif | Input `0` (di luar range 1-100) dengan `errors=[]`. | `errors` berisi pesan error, **bukan** SystemExit. |
| N-03 | `test_safe_int_cast_mode_langsung_exit_tanpa_errors_param` | Negatif | Input invalid `'xyz'` tanpa parameter `errors` (default None). | `SystemExit(1)`. |
| N-04 | `test_validate_int_range_mode_langsung_exit_tanpa_errors_param` | Negatif | Input `0` (di luar range) tanpa parameter `errors` (default None). | `SystemExit(1)`. |

---

## 5. Kaidah Standar Tambahan

### 5.1. Konvensi Penamaan Fungsi Test
- Format: `test_<nama_fungsi_target>_<kondisi_spesifik>_<hasil_expected>()`
- Contoh: `test_safe_int_cast_gagal_string_float()`
- Bahasa: Indonesia deskriptif, snake_case.

### 5.2. Format Docstring Test Function
```python
def test_nama_skenario() -> None:
    """Deskripsi singkat apa yang diuji.

    Tipe: Positif / Negatif / Edge Case / Boundary
    Target: <nama_fungsi_target>
    """
    # Arrange
    ...
    # Act
    ...
    # Assert
    ...
```

### 5.3. Handling Error Code Assertion
Untuk test yang mengharapkan `SystemExit(1)`, gunakan pola:
```python
with pytest.raises(SystemExit) as exc_info:
    <panggilan_fungsi>()
assert exc_info.value.code == 1
```

### 5.4. Clean State (Fixture Autouse)
Fixture `clean_env` yang sudah ada di file wajib dipertahankan dan **TIDAK BOLEH** dihapus atau dimodifikasi:
```python
@pytest.fixture(autouse=True)
def clean_env(monkeypatch: pytest.MonkeyPatch) -> Generator[None, None, None]:
    for var in [
        'APP_ENV', 'APP_CABANG_ID', 'DB_HOST', 'DB_PORT',
        'DB_USER', 'DB_PASSWORD', 'DB_NAME', 'DB_POOL_SIZE',
        'JWT_SECRET_KEY', 'JWT_LIFETIME_SECONDS', 'FERNET_KEY',
        'BACKUP_ZIP_PASSWORD', 'PRINTER_PORT', 'PRINTER_WIDTH_MM',
    ]:
        monkeypatch.delenv(var, raising=False)
    yield
```

### 5.5. Helper Functions yang Sudah Ada
Gunakan helper function yang sudah ada di file, **JANGAN** buat duplikat:
- `_make_valid_env() -> dict[str, str]` — Membuat dictionary env vars valid lengkap.
- `_mock_getenv_from_dict(env_dict) -> Callable` — Membuat side_effect untuk mock `os.getenv`.

### 5.6. Pola Mock Standard untuk `load_settings()`
Setiap test yang menguji `load_settings()` **WAJIB** menggunakan 3 decorator mock:
```python
@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_nama_skenario(
    mock_getenv: MagicMock, mock_load_dotenv: MagicMock, mock_exists: MagicMock
) -> None:
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    # ... modifikasi env_dict sesuai skenario ...
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)
    # Act & Assert
    ...
```

> **PERHATIAN**: Urutan parameter fungsi test **TERBALIK** dari urutan decorator `@patch` (dari bawah ke atas). `os.getenv` di decorator paling bawah → menjadi parameter pertama.

### 5.7. Import yang Diperlukan
Pastikan import berikut ada di bagian atas file:
```python
# 1. Standard Library
import sys
from collections.abc import Generator
from pathlib import Path
from typing import Callable, Any
from unittest.mock import patch, MagicMock

# 2. Third-Party
import pytest

# 3. Local Modules
import config.settings as settings_mod
from config.settings import (
    load_settings,
    _safe_int_cast,
    _validate_int_range,
    AppConfig,
    REQUIRED_ENV_VARS,
    VALID_APP_ENVS,
    VALID_PRINTER_WIDTHS,
    DEFAULT_DB_HOST,
    DEFAULT_DB_PORT,
    DEFAULT_DB_POOL_SIZE,
    DEFAULT_JWT_LIFETIME,
    DEFAULT_PRINTER_WIDTH,
    MIN_JWT_KEY_LENGTH,
    MIN_BACKUP_PASSWORD_LENGTH,
)
```

---

## 6. Folder Penyimpanan dan Dependensi

| Item | Spesifikasi |
|---|---|
| **File test** | `tests/test_settings.py` (file sudah ada, tambahkan test baru di bagian bawah) |
| **File `__init__.py`** | `tests/__init__.py` (sudah ada) |
| **Modul target** | `config/settings.py` |
| **Framework test** | `pytest==8.2.0` (sudah ada di `requirements.txt`) |
| **Coverage tool** | `coverage==7.5.1` (sudah ada di `requirements.txt`) |
| **Perintah run test** | `python -m pytest tests/test_settings.py -v --tb=short` |
| **Perintah run coverage** | `python -m coverage run -m pytest tests/test_settings.py -v && python -m coverage report -m --include=config/settings.py` |

---

## 7. Kriteria Keberhasilan (Definition of Done)

- [ ] Seluruh skenario test dari Bab 4 (GRUP A s.d N) telah diimplementasikan (yang belum ada di existing).
- [ ] **100% test PASS** saat dijalankan `pytest -v`.
- [ ] **Code coverage `config/settings.py` ≥ 90%** yang dibuktikan via `coverage report`.
- [ ] **Tidak ada** test function yang menggantung (TODO, pass, placeholder, print-only).
- [ ] **Tidak ada** test yang melakukan koneksi database riil atau membaca file `.env` riil.
- [ ] **Tidak ada** test baru yang menyebabkan test lama gagal (zero regression).
- [ ] **Tidak ada** modifikasi pada file selain `tests/test_settings.py`.
- [ ] Semua test function memiliki docstring lengkap (format PEP 257 Google Style).
- [ ] Semua test function memiliki type hint return `-> None`.
- [ ] Clean state terjamin — setiap test independen dan urutan eksekusi tidak mempengaruhi hasil.
