---
judul      : Validasi, Analisis, dan Penyempurnaan Dokumen Feasibility Study
target_file: docs/sdlc/01_planning/02_feasibility_study.md
fase_sdlc  : 01 — Planning
prioritas  : Tinggi
status     : Resolved
dibuat_oleh: Senior Business Analyst & Feasibility Consultant
tanggal    : 2026-05-21
---

# Validasi, Analisis, dan Penyempurnaan Dokumen Feasibility Study

## Deskripsi Singkat

Issue ini berisi instruksi low-level yang harus diikuti **langkah demi langkah** untuk memeriksa, menganalisis, memvalidasi, dan menyempurnakan dokumen **Feasibility Study** (`docs/sdlc/01_planning/02_feasibility_study.md`) agar memenuhi standar kualitas industri dan siap dijadikan acuan utama pengambilan keputusan GO/NO-GO serta input dokumen fase SDLC berikutnya.

---

## Persona yang Harus Diambil

Sebelum memulai pekerjaan apa pun, ambillah dan terapkan persona berikut secara penuh dan konsisten sepanjang seluruh proses validasi:

> **Kamu adalah seorang Senior Business Analyst & Feasibility Consultant** dengan pengalaman lebih dari 15 tahun dalam menyusun, mengaudit, dan mengesahkan dokumen studi kelayakan (feasibility study) proyek perangkat lunak — mulai dari skala UMKM hingga enterprise multinasional. Kamu menguasai secara mendalam lima dimensi kelayakan standar industri (teknis, operasional, ekonomi/finansial, jadwal, serta hukum & organisasional), metodologi SDLC Hybrid (Waterfall-Agile), analisis biaya-manfaat (Cost-Benefit Analysis), analisis risiko multi-dimensi, dan standar dokumentasi PMBoK / BABOK / IEEE 1012. Kamu memiliki pemahaman domain bisnis retail, percetakan kustom, UMKM Indonesia, dan sistem informasi manajemen. Kamu sangat teliti, tidak mentoleransi ambiguitas, tidak mentoleransi data kosong yang bisa diisi, dan selalu memastikan setiap dokumen yang kamu hasilkan dapat dipahami serta dieksekusi oleh junior programmer maupun AI model lain yang lebih kecil tanpa pertanyaan klarifikasi yang menghambat pekerjaan.

---

## Lokasi File yang Terlibat

| Peran | Path |
|---|---|
| **Target File (dokumen utama)** | `docs/sdlc/01_planning/02_feasibility_study.md` |
| **Referensi Primer 1** | `docs/sdlc/01_planning/01_project_charter.md` |
| **Referensi Primer 2** | `docs/sdlc/narasi.txt` |
| **Referensi Issue Pembuatan** | `docs/issue/0003_issue_feasibility_study.md` |
| **Direktori Referensi SDLC** | `docs/sdlc/` |

---

## Tahapan Implementasi (Checklist)

Ikuti setiap langkah secara **berurutan dari atas ke bawah**. Jangan melompati langkah. Tandai `[x]` pada setiap item setelah selesai dikerjakan sepenuhnya. Jangan menandai `[x]` jika langkah belum benar-benar selesai dikerjakan.

---

### TAHAP 0 — Persiapan & Pembacaan File

**Tujuan**: Memastikan kamu memiliki pemahaman menyeluruh terhadap semua file yang terlibat sebelum melakukan analisis apa pun.

- [ ] **0.1** Baca seluruh isi file `docs/sdlc/01_planning/02_feasibility_study.md` dari baris pertama hingga baris terakhir tanpa melewati satu baris pun. Catat:
  - [ ] 0.1.a — Versi dokumen saat ini (field `versi` pada frontmatter).
  - [ ] 0.1.b — Status dokumen saat ini (field `status` pada frontmatter).
  - [ ] 0.1.c — Semua file yang direferensikan di dalam isi dokumen (format `[ref: nama_file.md]`).
  - [ ] 0.1.d — Semua seksi dan subseksi yang ada (catat nomor dan judulnya).
- [ ] **0.2** Baca seluruh isi file `docs/sdlc/01_planning/01_project_charter.md` dari baris pertama hingga baris terakhir tanpa melewati satu baris pun. Dokumen ini adalah **referensi primer utama** bagi Feasibility Study.
- [ ] **0.3** Baca seluruh isi file `docs/sdlc/narasi.txt` dari baris pertama hingga baris terakhir tanpa melewati satu baris pun. Dokumen ini adalah **narasi asli pemilik usaha** yang menjadi sumber data konteks operasional bisnis.
- [ ] **0.4** Baca seluruh isi file `docs/issue/0003_issue_feasibility_study.md` dari baris pertama hingga baris terakhir. Dokumen ini berisi instruksi pembuatan awal Feasibility Study dan dapat menjadi acuan untuk memahami cakupan yang seharusnya ada.
- [ ] **0.5** Scan seluruh direktori `docs/sdlc/` untuk memastikan tidak ada file referensi tambahan yang relevan dan belum tercantum di dalam dokumen utama maupun dalam tabel Referensi Dokumen (Seksi 13).
- [ ] **0.6** Catat semua temuan awal (GAP, data kosong, potensi masalah) dalam catatan kerja internal sebelum melanjutkan ke Tahap berikutnya. Jangan langsung menulis ke file target dulu.

---

### TAHAP 1 — Validasi Kelengkapan Data dari File Referensi

**Tujuan**: Memastikan semua data dan informasi penting dari file referensi (`01_project_charter.md` dan `narasi.txt`) yang relevan untuk dokumen Feasibility Study sudah tercermin secara memadai di dalam dokumen utama.

#### 1A — Komparasi dengan `01_project_charter.md`

- [ ] **1A.1** Bandingkan konten Seksi **4 (Analisis Kelayakan Teknis)** pada dokumen utama dengan data teknis di `01_project_charter.md`. Verifikasi bahwa data berikut sudah terwakili:
  - [ ] 1A.1.a — Stack teknologi lengkap (Python versi, MySQL, semua library: `mysql-connector-python`, `python-dotenv`, `bcrypt`, `pyjwt`) [ref: 01_project_charter.md, Seksi 4.1.2].
  - [ ] 1A.1.b — Paradigma Functional Programming murni dan implikasinya terhadap kompleksitas pengembangan [ref: 01_project_charter.md, Seksi 8.2 N-2.4, Seksi 10 Risiko #4].
  - [ ] 1A.1.c — Seluruh 9 modul fungsional (M.1 s.d. M.9) dan tingkat kelayakan teknisnya [ref: 01_project_charter.md, Seksi 4.1.1].
  - [ ] 1A.1.d — Kebutuhan non-fungsional (N-2.1 s.d. N-2.6): RBAC, Audit Trail, bcrypt/JWT, FP, portabilitas OS, CLI [ref: 01_project_charter.md, Seksi 8.2].
  - [ ] 1A.1.e — Spesifikasi infrastruktur: Mini PC Server (Core i5/16GB RAM/SSD 512GB), PC Kasir, 2 UPS, LAN Cat6 [ref: 01_project_charter.md, Seksi 12].
  - [ ] 1A.1.f — Susunan tim pengembang AI (6 model AI spesialis, peran masing-masing) [ref: 01_project_charter.md, Seksi 7.1].
- [ ] **1A.2** Bandingkan konten Seksi **5 (Analisis Kelayakan Operasional)** dengan data operasional di `01_project_charter.md`. Verifikasi bahwa data berikut sudah terwakili:
  - [ ] 1A.2.a — 7 posisi staf operasional yang direncanakan dan deskripsi tugasnya [ref: 01_project_charter.md, Seksi 7.2].
  - [ ] 1A.2.b — Program pelatihan 3 hari dan skenario simulasi operasional [ref: 01_project_charter.md, Seksi 9.4 #3].
  - [ ] 1A.2.c — Rencana dukungan pasca Go-Live oleh tim AI [ref: 01_project_charter.md, Seksi 7.1].
  - [ ] 1A.2.d — Risiko resistensi staf terhadap antarmuka CLI [ref: 01_project_charter.md, Seksi 10 Risiko #6].
- [ ] **1A.3** Bandingkan konten Seksi **6 (Analisis Kelayakan Ekonomi)** dengan data finansial di `01_project_charter.md`. Verifikasi bahwa data berikut sudah terwakili:
  - [ ] 1A.3.a — Rincian 5 komponen CAPEX dengan nominal masing-masing (total Rp 40.000.000) [ref: 01_project_charter.md, Seksi 12].
  - [ ] 1A.3.b — Sumber pendanaan: laba operasional, pinjaman Bank BRI & Mandiri, pinjaman tanpa bunga kerabat [ref: 01_project_charter.md, Seksi 9.2 #5].
  - [ ] 1A.3.c — Risiko penarikan pinjaman tanpa bunga mendadak [ref: 01_project_charter.md, Seksi 10 Risiko #3].
- [ ] **1A.4** Bandingkan konten Seksi **7 (Analisis Kelayakan Jadwal)** dengan timeline di `01_project_charter.md`. Verifikasi bahwa data berikut sudah terwakili:
  - [ ] 1A.4.a — Seluruh 8 milestone (M.1 s.d. M.8) dengan bulan pelaksanaan yang benar [ref: 01_project_charter.md, Seksi 11].
  - [ ] 1A.4.b — Metodologi SDLC Hybrid (Waterfall-Agile) [ref: 01_project_charter.md, Seksi 9.4].
  - [ ] 1A.4.c — Faktor risiko keterlambatan: burnout pemilik dan kerumitan FP [ref: 01_project_charter.md, Seksi 10 Risiko #1, #4].
- [ ] **1A.5** Bandingkan konten Seksi **8 (Analisis Kelayakan Hukum & Organisasional)** dengan data legal di `01_project_charter.md`. Verifikasi bahwa data berikut sudah terwakili:
  - [ ] 1A.5.a — Lisensi semua software open-source (PSF, GPL, MIT/Apache) [ref: 01_project_charter.md, Seksi 12 #2].
  - [ ] 1A.5.b — Fitur keamanan data: bcrypt, JWT, RBAC, Audit Trail, enkripsi backup [ref: 01_project_charter.md, Seksi 8.2 N-2.1, N-2.2, N-2.3, 8.3 N-3.1].
  - [ ] 1A.5.c — Kewajiban NIB pada sistem OSS [ref konteks: kepatuhan legalitas UMKM Indonesia].
  - [ ] 1A.5.d — Risiko budaya cross-functional terhadap pertanggungjawaban kas kasir [ref: 01_project_charter.md, Seksi 10 Risiko #5].

#### 1B — Komparasi dengan `narasi.txt`

- [ ] **1B.1** Baca ulang `narasi.txt` baris per baris. Verifikasi bahwa data konteks berikut dari narasi sudah terintegrasi secara memadai di dalam dokumen Feasibility Study:
  - [ ] 1B.1.a — Kondisi single-fighter pemilik dan dampak burnout (baris 28, 47, 49-70, 74).
  - [ ] 1B.1.b — Lima divisi usaha dan jenis layanan yang ditawarkan (baris 3-18).
  - [ ] 1B.1.c — Kondisi keuangan: dua jenis pinjaman, tekanan setoran bank bulanan (baris 22-24, 66).
  - [ ] 1B.1.d — Kondisi operasional manual Excel yang berserakan (baris 47, 70).
  - [ ] 1B.1.e — Fitur-fitur khusus yang diminta: HPP BOM dimensi desimal (baris 95-96), penggajian otomatis berbasis laba (baris 77-82), rekonsiliasi kas (baris 83), limbah produksi (baris 87), privasi data (baris 89).
  - [ ] 1B.1.f — Konteks pentingnya sistem antrian untuk mencegah pesanan terlewat (baris 28, 74).
  - [ ] 1B.1.g — Kebutuhan PPOB dan jasa keuangan agen bank (baris 3-18).
- [ ] **1B.2** Untuk setiap data `narasi.txt` yang ditemukan **belum** tercermin di dokumen utama dan **relevan** untuk level Feasibility Study, tandai sebagai **[GAP-NARASI]** dan catat data pengisinya.

#### 1C — Komparasi dengan `0003_issue_feasibility_study.md`

- [ ] **1C.1** Periksa apakah seluruh bagian/seksi yang dimandatkan oleh `0003_issue_feasibility_study.md` sudah ada di dalam dokumen utama. Jika ada seksi yang dimandatkan namun tidak ada, tandai sebagai **[GAP-ISSUE]**.
- [ ] **1C.2** Pastikan tabel **Matriks Perbandingan Alternatif Solusi** (Seksi 9) sudah mencakup semua alternatif dan kriteria evaluasi yang dimandatkan oleh instruksi issue pembuatan.

---

### TAHAP 2 — Validasi Relevansi & Fokus Dokumen

**Tujuan**: Memastikan dokumen Feasibility Study **hanya** memuat informasi yang memang seharusnya ada di dokumen ini — tidak lebih, tidak kurang. Dokumen ini bukan SRS, bukan SDD, dan bukan Project Charter.

- [ ] **2.1** Periksa seluruh isi dokumen. Identifikasi apakah ada konten yang **terlalu detail** untuk level Feasibility Study dan seharusnya menjadi bagian dokumen fase berikutnya (SRS atau SDD). Contoh konten yang tidak seharusnya ada di Feasibility Study:
  - Skema tabel database atau ERD.
  - Pseudocode atau potongan kode program.
  - Spesifikasi endpoint API atau antarmuka pengguna secara detail.
  - Spesifikasi use case individual secara rinci.
  Jika ditemukan, tandai sebagai **[OUT-OF-SCOPE-FS]**.
- [ ] **2.2** Periksa apakah ada konten yang **sudah ada di Project Charter** dan hanya diulang secara verbatim (copy-paste) di dokumen Feasibility Study tanpa adanya analisis atau evaluasi kelayakan yang ditambahkan. Konten seperti ini tidak menambah nilai ke Feasibility Study dan sebaiknya dirangkum saja dengan referensi ke sumbernya.
- [ ] **2.3** Pastikan setiap pernyataan di dokumen Feasibility Study merupakan **hasil analisis dan evaluasi**, bukan sekadar pernyataan deskriptif tanpa penilaian. Contoh yang salah: *"Python memiliki ekosistem yang matang."* — harus dilengkapi dengan: *"Oleh karena itu, risiko teknologi ini tergolong Rendah dan teknologi ini dinyatakan Layak."*
- [ ] **2.4** Periksa apakah ada konten yang **duplikat atau redundan** di antara seksi-seksi dalam dokumen utama itu sendiri. Misalnya: suatu risiko disebutkan di dua tempat berbeda dengan narasi yang sama persis tanpa penambahan informasi baru.
- [ ] **2.5** Pastikan tingkat abstraksi dan kedalaman analisis di setiap seksi **konsisten dan sesuai** dengan standar dokumen Feasibility Study industri: cukup mendalam untuk mendukung keputusan GO/NO-GO, tetapi tidak terlalu detail hingga level implementasi teknis.

---

### TAHAP 3 — Validasi Struktur Dokumen

**Tujuan**: Memastikan struktur dokumen Feasibility Study sesuai dengan standar industri dokumen studi kelayakan yang profesional dan lengkap.

- [ ] **3.1** Verifikasi keberadaan dan kelengkapan seksi-seksi **wajib** berikut di dalam dokumen utama. Jika ada seksi yang tidak ada, tandai sebagai **[MISSING-SECTION]**:
  - [ ] 3.1.a — **Frontmatter / Metadata Dokumen**: nama proyek, versi, tanggal, status, penyusun.
  - [ ] 3.1.b — **Riwayat Perubahan Dokumen (Changelog)**: tabel versi, tanggal, perubahan, pelaksana.
  - [ ] 3.1.c — **Informasi Dokumen**: tujuan, cakupan, dan audiens dokumen ini.
  - [ ] 3.1.d — **Ringkasan Eksekutif (Executive Summary)**: latar belakang singkat, tujuan studi, dan **kesimpulan & rekomendasi akhir (GO/NO-GO)** yang langsung tertulis di awal dokumen.
  - [ ] 3.1.e — **Deskripsi Proyek yang Dievaluasi**: nama proyek, tujuan bisnis, ruang lingkup yang dievaluasi, stakeholder utama.
  - [ ] 3.1.f — **Analisis Kelayakan Teknis**: evaluasi teknologi, kompleksitas fitur, kapabilitas tim, infrastruktur, risiko teknis beserta mitigasinya, dan **kesimpulan kelayakan teknis**.
  - [ ] 3.1.g — **Analisis Kelayakan Operasional**: kesiapan SDM, dampak perubahan proses bisnis, penerimaan pengguna, kebutuhan pelatihan, dukungan pasca Go-Live, risiko operasional beserta mitigasinya, dan **kesimpulan kelayakan operasional**.
  - [ ] 3.1.h — **Analisis Kelayakan Ekonomi / Finansial**: estimasi CAPEX, OPEX, manfaat finansial (tangible), manfaat non-finansial (intangible), analisis biaya-manfaat (CBA), ROI, Payback Period, analisis sensitivitas (minimal 3 skenario), sumber pendanaan, risiko finansial beserta mitigasinya, dan **kesimpulan kelayakan ekonomi**.
  - [ ] 3.1.i — **Analisis Kelayakan Jadwal**: timeline yang direncanakan, evaluasi kerealistisan jadwal per fase, identifikasi jalur kritis (critical path), faktor penghambat jadwal, risiko jadwal beserta mitigasinya, dan **kesimpulan kelayakan jadwal**.
  - [ ] 3.1.j — **Analisis Kelayakan Hukum & Organisasional**: kepatuhan regulasi perizinan, kepatuhan UU PDP, lisensi perangkat lunak, aspek ketenagakerjaan, struktur organisasi, risiko hukum/organisasional beserta mitigasinya, dan **kesimpulan kelayakan hukum & organisasional**.
  - [ ] 3.1.k — **Analisis Alternatif Solusi**: deskripsi minimal 3 alternatif solusi, kelebihan & kekurangan masing-masing, **matriks perbandingan alternatif** dengan skor terbobot, dan **justifikasi pemilihan alternatif terbaik**.
  - [ ] 3.1.l — **Matriks Ringkasan Kelayakan**: tabel ringkasan semua dimensi kelayakan beserta status dan catatan kunci masing-masing.
  - [ ] 3.1.m — **Rekomendasi Akhir & Kesimpulan**: keputusan kelayakan formal (GO/NO-GO/GO WITH CONDITIONS), prasyarat yang harus dipenuhi sebelum melanjutkan, dan langkah-langkah selanjutnya (next steps).
  - [ ] 3.1.n — **Glosarium**: definisi semua istilah teknis, domain percetakan, dan keuangan yang digunakan.
  - [ ] 3.1.o — **Referensi Dokumen**: tabel lengkap semua file yang dijadikan acuan.
- [ ] **3.2** Periksa apakah ada **seksi tambahan** standar industri Feasibility Study yang umum namun belum ada di dokumen ini:
  - [ ] 3.2.a — **Asumsi dan Batasan Analisis**: apakah sudah ada pernyataan eksplisit tentang asumsi yang mendasari estimasi finansial dan jadwal? Jika belum ada sebagai seksi tersendiri atau sub-seksi yang jelas, ini perlu ditambahkan.
  - [ ] 3.2.b — **Net Present Value (NPV)**: apakah analisis keuangan sudah mempertimbangkan NPV selain ROI dan Payback Period? Untuk UMKM sederhana, NPV bisa disederhanakan atau disebutkan mengapa tidak disertakan.
  - [ ] 3.2.c — **Break-Even Analysis**: apakah sudah ada analisis titik impas (BEP) yang menunjukkan pada volume transaksi berapa sistem mulai memberikan keuntungan operasional?
- [ ] **3.3** Verifikasi bahwa **setiap sub-seksi analisis kelayakan** (Teknis, Operasional, Ekonomi, Jadwal, Hukum) diakhiri dengan blok **Kesimpulan Kelayakan** yang berisi:
  - Status kelayakan (Layak / Layak dengan Catatan / Tidak Layak) yang ditulis secara eksplisit dan jelas.
  - Catatan kunci yang menjadi syarat kelayakan.
- [ ] **3.4** Verifikasi bahwa **setiap tabel risiko** di setiap dimensi kelayakan memiliki kolom: Nomor, Risiko, Probabilitas (skala 1-5), Dampak (skala 1-5), dan Rencana Mitigasi yang konkret.
- [ ] **3.5** Verifikasi bahwa setiap seksi memiliki judul yang jelas, hierarki heading yang konsisten (H1 > H2 > H3 > H4), dan penomoran urut yang benar dan tidak ada yang loncat.
- [ ] **3.6** Verifikasi bahwa tabel, daftar berpoin, dan format markdown digunakan secara konsisten di seluruh dokumen dan dapat dirender dengan benar.

---

### TAHAP 4 — Validasi Kesiapan sebagai Acuan Fase SDLC Berikutnya

**Tujuan**: Memastikan dokumen Feasibility Study ini cukup kuat, lengkap, dan tidak ambigu sebagai **input utama** bagi dokumen SRS (Software Requirements Specification) di fase Requirements (Fase 2) dan dokumen SDLC fase-fase berikutnya.

- [ ] **4.1** Periksa apakah **Kesimpulan Kelayakan Akhir (GO/NO-GO/GO WITH CONDITIONS)** sudah dinyatakan secara tegas, jelas, dan tidak ambigu di dokumen utama. Keputusan ini harus bisa langsung dibaca dan dipahami oleh penyusun SRS tanpa perlu interpretasi tambahan.
- [ ] **4.2** Periksa apakah **semua 9 modul fungsional (M.1 s.d. M.9)** sudah dianalisis kelayakan teknisnya secara memadai di dokumen ini, sehingga penyusun SRS memiliki pemahaman awal tentang tingkat kesulitan dan risiko teknis masing-masing modul.
- [ ] **4.3** Periksa apakah **prasyarat dan catatan kelayakan** (conditions) yang tercantum di Rekomendasi Akhir sudah cukup spesifik dan dapat dieksekusi oleh pemilik usaha. Prasyarat yang terlalu umum (misalnya: "pemilik harus memenuhi kewajiban hukum") harus diperinci menjadi langkah aksi yang konkret.
- [ ] **4.4** Periksa apakah **risiko-risiko kritis** yang teridentifikasi di setiap dimensi kelayakan sudah dibubuhi rencana mitigasi yang cukup konkret untuk menjadi panduan bagi fase perencanaan risiko di dokumen SRS dan SDD berikutnya.
- [ ] **4.5** Periksa apakah **Analisis Alternatif Solusi (Seksi 9)** sudah cukup komprehensif dan justifikasi pemilihan solusinya sudah cukup kuat, sehingga penyusun SRS tidak perlu kembali mempertanyakan mengapa solusi CLI Python + MySQL dipilih.
- [ ] **4.6** Periksa apakah **Matriks Ringkasan Kelayakan (Seksi 10)** sudah merepresentasikan secara akurat keputusan akhir dari seluruh analisis dimensi kelayakan di dokumen ini.
- [ ] **4.7** Periksa apakah **Langkah Selanjutnya (Next Steps)** di Rekomendasi Akhir sudah cukup spesifik dan actionable (dapat langsung dilaksanakan), bukan hanya pernyataan abstrak seperti "lanjutkan ke fase berikutnya".
- [ ] **4.8** Periksa apakah data-data estimasi finansial (CAPEX, OPEX, manfaat, ROI, Payback Period) di Seksi 6 sudah cukup memadai sebagai baseline anggaran awal yang dapat dirujuk oleh pemilik usaha saat merencanakan arus kas pengembangan.

---

### TAHAP 5 — Validasi Bahasa & Keterbacaan

**Tujuan**: Memastikan dokumen menggunakan Bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau AI model lain yang lebih kecil/murah.

- [ ] **5.1** Baca ulang seluruh dokumen dari baris pertama hingga baris terakhir dengan perspektif sebagai **pembaca baru** yang belum mengenal proyek AbuCom sama sekali. Simulasikan bahwa kamu adalah junior programmer atau AI model murah yang hanya menerima dokumen ini tanpa konteks lain.
- [ ] **5.2** Periksa apakah ada **kalimat yang ambigu, bermakna ganda, atau dapat disalahartikan**. Contoh: kalimat pasif yang tidak jelas subjeknya, atau kalimat bersyarat yang kondisinya tidak eksplisit. Tandai dan perbaiki.
- [ ] **5.3** Periksa apakah ada **istilah teknis** (bahasa Inggris atau jargon domain percetakan/keuangan/IT) yang digunakan dalam isi dokumen **tanpa penjelasan** dan istilah tersebut **tidak ada** di bagian Glosarium. Jika ada, tambahkan definisinya ke Glosarium.
- [ ] **5.4** Periksa apakah ada **akronim atau singkatan** yang muncul untuk pertama kalinya dalam dokumen tanpa disertai kepanjangan atau penjelasannya. Contoh: RBAC, JWT, BOM, HPP, PPOB, UU PDP, NIB, OSS, PKWT, PKWTT. Perbaiki dengan menyertakan kepanjangan pada kemunculan pertama.
- [ ] **5.5** Pastikan semua kalimat menggunakan **kalimat aktif yang ringkas**. Kalimat pasif panjang yang bertele-tele harus dipecah atau diubah menjadi kalimat aktif yang lebih langsung.
- [ ] **5.6** Periksa **konsistensi penulisan nama** berikut di seluruh dokumen:
  - Nama proyek: harus selalu **"AbuCom"** (bukan "Abucom", "ABUCOM", atau "abucom").
  - Nama dokumen: harus menggunakan nama file yang benar.
  - Nama teknologi: Python, MySQL (bukan python, mysql).
  - Nama paradigma: *Functional Programming* (FP) — konsisten menggunakan huruf kapital dan cetak miring.
- [ ] **5.7** Periksa apakah setiap **label estimasi** (ESTIMASI, perlu validasi, belum dikonfirmasi) sudah ditulis secara konsisten dan jelas agar pembaca tahu mana data yang sudah pasti dan mana yang masih estimasi.
- [ ] **5.8** Khusus untuk **tabel-tabel data** (tabel risiko, tabel CBA, tabel matriks alternatif): periksa apakah konten sel tabel sudah cukup ringkas dan tidak ada sel yang terlalu panjang sehingga tabel sulit dibaca di layar terminal teks.

---

### TAHAP 6 — Validasi Kualitas & Pengisian Data yang Kosong

**Tujuan**: Memastikan tidak ada data yang kosong, placeholder yang belum diisi, atau field yang memerlukan pengisian manual namun sudah dapat diisi berdasarkan konteks yang tersedia.

- [ ] **6.1** Cari semua teks yang mengandung pola placeholder berikut di seluruh isi dokumen:
  - `[BELUM DITENTUKAN]`
  - `[ISI MANUAL]`
  - `**[BELUM DITENTUKAN — ISI MANUAL]**`
  - `TBD`, `TODO`, `N/A` tanpa keterangan.
  - `*(Diisi oleh...)*` tanpa data aktual.
  - Sel tabel yang kosong atau hanya berisi `-` tanpa alasan.
- [ ] **6.2** Untuk setiap placeholder yang ditemukan, evaluasi apakah datanya **bisa diisi** berdasarkan informasi yang sudah tersedia di `narasi.txt`, `01_project_charter.md`, atau konteks proyek yang ada. Jika bisa diisi, **isi dengan data yang relevan, realistis, dan konsisten** dengan konteks UMKM percetakan di Indonesia.
- [ ] **6.3** Khusus untuk placeholder **`[BELUM DITENTUKAN — ISI MANUAL]` pada Seksi 8.4 (Aspek Ketenagakerjaan — UMR setempat)**:
  - [ ] 6.3.a — Periksa apakah terdapat petunjuk lokasi usaha di `narasi.txt` (kota/kabupaten tempat AbuCom beroperasi). Jika ada, isi dengan referensi UMR daerah tersebut yang realistis sesuai konteks.
  - [ ] 6.3.b — Jika lokasi spesifik **tidak tersedia** di narasi, ganti placeholder dengan keterangan yang lebih informatif dan actionable, contoh: `*(UMR daerah operasional usaha — diisi oleh Pemilik Usaha berdasarkan Peraturan Gubernur/Bupati/Walikota setempat yang berlaku)*`.
- [ ] **6.4** Khusus untuk **Seksi 6.2 (Estimasi OPEX)** yang diberi label `*[ESTIMASI — belum dikonfirmasi pemilik]*`: Verifikasi bahwa angka-angka estimasi OPEX sudah realistis untuk konteks UMKM dengan server lokal (listrik, perawatan hardware, token API AI). Jika perlu, sesuaikan estimasi dengan data konteks yang ada.
- [ ] **6.5** Khusus untuk **Seksi 6.3 (Estimasi Manfaat Finansial)** yang diberi label `*[ESTIMASI — perlu validasi data riil dari pemilik]*`: Verifikasi bahwa asumsi estimasi manfaat (penghematan waktu, efisiensi limbah, penyelamatan transaksi terlewat) sudah didukung data kontekstual dari `narasi.txt` dan bukan hanya angka yang dikarang tanpa dasar.
- [ ] **6.6** Periksa apakah ada **sel tabel yang tidak konsisten atau logikanya keliru** di tabel-tabel berikut:
  - Tabel CBA (Seksi 6.5): pastikan kolom Total Biaya, Manfaat Finansial, dan Arus Kas Bersih matematis konsisten satu sama lain.
  - Tabel Payback Period (Seksi 6.7): pastikan formula dan angka hasilnya konsisten dengan data di Seksi 6.3 dan 6.2.
  - Tabel Matriks Perbandingan Alternatif (Seksi 9.4): pastikan Total Skor dihitung dengan benar dari penjumlahan skor per kriteria.
- [ ] **6.7** Periksa apakah ada **referensi internal** dalam isi dokumen (format `[ref: nama_file.md, Seksi X]`) yang **mengarah ke nomor seksi atau sub-seksi yang tidak ada** atau sudah berubah nomornya. Perbaiki referensi yang salah.
- [ ] **6.8** Periksa apakah ada **fakta atau pernyataan** di dalam dokumen yang **bertentangan** satu sama lain (inkonsistensi internal). Contoh: angka CAPEX di Seksi 6.1 berbeda dengan yang disebutkan di Seksi 2 atau Seksi 11.

---

### TAHAP 7 — Validasi Standar Spesifik Dokumen Feasibility Study

**Tujuan**: Memastikan aspek-aspek penting khas dokumen Feasibility Study yang sering terlewat sudah terpenuhi sesuai praktik industri.

- [ ] **7.1** **Konsistensi Keputusan GO/NO-GO**: Verifikasi bahwa keputusan akhir (GO/NO-GO/GO WITH CONDITIONS) yang tertulis di **Ringkasan Eksekutif (Seksi 2.3)** konsisten dengan kesimpulan yang tertulis di **Rekomendasi Akhir (Seksi 11.1)** dan konsisten dengan status kelayakan masing-masing dimensi di **Matriks Ringkasan Kelayakan (Seksi 10)**. Jika ada inkonsistensi, selaraskan ketiganya.
- [ ] **7.2** **Kelengkapan Tabel Risiko per Dimensi**: Verifikasi bahwa setiap dimensi kelayakan (Teknis, Operasional, Ekonomi, Jadwal, Hukum) memiliki tabel risiko dengan **minimal 2 risiko yang berbeda** dan spesifik untuk dimensi tersebut. Risiko yang disebutkan di dimensi Teknis tidak boleh sama persis dengan risiko di dimensi Operasional.
- [ ] **7.3** **Konsistensi Probabilitas & Dampak Risiko**: Untuk setiap risiko dalam tabel, verifikasi bahwa nilai Probabilitas (1-5) dan Dampak (1-5) yang diberikan **masuk akal** dan konsisten dengan narasi deskripsi risikonya. Risiko dengan dampak tinggi (4-5) harus memiliki mitigasi yang lebih kuat dari risiko dengan dampak rendah (1-2).
- [ ] **7.4** **Kualitas Mitigasi Risiko**: Periksa apakah setiap rencana mitigasi risiko bersifat **konkret dan dapat dieksekusi** (actionable). Mitigasi yang terlalu umum seperti "lakukan pemantauan rutin" atau "konsultasikan dengan ahli" tanpa detail lebih lanjut harus diperinci menjadi langkah aksi yang spesifik.
- [ ] **7.5** **Validitas Asumsi Estimasi Finansial**: Periksa apakah asumsi-asumsi di balik estimasi ROI (26%) dan Payback Period (9,5 bulan) sudah dinyatakan secara eksplisit di dalam dokumen. Asumsi yang tidak dinyatakan secara eksplisit membuat estimasi menjadi tidak dapat divalidasi. Tambahkan daftar asumsi jika belum ada.
- [ ] **7.6** **Kelayakan Analisis Sensitivitas**: Verifikasi bahwa ketiga skenario (Best, Base, Worst) di Seksi 6.8 menggunakan asumsi yang **berbeda secara bermakna** dan hasilnya masuk akal secara matematis. Payback Period di skenario Worst Case harus lebih lama dari Base Case, dan Base Case harus lebih lama dari Best Case.
- [ ] **7.7** **Konteks Lokal Indonesia**: Verifikasi bahwa dokumen sudah mempertimbangkan konteks spesifik UMKM Indonesia, antara lain:
  - [ ] 7.7.a — UU PDP No. 27 Tahun 2022 disebutkan dan dianalisis kepatuhannya.
  - [ ] 7.7.b — Sistem OSS (NIB) untuk legalitas usaha disebutkan.
  - [ ] 7.7.c — Regulasi ketenagakerjaan Indonesia (UU Cipta Kerja, PKWT/PKWTT) disebutkan.
  - [ ] 7.7.d — Nama bank lokal (BRI, Mandiri) sudah benar dan konsisten dengan `narasi.txt`.
- [ ] **7.8** **Kelengkapan Glosarium**: Verifikasi bahwa semua istilah berikut sudah ada di Glosarium beserta definisinya. Jika ada yang belum ada, tambahkan:
  - [ ] 7.8.a — Istilah domain percetakan: Stempel Flash, Baliho, Nama Dada, Buku Yasin, Map Snelhechter.
  - [ ] 7.8.b — Istilah domain keuangan: CAPEX, OPEX, ROI, Payback Period, Cost-Benefit Analysis, Analisis Sensitivitas.
  - [ ] 7.8.c — Istilah IT/sistem: BOM, HPP, PPOB, Audit Trail, RBAC, CLI, Functional Programming, JWT, UU PDP, Stock Opname, Kasbon, Retur, Uang Muka/DP.
  - [ ] 7.8.d — Istilah legal: NIB, OSS, PKWT, PKWTT — **jika** istilah ini disebutkan dalam isi dokumen. Jika belum ada di Glosarium, tambahkan.
- [ ] **7.9** **Kelengkapan Referensi Dokumen (Seksi 13)**: Verifikasi bahwa **semua file yang direferensikan** menggunakan format `[ref: nama_file]` di dalam isi dokumen sudah tercantum di tabel Referensi Dokumen pada Seksi 13. Tidak boleh ada file yang direferensikan di isi dokumen tetapi tidak ada di tabel referensi.
- [ ] **7.10** **Validasi Payback Period — Konsistensi Formula**: Verifikasi bahwa formula Payback Period di Seksi 6.7 menggunakan angka **Net Benefit Bulanan** yang konsisten dengan data di Seksi 6.3 (Manfaat Finansial) dikurangi data di Seksi 6.2 (OPEX Bulanan). Contoh: jika Manfaat Tangible Rp 4.700.000/bulan dan OPEX Rp 500.000/bulan, maka Net Benefit Bulanan = Rp 4.200.000/bulan, dan Payback Period = Rp 40.000.000 / Rp 4.200.000 = ~9,5 bulan. Jika ada ketidakkonsistenan angka, koreksi.

---

### TAHAP 8 — Penulisan Ulang Dokumen Final (Overwrite)

**Tujuan**: Menuangkan seluruh hasil validasi, koreksi, dan penyempurnaan ke file target secara lengkap dan utuh.

> ⚠️ **PERINGATAN KRITIS — BACA SEBELUM EKSEKUSI:**
> Langkah ini akan **menimpa (overwrite) seluruh isi** file `docs/sdlc/01_planning/02_feasibility_study.md`. Pastikan **semua tahap validasi (Tahap 1 s.d. 7) sudah selesai sepenuhnya** sebelum menjalankan langkah ini. Jangan menulis ke file target sebelum seluruh analisis selesai.

- [ ] **8.1** Susun dokumen final yang telah disempurnakan secara lengkap di dalam memori atau buffer kerja kamu terlebih dahulu. Dokumen final ini adalah gabungan dari dokumen asli yang sudah diperbaiki berdasarkan seluruh temuan di Tahap 1 s.d. 7.
- [ ] **8.2** Sebelum menulis, lakukan **verifikasi kelengkapan checklist internal** berikut terhadap dokumen final yang sudah kamu susun:
  - [ ] 8.2.a — Semua **[GAP]** yang ditemukan di Tahap 1 sudah diisi dengan konten yang sesuai.
  - [ ] 8.2.b — Semua konten **[OUT-OF-SCOPE-FS]** yang ditemukan di Tahap 2 sudah dihapus atau dipindahkan.
  - [ ] 8.2.c — Semua **[MISSING-SECTION]** yang ditemukan di Tahap 3 sudah ditambahkan.
  - [ ] 8.2.d — Semua **placeholder kosong** yang bisa diisi (ditemukan di Tahap 6) sudah terisi dengan data yang relevan.
  - [ ] 8.2.e — Semua **inkonsistensi data** (ditemukan di Tahap 6 dan 7) sudah diselaraskan.
  - [ ] 8.2.f — Semua **perbaikan bahasa** (ditemukan di Tahap 5) sudah diterapkan.
- [ ] **8.3** Pastikan perubahan versi dokumen diterapkan di **tiga lokasi** berikut dalam dokumen final:
  - [ ] 8.3.a — Field `versi` pada **frontmatter YAML**: ubah dari `1.0` menjadi `1.1` (atau lebih tinggi jika diperlukan).
  - [ ] 8.3.b — Field `tanggal` pada **frontmatter YAML**: perbarui ke tanggal hari ini (format `YYYY-MM-DD`).
  - [ ] 8.3.c — Tabel **Riwayat Perubahan Dokumen**: tambahkan baris baru yang mencatat: versi baru (`1.1`), tanggal hari ini, ringkasan singkat perubahan yang dilakukan, dan nama persona pelaksana issue ini (sesuai persona di awal dokumen issue ini).
- [ ] **8.4** Pastikan dokumen final yang sudah disusun memuat **semua seksi dari dokumen asli tanpa ada yang dihilangkan atau diringkas**. Tidak boleh ada seksi yang dipotong, diringkas menjadi `[...]`, atau dihapus kecuali terbukti tidak relevan berdasarkan temuan Tahap 2.
- [ ] **8.5** **TULIS** seluruh isi dokumen final ke file `docs/sdlc/01_planning/02_feasibility_study.md` dengan cara **overwrite penuh** — timpa dari baris pertama (frontmatter `---`) hingga baris terakhir dokumen. Seluruh teks harus ditulis ulang sepenuhnya. **Tidak boleh ada bagian yang dipotong, diringkas, atau digantikan dengan `[...]` atau `(lanjutan...)`**.
- [ ] **8.6** Setelah penulisan selesai, **baca kembali** file yang baru saja ditulis dari baris pertama hingga baris terakhir untuk verifikasi. Pastikan:
  - [ ] 8.6.a — Versi dokumen sudah berubah menjadi `v1.1` (atau lebih tinggi).
  - [ ] 8.6.b — Tabel Riwayat Perubahan sudah diperbarui dengan baris baru.
  - [ ] 8.6.c — Semua placeholder yang bisa diisi sudah terisi dengan data aktual.
  - [ ] 8.6.d — Tidak ada konten yang terpotong atau hilang di bagian tengah maupun akhir file.
  - [ ] 8.6.e — Format markdown dapat dirender dengan benar: heading konsisten, tabel rapi, list berpoin terstruktur, tebal (`**`), miring (`*`), dan kode (`` ` ``) digunakan secara konsisten.
  - [ ] 8.6.f — Total jumlah baris/karakter file baru **sama dengan atau lebih banyak** dari file asli (karena proses ini bersifat penyempurnaan, bukan pemangkasan).

---

### TAHAP 9 — Pembaruan Referensi Dokumen

**Tujuan**: Memastikan semua file yang digunakan sebagai referensi dalam proses validasi ini tercatat lengkap di bagian Referensi Dokumen.

- [ ] **9.1** Periksa bagian **Referensi Dokumen (Seksi 13)** pada dokumen yang baru saja ditulis.
- [ ] **9.2** Bandingkan daftar file di tabel Referensi Dokumen dengan semua file yang kamu gunakan selama proses validasi ini (Tahap 0 s.d. 8). Jika ada file yang kamu gunakan sebagai referensi tetapi **belum tercantum** di tabel, tambahkan.
- [ ] **9.3** Jika dalam proses perbaikan dokumen kamu menambahkan konten yang bersumber dari file baru (misalnya dari file lain di direktori `docs/sdlc/`), tambahkan file tersebut ke tabel Referensi Dokumen dengan format berikut:
  ```
  | [nomor urut] | `nama_file.ext` | `docs/path/ke/file` | Keterangan singkat isi dan relevansi file ini terhadap Feasibility Study |
  ```
- [ ] **9.4** Pastikan seluruh path referensi menggunakan **path relatif terhadap root proyek** (contoh: `docs/sdlc/narasi.txt`), bukan path absolut sistem operasi.
- [ ] **9.5** Pastikan penambahan referensi baru ini ditulis di **baris paling bawah** tabel Referensi Dokumen, mengikuti urutan nomor yang benar.

---

## Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **selesai** apabila **seluruh** kondisi berikut terpenuhi tanpa pengecualian:

- [ ] Semua checklist dari Tahap 0 hingga Tahap 9 sudah ditandai `[x]`.
- [ ] File `docs/sdlc/01_planning/02_feasibility_study.md` sudah berhasil ditimpa dengan konten yang telah disempurnakan dan dapat dibaca dari awal hingga akhir tanpa ada bagian yang terpotong.
- [ ] Versi dokumen sudah berubah dari `v1.0` menjadi `v1.1` (atau lebih tinggi jika diperlukan) di frontmatter **dan** di tabel Riwayat Perubahan.
- [ ] Tidak ada lagi placeholder `[ISI MANUAL]`, `[BELUM DITENTUKAN]`, `TBD`, atau `TODO` yang secara logis dapat diisi berdasarkan konteks yang tersedia.
- [ ] Tidak ada seksi dokumen yang hilang, terpotong, atau diringkas.
- [ ] Keputusan GO/NO-GO/GO WITH CONDITIONS konsisten di Ringkasan Eksekutif, Matriks Ringkasan Kelayakan, dan Rekomendasi Akhir.
- [ ] Semua tabel risiko memiliki minimal 2 risiko spesifik per dimensi kelayakan beserta mitigasi yang konkret.
- [ ] Semua data estimasi finansial (CAPEX, OPEX, ROI, Payback Period) konsisten satu sama lain secara matematis.
- [ ] Glosarium sudah mencakup semua istilah teknis, domain, dan keuangan yang digunakan di dalam dokumen.
- [ ] Tabel Referensi Dokumen sudah mencantumkan semua file yang digunakan sebagai referensi, termasuk file baru jika ada.
- [ ] Dokumen dapat dibaca dari awal hingga akhir oleh junior programmer atau AI model lain yang lebih kecil tanpa perlu mengajukan pertanyaan klarifikasi yang menghambat pekerjaan fase SDLC berikutnya.

---

## Catatan Penting untuk Pelaksana

1. **Jangan asumsikan data yang tidak ada** — jika informasi yang diperlukan tidak tersedia di `narasi.txt` maupun di `01_project_charter.md`, jangan mengarang angka atau fakta. Gunakan keterangan: `*(Memerlukan konfirmasi dari Pemilik Usaha)*`.
2. **Jangan mengubah keputusan bisnis yang sudah ditetapkan** — kamu boleh memperbaiki bahasa, melengkapi data yang kosong, memperbaiki inkonsistensi, dan menambah seksi yang kurang, tetapi **dilarang mengubah keputusan bisnis dan teknis** yang sudah ditetapkan pemilik: paradigma Functional Programming, stack Python + MySQL, durasi 12 bulan, total anggaran Rp 40.000.000, dan keputusan GO WITH CONDITIONS.
3. **Jangan memotong atau meringkas** — penulisan ulang di Tahap 8 harus menghasilkan dokumen yang **sama panjang atau lebih panjang** dari dokumen asli, karena proses ini adalah penyempurnaan dan pengayaan, bukan pemangkasan.
4. **Gunakan format markdown yang konsisten** — seluruh heading, tabel, list, bold, italic, dan code block harus mengikuti format yang sudah ada di dokumen asli. Jangan mengubah gaya penulisan secara drastis.
5. **Baca semua referensi sebelum menulis** — jangan mulai menyusun dokumen final (Tahap 8) sebelum kamu benar-benar selesai membaca semua file referensi yang tercantum di Tahap 0.
6. **Validasi matematika secara eksplisit** — setiap angka finansial (ROI, Payback Period, Total Skor Matriks) harus divalidasi kalkulasinya secara eksplisit di dalam checklist sebelum ditulis ke dokumen final. Jangan hanya menyalin angka dari dokumen asli tanpa memverifikasinya.
7. **Perhatikan label estimasi** — data yang berlabel `*[ESTIMASI]*` atau `*[ESTIMASI — belum dikonfirmasi pemilik]*` harus tetap diberi label tersebut di dokumen final kecuali datanya sudah dapat diverifikasi dari sumber referensi yang ada.

---

## Referensi Issue Terkait

| Issue ID | Judul | Keterangan |
|---|---|---|
| `0003` | Pembuatan Dokumen Feasibility Study | Issue pembuatan pertama dokumen yang menjadi target validasi issue ini. |
| `0001` | Pembuatan Dokumen Project Charter | Issue pembuatan dokumen Project Charter yang menjadi referensi primer utama Feasibility Study. |
| `0002` | Validasi Dokumen Project Charter | Issue validasi Project Charter — dapat dijadikan contoh pola pelaksanaan issue validasi ini. |
