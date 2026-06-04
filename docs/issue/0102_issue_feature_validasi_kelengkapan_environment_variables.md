---
judul        : Feature Validasi Kelengkapan Environment Variables
status       : OPEN
prioritas    : HIGH
dibuat_oleh  : Claude Opus 4.6 (Thinking) — Strategi Sistem & Keamanan
tanggal      : 2026-06-04
target_branch: feature/validasi-env-variables
---

# Issue — Feature Validasi Kelengkapan Environment Variables

## 1. Persona Pelaksana

**Peran yang WAJIB diadopsi oleh AI / Programmer pelaksana issue ini:**

> **Senior Python Configuration Security Engineer & Defensive Programming Specialist**

**Justifikasi pemilihan persona:**
Fitur validasi kelengkapan environment variables merupakan garis pertahanan pertama (*first line of defense*) pada startup aplikasi AbuCom. Persona ini dipilih karena memiliki otoritas dan keahlian spesifik dalam:
- Desain validasi konfigurasi runtime yang ketat dan aman (*fail-fast startup*).
- Penanganan error defensif tanpa membocorkan informasi sensitif.
- Pemahaman mendalam terhadap ekosistem `python-dotenv`, casting tipe data, dan manajemen kredensial `.env`.
- Kepatuhan terhadap standar keamanan UU PDP No. 27/2022 dan prinsip *Least Privilege*.
- Paradigma Functional Programming (FP) murni Python 3.14.2+ tanpa class di alur bisnis.

---

## 2. Dokumen Referensi Utama

Berikut adalah daftar file referensi yang **WAJIB dibaca dan diekstrak datanya** sebelum memulai implementasi:

| No | Prioritas | Nama Dokumen | Path Relatif File | Alasan Relevansi |
|:---:|:---:|---|---|---|
| 1 | **PRIMER** | Security Design v1.2 | `docs/sdlc/03_design/06_security_design.md` | Bab 6.5 (Startup Validator `.env`), Bab 6.1 (FERNET_KEY), kode error `ERR-FILE-001`, model ancaman THR-004/THR-006, klasifikasi sensitivitas data. |
| 2 | **PRIMER** | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` | Bab 10.1 (Aturan `.env` & `python-dotenv`), kode error `ERR-FILE-001`/`002`/`003`/`004`/`005`, layout direktori, Result Pattern, Type Hints, pure FP, naming convention. |
| 3 | **PRIMER** | Environment Setup v1.2 | `docs/sdlc/04_implementation/02_environment_setup.md` | Bab 8.2 (Template `.env.example` lengkap 14 variabel), Bab 8.6 (Smoke test startup), Bab 8.2.3-8.2.5 (Generasi key), perbedaan dev vs prod. |
| 4 | **PRIMER** | Module Structure v1.2 | `docs/sdlc/04_implementation/03_module_structure.md` | Bab 8.2 (Spesifikasi `config/settings.py`), Bab 10.1 (Entry point `main.py`), aturan layer dependency, SRS-F-ADD-01. |
| 5 | **SEKUNDER** | File `.env.example` | `.env.example` | Template resmi 14 variabel konfigurasi runtime dengan komentar `[HARUS DIISI MANUAL]`. SSoT daftar variabel. |
| 6 | **SEKUNDER** | File `config/settings.py` (existing) | `config/settings.py` | Kode implementasi existing yang sudah ada dan perlu divalidasi/diperkuat. |
| 7 | **SEKUNDER** | File `config/__init__.py` (existing) | `config/__init__.py` | Re-export existing yang sudah ada. |
| 8 | **SEKUNDER** | File `main.py` (existing) | `main.py` | Entry point existing — fungsi `validate_env_file()` sudah ada tapi belum komprehensif. |
| 9 | **TERSIER** | Narasi Pemilik | `docs/sdlc/narasi.txt` | Konteks bisnis: spesifikasi Python 3.14.2+, library wajib `python-dotenv`, paradigma FP, Dual-OS (Windows 11 & Linux Debian 12). |

> **[CATATAN]**: File `narasi.txt` masih dibutuhkan sebagai referensi tersier untuk memastikan keputusan teknis sejalan dengan mandat owner (FP murni, Python 3.14.2+, Dual-OS).

---

## 3. Ekstraksi Data Relevan dari Dokumen Referensi

**INSTRUKSI untuk pelaksana**: Sebelum menulis satu baris kode pun, **WAJIB** baca dan ekstrak seluruh detail data berikut dari dokumen referensi. Jangan lewatkan detail kecil apapun.

### 3.1. Data dari Security Design v1.2 (Bab 6.5 & terkait)

Ekstrak dan rangkum informasi berikut:

- [ ] **Bab 6.5 — Startup Validator**: Layer aplikasi menjalankan verifikasi keberadaan berkas `.env` dan keaslian variabel di dalamnya saat startup program. Jika berkas hilang atau tidak lengkap, startup sistem dibatalkan secara aman dengan pesan error `ERR-FILE-001`.
- [ ] **Bab 6.5 — Kebijakan Rotasi Kredensial**: JWT Secret Key, FERNET_KEY, dan sandi database wajib dirotasi setiap 6 bulan. Rotasi hanya boleh dilakukan oleh `pemilik`.
- [ ] **Bab 6.1 — FERNET_KEY**: Enkripsi WhatsApp CRM menggunakan `cryptography.fernet` dengan kunci Fernet 32-byte dari variabel `FERNET_KEY` di `.env`.
- [ ] **Bab 4.2 — JWT_SECRET_KEY**: Kunci rahasia minimum 32 karakter heksadesimal.
- [ ] **Bab 4.2 — JWT_LIFETIME_SECONDS**: Dibatasi maksimal 28.800 detik (8 jam).
- [ ] **Model Ancaman THR-004**: Pencurian fisik server — relevan karena `.env` berisi kredensial sensitif.
- [ ] **Model Ancaman THR-006**: Pemalsuan session JWT — relevan karena `JWT_SECRET_KEY` harus kuat.
- [ ] **Kode Error Keamanan**: `ERR-FILE-001` (file `.env` tidak ditemukan), serta kode error terkait startup.

### 3.2. Data dari Coding Standard v1.2 (Bab 10.1 & terkait)

Ekstrak dan rangkum informasi berikut:

- [ ] **Bab 10.1 — Aturan `.env`**: Kredensial sensitif WAJIB disimpan di `.env`, DILARANG di-hardcode. File `.env` WAJIB masuk `.gitignore`. Sediakan `.env.example` sebagai templat.
- [ ] **Bab 10.1 — Skrip Validator Otomatis**: WAJIB mengecek kelengkapan `.env` saat startup. Jika tidak ada, startup batal dengan `ERR-FILE-001`.
- [ ] **Bab 10.1 — `APP_ENV`**: Membedakan lingkungan `development` vs `production`.
- [ ] **Bab 11.5 — Katalog Error Code**:
  - `ERR-FILE-001`: File `.env` tidak ditemukan.
  - `ERR-FILE-002`: Variabel wajib belum diisi.
  - `ERR-FILE-003`: Tipe data tidak valid (bukan integer).
  - `ERR-FILE-004`: Nilai di luar rentang yang diizinkan.
  - `ERR-FILE-005`: `APP_ENV` tidak valid.
- [ ] **Bab 2.2.6 — Result Pattern**: Logika bisnis WAJIB mengembalikan `Result` NamedTuple.
- [ ] **Bab 7 — Type Hints PEP 484**: Seluruh fungsi publik WAJIB type hints lengkap. Gunakan `|` bukan `Optional`.
- [ ] **Bab 6 — Docstring PEP 257**: Seluruh fungsi publik WAJIB docstring Google Style (Args, Returns, Raises, Example).
- [ ] **Bab 5 — Code Style**: PEP 8, indentasi 4 spasi, max 120 karakter, single quote untuk internal, double quote untuk display/docstring.
- [ ] **Bab 10.8 — System Logging**: Modul `logging` Python wajib digunakan. `development` cetak ke console, `production` simpan ke file `.log`.
- [ ] **Bab 12 — Portabilitas Lintas OS**: Wajib `pathlib`, dilarang hardcode separator, encoding UTF-8 eksplisit.

### 3.3. Data dari Environment Setup v1.2 (Bab 8.2)

Ekstrak daftar lengkap 14 variabel `.env` beserta tipe data dan aturannya:

- [ ] **Kelompok 1 — Konfigurasi Lingkungan Runtime**:
  - `APP_ENV`: String. Nilai valid: `'development'` atau `'production'`. Default: `'production'`.
  - `APP_CABANG_ID`: Integer positif. Default: `1`.
- [ ] **Kelompok 2 — Kredensial Basis Data MySQL**:
  - `DB_HOST`: String IP address. Default produksi: `'192.168.1.200'`. Contoh dev: `'localhost'`.
  - `DB_PORT`: Integer. Default: `3306`. Rentang valid: `1-65535`.
  - `DB_USER`: String. Default: `'abucom_app'`.
  - `DB_PASSWORD`: String. **WAJIB DIISI MANUAL** (bertanda `YOUR_DB_PASSWORD_HERE`).
  - `DB_NAME`: String. Default: `'abucom_db'`.
  - `DB_POOL_SIZE`: Integer. Default: `5`. Rentang valid: `1-100`.
- [ ] **Kelompok 3 — JWT Otorisasi**:
  - `JWT_SECRET_KEY`: String. **WAJIB DIISI MANUAL** (bertanda `YOUR_JWT_SECRET_KEY_HERE`). Minimum 32 karakter hex.
  - `JWT_LIFETIME_SECONDS`: Integer positif. Default: `28800` (8 jam).
- [ ] **Kelompok 4 — Enkripsi WhatsApp CRM (UU PDP)**:
  - `FERNET_KEY`: String base64 Fernet 32-byte. **WAJIB DIISI MANUAL** (bertanda `YOUR_FERNET_KEY_HERE`).
- [ ] **Kelompok 5 — Backup Terenkripsi**:
  - `BACKUP_ZIP_PASSWORD`: String. **WAJIB DIISI MANUAL** (bertanda `YOUR_BACKUP_ZIP_PASSWORD_HERE`).
- [ ] **Kelompok 6 — Printer Thermal**:
  - `PRINTER_PORT`: String. Default: `'COM1'`.
  - `PRINTER_WIDTH_MM`: Integer. Nilai valid: `58` atau `80`. Default: `58`.

### 3.4. Data dari Kode Existing (`config/settings.py`)

Pahami status implementasi saat ini:

- [ ] File `config/settings.py` sudah ada dan berisi 222 baris kode.
- [ ] NamedTuple `AppConfig` sudah terdefinisi dengan 14 field.
- [ ] Fungsi `load_settings()` sudah ada dan melakukan:
  - Validasi keberadaan file `.env`.
  - Validasi 4 variabel wajib: `DB_PASSWORD`, `JWT_SECRET_KEY`, `FERNET_KEY`, `BACKUP_ZIP_PASSWORD`.
  - Deteksi placeholder `YOUR_*`.
  - Validasi `APP_ENV` (`development`/`production`).
  - Casting integer aman via `_safe_int_cast()`.
  - Validasi range via `_validate_int_range()`.
  - Validasi `PRINTER_WIDTH_MM` (58 atau 80).
- [ ] **Yang belum ada / perlu diperkuat**:
  - Validasi panjang minimum `JWT_SECRET_KEY` (min 32 karakter hex).
  - Validasi format `FERNET_KEY` (valid base64 Fernet key).
  - Validasi format `DB_HOST` (IP address atau hostname valid).
  - Validasi `DB_PASSWORD` tidak hanya tidak kosong tapi juga memiliki kekuatan minimum.
  - Validasi `BACKUP_ZIP_PASSWORD` memiliki panjang minimum.
  - Validasi `APP_CABANG_ID` positif (> 0).
  - Validasi `DB_USER` tidak kosong.
  - Validasi `DB_NAME` tidak kosong.
  - Validasi `PRINTER_PORT` tidak kosong.
  - Pelaporan semua error sekaligus (bukan berhenti di error pertama).
  - Unit test yang komprehensif (file `tests/test_settings.py` sudah ada tapi perlu diaudit kelengkapannya).
  - Logging terstruktur sesuai standar `Coding Standard Bab 10.8`.
  - Penandaan data kosong / inkonsistensi (`[DATA-KOSONG]` marker).

### 3.5. Data dari `main.py` (Entry Point Existing)

- [ ] Fungsi `validate_env_file()` sudah ada di `main.py` baris 15-26.
- [ ] Fungsi ini **hanya** mengecek keberadaan file `.env` (menggunakan `pathlib`).
- [ ] Setelah validasi file, `main.py` memanggil `load_settings()` dari `config.settings`.
- [ ] **Duplikasi logika**: Validasi keberadaan `.env` dilakukan di 2 tempat (`main.py` DAN `config/settings.py`). Ini perlu di-refactor agar Single Responsibility.

---

## 4. Batasan, Cakupan, dan Alur Pengerjaan

### 4.1. Cakupan Issue (IN-SCOPE)

Issue ini **HANYA** mencakup:

1. **Memperkuat validasi di `config/settings.py`** — menambahkan validasi yang belum ada.
2. **Refactor `main.py`** — menghapus duplikasi logika validasi `.env` yang sudah ditangani `config/settings.py`.
3. **Menambah/memperbarui unit test di `tests/test_settings.py`** — memastikan coverage ≥ 90% untuk fungsi validasi.
4. **Memperbarui `config/__init__.py`** — jika ada fungsi/tipe data baru yang perlu di-export.

### 4.2. Di Luar Cakupan (OUT-OF-SCOPE)

Issue ini **TIDAK BOLEH** menyentuh:

- ❌ Logika bisnis di `logic/` (HPP, payroll, financial engine).
- ❌ Modul database di `db/` (db_connector, query_builder, schema_initializer, seed_data).
- ❌ Modul middleware di `middleware/` (auth_jwt, rbac_guard, audit_logger).
- ❌ Modul utilities di `utils/` (crypto, backup, text_formatter).
- ❌ Modul CLI presentasi di `cli/`.
- ❌ Isi file `.env` atau `.env.example` (jangan mengubah format/isi template ini).
- ❌ File `schema.sql`, `requirements.txt`, `.gitignore`.
- ❌ Dokumen SDLC di `docs/sdlc/`.
- ❌ File test selain `tests/test_settings.py`.

### 4.3. Alur Pengerjaan (Workflow)

```
1. Baca Referensi ──► 2. Analisis Existing ──► 3. Rancang Perubahan ──► 4. Implementasi ──► 5. Testing ──► 6. Review
```

1. **Tahap Pembacaan**: Baca semua file referensi sesuai tabel di Bab 2.
2. **Tahap Analisis**: Pahami kode existing di `config/settings.py`, `config/__init__.py`, `main.py`, dan `tests/test_settings.py`.
3. **Tahap Rancangan**: Tentukan validasi apa saja yang perlu ditambahkan/diperkuat.
4. **Tahap Implementasi**: Tulis kode perubahan satu per satu, rapi dan bersih.
5. **Tahap Testing**: Jalankan dan pastikan semua test lulus 100%.
6. **Tahap Review**: Periksa ulang kepatuhan terhadap Coding Standard.

---

## 5. Instruksi Perlindungan Feature Lain

> ⚠️ **PERINGATAN KRITIS**: Pengerjaan issue ini **TIDAK BOLEH menyentuh atau merusak feature lain**.

### 5.1. Aturan Proteksi

- [ ] **DILARANG** mengubah signature fungsi publik yang sudah di-import oleh modul lain (contoh: `load_settings()` harus tetap mengembalikan `AppConfig`).
- [ ] **DILARANG** mengubah field/urutan field pada NamedTuple `AppConfig` karena modul `main.py` dan `db/db_connector.py` sudah menggunakan field-field ini.
- [ ] **DILARANG** menambah dependensi library baru di `requirements.txt` tanpa persetujuan.
- [ ] **DILARANG** mengubah error code yang sudah terdaftar di katalog (`ERR-FILE-001` s.d `ERR-FILE-005`).
- [ ] **DILARANG** mengubah isi file `.env` atau `.env.example`.
- [ ] **DILARANG** mengubah file apapun di folder `logic/`, `db/`, `middleware/`, `utils/`, `cli/`.
- [ ] Jika menambahkan validasi baru yang bisa mem-block startup, pastikan validasi tersebut TIDAK memblokir skenario yang sebelumnya berjalan normal.

### 5.2. Cara Verifikasi Tidak Merusak Feature Lain

- [ ] Setelah implementasi, jalankan `python main.py` dengan file `.env` yang sudah ada saat ini. Pastikan startup **tetap berjalan normal** seperti sebelumnya.
- [ ] Jalankan `pytest tests/` untuk memastikan **semua test existing tetap lulus**.
- [ ] Jalankan `pytest tests/test_settings.py -v` untuk memastikan test baru juga lulus.

---

## 6. Instruksi Kualitas dan Kebersihan Pengerjaan

> **PRINSIP**: Kerjakan dengan rapi, bersih, tidak tergesa-gesa, dan tidak buru-buru. Fokus pada kualitas maksimal.

### 6.1. Standar Kualitas Kode

- [ ] Setiap fungsi baru WAJIB memiliki **docstring PEP 257 Google Style** lengkap (deskripsi, Args, Returns, Raises, Example).
- [ ] Setiap fungsi baru WAJIB memiliki **type hints PEP 484** lengkap. Gunakan `str | None` bukan `Optional[str]`.
- [ ] Setiap fungsi baru WAJIB berupa **pure function** — tidak ada efek samping selain logging dan `sys.exit()`.
- [ ] Gunakan **`pathlib`** untuk semua operasi path. Dilarang hardcode separator.
- [ ] Gunakan **`logging`** module Python untuk semua log internal. Jangan gunakan `print()` untuk debugging.
- [ ] `print()` hanya boleh digunakan untuk **pesan error yang ditampilkan ke pengguna** di terminal CLI (format `⛔ ERR-XXX-YYY: Pesan`).
- [ ] Kode harus berjalan identik di **Windows 11** dan **Linux Debian 12** tanpa modifikasi.

### 6.2. Standar Penamaan

- [ ] Fungsi: `snake_case` format `verb_noun` (contoh: `validate_jwt_key_strength()`).
- [ ] Variabel: `snake_case` deskriptif (contoh: `jwt_key_length`).
- [ ] Konstanta: `UPPER_SNAKE_CASE` (contoh: `MIN_JWT_KEY_LENGTH`).
- [ ] NamedTuple: `PascalCase` (contoh: `ValidationResult`).

### 6.3. Standar Import

```python
# 1. Standard Library
import logging
import os
import re
import sys
from collections import namedtuple
from pathlib import Path

# 2. Third-Party
from dotenv import load_dotenv

# 3. Local Modules (jika ada)
```

---

## 7. Instruksi Kelengkapan Pengerjaan

> **PRINSIP**: Pastikan kelengkapan pengerjaan issue ini agar tidak dipertanyakan dan tidak menghambat feature lain.

### 7.1. Checklist Kelengkapan Deliverable

- [ ] File `config/settings.py` sudah diperkuat dengan semua validasi yang diperlukan.
- [ ] File `main.py` sudah di-refactor untuk menghapus duplikasi validasi `.env`.
- [ ] File `config/__init__.py` sudah diperbarui jika ada export baru.
- [ ] File `tests/test_settings.py` sudah diperbarui dengan test case komprehensif.
- [ ] Semua error code mengikuti katalog resmi (`ERR-FILE-001` s.d `ERR-FILE-005`).
- [ ] Semua fungsi baru memiliki docstring dan type hints lengkap.
- [ ] Semua test lulus 100% tanpa error.
- [ ] Code coverage untuk `config/settings.py` ≥ 90%.
- [ ] Kode berjalan identik di Windows 11 dan Linux Debian 12.
- [ ] Tidak ada import yang tidak digunakan (*dead import*).
- [ ] Tidak ada variabel yang tidak digunakan (*dead variable*).

### 7.2. Skenario Test Case yang WAJIB Ada

Minimal test case berikut **WAJIB** tertulis di `tests/test_settings.py`:

**Skenario Positif (Happy Path):**
- [ ] Test load settings dengan `.env` yang lengkap dan valid → sukses, mengembalikan `AppConfig`.
- [ ] Test load settings dengan `APP_ENV=development` → sukses.
- [ ] Test load settings dengan `APP_ENV=production` → sukses.
- [ ] Test load settings dengan `PRINTER_WIDTH_MM=80` → sukses.

**Skenario Negatif (Error Path):**
- [ ] Test file `.env` tidak ada → `sys.exit(1)` dengan `ERR-FILE-001`.
- [ ] Test `DB_PASSWORD` kosong → `sys.exit(1)` dengan `ERR-FILE-002`.
- [ ] Test `JWT_SECRET_KEY` masih placeholder `YOUR_JWT_SECRET_KEY_HERE` → `sys.exit(1)` dengan `ERR-FILE-002`.
- [ ] Test `FERNET_KEY` kosong → `sys.exit(1)` dengan `ERR-FILE-002`.
- [ ] Test `BACKUP_ZIP_PASSWORD` kosong → `sys.exit(1)` dengan `ERR-FILE-002`.
- [ ] Test `DB_PORT` bernilai bukan integer (misal `'abc'`) → `sys.exit(1)` dengan `ERR-FILE-003`.
- [ ] Test `DB_POOL_SIZE` bernilai bukan integer → `sys.exit(1)` dengan `ERR-FILE-003`.
- [ ] Test `DB_PORT` bernilai di luar rentang `1-65535` (misal `0` atau `99999`) → `sys.exit(1)` dengan `ERR-FILE-004`.
- [ ] Test `DB_POOL_SIZE` bernilai di luar rentang `1-100` → `sys.exit(1)` dengan `ERR-FILE-004`.
- [ ] Test `JWT_LIFETIME_SECONDS` bernilai negatif atau nol → `sys.exit(1)` dengan `ERR-FILE-004`.
- [ ] Test `APP_ENV` bernilai invalid (misal `'staging'`) → `sys.exit(1)` dengan `ERR-FILE-005`.
- [ ] Test `PRINTER_WIDTH_MM` bernilai non-standar → fallback ke default `58` (warning, bukan error).

**Skenario Validasi Kekuatan Kunci (yang perlu ditambahkan):**
- [ ] Test `JWT_SECRET_KEY` terlalu pendek (< 32 karakter) → peringatan atau error.
- [ ] Test `FERNET_KEY` format tidak valid (bukan base64 Fernet valid) → error.

**Skenario Edge Case:**
- [ ] Test semua variabel opsional menggunakan default value → sukses.
- [ ] Test `APP_CABANG_ID` bernilai `0` atau negatif → error atau warning.
- [ ] Test variabel dengan spasi di awal/akhir → tetap berfungsi (trim/strip).

---

## 8. Penandaan Data Kosong / Inkonsistensi

**INSTRUKSI**: Jika ditemukan data yang kosong, tidak ada pada file referensi, atau ada inkonsistensi, **WAJIB ditandai** dengan komentar berikut di dalam kode:

```python
# [DATA-KOSONG] Deskripsi data yang tidak ditemukan / tidak konsisten.
# Perlu konfirmasi dari pemilik proyek untuk menentukan nilai yang benar.
```

### 8.1. Inkonsistensi yang Sudah Teridentifikasi

| No | Deskripsi Inkonsistensi | Lokasi | Status |
|:---:|---|---|:---:|
| 1 | Default `DB_HOST` di `settings.py` adalah `'10.10.10.10'`, namun di `.env.example` adalah `'192.168.1.200'`, dan di Environment Setup adalah `'192.168.1.200'`. | `config/settings.py` baris 26 | ⚠️ PERLU KONFIRMASI |
| 2 | Minimum panjang `JWT_SECRET_KEY` disebutkan "32 karakter heksadesimal" di Security Design, tapi belum divalidasi di kode. | `config/settings.py` | ⚠️ BELUM DIIMPLEMENTASI |
| 3 | Validasi format `FERNET_KEY` (apakah base64 Fernet valid) belum ada. | `config/settings.py` | ⚠️ BELUM DIIMPLEMENTASI |
| 4 | `APP_CABANG_ID` tidak divalidasi apakah bernilai positif (> 0). | `config/settings.py` | ⚠️ BELUM DIIMPLEMENTASI |
| 5 | Duplikasi logika validasi `.env` ada di `main.py` DAN `config/settings.py`. | `main.py` baris 15-26 | ⚠️ PERLU REFACTOR |

> **INSTRUKSI**: Jika menemukan inkonsistensi baru selama implementasi, tambahkan ke tabel di atas dan tandai di kode dengan marker `[DATA-KOSONG]`.

---

## 9. Instruksi Tambahan (Best Practice Spesifik)

### 9.1. Validasi Fail-Fast vs Fail-Aggregated

**Rekomendasi arsitektural**: Saat ini `load_settings()` menghentikan eksekusi pada error pertama (`sys.exit(1)`). Pertimbangkan untuk mengumpulkan **semua error validasi terlebih dahulu** sebelum menampilkannya sekaligus, agar pengguna tidak perlu memperbaiki satu error, menjalankan ulang, menemukan error berikutnya, dst.

```python
# Contoh pendekatan fail-aggregated:
errors = []

if not env_path.exists():
    errors.append("ERR-FILE-001: File .env tidak ditemukan.")

for var_name in REQUIRED_ENV_VARS:
    value = os.getenv(var_name, '')
    if not value or value.startswith('YOUR_'):
        errors.append(f"ERR-FILE-002: Variabel {var_name} belum diisi di file .env.")

if errors:
    for err in errors:
        print(f"⛔ {err}")
    sys.exit(1)
```

> **[KEPUTUSAN DESAIN]**: Pelaksana BOLEH memilih salah satu pendekatan (fail-fast ATAU fail-aggregated). Jika memilih fail-aggregated, pastikan error `ERR-FILE-001` (file tidak ditemukan) tetap berhenti segera karena variabel tidak akan bisa di-load sama sekali.

### 9.2. Validasi Kekuatan JWT_SECRET_KEY

Sesuai Security Design Bab 4.2, `JWT_SECRET_KEY` harus minimum 32 karakter hex. Tambahkan validasi:

```python
MIN_JWT_KEY_LENGTH = 32

jwt_key = os.getenv('JWT_SECRET_KEY', '')
if len(jwt_key) < MIN_JWT_KEY_LENGTH:
    _logger.warning(
        f"JWT_SECRET_KEY terlalu pendek ({len(jwt_key)} karakter). "
        f"Minimum {MIN_JWT_KEY_LENGTH} karakter untuk keamanan optimal."
    )
    # Di production: wajib exit. Di development: warning saja.
    if app_env == 'production':
        errors.append(f"ERR-FILE-006: JWT_SECRET_KEY terlalu pendek di lingkungan production.")
```

> **[CATATAN]**: Error code `ERR-FILE-006` belum ada di katalog resmi. Jika pelaksana menambahkan error code baru, **WAJIB** gunakan prefix `ERR-FILE-` dan nomor urut setelah `005`. Tandai sebagai `[DATA-KOSONG]` jika katalog resmi belum mencakup kode ini.

### 9.3. Validasi Format FERNET_KEY

FERNET_KEY harus valid Fernet key (base64 URL-safe 32-byte). Tambahkan validasi:

```python
def _validate_fernet_key(fernet_key: str) -> bool:
    """Memvalidasi apakah string FERNET_KEY valid sebagai kunci Fernet.

    Args:
        fernet_key (str): String kunci Fernet dari file .env.

    Returns:
        bool: True jika kunci valid, False jika tidak.
    """
    try:
        from cryptography.fernet import Fernet
        Fernet(fernet_key.encode('utf-8'))
        return True
    except Exception:
        return False
```

### 9.4. Handling Sensitive Data di Log

**PERINGATAN KEAMANAN**: Saat logging error validasi, **DILARANG KERAS** mencetak/log nilai aktual dari variabel sensitif berikut:
- `DB_PASSWORD`
- `JWT_SECRET_KEY`
- `FERNET_KEY`
- `BACKUP_ZIP_PASSWORD`

Hanya boleh log **nama variabel** dan **jenis error**, bukan nilainya.

```python
# ❌ DILARANG:
_logger.error(f"DB_PASSWORD bernilai '{db_password}' — terlalu lemah!")

# ✅ BENAR:
_logger.error("ERR-FILE-002: Variabel DB_PASSWORD belum diisi di file .env.")
```

### 9.5. Kesesuaian dengan Paradigma FP

- Semua fungsi validasi baru **WAJIB pure function** (kecuali yang memang perlu I/O seperti `sys.exit()` dan `logging`).
- **DILARANG** membuat `class` untuk validasi. Gunakan fungsi biasa dan `namedtuple`.
- Semua data intermediary menggunakan **immutable structure** (tuple, namedtuple, frozenset).

### 9.6. Portabilitas Dual-OS

- Semua path menggunakan `pathlib.Path`.
- Semua file operation menggunakan `encoding='utf-8'` eksplisit.
- Jangan ada logika yang bergantung pada OS tertentu (Windows/Linux) di modul `config/`.

---

## 10. Checklist Implementasi Detail (Low-Level Step-by-Step)

Berikut adalah tahapan implementasi yang WAJIB diikuti secara berurutan. Tandai setiap item dengan `[x]` setelah selesai.

### Fase A: Persiapan dan Pembacaan Referensi

- [ ] **A.1.** Baca file `docs/sdlc/03_design/06_security_design.md` — fokus pada Bab 2.2 (THR-004, THR-006), Bab 4.2 (JWT), Bab 6.1 (Fernet), Bab 6.5 (Startup Validator).
- [ ] **A.2.** Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — fokus pada Bab 2.2.6 (Result Pattern), Bab 3 (Naming), Bab 5 (Code Style), Bab 6 (Docstrings), Bab 7 (Type Hints), Bab 10.1 (`.env` Rules), Bab 10.8 (Logging), Bab 11.5 (Error Codes), Bab 12 (Cross-OS).
- [ ] **A.3.** Baca file `docs/sdlc/04_implementation/02_environment_setup.md` — fokus pada Bab 8.2 (Template `.env.example`), Bab 8.2.3-8.2.5 (Key generation), Bab 8.6 (Smoke test).
- [ ] **A.4.** Baca file `docs/sdlc/04_implementation/03_module_structure.md` — fokus pada Bab 8.2 (`config/settings.py` spec), Bab 10.1 (`main.py` spec).
- [ ] **A.5.** Baca file `.env.example` untuk mendapatkan daftar lengkap 14 variabel.
- [ ] **A.6.** Baca file `docs/sdlc/narasi.txt` — catat mandat FP, Python 3.14.2+, Dual-OS.
- [ ] **A.7.** Baca file `config/settings.py` secara menyeluruh — catat semua validasi yang sudah ada.
- [ ] **A.8.** Baca file `config/__init__.py` — catat export yang sudah ada.
- [ ] **A.9.** Baca file `main.py` secara menyeluruh — catat fungsi `validate_env_file()` dan alur startup.
- [ ] **A.10.** Baca file `tests/test_settings.py` secara menyeluruh — catat test case yang sudah ada dan yang belum ada.

### Fase B: Analisis Gap (Identifikasi Yang Perlu Ditambahkan)

- [ ] **B.1.** Buat daftar validasi yang SUDAH ADA di `config/settings.py`.
- [ ] **B.2.** Buat daftar validasi yang BELUM ADA namun PERLU ADA berdasarkan dokumen referensi.
- [ ] **B.3.** Identifikasi duplikasi logika antara `main.py` dan `config/settings.py`.
- [ ] **B.4.** Identifikasi test case yang SUDAH ADA di `tests/test_settings.py`.
- [ ] **B.5.** Buat daftar test case yang PERLU DITAMBAHKAN (lihat Bab 7.2 issue ini).
- [ ] **B.6.** Catat semua inkonsistensi data yang ditemukan (tambahkan ke tabel Bab 8.1).

### Fase C: Implementasi Perubahan `config/settings.py`

- [ ] **C.1.** Tambahkan konstanta baru yang diperlukan di bagian atas file:
  ```python
  MIN_JWT_KEY_LENGTH = 32
  MIN_BACKUP_PASSWORD_LENGTH = 8
  ```
- [ ] **C.2.** Tambahkan fungsi validasi baru `_validate_fernet_key(fernet_key: str) -> bool`:
  - Validasi apakah string FERNET_KEY valid sebagai kunci Fernet.
  - Gunakan `cryptography.fernet.Fernet` untuk validasi.
  - Kembalikan `bool`.
  - Tambahkan docstring PEP 257 lengkap.
  - Tambahkan type hints lengkap.
- [ ] **C.3.** Tambahkan fungsi validasi baru `_validate_jwt_key_strength(jwt_key: str, app_env: str) -> None`:
  - Validasi minimum 32 karakter.
  - Di production: error fatal. Di development: warning.
  - Tambahkan docstring PEP 257 lengkap.
  - Tambahkan type hints lengkap.
- [ ] **C.4.** Perkuat fungsi `load_settings()` — tambahkan di dalamnya:
  - [ ] **C.4.1.** Validasi `APP_CABANG_ID` harus positif (> 0).
  - [ ] **C.4.2.** Validasi `DB_USER` tidak kosong.
  - [ ] **C.4.3.** Validasi `DB_NAME` tidak kosong.
  - [ ] **C.4.4.** Validasi panjang `JWT_SECRET_KEY` minimal 32 karakter (di production).
  - [ ] **C.4.5.** Validasi format `FERNET_KEY` menggunakan `_validate_fernet_key()`.
  - [ ] **C.4.6.** Validasi `BACKUP_ZIP_PASSWORD` memiliki panjang minimum.
  - [ ] **C.4.7.** Validasi `PRINTER_PORT` tidak kosong.
  - [ ] **C.4.8.** Perbaiki default `DB_HOST` dari `'10.10.10.10'` menjadi `'192.168.1.200'` agar konsisten dengan `.env.example` dan Environment Setup, **ATAU** tandai dengan `[DATA-KOSONG]` jika belum yakin.
- [ ] **C.5.** Pastikan semua pesan error menggunakan format standar: `⛔ ERR-FILE-XXX: Pesan deskriptif bahasa Indonesia`.
- [ ] **C.6.** Pastikan tidak ada nilai sensitif yang dicetak/log.
- [ ] **C.7.** Pastikan semua komentar existing dipertahankan (jangan hapus komentar yang tidak relevan dengan perubahan ini).
- [ ] **C.8.** Pastikan header module docstring diperbarui (tanggal dan deskripsi perubahan).

### Fase D: Refactor `main.py`

- [ ] **D.1.** Hapus fungsi `validate_env_file()` dari `main.py` (baris 15-26).
- [ ] **D.2.** Hapus pemanggilan `if not validate_env_file():` dari fungsi `main()` (baris 43-45).
- [ ] **D.3.** Biarkan validasi keberadaan `.env` sepenuhnya ditangani oleh `config/settings.py` → `load_settings()`.
- [ ] **D.4.** Pastikan alur startup di `main.py` tetap berfungsi normal:
  ```
  main() → load_settings() → create_connection_pool() → ...
  ```
- [ ] **D.5.** Perbarui komentar/docstring di `main.py` yang menyebutkan `validate_env_file()`.
- [ ] **D.6.** Jangan ubah apapun selain yang berkaitan dengan penghapusan duplikasi validasi `.env`.

### Fase E: Perbarui `config/__init__.py`

- [ ] **E.1.** Periksa apakah ada fungsi atau tipe data baru yang perlu di-export.
- [ ] **E.2.** Jika ada, tambahkan ke baris import di `config/__init__.py`.
- [ ] **E.3.** Jika tidak ada perubahan yang diperlukan, biarkan file ini apa adanya.

### Fase F: Implementasi/Perbarui Unit Test `tests/test_settings.py`

- [ ] **F.1.** Baca file existing `tests/test_settings.py` untuk memahami test yang sudah ada.
- [ ] **F.2.** Tambahkan test case untuk setiap skenario di Bab 7.2 yang belum ada.
- [ ] **F.3.** Setiap fungsi test WAJIB menggunakan pola penamaan: `test_<behavior_spesifik>()`.
- [ ] **F.4.** Gunakan `monkeypatch` atau `tmp_path` fixture pytest untuk meng-mock file `.env`.
- [ ] **F.5.** Gunakan `pytest.raises(SystemExit)` untuk menguji skenario `sys.exit(1)`.
- [ ] **F.6.** Pastikan test bersifat deterministik dan terisolasi (tidak bergantung pada file `.env` riil).
- [ ] **F.7.** Pastikan test tidak melakukan koneksi database riil.
- [ ] **F.8.** Tambahkan docstring pada setiap fungsi test yang menjelaskan skenario yang diuji.

### Fase G: Verifikasi dan Review Akhir

- [ ] **G.1.** Jalankan `python main.py` dengan file `.env` yang sudah ada → pastikan startup normal.
- [ ] **G.2.** Jalankan `pytest tests/test_settings.py -v` → pastikan semua test lulus 100%.
- [ ] **G.3.** Jalankan `pytest tests/ -v` → pastikan semua test di seluruh proyek tetap lulus.
- [ ] **G.4.** Jalankan `coverage run -m pytest tests/test_settings.py && coverage report -m --include="config/settings.py"` → pastikan coverage ≥ 90%.
- [ ] **G.5.** Review manual: periksa setiap fungsi baru memiliki docstring dan type hints.
- [ ] **G.6.** Review manual: periksa tidak ada import yang tidak digunakan.
- [ ] **G.7.** Review manual: periksa tidak ada variabel sensitif yang di-log/print.
- [ ] **G.8.** Review manual: periksa semua pesan error berbahasa Indonesia sesuai format standar.
- [ ] **G.9.** Review manual: periksa kode berjalan di Windows 11 DAN Linux Debian 12 (gunakan `pathlib`, bukan hardcode path separator).
- [ ] **G.10.** Pastikan semua file yang diubah telah diformat sesuai PEP 8 (indentasi 4 spasi, max 120 karakter per baris).
- [ ] **G.11.** Tandai `[DATA-KOSONG]` pada semua data yang masih belum pasti.

### Fase H: Git Commit

- [ ] **H.1.** `git add config/settings.py config/__init__.py main.py tests/test_settings.py`
- [ ] **H.2.** `git commit -m "feat: perkuat validasi kelengkapan environment variables (.env) pada startup"`
- [ ] **H.3.** Pastikan commit message mengikuti Conventional Commits format.

---

## 11. Ringkasan File yang Akan Dimodifikasi

| No | File Target | Aksi | Deskripsi Perubahan |
|:---:|---|:---:|---|
| 1 | `config/settings.py` | **MODIFY** | Tambah validasi kekuatan JWT key, format Fernet key, cabang_id positif, db_user/db_name/printer_port tidak kosong, panjang backup password. |
| 2 | `main.py` | **MODIFY** | Hapus duplikasi fungsi `validate_env_file()` dan pemanggilannya. |
| 3 | `config/__init__.py` | **MODIFY (jika perlu)** | Tambah export baru jika ada. |
| 4 | `tests/test_settings.py` | **MODIFY** | Tambah test case komprehensif untuk semua validasi baru dan existing. |

---

## 12. Referensi Cepat Error Code

| Kode Error | Deskripsi | Pemicu |
|---|---|---|
| `ERR-FILE-001` | File `.env` tidak ditemukan di root proyek. | `load_settings()` — file check |
| `ERR-FILE-002` | Variabel wajib belum diisi di file `.env`. | `load_settings()` — empty/placeholder check |
| `ERR-FILE-003` | Variabel bernilai bukan integer valid. | `_safe_int_cast()` — type check |
| `ERR-FILE-004` | Variabel bernilai di luar rentang yang diizinkan. | `_validate_int_range()` — range check |
| `ERR-FILE-005` | `APP_ENV` bernilai tidak valid. | `load_settings()` — enum check |

---

*Issue ini disusun oleh Claude Opus 4.6 (Thinking) — Strategi Sistem & Keamanan, berdasarkan analisis komprehensif terhadap 9 dokumen referensi SDLC AbuCom dan kode existing. Tanggal: 2026-06-04.*
