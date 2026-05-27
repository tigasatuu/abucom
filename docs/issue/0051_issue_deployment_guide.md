# Pembuatan dan Penyusunan Dokumen Deployment Guide

---

| Atribut Issue       | Nilai                                                                 |
|---------------------|-----------------------------------------------------------------------|
| **Judul**           | Pembuatan dan Penyusunan Dokumen Deployment Guide                     |
| **Proyek**          | AbuCom — Sistem Manajemen Terpadu Usaha Percetakan                    |
| **Fase SDLC**       | Fase 06 — Deployment                                                  |
| **Target File**     | `docs/sdlc/06_deployment/01_deployment_guide.md`                      |
| **Prioritas**       | High                                                                  |
| **Tanggal Dibuat**  | 2026-05-27                                                            |
| **Status**          | Open                                                                  |
| **Estimasi Effort** | Tinggi (Dokumen Substansif — 15+ Bab Utama)                          |

---

## 1. Deskripsi Issue

Issue ini bertujuan untuk membuat dan menyusun dokumen **Deployment Guide** secara lengkap, terperinci, dan substansif sebagai deliverable pertama pada **Fase 06 — Deployment** dalam siklus SDLC proyek AbuCom. Dokumen ini akan menjadi panduan operasional resmi langkah demi langkah (*step-by-step operational manual*) untuk melakukan deployment (peluncuran) sistem aplikasi AbuCom CLI dari lingkungan pengembangan (*development*) menuju lingkungan produksi (*production*) di toko percetakan fisik AbuCom.

Dokumen Deployment Guide ini harus memuat prosedur teknis yang sangat rinci mencakup:
- **Pre-deployment checklist** — verifikasi kesiapan seluruh komponen sebelum peluncuran.
- **Prosedur deployment server database** — migrasi skema, seed data, konfigurasi MySQL produksi.
- **Prosedur deployment klien kasir** — instalasi aplikasi Python CLI, konfigurasi `.env` produksi, printer thermal.
- **Prosedur deployment jaringan LAN** — konfigurasi topologi fisik, IP statis, firewall, router MikroTik.
- **Prosedur verifikasi pasca-deployment** — smoke test, health check konektivitas, validasi fungsional.
- **Prosedur rollback** — langkah pengembalian ke state aman jika deployment gagal.
- **Prosedur Go-Live** — serah terima sistem ke pemilik usaha, pelatihan staf, dan kriteria keberhasilan peluncuran.
- **Prosedur backup dan disaster recovery produksi** — cron job backup harian, prosedur pemulihan darurat.
- **Runbook operasional harian** — SOP startup/shutdown harian, pemeliharaan berkala, dan eskalasi masalah.
- **Matriks risiko deployment** — identifikasi risiko peluncuran dan rencana mitigasi terukur.

---

## 2. Persona Pelaksana

**Persona yang ditugaskan**: **Senior DevOps Engineer & Release Manager**

**Justifikasi pemilihan persona**:
- Dokumen Deployment Guide secara inheren merupakan domain utama seorang **DevOps Engineer** yang memahami siklus hidup peluncuran sistem (*release lifecycle*) dari development ke production.
- Persona ini memiliki otoritas dan kompetensi untuk menentukan prosedur instalasi infrastruktur server/klien, konfigurasi jaringan LAN, hardening keamanan OS, manajemen backup otomatis, dan prosedur rollback darurat.
- Sebagai **Release Manager**, persona ini bertanggung jawab memastikan seluruh kriteria kesiapan peluncuran (*go-live readiness criteria*) terpenuhi sebelum sistem diserahkan ke pemilik usaha.

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib** dibaca secara menyeluruh, dirangkum, dan dijadikan sumber data utama dalam penyusunan dokumen Deployment Guide ini. File diurutkan berdasarkan prioritas relevansi:

### 3.1. Referensi PRIMER (Wajib Dibaca Menyeluruh — Setiap Detail)

| No | Kode Ref | Nama Dokumen | Path File | Justifikasi Relevansi |
|:---:|:---:|---|---|---|
| 1 | **R-01** | Environment Setup v1.1 | `docs/sdlc/04_implementation/02_environment_setup.md` | **REFERENSI UTAMA TERPENTING.** Memuat seluruh prosedur teknis instalasi server Debian 12, klien Windows 11, MySQL, Python, venv, dependensi, `.env`, Git, printer, UPS, dan troubleshooting. Dokumen Deployment Guide harus meringkas dan mengadaptasi prosedur ini ke konteks peluncuran produksi yang final. |
| 2 | **R-02** | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` | Memuat blueprint arsitektur fisik LAN, topologi jaringan, spesifikasi hardware server/klien, diagram deployment Bab 9, strategi backup & disaster recovery, dan prosedur instalasi awal. |
| 3 | **R-03** | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | Memuat spesifikasi hardening keamanan OS, firewall ufw, proteksi database, bcrypt/JWT, enkripsi backup AES-256, chmod 700, rate limiting, dan SOP respon insiden keamanan. |
| 4 | **R-04** | Tech Stack Decision v1.1 | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Memuat keputusan arsitektural mutlak: Python 3.14.2+, MySQL LTS InnoDB, FP murni, Dual-OS, pustaka wajib, requirements.txt, dan strategi inisialisasi database (schema.sql & seed.sql). |

### 3.2. Referensi SEKUNDER (Dibaca Selektif — Ambil Data yang Relevan)

| No | Kode Ref | Nama Dokumen | Path File | Justifikasi Relevansi |
|:---:|:---:|---|---|---|
| 5 | **R-05** | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` | Memuat layout tree direktori proyek standar, .gitignore, .env.example, dan konvensi branching/commit Git yang relevan untuk prosedur deployment kode. |
| 6 | **R-06** | Database Schema v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | Script DDL fisik 28 tabel InnoDB yang wajib dieksekusi saat migrasi database produksi. |
| 7 | **R-07** | Test Plan v1.1 | `docs/sdlc/05_testing/01_test_plan.md` | Memuat lingkungan pengujian, checklist verifikasi, dan kriteria exit testing yang menjadi prasyarat masuk fase deployment. |
| 8 | **R-08** | Module Structure v1.1 | `docs/sdlc/04_implementation/03_module_structure.md` | Memuat struktur folder modul aplikasi yang akan di-deploy ke klien kasir. |
| 9 | **R-09** | Git Workflow v1.1 | `docs/sdlc/04_implementation/04_git_workflow.md` | Memuat strategi branching, tagging rilis, dan prosedur merge ke branch main untuk deployment produksi. |

### 3.3. Referensi TERSIER (Dibaca Jika Diperlukan)

| No | Kode Ref | Nama Dokumen | Path File | Justifikasi Relevansi |
|:---:|:---:|---|---|---|
| 10 | **R-10** | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | Referensi kebutuhan non-fungsional (performa, ketersediaan, portabilitas) yang wajib diverifikasi saat post-deployment. |
| 11 | **R-11** | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Referensi 8 peran RBAC dan kredensial default yang harus dikonfigurasi saat seed data produksi. |
| 12 | **R-12** | Narasi Pemilik | `docs/sdlc/narasi.txt` | Konteks bisnis dasar toko percetakan, mandat inovasi, dan spesifikasi teknis mandatori owner. |

> **CATATAN PENTING**: File `narasi.txt` (R-12) tetap digunakan sebagai referensi tersier karena masih menyimpan konteks bisnis fundamental (jenis produk/layanan, struktur organisasi, spesifikasi teknis mandatori) yang diperlukan untuk memahami lingkungan deployment fisik toko percetakan. Namun, sebagian besar informasi teknis detail sudah terekstrak dan terdokumentasi secara formal di file referensi primer R-01 s.d R-04.

---

## 4. Kerangka Struktur Dokumen Deployment Guide

Berikut adalah kerangka (*outline*) struktur dokumen yang **wajib** diikuti oleh pelaksana. Kerangka ini disusun mengikuti standar praktik industri deployment guide (IEEE/ISO/IEC 12207, DevOps Release Management best practices) yang diadaptasi untuk konteks sistem lokal LAN offline AbuCom:

```
---
dokumen    : Deployment Guide
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [TANGGAL PENGERJAAN]
status     : Draft
penyusun   : Senior DevOps Engineer & Release Manager
---

# Deployment Guide — AbuCom

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
### 1.7. Prasyarat Deployment (Prerequisites)

---

## 2. Ringkasan Arsitektur Deployment
### 2.1. Diagram Arsitektur Deployment Produksi (Mermaid)
### 2.2. Matriks Komponen Deployment per Node
### 2.3. Perbedaan Lingkungan Development vs Staging vs Production

---

## 3. Pre-Deployment Checklist
### 3.1. Checklist Kesiapan Kode Program
### 3.2. Checklist Kesiapan Testing (Exit Criteria Fase 05)
### 3.3. Checklist Kesiapan Infrastruktur Hardware
### 3.4. Checklist Kesiapan Jaringan LAN
### 3.5. Checklist Kesiapan Database
### 3.6. Checklist Kesiapan Keamanan
### 3.7. Checklist Persetujuan Stakeholder (Sign-off)

---

## 4. Prosedur Deployment Server Database (Linux Debian 12)
### 4.1. Persiapan Fisik Server (Mini PC, UPS, Kabel LAN)
### 4.2. Instalasi dan Konfigurasi Sistem Operasi Debian 12
### 4.3. Hardening Keamanan OS Server (ufw, SSH, chmod)
### 4.4. Instalasi dan Konfigurasi MySQL Server Produksi
### 4.5. Konfigurasi Jaringan IP Statis Server
### 4.6. Migrasi Database Schema Produksi (schema.sql)
### 4.7. Injeksi Data Awal Master Produksi (seed.sql)
### 4.8. Pembuatan Akun Database Aplikasi (abucom_app)
### 4.9. Konfigurasi Backup Otomatis (Cron Job Harian)
### 4.10. Verifikasi Status Service MySQL

---

## 5. Prosedur Deployment Klien Kasir (Windows 11)
### 5.1. Persiapan Fisik PC Kasir (UPS, Printer Thermal)
### 5.2. Konfigurasi Sistem Operasi Windows 11
### 5.3. Instalasi Runtime Python 3.14.2+ Produksi
### 5.4. Deployment Kode Aplikasi AbuCom CLI
### 5.5. Pembuatan Virtual Environment dan Instalasi Dependensi
### 5.6. Konfigurasi File .env Produksi
### 5.7. Konfigurasi Windows Terminal (UTF-8)
### 5.8. Konfigurasi Driver Printer Thermal
### 5.9. Konfigurasi Keamanan Klien (Akun Terbatas, Disable USB Autorun)
### 5.10. Pembuatan Shortcut Peluncuran Aplikasi

---

## 6. Prosedur Deployment Jaringan LAN
### 6.1. Pemasangan Fisik Topologi Jaringan (Star Topology)
### 6.2. Konfigurasi Router MikroTik (DHCP, IP Statis)
### 6.3. Konfigurasi Switch Hub Gigabit
### 6.4. Verifikasi Konektivitas Antar-Node (Ping, Port Test)
### 6.5. Pengujian Latensi dan Throughput LAN

---

## 7. Prosedur Verifikasi Pasca-Deployment (Post-Deployment Verification)
### 7.1. Smoke Test Konektivitas Database
### 7.2. Smoke Test Startup Aplikasi CLI
### 7.3. Smoke Test Login dan Autentikasi
### 7.4. Smoke Test Transaksi End-to-End
### 7.5. Smoke Test Pencetakan Struk Thermal
### 7.6. Smoke Test Backup Manual
### 7.7. Health Check Checklist Produksi

---

## 8. Prosedur Rollback Deployment
### 8.1. Kondisi Pemicu Rollback
### 8.2. Prosedur Rollback Database (Restore dari Backup)
### 8.3. Prosedur Rollback Kode Aplikasi (Git Revert)
### 8.4. Prosedur Rollback Konfigurasi Sistem
### 8.5. Verifikasi Pasca-Rollback

---

## 9. Prosedur Go-Live dan Serah Terima Sistem
### 9.1. Kriteria Keberhasilan Go-Live (Go/No-Go Decision)
### 9.2. Prosedur Serah Terima Sistem ke Pemilik Usaha
### 9.3. Pelatihan Staf Operasional (Training Plan)
### 9.4. Periode Stabilisasi (Hypercare Period)
### 9.5. Dokumentasi Serah Terima (Handover Checklist)

---

## 10. Prosedur Backup dan Disaster Recovery Produksi
### 10.1. Konfigurasi Cron Job Backup Harian Otomatis
### 10.2. Prosedur Backup Manual On-Demand
### 10.3. Strategi Retensi dan Rotasi Backup
### 10.4. Prosedur Disaster Recovery (Pemulihan Bencana)
### 10.5. Simulasi Uji Pemulihan Berkala

---

## 11. Runbook Operasional Harian
### 11.1. SOP Startup Harian Sistem (Buka Toko)
### 11.2. SOP Shutdown Harian Sistem (Tutup Toko)
### 11.3. SOP Pemeliharaan Berkala (Mingguan/Bulanan)
### 11.4. SOP Penanganan Masalah Umum (Troubleshooting)
### 11.5. SOP Eskalasi Masalah Kritis
### 11.6. SOP Graceful Shutdown saat Mati Listrik (UPS)

---

## 12. Keamanan Deployment
### 12.1. Hardening Checklist Produksi
### 12.2. Manajemen Kredensial Produksi (.env)
### 12.3. Verifikasi Konfigurasi Firewall Produksi
### 12.4. Verifikasi Enkripsi Backup AES-256
### 12.5. Verifikasi Kepatuhan UU PDP No. 27/2022

---

## 13. Matriks Risiko Deployment
### 13.1. Identifikasi Risiko Peluncuran
### 13.2. Analisis Dampak dan Probabilitas
### 13.3. Rencana Mitigasi per Risiko
### 13.4. Rencana Kontingensi

---

## 14. Persetujuan dan Otorisasi Deployment
(Tabel stakeholder, tanda tangan, tanggal)

---

## 15. Glosarium

---

## 16. Referensi Dokumen
(Tabel file referensi yang digunakan dalam penyusunan)
```

---

## 5. Instruksi Detail Pelaksanaan (Low-Level Checklist)

Berikut adalah tahapan demi tahapan yang **wajib** dilakukan oleh pelaksana (junior programmer atau LLM model AI yang lebih kecil/murah) untuk mengimplementasikan issue ini. Ikuti setiap checklist secara berurutan tanpa melewatkan satupun langkah.

---

### TAHAP 1: Persiapan dan Pembacaan File Referensi

> **TUJUAN**: Mengumpulkan, membaca, dan merangkum seluruh data dan informasi dari file referensi yang telah ditentukan. Setiap detail data yang relevan dengan Deployment Guide harus ditangkap — jangan sampai ada yang terlewat.

- [ ] **1.1** Baca file referensi **R-01** (`docs/sdlc/04_implementation/02_environment_setup.md`) secara menyeluruh dari baris pertama hingga baris terakhir. Ini adalah referensi **PALING PENTING** karena memuat seluruh prosedur teknis setup infrastruktur yang akan diadaptasi ke konteks deployment produksi.
- [ ] **1.2** Rangkum dari R-01 semua informasi berikut (catat setiap detail, jangan sampai terlewat):
  - [ ] 1.2.1 — Spesifikasi hardware server (Mini PC, prosesor, RAM, SSD, port jaringan)
  - [ ] 1.2.2 — Spesifikasi hardware klien kasir (PC Desktop, prosesor, RAM, SSD)
  - [ ] 1.2.3 — Spesifikasi perangkat jaringan (Switch Hub, Router MikroTik, Kabel Cat6)
  - [ ] 1.2.4 — Spesifikasi perangkat pendukung (UPS 600VA, Printer Thermal, Laci Kasir)
  - [ ] 1.2.5 — Prosedur instalasi Debian 12 Bookworm (langkah demi langkah, hostname, partisi, software selection)
  - [ ] 1.2.6 — Konfigurasi IP Statis server (`192.168.1.200`, `/etc/network/interfaces`)
  - [ ] 1.2.7 — Konfigurasi firewall ufw (deny incoming, allow SSH port 22, allow MySQL port 3306 dari 192.168.1.0/24)
  - [ ] 1.2.8 — Konfigurasi SSH hardening (`PermitRootLogin no`)
  - [ ] 1.2.9 — Pembuatan direktori backup (`/var/lib/mysql-backups/`, `chmod 700`)
  - [ ] 1.2.10 — Prosedur kompilasi Python 3.14.2+ dari source di Debian 12 (termasuk offline)
  - [ ] 1.2.11 — Prosedur instalasi Python 3.14.2+ di Windows 11 (termasuk PATH, admin)
  - [ ] 1.2.12 — Konfigurasi Windows Terminal UTF-8 (`chcp 65001`)
  - [ ] 1.2.13 — Keamanan klien Windows (akun Standard User, disable USB Autorun)
  - [ ] 1.2.14 — Prosedur instalasi MySQL Community Server LTS di Debian 12
  - [ ] 1.2.15 — Konfigurasi keamanan MySQL (`mysql_secure_installation`)
  - [ ] 1.2.16 — Konfigurasi bind-address (`192.168.1.200`), character set `utf8mb4`, isolation level `REPEATABLE READ`
  - [ ] 1.2.17 — Pembuatan database `abucom_db` dan `abucom_test_db`
  - [ ] 1.2.18 — Pembuatan akun MySQL `abucom_app` dengan privilege terbatas (SELECT, INSERT, UPDATE, DELETE)
  - [ ] 1.2.19 — Eksekusi `schema.sql` dan `seed.sql`
  - [ ] 1.2.20 — Verifikasi konektivitas remote MySQL dari klien Windows (ping, port test 3306)
  - [ ] 1.2.21 — Pembuatan virtual environment (`venv`), instalasi requirements.txt (termasuk offline wheels)
  - [ ] 1.2.22 — Daftar lengkap dependensi dan versi terkunci (mysql-connector-python, python-dotenv, bcrypt, pyjwt, cryptography, rich, tabulate, pytest, coverage)
  - [ ] 1.2.23 — Template `.env.example` lengkap (DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, DB_POOL_SIZE, JWT_SECRET_KEY, JWT_LIFETIME_SECONDS, FERNET_KEY, BACKUP_ZIP_PASSWORD, PRINTER_PORT, PRINTER_WIDTH_MM)
  - [ ] 1.2.24 — Prosedur generasi JWT Secret Key dan Fernet Key
  - [ ] 1.2.25 — Konvensi penanganan NULL MySQL ke Python None (`handle_null_decimal`)
  - [ ] 1.2.26 — Standar presisi desimal `ROUND_HALF_UP`
  - [ ] 1.2.27 — Template `.gitignore`
  - [ ] 1.2.28 — Konfigurasi Git identity, inisialisasi repository, strategi branching
  - [ ] 1.2.29 — Konfigurasi printer thermal (Generic/Text Only, port COM1/USB001)
  - [ ] 1.2.30 — Konfigurasi UPS (`apcupsd`, parameter BATTERYLEVEL 10, MINUTES 3)
  - [ ] 1.2.31 — Konfigurasi Router MikroTik (DHCP, IP Statis Make Static)
  - [ ] 1.2.32 — Setup lingkungan testing (database sandbox `abucom_test_db`, `.env.test`)
  - [ ] 1.2.33 — Setup backup dan recovery (direktori backup, enkripsi AES-256, prosedur restore manual)
  - [ ] 1.2.34 — Seluruh checklist verifikasi akhir lingkungan (Bab 13 Environment Setup)
  - [ ] 1.2.35 — Seluruh troubleshooting umum (koneksi DB, rendering ANSI, encoding UTF-8, dependensi Python, printer thermal)
  - [ ] 1.2.36 — Skrip otomasi setup (`setup_env.bat`)
  - [ ] 1.2.37 — Daftar port jaringan yang digunakan (3306 TCP, 22 TCP)

- [ ] **1.3** Baca file referensi **R-02** (`docs/sdlc/03_design/03_system_architecture.md`) secara menyeluruh. Rangkum informasi berikut:
  - [ ] 1.3.1 — Diagram konteks sistem dan batasan sistem (in-scope vs out-of-scope)
  - [ ] 1.3.2 — Arsitektur infrastruktur fisik (topologi LAN, spesifikasi hardware)
  - [ ] 1.3.3 — Konfigurasi OS server dan klien (dual-OS)
  - [ ] 1.3.4 — Strategi portabilitas lintas OS (pathlib, UTF-8, OS detection)
  - [ ] 1.3.5 — Arsitektur berlapis 4-layer (Presentation, Business Logic, Data Access, Persistence)
  - [ ] 1.3.6 — Arsitektur modular (10 modul fungsional dan peta dependensi)
  - [ ] 1.3.7 — Arsitektur data (connection pooling, retry mechanism, ACID, decimal precision, multi-branch ready)
  - [ ] 1.3.8 — Arsitektur keamanan (bcrypt, JWT, RBAC, sanitasi, audit trail, AES-256, UU PDP)
  - [ ] 1.3.9 — Diagram deployment (Bab 9 — Node Server, Node Klien, Perangkat Eksternal)
  - [ ] 1.3.10 — Strategi instalasi & setup awal (Bab 9.2)
  - [ ] 1.3.11 — Strategi backup & disaster recovery (Bab 9.3 — mysqldump cron job, AES-256 ZIP)
  - [ ] 1.3.12 — Strategi pemeliharaan (Bab 9.4 — log rotation, audit trail cleanup)
  - [ ] 1.3.13 — Konfigurasi file .env (template lengkap dari Bab 9.2.4)
  - [ ] 1.3.14 — Architecture Decision Records (5 ADR — LAN vs Cloud, FP vs OOP, CLI vs GUI, MySQL vs alternatif, JWT vs server-side session)
  - [ ] 1.3.15 — Analisis risiko arsitektur (9 risiko teknis dan mitigasi)

- [ ] **1.4** Baca file referensi **R-03** (`docs/sdlc/03_design/06_security_design.md`) secara menyeluruh. Rangkum informasi berikut:
  - [ ] 1.4.1 — Prinsip keamanan utama (Least Privilege, Defense in Depth, Separation of Duties, Default Deny, Fail-Secure, Data Minimization)
  - [ ] 1.4.2 — Model ancaman (8 threat: THR-001 s.d THR-008)
  - [ ] 1.4.3 — Klasifikasi sensitivitas data (3 tingkat: Sangat Sensitif, Sensitif, Operasional)
  - [ ] 1.4.4 — Hardening OS server dan klien
  - [ ] 1.4.5 — Keamanan koneksi database (parameterized queries, privilege minimization, ACID, repeatable read)
  - [ ] 1.4.6 — Otentikasi (bcrypt cost 12, JWT HS256 8 jam, rate limiting 5x/lockout 10 menit)
  - [ ] 1.4.7 — Otorisasi RBAC (8 peran, matriks akses, eskalasi supervisor)
  - [ ] 1.4.8 — Proteksi data (AES-256 backup, Fernet CRM, UU PDP)
  - [ ] 1.4.9 — Manajemen kredensial (.env isolation, .gitignore, startup validator)
  - [ ] 1.4.10 — Prosedur serah terima shift (handover security)
  - [ ] 1.4.11 — Prosedur backup dan restore aman
  - [ ] 1.4.12 — Prosedur pengelolaan akun pengguna (pembuatan, perubahan password, penonaktifan)
  - [ ] 1.4.13 — Keamanan fisik server
  - [ ] 1.4.14 — Kode error keamanan (ERR-AUTH, ERR-SESSION, ERR-DB, ERR-FILE, ERR-CASH)
  - [ ] 1.4.15 — SOP respon insiden keamanan (definisi insiden, fase deteksi, isolasi, pemulihan, pasca-insiden)

- [ ] **1.5** Baca file referensi **R-04** (`docs/sdlc/01_planning/04_tech_stack_decision.md`) secara menyeluruh. Rangkum informasi berikut:
  - [ ] 1.5.1 — Batasan teknologi mandatori (Python 3.14.2+, FP murni, MySQL, pustaka wajib, Dual-OS, CLI)
  - [ ] 1.5.2 — Prinsip arsitektur panduan (7 prinsip)
  - [ ] 1.5.3 — Spesifikasi platform Dual-OS (Debian 12 server, Windows 11 klien)
  - [ ] 1.5.4 — Arsitektur Client-Server LAN (topologi, hardware, konektivitas)
  - [ ] 1.5.5 — Strategi requirements.txt (versi terkunci)
  - [ ] 1.5.6 — Strategi inisialisasi database (schema.sql & seed.sql)
  - [ ] 1.5.7 — Keamanan dan autentikasi (bcrypt, JWT, RBAC, audit trail, UU PDP, SQL injection, rate limiting, sanitasi input)

- [ ] **1.6** Baca file referensi **R-05** (`docs/sdlc/04_implementation/01_coding_standard.md`) secara selektif. Catat:
  - [ ] 1.6.1 — Layout tree direktori proyek standar
  - [ ] 1.6.2 — Template `.gitignore` dan `.env.example`
  - [ ] 1.6.3 — Konvensi commit message dan branching

- [ ] **1.7** Baca file referensi **R-06** (`docs/sdlc/03_design/01_database_schema.sql`) secara selektif. Catat:
  - [ ] 1.7.1 — Daftar 28 tabel InnoDB yang harus dimigrasi
  - [ ] 1.7.2 — Instruksi CREATE DATABASE dan CHARACTER SET

- [ ] **1.8** Baca file referensi **R-07** (`docs/sdlc/05_testing/01_test_plan.md`) secara selektif. Catat:
  - [ ] 1.8.1 — Exit criteria pengujian yang menjadi prasyarat deployment (Bab 3.4.2)
  - [ ] 1.8.2 — Spesifikasi lingkungan pengujian (hardware, software, database sandbox)

- [ ] **1.9** Baca file referensi **R-08** (`docs/sdlc/04_implementation/03_module_structure.md`) secara selektif. Catat:
  - [ ] 1.9.1 — Struktur folder modul yang akan di-deploy

- [ ] **1.10** Baca file referensi **R-09** (`docs/sdlc/04_implementation/04_git_workflow.md`) secara selektif. Catat:
  - [ ] 1.10.1 — Prosedur tagging rilis versi
  - [ ] 1.10.2 — Prosedur merge feature branch ke main untuk rilis produksi

- [ ] **1.11** Baca file referensi **R-10** (`docs/sdlc/02_analysis/02_software_requirements.md`) secara selektif. Catat:
  - [ ] 1.11.1 — Kebutuhan non-fungsional (performa, ketersediaan, portabilitas) sebagai kriteria verifikasi pasca-deployment

- [ ] **1.12** Baca file referensi **R-11** (`docs/sdlc/02_analysis/06_access_control_matrix.md`) secara selektif. Catat:
  - [ ] 1.12.1 — 8 peran RBAC default dan kredensial awal yang harus disediakan saat seed data produksi

- [ ] **1.13** Baca file referensi **R-12** (`docs/sdlc/narasi.txt`) secara selektif. Catat:
  - [ ] 1.13.1 — Konteks bisnis toko percetakan (jenis produk/layanan)
  - [ ] 1.13.2 — Struktur organisasi (7 posisi staf)
  - [ ] 1.13.3 — Spesifikasi teknis mandatori owner (Python, FP, MySQL, Dual-OS)

---

### TAHAP 2: Penyusunan Dokumen Deployment Guide

> **TUJUAN**: Menulis dokumen Deployment Guide berdasarkan kerangka struktur di Bab 4 dan data rangkuman dari Tahap 1. Pastikan hanya data dan informasi yang relevan secara spesifik untuk konteks deployment yang dimasukkan ke dalam dokumen ini.

- [ ] **2.1** Buat file target: `docs/sdlc/06_deployment/01_deployment_guide.md`
- [ ] **2.2** Tulis **header metadata** (frontmatter) dokumen sesuai format standar proyek AbuCom:
  ```
  ---
  dokumen    : Deployment Guide
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [TANGGAL PENGERJAAN]
  status     : Draft
  penyusun   : Senior DevOps Engineer & Release Manager
  ---
  ```

- [ ] **2.3** Tulis **Riwayat Perubahan Dokumen** dalam format tabel markdown (kolom: Versi, Tanggal, Perubahan, Oleh).

- [ ] **2.4** Tulis **Bab 1 — Informasi Dokumen** secara lengkap:
  - [ ] 2.4.1 — Tujuan Dokumen: Jelaskan bahwa dokumen ini adalah panduan operasional langkah demi langkah untuk meluncurkan sistem AbuCom CLI dari development ke production di toko percetakan fisik.
  - [ ] 2.4.2 — Cakupan Dokumen: Sebutkan semua cakupan (deployment server, klien, jaringan, verifikasi, rollback, go-live, backup, runbook operasional).
  - [ ] 2.4.3 — Posisi Dokumen dalam SDLC: Gambarkan diagram posisi sebagai deliverable pertama Fase 06 — Deployment, setelah Fase 05 — Testing.
  - [ ] 2.4.4 — Hubungan dengan Dokumen SDLC Lainnya: Cantumkan dokumen Input (R-01 s.d R-12) dan dokumen Output (User Manual, Maintenance Guide jika ada).
  - [ ] 2.4.5 — Audiens Target: Junior Programmer (Pemilik), Tim AI, System Administrator.
  - [ ] 2.4.6 — Definisi, Akronim, Singkatan: Minimal 20 istilah relevan deployment (Go-Live, Rollback, Hypercare, Smoke Test, Health Check, Runbook, Cron Job, Graceful Shutdown, dll.).
  - [ ] 2.4.7 — Prasyarat Deployment: Sebutkan syarat mutlak yang harus terpenuhi sebelum deployment dimulai (seluruh kode committed, testing passed, hardware terpasang, dll.).

- [ ] **2.5** Tulis **Bab 2 — Ringkasan Arsitektur Deployment** berdasarkan data dari R-02 (System Architecture Bab 9):
  - [ ] 2.5.1 — Buat diagram Mermaid arsitektur deployment produksi (adaptasi dari Bab 9.1 System Architecture).
  - [ ] 2.5.2 — Buat tabel matriks komponen per node (Server Debian vs Klien Windows).
  - [ ] 2.5.3 — Buat tabel perbedaan lingkungan Development vs Production (adaptasi dari Bab 2.3 Environment Setup).

- [ ] **2.6** Tulis **Bab 3 — Pre-Deployment Checklist** secara sangat detail dengan format checkbox `[ ]` untuk setiap item:
  - [ ] 2.6.1 — Checklist kesiapan kode program (semua modul committed, branch main stabil, tagging rilis).
  - [ ] 2.6.2 — Checklist kesiapan testing (exit criteria Fase 05 terpenuhi: 100% test case pass, coverage ≥ 90%, 0% bug Critical/Major, UAT sign-off).
  - [ ] 2.6.3 — Checklist kesiapan hardware (server terpasang, klien terpasang, UPS, printer, switch, router, kabel Cat6).
  - [ ] 2.6.4 — Checklist kesiapan jaringan (konektivitas ping, port 3306 terbuka, latensi < 1ms).
  - [ ] 2.6.5 — Checklist kesiapan database (schema.sql valid, seed.sql valid, akun abucom_app dibuat).
  - [ ] 2.6.6 — Checklist kesiapan keamanan (firewall aktif, SSH hardened, backup folder locked, .env lengkap, JWT/Fernet key generated).
  - [ ] 2.6.7 — Checklist persetujuan stakeholder (sign-off pemilik usaha).

- [ ] **2.7** Tulis **Bab 4 — Prosedur Deployment Server Database** berdasarkan data dari R-01 dan R-02. Setiap sub-bab harus memuat:
  - Langkah-langkah yang **sangat detail** dan **berurutan** (numbered steps).
  - Perintah terminal yang **siap di-copy-paste** dalam blok kode (`bash`).
  - Keterangan OS target di setiap blok kode (`# [LINUX DEBIAN 12 — Server]`).
  - Tanda peringatan `⚠️ [HARUS DIISI MANUAL]` untuk parameter yang perlu disesuaikan per instalasi.
  - Langkah verifikasi (`Diharapkan output menampilkan: ...`) setelah setiap prosedur konfigurasi.

- [ ] **2.8** Tulis **Bab 5 — Prosedur Deployment Klien Kasir** berdasarkan data dari R-01 dan R-02. Sama seperti Bab 4, setiap langkah harus sangat detail dengan perintah terminal siap pakai.

- [ ] **2.9** Tulis **Bab 6 — Prosedur Deployment Jaringan LAN** berdasarkan data dari R-01 (Bab 10.3 Router MikroTik) dan R-02 (Bab 3).

- [ ] **2.10** Tulis **Bab 7 — Prosedur Verifikasi Pasca-Deployment** yang mencakup serangkaian smoke test dan health check untuk memvalidasi bahwa deployment berhasil. Setiap smoke test harus memiliki:
  - Tujuan pengujian.
  - Langkah-langkah eksekusi yang detail.
  - Hasil yang diharapkan (*expected result*).
  - Kriteria kelulusan (*pass/fail criteria*).

- [ ] **2.11** Tulis **Bab 8 — Prosedur Rollback Deployment** yang mencakup:
  - Kondisi pemicu rollback (kapan rollback harus dilakukan).
  - Langkah rollback database (restore dari backup terakhir yang valid).
  - Langkah rollback kode (git revert atau checkout ke tag rilis sebelumnya).
  - Langkah rollback konfigurasi sistem.
  - Verifikasi pasca-rollback.

- [ ] **2.12** Tulis **Bab 9 — Prosedur Go-Live dan Serah Terima Sistem** yang mencakup:
  - Kriteria Go/No-Go decision (checklist keputusan peluncuran).
  - Prosedur serah terima resmi ke pemilik usaha.
  - Rencana pelatihan staf operasional (durasi, materi, metode).
  - Periode hypercare (durasi monitoring ketat pasca-peluncuran, biasanya 1-2 minggu).
  - Template checklist handover.

- [ ] **2.13** Tulis **Bab 10 — Prosedur Backup dan Disaster Recovery Produksi** berdasarkan data dari R-01 (Bab 12), R-02 (Bab 9.3), dan R-03 (Bab 8.2). Mencakup:
  - Konfigurasi cron job backup harian otomatis (contoh crontab entry, waktu 21:00 WIB).
  - Prosedur backup manual on-demand.
  - Strategi retensi backup (berapa lama disimpan, rotasi).
  - Prosedur disaster recovery lengkap step-by-step.
  - Rencana simulasi uji pemulihan berkala (setidaknya 1x per kuartal).

- [ ] **2.14** Tulis **Bab 11 — Runbook Operasional Harian** yang mencakup SOP operasional untuk staf toko:
  - SOP startup harian (nyalakan server → cek MySQL → nyalakan klien → login → verifikasi koneksi).
  - SOP shutdown harian (serah terima shift → logout → backup → shutdown klien → shutdown server → matikan UPS).
  - SOP pemeliharaan berkala (update security patches, log rotation, audit trail cleanup, stock opname fisik hardware).
  - SOP troubleshooting umum (adaptasi dari R-01 Bab 14).
  - SOP eskalasi masalah kritis (kapan dan bagaimana menghubungi support teknis).
  - SOP graceful shutdown saat mati listrik (UPS countdown, prioritas aksi).

- [ ] **2.15** Tulis **Bab 12 — Keamanan Deployment** berdasarkan data dari R-03:
  - Hardening checklist produksi (format checkbox).
  - Manajemen kredensial produksi (generasi key, penyimpanan aman, rotasi berkala).
  - Verifikasi konfigurasi firewall.
  - Verifikasi enkripsi backup.
  - Verifikasi kepatuhan UU PDP.

- [ ] **2.16** Tulis **Bab 13 — Matriks Risiko Deployment** dalam format tabel:
  - Kolom: ID Risiko, Komponen, Deskripsi Risiko, Probabilitas (1-5), Dampak (1-5), Skor Risiko, Rencana Mitigasi, Rencana Kontingensi.
  - Minimal 8 risiko deployment spesifik (hardware failure, network failure, database corruption, konfigurasi salah, power outage, staf belum terlatih, rollback gagal, data loss).

- [ ] **2.17** Tulis **Bab 14 — Persetujuan dan Otorisasi Deployment** dalam format tabel stakeholder (Pemilik Usaha, Senior DevOps Engineer).

- [ ] **2.18** Tulis **Bab 15 — Glosarium** dengan minimal 25 istilah teknis yang relevan dengan deployment.

- [ ] **2.19** Tulis **Bab 16 — Referensi Dokumen** dalam format tabel yang mencantumkan seluruh 12 file referensi (R-01 s.d R-12) beserta path file, versi, prioritas, dan peran/hubungan dalam penyusunan.

---

### TAHAP 3: Penandaan Data Kosong

> **TUJUAN**: Memastikan setiap data yang tidak tersedia di file referensi ditandai dengan jelas agar bisa diisi secara manual.

- [ ] **3.1** Periksa seluruh isi dokumen yang telah ditulis. Untuk setiap data, parameter, atau informasi yang **tidak tersedia** di file referensi (misalnya password riil, IP address aktual router toko, nama domain toko, detail perangkat keras spesifik yang dibeli), tandai dengan format berikut:
  ```
  > ⚠️ **[HARUS DIISI MANUAL]**: [Deskripsi data yang harus diisi secara manual oleh pemilik usaha saat instalasi fisik].
  ```
- [ ] **3.2** Untuk data yang bersifat placeholder teknis (misalnya contoh password, contoh IP), gunakan format:
  ```
  > ⚠️ **[PLACEHOLDER — GANTI SAAT DEPLOYMENT]**: [Deskripsi nilai placeholder yang harus diganti dengan nilai produksi riil].
  ```

---

### TAHAP 4: Penyaringan Konten (Content Filtering)

> **TUJUAN**: Memastikan dokumen Deployment Guide hanya berisi data dan informasi yang memang seharusnya ada dalam dokumen ini, tanpa duplikasi atau pencampuran konten dari domain dokumen lain.

- [ ] **4.1** Periksa ulang seluruh bab. Pastikan **TIDAK ADA** konten berikut yang masuk ke dalam Deployment Guide (karena sudah dibahas di dokumen lain):
  - [ ] 4.1.1 — Detail logika bisnis pemrograman (milik Coding Standard dan Module Structure).
  - [ ] 4.1.2 — Detail desain UI/UX CLI atau alur navigasi menu (milik CLI Interaction Flow).
  - [ ] 4.1.3 — Detail test cases atau skenario pengujian (milik Test Plan dan Test Cases).
  - [ ] 4.1.4 — Detail spesifikasi fungsional modul (milik SRS).
  - [ ] 4.1.5 — Detail skema database atau relasi tabel (milik Database Schema dan ERD).
  - [ ] 4.1.6 — Detail desain arsitektur perangkat lunak internal (milik System Architecture).

- [ ] **4.2** Pastikan dokumen Deployment Guide **HANYA FOKUS** pada:
  - [ ] 4.2.1 — Prosedur teknis instalasi dan konfigurasi infrastruktur produksi.
  - [ ] 4.2.2 — Prosedur verifikasi dan validasi pasca-deployment.
  - [ ] 4.2.3 — Prosedur rollback dan disaster recovery.
  - [ ] 4.2.4 — Prosedur go-live, serah terima, dan pelatihan.
  - [ ] 4.2.5 — SOP operasional harian (runbook).
  - [ ] 4.2.6 — Checklist dan matriks risiko deployment.

---

### TAHAP 5: Pengecekan Kualitas Dokumen

> **TUJUAN**: Memastikan kualitas dokumen memenuhi standar kelengkapan dan kejelasan agar layak dijadikan referensi oleh dokumen SDLC selanjutnya.

- [ ] **5.1** Periksa **konsistensi terminologi** di seluruh dokumen:
  - [ ] 5.1.1 — Pastikan nama proyek selalu ditulis "AbuCom" (bukan "Abu Com" atau "abu-com").
  - [ ] 5.1.2 — Pastikan nama database selalu ditulis `abucom_db` (produksi) dan `abucom_test_db` (testing).
  - [ ] 5.1.3 — Pastikan alamat IP server selalu ditulis `192.168.1.200`.
  - [ ] 5.1.4 — Pastikan nama akun database selalu ditulis `abucom_app`.
  - [ ] 5.1.5 — Pastikan format kode error konsisten (`ERR-XXX-YYY`).

- [ ] **5.2** Periksa **kelengkapan diagram Mermaid**:
  - [ ] 5.2.1 — Minimal 3 diagram Mermaid: (1) Diagram arsitektur deployment, (2) Diagram alur deployment, (3) Diagram alur rollback.
  - [ ] 5.2.2 — Pastikan setiap diagram memiliki styling (classDef), label yang jelas, dan komentar penjelasan.

- [ ] **5.3** Periksa **kelengkapan tabel**:
  - [ ] 5.3.1 — Minimal 8 tabel utama: (1) Riwayat perubahan, (2) Matriks komponen, (3) Perbedaan lingkungan, (4) Pre-deployment checklist, (5) Smoke test results, (6) Matriks risiko, (7) Stakeholder approval, (8) Referensi dokumen.

- [ ] **5.4** Periksa **bahasa Indonesia** yang digunakan:
  - [ ] 5.4.1 — Pastikan kalimat ditulis secara natural, tidak ambigu, dan mudah dipahami.
  - [ ] 5.4.2 — Hindari kalimat yang terlalu panjang (maksimal 2-3 anak kalimat per kalimat).
  - [ ] 5.4.3 — Gunakan istilah teknis berbahasa Inggris yang sudah lazim (deploy, rollback, backup, restore, dll.) tanpa menerjemahkannya secara paksa.
  - [ ] 5.4.4 — Pastikan tidak ada typo atau kesalahan ejaan.

- [ ] **5.5** Periksa **kelayakan sebagai referensi** bagi dokumen SDLC selanjutnya:
  - [ ] 5.5.1 — Pastikan dokumen ini cukup detail untuk digunakan sebagai panduan mandiri oleh Junior Programmer tanpa perlu bertanya.
  - [ ] 5.5.2 — Pastikan setiap prosedur memiliki langkah verifikasi (*expected result*) agar pelaksana tahu prosedur berhasil.
  - [ ] 5.5.3 — Pastikan seluruh parameter konfigurasi yang bersifat variabel sudah ditandai `⚠️ [HARUS DIISI MANUAL]`.

- [ ] **5.6** Periksa **integritas cross-reference** antar bab:
  - [ ] 5.6.1 — Pastikan setiap referensi ke bab lain dalam dokumen ini valid (misal "lihat Bab 8.2 untuk prosedur rollback database").
  - [ ] 5.6.2 — Pastikan setiap referensi ke dokumen SDLC lain menggunakan path file yang benar.

---

### TAHAP 6: Penulisan ke Target File

> **TUJUAN**: Menuangkan seluruh hasil pengerjaan ke target file yang sudah ditentukan.

- [ ] **6.1** Tulis seluruh konten dokumen Deployment Guide yang sudah disusun ke file: `docs/sdlc/06_deployment/01_deployment_guide.md`
- [ ] **6.2** Pastikan file ditulis dengan encoding **UTF-8** tanpa BOM.
- [ ] **6.3** Pastikan format markdown valid dan ter-render dengan baik (heading, tabel, code block, checklist, diagram Mermaid).
- [ ] **6.4** Pastikan baris terakhir dokumen diakhiri dengan baris kosong (*newline*) sesuai konvensi standar.

---

### TAHAP 7: Penambahan Referensi di Bagian Akhir Dokumen

> **TUJUAN**: Menambahkan keterangan referensi file yang digunakan dalam pengerjaan.

- [ ] **7.1** Di baris paling bawah dokumen (setelah Bab 16), pastikan tabel referensi dokumen **sudah lengkap** mencantumkan ke-12 file referensi beserta:
  - Path relatif file.
  - Versi dokumen.
  - Prioritas (PRIMER / SEKUNDER / TERSIER).
  - Peran/hubungan spesifik dalam penyusunan dokumen Deployment Guide ini.

---

## 6. Instruksi Tambahan (Best Practices Deployment Guide)

Berikut adalah instruksi tambahan yang **wajib** diperhatikan oleh pelaksana karena merupakan kaidah standar pembuatan deployment guide yang relevan dengan ciri khas spesifik proyek AbuCom:

### 6.1. Deployment Offline-Only (Tanpa Internet)
- [ ] Karena lingkungan produksi AbuCom berjalan 100% luring (*offline LAN*), **setiap prosedur deployment yang membutuhkan unduhan dari internet** (seperti installer Python, MySQL, pustaka pip) harus dilengkapi dengan **instruksi alternatif luring** (unduh terlebih dahulu di tempat lain, salin via USB flashdisk, instalasi via local .deb packages atau offline pip wheels).
- [ ] Tandai setiap langkah yang membutuhkan internet dengan keterangan: `> ⚠️ **[CATATAN OFFLINE-ONLY LAN]**: ...`

### 6.2. Dual-OS Deployment
- [ ] Setiap prosedur terminal yang ditulis harus memiliki **penanda OS target** di awal blok kode:
  - Untuk server: `# [LINUX DEBIAN 12 — Server]`
  - Untuk klien kasir: `# [WINDOWS 11 — Klien]`
- [ ] Pastikan setiap prosedur yang berbeda antar OS ditulis secara terpisah untuk masing-masing OS.

### 6.3. Idempotency (Dapat Diulang Tanpa Efek Samping)
- [ ] Setiap prosedur deployment yang ditulis harus bersifat **idempotent** — artinya jika prosedur dijalankan ulang setelah gagal atau terputus, tidak boleh menyebabkan kerusakan data atau konfigurasi ganda. Jika ada langkah yang tidak idempotent (misal CREATE DATABASE), sertakan instruksi pengecekan awal (`IF NOT EXISTS`).

### 6.4. Versioning dan Tagging Rilis
- [ ] Dokumen harus menyertakan prosedur **pembuatan tag rilis** pada repositori Git sebelum deployment produksi (misal `git tag -a v1.0.0 -m "Release v1.0.0 - Production Deployment"`).
- [ ] Setiap deployment harus tercatat versinya untuk keperluan rollback.

### 6.5. Checklist Format Standar
- [ ] Seluruh checklist dalam dokumen wajib menggunakan **format checkbox markdown** `- [ ]` agar pelaksana bisa mencentang progres secara manual saat eksekusi deployment.

### 6.6. Estimasi Waktu per Prosedur
- [ ] Untuk setiap bab prosedur utama (Bab 4 s.d Bab 6), sertakan **estimasi waktu pengerjaan** agar pelaksana bisa merencanakan jadwal deployment (misal: "Estimasi waktu: ±2 jam").

### 6.7. Prosedur Verifikasi Wajib
- [ ] Setiap langkah konfigurasi yang ditulis **HARUS** diikuti oleh langkah **verifikasi** yang menjelaskan:
  - Perintah verifikasi yang harus dijalankan.
  - Output yang diharapkan (*expected result*).
  - Tindakan jika verifikasi gagal (*fallback action*).

### 6.8. Kontak Darurat dan Eskalasi
- [ ] Dokumen harus menyertakan bagian **kontak darurat** yang mencantumkan siapa yang harus dihubungi jika terjadi masalah kritis saat deployment (meskipun berupa placeholder `[HARUS DIISI MANUAL]`).

---

## 7. Ringkasan Tugas

| No | Tahapan | Jumlah Checklist | Estimasi Effort |
|:---:|---|:---:|---|
| 1 | Pembacaan dan Perangkuman File Referensi | 70+ item | Tinggi — baca 12 file referensi |
| 2 | Penyusunan Dokumen (16 Bab Utama) | 19 item | Sangat Tinggi — tulis 15+ bab substansif |
| 3 | Penandaan Data Kosong | 2 item | Rendah |
| 4 | Penyaringan Konten | 11 item | Sedang |
| 5 | Pengecekan Kualitas | 15+ item | Sedang |
| 6 | Penulisan ke Target File | 4 item | Rendah |
| 7 | Penambahan Referensi | 1 item | Rendah |
| **Total** | **7 Tahapan** | **120+ item checklist** | **Tinggi** |

---

## 8. Kriteria Selesai (Definition of Done)

Issue ini dianggap **SELESAI** jika dan hanya jika seluruh kondisi berikut terpenuhi:

1. [x] File `docs/sdlc/06_deployment/01_deployment_guide.md` telah dibuat dan terisi konten substansif.
2. [ ] Dokumen memiliki minimal **16 bab utama** sesuai kerangka di Bab 4.
3. [ ] Dokumen memiliki minimal **3 diagram Mermaid** yang valid.
4. [ ] Dokumen memiliki minimal **8 tabel** yang informatif.
5. [ ] Seluruh prosedur teknis memiliki perintah terminal yang **siap di-copy-paste**.
6. [ ] Seluruh data yang tidak tersedia ditandai dengan `⚠️ [HARUS DIISI MANUAL]`.
7. [ ] Dokumen ditulis dalam bahasa Indonesia yang natural dan mudah dipahami.
8. [ ] Bab Referensi Dokumen (Bab 16) mencantumkan seluruh 12 file referensi.
9. [ ] Seluruh checklist dalam issue ini tercentang `[x]`.

---