---
issue_id   : 0048
judul      : Validasi, Analisis, dan Penyempurnaan Dokumen UAT Script
target_file: docs/sdlc/05_testing/03_uat_script.md
dibuat_oleh: Senior UAT Analyst & Business Acceptance Specialist
tanggal    : 2026-05-26
status     : Open
prioritas  : High
---

# Issue 0048 — Validasi, Analisis, dan Penyempurnaan Dokumen UAT Script

## 1. Latar Belakang dan Tujuan Issue

Dokumen **UAT Script** (`docs/sdlc/05_testing/03_uat_script.md`) adalah dokumen eksekusi fase pengujian penerimaan pengguna (*User Acceptance Testing*) dari proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**. Dokumen ini memiliki peran kritis sebagai gerbang formal (*go/no-go gate*) sebelum sistem diizinkan masuk ke lingkungan produksi (*go-live*).

Issue ini dibuat untuk menugaskan sebuah siklus **validasi mendalam dan komprehensif** terhadap dokumen tersebut, memastikan bahwa setiap butir isi dokumen—dari kelengkapan data, keselarasan referensi, standar struktur industri, hingga kualitas bahasa—sudah memenuhi standar kualitas tinggi sebelum dokumen ini digunakan sebagai acuan tahapan SDLC berikutnya.

---

## 2. Persona yang Harus Digunakan

> **INSTRUKSI WAJIB:** Sebelum melakukan pekerjaan apa pun, implementor harus **mengadopsi dan mempertahankan persona berikut secara penuh** sepanjang seluruh proses validasi ini.

Implementor wajib berperan sebagai:

> **"Senior UAT Engineer & Software Quality Assurance Lead"** dengan keahlian mendalam di:
> - **IEEE 829 / ISO/IEC 29119** (standar dokumentasi pengujian perangkat lunak internasional)
> - **ISTQB CTAL-TAE** (International Software Testing Qualifications Board — Test Analyst Expert)
> - Validasi dokumen UAT berbasis bisnis untuk sistem POS/kasir, inventaris, dan manajemen usaha kecil-menengah
> - Analisis kritis konsistensi antara dokumen Test Plan, Test Cases, SRS, Use Cases, dan UAT Script
> - Audit kualitas bahasa teknis Indonesia: natural, tidak ambigu, tidak berputar-putar, langsung ke inti
> - Deteksi gap, inkonsistensi, redundansi, data kosong/placeholder, dan potensi halusinasi AI pada dokumen teknis panjang
> - Pemeriksaan presisi kalkulasi desimal keuangan (`Decimal(15,4)`, `ROUND_HALF_UP`) dalam konteks UAT
> - Penilaian kesiapan dokumen sebagai input yang berkualitas tinggi untuk fase SDLC berikutnya (UAT Execution & Test Report, Deployment/Release Document)

---

## 3. Dokumen Target dan Referensi

### 3.1. Dokumen Target (Utama — Subjek Validasi)

| Keterangan | Detail |
|---|---|
| **Nama Dokumen** | UAT Script |
| **Path File Target** | `docs/sdlc/05_testing/03_uat_script.md` |
| **Versi Saat Ini** | v1.0 |
| **Versi Setelah Revisi** | v1.1 |
| **Baris Total (estimasi)** | ±1.407 baris |

### 3.2. Dokumen Referensi yang Harus Dibaca dan Dikomparasi

Seluruh file referensi berikut **WAJIB dibaca terlebih dahulu** sebelum memulai proses validasi:

| No | Kode | Nama Dokumen | Path File |
|----|------|--------------|-----------|
| 1 | R-TP | Test Plan v1.1 | `docs/sdlc/05_testing/01_test_plan.md` |
| 2 | R-TC | Test Cases v1.1 | `docs/sdlc/05_testing/02_test_cases.md` |
| 3 | R-SRS | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| 4 | R-UC | Use Case Diagram v1.1 | `docs/sdlc/02_analysis/03_use_case_diagram.md` |
| 5 | R-ACM | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` |
| 6 | R-CLI | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` |
| 7 | R-BOM | BOM & HPP Design v1.1 | `docs/sdlc/03_design/05_bom_hpp_design.md` |
| 8 | R-SEC | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` |
| 9 | R-WF | Workflow Diagram v1.1 | `docs/sdlc/02_analysis/04_workflow_diagram.md` |

---

## 4. Kriteria dan Dimensi Validasi

Validasi harus dilakukan secara **menyeluruh** terhadap **10 dimensi** berikut. Setiap dimensi harus diperiksa satu per satu secara sistematis.

### Dimensi 1 — Komparasi Mendalam dengan Seluruh Referensi

Lakukan komparasi mendalam antara **dokumen target** dengan **seluruh 9 file referensi** yang tercantum di Bab 3.2. Periksa apakah:

- [ ] Setiap ID skenario asal yang tertulis di UAT Script (misal `M7-TC-001`, `M1-TC-002`) **ada dan konsisten** dengan yang didefinisikan di Test Plan (R-TP) dan Test Cases (R-TC).
- [ ] Setiap kode Test Case yang dirujuk (misal `TC-M7-001-01`) **ada dan sama persis** dengan yang didefinisikan di Test Cases (R-TC).
- [ ] Setiap kode SRS yang dirujuk (misal `SRS-F-030`) **ada dan sesuai** dengan yang didefinisikan di SRS (R-SRS).
- [ ] Setiap kode Use Case yang dirujuk (misal `UC-041`) **ada dan sesuai** dengan yang didefinisikan di Use Case Diagram (R-UC).
- [ ] Setiap peran/role yang disebutkan (misal `kasir`, `desainer`, `pemilik`, `kepala_percetakan`) **konsisten** dengan daftar 8 peran di Access Control Matrix (R-ACM).
- [ ] Kode error yang disebutkan (misal `ERR-SESSION-002`, `ERR-AUTH-003`, `ERR-VAL-007`) **ada dan konsisten** dengan katalog error di CLI Interaction Flow (R-CLI).
- [ ] Formula kalkulasi HPP BOM yang disebutkan (misal `HPP = Σ(Pemakaian × Harga Beli)`) **sesuai** dengan spesifikasi di BOM & HPP Design (R-BOM).
- [ ] Spesifikasi keamanan yang disebutkan (bcrypt cost factor 12, JWT 8 jam = 28.800 detik, Fernet enkripsi, AES-256, brute-force lockout 5x → 10 menit) **konsisten** dengan Security Design (R-SEC).
- [ ] Alur diagram mermaid E2E (UAT-E2E-001, 12 langkah) **konsisten** dengan Workflow Diagram (R-WF) dan urutan operasional bisnis harian toko percetakan.
- [ ] Spesifikasi navigasi CLI (breadcrumb `Dashboard > Inventaris > Opname`, input `0` = mundur, format kode error visual `⛔`) **sesuai** dengan CLI Interaction Flow (R-CLI).

### Dimensi 2 — Kelengkapan Data (Tidak Ada yang Terlewat)

Periksa apakah dokumen target **sudah merangkum semua data dan informasi yang relevan** dari file referensi. Tidak boleh ada data penting yang harusnya ada tapi tidak ada:

- [ ] Verifikasi bahwa **44 skrip UAT individual** (UAT-001 s.d. UAT-044) semuanya terdokumentasi secara lengkap, tidak ada yang hilang atau kosong tanpa konten.
- [ ] Verifikasi bahwa **1 skrip E2E** (UAT-E2E-001) memiliki 12 langkah simulasi hari operasional yang lengkap, termasuk referensi silang ke UAT individual yang relevan.
- [ ] Verifikasi bahwa **3 skrip non-fungsional** (UAT-NF-001, UAT-NF-002, UAT-NF-003) terdokumentasi dengan kriteria kelulusan yang terukur.
- [ ] Verifikasi bahwa seluruh **10 modul** (M.1 s.d. M.10) yang disebut di Bab 2.2 tercakup minimal oleh satu skrip UAT.
- [ ] Verifikasi bahwa setiap baris di **Matriks Ketertelusuran** (Bab 18.3) sudah terisi lengkap — tidak ada sel kosong pada kolom ID UAT, Test Case Terkait, Referensi SRS, Referensi Use Case, dan Modul/Sesi.
- [ ] Verifikasi bahwa **8 akun uji** (Test Fixtures, Bab 18.2) terisi lengkap dengan username, peran, dan deskripsi wewenang untuk semua 8 baris.
- [ ] Verifikasi bahwa **Checklist Kesiapan UAT** (Bab 4) sudah mencakup semua prasyarat teknis (hardware, runtime, database, data seed, dokumen acuan) yang disebutkan di Test Plan.
- [ ] Verifikasi bahwa setiap skrip UAT individual memiliki semua atribut tabel wajib: ID Skrip, Judul, Skenario Asal, Test Case Terkait, Referensi SRS/UC, Modul/Fitur, Aktor Penguji, Lingkungan, Prasyarat, Data Uji, Langkah Pengujian, Hasil Diharapkan, Hasil Aktual, Status, Catatan Temuan, dan Tanda Tangan Penguji.
- [ ] Periksa apakah ada skenario UAT yang **belum terdokumentasi** dari 44 skenario induk di Test Plan — identifikasi gap dan tambahkan jika ada yang kurang.

### Dimensi 3 — Kebersihan Konten (Hanya Data yang Relevan)

Periksa apakah dokumen target **hanya berisi data dan informasi yang spesifik dan memang perlu ada** dalam sebuah UAT Script:

- [ ] Pastikan dokumen ini **tidak memuat** detail teknis implementasi kode yang seharusnya hanya ada di dokumen desain (misal: query SQL detail, kode Python internal, skema tabel database lengkap).
- [ ] Pastikan dokumen ini **tidak menduplikasi** secara penuh konten Test Cases (R-TC) — UAT Script harus menerjemahkan langkah teknis menjadi instruksi berbahasa bisnis, bukan menyalin ulang test cases secara identik.
- [ ] Pastikan bagian **Out-of-Scope** (Bab 2.3) tidak terlalu luas hingga meng-exclude skenario yang seharusnya diuji dalam UAT.
- [ ] Pastikan **Glosarium** (Bab 18.1) hanya mendefinisikan istilah yang benar-benar digunakan dalam dokumen ini dan tidak mendefinisikan istilah teknis yang lebih cocok ada di dokumen desain atau SRS.
- [ ] Pastikan setiap **Data Uji** pada tiap skrip UAT berisi nilai konkret dan spesifik (bukan hanya `[placeholder]`), terukur, dan deterministik — tidak ambigu untuk dieksekusi ulang oleh penguji berbeda.
- [ ] Pastikan **Langkah Pengujian** pada tiap skrip UAT ditulis dari perspektif **pengguna bisnis** (Pemilik Usaha / Kepala Percetakan), bukan perspektif programmer — langkah harus berupa aksi yang dapat dilakukan di UI CLI tanpa memerlukan pengetahuan coding.

### Dimensi 4 — Standar Struktur Dokumen Industri

Periksa apakah dokumen ini memiliki **struktur yang sesuai standar industri dokumen UAT** (IEEE 829, ISO/IEC 29119-3):

- [ ] Periksa apakah ada **header dokumen** (front matter) yang memuat: nama dokumen, proyek, versi, tanggal, status, penyusun.
- [ ] Periksa apakah ada **riwayat perubahan dokumen** (change log) yang terisi lengkap.
- [ ] Periksa apakah ada bab **Informasi Dokumen** yang mencakup: tujuan, cakupan, posisi dalam SDLC, hubungan input/output, audiens target, definisi/akronim.
- [ ] Periksa apakah ada bab **Lingkup dan Tujuan UAT** yang mencakup: tujuan pengujian, cakupan modul, out-of-scope, dan kriteria keberhasilan keseluruhan.
- [ ] Periksa apakah ada bab **Organisasi dan Peran** yang mendefinisikan tim UAT dan jadwal pelaksanaan.
- [ ] Periksa apakah ada bab **Prasyarat dan Kesiapan UAT** (UAT Readiness Checklist) dengan entry criteria yang terukur.
- [ ] Periksa apakah setiap sesi UAT memiliki header sesi yang jelas (aktor utama, lingkungan pengujian).
- [ ] Periksa apakah ada bab **Pengujian Non-Fungsional** yang terpisah dari pengujian fungsional.
- [ ] Periksa apakah ada bab **Prosedur Defect Handling** dengan: klasifikasi keparahan (Blocker/Critical/Major/Minor/Cosmetic), template pencatatan bug, SLA perbaikan, prosedur eskalasi, dan kriteria masuk rilis.
- [ ] Periksa apakah ada bab **Exit Criteria dan Sign-Off** dengan kriteria terukur dan formulir persetujuan go-live yang formal.
- [ ] Periksa apakah ada **Lampiran** yang memuat: glosarium, data fixtures/test accounts, dan matriks ketertelusuran dua arah.
- [ ] Periksa apakah ada bab **Referensi Dokumen** di bagian akhir yang mendaftar semua file referensi dengan path, versi, dan kode referensi.

### Dimensi 5 — Kualitas sebagai Input SDLC Berikutnya

Periksa apakah dokumen ini **layak dijadikan acuan dan input berkualitas** untuk dokumen-dokumen pada fase SDLC berikutnya:

- [ ] **Untuk UAT Execution & Test Report:** Pastikan setiap skrip UAT memiliki kolom `Hasil Aktual`, `Status (PASS/FAIL)`, dan `Catatan Temuan` yang siap diisi saat eksekusi — tidak ada kolom yang hilang.
- [ ] **Untuk UAT Execution & Test Report:** Pastikan `Kriteria Keluar UAT` (Exit Criteria, Bab 17.1) cukup spesifik dan terukur secara kuantitatif sehingga bisa langsung dijadikan tolok ukur pelaporan hasil.
- [ ] **Untuk Deployment/Release Document:** Pastikan `Formulir Tanda Tangan Persetujuan Go-Live` (Bab 17.3) memuat semua field yang diperlukan: lokasi, tanggal, keputusan formal (diterima/ditolak), nama dan tanda tangan Pemilik Usaha dan Kepala Percetakan.
- [ ] **Untuk Training Manual:** Pastikan Langkah Pengujian pada skrip UAT cukup deskriptif sebagai panduan operasional bisnis, sehingga bisa menjadi bahan pelatihan karyawan baru.
- [ ] **Untuk semua dokumen downstream:** Pastikan Matriks Ketertelusuran dua arah (Bab 18.3) cukup lengkap sehingga bisa langsung dipakai untuk memetakan status pengujian ke ID SRS dan Use Case yang relevan.
- [ ] Pastikan tidak ada **pernyataan ambigu** atau **kriteria subjektif** dalam Hasil Diharapkan (misal: "tampilan cukup bagus", "performa oke") — semua kriteria harus deterministik dan terukur.

### Dimensi 6 — Kualitas Bahasa Indonesia

Periksa apakah dokumen ini menggunakan **bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami** oleh junior programmer atau AI model yang lebih kecil/murah:

- [ ] Cari dan perbaiki kalimat yang **ambigu** atau memiliki dua makna berbeda.
- [ ] Cari dan perbaiki kalimat yang **terlalu panjang dan berbelit-belit** — pecah menjadi kalimat lebih pendek jika perlu.
- [ ] Cari dan perbaiki **istilah teknis bahasa Inggris** yang belum dijelaskan atau tidak ada padanannya di Glosarium (Bab 18.1).
- [ ] Cari dan perbaiki **inkonsistensi penulisan istilah** — pastikan satu istilah ditulis konsisten di seluruh dokumen (misal: jangan campur "Kepala Percetakan" dan "kepala cetak" untuk orang yang sama).
- [ ] Cari dan perbaiki **salah ketik (typo)**, **salah ejaan**, atau **tanda baca yang tidak tepat** pada teks berbahasa Indonesia.
- [ ] Pastikan **Langkah Pengujian** pada setiap skrip UAT ditulis dengan kalimat aktif, ringkas, dan perintah yang jelas (misal: "Masukkan ID barang = `1`" bukan "Silakan dapat memasukkan nomor ID dari barang tersebut").
- [ ] Pastikan **Hasil Diharapkan** ditulis dengan kondisi konkret dan terverifikasi (misal: "Stok berkurang menjadi 8 Rim" bukan "Stok berkurang dengan benar").

### Dimensi 7 — Kualitas Kelengkapan yang Tidak Menghambat Pekerjaan

Periksa apakah kualitas kelengkapan isi dokumen ini **sudah cukup mandiri** sehingga tidak akan menyebabkan pertanyaan berulang atau interupsi saat dieksekusi:

- [ ] Pastikan setiap skrip UAT memiliki **prasyarat yang lengkap** dan spesifik sehingga penguji tahu persis kondisi database dan sistem yang diperlukan sebelum menjalankan skrip tersebut.
- [ ] Pastikan setiap skrip UAT memiliki **data uji yang konkret** dengan nilai numerik spesifik (`Decimal('2.0000')` bukan "sejumlah tertentu"), bukan hanya placeholder umum.
- [ ] Pastikan **Checklist Kesiapan UAT** (Bab 4) cukup detail sehingga tim teknis bisa mempersiapkan lingkungan pengujian tanpa perlu bertanya tambahan hal-hal dasar ke penyusun dokumen.
- [ ] Pastikan **Jadwal UAT** (Bab 3.2) walau kolom tanggal bertanda `[DITENTUKAN MANUAL]` — kolom durasi, penanggung jawab, dan cakupan skenario sudah lengkap dan tidak ambigu.
- [ ] Pastikan **klasifikasi tingkat keparahan defect** (Bab 16.1) sudah cukup jelas kriterianya sehingga penguji bisa mengklasifikasikan temuan bug secara mandiri tanpa perlu konfirmasi berulang.

### Dimensi 8 — Pengisian Data Kosong atau Placeholder

Periksa seluruh dokumen dan **identifikasi semua data yang kosong, belum terisi, atau bertanda placeholder**, lalu **isi dengan data yang sesuai, cocok, dan relevan** dalam ruang lingkup dokumen UAT Script ini:

- [ ] Cari semua teks bertanda `[DITENTUKAN MANUAL]`, `[DATA BELUM TERSEDIA]`, `[Ditentukan oleh User]`, `[Diisi...]`, atau sejenisnya di seluruh dokumen.
- [ ] Untuk setiap placeholder yang ditemukan, **tentukan apakah data tersebut bisa diisi** berdasarkan konteks dokumen ini dan referensi yang tersedia:
  - Jika **bisa diisi** (misal: nama kota dari konteks proyek, nama jabatan yang sudah diketahui dari ACM): **isi dengan data yang tepat**.
  - Jika **tidak bisa diisi** (misal: tanggal eksekusi UAT aktual yang belum direncanakan, nama fisik penandatangan): **biarkan sebagai placeholder yang jelas** dengan keterangan mengapa tidak bisa diisi dan siapa yang bertanggung jawab mengisinya.
- [ ] Khusus untuk placeholder yang memang **wajib diisi manual oleh Pemilik Usaha/Kepala Percetakan** (misal: tanggal pelaksanaan sesi UAT, kota dan tanggal tanda tangan go-live), tambahkan **catatan instruksi pengisian** yang jelas di samping placeholder tersebut.
- [ ] Periksa apakah kolom `Nama / Jabatan` pada tabel Tim Pelaksana UAT (Bab 3.1) untuk Senior UAT Analyst, Kepala Percetakan, dan QA Lead bisa diisi berdasarkan konteks proyek — jika bisa, isi; jika tidak, berikan instruksi pengisian yang jelas.

### Dimensi 9 — Validasi Khusus Dokumen UAT Script

Lakukan pemeriksaan tambahan yang spesifik terhadap ciri khas dokumen UAT Script:

- [ ] **Konsistensi Kalkulasi Desimal:** Verifikasi ulang setiap contoh kalkulasi numerik di dalam dokumen (HPP BOM, depresiasi, payroll, selisih kas, dsb.) — pastikan angka sudah benar secara matematis dan menggunakan format `Decimal(15,4)` dengan `ROUND_HALF_UP`. Referensi kalkulasi yang harus diverifikasi:
  - HPP BOM Stempel Flash: `(0.0025 × 100.000,0000) + (1.0000 × 4.500,0000) = 250,0000 + 4.500,0000 = 4.750,0000` — verifikasi kebenaran angka ini.
  - Depresiasi printer: `10.000.000,0000 / 60 = 166.666,6667` (ROUND_HALF_UP) — verifikasi kebenaran angka ini.
  - Bunga bank: `(10.000.000,0000 × 10%) / 12 = 83.333,3333` — verifikasi kebenaran angka ini.
  - Cicilan kerabat: `5.000.000,0000 / 10 = 500.000,0000` — verifikasi kebenaran angka ini.
  - Limbah karet: `0.0005 × 100.000,0000 = 50,0000` — verifikasi kebenaran angka ini.
  - Selisih kas handover normal: `800.000,0000 - (500.000,0000 + 300.000,0000) = 0,0000` — verifikasi kebenaran angka ini.
  - Selisih kas handover anomali: `780.000,0000 - 800.000,0000 = -20.000,0000` — verifikasi kebenaran angka ini.
  - Cari dan verifikasi kalkulasi numerik lainnya yang mungkin ada di seluruh dokumen.
- [ ] **Konsistensi Kode Error:** Pastikan kode error yang disebutkan di Hasil Diharapkan setiap skrip UAT sama persis dengan katalog error di CLI Interaction Flow (R-CLI) — tidak boleh ada kode yang tidak terdaftar.
- [ ] **Konsistensi Peran Penguji:** Verifikasi bahwa peran `Aktor Penguji` pada setiap skrip UAT sesuai dengan wewenang peran tersebut di Access Control Matrix (R-ACM) — misal, menu payroll hanya boleh diuji oleh Pemilik Usaha, bukan kasir.
- [ ] **Kelengkapan Diagram E2E Mermaid:** Pastikan diagram mermaid di UAT-E2E-001 (Bab 14.1) mencakup semua 12 langkah simulasi yang ada di tabel langkah di bawahnya, dan tidak ada langkah yang hilang dari diagram.
- [ ] **Konsistensi Username Akun Uji:** Pastikan semua `username` yang disebutkan di dalam Langkah Pengujian dan Prasyarat setiap skrip UAT konsisten dengan daftar 8 akun uji di Bab 18.2.
- [ ] **Validasi Kelengkapan Matriks Ketertelusuran (Bab 18.3):** Verifikasi bahwa 44 baris matriks sudah mencakup semua UAT-001 s.d. UAT-044 tanpa duplikasi, tanpa nomor yang terlewat, dan setiap baris terisi lengkap.
- [ ] **Kelayakan Sign-Off Criteria:** Periksa apakah 7 kriteria sign-off di Bab 17.2 mencakup semua aspek kritis (fungsional, keamanan, performa, kepatuhan regulasi UU PDP) yang disebutkan di Test Plan (R-TP) sebagai exit criteria UAT.
- [ ] **Cakupan Pengujian Non-Fungsional (Bab 15):** Verifikasi apakah 3 skrip non-fungsional (performance < 2 detik, CLI usability, encoding UTF-8) sudah mencakup semua aspek non-fungsional yang tertulis di Test Plan (R-TP) — jika ada aspek yang terlewat, tambahkan skrip baru.
- [ ] **Konsistensi Versi Referensi:** Pastikan semua referensi dokumen di Bab 19 (Referensi Dokumen) memiliki versi yang tertulis dengan benar dan konsisten dengan versi aktual dokumen referensi.

### Dimensi 10 — Konsistensi Internal Dokumen

Periksa apakah data dan informasi yang disebutkan di satu bagian dokumen **konsisten** dengan bagian lain di dokumen yang sama:

- [ ] Pastikan daftar modul di Bab 2.2 (10 modul M.1 s.d. M.10) konsisten dengan pengelompokan modul pada judul setiap skrip UAT di bab-bab sesi.
- [ ] Pastikan daftar sesi di Jadwal UAT (Bab 3.2) konsisten dengan jumlah dan urutan bab sesi (Bab 5 s.d. Bab 15).
- [ ] Pastikan daftar 44 skrip yang disebutkan di Bab 1.2 (Cakupan Dokumen) konsisten dengan jumlah skrip yang benar-benar ada di bab-bab sesi.
- [ ] Pastikan `Kriteria Keberhasilan UAT Keseluruhan` (Bab 2.4) konsisten dengan `Kriteria Keluar UAT` (Bab 17.1) — tidak boleh ada kontradiksi atau duplikasi yang membingungkan.
- [ ] Pastikan data jumlah use case yang disebutkan di Bab 17.2 ("44 Use Case") konsisten dengan total skenario UAT di Bab 1.2 ("44 skrip UAT") — verifikasi apakah ini merujuk ke hal yang sama atau berbeda.

---

## 5. Prosedur Implementasi (Langkah-Langkah Eksekusi Wajib)

> **PENTING:** Ikuti setiap langkah secara **berurutan**. Jangan melompati langkah. Tandai `[x]` setiap item checklist setelah diselesaikan sebelum melanjutkan ke langkah berikutnya.

---

### FASE 1 — Persiapan dan Pembacaan Dokumen

#### Langkah 1.1 — Adopsi Persona
- [ ] Baca kembali Bab 2 (Persona) dan internalisasi peran sebagai **Senior UAT Engineer & SQA Lead** sebelum melakukan pekerjaan apa pun.

#### Langkah 1.2 — Baca Dokumen Target Secara Penuh
- [ ] Buka dan baca **seluruh isi** file `docs/sdlc/05_testing/03_uat_script.md` dari baris pertama hingga baris terakhir tanpa melewatkan bagian mana pun.
- [ ] Catat secara internal: total jumlah skrip UAT yang ada, total bab/seksi, struktur umum dokumen, dan potensi masalah awal yang terlihat.

#### Langkah 1.3 — Baca Seluruh Dokumen Referensi
Baca setiap file referensi berikut secara penuh dan catat poin-poin kunci yang relevan:

- [ ] Baca `docs/sdlc/05_testing/01_test_plan.md` (R-TP) secara penuh — catat daftar 44 skenario induk, exit criteria UAT, error mapping, spesifikasi hardware, dan aspek non-fungsional.
- [ ] Baca `docs/sdlc/05_testing/02_test_cases.md` (R-TC) secara penuh — catat semua ID test case, langkah detail, data uji konkret, dan expected result per test case.
- [ ] Baca `docs/sdlc/02_analysis/02_software_requirements.md` (R-SRS) secara penuh — catat kode SRS-F-001 s.d. SRS-F-040, batasan input, dan aturan validasi bisnis.
- [ ] Baca `docs/sdlc/02_analysis/03_use_case_diagram.md` (R-UC) secara penuh — catat kode UC-001 s.d. UC-041 beserta aktor per use case.
- [ ] Baca `docs/sdlc/02_analysis/06_access_control_matrix.md` (R-ACM) secara penuh — catat 8 peran dan wewenang akses menu per peran.
- [ ] Baca `docs/sdlc/03_design/04_cli_interaction_flow.md` (R-CLI) secara penuh — catat katalog lengkap kode error, format navigasi breadcrumb, dan spesifikasi visual ANSI.
- [ ] Baca `docs/sdlc/03_design/05_bom_hpp_design.md` (R-BOM) secara penuh — catat formula HPP BOM, spesifikasi `Decimal(15,4)`, `ROUND_HALF_UP`, dan data komposisi produk kustom.
- [ ] Baca `docs/sdlc/03_design/06_security_design.md` (R-SEC) secara penuh — catat bcrypt cost factor, JWT duration (detik), Fernet key spec, AES-256 spec, dan kebijakan brute-force lockout.
- [ ] Baca `docs/sdlc/02_analysis/04_workflow_diagram.md` (R-WF) secara penuh — catat alur operasional bisnis harian, urutan proses, dan transisi status objek bisnis.

---

### FASE 2 — Analisis dan Validasi per Dimensi

> **INSTRUKSI:** Eksekusi setiap sub-langkah berikut secara berurutan. Jangan mulai dimensi berikutnya sebelum dimensi sebelumnya selesai sepenuhnya.

#### Langkah 2.1 — Validasi Dimensi 1: Komparasi Referensi
- [ ] Buat daftar semua ID skenario asal yang disebutkan di dokumen target, bandingkan satu per satu dengan daftar 44 skenario di Test Plan (R-TP) — catat yang konsisten dan yang berpotensi berbeda/salah.
- [ ] Buat daftar semua ID test case yang disebutkan di dokumen target, cocokkan satu per satu dengan Test Cases (R-TC) — catat yang ada dan yang tidak ditemukan di R-TC.
- [ ] Buat daftar semua kode SRS yang disebutkan di dokumen target, cocokkan dengan SRS (R-SRS) — catat yang konsisten dan yang mungkin salah tulis.
- [ ] Buat daftar semua kode UC yang disebutkan di dokumen target, cocokkan dengan Use Case Diagram (R-UC) — catat yang konsisten dan yang bermasalah.
- [ ] Verifikasi setiap kode error yang muncul di kolom `Hasil Diharapkan` terhadap katalog lengkap di CLI Flow (R-CLI) — catat kode error yang tidak terdaftar.
- [ ] Verifikasi semua kalkulasi numerik (HPP, depresiasi, cicilan, selisih kas, dll.) secara manual satu per satu — catat yang salah dan nilai koreksinya.
- [ ] Verifikasi semua spesifikasi keamanan (bcrypt, JWT, Fernet, AES-256, brute-force) terhadap Security Design (R-SEC) — catat inkonsistensi.
- [ ] Verifikasi alur diagram mermaid E2E (12 langkah) terhadap Workflow Diagram (R-WF) — catat urutan yang tidak sesuai alur bisnis nyata.
- [ ] Catat semua inkonsistensi yang ditemukan sebagai temuan — akan diperbaiki di Fase 3.

#### Langkah 2.2 — Validasi Dimensi 2: Kelengkapan Data
- [ ] Buat checklist 44 UAT individual: tulis UAT-001 s.d. UAT-044 dan centang mana yang ada di dokumen target — identifikasi yang hilang.
- [ ] Verifikasi UAT-E2E-001 memiliki tepat 12 langkah simulasi yang lengkap dan tidak ada langkah yang kosong kontennya.
- [ ] Verifikasi UAT-NF-001, UAT-NF-002, UAT-NF-003 terdokumentasi dengan kriteria kelulusan terukur (angka konkret, bukan perkiraan).
- [ ] Verifikasi semua 10 modul (M.1 s.d. M.10) tercakup minimal satu skrip UAT — identifikasi modul yang tidak memiliki skrip UAT sama sekali.
- [ ] Verifikasi matriks ketertelusuran (Bab 18.3) memiliki persis 44 baris lengkap tanpa ada yang kosong.
- [ ] Verifikasi 8 akun uji di Bab 18.2 terisi lengkap semua baris dan kolomnya.
- [ ] Verifikasi setiap skrip UAT memiliki semua atribut tabel wajib — catat skrip mana dan atribut apa yang hilang.
- [ ] Catat semua gap kelengkapan yang ditemukan — akan diisi di Fase 3.

#### Langkah 2.3 — Validasi Dimensi 3: Kebersihan Konten
- [ ] Identifikasi apakah ada konten teknis implementasi (query SQL, kode Python, skema tabel) yang tidak seharusnya ada di UAT Script — catat lokasi dan saran perbaikannya.
- [ ] Bandingkan narasi Langkah Pengujian di beberapa skrip UAT sampel dengan Test Cases (R-TC) yang bersesuaian — apakah ada yang duplikat 1:1 tanpa diterjemahkan ke bahasa bisnis?
- [ ] Verifikasi Out-of-Scope (Bab 2.3) tidak mengecualikan hal yang seharusnya diuji dalam UAT konteks bisnis toko percetakan.
- [ ] Verifikasi Glosarium (Bab 18.1) hanya berisi istilah yang relevan dan digunakan dalam dokumen ini — identifikasi istilah yang perlu ditambahkan atau dihapus.
- [ ] Verifikasi Data Uji di setiap skrip menggunakan nilai konkret dan deterministik — catat yang masih abstrak/umum.
- [ ] Catat temuan konten yang perlu dibersihkan atau disesuaikan.

#### Langkah 2.4 — Validasi Dimensi 4: Standar Struktur Industri
- [ ] Periksa keberadaan dan kelengkapan setiap elemen struktural standar yang tercantum di Dimensi 4 Bab 4 — centang yang ada, catat yang tidak ada.
- [ ] Identifikasi bab atau sub-bab yang hilang, kurang detail, atau tidak sesuai standar IEEE 829/ISO 29119-3.
- [ ] Catat semua temuan struktural yang perlu diperbaiki atau ditambahkan.

#### Langkah 2.5 — Validasi Dimensi 5: Kualitas sebagai Input SDLC Berikutnya
- [ ] Simulasikan perspektif pembuat UAT Test Report: periksa setiap skrip UAT — apakah semua kolom yang diperlukan untuk pelaporan hasil sudah ada?
- [ ] Simulasikan perspektif pembuat Deployment/Release Document: periksa formulir sign-off (Bab 17.3) — apakah semua field sudah lengkap?
- [ ] Simulasikan perspektif pembuat Training Manual: baca 5 skrip UAT acak — apakah Langkah Pengujian cukup deskriptif sebagai panduan operasional untuk karyawan baru?
- [ ] Identifikasi semua kriteria yang masih subjektif atau tidak terukur di kolom Hasil Diharapkan seluruh skrip UAT.
- [ ] Catat temuan yang perlu diperbaiki untuk meningkatkan kualitas sebagai input SDLC berikutnya.

#### Langkah 2.6 — Validasi Dimensi 6: Kualitas Bahasa Indonesia
- [ ] Baca ulang seluruh dokumen target secara khusus dengan fokus pada bahasa — bukan konten teknis.
- [ ] Tandai dan catat setiap kalimat yang ambigu, berbelit, atau tidak natural beserta saran perbaikannya.
- [ ] Tandai setiap istilah teknis bahasa Inggris yang tidak didefinisikan di Glosarium — tambahkan ke daftar untuk ditambahkan ke Glosarium.
- [ ] Tandai setiap inkonsistensi penulisan istilah di seluruh dokumen.
- [ ] Tandai setiap typo atau salah ejaan yang ditemukan.
- [ ] Tandai Langkah Pengujian yang ditulis tidak dalam format kalimat aktif/perintah yang jelas dan ringkas.
- [ ] Tandai Hasil Diharapkan yang masih menggunakan frasa tidak terukur atau subjektif.

#### Langkah 2.7 — Validasi Dimensi 7: Kualitas Kelengkapan Anti-Interupsi
- [ ] Uji 10 skrip UAT secara acak: apakah prasyaratnya cukup spesifik untuk disiapkan tanpa bertanya tambahan ke penyusun dokumen?
- [ ] Uji 10 skrip UAT secara acak: apakah Data Ujinya sudah konkret dan tidak perlu interpretasi lebih lanjut?
- [ ] Evaluasi Checklist Kesiapan UAT (Bab 4) secara keseluruhan: apakah tim teknis bisa menyiapkan lingkungan pengujian hanya dengan membaca Bab 4 ini?
- [ ] Evaluasi klasifikasi defect (Bab 16.1): baca setiap baris — apakah kriteria setiap level sudah cukup jelas untuk pengklasifikasian mandiri oleh penguji baru?

#### Langkah 2.8 — Validasi Dimensi 8: Data Kosong/Placeholder
- [ ] Lakukan pencarian sistematis pada seluruh teks dokumen target untuk menemukan semua string berikut (satu per satu): `[DITENTUKAN MANUAL]`, `[DATA BELUM TERSEDIA]`, `[Ditentukan oleh User]`, `[Diisi saat]`, `[XXX]`, `[TBD]`, `*[Diisi`, dan variasi lainnya.
- [ ] Buat daftar lengkap semua placeholder yang ditemukan beserta lokasi (nama bab, nomor skrip UAT, atau nama kolom tabel) dan konteks kalimatnya.
- [ ] Untuk setiap placeholder, tentukan: bisa diisi berdasarkan konteks referensi yang tersedia (R-TP, R-TC, R-ACM, dll.)? Jika ya, tentukan nilai yang tepat. Jika tidak, formulasikan instruksi pengisian yang jelas dan tentukan siapa penanggungjawabnya.

#### Langkah 2.9 — Validasi Dimensi 9: Ciri Khas UAT Script
- [ ] Verifikasi ulang semua kalkulasi desimal yang teridentifikasi di Dimensi 9 Bab 4 satu per satu — catat yang salah dan nilai koreksinya.
- [ ] Verifikasi setiap kode error yang disebutkan di seluruh skrip UAT ada di katalog R-CLI — identifikasi dan catat yang tidak ditemukan.
- [ ] Verifikasi peran penguji (Aktor Penguji) pada setiap skrip UAT sesuai wewenang di R-ACM — catat yang tidak sesuai.
- [ ] Verifikasi diagram mermaid E2E (Bab 14.1): hitung node diagram — apakah ada 12 node yang sesuai dengan 12 baris tabel di bawahnya?
- [ ] Hitung dan verifikasi semua username di Langkah Pengujian dan Prasyarat seluruh skrip UAT — cocokkan dengan 8 username di Bab 18.2.
- [ ] Hitung baris di Matriks Ketertelusuran (Bab 18.3): harus persis 44 baris data (UAT-001 s.d. UAT-044) tanpa duplikasi dan tanpa yang terlewat.
- [ ] Bandingkan 7 kriteria sign-off (Bab 17.2) dengan exit criteria di Test Plan (R-TP) — apakah ada aspek kritis yang tidak tercakup?
- [ ] Bandingkan 3 skrip non-fungsional (Bab 15) dengan aspek non-fungsional di Test Plan (R-TP) — apakah ada aspek yang tidak tercakup?
- [ ] Verifikasi versi semua dokumen di tabel Referensi (Bab 19) sudah benar dan konsisten.

#### Langkah 2.10 — Validasi Dimensi 10: Konsistensi Internal
- [ ] Verifikasi daftar 10 modul di Bab 2.2 konsisten dengan label modul pada judul setiap skrip UAT di bab sesi.
- [ ] Verifikasi daftar 10 sesi di Jadwal UAT (Bab 3.2) konsisten dengan jumlah dan urutan bab sesi (Bab 5 s.d. Bab 14).
- [ ] Verifikasi klaim "44 skrip UAT individual" di Bab 1.2 konsisten dengan jumlah skrip yang benar-benar terdokumentasi.
- [ ] Verifikasi tidak ada kontradiksi antara Kriteria Keberhasilan UAT (Bab 2.4) dan Kriteria Keluar UAT (Bab 17.1).
- [ ] Verifikasi referensi silang antar skrip UAT (misal dalam UAT-E2E-001 merujuk ke UAT-001, UAT-022, dst.) — pastikan nomor yang dirujuk konsisten dengan nomor skrip yang benar-benar ada.

---

### FASE 3 — Perbaikan dan Penyempurnaan Dokumen

> **INSTRUKSI KRITIS:** Berdasarkan seluruh temuan dari Fase 2, lakukan **semua perbaikan yang diperlukan** pada konten dokumen. Catat semua perubahan yang dilakukan untuk dimasukkan ke Riwayat Perubahan Dokumen.

#### Langkah 3.1 — Perbaiki Inkonsistensi Referensi
- [ ] Koreksi setiap kode skenario asal, test case, SRS, atau UC yang tidak konsisten dengan dokumen referensi.
- [ ] Koreksi setiap kode error yang tidak sesuai dengan katalog di R-CLI.
- [ ] Koreksi setiap kalkulasi numerik yang salah dengan nilai yang benar menggunakan `Decimal(15,4)` dan `ROUND_HALF_UP`.
- [ ] Koreksi setiap spesifikasi keamanan yang tidak konsisten dengan R-SEC.

#### Langkah 3.2 — Lengkapi Data yang Hilang
- [ ] Tambahkan skrip UAT yang hilang jika ada gap dari 44 skenario induk — setiap skrip baru harus memiliki semua 16 atribut tabel wajib.
- [ ] Lengkapi atribut tabel yang hilang pada skrip UAT yang tidak lengkap.
- [ ] Lengkapi baris matriks ketertelusuran yang kosong atau hilang.
- [ ] Lengkapi entri data fixtures yang kurang di Bab 18.2.
- [ ] Tambahkan skrip non-fungsional baru jika ada aspek non-fungsional dari Test Plan yang belum tercakup.

#### Langkah 3.3 — Bersihkan Konten yang Tidak Relevan
- [ ] Pindahkan atau ringkas konten teknis yang tidak seharusnya ada di UAT Script — jika diperlukan sebagai konteks, jadikan catatan kaki singkat.
- [ ] Terjemahkan Langkah Pengujian yang masih terlalu teknis/programmer ke bahasa bisnis yang dapat dipahami oleh Pemilik Usaha atau Kepala Percetakan.

#### Langkah 3.4 — Perbaiki Struktur Dokumen
- [ ] Tambahkan bab atau sub-bab yang hilang sesuai standar industri IEEE 829/ISO 29119-3.
- [ ] Perbaiki hierarki heading jika tidak konsisten (misal: Bab 5 untuk Sesi 1 vs. Bab 6 untuk Sesi 2, dst.).
- [ ] Pastikan setiap sesi UAT memiliki header sesi yang jelas (Aktor Utama, Lingkungan).

#### Langkah 3.5 — Isi Placeholder
- [ ] Isi semua placeholder yang bisa diisi berdasarkan konteks referensi dokumen dengan nilai yang tepat dan spesifik.
- [ ] Tambahkan instruksi pengisian yang jelas dan tegas pada placeholder yang memang harus diisi manual oleh Pemilik Usaha, Kepala Percetakan, atau Senior UAT Analyst.
- [ ] Pastikan tidak ada placeholder yang dibiarkan kosong tanpa penjelasan mengapa kosong dan siapa yang harus mengisi.

#### Langkah 3.6 — Perbaiki Bahasa Indonesia
- [ ] Perbaiki semua kalimat ambigu, berbelit, atau tidak natural — tulis ulang dengan kalimat yang singkat, jelas, dan langsung ke inti.
- [ ] Perbaiki semua typo dan salah ejaan yang ditemukan.
- [ ] Konsistensikan penulisan semua istilah di seluruh dokumen.
- [ ] Perbaiki semua Langkah Pengujian ke format kalimat aktif/perintah yang singkat dan jelas.
- [ ] Perbaiki semua Hasil Diharapkan ke format kondisi konkret dan terverifikasi dengan nilai numerik spesifik.
- [ ] Tambahkan definisi istilah baru yang perlu ke Glosarium (Bab 18.1).

#### Langkah 3.7 — Perbarui Riwayat Perubahan Dokumen
- [ ] Buka bagian Riwayat Perubahan Dokumen di awal dokumen target.
- [ ] Tambahkan baris baru untuk versi v1.1 dengan kolom: Versi (`1.1`), Tanggal (tanggal hari ini), Perubahan (ringkasan komprehensif semua perubahan yang dilakukan), dan Oleh (`Senior UAT Engineer & SQA Lead`).
- [ ] Ubah versi di header dokumen (front matter YAML) dari `1.0` menjadi `1.1`.
- [ ] Ubah tanggal di header dokumen menjadi tanggal revisi aktual hari ini.
- [ ] Ubah status di header dokumen dari `Draft` menjadi `Reviewed`.
- [ ] Update baris diagram SDLC posisi dokumen (Bab 1.3) — ubah label dari `UAT Script v1.0` menjadi `UAT Script v1.1`.

#### Langkah 3.8 — Tambahkan Referensi Baru (Jika Ada)
- [ ] Identifikasi apakah dalam proses validasi dan perbaikan ditemukan kebutuhan untuk merujuk ke file referensi baru yang belum terdaftar di Bab 19 dokumen target (misal: ERD, DB Schema, Narasi Proyek).
- [ ] Jika ada referensi baru yang digunakan, tambahkan di bagian paling bawah tabel Referensi Dokumen (Bab 19) dengan format: `| [nomor] | [KODE] | [Nama Dokumen] | [path/file.md] | [versi] |`
- [ ] Pastikan tidak ada referensi yang digunakan dalam penulisan konten tetapi tidak tercantum di tabel Bab 19.

---

### FASE 4 — Penulisan Ulang dan Overwrite File

> **INSTRUKSI MUTLAK — BACA DENGAN SEKSAMA SEBELUM EKSEKUSI:**

#### Langkah 4.1 — Siapkan Konten Final Dokumen
- [ ] Setelah **semua** perbaikan dari Fase 3 selesai diidentifikasi dan direncanakan, susun konten final dokumen yang telah diperbaiki secara menyeluruh.
- [ ] Pastikan urutan struktur dokumen benar: header YAML → Riwayat Perubahan → Bab 1 Informasi Dokumen → Bab 2 Lingkup UAT → Bab 3 Organisasi → Bab 4 Kesiapan → Bab 5-14 Sesi UAT → Bab 15 Non-Fungsional → Bab 16 Defect Handling → Bab 17 Exit Criteria & Sign-Off → Bab 18 Lampiran → Bab 19 Referensi.
- [ ] Verifikasi bahwa konten final mencakup semua 44 skrip UAT individual (UAT-001 s.d. UAT-044), 1 skrip E2E (UAT-E2E-001), dan 3 skrip non-fungsional (UAT-NF-001 s.d. UAT-NF-003).

#### Langkah 4.2 — Overwrite File Target
- [ ] Lakukan penulisan ulang **seluruh isi dokumen** dengan cara **menimpa (overwrite)** file `docs/sdlc/05_testing/03_uat_script.md` secara penuh.
- [ ] **MUTLAK:** Seluruh teks dari **baris pertama hingga baris terakhir** harus ditulis ulang sepenuhnya.
- [ ] **MUTLAK:** **TIDAK BOLEH ADA** konten yang dipotong (truncated), diringkas menjadi `[...]`, dihilangkan, atau diganti dengan keterangan "konten tidak berubah" — **SEMUA harus ditulis ulang secara eksplisit dan lengkap**.
- [ ] **MUTLAK:** Semua 44 skrip UAT individual, semua bab sesi, semua lampiran, seluruh matriks ketertelusuran, dan semua referensi harus ada secara penuh dalam file hasil overwrite.
- [ ] **MUTLAK:** Pastikan versi di header dokumen sudah berubah menjadi `1.1`.
- [ ] **MUTLAK:** Pastikan tanggal di header dokumen sudah diperbarui ke tanggal revisi.
- [ ] **MUTLAK:** Pastikan status di header dokumen sudah berubah menjadi `Reviewed`.

#### Langkah 4.3 — Verifikasi Hasil Overwrite
- [ ] Setelah overwrite selesai, **buka dan baca kembali file yang sudah ditimpa** dari baris pertama hingga baris terakhir.
- [ ] Verifikasi bahwa versi di front matter sudah berubah ke `1.1`.
- [ ] Verifikasi bahwa status di front matter sudah berubah ke `Reviewed`.
- [ ] Hitung jumlah skrip UAT yang ada: harus ditemukan UAT-001, UAT-002, ..., UAT-044 (44 skrip), UAT-E2E-001 (1 skrip), UAT-NF-001, UAT-NF-002, UAT-NF-003 (3 skrip).
- [ ] Verifikasi bahwa semua perbaikan dari Fase 3 sudah teraplikasi dengan benar di file final.
- [ ] Verifikasi bahwa Matriks Ketertelusuran di Bab 18.3 masih memiliki lengkap 44 baris data.
- [ ] Verifikasi bahwa Bab 19 (Referensi Dokumen) sudah memuat semua referensi termasuk yang baru ditambahkan (jika ada).
- [ ] Verifikasi bahwa Riwayat Perubahan Dokumen memiliki baris baru untuk versi v1.1.

---

## 6. Kriteria Selesai (Definition of Done)

Issue ini dianggap **selesai** jika dan hanya jika **seluruh** kondisi berikut terpenuhi:

1. `[ ]` Seluruh checklist di Fase 1, Fase 2, Fase 3, dan Fase 4 sudah ditandai `[x]`.
2. `[ ]` File `docs/sdlc/05_testing/03_uat_script.md` berhasil dioverwrite dengan konten v1.1 yang lengkap dan tidak ada truncasi sama sekali.
3. `[ ]` Versi dokumen sudah berubah menjadi `v1.1`, status menjadi `Reviewed`, dan Riwayat Perubahan Dokumen sudah memiliki entri baru untuk versi v1.1.
4. `[ ]` Tidak ada kode error, ID test case, ID SRS, atau ID UC yang disebutkan dalam dokumen yang tidak konsisten dengan dokumen referensinya.
5. `[ ]` Tidak ada kalkulasi numerik desimal yang salah di seluruh dokumen.
6. `[ ]` Tidak ada placeholder `[DITENTUKAN MANUAL]` atau `[DATA BELUM TERSEDIA]` yang bisa diisi berdasarkan konteks referensi tetapi tidak diisi.
7. `[ ]` Dokumen dapat dieksekusi oleh Pemilik Usaha dan Kepala Percetakan tanpa perlu membaca dokumen lain terlebih dahulu untuk memahami apa yang harus dilakukan dalam setiap skrip UAT.
8. `[ ]` Semua 44 skrip UAT individual, 1 skrip E2E, dan 3 skrip non-fungsional ada dalam dokumen final yang lengkap.
9. `[ ]` Matriks Ketertelusuran memiliki persis 44 baris data yang terisi lengkap.

---

## 7. Batasan dan Larangan Implementasi

> **JANGAN LAKUKAN** hal-hal berikut selama implementasi issue ini:

- ❌ **JANGAN** menghapus konten yang sudah ada tanpa alasan validasi yang kuat dan teridentifikasi di Fase 2.
- ❌ **JANGAN** mengubah ID UAT, ID Test Case, ID SRS, atau ID UC tanpa melakukan verifikasi silang terlebih dahulu dengan dokumen referensi yang bersangkutan.
- ❌ **JANGAN** mengganti nilai numerik atau data uji konkret dengan placeholder atau estimasi.
- ❌ **JANGAN** meringkas atau memotong Langkah Pengujian atau Hasil Diharapkan dengan alasan efisiensi — setiap langkah harus tetap lengkap dan spesifik.
- ❌ **JANGAN** menulis ulang dokumen secara parsial — harus overwrite penuh dari baris pertama ke terakhir tanpa exception.
- ❌ **JANGAN** mengubah konten kolom `Hasil Aktual`, `Status`, `Catatan Temuan`, dan `Tanda Tangan Penguji` — kolom-kolom ini memang harus tetap dalam kondisi placeholder karena akan diisi saat eksekusi UAT aktual oleh penguji manusia. Biarkan isinya `*[Diisi saat eksekusi UAT]*` atau `____________________`.
- ❌ **JANGAN** menambahkan skrip UAT baru yang tidak ada sumber rujukannya di Test Plan (R-TP) — setiap skrip UAT harus dapat ditelusuri ke skenario induk di Test Plan.
- ❌ **JANGAN** mengubah makna bisnis dari Langkah Pengujian atau Hasil Diharapkan — hanya perbaiki gaya bahasa, bukan substansi skenario pengujian.

---

## 8. Output yang Diharapkan

Setelah issue ini diimplementasikan, output yang diharapkan adalah:

| Artefak | Lokasi | Deskripsi |
|---|---|---|
| **UAT Script v1.1** | `docs/sdlc/05_testing/03_uat_script.md` | File hasil overwrite penuh — versi v1.1 yang telah divalidasi secara 10 dimensi, diperbaiki inkonsistensinya, dilengkapi datanya, dibersihkan bahasanya, dan siap digunakan sebagai dokumen eksekusi UAT aktual oleh Pemilik Usaha dan Kepala Percetakan proyek AbuCom. |

---

*Issue ini dibuat pada: 2026-05-26 oleh Senior UAT Analyst & Business Acceptance Specialist untuk proyek AbuCom.*
