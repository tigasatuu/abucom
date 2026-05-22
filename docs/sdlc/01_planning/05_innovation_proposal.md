---
dokumen    : Innovation Proposal
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : 2026-05-22
status     : Draft
penyusun   : Senior Innovation Strategist & Industry Best Practice Analyst
---

# Innovation Proposal — AbuCom

## Riwayat Perubahan Dokumen

| Versi | Tanggal    | Perubahan                                                   | Oleh                                                        |
|-------|------------|-------------------------------------------------------------|-------------------------------------------------------------|
| 1.0   | 2026-05-22 | Pembuatan awal dokumen secara komprehensif berdasarkan analisis Project Charter v1.1, Feasibility Study v1.1, Stakeholder Register v1.1, dan Tech Stack Decision v1.1. | Senior Innovation Strategist & Industry Best Practice Analyst |

---

## 1. Informasi Dokumen

Dokumen **Innovation Proposal** ini disusun untuk mendokumentasikan usulan inovasi strategis, fitur unggulan, dan praktik terbaik industri percetakan modern serta ritel yang akan diintegrasikan ke dalam sistem aplikasi **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**.

Sebagai dokumen ke-5 dan terakhir dalam fase **Planning** pada siklus SDLC AbuCom, posisi dokumen ini sangat krusial sebagai:
1. **Penyaring Strategi Inovasi**: Mendokumentasikan usulan inovasi teknis dan bisnis agar terdokumentasi secara formal dan terarah.
2. **Jembatan Konseptual**: Menghubungkan visi strategis pada [Project Charter v1.1](docs/sdlc/01_planning/01_project_charter.md) dan keputusan teknis pada [Tech Stack Decision v1.1](docs/sdlc/01_planning/04_tech_stack_decision.md) untuk diturunkan menjadi kebutuhan fungsional dan non-fungsional pada fase *Requirements* (SRS) dan desain skema basis data pada fase *Design* (SDD).
3. **Pemenuhan Mandat Bisnis**: Mengakomodasi mandat dari pemilik usaha (pada [narasi.txt](docs/sdlc/narasi.txt) Baris 98) agar tim pengembang AI proaktif mengusulkan peningkatan operasional, logika alur kerja, dan aspek keamanan demi meningkatkan kualitas sistem.

---

## 2. Ringkasan Eksekutif (Executive Summary)

Penyusunan sistem AbuCom dilatarbelakangi oleh kondisi operasional toko percetakan fisik pemilik usaha yang mengalami keletihan mental (*burnout*) akibat beban kerja manual (*single-fighter*) dalam mengelola 5 divisi usaha yang kompleks. Untuk mengatasi permasalahan tersebut, direncanakan rekrutmen 7 posisi staf baru yang didukung oleh sistem digital terpadu berbasis *Command Line Interface* (CLI) Python dan database MySQL lokal.

Dokumen ini memetakan total **38 usulan inovasi** yang dirancang khusus untuk meningkatkan keandalan operasional, keamanan kas/data pribadi, serta skalabilitas sistem AbuCom. Usulan tersebut terbagi menjadi:
1. **26 Inovasi Terintegrasi** (sudah masuk dalam perencanaan Project Charter dan Tech Stack Decision), yang mencakup inovasi arsitektur pemrograman fungsional murni, perhitungan HPP BOM presisi desimal, audit trail terstruktur JSON, hingga otentikasi session JWT.
2. **3 Rekomendasi Inovasi Sebelumnya** (backup otomatis, whatsapp template ready, prediksi re-order stok).
3. **9 Inovasi Tambahan Baru** yang diusulkan oleh tim AI, seperti Dashboard CLI ringkasan harian, riwayat harga beli supplier (*price tracking*), pengingat jatuh tempo otomatis, log serah terima shift kasir (*shift handover log*), pencatatan margin profit produk, sistem deteksi fraud sederhana, template cetak teks, import CSV, dan sistem konfigurasi dinamis (*runtime config*).

Secara strategis, integrasi seluruh inovasi ini diproyeksikan dapat memotong waktu rekapitulasi harian dari **2-3 jam menjadi instan (<5 detik)**, menekan kehilangan stok limbah cetak hingga **15%**, dan mengamankan data sensitif pemilik dari potensi kecurangan internal staf baru.

---

## 3. Latar Belakang dan Konteks Inovasi

### 3.1. Kondisi Operasional Saat Ini
Usaha UMKM AbuCom merupakan unit usaha terintegrasi yang melayani 5 kategori divisi bisnis: produksi cetak kustom (stempel flash, baliho, dll), retail ATK, PPOB saldo virtual, jasa keuangan agen bank, dan jasa teknis perbaikan printer/PC. 

Saat ini seluruh pembukuan transaksi keuangan, pelacakan stok bahan baku, mutasi saldo e-wallet, dan administrasi gaji/kasbon dilakukan secara manual menggunakan file-file Microsoft Excel yang berserakan. Hal ini memicu masalah inefisiensi, kerentanan kebocoran kas laci kasir (*fraud*), pembulatan dimensi bahan yang tidak akurat, serta *burnout* pemilik yang memegang peran tunggal operasional toko.

### 3.2. Mandat Inovasi dari Pemilik Usaha
Sebagai landasan formal, pemilik bisnis memberikan mandat inovasi pada dokumen [narasi.txt](docs/sdlc/narasi.txt) Baris 98:
> *"Saya mewajibkan tim AI pengembang untuk secara aktif melakukan analisis terhadap standar industri percetakan dan retail modern. Jika ditemukan fitur, logika alur kerja, atau metode keamanan yang belum saya sebutkan namun secara signifikan dapat meningkatkan kualitas sistem, efisiensi operasional, atau perlindungan data, maka tim AI **wajib** mengusulkannya dan memasukkannya ke dalam setiap dokumen perencanaan (fase SDLC) sebagai bagian dari penyempurnaan sistem ini."*

Mandat ini menjadi landasan hukum internal bagi tim AI untuk menyusun proposal ini dan menyuntikkan inovasi bernilai tinggi bagi keberlanjutan usaha AbuCom.

### 3.3. Tujuan Strategis Inovasi
Berdasarkan tujuan spesifik (SMART Goals) pada Project Charter, tujuan strategis inovasi didefinisikan sebagai berikut:
1. **Otomatisasi & Presisi Stok**: Mengurangi selisih stok fisik vs sistem hingga `< 1.0%` menggunakan BOM dimensi/volume desimal.
2. **Real-time Profitability**: Menyajikan laporan profitabilitas per divisi layanan secara instan (`< 5 detik`).
3. **Zero-Missed Orders**: Menghilangkan insiden pesanan terlewat melalui visualisasi status antrian terotomatisasi.
4. **Fraud Prevention & Security**: Melindungi data sensitif pemilik dan kas laci melalui enkripsi bcrypt, token JWT, RBAC, dan Audit Trail.
5. **Skalabilitas Ekspansi**: Menjamin kesiapan skema database MySQL 100% untuk multi-cabang sejak awal.

---

## 4. Inovasi yang Sudah Terintegrasi dalam Perencanaan

Bagian ini merangkum 26 inovasi yang telah disepakati pada dokumen perencanaan sebelumnya (Project Charter, Feasibility Study, dan Tech Stack Decision).

### 4.1. Inovasi Arsitektur dan Paradigma Sistem

#### **INV-INT-01: Arsitektur Multi-Cabang (Multi-Branch Ready)**
* **Deskripsi Teknis**: Penambahan kolom `cabang_id` (INT) sebagai *foreign key* ke tabel `cabang` pada setiap tabel utama database relasional MySQL.
* **Justifikasi Bisnis**: Mempersiapkan sistem untuk ekspansi bisnis jangka panjang tanpa perlu menulis ulang atau memigrasikan database di masa depan.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.9]](docs/sdlc/01_planning/01_project_charter.md), [Tech Stack Decision v1.1 Bagian 4.1](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Menjamin kesiapan migrasi multi-cabang terpusat (konsolidasi laporan) secara instan.

#### **INV-INT-02: Paradigma Functional Programming Murni**
* **Deskripsi Teknis**: Pembangunan program Python murni menggunakan fungsi-fungsi murni (*pure functions*), imutabilitas data (*namedtuples/frozen dataclasses*), *nested closures*, dan menolak penggunaan class/OOP pada logika bisnis utama.
* **Justifikasi Bisnis**: Menjamin keandalan kalkulasi finansial dan inventaris yang bebas dari efek samping (*side-effects*).
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 3.2](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Meminimalkan tingkat *bug* logika komputasi keuangan dan mempermudah unit testing.

#### **INV-INT-03: Arsitektur Client-Server Lokal (LAN)**
* **Deskripsi Teknis**: Penempatan database MySQL Server lokal pada Mini PC Server Debian 12 yang dihubungkan ke terminal klien kasir Windows 11 melalui kabel jaringan UTP Cat6.
* **Justifikasi Bisnis**: Menolak biaya langganan bulanan cloud (*OPEX reduction*) dan menjaga operasional toko tetap berjalan saat koneksi internet area mati.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 6.2](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Mengurangi pengeluaran operasional internet cloud dan memastikan waktu respon data `< 1ms`.

### 4.2. Inovasi Manajemen Inventaris dan Produksi

#### **INV-INT-04: Sistem HPP Otomatis Berbasis Bill of Materials (BOM) Presisi Desimal**
* **Deskripsi Teknis**: Kalkulasi HPP secara real-time berdasarkan komposisi multi-bahan yang menggunakan input dimensi desimal panjang x lebar (kertas baliho/karet flash stempel) atau volume desimal (cairan tinta) menggunakan pustaka `decimal` Python.
* **Justifikasi Bisnis**: Menggantikan kalkulasi taksiran manual yang rawan merugi dengan harga pokok penjualan yang presisi.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.2]](docs/sdlc/01_planning/01_project_charter.md), [Feasibility Study v1.1 Bagian 4.2.2](docs/sdlc/01_planning/02_feasibility_study.md).
* **Dampak Bisnis**: Akurasi HPP produk kustom mencapai 100%, mengoptimalkan penetapan harga jual.

#### **INV-INT-05: Pencatatan Limbah Produksi (Waste Management)**
* **Deskripsi Teknis**: Menu input khusus untuk mencatat bahan baku yang rusak atau salah cetak selama proses finishing produksi, terhubung dengan penyesuaian stok sistem.
* **Justifikasi Bisnis**: Mengukur inefisiensi bahan baku cetak secara objektif agar selisih stok gudang fisik vs sistem tetap akurat.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.2]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Menekan kerugian akibat limbah tidak teridentifikasi hingga 15% per tahun.

#### **INV-INT-06: Manajemen Satuan dan Atribut Barang (Unit of Measure)**
* **Deskripsi Teknis**: Logika konversi dinamis antar satuan ukur (contoh: Rim ↔ Lembar, Liter ↔ Mililiter) dengan dukungan angka pecahan desimal pada database MySQL.
* **Justifikasi Bisnis**: Memberikan fleksibilitas pencatatan stok bahan baku eceran di gudang percetakan.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.2]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Mempermudah staf gudang mengelola stok eceran tanpa perlu menghitung ulang secara manual.

#### **INV-INT-07: Sinkronisasi Barang Retail untuk Kebutuhan Produksi Internal**
* **Deskripsi Teknis**: Transaksi fungsional yang memotong stok barang retail ATK (kertas HVS, tinta) untuk digunakan sebagai bahan produksi internal dan mencatatnya sebagai pengeluaran operasional.
* **Justifikasi Bisnis**: Mencegah hilangnya barang retail dari gudang tanpa pelacakan finansial yang jelas.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.2]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Menghilangkan selisih stok barang retail yang dipakai untuk produksi mandiri.

#### **INV-INT-08: Rekonsiliasi Stok Berkala (Stock Opname)**
* **Deskripsi Teknis**: Fitur pembekuan stok sementara, input stok fisik, pencatatan otomatis nilai selisih barang, dan penyimpanan riwayat stock opname.
* **Justifikasi Bisnis**: Menyediakan mekanisme audit persediaan berkala guna meminimalisir kehilangan barang di gudang.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.2]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Selisih stok fisik vs sistem dapat ditekan di bawah 1.0% secara konsisten.

### 4.3. Inovasi Manajemen SDM dan Penggajian

#### **INV-INT-09: Sistem Penggajian Otomatis Cerdas (Smart Payroll)**
* **Deskripsi Teknis**: Fungsi seleksi kondisional: Gaji Tetap (jika target laba bulanan sebesar `[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha]` tercapai) vs Gaji Persentase Laba sebesar `[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha]` (jika target tidak tercapai).
* **Justifikasi Bisnis**: Menjaga stabilitas arus kas operasional toko dari ancaman kerugian saat omzet bulanan menurun.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.4]](docs/sdlc/01_planning/01_project_charter.md), [Feasibility Study v1.1 Bagian 4.2.4](docs/sdlc/01_planning/02_feasibility_study.md).
* **Dampak Bisnis**: Menghindari pengeluaran gaji yang melebihi kemampuan finansial bulanan toko.

#### **INV-INT-10: Sistem Poin Insentif Karyawan Berbasis Beban Kerja**
* **Deskripsi Teknis**: Akumulasi poin otomatis (1 poin = Rp 500 untuk transaksi rutin, 3 poin = Rp 1.500 untuk jasa dasar, 5 poin = Rp 2.500 untuk produk kustom, atau 10 poin = Rp 5.000 untuk pekerjaan berat/teknis) per transaksi berdasarkan tingkat kesulitan tugas, terintegrasi langsung dengan bonus slip gaji bulanan staf.
* **Justifikasi Bisnis**: Meningkatkan produktivitas kerja staf dan mendukung budaya saling membantu lintas fungsi (*cross-functional*).
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.4]](docs/sdlc/01_planning/01_project_charter.md), [Feasibility Study v1.1 Bagian 4.2.4](docs/sdlc/01_planning/02_feasibility_study.md).
* **Dampak Bisnis**: Memotivasi staf menyelesaikan antrian produksi lebih cepat dan merata.

#### **INV-INT-11: Manajemen Kasbon dengan Pemotongan Gaji Otomatis**
* **Deskripsi Teknis**: Modul pencatatan limit kasbon aktif per karyawan (sebesar `[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha]`), terintegrasi dengan pemotongan nominal gaji otomatis pada siklus penggajian bulanan.
* **Justifikasi Bisnis**: Menyederhanakan pencatatan utang karyawan secara transparan dan aman bagi kas pemilik.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.4]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Mengeliminasi piutang karyawan yang tidak tertagih akibat kelupaan rekap manual.

### 4.4. Inovasi Pelacakan Operasional dan Pelanggan

#### **INV-INT-12: Sistem Manajemen Antrian Digital (Job Tracking)**
* **Deskripsi Teknis**: Transisi 5 status pekerjaan (`Antri` -> `Proses Desain` -> `Produksi` -> `Selesai` -> `Diambil`) via update record database MySQL.
* **Justifikasi Bisnis**: Mencegah hilangnya pesanan kustom pelanggan (Zero-Missed Orders) di tengah kesibukan toko.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.5]](docs/sdlc/01_planning/01_project_charter.md), [Feasibility Study v1.1 Bagian 4.2.5](docs/sdlc/01_planning/02_feasibility_study.md).
* **Dampak Bisnis**: Menghilangkan insiden pesanan terlewat hingga 0%, meningkatkan kepuasan pelanggan.

#### **INV-INT-13: Arsip Desain Pelanggan untuk Cetak Ulang Cepat**
* **Deskripsi Teknis**: Penyimpanan metadata path direktori server lokal tempat menyimpan file desain pelanggan yang diinput oleh desainer.
* **Justifikasi Bisnis**: Memangkas waktu pencarian file desain pelanggan lama saat ingin melakukan cetak ulang (*re-order*).
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.5]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Mempercepat proses persiapan cetak ulang hingga 70% dibanding pencarian manual di komputer desainer.

#### **INV-INT-14: Database Pelanggan (CRM Sederhana)**
* **Deskripsi Teknis**: Tabel khusus untuk menyimpan data identitas pelanggan (Nama, Nomor WhatsApp) yang terhubung ke log riwayat pembelian.
* **Justifikasi Bisnis**: Menyediakan basis data kontak pelanggan terstruktur untuk penawaran promosi dan analisis perilaku belanja.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.8]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Mempermudah pemilik menghubungi pelanggan loyal untuk kampanye pemasaran tertarget.

### 4.5. Inovasi Keamanan dan Kepatuhan Regulasi

#### **INV-INT-15: Role-Based Access Control (RBAC) Multi-Level**
* **Deskripsi Teknis**: Pembatasan menu terminal CLI di tingkat aplikasi Python untuk membedakan antara menu Pemilik (sensitif/keuangan) dan menu Staf (operasional).
* **Justifikasi Bisnis**: Melindungi kerahasiaan data tabungan pribadi, pinjaman bank, dan payroll dari akses staf harian.
* **Sumber Data**: [Project Charter v1.1 Bagian 8.2 [N-2.1]](docs/sdlc/01_planning/01_project_charter.md), [Tech Stack Decision v1.1 Bagian 8.3](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Menjamin privasi data finansial pemilik 100% terjaga dari internal karyawan.

#### **INV-INT-16: Audit Trail Kronologis Terstruktur (JSON)**
* **Deskripsi Teknis**: Pencatatan log aktivitas sensitif (hapus data, edit stok, retur) ke tabel `audit_logs` dengan format JSON yang menyimpan nilai sebelum (*old_value*) dan sesudah (*new_value*).
* **Justifikasi Bisnis**: Mencegah dan melacak kecurangan kas (*fraud*) oleh karyawan operasional secara forensik.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.4](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Menyediakan bukti transparan pelacakan kesalahan input atau manipulasi data kasir.

#### **INV-INT-17: Enkripsi Kata Sandi Standar Industri (bcrypt Cost 12)**
* **Deskripsi Teknis**: Hashing satu arah sandi pengguna menggunakan pustaka `bcrypt` Python dengan cost factor 12 sebelum disimpan ke database MySQL.
* **Justifikasi Bisnis**: Mengamankan kata sandi dari ancaman peretasan database lokal oleh pihak internal/eksternal.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.1](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Kredensial staf terlindungi penuh, memenuhi prinsip privasi digital standar industri.

#### **INV-INT-18: Autentikasi Session Stateless (JWT 8 Jam)**
* **Deskripsi Teknis**: Penerbitan token JWT terenkripsi HS256 yang valid selama 8 jam (setara shift kerja staf) untuk validasi sesi CLI aktif.
* **Justifikasi Bisnis**: Menjaga integritas sesi aktif di memori CLI klien tanpa bergantung pada file session server yang rawan dimanipulasi.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.2](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Sesi pengguna otomatis logout saat shift berakhir, meminimalisir penyalahgunaan menu oleh staf shift berikutnya.

#### **INV-INT-19: Proteksi SQL Injection dan Validasi Input**
* **Deskripsi Teknis**: Penerapan parameterized queries (`%s`) resmi dari driver MySQL di Python, pelarangan manipulasi f-string SQL, dan validasi tipe data masukan terminal.
* **Justifikasi Bisnis**: Menutup celah keamanan database relasional dari injeksi karakter perusak sistem.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.6 & 8.8](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Stabilitas database MySQL terjamin dari serangan injeksi kode perusak.

#### **INV-INT-20: Rate Limiting Login CLI**
* **Deskripsi Teknis**: Logika penguncian akun sementara selama 10 menit (`locked_until`) di tabel database jika terjadi 5 kali gagal login berturut-turut.
* **Justifikasi Bisnis**: Mencegah tebakan kata sandi otomatis (*brute-force attack*) di komputer kasir.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.7](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Komputer kasir yang ditinggalkan staf aman dari upaya pembobolan login paksa.

#### **INV-INT-21: Enkripsi Backup Database (AES-256)**
* **Deskripsi Teknis**: Skrip ekspor database otomatis ke berkas SQL yang langsung dikompresi ke file zip terenkripsi AES-256 bit.
* **Justifikasi Bisnis**: Mematuhi regulasi hukum perlindungan data pribadi **UU PDP No. 27 Tahun 2022** di Indonesia.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.5](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: File cadangan database yang ditarik via flashdisk secara ilegal tidak dapat dibuka tanpa kunci AES pemilik.

### 4.6. Inovasi Keuangan dan Transaksi

#### **INV-INT-22: Multi-Skema Harga Dinamis (Retail, Grosir, Mitra)**
* **Deskripsi Teknis**: Kalkulasi otomatis harga jual di terminal kasir berdasarkan kuantitas barang (grosir) dan status keanggotaan pelanggan (mitra).
* **Justifikasi Bisnis**: Mengakomodasi kebutuhan strategi pemasaran fleksibel retail ATK untuk meningkatkan loyalitas pelanggan.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.1]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Proses penghitungan harga transaksi kasir berjalan otomatis dan bebas *human error*.

#### **INV-INT-23: Pembayaran Bertahap (DP dan Pelunasan)**
* **Deskripsi Teknis**: Pencatatan status tagihan terpisah untuk uang muka (`DP`) di awal dan `Pelunasan` saat barang diserahkan ke pelanggan.
* **Justifikasi Bisnis**: Menjaga ketersediaan kas modal belanja bahan baku untuk pesanan bernilai besar.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.1]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Memastikan seluruh piutang pesanan diselesaikan sebelum barang dibawa pulang pelanggan.

#### **INV-INT-24: Alur Pembatalan dan Retur Tersinkronisasi**
* **Deskripsi Teknis**: Transaksi ACID yang mengembalikan kuantitas stok barang retail dan memotong kas laci secara terintegrasi saat transaksi dibatalkan/retur.
* **Justifikasi Bisnis**: Menjaga keakuratan sinkronisasi data mutasi kas laci kasir dan sisa stok barang gudang.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.8]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Laporan keuangan harian bebas dari selisih nominal akibat retur barang yang tidak tercatat.

#### **INV-INT-25: Rekonsiliasi Kas Harian (Cash Reconciliation)**
* **Deskripsi Teknis**: Form input uang kas laci kasir fisik sebelum sistem diizinkan keluar (logout), mencocokkannya dengan kas tercatat sistem dan menyimpan nilai selisih.
* **Justifikasi Bisnis**: Mendeteksi dini selisih kas fisik akibat kembalian salah atau kelalaian kasir.
* **Sumber Data**: [Project Charter v1.1 Bagian 8.1 [F-6.5]](docs/sdlc/01_planning/01_project_charter.md), [Feasibility Study v1.1 Bagian 8.6](docs/sdlc/01_planning/02_feasibility_study.md).
* **Dampak Bisnis**: Disiplin pelaporan kas meningkat, kebocoran uang kas toko dapat diminimalisir hingga 99%.

#### **INV-INT-26: Laporan Laba/Rugi Instan per Divisi**
* **Deskripsi Teknis**: Agregasi otomatis pendapatan kotor dikurangi HPP bahan baku per transaksi yang dikelompokkan berdasarkan 5 divisi usaha.
* **Justifikasi Bisnis**: Menyajikan data profitabilitas riil setiap kategori usaha secara real-time untuk keputusan strategis pemilik.
* **Sumber Data**: [Project Charter v1.1 Bagian 8.1 [F-6.4]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Pemilik mengetahui divisi mana yang merugi atau menjadi kontributor laba terbesar secara instan (`< 5 detik`).

---

## 5. Usulan Inovasi Tambahan (Rekomendasi Baru)

Bagian ini memaparkan usulan inovasi tambahan yang dirancang secara proaktif untuk menyempurnakan sistem AbuCom berdasarkan tren industri percetakan modern dan ritel UMKM di Indonesia.

### 5.1. Inovasi yang Sudah Direkomendasikan di Dokumen Sebelumnya

#### **INV-REC-01: Backup Data Otomatis Berkala**
* **Deskripsi**: Penjadwalan skrip otomatis untuk melakukan backup basis data MySQL ke format berkas SQL terkompresi (.zip) setiap akhir hari operasional (Pukul 21:00) ke folder cadangan lokal terpisah.
* **Justifikasi Bisnis**: Menghindari hilangnya seluruh data transaksi dan inventaris akibat kegagalan perangkat keras (*harddisk crash*) di Mini PC Server.
* **Dampak Operasional**: Pemilik terbebas dari keharusan mengekspor database secara manual setiap hari.
* **Kompleksitas Implementasi**: Rendah.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-6 (Fase Implementasi I Akhir).

#### **INV-REC-02: Notifikasi Template WhatsApp Ready**
* **Deskripsi**: Sistem menyediakan menu CLI untuk menghasilkan teks template pesan WhatsApp terformat (DP diterima, pesanan selesai siap diambil, rincian biaya) yang disertai tautan web `https://wa.me/` untuk memudahkan disalin-tempel staf ke WhatsApp Web secara manual.
* **Justifikasi Bisnis**: Mengatasi keterbatasan aplikasi CLI yang tidak terhubung dengan API WA gateway berbayar, mempercepat komunikasi staf ke pelanggan.
* **Dampak Operasional**: Staf kasir/pramuniaga dapat mengabari pelanggan tentang status pesanan dalam waktu kurang dari 30 detik tanpa mengetik ulang pesan.
* **Kompleksitas Implementasi**: Rendah.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-5 (Fase Implementasi I).

#### **INV-REC-03: Analisis Prediksi Re-Order Stok**
* **Deskripsi**: Logika matematika fungsional untuk menganalisis rata-rata kecepatan pemakaian bahan baku (seperti kertas foto, rim kertas HVS) dari riwayat bulanan, memproyeksikan sisa hari ketersediaan stok, dan memicu alert visual jika stok diprediksi habis dalam 7 hari.
* **Justifikasi Bisnis**: Mencegah hilangnya potensi omzet akibat bahan baku kosong saat pelanggan datang membawa pesanan besar.
* **Dampak Operasional**: Staf gudang dibantu merencanakan belanja stok bahan secara terjadwal berdasarkan data historis pemakaian.
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-9 (Fase Implementasi II Akhir).

### 5.2. Inovasi Tambahan yang Diusulkan oleh Tim AI

#### **INV-NEW-01: Sistem Dashboard Ringkasan Harian CLI**
* **Deskripsi**: Tampilan antarmuka visual ringkas menggunakan panel `rich` saat user dengan level Pemilik berhasil login. Dashboard menampilkan ringkasan performa hari berjalan: total omzet, total profit kotor, jumlah antrian status pending, daftar stok kritis, dan total kas laci terhitung.
* **Justifikasi Bisnis**: Menyajikan visibilitas kilat terhadap kondisi toko tanpa perlu Pemilik membuka menu laporan satu per satu.
* **Dampak Operasional**: Pemilik langsung mengetahui isu operasional kritis (misal stok kosong atau antrian menumpuk) begitu membuka aplikasi di pagi hari.
* **Kompleksitas Implementasi**: Rendah.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-6 (Fase Implementasi I Akhir).

#### **INV-NEW-02: Fitur Riwayat Harga Beli Supplier (Price Tracking)**
* **Deskripsi**: Tabel database `supplier_prices` yang mencatat fluktuasi harga beli bahan baku/barang dari setiap supplier setiap kali dilakukan transaksi pengadaan barang masuk oleh staf gudang.
* **Justifikasi Bisnis**: Membantu usaha menghemat modal belanja dengan membandingkan harga historis dan memilih supplier yang menawarkan harga termurah untuk kualitas yang sama.
* **Dampak Operasional**: Staf gudang dibekali rekomendasi supplier termurah secara otomatis saat menginput rencana belanja stok.
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-7 (Fase Implementasi II Awal).

#### **INV-NEW-03: Sistem Notifikasi Jatuh Tempo Otomatis (Pinjaman & Supplier)**
* **Deskripsi**: Pemicu visual (*startup alert*) yang mendeteksi dan menampilkan pesan peringatan visual H-3 sebelum tanggal jatuh tempo cicilan bulanan Bank (BRI dan Mandiri) atau tanggal jatuh tempo pembayaran utang supplier tempo.
* **Justifikasi Bisnis**: Melindungi nama baik dan kredibilitas pemilik usaha dari catatan buruk kredit perbankan serta denda keterlambatan.
* **Dampak Operasional**: Mengeliminasi kelalaian pemilik dalam menyiapkan dana kas untuk pembayaran kewajiban rutin bulanan.
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-10 (Fase Implementasi III).

#### **INV-NEW-04: Log Aktivitas Shift Karyawan (Shift Handover Log)**
* **Deskripsi**: Tabel pencatatan serah terima shift kasir yang memuat: ID staf keluar, ID staf masuk, timestamp serah terima, total uang fisik di laci kasir saat diserahterimakan, catatan operasional khusus (misal: "mesin cetak stempel sedikit tersendat").
* **Justifikasi Bisnis**: Menjaga kedisiplinan operasional kasir dan mempermudah investigasi jika terjadi selisih kas fisik di akhir shift.
* **Dampak Operasional**: Mengikat pertanggungjawaban kas laci secara personal pada masing-masing kasir aktif.
* **Kompleksitas Implementasi**: Rendah.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-6 (Fase Implementasi I).

#### **INV-NEW-05: Fitur Pencatatan Margin Keuntungan per Produk**
* **Deskripsi**: Modul kalkulasi margin profit kotor persentase (margin = `((harga_jual - HPP_BOM) / harga_jual) * 100`) untuk setiap item barang retail dan jasa percetakan yang tersimpan dalam database.
* **Justifikasi Bisnis**: Membantu pemilik dalam mengevaluasi portofolio produk dan memfokuskan promosi pemasaran pada layanan dengan profit margin tertinggi.
* **Dampak Operasional**: Pemilik mendapatkan metrik persentase margin kotor instan langsung pada menu pengelolaan barang/jasa.
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-10 (Fase Implementasi III).

#### **INV-NEW-06: Sistem Peringatan Anomali Transaksi (Fraud Detection Sederhana)**
* **Deskripsi**: Logika pendeteksi aktivitas mencurigakan yang memantau: pembatalan transaksi berulang (>3 kali dalam 1 shift), retur barang retail berturut-turut oleh kasir yang sama, atau selisih rekonsiliasi kas fisik di atas batas toleransi `[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha]`.
* **Justifikasi Bisnis**: Mengurangi kerugian kebocoran kas dari kecurangan internal staf baru yang memanfaatkan kelemahan sistem transaksi.
* **Dampak Operasional**: Sistem secara otomatis mengirimkan alert notifikasi khusus pada panel dashboard pemilik saat login jika terdeteksi indikasi anomali.
* **Kompleksitas Implementasi**: Tinggi.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-10 (Fase Implementasi III).

#### **INV-NEW-07: Template Laporan Cetak Teks untuk Arsip Fisik**
* **Deskripsi**: Ekspor data laporan keuangan harian dan rekonsiliasi stok menjadi format plain text (.txt) yang dirancang khusus (lebar kolom disesuaikan) agar pas untuk dicetak langsung menggunakan printer thermal struk nota 58mm/80mm di toko.
* **Justifikasi Bisnis**: Menyediakan dokumentasi cetak fisik (*hardcopy*) untuk pencatatan laci kas harian tanpa memerlukan kertas besar printer standar.
* **Dampak Operasional**: Staf kasir dapat melampirkan kertas cetakan struk rekap harian bersama dengan setoran uang fisik harian ke laci Pemilik.
* **Kompleksitas Implementasi**: Rendah.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-5 (Fase Implementasi I).

#### **INV-NEW-08: Fitur Import Data CSV/Excel Semiautomatis**
* **Deskripsi**: Skrip modul CLI independen yang membaca berkas CSV ekspor data Excel lama milik pemilik usaha (master data barang, data supplier, data stok awal) dan memvalidasi kebersihan format datanya sebelum disimpan ke basis data MySQL.
* **Justifikasi Bisnis**: Mempercepat proses setup awal database AbuCom dari ribuan data Excel yang berserakan, menghindari entri data manual satu per satu yang rawan salah ketik.
* **Dampak Operasional**: Memangkas waktu inisialisasi go-live sistem dari estimasi berminggu-minggu menjadi kurang dari 1 hari operasional.
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-5 (Fase Implementasi I).

#### **INV-NEW-09: Sistem Konfigurasi Dinamis Tanpa Hardcode (Runtime Config)**
* **Deskripsi**: Penyimpanan parameter regulasi bisnis (persentase pembagian gaji bulanan sebesar `[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha]`, threshold limit nominal kasbon staf sebesar `[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha]`, nilai rupiah per poin insentif, dan limit kritis saldo PPOB sebesar `[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha]`) di tabel konfigurasi database `system_configs` yang dapat dimodifikasi oleh pemilik via menu CLI.
* **Justifikasi Bisnis**: Meniadakan keharusan melakukan perubahan kode program Python oleh tim AI di masa depan jika pemilik ingin merubah kebijakan operasional usahanya.
* **Dampak Operasional**: Memberikan fleksibilitas kontrol bisnis penuh di tangan pemilik selaku administrator utama sistem.
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-9 (Fase Implementasi II Akhir).

---

## 6. Analisis Kelayakan Inovasi

### 6.1. Matriks Kelayakan Inovasi Terintegrasi

Evaluasi kelayakan untuk 26 inovasi terintegrasi didasarkan pada parameter teknis dan operasional:

| Kode Inovasi | Nama Inovasi | Kelayakan Teknis | Kelayakan Operasional | Prioritas | Status |
|---|---|---|---|---|---|
| **INV-INT-01** | Arsitektur Multi-Cabang | Layak | Sangat Layak | High | Terintegrasi |
| **INV-INT-02** | Paradigma FP Murni | Layak dengan Catatan | Layak | High | Terintegrasi |
| **INV-INT-03** | Arsitektur Client-Server LAN | Layak | Layak | High | Terintegrasi |
| **INV-INT-04** | HPP BOM Desimal | Layak | Layak | High | Terintegrasi |
| **INV-INT-05** | Pencatatan Limbah Cetak | Layak | Layak dengan Catatan | High | Terintegrasi |
| **INV-INT-06** | Manajemen Satuan UoM | Layak | Layak | High | Terintegrasi |
| **INV-INT-07** | Sinkronisasi ATK Internal | Layak | Layak | Medium | Terintegrasi |
| **INV-INT-08** | Stock Opname Berkala | Layak | Layak dengan Catatan | High | Terintegrasi |
| **INV-INT-09** | Penggajian Smart Payroll | Layak | Layak | High | Terintegrasi |
| **INV-INT-10** | Poin Insentif Karyawan | Layak | Layak | High | Terintegrasi |
| **INV-INT-11** | Pemotongan Gaji Kasbon | Layak | Layak | High | Terintegrasi |
| **INV-INT-12** | Antrian Job Tracking | Layak | Layak dengan Catatan | High | Terintegrasi |
| **INV-INT-13** | Arsip Desain Pelanggan | Layak | Layak | Medium | Terintegrasi |
| **INV-INT-14** | Database Pelanggan CRM | Layak | Layak | Medium | Terintegrasi |
| **INV-INT-15** | RBAC Multi-Level | Layak | Layak | High | Terintegrasi |
| **INV-INT-16** | Audit Trail JSON | Layak | Layak | High | Terintegrasi |
| **INV-INT-17** | Enkripsi bcrypt Sandi | Layak | Layak | High | Terintegrasi |
| **INV-INT-18** | Autentikasi JWT | Layak | Layak | High | Terintegrasi |
| **INV-INT-19** | Proteksi SQL Injection | Layak | Layak | High | Terintegrasi |
| **INV-INT-20** | Rate Limiting Login | Layak | Layak | Medium | Terintegrasi |
| **INV-INT-21** | Enkripsi Backup database | Layak | Layak | High | Terintegrasi |
| **INV-INT-22** | Multi-Skema Harga | Layak | Layak | High | Terintegrasi |
| **INV-INT-23** | Pembayaran Bertahap DP | Layak | Layak | High | Terintegrasi |
| **INV-INT-24** | Batal/Retur Sinkron | Layak | Layak | High | Terintegrasi |
| **INV-INT-25** | Rekonsiliasi Kas Harian | Layak | Layak dengan Catatan | High | Terintegrasi |
| **INV-INT-26** | Laba/Rugi Instan Divisi | Layak | Layak | High | Terintegrasi |

### 6.2. Matriks Kelayakan Inovasi Tambahan (Rekomendasi Baru)

Evaluasi kelayakan untuk 12 inovasi tambahan baru (3 rekomendasi lama, 9 usulan baru):

| Kode Inovasi | Nama Inovasi | Kompleksitas | Dampak Bisnis | Prioritas | Fase Rekomendasi |
|---|---|---|---|---|---|
| **INV-REC-01** | Backup Otomatis Berkala | Rendah | Tinggi | High | Bulan ke-6 |
| **INV-REC-02** | Notifikasi WA Template | Rendah | Sedang | Medium | Bulan ke-5 |
| **INV-REC-03** | Prediksi Re-Order Stok | Sedang | Tinggi | High | Bulan ke-9 |
| **INV-NEW-01** | Dashboard Ringkasan CLI | Rendah | Tinggi | High | Bulan ke-6 |
| **INV-NEW-02** | Price Tracking Supplier | Sedang | Tinggi | Medium | Bulan ke-7 |
| **INV-NEW-03** | Alert Jatuh Tempo Utang | Sedang | Tinggi | High | Bulan ke-10 |
| **INV-NEW-04** | Shift Handover Log | Rendah | Sedang | Medium | Bulan ke-6 |
| **INV-NEW-05** | Margin Profit per Produk | Sedang | Tinggi | Medium | Bulan ke-10 |
| **INV-NEW-06** | Fraud Detection Sederhana | Tinggi | Tinggi | High | Bulan ke-10 |
| **INV-NEW-07** | Template Cetak Teks | Rendah | Sedang | Medium | Bulan ke-5 |
| **INV-NEW-08** | Import CSV Semiautomatis | Sedang | Tinggi | High | Bulan ke-5 |
| **INV-NEW-09** | Runtime Config Dinamis | Sedang | Tinggi | High | Bulan ke-9 |

### 6.3. Prioritasi Implementasi Inovasi

Prioritasi diurutkan berdasarkan kuadran kelayakan (Urgensi Operasional vs Dampak Bisnis):
1. **Prioritas Utama (Urgensi Tinggi / Dampak Tinggi)**:
   * **INV-NEW-08 (Import CSV)**: Wajib dibangun di awal (Bulan 5) untuk mendukung setup data awal yang bersih.
   * **INV-NEW-01 (Dashboard CLI)**: Disediakan saat menu utama selesai (Bulan 6) agar pemilik langsung memiliki visibilitas.
   * **INV-REC-01 (Backup Otomatis)**: Sebagai pelindung data harian selama fase implementasi berlangsung.
2. **Prioritas Kedua (Urgensi Sedang / Dampak Tinggi)**:
   * **INV-NEW-09 (Runtime Config)**: Dibangun paralel pada Bulan 9 untuk mempermudah parameterisasi modul HPP dan payroll.
   * **INV-REC-03 (Prediksi Re-Order)**: Digabungkan dengan implementasi modul inventaris akhir (Bulan 9).
3. **Prioritas Ketiga (Urgensi Rendah / Dampak Tinggi)**:
   * **INV-NEW-03 (Alert Jatuh Tempo)** & **INV-NEW-06 (Fraud Detection)**: Diimplementasikan pada fase akhir keuangan dan audit trail (Bulan 10).

---

## 7. Pemetaan Inovasi terhadap Modul Sistem

Matriks di bawah ini menunjukkan relasi pemetaan antara setiap inovasi (baris) dengan 9 Modul Utama AbuCom (kolom):

* **Keterangan Legenda Modul**:
  * **M.1**: Modul Manajemen Transaksi & Kebijakan Harga
  * **M.2**: Modul Manajemen Inventaris, BOM & Stock Opname
  * **M.3**: Modul Keuangan Digital, PPOB, Jasa Keuangan & Service
  * **M.4**: Modul Manajemen SDM, Penggajian & Poin Karyawan
  * **M.5**: Modul Sistem Manajemen Antrian & Pelacakan Desain
  * **M.6**: Modul Administrasi Pinjaman, Aset, & Pengeluaran Rutin
  * **M.7**: Modul Keamanan, Audit Trail & Hak Akses
  * **M.8**: Modul Pembatalan, Retur & CRM
  * **M.9**: Modul Skalabilitas Multi-Cabang

| Kode Inovasi | M.1 | M.2 | M.3 | M.4 | M.5 | M.6 | M.7 | M.8 | M.9 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **INV-INT-01** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **INV-INT-02** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| **INV-INT-03** | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — |
| **INV-INT-04** | ✓ | ✓ | — | — | — | — | — | — | — |
| **INV-INT-05** | — | ✓ | — | — | ✓ | — | — | — | — |
| **INV-INT-06** | — | ✓ | — | — | — | — | — | — | — |
| **INV-INT-07** | — | ✓ | — | — | — | ✓ | — | — | — |
| **INV-INT-08** | — | ✓ | — | — | — | — | — | — | — |
| **INV-INT-09** | — | — | — | ✓ | — | — | — | — | — |
| **INV-INT-10** | — | — | — | ✓ | — | — | — | — | — |
| **INV-INT-11** | — | — | — | ✓ | — | — | — | — | — |
| **INV-INT-12** | — | — | — | — | ✓ | — | — | — | — |
| **INV-INT-13** | — | — | — | — | ✓ | — | — | — | — |
| **INV-INT-14** | — | — | — | — | — | — | — | ✓ | — |
| **INV-INT-15** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| **INV-INT-16** | — | — | — | — | — | — | ✓ | — | — |
| **INV-INT-17** | — | — | — | — | — | — | ✓ | — | — |
| **INV-INT-18** | — | — | — | — | — | — | ✓ | — | — |
| **INV-INT-19** | — | — | — | — | — | — | ✓ | — | — |
| **INV-INT-20** | — | — | — | — | — | — | ✓ | — | — |
| **INV-INT-21** | — | — | — | — | — | — | ✓ | — | — |
| **INV-INT-22** | ✓ | — | — | — | — | — | — | — | — |
| **INV-INT-23** | ✓ | — | — | — | — | — | — | — | — |
| **INV-INT-24** | ✓ | ✓ | — | — | — | — | — | ✓ | — |
| **INV-INT-25** | — | — | — | — | — | — | ✓ | — | — |
| **INV-INT-26** | — | — | — | — | — | ✓ | — | — | — |
| **INV-REC-01** | — | — | — | — | — | — | ✓ | — | — |
| **INV-REC-02** | — | — | — | — | ✓ | — | — | ✓ | — |
| **INV-REC-03** | — | ✓ | — | — | — | — | — | — | — |
| **INV-NEW-01** | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — |
| **INV-NEW-02** | — | ✓ | — | — | — | — | — | — | — |
| **INV-NEW-03** | — | — | — | — | — | ✓ | — | — | — |
| **INV-NEW-04** | — | — | — | — | — | — | ✓ | — | — |
| **INV-NEW-05** | ✓ | — | — | — | — | — | — | — | — |
| **INV-NEW-06** | — | — | — | — | — | — | ✓ | — | — |
| **INV-NEW-07** | — | — | — | — | — | ✓ | — | — | — |
| **INV-NEW-08** | — | ✓ | — | — | — | — | ✓ | — | — |
| **INV-NEW-09** | ✓ | ✓ | — | ✓ | — | — | — | — | — |

---

## 8. Dampak Inovasi terhadap Fase SDLC Selanjutnya

### 8.1. Dampak terhadap Requirements (SRS)
1. **Peningkatan Rincian Fitur**: Setiap usulan inovasi (terutama 9 rekomendasi baru) wajib diuraikan secara detail menjadi daftar kebutuhan fungsional (FR) dan kebutuhan non-fungsional (NFR) spesifik per modul.
2. **Kriteria Input/Output**: Kebutuhan data input untuk import CSV (format file, delimiter) dan konfigurasi dinamis (tipe data parameter) harus dicantumkan di SRS tanpa ambiguitas.

### 8.2. Dampak terhadap Design (SDD & ERD)
1. **Perubahan ERD Basis Data**: Struktur ERD basis data MySQL wajib memuat tabel-tabel baru untuk mendukung inovasi:
   * Tabel `audit_logs` (log Audit Trail)
   * Tabel `system_configs` (konfigurasi dinamis)
   * Tabel `supplier_prices` (price tracking)
   * Tabel `shift_handover_logs` (serah terima shift)
2. **Skema Imutabilitas di SDD**: SDD harus merincikan alur logika passing state dan nested closures di Python untuk mensimulasikan manajemen state tanpa OOP.

### 8.3. Dampak terhadap Implementation
1. **Boilerplate Tambahan**: Pengembang harus membuat modul parser CSV dan modul logger audit trail di awal bulan ke-5 sebagai dependensi yang digunakan modul operasional.
2. **Disiplin Paradigma FP**: Penulisan fungsi HPP BOM desimal dan margin profit wajib bersih dari *side-effects* serta menggunakan modul `decimal` bawaan Python.

### 8.4. Dampak terhadap Testing (UAT)
1. **Skenario Uji Khusus**: Rencana pengujian wajib memuat skenario uji kasus anomali (*fraud testing*), simulasi pemadaman listrik (transaksi rollback), simulasi kegagalan parsing CSV, dan uji pembatasan menu RBAC.
2. **Simulasi Shift Handover**: Pengujian serah terima shift fisik kasir wajib disimulasikan secara langsung selama UAT oleh staf kasir baru.

---

## 9. Risiko Inovasi dan Rencana Mitigasi

Berikut adalah identifikasi risiko terkait usulan inovasi, probabilitas (1-5), dampak (1-5), serta rencana mitigasinya:

| No | Risiko Inovasi | Probabilitas | Dampak | Rencana Mitigasi |
|----|----------------|:------------:|:------:|------------------|
| 1  | **Scope Creep Akibat Inovasi Baru**: Penambahan fitur visual `rich` dan sistem deteksi fraud yang berlebihan memperpanjang durasi coding melebihi batas 12 bulan. | 3 | 4 | Tetapkan batas ruang lingkup inovasi baru yang rigid pada SRS; tunda inovasi prioritas rendah (seperti deteksi fraud rumit) ke fase pemeliharaan pasca go-live. |
| 2  | **FP Python Menghambat Logika Dinamis**: Ketiadaan class OOP menyulitkan programer junior mengimplementasikan konfigurasi dinamis atau log shift handover secara fungsional. | 2 | 4 | Siapkan template fungsi pembungkus state (*state pass wrapper*) oleh Claude Sonnet 4.6 di awal sprint sebagai acuan penulisan modul operasional. |
| 3  | **Staf Menolak Menu CLI ANSI**: Karyawan baru merasa kebingungan menatap layar teks terminal dan menuntut tampilan aplikasi GUI tablet modern. | 4 | 3 | Optimalkan pewarnaan ANSI menu CLI menggunakan panel `rich` untuk meniru visual kotak GUI, serta sediakan program pelatihan simulasi 3 hari. |
| 4  | **Latensi Query Laporan Margin**: Agregasi data HPP BOM desimal secara rekursif memperlambat performa respons CLI laporan keuangan tahunan. | 2 | 3 | Gunakan indeks relasional database MySQL yang optimal pada kolom transaksi dan buat *view* database khusus untuk mempercepat penarikan data margin. |
| 5  | **Kerusakan Data saat Setup CSV**: Struktur data pada file Excel lama pemilik tidak bersih (banyak baris kosong/typo) saat diimpor via modul CSV. | 4 | 4 | Buat fungsi parser fungsional yang dilengkapi logger error baris data yang gagal diimpor, sehingga staf gudang tahu data mana yang perlu diperbaiki. |

---

## 10. Persetujuan dan Otorisasi

Lembar otorisasi ini menandai persetujuan formal pemilik usaha terhadap usulan inovasi yang didokumentasikan untuk dilanjutkan ke fase requirements (SRS):

| Pihak Penandatangan | Jabatan/Peran | Tanda Tangan | Tanggal Persetujuan |
|---------------------|---------------|--------------|---------------------|
| Pemilik Usaha AbuCom | Sponsor Utama & Manajer Proyek | *(Menunggu Persetujuan Digital)* | *(Belum disetujui)* |
| Tim Pengembang AI | Lead Innovation Analyst | *(Menunggu Persetujuan Digital)* | *(Belum disetujui)* |

---

## 11. Glosarium

1. **Innovation Proposal**: Dokumen resmi perencanaan yang memotret usulan peningkatan sistem berbasis praktik terbaik industri.
2. **Best Practice**: Praktik atau metode terbaik yang teruji secara industri untuk menyelesaikan suatu permasalahan operasional/teknis.
3. **Scope Creep**: Penambahan fitur atau ruang lingkup proyek secara tidak terkendali di luar perencanaan yang disetujui, berpotensi menunda jadwal.
4. **Bill of Materials (BOM)**: Daftar komposisi bahan baku beserta takaran spesifik yang dibutuhkan untuk memproduksi satu unit produk cetak kustom.
5. **Harga Pokok Penjualan (HPP)**: Akumulasi biaya langsung (bahan baku, biaya limbah) yang dikeluarkan untuk menghasilkan produk/jasa yang terjual.
6. **Down Payment (DP)**: Pembayaran uang muka di awal transaksi sebagai tanda jadi sebelum pesanan kustom mulai diproduksi.
7. **Audit Trail**: Catatan log kronologis terotomatisasi yang mendokumentasikan rincian aktivitas pengguna di database demi keamanan.
8. **Role-Based Access Control (RBAC)**: Metode pembatasan otorisasi menu aplikasi berdasarkan peran/posisi jabatan staf yang terdaftar.
9. **JSON Web Token (JWT)**: Standar terbuka (RFC 7519) untuk pengiriman data session terenkripsi secara aman dan stateless antar client-server.
10. **bcrypt**: Algoritma enkripsi satu arah berbasis Blowfish cipher yang lambat dan aman, khusus untuk menyimpan kata sandi pengguna.
11. **Waste Management**: Metode pencatatan persentase bahan rusak/limbah cetak produksi untuk menjaga akurasi stok gudang.
12. **Unit of Measure (UoM)**: Spesifikasi satuan ukur standar yang digunakan untuk mencatat kuantitas barang persediaan (rim, ml, lembar, dll).
13. **Stock Opname**: Kegiatan pencocokan kuantitas stok barang fisik di gudang terhadap catatan saldo stok di aplikasi sistem secara berkala.
14. **PPOB (Payment Point Online Bank)**: Layanan pembayaran tagihan bulanan (listrik, air, BPJS) dan pembelian pulsa virtual secara digital.
15. **Cash Reconciliation**: Formulir pencocokan fisik uang tunai di laci kasir terhadap saldo kas yang tercatat dalam sistem pada akhir shift.
16. **Runtime Config**: Metode pengaturan konfigurasi aturan bisnis sistem secara dinamis di database tanpa merubah kode program.
17. **Price Tracking**: Fitur pelacakan riwayat fluktuasi harga beli barang dari vendor/supplier untuk efisiensi biaya pengadaan.
18. **Fraud Detection**: Logika pendeteksi pola transaksi anomali atau mencurigakan guna mencegah kecurangan kas internal.

---

## 12. Referensi Dokumen

Daftar dokumen acuan resmi yang digunakan dalam penyusunan Innovation Proposal ini:

| # | Nama File | Lokasi Path Relatif | Keterangan Penggunaan |
|---|---|---|---|
| 1 | `01_project_charter.md` | [01_project_charter.md](docs/sdlc/01_planning/01_project_charter.md) | Visi utama, ruang lingkup 9 modul, kebutuhan fungsional/non-fungsional, manfaat terukur, susunan tim pengembang AI. |
| 2 | `02_feasibility_study.md` | [02_feasibility_study.md](docs/sdlc/01_planning/02_feasibility_study.md) | Analisis kelayakan teknis per modul, evaluasi kelayakan finansial (ROI, NPV, Payback), risiko proyek. |
| 3 | `03_stakeholder_register.md` | [03_stakeholder_register.md](docs/sdlc/01_planning/03_stakeholder_register.md) | Hak akses RBAC per posisi staf, matriks modul vs stakeholder, regulasi PKWT/PKWTT ketenagakerjaan Indonesia. |
| 4 | `04_tech_stack_decision.md` | [04_tech_stack_decision.md](docs/sdlc/01_planning/04_tech_stack_decision.md) | Keputusan driver database, pustaka otentikasi (JWT/bcrypt), model portabilitas OS, unit testing FP. |
| 5 | `narasi.txt` | [narasi.txt](docs/sdlc/narasi.txt) | Alur kerja manual excel pemilik, rincian 5 divisi usaha, mandat inovasi Baris 98. |

