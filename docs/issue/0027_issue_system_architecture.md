---
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
target     : docs/sdlc/03_design/03_system_architecture.md
prioritas  : High
status     : Open
tanggal    : 2026-05-24
estimasi   : 4–6 jam kerja
assignee   : Junior Programmer / LLM Model AI (Gemini 3.1 Pro Low / GPT-OSS 120B Medium)
---

# Pembuatan & Penyusunan Dokumen System Architecture

## 1. Ringkasan Issue

Issue ini berisi **perencanaan low-level** untuk pembuatan dan penyusunan dokumen **System Architecture** proyek AbuCom. Dokumen ini merupakan deliverable ketiga pada **Fase 03 Design** dalam siklus SDLC AbuCom, setelah `01_database_schema.sql` dan `02_erd_database.md`.

Dokumen System Architecture bertujuan menyediakan cetak biru arsitektur sistem secara menyeluruh — mencakup topologi infrastruktur fisik, arsitektur perangkat lunak logis, pola desain modular, alur komunikasi antar-komponen, strategi keamanan berlapis, strategi deployment, serta panduan operasional — yang menjadi acuan utama bagi tim pengembang saat memasuki fase implementasi (coding).

---

## 2. Persona Pelaksana

**Persona yang ditugaskan**: **Senior Solutions Architect & System Design Lead**

**Justifikasi pemilihan persona**:
- Persona ini memiliki otoritas dan kompetensi dalam merancang arsitektur sistem end-to-end, mulai dari infrastruktur fisik (jaringan, server, klien) hingga arsitektur perangkat lunak logis (modular, layer, pattern).
- Memiliki pandangan holistik terhadap keamanan, performa, skalabilitas, dan maintainability sistem.
- Mampu menerjemahkan kebutuhan teknis dari SRS dan keputusan teknologi dari Tech Stack Decision menjadi blueprint arsitektur yang actionable untuk implementasi.

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca secara menyeluruh** sebelum memulai penyusunan dokumen. Setiap file diurutkan berdasarkan prioritas relevansinya terhadap dokumen System Architecture:

### 3.1. Referensi PRIMER (Wajib dibaca utuh, setiap detail penting)

| No | File Referensi | Path Relatif | Alasan Penggunaan |
|----|---------------|-------------|-------------------|
| 1 | **Tech Stack Decision v1.1** | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Sumber kebenaran tunggal untuk seluruh keputusan teknologi, arsitektur Client-Server LAN, paradigma FP, pustaka, platform OS, topologi jaringan, strategi keamanan, dan prinsip arsitektur panduan. Dokumen ini adalah **fondasi utama** dokumen System Architecture. |
| 2 | **Software Requirements Specification (SRS) v1.1** | `docs/sdlc/02_analysis/02_software_requirements.md` | Spesifikasi 10 modul fungsional, kebutuhan non-fungsional (performa, keamanan, presisi desimal), batasan desain & implementasi, dan lingkungan operasi. Menyediakan **kebutuhan yang harus diakomodasi** oleh arsitektur. |
| 3 | **Database Schema (DDL SQL) v1.1** | `docs/sdlc/03_design/01_database_schema.sql` | Skema fisik 28 tabel MySQL aktual yang harus direpresentasikan dalam arsitektur layer data/persistence. Menyediakan struktur data konkret untuk mapping arsitektural. |

### 3.2. Referensi SEKUNDER (Dibaca untuk konteks dan konsistensi)

| No | File Referensi | Path Relatif | Alasan Penggunaan |
|----|---------------|-------------|-------------------|
| 4 | **ERD Database v1.1** | `docs/sdlc/03_design/02_erd_database.md` | Visualisasi relasi antar-entitas (58 FK, 28 tabel, 5 kelompok fungsional). Menjadi input untuk diagram arsitektur layer data dan pemetaan modul-ke-tabel. |
| 5 | **Use Case Diagram (UCD) v1.1** | `docs/sdlc/02_analysis/03_use_case_diagram.md` | Pemetaan 8 aktor internal, 4 aktor eksternal, dan 44 use case. Menjadi input untuk diagram arsitektur layer presentasi CLI dan pemetaan RBAC ke modul. |
| 6 | **Workflow Diagram v1.1** | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Alur kerja operasional (As-Is dan To-Be) per modul. Menjadi input untuk sequence/interaction diagram dan pemetaan alur data lintas modul. |
| 7 | **Project Charter v1.1** | `docs/sdlc/01_planning/01_project_charter.md` | Batasan ruang lingkup proyek, susunan tim pengembang AI, jadwal, dan target milestone. |

### 3.3. Referensi TERSIER (Dibaca jika diperlukan data pelengkap)

| No | File Referensi | Path Relatif | Alasan Penggunaan |
|----|---------------|-------------|-------------------|
| 8 | **Business Requirements Document (BRD) v1.1** | `docs/sdlc/02_analysis/01_business_requirements.md` | Kebutuhan bisnis tingkat tinggi untuk validasi bahwa arsitektur mengakomodasi seluruh kebutuhan. |
| 9 | **Stakeholder Register v1.1** | `docs/sdlc/01_planning/03_stakeholder_register.md` | Pemetaan peran RBAC dan hak akses modul per stakeholder. |
| 10 | **Data Dictionary v1.1** | `docs/sdlc/02_analysis/05_data_dictionary.md` | Spesifikasi 307 atribut data untuk validasi mapping arsitektur data. |
| 11 | **Access Control Matrix v1.1** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Matriks hak akses RBAC detail per role per fitur. |
| 12 | **Feasibility Study v1.1** | `docs/sdlc/01_planning/02_feasibility_study.md` | Analisis kelayakan teknis dan infrastruktur. |
| 13 | **Innovation Proposal v1.1** | `docs/sdlc/01_planning/05_innovation_proposal.md` | Fitur inovasi yang diusulkan untuk diakomodasi arsitektur. |

### 3.4. Keputusan tentang `narasi.txt`

File `docs/sdlc/narasi.txt` **TIDAK perlu lagi** dijadikan referensi langsung. Seluruh informasi relevan dari narasi sudah terekstraksi dan terdokumentasi secara formal di dalam file referensi di atas (khususnya BRD, SRS, dan Tech Stack Decision). Menggunakan narasi mentah berisiko menimbulkan inkonsistensi dengan dokumen formal yang sudah tervalidasi.

---

## 4. Kerangka Struktur Dokumen System Architecture

Berikut adalah kerangka lengkap dokumen yang harus disusun. Struktur ini mengikuti standar industri **arc42** dan **IEEE 1471/42010** yang diadaptasi untuk konteks proyek UMKM percetakan dengan arsitektur Client-Server LAN lokal:

```
---
dokumen    : System Architecture
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [TANGGAL_PENGERJAAN]
status     : Draft
penyusun   : Senior Solutions Architect & System Design Lead
---

# System Architecture — AbuCom

## Riwayat Perubahan Dokumen
(Tabel riwayat versi)

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan

## 2. Konteks Sistem (System Context)
### 2.1. Diagram Konteks Sistem (Mermaid)
### 2.2. Aktor & Entitas Eksternal
### 2.3. Batasan Sistem (System Boundary)
### 2.4. Antarmuka Eksternal (External Interfaces)

## 3. Arsitektur Infrastruktur Fisik (Physical Architecture)
### 3.1. Topologi Jaringan LAN (Diagram Mermaid)
### 3.2. Spesifikasi Hardware
#### 3.2.1. Node Server Database (Linux Debian 12 Bookworm)
#### 3.2.2. Node Klien Kasir (Windows 11)
#### 3.2.3. Perangkat Jaringan (Switch, Router, Kabel)
#### 3.2.4. Perangkat Pendukung (UPS, Printer Thermal)
### 3.3. Konfigurasi Sistem Operasi
#### 3.3.1. Konfigurasi Server Linux Debian 12
#### 3.3.2. Konfigurasi Klien Windows 11
### 3.4. Strategi Portabilitas Lintas OS (Cross-OS)

## 4. Arsitektur Perangkat Lunak Logis (Logical Architecture)
### 4.1. Pola Arsitektur Keseluruhan (Architectural Pattern)
### 4.2. Diagram Arsitektur Berlapis (Layered Architecture — Mermaid)
### 4.3. Deskripsi Setiap Layer
#### 4.3.1. Presentation Layer (CLI Interface)
#### 4.3.2. Application/Business Logic Layer (Pure Functions FP)
#### 4.3.3. Data Access Layer (Database Connector)
#### 4.3.4. Data/Persistence Layer (MySQL InnoDB)
### 4.4. Pola Desain Fungsional (FP Design Patterns)
#### 4.4.1. Pure Functions & Immutability
#### 4.4.2. State Management tanpa OOP (Closures, State Dict Passing)
#### 4.4.3. Higher-Order Functions & Composition
#### 4.4.4. Error Handling Fungsional (Monad-like Pattern)

## 5. Arsitektur Modular (Module Architecture)
### 5.1. Diagram Dekomposisi Modul (Mermaid)
### 5.2. Deskripsi Modul dan Tanggung Jawab
#### 5.2.1. M.1 — Manajemen Transaksi & Kebijakan Harga
#### 5.2.2. M.2 — Manajemen Inventaris, BOM & Stock Opname
#### 5.2.3. M.3 — Layanan Keuangan Digital, PPOB & Jasa Service
#### 5.2.4. M.4 — Manajemen SDM, Penggajian & Poin Karyawan
#### 5.2.5. M.5 — Sistem Manajemen Antrian & Pelacakan Desain
#### 5.2.6. M.6 — Administrasi Pinjaman, Aset & Pengeluaran
#### 5.2.7. M.7 — Keamanan, Audit Trail & Hak Akses
#### 5.2.8. M.8 — Pembatalan, Retur & CRM
#### 5.2.9. M.9 — Skalabilitas Multi-Cabang
#### 5.2.10. M.10 — Konfigurasi Sistem Runtime
### 5.3. Matriks Dependensi Antar-Modul
### 5.4. Peta Modul ke Tabel Database (Module-to-Table Mapping)

## 6. Arsitektur Data (Data Architecture)
### 6.1. Model Data Fisik (Ringkasan 28 Tabel — 5 Kelompok)
### 6.2. Strategi Koneksi Database (Connection Pooling & Retry)
### 6.3. Strategi Transaksi Database (ACID & InnoDB)
### 6.4. Presisi Data Desimal (Decimal Strategy)
### 6.5. Strategi Multi-Branch Ready (cabang_id)
### 6.6. Strategi Migrasi Data Awal (schema.sql, seed.sql, CSV Import)

## 7. Arsitektur Keamanan (Security Architecture)
### 7.1. Diagram Keamanan Berlapis (Defense in Depth — Mermaid)
### 7.2. Otentikasi (Authentication)
#### 7.2.1. Enkripsi Kata Sandi (bcrypt Cost Factor 12)
#### 7.2.2. Manajemen Session CLI (JWT HS256, 8 Jam)
#### 7.2.3. Rate Limiting Login (5 percobaan, lockout 10 menit)
### 7.3. Otorisasi (Authorization)
#### 7.3.1. Role-Based Access Control (RBAC) — 8 Peran
#### 7.3.2. Matriks Akses Modul per Role
### 7.4. Proteksi Data
#### 7.4.1. Parameterized Queries (Anti SQL Injection)
#### 7.4.2. Sanitasi Input Terminal CLI
#### 7.4.3. Enkripsi Backup Database (AES-256)
#### 7.4.4. Kepatuhan UU PDP No. 27/2022
### 7.5. Audit Trail
#### 7.5.1. Struktur Log Audit JSON
#### 7.5.2. Pemicu Pencatatan Audit (Trigger Events)

## 8. Arsitektur Komunikasi & Alur Data (Communication Architecture)
### 8.1. Diagram Alur Data Antar-Layer (Mermaid)
### 8.2. Protokol Komunikasi Client-Server (TCP/IP Port 3306)
### 8.3. Diagram Sequence untuk Alur Kritis
#### 8.3.1. Alur Login & Pembuatan Session JWT
#### 8.3.2. Alur Transaksi Penjualan End-to-End
#### 8.3.3. Alur HPP BOM Desimal & Pemotongan Stok
#### 8.3.4. Alur Rekonsiliasi Kas & Shift Handover
### 8.4. Pola Penanganan Error & Exception Handling

## 9. Arsitektur Deployment & Operasional (Deployment Architecture)
### 9.1. Diagram Deployment (Mermaid)
### 9.2. Strategi Instalasi & Setup Awal
#### 9.2.1. Setup Server Database (MySQL + Linux Debian 12)
#### 9.2.2. Setup Klien Kasir (Python + Windows 11)
#### 9.2.3. Inisialisasi Database (schema.sql & seed.sql)
#### 9.2.4. Konfigurasi File .env
### 9.3. Strategi Backup & Disaster Recovery
### 9.4. Strategi Pemeliharaan (Maintenance)

## 10. Keputusan Arsitektur (Architecture Decision Records)
### 10.1. ADR-001: Client-Server LAN vs Cloud
### 10.2. ADR-002: Functional Programming vs OOP
### 10.3. ADR-003: CLI vs GUI/Web
### 10.4. ADR-004: MySQL vs Alternatif Database
### 10.5. ADR-005: JWT Stateless vs Server-Side Session

## 11. Kualitas & Atribut Non-Fungsional
### 11.1. Performa (Response Time < 1 detik)
### 11.2. Keandalan (Reliability & ACID)
### 11.3. Keamanan (Security Layers)
### 11.4. Portabilitas (Cross-OS Compatibility)
### 11.5. Skalabilitas (Multi-Branch Ready)
### 11.6. Pemeliharaan (Maintainability & FP Testability)
### 11.7. Kegunaan (Usability — CLI UX)

## 12. Analisis Risiko Arsitektur
### 12.1. Matriks Risiko Teknis
### 12.2. Rencana Mitigasi per Risiko
### 12.3. Kriteria Evaluasi Ulang Arsitektur

## 13. Matriks Ketertelusuran (Traceability Matrix)
### 13.1. Mapping Komponen Arsitektur ke SRS
### 13.2. Mapping Komponen Arsitektur ke Tech Stack Decision

## 14. Persetujuan dan Otorisasi

## 15. Glosarium

## 16. Referensi Dokumen
```

---

## 5. Instruksi Detail Pembuatan Dokumen

### TAHAP 1 — Persiapan & Pembacaan File Referensi

> **Tujuan**: Memahami secara menyeluruh seluruh konteks teknis proyek sebelum menulis satu baris pun.

- [ ] **1.1.** Baca file `docs/sdlc/01_planning/04_tech_stack_decision.md` secara utuh dari awal sampai akhir. Rangkum semua data berikut ke dalam catatan kerja internal:
  - [ ] 1.1.1. Seluruh keputusan teknologi yang berstatus `[MANDATORY]` dan `[REKOMENDASI]`
  - [ ] 1.1.2. 7 prinsip arsitektur panduan (Bagian 2.2)
  - [ ] 1.1.3. Spesifikasi bahasa pemrograman, paradigma FP, versi, dan keterbatasan
  - [ ] 1.1.4. Spesifikasi database MySQL: versi, engine InnoDB, konfigurasi kunci, strategi multi-branch
  - [ ] 1.1.5. Seluruh 6 pustaka (4 wajib + 2 rekomendasi) beserta versi, justifikasi, risiko & mitigasi
  - [ ] 1.1.6. Pustaka standar Python yang dimanfaatkan (decimal, functools, itertools, os, pathlib, dll.)
  - [ ] 1.1.7. Arsitektur Client-Server LAN: topologi, hardware server & klien, UPS, router, switch
  - [ ] 1.1.8. Strategi keamanan: bcrypt, JWT, RBAC, Audit Trail, SQL Injection, Rate Limiting, AES-256
  - [ ] 1.1.9. Strategi CLI: rich, tabulate, UX peningkatan, keterbatasan
  - [ ] 1.1.10. Strategi deployment: requirements.txt, schema.sql, seed.sql, unit testing
  - [ ] 1.1.11. Tim pengembang AI dan pembagian tanggung jawab (6 model AI)
  - [ ] 1.1.12. Matriks ringkasan tech stack (17 komponen)
  - [ ] 1.1.13. Analisis risiko teknis terintegrasi (8 risiko)
  - [ ] 1.1.14. Kompatibilitas tech stack dengan 9 modul fungsional

- [ ] **1.2.** Baca file `docs/sdlc/02_analysis/02_software_requirements.md` secara utuh. Rangkum:
  - [ ] 1.2.1. Deskripsi 10 modul fungsional (M.1 sampai M.10)
  - [ ] 1.2.2. Perspektif produk dan diagram arsitektur tingkat tinggi yang sudah ada
  - [ ] 1.2.3. Karakteristik 8 aktor pengguna beserta hak akses masing-masing
  - [ ] 1.2.4. Lingkungan operasi (runtime environment) dan spesifikasi node server/klien
  - [ ] 1.2.5. Batasan desain dan implementasi (FP murni, CLI, presisi desimal, multi-branch)
  - [ ] 1.2.6. Seluruh kebutuhan non-fungsional (performa, keamanan, reliabilitas, dll.)
  - [ ] 1.2.7. Diagram Mermaid arsitektur yang sudah ada di SRS (jika ada)

- [ ] **1.3.** Baca file `docs/sdlc/03_design/01_database_schema.sql` secara utuh. Rangkum:
  - [ ] 1.3.1. Jumlah total tabel (28) dan pengelompokan (Kelompok A–E)
  - [ ] 1.3.2. Konfigurasi database: CHARACTER SET, COLLATION, ENGINE
  - [ ] 1.3.3. Tabel-tabel kunci per modul (mapping tabel ke modul dari COMMENT pada CREATE TABLE)
  - [ ] 1.3.4. Pola desain: cabang_id di setiap tabel, created_at/updated_at, CHECK constraint
  - [ ] 1.3.5. Seed data yang di-insert (data awal cabang, pengguna, system_configs, saldo, dll.)

- [ ] **1.4.** Baca file `docs/sdlc/03_design/02_erd_database.md` secara utuh. Rangkum:
  - [ ] 1.4.1. Statistik model data: 28 tabel, 307 kolom, 58 FK, 9 unique, 42 CHECK
  - [ ] 1.4.2. 5 kelompok fungsional tabel dan daftar tabel per kelompok
  - [ ] 1.4.3. Pola desain database tingkat lanjut yang didokumentasikan (anti-normalisasi, index komposit, self-referencing FK)

- [ ] **1.5.** Baca file `docs/sdlc/02_analysis/03_use_case_diagram.md`. Rangkum:
  - [ ] 1.5.1. 8 aktor internal dan 4 aktor eksternal
  - [ ] 1.5.2. Daftar 44 use case beserta modul terkait
  - [ ] 1.5.3. Relasi include/extend antar use case

- [ ] **1.6.** Baca file `docs/sdlc/02_analysis/04_workflow_diagram.md`. Rangkum:
  - [ ] 1.6.1. Alur kerja As-Is (6 alur manual) dan pain points
  - [ ] 1.6.2. Alur kerja To-Be (38 alur terotomatisasi) per modul
  - [ ] 1.6.3. Peta keterhubungan workflow antar-modul (input-output)
  - [ ] 1.6.4. 3 alur lintas modul (Cross-Module)

- [ ] **1.7.** Baca file referensi SEKUNDER dan TERSIER lainnya sesuai kebutuhan:
  - [ ] 1.7.1. `docs/sdlc/01_planning/01_project_charter.md` — untuk timeline, milestone, scope
  - [ ] 1.7.2. `docs/sdlc/01_planning/03_stakeholder_register.md` — untuk RBAC per stakeholder
  - [ ] 1.7.3. `docs/sdlc/02_analysis/05_data_dictionary.md` — untuk validasi atribut data
  - [ ] 1.7.4. `docs/sdlc/02_analysis/06_access_control_matrix.md` — untuk detail RBAC
  - [ ] 1.7.5. `docs/sdlc/01_planning/02_feasibility_study.md` — untuk kelayakan infrastruktur
  - [ ] 1.7.6. `docs/sdlc/01_planning/05_innovation_proposal.md` — untuk fitur inovasi

### TAHAP 2 — Penyusunan Bagian Informasi Dokumen (Bab 1)

> **Tujuan**: Menyusun konteks formal dokumen.

- [ ] **2.1.** Tulis frontmatter YAML (dokumen, proyek, versi, tanggal, status, penyusun)
- [ ] **2.2.** Tulis tabel Riwayat Perubahan Dokumen (versi 1.0 awal)
- [ ] **2.3.** Tulis Bagian 1.1 (Tujuan Dokumen): Jelaskan bahwa dokumen ini menyediakan cetak biru arsitektur keseluruhan sistem AbuCom CLI yang menjadi panduan utama implementasi
- [ ] **2.4.** Tulis Bagian 1.2 (Cakupan Dokumen): Daftarkan semua aspek yang dicakup (infrastruktur fisik, arsitektur logis, keamanan, deployment, dll.)
- [ ] **2.5.** Tulis Bagian 1.3 (Posisi Dokumen dalam SDLC): Jelaskan posisi sebagai deliverable ke-3 Fase 03 Design, setelah database_schema.sql dan erd_database.md
- [ ] **2.6.** Tulis Bagian 1.4 (Hubungan dengan Dokumen Lainnya): Identifikasi input (Tech Stack, SRS, ERD, Schema) dan output (menjadi acuan SDD detail, Test Plan, Implementation Guide)
- [ ] **2.7.** Tulis Bagian 1.5 (Audiens Target): Junior Programmer, Tim AI, Staf Toko
- [ ] **2.8.** Tulis Bagian 1.6 (Definisi, Akronim, Singkatan): Kompilasi dari semua dokumen referensi, tambahkan istilah arsitektural spesifik

### TAHAP 3 — Penyusunan Konteks Sistem (Bab 2)

> **Tujuan**: Menggambarkan sistem dari perspektif luar (black-box view).

- [ ] **3.1.** Buat Diagram Konteks Sistem menggunakan Mermaid yang menunjukkan:
  - AbuCom CLI sebagai sistem pusat
  - 8 aktor internal (berdasarkan data UCD)
  - 4 aktor eksternal (berdasarkan data UCD)
  - Entitas infrastruktur: MySQL Server, File System, Printer Thermal
  - Aliran data masuk/keluar utama
- [ ] **3.2.** Tulis deskripsi setiap aktor dan entitas eksternal (ambil dari UCD Bagian 2)
- [ ] **3.3.** Tulis batasan sistem (System Boundary) — apa yang di dalam dan di luar sistem (ambil dari UCD Bagian 3.1 dan SRS Bagian 2.5)
- [ ] **3.4.** Tulis deskripsi antarmuka eksternal (terminal CLI, koneksi MySQL, file system, printer)

### TAHAP 4 — Penyusunan Arsitektur Infrastruktur Fisik (Bab 3)

> **Tujuan**: Mendokumentasikan arsitektur hardware dan jaringan toko fisik.

- [ ] **4.1.** Buat Diagram Topologi Jaringan LAN menggunakan Mermaid (ambil data dari Tech Stack Bagian 6.2):
  - Mini PC Server (Debian 12) ↔ Switch Hub Gigabit ↔ PC Kasir (Windows 11)
  - Kabel UTP Cat6, Router MikroTik, 2x UPS
- [ ] **4.2.** Tulis spesifikasi hardware server database (Core i5 Gen 12+, 16GB RAM, SSD 512GB NVMe)
- [ ] **4.3.** Tulis spesifikasi hardware klien kasir (Core i3, 8GB RAM, SSD 256GB NVMe)
- [ ] **4.4.** Tulis spesifikasi perangkat jaringan (Switch Hub Gigabit 8-Port, Router MikroTik, UTP Cat6)
- [ ] **4.5.** Tulis spesifikasi perangkat pendukung (2x UPS 600VA+, Printer Thermal 58mm/80mm)
- [ ] **4.6.** Tulis konfigurasi OS server (MySQL service, IP statis, chmod 700 backup, firewall port 3306)
- [ ] **4.7.** Tulis konfigurasi OS klien (Python 3.14.2+, Windows Terminal, encoding UTF-8)
- [ ] **4.8.** Tulis strategi portabilitas lintas OS (pathlib, encoding utf-8, platform.system(), cls/clear)

### TAHAP 5 — Penyusunan Arsitektur Perangkat Lunak Logis (Bab 4)

> **Tujuan**: Mendokumentasikan arsitektur software dalam bentuk layered architecture.

- [ ] **5.1.** Tentukan dan jelaskan pola arsitektur: **Layered Architecture (4-Layer)** dengan paradigma Functional Programming murni
- [ ] **5.2.** Buat Diagram Arsitektur Berlapis menggunakan Mermaid:
  - Layer 1 (Atas): Presentation Layer — CLI Interface (rich, tabulate, input/output terminal)
  - Layer 2: Application/Business Logic Layer — Pure Functions FP (logika bisnis, kalkulasi HPP/BOM, payroll, poin)
  - Layer 3: Data Access Layer — Database Connector (mysql-connector-python, connection pooling, parameterized queries)
  - Layer 4 (Bawah): Data/Persistence Layer — MySQL InnoDB (28 tabel, ACID, cabang_id)
  - Cross-cutting: Security (bcrypt, JWT, RBAC), Configuration (.env, system_configs), Logging (Audit Trail)
- [ ] **5.3.** Tulis deskripsi detail setiap layer:
  - [ ] 5.3.1. Presentation Layer: Komponen CLI, navigasi menu, validator input, rich panels, tabulate tables
  - [ ] 5.3.2. Business Logic Layer: Pure functions, state dictionary passing, nested closures, decimal precision, functools/itertools
  - [ ] 5.3.3. Data Access Layer: Connection factory, transaction wrapper (START/COMMIT/ROLLBACK), retry mechanism, connection pooling
  - [ ] 5.3.4. Persistence Layer: MySQL 8.x InnoDB, DECIMAL(15,4), utf8mb4, REPEATABLE READ isolation
- [ ] **5.4.** Tulis pola desain FP yang diterapkan:
  - [ ] 5.4.1. Pure Functions & Immutability (tuples, namedtuples, frozen dataclasses)
  - [ ] 5.4.2. State Management tanpa OOP (Nested Closures, State Dict Passing)
  - [ ] 5.4.3. Higher-Order Functions & Composition (functools.partial, reduce, map, filter)
  - [ ] 5.4.4. Error Handling Fungsional (Result/Either monad-like pattern)

### TAHAP 6 — Penyusunan Arsitektur Modular (Bab 5)

> **Tujuan**: Memetakan dekomposisi 10 modul fungsional dan dependensinya.

- [ ] **6.1.** Buat Diagram Dekomposisi Modul menggunakan Mermaid (10 modul + cross-cutting concerns)
- [ ] **6.2.** Tulis deskripsi setiap modul (M.1 s.d M.10):
  - Untuk setiap modul, dokumentasikan: Nama, Tanggung Jawab, Use Case terkait (dari UCD), Tabel database terkait (dari Schema), Layer yang terlibat, Dependensi ke modul lain
- [ ] **6.3.** Buat Matriks Dependensi Antar-Modul (tabel/diagram yang menunjukkan modul mana bergantung ke modul mana — ambil data dari Workflow Diagram Bagian 2.2 peta keterhubungan)
- [ ] **6.4.** Buat Peta Modul ke Tabel Database (mapping M.1→tabel apa saja, M.2→tabel apa saja, dst. — ambil dari COMMENT pada schema.sql)

### TAHAP 7 — Penyusunan Arsitektur Data (Bab 6)

> **Tujuan**: Mendokumentasikan strategi pengelolaan data.

- [ ] **7.1.** Tulis ringkasan model data fisik (28 tabel, 5 kelompok, referensi ke ERD)
- [ ] **7.2.** Tulis strategi koneksi database:
  - Connection pooling bawaan mysql-connector-python
  - Retry mechanism dengan exponential backoff
  - Timeout dan error handling koneksi
- [ ] **7.3.** Tulis strategi transaksi database:
  - Blok START TRANSACTION / COMMIT / ROLLBACK
  - Isolation Level REPEATABLE READ
  - Atomicity untuk operasi gabungan (stok + kas + audit)
- [ ] **7.4.** Tulis strategi presisi desimal:
  - Python: modul `decimal` wajib untuk semua kalkulasi keuangan dan stok
  - MySQL: DECIMAL(15,4) untuk semua kolom numerik keuangan
  - Larangan penggunaan tipe float
- [ ] **7.5.** Tulis strategi multi-branch ready:
  - Kolom cabang_id (INT FK) di setiap 28 tabel
  - Default cabang_id = 1 untuk fase satu cabang
  - Rancangan ekspansi masa depan
- [ ] **7.6.** Tulis strategi migrasi data awal:
  - schema.sql untuk inisialisasi struktur
  - seed.sql untuk data master awal
  - CSV import semiautomatis untuk data Excel lama

### TAHAP 8 — Penyusunan Arsitektur Keamanan (Bab 7)

> **Tujuan**: Mendokumentasikan seluruh lapisan keamanan sistem.

- [ ] **8.1.** Buat Diagram Keamanan Berlapis (Defense in Depth) menggunakan Mermaid
- [ ] **8.2.** Tulis detail otentikasi:
  - [ ] 8.2.1. bcrypt: Cost Factor 12, alur hash & verify, salt unik per user
  - [ ] 8.2.2. JWT: HS256, secret key dari .env, payload (user_id, role, cabang_id, exp), masa berlaku 8 jam
  - [ ] 8.2.3. Rate Limiting: 5 percobaan gagal, lockout 10 menit, failed_login_attempts di tabel pengguna
- [ ] **8.3.** Tulis detail otorisasi:
  - [ ] 8.3.1. RBAC: 8 peran (pemilik, kepala_percetakan, pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang)
  - [ ] 8.3.2. Matriks akses modul per role (ambil dari Access Control Matrix)
- [ ] **8.4.** Tulis proteksi data:
  - [ ] 8.4.1. Parameterized Queries (%s) — larangan f-string di query SQL
  - [ ] 8.4.2. Sanitasi input CLI: filter escape character, batas panjang, validasi regex
  - [ ] 8.4.3. Enkripsi backup AES-256, chmod 700 folder backup
  - [ ] 8.4.4. Kepatuhan UU PDP: enkripsi data CRM pelanggan, pembatasan akses data finansial
- [ ] **8.5.** Tulis mekanisme Audit Trail:
  - [ ] 8.5.1. Struktur tabel audit_logs (id, user_id, action_timestamp, action_type, target_table, old_value JSON, new_value JSON)
  - [ ] 8.5.2. Event pemicu: INSERT/UPDATE/DELETE pada tabel sensitif, login gagal, retur/batal

### TAHAP 9 — Penyusunan Arsitektur Komunikasi & Alur Data (Bab 8)

> **Tujuan**: Mendokumentasikan bagaimana data mengalir di dalam sistem.

- [ ] **9.1.** Buat Diagram Alur Data Antar-Layer menggunakan Mermaid (dari CLI input → business logic → data access → MySQL → response)
- [ ] **9.2.** Tulis protokol komunikasi Client-Server:
  - TCP/IP Port 3306 (default MySQL)
  - Kabel LAN UTP Cat6, latensi <1ms
  - IP statis server via Router MikroTik
- [ ] **9.3.** Buat minimal 4 Diagram Sequence menggunakan Mermaid:
  - [ ] 9.3.1. Alur Login & Pembuatan Session JWT (User → CLI → bcrypt verify → JWT generate → Dashboard)
  - [ ] 9.3.2. Alur Transaksi Penjualan End-to-End (Input → Harga Dinamis → Stok → Kas → Poin → Struk)
  - [ ] 9.3.3. Alur HPP BOM Desimal & Pemotongan Stok (Trigger Selesai → BOM Fetch → Decimal Calc → Stock Deduct)
  - [ ] 9.3.4. Alur Rekonsiliasi Kas & Shift Handover (Kas Fisik Input → Sistem Compare → Selisih → Audit)
- [ ] **9.4.** Tulis pola penanganan error:
  - Error code standar (ERR-DB-xxx, ERR-VAL-xxx, ERR-AUTH-xxx, ERR-STOCK-xxx, dll.)
  - Strategi retry, rollback, dan user notification

### TAHAP 10 — Penyusunan Arsitektur Deployment & Operasional (Bab 9)

> **Tujuan**: Mendokumentasikan cara deploy dan maintain sistem.

- [ ] **10.1.** Buat Diagram Deployment menggunakan Mermaid (Node Server + Node Klien + perangkat pendukung)
- [ ] **10.2.** Tulis prosedur setup server database:
  - Instalasi MySQL 8.x LTS di Debian 12
  - Konfigurasi user root, charset, collation, InnoDB
  - Eksekusi schema.sql dan seed.sql
- [ ] **10.3.** Tulis prosedur setup klien kasir:
  - Instalasi Python 3.14.2+ di Windows 11
  - pip install -r requirements.txt
  - Konfigurasi .env (DB_HOST, DB_PORT, DB_USER, DB_PASS, JWT_SECRET)
- [ ] **10.4.** Tulis strategi backup & disaster recovery:
  - Backup harian via mysqldump, kompresi zip AES-256
  - Prosedur restore dari backup terenkripsi
  - Perlindungan UPS untuk graceful shutdown
- [ ] **10.5.** Tulis strategi pemeliharaan:
  - Monitoring performa MySQL lokal
  - Rotasi log audit trail
  - Pembaruan pustaka Python (requirements.txt)

### TAHAP 11 — Penyusunan Keputusan Arsitektur / ADR (Bab 10)

> **Tujuan**: Mendokumentasikan alasan di balik keputusan arsitektur kunci.

- [ ] **11.1.** Tulis ADR-001: Client-Server LAN vs Cloud (ambil dari Tech Stack Bagian 6.3)
- [ ] **11.2.** Tulis ADR-002: Functional Programming vs OOP (ambil dari Tech Stack Bagian 3.2)
- [ ] **11.3.** Tulis ADR-003: CLI vs GUI/Web (ambil dari Tech Stack Bagian 7.2)
- [ ] **11.4.** Tulis ADR-004: MySQL vs PostgreSQL/SQLite/MariaDB (ambil dari Tech Stack Bagian 4.2)
- [ ] **11.5.** Tulis ADR-005: JWT Stateless vs Server-Side Session (ambil dari Tech Stack Bagian 5.4)
- [ ] **11.6.** Untuk setiap ADR, gunakan format: Konteks → Keputusan → Status → Konsekuensi → Alternatif Ditolak

### TAHAP 12 — Penyusunan Kualitas & Atribut Non-Fungsional (Bab 11)

> **Tujuan**: Memetakan bagaimana arsitektur memenuhi kebutuhan non-fungsional.

- [ ] **12.1.** Tulis target performa: response time <1 detik untuk semua operasi CLI, laporan keuangan <5 detik
- [ ] **12.2.** Tulis strategi keandalan: ACID InnoDB, UPS, retry connection, rollback otomatis
- [ ] **12.3.** Tulis ringkasan keamanan (referensi ke Bab 7)
- [ ] **12.4.** Tulis strategi portabilitas: pathlib, utf-8, platform detection, Windows Terminal
- [ ] **12.5.** Tulis strategi skalabilitas: cabang_id, index komposit, partitioning-ready
- [ ] **12.6.** Tulis strategi pemeliharaan: FP pure functions = mudah di-unit-test, code coverage 90%
- [ ] **12.7.** Tulis strategi kegunaan CLI: rich panels, tabulate tables, consistent navigation, hotkeys

### TAHAP 13 — Penyusunan Analisis Risiko Arsitektur (Bab 12)

> **Tujuan**: Mengidentifikasi dan memitigasi risiko arsitektural.

- [ ] **13.1.** Kompilasi risiko teknis dari Tech Stack Decision (8 risiko) dan tambahkan risiko arsitektural baru yang relevan
- [ ] **13.2.** Buat matriks risiko dengan kolom: ID, Komponen, Risiko, Probabilitas (1-5), Dampak (1-5), Skor, Rencana Mitigasi
- [ ] **13.3.** Tulis kriteria evaluasi ulang arsitektur (trigger re-evaluation) — ambil dari Tech Stack Bagian 13

### TAHAP 14 — Penyusunan Traceability, Persetujuan, Glosarium & Referensi (Bab 13–16)

> **Tujuan**: Melengkapi dokumen dengan mapping dan penutup formal.

- [ ] **14.1.** Buat matriks traceability: Komponen Arsitektur ↔ ID SRS (SRS-F-xxx, SRS-NF-xxx)
- [ ] **14.2.** Buat matriks traceability: Komponen Arsitektur ↔ Keputusan Tech Stack
- [ ] **14.3.** Tulis tabel persetujuan dan otorisasi (Pemilik Usaha sebagai penandatangan)
- [ ] **14.4.** Kompilasi glosarium dari semua dokumen referensi, tambahkan istilah arsitektural baru (Layer, Pattern, Deployment Node, ADR, dll.)
- [ ] **14.5.** Tulis daftar referensi file yang digunakan dalam format tabel: No, Nama Dokumen, Lokasi Path Relatif, Keterangan Penggunaan

### TAHAP 15 — Penulisan ke Target File

> **Tujuan**: Menuangkan seluruh hasil ke file target.

- [ ] **15.1.** Tulis seluruh konten dokumen System Architecture ke file target: `docs/sdlc/03_design/03_system_architecture.md`
- [ ] **15.2.** Pastikan semua diagram Mermaid dapat di-render dengan benar (gunakan sintaks ```` ```mermaid ````)
- [ ] **15.3.** Pastikan semua tabel markdown terformat rapi dan terbaca
- [ ] **15.4.** Pastikan penomoran bab dan sub-bab konsisten dan berurutan
- [ ] **15.5.** Pastikan tidak ada placeholder teks seperti `[TODO]`, `[TBD]`, atau `...` kecuali untuk data yang memang tidak tersedia di referensi (lihat instruksi penandaan data kosong di bawah)

### TAHAP 16 — Verifikasi & Validasi Akhir

> **Tujuan**: Memastikan kualitas dan kelengkapan dokumen.

- [ ] **16.1.** Verifikasi bahwa semua 7 prinsip arsitektur panduan dari Tech Stack tercermin dalam desain
- [ ] **16.2.** Verifikasi bahwa semua 10 modul fungsional terdokumentasi dalam arsitektur modular
- [ ] **16.3.** Verifikasi bahwa semua 28 tabel database ter-mapping ke modul yang tepat
- [ ] **16.4.** Verifikasi bahwa semua 6 pustaka wajib terdokumentasi dalam layer arsitektur yang sesuai
- [ ] **16.5.** Verifikasi bahwa semua keputusan keamanan (bcrypt, JWT, RBAC, AES-256, SQL injection protection) terdokumentasi
- [ ] **16.6.** Verifikasi bahwa semua diagram Mermaid memiliki konten yang akurat dan konsisten dengan teks deskriptif
- [ ] **16.7.** Verifikasi bahwa dokumen dapat dijadikan referensi fase SDLC selanjutnya (implementation) tanpa ambiguitas
- [ ] **16.8.** Verifikasi bahwa bahasa yang digunakan adalah Bahasa Indonesia yang natural, jelas, dan mudah dipahami
- [ ] **16.9.** Verifikasi bahwa referensi file tercantum di bagian akhir dokumen (Bab 16)

---

## 6. Instruksi Tambahan Spesifik Dokumen System Architecture

### 6.1. Penanganan Data Kosong

Jika ada data atau informasi yang dibutuhkan oleh kerangka dokumen namun **tidak tersedia** di dalam file referensi yang terdaftar, maka:
- **Tandai** bagian tersebut dengan format: `> ⚠️ **[DATA KOSONG]**: [Deskripsi data yang dibutuhkan]. Perlu diisi secara manual oleh Pemilik Proyek.`
- **Jangan mengarang atau mengasumsikan** data yang tidak ada.
- Contoh: Jika alamat IP statis server belum ditentukan, tulis: `> ⚠️ **[DATA KOSONG]**: Alamat IP statis Mini PC Server belum ditentukan. Perlu dikonfigurasi saat instalasi fisik oleh Pemilik Proyek.`

### 6.2. Kualitas Diagram Mermaid

- Setiap bab utama **wajib** memiliki minimal 1 diagram Mermaid yang relevan.
- Total minimum diagram: **10 diagram Mermaid** (Konteks, Topologi, Layered Architecture, Modul Dekomposisi, Dependensi Modul, Security Layers, Alur Data, 4x Sequence Diagram, Deployment).
- Gunakan styling warna yang konsisten dan sesuai dengan konvensi warna di Workflow Diagram v1.1.

### 6.3. Konsistensi Terminologi

- Gunakan istilah teknis yang **konsisten** dengan dokumen SDLC sebelumnya.
- Jangan mengganti nama modul (gunakan M.1 s.d M.10 sesuai SRS).
- Jangan mengganti nama tabel database (gunakan nama persis dari schema.sql).
- Jangan mengganti nama role pengguna (gunakan: pemilik, kepala_percetakan, pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang).

### 6.4. Keunikan Dokumen System Architecture

Dokumen ini harus memiliki **nilai tambah** yang tidak ada di dokumen lain:
- **Pandangan holistik**: Menghubungkan keputusan teknologi (Tech Stack) dengan implementasi konkret (Schema) melalui blueprint arsitektur.
- **Diagram sequence**: Menunjukkan aliran data real-time yang belum ada di Workflow Diagram (yang hanya menunjukkan alur bisnis, bukan alur teknis antar-layer).
- **Architecture Decision Records (ADR)**: Mendokumentasikan rasional keputusan arsitektur dalam format standar industri yang lebih terstruktur dari Tech Stack Decision.
- **Cross-cutting concerns**: Menjelaskan bagaimana aspek seperti keamanan, logging, dan konfigurasi memotong semua layer arsitektur.

### 6.5. Standar Bahasa

- Gunakan **Bahasa Indonesia** yang formal namun natural.
- Hindari kalimat yang terlalu panjang (maksimal 2 klausa per kalimat).
- Untuk istilah teknis yang tidak memiliki padanan Bahasa Indonesia yang umum, gunakan istilah asli dalam bahasa Inggris dengan penjelasan singkat dalam kurung pada kemunculan pertama.
- Contoh: "Sistem menggunakan pola *Layered Architecture* (arsitektur berlapis) untuk memisahkan tanggung jawab antar-komponen."

---

## 7. Kriteria Penerimaan (Acceptance Criteria)

Issue ini dianggap selesai jika:

- [ ] File `docs/sdlc/03_design/03_system_architecture.md` sudah terisi lengkap sesuai kerangka di Bagian 4
- [ ] Semua 16 bab utama tersusun dengan konten substantif (bukan placeholder)
- [ ] Minimal 10 diagram Mermaid tersedia dan akurat
- [ ] Minimal 4 Sequence Diagram untuk alur kritis tersedia
- [ ] 5 Architecture Decision Records (ADR) terdokumentasi
- [ ] Matriks traceability ke SRS dan Tech Stack Decision tersedia
- [ ] Semua data dari file referensi terangkum tanpa ada yang terlewat
- [ ] Data yang tidak tersedia ditandai dengan format `[DATA KOSONG]`
- [ ] Referensi file tercantum di bagian akhir dokumen
- [ ] Dokumen menggunakan Bahasa Indonesia yang natural dan tidak ambigu
- [ ] Dokumen layak dijadikan acuan utama untuk fase implementasi (coding)

---

## 8. Referensi File yang Digunakan dalam Penyusunan Issue Ini

| No | Nama Dokumen | Lokasi Path Relatif | Keterangan |
|----|-------------|---------------------|------------|
| 1 | Tech Stack Decision v1.1 | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Sumber utama keputusan teknologi dan arsitektur |
| 2 | Software Requirements Specification (SRS) v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | Spesifikasi 10 modul dan kebutuhan non-fungsional |
| 3 | Database Schema (DDL SQL) v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | Skema fisik 28 tabel MySQL |
| 4 | ERD Database v1.1 | `docs/sdlc/03_design/02_erd_database.md` | Visualisasi relasi data 58 FK |
| 5 | Use Case Diagram (UCD) v1.1 | `docs/sdlc/02_analysis/03_use_case_diagram.md` | Pemetaan 44 use case dan 12 aktor |
| 6 | Workflow Diagram v1.1 | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Alur kerja operasional per modul |
| 7 | Project Charter v1.1 | `docs/sdlc/01_planning/01_project_charter.md` | Scope, timeline, dan tim proyek |
| 8 | Stakeholder Register v1.1 | `docs/sdlc/01_planning/03_stakeholder_register.md` | Pemetaan peran dan hak akses |
| 9 | Business Requirements Document (BRD) v1.1 | `docs/sdlc/02_analysis/01_business_requirements.md` | Kebutuhan bisnis tingkat tinggi |
| 10 | Data Dictionary v1.1 | `docs/sdlc/02_analysis/05_data_dictionary.md` | Spesifikasi 307 atribut data |
| 11 | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Matriks RBAC detail |
| 12 | Feasibility Study v1.1 | `docs/sdlc/01_planning/02_feasibility_study.md` | Kelayakan teknis dan infrastruktur |
| 13 | Innovation Proposal v1.1 | `docs/sdlc/01_planning/05_innovation_proposal.md` | Fitur inovasi yang diusulkan |
| 14 | Narasi Awal Proyek | `docs/sdlc/narasi.txt` | Tidak digunakan (sudah terabstraksi ke dokumen formal) |
