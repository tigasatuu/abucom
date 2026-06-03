---
judul      : Feature Inisialisasi Skema Database Multi-Cabang
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
prioritas  : 🔴 CRITICAL (Blocker — Prasyarat Mutlak Sebelum Pengkodean Modul Fungsional)
status     : Open
assignee   : Claude Sonnet 4.6 (Thinking) — STK-004 (Deep Coding & Refactoring)
reviewer   : Gemini 3 Flash — STK-011 (Automated Reviewer & Debugger)
approver   : Junior Programmer — STK-000 (Owner & Release Manager)
tanggal    : 2026-06-03
estimasi   : 3-4 jam kerja fokus
branch     : `feat/init-database-schema`
---

# Issue — Feature Inisialisasi Skema Database Multi-Cabang

## 1. Ringkasan Issue

Issue ini bertujuan untuk mengimplementasikan **fitur inisialisasi skema database multi-cabang** pada sistem AbuCom CLI. Implementasi mencakup: pembuatan modul Python fungsional yang mampu menghubungkan aplikasi ke server MySQL, mengeksekusi DDL schema 28 tabel InnoDB relasional multi-cabang, menyisipkan data seed awal master (cabang default, akun pemilik, saldo PPOB/E-Wallet, parameter konfigurasi bisnis), serta menyediakan utilitas verifikasi integritas skema hasil eksekusi.

Fitur ini merupakan **prasyarat mutlak (blocker)** yang harus diselesaikan sebelum tim pengembang AI lainnya dapat memulai pengerjaan modul fungsional (M.1 — M.10) yang bergantung pada tabel-tabel database.

> ⚠️ **PERINGATAN KRITIS**: Issue ini bersifat **fondasi data arsitektural**. Kesalahan pada inisialisasi skema (salah urutan CREATE TABLE, salah constraint FK, salah seed data, atau koneksi pool yang tidak stabil) akan **berdampak cascading** ke seluruh modul dan seluruh issue berikutnya. Kerjakan dengan **rapi, bersih, tidak tergesa-gesa, dan tidak buru-buru**. Pastikan setiap detail kecil sesuai standar dokumen SDLC.

> ⚠️ **PERINGATAN ISOLASI**: Issue ini **HANYA** mengerjakan inisialisasi skema database. **JANGAN** mengimplementasikan logika bisnis, menu CLI interaktif, atau fitur modul fungsional apapun. Pastikan pengerjaan issue ini **tidak menyenggol atau merusak** file, folder, atau feature lain yang sudah dibuat di issue sebelumnya (#0093 Scaffolding).

---

## 2. Persona AI yang Ditugaskan

**Persona**: `Senior Database Infrastructure Engineer & Schema Migration Specialist`

**Deskripsi Persona**: Kamu adalah seorang insinyur infrastruktur database senior yang menguasai MySQL 8.x InnoDB secara mendalam, memahami relasi Foreign Key cascading, strategi connection pooling, ACID transaction integrity, dan paradigma Functional Programming (FP) Python murni. Kamu bertanggung jawab untuk membangun jembatan koneksi yang stabil antara aplikasi Python CLI dan server database MySQL melalui jaringan LAN lokal, serta memastikan seluruh 28 tabel skema multi-cabang terinisialisasi dengan sempurna dan terverifikasi.

**Sifat yang WAJIB dimiliki**:
- **Sangat Teliti terhadap DDL SQL**: Tidak melewatkan satupun tabel, constraint, index, atau seed data dari file schema sumber.
- **Patuh Standar FP**: Menggunakan NamedTuple, pure functions, Result pattern, dan **tidak menggunakan class** di folder `logic/`.
- **Defensive Programmer**: Selalu menangani error koneksi, timeout, dan missing file secara graceful dengan kode error standar (`ERR-DB-xxx`, `ERR-FILE-xxx`).
- **Tidak Tergesa-gesa**: Mengerjakan secara bertahap, memverifikasi setiap tahap sebelum lanjut ke tahap berikutnya.
- **Komunikatif**: Menandai setiap data yang kosong, ambigu, atau tidak ditemukan di file referensi agar bisa ditindaklanjuti.
- **Tidak Merusak**: Memastikan file-file yang sudah ada dari scaffolding (#0093) tidak termodifikasi secara tidak sengaja kecuali yang memang diperlukan secara eksplisit (seperti mengaktifkan import `mysql.connector` di `db/db_connector.py`).

---

## 3. Dokumen Referensi Utama

Berikut adalah daftar dokumen SDLC yang menjadi **dasar utama (Source of Truth)** untuk pengerjaan issue ini. Baca dan ekstrak seluruh detail yang relevan dari setiap dokumen sebelum memulai implementasi.

| Prioritas | Dokumen Referensi | Path File | Bagian yang Relevan |
|:---------:|:------------------|:----------|:--------------------|
| **PRIMER** | Database Schema DDL SQL v1.2 | `docs/sdlc/03_design/01_database_schema.sql` | **SELURUH ISI FILE** — 28 tabel, 58 FK, 42 CHECK, 4 composite index, seed data cabang+pengguna+saldo_ppob+saldo_ewallet+system_configs, verifikasi integritas, konfigurasi awal session |
| **PRIMER** | ERD Database v1.2 | `docs/sdlc/03_design/02_erd_database.md` | Bab 2 (Ringkasan Model Data: 28 tabel, 284 kolom, 58 FK), Bab 3 (Full ERD 28 tabel), Bab 4 (ERD per Kelompok — 5 kelompok fungsional), Bab 5 (Matriks relasi & kardinalitas 58 FK) |
| **PRIMER** | Environment Setup v1.2 | `docs/sdlc/04_implementation/02_environment_setup.md` | Bab 6.6 (Pembuatan Database & Akun `abucom_app`), Bab 6.7 (Eksekusi Schema SQL), Bab 6.8 (Eksekusi Seed Data), Bab 6.9 (Verifikasi Konektivitas Remote), Bab 8 (Konfigurasi Proyek Aplikasi: `.env.example`) |
| **PRIMER** | System Architecture v1.2 | `docs/sdlc/03_design/03_system_architecture.md` | Bab 6.2 (Connection Pooling `abupool` & Retry Mechanism), Bab 6.3 (ACID Transaction & InnoDB), Bab 6.5 (Multi-Branch `cabang_id` Strategy), Bab 6.6 (Migrasi Data Awal: schema.sql, seed.sql) |
| **PRIMER** | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` | Bab 2.2.6 (Result Pattern NamedTuple), Bab 3 (Konvensi Penamaan), Bab 6.4 (Header Module Docstring), Bab 13 (Dependensi `mysql-connector-python==8.4.0`), Bab 16 (10 Larangan Mutlak) |
| **SEKUNDER** | Security Design v1.2 | `docs/sdlc/03_design/06_security_design.md` | Bab 3.4 (Database User Privilege: `abucom_app` hanya SELECT/INSERT/UPDATE/DELETE), Bab 4.1 (bcrypt Cost Factor 12 untuk seed password pemilik), Bab 6.5 (Manajemen Kredensial `.env`) |
| **SEKUNDER** | Git Workflow v1.2 | `docs/sdlc/04_implementation/04_git_workflow.md` | Bab 5 (Konvensi commit message: `feat(scope): deskripsi`) |
| **TERSIER** | Narasi Pemilik | `docs/sdlc/narasi.txt` | Konteks bisnis: multi-cabang readiness (poin skalabilitas), susunan tim AI, DB MySQL server lokal LAN |

> **Catatan Referensi**: File `narasi.txt` masih dibutuhkan sebagai konteks bisnis umum untuk memahami motivasi desain multi-cabang (ribuan cabang masa depan) dan topologi LAN server-client.

---

## 4. Rangkuman Detail Data dari Dokumen Referensi

Berikut adalah **ekstraksi lengkap** seluruh detail data yang relevan dan spesifik dari dokumen referensi yang mendukung pengerjaan issue ini:

### 4.1. Arsitektur Database AbuCom (Sumber: Database Schema v1.2 & ERD v1.2)

**Statistik Model Data**:
- **Total Tabel**: 28
- **Total Kolom/Atribut**: 284
- **Total Relasi Foreign Key**: 58
- **Total Unique Constraint**: 9 (tunggal & composite)
- **Total CHECK Constraint**: 42
- **Total Index Tambahan (Composite)**: 4
- **Multi-Cabang Ready (`cabang_id`)**: 100% (28 dari 28 tabel)
- **Audit Trail Ready (`created_at`/`updated_at`)**: 100% (28 dari 28 tabel)
- **Engine**: InnoDB (seluruh tabel)
- **Character Set**: `utf8mb4`
- **Collation**: `utf8mb4_unicode_ci`

**5 Kelompok Fungsional Tabel**:

| Kelompok | Deskripsi | Daftar Tabel |
|:--------:|:----------|:-------------|
| **A** | Tabel Induk (Master Tanpa FK) | `cabang` |
| **B** | Tabel Master Level 2 (FK ke Cabang) | `pengguna`, `pelanggan`, `supplier`, `barang`, `saldo_ppob`, `saldo_ewallet`, `system_configs` |
| **C** | Tabel Transaksional (FK ke Master) | `bom_komposisi`, `transaksi`, `detail_transaksi`, `antrian_kerja`, `absensi`, `kasbon`, `payroll`, `pengeluaran`, `limbah_produksi`, `jasa_service`, `poin_insentif`, `shift_handover` |
| **D** | Tabel Administrasi & Keuangan | `utang_supplier`, `pinjaman_bank`, `pinjaman_kerabat`, `aset` |
| **E** | Tabel Audit & Rekonsiliasi | `audit_logs`, `backup_logs`, `stock_opname`, `riwayat_harga_supplier` |

### 4.2. Konfigurasi Awal MySQL yang Harus Diset di Script (Sumber: Database Schema v1.2 Bagian 1)

```sql
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION';
SET NAMES utf8mb4;
```

### 4.3. Seed Data Awal yang Harus Disisipi (Sumber: Database Schema v1.2 Bagian 4)

**4.3.1. Seed `cabang` (1 baris)**:
```sql
INSERT INTO cabang (id, nama_cabang, alamat, telp) 
VALUES (1, 'Toko Pusat Bandung', 'Jl. Raya Percetakan No. 45, RT 02/RW 03, Kecamatan Sukamaju, Kota Bandung, Jawa Barat, 40123', '0227654321');
```

**4.3.2. Seed `pengguna` (1 baris — akun pemilik default)**:
```sql
INSERT INTO pengguna (id, nama_lengkap, username, password_hash, role, failed_login_attempts, locked_until, cabang_id) 
VALUES (1, 'Pemilik Usaha AbuCom', 'pemilik', '$2b$12$K3h8jD8sS9fJ2gK3l8h9oOa8fS8jK9l8g7h6j5k4l3m2n1o0p9q8r', 'pemilik', 0, NULL, 1);
```

> 🚩 **PENANDA DATA KRITIS — PASSWORD HASH SEED**: Nilai `password_hash` di atas adalah **placeholder bcrypt**. Pada implementasi, password hash pemilik harus di-generate ulang secara riil menggunakan `bcrypt.hashpw()` dengan Cost Factor 12 dari password default yang ditentukan pemilik (misal: `admin123` sebagai default awal yang wajib diganti saat first run). Tandai ini di kode sebagai `# TODO: Generate bcrypt hash riil saat deployment`.

**4.3.3. Seed `saldo_ppob` (2 baris)**:
```sql
INSERT INTO saldo_ppob (akun_tipe, saldo_terakhir, cabang_id) 
VALUES 
('Pulsa_Data', 1000000.0000, 1),
('Token_Tagihan', 1500000.0000, 1);
```

**4.3.4. Seed `saldo_ewallet` (6 baris)**:
```sql
INSERT INTO saldo_ewallet (nama_ewallet, saldo_terakhir, biaya_admin_flat, biaya_admin_persen, limit_harian, cabang_id) 
VALUES 
('Mandiri Agen', 2000000.0000, 3000.0000, 0.0000, 50000000.0000, 1),
('Dana', 1000000.0000, 1000.0000, 0.0000, 10000000.0000, 1),
('Gopay', 1000000.0000, 1000.0000, 0.0000, 10000000.0000, 1),
('LinkAja', 1000000.0000, 1000.0000, 0.0000, 10000000.0000, 1),
('ShopeePay', 1000000.0000, 1000.0000, 0.0000, 10000000.0000, 1),
('OVO', 1000000.0000, 1000.0000, 0.0000, 10000000.0000, 1);
```

**4.3.5. Seed `system_configs` (13 baris parameter bisnis)**:

| No | `parameter_key` | `parameter_value` | `tipe_data` | `deskripsi` |
|:--:|:----------------|:-------------------|:------------|:------------|
| 1 | `target_laba_payroll` | `15000000.0000` | `DECIMAL` | Target laba bersih bulanan untuk skema gaji tetap (Skenario A Smart Payroll) |
| 2 | `porsi_gaji_laba` | `0.2500` | `DECIMAL` | Persentase alokasi laba bersih untuk pool gaji karyawan (Skenario B Smart Payroll) |
| 3 | `limit_kasbon_staf` | `1000000.0000` | `DECIMAL` | Pagu maksimal utang kasbon aktif kumulatif per staf |
| 4 | `threshold_saldo_ppob` | `150000.0000` | `DECIMAL` | Batas saldo minimum PPOB yang memicu alert deposit |
| 5 | `min_topup_ppob` | `500000.0000` | `DECIMAL` | Nominal minimum deposit topup saldo PPOB |
| 6 | `toleransi_selisih_kas` | `10000.0000` | `DECIMAL` | Batas toleransi selisih kas kasir sebelum status ANOMALI |
| 7 | `poin_tier_1_rupiah` | `500.0000` | `DECIMAL` | Nilai rupiah per poin insentif Tier 1 (transaksi mudah) |
| 8 | `poin_tier_2_rupiah` | `1500.0000` | `DECIMAL` | Nilai rupiah per poin insentif Tier 2 (jasa dasar) |
| 9 | `poin_tier_3_rupiah` | `2500.0000` | `DECIMAL` | Nilai rupiah per poin insentif Tier 3 (produk kustom) |
| 10 | `poin_tier_4_rupiah` | `5000.0000` | `DECIMAL` | Nilai rupiah per poin insentif Tier 4 (pekerjaan berat/teknis) |
| 11 | `threshold_pengeluaran` | `500000.0000` | `DECIMAL` | Batas nominal pengeluaran yang memerlukan otorisasi pemilik |
| 12 | `umr_daerah` | `3200000.0000` | `DECIMAL` | Upah Minimum Regional daerah sebagai batas proteksi gaji minimum staf |
| 13 | `dana_cadangan_darurat` | `4500000.0000` | `DECIMAL` | Cadangan kas darurat minimal yang harus dijaga di laci kasir |

### 4.4. Composite Index Tambahan (Sumber: Database Schema v1.2 Bagian 3)

```sql
CREATE INDEX idx_transaksi_tanggal_cabang ON transaksi(tanggal_transaksi, cabang_id);
CREATE INDEX idx_absensi_pengguna_tanggal ON absensi(pengguna_id, tanggal);
CREATE INDEX idx_antrian_status_cabang ON antrian_kerja(status_antrian, cabang_id);
CREATE INDEX idx_barang_tipe_cabang ON barang(tipe_barang, cabang_id);
```

### 4.5. Verifikasi Integritas Pasca-Eksekusi (Sumber: Database Schema v1.2 Bagian 5)

Setelah eksekusi schema dan seed data, hasil yang diharapkan:
- `SHOW TABLES;` → **28 tabel**
- `SELECT COUNT(*) FROM cabang;` → **1**
- `SELECT COUNT(*) FROM pengguna;` → **1**
- `SELECT COUNT(*) FROM saldo_ppob;` → **2**
- `SELECT COUNT(*) FROM saldo_ewallet;` → **6**
- `SELECT COUNT(*) FROM system_configs;` → **13**

### 4.6. Restorasi Konfigurasi MySQL Pasca-Eksekusi (Sumber: Database Schema v1.2 Bagian 6)

```sql
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
```

### 4.7. Connection Pool Factory (Sumber: System Architecture v1.2 Bab 6.2)

- **Pool Name**: `abupool`
- **Pool Size**: 5 (dimuat dari `.env` variabel `DB_POOL_SIZE`)
- **Retry Mechanism**: Exponential backoff $2^n$ detik (2s, 4s, 8s), maksimal 3 kali retry
- **Error Codes Retry**: MySQL 2006 (Server has gone away) dan 2013 (Lost connection)
- **Driver**: `mysql.connector.pooling.MySQLConnectionPool`

### 4.8. Konfigurasi Koneksi dari .env (Sumber: Environment Setup v1.2 Bab 8.2)

| Variabel `.env` | Default | Keterangan |
|:-----------------|:--------|:-----------|
| `DB_HOST` | `10.10.10.10` | IP statis server MySQL LAN lokal |
| `DB_PORT` | `3306` | Port MySQL standard |
| `DB_USER` | `abucom_app` | Akun aplikasi privilege terbatas |
| `DB_PASSWORD` | `YOUR_DB_PASSWORD_HERE` | Wajib diisi manual |
| `DB_NAME` | `abucom_db` | Nama database produksi |
| `DB_POOL_SIZE` | `5` | Jumlah koneksi dalam pool |

### 4.9. Hak Akses User `abucom_app` (Sumber: Security Design v1.2 Bab 3.4)

- **Diizinkan**: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- **Dilarang**: `DROP`, `ALTER`, `CREATE`, `GRANT`
- **Implikasi**: Eksekusi DDL (`CREATE TABLE`, `CREATE INDEX`, `DROP DATABASE`) **harus menggunakan akun `root` MySQL**, bukan `abucom_app`. Modul Python hanya perlu membaca schema yang sudah dieksekusi dan melakukan operasi DML.

---

## 5. Batasan, Cakupan, dan Alur Pengerjaan

### 5.1. Cakupan Issue (Scope — Yang HARUS Dikerjakan)

- [ ] Mengaktifkan dan mengimplementasikan koneksi database riil di `db/db_connector.py` (connection pool factory + retry mechanism).
- [ ] Membuat modul baru `db/schema_initializer.py` — utilitas fungsional untuk membaca file `.sql`, mengeksekusi DDL schema, seed data, dan memverifikasi hasilnya.
- [ ] Menyalin file `docs/sdlc/03_design/01_database_schema.sql` ke root proyek sebagai `schema.sql` (file kerja untuk eksekusi).
- [ ] Mengupdate `db/__init__.py` untuk expose fungsi-fungsi baru.
- [ ] Mengupdate `main.py` untuk mengintegrasikan startup koneksi database dan menampilkan status koneksi.
- [ ] Membuat file test `tests/test_db_connection.py` dengan test koneksi dan verifikasi schema.
- [ ] Memverifikasi seluruh 28 tabel terbuat, 4 composite index ada, seed data terinsert.

### 5.2. Di Luar Cakupan (Out-of-Scope — Yang TIDAK BOLEH Dikerjakan)

> ⚠️ **PERINGATAN**: Jangan melampaui batasan berikut. Fokus hanya pada inisialisasi skema database.

- ❌ Implementasi logika bisnis modul M.1 — M.10 (itu tugas issue berikutnya).
- ❌ Implementasi menu CLI interaktif lengkap (hanya update `main.py` untuk startup koneksi).
- ❌ Pembuatan unit test logika bisnis (hanya test koneksi dan verifikasi schema).
- ❌ Modifikasi file apapun di folder `docs/` (dokumentasi SDLC sudah final).
- ❌ Modifikasi file di folder `cli/`, `logic/`, `middleware/`, `utils/` kecuali yang disebut eksplisit.
- ❌ Pembuatan fitur backup/restore database (itu tugas issue terpisah).
- ❌ Setup MySQL server fisik di Debian (itu tugas Environment Setup manual oleh pemilik — di luar scope Python).
- ❌ Pembuatan akun `abucom_app` di MySQL (itu tugas DBA/pemilik di server).

### 5.3. Prinsip Keamanan Fitur (Non-Destructive)

> ⚠️ **PERINGATAN KRITIS KEAMANAN DATA**:

- Script inisialisasi schema mengandung `DROP DATABASE IF EXISTS abucom_db` di file DDL asli. **WAJIB** menambahkan mekanisme konfirmasi ganda (double confirmation) sebelum eksekusi destructive ini.
- Script **TIDAK BOLEH** dijalankan otomatis tanpa konfirmasi eksplisit dari pengguna CLI.
- Tambahkan flag `--force` atau mekanisme input konfirmasi manual (`Ketik 'YA SAYA YAKIN' untuk melanjutkan`) sebelum DROP DATABASE.

### 5.4. Alur Pengerjaan (Workflow)

```
1. Baca & Pahami Referensi
         │
         v
2. Buat Branch: feat/init-database-schema
         │
         v
3. Salin file schema.sql ke root proyek
         │
         v
4. Implementasi db/db_connector.py (koneksi riil + pool + retry)
         │
         v
5. Buat file db/schema_initializer.py (baca SQL, eksekusi, verifikasi)
         │
         v
6. Update db/__init__.py (expose fungsi baru)
         │
         v
7. Update main.py (integrasi startup koneksi + status)
         │
         v
8. Buat tests/test_db_connection.py (test koneksi + verifikasi schema)
         │
         v
9. Verifikasi Kelengkapan Akhir (28 tabel, index, seed data)
         │
         v
10. Commit Atomis per Tahap + Push ke Server LAN
         │
         v
11. Quality Gate Review oleh Gemini 3 Flash (STK-011)
```

---

## 6. Instruksi Implementasi Detail (Low-Level Checklist)

### ⚙️ TAHAP 0 — Pembacaan dan Pemahaman Referensi

> **Tujuan**: Pastikan kamu memahami seluruh standar dan detail teknis database sebelum menulis satu baris kode pun.

- [ ] Baca file `docs/sdlc/03_design/01_database_schema.sql` secara **keseluruhan (775 baris)**. Fokus pada:
  - [ ] Bagian 1 — Konfigurasi Awal (`SET` variables, `DROP DATABASE`, `CREATE DATABASE`, `USE`).
  - [ ] Bagian 2 — Pembuatan Tabel: catat **urutan** 28 tabel (Kelompok A → B → C → D → E). Urutan ini **KRITIS** karena tabel child harus dibuat setelah tabel parent-nya.
  - [ ] Bagian 3 — 4 Composite Index (`CREATE INDEX`).
  - [ ] Bagian 4 — Seed Data (`INSERT INTO`): catat jumlah baris per tabel (cabang=1, pengguna=1, saldo_ppob=2, saldo_ewallet=6, system_configs=13).
  - [ ] Bagian 5 — Query Verifikasi Integritas (`SHOW TABLES`, `SELECT COUNT`).
  - [ ] Bagian 6 — Restorasi Konfigurasi MySQL.
- [ ] Baca file `docs/sdlc/03_design/02_erd_database.md`. Fokus pada:
  - [ ] Bab 2.1 — Statistik model data (28 tabel, 284 kolom, 58 FK).
  - [ ] Bab 2.2 — Klasifikasi 5 kelompok fungsional dan daftar tabel masing-masing.
  - [ ] Bab 5 — Matriks relasi FK (pastikan semua `ON DELETE` dan `ON UPDATE` dipahami).
- [ ] Baca file `docs/sdlc/04_implementation/02_environment_setup.md`. Fokus pada:
  - [ ] Bab 6.6 — Pembuatan database `abucom_db` dan user `abucom_app` (pahami privilege boundaries).
  - [ ] Bab 6.7 — Instruksi eksekusi schema: `mysql -u root -p abucom_db < /tmp/schema.sql`.
  - [ ] Bab 6.9 — Verifikasi konektivitas remote (ping + port test).
- [ ] Baca file `docs/sdlc/03_design/03_system_architecture.md`. Fokus pada:
  - [ ] Bab 6.2 — Connection Pooling (`abupool`, pool_size=5, retry 3x exponential backoff).
  - [ ] Bab 6.3 — ACID Transaction Strategy (`START TRANSACTION`, `COMMIT`, `ROLLBACK`).
  - [ ] Bab 6.5 — Multi-Branch Ready (`cabang_id` default 1 di semua tabel).
  - [ ] Bab 6.6 — Strategi migrasi data awal (schema.sql + seed.sql).
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md`. Fokus pada:
  - [ ] Bab 2.2.6 — Template Result Pattern NamedTuple.
  - [ ] Bab 3 — Konvensi Penamaan (snake_case fungsi, PascalCase NamedTuple).
  - [ ] Bab 6.4 — Template Header Module Docstring.
  - [ ] Bab 13 — Dependensi: `mysql-connector-python==8.4.0` (sudah ada di requirements.txt).
  - [ ] Bab 16 — 10 Larangan Mutlak (terutama: **DILARANG float**, **DILARANG class di logic/**, **DILARANG f-string SQL**).
- [ ] Baca file `docs/sdlc/03_design/06_security_design.md`. Fokus pada:
  - [ ] Bab 3.4 — Privilege `abucom_app` (hanya DML, bukan DDL).
  - [ ] Bab 4.1 — bcrypt Cost Factor 12 untuk seed password pemilik.
- [ ] Baca file `docs/sdlc/narasi.txt` untuk memahami konteks bisnis pemilik terkait multi-cabang dan topologi LAN.

> 🚩 **PENTING**: Jika ada perbedaan antara dokumen, **prioritaskan Database Schema v1.2** karena itu adalah DDL fisik final. Jika DDL tidak menyebutkan detail tertentu, cek di ERD v1.2 dan System Architecture v1.2.

---

### ⚙️ TAHAP 1 — Pembuatan Branch Git

- [ ] Pastikan kamu berada di branch `develop` yang sudah terbaru:
  ```bash
  git checkout develop
  git pull origin develop
  ```
- [ ] Buat branch baru sesuai konvensi Git Workflow:
  ```bash
  git checkout -b feat/init-database-schema
  ```

---

### ⚙️ TAHAP 2 — Penyalinan File Schema SQL ke Root Proyek

> **Tujuan**: Menyediakan file schema.sql di root proyek agar dapat dibaca oleh modul Python.

- [ ] Salin file `docs/sdlc/03_design/01_database_schema.sql` ke root proyek dengan nama `schema.sql`:
  ```bash
  cp docs/sdlc/03_design/01_database_schema.sql schema.sql
  ```
  Pada Windows:
  ```cmd
  copy docs\sdlc\03_design\01_database_schema.sql schema.sql
  ```
- [ ] Pastikan file `schema.sql` menggunakan encoding **UTF-8** dan line ending **LF**.
- [ ] Pastikan file `schema.sql` **TIDAK** dimasukkan ke `.gitignore` — file ini harus di-track oleh Git.
- [ ] Verifikasi file tersalin dengan benar:
  - [ ] Baris pertama berisi `-- ============================================================`
  - [ ] Baris terakhir berisi baris kosong setelah footer referensi dokumen.
  - [ ] Total baris: ~775 baris.

- [ ] **COMMIT ATOMIS TAHAP 2**:
  ```bash
  git add schema.sql
  git commit -m "feat(db): salin database schema DDL SQL v1.2 ke root proyek"
  ```

---

### ⚙️ TAHAP 3 — Implementasi `db/db_connector.py` (Koneksi Riil)

> **Tujuan**: Mengaktifkan koneksi database riil menggantikan stub placeholder dari issue #0093. Implementasi connection pool factory dan retry mechanism sesuai System Architecture v1.2.

- [ ] Buka file `db/db_connector.py` yang sudah ada dari scaffolding.
- [ ] **Aktifkan import** `mysql.connector` yang sebelumnya di-comment:
  ```python
  import mysql.connector
  from mysql.connector import pooling, errors
  ```
- [ ] **Hapus komentar** `# TODO: Import mysql.connector setelah environment setup selesai`.
- [ ] Tambahkan import `logging` untuk diagnostic messages.
- [ ] Implementasikan variabel modul-level untuk menyimpan referensi pool:
  ```python
  # Variabel modul-level untuk menyimpan referensi pool (FP: closure-like state)
  _connection_pool = None
  ```
- [ ] Implementasikan fungsi `create_connection_pool()` secara **riil** (bukan stub):
  - [ ] Gunakan `mysql.connector.pooling.MySQLConnectionPool`.
  - [ ] Pool name: `abupool` (sesuai System Architecture Bab 6.2).
  - [ ] Pool size: dimuat dari parameter (default 5 dari `.env`).
  - [ ] Set `pool_reset_session=True`.
  - [ ] Tangani exception `mysql.connector.Error` dan kembalikan `Result` pattern.
  - [ ] Simpan referensi pool ke variabel modul `_connection_pool`.
  - [ ] Return `Result(True, pool, None)` jika sukses.
  - [ ] Return `Result(False, None, 'ERR-DB-001: ...')` jika gagal.
- [ ] Implementasikan fungsi `get_db_connection()` secara **riil**:
  - [ ] Ambil koneksi dari `_connection_pool.get_connection()`.
  - [ ] Implementasikan retry exponential backoff: 3 kali, interval $2^{attempt}$ detik (2s, 4s, 8s).
  - [ ] Tangkap error code 2006 dan 2013 untuk retry.
  - [ ] Return `Result(True, connection, None)` jika sukses.
  - [ ] Return `Result(False, None, 'ERR-DB-001: ...')` jika semua retry gagal.
- [ ] Tambahkan fungsi baru `close_connection_pool()`:
  ```python
  def close_connection_pool() -> Result:
      """Menutup connection pool database secara aman.

      Returns:
          Result: NamedTuple berisi status penutupan pool.
      """
  ```
- [ ] Tambahkan fungsi baru `get_root_connection()` khusus untuk eksekusi DDL dengan akun root:
  ```python
  def get_root_connection(
      host: str,
      port: int,
      user: str,
      password: str
  ) -> Result:
      """Membuat koneksi langsung (non-pool) ke MySQL sebagai root untuk eksekusi DDL.

      Fungsi ini digunakan KHUSUS untuk inisialisasi schema awal
      yang memerlukan privilege CREATE/DROP TABLE.
      TIDAK menggunakan connection pool.

      Args:
          host (str): Alamat IP statis server database.
          port (int): Port database MySQL.
          user (str): Username root MySQL.
          password (str): Password root MySQL.

      Returns:
          Result: NamedTuple berisi koneksi root atau pesan error.
      """
  ```
- [ ] Pastikan setiap fungsi memiliki **type hints** lengkap dan **docstring PEP 257**.
- [ ] Pastikan menggunakan **4 spasi indentasi**, **single quote** untuk string, **double quote** untuk docstring.
- [ ] Pastikan `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])` tetap konsisten.

- [ ] **COMMIT ATOMIS TAHAP 3**:
  ```bash
  git add db/db_connector.py
  git commit -m "feat(db): implementasi connection pool riil dan retry mechanism"
  ```

---

### ⚙️ TAHAP 4 — Pembuatan File `db/schema_initializer.py`

> **Tujuan**: Membuat modul fungsional baru yang bertanggung jawab membaca file schema.sql, mengeksekusi DDL CREATE TABLE, menyisipkan seed data, dan memverifikasi hasil.

- [ ] Buat file baru `db/schema_initializer.py`.
- [ ] Tulis **header module docstring** sesuai Coding Standard Bab 6.4:
  ```python
  """
  Nama Modul: schema_initializer.py
  Deskripsi: Utilitas fungsional untuk inisialisasi skema database MySQL
             multi-cabang AbuCom. Membaca file DDL SQL, mengeksekusi
             CREATE TABLE/INDEX/INSERT secara transaksional, dan memverifikasi
             integritas seluruh 28 tabel, 4 composite index, dan seed data.
  Author: Claude Sonnet 4.6 (STK-004)
  Tanggal: 2026-06-03
  """
  ```
- [ ] Import yang diperlukan:
  ```python
  import os
  from pathlib import Path
  from collections import namedtuple
  
  import mysql.connector
  from mysql.connector import errors
  ```
- [ ] Definisikan Result pattern konsisten:
  ```python
  Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
  ```
- [ ] Definisikan konstanta verifikasi:
  ```python
  # Konstanta verifikasi integritas schema
  EXPECTED_TABLE_COUNT = 28
  EXPECTED_SEED_COUNTS = {
      'cabang': 1,
      'pengguna': 1,
      'saldo_ppob': 2,
      'saldo_ewallet': 6,
      'system_configs': 13,
  }
  ```
- [ ] Implementasikan fungsi `read_sql_file()`:
  ```python
  def read_sql_file(file_path: str) -> Result:
      """Membaca dan mem-parsing file SQL menjadi daftar statement individual.

      Memisahkan multi-statement SQL berdasarkan delimiter semicolon (;).
      Mengabaikan baris komentar (-- ...) dan baris kosong.

      Args:
          file_path (str): Path absolut atau relatif ke file .sql.

      Returns:
          Result: NamedTuple berisi list[str] statement SQL atau pesan error.
      """
  ```
  - [ ] Baca file dengan `encoding='utf-8'`.
  - [ ] Tangani `FileNotFoundError` → return `Result(False, None, 'ERR-FILE-003: ...')`.
  - [ ] Split content berdasarkan `;` untuk mendapat individual statements.
  - [ ] Filter out baris komentar (`--`) dan baris kosong.
  - [ ] Return `Result(True, statements, None)`.

- [ ] Implementasikan fungsi `execute_schema_init()`:
  ```python
  def execute_schema_init(
      root_connection,
      sql_statements: list[str]
  ) -> Result:
      """Mengeksekusi seluruh statement DDL SQL secara berurutan.

      Statement dieksekusi satu per satu secara berurutan (bukan batch)
      karena DDL MySQL auto-commit dan tidak bisa di-wrap dalam transaction.

      Args:
          root_connection: Koneksi MySQL root (bukan abucom_app).
          sql_statements (list[str]): Daftar statement SQL dari read_sql_file().

      Returns:
          Result: NamedTuple berisi jumlah statement yang berhasil dieksekusi.
      """
  ```
  - [ ] Gunakan `cursor.execute()` untuk setiap statement satu-per-satu.
  - [ ] Tangkap exception per-statement dan log error tanpa menghentikan seluruh proses.
  - [ ] Return total statement sukses dan gagal.

- [ ] Implementasikan fungsi `verify_schema_integrity()`:
  ```python
  def verify_schema_integrity(db_connection) -> Result:
      """Memverifikasi integritas skema database hasil inisialisasi.

      Memeriksa:
      1. Jumlah tabel = 28
      2. Keberadaan 4 composite index
      3. Jumlah seed data per tabel master

      Args:
          db_connection: Koneksi aktif ke database abucom_db.

      Returns:
          Result: NamedTuple berisi dict laporan verifikasi atau pesan error.
      """
  ```
  - [ ] Jalankan `SHOW TABLES` dan hitung jumlahnya (harus 28).
  - [ ] Jalankan `SHOW INDEX FROM transaksi` dsb untuk memastikan 4 composite index ada.
  - [ ] Jalankan `SELECT COUNT(*) FROM cabang` dsb untuk verifikasi seed data.
  - [ ] Return dict berisi detail verifikasi: `{'tables': 28, 'indexes': 4, 'seeds': {...}}`.

- [ ] Implementasikan fungsi `run_full_initialization()`:
  ```python
  def run_full_initialization(
      root_host: str,
      root_port: int,
      root_user: str,
      root_password: str,
      schema_file_path: str,
      app_db_name: str = 'abucom_db'
  ) -> Result:
      """Menjalankan proses inisialisasi skema database secara lengkap.

      Alur eksekusi:
      1. Buka koneksi root ke MySQL server.
      2. Baca file schema.sql.
      3. Eksekusi seluruh DDL statement.
      4. Verifikasi integritas hasil.
      5. Tutup koneksi root.

      Args:
          root_host (str): IP server MySQL.
          root_port (int): Port MySQL.
          root_user (str): Username root MySQL.
          root_password (str): Password root MySQL.
          schema_file_path (str): Path file schema.sql.
          app_db_name (str): Nama database target (default 'abucom_db').

      Returns:
          Result: NamedTuple berisi laporan inisialisasi lengkap.
      """
  ```

- [ ] Pastikan TIDAK ada penggunaan `class` di file ini (FP murni).
- [ ] Pastikan TIDAK ada penggunaan `float` untuk nilai apapun.
- [ ] Pastikan TIDAK ada f-string dalam query SQL (gunakan `%s` bindings untuk parameterized queries pada SELECT verifikasi).

- [ ] **COMMIT ATOMIS TAHAP 4**:
  ```bash
  git add db/schema_initializer.py
  git commit -m "feat(db): buat modul schema_initializer untuk inisialisasi DDL dan seed data"
  ```

---

### ⚙️ TAHAP 5 — Update `db/__init__.py`

> **Tujuan**: Expose fungsi-fungsi baru dari modul yang diimplementasikan.

- [ ] Buka file `db/__init__.py` yang sudah ada.
- [ ] Tambahkan import untuk fungsi-fungsi baru:
  ```python
  from db.db_connector import create_connection_pool, get_db_connection, close_connection_pool
  from db.schema_initializer import run_full_initialization, verify_schema_integrity
  ```
- [ ] Pastikan header module docstring **TIDAK dihapus** dari file yang sudah ada.

- [ ] **COMMIT ATOMIS TAHAP 5**:
  ```bash
  git add db/__init__.py
  git commit -m "feat(db): expose fungsi connection pool dan schema initializer di __init__"
  ```

---

### ⚙️ TAHAP 6 — Update `main.py` (Integrasi Startup Koneksi)

> **Tujuan**: Mengintegrasikan startup koneksi database ke entry point aplikasi. Menggantikan placeholder `TODO` dengan pemanggilan riil.

- [ ] Buka file `main.py` yang sudah ada.
- [ ] **JANGAN HAPUS** kode yang sudah ada. Hanya **update blok TODO** yang relevan.
- [ ] Tambahkan import di bagian atas:
  ```python
  from config.settings import load_settings
  from db.db_connector import create_connection_pool, close_connection_pool
  ```
- [ ] Update blok `# Tahap 2: Muat konfigurasi dari .env`:
  ```python
  # Tahap 2: Muat konfigurasi dari .env
  config = load_settings()
  print(f'[INFO] Konfigurasi dimuat. Cabang ID: {config.app_cabang_id}')
  print(f'[INFO] Target database: {config.db_name}@{config.db_host}:{config.db_port}')
  ```
- [ ] Update blok `# Tahap 3: Inisialisasi koneksi database pool`:
  ```python
  # Tahap 3: Inisialisasi koneksi database pool
  pool_result = create_connection_pool(
      host=config.db_host,
      port=config.db_port,
      user=config.db_user,
      password=config.db_password,
      database=config.db_name,
      pool_size=config.db_pool_size,
  )
  if not pool_result.is_success:
      print(f'⛔ {pool_result.error_msg}')
      print('   Pastikan MySQL Server aktif dan kredensial di .env sudah benar.')
      sys.exit(1)
  print('[INFO] Connection pool database berhasil diinisialisasi (abupool).')
  ```
- [ ] **Pertahankan** blok `# Tahap 4: Peluncuran antarmuka CLI login` dengan TODO placeholder-nya.
- [ ] Tambahkan blok cleanup sebelum `input()` akhir:
  ```python
  # Cleanup: Tutup connection pool saat aplikasi ditutup
  close_connection_pool()
  ```
- [ ] Pastikan `main.py` **tetap compilable** tanpa error.

- [ ] **COMMIT ATOMIS TAHAP 6**:
  ```bash
  git add main.py
  git commit -m "feat(db): integrasi startup koneksi database pool di main.py"
  ```

---

### ⚙️ TAHAP 7 — Pembuatan File Test `tests/test_db_connection.py`

> **Tujuan**: Membuat test otomatis untuk memvalidasi koneksi database dan integritas schema.

- [ ] Buat file baru `tests/test_db_connection.py`.
- [ ] Tulis **header module docstring**:
  ```python
  """
  Nama Modul: test_db_connection.py
  Deskripsi: Integration testing koneksi database MySQL dan verifikasi
             integritas skema 28 tabel multi-cabang AbuCom.
  Author: Claude Sonnet 4.6 (STK-004)
  Tanggal: 2026-06-03
  """
  ```
- [ ] Implementasikan test cases berikut:
  - [ ] `test_create_connection_pool_with_valid_config()` — Pastikan pool berhasil dibuat dengan parameter valid.
  - [ ] `test_create_connection_pool_with_invalid_host()` — Pastikan return `Result(False, ...)` jika host tidak valid.
  - [ ] `test_get_db_connection_returns_active_connection()` — Pastikan koneksi yang didapat dari pool aktif dan bisa query.
  - [ ] `test_schema_has_28_tables()` — Pastikan `SHOW TABLES` return 28 tabel.
  - [ ] `test_seed_data_cabang_count()` — Pastikan `SELECT COUNT(*) FROM cabang` = 1.
  - [ ] `test_seed_data_pengguna_count()` — Pastikan `SELECT COUNT(*) FROM pengguna` = 1.
  - [ ] `test_seed_data_system_configs_count()` — Pastikan `SELECT COUNT(*) FROM system_configs` = 13.
  - [ ] `test_composite_index_exists_on_transaksi()` — Pastikan index `idx_transaksi_tanggal_cabang` ada.
  - [ ] `test_read_sql_file_valid_path()` — Pastikan `read_sql_file('schema.sql')` return sukses.
  - [ ] `test_read_sql_file_invalid_path()` — Pastikan `read_sql_file('nonexistent.sql')` return error.

- [ ] Setiap test function harus memiliki **type hints** `-> None` dan **docstring PEP 257**.
- [ ] Gunakan `pytest` fixture untuk setup/teardown koneksi jika diperlukan.

> 🚩 **CATATAN TEST**: Test ini memerlukan **database MySQL yang sudah tersetup dan schema sudah dieksekusi**. Jika database belum tersedia, test akan di-skip. Gunakan `pytest.mark.skipif` untuk menangani kondisi ini secara graceful.

- [ ] **COMMIT ATOMIS TAHAP 7**:
  ```bash
  git add tests/test_db_connection.py
  git commit -m "feat(test): tambah integration test koneksi database dan verifikasi schema"
  ```

---

### ⚙️ TAHAP 8 — Verifikasi Kelengkapan Akhir

> **Tujuan**: Pastikan TIDAK ADA satupun file yang terlewat atau detail yang kurang.

- [ ] Jalankan perintah `tree` (Windows) atau `find . -type f -name "*.py"` (Linux) dan bandingkan output dengan checklist di bawah.
- [ ] Verifikasi **checklist kelengkapan file** berikut:

**File Root (baru):**
- [ ] `schema.sql` — ada, berisi 775 baris DDL SQL, 28 tabel, seed data, verifikasi integritas.

**Package `db/` (file dimodifikasi + file baru):**
- [ ] `db/__init__.py` — ada, sudah mengekspose `create_connection_pool`, `get_db_connection`, `close_connection_pool`, `run_full_initialization`, `verify_schema_integrity`.
- [ ] `db/db_connector.py` — ada, sudah memiliki implementasi riil `create_connection_pool()`, `get_db_connection()`, `close_connection_pool()`, `get_root_connection()`. Import `mysql.connector` sudah aktif (tidak lagi di-comment).
- [ ] `db/query_builder.py` — ada, **TIDAK DIMODIFIKASI** dari scaffolding (masih stub).
- [ ] `db/schema_initializer.py` — ada **(FILE BARU)**, memiliki fungsi `read_sql_file()`, `execute_schema_init()`, `verify_schema_integrity()`, `run_full_initialization()`.

**File `main.py` (dimodifikasi):**
- [ ] `main.py` — ada, startup koneksi database pool sudah diimplementasikan, cleanup pool ada sebelum exit.

**Package `tests/` (file baru):**
- [ ] `tests/test_db_connection.py` — ada **(FILE BARU)**, berisi 10 test cases.

**File yang TIDAK BOLEH BERUBAH:**
- [ ] `config/settings.py` — **TIDAK BERUBAH** (sudah benar dari scaffolding).
- [ ] `.env.example` — **TIDAK BERUBAH**.
- [ ] `requirements.txt` — **TIDAK BERUBAH** (`mysql-connector-python==8.4.0` sudah ada).
- [ ] Semua file di `cli/`, `logic/`, `middleware/`, `utils/` — **TIDAK BERUBAH**.
- [ ] Semua file di `docs/` — **TIDAK BERUBAH**.

---

### ⚙️ TAHAP 9 — Verifikasi Teknis

- [ ] Jalankan `python -m py_compile db/db_connector.py` — pastikan tidak ada error kompilasi.
- [ ] Jalankan `python -m py_compile db/schema_initializer.py` — pastikan tidak ada error kompilasi.
- [ ] Jalankan `python -m py_compile main.py` — pastikan tidak ada error kompilasi.
- [ ] Jalankan `python main.py` dari root proyek. Hasil yang diharapkan:
  - Jika `.env` **belum ada**: Pesan `⛔ ERR-FILE-001`.
  - Jika `.env` **ada tapi DB tidak tersedia**: Pesan `⛔ ERR-DB-001: ...` diikuti pesan petunjuk.
  - Jika `.env` **ada dan DB tersedia**: Pesan `[INFO] Connection pool database berhasil diinisialisasi (abupool).`
- [ ] Jalankan `pytest tests/test_db_connection.py -v` — pastikan test yang bisa berjalan PASSED, test yang butuh DB di-skip gracefully.
- [ ] Jalankan `pytest tests/ -v` — pastikan **SELURUH** test dari scaffolding (#0093) masih **PASSED** (tidak ada regresi).

---

### ⚙️ TAHAP 10 — Push dan Quality Gate

- [ ] Push seluruh commit ke server LAN:
  ```bash
  git push origin feat/init-database-schema
  ```
- [ ] Picu review otomatis oleh Gemini 3 Flash (STK-011) untuk memverifikasi:
  - [ ] Seluruh file `.py` baru memiliki header module docstring.
  - [ ] Seluruh nama file dan folder menggunakan `snake_case`.
  - [ ] Tidak ada kata kunci `class` di file `db/schema_initializer.py`.
  - [ ] Tidak ada penggunaan `float` untuk perhitungan atau seed data.
  - [ ] Tidak ada f-string dalam query SQL.
  - [ ] Tidak ada credentials riil yang di-hardcode (semua dari `.env`).
  - [ ] Import `mysql.connector` sudah aktif (tidak lagi di-comment) di `db/db_connector.py`.
  - [ ] File `db/query_builder.py` **TIDAK TERSENTUH**.
  - [ ] Seluruh test dari scaffolding (#0093) masih PASSED.
- [ ] Serahkan ke Junior Programmer (STK-000) untuk approval akhir.

---

## 7. Instruksi Khusus Inisialisasi Database

### 7.1. Aturan Penulisan Fungsi Baru

Setiap **fungsi baru** WAJIB mengikuti format ini:

```python
def nama_fungsi(parameter: tipe) -> tipe_return:
    """Deskripsi singkat apa yang dilakukan fungsi ini.

    (Ref: [Nama Dokumen SDLC] Bab X.Y)

    Args:
        parameter (tipe): Deskripsi parameter.

    Returns:
        tipe_return: Deskripsi return value.
    """
    # Implementasi
    pass
```

### 7.2. Aturan Penanganan Error MySQL

Setiap error MySQL yang tertangkap WAJIB:
1. Di-wrap dalam Result pattern: `Result(False, None, 'ERR-DB-XXX: Deskripsi error')`.
2. Di-log ke stderr atau logging module (jangan print ke stdout).
3. **TIDAK** menghentikan seluruh program secara tiba-tiba (graceful degradation).
4. Menyertakan kode error MySQL asli di dalam pesan: `f'ERR-DB-001: Koneksi gagal (MySQL Error {e.errno}: {e.msg})'`.

### 7.3. Aturan Eksekusi DDL Multi-Statement

File `schema.sql` mengandung **ratusan statement SQL** yang harus dieksekusi berurutan. Aturan:
1. Gunakan `cursor.execute()` per-statement (bukan `cursor.executemany()`).
2. **Alternatif**: Gunakan parameter `multi=True` pada `cursor.execute(full_sql, multi=True)` yang didukung `mysql-connector-python` untuk eksekusi multi-statement. **Jika menggunakan metode ini**, pastikan mengiterasi semua result sets:
   ```python
   for result in cursor.execute(sql_content, multi=True):
       pass  # Konsumsi seluruh result sets
   ```
3. Statement `SET`, `DROP DATABASE`, `CREATE DATABASE`, `USE` harus diperlakukan khusus karena mengubah konteks koneksi.
4. Tangkap error per-statement agar satu statement gagal tidak menghentikan seluruh proses.

### 7.4. Aturan Keamanan Script Inisialisasi

1. Script inisialisasi **HANYA** boleh dijalankan secara eksplisit dari menu/command khusus, **BUKAN** otomatis saat startup `main.py`.
2. Sebelum `DROP DATABASE`, **WAJIB** menampilkan peringatan:
   ```
   ⚠️  PERINGATAN: Operasi ini akan MENGHAPUS SELURUH DATA di database abucom_db!
   ⚠️  Seluruh tabel, data transaksi, dan konfigurasi akan HILANG PERMANEN.
   
   Ketik 'YA SAYA YAKIN' untuk melanjutkan, atau tekan Enter untuk membatalkan:
   ```
3. Password root MySQL **TIDAK BOLEH** disimpan di `.env`. Harus diminta secara interaktif via `getpass.getpass()` saat proses inisialisasi.

### 7.5. Encoding File

- Semua file `.py` baru WAJIB menggunakan encoding **UTF-8**.
- Semua file `.py` baru WAJIB menggunakan line ending **LF** (sesuai `.gitattributes`).
- File `schema.sql` WAJIB menggunakan encoding **UTF-8**.

---

## 8. Data yang Kosong / Perlu Ditindaklanjuti

> 🚩 **PENANDA DATA YANG MEMERLUKAN TINDAK LANJUT**:

| No | Item | Status | Catatan |
|:--:|:-----|:------:|:--------|
| 1 | Password hash seed `pengguna.pemilik` | ⚠️ PLACEHOLDER | Nilai `$2b$12$K3h8jD8sS9fJ2gK3l8h9oOa8fS8jK9l8g7h6j5k4l3m2n1o0p9q8r` di schema.sql adalah **placeholder**. Password riil harus di-generate saat deployment. Tandai di kode: `# TODO: Generate bcrypt hash riil saat deployment pertama`. |
| 2 | IP Server MySQL di `.env` | ⚠️ PLACEHOLDER | Default `DB_HOST=10.10.10.10` di `.env.example` adalah contoh. IP riil server LAN toko (`192.168.1.200` sesuai Environment Setup) harus diset manual oleh pemilik saat deployment. |
| 3 | File `seed.sql` terpisah | ℹ️ TIDAK DIPERLUKAN | Di `01_database_schema.sql`, seed data **sudah terintegrasi** di dalam file DDL (Bagian 4). Tidak perlu membuat file `seed.sql` terpisah untuk issue ini. Environment Setup Bab 6.8 menyebutkan `seed.sql` tapi pada DDL v1.2 seed sudah inline. |
| 4 | Database `abucom_test_db` | ℹ️ OPSIONAL | Environment Setup Bab 6.6.2 menyebutkan database testing `abucom_test_db`. Issue ini **hanya** fokus pada database produksi `abucom_db`. Testing database akan dikerjakan di issue terpisah. |
| 5 | Privilege `CREATE`/`DROP` untuk `abucom_app` | ⚠️ KETERBATASAN DESAIN | User `abucom_app` **TIDAK MEMILIKI** privilege DDL (CREATE/DROP/ALTER). Eksekusi schema.sql **HARUS** menggunakan akun `root` MySQL. Modul `schema_initializer.py` harus meminta credentials root secara interaktif. |
| 6 | Password `abucom_app` di `.env` | ⚠️ MANUAL | Nilai `DB_PASSWORD=YOUR_DB_PASSWORD_HERE` di `.env.example`. Password riil harus diset manual oleh pemilik setelah membuat user di MySQL server (Environment Setup Bab 6.6.3). |
| 7 | IP Server di `config/settings.py` | ℹ️ SUDAH BENAR | Default `DEFAULT_DB_HOST = '10.10.10.10'` di `settings.py` sudah sesuai dengan `.env.example`. IP riil disesuaikan via `.env`. |

---

## 9. Checklist Kualitas Akhir

Sebelum menandai issue ini sebagai **Done**, pastikan seluruh item berikut terpenuhi:

- [ ] **Kelengkapan File**: Semua file baru (`schema.sql`, `db/schema_initializer.py`, `tests/test_db_connection.py`) telah dibuat.
- [ ] **Modifikasi Terkontrol**: Hanya file `db/db_connector.py`, `db/__init__.py`, dan `main.py` yang dimodifikasi — tidak ada file lain yang tersentuh.
- [ ] **Konvensi Penamaan**: Seluruh nama file/folder baru menggunakan `snake_case`, NamedTuple menggunakan `PascalCase`.
- [ ] **Header Docstring**: Setiap file `.py` baru memiliki header module docstring PEP 257.
- [ ] **Type Hints**: Setiap fungsi baru memiliki type hints pada parameter dan return value.
- [ ] **Tidak Ada Class**: Tidak ada deklarasi `class` di file `db/schema_initializer.py`.
- [ ] **Tidak Ada Float**: Tidak ada penggunaan tipe `float` di seluruh file yang dimodifikasi/dibuat.
- [ ] **Tidak Ada F-String SQL**: Tidak ada penggunaan f-string untuk menyusun query SQL.
- [ ] **Tidak Ada Credentials Hardcoded**: Semua credentials dimuat dari `.env` atau diminta interaktif.
- [ ] **Result Pattern Konsisten**: Definisi `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])` konsisten di semua file.
- [ ] **Encoding UTF-8**: Seluruh file `.py` baru ber-encoding UTF-8.
- [ ] **Line Ending LF**: Seluruh file `.py` baru menggunakan LF (diatur oleh `.gitattributes`).
- [ ] **Compilable**: Seluruh file `.py` yang dimodifikasi/dibuat lolos `python -m py_compile` tanpa error.
- [ ] **Tests Regresi**: `pytest tests/ -v` → Seluruh test dari scaffolding (#0093) masih **PASSED** (tidak ada regresi).
- [ ] **Commit Rapi**: Setiap commit mengikuti Conventional Commits format `feat(scope): deskripsi`.
- [ ] **Tidak Menyenggol Fitur Lain**: Tidak ada modifikasi file di folder `docs/`, `cli/`, `logic/`, `middleware/`, `utils/`, atau `exports/`.
- [ ] **Data Kosong Ditandai**: Semua item yang kosong/ambigu sudah dicatat di Bab 8.
- [ ] **Konfirmasi Destruktif**: Mekanisme konfirmasi ganda sudah ada sebelum operasi `DROP DATABASE`.

---

## 10. Instruksi Tambahan Spesifik untuk Issue Ini

### 10.1. Urutan Eksekusi DDL yang Benar

File `schema.sql` sudah diurutkan secara benar berdasarkan dependensi FK:
1. **Kelompok A** (tabel tanpa FK): `cabang` — **harus pertama**.
2. **Kelompok B** (FK ke `cabang`): `pengguna`, `pelanggan`, `supplier`, `barang`, `saldo_ppob`, `saldo_ewallet`, `system_configs`.
3. **Kelompok C** (FK ke Kelompok B): `bom_komposisi`, `transaksi`, `detail_transaksi`, dll.
4. **Kelompok D** (FK ke Kelompok B): `utang_supplier`, `pinjaman_bank`, dll.
5. **Kelompok E** (FK ke Kelompok B/C): `audit_logs`, `backup_logs`, `stock_opname`, `riwayat_harga_supplier`.

> ⚠️ **JANGAN** mengubah urutan CREATE TABLE di file `schema.sql`. Urutan sudah dioptimalkan agar tidak ada error FK dependency.

### 10.2. Strategi Multi-Statement SQL

`mysql-connector-python` mendukung eksekusi multi-statement via parameter `multi=True`:
```python
cursor = connection.cursor()
for result in cursor.execute(sql_content, multi=True):
    if result.with_rows:
        rows = result.fetchall()
connection.commit()
```

Namun perlu diperhatikan:
- Statement `SET`, `DROP DATABASE`, `CREATE DATABASE`, dan `USE` mengubah konteks koneksi.
- Setelah `USE abucom_db`, seluruh statement selanjutnya akan merujuk database tersebut.
- Jika menggunakan `multi=True`, pastikan koneksi **TIDAK** menggunakan connection pool (gunakan koneksi langsung root).

### 10.3. Integrasi dengan Scaffolding yang Sudah Ada

File `db/db_connector.py` dari scaffolding (#0093) sudah memiliki:
- Definisi `Result` namedtuple
- Konstanta `MAX_RETRIES = 3` dan `RETRY_ERROR_CODES = (2006, 2013)`
- Stub fungsi `create_connection_pool()` dan `get_db_connection()`

**INSTRUKSI**: Pertahankan struktur yang sudah ada, hanya **ganti isi fungsi** dari stub (return placeholder) ke implementasi riil. **JANGAN** mengubah signature fungsi yang sudah ada kecuali menambahkan parameter opsional baru.

### 10.4. Penanganan Konfigurasi `.env` yang Sudah Ada

File `config/settings.py` sudah membaca variabel `.env` dan menyediakannya via `AppConfig` namedtuple. **Gunakan** `load_settings()` untuk mendapatkan konfigurasi database. **JANGAN** membaca `.env` secara manual di `db/db_connector.py`.

### 10.5. Kompatibilitas Lintas OS (Windows & Linux)

Sesuai System Architecture v1.2 Bab 3.4:
- Gunakan `pathlib.Path` untuk resolusi path file `schema.sql`, **BUKAN** string concatenation manual.
- Gunakan `open(file_path, 'r', encoding='utf-8')` secara eksplisit saat membaca file SQL.

---

## 11. Referensi Commit Message untuk Issue Ini

Berikut adalah daftar lengkap commit message yang harus digunakan (sesuai Conventional Commits dan Git Workflow Bab 5):

| Tahap | Commit Message |
|:-----:|:---------------|
| 2 | `feat(db): salin database schema DDL SQL v1.2 ke root proyek` |
| 3 | `feat(db): implementasi connection pool riil dan retry mechanism` |
| 4 | `feat(db): buat modul schema_initializer untuk inisialisasi DDL dan seed data` |
| 5 | `feat(db): expose fungsi connection pool dan schema initializer di __init__` |
| 6 | `feat(db): integrasi startup koneksi database pool di main.py` |
| 7 | `feat(test): tambah integration test koneksi database dan verifikasi schema` |

---

*Issue ini dideklarasikan sebagai spesifikasi resmi inisialisasi skema database multi-cabang proyek AbuCom. Dikerjakan oleh persona `Senior Database Infrastructure Engineer & Schema Migration Specialist`.*
