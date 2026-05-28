---
judul     : Validasi, Analisis & Perbaikan Menyeluruh — ERD Database AbuCom
dokumen   : ERD Database
target    : docs/sdlc/03_design/02_erd_database.md
referensi : docs/sdlc/
dibuat    : 2026-05-29
status    : Open
prioritas : High
assignee  : Junior Programmer / AI LLM Model
---

# Validasi, Analisis & Perbaikan Menyeluruh: ERD Database AbuCom

## Latar Belakang

Dokumen **ERD Database** (`docs/sdlc/03_design/02_erd_database.md`) merupakan deliverable visual formal kedua pada Fase 03 Design SDLC AbuCom. Dokumen ini bertanggung jawab untuk merepresentasikan seluruh arsitektur relasional 28 tabel, 58 foreign key, dan 5 kelompok fungsional basis data MySQL 8.x dalam bentuk visual standar Mermaid erDiagram (Crow's Foot notation).

Sebagai dokumen yang akan menjadi **acuan visual utama bagi Backend Developer, AI Coding Assistant, dan DBA** dalam mengimplementasikan API, query JOIN, dan decorator RBAC, dokumen ini harus melewati proses validasi ketat sebelum digunakan sebagai input pada fase SDLC berikutnya (Fase 04 — Implementation).

Issue ini menginstruksikan pelaksana untuk melakukan **audit, komparasi, validasi, dan penulisan ulang (overwrite)** dokumen secara menyeluruh.

---

## Persona Validator

> **PENTING**: Sebelum memulai implementasi, kamu harus membaca dan menginternalisasi persona berikut. Seluruh penilaian, analisis, dan keputusan revisi harus dijalankan dari sudut pandang persona ini tanpa pengecualian.

Kamu adalah seorang **Senior Database Architect & Data Modeling Specialist** dengan spesialisasi dalam:

- **ERD & Relational Data Modeling**: Lebih dari 10 tahun pengalaman merancang skema relasional MySQL/PostgreSQL skala enterprise, termasuk multi-tenant architecture dan multi-branch readiness.
- **SDLC Documentation Standards**: Ahli dalam standar dokumentasi teknis industri (IEEE 830, ISO/IEC 25010), memastikan setiap deliverable memenuhi kriteria *completeness*, *consistency*, *correctness*, dan *unambiguity*.
- **SQL Physical Schema Validation**: Mampu membaca DDL SQL secara verbatim dan memvalidasi keselarasan antara definisi fisik database dengan representasi visualnya (ERD).
- **Data Integrity & Constraint Auditing**: Pakar dalam mengaudit implementasi FK, CHECK constraint, UNIQUE constraint, index komposit, dan aturan ON DELETE/ON UPDATE.
- **Technical Communication**: Mampu menilai kualitas bahasa teknis Indonesia untuk memastikan tidak ada ambiguitas yang dapat menyebabkan junior developer salah interpretasi.

Kamu dikenal dengan standar review yang **tidak toleran terhadap inkonsistensi**, **tidak menerima data placeholder**, dan **tidak mengizinkan informasi yang membingungkan** lolos ke fase implementasi.

---

## Tujuan Issue

1. Memastikan dokumen ERD mencerminkan **100% keakuratan** terhadap seluruh file referensi teknis.
2. Memastikan dokumen hanya memuat informasi yang **relevan dan spesifik** untuk sebuah dokumen ERD.
3. Memastikan dokumen memiliki **struktur standar industri** yang lengkap dan informatif.
4. Memastikan dokumen **layak dijadikan input** untuk Fase 04 Implementation.
5. Memastikan dokumen ditulis dalam **bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami** oleh junior programmer atau AI model yang lebih kecil.
6. Memastikan **tidak ada data kosong, placeholder, atau informasi yang perlu diisi manual** tersisa dalam dokumen.
7. Menuangkan hasil perbaikan ke file target dengan **overwrite penuh** tanpa pemotongan.

---

## Daftar File yang Harus Dibaca

Sebelum melakukan analisis apa pun, baca semua file berikut secara lengkap dari baris pertama hingga terakhir. Jangan lewatkan satu baris pun.

### File Target (Dokumen Utama — Objek yang Divalidasi)

- [ ] **Baca**: `docs/sdlc/03_design/02_erd_database.md` — ini adalah dokumen yang akan divalidasi dan di-overwrite.

### File Referensi (Sumber Kebenaran)

- [ ] **Baca**: `docs/sdlc/03_design/01_database_schema.sql` (REF-01 — Sumber Kebenaran Tunggal fisik MySQL final: 28 tabel, 307 kolom, semua FK/CHECK/UQ/index)
- [ ] **Baca**: `docs/sdlc/02_analysis/05_data_dictionary.md` (REF-02 — Kamus 307 atribut, domain status, traceability SRS-F-xxx)
- [ ] **Baca**: `docs/sdlc/02_analysis/06_access_control_matrix.md` (REF-03 — Anotasi sensitivitas data per tabel dan otorisasi RBAC)
- [ ] **Baca**: `docs/sdlc/02_analysis/02_software_requirements.md` (REF-04 — SRS-F-001 s.d SRS-F-040: validasi kebutuhan fungsional)
- [ ] **Baca**: `docs/sdlc/02_analysis/01_business_requirements.md` (REF-05 — BR-F-01 s.d BR-F-40: batasan bisnis payroll, HPP, depresiasi, kasbon)
- [ ] **Baca**: `docs/sdlc/01_planning/04_tech_stack_decision.md` (REF-06 — Konfigurasi teknis MySQL: InnoDB, utf8mb4, utf8mb4_unicode_ci)

---

## Tahapan Implementasi (Step-by-Step)

Ikuti setiap tahap secara **berurutan**. Jangan melanjutkan ke tahap berikutnya sebelum tahap sebelumnya selesai sepenuhnya. Tandai setiap checklist [ ] menjadi [x] saat selesai dikerjakan.

---

### TAHAP 1 — Pembacaan & Pemahaman Seluruh File

- [ ] **1.1** Buka dan baca file `docs/sdlc/03_design/02_erd_database.md` dari baris 1 hingga baris terakhir. Catat secara mental: jumlah tabel, jumlah FK, jumlah constraint, versi dokumen, dan semua klaim statistik yang ada di dalam dokumen ini.
- [ ] **1.2** Buka dan baca file `docs/sdlc/03_design/01_database_schema.sql` dari awal hingga akhir. Hitung dan catat: total tabel (CREATE TABLE), total kolom per tabel, total FK (FOREIGN KEY), total UNIQUE constraint, total CHECK constraint, total index komposit, dan isi seed data (INSERT INTO).
- [ ] **1.3** Buka dan baca file `docs/sdlc/02_analysis/05_data_dictionary.md` dari awal hingga akhir. Catat: definisi domain status setiap kolom ENUM/VARCHAR, deskripsi atribut per tabel, dan mapping SRS-F-xxx ke setiap tabel.
- [ ] **1.4** Buka dan baca file `docs/sdlc/02_analysis/06_access_control_matrix.md` dari awal hingga akhir. Catat: tingkat sensitivitas data per tabel (Operasional / Sensitif / Sangat Sensitif) dan peta otorisasi RBAC per operasi CRUD.
- [ ] **1.5** Buka dan baca file `docs/sdlc/02_analysis/02_software_requirements.md` dari awal hingga akhir. Catat: setiap SRS-F-xxx yang relevan dengan tabel-tabel di ERD.
- [ ] **1.6** Buka dan baca file `docs/sdlc/02_analysis/01_business_requirements.md` dari awal hingga akhir. Catat: batasan-batasan bisnis yang mempengaruhi CHECK constraint (nominal, limit, threshold).
- [ ] **1.7** Buka dan baca file `docs/sdlc/01_planning/04_tech_stack_decision.md` dari awal hingga akhir. Catat: versi MySQL, storage engine, charset, dan collation yang diputuskan secara resmi.

---

### TAHAP 2 — Validasi Kelengkapan Isi (Komparasi Mendalam dengan Referensi)

> **Tujuan**: Memastikan tidak ada informasi penting dari file referensi yang terlewat untuk dimasukkan ke dalam dokumen ERD.

#### 2.1 Validasi Statistik Model Data (Bab 2.1)

- [ ] **2.1.1** Hitung ulang total tabel dari `01_database_schema.sql`. Bandingkan dengan klaim "Total Tabel: 28" di Bab 2.1. Jika berbeda, catat selisihnya.
- [ ] **2.1.2** Hitung ulang total kolom dari `01_database_schema.sql` dengan menjumlahkan kolom per tabel. Bandingkan dengan klaim "Total Kolom/Atribut: 307" di Bab 2.1. Jika berbeda, catat tabel mana yang jumlah kolomnya tidak sinkron.
- [ ] **2.1.3** Hitung ulang total FK dari `01_database_schema.sql` (cari semua klausa `FOREIGN KEY`). Bandingkan dengan klaim "Total Relasi Foreign Key: 58" di Bab 2.1. Jika berbeda, identifikasi FK mana yang hilang atau berlebihan.
- [ ] **2.1.4** Hitung ulang total UNIQUE constraint dari `01_database_schema.sql` (cari semua klausa `UNIQUE KEY` dan `UNIQUE`). Bandingkan dengan klaim "Total Unique Constraint: 9" di Bab 2.1.
- [ ] **2.1.5** Hitung ulang total CHECK constraint dari `01_database_schema.sql` (cari semua klausa `CONSTRAINT chk_`). Bandingkan dengan klaim "Total CHECK Constraint: 42" di Bab 2.1.
- [ ] **2.1.6** Hitung ulang total index komposit dari `01_database_schema.sql` (cari semua klausa `INDEX idx_`). Bandingkan dengan klaim "Total Index Tambahan (Composite): 4" di Bab 2.1.
- [ ] **2.1.7** Verifikasi klaim "100% tabel memiliki `cabang_id`" — periksa setiap CREATE TABLE di SQL apakah memiliki kolom `cabang_id`. Tandai tabel yang tidak memilikinya jika ada.
- [ ] **2.1.8** Verifikasi klaim "100% tabel memiliki `created_at`/`updated_at`" — periksa setiap CREATE TABLE di SQL apakah memiliki kedua kolom timestamp ini.

#### 2.2 Validasi Diagram ERD Utama (Bab 3.1)

- [ ] **2.2.1** Untuk setiap tabel dalam diagram Mermaid Bab 3.1, verifikasi bahwa semua kolom PK dan FK yang ditampilkan sesuai dengan definisi DDL SQL. Cek apakah ada FK yang terdefinisi di SQL namun tidak muncul di diagram utama.
- [ ] **2.2.2** Verifikasi semua relasi (garis Crow's Foot) yang terdaftar dalam diagram Bab 3.1. Pastikan setiap relasi FK di SQL memiliki baris relasi yang bersesuaian di diagram. Tidak boleh ada relasi yang hilang.
- [ ] **2.2.3** Verifikasi label semantik relasi (misal: `"menaungi"`, `"memproses"`) untuk memastikan tidak ada label yang ambigu atau salah deskripsi jika dibandingkan dengan konteks bisnis di `01_business_requirements.md`.

#### 2.3 Validasi Diagram ERD per Kelompok (Bab 4)

- [ ] **2.3.1** Untuk setiap tabel pada Kelompok A–E (Bab 4.1 s.d 4.5), bandingkan satu per satu **nama kolom**, **tipe data**, **constraint (PK/FK/UQ)**, dan **deskripsi kolom** di diagram Mermaid dengan definisi aktual di `01_database_schema.sql` dan deskripsi di `05_data_dictionary.md`.
- [ ] **2.3.2** Pastikan tidak ada kolom yang ada di SQL namun tidak muncul di diagram sub-kelompok.
- [ ] **2.3.3** Pastikan tidak ada kolom yang muncul di diagram sub-kelompok namun tidak terdefinisi di SQL.
- [ ] **2.3.4** Validasi tipe data setiap kolom: pastikan tipe data pada diagram (misal: `int`, `varchar`, `decimal`, `timestamp`, `bigint`, `boolean`, `json`, `text`, `date`) tepat sesuai dengan DDL SQL. Perhatikan khususnya kolom `ukuran_file_kb` di `backup_logs` (harus `bigint`), dan kolom `stok_saat_ini` di `barang` (harus `decimal`).
- [ ] **2.3.5** Validasi semua relasi inter-tabel pada diagram sub-kelompok. Pastikan arah relasi (parent → child), kardinalitas (`||--o{`, `||--|{`, `||--||`), dan label semantik sesuai dengan FK DDL SQL.

#### 2.4 Validasi Matriks FK (Bab 5.1)

- [ ] **2.4.1** Bandingkan setiap baris dalam tabel Matriks FK Bab 5.1 (58 baris) dengan deklarasi FK aktual di `01_database_schema.sql`. Periksa: nama kolom FK, nama tabel parent, nama kolom referensi, aturan ON DELETE, dan aturan ON UPDATE.
- [ ] **2.4.2** Pastikan urutan nomor baris FK konsisten dan tidak ada nomor yang hilang atau terduplikasi.
- [ ] **2.4.3** Pastikan kolom "Keterangan Aturan Bisnis" untuk setiap FK didukung oleh narasi di `01_business_requirements.md` atau `02_software_requirements.md`.

#### 2.5 Validasi Constraint Komposit (Bab 5.3)

- [ ] **2.5.1** Ambil seluruh daftar UNIQUE KEY dari `01_database_schema.sql`. Bandingkan dengan daftar di Bab 5.3 (Unique Composite Constraints). Pastikan semua UNIQUE KEY yang ada di SQL terdokumentasi, dan tidak ada yang fiktif di dokumen.
- [ ] **2.5.2** Ambil seluruh daftar CHECK constraint (`CONSTRAINT chk_`) dari `01_database_schema.sql`. Bandingkan satu per satu dengan daftar di Bab 5.3. Pastikan nama constraint, nama kolom, dan ekspresi nilai valid (misal: `>= 0`, `> 0`, rentang nilai) semuanya akurat.
- [ ] **2.5.3** Jika ada CHECK constraint di SQL yang tidak ada di dokumen, tambahkan. Jika ada di dokumen namun tidak ada di SQL, hapus atau perbaiki.

#### 2.6 Validasi Kamus Entitas Ringkas (Bab 6)

- [ ] **2.6.1** Untuk setiap baris tabel di Bab 6, verifikasi kolom "Jumlah Kolom" dengan menghitung aktual kolom pada DDL CREATE TABLE di SQL (termasuk PK, FK, dan kolom biasa).
- [ ] **2.6.2** Verifikasi kolom "FK Keluar" untuk setiap tabel dengan menghitung semua klausa FOREIGN KEY di dalam definisi tabel tersebut di SQL.
- [ ] **2.6.3** Verifikasi kolom "FK Masuk" untuk setiap tabel dengan menghitung berapa banyak tabel lain yang merujuk ke tabel ini sebagai parent di SQL.
- [ ] **2.6.4** Verifikasi kolom "Sensitivitas" dengan mencocokkan ke `06_access_control_matrix.md`. Pastikan nilai `Operasional`, `Sensitif`, atau `Sangat Sensitif` konsisten.
- [ ] **2.6.5** Verifikasi kolom "Modul Terkait" dengan mencocokkan ke `02_software_requirements.md`.
- [ ] **2.6.6** Verifikasi kolom "Jenis Derivasi" (SRS-F-xxx atau **Derivasi**) dengan mencocokkan ke `05_data_dictionary.md` dan `02_software_requirements.md`.

#### 2.7 Validasi Catatan Desain (Bab 7)

- [ ] **2.7.1** Verifikasi Bab 7.1 (Multi-Cabang): pastikan klaim 28 tabel memiliki `cabang_id` sesuai dengan hasil hitung di langkah 2.1.7.
- [ ] **2.7.2** Verifikasi Bab 7.3 (Self-Referencing FK): pastikan pola relasi `bom_komposisi` dengan `barang` akurat sesuai DDL SQL (termasuk aturan ON DELETE RESTRICT vs CASCADE).
- [ ] **2.7.3** Verifikasi Bab 7.4 (Nullable FK): pastikan semua kolom nullable FK yang disebutkan memang terdefinisi sebagai `NULL` (bukan `NOT NULL`) di DDL SQL. Periksa apakah ada kolom nullable FK lain yang belum disebutkan di bab ini.
- [ ] **2.7.4** Verifikasi Bab 7.5 (7 Tabel Derivasi): pastikan daftar 7 tabel derivasi yang disebut konsisten dengan kolom "Jenis Derivasi = **Derivasi**" di Bab 6. Jika jumlahnya tidak cocok, sesuaikan narasi.
- [ ] **2.7.5** Verifikasi Bab 7.6 (Anti-Normalisasi): pastikan 4 kolom derived yang disebut (`detail_transaksi.subtotal`, `shift_handover.selisih`, `limbah_produksi.kerugian_nominal`, `payroll.gaji_bersih`) memang eksis di DDL SQL sebagai kolom fisik tersimpan (bukan GENERATED ALWAYS atau VIRTUAL).
- [ ] **2.7.6** Verifikasi Bab 7.7 (Composite Index): pastikan 4 index yang disebutkan beserta kolom-kolomnya persis sama dengan deklarasi `KEY idx_` atau `CREATE INDEX` di DDL SQL.
- [ ] **2.7.7** Verifikasi Bab 7.8 (Seed Data): pastikan data inisialisasi yang disebutkan (jumlah agen e-wallet, jumlah parameter system_configs, nilai nominal saldo awal) konsisten dengan data `INSERT INTO` di `01_database_schema.sql`.

#### 2.8 Validasi Contoh Query JOIN (Bab 8.3)

- [ ] **2.8.1** Periksa 3 contoh query SQL di Bab 8.3. Pastikan nama tabel, nama kolom, dan alias yang digunakan dalam query sesuai persis dengan DDL SQL. Query yang salah nama tabel/kolomnya akan menyesatkan developer.
- [ ] **2.8.2** Pastikan setiap query menggunakan jenis JOIN yang tepat (INNER JOIN vs LEFT JOIN) sesuai dengan aturan nullable FK yang terdefinisi. Kolom nullable FK harus menggunakan LEFT JOIN, bukan INNER JOIN.

#### 2.9 Validasi Referensi Dokumen (Bab 9)

- [ ] **2.9.1** Pastikan semua 6 referensi (REF-01 s.d REF-06) di tabel Bab 9 memiliki path file yang benar dan dapat ditemukan di dalam direktori `docs/sdlc/`. Verifikasi setiap path dengan membuka/list direktori.
- [ ] **2.9.2** Pastikan kolom "Kontribusi Konten Terhadap ERD" untuk setiap referensi akurat, spesifik, dan deskriptif — bukan hanya kalimat umum.

---

### TAHAP 3 — Validasi Relevansi & Kebersihan Konten

> **Tujuan**: Memastikan dokumen ERD hanya memuat data dan informasi yang memang seharusnya ada dalam sebuah dokumen ERD, bukan data yang seharusnya berada di dokumen lain.

- [ ] **3.1** Periksa apakah ada konten yang terlalu detail di tingkat implementasi (misalnya logika bisnis Python, konfigurasi server OS, atau prosedur deployment) yang seharusnya ada di dokumen Fase 04 Implementation atau dokumen lain. Jika ada, tandai untuk dihapus atau dipindahkan.
- [ ] **3.2** Periksa apakah ada duplikasi informasi yang kontradiktif antara Bab 3 (ERD Utama), Bab 4 (ERD per Kelompok), dan Bab 5 (Matriks Relasi). Duplikasi dalam format berbeda untuk tujuan berbeda tidak masalah, namun nilai/data yang saling bertentangan harus diperbaiki.
- [ ] **3.3** Periksa apakah Bab 1.6 (Konvensi Notasi) sudah mencakup **semua** notasi Mermaid erDiagram yang digunakan dalam diagram Bab 3 dan Bab 4. Jika ada notasi yang digunakan tapi tidak dijelaskan di legenda, tambahkan.
- [ ] **3.4** Periksa apakah ada tabel yang diklasifikasikan ke kelompok yang tidak tepat secara fungsional. Bandingkan dengan deskripsi kelompok dan justifikasi bisnis dari `01_business_requirements.md`.

---

### TAHAP 4 — Validasi Standar Struktur Dokumen

> **Tujuan**: Memastikan dokumen memiliki struktur yang sesuai dengan standar dokumentasi teknis ERD industri dan lengkap sebagai deliverable formal SDLC.

- [ ] **4.1** Periksa frontmatter YAML (metadata header): pastikan lengkap dan konsisten (field: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`). Tidak boleh ada field yang kosong.
- [ ] **4.2** Periksa tabel "Riwayat Perubahan Dokumen": pastikan ada dan mencatat semua versi sebelumnya dengan lengkap (kolom: Versi, Tanggal, Perubahan, Oleh). Versi terbaru harus di baris paling atas.
- [ ] **4.3** Periksa Bab 1 (Informasi Dokumen): pastikan memuat semua sub-bagian standar — Tujuan, Cakupan, Posisi SDLC, Hubungan dengan Dokumen Lain, Audiens Target, dan Konvensi Notasi/Legenda.
- [ ] **4.4** Periksa Bab 2 (Ringkasan Model Data): pastikan statistik ringkasan cukup detail dan klasifikasi tabel menggunakan tabel terformat yang informatif.
- [ ] **4.5** Periksa Bab 3 (ERD Utama) dan Bab 4 (ERD per Kelompok): pastikan keduanya hadir dan dapat dibedakan tujuannya — Bab 3 untuk gambaran global (PK/FK/UQ saja), Bab 4 untuk detail per kelompok (semua kolom beserta tipe data dan deskripsi).
- [ ] **4.6** Periksa Bab 5 (Matriks Relasi & Kardinalitas): pastikan memuat matriks FK lengkap, penjelasan aturan integritas referensial, dan daftar constraint komposit yang cukup detail untuk dipahami junior developer tanpa harus membuka SQL secara langsung.
- [ ] **4.7** Periksa Bab 6 (Kamus Entitas Ringkas): pastikan ada dan informatif sebagai quick-reference metadata 28 tabel.
- [ ] **4.8** Periksa Bab 7 (Catatan Desain & Keputusan Arsitektural): pastikan mendokumentasikan semua pola desain non-obvious yang dapat mempengaruhi keputusan coding backend (multi-branch, audit trail, self-referencing, nullable FK, derivasi, anti-normalisasi, index, seed data).
- [ ] **4.9** Periksa Bab 8 (Panduan Pembacaan untuk Fase Selanjutnya): pastikan memuat cara membaca notasi kardinalitas, petunjuk bagi backend developer, dan contoh query JOIN yang valid dan relevan.
- [ ] **4.10** Periksa Bab 9 (Referensi Dokumen): pastikan ada dan lengkap dengan tabel referensi berformat standar (No, Kode Ref, Nama Dokumen, Path Berkas, Kontribusi Konten).
- [ ] **4.11** Evaluasi apakah ada bab penting yang seharusnya ada dalam sebuah ERD dokumen industri namun belum hadir, misalnya:
  - Glosarium istilah teknis (jika banyak singkatan yang belum pernah dijelaskan di dalam dokumen).
  - Diagram arsitektur modul fungsional (jika belum ada visualisasi non-Mermaid yang menunjukkan hierarki kelompok tabel).
  - Jika perlu ditambahkan dan relevan, tambahkan bab tersebut dengan konten yang sesuai.

---

### TAHAP 5 — Validasi Kelayakan sebagai Input Fase Selanjutnya

> **Tujuan**: Memastikan dokumen cukup lengkap dan mandiri sehingga developer atau AI model dapat menggunakannya sebagai referensi utama tanpa harus selalu membuka SQL file atau bertanya kepada senior developer.

- [ ] **5.1** Baca kembali dokumen dari perspektif seorang **Backend Developer** yang pertama kali mengerjakan implementasi Python untuk AbuCom. Pastikan dokumen memberikan cukup informasi untuk:
  - Mengetahui tabel mana yang harus di-JOIN untuk setiap modul utama (Transaksi, Antrian, SDM, Keuangan, Audit)?
  - Mengetahui kolom mana yang nullable dan mana yang NOT NULL untuk penanganan error di Python?
  - Mengetahui aturan ON DELETE dan ON UPDATE untuk setiap FK agar tidak menyebabkan bug integritas referensial?
  - Mengetahui tabel mana yang memerlukan decorator `@require_role` tertentu berdasarkan level sensitivitas?
- [ ] **5.2** Identifikasi apakah ada "gap informasi" — yaitu pertanyaan teknis wajar yang mungkin diajukan oleh junior developer saat implementasi namun jawabannya tidak dapat ditemukan di dalam dokumen ini (selain harus membuka SQL secara langsung). Jika ada, isi gap tersebut di bagian yang paling relevan.
- [ ] **5.3** Pastikan format Mermaid erDiagram yang digunakan valid secara sintaks dan dapat dirender tanpa error oleh renderer Mermaid standar (GitHub Markdown). Perhatikan karakter khusus dalam label relasi — label yang mengandung spasi atau karakter non-alfanumerik harus dibungkus tanda kutip ganda (`"`).
- [ ] **5.4** Periksa apakah setiap tabel pada Bab 4 memiliki penjelasan naratif singkat **sebelum** blok diagram Mermaid yang menjelaskan peran dan konteks bisnis tabel tersebut dalam sistem AbuCom. Jika ada yang kurang deskriptif atau tidak ada sama sekali, tambahkan narasi yang informatif.

---

### TAHAP 6 — Validasi Bahasa Indonesia

> **Tujuan**: Memastikan seluruh narasi dokumen menggunakan bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau AI model yang lebih murah.

- [ ] **6.1** Baca seluruh narasi (bukan kode/diagram) dari dokumen dengan cermat. Identifikasi dan perbaiki kalimat yang:
  - Terlalu panjang atau berbelit-belit (lebih dari 40 kata dalam satu kalimat) — pecah menjadi dua kalimat atau lebih.
  - Menggunakan istilah teknis tanpa penjelasan konteks, terutama pada bagian yang ditujukan untuk audiens non-teknis (Kepala Percetakan, Staf Internal).
  - Memiliki makna ganda (ambigu) yang bisa disalah-tafsirkan oleh pembaca yang berbeda latar belakang.
- [ ] **6.2** Periksa konsistensi penggunaan istilah di seluruh dokumen:
  - "Tabel" vs "entitas" vs "relasi" — pastikan digunakan sesuai konteksnya secara konsisten.
  - Nama tabel SELALU ditulis dalam format backtick (contoh: `pengguna`, `transaksi`).
  - Nama kolom SELALU ditulis dalam format backtick (contoh: `cabang_id`, `no_invoice`).
  - Singkatan yang digunakan (FK, PK, UQ, DDL, ERD, RBAC, SDLC, SRS, BRD, ACM, DBA) harus sudah diperkenalkan kepanjangannya minimal satu kali di bagian awal dokumen.
- [ ] **6.3** Periksa apakah deskripsi kolom pada diagram Mermaid (teks dalam tanda kutip setelah nama tipe data) sudah informatif, singkat, dan tidak ambigu. Usahakan maksimal 10 kata per deskripsi. Jika ada yang lebih panjang atau tidak jelas, sederhanakan tanpa menghilangkan informasi esensial.
- [ ] **6.4** Periksa apakah label relasi Mermaid (teks setelah tanda titik dua pada baris relasi) sudah menggunakan kata kerja aktif yang tepat dan deskriptif (misal: `"menaungi"`, `"mencatat"`, `"memicu"`). Hindari label yang terlalu generik seperti `"ref"`, `"has"`, atau `"link"`.

---

### TAHAP 7 — Validasi Kelengkapan Data (Tidak Ada Data Kosong)

> **Tujuan**: Memastikan tidak ada field kosong, placeholder, atau data yang perlu diisi manual tersisa dalam dokumen.

- [ ] **7.1** Scan seluruh dokumen untuk menemukan teks berikut (semua variasi, case-insensitive): `TODO`, `TBD`, `[KOSONG]`, `[isi manual]`, `[...]`, `placeholder`, tanda dash panjang `—` yang digunakan sebagai pengganti data, atau sel tabel yang kosong. Jika ditemukan, isi dengan data yang sesuai berdasarkan referensi.
- [ ] **7.2** Periksa tabel Kamus Entitas Ringkas (Bab 6): pastikan setiap sel pada 28 baris x 9 kolom terisi dengan data yang valid, tidak ada yang kosong atau berisi tanda tanya.
- [ ] **7.3** Periksa tabel Matriks FK (Bab 5.1): pastikan setiap sel pada 58 baris x 9 kolom terisi dengan data yang valid. Kolom "Keterangan Aturan Bisnis" harus berupa kalimat deskriptif yang nyata, bukan placeholder.
- [ ] **7.4** Periksa tabel Referensi Dokumen (Bab 9): pastikan setiap sel pada 6 baris x 5 kolom terisi dengan data yang valid.
- [ ] **7.5** Periksa metadata frontmatter YAML: pastikan semua field memiliki nilai yang valid dan akurat, tidak ada yang kosong atau berisi tanda tanya.
- [ ] **7.6** Periksa tabel Riwayat Perubahan Dokumen: pastikan setiap baris riwayat memiliki semua kolom terisi (Versi, Tanggal, Perubahan, Oleh).

---

### TAHAP 8 — Penulisan Revisi & Overwrite File

> **PERINGATAN KRITIS**: Tahap ini adalah tahap paling penting dan tidak boleh dilakukan secara parsial. Seluruh isi dokumen **harus ditulis ulang sepenuhnya** dari baris pertama hingga terakhir. Tidak boleh ada pemotongan, peringkasan, atau penghilangan konten apa pun.

- [ ] **8.1** Kompilasi seluruh temuan dari Tahap 2 s.d 7 menjadi daftar perbaikan yang konkret. Untuk setiap perbaikan, catat: (a) lokasi bab/sub-bab, (b) data/teks lama yang salah, (c) data/teks baru yang benar dan valid.

- [ ] **8.2** Mulai menyusun dokumen revisi lengkap. Ikuti aturan penulisan berikut secara mutlak:
  - **Versi dokumen**: Ubah dari versi saat ini ke versi berikutnya (misal: `1.1` menjadi `1.2`) pada frontmatter YAML dan tabel Riwayat Perubahan.
  - **Tanggal**: Gunakan tanggal hari ini sebagai tanggal revisi di frontmatter dan tabel riwayat.
  - **Riwayat Perubahan**: Tambahkan baris baru di bagian **paling atas** tabel riwayat (bukan di bawah) yang merangkum semua perubahan yang dilakukan dalam revisi ini secara singkat, padat, dan informatif.
  - **Seluruh isi**: Pertahankan semua konten yang sudah benar dan valid. Perbaiki konten yang salah. Tambahkan konten yang kurang. Hapus atau pindahkan konten yang tidak relevan.

- [ ] **8.3** Tulis ulang seluruh isi dokumen ke file `docs/sdlc/03_design/02_erd_database.md` menggunakan mode **overwrite** (timpa file yang sudah ada). Pastikan hal-hal berikut terpenuhi secara mutlak:
  - Baris pertama dokumen hasil overwrite adalah `---` (baris pembuka frontmatter YAML).
  - Baris terakhir dokumen adalah baris terakhir konten Bab 9 (Referensi Dokumen) atau bab terakhir yang relevan, **tanpa ada baris yang terpotong atau hilang**.
  - Semua diagram Mermaid pada Bab 3 dan Bab 4 ditulis ulang lengkap — tidak ada diagram yang diringkas, dipotong dengan `...`, atau diganti dengan komentar `[dst]`.
  - Semua tabel markdown (Matriks FK, Kamus Entitas, Referensi Dokumen, Riwayat Perubahan) ditulis ulang baris per baris, tidak ada baris tabel yang dilewati atau diganti dengan `...`.
  - Semua blok kode SQL pada Bab 8.3 ditulis ulang sepenuhnya, tidak ada yang diringkas.

- [ ] **8.4** Setelah overwrite selesai, buka kembali file `docs/sdlc/03_design/02_erd_database.md` dan lakukan **verifikasi post-overwrite** satu per satu:
  - [ ] **8.4.1** Verifikasi baris pertama adalah `---` (pembuka frontmatter YAML).
  - [ ] **8.4.2** Verifikasi nomor versi sudah berubah ke versi terbaru.
  - [ ] **8.4.3** Verifikasi baris terakhir file tidak terpotong — bukan baris `...` atau baris setengah jadi yang tidak koheren.
  - [ ] **8.4.4** Hitung total baris file baru. Pastikan jumlahnya masuk akal (umumnya sama atau lebih banyak dari file sebelumnya jika ada penambahan konten, dan tidak berkurang drastis).
  - [ ] **8.4.5** Lakukan pencarian teks `TODO`, `TBD`, `[KOSONG]` di file baru. Pastikan tidak ditemukan satu pun.
  - [ ] **8.4.6** Pastikan tabel Riwayat Perubahan memiliki baris revisi terbaru di bagian paling atas dengan versi dan tanggal yang benar.

---

### TAHAP 9 — Pembaruan Daftar Referensi (Jika Ada Referensi Baru)

- [ ] **9.1** Jika selama proses validasi kamu menemukan bahwa ada file referensi lain di dalam `docs/sdlc/` yang ternyata digunakan atau dikutip dalam perbaikan dokumen (namun belum tercantum di Bab 9 tabel referensi), tambahkan file tersebut sebagai entri baru di akhir tabel Bab 9 dengan format yang konsisten:
  - Nomor urut berikutnya.
  - Kode referensi baru (misal: REF-07, REF-08, dst.).
  - Nama dokumen dan versinya.
  - Path berkas relatif yang akurat dan dapat ditemukan.
  - Deskripsi kontribusi konten yang spesifik terhadap ERD — bukan kalimat generik.
- [ ] **9.2** Pastikan penambahan referensi baru ini juga tercermin dalam deskripsi revisi pada tabel Riwayat Perubahan Dokumen.

---

## Catatan Penting untuk Pelaksana

> [!IMPORTANT]
> **Jangan pernah menulis ulang dokumen secara parsial atau terpotong.** Jika keterbatasan panjang output menghalangi penulisan seluruh dokumen dalam satu operasi tulis, lakukan penulisan dalam beberapa operasi **append** berurutan (bukan overwrite ulang), dimulai dari baris 1 dan berakhir di baris terakhir tanpa ada celah atau lompatan konten. Pastikan hasilnya adalah satu file utuh yang koheren.

> [!IMPORTANT]
> **Jangan membuat asumsi terhadap data yang tidak dapat ditemukan di referensi.** Jika ada informasi yang tidak dapat dikonfirmasi dari file referensi mana pun, cantumkan catatan eksplisit menggunakan HTML comment (misal: `<!-- Perlu konfirmasi: nilai X belum tersedia di referensi -->`) agar tim dapat menindaklanjutinya, daripada mengisi dengan data yang salah atau data fiktif.

> [!WARNING]
> **Perubahan versi dokumen bersifat wajib.** Setiap kali file ini di-overwrite, nomor versi HARUS dinaikkan satu level minor (misal: v1.1 menjadi v1.2). Jangan abaikan instruksi ini karena version tracking adalah mekanisme audit perubahan dokumen SDLC AbuCom yang tidak boleh dilewati.

> [!NOTE]
> **Prioritas validasi**: Validasi akurasi data teknis (Tahap 2) adalah yang paling kritis. Kesalahan statistik, FK yang hilang, tipe data yang salah, atau nama kolom yang tidak tepat di ERD akan langsung menyebabkan bug di implementasi Python Fase 04. Utamakan koreksi teknis ini di atas perbaikan bahasa atau penambahan struktur narasi.

---

## Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **selesai** jika dan hanya jika seluruh kondisi berikut terpenuhi:

- [ ] Seluruh checklist dari Tahap 1 hingga Tahap 9 sudah bertanda [x].
- [ ] File `docs/sdlc/03_design/02_erd_database.md` telah di-overwrite dengan konten versi terbaru yang nomor versinya lebih tinggi dari versi sebelumnya.
- [ ] Tidak ada kata kunci `TODO`, `TBD`, `[KOSONG]`, `placeholder` yang tersisa dalam file.
- [ ] Semua klaim statistik (total tabel, kolom, FK, UNIQUE constraint, CHECK constraint, index komposit) telah diverifikasi dan konsisten 100% dengan `01_database_schema.sql`.
- [ ] Semua diagram Mermaid erDiagram pada Bab 3 dan Bab 4 ditulis lengkap tanpa ada pemotongan atau diagram yang hilang.
- [ ] Semua tabel markdown (Matriks FK, Kamus Entitas Ringkas, Referensi Dokumen) ditulis lengkap tanpa ada baris yang hilang atau digantikan oleh `...`.
- [ ] Dokumen dapat dibaca, dipahami, dan digunakan secara mandiri oleh junior programmer atau AI model yang lebih murah sebagai acuan utama implementasi database, tanpa harus selalu menginterupsi proses kerja fase SDLC selanjutnya untuk meminta klarifikasi.

---

*Issue ini dibuat secara otomatis oleh sistem perencanaan SDLC AbuCom pada 2026-05-29. Untuk pertanyaan teknis terkait konteks proyek, rujuk file `docs/sdlc/narasi.txt` atau konsultasikan ke dokumen referensi yang tercantum di Bab 9 file target.*
