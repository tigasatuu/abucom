# Pembuatan Dokumen Environment Setup

---

| Atribut          | Detail                                                                     |
| :--------------- | :------------------------------------------------------------------------- |
| **Judul**        | Pembuatan dan Penyusunan Dokumen Environment Setup                         |
| **Dokumen Utama**| Environment Setup                                                          |
| **Target File**  | `docs/sdlc/04_implementation/02_environment_setup.md`                      |
| **Fase SDLC**    | Fase 04 — Implementation (Konstruksi)                                      |
| **Prioritas**    | Tinggi — Prasyarat mutlak sebelum pengkodean modul dimulai                 |
| **Status**       | 🟡 Open — Menunggu Eksekusi                                                |
| **Tanggal Buat** | 2026-05-26                                                                 |

---

## 1. Deskripsi Issue

Issue ini menginstruksikan pembuatan dan penyusunan dokumen **Environment Setup** secara lengkap, detail, dan komprehensif. Dokumen ini merupakan deliverable kedua pada **Fase 04 — Implementation** dalam siklus SDLC proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**.

Dokumen Environment Setup berfungsi sebagai **panduan teknis langkah demi langkah** yang mendokumentasikan seluruh prosedur instalasi, konfigurasi, dan persiapan lingkungan pengembangan (*development environment*) serta lingkungan produksi (*production environment*) agar tim pengembang (Junior Programmer dan model AI) dapat segera memulai proses penulisan kode program setelah membaca dokumen ini.

**Mengapa dokumen ini penting?**
- Tanpa panduan setup yang jelas, Junior Programmer akan kesulitan menyiapkan mesin kerja secara konsisten.
- Dokumen ini menjamin **reprodusibilitas** lingkungan di semua node (Server Debian & Klien Windows).
- Menjadi acuan bagi dokumen fase SDLC selanjutnya (coding, testing, deployment).

---

## 2. Persona Pelaksana

| Atribut            | Detail                                                              |
| :----------------- | :------------------------------------------------------------------ |
| **Persona**        | **Senior DevOps Engineer & Infrastructure Setup Specialist**        |
| **Justifikasi**    | Persona ini memiliki otoritas dan keahlian paling relevan untuk menyusun dokumen panduan instalasi runtime, konfigurasi database server, setup jaringan LAN, manajemen dependensi, konfigurasi keamanan OS, dan prosedur verifikasi lingkungan lintas platform (Dual-OS). Persona ini memahami interaksi antara komponen infrastruktur fisik (hardware, jaringan) dengan komponen perangkat lunak (Python, MySQL, library) secara menyeluruh. |

---

## 3. File Referensi yang Digunakan

Berikut adalah file referensi yang **wajib dibaca** secara lengkap sebelum memulai penyusunan dokumen utama, diurutkan berdasarkan prioritas relevansi:

| No | Prioritas     | Nama File Referensi           | Path Relatif                                           | Alasan Pemilihan                                                                                                     |
| :-: | :-----------: | :---------------------------- | :----------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| 1  | **PRIMER**    | Tech Stack Decision           | `docs/sdlc/01_planning/04_tech_stack_decision.md`       | SSoT (Single Source of Truth) untuk semua keputusan teknologi: Python 3.14.2+, MySQL LTS, dual-OS, pustaka wajib & versi terkunci, requirements.txt, schema.sql & seed.sql, serta spesifikasi hardware. |
| 2  | **PRIMER**    | System Architecture           | `docs/sdlc/03_design/03_system_architecture.md`         | Blueprint arsitektur fisik (topologi LAN, spesifikasi hardware server & klien, konfigurasi IP statis, bind-address MySQL, firewall ufw), konfigurasi OS dual-OS, dan strategi portabilitas. |
| 3  | **PRIMER**    | Security Design               | `docs/sdlc/03_design/06_security_design.md`             | Spesifikasi konfigurasi keamanan: .env variables (JWT secret, Fernet key, DB credentials), chmod 700 backup dir, ufw firewall rules, MySQL user privilege minimization (`abucom_app`), dan OS hardening. |
| 4  | **PRIMER**    | Coding Standard               | `docs/sdlc/04_implementation/01_coding_standard.md`     | Struktur direktori proyek standar, requirements.txt dengan versi terkunci, .env.example template, .gitignore rules, konvensi connection pooling, dan konfigurasi runtime. |
| 5  | **SEKUNDER**  | Database Schema               | `docs/sdlc/03_design/01_database_schema.sql`            | File DDL SQL fisik yang harus dieksekusi saat setup database (CREATE DATABASE, CREATE TABLE, indexes, triggers). |
| 6  | **SEKUNDER**  | Software Requirements Spec    | `docs/sdlc/02_analysis/02_software_requirements.md`     | Spesifikasi kebutuhan non-fungsional terkait performa, kompatibilitas OS, dan parameterisasi runtime. |
| 7  | **TERSIER**   | Narasi Pemilik                | `docs/sdlc/narasi.txt`                                  | Konteks bisnis dasar: spesifikasi sistem (Python 3.14.2+, library utama, OS target), dan susunan tim pengembang AI. |

> **Catatan**: File `narasi.txt` masih dibutuhkan sebagai referensi tersier untuk memvalidasi konteks spesifikasi teknis mandatori yang berasal langsung dari permintaan pemilik usaha.

---

## 4. Kerangka Struktur Dokumen Utama

Berikut adalah kerangka (*outline*) lengkap dokumen **Environment Setup** yang harus disusun. Kerangka ini mengikuti standar praktik industri (*Industry Best Practice*) untuk dokumen panduan setup lingkungan pengembangan perangkat lunak:

```
---
dokumen    : Environment Setup
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [TANGGAL PEMBUATAN]
status     : Draft
penyusun   : Senior DevOps Engineer & Infrastructure Setup Specialist
---

# Environment Setup — AbuCom

## Riwayat Perubahan Dokumen
(Tabel riwayat versi: Versi | Tanggal | Perubahan | Oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan
### 1.7. Prasyarat Pengetahuan (Prerequisites)

---

## 2. Ringkasan Arsitektur Lingkungan
### 2.1. Diagram Topologi Lingkungan (Mermaid)
### 2.2. Matriks Node dan Komponen
### 2.3. Perbedaan Lingkungan Development vs Production

---

## 3. Spesifikasi Hardware dan Infrastruktur Jaringan
### 3.1. Spesifikasi Node Server Database (Mini PC — Linux Debian 12)
### 3.2. Spesifikasi Node Klien Kasir (PC Desktop — Windows 11)
### 3.3. Perangkat Jaringan (Switch, Router, Kabel)
### 3.4. Perangkat Pendukung (UPS, Printer Thermal)
### 3.5. Checklist Verifikasi Hardware

---

## 4. Setup Sistem Operasi — Server Linux Debian 12 Bookworm
### 4.1. Instalasi Minimal Linux Debian 12
### 4.2. Konfigurasi Jaringan (IP Statis Server)
### 4.3. Hardening Keamanan OS Server
#### 4.3.1. Konfigurasi Firewall (ufw)
#### 4.3.2. Konfigurasi SSH Aman
#### 4.3.3. Pembatasan Hak Akses Direktori
### 4.4. Instalasi Python 3.14.2+ di Linux Debian 12
### 4.5. Verifikasi Instalasi Python di Server

---

## 5. Setup Sistem Operasi — Klien Windows 11
### 5.1. Konfigurasi Dasar Windows 11
### 5.2. Instalasi Python 3.14.2+ di Windows 11
### 5.3. Konfigurasi PATH Environment Variable
### 5.4. Konfigurasi Windows Terminal (UTF-8 / chcp 65001)
### 5.5. Konfigurasi Keamanan Klien (Akun Terbatas, Disable USB Autorun)
### 5.6. Verifikasi Instalasi Python di Windows

---

## 6. Setup Database MySQL Server
### 6.1. Instalasi MySQL Community Server (LTS) di Linux Debian 12
### 6.2. Konfigurasi Keamanan MySQL (mysql_secure_installation)
### 6.3. Konfigurasi Bind Address untuk Akses LAN
### 6.4. Konfigurasi Character Set dan Collation (utf8mb4)
### 6.5. Konfigurasi Transaction Isolation Level (REPEATABLE READ)
### 6.6. Pembuatan Database dan Akun Aplikasi (abucom_app)
#### 6.6.1. Pembuatan Database Utama (abucom_db)
#### 6.6.2. Pembuatan Database Testing (abucom_test_db)
#### 6.6.3. Pembuatan Akun MySQL Aplikasi dengan Privilege Terbatas
### 6.7. Eksekusi Schema SQL (schema.sql)
### 6.8. Eksekusi Seed Data (seed.sql)
### 6.9. Verifikasi Konektivitas MySQL dari Klien Windows (Remote Test)

---

## 7. Setup Lingkungan Python dan Dependensi
### 7.1. Pembuatan Virtual Environment (venv)
### 7.2. Instalasi Dependensi dari requirements.txt
### 7.3. Daftar Lengkap Dependensi dan Versi Terkunci
#### 7.3.1. Dependensi Wajib (Mandatory)
#### 7.3.2. Dependensi Rekomendasi
#### 7.3.3. Dependensi Pengembangan (Development Only)
### 7.4. Verifikasi Instalasi Seluruh Dependensi
### 7.5. Troubleshooting Instalasi Dependensi Umum

---

## 8. Konfigurasi Proyek Aplikasi
### 8.1. Struktur Direktori Proyek Standar
### 8.2. Pembuatan File .env (Konfigurasi Kredensial Rahasia)
#### 8.2.1. Template .env.example Lengkap
#### 8.2.2. Panduan Pengisian Setiap Variabel .env
#### 8.2.3. Generasi Secret Key JWT (32+ Karakter Hex)
#### 8.2.4. Generasi Fernet Key (UU PDP Compliance)
### 8.3. Konfigurasi File .gitignore
### 8.4. Konfigurasi File requirements.txt
### 8.5. Verifikasi Startup Aplikasi CLI (Smoke Test)

---

## 9. Setup Version Control (Git)
### 9.1. Instalasi Git
### 9.2. Konfigurasi Git Identity
### 9.3. Inisialisasi Repository
### 9.4. Strategi Branching (Feature Branching)
### 9.5. Konvensi Commit Message

---

## 10. Setup Perangkat Keras Pendukung
### 10.1. Konfigurasi Printer Thermal (Port Serial/USB)
### 10.2. Konfigurasi UPS (Graceful Shutdown)
### 10.3. Konfigurasi Router MikroTik (DHCP & IP Statis)

---

## 11. Setup Lingkungan Testing
### 11.1. Konfigurasi Database Testing (abucom_test_db)
### 11.2. Instalasi Framework Testing (unittest / pytest)
### 11.3. Konfigurasi .env.test (Variabel Testing)
### 11.4. Verifikasi Eksekusi Test Suite

---

## 12. Setup Backup dan Recovery
### 12.1. Konfigurasi Direktori Backup Server (/var/lib/mysql-backups/)
### 12.2. Konfigurasi Enkripsi Backup AES-256
### 12.3. Verifikasi Prosedur Backup Manual
### 12.4. Verifikasi Prosedur Restore Manual

---

## 13. Checklist Verifikasi Akhir Lingkungan
### 13.1. Checklist Server Linux Debian 12
### 13.2. Checklist Klien Windows 11
### 13.3. Checklist Konektivitas Jaringan LAN
### 13.4. Checklist Keamanan
### 13.5. Checklist Kesiapan Development

---

## 14. Troubleshooting Umum
### 14.1. Masalah Koneksi Database dari Klien
### 14.2. Masalah Rendering ANSI di Terminal Windows
### 14.3. Masalah Encoding UTF-8 Lintas OS
### 14.4. Masalah Instalasi Dependensi Python
### 14.5. Masalah Printer Thermal

---

## 15. Lampiran
### 15.1. Template Lengkap File .env.example
### 15.2. Template Lengkap File .gitignore
### 15.3. Template Lengkap File requirements.txt
### 15.4. Skrip Otomasi Setup (Opsional)
### 15.5. Daftar Port Jaringan yang Digunakan

---

## 16. Referensi Dokumen
(Tabel referensi: No | Nama Dokumen | Path Relatif | Versi | Prioritas | Peran)
```

---

## 5. Instruksi Penyusunan Dokumen

### 5.1. Instruksi Umum

1. **Rangkum semua data dan informasi** dari setiap file referensi yang tercantum di Bagian 3. Pastikan setiap detail teknis (versi software, nomor port, IP address, nama variabel, perintah terminal, konfigurasi file) dari file referensi tidak ada yang terlewat.

2. **Hanya ambil data yang relevan** dengan dokumen Environment Setup. Informasi yang berkaitan dengan logika bisnis, alur kerja operasional, desain UI CLI, atau kalkulasi keuangan **tidak perlu** dimasukkan ke dokumen ini. Fokuskan hanya pada:
   - Spesifikasi hardware dan jaringan
   - Instalasi dan konfigurasi software (OS, Python, MySQL, library)
   - Konfigurasi keamanan infrastruktur (firewall, hak akses, kredensial)
   - Setup proyek (direktori, .env, .gitignore, requirements.txt)
   - Setup version control (Git)
   - Setup testing environment
   - Setup backup/recovery
   - Verifikasi dan troubleshooting

3. **Pastikan dokumen ini self-contained** — layak dijadikan sebagai referensi, acuan, dan input utama bagi dokumen dan aktivitas pada fase SDLC selanjutnya (coding, testing, deployment) tanpa perlu membuka dokumen referensi lain.

4. **Gunakan bahasa Indonesia** yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh Junior Programmer atau model AI yang lebih murah. Hindari kalimat berbelit-belit. Gunakan kalimat pendek dan langsung.

5. **Pastikan kualitas dan kelengkapan** isi dokumen ini tidak perlu dipertanyakan atau diinterupsi. Dokumen ini harus cukup lengkap sehingga tidak menghambat proses pekerjaan fase SDLC selanjutnya.

6. **Tandai data yang kosong** — Jika ada data teknis yang tidak tersedia atau belum ada di dalam file referensi (misalnya: IP address aktual router, password MySQL root yang sebenarnya, port printer fisik yang tepat), tandai dengan format:
   ```
   > ⚠️ **[HARUS DIISI MANUAL]**: [Deskripsi data yang harus diisi dan oleh siapa]
   ```

7. **Tambahkan referensi dokumen** di bagian akhir (Bab 16) dalam format tabel yang mencantumkan semua file referensi yang digunakan dalam penyusunan dokumen ini.

8. **Tuangkan semua hasil penyusunan** ke dalam target file: `docs/sdlc/04_implementation/02_environment_setup.md`

### 5.2. Instruksi Khusus Dokumen Environment Setup

Selain instruksi umum di atas, perhatikan kaidah khusus berikut yang merupakan ciri khas dokumen Environment Setup berstandar industri:

1. **Setiap langkah instalasi harus menyertakan perintah terminal/command yang tepat** — Jangan hanya mendeskripsikan "instal Python", tetapi berikan perintah lengkap beserta opsi yang digunakan (contoh: `sudo apt install python3.14 python3.14-venv -y`).

2. **Setiap langkah konfigurasi file harus menyertakan contoh isi file yang lengkap** — Untuk file konfigurasi seperti `.env`, `.gitignore`, `requirements.txt`, `/etc/network/interfaces`, `mysqld.cnf`, sertakan contoh isi file dalam blok kode yang bisa langsung di-copy-paste.

3. **Setiap langkah harus diakhiri dengan perintah verifikasi** — Setelah setiap instalasi atau konfigurasi, berikan perintah verifikasi dan contoh output yang diharapkan (contoh: `python3.14 --version` → output: `Python 3.14.2`).

4. **Bedakan perintah untuk Linux vs Windows** — Karena proyek ini berjalan dual-OS, setiap perintah terminal harus dibedakan dengan jelas menggunakan label:
   ```bash
   # [LINUX DEBIAN 12 — Server]
   sudo apt install ...

   # [WINDOWS 11 — Klien]
   pip install ...
   ```

5. **Sertakan diagram Mermaid** untuk topologi jaringan dan arsitektur lingkungan agar memudahkan visualisasi.

6. **Sertakan checklist verifikasi akhir** dalam format checkbox markdown yang bisa dicentang oleh Junior Programmer setelah selesai melakukan setiap langkah setup.

7. **Sertakan bagian Troubleshooting** untuk masalah umum yang sering terjadi saat setup, lengkap dengan solusi langkah demi langkahnya.

8. **Konsistensi dengan Coding Standard** — Pastikan struktur direktori proyek, format .env, format .gitignore, dan isi requirements.txt yang didokumentasikan dalam Environment Setup **100% konsisten** dengan yang sudah didefinisikan di Coding Standard v1.1.

9. **Sertakan metadata header YAML** di bagian paling atas dokumen, konsisten dengan format metadata header dokumen SDLC AbuCom lainnya.

---

## 6. Tahapan Eksekusi (Step-by-Step Checklist)

Berikut adalah checklist tahapan eksekusi yang **wajib diikuti secara berurutan** oleh pelaksana (Junior Programmer atau model AI). Setiap tahapan harus diselesaikan sebelum melanjutkan ke tahapan berikutnya.

### Fase A — Persiapan dan Pembacaan Referensi

- [ ] **A.1.** Baca file `docs/sdlc/narasi.txt` secara lengkap dari baris pertama sampai terakhir. Catat informasi berikut:
  - [ ] Bahasa pemrograman dan versi wajib (Python 3.14.2+)
  - [ ] Library utama wajib (`mysql-connector-python`, `python-dotenv`, `bcrypt`, `pyjwt`)
  - [ ] Sistem operasi target (Linux Debian 12 Bookworm dan Windows 11)
  - [ ] Susunan tim pengembang (6 model AI + 1 Junior Programmer)

- [ ] **A.2.** Baca file `docs/sdlc/01_planning/04_tech_stack_decision.md` secara lengkap dari baris pertama sampai terakhir. Catat informasi berikut:
  - [ ] Versi Python spesifik yang diwajibkan
  - [ ] Paradigma FP murni (konteks: tidak ada class di alur bisnis)
  - [ ] MySQL Community Server versi LTS yang direkomendasikan (8.0/8.4)
  - [ ] Daftar lengkap dependensi wajib beserta versi terkunci (Tabel Bab 5.7)
  - [ ] Daftar dependensi rekomendasi (`rich`, `tabulate`) beserta versi
  - [ ] Daftar pustaka standard library Python yang dimanfaatkan (Bab 5.5)
  - [ ] Spesifikasi hardware server dan klien (Bab 6.2)
  - [ ] Arsitektur Client-Server LAN dan topologi jaringan (Bab 6.2)
  - [ ] Strategi requirements.txt dan format deklarasi (Bab 9.4)
  - [ ] Strategi inisialisasi database: schema.sql dan seed.sql (Bab 9.5)
  - [ ] Konfigurasi MySQL: character set utf8mb4, collation, InnoDB, REPEATABLE READ (Bab 4.1)
  - [ ] Strategi portabilitas kode lintas OS (Bab 6.1)
  - [ ] Alat pengembangan dan version control Git (Bab 9.1)

- [ ] **A.3.** Baca file `docs/sdlc/03_design/03_system_architecture.md` secara lengkap dari baris pertama sampai terakhir. Catat informasi berikut:
  - [ ] Diagram topologi jaringan LAN (Bab 3.1) — salin atau adaptasi diagram Mermaid
  - [ ] Spesifikasi hardware server node (Bab 3.2.1): prosesor, RAM, SSD, jaringan
  - [ ] Spesifikasi hardware klien node (Bab 3.2.2): prosesor, RAM, SSD
  - [ ] Spesifikasi perangkat jaringan: switch, router MikroTik, kabel (Bab 3.2.3)
  - [ ] Spesifikasi perangkat pendukung: UPS, printer thermal (Bab 3.2.4)
  - [ ] Konfigurasi server Linux Debian 12 (Bab 3.3.1):
    - [ ] Service daemon MySQL (`mysql.service`)
    - [ ] Konfigurasi IP statis server (`/etc/network/interfaces`) — catat IP: `192.168.1.200`
    - [ ] MySQL bind address (`/etc/mysql/mysql.conf.d/mysqld.cnf`) — `bind-address = 192.168.1.200`
    - [ ] Firewall ufw — `ufw allow from 192.168.1.0/24 to any port 3306 proto tcp`
    - [ ] Hak akses folder backup — `chmod 700`
  - [ ] Konfigurasi klien Windows 11 (Bab 3.3.2):
    - [ ] Python 3.14.2+ terinstal dan terdaftar di PATH
    - [ ] Windows Terminal modern dengan UTF-8 (`chcp 65001`)
    - [ ] Driver printer thermal generic text-only — variabel `PRINTER_PORT` di `.env`
  - [ ] Strategi portabilitas lintas OS (Bab 3.4): pathlib, encoding UTF-8, platform.system()
  - [ ] Struktur layout direktori proyek standar (Bab 4 di Coding Standard)
  - [ ] Strategi koneksi database: connection pooling (pool_size=5), retry mechanism (Bab 6.2)
  - [ ] Strategi migrasi data awal: schema.sql, seed.sql, CSV import (Bab 6.6)

- [ ] **A.4.** Baca file `docs/sdlc/03_design/06_security_design.md` secara lengkap dari baris pertama sampai terakhir. Catat informasi berikut:
  - [ ] Variabel .env yang dibutuhkan:
    - [ ] Kredensial database MySQL (host, port, user, password, database name)
    - [ ] JWT secret key (minimum 32 karakter hex)
    - [ ] Fernet key untuk enkripsi UU PDP
    - [ ] Password enkripsi backup AES-256 (`BACKUP_ZIP_PASSWORD`)
    - [ ] Port printer thermal (`PRINTER_PORT`)
  - [ ] MySQL user privilege minimization: akun `abucom_app` (Bab 3.4)
    - [ ] Privilege yang diizinkan: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
    - [ ] Privilege yang dilarang: `DROP`, `ALTER`, `CREATE`, `GRANT`
  - [ ] OS hardening server Debian (Bab 3.3):
    - [ ] chmod 700 pada direktori backup
    - [ ] Disable SSH root login (`PermitRootLogin no`)
    - [ ] MySQL bind-address ke IP statis lokal
  - [ ] OS hardening klien Windows (Bab 3.3):
    - [ ] Akun Windows non-administrator terbatas
    - [ ] Disable USB autorun
  - [ ] Startup validator: pengecekan keberadaan .env dan kelengkapan variabel (Bab 6.5)

- [ ] **A.5.** Baca file `docs/sdlc/04_implementation/01_coding_standard.md` secara lengkap dari baris pertama sampai terakhir. Catat informasi berikut:
  - [ ] Layout direktori standar proyek AbuCom lengkap (Bab 4.1) — salin tree structure
  - [ ] Daftar dependensi wajib dengan versi terkunci (Bab 13.2)
  - [ ] Daftar dependensi rekomendasi (Bab 13.3)
  - [ ] Daftar pustaka standard library (Bab 13.4)
  - [ ] Aturan .gitignore (Bab 15.4): `.env`, `__pycache__/`, `*.pyc`, `.pytest_cache/`, `exports/backups/`, `exports/receipts/`
  - [ ] Aturan penambahan dependensi baru (Bab 13.5)
  - [ ] Connection pooling initialization (Bab 8.9): `pool_name="abupool"`, `pool_size=5`
  - [ ] Konfigurasi database testing: `abucom_test_db` (Bab 14.5)
  - [ ] Dependensi keamanan tambahan: `cryptography==42.0.5` (Bab 13.2)

- [ ] **A.6.** Baca file `docs/sdlc/03_design/01_database_schema.sql` secara lengkap. Catat informasi berikut:
  - [ ] Nama database yang harus dibuat
  - [ ] Jumlah tabel (28 tabel)
  - [ ] Konfigurasi ENGINE=InnoDB pada semua tabel
  - [ ] Konfigurasi CHARACTER SET dan COLLATION
  - [ ] Perintah CREATE DATABASE yang digunakan

- [ ] **A.7.** Baca file `docs/sdlc/02_analysis/02_software_requirements.md` secara sekilas (scan). Catat informasi berikut jika ada:
  - [ ] Kebutuhan non-fungsional terkait performa dan kompatibilitas OS
  - [ ] Parameterisasi runtime system_configs

### Fase B — Perangkuman dan Penyaringan Data

- [ ] **B.1.** Kompilasi semua catatan dari Fase A ke dalam satu rangkuman internal.
- [ ] **B.2.** Saring dan kelompokkan data berdasarkan bab-bab kerangka dokumen (Bagian 4 issue ini):
  - [ ] Data yang masuk ke Bab 2 (Ringkasan Arsitektur Lingkungan)
  - [ ] Data yang masuk ke Bab 3 (Spesifikasi Hardware & Jaringan)
  - [ ] Data yang masuk ke Bab 4 (Setup Server Linux Debian 12)
  - [ ] Data yang masuk ke Bab 5 (Setup Klien Windows 11)
  - [ ] Data yang masuk ke Bab 6 (Setup Database MySQL)
  - [ ] Data yang masuk ke Bab 7 (Setup Python & Dependensi)
  - [ ] Data yang masuk ke Bab 8 (Konfigurasi Proyek Aplikasi)
  - [ ] Data yang masuk ke Bab 9 (Setup Version Control Git)
  - [ ] Data yang masuk ke Bab 10 (Setup Perangkat Keras Pendukung)
  - [ ] Data yang masuk ke Bab 11 (Setup Lingkungan Testing)
  - [ ] Data yang masuk ke Bab 12 (Setup Backup & Recovery)
  - [ ] Data yang masuk ke Bab 13 (Checklist Verifikasi Akhir)
  - [ ] Data yang masuk ke Bab 14 (Troubleshooting)
  - [ ] Data yang masuk ke Bab 15 (Lampiran)
- [ ] **B.3.** Identifikasi dan tandai data yang **tidak tersedia** di file referensi (untuk diberi tag `[HARUS DIISI MANUAL]`).
- [ ] **B.4.** Pastikan **tidak ada data logika bisnis** (HPP, BOM, payroll, antrian, CRM) yang masuk ke dalam dokumen ini. Jika ada, buang.

### Fase C — Penyusunan Dokumen

- [ ] **C.1.** Buat file target `docs/sdlc/04_implementation/02_environment_setup.md`.
- [ ] **C.2.** Tulis metadata header YAML di bagian paling atas file:
  ```yaml
  ---
  dokumen    : Environment Setup
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [TANGGAL HARI INI]
  status     : Draft
  penyusun   : Senior DevOps Engineer & Infrastructure Setup Specialist
  ---
  ```
- [ ] **C.3.** Tulis Riwayat Perubahan Dokumen (tabel versi awal v1.0).
- [ ] **C.4.** Tulis Bab 1 — Informasi Dokumen:
  - [ ] 1.1. Tujuan Dokumen: jelaskan bahwa dokumen ini adalah panduan teknis langkah-demi-langkah untuk setup lingkungan
  - [ ] 1.2. Cakupan: list cakupan setup yang dibahas
  - [ ] 1.3. Posisi Dokumen dalam SDLC: sertakan diagram ASCII posisi deliverable
  - [ ] 1.4. Hubungan dengan Dokumen Lainnya: list dokumen input dan output
  - [ ] 1.5. Audiens Target: Junior Programmer, Tim AI, System Administrator
  - [ ] 1.6. Definisi, Akronim: sesuaikan dengan akronim yang digunakan
  - [ ] 1.7. Prasyarat Pengetahuan: list pengetahuan dasar yang harus dimiliki pembaca
- [ ] **C.5.** Tulis Bab 2 — Ringkasan Arsitektur Lingkungan:
  - [ ] Sertakan diagram Mermaid topologi lingkungan (adaptasi dari System Architecture Bab 3.1)
  - [ ] Buat tabel matriks node dan komponen
  - [ ] Jelaskan perbedaan development vs production
- [ ] **C.6.** Tulis Bab 3 — Spesifikasi Hardware dan Infrastruktur Jaringan:
  - [ ] Salin dan format ulang spesifikasi dari System Architecture Bab 3.2
  - [ ] Sertakan checklist verifikasi hardware dalam format checkbox
- [ ] **C.7.** Tulis Bab 4 — Setup Sistem Operasi Server Linux Debian 12:
  - [ ] Setiap langkah harus menyertakan perintah terminal yang bisa di-copy-paste
  - [ ] Sertakan perintah verifikasi dan contoh output yang diharapkan
  - [ ] Sertakan konfigurasi IP statis dari System Architecture Bab 3.3.1
  - [ ] Sertakan konfigurasi firewall ufw
  - [ ] Sertakan konfigurasi SSH aman dari Security Design Bab 3.3
  - [ ] Sertakan langkah instalasi Python 3.14.2+ di Debian
- [ ] **C.8.** Tulis Bab 5 — Setup Sistem Operasi Klien Windows 11:
  - [ ] Langkah instalasi Python 3.14.2+ di Windows 11 (installer, PATH)
  - [ ] Konfigurasi Windows Terminal dan UTF-8
  - [ ] Konfigurasi keamanan klien (akun terbatas, disable USB autorun) dari Security Design
- [ ] **C.9.** Tulis Bab 6 — Setup Database MySQL Server:
  - [ ] Langkah instalasi MySQL di Debian 12
  - [ ] Langkah mysql_secure_installation
  - [ ] Konfigurasi bind-address, character set, collation, isolation level
  - [ ] Perintah SQL pembuatan database `abucom_db` dan `abucom_test_db`
  - [ ] Perintah SQL pembuatan user `abucom_app` dengan privilege terbatas dari Security Design Bab 3.4
  - [ ] Instruksi eksekusi file `schema.sql` dan `seed.sql`
  - [ ] Langkah verifikasi koneksi remote dari klien Windows
- [ ] **C.10.** Tulis Bab 7 — Setup Lingkungan Python dan Dependensi:
  - [ ] Perintah pembuatan virtual environment (venv) untuk Linux dan Windows
  - [ ] Perintah instalasi dari requirements.txt
  - [ ] Tabel daftar lengkap dependensi dari Coding Standard Bab 13
  - [ ] Perintah verifikasi instalasi setiap library
  - [ ] Troubleshooting instalasi umum (misal: build error bcrypt di Windows)
- [ ] **C.11.** Tulis Bab 8 — Konfigurasi Proyek Aplikasi:
  - [ ] Salin dan format ulang struktur direktori dari Coding Standard Bab 4.1
  - [ ] Sertakan template .env.example lengkap dengan komentar penjelasan setiap variabel
  - [ ] Sertakan panduan generasi JWT secret key dan Fernet key
  - [ ] Sertakan template .gitignore lengkap dari Coding Standard Bab 15.4
  - [ ] Sertakan template requirements.txt lengkap
  - [ ] Sertakan langkah smoke test startup aplikasi
- [ ] **C.12.** Tulis Bab 9 — Setup Version Control Git:
  - [ ] Perintah instalasi dan konfigurasi Git
  - [ ] Strategi branching sesuai Coding Standard Bab 15
  - [ ] Konvensi commit message
- [ ] **C.13.** Tulis Bab 10 — Setup Perangkat Keras Pendukung:
  - [ ] Konfigurasi printer thermal (COM1/USB) dari System Architecture Bab 3.3.2
  - [ ] Konfigurasi UPS
  - [ ] Konfigurasi router MikroTik
  - [ ] Tandai data yang harus diisi manual dengan tag `[HARUS DIISI MANUAL]`
- [ ] **C.14.** Tulis Bab 11 — Setup Lingkungan Testing:
  - [ ] Konfigurasi database testing dari Coding Standard Bab 14.5
  - [ ] Setup framework testing
  - [ ] Konfigurasi .env.test
- [ ] **C.15.** Tulis Bab 12 — Setup Backup dan Recovery:
  - [ ] Konfigurasi direktori backup dari Security Design Bab 8.2
  - [ ] Konfigurasi enkripsi backup AES-256
  - [ ] Prosedur verifikasi backup dan restore
- [ ] **C.16.** Tulis Bab 13 — Checklist Verifikasi Akhir:
  - [ ] Buat checklist dalam format `- [ ]` untuk setiap komponen:
    - [ ] Checklist Server Linux Debian 12 (minimal 10 item)
    - [ ] Checklist Klien Windows 11 (minimal 8 item)
    - [ ] Checklist Konektivitas Jaringan LAN (minimal 5 item)
    - [ ] Checklist Keamanan (minimal 8 item)
    - [ ] Checklist Kesiapan Development (minimal 5 item)
- [ ] **C.17.** Tulis Bab 14 — Troubleshooting Umum:
  - [ ] Masalah koneksi database dari klien (Error 2003, 2006, 2013)
  - [ ] Masalah rendering ANSI di terminal Windows
  - [ ] Masalah encoding UTF-8 lintas OS
  - [ ] Masalah instalasi dependensi Python (bcrypt build, cryptography)
  - [ ] Masalah printer thermal
- [ ] **C.18.** Tulis Bab 15 — Lampiran:
  - [ ] Template .env.example lengkap (copy-paste ready)
  - [ ] Template .gitignore lengkap (copy-paste ready)
  - [ ] Template requirements.txt lengkap (copy-paste ready)
  - [ ] Daftar port jaringan yang digunakan (Port 3306 MySQL, dll)
- [ ] **C.19.** Tulis Bab 16 — Referensi Dokumen:
  - [ ] Buat tabel referensi dengan kolom: No | Nama Dokumen Referensi | Path Relatif File | Versi | Prioritas | Peran dalam Penyusunan
  - [ ] Masukkan semua 7 file referensi dari Bagian 3 issue ini

### Fase D — Validasi dan Finalisasi

- [ ] **D.1.** Validasi konsistensi data:
  - [ ] Versi Python di dokumen ini = `3.14.2+` (konsisten dengan narasi.txt, Tech Stack, Coding Standard)
  - [ ] Versi MySQL di dokumen ini = `8.0/8.4 LTS` (konsisten dengan Tech Stack Decision)
  - [ ] Daftar dependensi dan versi di dokumen ini konsisten 100% dengan Coding Standard Bab 13
  - [ ] Struktur direktori proyek di dokumen ini konsisten 100% dengan Coding Standard Bab 4.1
  - [ ] Isi .gitignore di dokumen ini konsisten 100% dengan Coding Standard Bab 15.4
  - [ ] IP statis server di dokumen ini = `192.168.1.200` (konsisten dengan System Architecture Bab 3.3.1)
  - [ ] Konfigurasi keamanan di dokumen ini konsisten dengan Security Design
- [ ] **D.2.** Validasi bahwa **semua perintah terminal** yang ditulis memiliki format yang benar dan bisa di-copy-paste langsung.
- [ ] **D.3.** Validasi bahwa **semua file template** (.env.example, .gitignore, requirements.txt) yang dicantumkan di Lampiran isinya lengkap dan bisa langsung digunakan.
- [ ] **D.4.** Validasi bahwa **setiap langkah instalasi** diakhiri dengan perintah verifikasi dan contoh output yang diharapkan.
- [ ] **D.5.** Validasi bahwa **semua data kosong** yang belum tersedia di file referensi sudah ditandai dengan `> ⚠️ **[HARUS DIISI MANUAL]**`.
- [ ] **D.6.** Validasi bahwa **tidak ada data logika bisnis** (HPP, BOM, payroll, CRM) yang masuk ke dokumen ini.
- [ ] **D.7.** Validasi bahwa **bahasa Indonesia** yang digunakan natural, tidak ambigu, dan mudah dipahami.
- [ ] **D.8.** Validasi bahwa **Bab 16 (Referensi Dokumen)** sudah terisi lengkap dengan semua file referensi.
- [ ] **D.9.** Simpan file final ke path: `docs/sdlc/04_implementation/02_environment_setup.md`
- [ ] **D.10.** Verifikasi file sudah tersimpan dengan benar dan bisa dibuka tanpa error.

---

## 7. Kriteria Selesai (Definition of Done)

Issue ini dianggap selesai jika **semua** kriteria berikut terpenuhi:

- [ ] File `docs/sdlc/04_implementation/02_environment_setup.md` sudah terisi dengan konten lengkap.
- [ ] Seluruh 16 bab sesuai kerangka di Bagian 4 sudah ditulis.
- [ ] Metadata header YAML sudah ada di baris paling atas.
- [ ] Tabel Riwayat Perubahan Dokumen sudah ada.
- [ ] Minimal 1 diagram Mermaid (topologi lingkungan) sudah disertakan.
- [ ] Template .env.example, .gitignore, dan requirements.txt sudah lengkap dan copy-paste ready di Lampiran.
- [ ] Semua data kosong sudah ditandai `[HARUS DIISI MANUAL]`.
- [ ] Tabel referensi dokumen (Bab 16) sudah terisi lengkap.
- [ ] Tidak ada informasi logika bisnis yang masuk ke dokumen ini.
- [ ] Bahasa Indonesia yang digunakan natural dan tidak ambigu.
- [ ] Seluruh checklist Fase A sampai Fase D sudah tercentang `[x]`.

---

## 8. Catatan Tambahan

1. **Jangan berasumsi atau mengarang data** — Semua informasi teknis (versi, port, IP, konfigurasi) harus bersumber dari file referensi. Jika tidak ada, tandai sebagai `[HARUS DIISI MANUAL]`.

2. **Jangan menyederhanakan berlebihan** — Dokumen ini harus cukup detail sehingga seseorang yang baru pertama kali menyiapkan lingkungan AbuCom bisa mengikutinya dari awal sampai akhir tanpa bertanya.

3. **Prioritaskan kejelasan** — Lebih baik menjelaskan sesuatu secara berulang daripada membiarkannya ambigu.

4. **Perhatikan keamanan** — Jangan pernah menuliskan password atau secret key yang sebenarnya di dalam dokumen. Gunakan placeholder yang jelas (contoh: `YOUR_MYSQL_ROOT_PASSWORD_HERE`).

5. **Pustaka `cryptography==42.0.5`** — Library ini ditemukan di Coding Standard sebagai dependensi tambahan wajib untuk enkripsi Fernet (UU PDP compliance). Pastikan library ini masuk ke dalam daftar dependensi dan requirements.txt di dokumen Environment Setup.

---

*Issue ini dibuat pada 2026-05-26 sebagai panduan perencanaan low-level untuk penyusunan dokumen Environment Setup proyek AbuCom.*
