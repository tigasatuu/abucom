---
dokumen    : Project Charter
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.1
tanggal    : 2026-05-21
status     : Validated
penyusun   : Senior Project Manager / Lead Business Analyst
---

# Project Charter — AbuCom

## Riwayat Perubahan Dokumen

| Versi | Tanggal    | Perubahan                                                   | Oleh                                            |
|-------|------------|-------------------------------------------------------------|-------------------------------------------------|
| 1.0   | 2026-05-20 | Pembuatan awal dokumen berdasarkan analisis `narasi.txt`    | Senior Project Manager / Lead Business Analyst  |
| 1.1   | 2026-05-21 | Penyempurnaan menyeluruh berdasarkan validasi issue #0002. Melengkapi estimasi anggaran, menambahkan modul limbah produksi & manajemen satuan, detail alur kerja manual, metodologi pengembangan, manfaat terukur, dependensi, dan eliminasi placeholder. | Principal Business Analyst & Senior Technical PM |

---

## 1. Informasi Umum Proyek

### 1.1. Nama Proyek
**AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**  
*(Aplikasi manajemen internal terintegrasi untuk otomatisasi operasional percetakan, retail ATK, layanan digital/PPOB, jasa keuangan, dan jasa teknis).*

### 1.2. Deskripsi Singkat Proyek
Proyek ini bertujuan untuk merancang dan membangun sistem aplikasi manajemen terpadu berbasis *Command Line Interface* (CLI) untuk mengotomatisasi seluruh kegiatan operasional harian pada usaha UMKM AbuCom. Sistem ini dirancang menggunakan bahasa pemrograman Python 3.14.2+ dengan paradigma *Functional Programming* murni dan didukung oleh sistem basis data relasional MySQL. Aplikasi ini akan mengintegrasikan manajemen transaksi penjualan, manajemen inventaris barang baku & retail dengan metode *Bill of Materials* (BOM) presisi, pencatatan limbah produksi, manajemen keuangan terpadu (laba/rugi, pengeluaran rutin, tabungan aset, administrasi pinjaman modal), sistem *job tracking* antrian produksi, manajemen SDM & penggajian cerdas, serta arsip desain pelanggan. Sistem ini juga dirancang dengan arsitektur yang siap dikembangkan untuk kebutuhan multi-cabang (*Multi-Branch Ready*).

### 1.3. Sponsor / Pemilik Proyek
* **Nama**: Pemilik Usaha UMKM Percetakan AbuCom  
* **Peran**: Inisiator Proyek, Pemilik Bisnis, Penyedia Pendanaan (Sponsor), dan Pengguna Utama (*Key User*).

### 1.4. Manajer Proyek / Penanggung Jawab
**Pemilik Usaha AbuCom (bertindak sebagai Junior Programmer & Manajer Proyek Internal)**  
*(Bertanggung jawab atas koordinasi internal proyek, integrasi fungsional CLI, pengujian langsung, serta penyelarasan keputusan bisnis).*

### 1.5. Tanggal Mulai Proyek
`2026-05-20` (Tanggal inisiasi proyek berdasarkan pembuatan issue).

### 1.6. Perkiraan Tanggal Selesai
`2027-05-20`  
*(Berdasarkan arahan pemilik proyek untuk draf awal, estimasi jangka waktu keseluruhan pengerjaan proyek direncanakan berlangsung selama **12 bulan**).*

### 1.7. Versi Dokumen
**Versi 1.1** (Diperbarui dan disempurnakan berdasarkan validasi formal).

---

## 2. Latar Belakang dan Justifikasi Proyek

### 2.1. Kondisi Saat Ini (Current State)
Usaha UMKM AbuCom merupakan penyedia layanan jasa percetakan dan beberapa unit usaha pendukung yang berlokasi di satu tempat fisik. Saat ini, seluruh operasional usaha dikelola dan dijalankan secara mandiri oleh pemilik usaha *(single-fighter)* `[ref: narasi.txt, baris 1]`.  

Usaha ini melayani lima kategori produk dan layanan utama yang kompleks `[ref: narasi.txt, baris 3-18]`:
1. **Produk Percetakan (Produksi Sendiri)**: Stempel flash, cetak foto, pembuatan buku yasin, undangan pernikahan, cetak baliho, fotokopi, pengetikan dokumen, print data, cetak stiker, hingga pembuatan nama dada dan jasa percetakan kustom.
2. **Alat Tulis Kantor / ATK (Retail)**: Penjualan barang retail fisik seperti kertas HVS, kertas foto, kertas undangan, tinta printer, pulpen, hekter, berbagai map (snelhechter, biasa, warna), lakban, selotip, pensil, dan perlengkapan kantor.
3. **Layanan Digital & PPOB**: Penjualan pulsa HP, pulsa listrik (token), paket data, dan pembayaran tagihan listrik bulanan.
4. **Jasa Keuangan**: Layanan transfer uang antar bank dan jasa tarik tunai.
5. **Jasa Teknis**: Layanan perbaikan (service) printer serta instalasi ulang sistem operasi pada komputer dan laptop pelanggan.

Seluruh pencatatan transaksi keuangan, pelacakan sisa stok bahan baku, mutasi akun digital, pembayaran pinjaman modal, dan rekapitulasi data masih dikerjakan secara manual oleh pemilik menggunakan Microsoft Excel dengan file yang berserakan dan tidak terintegrasi `[ref: narasi.txt, baris 47]`. Berikut adalah gambaran alur kerja manual per divisi saat ini `[ref: narasi.txt, baris 49-70]`:
*   **Divisi Percetakan (Produk Unggulan)**: Pemilik melayani pelanggan, mendesain pesanan kustom, mengambil bahan baku fisik di gudang, melakukan cetak dan *finishing* (pemotongan, laminasi, dll), mengemas hasil cetak, hingga menyerahkannya ke pelanggan. Setelah itu, pemilik mencatat transaksi di Excel, menghitung sisa stok bahan secara manual, memantau ketersediaan bahan, membuat daftar belanja pengadaan jika stok menipis, melakukan pembelian fisik ke supplier, dan menginput kembali bahan yang baru dibeli ke dalam database stok.
*   **Divisi ATK (Retail)**: Pemilik melayani pembeli langsung, memeriksa daftar harga di lembar kerja Excel, menjumlahkan total belanjaan, memberikan kembalian, dan secara manual mengurangi stok di Excel satu per satu. Pemilik juga harus melakukan pemeriksaan fisik berkala di gudang, merapikan pajangan, serta merencanakan pengadaan barang yang habis dengan menentukan harga jual baru berdasarkan harga beli terupdate dari supplier.
*   **Divisi Pulsa dan PPOB**: Mengelola dua akun saldo deposit terpisah (akun pulsa/data dan akun token/tagihan listrik). Pemilik harus memastikan saldo tidak habis secara fisik, melakukan deposit minimal Rp 500.000 jika saldo mendekati batas kritis Rp 150.000, serta mencatat setiap transaksi penjualan ke dalam Excel secara manual demi pelaporan keuangan.
*   **Divisi Jasa Keuangan**: Pemilik mengelola transaksi transfer dan tarik tunai menggunakan 6 akun uang elektronik/perbankan digital (Agen Bank Mandiri, Dana, Gopay, LinkAja, ShopeePay, OVO). Alur kerjanya adalah pemilik harus memilih akun dengan biaya admin termurah bagi pelanggan sesuai jenis layanan, menjaga keseimbangan saldo di setiap akun berdasarkan keramaian (*traffic*), dan mencatat manual setiap mutasi saldo di Excel.
*   **Divisi Jasa Teknis & Service**: Menerima printer rusak atau laptop/komputer pelanggan yang ingin diinstal ulang. Pemilik melakukan perbaikan fisik, melakukan pengetesan, menyerahkan kembali ke pelanggan, menerima pembayaran, dan mencatatnya ke dalam file Excel transaksi harian.
*   **Administrasi Pinjaman, SDM & Pengeluaran**:
    *   *Pinjaman Tanpa Bunga*: Pemilik mencatat secara manual siapa peminjamnya (sahabat, keluarga, orang tua), nominal yang ditarik/dikembalikan, dan sisa saldo terutang agar pencatatan tetap transparan mengingat penarikan dana bisa terjadi secara mendadak.
    *   *Pinjaman Bank*: Pemilik melacak jadwal setoran bulanan, bunga, sisa tenor, dan tanggal jatuh tempo Bank BRI & Bank Mandiri pada catatan Excel agar terhindar dari denda keterlambatan.
    *   *Administrasi SDM & Pengeluaran*: Pemilik mengelola pengeluaran rutin bulanan (air, listrik, internet), biaya tidak terduga, daftar aset fisik (printer, PC, CCTV), serta merencanakan pencatatan kasbon karyawan secara manual.

### 2.2. Permasalahan Utama (Problem Statement)
Kompleksitas pengelolaan lima divisi usaha yang berjalan bersamaan secara manual menyebabkan pemilik usaha mengalami stres berat, keletihan mental (*burnout*), dan kewalahan secara fisik `[ref: narasi.txt, baris 28]`. Pemilik harus membagi fokus antara melayani pelanggan langsung di toko, mengeksekusi produksi cetak, mengambil bahan baku, melakukan pembukuan keuangan, memantau stok, hingga merespon cepat order pelanggan melalui WhatsApp `[ref: narasi.txt, baris 28]`. Data Excel yang tidak sinkron membuat pemantauan sisa bahan baku di gudang tidak akurat, laporan laba rugi bulanan sulit dipastikan, dan terdapat risiko tinggi adanya transaksi atau pesanan pelanggan yang terlewat `[ref: narasi.txt, baris 70, 74, 86]`.

### 2.3. Dampak Jika Tidak Ditangani
Jika kondisi ini terus berlanjut tanpa adanya otomatisasi sistem:
* **Penurunan Kualitas Layanan**: Respons terhadap pelanggan melambat, pesanan terancam terlewat atau salah cetak, yang berujung pada hilangnya kepercayaan pelanggan.
* **Kerugian Finansial & Kebocoran Kas**: Kesalahan pencatatan kas/bank, selisih stok bahan baku yang rusak/hilang tanpa tercatat (limbah produksi tidak terukur), serta denda keterlambatan pembayaran pinjaman bank akibat lupa jatuh tempo.
* **Kegagalan Ekspansi Organisasi**: Rencana rekrutmen karyawan baru guna meringankan beban pemilik terancam gagal atau tidak terkendali karena belum tersedianya sistem absensi, sistem poin kinerja, dan manajemen kasbon/gaji yang terstruktur.
* **Masalah Kesehatan Pemilik**: *Burnout* berkepanjangan dapat mengganggu kesehatan pemilik, yang berpotensi menghentikan operasional usaha sepenuhnya mengingat posisi pemilik sebagai *single point of failure*.

---

## 3. Tujuan Proyek (Project Objectives)

### 3.1. Tujuan Umum
Merancang, membangun, dan menerapkan sistem aplikasi manajemen operasional dan keuangan terpadu berbasis CLI (Command Line Interface) yang modular, aman, dan berkinerja tinggi guna mengotomatisasi seluruh alur bisnis AbuCom, meniadakan ketergantungan pada pencatatan Excel manual yang berserakan, serta menyajikan laporan stok dan keuangan yang akurat secara real-time demi mendukung fokus pemilik pada pengembangan strategis usaha.

### 3.2. Tujuan Spesifik (SMART Goals)
* **S.1 (Otomatisasi Inventaris & Komposisi HPP)**: Mengurangi selisih antara stok barang fisik di gudang dengan catatan sistem hingga kurang dari 1.0% melalui fitur sinkronisasi otomatis menggunakan Bill of Materials (BOM) berdasarkan dimensi panjang x lebar atau volume secara presisi saat transaksi selesai `[ref: narasi.txt, baris 93, 95]`.
* **S.2 (Keuangan Instan & Laba/Rugi Divisi)**: Menyajikan laporan keuangan laba/rugi, pengeluaran rutin, dan tabungan aset secara instan (waktu pemrosesan < 5 detik) untuk memudahkan analisis profitabilitas per divisi layanan (5 kategori usaha) `[ref: narasi.txt, baris 83-84]`.
* **S.3 (Manajemen Antrian & Zero-Missed Orders)**: Mencapai tingkat *zero-missed orders* (tidak ada pesanan yang terlewat) melalui penerapan sistem pelacakan status pesanan (*job tracking*) digital dengan lima tahapan status terintegrasi `[ref: narasi.txt, baris 86]`.
* **S.4 (Manajemen SDM & Penggajian Fleksibel)**: Mempersiapkan kesiapan operasional rekrutmen 7 posisi staf baru melalui modul absensi yang terintegrasi langsung dengan sistem penggajian cerdas (gaji pokok/persentase keuntungan) dan manajemen kasbon otomatis `[ref: narasi.txt, baris 34-43, 67, 77]`.
* **S.5 (Arsitektur Multi-Cabang)**: Merancang database MySQL yang memiliki kesiapan 100% untuk menampung data multi-cabang (*Multi-Branch Ready*), sehingga siap digunakan untuk ekspansi cabang baru tanpa perlu merombak ulang skema data inti `[ref: narasi.txt, baris 97]`.

### 3.3. Manfaat Bisnis yang Terukur (Measurable Business Benefits)
Penerapan sistem aplikasi AbuCom ini ditargetkan memberikan manfaat bisnis nyata yang dapat diukur secara kuantitatif:
1. **Reduksi Waktu Pembukuan**: Mengurangi waktu rekapitulasi transaksi harian dan penyusunan laporan keuangan laba/rugi per divisi dari rata-rata **2-3 jam per hari** menjadi **instan (< 5 detik)** secara otomatis setelah transaksi selesai.
2. **Efisiensi Inventaris & Pencegahan Kerugian**: Menurunkan kerugian akibat bahan baku rusak atau tidak tercatat (limbah produksi) sebesar **15%** melalui fitur pelacakan limbah produksi yang tersinkronisasi.
3. **Penyelamatan Transaksi Terlewat**: Menghilangkan insiden pesanan yang terlewat atau lupa dikerjakan hingga **0% (Zero-Missed Orders)** menggunakan modul *Job Tracking* digital yang interaktif.
4. **Skalabilitas Operasional**: Membuka jalan bagi pemilik usaha untuk mendelegasikan **90%** operasional teknis harian kepada 7 staf baru tanpa khawatir terjadi kecurangan saldo atau kebocoran data keuangan sensitif berkat sistem RBAC dan log *Audit Trail* yang ketat.

---

## 4. Ruang Lingkup Proyek (Project Scope)

### 4.1. Dalam Ruang Lingkup (In-Scope)

#### 4.1.1. Modul / Fitur Utama
* **M.1. Modul Manajemen Transaksi & Kebijakan Harga**:
  * Mendukung pembayaran bertahap: Uang Muka (DP) dan Pelunasan saat barang diambil `[ref: narasi.txt, baris 76]`.
  * Mengelola multi-skema harga: harga retail, harga grosir (berdasarkan kuantitas), dan harga spesial untuk mitra bisnis `[ref: narasi.txt, baris 76]`.
* **M.2. Modul Manajemen Inventaris, BOM & Stock Opname**:
  * Pencatatan data supplier/vendor, riwayat harga beli barang, dan manajemen hutang pembelian barang `[ref: narasi.txt, baris 90]`.
  * Sistem Harga Pokok Penjualan (HPP) otomatis menggunakan komposisi bahan baku (*Bill of Materials* / BOM) multi-bahan untuk produk kustom (misal: satu stempel flash terdiri dari gagang stempel, tinta stempel, kertas buffalo, dan karet flash) `[ref: narasi.txt, baris 95]`.
  * Perhitungan pemakaian bahan lembaran/cairan berdasarkan satuan dimensi (panjang x lebar) atau volume desimal presisi (float) agar pengurangan stok bahan baku akurat sesuai ukuran riil pesanan `[ref: narasi.txt, baris 95-96]`.
  * **Pencatatan Limbah Produksi (Waste Management)**: Fitur khusus untuk mencatat bahan baku yang rusak atau salah cetak selama proses produksi, sehingga stok gudang dan aplikasi tetap sinkron dan biaya limbah dapat dianalisis `[ref: narasi.txt, baris 87]`.
  * **Manajemen Satuan & Atribut Barang (Unit of Measure)**: Dukungan pengelolaan berbagai jenis satuan ukur (rim, lembar, pcs, mililiter, gram, dimensi panjang x lebar) dan spesifikasi teknis unik untuk setiap kategori barang, dengan dukungan pencatatan stok desimal presisi untuk sisa bahan baku `[ref: narasi.txt, baris 96]`.
  * Fitur sinkronisasi barang retail (ATK) yang diambil untuk kebutuhan internal produksi (otomatis mengurangi stok ATK retail dan menambah biaya operasional produksi) `[ref: narasi.txt, baris 95]`.
  * Fitur rekonsiliasi stok (*Stock Opname*) berkala untuk mencocokkan stok fisik vs aplikasi serta menyimpan riwayat selisihnya `[ref: narasi.txt, baris 93]`.
* **M.3. Modul Layanan Keuangan Digital, PPOB, Jasa Keuangan & Service**:
  * Rekonsiliasi saldo akun digital PPOB (minimal deposit Rp 500.000 jika saldo < Rp 150.000) `[ref: narasi.txt, baris 55]`.
  * Pencatatan transaksi transfer uang & tarik tunai (memilih akun biaya admin paling murah bagi pelanggan) `[ref: narasi.txt, baris 58-59]`.
  * Pencatatan transaksi service printer & install laptop/komputer `[ref: narasi.txt, baris 61]`.
* **M.4. Modul Manajemen SDM, Penggajian & Poin Karyawan**:
  * Manajemen data karyawan, absensi harian, dan pencatatan riwayat kasbon karyawan dengan fitur potong gaji otomatis `[ref: narasi.txt, baris 67]`.
  * Penggajian otomatis cerdas (Gaji Tetap jika target laba bersih tercapai, atau Gaji Persentase Laba jika target tidak tercapai) `[ref: narasi.txt, baris 77]`.
  * Sistem Poin Karyawan (Insentif): transaksi rutin (1 poin/Rp 500), jasa dasar (3 poin/Rp 1.500), produk kustom (5 poin/Rp 2.500), dan pekerjaan teknis/berat (10 poin/Rp 5.000) `[ref: narasi.txt, baris 78-82]`.
* **M.5. Modul Sistem Manajemen Antrian & Pelacakan Desain**:
  * Pelacakan status pesanan (*job tracking*) dengan 5 status: `Antri`, `Proses Desain`, `Produksi`, `Selesai`, `Diambil` `[ref: narasi.txt, baris 86]`.
  * Arsip Desain Pelanggan: Pencatatan lokasi penyimpanan file desain untuk memudahkan cetak ulang `[ref: narasi.txt, baris 88]`.
* **M.6. Modul Administrasi Pinjaman, Aset, & Pengeluaran Rutin**:
  * Pencatatan pinjaman tanpa bunga (transparansi penarikan fleksibel) dan pinjaman bank (setoran bulanan, tenor, jatuh tempo Mandiri/BRI) `[ref: narasi.txt, baris 22-24, 65-66]`.
  * Manajemen aset tetap, depresiasi, pengeluaran operasional rutin, biaya tak terduga, dan tabungan khusus pengadaan alat baru `[ref: narasi.txt, baris 70]`.
* **M.7. Modul Keamanan, Audit Trail & Hak Akses**:
  * Pembatasan hak akses (*Role-based Access Control*): Menu khusus "Pemilik" (keuangan sensitif, tabungan, pinjaman) dan menu "Karyawan" (hanya terkait operasional harian) `[ref: narasi.txt, baris 89]`.
  * Catatan riwayat aktivitas (*Audit Trail*) mencatat siapa, melakukan apa, dan kapan `[ref: narasi.txt, baris 85]`.
  * Dukungan input data awal secara manual dari data lama Excel yang berserakan `[ref: narasi.txt, baris 70]`.
* **M.8. Modul Pembatalan, Retur & CRM**:
  * Alur retur barang rusak/salah cetak serta pembatalan transaksi (pengembalian DP) agar stok dan kas tetap sinkron `[ref: narasi.txt, baris 91]`.
  * Database Pelanggan (CRM): Pencatatan kontak nama/WA dan riwayat transaksi `[ref: narasi.txt, baris 92]`.
* **M.9. Skalabilitas Multi-Cabang (*Multi-Branch Ready*)**:
  * Penambahan pengenal ID unit/cabang di setiap tabel basis data transaksi, persediaan, aset, keuangan, dan SDM `[ref: narasi.txt, baris 97]`.

#### 4.1.2. Platform & Teknologi
* **Bahasa Pemrograman**: Python 3.14.2 ke atas (Wajib menerapkan paradigma *Functional Programming*, menghindari OOP kelas di alur bisnis utama) `[ref: narasi.txt, baris 104]`.
* **Sistem Database**: MySQL Server `[ref: narasi.txt, baris 104]`.
* **Pustaka Utama**: `mysql-connector-python`, `python-dotenv`, `bcrypt`, `pyjwt` `[ref: narasi.txt, baris 105]`.
* **Sistem Operasi**: Linux Debian 12 Bookworm dan Windows 11 `[ref: narasi.txt, baris 106]`.
* **Tipe Antarmuka**: Console / Command Line Interface (CLI) `[ref: narasi.txt, baris 103]`.

### 4.2. Di Luar Ruang Lingkup (Out-of-Scope)
* Pembangunan Antarmuka Grafis (GUI) berbasis Desktop maupun aplikasi Web (untuk fase awal proyek).
* Aplikasi Mobile (Android/iOS) untuk operasional atau pemantauan.
* Integrasi otomatis *Real-Time API* pihak ketiga dengan penyedia PPOB dan Agen Keuangan (pengelolaan saldo dan mutasi masih bersifat pencatatan manual atas tindakan fisik yang dilakukan).
* Integrasi langsung dengan API Payment Gateway pihak ketiga (seperti Midtrans/Xendit) untuk pembayaran non-tunai otomatis.
* Sinkronisasi otomatis dengan API WhatsApp Messenger (pemberitahuan atau pelacakan status pesanan masih dikelola internal sistem, belum otomatis mengirim pesan WA fisik ke pelanggan).
* Integrasi dengan API sistem inventaris pihak ketiga atau marketplace luar.

---

## 5. Deskripsi Produk / Deliverables

### 5.1. Produk Utama yang Dihasilkan
Sistem aplikasi konsol CLI Python terintegrasi yang terhubung ke database relasional MySQL lokal, dilengkapi dengan berkas konfigurasi sistem (.env), skrip inisialisasi tabel database (.sql), data awal dummy, serta modul fungsional yang siap pakai pada sistem operasi Linux Debian 12 dan Windows 11.

### 5.2. Daftar Deliverables per Fase SDLC
1. **Fase 1: Planning (Perencanaan)**
   * Berkas [Project Charter](file: docs/sdlc/01_planning/01_project_charter.md) (Dokumen ini)
2. **Fase 2: Requirements (Kebutuhan)**
   * Dokumen Spesifikasi Kebutuhan Perangkat Lunak / *Software Requirements Specification* (SRS)
3. **Fase 3: Design (Desain)**
   * Dokumen Arsitektur & Desain Basis Data / *System Design Document* (SDD) termasuk Diagram Entity-Relationship (ERD) dan skema basis data Multi-Branch.
4. **Fase 4: Implementation (Implementasi)**
   * Kode Sumber (*Source Code*) Python terstruktur menggunakan paradigma *Functional Programming*.
   * Berkas Inisialisasi Skema MySQL (`schema.sql`) dan skrip data awal dummy (`seed.sql`).
   * Konfigurasi berkas lingkungan runtime (`.env.example`).
5. **Fase 5: Testing (Pengujian)**
   * Dokumen Skenario & Rencana Pengujian (*Test Plan & Test Cases*).
   * Laporan Hasil Pengujian Penerimaan Pengguna (*User Acceptance Testing - UAT Report*).
6. **Fase 6: Deployment & Operational (Penerapan)**
   * Buku Panduan Instalasi Sistem (*Deployment & Technical Guide*).
   * Buku Panduan Pengguna CLI (*CLI User Manual*).

---

## 6. Stakeholder Proyek

### 6.1. Daftar Stakeholder
* **Pemilik Usaha AbuCom**: Sponsor Utama, Manajer Proyek (Junior Programmer), dan Pengguna Utama (Key User).
* **Calon Staf Karyawan (7 Posisi)**: Pengguna Operasional Harian Aplikasi (End-User).
* **Pelanggan AbuCom**: Pihak eksternal penerima manfaat layanan (Indirect Stakeholder).
* **Vendor & Supplier Bahan Baku / ATK**: Penyedia pasokan barang retail dan bahan cetak (Indirect Stakeholder).
* **Bank BRI & Bank Mandiri**: Institusi keuangan pemberi kredit modal usaha (Financial Stakeholder).
* **Kerabat & Keluarga (Sahabat/Teman/Orang Tua)**: Pemberi dana pinjaman tanpa bunga yang bersifat fleksibel (Financial Stakeholder).

### 6.2. Peran dan Tanggung Jawab (RACI Matrix)

| Aktivitas / Deliverables | Pemilik Usaha | Karyawan Staf | Tim Pengembang AI | Pihak Kreditur / Sahabat |
|--------------------------|:-------------:|:-------------:|:-----------------:|:------------------------:|
| Perencanaan & Project Charter | **A / R** | I | R | I |
| Spesifikasi Kebutuhan (SRS) | **A / R** | C | R | I |
| Desain Arsitektur & DB (SDD) | **A** | I | **R** | I |
| Implementasi Kode Program | **A / R** | I | **R** | I |
| Pengujian Fungsional & UAT | **A / R** | **R** | C | I |
| Instalasi & Input Data Excel | **A / R** | R | C | I |
| Operasional & Rekonsiliasi Harian | **A** | **R** | I | I |

* **R (Responsible)**: Pihak yang melakukan pekerjaan secara langsung untuk menyelesaikan tugas.
* **A (Accountable)**: Pihak yang memegang tanggung jawab penuh atas hasil akhir pekerjaan dan memiliki hak keputusan mutlak.
* **C (Consulted)**: Pihak yang dimintai masukan, pendapat, atau keahliannya sebelum pekerjaan diselesaikan.
* **I (Informed)**: Pihak yang diberi tahu mengenai perkembangan atau hasil akhir pekerjaan setelah selesai.

---

## 7. Tim Proyek dan Struktur Organisasi

### 7.1. Susunan Tim Pengembang
Proyek ini dikerjakan secara kolaboratif antara pemilik usaha sebagai programmer junior internal dan tim asisten AI spesialis `[ref: narasi.txt, baris 108-115]`:

| Anggota Tim | Peran Utama | Deskripsi Spesialisasi dan Tanggung Jawab |
|-------------|-------------|-------------------------------------------|
| **Anggota 0: Pemilik Usaha** | Junior Programmer | Menjadi pemilik kode utama, melakukan integrasi komponen, menguji fungsionalitas CLI secara langsung, melakukan *debugging* dasar, dan memberikan keputusan bisnis akhir. |
| **Anggota 1: Gemini 3.1 Pro (High)** | Lead Architect & Heavy Logic | Bertanggung jawab atas perancangan struktur arsitektur sistem yang modular, merancang logika komputasi yang berat (seperti algoritma BOM dimensi desimal dan penggajian otomatis cerdas). |
| **Anggota 2: Gemini 3.1 Pro (Low)** | Routine Coding & Documentation | Menangani penulisan kode-kode rutin, pembuatan dokumentasi formal SDLC (SRS, SDD, User Manual), dan pemetaan modul. |
| **Anggota 3: Gemini 3 Flash** | Fast Reviewer & Debugger | Melakukan tinjauan cepat terhadap perubahan kode, mengidentifikasi kesalahan sintaksis, dan melakukan perbaikan *bug* secara cepat dan ringan. |
| **Anggota 4: Claude Sonnet 4.6 (Thinking)** | Deep Coder & Refactoring Specialist | Fokus pada penulisan kode fungsional yang kompleks, mengoptimalkan kinerja aplikasi CLI, menyusun modul-modul kritis, dan melakukan refaktorisasi kode agar rapi dan efisien. |
| **Anggota 5: Claude Opus 4.6 (Thinking)** | System Strategist & Security Lead | Merancang strategi integritas data, merancang skema keamanan sistem (enkripsi sandi bcrypt, penanganan token JWT), audit trail, dan perlindungan privasi. |
| **Anggota 6: GPT-OSS 120B (Medium)** | Boilerplate Generator & Dummy Data Specialist | Menyediakan struktur kode awal (*boilerplate*), skrip pembuatan tabel basis data, dan menyusun data dummy/seed SQL yang realistis untuk kebutuhan pengujian. |

### 7.2. Pembagian Peran dan Tanggung Jawab Tim Staf (Operasional Pasca Go-Live)
Struktur organisasi operasional yang direncanakan oleh pemilik usaha untuk diakomodasi di dalam hak akses aplikasi `[ref: narasi.txt, baris 32-41]`:
1. **Kepala Percetakan**: Mengkoordinasikan seluruh operasional toko, mengawasi ketersediaan stok, memantau antrian pengerjaan, dan menerima laporan operasional harian.
2. **Staf Pramuniaga**: Melayani pelanggan di garda depan, mencatat data kontak pelanggan (CRM), mencantumkan spesifikasi pesanan, dan menginput data antrian transaksi.
3. **Staf Kasir**: Menangani transaksi pembayaran, mencatat uang muka (DP) dan pelunasan, serta melakukan rekonsiliasi kas laci fisik terhadap sistem setiap akhir hari kerja.
4. **Staf Desainer**: Mengakses antrian status `Proses Desain`, mendesain pesanan kustom, mengunggah arsip lokasi berkas desain pelanggan, dan mengubah status antrian menjadi `Produksi`.
5. **Staf Produksi Cetak**: Mengakses antrian status `Produksi`, melakukan eksekusi cetak fisik, mencatat jumlah pemakaian bahan baku riil & limbah produksi yang rusak/salah cetak, dan memperbarui status antrian ke `Selesai`.
6. **Staf Fotocopy & Print Dokumen**: Mengelola dan mencatat transaksi fotokopi cepat dan print dokumen harian serta membantu operasional produksi cetak jika terjadi antrian padat.
7. **Staf Gudang**: Mengelola keluar masuk bahan baku & barang retail ATK, mencatat data supplier, melakukan *Stock Opname* berkala, serta mencatat hutang pembelian barang supplier.

---

## 8. Kebutuhan Bisnis Tingkat Tinggi (High-Level Requirements)

### 8.1. Kebutuhan Fungsional Utama
Kebutuhan fungsional dikelompokkan secara logis berdasarkan divisi operasional yang diekstrak dari harapan pemilik usaha `[ref: narasi.txt, baris 74-98]`:

#### A. Manajemen Transaksi dan Kebijakan Harga (Sales & Pricing)
* **F-1.1**: Sistem harus mampu mencatat transaksi penjualan produk cetak kustom, penjualan barang retail ATK, penjualan pulsa/PPOB, transaksi jasa keuangan, serta jasa teknis secara terpisah namun terintegrasi dalam satu database.
* **F-1.2**: Sistem harus mendukung skema pembayaran fleksibel: pencatatan Uang Muka (DP) di awal dan Pelunasan di akhir saat pengambilan barang.
* **F-1.3**: Sistem harus mengelola multi-skema harga barang: Harga Retail (satuan), Harga Grosir (otomatis berubah berdasarkan batas minimum kuantitas pembelian), dan Harga Spesial Mitra.
* **F-1.4**: Sistem harus mampu mengelola alur transaksi pembatalan pesanan (termasuk pengembalian uang muka/DP) dan retur barang retail yang rusak/salah cetak dengan melakukan pengembalian stok & penyesuaian kas yang sinkron secara otomatis.

#### B. Manajemen Inventaris, BOM & Stock Opname (Inventory Control)
* **F-2.1**: Sistem harus mampu menghitung Harga Pokok Penjualan (HPP) secara dinamis dan otomatis berdasarkan komposisi bahan baku (*Bill of Materials* / BOM) untuk setiap jenis produk percetakan kustom.
* **F-2.2**: Sistem harus mendukung perhitungan pemakaian bahan baku lembaran atau cairan menggunakan satuan dimensi (panjang x lebar) atau volume desimal (presisi float) agar pengurangan stok bahan baku sesuai dengan ukuran riil pesanan.
* **F-2.3**: Sistem harus menyediakan fitur sinkronisasi pemakaian barang retail (ATK) yang diambil untuk kebutuhan internal produksi (mengurangi stok ATK dan memasukannya ke biaya operasional produksi).
* **F-2.4**: Sistem harus menyediakan menu pencatatan dan pelaporan data vendor/supplier, riwayat fluktuasi harga beli bahan baku dari supplier, serta pencatatan utang usaha atas pembelian barang tempo.
* **F-2.5**: Sistem harus memfasilitasi kegiatan *Stock Opname* berkala, mencatat selisih stok fisik vs stok sistem, dan menyimpan riwayat rekonsiliasi stok tersebut.

#### C. Layanan Keuangan Digital, PPOB, Jasa Keuangan & Jasa Teknis
* **F-3.1**: Sistem harus melacak saldo virtual PPOB pada dua akun terpisah (akun pulsa/data dan akun token/tagihan listrik) serta memberikan peringatan pengisian saldo (*alert*) jika saldo mendekati batas Rp 150.000 dengan target deposit minimal Rp 500.000.
* **F-3.2**: Sistem harus mencatat transaksi jasa keuangan (transfer & tarik tunai) dengan kemampuan memetakan biaya administrasi paling ekonomis berdasarkan 6 akun digital (Mandiri, Dana, Gopay, LinkAja, ShopeePay, OVO).
* **F-3.3**: Sistem harus mencatat transaksi penerimaan dan penyelesaian jasa service printer serta instalasi sistem operasi laptop/komputer.

#### D. Manajemen SDM, Penggajian & Poin Insentif Karyawan
* **F-4.1**: Sistem harus mencatat data profil karyawan, data kehadiran/absensi harian, dan riwayat penarikan kasbon (pinjaman karyawan).
* **F-4.2**: Sistem harus menghitung penggajian bulanan staf secara otomatis dengan skema cerdas: menggunakan Gaji Tetap Bulanan jika laba bersih usaha mencapai target yang ditentukan, atau menggunakan Gaji Persentase Laba Bersih jika target laba bulanan tidak tercapai.
* **F-4.3**: Sistem harus melakukan pemotongan gaji secara otomatis pada slip gaji bulanan karyawan jika karyawan tersebut memiliki sisa utang kasbon aktif.
* **F-4.4**: Sistem harus menghitung akumulasi poin insentif beban kerja karyawan per transaksi harian dengan ketentuan:
  * 1 Poin (Rp 500): Transaksi rutin/mudah (ATK, Pulsa, Transfer uang nominal kecil).
  * 3 Poin (Rp 1.500): Jasa dasar (Fotokopi, Print, Pengetikan, Transfer nominal besar).
  * 5 Poin (Rp 2.500): Produk kustom (Stempel flash, cetak foto, stiker, cetak nama dada).
  * 10 Poin (Rp 5.000): Pekerjaan berat/teknis (Cetak baliho, buku yasin, undangan pernikahan, service printer, install laptop).

#### E. Job Tracking, Arsip Desain & CRM (Operasional & Pelanggan)
* **F-5.1**: Sistem harus mengelola antrian pekerjaan (*Job Tracking*) dengan transisi status yang jelas: `Antri` -> `Proses Desain` -> `Produksi` -> `Selesai` -> `Diambil`.
* **F-5.2**: Sistem harus menyediakan fitur pencatatan lokasi fisik/digital dari arsip desain pelanggan (direktori penyimpanan berkas) untuk pencarian cepat cetak ulang di masa depan.
* **F-5.3**: Sistem harus mengelola database pelanggan (CRM) sederhana yang menyimpan nama, nomor WhatsApp, serta riwayat transaksi mereka.

#### F. Manajemen Keuangan Terpadu & Administrasi Pinjaman Modal
* **F-6.1**: Sistem harus mencatat secara transparan pinjaman modal tanpa bunga (riwayat siapa peminjam, waktu penarikan, pengembalian fleksibel, sisa saldo terutang).
* **F-6.2**: Sistem harus mencatat pinjaman modal bank berbunga (BRI dan Mandiri) yang meliputi riwayat setoran bulanan, sisa tenor (bulan), bunga, dan tanggal jatuh tempo bulanan.
* **F-6.3**: Sistem harus mencatat pengeluaran rutin operasional (air, listrik, internet), biaya tak terduga (kerusakan mesin, transport), pencatatan aset tetap usaha, dan tabungan khusus pengadaan alat baru di masa depan.
* **F-6.4**: Sistem harus mampu menyajikan laporan laba rugi usaha komprehensif harian, bulanan, dan tahunan yang dapat dianalisis per kategori layanan.
* **F-6.5**: Sistem harus memfasilitasi menu rekonsiliasi kas (pencocokan uang tunai fisik di laci kasir vs uang kas tercatat di sistem) di setiap akhir shift/hari kerja.

### 8.2. Kebutuhan Non-Fungsional Utama
* **N-2.1. Keamanan & Privasi Hak Akses**: Sistem harus membatasi akses melalui *Role-based Access Control* (RBAC). Menu administrasi modal pinjaman bank, tabungan alat, pengeluaran rutin besar, dan penggajian hanya dapat diakses oleh Pemilik (*Role: Pemilik*). Karyawan (*Role: Staf*) hanya diijinkan mengakses transaksi, antrian pekerjaan, stock opname, dan absensi harian.
* **N-2.2. Audit Trail**: Sistem wajib mencatat setiap aktivitas perubahan data sensitif (hapus transaksi, perubahan stok manual, persetujuan kasbon, retur) ke dalam tabel log audit (*Audit Trail*) yang mencatat: ID User, Waktu kejadian (Timestamp), Tipe Aksi, Tabel/Data yang diubah, dan Nilai sebelum/sesudah perubahan.
* **N-2.3. Keamanan Data Kredensial**: Sandi pengguna harus disimpan dalam basis data menggunakan enkripsi satu arah *bcrypt*. Verifikasi otentikasi session CLI menggunakan token berbasis *JSON Web Token* (JWT) yang aman.
* **N-2.4. Keandalan & Integritas Paradigma**: Seluruh fungsi logika bisnis di dalam aplikasi Python harus ditulis menggunakan paradigma *Functional Programming* murni (menggunakan fungsi murni tanpa *side-effects*, memanfaatkan imutabilitas, fungsi tingkat tinggi / *higher-order functions*, dan rekursi jika diperlukan) untuk memastikan keandalan, keterbacaan, dan kemudahan pengujian kode.
* **N-2.5. Portabilitas OS & Multi-Branch**: Aplikasi CLI Python harus dapat dijalankan dengan lancar tanpa ada perbedaan fungsionalitas di lingkungan terminal Linux Debian 12 Bookworm maupun Command Prompt/PowerShell Windows 11. Database dirancang agar siap menampung ID cabang yang fleksibel untuk ekspansi multi-cabang.
* **N-2.6. Kecepatan Respons**: Pembuatan laporan keuangan tahunan dan rekonsiliasi stok harus diproses dalam waktu kurang dari 5 detik pada spesifikasi hardware standar.

### 8.3. Rekomendasi Inovasi & Best Practice `[REKOMENDASI]`
Sesuai dengan **Mandat Inovasi & Best Practice** `[ref: narasi.txt, baris 98]`, tim pengembang AI merekomendasikan fitur tambahan berikut untuk diintegrasikan secara bertahap pada fase berikutnya:
* **N-3.1 [REKOMENDASI] Pembuatan Backup Data Otomatis berkala**: Sistem menyediakan fitur ekspor basis data otomatis ke format berkas SQL terkompresi (.zip/.tar.gz) secara berkala (harian atau mingguan) ke direktori lokal cadangan atau cloud penyimpanan untuk menghindari kehilangan data akibat kerusakan hardware.
* **N-3.2 [REKOMENDASI] Notifikasi Template WhatsApp Ready**: Karena aplikasi ini berbasis CLI dan tidak berintegrasi langsung dengan API WhatsApp berbayar, sistem menyediakan fitur *generate* link teks template WhatsApp (menggunakan format `https://wa.me/` dengan isi pesan otomatis seperti pemberitahuan DP diterima, pesanan selesai siap diambil, dll.) yang dapat disalin-tempel oleh staf ke WhatsApp Web secara manual dengan cepat.
* **N-3.3 [REKOMENDASI] Analisis Prediksi Re-Order Stok**: Sistem menganalisis rata-rata kecepatan pemakaian bahan baku (seperti kertas foto atau kertas undangan) dari riwayat transaksi bulanan dan memberikan notifikasi rekomendasi belanja stok kepada Staf Gudang 7 hari sebelum stok diperkirakan habis berdasarkan pola konsumsi usaha.

---

## 9. Asumsi dan Batasan (Assumptions & Constraints)

### 9.1. Asumsi
1. **Perekrutan Staf Berjalan Lancar**: Diasumsikan pemilik usaha dapat merekrut staf untuk mengisi 7 posisi struktur organisasi yang direncanakan tepat waktu sebelum atau bertepatan dengan masa penerapan (*Go-Live*) aplikasi.
2. **Ketersediaan Data Awal**: Pemilik usaha bersedia meluangkan waktu untuk melakukan migrasi dan input data manual pertama dari data Excel yang berserakan (data barang retail, bahan baku stempel, daftar supplier, dan riwayat sisa pinjaman) agar database awal bersih dan valid.
3. **Infrastruktur Jaringan & Listrik**: Toko fisik memiliki koneksi jaringan lokal stabil (LAN/WLAN) untuk menghubungkan komputer kasir/operasional CLI dengan komputer server database MySQL lokal, serta memiliki pasokan listrik yang stabil.
4. **Keamanan Fisik Perangkat**: Komputer yang digunakan di toko fisik aman secara fisik dan hanya dapat diakses oleh staf yang terdaftar.
5. **Kolaborasi Tim AI**: Tim pengembang AI yang ditunjuk dapat bekerja sama secara harmonis sesuai spesifikasi dan pembagian tanggung jawab masing-masing anggota tim.

### 9.2. Batasan
1. **Antarmuka Terbatas**: Aplikasi murni berbasis terminal/konsol teks CLI (Command Line Interface). Tidak ada tampilan grafis (GUI), halaman web interaktif, atau aplikasi mobile pada tahap awal pengembangan ini.
2. **Keterbatasan Paradigma Pemrograman**: Wajib menerapkan paradigma *Functional Programming* murni dalam kode program Python (tidak menggunakan class/OOP di alur bisnis utama). Batasan ini dapat meningkatkan kompleksitas penulisan kode untuk modul-modul yang biasanya lebih mudah ditulis dengan OOP (seperti state manajemen).
3. **Versi Runtime Kritis**: Aplikasi dikembangkan khusus untuk dijalankan pada Python versi minimal 3.14.2+ dengan database relasional MySQL Server.
4. **Akses Data Pihak Ketiga Bersifat Manual**: Transaksi keuangan digital (e-wallet Agen) dan transaksi pulsa/PPOB tidak terhubung dengan API perbankan/provider secara otomatis. Staf harus melakukan tindakan fisik terlebih dahulu (misal: transfer lewat HP Agen) lalu mencatatnya secara manual di aplikasi.
5. **Batasan Anggaran & Cabang Fisik**: Proyek ini dibiayai secara mandiri dari laba operasional dan pinjaman modal UMKM AbuCom, dengan penerapan tahap awal difokuskan hanya untuk 1 cabang fisik terlebih dahulu (meski skema basis data dirancang siap untuk multi-cabang).

### 9.3. Dependensi Proyek (Project Dependencies)
Keberhasilan implementasi proyek ini bergantung pada beberapa faktor eksternal dan ketergantungan sistem berikut:
1. **Keandalan Akses Saldo & Akun Pihak Ketiga**: Aplikasi ini bergantung pada ketersediaan operasional fisik dan saldo pada akun PPOB serta 6 e-wallet (Agen Mandiri, Dana, Gopay, LinkAja, ShopeePay, OVO). Ketidaktersediaan saldo atau akun yang terblokir akan menghentikan transaksi di divisi jasa keuangan.
2. **Ketersediaan & Stabilitas Listrik & Koneksi Lokal**: Karena database MySQL dijalankan di server lokal, aplikasi bergantung pada pasokan listrik toko (UPS sebagai cadangan) dan kestabilan jaringan LAN/WiFi lokal untuk menghubungkan klien CLI ke database server.
3. **Kompatibilitas Runtime Python**: Ketergantungan pada runtime Python versi minimal 3.14.2+ beserta pustaka pendukung (`mysql-connector-python`, `bcrypt`, `pyjwt`). Jika sistem operasi Windows atau Linux tidak terinstal versi Python yang sesuai, aplikasi tidak dapat dijalankan.
4. **Kualitas Migrasi Data Awal**: Ketergantungan pada ketepatan dan kebersihan data awal yang diimpor dari Excel manual. Jika data awal yang disediakan pemilik tidak akurat, sistem baru akan menghasilkan laporan stok dan HPP yang salah sejak awal (*garbage in, garbage out*).

### 9.4. Metodologi Pengembangan Proyek
Proyek ini akan dikembangkan menggunakan **Pendekatan Hybrid (Waterfall & Agile)** untuk mengoptimalkan kualitas perencanaan dan fleksibilitas pengerjaan kode:
*   **Fase Perencanaan & Desain (Waterfall)**: Digunakan pada Fase 1 hingga Fase 3 (Project Charter, SRS, SDD, dan ERD). Setiap dokumen harus disetujui secara formal oleh Pemilik Usaha sebelum fase berikutnya dimulai. Hal ini penting untuk memastikan batasan ruang lingkup yang rigid dan arsitektur database multi-branch yang solid.
*   **Fase Implementasi & Pengujian (Agile / Iteratif)**: Digunakan pada Fase 4 dan Fase 5. Pengerjaan kode sumber Python akan dibagi ke dalam sprint 2 mingguan. Setiap akhir sprint, tim pengembang AI akan menyajikan modul CLI yang siap uji kepada Junior Programmer (Pemilik) untuk mendapatkan umpan balik cepat dan perbaikan bug segera.
*   **Fase Penerapan & Go-Live (Waterfall)**: Migrasi data awal, pelatihan staf selama 3 hari, dan go-live sistem akan dilakukan secara terstruktur sesuai prosedur panduan instalasi.

---

## 10. Risiko Awal (Initial Risks)

Berikut adalah identifikasi risiko awal proyek, probabilitas kejadian (1 = Rendah, 5 = Tinggi), dampak terhadap keberhasilan proyek (1 = Rendah, 5 = Tinggi), serta rencana mitigasi awal:

| No | Risiko | Probabilitas | Dampak | Rencana Mitigasi Awal |
|----|--------|:------------:|:------:|-----------------------|
| 1  | **Single Point of Failure (Burnout Pemilik)**: Pemilik sakit atau kelelahan ekstrim sebelum aplikasi selesai dikembangkan, menghambat proses klarifikasi kebutuhan bisnis riil. | 3 | 5 | Mengoptimalkan pengerjaan oleh tim pengembang AI berdasarkan dokumentasi rinci yang telah dibuat, serta merencanakan sesi ulasan berkala yang singkat namun padat bersama pemilik usaha. |
| 2  | **Ketidakakuratan Migrasi Data Excel**: Data stok dan keuangan lama yang berserakan di berbagai file Excel tidak valid, rusak, atau memiliki duplikasi yang tinggi saat dimasukkan manual. | 4 | 4 | Membuat skrip validasi data input di aplikasi CLI untuk menyaring data kosong, format salah, atau data duplikat sebelum disimpan ke database MySQL. |
| 3  | **Penarikan Dana Mendadak pada Pinjaman Tanpa Bunga**: Rekan atau keluarga menarik dana pinjaman tanpa bunga secara mendadak saat proyek sedang berjalan, mengganggu arus kas operasional usaha. | 3 | 4 | Merancang sistem pencatatan tabungan khusus dan dana cadangan darurat terpisah dalam modul keuangan untuk memastikan biaya pengembangan dan operasional kritis tetap terjamin. |
| 4  | **Kerumitan Paradigma Functional Programming**: Kesulitan dalam mengelola status aplikasi yang dinamis (state management) tanpa paradigma OOP, berpotensi menunda jadwal pengerjaan. | 2 | 4 | Memanfaatkan pustaka internal Python seperti *functools*, *operator*, dan fungsi-fungsi generator, serta menugaskan Claude Sonnet 4.6 secara intensif untuk melakukan refaktorisasi kode yang rumit agar tetap bersih dan fungsional. |
| 5  | **Kecurangan Karyawan (Fraud) pada Saldo Digital**: Karyawan melakukan manipulasi penginputan transaksi kas atau transfer saldo digital secara ilegal di luar otorisasi sistem. | 3 | 5 | Mengaktifkan modul *Audit Trail* yang sangat ketat untuk setiap aksi perubahan data sensitif, mengunci akses menu administrasi keuangan sensitif hanya untuk pemilik usaha, dan melakukan pencocokan kas fisik (*Cash Reconciliation*) harian. |
| 6  | **Ketidaksesuaian Karyawan Baru**: Staf baru yang direkrut tidak memiliki literasi komputer yang cukup untuk mengoperasikan aplikasi berbasis CLI dengan lancar. | 3 | 3 | Menyusun berkas *CLI User Manual* yang sangat sederhana, interaktif, dan mudah dibaca, serta mengadakan pelatihan simulasi sistem CLI selama 3 hari sebelum staf dilepas mengoperasikan aplikasi sendiri. |

---

## 11. Milestone dan Jadwal Tingkat Tinggi

Berikut adalah draf milestone tingkat tinggi untuk jangka waktu pengerjaan 12 bulan:

| No | Fase Proyek / Milestone Utama | Perkiraan Target Selesai | Status | Keterangan |
|----|-------------------------------|--------------------------|:------:|------------|
| 1  | **Inisiasi & Perencanaan**: Penyusunan dan Persetujuan Project Charter | `Bulan 1` | Selesai | Menyetujui visi, ruang lingkup, dan pondasi SDLC (v1.1). |
| 2  | **Analisis Kebutuhan**: Penyusunan dokumen SRS (Software Requirements Specification) | `Bulan 2` | `[ ]` | Menguraikan 20+ fitur detail secara fungsional. |
| 3  | **Desain Sistem & DB**: Penyusunan dokumen SDD (System Design Document) & ERD Skema Multi-Branch | `Bulan 3 - 4` | `[ ]` | Merancang relasi tabel basis data MySQL & struktur logika. |
| 4  | **Implementasi - Fase I**: Boilerplate DB, Sistem Otorisasi JWT, Keamanan, & Modul CRM / Transaksi Dasar | `Bulan 5 - 6` | `[ ]` | Fondasi dasar program CLI & enkripsi password. |
| 5  | **Implementasi - Fase II**: Modul Inventaris presisi, BOM desimal, Kasbon/SDM, & Manajemen Antrian | `Bulan 7 - 9` | `[ ]` | Integrasi perhitungan logistik & perhitungan penggajian cerdas. |
| 6  | **Implementasi - Fase III**: Modul Keuangan Terpadu, Laba/Rugi Divisi, Administrasi Pinjaman & Aset | `Bulan 10` | `[ ]` | Integrasi laporan profitabilitas & audit trail. |
| 7  | **Integrasi & Pengujian**: Pelaksanaan Skenario Uji (Test Plan) & User Acceptance Testing (UAT) | `Bulan 11` | `[ ]` | Pengujian fungsionalitas menyeluruh dan simulasi bug. |
| 8  | **Penerapan & Pelatihan (Go-Live)**: Migrasi data awal Excel, Pelatihan staf, & Penyerahan User Manual | `Bulan 12` | `[ ]` | Sistem resmi berjalan penuh menggantikan Excel manual. |

---

## 12. Estimasi Anggaran Tingkat Tinggi (High-Level Budget)

Estimasi anggaran pengembangan ini disusun berdasarkan analisis kebutuhan infrastruktur fisik toko, server database lokal, dan operasional awal untuk UMKM percetakan skala menengah di Indonesia. Seluruh alokasi pengerjaan software dialokasikan secara efisien dengan memanfaatkan kolaborasi tim pengembang AI eksternal dan pemilik usaha sebagai *programmer* internal.

Berikut adalah rincian estimasi komponen biaya proyek AbuCom yang realistis:

| No | Komponen Biaya | Estimasi (Rp) | Keterangan |
|---|----------------|---------------|------------|
| 1 | **Perangkat Keras (Hardware)**: Pengadaan Mini PC Server lokal (Core i5, 16GB RAM, SSD 512GB), 1 PC Kasir/Operasional tambahan, dan 2 unit UPS penstabil daya. | Rp 15.500.000 | Infrastruktur fisik server & PC kasir di toko |
| 2 | **Infrastruktur Jaringan**: Pengadaan Router MikroTik, Switch Hub 8-Port, kabel UTP Cat6, konektor RJ45, serta jasa instalasi kabel jaringan lokal. | Rp 2.500.000 | Konektivitas data klien CLI ke server database |
| 3 | **Biaya Pengembangan Perangkat Lunak**: Alokasi resource tim AI (token API premium Claude/Gemini/OpenAI) dan kompensasi waktu internal Junior Programmer. | Rp 15.000.000 | Implementasi modul fungsional & skema keamanan |
| 4 | **Pelatihan & Operasional Awal**: Pencetakan Buku Panduan User Manual CLI, penyediaan konsumsi simulasi sistem selama masa pelatihan staf 3 hari. | Rp 2.500.000 | Pelatihan 7 staf baru sebelum sistem berjalan penuh |
| 5 | **Dana Cadangan Darurat (Contingency Fund)**: Alokasi dana tak terduga untuk menangani kendala teknis darurat atau kenaikan harga hardware. | Rp 4.500.000 | Penanganan risiko teknis selama pengerjaan |
| **Total** | **Estimasi Anggaran Proyek** | **Rp 40.000.000** | **Total anggaran investasi sistem terpadu** |

### Asumsi Estimasi Anggaran:
1. **Pemanfaatan Perangkat Sedia Ada**: Toko fisik sudah memiliki minimal 1 unit PC operasional yang layak dan 1 printer laser untuk operasional dasar, sehingga biaya pengadaan PC hanya mencakup PC tambahan untuk kasir dan server mini terdedikasi.
2. **Tanpa Biaya Lisensi OS Berbayar**: Server basis data menggunakan OS Linux Ubuntu/Debian Server (Open Source/Gratis) dan sistem basis data menggunakan MySQL Community Server (Gratis), sehingga meminimalkan biaya software pihak ketiga.
3. **Biaya Jaringan Sekali Bayar**: Biaya instalasi jaringan lokal bersifat investasi satu kali (*one-time capital expenditure*) dengan menggunakan kabel fisik untuk kestabilan transfer data.
4. **Biaya Token API Bersifat Fleksibel**: Alokasi Rp 15.000.000 sudah mencakup cadangan token API yang cukup untuk eksplorasi arsitektur kompleks oleh model AI berpikir dalam (deep reasoning model) selama siklus 12 bulan.

---

## 13. Kriteria Keberhasilan Proyek (Success Criteria)

Proyek pembangunan sistem manajemen terpadu AbuCom ini dinyatakan sukses apabila memenuhi kriteria terukur (*Definition of Done*) yang objektif berikut:

1. **Otomatisasi Laporan Finansial (100% Bebas Excel)**:
   * **Indikator**: 100% laporan laba/rugi, pengeluaran rutin, tabungan aset, dan rekonsiliasi kas dihasilkan secara real-time langsung melalui terminal CLI.
   * **Metode Uji**: Verifikasi biner (Ya/Tidak) bahwa tidak ada data transaksi harian yang perlu disalin ulang secara manual ke Microsoft Excel untuk menyusun laporan laba/rugi bulanan.
2. **Akurasi Sinkronisasi Stok Bahan Baku (< 1.0% Selisih)**:
   * **Indikator**: Selisih antara jumlah stok bahan baku di gudang fisik dengan stok yang tercatat di sistem pada saat *Stock Opname* berkala di bawah 1.0%.
   * **Metode Uji**: `(Jumlah Selisih Stok Fisik / Total Stok Sistem) * 100% <= 1.0%` yang diuji setelah berjalan 1 bulan operasional penuh menggunakan BOM dimensi/volume desimal.
3. **Efisiensi Antrian Produksi (Zero-Missed Orders)**:
   * **Indikator**: 0 pesanan pelanggan yang terlewat, terlambat, atau tidak dikerjakan akibat kelalaian staf operasional.
   * **Metode Uji**: Verifikasi log data antrian pada akhir bulan menunjukkan status transisi dari `Antri` hingga `Diambil` selesai 100% untuk semua ID pesanan terdaftar.
4. **Integritas & Keamanan Hak Akses (100% Terjaga)**:
   * **Indikator**: Staf non-otoritas sama sekali tidak dapat mengakses menu keuangan sensitif, pinjaman modal, tabungan, dan penggajian karyawan.
   * **Metode Uji**: Pengujian penetrasi internal (UAT) menunjukkan 100% percobaan akses ilegal oleh *role* Staf ke menu khusus Pemilik berhasil ditolak sistem dengan pesan error otorisasi yang sesuai.
5. **Mitigasi Burnout Pemilik Usaha**:
   * **Indikator**: Pemilik usaha berhasil mendelegasikan 100% aktivitas transaksi kas, desain, produksi, dan gudang kepada staf yang direkrut, serta melacak kehadiran dan gaji mereka secara otomatis melalui aplikasi.
   * **Metode Uji**: Pemilik hanya perlu masuk ke sistem minimal 1 kali seminggu untuk memantau laporan laba/rugi dan menyetujui payroll, sementara operasional harian berjalan mandiri tanpa intervensi fisik pemilik.

---

## 14. Persetujuan dan Otorisasi (Approval)

Dokumen Project Charter ini diajukan dan disetujui sebagai acuan dasar yang mengikat untuk pengerjaan seluruh siklus SDLC berikutnya. Persetujuan ini menyatakan bahwa visi, ruang lingkup, anggaran, dan batasan yang tertera di dalam dokumen ini telah divalidasi dan disepakati bersama.

| Pihak Penandatangan | Jabatan / Peran | Tanda Tangan | Tanggal Persetujuan |
|---------------------|-----------------|--------------|---------------------|
| **Pemilik Usaha AbuCom** | Inisiator, Sponsor Proyek & Junior Programmer | *(Disetujui secara Digital)* | 2026-05-21 |
| **Pemilik Usaha AbuCom** | Manajer Proyek & Penanggung Jawab Internal | *(Disetujui secara Digital)* | 2026-05-21 |

---

## 15. Referensi Dokumen

| # | Nama File | Lokasi Fisik / Path Relatif | Keterangan |
|---|---|---|---|
| 1 | `narasi.txt` | [narasi.txt](file: docs/sdlc/narasi.txt) | Dokumen primer narasi kebutuhan bisnis, operasional, teknis, dan keuangan yang ditulis langsung oleh pemilik usaha AbuCom. |
| 2 | `0002_issue_validasi_project_charter.md` | [0002_issue_validasi_project_charter.md](file: docs/issue/0002_issue_validasi_project_charter.md) | Dokumen instruksi validasi, analisis, dan penyempurnaan Project Charter untuk meningkatkan kualitas standar industri. |

---

## Glosarium Istilah Domain Percetakan & Bisnis (Glossary)

Berikut adalah glosarium penjelasan singkat istilah teknis industri percetakan, retail, dan finansial yang digunakan di dalam dokumen ini untuk menyamakan persepsi seluruh pembaca teknis:
1. **Stempel Flash**: Jenis stempel otomatis tanpa bantalan tinta eksternal, yang menggunakan karet khusus penyerap tinta warna yang disinari lampu kilat (flash) mesin stempel saat pembuatan.
2. **Baliho**: Media promosi cetak luar ruangan (outdoor) berskala besar, biasanya dicetak di atas bahan flexi menggunakan mesin printer format lebar (*wide-format printer*).
3. **Nama Dada**: Papan nama kecil (pin/tag name) yang biasanya dipasang di dada pakaian karyawan/pegawai, terbuat dari bahan akrilik, PVC, atau logam kuningan dengan lapisan resin bening.
4. **Buku Yasin**: Buku berisi surat Yasin dan tahlil yang dicetak khusus secara kustom untuk acara peringatan kematian, biasanya dilengkapi sampul tebal (*hardcover*) hiasan emas.
5. **Map Snelhechter**: Jenis map kertas atau plastik yang dilengkapi dengan pengikat jepitan logam di bagian tengahnya untuk menjepit dokumen kertas yang telah dilubangi.
6. **PPOB (Payment Point Online Bank)**: Layanan loket pembayaran tagihan online yang bekerja sama dengan perbankan, seperti pembelian pulsa, paket data, token listrik PLN, pembayaran tagihan air, internet, dan TV kabel.
7. **Jasa Transfer & Tarik Tunai Agen**: Layanan keuangan retail yang diselenggarakan oleh agen bank resmi (seperti Agen BRILink atau Agen Mandiri) untuk memfasilitasi transfer uang antar bank dan penarikan tunai secara instan menggunakan mesin EDC atau aplikasi mobile bank dengan komisi admin tertentu.
8. **Bill of Materials (BOM)**: Daftar komprehensif bahan baku, komponen, dan kuantitas yang dibutuhkan untuk memproduksi satu unit produk akhir (dalam percetakan: daftar bahan stempel, tinta, kertas, pelapis untuk memproduksi satu stempel flash).
9. **Stock Opname**: Proses penghitungan fisik persediaan barang/bahan baku di gudang secara langsung untuk kemudian dicocokkan dengan catatan stok yang ada pada sistem/aplikasi guna menemukan dan menyesuaikan selisih.
10. **Audit Trail**: Berkas catatan log historis yang merekam urutan aktivitas sistem secara kronologis, berguna sebagai bukti penelusuran tindakan keamanan jika terjadi perubahan data sensitif.
11. **Kasbon**: Skema pinjaman uang tunai di muka yang diberikan perusahaan/pemilik kepada karyawan, yang pengembaliannya dipotong langsung secara otomatis dari gaji bulanan karyawan bersangkutan.
12. **Uang Muka / DP (Down Payment)**: Pembayaran sebagian dari total harga transaksi yang diserahkan pelanggan di awal sebagai tanda jadi pesanan sebelum proses produksi dimulai.
13. **Retur**: Proses pengembalian barang yang telah dibeli oleh pelanggan atau barang yang dibeli dari supplier karena alasan cacat produksi, rusak, atau tidak sesuai spesifikasi pesanan.
14. **Functional Programming (Pemrograman Fungsional)**: Paradigma pemrograman yang memperlakukan komputasi sebagai evaluasi fungsi matematika dan menghindari perubahan status (*state*) serta data yang dapat dimutasi (*mutable data*).
