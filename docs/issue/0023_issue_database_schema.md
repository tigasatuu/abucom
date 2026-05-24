# Pembuatan & Penyusunan Dokumen Database Schema (DDL SQL)

---

| Atribut Issue     | Nilai                                                                    |
|-------------------|--------------------------------------------------------------------------|
| **Judul**         | Pembuatan & Penyusunan Dokumen Database Schema (DDL SQL) AbuCom          |
| **Tipe**          | Task — Pembuatan Dokumen Teknis SDLC                                     |
| **Prioritas**     | 🔴 Critical (Blocking untuk seluruh fase Implementation)                 |
| **Fase SDLC**     | Fase 03 — Design                                                         |
| **Dokumen Utama** | Database Schema (DDL SQL)                                                |
| **Target File**   | `docs/sdlc/03_design/01_database_schema.sql`                            |
| **Status**        | 🔲 Open                                                                 |
| **Tanggal Dibuat**| 2026-05-24                                                               |
| **Estimasi**      | 1 sesi kerja penuh (≈ 3-5 jam)                                          |

---

## 1. Persona Pelaksana

**Persona yang ditugaskan**: **Senior Database Architect & DDL Implementation Specialist**

**Justifikasi pemilihan persona**:
- Dokumen ini adalah file DDL SQL (Data Definition Language) yang berisi perintah-perintah `CREATE DATABASE`, `CREATE TABLE`, `ALTER TABLE`, `CREATE INDEX`, dan `INSERT INTO` untuk inisialisasi skema basis data MySQL AbuCom.
- Persona ini memiliki otoritas dan keahlian teknis paling relevan dalam:
  - Menerjemahkan spesifikasi Data Dictionary (kamus data) menjadi sintaks DDL SQL yang presisi dan valid.
  - Memastikan integritas referensial (Foreign Key, ON DELETE, ON UPDATE) antar 28 tabel.
  - Menerapkan CHECK constraint, UNIQUE constraint, dan composite index sesuai standar praktik industri MySQL InnoDB.
  - Memastikan urutan pembuatan tabel (dependency order) agar tidak terjadi error referensi FK saat eksekusi.
  - Menyertakan seed data awal (INSERT) sesuai spesifikasi Data Dictionary.

---

## 2. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca dan dirangkum** sebelum memulai pengerjaan. File-file ini dipilih berdasarkan relevansi langsung terhadap kebutuhan spesifik dokumen Database Schema:

### 2.1. Referensi Primer (Wajib Baca Utama)

| No | File Referensi | Path Relatif | Alasan Pemilihan |
|----|----------------|--------------|------------------|
| 1  | **Data Dictionary v1.1** | `docs/sdlc/02_analysis/05_data_dictionary.md` | **Sumber utama paling kritis**. Berisi definisi lengkap 28 tabel, 282 kolom/atribut, tipe data MySQL, constraint (PK/FK/UQ/NN/AI/CK), default value, domain nilai, matriks relasi FK (58 entri), composite index, aturan bisnis data, formula komputasi, seed data awal, dan kebijakan retensi log. File ini adalah cetak biru (blueprint) tunggal yang harus diterjemahkan 1:1 menjadi sintaks DDL SQL. |
| 2  | **Access Control Matrix v1.1** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Berisi klasifikasi tingkat sensitivitas tabel (Sangat Sensitif, Sensitif, Operasional), matriks CRUD per tabel per role, dan aturan otorisasi eskalasi. Dibutuhkan untuk menambahkan komentar SQL (COMMENT) pada setiap tabel yang menjelaskan tingkat sensitivitas dan role yang berhak mengakses. |
| 3  | **Tech Stack Decision v1.1** | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Berisi konfigurasi teknis MySQL yang wajib dipatuhi: versi MySQL 8.0/8.4 LTS, engine InnoDB, charset utf8mb4, collation utf8mb4_unicode_ci, transaction isolation REPEATABLE READ, strategi schema.sql & seed.sql, serta konvensi parameterized queries. |

### 2.2. Referensi Sekunder (Pendukung Kontekstual)

| No | File Referensi | Path Relatif | Alasan Pemilihan |
|----|----------------|--------------|------------------|
| 4  | **Software Requirements Specification v1.1** | `docs/sdlc/02_analysis/02_software_requirements.md` | Untuk cross-check kode kebutuhan fungsional (SRS-F-xxx) yang dirujuk oleh setiap tabel di Data Dictionary, memastikan tidak ada kebutuhan fungsional yang terlewat. |
| 5  | **Business Requirements Document v1.1** | `docs/sdlc/02_analysis/01_business_requirements.md` | Untuk cross-check kode kebutuhan bisnis (BR-F-xx) dan memvalidasi aturan bisnis data (domain nilai, parameter default, formula). |

### 2.3. File yang TIDAK Dipilih

| File | Alasan Tidak Dipilih |
|------|---------------------|
| `docs/sdlc/narasi.txt` | Narasi sudah terabstraksi seluruhnya ke dalam dokumen BRD, SRS, dan Data Dictionary. Semua informasi yang dibutuhkan untuk DDL SQL sudah tersedia di file referensi primer di atas. Menggunakan narasi mentah berisiko menimbulkan inkonsistensi dengan spesifikasi yang sudah divalidasi. |
| Use Case Diagram & Workflow Diagram | Dokumen ini fokus pada alur interaksi aktor dan proses bisnis, bukan pada struktur fisik data. Informasi yang relevan sudah tercakup di Data Dictionary dan ACM. |
| Project Charter, Feasibility Study, Stakeholder Register, Innovation Proposal | Dokumen fase Planning ini sudah dikonsolidasi ke dalam dokumen fase Analysis. Tidak diperlukan lagi untuk pembuatan DDL SQL. |

---

## 3. Kerangka Struktur Dokumen Database Schema (DDL SQL)

Berikut adalah kerangka standar dokumen `01_database_schema.sql` yang harus diikuti. Kerangka ini mengikuti praktik industri standar untuk file inisialisasi database production-grade:

```
┌─────────────────────────────────────────────────────────┐
│  BAGIAN 0 — Header & Metadata Dokumen (SQL Comment)     │
│  ├── Informasi proyek, versi, tanggal, penyusun         │
│  ├── Riwayat perubahan dokumen                          │
│  ├── Deskripsi tujuan file                              │
│  ├── Prasyarat eksekusi                                 │
│  └── Instruksi cara menjalankan file ini                │
├─────────────────────────────────────────────────────────┤
│  BAGIAN 1 — Konfigurasi Awal & Pembuatan Database       │
│  ├── SET konfigurasi session MySQL                      │
│  ├── DROP DATABASE IF EXISTS (reset bersih)             │
│  ├── CREATE DATABASE dengan charset & collation         │
│  └── USE database                                       │
├─────────────────────────────────────────────────────────┤
│  BAGIAN 2 — Pembuatan Tabel (CREATE TABLE)              │
│  ├── Kelompok A: Tabel Induk/Master (tanpa FK)          │
│  │   └── cabang                                         │
│  ├── Kelompok B: Tabel Master Level 2 (FK ke cabang)    │
│  │   └── pengguna, pelanggan, supplier, barang,         │
│  │       saldo_ppob, saldo_ewallet, system_configs      │
│  ├── Kelompok C: Tabel Transaksional (FK ke master)     │
│  │   └── transaksi, detail_transaksi, antrian_kerja,    │
│  │       bom_komposisi, absensi, kasbon, payroll,       │
│  │       pengeluaran, limbah_produksi, poin_insentif,   │
│  │       jasa_service, shift_handover                   │
│  ├── Kelompok D: Tabel Administrasi & Keuangan          │
│  │   └── utang_supplier, pinjaman_bank,                 │
│  │       pinjaman_kerabat, aset                         │
│  ├── Kelompok E: Tabel Audit & Rekonsiliasi             │
│  │   └── audit_logs, backup_logs, stock_opname,         │
│  │       riwayat_harga_supplier                         │
│  └── (Setiap tabel disertai COMMENT pada tabel & kolom) │
├─────────────────────────────────────────────────────────┤
│  BAGIAN 3 — Pembuatan Index Tambahan (CREATE INDEX)     │
│  ├── idx_transaksi_tanggal_cabang                       │
│  ├── idx_absensi_pengguna_tanggal                       │
│  ├── idx_antrian_status_cabang                          │
│  └── idx_barang_tipe_cabang                             │
├─────────────────────────────────────────────────────────┤
│  BAGIAN 4 — Data Seed Awal (INSERT INTO)                │
│  ├── Seed cabang default (Toko Pusat Bandung)           │
│  ├── Seed pengguna default (akun pemilik)               │
│  ├── Seed saldo_ppob (2 akun PPOB)                     │
│  ├── Seed saldo_ewallet (6 akun e-wallet)              │
│  └── Seed system_configs (13 parameter bisnis)          │
├─────────────────────────────────────────────────────────┤
│  BAGIAN 5 — Verifikasi Integritas (Opsional)            │
│  ├── Query SHOW TABLES untuk validasi jumlah tabel      │
│  └── Query SELECT COUNT(*) untuk validasi seed data     │
├─────────────────────────────────────────────────────────┤
│  BAGIAN 6 — Footer & Referensi Dokumen (SQL Comment)    │
│  └── Daftar file referensi yang digunakan               │
└─────────────────────────────────────────────────────────┘
```

---

## 4. Instruksi Detail Tahapan Implementasi

> **PENTING**: Instruksi di bawah ini ditulis untuk dieksekusi oleh **junior programmer** atau **LLM model AI yang lebih murah**. Ikuti setiap langkah secara berurutan. Jangan melewati satupun checklist. Jangan berasumsi atau mengarang data yang tidak ada di file referensi.

---

### FASE A — Persiapan & Pembacaan File Referensi

> Tujuan: Memahami seluruh data dan informasi yang dibutuhkan sebelum menulis satu baris SQL pun.

- [ ] **A.1** — Buka dan baca file `docs/sdlc/02_analysis/05_data_dictionary.md` dari baris pertama hingga baris terakhir secara menyeluruh.
- [ ] **A.2** — Dari Data Dictionary, rangkum dan catat informasi berikut (jangan sampai ada yang terlewat):
  - [ ] A.2.1 — Daftar lengkap 28 nama tabel beserta deskripsi singkatnya (Bab 2.1).
  - [ ] A.2.2 — Diagram ER Konseptual Mermaid (Bab 2.2) — pahami relasi antar tabel.
  - [ ] A.2.3 — Spesifikasi detail setiap tabel (Bab 3.1 s.d 3.28): nama kolom, tipe data MySQL, constraint (PK/FK/UQ/NN/AI/CK), nullable, default value, dan catatan implementasi.
  - [ ] A.2.4 — Table-Level Constraints & Checks untuk setiap tabel yang memilikinya (contoh: CHECK constraint pada `barang.harga_beli >= 0`, UNIQUE composite pada `bom_komposisi`, dll).
  - [ ] A.2.5 — Seluruh 19 kamus domain nilai / Value Domain (Bab 4.1 s.d 4.19) — pahami nilai-nilai ENUM/status yang valid untuk setiap kolom.
  - [ ] A.2.6 — Matriks relasi Foreign Key lengkap 58 entri (Bab 5.1): tabel asal, kolom FK, tabel referensi, kolom referensi, tipe relasi, ON DELETE, ON UPDATE.
  - [ ] A.2.7 — Aturan constraint integritas referensial (Bab 5.3): ON DELETE RESTRICT, CASCADE, SET NULL.
  - [ ] A.2.8 — Aturan bisnis data (Bab 6): validasi input, formula komputasi, constraint database, default value.
  - [ ] A.2.9 — Daftar Primary Key, Unique Constraint, dan 4 rekomendasi Composite Index (Bab 7).
  - [ ] A.2.10 — Spesifikasi Data Seed Awal Minimum (Bab 11.1): seed cabang, pengguna, saldo_ppob, saldo_ewallet, system_configs.
  - [ ] A.2.11 — Kebijakan retensi data log audit (Bab 11.2).
- [ ] **A.3** — Buka dan baca file `docs/sdlc/02_analysis/06_access_control_matrix.md`. Rangkum informasi berikut:
  - [ ] A.3.1 — Klasifikasi tingkat sensitivitas 28 tabel database (Bab 3.2): Sangat Sensitif, Sensitif, Operasional.
  - [ ] A.3.2 — Matriks CRUD per tabel per role (Bab 5.2) — untuk menambahkan komentar SQL informatif.
- [ ] **A.4** — Buka dan baca file `docs/sdlc/01_planning/04_tech_stack_decision.md`. Rangkum informasi berikut:
  - [ ] A.4.1 — Konfigurasi database MySQL yang wajib: versi MySQL 8.0/8.4 LTS, engine InnoDB, charset utf8mb4, collation utf8mb4_unicode_ci (Bab 4.1).
  - [ ] A.4.2 — Strategi schema.sql & seed.sql (Bab 9.5).
  - [ ] A.4.3 — Strategi keamanan audit trail (Bab 8.4).
- [ ] **A.5** — (Opsional) Buka file `docs/sdlc/02_analysis/02_software_requirements.md` untuk cross-check kode SRS-F-xxx jika ada keraguan pada referensi kode kebutuhan fungsional.
- [ ] **A.6** — (Opsional) Buka file `docs/sdlc/02_analysis/01_business_requirements.md` untuk cross-check kode BR-F-xx jika ada keraguan pada aturan bisnis data.

---

### FASE B — Penyusunan Bagian 0: Header & Metadata Dokumen

> Tujuan: Menulis blok komentar SQL di bagian paling atas file yang berisi informasi identitas dokumen.

- [ ] **B.1** — Tulis blok komentar SQL multi-baris (`-- ` atau `/* */`) di awal file `01_database_schema.sql` yang berisi:
  - [ ] B.1.1 — Nama dokumen: `Database Schema (DDL SQL)`
  - [ ] B.1.2 — Nama proyek: `AbuCom — Sistem Manajemen Terpadu Usaha Percetakan`
  - [ ] B.1.3 — Versi dokumen: `1.0`
  - [ ] B.1.4 — Tanggal pembuatan
  - [ ] B.1.5 — Penyusun: `Senior Database Architect & DDL Implementation Specialist`
  - [ ] B.1.6 — Status dokumen: `Draft`
  - [ ] B.1.7 — Deskripsi singkat tujuan file ini (1-2 kalimat)
  - [ ] B.1.8 — Prasyarat eksekusi: MySQL Server 8.0/8.4 LTS harus sudah terinstal dan berjalan
  - [ ] B.1.9 — Instruksi cara menjalankan: `mysql -u root -p < 01_database_schema.sql`
  - [ ] B.1.10 — Tabel riwayat perubahan dokumen dalam format komentar SQL

---

### FASE C — Penyusunan Bagian 1: Konfigurasi Awal & Pembuatan Database

> Tujuan: Menulis perintah SQL untuk konfigurasi session dan pembuatan database.

- [ ] **C.1** — Tulis komentar pemisah bagian: `-- ============================================================`
- [ ] **C.2** — Tulis perintah `SET` untuk konfigurasi session MySQL:
  - [ ] C.2.1 — `SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;`
  - [ ] C.2.2 — `SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;`
  - [ ] C.2.3 — `SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION';`
  - [ ] C.2.4 — `SET NAMES utf8mb4;`
- [ ] **C.3** — Tulis perintah `DROP DATABASE IF EXISTS abucom;`
- [ ] **C.4** — Tulis perintah `CREATE DATABASE abucom CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;`
- [ ] **C.5** — Tulis perintah `USE abucom;`

---

### FASE D — Penyusunan Bagian 2: Pembuatan Tabel (CREATE TABLE)

> Tujuan: Menulis perintah CREATE TABLE untuk seluruh 28 tabel dengan urutan dependency yang benar.
>
> **ATURAN KRITIS**:
> - Urutan pembuatan tabel HARUS mengikuti dependency FK. Tabel induk (parent) dibuat terlebih dahulu sebelum tabel anak (child).
> - Setiap tabel WAJIB menggunakan `ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci`.
> - Setiap tabel WAJIB memiliki komentar `COMMENT='...'` yang menjelaskan deskripsi dan tingkat sensitivitas.
> - Setiap kolom harus ditulis PERSIS sesuai spesifikasi Data Dictionary: nama, tipe data, constraint, nullable, default.
> - Setiap FOREIGN KEY harus ditulis dengan `CONSTRAINT fk_[tabel_anak]_[kolom_fk]` beserta `ON DELETE` dan `ON UPDATE` sesuai matriks FK Data Dictionary Bab 5.1.
> - Setiap CHECK constraint harus ditulis sesuai Data Dictionary.
> - Setiap UNIQUE constraint (termasuk composite) harus ditulis sesuai Data Dictionary.

#### Kelompok A — Tabel Induk (Tanpa Foreign Key)

- [ ] **D.1** — Tulis `CREATE TABLE cabang` (6 kolom) sesuai Data Dictionary Bab 3.1.
  - [ ] D.1.1 — Pastikan `id` adalah `INT NOT NULL AUTO_INCREMENT PRIMARY KEY`.
  - [ ] D.1.2 — Pastikan `nama_cabang` memiliki `UNIQUE`.
  - [ ] D.1.3 — Pastikan `created_at` default `CURRENT_TIMESTAMP`.
  - [ ] D.1.4 — Pastikan `updated_at` default `CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP`.
  - [ ] D.1.5 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Operasional).

#### Kelompok B — Tabel Master Level 2 (FK ke cabang)

- [ ] **D.2** — Tulis `CREATE TABLE pengguna` (10 kolom) sesuai Data Dictionary Bab 3.2.
  - [ ] D.2.1 — Pastikan `username` memiliki `UNIQUE`.
  - [ ] D.2.2 — Pastikan `failed_login_attempts` memiliki `DEFAULT 0` dan CHECK `BETWEEN 0 AND 5`.
  - [ ] D.2.3 — Pastikan `locked_until` nullable (`NULL`).
  - [ ] D.2.4 — Pastikan `cabang_id` memiliki FK ke `cabang(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE` dan `DEFAULT 1`.
  - [ ] D.2.5 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Operasional).
- [ ] **D.3** — Tulis `CREATE TABLE pelanggan` (7 kolom) sesuai Data Dictionary Bab 3.3.
  - [ ] D.3.1 — Pastikan `whatsapp` memiliki `UNIQUE`.
  - [ ] D.3.2 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.3.3 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Operasional).
- [ ] **D.4** — Tulis `CREATE TABLE supplier` (7 kolom) sesuai Data Dictionary Bab 3.4.
  - [ ] D.4.1 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.4.2 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Operasional).
- [ ] **D.5** — Tulis `CREATE TABLE barang` (13 kolom) sesuai Data Dictionary Bab 3.5.
  - [ ] D.5.1 — Pastikan seluruh 5 CHECK constraint: `harga_beli >= 0`, `harga_retail >= 0`, `harga_grosir >= 0`, `harga_mitra >= 0`, `min_grosir > 0`.
  - [ ] D.5.2 — Pastikan `stok_saat_ini` tipe `DECIMAL(15,4)` dengan default `0.0000`.
  - [ ] D.5.3 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.5.4 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Operasional).
- [ ] **D.6** — Tulis `CREATE TABLE saldo_ppob` (7 kolom) sesuai Data Dictionary Bab 3.16.
  - [ ] D.6.1 — Pastikan `akun_tipe` memiliki `UNIQUE`.
  - [ ] D.6.2 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.6.3 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Operasional).
- [ ] **D.7** — Tulis `CREATE TABLE saldo_ewallet` (9 kolom) sesuai Data Dictionary Bab 3.27.
  - [ ] D.7.1 — Pastikan `nama_ewallet` memiliki `UNIQUE`.
  - [ ] D.7.2 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.7.3 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Operasional).
- [ ] **D.8** — Tulis `CREATE TABLE system_configs` (8 kolom) sesuai Data Dictionary Bab 3.28.
  - [ ] D.8.1 — Pastikan `parameter_key` memiliki `UNIQUE`.
  - [ ] D.8.2 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.8.3 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sangat Sensitif).

#### Kelompok C — Tabel Transaksional (FK ke tabel master)

- [ ] **D.9** — Tulis `CREATE TABLE bom_komposisi` (7 kolom) sesuai Data Dictionary Bab 3.6.
  - [ ] D.9.1 — Pastikan UNIQUE composite `(barang_induk_id, bahan_baku_id)`.
  - [ ] D.9.2 — Pastikan FK `barang_induk_id` ke `barang(id)` dengan `ON DELETE CASCADE ON UPDATE CASCADE`.
  - [ ] D.9.3 — Pastikan FK `bahan_baku_id` ke `barang(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.9.4 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.9.5 — Tambahkan `COMMENT` pada tabel.
- [ ] **D.10** — Tulis `CREATE TABLE transaksi` (14 kolom) sesuai Data Dictionary Bab 3.7.
  - [ ] D.10.1 — Pastikan `no_invoice` memiliki `UNIQUE`.
  - [ ] D.10.2 — Pastikan `pelanggan_id` nullable (FK ke `pelanggan(id)` dengan `ON DELETE SET NULL`).
  - [ ] D.10.3 — Pastikan `kasir_id` FK ke `pengguna(id)` dengan `ON DELETE RESTRICT`.
  - [ ] D.10.4 — Pastikan CHECK: `total_bayar >= 0`, `dp_bayar >= 0 AND dp_bayar <= total_bayar`.
  - [ ] D.10.5 — Pastikan default value: `status_pembayaran='BELUM LUNAS'`, `status_pengambilan='BELUM DIAMBIL'`, `metode_pembayaran='Kas'`, `tipe_pelanggan='Retail'`.
  - [ ] D.10.6 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.10.7 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sensitif).
- [ ] **D.11** — Tulis `CREATE TABLE detail_transaksi` (9 kolom) sesuai Data Dictionary Bab 3.8.
  - [ ] D.11.1 — Pastikan FK `transaksi_id` ke `transaksi(id)` dengan `ON DELETE CASCADE ON UPDATE CASCADE`.
  - [ ] D.11.2 — Pastikan FK `barang_id` ke `barang(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.11.3 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.11.4 — Tambahkan `COMMENT` pada tabel.
- [ ] **D.12** — Tulis `CREATE TABLE antrian_kerja` (11 kolom) sesuai Data Dictionary Bab 3.9.
  - [ ] D.12.1 — Pastikan FK `transaksi_id` ke `transaksi(id)` dengan `ON DELETE CASCADE ON UPDATE CASCADE`.
  - [ ] D.12.2 — Pastikan `desainer_id` dan `produksi_id` nullable (FK ke `pengguna(id)` dengan `ON DELETE SET NULL`).
  - [ ] D.12.3 — Pastikan `path_desain` default `''` (string kosong).
  - [ ] D.12.4 — Pastikan `timestamp_selesai` nullable.
  - [ ] D.12.5 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.12.6 — Tambahkan `COMMENT` pada tabel.
- [ ] **D.13** — Tulis `CREATE TABLE absensi` (7 kolom) sesuai Data Dictionary Bab 3.10.
  - [ ] D.13.1 — Pastikan UNIQUE composite `(pengguna_id, tanggal)`.
  - [ ] D.13.2 — Pastikan FK `pengguna_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.13.3 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.13.4 — Tambahkan `COMMENT` pada tabel.
- [ ] **D.14** — Tulis `CREATE TABLE kasbon` (10 kolom) sesuai Data Dictionary Bab 3.11.
  - [ ] D.14.1 — Pastikan CHECK: `nominal_pinjaman > 0`, `sisa_utang >= 0 AND sisa_utang <= nominal_pinjaman`, `cicilan_per_bulan >= 0`.
  - [ ] D.14.2 — Pastikan default `status_kasbon='AKTIF'`.
  - [ ] D.14.3 — Pastikan FK `pengguna_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.14.4 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.14.5 — Tambahkan `COMMENT` pada tabel.
- [ ] **D.15** — Tulis `CREATE TABLE payroll` (12 kolom) sesuai Data Dictionary Bab 3.12.
  - [ ] D.15.1 — Pastikan CHECK: `gaji_pokok >= 0`, `bonus_insentif >= 0`, `potongan_kasbon >= 0`, `gaji_bersih >= 0`.
  - [ ] D.15.2 — Pastikan `metode_bayar_gaji` default `'Tunai'`.
  - [ ] D.15.3 — Pastikan FK `pengguna_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.15.4 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.15.5 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sangat Sensitif).
- [ ] **D.16** — Tulis `CREATE TABLE pengeluaran` (10 kolom) sesuai Data Dictionary Bab 3.13.
  - [ ] D.16.1 — Pastikan `disetujui_pemilik` tipe `BOOLEAN` default `FALSE`.
  - [ ] D.16.2 — Pastikan FK `kasir_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.16.3 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.16.4 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sensitif).
- [ ] **D.17** — Tulis `CREATE TABLE limbah_produksi` (11 kolom) sesuai Data Dictionary Bab 3.15.
  - [ ] D.17.1 — Pastikan FK `transaksi_id` ke `transaksi(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.17.2 — Pastikan FK `bahan_baku_id` ke `barang(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.17.3 — Pastikan FK `produksi_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.17.4 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.17.5 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sensitif).
- [ ] **D.18** — Tulis `CREATE TABLE jasa_service` (13 kolom) sesuai Data Dictionary Bab 3.17.
  - [ ] D.18.1 — Pastikan `pelanggan_id` nullable (FK ke `pelanggan(id)` dengan `ON DELETE SET NULL`).
  - [ ] D.18.2 — Pastikan `nama_non_pelanggan` nullable.
  - [ ] D.18.3 — Pastikan `tanggal_selesai` nullable.
  - [ ] D.18.4 — Pastikan FK `teknisi_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.18.5 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.18.6 — Tambahkan `COMMENT` pada tabel.
- [ ] **D.19** — Tulis `CREATE TABLE poin_insentif` (10 kolom) sesuai Data Dictionary Bab 3.18.
  - [ ] D.19.1 — Pastikan FK `transaksi_id` ke `transaksi(id)` dengan `ON DELETE CASCADE ON UPDATE CASCADE`.
  - [ ] D.19.2 — Pastikan FK `pengguna_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.19.3 — Pastikan `status_poin` default `'AKTIF'`.
  - [ ] D.19.4 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.19.5 — Tambahkan `COMMENT` pada tabel.
- [ ] **D.20** — Tulis `CREATE TABLE shift_handover` (14 kolom) sesuai Data Dictionary Bab 3.19.
  - [ ] D.20.1 — Pastikan FK `kasir_keluar_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.20.2 — Pastikan FK `kasir_masuk_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.20.3 — Pastikan FK `supervisor_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.20.4 — Pastikan `catatan_alasan` nullable.
  - [ ] D.20.5 — Pastikan `status_handover` default `'NORMAL'`.
  - [ ] D.20.6 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.20.7 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sensitif).

#### Kelompok D — Tabel Administrasi & Keuangan

- [ ] **D.21** — Tulis `CREATE TABLE utang_supplier` (11 kolom) sesuai Data Dictionary Bab 3.20.
  - [ ] D.21.1 — Pastikan CHECK: `nominal_utang > 0`, `sisa_utang >= 0 AND sisa_utang <= nominal_utang`.
  - [ ] D.21.2 — Pastikan `tanggal_pelunasan` nullable.
  - [ ] D.21.3 — Pastikan `status_utang` default `'BELUM LUNAS'`.
  - [ ] D.21.4 — Pastikan FK `supplier_id` ke `supplier(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.21.5 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.21.6 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sensitif).
- [ ] **D.22** — Tulis `CREATE TABLE pinjaman_bank` (14 kolom) sesuai Data Dictionary Bab 3.22.
  - [ ] D.22.1 — Pastikan `status_pinjaman` default `'BELUM LUNAS'`.
  - [ ] D.22.2 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.22.3 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sangat Sensitif).
- [ ] **D.23** — Tulis `CREATE TABLE pinjaman_kerabat` (10 kolom) sesuai Data Dictionary Bab 3.23.
  - [ ] D.23.1 — Pastikan `tanggal_pengembalian` nullable.
  - [ ] D.23.2 — Pastikan `status_pinjaman` default `'BELUM LUNAS'`.
  - [ ] D.23.3 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.23.4 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sangat Sensitif).
- [ ] **D.24** — Tulis `CREATE TABLE aset` (13 kolom) sesuai Data Dictionary Bab 3.24.
  - [ ] D.24.1 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.24.2 — Tambahkan `COMMENT` pada tabel.

#### Kelompok E — Tabel Audit & Rekonsiliasi

- [ ] **D.25** — Tulis `CREATE TABLE audit_logs` (10 kolom) sesuai Data Dictionary Bab 3.14.
  - [ ] D.25.1 — Pastikan `old_value` dan `new_value` bertipe `JSON` dan nullable.
  - [ ] D.25.2 — Pastikan FK `pengguna_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.25.3 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.25.4 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sangat Sensitif).
- [ ] **D.26** — Tulis `CREATE TABLE backup_logs` (8 kolom) sesuai Data Dictionary Bab 3.21.
  - [ ] D.26.1 — Pastikan FK `pengguna_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.26.2 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.26.3 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sangat Sensitif).
- [ ] **D.27** — Tulis `CREATE TABLE stock_opname` (13 kolom) sesuai Data Dictionary Bab 3.25.
  - [ ] D.27.1 — Pastikan `status_opname` default `'DRAFT'`.
  - [ ] D.27.2 — Pastikan `supervisor_id` nullable (FK ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`).
  - [ ] D.27.3 — Pastikan `catatan_opname` nullable.
  - [ ] D.27.4 — Pastikan FK `barang_id` ke `barang(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.27.5 — Pastikan FK `user_id` ke `pengguna(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.27.6 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.27.7 — Tambahkan `COMMENT` pada tabel: deskripsi + tingkat sensitivitas (Sensitif).
- [ ] **D.28** — Tulis `CREATE TABLE riwayat_harga_supplier` (8 kolom) sesuai Data Dictionary Bab 3.26.
  - [ ] D.28.1 — Pastikan FK `barang_id` ke `barang(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.28.2 — Pastikan FK `supplier_id` ke `supplier(id)` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.28.3 — Pastikan FK `cabang_id` dengan `ON DELETE RESTRICT ON UPDATE CASCADE`.
  - [ ] D.28.4 — Tambahkan `COMMENT` pada tabel.

---

### FASE E — Penyusunan Bagian 3: Pembuatan Index Tambahan

> Tujuan: Menulis perintah CREATE INDEX untuk 4 composite index yang direkomendasikan di Data Dictionary Bab 7.3.

- [ ] **E.1** — Tulis komentar pemisah bagian index.
- [ ] **E.2** — Tulis `CREATE INDEX idx_transaksi_tanggal_cabang ON transaksi(tanggal_transaksi, cabang_id);`
- [ ] **E.3** — Tulis `CREATE INDEX idx_absensi_pengguna_tanggal ON absensi(pengguna_id, tanggal);`
  - Catatan: UNIQUE composite sudah dibuat di CREATE TABLE. Index ini bersifat tambahan jika belum tercakup oleh UNIQUE constraint.
- [ ] **E.4** — Tulis `CREATE INDEX idx_antrian_status_cabang ON antrian_kerja(status_antrian, cabang_id);`
- [ ] **E.5** — Tulis `CREATE INDEX idx_barang_tipe_cabang ON barang(tipe_barang, cabang_id);`

---

### FASE F — Penyusunan Bagian 4: Data Seed Awal (INSERT INTO)

> Tujuan: Menulis perintah INSERT INTO untuk data awal minimum sesuai Data Dictionary Bab 11.1.
>
> **ATURAN KRITIS**: Gunakan data PERSIS seperti yang tertulis di Data Dictionary Bab 11.1. Jangan mengarang atau mengubah nilai seed data.

- [ ] **F.1** — Tulis komentar pemisah bagian seed data.
- [ ] **F.2** — Tulis `INSERT INTO cabang` dengan data:
  - `id=1`, `nama_cabang='Toko Pusat Bandung'`, `alamat='Jl. Raya Percetakan No. 45, RT 02/RW 03, Kecamatan Sukamaju, Kota Bandung, Jawa Barat, 40123'`, `telp='0227654321'`.
- [ ] **F.3** — Tulis `INSERT INTO pengguna` dengan data:
  - `id=1`, `nama_lengkap='Pemilik Usaha AbuCom'`, `username='pemilik'`, `password_hash='$2b$12$K3h8jD8sS9fJ2gK3l8h9oOa8fS8jK9l8g7h6j5k4l3m2n1o0p9q8r'`, `role='pemilik'`, `failed_login_attempts=0`, `locked_until=NULL`, `cabang_id=1`.
- [ ] **F.4** — Tulis `INSERT INTO saldo_ppob` dengan 2 baris data:
  - Baris 1: `akun_tipe='Pulsa_Data'`, `saldo_terakhir=1000000.0000`, `cabang_id=1`.
  - Baris 2: `akun_tipe='Token_Tagihan'`, `saldo_terakhir=1500000.0000`, `cabang_id=1`.
- [ ] **F.5** — Tulis `INSERT INTO saldo_ewallet` dengan 6 baris data sesuai Data Dictionary:
  - Baris 1: `nama_ewallet='Mandiri Agen'`, `saldo_terakhir=2000000.0000`, `biaya_admin_flat=3000.0000`, `biaya_admin_persen=0.0000`, `limit_harian=50000000.0000`, `cabang_id=1`.
  - Baris 2: `nama_ewallet='Dana'`, `saldo_terakhir=1000000.0000`, `biaya_admin_flat=1000.0000`, `biaya_admin_persen=0.0000`, `limit_harian=10000000.0000`, `cabang_id=1`.
  - Baris 3: `nama_ewallet='Gopay'`, `saldo_terakhir=1000000.0000`, `biaya_admin_flat=1000.0000`, `biaya_admin_persen=0.0000`, `limit_harian=10000000.0000`, `cabang_id=1`.
  - Baris 4: `nama_ewallet='LinkAja'`, `saldo_terakhir=1000000.0000`, `biaya_admin_flat=1000.0000`, `biaya_admin_persen=0.0000`, `limit_harian=10000000.0000`, `cabang_id=1`.
  - Baris 5: `nama_ewallet='ShopeePay'`, `saldo_terakhir=1000000.0000`, `biaya_admin_flat=1000.0000`, `biaya_admin_persen=0.0000`, `limit_harian=10000000.0000`, `cabang_id=1`.
  - Baris 6: `nama_ewallet='OVO'`, `saldo_terakhir=1000000.0000`, `biaya_admin_flat=1000.0000`, `biaya_admin_persen=0.0000`, `limit_harian=10000000.0000`, `cabang_id=1`.
- [ ] **F.6** — Tulis `INSERT INTO system_configs` dengan 13 baris data sesuai Data Dictionary Bab 6.4:
  - [ ] F.6.1 — `parameter_key='target_laba_payroll'`, `parameter_value='15000000.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Target laba bersih bulanan untuk skema gaji tetap (Skenario A Smart Payroll)'`, `cabang_id=1`.
  - [ ] F.6.2 — `parameter_key='porsi_gaji_laba'`, `parameter_value='0.2500'`, `tipe_data='DECIMAL'`, `deskripsi='Persentase alokasi laba bersih untuk pool gaji karyawan (Skenario B Smart Payroll)'`, `cabang_id=1`.
  - [ ] F.6.3 — `parameter_key='limit_kasbon_staf'`, `parameter_value='1000000.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Pagu maksimal utang kasbon aktif kumulatif per staf'`, `cabang_id=1`.
  - [ ] F.6.4 — `parameter_key='threshold_saldo_ppob'`, `parameter_value='150000.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Batas saldo minimum PPOB yang memicu alert deposit'`, `cabang_id=1`.
  - [ ] F.6.5 — `parameter_key='min_topup_ppob'`, `parameter_value='500000.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Nominal minimum deposit topup saldo PPOB'`, `cabang_id=1`.
  - [ ] F.6.6 — `parameter_key='toleransi_selisih_kas'`, `parameter_value='10000.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Batas toleransi selisih kas kasir sebelum status ANOMALI'`, `cabang_id=1`.
  - [ ] F.6.7 — `parameter_key='poin_tier_1_rupiah'`, `parameter_value='500.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Nilai rupiah per poin insentif Tier 1 (transaksi mudah)'`, `cabang_id=1`.
  - [ ] F.6.8 — `parameter_key='poin_tier_2_rupiah'`, `parameter_value='1500.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Nilai rupiah per poin insentif Tier 2 (jasa dasar)'`, `cabang_id=1`.
  - [ ] F.6.9 — `parameter_key='poin_tier_3_rupiah'`, `parameter_value='2500.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Nilai rupiah per poin insentif Tier 3 (produk kustom)'`, `cabang_id=1`.
  - [ ] F.6.10 — `parameter_key='poin_tier_4_rupiah'`, `parameter_value='5000.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Nilai rupiah per poin insentif Tier 4 (pekerjaan berat/teknis)'`, `cabang_id=1`.
  - [ ] F.6.11 — `parameter_key='threshold_pengeluaran'`, `parameter_value='500000.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Batas nominal pengeluaran yang memerlukan otorisasi pemilik'`, `cabang_id=1`.
  - [ ] F.6.12 — `parameter_key='umr_daerah'`, `parameter_value='3200000.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Upah Minimum Regional daerah sebagai batas proteksi gaji minimum staf'`, `cabang_id=1`.
  - [ ] F.6.13 — `parameter_key='dana_cadangan_darurat'`, `parameter_value='4500000.0000'`, `tipe_data='DECIMAL'`, `deskripsi='Cadangan kas darurat minimal yang harus dijaga di laci kasir'`, `cabang_id=1`.

---

### FASE G — Penyusunan Bagian 5: Verifikasi Integritas

> Tujuan: Menambahkan query verifikasi sederhana di akhir file untuk memastikan semua tabel dan seed data berhasil dibuat.

- [ ] **G.1** — Tulis komentar pemisah bagian verifikasi.
- [ ] **G.2** — Tulis query `SHOW TABLES;` disertai komentar: `-- Hasil yang diharapkan: 28 tabel`.
- [ ] **G.3** — Tulis query `SELECT COUNT(*) AS total_cabang FROM cabang;` disertai komentar: `-- Hasil yang diharapkan: 1`.
- [ ] **G.4** — Tulis query `SELECT COUNT(*) AS total_pengguna FROM pengguna;` disertai komentar: `-- Hasil yang diharapkan: 1`.
- [ ] **G.5** — Tulis query `SELECT COUNT(*) AS total_saldo_ppob FROM saldo_ppob;` disertai komentar: `-- Hasil yang diharapkan: 2`.
- [ ] **G.6** — Tulis query `SELECT COUNT(*) AS total_saldo_ewallet FROM saldo_ewallet;` disertai komentar: `-- Hasil yang diharapkan: 6`.
- [ ] **G.7** — Tulis query `SELECT COUNT(*) AS total_system_configs FROM system_configs;` disertai komentar: `-- Hasil yang diharapkan: 13`.

---

### FASE H — Penyusunan Bagian 6: Restorasi Konfigurasi & Footer

> Tujuan: Mengembalikan konfigurasi MySQL session dan menambahkan referensi dokumen.

- [ ] **H.1** — Tulis perintah restorasi konfigurasi session:
  - [ ] H.1.1 — `SET SQL_MODE=@OLD_SQL_MODE;`
  - [ ] H.1.2 — `SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;`
  - [ ] H.1.3 — `SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;`
- [ ] **H.2** — Tulis blok komentar SQL footer yang berisi daftar referensi dokumen yang digunakan:
  ```
  -- ============================================================
  -- REFERENSI DOKUMEN
  -- ============================================================
  -- File ini disusun berdasarkan referensi dari dokumen-dokumen berikut:
  --
  -- [REF-01] Data Dictionary v1.1
  --          Path: docs/sdlc/02_analysis/05_data_dictionary.md
  --          Kontribusi: Sumber utama definisi 28 tabel, 282 kolom, constraint,
  --                      matriks FK, domain nilai, seed data, dan aturan bisnis.
  --
  -- [REF-02] Access Control Matrix v1.1
  --          Path: docs/sdlc/02_analysis/06_access_control_matrix.md
  --          Kontribusi: Klasifikasi tingkat sensitivitas tabel dan matriks CRUD.
  --
  -- [REF-03] Tech Stack Decision v1.1
  --          Path: docs/sdlc/01_planning/04_tech_stack_decision.md
  --          Kontribusi: Konfigurasi MySQL (engine, charset, collation) dan
  --                      strategi inisialisasi schema.sql.
  --
  -- [REF-04] Software Requirements Specification v1.1
  --          Path: docs/sdlc/02_analysis/02_software_requirements.md
  --          Kontribusi: Cross-check kode kebutuhan fungsional (SRS-F-xxx).
  --
  -- [REF-05] Business Requirements Document v1.1
  --          Path: docs/sdlc/02_analysis/01_business_requirements.md
  --          Kontribusi: Cross-check aturan bisnis dan domain nilai (BR-F-xx).
  -- ============================================================
  ```

---

### FASE I — Penulisan ke Target File

> Tujuan: Memastikan semua hasil pengerjaan ditulis ke target file yang sudah ditentukan.

- [ ] **I.1** — Tuangkan SELURUH hasil pengerjaan dari Fase B hingga Fase H ke dalam satu file utuh: `docs/sdlc/03_design/01_database_schema.sql`.
- [ ] **I.2** — Pastikan file menggunakan encoding **UTF-8 tanpa BOM**.
- [ ] **I.3** — Pastikan setiap baris perintah SQL diakhiri dengan tanda titik koma (`;`).
- [ ] **I.4** — Pastikan komentar pemisah antar bagian menggunakan format yang konsisten (contoh: `-- ============================================================`).
- [ ] **I.5** — Pastikan tidak ada karakter khusus atau invisible character yang masuk ke dalam file.

---

### FASE J — Validasi & Review Akhir

> Tujuan: Melakukan pengecekan kualitas akhir sebelum dokumen dinyatakan selesai.

- [ ] **J.1** — Hitung ulang jumlah statement `CREATE TABLE` di dalam file. **Harus berjumlah tepat 28**.
- [ ] **J.2** — Hitung ulang jumlah statement `CREATE INDEX` (non-PK, non-UNIQUE). **Harus berjumlah minimal 4**.
- [ ] **J.3** — Hitung ulang jumlah statement `INSERT INTO`. **Harus mencakup 5 tabel seed** (cabang, pengguna, saldo_ppob, saldo_ewallet, system_configs).
- [ ] **J.4** — Verifikasi bahwa urutan `CREATE TABLE` tidak menimbulkan error referensi FK (tabel parent selalu dibuat sebelum tabel child).
- [ ] **J.5** — Verifikasi bahwa setiap kolom `cabang_id` pada 28 tabel memiliki `DEFAULT 1` dan FK ke `cabang(id)`.
- [ ] **J.6** — Verifikasi bahwa setiap tabel memiliki kolom `created_at` dan `updated_at` dengan default timestamp.
- [ ] **J.7** — Verifikasi bahwa semua CHECK constraint yang disebutkan di Data Dictionary sudah tertulis.
- [ ] **J.8** — Verifikasi bahwa semua UNIQUE constraint (termasuk composite) sudah tertulis.
- [ ] **J.9** — Jika ada data atau informasi yang **tidak tersedia** di file referensi dan tidak bisa diputuskan sendiri, tandai dengan komentar SQL: `-- [TODO: DATA KOSONG] Deskripsi apa yang perlu diisi manual`.
- [ ] **J.10** — Lakukan pembacaan ulang akhir keseluruhan file dari baris pertama hingga baris terakhir untuk memastikan tidak ada typo, syntax error SQL, atau inkonsistensi.

---

## 5. Instruksi Tambahan Khas Dokumen DDL SQL

Berikut adalah instruksi tambahan yang relevan secara spesifik dengan ciri khas dokumen DDL SQL dan standar industri yang mungkin belum tercakup dalam kriteria di atas:

### 5.1. Konvensi Penamaan Constraint
- Semua FOREIGN KEY diberi nama eksplisit dengan pola: `CONSTRAINT fk_[nama_tabel_anak]_[nama_kolom_fk]`.
  - Contoh: `CONSTRAINT fk_pengguna_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id)`.
- Semua CHECK constraint diberi nama eksplisit dengan pola: `CONSTRAINT chk_[nama_tabel]_[nama_kolom]`.
  - Contoh: `CONSTRAINT chk_barang_harga_beli CHECK (harga_beli >= 0)`.
- Semua UNIQUE composite constraint diberi nama eksplisit dengan pola: `CONSTRAINT uq_[nama_tabel]_[deskripsi]`.
  - Contoh: `CONSTRAINT uq_bom_induk_bahan UNIQUE (barang_induk_id, bahan_baku_id)`.

### 5.2. Komentar SQL pada Kolom
- Setiap kolom WAJIB memiliki `COMMENT 'deskripsi bisnis singkat'` yang diambil dari kolom "Deskripsi Bisnis" di Data Dictionary.
- Contoh: `nama_cabang VARCHAR(100) NOT NULL UNIQUE COMMENT 'Nama unik dari unit cabang usaha fisik'`.

### 5.3. Komentar SQL pada Tabel
- Setiap tabel WAJIB memiliki `COMMENT='Deskripsi tabel | Sensitivitas: [Level] | Modul: [Kode Modul]'`.
- Contoh: `COMMENT='Data cabang toko fisik AbuCom multi-branch | Sensitivitas: Operasional | Modul: M.9'`.

### 5.4. Pemisahan Visual Bagian
- Gunakan komentar blok pemisah yang jelas antar bagian utama dan antar kelompok tabel.
- Gunakan komentar sub-header sebelum setiap `CREATE TABLE` yang mencantumkan nomor urut tabel dan deskripsi singkat.

### 5.5. Idempoten File
- File DDL ini harus bersifat **idempoten** (aman dijalankan berulang kali). Gunakan `DROP DATABASE IF EXISTS` di awal untuk memastikan eksekusi ulang tidak error.

### 5.6. Hindari Penggunaan ENUM
- Meskipun domain nilai memiliki pilihan terbatas, JANGAN menggunakan tipe data `ENUM` MySQL. Gunakan `VARCHAR(n)` sesuai spesifikasi Data Dictionary. Validasi domain nilai dilakukan di sisi aplikasi Python, bukan di sisi database.

### 5.7. Perhatikan Presisi Desimal
- Semua kolom yang menyimpan nominal uang dan kuantitas desimal WAJIB menggunakan tipe `DECIMAL(15,4)` sesuai spesifikasi Data Dictionary. JANGAN menggunakan `FLOAT` atau `DOUBLE`.

---

## 6. Kriteria Penerimaan (Acceptance Criteria)

Issue ini dinyatakan **selesai (Done)** jika dan hanya jika:

| No | Kriteria | Status |
|----|----------|--------|
| 1 | File `docs/sdlc/03_design/01_database_schema.sql` berisi konten DDL SQL lengkap yang tidak kosong. | ⬜ |
| 2 | File berisi tepat **28 statement CREATE TABLE** yang mencakup seluruh tabel di Data Dictionary. | ⬜ |
| 3 | Urutan CREATE TABLE mengikuti dependency FK (parent sebelum child). | ⬜ |
| 4 | Semua FOREIGN KEY, CHECK, UNIQUE constraint tertulis sesuai Data Dictionary. | ⬜ |
| 5 | Semua tabel menggunakan `ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci`. | ⬜ |
| 6 | Semua tabel memiliki `COMMENT` yang mencakup deskripsi dan tingkat sensitivitas. | ⬜ |
| 7 | Semua kolom memiliki `COMMENT` berisi deskripsi bisnis singkat. | ⬜ |
| 8 | File berisi minimal **4 statement CREATE INDEX** tambahan sesuai rekomendasi Data Dictionary. | ⬜ |
| 9 | File berisi INSERT seed data untuk 5 tabel (cabang, pengguna, saldo_ppob, saldo_ewallet, system_configs) sesuai Data Dictionary Bab 11.1. | ⬜ |
| 10 | File berisi bagian verifikasi integritas (SHOW TABLES dan SELECT COUNT). | ⬜ |
| 11 | File berisi header metadata dan footer referensi dokumen. | ⬜ |
| 12 | File bersifat idempoten (aman dieksekusi ulang berulang kali). | ⬜ |
| 13 | Semua kolom `cabang_id` pada 28 tabel memiliki DEFAULT 1 dan FK ke `cabang(id)`. | ⬜ |
| 14 | Semua tabel memiliki kolom `created_at` dan `updated_at` dengan default timestamp yang sesuai. | ⬜ |
| 15 | File ditulis menggunakan bahasa SQL standar MySQL 8.x dengan komentar berbahasa Indonesia yang natural dan mudah dipahami. | ⬜ |
| 16 | Dokumen layak dijadikan referensi dan input utama untuk fase SDLC selanjutnya (Implementation & seed.sql). | ⬜ |
| 17 | Tidak ada data yang hilang atau dikarang. Data kosong ditandai dengan `[TODO: DATA KOSONG]`. | ⬜ |

---

## 7. Referensi Dokumen

Dokumen issue ini disusun berdasarkan analisis dan derivasi dari file-file berikut:

| No | Dokumen Referensi | Path Relatif |
|----|-------------------|--------------|
| 1 | Data Dictionary v1.1 | `docs/sdlc/02_analysis/05_data_dictionary.md` |
| 2 | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` |
| 3 | Tech Stack Decision v1.1 | `docs/sdlc/01_planning/04_tech_stack_decision.md` |
| 4 | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| 5 | Business Requirements Document v1.1 | `docs/sdlc/02_analysis/01_business_requirements.md` |
| 6 | Narasi Pemilik Usaha | `docs/sdlc/narasi.txt` |
