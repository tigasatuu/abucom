# Validasi Menyeluruh Dokumen Coding Standard

## 1. Konteks Tugas

| Field              | Detail                                                                                     |
| :----------------- | :----------------------------------------------------------------------------------------- |
| **Dokumen Utama**  | Coding Standard                                                                            |
| **Target File**    | `docs/sdlc/04_implementation/01_coding_standard.md`                                       |
| **Lokasi Referensi** | `docs/sdlc/`                                                                             |
| **Versi Saat Ini** | v1.1                                                                                       |
| **Versi Target**   | v1.2                                                                                       |
| **Status**         | Open                                                                                       |
| **Prioritas**      | Tinggi                                                                                     |
| **Fase SDLC**      | 04 — Implementation (Konstruksi Kode)                                                      |

### Latar Belakang

Dokumen **Coding Standard** (`docs/sdlc/04_implementation/01_coding_standard.md`) adalah deliverable pertama pada Fase Konstruksi SDLC AbuCom. Dokumen ini berfungsi sebagai **instruksi mutlak pengkodean** bagi Junior Programmer maupun model AI asisten pengembang. Karena dokumen ini menjadi acuan wajib bagi seluruh pengembangan kode sumber proyek, validitas, kelengkapan, dan kualitasnya harus ditegakkan dengan standar industri tertinggi sebelum digunakan sebagai input fase-fase SDLC berikutnya (pengujian, deployment, dan maintenance).

Dokumen ini saat ini telah berada pada versi **v1.1** dan telah melalui satu siklus revisi. Namun, perlu dilakukan audit independen yang menyeluruh untuk memastikan tidak ada informasi dari 9 dokumen referensi yang terlewat, struktur dokumen sudah baku sesuai standar industri, bahasa yang digunakan sudah natural dan tidak ambigu, serta tidak ada data kosong yang dapat menghambat pekerjaan fase selanjutnya.

---

## 2. Persona Pelaksana

> **PENTING**: Sebelum memulai pekerjaan apa pun, kamu harus sepenuhnya mengadopsi persona berikut ini. Seluruh penilaian, analisis, dan keputusan revisi harus dilakukan dari sudut pandang persona ini.

**Persona yang harus diadopsi:**

Kamu adalah seorang **Principal Software Engineering Standards Architect & Python Quality Assurance Lead** dengan spesialisasi mendalam di:
- Standar penulisan kode Python industri (PEP 8, PEP 257, PEP 484, PEP 3107)
- Arsitektur Pemrograman Fungsional Murni (Pure Functional Programming) Python tanpa OOP
- Praktik Secure Coding (OWASP, NIST 800-53, UU PDP No. 27/2022 Indonesia)
- Pengelolaan keamanan basis data relasional MySQL InnoDB (ACID, connection pooling, parameterized queries)
- Pembuatan dan validasi standar dokumentasi teknis industri perangkat lunak (IEEE 829, ISO/IEC 26514)
- Penilaian kelayakan dokumen teknis sebagai referensi bagi entitas eksekutor dengan kapabilitas terbatas (Junior Programmer dan LLM model ekonomis)

Kamu bersifat **kritis, teliti, dan tidak kompromi** terhadap standar. Kamu tidak akan menerima dokumen yang ambigu, tidak lengkap, atau berpotensi memicu kesalahan interpretasi oleh pelaksana dengan kapabilitas terbatas.

---

## 3. Daftar Dokumen Referensi yang Harus Dibaca

Sebelum melakukan analisis dokumen utama, kamu **WAJIB** membaca dan memahami seluruh isi dari dokumen-dokumen referensi berikut ini secara berurutan. Ini adalah sumber kebenaran tunggal (SSoT) yang harus divalidasi keselarasannya dengan dokumen utama.

| No | Nama Dokumen                        | Path File                                                       | Prioritas  |
| :-:| :---------------------------------- | :-------------------------------------------------------------- | :--------- |
| 1  | Tech Stack Decision                 | `docs/sdlc/01_planning/04_tech_stack_decision.md`               | PRIMER     |
| 2  | System Architecture                 | `docs/sdlc/03_design/03_system_architecture.md`                 | PRIMER     |
| 3  | Security Design                     | `docs/sdlc/03_design/06_security_design.md`                     | PRIMER     |
| 4  | BOM & HPP Design                    | `docs/sdlc/03_design/05_bom_hpp_design.md`                      | SEKUNDER   |
| 5  | CLI Interaction Flow                | `docs/sdlc/03_design/04_cli_interaction_flow.md`                | SEKUNDER   |
| 6  | Software Requirements Specification | `docs/sdlc/02_analysis/02_software_requirements.md`             | SEKUNDER   |
| 7  | Database Schema (DDL SQL)           | `docs/sdlc/03_design/01_database_schema.sql`                    | TERSIER    |
| 8  | ERD Database                        | `docs/sdlc/03_design/02_erd_database.md`                        | TERSIER    |
| 9  | Access Control Matrix               | `docs/sdlc/02_analysis/06_access_control_matrix.md`             | SEKUNDER   |

---

## 4. Tahapan Implementasi (Checklist Eksekusi)

Ikuti setiap tahapan secara **berurutan dari atas ke bawah**. Jangan melompati tahapan. Tandai `[x]` setiap checklist setelah selesai dikerjakan. Jangan melakukan penulisan file apa pun sebelum seluruh tahap analisis (Tahap 0 s.d. 9) selesai.

---

### TAHAP 0 — Persiapan & Pembacaan File

- [ ] **[BACA]** Buka dan baca seluruh isi file dokumen utama dari baris pertama hingga baris terakhir:
  `docs/sdlc/04_implementation/01_coding_standard.md`
  - Catat versi dokumen saat ini (saat ini: **v1.1**)
  - Catat semua bab/section yang ada (Bab 1 s.d. 18)
  - Catat semua file referensi yang disebutkan di Bab 18 (Referensi Dokumen)

- [ ] **[BACA]** Baca seluruh isi **Tech Stack Decision** (`docs/sdlc/01_planning/04_tech_stack_decision.md`) dari baris pertama hingga terakhir. Catat semua poin teknis kunci seperti:
  - Versi Python yang ditetapkan
  - Daftar dependensi library dengan versi terkunci
  - Aturan portabilitas Dual-OS
  - Standard library yang wajib digunakan

- [ ] **[BACA]** Baca seluruh isi **System Architecture** (`docs/sdlc/03_design/03_system_architecture.md`) dari baris pertama hingga terakhir. Catat semua poin teknis kunci seperti:
  - Arsitektur 4-layer beserta aturan dependensi antar-layer
  - Spesifikasi connection pool (`pool_name`, `pool_size`)
  - Mekanisme retry exponential backoff dan kode error MySQL yang ditangani (`2006`, `2013`)
  - Standard transaksional ACID (commit/rollback)
  - Strategi manajemen data Decimal dan tipe data numerik
  - Layout folder dan dekomposisi 10 modul bisnis

- [ ] **[BACA]** Baca seluruh isi **Security Design** (`docs/sdlc/03_design/06_security_design.md`) dari baris pertama hingga terakhir. Catat semua poin teknis kunci seperti:
  - Spesifikasi bcrypt cost factor
  - Spesifikasi JWT (algoritma, masa berlaku, format)
  - Matriks RBAC dan eskalasi otorisasi
  - Aturan sanitasi input CLI
  - Format audit log JSON (field-field wajib)
  - Spesifikasi enkripsi Fernet UU PDP (panjang kunci, kolom yang dilindungi)
  - Startup validator `.env` dan kode error startup

- [ ] **[BACA]** Baca seluruh isi **BOM & HPP Design** (`docs/sdlc/03_design/05_bom_hpp_design.md`) dari baris pertama hingga terakhir. Catat semua poin teknis kunci seperti:
  - Pseudocode pure FP untuk kalkulasi HPP
  - Pola NamedTuple yang digunakan
  - Logika sinkronisasi ATK internal
  - Aturan pembulatan Decimal spesifik

- [ ] **[BACA]** Baca seluruh isi **CLI Interaction Flow** (`docs/sdlc/03_design/04_cli_interaction_flow.md`) dari baris pertama hingga terakhir. Catat semua poin teknis kunci seperti:
  - Konvensi warna ANSI yang digunakan
  - Format error codes (`ERR-[KATEGORI]-[NOMOR]`)
  - Konvensi navigasi hotkey (misalnya tombol `0` untuk back)
  - Konvensi breadcrumb menu
  - Spesifikasi `getpass` untuk input password

- [ ] **[BACA]** Baca seluruh isi **Software Requirements Specification** (`docs/sdlc/02_analysis/02_software_requirements.md`) dari baris pertama hingga terakhir. Catat semua poin teknis kunci seperti:
  - Requirement non-fungsional performa
  - Target Code Coverage yang ditetapkan
  - Batasan runtime dan parameterisasi sistem

- [ ] **[BACA]** Baca seluruh isi **Database Schema DDL** (`docs/sdlc/03_design/01_database_schema.sql`) dari baris pertama hingga terakhir. Catat semua poin teknis kunci seperti:
  - Penamaan tabel dan kolom yang ada
  - Tipe data yang digunakan (khususnya `DECIMAL(15,4)`, `NULL`/`NOT NULL`)
  - Default value kolom
  - Constraint dan index
  - Storage engine yang digunakan (InnoDB)

- [ ] **[BACA]** Baca seluruh isi **ERD Database** (`docs/sdlc/03_design/02_erd_database.md`) dari baris pertama hingga terakhir. Catat entitas-entitas utama, relasi antar-tabel, dan konvensi penamaan entity.

- [ ] **[BACA]** Baca seluruh isi **Access Control Matrix** (`docs/sdlc/02_analysis/06_access_control_matrix.md`) dari baris pertama hingga terakhir. Catat:
  - Seluruh role pengguna yang ada
  - Daftar menu ID yang diotorisasi per role
  - Aturan eskalasi sandi supervisor/pemilik

---

### TAHAP 1 — Validasi Kelengkapan: Komparasi Dokumen Utama vs. Semua Referensi

> **Tujuan**: Memastikan tidak ada data, aturan, atau spesifikasi teknis penting dari dokumen-dokumen referensi yang terlewat atau tidak diakomodasi dalam dokumen utama.

#### 1.1 Komparasi dengan Tech Stack Decision

- [ ] **[ANALISIS]** Periksa apakah versi Python yang ditetapkan di Tech Stack Decision sudah tercantum secara eksplisit di dokumen utama (Bab 2.2, 7.2, dan bagian lain yang relevan).
- [ ] **[ANALISIS]** Periksa apakah setiap dependensi library beserta versi terkunci yang ada di Tech Stack Decision sudah tercantum lengkap di Bab 13 dokumen utama. Cocokkan satu per satu.
- [ ] **[ANALISIS]** Periksa apakah aturan portabilitas Dual-OS dari Tech Stack Decision sudah diakomodasi sepenuhnya di Bab 12 dokumen utama.
- [ ] **[ANALISIS]** Periksa apakah ada standard library Python yang disebut di Tech Stack Decision namun tidak tercantum di Bab 13.4 dokumen utama.
- [ ] **[CATAT]** Buat daftar temuan gap (jika ada) dari komparasi ini.

#### 1.2 Komparasi dengan System Architecture

- [ ] **[ANALISIS]** Periksa apakah spesifikasi `pool_name="abupool"` dan `pool_size=5` sudah disebutkan secara konsisten dan eksplisit di Bab 8.9 dan 9.5 dokumen utama.
- [ ] **[ANALISIS]** Periksa apakah mekanisme retry exponential backoff 3 kali dengan kode error `2006` dan `2013` sudah dijelaskan secara spesifik di Bab 8.9 dan 9.6 dokumen utama.
- [ ] **[ANALISIS]** Periksa apakah seluruh 10 modul bisnis (M.1 s.d. M.10) dari System Architecture sudah terwakili dalam layout direktori di Bab 4.1 dokumen utama dan masing-masing modul teridentifikasi dalam komentar di struktur direktori.
- [ ] **[ANALISIS]** Periksa apakah aturan one-way dependency antar-layer (`cli/ → logic/ → db/ → MySQL`) sudah tercantum dan tidak ada kontradiksi dengan System Architecture.
- [ ] **[ANALISIS]** Periksa apakah standard mapping `DECIMAL(15,4)` MySQL ↔ `Decimal('0.0000')` Python sudah tercantum di Bab 9.7.
- [ ] **[ANALISIS]** Periksa apakah penanganan `NULL` MySQL → `None` Python beserta helper function default `Decimal('0.0000')` sudah ada di Bab 9.8.
- [ ] **[CATAT]** Buat daftar temuan gap (jika ada) dari komparasi ini.

#### 1.3 Komparasi dengan Security Design

- [ ] **[ANALISIS]** Periksa apakah bcrypt cost factor 12 sudah disebutkan secara eksplisit di Bab 10.2 dokumen utama.
- [ ] **[ANALISIS]** Periksa apakah algoritma JWT HS256, masa berlaku 8 jam (28.800 detik), dan secret key dari `.env` sudah disebutkan di Bab 10.3 dokumen utama.
- [ ] **[ANALISIS]** Periksa apakah aturan RBAC guard decorator/fungsional mengacu pada matriks otorisasi dari Access Control Matrix (bukan hardcode biner) sudah tercantum di Bab 10.4.
- [ ] **[ANALISIS]** Periksa apakah aturan sanitasi input CLI (pembuangan karakter kontrol di bawah byte `\x20`, termasuk `\x1b` ANSI escape) sudah ada di Bab 10.5.
- [ ] **[ANALISIS]** Periksa apakah format field-field wajib audit log JSON di tabel `audit_logs` (termasuk `old_value`, `new_value`) sudah disebutkan di Bab 10.6.
- [ ] **[ANALISIS]** Periksa apakah enkripsi Fernet 32-byte dari `.env` untuk kolom WhatsApp CRM pelanggan sudah disebutkan di Bab 10.7. Pastikan nama library `cryptography==42.0.5` tercantum di Bab 13.2.
- [ ] **[ANALISIS]** Periksa apakah startup validator `.env` dengan kode error `ERR-FILE-001` (atau kode setara) sudah ada di Bab 10.1.
- [ ] **[CATAT]** Buat daftar temuan gap (jika ada) dari komparasi ini.

#### 1.4 Komparasi dengan BOM & HPP Design

- [ ] **[ANALISIS]** Periksa apakah pola NamedTuple yang digunakan di pseudocode BOM & HPP Design (misal: `BOMItem`) sudah menjadi contoh standar di Bab 8.3 dokumen utama.
- [ ] **[ANALISIS]** Periksa apakah aturan pembulatan `ROUND_HALF_UP` dan presisi `Decimal('0.0001')` yang digunakan di BOM & HPP sudah tercantum di Bab 2.4 dan 9.7 dokumen utama.
- [ ] **[ANALISIS]** Periksa apakah logika sinkronisasi pengurangan stok ATK internal sudah disebutkan atau direferensikan di bagian yang relevan.
- [ ] **[CATAT]** Buat daftar temuan gap (jika ada) dari komparasi ini.

#### 1.5 Komparasi dengan CLI Interaction Flow

- [ ] **[ANALISIS]** Periksa apakah format error code `ERR-[KATEGORI]-[NOMOR]` beserta contoh penggunaannya sudah ada di Bab 11.5 dokumen utama.
- [ ] **[ANALISIS]** Periksa apakah konvensi warna ANSI (Hijau/Merah/Kuning/Biru) yang ditetapkan di CLI Interaction Flow sudah konsisten dengan yang tercantum di Bab 11.1.
- [ ] **[ANALISIS]** Periksa apakah tombol `0` sebagai hotkey navigasi back dan format breadcrumb sudah ada di Bab 11.3.
- [ ] **[ANALISIS]** Periksa apakah konvensi `getpass` untuk input password sudah ada di Bab 11.4.
- [ ] **[CATAT]** Buat daftar temuan gap (jika ada) dari komparasi ini.

#### 1.6 Komparasi dengan Software Requirements Specification

- [ ] **[ANALISIS]** Periksa apakah target Code Coverage yang mungkin ditetapkan di SRS sudah selaras dengan Bab 14.2 dokumen utama (≥ 90%).
- [ ] **[ANALISIS]** Periksa apakah requirement non-fungsional performa (misalnya waktu respons operasi) yang ada di SRS sudah diakomodasi atau direferensikan.
- [ ] **[CATAT]** Buat daftar temuan gap (jika ada) dari komparasi ini.

#### 1.7 Komparasi dengan Database Schema (DDL SQL)

- [ ] **[ANALISIS]** Periksa apakah konvensi penamaan kolom di dokumen utama (Bab 3.7) sudah mencerminkan seluruh penamaan tabel dan kolom aktual yang ada di DDL SQL (khususnya tabel-tabel utama: `pengguna`, `pelanggan`, `audit_logs`, dan tabel bisnis lainnya).
- [ ] **[ANALISIS]** Periksa apakah tipe data `DECIMAL(15,4)` di DDL sudah 100% selaras dengan standard Python `Decimal('0.0000')` yang tercantum di dokumen utama.
- [ ] **[ANALISIS]** Periksa apakah storage engine `InnoDB` sudah disebutkan di dokumen utama sebagai alasan dukungan transaksi ACID.
- [ ] **[CATAT]** Buat daftar temuan gap (jika ada) dari komparasi ini.

#### 1.8 Komparasi dengan ERD Database

- [ ] **[ANALISIS]** Periksa apakah nama-nama entitas utama di ERD sudah selaras dengan konvensi penamaan variabel Python di dokumen utama (Bab 3.7).
- [ ] **[ANALISIS]** Periksa apakah ada entitas di ERD yang belum diakomodasi dalam struktur direktori atau aturan penamaan di dokumen utama.
- [ ] **[CATAT]** Buat daftar temuan gap (jika ada) dari komparasi ini.

#### 1.9 Komparasi dengan Access Control Matrix

- [ ] **[ANALISIS]** Periksa apakah seluruh role yang ada di Access Control Matrix (pemilik, kasir, gudang, dll.) sudah tercantum sebagai contoh di Bab 10.4 dokumen utama.
- [ ] **[ANALISIS]** Periksa apakah aturan eskalasi sandi supervisor/pemilik untuk operasi retur/opname sudah disebutkan di Bab 11.4 (getpass) atau bagian yang relevan.
- [ ] **[CATAT]** Buat daftar temuan gap (jika ada) dari komparasi ini.

---

### TAHAP 2 — Validasi Relevansi: Dokumen Utama Hanya Berisi Informasi yang Sesuai

> **Tujuan**: Memastikan dokumen utama tidak memuat informasi yang tidak relevan, duplikat berlebihan, atau menyalin konten yang seharusnya hanya direferensikan (bukan diulang) dari dokumen lain.

- [ ] **[ANALISIS]** Periksa setiap bab dokumen utama: apakah ada konten yang terlalu mendetail tentang topik yang seharusnya hanya menjadi domain dokumen referensi lain? (Misalnya: apakah ada penjelasan lengkap desain database yang seharusnya hanya ada di DDL/ERD?)
- [ ] **[ANALISIS]** Periksa apakah contoh kode Python yang disertakan di dokumen utama (Bab 2, 6, 7, 8, 9, 10, 11, 12) sudah **spesifik pada standar pengkodean** dan bukan pada logika bisnis detail yang seharusnya ada di dokumen desain?
- [ ] **[ANALISIS]** Periksa apakah ada pengulangan konten yang sama persis di lebih dari satu bab tanpa justifikasi yang jelas (redundansi yang tidak perlu)?
- [ ] **[ANALISIS]** Periksa apakah setiap aturan yang tercantum memang relevan dengan konteks "standar penulisan kode" dan bukan merupakan "spesifikasi desain" atau "spesifikasi requirement"?
- [ ] **[CATAT]** Buat daftar konten yang dinilai tidak relevan atau berlebihan (jika ada).

---

### TAHAP 3 — Validasi Struktur Dokumen: Standar Industri

> **Tujuan**: Memastikan struktur dan susunan bab dokumen utama memenuhi standar penulisan dokumen teknis industri perangkat lunak.

- [ ] **[ANALISIS]** Periksa apakah dokumen memiliki **metadata header** yang lengkap (nama dokumen, versi, tanggal, status, penyusun).
- [ ] **[ANALISIS]** Periksa apakah dokumen memiliki **riwayat perubahan (change log)** yang tercatat dengan baik.
- [ ] **[ANALISIS]** Periksa apakah urutan bab sudah logis dan mengalir secara hierarkis:
  - Informasi Dokumen → Prinsip Dasar → Konvensi Penamaan → Struktur Direktori → Format Kode → Dokumentasi → Type Hints → Arsitektur → Database → Keamanan → CLI → Portabilitas → Dependensi → Testing → Version Control → Larangan → Checklist → Referensi.
- [ ] **[ANALISIS]** Periksa apakah setiap aturan yang disebutkan sudah **diklasifikasikan** menggunakan level kepatuhan RFC 2119 yang telah ditetapkan di Bab 1.7 (`[WAJIB]`, `[DILARANG]`, `[DIREKOMENDASIKAN]`, `[OPSIONAL]`).
- [ ] **[ANALISIS]** Periksa apakah setiap contoh kode Python yang disajikan memiliki:
  - Label konteks yang jelas (`# PATUH STANDARD:` atau `# MELANGGAR:`)
  - Komentar penjelasan singkat
  - Kode yang dapat dieksekusi (sintaksis Python yang benar)
- [ ] **[ANALISIS]** Periksa apakah **tabel ringkasan** (seperti Tabel Konvensi Penamaan di Bab 3.8 dan Tabel Larangan di Bab 16) sudah lengkap, akurat, dan formatnya konsisten.
- [ ] **[ANALISIS]** Periksa apakah Bab 18 (Referensi Dokumen) sudah lengkap dan seluruh dokumen yang disebutkan di dalam teks dokumen utama juga tercantum di tabel referensi.
- [ ] **[ANALISIS]** Periksa apakah setiap referensi silang di dalam dokumen utama (seperti `(Ref: [Security Design] Bab X.Y)`) sudah mengarah ke bab/bagian yang benar dan relevan.
- [ ] **[CATAT]** Buat daftar temuan ketidaksesuaian struktur (jika ada).

---

### TAHAP 4 — Validasi Kelayakan sebagai Referensi Input Fase SDLC Berikutnya

> **Tujuan**: Memastikan dokumen utama ini cukup kuat dan komprehensif untuk menjadi acuan dan input utama bagi dokumen-dokumen fase SDLC berikutnya (testing, deployment, maintenance).

- [ ] **[ANALISIS]** Periksa apakah aturan di Bab 14 (Testing Standards) sudah cukup spesifik untuk dijadikan dasar penulisan **Test Plan** dan **Test Case** pada Fase 05?
  - Apakah ada target Coverage yang jelas?
  - Apakah ada konvensi penamaan test file dan test function?
  - Apakah ada aturan tentang penggunaan mock/fixture untuk pure functions?
  - Apakah ada aturan tentang test isolation (tidak boleh koneksi DB production)?
- [ ] **[ANALISIS]** Periksa apakah aturan di Bab 15 (Version Control) sudah cukup lengkap untuk dijadikan pedoman operasional Git harian bagi programmer?
  - Apakah ada konvensi penamaan branch?
  - Apakah ada aturan commit message?
  - Apakah ada aturan merge/PR?
- [ ] **[ANALISIS]** Periksa apakah aturan di Bab 13 (Dependensi) dan Bab 12 (Portabilitas) sudah cukup untuk mendukung proses **Deployment** pada Fase 06?
- [ ] **[ANALISIS]** Periksa apakah Bab 17 (Checklist Kepatuhan) cukup komprehensif sebagai gate check sebelum kode di-merge, sehingga kode yang masuk ke branch utama sudah terjamin kualitasnya?
- [ ] **[ANALISIS]** Periksa apakah ada aspek pengkodean penting yang sama sekali belum dibahas dalam dokumen ini yang dapat menghambat pekerjaan fase selanjutnya? Misalnya:
  - Aturan penanganan logging aplikasi (bukan hanya audit trail keamanan)
  - Aturan penanganan konfigurasi environment (development vs. production)
  - Aturan tentang format struk nota cetak thermal
- [ ] **[CATAT]** Buat daftar temuan (jika ada).

---

### TAHAP 5 — Validasi Kualitas Bahasa Indonesia

> **Tujuan**: Memastikan seluruh teks dokumen menggunakan Bahasa Indonesia yang baku, natural, tidak ambigu, dan mudah dipahami oleh Junior Programmer atau model AI yang lebih sederhana.

- [ ] **[ANALISIS]** Baca ulang seluruh teks naratif (bukan kode) dari setiap bab. Identifikasi kalimat yang:
  - Terlalu panjang dan sulit diparsing dalam satu baca
  - Menggunakan kata teknis bahasa Inggris tanpa konteks yang cukup
  - Ambigu (dapat diinterpretasikan dengan lebih dari satu makna)
  - Menggunakan kalimat pasif berlebihan yang menyembunyikan subjek (siapa yang harus melakukan apa)
- [ ] **[ANALISIS]** Periksa apakah semua akronim dan singkatan teknis yang digunakan di dalam teks sudah didefinisikan di Bab 1.6 (Definisi, Akronim, dan Singkatan)?
  - Contoh: apakah akronim `HOF`, `CRUD`, `UoM`, `OPEX`, `UPS` yang ada di Bab 1.6 memang benar-benar digunakan di dalam teks dokumen, atau hanya terdaftar tanpa penggunaan?
- [ ] **[ANALISIS]** Periksa konsistensi penggunaan istilah teknis di seluruh dokumen:
  - Apakah istilah "pure function" dan "fungsi murni" digunakan secara konsisten dan tidak saling menggantikan secara acak?
  - Apakah istilah "imutabel" dan "immutable" digunakan konsisten?
  - Apakah istilah untuk "sandi" vs "password" vs "kredensial" digunakan pada konteks yang tepat?
- [ ] **[ANALISIS]** Periksa apakah setiap aturan (`[WAJIB]`, `[DILARANG]`, dll.) dirumuskan dalam kalimat aktif yang jelas: siapa yang melakukan apa, dalam kondisi apa, dengan menggunakan apa?
- [ ] **[CATAT]** Buat daftar kalimat atau frasa yang perlu diperbaiki (jika ada).

---

### TAHAP 6 — Validasi Kelengkapan: Tidak Ada Gangguan bagi Fase Berikutnya

> **Tujuan**: Memastikan tidak ada bagian dalam dokumen yang setengah jadi, tidak jelas, atau akan selalu dipertanyakan oleh pelaksana, sehingga pekerjaan fase selanjutnya tidak terganggu.

- [ ] **[ANALISIS]** Baca setiap aturan dan instruksi. Identifikasi aturan yang:
  - Menggunakan frasa tidak pasti seperti "sesuai kebutuhan", "jika diperlukan", "dll.", "dan sebagainya" tanpa definisi yang lebih konkret.
  - Menimbulkan pertanyaan lanjutan yang wajar bagi pembaca baru (misalnya: "berapa lama retry interval-nya?", "di tabel mana audit log disimpan?")
- [ ] **[ANALISIS]** Periksa apakah setiap boilerplate kode Python yang disertakan (Bab 8, 9, 10, 11, 12) sudah **siap pakai** (syntactically correct, tidak ada placeholder yang perlu diisi seperti `# TODO: implement here`)?
- [ ] **[ANALISIS]** Periksa apakah aturan tentang **interval waktu retry** di Bab 8.9 dan 9.6 sudah spesifik (misalnya: "1 detik, 2 detik, 4 detik" atau "menggunakan formula `2^attempt` detik")?
- [ ] **[ANALISIS]** Periksa apakah Checklist di Bab 17 sudah mencakup semua aspek kritis yang disebutkan di seluruh dokumen (tidak ada aturan penting yang tidak masuk checklist)?
- [ ] **[CATAT]** Buat daftar temuan (jika ada).

---

### TAHAP 7 — Validasi dan Pengisian Data Kosong

> **Tujuan**: Mengidentifikasi dan mengisi setiap bagian dokumen yang memiliki data kosong, placeholder, atau nilai yang belum ditetapkan.

- [ ] **[ANALISIS]** Cari seluruh teks dalam dokumen yang mengandung:
  - `[BELUM DIISI]`, `[TBD]`, `[TODO]`, `[N/A]`, `...`, atau placeholder setara
  - Tanda kurung kosong `()` atau `[]` tanpa isi
  - Kalimat yang berakhir dengan ":" tanpa konten di bawahnya
- [ ] **[ANALISIS]** Untuk setiap data kosong yang ditemukan, tentukan apakah:
  - Data tersebut dapat diisi menggunakan informasi dari dokumen-dokumen referensi yang sudah dibaca di Tahap 0
  - Data tersebut dapat diisi menggunakan pengetahuan domain standar industri Python
  - Data tersebut memang tidak relevan dan bagian tersebut sebaiknya dihapus
- [ ] **[TINDAKAN]** Isi setiap data kosong yang dapat diisi dengan nilai yang spesifik, akurat, dan sesuai konteks dokumen. Jangan biarkan satu pun placeholder kosong tersisa.
- [ ] **[VERIFIKASI]** Setelah semua data kosong diisi, verifikasi kembali bahwa data yang diisikan konsisten dengan dokumen referensi.

---

### TAHAP 8 — Validasi Spesifik Dokumen Coding Standard

> **Tujuan**: Melakukan pemeriksaan aspek-aspek khusus yang merupakan ciri khas dokumen Coding Standard dan umumnya menjadi titik lemah dalam dokumen sejenis.

- [ ] **[ANALISIS]** **Kelengkapan Contoh Kode**: Periksa apakah setiap aturan pengkodean yang bersifat `[WAJIB]` atau `[DILARANG]` sudah disertai dengan **minimal satu contoh kode** yang menunjukkan pola salah (❌) dan pola benar (✅)?
- [ ] **[ANALISIS]** **Sintaksis Python 3.14.2+**: Verifikasi bahwa seluruh contoh kode Python dalam dokumen:
  - Tidak menggunakan `typing.List`, `typing.Dict`, `typing.Tuple` (deprecated di Python 3.9+, dan dilarang di Python 3.14.2+)
  - Menggunakan `list[...]`, `dict[...]`, `tuple[...]` secara langsung
  - Menggunakan operator pipe `|` untuk Union type (misalnya `Decimal | None`)
  - Menggunakan sintaksis `from collections import namedtuple` yang benar
  - Semua import sudah sesuai dan tidak ada circular import
- [ ] **[ANALISIS]** **Konsistensi Contoh NamedTuple vs Frozen Dataclass**: Periksa apakah panduan pemilihan antara `NamedTuple` dan `@dataclass(frozen=True)` di Bab 3.5 sudah jelas dan tidak ambigu?
- [ ] **[ANALISIS]** **Kelengkapan Error Code Catalog**: Periksa apakah Bab 11.5 hanya menyebut format error code tanpa memberikan **catalog/daftar** error code yang sudah didefinisikan? Jika iya, apakah perlu ada tabel catalog error code minimal untuk kategori utama (ERR-AUTH, ERR-DB, ERR-STOCK, ERR-FILE, ERR-VAL, ERR-NET)?
- [ ] **[ANALISIS]** **Template Boilerplate Module Header**: Periksa apakah Bab 6.4 hanya menyebut kewajiban module header tanpa memberikan **template konkret** boilerplate-nya? Jika iya, tambahkan template header file `.py` yang lengkap.
- [ ] **[ANALISIS]** **Konvensi Penulisan Commit Message**: Periksa apakah Bab 15 mencantumkan konvensi format commit message yang jelas (misalnya format Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`)? Jika belum ada, tambahkan.
- [ ] **[ANALISIS]** **Penanganan Konfigurasi Environment**: Periksa apakah ada aturan tentang bagaimana membedakan konfigurasi `development` vs `production` (misalnya variabel `APP_ENV` di `.env`)? Jika belum ada dan relevan, tambahkan.
- [ ] **[ANALISIS]** **Standard Logging Aplikasi**: Periksa apakah ada aturan tentang penggunaan modul `logging` Python standar untuk debugging dan informasi runtime aplikasi (berbeda dari audit trail keamanan)? Jika ada gap, tambahkan.
- [ ] **[CATAT]** Buat daftar temuan dari validasi spesifik ini.

---

### TAHAP 9 — Kompilasi Seluruh Temuan dan Penyusunan Dokumen Revisi

> **Tujuan**: Mengintegrasikan seluruh temuan dari Tahap 1-8 menjadi satu dokumen revisi yang komprehensif dan siap untuk dituliskan.

- [ ] **[KOMPILASI]** Buat daftar konsolidasi semua temuan dari seluruh tahap analisis (Tahap 1 s.d. 8), kelompokkan berdasarkan jenis:
  - **GAP**: Informasi dari referensi yang terlewat
  - **IRRELEVAN**: Konten yang tidak sesuai domain dokumen ini
  - **STRUKTUR**: Ketidaksesuaian struktur atau format
  - **BAHASA**: Kalimat ambigu atau tidak natural
  - **DATA KOSONG**: Placeholder atau nilai yang belum diisi
  - **KODE**: Contoh kode yang salah sintaksis atau tidak lengkap
  - **TAMBAHAN**: Konten baru yang perlu ditambahkan sesuai standar industri

- [ ] **[RENCANA]** Untuk setiap temuan, tentukan tindakan yang akan diambil:
  - Tambah konten baru
  - Perbaiki kalimat yang ada
  - Isi data kosong
  - Hapus konten yang tidak relevan
  - Perbaiki contoh kode
  - Perbaiki referensi silang

- [ ] **[VERIFIKASI AKHIR]** Sebelum menulis ulang, pastikan:
  - Semua gap dari referensi sudah akan ditangani
  - Tidak ada instruksi baru yang bertentangan dengan aturan yang sudah ada
  - Versi dokumen sudah direncanakan untuk diubah dari `v1.1` menjadi `v1.2`
  - Tanggal dokumen sudah direncanakan untuk diperbarui ke tanggal revisi hari ini
  - Riwayat perubahan sudah akan diperbarui dengan ringkasan perubahan yang komprehensif

---

### TAHAP 10 — Penulisan Ulang Dokumen ke Target File (OVERWRITE)

> **Tujuan**: Menuangkan seluruh hasil validasi dan perbaikan ke dalam file target dengan cara menimpa (overwrite) secara penuh.

> **⚠️ PERINGATAN KRITIS**: Tahap ini adalah tahap penulisan. Baca seluruh instruksi di bawah ini sebelum mulai menulis.

#### 10.1 Persiapan Penulisan

- [ ] **[PERSIAPAN]** Konfirmasi bahwa seluruh Tahap 0 s.d. 9 sudah selesai dan seluruh temuan sudah dikompilasi.
- [ ] **[PERSIAPAN]** Siapkan versi final dokumen lengkap di memori/scratch sebelum mulai menulis ke file.
- [ ] **[PERSIAPAN]** Pastikan versi dokumen sudah diubah: **dari `v1.1` menjadi `v1.2`**.
- [ ] **[PERSIAPAN]** Pastikan tanggal dokumen di header sudah diperbarui ke tanggal hari ini.
- [ ] **[PERSIAPAN]** Pastikan entri riwayat perubahan versi `v1.2` sudah disiapkan dengan deskripsi yang informatif tentang perubahan yang dilakukan.

#### 10.2 Penulisan File (Overwrite)

- [ ] **[TULIS]** Buka file target: `docs/sdlc/04_implementation/01_coding_standard.md`
- [ ] **[TULIS]** Timpa (overwrite) seluruh konten file dari baris pertama hingga baris terakhir dengan dokumen revisi yang telah disiapkan.
- [ ] **[WAJIB - NO TRUNCATION]** **INSTRUKSI MUTLAK**: Seluruh teks dokumen dari baris pertama (metadata header `---`) hingga baris terakhir (baris terakhir Bab 18 Referensi Dokumen) HARUS ditulis ulang sepenuhnya. **DILARANG KERAS** melakukan:
  - Memotong konten di tengah jalan
  - Menulis `[... konten selanjutnya tidak berubah ...]` atau kalimat serupa
  - Meringkas bab atau subbab yang "dianggap tidak berubah"
  - Menghilangkan contoh kode yang ada
  - Menghilangkan bab mana pun
- [ ] **[VERIFIKASI PANJANG]** Setelah selesai menulis, bandingkan jumlah baris file baru dengan file lama (v1.1 memiliki **864 baris**). Dokumen revisi v1.2 diperkirakan memiliki lebih banyak baris karena ada penambahan konten.

#### 10.3 Verifikasi Pasca Penulisan

- [ ] **[VERIFIKASI]** Baca ulang 20 baris pertama file yang baru ditulis. Pastikan metadata header sudah benar (versi `v1.2`, tanggal terbaru, status `Approved`).
- [ ] **[VERIFIKASI]** Baca ulang bagian Riwayat Perubahan. Pastikan entri `v1.2` sudah ada dan isi `v1.1` masih ada (tidak dihapus).
- [ ] **[VERIFIKASI]** Cari teks `v1.1` di dalam isi dokumen (bukan di riwayat perubahan). Jika ada referensi versi di diagram atau judul yang seharusnya diperbarui ke `v1.2`, pastikan sudah diperbarui.
- [ ] **[VERIFIKASI]** Baca ulang Bab 18 (Referensi Dokumen). Pastikan semua referensi yang ada di v1.1 masih ada, dan jika ada referensi baru yang ditambahkan selama proses perbaikan, sudah ditambahkan di baris paling bawah tabel.
- [ ] **[VERIFIKASI]** Pastikan tidak ada karakter encoding yang rusak (karakter aneh seperti `â€"` atau `Ã`) akibat masalah encoding saat penulisan file. Gunakan encoding `utf-8` secara eksplisit.

---

### TAHAP 11 — Penambahan Referensi Baru (Jika Ada)

> **Tujuan**: Memastikan setiap dokumen atau sumber baru yang digunakan selama proses perbaikan dicatat secara formal di Bab 18 dokumen utama.

- [ ] **[PERIKSA]** Apakah selama proses analisis dan perbaikan (Tahap 1-9), kamu menggunakan informasi dari dokumen atau sumber yang **belum tercantum** di Bab 18 Referensi Dokumen?
- [ ] **[TINDAKAN]** Jika ya, tambahkan setiap dokumen/sumber baru tersebut ke tabel Bab 18 dengan format yang sama:
  - Nomor urut (lanjutkan dari nomor terakhir)
  - Nama Dokumen Referensi
  - Path Relatif File
  - Versi
  - Prioritas (PRIMER / SEKUNDER / TERSIER)
  - Peran dalam Penyusunan (deskripsi singkat kontribusi referensi ini)
- [ ] **[VERIFIKASI]** Pastikan semua referensi baru yang ditambahkan benar-benar ada file-nya di dalam proyek (path yang dicantumkan valid).

---

## 5. Kriteria Selesai (Definition of Done)

Issue ini dinyatakan selesai apabila seluruh kondisi berikut terpenuhi:

- [ ] Seluruh 11 Tahap di atas telah dieksekusi dan semua item checklist bertanda `[x]`.
- [ ] File `docs/sdlc/04_implementation/01_coding_standard.md` telah berhasil ditimpa (overwrite) dengan dokumen versi `v1.2`.
- [ ] Dokumen v1.2 memiliki jumlah baris yang sama atau lebih banyak dari v1.1 (864 baris), sebagai bukti tidak ada konten yang dihilangkan.
- [ ] Metadata header dokumen mencantumkan versi `v1.2` dan tanggal revisi terbaru.
- [ ] Riwayat perubahan mencantumkan entri `v1.2` dengan deskripsi perubahan yang komprehensif.
- [ ] Tidak ada satu pun placeholder kosong (`[TBD]`, `[BELUM DIISI]`, dll.) yang tersisa di dalam dokumen.
- [ ] Semua contoh kode Python dalam dokumen menggunakan sintaksis yang valid untuk Python 3.14.2+ (tidak ada `typing.List`, dll.).
- [ ] Semua referensi baru yang digunakan sudah ditambahkan ke Bab 18.
- [ ] Seluruh aturan penting di dalam dokumen sudah tercantum di Checklist Kepatuhan (Bab 17).

---

## 6. Catatan Tambahan untuk Pelaksana

> Baca catatan ini sebelum memulai pekerjaan.

1. **Jangan membuat asumsi**: Jika sebuah nilai atau spesifikasi tidak ditemukan di dokumen referensi maupun di dokumen utama, cari terlebih dahulu di dokumen referensi lain yang ada. Jika benar-benar tidak ada, gunakan standar industri Python yang paling umum dan dokumentasikan pilihan tersebut di riwayat perubahan.

2. **Prioritaskan ketepatan di atas kecepatan**: Dokumen ini akan menjadi acuan untuk ratusan atau ribuan baris kode yang akan ditulis. Satu aturan yang ambigu dapat menyebabkan inkonsistensi di seluruh codebase.

3. **Uji setiap contoh kode secara mental**: Sebelum menuliskan contoh kode ke dokumen, jalankan secara mental: apakah kode ini bisa dieksekusi tanpa error? Apakah import-nya sudah benar? Apakah tipe datanya konsisten?

4. **Hindari tumpang tindih dengan dokumen lain**: Jika suatu informasi detail sudah ada di dokumen referensi, cukup buat referensi silang (`Ref: [Nama Dokumen] Bab X.Y`) — jangan salin kontennya secara verbatim. Kecuali untuk contoh kode boilerplate yang memang harus ada di sini sebagai panduan langsung.

5. **Gunakan bahasa yang assertif dan imperatif**: Setiap aturan harus terdengar seperti perintah yang jelas, bukan saran yang bisa diabaikan. Contoh yang benar: "Seluruh fungsi publik **WAJIB** memiliki type hints." Contoh yang salah: "Sebaiknya fungsi publik memiliki type hints jika memungkinkan."

6. **Jaga konsistensi format di seluruh dokumen**: Gunakan format yang sama untuk semua elemen serupa. Jika satu aturan menggunakan format `[WAJIB]` di awal kalimat, semua aturan setingkat harus menggunakan format yang sama.

---

*Issue ini dibuat pada: 2026-05-29*
*Dibuat oleh: Antigravity AI Agent*
*Target file: `docs/sdlc/04_implementation/01_coding_standard.md`*
