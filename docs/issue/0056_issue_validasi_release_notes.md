# Validasi, Analisis & Penyempurnaan Dokumen Release Notes

---

## Metadata Issue

| Field              | Detail                                                              |
| :----------------- | :------------------------------------------------------------------ |
| **Judul**          | Validasi, Analisis & Penyempurnaan Dokumen Release Notes            |
| **Tipe**           | Documentation Review & Validation                                   |
| **Prioritas**      | 🔴 High                                                             |
| **Status**         | Open                                                                |
| **Assignee**       | Junior Programmer / LLM Model AI                                    |
| **Dibuat oleh**    | Antigravity (Senior DevOps Lead)                                    |
| **Tanggal Dibuat** | 2026-05-27                                                          |
| **Target File**    | `docs/sdlc/06_deployment/03_release_notes.md`                       |
| **Lokasi Referensi** | `docs/sdlc/`                                                      |

---

## 1. Latar Belakang & Konteks

Dokumen **Release Notes v1.0** (`docs/sdlc/06_deployment/03_release_notes.md`) telah selesai dibuat pada fase awal penyusunan. Dokumen ini mencakup **19 bab utama** yang mendokumentasikan rilis perdana sistem aplikasi **AbuCom CLI v1.0.0** — sistem manajemen terpadu berbasis CLI untuk usaha percetakan.

Issue ini dibuat untuk memastikan bahwa dokumen Release Notes tersebut:
- Tidak ada data yang terlewat dari dokumen referensi sumbernya.
- Tidak mengandung konten yang tidak relevan atau tidak seharusnya ada di dokumen Release Notes.
- Memiliki struktur dokumen yang sesuai standar industri.
- Layak dijadikan acuan resmi input bagi fase SDLC berikutnya.
- Menggunakan bahasa Indonesia yang natural, jelas, dan tidak ambigu.
- Bebas dari data kosong yang seharusnya bisa diisi dari konteks yang tersedia.

Dokumen ini mereferensikan **16 berkas dokumentasi SDLC AbuCom** yang tertera pada Bab 19 (Referensi Dokumen) sebagai sumber primer, sekunder, dan tersier.

---

## 2. Persona Validator

> **INSTRUKSI WAJIB:** Sebelum memulai pekerjaan apa pun, adopsi dan pertahankan persona berikut ini secara penuh selama seluruh proses validasi berlangsung.

Kamu adalah seorang **Senior Technical Documentation Auditor & Release Engineering Specialist** dengan pengalaman lebih dari 12 tahun di bidang:

- **Release Management:** Menyusun, memeriksa, dan memvalidasi dokumen Release Notes untuk produk perangkat lunak enterprise dan startup teknologi.
- **SDLC Governance:** Memastikan keterkaitan dan konsistensi antar-dokumen dalam siklus hidup pengembangan sistem (SDLC) secara end-to-end.
- **Technical Writing Standard:** Menerapkan standar dokumentasi teknis industri seperti yang digunakan oleh tim engineering Google, Microsoft, HashiCorp, dan Atlassian.
- **Quality Gate Reviewer:** Bertugas sebagai penjaga gerbang kualitas dokumen yang tidak meloloskan dokumen jika ada celah informasi, ketidakkonsistenan data, atau ambiguitas bahasa.
- **Security & Compliance Aware:** Memahami konteks keamanan (bcrypt, JWT, Fernet, AES-256, RBAC) dan kepatuhan regulasi (UU PDP No. 27/2022) yang relevan dengan dokumen ini.

Kamu dikenal sangat ketat, tidak mentoleransi ketidaklengkapan data, dan selalu memastikan setiap dokumen yang kamu validasi bisa dijadikan **satu-satunya sumber kebenaran** yang dapat dipercaya tanpa perlu selalu dikonfirmasi ulang.

---

## 3. Dokumen yang Terlibat

### 3.1. Target File (Dokumen Utama yang Divalidasi)

```
docs/sdlc/06_deployment/03_release_notes.md
```

### 3.2. File Referensi (16 Dokumen Sumber)

| Kode | Path File                                            | Prioritas  |
| :--: | :--------------------------------------------------- | :--------: |
| R-01 | `docs/sdlc/01_planning/01_project_charter.md`        | PRIMER     |
| R-02 | `docs/sdlc/02_analysis/02_software_requirements.md`  | PRIMER     |
| R-03 | `docs/sdlc/06_deployment/01_deployment_guide.md`     | PRIMER     |
| R-04 | `docs/sdlc/06_deployment/02_environment_config.yaml` | PRIMER     |
| R-05 | `docs/sdlc/05_testing/01_test_plan.md`               | PRIMER     |
| R-06 | `docs/sdlc/03_design/03_system_architecture.md`      | SEKUNDER   |
| R-07 | `docs/sdlc/03_design/06_security_design.md`          | SEKUNDER   |
| R-08 | `docs/sdlc/01_planning/04_tech_stack_decision.md`    | SEKUNDER   |
| R-09 | `docs/sdlc/03_design/01_database_schema.sql`         | SEKUNDER   |
| R-10 | `docs/sdlc/04_implementation/03_module_structure.md` | SEKUNDER   |
| R-11 | `docs/sdlc/04_implementation/04_git_workflow.md`     | SEKUNDER   |
| R-12 | `docs/sdlc/05_testing/02_test_cases.md`              | TERSIER    |
| R-13 | `docs/sdlc/05_testing/03_uat_script.md`              | TERSIER    |
| R-14 | `docs/sdlc/05_testing/04_bug_report_template.md`     | TERSIER    |
| R-15 | `docs/sdlc/02_analysis/06_access_control_matrix.md`  | TERSIER    |
| R-16 | `docs/sdlc/04_implementation/01_coding_standard.md`  | TERSIER    |

---

## 4. Kriteria Validasi (Acceptance Criteria)

Dokumen Release Notes dinyatakan **LULUS VALIDASI** hanya jika memenuhi semua kriteria berikut:

| ID Kriteria | Deskripsi Kriteria Validasi                                                                                   | Status    |
| :---------: | :------------------------------------------------------------------------------------------------------------ | :-------: |
| **KV-01**   | Seluruh data kunci dari 16 dokumen referensi yang relevan dengan Release Notes sudah terangkum di dokumen.    | [ ] Belum |
| **KV-02**   | Tidak ada konten yang tidak relevan / tidak seharusnya ada di dokumen Release Notes yang ikut tercantum.      | [ ] Belum |
| **KV-03**   | Struktur 19 bab dokumen sesuai standar industri Release Notes yang komprehensif dan informatif.               | [ ] Belum |
| **KV-04**   | Dokumen layak sebagai referensi input primer bagi fase-fase SDLC berikutnya (User Manual, Serah Terima, dll). | [ ] Belum |
| **KV-05**   | Seluruh teks menggunakan bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, mudah dipahami.    | [ ] Belum |
| **KV-06**   | Kualitas kelengkapan isi tidak akan menimbulkan pertanyaan ulang yang menghambat pekerjaan fase SDLC berikutnya. | [ ] Belum |
| **KV-07**   | Tidak ada field data kosong yang bisa diisi dari konteks dokumen referensi yang tersedia.                     | [ ] Belum |
| **KV-08**   | Nomor versi dokumen diperbarui (dari v1.0 menjadi v1.1) sebagai tanda telah direvisi.                        | [ ] Belum |
| **KV-09**   | Seluruh teks dokumen ditulis ulang penuh tanpa ada pemotongan, peringkasan, atau penghilangan konten.         | [ ] Belum |
| **KV-10**   | Jika ada referensi baru yang digunakan saat perbaikan, tercantum di bagian akhir Bab 19.                     | [ ] Belum |

---

## 5. Tahapan Implementasi (Low-Level Checklist)

> **PERINGATAN PENTING:** Ikuti setiap tahapan di bawah ini secara **berurutan dari atas ke bawah** tanpa melewatkan satu pun langkah. Jangan lakukan asumsi. Jika sebuah instruksi memerintahkan untuk membaca file, baca file tersebut secara penuh sebelum melanjutkan ke langkah berikutnya.

---

### FASE 0 — PERSIAPAN & ORIENTASI

- [ ] **[0.1]** Baca secara penuh dan seksama file target utama:
  ```
  docs/sdlc/06_deployment/03_release_notes.md
  ```
  Baca dari **baris pertama hingga baris terakhir** tanpa melewatkan satu baris pun. Tandai dalam catatan kerjamu bahwa file ini adalah **"Dokumen Utama"** yang akan divalidasi.

- [ ] **[0.2]** Catat struktur bab dokumen utama yang ada saat ini (dari Bab 1 hingga Bab 19). Verifikasi apakah semua 19 bab sudah hadir.

- [ ] **[0.3]** Baca secara penuh **5 dokumen referensi PRIMER** satu per satu dalam urutan berikut:
  - [ ] **[0.3.a]** Baca `docs/sdlc/01_planning/01_project_charter.md` (R-01) dari awal hingga akhir.
  - [ ] **[0.3.b]** Baca `docs/sdlc/02_analysis/02_software_requirements.md` (R-02) dari awal hingga akhir.
  - [ ] **[0.3.c]** Baca `docs/sdlc/06_deployment/01_deployment_guide.md` (R-03) dari awal hingga akhir.
  - [ ] **[0.3.d]** Baca `docs/sdlc/06_deployment/02_environment_config.yaml` (R-04) dari awal hingga akhir.
  - [ ] **[0.3.e]** Baca `docs/sdlc/05_testing/01_test_plan.md` (R-05) dari awal hingga akhir.

- [ ] **[0.4]** Baca secara penuh **6 dokumen referensi SEKUNDER** satu per satu dalam urutan berikut:
  - [ ] **[0.4.a]** Baca `docs/sdlc/03_design/03_system_architecture.md` (R-06) dari awal hingga akhir.
  - [ ] **[0.4.b]** Baca `docs/sdlc/03_design/06_security_design.md` (R-07) dari awal hingga akhir.
  - [ ] **[0.4.c]** Baca `docs/sdlc/01_planning/04_tech_stack_decision.md` (R-08) dari awal hingga akhir.
  - [ ] **[0.4.d]** Baca `docs/sdlc/03_design/01_database_schema.sql` (R-09) dari awal hingga akhir.
  - [ ] **[0.4.e]** Baca `docs/sdlc/04_implementation/03_module_structure.md` (R-10) dari awal hingga akhir.
  - [ ] **[0.4.f]** Baca `docs/sdlc/04_implementation/04_git_workflow.md` (R-11) dari awal hingga akhir.

- [ ] **[0.5]** Baca secara penuh **5 dokumen referensi TERSIER** satu per satu dalam urutan berikut:
  - [ ] **[0.5.a]** Baca `docs/sdlc/05_testing/02_test_cases.md` (R-12) dari awal hingga akhir.
  - [ ] **[0.5.b]** Baca `docs/sdlc/05_testing/03_uat_script.md` (R-13) dari awal hingga akhir.
  - [ ] **[0.5.c]** Baca `docs/sdlc/05_testing/04_bug_report_template.md` (R-14) dari awal hingga akhir.
  - [ ] **[0.5.d]** Baca `docs/sdlc/02_analysis/06_access_control_matrix.md` (R-15) dari awal hingga akhir.
  - [ ] **[0.5.e]** Baca `docs/sdlc/04_implementation/01_coding_standard.md` (R-16) dari awal hingga akhir.

---

### FASE 1 — VALIDASI KELENGKAPAN DATA (KV-01)

> **Tujuan:** Memastikan dokumen utama sudah merangkum SEMUA data dan informasi penting yang relevan dari 16 dokumen referensi. Tidak boleh ada data kunci yang terlewat.

- [ ] **[1.1]** Komparasi Bab 2 (Ringkasan Rilis) dengan R-01 (Project Charter):
  - [ ] **[1.1.a]** Verifikasi nama produk, nomor versi, dan tipe rilis sudah sesuai dengan Project Charter.
  - [ ] **[1.1.b]** Verifikasi tanggal rilis — jika Project Charter mencantumkan tanggal milestone go-live, gunakan data itu. Jika tidak tersedia, pertahankan placeholder dengan catatan yang tepat.
  - [ ] **[1.1.c]** Verifikasi deskripsi umum rilis mencakup konteks penggantian sistem Excel ke CLI sesuai visi di Project Charter.
  - [ ] **[1.1.d]** Verifikasi highlight fitur utama di Bab 2.5 sudah mencerminkan seluruh modul besar yang disebut di Project Charter.

- [ ] **[1.2]** Komparasi Bab 4 (Fitur Baru) dengan R-02 (SRS):
  - [ ] **[1.2.a]** Periksa apakah semua ID kebutuhan fungsional dari SRS-F-001 hingga SRS-F-040 beserta SRS-F-ADD-01 s.d SRS-F-ADD-05 sudah tercantum di Bab 4.
  - [ ] **[1.2.b]** Verifikasi nama, deskripsi, dan detail teknis setiap fitur SRS di Bab 4 konsisten dengan isi R-02 (tidak ada perbedaan nilai nominal, parameter, atau logika bisnis).
  - [ ] **[1.2.c]** Periksa apakah ada fitur di R-02 yang belum tercantum atau terlewat di Bab 4.

- [ ] **[1.3]** Komparasi Bab 3 (Persyaratan Sistem) dengan R-06 (System Architecture):
  - [ ] **[1.3.a]** Verifikasi spesifikasi hardware server dan klien kasir sudah sesuai dengan R-06.
  - [ ] **[1.3.b]** Verifikasi topologi jaringan LAN, switch, router, dan IP yang tertera di Bab 3.3 sesuai dengan R-06.

- [ ] **[1.4]** Komparasi Bab 5 (Fitur Keamanan) dengan R-07 (Security Design):
  - [ ] **[1.4.a]** Verifikasi parameter bcrypt (cost factor 12, salt 16 bytes) sesuai R-07.
  - [ ] **[1.4.b]** Verifikasi parameter JWT (HS256, 8 jam / 28.800 detik) sesuai R-07.
  - [ ] **[1.4.c]** Verifikasi matriks RBAC 8 peran di Bab 5.2 sudah sesuai dan konsisten dengan R-02 dan R-15. Periksa apakah ada baris peran atau kolom menu yang terlewat.
  - [ ] **[1.4.d]** Verifikasi detail hardening infrastruktur (UFW rules, chmod 700, AutoPlay registry, mysqldump passwordless, AES-256 ZIP backup) sesuai R-07 dan R-03.

- [ ] **[1.5]** Komparasi Bab 9 (Panduan Instalasi) dengan R-03 (Deployment Guide):
  - [ ] **[1.5.a]** Verifikasi prosedur setup server Debian 12 di Bab 9.1.1 sudah mencakup seluruh langkah kritis dari R-03 (IP statis, UFW rules, Python compile, MySQL install, bind-address, schema import, user DB, cron backup).
  - [ ] **[1.5.b]** Verifikasi prosedur setup klien Windows 11 di Bab 9.1.2 sudah mencakup OS hardening, instalasi Python, copy venv, konfigurasi `.env`, dan setup printer sesuai R-03.
  - [ ] **[1.5.c]** Verifikasi prosedur rollback (restore database dan kode klien) sudah lengkap dan akurat.

- [ ] **[1.6]** Komparasi Bab 10 (Konfigurasi Default) dengan R-04 (Environment Config):
  - [ ] **[1.6.a]** Verifikasi semua parameter produksi di Bab 10.1 (DB host, port, pool size, retry, logging level) sesuai R-04.
  - [ ] **[1.6.b]** Verifikasi semua parameter keamanan di Bab 10.2 sesuai R-04.
  - [ ] **[1.6.c]** Verifikasi semua baris tabel Runtime Config di Bab 10.4 sudah lengkap — tidak ada parameter yang ada di R-04 namun terlewat dari tabel ini. Jika ada parameter yang terlewat, tambahkan.

- [ ] **[1.7]** Komparasi Bab 11 (QA Summary) dengan R-05 (Test Plan):
  - [ ] **[1.7.a]** Verifikasi bahwa Bab 11 sudah menyebut strategi testing (unit, integrasi, UAT) sesuai pendekatan di R-05.
  - [ ] **[1.7.b]** Verifikasi referensi ke Test Plan di Bab 11.5 sudah mengarah ke path file yang benar.
  - [ ] **[1.7.c]** Periksa apakah ada exit criteria dari R-05 yang seharusnya disebut namun terlewat.

- [ ] **[1.8]** Komparasi Bab 12 (Arsitektur & Topologi) dengan R-06 (System Architecture):
  - [ ] **[1.8.a]** Verifikasi diagram Mermaid di Bab 12.1 mencerminkan topologi node yang benar (server, kasir, switch, router, UPS, printer, laci kasir).
  - [ ] **[1.8.b]** Verifikasi matriks komponen per node di Bab 12.2 sudah lengkap mencakup semua pustaka utama yang tertera di R-08 (Tech Stack Decision) dan R-02 (SRS).

- [ ] **[1.9]** Komparasi Bab 13 (Matriks Risiko) dengan R-03 (Deployment Guide):
  - [ ] **[1.9.a]** Verifikasi 8 risiko yang tercantum di Bab 13 sudah sesuai dengan daftar risiko deployment di R-03.
  - [ ] **[1.9.b]** Verifikasi setiap nilai probabilitas (Prob), dampak, skor risiko, mitigasi, dan kontingensi sudah akurat dan konsisten dengan R-03.

- [ ] **[1.10]** Komparasi Bab 14 (Tim Pengembang) dengan R-01 (Project Charter):
  - [ ] **[1.10.a]** Verifikasi daftar nama anggota tim, peran, dan tanggung jawab sudah sesuai dengan susunan tim di Project Charter.
  - [ ] **[1.10.b]** Verifikasi matriks RACI di Bab 14.2 sudah mencerminkan aktivitas dan penugasan yang sesuai dengan struktur proyek di R-01.

- [ ] **[1.11]** Komparasi Bab 19 (Referensi Dokumen) dengan kondisi aktual file sistem:
  - [ ] **[1.11.a]** Verifikasi semua 16 path file referensi yang tercantum di Bab 19 adalah path yang valid dan benar (cek dengan membandingkan apa yang sudah dibaca di Fase 0).
  - [ ] **[1.11.b]** Verifikasi versi semua dokumen referensi di Bab 19 konsisten dengan versi aktual dokumen yang ada.

---

### FASE 2 — VALIDASI RELEVANSI KONTEN (KV-02)

> **Tujuan:** Memastikan dokumen utama HANYA berisi konten yang relevan dan sesuai spesifik untuk dokumen Release Notes. Bersihkan konten yang tidak seharusnya ada.

- [ ] **[2.1]** Periksa seluruh isi Bab 4 (Fitur Baru):
  - [ ] **[2.1.a]** Pastikan setiap fitur yang dicantumkan adalah fitur yang **dirilis pada v1.0.0** — bukan fitur rencana masa depan. Fitur rencana masa depan harus dipindahkan ke Bab 15 (Roadmap).
  - [ ] **[2.1.b]** Pastikan level detail deskripsi fitur di Bab 4 sudah proporsional — tidak terlalu singkat (tidak informatif) dan tidak terlalu panjang seperti SRS (bukan tempat spesifikasi teknis mendalam).

- [ ] **[2.2]** Periksa Bab 9 (Panduan Instalasi):
  - [ ] **[2.2.a]** Pastikan Bab 9 hanya berisi **ringkasan prosedur utama** dan bukan duplikasi lengkap dari Deployment Guide. Detail teknis mendalam harus tetap dirujuk ke R-03, bukan diduplikasi penuh di sini.
  - [ ] **[2.2.b]** Verifikasi bahwa prosedur yang ada di Bab 9 sudah cukup untuk memandu seseorang memahami alur instalasi tanpa harus membuka dokumen lain terlebih dahulu.

- [ ] **[2.3]** Periksa Bab 10 (Konfigurasi Default):
  - [ ] **[2.3.a]** Pastikan Bab 10 hanya memuat parameter konfigurasi yang relevan dengan **kondisi default produksi**, bukan seluruh isi environment config.
  - [ ] **[2.3.b]** Pastikan tidak ada parameter konfigurasi yang bersifat development/testing ikut tercantum di sini.

- [ ] **[2.4]** Periksa Bab 6 (Bug Fixes & Improvements):
  - [ ] **[2.4.a]** Karena ini rilis perdana (v1.0.0), pastikan konten Bab 6.1 (daftar bug yang diperbaiki) sudah memberikan penjelasan yang tepat dan tidak membingungkan — jelas bahwa tidak ada bug rilis produksi sebelumnya yang diperbaiki.
  - [ ] **[2.4.b]** Verifikasi peningkatan performa dan antarmuka yang disebut di Bab 6.2 dan 6.3 adalah peningkatan yang **sudah diimplementasikan** di v1.0.0, bukan rencana.

---

### FASE 3 — VALIDASI STRUKTUR DOKUMEN (KV-03)

> **Tujuan:** Memastikan struktur 19 bab dokumen Release Notes sudah sesuai dengan standar industri, lengkap, dan informatif.

- [ ] **[3.1]** Periksa apakah struktur bab dokumen sudah mencakup komponen standar dokumen Release Notes tingkat enterprise:
  - [ ] **[3.1.a]** Riwayat perubahan dokumen (Document History / Changelog).
  - [ ] **[3.1.b]** Informasi produk & versi yang jelas (nama, versi, tipe, tanggal, deskripsi).
  - [ ] **[3.1.c]** Persyaratan sistem (hardware, software, jaringan).
  - [ ] **[3.1.d]** Daftar fitur baru yang dirilis (New Features).
  - [ ] **[3.1.e]** Fitur keamanan (Security Features).
  - [ ] **[3.1.f]** Perbaikan bug dan peningkatan (Bug Fixes & Improvements).
  - [ ] **[3.1.g]** Batasan yang diketahui (Known Limitations).
  - [ ] **[3.1.h]** Masalah yang diketahui (Known Issues).
  - [ ] **[3.1.i]** Panduan instalasi dan upgrade.
  - [ ] **[3.1.j]** Konfigurasi default rilis.
  - [ ] **[3.1.k]** Ringkasan hasil pengujian kualitas (QA Summary).
  - [ ] **[3.1.l]** Diagram arsitektur deployment.
  - [ ] **[3.1.m]** Matriks risiko rilis.
  - [ ] **[3.1.n]** Informasi tim pengembang dan RACI matrix.
  - [ ] **[3.1.o]** Roadmap rilis berikutnya.
  - [ ] **[3.1.p]** Kontak dukungan teknis dan eskalasi.
  - [ ] **[3.1.q]** Halaman persetujuan dan otorisasi rilis (Approval Page).
  - [ ] **[3.1.r]** Glosarium istilah teknis.
  - [ ] **[3.1.s]** Daftar referensi dokumen yang digunakan.

- [ ] **[3.2]** Verifikasi kerapihan header dokumen YAML front matter:
  - [ ] **[3.2.a]** Pastikan field `versi` di YAML front matter sudah diperbarui dari `1.0` menjadi `1.1`.
  - [ ] **[3.2.b]** Pastikan field `tanggal` di YAML front matter sudah mencerminkan tanggal revisi terkini.
  - [ ] **[3.2.c]** Pastikan field `status` diperbarui jika ada perubahan status dari Draft menjadi Revised atau tetap Draft (sesuaikan dengan konteks).

- [ ] **[3.3]** Periksa konsistensi penomoran:
  - [ ] **[3.3.a]** Pastikan semua nomor bab dan sub-bab terurut dengan benar dan tidak ada yang loncat.
  - [ ] **[3.3.b]** Pastikan semua ID referensi (R-01 s.d R-16) digunakan secara konsisten di seluruh dokumen.
  - [ ] **[3.3.c]** Pastikan semua ID risiko (RSK-01 s.d RSK-08) konsisten.
  - [ ] **[3.3.d]** Pastikan semua ID fitur (SRS-F-001 s.d SRS-F-040, SRS-F-ADD-01 s.d SRS-F-ADD-05) konsisten.

- [ ] **[3.4]** Periksa kelengkapan elemen visual dan navigasi:
  - [ ] **[3.4.a]** Pastikan setiap bab dipisahkan dengan garis horizontal `---`.
  - [ ] **[3.4.b]** Pastikan semua tabel memiliki header yang jelas dan data yang terisi.
  - [ ] **[3.4.c]** Pastikan diagram Mermaid di Bab 12.1 dapat dirender dengan sintaks yang valid.
  - [ ] **[3.4.d]** Pastikan semua blok kode memiliki label bahasa yang tepat (sql, text, mermaid, dll).

- [ ] **[3.5]** Periksa apakah ada bab atau sub-bab penting yang **seharusnya ada** di dokumen Release Notes industri namun belum tercantum:
  - [ ] **[3.5.a]** **Hypercare Period:** Dokumen Release Notes tingkat enterprise umumnya menyebutkan periode hypercare (periode support intensif pasca go-live). Periksa apakah ini perlu ditambahkan sebagai sub-bab di Bab 15 atau Bab 16.
  - [ ] **[3.5.b]** **Changelog Format:** Verifikasi riwayat perubahan dokumen di bagian atas cukup menggambarkan evolusi dokumen ini.
  - [ ] **[3.5.c]** **Disclaimer / Catatan Hukum:** Untuk dokumen enterprise, pertimbangkan apakah perlu ada catatan disclaimer singkat terkait kerahasiaan dokumen internal.

---

### FASE 4 — VALIDASI KELAYAKAN SEBAGAI INPUT SDLC BERIKUTNYA (KV-04)

> **Tujuan:** Memastikan dokumen ini dapat berdiri sendiri sebagai input primer yang lengkap dan tidak ambigu bagi dokumen-dokumen fase SDLC selanjutnya.

- [ ] **[4.1]** Identifikasi dokumen SDLC yang akan mengonsumsi Release Notes ini sebagai input:
  - [ ] **[4.1.a]** **User Manual / Buku Panduan Pengguna:** Periksa apakah Bab 4 (Fitur Baru) dan Bab 5 (Keamanan) sudah cukup informatif untuk menjadi acuan tim penulis User Manual. Apakah nama fitur, alur, dan terminologinya konsisten?
  - [ ] **[4.1.b]** **Berita Acara Serah Terima Sistem:** Periksa apakah Bab 17 (Persetujuan) sudah memuat semua pihak yang relevan dan format yang tepat untuk dijadikan lampiran berita acara.
  - [ ] **[4.1.c]** **Training Material / Materi Pelatihan Kasir:** Periksa apakah Bab 7 (Known Limitations) dan Bab 16 (Kontak Dukungan) sudah cukup lengkap untuk membantu penyusunan materi pelatihan kasir.

- [ ] **[4.2]** Verifikasi semua tautan lintas dokumen di seluruh bab:
  - [ ] **[4.2.a]** Temukan setiap hyperlink atau referensi path dokumen di dalam dokumen utama (format `[nama](path)`).
  - [ ] **[4.2.b]** Pastikan setiap path yang direferensikan sudah benar dan file-nya ada di sistem (bandingkan dengan daftar file yang sudah dibaca di Fase 0).

- [ ] **[4.3]** Verifikasi kemandirian informasi:
  - [ ] **[4.3.a]** Seseorang yang membaca Release Notes ini tanpa akses ke 16 dokumen referensi harus sudah mendapat gambaran lengkap tentang: apa yang dirilis, apa kebutuhannya, bagaimana menginstalasinya, apa batasannya, dan siapa yang bertanggung jawab.
  - [ ] **[4.3.b]** Jika ada informasi penting yang hanya bisa dipahami dengan membuka dokumen referensi, tambahkan ringkasan atau kutipan langsung yang tepat di dokumen utama.

---

### FASE 5 — VALIDASI BAHASA INDONESIA (KV-05)

> **Tujuan:** Memastikan seluruh teks menggunakan bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau LLM lain yang lebih murah.

- [ ] **[5.1]** Baca ulang seluruh dokumen dengan fokus pada kualitas bahasa:
  - [ ] **[5.1.a]** Identifikasi kalimat yang terlalu panjang (lebih dari 3 klausa dalam 1 kalimat) dan pecah menjadi kalimat yang lebih pendek dan jelas.
  - [ ] **[5.1.b]** Identifikasi istilah teknis bahasa Inggris yang digunakan tanpa padanan atau penjelasan bahasa Indonesia — pastikan setiap istilah teknis asing sudah dijelaskan di Bab 1.6 (Definisi & Akronim) atau Bab 18 (Glosarium).
  - [ ] **[5.1.c]** Periksa konsistensi penggunaan istilah teknis — misalnya, jika "kasir" di satu tempat dan "staf kasir" di tempat lain, pastikan dipilih satu terminologi konsisten.
  - [ ] **[5.1.d]** Periksa tidak ada typo, salah eja, atau salah tata bahasa yang signifikan.

- [ ] **[5.2]** Periksa Bab 18 (Glosarium):
  - [ ] **[5.2.a]** Pastikan semua istilah teknis yang digunakan di seluruh dokumen sudah ada entri glosariumnya.
  - [ ] **[5.2.b]** Jika ada istilah teknis yang digunakan berulang di dokumen namun belum ada di glosarium, tambahkan entri baru di Bab 18.
  - [ ] **[5.2.c]** Pastikan setiap definisi di glosarium sudah jelas dan mudah dipahami oleh non-teknis (seperti Kepala Percetakan atau Pemilik Usaha).

- [ ] **[5.3]** Periksa Bab 1.6 (Definisi, Akronim, dan Singkatan):
  - [ ] **[5.3.a]** Pastikan daftar akronim di Bab 1.6 tidak ada yang overlap atau duplikat dengan Bab 18 (Glosarium). Keduanya boleh ada, tapi harus komplemen — Bab 1.6 untuk akronim singkat, Bab 18 untuk definisi lengkap.

---

### FASE 6 — VALIDASI KELENGKAPAN YANG TIDAK AMBIGU (KV-06)

> **Tujuan:** Memastikan kualitas isi dokumen tidak akan selalu dipertanyakan atau diinterupsi yang berpotensi menghambat fase SDLC berikutnya.

- [ ] **[6.1]** Periksa Bab 2.2 (Tanggal Rilis):
  - [ ] **[6.1.a]** Saat ini Bab 2.2 masih berisi placeholder `[DATA BELUM TERSEDIA...]`. Periksa apakah dari Project Charter (R-01) ada data milestone tanggal go-live yang bisa digunakan.
  - [ ] **[6.1.b]** Jika dari R-01 tersedia estimasi tanggal, ganti placeholder dengan data tersebut beserta catatan "(Estimasi, konfirmasi setelah UAT sign-off)".
  - [ ] **[6.1.c]** Jika tidak tersedia sama sekali dari referensi manapun, pertahankan placeholder namun perbaiki redaksinya agar lebih informatif dan tidak terkesan data hilang.

- [ ] **[6.2]** Periksa Bab 8 (Known Issues):
  - [ ] **[6.2.a]** Saat ini Bab 8 berisi placeholder `[DATA BELUM TERSEDIA...]`. Periksa apakah dari R-14 (Bug Report Template) ada template atau daftar known issues yang bisa digunakan.
  - [ ] **[6.2.b]** Jika tidak ada data known issues aktual, buat konten yang **informatif dan tidak kosong** — misalnya, tambahkan penjelasan mengapa belum ada data, kapan data ini akan diisi, dan siapa penanggung jawabnya. Ganti placeholder dengan paragraf yang jelas.

- [ ] **[6.3]** Periksa Bab 11 (QA Summary):
  - [ ] **[6.3.a]** Saat ini Bab 11.1, 11.2, 11.3, dan 11.4 masih berisi placeholder `[DATA BELUM TERSEDIA...]`. Dari R-05 (Test Plan) dan R-12 (Test Cases), periksa apakah ada data hasil testing sandbox yang bisa digunakan.
  - [ ] **[6.3.b]** Jika ada data testing sandbox/draft dari referensi, gunakan data tersebut untuk mengisi bab ini dengan catatan "(Hasil sandbox, belum final produksi)".
  - [ ] **[6.3.c]** Jika sama sekali tidak ada data, perbaiki placeholder menjadi kalimat informatif yang menjelaskan status aktual, bukan sekadar `[DATA BELUM TERSEDIA]`.

- [ ] **[6.4]** Periksa Bab 16.1 (Kontak Dukungan Teknis):
  - [ ] **[6.4.a]** Nomor WhatsApp `+62-812-3456-7890` dan email `support@abucom.com` terlihat seperti data contoh/placeholder. Periksa apakah R-01 atau dokumen referensi lainnya memiliki data kontak resmi yang benar.
  - [ ] **[6.4.b]** Jika data kontak resmi tersedia dari referensi, ganti dengan data yang benar. Jika tidak, tambahkan catatan bahwa data ini perlu dikonfirmasi manual oleh Pemilik Usaha.

- [ ] **[6.5]** Periksa Bab 17 (Persetujuan & Otorisasi):
  - [ ] **[6.5.a]** Verifikasi nama "Donsise" sebagai Kepala Percetakan — apakah nama ini valid sesuai data di Project Charter atau dokumen referensi lainnya. Jika ada inkonsistensi, sesuaikan.
  - [ ] **[6.5.b]** Verifikasi format tanda tangan `[SIGNED VIA AI AGENT]` — apakah format ini sudah sesuai untuk dokumen formal internal. Jika perlu, perbaiki menjadi format yang lebih formal.

---

### FASE 7 — IDENTIFIKASI & PENGISIAN DATA KOSONG (KV-07)

> **Tujuan:** Menemukan SEMUA field, tabel, atau paragraf yang kosong atau berisi placeholder yang bisa diisi dari informasi yang tersedia di dokumen referensi.

- [ ] **[7.1]** Lakukan pencarian menyeluruh di seluruh dokumen utama untuk setiap kemunculan pola berikut:
  - [ ] **[7.1.a]** Cari teks `[DATA BELUM TERSEDIA` — catat semua baris yang mengandung pola ini.
  - [ ] **[7.1.b]** Cari teks `[TBD` atau `[TODO` — catat semua baris yang mengandung pola ini.
  - [ ] **[7.1.c]** Cari teks yang diawali `[` dan diakhiri `]` yang merupakan placeholder — catat semua lokasi ini.

- [ ] **[7.2]** Untuk setiap placeholder yang ditemukan di [7.1], lakukan hal berikut:
  - [ ] **[7.2.a]** Tentukan apakah data pengisi tersedia dari salah satu 16 dokumen referensi yang sudah dibaca di Fase 0.
  - [ ] **[7.2.b]** Jika data tersedia: **Isi placeholder tersebut dengan data yang akurat dari referensi** beserta catatan sumber data jika perlu.
  - [ ] **[7.2.c]** Jika data tidak tersedia dari referensi manapun: **Ganti placeholder dengan kalimat informatif** yang menjelaskan mengapa data belum tersedia, kapan akan diisi, dan siapa yang bertanggung jawab mengisinya. Jangan biarkan placeholder kosong tanpa penjelasan.

- [ ] **[7.3]** Periksa tabel yang memiliki kolom atau baris kosong tanpa penjelasan:
  - [ ] **[7.3.a]** Tabel Riwayat Perubahan Dokumen — pastikan sudah terisi lengkap.
  - [ ] **[7.3.b]** Tabel Matriks RBAC di Bab 5.2 — verifikasi tidak ada sel yang seharusnya memiliki nilai tapi kosong.
  - [ ] **[7.3.c]** Tabel Runtime Config di Bab 10.4 — verifikasi tidak ada parameter yang hilang.
  - [ ] **[7.3.d]** Tabel Matriks Risiko di Bab 13 — verifikasi semua kolom terisi lengkap.
  - [ ] **[7.3.e]** Tabel Tim Pengembang di Bab 14.1 — verifikasi tidak ada tanggung jawab yang kosong.
  - [ ] **[7.3.f]** Tabel RACI di Bab 14.2 — verifikasi semua sel sudah terisi dengan R/A/C/I yang tepat.
  - [ ] **[7.3.g]** Tabel Persetujuan di Bab 17 — verifikasi semua field terisi.
  - [ ] **[7.3.h]** Tabel Referensi Dokumen di Bab 19 — verifikasi tidak ada field yang kosong.

---

### FASE 8 — VALIDASI SPESIFIK RELEASE NOTES (Tambahan Kaidah Standar)

> **Tujuan:** Memvalidasi aspek-aspek khusus yang merupakan kaidah standar industri untuk dokumen Release Notes yang tidak boleh terlewat.

- [ ] **[8.1]** Validasi Semantic Versioning (SemVer):
  - [ ] **[8.1.a]** Verifikasi bahwa penomoran `v1.0.0` sudah tepat menggunakan format SemVer `vMAJOR.MINOR.PATCH`.
  - [ ] **[8.1.b]** Pastikan alasan pemilihan Major Release (bukan Minor atau Patch) sudah dijelaskan secara eksplisit di Bab 2.3.

- [ ] **[8.2]** Validasi Dependency Pinning:
  - [ ] **[8.2.a]** Verifikasi semua versi pustaka yang tercantum di Bab 3.2.3 menggunakan versi yang di-pin secara eksak (`==`) bukan menggunakan range (`>=` atau `~=`).
  - [ ] **[8.2.b]** Bandingkan daftar pustaka di Bab 3.2.3 dengan yang ada di R-08 (Tech Stack Decision) — pastikan tidak ada pustaka yang terlewat atau berbeda versi.

- [ ] **[8.3]** Validasi Breaking Changes:
  - [ ] **[8.3.a]** Karena ini rilis perdana (v1.0.0), tidak ada breaking changes dari versi sebelumnya. Pastikan Bab 6 sudah menjelaskan hal ini dengan tepat dan tidak membingungkan.
  - [ ] **[8.3.b]** Verifikasi Bab 9.2 (Upgrade dari Versi Sebelumnya) sudah jelas menyatakan bahwa tidak ada prosedur upgrade karena ini rilis perdana.

- [ ] **[8.4]** Validasi Migration Notes:
  - [ ] **[8.4.a]** Dokumen ini adalah migrasi dari sistem Excel ke CLI. Verifikasi apakah ada catatan migrasi data (import CSV/Excel) yang seharusnya disebutkan di bagian panduan instalasi atau bab terpisah.
  - [ ] **[8.4.b]** Referensikan SRS-F-035 (Input Data Awal Manual dari Excel) dan SRS-F-014 (Import CSV) — apakah catatan ini sudah ada di dokumen? Jika belum, tambahkan.

- [ ] **[8.5]** Validasi Rollback & Disaster Recovery:
  - [ ] **[8.5.a]** Verifikasi prosedur rollback di Bab 9.3 sudah mencakup skenario terburuk (database korup total, kode klien rusak).
  - [ ] **[8.5.b]** Verifikasi ada informasi kapan prosedur rollback harus diaktifkan (kondisi trigger rollback).

- [ ] **[8.6]** Validasi SOP Operasional Harian:
  - [ ] **[8.6.a]** Verifikasi bahwa SOP startup dan shutdown di Bab 10.3 sudah konsisten dengan runbook operasional di R-03 (Deployment Guide).
  - [ ] **[8.6.b]** Pastikan urutan langkah SOP di Bab 10.3 sudah benar dan tidak ada langkah yang terlewat.

- [ ] **[8.7]** Validasi Kepatuhan Regulasi:
  - [ ] **[8.7.a]** Verifikasi bahwa referensi ke UU PDP No. 27 Tahun 2022 di seluruh dokumen sudah konsisten dan tepat.
  - [ ] **[8.7.b]** Pastikan kewajiban Right to Erasure yang disebut di Bab 5.3 sudah memiliki mekanisme teknis yang jelas (tidak sekadar disebutkan tapi ada prosedurnya).

---

### FASE 9 — KOMPILASI TEMUAN & DRAF REVISI

> **Tujuan:** Mengkompilasi semua temuan dari Fase 1–8 menjadi daftar perubahan yang akan diterapkan ke dokumen.

- [ ] **[9.1]** Buat daftar temuan berdasarkan kategori:
  - [ ] **[9.1.a]** Temuan **DATA TERLEWAT** (informasi dari referensi yang belum ada di dokumen utama).
  - [ ] **[9.1.b]** Temuan **DATA TIDAK RELEVAN** (informasi yang ada di dokumen tapi seharusnya tidak ada).
  - [ ] **[9.1.c]** Temuan **STRUKTUR HILANG** (bab, sub-bab, atau elemen yang seharusnya ada tapi tidak ada).
  - [ ] **[9.1.d]** Temuan **DATA TIDAK KONSISTEN** (perbedaan nilai atau deskripsi antara dokumen utama dan referensi).
  - [ ] **[9.1.e]** Temuan **PLACEHOLDER BELUM TERISI** (field yang masih berisi teks placeholder).
  - [ ] **[9.1.f]** Temuan **BAHASA TIDAK JELAS** (kalimat ambigu, terlalu teknis tanpa penjelasan, atau typo).

- [ ] **[9.2]** Untuk setiap temuan, tentukan:
  - [ ] **[9.2.a]** Lokasi baris atau bab di dokumen utama yang bermasalah.
  - [ ] **[9.2.b]** Data atau konten koreksi yang akan digunakan (dan dari referensi mana).
  - [ ] **[9.2.c]** Apakah perubahan ini membutuhkan penambahan referensi baru di Bab 19.

- [ ] **[9.3]** Tentukan apakah ada file referensi baru (di luar 16 yang sudah ada) yang digunakan dalam proses perbaikan ini:
  - [ ] **[9.3.a]** Jika ada referensi baru: catat nama file, path, versi, prioritas, dan perannya untuk ditambahkan di Bab 19.

---

### FASE 10 — PENULISAN ULANG DOKUMEN FINAL (KV-08, KV-09, KV-10)

> **Tujuan:** Menuangkan seluruh hasil validasi dan perbaikan ke file target dengan cara menimpa (overwrite) dokumen secara penuh.

> **⚠️ PERINGATAN KRITIS — BACA DENGAN SEKSAMA SEBELUM MENULIS:**
> - Kamu **WAJIB** menulis ulang dokumen dari **baris pertama hingga baris terakhir** secara lengkap.
> - **DILARANG KERAS** melakukan pemotongan (truncation), peringkasan (summary), atau penghilangan (omission) pada bagian mana pun dari dokumen.
> - Setiap bab, sub-bab, paragraf, tabel, diagram, dan kode blok yang **tidak bermasalah** harus tetap ditulis ulang **identik** dengan aslinya.
> - Hanya bagian yang memiliki **temuan validasi** yang boleh diubah, ditambah, atau diperbaiki.
> - **JANGAN** menulis `[... isi tetap sama ...]` atau komentar serupa — tulis ulang sepenuhnya.

- [ ] **[10.1]** Perbarui YAML front matter:
  - [ ] **[10.1.a]** Ubah `versi: 1.0` menjadi `versi: 1.1`.
  - [ ] **[10.1.b]** Ubah `tanggal` ke tanggal revisi saat ini.
  - [ ] **[10.1.c]** Pastikan `status` diperbarui menjadi `Revisi` atau tetap `Draft` sesuai kondisi.
  - [ ] **[10.1.d]** Tambahkan field `reviewer_revisi` atau perbarui field `reviewer` jika perlu.

- [ ] **[10.2]** Tambahkan baris baru di tabel Riwayat Perubahan Dokumen:
  - [ ] **[10.2.a]** Tambahkan baris versi 1.1 dengan tanggal revisi, deskripsi perubahan yang dilakukan, dan nama validator (nama persona yang digunakan).

- [ ] **[10.3]** Terapkan semua perbaikan hasil temuan Fase 1–8 ke setiap bab secara berurutan:
  - [ ] **[10.3.a]** Terapkan perubahan Bab 1 (Informasi Dokumen) jika ada.
  - [ ] **[10.3.b]** Terapkan perubahan Bab 2 (Ringkasan Rilis) jika ada.
  - [ ] **[10.3.c]** Terapkan perubahan Bab 3 (Persyaratan Sistem) jika ada.
  - [ ] **[10.3.d]** Terapkan perubahan Bab 4 (Fitur Baru) jika ada.
  - [ ] **[10.3.e]** Terapkan perubahan Bab 5 (Fitur Keamanan) jika ada.
  - [ ] **[10.3.f]** Terapkan perubahan Bab 6 (Bug Fixes) jika ada.
  - [ ] **[10.3.g]** Terapkan perubahan Bab 7 (Known Limitations) jika ada.
  - [ ] **[10.3.h]** Terapkan perubahan Bab 8 (Known Issues) jika ada.
  - [ ] **[10.3.i]** Terapkan perubahan Bab 9 (Panduan Instalasi) jika ada.
  - [ ] **[10.3.j]** Terapkan perubahan Bab 10 (Konfigurasi Default) jika ada.
  - [ ] **[10.3.k]** Terapkan perubahan Bab 11 (QA Summary) jika ada.
  - [ ] **[10.3.l]** Terapkan perubahan Bab 12 (Arsitektur) jika ada.
  - [ ] **[10.3.m]** Terapkan perubahan Bab 13 (Matriks Risiko) jika ada.
  - [ ] **[10.3.n]** Terapkan perubahan Bab 14 (Tim Pengembang) jika ada.
  - [ ] **[10.3.o]** Terapkan perubahan Bab 15 (Roadmap) jika ada.
  - [ ] **[10.3.p]** Terapkan perubahan Bab 16 (Kontak Dukungan) jika ada.
  - [ ] **[10.3.q]** Terapkan perubahan Bab 17 (Persetujuan) jika ada.
  - [ ] **[10.3.r]** Terapkan perubahan Bab 18 (Glosarium) jika ada.
  - [ ] **[10.3.s]** Terapkan perubahan Bab 19 (Referensi Dokumen) jika ada — tambahkan file referensi baru di baris paling bawah tabel jika ada yang digunakan.

- [ ] **[10.4]** Tulis ulang seluruh dokumen ke file target dengan cara **overwrite penuh**:
  - [ ] **[10.4.a]** Buka file `docs/sdlc/06_deployment/03_release_notes.md` untuk ditulis ulang.
  - [ ] **[10.4.b]** Tulis dari **baris 1** (YAML front matter `---`) hingga **baris terakhir** (baris penutup dokumen).
  - [ ] **[10.4.c]** Pastikan tidak ada baris dari dokumen asli yang terlewat dituliskan kembali.
  - [ ] **[10.4.d]** Jika ada referensi baru yang ditambahkan dalam proses perbaikan, pastikan sudah ditambahkan sebagai baris baru di bagian paling bawah tabel pada Bab 19.

---

### FASE 11 — VERIFIKASI PASCA-PENULISAN

> **Tujuan:** Memverifikasi bahwa file yang sudah ditulis ulang sudah benar, lengkap, dan tidak ada yang terpotong.

- [ ] **[11.1]** Baca ulang file yang sudah ditulis ulang dari baris pertama hingga baris terakhir:
  - [ ] **[11.1.a]** Konfirmasi bahwa YAML front matter sudah memuat versi `1.1`.
  - [ ] **[11.1.b]** Konfirmasi bahwa tabel Riwayat Perubahan Dokumen sudah memuat baris versi 1.1.
  - [ ] **[11.1.c]** Konfirmasi bahwa semua 19 bab masih hadir dan tidak ada yang hilang.
  - [ ] **[11.1.d]** Konfirmasi bahwa semua perbaikan dari Fase 1–8 sudah diterapkan dengan benar.
  - [ ] **[11.1.e]** Konfirmasi bahwa tidak ada placeholder `[DATA BELUM TERSEDIA...]` yang tidak tertangani.
  - [ ] **[11.1.f]** Konfirmasi bahwa baris penutup dokumen masih ada dan utuh.

- [ ] **[11.2]** Verifikasi integritas tabel:
  - [ ] **[11.2.a]** Pastikan semua tabel markdown masih memiliki format yang valid (header, separator `|---|`, dan baris data).
  - [ ] **[11.2.b]** Pastikan diagram Mermaid masih terbuka dengan ` ```mermaid ` dan tertutup dengan ` ``` ` yang benar.

- [ ] **[11.3]** Verifikasi kelengkapan Bab 19:
  - [ ] **[11.3.a]** Hitung jumlah baris di tabel Bab 19 — pastikan minimal 16 baris (R-01 s.d R-16) masih ada.
  - [ ] **[11.3.b]** Jika ada referensi baru yang ditambahkan, pastikan baris baru sudah berada di bagian **paling bawah** tabel dan penomoran sudah benar (No 17, 18, dst.).

- [ ] **[11.4]** Tandai semua kriteria validasi di Tabel Kriteria Validasi (bagian 4 issue ini) yang sudah terpenuhi dengan mengubah `[ ] Belum` menjadi `[x] Terpenuhi`.

---

## 6. Definisi Selesai (Definition of Done)

Issue ini dinyatakan **SELESAI** jika dan hanya jika semua kondisi berikut terpenuhi:

- [ ] Semua checklist dari Fase 0 hingga Fase 11 sudah dicentang `[x]`.
- [ ] File `docs/sdlc/06_deployment/03_release_notes.md` sudah ditulis ulang secara penuh (overwrite).
- [ ] YAML front matter sudah menampilkan `versi: 1.1`.
- [ ] Tabel Riwayat Perubahan sudah memiliki baris v1.1.
- [ ] Tidak ada placeholder `[DATA BELUM TERSEDIA...]` yang tersisa tanpa penanganan yang tepat.
- [ ] Semua 10 kriteria validasi (KV-01 s.d KV-10) sudah terpenuhi.
- [ ] Jika ada file referensi baru, sudah tercantum di Bab 19 pada baris paling bawah.

---

## 7. Catatan Tambahan untuk Implementor

> **Baca seluruh catatan ini sebelum mulai bekerja.**

1. **Prioritaskan membaca file sebelum menulis.** Jangan pernah berasumsi tentang isi dokumen referensi. Baca dulu, baru analisis.

2. **Jangan meringkas atau mempersingkat konten yang ada.** Dokumen Release Notes ini harus tetap panjang dan lengkap. Jika kamu merasa konten terlalu panjang, itu bukan masalah — kelengkapan adalah prioritas utama.

3. **Satu overwrite di akhir.** Jangan tulis ulang file berkali-kali. Kumpulkan semua temuan terlebih dahulu (Fase 0–9), baru tulis ulang sekali di Fase 10.

4. **Jika ragu antara menambah atau tidak.** Jika kamu menemukan data dari referensi yang relevan dengan Release Notes dan tidak ada di dokumen utama, TAMBAHKAN. Lebih baik dokumen terlalu lengkap daripada ada informasi penting yang hilang.

5. **Jika ada konflik data antara referensi.** Gunakan urutan prioritas: PRIMER > SEKUNDER > TERSIER. Jika dua dokumen PRIMER saling bertentangan, pilih yang lebih spesifik dan tambahkan catatan penjelasan.

6. **Bab 19 adalah sakral.** Jangan menghapus atau mengubah baris yang sudah ada di tabel Bab 19. Kamu hanya boleh menambahkan baris baru di bagian paling bawah jika ada referensi baru yang digunakan.

7. **Versi dokumen adalah sinyal revisi.** Perubahan versi dari 1.0 ke 1.1 di YAML front matter dan di tabel Riwayat Perubahan adalah bukti bahwa validasi sudah dilakukan. Jangan lewatkan ini.

8. **Periksa konsistensi angka-angka.** Untuk dokumen ini, banyak parameter berupa angka (Rp 15.000.000, Rp 1.600.000, 28.800 detik, 192.168.1.200, dll). Setiap angka harus diverifikasi konsisten dengan referensi — satu angka yang berbeda bisa mengakibatkan kesalahan operasional nyata.

---

*Issue ini dibuat oleh Antigravity (Senior DevOps Lead) pada 2026-05-27 sebagai panduan implementasi low-level untuk validasi dokumen Release Notes AbuCom v1.0.0.*
