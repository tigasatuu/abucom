---
judul          : Validasi & Perbaikan Menyeluruh Dokumen Changelog AbuCom
dokumen_target : docs/sdlc/07_maintenance/02_changelog.md
lokasi_ref     : docs/sdlc/
tanggal_dibuat : 2026-05-28
prioritas      : Tinggi
status         : Open
ditugaskan_ke  : Junior Programmer / AI Model
---

# Validasi & Perbaikan Menyeluruh Dokumen Changelog AbuCom

## Latar Belakang

Dokumen **Changelog** (`docs/sdlc/07_maintenance/02_changelog.md`) merupakan *Single Source of Truth* resmi seluruh riwayat perubahan sistem AbuCom versi v1.0.0 hingga roadmap masa depan. Dokumen ini disusun dari 14 berkas referensi SDLC formal. Sebelum dokumen ini digunakan sebagai acuan audit dan input fase-fase SDLC berikutnya, dokumen **wajib** divalidasi secara menyeluruh untuk memastikan kelengkapan, ketepatan, keselarasan struktur, dan kualitas bahasa.

Issue ini memberikan instruksi tahap demi tahap (low-level) yang harus diikuti secara berurutan tanpa ada langkah yang dilewati atau diasumsikan.

---

## Persona yang Harus Diasumsikan

> **WAJIB DIBACA SEBELUM MEMULAI.**

Sebelum mengerjakan satu pun tugas di bawah ini, kamu **harus** mengambil peran sebagai persona berikut dan mempertahankan perspektif ini sepanjang seluruh proses validasi:

```
Kamu adalah seorang SENIOR TECHNICAL WRITER & SDLC DOCUMENTATION AUDITOR
dengan spesialisasi ganda:

1. Configuration Manager & Release Engineer berpengalaman 10+ tahun yang
   telah mengelola siklus rilis enterprise skala besar, mahir dalam standar
   Keep a Changelog (keepachangelog.com), Semantic Versioning (semver.org),
   dan Conventional Commits.

2. Software Quality Assurance Analyst yang terbiasa melakukan cross-audit
   lintas dokumen SDLC (dari fase Planning hingga Maintenance) untuk
   memastikan konsistensi, kelengkapan, dan ketertelusuran (traceability)
   antardokumen.

Standar kualitas yang kamu terapkan: tidak ada data kosong yang dibiarkan,
tidak ada entri yang terlewat, tidak ada informasi yang tidak relevan
yang menyelinap masuk, dan tidak ada kalimat yang ambigu.
```

---

## Dokumen Target

| Atribut         | Nilai                                              |
|:----------------|:---------------------------------------------------|
| **File Target** | `docs/sdlc/07_maintenance/02_changelog.md`         |
| **Versi Saat Ini** | v1.0                                            |
| **Versi Setelah Revisi** | v1.1                                   |
| **Status Saat Ini** | Draft                                         |

---

## Daftar File Referensi yang Harus Dibaca

Baca **semua** file referensi berikut sebelum memulai validasi apapun. Jangan melewati satu pun file. Tandai setiap file yang sudah dibaca dengan `[x]`.

### Referensi PRIMER (baca pertama, paling penting)

- [ ] **[R-01]** `docs/sdlc/06_deployment/03_release_notes.md`
- [ ] **[R-02]** `docs/sdlc/07_maintenance/01_maintenance_guide.md`
- [ ] **[R-03]** `docs/sdlc/04_implementation/04_git_workflow.md`
- [ ] **[R-04]** `docs/sdlc/01_planning/01_project_charter.md`
- [ ] **[R-05]** `docs/sdlc/02_analysis/02_software_requirements.md`

### Referensi SEKUNDER (baca kedua)

- [ ] **[R-06]** `docs/sdlc/03_design/01_database_schema.sql`
- [ ] **[R-07]** `docs/sdlc/03_design/03_system_architecture.md`
- [ ] **[R-08]** `docs/sdlc/03_design/06_security_design.md`

### Referensi TERSIER (baca ketiga)

- [ ] **[R-09]** `docs/sdlc/04_implementation/01_coding_standard.md`
- [ ] **[R-10]** `docs/sdlc/04_implementation/03_module_structure.md`
- [ ] **[R-11]** `docs/sdlc/05_testing/01_test_plan.md`
- [ ] **[R-12]** `docs/sdlc/06_deployment/01_deployment_guide.md`
- [ ] **[R-13]** `docs/sdlc/01_planning/04_tech_stack_decision.md`
- [ ] **[R-14]** `docs/sdlc/05_testing/04_bug_report_template.md`

### Referensi Tambahan yang Mungkin Diperlukan (baca jika ada gap informasi)

- [ ] **[R-ADD-01]** `docs/sdlc/01_planning/02_feasibility_study.md`
- [ ] **[R-ADD-02]** `docs/sdlc/01_planning/03_stakeholder_register.md`
- [ ] **[R-ADD-03]** `docs/sdlc/01_planning/05_innovation_proposal.md`
- [ ] **[R-ADD-04]** `docs/sdlc/02_analysis/01_business_requirements.md`
- [ ] **[R-ADD-05]** `docs/sdlc/02_analysis/03_use_case_diagram.md`
- [ ] **[R-ADD-06]** `docs/sdlc/02_analysis/04_workflow_diagram.md`
- [ ] **[R-ADD-07]** `docs/sdlc/02_analysis/05_data_dictionary.md`
- [ ] **[R-ADD-08]** `docs/sdlc/02_analysis/06_access_control_matrix.md`
- [ ] **[R-ADD-09]** `docs/sdlc/03_design/02_erd_database.md`
- [ ] **[R-ADD-10]** `docs/sdlc/03_design/04_cli_interaction_flow.md`
- [ ] **[R-ADD-11]** `docs/sdlc/03_design/05_bom_hpp_design.md`
- [ ] **[R-ADD-12]** `docs/sdlc/05_testing/02_test_cases.md`
- [ ] **[R-ADD-13]** `docs/sdlc/05_testing/03_uat_script.md`
- [ ] **[R-ADD-14]** `docs/sdlc/06_deployment/02_environment_config.yaml`

---

## Tahapan Implementasi (Eksekusi Berurutan)

> **PERHATIAN KRITIS:** Eksekusi setiap tahap secara **berurutan dari atas ke bawah**. Jangan melompat ke tahap berikutnya sebelum tahap sebelumnya selesai sepenuhnya. Setiap kotak centang `[ ]` merepresentasikan satu tindakan atomik yang harus diselesaikan.

---

### TAHAP 0 — Persiapan & Pembacaan Dokumen

**Tujuan:** Membaca seluruh dokumen yang relevan sebelum melakukan analisis apapun.

- [ ] **0.1** Baca seluruh isi file `docs/sdlc/07_maintenance/02_changelog.md` dari baris pertama hingga baris terakhir. Jangan berhenti di tengah.
- [ ] **0.2** Catat versi dokumen saat ini (cek baris `versi :` di bagian front-matter YAML). Pastikan versi saat ini adalah `1.0`.
- [ ] **0.3** Catat seluruh kode referensi yang disebutkan di bagian **Seksi 7. Referensi Dokumen** pada dokumen target (R-01 hingga R-14).
- [ ] **0.4** Baca seluruh file referensi PRIMER [R-01] hingga [R-05] sesuai urutan daftar di atas. Catat poin-poin utama dari setiap file yang relevan dengan changelog.
- [ ] **0.5** Baca seluruh file referensi SEKUNDER [R-06] hingga [R-08]. Catat data teknis (nama tabel, spesifikasi hardware, mekanisme keamanan) yang perlu diverifikasi.
- [ ] **0.6** Baca seluruh file referensi TERSIER [R-09] hingga [R-14]. Catat standar penulisan, format bug, dan hasil testing yang perlu dicerminkan di changelog.
- [ ] **0.7** Baca file `docs/sdlc/narasi.txt` jika ada, sebagai konteks tambahan proyek.

---

### TAHAP 1 — Validasi Kelengkapan: Apakah Semua Data dari Referensi Sudah Terangkum?

**Tujuan:** Memastikan tidak ada informasi penting dari file referensi yang terlewat di dokumen changelog.

> **Cara kerja:** Untuk setiap poin di bawah, bandingkan isi dokumen target dengan isi file referensi yang disebutkan. Jika ada yang terlewat, **catat sebagai temuan** (gunakan format: `[TEMUAN-1.X] Deskripsi temuan`). Temuan ini akan diperbaiki di Tahap 5.

#### 1.A — Kelengkapan Entri Fitur Fungsional (SRS-F-XXX)

- [ ] **1.A.1** Buka file [R-05] `docs/sdlc/02_analysis/02_software_requirements.md`. Ekstrak semua kode kebutuhan fungsional (SRS-F-001 s.d SRS-F-040 dan SRS-F-ADD-01 s.d SRS-F-ADD-05).
- [ ] **1.A.2** Buka file [R-01] `docs/sdlc/06_deployment/03_release_notes.md`. Ekstrak semua fitur dan item perubahan yang terdaftar.
- [ ] **1.A.3** Cocokkan satu per satu: apakah **setiap kode SRS-F-XXX** dari [R-05] sudah ada entri-nya di **Seksi 3** dokumen target?
  - Jika ada SRS-F-XXX yang ada di [R-05] tetapi **tidak ada** di changelog → catat sebagai temuan.
  - Jika ada SRS-F-XXX yang ada di changelog tetapi **tidak ada** di [R-05] → catat sebagai temuan (inkonsistensi).
- [ ] **1.A.4** Cocokkan satu per satu: apakah **setiap fitur baru** yang disebutkan di [R-01] Release Notes sudah ada entri changelog-nya di Seksi 3?
  - Jika ada fitur di [R-01] yang tidak ada di changelog → catat sebagai temuan.

#### 1.B — Kelengkapan Entri Keamanan (Security)

- [ ] **1.B.1** Buka file [R-08] `docs/sdlc/03_design/06_security_design.md`. Ekstrak seluruh mekanisme keamanan yang diimplementasikan.
- [ ] **1.B.2** Cocokkan: apakah **setiap mekanisme keamanan** dari [R-08] sudah tercermin di sub-seksi `#### Keamanan (Security)` pada Seksi 3 dokumen target?
  - Jika ada mekanisme keamanan di [R-08] yang tidak ada di changelog → catat sebagai temuan.

#### 1.C — Kelengkapan Entri Infrastruktur (Infrastructure)

- [ ] **1.C.1** Buka file [R-07] `docs/sdlc/03_design/03_system_architecture.md`. Ekstrak spesifikasi hardware, topologi jaringan, dan konfigurasi sistem.
- [ ] **1.C.2** Buka file [R-06] `docs/sdlc/03_design/01_database_schema.sql`. Hitung dan catat jumlah total tabel yang ada. Verifikasi apakah angka "28 tabel" di dokumen target sudah benar sesuai file SQL aktual.
- [ ] **1.C.3** Buka file [R-13] `docs/sdlc/01_planning/04_tech_stack_decision.md`. Ekstrak daftar locked dependencies (nama paket dan versinya).
- [ ] **1.C.4** Cocokkan: apakah **semua spesifikasi infrastruktur** (hardware, jaringan, runtime, locked packages) dari [R-07] dan [R-13] sudah ada di sub-seksi `#### Infrastruktur (Infrastructure)` pada Seksi 3?
  - Jika ada komponen infrastruktur yang terlewat → catat sebagai temuan.

#### 1.D — Kelengkapan Known Issues

- [ ] **1.D.1** Buka file [R-14] `docs/sdlc/05_testing/04_bug_report_template.md`. Ekstrak semua bug yang sudah tercatat dengan status belum terselesaikan.
- [ ] **1.D.2** Buka file [R-01] `docs/sdlc/06_deployment/03_release_notes.md`. Ekstrak bagian Known Issues / Known Limitations.
- [ ] **1.D.3** Buka file [R-11] `docs/sdlc/05_testing/01_test_plan.md`. Cek apakah ada bug atau batasan yang dicatat di sana yang tidak ada di changelog.
- [ ] **1.D.4** Cocokkan: apakah **semua Known Issues** dari sumber di atas sudah ada di tabel `#### Masalah yang Diketahui (Known Issues)` dan daftar `#### Batasan yang Diketahui (Known Limitations)` pada Seksi 3?
  - Jika ada yang terlewat → catat sebagai temuan.

#### 1.E — Kelengkapan Roadmap (Upcoming Releases)

- [ ] **1.E.1** Buka file [R-01] Release Notes. Cari bagian roadmap atau rilis mendatang yang direncanakan.
- [ ] **1.E.2** Cocokkan: apakah **semua item roadmap** (v1.1.0 dan v2.0.0) dari [R-01] sudah ada di **Seksi 4. Rilis yang Direncanakan** dokumen target?
  - Jika ada item roadmap yang terlewat → catat sebagai temuan.

#### 1.F — Kelengkapan Daftar Dokumentasi SDLC

- [ ] **1.F.1** Buka direktori `docs/sdlc/` dan catat seluruh file `.md` dan `.sql` yang ada secara rekursif.
- [ ] **1.F.2** Cocokkan: apakah **setiap file dokumen SDLC** yang ada di direktori `docs/sdlc/` sudah terdaftar di sub-seksi `#### Dokumentasi (Documentation)` pada Seksi 3?
  - Jika ada file dokumen yang ada di direktori tetapi tidak terdaftar di changelog → catat sebagai temuan.
  - Jika ada file yang terdaftar di changelog tetapi tidak ada di direktori → catat sebagai temuan.

---

### TAHAP 2 — Validasi Relevansi: Apakah Semua Konten yang Ada Memang Seharusnya Ada?

**Tujuan:** Memastikan dokumen changelog bebas dari informasi yang tidak relevan, keluar dari ruang lingkup, atau duplikat.

> **Cara kerja:** Untuk setiap poin di bawah, periksa apakah konten di dokumen target memang sesuai dengan fungsi dan tujuan dokumen changelog. Jika ada konten yang tidak relevan, catat sebagai temuan.

- [ ] **2.1** Periksa **Seksi 1 (Informasi Dokumen)**: apakah semua sub-seksi (1.1 hingga 1.7) hanya berisi informasi yang relevan untuk dokumen changelog? Pastikan tidak ada detail teknis implementasi yang seharusnya berada di dokumen lain.
- [ ] **2.2** Periksa **Seksi 2 (Panduan Pembacaan)**: apakah panduan ini sudah cukup dan tidak berlebihan? Pastikan tidak ada konten yang menduplikasi isi dari Seksi 5.
- [ ] **2.3** Periksa **Seksi 3 (Changelog Rilis Terbaru)**: pastikan setiap entri `Added`, `Security`, `Infrastructure`, `Documentation` memang merupakan informasi yang tepat untuk changelog. Tidak ada entri yang terlalu detail (seharusnya ada di dokumen desain) atau terlalu umum.
- [ ] **2.4** Periksa entri-entri di **Seksi 3** secara satu per satu: apakah ada entri yang berisi spesifikasi teknis terlalu mendalam yang seharusnya ada di dokumen SRS, Architecture, atau Security Design — bukan di changelog? Jika ada, catat sebagai temuan.
- [ ] **2.5** Periksa **Seksi 4 (Rilis yang Direncanakan)**: apakah semua item roadmap yang terdaftar memang benar-benar sudah direncanakan secara eksplisit di dokumen referensi [R-01] atau [R-04]? Jika ada item yang tidak memiliki dasar referensi → catat sebagai temuan.
- [ ] **2.6** Periksa **Seksi 5 (Pedoman Penulisan)**: apakah semua pedoman yang ada di sini memang spesifik untuk changelog AbuCom dan tidak hanya menyalin isi dari dokumen Git Workflow [R-03]? Jika ada duplikasi tidak bernilai tambah → catat sebagai temuan.
- [ ] **2.7** Periksa **Seksi 6 (Glosarium)**: apakah semua istilah yang terdaftar memang digunakan di dalam dokumen ini? Jika ada istilah yang terdaftar di glosarium tetapi tidak muncul di konten dokumen → catat sebagai temuan.
- [ ] **2.8** Periksa **Seksi 7 (Referensi)**: apakah semua 14 referensi yang terdaftar memang benar-benar digunakan sebagai sumber informasi di dokumen ini? Jika ada referensi yang terdaftar tetapi tidak ada jejak penggunaannya di konten → catat sebagai temuan.

---

### TAHAP 3 — Validasi Struktur: Apakah Dokumen Memenuhi Standar Industri?

**Tujuan:** Memastikan dokumen changelog memiliki struktur yang lengkap, konsisten, dan sesuai standar praktik industri (*Keep a Changelog* dan praktik enterprise).

- [ ] **3.1** Periksa **front-matter YAML** (baris 1–8): pastikan semua field ada dan terisi: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`. Jika ada yang kosong atau tidak relevan → catat sebagai temuan.
- [ ] **3.2** Periksa **tabel Riwayat Perubahan Dokumen** (Seksi di atas Seksi 1): pastikan tabel ini ada, terformat benar, dan semua kolom terisi (`Versi`, `Tanggal`, `Deskripsi Perubahan`, `Oleh`). Jika ada sel kosong → catat sebagai temuan.
- [ ] **3.3** Verifikasi urutan hierarki heading: pastikan heading menggunakan format `#` (H1) → `##` (H2) → `###` (H3) → `####` (H4) secara konsisten tanpa ada loncatan level. Tidak ada H4 yang muncul tanpa H3 induknya.
- [ ] **3.4** Periksa apakah ada **Seksi `## [Unreleased]`** di bagian paling atas Seksi 3 (sebelum `[1.0.0]`). Menurut standar *Keep a Changelog*, seksi `[Unreleased]` adalah **wajib** untuk menampung draf perubahan berikutnya. Jika tidak ada → catat sebagai temuan dan tambahkan.
- [ ] **3.5** Periksa format heading versi di Seksi 3: apakah menggunakan format standar `### [MAJOR.MINOR.PATCH] — YYYY-MM-DD`? Pastikan format konsisten untuk semua versi yang terdaftar.
- [ ] **3.6** Periksa apakah urutan kategori perubahan di dalam Seksi 3 mengikuti urutan standar yang didefinisikan di Seksi 2.3 dan Seksi 5.3: `Added → Changed → Deprecated → Removed → Fixed → Security → Infrastructure → Documentation`. Jika urutan berbeda → catat sebagai temuan.
- [ ] **3.7** Periksa **Seksi 4 (Rilis yang Direncanakan)**: apakah format heading versi juga konsisten dengan Seksi 3? Apakah ada tanggal estimasi yang seharusnya ada tetapi tidak ada, atau ada yang memerlukan penanda `(Planned)` atau `(Estimasi)`?
- [ ] **3.8** Periksa **tabel referensi di Seksi 7**: pastikan semua kolom terisi lengkap untuk setiap baris (`Kode Ref`, `Nama Dokumen Referensi`, `Path Relatif Berkas`, `Versi`, `Prioritas`, `Peran / Hubungan`). Jika ada sel kosong atau `-` tanpa keterangan → catat sebagai temuan.
- [ ] **3.9** Periksa apakah ada **footer/penutup dokumen** di baris paling bawah. Pastikan ada kalimat penutup yang menyatakan keabsahan dokumen. Jika tidak ada → catat sebagai temuan.
- [ ] **3.10** Periksa apakah ada **horizontal rule (`---`)** sebagai pemisah antar seksi utama untuk keterbacaan. Pastikan semua seksi utama (H2) dipisahkan dengan `---`.
- [ ] **3.11** Verifikasi apakah dokumen sudah mencantumkan **tanggal rilis aktual** atau **penanda data belum tersedia** yang sesuai format `[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha setelah Go-Live]` untuk data yang memang belum ada (seperti tanggal Go-Live aktual, commit hash). Jika tanggal Go-Live masih estimasi tetapi tidak ditandai dengan jelas → catat sebagai temuan.

---

### TAHAP 4 — Validasi Kelayakan sebagai Referensi Dokumen Hilir

**Tujuan:** Memastikan dokumen ini bisa digunakan sebagai input yang memadai oleh dokumen-dokumen SDLC pada fase berikutnya (audit berkala, debugging, patch release).

- [ ] **4.1** Periksa apakah setiap entri fitur di Seksi 3 memiliki **kode referensi SRS-F-XXX** yang valid (bisa ditelusuri ke [R-05]). Jika ada entri tanpa kode referensi → catat sebagai temuan.
- [ ] **4.2** Periksa apakah setiap entri Known Issues di tabel Seksi 3 memiliki kolom **ID Masalah** dengan format `DEF-XXX` yang valid (bisa ditelusuri ke [R-14]). Jika ada baris tanpa ID atau dengan ID format tidak konsisten → catat sebagai temuan.
- [ ] **4.3** Periksa apakah penomoran versi di seluruh dokumen sudah mengikuti konvensi **SemVer** (`vMAJOR.MINOR.PATCH`) secara konsisten. Jika ada inkonsistensi format versi (misalnya `1.0` vs `v1.0` vs `v1.0.0`) → catat sebagai temuan dan tentukan format yang konsisten.
- [ ] **4.4** Periksa apakah setiap entri di Seksi 3 menggunakan **kata kerja bentuk lampau** yang tepat (Ditambahkan, Diperbaiki, Diubah, dll.) sesuai konvensi di Seksi 1.7 dan 2.3. Jika ada yang menggunakan kata kerja present tense atau bentuk tidak konsisten → catat sebagai temuan.
- [ ] **4.5** Periksa apakah setiap entri fungsional diakhiri dengan **penunjuk modul** `*(Modul M.X)*` sesuai konvensi di Seksi 1.7. Jika ada yang tidak memiliki penunjuk modul → catat sebagai temuan.
- [ ] **4.6** Periksa **Seksi 5.4 (Integrasi Git Workflow)**: apakah panduan pemetaan tipe commit (`feat`, `fix`, `docs`, `perf`, `refactor`) ke kategori changelog sudah lengkap? Apakah ada tipe commit dari [R-03] yang belum dipetakan (misal: `chore`, `test`, `build`, `ci`)? Jika ada → catat sebagai temuan.
- [ ] **4.7** Periksa apakah dokumen ini cukup mandiri sehingga pembaca baru (junior programmer atau AI model) dapat memahami konteks perubahan tanpa harus membaca semua 14 dokumen referensi. Jika ada istilah atau singkatan yang digunakan tetapi tidak ada di Seksi 1.6 Glosarium/Definisi → catat sebagai temuan.
- [ ] **4.8** Periksa apakah semua path file yang disebutkan di dalam dokumen (di Seksi 1.3, 1.4, 3, dan 7) sudah benar dan konsisten (tidak ada typo pada nama folder atau file). Bandingkan dengan hasil listing direktori aktual.

---

### TAHAP 5 — Validasi Bahasa Indonesia

**Tujuan:** Memastikan seluruh teks menggunakan Bahasa Indonesia yang natural, baku, tidak ambigu, dan mudah dipahami.

- [ ] **5.1** Baca seluruh isi dokumen target **khusus dari sisi bahasa**. Fokus pada: ketepatan pilihan kata, kejelasan kalimat, dan konsistensi terminologi.
- [ ] **5.2** Identifikasi kalimat yang terlalu panjang (lebih dari 3 klausa dalam satu kalimat) yang berpotensi membingungkan. Pecah menjadi kalimat lebih pendek jika perlu. Catat setiap kalimat yang perlu diperbaiki.
- [ ] **5.3** Periksa konsistensi penulisan istilah teknis: apakah istilah yang sama selalu ditulis dengan cara yang sama di seluruh dokumen? Contoh: pastikan tidak ada campur aduk antara `changelog`, `Changelog`, dan `CHANGELOG` dalam konteks yang sama. Catat inkonsistensi.
- [ ] **5.4** Periksa apakah ada istilah bahasa Inggris yang digunakan tanpa tanda kurung atau penjelasan padanannya (untuk istilah yang tidak ada di Seksi 1.6 Glosarium). Jika ada istilah asing baru yang belum didefinisikan → catat sebagai temuan.
- [ ] **5.5** Periksa apakah ada **campuran bahasa** yang tidak konsisten dalam satu kalimat (code-mixing tanpa pola jelas), misalnya kalimat yang setengah Indonesia setengah Inggris tanpa alasan teknis. Jika ada → catat sebagai temuan.
- [ ] **5.6** Pastikan semua instruksi dan panduan di Seksi 5 menggunakan kalimat **imperatif aktif** yang jelas (misalnya: "Tambahkan entri...", "Gunakan format...", "Pastikan..."). Hindari kalimat pasif yang ambigu.
- [ ] **5.7** Pastikan penomoran list (1, 2, 3...) dan bullet list (-) digunakan secara konsisten: gunakan **angka** untuk langkah berurutan dan **bullet** untuk item tidak berurutan.
- [ ] **5.8** Periksa typo, salah ketik, dan kesalahan ejaan di seluruh dokumen.

---

### TAHAP 6 — Validasi Data Kosong & Pengisian Data

**Tujuan:** Menemukan dan mengisi semua placeholder data kosong yang ada di dokumen.

- [ ] **6.1** Cari semua kemunculan string berikut di dokumen target dan catat lokasinya (nomor baris):
  - `[DATA BELUM TERSEDIA`
  - `[TBD]`
  - `[TODO]`
  - `XXX` (yang bukan bagian dari format contoh template)
  - `[...]`
  - Sel tabel yang berisi `-` atau kosong tanpa penjelasan
- [ ] **6.2** Untuk setiap placeholder yang ditemukan di **6.1**, tentukan apakah data tersebut bisa diisi berdasarkan informasi dari file referensi yang sudah dibaca di Tahap 0. Jika bisa → isi dengan data yang tepat dan relevan. Jika tidak bisa (membutuhkan data real-time seperti commit hash atau tanggal Go-Live aktual) → pertahankan dengan format penanda yang sudah didefinisikan di Seksi 2.5 dokumen target.
- [ ] **6.3** Periksa apakah ada kolom di tabel yang seharusnya terisi tetapi terlihat diisi dengan nilai generik atau placeholder tersembunyi (bukan format resmi). Jika ada → isi dengan data yang sesuai dari referensi.
- [ ] **6.4** Periksa `tanggal` di front-matter YAML: apakah sudah berisi tanggal revisi yang benar? Update ke tanggal revisi saat ini.
- [ ] **6.5** Periksa `status` di front-matter YAML: apakah perlu diubah dari `Draft` setelah validasi selesai? Tentukan status yang tepat berdasarkan kelengkapan konten setelah semua perbaikan.

---

### TAHAP 7 — Kompilasi Semua Temuan

**Tujuan:** Mengumpulkan semua temuan dari Tahap 1–6 sebelum menerapkan perbaikan.

- [ ] **7.1** Buat daftar terkonsolidasi semua temuan dengan format:
  ```
  [TEMUAN-X.Y] Kategori: [Kelengkapan/Relevansi/Struktur/Kelayakan/Bahasa/Data Kosong]
  Lokasi: Seksi X.Y / Baris X
  Masalah: [deskripsi masalah]
  Solusi: [deskripsi solusi yang akan diterapkan]
  ```
- [ ] **7.2** Kelompokkan temuan berdasarkan tingkat kekritisan:
  - **KRITIS:** Temuan yang membuat dokumen tidak bisa digunakan sebagai referensi (data hilang, struktur rusak, kode referensi tidak valid).
  - **PENTING:** Temuan yang mengurangi kualitas dokumen secara signifikan (data tidak lengkap, bahasa ambigu, format tidak konsisten).
  - **MINOR:** Temuan kosmetik (typo, spasi, format minor).
- [ ] **7.3** Urutkan perbaikan: selesaikan temuan **KRITIS** dulu, lalu **PENTING**, lalu **MINOR**.

---

### TAHAP 8 — Penerapan Perbaikan (Implementasi Revisi)

**Tujuan:** Menerapkan semua perbaikan berdasarkan temuan yang sudah dikompilasi.

> **ATURAN KETAT UNTUK TAHAP INI:**
> - Kerjakan perbaikan satu per satu berdasarkan urutan tingkat kekritisan (KRITIS → PENTING → MINOR).
> - Setiap perbaikan harus spesifik dan terukur. Jangan membuat perubahan yang tidak berdasarkan temuan.
> - Perubahan harus mempertahankan gaya, nada, dan terminologi yang sudah ada di dokumen.
> - Jangan menghapus konten yang sudah ada kecuali terbukti tidak relevan berdasarkan analisis Tahap 2.

- [ ] **8.1** Terapkan semua perbaikan **KRITIS** dari daftar temuan Tahap 7.
  - Untuk setiap perbaikan: tandai temuan sebagai `[SELESAI]` setelah diterapkan.
- [ ] **8.2** Terapkan semua perbaikan **PENTING** dari daftar temuan Tahap 7.
  - Untuk setiap perbaikan: tandai temuan sebagai `[SELESAI]` setelah diterapkan.
- [ ] **8.3** Terapkan semua perbaikan **MINOR** dari daftar temuan Tahap 7.
  - Untuk setiap perbaikan: tandai temuan sebagai `[SELESAI]` setelah diterapkan.
- [ ] **8.4** Jika dalam proses perbaikan kamu menemukan file referensi baru yang belum terdaftar di Seksi 7 dokumen target namun digunakan sebagai sumber informasi perbaikan, **tambahkan** referensi tersebut ke tabel Seksi 7 dengan format kolom yang sama (kode ref baru, nama dokumen, path, versi, prioritas, peran).
- [ ] **8.5** Update **tabel Riwayat Perubahan Dokumen** (di bawah front-matter, di atas Seksi 1): tambahkan baris baru untuk revisi v1.1 dengan format:
  ```
  | **1.1** | [tanggal-hari-ini] | [deskripsi singkat perubahan yang dilakukan] | Senior Technical Writer & SDLC Documentation Auditor |
  ```
- [ ] **8.6** Update **versi** di front-matter YAML: ubah `versi : 1.0` menjadi `versi : 1.1`.
- [ ] **8.7** Update **tanggal** di front-matter YAML: ubah ke tanggal hari ini.
- [ ] **8.8** Update **status** di front-matter YAML: tentukan apakah status perlu diubah (misal dari `Draft` menjadi `Review` atau `Final`).

---

### TAHAP 9 — Penulisan Ulang & Overwrite File

**Tujuan:** Menuangkan seluruh hasil dokumen yang telah direvisi ke file target dengan cara menimpa (overwrite).

> **PERINGATAN KRITIS — BACA SEBELUM MELANJUTKAN:**
> - **Tulis ulang SELURUH dokumen dari baris pertama hingga baris terakhir.** Tidak boleh ada bagian yang dipotong, diringkas, atau dihilangkan (NO TRUNCATION).
> - Jika tooling yang kamu gunakan memiliki batasan token output, bagi penulisan menjadi beberapa bagian TETAPI pastikan setiap bagian disambung tanpa kehilangan satu baris pun.
> - Verifikasi jumlah baris output ≥ jumlah baris input (karena ada penambahan konten dari perbaikan).
> - **Jangan** mengganti konten yang sudah benar dengan konten yang berbeda hanya karena terasa "lebih baik" tanpa dasar temuan.

- [ ] **9.1** Siapkan seluruh konten dokumen yang sudah direvisi dalam memori/scratchpad. Pastikan:
  - Front-matter YAML sudah diupdate (versi → 1.1, tanggal → hari ini, status → sesuai hasil Tahap 8.8).
  - Tabel Riwayat Perubahan Dokumen sudah ada baris v1.1.
  - Semua seksi (1 hingga 7) sudah memasukkan semua perbaikan dari Tahap 8.
  - Semua referensi baru (jika ada) sudah ditambahkan di Seksi 7.
  - Footer penutup dokumen ada di baris paling akhir.
- [ ] **9.2** Tulis ulang seluruh konten dokumen ke file `docs/sdlc/07_maintenance/02_changelog.md` dengan mode **overwrite** (timpa seluruh isi file).
- [ ] **9.3** Setelah penulisan selesai, baca kembali file yang sudah ditulis dari baris pertama hingga baris terakhir untuk memverifikasi tidak ada konten yang terpotong.
- [ ] **9.4** Hitung jumlah baris file baru. Pastikan jumlah baris baru ≥ jumlah baris file asli (368 baris). Jika lebih sedikit → ada konten yang hilang, ulangi dari **9.1**.
- [ ] **9.5** Verifikasi bahwa bagian `versi` di front-matter sudah berubah dari `1.0` menjadi `1.1`.
- [ ] **9.6** Verifikasi bahwa baris terakhir dokumen bukan baris kosong tanpa footer.

---

### TAHAP 10 — Verifikasi Akhir (Post-Write Validation)

**Tujuan:** Melakukan pengecekan akhir untuk memastikan semua perbaikan sudah diterapkan dengan benar.

- [ ] **10.1** Baca ulang seluruh dokumen yang sudah ditulis. Centang setiap poin berikut:
  - [ ] Front-matter YAML terisi lengkap dan versi adalah `1.1`.
  - [ ] Tabel Riwayat Perubahan Dokumen memiliki setidaknya 2 baris (v1.0 dan v1.1).
  - [ ] Seksi 1.1 hingga 1.7 ada dan terisi lengkap.
  - [ ] Seksi 2.1 hingga 2.5 ada dan terisi lengkap.
  - [ ] Seksi 3 berisi semua entri `Added`, `Security`, `Infrastructure`, `Documentation`, `Known Limitations`, `Known Issues`.
  - [ ] Seksi 4 berisi roadmap v1.1.0 dan v2.0.0.
  - [ ] Seksi 5.1 hingga 5.4 ada dan terisi lengkap.
  - [ ] Seksi 6 berisi glosarium yang lengkap.
  - [ ] Seksi 7 berisi tabel referensi lengkap (minimal 14 referensi, atau lebih jika ada referensi baru yang ditambahkan).
  - [ ] Footer penutup ada di baris paling akhir.
- [ ] **10.2** Lakukan pencarian string di file hasil untuk memastikan tidak ada placeholder yang tertinggal:
  - Cari: `[TBD]` → harus tidak ditemukan.
  - Cari: `[TODO]` → harus tidak ditemukan.
  - Cari: `SRS-F-XXX` di luar konteks template/contoh → harus tidak ditemukan.
  - Cari: `DEF-XXX` di luar konteks template/contoh → harus tidak ditemukan.
- [ ] **10.3** Verifikasi bahwa semua kode SRS-F-XXX yang ada di entri Seksi 3 bisa ditelusuri ke dokumen [R-05].
- [ ] **10.4** Verifikasi bahwa semua ID bug DEF-XXX yang ada di tabel Known Issues bisa ditelusuri ke dokumen [R-14].
- [ ] **10.5** Pastikan tidak ada heading yang melayang tanpa konten (heading diikuti langsung oleh heading berikutnya tanpa isi apapun).
- [ ] **10.6** Buat laporan ringkas hasil validasi dengan format berikut dan **tampilkan di output** (jangan simpan ke file terpisah):

  ```
  ═══════════════════════════════════════════════
  LAPORAN HASIL VALIDASI CHANGELOG v1.0 → v1.1
  ═══════════════════════════════════════════════
  Tanggal Validasi   : [tanggal]
  File Target        : docs/sdlc/07_maintenance/02_changelog.md
  Versi Sebelumnya   : 1.0
  Versi Sesudahnya   : 1.1
  -----------------------------------------------
  Total Temuan KRITIS   : [N]
  Total Temuan PENTING  : [N]
  Total Temuan MINOR    : [N]
  Total Temuan          : [N]
  -----------------------------------------------
  Temuan yang Diperbaiki: [N]
  Data Kosong Diisi     : [N]
  Referensi Baru Ditambahkan: [N] (jika ada)
  -----------------------------------------------
  Status Akhir       : SELESAI / MEMERLUKAN TINDAK LANJUT
  ═══════════════════════════════════════════════
  ```

---

## Kriteria Keberhasilan (Definition of Done)

Issue ini dinyatakan **SELESAI** apabila **semua** kondisi berikut terpenuhi:

- [ ] Seluruh 10 tahap di atas telah diselesaikan tanpa ada langkah yang dilewati.
- [ ] File `docs/sdlc/07_maintenance/02_changelog.md` berhasil dioverwrite dengan versi 1.1.
- [ ] Jumlah baris file hasil ≥ 368 baris (jumlah baris file asli).
- [ ] Tidak ada placeholder `[TBD]`, `[TODO]`, atau `SRS-F-XXX`/`DEF-XXX` di luar konteks template yang tertinggal.
- [ ] Semua SRS-F-XXX yang disebut di Seksi 3 valid dan bisa ditelusuri ke [R-05].
- [ ] Semua DEF-XXX yang disebut di tabel Known Issues valid dan bisa ditelusuri ke [R-14].
- [ ] Versi dokumen di front-matter berubah dari `1.0` menjadi `1.1`.
- [ ] Tabel Riwayat Perubahan Dokumen memiliki baris baru untuk v1.1.
- [ ] Laporan ringkas hasil validasi telah ditampilkan di output.

---

## Hal-hal yang DILARANG (Anti-Pattern)

> **JANGAN** melakukan hal-hal berikut. Ini akan dianggap sebagai kegagalan eksekusi:

- ❌ Melewati salah satu tahap implementasi.
- ❌ Memotong, meringkas, atau menghilangkan konten apapun saat menulis ulang file.
- ❌ Menulis ulang file sebelum semua tahap analisis (Tahap 0–7) selesai.
- ❌ Menambahkan opini subjektif atau konten baru yang tidak berdasarkan temuan dari referensi.
- ❌ Mengubah terminologi kunci proyek (nama modul, nama tabel, kode SRS-F-XXX) tanpa dasar dari referensi.
- ❌ Menganggap sesuatu sudah benar tanpa memverifikasinya langsung dari file referensi.
- ❌ Mengisi data kosong dengan informasi yang dikarang/dihipotesiskan tanpa dasar dari referensi.
- ❌ Membuat file baru atau memindahkan file — hanya **overwrite** file target yang diizinkan.

---

*Issue ini dibuat pada 2026-05-28 sebagai instruksi low-level untuk validasi dan perbaikan dokumen Changelog AbuCom v1.0 → v1.1.*
