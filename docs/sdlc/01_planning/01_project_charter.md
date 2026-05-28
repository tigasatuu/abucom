---
dokumen    : Project Charter
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.2
tanggal    : 2026-05-28
status     : Validated
penyusun   : Principal Business Analyst & Senior Technical PM
---

# Project Charter — AbuCom

## Riwayat Perubahan Dokumen

| Versi | Tanggal    | Perubahan                                                   | Oleh                                            |
|-------|------------|-------------------------------------------------------------|-------------------------------------------------|
| 1.0   | 2026-05-20 | Pembuatan awal dokumen berdasarkan analisis `narasi.txt`    | Senior Project Manager / Lead Business Analyst  |
| 1.1   | 2026-05-21 | Penyempurnaan menyeluruh berdasarkan validasi. Melengkapi estimasi anggaran, menambahkan modul limbah produksi & manajemen satuan, detail alur kerja manual, metodologi pengembangan, manfaat terukur, dependensi, dan eliminasi placeholder. | Principal Business Analyst & Senior Technical PM |
| 1.2   | 2026-05-28 | Validasi menyeluruh : Melengkapi integrasi data dari dokumen Feasibility Study, Stakeholder Register, Tech Stack Decision, dan Innovation Proposal. Mengisi placeholder, melengkapi Glosarium, menambahkan Risk Score, dan standarisasi bahasa dokumen sesuai standar industri. | Principal Business Analyst & Senior Technical PM |

---

## 1. Informasi Umum Proyek

### 1.1. Nama Proyek
**AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**  
*(Aplikasi manajemen internal terintegrasi untuk otomatisasi operasional percetakan, retail ATK, layanan digital/PPOB, jasa keuangan, dan jasa teknis).*

### 1.2. Deskripsi Singkat Proyek
Proyek ini bertujuan untuk merancang dan membangun sistem aplikasi manajemen terpadu berbasis *Command Line Interface* (CLI) untuk mengotomatisasi seluruh kegiatan operasional harian pada usaha UMKM AbuCom. Sistem ini dirancang menggunakan bahasa pemrograman Python versi minimal 3.14.2+ dengan paradigma *Functional Programming* murni dan didukung oleh sistem basis data relasional MySQL (versi 8.0/8.4 LTS). Aplikasi ini akan mengintegrasikan manajemen transaksi penjualan, manajemen inventaris barang baku dan retail dengan metode *Bill of Materials* (BOM) presisi desimal, pencatatan limbah produksi, manajemen keuangan terpadu (laba/rugi, pengeluaran rutin, tabungan aset, administrasi pinjaman modal), sistem *job tracking* antrian produksi, manajemen SDM dan penggajian cerdas, serta arsip desain pelanggan. Sistem ini juga dirancang dengan arsitektur yang siap dikembangkan untuk kebutuhan multi-cabang (*Multi-Branch Ready*).

### 1.3. Sponsor / Pemilik Proyek
* **Nama**: Pemilik Usaha UMKM Percetakan AbuCom  
* **Peran**: Inisiator Proyek, Pemilik Bisnis, Penyedia Pendanaan (Sponsor), dan Pengguna Utama (*Key User*).

### 1.4. Manajer Proyek / Penanggung Jawab
**Pemilik Usaha AbuCom (bertindak sebagai Junior Programmer dan Manajer Proyek Internal)**  
*(Bertanggung jawab atas koordinasi internal proyek, integrasi fungsional CLI, pengujian langsung, serta penyelarasan keputusan bisnis).*

### 1.5. Tanggal Mulai Proyek
`2026-05-20` (Tanggal inisiasi proyek berdasarkan pembuatan issue).

### 1.6. Perkiraan Tanggal Selesai
`2027-05-20`  
*(Berdasarkan arahan pemilik proyek untuk draf awal, estimasi jangka waktu keseluruhan pengerjaan proyek direncanakan berlangsung selama **12 bulan**).*

### 1.7. Versi Dokumen
**Versi 1.2** (Diperbarui dan disempurnakan berdasarkan validasi formal komprehensif seluruh referensi SDLC awal).

---

## 2. Latar Belakang dan Justifikasi Proyek

### 2.1. Kondisi Saat Ini (Current State)
Usaha UMKM AbuCom merupakan penyedia layanan jasa percetakan dan beberapa unit usaha pendukung yang berlokasi di satu tempat fisik. Saat ini, seluruh operasional usaha dikelola dan dijalankan secara mandiri oleh pemilik usaha *(single-fighter)*.  

Usaha ini melayani lima kategori produk dan layanan utama yang kompleks:
1. **Produk Percetakan (Produksi Sendiri)**: Stempel flash, cetak foto, pembuatan buku yasin, undangan pernikahan, cetak baliho, fotokopi, pengetikan dokumen, print data, cetak stiker, hingga pembuatan nama dada dan jasa percetakan kustom.
2. **Alat Tulis Kantor / ATK (Retail)**: Penjualan barang retail fisik seperti kertas HVS, kertas foto, kertas undangan, tinta printer, pulpen, hekter, berbagai map (snelhechter, biasa, warna), lakban, selotip, pensil, dan perlengkapan kantor.
3. **Layanan Digital & PPOB**: Penjualan pulsa HP, pulsa listrik (token), paket data, dan pembayaran tagihan listrik bulanan.
4. **Jasa Keuangan**: Layanan transfer uang antar bank dan jasa tarik tunai.
5. **Jasa Teknis & Service**: Layanan perbaikan (service) printer serta instalasi ulang sistem operasi pada komputer dan laptop pelanggan.

Seluruh pencatatan transaksi keuangan, pelacakan sisa stok bahan baku, mutasi akun digital, pembayaran pinjaman modal, dan rekapitulasi data masih dikerjakan secara manual oleh pemilik menggunakan Microsoft Excel dengan file yang berserakan dan tidak terintegrasi. Berikut adalah gambaran alur kerja manual per divisi saat ini:
*   **Divisi Percetakan (Produk Unggulan)**: Pemilik melayani pelanggan, mendesain pesanan kustom, mengambil bahan baku fisik di gudang, melakukan cetak dan *finishing* (pemotongan, laminasi, dll), mengemas hasil cetak, hingga menyerahkannya ke pelanggan. Setelah itu, pemilik mencatat transaksi di Excel, menghitung sisa stok bahan secara manual, memantau ketersediaan bahan, membuat daftar belanja pengadaan jika stok menipis, melakukan pembelian fisik ke supplier, dan menginput kembali bahan yang baru dibeli ke dalam database stok.
*   **Divisi ATK (Retail)**: Pemilik melayani pembeli langsung, memeriksa daftar harga di lembar kerja Excel, menjumlahkan total belanjaan, memberikan kembalian, dan secara manual mengurangi stok di Excel satu per satu. Pemilik juga harus melakukan pemeriksaan fisik berkala di gudang, merapikan pajangan, serta merencanakan pengadaan barang yang habis dengan menentukan harga jual baru berdasarkan harga beli terupdate dari supplier.
*   **Divisi Pulsa dan PPOB**: Mengelola dua akun saldo deposit terpisah (akun pulsa/data dan akun token/tagihan listrik). Pemilik harus memastikan saldo tidak habis secara fisik, melakukan deposit minimal Rp 500.000 jika saldo mendekati batas kritis Rp 150.000, serta mencatat setiap transaksi penjualan ke dalam Excel secara manual demi pelaporan keuangan.
*   **Divisi Jasa Keuangan**: Pemilik mengelola transaksi transfer dan tarik tunai menggunakan 6 akun uang elektronik/perbankan digital (Agen Bank Mandiri, Dana, Gopay, LinkAja, ShopeePay, OVO). Alur kerjanya adalah pemilik harus memilih akun dengan biaya administrasi termurah bagi pelanggan sesuai jenis layanan, menjaga keseimbangan saldo di setiap akun berdasarkan keramaian (*traffic*), dan mencatat manual setiap mutasi saldo di Excel.
*   **Divisi Jasa Teknis & Service**: Menerima printer rusak atau laptop/komputer pelanggan yang ingin diinstal ulang. Pemilik melakukan perbaikan fisik, melakukan pengetesan, menyerahkan kembali ke pelanggan, menerima pembayaran, dan mencatatnya ke dalam file Excel transaksi harian.
*   **Administrasi Pinjaman, SDM & Pengeluaran**:
    *   *Pinjaman Tanpa Bunga*: Pemilik mencatat secara manual siapa peminjamnya (sahabat, keluarga, orang tua), nominal yang ditarik/dikembalikan, dan sisa saldo terutang agar pencatatan tetap transparan mengingat penarikan dana bisa terjadi secara mendadak.
    *   *Pinjaman Bank*: Pemilik melacak jadwal setoran bulanan, bunga, sisa tenor, dan tanggal jatuh tempo Bank BRI dan Bank Mandiri pada catatan Excel agar terhindar dari denda keterlambatan.
    *   *Administrasi SDM & Pengeluaran*: Pemilik mengelola pengeluaran rutin bulanan (air, listrik, internet), biaya tidak terduga, daftar aset fisik (printer, PC, CCTV), serta merencanakan pencatatan kasbon karyawan secara manual.

### 2.2. Permasalahan Utama (Problem Statement)
Kompleksitas pengelolaan lima divisi usaha yang berjalan bersamaan secara manual menyebabkan pemilik usaha mengalami stres berat, keletihan mental (*burnout*), dan kewalahan secara fisik. Pemilik harus membagi fokus antara melayani pelanggan langsung di toko, mengeksekusi produksi cetak, mengambil bahan baku, melakukan pembukuan keuangan, memantau stok, hingga merespons cepat order pelanggan melalui WhatsApp. Data Excel yang tidak sinkron membuat pemantauan sisa bahan baku di gudang tidak akurat, laporan laba rugi bulanan sulit dipastikan, dan terdapat risiko tinggi adanya transaksi atau pesanan pelanggan yang terlewat.

### 2.3. Dampak Jika Tidak Ditangani
Jika kondisi ini terus berlanjut tanpa adanya otomatisasi sistem:
* **Penurunan Kualitas Layanan**: Respons terhadap pelanggan melambat, pesanan terancam terlewat atau salah cetak, yang berujung pada hilangnya kepercayaan pelanggan.
* **Kerugian Finansial & Kebocoran Kas**: Kesalahan pencatatan kas/bank, selisih stok bahan baku yang rusak/hilang tanpa tercatat (limbah produksi tidak terukur), serta denda keterlambatan pembayaran pinjaman bank akibat lupa jatuh tempo.
* **Kegagalan Ekspansi Organisasi**: Rencana rekrutmen karyawan baru guna meringankan beban pemilik terancam gagal atau tidak terkendali karena belum tersedianya sistem absensi, sistem poin kinerja, dan manajemen kasbon/gaji yang terstruktur.
* **Masalah Kesehatan Pemilik**: *Burnout* berkepanjangan dapat mengganggu kesehatan pemilik, yang berpotensi menghentikan operasional usaha sepenuhnya mengingat posisi pemilik sebagai *single point of failure*.

### 2.4. Justifikasi Kelayakan Proyek
Berdasarkan hasil dokumen *Feasibility Study*, proyek otomasi ini dinyatakan **Layak (Go) dengan Catatan**. Proyek ini diproyeksikan memiliki tingkat pengembalian investasi (ROI) sebesar **26%**, **Net Present Value (NPV) Rp 47.471.075**, dan periode pengembalian modal (*Payback Period*) sekitar **9,5 bulan**. Manfaat strategis dalam mengeliminasi burnout pemilik dan mencegah kebocoran kas menjadikan proyek ini mutlak diperlukan bagi keberlangsungan AbuCom.

---

## 3. Tujuan Proyek (Project Objectives)

### 3.1. Tujuan Umum
Merancang, membangun, dan menerapkan sistem aplikasi manajemen operasional dan keuangan terpadu berbasis CLI (*Command Line Interface*) yang modular, aman, dan berkinerja tinggi guna mengotomatisasi seluruh alur bisnis AbuCom, meniadakan ketergantungan pada pencatatan Excel manual yang berserakan, serta menyajikan laporan stok dan keuangan yang akurat secara real-time demi mendukung fokus pemilik pada pengembangan strategis usaha.

### 3.2. Tujuan Spesifik (SMART Goals)
* **S.1 (Otomatisasi Inventaris & Komposisi HPP)**: Mengurangi selisih antara stok barang fisik di gudang dengan catatan sistem hingga kurang dari 1.0% melalui fitur sinkronisasi otomatis menggunakan Bill of Materials (BOM) berdasarkan dimensi panjang x lebar atau volume secara presisi dalam 6 bulan pertama implementasi.
* **S.2 (Keuangan Instan & Laba/Rugi Divisi)**: Menyajikan laporan keuangan laba/rugi, pengeluaran rutin, dan tabungan aset secara instan (waktu pemrosesan < 5 detik) untuk memudahkan analisis profitabilitas per divisi layanan pada setiap akhir bulan.
* **S.3 (Manajemen Antrian & Zero-Missed Orders)**: Mencapai tingkat operasional *zero-missed orders* (0 pesanan pelanggan terlewat) sejak hari pertama Go-Live melalui penerapan sistem pelacakan status pesanan (*job tracking*) digital dengan lima tahapan status terintegrasi.
* **S.4 (Manajemen SDM & Penggajian Fleksibel)**: Memastikan kesiapan operasional modul rekrutmen 7 posisi staf baru dengan absensi terintegrasi, penggajian cerdas, dan manajemen kasbon otomatis sebelum operasional penuh bulan ke-12.
* **S.5 (Arsitektur Multi-Cabang)**: Merancang database MySQL yang memiliki kesiapan 100% untuk menampung data multi-cabang (*Multi-Branch Ready*), sehingga siap digunakan untuk ekspansi cabang baru tanpa perlu merombak ulang skema data inti di masa depan.

### 3.3. Manfaat Bisnis yang Terukur (Measurable Business Benefits)
Penerapan sistem aplikasi AbuCom ini ditargetkan memberikan manfaat bisnis nyata yang dapat diukur secara kuantitatif:
1. **Reduksi Waktu Pembukuan**: Mengurangi waktu rekapitulasi transaksi harian dan penyusunan laporan keuangan laba/rugi per divisi dari rata-rata **2-3 jam per hari** menjadi **instan (< 5 detik)** secara otomatis setelah transaksi selesai.
2. **Efisiensi Inventaris & Pencegahan Kerugian**: Menurunkan kerugian akibat bahan baku rusak atau tidak tercatat (limbah produksi) sebesar **15%** per tahun melalui fitur pelacakan limbah produksi yang tersinkronisasi.
3. **Penyelamatan Transaksi Terlewat**: Menghilangkan insiden pesanan yang terlewat atau lupa dikerjakan hingga **0% (*Zero-Missed Orders*)** menggunakan modul *Job Tracking* digital yang interaktif.
4. **Skalabilitas Operasional**: Membuka jalan bagi pemilik usaha untuk mendelegasikan **90%** operasional teknis harian kepada 7 staf baru tanpa khawatir terjadi kecurangan saldo atau kebocoran data keuangan sensitif berkat sistem RBAC dan log *Audit Trail* yang ketat.

---

## 4. Ruang Lingkup Proyek (Project Scope)

### 4.1. Dalam Ruang Lingkup (In-Scope)

#### 4.1.1. Modul / Fitur Utama
* **M.1. Modul Manajemen Transaksi & Kebijakan Harga**:
  * Mendukung pembayaran bertahap: Uang Muka (DP) dan Pelunasan saat barang diambil.
  * Mengelola multi-skema harga dinamis: harga retail, harga grosir (berdasarkan kuantitas), dan harga spesial untuk mitra bisnis.
* **M.2. Modul Manajemen Inventaris, BOM & Stock Opname**:
  * Pencatatan data supplier/vendor, riwayat harga beli barang, dan manajemen utang pembelian barang.
  * Sistem Harga Pokok Penjualan (HPP) otomatis menggunakan komposisi bahan baku (*Bill of Materials* / BOM) multi-bahan untuk produk kustom.
  * Perhitungan pemakaian bahan lembaran/cairan berdasarkan satuan dimensi (panjang x lebar) atau volume desimal presisi (*float*) agar pengurangan stok bahan baku akurat sesuai ukuran riil pesanan.
  * **Pencatatan Limbah Produksi (*Waste Management*)**: Fitur khusus untuk mencatat bahan baku yang rusak atau salah cetak selama proses produksi, sehingga stok gudang dan aplikasi tetap sinkron dan biaya limbah dapat dianalisis.
  * **Manajemen Satuan & Atribut Barang (*Unit of Measure*)**: Dukungan pengelolaan berbagai jenis satuan ukur (rim, lembar, pcs, mililiter, gram, dimensi panjang x lebar) dan spesifikasi teknis unik untuk setiap kategori barang, dengan dukungan pencatatan stok desimal presisi untuk sisa bahan baku.
  * Fitur sinkronisasi barang retail (ATK) yang diambil untuk kebutuhan internal produksi (otomatis mengurangi stok ATK retail dan menambah biaya operasional produksi).
  * Fitur rekonsiliasi stok (*Stock Opname*) berkala untuk mencocokkan stok fisik terhadap sistem serta menyimpan riwayat selisihnya.
* **M.3. Modul Layanan Keuangan Digital, PPOB, Jasa Keuangan & Service**:
  * Rekonsiliasi saldo akun digital PPOB (minimal deposit Rp 500.000 jika saldo < Rp 150.000).
  * Pencatatan transaksi transfer uang dan tarik tunai dengan kemampuan memetakan akun biaya administrasi paling ekonomis.
  * Pencatatan transaksi service printer dan install laptop/komputer.
* **M.4. Modul Manajemen SDM, Penggajian & Poin Karyawan**:
  * Manajemen data karyawan, absensi harian, dan pencatatan riwayat kasbon karyawan dengan fitur potong gaji otomatis.
  * Penggajian otomatis cerdas (Gaji Tetap jika target laba bersih tercapai, atau Gaji Persentase Laba jika target tidak tercapai).
  * Sistem Poin Karyawan (Insentif): transaksi rutin (1 poin/Rp 500), jasa dasar (3 poin/Rp 1.500), produk kustom (5 poin/Rp 2.500), dan pekerjaan teknis/berat (10 poin/Rp 5.000).
* **M.5. Modul Sistem Manajemen Antrian & Pelacakan Desain**:
  * Pelacakan status pesanan (*Job Tracking*) dengan 5 status: `Antri` -> `Proses Desain` -> `Produksi` -> `Selesai` -> `Diambil`.
  * Arsip Desain Pelanggan: Pencatatan metadata path direktori lokasi penyimpanan file desain pelanggan di server.
* **M.6. Modul Administrasi Pinjaman, Aset, & Pengeluaran Rutin**:
  * Pencatatan pinjaman tanpa bunga kerabat/keluarga (transparansi penarikan fleksibel, sisa saldo terutang).
  * Pencatatan pinjaman bank berbunga (setoran bulanan, tenor, jatuh tempo Mandiri dan BRI).
  * Manajemen aset tetap, depresiasi, pengeluaran operasional rutin, biaya tak terduga, dan tabungan khusus pengadaan alat baru di masa depan.
* **M.7. Modul Keamanan, Audit Trail & Hak Akses**:
  * Pembatasan hak akses (*Role-Based Access Control*): Menu khusus "Pemilik" (keuangan sensitif, tabungan, pinjaman, payroll) dan menu "Karyawan" (hanya terkait operasional harian).
  * Catatan riwayat aktivitas (*Audit Trail* format JSON) mencatat siapa, melakukan apa, nilai sebelum dan nilai sesudah perubahan, serta kapan.
  * Dukungan import data awal secara manual dari data lama Excel yang berserakan.
* **M.8. Modul Pembatalan, Retur & CRM**:
  * Alur retur barang rusak/salah cetak serta pembatalan transaksi (termasuk pengembalian DP) agar stok dan kas tetap sinkron otomatis.
  * Database Pelanggan (CRM): Pencatatan kontak nama/WhatsApp dan riwayat transaksi pelanggan.
* **M.9. Skalabilitas Multi-Cabang (*Multi-Branch Ready*)**:
  * Penambahan pengenal kolom `cabang_id` di setiap tabel basis data transaksi, persediaan, aset, keuangan, dan SDM.

#### 4.1.2. Platform & Teknologi
* **Bahasa Pemrograman**: Python versi minimal 3.14.2+ (Wajib menerapkan paradigma *Functional Programming* murni, larangan keras menggunakan konsep *Object-Oriented Programming* / OOP di alur bisnis utama).
* **Sistem Database**: MySQL Server versi 8.0/8.4 LTS lokal.
* **Pustaka Utama**: `mysql-connector-python`, `python-dotenv`, `bcrypt`, `pyjwt`, `rich`, `tabulate`.
* **Sistem Operasi Target**: Berjalan sebagai klien-server lokal pada Linux Debian 12 Bookworm (Server) dan Windows 11 (Klien).
* **Tipe Antarmuka**: Murni *Command Line Interface* (CLI) berbasis teks konsol interaktif.

### 4.2. Di Luar Ruang Lingkup (Out-of-Scope)
* **Aplikasi Web / GUI**: Pembuatan antarmuka pengguna berbasis Grafis (GUI desktop) maupun halaman aplikasi Web secara eksplisit tidak disertakan pada tahap ini.
* **Aplikasi Mobile**: Pengembangan aplikasi Android/iOS untuk operasional atau pemantauan secara eksplisit tidak disertakan.
* **Integrasi API Real-Time Eksternal**: Sistem tidak terhubung langsung melalui API pihak ketiga dengan penyedia PPOB, *payment gateway* (Midtrans/Xendit), atau perbankan otomatis. Seluruh transaksi saldo bersifat pencatatan manual atas tindakan fisik operasional.
* **API WhatsApp Gateway**: Sistem tidak terhubung dengan WhatsApp API berbayar untuk mengirim pesan ke pelanggan secara otomatis.
* **Integrasi Marketplace Eksternal**: Sistem tidak dihubungkan untuk sinkronisasi pesanan dari e-commerce/marketplace eksternal (Tokopedia, Shopee, dsb).
* **Laporan Pajak Otomatis**: Integrasi dan perhitungan otomatis pelaporan pajak penghasilan negara (e-Faktur/DJP) tidak disertakan.
* **Dukungan Multi-Bahasa**: Sistem hanya menggunakan antarmuka Bahasa Indonesia, tanpa fitur pelokalan (*localization*) bahasa asing.

---

## 5. Deskripsi Produk / Deliverables

### 5.1. Produk Utama yang Dihasilkan
Sistem aplikasi konsol CLI Python terintegrasi yang terhubung ke database relasional MySQL lokal, dilengkapi dengan berkas konfigurasi sistem (`.env`), skrip inisialisasi struktur tabel database (`schema.sql`), data awal (*seed data* dummy `seed.sql`), serta modul fungsional yang siap pakai pada sistem operasi Linux Debian 12 dan Windows 11.

### 5.2. Daftar Deliverables per Fase SDLC
1. **Fase 1: Planning (Perencanaan)**
   * Berkas [Project Charter](docs/sdlc/01_planning/01_project_charter.md) (Dokumen ini)
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
* **Pemilik Usaha AbuCom**: Sponsor Utama, Manajer Proyek (Junior Programmer), dan Pengguna Utama (*Key User*).
* **Calon Staf Karyawan (7 Posisi)**: Pengguna Operasional Harian Aplikasi (*End-User*).
* **Pelanggan AbuCom**: Pihak eksternal penerima manfaat layanan (*Indirect Stakeholder / Beneficiary*).
* **Vendor & Supplier Bahan Baku / ATK**: Penyedia pasokan barang retail dan bahan cetak (*Indirect Stakeholder / Supply Chain*).
* **Bank BRI & Bank Mandiri**: Institusi perbankan pemberi kredit modal usaha berbunga (*Financial Stakeholder*).
* **Kerabat & Keluarga (Sahabat/Orang Tua)**: Pemberi dana pinjaman tanpa bunga yang bersifat fleksibel (*Financial Stakeholder*).
* **Tim Pengembang AI (6 Model Spesialis)**: Arsitek, pengembang perangkat lunak, dan spesialis teknis proyek.

### 6.2. Peran dan Tanggung Jawab (RACI Matrix)

| Aktivitas / Deliverables | Pemilik Usaha | Staf Karyawan | Tim Pengembang AI | Pihak Kreditur / Sahabat |
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
Proyek ini dikerjakan secara kolaboratif antara pemilik usaha sebagai programmer junior internal dan tim asisten AI spesialis:

| Anggota Tim | Peran Utama | Deskripsi Spesialisasi dan Tanggung Jawab |
|-------------|-------------|-------------------------------------------|
| **Anggota 0: Pemilik Usaha** | Junior Programmer | Menjadi pemilik kode utama, melakukan integrasi komponen fungsional, dan menguji langsung kapabilitas aplikasi. |
| **Anggota 1: Gemini 3.1 Pro (High)** | Lead Architect & Heavy Logic | Bertanggung jawab merancang arsitektur sistem modular dan fungsi komputasi berat (algoritma BOM dan penggajian cerdas). |
| **Anggota 2: Gemini 3.1 Pro (Low)** | Routine Coding & Documentation | Menyusun dokumentasi SDLC, pemetaan modul, dan menulis kode rutin. |
| **Anggota 3: Gemini 3 Flash** | Fast Reviewer & Debugger | Melakukan tinjauan kode yang efisien, menemukan *error runtime*, dan perbaikan bug ringan secara cepat. |
| **Anggota 4: Claude Sonnet 4.6 (Thinking)** | Deep Coder & Refactoring Specialist | Membangun skrip Python murni yang efisien, mengoptimalkan interaksi CLI, serta melakukan refaktorisasi kompleksitas tinggi. |
| **Anggota 5: Claude Opus 4.6 (Thinking)** | System Strategist & Security Lead | Mengamankan integritas arsitektur, menyiapkan fungsi JWT, bcrypt, rancangan *Audit Trail*, dan perlindungan kerahasiaan data (UU PDP). |
| **Anggota 6: GPT-OSS 120B (Medium)** | Boilerplate Generator & Dummy Data Specialist | Menghasilkan kode boilerplate SQL dan menyiapkan data seed sampel transaksi. |

### 7.2. Pembagian Peran dan Tanggung Jawab Tim Staf (Operasional Pasca Go-Live)
Struktur organisasi operasional yang direncanakan oleh pemilik usaha untuk diakomodasi di dalam hak akses aplikasi:
1. **Kepala Percetakan**: Mengkoordinasikan operasional toko, mengawasi ketersediaan stok, memantau antrean, dan memvalidasi absen.
2. **Staf Pramuniaga**: Melayani pelanggan garda depan, mencatat data kontak (CRM), dan menginput pesanan ke sistem antrean (`Antri`).
3. **Staf Kasir**: Menangani transaksi uang tunai, mencatat Uang Muka (DP) dan pelunasan, serta melakukan rekonsiliasi kas laci harian.
4. **Staf Desainer**: Mengakses antrean pesanan desain, mengerjakan file kustom, mencatat path arsip desain, dan merubah status ke `Produksi`.
5. **Staf Produksi Cetak**: Mengakses pekerjaan berstatus `Produksi`, melakukan cetak riil, mencatat sisa bahan/limbah cetak, dan merubah ke `Selesai`.
6. **Staf Fotocopy & Print Dokumen**: Mengurus transaksi jasa cetak kilat secara kasual serta berfungsi fleksibel membantu produksi jika sangat ramai.
7. **Staf Gudang**: Menerima/mengeluarkan barang, mencatat profil vendor, utang usaha, serta bertanggung jawab terhadap audit stok fisik (*Stock Opname*).

---

## 8. Kebutuhan Bisnis Tingkat Tinggi (High-Level Requirements)

### 8.1. Kebutuhan Fungsional Utama
Kebutuhan fungsional dikelompokkan secara logis berdasarkan divisi operasional yang diekstrak dari harapan pemilik usaha:

#### A. Manajemen Transaksi dan Kebijakan Harga (Sales & Pricing)
* **F-1.1**: Sistem wajib mencatat transaksi penjualan produk cetak kustom, penjualan barang retail ATK, penjualan pulsa/PPOB, transaksi jasa keuangan, serta jasa teknis secara terpisah namun terintegrasi dalam satu database.
* **F-1.2**: Sistem wajib mendukung skema pembayaran bertahap: pencatatan penerimaan Uang Muka (DP) di awal dan penyelesaian Pelunasan di akhir saat pengambilan barang.
* **F-1.3**: Sistem wajib mengelola skema harga multi-tingkat secara otomatis: Harga Retail, Harga Grosir (kuantitas volume), dan Harga Mitra khusus.
* **F-1.4**: Sistem wajib memfasilitasi transaksi pembatalan pesanan dan alur retur barang rusak dengan dukungan penyesuaian (*rollback*) otomatis terhadap stok barang dan kas finansial.

#### B. Manajemen Inventaris, BOM & Stock Opname (Inventory Control)
* **F-2.1**: Sistem wajib menghitung Harga Pokok Penjualan (HPP) produk kustom menggunakan pendekatan otomatis dari definisi bahan multikomponen (*Bill of Materials* / BOM).
* **F-2.2**: Sistem wajib menyediakan kalkulasi pengurangan stok bahan baku menggunakan presisi data tipe desimal (*float*) dengan dukungan ukuran dimensi panjang dikalikan lebar, maupun volume cair.
* **F-2.3**: Sistem wajib mendukung sinkronisasi otomatis konversi item ritel ATK untuk dipergunakan internal toko (mengurangi jumlah item dijual dan menambah ke beban operasional cetak).
* **F-2.4**: Sistem wajib memberikan menu pencatatan profil setiap vendor, melacak riwayat harga pembelian untuk tren, serta mencatat status utang tempo jatuh waktu atas faktur pembelian.
* **F-2.5**: Sistem wajib menyediakan mekanisme dokumentasi perbandingan fisik berkala melalui modul rekonsiliasi (*Stock Opname*) beserta persetujuan laporan selisihnya.

#### C. Layanan Keuangan Digital, PPOB, Jasa Keuangan & Jasa Teknis
* **F-3.1**: Sistem wajib melacak sisa saldo secara terpisah pada akun pulsa/data dan token PLN, disertai pemberitahuan visual jika mencapai ambang Rp 150.000 dengan ketentuan log deposit Rp 500.000.
* **F-3.2**: Sistem wajib memberikan rekomendasi transaksi bagi agen keuangan berdasarkan kalkulasi biaya administrasi terendah di antara 6 e-wallet utama (Agen Bank Mandiri, Dana, Gopay, LinkAja, ShopeePay, OVO).
* **F-3.3**: Sistem wajib menyediakan log pelacakan barang servis printer atau laptop untuk mengetahui perbaikan yang sedang berjalan dan mencatat biaya layanan perbaikannya.

#### D. Manajemen SDM, Penggajian & Poin Insentif Karyawan
* **F-4.1**: Sistem wajib merekam basis data seluruh karyawan operasional, buku absensi/kehadiran, serta batas plafon kredit maksimum utang kasbon.
* **F-4.2**: Sistem wajib menghitung pengeluaran gaji karyawan dengan logika otomatis Gaji Tetap (kondisi laba sesuai target yang ditentukan) atau Persentase Laba (kondisi operasional di bawah target).
* **F-4.3**: Sistem wajib mengeksekusi integrasi potong gaji pada laporan penggajian akhir bulan karyawan yang masih memegang nilai utang sisa kasbon berjalan.
* **F-4.4**: Sistem wajib memberikan apresiasi penilaian performa poin per penyelesaian transaksi: 1 poin untuk pekerjaan ringan hingga 10 poin untuk beban pekerjaan kompleks teknis tinggi.

#### E. Job Tracking, Arsip Desain & CRM (Operasional & Pelanggan)
* **F-5.1**: Sistem wajib memfasilitasi pelacakan papan pekerjaan terpusat menggunakan status: `Antri`, `Proses Desain`, `Produksi`, `Selesai`, dan `Diambil`.
* **F-5.2**: Sistem wajib menyediakan indeks pencarian path folder lokal dokumen file desain cetak setiap klien agar memudahkan *re-order*.
* **F-5.3**: Sistem wajib membuat tabel CRM kontak pelanggan berdasarkan nama dan nomor ponsel yang berhubungan dengan histori invoice mereka.

#### F. Manajemen Keuangan Terpadu & Administrasi Pinjaman Modal
* **F-6.1**: Sistem wajib mencatat mutasi pinjaman lunak tanpa bunga dari kolega keluarga, meliputi saldo akhir yang ditarik, pengembalian bebas waktu, serta utang tersisa.
* **F-6.2**: Sistem wajib memiliki jadwal pemantauan pelunasan tenor untuk entitas komersial (Bank Mandiri dan Bank BRI) meliputi komponen cicilan pokok dan beban bunga.
* **F-6.3**: Sistem wajib mencatat pemisahan beban pengeluaran utilitas rutin, dana perawatan, pencatatan penyusutan aset inventaris besar, serta dana tabungan hardware secara disiplin.
* **F-6.4**: Sistem wajib menyajikan rincian perbandingan beban HPP melawan pendapatan penjualan total secara *real-time* menjadi laporan komprehensif Laba/Rugi.
* **F-6.5**: Sistem wajib mewajibkan pelaporan rekonsiliasi dana fisik dalam kotak laci uang pada saat giliran kasir usai dan mencatat apabila ada kelebihan/kekurangan saldo harian.

### 8.2. Kebutuhan Non-Fungsional Utama
* **N-2.1. Keamanan & Privasi Hak Akses**: Sistem wajib membatasi fungsionalitas menggunakan kerangka *Role-Based Access Control* (RBAC) ketat. Transaksi rahasia (laba bersih, pinjaman modal, aset tabungan, gaji) hanya berhak dibuka oleh `Role: Pemilik`. Modul lainnya (stok kasir dan rekap harian) didistribusikan untuk `Role: Staf`.
* **N-2.2. Audit Trail Terstruktur JSON**: Sistem wajib memelihara rekaman forensik jejak mutasi penghapusan data, pengubahan stok ilegal, dan retur menggunakan format JSON komprehensif (User ID, waktu aksi, `old_value`, dan `new_value`).
* **N-2.3. Keamanan Kriptografi Kredensial**: Seluruh sandi pengguna wajib dilindungi melalui enkripsi menggunakan algoritma *bcrypt* (*cost factor 12*). Sesi otentikasi login wajib menggunakan token *JSON Web Token* (JWT) tanpa keadaan (*stateless*) beralgoritma HS256 kedaluwarsa 8 jam.
* **N-2.4. Integritas Paradigma Functional Programming**: Sistem wajib menggunakan penerapan kaidah murni dan ketat fungsional Python; semua model bisnis logika bebas *side-effects*, memanfaatkan imutabilitas, dan melarang penggunaan perancangan objek/kelas di alur transaksi.
* **N-2.5. Portabilitas OS & Multi-Branch**: Aplikasi CLI Python wajib dieksekusi identik bebas dependensi antar Windows 11 di sisi klien dan Debian 12 pada level server (LAN). Struktur relasional MySQL dirancang memuat `cabang_id` guna fasilitasi skalabilitas vertikal antar unit toko.
* **N-2.6. Kecepatan Respons**: Rendering modul laporan Laporan Laba Rugi akhir bulan dan pengambilan tabel stok desimal masif wajib diselesaikan secara performa tinggi kurang dari 5 detik.

### 8.3. Rekomendasi Inovasi & Best Practice `[REKOMENDASI]`
Sesuai dengan **Mandat Inovasi & Best Practice**, tim pengembang AI merekomendasikan fitur tambahan inovatif berikut untuk diintegrasikan secara proaktif pada fase pengembangan berikutnya:
* **N-3.1 [REKOMENDASI] Pembuatan Backup Data Otomatis Berkala (AES-256)**: Sistem wajib menyediakan skrip pencadangan arsip basis data MySQL otomatis harian (.zip/.tar.gz) terenkripsi AES-256 bit untuk mematuhi UU PDP No. 27 Tahun 2022.
* **N-3.2 [REKOMENDASI] Notifikasi Template WhatsApp Ready**: Sistem direkomendasikan memiliki fitur memproduksi tautan teks parameter (*generate link* `https://wa.me/`) otomatis berisi tagihan/pelunasan untuk disalin-tempel oleh staf kasir.
* **N-3.3 [REKOMENDASI] Analisis Prediksi Re-Order Stok**: Sistem direkomendasikan mengimplementasikan logika analisa fungsional memprediksi perkiraan sisa daya tahan bahan baku berlandaskan histori belanja, memberikan peringatan visual pemesanan vendor 7 hari sebelum habis.
* **N-3.4 [REKOMENDASI] Dashboard Ringkasan Harian CLI**: Menambahkan layar selamat datang visual CLI interaktif khusus `Role: Pemilik` berisikan omzet harian ringkas, profitabilitas kotor, dan jumlah pesanan menunggu.
* **N-3.5 [REKOMENDASI] Fitur Riwayat Harga Beli Supplier (Price Tracking)**: Menambahkan modul referensi historis bagi gudang dalam menentukan penyedia grosir harga terendah.
* **N-3.6 [REKOMENDASI] Sistem Notifikasi Jatuh Tempo Utang Otomatis**: Menyediakan peringatan terminal pengingat tenggat waktu pembayaran H-3 terhadap cicilan komersial perbankan dan piutang supplier grosir.
* **N-3.7 [REKOMENDASI] Log Aktivitas Shift Karyawan (Shift Handover Log)**: Fitur pelimpahan pertanggungjawaban dana uang antara giliran kerja pagi vs sore untuk staf operasional.
* **N-3.8 [REKOMENDASI] Fitur Pencatatan Margin Keuntungan per Produk**: Metrik profitabilitas harga dikurangi HPP untuk menganalisis dan menyeleksi produk jasa cetak terlaris toko.
* **N-3.9 [REKOMENDASI] Sistem Peringatan Anomali Transaksi (Fraud Detection Sederhana)**: Algoritma peringatan deteksi pembatalan invoice berulang-ulang dari entitas kasir berpotensi kecurangan *fraud* kas.
* **N-3.10 [REKOMENDASI] Template Laporan Cetak Teks untuk Arsip Fisik**: Penyesuaian layout output teks kolom tabel harian agar dicetak menggunakan printer *thermal receipt* lokal 58/80mm toko.
* **N-3.11 [REKOMENDASI] Fitur Import Data CSV Semiautomatis**: Skrip otomatisasi validasi tipe baris ekspor Excel awal milik Pemilik agar go-live inisiasi proyek minim *human-error*.
* **N-3.12 [REKOMENDASI] Sistem Konfigurasi Dinamis Tanpa Hardcode (Runtime Config)**: Pemisahan parameter nilai profit persentase payroll, batas kasbon karyawan, dll ke tabel `system_configs` terdedikasi.

---

## 9. Asumsi dan Batasan (Assumptions & Constraints)

### 9.1. Asumsi
1. **Perekrutan Staf Berjalan Lancar**: Diasumsikan pemilik usaha dapat merekrut staf untuk mengisi 7 posisi struktur organisasi yang direncanakan tepat waktu sebelum atau bertepatan dengan masa penerapan (*Go-Live*) aplikasi.
2. **Ketersediaan Data Awal**: Pemilik usaha bersedia meluangkan waktu untuk melakukan migrasi dan input data manual pertama dari data Excel yang berserakan (data barang retail, bahan baku stempel, daftar supplier, dan riwayat sisa pinjaman) agar database awal bersih dan valid.
3. **Infrastruktur Jaringan & Listrik**: Toko fisik memiliki koneksi jaringan lokal stabil (LAN/WLAN) untuk menghubungkan komputer kasir/operasional CLI dengan komputer server database MySQL lokal, serta memiliki pasokan listrik yang stabil.
4. **Keamanan Fisik Perangkat**: Komputer yang digunakan di toko fisik aman secara fisik dan hanya dapat diakses oleh staf yang terdaftar (kepatuhan regulasi perlindungan data pribadi hukum setempat).
5. **Kolaborasi Tim AI**: Tim pengembang AI yang ditunjuk dapat bekerja sama secara harmonis sesuai spesifikasi dan pembagian tanggung jawab teknologi masing-masing anggota tim.

### 9.2. Batasan
1. **Antarmuka Terbatas**: Aplikasi murni berbasis terminal/konsol teks CLI (*Command Line Interface*). Tidak ada tampilan grafis (GUI), halaman web interaktif, atau aplikasi mobile pada tahap awal pengembangan ini.
2. **Keterbatasan Paradigma Pemrograman**: Wajib menerapkan paradigma *Functional Programming* murni dalam kode program Python (tidak menggunakan class/OOP di alur bisnis utama). Batasan ini dapat meningkatkan kompleksitas penulisan kode untuk modul-modul manajemen *state*.
3. **Versi Runtime Kritis**: Aplikasi dikembangkan secara ketat khusus dijalankan pada Python versi minimal 3.14.2+ dengan database relasional MySQL versi 8.0/8.4 LTS lokal.
4. **Akses Data Pihak Ketiga Bersifat Manual**: Transaksi keuangan digital (e-wallet Agen) dan transaksi pulsa/PPOB tidak terhubung dengan API perbankan/provider secara otomatis real-time. Staf wajib melakukan tindakan fisik layanan di ponsel terlebih dahulu lalu mencatat keberhasilan prosesnya secara manual.
5. **Batasan Anggaran & Cabang Fisik**: Proyek ini dibiayai secara mandiri dari laba operasional (Rp 40.000.000 estimasi), implementasi difokuskan instalasi hardware hanya untuk 1 cabang fisik terlebih dahulu.

### 9.3. Dependensi Proyek (Project Dependencies)
Keberhasilan implementasi proyek ini bergantung pada beberapa faktor eksternal dan ketergantungan sistem berikut:
1. **Keandalan Akses Saldo & Akun Pihak Ketiga**: Aplikasi ini sangat bergantung pada ketersediaan operasional fisik dan saldo akun pada penyedia pulsa PPOB serta kelancaran jaringan 6 aplikasi pembayaran e-wallet.
2. **Ketersediaan & Stabilitas Listrik & Koneksi Lokal**: Aplikasi bergantung mutlak pada pasokan listrik toko untuk Mini PC Server (UPS dibutuhkan secara mutlak) dan perangkat *Switch Hub* jaringan karena basis data di-hosting dalam satu tempat fisik tanpa failover server cloud (arsitektur LAN lokal).
3. **Kompatibilitas Runtime Python**: Ketergantungan instalasi lingkungan OS Linux Debian 12 serta OS Windows 11 dengan pustaka *driver* esensial (`mysql-connector-python`, `bcrypt`, `pyjwt`, `rich`, `tabulate`).
4. **Kualitas Migrasi Data Awal**: Proses *setup* inisial dipengaruhi oleh kebersihan integritas data dari catatan pembukuan Excel masa lampau (*garbage in, garbage out*).

### 9.4. Metodologi Pengembangan Proyek
Proyek ini akan dikembangkan menggunakan **Pendekatan Hybrid (Waterfall & Agile)** untuk mengoptimalkan kualitas perencanaan dokumentasi dan kecepatan rilis kode perangkat lunak:
*   **Fase Perencanaan & Desain (Waterfall)**: Digabungkan pada penyelesaian iterasi Fase 1 hingga Fase 3 secara rigid. Seluruh Dokumen Business Case, dokumen SRS, serta SDD wajib direview serta divalidasi tandatangan formal (*formal sign-off*) karena mendikte kerangka tulang punggung sistem fungsional dan model keamanan RBAC/JWT.
*   **Fase Implementasi & Pengujian (Agile / Iteratif)**: Diterapkan pada Fase 4 dan 5 dalam rentang sprint berkala selama **2 mingguan**. Sub-tim model berpikir dalam *Claude* dan AI *Gemini* akan merilis cuplikan menu CLI dan mendemonstrasikannya ke *Junior Programmer* demi menerima validasi umpan balik kilat, evaluasi logika desimal, serta koreksi bug asinkron. Manajeman perubahan (*change management*) ditangani dengan prioritas backlog sprint bulanan.
*   **Fase Penerapan & Go-Live (Waterfall)**: Rencana penyebaran dilakukan sesuai langkah pengawalan *deployment*, instalasi server Debian, pelatihan fisik tatap muka 3 hari operasional, serta importase skrip database CSV manual.

---

## 10. Risiko Awal (Initial Risk Register)

Berikut adalah identifikasi risiko awal proyek, Probabilitas kejadian (1 = Rendah, 5 = Tinggi), Dampak proyek (1 = Rendah, 5 = Tinggi), Risk Score (Probabilitas × Dampak), serta rencana mitigasi yang konkret:

| No | Risk ID | Risiko | Probabilitas | Dampak | Risk Score | Rencana Mitigasi Awal |
|----|---------|--------|:------------:|:------:|:----------:|-----------------------|
| 1  | RSK-01 | **Single Point of Failure (Burnout Pemilik)**: Pemilik usaha sakit ekstrim sebelum aplikasi dirilis, menunda pengujian dan persetujuan. | 3 | 5 | **15** | Tim AI akan mematuhi spesifikasi desain mendetail yang telah disepakati untuk menghindari re-desain ulang serta menerapkan rapat ulasan singkat mingguan dengan pemilik untuk menghindari kelelahan tambahan. |
| 2  | RSK-02 | **Kerusakan Data MySQL Fisik (Power Failure)**: Mini PC Server Linux mati mendadak saat transaksi berlangsung, menyebabkan korupsi data *InnoDB* parsial. | 3 | 5 | **15** | Wajib melakukan investasi perangkat penyetabil daya 2 unit UPS, implementasi query berbasis ACID (START TRANSACTION, COMMIT, ROLLBACK) di semua operasi, serta penjadwalan *backup* database .sql terenkripsi harian di malam hari. |
| 3  | RSK-03 | **Tantangan Kurva Pembelajaran Paradigma FP Python**: Keterlambatan sprint coding di bulan ke-7 karena pengelola kode Junior Programmer bingung membaca modifikasi kode murni, rekursi, dan closure. | 2 | 4 | **8** | Menugaskan spesialis refaktorisasi Claude Sonnet 4.6 menyertakan dokumentasi penulisan sintaks komprehensif serta membangun *wrapper* pola fungsi untuk mengurangi *boilerplate*. |
| 4  | RSK-04 | **Penarikan Dana Mendadak pada Pinjaman Kerabat**: Rekan/keluarga menarik tabungan tanpa bunga secara tiba-tiba dalam jumlah masif, menghentikan pembelian komponen PC proyek. | 3 | 4 | **12** | Menyediakan anggaran alokasi *Contingency Fund* sebesar Rp 4.500.000, diamankan pada tabungan perbankan terpisah dan tidak diputar di sirkulasi arus kas belanja bahan baku percetakan. |
| 5  | RSK-05 | **Kebocoran Fraud Internal Karyawan Kasir**: Manipulasi staf di jam ramai pelayanan operasional melalui *refund* barang atau klaim kehilangan secara sengaja. | 3 | 5 | **15** | Menegakkan RBAC otorisasi ketat di semua layer antarmuka, mengeksekusi pendataan rekaman nilai pada tabel JSON `audit_logs` di backend secara senyap untuk deteksi pelacakan. |
| 6  | RSK-06 | **Kesulitan Adopsi Antarmuka CLI Teks Staf Baru**: Kelambatan pencatatan pelayanan kasir antrean depan oleh pramuniaga yang gagap beradaptasi dengan navigasi non-mouse (*keyboard hotkeys*). | 3 | 3 | **9** | Membangun visual panel interaktif pewarnaan kontras CLI, menyediakan *User Manual* format infografik navigasi pendek, dan mensyaratkan 3 hari percobaan simulasi kasir *sandbox*. |
| 7  | RSK-07 | **Kebocoran Data Kredensial & Privasi (UU PDP)**: Peretasan/Pencurian file *database dump* atau akses direktori aset server Mini PC. | 2 | 5 | **10** | Mewajibkan seluruh arsip backup dikunci algoritma *AES-256*, enkripsi autentikasi login menggunakan algoritma *bcrypt* ber-Cost 12, dan pembatasan izin (*chmod 700*) Linux *root user* server. |
| 8  | RSK-08 | **Migrasi File Excel Awal Yang Tidak Akurat**: Duplikasi entri *supplier* dan kerancuan desimal ukuran material dari pencatatan lama membanjiri relasional MySQL baru. | 4 | 4 | **16** | Mewajibkan pengembangan skrip validator CLI import data CSV yang dapat menyaring nilai cacat logika (*null/nan*) untuk direvisi dahulu sebelum dimasukkan ke tabel final. |

---

## 11. Milestone dan Jadwal Tingkat Tinggi

Berikut adalah jadwal *milestone* rancangan level strategis berdurasi penyelesaian 12 bulan:

| No | Fase Proyek / Milestone Utama | Perkiraan Target Selesai | Status | Keterangan |
|----|-------------------------------|--------------------------|:------:|------------|
| 1  | **Inisiasi & Perencanaan**: Penyusunan dan Persetujuan Project Charter Lengkap Terintegrasi | `Bulan 1` | Selesai | Menyetujui visi, ruang lingkup, dan pondasi formal metodologi hibrida (v1.2). |
| 2  | **Analisis Kebutuhan**: Penyusunan dokumen formal SRS (*Software Requirements Specification*) | `Bulan 2` | Belum Dimulai | Menguraikan >42 rincian fitur kebutuhan operasional & validasi non-fungsional. |
| 3  | **Desain Sistem & DB**: Penyusunan dokumen SDD (*System Design Document*) & ERD Skema Multi-Branch | `Bulan 3 - 4` | Belum Dimulai | Merancang relasi entitas tabel MySQL, RBAC JWT Schema, dan *Audit Trail* JSON log. |
| 4  | **Implementasi - Fase I**: Infrastruktur CLI, RBAC, Modul CRM Pelanggan & Basis Transaksi, Impor CSV Awal | `Bulan 5 - 6` | Belum Dimulai | Fondasi Python FP, migrasi berkas otentikasi `.env`, login session bcrypt, & *dashboard*. |
| 5  | **Implementasi - Fase II**: Logika Modul Inventaris presisi BOM desimal, Penggajian Kasbon SDM cerdas | `Bulan 7 - 9` | Belum Dimulai | Algoritma perhitungan desimal presisi persediaan terintegrasi dengan struktur payroll gaji staf. |
| 6  | **Implementasi - Fase III**: Eksekusi Modul PPOB, Keuangan Terpadu & Fitur Laba/Rugi, Penjadwalan Backup | `Bulan 10` | Belum Dimulai | Menghimpun agregasi profitabilitas analitik antar 5 divisi, mitigasi peringatan fraud transaksi kasir. |
| 7  | **Integrasi & Pengujian**: Pelaksanaan Skenario Uji (Test Plan) & User Acceptance Testing (UAT) komprehensif | `Bulan 11` | Belum Dimulai | Validasi asersi 100% test logika *Functional Programming*, penyelesaian beban stress login kasir bersamaan. |
| 8  | **Penerapan & Pelatihan (Go-Live)**: Migrasi final data bersih, Pelatihan simulasi 3 Hari Staf, Sistem Produksi | `Bulan 12` | Belum Dimulai | Pemasangan Server Mini Linux, Windows Klien PC. Aplikasi berjalan penuh (*Zero-Missed Order*). |

---

## 12. Estimasi Anggaran Tingkat Tinggi (High-Level Budget)

Estimasi anggaran proyek disusun secara terperinci untuk memenuhi kebutuhan hardware infrastruktur Dual-OS toko, pengamanan server LAN lokal, alat pelatihan, dan resource pengembangan perangkat lunak berbasis API tim model eksternal AI:

| No | Komponen Biaya | Estimasi (Rp) | Keterangan / Asumsi Anggaran Dasar |
|----|----------------|---------------|------------------------------------|
| 1 | **Perangkat Keras (Hardware)** | Rp 15.500.000 | Pengadaan Mini PC Server Linux khusus (Core i5 gen-12, 16GB RAM, SSD 512GB), pengadaan 1 PC Windows Klien tambahan untuk terminal kasir, 2 unit baterai penstabil tegangan (UPS) mutlak diwajibkan untuk perlindungan dari pemadaman listrik. Asumsi printer/scanner dari perangkat lama. |
| 2 | **Infrastruktur Jaringan LAN Toko** | Rp 2.500.000 | Router jaringan statik MikroTik, Switch Hub Gigabit 8-Port, perkabelan fisik *Star Network* UTP Cat6, pengkabelan RJ45, dan jasa instalasi fisik teknisi vendor. Meniadakan konektivitas WiFi untuk jaminan latensi transfer data. |
| 3 | **Pengembangan Sistem / Software** | Rp 15.000.000 | Kompensasi logistik internal *Junior Programmer*, pembelian paket layanan API bulanan premium AI Claude Sonnet/Opus 4.6 (Thinking), langganan API model logis komputasi tinggi AI Google Gemini 3.1 Pro untuk kalkulasi HPP dan analisa arsitektural selama 12 bulan. Lisensi OS Ubuntu/Debian dan MySQL ditiadakan (open-source). |
| 4 | **Pelatihan Staf & Operasional Transisi** | Rp 2.500.000 | Biaya cetak dokumen *hardcopy* panduan *CLI User Manual* interaktif. Alokasi paket kompensasi konsumsi operasional makan karyawan selama masa percobaan kerja *sandbox training* simulasi 3 hari praktek terminal tanpa risiko pelayanan tamu nyata. |
| 5 | **Dana Cadangan Darurat (*Contingency*)** | Rp 4.500.000 | Alokasi pencadangan penyangga permodalan di-kunci secara terpisah dalam rekening bank untuk melindungi sirkulasi dana pengerjaan dari ancaman klaim mendadak pengembalian investasi kerabat, inflasi hardware PC, atau perpanjangan durasi token API tak terduga. |
| **_** | **Total Estimasi Anggaran Proyek** | **Rp 40.000.000** | **Total komitmen anggaran finansial akhir (CAPEX/OPEX fase awal)** |

---

## 13. Kriteria Keberhasilan Proyek (Success Criteria)

Proyek pembangunan sistem manajemen terpadu AbuCom ini dinyatakan sukses dan bisa dipindahtangankan (*Definition of Done*) apabila memenuhi lima parameter teknis dan fungsional terukur berikut ini di masa *User Acceptance Testing* dan fase bulan *Go-Live*:

1. **Otomatisasi Laporan Finansial (100% Bebas File Excel)**:
   * **Indikator**: Meniadakan seutuhnya pencatatan manual *spreadsheet* sekunder; seluruh (100%) agregat Laba/Rugi, pengeluaran utilitas bulanan, penarikan piutang, tabungan cadangan aset diproses langsung dari basis data.
   * **Metode Uji**: Verifikasi komparasi validasi silang nol manual input (*Zero Manual Input*) dari data MySQL ke terminal laporan CLI, memberikan laporan tepat hitung (*balance*).
2. **Akurasi Konversi BOM Presisi Desimal Stok Fisik (< 1.0% Selisih)**:
   * **Indikator**: Ketepatan rumus fraksi desimal volume perhitungan pemotongan stok pada rekap *Bill of Materials* terbukti relevan menjaga selisih penyimpangan laporan inventaris *Stock Opname* berkala di bawah ambang batas toleransi **1.0%**.
   * **Metode Uji**: Metrik `(Jumlah Selisih Stok Fisik Barang / Total Inventaris Tercatat) * 100% <= 1.0%` sukses tercapai di minggu keempat *Go-Live* produksi nyata.
3. **Penyelamatan Efisiensi Pemrosesan Antrian (0% Transaksi Terlewat)**:
   * **Indikator**: Zero insiden (*Zero-Missed Orders*) pembatalan tagihan disebabkan oleh antrean file produksi desain yang dilupakan oleh unit divisi cetak di keramaian *traffic*.
   * **Metode Uji**: Evaluasi laporan agregasi bulanan menunjukkan integritas seluruh rekaman alur status pesanan bertransisi secara mulus dari `Antri` hingga status sukses `Diambil` oleh pelanggan (100% *conversion rate* log).
4. **Resistensi Keamanan RBAC Eksternal/Internal (100% Pelanggaran Ditolak)**:
   * **Indikator**: Modul operasional privasi kredensial (payroll staf, pinjaman finansial, dan kas bersih) diamankan sepenuhnya eksklusif pada otorisasi sesi identifikasi token *Role: Pemilik*.
   * **Metode Uji**: Menjalankan pengujian penetrasi *sandbox* internal dengan melancarkan minimum 50 percobaan manipulasi hak akses staf yang menghasilkan pengembalian error penolakan *JWT Token Expired/Invalid Role* mutlak 100%.
5. **Mitigasi Pemulihan Produktivitas (*Burnout*) Pemilik Tunggal Usaha**:
   * **Indikator**: Delegasi 90% administrasi transaksi, perancangan desain, pergudangan cetak ke pundak operasional tim staf baru sambil melacak keutuhan uang kas setoran dari jauh.
   * **Metode Uji**: Tinjauan kuantitatif jumlah rutinitas; pemilik tervalidasi hanya menjalankan *login session* harian < 30 menit (berkurang drastis dari 2-3 jam manual kerja administratif), membuktikan pendelegasian berhasil diaplikasikan secara produktif.

---

## 14. Persetujuan dan Otorisasi (Approval)

Dokumen Project Charter ini diajukan dan disetujui secara sadar sebagai acuan kesepakatan final yang definitif dan mengikat secara prosedural untuk kelanjutan seluruh tahapan perancangan arsitektur *Software Requirements Specification* (SRS), *System Design Document* (SDD), hingga komitmen penulisan program. Modifikasi perubahan fundamental dari ruang lingkup (*scope creep*), rancangan finansial proyeksi, dan kerangka desain harus mendapatkan pendelegasian *Change Management* revisi kembali kepada penandatangan terkait.

| Pihak Penandatangan | Jabatan / Peran | Tanda Tangan | Tanggal Persetujuan |
|---------------------|-----------------|--------------|---------------------|
| **Pemilik Usaha AbuCom** | Inisiator, Sponsor Proyek & Junior Programmer | *(Disetujui secara Digital)* | 2026-05-21 |
| **Pemilik Usaha AbuCom** | Manajer Proyek & Penanggung Jawab Internal | *(Disetujui secara Digital)* | 2026-05-21 |
| **Gemini 3.1 Pro (High)** | Lead Architect & Heavy Logic (Tim AI) | *(Disetujui secara Digital)* | 2026-05-28 |

---

## 15. Referensi Dokumen

Daftar pustaka aset referensi SDLC awal yang terkandung dalam agregasi sinkronisasi penyempurnaan isi proposal struktural dokumen:

| # | Nama File | Lokasi Fisik / Path Relatif | Keterangan |
|---|---|---|---|
| 1 | `narasi.txt` | [narasi.txt](docs/sdlc/narasi.txt) | Dokumen primer narasi kebutuhan bisnis, operasional manual, teknis harapan, dan detail alur produk dari kacamata pemilik usaha langsung. |
| 2 | `02_feasibility_study.md` | [02_feasibility_study.md](docs/sdlc/01_planning/02_feasibility_study.md) | Analisis matriks kelayakan ekonomi, ROI keuangan, rekomendasi operasional alternatif dan mitigasi risiko teknis. |
| 3 | `03_stakeholder_register.md` | [03_stakeholder_register.md](docs/sdlc/01_planning/03_stakeholder_register.md) | Daftar analitik klasifikasi pemetaan pengaruh pemangku kepentingan (internal, eksternal, kreditur, supplier) serta matriks RACI detail. |
| 4 | `04_tech_stack_decision.md` | [04_tech_stack_decision.md](docs/sdlc/01_planning/04_tech_stack_decision.md) | Kesimpulan keputusan platform *Dual-OS*, dependensi ekosistem Python 3.14.2+ (FP murni), topologi LAN lokal, dan skema keamanan JWT/bcrypt. |
| 5 | `05_innovation_proposal.md` | [05_innovation_proposal.md](docs/sdlc/01_planning/05_innovation_proposal.md) | Strategi usulan inisiatif rekomendasi *best practice* (Dashboard CLI, Fraud Detection, Shift Handover, Runtime Config) tambahan. |

---

## Glosarium Istilah Domain Percetakan & Bisnis (Glossary)

Berikut adalah pendefinisian ringkas istilah glosarium kamus data perbendaharaan spesifik teknis domain retail Indonesia, industri cetak kustom, regulasi UMKM, dan disiplin perangkat lunak yang terkandung dalam dokumen:

1. **Stempel Flash**: Jenis stempel otomatis tanpa bantalan tinta eksternal, yang menggunakan karet khusus penyerap tinta warna yang disinari lampu kilat (*flash*) mesin stempel saat pembuatan.
2. **Baliho**: Media promosi cetak luar ruangan (*outdoor*) berskala besar, biasanya dicetak di atas bahan *flexi* menggunakan mesin printer format lebar (*wide-format printer*).
3. **Nama Dada**: Papan nama kecil (pin/*tag name*) yang biasanya dipasang di dada pakaian pegawai, terbuat dari bahan akrilik, PVC, atau logam kuningan berlapiskan pelindung resin bening.
4. **Buku Yasin**: Buku kumpulan Surat Yasin Al-Quran yang dirancang kustom untuk acara selamatan kematian, dilengkapi tata letak *hardcover* karton dengan bingkai *hot-print* warna emas.
5. **Map Snelhechter**: Jenis stopmap penjepit dokumen *file* (kertas/plastik PVC) yang dilengkapi dengan mekanika pita/jepitan kawat seng logam di area tengahnya untuk pengarsipan arsip.
6. **PPOB (*Payment Point Online Bank*)**: Agen layanan aplikasi transaksi pembayaran tagihan secara daring pihak ketiga, untuk pelunasan token listrik prabayar PLN, pulsa telpon/data reguler, serta paket data.
7. **Jasa Transfer & Tarik Tunai Agen**: Entitas bisnis cabang penyedia kas fisik uang fiat resmi terafiliasi layanan perbankan (Agen Mandiri/BRILink dll) guna melakukan mutasi antarbank domestik atau penarikan tunai e-wallet.
8. **Bill of Materials (BOM)**: Struktur resep hierarkis daftar material baku mentah logistik (misal material *tinta stempel* ML, *karet flash* cm2, kertas HVS *lembar*) guna memproduksi kuantitas spesifik unit akhir produk cetak secara presisi.
9. **Stock Opname**: Operasional *auditing* reguler mematikan sirkulasi gudang untuk merekam data kuantitas fisik persediaan kasatmata secara manual dan melakukan pencocokan selisih minus terhadap catatan inventaris di basis data sistem.
10. **Audit Trail**: Format dokumentasi *record* terenkripsi sistem (*JSON structured logs*) berisikan runtutan *time-stamped* kronologi modifikasi atau manipulasi nilai database (`old_value` ke `new_value`) untuk akuntabilitas forensik.
11. **Kasbon**: Mekanisme pengambilan fasilitas pinjaman likuiditas karyawan yang dicairkan dimuka, terintegrasi pemotongan angsuran secara otomatis di awal periode pembayaran gaji bulanan agar dana terhindar kredit macet.
12. **Uang Muka / DP (*Down Payment*)**: Instrumen persentase pembayaran sebagian termin nilai *invoice* final transaksi pelanggan yang dilunasi dimuka (*upfront*), berguna mengurangi risiko batal saat spesifikasi produksi kustom telah dieksekusi.
13. **Retur**: Tata kelola logistik pengembalian fisik barang dari konsumen yang dikarenakan masalah cacat manufaktur, malfungsi cetak, atau ketidaksesuaian pesanan pelanggan, berdampak pada pengembalian kas laci kasir.
14. **Functional Programming (FP)**: Paradigma konstruksi desain perangkat lunak deklaratif yang mensyaratkan fungsi matematika murni (*Pure Functions*), imutabilitas data, pelarangan efek samping variabel (*Side-effects*), serta penghindaran konsepsi *Object-Oriented Programming* (Class/Objek).
15. **UMKM**: Usaha Mikro, Kecil, dan Menengah; merujuk pada skala usaha bisnis seperti percetakan AbuCom sesuai dengan regulasi kriteria investasi pemerintah Republik Indonesia.
16. **RBAC (*Role-Based Access Control*)**: Paradigma sistem perizinan keamanan otorisasi bertingkat berdasarkan klasifikasi peran kewenangan staf (contoh: `Role: Pemilik` vs `Role: Staf`) dalam mengakses kapabilitas tampilan menu operasi layar terminal.
17. **JWT (*JSON Web Token*)**: Protokol autentikasi *stateless* terenkripsi yang ditransmisikan setelah pengguna berhasil mengidentifikasi password (login) untuk manajemen otorisasi sesi CLI (*session token*) tanpa bergantung file session server.
18. **bcrypt**: Algoritma fungsi kriptografi *hashing* searah (*one-way*) ber-kunci (*Cost Factor*) untuk mengamankan penyimpanan teks kata sandi pengguna sebagai *string* karakter acak ke dalam tabel *database* yang anti peretasan tebakan massal (*bruteforce*).
