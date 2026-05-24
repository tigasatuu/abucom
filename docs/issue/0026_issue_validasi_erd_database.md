---
judul      : Validasi & Perbaikan Dokumen ERD Database AbuCom
target_file: docs/sdlc/03_design/02_erd_database.md
fase_sdlc  : 03 — Design
prioritas  : Tinggi
status     : Open
dibuat_oleh: Senior Database Architect & Data Modeling Specialist
tanggal    : 2026-05-24
---

# Validasi & Perbaikan Dokumen ERD Database AbuCom

## 1. Latar Belakang & Tujuan Issue

Dokumen **ERD Database** (`docs/sdlc/03_design/02_erd_database.md`) merupakan deliverable visual kritis pada Fase 03 Design yang berfungsi sebagai peta arsitektur data relasional resmi sistem AbuCom. Dokumen ini menjadi **referensi utama** bagi backend developer, AI coding assistant, dan DBA dalam mengimplementasikan query JOIN, RBAC decorator, dan logika transaksional Python.

Issue ini bertujuan memastikan bahwa dokumen ERD Database telah:
1. Merangkum **seluruh** data dari dokumen referensi tanpa ada yang terlewat.
2. Hanya memuat data yang **relevan dan spesifik** untuk dokumen ERD (tidak memuat konten luar domain).
3. Memenuhi **standar struktur dokumen industri** yang lengkap dan informatif.
4. **Layak dijadikan input** bagi fase SDLC selanjutnya tanpa ambiguitas.
5. Ditulis dalam **Bahasa Indonesia yang natural** dan mudah dipahami oleh junior programmer maupun LLM model AI yang lebih kecil.
6. Bebas dari **data kosong, placeholder, atau nilai yang perlu diisi manual**.

---

## 2. Persona Validator

> **Kamu adalah Senior Database Architect & ERD Specialist** dengan keahlian:
> - Lebih dari 10 tahun pengalaman dalam pemodelan data relasional MySQL/PostgreSQL untuk sistem ERP skala UKM hingga enterprise.
> - Sertifikasi resmi MySQL Database Administrator (Oracle Certified Professional).
> - Keahlian mendalam dalam Crow's Foot ERD notation, normalisasi database (1NF–3NF/BCNF), dan pola desain database multi-tenant/multi-branch.
> - Pengalaman memvalidasi dan menulis dokumentasi teknis SDLC (ERD, Data Dictionary, Database Schema) yang dijadikan referensi produksi oleh tim pengembang junior dan LLM AI.
> - Memahami konteks bisnis sistem manajemen percetakan: transaksi kasir, antrian produksi cetak, payroll, PPOB, CRM pelanggan, dan manajemen aset.
>
> **Kamu wajib bertindak sebagai validator yang kritis, teliti, dan tidak toleran terhadap kelemahan dokumentasi** yang dapat menyebabkan ambiguitas implementasi pada fase-fase SDLC berikutnya.

---

## 3. Dokumen yang Terlibat

### 3.1. Dokumen Target (Dokumen Utama yang Divalidasi)
| Peran | Path Berkas |
|---|---|
| **Target (Dokumen Utama)** | `docs/sdlc/03_design/02_erd_database.md` |

### 3.2. Dokumen Referensi (Sumber Kebenaran Validasi)
| No | Kode | Nama Dokumen | Path Berkas |
|:---:|---|---|---|
| 1 | REF-01 | Database Schema SQL | `docs/sdlc/03_design/01_database_schema.sql` |
| 2 | REF-02 | Data Dictionary | `docs/sdlc/02_analysis/05_data_dictionary.md` |
| 3 | REF-03 | Access Control Matrix | `docs/sdlc/02_analysis/06_access_control_matrix.md` |
| 4 | REF-04 | Software Requirements Specification (SRS) | `docs/sdlc/02_analysis/02_software_requirements.md` |
| 5 | REF-05 | Business Requirements Document (BRD) | `docs/sdlc/02_analysis/01_business_requirements.md` |
| 6 | REF-06 | Tech Stack Decision | `docs/sdlc/01_planning/04_tech_stack_decision.md` |

---

## 4. Instruksi Implementasi — Tahapan Step-by-Step

Ikuti seluruh tahapan berikut **secara berurutan dari atas ke bawah**. Jangan melewati satu tahapan pun. Tandai setiap item `[ ]` menjadi `[x]` setelah selesai dikerjakan.

---

### FASE 0 — Persiapan & Pembacaan Dokumen

> Tujuan: Memuat seluruh konteks yang dibutuhkan ke dalam memori sebelum memulai validasi apapun.

- [ ] **0.1.** Baca seluruh isi file target dari baris pertama hingga baris terakhir:
  ```
  Baca file: docs/sdlc/03_design/02_erd_database.md
  ```
  Catat: (a) versi dokumen saat ini, (b) total bab/seksi, (c) daftar referensi yang tercantum di bagian akhir dokumen.

- [ ] **0.2.** Baca seluruh isi REF-01 — Database Schema SQL dari baris pertama hingga baris terakhir:
  ```
  Baca file: docs/sdlc/03_design/01_database_schema.sql
  ```
  Catat: (a) total tabel, (b) total kolom per tabel, (c) semua nama constraint (PK, FK, UQ, CHECK), (d) semua nama index, (e) semua aturan `ON DELETE` / `ON UPDATE` per FK, (f) seed data yang ada.

- [ ] **0.3.** Baca seluruh isi REF-02 — Data Dictionary dari baris pertama hingga baris terakhir:
  ```
  Baca file: docs/sdlc/02_analysis/05_data_dictionary.md
  ```
  Catat: (a) total tabel yang terdaftar, (b) statistik atribut per tabel, (c) kode traceability SRS-F-xxx yang tercantum, (d) daftar enum/domain nilai yang terdefinisi.

- [ ] **0.4.** Baca seluruh isi REF-03 — Access Control Matrix dari baris pertama hingga baris terakhir:
  ```
  Baca file: docs/sdlc/02_analysis/06_access_control_matrix.md
  ```
  Catat: (a) level sensitivitas data per tabel (Operasional/Sensitif/Sangat Sensitif), (b) aturan RBAC per role per modul.

- [ ] **0.5.** Baca seluruh isi REF-04 — SRS dari baris pertama hingga baris terakhir:
  ```
  Baca file: docs/sdlc/02_analysis/02_software_requirements.md
  ```
  Catat: (a) kode SRS-F-001 s.d SRS-F-040, (b) entitas database yang dirujuk per kode SRS, (c) aturan bisnis spesifik yang berdampak pada desain ERD.

- [ ] **0.6.** Baca seluruh isi REF-05 — BRD dari baris pertama hingga baris terakhir:
  ```
  Baca file: docs/sdlc/02_analysis/01_business_requirements.md
  ```
  Catat: (a) kode BR-F-01 s.d BR-F-40, (b) batasan komputasi bisnis (payroll, depresiasi, HPP, limit kasbon) yang berdampak pada kolom tabel ERD.

- [ ] **0.7.** Baca seluruh isi REF-06 — Tech Stack Decision dari baris pertama hingga baris terakhir:
  ```
  Baca file: docs/sdlc/01_planning/04_tech_stack_decision.md
  ```
  Catat: (a) konfigurasi teknis MySQL (engine, charset, collation, versi), (b) konvensi penamaan objek database.

---

### FASE 1 — Validasi Kelengkapan Data (Komparasi dengan Referensi)

> Tujuan: Memastikan dokumen ERD **tidak ada yang terlewat** dari dokumen referensi.

#### 1.A. Komparasi dengan REF-01 (Database Schema SQL)

- [ ] **1.A.1.** Hitung total tabel yang didefinisikan dalam `01_database_schema.sql`. Bandingkan dengan total tabel yang terdokumentasi di ERD (Bab 2.1 dan Bab 3). **Harus sama persis — 28 tabel.**
  - Jika ada tabel di SQL yang tidak ada di ERD → catat sebagai temuan **[MISSING_TABLE]**.

- [ ] **1.A.2.** Untuk setiap tabel, bandingkan **jumlah dan nama kolom** di SQL vs ERD (Bab 4). Periksa satu per satu:
  - `cabang`, `pengguna`, `pelanggan`, `supplier`, `barang`, `saldo_ppob`, `saldo_ewallet`, `system_configs`
  - `bom_komposisi`, `transaksi`, `detail_transaksi`, `antrian_kerja`, `absensi`, `kasbon`, `payroll`, `pengeluaran`, `limbah_produksi`, `jasa_service`, `poin_insentif`, `shift_handover`
  - `utang_supplier`, `pinjaman_bank`, `pinjaman_kerabat`, `aset`
  - `audit_logs`, `backup_logs`, `stock_opname`, `riwayat_harga_supplier`
  - Jika ada kolom di SQL yang tidak muncul di diagram Mermaid ERD → catat sebagai **[MISSING_COLUMN]**.
  - Jika ada kolom di ERD yang tidak ada di SQL → catat sebagai **[PHANTOM_COLUMN]**.

- [ ] **1.A.3.** Bandingkan **tipe data** setiap kolom di SQL vs notasi tipe data di diagram ERD Mermaid. Contoh: SQL `DECIMAL(15,4)` harus dicatat sebagai `decimal` di ERD; SQL `TINYINT(1)` = `boolean`; SQL `BIGINT` = `bigint`. Catat setiap ketidaksesuaian sebagai **[TYPE_MISMATCH]**.

- [ ] **1.A.4.** Bandingkan **annotation constraint** (PK, FK, UQ) per kolom di diagram Mermaid ERD vs SQL. Catat setiap annotation yang salah atau hilang sebagai **[CONSTRAINT_MISMATCH]**.

- [ ] **1.A.5.** Hitung total relasi FK di Matriks Bab 5.1 (harus 58 baris). Bandingkan satu per satu setiap FK dengan definisi `FOREIGN KEY` di SQL, termasuk:
  - Nama kolom FK (child).
  - Nama tabel parent.
  - Nama kolom referensi (PK parent).
  - Aturan `ON DELETE` dan `ON UPDATE`.
  - Jika ada FK di SQL yang tidak ada di matriks → catat **[MISSING_FK]**.
  - Jika ada FK di matriks yang tidak ada di SQL → catat **[PHANTOM_FK]**.
  - Jika `ON DELETE` atau `ON UPDATE` berbeda → catat **[FK_RULE_MISMATCH]**.

- [ ] **1.A.6.** Bandingkan **seluruh nama CHECK constraint** di Bab 5.3 vs SQL. Pastikan:
  - Nama constraint sama persis.
  - Ekspresi validasi (nilai batas: >, >=, <=) sama persis.
  - Catat perbedaan sebagai **[CHECK_MISMATCH]** atau **[MISSING_CHECK]**.

- [ ] **1.A.7.** Periksa apakah **Unique Composite Constraint** di Bab 5.3 sudah mencakup semua `UNIQUE KEY` / `UNIQUE INDEX` komposit yang ada di SQL. Catat yang terlewat sebagai **[MISSING_UQ]**.

- [ ] **1.A.8.** Periksa apakah **Additional Composite Index** (non-FK, non-PK, non-UQ) yang didefinisikan di SQL juga terdokumentasi di ERD (bisa di Bab 5.3 atau Bab 7). Catat yang terlewat sebagai **[MISSING_INDEX]**.

- [ ] **1.A.9.** Verifikasi **statistik di Bab 2.1** (Total Tabel, Total Kolom, Total Relasi FK, Total Unique Constraint, Total CHECK Constraint, Total Index Tambahan) apakah sesuai dengan hitungan aktual di SQL. Koreksi angka yang salah.

#### 1.B. Komparasi dengan REF-02 (Data Dictionary)

- [ ] **1.B.1.** Bandingkan **daftar domain/enum nilai** yang terdefinisi di Data Dictionary vs nilai enum yang tercantum dalam deskripsi kolom di diagram ERD Mermaid (bagian kolom komentar `"..."` pada setiap atribut). Misalnya: `status_pembayaran` harus mencantumkan semua nilai enum: `LUNAS/BELUM LUNAS/BATAL/RETUR`. Catat yang kurang lengkap sebagai **[ENUM_INCOMPLETE]**.

- [ ] **1.B.2.** Verifikasi **kode traceability SRS-F-xxx** di Kamus Entitas Bab 6 (kolom "Jenis Derivasi"). Bandingkan dengan kode SRS yang tercantum di Data Dictionary. Pastikan setiap tabel yang bukan derivasi memiliki kode SRS yang benar dan valid. Catat yang salah sebagai **[SRS_CODE_MISMATCH]**.

- [ ] **1.B.3.** Bandingkan **jumlah kolom per tabel** di kolom "Jumlah Kolom" Bab 6 vs hitungan aktual kolom di SQL. Koreksi angka yang tidak sesuai.

#### 1.C. Komparasi dengan REF-03 (Access Control Matrix)

- [ ] **1.C.1.** Bandingkan **level sensitivitas** di Bab 6 kolom "Sensitivitas" (Operasional/Sensitif/Sangat Sensitif) vs klasifikasi level sensitivitas yang tercantum di ACM. Pastikan setiap tabel memiliki level yang konsisten. Catat yang berbeda sebagai **[SENSITIVITY_MISMATCH]**.

#### 1.D. Komparasi dengan REF-04 & REF-05 (SRS & BRD)

- [ ] **1.D.1.** Periksa apakah **contoh query SQL** di Bab 8.3 sudah mencakup representasi modul-modul yang paling kompleks dan kritikal menurut SRS (minimal Modul Transaksi M.1, Antrian M.5, dan SDM M.4). Jika ada modul kritis SRS yang belum direpresentasikan dengan contoh query → tambahkan query yang relevan.

- [ ] **1.D.2.** Periksa apakah **batasan komputasi bisnis** dari BRD (threshold payroll, limit kasbon, margin depresiasi, persentase bunga bank) yang berdampak pada kolom ERD sudah disebutkan dalam deskripsi kolom atau Catatan Desain Bab 7. Catat yang terlewat sebagai **[BRD_CONSTRAINT_MISSING]**.

#### 1.E. Komparasi dengan REF-06 (Tech Stack Decision)

- [ ] **1.E.1.** Verifikasi apakah **konfigurasi teknis MySQL** (Engine InnoDB, Charset utf8mb4, Collation utf8mb4_unicode_ci, Versi MySQL 8.x LTS) sudah disebutkan dengan benar di dokumen ERD (Bab 1 atau Bab 7). Koreksi jika ada ketidaksesuaian dengan Tech Stack Decision.

---

### FASE 2 — Validasi Relevansi Konten (Kebersihan Dokumen)

> Tujuan: Memastikan dokumen ERD **tidak memuat konten di luar domain** yang seharusnya ada dalam dokumen ini.

- [ ] **2.1.** Periksa apakah ada **logika aplikasi (application logic)** yang tidak seharusnya ada dalam dokumen ERD, misalnya: pseudocode Python, flow diagram proses bisnis, wireframe UI, atau spesifikasi API endpoint. Hapus jika ditemukan.

- [ ] **2.2.** Periksa apakah ada **duplikasi konten** antara bab-bab di ERD — misalnya, penjelasan yang persis sama muncul di dua tempat berbeda tanpa tujuan yang jelas. Jika ada, ringkas atau hilangkan duplikasi tersebut.

- [ ] **2.3.** Periksa apakah **deskripsi kolom** di diagram Mermaid ERD (Bab 4) hanya berisi informasi yang memang relevan untuk dokumen ERD (nama kolom, tipe data, constraint, deskripsi singkat domain bisnis). Bukan spesifikasi pengkodean Python, validasi form UI, atau spesifikasi REST API.

- [ ] **2.4.** Periksa apakah **Catatan Desain Bab 7** hanya berisi keputusan arsitektural **level database** (pola desain skema, filosofi foreign key, pola penamaan), bukan keputusan arsitektural level aplikasi atau infrastruktur.

- [ ] **2.5.** Periksa apakah **contoh query SQL Bab 8.3** hanya menampilkan query yang benar-benar relevan untuk menggambarkan cara membaca ERD — bukan query DML penginputan data, prosedur tersimpan, atau trigger yang berlebihan.

---

### FASE 3 — Validasi Standar Struktur Dokumen (Industri Praktik)

> Tujuan: Memastikan ERD Database memenuhi standar kelengkapan dokumen teknis industri yang profesional.

- [ ] **3.1.** Periksa apakah **header YAML frontmatter** (baris 1-8) sudah lengkap dan benar berisi: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`. Lengkapi field yang kosong dengan nilai yang sesuai.

- [ ] **3.2.** Periksa apakah **Tabel Riwayat Perubahan Dokumen** (Change Log) sudah ada di bagian paling awal dokumen dengan kolom: Versi, Tanggal, Perubahan, Oleh. Pastikan ada minimal satu entri riwayat yang valid.

- [ ] **3.3.** Periksa apakah **Bab 1 Informasi Dokumen** sudah mencakup semua sub-seksi standar berikut:
  - [ ] **1.1.** Tujuan Dokumen — menjelaskan *mengapa* dokumen ini dibuat.
  - [ ] **1.2.** Cakupan Dokumen — menjelaskan *apa saja* yang dicakup (jumlah tabel, FK, kelompok).
  - [ ] **1.3.** Posisi Dokumen dalam SDLC — menampilkan posisi ERD dalam alur SDLC.
  - [ ] **1.4.** Hubungan dengan Dokumen SDLC Lainnya — daftar input dan output dokumen.
  - [ ] **1.5.** Audiens Target — siapa pembaca dokumen ini dan bagaimana cara membacanya.
  - [ ] **1.6.** Konvensi Notasi ERD & Legenda Simbol — tabel notasi Crow's Foot dan kunci simbol yang digunakan.

- [ ] **3.4.** Periksa apakah **Bab 2 Ringkasan Model Data** sudah mencakup:
  - [ ] **2.1.** Statistik Ringkasan (angka-angka akurat yang terverifikasi dari Fase 1).
  - [ ] **2.2.** Klasifikasi Kelompok Tabel — diagram ASCII dan tabel pengelompokan fungsional 5 kelompok.

- [ ] **3.5.** Periksa apakah **Bab 3 Diagram ERD Utama** menyajikan satu diagram Mermaid `erDiagram` tunggal yang menampilkan seluruh 28 tabel dengan fokus pada PK, FK, UQ, dan relasi antar tabel. Diagram ini harus bisa dirender oleh Mermaid.js tanpa error syntax.

- [ ] **3.6.** Periksa apakah **Bab 4 Sub-Diagram Modular** sudah menyajikan diagram terpisah untuk masing-masing 5 kelompok fungsional (A, B, C, D, E) dengan **seluruh nama kolom, tipe data, constraint, dan deskripsi**. Tidak boleh ada kolom yang hilang di diagram modular.

- [ ] **3.7.** Periksa apakah **Bab 5 Matriks Relasi & Kardinalitas** sudah lengkap dengan:
  - [ ] **5.1.** Tabel matriks FK lengkap 58 baris dengan kolom: No, Tabel Asal, Kolom FK, Tabel Referensi, Kolom Referensi, Tipe Relasi, ON DELETE, ON UPDATE, Keterangan Aturan Bisnis.
  - [ ] **5.2.** Penjelasan aturan integritas referensial (ON DELETE RESTRICT / CASCADE / SET NULL).
  - [ ] **5.3.** Daftar Constraint Komposit (Unique Composite + CHECK Constraints).

- [ ] **3.8.** Periksa apakah **Bab 6 Kamus Entitas Ringkas** menampilkan tabel 28 baris dengan kolom: No, Nama Tabel, Kelompok, Jumlah Kolom, Modul Terkait, FK Keluar, FK Masuk, Sensitivitas, Jenis Derivasi. Semua angka harus akurat.

- [ ] **3.9.** Periksa apakah **Bab 7 Catatan Desain & Keputusan Arsitektural** sudah membahas minimal pola desain berikut yang bersifat unik pada skema AbuCom:
  - [ ] **7.1.** Pola Multi-Cabang (`cabang_id` sebagai FK universal).
  - [ ] **7.2.** Pola Audit Trail (`created_at`/`updated_at` universal).
  - [ ] **7.3.** Pola Self-Referencing FK (`bom_komposisi` → `barang`).
  - [ ] **7.4.** Pola Nullable FK (kasus opsional bisnis).
  - [ ] **7.5.** Pola Tabel Derivasi (7 tabel tambahan di luar SRS dasar).

- [ ] **3.10.** Periksa apakah **Bab 8 Panduan Pembacaan Diagram** sudah mencakup:
  - [ ] **8.1.** Cara Membaca Notasi Kardinalitas dengan contoh kalimat bisnis nyata.
  - [ ] **8.2.** Petunjuk Penggunaan ERD untuk Backend Developer (ACID transaction, Decimal precision, RBAC).
  - [ ] **8.3.** Minimal 3 contoh query SQL JOIN yang merepresentasikan skenario bisnis berbeda berdasarkan peta relasi ERD.

- [ ] **3.11.** Periksa apakah **Bab 9 Referensi Dokumen** (atau bab terakhir) sudah menampilkan tabel referensi lengkap dengan kolom: No, Kode Ref, Nama Dokumen Acuan, Path Berkas Relatif, Kontribusi Konten Terhadap ERD. Semua REF-01 s.d REF-06 harus ada.

---

### FASE 4 — Validasi Kelayakan sebagai Referensi Fase SDLC Selanjutnya

> Tujuan: Memastikan dokumen ERD siap digunakan sebagai input utama untuk fase implementasi (coding), testing, dan deployment.

- [ ] **4.1.** Periksa apakah setiap **entitas (tabel)** di ERD memiliki informasi yang cukup bagi backend developer untuk menulis query SQL tanpa harus kembali membaca file `01_database_schema.sql`:
  - Nama tabel, seluruh nama kolom, tipe data, constraint (PK/FK/UQ), dan deskripsi singkat bisnis.
  - Jika ada kolom tanpa deskripsi → tambahkan deskripsi singkat yang informatif.

- [ ] **4.2.** Periksa apakah **aturan bisnis kritis** yang mempengaruhi logika query sudah tercantum, misalnya:
  - Kolom nullable vs NOT NULL yang mempengaruhi penggunaan `LEFT JOIN` vs `INNER JOIN`.
  - Kolom dengan default value yang mempengaruhi INSERT logic.
  - Kolom dengan CHECK constraint yang mempengaruhi validasi input.
  - Jika belum tercantum → tambahkan catatan pada bab yang relevan.

- [ ] **4.3.** Periksa apakah **contoh query JOIN** di Bab 8.3 sudah mendemonstrasikan penggunaan `LEFT JOIN` untuk kolom FK nullable (misalnya: `transaksi.pelanggan_id` yang bisa NULL untuk walk-in customer). Jika belum → tambahkan satu contoh query yang relevan.

- [ ] **4.4.** Periksa apakah **Kamus Entitas Ringkas** Bab 6 sudah mencantumkan kolom "Modul Terkait" dengan kode modul yang benar (M.1 s.d M.10) sehingga backend developer dapat dengan mudah mengidentifikasi tabel mana yang relevan dengan modul CLI yang sedang diimplementasikan.

- [ ] **4.5.** Pastikan **tidak ada bab atau seksi yang berisi placeholder** seperti: `[TODO]`, `[TBD]`, `[Perlu diisi]`, `N/A`, atau teks template yang belum diganti. Isi semua placeholder dengan konten aktual yang sesuai.

---

### FASE 5 — Validasi Kualitas Bahasa Indonesia

> Tujuan: Memastikan seluruh teks dalam Bahasa Indonesia natural, tidak ambigu, dan mudah dipahami oleh junior programmer maupun LLM model AI yang lebih kecil.

- [ ] **5.1.** Baca ulang **Bab 1 (Informasi Dokumen)** secara keseluruhan. Periksa:
  - Apakah setiap kalimat menggunakan struktur Subjek-Predikat-Objek yang jelas?
  - Apakah ada istilah teknis bahasa Inggris yang digunakan tanpa penjelasan atau padanan Bahasa Indonesia yang kontekstual?
  - Perbaiki kalimat yang ambigu atau terlalu panjang (>3 klausa dalam satu kalimat).

- [ ] **5.2.** Periksa **konsistensi terminologi** di seluruh dokumen:
  - Istilah yang sama harus selalu menggunakan kata yang sama. Contoh: jangan campurkan "kasbon" dan "pinjaman karyawan" untuk merujuk hal yang sama.
  - Nama tabel database harus selalu ditulis dalam backtick `` `nama_tabel` ``.
  - Nama kolom database harus selalu ditulis dalam backtick `` `nama_kolom` ``.
  - Catat ketidakkonsistenan sebagai **[TERMINOLOGY_INCONSISTENT]**.

- [ ] **5.3.** Periksa **label relasi pada diagram Mermaid** (teks dalam tanda kutip setelah tanda titik dua): apakah label tersebut ditulis dalam Bahasa Indonesia yang deskriptif dan menggambarkan arah relasi bisnis secara jelas? Hindari label generik seperti `"has"` atau `"ref"`. Perbaiki label yang tidak informatif.

- [ ] **5.4.** Periksa **deskripsi kolom** dalam diagram Mermaid (teks dalam tanda kutip setelah nama kolom): apakah setiap deskripsi sudah singkat (maksimal 7 kata), jelas, dan tidak menggunakan singkatan yang tidak lazim? Perbaiki yang tidak informatif.

- [ ] **5.5.** Periksa **Bab 7 (Catatan Desain)** dan **Bab 8 (Panduan Pembacaan)**: apakah penjelasannya sudah cukup self-explanatory sehingga junior programmer yang baru bergabung bisa langsung memahami tanpa perlu bertanya?

- [ ] **5.6.** Periksa **keterangan aturan bisnis** di Bab 5.1 (kolom "Keterangan Aturan Bisnis"): apakah setiap keterangan menjelaskan **mengapa** aturan FK tersebut dipilih, bukan hanya **apa** yang terjadi? Perbaiki yang hanya mendeskripsikan mekanisme tanpa konteks bisnis.

---

### FASE 6 — Validasi Kelengkapan & Ketiadaan Interupsi Proses

> Tujuan: Memastikan dokumen tidak akan selalu dipertanyakan atau diinterupsi selama proses kerja fase berikutnya.

- [ ] **6.1.** Simulasikan pertanyaan yang mungkin diajukan junior programmer saat membaca dokumen ini:
  - "Kolom apa saja yang nullable di tabel X?" → Periksa apakah informasi ini bisa ditemukan dari ERD atau catatan Bab 7.4. Jika tidak → tambahkan tabel ringkasan kolom nullable per entitas yang memiliki nullable FK.
  - "Apa nilai valid untuk kolom `status_pembayaran`?" → Periksa apakah enum values sudah tercantum di deskripsi kolom ERD. Jika tidak → tambahkan.
  - "Bagaimana cara menghitung `gaji_bersih`?" → Periksa apakah formula bisnis sudah ada. Jika tidak → tambahkan di Bab 7 atau deskripsi kolom `payroll`.

- [ ] **6.2.** Periksa apakah **relasi One-to-One antara `transaksi` dan `antrian_kerja`** sudah dijelaskan dengan cukup (termasuk implikasinya: tidak setiap transaksi memiliki antrian kerja — hanya transaksi jasa cetak kustom). Jika penjelasan kurang → lengkapi di Bab 7 atau Bab 5.

- [ ] **6.3.** Periksa apakah **pola multi-FK ke tabel `pengguna`** dalam tabel `antrian_kerja` (desainer_id, produksi_id), `shift_handover` (kasir_keluar_id, kasir_masuk_id, supervisor_id), dan `stock_opname` (pengguna_id, supervisor_id) sudah dijelaskan dengan cukup — termasuk mengapa beberapa FK ini nullable. Jika belum → tambahkan penjelasan di Bab 7.4.

- [ ] **6.4.** Periksa apakah **self-referencing FK** di `bom_komposisi` (barang_induk_id dan bahan_baku_id keduanya merujuk ke `barang.id`) sudah cukup dijelaskan dengan contoh nyata data bisnis (contoh: Stempel Bulat → Karet Gagang + Tinta). Jika contoh tidak ada atau tidak jelas → tambahkan.

- [ ] **6.5.** Periksa apakah terdapat **anomali potensial** yang belum terdokumentasi:
  - Apakah mungkin `kas_awal` + akumulasi transaksi tidak sama dengan `kas_sistem` dalam `shift_handover`? Apakah formula ini sudah dijelaskan?
  - Apakah kolom `selisih` di `stock_opname` merupakan hasil komputasi atau input manual? Apakah sudah dijelaskan?
  - Apakah hubungan `poin_insentif` ↔ `payroll` (poin dikonversi ke `bonus_insentif`) sudah terdokumentasi dalam ERD?
  - Jika belum → tambahkan catatan relevan di Bab 7 atau Bab 8.

---

### FASE 7 — Identifikasi & Pengisian Data Kosong / Placeholder

> Tujuan: Tidak boleh ada data kosong, nilai `N/A`, placeholder, atau konten yang "perlu diisi manual" setelah fase validasi ini selesai.

- [ ] **7.1.** Scan seluruh dokumen dari baris pertama hingga baris terakhir. Cari semua kemunculan teks berikut (case-insensitive):
  ```
  [TODO], [TBD], [Perlu diisi], [Akan diisi], N/A, TBD, TODO,
  "...", placeholder, contoh sementara, coming soon, belum tersedia
  ```
  Catat setiap lokasi (nomor bab dan baris) sebagai **[PLACEHOLDER_FOUND]**.

- [ ] **7.2.** Untuk setiap `[PLACEHOLDER_FOUND]` yang ditemukan:
  - Identifikasi data apa yang seharusnya mengisi placeholder tersebut berdasarkan konteks dokumen dan data yang tersedia di file referensi (REF-01 s.d REF-06).
  - Isi placeholder tersebut dengan data aktual yang sesuai, cocok, dan masih dalam ruang lingkup dokumen ERD.
  - **Jangan biarkan satu pun placeholder tersisa setelah tahapan ini.**

- [ ] **7.3.** Periksa apakah ada **sel tabel yang kosong** di bab manapun. Jika ada → isi dengan data yang valid berdasarkan referensi.

- [ ] **7.4.** Periksa **versi dokumen** di header YAML frontmatter dan Tabel Riwayat Perubahan. Versi **wajib dinaikkan** dari `1.0` menjadi `1.1` (atau dari versi saat ini ke versi berikutnya) sebagai tanda telah melalui proses validasi dan revisi.

---

### FASE 8 — Penulisan Ulang Dokumen ke File Target

> **PERHATIAN KRITIS**: Tahapan ini adalah tahapan penulisan final. Baca seluruh instruksi sebelum mengeksekusi.

- [ ] **8.1.** Sebelum menulis, lakukan **review akhir** terhadap seluruh temuan dari Fase 1 s.d Fase 7. Susun daftar semua perubahan yang akan dilakukan.

- [ ] **8.2.** Tulis ulang **seluruh dokumen** dari baris pertama hingga baris terakhir ke file target yang sama:
  ```
  Target file: docs/sdlc/03_design/02_erd_database.md
  Mode       : OVERWRITE (timpa seluruh konten lama)
  ```

- [ ] **8.3.** Aturan penulisan yang **wajib dipatuhi secara mutlak**:
  - [ ] **8.3.a.** Tulis seluruh teks dari baris pertama (`---` header YAML) hingga baris terakhir (baris referensi terakhir) **tanpa ada yang dipotong, diringkas, atau dihilangkan**. **NO TRUNCATION**.
  - [ ] **8.3.b.** Semua bab, sub-bab, tabel, diagram Mermaid, contoh query SQL, deskripsi, dan catatan harus **ditulis lengkap sepenuhnya**.
  - [ ] **8.3.c.** Versi dokumen di **header YAML frontmatter** (baris `versi:`) harus diubah — contoh: dari `1.0` menjadi `1.1`.
  - [ ] **8.3.d.** Tanggal di header YAML frontmatter (baris `tanggal:`) harus diperbarui ke tanggal pelaksanaan validasi ini.
  - [ ] **8.3.e.** Status dokumen di header YAML frontmatter (baris `status:`) harus diubah dari `Draft` menjadi `Review` atau `Final` sesuai hasil validasi.
  - [ ] **8.3.f.** Tambahkan **satu baris baru** di Tabel Riwayat Perubahan Dokumen yang mencatat: versi baru, tanggal hari ini, ringkasan perubahan yang dilakukan, dan nama persona validator.
  - [ ] **8.3.g.** Seluruh diagram Mermaid `erDiagram` harus **ditulis ulang lengkap** — tidak boleh ada diagram yang dipotong atau disingkat.
  - [ ] **8.3.h.** Seluruh tabel Matriks FK (Bab 5.1) harus **ditulis ulang 58 baris lengkap** — tidak boleh ada baris yang dilewati.
  - [ ] **8.3.i.** Seluruh tabel CHECK Constraint (Bab 5.3) harus **ditulis ulang lengkap** — tidak boleh ada constraint yang dilewati.
  - [ ] **8.3.j.** Seluruh Kamus Entitas (Bab 6) harus **ditulis ulang 28 baris lengkap** — tidak boleh ada entitas yang dihilangkan.

- [ ] **8.4.** Jika selama proses validasi ditemukan **dokumen referensi baru** (di luar REF-01 s.d REF-06 yang sudah ada) yang digunakan sebagai acuan perbaikan, maka **wajib menambahkan** baris referensi baru tersebut di bagian akhir Bab 9 (Referensi Dokumen) sebelum menyimpan file.

- [ ] **8.5.** Setelah penulisan selesai, **verifikasi integritas file** dengan melakukan pembacaan ulang:
  ```
  Baca kembali file: docs/sdlc/03_design/02_erd_database.md
  ```
  Pastikan:
  - [ ] Header YAML frontmatter ada dan lengkap di baris paling atas.
  - [ ] Versi dokumen sudah berubah (contoh: `1.1`).
  - [ ] Tabel Riwayat Perubahan sudah memiliki baris baru.
  - [ ] Semua bab (1 s.d 9) ada dan tidak ada yang terpotong.
  - [ ] Tidak ada teks `[TRUNCATED]`, `[...]`, atau `...` yang mengindikasikan konten yang dipotong.
  - [ ] Semua diagram Mermaid dimulai dengan ` ```mermaid` dan diakhiri dengan ` ``` `.

---

### FASE 9 — Validasi Tambahan Spesifik ERD (Kriteria Khusus Dokumen ERD)

> Instruksi tambahan yang relevan secara spesifik untuk dokumen ERD — tidak ditemukan pada checklist umum dokumen SDLC lainnya.

- [ ] **9.1. Validasi Sintaks Mermaid**: Periksa seluruh diagram `erDiagram` untuk memastikan:
  - Tidak ada karakter spesial yang menyebabkan error render Mermaid (seperti tanda `&`, `<`, `>` yang harus di-escape atau diganti).
  - Setiap blok `erDiagram` dibuka dan ditutup dengan benar.
  - Setiap nama tabel (entitas) menggunakan `snake_case` tanpa spasi.
  - Setiap notasi relasi menggunakan sintaks Crow's Foot yang valid: `||--o{`, `||--|{`, `||--||`.
  - Setiap label relasi diapit tanda kutip ganda `"..."`.

- [ ] **9.2. Validasi Konsistensi Notasi Kardinalitas**: Pastikan kardinalitas yang ditampilkan di diagram Mermaid **konsisten** dengan penjelasan di Bab 5 (Matriks Relasi). Contoh: jika di matriks FK no.17 disebutkan `antrian_kerja.transaksi_id` bertipe `One-to-One`, maka di diagram harus menggunakan notasi `||--||`, bukan `||--o{`.

- [ ] **9.3. Validasi Kelengkapan Kolom di Sub-Diagram**: Hitung jumlah kolom yang terdefinisi di setiap entitas dalam **Bab 4 (Sub-Diagram Modular)** dan bandingkan dengan jumlah kolom aktual di SQL. Jumlah harus sama persis untuk setiap tabel.

- [ ] **9.4. Validasi Arah Relasi**: Pastikan **arah relasi** di diagram Mermaid sudah benar — tabel parent (referensi) berada di sebelah kiri, tabel child (yang memiliki FK) di sebelah kanan. Contoh: `cabang ||--o{ pengguna` artinya `cabang` adalah parent, `pengguna` adalah child yang memiliki `cabang_id FK`.

- [ ] **9.5. Validasi Relasi yang Terduplikasi di Diagram Utama**: Pada **Bab 3 (Full ERD)**, tabel `pengguna` memiliki banyak peran (kasir, desainer, teknisi, supervisor, dll.) yang menghasilkan multiple relasi ke tabel yang sama. Pastikan setiap relasi FK yang unik sudah tercakup tanpa duplikasi yang membingungkan, dan labelnya cukup distinktif untuk membedakan peran.

- [ ] **9.6. Validasi Normalisasi**: Periksa apakah ada potensi **anomali data** yang belum terdokumentasi sebagai keputusan desain di Bab 7:
  - Kolom `selisih` di `shift_handover` (derived dari `kas_fisik - kas_sistem`): apakah ini *redundant column* atau *derived value yang disengaja disimpan* untuk audit? Pastikan ada penjelasan di Bab 7.
  - Kolom `subtotal` di `detail_transaksi` (derived dari `kuantitas * harga_jual`): sama seperti di atas.
  - Kolom `kerugian_nominal` di `limbah_produksi` (derived dari `kuantitas_limbah * harga_beli`): sama.
  - Kolom `gaji_bersih` di `payroll` (derived dari formula): sama.
  - Jika belum ada penjelasan → tambahkan sub-seksi baru di Bab 7: **"7.6. Derived Columns & Redundant Storage (Keputusan Anti-Normalisasi)"**.

- [ ] **9.7. Validasi Index Strategy**: Periksa apakah Bab 7 atau Bab 5.3 sudah mendokumentasikan **strategi indexing** composite index yang ada di SQL (selain PK dan FK index yang otomatis) dan menjelaskan **mengapa** index tersebut dipilih (kolom apa yang sering menjadi filter query). Jika belum → tambahkan sub-seksi baru: **"7.7. Strategi Index Komposit"**.

- [ ] **9.8. Validasi Seed Data**: Periksa apakah ERD mencantumkan informasi terkait **seed data awal** yang ada di SQL (data `cabang` pusat, data user `pemilik`, data `system_configs` default, data `saldo_ewallet` 6 akun, dll.) di bagian yang relevan (misalnya Bab 7 atau Bab 2). Ini penting agar backend developer tahu titik awal data. Jika belum → tambahkan catatan ringkas di Bab 7.

---

## 5. Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **selesai** jika seluruh kondisi berikut terpenuhi:

- [ ] Semua checklist di Fase 0 s.d Fase 9 telah diberi tanda `[x]`.
- [ ] File `docs/sdlc/03_design/02_erd_database.md` telah ditimpa (overwrite) dengan dokumen yang telah divalidasi sepenuhnya.
- [ ] Versi dokumen telah dinaikkan (contoh: dari `v1.0` menjadi `v1.1`).
- [ ] Tidak ada satu pun placeholder, data kosong, atau konten yang dipotong (`[...]`) dalam dokumen final.
- [ ] Dokumen dapat dibaca dari awal hingga akhir tanpa menimbulkan pertanyaan yang tidak terjawab oleh dokumen itu sendiri.
- [ ] Seluruh diagram Mermaid `erDiagram` dapat dirender tanpa error sintaks.
- [ ] Jika ada referensi baru yang ditambahkan, sudah tercantum di Bab 9 (Referensi Dokumen).

---

## 6. Catatan Penting untuk Pelaksana

> **Baca ini sebelum memulai eksekusi:**

1. **Jangan** pernah menulis sebagian dokumen lalu menyambung dengan `[...]` atau `[TRUNCATED]`. Seluruh teks harus ditulis penuh.
2. **Jangan** menghapus konten yang valid hanya karena terlalu panjang. ERD Database adalah dokumen yang memang besar — panjang dokumen adalah fitur, bukan bug.
3. **Jangan** membuat asumsi tentang nilai yang tidak tersedia. Selalu rujuk kembali ke file referensi (REF-01 s.d REF-06) untuk mencari data yang akurat.
4. **Jangan** mengubah struktur bab yang sudah ada jika tidak diperlukan. Hanya perbaiki konten yang memang perlu diperbaiki.
5. **Selalu** tandai temuan dengan kode `[KODE_TEMUAN]` sebelum memperbaikinya, agar proses validasi dapat dilacak.
6. Jika tools penulisan file memiliki **batas ukuran output**, bagi penulisan menjadi beberapa blok berurutan (misalnya: Bab 1-4 dulu, lalu append Bab 5-9), **tetapi pastikan tidak ada bab yang terpotong** dan tidak ada overlap konten antar blok.
7. Lakukan validasi secara **linear — satu fase selesai sebelum lanjut ke fase berikutnya**. Jangan melompat-lompat fase.

---

*Issue ini dibuat pada: 2026-05-24 | Dibuat oleh: Senior Database Architect & Data Modeling Specialist*
*Konteks proyek: AbuCom — Sistem Manajemen Terpadu Usaha Percetakan (CLI-based, Python, MySQL 8.x)*
