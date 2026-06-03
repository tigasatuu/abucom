---
judul      : Scaffolding Project
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
prioritas  : 🔴 CRITICAL (Blocker — Prasyarat Mutlak Sebelum Pengkodean Modul)
status     : Open
assignee   : GPT-OSS 120B (Medium) — STK-014 (Boilerplate & Dummy Data Provider)
reviewer   : Gemini 3 Flash — STK-011 (Automated Reviewer & Debugger)
approver   : Junior Programmer — STK-000 (Owner & Release Manager)
tanggal    : 2026-06-03
estimasi   : 2-3 jam kerja fokus
branch     : `chore/scaffolding-project`
---

# Issue — Scaffolding Project

## 1. Ringkasan Issue

Issue ini bertujuan untuk membangun kerangka awal (scaffolding) seluruh struktur direktori, file-file boilerplate, file konfigurasi dasar, dan file entry point proyek **AbuCom** sesuai dengan blueprint yang telah didefinisikan secara resmi di dalam dokumen-dokumen SDLC Fase 03 (Design) dan Fase 04 (Implementation). Scaffolding ini merupakan **prasyarat mutlak (blocker)** yang harus diselesaikan sebelum tim pengembang AI lainnya dapat memulai pengerjaan modul fungsional (M.1 — M.10).

> ⚠️ **PERINGATAN KRITIS**: Issue ini bersifat **fondasi arsitektural**. Kesalahan pada scaffolding (salah nama file, salah lokasi folder, salah format boilerplate) akan **berdampak cascading** ke seluruh modul dan seluruh issue berikutnya. Kerjakan dengan **rapi, bersih, tidak tergesa-gesa, dan tidak buru-buru**. Pastikan setiap detail kecil sesuai standar.

---

## 2. Persona AI yang Ditugaskan

**Persona**: `Senior Project Scaffolding Engineer & Boilerplate Architect`

**Deskripsi Persona**: Kamu adalah seorang insinyur arsitektur proyek senior yang sangat teliti, disiplin, dan berorientasi pada kualitas. Kamu bertanggung jawab untuk membangun fondasi struktural proyek dengan presisi absolut. Kamu memahami bahwa setiap file, setiap folder, setiap baris boilerplate yang kamu tulis akan menjadi pondasi bagi seluruh tim pengembang AI lainnya. Kamu tidak pernah terburu-buru, kamu selalu memverifikasi ulang setiap hasil kerjamu terhadap dokumen referensi sebelum melanjutkan ke langkah berikutnya.

**Sifat yang WAJIB dimiliki**:
- **Sangat Teliti**: Tidak melewatkan satupun file atau folder dari blueprint.
- **Patuh Standar**: Mengikuti setiap aturan penamaan, format, dan konvensi dari Coding Standard secara harfiah.
- **Tidak Tergesa-gesa**: Mengerjakan secara bertahap dan memverifikasi setiap tahap.
- **Komunikatif**: Menandai setiap data yang kosong atau ambigu agar bisa ditindaklanjuti.

---

## 3. Dokumen Referensi Utama

Berikut adalah daftar dokumen SDLC yang menjadi **dasar utama (Source of Truth)** untuk pengerjaan issue ini. Baca dan ekstrak seluruh detail yang relevan dari setiap dokumen sebelum memulai implementasi.

| Prioritas | Dokumen Referensi | Path File | Bagian yang Relevan |
|:---------:|:------------------|:----------|:--------------------|
| **PRIMER** | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` | Bab 4 (Struktur Direktori Proyek), Bab 3 (Konvensi Penamaan), Bab 6 (Docstrings & Header Module), Bab 13 (Dependensi), Bab 15 (Git) |
| **PRIMER** | Environment Setup v1.2 | `docs/sdlc/04_implementation/02_environment_setup.md` | Bab 8 (Konfigurasi Proyek Aplikasi: .env.example, .gitignore, requirements.txt, struktur direktori, smoke test) |
| **PRIMER** | Module Structure v1.2 | `docs/sdlc/04_implementation/03_module_structure.md` | Bab 3 (Layout Direktori Lengkap), Bab 4–9 (Spesifikasi setiap file .py), Bab 10 (Entry Point & Root Files) |
| **PRIMER** | Git Workflow v1.2 | `docs/sdlc/04_implementation/04_git_workflow.md` | Bab 3.5 (Inisialisasi Repository), Bab 3.6 (.gitignore lengkap), Bab 3.7 (.gitattributes) |
| **SEKUNDER** | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` | Arsitektur 4-layer, connection pool `abupool` |
| **SEKUNDER** | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | Spesifikasi bcrypt, JWT, Fernet, RBAC |
| **TERSIER** | Narasi Pemilik | `docs/sdlc/narasi.txt` | Konteks bisnis umum, susunan tim AI |

> **Catatan**: File `narasi.txt` masih dibutuhkan sebagai referensi konteks bisnis umum untuk memastikan scaffolding mencakup seluruh aspek layanan yang disebutkan pemilik usaha.

---

## 4. Rangkuman Detail Data dari Dokumen Referensi

Berikut adalah **ekstraksi lengkap** seluruh detail data yang relevan dari dokumen referensi untuk pengerjaan scaffolding:

### 4.1. Struktur Direktori Standar (Sumber: Coding Standard Bab 4.1 & Module Structure Bab 3.1)

```
abucom/
│
├── main.py                     # Entry point peluncuran aplikasi CLI
├── requirements.txt            # Dependensi library versi terkunci
├── .env.example                # Templat konfigurasi rahasia program
├── .gitignore                  # Berkas pengabaian version control Git
├── .gitattributes              # Atribusi line ending Dual-OS
│
├── cli/                        # LAYER 1: PRESENTATION (Visual & Menus)
│   ├── __init__.py             # Expose fungsi menu utama
│   ├── dashboard.py            # Menus dashboard harian per role (M.7)
│   ├── menu_transaksi.py       # Interaksi Modul M.1 & M.8 (CRM)
│   ├── menu_inventaris.py      # Interaksi Modul M.2 & M.5 (Antrian)
│   ├── menu_ppob_service.py    # Interaksi Modul M.3
│   ├── menu_sdm_finansial.py   # Interaksi Modul M.4 & M.6 (Pinjaman)
│   ├── menu_laporan.py         # Interaksi Modul M.9 (Laporan Keuangan)
│   └── menu_configs.py         # Interaksi Modul M.10 (Configs)
│
├── logic/                      # LAYER 2: BUSINESS LOGIC (Pure FP Python)
│   ├── __init__.py
│   ├── bom_hpp.py              # Logika kalkulasi HPP desimal (M.2)
│   ├── smart_payroll.py        # Logika payroll & komisi poin (M.4)
│   ├── financial_engine.py     # Logika pinjaman & laba rugi (M.6)
│   ├── financial_reporter.py   # Logika agregasi laporan keuangan (M.9)
│   └── safety_validator.py     # Logika sanitasi input & checks
│
├── db/                         # LAYER 3: DATA ACCESS (SQL Engine)
│   ├── __init__.py
│   ├── db_connector.py         # Connection pooling & base connection
│   └── query_builder.py        # Parameterized transactional wrappers
│
├── middleware/                 # CROSS-CUTTING CONCERNS (Sec & Log)
│   ├── __init__.py
│   ├── auth_jwt.py             # Security logic otentikasi & JWT Sesi
│   ├── rbac_guard.py           # Otorisasi Level Menu & Action Guard
│   └── audit_logger.py         # Perekaman kronologis database JSON
│
├── config/                     # PENGELOLAAN KONFIGURASI RUNTIME
│   ├── __init__.py
│   └── settings.py             # Agregasi & casting variables berkas .env
│
├── utils/                      # PUSTAKA UTAS (Helper Functions)
│   ├── __init__.py
│   ├── crypto.py               # Helper bcrypt password hash
│   ├── backup.py               # Utilitas backup zip AES-256
│   └── text_formatter.py       # Formatting thermal struk & rich tables
│
├── exports/                    # DIREKTORI KELUARAN FILE LOKAL
│   ├── backups/                # Hasil backup database .zip terenkripsi
│   │   └── .gitkeep
│   ├── designs/                # Mockup file PDF desain pelanggan
│   │   └── .gitkeep
│   └── receipts/               # Berkas cetak nota struk .txt
│       └── .gitkeep
│
└── tests/                      # AUTOMATED UNIT & INTEGRATION TESTING
    ├── __init__.py
    ├── test_bom_hpp.py         # Unit testing pure functions kalkulasi
    └── test_rbac_security.py   # Integration testing otorisasi RBAC
```

### 4.2. Daftar Dependensi Versi Terkunci (Sumber: Coding Standard Bab 13.2–13.3 & Environment Setup Bab 7.3)

**Wajib (Mandatory)**:
```
mysql-connector-python==8.4.0
python-dotenv==1.0.1
bcrypt==4.1.0
pyjwt==2.8.0
cryptography==42.0.5
```

**Rekomendasi (Visual CLI)**:
```
rich==13.7.0
tabulate==0.9.0
```

**Development Only**:
```
pytest==8.2.0
coverage==7.5.1
```

### 4.3. Template .env.example (Sumber: Environment Setup Bab 8.2.1)

```ini
# ==============================================================================
# TEMPLAT KONFIGURASI RUNTIME ABUCOM - .env.example
# Salin file ini menjadi '.env' di folder proyek kasir dan isi nilainya.
# ==============================================================================

# 1. Konfigurasi Lingkungan Runtime
APP_ENV=production
APP_CABANG_ID=1

# 2. Kredensial Basis Data MySQL Server
DB_HOST=10.10.10.10
DB_PORT=3306
DB_USER=abucom_app
# [HARUS DIISI MANUAL] Isi dengan password user abucom_app yang kuat.
DB_PASSWORD=YOUR_DB_PASSWORD_HERE
DB_NAME=abucom_db
DB_POOL_SIZE=5

# 3. Kunci Rahasia Otorisasi Sesi JWT (HS256)
# [HARUS DIISI MANUAL] Hasilkan kunci dengan: python -c "import secrets; print(secrets.token_hex(32))"
JWT_SECRET_KEY=YOUR_JWT_SECRET_KEY_HERE
JWT_LIFETIME_SECONDS=28800

# 4. Kunci Enkripsi WhatsApp CRM Pelanggan (Fernet Cryptography)
# [HARUS DIISI MANUAL] Hasilkan kunci dengan: python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode('utf-8'))"
FERNET_KEY=YOUR_FERNET_KEY_HERE

# 5. Konfigurasi Pencadangan Database Terenkripsi AES-256
# [HARUS DIISI MANUAL] Hasilkan kata sandi acak kuat.
BACKUP_ZIP_PASSWORD=YOUR_BACKUP_ZIP_PASSWORD_HERE

# 6. Konfigurasi Printer Thermal Nota Toko
# Nama COM port (Windows) atau berkas port (Linux) printer
PRINTER_PORT=COM1
PRINTER_WIDTH_MM=58
```

### 4.4. Template .gitignore Lengkap (Sumber: Git Workflow Bab 3.6)

```
# ==============================================================================
# KONFIGURASI PENGABAIAN GIT ABUCOM
# ==============================================================================

# 1. Konfigurasi Rahasia & Kredensial (KEAMANAN SANGAT SENSITIF)
.env
.env.test

# 2. Python Cache, Compiler & Runtime Environments
__pycache__/
*.pyc
*.pyo
*.pyd
.pytest_cache/
.coverage
htmlcov/
venv/
ENV/
pip_wheels/

# 3. Hasil Backup, Desain, Struk Kasir Lokal & Handover Notes
exports/backups/*
exports/designs/*
exports/receipts/*
exports/handover/*
!exports/backups/.gitkeep
!exports/designs/.gitkeep
!exports/receipts/.gitkeep
!exports/handover/.gitkeep

# 4. Berkas Temporary Sistem Operasi & IDE
Thumbs.db
Desktop.ini
.DS_Store
.vscode/
.idea/
*.log
*.bak
```

### 4.5. Template .gitattributes (Sumber: Git Workflow Bab 3.7)

```
# ==============================================================================
# ATRIBUSI LINE ENDING DUAL-OS ABUCOM
# ==============================================================================

# Atur default penanganan teks secara otomatis
* text=auto

# Paksa file Python, Markdown, SQL, dan Teks menggunakan line-feed (LF) khas Linux
*.py text eol=lf
*.md text eol=lf
*.sql text eol=lf
*.txt text eol=lf

# Paksa file batch script Windows menggunakan carriage-return + line-feed (CRLF)
*.bat text eol=crlf
*.cmd text eol=crlf
```

### 4.6. Template Header Module Python (Sumber: Coding Standard Bab 6.4)

```python
"""
Nama Modul: <nama_file.py>
Deskripsi: <Deskripsi singkat tujuan modul ini — 1-2 kalimat>.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""
```

### 4.7. Template Result Pattern (Sumber: Coding Standard Bab 2.2.6)

```python
from collections import namedtuple

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
```

### 4.8. Konvensi Penamaan (Sumber: Coding Standard Bab 3)

| Entitas Kode | Aturan Format | Contoh Benar |
|:-------------|:--------------|:-------------|
| Direktori/Berkas | `snake_case` | `logic/bom_hpp.py` |
| Fungsi | `snake_case` (verb_noun) | `hitung_gaji_bersih()` |
| Variabel/Parameter | `snake_case` | `sisa_utang_kasbon` |
| Konstanta | `UPPER_SNAKE_CASE` | `JWT_SECRET_KEY` |
| NamedTuple / Dataclass | `PascalCase` | `TransactionRecord` |

---

## 5. Batasan, Cakupan, dan Alur Pengerjaan

### 5.1. Cakupan Issue (Scope — Yang HARUS Dikerjakan)

- [x] Pembuatan seluruh struktur folder/direktori sesuai blueprint.
- [x] Pembuatan seluruh file `.py` kosong dengan header module docstring dan boilerplate minimal.
- [x] Pembuatan seluruh file `__init__.py` pada setiap package Python.
- [x] Pembuatan file `.gitkeep` pada direktori output kosong (`exports/`).
- [x] Pembuatan file `requirements.txt` dengan versi terkunci.
- [x] Pembuatan file `.env.example` dengan template lengkap.
- [x] Pembuatan file `.gitignore` sesuai standar Git Workflow.
- [x] Pembuatan file `.gitattributes` untuk Dual-OS line ending.
- [x] Pembuatan file `main.py` sebagai entry point dengan startup boilerplate.
- [x] Pembuatan file `config/settings.py` dengan boilerplate pembacaan `.env`.
- [x] Pembuatan file `db/db_connector.py` dengan boilerplate connection pool factory.
- [x] Pembuatan file `logic/safety_validator.py` dengan boilerplate sanitasi input.
- [x] Pembuatan file `middleware/auth_jwt.py` dengan boilerplate fungsi stub bcrypt & JWT.
- [x] Pembuatan file `middleware/rbac_guard.py` dengan boilerplate decorator RBAC.
- [x] Pembuatan file `middleware/audit_logger.py` dengan boilerplate fungsi stub audit trail.
- [x] Pembuatan file `utils/crypto.py` dengan boilerplate fungsi stub Fernet encrypt/decrypt.
- [x] Pembuatan file `tests/` dengan boilerplate test stub minimal.

### 5.2. Di Luar Cakupan (Out-of-Scope — Yang TIDAK BOLEH Dikerjakan)

> ⚠️ **PERINGATAN**: Jangan melampaui batasan berikut. Fokus hanya pada scaffolding.

- ❌ Implementasi logika bisnis lengkap (itu tugas issue berikutnya oleh tim AI spesialis).
- ❌ Pengerjaan koneksi database riil ke server MySQL (hanya boilerplate factory).
- ❌ Pengisian data seed (`seed.sql`) atau migrasi schema (`schema.sql`).
- ❌ Implementasi menu CLI interaktif lengkap (hanya stub placeholder).
- ❌ Pembuatan unit test lengkap (hanya file stub kosong dengan 1 test placeholder).
- ❌ Konfigurasi virtual environment (`venv/`) — itu sudah diatur di Environment Setup.
- ❌ Modifikasi file apapun di folder `docs/` (dokumentasi SDLC sudah final).

### 5.3. Alur Pengerjaan (Workflow)

```
1. Baca & Pahami Referensi
         │
         v
2. Buat Branch: chore/scaffolding-project
         │
         v
3. Buat Struktur Direktori (folder kosong dulu)
         │
         v
4. Buat File Konfigurasi Root (.env.example, .gitignore, .gitattributes, requirements.txt)
         │
         v
5. Buat File Entry Point (main.py)
         │
         v
6. Buat File Boilerplate per Layer (config → db → middleware → utils → logic → cli → tests)
         │
         v
7. Buat File .gitkeep di exports/
         │
         v
8. Verifikasi Kelengkapan (cek semua file vs blueprint)
         │
         v
9. Commit Atomis per Layer + Push ke Server LAN
         │
         v
10. Quality Gate Review oleh Gemini 3 Flash (STK-011)
```

---

## 6. Instruksi Implementasi Detail (Low-Level Checklist)

### ⚙️ TAHAP 0 — Pembacaan dan Pemahaman Referensi

> **Tujuan**: Pastikan kamu memahami seluruh standar sebelum menulis satu baris kode pun.

- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` secara **keseluruhan**. Fokus pada:
  - [ ] Bab 4.1 — Layout Direktori Standar (catat setiap nama file dan folder).
  - [ ] Bab 3 — Konvensi Penamaan (catat aturan snake_case, PascalCase, UPPER_SNAKE_CASE).
  - [ ] Bab 6.4 — Template Header File Module Docstring.
  - [ ] Bab 2.2.6 — Template Result Pattern NamedTuple.
  - [ ] Bab 13.2–13.3 — Daftar Dependensi Wajib + Rekomendasi.
  - [ ] Bab 16 — Daftar 10 Larangan Mutlak (jangan langgar satupun).
- [ ] Baca file `docs/sdlc/04_implementation/02_environment_setup.md`. Fokus pada:
  - [ ] Bab 8.1 — Struktur Direktori (bandingkan dengan Coding Standard, ambil yang paling lengkap).
  - [ ] Bab 8.2 — Template `.env.example` lengkap.
  - [ ] Bab 8.5 — Konfigurasi `.gitignore`.
  - [ ] Bab 15.3 — Template `requirements.txt`.
- [ ] Baca file `docs/sdlc/04_implementation/03_module_structure.md`. Fokus pada:
  - [ ] Bab 3.1 — Diagram Tree Direktori (ini adalah blueprint **utama** untuk scaffolding).
  - [ ] Bab 4 s.d 9 — Spesifikasi setiap file .py (catat nama fungsi publik dan signature).
  - [ ] Bab 10 — Entry Point `main.py` dan file root.
- [ ] Baca file `docs/sdlc/04_implementation/04_git_workflow.md`. Fokus pada:
  - [ ] Bab 3.5 — Inisialisasi Repository & baseline commit.
  - [ ] Bab 3.6 — Template `.gitignore` lengkap (ini versi paling lengkap, gunakan ini).
  - [ ] Bab 3.7 — Template `.gitattributes`.
  - [ ] Bab 5 — Konvensi commit message (untuk commit scaffolding nanti).
- [ ] Baca file `docs/sdlc/narasi.txt` untuk memahami konteks bisnis umum pemilik usaha.

> 🚩 **PENTING**: Jika ada perbedaan antara dokumen (misal nama file berbeda antara Coding Standard dan Module Structure), **prioritaskan Module Structure v1.2** karena itu adalah dokumen yang paling terkini dan spesifik untuk dekomposisi file. Jika Module Structure tidak menyebutkan file tertentu tapi Coding Standard menyebutkan, **tambahkan file tersebut**.

---

### ⚙️ TAHAP 1 — Pembuatan Branch Git

- [ ] Pastikan kamu berada di branch `develop` yang sudah terbaru:
  ```bash
  git checkout develop
  git pull origin develop
  ```
- [ ] Buat branch baru sesuai konvensi Git Workflow:
  ```bash
  git checkout -b chore/scaffolding-project
  ```

---

### ⚙️ TAHAP 2 — Pembuatan Struktur Direktori

> **Tujuan**: Buat seluruh folder kosong sesuai blueprint.

- [ ] Buat direktori `cli/`
- [ ] Buat direktori `logic/`
- [ ] Buat direktori `db/`
- [ ] Buat direktori `middleware/`
- [ ] Buat direktori `config/`
- [ ] Buat direktori `utils/`
- [ ] Buat direktori `exports/`
- [ ] Buat direktori `exports/backups/`
- [ ] Buat direktori `exports/designs/`
- [ ] Buat direktori `exports/receipts/`
- [ ] Buat direktori `tests/`

> ✅ **Verifikasi**: Jalankan perintah `tree` atau `ls -R` dan bandingkan hasilnya dengan blueprint di Bab 4.1 dokumen ini. Pastikan tidak ada folder yang terlewat.

---

### ⚙️ TAHAP 3 — Pembuatan File Konfigurasi Root

#### 3.1. File: `requirements.txt`

- [ ] Buat file `requirements.txt` di root proyek.
- [ ] Isi dengan daftar dependensi versi terkunci berikut (salin **persis** dari Bab 4.2 dokumen ini):

```
mysql-connector-python==8.4.0
python-dotenv==1.0.1
bcrypt==4.1.0
pyjwt==2.8.0
cryptography==42.0.5
rich==13.7.0
tabulate==0.9.0
pytest==8.2.0
coverage==7.5.1
```

- [ ] Pastikan tidak ada baris kosong tambahan di akhir file.
- [ ] Pastikan tidak ada spasi di sekitar tanda `==`.

#### 3.2. File: `.env.example`

- [ ] Buat file `.env.example` di root proyek.
- [ ] Salin **persis** konten template dari Bab 4.3 dokumen ini.
- [ ] Pastikan semua placeholder bertuliskan `YOUR_..._HERE` (bukan nilai riil).
- [ ] Pastikan ada komentar panduan generasi key JWT dan Fernet.

#### 3.3. File: `.gitignore`

- [ ] Buat file `.gitignore` di root proyek.
- [ ] Salin **persis** konten template dari Bab 4.4 dokumen ini (versi Git Workflow — yang paling lengkap).
- [ ] Pastikan ada exception rule `!exports/.../.gitkeep` agar `.gitkeep` tetap di-track.

#### 3.4. File: `.gitattributes`

- [ ] Buat file `.gitattributes` di root proyek.
- [ ] Salin **persis** konten template dari Bab 4.5 dokumen ini.
- [ ] Pastikan file `.py` diset `eol=lf` dan file `.bat`/`.cmd` diset `eol=crlf`.

#### 3.5. File: `.gitkeep` pada Direktori Output

- [ ] Buat file kosong `exports/backups/.gitkeep`
- [ ] Buat file kosong `exports/designs/.gitkeep`
- [ ] Buat file kosong `exports/receipts/.gitkeep`

> ✅ **Verifikasi Tahap 3**: Pastikan file berikut sudah ada di root:
> `requirements.txt`, `.env.example`, `.gitignore`, `.gitattributes`
> Dan file `.gitkeep` ada di setiap subdirektori `exports/`.

- [ ] **COMMIT ATOMIS TAHAP 3**:
  ```bash
  git add requirements.txt .env.example .gitignore .gitattributes exports/
  git commit -m "chore(config): tambah file konfigurasi root scaffolding project"
  ```

---

### ⚙️ TAHAP 4 — Pembuatan File Entry Point (`main.py`)

- [ ] Buat file `main.py` di root proyek.
- [ ] Tulis boilerplate entry point berikut:

```python
"""
Nama Modul: main.py
Deskripsi: Entry point utama peluncuran aplikasi CLI AbuCom.
           Memvalidasi kelengkapan file .env, menginisialisasi koneksi database,
           dan meluncurkan antarmuka login terminal CLI.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import sys
import os
from pathlib import Path


def validate_env_file() -> bool:
    """Memvalidasi keberadaan file konfigurasi .env di root proyek.

    Returns:
        bool: True jika file .env ditemukan, False jika tidak.
    """
    env_path = Path(__file__).parent / '.env'
    if not env_path.exists():
        print("⛔ ERR-FILE-001: File .env tidak ditemukan di root proyek.")
        print("   Salin file .env.example menjadi .env dan lengkapi kredensial.")
        return False
    return True


def main() -> None:
    """Fungsi utama entry point aplikasi AbuCom CLI."""
    print("=" * 60)
    print("  AbuCom — Sistem Manajemen Terpadu Usaha Percetakan")
    print("=" * 60)
    print()

    # Tahap 1: Validasi keberadaan file konfigurasi .env
    if not validate_env_file():
        sys.exit(1)

    # Tahap 2: Muat konfigurasi dari .env
    # TODO: Implementasi pemanggilan config/settings.py

    # Tahap 3: Inisialisasi koneksi database pool
    # TODO: Implementasi pemanggilan db/db_connector.py

    # Tahap 4: Peluncuran antarmuka CLI login
    # TODO: Implementasi pemanggilan cli/__init__.py -> start_cli_app()

    print("[INFO] Scaffolding berhasil. Modul belum diimplementasikan.")
    print("[INFO] Tekan Enter untuk keluar...")
    input()


if __name__ == '__main__':
    main()
```

- [ ] Pastikan file menggunakan **4 spasi indentasi** (bukan Tab).
- [ ] Pastikan file menggunakan **single quote** untuk string internal dan **double quote** untuk docstring.
- [ ] Pastikan setiap fungsi memiliki **type hints** dan **docstring PEP 257**.

- [ ] **COMMIT ATOMIS TAHAP 4**:
  ```bash
  git add main.py
  git commit -m "chore(config): tambah entry point main.py scaffolding project"
  ```

---

### ⚙️ TAHAP 5 — Pembuatan Boilerplate Layer: `config/`

#### 5.1. File: `config/__init__.py`

- [ ] Buat file `config/__init__.py` dengan isi:

```python
"""
Nama Modul: config/__init__.py
Deskripsi: Package inisialisasi modul konfigurasi runtime AbuCom.
           Expose fungsi dan variabel settings.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

from config.settings import load_settings
```

#### 5.2. File: `config/settings.py`

- [ ] Buat file `config/settings.py` dengan boilerplate:

```python
"""
Nama Modul: settings.py
Deskripsi: Agregasi dan casting data bertipe aman dari file kredensial
           rahasia lokal .env menggunakan library python-dotenv.
           Menyediakan variabel konfigurasi sebagai read-only dictionary.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import os
import sys
from pathlib import Path
from collections import namedtuple

from dotenv import load_dotenv


# Konstanta konfigurasi default
DEFAULT_DB_HOST = '10.10.10.10'
DEFAULT_DB_PORT = 3306
DEFAULT_DB_POOL_SIZE = 5
DEFAULT_JWT_LIFETIME = 28800
DEFAULT_PRINTER_WIDTH = 58

# NamedTuple imutabel untuk konfigurasi runtime
AppConfig = namedtuple('AppConfig', [
    'app_env',
    'app_cabang_id',
    'db_host',
    'db_port',
    'db_user',
    'db_password',
    'db_name',
    'db_pool_size',
    'jwt_secret_key',
    'jwt_lifetime_seconds',
    'fernet_key',
    'backup_zip_password',
    'printer_port',
    'printer_width_mm',
])


def load_settings() -> AppConfig:
    """Memuat dan memvalidasi seluruh variabel konfigurasi dari file .env.

    Returns:
        AppConfig: NamedTuple imutabel berisi seluruh konfigurasi runtime.

    Raises:
        SystemExit: Jika file .env tidak ditemukan atau variabel wajib kosong.
    """
    env_path = Path(__file__).parent.parent / '.env'

    if not env_path.exists():
        print("⛔ ERR-FILE-001: File .env tidak ditemukan.")
        sys.exit(1)

    load_dotenv(dotenv_path=str(env_path))

    # Validasi variabel wajib tidak boleh kosong
    required_vars = ['DB_PASSWORD', 'JWT_SECRET_KEY', 'FERNET_KEY']
    for var_name in required_vars:
        if not os.getenv(var_name) or os.getenv(var_name, '').startswith('YOUR_'):
            print(f"⛔ ERR-FILE-002: Variabel {var_name} belum diisi di file .env.")
            sys.exit(1)

    return AppConfig(
        app_env=os.getenv('APP_ENV', 'development'),
        app_cabang_id=int(os.getenv('APP_CABANG_ID', '1')),
        db_host=os.getenv('DB_HOST', DEFAULT_DB_HOST),
        db_port=int(os.getenv('DB_PORT', str(DEFAULT_DB_PORT))),
        db_user=os.getenv('DB_USER', 'abucom_app'),
        db_password=os.getenv('DB_PASSWORD', ''),
        db_name=os.getenv('DB_NAME', 'abucom_db'),
        db_pool_size=int(os.getenv('DB_POOL_SIZE', str(DEFAULT_DB_POOL_SIZE))),
        jwt_secret_key=os.getenv('JWT_SECRET_KEY', ''),
        jwt_lifetime_seconds=int(os.getenv('JWT_LIFETIME_SECONDS', str(DEFAULT_JWT_LIFETIME))),
        fernet_key=os.getenv('FERNET_KEY', ''),
        backup_zip_password=os.getenv('BACKUP_ZIP_PASSWORD', ''),
        printer_port=os.getenv('PRINTER_PORT', 'COM1'),
        printer_width_mm=int(os.getenv('PRINTER_WIDTH_MM', str(DEFAULT_PRINTER_WIDTH))),
    )
```

- [ ] Pastikan `AppConfig` menggunakan **NamedTuple** (imutabel, sesuai FP).
- [ ] Pastikan ada validasi variabel wajib dan kode error `ERR-FILE-001` dan `ERR-FILE-002`.

- [ ] **COMMIT ATOMIS TAHAP 5**:
  ```bash
  git add config/
  git commit -m "chore(config): tambah boilerplate config/settings.py scaffolding"
  ```

---

### ⚙️ TAHAP 6 — Pembuatan Boilerplate Layer: `db/`

#### 6.1. File: `db/__init__.py`

- [ ] Buat file `db/__init__.py` dengan isi:

```python
"""
Nama Modul: db/__init__.py
Deskripsi: Package inisialisasi modul Data Access Layer AbuCom.
           Expose fungsi connection pooling dan query builder.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""
```

#### 6.2. File: `db/db_connector.py`

- [ ] Buat file `db/db_connector.py` dengan boilerplate connection pool:

```python
"""
Nama Modul: db_connector.py
Deskripsi: Inisialisasi connection pool database MySQL lokal menggunakan
           driver mysql-connector-python. Implementasi retry automatic
           dengan exponential backoff saat menangkap error MySQL 2006/2013.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

import time
from collections import namedtuple

# TODO: Import mysql.connector setelah environment setup selesai
# import mysql.connector
# from mysql.connector import pooling


# Konstanta retry mechanism
MAX_RETRIES = 3
RETRY_ERROR_CODES = (2006, 2013)

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


def create_connection_pool(
    host: str,
    port: int,
    user: str,
    password: str,
    database: str,
    pool_size: int = 5,
    pool_name: str = 'abupool'
) -> Result:
    """Membuat connection pool database MySQL lokal.

    Args:
        host (str): Alamat IP statis server database (default 10.10.10.10).
        port (int): Port database MySQL (default 3306).
        user (str): Username database (default abucom_app).
        password (str): Password database.
        database (str): Nama database target.
        pool_size (int): Jumlah koneksi dalam pool (default 5).
        pool_name (str): Nama identifikasi pool (default 'abupool').

    Returns:
        Result: NamedTuple berisi status koneksi pool.
    """
    # TODO: Implementasi connection pool factory
    # pool = mysql.connector.pooling.MySQLConnectionPool(
    #     pool_name=pool_name,
    #     pool_size=pool_size,
    #     pool_reset_session=True,
    #     host=host,
    #     port=port,
    #     user=user,
    #     password=password,
    #     database=database
    # )
    return Result(False, None, 'ERR-DB-001: Connection pool belum diimplementasikan.')


def get_db_connection(max_retries: int = MAX_RETRIES) -> Result:
    """Mengambil koneksi aktif dari pool dengan retry exponential backoff.

    Retry dilakukan 3 kali dengan interval 2^attempt detik (2s, 4s, 8s)
    saat menangkap MySQL error code 2006 atau 2013.

    Args:
        max_retries (int): Jumlah maksimum percobaan ulang (default 3).

    Returns:
        Result: NamedTuple berisi koneksi database atau pesan error.
    """
    # TODO: Implementasi retry mechanism
    return Result(False, None, 'ERR-DB-001: Get connection belum diimplementasikan.')
```

#### 6.3. File: `db/query_builder.py`

- [ ] Buat file `db/query_builder.py` dengan boilerplate:

```python
"""
Nama Modul: query_builder.py
Deskripsi: Wrapper eksekusi query SQL aman terparameter (%s bindings)
           dan block penjamin atomik ACID transaksi InnoDB.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

from collections import namedtuple
from typing import Callable, Any

Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])


def execute_query(db_connection, query: str, params: tuple | None = None) -> Result:
    """Mengeksekusi query SQL tunggal dengan parameterized bindings %s.

    Args:
        db_connection: Objek koneksi database aktif dari pool.
        query (str): String query SQL dengan placeholder %s.
        params (tuple | None): Parameter binding untuk query.

    Returns:
        Result: NamedTuple berisi hasil eksekusi query.
    """
    # TODO: Implementasi parameterized query execution
    return Result(False, None, 'ERR-DB-002: Execute query belum diimplementasikan.')


def execute_acid_transaction(
    db_connection,
    operations: list[Callable[[Any], Any]]
) -> Result:
    """Wrapper fungsional penjamin transaksi ACID rollback/commit InnoDB.

    Args:
        db_connection: Objek koneksi database aktif dari pool.
        operations (list[Callable]): Daftar fungsi operasi yang dieksekusi atomik.

    Returns:
        Result: NamedTuple berisi status transaksi dan hasil operasi.
    """
    # TODO: Implementasi ACID transaction wrapper
    # cursor = db_connection.cursor()
    # try:
    #     db_connection.start_transaction()
    #     results = [op(cursor) for op in operations]
    #     db_connection.commit()
    #     return Result(True, results, None)
    # except Exception as e:
    #     db_connection.rollback()
    #     return Result(False, None, f"ERR-DB-TX: {str(e)}")
    return Result(False, None, 'ERR-DB-003: ACID transaction belum diimplementasikan.')
```

- [ ] **COMMIT ATOMIS TAHAP 6**:
  ```bash
  git add db/
  git commit -m "chore(db): tambah boilerplate db_connector dan query_builder scaffolding"
  ```

---

### ⚙️ TAHAP 7 — Pembuatan Boilerplate Layer: `middleware/`

#### 7.1. File: `middleware/__init__.py`

- [ ] Buat file `middleware/__init__.py` dengan header module docstring.

#### 7.2. File: `middleware/auth_jwt.py`

- [ ] Buat file dengan stub fungsi: `hash_password()`, `verify_password()`, `create_jwt_session()`, `verify_jwt_session()`.
- [ ] Sertakan konstanta: `BCRYPT_COST_FACTOR = 12`, `JWT_ALGORITHM = 'HS256'`.
- [ ] Sertakan komentar referensi ke Security Design Bab 4.1 dan Bab 4.2.
- [ ] Setiap fungsi harus memiliki type hints lengkap dan docstring PEP 257.
- [ ] Gunakan `# TODO:` untuk menandai implementasi yang belum dilakukan.

#### 7.3. File: `middleware/rbac_guard.py`

- [ ] Buat file dengan stub fungsi: `check_menu_permission()`, `require_role()` (decorator).
- [ ] Sertakan komentar: "Matriks RBAC akan dimuat dari database/config, bukan di-hardcode."
- [ ] Setiap fungsi harus memiliki type hints lengkap dan docstring PEP 257.

#### 7.4. File: `middleware/audit_logger.py`

- [ ] Buat file dengan stub fungsi: `log_audit_trail()`.
- [ ] Sertakan parameter lengkap: `pengguna_id`, `action_type`, `target_table`, `old_val`, `new_val`, `cabang_id`, `db_connection`.
- [ ] Setiap fungsi harus memiliki type hints lengkap dan docstring PEP 257.

- [ ] **COMMIT ATOMIS TAHAP 7**:
  ```bash
  git add middleware/
  git commit -m "chore(middleware): tambah boilerplate auth_jwt, rbac_guard, audit_logger"
  ```

---

### ⚙️ TAHAP 8 — Pembuatan Boilerplate Layer: `utils/`

#### 8.1. File: `utils/__init__.py`

- [ ] Buat file `utils/__init__.py` dengan header module docstring.

#### 8.2. File: `utils/crypto.py`

- [ ] Buat file dengan stub fungsi: `encrypt_whatsapp_number()`, `decrypt_whatsapp_number()`.
- [ ] Sertakan komentar referensi ke UU PDP No. 27/2022 dan Security Design Bab 6.1.
- [ ] Type hints: `(wa_number: str, fernet_key: str) -> str`.

#### 8.3. File: `utils/backup.py`

- [ ] Buat file dengan stub fungsi: `run_backup_manual()`.
- [ ] Sertakan komentar bahwa backup menggunakan ZIP AES-256.

#### 8.4. File: `utils/text_formatter.py`

- [ ] Buat file dengan stub fungsi: `format_thermal_nota()`, `clear_terminal()`.
- [ ] Untuk `clear_terminal()`, implementasikan **langsung** (bukan stub) karena sederhana:
  ```python
  import platform
  import os

  def clear_terminal() -> None:
      """Membersihkan layar terminal console secara lintas OS."""
      os.system('cls' if platform.system() == 'Windows' else 'clear')
  ```

- [ ] **COMMIT ATOMIS TAHAP 8**:
  ```bash
  git add utils/
  git commit -m "chore(utils): tambah boilerplate crypto, backup, text_formatter"
  ```

---

### ⚙️ TAHAP 9 — Pembuatan Boilerplate Layer: `logic/`

#### 9.1. File: `logic/__init__.py`

- [ ] Buat file `logic/__init__.py` dengan header module docstring.

#### 9.2. File: `logic/bom_hpp.py`

- [ ] Buat file dengan:
  - [ ] NamedTuple `BOMKomponen` = `('bahan_baku_id', 'nama_barang', 'kuantitas', 'harga_beli')`
  - [ ] NamedTuple `Result` = `('is_success', 'data', 'error_msg')`
  - [ ] Stub fungsi: `hitung_biaya_komponen()`, `hitung_hpp_produk()`, `proses_pemotongan_stok()`.
  - [ ] Import `decimal.Decimal` dan `decimal.ROUND_HALF_UP`.

#### 9.3. File: `logic/smart_payroll.py`

- [ ] Buat file dengan:
  - [ ] NamedTuple `PayrollResult` = `('gaji_pokok', 'insentif_poin', 'potongan_kasbon', 'gaji_bersih')`
  - [ ] Stub fungsi: `hitung_gaji_bagi_hasil()`, `hitung_komisi_poin()`, `hitung_payroll_akhir()`.

#### 9.4. File: `logic/financial_engine.py`

- [ ] Buat file dengan:
  - [ ] NamedTuple `DepresiasiResult` = `('penyusutan_bulanan', 'akumulasi_penyusutan', 'nilai_buku')`
  - [ ] Stub fungsi: `hitung_penyusutan_garis_lurus()`, `verifikasi_limit_pengeluaran()`.

#### 9.5. File: `logic/financial_reporter.py`

- [ ] Buat file dengan:
  - [ ] Stub fungsi: `generate_laporan_laba_rugi()`, `generate_laporan_arus_kas()`.
  - [ ] Sertakan komentar: "Modul M.9 — Logika agregasi laporan keuangan."

#### 9.6. File: `logic/safety_validator.py`

- [ ] Buat file dengan:
  - [ ] NamedTuple `ValidationStatus` = `('is_valid', 'sanitized_data', 'error_msg')`
  - [ ] Stub fungsi: `sanitasi_input_cli()`, `validasi_kekuatan_sandi()`.
  - [ ] Fungsi `sanitasi_input_cli()` boleh langsung **diimplementasikan** (sederhana):
    ```python
    def sanitasi_input_cli(raw_input: str) -> str:
        """Membuang karakter kontrol ASCII di bawah byte 0x20.

        Args:
            raw_input (str): String mentah dari input keyboard CLI.

        Returns:
            str: String yang sudah dibersihkan dari karakter kontrol.
        """
        return ''.join(char for char in raw_input if ord(char) >= 0x20)
    ```

- [ ] **COMMIT ATOMIS TAHAP 9**:
  ```bash
  git add logic/
  git commit -m "chore(logic): tambah boilerplate bom_hpp, payroll, financial, safety"
  ```

---

### ⚙️ TAHAP 10 — Pembuatan Boilerplate Layer: `cli/`

#### 10.1. File: `cli/__init__.py`

- [ ] Buat file dengan stub fungsi: `start_cli_app()`.

#### 10.2. File: `cli/dashboard.py`

- [ ] Buat file dengan stub fungsi: `render_dashboard()`, `handle_navigation()`.
- [ ] Parameter wajib: `session_state: dict`.

#### 10.3. File: `cli/menu_transaksi.py`

- [ ] Buat file dengan stub fungsi: `show_menu_transaksi()`, `form_pencatatan_transaksi()`, `form_dp_pelunasan()`, `form_retur_pembatalan()`, `form_crm_pelanggan()`.

#### 10.4. File: `cli/menu_inventaris.py`

- [ ] Buat file dengan stub fungsi: `show_menu_inventaris()`, `form_kelola_barang()`, `form_komposisi_bom()`, `form_mencatat_limbah()`, `form_stock_opname()`, `form_import_csv()`, `form_kelola_supplier()`, `trigger_backup_restore()`, `form_job_tracking_antrian()`, `form_arsip_desain()`, `trigger_whatsapp_link()`.

#### 10.5. File: `cli/menu_ppob_service.py`

- [ ] Buat file dengan stub fungsi: `show_menu_ppob_service()`, `form_ppob_deposit()`, `view_ewallet_terhemat()`, `form_jasa_service()`.

#### 10.6. File: `cli/menu_sdm_finansial.py`

- [ ] Buat file dengan stub fungsi: `show_menu_sdm_finansial()`, `form_absensi_kasbon()`, `trigger_smart_payroll()`, `form_pinjaman_modal()`, `view_laba_rugi_divisi()`, `form_pengeluaran_rutin()`.

#### 10.7. File: `cli/menu_laporan.py`

- [ ] Buat file dengan stub fungsi: `show_menu_laporan()`.
- [ ] Sertakan komentar: "Modul M.9 — Menu interaksi laporan keuangan."

#### 10.8. File: `cli/menu_configs.py`

- [ ] Buat file dengan stub fungsi: `show_menu_configs()`, `form_update_parameter()`.

> **PENTING untuk semua file `cli/`**: Setiap stub fungsi harus:
> - Menerima parameter `session_state: dict`.
> - Mengembalikan `-> None`.
> - Memiliki docstring PEP 257 yang menyebutkan modul fungsional terkait.
> - Mengandung `# TODO:` menandai implementasi di masa depan.
> - Mencetak placeholder: `print("[PLACEHOLDER] Menu belum diimplementasikan.")`.

- [ ] **COMMIT ATOMIS TAHAP 10**:
  ```bash
  git add cli/
  git commit -m "chore(cli): tambah boilerplate seluruh menu presentasi CLI scaffolding"
  ```

---

### ⚙️ TAHAP 11 — Pembuatan Boilerplate Layer: `tests/`

#### 11.1. File: `tests/__init__.py`

- [ ] Buat file `tests/__init__.py` dengan header module docstring.

#### 11.2. File: `tests/test_bom_hpp.py`

- [ ] Buat file dengan 1 test placeholder:

```python
"""
Nama Modul: test_bom_hpp.py
Deskripsi: Unit testing deterministic terisolasi untuk fungsi kalkulasi
           HPP dan BOM desimal pada logic/bom_hpp.py.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

from decimal import Decimal


def test_placeholder_bom_hpp() -> None:
    """Placeholder test — akan diganti dengan test cases riil oleh tim AI spesialis."""
    assert Decimal('1.0000') + Decimal('2.0000') == Decimal('3.0000')
```

#### 11.3. File: `tests/test_rbac_security.py`

- [ ] Buat file dengan 1 test placeholder:

```python
"""
Nama Modul: test_rbac_security.py
Deskripsi: Integration testing sandbox untuk simulasi otorisasi RBAC
           multi-user dan validasi akses menu CLI.
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""


def test_placeholder_rbac() -> None:
    """Placeholder test — akan diganti dengan test cases riil oleh tim AI spesialis."""
    assert True
```

- [ ] **COMMIT ATOMIS TAHAP 11**:
  ```bash
  git add tests/
  git commit -m "chore(test): tambah boilerplate test stub placeholder scaffolding"
  ```

---

### ⚙️ TAHAP 12 — Verifikasi Kelengkapan Akhir

> **Tujuan**: Pastikan TIDAK ADA satupun file atau folder yang terlewat.

- [ ] Jalankan perintah `tree` (Windows) atau `find . -type f` (Linux) dan bandingkan output dengan blueprint di Bab 4.1 dokumen ini.
- [ ] Verifikasi **checklist kelengkapan file** berikut:

**File Root:**
- [ ] `main.py` — ada, memiliki header docstring, ada fungsi `main()` dan `validate_env_file()`.
- [ ] `requirements.txt` — ada, berisi 9 dependensi dengan versi terkunci.
- [ ] `.env.example` — ada, berisi 12 variabel konfigurasi dengan placeholder.
- [ ] `.gitignore` — ada, berisi aturan pengabaian untuk `.env`, `venv/`, `__pycache__/`, `exports/`.
- [ ] `.gitattributes` — ada, berisi aturan `eol=lf` untuk `.py` dan `eol=crlf` untuk `.bat`.

**Package `config/` (2 file):**
- [ ] `config/__init__.py` — ada, import `load_settings`.
- [ ] `config/settings.py` — ada, memiliki `AppConfig` NamedTuple dan fungsi `load_settings()`.

**Package `db/` (3 file):**
- [ ] `db/__init__.py` — ada.
- [ ] `db/db_connector.py` — ada, memiliki stub `create_connection_pool()` dan `get_db_connection()`.
- [ ] `db/query_builder.py` — ada, memiliki stub `execute_query()` dan `execute_acid_transaction()`.

**Package `middleware/` (4 file):**
- [ ] `middleware/__init__.py` — ada.
- [ ] `middleware/auth_jwt.py` — ada, memiliki stub 4 fungsi autentikasi.
- [ ] `middleware/rbac_guard.py` — ada, memiliki stub `check_menu_permission()` dan `require_role()`.
- [ ] `middleware/audit_logger.py` — ada, memiliki stub `log_audit_trail()`.

**Package `utils/` (4 file):**
- [ ] `utils/__init__.py` — ada.
- [ ] `utils/crypto.py` — ada, memiliki stub `encrypt_whatsapp_number()` dan `decrypt_whatsapp_number()`.
- [ ] `utils/backup.py` — ada, memiliki stub `run_backup_manual()`.
- [ ] `utils/text_formatter.py` — ada, memiliki `clear_terminal()` (implementasi langsung) dan stub `format_thermal_nota()`.

**Package `logic/` (6 file):**
- [ ] `logic/__init__.py` — ada.
- [ ] `logic/bom_hpp.py` — ada, memiliki NamedTuple `BOMKomponen` dan 3 stub fungsi.
- [ ] `logic/smart_payroll.py` — ada, memiliki NamedTuple `PayrollResult` dan 3 stub fungsi.
- [ ] `logic/financial_engine.py` — ada, memiliki NamedTuple `DepresiasiResult` dan 2 stub fungsi.
- [ ] `logic/financial_reporter.py` — ada, memiliki 2 stub fungsi.
- [ ] `logic/safety_validator.py` — ada, memiliki NamedTuple `ValidationStatus` dan fungsi `sanitasi_input_cli()` (terimplementasi).

**Package `cli/` (8 file):**
- [ ] `cli/__init__.py` — ada, memiliki stub `start_cli_app()`.
- [ ] `cli/dashboard.py` — ada, memiliki stub `render_dashboard()` dan `handle_navigation()`.
- [ ] `cli/menu_transaksi.py` — ada, memiliki 5 stub fungsi.
- [ ] `cli/menu_inventaris.py` — ada, memiliki 11 stub fungsi.
- [ ] `cli/menu_ppob_service.py` — ada, memiliki 4 stub fungsi.
- [ ] `cli/menu_sdm_finansial.py` — ada, memiliki 6 stub fungsi.
- [ ] `cli/menu_laporan.py` — ada, memiliki 1 stub fungsi.
- [ ] `cli/menu_configs.py` — ada, memiliki 2 stub fungsi.

**Package `tests/` (3 file):**
- [ ] `tests/__init__.py` — ada.
- [ ] `tests/test_bom_hpp.py` — ada, memiliki 1 test placeholder.
- [ ] `tests/test_rbac_security.py` — ada, memiliki 1 test placeholder.

**Direktori `exports/` (3 subdirektori + 3 .gitkeep):**
- [ ] `exports/backups/.gitkeep` — ada.
- [ ] `exports/designs/.gitkeep` — ada.
- [ ] `exports/receipts/.gitkeep` — ada.

**Total file yang harus ada: ~37 file** (termasuk __init__.py, .gitkeep, dan file konfigurasi root).

---

### ⚙️ TAHAP 13 — Verifikasi Teknis

- [ ] Jalankan `python main.py` dari root proyek. Pastikan tidak ada `ImportError` atau `SyntaxError`.
  - Hasil yang diharapkan: Pesan "⛔ ERR-FILE-001" (karena `.env` belum ada) atau pesan "[INFO] Scaffolding berhasil" (jika `.env` ada).
- [ ] Jalankan `python -m py_compile config/settings.py` — pastikan tidak ada error kompilasi.
- [ ] Jalankan `python -m py_compile db/db_connector.py` — pastikan tidak ada error kompilasi.
- [ ] Jalankan `python -m py_compile logic/safety_validator.py` — pastikan tidak ada error kompilasi.
- [ ] Jalankan `pytest tests/ -v` — pastikan 2 placeholder test berstatus **PASSED**.

---

### ⚙️ TAHAP 14 — Push dan Quality Gate

- [ ] Push seluruh commit ke server LAN:
  ```bash
  git push origin chore/scaffolding-project
  ```
- [ ] Picu review otomatis oleh Gemini 3 Flash (STK-011) untuk memverifikasi:
  - [ ] Seluruh file `.py` memiliki header module docstring.
  - [ ] Seluruh nama file dan folder menggunakan `snake_case`.
  - [ ] Tidak ada kata kunci `class` di folder `logic/`.
  - [ ] Tidak ada credentials riil di `.env.example`.
  - [ ] File `.gitignore` mengecualikan `.env` dan `venv/`.
- [ ] Serahkan ke Junior Programmer (STK-000) untuk approval akhir.

---

## 7. Instruksi Khusus Scaffolding

### 7.1. Aturan Penulisan Boilerplate Stub

Setiap **stub fungsi** (fungsi placeholder yang belum diimplementasikan) WAJIB mengikuti format ini:

```python
def nama_fungsi(parameter: tipe) -> tipe_return:
    """Deskripsi singkat apa yang akan dilakukan fungsi ini.

    (Ref: [Nama Dokumen SDLC] Bab X.Y)

    Args:
        parameter (tipe): Deskripsi parameter.

    Returns:
        tipe_return: Deskripsi return value.
    """
    # TODO: Implementasi oleh [Nama AI Spesialis] pada issue berikutnya
    pass
```

### 7.2. Aturan Penamaan NamedTuple dalam Boilerplate

- Gunakan format `PascalCase`.
- Definisikan di bagian atas file setelah import.
- Gunakan `from collections import namedtuple` (bukan `typing.NamedTuple`).

### 7.3. Aturan Import dalam Boilerplate

- Jika modul belum tersedia (misal `mysql.connector` saat belum install), gunakan komentar `# TODO: Import setelah environment setup`.
- **JANGAN** menghapus import yang sudah ada di template — tandai saja dengan komentar.

### 7.4. Encoding File

- Semua file `.py` WAJIB menggunakan encoding **UTF-8**.
- Semua file `.py` WAJIB menggunakan line ending **LF** (sesuai `.gitattributes`).

---

## 8. Data yang Kosong / Perlu Ditindaklanjuti

> 🚩 **PENANDA DATA YANG MEMERLUKAN TINDAK LANJUT**:

| No | Item | Status | Catatan |
|:--:|:-----|:------:|:--------|
| 1 | File `seed.sql` (data inisial master) | ⚠️ BELUM ADA | Belum dibuat. Akan dikerjakan di issue terpisah untuk inisialisasi database. |
| 2 | File `schema.sql` (DDL tabel) | ⚠️ SUDAH ADA DI DOCS | File `docs/sdlc/03_design/01_database_schema.sql` sudah ada. Perlu disalin ke root proyek pada issue database setup. |
| 3 | Folder `exports/handover/` | ⚠️ DISEBUTKAN DI GITIGNORE | File `.gitignore` menyebutkan `exports/handover/*` tapi folder ini tidak ada di blueprint Module Structure. **Keputusan**: Buat folder ini beserta `.gitkeep` untuk konsistensi dengan `.gitignore`. |
| 4 | File `setup_env.bat` | ℹ️ OPSIONAL | Disebutkan di Environment Setup Bab 15.4. Bersifat opsional, boleh ditambahkan atau tidak. |
| 5 | File `cli/menu_laporan.py` | ℹ️ ADA DI CODING STD | Disebutkan di Coding Standard v1.2 Bab 4.1 tapi tidak di Module Structure v1.2 awal. **Keputusan**: Tetap buat file ini sesuai Coding Standard. |
| 6 | File `logic/financial_reporter.py` | ℹ️ ADA DI CODING STD | Disebutkan di Coding Standard v1.2 Bab 4.1. **Keputusan**: Tetap buat file ini. |

---

## 9. Checklist Kualitas Akhir

Sebelum menandai issue ini sebagai **Done**, pastikan seluruh item berikut terpenuhi:

- [ ] **Kelengkapan**: Seluruh ~37 file telah dibuat sesuai blueprint (tidak ada yang terlewat).
- [ ] **Konvensi Penamaan**: Seluruh nama file/folder menggunakan `snake_case`, NamedTuple menggunakan `PascalCase`.
- [ ] **Header Docstring**: Setiap file `.py` memiliki header module docstring PEP 257.
- [ ] **Type Hints**: Setiap fungsi stub memiliki type hints pada parameter dan return value.
- [ ] **Tidak Ada Class**: Tidak ada deklarasi `class` di folder `logic/` (FP murni).
- [ ] **Tidak Ada Credentials**: File `.env.example` hanya berisi placeholder `YOUR_..._HERE`.
- [ ] **Tidak Ada Float**: Tidak ada penggunaan tipe `float` untuk perhitungan keuangan.
- [ ] **Encoding UTF-8**: Seluruh file `.py` ber-encoding UTF-8.
- [ ] **Line Ending LF**: Seluruh file `.py` menggunakan LF (diatur oleh `.gitattributes`).
- [ ] **Compilable**: Seluruh file `.py` lolos `python -m py_compile` tanpa error.
- [ ] **Tests Pass**: `pytest tests/ -v` menghasilkan 2 PASSED, 0 FAILED.
- [ ] **Commit Rapi**: Setiap commit mengikuti Conventional Commits format `chore(scope): deskripsi`.
- [ ] **Tidak Menyenggol Fitur Lain**: Tidak ada modifikasi file di folder `docs/` atau file milik modul lain.
- [ ] **Data Kosong Ditandai**: Semua item yang kosong/ambigu sudah dicatat di Bab 8.

---

## 10. Catatan Tambahan Scaffolding

### 10.1. Urutan Pembuatan File per Layer

Urutan pembuatan file sangat penting untuk menghindari circular import:
1. **`config/`** → paling dasar, tidak bergantung pada modul lain.
2. **`db/`** → bergantung pada `config/` untuk membaca `.env`.
3. **`middleware/`** → bergantung pada `db/` untuk audit logging.
4. **`utils/`** → utilitas independen, minimal dependensi.
5. **`logic/`** → bergantung pada `db/` dan `utils/`.
6. **`cli/`** → bergantung pada `logic/`, `middleware/`, `utils/`.
7. **`tests/`** → bergantung pada `logic/` (dan `db/` untuk integration test).

### 10.2. Stub vs Implementasi Langsung

Beberapa fungsi yang sangat sederhana dan tidak memiliki dependensi **boleh langsung diimplementasikan** (bukan stub):
- `utils/text_formatter.py` → `clear_terminal()` (hanya 2 baris kode).
- `logic/safety_validator.py` → `sanitasi_input_cli()` (hanya 1 baris list comprehension).
- `config/settings.py` → `load_settings()` (logika pembacaan `.env` — sudah diberikan boilerplate lengkap).

### 10.3. Konsistensi Antar-File

Pastikan definisi `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])` konsisten di semua file yang menggunakannya. Jangan ada file yang memakai field berbeda.

---

## 11. Referensi Commit Message untuk Issue Ini

Berikut adalah daftar lengkap commit message yang harus digunakan (sesuai Conventional Commits dan Git Workflow Bab 5):

| Tahap | Commit Message |
|:-----:|:---------------|
| 3 | `chore(config): tambah file konfigurasi root scaffolding project` |
| 4 | `chore(config): tambah entry point main.py scaffolding project` |
| 5 | `chore(config): tambah boilerplate config/settings.py scaffolding` |
| 6 | `chore(db): tambah boilerplate db_connector dan query_builder scaffolding` |
| 7 | `chore(middleware): tambah boilerplate auth_jwt, rbac_guard, audit_logger` |
| 8 | `chore(utils): tambah boilerplate crypto, backup, text_formatter` |
| 9 | `chore(logic): tambah boilerplate bom_hpp, payroll, financial, safety` |
| 10 | `chore(cli): tambah boilerplate seluruh menu presentasi CLI scaffolding` |
| 11 | `chore(test): tambah boilerplate test stub placeholder scaffolding` |

---

*Issue ini dideklarasikan sebagai spesifikasi resmi scaffolding proyek AbuCom. Dikerjakan oleh persona `Senior Project Scaffolding Engineer & Boilerplate Architect`.*
