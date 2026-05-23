---
judul      : Validasi, Analisis & Perbaikan Menyeluruh Business Requirements Document (BRD) v1.0
target_file: docs/sdlc/02_analysis/01_business_requirements.md
prioritas  : High
status     : Open
dibuat_oleh: Senior Business Analyst & Requirements Engineering Specialist
tanggal    : 2026-05-23
---

# Validasi, Analisis & Perbaikan Menyeluruh Business Requirements Document (BRD)

## Ringkasan Issue

Dokumen **Business Requirements Document (BRD)** v1.0 yang berlokasi di `docs/sdlc/02_analysis/01_business_requirements.md` telah selesai disusun pada tahap pertama. Issue ini menugaskan executor untuk melakukan validasi komprehensif, analisis komparatif mendalam, dan perbaikan menyeluruh terhadap dokumen tersebut agar memenuhi standar kualitas industri yang sesungguhnya sebelum dokumen ini digunakan sebagai input primer bagi fase SDLC berikutnya (SRS, SDD, dan Test Plan).

---

## Persona Executor

> **WAJIB DIBACA SEBELUM MEMULAI**
>
> Kamu adalah seorang **Principal Business Analyst** dengan spesialisasi ganda sebagai **Requirements Engineering Specialist** dan **SDLC Quality Assurance Auditor** yang memiliki pengalaman lebih dari 15 tahun dalam mendokumentasikan sistem informasi bisnis skala UMKM hingga enterprise di Indonesia.
>
> Keahlianmu mencakup:
> - Validasi ketat Business Requirements Document (BRD) dan Software Requirements Specification (SRS) berdasarkan standar industri IEEE 830 dan BABOK v3.
> - Analisis komparatif traceability antara dokumen fase Planning dan dokumen Analysis.
> - Identifikasi data hilang (*missing data*), ambiguitas bahasa, inkonsistensi lintas dokumen, dan isu struktur dokumen.
> - Pemahaman mendalam domain bisnis UMKM percetakan di Indonesia: workflow produksi cetak, manajemen inventaris BOM desimal, penggajian, PPOB, dan jasa keuangan digital.
>
> Tugasmu adalah **memeriksa, menganalisis, memvalidasi, memperbaiki, dan menuliskan ulang** dokumen target secara menyeluruh. Kamu tidak diperbolehkan bersikap permisif terhadap kekurangan dokumen. Validasimu harus **ketat, otoritatif, dan tidak berkompromi**.

---

## Konteks Dokumen

| Atribut              | Nilai                                                          |
|---|---|
| **Dokumen Utama**    | Business Requirements Document (BRD) v1.0                     |
| **Target File**      | `docs/sdlc/02_analysis/01_business_requirements.md`            |
| **Lokasi Referensi** | `docs/sdlc/`                                                   |
| **Versi Saat Ini**   | 1.0                                                            |
| **Target Versi**     | 1.1 (setelah direvisi)                                         |
| **Status Awal**      | Draft                                                          |

### Daftar File Referensi yang Wajib Dibaca

| # | File Referensi               | Path Relatif                                        |
|---|---|---|
| R1 | `01_project_charter.md`    | `docs/sdlc/01_planning/01_project_charter.md`      |
| R2 | `02_feasibility_study.md`  | `docs/sdlc/01_planning/02_feasibility_study.md`    |
| R3 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` |
| R4 | `04_tech_stack_decision.md`| `docs/sdlc/01_planning/04_tech_stack_decision.md`  |
| R5 | `05_innovation_proposal.md`| `docs/sdlc/01_planning/05_innovation_proposal.md`  |
| R6 | `narasi.txt`               | `docs/sdlc/narasi.txt`                             |

---

## Tahapan Implementasi (Low-Level Checklist)

> **ATURAN PENTING UNTUK EXECUTOR:**
> - Ikuti setiap tahap secara **berurutan dari Tahap 1 hingga Tahap 9**. Jangan melompati tahap.
> - Setiap checklist `[ ]` wajib diselesaikan dan ditandai `[x]` sebelum berpindah ke checklist berikutnya.
> - Catat temuan masalah di setiap sub-tahap secara eksplisit sebelum melanjutkan.
> - **Jangan menulis ulang dokumen sebelum Tahap 8.** Fase 1–7 adalah fase investigasi dan analisis murni.
> - Jika tidak ada masalah ditemukan pada sebuah sub-tahap, catat secara eksplisit: "TIDAK ADA MASALAH."

---

### TAHAP 1 — Pembacaan & Pemahaman Awal (Orientasi Konteks)

Tujuan: Membangun pemahaman penuh atas seluruh dokumen yang relevan sebelum analisis dimulai.

- [ ] **1.1** Baca seluruh isi `docs/sdlc/02_analysis/01_business_requirements.md` dari baris pertama hingga baris terakhir tanpa melewati satu pun bagian.
- [ ] **1.2** Baca seluruh isi `docs/sdlc/01_planning/01_project_charter.md` dari awal hingga akhir.
- [ ] **1.3** Baca seluruh isi `docs/sdlc/01_planning/02_feasibility_study.md` dari awal hingga akhir.
- [ ] **1.4** Baca seluruh isi `docs/sdlc/01_planning/03_stakeholder_register.md` dari awal hingga akhir.
- [ ] **1.5** Baca seluruh isi `docs/sdlc/01_planning/04_tech_stack_decision.md` dari awal hingga akhir.
- [ ] **1.6** Baca seluruh isi `docs/sdlc/01_planning/05_innovation_proposal.md` dari awal hingga akhir.
- [ ] **1.7** Baca seluruh isi `docs/sdlc/narasi.txt` dari awal hingga akhir.
- [ ] **1.8** Identifikasi dan catat secara eksplisit seluruh entitas kunci berikut dari semua file referensi di atas:
  - Daftar seluruh modul sistem beserta kode modul yang disebutkan di file referensi.
  - Daftar seluruh stakeholder (internal & eksternal) beserta kode ID dan peran/role-nya.
  - Seluruh angka numerik bisnis kritis (ROI, NPV, Payback Period, CAPEX, target laba, UMR, batas kasbon, threshold PPOB, limit persentase, toleransi stok, waktu respons, dll.).
  - Seluruh batasan teknologi yang bersifat mandatori (Python, MySQL, CLI, bcrypt, JWT, ACID, library decimal, dll.).
  - Seluruh kode referensi yang ada di dokumen referensi (misal: `[F-1.1]`, `[N-3.3]`, `[INV-INT-22]`, `[STK-001]`, dll.) beserta deskripsi singkat masing-masing.

---

### TAHAP 2 — Validasi Kelengkapan: Komparasi BRD vs Semua File Referensi

Tujuan: Memastikan tidak ada data, fitur, stakeholder, atau aturan bisnis yang hilang dari dokumen BRD dibandingkan sumber referensinya.

#### 2.1 — Komparasi terhadap Project Charter (`R1`)

- [ ] **2.1.1** Buat daftar lengkap semua modul yang didefinisikan di `01_project_charter.md`. Kemudian periksa satu per satu apakah setiap modul tersebut telah tercantum dan dideskripsikan di dalam BRD dengan cakupan yang memadai.
- [ ] **2.1.2** Buat daftar lengkap semua kode kebutuhan fungsional `[F-X.X]` dari Project Charter. Kemudian periksa satu per satu apakah setiap kode tersebut telah diderivasi menjadi minimal satu kebutuhan bisnis `BR-F-XX` di BRD dan tercantum di kolom "Sumber Data".
- [ ] **2.1.3** Buat daftar lengkap semua kode kebutuhan non-fungsional `[N-X.X]` dari Project Charter. Kemudian periksa satu per satu apakah setiap kode tersebut telah diderivasi menjadi minimal satu kebutuhan bisnis `BR-NF-XX` di BRD dan tercantum di kolom "Sumber Data".
- [ ] **2.1.4** Periksa apakah angka-angka finansial kritis (CAPEX total, target ROI, NPV, Payback Period) yang tercantum di Project Charter konsisten dan sama persis dengan nilai yang tertulis di BRD. Catat setiap ketidaksesuaian nilai.
- [ ] **2.1.5** Periksa apakah ruang lingkup proyek (in-scope dan out-of-scope) di Project Charter selaras dengan batasan yang dideklarasikan di BRD. Catat setiap item ruang lingkup yang tidak sinkron.
- [ ] **2.1.6** Catat setiap item dari Project Charter yang **tidak ditemukan atau tidak diderivasi** di BRD sebagai temuan `[MISSING-Charter-XX]`.

#### 2.2 — Komparasi terhadap Feasibility Study (`R2`)

- [ ] **2.2.1** Periksa apakah semua angka numerik kelayakan ekonomi (ROI, NPV, IRR jika ada, Payback Period, BEP) dari Feasibility Study tercantum di BRD dengan nilai yang identik. Catat setiap ketidaksesuaian.
- [ ] **2.2.2** Periksa apakah seluruh prasyarat kelayakan operasional (kebutuhan SDM, infrastruktur, pelatihan staf) yang teridentifikasi di Feasibility Study telah muncul sebagai kebutuhan bisnis atau asumsi/ketergantungan di BRD.
- [ ] **2.2.3** Periksa apakah status keputusan kelayakan ("GO WITH CONDITIONS" atau apapun statusnya) dicantumkan secara eksplisit di BRD.
- [ ] **2.2.4** Periksa apakah risiko-risiko utama yang diidentifikasi di Feasibility Study telah terwakili di bagian manajemen risiko BRD.
- [ ] **2.2.5** Catat setiap item dari Feasibility Study yang **tidak ditemukan** di BRD sebagai temuan `[MISSING-Feasibility-XX]`.

#### 2.3 — Komparasi terhadap Stakeholder Register (`R3`)

- [ ] **2.3.1** Hitung jumlah total stakeholder yang terdaftar di `03_stakeholder_register.md`. Kemudian bandingkan dengan jumlah yang disebutkan di BRD (BRD Bagian 1.2 menyebut "19 pemangku kepentingan"). Pastikan angkanya konsisten.
- [ ] **2.3.2** Untuk setiap kode stakeholder internal (`STK-00X`) dari Stakeholder Register, periksa apakah perannya telah terakomodasi dalam tabel RBAC hak akses BRD (Bagian 5.3). Catat yang tidak ada.
- [ ] **2.3.3** Untuk setiap kode stakeholder eksternal dari Stakeholder Register, periksa apakah disebutkan di BRD Bagian 5.4. Catat yang tidak ada.
- [ ] **2.3.4** Periksa konsistensi nama peran/role (misal: `kepala_percetakan`, `kasir`, `pramuniaga`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang`, `pemilik`) antara Stakeholder Register dengan tabel RBAC di BRD. Catat setiap perbedaan nama atau typo sebagai inkonsistensi.
- [ ] **2.3.5** Catat setiap stakeholder dari Register yang **tidak ditemukan atau tidak terwakili** di BRD sebagai temuan `[MISSING-Stakeholder-STK-XX]`.

#### 2.4 — Komparasi terhadap Tech Stack Decision (`R4`)

- [ ] **2.4.1** Buat daftar semua keputusan teknologi yang bersifat mandatori dari `04_tech_stack_decision.md` (bahasa pemrograman, database, paradigma antarmuka, library utama keamanan, dll.). Kemudian periksa apakah setiap keputusan tersebut telah disebutkan sebagai kebutuhan non-fungsional `BR-NF-XX` di BRD.
- [ ] **2.4.2** Periksa apakah keputusan keamanan dari Tech Stack (enkripsi password dengan bcrypt, otentikasi sesi dengan JWT, transaksi ACID di MySQL, kontrol akses RBAC) tercermin secara eksplisit di kebutuhan bisnis BRD.
- [ ] **2.4.3** Periksa apakah batasan platform (berjalan di lingkungan lokal/LAN, tanpa dependensi koneksi internet aktif untuk operasional inti, atau batasan lain yang disebutkan di Tech Stack) tercermin di bagian ruang lingkup, asumsi, atau kebutuhan non-fungsional BRD.
- [ ] **2.4.4** Periksa apakah library `decimal` Python untuk presisi kalkulasi BOM disebutkan secara eksplisit di kebutuhan bisnis terkait (contoh: BR-F-07 atau equivalen).
- [ ] **2.4.5** Catat setiap keputusan teknis mandatori dari Tech Stack yang **tidak terwakili** di BRD sebagai temuan `[MISSING-TechStack-XX]`.

#### 2.5 — Komparasi terhadap Innovation Proposal (`R5`)

- [ ] **2.5.1** Buat daftar lengkap seluruh kode inovasi dari `05_innovation_proposal.md`. Pisahkan berdasarkan kategori: inovasi terintegrasi (`[INV-INT-XX]`), inovasi direkomendasikan (`[INV-REC-XX]`), dan inovasi baru (`[INV-NEW-XX]`).
- [ ] **2.5.2** Untuk setiap kode inovasi dari daftar di atas, periksa apakah kode tersebut direferensikan di kolom "Sumber Data" pada salah satu kebutuhan bisnis (`BR-F-XX` atau `BR-NF-XX`) di BRD.
- [ ] **2.5.3** Identifikasi dan catat kode inovasi dari Innovation Proposal yang sama sekali **tidak disebutkan** di BRD manapun sebagai temuan `[MISSING-INV-XX]`.
- [ ] **2.5.4** Untuk setiap inovasi yang tidak direferensikan, tentukan apakah inovasi tersebut **seharusnya masuk** ke BRD (karena bersifat kebutuhan bisnis) atau memang sengaja tidak dimasukkan karena merupakan detail teknis implementasi yang menjadi domain SRS/SDD.

#### 2.6 — Komparasi terhadap Narasi Pemilik Usaha (`R6`)

- [ ] **2.6.1** Baca ulang `docs/sdlc/narasi.txt` dan ekstrak daftar: (a) semua pain point yang dikeluhkan pemilik, (b) semua harapan dan mandat solusi pemilik, (c) semua alur kerja manual per divisi yang dideskripsikan.
- [ ] **2.6.2** Untuk setiap pain point dari narasi, periksa apakah sudah terwakili di Bagian 4.2 (Identifikasi Titik Kelemahan) BRD.
- [ ] **2.6.3** Untuk setiap harapan solusi dari pemilik yang bersifat fungsional, periksa apakah sudah diterjemahkan menjadi kebutuhan bisnis `BR-F-XX` di BRD.
- [ ] **2.6.4** Periksa konsistensi detail operasional spesifik dari narasi (seperti: nominal threshold PPOB, jumlah akun e-wallet, jumlah staf yang akan direkrut, nama bank mitra, nama penyedia saldo PPOB) dengan nilai yang tertulis di BRD.
- [ ] **2.6.5** Catat setiap item narasi pemilik yang **tidak ditemukan di BRD** sebagai temuan `[MISSING-Narasi-XX]`.

---

### TAHAP 3 — Validasi Kebersihan Konten: Relevansi & Fokus Dokumen

Tujuan: Memastikan BRD **hanya** memuat data dan informasi yang benar-benar merupakan domain kebutuhan bisnis, dan tidak terkontaminasi oleh detail teknis implementasi yang bukan ranah BRD.

- [ ] **3.1** Baca ulang seluruh bagian kebutuhan fungsional (Bagian 7) dan non-fungsional (Bagian 8) BRD dengan kritis.
- [ ] **3.2** Identifikasi setiap kebutuhan yang terlalu detail secara teknis, misalnya: menyebutkan nama tabel database MySQL secara spesifik, nama kolom, nama fungsi/method Python, algoritma implementasi, atau detail kode program. Konten seperti ini seharusnya berada di SRS atau SDD — catat sebagai temuan `[OVER-SPEC-XX]`.
- [ ] **3.3** Identifikasi setiap kebutuhan yang terlalu abstrak atau generik sehingga tidak memberikan panduan yang cukup bagi pembuat SRS (contoh: "sistem harus memudahkan pekerjaan staf" tanpa ada aturan bisnis yang konkret) — catat sebagai temuan `[UNDER-SPEC-XX]`.
- [ ] **3.4** Verifikasi bahwa setiap `BR-F-XX` dan `BR-NF-XX` memiliki **semua** atribut berikut secara lengkap: **Deskripsi**, **Aktor Terkait**, **Aturan Bisnis**, **Kriteria Penerimaan**, **Prioritas**, dan **Sumber Data**. Catat kebutuhan bisnis yang tidak lengkap strukturnya sebagai temuan `[INCOMPLETE-BR-XX]`.
- [ ] **3.5** Verifikasi bahwa nilai **Prioritas** setiap `BR-F-XX` dan `BR-NF-XX` (High/Medium/Low) logis dan konsisten dengan tingkat kekritisan bisnisnya. Catat setiap prioritas yang terlihat tidak proporsional sebagai temuan `[PRIORITY-MISMATCH-XX]`.
- [ ] **3.6** Verifikasi bahwa setiap aturan bisnis (`Aturan Bisnis`) di setiap `BR-F-XX` bersifat **terukur dan spesifik**, bukan kalimat ambigu seperti "sistem harus cepat" atau "sistem harus aman". Catat kalimat ambigu sebagai temuan `[AMBIGUOUS-RULE-XX]`.
- [ ] **3.7** Verifikasi bahwa setiap Kriteria Penerimaan (`Kriteria Penerimaan`) bersifat **dapat diuji (testable)** — artinya ada kondisi masukan (*input*) yang jelas dan keluaran (*output* atau *outcome*) yang dapat diverifikasi. Catat kriteria yang tidak bisa diuji secara objektif sebagai temuan `[UNTESTABLE-AC-XX]`.

---

### TAHAP 4 — Validasi Standar Struktur Dokumen BRD Industri

Tujuan: Memastikan dokumen BRD memiliki struktur, seksi, dan kelengkapan yang sesuai standar praktik industri (BABOK v3 / IEEE 830-compatible).

- [ ] **4.1** Verifikasi keberadaan dan kelengkapan **Riwayat Perubahan Dokumen** (Document Change Log). Pastikan kolom: Versi, Tanggal, Perubahan, dan Oleh tersedia dan terisi dengan benar.
- [ ] **4.2** Verifikasi keberadaan bagian **Informasi Dokumen** yang mencakup semua sub-bagian: Tujuan Dokumen, Cakupan Dokumen, Posisi dalam SDLC, Hubungan dengan Dokumen Lain, dan Audiens Target.
- [ ] **4.3** Verifikasi keberadaan dan kualitas **Ringkasan Eksekutif** — pastikan sudah merangkum: konteks masalah bisnis, solusi yang diusulkan, nilai investasi, dan keputusan strategis secara ringkas namun informatif.
- [ ] **4.4** Verifikasi keberadaan dan kelengkapan bagian **Profil Bisnis & Konteks Operasional**, termasuk: deskripsi usaha, struktur organisasi (kondisi saat ini dan rencana), daftar kategori layanan/produk per divisi, budaya kerja, dan sumber pendanaan.
- [ ] **4.5** Verifikasi keberadaan dan kelengkapan bagian **Analisis Proses Bisnis As-Is** untuk setiap divisi usaha yang relevan.
- [ ] **4.6** Verifikasi keberadaan bagian **Identifikasi Titik Kelemahan (Pain Points)** yang dianalisis dari proses As-Is secara konkret.
- [ ] **4.7** Verifikasi keberadaan dan kelengkapan bagian **Proses Bisnis To-Be** yang menggambarkan transformasi alur kerja setelah sistem diterapkan (disarankan menggunakan diagram atau narasi berurutan).
- [ ] **4.8** Verifikasi keberadaan bagian **Pemangku Kepentingan (Stakeholder)** yang mencakup: daftar aktor internal dengan role-nya, daftar aktor eksternal, kebutuhan dan ekspektasi per aktor, dan tabel RBAC hak akses menu sistem.
- [ ] **4.9** Verifikasi keberadaan bagian **Tujuan Bisnis (Business Goals)** yang mencakup tujuan umum dan tujuan SMART (Specific, Measurable, Achievable, Relevant, Time-bound) yang terukur.
- [ ] **4.10** Verifikasi keberadaan bagian **Manfaat Bisnis (Business Benefits)** yang mencakup manfaat kuantitatif (dengan angka) dan manfaat kualitatif.
- [ ] **4.11** Verifikasi keberadaan bagian **Kebutuhan Fungsional (Functional Requirements)** yang dikelompokkan per modul dengan format terstruktur.
- [ ] **4.12** Verifikasi keberadaan bagian **Kebutuhan Non-Fungsional (Non-Functional Requirements)** yang mencakup minimal: kinerja (*performance*), keamanan (*security*), kegunaan (*usability*), keandalan (*reliability*), kepatuhan (*compliance*), dan kemudahan pemeliharaan (*maintainability*).
- [ ] **4.13** Verifikasi keberadaan bagian **Asumsi dan Ketergantungan (Assumptions & Dependencies)**. Ini adalah bagian yang sering absen namun kritis untuk menjelaskan prasyarat yang harus dipenuhi agar proyek dapat berjalan. Jika bagian ini tidak ada, tandai sebagai temuan `[MISSING-SECTION-AsumpsiKetergantungan]`.
- [ ] **4.14** Verifikasi keberadaan bagian **Manajemen Risiko Bisnis** yang mencakup: identifikasi risiko, dampak, probabilitas, dan strategi mitigasi untuk setiap risiko.
- [ ] **4.15** Verifikasi keberadaan bagian **Kriteria Keberhasilan & Penerimaan Bisnis (Business Acceptance Criteria)** di level dokumen keseluruhan (bukan hanya di level kebutuhan individual).
- [ ] **4.16** Verifikasi keberadaan **Glosarium Istilah Domain** yang mencakup semua istilah teknis bisnis dan domain percetakan yang digunakan dalam dokumen.
- [ ] **4.17** Verifikasi keberadaan **Daftar Referensi Dokumen** yang lengkap di bagian akhir dokumen.
- [ ] **4.18** Catat setiap seksi yang **tidak ada atau tidak lengkap** sebagai temuan `[MISSING-SECTION-XX]`.
- [ ] **4.19** Verifikasi konsistensi penomoran seksi dari awal hingga akhir dokumen — pastikan tidak ada nomor yang loncat, berulang, atau tidak berurutan.

---

### TAHAP 5 — Validasi Kesiapan sebagai Input Fase SDLC Berikutnya

Tujuan: Memastikan BRD ini cukup lengkap dan berkualitas untuk dijadikan sebagai **referensi primer** bagi pembuatan SRS, SDD, dan Test Plan.

- [ ] **5.1** Baca ulang setiap `BR-F-XX`. Verifikasi bahwa setiap kebutuhan dirumuskan dengan cukup spesifik sehingga seorang engineer yang membuat SRS dapat langsung mendefinisikan *use case* atau *user story* dari kebutuhan tersebut **tanpa perlu menebak-nebak maksudnya**. Catat yang tidak memenuhi sebagai temuan `[NOT-SRS-READY-XX]`.
- [ ] **5.2** Baca ulang setiap `BR-NF-XX`. Verifikasi bahwa setiap kebutuhan memiliki nilai parameter yang cukup spesifik sehingga seorang engineer dapat langsung mentranslasikannya menjadi *test case* kinerja atau keamanan. Contoh yang baik: "waktu respons penyimpanan transaksi < 1 detik". Contoh yang buruk: "sistem harus responsif". Catat yang tidak memenuhi sebagai temuan `[NOT-SRS-READY-NF-XX]`.
- [ ] **5.3** Verifikasi bahwa tabel RBAC (Bagian 5.3) cukup lengkap dan granular untuk langsung dijadikan sebagai dasar desain sistem otentikasi dan otorisasi di SDD. Periksa apakah ada menu sistem penting yang belum terdefinisi hak aksesnya per role.
- [ ] **5.4** Verifikasi bahwa diagram atau narasi proses bisnis To-Be (Bagian 4.3) cukup lengkap untuk dijadikan sebagai dasar desain diagram alur sistem (*flowchart* atau *sequence diagram*) di SDD.
- [ ] **5.5** Verifikasi bahwa seluruh aturan bisnis numerik yang kritis (threshold, batas limit, target, formula kalkulasi) telah didokumentasikan secara eksplisit di BRD sehingga tidak ada nilai yang harus "dikira-kira" oleh engineer berikutnya.
- [ ] **5.6** Verifikasi bahwa BRD mendefinisikan dengan jelas **mana yang In-Scope dan Out-of-Scope** dari sistem, sehingga tim developer tidak akan membangun fitur di luar batas yang disepakati.
- [ ] **5.7** Verifikasi bahwa Kriteria Penerimaan pada setiap `BR-F-XX` cukup spesifik untuk dapat langsung dijadikan sebagai dasar penulisan skenario pengujian (*test scenario*) di Test Plan tanpa interpretasi tambahan.
- [ ] **5.8** Catat setiap kebutuhan yang **terlalu ambigu** untuk dijadikan basis SRS, SDD, atau Test Plan sebagai temuan `[NOT-SRS-READY-XX]`.

---

### TAHAP 6 — Validasi Bahasa & Komunikasi

Tujuan: Memastikan seluruh dokumen menggunakan Bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau LLM model AI yang lebih murah.

- [ ] **6.1** Baca ulang seluruh dokumen BRD sekali lagi dengan perspektif sebagai **junior programmer yang baru bergabung** dan belum pernah membaca satu pun dokumen referensi sebelumnya.
- [ ] **6.2** Identifikasi setiap kalimat atau paragraf yang dapat memiliki **lebih dari satu interpretasi** (ambigu) — catat sebagai temuan `[AMBIGUOUS-LANG-XX]`.
- [ ] **6.3** Identifikasi setiap penggunaan istilah domain teknis atau bisnis percetakan yang **tidak didefinisikan di Glosarium** — catat sebagai temuan `[UNDEFINED-TERM-XX]` dan rekomendasikan untuk ditambahkan ke Glosarium.
- [ ] **6.4** Identifikasi setiap kalimat yang menggunakan **struktur bahasa yang tidak natural dalam Bahasa Indonesia**, misalnya: kalimat pasif yang membingungkan, kalimat terlalu panjang dengan banyak anak kalimat bersyarat, atau pencampuran istilah teknis Inggris dan awam Indonesia yang tidak konsisten — catat sebagai temuan `[BAD-LANG-XX]`.
- [ ] **6.5** Verifikasi konsistensi penggunaan istilah di seluruh dokumen. Pastikan satu konsep hanya menggunakan satu istilah yang sama (contoh: jangan gunakan "staf kasir" di satu tempat dan "kasir" di tempat lain secara bergantian tanpa alasan). Catat inkonsistensi sebagai temuan `[INCONSISTENT-TERM-XX]`.
- [ ] **6.6** Verifikasi bahwa seluruh singkatan dan akronim (BRD, SDLC, CLI, BOM, HPP, RBAC, PPOB, JWT, UMR, ACID, NIB, dll.) **telah dideklarasikan kepanjangannya** minimal pada pertama kali muncul di dalam dokumen.
- [ ] **6.7** Verifikasi konsistensi format angka numerik Bahasa Indonesia di seluruh dokumen: pemisah ribuan menggunakan titik (`.`) dan pemisah desimal menggunakan koma (`,`). Contoh benar: `Rp 1.000.000`. Contoh salah: `Rp 1,000,000`. Catat inkonsistensi sebagai temuan `[FORMAT-NUMBER-XX]`.

---

### TAHAP 7 — Validasi Data Kosong & Placeholder

Tujuan: Mengidentifikasi dan mengisi semua data yang masih kosong, belum tersedia, atau berbentuk placeholder.

- [ ] **7.1** Lakukan pencarian penuh pada dokumen BRD untuk menemukan semua teks yang mengandung kata atau pola berikut: `[BELUM TERSEDIA`, `[DIISI`, `[PLACEHOLDER`, `TBD`, `N/A`, `TODO`, atau pola `{...}` (kurung kurawal sebagai placeholder). Catat setiap lokasi dan baris yang ditemukan beserta konteks kalimatnya.
- [ ] **7.2** Untuk setiap placeholder yang ditemukan di langkah 7.1, lakukan analisis berikut:
  - Apakah data tersebut **dapat diisi berdasarkan konteks dan inferensi logis dari dokumen referensi** (R1–R6)?
  - Atau apakah data tersebut **harus diisi manual oleh pemilik usaha** karena merupakan informasi privat yang tidak tersedia di dokumen manapun (misal: alamat fisik toko, nomor rekening, UMR daerah spesifik)?
- [ ] **7.3** Untuk setiap placeholder yang **dapat diisi dari konteks referensi** atau dari inferensi logis yang masih dalam ruang lingkup dokumen ini: **isi dengan data yang paling relean, logis, dan sesuai**. Sertakan catatan singkat tentang dasar pengisian data tersebut.
- [ ] **7.4** Untuk setiap placeholder yang **wajib diisi manual oleh pemilik** karena bersifat data privat: ubah format placeholder menjadi **catatan instruksi yang jelas** kepada pemilik usaha dengan format: `> ⚠️ PERLU DIISI PEMILIK: [Instruksi pengisian yang spesifik dan jelas]`.
- [ ] **7.5** Verifikasi bahwa tidak ada **data numerik kritis** yang masih berbentuk "contoh sementara" (contoh: `Contoh: Rp X`) yang dapat disalahartikan sebagai nilai resmi di versi final. Setiap angka harus merupakan nilai yang telah ditetapkan atau instruksi pengisian yang jelas.
- [ ] **7.6** Verifikasi bahwa seluruh referensi silang internal di dalam dokumen (misal: "lihat Bagian X.Y" atau "sesuai aturan BR-F-XX") masih valid dan menunjuk ke bagian atau kode yang benar dan ada di dalam dokumen.

---

### TAHAP 8 — Penulisan Ulang Menyeluruh & Penyimpanan Final

> **PERINGATAN KRITIS UNTUK EXECUTOR: INI ADALAH TAHAP PENULISAN.**
>
> Lakukan penulisan ulang dokumen secara menyeluruh dalam satu proses yang tidak terputus. Pastikan Anda memiliki seluruh daftar perbaikan dari Tahap 1–7 sebelum mulai menulis. Jangan menulis secara parsial atau bertahap yang menghasilkan file tidak lengkap.

#### 8.1 — Persiapan Sebelum Menulis

- [ ] **8.1.1** Kompilasi seluruh temuan dari Tahap 2 hingga 7 ke dalam satu daftar tindakan perbaikan terstruktur. Kelompokkan menjadi: (a) Konten Hilang yang harus ditambahkan, (b) Seksi tidak lengkap yang harus dilengkapi, (c) Perbaikan bahasa, (d) Pengisian placeholder, (e) Koreksi nilai atau inkonsistensi data.
- [ ] **8.1.2** Tentukan urutan penulisan ulang konten berdasarkan struktur dokumen yang telah divalidasi di Tahap 4. Buat kerangka (*outline*) lengkap dokumen sebelum mulai menulis.
- [ ] **8.1.3** Siapkan daftar seluruh konten baru yang akan **ditambahkan** ke dokumen (seksi baru, kebutuhan bisnis baru, istilah glosarium baru, referensi baru).
- [ ] **8.1.4** Siapkan daftar seluruh konten yang akan **dihapus** karena terbukti tidak relevan, out-of-scope untuk BRD, atau terduplikasi.

#### 8.2 — Penulisan Ulang Dokumen

- [ ] **8.2.1** Tulis ulang dokumen BRD secara **menyeluruh dan lengkap** mulai dari baris pertama (header YAML frontmatter) hingga baris terakhir (daftar referensi dokumen). **Tidak ada bagian yang boleh diringkas, dipotong, atau dilompati. Seluruh teks dari baris pertama hingga terakhir harus ditulis ulang sepenuhnya (no truncation).**
- [ ] **8.2.2** Ubah nomor versi di YAML frontmatter dari `versi: 1.0` menjadi `versi: 1.1`.
- [ ] **8.2.3** Ubah `status` di YAML frontmatter dari `Draft` menjadi `Revised`.
- [ ] **8.2.4** Perbarui `tanggal` di YAML frontmatter ke tanggal penulisan ulang dilakukan (tanggal saat eksekusi issue ini).
- [ ] **8.2.5** Tambahkan satu baris baru di tabel **Riwayat Perubahan Dokumen** untuk mencatat revisi v1.1. Baris baru wajib berisi: Versi `1.1`, Tanggal hari ini, Perubahan (ringkasan komprehensif semua perbaikan yang dilakukan dalam 1–3 kalimat), Oleh (nama Persona Executor).
- [ ] **8.2.6** Terapkan semua perbaikan dari daftar temuan Tahap 2–7 ke dalam konten yang ditulis ulang. Jangan lewatkan satu pun poin perbaikan.
- [ ] **8.2.7** Pastikan seluruh seksi yang wajib ada (hasil validasi Tahap 4, poin 4.1–4.17) hadir lengkap di dokumen yang ditulis ulang. Jika ada seksi yang belum ada di versi lama, tambahkan sebagai seksi baru dengan konten yang relean.
- [ ] **8.2.8** Pastikan tidak ada placeholder `[BELUM TERSEDIA...]` atau `{...}` yang masih tertinggal dalam bentuk aslinya, kecuali yang memang wajib diisi manual oleh pemilik dan sudah diubah menjadi format catatan instruksi (sesuai hasil Tahap 7.4).

#### 8.3 — Penyimpanan ke Target File (Overwrite)

- [ ] **8.3.1** Simpan hasil penulisan ulang **langsung menimpa (overwrite)** file yang ada di path: `docs/sdlc/02_analysis/01_business_requirements.md`.
- [ ] **8.3.2** Pastikan penyimpanan dilakukan **dalam satu operasi tulis tunggal** yang mencakup seluruh konten dari baris pertama hingga baris terakhir. Jangan menyimpan secara bertahap atau per-bagian yang berisiko menghasilkan file tidak lengkap.
- [ ] **8.3.3** Setelah penyimpanan selesai, baca kembali file yang telah disimpan dari baris pertama hingga baris terakhir untuk **verifikasi integritas konten** — pastikan tidak ada konten yang terpotong, hilang di tengah, atau corrupt.
- [ ] **8.3.4** Verifikasi bahwa versi dokumen di dalam file tersimpan adalah `v1.1` dan bukan `v1.0`.
- [ ] **8.3.5** Verifikasi bahwa jumlah total baris file hasil revisi **sama atau lebih banyak** dari file original (847 baris). Jika lebih sedikit, periksa ulang apakah ada konten yang tidak sengaja terhapus sebelum menyimpan final.

#### 8.4 — Pembaruan Daftar Referensi Dokumen

- [ ] **8.4.1** Jika selama proses validasi dan perbaikan Tahap 2–7 ditemukan kebutuhan untuk merujuk ke dokumen atau sumber referensi **tambahan** yang belum ada di tabel Referensi Dokumen (bagian akhir BRD), tambahkan entri baru tersebut di bagian paling bawah tabel referensi.
- [ ] **8.4.2** Pastikan setiap entri referensi tambahan memiliki semua kolom yang lengkap: Nomor urut, Nama berkas, Path relatif yang valid, dan Keterangan singkat relevansi referensi tersebut.
- [ ] **8.4.3** Verifikasi bahwa semua path relatif di seluruh tabel referensi dapat diakses dari root direktori proyek — jangan mencantumkan path yang tidak ada atau salah.

---

### TAHAP 9 — Verifikasi Akhir & Pelaporan

- [ ] **9.1** Baca kembali dokumen BRD hasil revisi dari awal hingga akhir satu kali lagi sebagai verifikasi akhir menyeluruh sebelum issue dinyatakan selesai.
- [ ] **9.2** Konfirmasi bahwa dokumen telah memenuhi **seluruh** kriteria keberhasilan issue ini:
  - [ ] **9.2.1** Semua data dari 6 file referensi (R1–R6) yang relevan untuk BRD telah terakomodasi.
  - [ ] **9.2.2** Tidak ada data atau informasi yang berada di luar ruang lingkup domain BRD yang masih tertinggal.
  - [ ] **9.2.3** Struktur dokumen lengkap sesuai standar industri BRD (semua seksi wajib ada).
  - [ ] **9.2.4** Dokumen siap dijadikan sebagai input primer pembuatan SRS, SDD, dan Test Plan.
  - [ ] **9.2.5** Bahasa Indonesia yang digunakan natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau LLM model AI yang lebih murah.
  - [ ] **9.2.6** Tidak ada data kosong atau placeholder yang tidak terselesaikan.
  - [ ] **9.2.7** Versi dokumen telah diperbarui ke v1.1 dan status menjadi `Revised`.
  - [ ] **9.2.8** File telah berhasil disimpan ke `docs/sdlc/02_analysis/01_business_requirements.md`.
- [ ] **9.3** Buat dan tampilkan ringkasan laporan akhir yang mencantumkan:
  - Total jumlah temuan yang ditemukan (dikelompokkan per kategori: MISSING, OVER-SPEC, INCOMPLETE, AMBIGUOUS, dll.).
  - Total jumlah perbaikan yang berhasil diterapkan.
  - Daftar semua placeholder yang diisi beserta nilai/instruksi yang digunakan.
  - Daftar semua seksi baru yang berhasil ditambahkan (jika ada).
  - Daftar semua konten yang dihapus karena out-of-scope (jika ada).
  - Pernyataan konfirmasi final bahwa dokumen BRD v1.1 telah siap digunakan sebagai input primer fase SDLC berikutnya.

---

## Kriteria Validasi Tambahan Khusus Dokumen BRD

> Berikut adalah kaidah standar tambahan yang khusus berlaku untuk tipe dokumen **Business Requirements Document (BRD)** dan wajib diperiksa sebagai bagian dari validasi menyeluruh:

### A. Traceability Matrix (Ketertelusuran Kebutuhan)

- [ ] **A.1** Verifikasi bahwa setiap `BR-F-XX` memiliki atribut **Sumber Data** yang mencantumkan kode referensi spesifik dari dokumen sumber (contoh: `Project Charter v1.1 Bagian 8.1 [F-1.1]`, `Innovation Proposal v1.1 [INV-INT-22]`). Kebutuhan bisnis tanpa sumber data yang jelas adalah kebutuhan yang tidak dapat diverifikasi asal-usulnya — tidak dapat diterima dalam BRD berkualitas industri.
- [ ] **A.2** Verifikasi bahwa tidak ada `BR-F-XX` yang muncul tanpa dasar referensi yang jelas (kebutuhan "asal muncul" yang tidak dapat ditelusuri ke dokumen sumber manapun). Catat sebagai temuan `[NO-SOURCE-BR-XX]`.

### B. Kejelasan Aturan Bisnis Numerik

- [ ] **B.1** Buat daftar lengkap **semua angka numerik bisnis kritis** yang disebutkan di BRD. Contoh: threshold saldo PPOB Rp 150.000, deposit minimal PPOB Rp 500.000, target laba bulanan Rp 15.000.000, persentase payroll laba 25%, jaminan minimum gaji 50% UMR, batas kasbon Rp 1.000.000 atau 30% gaji, toleransi selisih stok 1.0%, waktu respons laporan < 5 detik, waktu simpan transaksi < 1 detik, jumlah staf 7, jumlah e-wallet 6, jumlah akun PPOB 2, dll.
- [ ] **B.2** Untuk setiap angka numerik dari daftar di atas, verifikasi bahwa nilainya **konsisten** dengan yang tertera di dokumen referensi (R1–R6). Catat setiap inkonsistensi nilai sebagai temuan `[VALUE-MISMATCH-XX]`.
- [ ] **B.3** Verifikasi bahwa tidak ada angka numerik kritis yang masih berbentuk "nilai contoh sementara" atau "perkiraan" yang dapat menimbulkan kebingungan atau salah interpretasi di fase berikutnya.

### C. Konsistensi Nama Modul & Kode Kebutuhan

- [ ] **C.1** Verifikasi bahwa nama-nama modul yang disebutkan di BRD (M.1, M.2, ..., hingga M.9 atau sesuai isi dokumen) konsisten dengan nama modul yang ada di Project Charter dan Innovation Proposal. Catat setiap perbedaan penamaan.
- [ ] **C.2** Verifikasi bahwa kode `BR-F-XX` dan `BR-NF-XX` tidak ada yang terduplikasi (dua kebutuhan berbeda dengan kode yang sama) dan penomorannya berurutan secara logis tanpa loncat nomor.
- [ ] **C.3** Verifikasi bahwa total jumlah kebutuhan fungsional dan non-fungsional yang diklaim di Bagian 1.2 (Cakupan Dokumen) BRD sesuai dengan jumlah aktual `BR-F-XX` dan `BR-NF-XX` yang benar-benar ada di dalam dokumen.

### D. Kejelasan Batasan Sistem (System Boundary)

- [ ] **D.1** Verifikasi bahwa BRD secara eksplisit mendefinisikan **apa yang ADA di dalam sistem** (in-scope) dan **apa yang TIDAK ADA di dalam sistem** (out-of-scope) — ini krusial untuk mencegah *scope creep* saat engineer membuat SRS.
- [ ] **D.2** Verifikasi bahwa batasan integrasi sistem eksternal dinyatakan secara jelas. Contoh: apakah sistem terhubung ke API penyedia PPOB eksternal secara real-time, atau hanya mencatat transaksi secara manual? Apakah sistem terhubung ke API e-wallet, atau pemilik mengoperasikan e-wallet secara manual dan hanya input datanya ke sistem?

### E. Asumsi dan Ketergantungan yang Eksplisit

- [ ] **E.1** Verifikasi bahwa BRD secara eksplisit mendokumentasikan **asumsi bisnis** yang dibuat selama penyusunan. Contoh asumsi: internet toko tersedia dan stabil untuk fitur-fitur tertentu, semua karyawan baru akan mendapatkan pelatihan sistem sebelum go-live, data Excel lama pemilik tersedia dalam format CSV yang dapat diekspor, dll.
- [ ] **E.2** Verifikasi bahwa BRD secara eksplisit mendokumentasikan **ketergantungan proyek** yang dapat memblokir implementasi jika tidak terpenuhi. Contoh: ketersediaan infrastruktur Mini PC Server sebelum deployment, selesainya proses rekrutmen 7 staf sebelum go-live, tersedianya lisensi atau akses software yang dibutuhkan, dll.
- [ ] **E.3** Jika bagian Asumsi dan Ketergantungan **belum ada** di BRD, wajib ditambahkan sebagai seksi baru berdasarkan inferensi yang valid dari dokumen referensi (R1–R6).

### F. Kepatuhan Regulasi yang Eksplisit

- [ ] **F.1** Verifikasi bahwa kewajiban kepatuhan **UU PDP No. 27/2022** (Undang-Undang Pelindungan Data Pribadi) dinyatakan secara eksplisit sebagai kebutuhan non-fungsional dengan detail: data pribadi apa yang dilindungi (nomor WhatsApp pelanggan, data transaksi), mekanisme perlindungan apa yang diwajibkan (enkripsi, pembatasan akses RBAC, dll.), dan sanksi potensial atas kegagalan kepatuhan.
- [ ] **F.2** Verifikasi bahwa kebutuhan kepatuhan terkait **regulasi ketenagakerjaan Indonesia** (penggunaan kontrak PKWT/PKWTT, batas limit kasbon yang proporsional dan aman secara hukum, penghitungan gaji dengan acuan UMR daerah) dinyatakan secara eksplisit sebagai aturan bisnis dalam modul SDM dan Payroll.
- [ ] **F.3** Periksa apakah ada regulasi atau peraturan lain yang relevan untuk UMKM percetakan di Indonesia yang belum disebutkan di BRD namun seharusnya ada. Contoh: kewajiban menerbitkan bukti transaksi/nota, kewajiban menyimpan data keuangan dalam periode waktu tertentu, kewajiban pelaporan keuangan untuk pinjaman bank, atau kewajiban kepatuhan terkait Nomor Induk Berusaha (NIB).

### G. Kesiapan Desain Basis Data (Database Design Readiness)

- [ ] **G.1** Verifikasi bahwa seluruh entitas data utama bisnis (Pelanggan/CRM, Produk/Barang, Transaksi, Pesanan, Karyawan, Absensi, Payroll, Inventaris/Stok, Supplier, Pinjaman, Kas/Rekonsiliasi, Audit Trail, dll.) dapat diidentifikasi secara jelas dari kebutuhan bisnis yang ada di BRD. Jika ada entitas data penting yang tidak tersirat dari BRD manapun, catat sebagai temuan `[MISSING-ENTITY-XX]`.
- [ ] **G.2** Verifikasi bahwa kebutuhan multi-cabang (*multi-branch ready*) disebutkan secara eksplisit sebagai kebutuhan bisnis, termasuk implikasinya (setiap record data terkait dengan ID cabang).

---

## Contoh Format Pencatatan Temuan (Referensi Executor)

Gunakan format standar berikut saat mencatat temuan di setiap tahap analisis:

```
[MISSING-Charter-01]         : Kebutuhan [F-2.6] dari Project Charter (fitur laporan akhir bulan per divisi) tidak ditemukan padanannya di BRD manapun.
[MISSING-Feasibility-01]     : Nilai IRR yang tercantum di Feasibility Study tidak disebutkan di Executive Summary BRD.
[MISSING-Stakeholder-STK-14] : Stakeholder STK-014 dari Stakeholder Register tidak disebutkan di BRD Bagian 5.4.
[MISSING-TechStack-01]       : Keputusan penggunaan paradigma Functional Programming dari Tech Stack tidak tercermin di BR-NF manapun.
[MISSING-INV-15]             : Kode inovasi [INV-REC-01] dari Innovation Proposal tidak direferensikan di kolom Sumber Data manapun di BRD.
[MISSING-Narasi-01]          : Pain point "pesanan WhatsApp yang lupa dikerjakan" dari narasi.txt tidak disebutkan di Bagian 4.2 BRD.
[MISSING-SECTION-01]         : Bagian "Asumsi dan Ketergantungan" tidak ditemukan di BRD.
[OVER-SPEC-01]               : BR-F-07 menyebutkan nama tabel database MySQL secara spesifik — ini ranah SRS/SDD, bukan BRD.
[UNDER-SPEC-01]              : BR-F-24 tidak menjelaskan kondisi bisnis kapan notifikasi WhatsApp ini dipicu.
[INCOMPLETE-BR-15]           : BR-F-15 tidak memiliki atribut "Aturan Bisnis" — hanya ada Deskripsi dan Kriteria Penerimaan.
[AMBIGUOUS-RULE-07]          : Aturan bisnis BR-F-07 menyebut "presisi tinggi" tanpa mendefinisikan berapa angka desimal yang dimaksud.
[UNTESTABLE-AC-12]           : Kriteria penerimaan BR-F-12 berbunyi "sistem menampilkan notifikasi" tanpa mendefinisikan kondisi trigger yang spesifik dan terukur.
[PRIORITY-MISMATCH-01]       : BR-F-05 (Pelacakan Margin) diberi prioritas Medium padahal sangat kritis untuk penentuan HPP dan laba.
[NOT-SRS-READY-01]           : BR-F-06 tidak cukup spesifik — tidak menyebutkan format data dan struktur file .txt yang dihasilkan.
[VALUE-MISMATCH-01]          : BRD Bagian 6.2 menyebut target laba Rp 15.000.000 namun Feasibility Study mencantumkan nilai yang berbeda. Harus diklarifikasi dan diselaraskan.
[UNDEFINED-TERM-01]          : Istilah "finishing laminasi" digunakan di Bagian 4.1.1 namun tidak ada entri di Glosarium.
[INCONSISTENT-TERM-01]       : "Staf Kasir" dan "kasir" digunakan bergantian tanpa konsistensi di Bagian 5 dan Bagian 7.
[FORMAT-NUMBER-01]           : Bagian 6.3 menulis "Rp 2,000,000" (format AS) bukan "Rp 2.000.000" (format Indonesia).
[NO-SOURCE-BR-01]            : BR-F-25 tidak memiliki atribut Sumber Data — tidak dapat diverifikasi asal-usulnya.
[AMBIGUOUS-LANG-01]          : Kalimat di Bagian 4.3 poin 6 dapat diinterpretasikan dengan dua cara berbeda terkait siapa yang berwenang mengubah status pesanan.
[MISSING-ENTITY-01]          : Entitas data "Log Audit Trail" tidak tersirat secara eksplisit dari kebutuhan bisnis manapun di BRD.
```

---

## Referensi Dokumen Issue Ini

| #  | File                          | Path                                                | Keterangan                              |
|---|---|---|---|
| 1  | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | Target file utama yang divalidasi       |
| 2  | `01_project_charter.md`       | `docs/sdlc/01_planning/01_project_charter.md`       | Referensi R1 — Ruang lingkup & modul   |
| 3  | `02_feasibility_study.md`     | `docs/sdlc/01_planning/02_feasibility_study.md`     | Referensi R2 — Kelayakan ekonomi        |
| 4  | `03_stakeholder_register.md`  | `docs/sdlc/01_planning/03_stakeholder_register.md`  | Referensi R3 — Profil stakeholder       |
| 5  | `04_tech_stack_decision.md`   | `docs/sdlc/01_planning/04_tech_stack_decision.md`   | Referensi R4 — Batasan teknologi        |
| 6  | `05_innovation_proposal.md`   | `docs/sdlc/01_planning/05_innovation_proposal.md`   | Referensi R5 — Parameter 42 inovasi    |
| 7  | `narasi.txt`                  | `docs/sdlc/narasi.txt`                              | Referensi R6 — Narasi asli pemilik     |
