---
judul      : Unit Test Feature Pembacaan Konfigurasi Dotenv Saat Startup
prioritas  : High
status     : Open
tipe       : Unit Testing
modul      : config/settings.py
target     : tests/test_settings.py
tanggal    : 2026-06-04
penyusun   : Claude Opus 4.6 (Thinking) — Strategi Sistem & Keamanan
---

# ISSUE - Unit Test Feature Pembacaan Konfigurasi Dotenv Saat Startup

## 1. Penetapan Persona Eksekutor

**Persona yang WAJIB diadopsi oleh AI/Programmer pelaksana:**

> **Senior Python QA Engineer & Unit Test Specialist**
> Kamu adalah seorang Senior QA Engineer yang ahli dalam menulis unit test Python menggunakan `pytest` dan `unittest.mock`. Kamu memiliki keahlian mendalam dalam menguji modul konfigurasi yang melibatkan pembacaan file `.env`, environment variables, type casting, dan validasi input. Kamu sangat teliti terhadap edge cases, memahami prinsip isolasi test (mocking), dan memastikan setiap jalur kode (`code path`) tercakup oleh skenario test tanpa koneksi ke resource eksternal (filesystem nyata, database, jaringan). Kamu menulis kode Python yang patuh terhadap standar PEP 8, PEP 257, dan PEP 484 sesuai Coding Standard proyek AbuCom.

---

## 2. Dokumen Referensi Utama

Berikut dokumen SDLC yang **WAJIB** dibaca dan diekstrak datanya sebelum memulai pengerjaan:

| No | Dokumen Referensi | Path Relatif | Prioritas | Relevansi |
|----|-------------------|--------------|-----------|-----------|
| 1 | **Coding Standard** | `docs/sdlc/04_implementation/01_coding_standard.md` | **PRIMER** | Konvensi penamaan test file/function, aturan unit test pure functions, format docstring, type hints, import order, header module |
| 2 | **Test Plan** | `docs/sdlc/05_testing/01_test_plan.md` | **PRIMER** | Strategi unit testing, target coverage ≥ 90%, framework `pytest==8.2.0`, `coverage==7.5.1`, aturan isolasi tanpa koneksi fisik |
| 3 | **Source Code Target** | `config/settings.py` | **PRIMER** | Kode implementasi yang diuji: `load_settings()`, `_safe_int_cast()`, `_validate_int_range()`, `AppConfig`, konstanta |
| 4 | **Environment Template** | `.env.example` | **SEKUNDER** | Daftar lengkap 14 variabel environment dan format placeholder `YOUR_*` |
| 5 | **Existing Test File** | `tests/test_settings.py` | **SEKUNDER** | File test yang sudah ada (9 test) yang akan di-**overwrite sepenuhnya** dengan versi yang lebih lengkap |
| 6 | **Narasi Proyek** | `docs/sdlc/narasi.txt` | **TERSIER** | Tidak digunakan langsung — konteks bisnis sudah tercakup di Coding Standard dan Test Plan |

---

## 3. Ringkasan Data Relevan dari Dokumen Referensi

### 3.1. Dari Coding Standard (`01_coding_standard.md`)

**Standar Unit Testing (Bab 14):**
- Framework: `pytest` (Bab 14.1)
- Target coverage: ≥ 90% logika bisnis (Bab 14.2)
- Penamaan file test: `test_<modul_target>.py` di folder `tests/` (Bab 14.3)
- Penamaan fungsi test: `test_<behavior_spesifik>()` (Bab 14.3)
- Unit test **WAJIB** deterministik, terisolasi penuh, **DILARANG** koneksi fisik database/file system (Bab 14.4)
- Data test disuplai melalui mock (Bab 14.4)

**Standar Kode:**
- Paradigma: Functional Programming murni, tanpa `class` di alur bisnis (Bab 2.2)
- Import order: Standard Library → Third-Party → Local Modules (Bab 5.4.1)
- String: single quote (`'`) untuk internal, double quote (`"`) untuk display/docstring (Bab 5.5)
- Type hints wajib pada semua fungsi publik (Bab 7.1)
- Header module docstring wajib (Bab 6.4)
- Docstring format PEP 257 Google Style dengan Args/Returns/Raises (Bab 6.2)
- Batas baris: ≤ 120 karakter (Bab 5.3)
- Indentasi: 4 spasi (Bab 5.2)
- 2 baris kosong antar fungsi top-level (Bab 5.2)

**Standar Konfigurasi `.env` (Bab 10.1):**
- Kredensial wajib di `.env`, dilarang hardcode
- Validator startup wajib cek kelengkapan `.env`
- Jika `.env` tidak ada → `ERR-FILE-001` → startup batal `sys.exit(1)`

**Error Code Catalog (Bab 11.5):**
- `ERR-FILE-001`: File .env tidak ditemukan
- `ERR-FILE-002`: Variabel wajib belum diisi
- `ERR-FILE-003`: Tipe data tidak valid (bukan integer)
- `ERR-FILE-004`: Nilai di luar rentang
- `ERR-FILE-005`: APP_ENV tidak valid

### 3.2. Dari Test Plan (`01_test_plan.md`)

**Strategi Testing Relevan:**
- Unit Testing ditargetkan pada pure functions terbebas dari efek samping I/O (Bab 3.1.1)
- Pendekatan: deterministik menggunakan mock data structures (Bab 3.1.1)
- White-Box Testing untuk memverifikasi jalur logika internal, exception handling, dan coverage (Bab 3.3)
- Error Code `ERR-FILE-001` terdaftar di matriks ketertelusuran (Bab 12.4 baris 820)
- Modul Tambahan (Additional) mencakup "Startup validation .env" (Bab 2.1 baris 123)

**Testing Tools:**
- `pytest==8.2.1` (atau versi stabil di venv, saat ini `pytest==8.2.0` di `requirements.txt`)
- `coverage==7.5.1`

### 3.3. Dari Source Code `config/settings.py`

**Fungsi yang WAJIB diuji:**

| No | Fungsi/Entitas | Baris | Deskripsi |
|----|----------------|-------|-----------|
| 1 | `AppConfig` | L42-L57 | NamedTuple imutabel dengan 14 field konfigurasi |
| 2 | `_safe_int_cast(value, default, var_name)` | L60-L83 | Casting string ke int dengan fallback, `sys.exit(1)` jika gagal |
| 3 | `_validate_int_range(value, min_val, max_val, var_name)` | L86-L107 | Validasi integer dalam rentang, `sys.exit(1)` jika di luar |
| 4 | `load_settings()` | L110-L220 | Fungsi utama: load `.env`, validasi, cast, return `AppConfig` |

**Konstanta yang relevan untuk test:**

| Konstanta | Nilai | Deskripsi |
|-----------|-------|-----------|
| `DEFAULT_DB_HOST` | `'10.10.10.10'` | Default host database |
| `DEFAULT_DB_PORT` | `3306` | Default port MySQL |
| `DEFAULT_DB_POOL_SIZE` | `5` | Default ukuran pool |
| `DEFAULT_JWT_LIFETIME` | `28800` | Default lifetime JWT (8 jam) |
| `DEFAULT_PRINTER_WIDTH` | `58` | Default lebar printer mm |
| `VALID_APP_ENVS` | `('development', 'production')` | Nilai APP_ENV yang valid |
| `VALID_PRINTER_WIDTHS` | `(58, 80)` | Lebar printer yang valid |
| `REQUIRED_ENV_VARS` | `('DB_PASSWORD', 'JWT_SECRET_KEY', 'FERNET_KEY', 'BACKUP_ZIP_PASSWORD')` | 4 variabel wajib |

**Alur validasi `load_settings()` (4 tahap berurutan):**
1. Cek keberadaan fisik `.env` → `ERR-FILE-001` + `sys.exit(1)`
2. Load dotenv → validasi 4 variabel wajib tidak kosong dan tidak placeholder `YOUR_*` → `ERR-FILE-002` + `sys.exit(1)`
3. Validasi `APP_ENV` ∈ `('development', 'production')` → `ERR-FILE-005` + `sys.exit(1)`
4. Casting integer + validasi range:
   - `APP_CABANG_ID`: int cast, default `1`
   - `DB_PORT`: int cast + range `1-65535` → `ERR-FILE-003` / `ERR-FILE-004`
   - `DB_POOL_SIZE`: int cast + range `1-100` → `ERR-FILE-003` / `ERR-FILE-004`
   - `JWT_LIFETIME_SECONDS`: int cast + positif (> 0) → `ERR-FILE-003` / `ERR-FILE-004`
   - `PRINTER_WIDTH_MM`: int cast + fallback ke default jika bukan 58/80 (warning, bukan exit)

### 3.4. Dari `.env.example`

**Daftar 14 variabel environment:**
1. `APP_ENV` — default: `production`
2. `APP_CABANG_ID` — default: `1`
3. `DB_HOST` — default: `10.10.10.10`
4. `DB_PORT` — default: `3306`
5. `DB_USER` — default: `abucom_app`
6. `DB_PASSWORD` — **WAJIB** (placeholder: `YOUR_DB_PASSWORD_HERE`)
7. `DB_NAME` — default: `abucom_db`
8. `DB_POOL_SIZE` — default: `5`
9. `JWT_SECRET_KEY` — **WAJIB** (placeholder: `YOUR_JWT_SECRET_KEY_HERE`)
10. `JWT_LIFETIME_SECONDS` — default: `28800`
11. `FERNET_KEY` — **WAJIB** (placeholder: `YOUR_FERNET_KEY_HERE`)
12. `BACKUP_ZIP_PASSWORD` — **WAJIB** (placeholder: `YOUR_BACKUP_ZIP_PASSWORD_HERE`)
13. `PRINTER_PORT` — default: `COM1`
14. `PRINTER_WIDTH_MM` — default: `58`

---

## 4. Batasan dan Cakupan Pengerjaan

### 4.1. Cakupan (In-Scope)
- [x] Unit test untuk fungsi `_safe_int_cast()`
- [x] Unit test untuk fungsi `_validate_int_range()`
- [x] Unit test untuk fungsi `load_settings()` (seluruh 4 tahap validasi)
- [x] Validasi imutabilitas `AppConfig` (NamedTuple)
- [x] Validasi konstanta modul (`REQUIRED_ENV_VARS`, `VALID_APP_ENVS`, dll.)
- [x] Verifikasi seluruh 5 kode error (`ERR-FILE-001` s.d `ERR-FILE-005`)

### 4.2. Di Luar Cakupan (Out-of-Scope)
- ❌ Koneksi fisik ke database MySQL
- ❌ Pembacaan file `.env` yang sesungguhnya dari disk
- ❌ Modifikasi kode `config/settings.py` (hanya membuat test)
- ❌ Integration test dengan `main.py` atau modul lain
- ❌ Test untuk modul `config/__init__.py`
- ❌ Test performa / benchmark timing

### 4.3. Aturan Isolasi
- **WAJIB** menggunakan `unittest.mock.patch` untuk mock:
  - `config.settings.Path.exists` — simulasi ada/tidaknya `.env`
  - `config.settings.load_dotenv` — mencegah pembacaan `.env` dari disk
  - `config.settings.os.getenv` — menyuplai data environment tanpa OS
- **WAJIB** menggunakan `pytest.raises(SystemExit)` untuk menguji `sys.exit(1)`
- **DILARANG** membuat/menghapus file `.env` fisik di filesystem
- **DILARANG** menggunakan `os.environ` langsung (gunakan mock `os.getenv`)
- **WAJIB** memastikan setiap test tidak meninggalkan side effect ke test lain

---

## 5. Alur Pengerjaan (Step-by-Step)

### Fase 0: Pembacaan dan Pemahaman Konteks

- [ ] **0.1** Baca file `config/settings.py` secara lengkap dari baris 1 hingga 222. Pahami:
  - Struktur NamedTuple `AppConfig` dan ke-14 field-nya
  - Fungsi `_safe_int_cast()` — parameter, return type, kondisi `sys.exit(1)`
  - Fungsi `_validate_int_range()` — parameter, return type, kondisi `sys.exit(1)`
  - Fungsi `load_settings()` — seluruh 4 tahap validasi berurutan
  - Konstanta modul: `DEFAULT_*`, `VALID_*`, `REQUIRED_ENV_VARS`
  - 5 kode error: `ERR-FILE-001` s.d `ERR-FILE-005`
- [ ] **0.2** Baca file `config/__init__.py` untuk memahami public exports modul
- [ ] **0.3** Baca file `.env.example` untuk memahami daftar 14 variabel dan format placeholder
- [ ] **0.4** Baca file `tests/test_unit_db_connector.py` baris 1-50 sebagai referensi pola penulisan:
  - Header module docstring
  - Import structure
  - `@pytest.fixture(autouse=True)` untuk clean state
  - Pola Arrange-Act-Assert

### Fase 1: Persiapan File Test

- [ ] **1.1** Buka (atau buat baru) file `tests/test_settings.py`
- [ ] **1.2** Tulis header module docstring sesuai template standar AbuCom:
  ```python
  """
  Nama Modul: test_settings.py
  Deskripsi: Unit test terisolasi (mocked) untuk modul config/settings.py.
             Menguji seluruh fungsi pembacaan konfigurasi dotenv saat startup,
             termasuk validasi keberadaan file, variabel wajib, casting tipe data,
             validasi rentang nilai, dan pembentukan AppConfig imutabel.
  Author: [Nama AI Pelaksana]
  Tanggal: [YYYY-MM-DD]
  """
  ```
- [ ] **1.3** Tulis blok import sesuai urutan standar:
  ```python
  # 1. Standard Library
  import sys
  from pathlib import Path
  from unittest.mock import patch, MagicMock, call

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
  )
  ```

### Fase 2: Fixture Clean State

- [ ] **2.1** Buat fixture `autouse=True` untuk membersihkan environment di setiap test:
  ```python
  @pytest.fixture(autouse=True)
  def clean_env(monkeypatch):
      """Membersihkan environment variables sebelum setiap test.

      Memastikan setiap test dimulai dari clean state tanpa sisa
      environment variables dari test sebelumnya yang bisa mencemari
      hasil mock os.getenv.
      """
      # Hapus semua env vars yang relevan agar tidak bocor antar test
      for var in [
          'APP_ENV', 'APP_CABANG_ID', 'DB_HOST', 'DB_PORT',
          'DB_USER', 'DB_PASSWORD', 'DB_NAME', 'DB_POOL_SIZE',
          'JWT_SECRET_KEY', 'JWT_LIFETIME_SECONDS', 'FERNET_KEY',
          'BACKUP_ZIP_PASSWORD', 'PRINTER_PORT', 'PRINTER_WIDTH_MM',
      ]:
          monkeypatch.delenv(var, raising=False)
      yield
  ```

- [ ] **2.2** Buat helper function untuk menyuplai mock env lengkap yang valid:
  ```python
  def _make_valid_env() -> dict:
      """Mengembalikan dictionary environment variables yang valid dan lengkap.

      Returns:
          dict: Kumpulan key-value env vars yang akan lolos semua validasi.
      """
      return {
          'APP_ENV': 'production',
          'APP_CABANG_ID': '2',
          'DB_HOST': '192.168.1.200',
          'DB_PORT': '3306',
          'DB_USER': 'abucom_app',
          'DB_PASSWORD': 'S3cureP@ssw0rd!',
          'DB_NAME': 'abucom_db',
          'DB_POOL_SIZE': '5',
          'JWT_SECRET_KEY': 'e837df26a91bb812b7a90f19c991f812cb71a9ee08311ab81ab65b1cd78201de',
          'JWT_LIFETIME_SECONDS': '28800',
          'FERNET_KEY': 'Z2VtaW5pYW50aWdyYXZpdHlzZWN1cmVjcm1rZXkyMDI2',
          'BACKUP_ZIP_PASSWORD': 'AES256EncryptBackup2026#',
          'PRINTER_PORT': 'COM1',
          'PRINTER_WIDTH_MM': '58',
      }
  ```

- [ ] **2.3** Buat helper function untuk membuat mock `os.getenv` dari dictionary:
  ```python
  def _mock_getenv_from_dict(env_dict: dict):
      """Membuat side_effect function untuk mock os.getenv dari dictionary.

      Args:
          env_dict (dict): Dictionary berisi key-value environment variables.

      Returns:
          Callable: Fungsi side_effect yang kompatibel dengan os.getenv signature.
      """
      def _side_effect(key, default=None):
          return env_dict.get(key, default)
      return _side_effect
  ```

### Fase 3: Penulisan Skenario Test

> **PENTING:** Setiap fungsi test WAJIB mengikuti pola **Arrange-Act-Assert** dengan komentar pembatas.
> Setiap fungsi test WAJIB memiliki docstring yang menjelaskan skenario, tipe (Positif/Negatif/Edge Case), dan target fungsi.

---

#### Grup A: Test Konstanta dan Struktur Data (Validasi Input)

- [ ] **3.A.01** `test_required_env_vars_berisi_empat_variabel_wajib()`
  - Tipe: Validasi Input
  - Verifikasi `REQUIRED_ENV_VARS` adalah tuple berisi tepat 4 elemen
  - Verifikasi isi: `'DB_PASSWORD'`, `'JWT_SECRET_KEY'`, `'FERNET_KEY'`, `'BACKUP_ZIP_PASSWORD'`

- [ ] **3.A.02** `test_valid_app_envs_berisi_development_dan_production()`
  - Tipe: Validasi Input
  - Verifikasi `VALID_APP_ENVS` adalah tuple berisi tepat `('development', 'production')`

- [ ] **3.A.03** `test_valid_printer_widths_berisi_58_dan_80()`
  - Tipe: Validasi Input
  - Verifikasi `VALID_PRINTER_WIDTHS` adalah tuple berisi tepat `(58, 80)`

- [ ] **3.A.04** `test_default_konstanta_memiliki_nilai_yang_benar()`
  - Tipe: Validasi Input
  - Verifikasi: `DEFAULT_DB_HOST == '10.10.10.10'`
  - Verifikasi: `DEFAULT_DB_PORT == 3306`
  - Verifikasi: `DEFAULT_DB_POOL_SIZE == 5`
  - Verifikasi: `DEFAULT_JWT_LIFETIME == 28800`
  - Verifikasi: `DEFAULT_PRINTER_WIDTH == 58`

- [ ] **3.A.05** `test_appconfig_memiliki_14_field_yang_benar()`
  - Tipe: Validasi Input
  - Verifikasi `AppConfig._fields` memiliki tepat 14 elemen
  - Verifikasi nama setiap field sesuai definisi di `settings.py`

- [ ] **3.A.06** `test_appconfig_bersifat_imutabel()`
  - Tipe: Validasi Input
  - Buat instansi `AppConfig` dengan data dummy
  - Verifikasi `pytest.raises(AttributeError)` saat mencoba mengubah atribut

---

#### Grup B: Test `_safe_int_cast()` (7 skenario)

- [ ] **3.B.01** `test_safe_int_cast_sukses_string_integer_valid()`
  - Tipe: Positif
  - Input: `value='123'`, `default=10`, `var_name='TEST'`
  - Expected: return `123`

- [ ] **3.B.02** `test_safe_int_cast_sukses_return_default_saat_none()`
  - Tipe: Positif
  - Input: `value=None`, `default=42`, `var_name='TEST'`
  - Expected: return `42`

- [ ] **3.B.03** `test_safe_int_cast_sukses_string_negatif()`
  - Tipe: Positif
  - Input: `value='-5'`, `default=10`, `var_name='TEST'`
  - Expected: return `-5`

- [ ] **3.B.04** `test_safe_int_cast_sukses_string_nol()`
  - Tipe: Positif
  - Input: `value='0'`, `default=10`, `var_name='TEST'`
  - Expected: return `0`

- [ ] **3.B.05** `test_safe_int_cast_gagal_string_bukan_angka()`
  - Tipe: Negatif
  - Input: `value='abc'`, `default=10`, `var_name='TEST_VAR'`
  - Expected: `SystemExit` dengan code `1`

- [ ] **3.B.06** `test_safe_int_cast_gagal_string_float()`
  - Tipe: Negatif / Edge Case
  - Input: `value='3.14'`, `default=10`, `var_name='DB_PORT'`
  - Expected: `SystemExit` dengan code `1`

- [ ] **3.B.07** `test_safe_int_cast_gagal_string_kosong()`
  - Tipe: Negatif / Edge Case
  - Input: `value=''`, `default=10`, `var_name='DB_PORT'`
  - Expected: `SystemExit` dengan code `1`

---

#### Grup C: Test `_validate_int_range()` (7 skenario)

- [ ] **3.C.01** `test_validate_int_range_sukses_nilai_di_tengah_rentang()`
  - Tipe: Positif
  - Input: `value=50`, `min_val=1`, `max_val=100`, `var_name='TEST'`
  - Expected: return `50`

- [ ] **3.C.02** `test_validate_int_range_sukses_nilai_sama_dengan_batas_bawah()`
  - Tipe: Edge Case (Boundary)
  - Input: `value=1`, `min_val=1`, `max_val=100`, `var_name='TEST'`
  - Expected: return `1`

- [ ] **3.C.03** `test_validate_int_range_sukses_nilai_sama_dengan_batas_atas()`
  - Tipe: Edge Case (Boundary)
  - Input: `value=100`, `min_val=1`, `max_val=100`, `var_name='TEST'`
  - Expected: return `100`

- [ ] **3.C.04** `test_validate_int_range_gagal_nilai_di_bawah_batas_minimum()`
  - Tipe: Negatif
  - Input: `value=0`, `min_val=1`, `max_val=100`, `var_name='DB_PORT'`
  - Expected: `SystemExit` dengan code `1`

- [ ] **3.C.05** `test_validate_int_range_gagal_nilai_di_atas_batas_maksimum()`
  - Tipe: Negatif
  - Input: `value=101`, `min_val=1`, `max_val=100`, `var_name='DB_POOL_SIZE'`
  - Expected: `SystemExit` dengan code `1`

- [ ] **3.C.06** `test_validate_int_range_gagal_nilai_negatif()`
  - Tipe: Negatif
  - Input: `value=-10`, `min_val=1`, `max_val=65535`, `var_name='DB_PORT'`
  - Expected: `SystemExit` dengan code `1`

- [ ] **3.C.07** `test_validate_int_range_sukses_nilai_batas_port_65535()`
  - Tipe: Edge Case (Boundary)
  - Input: `value=65535`, `min_val=1`, `max_val=65535`, `var_name='DB_PORT'`
  - Expected: return `65535`

---

#### Grup D: Test `load_settings()` — Tahap 1: Keberadaan File `.env` (3 skenario)

- [ ] **3.D.01** `test_load_settings_gagal_file_env_tidak_ditemukan()`
  - Tipe: Negatif
  - Mock: `config.settings.Path.exists` return `False`
  - Expected: `SystemExit` code `1`
  - Verifikasi: error sesuai kode `ERR-FILE-001`

- [ ] **3.D.02** `test_load_settings_memanggil_load_dotenv_saat_file_ada()`
  - Tipe: Positif
  - Mock: `Path.exists` return `True`, `load_dotenv`, `os.getenv` dengan env valid lengkap
  - Expected: `load_dotenv` dipanggil tepat 1 kali
  - Verifikasi: argumen `encoding='utf-8'` dilewatkan ke `load_dotenv`

- [ ] **3.D.03** `test_load_settings_path_env_menunjuk_ke_root_proyek()`
  - Tipe: Validasi
  - Mock: `Path.exists` return `True`, env valid
  - Expected: path `.env` dihitung dari `Path(__file__).parent.parent / '.env'`
  - Verifikasi: `load_dotenv` menerima path string yang berakhir dengan `.env`

---

#### Grup E: Test `load_settings()` — Tahap 2: Validasi Variabel Wajib (8 skenario)

- [ ] **3.E.01** `test_load_settings_gagal_db_password_kosong()`
  - Tipe: Negatif
  - Mock: env valid kecuali `DB_PASSWORD` = `''`
  - Expected: `SystemExit` code `1` (ERR-FILE-002)

- [ ] **3.E.02** `test_load_settings_gagal_jwt_secret_key_kosong()`
  - Tipe: Negatif
  - Mock: env valid kecuali `JWT_SECRET_KEY` = `''`
  - Expected: `SystemExit` code `1` (ERR-FILE-002)

- [ ] **3.E.03** `test_load_settings_gagal_fernet_key_kosong()`
  - Tipe: Negatif
  - Mock: env valid kecuali `FERNET_KEY` = `''`
  - Expected: `SystemExit` code `1` (ERR-FILE-002)

- [ ] **3.E.04** `test_load_settings_gagal_backup_zip_password_kosong()`
  - Tipe: Negatif
  - Mock: env valid kecuali `BACKUP_ZIP_PASSWORD` = `''`
  - Expected: `SystemExit` code `1` (ERR-FILE-002)

- [ ] **3.E.05** `test_load_settings_gagal_db_password_placeholder()`
  - Tipe: Negatif
  - Mock: env valid kecuali `DB_PASSWORD` = `'YOUR_DB_PASSWORD_HERE'`
  - Expected: `SystemExit` code `1` (ERR-FILE-002)

- [ ] **3.E.06** `test_load_settings_gagal_jwt_secret_key_placeholder()`
  - Tipe: Negatif
  - Mock: env valid kecuali `JWT_SECRET_KEY` = `'YOUR_JWT_SECRET_KEY_HERE'`
  - Expected: `SystemExit` code `1` (ERR-FILE-002)

- [ ] **3.E.07** `test_load_settings_gagal_fernet_key_placeholder()`
  - Tipe: Negatif
  - Mock: env valid kecuali `FERNET_KEY` = `'YOUR_FERNET_KEY_HERE'`
  - Expected: `SystemExit` code `1` (ERR-FILE-002)

- [ ] **3.E.08** `test_load_settings_gagal_backup_zip_password_placeholder()`
  - Tipe: Negatif
  - Mock: env valid kecuali `BACKUP_ZIP_PASSWORD` = `'YOUR_BACKUP_ZIP_PASSWORD_HERE'`
  - Expected: `SystemExit` code `1` (ERR-FILE-002)

---

#### Grup F: Test `load_settings()` — Tahap 3: Validasi APP_ENV (4 skenario)

- [ ] **3.F.01** `test_load_settings_sukses_app_env_production()`
  - Tipe: Positif
  - Mock: env valid dengan `APP_ENV` = `'production'`
  - Expected: `config.app_env == 'production'`

- [ ] **3.F.02** `test_load_settings_sukses_app_env_development()`
  - Tipe: Positif
  - Mock: env valid dengan `APP_ENV` = `'development'`
  - Expected: `config.app_env == 'development'`

- [ ] **3.F.03** `test_load_settings_gagal_app_env_staging()`
  - Tipe: Negatif
  - Mock: env valid kecuali `APP_ENV` = `'staging'`
  - Expected: `SystemExit` code `1` (ERR-FILE-005)

- [ ] **3.F.04** `test_load_settings_gagal_app_env_string_acak()`
  - Tipe: Negatif
  - Mock: env valid kecuali `APP_ENV` = `'testing'`
  - Expected: `SystemExit` code `1` (ERR-FILE-005)

---

#### Grup G: Test `load_settings()` — Tahap 4: Casting & Validasi Numerik (16 skenario)

**Sub-grup G1: DB_PORT**

- [ ] **3.G.01** `test_load_settings_sukses_db_port_valid()`
  - Tipe: Positif
  - Mock: env valid dengan `DB_PORT` = `'3307'`
  - Expected: `config.db_port == 3307`

- [ ] **3.G.02** `test_load_settings_sukses_db_port_default_3306()`
  - Tipe: Positif
  - Mock: env valid tanpa key `DB_PORT` (return `None` dari `os.getenv`)
  - Expected: `config.db_port == 3306` (DEFAULT_DB_PORT)

- [ ] **3.G.03** `test_load_settings_gagal_db_port_bukan_angka()`
  - Tipe: Negatif
  - Mock: env valid kecuali `DB_PORT` = `'abc'`
  - Expected: `SystemExit` code `1` (ERR-FILE-003)

- [ ] **3.G.04** `test_load_settings_gagal_db_port_nol()`
  - Tipe: Negatif
  - Mock: env valid kecuali `DB_PORT` = `'0'`
  - Expected: `SystemExit` code `1` (ERR-FILE-004: di luar rentang 1-65535)

- [ ] **3.G.05** `test_load_settings_gagal_db_port_melebihi_65535()`
  - Tipe: Negatif / Edge Case
  - Mock: env valid kecuali `DB_PORT` = `'70000'`
  - Expected: `SystemExit` code `1` (ERR-FILE-004)

- [ ] **3.G.06** `test_load_settings_sukses_db_port_batas_atas_65535()`
  - Tipe: Edge Case (Boundary)
  - Mock: env valid dengan `DB_PORT` = `'65535'`
  - Expected: `config.db_port == 65535`

- [ ] **3.G.07** `test_load_settings_sukses_db_port_batas_bawah_1()`
  - Tipe: Edge Case (Boundary)
  - Mock: env valid dengan `DB_PORT` = `'1'`
  - Expected: `config.db_port == 1`

**Sub-grup G2: DB_POOL_SIZE**

- [ ] **3.G.08** `test_load_settings_sukses_db_pool_size_valid()`
  - Tipe: Positif
  - Mock: env valid dengan `DB_POOL_SIZE` = `'10'`
  - Expected: `config.db_pool_size == 10`

- [ ] **3.G.09** `test_load_settings_sukses_db_pool_size_default()`
  - Tipe: Positif
  - Mock: env valid tanpa key `DB_POOL_SIZE`
  - Expected: `config.db_pool_size == 5` (DEFAULT_DB_POOL_SIZE)

- [ ] **3.G.10** `test_load_settings_gagal_db_pool_size_nol()`
  - Tipe: Negatif
  - Mock: env valid kecuali `DB_POOL_SIZE` = `'0'`
  - Expected: `SystemExit` code `1` (ERR-FILE-004: di luar rentang 1-100)

- [ ] **3.G.11** `test_load_settings_gagal_db_pool_size_melebihi_100()`
  - Tipe: Negatif
  - Mock: env valid kecuali `DB_POOL_SIZE` = `'200'`
  - Expected: `SystemExit` code `1` (ERR-FILE-004)

**Sub-grup G3: JWT_LIFETIME_SECONDS**

- [ ] **3.G.12** `test_load_settings_sukses_jwt_lifetime_valid()`
  - Tipe: Positif
  - Mock: env valid dengan `JWT_LIFETIME_SECONDS` = `'3600'`
  - Expected: `config.jwt_lifetime_seconds == 3600`

- [ ] **3.G.13** `test_load_settings_sukses_jwt_lifetime_default_28800()`
  - Tipe: Positif
  - Mock: env valid tanpa key `JWT_LIFETIME_SECONDS`
  - Expected: `config.jwt_lifetime_seconds == 28800` (DEFAULT_JWT_LIFETIME)

- [ ] **3.G.14** `test_load_settings_gagal_jwt_lifetime_negatif()`
  - Tipe: Negatif
  - Mock: env valid kecuali `JWT_LIFETIME_SECONDS` = `'-60'`
  - Expected: `SystemExit` code `1` (ERR-FILE-004)

- [ ] **3.G.15** `test_load_settings_gagal_jwt_lifetime_nol()`
  - Tipe: Negatif / Edge Case
  - Mock: env valid kecuali `JWT_LIFETIME_SECONDS` = `'0'`
  - Expected: `SystemExit` code `1` (harus positif, > 0)

**Sub-grup G4: PRINTER_WIDTH_MM**

- [ ] **3.G.16** `test_load_settings_sukses_printer_width_80mm()`
  - Tipe: Positif
  - Mock: env valid dengan `PRINTER_WIDTH_MM` = `'80'`
  - Expected: `config.printer_width_mm == 80`

---

#### Grup H: Test `load_settings()` — Printer Width Non-Standar & Fallback (3 skenario)

- [ ] **3.H.01** `test_load_settings_printer_width_non_standar_fallback_ke_default()`
  - Tipe: Edge Case
  - Mock: env valid kecuali `PRINTER_WIDTH_MM` = `'100'`
  - Expected: `config.printer_width_mm == 58` (fallback ke DEFAULT_PRINTER_WIDTH)

- [ ] **3.H.02** `test_load_settings_printer_width_non_standar_32mm_fallback()`
  - Tipe: Edge Case
  - Mock: env valid kecuali `PRINTER_WIDTH_MM` = `'32'`
  - Expected: `config.printer_width_mm == 58` (fallback)

- [ ] **3.H.03** `test_load_settings_printer_width_default_saat_tidak_diset()`
  - Tipe: Positif
  - Mock: env valid tanpa key `PRINTER_WIDTH_MM`
  - Expected: `config.printer_width_mm == 58` (DEFAULT_PRINTER_WIDTH)

---

#### Grup I: Test `load_settings()` — Sukses Penuh & Default Values (5 skenario)

- [ ] **3.I.01** `test_load_settings_sukses_semua_variabel_lengkap()`
  - Tipe: Positif (Golden Path)
  - Mock: env valid lengkap dari `_make_valid_env()`
  - Expected: return `AppConfig` dengan 14 field terisi benar
  - Verifikasi setiap field satu per satu:
    - `config.app_env == 'production'`
    - `config.app_cabang_id == 2`
    - `config.db_host == '192.168.1.200'`
    - `config.db_port == 3306`
    - `config.db_user == 'abucom_app'`
    - `config.db_password == 'S3cureP@ssw0rd!'`
    - `config.db_name == 'abucom_db'`
    - `config.db_pool_size == 5`
    - `config.jwt_secret_key == 'e837df26...'`
    - `config.jwt_lifetime_seconds == 28800`
    - `config.fernet_key == 'Z2VtaW5p...'`
    - `config.backup_zip_password == 'AES256EncryptBackup2026#'`
    - `config.printer_port == 'COM1'`
    - `config.printer_width_mm == 58`

- [ ] **3.I.02** `test_load_settings_sukses_return_type_adalah_appconfig()`
  - Tipe: Positif
  - Mock: env valid
  - Expected: `isinstance(config, AppConfig) is True`

- [ ] **3.I.03** `test_load_settings_sukses_menggunakan_default_values()`
  - Tipe: Positif
  - Mock: env hanya dengan 4 variabel wajib diisi, sisanya `None`/default
  - Expected: setiap field menggunakan default yang benar:
    - `app_env == 'production'` (default di `os.getenv`)
    - `app_cabang_id == 1` (DEFAULT via `_safe_int_cast`)
    - `db_host == '10.10.10.10'` (DEFAULT_DB_HOST)
    - `db_port == 3306` (DEFAULT_DB_PORT)
    - `db_user == 'abucom_app'`
    - `db_pool_size == 5` (DEFAULT_DB_POOL_SIZE)
    - `jwt_lifetime_seconds == 28800` (DEFAULT_JWT_LIFETIME)
    - `printer_port == 'COM1'`
    - `printer_width_mm == 58` (DEFAULT_PRINTER_WIDTH)

- [ ] **3.I.04** `test_load_settings_sukses_app_cabang_id_default_1()`
  - Tipe: Positif
  - Mock: env valid tanpa `APP_CABANG_ID`
  - Expected: `config.app_cabang_id == 1`

- [ ] **3.I.05** `test_load_settings_sukses_app_cabang_id_custom()`
  - Tipe: Positif
  - Mock: env valid dengan `APP_CABANG_ID` = `'5'`
  - Expected: `config.app_cabang_id == 5`

---

#### Grup J: Test Tambahan — Edge Cases & Variasi (6 skenario)

- [ ] **3.J.01** `test_load_settings_gagal_app_env_huruf_kapital()`
  - Tipe: Negatif / Edge Case
  - Mock: env valid kecuali `APP_ENV` = `'Production'` (huruf besar P)
  - Expected: `SystemExit` code `1` (case sensitive, bukan dalam VALID_APP_ENVS)

- [ ] **3.J.02** `test_load_settings_gagal_app_env_string_kosong()`
  - Tipe: Negatif / Edge Case
  - Mock: env valid kecuali `APP_ENV` = `''` (kosong, tapi bukan None)
  - Expected: `SystemExit` code `1` (ERR-FILE-005: bukan valid app env)

- [ ] **3.J.03** `test_load_settings_gagal_db_port_negatif()`
  - Tipe: Negatif
  - Mock: env valid kecuali `DB_PORT` = `'-1'`
  - Expected: `SystemExit` code `1` (ERR-FILE-004)

- [ ] **3.J.04** `test_load_settings_gagal_app_cabang_id_bukan_angka()`
  - Tipe: Negatif
  - Mock: env valid kecuali `APP_CABANG_ID` = `'cabang_a'`
  - Expected: `SystemExit` code `1` (ERR-FILE-003)

- [ ] **3.J.05** `test_load_settings_db_host_default_saat_tidak_diset()`
  - Tipe: Positif
  - Mock: env valid tanpa key `DB_HOST`
  - Expected: `config.db_host == '10.10.10.10'` (DEFAULT_DB_HOST)

- [ ] **3.J.06** `test_load_settings_db_name_default_saat_tidak_diset()`
  - Tipe: Positif
  - Mock: env valid tanpa key `DB_NAME`
  - Expected: `config.db_name == 'abucom_db'`

---

### Fase 4: Verifikasi dan Eksekusi Test

- [ ] **4.1** Pastikan seluruh skenario test di atas berjumlah **59 test functions** (6A + 7B + 7C + 3D + 8E + 4F + 16G + 3H + 5I + 6J = 65 skenario — disesuaikan berdasarkan hitungan final)
- [ ] **4.2** Jalankan perintah test:
  ```bash
  python -m pytest tests/test_settings.py -v --tb=short
  ```
- [ ] **4.3** Verifikasi semua test **PASS** (0 failures, 0 errors)
- [ ] **4.4** Jalankan coverage:
  ```bash
  python -m coverage run -m pytest tests/test_settings.py -v
  python -m coverage report -m --include="config/settings.py"
  ```
- [ ] **4.5** Verifikasi coverage `config/settings.py` ≥ **90%**
- [ ] **4.6** Jika ada test yang FAIL, debug dan perbaiki. Jangan mengubah `config/settings.py`.

---

## 6. Konvensi Penamaan Fungsi Test

Setiap fungsi test WAJIB mengikuti pola penamaan:

```
test_<nama_fungsi_target>_<behavior_spesifik_dalam_bahasa_indonesia>()
```

**Contoh:**
- `test_safe_int_cast_sukses_string_integer_valid()`
- `test_load_settings_gagal_db_password_kosong()`
- `test_validate_int_range_sukses_nilai_sama_dengan_batas_bawah()`

**Aturan tambahan:**
- Gunakan kata `sukses` untuk skenario positif
- Gunakan kata `gagal` untuk skenario negatif
- Gunakan underscore sebagai pemisah kata
- Jangan gunakan singkatan yang ambigu
- Nama harus self-documenting (bisa dipahami tanpa membaca body)

---

## 7. Konvensi Penanganan Error dalam Test

Setiap test yang mengecek `sys.exit(1)` WAJIB menggunakan pola:

```python
with pytest.raises(SystemExit) as exc_info:
    <pemanggilan fungsi>
assert exc_info.value.code == 1
```

**Jangan** menggunakan:
- `try-except SystemExit` manual
- `assert False` di dalam blok yang seharusnya raise

---

## 8. Pola Mock Standar untuk `load_settings()`

Setiap test `load_settings()` WAJIB menggunakan triple mock berikut:

```python
@patch('config.settings.Path.exists')
@patch('config.settings.load_dotenv')
@patch('config.settings.os.getenv')
def test_nama_test(mock_getenv, mock_load_dotenv, mock_exists):
    # Arrange
    mock_exists.return_value = True
    env_dict = _make_valid_env()
    # ... modifikasi env_dict sesuai skenario ...
    mock_getenv.side_effect = _mock_getenv_from_dict(env_dict)

    # Act
    config = load_settings()  # atau pytest.raises(SystemExit)

    # Assert
    ...
```

**Urutan decorator (dari bawah ke atas):**
1. `@patch('config.settings.os.getenv')` — paling bawah → parameter pertama `mock_getenv`
2. `@patch('config.settings.load_dotenv')` — tengah → parameter kedua `mock_load_dotenv`
3. `@patch('config.settings.Path.exists')` — paling atas → parameter ketiga `mock_exists`

---

## 9. Folder Penyimpanan dan Dependency

| Item | Nilai |
|------|-------|
| **File test** | `tests/test_settings.py` |
| **File target yang diuji** | `config/settings.py` |
| **Framework test** | `pytest==8.2.0` (sudah di `requirements.txt`) |
| **Coverage tool** | `coverage==7.5.1` (sudah di `requirements.txt`) |
| **Mock library** | `unittest.mock` (Standard Library, tidak perlu install) |
| **Perintah eksekusi** | `python -m pytest tests/test_settings.py -v` |
| **Perintah coverage** | `python -m coverage run -m pytest tests/test_settings.py -v && python -m coverage report -m --include="config/settings.py"` |

---

## 10. Kriteria Penyelesaian (Definition of Done)

- [ ] File `tests/test_settings.py` berisi **minimal 59 fungsi test** yang mencakup seluruh skenario di atas
- [ ] Setiap fungsi test memiliki docstring deskriptif
- [ ] Setiap fungsi test menggunakan pola Arrange-Act-Assert dengan komentar pembatas
- [ ] Fixture `clean_env` berjalan `autouse=True` untuk membersihkan state
- [ ] Semua test **PASS** tanpa failure atau error
- [ ] Coverage `config/settings.py` ≥ **90%**
- [ ] Tidak ada fungsi yang berisi `TODO` atau `pass` (semua implementasi komplit)
- [ ] Tidak ada modifikasi terhadap `config/settings.py`
- [ ] Tidak ada koneksi fisik ke database, filesystem `.env`, atau resource eksternal
- [ ] Kode test patuh terhadap Coding Standard AbuCom:
  - Header module docstring ✅
  - Import order (Standard → Third-Party → Local) ✅
  - Type hints pada fungsi publik ✅
  - snake_case naming ✅
  - Single quote untuk string internal ✅
  - Batas baris ≤ 120 karakter ✅
  - 4 spasi indentasi ✅
  - 2 baris kosong antar fungsi top-level ✅

---

## 11. Ringkasan Total Skenario Test

| Grup | Target Fungsi | Positif | Negatif | Edge Case | Validasi | Total |
|------|---------------|---------|---------|-----------|----------|-------|
| A | Konstanta & AppConfig | — | — | — | 6 | **6** |
| B | `_safe_int_cast()` | 4 | 3 | — | — | **7** |
| C | `_validate_int_range()` | 1 | 3 | 3 | — | **7** |
| D | `load_settings()` Tahap 1 | 1 | 1 | — | 1 | **3** |
| E | `load_settings()` Tahap 2 | — | 8 | — | — | **8** |
| F | `load_settings()` Tahap 3 | 2 | 2 | — | — | **4** |
| G | `load_settings()` Tahap 4 | 8 | 7 | 1 | — | **16** |
| H | Printer Width Fallback | 1 | — | 2 | — | **3** |
| I | Sukses Penuh & Defaults | 5 | — | — | — | **5** |
| J | Edge Cases Tambahan | 2 | 4 | — | — | **6** |
| | **TOTAL** | **24** | **28** | **6** | **7** | **65** |

---

## 12. Catatan Penting untuk Pelaksana

> **⚠️ PERINGATAN KRITIS:**
> 1. **JANGAN** mengubah, menambah, atau menghapus kode apapun di `config/settings.py`. Issue ini hanya untuk membuat test.
> 2. **JANGAN** membuat file `.env` fisik untuk testing. Semua data disuplai via mock `os.getenv`.
> 3. **JANGAN** meninggalkan fungsi test yang isinya `pass` atau `# TODO`. Semua harus terisi komplit.
> 4. **JANGAN** menggunakan `os.environ` langsung. Selalu gunakan `@patch('config.settings.os.getenv')`.
> 5. **PASTIKAN** setiap test bersifat idempotent — bisa dijalankan berulang kali dengan hasil konsisten.
> 6. **PASTIKAN** tidak ada test yang bergantung pada urutan eksekusi test lain.
> 7. **GUNAKAN** helper `_make_valid_env()` sebagai basis, lalu modifikasi field yang relevan per skenario.
> 8. File `tests/test_settings.py` yang sudah ada (9 test lama) akan di-**overwrite seluruhnya** dengan implementasi baru yang lebih lengkap (65 test).
