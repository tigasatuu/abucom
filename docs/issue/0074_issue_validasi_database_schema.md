# Validasi & Penyempurnaan Dokumen Database Schema

---

## Informasi Konteks Issue

| Field                | Detail                                                               |
|----------------------|----------------------------------------------------------------------|
| **Dokumen Utama**    | Database Schema (DDL SQL)                                            |
| **Target File**      | `docs/sdlc/03_design/01_database_schema.sql`                        |
| **Lokasi Referensi** | `docs/sdlc/`                                                         |
| **Versi Saat Ini**   | v1.1                                                                 |
| **Versi Target**     | v1.2                                                                 |
| **Prioritas**        | Tinggi                                                               |
| **Label**            | `validation` `database` `design-phase` `sdlc`                       |
| **Ditugaskan Kepada**| Junior Programmer / LLM Model AI                                     |
| **Dibuat Oleh**      | Senior Database Architect                                            |
| **Tanggal Issue**    | 2026-05-29                                                           |

---

## Latar Belakang

Dokumen `docs/sdlc/03_design/01_database_schema.sql` adalah file DDL SQL yang mendefinisikan seluruh struktur basis data fisik MySQL 8.x untuk sistem **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**. Dokumen ini terdiri dari 28 tabel, index tambahan, data seed awal, verifikasi integritas, dan referensi dokumen.

Dokumen ini berfungsi sebagai **sumber kebenaran tunggal (single source of truth)** untuk seluruh struktur basis data dan akan menjadi **referensi utama** bagi dokumen-dokumen fase SDLC berikutnya, yakni fase implementasi (04_implementation), pengujian (05_testing), dan seterusnya.

Karena posisinya yang sangat kritis, dokumen ini **wajib divalidasi secara menyeluruh dan ketat** sebelum digunakan sebagai acuan oleh fase berikutnya. Issue ini mendokumentasikan seluruh tugas validasi yang harus diselesaikan.

---

## Persona yang Harus Diadopsi

> **PENTING:** Sebelum memulai pekerjaan apapun, adopsi dan pertahankan persona berikut ini sepanjang seluruh proses validasi.

Kamu adalah **Senior Database Architect & DDL Validation Expert** dengan spesialisasi:

- **MySQL 8.x DDL Expert**: Menguasai seluruh sintaks DDL MySQL 8.0/8.4 LTS secara mendalam, mencakup `CREATE TABLE`, `CONSTRAINT`, `INDEX`, `ENGINE`, `CHARSET`, `COLLATE`, tipe data, dan semua opsi lanjutan.
- **Relational Database Normalization Master**: Ahli normalisasi hingga 3NF/BCNF, identifikasi anomali data, integritas referensial, dan desain constraint yang tepat.
- **Business Domain Expert – Usaha Percetakan**: Memahami alur bisnis percetakan kecil-menengah secara mendalam, termasuk manajemen stok bahan baku, BOM produksi, sistem kasir, PPOB, e-wallet, payroll, absensi, kasbon, aset, dan audit trail.
- **Technical Documentation Reviewer**: Ahli standar dokumentasi teknis industri, termasuk standar komentar SQL, metadata dokumen, riwayat perubahan, dan kelengkapan referensi dokumen.
- **SDLC Continuity Validator**: Memahami bagaimana output fase Design (dokumen ini) menjadi input fase Implementation & Testing, sehingga mampu menilai apakah dokumen ini sudah cukup lengkap, tidak ambigu, dan tidak akan membutuhkan klarifikasi berulang.

Dengan persona ini, kamu akan menilai dokumen ini dengan standar **tinggi, kritis, dan tidak toleran terhadap ambiguitas atau ketidaklengkapan**.

---

## File Referensi yang Harus Dibaca

Berikut adalah semua file yang **wajib dibaca terlebih dahulu** sebelum melakukan validasi. Baca **seluruh isi** setiap file, jangan dilewati atau diabaikan.

| Kode Ref | File                                                              | Kontribusi Validasi                                                                 |
|----------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| REF-01   | `docs/sdlc/02_analysis/05_data_dictionary.md`                    | Sumber utama: definisi 28 tabel, 282 kolom, constraint, FK, domain nilai, seed data |
| REF-02   | `docs/sdlc/02_analysis/06_access_control_matrix.md`             | Klasifikasi sensitivitas tabel, matriks CRUD per role                               |
| REF-03   | `docs/sdlc/01_planning/04_tech_stack_decision.md`               | Konfigurasi MySQL (engine, charset, collation), strategi inisialisasi schema.sql    |
| REF-04   | `docs/sdlc/02_analysis/02_software_requirements.md`             | Cross-check kebutuhan fungsional (SRS-F-xxx)                                        |
| REF-05   | `docs/sdlc/02_analysis/01_business_requirements.md`             | Cross-check aturan bisnis dan domain nilai (BR-F-xx)                                |

---

## Daftar Tugas Validasi (Checklist)

Kerjakan semua tugas berikut **secara berurutan dari atas ke bawah**. Jangan melompat atau melewati satu pun langkah. Tandai setiap tugas dengan `[x]` setelah selesai dikerjakan.

---

### FASE 0 — PERSIAPAN & PEMBACAAN FILE

- [ ] **[BACA-0.1]** Buka dan baca seluruh isi file target: `docs/sdlc/03_design/01_database_schema.sql` (dari baris pertama hingga baris terakhir, tanpa pengecualian). Hitung dan catat jumlah total tabel, index, seed data, dan query verifikasi yang ada.
- [ ] **[BACA-0.2]** Buka dan baca seluruh isi file `docs/sdlc/02_analysis/05_data_dictionary.md` (REF-01). Catat: total tabel terdefinisi, total kolom per tabel, semua constraint (PK, FK, UNIQUE, CHECK), semua domain nilai enum, semua seed data yang dipersyaratkan, dan semua aturan bisnis yang relevan dengan skema.
- [ ] **[BACA-0.3]** Buka dan baca seluruh isi file `docs/sdlc/02_analysis/06_access_control_matrix.md` (REF-02). Catat: klasifikasi sensitivitas setiap tabel dan matriks CRUD per role pengguna.
- [ ] **[BACA-0.4]** Buka dan baca seluruh isi file `docs/sdlc/01_planning/04_tech_stack_decision.md` (REF-03). Catat: versi MySQL yang dipilih, konfigurasi engine, charset, collation, dan ketentuan khusus inisialisasi skema.
- [ ] **[BACA-0.5]** Buka dan baca seluruh isi file `docs/sdlc/02_analysis/02_software_requirements.md` (REF-04). Catat: semua kode kebutuhan fungsional (SRS-F-xxx) yang berhubungan dengan data, penyimpanan, dan struktur tabel.
- [ ] **[BACA-0.6]** Buka dan baca seluruh isi file `docs/sdlc/02_analysis/01_business_requirements.md` (REF-05). Catat: semua aturan bisnis (BR-F-xx) yang berimplikasi pada struktur tabel, constraint, atau domain nilai.

---

### FASE 1 — VALIDASI KELENGKAPAN: CAKUPAN REFERENSI

> **Tujuan:** Memastikan dokumen utama merangkum **semua** data dan informasi yang ada di file referensi. Tidak boleh ada data dari referensi yang terlewat.

- [ ] **[VAL-1.1]** Bandingkan daftar tabel di `01_database_schema.sql` dengan daftar tabel di REF-01 (`05_data_dictionary.md`). Verifikasi bahwa **semua 28 tabel** yang didefinisikan di data dictionary sudah ada di dalam schema SQL. Catat tabel mana saja jika ada yang hilang.
- [ ] **[VAL-1.2]** Untuk **setiap tabel**, bandingkan daftar kolom di `01_database_schema.sql` dengan daftar kolom di REF-01. Verifikasi bahwa **setiap kolom** dari data dictionary sudah ada di schema SQL dengan nama yang identik. Catat kolom mana saja yang hilang per tabel.
- [ ] **[VAL-1.3]** Untuk **setiap kolom**, bandingkan tipe data di `01_database_schema.sql` dengan tipe data di REF-01. Verifikasi bahwa tidak ada perbedaan tipe data (misalnya: `INT` vs `BIGINT`, `VARCHAR(50)` vs `VARCHAR(100)`, `DECIMAL(15,4)` vs `DECIMAL(10,2)`). Catat semua perbedaan yang ditemukan.
- [ ] **[VAL-1.4]** Untuk **setiap kolom**, bandingkan nilai `DEFAULT` di `01_database_schema.sql` dengan yang didefinisikan di REF-01. Verifikasi tidak ada ketidaksesuaian nilai default. Catat semua perbedaan.
- [ ] **[VAL-1.5]** Untuk **setiap kolom**, bandingkan atribut `NOT NULL` / `NULL` di `01_database_schema.sql` dengan REF-01. Verifikasi bahwa kolom yang seharusnya nullable sudah `NULL` dan sebaliknya. Catat semua perbedaan.
- [ ] **[VAL-1.6]** Untuk **setiap kolom yang memiliki domain nilai terbatas (enum)**, bandingkan daftar nilai valid yang tertulis di COMMENT kolom `01_database_schema.sql` dengan domain nilai yang didefinisikan di REF-01. Verifikasi tidak ada nilai yang hilang atau salah. Catat semua perbedaan.
- [ ] **[VAL-1.7]** Bandingkan seluruh daftar **PRIMARY KEY, UNIQUE KEY, FOREIGN KEY, dan CHECK CONSTRAINT** di `01_database_schema.sql` dengan yang didefinisikan di REF-01. Verifikasi bahwa semua constraint sudah ada, dengan kolom yang benar, dan action referensial yang tepat (`ON DELETE`, `ON UPDATE`). Catat semua yang hilang atau berbeda.
- [ ] **[VAL-1.8]** Bandingkan **data seed awal** di `01_database_schema.sql` (BAGIAN 4) dengan data seed yang dipersyaratkan di REF-01. Verifikasi bahwa semua seed record yang diharuskan sudah ada dengan nilai yang benar. Catat seed yang hilang atau berbeda nilainya.
- [ ] **[VAL-1.9]** Bandingkan konfigurasi **INDEX** di `01_database_schema.sql` (BAGIAN 3) dengan kebutuhan index yang mungkin disebutkan di REF-01, REF-04, atau REF-03. Verifikasi bahwa tidak ada index penting yang terlewat berdasarkan pola query yang dibutuhkan sistem.
- [ ] **[VAL-1.10]** Periksa atribut `COMMENT` pada **setiap tabel** di `01_database_schema.sql`. Bandingkan dengan klasifikasi sensitivitas di REF-02. Verifikasi bahwa nilai `Sensitivitas` dan `Modul` di setiap COMMENT tabel sudah sesuai dan akurat. Catat semua yang tidak sesuai.
- [ ] **[VAL-1.11]** Periksa **13 parameter** di seed `system_configs`. Verifikasi setiap parameter (`parameter_key`, `parameter_value`, `tipe_data`, `deskripsi`) sudah lengkap dan sesuai dengan aturan bisnis yang ada di REF-05 dan REF-04. Catat parameter yang nilai atau deskripsinya tidak sesuai.

---

### FASE 2 — VALIDASI RELEVANSI: TIDAK ADA DATA BERLEBIHAN

> **Tujuan:** Memastikan dokumen utama hanya memuat data yang **sesuai dan dibutuhkan** oleh dokumen Database Schema. Dokumen ini harus bersih dari informasi yang tidak relevan dengan konteksnya.

- [ ] **[VAL-2.1]** Periksa apakah ada tabel, kolom, constraint, atau index di `01_database_schema.sql` yang **tidak pernah disebutkan atau tidak diperlukan** oleh satu pun file referensi. Jika ada, tandai sebagai kandidat untuk dihapus atau dipertanyakan, dan catat alasannya.
- [ ] **[VAL-2.2]** Periksa apakah COMMENT pada tabel atau kolom mengandung informasi yang **lebih cocok berada di dokumen lain** (misalnya: penjelasan alur bisnis panjang yang seharusnya ada di data dictionary, bukan di COMMENT DDL). Jika COMMENT terlalu verbose dan tidak standar, tandai untuk dipersingkat agar tetap informasional tapi ringkas.
- [ ] **[VAL-2.3]** Periksa apakah BAGIAN 5 (Verifikasi Integritas) hanya memuat **query verifikasi yang relevan** dengan isi schema yang ada. Verifikasi bahwa angka yang diharapkan di setiap query (`total_cabang`, `total_pengguna`, dst.) sesuai dengan jumlah record yang dimasukkan di BAGIAN 4.
- [ ] **[VAL-2.4]** Periksa apakah ada duplikasi definisi: kolom yang didefinisikan dua kali, constraint yang terdefinisi ganda, atau index yang sudah tercakup oleh PRIMARY KEY/UNIQUE KEY sehingga redundan. Catat jika ditemukan.

---

### FASE 3 — VALIDASI STRUKTUR DOKUMEN

> **Tujuan:** Memastikan dokumen ini memiliki struktur yang **standar, lengkap, dan informatif** sesuai praktik industri dokumentasi DDL SQL.

- [ ] **[VAL-3.1]** Verifikasi **HEADER & METADATA DOKUMEN** (BAGIAN 0 / Header di awal file). Periksa kelengkapan field berikut dan pastikan semua terisi dengan benar:
  - `Nama Dokumen` — harus ada dan deskriptif
  - `Nama Proyek` — harus ada dan konsisten dengan nama proyek di file referensi lain
  - `Versi Dokumen` — harus ada (akan diperbarui menjadi v1.2 di akhir)
  - `Tanggal Pembuatan` — harus ada
  - `Penyusun` — harus ada
  - `Status Dokumen` — harus ada
  - `Deskripsi` — harus ada dan menjelaskan isi file secara akurat
  - `Prasyarat` — harus ada dan menyebutkan versi MySQL yang tepat sesuai REF-03
  - `Pembatasan Akses` — harus ada
  - `Instruksi Eksekusi` — harus ada dengan sintaks perintah yang benar
  - `Riwayat Perubahan` — harus ada dengan format tabel yang terstruktur

- [ ] **[VAL-3.2]** Verifikasi bahwa **urutan bagian dokumen** sudah logis dan standar untuk file DDL SQL industri:
  - Bagian 1: Konfigurasi Awal & Pembuatan Database
  - Bagian 2: Pembuatan Tabel (CREATE TABLE) — dikelompokkan secara logis berdasarkan dependency
  - Bagian 3: Pembuatan Index Tambahan (CREATE INDEX)
  - Bagian 4: Data Seed Awal (INSERT INTO)
  - Bagian 5: Verifikasi Integritas (SHOW TABLES / SELECT COUNT)
  - Bagian 6: Restorasi Konfigurasi & Footer
  - Bagian Referensi Dokumen

- [ ] **[VAL-3.3]** Verifikasi bahwa **pengelompokan tabel** di BAGIAN 2 sudah logis dan konsisten:
  - Kelompok A: Tabel Induk (tanpa FK)
  - Kelompok B: Tabel Master Level 2 (FK ke Cabang)
  - Kelompok C: Tabel Transaksional (FK ke Master)
  - Kelompok D: Tabel Administrasi & Keuangan
  - Kelompok E: Tabel Audit & Rekonsiliasi
  - Verifikasi bahwa setiap tabel masuk ke kelompok yang paling tepat berdasarkan dependency FK-nya.

- [ ] **[VAL-3.4]** Verifikasi bahwa **urutan pembuatan tabel** sudah memenuhi prinsip dependency: tabel yang direferensikan oleh FK harus didefinisikan **lebih dahulu** daripada tabel yang mereferensikannya. Lakukan pemetaan dependency FK untuk memastikan tidak ada circular dependency atau urutan yang salah.

- [ ] **[VAL-3.5]** Verifikasi bahwa setiap blok `CREATE TABLE` memiliki **separator komentar yang konsisten** dengan format:
  ```
  -- ------------------------------------------------------------
  -- [TABEL XX] nama_tabel
  -- ------------------------------------------------------------
  ```
  Dan bahwa nomor urut tabel `[TABEL XX]` sudah berurutan dan tidak ada yang terlewat atau terduplikasi.

- [ ] **[VAL-3.6]** Verifikasi bahwa BAGIAN 6 (Restorasi Konfigurasi) selalu ada dan me-restore **tepat tiga variabel session** yang di-set di BAGIAN 1: `SQL_MODE`, `FOREIGN_KEY_CHECKS`, dan `UNIQUE_CHECKS`.

- [ ] **[VAL-3.7]** Verifikasi bahwa BAGIAN REFERENSI DOKUMEN mencantumkan **semua file referensi** yang benar-benar dikonsultasikan dalam penyusunan dokumen ini. Format setiap referensi harus konsisten dengan:
  ```
  -- [REF-XX] Nama Dokumen vX.X
  --          Path: docs/sdlc/...
  --          Kontribusi: [deskripsi kontribusi spesifik]
  ```

---

### FASE 4 — VALIDASI KUALITAS DDL SQL

> **Tujuan:** Memastikan kualitas DDL SQL sudah sesuai standar MySQL 8.x dan siap dieksekusi tanpa error.

- [ ] **[VAL-4.1]** Periksa **setiap definisi kolom** untuk memastikan:
  - Tipe data sudah tepat dan optimal untuk kebutuhan bisnis yang didefinisikan (tidak terlalu besar, tidak terlalu kecil)
  - Kolom bertipe `DECIMAL` menggunakan presisi `(15,4)` secara konsisten untuk semua nilai keuangan/moneter
  - Kolom bertipe `VARCHAR` memiliki panjang yang masuk akal dan konsisten dengan domain datanya
  - Kolom bertipe `TIMESTAMP` atau `DATE` dipilih dengan tepat (DATE untuk tanggal saja, TIMESTAMP untuk waktu presisi)
  - Tidak ada tipe data yang deprecated di MySQL 8.x yang digunakan (misalnya: `ENUM` inline disarankan diganti pendekatan COMMENT + CHECK)

- [ ] **[VAL-4.2]** Periksa **setiap CONSTRAINT CHECK** untuk memastikan:
  - Logika constraint sudah benar secara matematis (misalnya: `sisa_utang >= 0 AND sisa_utang <= nominal_pinjaman`)
  - Nama constraint mengikuti konvensi penamaan: `chk_{nama_tabel}_{nama_kolom}`
  - Tidak ada kolom yang logikanya butuh CHECK constraint tapi belum memilikinya (misalnya: kolom harga, kuantitas, nominal)

- [ ] **[VAL-4.3]** Periksa **setiap FOREIGN KEY** untuk memastikan:
  - Tipe data kolom FK identik dengan tipe data kolom PK yang direferensikan (keduanya `INT NOT NULL`)
  - Nama constraint FK mengikuti konvensi: `fk_{nama_tabel}_{nama_kolom_fk}`
  - Action referensial (`ON DELETE`, `ON UPDATE`) sudah tepat sesuai logika bisnis:
    - `CASCADE`: digunakan saat child harus ikut terhapus/terupdate (misalnya: detail_transaksi → transaksi)
    - `RESTRICT`: digunakan saat parent tidak boleh dihapus selama masih direferensikan
    - `SET NULL`: digunakan saat FK boleh menjadi NULL jika parent dihapus (kolom harus `NULL`able)

- [ ] **[VAL-4.4]** Periksa **setiap UNIQUE KEY / UNIQUE CONSTRAINT** untuk memastikan:
  - Nama constraint mengikuti konvensi: `uq_{nama_tabel}_{nama_kolom1}_{kolom2...}` atau menggunakan `UNIQUE` langsung di definisi kolom untuk single-column unique
  - Tidak ada kolom atau kombinasi kolom yang harusnya unique secara bisnis tapi belum diberi UNIQUE constraint

- [ ] **[VAL-4.5]** Periksa **BAGIAN 3 (Index Tambahan)** untuk memastikan:
  - Nama index mengikuti konvensi: `idx_{nama_tabel}_{kolom1}_{kolom2}`
  - Setiap index yang ada memiliki justifikasi query yang jelas (kolom yang sering digunakan di klausa `WHERE`, `ORDER BY`, atau `GROUP BY` berdasarkan alur bisnis sistem)
  - Index komposit sudah diurutkan dari kolom dengan selektivitas tertinggi ke terendah (kolom yang paling sering dijadikan filter pertama)
  - Periksa apakah ada pola query kritis lain yang membutuhkan index tambahan berdasarkan alur transaksi di REF-04 dan REF-05

- [ ] **[VAL-4.6]** Periksa **konfigurasi BAGIAN 1** untuk memastikan:
  - `SET NAMES utf8mb4` sudah ada
  - `ENGINE=InnoDB` digunakan secara konsisten di semua tabel (sesuai REF-03)
  - `DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci` digunakan secara konsisten di semua tabel
  - Perintah `DROP DATABASE IF EXISTS` diikuti peringatan komentar yang memadai sebelumnya
  - `CREATE DATABASE` menggunakan charset dan collation yang sama

- [ ] **[VAL-4.7]** Periksa **COMMENT tabel** untuk memastikan format standar terpenuhi: `'[Deskripsi fungsi tabel] | Sensitivitas: [Nilai] | Modul: [Kode]'`. Nilai sensitivitas harus salah satu dari: `Operasional`, `Sensitif`, atau `Sangat Sensitif` (sesuai REF-02). Kode modul harus konsisten dengan modul yang didefinisikan di REF-04.

- [ ] **[VAL-4.8]** Periksa **COMMENT kolom** untuk memastikan:
  - Setiap kolom memiliki COMMENT yang non-kosong dan informatif
  - COMMENT kolom yang memiliki domain nilai terbatas menyertakan daftar nilai valid: `Nilai valid: 'X' | 'Y' | 'Z'`
  - COMMENT tidak mengandung karakter spesial yang bisa menyebabkan error parsing SQL

---

### FASE 5 — VALIDASI KELAYAKAN SEBAGAI REFERENSI SDLC

> **Tujuan:** Memastikan dokumen ini sudah **cukup lengkap, tidak ambigu, dan tidak akan selalu dipertanyakan** oleh fase SDLC berikutnya (Implementation & Testing).

- [ ] **[VAL-5.1]** Bayangkan kamu adalah developer yang akan mengimplementasikan sistem AbuCom menggunakan dokumen ini sebagai satu-satunya acuan database. Periksa apakah ada **informasi yang hilang** yang akan membuatmu harus bertanya atau menebak-nebak, misalnya:
  - Apakah instruksi eksekusi sudah lengkap untuk berbagai lingkungan (development, production)?
  - Apakah peringatan tentang `DROP DATABASE` sudah cukup jelas?
  - Apakah urutan eksekusi sudah eksplisit?

- [ ] **[VAL-5.2]** Bayangkan kamu adalah QA Engineer yang akan membuat test case database. Periksa apakah ada **constraint atau aturan bisnis** yang **implisit** (hanya diketahui dari konteks bisnis) tapi **belum dituangkan** ke dalam CONSTRAINT SQL. Misalnya: apakah ada aturan bisnis di REF-05 yang belum diimplementasikan sebagai CHECK constraint? Catat semua yang ditemukan.

- [ ] **[VAL-5.3]** Periksa apakah ada **ambiguitas logika bisnis** yang terindikasi dari definisi kolom. Contoh: kolom `dp_bayar` di tabel `transaksi` memiliki CHECK `dp_bayar <= total_bayar` — apakah ini sudah mencakup semua skenario (misalnya: bagaimana jika DP = 0 untuk transaksi LUNAS)?. Catat semua potensi ambiguitas.

- [ ] **[VAL-5.4]** Periksa apakah BAGIAN 5 (Verifikasi Integritas) sudah **cukup representatif** sebagai checklist pasca-instalasi. Pertimbangkan apakah perlu ditambahkan query verifikasi untuk: memastikan FK berfungsi, memastikan index terbentuk, atau memastikan nilai seed kritis sudah benar.

- [ ] **[VAL-5.5]** Periksa apakah dokumentasi teknis yang ada sudah memadai untuk **developer Python** yang akan mengakses database ini (sesuai REF-03 bahwa sistem dibangun dengan Python CLI). Misalnya: apakah tipe data sudah dipetakan dengan jelas sehingga developer tahu cara casting di Python?

---

### FASE 6 — VALIDASI BAHASA & KETERBACAAN

> **Tujuan:** Memastikan bahasa Indonesia yang digunakan **natural, tidak ambigu, dan mudah dipahami** oleh junior programmer atau LLM model AI.

- [ ] **[VAL-6.1]** Baca ulang **seluruh COMMENT tabel** dan pastikan:
  - Menggunakan Bahasa Indonesia yang baku dan natural (bukan hasil terjemahan kaku dari Bahasa Inggris)
  - Tidak mengandung kata-kata teknis asing yang tidak dijelaskan
  - Tidak ambigu: setiap COMMENT hanya memiliki satu interpretasi yang mungkin
  - Setiap COMMENT menjawab pertanyaan "Apa fungsi tabel ini?" secara langsung

- [ ] **[VAL-6.2]** Baca ulang **seluruh COMMENT kolom** dan pastikan:
  - Menggunakan Bahasa Indonesia yang baku dan natural
  - Deskripsi COMMENT menjelaskan **makna bisnis** kolom tersebut, bukan hanya mendeskripsikan nama kolomnya (hindari COMMENT yang hanya mengulang nama kolom)
  - Tidak ada COMMENT yang bisa disalahartikan atau menimbulkan kebingungan
  - Panjang COMMENT proporsional: tidak terlalu singkat (satu kata) dan tidak terlalu panjang (lebih dari 2 kalimat)

- [ ] **[VAL-6.3]** Periksa semua **komentar blok** (separator bagian, peringatan, catatan) untuk memastikan:
  - Menggunakan Bahasa Indonesia yang natural dan profesional
  - Pesan peringatan (misalnya peringatan DROP DATABASE) sudah cukup tegas dan jelas
  - Tidak ada komentar yang membingungkan atau kontradiktif

- [ ] **[VAL-6.4]** Periksa semua **nama constraint** dan **nama index** untuk memastikan mengikuti konvensi penamaan yang konsisten (snake_case, deskriptif, menggunakan prefix yang tepat: `chk_`, `fk_`, `uq_`, `idx_`).

---

### FASE 7 — VALIDASI DATA KOSONG & PENGISIAN OTOMATIS

> **Tujuan:** Mengidentifikasi dan mengisi semua data yang kosong, placeholder, atau perlu dilengkapi dengan data yang sesuai dan relevan.

- [ ] **[VAL-7.1]** Periksa **COMMENT kolom** yang kosong atau hanya berisi placeholder seperti `''`, `-`, `TODO`, `TBD`, `N/A`, atau deskripsi yang sangat singkat dan tidak informatif. Isi dengan COMMENT yang tepat dan deskriptif sesuai konteks bisnis dokumen ini.

- [ ] **[VAL-7.2]** Periksa apakah ada **nilai DEFAULT** yang masih berupa placeholder (misalnya: `DEFAULT 'PLACEHOLDER'` atau `DEFAULT ''` pada kolom yang seharusnya memiliki nilai default yang bermakna). Isi dengan nilai default yang sesuai.

- [ ] **[VAL-7.3]** Periksa **data seed** di BAGIAN 4. Pastikan nilai seed yang ada sudah realistis dan sesuai konteks bisnis percetakan (misalnya: nilai saldo, alamat, parameter bisnis). Jika ada nilai yang tidak realistis atau terlalu generik (misalnya: `password_hash` yang sudah ada adalah hash fiktif — verifikasi ini adalah placeholder yang benar untuk seed data), pastikan sudah diberi komentar penjelasan yang cukup.

- [ ] **[VAL-7.4]** Periksa apakah ada kolom dengan tipe `TEXT` atau `VARCHAR` yang COMMENT-nya menyebutkan "diisi manual" atau "perlu konfigurasi" tanpa penjelasan lebih lanjut tentang format atau aturan pengisiannya. Tambahkan penjelasan format yang diperlukan di COMMENT.

- [ ] **[VAL-7.5]** Periksa semua **kolom tanggal/waktu** yang memiliki nilai `NULL DEFAULT NULL`. Verifikasi bahwa kolom-kolom ini memang seharusnya nullable secara bisnis (misalnya: `tanggal_selesai` yang baru terisi setelah proses selesai). Jika ada yang seharusnya memiliki nilai default, koreksi.

---

### FASE 8 — FINALISASI & PENULISAN ULANG

> **Tujuan:** Menuangkan seluruh hasil validasi ke file target dengan cara overwrite penuh.

- [ ] **[FIN-8.1]** Buat **ringkasan temuan** dari semua fase validasi (1 hingga 7) sebelum menulis ulang. Catat:
  - Total temuan per kategori (kelengkapan, relevansi, struktur, kualitas DDL, kelayakan SDLC, bahasa, data kosong)
  - Jumlah perubahan yang akan dilakukan
  - Daftar kolom/tabel/constraint yang dimodifikasi, ditambah, atau dihapus

- [ ] **[FIN-8.2]** Berdasarkan semua temuan dari Fase 1–7, susun versi dokumen yang sudah divalidasi dan diperbaiki secara lengkap di memori (atau scratch pad). Pastikan:
  - Seluruh koreksi dari semua fase validasi sudah diterapkan
  - Dokumen tetap berformat SQL yang valid dan bisa dieksekusi langsung di MySQL 8.x
  - Tidak ada informasi yang dipotong, diringkas, atau dihilangkan dari versi sebelumnya kecuali memang harus dihapus berdasarkan temuan validasi

- [ ] **[FIN-8.3]** Update **nomor versi** dokumen:
  - Ubah `Versi Dokumen: 1.1` menjadi `Versi Dokumen: 1.2`
  - Tambahkan baris baru di tabel **RIWAYAT PERUBAHAN DOKUMEN** dengan format:
    ```
    -- 1.2   | 2026-05-29 | Validasi menyeluruh: [ringkasan singkat perubahan] | [Nama Persona]
    ```

- [ ] **[FIN-8.4]** Lakukan penulisan ulang (overwrite) ke file target **`docs/sdlc/03_design/01_database_schema.sql`** menggunakan tool yang tersedia. Instruksi kritis penulisan:
  - **WAJIB**: Tulis ulang **seluruh konten file dari baris pertama hingga baris terakhir** dalam satu operasi tulis
  - **DILARANG**: Memotong, meringkas, atau menghilangkan bagian manapun dari dokumen
  - **DILARANG**: Hanya menulis sebagian file (misalnya hanya bagian yang berubah saja)
  - **WAJIB**: Pastikan file yang ditulis adalah **SQL yang valid** dan bisa dieksekusi tanpa error
  - **WAJIB**: Pastikan semua perubahan dari hasil validasi sudah masuk ke file yang ditulis

- [ ] **[FIN-8.5]** Setelah penulisan selesai, lakukan **verifikasi akhir** dengan membaca kembali file yang baru ditulis untuk memastikan:
  - File tidak terpotong di tengah (cek baris terakhir: harus ada BAGIAN REFERENSI DOKUMEN yang lengkap)
  - Versi dokumen sudah berubah menjadi `1.2`
  - Riwayat perubahan sudah diperbarui
  - Tidak ada karakter aneh atau encoding yang rusak

- [ ] **[FIN-8.6]** Jika selama proses validasi ditemukan **file referensi tambahan** yang dikonsultasikan (selain REF-01 sampai REF-05 yang sudah ada), tambahkan file tersebut di **bagian akhir BAGIAN REFERENSI DOKUMEN** dengan format yang konsisten:
  ```
  -- [REF-06] Nama Dokumen vX.X
  --          Path: docs/sdlc/...
  --          Kontribusi: [deskripsi kontribusi spesifik]
  ```

---

## Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **SELESAI** hanya jika **seluruh** kondisi berikut terpenuhi:

- [ ] Semua checklist di Fase 0 hingga Fase 8 sudah ditandai `[x]`
- [ ] File `docs/sdlc/03_design/01_database_schema.sql` sudah berhasil di-overwrite dengan versi terbaru
- [ ] Versi dokumen sudah berubah dari `v1.1` menjadi `v1.2`
- [ ] Riwayat perubahan di header dokumen sudah diperbarui
- [ ] File SQL hasil akhir valid secara sintaks dan bisa dieksekusi di MySQL 8.x tanpa error
- [ ] Tidak ada bagian dokumen yang terpotong atau hilang dibanding versi sebelumnya (kecuali yang memang sengaja dihapus berdasarkan temuan validasi yang terdokumentasi)
- [ ] Semua referensi dokumen yang digunakan tercantum di bagian REFERENSI DOKUMEN

---

## Catatan Penting untuk Implementor

> [!IMPORTANT]
> **Baca seluruh issue ini terlebih dahulu sebelum mulai bekerja.** Jangan langsung lompat ke pekerjaan tanpa memahami konteks, persona, dan semua instruksi.

> [!WARNING]
> **Jangan pernah menulis sebagian file saja.** Penulisan ke file target harus selalu mencakup **seluruh konten dari baris pertama hingga baris terakhir** dalam satu operasi. Penulisan sebagian akan merusak file.

> [!CAUTION]
> **Jangan melakukan perubahan spekulatif.** Setiap perubahan yang kamu buat harus berdasarkan bukti yang bisa dilacak ke salah satu dari 5 file referensi yang disebutkan. Jika kamu tidak menemukan justifikasi di file referensi, **jangan buat perubahan tersebut** — dokumentasikan saja sebagai catatan/pertanyaan.

> [!NOTE]
> File `docs/sdlc/03_design/` juga berisi dokumen desain lain (ERD, System Architecture, CLI Interaction Flow, BOM HHP Design, Security Design) yang **tidak boleh dimodifikasi** dalam issue ini. Fokus hanya pada `01_database_schema.sql`.

---

## Referensi Terkait

- [01_database_schema.sql](sdlc/03_design/01_database_schema.sql) — File target dokumen utama
- [05_data_dictionary.md](sdlc/02_analysis/05_data_dictionary.md) — REF-01: Sumber definisi tabel & kolom
- [06_access_control_matrix.md](sdlc/02_analysis/06_access_control_matrix.md) — REF-02: Klasifikasi sensitivitas
- [04_tech_stack_decision.md](sdlc/01_planning/04_tech_stack_decision.md) — REF-03: Konfigurasi MySQL
- [02_software_requirements.md](sdlc/02_analysis/02_software_requirements.md) — REF-04: Kebutuhan fungsional
- [01_business_requirements.md](sdlc/02_analysis/01_business_requirements.md) — REF-05: Aturan bisnis
