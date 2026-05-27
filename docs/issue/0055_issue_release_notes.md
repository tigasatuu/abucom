# Pembuatan dan Penyusunan Dokumen Release Notes

---

## Metadata Issue

| Atribut            | Nilai                                                        |
|--------------------|--------------------------------------------------------------|
| **Judul**          | Pembuatan dan Penyusunan Dokumen Release Notes v1.0          |
| **Dokumen Utama**  | Release Notes                                                |
| **Target File**    | `docs/sdlc/06_deployment/03_release_notes.md`                |
| **Fase SDLC**      | Fase 06 — Deployment (Deliverable ke-3)                      |
| **Prioritas**      | High                                                         |
| **Status**         | Open                                                         |
| **Tanggal Dibuat** | 2026-05-27                                                   |
| **Estimasi Waktu** | 3 - 4 Jam                                                    |

---

## 1. Persona Pelaksana

| Atribut                   | Nilai                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------|
| **Persona Utama**         | **Senior Release Manager & Technical Documentation Engineer**                             |
| **Justifikasi Pemilihan** | Release Notes adalah dokumen resmi yang mencatat seluruh perubahan, fitur baru, perbaikan, batasan, dan informasi rilis produk perangkat lunak. Persona ini memiliki otoritas dan keahlian untuk: (1) merangkum seluruh deliverable dari setiap fase SDLC menjadi ringkasan rilis yang kohesif; (2) mengidentifikasi fitur, perbaikan, dan batasan teknis yang diketahui (*known issues*); (3) menyusun catatan migrasi dan upgrade path; (4) memastikan dokumen dapat dipahami oleh audiens teknis maupun non-teknis. |
| **Reviewer**              | Antigravity (Senior DevOps Lead)                                                          |
| **Approved By**           | Alfatih (Pemilik Usaha AbuCom)                                                            |

---

## 2. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca dan dirangkum** oleh pelaksana sebelum memulai penyusunan dokumen Release Notes. File-file ini dipilih karena mengandung data dan informasi yang secara spesifik dibutuhkan oleh dokumen Release Notes.

### 2.1. Referensi Prioritas PRIMER

File-file berikut adalah **sumber data utama** yang wajib dibaca secara menyeluruh tanpa terlewat satu detail pun:

| No | Kode Ref | Nama Dokumen                       | Path Relatif                                                   | Justifikasi Pemilihan                                                                                                                                       |
|:--:|:--------:|:-----------------------------------|:---------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | **R-01** | Project Charter v1.1               | `docs/sdlc/01_planning/01_project_charter.md`                  | Sumber informasi nama proyek, deskripsi singkat, tujuan, ruang lingkup, deliverables per fase, tim pengembang, milestone, estimasi anggaran, dan versi produk. |
| 2  | **R-02** | Software Requirements Spec v1.1    | `docs/sdlc/02_analysis/02_software_requirements.md`            | Sumber daftar lengkap fitur fungsional (SRS-F-001 s.d SRS-F-040), modul (M.1-M.10), kebutuhan non-fungsional, dan spesifikasi teknis lingkungan runtime.     |
| 3  | **R-03** | Deployment Guide v1.1              | `docs/sdlc/06_deployment/01_deployment_guide.md`               | Sumber informasi arsitektur deployment, pre-deployment checklist, prosedur go-live, smoke test, rollback, matriks risiko, dan SOP runbook harian.              |
| 4  | **R-04** | Environment Config v1.1            | `docs/sdlc/06_deployment/02_environment_config.yaml`           | Sumber parameter konfigurasi lengkap (database, keamanan, jaringan, printer, backup, error codes, lingkungan dev/staging/prod).                                |
| 5  | **R-05** | Test Plan v1.1                     | `docs/sdlc/05_testing/01_test_plan.md`                         | Sumber strategi pengujian, exit criteria (100% pass, coverage ≥ 90%, 0 major bug), dan skenario UAT sign-off yang menentukan kesiapan rilis.                  |

### 2.2. Referensi Prioritas SEKUNDER

File-file berikut menyediakan **data pendukung teknis** yang diperlukan untuk melengkapi detail fitur dan arsitektur di dalam Release Notes:

| No | Kode Ref | Nama Dokumen                       | Path Relatif                                                   | Justifikasi Pemilihan                                                                                                                |
|:--:|:--------:|:-----------------------------------|:---------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| 6  | **R-06** | System Architecture v1.1           | `docs/sdlc/03_design/03_system_architecture.md`                | Sumber diagram arsitektur sistem, topologi LAN, connection pooling, dan desain multi-branch ready.                                    |
| 7  | **R-07** | Security Design v1.1               | `docs/sdlc/03_design/06_security_design.md`                    | Sumber fitur keamanan (bcrypt, JWT, RBAC, Fernet CRM, AES-256, audit trail, UU PDP) yang wajib dicantumkan di Release Notes.          |
| 8  | **R-08** | Tech Stack Decision v1.1           | `docs/sdlc/01_planning/04_tech_stack_decision.md`              | Sumber keputusan stack teknologi (Python 3.14.2+, MySQL 8.4 LTS, FP paradigm, locked library versions).                              |
| 9  | **R-09** | Database Schema v1.1               | `docs/sdlc/03_design/01_database_schema.sql`                   | Sumber jumlah tabel relasional (28 tabel InnoDB), relasi Foreign Key, dan engine database yang digunakan.                             |
| 10 | **R-10** | Module Structure v1.1              | `docs/sdlc/04_implementation/03_module_structure.md`           | Sumber struktur direktori proyek, pemetaan modul-to-file, dan daftar entry point aplikasi.                                            |
| 11 | **R-11** | Git Workflow v1.1                  | `docs/sdlc/04_implementation/04_git_workflow.md`               | Sumber konvensi tagging rilis (SemVer), branching strategy, dan prosedur release tagging formal.                                      |

### 2.3. Referensi Prioritas TERSIER

| No | Kode Ref | Nama Dokumen                       | Path Relatif                                                   | Justifikasi Pemilihan                                                                                                |
|:--:|:--------:|:-----------------------------------|:---------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| 12 | **R-12** | Test Cases v1.1                    | `docs/sdlc/05_testing/02_test_cases.md`                        | Sumber jumlah kasus uji dan hasil pengujian yang memperkuat pernyataan kualitas rilis.                                |
| 13 | **R-13** | UAT Script v1.1                    | `docs/sdlc/05_testing/03_uat_script.md`                        | Sumber skenario penerimaan pengguna yang digunakan untuk memvalidasi kelayakan rilis.                                 |
| 14 | **R-14** | Bug Report Template v1.1           | `docs/sdlc/05_testing/04_bug_report_template.md`               | Sumber format pelaporan bug dan known issues yang perlu dicantumkan di Release Notes.                                 |
| 15 | **R-15** | Access Control Matrix v1.1         | `docs/sdlc/02_analysis/06_access_control_matrix.md`            | Sumber 8 peran RBAC, hak akses per modul, dan batasan otorisasi yang relevan dengan fitur keamanan rilis.             |
| 16 | **R-16** | Coding Standard v1.1               | `docs/sdlc/04_implementation/01_coding_standard.md`            | Sumber paradigma FP, konvensi kode, dan quality gate yang menjadi standar pengembangan rilis ini.                     |

> **Catatan**: File `docs/sdlc/narasi.txt` **TIDAK dipilih** sebagai referensi karena seluruh informasi bisnis yang relevan sudah terabsorpsi secara lengkap ke dalam dokumen-dokumen SDLC formal di atas (khususnya R-01 Project Charter dan R-02 SRS). Menggunakan narasi mentah untuk Release Notes berpotensi menghasilkan informasi yang tidak terstruktur dan redundan.

---

## 3. Kerangka Struktur Dokumen Release Notes

Berikut adalah kerangka standar dokumen Release Notes yang harus diikuti pelaksana. Struktur ini mengacu pada praktik industri **IEEE 1063** (Software User Documentation) dan format Release Notes standar produk perangkat lunak enterprise.

```
---
dokumen    : Release Notes
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [TANGGAL PENYUSUNAN]
status     : [STATUS DOKUMEN]
penyusun   : Senior Release Manager & Technical Documentation Engineer
reviewer   : Antigravity (Senior DevOps Lead)
approved_by: Alfatih (Pemilik Usaha AbuCom)
---

# Release Notes — AbuCom v[NOMOR VERSI RILIS]

## Riwayat Perubahan Dokumen
(Tabel versi, tanggal, perubahan, oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya (Input & Output)
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan

---

## 2. Ringkasan Rilis (Release Summary)
### 2.1. Nama Produk dan Nomor Versi Rilis
### 2.2. Tanggal Rilis
### 2.3. Tipe Rilis (Major / Minor / Patch)
### 2.4. Deskripsi Umum Rilis
### 2.5. Highlight Fitur Utama Rilis (Bullet Points)

---

## 3. Persyaratan Sistem (System Requirements)
### 3.1. Persyaratan Hardware Minimum
#### 3.1.1. Server Database
#### 3.1.2. Klien Kasir
#### 3.1.3. Perangkat Jaringan
#### 3.1.4. Perangkat Pendukung (UPS, Printer Thermal)
### 3.2. Persyaratan Software
#### 3.2.1. Sistem Operasi yang Didukung
#### 3.2.2. Runtime dan Database Engine
#### 3.2.3. Pustaka Dependensi (requirements.txt)
### 3.3. Persyaratan Jaringan

---

## 4. Fitur Baru (New Features)
### 4.1. Modul M.1 — Manajemen Transaksi & Kebijakan Harga
### 4.2. Modul M.2 — Manajemen Inventaris, BOM & Stock Opname
### 4.3. Modul M.3 — Layanan Keuangan Digital, PPOB & Jasa Service
### 4.4. Modul M.4 — Manajemen SDM, Penggajian & Poin Karyawan
### 4.5. Modul M.5 — Sistem Manajemen Antrian & Pelacakan Desain
### 4.6. Modul M.6 — Administrasi Pinjaman, Aset & Pengeluaran
### 4.7. Modul M.7 — Keamanan, Audit Trail & Hak Akses
### 4.8. Modul M.8 — Pembatalan, Retur & CRM
### 4.9. Modul M.9 — Skalabilitas Multi-Cabang
### 4.10. Modul M.10 — Konfigurasi Sistem Runtime

---

## 5. Fitur Keamanan Rilis (Security Features)
### 5.1. Otentikasi (bcrypt & JWT)
### 5.2. Otorisasi (RBAC 8 Peran)
### 5.3. Proteksi Data Pribadi (Fernet CRM & UU PDP)
### 5.4. Hardening Infrastruktur (Firewall, SSH, Backup AES-256)
### 5.5. Audit Trail & Fraud Detection

---

## 6. Perbaikan Bug dan Peningkatan (Bug Fixes & Improvements)
### 6.1. Daftar Bug yang Diperbaiki
### 6.2. Peningkatan Performa
### 6.3. Peningkatan Antarmuka CLI

---

## 7. Batasan yang Diketahui (Known Limitations)
### 7.1. Batasan Fungsional
### 7.2. Batasan Teknis
### 7.3. Batasan Integrasi Pihak Ketiga
### 7.4. Fitur di Luar Cakupan (Out-of-Scope)

---

## 8. Masalah yang Diketahui (Known Issues)
(Tabel: ID, Deskripsi, Dampak, Workaround, Status)

---

## 9. Panduan Instalasi dan Upgrade
### 9.1. Instalasi Baru (Fresh Install)
### 9.2. Upgrade dari Versi Sebelumnya (jika ada)
### 9.3. Prosedur Rollback
### 9.4. Referensi Deployment Guide

---

## 10. Konfigurasi Default Rilis
### 10.1. Parameter Lingkungan Produksi
### 10.2. Parameter Keamanan Default
### 10.3. Parameter Operasional Harian
### 10.4. Referensi Environment Config

---

## 11. Hasil Pengujian dan Kualitas Rilis (Quality Assurance Summary)
### 11.1. Ringkasan Hasil Unit Testing
### 11.2. Ringkasan Hasil Integration Testing
### 11.3. Ringkasan Hasil UAT (User Acceptance Testing)
### 11.4. Kriteria Exit Testing yang Terpenuhi
### 11.5. Matriks Ketertelusuran Pengujian (Traceability)

---

## 12. Arsitektur dan Topologi Deployment
### 12.1. Diagram Arsitektur Deployment (Mermaid)
### 12.2. Matriks Komponen per Node
### 12.3. Topologi Jaringan LAN Offline

---

## 13. Matriks Risiko Rilis
(Tabel: ID, Risiko, Probabilitas, Dampak, Mitigasi, Kontingensi)

---

## 14. Informasi Tim Pengembang
### 14.1. Susunan Tim Pengembang
### 14.2. Pembagian Tanggung Jawab per Fase SDLC

---

## 15. Rencana Rilis Selanjutnya (Roadmap)
### 15.1. Fitur yang Direncanakan untuk Versi Berikutnya
### 15.2. Peningkatan yang Direncanakan

---

## 16. Informasi Dukungan Teknis dan Kontak
### 16.1. Kontak Dukungan Teknis
### 16.2. Jam Layanan Operasional
### 16.3. Prosedur Eskalasi

---

## 17. Persetujuan dan Otorisasi Rilis
(Tabel: Posisi, Nama, Tanda Tangan, Tanggal)

---

## 18. Glosarium

---

## 19. Referensi Dokumen
(Tabel: No, Kode Ref, Nama Dokumen, Path, Versi, Prioritas, Peran)
```

---

## 4. Instruksi Detail Pelaksanaan

### Tahap 0: Persiapan Awal

- [ ] **0.1.** Baca dan pahami seluruh isi issue ini (`docs/issue/0055_issue_release_notes.md`) secara menyeluruh sebelum memulai pengerjaan.
- [ ] **0.2.** Pastikan kamu menggunakan persona **Senior Release Manager & Technical Documentation Engineer** selama pengerjaan.
- [ ] **0.3.** Catat bahwa target file output adalah: `docs/sdlc/06_deployment/03_release_notes.md`.
- [ ] **0.4.** Catat bahwa dokumen ini adalah **Deliverable ke-3** pada Fase 06 — Deployment dalam siklus SDLC AbuCom, yang berada setelah Deployment Guide (Deliverable ke-1) dan Environment Config (Deliverable ke-2).

### Tahap 1: Pembacaan dan Perangkuman File Referensi PRIMER

> **INSTRUKSI KRITIS**: Baca setiap file referensi secara **MENYELURUH dari baris pertama hingga baris terakhir**. Jangan melewatkan atau melompati bagian apapun. Rangkum **SEMUA** data dan informasi yang ada di dalam setiap file. Setiap detail jangan sampai ada yang terlewat.

- [ ] **1.1.** Baca file **R-01** (`docs/sdlc/01_planning/01_project_charter.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Nama proyek, deskripsi singkat, versi dokumen, dan tanggal.
  - [ ] Tujuan proyek (umum dan spesifik SMART Goals S.1 s.d S.5).
  - [ ] Manfaat bisnis yang terukur (4 metrik kuantitatif).
  - [ ] Ruang lingkup proyek (in-scope: 9 modul M.1-M.9, dan out-of-scope).
  - [ ] Daftar deliverables per fase SDLC (Fase 1 s.d Fase 6).
  - [ ] Susunan tim pengembang (7 anggota: Junior Programmer + 6 AI).
  - [ ] Milestone dan jadwal tingkat tinggi (8 milestone, 12 bulan).
  - [ ] Estimasi anggaran (5 komponen biaya, total Rp 40 juta).
  - [ ] Kriteria keberhasilan proyek (5 kriteria terukur).
  - [ ] Risiko awal proyek (6 risiko).
  - [ ] Metodologi pengembangan (Hybrid Waterfall & Agile).
  - [ ] Platform & teknologi (Python 3.14.2+, MySQL, FP, CLI, Dual-OS).

- [ ] **1.2.** Baca file **R-02** (`docs/sdlc/02_analysis/02_software_requirements.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Daftar lengkap 10 modul fungsional (M.1 s.d M.10) beserta ringkasan fungsinya.
  - [ ] Daftar lengkap seluruh kebutuhan fungsional (SRS-F-001 s.d SRS-F-040).
  - [ ] Daftar kebutuhan non-fungsional (SRS-NF-001 s.d SRS-NF-011).
  - [ ] Spesifikasi lingkungan runtime (hardware, software, dependency libraries beserta versi).
  - [ ] Karakteristik 8 aktor/pengguna sistem (pemilik, kepala_percetakan, pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang).
  - [ ] Batasan desain dan implementasi (FP murni, CLI only, presisi desimal, multi-branch ready).

- [ ] **1.3.** Baca file **R-03** (`docs/sdlc/06_deployment/01_deployment_guide.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Ringkasan arsitektur deployment (diagram Mermaid, matriks komponen per node).
  - [ ] Perbedaan lingkungan Development vs Staging vs Production (tabel).
  - [ ] Pre-deployment checklist lengkap (7 kategori checklist).
  - [ ] Prosedur deployment server (Debian 12) dan klien kasir (Windows 11).
  - [ ] Prosedur deployment jaringan LAN.
  - [ ] Smoke test verifikasi pasca-deployment (ST-01 s.d ST-06).
  - [ ] Prosedur rollback deployment (database dan kode).
  - [ ] Prosedur go-live, serah terima, dan pelatihan staf.
  - [ ] Periode hypercare (2 minggu).
  - [ ] Prosedur backup dan disaster recovery.
  - [ ] Runbook operasional harian (SOP startup/shutdown, troubleshooting).
  - [ ] Hardening checklist keamanan deployment.
  - [ ] Matriks risiko deployment (8 risiko: RSK-01 s.d RSK-08).
  - [ ] Persetujuan dan otorisasi deployment (tabel stakeholder).

- [ ] **1.4.** Baca file **R-04** (`docs/sdlc/06_deployment/02_environment_config.yaml`) secara menyeluruh. Rangkum dan catat:
  - [ ] Parameter konfigurasi 3 lingkungan (development, staging, production).
  - [ ] Konfigurasi infrastruktur fisik (network, hardware, printer).
  - [ ] Konfigurasi sistem operasi (server Debian 12, client Windows 11).
  - [ ] Konfigurasi database (MySQL 8.4, user, privileges, schema files).
  - [ ] Konfigurasi runtime Python (versi, dependencies, venv, offline install).
  - [ ] Konfigurasi keamanan (bcrypt, JWT, RBAC 8 peran, Fernet, AES-256, hardening OS).
  - [ ] Konfigurasi backup dan recovery (cron, retensi, disaster recovery).
  - [ ] Konfigurasi connection pool dan retry mechanism.
  - [ ] Kode error dan troubleshooting.
  - [ ] Parameter operasional harian (SOP startup/shutdown).
  - [ ] Kontak dukungan teknis dan eskalasi.

- [ ] **1.5.** Baca file **R-05** (`docs/sdlc/05_testing/01_test_plan.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Strategi pengujian (4 tingkat: Unit, Integration, System, UAT).
  - [ ] Tipe pengujian (7 tipe: Functional, Security, Decimal Precision, Database Integrity, CLI Interface, Compatibility Dual-OS, Regression).
  - [ ] Pemetaan cakupan pengujian per modul (M.1 s.d M.10) termasuk jumlah skenario uji.
  - [ ] Exit criteria pengujian (100% pass, coverage ≥ 90%, 0 critical/major bug, UAT sign-off).
  - [ ] Pengujian keamanan (bcrypt, JWT, RBAC, SQL Injection, rate limiting, sanitasi CLI, audit trail, enkripsi, UU PDP).
  - [ ] Pengujian presisi desimal (HPP BOM, ROUND_HALF_UP, rekonsiliasi kas, smart payroll, depresiasi).
  - [ ] Pengujian non-fungsional (performa, ketersediaan, backup/restore, import CSV, kapasitas).
  - [ ] Lingkungan pengujian (hardware dan software).

### Tahap 2: Pembacaan dan Perangkuman File Referensi SEKUNDER

- [ ] **2.1.** Baca file **R-06** (`docs/sdlc/03_design/03_system_architecture.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Diagram arsitektur sistem (topologi LAN, 4-layer arsitektur logis).
  - [ ] Spesifikasi connection pooling ('abupool' size 5) dan retry mechanism.
  - [ ] Desain multi-branch ready (cabang_id di setiap tabel).
  - [ ] Diagram deployment fisik (Mermaid).

- [ ] **2.2.** Baca file **R-07** (`docs/sdlc/03_design/06_security_design.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Detail implementasi bcrypt (cost factor 12, salt 16 bytes).
  - [ ] Detail implementasi JWT (HS256, lifetime 8 jam/28800 detik, payload fields).
  - [ ] Detail RBAC (8 peran, matriks hak akses per menu).
  - [ ] Detail Fernet CRM (enkripsi simetris nomor WhatsApp pelanggan, kepatuhan UU PDP).
  - [ ] Detail AES-256 backup (enkripsi ZIP cadangan database).
  - [ ] Detail audit trail (format JSON, trigger events, retensi 12 bulan).
  - [ ] OS Hardening (ufw firewall rules, SSH root login disabled, chmod 700).
  - [ ] Rate limiting (5 kali gagal, lockout 10 menit).
  - [ ] Sanitasi input CLI.

- [ ] **2.3.** Baca file **R-08** (`docs/sdlc/01_planning/04_tech_stack_decision.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Keputusan stack teknologi utama dan justifikasinya.
  - [ ] Versi locked library (mysql-connector-python==8.4.0, python-dotenv==1.0.1, bcrypt==4.1.0, pyjwt==2.8.0, cryptography==42.0.5, rich==13.7.0, tabulate==0.9.0).
  - [ ] Keputusan paradigma Functional Programming murni.
  - [ ] Keputusan CLI-only dan dual-OS portabilitas.

- [ ] **2.4.** Baca file **R-09** (`docs/sdlc/03_design/01_database_schema.sql`) secara menyeluruh. Rangkum dan catat:
  - [ ] Jumlah total tabel relasional (28 tabel InnoDB).
  - [ ] Daftar nama tabel dan tujuan utamanya.
  - [ ] Engine database (InnoDB), character set (utf8mb4), dan collation.
  - [ ] Fitur-fitur kunci database (Foreign Key, CHECK Constraints, DECIMAL(15,4), cabang_id).

- [ ] **2.5.** Baca file **R-10** (`docs/sdlc/04_implementation/03_module_structure.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Struktur direktori proyek (folder tree ASCII).
  - [ ] Pemetaan modul-to-file (10 modul ke file Python).
  - [ ] Entry point aplikasi (main.py).
  - [ ] Daftar folder utama (cli/, logic/, db/, middleware/, config/, utils/, exports/, tests/).

- [ ] **2.6.** Baca file **R-11** (`docs/sdlc/04_implementation/04_git_workflow.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Konvensi tagging rilis (SemVer: vMAJOR.MINOR.PATCH).
  - [ ] Strategi branching (Feature Branching Model).
  - [ ] Quality gate pre-merge (12 checklist Coding Standard).
  - [ ] Prosedur pembuatan tag release formal.

### Tahap 3: Pembacaan dan Perangkuman File Referensi TERSIER

- [ ] **3.1.** Baca file **R-12** (`docs/sdlc/05_testing/02_test_cases.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Jumlah total kasus uji dan status pengujian.
  - [ ] Distribusi kasus uji per modul.

- [ ] **3.2.** Baca file **R-13** (`docs/sdlc/05_testing/03_uat_script.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Skenario UAT yang dieksekusi.
  - [ ] Kriteria sign-off penerimaan pengguna.

- [ ] **3.3.** Baca file **R-14** (`docs/sdlc/05_testing/04_bug_report_template.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Format pelaporan bug.
  - [ ] Daftar known issues (jika ada).
  - [ ] Status bug terbuka (open) yang belum diperbaiki.

- [ ] **3.4.** Baca file **R-15** (`docs/sdlc/02_analysis/06_access_control_matrix.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Matriks hak akses 8 peran per menu/modul.
  - [ ] Daftar menu yang dibatasi dan eskalasi sandi.

- [ ] **3.5.** Baca file **R-16** (`docs/sdlc/04_implementation/01_coding_standard.md`) secara menyeluruh. Rangkum dan catat:
  - [ ] Standar coding yang diterapkan (PEP 484, PEP 257, Conventional Commits).
  - [ ] Quality gate checklist (12 poin kepatuhan).

### Tahap 4: Filterisasi dan Ekstraksi Data Spesifik Release Notes

> **INSTRUKSI KRITIS**: Dari seluruh rangkuman yang sudah dikumpulkan pada Tahap 1-3, ambil **HANYA** data dan informasi yang secara spesifik dibutuhkan oleh dokumen Release Notes. Tujuannya agar dokumen ini bersih, fokus, dan hanya berisi informasi yang memang seharusnya ada di dalam catatan rilis resmi.

- [ ] **4.1.** Dari rangkuman R-01 (Project Charter), ekstrak hanya:
  - [ ] Nama proyek, versi, deskripsi singkat produk.
  - [ ] Daftar deliverables per fase (sebagai bukti kelengkapan rilis).
  - [ ] Susunan tim pengembang (untuk bagian Informasi Tim).
  - [ ] Estimasi anggaran (opsional, sebagai informasi investasi).
  - [ ] Kriteria keberhasilan proyek (sebagai indikator kualitas rilis).
  - [ ] Roadmap dan rencana fitur berikutnya (dari milestone belum selesai).

- [ ] **4.2.** Dari rangkuman R-02 (SRS), ekstrak hanya:
  - [ ] Daftar fitur baru per modul (M.1-M.10) yang termasuk dalam rilis ini.
  - [ ] Spesifikasi lingkungan runtime yang dibutuhkan (untuk bagian Persyaratan Sistem).
  - [ ] Daftar library dependensi beserta versi locked (untuk bagian Persyaratan Software).
  - [ ] Batasan desain dan out-of-scope (untuk bagian Known Limitations).
  - [ ] Daftar 8 aktor/peran pengguna (untuk bagian fitur keamanan RBAC).

- [ ] **4.3.** Dari rangkuman R-03 (Deployment Guide), ekstrak hanya:
  - [ ] Diagram arsitektur deployment (untuk bagian Arsitektur).
  - [ ] Perbedaan lingkungan (untuk bagian Konfigurasi Default).
  - [ ] Referensi prosedur instalasi dan upgrade (untuk bagian Panduan Instalasi).
  - [ ] Referensi prosedur rollback (untuk bagian Panduan Instalasi).
  - [ ] Matriks risiko deployment (untuk bagian Matriks Risiko Rilis).
  - [ ] Kontak dukungan teknis dan eskalasi (untuk bagian Dukungan Teknis).

- [ ] **4.4.** Dari rangkuman R-04 (Environment Config), ekstrak hanya:
  - [ ] Parameter konfigurasi produksi default (untuk bagian Konfigurasi Default Rilis).
  - [ ] Parameter keamanan default (bcrypt cost, JWT lifetime, rate limiting).
  - [ ] Kode error dan troubleshooting (untuk bagian Known Issues atau Troubleshooting).
  - [ ] Kontak eskalasi.

- [ ] **4.5.** Dari rangkuman R-05 (Test Plan), ekstrak hanya:
  - [ ] Ringkasan hasil pengujian (untuk bagian Quality Assurance Summary).
  - [ ] Exit criteria yang terpenuhi.
  - [ ] Jumlah test cases per modul.

- [ ] **4.6.** Dari rangkuman R-06 s.d R-16, ekstrak data pendukung sesuai kebutuhan masing-masing bab Release Notes.

### Tahap 5: Penyusunan Dokumen Release Notes

> **INSTRUKSI KRITIS**: Gunakan kerangka struktur yang sudah ditentukan di **Bagian 3** issue ini. Pastikan setiap bab dan sub-bab terisi sesuai data yang sudah diekstrak pada Tahap 4.

- [ ] **5.1.** Buat header YAML metadata dokumen sesuai format standar:
  - [ ] Isi `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`, `reviewer`, `approved_by`.
  - [ ] Gunakan versi dokumen `1.0` untuk penyusunan awal.

- [ ] **5.2.** Susun **Riwayat Perubahan Dokumen** (tabel versi, tanggal, deskripsi perubahan, oleh).

- [ ] **5.3.** Susun **Bab 1: Informasi Dokumen**:
  - [ ] Tulis tujuan dokumen Release Notes secara jelas.
  - [ ] Tulis cakupan dokumen (mencakup rilis versi berapa dari produk apa).
  - [ ] Gambarkan posisi dokumen dalam SDLC menggunakan diagram ASCII.
  - [ ] Tulis hubungan input/output dengan dokumen SDLC lainnya.
  - [ ] Tulis audiens target (Pemilik Usaha, Staf Toko, System Administrator).
  - [ ] Tulis daftar definisi, akronim, dan singkatan yang digunakan.

- [ ] **5.4.** Susun **Bab 2: Ringkasan Rilis**:
  - [ ] Tulis nama produk lengkap dan nomor versi rilis (misal v1.0.0).
  - [ ] Tulis tanggal rilis.
  - [ ] Tulis tipe rilis (Major Release — karena ini rilis pertama).
  - [ ] Tulis deskripsi umum rilis (ringkasan 1-2 paragraf tentang apa yang dirilis).
  - [ ] Tulis highlight fitur utama dalam bentuk bullet points (5-10 fitur terpenting).

- [ ] **5.5.** Susun **Bab 3: Persyaratan Sistem**:
  - [ ] Isi spesifikasi hardware minimum (server, klien, jaringan, perangkat pendukung) dari data R-03 dan R-04.
  - [ ] Isi persyaratan software (OS, runtime Python, MySQL, library dependencies beserta versi) dari data R-02, R-04, dan R-08.
  - [ ] Isi persyaratan jaringan (LAN offline, IP statis, topologi bintang) dari data R-03 dan R-06.

- [ ] **5.6.** Susun **Bab 4: Fitur Baru** (per modul M.1 s.d M.10):
  - [ ] Untuk setiap modul, tulis daftar fitur fungsional yang disertakan dalam rilis ini.
  - [ ] Gunakan format tabel atau bullet points untuk setiap fitur.
  - [ ] Sertakan ID referensi SRS (misal SRS-F-001) untuk setiap fitur agar dapat ditelusuri.
  - [ ] Pastikan deskripsi fitur ringkas, jelas, dan menggunakan bahasa Indonesia yang natural.

- [ ] **5.7.** Susun **Bab 5: Fitur Keamanan Rilis**:
  - [ ] Tulis detail fitur otentikasi bcrypt dan JWT dari data R-07.
  - [ ] Tulis detail fitur otorisasi RBAC 8 peran dari data R-07 dan R-15.
  - [ ] Tulis detail proteksi data pribadi Fernet CRM dan kepatuhan UU PDP dari data R-07.
  - [ ] Tulis detail hardening infrastruktur (firewall, SSH, backup AES-256) dari data R-07 dan R-03.
  - [ ] Tulis detail audit trail dan fraud detection dari data R-07.

- [ ] **5.8.** Susun **Bab 6: Perbaikan Bug dan Peningkatan**:
  - [ ] Jika ini adalah rilis pertama (v1.0.0), tulis bahwa ini adalah rilis inisial dan belum ada bug sebelumnya yang diperbaiki.
  - [ ] Catat peningkatan apapun dari validasi dokumen sebelumnya (v1.0 ke v1.1 pada masing-masing dokumen SDLC).
  - [ ] Jika ada data bug dari R-14 (Bug Report Template), masukkan daftar bug yang sudah diperbaiki.
  - [ ] Jika tidak ada data bug, tandai: `[DATA BELUM TERSEDIA — Bagian ini akan diisi setelah fase testing selesai dan bug report final tersedia]`.

- [ ] **5.9.** Susun **Bab 7: Batasan yang Diketahui**:
  - [ ] Tulis batasan fungsional (CLI-only, tidak ada GUI, tidak ada mobile app) dari data R-01.
  - [ ] Tulis batasan teknis (FP murni, Python 3.14.2+ wajib, MySQL only) dari data R-01 dan R-02.
  - [ ] Tulis batasan integrasi pihak ketiga (PPOB manual, e-wallet manual, WhatsApp tidak otomatis) dari data R-01.
  - [ ] Tulis fitur di luar cakupan (out-of-scope) dari data R-01.

- [ ] **5.10.** Susun **Bab 8: Masalah yang Diketahui (Known Issues)**:
  - [ ] Jika ada data known issues dari R-14, buat tabel (ID, Deskripsi, Dampak, Workaround, Status).
  - [ ] Jika tidak ada data known issues, tandai: `[DATA BELUM TERSEDIA — Bagian ini akan diisi setelah fase testing selesai dan daftar known issues teridentifikasi]`.

- [ ] **5.11.** Susun **Bab 9: Panduan Instalasi dan Upgrade**:
  - [ ] Tulis ringkasan langkah instalasi baru (referensikan ke Deployment Guide R-03 untuk detail lengkap).
  - [ ] Tulis keterangan bahwa ini adalah rilis pertama sehingga prosedur upgrade belum tersedia.
  - [ ] Tulis ringkasan prosedur rollback (referensikan ke Bab 8 Deployment Guide).
  - [ ] Berikan referensi langsung ke Deployment Guide untuk instruksi step-by-step.

- [ ] **5.12.** Susun **Bab 10: Konfigurasi Default Rilis**:
  - [ ] Tulis parameter lingkungan produksi default dari data R-04 (database host, port, pool size, dll).
  - [ ] Tulis parameter keamanan default (bcrypt cost 12, JWT lifetime 8 jam, rate limiting 5/10 menit).
  - [ ] Tulis parameter operasional harian (SOP startup 07:45, shutdown 21:05) dari data R-04.
  - [ ] Berikan referensi ke Environment Config YAML untuk detail lengkap.

- [ ] **5.13.** Susun **Bab 11: Hasil Pengujian dan Kualitas Rilis**:
  - [ ] Tulis ringkasan hasil unit testing dari data R-05.
  - [ ] Tulis ringkasan hasil integration testing dari data R-05.
  - [ ] Tulis ringkasan hasil UAT dari data R-05 dan R-13.
  - [ ] Tulis exit criteria yang terpenuhi (100% pass, coverage ≥ 90%, 0 critical/major bug, UAT sign-off).
  - [ ] Jika data aktual testing belum tersedia, tandai: `[DATA BELUM TERSEDIA — Bagian ini akan diisi setelah fase testing selesai dan test report final tersedia]`.

- [ ] **5.14.** Susun **Bab 12: Arsitektur dan Topologi Deployment**:
  - [ ] Salin dan sesuaikan diagram arsitektur Mermaid dari R-03.
  - [ ] Salin matriks komponen per node dari R-03.
  - [ ] Tulis topologi jaringan LAN offline dari data R-03 dan R-06.

- [ ] **5.15.** Susun **Bab 13: Matriks Risiko Rilis**:
  - [ ] Salin dan sesuaikan matriks risiko deployment dari R-03 (RSK-01 s.d RSK-08).
  - [ ] Pastikan format tabel konsisten.

- [ ] **5.16.** Susun **Bab 14: Informasi Tim Pengembang**:
  - [ ] Tulis tabel susunan tim dari data R-01 (7 anggota).
  - [ ] Tulis pembagian tanggung jawab per fase.

- [ ] **5.17.** Susun **Bab 15: Rencana Rilis Selanjutnya (Roadmap)**:
  - [ ] Tulis fitur yang direncanakan untuk versi berikutnya (v1.1.0, v2.0.0) berdasarkan rekomendasi inovasi R-01 Bab 8.3.
  - [ ] Tulis peningkatan yang direncanakan (GUI, mobile app, API integrasi) berdasarkan out-of-scope R-01.

- [ ] **5.18.** Susun **Bab 16: Informasi Dukungan Teknis dan Kontak**:
  - [ ] Tulis kontak dukungan teknis dari data R-03 dan R-04 (WhatsApp, email).
  - [ ] Tulis jam layanan operasional (08:00-21:30 WIB).
  - [ ] Tulis prosedur eskalasi 3 fase (isolasi, pelaporan, pemulihan).

- [ ] **5.19.** Susun **Bab 17: Persetujuan dan Otorisasi Rilis**:
  - [ ] Buat tabel persetujuan (Posisi, Nama, Tanda Tangan, Tanggal) dari data R-03 Bab 14.
  - [ ] Cantumkan minimal 3 stakeholder: Pemilik Usaha, Senior DevOps Lead, Kepala Percetakan.

- [ ] **5.20.** Susun **Bab 18: Glosarium**:
  - [ ] Kumpulkan seluruh istilah teknis dan akronim yang digunakan dalam dokumen.
  - [ ] Tulis definisi singkat untuk setiap istilah.
  - [ ] Urutkan secara alfabet atau numerikal.

- [ ] **5.21.** Susun **Bab 19: Referensi Dokumen**:
  - [ ] Buat tabel referensi lengkap yang mencantumkan seluruh file yang digunakan dalam penyusunan Release Notes ini.
  - [ ] Gunakan format: No, Kode Ref, Nama Dokumen, Path Relatif, Versi, Prioritas (PRIMER/SEKUNDER/TERSIER), Peran/Hubungan.
  - [ ] Cantumkan seluruh 16 file referensi (R-01 s.d R-16) sesuai daftar di **Bagian 2** issue ini.

### Tahap 6: Penandaan Data yang Kosong

> **INSTRUKSI KRITIS**: Jika ada data yang tidak ditemukan atau belum tersedia di dalam file referensi, **JANGAN membuat asumsi atau mengisi data palsu (halusinasi)**. Tandai bagian tersebut dengan format penanda yang konsisten agar pemilik proyek dapat mengidentifikasi dan mengisinya secara manual.

- [ ] **6.1.** Periksa seluruh isi dokumen Release Notes yang sudah disusun.
- [ ] **6.2.** Untuk setiap data yang kosong atau tidak ditemukan di file referensi, gunakan format penanda:
  ```
  [DATA BELUM TERSEDIA — <deskripsi singkat data yang dibutuhkan>]
  ```
- [ ] **6.3.** Contoh penanda yang valid:
  - `[DATA BELUM TERSEDIA — Nomor versi rilis final akan ditentukan setelah tagging Git release]`
  - `[DATA BELUM TERSEDIA — Tanggal rilis resmi akan ditentukan setelah UAT sign-off selesai]`
  - `[DATA BELUM TERSEDIA — Daftar bug yang diperbaiki akan diisi setelah test report final]`
  - `[DATA BELUM TERSEDIA — Hasil aktual unit test coverage akan diisi setelah pengujian]`

### Tahap 7: Validasi Kualitas Dokumen

- [ ] **7.1.** Periksa bahwa seluruh 19 bab dalam kerangka struktur (Bagian 3) telah terisi dengan konten yang substantif.
- [ ] **7.2.** Periksa bahwa tidak ada bab yang kosong tanpa penjelasan atau penanda `[DATA BELUM TERSEDIA]`.
- [ ] **7.3.** Periksa konsistensi data antar-bab:
  - [ ] Versi library di Bab 3 (Persyaratan Sistem) harus konsisten dengan data di R-02 dan R-08.
  - [ ] Daftar modul di Bab 4 (Fitur Baru) harus konsisten dengan 10 modul di R-02.
  - [ ] Parameter keamanan di Bab 5 dan Bab 10 harus konsisten dengan data di R-07 dan R-04.
  - [ ] Matriks risiko di Bab 13 harus konsisten dengan data di R-03 Bab 13.
- [ ] **7.4.** Periksa bahwa bahasa Indonesia yang digunakan bersifat:
  - [ ] Natural dan tidak kaku.
  - [ ] Tidak ambigu dan tidak membingungkan.
  - [ ] Mudah dipahami oleh junior programmer atau AI model lain.
  - [ ] Tidak mengandung istilah asing yang belum didefinisikan di glosarium.
- [ ] **7.5.** Periksa bahwa dokumen ini layak dijadikan sebagai:
  - [ ] Referensi resmi rilis produk AbuCom.
  - [ ] Input bagi penyusunan User Manual dan dokumen operasional pasca-deployment.
  - [ ] Bukti kelengkapan dan kualitas pengembangan sistem kepada stakeholder.
- [ ] **7.6.** Periksa bahwa dokumen tidak memerlukan interupsi berulang yang menghambat proses SDLC selanjutnya (kelengkapan dan kualitas harus final pada versi ini, kecuali bagian yang memang ditandai `[DATA BELUM TERSEDIA]`).

### Tahap 8: Penulisan Output ke Target File

- [ ] **8.1.** Tuangkan seluruh hasil penyusunan dokumen Release Notes ke dalam target file: `docs/sdlc/06_deployment/03_release_notes.md`.
- [ ] **8.2.** Pastikan file ditulis secara **utuh dari baris pertama hingga baris terakhir** tanpa ada bagian yang terpotong (*truncated*) atau hilang.
- [ ] **8.3.** Pastikan format Markdown valid dan ter-render dengan baik (heading, tabel, code blocks, Mermaid diagrams).
- [ ] **8.4.** Pastikan file encoding menggunakan **UTF-8 tanpa BOM**.
- [ ] **8.5.** Pastikan tidak ada placeholder umum (seperti `[TODO]`, `[TBD]`, `[...]`) yang bukan merupakan penanda `[DATA BELUM TERSEDIA]`.

---

## 5. Instruksi Tambahan Khusus Release Notes

Berikut adalah instruksi tambahan yang spesifik dan relevan dengan ciri khas dokumen Release Notes yang mungkin belum tercakup dalam kriteria utama di atas:

### 5.1. Nomor Versi Rilis
- [ ] Gunakan format **Semantic Versioning (SemVer)** sesuai konvensi di R-11 Git Workflow: `vMAJOR.MINOR.PATCH`.
- [ ] Karena ini adalah rilis pertama (inisial), gunakan nomor versi **v1.0.0** sebagai baseline rilis produksi pertama.

### 5.2. Changelog Format
- [ ] Untuk setiap fitur baru di Bab 4, gunakan format changelog yang mudah di-scan:
  ```markdown
  - **[SRS-F-001] Pencatatan Transaksi Penjualan Multi-Divisi**: Sistem mendukung pencatatan transaksi dari 5 divisi usaha (percetakan, ATK, PPOB, jasa keuangan, jasa teknis) secara terintegrasi.
  ```

### 5.3. Kompatibilitas dan Portabilitas
- [ ] Cantumkan secara eksplisit bahwa rilis ini mendukung **dual-OS** (Windows 11 dan Linux Debian 12 Bookworm).
- [ ] Cantumkan bahwa rilis ini beroperasi secara **100% luring (offline-only LAN)** tanpa memerlukan koneksi internet.

### 5.4. Deprecation Notices
- [ ] Karena ini adalah rilis pertama, **tidak ada** fitur yang di-deprecate. Cantumkan pernyataan ini secara eksplisit di dokumen.

### 5.5. Migration Path
- [ ] Cantumkan bahwa rilis ini memigrasikan seluruh operasional pencatatan manual berbasis Microsoft Excel ke sistem aplikasi CLI terintegrasi.
- [ ] Cantumkan referensi ke fitur Import CSV (SRS-F-014) sebagai jalur migrasi data awal dari Excel lama.

### 5.6. Licensing
- [ ] Cantumkan bahwa seluruh software yang digunakan bersifat open-source dan gratis:
  - Linux Debian 12 (Open Source)
  - MySQL Community Server (Open Source / GPL)
  - Python 3.14.2+ (PSF License)
  - Seluruh library dependencies (Open Source licenses)

### 5.7. Compliance
- [ ] Cantumkan secara eksplisit bahwa rilis ini memenuhi kepatuhan terhadap:
  - **UU PDP No. 27 Tahun 2022** (Perlindungan Data Pribadi) melalui enkripsi Fernet pada data CRM pelanggan.
  - Prinsip **ACID** (Atomicity, Consistency, Isolation, Durability) pada integritas transaksi database.
  - Prinsip **Least Privilege** pada manajemen hak akses database user aplikasi.

---

## 6. Ringkasan Checklist Akhir

Sebelum dianggap selesai, pastikan seluruh item berikut telah terpenuhi:

- [ ] Semua 16 file referensi (R-01 s.d R-16) telah dibaca secara menyeluruh.
- [ ] Semua data yang relevan telah dirangkum dan diekstrak.
- [ ] Seluruh 19 bab kerangka dokumen Release Notes telah terisi.
- [ ] Data yang kosong/tidak ditemukan telah ditandai dengan `[DATA BELUM TERSEDIA]`.
- [ ] Konsistensi data antar-bab telah diverifikasi.
- [ ] Bahasa Indonesia natural, tidak ambigu, mudah dipahami.
- [ ] Referensi dokumen (Bab 19) telah lengkap mencantumkan seluruh 16 file referensi.
- [ ] Output telah ditulis utuh ke file `docs/sdlc/06_deployment/03_release_notes.md`.
- [ ] File tidak terpotong (truncated) dan encoding UTF-8 valid.

---

*Issue ini disusun oleh Antigravity pada 27 Mei 2026 sebagai panduan low-level bagi junior programmer atau model AI lain untuk menyusun dokumen Release Notes AbuCom secara komprehensif dan bebas halusinasi.*
