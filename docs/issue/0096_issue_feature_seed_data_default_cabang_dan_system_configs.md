# Issue — Feature: Seed Data Default Cabang dan System Configs

---

## Metadata Issue

| Atribut         | Nilai                                                                          |
| :-------------- | :----------------------------------------------------------------------------- |
| **Judul**       | Feature: Seed Data Default Cabang dan System Configs                           |
| **Tipe**        | Feature Implementation (Data Layer — Seed & Verification)                      |
| **Prioritas**   | 🔴 CRITICAL — Blocking seluruh modul fungsional M.1 s.d M.10                  |
| **Status**      | 📋 OPEN — Menunggu implementasi                                               |
| **Target File** | `db/seed_data.py` (NEW), update `db/schema_initializer.py`, update `db/__init__.py` |
| **Tanggal**     | 2026-06-04                                                                     |

---

## 1. Persona Eksekutor

**Kamu adalah `Senior Database Seed Engineer & Data Integrity Specialist`.**

Kamu memiliki keahlian mendalam dalam:
- Penulisan skrip seed data Python yang presisi, idempoten, dan transaksional ACID.
- Pemahaman arsitektur multi-cabang (`cabang_id` sebagai foreign key induk seluruh 27 tabel turunan).
- Validasi integritas referensial data seed terhadap skema DDL MySQL 8.x LTS.
- Penulisan kode Python fungsional murni (FP) tanpa class, menggunakan `NamedTuple`, `Result Pattern`, dan `decimal.Decimal` presisi 4 desimal (`ROUND_HALF_UP`).
- Pembuatan bcrypt hash Cost Factor 12 untuk password akun pemilik default.
- Penulisan unit test deterministik 100% tanpa koneksi database fisik (mock/patch).

**Kompetensi kunci yang harus kamu terapkan:**
- Kamu WAJIB memastikan seluruh seed data ter-insert ke database secara atomik (all-or-nothing).
- Kamu WAJIB memastikan seed data bersifat **idempoten** — menjalankan ulang seed tidak akan menyebabkan error duplikasi (gunakan `INSERT IGNORE` atau pengecekan `SELECT COUNT(*)` sebelum insert).
- Kamu WAJIB mematuhi seluruh standar Coding Standard v1.2 AbuCom tanpa pengecualian.

---

## 2. Dokumen Referensi

Berikut adalah daftar file referensi yang **WAJIB** dibaca dan diekstrak datanya sebelum memulai implementasi. Baca setiap file secara menyeluruh, jangan lewatkan detail kecil apapun yang relevan.

### 2.1. Referensi PRIMER (Sumber Kebenaran Tunggal)

| No | File Referensi | Path Relatif | Bagian yang WAJIB Diekstrak |
|----|---------------|-------------|---------------------------|
| R-01 | **Database Schema DDL SQL v1.2** | `docs/sdlc/03_design/01_database_schema.sql` | **BAGIAN 4 — DATA SEED AWAL (INSERT INTO)** pada baris 676-718: Seluruh INSERT statement untuk tabel `cabang`, `pengguna`, `saldo_ppob`, `saldo_ewallet`, dan `system_configs`. Catat dengan presisi seluruh kolom, nilai, tipe data, dan jumlah baris yang diharapkan. |
| R-02 | **Data Dictionary v1.2** | `docs/sdlc/02_analysis/05_data_dictionary.md` | **Bab 3.1** (Tabel `cabang` — 6 kolom), **Bab 3.28** (Tabel `system_configs` — 8 kolom), **Bab 6.4** (Aturan Default Value — 13 parameter), **Bab 9** (Spesifikasi Seed Data Awal Minimum baris 1527-1558). |
| R-03 | **schema.sql (Active)** | `schema.sql` (root project) | File skema aktif yang dieksekusi oleh `schema_initializer.py`. Bandingkan dengan R-01 untuk memastikan konsistensi 100%. |

### 2.2. Referensi SEKUNDER (Standar & Arsitektur)

| No | File Referensi | Path Relatif | Bagian yang Relevan |
|----|---------------|-------------|---------------------|
| R-04 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | Bab 2.2 (FP Murni), Bab 2.4 (Decimal-First), Bab 3 (Naming), Bab 6 (Docstring PEP 257), Bab 7 (Type Hints), Bab 8.7 (Result Pattern), Bab 8.8 (ACID Transaction Wrapper), Bab 9 (Parameterized Queries `%s`), Bab 10.2 (bcrypt Cost 12). |
| R-05 | **Module Structure v1.2** | `docs/sdlc/04_implementation/03_module_structure.md` | Bab 3.1 (Layout Direktori — posisi `db/`), Bab 6.2-6.3 (Spesifikasi `db/db_connector.py` dan `db/query_builder.py`). |
| R-06 | **System Architecture v1.1** | `docs/sdlc/03_design/03_system_architecture.md` | Arsitektur 4-layer, multi-branch ready, connection pool, retry mechanism. |
| R-07 | **ERD Database v1.1** | `docs/sdlc/03_design/02_erd_database.md` | Bab 7.8 (Seed Data) — spesifikasi seed data awal dan validasi integritas. |
| R-08 | **Software Requirements Spec v1.1** | `docs/sdlc/02_analysis/02_software_requirements.md` | SRS-F-036 (Setup Wizard), SRS-F-038 (Parameter Tabel Konfigurasi), SRS-F-040 (Config Runtime), Lampiran 10.1 (Daftar lengkap parameter `system_configs`). |

### 2.3. Referensi KODE EXISTING

| No | File Referensi | Path Relatif | Relevansi |
|----|---------------|-------------|-----------|
| E-01 | **schema_initializer.py** | `db/schema_initializer.py` | Kode existing yang sudah mengeksekusi DDL + seed via SQL file. Pahami alur `run_full_initialization()`, `verify_schema_integrity()`, dan konstanta `EXPECTED_SEED_COUNTS`. |
| E-02 | **db_connector.py** | `db/db_connector.py` | Kode existing connection pool dan `get_root_connection()`. Pahami pola Result Pattern yang sudah diterapkan. |
| E-03 | **query_builder.py** | `db/query_builder.py` | Kode existing ACID transaction wrapper. |
| E-04 | **db/__init__.py** | `db/__init__.py` | Re-export modul db. Perlu di-update untuk mengekspos fungsi seed baru. |

### 2.4. Referensi Narasi (Konteks Bisnis)

| No | File Referensi | Path Relatif | Relevansi |
|----|---------------|-------------|-----------|
| N-01 | **narasi.txt** | `docs/sdlc/narasi.txt` | **Masih dibutuhkan** sebagai konteks bisnis. Baris 56-59: Detail 6 akun e-wallet (Mandiri Agen, Dana, Gopay, LinkAja, ShopeePay, OVO). Baris 77-82: Sistem poin 4-tier (500, 1500, 2500, 5000). Baris 97: Multi-branch ready dengan `cabang_id`. |

---

## 3. Ekstraksi Data Referensi — Rangkuman Detail Lengkap

> **INSTRUKSI**: Sebelum menulis kode apapun, kamu WAJIB membaca seluruh file referensi di Bab 2 dan mengekstrak semua data berikut. Jangan lewatkan satu pun detail kecil. Catat hasilnya secara internal sebelum memulai implementasi.

### 3.1. Data Seed Tabel `cabang` (1 baris)

Sumber: R-01 baris 680-681, R-02 Bab 3.1

```sql
INSERT INTO cabang (id, nama_cabang, alamat, telp)
VALUES (1, 'Toko Pusat Bandung', 'Jl. Raya Percetakan No. 45, RT 02/RW 03, Kecamatan Sukamaju, Kota Bandung, Jawa Barat, 40123', '0227654321');
```

| Kolom | Tipe | Nilai Seed | Catatan |
|-------|------|-----------|---------|
| `id` | INT, PK, AI | `1` | ID default wajib = 1, menjadi FK induk seluruh 27 tabel |
| `nama_cabang` | VARCHAR(100), UQ, NN | `'Toko Pusat Bandung'` | Nama unik cabang pusat |
| `alamat` | TEXT, NN | `'Jl. Raya Percetakan No. 45, RT 02/RW 03, Kecamatan Sukamaju, Kota Bandung, Jawa Barat, 40123'` | Alamat fisik lengkap |
| `telp` | VARCHAR(20), NN | `'0227654321'` | Nomor telepon kontak |
| `created_at` | TIMESTAMP | AUTO | Auto-generated |
| `updated_at` | TIMESTAMP | AUTO | Auto-generated |

### 3.2. Data Seed Tabel `pengguna` (1 baris — Akun Pemilik Default)

Sumber: R-01 baris 684-685, R-04 Bab 10.2

```sql
INSERT INTO pengguna (id, nama_lengkap, username, password_hash, role, failed_login_attempts, locked_until, cabang_id)
VALUES (1, 'Pemilik Usaha AbuCom', 'pemilik', '<BCRYPT_HASH>', 'pemilik', 0, NULL, 1);
```

| Kolom | Tipe | Nilai Seed | Catatan |
|-------|------|-----------|---------|
| `id` | INT, PK, AI | `1` | ID pemilik wajib = 1 |
| `nama_lengkap` | VARCHAR(100), NN | `'Pemilik Usaha AbuCom'` | Nama lengkap default |
| `username` | VARCHAR(50), UQ, NN | `'pemilik'` | Username login default |
| `password_hash` | VARCHAR(255), NN | **HARUS di-generate runtime** | bcrypt Cost 12 dari password default `'admin123'` |
| `role` | VARCHAR(30), NN | `'pemilik'` | Peran absolut tertinggi |
| `failed_login_attempts` | INT, NN | `0` | Counter login gagal |
| `locked_until` | TIMESTAMP, NULL | `NULL` | Tidak terkunci |
| `cabang_id` | INT, FK, NN | `1` | Merujuk `cabang.id = 1` |

> **⚠️ KRITIS**: Password hash di file `schema.sql` adalah **placeholder** (`$2b$12$K3h8jD8sS9fJ2gK3l8h9oO...`). Kode seed Python WAJIB men-generate bcrypt hash RIIL dari password `'admin123'` menggunakan `bcrypt.gensalt(rounds=12)` saat runtime. Ini sudah dilakukan di `schema_initializer.py` baris 336-338, namun harus dipastikan konsistensinya di modul seed baru.

### 3.3. Data Seed Tabel `saldo_ppob` (2 baris)

Sumber: R-01 baris 688-691, N-01 baris 56

| Kolom | Baris 1 | Baris 2 |
|-------|---------|---------|
| `akun_tipe` | `'Pulsa_Data'` | `'Token_Tagihan'` |
| `saldo_terakhir` | `1000000.0000` | `1500000.0000` |
| `cabang_id` | `1` | `1` |

### 3.4. Data Seed Tabel `saldo_ewallet` (6 baris)

Sumber: R-01 baris 694-701, N-01 baris 59

| No | `nama_ewallet` | `saldo_terakhir` | `biaya_admin_flat` | `biaya_admin_persen` | `limit_harian` | `cabang_id` |
|----|---------------|-----------------|-------------------|--------------------|--------------|----|
| 1 | `'Mandiri Agen'` | `2000000.0000` | `3000.0000` | `0.0000` | `50000000.0000` | `1` |
| 2 | `'Dana'` | `1000000.0000` | `1000.0000` | `0.0000` | `10000000.0000` | `1` |
| 3 | `'Gopay'` | `1000000.0000` | `1000.0000` | `0.0000` | `10000000.0000` | `1` |
| 4 | `'LinkAja'` | `1000000.0000` | `1000.0000` | `0.0000` | `10000000.0000` | `1` |
| 5 | `'ShopeePay'` | `1000000.0000` | `1000.0000` | `0.0000` | `10000000.0000` | `1` |
| 6 | `'OVO'` | `1000000.0000` | `1000.0000` | `0.0000` | `10000000.0000` | `1` |

### 3.5. Data Seed Tabel `system_configs` (13 baris)

Sumber: R-01 baris 704-718, R-02 Bab 6.4 baris 1369-1382, R-08 SRS-F-038

| No | `parameter_key` | `parameter_value` | `tipe_data` | `deskripsi` | `cabang_id` |
|----|----------------|-------------------|-------------|-------------|-------------|
| 1 | `'target_laba_payroll'` | `'15000000.0000'` | `'DECIMAL'` | `'Target laba bersih bulanan untuk skema gaji tetap (Skenario A Smart Payroll)'` | `1` |
| 2 | `'porsi_gaji_laba'` | `'0.2500'` | `'DECIMAL'` | `'Persentase alokasi laba bersih untuk pool gaji karyawan (Skenario B Smart Payroll)'` | `1` |
| 3 | `'limit_kasbon_staf'` | `'1000000.0000'` | `'DECIMAL'` | `'Pagu maksimal utang kasbon aktif kumulatif per staf'` | `1` |
| 4 | `'threshold_saldo_ppob'` | `'150000.0000'` | `'DECIMAL'` | `'Batas saldo minimum PPOB yang memicu alert deposit'` | `1` |
| 5 | `'min_topup_ppob'` | `'500000.0000'` | `'DECIMAL'` | `'Nominal minimum deposit topup saldo PPOB'` | `1` |
| 6 | `'toleransi_selisih_kas'` | `'10000.0000'` | `'DECIMAL'` | `'Batas toleransi selisih kas kasir sebelum status ANOMALI'` | `1` |
| 7 | `'poin_tier_1_rupiah'` | `'500.0000'` | `'DECIMAL'` | `'Nilai rupiah per poin insentif Tier 1 (transaksi mudah)'` | `1` |
| 8 | `'poin_tier_2_rupiah'` | `'1500.0000'` | `'DECIMAL'` | `'Nilai rupiah per poin insentif Tier 2 (jasa dasar)'` | `1` |
| 9 | `'poin_tier_3_rupiah'` | `'2500.0000'` | `'DECIMAL'` | `'Nilai rupiah per poin insentif Tier 3 (produk kustom)'` | `1` |
| 10 | `'poin_tier_4_rupiah'` | `'5000.0000'` | `'DECIMAL'` | `'Nilai rupiah per poin insentif Tier 4 (pekerjaan berat/teknis)'` | `1` |
| 11 | `'threshold_pengeluaran'` | `'500000.0000'` | `'DECIMAL'` | `'Batas nominal pengeluaran yang memerlukan otorisasi pemilik'` | `1` |
| 12 | `'umr_daerah'` | `'3200000.0000'` | `'DECIMAL'` | `'Upah Minimum Regional daerah sebagai batas proteksi gaji minimum staf'` | `1` |
| 13 | `'dana_cadangan_darurat'` | `'4500000.0000'` | `'DECIMAL'` | `'Cadangan kas darurat minimal yang harus dijaga di laci kasir'` | `1` |

### 3.6. Ringkasan Validasi Integritas Seed

Sumber: R-01 baris 722-739 (BAGIAN 5 — VERIFIKASI INTEGRITAS)

| Tabel | Jumlah Baris Diharapkan |
|-------|------------------------|
| `cabang` | 1 |
| `pengguna` | 1 |
| `saldo_ppob` | 2 |
| `saldo_ewallet` | 6 |
| `system_configs` | 13 |
| **Total seed records** | **23** |

---

## 4. Batasan, Cakupan & Alur Pengerjaan

### 4.1. Cakupan (IN SCOPE)

- [x] Pembuatan file baru `db/seed_data.py` berisi fungsi-fungsi pure FP untuk seed data.
- [x] Fungsi seed idempoten untuk 5 tabel: `cabang`, `pengguna`, `saldo_ppob`, `saldo_ewallet`, `system_configs`.
- [x] Fungsi verifikasi integritas seed data setelah insert.
- [x] Generate bcrypt hash riil untuk password pemilik default (`'admin123'`).
- [x] Update `db/__init__.py` untuk re-export fungsi seed baru.
- [x] Unit test deterministik di `tests/test_unit_seed_data.py` (tanpa koneksi database).
- [x] Konsistensi data seed antara `schema.sql` ↔ `seed_data.py` ↔ `schema_initializer.py`.

### 4.2. Di Luar Cakupan (OUT OF SCOPE) — JANGAN DIKERJAKAN

- ❌ Mengubah file `schema.sql` atau `docs/sdlc/03_design/01_database_schema.sql`.
- ❌ Mengubah struktur DDL (CREATE TABLE) yang sudah ada.
- ❌ Menambahkan tabel baru ke database.
- ❌ Mengubah logika di `db/db_connector.py` (connection pool sudah stabil).
- ❌ Mengimplementasikan fitur CLI menu configs (M.10) — itu issue terpisah.
- ❌ Mengubah file di folder `cli/`, `logic/`, `middleware/`, `config/`, `utils/`.
- ❌ Mengubah file `main.py`.

### 4.3. Alur Pengerjaan (Execution Flow)

```
[FASE 1: PEMBACAAN REFERENSI]
     │
     ▼
[FASE 2: PEMBUATAN db/seed_data.py]
     │
     ▼
[FASE 3: UPDATE db/__init__.py]
     │
     ▼
[FASE 4: PEMBUATAN tests/test_unit_seed_data.py]
     │
     ▼
[FASE 5: VERIFIKASI & VALIDASI]
```

---

## 5. Proteksi Feature Lain — Aturan Keamanan

> **INSTRUKSI KRITIS**: Pengerjaan issue ini **TIDAK BOLEH** menyentuh atau merusak feature lain yang sudah berjalan. Patuhi aturan berikut:

- [ ] **Jangan mengubah** file `db/db_connector.py` — connection pool dan retry mechanism sudah stabil.
- [ ] **Jangan mengubah** file `db/query_builder.py` — ACID transaction wrapper sudah stabil.
- [ ] **Jangan mengubah** file `db/schema_initializer.py` — file ini sudah bekerja dan di-test oleh issue sebelumnya. Modul seed baru harus berdiri sendiri dan bisa dipanggil secara independen.
- [ ] **Jangan mengubah** file `schema.sql` — sumber kebenaran DDL + seed SQL.
- [ ] **Jangan mengubah** file apapun di folder `cli/`, `logic/`, `middleware/`, `config/`, `utils/`.
- [ ] **Jangan menghapus** test file yang sudah ada di `tests/`.
- [ ] **Jangan menghapus** komentar atau docstring existing yang tidak terkait perubahan kamu.
- [ ] Pastikan konstanta `EXPECTED_SEED_COUNTS` di `schema_initializer.py` **TETAP KONSISTEN** dengan data seed yang kamu buat.
- [ ] Jalankan test existing (`pytest tests/`) setelah selesai dan pastikan **TIDAK ADA test yang rusak**.

---

## 6. Instruksi Kualitas Pengerjaan

> **⚠️ PENTING**: Kerjakan issue ini dengan **RAPI, BERSIH, TIDAK TERGESA-GESA, dan TIDAK BURU-BURU** agar hasilnya maksimal. Jangan skip langkah apapun.

### 6.1. Standar Kualitas Kode

- [ ] Setiap fungsi publik WAJIB memiliki docstring PEP 257 lengkap (Args, Returns, Raises, Example).
- [ ] Setiap fungsi publik WAJIB memiliki type hints PEP 484 lengkap pada semua parameter dan return value.
- [ ] Gunakan `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])` untuk return value.
- [ ] Gunakan `decimal.Decimal` untuk semua nilai nominal keuangan — DILARANG menggunakan `float`.
- [ ] Gunakan parameterized queries `%s` — DILARANG menggunakan f-string untuk SQL.
- [ ] Semua string SQL keyword HARUS uppercase (`INSERT INTO`, `SELECT`, `WHERE`, dll.).
- [ ] Import diurutkan: Standard Library → Third-Party → Local Modules.
- [ ] Header file module docstring PEP 257 di baris paling atas.
- [ ] Nama fungsi format `snake_case` (verb_noun): `seed_cabang_default()`, `verify_seed_integrity()`.
- [ ] Nama konstanta format `UPPER_SNAKE_CASE`: `DEFAULT_CABANG_DATA`, `EXPECTED_SEED_COUNTS`.
- [ ] Batas panjang baris maksimal 120 karakter.
- [ ] 2 baris kosong di antara definisi fungsi top-level.

### 6.2. Standar Kelengkapan

- [ ] Seluruh 13 parameter `system_configs` WAJIB di-seed LENGKAP, jangan ada yang terlewat.
- [ ] Seluruh 6 akun e-wallet WAJIB di-seed LENGKAP dengan kolom `biaya_admin_flat`, `biaya_admin_persen`, dan `limit_harian`.
- [ ] Seluruh 2 akun PPOB WAJIB di-seed LENGKAP.
- [ ] Data cabang WAJIB memiliki alamat lengkap persis seperti di `schema.sql`.
- [ ] Data pengguna pemilik WAJIB memiliki bcrypt hash yang VALID (bukan placeholder).
- [ ] Verifikasi COUNT per tabel WAJIB cocok dengan `EXPECTED_SEED_COUNTS` di `schema_initializer.py`.

---

## 7. Penanganan Data Kosong / Tidak Tersedia

> **INSTRUKSI**: Jika ada data yang kosong, tidak ada, atau ambigu pada file referensi, **JANGAN** mengisi dengan asumsi sendiri. Tandai dengan format berikut:

```python
# ⚠️ DATA_KOSONG: [nama_kolom] pada [nama_tabel] tidak ditemukan di referensi [R-XX].
# Tindak lanjut diperlukan sebelum deployment produksi.
```

Setelah implementasi selesai, daftarkan semua temuan data kosong di akhir file sebagai komentar blok terstruktur.

---

## 8. Instruksi Tambahan Spesifik Seed Data

### 8.1. Idempoten — Seed Harus Aman Dijalankan Berkali-kali

- [ ] Setiap fungsi seed WAJIB mengecek apakah data sudah ada sebelum INSERT.
- [ ] Gunakan pola: `SELECT COUNT(*) FROM tabel WHERE kondisi_unik` → jika > 0, skip insert, return Result sukses.
- [ ] JANGAN gunakan `TRUNCATE` atau `DELETE` sebelum INSERT — ini berbahaya untuk data produksi.

### 8.2. Urutan Insert Harus Benar (Dependency Order)

Karena ada foreign key constraint, urutan seed WAJIB:
1. `cabang` (tabel induk, TIDAK punya FK ke tabel lain)
2. `pengguna` (FK ke `cabang.id`)
3. `saldo_ppob` (FK ke `cabang.id`)
4. `saldo_ewallet` (FK ke `cabang.id`)
5. `system_configs` (FK ke `cabang.id`)

> **⚠️ KRITIS**: Jika `cabang` id=1 belum ada, seluruh INSERT ke tabel 2-5 PASTI GAGAL karena `FOREIGN KEY CONSTRAINT` violation. Pastikan urutan ini dipatuhi.

### 8.3. Transaksi ACID untuk Seed

- [ ] Seluruh operasi seed WAJIB dibungkus dalam satu transaksi ACID.
- [ ] Jika ada satu insert yang gagal, seluruh seed harus di-ROLLBACK.
- [ ] Jika semua insert berhasil, COMMIT.
- [ ] Gunakan pola `start_transaction()` → operasi → `commit()` / `rollback()`.

### 8.4. Validasi Pasca-Seed

- [ ] Setelah seed berhasil, jalankan fungsi verifikasi yang mengecek:
  - `SELECT COUNT(*) FROM cabang` = 1
  - `SELECT COUNT(*) FROM pengguna` = 1
  - `SELECT COUNT(*) FROM saldo_ppob` = 2
  - `SELECT COUNT(*) FROM saldo_ewallet` = 6
  - `SELECT COUNT(*) FROM system_configs` = 13
- [ ] Verifikasi bahwa password hash di `pengguna.id=1` adalah bcrypt valid (dimulai dengan `$2b$12$`).
- [ ] Verifikasi bahwa `system_configs` memiliki 13 unique `parameter_key`.

### 8.5. Logging

- [ ] Gunakan `logging.getLogger('abucom.db.seed')` untuk logging.
- [ ] Log level INFO untuk setiap tabel yang berhasil di-seed: `"Seed tabel cabang: 1 baris berhasil diinsert."`.
- [ ] Log level WARNING jika tabel sudah memiliki data (skip): `"Seed tabel cabang: data sudah ada, skip insert."`.
- [ ] Log level ERROR untuk kegagalan: `"ERR-DB-SEED-001: Gagal seed tabel cabang."`.

---

## 9. Checklist Implementasi Tahap-demi-Tahap

### FASE 1: Pembacaan & Ekstraksi Referensi

- [ ] **1.1.** Baca file `docs/sdlc/03_design/01_database_schema.sql` — fokus pada BAGIAN 4 (baris 676-718) dan BAGIAN 5 (baris 722-739).
- [ ] **1.2.** Baca file `docs/sdlc/02_analysis/05_data_dictionary.md` — fokus pada Bab 3.1 (tabel cabang), Bab 3.28 (tabel system_configs), dan Bab 6.4 (13 parameter default).
- [ ] **1.3.** Baca file `schema.sql` (root project) — bandingkan BAGIAN 4 seed data dengan R-01 untuk verifikasi konsistensi.
- [ ] **1.4.** Baca file `db/schema_initializer.py` — pahami pola yang digunakan: `Result` namedtuple, konstanta `EXPECTED_SEED_COUNTS`, alur `run_full_initialization()`.
- [ ] **1.5.** Baca file `db/db_connector.py` — pahami pola `Result` pattern dan `get_root_connection()`.
- [ ] **1.6.** Baca file `db/query_builder.py` — pahami pola ACID transaction wrapper.
- [ ] **1.7.** Baca file `db/__init__.py` — pahami apa saja yang sudah di-export.
- [ ] **1.8.** Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — minimal Bab 2, 3, 6, 7, 8, 9, 10.
- [ ] **1.9.** Baca file `docs/sdlc/narasi.txt` — ekstrak informasi 6 akun e-wallet dan 4-tier poin.
- [ ] **1.10.** Catat semua data yang diekstrak. Bandingkan antar-sumber untuk konsistensi. Jika ada perbedaan, prioritaskan `schema.sql` (active) dan `01_database_schema.sql` (SSoT design).

### FASE 2: Pembuatan File `db/seed_data.py` (NEW)

- [ ] **2.1.** Buat file baru `db/seed_data.py`.
- [ ] **2.2.** Tulis header module docstring PEP 257:
  ```python
  """
  Nama Modul: seed_data.py
  Deskripsi: Utilitas fungsional untuk seeding data default awal (bootstrapping)
             ke database MySQL AbuCom. Mencakup tabel cabang, pengguna, saldo_ppob,
             saldo_ewallet, dan system_configs. Bersifat idempoten dan transaksional ACID.
  Author: [Nama Pengembang / AI Asisten]
  Tanggal: [YYYY-MM-DD]
  """
  ```
- [ ] **2.3.** Tulis import statements (urutan: Standard → Third-Party → Local):
  ```python
  # 1. Standard Library
  import logging
  from collections import namedtuple

  # 2. Third-Party
  import mysql.connector
  import bcrypt
  ```
- [ ] **2.4.** Definisikan logger:
  ```python
  _logger = logging.getLogger('abucom.db.seed')
  ```
- [ ] **2.5.** Definisikan NamedTuple Result (konsisten dengan modul existing):
  ```python
  Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
  ```
- [ ] **2.6.** Definisikan konstanta data seed sebagai tuple of tuples (IMMUTABLE):
  - `DEFAULT_CABANG_DATA` — tuple berisi (id, nama_cabang, alamat, telp)
  - `DEFAULT_PENGGUNA_DATA` — tuple berisi (id, nama_lengkap, username, role, failed_login_attempts, cabang_id)
  - `DEFAULT_SALDO_PPOB_DATA` — tuple of tuples berisi (akun_tipe, saldo_terakhir, cabang_id)
  - `DEFAULT_SALDO_EWALLET_DATA` — tuple of tuples berisi 6 baris data e-wallet
  - `DEFAULT_SYSTEM_CONFIGS_DATA` — tuple of tuples berisi 13 baris parameter config
  - `DEFAULT_PASSWORD` — string `'admin123'`
  - `EXPECTED_SEED_COUNTS` — dict `{'cabang': 1, 'pengguna': 1, 'saldo_ppob': 2, 'saldo_ewallet': 6, 'system_configs': 13}`
- [ ] **2.7.** Implementasi fungsi `generate_default_password_hash(password: str) -> Result`:
  - Generate bcrypt hash dengan `bcrypt.gensalt(rounds=12)`.
  - Return `Result(True, hashed_password_string, None)` jika sukses.
  - Return `Result(False, None, error_msg)` jika gagal.
  - Validasi bahwa hash dimulai dengan `$2b$12$`.
- [ ] **2.8.** Implementasi fungsi `seed_cabang_default(cursor) -> Result`:
  - Cek `SELECT COUNT(*) FROM cabang WHERE id = 1`.
  - Jika sudah ada, log WARNING dan return sukses (skip).
  - Jika belum ada, `INSERT INTO cabang (id, nama_cabang, alamat, telp) VALUES (%s, %s, %s, %s)`.
  - Gunakan parameterized query `%s`.
  - Return Result.
- [ ] **2.9.** Implementasi fungsi `seed_pengguna_default(cursor, password_hash: str) -> Result`:
  - Cek `SELECT COUNT(*) FROM pengguna WHERE id = 1`.
  - Jika sudah ada, log WARNING dan return sukses (skip).
  - Jika belum ada, INSERT dengan bcrypt hash yang sudah di-generate.
  - Gunakan parameterized query `%s`.
  - Return Result.
- [ ] **2.10.** Implementasi fungsi `seed_saldo_ppob_default(cursor) -> Result`:
  - Cek `SELECT COUNT(*) FROM saldo_ppob`.
  - Jika count >= 2, log WARNING dan return sukses (skip).
  - Jika kurang, gunakan `INSERT IGNORE INTO saldo_ppob (...) VALUES (%s, %s, %s)`.
  - Loop untuk setiap baris di `DEFAULT_SALDO_PPOB_DATA`.
  - Return Result dengan jumlah baris yang diinsert.
- [ ] **2.11.** Implementasi fungsi `seed_saldo_ewallet_default(cursor) -> Result`:
  - Cek `SELECT COUNT(*) FROM saldo_ewallet`.
  - Jika count >= 6, log WARNING dan return sukses (skip).
  - Jika kurang, gunakan `INSERT IGNORE INTO saldo_ewallet (...) VALUES (%s, %s, %s, %s, %s, %s)`.
  - Loop untuk setiap baris di `DEFAULT_SALDO_EWALLET_DATA`.
  - Return Result dengan jumlah baris yang diinsert.
- [ ] **2.12.** Implementasi fungsi `seed_system_configs_default(cursor) -> Result`:
  - Cek `SELECT COUNT(*) FROM system_configs`.
  - Jika count >= 13, log WARNING dan return sukses (skip).
  - Jika kurang, gunakan `INSERT IGNORE INTO system_configs (...) VALUES (%s, %s, %s, %s, %s)`.
  - Loop untuk setiap baris di `DEFAULT_SYSTEM_CONFIGS_DATA`.
  - Return Result dengan jumlah baris yang diinsert.
- [ ] **2.13.** Implementasi fungsi `verify_seed_integrity(cursor) -> Result`:
  - Untuk setiap tabel di `EXPECTED_SEED_COUNTS`, jalankan `SELECT COUNT(*) FROM tabel`.
  - Bandingkan count aktual dengan expected.
  - Verifikasi bahwa `pengguna.id=1` memiliki `password_hash` yang dimulai dengan `$2b$12$`.
  - Verifikasi bahwa `system_configs` memiliki 13 unique `parameter_key`.
  - Return Result berisi dict report: `{'cabang': 1, 'pengguna': 1, ...}` jika valid.
  - Return Result dengan error message jika ada mismatch.
- [ ] **2.14.** Implementasi fungsi utama `run_seed_all(db_connection) -> Result`:
  - Wrapper transaksional ACID yang memanggil seluruh fungsi seed secara berurutan:
    1. `generate_default_password_hash(DEFAULT_PASSWORD)`
    2. `db_connection.start_transaction()`
    3. `seed_cabang_default(cursor)`
    4. `seed_pengguna_default(cursor, password_hash)`
    5. `seed_saldo_ppob_default(cursor)`
    6. `seed_saldo_ewallet_default(cursor)`
    7. `seed_system_configs_default(cursor)`
    8. `db_connection.commit()` jika semua sukses
    9. `verify_seed_integrity(cursor)`
  - Jika ada kegagalan di langkah 3-7, `db_connection.rollback()`.
  - Return Result berisi laporan lengkap.
- [ ] **2.15.** Pastikan tidak ada `class` keyword di seluruh file (FP murni).
- [ ] **2.16.** Pastikan tidak ada `float` — semua nominal keuangan di Decimal string.
- [ ] **2.17.** Pastikan semua SQL query menggunakan `%s` parameterized.
- [ ] **2.18.** Pastikan logging di setiap langkah penting.

### FASE 3: Update File `db/__init__.py`

- [ ] **3.1.** Baca file existing `db/__init__.py`.
- [ ] **3.2.** Tambahkan import dan re-export untuk `seed_data`:
  ```python
  from db.seed_data import run_seed_all
  from db.seed_data import verify_seed_integrity
  ```
- [ ] **3.3.** Pastikan import existing TIDAK diubah atau dihapus.
- [ ] **3.4.** Pastikan `__init__.py` tidak memiliki circular import.

### FASE 4: Pembuatan File `tests/test_unit_seed_data.py` (NEW)

- [ ] **4.1.** Buat file baru `tests/test_unit_seed_data.py`.
- [ ] **4.2.** Tulis header module docstring PEP 257.
- [ ] **4.3.** Import yang diperlukan:
  ```python
  import pytest
  from unittest.mock import MagicMock, patch, call
  from collections import namedtuple
  from db.seed_data import (
      generate_default_password_hash,
      seed_cabang_default,
      seed_pengguna_default,
      seed_saldo_ppob_default,
      seed_saldo_ewallet_default,
      seed_system_configs_default,
      verify_seed_integrity,
      run_seed_all,
      DEFAULT_CABANG_DATA,
      DEFAULT_SALDO_PPOB_DATA,
      DEFAULT_SALDO_EWALLET_DATA,
      DEFAULT_SYSTEM_CONFIGS_DATA,
      EXPECTED_SEED_COUNTS,
  )
  ```
- [ ] **4.4.** Tulis test untuk `generate_default_password_hash()`:
  - Test sukses: hash dimulai dengan `$2b$12$`.
  - Test Result.is_success = True.
  - Test hash bukan sama dengan plain password.
- [ ] **4.5.** Tulis test untuk `seed_cabang_default()`:
  - Test ketika tabel sudah ada data (skip insert, return sukses).
  - Test ketika tabel kosong (execute INSERT, return sukses).
  - Test SQL query yang digunakan benar (parameterized `%s`).
  - Gunakan MagicMock untuk cursor.
- [ ] **4.6.** Tulis test untuk `seed_pengguna_default()`:
  - Test ketika user id=1 sudah ada (skip insert).
  - Test ketika user belum ada (INSERT dengan hash).
  - Test bahwa password_hash di INSERT bukan plain text.
- [ ] **4.7.** Tulis test untuk `seed_saldo_ppob_default()`:
  - Test skip ketika count >= 2.
  - Test INSERT 2 baris ketika kosong.
  - Test domain value `akun_tipe` sesuai: `'Pulsa_Data'`, `'Token_Tagihan'`.
- [ ] **4.8.** Tulis test untuk `seed_saldo_ewallet_default()`:
  - Test skip ketika count >= 6.
  - Test INSERT 6 baris ketika kosong.
  - Test bahwa semua 6 nama ewallet ada: `'Mandiri Agen'`, `'Dana'`, `'Gopay'`, `'LinkAja'`, `'ShopeePay'`, `'OVO'`.
- [ ] **4.9.** Tulis test untuk `seed_system_configs_default()`:
  - Test skip ketika count >= 13.
  - Test INSERT 13 baris ketika kosong.
  - Test bahwa semua 13 `parameter_key` ada dalam konstanta.
  - Test bahwa `tipe_data` semua = `'DECIMAL'` untuk 13 parameter ini.
- [ ] **4.10.** Tulis test untuk `verify_seed_integrity()`:
  - Test valid: semua count cocok.
  - Test invalid: satu count tidak cocok (return is_success=False).
- [ ] **4.11.** Tulis test untuk `run_seed_all()`:
  - Test full flow sukses (mock semua sub-fungsi).
  - Test rollback ketika satu seed gagal.
  - Test bahwa transaksi di-commit jika semua sukses.
  - Test bahwa transaksi di-rollback jika ada kegagalan.
- [ ] **4.12.** Tulis test untuk konsistensi konstanta:
  - Test `len(DEFAULT_SYSTEM_CONFIGS_DATA) == 13`.
  - Test `len(DEFAULT_SALDO_EWALLET_DATA) == 6`.
  - Test `len(DEFAULT_SALDO_PPOB_DATA) == 2`.
  - Test `EXPECTED_SEED_COUNTS['system_configs'] == 13`.
- [ ] **4.13.** Pastikan SEMUA test bisa jalan tanpa koneksi database fisik (100% mock).
- [ ] **4.14.** Target code coverage minimal **90%** untuk `db/seed_data.py`.

### FASE 5: Verifikasi & Validasi

- [ ] **5.1.** Jalankan `python -m py_compile db/seed_data.py` — pastikan tidak ada syntax error.
- [ ] **5.2.** Jalankan `python -m py_compile tests/test_unit_seed_data.py` — pastikan tidak ada syntax error.
- [ ] **5.3.** Jalankan `pytest tests/test_unit_seed_data.py -v` — pastikan semua test PASS.
- [ ] **5.4.** Jalankan `pytest tests/ -v` — pastikan test EXISTING juga masih PASS (tidak ada regresi).
- [ ] **5.5.** Jalankan `pytest tests/ --cov=db/seed_data --cov-report=term-missing` — pastikan coverage >= 90%.
- [ ] **5.6.** Review manual: pastikan seluruh 13 parameter `system_configs` ada dan nilainya benar.
- [ ] **5.7.** Review manual: pastikan seluruh 6 akun e-wallet ada dan nilainya benar.
- [ ] **5.8.** Review manual: pastikan data cabang dan pengguna pemilik sesuai referensi.
- [ ] **5.9.** Cross-check konstanta `EXPECTED_SEED_COUNTS` di `seed_data.py` dengan `schema_initializer.py` — HARUS IDENTIK.
- [ ] **5.10.** Pastikan file `db/__init__.py` sudah mengekspos `run_seed_all` dan `verify_seed_integrity`.

---

## 10. Deliverables (Hasil Akhir yang Diharapkan)

| No | File | Aksi | Deskripsi |
|----|------|------|-----------|
| 1 | `db/seed_data.py` | **[NEW]** | Modul seed data FP murni, idempoten, transaksional ACID |
| 2 | `db/__init__.py` | **[MODIFY]** | Tambah re-export `run_seed_all`, `verify_seed_integrity` |
| 3 | `tests/test_unit_seed_data.py` | **[NEW]** | Unit test deterministik mock, coverage >= 90% |

---

## 11. Kriteria Selesai (Definition of Done)

- [ ] File `db/seed_data.py` terbuat lengkap dengan semua fungsi seed + verifikasi.
- [ ] File `tests/test_unit_seed_data.py` terbuat lengkap dengan coverage >= 90%.
- [ ] `pytest tests/ -v` → **SEMUA TEST PASS** (termasuk test existing).
- [ ] Tidak ada syntax error di semua file baru.
- [ ] Tidak ada file existing yang rusak atau berubah perilakunya.
- [ ] Semua 23 baris seed data (1+1+2+6+13) terdefinisi lengkap dan akurat.
- [ ] Password hash di-generate dengan bcrypt Cost 12 (bukan placeholder).
- [ ] Seluruh kode mematuhi Coding Standard v1.2 AbuCom (FP, docstring, type hints, naming).
- [ ] Tidak ada data yang hilang, terlewat, atau diasumsikan tanpa dasar referensi.
- [ ] Tidak ada `float`, `class`, f-string SQL, atau wildcard import.

---

## 12. Catatan & Risiko

### 12.1. Risiko yang Harus Diwaspadai

| Risiko | Dampak | Mitigasi |
|--------|--------|---------|
| Password placeholder dari `schema.sql` digunakan tanpa di-replace | Akun pemilik tidak bisa login | Selalu generate bcrypt hash baru saat seed |
| Urutan seed salah (insert pengguna sebelum cabang) | FK constraint violation | Patuhi urutan dependency: cabang → pengguna → ppob → ewallet → configs |
| Duplikasi data saat seed dijalankan ulang | Unique constraint violation | Implementasi idempoten check sebelum INSERT |
| Konstanta EXPECTED_SEED_COUNTS tidak konsisten antara seed_data.py dan schema_initializer.py | Verifikasi gagal meskipun data benar | Cross-check manual sebelum commit |

### 12.2. Catatan Khusus

- Data seed saat ini menggunakan data PLACEHOLDER (alamat, telepon cabang). Untuk deployment produksi, data ini harus diganti dengan data riil — namun **BUKAN bagian dari scope issue ini**.
- Default password `'admin123'` WAJIB diganti oleh pemilik saat login pertama — namun implementasi fitur "force change password" adalah **issue terpisah**.
- Seluruh 13 parameter `system_configs` memiliki `tipe_data = 'DECIMAL'`. Jika di masa depan ada parameter bertipe `VARCHAR`, `INT`, atau `BOOLEAN`, modul ini harus di-extend — namun **BUKAN bagian dari scope issue ini**.
