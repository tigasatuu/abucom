# Issue #0019 — Pembuatan dan Penyusunan Dokumen Data Dictionary

---

| Atribut         | Nilai                                                                         |
|-----------------|-------------------------------------------------------------------------------|
| **Judul**       | Pembuatan dan Penyusunan Dokumen Data Dictionary                              |
| **Dokumen Utama** | Data Dictionary                                                             |
| **Target File** | `docs/sdlc/02_analysis/05_data_dictionary.md`                                |
| **Status**      | 📋 Open — Belum Dikerjakan                                                    |
| **Prioritas**   | High                                                                          |
| **Tanggal Dibuat** | 2026-05-24                                                                 |
| **Dibuat Oleh** | Claude Opus 4.6 (Thinking) — Strategi Sistem & Perencanaan Dokumen           |
| **Dikerjakan Oleh** | Junior Programmer / LLM Model AI                                         |

---

## 1. Persona Pelaksana

**Persona yang ditugaskan**: **Senior Database Architect & Data Modeling Specialist**

**Alasan pemilihan persona**:
- Data Dictionary adalah dokumen yang mendefinisikan secara mendetail **setiap elemen data** dalam sistem: nama tabel, nama kolom, tipe data, constraint, relasi, domain nilai, dan deskripsi bisnis.
- Persona ini memiliki otoritas tertinggi dalam mendefinisikan skema data relasional, memahami normalisasi database, konvensi penamaan tabel/kolom MySQL, serta mampu menjembatani terminologi teknis database dengan kebutuhan bisnis operasional.
- Persona ini memastikan bahwa Data Dictionary yang dihasilkan layak dijadikan panduan implementasi langsung untuk penulisan `schema.sql`, `seed.sql`, dan kode Python pada fase SDLC berikutnya (Fase 03 Design dan Fase 04 Implementation).

---

## 2. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca secara menyeluruh** sebelum memulai penyusunan dokumen. File diurutkan berdasarkan prioritas relevansi terhadap Data Dictionary:

| No | Prioritas  | Nama File Referensi                        | Lokasi Path Relatif                                       | Alasan Pemilihan                                                                                                       |
|----|:----------:|--------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 1  | **PRIMER** | Software Requirements Specification (SRS)  | `docs/sdlc/02_analysis/02_software_requirements.md`       | Sumber utama definisi entitas data, atribut kolom, tipe data MySQL, constraint, relasi FK, dan model data konseptual (Bab 6 SRS). Seluruh 21+ tabel dan atributnya didefinisikan di sini. |
| 2  | **PRIMER** | Business Requirements Document (BRD)       | `docs/sdlc/02_analysis/01_business_requirements.md`       | Sumber aturan bisnis, domain nilai status, parameter konfigurasi, dan konteks deskripsi bisnis setiap elemen data.      |
| 3  | **SEKUNDER** | Use Case Diagram (UCD)                   | `docs/sdlc/02_analysis/03_use_case_diagram.md`            | Sumber pemetaan aktor-entitas, alur data masuk/keluar per use case, dan validasi kelengkapan atribut yang digunakan di setiap interaksi. |
| 4  | **SEKUNDER** | Workflow Diagram                         | `docs/sdlc/02_analysis/04_workflow_diagram.md`            | Sumber alur proses transaksional yang mengonfirmasi tabel dan kolom mana yang terlibat di setiap langkah workflow.       |
| 5  | **SEKUNDER** | Tech Stack Decision                      | `docs/sdlc/01_planning/04_tech_stack_decision.md`         | Sumber batasan teknis MySQL 8.4 LTS, InnoDB, tipe data DECIMAL(15,4), dan paradigma Functional Programming.            |
| 6  | **TERSIER** | Project Charter                           | `docs/sdlc/01_planning/01_project_charter.md`             | Konteks ruang lingkup proyek, 10 modul, dan deliverables yang mempengaruhi cakupan tabel database.                     |
| 7  | **TERSIER** | Innovation Proposal                       | `docs/sdlc/01_planning/05_innovation_proposal.md`         | Sumber fitur inovasi yang mungkin menambahkan entitas/atribut tambahan yang belum tercantum di BRD/SRS.                |
| 8  | **TERSIER** | Stakeholder Register                      | `docs/sdlc/01_planning/03_stakeholder_register.md`        | Konteks peran 8 aktor internal yang menentukan domain nilai kolom `role` pada tabel `pengguna`.                        |
| 9  | **TERSIER** | Feasibility Study                         | `docs/sdlc/01_planning/02_feasibility_study.md`           | Konteks parameter ekonomi (UMR, BEP, CAPEX) yang mempengaruhi nilai default pada tabel `system_configs`.               |

> **Catatan**: File `docs/sdlc/narasi.txt` **tidak lagi diperlukan** sebagai referensi langsung karena seluruh informasi narasi asli pemilik usaha sudah sepenuhnya diserap, diderivasi, dan diperinci ke dalam dokumen BRD v1.1 dan SRS v1.1.

---

## 3. Kerangka Struktur Dokumen Data Dictionary

Berikut adalah kerangka struktur dokumen Data Dictionary yang harus diikuti secara ketat. Struktur ini mengikuti standar praktik industri (*IEEE/ISO-style Data Dictionary*) yang disesuaikan dengan konteks proyek AbuCom:

```
---
(metadata YAML front matter)
---

# Data Dictionary — AbuCom

## Riwayat Perubahan Dokumen
(Tabel riwayat versi)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target
### 1.6. Konvensi Penulisan & Notasi

---

## 2. Ringkasan Model Data
### 2.1. Daftar Master Entitas (Tabel Database)
### 2.2. Diagram ER Konseptual (Mermaid)
### 2.3. Statistik Ringkasan Model Data

---

## 3. Spesifikasi Entitas dan Atribut Detail
### 3.1. Tabel: cabang
### 3.2. Tabel: pengguna
### 3.3. Tabel: pelanggan
### 3.4. Tabel: supplier
### 3.5. Tabel: barang
### 3.6. Tabel: bom_komposisi
### 3.7. Tabel: transaksi
### 3.8. Tabel: detail_transaksi
### 3.9. Tabel: antrian_kerja
### 3.10. Tabel: absensi
### 3.11. Tabel: kasbon
### 3.12. Tabel: payroll
### 3.13. Tabel: pengeluaran
### 3.14. Tabel: audit_logs
### 3.15. Tabel: limbah_produksi
### 3.16. Tabel: saldo_ppob
### 3.17. Tabel: jasa_service
### 3.18. Tabel: poin_insentif
### 3.19. Tabel: shift_handover
### 3.20. Tabel: utang_supplier
### 3.21. Tabel: backup_logs
### 3.22. Tabel: pinjaman_bank
### 3.23. Tabel: pinjaman_kerabat
### 3.24. Tabel: aset
### 3.25. Tabel: stock_opname
### 3.26. Tabel: riwayat_harga_supplier
### 3.27. Tabel: saldo_ewallet
### 3.28. Tabel: system_configs
(dan tabel lainnya yang ditemukan di file referensi)

---

## 4. Kamus Domain Nilai (Value Domain Dictionary)
### 4.1. Domain Status Pembayaran
### 4.2. Domain Status Pengambilan
### 4.3. Domain Tipe Pelanggan
### 4.4. Domain Tipe Barang
### 4.5. Domain Status Antrian Kerja
### 4.6. Domain Status Kehadiran
### 4.7. Domain Status Kasbon
### 4.8. Domain Tipe Pengeluaran
### 4.9. Domain Action Type Audit
### 4.10. Domain Peran Pengguna (Role)
### 4.11. Domain Metode Pembayaran
### 4.12. Domain Status Perbaikan Jasa Service
### 4.13. Domain Status Poin Insentif
### 4.14. Domain Status Handover
### 4.15. Domain Tipe Pinjaman
### 4.16. Domain Status Utang
### 4.17. Domain Status Backup
### 4.18. Domain Tipe Akun PPOB
(dan domain lainnya yang ditemukan di file referensi)

---

## 5. Relasi Antar-Entitas (Relationship Matrix)
### 5.1. Matriks Relasi Foreign Key
### 5.2. Diagram Relasional Lengkap (Mermaid ERD)
### 5.3. Daftar Constraint Integritas Referensial

---

## 6. Aturan Bisnis Data (Data Business Rules)
### 6.1. Aturan Validasi Input
### 6.2. Aturan Komputasi & Formula
### 6.3. Aturan Constraint Database
### 6.4. Aturan Default Value

---

## 7. Indeks dan Optimasi Database
### 7.1. Daftar Primary Key
### 7.2. Daftar Unique Constraint
### 7.3. Rekomendasi Index Tambahan

---

## 8. Matriks Ketertelusuran (Traceability Matrix)
### 8.1. Pemetaan Entitas → Modul Fungsional
### 8.2. Pemetaan Entitas → Kebutuhan BRD/SRS

---

## 9. Glosarium Istilah Data

---

## 10. Referensi Dokumen
```

---

## 4. Spesifikasi Format Tabel per Entitas

Untuk setiap tabel database pada **Bagian 3 (Spesifikasi Entitas dan Atribut Detail)**, gunakan format tabel standar berikut secara konsisten:

### 4.1. Header Informasi Tabel

```markdown
### 3.X. Tabel: `nama_tabel`

| Atribut Tabel     | Nilai                                                  |
|-------------------|--------------------------------------------------------|
| **Nama Tabel**    | `nama_tabel`                                           |
| **Deskripsi**     | [Deskripsi bisnis tabel dalam 1-2 kalimat]             |
| **Modul Terkait** | M.X — [Nama Modul]                                    |
| **Derivasi SRS**  | SRS-F-XXX                                              |
| **Derivasi BRD**  | BR-F-XX                                                |
| **Engine MySQL**  | InnoDB                                                 |
| **Charset**       | utf8mb4                                                |
| **Collation**     | utf8mb4_unicode_ci                                     |
```

### 4.2. Tabel Detail Atribut/Kolom

```markdown
| No | Nama Kolom        | Tipe Data MySQL   | Constraint                    | Null? | Default         | Deskripsi Bisnis                                | Domain Nilai           |
|----|-------------------|-------------------|-------------------------------|:-----:|-----------------|------------------------------------------------|------------------------|
| 1  | `id`              | INT               | PK, AUTO_INCREMENT            | NOT NULL | -            | Identifikasi unik baris data.                  | Auto-generated integer |
| 2  | `nama_xxx`        | VARCHAR(100)      | -                             | NOT NULL | -            | [Deskripsi kolom]                              | Free text              |
| 3  | `cabang_id`       | INT               | FK → `cabang.id`              | NOT NULL | 1            | Identifikasi unit cabang multi-branch ready.   | Referensi `cabang.id`  |
```

### 4.3. Catatan Tambahan per Tabel (opsional)

```markdown
> **Catatan Implementasi**:
> - [Catatan teknis khusus tabel ini]
> - [Aturan bisnis spesifik tabel ini]
```

---

## 5. Instruksi Implementasi (Tahapan Checklist)

### Fase A — Persiapan dan Pembacaan File Referensi

- [ ] **A.1** — Baca **seluruh** isi file `docs/sdlc/02_analysis/02_software_requirements.md` dari baris pertama hingga baris terakhir **tanpa terpotong**. Fokus utama pada:
  - [ ] A.1.1 — Bab 2.4 (Lingkungan Operasi) — catat versi library dan database engine.
  - [ ] A.1.2 — Bab 2.5 (Batasan Desain) — catat aturan presisi `DECIMAL(15,4)` dan `cabang_id`.
  - [ ] A.1.3 — Bab 3 (Spesifikasi Kebutuhan Fungsional) — catat **seluruh** nama kolom input/output yang disebutkan di setiap SRS-F-XXX (dari SRS-F-001 hingga SRS-F-040 dan SRS-F-ADD-01 hingga SRS-F-ADD-05).
  - [ ] A.1.4 — Bab 4 (Spesifikasi Non-Fungsional) — catat batasan tipe data dan metrik performa.
  - [ ] A.1.5 — **Bab 6 (Model Data Konseptual)** — ini adalah sumber paling kritis. Catat **semua 21+ tabel** beserta **seluruh atribut kolom**, tipe data, constraint PK/FK, dan relasi antar-tabel yang tercantum di Bagian 6.1 dan 6.2.
  - [ ] A.1.6 — Bab 7 (RTM - Requirements Traceability Matrix) — catat pemetaan SRS → Modul → Tabel Database.
  - [ ] A.1.7 — Bab 10 (Lampiran) — catat Daftar Parameter `system_configs`, Daftar Kode Error, dan Domain Status.

- [ ] **A.2** — Baca **seluruh** isi file `docs/sdlc/02_analysis/01_business_requirements.md` dari baris pertama hingga baris terakhir **tanpa terpotong**. Fokus pada:
  - [ ] A.2.1 — Bab 5.3 (RBAC Hak Akses) — catat 8 domain nilai peran pengguna.
  - [ ] A.2.2 — Bab 7 (Kebutuhan Bisnis Fungsional) — catat aturan bisnis dan domain nilai status di setiap BR-F-XX.
  - [ ] A.2.3 — Bab 8 (Kebutuhan Non-Fungsional) — catat batasan teknis database.
  - [ ] A.2.4 — Bab 9 (Aturan Bisnis Numerik Eksplisit) — catat nilai-nilai numerik default untuk `system_configs`.
  - [ ] A.2.5 — Bab 12 (Manajemen Risiko) — catat parameter risiko yang mempengaruhi data (misal dana cadangan darurat).

- [ ] **A.3** — Baca **seluruh** isi file `docs/sdlc/02_analysis/03_use_case_diagram.md` dari baris pertama hingga baris terakhir **tanpa terpotong**. Fokus pada:
  - [ ] A.3.1 — Bab 3.2 (Master Daftar Use Case) — catat pemetaan UC → tabel yang terlibat.
  - [ ] A.3.2 — Bab 5 (Spesifikasi Naratif) — validasi atribut input/output di setiap alur use case.

- [ ] **A.4** — Baca **seluruh** isi file `docs/sdlc/02_analysis/04_workflow_diagram.md` dari baris pertama hingga baris terakhir **tanpa terpotong**. Fokus pada:
  - [ ] A.4.1 — Identifikasi tabel dan kolom yang disebutkan di setiap narasi prosedural workflow.
  - [ ] A.4.2 — Validasi bahwa setiap data yang mengalir antar-modul memiliki entitas dan atribut yang terdefinisi.

- [ ] **A.5** — Baca isi file `docs/sdlc/01_planning/04_tech_stack_decision.md`. Fokus pada:
  - [ ] A.5.1 — Catat versi MySQL (8.4 LTS), engine (InnoDB), charset (utf8mb4), dan library Python.
  - [ ] A.5.2 — Catat batasan paradigma Functional Programming yang mempengaruhi pola akses data.

- [ ] **A.6** — Baca isi file `docs/sdlc/01_planning/01_project_charter.md`. Fokus pada:
  - [ ] A.6.1 — Catat cakupan 10 modul dan pemetaannya ke entitas data.

- [ ] **A.7** — Baca isi file `docs/sdlc/01_planning/05_innovation_proposal.md`. Fokus pada:
  - [ ] A.7.1 — Identifikasi fitur inovasi yang mungkin menambahkan tabel/kolom baru yang belum ada di SRS.

- [ ] **A.8** — Baca isi file `docs/sdlc/01_planning/03_stakeholder_register.md`. Fokus pada:
  - [ ] A.8.1 — Catat 19 stakeholder dan pemetaan 8 role internal untuk domain nilai `role` di tabel `pengguna`.

- [ ] **A.9** — Baca isi file `docs/sdlc/01_planning/02_feasibility_study.md`. Fokus pada:
  - [ ] A.9.1 — Catat parameter ekonomi (UMR, target laba, dana cadangan) untuk domain nilai `system_configs`.

---

### Fase B — Inventarisasi dan Konsolidasi Data

- [ ] **B.1** — Buat daftar master **seluruh entitas (tabel database)** yang ditemukan di semua file referensi. Pastikan mencakup minimal tabel-tabel berikut (sesuai SRS v1.1 Bab 6.1):
  - [ ] B.1.1 — `cabang`
  - [ ] B.1.2 — `pengguna`
  - [ ] B.1.3 — `pelanggan`
  - [ ] B.1.4 — `supplier`
  - [ ] B.1.5 — `barang`
  - [ ] B.1.6 — `bom_komposisi`
  - [ ] B.1.7 — `transaksi`
  - [ ] B.1.8 — `detail_transaksi`
  - [ ] B.1.9 — `antrian_kerja`
  - [ ] B.1.10 — `absensi`
  - [ ] B.1.11 — `kasbon`
  - [ ] B.1.12 — `payroll`
  - [ ] B.1.13 — `pengeluaran`
  - [ ] B.1.14 — `audit_logs`
  - [ ] B.1.15 — `limbah_produksi`
  - [ ] B.1.16 — `saldo_ppob`
  - [ ] B.1.17 — `jasa_service`
  - [ ] B.1.18 — `poin_insentif`
  - [ ] B.1.19 — `shift_handover`
  - [ ] B.1.20 — `utang_supplier`
  - [ ] B.1.21 — `backup_logs`
  - [ ] B.1.22 — `pinjaman_bank` (disebutkan di SRS-F-025)
  - [ ] B.1.23 — `pinjaman_kerabat` (disebutkan di SRS-F-025)
  - [ ] B.1.24 — `aset` (disebutkan di SRS-F-028)
  - [ ] B.1.25 — `stock_opname` (disebutkan di SRS-F-011)
  - [ ] B.1.26 — `riwayat_harga_supplier` (disebutkan di SRS-F-013)
  - [ ] B.1.27 — `saldo_ewallet` (disebutkan di SRS-F-016 dan RTM Backward)
  - [ ] B.1.28 — `system_configs` (disebutkan di SRS-F-038 dan Lampiran 10.1)

- [ ] **B.2** — Untuk setiap tabel, konsolidasikan **seluruh atribut/kolom** dari semua file referensi. Jika ada kolom yang disebutkan di SRS Input/Output tetapi belum tercantum di Bab 6.1 SRS, **tetap masukkan** ke Data Dictionary dan berikan catatan sumber derivasinya.

- [ ] **B.3** — Buat daftar master **seluruh domain nilai (value domains)** yang disebutkan di file referensi. Contoh:
  - [ ] B.3.1 — `status_pembayaran`: 'LUNAS', 'BELUM LUNAS', 'BATAL', 'RETUR'
  - [ ] B.3.2 — `status_antrian`: 'Antri', 'Proses Desain', 'Produksi', 'Selesai', 'Diambil'
  - [ ] B.3.3 — `role`: 'pemilik', 'kepala_percetakan', 'pramuniaga', 'kasir', 'desainer', 'produksi_cetak', 'fotocopy_print', 'gudang'
  - [ ] B.3.4 — Dan seluruh domain lainnya yang ditemukan di file referensi.

- [ ] **B.4** — Buat daftar master **seluruh relasi Foreign Key** antar-tabel berdasarkan data di SRS Bab 6.1 dan Bab 6.2.

- [ ] **B.5** — Identifikasi dan catat semua **tabel atau kolom yang disebutkan secara implisit** di SRS (misalnya dalam bagian Input/Logika Bisnis/Output) tetapi belum memiliki definisi eksplisit di Bab 6.1 SRS. Beri tanda `[DATA KOSONG — PERLU KONFIRMASI MANUAL]` pada item tersebut.

---

### Fase C — Penyusunan Dokumen

- [ ] **C.1** — Tulis bagian **metadata YAML front matter** di baris paling atas file target. Format:
  ```yaml
  ---
  dokumen    : Data Dictionary
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [tanggal pengerjaan dalam format YYYY-MM-DD]
  status     : Draft
  penyusun   : Senior Database Architect & Data Modeling Specialist
  ---
  ```

- [ ] **C.2** — Tulis bagian **Riwayat Perubahan Dokumen** dalam format tabel markdown (kolom: Versi, Tanggal, Perubahan, Oleh).

- [ ] **C.3** — Tulis **Bab 1 (Informasi Dokumen)** lengkap:
  - [ ] C.3.1 — Tujuan Dokumen: jelaskan bahwa dokumen ini mendefinisikan secara detail seluruh elemen data dalam database MySQL AbuCom.
  - [ ] C.3.2 — Cakupan Dokumen: sebutkan jumlah total tabel, jumlah total atribut, jumlah domain nilai, dll.
  - [ ] C.3.3 — Posisi Dokumen dalam SDLC: jelaskan bahwa Data Dictionary adalah artefak **kelima dan terakhir** pada Fase 02 Analysis, setelah BRD, SRS, UCD, dan Workflow Diagram. Jelaskan posisinya sebagai jembatan ke Fase 03 Design (ERD fisik dan `schema.sql`).
  - [ ] C.3.4 — Hubungan dengan Dokumen SDLC Lainnya: jelaskan relasi input (BRD, SRS, UCD, Workflow) dan output (ERD, schema.sql, seed.sql, SDD).
  - [ ] C.3.5 — Audiens Target: Pemilik Usaha/Junior Programmer, Tim AI, Calon Karyawan.
  - [ ] C.3.6 — Konvensi Penulisan & Notasi: jelaskan konvensi tipe data MySQL yang digunakan (INT, VARCHAR, DECIMAL, TEXT, DATE, TIMESTAMP, JSON, BOOLEAN), konvensi penamaan kolom (snake_case), dan simbol-simbol yang dipakai (PK, FK, UQ, NN, AI, dsb).

- [ ] **C.4** — Tulis **Bab 2 (Ringkasan Model Data)**:
  - [ ] C.4.1 — Buat tabel ringkasan daftar master seluruh entitas (kolom: No, Nama Tabel, Deskripsi Singkat, Modul Terkait, Jumlah Kolom, Derivasi SRS).
  - [ ] C.4.2 — Salin dan sesuaikan diagram ER Konseptual Mermaid dari SRS Bab 6.3, perluas jika ada tabel tambahan yang ditemukan (misalnya `pinjaman_bank`, `pinjaman_kerabat`, `aset`, `stock_opname`, `riwayat_harga_supplier`, `saldo_ewallet`, `system_configs`).
  - [ ] C.4.3 — Tulis statistik ringkasan (total tabel, total kolom, total FK, total domain nilai).

- [ ] **C.5** — Tulis **Bab 3 (Spesifikasi Entitas dan Atribut Detail)** — ini adalah inti dokumen:
  - [ ] C.5.1 — Untuk **setiap tabel**, tulis header informasi tabel sesuai format di Bagian 4.1 issue ini.
  - [ ] C.5.2 — Untuk **setiap tabel**, tulis tabel detail atribut/kolom sesuai format di Bagian 4.2 issue ini. Pastikan:
    - [ ] Setiap kolom memiliki: No urut, Nama Kolom, Tipe Data MySQL yang tepat (INT, VARCHAR(n), DECIMAL(15,4), TEXT, DATE, TIMESTAMP, JSON, BOOLEAN), Constraint (PK/FK/UQ/INDEX), Nullable (NOT NULL atau NULL), Default Value, Deskripsi Bisnis yang jelas dalam bahasa Indonesia, dan Domain Nilai jika berupa enum/status.
    - [ ] Kolom `id` selalu di urutan pertama dengan `INT, PK, AUTO_INCREMENT, NOT NULL`.
    - [ ] Kolom `cabang_id` (INT, FK → `cabang.id`, NOT NULL, Default: 1) selalu ada di **setiap tabel utama** sesuai mandat Multi-Branch Ready (SRS-F-037).
    - [ ] Kolom timestamp (`created_at`, `updated_at`) ditambahkan di setiap tabel jika belum ada, sesuai best practice audit data.
  - [ ] C.5.3 — Untuk setiap tabel, tambahkan **Catatan Implementasi** jika ada aturan khusus (misalnya: "Kolom `old_value` dan `new_value` menggunakan tipe data native JSON MySQL" atau "Kolom `stok_saat_ini` wajib mendukung angka desimal negatif untuk stok minus").
  - [ ] C.5.4 — Jika ada **tabel yang disebutkan di SRS/BRD tetapi definisi kolomnya tidak lengkap atau tidak ada**, definisikan struktur kolomnya berdasarkan konteks bisnis dari BRD/SRS, dan beri tanda `[DERIVASI — definisi kolom diturunkan dari konteks SRS/BRD karena belum didefinisikan eksplisit di Bab 6.1 SRS]`.

- [ ] **C.6** — Tulis **Bab 4 (Kamus Domain Nilai)** — dokumentasikan semua value domain:
  - [ ] C.6.1 — Untuk setiap domain, buat tabel dengan kolom: Nilai, Label, Deskripsi, dan Sumber (BRD/SRS reference ID).
  - [ ] C.6.2 — Pastikan domain mencakup semua nilai enum/status yang disebutkan di SRS Bab 6.1, Bab 3, dan Lampiran 10.2.

- [ ] **C.7** — Tulis **Bab 5 (Relasi Antar-Entitas)**:
  - [ ] C.7.1 — Buat matriks relasi FK lengkap (kolom: Tabel Asal, Kolom FK, Tabel Referensi, Kolom Referensi, Tipe Relasi, ON DELETE, ON UPDATE).
  - [ ] C.7.2 — Buat diagram ERD Mermaid yang lengkap mencakup **seluruh tabel** beserta relasi (perluas dari SRS Bab 6.3 yang hanya mencantumkan 21 tabel).
  - [ ] C.7.3 — Dokumentasikan constraint integritas referensial (CASCADE, RESTRICT, SET NULL, dll).

- [ ] **C.8** — Tulis **Bab 6 (Aturan Bisnis Data)**:
  - [ ] C.8.1 — Aturan Validasi Input: rangkum semua aturan validasi dari SRS Bab 3 (misal: "Kuantitas barang HARUS > 0", "WhatsApp HARUS format `^628[0-9]{8,11}$`").
  - [ ] C.8.2 — Aturan Komputasi & Formula: rangkum semua formula matematika dari SRS (HPP BOM, Margin, Smart Payroll, Depresiasi, dll).
  - [ ] C.8.3 — Aturan Constraint Database: catat constraint CHECK, UNIQUE, NOT NULL yang harus diterapkan.
  - [ ] C.8.4 — Aturan Default Value: catat semua default value dari Lampiran 10.1 SRS (`system_configs`).

- [ ] **C.9** — Tulis **Bab 7 (Indeks dan Optimasi Database)**:
  - [ ] C.9.1 — Daftar Primary Key untuk setiap tabel.
  - [ ] C.9.2 — Daftar Unique Constraint (misal: `username` di `pengguna`, `no_invoice` di `transaksi`).
  - [ ] C.9.3 — Rekomendasi Index tambahan berdasarkan SRS (misal: composite index pada `tanggal_transaksi` + `cabang_id` sesuai SRS-F-026).

- [ ] **C.10** — Tulis **Bab 8 (Matriks Ketertelusuran)**:
  - [ ] C.10.1 — Pemetaan Entitas → Modul Fungsional (M.1 s.d M.10).
  - [ ] C.10.2 — Pemetaan Entitas → Kebutuhan BRD (BR-F-XX) dan SRS (SRS-F-XXX).

- [ ] **C.11** — Tulis **Bab 9 (Glosarium Istilah Data)**: definisikan istilah-istilah teknis database yang dipakai di dokumen ini (PK, FK, UQ, AUTO_INCREMENT, CASCADE, InnoDB, DECIMAL, VARCHAR, INDEX, UNIQUE, ACID, dll).

- [ ] **C.12** — Tulis **Bab 10 (Referensi Dokumen)**: cantumkan seluruh file referensi yang digunakan dalam penyusunan dokumen ini sesuai tabel di Bagian 2 issue ini.

---

### Fase D — Validasi dan Penandaan Data Kosong

- [ ] **D.1** — Lakukan cross-check: pastikan **setiap tabel yang disebutkan di RTM Backward SRS (Bab 7.2)** sudah tercantum di Data Dictionary.

- [ ] **D.2** — Lakukan cross-check: pastikan **setiap kolom input/output yang disebutkan di SRS Bab 3** (SRS-F-001 s.d SRS-F-040 dan SRS-F-ADD-01 s.d SRS-F-ADD-05) sudah memiliki definisi di tabel yang sesuai di Data Dictionary.

- [ ] **D.3** — Lakukan cross-check: pastikan **setiap domain nilai status** yang disebutkan di SRS sudah terdokumentasi di Bab 4 (Kamus Domain Nilai).

- [ ] **D.4** — Untuk setiap data yang **tidak ditemukan** atau **kosong** di file referensi (misalnya: definisi kolom tabel yang hanya disebut namanya tanpa detail atribut), berikan penandaan berikut di baris yang relevan:

  ```markdown
  > ⚠️ **[DATA KOSONG — PERLU KONFIRMASI MANUAL]**: [Deskripsi data apa yang kosong dan alasan mengapa data ini tidak ditemukan di file referensi.]
  ```

- [ ] **D.5** — Pastikan tidak ada tabel yang hanya punya `id` dan `cabang_id` tanpa kolom fungsional lainnya. Jika ada, itu indikasi ada data yang terlewat — periksa kembali file referensi.

---

### Fase E — Penulisan Hasil ke Target File

- [ ] **E.1** — Tuangkan **seluruh** hasil penyusunan dokumen Data Dictionary ke dalam file target: `docs/sdlc/02_analysis/05_data_dictionary.md`.

- [ ] **E.2** — Pastikan file output menggunakan encoding **UTF-8** dan format **Markdown** yang valid.

- [ ] **E.3** — Pastikan seluruh tabel markdown ter-render dengan benar (kolom sejajar, separator `|---|` lengkap).

- [ ] **E.4** — Pastikan seluruh diagram Mermaid menggunakan sintaks yang valid dan dapat di-render.

- [ ] **E.5** — Pastikan **tidak ada konten yang terpotong** (truncated) di bagian mana pun dari dokumen. Jika dokumen panjang, tetap tulis lengkap dari awal sampai akhir tanpa pemotongan.

- [ ] **E.6** — Lakukan pembacaan ulang terakhir: pastikan dokumen menggunakan **bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami**.

---

## 6. Instruksi Tambahan (Best Practice Data Dictionary)

### 6.1. Konsistensi Penamaan
- Seluruh nama tabel dan kolom menggunakan konvensi **snake_case** huruf kecil.
- Nama tabel menggunakan bentuk **tunggal** (singular), bukan jamak (misal: `transaksi`, bukan `transaksi_list`).
- Kolom Foreign Key menggunakan format `[nama_tabel_referensi]_id` (misal: `cabang_id`, `pengguna_id`, `supplier_id`).

### 6.2. Standar Tipe Data MySQL
- Kolom ID primary key: `INT AUTO_INCREMENT`.
- Kolom string pendek (nama, username, role, status): `VARCHAR(n)` dengan panjang disesuaikan.
- Kolom string panjang (deskripsi, alamat, catatan): `TEXT`.
- Kolom keuangan dan kuantitas presisi: `DECIMAL(15,4)` — **wajib**, dilarang menggunakan `FLOAT` atau `DOUBLE`.
- Kolom tanggal saja: `DATE`.
- Kolom tanggal + waktu: `TIMESTAMP` dengan `DEFAULT CURRENT_TIMESTAMP`.
- Kolom data terstruktur audit: `JSON`.
- Kolom boolean: `BOOLEAN` (alias `TINYINT(1)` di MySQL).

### 6.3. Kolom Wajib di Setiap Tabel
Setiap tabel **wajib** memiliki kolom-kolom berikut sebagai standar:
- `id` (INT, PK, AUTO_INCREMENT)
- `cabang_id` (INT, FK → `cabang.id`, NOT NULL, DEFAULT 1) — Mandat Multi-Branch Ready SRS-F-037.
- `created_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP) — Jika belum ada di SRS, tetap tambahkan sebagai best practice audit trail.
- `updated_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) — Jika belum ada di SRS, tetap tambahkan sebagai best practice audit trail.

### 6.4. Kualitas Deskripsi Bisnis
- Setiap kolom **wajib** memiliki deskripsi bisnis yang menjelaskan **apa** data tersebut, **untuk apa** digunakan, dan **dari mana** data tersebut berasal dalam konteks operasional toko AbuCom.
- Deskripsi harus ditulis dalam bahasa Indonesia yang natural dan tidak menggunakan jargon teknis tanpa penjelasan.
- Contoh deskripsi yang baik: "Nominal uang muka yang dibayarkan pelanggan di awal pesanan cetak kustom sebelum barang jadi."
- Contoh deskripsi yang buruk: "DP field."

### 6.5. Kelengkapan dan Kualitas
- Dokumen ini harus **lengkap** dan **self-contained**: seseorang yang membaca Data Dictionary ini harus bisa memahami **seluruh struktur database** AbuCom tanpa perlu membuka dokumen SRS atau BRD.
- Dokumen ini harus layak dijadikan **panduan implementasi langsung** untuk menuliskan `schema.sql` di Fase 03 Design.
- Kualitas dokumen harus sedemikian rupa sehingga **tidak perlu dipertanyakan ulang** oleh tim pengembang di fase SDLC berikutnya.

---

## 7. Kriteria Selesai (Definition of Done)

Issue ini dianggap **selesai** jika:

- [ ] Seluruh checklist di Fase A sampai Fase E sudah berstatus `[x]` (tercentang selesai).
- [ ] File `docs/sdlc/02_analysis/05_data_dictionary.md` telah terisi lengkap dari bagian metadata YAML hingga bagian Referensi Dokumen.
- [ ] Seluruh tabel database (minimal 28 tabel) sudah terdokumentasi dengan detail atribut lengkap.
- [ ] Seluruh domain nilai sudah terdokumentasi di Bab 4.
- [ ] Seluruh relasi FK sudah terdokumentasi di Bab 5.
- [ ] Diagram ERD Mermaid lengkap dan valid di Bab 5.
- [ ] Matriks traceability lengkap di Bab 8.
- [ ] Data yang kosong sudah diberi penandaan `[DATA KOSONG — PERLU KONFIRMASI MANUAL]`.
- [ ] Bahasa Indonesia yang digunakan natural, jelas, dan tidak ambigu.
- [ ] Tidak ada konten yang terpotong (truncated).
- [ ] Dokumen layak dijadikan referensi utama bagi Fase 03 Design (ERD dan schema.sql).

---

## 8. Referensi File yang Digunakan dalam Pembuatan Issue Ini

| No | Nama File                          | Lokasi Path Relatif                                       | Keterangan                                                 |
|----|------------------------------------|------------------------------------------------------------|-----------------------------------------------------------|
| 1  | Software Requirements Specification | `docs/sdlc/02_analysis/02_software_requirements.md`       | Sumber utama definisi entitas, atribut, dan model data.    |
| 2  | Business Requirements Document      | `docs/sdlc/02_analysis/01_business_requirements.md`       | Sumber aturan bisnis dan domain nilai status.              |
| 3  | Use Case Diagram                    | `docs/sdlc/02_analysis/03_use_case_diagram.md`            | Sumber pemetaan aktor-entitas dan alur interaksi.          |
| 4  | Workflow Diagram                    | `docs/sdlc/02_analysis/04_workflow_diagram.md`            | Sumber alur transaksional dan tabel yang terlibat.         |
| 5  | Tech Stack Decision                 | `docs/sdlc/01_planning/04_tech_stack_decision.md`         | Sumber batasan teknis MySQL dan paradigma FP.              |
| 6  | Project Charter                     | `docs/sdlc/01_planning/01_project_charter.md`             | Sumber ruang lingkup 10 modul proyek.                     |
| 7  | Innovation Proposal                 | `docs/sdlc/01_planning/05_innovation_proposal.md`         | Sumber fitur inovasi tambahan.                            |
| 8  | Stakeholder Register                | `docs/sdlc/01_planning/03_stakeholder_register.md`        | Sumber domain nilai peran pengguna (8 role).               |
| 9  | Feasibility Study                   | `docs/sdlc/01_planning/02_feasibility_study.md`           | Sumber parameter ekonomi dan default config.               |
