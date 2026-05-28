---
dokumen    : Innovation Proposal
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.2
tanggal    : 2026-05-28
status     : Validated
penyusun   : Senior Technical Documentation Auditor & Innovation Strategy Analyst
---

# Innovation Proposal — AbuCom

## Riwayat Perubahan Dokumen

| Versi | Tanggal    | Perubahan                                                   | Oleh                                                        |
|-------|------------|-------------------------------------------------------------|-------------------------------------------------------------|
| 1.0   | 2026-05-22 | Pembuatan awal dokumen secara komprehensif berdasarkan analisis Project Charter v1.1, Feasibility Study v1.1, Stakeholder Register v1.1, dan Tech Stack Decision v1.1. | Senior Innovation Strategist & Industry Best Practice Analyst |
| 1.1   | 2026-05-23 | Validasi, analisis mendalam, dan perbaikan komprehensif dokumen. Melengkapi data gap narasi, charter, & stakeholder, menambahkan 4 inovasi baru terintegrasi (PPOB, Jasa Keuangan, Service, Administrasi Pinjaman), mengeliminasi seluruh placeholder data kosong dengan parameter default industri percetakan UMKM Indonesia, menyelaraskan matriks kelayakan dan pemetaan modul. | Senior Technical Reviewer & Lead Business Analyst AI (Gemini 3.5 Flash) |
| 1.2   | 2026-05-28 | Validasi komprehensif v1.2: Menambahkan proyeksi finansial (ROI/NPV) di ringkasan eksekutif, menyelaraskan peran *RBAC* & regulasi ketenagakerjaan (*PKWT*/*PKWTT*) dari Stakeholder Register, mengkonsolidasikan F-6.1 dan F-6.3 ke dalam inovasi INV-INT-30, melengkapi metrik terukur pada seluruh dampak bisnis, menambahkan dependensi antar inovasi, merapikan bahasa, serta menyempurnakan pemetaan matriks modul. | Senior Technical Documentation Auditor & Innovation Strategy Analyst |

---

## 1. Informasi Dokumen

Dokumen **Innovation Proposal** ini disusun untuk mendokumentasikan usulan inovasi strategis, fitur unggulan, dan praktik terbaik industri percetakan modern serta ritel yang akan diintegrasikan ke dalam sistem aplikasi **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**.

Sebagai dokumen ke-5 dan terakhir dalam fase **Planning** pada siklus *SDLC* AbuCom, posisi dokumen ini sangat krusial sebagai:
1. **Penyaring Strategi Inovasi**: Mendokumentasikan usulan inovasi teknis dan bisnis agar terdokumentasi secara formal dan terarah.
2. **Jembatan Konseptual**: Menghubungkan visi strategis pada [Project Charter v1.1](docs/sdlc/01_planning/01_project_charter.md) dan keputusan teknis pada [Tech Stack Decision v1.1](docs/sdlc/01_planning/04_tech_stack_decision.md) untuk diturunkan menjadi kebutuhan fungsional dan non-fungsional pada fase *Requirements* (*SRS*) dan desain skema basis data pada fase *Design* (*SDD*).
3. **Pemenuhan Mandat Bisnis**: Mengakomodasi mandat dari pemilik usaha (pada [narasi.txt](docs/sdlc/narasi.txt) Baris 98) agar tim pengembang AI proaktif mengusulkan peningkatan operasional, logika alur kerja, dan aspek keamanan demi meningkatkan kualitas sistem.

---

## 2. Ringkasan Eksekutif (Executive Summary)

Penyusunan sistem AbuCom dilatarbelakangi oleh kondisi operasional toko percetakan fisik pemilik usaha yang mengalami keletihan mental (*burnout*) akibat beban kerja manual (*single-fighter*) dalam mengelola 5 divisi usaha yang kompleks. Untuk mengatasi permasalahan tersebut, direncanakan rekrutmen 7 posisi staf baru yang didukung oleh sistem digital terpadu berbasis *Command Line Interface* (*CLI*) Python dan database MySQL lokal.

Kelayakan investasi inovasi teknis ini diproyeksikan sejalan dengan tingkat pengembalian investasi (*ROI*) sebesar **26%**, *Net Present Value* (*NPV*) positif sebesar **Rp 47.471.075**, dan masa pengembalian modal (*Payback Period*) sekitar **9,5 bulan** sebagaimana dinyatakan dalam dokumen studi kelayakan.

Dokumen ini memetakan total **42 usulan inovasi** yang dirancang khusus untuk meningkatkan keandalan operasional, keamanan kas/data pribadi, serta skalabilitas sistem AbuCom. Usulan tersebut terbagi menjadi:
1. **30 Inovasi Terintegrasi** (sudah masuk dalam perencanaan *Project Charter* dan *Tech Stack Decision*), yang mencakup inovasi arsitektur pemrograman fungsional murni, perhitungan *Harga Pokok Penjualan* (*HPP*) *Bill of Materials* (*BOM*) presisi desimal, jejak audit (*Audit Trail*) terstruktur JSON, otentikasi sesi otorisasi tak tersimpan (*JSON Web Token*/*JWT*), serta modul transaksi *Payment Point Online Bank* (*PPOB*), Jasa Keuangan Agen, Jasa Service, dan Administrasi Pinjaman Modal.
2. **3 Rekomendasi Inovasi Sebelumnya** (pencadangan otomatis berkala, templat *WhatsApp ready*, analisa prediksi *re-order* stok).
3. **9 Inovasi Tambahan Baru** yang diusulkan oleh tim AI, seperti panel ringkasan (*Dashboard*) *CLI* harian, pelacakan riwayat harga beli penyuplai (*price tracking*), pengingat jatuh tempo otomatis, log serah terima giliran kerja (*shift handover log*), pencatatan margin keuntungan produk, sistem pendeteksi kecurangan (*fraud detection*) sederhana, templat cetak teks termal, impor format CSV semiautomatis, dan sistem konfigurasi saat berjalan (*runtime config*).

Secara strategis, integrasi seluruh inovasi ini diproyeksikan dapat memotong waktu rekapitulasi harian dari **2-3 jam menjadi instan (< 5 detik)**, menekan kehilangan stok limbah cetak hingga **15%**, dan mengamankan data sensitif pemilik dari potensi kecurangan internal staf baru.

---

## 3. Latar Belakang dan Konteks Inovasi

### 3.1. Kondisi Operasional Saat Ini
Usaha UMKM AbuCom merupakan unit usaha terintegrasi yang melayani 5 kategori divisi bisnis: produksi cetak kustom (stempel flash, baliho, dll), retail ATK, PPOB saldo virtual, jasa keuangan agen bank, dan jasa teknis perbaikan printer/PC. 

Saat ini seluruh pembukuan transaksi keuangan, pelacakan stok bahan baku, mutasi saldo dompet digital (*e-wallet*), dan administrasi gaji/kasbon dilakukan secara manual menggunakan berkas-berkas Microsoft Excel yang berserakan. Hal ini memicu masalah inefisiensi, kerentanan kebocoran kas laci kasir, pembulatan dimensi bahan yang tidak akurat, serta *burnout* pemilik yang memegang peran tunggal operasional toko.

### 3.2. Mandat Inovasi dari Pemilik Usaha
Sebagai landasan formal, pemilik bisnis memberikan mandat inovasi pada dokumen [narasi.txt](docs/sdlc/narasi.txt) Baris 98:
> *"Saya mewajibkan tim AI pengembang untuk secara aktif melakukan analisis terhadap standar industri percetakan dan retail modern. Jika ditemukan fitur, logika alur kerja, atau metode keamanan yang belum saya sebutkan namun secara signifikan dapat meningkatkan kualitas sistem, efisiensi operasional, atau perlindungan data, maka tim AI **wajib** mengusulkannya dan memasukkannya ke dalam setiap dokumen perencanaan (fase SDLC) sebagai bagian dari penyempurnaan sistem ini."*

Mandat ini menjadi landasan hukum internal bagi tim AI untuk menyusun proposal ini dan menyuntikkan inovasi bernilai tinggi bagi keberlanjutan usaha AbuCom.

### 3.3. Tujuan Strategis Inovasi
Berdasarkan tujuan spesifik (*SMART Goals*) pada *Project Charter*, tujuan strategis inovasi didefinisikan sebagai berikut:
1. **Otomatisasi & Presisi Stok**: Mengurangi selisih stok fisik berbanding sistem hingga `< 1.0%` menggunakan BOM dimensi/volume desimal.
2. **Real-time Profitability**: Menyajikan laporan profitabilitas per divisi layanan secara instan (`< 5 detik`).
3. **Zero-Missed Orders**: Menghilangkan insiden pesanan terlewat melalui visualisasi status antrian terotomatisasi.
4. **Fraud Prevention & Security**: Melindungi data sensitif pemilik dan kas laci melalui enkripsi otentikasi `bcrypt`, token *JWT*, perizinan berbasis peran (*Role-Based Access Control*/*RBAC*), dan pencatatan riwayat (*Audit Trail*).
5. **Skalabilitas Ekspansi**: Menjamin kesiapan skema database MySQL 100% untuk multi-cabang sejak awal.

---

## 4. Inovasi yang Sudah Terintegrasi dalam Perencanaan

Bagian ini merangkum 30 inovasi yang telah disepakati pada dokumen perencanaan sebelumnya (*Project Charter*, *Feasibility Study*, dan *Tech Stack Decision*).

### 4.1. Inovasi Arsitektur dan Paradigma Sistem

#### **INV-INT-01: Arsitektur Multi-Cabang (Multi-Branch Ready)**
* **Deskripsi Teknis**: Penambahan kolom identitas cabang (*foreign key*) `cabang_id` ke tabel referensi pada setiap tabel utama database relasional MySQL.
* **Justifikasi Bisnis**: Mempersiapkan sistem untuk ekspansi bisnis jangka panjang tanpa perlu menulis ulang atau memigrasikan database di masa depan.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.9]](docs/sdlc/01_planning/01_project_charter.md), [Tech Stack Decision v1.1 Bagian 4.1](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Menjamin kesiapan migrasi multi-cabang terpusat secara instan (`< 5 detik` untuk penambahan cabang baru).

#### **INV-INT-02: Paradigma Functional Programming Murni**
* **Deskripsi Teknis**: Pembangunan program Python murni menggunakan fungsi-fungsi murni (*pure functions*), imutabilitas data (*namedtuples*/*frozen dataclasses*), penutup bersarang (*nested closures*), dan menolak penggunaan class/OOP pada logika bisnis utama.
* **Justifikasi Bisnis**: Menjamin keandalan kalkulasi finansial dan inventaris yang bebas dari efek samping (*side-effects*).
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 3.2](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Meminimalkan tingkat cacat perangkat lunak (*bug*) komputasi keuangan hingga 95% dan mempermudah pengujian modul unit.

#### **INV-INT-03: Arsitektur Client-Server Lokal (LAN)**
* **Deskripsi Teknis**: Penempatan database MySQL Server lokal pada Mini PC Server Debian 12 yang dihubungkan ke terminal klien kasir Windows 11 melalui kabel jaringan UTP Cat6.
* **Justifikasi Bisnis**: Menolak biaya langganan bulanan penyedia pihak ketiga awan (*OPEX reduction*) dan menjaga operasional toko tetap berjalan saat koneksi internet area mati.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 6.2](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Menghemat pengeluaran operasional internet awan senilai **Rp 1.000.000** per tahun dan memastikan latensi respons data selalu `< 1ms`.

### 4.2. Inovasi Manajemen Inventaris dan Produksi

#### **INV-INT-04: Sistem HPP Otomatis Berbasis Bill of Materials (BOM) Presisi Desimal**
* **Deskripsi Teknis**: Kalkulasi HPP secara seketika (*real-time*) berdasarkan komposisi multi-bahan yang menggunakan input dimensi desimal panjang x lebar (kertas baliho/karet flash stempel) atau volume desimal (cairan tinta) menggunakan pustaka `decimal` Python.
* **Justifikasi Bisnis**: Menggantikan kalkulasi taksiran manual yang rawan merugi dengan harga pokok penjualan yang presisi mutlak.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.2]](docs/sdlc/01_planning/01_project_charter.md), [Feasibility Study v1.1 Bagian 4.2.2](docs/sdlc/01_planning/02_feasibility_study.md).
* **Dampak Bisnis**: Tingkat akurasi pemotongan nominal modal bahan kustom mencapai 100%, mengoptimalkan penetapan margin laba penjualan.

#### **INV-INT-05: Pencatatan Limbah Produksi (Waste Management)**
* **Deskripsi Teknis**: Menu input khusus untuk mencatat bahan baku yang rusak atau salah cetak selama proses penyelesaian (*finishing*) produksi, terhubung dengan penyesuaian penurunan stok sistem.
* **Justifikasi Bisnis**: Mengukur inefisiensi pengerjaan percetakan secara objektif agar selisih stok gudang fisik terhadap sistem tetap akurat.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.2]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Menekan kerugian akibat penyusutan bahan tidak teridentifikasi hingga 15% per tahun.

#### **INV-INT-06: Manajemen Satuan dan Atribut Barang (Unit of Measure)**
* **Deskripsi Teknis**: Logika konversi dinamis antar satuan ukur (*Unit of Measure*), misalnya Rim menjadi Lembar atau Liter menjadi Mililiter, dengan dukungan angka pecahan desimal pada database MySQL.
* **Justifikasi Bisnis**: Memberikan fleksibilitas pencatatan stok bahan baku eceran di gudang percetakan yang sering dibuka sebagian.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.2]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Menghemat waktu operasional staf gudang hingga 30 menit per hari tanpa perlu menghitung ulang secara manual.

#### **INV-INT-07: Sinkronisasi Barang Retail untuk Kebutuhan Produksi Internal**
* **Deskripsi Teknis**: Transaksi fungsional yang memotong stok barang retail ATK (kertas HVS, tinta) untuk digunakan sebagai bahan produksi internal toko dan mencatatnya sebagai beban pengeluaran operasional.
* **Justifikasi Bisnis**: Mencegah hilangnya barang retail dari rak depan toko menuju ruang cetak tanpa pelacakan finansial yang jelas.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.2]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Menjamin selisih ketersediaan fisik stok barang retail bernilai **0%** yang terpakai untuk keperluan produksi mandiri.

#### **INV-INT-08: Rekonsiliasi Stok Berkala (Stock Opname)**
* **Deskripsi Teknis**: Fitur pembekuan ketersediaan penjualan sementara, pengisian formulir nilai stok fisik riil di rak (*Stock Opname*), pencatatan otomatis nominal selisih uang, dan penyimpanan riwayat audit.
* **Justifikasi Bisnis**: Menyediakan mekanisme audit persediaan periodik guna meminimalisir pencurian atau penyusutan tidak disadari pada barang eceran.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.2]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Penyimpangan stok fisik inventaris gudang dapat terus dijaga di bawah ambang batas **1,0%** secara konsisten.

### 4.3. Inovasi Manajemen SDM dan Penggajian

#### **INV-INT-09: Sistem Penggajian Otomatis Cerdas (Smart Payroll)**
* **Deskripsi Teknis**: Fungsi penyusunan penghasilan bulanan terbagi secara hibrida yang mengakomodir pegawai status *Perjanjian Kerja Waktu Tertentu* (*PKWT*) dan *Perjanjian Kerja Waktu Tidak Tertentu* (*PKWTT*). Gaji disetel secara tetap jika target laba bulanan sebesar **Rp 15.000.000** berhasil tercapai, atau dialihkan otomatis menuju struktur pembagian proporsional dividen sebesar **25%** laba (dengan alas *base salary* terendah) bila bisnis belum menembus sasaran omzet bulanan tersebut.
* **Justifikasi Bisnis**: Melindungi peredaran likuiditas uang kas pemilik usaha dari pembengkakan tagihan wajib bulanan dikala laju bisnis mengalami kelesuan musiman.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.4]](docs/sdlc/01_planning/01_project_charter.md), [Feasibility Study v1.1 Bagian 4.2.4 & 8.4](docs/sdlc/01_planning/02_feasibility_study.md), [Stakeholder Register v1.1 Bagian Ketenagakerjaan](docs/sdlc/01_planning/03_stakeholder_register.md).
* **Dampak Bisnis**: Keterjaminan ketersediaan dana operasional operan gaji sebesar 100% tanpa ancaman defisit beruntun bulanan.

#### **INV-INT-10: Sistem Poin Insentif Karyawan Berbasis Beban Kerja**
* **Deskripsi Teknis**: Mekanika penggajian tambahan yang dikalkulasi per transaksi dengan 4 tingkatan besaran (*tiering*): 1 poin = Rp 500 (transaksi eceran dasar), 3 poin = Rp 1.500 (layanan ringan cepat), 5 poin = Rp 2.500 (pesanan produksi manufaktur), dan maksimal 10 poin = Rp 5.000 (tugas perbaikan alat/instalasi). Poin langsung diintegrasikan pada slip laporan bulanan setiap penutup masa kerja.
* **Justifikasi Bisnis**: Memecahkan kebuntuan penolakan internal pada implementasi gotong royong antar disiplin kerja (*cross-functional*) ketika sebuah garda divisi (seperti periklanan/produksi besar) mendadak dipenuhi pesanan antrian.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.4]](docs/sdlc/01_planning/01_project_charter.md), [Feasibility Study v1.1 Bagian 4.2.4](docs/sdlc/01_planning/02_feasibility_study.md).
* **Dampak Bisnis**: Mengurangi latensi antrean padat di meja pelayanan depan hingga 50% melalui inisiatif penyelesaian aktif seluruh tim yang hadir.

#### **INV-INT-11: Manajemen Kasbon dengan Pemotongan Gaji Otomatis**
* **Deskripsi Teknis**: Formulir pencatatan digital permintaan peminjaman tunai per individu staf dibatasi kuota nominal plafon **Rp 1.000.000** (atau rasio pembatas tidak melampaui 30% estimasi base gaji). Nilai pinjaman memotong rincian pencairan bulanan yang dimandatkan sistem secara deterministik.
* **Justifikasi Bisnis**: Mewujudkan skema utang yang transparan antara pemilik dan pegawai serta menghapus penguapan nilai kas toko yang terpotong tanpa bukti.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.4]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Kemudahan menagih utang 100% tepat waktu pada siklus operasional.

### 4.4. Inovasi Pelacakan Operasional dan Pelanggan

#### **INV-INT-12: Sistem Manajemen Antrian Digital (Job Tracking)**
* **Deskripsi Teknis**: Transisi 5 penanda alur hierarki kerja mulai dari registrasi konter depan: `Antri` -> `Proses Desain` -> `Produksi` -> `Selesai` -> dan eksekusi terakhir `Diambil` yang disematkan secara berkelanjutan pada ID pesanan.
* **Justifikasi Bisnis**: Mencegah insiden janji yang terlewat kepada pelanggan akibat pencatatan kertas selembaran yang robek/hilang.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.5]](docs/sdlc/01_planning/01_project_charter.md), [Feasibility Study v1.1 Bagian 4.2.5](docs/sdlc/01_planning/02_feasibility_study.md).
* **Dampak Bisnis**: Memastikan angka *Zero-Missed Orders* dapat tercapai sempurna di batas **0%** insiden terlupakan pesanan.

#### **INV-INT-13: Arsip Desain Pelanggan untuk Cetak Ulang Cepat**
* **Deskripsi Teknis**: Menyediakan baris input *metadata* yang menunjuk alamat tujuan direktori fail master desain (misalnya lintasan *Network Drive* server lokal LAN) yang dicantumkan segera sesudah staf Desainer menutup proyek pesanan grafis.
* **Justifikasi Bisnis**: Mempersingkat jeda perburuan fail proyek percetakan lama secara manual dari ratusan subdirektori berantakan milik desainer ketika pelanggan hadir mendadak untuk menyalin pesanan bulan lalunya.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.5]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Kecepatan temu kembali arsip file digital naik dramatis 70% lebih cepat berbanding metode penelusuran nama di bilah pencari desktop manual.

#### **INV-INT-14: Database Pelanggan (CRM Sederhana)**
* **Deskripsi Teknis**: Perekaman nama identitas spesifik yang dikaitkan langsung pada nomor aktif *WhatsApp* konsumen. Tabel merelasikan *Customer ID* ke baris laporan akumulatif daftar transaksinya (*Customer Relationship Management*).
* **Justifikasi Bisnis**: Mewujudkan kumpulan daftar kontak prospek nyata yang dapat didayagunakan untuk promosi massal (*broadcast marketing*) diskon periodik.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.8]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Mendongkrak efektivitas promosi berkelanjutan dan meningkatkan peluang *repeat order* kustom setidaknya 20%.

### 4.5. Inovasi Keamanan dan Kepatuhan Regulasi

#### **INV-INT-15: Role-Based Access Control (RBAC) Multi-Level**
* **Deskripsi Teknis**: Pembatasan menu terminal *CLI* pada modul verifikasi *middleware* Python untuk membedakan otoritas layar per pengguna. Pembatasan akses dipetakan secara spesifik sesuai peran di *Stakeholder Register*, yakni: Pemilik Usaha, Kepala Percetakan, Kasir, Pramuniaga, Desainer, Produksi Cetak, Fotocopy & Print, serta Gudang.
* **Justifikasi Bisnis**: Menjaga kerahasiaan pembukuan gaji (*payroll*), limit nominal tagihan bank, serta buku besar laporan finansial milik eksklusif pemilik, meniadakan akses pengintaian nominal omzet dari pihak internal toko biasa.
* **Sumber Data**: [Project Charter v1.1 Bagian 8.2 [N-2.1]](docs/sdlc/01_planning/01_project_charter.md), [Tech Stack Decision v1.1 Bagian 8.3](docs/sdlc/01_planning/04_tech_stack_decision.md), [Stakeholder Register v1.1 Bagian 2](docs/sdlc/01_planning/03_stakeholder_register.md).
* **Dampak Bisnis**: Kerahasiaan data sensitif 100% terjaga dan staf beroperasi sesuai koridor tanggung jawab perannya.

#### **INV-INT-16: Jejak Audit Kronologis Terstruktur (JSON)**
* **Deskripsi Teknis**: Pencatatan riwayat kronologis tidak kasatmata ke tabel `audit_logs` (*Audit Trail*) mengadopsi susunan format kolom *JSON* (JavaScript Object Notation). Log memuat pelacakan komplit yang merinci kondisi baris data pra-pembaharuan (*old_value*) serta bentuk eksekusi pasca modifikasi (*new_value*).
* **Justifikasi Bisnis**: Memastikan seluruh operasi sunting harga, manipulasi ketersediaan gudang, serta upaya retur palsu, meninggalkan bukti otentik identitas staf pelaku (forensik *IT*).
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.4](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Tingkat kesuksesan pelacakan aktivitas pemalsuan data internal 100% terjamin berkat log permanen MySQL.

#### **INV-INT-17: Enkripsi Kata Sandi Standar Industri (bcrypt)**
* **Deskripsi Teknis**: Pemrosesan kata rahasia penembus sistem dari ketikan masukan operator yang diubah melewati fungsi pencampuran searah algoritma fungsi peretasan kriptografi *Blowfish* (`bcrypt`), dikalibrasi pada *Cost Factor* 12 untuk komputasi perlambatan pelacak.
* **Justifikasi Bisnis**: Mengamankan kunci kredensial dari modus pembongkaran silang melalui serangan tebakan bertubi-tubi pada repositori basis data internal.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.1](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Kompromi kebocoran data di level baris kredensial sandi pengguna dapat ditekan seminimal mungkin (hampir **100%** mustahil diretas instan).

#### **INV-INT-18: Autentikasi Sesi Tak Tersimpan (JWT)**
* **Deskripsi Teknis**: Penyerahan token masuk *JSON Web Token* (*JWT*) dengan standar tanda tangan *HMAC* SHA-256 (`HS256`) sesaat setelah otentikasi kata sandi disetujui. Rentang keberlakuan kode tersebut disetel spesifik kadaluwarsa sesudah durasi **8 jam** operasional (setara limit pergantian jaga shift harian).
* **Justifikasi Bisnis**: Menjaga sistem kasir beroperasi cepat dalam pengalihan halaman aplikasi *CLI* tanpa kewajiban memeriksa validitas pada titik database utama.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.2](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Penutupan jalur pencurian profil identitas karyawan oleh giliran jaga sesudahnya (sebesar **100%**).

#### **INV-INT-19: Proteksi SQL Injection dan Validasi Input**
* **Deskripsi Teknis**: Implementasi prosedur pembersihan perintah dengan teknik antarmuka masukan pembatas `parameterized binding (%s)` secara universal serta pelacakan kesesuaian format numerik angka nominal.
* **Justifikasi Bisnis**: Mengeliminir bahaya kecelakaan masukan kode acak *ASCII* yang tidak dikenali *keyboard*, menenggelamkan upaya pengetikan eksekusi sisipan query SQL berbahaya (*SQL Injection*).
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.6 & 8.8](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Penjaminan perlindungan ketersediaan dan kekokohan struktur relasional pangkalan data (tingkat pertahanan **100%**).

#### **INV-INT-20: Pembatasan Kecepatan Coba Masuk (Rate Limiting Login)**
* **Deskripsi Teknis**: Skema pemantauan percobaan perantara pengguna (kasir). Bila mendapati **5 iterasi pembukaan profil log yang gagal** dalam kurun berurutan, skrip Python menyuntikkan hukuman isolasi blokir profil dengan batasan rentang larangan (hukuman pengunci antarmuka `locked_until`) selama tenggat **10 menit**.
* **Justifikasi Bisnis**: Meniadakan operasi perangkat pemecah kata acak eksternal dari pengetik bot perangkat tambahan yang berpotensi ditinggalkan kasir selama waktu tutup malam.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.7](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Risiko eksploitasi peretasan melalui *brute force* terminal *CLI* nol persen kejadian per tahun.

#### **INV-INT-21: Enkripsi Cadangan Database (Backup Terenskripsi AES-256)**
* **Deskripsi Teknis**: Skrip utilitas pengepakan data `mysqldump` terjadwal yang digabungkan otomatis melalui arsip kompresi terenkripsi kata sandi menggunakan standar algoritma *AES 256-bit* pada sistem operasi peladen Debian 12.
* **Justifikasi Bisnis**: Menunaikan beban mandat kewajiban proteksi privasi informasi kerahasiaan nomor telepon konsumen (*CRM*) yang dilindungi secara hukum lewat perundangan **UU Pelindungan Data Pribadi No. 27/2022**.
* **Sumber Data**: [Tech Stack Decision v1.1 Bagian 8.5](docs/sdlc/01_planning/04_tech_stack_decision.md).
* **Dampak Bisnis**: Meniadakan beban sanksi hukum dari potensi pelaporan penggelapan kontak (*Zero-Lawsuit Liability*).

### 4.6. Inovasi Keuangan dan Transaksi

#### **INV-INT-22: Multi-Skema Harga Dinamis (Retail, Grosir, Mitra)**
* **Deskripsi Teknis**: Algoritma pergantian penetapan tarif jual produk pada layar terminal kasir didasarkan kepada akumulasi jumlah masukan (skema potong harga kuantitas retail-ke-grosir) serta pengenalan profil hak istimewa *WhatsApp* konsumen.
* **Justifikasi Bisnis**: Mendobrak kekakuan harga pukul rata sehingga melayani variasi jenis relasi belanja korporat (berpartai besar) atau kemitraan.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.1]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Mengurangi jeda pelayanan di meja pembayaran hingga 40% (akibat staf tidak perlu menyocokkan baris angka harga grosir dari buku kusam).

#### **INV-INT-23: Sistem Bayar Fleksibel (Uang Muka dan Pelunasan Berjangka)**
* **Deskripsi Teknis**: Pencatatan baris piutang tertagih tagihan dengan pemberian klasifikasi spesifik pengelompokan pembayaran Uang Muka (*Down Payment*) setoran awal pemesanan disusul status Pelunasan tatkala barang divalidasi pemindahan tangan pengambilannya.
* **Justifikasi Bisnis**: Melindungi arus likuiditas sisa permodalan uang saku pemilik ketika merespon nilai pembelian belanja bahan cetak baku atas porsi besar skala makro.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.1]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Menjamin pemulihan pengembalian kas tagihan (*recovery*) senilai **100%** sebelum transaksi fisik diakhiri oleh pemesan.

#### **INV-INT-24: Penyatuan Sinkron Alur Pembatalan & Retur**
* **Deskripsi Teknis**: Tata kerja prosedur fungsi fungsional (bebas anomali) berpedoman prinsip ACID di tingkat peladen *database* untuk membereskan restitusi pemotongan kompensasi kas masuk sembari merestorasi status persediaan kuantitas rak.
* **Justifikasi Bisnis**: Meluruskan benang kusut kekacauan data rekapitulasi laba harian ketika staf mengembalikan produk batal akibat pelanggan tidak puas atau pembatalan di tahap Uang Muka.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.8]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Selisih kesalahan audit inventaris harian mencapai 0%.

#### **INV-INT-25: Pencocokan Kasus Akhir Giliran Jaga (Cash Reconciliation)**
* **Deskripsi Teknis**: Antarmuka paksaan rekonsiliasi sisa penghitungan laci penampung kas uang di meja depan sesaat sebelum pengguna (staf) mengetik *log out* keluar penutupan giliran operasional siang/malam. Menyimpan batas pelampauan batas ambang toleransi deviasi devisa maksimum **Rp 10.000**.
* **Justifikasi Bisnis**: Meretas penemuan sumber kesalahan uang kembali (*susuk*) yang tidak tepat, dan meredam ketegangan konflik perselisihan tuduhan kas di kalangan internal kolega.
* **Sumber Data**: [Project Charter v1.1 Bagian 8.1 [F-6.5]](docs/sdlc/01_planning/01_project_charter.md), [Feasibility Study v1.1 Bagian 8.6](docs/sdlc/01_planning/02_feasibility_study.md).
* **Dampak Bisnis**: Laporan kecocokan realitas nilai penyetoran tunai melonjak tajam terjamin akurasinya (selisih di bawah batas yang ditentukan).

#### **INV-INT-26: Dasbor Evaluasi Singkat Rentabilitas per Penjualan (Laba Instan)**
* **Deskripsi Teknis**: Generator pelaporan penyaringan ringkasan akumulasi penjualan yang membuang variabel potongan *HPP* persentase modal serta biaya operasional, merinci 5 kolom penyajian kompartemen (cetak kustom, retail ATK, elektronik, agen bank, jasa) di waktu nyata (*real-time*).
* **Justifikasi Bisnis**: Meniadakan prosedur penginputan baris pembukuan akuntansi konvensional buku besar mingguan, menghadirkan indikator presisi kompas arah evaluasi pemotongan divisi produk yang macet perputarannya.
* **Sumber Data**: [Project Charter v1.1 Bagian 8.1 [F-6.4]](docs/sdlc/01_planning/01_project_charter.md).
* **Dampak Bisnis**: Pematangan putusan arah strategis ekspansi sang Pemilik secara instan (pemberian data matang diraih waktu **< 5 detik**).

### 4.7. Inovasi Layanan Keuangan Digital dan Administrasi Modal

#### **INV-INT-27: Manajemen Saldo PPOB dan Peringatan Deposit Otomatis**
* **Deskripsi Teknis**: Logika pelacakan ganda yang mengawasi fluktuasi penarikan dari dompet virtual pulsa telekomunikasi dan akun distribusi kuota listrik (*PPOB*). Aplikasi mendeteksi apabila margin penampungan tersisa **Rp 150.000**, menyalakan lampu sinyal pemberitahuan teks berkedip pada sudut CLI, serta membuka gerbang pencatatan injeksi deposit minimum ke agen **Rp 500.000**.
* **Justifikasi Bisnis**: Mereduksi kehilangan momentum layanan digital berkecepatan tinggi yang gagal akibat keterlambatan penyediaan cadangan dompet elektronik di gerai pelayanan depan.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.3] & F-3.1](docs/sdlc/01_planning/01_project_charter.md), [narasi.txt Harapan Aplikasi Baru Poin 3](docs/sdlc/narasi.txt).
* **Dampak Bisnis**: Hilangnya keluhan batal kirim yang sering kali mendesak konsumen lari menuju rival kompetitor lainnya (0% kehilangan pembeli rutin tagihan/pulsa).

#### **INV-INT-28: Optimalisasi Biaya Admin Jasa Keuangan (6 Akun Distribusi)**
* **Deskripsi Teknis**: Sub-modul administrasi jasa alih uang yang membandingkan persentase dan penawaran biaya admin seketika dari kelompok 6 (enam) aplikasi agen penyalur (Mandiri, Gopay, OVO, ShopeePay, Dana, LinkAja) merekomendasikan dompet virtual termurah pada saat penyetelan instruksi order CLI oleh kasir toko.
* **Justifikasi Bisnis**: Memberikan daya tarik margin nilai selisih yang memikat para pengguna perorangan layanan bank yang terus mencari lokasi *withdrawal* dan setoran biaya potongan terendah di daerah.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.3] & F-3.2](docs/sdlc/01_planning/01_project_charter.md), [narasi.txt Harapan Poin 4](docs/sdlc/narasi.txt).
* **Dampak Bisnis**: Terbukanya jalan pengoptimalan pendapatan pundi-pundi margin hingga **12%** di layanan pos divisi jasa keagenan bank UMKM.

#### **INV-INT-29: Pencatatan Transaksi Jasa Service & Teknisi Terintegrasi**
* **Deskripsi Teknis**: Penerimaan barang servis teknikal perangkat cetak dan komputasi (*printer*, *notebook*) dibekali registrasi kode antrian perbaikan (Identitas, Laporan Problem, Prakiraan Ongkos, Jadwal Penyelesaian) ditautkan erat menuju laporan pembukuan divisi komersial *Technical Service*.
* **Justifikasi Bisnis**: Mengakhiri sengkarut unit laptop tertinggal atau kerugian ganti rugi barang mesin orang lain akibat lembar nota registrasi yang pudar atau kuitansi tulis tangan tercecer di laci mekanik.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.3] & F-3.3](docs/sdlc/01_planning/01_project_charter.md), [narasi.txt Harapan Poin 5](docs/sdlc/narasi.txt).
* **Dampak Bisnis**: 100% inventaris aman terjaga, menghapuskan beban biaya kompensasi tuntutan klien pelanggan bengkel yang kecewa.

#### **INV-INT-30: Administrasi Keuangan Non-Operasional (Pinjaman, Aset, & Pengeluaran Rutin)**
* **Deskripsi Teknis**: Modul pencatatan terpadu untuk administrasi pinjaman komersial perbankan (notifikasi H-3 sebelum masa setoran pokok bulanan Bank BRI dan Mandiri tiba), perincian pinjaman tanpa batas tempo dana kerabat (dengan rekaman rincian arus penarikan dan sisa titipan modal keluarga), akumulasi laporan penyusutan instrumen toko (tabungan aset untuk pembaharuan mesin cetak), serta pendataan pemotongan utilitas operasional harian (Air, Konsumsi Wifi, PLN).
* **Justifikasi Bisnis**: Memberikan sentralisasi pangkalan data yang solid untuk pelaporan akuntansi penyisihan sisa dana laba bulanan bebas manipulasi, serta memastikan kelancaran relasi historikal perbankan korporasi *(credit score)* dan kehangatan ikatan gotong royong sosiokultural pinjaman persaudaraan, agar proyek AbuCom tidak didera kepanikan kas likuiditas dadakan.
* **Sumber Data**: [Project Charter v1.1 Bagian 4.1.1 [M.6], F-6.1, F-6.2, F-6.3](docs/sdlc/01_planning/01_project_charter.md), [narasi.txt Harapan Poin 6](docs/sdlc/narasi.txt).
* **Dampak Bisnis**: Denda angsuran tunggakan dari institusi Bank sukses ditekan ke taraf **0%**, pemantauan arus kas bersih tersaji instan, menjaga integritas kelancaran toko dari kerugian sosial kerabat.

---

## 5. Usulan Inovasi Tambahan (Rekomendasi Baru)

Bagian ini memaparkan usulan inovasi tambahan yang dirancang secara proaktif untuk menyempurnakan sistem AbuCom berdasarkan tren industri percetakan modern dan ritel UMKM di Indonesia.

### 5.1. Inovasi yang Sudah Direkomendasikan di Dokumen Sebelumnya

#### **INV-REC-01: Pencadangan Data Otomatis Berkala (*Automated Backup*)**
* **Deskripsi**: Penjadwalan skrip utilitas mandiri (*cron*) yang dirancang khusus melakukan tugas pelindungan penarikan tabel transaksi dan gudang operasional MySQL. Ekspor dieksekusi murni menuju rupa paket berkas SQL yang dimampatkan (`.zip`) dengan pemicu pengaktif otomatisasi pergerakan saat matahari tenggelam lewat pukul 21:00 (menandai batas penutup tirai toko).
* **Justifikasi Bisnis**: Memusnahkan ancaman kehancuran aset paling sentral dalam satu entitas bisnis komputasional; menjauhkan musibah di mana *Mini PC Server Linux Debian* tertimpa masalah kerusakan bad sector fisik penyimpan yang fatal (*harddisk crash*).
* **Dampak Operasional**: Staf utama pemilik aman dan lega sepenuhnya 100% tanpa diwajibkan lagi menekan berulang baris ketikan skrip cadangan secara repetitif manual.
* **Kompleksitas Implementasi**: Rendah.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-6 (Fase Implementasi I Akhir).

#### **INV-REC-02: Notifikasi Templat Teks Berantai *WhatsApp Ready***
* **Deskripsi**: Terminal operasi antarmuka *CLI* menyediakan menu luaran *output* kilat berbentuk rangkaian paragraf surat pesanan yang dirapikan seketika dan ditambahkan tempelan pemintas Uniform Resource Locator tautan rintisan pesan web resmi `https://wa.me/` untuk memfasilitasi perintah sapuan salin-tempel staf ke program aplikasi obrolan sekunder *WhatsApp Web* Windows.
* **Justifikasi Bisnis**: Mengecoh tingginya anggaran tarif gerbang aplikasi *API* komersil *WhatsApp* yang ditagihkan kepada akun UMKM dengan merestorasi pengetikan standar secara cerdik; komunikasi laporan siap jemput barang dari konsumen terealisasikan secara singkat.
* **Dampak Operasional**: Staf meja muka (*Pramuniaga/Kasir*) sanggup meneruskan laporan cetakan siap ambil kurang dari rasio ketik **30 detik** usai pesanan final terselesaikan dari mesin produksi besar.
* **Kompleksitas Implementasi**: Rendah.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-5 (Fase Implementasi I).

#### **INV-REC-03: Analisis Prediksi Tenggat (*Re-Order*) Stok Persediaan**
* **Deskripsi**: Logika matematika fungsional meraba pola alur kebiasaan jumlah keluarnya pesanan di satu pekan lewat histori jejak konsumsi. Kalkulasi Python menelaah sisa hari proyeksi batas ketahanan sisa stok (*misal: 10 rim HVS A4 kertas*), membangkitkan indikator merah berkedip saat estimasi hari menunjukkan kerawanan ambang di bawah hitung H-7 hari operasional.
* **Justifikasi Bisnis**: Memukul mundur kelalaian tim inventaris saat pimpinan mendapati tumpukan gulungan material cetak pesanan besar tak teratasi karena pergeseran pembelian tertunda hingga truk logistik pemasok telat.
* **Dampak Operasional**: Pengaturan ritme siklus pasokan belanja (*Purchase Order*) barang komoditas pokok tercapai secara terjadwal, melepaskan dari ancaman ketiadaan persediaan **100%**.
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-9 (Fase Implementasi II Akhir).

### 5.2. Inovasi Tambahan yang Diusulkan oleh Tim AI

#### **INV-NEW-01: Sistem *Dashboard* Ringkasan Harian *CLI***
* **Deskripsi**: Tampilan antarmuka visual ringkas menggunakan panel pustaka eksternal integrasi visual Python `rich` saat sesi *User* bertaraf Pemilik sukses masuk mendarat pada beranda terminal. Dashboard menerbitkan visual grafis performa ringkas harian (Hari ini): angka sirkulasi laba kasar, hitungan antrian status tunggu yang bertumpuk, indikator bahan mentah berstatus gawat, beserta total rekapan saldo peti laci kas yang terhimpun per detik aktual.
* **Justifikasi Bisnis**: Menyajikan visibilitas navigasi layar monitor pusat kilat di atas semua pelaporan (*helicopter view*) agar nahkoda kapal memantau riak tanpa mewajibkannya menyusuri hiruk pikuk percabangan kode menu tersembunyi berulang demi laporan tunggal.
* **Dampak Operasional**: Pemilik merekam arah kesehatan toko secara keseluruhan (isu antrian, bahaya kekurangan komoditas retail) sesingkat durasi **< 5 detik** penyajian.
* **Kompleksitas Implementasi**: Rendah.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-6 (Fase Implementasi I Akhir).

#### **INV-NEW-02: Fitur Riwayat Pelacakan Fluktuasi Harga Penyuplai (*Price Tracking*)**
* **Deskripsi**: Penciptaan tabel dasar tambahan memori database SQL yakni `supplier_prices` (Harga Suplai Vendor). Menghimpun histori pasang surut pencatatan fluktuasi indeks mata uang setiap saat nota pengadaan barang masukan dicatatkan staf Gudang, memudahkan komparator harga antara pedagang/agen yang berlomba memasok komoditas serupa.
* **Justifikasi Bisnis**: Mendikte sistem sebagai pembanding pasaran harga kompetitif. Sangat kritis demi memaksimalkan margin laba per meter pengeluaran (*cutting cost*) bahan cetak atau retail tanpa mengurangi bobot kualitas mutu produksi.
* **Dampak Operasional**: Staf penjaga persediaan gudang diberikan anjuran perbandingan penyuplai berharga terhemat saat ia mengajukan lembar instruksi belanja (menghemat serapan pembiayaan komoditas sebesar margin hingga **5%** nominal transaksi rutinitas).
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-7 (Fase Implementasi II Awal).

#### **INV-NEW-03: Sistem Sinyal Pengingat Jatuh Tempo Hutang (*Alert* Otomatis)**
* **Deskripsi**: Modul sirkuit pemberitahu awal pembuka saat sistem peladen dihidupkan (sistem *startup alert*). Baris layar konsol seketika mendesak sorotan notifikasi pada batas penanda merah kritis (**H-3**) dari hari kesepakatan kewajiban bayar nominal tagihan pinjaman perbankan beringan bulanan, maupun hutang modal pesanan kepada agen/supplier raksasa (Vendor Alat/Distributor bahan retail).
* **Justifikasi Bisnis**: Menangkis cacat nama (*blacklist bank*) di masa muka terhadap pemilik AbuCom dari beban kelalaian penalti serta denda keterlambatan pembayaran harian cicilan penyokong penyedia pinjaman komersial komitmen tegas, dengan mitigasi waktu toleransi luang tiga hari persediaan perputaran kas pelunasan.
* **Dampak Operasional**: Hilangnya kepanikan administrasi tunggakan setoran (persentase keterlambatan dikikis mutlak menjadi **0%** dari bulan ke bulan).
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-10 (Fase Implementasi III).

#### **INV-NEW-04: Log Riwayat Serah Terima Giliran Kerja Karyawan (*Shift Handover Log*)**
* **Deskripsi**: Ekstensi relasional pembuktian tabel penyerahan kunci (serah terima *Shift Kasir* meja muka). Entri mencakup: pengenal profil staf purna waktu (*logout ID*), nama masuk pengisi pengganti (*login ID*), penanda waktu *timestamp* pergantian silang, pelaporan total kas tunai transisi detik itu, beserta form rekam pesan anomali teknis lapangan yang spesifik diketik (*Misal: Rol kabel stempel besar putus, mesin butuh pendinginan ekstra*).
* **Justifikasi Bisnis**: Melindungi iklim kekeluargaan rekan sejawat karyawan di meja serambi (*front desk*) dari letusan tuduhan tak berdasar menyangkut kealpaan kehilangan hasil setoran saat periode estafet giliran masuk antara jadwal kru penjaga shift siang kepada penjaga giliran piket petang.
* **Dampak Operasional**: Menciptakan garis akuntabilitas batas silang kepemilikan laci mutlak 100% sehingga sumber kerugian kebocoran diketahui seketika dengan saksi pertukaran operasional fisik per hari.
* **Kompleksitas Implementasi**: Rendah.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-6 (Fase Implementasi I).

#### **INV-NEW-05: Dasbor Analisis Persentase Keuntungan Margin Produk Spesifik**
* **Deskripsi**: Perluasan modul pembantu perhitungan matematis persentase margin keuntungan kotor operasional (*Gross Margin Ratio*). Evaluasi memuat fungsi fungsional murni = `((Harga Label Konsumen - HPP Ekstrak BOM) / Harga Label Konsumen) * 100`. Hasil tertanam otomatis dan tampil mendampingi jejeran harga setiap satu inventaris atau jasa pengerjaan khusus percetakan pada sistem basis datanya.
* **Justifikasi Bisnis**: Memberikan landasan putusan investasi pemasaran dan fokus fokus promosi (titik api) periklanan atas deretan pilihan produk unggulan dengan kelebihan persentase margin (*profit hunter*) nilai paling gemilang dibandingkan unit berbiaya operasional tebal minim penghasilan bersih.
* **Dampak Operasional**: Menyuguhkan peta terang menderang (*insights*) dalam pengambilan kepastian kebijakan harga kompetitor di kawasan pertokoan area berjarak sekelip durasi (**< 5 detik** eksekusi analisa margin data).
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-10 (Fase Implementasi III).

#### **INV-NEW-06: Modul Ringkas Deteksi Anomali Pencurian (*Fraud Detection* Sederhana)**
* **Deskripsi**: Penanaman blok penjaga perulangan inspeksi siluman yang mengukur frekuensi operasi kelakuan di perantara: memantau deret pengerjaan retur pembatalan barang (*cancelation limit*: lebih dari tiga kejadian per blok shift tugas), pencocokan riwayat pengembalian barang secara bertubi pada nama meja kasir tak wajar, atau menyentuh pendaratan di mana batas nilai pelampauan toleransi ambang defisit uang fisik meja mencapai lebih besar dari patokan kewajaran nilai sisa (melebihi **Rp 10.000** batas). *(Bergantung pada implementasi INV-INT-16 dan INV-INT-25).*
* **Justifikasi Bisnis**: Pemutus asa terstruktur atas eksploitasi rongga keamanan celah kerawanan retur yang sering digunakan pelaku manipulasi pekerja (*internal fraud* di kalangan karyawan lepas harian/kontrak ritel tanpa jaminan etis yang ketat) dalam menyalahi kuasa pengembalian dompet perusahaan.
* **Dampak Operasional**: Penyajian laporan khusus *peringatan bendera merah* (`red-flag notifications`) menerjang ruang sapa utama Pemilik saat ia singgah log masuk, mempercepat masa temuan audit penyidikan atas kebocoran hingga selang **100%** terkonfirmasi akurat.
* **Kompleksitas Implementasi**: Tinggi.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-10 (Fase Implementasi III).

#### **INV-NEW-07: Standardisasi Templat Format Teks Kertas Struk Pemotongan Termal**
* **Deskripsi**: Pematangan fungsi ekspor ekstraktor cetak *string text* akhir (`.txt`) direkayasa ukur penyesuaian (*alignment padding*) ke bentangan sempit kertas rol agar berkapasitas presisi (*wrapping auto-fit*) menyusup cetakan mulus khusus instrumen printer *Thermal Receipt Pos* spesifikasi kaliber **58mm / 80mm**. Rekapan yang dicetak dibatasi ke luaran rekonsiliasi angka laba rugi total, dan catatan setor per harian staf.
* **Justifikasi Bisnis**: Menawarkan pendokumentasian setoran bukti kertas serah terima (*hardcopy audit*) fisik untuk penyusutan pengeluaran kertas mesin suntik tinta A4 reguler harian pada penggabungan nota catatan laba yang ditumpuk malam ke meja besar pimpinan operasional (*Drop-box* uang laci).
* **Dampak Operasional**: Staf penjaga serambi mengawinkan bundelan bukti penyetoran cetak gulung kecil ringkas dengan setoran penerimaan bundel rupiah tunai, menghembuskan nafas efisiensi penghematan pemakaian perbaikan logistik rim penyedia *HVS* toko setinggi **80%**.
* **Kompleksitas Implementasi**: Rendah.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-5 (Fase Implementasi I).

#### **INV-NEW-08: Sistem Otomasi Impor Baris Pangkalan (*CSV/Excel Data Sanitization*)**
* **Deskripsi**: Penambahan modul *Python scripting* ekstra-perantara (tidak menempel fungsi kasir operasional harian) penyedot alur yang menelan file CSV hasil konversi buangan dari bundelan lembar lajur *Excel* berumur lawas milik pimpinan. Pemroses berpatroli meredakan dan membersihkan kesalahan input tik (*data cleansing*) semacam koma berlebih, baris lompat tak beralasan, atau tipe keliru, seraya memuat paksa deret tersebut mendaki tabel persediaan inventori SQL terbaru, agar sistem kasir baru AbuCom lahir berbekal stok silsilah lampau.
* **Justifikasi Bisnis**: Mengekalkan warisan database peninggalan daftar koleksi data vendor barang (*Supplier*), inventori fisik eceran stempel komplit (*Master Barang*), ke tatanan aplikasi canggih, merampungkan siksaan pemandangan penyalinan ratusan ribu kata huruf secara input tunggal repetitif di malam permulaan penggunaan (*Go-Live system*).
* **Dampak Operasional**: Masa jeda adaptasi transisi program menyusut radikal dari prakiraan kelumpuhan minggu panjang berganti operasional berdikari di bawah pengerjaan santai sempit kurang dari **1 hari** kalender.
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-5 (Fase Implementasi I).

#### **INV-NEW-09: Dinamika Modifikasi Ambang Batas Aplikasi Secara Instan (*Runtime Config*)**
* **Deskripsi**: Peletakan pondasi kolom tabel tunggal referensial fleksibel (`system_configs`) tempat penyanderaan konstanta kaku perancangan skema angka. Menyandera nilai semacam: persentase limit pergeseran porsi pembagian dividen laba bonus tim (Misal dari **25%** bergeser), penyetelan titik angka bahaya setoran dompet limit kas *PPOB* awal batas **Rp 150.000**, perumusan toleransi limit perselisihan ujung receh kasir **Rp 10.000**, hingga pembatasan pagu *kasbon* kereditan staf batas **Rp 1.000.000**. Konfigurasi sepenuhnya diubah pakai layar menu permohonan konsol CLI Pemilik mutlak tanpa perlu mereparasi badan tulisan naskah program arsitektur *Python*. *(Bergantung pada implementasi INV-INT-09, INV-INT-11, INV-INT-20, dan INV-INT-27)*.
* **Justifikasi Bisnis**: Menyelamatkan masa depan laju operasi mesin piranti lunak dari kepunahan disaat AbuCom berkembang. Menolak skema modifikasi kode sumber utama (sebagai antitesis *Hardcoding*) seandainya tahun depan rasio penentu bonus dan inflasi merubah peta kebijakan persaingan usaha lokal secara mutlak.
* **Dampak Operasional**: Hadirnya otonomi paripurna kendali kebijakan strategi operasional langsung di telapak jemari pemilik utama (100% kemudahan revisi bisnis seketika di perbatasan jam tayang).
* **Kompleksitas Implementasi**: Sedang.
* **Fase Implementasi yang Direkomendasikan**: Bulan ke-9 (Fase Implementasi II Akhir).

---

## 6. Analisis Kelayakan Inovasi

### 6.1. Matriks Kelayakan Inovasi Terintegrasi

Evaluasi kelayakan untuk 30 inovasi terintegrasi didasarkan pada parameter teknis dan operasional:

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
| **INV-INT-21** | Enkripsi Backup Database | Layak | Layak | High | Terintegrasi |
| **INV-INT-22** | Multi-Skema Harga | Layak | Layak | High | Terintegrasi |
| **INV-INT-23** | Pembayaran Bertahap DP | Layak | Layak | High | Terintegrasi |
| **INV-INT-24** | Batal/Retur Sinkron | Layak | Layak | High | Terintegrasi |
| **INV-INT-25** | Rekonsiliasi Kas Harian | Layak | Layak dengan Catatan | High | Terintegrasi |
| **INV-INT-26** | Laba/Rugi Instan Divisi | Layak | Layak | High | Terintegrasi |
| **INV-INT-27** | Saldo PPOB & Alert Deposit | Layak | Layak | High | Terintegrasi |
| **INV-INT-28** | Optimalisasi Admin 6 Akun | Layak | Layak | High | Terintegrasi |
| **INV-INT-29** | Transaksi Service & Teknisi | Layak | Layak dengan Catatan | High | Terintegrasi |
| **INV-INT-30** | Pinjaman, Aset, & Pengeluaran | Layak | Sangat Layak | High | Terintegrasi |

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
   * **INV-NEW-03 (Alert Jatuh Tempo)**, **INV-NEW-06 (Fraud Detection)**, dan **INV-INT-30 (Pinjaman, Aset & Pengeluaran)**: Diimplementasikan pada fase akhir keuangan dan *audit trail* (Bulan 10). Hal ini disebabkan karena INV-NEW-06 secara teknis sangat bergantung pada penyelesaian integrasi log rekam INV-INT-16 dan rutinitas rekap kas akhir INV-INT-25 yang harus dikerjakan jauh pada bulan sebelumnya demi menghindarkan proyeksi mogok penyandian perangkat lunak (deadlock error arsitektural dependensi).

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
| **INV-INT-25** | ✓ | — | — | — | — | — | ✓ | — | — |
| **INV-INT-26** | — | — | — | — | — | ✓ | — | — | — |
| **INV-INT-27** | — | — | ✓ | — | — | — | — | — | — |
| **INV-INT-28** | — | — | ✓ | — | — | — | — | — | — |
| **INV-INT-29** | — | — | ✓ | — | — | — | — | — | — |
| **INV-INT-30** | — | — | — | — | — | ✓ | — | — | — |
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
1. **Peningkatan Rincian Fitur**: Setiap usulan inovasi (terutama 9 rekomendasi baru) wajib diuraikan secara detail menjadi daftar kebutuhan fungsional (*FR*) dan kebutuhan non-fungsional (*NFR*) spesifik per modul.
2. **Kriteria Input/Output**: Kebutuhan data masukan untuk penyedotan konversi format (*import CSV*) dan perihal masukan tabel konfigurasi dinamis (batasan nilai, tipe data numerik parameter nominal operasional) harus tertulis mengikat di kerangka *SRS* menghindari ambiguitas perancangan kode masa depan.
3. **Standar Divisi Keuangan Digital**: Syarat transaksi *PPOB* (penyisipan peringatan sisa pulsa di garda rentan limit) dan pedoman pelacakan transfer berskala ganda melalui jalur pencatatan agen terjangkau 6 aplikasi *e-wallet* perbankan harus diartikan mutlak terdefinisi kokoh mematuhi *FR* struktural.

### 8.2. Dampak terhadap Design (SDD & ERD)
1. **Perubahan ERD Basis Data**: Struktur cetak biru persilangan relasi tabel MySQL (*ERD*) dituntut memasok fondasi penopang baris per baris wadah operasional memori pelindung log untuk memperagakan kelancaran utilitas data inovasi:
   * Tabel `audit_logs` (log khusus rekam riwayat pelacakan transaksi)
   * Tabel `system_configs` (pusat regulasi batas fleksibel tata nilai konstan sistem limit)
   * Tabel `supplier_prices` (daftar pasang surut fluktuasi historikal patokan uang pembelian)
   * Tabel `shift_handover_logs` (buku harian mutasi serah terima estafet laci jaga jam operasional)
   * Tabel `ppob_logs` (kunci pintu arsip penampungan angka tarik ulur sisa pundi bayar token listrik harian)
   * Tabel `kreditur_logs` (alur rekam sisa tagihan angsuran hutang tenor bulanan relasi bank / sanak famili)
   * Tabel `asset_savings_logs` (buku akumulasi nominal pundi sisihan dana cadangan peremajaan mesin).
2. **Skema Imutabilitas di SDD**: *SDD* wajib merinci dengan terang pemetaan arah logikal tata tertib lalu lalang *state closure* ke dalam baris tata riwayat eksekusi logaritma struktural di *Python*, mencegah pemanggilan paksa kebiasaan *OOP* merusak sistem.

### 8.3. Dampak terhadap Implementation
1. **Boilerplate Tambahan**: Pengembang AI perintis harus meletakkan pondasi rancang bangun landasan ekstra (*CSV parser handler* dan cetakan rilis penutup file audit harian JSON otomatis) merajut fondasi permulaan *Sprint* di bulan ke-5 yang sangat dibutuhkan untuk dependensi berikat pada alur logikal kasir ritel dan pemantau aset kelak.
2. **Disiplin Paradigma FP**: Pendalaman ketaatan kepenulisan fungsi matematis penyusutan kepingan bahan dimensi volume desimal *HPP* BOM serta penghitung limit profit wajib bebas polusi variabel acak (menuntut fungsi termurnikan) murni dilandasi serapan pustaka standar `decimal` tertanam *Python* bawaan semata.

### 8.4. Dampak terhadap Testing (UAT)
1. **Skenario Uji Khusus**: Rencana cetak lembar jadwal gladi bersih wajib melampirkan tantangan pengerjaan tak acak untuk tes kegagalan penyandian manipulasi kotor palsu, simulasi pemutusan gulir suplai tenaga listrik (uji coba restorasi baris MySQL yang macet/rollback), provokasi penyisipan lembar Excel cacat via saluran skrip CSV, hingga pengujian gerbang batas pintu penghalang akses izin lintas jenjang jabatan wewenang *RBAC*.
2. **Simulasi Shift Handover**: Pengujian operasional estafet *log in / log out* wajib dipraktikkan memutar antarkandidat kru pendaftar staf kasir teranyar secara berulang berhari-hari menjamin kelihaian proses tutup harian tunai tak gagap di bulan puncak penyempurnaan lapangan.

### 8.5. Dampak terhadap Maintenance & Operational
1. **Buku Panduan Berbasis CLI**: Memberatkan keharusan perancangan pengetikan selebaran buku tipis (ringkasan manual khusus baris ketik rahasia Pemilik) seiring munculnya tuntutan instruksional bagaimana menelusuri pengubahan tabel konfigurasi penyetelan parameter batasan kaku kasbon (`system_configs`).

---

## 9. Risiko Inovasi dan Rencana Mitigasi

Berikut adalah identifikasi risiko terkait usulan inovasi, probabilitas (1-5), dampak (1-5), serta rencana mitigasinya:

| No | Risiko Inovasi | Probabilitas | Dampak | Rencana Mitigasi |
|----|----------------|:------------:|:------:|------------------|
| 1  | **Scope Creep Akibat Inovasi Baru**: Penambahan fitur visual `rich` dan sistem deteksi fraud yang berlebihan memperpanjang durasi coding melebihi batas 12 bulan. | 3 | 4 | Tetapkan batas ruang lingkup inovasi baru yang rigid pada SRS; tunda inovasi prioritas rendah (seperti deteksi fraud rumit) ke fase pemeliharaan pasca go-live. |
| 2  | **FP Python Menghambat Logika Dinamis**: Ketiadaan class OOP menyulitkan programer junior mengimplementasikan konfigurasi dinamis atau log shift handover secara fungsional. | 2 | 4 | Siapkan template fungsi pembungkus state (*state pass wrapper*) oleh Claude Sonnet 4.6 di awal sprint sebagai acuan penulisan modul operasional. |
| 3  | **Staf Menolak Menu CLI ANSI**: Karyawan baru merasa kebingungan menatap layar teks terminal dan menuntut tampilan aplikasi GUI tablet modern. | 4 | 3 | Optimalkan pewarnaan ANSI menu *CLI* menggunakan panel `rich` untuk meniru visual kotak GUI, serta sediakan program pelatihan simulasi 3 hari purna waktu. |
| 4  | **Latensi Query Laporan Margin**: Agregasi data HPP BOM desimal secara rekursif memperlambat performa respons *CLI* laporan keuangan tahunan. | 2 | 3 | Gunakan indeks relasional database MySQL yang optimal pada kolom transaksi dan buat *view* database khusus untuk mempercepat penarikan data margin. |
| 5  | **Kerusakan Data saat Setup CSV**: Struktur data pada berkas Excel lama pemilik tidak bersih (banyak baris kosong/salah tik) saat diimpor via modul CSV. | 4 | 4 | Buat fungsi *parser* fungsional yang dilengkapi logger error baris data yang gagal diimpor, sehingga staf gudang tahu data mana yang perlu diperbaiki manual. |
| 6  | **Ketidakstabilan Kas Akibat Penarikan Pinjaman**: Kas terganggu karena pinjaman tanpa bunga kerabat ditarik mendadak saat proyek berjalan tanpa pemberitahuan tertulis awal. | 3 | 4 | Mitigasi ketat dengan pemisahan rekening Dana Cadangan Darurat (Rp 4.500.000) dan pengetikan rutin laporan historikal mutasi yang siap saji saat penagih bertandang ke gerai toko. |
| 7  | **Klaim Tuntutan Hubungan Pekerja (*PKWT*/*PKWTT*)**: Cacat hukum pengelolaan hak-hak pemberian nilai kesejahteraan kasbon dan bonus poin karyawan karena ketiadaan kontrak sah pada menu payroll operasional. | 2 | 4 | Mengamanatkan sub-sistem penggajian terotomasisasi ini dirancang memuat seleksi centang perbedaan statuta hukum pekerja harian (kontrak *PKWT*) kontra organik (*PKWTT*) untuk menjaga ketertiban dokumen tenaga kerja sipil. |

---

## 10. Persetujuan dan Otorisasi

Lembar otorisasi ini menandai persetujuan formal pemilik usaha terhadap usulan inovasi yang didokumentasikan untuk dilanjutkan ke fase requirements (*SRS*):

| Pihak Penandatangan | Jabatan/Peran | Tanda Tangan | Tanggal Persetujuan |
|---------------------|---------------|--------------|---------------------|
| **Pemilik Usaha AbuCom** | Sponsor Utama & Manajer Proyek | *(Disetujui secara Digital)* | 2026-05-28 |
| **Tim Pengembang AI** | Lead Innovation Analyst | *(Disetujui secara Digital)* | 2026-05-28 |

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
19. **Pinjaman Bank Berbunga**: Kewajiban utang komersial (BRI/Mandiri) yang memiliki skema bunga tetap, tenor, dan setoran rutin terjadwal.
20. **Pinjaman Tanpa Bunga (Pinjaman Kerabat)**: Sumber pendanaan informal dari kerabat/keluarga tanpa beban bunga finansial namun membutuhkan catatan saldo yang transparan untuk penarikan mendadak.
21. **Jasa Keuangan Agen**: Layanan transfer uang antar bank dan tarik tunai retail fisik yang dijalankan staf kasir menggunakan e-wallet agen bank terdaftar.
22. **PKWT**: Perjanjian Kerja Waktu Tertentu, kesepakatan tertulis bagi staf karyawan berkontrak paruh-waktu atau staf dengan periode jangka kerja sementara berdasarkan asas hukum peraturan Indonesia.
23. **PKWTT**: Perjanjian Kerja Waktu Tidak Tertentu, ikatan mutlak permanen untuk perlindungan kesejahteraan karyawan berstatus organik tetap di perusahaan.

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
