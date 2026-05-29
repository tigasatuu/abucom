---
judul      : Validasi, Analisis, dan Penyempurnaan Dokumen Test Plan
target_file: docs/sdlc/05_testing/01_test_plan.md
dibuat_oleh: Senior QA Architect & SDLC Documentation Specialist
tanggal    : 2026-05-29
status     : Open
prioritas  : High
---

# Validasi, Analisis, dan Penyempurnaan Dokumen Test Plan

## Ringkasan Issue

Dokumen **Test Plan** (`docs/sdlc/05_testing/01_test_plan.md`) adalah cetak biru pengujian formal fase SDLC-05 yang menjadi acuan utama pembuatan **Test Cases**, **Test Scripts**, dan **Test Report**. Dokumen ini harus divalidasi secara ketat untuk memastikan kelengkapan, konsistensi, akurasi teknis, dan kualitasnya sebelum digunakan sebagai input pada fase SDLC berikutnya.

Issue ini berisi instruksi **low-level step-by-step** yang wajib dieksekusi secara berurutan oleh pelaksana (junior programmer atau AI model lain). Setiap langkah memiliki checklist eksplisit agar tidak ada ambiguitas maupun halusinasi dalam implementasi.

---

## Persona Pelaksana

Sebelum memulai pekerjaan, pelaksana **wajib** mengadopsi persona berikut secara penuh selama seluruh proses validasi ini berlangsung:

> **Anda adalah seorang Senior QA Architect & SDLC Documentation Specialist** dengan pengalaman lebih dari 10 tahun dalam industri pengembangan perangkat lunak skala enterprise. Anda memiliki keahlian mendalam dalam standar IEEE 829 (Test Documentation), ISTQB Certified Tester Foundation Level, dan praktik terbaik dokumentasi SDLC untuk sistem keuangan dan POS (Point-of-Sale). Anda sangat teliti, kritis, dan tidak mentoleransi ketidakkonsistenan data sekecil apapun antara dokumen utama dan dokumen referensinya. Anda memahami setiap implikasi teknis dari setiap baris dokumen Test Plan ini terhadap proses pengujian nyata di lapangan, dan Anda bertanggung jawab penuh atas kualitas output dokumen ini sebelum diserahkan ke fase eksekusi pengujian berikutnya.

---

## Informasi Konteks

| Atribut | Detail |
|---|---|
| **Dokumen Utama (Target)** | Test Plan |
| **Target File** | `docs/sdlc/05_testing/01_test_plan.md` |
| **Lokasi Referensi** | `docs/sdlc/` (seluruh subdirektori) |
| **Versi Dokumen Saat Ini** | v1.1 |
| **Versi Target Setelah Revisi** | v1.2 |
| **Standar Acuan** | IEEE 829, ISTQB CTFL, Praktik Industri QA |

---

## Dimensi Validasi

Issue ini mencakup **10 dimensi validasi** yang harus dieksekusi secara berurutan dan menyeluruh:

| No | Dimensi | Fokus Validasi |
|:---:|---|---|
| D-01 | Kelengkapan Konten vs Referensi | Apakah semua data dari file referensi sudah terserap? |
| D-02 | Relevansi & Kebersihan Konten | Apakah dokumen hanya memuat data yang sesuai scope-nya? |
| D-03 | Standar Struktur Dokumen | Apakah struktur sudah sesuai praktik industri (IEEE 829)? |
| D-04 | Kualitas sebagai Referensi SDLC | Apakah layak dijadikan acuan fase SDLC berikutnya? |
| D-05 | Kualitas Bahasa Indonesia | Apakah bahasa natural, tidak ambigu, mudah dipahami? |
| D-06 | Kelengkapan Bebas Interupsi | Apakah tidak akan selalu dipertanyakan saat digunakan? |
| D-07 | Data Kosong / Placeholder | Apakah ada field yang belum terisi dan perlu dilengkapi? |
| D-08 | Konsistensi Internal Dokumen | Apakah data antar-bab saling konsisten dan tidak kontradiktif? |
| D-09 | Ketertelusuran (Traceability) | Apakah setiap skenario uji terhubung ke SRS, UC, dan modul? |
| D-10 | Keamanan & Kepatuhan Regulasi | Apakah aspek keamanan dan UU PDP sudah tercakup penuh? |

---

## Tahapan Implementasi (Step-by-Step)

> **PERINGATAN KRITIS:** Eksekusi setiap tahapan **secara berurutan dari Tahap 1 hingga Tahap 10**. Jangan melompati tahapan. Jangan menulis ke file apapun sebelum Tahap 10 diizinkan. Seluruh hasil analisis harus dikumpulkan terlebih dahulu di memori/scratchpad sebelum dituangkan ke file target.

---

### TAHAP 1 — Persiapan: Baca dan Pahami Dokumen Utama

**Tujuan:** Membangun pemahaman menyeluruh tentang isi dokumen utama sebelum melakukan komparasi apapun.

- [ ] **[BACA]** Buka dan baca tuntas seluruh isi file `docs/sdlc/05_testing/01_test_plan.md` dari baris pertama hingga baris terakhir tanpa terkecuali.
- [ ] **[CATAT]** Identifikasi dan catat struktur bab dokumen ini (daftar semua heading `##` dan `###` yang ada).
- [ ] **[CATAT]** Identifikasi dan catat seluruh file referensi yang disebutkan di **Bab 15 (Referensi Dokumen)** beserta kode referensi (R-01 s.d R-18 dan seterusnya) serta path file-nya.
- [ ] **[CATAT]** Identifikasi dan catat seluruh ID skenario uji yang ada (format: `MX-TC-YYY`).
- [ ] **[CATAT]** Identifikasi dan catat seluruh ID SRS (SRS-F-XXX dan SRS-NF-XXX) yang direferensikan.
- [ ] **[CATAT]** Identifikasi dan catat seluruh ID Use Case (UC-XXX) yang direferensikan.
- [ ] **[CATAT]** Identifikasi dan catat seluruh kode error (ERR-XXX-YYY) yang disebutkan.
- [ ] **[CATAT]** Identifikasi dan catat semua field, tabel, atau placeholder yang terindikasi belum terisi (`*[Diisi saat eksekusi pengujian]*`, `[DATA BELUM TERSEDIA]`, `N/A`, atau sejenisnya).

---

### TAHAP 2 — Baca Seluruh File Referensi

**Tujuan:** Mengumpulkan seluruh data dari semua file referensi yang tercantum di Bab 15 dokumen utama, sebagai bahan komparasi.

Untuk setiap referensi di bawah ini, lakukan checklist pembacaan:

- [ ] **[BACA R-01]** Baca file `docs/sdlc/02_analysis/02_software_requirements.md` — Catat: (a) seluruh ID SRS-F (fungsional) dan SRS-NF (non-fungsional) beserta nama dan deskripsinya; (b) total jumlah SRS-F dan SRS-NF; (c) versi dokumen.
- [ ] **[BACA R-02]** Baca file `docs/sdlc/02_analysis/03_use_case_diagram.md` — Catat: (a) seluruh ID Use Case (UC-XXX) beserta nama dan aktor; (b) total jumlah UC; (c) versi dokumen.
- [ ] **[BACA R-03]** Baca file `docs/sdlc/02_analysis/06_access_control_matrix.md` — Catat: (a) daftar lengkap 8 peran internal beserta nama persis setiap peran; (b) peta hak akses per peran per menu/modul; (c) versi dokumen.
- [ ] **[BACA R-04]** Baca file `docs/sdlc/03_design/06_security_design.md` — Catat: (a) spesifikasi bcrypt cost factor; (b) durasi JWT expiry; (c) jumlah maksimum gagal login sebelum lockout; (d) durasi lockout; (e) detail mekanisme audit log; (f) spesifikasi enkripsi (Fernet, AES-256); (g) ketentuan UU PDP; (h) versi dokumen.
- [ ] **[BACA R-05]** Baca file `docs/sdlc/03_design/03_system_architecture.md` — Catat: (a) spesifikasi hardware node server dan node klien; (b) topologi jaringan LAN; (c) port dan protokol; (d) versi dokumen.
- [ ] **[BACA R-06]** Baca file `docs/sdlc/03_design/01_database_schema.sql` — Catat: (a) nama database; (b) daftar tabel yang relevan untuk pengujian (terutama `pengguna`, `audit_logs`, `pelanggan`, `kasbon`, `system_configs`, `persediaan`); (c) tipe data kolom keuangan (DECIMAL); (d) constraint kritis (CHECK, FOREIGN KEY, UNIQUE); (e) versi schema.
- [ ] **[BACA R-07]** Baca file `docs/sdlc/03_design/02_erd_database.md` — Catat: (a) jumlah total tabel; (b) relasi antar-tabel kritis; (c) versi dokumen.
- [ ] **[BACA R-08]** Baca file `docs/sdlc/03_design/05_bom_hpp_design.md` — Catat: (a) rumus kalkulasi HPP BOM; (b) spesifikasi tipe data Decimal(15,4); (c) aturan pembulatan ROUND_HALF_UP; (d) mekanisme InnoDB row locking FOR UPDATE; (e) definisi limbah/waste; (f) mekanisme sinkronisasi ATK internal; (g) versi dokumen.
- [ ] **[BACA R-09]** Baca file `docs/sdlc/03_design/04_cli_interaction_flow.md` — Catat: (a) daftar menu navigasi CLI beserta breadcrumb; (b) standar kode error ERR-XXX-YYY yang didefinisikan; (c) spesifikasi format struk thermal (58mm / 80mm, karakter per baris); (d) library rendering (rich, tabulate); (e) versi dokumen.
- [ ] **[BACA R-10]** Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — Catat: (a) paradigma pemrograman (FP/pure functions); (b) aturan pelarangan f-string SQL; (c) standar penggunaan parameterized query; (d) versi dokumen.
- [ ] **[BACA R-11]** Baca file `docs/sdlc/04_implementation/02_environment_setup.md` — Catat: (a) versi Python yang digunakan; (b) versi MySQL yang digunakan; (c) daftar dependency library beserta versinya; (d) struktur berkas `.env`; (e) versi dokumen.
- [ ] **[BACA R-12]** Baca file `docs/sdlc/04_implementation/03_module_structure.md` — Catat: (a) daftar modul (M.1–M.10) beserta nama resmi dan deskripsinya; (b) folder struktur logic/; (c) versi dokumen.
- [ ] **[BACA R-13]** Baca file `docs/sdlc/04_implementation/04_git_workflow.md` — Catat: (a) informasi yang relevan untuk konteks testing workflow (branch strategy, commit convention); (b) versi dokumen.
- [ ] **[BACA R-14]** Periksa keberadaan file `docs/sdlc/04_implementation/05_development_roadmap.md`. Jika file **tidak ditemukan**, catat status: `[TIDAK TERSEDIA FISIK]` dan pastikan keterangan ini sudah ada di Bab 15 dokumen utama.
- [ ] **[BACA R-15]** Baca file `docs/sdlc/02_analysis/01_business_requirements.md` — Catat: (a) fitur bisnis utama; (b) skala operasional (UMKM percetakan); (c) versi dokumen.
- [ ] **[BACA R-16]** Baca file `docs/sdlc/01_planning/04_tech_stack_decision.md` — Catat: (a) keputusan tech stack resmi (Python, MySQL, library); (b) versi dokumen.
- [ ] **[BACA R-17]** Baca file `docs/sdlc/02_analysis/04_workflow_diagram.md` — Catat: (a) alur proses bisnis utama yang relevan untuk skenario pengujian; (b) versi dokumen.
- [ ] **[BACA R-18]** Baca file `docs/sdlc/02_analysis/05_data_dictionary.md` — Catat: (a) definisi field-field kritis (terutama DECIMAL, UoM, ENUM status); (b) versi dokumen.
- [ ] **[BACA TAMBAHAN]** Periksa keberadaan file `docs/sdlc/narasi.txt`. Jika ada, baca dan catat informasi konteks bisnis yang relevan.

---

### TAHAP 3 — Validasi Dimensi D-01: Kelengkapan Konten vs Referensi

**Tujuan:** Memastikan semua data dan informasi penting dari file referensi sudah terserap ke dalam dokumen utama Test Plan.

- [ ] **[PERIKSA]** Bandingkan daftar seluruh **ID SRS-F** (dari R-01) dengan seluruh ID SRS yang direferensikan di Bab 4 (tabel skenario per modul) dan Bab 12.1 (Traceability Matrix). Apakah ada SRS-F yang belum memiliki skenario uji di Test Plan? Catat temuannya.
- [ ] **[PERIKSA]** Bandingkan daftar seluruh **ID SRS-NF** (dari R-01) dengan Bab 12.2. Apakah ada SRS-NF yang belum dipetakan ke skenario/bab pengujian? Catat temuannya.
- [ ] **[PERIKSA]** Bandingkan daftar seluruh **ID Use Case** (dari R-02) dengan Bab 12.3. Apakah total jumlah UC terpetakan sudah sesuai? Apakah ada UC yang tidak memiliki skenario uji terkait? Catat temuannya.
- [ ] **[PERIKSA]** Bandingkan **8 peran RBAC** dari R-03 dengan peran yang disebutkan di Bab 5.2 (Pengujian RBAC) dan daftar peran di Bab 1.6. Apakah nama-nama peran sudah konsisten dan lengkap? Catat perbedaannya jika ada.
- [ ] **[PERIKSA]** Bandingkan **spesifikasi keamanan** dari R-04 (bcrypt cost factor, durasi JWT, jumlah gagal login, durasi lockout, mekanisme enkripsi) dengan Bab 5 dokumen utama. Apakah semua parameter spesifik sudah tercantum dengan benar dan akurat? Catat temuannya.
- [ ] **[PERIKSA]** Bandingkan **spesifikasi hardware dan topologi jaringan** dari R-05 dengan Bab 10 (Lingkungan Pengujian). Apakah spesifikasi node server, klien, jaringan, dan port sudah lengkap dan akurat? Catat temuannya.
- [ ] **[PERIKSA]** Bandingkan **tipe data DECIMAL, constraint database** dari R-06 dan R-07 dengan Bab 6 (Pengujian Presisi Desimal) dan Bab 7 (Pengujian Integrasi). Apakah kalkulasi boundary testing sudah menggunakan tipe data yang benar? Catat temuannya.
- [ ] **[PERIKSA]** Bandingkan **rumus HPP BOM, ROUND_HALF_UP, FOR UPDATE** dari R-08 dengan Bab 6.1, 6.2, dan 6.4. Apakah contoh kalkulasi numerik konkret sudah konsisten dengan spesifikasi matematika di R-08? Catat temuannya.
- [ ] **[PERIKSA]** Bandingkan **kode error ERR-XXX-YYY** dari R-09 dengan Bab 12.4 dan skenario di Bab 5 dan Bab 8. Apakah ada kode error dari R-09 yang belum tercakup di Test Plan? Catat temuannya.
- [ ] **[PERIKSA]** Bandingkan **daftar nama modul resmi M.1–M.10** dari R-12 dengan nama modul yang digunakan di Bab 2.1 dan Bab 4. Apakah nama modul konsisten? Catat temuannya.
- [ ] **[PERIKSA]** Bandingkan **daftar dependency library dan versinya** dari R-11 dengan Bab 10.2. Apakah versi library sudah sinkron? Catat temuannya.
- [ ] **[PERIKSA]** Bandingkan **alur proses bisnis** dari R-17 dengan skenario UAT di Bab 3.1.4. Apakah skenario UAT sudah mencerminkan alur operasional harian yang didefinisikan di R-17? Catat temuannya.

---

### TAHAP 4 — Validasi Dimensi D-02: Relevansi & Kebersihan Konten

**Tujuan:** Memastikan dokumen Test Plan hanya memuat data dan informasi yang memang diperlukan dalam konteks perencanaan pengujian, tidak lebih dan tidak kurang.

- [ ] **[PERIKSA]** Periksa setiap bab apakah ada informasi yang seharusnya berada di dokumen lain (misalnya detail implementasi kode yang seharusnya di Coding Standard, atau detail spesifikasi database yang seharusnya di Schema). Catat jika ada.
- [ ] **[PERIKSA]** Periksa apakah setiap skenario uji di Bab 4 sudah difokuskan pada **hasil yang dapat diverifikasi** (expected output), bukan pada detail implementasi internal kode. Catat jika ada skenario yang terlalu jauh masuk ke level implementasi.
- [ ] **[PERIKSA]** Periksa apakah Bab 14 (Lampiran) memuat template yang memang relevan untuk fase pengujian ini (Test Case template, Test Report template). Apakah ada lampiran yang tidak relevan? Catat temuannya.
- [ ] **[PERIKSA]** Periksa apakah Bab 15 (Referensi) hanya mendaftarkan file yang benar-benar dikutip atau digunakan sebagai sumber data di dalam dokumen. Jika ada referensi yang tidak dirujuk di badan dokumen, catat sebagai kandidat penghapusan.
- [ ] **[PERIKSA]** Periksa apakah ada duplikasi informasi yang sama persis yang muncul di lebih dari satu bab tanpa tujuan yang jelas. Catat duplikasi yang ditemukan.

---

### TAHAP 5 — Validasi Dimensi D-03: Standar Struktur Dokumen (IEEE 829)

**Tujuan:** Memastikan struktur dokumen Test Plan sudah sesuai standar industri pengujian perangkat lunak (IEEE 829) dan kelengkapan komponen wajib.

- [ ] **[PERIKSA]** Verifikasi keberadaan komponen wajib IEEE 829 berikut di dalam dokumen:
  - [ ] Test Plan Identifier (judul, versi, tanggal, penyusun) — ada di header?
  - [ ] Introduction / Purpose — ada di Bab 1.1?
  - [ ] Test Items / Features to be Tested — ada di Bab 2.1?
  - [ ] Features Not to be Tested — ada di Bab 2.2?
  - [ ] Approach / Test Strategy — ada di Bab 3?
  - [ ] Item Pass/Fail Criteria — ada di Bab 3.4?
  - [ ] Suspension Criteria & Resumption Requirements — ada di Bab 3.4.3 dan 3.4.4?
  - [ ] Test Deliverables (output dokumen) — ada di Bab 1.4?
  - [ ] Testing Tasks (jadwal dan siklus) — ada di Bab 11.2?
  - [ ] Environmental Needs — ada di Bab 10?
  - [ ] Responsibilities — ada di Bab 11.1?
  - [ ] Staffing and Training Needs — ada (minimal tersirat) di Bab 11.1?
  - [ ] Schedule — ada di Bab 11.2?
  - [ ] Risks and Contingencies — ada di Bab 2.4?
  - [ ] Approvals / Sign-Off — ada di Bab 13.3?
- [ ] **[PERIKSA]** Periksa apakah dokumen memiliki **Riwayat Perubahan Dokumen** (Change Log) yang terisi lengkap dengan versi, tanggal, deskripsi perubahan, dan pelaksana. Catat jika ada field kosong.
- [ ] **[PERIKSA]** Periksa apakah setiap bab utama memiliki penjelasan narasi pembuka yang cukup sebelum langsung masuk ke tabel atau daftar. Catat bab yang langsung dimulai dengan tabel tanpa narasi konteks.
- [ ] **[PERIKSA]** Periksa konsistensi format heading: apakah semua heading menggunakan konvensi yang seragam (`##` untuk bab, `###` untuk sub-bab, `####` untuk sub-sub-bab)?
- [ ] **[PERIKSA]** Periksa apakah ada komponen tambahan yang sebaiknya ditambahkan untuk dokumen Test Plan yang bersifat keuangan/UMKM (misalnya: **Defect Lifecycle Diagram**, **Metrik Kualitas**, **Glosarium Istilah Pengujian**). Verifikasi apakah komponen-komponen ini sudah ada.
- [ ] **[TAMBAHKAN JIKA TIDAK ADA]** Jika ditemukan komponen IEEE 829 wajib yang benar-benar tidak ada di dokumen, tandai sebagai item yang perlu ditambahkan di Tahap 9.

---

### TAHAP 6 — Validasi Dimensi D-04: Kualitas sebagai Referensi SDLC Berikutnya

**Tujuan:** Memastikan dokumen ini layak menjadi referensi dan input utama bagi dokumen-dokumen fase SDLC berikutnya: Test Cases, Test Scripts, dan Test Report.

- [ ] **[PERIKSA]** Verifikasi apakah setiap **ID Skenario Uji** (format `MX-TC-YYY`) sudah cukup detail untuk dijadikan basis pembuatan Test Case yang rinci. Minimal setiap skenario harus memiliki: (a) deskripsi yang jelas; (b) SRS terkait; (c) UC terkait; (d) tipe test; (e) prioritas.
- [ ] **[PERIKSA]** Verifikasi apakah **template Test Case** di Bab 14.2 memiliki seluruh field standar: ID, nama, modul, peran aktor, prakondisi, langkah uji, hasil diharapkan, hasil aktual, status. Catat jika ada field yang kurang.
- [ ] **[PERIKSA]** Verifikasi apakah **template Test Report** di Bab 14.3 memiliki elemen statistik yang cukup untuk evaluasi go-live decision. Catat jika ada elemen penting yang kurang.
- [ ] **[PERIKSA]** Verifikasi apakah **Matriks Ketertelusuran (Bab 12)** sudah mencakup kolom-kolom yang dibutuhkan (ID SRS, nama, ID skenario, status). Apakah status semua item sudah terisi dengan nilai yang valid (`Cocok`, `Parsial`, `Belum Ada`)?
- [ ] **[PERIKSA]** Verifikasi apakah **kriteria sign-off UAT** di Bab 13.3 sudah terukur, spesifik, dan dapat diverifikasi secara objektif (bukan kriteria yang masih ambigu). Catat kriteria yang masih subjektif atau tidak terukur.
- [ ] **[PERIKSA]** Verifikasi apakah dokumen ini menyebutkan **lokasi file output** yang akan dihasilkan (misal: `docs/sdlc/05_testing/defect_log.md`). Pastikan path ini konsisten dengan yang disebutkan di Bab 11.3.3.
- [ ] **[PERIKSA]** Verifikasi apakah **Bab 3.4.1 (Entry Criteria)** dan **Bab 3.4.2 (Exit Criteria)** sudah memiliki kriteria yang spesifik dan terukur secara kuantitatif (angka, persentase, jumlah). Catat kriteria yang masih kualitatif/ambigu.

---

### TAHAP 7 — Validasi Dimensi D-05: Kualitas Bahasa Indonesia

**Tujuan:** Memastikan seluruh konten ditulis dalam Bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau AI model lain yang lebih murah.

- [ ] **[PERIKSA]** Baca ulang seluruh teks narasi (bukan tabel, bukan kode) di setiap bab. Tandai setiap kalimat yang:
  - [ ] Terlalu panjang (lebih dari 3 klausa dalam satu kalimat)
  - [ ] Menggunakan istilah teknis tanpa penjelasan atau tanpa referensi ke Bab 1.6 (Glosarium)
  - [ ] Menggunakan konstruksi kalimat yang ambigu (subjek tidak jelas, kata kerja ganda)
  - [ ] Menggunakan istilah Bahasa Inggris yang sudah ada padanan resminya dalam Bab 1.6 tanpa penanda *italic*
- [ ] **[PERIKSA]** Verifikasi apakah semua istilah teknis dan akronim yang digunakan di badan dokumen sudah terdaftar di **Bab 1.6 (Glosarium)**. Jika ada istilah/akronim yang digunakan tapi tidak terdaftar, tandai sebagai item yang perlu ditambahkan di glosarium.
- [ ] **[PERIKSA]** Verifikasi konsistensi penulisan nama teknis: (a) nama modul (`M.1`, `M.2`, dst.) konsisten di seluruh dokumen; (b) nama peran pengguna (`pemilik`, `kasir`, `desainer`, dst.) konsisten dalam huruf kecil sesuai format kode program; (c) nama file referensi konsisten menggunakan format code (backtick).
- [ ] **[PERIKSA]** Verifikasi apakah **langkah-langkah skenario pengujian** di Bab 5, 6, 7, 8, dan 9 ditulis dalam format imperatif yang jelas dan mudah diikuti tanpa ambiguitas. Contoh format baik: "Lakukan login sebagai `kasir`." vs format buruk: "User melakukan login."

---

### TAHAP 8 — Validasi Dimensi D-06, D-07, D-08, D-09, D-10 (Gabungan)

**Tujuan:** Validasi aspek-aspek kritis yang saling berkaitan untuk memastikan dokumen tidak akan menghambat pekerjaan fase berikutnya.

#### D-06: Kelengkapan Bebas Interupsi
- [ ] **[PERIKSA]** Simulasikan perspektif AI model junior yang akan membaca dokumen ini untuk membuat Test Cases. Apakah ada pertanyaan yang akan selalu muncul karena informasi kurang? Misalnya: "Berapa tepatnya pool_size connection pooling?", "Apa nama database test yang digunakan?", "Berapa lama durasi lockout brute force?". Catat setiap pertanyaan potensial yang belum terjawab di dokumen.
- [ ] **[PERIKSA]** Verifikasi apakah **Bab 10.5 (Konfigurasi .env Pengujian)** sudah lengkap dengan seluruh parameter environment variable yang dibutuhkan sistem untuk beroperasi di mode test. Bandingkan dengan R-11 (Environment Setup).
- [ ] **[PERIKSA]** Verifikasi apakah **Bab 10.3 (Database Pengujian)** sudah menyebutkan nama database test (`abucom_test_db`), cara setup (schema.sql + seed.sql), dan aturan isolasi dari production database.
- [ ] **[PERIKSA]** Verifikasi apakah **Bab 10.4 (Data Pengujian/Fixtures)** sudah menyebutkan file fixture yang dibutuhkan (`test_fixtures.json` atau `seed_test.sql`) beserta konten minimumnya (8 akun pengguna, master barang, supplier, system_configs).

#### D-07: Data Kosong / Placeholder
- [ ] **[PERIKSA]** Cari seluruh kemunculan teks berikut di dokumen (case-insensitive): `[DATA BELUM TERSEDIA]`, `[TIDAK TERSEDIA]`, `[TBD]`, `[belum diisi]`, `N/A`, `*[Diisi saat eksekusi pengujian]*`, `...`, `[...]`.
- [ ] **[TENTUKAN]** Untuk setiap placeholder yang ditemukan: (a) Apakah placeholder tersebut **memang wajar** karena akan diisi saat eksekusi (misal: di template Test Case dan Test Report di Bab 14)? Jika ya, biarkan. (b) Apakah placeholder tersebut **seharusnya sudah terisi** dalam dokumen perencanaan (misal: di Bab 15 untuk R-14 yang tidak tersedia)? Jika ya, isi dengan data yang relevan atau keterangan pengganti yang jelas.
- [ ] **[ISI]** Untuk R-14 (Development Roadmap) yang dinyatakan `[TIDAK TERSEDIA FISIK]`: Pastikan sudah ada keterangan eksplisit di Bab 11.2 dan Bab 15 bahwa jadwal disusun secara tentatif dan file ini belum tersedia. Jika keterangan belum ada, tambahkan.
- [ ] **[PERIKSA]** Verifikasi Bab 13.3 (Sign-Off UAT): Apakah kolom tanggal, nama, dan tanda tangan sudah memiliki format placeholder yang jelas (garis bawah `______`)? Apakah kota dan tanggal pembuatan sudah terisi?

#### D-08: Konsistensi Internal Dokumen
- [ ] **[PERIKSA]** Hitung total skenario uji dari Bab 4 (jumlahkan semua baris `MX-TC-YYY`). Bandingkan dengan angka yang diklaim di Bab 3.4.2 ("44 kasus uji") dan Bab 13.3 Kriteria 1 ("44 Use Case"). Apakah angkanya konsisten? Catat jika ada perbedaan.
- [ ] **[PERIKSA]** Verifikasi konsistensi angka UMR yang disebutkan di Bab 4.4 (M4-TC-003) dan Bab 6.5: apakah nilai batas minimum 50% UMR (Rp 1.600.000) konsisten? Bandingkan dengan R-01 (SRS-F-019).
- [ ] **[PERIKSA]** Verifikasi konsistensi nilai `pool_size` connection pool: di Bab 2.1 disebutkan `pool_size=5`, di Bab 7.1 disebutkan `pool_size = 5`. Pastikan nilai ini konsisten di seluruh dokumen dan sesuai dengan R-11.
- [ ] **[PERIKSA]** Verifikasi konsistensi batas toleransi selisih kas: di Bab 2.1 disebutkan `selisih laci kas > Rp 10.000`, di Bab 6.3 dan 12.4 juga disebutkan `Rp 10.000`. Pastikan semua penyebutan konsisten.
- [ ] **[PERIKSA]** Verifikasi konsistensi jumlah retry mechanism: di Bab 2.1 disebutkan `3x exponential backoff`, di Bab 7.1 disebutkan `3 kali`. Pastikan konsisten.
- [ ] **[PERIKSA]** Verifikasi konsistensi format penulisan nominal rupiah: apakah sudah menggunakan format yang seragam (contoh: `Rp 150.000` vs `Rp150.000`)?

#### D-09: Ketertelusuran (Traceability)
- [ ] **[PERIKSA]** Verifikasi apakah semua **skenario uji di Bab 4** sudah terpetakan di **Matriks Ketertelusuran Bab 12.1** (kolom SRS) dan **Bab 12.3** (kolom UC). Jika ada skenario yang ada di Bab 4 tapi tidak ada di Bab 12, catat sebagai gap traceability.
- [ ] **[PERIKSA]** Verifikasi apakah **Bab 12.4 (Kode Error → Test Validation)** sudah mencantumkan seluruh kode error yang disebut di Bab 5 dan Bab 8. Jika ada kode error yang disebut tapi tidak ada di Bab 12.4, tambahkan.
- [ ] **[PERIKSA]** Verifikasi apakah setiap **bab pengujian spesifik** (Bab 5, 6, 7, 8, 9) memiliki referensi balik ke ID Skenario (MX-TC-YYY) sehingga Test Case author tahu mana skenario yang didetailkan di masing-masing bab.

#### D-10: Keamanan & Kepatuhan Regulasi
- [ ] **[PERIKSA]** Verifikasi apakah **8 skenario pengujian keamanan** di Bab 5 sudah mencakup seluruh mekanisme keamanan yang didefinisikan di R-04 (Security Design). Catat jika ada mekanisme keamanan yang tidak memiliki skenario uji.
- [ ] **[PERIKSA]** Verifikasi apakah pengujian **UU PDP No. 27/2022** (Right to Erasure) sudah tercakup dan skenarionya sudah spesifik menyebutkan hard delete (bukan soft delete). Pastikan konsisten dengan R-04.
- [ ] **[PERIKSA]** Verifikasi apakah **pengujian enkripsi AES-256 backup** menyebutkan folder output backup yang spesifik (`/exports/backups/`) dan metode verifikasi yang konkret (ekstraksi manual menggunakan utilitas OS). Bandingkan dengan R-04 dan R-08.
- [ ] **[PERIKSA]** Verifikasi apakah **pengujian parameterized query** (SQL Injection, Bab 5.3) sudah menyebutkan larangan eksplisit penggunaan f-string SQL, sesuai dengan standar di R-10 (Coding Standard).

---

### TAHAP 9 — Sintesis: Kumpulkan Seluruh Temuan dan Susun Perbaikan

**Tujuan:** Mengkonsolidasikan seluruh temuan dari Tahap 3–8 menjadi daftar perbaikan konkret yang akan diterapkan ke dokumen.

- [ ] **[KUMPULKAN]** Buat daftar lengkap seluruh temuan dari Tahap 3–8, dikategorikan berdasarkan dimensi validasi (D-01 s.d D-10).
- [ ] **[KLASIFIKASI]** Untuk setiap temuan, tentukan jenis tindakan yang diperlukan:
  - `[TAMBAH]` — Informasi perlu ditambahkan karena belum ada
  - `[KOREKSI]` — Informasi ada tapi salah atau tidak akurat
  - `[HAPUS]` — Informasi ada tapi tidak relevan atau duplikat
  - `[REFORMULASI]` — Informasi benar tapi perlu ditulis ulang agar lebih jelas
  - `[BIARKAN]` — Informasi sudah benar dan tidak perlu diubah
- [ ] **[SUSUN]** Siapkan seluruh konten dokumen yang telah direvisi secara lengkap di memori/scratchpad — mulai dari baris pertama (header `---`) hingga baris terakhir (baris referensi terakhir di Bab 15). Pastikan:
  - [ ] Versi dokumen berubah dari `v1.1` menjadi `v1.2`
  - [ ] Baris Riwayat Perubahan ditambahkan: versi `1.2`, tanggal saat ini, deskripsi perubahan (ringkasan validasi yang dilakukan), nama pelaksana (Senior QA Architect & SDLC Documentation Specialist)
  - [ ] Semua temuan perbaikan sudah diintegrasikan ke bab yang tepat
  - [ ] Semua placeholder yang seharusnya sudah terisi, sudah diisi dengan data yang relevan
  - [ ] Glosarium di Bab 1.6 sudah dilengkapi dengan istilah/akronim yang ditemukan di badan dokumen tapi belum terdaftar
  - [ ] Jika ada file referensi baru yang digunakan dalam perbaikan, sudah ditambahkan di Bab 15 di baris paling bawah tabel referensi
- [ ] **[VERIFIKASI AKHIR SEBELUM TULIS]** Lakukan pengecekan terakhir:
  - [ ] Total baris konten baru sudah dihitung dan tidak ada bagian yang terpotong
  - [ ] Tidak ada bab yang hilang dibanding versi sebelumnya
  - [ ] Tidak ada bab yang baru muncul tanpa justifikasi
  - [ ] Format markdown valid (tidak ada heading yang rusak, tabel yang tidak sejajar, atau fence code block yang tidak tertutup)

---

### TAHAP 10 — Penulisan Akhir: Overwrite File Target

**Tujuan:** Menuangkan seluruh hasil dokumen yang telah divalidasi dan disempurnakan ke file target dengan cara menimpa (overwrite) sepenuhnya.

> **PERINGATAN MUTLAK — WAJIB DIBACA SEBELUM MENULIS:**
> 1. Seluruh teks dari **baris pertama hingga baris terakhir** dokumen harus ditulis ulang sepenuhnya.
> 2. **DILARANG KERAS** memotong (truncating), meringkas, atau menghilangkan bagian apapun dari dokumen yang sudah divalidasi.
> 3. **DILARANG KERAS** menulis `...`, `[lanjutan]`, `[dst]`, `[terpotong]`, atau kalimat apapun yang menandakan konten tidak ditulis penuh.
> 4. Jika konten terlalu panjang untuk satu kali penulisan, tulis dalam **beberapa blok berurutan** dengan instruksi overwrite di blok pertama dan append di blok-blok berikutnya — namun pastikan **tidak ada baris yang terlewat** di antara blok.
> 5. Verifikasi hasil akhir dengan membaca ulang minimal 3 bagian secara acak (awal, tengah, akhir) untuk memastikan tidak ada konten yang terpotong.

- [ ] **[TULIS]** Buka file `docs/sdlc/05_testing/01_test_plan.md` dengan mode **overwrite (tulis ulang dari awal)**.
- [ ] **[TULIS]** Tuliskan seluruh konten dokumen yang sudah direvisi — mulai dari header `---` di baris pertama hingga baris terakhir tabel referensi di Bab 15 — tanpa ada yang dipotong, diringkas, atau dihilangkan.
- [ ] **[VERIFIKASI]** Setelah penulisan selesai, baca kembali file `docs/sdlc/05_testing/01_test_plan.md` untuk memverifikasi:
  - [ ] Versi di header sudah berubah menjadi `1.2`
  - [ ] Baris Riwayat Perubahan v1.2 sudah ada dan terisi lengkap
  - [ ] Jumlah total baris file hasil tidak lebih sedikit dari jumlah baris file awal (kecuali ada penghapusan yang justified)
  - [ ] Semua 15 bab utama (Bab 1 s.d Bab 15) masih ada dan lengkap
  - [ ] Semua tabel di Bab 4, 12.1, 12.2, 12.3, 12.4, dan 15 masih lengkap
  - [ ] Tidak ada heading bab yang hilang
  - [ ] Tidak ada kode fence block (``` atau ~~~) yang tidak tertutup
  - [ ] Jika ada referensi baru yang ditambahkan, baris baru sudah muncul di Bab 15
- [ ] **[LAPORKAN]** Setelah overwrite berhasil, buat laporan singkat yang berisi:
  - Total temuan per dimensi validasi (D-01 s.d D-10)
  - Daftar perubahan utama yang dilakukan
  - Konfirmasi versi dokumen telah berubah menjadi v1.2
  - Konfirmasi tidak ada konten yang terpotong

---

## Instruksi Tambahan Khusus Dokumen Test Plan

Selain 10 instruksi di atas, berikut adalah validasi tambahan yang spesifik untuk karakteristik dokumen Test Plan pada proyek AbuCom:

### A. Validasi Spesifik Kalkulasi Keuangan
- [ ] **[PERIKSA]** Verifikasi bahwa **semua contoh kalkulasi numerik** di Bab 6 (Presisi Desimal) menggunakan angka yang konsisten dan dapat diverifikasi secara matematis. Lakukan perhitungan manual untuk setiap contoh:
  - Bab 6.1: `0.0025 × Rp 100.000 + Rp 4.500 = Rp 4.750` → wajib benar
  - Bab 6.5: `(Rp 12.000.000 × 25%) ÷ 5 = Rp 600.000` → wajib benar
  - Bab 6.5: `50% × Rp 3.200.000 = Rp 1.600.000` → wajib benar
  - Bab 6.5: `Rp 10.000.000 ÷ 60 = Rp 166.666,6667` (ROUND_HALF_UP) → wajib benar
- [ ] **[PERIKSA]** Verifikasi bahwa **boundary cases** di Bab 6.2 (`100.00005`, `100.00004`) sudah logis dan konsisten dengan definisi `ROUND_HALF_UP` (round half ke atas menjauhi nol).

### B. Validasi Khusus Kompatibilitas Dual-OS
- [ ] **[PERIKSA]** Verifikasi bahwa setiap skenario pengujian di Bab 7.5 (Dual-OS) sudah menyebutkan secara eksplisit mesin mana yang menjalankan server (Debian 12) dan mana yang menjalankan klien (Windows 11). Pastikan tidak ada ambiguitas.

### C. Validasi Khusus Diagram dan Visual
- [ ] **[PERIKSA]** Verifikasi bahwa semua diagram ASCII art (Bab 1.3, Bab 3.1, Bab 10) ter-render dengan benar dalam format markdown dan tidak rusak tata letaknya.
- [ ] **[PERIKSA]** Verifikasi bahwa diagram **Mermaid** di Bab 11.4.3 (Defect Lifecycle) menggunakan sintaks yang valid dan tidak akan error saat di-render.

### D. Validasi Path File dan Referensi
- [ ] **[PERIKSA]** Verifikasi semua path file yang disebutkan di Bab 1.4 (link dokumen) dan Bab 15 menggunakan format path yang konsisten (relative path dari root repositori).
- [ ] **[PERIKSA]** Verifikasi bahwa path file di **Bab 1.4** yang menggunakan format absolut Windows (`file:///c:/Users/donsise/...`) perlu dikoreksi menjadi path relatif yang sesuai dengan struktur repositori AbuCom (`docs/sdlc/...`). Jika ya, koreksi path tersebut.

### E. Validasi Kelengkapan Glosarium
- [ ] **[PERIKSA]** Periksa apakah akronim berikut yang muncul di badan dokumen sudah terdaftar di Bab 1.6: `FP`, `UoM`, `BOM`, `HPP`, `PPOB`, `RBAC`, `JWT`, `UU PDP`, `OPEX`, `ACID`, `LAN`, `CLI`, `UAT`, `CSV`, `UPS`, `ATK`, `ERD`, `SRS`, `UC`, `SDLC`, `IEEE`, `ISTQB`. Jika ada yang belum terdaftar, tambahkan.
- [ ] **[PERIKSA]** Tambahkan akronim/istilah berikut ke glosarium jika belum ada: `venv` (*Virtual Environment*: lingkungan Python terisolasi), `pytest` (framework pengujian unit Python), `coverage.py` (alat ukur code coverage Python), `seed.sql` (skrip data awal database), `schema.sql` (skrip struktur tabel database).

---

## Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **selesai** jika seluruh kondisi berikut terpenuhi:

- [ ] Seluruh 10 Tahapan telah dieksekusi secara berurutan dan lengkap.
- [ ] File `docs/sdlc/05_testing/01_test_plan.md` telah di-overwrite dengan versi v1.2 yang telah divalidasi.
- [ ] Versi dokumen di header file sudah berubah menjadi `1.2`.
- [ ] Baris Riwayat Perubahan v1.2 sudah ditambahkan dan terisi lengkap.
- [ ] Tidak ada konten yang terpotong, diringkas, atau dihilangkan.
- [ ] Semua temuan perbaikan sudah terintegrasi ke dalam dokumen yang ditulis ulang.
- [ ] Semua placeholder yang seharusnya sudah terisi telah diisi dengan data yang relevan.
- [ ] Path file di Bab 1.4 telah dikoreksi menjadi path relatif repositori.
- [ ] Jika ada file referensi baru yang digunakan, sudah ditambahkan di Bab 15.
- [ ] Laporan singkat hasil validasi telah dibuat dan dilaporkan.

---

## Catatan untuk Pelaksana

> **JANGAN** membuat asumsi atau mengarang data yang tidak ada di dokumen referensi. Jika ada data yang tidak dapat ditemukan di file referensi manapun, tuliskan keterangan yang jujur dan transparan (misalnya: `[Mengacu pada R-04, data ini belum terdefinisi]`) daripada mengarang data yang bisa menyesatkan.

> **JANGAN** mengubah ruang lingkup atau tujuan dokumen Test Plan ini. Dokumen ini adalah **perencanaan pengujian**, bukan dokumen implementasi, bukan test cases, dan bukan test report. Semua penambahan konten harus tetap dalam konteks perencanaan pengujian.

> **PRIORITASKAN** konsistensi data antara dokumen utama dan file referensi di atas preferensi gaya bahasa. Jika ada konflik antara data di Test Plan dan data di file referensi (SRS, Security Design, dll.), **data dari file referensi yang berlaku** sebagai sumber kebenaran.

---

*Issue dibuat oleh: Senior QA Architect & SDLC Documentation Specialist*
*Tanggal pembuatan: 2026-05-29*
*Target penyelesaian: Segera (blocking untuk pembuatan Test Cases)*
