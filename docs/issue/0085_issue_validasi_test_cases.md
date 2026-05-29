# Validasi, Audit & Penyempurnaan Dokumen Test Cases v1.1

---

**Dokumen Utama** : `docs/sdlc/05_testing/02_test_cases.md`
**Lokasi Referensi** : `docs/sdlc/`
**Versi Saat Ini** : v1.1
**Target Versi** : v1.2
**Prioritas** : High
**Jenis** : Documentation Audit & Revision
**Dibuat** : 2026-05-29

---

## Persona Auditor

Anda adalah **Principal QA Architect & SDLC Documentation Reviewer** dengan kompetensi lintas disiplin:

- **Keahlian Utama**: IEEE 829 (standar dokumentasi pengujian), ISTQB Foundation & Advanced Level, standar ketertelusuran test case industri, dan metodologi QA modern.
- **Domain Bisnis**: Sistem ERP/POS berbasis CLI Python (AbuCom), arsitektur LAN client-server MySQL, kalkulasi keuangan presisi desimal `ROUND_HALF_UP`, dan sistem RBAC multi-peran.
- **Sikap Kerja**: Skeptis dan kritis. Anda tidak menerima asumsi apa pun. Setiap klaim di dalam dokumen **wajib** dapat ditelusuri kembali ke dokumen referensi induknya. Anda memeriksa konsistensi data numerik hingga 4 digit desimal, kelengkapan setiap kolom tabel kasus uji, dan kejelasan bahasa yang bebas dari ambiguitas.
- **Standar Output**: Seluruh hasil perbaikan Anda harus memenuhi kelayakan sebagai **input langsung** bagi tim QA Engineer, AI Testing Agent, dan programmer junior yang akan mengeksekusi test script `pytest` pada fase berikutnya.

---

## Konteks & Latar Belakang Issue

Dokumen `02_test_cases.md` (v1.1) merupakan deliverable kedua pada **Fase 05 — Testing** proyek AbuCom. Dokumen ini menjabarkan **70 kasus uji** operasional yang diturunkan dari **44 skenario uji** pada dokumen `Test Plan v1.1`.

Dokumen ini menjadi **satu-satunya sumber kebenaran** bagi AI Testing Agent dan QA Engineer dalam merancang test suite `pytest` dan menyusun Test Report. Oleh karena itu, kualitas, akurasi, dan kelengkapan dokumen ini bersifat **kritikal** dan tidak boleh menimbulkan pertanyaan atau interupsi saat fase eksekusi pengujian berlangsung.

Issue ini memerintahkan audit menyeluruh dan penulisan ulang penuh dokumen tersebut menjadi versi **v1.2**.

---

## Daftar Dokumen Referensi yang Wajib Dibaca

Sebelum memulai audit, baca dan pahami seluruh dokumen referensi berikut secara lengkap dari baris pertama hingga terakhir:

- [ ] **[R-TP]** `docs/sdlc/05_testing/01_test_plan.md` — Test Plan v1.1 (Sumber induk 44 skenario uji, fixtures global, error mapping, dan spesifikasi lingkungan pengujian)
- [ ] **[R-SRS]** `docs/sdlc/02_analysis/02_software_requirements.md` — SRS v1.1 (Batasan input, logika kalkulasi, aturan validasi, dan parameter data)
- [ ] **[R-UC]** `docs/sdlc/02_analysis/03_use_case_diagram.md` — Use Case Diagram v1.1 (Alur naratif utama, alternatif, dan pengecualian)
- [ ] **[R-ACM]** `docs/sdlc/02_analysis/06_access_control_matrix.md` — Access Control Matrix v1.1 (Hak otorisasi RBAC biner per peran)
- [ ] **[R-SEC]** `docs/sdlc/03_design/06_security_design.md` — Security Design v1.1 (Desain sistem keamanan: bcrypt, JWT, Fernet, RBAC dekorator)
- [ ] **[R-BOM]** `docs/sdlc/03_design/05_bom_hpp_design.md` — BOM & HPP Design v1.1 (Formula kalkulasi HPP, struktur Bill of Material, dan presisi desimal)
- [ ] **[R-CLI]** `docs/sdlc/03_design/04_cli_interaction_flow.md` — CLI Interaction Flow v1.1 (Spesifikasi rendering ANSI rich, breadcrumb navigasi, wrapping thermal)
- [ ] **[R-DB]** `docs/sdlc/03_design/01_database_schema.sql` — Database Schema v1.1 (DDL tabel, constraint, tipe data kolom, dan nama tabel resmi di MySQL)
- [ ] **[R-ERD]** `docs/sdlc/03_design/02_erd_database.md` — ERD Database v1.1 (Relasi antar entitas dan nama kolom resmi)

---

## Instruksi Audit — Tahapan Demi Tahapan

Ikuti setiap checklist di bawah **secara berurutan**. Jangan melompat ke tahap berikutnya sebelum tahap sebelumnya tuntas. Catat seluruh temuan anomali sebelum mulai menulis ulang.

---

### TAHAP 1 — Persiapan & Pembacaan Dokumen

- [ ] **1.1** Buka dan baca `docs/sdlc/05_testing/02_test_cases.md` secara penuh dari baris pertama (header YAML frontmatter) hingga baris terakhir (tabel Referensi Dokumen Bab 21). Jangan lewati satu bagian pun.
- [ ] **1.2** Catat jumlah total kasus uji yang saat ini terdaftar dalam dokumen (berdasarkan Bab 2.1 Ringkasan Cakupan).
- [ ] **1.3** Catat seluruh nama file referensi yang disebutkan secara eksplisit di dalam dokumen (Bab 1.4 dan Bab 21).
- [ ] **1.4** Baca seluruh dokumen referensi yang terdaftar pada bagian **"Daftar Dokumen Referensi"** di atas, satu per satu secara lengkap dan berurutan.

---

### TAHAP 2 — Audit Kelengkapan & Ketertelusuran (Completeness & Traceability Audit)

> **Tujuan**: Memastikan setiap skenario uji dari Test Plan v1.1 telah diturunkan menjadi minimal 1 kasus uji di dokumen ini, tanpa ada gap atau skenario yang terlewat.

- [ ] **2.1** Ekstrak dan catat seluruh **44 ID Skenario Uji** dari `Test Plan v1.1` (misal: M1-TC-001 s.d M10-TC-001, SEC, DEC, INT, CLI, NF). Buat daftar sederhana semua ID tersebut.
- [ ] **2.2** Bandingkan satu per satu setiap ID skenario dari Test Plan dengan kasus uji yang ada di Bab 4 s.d Bab 18 dokumen ini. Pastikan setiap skenario memiliki minimal 1 kasus uji terkait.
- [ ] **2.3** Tandai skenario mana yang:
  - Sudah terwakili dengan cukup lengkap dan granular.
  - Belum terwakili sama sekali (gap / missing test case).
  - Kurang terwakili (hanya ada 1 test case padahal skenario memiliki alur positif, negatif, dan edge case yang berbeda).
- [ ] **2.4** Periksa **Matriks Ketertelusuran Bab 19** secara menyeluruh:
  - [ ] **2.4.1** Pastikan setiap baris di Tabel 19.1 (TC → Skenario Test Plan) **konsisten** dengan ID skenario asal yang benar dari Test Plan v1.1.
  - [ ] **2.4.2** Pastikan setiap baris di Tabel 19.2 (TC → SRS-F) merujuk kode SRS yang benar dan relevan berdasarkan bacaan dokumen SRS v1.1.
  - [ ] **2.4.3** Pastikan setiap baris di Tabel 19.3 (TC → UC) merujuk kode Use Case yang tepat berdasarkan bacaan dokumen Use Case Diagram v1.1.
  - [ ] **2.4.4** Periksa apakah ada kasus uji (TC) yang sudah dibuat di Bab 4–18 **namun tidak terdaftar** di matriks Bab 19, atau sebaliknya.
- [ ] **2.5** Periksa **Tabel 19.4 Kode Error Mapping**: Pastikan setiap kode error (`ERR-XXX-NNN`) yang dipicu dalam langkah uji di seluruh kasus uji sudah terdaftar di tabel ini. Cek apakah ada kode error yang dipakai di body test case tapi tidak ada di tabel 19.4.
- [ ] **2.6** Bandingkan angka statistik di **Bab 19.5 Ringkasan Statistik Cakupan** dengan hitungan aktual Anda. Catat setiap ketidaksesuaian angka untuk diperbaiki saat penulisan ulang.

---

### TAHAP 3 — Audit Relevansi & Fokus Konten (Content Relevance Audit)

> **Tujuan**: Memastikan dokumen ini **hanya** memuat konten yang relevan sebagai Test Case document, tidak mengandung konten yang seharusnya ada di dokumen lain (misal: Test Plan, SRS, atau Design doc).

- [ ] **3.1** Periksa setiap bagian dokumen (Bab 1 s.d Bab 21). Identifikasi apakah ada paragraf, tabel, atau sub-bab yang menduplikasi konten verbatim dari dokumen referensi dan **seharusnya cukup dikutip/dirujuk** saja, bukan disalin mentah-mentah ke sini.
- [ ] **3.2** Periksa apakah ada **informasi desain sistem** (arsitektur database, flow diagram, logika bisnis panjang) yang tidak diperlukan dalam test case document dan seharusnya dihapus atau digantikan dengan referensi singkat ke dokumen sumber.
- [ ] **3.3** Pastikan setiap **Data Uji (Test Data)** pada setiap kasus uji hanya memuat data yang **spesifik dan cukup** untuk menjalankan langkah uji tersebut, tidak lebih. Jika ada data uji yang ambigu, kosong, atau terlalu umum, tandai untuk diperbaiki.
- [ ] **3.4** Periksa apakah **Bab 3 — Lingkungan Pengujian & Prakondisi Global** tidak menduplikasi informasi dari Test Plan v1.1 secara berlebihan. Pastikan bagian ini hanya menyarikan informasi yang relevan secara operasional untuk eksekutor test case, bukan menyalin ulang seluruh bab dari Test Plan.

---

### TAHAP 4 — Audit Struktur Dokumen (Document Structure Audit)

> **Tujuan**: Memastikan struktur dokumen memenuhi standar IEEE 829 dan best practice industri untuk Test Case Specification document.

- [ ] **4.1** Periksa **YAML Frontmatter** (baris 1–8): Pastikan semua field terisi lengkap dan benar:
  - Field `dokumen` berisi nama dokumen yang tepat.
  - Field `proyek` berisi nama proyek yang tepat.
  - Field `versi` berisi nilai `1.1` (akan diperbarui menjadi `1.2` pada tahap penulisan ulang).
  - Field `tanggal` berisi tanggal yang valid.
  - Field `status` berisi nilai yang sesuai.
  - Field `penyusun` berisi nama persona yang sesuai.
- [ ] **4.2** Periksa **Bab 1 — Informasi Dokumen**: Pastikan semua sub-bab standar ada dan informatif:
  - [ ] **4.2.1** Bab 1.1: Tujuan Dokumen — jelas, spesifik, dan menyebut Test Plan v1.1 sebagai dokumen induk.
  - [ ] **4.2.2** Bab 1.2: Cakupan Dokumen — menyebutkan jumlah total TC, modul, dan tipe pengujian yang dicover secara akurat.
  - [ ] **4.2.3** Bab 1.3: Posisi dalam SDLC — diagram alir ASCII jelas menunjukkan posisi dokumen ini antara Test Plan dan Test Scripts.
  - [ ] **4.2.4** Bab 1.4: Hubungan Dokumen SDLC — daftar dokumen input dan output lengkap dengan path file yang valid.
  - [ ] **4.2.5** Bab 1.5: Audiens Target — spesifik dan terdiferensiasi untuk setiap jenis pembaca.
  - [ ] **4.2.6** Bab 1.6: Definisi & Akronim — semua istilah teknis yang digunakan dalam dokumen terdefinisi di sini. Tambahkan istilah yang kurang.
  - [ ] **4.2.7** Bab 1.7: Konvensi Penulisan Test Case — format ID dan skema penamaan jelas, konsisten, dan lengkap contohnya.
- [ ] **4.3** Periksa **Bab 2 — Ringkasan Cakupan**: Pastikan angka di seluruh tabel (Bab 2.1, 2.2, 2.3, 2.4) akurat dan konsisten satu sama lain serta dengan jumlah aktual TC di body dokumen.
- [ ] **4.4** Periksa **Bab 3 — Lingkungan & Prakondisi Global**: Pastikan spesifikasi lingkungan (OS, Python, MySQL, versi), fixtures data uji, Entry Criteria, Exit Criteria, dan dependency map lengkap dan akurat.
- [ ] **4.5** Periksa **Bab 4 s.d Bab 18 (Body Test Cases)**: Untuk setiap kasus uji, pastikan **semua kolom atribut tabel** hadir dan terisi lengkap tanpa ada yang kosong, placeholder tidak valid, atau tidak informatif:
  - [ ] **4.5.1** **ID Kasus Uji** — format konsisten sesuai konvensi Bab 1.7 (`TC-[MODUL]-[SKENARIO]-[URUT]`).
  - [ ] **4.5.2** **Skenario Asal** — merujuk ID skenario yang valid dari Test Plan v1.1.
  - [ ] **4.5.3** **Referensi SRS / UC** — kode SRS dan UC yang spesifik dan valid, bukan perkiraan.
  - [ ] **4.5.4** **Modul / Fitur** — nama modul konsisten dengan penamaan resmi di seluruh dokumen.
  - [ ] **4.5.5** **Tipe / Tingkat / Pri** — menggunakan salah satu nilai valid: Tipe (Functional/Security/Precision/Boundary/Database/CLI/Integrity); Tingkat (Unit/Integration/System); Prioritas (High/Medium/Low).
  - [ ] **4.5.6** **Peran Aktor** — username atau role yang valid sesuai tabel fixtures Bab 3.3 (misal: `kasir`, `pemilik`, `kepala`, dll.).
  - [ ] **4.5.7** **Prakondisi** — kondisi awal yang spesifik, terukur, dan cukup untuk memastikan TC dapat dieksekusi tanpa setup tambahan yang tidak terdokumentasi.
  - [ ] **4.5.8** **Data Uji (Test Data)** — data konkret dengan tipe dan nilai presisi desimal yang benar (bukan nilai estimasi atau placeholder).
  - [ ] **4.5.9** **Langkah Uji** — urutan langkah yang deterministik, tidak ambigu, dan bisa dieksekusi oleh programmer junior tanpa interpretasi.
  - [ ] **4.5.10** **Hasil Diharapkan** — ekspektasi spesifik, terukur, dan verifiable (bukan deskripsi umum yang tidak bisa dikonversi ke assertion pytest).
  - [ ] **4.5.11** **Hasil / Status Uji** — berisi template placeholder standar `*[Diisi saat eksekusi]*` / `*[Diisi saat eksekusi: PASS/FAIL]*`.
  - [ ] **4.5.12** **Catatan Tambahan** — berisi informasi relevan atau tanda `-` jika tidak ada catatan. Tidak boleh dikosongkan tanpa penanda.
- [ ] **4.6** Periksa apakah ada test case yang menggunakan **format ringkas** (bullet list, bukan tabel penuh) yang **seharusnya** diubah ke format tabel standar seperti TC lainnya agar konsisten. Jika ada, konversi ke format tabel standar.
- [ ] **4.7** Periksa **Bab 19 — Matriks Ketertelusuran**: Pastikan semua 5 sub-tabel (19.1, 19.2, 19.3, 19.4, 19.5) ada dan lengkap.
- [ ] **4.8** Periksa **Bab 20 — Lampiran**: Pastikan:
  - Bab 20.1 Glosarium mencakup semua istilah teknis yang muncul di dokumen.
  - Bab 20.2 Data Seed Representatif akurat sesuai DDL Schema dan konsisten dengan data uji di body TC.
  - Bab 20.3 Template Defect Report lengkap dan dapat langsung digunakan.
- [ ] **4.9** Periksa **Bab 21 — Referensi Dokumen**: Pastikan semua dokumen yang dikutip di seluruh body dokumen terdaftar di sini. Pastikan path file dan versi akurat.

---

### TAHAP 5 — Audit Kualitas Data & Akurasi Teknis (Technical Accuracy Audit)

> **Tujuan**: Memverifikasi bahwa setiap nilai numerik, nama fungsi, nama tabel/kolom database, kode error, dan pesan error di dalam dokumen akurat sesuai referensi teknis yang berlaku.

- [ ] **5.1** **Verifikasi Akurasi Kalkulasi Desimal**: Hitung secara manual setiap nilai kalkulasi desimal yang disebutkan dalam Hasil Diharapkan test case:
  - [ ] **5.1.1** `TC-M2-002-01`: HPP BOM = `0.0025 × 100000.0000 + 1.0000 × 4500.0000` → harus = `Decimal('4750.0000')`.
  - [ ] **5.1.2** `TC-M2-003-01`: Kerugian limbah = `0.0005 × 100000.0000` → harus = `Rp 50,0000`.
  - [ ] **5.1.3** `TC-M6-002-01`: Depresiasi bulanan = `10000000.0000 / 60` → harus = `Decimal('166666.6667')` dengan pembulatan `ROUND_HALF_UP`.
  - [ ] **5.1.4** `TC-DEC-003-01`: Saldo akhir = `500000.0000 + 1523.1234 + 2456.8766 + 3000.0000` → harus = `Decimal('506980.0000')`.
  - [ ] **5.1.5** `TC-DEC-004-01`: Sisa stok = `1.0000 - 0.0125` → harus = `Decimal('0.9875')`.
  - [ ] **5.1.6** `TC-M1-006-01`: Margin % = `(10000.0000 - 7500.0000) / 10000.0000 × 100` → harus = `Decimal('25.0000')`.
  - [ ] **5.1.7** `TC-M4-002-01` dan `TC-M4-003-01`: Verifikasi semua nilai kalkulasi payroll dan UMR dengan mengacu ke SRS v1.1.
  - [ ] **5.1.8** Periksa TC lain yang mengandung kalkulasi numerik dan belum tercantum di atas. Verifikasi masing-masing.
- [ ] **5.2** **Verifikasi Nama Tabel & Kolom Database**: Bandingkan setiap nama tabel (misal: `transaksi`, `barang`, `audit_logs`, `utang_usaha`, `pinjaman_cicilan`, `antrian_desain`, `handover_logs`, dll.) dan nama kolom (misal: `cabang_id`, `locked_until`, `old_value`, `new_value`, `failed_login_attempts`, dll.) yang disebutkan di dalam Langkah Uji dan Hasil Diharapkan dengan **DDL resmi** di `docs/sdlc/03_design/01_database_schema.sql`. Tandai dan catat setiap ketidaksesuaian nama untuk diperbaiki.
- [ ] **5.3** **Verifikasi Kode Error & Pesan Error**: Pastikan setiap kode error (`ERR-AUTH-001`, `ERR-DB-001`, dll.) dan string pesan error yang tepat konsisten dengan error mapping yang terdapat di `Test Plan v1.1` dan `Security Design v1.1`. Perbaiki jika ada pesan yang salah ejaan, tidak konsisten, atau berbeda antara TC dan tabel 19.4.
- [ ] **5.4** **Verifikasi Nama Fungsi Python**: Periksa setiap nama fungsi yang dipanggil dalam Langkah Uji (misal: `hitung_harga_jual(...)`, `kalkulasi_hpp_bom(...)`, `hitung_depresiasi_bulanan(...)`, `generate_wa_link(...)`, `rekomendasi_admin_terhemat(...)`, `format_struk_thermal(...)`, `pembulatan_presisi(...)`, dll.). Pastikan nama fungsi, parameter, dan tipe data argumen konsisten dengan yang dispesifikasikan di SRS v1.1 atau dokumen desain terkait.
- [ ] **5.5** **Verifikasi Data Fixtures**: Pastikan seluruh data uji (test data) yang merujuk fixtures awal (misal: `barang_id = 1`, `supplier_id = 1`, username `kasir01`, dll.) konsisten dengan data seed yang terdefinisi di **Bab 3.3 Data Uji Global** dan **Bab 20.2 Contoh Data Seed** dalam dokumen ini, serta konsisten dengan skema database resmi.
- [ ] **5.6** **Verifikasi Peran Aktor RBAC**: Bandingkan setiap nilai `Peran Aktor` dalam setiap TC dengan **Access Control Matrix v1.1**. Pastikan aktor yang dipilih dalam setiap TC memiliki **hak akses yang valid dan sesuai** untuk modul dan fitur yang sedang diuji. Tandai jika ada TC yang menggunakan aktor dengan peran yang salah atau tidak memiliki otorisasi yang diuji.
- [ ] **5.7** **Verifikasi Dependency Map (Bab 3.5)**: Periksa apakah diagram Mermaid dependency sudah mencakup semua TC yang memiliki dependensi urutan eksekusi kritis. Tambahkan node jika ada TC yang seharusnya masuk ke dalam diagram namun belum ada.
- [ ] **5.8** **Verifikasi Konsistensi Judul Bab dengan Isi**: Pastikan judul setiap sub-bab TC (misal: "TC-M1-001: Input transaksi penjualan multi-divisi cepat") secara akurat mencerminkan isi TC di dalamnya dan konsisten dengan nama skenario di Test Plan v1.1.

---

### TAHAP 6 — Audit Kelayakan Sebagai Referensi Fase SDLC Berikutnya

> **Tujuan**: Memastikan dokumen ini cukup lengkap dan akurat untuk dijadikan input langsung bagi pembuatan Test Scripts (pytest) dan Test Report tanpa memerlukan klarifikasi tambahan.

- [ ] **6.1** Periksa setiap **Langkah Uji** (kolom ke-9): Apakah langkah-langkah tersebut cukup deterministik dan operasional sehingga QA Engineer atau AI Testing Agent dapat langsung menerjemahkannya menjadi kode `pytest` **tanpa interpretasi atau asumsi tambahan**?
  - Jika ada langkah yang ambigu (misal: "Jalankan kalkulasi" tanpa menyebut nama fungsi spesifik), perbaiki menjadi instruksi konkret dengan nama fungsi dan argumen yang lengkap.
  - Jika ada langkah yang bergantung pada state global yang tidak terdefinisi di Prakondisi, tambahkan ke Prakondisi.
- [ ] **6.2** Periksa setiap **Hasil Diharapkan** (kolom ke-10): Apakah ekspektasi cukup spesifik dan terukur untuk dikonversi menjadi assertion `assert` dalam kode `pytest`?
  - **Contoh tidak cukup baik** (hindari): "Sistem menampilkan pesan error." (terlalu umum, tidak bisa di-assert)
  - **Contoh cukup baik** (gunakan): "Menampilkan visual error: `⛔ ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!`" (spesifik dan verifiable)
  - Perbaiki semua Hasil Diharapkan yang tidak cukup spesifik.
- [ ] **6.3** Periksa apakah setiap **TC yang mereferensikan TC lain** (menggunakan frasa "Rujuk detail pada TC-XX-YYY") masih menyertakan informasi minimal yang cukup (Aktor, Prakondisi, Data Uji, Expected Result ringkas) agar TC tersebut tidak menyebabkan kebingungan saat eksekusi mandiri.
- [ ] **6.4** Periksa apakah ada **celah pengujian (test coverage gap)** yang kritis — yaitu fitur atau aturan bisnis penting yang disebutkan di SRS atau Test Plan namun **tidak ada satu pun TC yang mengujinya**. Jika ditemukan, tambahkan TC baru yang mengisi gap tersebut dengan format tabel standar lengkap.

---

### TAHAP 7 — Audit Kualitas Bahasa Indonesia (Language Quality Audit)

> **Tujuan**: Memastikan seluruh teks menggunakan Bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh programmer junior atau LLM model AI yang lebih murah.

- [ ] **7.1** Baca ulang seluruh teks narasi (paragraf, bullet point, isi kolom tabel) dari Bab 1 hingga Bab 21. Identifikasi dan catat kalimat yang:
  - Terlalu panjang dan berpotensi menimbulkan salah baca (lebih dari 40 kata per kalimat).
  - Menggunakan kata teknis asing tanpa penjelasan di glosarium Bab 20.1.
  - Menggunakan istilah yang tidak konsisten untuk menyebut hal yang sama (misal: "kasus uji" vs "test case" vs "skenario" digunakan secara acak tanpa pola yang jelas).
  - Mengandung kalimat pasif ganda yang sulit diparsing oleh pembaca non-senior.
- [ ] **7.2** Periksa dan terapkan konsistensi penulisan istilah teknis di seluruh dokumen:
  - Nama fungsi Python: selalu dalam `backtick` (misal: `hitung_hpp_bom()`).
  - Nama tabel DB: selalu dalam `backtick` (misal: `transaksi`, `barang`).
  - Kode error: selalu dalam format `ERR-XXX-NNN` dan `backtick`.
  - Nilai desimal: selalu dalam format `Decimal('X.XXXX')` untuk nilai uji, atau format rupiah `Rp X.XXX,XXXX` untuk narasi.
  - Nama peran/role: selalu dalam `backtick` (misal: `kasir`, `pemilik`, `kepala`).
  - Username: selalu dalam `backtick` (misal: `kasir01`, `gudang01`).
- [ ] **7.3** Periksa apakah judul setiap sub-bab (Bab 4.1, 4.2, dst.) cukup informatif dan mencerminkan isi TC yang ada di dalamnya dengan tepat.
- [ ] **7.4** Periksa **Langkah Uji** setiap TC: apakah urutan langkah ditulis dengan kata kerja imperatif yang jelas dan standar (misal: Masuk, Input, Klik, Jalankan, Verifikasi, Pilih, Simpan, Logout) dan tidak mengandung kata kerja ambigu di awal instruksi.

---

### TAHAP 8 — Audit Data Kosong & Placeholder (Empty Data Audit)

> **Tujuan**: Memastikan tidak ada kolom, field, atau bagian yang dibiarkan kosong, mengandung placeholder yang belum diisi, atau mengandung nilai tidak valid.

- [ ] **8.1** Periksa seluruh kolom `Catatan Tambahan` pada setiap TC: Harus berisi informasi relevan (dependensi, referensi, keterangan teknis) **atau** diisi dengan tanda `-` secara eksplisit. Tidak boleh dikosongkan tanpa penanda.
- [ ] **8.2** Periksa seluruh kolom `Hasil / Status Uji` pada setiap TC: Harus berisi template standar `*[Diisi saat eksekusi]*` / `*[Diisi saat eksekusi: PASS/FAIL]*` secara konsisten di semua TC tanpa variasi format.
- [ ] **8.3** Periksa apakah ada baris di **Matriks Ketertelusuran Bab 19** yang memiliki sel kosong atau nilai `N/A` tanpa penjelasan. Isi atau perbaiki setiap baris yang tidak lengkap.
- [ ] **8.4** Periksa **Bab 20.2 (Data Seed)**: Pastikan contoh data representatif yang disajikan **konsisten secara numerik** dengan data yang digunakan di dalam TC (misal: `barang_id = 1` di `TC-M1-001-01` harus berkorespondensi dengan `id = 1` di tabel seed dengan nilai stok dan harga yang sama).
- [ ] **8.5** Periksa **kolom `Status`** di seluruh tabel Bab 19: Pastikan semua baris memiliki nilai `Cocok` atau `Sesuai`, bukan dikosongkan atau diisi nilai tidak valid.
- [ ] **8.6** Periksa apakah ada nilai kalkulasi numerik dalam Hasil Diharapkan yang masih mengandung kata "misal", "kira-kira", atau nilai placeholder yang belum dihitung secara aktual. Ganti dengan nilai kalkulasi yang benar dan presisi.

---

### TAHAP 9 — Audit Tambahan Spesifik Test Case Document

> **Instruksi tambahan yang relevan khusus untuk dokumen bertipe Test Case Specification.**

- [ ] **9.1** **Verifikasi Isolasi Test Case**: Pastikan setiap TC dapat dieksekusi secara mandiri tanpa merusak state untuk TC lain. Jika memang ada dependensi eksekusi, pastikan dependensi tersebut **sudah terdokumentasi secara eksplisit** di kolom Catatan Tambahan dan/atau di Bab 3.5 Dependency Map.
- [ ] **9.2** **Verifikasi Boundary Value Analysis**: Periksa kasus uji bertipe `Boundary`. Pastikan nilai batas bawah, batas atas, dan tepat-di-batas (`on-boundary`, `off-boundary`) sudah tercakup secara eksplisit dalam Data Uji dan Langkah Uji. Tambahkan kasus uji boundary yang masih kurang jika ditemukan.
- [ ] **9.3** **Verifikasi Negative Testing Coverage**: Periksa setiap modul (M.1 s.d M.10). Pastikan setiap fungsi bisnis utama memiliki minimal 1 kasus uji negatif (unhappy path) yang menguji skenario input tidak valid, otorisasi gagal, atau kegagalan sistem.
- [ ] **9.4** **Verifikasi Konsistensi ID Penomoran TC**: Pastikan semua ID kasus uji (`TC-M1-001-01`, `TC-SEC-003-01`, dll.) mengikuti **konvensi penulisan Bab 1.7** secara konsisten tanpa ada format yang menyimpang (misal: menggunakan dua digit skenario alih-alih tiga digit, atau ada gap dalam penomoran URUT yang tidak dijelaskan).
- [ ] **9.5** **Verifikasi Sinkronisasi Ringkasan (Bab 2)**: Setelah semua penambahan/penghapusan TC selesai dianalisis, hitung ulang total per modul (Bab 2.1), per tipe (Bab 2.2), per prioritas (Bab 2.3), dan per tingkat pengujian (Bab 2.4). Catat angka-angka baru yang akurat untuk diterapkan saat penulisan ulang.
- [ ] **9.6** **Periksa Skenario Edge Case Khusus Sistem AbuCom**: Sistem AbuCom memiliki karakteristik khusus berikut yang perlu mendapat perhatian ekstra:
  - [ ] **9.6.1** **Presisi Desimal**: Pastikan setiap kalkulasi keuangan diuji dengan nilai desimal non-integer (bukan hanya bilangan bulat) untuk membuktikan tidak ada floating-point drift di Python.
  - [ ] **9.6.2** **RBAC Multi-Peran**: Pastikan ada TC yang menguji bahwa setiap tindakan kritis (pembatalan, approval, eskalasi sandi) **hanya** bisa dilakukan oleh peran yang berwenang, dan peran lain benar-benar diblokir.
  - [ ] **9.6.3** **Transaksi ACID**: Pastikan ada TC yang menguji atomisitas transaksi database (rollback total jika terjadi kegagalan di tengah proses multi-langkah yang melibatkan lebih dari 1 tabel).
  - [ ] **9.6.4** **Sesi JWT Stateless**: Pastikan ada TC yang menguji masa berlaku token (expiry setelah 28.800 detik / 8 jam) dan pemblokiran akses total pasca-expiry.
  - [ ] **9.6.5** **Rendering CLI ANSI**: Pastikan ada TC yang memverifikasi bahwa output visual ANSI (warna, box-drawing, breadcrumb) dirender dengan benar pada kedua OS target (Windows 11 dan Debian 12) tanpa mojibake.
- [ ] **9.7** **Periksa Konsistensi Antar-TC dalam Modul yang Sama**: Pastikan TC yang berada dalam modul yang sama menggunakan data fixtures yang konsisten (misal: `barang_id` yang sama harus merujuk barang yang sama di semua TC M.2). Inconsistency antar TC dalam modul yang sama dapat menyebabkan konflik saat eksekusi sequential test suite.

---

### TAHAP 10 — Penulisan Ulang & Overwrite Dokumen

> ⚠️ **PERINGATAN KRITIS**: Tahap ini adalah tahap penulisan akhir. Eksekusi hanya setelah Tahap 1 s.d 9 selesai sepenuhnya dan seluruh temuan telah dianalisis dan dicatat. Jangan memulai penulisan ulang jika masih ada tahap audit yang belum selesai.

- [ ] **10.1** Gabungkan seluruh temuan dari Tahap 2 s.d 9 menjadi satu daftar perubahan terstruktur sebelum mulai menulis.
- [ ] **10.2** Buka file target `docs/sdlc/05_testing/02_test_cases.md` dan siapkan untuk ditimpa (overwrite penuh).
- [ ] **10.3** Tulis ulang **seluruh dokumen dari baris pertama hingga baris terakhir** dengan menerapkan semua perbaikan yang ditemukan. Aturan penulisan ulang yang wajib dipatuhi:

  **MUTLAK DILARANG:**
  - ❌ Memotong, meringkas, atau menghilangkan bagian mana pun dari dokumen asli yang sudah benar.
  - ❌ Mengganti konten dengan placeholder seperti `[lanjutan...]`, `[isi sebelumnya tetap]`, `[dst.]`, `[omitted for brevity]`, atau bentuk pemendekan apa pun.
  - ❌ Melewati bab, sub-bab, atau TC mana pun meskipun tidak ada perubahan pada bagian tersebut.
  - ❌ Menulis hanya sebagian dokumen dan berhenti di tengah-tengah.
  - ❌ Menggunakan komentar seperti "bagian ini tidak berubah" sebagai pengganti konten.

  **WAJIB DILAKUKAN:**
  - ✅ Tulis ulang setiap baris — dari YAML frontmatter baris 1 hingga baris terakhir tabel Referensi (Bab 21).
  - ✅ Perbarui nilai `versi` di YAML frontmatter dari `1.1` menjadi `1.2`.
  - ✅ Perbarui nilai `tanggal` di YAML frontmatter ke tanggal eksekusi audit ini.
  - ✅ Tambahkan baris baru di **Tabel Riwayat Perubahan Dokumen** yang mencatat perubahan versi `1.2` secara ringkas namun informatif (sebutkan perubahan utama apa yang dilakukan).
  - ✅ Perbarui seluruh angka statistik di Bab 2 sesuai hitungan aktual TC final setelah semua perubahan diterapkan.
  - ✅ Terapkan semua koreksi teknis, tambahan TC baru, dan perbaikan bahasa Indonesia yang ditemukan di Tahap 2–9.

- [ ] **10.4** Setelah penulisan ulang selesai, hitung jumlah baris total file output. Jika jumlah baris output **lebih sedikit lebih dari 10%** dari file asli tanpa justifikasi penghapusan konten yang jelas, ulangi penulisan ulang dengan lebih lengkap.
- [ ] **10.5** Lakukan **self-review akhir**: Baca ulang dokumen hasil penulisan ulang secara menyeluruh. Verifikasi minimal setiap judul bab dari Bab 1 s.d Bab 21, dan pilih minimal 5 TC secara acak dari modul berbeda untuk diperiksa kelengkapan kolomnya.

---

### TAHAP 11 — Pembaruan Referensi Dokumen (Bab 21)

- [ ] **11.1** Setelah penulisan ulang selesai, tinjau kembali **Bab 21 — Referensi Dokumen** dalam file yang baru ditulis.
- [ ] **11.2** Jika selama proses audit ditemukan bahwa ada dokumen referensi **baru yang dikutip atau dirujuk** di dalam tubuh dokumen namun belum terdaftar di Bab 21, tambahkan dokumen tersebut sebagai baris baru di tabel referensi di bagian **paling bawah** tabel, dengan format kolom yang konsisten:

  ```
  | [No urut baru] | [Kode Ref baru] | [Nama Dokumen Lengkap] | [path/file.md] | [Versi] |
  ```

- [ ] **11.3** Pastikan seluruh path file yang terdaftar di Bab 21 **valid dan dapat diakses** (tidak ada path yang salah tulis atau merujuk file yang tidak ada).
- [ ] **11.4** Verifikasi bahwa nomor urut referensi (kolom `No`) berurutan tanpa gap setelah penambahan baris baru.

---

## Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **SELESAI** jika dan hanya jika seluruh kondisi berikut terpenuhi:

| # | Kriteria | Status |
|---|---|:---:|
| 1 | Seluruh 44 skenario uji dari Test Plan v1.1 terwakili minimal 1 TC di dokumen | `[ ]` |
| 2 | Seluruh kolom tabel TC terisi lengkap tanpa placeholder kosong yang tidak valid | `[ ]` |
| 3 | Semua kalkulasi desimal di Hasil Diharapkan telah diverifikasi akurat secara manual | `[ ]` |
| 4 | Semua nama tabel/kolom DB konsisten dengan DDL Schema resmi | `[ ]` |
| 5 | Semua kode error dan pesan error konsisten dengan error mapping di Test Plan v1.1 | `[ ]` |
| 6 | Matriks ketertelusuran Bab 19 (semua 5 sub-tabel) lengkap dan konsisten | `[ ]` |
| 7 | Angka statistik Bab 2 dan Bab 19.5 akurat dengan hitungan TC aktual | `[ ]` |
| 8 | Bahasa Indonesia di seluruh dokumen natural, tidak ambigu, dan konsisten | `[ ]` |
| 9 | Dokumen telah ditulis ulang penuh ke file target tanpa truncation | `[ ]` |
| 10 | Versi dokumen telah diperbarui menjadi v1.2 di frontmatter dan riwayat perubahan | `[ ]` |
| 11 | Referensi baru (jika ada) telah ditambahkan di Bab 21 baris paling bawah | `[ ]` |

---

## Catatan Teknis untuk Eksekutor

1. **Jangan berasumsi**: Jika ragu terhadap kebenaran suatu nilai atau nama, selalu cek ke dokumen referensi yang sesuai. Lebih baik lambat tapi akurat daripada cepat tapi salah.
2. **Pecah pekerjaan besar**: Jika batas konteks (context window) Anda terbatas, kerjakan satu modul (misal: satu bab/section) dalam satu sesi, lalu gabungkan di akhir. Jangan coba tulis seluruh dokumen dalam satu prompt jika kapasitas tidak memungkinkan — kerjakan per bagian lalu overwrite secara bertahap.
3. **Prioritaskan TC High**: Jika terpaksa harus memilih, pastikan kasus uji bertipe `High` dan `Security` adalah yang pertama dipastikan lengkap dan akurat sebelum yang lain.
4. **Simpan temuan anomali**: Sebelum menulis ulang, simpan catatan temuan anomali Anda (bisa dalam format scratch pad atau komentar internal) agar tidak ada temuan yang terlupakan saat tahap penulisan ulang.
5. **Hindari hallusinasi**: Jangan mengarang nama tabel, nama fungsi, nilai numerik, atau kode error yang tidak dapat Anda temukan di dokumen referensi. Jika tidak ditemukan di referensi mana pun, tandai dengan `[PERLU VERIFIKASI MANUAL]` dan lanjutkan ke item berikutnya.
6. **Verifikasi sinkronisasi data**: Setiap kali Anda menambahkan atau mengubah TC, pastikan perubahan tersebut juga tercermin di Bab 2 (Ringkasan Cakupan), Bab 19 (Matriks Ketertelusuran), dan Bab 20.2 (Data Seed) jika relevan.
