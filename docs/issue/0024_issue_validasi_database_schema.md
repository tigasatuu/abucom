# Validasi & Penyempurnaan Dokumen Database Schema

---

## Informasi Issue

| Atribut              | Detail                                                                 |
|----------------------|------------------------------------------------------------------------|
| **Judul**            | Validasi & Penyempurnaan Dokumen Database Schema                       |
| **Tanggal Dibuat**   | 2026-05-24                                                             |
| **Dibuat Oleh**      | Senior Software Architect                                              |
| **Status**           | Open                                                                   |
| **Prioritas**        | Tinggi                                                                 |
| **Dokumen Utama**    | `docs/sdlc/03_design/01_database_schema.sql`                          |
| **Lokasi Referensi** | `docs/sdlc/`                                                           |

---

## Persona Validator

Sebelum memulai pekerjaan, internalisasi dan kunci persona berikut ini secara penuh. Seluruh pekerjaan validasi dalam issue ini **HARUS** dilakukan dari sudut pandang persona ini.

> **Kamu adalah seorang Senior Database Architect & DDL Validation Expert** dengan pengalaman lebih dari 12 tahun merancang dan mengaudit skema basis data relasional untuk sistem enterprise multi-cabang di industri retail dan jasa. Kamu memiliki keahlian mendalam dalam:
>
> - **MySQL 8.x DDL** — DDL syntax, engine InnoDB, charset/collation, indexing strategy, constraint enforcement, foreign key semantics.
> - **Data Modeling** — Normalisasi hingga 3NF, relasi antar entitas, naming convention, sensitivitas data.
> - **SDLC Design Phase** — Kamu memahami bahwa dokumen `database_schema.sql` adalah **kontrak teknis** yang menjadi acuan bagi fase-fase SDLC berikutnya: implementasi backend, testing, deployment, dan maintenance.
> - **Referensi Cross-Check** — Kamu wajib membandingkan setiap entitas di dokumen utama dengan sumber referensinya secara menyeluruh, tidak boleh ada asumsi.
> - **Bahasa Indonesia Teknis** — Kamu menulis komentar dan keterangan dalam Bahasa Indonesia yang baku, natural, tidak ambigu, dan dapat dipahami oleh junior programmer atau LLM model yang lebih sederhana.
>
> **Standar kelulusanmu sangat ketat.** Dokumen yang kamu hasilkan harus bersih, lengkap, tidak redundan, tidak ambigu, dan siap dijadikan acuan produksi tanpa pertanyaan lanjutan.

---

## Deskripsi & Tujuan Issue

Dokumen `docs/sdlc/03_design/01_database_schema.sql` adalah output fase Design pada SDLC proyek AbuCom. Dokumen ini merupakan **kontrak teknis DDL MySQL 8.x** yang mendefinisikan 28 tabel, constraint, index, seed data, dan verifikasi skema basis data fisik sistem manajemen usaha percetakan AbuCom.

Issue ini bertujuan untuk melakukan **validasi menyeluruh dan penyempurnaan** dokumen tersebut agar:

1. Semua informasi dari dokumen-dokumen referensi telah terangkum dengan tepat dan tidak ada yang terlewat.
2. Dokumen hanya memuat informasi yang **relevan dan spesifik** untuk sebuah `database_schema.sql` — tidak ada informasi di luar scope.
3. Struktur dokumen memenuhi **standar industri** untuk DDL SQL file.
4. Dokumen layak menjadi **input berkualitas tinggi** bagi fase SDLC berikutnya (implementasi, testing, deployment).
5. Bahasa komentar **Bahasa Indonesia** di seluruh dokumen baku, natural, tidak ambigu.
6. Dokumen tidak memiliki **data kosong, placeholder, atau nilai yang belum diisi**.
7. Dokumen bersih dari pertanyaan lanjutan yang dapat menghambat pekerjaan tim selanjutnya.

---

## Dokumen Referensi yang Harus Dibaca

Berikut adalah seluruh dokumen referensi yang **WAJIB** dibaca sebelum melakukan validasi. Dokumen-dokumen ini adalah sumber kebenaran tunggal (*source of truth*) untuk isi dari `01_database_schema.sql`.

| ID Referensi | Nama Dokumen                             | Path                                                | Kontribusi Utama                                                                    |
|--------------|------------------------------------------|-----------------------------------------------------|-------------------------------------------------------------------------------------|
| REF-01       | Data Dictionary v1.1                     | `docs/sdlc/02_analysis/05_data_dictionary.md`       | Definisi 28 tabel, 282 kolom, constraint, domain nilai, seed data, aturan bisnis    |
| REF-02       | Access Control Matrix v1.1               | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Tingkat sensitivitas tabel dan matriks CRUD per role                                |
| REF-03       | Tech Stack Decision v1.1                 | `docs/sdlc/01_planning/04_tech_stack_decision.md`   | Konfigurasi MySQL (engine, charset, collation) dan strategi inisialisasi             |
| REF-04       | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | Cross-check kode kebutuhan fungsional (SRS-F-xxx)                                   |
| REF-05       | Business Requirements Document v1.1      | `docs/sdlc/02_analysis/01_business_requirements.md` | Cross-check aturan bisnis dan domain nilai (BR-F-xx)                                |

---

## Checklist Implementasi (Low-Level Step-by-Step)

Ikuti setiap langkah di bawah ini **secara berurutan dari atas ke bawah**. Jangan melewati atau menggabungkan langkah. Tandai setiap item `[ ]` menjadi `[x]` setelah selesai dikerjakan.

---

### FASE 0 — Persiapan & Pembacaan Dokumen

> **Tujuan:** Memastikan kamu memiliki pemahaman penuh atas seluruh konteks sebelum mulai melakukan validasi.

- [ ] **[BACA-0.1]** Baca seluruh isi dokumen utama dari baris pertama hingga baris terakhir:
  - File: `docs/sdlc/03_design/01_database_schema.sql`
  - Catat dalam memorimu: jumlah tabel, jumlah kolom per tabel, nama-nama constraint, jumlah index, isi seed data, isi verifikasi, dan daftar referensi yang tertulis di bagian REFERENSI DOKUMEN.

- [ ] **[BACA-0.2]** Baca seluruh isi REF-01 (Data Dictionary):
  - File: `docs/sdlc/02_analysis/05_data_dictionary.md`
  - Catat: definisi setiap tabel (nama, deskripsi), setiap kolom (tipe data, constraint, nilai default, komentar), domain nilai enum, seed data yang diharapkan, dan aturan bisnis.

- [ ] **[BACA-0.3]** Baca seluruh isi REF-02 (Access Control Matrix):
  - File: `docs/sdlc/02_analysis/06_access_control_matrix.md`
  - Catat: tingkat sensitivitas setiap tabel, dan modul terkait.

- [ ] **[BACA-0.4]** Baca seluruh isi REF-03 (Tech Stack Decision):
  - File: `docs/sdlc/01_planning/04_tech_stack_decision.md`
  - Catat: spesifikasi MySQL yang direkomendasikan (versi, engine, charset, collation, SQL mode).

- [ ] **[BACA-0.5]** Baca seluruh isi REF-04 (Software Requirements Specification):
  - File: `docs/sdlc/02_analysis/02_software_requirements.md`
  - Catat: seluruh kode SRS-F-xxx dan persyaratan fungsional yang berkaitan dengan struktur data.

- [ ] **[BACA-0.6]** Baca seluruh isi REF-05 (Business Requirements Document):
  - File: `docs/sdlc/02_analysis/01_business_requirements.md`
  - Catat: seluruh aturan bisnis BR-F-xx dan domain nilai yang relevan dengan definisi tabel.

---

### FASE 1 — Validasi Kelengkapan (Tidak Ada yang Terlewat dari Referensi)

> **Tujuan:** Memastikan **semua** data dan informasi yang ada di dokumen referensi sudah terangkum di dokumen utama. Tidak boleh ada satu pun tabel, kolom, constraint, index, seed data, atau aturan bisnis dari referensi yang hilang.

- [ ] **[VAL-1.1]** Bandingkan daftar tabel di dokumen utama dengan daftar tabel di REF-01 (Data Dictionary):
  - Pastikan **jumlah tabel sama persis** (28 tabel).
  - Pastikan **nama setiap tabel** identik antara Data Dictionary dengan DDL SQL.
  - Jika ada tabel yang ada di REF-01 tetapi **tidak ada di dokumen utama** → tandai sebagai **MISSING_TABLE** dan catat untuk diperbaiki.
  - Jika ada tabel di dokumen utama tetapi **tidak ada di REF-01** → tandai sebagai **EXTRA_TABLE** dan catat untuk dievaluasi.

- [ ] **[VAL-1.2]** Untuk setiap tabel, bandingkan **daftar kolom** antara dokumen utama dengan REF-01:
  - Lakukan satu per satu, dari tabel 01 (`cabang`) hingga tabel 28 (`riwayat_harga_supplier`).
  - Untuk setiap kolom: periksa **nama kolom**, **tipe data**, **panjang/presisi**, **NULL/NOT NULL**, **DEFAULT value**, **AUTO_INCREMENT**, dan **COMMENT**.
  - Jika ada kolom yang ada di REF-01 tetapi **tidak ada di DDL** → tandai **MISSING_COLUMN**.
  - Jika ada kolom di DDL tetapi **tidak ada di REF-01** → tandai **EXTRA_COLUMN**.
  - Jika tipe data atau properti **tidak sesuai** dengan REF-01 → tandai **TYPE_MISMATCH**.

- [ ] **[VAL-1.3]** Bandingkan seluruh **PRIMARY KEY** antara DDL dengan REF-01:
  - Pastikan setiap tabel memiliki PRIMARY KEY yang sesuai.
  - Pastikan kolom PK menggunakan `INT NOT NULL AUTO_INCREMENT` sesuai spesifikasi REF-01.

- [ ] **[VAL-1.4]** Bandingkan seluruh **FOREIGN KEY** antara DDL dengan REF-01:
  - Periksa setiap FK: nama constraint, kolom referensi, tabel target, kolom target, `ON DELETE`, dan `ON UPDATE`.
  - Pastikan semantik `ON DELETE` (CASCADE / RESTRICT / SET NULL) sesuai dengan aturan bisnis di REF-01 dan REF-05.

- [ ] **[VAL-1.5]** Bandingkan seluruh **UNIQUE CONSTRAINT** antara DDL dengan REF-01:
  - Pastikan semua kolom/kombinasi kolom yang ditetapkan UNIQUE di REF-01 sudah ada di DDL.

- [ ] **[VAL-1.6]** Bandingkan seluruh **CHECK CONSTRAINT** antara DDL dengan REF-01:
  - Pastikan semua aturan domain nilai (range, minimum, maximum) dari REF-01 dan REF-05 sudah diimplementasikan sebagai CHECK constraint.
  - Periksa logika kondisi setiap CHECK: apakah ekspresi SQL-nya sudah benar secara matematika dan bisnis?

- [ ] **[VAL-1.7]** Bandingkan **COMMENT pada tabel** (`COMMENT='...'`) dengan REF-01 dan REF-02:
  - Pastikan format COMMENT tabel mengandung: deskripsi singkat | `Sensitivitas: [level]` | `Modul: M.[nomor]`.
  - Pastikan level sensitivitas sesuai dengan REF-02 (Access Control Matrix).
  - Pastikan nomor modul sesuai dengan REF-04 (SRS).

- [ ] **[VAL-1.8]** Bandingkan **COMMENT pada setiap kolom** dengan REF-01:
  - Setiap kolom harus memiliki COMMENT yang deskriptif, tidak generik.
  - Pastikan COMMENT kolom mencerminkan definisi bisnis dari REF-01, bukan sekadar pengulangan nama kolom.

- [ ] **[VAL-1.9]** Bandingkan **INDEX tambahan (BAGIAN 3)** dengan REF-01 dan REF-04:
  - Pastikan semua index yang direkomendasikan REF-01 sudah ada.
  - Periksa apakah ada kolom frekuensi akses tinggi (berdasarkan REF-04 use case) yang belum diindeks tetapi seharusnya diindeks.

- [ ] **[VAL-1.10]** Bandingkan **seed data (BAGIAN 4)** dengan REF-01:
  - Periksa seed `cabang`: nama, alamat, telepon.
  - Periksa seed `pengguna`: nama, username, role, bcrypt hash.
  - Periksa seed `saldo_ppob`: jumlah akun (harus 2), tipe akun, nilai saldo awal.
  - Periksa seed `saldo_ewallet`: jumlah akun (harus 6), nama e-wallet, biaya admin, limit harian.
  - Periksa seed `system_configs`: jumlah parameter (harus 13), setiap `parameter_key`, `parameter_value`, `tipe_data`, dan `deskripsi`.
  - Jika ada nilai seed yang **kosong, placeholder, atau tidak realistis** → tandai dan isi dengan nilai yang sesuai dengan konteks bisnis percetakan AbuCom berdasarkan REF-01 dan REF-05.

- [ ] **[VAL-1.11]** Bandingkan **query verifikasi (BAGIAN 5)** dengan isi seed data:
  - Pastikan angka expected result di komentar (`-- Hasil yang diharapkan: X`) sesuai dengan jumlah baris seed yang di-INSERT di BAGIAN 4.

- [ ] **[VAL-1.12]** Bandingkan **konfigurasi MySQL (BAGIAN 1)** dengan REF-03 (Tech Stack Decision):
  - Periksa: `SQL_MODE`, `NAMES utf8mb4`, `CHARACTER SET utf8mb4`, `COLLATE utf8mb4_unicode_ci`.
  - Periksa apakah `ENGINE=InnoDB` konsisten di semua tabel.
  - Pastikan semua konfigurasi sesuai dengan spesifikasi REF-03.

---

### FASE 2 — Validasi Relevansi (Tidak Ada yang Berlebihan / Out of Scope)

> **Tujuan:** Memastikan dokumen utama **hanya memuat** informasi yang memang termasuk dalam scope sebuah `database_schema.sql`. Tidak ada narasi panjang, logika aplikasi, pseudocode, atau data yang seharusnya ada di dokumen lain.

- [ ] **[VAL-2.1]** Periksa apakah ada komentar SQL yang bersifat narasi panjang / penjelasan bisnis yang seharusnya ada di dokumen lain (misal: BRD atau SRS), bukan di DDL SQL:
  - Komentar dalam DDL SQL **diperbolehkan** selama bersifat teknis (tipe data, constraint semantics, catatan implementasi MySQL).
  - Komentar yang hanya menduplikasi informasi dari REF-01/REF-05 tanpa nilai tambah teknis → pertimbangkan untuk diringkas atau dihapus.

- [ ] **[VAL-2.2]** Periksa apakah ada definisi **stored procedure, trigger, view, atau function** di dalam file ini:
  - Jika ada, evaluasi apakah memang seharusnya ada di file skema ini atau harus dipindah ke file terpisah sesuai konvensi REF-03.

- [ ] **[VAL-2.3]** Periksa apakah ada **kolom redundan** di antara tabel yang seharusnya tidak ada:
  - Contoh: apakah ada data yang seharusnya bisa di-JOIN dari tabel lain tetapi malah di-denormalize tanpa alasan yang jelas?
  - Jika ada, catat dan evaluasi apakah perlu dihapus atau ada justifikasi teknis yang kuat.

- [ ] **[VAL-2.4]** Periksa apakah `created_at` dan `updated_at` ada di **semua tabel** secara konsisten:
  - Semua tabel harus memiliki kedua kolom ini dengan tipe `TIMESTAMP NOT NULL` dan nilai default yang tepat.
  - Pastikan `updated_at` menggunakan `ON UPDATE CURRENT_TIMESTAMP`.

---

### FASE 3 — Validasi Standar Struktur Dokumen

> **Tujuan:** Memastikan struktur file DDL SQL memenuhi standar industri dan konsisten dari awal hingga akhir.

- [ ] **[VAL-3.1]** Periksa **HEADER & METADATA DOKUMEN** (Bagian Komentar Atas):
  - Harus ada: Nama Dokumen, Nama Proyek, Versi Dokumen, Tanggal Pembuatan, Penyusun, Status Dokumen, Deskripsi, Prasyarat, Instruksi Eksekusi.
  - Harus ada: Tabel RIWAYAT PERUBAHAN DOKUMEN dengan minimal satu entri.
  - Jika ada field yang kosong atau belum diisi → isi dengan nilai yang sesuai.

- [ ] **[VAL-3.2]** Periksa **urutan bagian dokumen**:
  - BAGIAN 1: Konfigurasi Awal & Pembuatan Database
  - BAGIAN 2: Pembuatan Tabel (CREATE TABLE) — dikelompokkan per tier dependency
  - BAGIAN 3: Pembuatan Index Tambahan (CREATE INDEX)
  - BAGIAN 4: Data Seed Awal (INSERT INTO)
  - BAGIAN 5: Verifikasi Integritas
  - BAGIAN 6: Restorasi Konfigurasi & Footer
  - REFERENSI DOKUMEN
  - Jika ada bagian yang hilang atau urutannya salah → perbaiki.

- [ ] **[VAL-3.3]** Periksa **pengelompokan tabel (KELOMPOK A, B, C, D, E)**:
  - Kelompok A: Tabel Induk (tanpa FK ke tabel lain) → hanya `cabang`.
  - Kelompok B: Tabel Master Level 2 (FK ke `cabang`) → `pengguna`, `pelanggan`, `supplier`, `barang`, `saldo_ppob`, `saldo_ewallet`, `system_configs`.
  - Kelompok C: Tabel Transaksional (FK ke tabel master) → tabel-tabel operasional.
  - Kelompok D: Tabel Administrasi & Keuangan → `utang_supplier`, `pinjaman_bank`, `pinjaman_kerabat`, `aset`.
  - Kelompok E: Tabel Audit & Rekonsiliasi → `audit_logs`, `backup_logs`, `stock_opname`, `riwayat_harga_supplier`.
  - Pastikan setiap tabel ditempatkan di kelompok yang tepat berdasarkan dependency FK-nya.

- [ ] **[VAL-3.4]** Periksa **naming convention** untuk semua identifier:
  - Nama tabel: `snake_case`, huruf kecil, Bahasa Indonesia.
  - Nama kolom: `snake_case`, huruf kecil, Bahasa Indonesia.
  - Nama constraint FK: `fk_[nama_tabel]_[nama_kolom]`.
  - Nama constraint UNIQUE: `uq_[nama_tabel]_[nama_kolom(s)]`.
  - Nama constraint CHECK: `chk_[nama_tabel]_[nama_kolom]`.
  - Nama index: `idx_[nama_tabel]_[nama_kolom(s)]`.
  - Jika ada pelanggaran naming convention → perbaiki secara konsisten.

- [ ] **[VAL-3.5]** Periksa **konsistensi tipe data** yang digunakan:
  - ID / primary key: `INT NOT NULL AUTO_INCREMENT`.
  - ID foreign key: `INT NOT NULL` (jika wajib) atau `INT NULL DEFAULT NULL` (jika opsional).
  - Nilai moneter / kuantitas: `DECIMAL(15,4)`.
  - String pendek (nama, kode): `VARCHAR(n)` dengan panjang yang wajar.
  - Teks panjang (deskripsi, alamat): `TEXT`.
  - Flag boolean: `BOOLEAN`.
  - Tanggal saja: `DATE`.
  - Tanggal + waktu: `TIMESTAMP`.
  - JSON blob: `JSON`.
  - Jika ada inkonsistensi → perbaiki.

- [ ] **[VAL-3.6]** Periksa **kelengkapan dan format COMMENT setiap tabel**:
  - Format wajib: `'[Deskripsi singkat] | Sensitivitas: [level] | Modul: M.[nomor]'`
  - Level sensitivitas yang valid (sesuai REF-02): `Operasional`, `Sensitif`, `Sangat Sensitif`.
  - Deskripsi harus tidak lebih dari 70 karakter untuk keterbacaan.

- [ ] **[VAL-3.7]** Periksa **COMMENT setiap kolom** — pastikan setiap kolom memiliki COMMENT yang:
  - Tidak kosong.
  - Tidak generik (hindari: "ID kolom ini", "nilai kolom ini").
  - Menjelaskan tujuan bisnis kolom dalam 1 kalimat ringkas.
  - Ditulis dalam Bahasa Indonesia yang natural.

- [ ] **[VAL-3.8]** Periksa **separator komentar** antar bagian untuk memastikan konsistensi visual:
  - Separator bagian besar: `-- ============================================================`
  - Separator bagian tabel: `-- ------------------------------------------------------------`
  - Label tabel: `-- [TABEL XX] nama_tabel`
  - Pastikan semua 28 tabel memiliki label yang benar dan berurutan (01 s.d. 28).

---

### FASE 4 — Validasi Kesiapan Sebagai Referensi SDLC Berikutnya

> **Tujuan:** Memastikan dokumen ini layak dijadikan input bagi fase-fase SDLC berikutnya (implementasi backend, unit testing, deployment, maintenance).

- [ ] **[VAL-4.1]** Periksa apakah **setiap tabel memiliki deskripsi yang cukup** untuk tim developer dapat:
  - Memahami tujuan tabel tanpa perlu membaca dokumen lain.
  - Memahami relasi tabel (FK) tanpa ambiguitas.
  - Mengetahui nilai-nilai valid untuk kolom enum/status (domain nilai harus tertulis di COMMENT atau keterangan inline).

- [ ] **[VAL-4.2]** Periksa apakah **domain nilai enum / status** terdokumentasi dengan jelas:
  - Kolom seperti `role`, `tipe_barang`, `status_pembayaran`, `status_pengambilan`, `metode_pembayaran`, `tipe_pelanggan`, `status_antrian`, `status_kehadiran`, `status_kasbon`, `metode_bayar_gaji`, `status_utang`, `status_pinjaman`, `status_perbaikan`, `status_poin`, `status_handover`, `status_opname`, `status_backup`, `action_type` — apakah nilai-nilai enum yang valid **disebutkan** di COMMENT kolom atau di komentar inline di atas kolom tersebut?
  - Jika belum ada → tambahkan komentar SQL di atas baris definisi kolom tersebut, contoh format:
    ```sql
    -- Nilai valid: 'AKTIF' | 'LUNAS'
    status_kasbon VARCHAR(20) NOT NULL DEFAULT 'AKTIF' COMMENT '...',
    ```

- [ ] **[VAL-4.3]** Periksa apakah **instruksi eksekusi** di header dokumen sudah lengkap dan benar:
  - Command eksekusi MySQL harus tepat dan dapat langsung di-copy-paste.
  - Prasyarat (versi MySQL, user privilege) harus disebutkan.

- [ ] **[VAL-4.4]** Periksa apakah **query verifikasi (BAGIAN 5)** mencakup semua aspek penting:
  - Minimal: verifikasi jumlah tabel, verifikasi baris seed per tabel yang di-INSERT.
  - Apakah ada verifikasi yang perlu ditambahkan? Misalnya: verifikasi FK (SHOW CREATE TABLE), atau verifikasi index (SHOW INDEX FROM [tabel]).
  - Jika ada yang perlu ditambahkan → tambahkan query verifikasi beserta komentar expected result-nya.

- [ ] **[VAL-4.5]** Periksa apakah ada **FK constraint yang bisa menyebabkan masalah saat eksekusi** (urutan CREATE TABLE):
  - Tabel yang memiliki FK harus dibuat **setelah** tabel yang direferensikannya.
  - Urutan saat ini (Kelompok A → B → C → D → E) harus valid secara dependency.
  - Jika ada pelanggaran urutan → catat dan perbaiki.

- [ ] **[VAL-4.6]** Periksa apakah **`DROP DATABASE IF EXISTS`** dan **`CREATE DATABASE`** di BAGIAN 1 sudah tepat:
  - Nama database: `abucom_db`.
  - Ini adalah file inisialisasi, bukan migration — `DROP DATABASE IF EXISTS` di awal adalah perilaku yang diharapkan.
  - Pastikan ada komentar peringatan eksplisit tepat sebelum baris `DROP DATABASE`:
    ```sql
    -- PERINGATAN: Script ini akan menghapus dan membuat ulang database abucom_db dari awal.
    -- Pastikan backup sudah dilakukan sebelum menjalankan script ini di lingkungan produksi.
    ```
  - Jika komentar peringatan belum ada → tambahkan.

---

### FASE 5 — Validasi Kualitas Bahasa Indonesia

> **Tujuan:** Memastikan seluruh teks Bahasa Indonesia dalam dokumen (terutama COMMENT tabel dan kolom) natural, baku, tidak ambigu, dan mudah dipahami oleh junior programmer atau LLM model yang lebih sederhana.

- [ ] **[VAL-5.1]** Baca ulang **COMMENT setiap tabel** (total 28 tabel):
  - Pastikan tidak ada kata yang salah eja (typo).
  - Pastikan kalimat tidak ambigu: satu kalimat = satu makna.
  - Pastikan menggunakan Bahasa Indonesia baku (hindari singkatan informal seperti "tsb", "dll", "utk", "yg" di dalam COMMENT).
  - Pastikan kata teknis (nama tabel, nama kolom, akronim) konsisten menggunakan format yang sama di seluruh dokumen.

- [ ] **[VAL-5.2]** Baca ulang **COMMENT setiap kolom** (total ±282 kolom):
  - Pastikan tidak ada kolom dengan COMMENT kosong atau COMMENT generik.
  - Pastikan COMMENT menjelaskan "apa tujuan kolom ini dalam konteks bisnis" — bukan hanya pengulangan nama kolom.
  - Contoh COMMENT yang **buruk**: `'ID kolom'`, `'Nilai nominal'`, `'Status data'`.
  - Contoh COMMENT yang **baik**: `'Identifikasi unik akun pengguna staf'`, `'Nominal uang muka Down Payment yang diterima kasir'`, `'Status pelunasan utang usaha tempo supplier'`.

- [ ] **[VAL-5.3]** Baca ulang seluruh **komentar header dan komentar bagian** (semua baris `--`):
  - Pastikan tidak ada typo atau kalimat yang terpotong.
  - Pastikan judul setiap bagian jelas dan informatif.

- [ ] **[VAL-5.4]** Periksa **konsistensi terminologi** di seluruh dokumen:
  - Istilah yang sama harus ditulis sama di seluruh file.
  - Pastikan terminologi kunci berikut digunakan secara konsisten: `pengguna`, `pelanggan`, `kasir`, `operator`, `supervisor`, `pemilik`, `cabang`, `barang`, `transaksi`, `nota`, `antrian`, `produksi`, `limbah`, `aset`, `payroll`, `kasbon`, `shift`, `PPOB`, `e-wallet`.
  - Contoh yang tidak konsisten: menyebut "kasir" di satu tempat dan "operator kasir" di tempat lain untuk entitas yang sama → standarkan ke satu pilihan.

---

### FASE 6 — Validasi Data Kosong & Placeholder

> **Tujuan:** Memastikan tidak ada data yang masih kosong, NULL yang tidak seharusnya, placeholder, atau nilai yang perlu diisi manual.

- [ ] **[VAL-6.1]** Periksa apakah ada nilai **DEFAULT** yang menggunakan angka `0` atau string kosong `''` padahal seharusnya ada nilai spesifik:
  - Khusus untuk kolom yang secara bisnis **tidak mungkin bernilai 0 atau kosong** saat pertama kali dibuat → evaluasi apakah DEFAULT-nya sudah benar.

- [ ] **[VAL-6.2]** Periksa nilai-nilai **seed data** di BAGIAN 4:
  - Apakah `password_hash` untuk akun `pemilik` menggunakan string yang realistis dan sesuai format bcrypt (format: `$2b$12$...`, panjang 60 karakter)?
  - Apakah alamat cabang seed cukup lengkap (termasuk RT/RW, kelurahan, kecamatan, kota, provinsi, kode pos)?
  - Apakah nomor telepon seed menggunakan format yang valid (diawali `0` atau `+62`)?
  - Apakah nilai-nilai saldo, biaya admin, limit harian pada seed `saldo_ewallet` sudah realistis untuk konteks bisnis percetakan di Indonesia?
  - Apakah semua 13 `parameter_value` pada seed `system_configs` terisi dengan nilai yang benar dan realistis (bukan placeholder seperti `'TODO'`, `'0'`, atau `''`)?
  - Jika ada yang tidak realistis atau kosong → ganti dengan nilai yang sesuai berdasarkan konteks bisnis REF-05 (BRD).

- [ ] **[VAL-6.3]** Periksa apakah ada **kolom dengan `NOT NULL` tanpa `DEFAULT`** yang berpotensi menyebabkan error insert jika tidak semua kolom disediakan saat runtime:
  - Ini adalah validasi keamanan DDL — pastikan setiap kolom `NOT NULL` tanpa DEFAULT memang disengaja (artinya nilai kolom tersebut selalu wajib disediakan oleh aplikasi).
  - Jika ada kolom `NOT NULL` tanpa DEFAULT yang seharusnya memiliki DEFAULT → tambahkan DEFAULT yang sesuai.

- [ ] **[VAL-6.4]** Periksa apakah ada **`TODO`**, **`FIXME`**, **`[ISI MANUAL]`**, atau **placeholder teks** lainnya di dalam file:
  - Jika ada → isi atau hapus sesuai konteks.

---

### FASE 7 — Validasi Tambahan Khusus DDL SQL

> **Tujuan:** Memastikan aspek-aspek teknis spesifik DDL SQL yang sering terlewat sudah benar.

- [ ] **[VAL-7.1]** Periksa apakah semua **nama constraint** bersifat unik di seluruh database:
  - MySQL mengharuskan nama constraint FK unik secara global di dalam satu database.
  - Pastikan tidak ada dua constraint berbeda yang memiliki nama yang sama.

- [ ] **[VAL-7.2]** Periksa **keberadaan kolom `cabang_id`** di seluruh tabel:
  - Semua tabel harus memiliki kolom `cabang_id INT NOT NULL DEFAULT 1` dengan FK ke `cabang(id)`.
  - `DEFAULT 1` digunakan untuk memastikan semua data secara default terikat ke cabang pertama (Toko Pusat).
  - Pastikan tidak ada tabel yang ketinggalan kolom `cabang_id`.

- [ ] **[VAL-7.3]** Periksa **semantik `ON DELETE` pada setiap FK**:
  - `ON DELETE CASCADE`: Gunakan hanya jika child record tidak bermakna tanpa parent (contoh: `detail_transaksi` → `transaksi`).
  - `ON DELETE RESTRICT`: Gunakan jika parent tidak boleh dihapus selama masih ada child (contoh: `pengguna` tidak boleh dihapus jika masih ada `transaksi` yang terkait).
  - `ON DELETE SET NULL`: Gunakan jika child boleh tetap ada dengan FK menjadi NULL (contoh: `transaksi.pelanggan_id` boleh NULL jika pelanggan dihapus).
  - Evaluasi setiap FK apakah semantiknya sudah benar secara bisnis berdasarkan REF-01 dan REF-05.

- [ ] **[VAL-7.4]** Periksa apakah **index pada kolom yang sering difilter** sudah ada:
  - Evaluasi berdasarkan use case di REF-04: apakah ada kolom yang sering digunakan dalam kondisi `WHERE`, `JOIN`, atau `ORDER BY` tetapi belum memiliki index di BAGIAN 3?
  - Jika ada → tambahkan index di BAGIAN 3 dengan format `CREATE INDEX idx_[tabel]_[kolom] ON [tabel]([kolom]);`.

- [ ] **[VAL-7.5]** Periksa apakah **`DECIMAL(15,4)`** sudah tepat untuk semua kolom moneter:
  - `DECIMAL(15,4)` = maksimum 15 digit total, 4 digit desimal. Artinya nilai maksimum adalah `99.999.999.999,9999`.
  - Pastikan presisi ini cukup untuk semua konteks (nominal pinjaman bank, nilai aset, dst).
  - Jika ada kolom yang nilainya bisa melebihi batas ini → perbesar presisi menjadi `DECIMAL(18,4)` atau sesuaikan.

- [ ] **[VAL-7.6]** Periksa apakah **`VARCHAR` length** pada setiap kolom sudah wajar:
  - `VARCHAR(50)` untuk `username`: apakah cukup?
  - `VARCHAR(255)` untuk `password_hash`: sesuai untuk output bcrypt (60 karakter), VARCHAR(255) aman.
  - `VARCHAR(50)` untuk `no_invoice`: apakah cukup untuk format `INV/YYYYMMDD/XXXX`?
  - Evaluasi dan sesuaikan jika ada yang terlalu pendek atau tidak masuk akal.

- [ ] **[VAL-7.7]** Periksa apakah **`BOOLEAN`** di kolom `disetujui_pemilik` pada tabel `pengeluaran` sudah tepat:
  - Di MySQL 8.x, `BOOLEAN` adalah alias untuk `TINYINT(1)`. Ini sudah benar.
  - Pastikan DEFAULT value-nya `FALSE` (atau `0`) dan COMMENT-nya menjelaskan makna `TRUE` dan `FALSE` secara bisnis.

- [ ] **[VAL-7.8]** Periksa apakah tabel `audit_logs` sudah mencakup **semua field yang dibutuhkan** untuk audit trail yang komprehensif:
  - Minimal harus ada: `pengguna_id`, `action_timestamp`, `action_type`, `target_table`, `old_value` (JSON), `new_value` (JSON), `cabang_id`.
  - Evaluasi apakah perlu menambahkan kolom `ip_address VARCHAR(45)` (alamat IP client) untuk kebutuhan forensik keamanan berdasarkan REF-02 dan REF-04.
  - Jika REF-02 atau REF-04 mengharuskan pencatatan IP → tambahkan kolom tersebut.

- [ ] **[VAL-7.9]** Periksa apakah tabel `backup_logs` sudah mencakup field yang cukup informatif:
  - Minimal: `tanggal_backup`, `nama_file`, `status_backup`, `pengguna_id`, `cabang_id`.
  - Evaluasi apakah perlu menambahkan `ukuran_file_kb BIGINT` (ukuran file backup) berdasarkan kebutuhan di REF-04.
  - Jika diperlukan → tambahkan dengan COMMENT yang jelas.

- [ ] **[VAL-7.10]** Periksa **restorasi konfigurasi di BAGIAN 6**:
  - Harus ada tiga baris restorasi: `SET SQL_MODE`, `SET FOREIGN_KEY_CHECKS`, `SET UNIQUE_CHECKS` — dikembalikan ke nilai semula menggunakan variabel `@OLD_*` yang disimpan di BAGIAN 1.
  - Pastikan urutannya kebalikan dari urutan SET di BAGIAN 1.

---

### FASE 8 — Kompilasi Temuan & Penulisan Ulang Dokumen

> **Tujuan:** Menuangkan seluruh hasil validasi ke dalam dokumen utama dengan cara menimpa (overwrite) penuh, tanpa pemotongan, tanpa penghilangan baris.

- [ ] **[TULIS-8.1]** Setelah semua fase validasi (1–7) selesai, kompilasi seluruh temuan:
  - Buat daftar internal semua item yang perlu diperbaiki (MISSING, MISMATCH, perlu ditambah, perlu diubah).
  - Kelompokkan per kategori: missing table/column, wrong type, missing constraint, wrong semantics, missing comment, missing seed, typo/bahasa, dll.

- [ ] **[TULIS-8.2]** Terapkan semua perbaikan ke dalam salinan kerja dokumen:
  - Mulai dari baris 1 (header metadata) hingga baris terakhir (baris kosong setelah REFERENSI DOKUMEN).
  - Pastikan **tidak ada baris yang dihilangkan** dari versi sebelumnya kecuali memang terbukti salah atau redundan berdasarkan temuan validasi.
  - Pastikan **tidak ada konten yang diringkas** atau dipotong dengan `...` atau sejenisnya.

- [ ] **[TULIS-8.3]** Perbarui **versi dokumen** di header:
  - Ubah `Versi Dokumen: 1.0` menjadi `Versi Dokumen: 1.1`.
  - Tambahkan baris baru di tabel RIWAYAT PERUBAHAN DOKUMEN:
    ```
    -- 1.1   | 2026-05-24 | Validasi & penyempurnaan menyeluruh     | Senior Database Architect & DDL Validation Expert
    ```

- [ ] **[TULIS-8.4]** Perbarui **status dokumen** di header:
  - Jika semua temuan sudah diselesaikan sepenuhnya → ubah menjadi `Status Dokumen: Final`.
  - Jika ada temuan yang ditunda (memerlukan keputusan bisnis) → ubah menjadi `Status Dokumen: Review`.

- [ ] **[TULIS-8.5]** Tulis ulang **seluruh isi dokumen** ke file target dengan cara **overwrite penuh**:
  - Target file: `docs/sdlc/03_design/01_database_schema.sql`
  - **WAJIB:** Tulis dari baris pertama hingga baris terakhir secara lengkap dan utuh.
  - **DILARANG KERAS:** Memotong, meringkas, atau menghilangkan baris apapun (`no truncation, no omission`).
  - **DILARANG KERAS:** Menyisipkan placeholder `[...]`, `(dst)`, `(lanjutan)`, atau notasi pemotongan apapun dalam isi file.
  - Pastikan file hasil dapat dieksekusi langsung di MySQL 8.x tanpa modifikasi tambahan.

- [ ] **[TULIS-8.6]** Verifikasi hasil penulisan dengan cara membaca ulang file yang baru ditulis:
  - Baca ulang baris pertama dokumen: pastikan header metadata sudah diperbarui (versi 1.1, status terbaru).
  - Baca ulang baris terakhir dokumen: pastikan bagian REFERENSI DOKUMEN masih ada dan lengkap.
  - Hitung jumlah statement `CREATE TABLE` di file hasil: harus tepat 28.
  - Hitung jumlah statement `INSERT INTO`: pastikan sesuai dengan semua grup seed yang didefinisikan.
  - Pastikan tidak ada baris yang terpotong atau hilang dibandingkan dengan versi sebelumnya ditambah semua perbaikan baru.

---

### FASE 9 — Pembaruan Referensi Dokumen

> **Tujuan:** Jika selama proses validasi ditemukan bahwa ada dokumen referensi baru yang digunakan (yang belum terdaftar di bagian REFERENSI DOKUMEN), maka dokumen tersebut harus ditambahkan.

- [ ] **[REF-9.1]** Identifikasi apakah selama proses validasi (Fase 1–7) kamu merujuk ke dokumen referensi **selain** REF-01 s.d. REF-05 yang sudah terdaftar:
  - Periksa apakah ada dokumen di `docs/sdlc/01_planning/` atau `docs/sdlc/02_analysis/` yang tidak ada di daftar referensi tetapi faktanya dijadikan acuan.
  - Jika ya, buat daftar dokumen referensi baru beserta path-nya dan kontribusinya.

- [ ] **[REF-9.2]** Jika ada referensi baru, tambahkan di bagian `-- REFERENSI DOKUMEN` di **baris paling bawah** dokumen (sebelum baris kosong penutup), dengan format yang konsisten:
  ```sql
  --
  -- [REF-06] [Nama Dokumen] v[versi]
  --          Path: docs/sdlc/[path]/[nama_file]
  --          Kontribusi: [Penjelasan kontribusi dokumen ini terhadap skema]
  ```

- [ ] **[REF-9.3]** Pastikan seluruh dokumen referensi yang terdaftar (REF-01 s.d. REF-0X) memiliki **format yang konsisten** satu sama lain (spasi, tanda baca, panjang baris komentar).

---

## Kriteria Keberhasilan (Definition of Done)

Issue ini dianggap **selesai dan berhasil** jika seluruh checklist di atas telah ditandai `[x]` DAN semua kriteria di bawah ini terpenuhi:

| No | Kriteria                                                                                                   | Status |
|----|------------------------------------------------------------------------------------------------------------|--------|
| 1  | Semua 28 tabel dari REF-01 sudah ada dan sesuai di dokumen utama                                          | [ ]    |
| 2  | Semua kolom di setiap tabel sesuai dengan REF-01 (nama, tipe, constraint, default, comment)                | [ ]    |
| 3  | Semua FK memiliki semantik `ON DELETE` yang benar secara bisnis                                            | [ ]    |
| 4  | Semua constraint CHECK merepresentasikan aturan domain nilai dari REF-01 dan REF-05                        | [ ]    |
| 5  | Semua nilai domain enum/status terdokumentasi di COMMENT atau komentar inline                              | [ ]    |
| 6  | Tingkat sensitivitas tabel pada COMMENT sesuai dengan REF-02                                               | [ ]    |
| 7  | Konfigurasi MySQL di BAGIAN 1 sesuai dengan spesifikasi REF-03                                             | [ ]    |
| 8  | Seed data lengkap, realistis, dan tidak mengandung placeholder                                             | [ ]    |
| 9  | Query verifikasi expected result sesuai dengan jumlah baris seed yang di-INSERT                            | [ ]    |
| 10 | Seluruh komentar ditulis dalam Bahasa Indonesia yang baku, natural, tidak ambigu                           | [ ]    |
| 11 | Tidak ada data kosong, TODO, FIXME, atau placeholder di seluruh dokumen                                    | [ ]    |
| 12 | Versi dokumen sudah diperbarui ke `1.1` dan riwayat perubahan sudah ditambahkan                           | [ ]    |
| 13 | File hasil dapat dieksekusi di MySQL 8.x tanpa error                                                       | [ ]    |
| 14 | Semua referensi yang digunakan terdaftar di bagian REFERENSI DOKUMEN                                       | [ ]    |

---

## Catatan Penting untuk Pelaksana

> **Baca ini sebelum memulai pekerjaan.**

1. **Jangan berasumsi.** Setiap keputusan teknis (tipe data, constraint, nilai default, COMMENT) harus dapat ditelusuri ke salah satu dokumen referensi (REF-01 s.d. REF-05). Jika tidak ada dasarnya di referensi manapun, dokumentasikan alasannya secara eksplisit dalam komentar SQL.

2. **Jangan meringkas atau memotong output.** Saat menulis ulang dokumen di TULIS-8.5, seluruh konten dari baris pertama hingga baris terakhir **harus** ditulis lengkap. Menggunakan `[...]`, `(baris berikutnya)`, atau notasi pemotongan apapun adalah pelanggaran kritis.

3. **Jangan mengubah yang tidak perlu.** Jika sebuah baris sudah benar dan sesuai referensi, jangan ubah hanya demi selera estetika. Perubahan hanya dilakukan jika ada temuan validasi yang konkret dan terdokumentasi.

4. **Urutan eksekusi SQL adalah kritis.** Jangan mengubah urutan CREATE TABLE sembarangan. Tabel yang direferensikan FK harus selalu didefinisikan **sebelum** tabel yang menggunakannya.

5. **Kerjakan satu tugas satu waktu.** Selesaikan setiap item checklist secara berurutan dari BACA-0.1 hingga REF-9.3. Jangan loncat-loncat antar fase karena temuan di Fase 1 bisa mempengaruhi pekerjaan di Fase berikutnya.

---

*Issue ini dibuat oleh: Senior Software Architect | Proyek: AbuCom | Tanggal: 2026-05-24*
