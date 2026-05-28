---
dokumen    : Feasibility Study (Studi Kelayakan Proyek)
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.2
tanggal    : 2026-05-28
status     : Validated
penyusun   : Senior Business Analyst & Feasibility Consultant
---

# Feasibility Study — AbuCom

## Riwayat Perubahan Dokumen

| Versi | Tanggal    | Perubahan        | Oleh                                          |
|-------|------------|------------------|-----------------------------------------------|
| 1.0   | 2026-05-21 | Pembuatan awal   | Senior Business Analyst & Feasibility Consultant |
| 1.1   | 2026-05-21 | Validasi, Analisis, dan Penyempurnaan Dokumen Feasibility Study. Melengkapi data gap narasi & charter, memperbaiki parameter UMR, menambahkan break-even analysis & NPV, serta memperbarui riwayat perubahan. | Senior Business Analyst & Feasibility Consultant |
| 1.2   | 2026-05-28 | Validasi menyeluruh: kelengkapan referensi dokumen, perincian modul di Seksi 3, penyelarasan bahasa Indonesia teknis, perbaikan struktur risiko industri, eliminasi placeholder UMR dan estimasi data, penambahan glosarium baru, serta pengisian tabel referensi secara komprehensif. | Senior Business Analyst & Feasibility Consultant |

---

## 1. Informasi Dokumen
Dokumen ini disusun untuk menganalisis dan mengevaluasi tingkat kelayakan dari rencana pembangunan **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**. Analisis dilakukan secara komprehensif pada lima dimensi kelayakan standar industri untuk mendukung pengambilan keputusan strategis bisnis apakah proyek ini layak dilanjutkan (GO) atau tidak (NO-GO) ke fase SDLC berikutnya.

---

## 2. Ringkasan Eksekutif (Executive Summary)

### 2.1. Latar Belakang Singkat
Usaha UMKM AbuCom merupakan penyedia jasa percetakan, retail ATK, PPOB, jasa keuangan, dan jasa teknis yang saat ini dikelola dan dijalankan secara mandiri oleh pemilik usaha (*single-fighter*). Akibat kompleksitas pengelolaan lima divisi usaha tersebut yang dilakukan secara manual menggunakan berkas Microsoft Excel yang berserakan, pemilik mengalami stres berat, keletihan mental (*burnout*), serta risiko operasional yang tinggi seperti pesanan terlewat dan selisih persediaan barang baku yang signifikan. Untuk mengatasi permasalahan tersebut, diusulkan pembangunan sistem aplikasi manajemen internal terpadu berbasis *Command Line Interface* (CLI) menggunakan Python dan MySQL.

### 2.2. Deskripsi Masalah (Problem Statement)
Absennya sistem yang terintegrasi memaksa pemilik usaha untuk menangani seluruh proses—mulai dari pelayanan, desain, pembukuan, hingga pemantauan stok bahan baku—secara sendirian dan tidak akurat. Pendekatan manual berbasis Excel ini membatasi kapasitas pertumbuhan bisnis dan secara perlahan dapat memicu terhentinya operasional secara total apabila batas kelelahan fisik dan mental pemilik telah terlampaui. Oleh karena itu, terdapat urgensi yang sangat mendesak (kondisi *burnout*) untuk segera membangun solusi piranti lunak otomasi yang mampu mendelegasikan beban administratif ini kepada staf operasional yang baru akan direkrut.

### 2.3. Tujuan Studi Kelayakan
Studi kelayakan ini bertujuan untuk mengevaluasi secara objektif, kritis, dan berbasis data apakah proposal proyek aplikasi kustom CLI Python untuk AbuCom layak diimplementasikan dari aspek kelayakan teknis, operasional, ekonomi/finansial, jadwal, serta hukum dan organisasional.

### 2.4. Kesimpulan dan Rekomendasi Akhir
Berdasarkan hasil analisis mendalam terhadap kelima dimensi kelayakan, serta justifikasi utama untuk memitigasi urgensi kondisi *burnout* dari sang pemilik usaha, proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan** dinyatakan:

$$\color{orange}{\textbf{GO DENGAN CATATAN (GO WITH CONDITIONS)}}$$

Sistem ini sangat layak secara ekonomi dan jadwal, serta memiliki urgensi operasional yang sangat tinggi untuk mengatasi kelelahan ekstrem pemilik. Namun, status kelayakan **Teknis**, **Operasional**, dan **Hukum** berada pada tingkat **"Layak dengan Catatan"** karena adanya risiko kritis terkait kerumitan paradigma *Functional Programming* (FP) murni, proses rekrutmen staf baru, serta kepatuhan perlindungan data pribadi pelanggan. Proyek ini direkomendasikan untuk segera dilanjutkan ke Fase *Requirements* (SRS) setelah prasyarat mitigasi risiko dipenuhi oleh Pemilik Usaha.

---

## 3. Deskripsi Proyek yang Dievaluasi

### 3.1. Nama dan Deskripsi Proyek
Proyek ini bernama **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**. Proyek ini mencakup perancangan dan pembangunan aplikasi manajemen internal terpadu berbasis teks (CLI) yang modular untuk mengotomatisasi seluruh kegiatan harian lima divisi usaha.

### 3.2. Tujuan Bisnis Proyek
Menghilangkan ketergantungan pada pencatatan manual Microsoft Excel yang tidak terintegrasi, mengotomatisasi pembukuan laba rugi instan per divisi, menerapkan manajemen persediaan berbasis komposisi bahan baku (*Bill of Materials*), mencegah pesanan pelanggan terlewat (*zero-missed orders*), serta mempersiapkan pondasi sistem operasi digital yang siap dikembangkan untuk ekspansi cabang baru (*multi-branch ready*).

### 3.3. Ruang Lingkup Proyek yang Dievaluasi
Ruang lingkup aplikasi yang dievaluasi mencakup 9 modul fungsional utama:

1. **M.1. Modul Manajemen Transaksi & Kebijakan Harga**
   - *Deskripsi*: Melayani pembayaran Uang Muka (DP) bertahap dan pelunasan, serta mendukung dinamika skema harga ritel, grosir, dan mitra secara terpadu.
   - *Kompleksitas Teknis*: Menengah. Harus diolah menggunakan *pattern matching* dalam FP murni guna menghindari mutasi data (perubahan status transaksi mutlak imutabel).
2. **M.2. Modul Manajemen Inventaris, BOM & Stock Opname**
   - *Deskripsi*: Automasi perhitungan Harga Pokok Penjualan (HPP) berbasis komposisi multi-bahan baku (BOM), kalkulasi stok berdimensi desimal presisi (*float*), manajemen limbah (waste), hingga integrasi pemindahan barang retail dan fitur *Stock Opname*.
   - *Kompleksitas Teknis*: Tinggi. Membutuhkan proses *pure functions* secara rekursif dan penerapan ketepatan tipe data desimal agar pencatatan presisi volume/panjang tidak berisiko terjadi pembulatan galat.
3. **M.3. Modul Layanan Keuangan Digital, PPOB, Jasa Keuangan & Service**
   - *Deskripsi*: Pencatatan mutasi saldo manual untuk transaksi pulsa, paket data, PPOB, jasa transfer bank, tarik tunai, serta log reparasi servis PC/Printer pelanggan.
   - *Kompleksitas Teknis*: Rendah. Tidak ada sinkronisasi otomatis ke gerbang API eksternal (*payment gateway*), sehingga operasi bersifat CRUD pencatatan log transaksi standar.
4. **M.4. Modul Manajemen SDM, Penggajian & Poin Karyawan**
   - *Deskripsi*: Sistem kelola presensi harian, administrasi kasbon pinjaman, sistem penggajian dinamis (gaji persentase atau gaji tetap berdasarkan laba perusahaan), serta konversi poin insentif beban kerja harian.
   - *Kompleksitas Teknis*: Tinggi. Logika kondisional berlapis untuk menggabungkan variabel presensi, utang pemotongan kasbon, akumulasi transaksi, dan capaian target finansial ke dalam satu *pipeline* rekursif fungsional tanpa menimbulkan interupsi mutasi *state*.
5. **M.5. Modul Sistem Manajemen Antrian & Pelacakan Desain**
   - *Deskripsi*: Pelacakan *Job Tracking* siklus desain dengan lima tahapan: `Antri` -> `Proses Desain` -> `Produksi` -> `Selesai` -> `Diambil`, disertai manajemen tautan ke jalur map desain komputer (arsip).
   - *Kompleksitas Teknis*: Menengah. Modifikasi sekuensial *record* database yang dipicu oleh instruksi operasional CLI di *frontend*.
6. **M.6. Modul Administrasi Pinjaman, Aset, & Pengeluaran Rutin**
   - *Deskripsi*: Sistem *tracking* pengeluaran rutin operasional bulanan, pelunasan pokok utang serta bunga bank, pengembalian penarikan fleksibel investasi sahabat, hingga manajemen depresiasi aset dan tabungan hardware baru.
   - *Kompleksitas Teknis*: Menengah. Melibatkan kalkulasi linier matematis untuk mengolah perhitungan persentase tenor bulanan utang berbunga.
7. **M.7. Modul Keamanan, Audit Trail & Hak Akses**
   - *Deskripsi*: Otorisasi sesi berbasis profil *Role-Based Access Control* (RBAC) bagi kelompok hierarki Pemilik Usaha dan Karyawan, didukung dengan jejak log *Audit Trail* modifikasi format JSON, serta fasilitas penyiapan data inisial *(data seeding)* manual.
   - *Kompleksitas Teknis*: Tinggi. Menuntut implementasi algoritma JWT *stateless*, integrasi *hash bcrypt*, dan penerapan sistem izin yang menyekat alur operasi *backend* sejak dari gerbang penerimaan input.
8. **M.8. Modul Pembatalan, Retur & CRM**
   - *Deskripsi*: Pembatalan/retur transaksi kompleks yang mengembalikan kembali sisa stok gudang riil, serta pengolahan buku kontak pelanggan (CRM WhatsApp dan direktori histori pesanan).
   - *Kompleksitas Teknis*: Menengah. Memerlukan *soft-rollback* dan transaksi tipe *COMMIT* terstruktur dari *database* (MySQL).
9. **M.9. Skalabilitas Multi-Cabang**
   - *Deskripsi*: Inklusi relasional pengenal entitas `cabang_id` sejak perancangan awal pangkalan data (*Multi-Branch Ready*), demi kehandalan ekspansi replikasi arsitektur di masa depan.
   - *Kompleksitas Teknis*: Menengah. Skema normalisasi awal *database* relasional.

### 3.4. Stakeholder Utama
*   **Pemilik Usaha AbuCom**: Sponsor Utama, Manajer Proyek (Junior Programmer), dan Pengguna Utama.
*   **Calon Staf Karyawan (7 Posisi)**: Pengguna operasional harian sistem (Kepala Percetakan, Pramuniaga, Kasir, Desainer, Produksi Cetak, Fotocopy/Print, Staf Gudang).
*   **Kreditur**: Bank Mandiri & Bank BRI (pinjaman berbunga) serta Sahabat/Kerabat/Keluarga (pinjaman tanpa bunga).

### 3.5. Asumsi dan Batasan Studi Kelayakan
Untuk menjaga kredibilitas dan keandalan analisis evaluasi ini, ditetapkan beberapa asumsi dan batasan analisis:
*   **Asumsi Keuangan**: Nilai CAPEX Rp 40.000.000 terkunci dan tidak mengalami fluktuasi harga >10% sebelum pengadaan. Manfaat finansial terukur dihitung dengan asumsi stabilitas volume pesanan bulanan rata-rata seperti tahun operasional berjalan.
*   **Asumsi Organisasional**: Proses rekrutmen untuk 7 staf baru selesai tepat waktu sebelum Go-Live.
*   **Batasan Teknis**: Evaluasi didasarkan pada antarmuka CLI yang dijalankan secara lokal *client-server* via LAN Cat6 di 1 cabang fisik, dengan pembatasan mutlak tidak menggunakan konsep *Object-Oriented Programming* (OOP) pada logika bisnis inti program Python.

---

## 4. Analisis Kelayakan Teknis (Technical Feasibility)

### 4.1. Evaluasi Teknologi yang Dipilih

#### 4.1.1. Bahasa Pemrograman (Python 3.14.2+ & Functional Programming)
*   **Kelebihan**: Python memiliki ekosistem yang matang, pustaka standar yang melimpah, serta portabilitas tinggi di lintas OS. Penggunaan paradigma *Functional Programming* (FP) murni (fungsi murni, imutabilitas, *higher-order functions*) meningkatkan keamanan, testabilitas, dan mengeliminasi efek samping (*side-effects*) dalam perhitungan HPP dan keuangan.
*   **Tantangan**: FP murni di Python memiliki kurva pembelajaran yang sangat curam untuk programer tingkat junior karena Python secara bawaan merupakan bahasa multi-paradigma yang condong ke OOP/imperatif. Manajemen *state* aplikasi tanpa menggunakan entitas objek akan membutuhkan abstraksi arsitektur yang cukup tinggi.
*   **Penilaian**: **Layak dengan Catatan** (Catatan: Diperlukan bimbingan intensif dari asisten AI spesialis *deep coding* seperti Claude Sonnet 4.6 untuk menyusun kerangka *state management* fungsional).

#### 4.1.2. Sistem Basis Data (MySQL)
*   **Kelebihan**: MySQL Community Server merupakan *database* relasional berskala industri yang stabil, gratis, berkinerja tinggi, dan mendukung kepatuhan ACID (Atomicity, Consistency, Isolation, Durability) yang sangat krusial untuk transaksi keuangan terintegrasi AbuCom.
*   **Penilaian**: **Layak** (Sangat sesuai untuk skala data UMKM dan siap mendukung arsitektur relasional multi-cabang).

#### 4.1.3. Pustaka Pendukung
*   `mysql-connector-python` (driver DB standar), `python-dotenv` (keamanan kredensial), `bcrypt` (enkripsi satu arah sandi), dan `pyjwt` (autentikasi *session* CLI). Seluruh *library* ini bersifat *open-source*, stabil, dan memiliki dokumentasi melimpah.
*   **Penilaian**: **Layak**.

#### 4.1.4. Platform & Sistem Operasi
*   Aplikasi CLI Python dan database MySQL dapat dijalankan lintas OS pada terminal Linux Debian 12 Bookworm (Server lokal) maupun Windows 11 (PC Kasir) tanpa ada modifikasi logika inti.
*   **Penilaian**: **Layak**.

#### 4.1.5. Antarmuka (CLI / Console)
*   **Kelebihan**: Aplikasi CLI sangat ringan, tidak membutuhkan kartu grafis, memiliki waktu respon yang instan (< 1 detik), bebas dari *overhead rendering* GUI, dan sangat cepat dioperasikan oleh kasir berpengalaman menggunakan pintasan keyboard (*hotkeys*).
*   **Tantangan**: Aspek estetika visual sangat minim (hanya berbasis teks) dan membutuhkan waktu adaptasi lebih lama bagi staf baru yang terbiasa dengan antarmuka berbasis grafis (GUI).
*   **Penilaian**: **Layak dengan Catatan** (Catatan: Antarmuka teks harus dirancang dengan tata letak menu yang intuitif, kode warna ANSI untuk pembeda status, dan petunjuk input yang jelas).

### 4.2. Evaluasi Kompleksitas Fitur Utama
Kompleksitas tinggi bersumber dari tuntutan algoritma murni pada logika fungsional, terutamanya terkait perhitungan persediaan berbasis komposisi BOM (M.2) maupun sistem perhitungan insentif *payroll* gaji adaptif (M.4) yang melibatkan multi-kondisi dari presensi hingga akumulasi beban *point*. Evaluasi teknis menyoroti bahwa modul kalkulasi persediaan dapat difasilitasi dengan aman menggunakan `decimal` bawaan Python dan pengolahan rekursi `reduce` / `map`, selama tipe desimal di *database* relasional disesuaikan. Pemrosesan stateful antrian operasi (M.5) diwajibkan memberikan rujukan instansiasi kembalian data baru (imutable), dijamin kapabel sepenuhnya jika diolah secara disiplin. 

### 4.3. Evaluasi Kapabilitas Tim Pengembang
Kolaborasi tim pengembang tergolong unik dan berpotensi sangat efektif: 1 Junior Programmer (Pemilik Usaha yang bertindak sebagai PM & integrator) dibantu oleh 6 model AI spesialis dengan tugas terstruktur (Gemini 3.1 Pro untuk logika arsitektur berat, Claude Sonnet 4.6 untuk penulisan kode fungsional mendalam, dan Claude Opus untuk keamanan/strategi).
*   **Risiko**: Risiko terbesar adalah ketidakcocokan kode program saat Junior Programmer melakukan penggabungan (integrasi) modul-modul FP dari AI yang berbeda.
*   **Penilaian**: **Layak dengan Catatan** (Catatan: Junior Programmer harus disiplin melakukan *review* sintaksis cepat menggunakan Gemini 3 Flash serta mematuhi standardisasi struktur kode di bawah arahan Lead Architect AI).

### 4.4. Evaluasi Infrastruktur Teknis yang Dibutuhkan
Kebutuhan fisik infrastruktur untuk mendukung topologi Client-Server lokal di toko percetakan sangat minimal:
1.  **Server Lokal**: 1 Unit Mini PC (Core i5, 16GB RAM, SSD 512GB) yang berfungsi sebagai *host* server database MySQL lokal.
2.  **Klien CLI**: PC Kasir/Operasional yang terhubung via jaringan kabel LAN (UTP Cat6) ke server lokal.
3.  **Daya Cadangan**: 2 Unit UPS untuk melindungi Mini PC Server dan PC Kasir dari kerusakan integritas data *database* akibat pemadaman listrik tiba-tiba.
*   **Penilaian**: **Layak** (Infrastruktur ini standar, murah, dan sangat memadai untuk operasional UMKM).

### 4.5. Risiko Teknis dan Mitigasi

| No | Risiko Teknis | Probabilitas | Dampak | Rencana Mitigasi |
|----|---------------|:------------:|:------:|------------------|
| 1  | **Kebocoran Memori atau Rekursi Tak Terbatas**: Kesalahan logika FP murni (rekursi tak terbatas) di Python yang dapat menyebabkan memori server penuh (*stack overflow*). | 2 | 4 | Batasi kedalaman rekursi di Python, prioritaskan penggunaan iterasi fungsional (`map/filter` atau generator *lazy-evaluation*) yang lebih aman bagi alokasi memori. |
| 2  | **Korup Data Database Akibat Mati Listrik**: Listrik mati mendadak saat transaksi database MySQL sedang berlangsung. | 3 | 4 | Terapkan transaksi *database* dengan skema `COMMIT` & `ROLLBACK` yang ketat di MySQL, serta gunakan UPS penstabil daya cadangan untuk Mini PC Server. |
| 3  | **Kesalahan Pembulatan Desimal**: Nilai desimal persediaan bahan baku (panjang/lebar/cairan) tidak sinkron akibat pembulatan *floating point* standar Python. | 3 | 3 | Gunakan modul bawaan `decimal` di Python dengan pengaturan presisi tetap (misal: 4 angka di belakang koma) untuk menjamin akurasi perhitungan matematika inventaris. |

### 4.6. Kesimpulan Kelayakan Teknis
$$\color{orange}{\textbf{LAYAK DENGAN CATATAN (FEASIBLE WITH CONDITIONS)}}$$

Teknologi yang dipilih (Python CLI + MySQL) sangat matang dan andal untuk mengotomatisasi sistem operasional AbuCom. Catatan utama terletak pada disiplin penerapan paradigma *Functional Programming* murni untuk menghindari efek samping pengolahan data serta penanganan visual antarmuka CLI agar tetap ramah digunakan oleh staf operasional.

---

## 5. Analisis Kelayakan Operasional (Operational Feasibility)

### 5.1. Kesiapan Organisasi dan SDM

#### 5.1.1. Kondisi Operasional Saat Ini (Single-Fighter)
Kondisi saat ini sangat tidak berkelanjutan. Pemilik bertindak sebagai *single point of failure* yang melakukan segalanya secara manual, mulai dari mendesain, mencetak, melayani kasir, hingga memantau stok bahan. Adopsi sistem baru akan memberikan dampak positif yang sangat signifikan bagi pemulihan kesehatan mental pemilik usaha dengan memangkas beban administratif harian.

#### 5.1.2. Rencana Rekrutmen 7 Posisi Staf
Pemilik telah memiliki rencana pembagian divisi kerja yang solid untuk 7 posisi operasional (Kepala Percetakan, Pramuniaga, Kasir, Desainer, Produksi Cetak, Fotocopy/Print, Staf Gudang). Rencana ini sangat realistis untuk mendukung efisiensi operasional. Namun, kesuksesan operasional sistem bergantung penuh pada keberhasilan rekrutmen staf ini sebelum sistem diterapkan (Go-Live).

#### 5.1.3. Kesiapan Literasi Digital Pengguna
*   **Pemilik Usaha**: Memiliki latar belakang cukup (bertindak sebagai Junior Programmer), sehingga memiliki kesiapan digital yang sangat baik untuk mengelola server basis data.
*   **Karyawan Staf Baru**: Latar belakang calon karyawan kemungkinan sangat bervariasi. Penggunaan sistem berbasis teks (CLI) yang tidak memiliki visual tombol grafis berpotensi memicu kesulitan adaptasi awal dan kebingungan input perintah teks.

### 5.2. Dampak Perubahan Proses Bisnis (dari Manual Excel ke CLI)
Transisi dari *file* Excel manual yang terpisah-pisah menuju sistem CLI database terpadu akan merevolusi alur kerja:
*   Transaksi kas langsung terhubung dengan pemotongan stok bahan baku secara *real-time* via skema BOM.
*   Pencatatan limbah produksi (*waste management*) terdokumentasi terpisah untuk rekonsiliasi stok.
*   Dampak awal: Staf operasional akan menghadapi beban kerja tambahan untuk menginput data awal persediaan secara manual dari data Excel lama yang tidak terstruktur. Namun, setelah fase input selesai, beban operasional harian diproyeksikan terpangkas hingga **90%**.

### 5.3. Penerimaan Pengguna (User Acceptance)
Tingkat penerimaan dari pemilik usaha diproyeksikan mencapai **100% (Sangat Tinggi)** karena sistem ini diinisiasi langsung oleh pemilik untuk mengatasi masalah pribadinya (*burnout*). Untuk karyawan baru, potensi resistensi dapat dieliminasi melalui struktur menu CLI yang konsisten dan dukungan dokumentasi instruksi yang ringkas.

### 5.4. Kebutuhan Pelatihan dan Manajemen Perubahan
Telah direncanakan program pelatihan sistem selama **3 hari** berupa simulasi operasional penuh (dari melayani pelanggan, input DP, proses antrian, produksi, pencatatan limbah, hingga pelunasan di kasir dan *stock opname*). Durasi 3 hari dinilai cukup memadai jika didukung oleh skenario simulasi yang matang dan tersedianya berkas *CLI User Manual* yang mudah dipahami.

### 5.5. Dukungan Operasional Pasca Go-Live
Junior Programmer (Pemilik Usaha) akan memegang peran utama sebagai administrator teknis lokal di toko. Tim asisten AI akan selalu siaga mendukung penyelesaian masalah *bug* perangkat lunak secara asinkron.
*   **Penilaian**: **Layak**.

### 5.6. Risiko Operasional dan Mitigasi

| No | Risiko Operasional | Probabilitas | Dampak | Rencana Mitigasi |
|----|--------------------|:------------:|:------:|------------------|
| 1  | **Keterlambatan Rekrutmen Karyawan Baru**: Karyawan belum lengkap saat sistem siap Go-Live, sehingga pemilik terpaksa mengoperasikan CLI sendirian dan tetap mengalami burnout. | 3 | 5 | Lakukan proses rekrutmen staf secara paralel pada Bulan 9-10 saat aplikasi memasuki Fase Implementasi Akhir. |
| 2  | **Human Error Input Perintah CLI**: Karyawan salah menginput kode produk atau perintah teks yang dapat mengacaukan antrian atau transaksi. | 4 | 3 | Implementasikan fitur konfirmasi input (misal: "Apakah data transaksi sudah benar? [Y/N]") dan fungsi pembatalan bertahap (*soft-rollback*) di aplikasi. |
| 3  | **Resistensi Budaya Kerjasama Tim**: Karyawan enggan membantu divisi lain (*cross-functional*) karena merasa di luar deskripsi kerja mereka. | 3 | 3 | Gunakan sistem Poin Insentif Karyawan yang adil untuk menghargai setiap bantuan kerja lintas divisi secara transparan. |

### 5.7. Kesimpulan Kelayakan Operasional
$$\color{orange}{\textbf{LAYAK DENGAN CATATAN (FEASIBLE WITH CONDITIONS)}}$$

Sistem ini sangat mendesak dan layak untuk membebaskan Pemilik Usaha dari masalah *burnout* operasional harian. Catatan penting keberhasilan operasional terletak pada **disiplin rekrutmen staf tepat waktu** dan **efektivitas pelatihan simulasi 3 hari** untuk memastikan seluruh staf baru mampu mengoperasikan terminal CLI tanpa kebingungan teknis.

---

## 6. Analisis Kelayakan Ekonomi / Finansial (Economic Feasibility)

### 6.1. Estimasi Biaya Pengembangan (Capital Expenditure - CAPEX)
Berdasarkan data anggaran terstruktur pada Project Charter, total investasi awal pengembangan sistem adalah **Rp 40.000.000**. Biaya ini dialokasikan ke 5 komponen pokok berikut:
1.  **Perangkat Keras (Hardware)** (Mini PC Server, PC Kasir, 2 UPS): Rp 15.500.000.
2.  **Infrastruktur Jaringan** (Router, Switch UTP Cat6, Jasa teknisi): Rp 2.500.000.
3.  **Biaya Pengembangan Software** (Token API AI premium & konsumsi logistik Junior PM): Rp 15.000.000.
4.  **Pelatihan Staf & Operasional Awal** (Konsumsi 3 hari pelatihan dan pencetakan modul *User Manual*): Rp 2.500.000.
5.  **Dana Cadangan Darurat (Contingency Fund)**: Rp 4.500.000.
*   **Evaluasi**: Anggaran kapital sejumlah Rp 40 juta sangat efisien dan realistis untuk ukuran UMKM percetakan karena meniadakan sepenuhnya biaya sewa berulang atas lisensi komersial sistem operasi dan peranti lunak manajemen *database*.

### 6.2. Estimasi Biaya Operasional Berkelanjutan (Operational Expenditure - OPEX)
Data berikut adalah proyeksi estimasi analitik berdasarkan standar pemeliharaan infrastruktur ritel digital, dan akan disesuaikan saat sistem berjalan riil:
Biaya operasional bulanan pasca Go-Live diestimasi mencakup pengeluaran berikut:
*   Listrik Tambahan Mini PC Server & PC Klien: Rp 150.000 / bulan.
*   Pemeliharaan Peralatan Jaringan & Hardware Fisik: Rp 150.000 / bulan.
*   Alokasi Token Akses API AI Sekunder (Untuk diagnosa bug dan resolusi insidental): Rp 200.000 / bulan.
*   **Total OPEX Bulanan**: **Rp 500.000 / bulan** (atau **Rp 6.000.000 / tahun**).

### 6.3. Estimasi Manfaat Finansial (Tangible Benefits)
Data proyeksi manfaat finansial berikut adalah perhitungan estimasi berlandaskan ukuran rata-rata transaksi dan kapasitas layanan percetakan UMKM di kelas yang serupa:
Penerapan aplikasi ini ditargetkan memberikan penghematan dan peningkatan profitabilitas terukur:
1.  **Penghematan Waktu Pembukuan Administratif**: Reduksi drastis waktu rekapitulasi data fisik dari 2-3 jam/hari menjadi instan. Apabila nilai produktivitas tenaga pengerjaan ini dialokasikan, akan bernilai senilai Rp 1.500.000 / bulan.
2.  **Efisiensi Pengendalian Limbah Bahan Baku (Turun 15%)**: Mencegah kebocoran berlebih stok bahan baku cetak yang diretur atau salah cetak berkat keharusan audit melalui modul pencatatan limbah *waste management*. Diestimasikan mampu menghemat beban biaya bahan senilai Rp 1.200.000 / bulan.
3.  **Penyelamatan Transaksi Terlewat (Zero-Missed Orders)**: Penyelamatan penyelesaian tagihan secara faktual atas 3-5 antrean pesanan produk *custom* (seperti cetak stempel khusus, yasin, dan baliho) yang pada prosedur terdahulu kerap tertunda/lupa akibat beban *burnout* pikiran pemilik tunggal. Nilai omzet kotor per bulan yang tervalidasi dapat diselamatkan diestimasikan sebesar Rp 2.000.000 / bulan.
*   **Total Manfaat Tangible**: **Rp 4.700.000 / bulan** (atau **Rp 56.400.000 / tahun**).

### 6.4. Estimasi Manfaat Non-Finansial (Intangible Benefits)
*   **Reduksi Stres Ekstrem**: Pemulihan drastis kondisi kesehatan mental psikologis Pemilik Usaha dari jebakan *burnout* kronis harian.
*   **Peningkatan Kepercayaan Layanan (*Brand Trust*)**: Memastikan pelayanan interaksi tamu pelanggan jauh lebih tepat waktu, terkelola, dan tampil profesional secara digital.
*   **Proteksi Keamanan Kas Internal**: Menghapuskan celah kecurangan keuangan rawan penipuan (frauds) dari staf karyawan karena intervensi keamanan ketat arsitektur perlindungan hak akses RBAC eksklusif.
*   **Kesiapan Agresivitas Ekspansi Bisnis**: Meresmikan keberadaan struktur standardisasi perangkat lunak yang *multi-branch ready* yang mampu direplikasi seketika (duplikasi arsitektur) bilamana pemodal bermaksud melebarkan sayap unit usaha pertokoan di lokasi kota sekunder lain.

### 6.5. Analisis Biaya-Manfaat (Cost-Benefit Analysis)
Data matriks disimulasikan sebagai parameter evaluasi proyeksi untuk durasi pengerjaan setahun awal (*Tahun 0*) dilanjutkan dua tahun operasional produktif (Tahun 1 & 2):

| Deskripsi | Tahun 0 (Pengembangan) | Tahun 1 (Operasional) | Tahun 2 (Operasional) |
|-----------|------------------------|-----------------------|-----------------------|
| **Biaya Investasi (CAPEX)** | Rp 40.000.000 | Rp 0 | Rp 0 |
| **Biaya Operasional (OPEX)** | Rp 0 | Rp 6.000.000 | Rp 6.000.000 |
| **Total Biaya Terkalkulasi**| **Rp 40.000.000** | **Rp 6.000.000** | **Rp 6.000.000** |
| **Manfaat Finansial Akumulatif** | Rp 0 | Rp 56.400.000 | Rp 56.400.000 |
| **Arus Kas Bersih (Net Benefit)** | **(Rp 40.000.000)** | **Rp 50.400.000** | **Rp 50.400.000** |

### 6.6. Net Present Value (NPV)
Penilaian *Net Present Value* diproyeksikan dengan penerapan *discount rate* yang wajar sebesar **10% per tahun** mengacu kepada kalkulasi penyesuaian nilai penyusutan suku bunga makro industri layanan mikro/menengah saat ini di Indonesia. Hasil NPV pada siklus investasi periode dua tahun awal operasional aplikasi dipaparkan sebagai berikut:
*   Tahun 0 (Aliran Kas Pengembangan Awal): (Rp 40.000.000)
*   Tahun 1 (Present Value dari Net Benefit Rp 50.400.000): Rp 45.818.182
*   Tahun 2 (Present Value dari Net Benefit Rp 50.400.000): Rp 41.652.893
*   Total Present Value dari keseluruhan Manfaat Bersih (Tahun 1+2): Rp 87.471.075

$$\text{NPV} = \text{Total PV of Benefits} - \text{CAPEX}$$
$$\text{NPV} = \text{Rp 87.471.075} - \text{Rp 40.000.000} = \text{Rp 47.471.075}$$

Karena hasil kalkulasi metrik kelayakan **NPV terbukti bernilai positif (Rp 47.471.075)**, pengerjaan proyek perangkat lunak kustom ini sangat menguntungkan sehingga dari perspektif validasi penanaman kapital internal AbuCom ditetapkan statusnya sebagai **Sangat Layak**.

### 6.7. Estimasi Return on Investment (ROI)
Tingkat persentase rasio pengembalian modal pada titik ekuilibrium akhir di Tahun 1 dipaparkan dalam formula sederhana:

$$\text{ROI} = \frac{\text{Net Benefit Tahun 1} - \text{CAPEX}}{\text{CAPEX}} \times 100\%$$
$$\text{ROI} = \frac{\text{Rp 50.400.000} - \text{Rp 40.000.000}}{\text{Rp 40.000.000}} \times 100\% = 26.0\%$$

Pengembalian investasi bersih proyek membukukan indikator keuntungan yang prestisius pada besaran marjin **26.0%** pasca penutupan masa produksi tahun 1, sehingga merefleksikan nilai tambah investasi teknologi internal yang amat meyakinkan bagi pengelola finansial usaha mikrobisnis.

### 6.8. Estimasi Payback Period (Periode Pengembalian Modal)
Menghitung kecepatan rentang tempo pengumpulan aset dana kembali berlandaskan nominal bersih (Net Benefit Bulanan sejumlah Rp 4.200.000 per bulan yang disarikan dari pengurangan keuntungan kotor operasional [Rp 4.700.000] terhadap OPEX rutin [Rp 500.000]):

$$\text{Payback Period} = \frac{\text{Total CAPEX}}{\text{Net Benefit Bulanan}} = \frac{\text{Rp 40.000.000}}{\text{Rp 4.200.000 / bulan}} = 9.5 \text{ Bulan}$$

Investasi *sunk-cost* awal penganggaran CAPEX sejumlah Rp 40.000.000 diproyeksikan akan **kembali tertutupi dengan tuntas dan lunas dalam masa berjalan 9,5 bulan** pasca inisiasi peresmian fase produksi operasional (Go-Live) aplikasi.

### 6.9. Analisis Titik Impas (Break-Even Point - BEP)
Uji Break-Even Point kelayakan ketahanan produksi dirumuskan pada 2 skenario pembuktian variabel operasional logistik ritel cetak:
1.  **BEP Berdasarkan Tempo Waktu Siklus Produksi Operasional**: Parameter ekuilibrium antara kompensasi injeksi modal awal perangkat CAPEX dan tanggungan biaya daya utilitas peladen OPEX secara kumulatif terpenuhi seketika di kalender berjalan di **bulan ke-9,5** di masa aplikasi digunakan produktif oleh konsumen ritel reguler percetakan.
2.  **BEP Berdasarkan Tolok Ukur Beban Volume Faktur Transaksi Cetak (*Custom Orders*)**:
    *   Jika diasumsikan persentase laba kotor marjin atas selisih harga jual dan harga komponen baku sebuah penyelesaian jasa pencetakan desain per *invoice* senilai **Rp 50.000 / satuan pesanan**.
    *   *BEP Pemenuhan Dana Alat (CAPEX)*: Mewajibkan aplikasi perangkat menuntaskan pengelolaan manajemen siklus sikuen pencetakan secara sukses sebanyak **800 transaksi** nota order cetak pesanan untuk melunasi biaya akuisisi aset infrastruktur pengadaan (Rp 40.000.000 / Rp 50.000).
    *   *BEP Pemenuhan Biaya Bulanan (OPEX)*: Aplikasi operasional toko secara konsisten diwajibkan mampu menuntaskan beban kerja sejumlah nominal minimum **10 transaksi** pencetakan kustom tiap bulan. Menilik rekam jejak laju lalu-lintas omzet (*traffic*) reguler pemesanan pelanggan ke lokasi ruko pada jam ramai yang masif, beban porsi kecil sebanyak sepuluh faktur kustom tersebut merupakan suatu angka target absolut yang dinilai **luar biasa mudah direalisasikan**.

### 6.10. Analisis Sensitivitas (Proyeksi 3 Skenario)
Proyeksi evaluasi dampak fluktuasi anomali finansial ditranslasikan dalam matriks tiga uji simulasi ketahanan proyek (Sensitivitas Finansial Kelayakan Proyeksi):

*   **Skenario A: Situasi Puncak (Best Case Scenario)**
    *   Asumsi pendorong: Optimalisasi serapan tenaga pramuniaga meroketkan indeks rasio manfaat riil penghematan finansial hingga menyentuh margin puncak (Rp 5.500.000/bulan bersih) dengan retensi tagihan biaya operasional OPEX tetap konservatif pada kalkulasi dasar (tanpa pembengkakan listrik).
    *   *Proyeksi Waktu Pelunasan (Payback Period)*: Memendek secara signfikan menjadi rentang waktu pemulihan mutlak di **8 Bulan**.
*   **Skenario B: Basis Dasar Harapan (Base Case Scenario)**
    *   Asumsi penahan ekuilibrium: Pelaksanaan seluruh kerangka arsitektur berjalan seirama ketetapan dokumentasi acuan dengan margin standar (Manfaat kotor Rp 4.700.000/bulan) dan pencairan pemeliharaan OPEX stagnan pada Rp 500.000/bulan.
    *   *Proyeksi Waktu Pelunasan (Payback Period)*: Mengikuti formula perhitungan konvensional standar pada angka moderat di kalender masa berjalan penyelesaian proyeksi bulan yang ke-**9,5 Bulan**.
*   **Skenario C: Krisis Paling Kelam (Worst Case Scenario)**
    *   Asumsi pelemah kerangka: Terjadinya syok disrupsi kesulitan adopsi penyesuaian transisi antarmuka CLI terminal teks di hari pertama *training* operasional, sehingga manfaat nyata finansial efisiensi anjlok dramatis di titik minimal Rp 3.000.000 per bulan. Paralel dengan kondisi itu, fluktuasi tagihan daya listrik mengerek pembengkakan tagihan OPEX meningkat drastis di luar kewajaran mencapai titik Rp 700.000 per bulan, ditambah dengan keharusan membongkar seluruh deposit kas perisai Contingency Rp 4.500.000 sedari hari awal inisialisasi akibat klaim eksternal pinjaman tiba-tiba.
    *   *Proyeksi Waktu Pelunasan (Payback Period)*: Mundur secara kalkulatif hingga dua kali lipat menjadi tempo penyelesaian **19 Bulan** operasional penuh. Namun meski terpuruk demikian jauh, indikator waktu yang tercapai ini *terbukti nyata masih terselamatkan dan tertambat di bawah ambang batas waktu tenggat masa tenggang kritis proyek investasi berumur 2 Tahun (24 Bulan)*; memvalidasi status daya ketahanan proteksi kelayakan permodalan internal sebagai langkah bisnis yang dipertanggungjawabkan (Sangat Logis & Rasional untuk ditindaklanjuti).

### 6.11. Sumber Pendanaan dan Kemampuan Finansial
1.  **Sirkulasi Dana Laba Usaha**: Menjadi fondasi pendorong primer logistik yang dikucurkan secara parsial dari hasil jerih operasional konvensional toko.
2.  **Pinjaman Komersial Institusi Perbankan (Bank BRI & Mandiri)**: Pemodal utama aset riil infrastruktur alat, memastikan fleksibilitas alur pengerjaan tak pernah tertunda asalkan tempo jadwal amortisasi rutinan hutang bulanan terpenuhi secara disiplin (menghindari kredit macet).
3.  **Bantuan Pembiayaan Non-Komersial (Tabungan Keluarga / Kerabat)**: Pemasok modal lunak nir-bunga penyokong pengerjaan peranti perangkat lunak AI, fleksibel menopang tanpa batas waktu absolut kalender.
    *   *Risiko Kritis Penopang Dana*: Kelenturan waktu ini adalah pisau bermata dua. Pemodal kerabat dapat saja mendadak mencabut izin pemanfaatan keseluruhan likuiditasnya. Hal itu sangat berpotensi memorakporandakan ketersediaan dana pemeliharaan *software*, memberhentikan kompensasi pengembangan tenaga SDM di luar perhitungan.

### 6.12. Risiko Finansial dan Mitigasi

| No | Risiko Finansial | Probabilitas | Dampak | Rencana Mitigasi |
|----|------------------|:------------:|:------:|------------------|
| 1  | **Penarikan Dana Mendadak oleh Sahabat/Keluarga**: Likuiditas kas terganggu karena pinjaman tanpa bunga ditarik tiba-tiba saat pengerjaan modul kritis. | 3 | 4 | Gunakan alokasi Dana Cadangan Darurat Rp 4.500.000 khusus untuk mengunci biaya teknis *software*, jangan campur dengan kas toko. |
| 2  | **Kenaikan Harga Hardware Lokal**: Harga Mini PC Server atau PC Kasir naik tajam di pasar Indonesia sebelum sempat dibeli. | 3 | 2 | Lakukan pembelian perangkat keras utama (Mini PC Server & UPS) di Bulan ke-5 (Awal Fase Implementasi) untuk mengunci harga. |
| 3  | **Beban Bunga Bank Mengganggu Operasional**: Aliran kas tersedot untuk membayar setoran bulanan Bank BRI/Mandiri di tengah penurunan omzet sementara. | 2 | 4 | Buat modul pencatatan pengingat jatuh tempo setoran bank bulanan untuk menghindari denda keterlambatan pembayaran. |

### 6.13. Kesimpulan Kelayakan Ekonomi
$$\color{orange}{\textbf{LAYAK DENGAN CATATAN (FEASIBLE WITH CONDITIONS)}}$$

Secara finansial, proyek kustom CLI Python ini sangat menguntungkan dengan estimasi *Payback Period* yang cepat (9,5 bulan), ROI tinggi (26%), dan NPV yang sangat positif (Rp 47.471.075). Catatan kelayakan terletak pada **pengelolaan likuiditas modal pinjaman tanpa bunga** yang harus dipisahkan dari modal kerja harian toko untuk mengantisipasi penarikan dana mendadak.

---

## 7. Analisis Kelayakan Jadwal (Schedule Feasibility)

### 7.1. Timeline yang Direncanakan (12 Bulan)
Telah disusun jadwal tingkat tinggi yang terbagi menjadi 8 milestone besar selama 12 bulan (Tenggat Acuan: Mei 2026 s.d. Mei 2027):
*   **M.1. Perencanaan (Bulan 1 - Mei 2026)**: Penyusunan Project Charter dan Feasibility Study (Selesai).
*   **M.2. Analisis Requirements (Bulan 2)**: Penyusunan dokumen formal SRS (Status: Terbuka).
*   **M.3. Desain Sistem & DB (Bulan 3-4)**: Rancangan logikal SDD, skema JWT RBAC, & rancangan ERD tabel *multi-branch ready*.
*   **M.4. Implementasi Fase I (Bulan 5-6)**: Rilis versi *Alpha* (Dasar operasional CLI Python FP, otentikasi login *bcrypt*, importase CSV/Excel manual awal modul pelanggan CRM & basis kas).
*   **M.5. Implementasi Fase II (Bulan 7-9)**: Peluncuran versi krusial pengolah logika *decimal* BOM Inventaris & HPP, digabung kalkulasi dinamis presensi serta modul kasbon insentif kinerja *point* (Payroll cerdas), plus transisi papan status pesanan Antrean (M.5).
*   **M.6. Implementasi Fase III (Bulan 10)**: Modul Laba/Rugi, jadwal beban kredit bank (Pinjaman modal), laporan aset penyusutan (Tabungan perangkat keras baru), rekap utilitas operasi, & pengaktifan fungsi pemantau senyap *Audit Trail*.
*   **M.7. Integrasi & Pengujian (Bulan 11)**: Pelaksanaan validasi asersi skenario Uji Terpadu (SIT) interaktif simulasi beban & validasi User Acceptance Testing (UAT).
*   **M.8. Go-Live & Pelatihan (Bulan 12 - Mei 2027)**: Integrasi lingkungan OS final Linux Debian 12 untuk Server beserta klien terminal Windows 11 di pertokoan riil, dilanjutkan sesi ekstensif praktek modul terminal 3 Hari Penuh tanpa *database* kotor kepada 7 awak staf baru operasional toko kasir depan.

### 7.2. Evaluasi Kerealistisan Jadwal per Fase
*   **Durasi Keseluruhan (12 Bulan)**: Sangat longgar dan realistis untuk skala aplikasi internal UMKM. Rata-rata pengembangan aplikasi sejenis hanya membutuhkan waktu 4-6 bulan. Alokasi 12 bulan memberikan ruang yang sangat aman bagi Pemilik Usaha yang bertindak sebagai Junior Programmer di tengah kesibukan mengelola toko.
*   **Bulan 7-9 (Implementasi Fase II - Persediaan & SDM)**: Alokasi 3 bulan dinilai sangat realistis untuk menyelesaikan logika terberat (BOM desimal dan skema penggajian otomatis) karena modul-modul ini dikerjakan secara paralel oleh Claude Sonnet 4.6 (spesialis *deep coding*) dan Gemini 3.1 Pro.
*   **Bulan 11 (Testing & UAT)**: Alokasi 1 bulan sangat memadai untuk melakukan pengujian manual CLI secara menyeluruh oleh Junior Programmer dan calon staf baru.

### 7.3. Identifikasi Jalur Kritis (Critical Path)
Jalur kritis proyek (keterlambatan pada fase ini akan menunda Go-Live proyek) meliputi:
1.  **Fase 3: Desain Basis Data (Bulan 3-4)**: Skema *database multi-branch ready* harus benar dan matang sejak awal. Jika skema *database* salah, seluruh implementasi kode program di bulan berikutnya harus dirombak total.
2.  **Fase 5: Uji Coba HPP BOM (Bulan 7-9)**: Logika matematika dimensi desimal presisi harus divalidasi keakuratannya sebelum masuk ke modul keuangan terintegrasi.

### 7.4. Faktor yang Dapat Memperlambat Jadwal
*   **Stres dan Burnout Pemilik**: Karena pemilik mengelola toko sendirian selama masa pengembangan, kelelahan fisik dapat menunda sesi klarifikasi kebutuhan atau pengujian modul *sprint*.
*   **Kerumitan FP di Python**: Menolak OOP dan memaksa menulis kerangka kerja *Functional Programming* murni untuk fitur dinamis berpotensi memicu kendala penulisan kode yang memperlambat pengerjaan Junior Programmer.

### 7.5. Risiko Jadwal dan Mitigasi

| No | Risiko Jadwal | Probabilitas | Dampak | Rencana Mitigasi |
|----|---------------|:------------:|:------:|------------------|
| 1  | **Burnout Pemilik Menghentikan Ulasan Proyek**: Pemilik sakit/kelelahan sehingga tidak sempat mereview hasil *sprint coding* 2 mingguan. | 3 | 5 | Serahkan penulisan dokumentasi rutin sepenuhnya kepada Gemini 3.1 Pro (Low) dan optimalkan waktu pemilik hanya untuk *testing* fungsional CLI yang krusial. |
| 2  | **Kerumitan Sintaksis FP Memperlambat Kodifikasi**: Kesulitan merancang alur *state* fungsional yang bersih dari OOP. | 2 | 4 | Gunakan pustaka standar `functools` dan manfaatkan Claude Sonnet 4.6 secara intensif untuk melakukan refaktorisasi kerangka program sejak awal implementasi. |
| 3  | **Input Data Awal Excel yang Berserakan Memakan Waktu**: Proses menyalin data dari Excel lama ke database MySQL memakan waktu berminggu-minggu. | 4 | 3 | Buatkan menu import CSV/Excel sederhana pada aplikasi CLI di akhir Fase I untuk mempercepat proses migrasi data awal secara semi-otomatis. |

### 7.6. Kesimpulan Kelayakan Jadwal
$$\color{green}{\textbf{LAYAK (FEASIBLE)}}$$

Dengan alokasi total durasi 12 bulan yang didukung metodologi pengembangan Hybrid (Waterfall-Agile), serta bantuan intensif dari 6 asisten AI spesialis, jadwal proyek ini dinilai **Sangat Layak** dan aman untuk dicapai tanpa mengganggu kestabilan fisik Pemilik Usaha. Penetapan acuan rilis operasional paling mutlak dilaksanakan selambatnya pada Bulan Mei 2027.

---

## 8. Analisis Kelayakan Hukum dan Organisasional (Legal & Organizational Feasibility)

### 8.1. Kepatuhan Regulasi dan Perizinan Usaha
Catatan Legalitas: Penilaian ini didasarkan pada regulasi perizinan industri makro ritel domestik umum UMKM di Indonesia saat ini, dan memerlukan konsultasi perizinan komprehensif lebih lanjut terhadap sistem OSS daerah setempat bersama aparat yudikatif/pejabat pemerintahan setempat bilamana dibutuhkan penerapan yang mengikat secara spesifik-definitif.

Sebagai unit usaha mikro, AbuCom diwajibkan menjunjung kepatuhan normatif atas kewajiban pendaftaran badan legal administrasi negara untuk mengesahkan dan melindungi segala tindak transaksional korporasi, termasuk kewajiban mutlak pelaporan Nomor Induk Berusaha (NIB). NIB yang bernaung dalam sistem terpadu pemerintah bertajuk Online Single Submission (OSS) ini sangat krusial bagi jaminan operasi kelancaran rekrutmen pekerja dan membebaskan Pemilik Usaha dari jeratan hukuman pemberhentian paksa.
*   **Penilaian**: **Layak**.

### 8.2. Kepatuhan Perlindungan Data Pribadi (UU PDP No. 27 Tahun 2022)
Aplikasi AbuCom menyimpan data sensitif pelanggan (Nama, Nomor WhatsApp, Riwayat Transaksi) dalam modul CRM, data riwayat kasbon karyawan, serta data keuangan pinjaman bank pemilik. Sesuai ketentuan **UU PDP No. 27 Tahun 2022** di Indonesia, pemilik bertindak sebagai pengendali data pribadi pelanggan dan wajib memastikan keamanannya dari kebocoran yang berpotensi memicu sanksi denda hukum administrasi maupun pidana.
*   **Evaluasi Kelayakan**: Sistem telah merancang fitur pengamanan standar industri yang memadai untuk mematuhi UU PDP:
    *   Enkripsi satu arah *bcrypt* untuk kata sandi akun karyawan.
    *   *JSON Web Token* (JWT) untuk mengamankan *session* data CLI.
    *   Sistem pembatasan menu (RBAC) yang sangat ketat: Karyawan tidak diizinkan mengekspor atau melihat menu keuangan sensitif pemilik.
    *   *Audit Trail* mencatat setiap aktivitas penghapusan atau perubahan data sensitif.
*   **Penilaian**: **Layak dengan Catatan** (Catatan: Server basis data MySQL lokal harus dilindungi kata sandi *root* yang sangat kuat dan direktori backup database wajib dienkripsi).

### 8.3. Lisensi Perangkat Lunak
Seluruh komponen perangkat lunak yang dipilih aman dari tuntutan pelanggaran hak cipta:
*   Bahasa Python berlisensi PSF (Python Software Foundation License) — 100% bebas biaya dan aman untuk komersial.
*   Database MySQL Community Edition berlisensi GPL (General Public License) — 100% bebas biaya untuk penggunaan internal bisnis.
*   Pustaka Python (`bcrypt`, `pyjwt`, `mysql-connector-python`) berlisensi *open-source* MIT/Apache/GPL yang aman.
*   **Penilaian**: **Layak** (Bebas biaya lisensi tahunan, mengeliminasi risiko pembajakan software).

### 8.4. Aspek Ketenagakerjaan
Catatan Legalitas: Penilaian normatif kesejahteraan pegawai pada sub-bab perundingan di bawah ini adalah analisa logikal atas penerapan kewajiban-kewajiban mendasar aturan Ketenagakerjaan Nasional Republik Indonesia secara umum, yang pada penerapannya tetap harus disesuaikan secara proporsional berlandaskan kesepakatan tertulis mutlak antara pemberi kerja dengan individu staf sesuai batas kemampuan aset toko ritel berstandar UMKM.

Rencana rekrutmen 7 staf baru wajib mematuhi regulasi ketenagakerjaan dasar di Indonesia yang diatur dalam undang-undang ketenagakerjaan (termasuk UU Cipta Kerja).
*   **Tantangan**: Pemilik harus menetapkan skema kontrak kerja yang jelas, baik Perjanjian Kerja Waktu Tertentu (**PKWT** untuk staf kasir/gudang kontrak) maupun Perjanjian Kerja Waktu Tidak Tertentu (**PKWTT** untuk posisi tetap Kepala Percetakan). Pemilik juga harus menghitung standar upah bulanan wajar yang disesuaikan dengan regulasi upah setempat:

    *(Sebagai acuan awal untuk wilayah kabupaten/kota non-metropolitan di Indonesia, Upah Minimum Regional (UMR) atau UMK tahun 2025 berkisar antara **Rp 2.000.000 hingga Rp 4.500.000 per bulan**, tergantung ketetapan peraturan daerah bersangkutan. Pemilik usaha wajib memvalidasi nilai angka mutlak UMR secara resmi melalui peninjauan langsung ke portal resmi milik Kementerian Ketenagakerjaan Republik Indonesia di `kemnaker.go.id` atau menghubungi dinas tenaga kerja setempat guna penyelarasan parameter).*

*   **Dukungan Sistem**: Modul SDM dan penggajian cerdas AbuCom memfasilitasi administrasi yang transparan bagi pemenuhan hak karyawan (perhitungan absensi harian, pemotongan otomatis sisa kasbon, dan akumulasi bonus poin insentif beban kerja).
*   **Penilaian**: **Layak dengan Catatan** (Catatan: Pemilik wajib berkonsultasi mengenai standar kontrak kerja dasar untuk menghindari konflik ketenagakerjaan hukum di masa depan).

### 8.5. Struktur Organisasi dan Kesiapan Tata Kelola
Struktur organisasi 7 posisi operasional didukung budaya kerjasama lintas divisi (*cross-functional*) yang fleksibel. Budaya ini sangat baik untuk menambal kekosongan saat divisi lain sibuk.
*   **Kerentanan**: Budaya *cross-functional* tanpa kejelasan wewenang dapat memicu kekacauan pertanggungjawaban kas kasir jika ada karyawan non-kasir yang ikut melakukan transaksi pembayaran di aplikasi.
*   **Solusi**: Aplikasi CLI harus menerapkan kewajiban *login session* dengan ID unik karyawan untuk setiap kali transaksi diinput ke dalam terminal kasir, guna memastikan integritas log aktivitas (*Audit Trail*).
*   **Penilaian**: **Layak**.

### 8.6. Risiko Hukum/Organisasional dan Mitigasi

| No | Risiko Hukum/Organisasional | Probabilitas | Dampak | Rencana Mitigasi |
|----|-----------------------------|:------------:|:------:|------------------|
| 1  | **Pelanggaran UU PDP Akibat Flashdisk Karyawan**: Karyawan menyalin *file* database cadangan (.sql/.zip) yang berisi data pelanggan secara ilegal. | 2 | 5 | Kunci akses direktori *backup* database lokal di sistem operasi Linux Debian 12 hanya untuk user *root*, serta lakukan enkripsi pada file zip cadangan database menggunakan algoritma AES-256. |
| 2  | **Konflik Selisih Kas akibat Budaya Cross-Functional**: Beberapa staf bergantian menggunakan PC Kasir yang sama sehingga terjadi selisih kas fisik di laci kasir. | 4 | 4 | Terapkan menu rekonsiliasi kas (*Cash Reconciliation*) wajib di akhir setiap *shift*/hari kerja, di mana staf kasir aktif harus memasukkan jumlah uang fisik sebelum dapat melakukan penutupan sistem. |
| 3  | **Risiko Ketidakpastian Skema Kontrak Kerja (PKWT/PKWTT)**: Adanya tuntutan kompensasi kerugian finansial atau sanggahan ketenagakerjaan akibat tidak disahkannya draf kontrak tertulis yang spesifik saat masa awal masuk masa orientasi pelatihan calon staf kerja/pramuniaga baru. | 2 | 4 | Melakukan sesi penyusunan dokumen nota pakta integritas dan penerbitan draf rancangan surat keputusan *standar operating procedures* (SOP) tentang PKWT harian/bulanan di pekan awal periode penugasan rekrutmen. |

### 8.7. Kesimpulan Kelayakan Hukum & Organisasional
$$\color{orange}{\textbf{LAYAK DENGAN CATATAN (FEASIBLE WITH CONDITIONS)}}$$

Proyek ini sepenuhnya aman dari sisi lisensi *software open-source* dan regulasi bisnis perizinan. Catatan kelayakan kritis terletak pada **disiplin kepatuhan UU PDP** terkait keamanan database pelanggan dari penyalinan ilegal, **kejelasan otorisasi sistem kasir** untuk mendukung budaya kerjasama tim tanpa memicu selisih pencatatan kas fisik, serta implementasi standar dokumentasi perjanjian kerja profesional dengan calon tim pendukung 7 pegawai baru.

---

## 9. Analisis Alternatif Solusi

Untuk memvalidasi kelayakan solusi yang diusulkan, dilakukan analisis perbandingan objektif terhadap 3 alternatif keputusan bisnis:

### 9.1. Alternatif 1: Tetap Menggunakan Excel (Status Quo / Do Nothing)
*   **Deskripsi**: Mempertahankan operasional harian yang berjalan saat ini dengan mengandalkan rekap manual lembar kerja Microsoft Excel yang berserakan.
*   **Kelebihan**: Bebas investasi finansial awal (CAPEX Rp 0) dan tidak memerlukan waktu pelatihan staf baru.
*   **Kekurangan**: Data inventaris dan keuangan tetap terfragmentasi, limbah produksi tidak terukur, rawan kesalahan ketik manual (*human error*), tidak memiliki hak akses pengaman data sensitif, tidak *scalable*, dan Pemilik Usaha dipastikan akan mengalami tingkat *burnout* kronis yang mengancam kesehatan.

### 9.2. Alternatif 2: Menggunakan Aplikasi Siap Pakai (Off-the-Shelf Software)
*   **Deskripsi**: Menggunakan platform *Software-as-a-Service* (SaaS) ritel/POS berbayar populer di Indonesia seperti Accurate Online, Jurnal.id, Moka POS, atau Pawoon.
*   **Kelebihan**: Cepat diimplementasikan, memiliki antarmuka grafis (GUI) yang sangat ramah pengguna, didukung tim *support* vendor, serta teruji secara industri ritel.
*   **Kekurangan**:
    1.  **Biaya Berkelanjutan (OPEX) Sangat Tinggi**: Memerlukan biaya langganan bulanan per lisensi *user*/cabang yang membengkak dalam jangka panjang (UMKM *recurring cost*).
    2.  **Ketidakcocokan Fitur Kritis**: Tidak ada *software* ritel siap pakai yang mendukung formula HPP kustom berbasis Bill of Materials (BOM) multi-bahan yang berpresisi desimal untuk percetakan kustom.
    3.  **Tidak Mendukung Penggajian Cerdas & Poin Kustom**: Logika gaji fleksibel berbasis laba dan insentif beban kerja harian AbuCom tidak dapat diakomodasi di sistem POS standard.
    4.  **Keterbatasan Kontrol Data**: Data keuangan sensitif dan pinjaman modal pemilik harus disimpan di server pihak ketiga (*cloud* vendor), melanggar privasi penuh yang diharapkan pemilik.

### 9.3. Alternatif 3: Membangun Aplikasi Kustom CLI (Solusi yang Diusulkan)
*   **Deskripsi**: Membangun aplikasi internal terpadu kustom berbasis CLI menggunakan bahasa pemrograman Python 3.14.2+ dengan database relasional MySQL lokal.
*   **Kelebihan**:
    1.  **100% Sesuai Kebutuhan Bisnis**: Seluruh logika unik (HPP BOM dimensi desimal, penggajian otomatis, sistem poin, status antrian, dan pengelolaan pinjaman modal) diakomodasi secara presisi.
    2.  **Biaya Investasi Sekali Bayar (CAPEX)**: Infrastruktur hardware mini PC server dan jaringan menjadi aset fisik milik toko, tanpa biaya langganan bulanan *software*.
    3.  **Kontrol Keamanan Mutlak**: File database disimpan di server lokal fisik di toko, sepenuhnya aman dari akses pihak ketiga luar.
    4.  **Kesiapan Skalabilitas Ekspansi**: Database dirancang siap menampung ID cabang sejak awal (*Multi-Branch Ready*).
*   **Kekurangan**: Membutuhkan waktu pengembangan selama 12 bulan, risiko kegagalan teknis *coding* FP, serta menuntut waktu adaptasi staf terhadap visual teks CLI.

### 9.4. Matriks Perbandingan Alternatif

Evaluasi matriks menggunakan skala skor **1 (Sangat Buruk)** s.d. **5 (Sangat Baik)** berdasarkan 8 kriteria evaluasi bisnis:

| No | Kriteria Evaluasi Bisnis | Alternatif 1 (Excel) | Alternatif 2 (SaaS Off-the-Shelf) | Alternatif 3 (Kustom CLI Python) |
|----|--------------------------|:--------------------:|:---------------------------------:|:--------------------------------:|
| 1  | Biaya Awal (CAPEX)       | 5                    | 4                                 | 2                                |
| 2  | Biaya Berkelanjutan      | 5                    | 1 (Recurring mahal)               | 4 (Sangat murah)                 |
| 3  | Kesesuaian Fitur Unik    | 2                    | 1 (BOM & Gaji ditolak)            | 5 (100% presisi)                 |
| 4  | Fleksibilitas Kustomisasi| 3                    | 1 (Kaku/Vendor lock-in)           | 5 (Sangat fleksibel)             |
| 5  | Waktu Penerapan          | 5 (Instan)           | 4 (Sangat Cepat)                  | 2 (12 Bulan)                     |
| 6  | Kemudahan Penggunaan     | 3                    | 5 (GUI Ramah)                     | 3 (CLI Teks)                     |
| 7  | Skalabilitas Multi-Cabang| 1                    | 4                                 | 5 (Desain database handal)       |
| 8  | Kontrol Data & Privasi   | 4                    | 1 (Server luar cloud)             | 5 (Server fisik lokal)           |
|    | **Total Skor**           | **28**               | **21**                            | **31**                           |

### 9.5. Justifikasi Pemilihan Alternatif Terbaik
Berdasarkan hasil analisis matriks perbandingan, **Alternatif 3 (Aplikasi Kustom CLI Python)** memperoleh total skor tertinggi (**31 poin**) dibandingkan Excel (28 poin) dan SaaS POS (21 poin). 

Meskipun Alternatif 3 menuntut investasi finansial awal (Rp 40 juta) dan waktu tunggu pengembangan selama 12 bulan, alternatif ini merupakan **satu-satunya solusi** yang mampu mengakomodasi kebutuhan kritis fungsional AbuCom yang sangat spesifik, yaitu formula perhitungan HPP BOM dimensi desimal dan manajemen penggajian cerdas berbasis insentif poin. Alternatif 2 ditolak secara mutlak karena keterbatasan fitur standard ritel mereka yang tidak dapat dikustomisasi, sementara Alternatif 1 harus segera ditinggalkan untuk mencegah kehancuran kesehatan mental pemilik akibat *burnout* operasional harian.

---

## 10. Matriks Ringkasan Kelayakan

Berikut adalah rangkuman evaluasi kelayakan komprehensif AbuCom berdasarkan hasil analisis kelima dimensi kelayakan:

| No | Dimensi Kelayakan | Status Kelayakan | Catatan Kunci & Syarat Kelayakan |
|----|-------------------|:----------------:|-----------------------------------|
| 1  | **Kelayakan Teknis** | $$\color{orange}{\textbf{Layak dg Catatan}}$$ | Pustaka & runtime Python/MySQL sangat stabil. Diperlukan kedisiplinan integrasi asisten AI untuk memitigasi kerumitan *state management* dalam *Functional Programming*. |
| 2  | **Kelayakan Operasional** | $$\color{orange}{\textbf{Layak dg Catatan}}$$ | Sistem amat mendesak dibutuhkan untuk menanggulangi ancaman *burnout* Pemilik Usaha. Seluruh program seleksi staf baru operasional mesti dituntaskan sukses saat pengujung pekan jelang waktu Go-Live rilis aplikasi. |
| 3  | **Kelayakan Ekonomi** | $$\color{orange}{\textbf{Layak dg Catatan}}$$ | Potensi pengembalian modal investasi sangat cepat (~9,5 bulan), ROI tinggi (26%), dan NPV positif (Rp 47.471.075). Kas pengembangan proyek wajib dilindungi dari penarikan mendadak modal pinjaman tanpa bunga. |
| 4  | **Kelayakan Jadwal** | $$\color{green}{\textbf{Layak}}$$ | Alokasi waktu keseluruhan 12 bulan sangat longgar dan realistis untuk diselesaikan secara kolaboratif bersama 6 asisten AI spesialis. |
| 5  | **Kelayakan Hukum** | $$\color{orange}{\textbf{Layak dg Catatan}}$$ | 100% aman dari masalah biaya lisensi *software* komersial. Penerapan NIB pada OSS dan kontrak kerja PKWT/PKWTT staf harus diatur legalitasnya. Direktori *backup* database wajib dienkripsi kuat untuk mematuhi ketentuan UU PDP No. 27/2022. |

---

## 11. Rekomendasi Akhir dan Kesimpulan

### 11.1. Keputusan Kelayakan
Berdasarkan evaluasi komprehensif terhadap seluruh aspek teknis, operasional, finansial, jadwal, dan hukum, proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan** diputuskan **GO DENGAN CATATAN (GO WITH CONDITIONS)**. Keputusan bisnis ini diambil karena manfaat strategis otomatisasi sistem yang akan menyelamatkan kelangsungan usaha dari risiko kegagalan operasional (*burnout* pemilik tunggal) jauh lebih besar daripada sekadar mempermasalahkan tantangan kurva pengerjaan arsitektur pengkodean *backend*.

### 11.2. Prasyarat dan Catatan Penting Sebelum Melanjutkan
Sebelum proyek melangkah secara formal ke Fase SDLC berikutnya (Requirements & SRS), Pemilik Usaha wajib memenuhi prasyarat kritis berikut:
1.  **Penguncian Dana Contingency**: Pisahkan dana cadangan darurat sebesar **Rp 4.500.000** ke dalam rekening khusus terpisah untuk menjamin pengerjaan software tidak terganggu jika pinjaman tanpa bunga kerabat ditarik mendadak.
2.  **Pemetaan Dasar Upah Pokok**: Pemilik wajib menetapkan nominal upah bulanan minimum kandidat pelamar yang disesuaikan acuan ketetapan UU Ketenagakerjaan melalui eksplorasi referensi dari portal Disnaker *online* di `kemnaker.go.id` untuk persiapan pendataan variabel sistem *payroll*.
3.  **Draft Skenario Uji Awal (BOM)**: Menyusun draf manual rekapitulasi hitung dimensi material (ukuran presisi kertas stempel khusus sentimeter persegi) demi memvalidasi rasionalitas skrip *testing* rekursi HPP di waktu iterasi.

### 11.3. Langkah Selanjutnya (Next Steps)
Setelah dokumen Feasibility Study ini disetujui secara digital oleh Pemilik Usaha:
1.  Segera inisiasi Fase 2 (Requirements) untuk menyusun dokumen **SRS (Software Requirements Specification)** yang merinci 20+ detail kebutuhan fungsional secara formal. Benih modul fitur dalam spesifikasi SRS tersebut secara langsung diadopsi menduplikasi struktur kerangka 9 sub-sistem utama sebagaimana yang diuraikan mendetail pada sub-bab perincian deskripsi (Seksi 3.3 dokumen ini).
2.  Lakukan proses pembersihan data awal (*cleansing*) pada catatan Excel yang berserakan agar siap diimpor saat sistem selesai dideploy.
3.  Persiapkan skedul rekrutmen staf pramuniaga dan gudang selambat-lambatnya pada Bulan ke-9 pengembangan ekosistem logikal *backend*.

---

## 12. Glosarium

Berikut adalah glosarium istilah domain percetakan, retail, teknis, hukum, dan keuangan yang digunakan dalam analisis studi kelayakan ini untuk menyamakan pemahaman pembaca:
1.  **Stempel Flash**: Jenis stempel otomatis tanpa bantalan tinta eksternal, yang menggunakan karet khusus penyerap tinta warna yang disinari lampu kilat (flash) mesin stempel saat pembuatan.
2.  **Baliho**: Media promosi cetak luar ruangan (outdoor) berskala besar, biasanya dicetak di atas bahan flexi menggunakan mesin printer format lebar (*wide-format printer*).
3.  **Nama Dada**: Papan nama kecil (pin/tag name) yang biasanya dipasang di dada pakaian karyawan/pegawai, terbuat dari bahan akrilik, PVC, atau logam kuningan dengan lapisan resin bening.
4.  **Buku Yasin**: Buku berisi surat Yasin dan tahlil yang dicetak khusus secara kustom untuk acara peringatan kematian, biasanya dilengkapi sampul tebal (*hardcover*) hiasan emas.
5.  **Map Snelhechter**: Jenis map kertas atau plastik yang dilengkapi dengan pengikat jepitan logam di bagian tengahnya untuk menjepit dokumen kertas yang telah dilubangi.
6.  **PPOB (Payment Point Online Bank)**: Layanan loket pembayaran tagihan online yang bekerja sama dengan perbankan, seperti pembelian pulsa, paket data, token listrik PLN, pembayaran tagihan air, internet, dan TV kabel.
7.  **Jasa Transfer & Tarik Tunai Agen**: Layanan keuangan retail yang diselenggarakan oleh agen bank resmi (seperti Agen BRILink atau Agen Mandiri) untuk memfasilitasi transfer uang antar bank dan penarikan tunai secara instan menggunakan mesin EDC atau aplikasi mobile bank dengan komisi admin tertentu.
8.  **Bill of Materials (BOM)**: Daftar komprehensif bahan baku, komponen, dan kuantitas yang dibutuhkan untuk memproduksi satu unit produk akhir (dalam percetakan: daftar bahan stempel, tinta, kertas, pelapis untuk memproduksi satu stempel flash).
9.  **Stock Opname**: Proses penghitungan fisik persediaan barang/bahan baku di gudang secara langsung untuk kemudian dicocokkan dengan catatan stok yang ada pada sistem/aplikasi guna menemukan dan menyesuaikan selisih.
10. **Audit Trail**: Berkas catatan log historis yang merekam urutan aktivitas sistem secara kronologis, berguna sebagai bukti penelusuran tindakan keamanan jika terjadi perubahan data sensitif.
11. **Kasbon**: Skema pinjaman uang tunai di muka yang diberikan perusahaan/pemilik kepada karyawan, yang pengembaliannya dipotong langsung secara otomatis dari gaji bulanan karyawan bersangkutan.
12. **Uang Muka / DP (Down Payment)**: Pembayaran sebagian dari total harga transaksi yang diserahkan pelanggan di awal sebagai tanda jadi pesanan sebelum proses produksi dimulai.
13. **Retur**: Proses pengembalian barang yang telah dibeli oleh pelanggan atau barang yang dibeli dari supplier karena alasan cacat produksi, rusak, atau tidak sesuai spesifikasi pesanan.
14. **Functional Programming (FP)**: Paradigma pemrograman yang memperlakukan komputasi sebagai evaluasi fungsi matematika dan menghindari perubahan status (*state*) serta data yang dapat dimutasi (*mutable data*).
15. **CAPEX (Capital Expenditure)**: Investasi awal berupa biaya pengeluaran modal untuk pengadaan aset fisik infrastruktur (Mini PC Server, jaringan lokal, PC Kasir) di awal proyek.
16. **OPEX (Operational Expenditure)**: Biaya operasional rutin bulanan/tahunan pasca Go-Live yang dibutuhkan untuk memelihara kestabilan sistem aplikasi dan infrastruktur server.
17. **ROI (Return on Investment)**: Rasio persentase yang menunjukkan tingkat efisiensi atau profitabilitas dari pengembalian modal investasi yang ditanamkan pada proyek.
18. **Payback Period**: Jangka waktu yang dibutuhkan untuk memperoleh kembali seluruh modal investasi awal (CAPEX) berdasarkan akumulasi arus manfaat bersih tahunan.
19. **Cost-Benefit Analysis**: Metode analisis finansial sistematis yang membandingkan total estimasi biaya dengan total estimasi manfaat yang diperoleh guna menentukan kelayakan ekonomi.
20. **Analisis Sensitivitas**: Analisis simulasi keuangan proyeksi kelayakan ekonomi di bawah pengaruh fluktuasi parameter eksternal (Best Case, Base Case, Worst Case).
21. **Jalur Kritis (Critical Path)**: Rangkaian aktivitas proyek yang menentukan durasi tercepat penyelesaian keseluruhan proyek, di mana keterlambatan pada jalur ini akan otomatis menunda tanggal selesai proyek.
22. **UU PDP (Undang-Undang Pelindungan Data Pribadi)**: Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 yang mengatur mengenai hak subjek data pribadi, kewajiban pengelola data, dan sanksi hukum atas kebocoran data.
23. **NPV (Net Present Value)**: Selisih antara nilai sekarang dari aliran kas masuk (manfaat) dengan nilai sekarang dari aliran kas keluar (CAPEX) pada periode waktu tertentu dengan memperhitungkan faktor diskonto.
24. **BEP (Break-Even Point)**: Analisis titik impas untuk mengetahui tingkat volume transaksi atau masa operasional di mana total biaya investasi dan operasional sama dengan total pendapatan/manfaat.
25. **NIB (Nomor Induk Berusaha)**: Identitas pelaku usaha resmi di Indonesia yang diterbitkan oleh Lembaga OSS setelah pelaku usaha melakukan pendaftaran usahanya.
26. **OSS (Online Single Submission)**: Sistem perizinan berusaha terintegrasi secara elektronik yang dikelola oleh Kementerian Investasi/BKPM RI untuk memfasilitasi legalitas UMKM dan korporasi di Indonesia.
27. **PKWT (Perjanjian Kerja Waktu Tertentu)**: Perjanjian kerja antara pekerja/buruh dengan pengusaha untuk mengadakan hubungan kerja dalam waktu tertentu atau untuk pekerja yang bersifat tidak tetap/kontrak.
28. **PKWTT (Perjanjian Kerja Waktu Tidak Tertentu)**: Perjanjian kerja antara pekerja/buruh dengan pengusaha untuk mengadakan hubungan kerja yang bersifat tetap.
29. **Single-fighter**: Istilah informal yang merujuk pada situasi seorang Pemilik Usaha yang menjalankan dan memegang seluruh tanggung jawab manajemen dan operasional secara mandiri, tanpa dukungan karyawan/tim.
30. **Burnout**: Kondisi keletihan secara emosional, mental, maupun fisik yang teramat parah yang dialami oleh seseorang akibat tekanan stres beban pekerjaan (*workload*) kronis yang melampaui batas kewajaran penanganan individu.
31. **Zero-missed orders**: Tingkat sasaran kualitas pelayanan operasional bisnis yang menjamin tidak adanya satupun order transaksi pesanan yang dilupakan maupun yang gagal terverifikasi hingga tahap penyerahan/penjemputan barang produksi final.
32. **Multi-branch ready**: Desain kesiapan infrastruktur pangkalan data (*database*) aplikasi perangkat lunak semenjak mula fase arsitekturalnya untuk sanggup menampung integrasi rekap data dari banyak entitas gerai operasional (cabang) dengan hanya memberikan variabel unik (ID), membebaskan *programmer* dari keperluan mereparasi seluruh pondasi skema tabel inti saat melakukan ekspansi.
33. **Junior Programmer**: Tingkatan atau *role* kompetensi rekayasa *software* awal dari perancang pemrograman Python eksekutor lapangan yang bertanggung jawab menjadi inisiator *coding* di toko operasional AbuCom.

---

## 13. Referensi Dokumen

Berikut adalah daftar dokumen acuan primer dan sekunder yang secara langsung menopang integritas maupun sinkronisasi pengkajian landasan analitik dokumen Studi Kelayakan (*Feasibility Study*) v1.2 ini:

| # | Nama File                     | Lokasi / Path Relatif                              | Keterangan                                                                    |
|---|-------------------------------|----------------------------------------------------|-------------------------------------------------------------------------------|
| 1 | `01_project_charter.md`       | `docs/sdlc/01_planning/01_project_charter.md`      | Dokumen *Project Charter* v1.2 — referensi acuan primer validasi *budgeting* (CAPEX), *timeline* 12 bulan (8 *milestone*), struktur tim kolaborasi AI (7 staf, 6 asisten AI), parameter ROI & NPV, serta konfirmasi status 9 spesifikasi modul fungsional tingkat tinggi. |
| 2 | `narasi.txt`                  | `docs/sdlc/narasi.txt`                             | Dokumen log primer operasional kacamata Pemilik Usaha — referensi fondasi urgensi mitigasi keletihan esktrem (*burnout*), alur pelayanan *single-fighter*, ragam *multi-branch ready*, skema poin fungsional pengawasan *cross-functional*, serta tuntutan perlindungan rekap inventaris desimal retail ATK. |
| 3 | `03_stakeholder_register.md`  | `docs/sdlc/01_planning/03_stakeholder_register.md` | Analisis pengelompokan klasifikasi pemangku kepentingan untuk meninjau keterlibatan penyokong dana internal perbankan komersil maupun dukungan non-komersial keluarga, termasuk pemetaan staf kasir dan entitas peranan. |
| 4 | `04_tech_stack_decision.md`   | `docs/sdlc/01_planning/04_tech_stack_decision.md`  | Dokumen ketetapan rasionalitas pondasi arsitektural *Functional Programming* murni (*Pure FP*) dan pelarangan OOP, skema peranti otentikasi *JSON Web Token* (JWT), pengaman *hashing bcrypt*, serta infrastruktur rujukan terminal Debian + Klien Windows. |
| 5 | `05_innovation_proposal.md`   | `docs/sdlc/01_planning/05_innovation_proposal.md`  | Kerangka acuan pengingat sistematis atas pengembangan modul ekstra inovatif (*Best Practices*), peringatan keamanan anomali riwayat order (Fraud *detection*), *shift handover*, *price tracking*, serta perancangan laporan laba kotor *real-time*. |
