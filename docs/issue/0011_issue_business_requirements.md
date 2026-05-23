---
judul      : Pembuatan dan Penyusunan Dokumen Business Requirements
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
prioritas  : High
status     : Open
tanggal    : 2026-05-23
target     : docs/sdlc/02_analysis/01_business_requirements.md
assignee   : Junior Programmer / LLM AI Model (Routine Coding & Documentation)
---

# Pembuatan dan Penyusunan Dokumen Business Requirements

## 1. Ringkasan Issue

Issue ini berisi instruksi perencanaan low-level yang sangat detail dan eksplisit untuk pembuatan dokumen **Business Requirements Document (BRD)** proyek AbuCom. Dokumen BRD ini merupakan dokumen pertama pada **Fase 02 Analysis** dalam siklus SDLC AbuCom dan menjadi jembatan antara fase Planning yang sudah selesai dengan fase Requirements (SRS) yang akan dikerjakan berikutnya.

**Tujuan utama issue ini** adalah memastikan siapapun yang mengeksekusi (junior programmer atau LLM AI model yang lebih murah/kecil) dapat mengerjakan pembuatan dokumen BRD ini **tanpa ambiguitas, tanpa halusinasi, dan tanpa interpretasi yang salah** terhadap data dan informasi yang ada pada file referensi.

---

## 2. Persona Pelaksana

### 2.1. Persona yang Ditugaskan
**Senior Business Analyst & Requirements Engineering Specialist**

### 2.2. Alasan Pemilihan Persona
Persona ini dipilih karena alasan berikut:
1. **Otoritas Domain**: Business Analyst adalah persona standar industri yang paling kompeten dan memiliki otoritas penuh dalam menganalisis, mengekstrak, dan mendokumentasikan kebutuhan bisnis dari pemangku kepentingan ke dalam format dokumen formal yang terstruktur.
2. **Keterampilan Kritis**: Persona ini memiliki kemampuan untuk menerjemahkan kebutuhan operasional pemilik usaha (yang bersifat naratif dan informal) menjadi pernyataan kebutuhan bisnis yang terukur, tidak ambigu, dan dapat diverifikasi.
3. **Jembatan Komunikasi**: Business Analyst berperan sebagai jembatan antara bahasa bisnis pemilik usaha dan bahasa teknis tim pengembang, memastikan tidak ada informasi yang hilang atau salah diterjemahkan pada fase SDLC selanjutnya.
4. **Kelengkapan Dokumentasi**: Persona ini terlatih untuk memastikan setiap kebutuhan bisnis didokumentasikan secara lengkap dengan kriteria penerimaan (*acceptance criteria*) yang jelas, sehingga dokumen ini layak menjadi acuan utama bagi SRS, SDD, dan fase pengujian.

---

## 3. File Referensi yang Digunakan

### 3.1. Daftar File Referensi yang Dipilih

Berikut adalah file referensi yang **wajib dibaca secara menyeluruh** sebelum memulai penyusunan dokumen BRD. Setiap file dipilih berdasarkan tingkat relevansi dan kontribusi datanya terhadap kebutuhan spesifik dokumen Business Requirements:

| # | Prioritas | Nama File | Lokasi Path Relatif | Alasan Pemilihan |
|---|-----------|-----------|----------------------|------------------|
| 1 | **Primer** | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Sumber utama definisi ruang lingkup proyek, tujuan SMART, kebutuhan fungsional & non-fungsional tingkat tinggi, modul sistem, stakeholder, dan kriteria keberhasilan. Data di sini adalah fondasi utama BRD. |
| 2 | **Primer** | `02_feasibility_study.md` | `docs/sdlc/01_planning/02_feasibility_study.md` | Sumber validasi kelayakan teknis per modul, analisis kompleksitas fitur, risiko operasional, dan batasan sistem yang mempengaruhi kebutuhan bisnis. |
| 3 | **Primer** | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Sumber profil lengkap stakeholder, kebutuhan & ekspektasi per posisi, pemetaan hak akses RBAC, dan matriks keterlibatan yang menentukan pembagian kebutuhan bisnis per aktor pengguna. |
| 4 | **Sekunder** | `04_tech_stack_decision.md` | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Sumber batasan teknis mandatori (Python FP, MySQL, CLI), strategi keamanan (bcrypt, JWT, RBAC, Audit Trail), dan konfigurasi teknis yang membatasi atau mempengaruhi kebutuhan bisnis. |
| 5 | **Sekunder** | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Sumber daftar 42 inovasi (30 terintegrasi + 12 rekomendasi baru) yang wajib diakomodasi sebagai kebutuhan bisnis, termasuk parameter konfigurasi spesifik (threshold PPOB, limit kasbon, target laba). |
| 6 | **Pendukung** | `narasi.txt` | `docs/sdlc/narasi.txt` | Sumber narasi asli pemilik usaha. **Masih dibutuhkan** sebagai referensi pendukung untuk memvalidasi bahwa tidak ada kebutuhan operasional asli pemilik yang terlewat dari dokumen planning, dan untuk mempertahankan konteks budaya kerja cross-functional serta detail alur kerja manual yang mungkin belum sepenuhnya terekstrak ke dokumen lain. |

### 3.2. Alasan Pemilihan narasi.txt sebagai Referensi Pendukung
File `narasi.txt` tetap digunakan sebagai referensi pendukung (bukan primer) karena:
- Sebagian besar data operasional di `narasi.txt` sudah terekstrak secara formal ke dalam `01_project_charter.md` dan `03_stakeholder_register.md`.
- Namun, `narasi.txt` masih mengandung nuansa konteks budaya kerja (*cross-functional*, gotong-royong antar staf) dan detail operasional mikro (seperti alur kerja manual per divisi) yang perlu divalidasi ulang agar tidak ada kebutuhan bisnis yang hilang.
- Gunakan `narasi.txt` hanya sebagai **cross-check akhir** setelah semua data dari 5 dokumen primer/sekunder sudah dirangkum.

---

## 4. Instruksi Pelaksanaan — Tahapan Detail

### Fase A: Persiapan dan Pembacaan File Referensi

> **PENTING**: Baca setiap file referensi secara **MENYELURUH dari awal hingga akhir**. Jangan melewatkan satu bagian pun. Setiap detail data dan informasi yang ada di dalam file referensi berpotensi menjadi input bagi dokumen BRD.

- [ ] **A.1.** Baca file `docs/sdlc/01_planning/01_project_charter.md` secara menyeluruh dari baris pertama hingga baris terakhir.
- [ ] **A.2.** Baca file `docs/sdlc/01_planning/02_feasibility_study.md` secara menyeluruh dari baris pertama hingga baris terakhir.
- [ ] **A.3.** Baca file `docs/sdlc/01_planning/03_stakeholder_register.md` secara menyeluruh dari baris pertama hingga baris terakhir.
- [ ] **A.4.** Baca file `docs/sdlc/01_planning/04_tech_stack_decision.md` secara menyeluruh dari baris pertama hingga baris terakhir.
- [ ] **A.5.** Baca file `docs/sdlc/01_planning/05_innovation_proposal.md` secara menyeluruh dari baris pertama hingga baris terakhir.
- [ ] **A.6.** Baca file `docs/sdlc/narasi.txt` secara menyeluruh dari baris pertama hingga baris terakhir.

---

### Fase B: Perangkuman Data dan Informasi dari File Referensi

> **PENTING**: Rangkum **semua** data dan informasi yang ada di setiap file referensi. Jangan ada detail yang terlewat. Perangkuman ini bersifat internal (tidak ditulis ke target file), digunakan sebagai bahan mentah untuk menyusun dokumen BRD.

- [ ] **B.1.** Dari `01_project_charter.md`, rangkum dan catat data berikut:
  - [ ] B.1.1. Nama proyek, deskripsi singkat, sponsor, dan manajer proyek
  - [ ] B.1.2. Latar belakang dan justifikasi proyek (kondisi saat ini, permasalahan, dampak)
  - [ ] B.1.3. Tujuan umum dan tujuan spesifik SMART (S.1 sampai S.5)
  - [ ] B.1.4. Manfaat bisnis terukur (4 poin kuantitatif)
  - [ ] B.1.5. Ruang lingkup proyek — seluruh modul fitur utama (M.1 sampai M.9) beserta sub-fiturnya
  - [ ] B.1.6. Platform dan teknologi (batasan teknis)
  - [ ] B.1.7. Hal-hal di luar ruang lingkup (out-of-scope)
  - [ ] B.1.8. Deliverables per fase SDLC
  - [ ] B.1.9. Daftar stakeholder dan RACI Matrix
  - [ ] B.1.10. Susunan tim pengembang dan peran
  - [ ] B.1.11. Kebutuhan fungsional utama per divisi (F-1.x sampai F-6.x)
  - [ ] B.1.12. Kebutuhan non-fungsional utama (N-2.x)
  - [ ] B.1.13. Rekomendasi inovasi dan best practice (N-3.x)
  - [ ] B.1.14. Asumsi, batasan, dan dependensi proyek
  - [ ] B.1.15. Risiko awal dan rencana mitigasi
  - [ ] B.1.16. Milestone dan jadwal tingkat tinggi
  - [ ] B.1.17. Estimasi anggaran tingkat tinggi
  - [ ] B.1.18. Kriteria keberhasilan proyek
  - [ ] B.1.19. Glosarium istilah domain percetakan

- [ ] **B.2.** Dari `02_feasibility_study.md`, rangkum dan catat data berikut:
  - [ ] B.2.1. Evaluasi kelayakan teknis per teknologi dan per modul (M.1 sampai M.9)
  - [ ] B.2.2. Evaluasi kelayakan operasional (kesiapan organisasi, SDM, pelatihan)
  - [ ] B.2.3. Evaluasi kelayakan ekonomi (CAPEX, OPEX, ROI, NPV, Payback Period, BEP)
  - [ ] B.2.4. Evaluasi kelayakan jadwal (timeline 12 bulan, jalur kritis)
  - [ ] B.2.5. Evaluasi kelayakan hukum (UU PDP, NIB, PKWT/PKWTT, lisensi software)
  - [ ] B.2.6. Analisis alternatif solusi dan matriks perbandingan
  - [ ] B.2.7. Risiko teknis, operasional, finansial, jadwal, dan hukum beserta mitigasinya
  - [ ] B.2.8. Kesimpulan kelayakan per dimensi dan rekomendasi akhir (GO WITH CONDITIONS)
  - [ ] B.2.9. Prasyarat dan catatan penting sebelum melanjutkan

- [ ] **B.3.** Dari `03_stakeholder_register.md`, rangkum dan catat data berikut:
  - [ ] B.3.1. Daftar seluruh 19 stakeholder (14 internal + 5 eksternal) beserta ID, nama, peran, dan kategori
  - [ ] B.3.2. Profil detail setiap stakeholder: kebutuhan, ekspektasi, hak akses RBAC, dan status ketenagakerjaan
  - [ ] B.3.3. Matriks Power/Interest Grid per stakeholder
  - [ ] B.3.4. Matriks Pengaruh/Dampak dan prioritas pengelolaan
  - [ ] B.3.5. Engagement Assessment Matrix (kondisi saat ini vs diharapkan)
  - [ ] B.3.6. Strategi komunikasi dan rencana pengelolaan stakeholder
  - [ ] B.3.7. Matriks Pemetaan Modul vs Stakeholder

- [ ] **B.4.** Dari `04_tech_stack_decision.md`, rangkum dan catat data berikut:
  - [ ] B.4.1. Batasan teknologi mandatori (6 keputusan non-negotiable)
  - [ ] B.4.2. Prinsip arsitektur panduan (7 prinsip)
  - [ ] B.4.3. Keputusan tech stack per komponen (bahasa, database, pustaka, OS, antarmuka, keamanan)
  - [ ] B.4.4. Strategi keamanan dan autentikasi (bcrypt, JWT, RBAC, Audit Trail, SQL Injection, Rate Limiting)
  - [ ] B.4.5. Strategi infrastruktur (Client-Server LAN, Dual-OS)
  - [ ] B.4.6. Strategi pengembangan (requirements.txt, schema.sql, seed.sql, unit testing)

- [ ] **B.5.** Dari `05_innovation_proposal.md`, rangkum dan catat data berikut:
  - [ ] B.5.1. Daftar 30 inovasi terintegrasi (INV-INT-01 sampai INV-INT-30) dengan deskripsi, justifikasi, dan dampak bisnis
  - [ ] B.5.2. Daftar 3 rekomendasi inovasi sebelumnya (INV-REC-01 sampai INV-REC-03)
  - [ ] B.5.3. Daftar 9 inovasi tambahan baru (INV-NEW-01 sampai INV-NEW-09) dengan parameter spesifik
  - [ ] B.5.4. Matriks kelayakan inovasi dan prioritasi implementasi
  - [ ] B.5.5. Pemetaan inovasi terhadap 9 modul sistem
  - [ ] B.5.6. Dampak inovasi terhadap fase SDLC selanjutnya
  - [ ] B.5.7. Parameter konfigurasi spesifik (target laba Rp 15.000.000, persentase gaji 25%, limit kasbon Rp 1.000.000, threshold PPOB Rp 150.000, toleransi kas Rp 10.000, dll.)

- [ ] **B.6.** Dari `narasi.txt`, rangkum dan catat data berikut:
  - [ ] B.6.1. Jenis produk dan layanan (5 kategori lengkap dengan detailnya)
  - [ ] B.6.2. Alur kerja manual per divisi saat ini (detail langkah-langkah operasional)
  - [ ] B.6.3. Pengelolaan modal dan pinjaman (2 jenis sumber pendanaan)
  - [ ] B.6.4. Kondisi operasional pemilik (burnout, single-fighter)
  - [ ] B.6.5. Rencana struktur organisasi dan budaya kerja cross-functional
  - [ ] B.6.6. Harapan spesifik pemilik untuk aplikasi baru (seluruh bullet point)
  - [ ] B.6.7. Kebutuhan teknis (spesifikasi sistem dan tim pengembang)
  - [ ] B.6.8. Validasi silang: pastikan setiap poin di narasi.txt sudah terakomodasi di dokumen planning sebelumnya. Jika ada yang belum terakomodasi, tandai untuk dimasukkan ke BRD

---

### Fase C: Filtrasi dan Seleksi Data Spesifik untuk BRD

> **PENTING**: Dari hasil rangkuman Fase B, **hanya ambil data dan informasi yang secara spesifik dibutuhkan oleh dokumen Business Requirements**. Dokumen BRD harus bersih, fokus, dan hanya berisi data yang memang seharusnya ada di dalam dokumen ini. Jangan memasukkan data yang lebih cocok berada di dokumen SRS, SDD, atau dokumen teknis lainnya.

- [ ] **C.1.** Pilih dan kelompokkan data yang masuk ke dalam cakupan BRD:
  - [ ] C.1.1. **Konteks Bisnis**: Latar belakang usaha, permasalahan, dampak, dan justifikasi proyek
  - [ ] C.1.2. **Tujuan Bisnis**: Tujuan umum dan tujuan spesifik yang terukur (SMART)
  - [ ] C.1.3. **Pemangku Kepentingan**: Identifikasi aktor bisnis, kebutuhan, ekspektasi, dan hak akses per peran
  - [ ] C.1.4. **Proses Bisnis**: Alur kerja manual saat ini (as-is) dan alur kerja digital yang diharapkan (to-be) per divisi
  - [ ] C.1.5. **Kebutuhan Bisnis Fungsional**: Seluruh kebutuhan fitur per modul yang berorientasi bisnis (bukan teknis)
  - [ ] C.1.6. **Kebutuhan Bisnis Non-Fungsional**: Keamanan, privasi, keandalan, kecepatan, portabilitas
  - [ ] C.1.7. **Aturan Bisnis**: Kebijakan harga, skema pembayaran, penggajian, poin insentif, limit kasbon, threshold PPOB
  - [ ] C.1.8. **Batasan dan Asumsi Bisnis**: Batasan operasional, batasan anggaran, asumsi rekrutmen
  - [ ] C.1.9. **Kriteria Penerimaan Bisnis**: Indikator keberhasilan yang terukur per kebutuhan
  - [ ] C.1.10. **Risiko Bisnis**: Risiko yang berdampak pada kebutuhan bisnis beserta mitigasinya

- [ ] **C.2.** Pisahkan dan **jangan masukkan** data berikut ke dalam BRD (karena lebih cocok di dokumen lain):
  - [ ] C.2.1. Detail implementasi teknis kode program (FP patterns, closures, decorators) → SRS/SDD
  - [ ] C.2.2. Skema tabel database dan ERD → SDD
  - [ ] C.2.3. Konfigurasi server, jaringan LAN, dan topologi fisik → SDD/Deployment Guide
  - [ ] C.2.4. Detail pustaka Python dan versi spesifik → Tech Stack Decision/SDD
  - [ ] C.2.5. Skenario pengujian dan test cases → Test Plan

---

### Fase D: Penyusunan Dokumen BRD ke Target File

> **PENTING**: Susun dokumen BRD menggunakan kerangka struktur standar industri yang ditentukan pada Bagian 5 di bawah. Gunakan bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami. Setiap pernyataan kebutuhan bisnis harus bersifat **deklaratif** (menyatakan apa yang harus dicapai) dan **terverifikasi** (dapat diuji kebenarannya).

- [ ] **D.1.** Buat file header metadata (front matter YAML) di bagian paling atas target file dengan informasi:
  - [ ] D.1.1. `dokumen`: Business Requirements Document (BRD)
  - [ ] D.1.2. `proyek`: AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  - [ ] D.1.3. `versi`: 1.0
  - [ ] D.1.4. `tanggal`: (tanggal saat pengerjaan)
  - [ ] D.1.5. `status`: Draft
  - [ ] D.1.6. `penyusun`: Senior Business Analyst & Requirements Engineering Specialist

- [ ] **D.2.** Tulis bagian **Riwayat Perubahan Dokumen** dalam format tabel:
  - [ ] D.2.1. Kolom: Versi, Tanggal, Perubahan, Oleh
  - [ ] D.2.2. Isi baris pertama: versi 1.0, tanggal pengerjaan, "Pembuatan awal dokumen berdasarkan analisis seluruh dokumen fase Planning", persona pelaksana

- [ ] **D.3.** Tulis bagian **Informasi Dokumen** yang menjelaskan:
  - [ ] D.3.1. Tujuan dan cakupan dokumen BRD
  - [ ] D.3.2. Posisi dokumen dalam siklus SDLC (fase Analysis)
  - [ ] D.3.3. Hubungan dokumen BRD dengan dokumen SDLC lainnya (sebagai input untuk SRS, SDD, Test Plan)
  - [ ] D.3.4. Audiens target pembaca dokumen

- [ ] **D.4.** Tulis bagian **Ringkasan Eksekutif (Executive Summary)**:
  - [ ] D.4.1. Rangkuman kondisi bisnis saat ini
  - [ ] D.4.2. Permasalahan utama yang mendorong proyek
  - [ ] D.4.3. Solusi yang diusulkan secara garis besar
  - [ ] D.4.4. Manfaat bisnis utama yang diharapkan
  - [ ] D.4.5. Keputusan strategis (GO WITH CONDITIONS dari Feasibility Study)

- [ ] **D.5.** Tulis bagian **Profil Bisnis dan Konteks Operasional**:
  - [ ] D.5.1. Deskripsi usaha AbuCom (jenis usaha, lokasi, skala)
  - [ ] D.5.2. Struktur organisasi saat ini (single-fighter) dan yang direncanakan (7 posisi staf)
  - [ ] D.5.3. Kategori produk dan layanan (5 divisi usaha lengkap dengan rincian produk/jasa per divisi)
  - [ ] D.5.4. Budaya kerja yang diterapkan (cross-functional, saling melengkapi)
  - [ ] D.5.5. Sumber pendanaan usaha (pinjaman bank berbunga dan pinjaman kerabat tanpa bunga)

- [ ] **D.6.** Tulis bagian **Analisis Proses Bisnis**:
  - [ ] D.6.1. Proses Bisnis Saat Ini (*As-Is*): uraikan alur kerja manual per divisi berdasarkan narasi pemilik usaha
    - [ ] D.6.1.1. Alur kerja divisi Percetakan (Produk Unggulan)
    - [ ] D.6.1.2. Alur kerja divisi Penjualan ATK (Retail)
    - [ ] D.6.1.3. Alur kerja divisi Layanan Pulsa dan PPOB
    - [ ] D.6.1.4. Alur kerja divisi Jasa Keuangan (Transfer & Tarik Tunai)
    - [ ] D.6.1.5. Alur kerja divisi Jasa Teknis (Service & Install)
    - [ ] D.6.1.6. Alur kerja Administrasi Pinjaman, SDM, dan Pengeluaran
  - [ ] D.6.2. Identifikasi Titik Kelemahan (*Pain Points*) pada setiap proses bisnis as-is
  - [ ] D.6.3. Proses Bisnis yang Diharapkan (*To-Be*): uraikan alur kerja digital terotomatisasi yang diharapkan pemilik per divisi menggunakan sistem baru

- [ ] **D.7.** Tulis bagian **Pemangku Kepentingan dan Kebutuhan Bisnis per Aktor**:
  - [ ] D.7.1. Daftar aktor pengguna sistem (Pemilik, Kepala Percetakan, Pramuniaga, Kasir, Desainer, Produksi Cetak, Fotocopy/Print, Gudang)
  - [ ] D.7.2. Kebutuhan dan ekspektasi bisnis per aktor pengguna
  - [ ] D.7.3. Hak akses dan pembatasan menu per aktor (RBAC)
  - [ ] D.7.4. Aktor eksternal yang relevan (Pelanggan, Supplier, Bank BRI, Bank Mandiri, Kerabat/Keluarga)
  - [ ] D.7.5. Kebutuhan dan ekspektasi aktor eksternal

- [ ] **D.8.** Tulis bagian **Tujuan Bisnis dan Manfaat Terukur**:
  - [ ] D.8.1. Tujuan umum proyek
  - [ ] D.8.2. Tujuan spesifik yang terukur (SMART Goals S.1 sampai S.5)
  - [ ] D.8.3. Manfaat bisnis kuantitatif (reduksi waktu pembukuan, efisiensi limbah, penyelamatan transaksi, skalabilitas)
  - [ ] D.8.4. Manfaat bisnis kualitatif (reduksi stres, kredibilitas, keamanan internal, kesiapan ekspansi)

- [ ] **D.9.** Tulis bagian **Kebutuhan Bisnis Fungsional** yang dikelompokkan per modul sistem:
  - [ ] D.9.1. **Modul Manajemen Transaksi & Kebijakan Harga (M.1)**:
    - [ ] D.9.1.1. Kebutuhan pencatatan transaksi penjualan multi-divisi
    - [ ] D.9.1.2. Kebutuhan skema pembayaran fleksibel (DP dan Pelunasan)
    - [ ] D.9.1.3. Kebutuhan multi-skema harga (Retail, Grosir berdasarkan kuantitas, Mitra)
    - [ ] D.9.1.4. Kebutuhan alur pembatalan dan retur (pengembalian DP, sinkronisasi kas & stok)
  - [ ] D.9.2. **Modul Manajemen Inventaris, BOM & Stock Opname (M.2)**:
    - [ ] D.9.2.1. Kebutuhan HPP otomatis berbasis Bill of Materials (BOM) multi-bahan
    - [ ] D.9.2.2. Kebutuhan pemakaian bahan baku dimensi desimal (panjang x lebar) dan volume desimal
    - [ ] D.9.2.3. Kebutuhan sinkronisasi barang retail ATK untuk produksi internal
    - [ ] D.9.2.4. Kebutuhan pencatatan supplier/vendor, riwayat harga beli, dan hutang usaha
    - [ ] D.9.2.5. Kebutuhan rekonsiliasi stok (Stock Opname) berkala
    - [ ] D.9.2.6. Kebutuhan pencatatan limbah produksi (Waste Management)
    - [ ] D.9.2.7. Kebutuhan manajemen satuan dan atribut barang (Unit of Measure)
  - [ ] D.9.3. **Modul Layanan Keuangan Digital, PPOB, Jasa Keuangan & Service (M.3)**:
    - [ ] D.9.3.1. Kebutuhan pelacakan saldo PPOB 2 akun terpisah dengan alert deposit
    - [ ] D.9.3.2. Kebutuhan pencatatan transaksi transfer & tarik tunai dengan 6 akun digital
    - [ ] D.9.3.3. Kebutuhan pencatatan transaksi jasa service printer dan install laptop/PC
  - [ ] D.9.4. **Modul Manajemen SDM, Penggajian & Poin Karyawan (M.4)**:
    - [ ] D.9.4.1. Kebutuhan pencatatan data profil karyawan, absensi, dan kasbon
    - [ ] D.9.4.2. Kebutuhan penggajian otomatis cerdas (gaji tetap vs persentase laba)
    - [ ] D.9.4.3. Kebutuhan pemotongan gaji otomatis untuk kasbon aktif
    - [ ] D.9.4.4. Kebutuhan sistem poin insentif beban kerja (4 tier: 1, 3, 5, 10 poin)
  - [ ] D.9.5. **Modul Sistem Manajemen Antrian & Pelacakan Desain (M.5)**:
    - [ ] D.9.5.1. Kebutuhan antrian pekerjaan (Job Tracking) dengan 5 status transisi
    - [ ] D.9.5.2. Kebutuhan arsip desain pelanggan untuk cetak ulang cepat
  - [ ] D.9.6. **Modul Administrasi Pinjaman, Aset, & Pengeluaran Rutin (M.6)**:
    - [ ] D.9.6.1. Kebutuhan pencatatan pinjaman tanpa bunga (transparansi penarikan fleksibel)
    - [ ] D.9.6.2. Kebutuhan pencatatan pinjaman bank berbunga (BRI & Mandiri: setoran, tenor, jatuh tempo)
    - [ ] D.9.6.3. Kebutuhan pencatatan pengeluaran rutin, biaya tak terduga, aset tetap, tabungan alat
    - [ ] D.9.6.4. Kebutuhan laporan laba/rugi komprehensif (harian, bulanan, tahunan per divisi)
    - [ ] D.9.6.5. Kebutuhan rekonsiliasi kas laci kasir harian
  - [ ] D.9.7. **Modul Keamanan, Audit Trail & Hak Akses (M.7)**:
    - [ ] D.9.7.1. Kebutuhan pembatasan hak akses (RBAC: Pemilik vs Karyawan per posisi)
    - [ ] D.9.7.2. Kebutuhan pencatatan riwayat aktivitas (Audit Trail)
    - [ ] D.9.7.3. Kebutuhan keamanan data kredensial (enkripsi sandi, autentikasi session)
    - [ ] D.9.7.4. Kebutuhan perlindungan data pribadi (kepatuhan UU PDP)
  - [ ] D.9.8. **Modul Pembatalan, Retur & CRM (M.8)**:
    - [ ] D.9.8.1. Kebutuhan alur retur dan pembatalan transaksi
    - [ ] D.9.8.2. Kebutuhan database pelanggan (CRM: nama, WA, riwayat transaksi)
  - [ ] D.9.9. **Modul Skalabilitas Multi-Cabang (M.9)**:
    - [ ] D.9.9.1. Kebutuhan arsitektur data multi-cabang ready
    - [ ] D.9.9.2. Kebutuhan identifikasi ID cabang pada setiap entitas data

  > **CATATAN PENTING untuk D.9**: Setiap kebutuhan bisnis fungsional harus ditulis dengan format yang konsisten mencakup:
  > - **ID Kebutuhan**: Kode unik (contoh: BR-F-01, BR-F-02, dst.)
  > - **Nama Kebutuhan**: Judul singkat dan deskriptif
  > - **Deskripsi**: Penjelasan lengkap kebutuhan bisnis
  > - **Aktor/Pengguna Terkait**: Siapa yang menggunakan fitur ini
  > - **Aturan Bisnis**: Kebijakan atau formula yang berlaku
  > - **Kriteria Penerimaan**: Indikator keberhasilan yang terukur
  > - **Prioritas**: High / Medium / Low
  > - **Sumber Data**: Referensi ke dokumen planning terkait

- [ ] **D.10.** Tulis bagian **Kebutuhan Bisnis Non-Fungsional**:
  - [ ] D.10.1. Kebutuhan keamanan dan privasi hak akses
  - [ ] D.10.2. Kebutuhan audit dan pelacakan aktivitas
  - [ ] D.10.3. Kebutuhan keamanan data kredensial
  - [ ] D.10.4. Kebutuhan keandalan dan paradigma pemrograman
  - [ ] D.10.5. Kebutuhan portabilitas lintas OS
  - [ ] D.10.6. Kebutuhan kecepatan respons sistem
  - [ ] D.10.7. Kebutuhan skalabilitas dan multi-cabang

  > **CATATAN untuk D.10**: Setiap kebutuhan non-fungsional ditulis dengan format:
  > - **ID Kebutuhan**: Kode unik (contoh: BR-NF-01, BR-NF-02, dst.)
  > - **Nama Kebutuhan**: Judul singkat
  > - **Deskripsi**: Penjelasan lengkap
  > - **Kriteria Penerimaan**: Metrik terukur (misalnya: "waktu pembuatan laporan < 5 detik")
  > - **Prioritas**: High / Medium / Low

- [ ] **D.11.** Tulis bagian **Aturan Bisnis (Business Rules)**:
  - [ ] D.11.1. Aturan kebijakan harga (retail, grosir berdasarkan kuantitas minimum, mitra)
  - [ ] D.11.2. Aturan pembayaran bertahap (DP di awal, pelunasan saat pengambilan)
  - [ ] D.11.3. Aturan penggajian cerdas (gaji tetap jika laba ≥ Rp 15.000.000, persentase 25% dari laba bersih jika target tidak tercapai, jaminan minimum 50% UMR)
  - [ ] D.11.4. Aturan poin insentif karyawan (1 poin = Rp 500, 3 poin = Rp 1.500, 5 poin = Rp 2.500, 10 poin = Rp 5.000)
  - [ ] D.11.5. Aturan kasbon karyawan (limit Rp 1.000.000 atau 30% gaji, potong gaji otomatis)
  - [ ] D.11.6. Aturan threshold PPOB (alert jika saldo < Rp 150.000, deposit minimal Rp 500.000)
  - [ ] D.11.7. Aturan status antrian pekerjaan (transisi: Antri → Proses Desain → Produksi → Selesai → Diambil)
  - [ ] D.11.8. Aturan rekonsiliasi kas (toleransi selisih maksimal Rp 10.000 per shift kasir)
  - [ ] D.11.9. Aturan rate limiting login (maks 5 kali gagal → kunci 10 menit)
  - [ ] D.11.10. Aturan session timeout (JWT 8 jam = 1 shift kerja)
  - [ ] D.11.11. Aturan pembatalan dan retur (pengembalian DP, sinkronisasi kas & stok)
  - [ ] D.11.12. Aturan pinjaman tanpa bunga (penarikan fleksibel, transparan)
  - [ ] D.11.13. Aturan pinjaman bank (setoran bulanan, tenor, bunga, alert H-3 jatuh tempo)

- [ ] **D.12.** Tulis bagian **Inovasi dan Rekomendasi Best Practice**:
  - [ ] D.12.1. Ringkasan inovasi terintegrasi yang berdampak pada kebutuhan bisnis (pilih yang relevan)
  - [ ] D.12.2. Ringkasan inovasi tambahan baru yang direkomendasikan (9 inovasi dari INV-NEW)
  - [ ] D.12.3. Dampak inovasi terhadap kebutuhan bisnis dan prioritas implementasi

- [ ] **D.13.** Tulis bagian **Batasan dan Asumsi Bisnis**:
  - [ ] D.13.1. Batasan operasional (antarmuka CLI, single-branch awal, data pihak ketiga manual)
  - [ ] D.13.2. Batasan anggaran (CAPEX Rp 40.000.000)
  - [ ] D.13.3. Batasan waktu (12 bulan pengembangan)
  - [ ] D.13.4. Asumsi rekrutmen (7 staf baru sebelum go-live)
  - [ ] D.13.5. Asumsi ketersediaan data awal (migrasi dari Excel)
  - [ ] D.13.6. Asumsi infrastruktur (koneksi LAN stabil, listrik stabil)

- [ ] **D.14.** Tulis bagian **Risiko Bisnis dan Mitigasi**:
  - [ ] D.14.1. Risiko burnout pemilik
  - [ ] D.14.2. Risiko ketidakakuratan migrasi data Excel
  - [ ] D.14.3. Risiko penarikan dana mendadak (pinjaman tanpa bunga)
  - [ ] D.14.4. Risiko kecurangan karyawan (fraud)
  - [ ] D.14.5. Risiko ketidaksesuaian karyawan baru (literasi CLI rendah)
  - [ ] D.14.6. Risiko keterlambatan rekrutmen staf
  - [ ] D.14.7. Format tabel: Risiko, Probabilitas, Dampak, Mitigasi

- [ ] **D.15.** Tulis bagian **Kriteria Penerimaan Bisnis (Business Acceptance Criteria)**:
  - [ ] D.15.1. Otomatisasi laporan finansial (100% bebas Excel)
  - [ ] D.15.2. Akurasi sinkronisasi stok bahan baku (< 1.0% selisih)
  - [ ] D.15.3. Efisiensi antrian produksi (zero-missed orders)
  - [ ] D.15.4. Integritas keamanan hak akses (100% terjaga)
  - [ ] D.15.5. Mitigasi burnout pemilik (delegasi 100% operasional ke staf)
  - [ ] D.15.6. Setiap kriteria dilengkapi indikator dan metode uji

- [ ] **D.16.** Tulis bagian **Glosarium Istilah Bisnis dan Domain Percetakan**:
  - [ ] D.16.1. Salin seluruh istilah glosarium dari Project Charter dan Feasibility Study
  - [ ] D.16.2. Tambahkan istilah baru yang muncul di dokumen BRD ini (jika ada)
  - [ ] D.16.3. Pastikan setiap istilah disusun secara alfabetis

- [ ] **D.17.** Tulis bagian **Referensi Dokumen** di bagian akhir baris paling bawah:
  - [ ] D.17.1. Buat tabel daftar file referensi yang digunakan dalam penyusunan BRD
  - [ ] D.17.2. Format tabel: #, Nama File, Lokasi Path Relatif, Keterangan
  - [ ] D.17.3. Masukkan ke-6 file referensi yang tertera pada Bagian 3.1 issue ini

---

### Fase E: Penandaan Data Kosong

> **PENTING**: Jika ada data atau informasi yang dibutuhkan oleh BRD tetapi **TIDAK DITEMUKAN** di dalam file referensi, maka data tersebut **JANGAN dikarang atau dihalusinasi**. Tandai data kosong tersebut menggunakan format placeholder berikut agar dapat diketahui dan diisi secara manual oleh pemilik usaha:

**Format penandaan data kosong:**
```
`[BELUM TERSEDIA — Diisi oleh Pemilik Usaha. Contoh: {deskripsi data yang dibutuhkan}]`
```

- [ ] **E.1.** Periksa seluruh isi dokumen BRD yang telah ditulis.
- [ ] **E.2.** Identifikasi setiap bagian yang membutuhkan data spesifik dari pemilik namun tidak tersedia di file referensi.
- [ ] **E.3.** Tandai setiap data kosong menggunakan format placeholder di atas.
- [ ] **E.4.** Contoh data yang mungkin kosong (berdasarkan pengamatan file referensi):
  - Nama lengkap pemilik usaha
  - Alamat toko fisik
  - Nominal UMR daerah operasional
  - Jumlah omzet rata-rata bulanan aktual
  - Nama supplier utama bahan baku
  - Detail pinjaman bank (nominal, bunga, sisa tenor)
  - Data spesifik staf yang sudah direkrut (jika ada)

---

### Fase F: Validasi Akhir dan Penulisan ke Target File

- [ ] **F.1.** Validasi bahwa seluruh bagian kerangka dokumen BRD (Bagian 5) sudah terisi lengkap.
- [ ] **F.2.** Validasi bahwa setiap kebutuhan bisnis fungsional memiliki ID unik, deskripsi, aktor, aturan bisnis, kriteria penerimaan, prioritas, dan sumber data.
- [ ] **F.3.** Validasi bahwa setiap kebutuhan bisnis non-fungsional memiliki ID unik, deskripsi, kriteria terukur, dan prioritas.
- [ ] **F.4.** Validasi bahwa tidak ada data yang dikarang atau dihalusinasi — semua data bersumber dari file referensi.
- [ ] **F.5.** Validasi bahwa data kosong sudah ditandai dengan format placeholder.
- [ ] **F.6.** Validasi bahwa bahasa Indonesia yang digunakan natural, tidak ambigu, dan mudah dipahami.
- [ ] **F.7.** Validasi bahwa bagian Referensi Dokumen sudah lengkap di bagian akhir dokumen.
- [ ] **F.8.** Validasi bahwa dokumen ini memiliki kualitas kelengkapan isi yang cukup untuk dijadikan referensi, acuan, dan input utama bagi dokumen pada fase SDLC selanjutnya (SRS, SDD, Test Plan) tanpa perlu dipertanyakan ulang.
- [ ] **F.9.** Tuangkan seluruh hasil penyusunan dokumen BRD ke target file: `docs/sdlc/02_analysis/01_business_requirements.md`
- [ ] **F.10.** Pastikan dokumen ditulis secara utuh dan lengkap dari awal hingga akhir ke target file. **JANGAN melakukan pemotongan (truncation), penyingkatan, atau penggantian isi dengan placeholder seperti "... (sama seperti di atas)" atau "... (lihat referensi)"**. Setiap bagian harus ditulis penuh dan lengkap.

---

## 5. Kerangka Struktur Dokumen BRD (Standar Industri)

Berikut adalah kerangka struktur dokumen Business Requirements Document yang harus diikuti. Kerangka ini disusun berdasarkan standar praktik industri (IEEE, BABOK, PMBOK) yang disesuaikan dengan konteks proyek UMKM AbuCom:

```
---
(metadata YAML front matter)
---

# Business Requirements Document (BRD) — AbuCom

## Riwayat Perubahan Dokumen
(tabel riwayat versi)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target

---

## 2. Ringkasan Eksekutif (Executive Summary)

---

## 3. Profil Bisnis dan Konteks Operasional
### 3.1. Deskripsi Usaha
### 3.2. Struktur Organisasi (Saat Ini dan Rencana)
### 3.3. Kategori Produk dan Layanan (5 Divisi)
### 3.4. Budaya Kerja
### 3.5. Sumber Pendanaan Usaha

---

## 4. Analisis Proses Bisnis
### 4.1. Proses Bisnis Saat Ini (As-Is)
#### 4.1.1. Alur Kerja Divisi Percetakan
#### 4.1.2. Alur Kerja Divisi Penjualan ATK
#### 4.1.3. Alur Kerja Divisi Layanan Pulsa dan PPOB
#### 4.1.4. Alur Kerja Divisi Jasa Keuangan
#### 4.1.5. Alur Kerja Divisi Jasa Teknis
#### 4.1.6. Alur Kerja Administrasi Pinjaman, SDM, dan Pengeluaran
### 4.2. Identifikasi Titik Kelemahan (Pain Points)
### 4.3. Proses Bisnis yang Diharapkan (To-Be)

---

## 5. Pemangku Kepentingan dan Kebutuhan Bisnis per Aktor
### 5.1. Aktor Internal Pengguna Sistem
### 5.2. Kebutuhan dan Ekspektasi per Aktor
### 5.3. Hak Akses dan Pembatasan Menu per Aktor (RBAC)
### 5.4. Aktor Eksternal
### 5.5. Kebutuhan dan Ekspektasi Aktor Eksternal

---

## 6. Tujuan Bisnis dan Manfaat Terukur
### 6.1. Tujuan Umum
### 6.2. Tujuan Spesifik (SMART Goals)
### 6.3. Manfaat Bisnis Kuantitatif
### 6.4. Manfaat Bisnis Kualitatif

---

## 7. Kebutuhan Bisnis Fungsional
### 7.1. Modul Manajemen Transaksi & Kebijakan Harga (M.1)
### 7.2. Modul Manajemen Inventaris, BOM & Stock Opname (M.2)
### 7.3. Modul Layanan Keuangan Digital, PPOB, Jasa Keuangan & Service (M.3)
### 7.4. Modul Manajemen SDM, Penggajian & Poin Karyawan (M.4)
### 7.5. Modul Sistem Manajemen Antrian & Pelacakan Desain (M.5)
### 7.6. Modul Administrasi Pinjaman, Aset, & Pengeluaran Rutin (M.6)
### 7.7. Modul Keamanan, Audit Trail & Hak Akses (M.7)
### 7.8. Modul Pembatalan, Retur & CRM (M.8)
### 7.9. Modul Skalabilitas Multi-Cabang (M.9)

---

## 8. Kebutuhan Bisnis Non-Fungsional
### 8.1. Keamanan dan Privasi
### 8.2. Audit dan Pelacakan Aktivitas
### 8.3. Keamanan Kredensial
### 8.4. Keandalan Sistem
### 8.5. Portabilitas
### 8.6. Kecepatan Respons
### 8.7. Skalabilitas

---

## 9. Aturan Bisnis (Business Rules)

---

## 10. Inovasi dan Rekomendasi Best Practice
### 10.1. Inovasi Terintegrasi
### 10.2. Inovasi Tambahan Baru
### 10.3. Dampak dan Prioritas Implementasi

---

## 11. Batasan dan Asumsi Bisnis
### 11.1. Batasan Operasional
### 11.2. Batasan Anggaran dan Waktu
### 11.3. Asumsi Bisnis

---

## 12. Risiko Bisnis dan Mitigasi

---

## 13. Kriteria Penerimaan Bisnis (Business Acceptance Criteria)

---

## 14. Glosarium Istilah Bisnis dan Domain Percetakan

---

## 15. Referensi Dokumen
```

---

## 6. Instruksi Tambahan dan Kaidah Penulisan

### 6.1. Kaidah Bahasa dan Gaya Penulisan
- [ ] Gunakan bahasa Indonesia yang baku, natural, dan mudah dipahami.
- [ ] Hindari kalimat yang terlalu panjang dan berbelit-belit. Gunakan kalimat yang ringkas namun informatif.
- [ ] Hindari penggunaan jargon teknis implementasi (kode program, nama pustaka, nama fungsi) di bagian kebutuhan bisnis. Gunakan bahasa bisnis dan operasional.
- [ ] Jika harus menggunakan istilah teknis, pastikan istilah tersebut sudah didefinisikan di Glosarium.
- [ ] Setiap pernyataan kebutuhan bisnis harus bersifat **deklaratif** (menyatakan apa yang harus dicapai, bukan bagaimana cara mencapainya).
- [ ] Setiap pernyataan kebutuhan bisnis harus bersifat **terverifikasi** (dapat diuji kebenarannya dengan metode uji yang jelas).

### 6.2. Kaidah Konsistensi dan Traceability
- [ ] Gunakan ID unik yang konsisten untuk setiap kebutuhan bisnis (BR-F-xx untuk fungsional, BR-NF-xx untuk non-fungsional).
- [ ] Setiap kebutuhan bisnis harus merujuk ke sumber data asli di file referensi (contoh: "Sumber: Project Charter v1.1, Bagian 4.1.1 [M.1]").
- [ ] Pastikan tidak ada kebutuhan bisnis yang bertentangan atau kontradiktif satu sama lain.

### 6.3. Kaidah Kelengkapan Konten
- [ ] Jangan memotong atau menyingkat isi dokumen. Tulis secara utuh dan lengkap dari awal hingga akhir.
- [ ] Jangan menggunakan placeholder seperti "... (sama seperti sebelumnya)" atau "... (lihat referensi)" untuk menggantikan konten yang seharusnya ditulis.
- [ ] Setiap tabel harus diisi secara lengkap, tidak boleh ada baris yang kosong tanpa keterangan.
- [ ] Pastikan setiap bagian kerangka dokumen terisi — jika suatu bagian tidak relevan, tuliskan alasan mengapa bagian tersebut tidak relevan.

### 6.4. Kaidah Keunikan Dokumen BRD
Beberapa kaidah spesifik yang menjadi ciri khas dokumen Business Requirements:
- [ ] Dokumen BRD **berfokus pada perspektif bisnis**, bukan perspektif teknis implementasi.
- [ ] Setiap kebutuhan harus menjawab pertanyaan **"APA yang dibutuhkan bisnis?"** bukan **"BAGAIMANA sistem mengimplementasikan?"**.
- [ ] Bagian Analisis Proses Bisnis (As-Is dan To-Be) adalah komponen kunci pembeda BRD dari dokumen SDLC lainnya. Bagian ini harus ditulis secara detail dan komprehensif.
- [ ] Aturan Bisnis (*Business Rules*) harus didokumentasikan dengan nilai parameter yang eksplisit dan spesifik (angka, persentase, nominal rupiah).
- [ ] Kriteria Penerimaan Bisnis harus dapat diukur secara kuantitatif dan diverifikasi secara objektif.

### 6.5. Instruksi Tambahan untuk Memastikan Kualitas
- [ ] Pastikan isi dokumen BRD ini layak dijadikan satu-satunya referensi utama bagi tim pengembang saat menyusun dokumen SRS (Software Requirements Specification) pada fase berikutnya.
- [ ] Pastikan isi dokumen BRD ini tidak menyisakan pertanyaan mendasar yang harus ditanyakan ulang kepada pemilik usaha, kecuali data yang memang harus diisi secara manual oleh pemilik (ditandai dengan placeholder).
- [ ] Pastikan dokumen BRD ini menyediakan konteks bisnis yang cukup agar dokumen SDD (System Design Document) dapat merancang skema database dan arsitektur sistem yang sesuai.
- [ ] Pastikan seluruh 42 inovasi yang tercatat di Innovation Proposal terakomodasi sebagai kebutuhan bisnis di dokumen BRD ini (baik sebagai kebutuhan fungsional maupun non-fungsional).

---

## 7. Lokasi Target File Output

```
docs/sdlc/02_analysis/01_business_requirements.md
```

Tulis seluruh hasil pengerjaan pembuatan dan penyusunan dokumen Business Requirements ke file di atas. File ini sudah ada (kosong) dan siap ditulisi.

---

## 8. Ringkasan Checklist Eksekusi

| Fase | Deskripsi | Status |
|------|-----------|--------|
| **A** | Pembacaan 6 file referensi secara menyeluruh | `[ ]` |
| **B** | Perangkuman seluruh data dari 6 file referensi | `[ ]` |
| **C** | Filtrasi dan seleksi data spesifik untuk BRD | `[ ]` |
| **D** | Penyusunan dokumen BRD sesuai kerangka standar industri (17 sub-bagian) | `[ ]` |
| **E** | Penandaan data kosong dengan format placeholder | `[ ]` |
| **F** | Validasi akhir dan penulisan ke target file | `[ ]` |

---

## 9. Referensi Issue

| # | Nama File | Lokasi | Keterangan |
|---|-----------|--------|------------|
| 1 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Dokumen Project Charter v1.1 — referensi primer utama |
| 2 | `02_feasibility_study.md` | `docs/sdlc/01_planning/02_feasibility_study.md` | Dokumen Feasibility Study v1.1 — referensi primer |
| 3 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Dokumen Stakeholder Register v1.1 — referensi primer |
| 4 | `04_tech_stack_decision.md` | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Dokumen Tech Stack Decision v1.1 — referensi sekunder |
| 5 | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Dokumen Innovation Proposal v1.1 — referensi sekunder |
| 6 | `narasi.txt` | `docs/sdlc/narasi.txt` | Narasi asli pemilik usaha — referensi pendukung cross-check |
