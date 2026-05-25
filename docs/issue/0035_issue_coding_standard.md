---
judul          : Issue — Pembuatan dan Penyusunan Dokumen Coding Standard
target_file    : docs/sdlc/04_implementation/01_coding_standard.md
prioritas      : High
status         : Open
tanggal_dibuat : 2026-05-25
persona_pelaksana : Principal Software Engineering Standards Architect & FP Code Quality Lead
---

# Pembuatan dan Penyusunan Dokumen Coding Standard

## 1. Ringkasan Issue

Issue ini berisi perencanaan low-level untuk pembuatan dan penyusunan dokumen **Coding Standard** pada proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**. Dokumen ini merupakan deliverable pertama pada **Fase 04 — Implementation** dalam siklus SDLC AbuCom. Dokumen Coding Standard mendefinisikan seluruh aturan, konvensi, standar penulisan kode Python, pola arsitektur fungsional, dan panduan kualitas kode yang bersifat **mengikat dan wajib dipatuhi** oleh seluruh anggota tim pengembang (6 model AI dan 1 Junior Programmer) selama fase implementasi berlangsung.

---

## 2. Persona Pelaksana

**Persona**: `Principal Software Engineering Standards Architect & FP Code Quality Lead`

**Justifikasi Pemilihan Persona**:
- Dokumen Coding Standard membutuhkan persona yang memiliki otoritas tinggi dalam mendefinisikan aturan penulisan kode yang bersifat mengikat bagi seluruh anggota tim pengembang.
- Persona ini harus memahami secara mendalam paradigma **Functional Programming (FP) murni** yang menjadi mandat wajib proyek AbuCom, termasuk pola-pola desain fungsional tingkat lanjut (Pure Functions, Immutability, State Dictionary Passing, Nested Closures, Higher-Order Functions, Monad-like Error Handling).
- Persona ini harus memiliki wawasan luas mengenai standar industri penulisan kode Python (PEP 8, PEP 257, PEP 484), konvensi penamaan, struktur direktori proyek, dan praktik terbaik untuk menjamin konsistensi, keterbacaan, dan pemeliharaan kode jangka panjang.
- Persona ini harus mampu menyusun aturan yang jelas, tidak ambigu, dan langsung dapat diimplementasikan oleh Junior Programmer maupun model AI pengkoding yang lebih kecil.

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **WAJIB** dibaca dan dirangkum secara menyeluruh oleh pelaksana sebelum memulai penyusunan dokumen utama. File-file ini dipilih berdasarkan relevansi langsung terhadap konten dokumen Coding Standard:

| No | File Referensi | Path Relatif | Prioritas | Alasan Pemilihan |
|:---:|---|---|:---:|---|
| 1 | **Tech Stack Decision v1.1** | `docs/sdlc/01_planning/04_tech_stack_decision.md` | **PRIMER** | SSoT untuk batasan mandatory bahasa Python 3.14.2+, paradigma FP murni, pustaka wajib & rekomendasi (beserta versi), konvensi arsitektur kode, strategi requirements.txt, strategi unit testing FP, dan deployment dual-OS. |
| 2 | **System Architecture v1.1** | `docs/sdlc/03_design/03_system_architecture.md` | **PRIMER** | Definisi arsitektur berlapis 4-Layer FP, pola desain fungsional (Pure Functions, Immutability, State Dict Passing, Closures, Higher-Order Functions, Monad-like Error Handling), aturan dependensi antar-layer, dekomposisi modular 10 modul, dan konvensi penamaan berkas modul. |
| 3 | **Security Design v1.1** | `docs/sdlc/03_design/06_security_design.md` | **PRIMER** | Standar penulisan kode keamanan: parameterized queries wajib (`%s`), pelarangan f-string SQL, sanitasi input CLI, pola RBAC decorator/guard fungsional, manajemen kredensial `.env`, dan pseudocode FP keamanan. |
| 4 | **BOM & HPP Design v1.1** | `docs/sdlc/03_design/05_bom_hpp_design.md` | **SEKUNDER** | Contoh implementasi referensi pseudocode FP murni Python yang sudah terstandarisasi: penggunaan `namedtuple`, `decimal.Decimal`, pola `ProcessResult`, transaction wrapper ACID, `FOR UPDATE` locking, dan konvensi error handling fungsional. |
| 5 | **CLI Interaction Flow v1.1** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | **SEKUNDER** | Konvensi presentation layer CLI: standar visual ANSI (`rich`), format tabel (`tabulate`), pola navigasi menu, konvensi kode error (`ERR-XXX-YYY`), standar validasi input, dan aksesibilitas lintas OS. |
| 6 | **Software Requirements Specification v1.1** | `docs/sdlc/02_analysis/02_software_requirements.md` | **SEKUNDER** | Spesifikasi non-fungsional terkait performa (<1 detik respon), code coverage target (90%), batasan desain FP/CLI, dan dependency library beserta versinya. |
| 7 | **Database Schema v1.1 (DDL SQL)** | `docs/sdlc/03_design/01_database_schema.sql` | **TERSIER** | Konvensi penamaan tabel, kolom, constraint, tipe data `DECIMAL(15,4)`, charset `utf8mb4`, collation `utf8mb4_unicode_ci`, engine `InnoDB`, dan pola komentar SQL. |
| 8 | **ERD Database v1.1** | `docs/sdlc/03_design/02_erd_database.md` | **TERSIER** | Referensi pola relasi 28 tabel untuk memastikan konsistensi penamaan entity di kode Python dengan skema database. |

> **Catatan**: File `narasi.txt` (`docs/sdlc/narasi.txt`) **TIDAK** digunakan sebagai referensi langsung untuk issue ini karena seluruh informasi teknis yang dibutuhkan oleh dokumen Coding Standard sudah terekstraksi secara lengkap dan terformalisasi ke dalam 8 file referensi di atas.

---

## 4. Kerangka Struktur Dokumen Utama

Berikut adalah kerangka (*outline*) struktur dokumen Coding Standard yang **WAJIB** diikuti oleh pelaksana. Kerangka ini disusun mengacu pada standar industri dokumen coding standard/guidelines yang sesungguhnya (misalnya Google Python Style Guide, PEP 8, dan Airbnb Style Guide):

```
---
dokumen    : Coding Standard
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [TANGGAL_PENGERJAAN]
status     : Draft
penyusun   : Principal Software Engineering Standards Architect & FP Code Quality Lead
---

# Coding Standard — AbuCom

## Riwayat Perubahan Dokumen
(Tabel: Versi | Tanggal | Perubahan | Oleh)

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan
### 1.7. Tingkat Kepatuhan (Compliance Levels)
     - Definisi keyword: WAJIB (MUST), DILARANG (MUST NOT), DIREKOMENDASIKAN (SHOULD), OPSIONAL (MAY)

## 2. Prinsip Dasar Penulisan Kode
### 2.1. Filosofi Kode AbuCom
### 2.2. Prinsip Functional Programming (FP) Murni
     - Fungsi Murni (Pure Functions)
     - Imutabilitas Data (Data Immutability)
     - Tanpa Class/OOP di Alur Bisnis Utama
     - Pengelolaan State Tanpa OOP (Closures, State Dict Passing)
     - Higher-Order Functions & Composition
     - Monad-like Error Handling (Result/Either Pattern)
### 2.3. Prinsip Keamanan dalam Kode (Secure Coding)
### 2.4. Prinsip Presisi Desimal (Decimal-First)

## 3. Konvensi Penamaan (Naming Conventions)
### 3.1. Penamaan File dan Direktori
### 3.2. Penamaan Fungsi (snake_case)
### 3.3. Penamaan Variabel dan Konstanta
### 3.4. Penamaan Parameter Fungsi
### 3.5. Penamaan NamedTuple dan Frozen Dataclass
### 3.6. Penamaan Modul dan Package
### 3.7. Konvensi Penamaan Database Entity di Kode Python
### 3.8. Tabel Ringkasan Konvensi Penamaan

## 4. Struktur Direktori Proyek
### 4.1. Layout Direktori Standar
### 4.2. Penjelasan Setiap Direktori dan File
### 4.3. Aturan Penempatan File Baru

## 5. Standar Format dan Gaya Kode (Code Style)
### 5.1. Kepatuhan PEP 8
### 5.2. Indentasi dan Spasi
### 5.3. Panjang Baris Maksimum
### 5.4. Penggunaan Import
     - Urutan Import (Standard Library → Third-Party → Local)
     - Larangan Wildcard Import
### 5.5. Penggunaan String
     - Single Quote vs Double Quote
     - F-string untuk Output Display (BUKAN untuk SQL)
### 5.6. Penggunaan Komentar dan Whitespace

## 6. Standar Dokumentasi Kode (Docstrings & Comments)
### 6.1. Format Docstring Fungsi (PEP 257)
### 6.2. Template Docstring Standar AbuCom
### 6.3. Komentar Inline
### 6.4. Header File / Module Docstring
### 6.5. Penulisan TODO dan FIXME

## 7. Standar Type Hints (PEP 484)
### 7.1. Kewajiban Type Hints pada Semua Fungsi Publik
### 7.2. Penggunaan Modul `typing`
### 7.3. Type Hints untuk Decimal, NamedTuple, dan Koleksi
### 7.4. Contoh Implementasi Type Hints Standar

## 8. Arsitektur Kode dan Pola Desain Fungsional
### 8.1. Arsitektur Berlapis 4-Layer
     - Presentation Layer (CLI)
     - Business Logic Layer (Pure Functions)
     - Data Access Layer (DB Connector)
     - Data/Persistence Layer (MySQL)
### 8.2. Aturan Dependensi Antar-Layer
### 8.3. Pola Pure Functions & Immutability
     - Template NamedTuple/Frozen Dataclass
     - Contoh Implementasi Standar
### 8.4. Pola State Dictionary Passing
### 8.5. Pola Nested Closures
### 8.6. Pola Higher-Order Functions & Composition
### 8.7. Pola Error Handling Fungsional (Result Pattern)
     - Definisi Result NamedTuple
     - Aturan Penggunaan
     - Contoh Implementasi
### 8.8. Pola Transaction Wrapper ACID
     - Template Fungsi Transaksional
     - Aturan START TRANSACTION / COMMIT / ROLLBACK
### 8.9. Pola Connection Pooling & Retry Mechanism

## 9. Standar Penulisan Kode Database (SQL & Data Access)
### 9.1. Wajib Parameterized Queries (`%s` Bindings)
### 9.2. Pelarangan Mutlak F-string / String Formatting untuk SQL
### 9.3. Konvensi Penulisan Query SQL di Python
### 9.4. Penggunaan `cursor.execute()` dan `cursor.executemany()`
### 9.5. Penanganan Koneksi Database (Connection Pooling)
### 9.6. Penanganan Error Database (Retry & Rollback)
### 9.7. Standar Tipe Data `DECIMAL(15,4)` dan Mapping Python `decimal.Decimal`

## 10. Standar Penulisan Kode Keamanan (Secure Coding Standard)
### 10.1. Aturan Pengelolaan Kredensial (`.env` & `python-dotenv`)
### 10.2. Aturan Enkripsi Sandi (`bcrypt` Cost Factor 12)
### 10.3. Aturan Manajemen Session (`JWT` HS256)
### 10.4. Aturan Implementasi RBAC (Guard/Decorator Fungsional)
### 10.5. Aturan Sanitasi Input CLI
### 10.6. Aturan Audit Trail Logging
### 10.7. Aturan Proteksi Data Pribadi (UU PDP Compliance)

## 11. Standar Penulisan Kode CLI (Presentation Layer)
### 11.1. Konvensi Visual `rich` (Panels, Colors, Progress Bars)
### 11.2. Konvensi Tabel `tabulate`
### 11.3. Konvensi Navigasi Menu (Hotkey, Breadcrumb, Back/Exit)
### 11.4. Konvensi Input Password (`getpass`)
### 11.5. Konvensi Pesan Error Visual (`ERR-XXX-YYY`)
### 11.6. Konvensi Pembersihan Layar Terminal (Cross-OS)
### 11.7. Konvensi Encoding UTF-8 Eksplisit

## 12. Standar Portabilitas Lintas OS (Cross-OS Compatibility)
### 12.1. Penggunaan `pathlib` untuk Path Management
### 12.2. Penggunaan `platform.system()` untuk Deteksi OS
### 12.3. Penggunaan Encoding `utf-8` Eksplisit
### 12.4. Larangan Hardcode Path Separator

## 13. Standar Pengelolaan Dependensi
### 13.1. File `requirements.txt` dengan Versi Terkunci
### 13.2. Daftar Dependensi Wajib (Mandatory)
### 13.3. Daftar Dependensi Rekomendasi
### 13.4. Daftar Pustaka Standard Library yang Dimanfaatkan
### 13.5. Aturan Penambahan Dependensi Baru

## 14. Standar Pengujian (Testing Standards)
### 14.1. Framework Testing (`unittest` / `pytest`)
### 14.2. Target Code Coverage (≥ 90% Logika Bisnis)
### 14.3. Konvensi Penamaan Test File dan Test Function
### 14.4. Aturan Unit Testing Pure Functions
### 14.5. Aturan Integration Testing Database
### 14.6. Aturan Testing Keamanan (RBAC, SQL Injection)

## 15. Standar Version Control (Git)
### 15.1. Strategi Branching (Feature Branching)
### 15.2. Konvensi Penamaan Branch
### 15.3. Konvensi Commit Message
### 15.4. Aturan `.gitignore`
### 15.5. Aturan Code Review

## 16. Daftar Larangan Mutlak (Prohibited Practices)
     - Tabel komprehensif seluruh praktik yang DILARANG KERAS

## 17. Checklist Kepatuhan Coding Standard
     - Tabel checklist self-review sebelum commit/merge

## 18. Referensi Dokumen
     - Tabel daftar file referensi yang digunakan dalam penyusunan dokumen ini
```

---

## 5. Instruksi Detail Tahapan Implementasi

### Tahap 1: Persiapan dan Pembacaan File Referensi

Baca secara menyeluruh dan rangkum **setiap detail** dari setiap file referensi berikut. Jangan ada data atau informasi yang terlewat. Fokuskan perangkuman pada data dan informasi yang **spesifik relevan** untuk dokumen Coding Standard.

- [ ] **1.1.** Baca file `docs/sdlc/01_planning/04_tech_stack_decision.md` secara **LENGKAP dari awal hingga akhir**.
  - [ ] Rangkum seluruh batasan mandatory: Python 3.14.2+, FP Murni (tanpa class), MySQL, CLI.
  - [ ] Rangkum seluruh pustaka wajib beserta versi spesifik: `mysql-connector-python==8.4.0`, `python-dotenv==1.0.1`, `bcrypt==4.1.0`, `pyjwt==2.8.0`.
  - [ ] Rangkum seluruh pustaka rekomendasi beserta versi: `rich==13.7.0`, `tabulate==0.9.0`.
  - [ ] Rangkum seluruh pustaka standard library yang dimanfaatkan: `decimal`, `functools`, `itertools`, `operator`, `os`, `pathlib`, `json`, `csv`, `datetime`, `typing`, `getpass`, `textwrap`, `shutil`.
  - [ ] Rangkum prinsip arsitektur panduan: portabilitas lintas OS, imutabilitas data, fungsi murni, keamanan berlapis, integritas transaksional ACID, presisi desimal, skalabilitas multi-cabang.
  - [ ] Rangkum strategi pengelolaan state FP tanpa OOP: Nested Closures, State Dictionary Passing, Monad-like Error Handling.
  - [ ] Rangkum strategi requirements.txt, versi terkunci, `pip install -r requirements.txt`.
  - [ ] Rangkum strategi pengujian fungsional: unit testing pure functions, `unittest`/`pytest`, coverage 90%.
  - [ ] Rangkum strategi branching: Feature Branching, review oleh Gemini 3 Flash.
  - [ ] Rangkum konvensi dual-OS: `pathlib`, encoding `utf-8` eksplisit, `platform.system()`.
  - [ ] Rangkum keamanan kode: parameterized queries `%s`, pelarangan f-string SQL, SQL Injection prevention, rate limiting, sanitasi input.

- [ ] **1.2.** Baca file `docs/sdlc/03_design/03_system_architecture.md` secara **LENGKAP dari awal hingga akhir**.
  - [ ] Rangkum arsitektur berlapis 4-Layer (Presentation, Business Logic, Data Access, Data/Persistence) beserta tanggung jawab masing-masing layer.
  - [ ] Rangkum aturan FP per layer: layer presentation boleh I/O side-effect tapi dilarang komputasi aritmatika; layer business logic wajib pure functions; layer data access mengelola connection pooling dan parameterized queries.
  - [ ] Rangkum pola desain fungsional: Pure Functions & Immutability (namedtuple, frozen dataclass), State Management tanpa OOP, Higher-Order Functions & Composition, Error Handling Fungsional (Result/Either NamedTuple).
  - [ ] Rangkum contoh kode implementasi dari dokumen: `BOMItem`, `hitung_hpp_bom()`, `Result` namedtuple, `validasi_tarik_kasbon()`, `execute_transactional_action()`.
  - [ ] Rangkum dekomposisi 10 modul fungsional dan peta modul ke tabel database.
  - [ ] Rangkum aturan dependensi antar-layer: aliran satu arah atas ke bawah, layer bawah dilarang mengenal layer di atasnya.
  - [ ] Rangkum strategi koneksi database: connection pooling, retry mechanism exponential backoff, ACID transaction block.
  - [ ] Rangkum strategi presisi desimal: `DECIMAL(15,4)` di MySQL, `decimal.Decimal` di Python, larangan `float`.
  - [ ] Rangkum cross-cutting concerns: JWT & bcrypt Security Engine, dotenv configs reader, JSON Audit Trail logger.

- [ ] **1.3.** Baca file `docs/sdlc/03_design/06_security_design.md` secara **LENGKAP dari awal hingga akhir**.
  - [ ] Rangkum standar parameterized queries wajib (`%s` bindings) dan pelarangan f-string/string concatenation SQL.
  - [ ] Rangkum aturan pengelolaan kredensial: `.env` file, `.gitignore`, `.env.example`, startup validator.
  - [ ] Rangkum aturan enkripsi sandi: `bcrypt` cost factor 12, `bcrypt.hashpw()`, `bcrypt.checkpw()`.
  - [ ] Rangkum aturan manajemen session: JWT HS256, secret key 32+ hex chars, payload klaim, masa berlaku 8 jam, handling expiration.
  - [ ] Rangkum aturan RBAC: `require_permission()` function guard, 8 peran, matriks akses per modul, default deny.
  - [ ] Rangkum aturan sanitasi input: filter ASCII control chars `< \x20`, length bounds, regex validation.
  - [ ] Rangkum aturan audit trail: skema tabel `audit_logs`, event pemicu, format JSON `old_value`/`new_value`.
  - [ ] Rangkum aturan proteksi data UU PDP: enkripsi WhatsApp CRM reversible (`cryptography.fernet`), `FERNET_KEY` dari `.env`.
  - [ ] Rangkum kamus kode error keamanan: `ERR-AUTH-xxx`, `ERR-SESSION-xxx`, `ERR-DB-xxx`, `ERR-FILE-xxx`, `ERR-CASH-xxx`.

- [ ] **1.4.** Baca file `docs/sdlc/03_design/05_bom_hpp_design.md` secara **LENGKAP dari awal hingga akhir**.
  - [ ] Rangkum contoh pseudocode FP murni Python yang sudah terstandarisasi sebagai referensi pola kode: `BOMKomponen`, `KalkulasiResult`, `ProcessResult` namedtuple, `hitung_biaya_komponen()`, `hitung_hpp_produk()`, `daftar_bom_baru()`, `proses_pemotongan_stok()`, `proses_limbah_produksi()`, `sinkronisasi_atk_internal()`.
  - [ ] Rangkum penerapan paradigma FP: tanpa class/OOP, pure functions, immutable data, `decimal.Decimal`, `collections.namedtuple`.
  - [ ] Rangkum pola transaction wrapper ACID: `start_transaction()`, `commit()`, `rollback()`, `FOR UPDATE` locking, `cursor.execute()` parameterized.
  - [ ] Rangkum pola presisi desimal: `Decimal('0.0000')`, `.quantize(Decimal('0.0001'))`, `ROUND_HALF_UP`.

- [ ] **1.5.** Baca file `docs/sdlc/03_design/04_cli_interaction_flow.md` secara **LENGKAP dari awal hingga akhir**.
  - [ ] Rangkum konvensi navigasi global: tombol `0` kembali, hotkey numerik, konfirmasi `[Y/N]`, enter kosong, exit darurat `q`/`Ctrl+C`.
  - [ ] Rangkum konvensi visual: `rich` panels, `tabulate` tabel, ANSI color palette (Green=sukses, Red=error, Yellow=warning, Blue=info, Magenta=judul).
  - [ ] Rangkum konvensi input validasi: sanitasi ASCII, password masking `getpass`, fixed-point decimal, regex validation.
  - [ ] Rangkum konvensi pesan error: format `ERR-[KATEGORI]-[NOMOR]: [Pesan deskriptif]`, kategori kode error.
  - [ ] Rangkum konvensi aksesibilitas lintas OS: `chcp 65001`, cross-OS paths `pathlib`, platform-aware clear screen.

- [ ] **1.6.** Baca file `docs/sdlc/02_analysis/02_software_requirements.md` secara **LENGKAP dari awal hingga akhir**.
  - [ ] Rangkum batasan desain dan implementasi: FP murni, CLI user interface, presisi desimal keuangan & gudang, multi-branch ready.
  - [ ] Rangkum kebutuhan non-fungsional terkait kode: performa <1 detik, code coverage 90%, dependency library dengan versi.
  - [ ] Rangkum catatan implementasi dari SRS-F items yang relevan (pola fungsi murni, tipe data, format error code).

- [ ] **1.7.** Baca file `docs/sdlc/03_design/01_database_schema.sql` secara **LENGKAP dari awal hingga akhir**.
  - [ ] Rangkum konvensi penamaan database: nama tabel (`snake_case`), nama kolom (`snake_case`), constraint naming (`fk_`, `chk_`, `uq_`).
  - [ ] Rangkum tipe data yang digunakan: `INT`, `VARCHAR`, `DECIMAL(15,4)`, `TIMESTAMP`, `JSON`, `BOOLEAN`/`TINYINT(1)`.
  - [ ] Rangkum standar charset `utf8mb4`, collation `utf8mb4_unicode_ci`, engine `InnoDB`.
  - [ ] Rangkum pola komentar SQL (`COMMENT`).

- [ ] **1.8.** Baca file `docs/sdlc/03_design/02_erd_database.md` secara **LENGKAP dari awal hingga akhir**.
  - [ ] Rangkum pola penamaan entity untuk memastikan konsistensi penamaan di kode Python.
  - [ ] Rangkum pola relasi (FK, Self-Referencing FK) untuk panduan penulisan query.

---

### Tahap 2: Analisis dan Konsolidasi Data

- [ ] **2.1.** Setelah membaca semua file referensi, konsolidasikan seluruh data dan informasi yang telah dirangkum ke dalam satu daftar terstruktur.
- [ ] **2.2.** Identifikasi dan pisahkan data yang **RELEVAN** untuk dokumen Coding Standard dari data yang tidak relevan.
  - Data yang RELEVAN: aturan penulisan kode, konvensi penamaan, pola arsitektur kode, aturan keamanan kode, aturan testing, aturan version control, daftar pustaka/dependensi, batasan teknologi, contoh kode referensi.
  - Data yang TIDAK RELEVAN: detail alur bisnis operasional toko, detail harga produk, detail struktur organisasi karyawan, detail kebutuhan fungsional bisnis (kecuali yang berdampak pada aturan kode).
- [ ] **2.3.** Identifikasi data yang **KOSONG** atau **TIDAK TERSEDIA** dari file referensi. Tandai bagian tersebut dengan placeholder `[DATA_BELUM_TERSEDIA — Perlu diisi manual oleh Pemilik/Lead Architect]` agar dapat diketahui dan diisi secara manual di kemudian hari.
- [ ] **2.4.** Verifikasi bahwa semua data numerik, nama pustaka, nomor versi, dan konfigurasi teknis yang dikutip dari file referensi **KONSISTEN** dan tidak saling bertentangan.

---

### Tahap 3: Penyusunan Dokumen Utama

Susun dokumen utama mengikuti kerangka struktur pada Bab 4 di atas. Pastikan setiap bagian ditulis dengan kualitas berikut:

- [ ] **3.1. Tulis Front Matter (YAML metadata header)**
  - [ ] Isi field: `dokumen`, `proyek`, `versi` (1.0), `tanggal`, `status` (Draft), `penyusun`.

- [ ] **3.2. Tulis Riwayat Perubahan Dokumen**
  - [ ] Buat tabel dengan kolom: Versi | Tanggal | Perubahan | Oleh.
  - [ ] Isi satu baris versi 1.0 dengan deskripsi inisialisasi.

- [ ] **3.3. Tulis Bab 1 — Informasi Dokumen**
  - [ ] Tulis Tujuan Dokumen: jelaskan bahwa dokumen ini adalah panduan mengikat standar penulisan kode untuk seluruh tim.
  - [ ] Tulis Cakupan Dokumen: sebutkan semua topik yang dicakup.
  - [ ] Tulis Posisi Dokumen dalam SDLC: Fase 04 Implementation, deliverable pertama, diagram posisi ASCII art.
  - [ ] Tulis Hubungan dengan Dokumen Lainnya: sebutkan dokumen input (dari Fase 01-03) dan output (menjadi acuan implementasi kode dan testing).
  - [ ] Tulis Audiens Target: Junior Programmer, 6 model AI, QA team.
  - [ ] Tulis Definisi, Akronim, dan Singkatan: daftar semua istilah teknis yang digunakan.
  - [ ] Tulis Tingkat Kepatuhan: definisikan keyword WAJIB/DILARANG/DIREKOMENDASIKAN/OPSIONAL (sesuai RFC 2119 style).

- [ ] **3.4. Tulis Bab 2 — Prinsip Dasar Penulisan Kode**
  - [ ] Tulis Filosofi Kode AbuCom: prinsip keterbacaan, kesederhanaan, konsistensi, dan keamanan.
  - [ ] Tulis Prinsip FP Murni secara **LENGKAP** beserta contoh kode Python:
    - [ ] Fungsi Murni: definisi, aturan, contoh.
    - [ ] Imutabilitas Data: `namedtuple`, `frozen dataclass`, larangan mutasi variabel.
    - [ ] Larangan Class/OOP di alur bisnis utama.
    - [ ] State Dictionary Passing: cara mengelola state login, keranjang belanja, navigasi CLI.
    - [ ] Nested Closures: contoh penggunaan.
    - [ ] Higher-Order Functions: `map()`, `filter()`, `reduce()`, `functools.partial()`.
    - [ ] Monad-like Error Handling: `Result` namedtuple, contoh penggunaan.
  - [ ] Tulis Prinsip Secure Coding: defense in depth dalam kode.
  - [ ] Tulis Prinsip Decimal-First: seluruh perhitungan keuangan dan stok wajib `decimal.Decimal`.

- [ ] **3.5. Tulis Bab 3 — Konvensi Penamaan**
  - [ ] Tulis aturan penamaan file dan direktori (`snake_case`).
  - [ ] Tulis aturan penamaan fungsi (`snake_case`, verb_noun pattern).
  - [ ] Tulis aturan penamaan variabel (deskriptif, `snake_case`), konstanta (`UPPER_SNAKE_CASE`).
  - [ ] Tulis aturan penamaan parameter fungsi.
  - [ ] Tulis aturan penamaan NamedTuple dan Frozen Dataclass (`PascalCase`).
  - [ ] Tulis aturan penamaan modul dan package.
  - [ ] Tulis aturan penamaan yang konsisten antara entity database dan variabel Python.
  - [ ] Buat tabel ringkasan konvensi penamaan.

- [ ] **3.6. Tulis Bab 4 — Struktur Direktori Proyek**
  - [ ] Definisikan layout direktori standar proyek AbuCom (berdasarkan pola dari System Architecture dan BOM/HPP Design): `main.py`, `cli/`, `logic/`, `db/`, `middleware/`, `utils/`, `config/`, `tests/`, `exports/`, `docs/`, dll.
  - [ ] Jelaskan tujuan setiap direktori.
  - [ ] Tulis aturan penempatan file baru.

- [ ] **3.7. Tulis Bab 5 — Standar Format dan Gaya Kode**
  - [ ] Tulis kepatuhan PEP 8 (dengan pengecualian spesifik jika ada).
  - [ ] Tulis aturan indentasi: 4 spasi, tanpa tab.
  - [ ] Tulis panjang baris maksimum: 120 karakter (atau sesuai keputusan).
  - [ ] Tulis aturan import: urutan (stdlib → third-party → local), larangan wildcard `from x import *`.
  - [ ] Tulis aturan penggunaan string: single quote untuk kode internal, double quote untuk user-facing string/docstring, f-string untuk output display BUKAN SQL.
  - [ ] Tulis aturan komentar dan whitespace.

- [ ] **3.8. Tulis Bab 6 — Standar Dokumentasi Kode**
  - [ ] Tulis format docstring fungsi (PEP 257 style).
  - [ ] Buat template docstring standar AbuCom dengan field: deskripsi, Args, Returns, Raises, Example.
  - [ ] Tulis aturan komentar inline: kapan digunakan, format.
  - [ ] Tulis aturan header file/module docstring.
  - [ ] Tulis aturan penulisan TODO dan FIXME.

- [ ] **3.9. Tulis Bab 7 — Standar Type Hints**
  - [ ] Tulis kewajiban type hints pada semua fungsi publik.
  - [ ] Tulis penggunaan modul `typing` (`Optional`, `Union`, `Callable`, `Tuple`, `List`, `Dict`).
  - [ ] Tulis type hints untuk `Decimal`, `NamedTuple`, koleksi.
  - [ ] Berikan contoh implementasi type hints standar.

- [ ] **3.10. Tulis Bab 8 — Arsitektur Kode dan Pola Desain Fungsional**
  - [ ] Tulis deskripsi arsitektur berlapis 4-Layer beserta diagram (Mermaid atau ASCII).
  - [ ] Tulis aturan dependensi antar-layer secara eksplisit.
  - [ ] Tulis setiap pola desain fungsional (Pure Functions, State Dict Passing, Closures, HOF, Result Pattern, Transaction Wrapper, Connection Pooling) beserta:
    - Definisi dan tujuan pola.
    - Template kode standar yang WAJIB diikuti.
    - Contoh implementasi nyata dari konteks AbuCom.
    - Larangan dan kesalahan umum yang harus dihindari.

- [ ] **3.11. Tulis Bab 9 — Standar Penulisan Kode Database**
  - [ ] Tulis aturan parameterized queries wajib beserta contoh benar dan salah.
  - [ ] Tulis pelarangan mutlak f-string/string formatting untuk SQL beserta contoh.
  - [ ] Tulis konvensi penulisan query SQL di Python: multi-line string, indentasi query.
  - [ ] Tulis aturan `cursor.execute()` dan `cursor.executemany()`.
  - [ ] Tulis aturan connection pooling: `MySQLConnectionPool`, pool size.
  - [ ] Tulis aturan error handling database: retry mechanism, rollback.
  - [ ] Tulis mapping tipe data MySQL ↔ Python (`DECIMAL(15,4)` ↔ `decimal.Decimal`).

- [ ] **3.12. Tulis Bab 10 — Standar Penulisan Kode Keamanan**
  - [ ] Tulis aturan `.env` dan `python-dotenv`: variabel wajib, `.gitignore`, `.env.example`, startup validator.
  - [ ] Tulis aturan `bcrypt`: cost factor 12, `hashpw()`, `checkpw()`, contoh kode.
  - [ ] Tulis aturan JWT: HS256, secret key, payload, masa berlaku 8 jam, handling expiration, contoh kode.
  - [ ] Tulis aturan RBAC guard/decorator fungsional: `require_permission()`, `check_permission()`, contoh kode.
  - [ ] Tulis aturan sanitasi input: filter `< \x20`, length bounds, regex validation, contoh kode.
  - [ ] Tulis aturan audit trail logging: format JSON, event trigger, contoh kode.
  - [ ] Tulis aturan proteksi data UU PDP: enkripsi reversible CRM, `FERNET_KEY`.

- [ ] **3.13. Tulis Bab 11 — Standar Penulisan Kode CLI**
  - [ ] Tulis konvensi `rich`: panels, colors, progress bars, fallback terminal.
  - [ ] Tulis konvensi `tabulate`: format tabel, pembatasan lebar kolom.
  - [ ] Tulis konvensi navigasi menu: hotkey, breadcrumb, back/exit.
  - [ ] Tulis konvensi `getpass` untuk input password.
  - [ ] Tulis konvensi pesan error visual: format, warna, kode error.
  - [ ] Tulis konvensi pembersihan layar terminal lintas OS.
  - [ ] Tulis konvensi encoding UTF-8 eksplisit.

- [ ] **3.14. Tulis Bab 12 — Standar Portabilitas Lintas OS**
  - [ ] Tulis aturan `pathlib` untuk path management.
  - [ ] Tulis aturan `platform.system()` untuk deteksi OS.
  - [ ] Tulis aturan encoding `utf-8` eksplisit.
  - [ ] Tulis larangan hardcode path separator (`/` atau `\`).

- [ ] **3.15. Tulis Bab 13 — Standar Pengelolaan Dependensi**
  - [ ] Tulis format `requirements.txt` dengan versi terkunci (pin exact version).
  - [ ] Tulis daftar lengkap dependensi wajib beserta versi, lisensi, dan fungsi.
  - [ ] Tulis daftar dependensi rekomendasi beserta versi.
  - [ ] Tulis daftar pustaka standard library yang dimanfaatkan beserta fungsi.
  - [ ] Tulis aturan penambahan dependensi baru: proses review, justifikasi.

- [ ] **3.16. Tulis Bab 14 — Standar Pengujian**
  - [ ] Tulis framework testing: `unittest` atau `pytest`.
  - [ ] Tulis target code coverage: ≥ 90% logika bisnis.
  - [ ] Tulis konvensi penamaan test file (`test_<module>.py`) dan test function (`test_<behavior>`).
  - [ ] Tulis aturan unit testing pure functions: isolasi, deterministic, tanpa database.
  - [ ] Tulis aturan integration testing database.
  - [ ] Tulis aturan testing keamanan.

- [ ] **3.17. Tulis Bab 15 — Standar Version Control (Git)**
  - [ ] Tulis strategi branching: `main`, `feature/<nama-modul>`, `bugfix/<deskripsi>`.
  - [ ] Tulis konvensi penamaan branch.
  - [ ] Tulis konvensi commit message: format, bahasa, contoh.
  - [ ] Tulis aturan `.gitignore`: file yang wajib dikecualikan (`.env`, `__pycache__`, `.pyc`, `exports/backups/`).
  - [ ] Tulis aturan code review: reviewer (Gemini 3 Flash), checklist review.

- [ ] **3.18. Tulis Bab 16 — Daftar Larangan Mutlak**
  - [ ] Buat tabel komprehensif seluruh praktik yang **DILARANG KERAS** dalam penulisan kode AbuCom:
    - Penggunaan `class` dan OOP di alur bisnis utama.
    - Penggunaan `float` untuk perhitungan keuangan/stok.
    - Penggunaan f-string / string formatting untuk SQL query.
    - Penggunaan wildcard import `from x import *`.
    - Hardcode kredensial di source code.
    - Hardcode path separator (`/` atau `\`).
    - Mutasi variabel global di fungsi bisnis.
    - Penggunaan `try-except` tanpa spesifik exception class.
    - Penggunaan encoding selain UTF-8.
    - Commit file `.env` ke Git repository.
    - Dan lain-lain sesuai temuan dari file referensi.

- [ ] **3.19. Tulis Bab 17 — Checklist Kepatuhan**
  - [ ] Buat tabel checklist self-review yang wajib dilengkapi developer sebelum commit/merge:
    - [ ] Apakah semua fungsi memiliki type hints?
    - [ ] Apakah semua fungsi memiliki docstring?
    - [ ] Apakah semua query SQL menggunakan parameterized binding `%s`?
    - [ ] Apakah semua perhitungan keuangan menggunakan `decimal.Decimal`?
    - [ ] Apakah tidak ada penggunaan `class` di alur bisnis?
    - [ ] Apakah kode berjalan di Windows dan Linux tanpa modifikasi?
    - [ ] Dan lain-lain sesuai aturan di bab-bab sebelumnya.

- [ ] **3.20. Tulis Bab 18 — Referensi Dokumen**
  - [ ] Buat tabel daftar seluruh file referensi yang digunakan dalam penyusunan dokumen ini (sesuai tabel di Bab 3 issue ini).
  - [ ] Sertakan path relatif, nama dokumen, versi, dan keterangan penggunaan.

---

### Tahap 4: Validasi dan Finalisasi

- [ ] **4.1.** Periksa ulang seluruh isi dokumen utama terhadap kerangka struktur di Bab 4 issue ini. Pastikan **TIDAK ADA** bab atau sub-bab yang terlewat.
- [ ] **4.2.** Periksa ulang konsistensi seluruh data numerik, nama pustaka, versi, dan konfigurasi teknis yang dikutip terhadap file referensi asli.
- [ ] **4.3.** Periksa ulang semua contoh kode Python yang diberikan:
  - [ ] Pastikan mengikuti paradigma FP murni (tanpa class).
  - [ ] Pastikan menggunakan `decimal.Decimal` untuk perhitungan.
  - [ ] Pastikan menggunakan parameterized queries `%s` untuk SQL.
  - [ ] Pastikan menggunakan `namedtuple` atau `frozen dataclass` untuk struktur data.
- [ ] **4.4.** Periksa ulang bahwa tidak ada bagian yang mengandung placeholder `[DATA_BELUM_TERSEDIA]` kecuali memang datanya benar-benar tidak tersedia dari file referensi.
- [ ] **4.5.** Periksa ulang bahwa bahasa Indonesia yang digunakan bersifat **natural, tidak ambigu, tidak membingungkan**, dan mudah dipahami oleh Junior Programmer atau AI model lain yang lebih murah.
- [ ] **4.6.** Periksa ulang bahwa seluruh format markdown sudah benar: heading, tabel, code block, list, bold, italic.
- [ ] **4.7.** Pastikan kualitas dan kelengkapan dokumen ini **cukup memadai** untuk langsung dijadikan referensi implementasi oleh developer tanpa perlu bertanya ulang atau menginterupsi proses pekerjaan fase SDLC selanjutnya.

---

### Tahap 5: Penulisan ke Target File

- [ ] **5.1.** Tuangkan **SELURUH** hasil pengerjaan dokumen utama ke dalam target file: `docs/sdlc/04_implementation/01_coding_standard.md`.
- [ ] **5.2.** Pastikan penulisan ke target file dilakukan secara **LENGKAP** dan **TIDAK TERPOTONG** (full overwrite, bukan append).
- [ ] **5.3.** Pastikan file target menggunakan encoding **UTF-8** dan line ending yang konsisten.
- [ ] **5.4.** Verifikasi bahwa file target sudah tertulis dengan benar dengan membaca kembali beberapa baris awal dan akhir file.

---

## 6. Instruksi Tambahan Spesifik Coding Standard

Berikut adalah instruksi tambahan yang merupakan kaidah standar pembuatan dokumen Coding Standard yang **WAJIB** diperhatikan:

- [ ] **6.1.** Setiap aturan dalam dokumen harus diklasifikasikan ke dalam salah satu tingkat kepatuhan: **WAJIB** (MUST), **DILARANG** (MUST NOT), **DIREKOMENDASIKAN** (SHOULD), atau **OPSIONAL** (MAY). Klasifikasi ini harus tertera secara eksplisit menggunakan label bold pada setiap aturan.
- [ ] **6.2.** Setiap aturan yang bersifat WAJIB atau DILARANG harus disertai dengan **justifikasi teknis** singkat (1-2 kalimat) mengapa aturan tersebut diterapkan.
- [ ] **6.3.** Setiap aturan yang melibatkan penulisan kode harus disertai dengan **contoh kode yang BENAR** (✅) dan **contoh kode yang SALAH** (❌) agar tidak ada ambiguitas implementasi.
- [ ] **6.4.** Untuk setiap pola desain fungsional di Bab 8, sediakan **template kode standar** (*boilerplate*) yang dapat di-copy-paste langsung oleh developer sebagai titik awal.
- [ ] **6.5.** Pastikan dokumen ini memuat informasi yang cukup untuk menjawab pertanyaan-pertanyaan implementasi umum berikut tanpa perlu membuka dokumen lain:
  - "Bagaimana cara membuat fungsi baru yang benar di AbuCom?"
  - "Bagaimana cara menulis query database yang aman?"
  - "Bagaimana cara menangani error secara fungsional?"
  - "Bagaimana cara mengelola state login tanpa class?"
  - "Bagaimana cara memastikan kode berjalan di Windows dan Linux?"
  - "Bagaimana struktur direktori proyek yang benar?"
  - "Apa saja yang dilarang dalam penulisan kode?"
- [ ] **6.6.** Gunakan diagram Mermaid untuk memvisualisasikan arsitektur 4-layer, alur dependensi antar-layer, dan pola-pola fungsional jika membantu pemahaman.
- [ ] **6.7.** Di setiap bab, jika ada aturan yang mengacu pada dokumen lain, sertakan referensi silang (*cross-reference*) ke dokumen asal dengan format: `(Ref: [Nama Dokumen] Bab X.Y)`.

---

## 7. Ringkasan Kriteria Kualitas Dokumen

| No | Kriteria | Standar |
|:---:|---|---|
| 1 | Kelengkapan bab dan sub-bab | Sesuai kerangka di Bab 4 issue ini, **TIDAK BOLEH** ada yang terlewat. |
| 2 | Keakuratan data teknis | Semua data (nama pustaka, versi, konfigurasi) **HARUS** konsisten dengan file referensi. |
| 3 | Contoh kode | Setiap aturan teknis **HARUS** memiliki contoh kode benar (✅) dan salah (❌). |
| 4 | Tingkat kepatuhan | Setiap aturan **HARUS** berlabel WAJIB/DILARANG/DIREKOMENDASIKAN/OPSIONAL. |
| 5 | Bahasa | Bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami. |
| 6 | Referensi silang | Setiap aturan yang berasal dari dokumen lain **HARUS** memiliki cross-reference. |
| 7 | Data kosong | Data yang tidak tersedia **HARUS** ditandai `[DATA_BELUM_TERSEDIA]`. |
| 8 | Referensi dokumen | Bab terakhir **HARUS** mencantumkan seluruh file referensi. |
| 9 | Self-contained | Dokumen **HARUS** cukup lengkap sebagai acuan mandiri untuk implementasi. |
| 10 | Tidak terpotong | File target **HARUS** ditulis secara lengkap tanpa truncation. |

---

## 8. Referensi File untuk Penyusunan Issue Ini

| No | Nama Dokumen | Path Relatif | Versi |
|:---:|---|---|:---:|
| 1 | Tech Stack Decision | `docs/sdlc/01_planning/04_tech_stack_decision.md` | v1.1 |
| 2 | System Architecture | `docs/sdlc/03_design/03_system_architecture.md` | v1.1 |
| 3 | Security Design | `docs/sdlc/03_design/06_security_design.md` | v1.1 |
| 4 | BOM & HPP Design | `docs/sdlc/03_design/05_bom_hpp_design.md` | v1.1 |
| 5 | CLI Interaction Flow | `docs/sdlc/03_design/04_cli_interaction_flow.md` | v1.1 |
| 6 | Software Requirements Specification | `docs/sdlc/02_analysis/02_software_requirements.md` | v1.1 |
| 7 | Database Schema (DDL SQL) | `docs/sdlc/03_design/01_database_schema.sql` | v1.1 |
| 8 | ERD Database | `docs/sdlc/03_design/02_erd_database.md` | v1.1 |
