# Pembuatan Dokumen Module Structure

---

| Atribut         | Nilai                                                                      |
| :-------------- | :------------------------------------------------------------------------- |
| **Judul**       | Pembuatan dan Penyusunan Dokumen Module Structure                          |
| **Dokumen Utama** | Module Structure                                                         |
| **Target File** | `docs/sdlc/04_implementation/03_module_structure.md`                       |
| **Fase SDLC**   | Fase 04 — Implementation (Konstruksi)                                      |
| **Prioritas**   | High                                                                       |
| **Status**      | Open                                                                       |
| **Tanggal Dibuat** | 2026-05-26                                                              |
| **Estimasi Deliverable** | Deliverable ketiga pada Fase 04 Implementation                    |

---

## 1. Persona Pelaksana

**Persona**: `Senior Software Architect & Module Decomposition Specialist`

**Justifikasi Pemilihan Persona**:
Dokumen Module Structure merupakan cetak biru teknis (blueprint) yang memetakan dekomposisi seluruh kode program ke dalam modul-modul fungsional, paket direktori, dan file Python spesifik. Dokumen ini memerlukan keahlian arsitektural dalam menerjemahkan arsitektur logis 4-layer dan 10 modul fungsional (dari System Architecture) menjadi peta file-level detail yang bisa langsung digunakan programmer untuk menulis kode. Persona ini memiliki otoritas penuh dalam:
- Menentukan pemetaan modul fungsional → file Python → fungsi publik.
- Menentukan pola dependensi impor antar-file secara searah (top-down).
- Menentukan kontrak antarmuka (interface contract) setiap file modul.
- Memastikan kepatuhan terhadap prinsip FP murni, arsitektur berlapis, dan Coding Standard v1.1.

---

## 2. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca dan dirangkum** secara menyeluruh sebagai dasar utama penyusunan dokumen Module Structure. File-file dipilih berdasarkan relevansi langsung terhadap dekomposisi modul dan struktur kode:

| No | File Referensi | Path Relatif | Prioritas | Alasan Pemilihan |
| :---: | --- | --- | :---: | --- |
| 1 | **System Architecture v1.1** | `docs/sdlc/03_design/03_system_architecture.md` | **PRIMER** | Sumber utama arsitektur berlapis 4-layer, dekomposisi 10 modul fungsional (M.1—M.10), matriks dependensi antar-modul, peta module-to-table database mapping, dan deskripsi tanggung jawab setiap modul. |
| 2 | **Coding Standard v1.1** | `docs/sdlc/04_implementation/01_coding_standard.md` | **PRIMER** | Sumber utama layout direktori proyek standar (`cli/`, `logic/`, `db/`, `middleware/`, `config/`, `utils/`, `tests/`, `exports/`), konvensi penamaan file, aturan penempatan file baru, dan pola desain FP (NamedTuple, State Dict Passing, Result Pattern, Transaction Wrapper, Connection Pool). |
| 3 | **Software Requirements Specification (SRS) v1.1** | `docs/sdlc/02_analysis/02_software_requirements.md` | **PRIMER** | Sumber spesifikasi teknis 40+ kebutuhan fungsional (SRS-F-001 s.d SRS-F-040), input/output setiap fitur, logika bisnis, aturan validasi, dan penanganan exception — yang semuanya harus dipetakan ke file modul spesifik. |
| 4 | **CLI Interaction Flow v1.1** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | **SEKUNDER** | Sumber peta hierarki menu CLI global, matriks visibilitas menu per role (8 peran), alur interaksi 44 use case (UC-001 s.d UC-044), dan ID menu yang harus dipetakan ke file handler di `cli/`. |
| 5 | **Database Schema v1.1 (DDL SQL)** | `docs/sdlc/03_design/01_database_schema.sql` | **SEKUNDER** | Referensi 28 tabel InnoDB fisik, kolom, tipe data, foreign key, dan triggers — untuk memvalidasi peta module-to-table dan memastikan setiap tabel tercakup oleh file query di `db/`. |
| 6 | **Security Design v1.1** | `docs/sdlc/03_design/06_security_design.md` | **SEKUNDER** | Referensi modul keamanan (bcrypt, JWT, RBAC, audit trail, sanitasi CLI, UU PDP Fernet) — untuk memastikan cross-cutting concerns di `middleware/` dan `utils/` terdefinisi lengkap. |
| 7 | **Access Control Matrix v1.1** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | **SEKUNDER** | Referensi otorisasi granular per menu per role — untuk validasi RBAC guard di `middleware/rbac_guard.py`. |
| 8 | **BOM & HPP Design v1.1** | `docs/sdlc/03_design/05_bom_hpp_design.md` | **TERSIER** | Referensi pseudocode pure FP kalkulasi HPP desimal — untuk validasi pemetaan fungsi di `logic/bom_hpp.py`. |
| 9 | **ERD Database v1.1** | `docs/sdlc/03_design/02_erd_database.md` | **TERSIER** | Referensi visual relasi Crow's Foot 58 FK dan kardinalitas — untuk validasi dependensi data antar-modul. |
| 10 | **Environment Setup v1.1** | `docs/sdlc/04_implementation/02_environment_setup.md` | **TERSIER** | Referensi requirements.txt, .env template, dan konfigurasi virtual environment — untuk validasi kelengkapan entry point dan file konfigurasi. |

> **Catatan**: File `narasi.txt` (`docs/sdlc/narasi.txt`) **tidak diperlukan** lagi sebagai referensi untuk dokumen ini, karena seluruh informasi yang relevan dari narasi sudah terabstraksi secara lengkap ke dalam dokumen-dokumen SDLC di atas (terutama SRS, System Architecture, dan Coding Standard).

---

## 3. Kerangka Struktur Dokumen Utama

Dokumen Module Structure wajib disusun menggunakan kerangka struktur berikut, yang merupakan standar praktik industri (*Software Module Specification*) yang disesuaikan dengan konteks proyek AbuCom:

```
---
dokumen    : Module Structure
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [TANGGAL PENGERJAAN]
status     : Draft
penyusun   : Senior Software Architect & Module Decomposition Specialist
---

# Module Structure — AbuCom

## Riwayat Perubahan Dokumen
(Tabel riwayat versi: Versi, Tanggal, Perubahan, Oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya (Input & Output)
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan

---

## 2. Arsitektur Modular Overview
### 2.1. Diagram Arsitektur Berlapis 4-Layer (Mermaid)
### 2.2. Aturan Dependensi Antar-Layer (Satu Arah Top-Down)
### 2.3. Ringkasan 10 Modul Fungsional (Tabel)
### 2.4. Diagram Dekomposisi Modul ke Layer (Mermaid)

---

## 3. Layout Direktori Proyek Lengkap
### 3.1. Diagram Tree Direktori (ASCII)
### 3.2. Penjelasan Tujuan Setiap Direktori
### 3.3. Aturan Penempatan File Baru

---

## 4. Spesifikasi Modul — Layer 1: Presentation (cli/)
### 4.1. File: cli/__init__.py
### 4.2. File: cli/dashboard.py
### 4.3. File: cli/menu_transaksi.py
### 4.4. File: cli/menu_inventaris.py
### 4.5. File: cli/menu_ppob_service.py
### 4.6. File: cli/menu_sdm_finansial.py
### 4.7. File: cli/menu_configs.py

(Setiap file harus didokumentasikan dengan format:)
- Tujuan / Tanggung Jawab File
- Modul Fungsional Terkait (M.x)
- Daftar Fungsi Publik (nama fungsi, parameter, return type, deskripsi singkat)
- Dependensi Impor (file mana yang diimpor)
- Hubungan dengan Use Case / Menu ID
- Tabel Database yang Diakses (jika ada, via layer 3)
- Hak Akses / RBAC Role yang Diizinkan

---

## 5. Spesifikasi Modul — Layer 2: Business Logic (logic/)
### 5.1. File: logic/__init__.py
### 5.2. File: logic/bom_hpp.py
### 5.3. File: logic/smart_payroll.py
### 5.4. File: logic/financial_engine.py
### 5.5. File: logic/safety_validator.py

(Setiap file harus didokumentasikan dengan format sama seperti Bab 4, ditambah:)
- Aturan FP Murni yang Berlaku (pure functions, immutability, decimal-first)
- Contoh Signature Fungsi (dengan type hints lengkap)
- Modul SRS yang Di-cover (SRS-F-xxx)

---

## 6. Spesifikasi Modul — Layer 3: Data Access (db/)
### 6.1. File: db/__init__.py
### 6.2. File: db/db_connector.py
### 6.3. File: db/query_builder.py

(Setiap file harus didokumentasikan dengan format sama, ditambah:)
- Pola Connection Pooling & Retry Mechanism
- Pola Transaction Wrapper ACID
- Peta Query ke Tabel Database (module-to-table mapping)
- Konvensi Parameterized Query (%s bindings)

---

## 7. Spesifikasi Modul — Cross-cutting Concerns: Middleware (middleware/)
### 7.1. File: middleware/__init__.py
### 7.2. File: middleware/auth_jwt.py
### 7.3. File: middleware/rbac_guard.py
### 7.4. File: middleware/audit_logger.py

(Setiap file harus didokumentasikan dengan format sama, ditambah:)
- Integrasi dengan Security Design v1.1
- Referensi Access Control Matrix

---

## 8. Spesifikasi Modul — Configuration (config/)
### 8.1. File: config/__init__.py
### 8.2. File: config/settings.py

---

## 9. Spesifikasi Modul — Utilities (utils/)
### 9.1. File: utils/__init__.py
### 9.2. File: utils/crypto.py
### 9.3. File: utils/backup.py
### 9.4. File: utils/text_formatter.py

---

## 10. Spesifikasi Modul — Entry Point & Konfigurasi Root
### 10.1. File: main.py
### 10.2. File: requirements.txt
### 10.3. File: .env.example
### 10.4. File: .gitignore

---

## 11. Spesifikasi Modul — Testing (tests/)
### 11.1. File: tests/__init__.py
### 11.2. File: tests/test_bom_hpp.py
### 11.3. File: tests/test_rbac_security.py

---

## 12. Spesifikasi Modul — Output Directories (exports/)
### 12.1. Direktori: exports/backups/
### 12.2. Direktori: exports/designs/
### 12.3. Direktori: exports/receipts/

---

## 13. Matriks Pemetaan Modul Fungsional ke File (Module-to-File Mapping)
(Tabel lengkap: Modul M.1—M.10 → File Python di setiap layer)

---

## 14. Matriks Pemetaan SRS ke File (SRS-to-File Traceability)
(Tabel lengkap: SRS-F-xxx → File Python handler utama)

---

## 15. Matriks Pemetaan Tabel Database ke File (Table-to-File Mapping)
(Tabel lengkap: 28 Tabel MySQL → File query handler di db/ & file logika di logic/)

---

## 16. Matriks Dependensi Impor Antar-File (Inter-File Import Matrix)
(Diagram Mermaid atau tabel yang memetakan relasi impor antar-file Python)

---

## 17. Diagram Alur Dependensi Modul (Mermaid)
(Diagram visual yang menggambarkan aliran dependensi 10 modul melalui file-file Python)

---

## 18. Persetujuan dan Otorisasi

---

## 19. Glosarium

---

## 20. Referensi Dokumen
(Tabel daftar file referensi yang digunakan beserta path relatif dan keterangan penggunaan)
```

---

## 4. Instruksi Detail Langkah Demi Langkah

### Fase A: Persiapan dan Pembacaan File Referensi

- [ ] **A.1.** Baca dan pahami file referensi berikut secara menyeluruh (jangan skip satupun bagian):
  - [ ] A.1.1. Baca `docs/sdlc/03_design/03_system_architecture.md` — fokus pada:
    - Bab 4 (Arsitektur Perangkat Lunak Logis — 4-Layer)
    - Bab 5 (Arsitektur Modular — Dekomposisi 10 Modul, Deskripsi Tanggung Jawab, Matriks Dependensi, Peta Module-to-Table)
    - Bab 7 (Arsitektur Keamanan — RBAC Matrix)
    - Bab 8 (Arsitektur Komunikasi — Sequence Diagrams)
  - [ ] A.1.2. Baca `docs/sdlc/04_implementation/01_coding_standard.md` — fokus pada:
    - Bab 4 (Struktur Direktori Proyek — Layout, Penjelasan per Direktori)
    - Bab 8 (Arsitektur Kode dan Pola Desain Fungsional — 4-Layer, Pure Functions, State Dict, Closures, Result Pattern, Transaction Wrapper, Connection Pool)
    - Bab 3 (Konvensi Penamaan — file, fungsi, variabel, NamedTuple)
    - Bab 7 (Standar Type Hints)
    - Bab 13 (Dependensi)
  - [ ] A.1.3. Baca `docs/sdlc/02_analysis/02_software_requirements.md` — fokus pada:
    - Bab 1.2 (Cakupan — Ringkasan 10 Modul)
    - Bab 2.3 (Klasifikasi 8 Aktor)
    - Bab 3 (Seluruh Spesifikasi Kebutuhan Fungsional — SRS-F-001 s.d SRS-F-040): catat setiap SRS-F beserta modul terkaitnya, input/output, dan fungsi kalkulasi yang dibutuhkan
  - [ ] A.1.4. Baca `docs/sdlc/03_design/04_cli_interaction_flow.md` — fokus pada:
    - Bab 3 (Peta Hierarki Menu CLI Global — Diagram dan Tabel Deskripsi Menu)
    - Bab 3.3 (Matriks Visibilitas Menu per Role)
    - Bab 4-14 (Alur Interaksi Detail 44 Use Case — catat menu ID, aktor, dan fitur)
  - [ ] A.1.5. Baca `docs/sdlc/03_design/01_database_schema.sql` — catat:
    - Daftar lengkap 28 tabel database beserta kolomnya
    - Foreign key relationships
    - Triggers dan composite index
  - [ ] A.1.6. Baca `docs/sdlc/03_design/06_security_design.md` — fokus pada:
    - Modul keamanan: bcrypt, JWT, RBAC, audit trail, sanitasi, UU PDP
    - Komponen yang harus ada di `middleware/` dan `utils/`
  - [ ] A.1.7. Baca `docs/sdlc/02_analysis/06_access_control_matrix.md` — catat:
    - Matriks otorisasi granular per menu per role
  - [ ] A.1.8. Baca `docs/sdlc/03_design/05_bom_hpp_design.md` — catat:
    - Pseudocode FP kalkulasi HPP dan BOM
  - [ ] A.1.9. Baca `docs/sdlc/03_design/02_erd_database.md` — catat:
    - Relasi visual FK dan kardinalitas antar-tabel
  - [ ] A.1.10. Baca `docs/sdlc/04_implementation/02_environment_setup.md` — catat:
    - Layout direktori proyek (Bab 8.1)
    - Template .env.example (Bab 8.2)
    - Daftar requirements.txt (Bab 7.3)

### Fase B: Pengolahan dan Pemetaan Data

- [ ] **B.1.** Buat rangkuman internal (catatan kerja) yang merangkum:
  - [ ] B.1.1. Daftar lengkap 10 modul fungsional (M.1 — M.10) beserta tanggung jawab, tabel terkait, dan hak akses aktor dari System Architecture Bab 5.
  - [ ] B.1.2. Matriks dependensi antar-modul dari System Architecture Bab 5.3.
  - [ ] B.1.3. Peta module-to-table dari System Architecture Bab 5.4.
  - [ ] B.1.4. Layout direktori proyek lengkap dari Coding Standard Bab 4.1.
  - [ ] B.1.5. Daftar seluruh SRS-F (SRS-F-001 s.d SRS-F-040) beserta modul terkait dan fungsi yang dibutuhkan.
  - [ ] B.1.6. Daftar seluruh Menu ID (MENU-M1-001 s.d MENU-M10-001 dan MENU-BASE-001 s.d MENU-BASE-004) beserta Use Case terkait.
  - [ ] B.1.7. Daftar 28 tabel database beserta kelompoknya (A, B, C, D, E).
  - [ ] B.1.8. Daftar komponen keamanan yang harus dipetakan ke middleware/ dan utils/.
  - [ ] B.1.9. Daftar pola desain FP (NamedTuple, Result Pattern, State Dict Passing, Closures, HOF, Transaction Wrapper, Connection Pool) dari Coding Standard Bab 8.

- [ ] **B.2.** Lakukan pemetaan silang (cross-mapping):
  - [ ] B.2.1. Petakan setiap modul fungsional (M.1—M.10) → file Python spesifik di setiap layer (`cli/`, `logic/`, `db/`, `middleware/`).
  - [ ] B.2.2. Petakan setiap SRS-F → file Python handler utama.
  - [ ] B.2.3. Petakan setiap tabel database (28 tabel) → file Python yang mengaksesnya.
  - [ ] B.2.4. Petakan setiap Menu ID → file Python handler di `cli/`.
  - [ ] B.2.5. Petakan setiap Use Case (UC-001 s.d UC-044) → file Python handler utama.
  - [ ] B.2.6. Tentukan dependensi impor antar-file (pastikan aliran impor searah: cli → logic → db, middleware bersifat cross-cutting).

### Fase C: Penulisan Dokumen

- [ ] **C.1.** Tulis metadata header YAML (dokumen, proyek, versi, tanggal, status, penyusun).
- [ ] **C.2.** Tulis tabel Riwayat Perubahan Dokumen (versi 1.0, tanggal pengerjaan, deskripsi perubahan, nama persona).
- [ ] **C.3.** Tulis Bab 1 — Informasi Dokumen:
  - [ ] C.3.1. Tujuan Dokumen: jelaskan bahwa dokumen ini memetakan seluruh modul kode program ke file-file Python spesifik.
  - [ ] C.3.2. Cakupan Dokumen: sebutkan cakupan (dekomposisi file, fungsi publik, dependensi impor, peta SRS-to-file, peta table-to-file).
  - [ ] C.3.3. Posisi Dokumen dalam SDLC: jelaskan posisi sebagai deliverable ketiga Fase 04 Implementation, setelah Coding Standard dan Environment Setup.
  - [ ] C.3.4. Hubungan dengan Dokumen Lainnya: tulis daftar dokumen input (acuan) dan output (penerima manfaat).
  - [ ] C.3.5. Audiens Target.
  - [ ] C.3.6. Definisi, Akronim, dan Singkatan.
- [ ] **C.4.** Tulis Bab 2 — Arsitektur Modular Overview:
  - [ ] C.4.1. Diagram Arsitektur Berlapis 4-Layer (Mermaid) — adaptasi dari System Architecture Bab 4.2.
  - [ ] C.4.2. Aturan Dependensi Antar-Layer.
  - [ ] C.4.3. Tabel Ringkasan 10 Modul Fungsional (M.1—M.10 dengan tanggung jawab singkat).
  - [ ] C.4.4. Diagram Dekomposisi Modul ke Layer (Mermaid baru yang menunjukkan mapping M.x → folder layer).
- [ ] **C.5.** Tulis Bab 3 — Layout Direktori Proyek Lengkap:
  - [ ] C.5.1. Diagram Tree Direktori (ASCII) — dari Coding Standard Bab 4.1, pastikan lengkap.
  - [ ] C.5.2. Penjelasan tujuan setiap direktori.
  - [ ] C.5.3. Aturan penempatan file baru.
- [ ] **C.6.** Tulis Bab 4 — Spesifikasi Modul Layer 1: Presentation (`cli/`):
  - [ ] C.6.1. Untuk setiap file di `cli/` (dashboard.py, menu_transaksi.py, menu_inventaris.py, menu_ppob_service.py, menu_sdm_finansial.py, menu_configs.py, __init__.py), tulis:
    - Tujuan / Tanggung Jawab File
    - Modul Fungsional Terkait (M.x)
    - Daftar Fungsi Publik beserta parameter, return type, dan deskripsi singkat
    - Dependensi Impor (file mana yang diimpor dari logic/ dan middleware/)
    - Hubungan dengan Use Case / Menu ID (tulis mapping UC-xxx dan MENU-Mx-xxx)
    - Tabel Database yang Diakses (via layer 3)
    - Hak Akses RBAC Role yang Diizinkan
  - [ ] C.6.2. Pastikan setiap Use Case (UC-001 s.d UC-044) tercakup di salah satu file cli/.
- [ ] **C.7.** Tulis Bab 5 — Spesifikasi Modul Layer 2: Business Logic (`logic/`):
  - [ ] C.7.1. Untuk setiap file di `logic/` (bom_hpp.py, smart_payroll.py, financial_engine.py, safety_validator.py, __init__.py), tulis format yang sama + aturan FP murni, contoh signature fungsi, dan SRS yang di-cover.
  - [ ] C.7.2. Pastikan setiap fungsi kalkulasi yang disebutkan di SRS (HPP BOM, Smart Payroll, Depresiasi Aset, Margin, dll.) tercakup di salah satu file logic/.
- [ ] **C.8.** Tulis Bab 6 — Spesifikasi Modul Layer 3: Data Access (`db/`):
  - [ ] C.8.1. Untuk setiap file di `db/` (db_connector.py, query_builder.py, __init__.py), tulis format yang sama + pola Connection Pooling, Retry Mechanism, Transaction Wrapper, konvensi Parameterized Query.
  - [ ] C.8.2. Tulis peta query ke tabel database yang komprehensif.
- [ ] **C.9.** Tulis Bab 7 — Spesifikasi Modul Cross-cutting: Middleware (`middleware/`):
  - [ ] C.9.1. Untuk setiap file di `middleware/` (auth_jwt.py, rbac_guard.py, audit_logger.py, __init__.py), tulis format yang sama + integrasi dengan Security Design dan Access Control Matrix.
- [ ] **C.10.** Tulis Bab 8 — Spesifikasi Modul Configuration (`config/`):
  - [ ] C.10.1. Untuk setiap file di `config/` (settings.py, __init__.py), tulis format yang sama + variabel .env yang dikelola.
- [ ] **C.11.** Tulis Bab 9 — Spesifikasi Modul Utilities (`utils/`):
  - [ ] C.11.1. Untuk setiap file di `utils/` (crypto.py, backup.py, text_formatter.py, __init__.py), tulis format yang sama.
- [ ] **C.12.** Tulis Bab 10 — Spesifikasi Entry Point & Konfigurasi Root:
  - [ ] C.12.1. Spesifikasi main.py (entry point, alur startup, validasi .env).
  - [ ] C.12.2. Spesifikasi requirements.txt.
  - [ ] C.12.3. Spesifikasi .env.example.
  - [ ] C.12.4. Spesifikasi .gitignore.
- [ ] **C.13.** Tulis Bab 11 — Spesifikasi Modul Testing (`tests/`):
  - [ ] C.13.1. Untuk setiap file di `tests/` (test_bom_hpp.py, test_rbac_security.py, __init__.py), tulis format yang sama + target coverage.
- [ ] **C.14.** Tulis Bab 12 — Spesifikasi Output Directories (`exports/`):
  - [ ] C.14.1. Penjelasan tujuan setiap subdirektori (backups/, designs/, receipts/).
- [ ] **C.15.** Tulis Bab 13 — Matriks Pemetaan Modul Fungsional ke File (Module-to-File Mapping):
  - [ ] C.15.1. Buat tabel lengkap: kolom = Layer (cli, logic, db, middleware, utils), baris = Modul M.1—M.10, isi = file Python terkait.
- [ ] **C.16.** Tulis Bab 14 — Matriks Pemetaan SRS ke File (SRS-to-File Traceability):
  - [ ] C.16.1. Buat tabel: SRS-F-xxx → File handler utama di cli/, logic/, dan db/.
- [ ] **C.17.** Tulis Bab 15 — Matriks Pemetaan Tabel Database ke File (Table-to-File Mapping):
  - [ ] C.17.1. Buat tabel: 28 Tabel MySQL → File query handler di db/ + file logika di logic/.
- [ ] **C.18.** Tulis Bab 16 — Matriks Dependensi Impor Antar-File (Inter-File Import Matrix):
  - [ ] C.18.1. Buat diagram Mermaid atau tabel yang menunjukkan relasi impor antar-file Python — pastikan aliran impor searah (atas ke bawah).
- [ ] **C.19.** Tulis Bab 17 — Diagram Alur Dependensi Modul (Mermaid):
  - [ ] C.19.1. Buat diagram visual lengkap yang menggambarkan aliran dependensi 10 modul melalui file-file Python (adaptasi dari System Architecture Bab 5.3 tapi di level file).
- [ ] **C.20.** Tulis Bab 18 — Persetujuan dan Otorisasi:
  - [ ] C.20.1. Buat tabel persetujuan (Peran, Nama, Tanda Tangan, Tanggal).
- [ ] **C.21.** Tulis Bab 19 — Glosarium:
  - [ ] C.21.1. Buat daftar istilah teknis yang digunakan dalam dokumen beserta definisi singkat.
- [ ] **C.22.** Tulis Bab 20 — Referensi Dokumen:
  - [ ] C.22.1. Buat tabel daftar seluruh file referensi yang digunakan beserta path relatif dan keterangan penggunaan.

### Fase D: Validasi dan Finalisasi

- [ ] **D.1.** Validasi kelengkapan dokumen:
  - [ ] D.1.1. Pastikan seluruh 10 modul fungsional (M.1—M.10) tercakup dalam spesifikasi file.
  - [ ] D.1.2. Pastikan seluruh file yang ada di layout direktori Coding Standard tercakup dalam dokumen.
  - [ ] D.1.3. Pastikan seluruh SRS-F (SRS-F-001 s.d SRS-F-040) tercakup di matriks SRS-to-File.
  - [ ] D.1.4. Pastikan seluruh 28 tabel database tercakup di matriks Table-to-File.
  - [ ] D.1.5. Pastikan seluruh Use Case (UC-001 s.d UC-044) tercakup di matriks.
  - [ ] D.1.6. Pastikan seluruh Menu ID tercakup di spesifikasi file cli/.
  - [ ] D.1.7. Pastikan aliran dependensi impor antar-file berjalan searah (cli → logic → db).
  - [ ] D.1.8. Pastikan tidak ada cross-layer violation (file logic/ tidak mengimpor dari cli/).

- [ ] **D.2.** Tandai data kosong:
  - [ ] D.2.1. Jika ada data yang tidak ditemukan di file referensi (misalnya fungsi spesifik yang belum terdefinisi), tandai dengan format: `⚠️ **[PERLU DIISI MANUAL]**: [deskripsi data yang kosong]`.

- [ ] **D.3.** Validasi kualitas penulisan:
  - [ ] D.3.1. Pastikan bahasa Indonesia yang digunakan natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau AI model lain yang lebih murah.
  - [ ] D.3.2. Pastikan setiap istilah teknis asing (bahasa Inggris) yang pertama kali muncul disertai penjelasan singkat dalam bahasa Indonesia.
  - [ ] D.3.3. Pastikan format tabel, diagram Mermaid, dan kode contoh tersintaks dengan benar.
  - [ ] D.3.4. Pastikan setiap bab memiliki isi substansial (bukan hanya judul kosong).

- [ ] **D.4.** Validasi dokumen layak jadi referensi:
  - [ ] D.4.1. Pastikan isi dokumen ini cukup detail dan lengkap untuk dijadikan acuan langsung oleh programmer yang akan menulis kode setiap file Python (tanpa perlu bertanya balik atau mencari informasi tambahan di dokumen lain).
  - [ ] D.4.2. Pastikan setiap file Python yang disebutkan memiliki spesifikasi fungsi publik yang jelas (nama, parameter, return type, deskripsi) sehingga programmer dapat langsung menulis implementasinya.

### Fase E: Penulisan ke Target File

- [ ] **E.1.** Tuangkan seluruh hasil pengerjaan ke target file: `docs/sdlc/04_implementation/03_module_structure.md`.
- [ ] **E.2.** Pastikan file ditulis dengan encoding UTF-8.
- [ ] **E.3.** Pastikan file **menimpa/overwrite** seluruh isi file target yang sudah ada (file saat ini masih kosong).

---

## 5. Instruksi Tambahan Spesifik Dokumen Module Structure

### 5.1. Tingkat Granularitas Spesifikasi Fungsi
Untuk setiap file Python, daftar fungsi publik harus mencakup **minimal** informasi berikut:

```
| No | Nama Fungsi | Parameter | Return Type | Deskripsi | SRS Terkait |
|----|-------------|-----------|-------------|-----------|-------------|
| 1  | nama_fungsi | (param1: type, param2: type) | ReturnType | Deskripsi singkat | SRS-F-xxx |
```

### 5.2. Penanganan Modul yang Belum Terdefinisi Eksplisit
Jika dari analisis SRS dan System Architecture ditemukan kebutuhan fungsional yang belum terwakili oleh file yang ada di layout Coding Standard, maka:
- Usulkan file baru yang perlu ditambahkan (dengan justifikasi).
- Tempatkan file baru sesuai aturan penempatan layer.
- Tandai dengan keterangan: `📌 **[FILE BARU DIUSULKAN]**: [alasan penambahan]`.

### 5.3. Konsistensi Penamaan Fungsi
Semua nama fungsi yang dicantumkan dalam spesifikasi harus mematuhi konvensi `snake_case` (verb_noun) sesuai Coding Standard Bab 3.2. Contoh:
- ✅ `hitung_hpp_bom()`, `verifikasi_login_user()`, `format_struk_nota()`
- ❌ `HitungHPP()`, `login()`, `process()`

### 5.4. Pendokumentasian NamedTuple dan Data Structure
Untuk setiap file di `logic/`, dokumentasikan juga NamedTuple atau frozen Dataclass yang didefinisikan di file tersebut (nama, field, tipe data). Contoh:

```
| NamedTuple | Fields | Tipe Data Fields |
|------------|--------|------------------|
| BOMItem    | bahan_baku_id, qty_pemakaian, harga_beli | int, Decimal, Decimal |
```

### 5.5. Diagram Mermaid Wajib
Dokumen ini wajib memuat **minimal** diagram Mermaid berikut:
1. Diagram Arsitektur Berlapis 4-Layer (adaptasi dari System Architecture).
2. Diagram Dekomposisi Modul ke Layer (mapping M.x → folder layer).
3. Diagram Dependensi Impor Antar-File (menunjukkan aliran impor searah).
4. Diagram Alur Dependensi Modul melalui File (detail level file).

### 5.6. Catatan tentang Kelengkapan
Dokumen ini harus disusun sedemikian rupa sehingga **tidak memunculkan pertanyaan lanjutan** yang akan menghambat proses pengerjaan fase SDLC selanjutnya (yaitu penulisan kode program aktual). Jika ada informasi yang masih ambigu dari file referensi, buatlah keputusan yang paling masuk akal dan tandai sebagai asumsi yang bisa direvisi.

---

## 6. Kriteria Penerimaan (Acceptance Criteria)

- [ ] Dokumen berhasil ditulis ke target file `docs/sdlc/04_implementation/03_module_structure.md`.
- [ ] Seluruh 20 bab sesuai kerangka struktur terisi substansial (tidak ada bab kosong).
- [ ] Seluruh 10 modul fungsional (M.1—M.10) tercakup dalam spesifikasi file.
- [ ] Seluruh file Python di layout direktori Coding Standard tercakup dan terdokumentasi.
- [ ] Minimal 4 diagram Mermaid tersedia (4-Layer, Dekomposisi Modul, Import Matrix, Dependensi Modul).
- [ ] Matriks Module-to-File, SRS-to-File, Table-to-File, dan Inter-File Import terisi lengkap.
- [ ] Setiap file memiliki daftar fungsi publik dengan parameter, return type, dan deskripsi.
- [ ] Bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami.
- [ ] Data kosong ditandai dengan `⚠️ **[PERLU DIISI MANUAL]**`.
- [ ] Bab Referensi Dokumen berisi daftar lengkap file yang dijadikan acuan.
- [ ] Dokumen layak dijadikan input untuk fase pengkodean modul (Fase 04 berikutnya).

---

## 7. Referensi File untuk Issue Ini

| No | File Referensi | Path Relatif |
| :---: | --- | --- |
| 1 | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` |
| 2 | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` |
| 3 | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| 4 | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` |
| 5 | Database Schema v1.1 (DDL SQL) | `docs/sdlc/03_design/01_database_schema.sql` |
| 6 | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` |
| 7 | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` |
| 8 | BOM & HPP Design v1.1 | `docs/sdlc/03_design/05_bom_hpp_design.md` |
| 9 | ERD Database v1.1 | `docs/sdlc/03_design/02_erd_database.md` |
| 10 | Environment Setup v1.1 | `docs/sdlc/04_implementation/02_environment_setup.md` |
