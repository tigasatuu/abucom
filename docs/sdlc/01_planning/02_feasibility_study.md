---
dokumen    : Feasibility Study (Studi Kelayakan Proyek)
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.1
tanggal    : 2026-05-21
status     : Validated
penyusun   : Senior Business Analyst & Feasibility Consultant
---

# Feasibility Study — AbuCom

## Riwayat Perubahan Dokumen

| Versi | Tanggal    | Perubahan        | Oleh                                          |
|-------|------------|------------------|-----------------------------------------------|
| 1.0   | 2026-05-21 | Pembuatan awal   | Senior Business Analyst & Feasibility Consultant |
| 1.1   | 2026-05-21 | Validasi, Analisis, dan Penyempurnaan Dokumen Feasibility Study berdasarkan issue #0004. Melengkapi data gap narasi & charter, memperbaiki parameter UMR, menambahkan break-even analysis & NPV, serta memperbarui riwayat perubahan. | Senior Business Analyst & Feasibility Consultant |

---

## 1. Informasi Dokumen
Dokumen ini disusun untuk menganalisis dan mengevaluasi tingkat kelayakan dari rencana pembangunan **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan** [ref: 01_project_charter.md, Seksi 1.1]. Analisis dilakukan secara komprehensif pada lima dimensi kelayakan standar industri untuk mendukung pengambilan keputusan strategis bisnis apakah proyek ini layak dilanjutkan (GO) atau tidak (NO-GO) ke fase SDLC berikutnya [ref: 0003_issue_feasibility_study.md, Seksi 3].

---

## 2. Ringkasan Eksekutif (Executive Summary)

### 2.1. Latar Belakang Singkat
Usaha UMKM AbuCom merupakan penyedia jasa percetakan, retail ATK, PPOB, jasa keuangan, dan jasa teknis yang saat ini dikelola dan dijalankan secara mandiri oleh pemilik usaha (*single-fighter*) [ref: narasi.txt, baris 1, 3-18]. Akibat kompleksitas pengelolaan lima divisi usaha tersebut yang dilakukan secara manual menggunakan berkas Microsoft Excel yang berserakan, pemilik mengalami stres berat, keletihan mental (*burnout*), serta risiko operasional yang tinggi seperti pesanan terlewat dan selisih persediaan barang baku yang signifikan [ref: narasi.txt, baris 28, 47, 70, 74]. Untuk mengatasi permasalahan tersebut, diusulkan pembangunan sistem aplikasi manajemen internal terpadu berbasis *Command Line Interface* (CLI) menggunakan Python dan MySQL [ref: 01_project_charter.md, Seksi 1.2].

### 2.2. Tujuan Studi Kelayakan
Studi kelayakan ini bertujuan untuk mengevaluasi secara objektif, kritis, dan berbasis data apakah proposal proyek aplikasi kustom CLI Python untuk AbuCom layak diimplementasikan dari aspek kelayakan teknis, operasional, ekonomi/finansial, jadwal, serta hukum dan organisasional [ref: 0003_issue_feasibility_study.md, Bagian 1].

### 2.3. Kesimpulan dan Rekomendasi Akhir
Berdasarkan hasil analisis mendalam terhadap kelima dimensi kelayakan, proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan** dinyatakan:

$$\color{orange}{\textbf{GO DENGAN CATATAN (GO WITH CONDITIONS)}}$$

Sistem ini sangat layak secara ekonomi dan jadwal, serta memiliki urgensi operasional yang sangat tinggi untuk mengatasi *burnout* pemilik. Namun, status kelayakan **Teknis**, **Operasional**, dan **Hukum** berada pada tingkat **"Layak dengan Catatan"** karena adanya risiko kritis terkait kerumitan paradigma *Functional Programming* murni [ref: 01_project_charter.md, Seksi 9.2 #2], proses rekrutmen staf baru [ref: 01_project_charter.md, Seksi 9.1 #1], serta kepatuhan perlindungan data pribadi pelanggan [ref: 01_project_charter.md, Seksi 8.2 N-2.1]. Proyek ini direkomendasikan untuk segera dilanjutkan ke Fase *Requirements* (SRS) setelah prasyarat mitigasi risiko dipenuhi oleh pemilik usaha [ref: 01_project_charter.md, Seksi 11 #2].

---

## 3. Deskripsi Proyek yang Dievaluasi

### 3.1. Nama dan Deskripsi Proyek
Proyek ini bernama **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan** [ref: 01_project_charter.md, Seksi 1.1]. Proyek ini mencakup perancangan dan pembangunan aplikasi manajemen internal terpadu berbasis teks (CLI) yang modular untuk mengotomatisasi seluruh kegiatan harian lima divisi usaha [ref: 01_project_charter.md, Seksi 1.2].

### 3.2. Tujuan Bisnis Proyek
Menghilangkan ketergantungan pada pencatatan manual Microsoft Excel yang tidak terintegrasi, mengotomatisasi pembukuan laba rugi instan per divisi, menerapkan manajemen persediaan berbasis komposisi bahan baku (*Bill of Materials*), mencegah pesanan pelanggan terlewat (*zero-missed orders*), serta mempersiapkan pondasi sistem operasi digital yang siap dikembangkan untuk ekspansi cabang baru (*multi-branch ready*) [ref: 01_project_charter.md, Seksi 3.1, 3.2].

### 3.3. Ruang Lingkup Proyek yang Dievaluasi
Ruang lingkup aplikasi yang dievaluasi mencakup 9 modul fungsional utama [ref: 01_project_charter.md, Seksi 4.1.1]:
*   **M.1. Modul Manajemen Transaksi & Kebijakan Harga**: Pembayaran DP & pelunasan, skema harga retail/grosir/mitra.
*   **M.2. Modul Manajemen Inventaris, BOM & Stock Opname**: HPP otomatis berbasis komposisi bahan, stok dimensi desimal presisi, manajemen limbah, dan rekonsiliasi persediaan.
*   **M.3. Modul Layanan Keuangan Digital, PPOB, Jasa Keuangan & Service**: Pembukuan pulsa/PPOB, transfer/tarik tunai, dan jasa service printer/PC.
*   **M.4. Modul Manajemen SDM, Penggajian & Poin Karyawan**: Absensi, kasbon, penggajian berbasis laba, dan poin insentif beban kerja.
*   **M.5. Modul Sistem Manajemen Antrian & Pelacakan Desain**: Transisi 5 status pekerjaan dan arsip lokasi berkas desain.
*   **M.6. Modul Administrasi Pinjaman, Aset, & Pengeluaran Rutin**: Pencatatan pinjaman bank, pinjaman tanpa bunga fleksibel, depresiasi aset, dan tabungan khusus alat.
*   **M.7. Modul Keamanan, Audit Trail & Hak Akses**: Pembatasan menu (RBAC) Pemilik vs Karyawan, log aktivitas, dan migrasi input awal manual.
*   **M.8. Modul Pembatalan, Retur & CRM**: Alur retur/pembatalan transaksi dan database kontak pelanggan.
*   **M.9. Skalabilitas Multi-Cabang**: Struktur tabel database MySQL dengan field ID cabang/unit usaha.

### 3.4. Stakeholder Utama
*   **Pemilik Usaha AbuCom**: Sponsor Utama, Manajer Proyek (Junior Programmer), dan Pengguna Utama [ref: 01_project_charter.md, Seksi 6.1].
*   **Calon Staf Karyawan (7 Posisi)**: Pengguna operasional harian sistem (Kepala Percetakan, Pramuniaga, Kasir, Desainer, Produksi Cetak, Fotocopy/Print, Staf Gudang) [ref: 01_project_charter.md, Seksi 7.2].
*   **Kreditur**: Bank Mandiri & Bank BRI (pinjaman berbunga) serta Sahabat/Kerabat/Keluarga (pinjaman tanpa bunga) [ref: 01_project_charter.md, Seksi 6.1].

### 3.5. Asumsi dan Batasan Studi Kelayakan
Untuk menjaga kredibilitas dan keandalan analisis evaluasi ini, ditetapkan beberapa asumsi dan batasan analisis:
*   **Asumsi Keuangan**: Nilai CAPEX Rp 40.000.000 terkunci dan tidak mengalami fluktuasi harga >10% sebelum pengadaan. Manfaat finansial tangible dihitung dengan asumsi stabilitas volume pesanan bulanan rata-rata seperti tahun operasional berjalan [ref: 01_project_charter.md, Seksi 12].
*   **Asumsi Organisasional**: Proses rekrutmen untuk 7 staf baru selesai tepat waktu sebelum go-live [ref: 01_project_charter.md, Seksi 9.1 #1].
*   **Batasan Teknis**: Evaluasi didasarkan pada antarmuka CLI yang dijalankan secara lokal client-server via LAN Cat6 di 1 cabang fisik, dengan pembatasan mutlak tidak menggunakan OOP pada logika bisnis inti program Python [ref: 01_project_charter.md, Seksi 9.2 #1, #2].

---

## 4. Analisis Kelayakan Teknis (Technical Feasibility)

### 4.1. Evaluasi Teknologi yang Dipilih

#### 4.1.1. Bahasa Pemrograman (Python 3.14.2+ & Functional Programming)
*   **Kelebihan**: Python memiliki ekosistem yang matang, pustaka standar yang melimpah, serta portabilitas tinggi di lintas OS [ref: 01_project_charter.md, Seksi 8.2 N-2.5]. Penggunaan paradigma *Functional Programming* (FP) murni (fungsi murni, imutabilitas, *higher-order functions*) meningkatkan keamanan, testabilitas, dan mengeliminasi efek samping (*side-effects*) dalam perhitungan HPP dan keuangan [ref: 01_project_charter.md, Seksi 8.2 N-2.4].
*   **Tantangan**: FP murni di Python memiliki *learning curve* yang sangat curam untuk programer tingkat junior karena Python secara bawaan merupakan bahasa multi-paradigma yang lebih condong ke OOP/imperatif. Manajemen *state* aplikasi (seperti sesi login pengguna atau transisi status transaksi) tanpa menggunakan *Class/Object* membutuhkan abstraksi tingkat tinggi (misalnya memanfaatkan *nested closures*, modul `functools`, atau struktur data imutabel khusus) [ref: 01_project_charter.md, Seksi 10 Risiko #4].
*   **Penilaian**: **Layak dengan Catatan** (Catatan: Diperlukan bimbingan intensif dari asisten AI spesialis *deep coding* seperti Claude Sonnet 4.6 untuk menyusun kerangka *state management* fungsional [ref: 01_project_charter.md, Seksi 7.1 Anggota 4]).

#### 4.1.2. Sistem Basis Data (MySQL)
*   **Kelebihan**: MySQL Community Server merupakan database relasional berskala industri yang stabil, gratis, berkinerja tinggi, dan mendukung kepatuhan ACID (Atomicity, Consistency, Isolation, Durability) yang sangat krusial untuk transaksi keuangan terintegrasi AbuCom [ref: 01_project_charter.md, Seksi 4.1.2, 12 #2].
*   **Penilaian**: **Layak** (Sangat sesuai untuk skala data UMKM dan siap mendukung arsitektur relasional multi-cabang [ref: 01_project_charter.md, Seksi 3.2 S.5]).

#### 4.1.3. Pustaka Pendukung
*   `mysql-connector-python` (driver DB standar), `python-dotenv` (keamanan kredensial), `bcrypt` (enkripsi satu arah sandi), dan `pyjwt` (autentikasi session CLI) [ref: 01_project_charter.md, Seksi 4.1.2]. Seluruh library ini bersifat open-source, stabil, dan memiliki dokumentasi melimpah [ref: 01_project_charter.md, Seksi 12 #2].
*   **Penilaian**: **Layak**.

#### 4.1.4. Platform & Sistem Operasi
*   Aplikasi CLI Python dan database MySQL dapat dijalankan lintas OS pada terminal Linux Debian 12 Bookworm (Server lokal) maupun Windows 11 (PC Kasir) tanpa ada modifikasi logika inti [ref: 01_project_charter.md, Seksi 8.2 N-2.5].
*   **Penilaian**: **Layak**.

#### 4.1.5. Antarmuka (CLI / Console)
*   **Kelebihan**: Aplikasi CLI sangat ringan, tidak membutuhkan kartu grafis, memiliki waktu respon yang instan (< 1 detik), bebas dari overhead rendering GUI, dan sangat cepat dioperasikan oleh kasir berpengalaman menggunakan pintasan keyboard (hotkeys) [ref: 01_project_charter.md, Seksi 8.2 N-2.6].
*   **Tantangan**: Aspek estetika visual sangat minim (hanya berbasis teks) dan membutuhkan waktu adaptasi lebih lama bagi staf baru yang terbiasa dengan antarmuka berbasis grafis (GUI) [ref: 01_project_charter.md, Seksi 10 Risiko #6].
*   **Penilaian**: **Layak dengan Catatan** (Catatan: Antarmuka teks harus dirancang dengan tata letak menu yang intuitif, kode warna ANSI untuk pembeda status, dan petunjuk input yang jelas [ref: narasi.txt, baris 86, 103]).

### 4.2. Evaluasi Kompleksitas Fitur Utama

#### 4.2.1. Modul Manajemen Transaksi & Kebijakan Harga (M.1)
*   **Detail & Kompleksitas**: Logika penanganan pembayaran bertahap (DP di awal, pelunasan di akhir) dikombinasikan dengan 3 skema harga yang berbeda (retail, grosir terhitung otomatis berbasis kuantitas, dan mitra khusus) [ref: 01_project_charter.md, Seksi 8.1 F-1.2, F-1.3]. Pemrosesan ini melibatkan kalkulasi multi-kondisi. Dalam FP murni, logika ini harus disusun menggunakan *pattern matching* atau percabangan fungsional murni tanpa mengubah status *state* order awal secara mutasi langsung.
*   **Penilaian**: **Layak**.

#### 4.2.2. Modul Manajemen Inventaris, BOM & Stock Opname (M.2)
*   **Detail & Kompleksitas**: Perhitungan HPP otomatis yang melibatkan multi-bahan (BOM) dengan satuan dimensi panjang x lebar (misal: pemakaian bahan stempel atau kertas baliho) serta volume desimal (tinta cairan) merupakan logika matematika berat [ref: narasi.txt, baris 95-96]. Dalam paradigma FP, perhitungan ini harus diselesaikan melalui fungsi murni (*pure functions*) rekursif atau operasi fungsional iteratif (`map`, `filter`, `reduce`). Evaluasi menunjukkan bahwa Python mendukung presisi desimal mengambang (*float* atau modul `decimal` bawaan) yang memadai untuk menghitung sisa bahan baku di gudang secara akurat [ref: 01_project_charter.md, Seksi 8.1 F-2.2]. Fitur sinkronisasi barang retail untuk produksi internal dan stock opname diakomodasi melalui relasi tabel.
*   **Penilaian**: **Layak**.

#### 4.2.3. Modul Layanan Keuangan Digital, PPOB, Jasa Keuangan & Service (M.3)
*   **Detail & Kompleksitas**: Mengingat tidak ada integrasi API pihak ketiga secara otomatis (sesuai batasan luar ruang lingkup) [ref: 01_project_charter.md, Seksi 4.2], kompleksitas modul ini berada pada tingkat rendah ke sedang. Sistem hanya mencatat mutasi manual dari tindakan fisik yang dilakukan pemilik/karyawan. Fitur penentu rekomendasi akun digital termurah dari 6 e-wallet (Mandiri, Dana, Gopay, LinkAja, ShopeePay, OVO) diselesaikan menggunakan pencarian data statis terindeks [ref: 01_project_charter.md, Seksi 8.1 F-3.2]. Peringatan deposit PPOB otomatis diatur pada limit Rp 150.000 [ref: 01_project_charter.md, Seksi 8.1 F-3.1].
*   **Penilaian**: **Layak**.

#### 4.2.4. Modul Manajemen SDM, Penggajian & Poin Karyawan (M.4)
*   **Detail & Kompleksitas**: Modul penggajian cerdas melibatkan kondisi target laba bersih usaha (gaji tetap vs persentase laba) digabung dengan akumulasi poin insentif beban kerja (1, 3, 5, atau 10 poin per aktivitas transaksi staf) [ref: 01_project_charter.md, Seksi 8.1 F-4.2, F-4.4]. Skema kasbon terpotong otomatis juga diintegrasikan [ref: 01_project_charter.md, Seksi 8.1 F-4.3]. Struktur logika kondisional ini sepenuhnya berada dalam batas kapabilitas pemrograman Python dengan integrasi *foreign key* MySQL yang dijamin kepatuhan ACID.
*   **Penilaian**: **Layak**.

#### 4.2.5. Modul Sistem Manajemen Antrian & Pelacakan Desain (M.5)
*   **Detail & Kompleksitas**: Sistem antrian harus memantau transisi 5 status pekerjaan secara sekuensial (`Antri` -> `Proses Desain` -> `Produksi` -> `Selesai` -> `Diambil`) [ref: 01_project_charter.md, Seksi 8.1 F-5.1]. Karena status berubah secara dinamis, FP murni menuntut pemrosesan perubahan data melalui pengembalian record baru yang memuat status terupdate (imutabilitas record database). Fitur arsip lokasi berkas desain diselesaikan melalui penyimpanan path direktori lokal.
*   **Penilaian**: **Layak**.

#### 4.2.6. Modul Administrasi Pinjaman, Aset, & Pengeluaran Rutin (M.6)
*   **Detail & Kompleksitas**: Pencatatan pinjaman modal tanpa bunga yang sangat fleksibel (penarikan, pengembalian, sisa saldo) dan pelacakan pinjaman bank (BRI/Mandiri) yang meliputi tenor, bunga, dan notifikasi jatuh tempo bulanan [ref: 01_project_charter.md, Seksi 8.1 F-6.1, F-6.2]. Ditambah perhitungan depresiasi aset tetap dan tabungan alat. Logika ini bersifat komputasi linier standar dan mudah diimplementasikan pada database relasional.
*   **Penilaian**: **Layak**.

#### 4.2.7. Modul Keamanan, Audit Trail & Hak Akses (M.7)
*   **Detail & Kompleksitas**: Mekanisme pengamanan hak akses menu Pemilik vs Karyawan di tingkat aplikasi CLI (RBAC) [ref: 01_project_charter.md, Seksi 8.2 N-2.1], enkripsi kata sandi menggunakan pustaka `bcrypt` [ref: 01_project_charter.md, Seksi 8.2 N-2.3], dan pencatatan log *Audit Trail* ke tabel terpisah MySQL [ref: 01_project_charter.md, Seksi 8.2 N-2.2] sepenuhnya siap diimplementasikan secara standar industri keamanan perangkat lunak.
*   **Penilaian**: **Layak**.

#### 4.2.8. Modul Pembatalan, Retur & CRM (M.8)
*   **Detail & Kompleksitas**: Alur pembatalan transaksi dengan pengembalian DP atau retur barang retail rusak [ref: 01_project_charter.md, Seksi 8.1 F-1.4]. Kompleksitas modul ini terletak pada konsistensi sinkronisasi kas dan stok secara bersamaan saat retur/batal terjadi. Keandalan database MySQL (*transactional COMMIT/ROLLBACK*) menjamin integritas data dalam modul ini. Pencatatan CRM pelanggan menyimpan kontak WA dan log riwayat pesanan [ref: 01_project_charter.md, Seksi 8.1 F-5.3].
*   **Penilaian**: **Layak**.

#### 4.2.9. Modul Skalabilitas Multi-Cabang (M.9)
*   **Detail & Kompleksitas**: Kompleksitas arsitektur basis data multi-cabang dicapai secara elegan dengan menambahkan kolom `cabang_id` di setiap tabel utama (transaksi, stok, keuangan, SDM) [ref: 01_project_charter.md, Seksi 4.1.1 M.9]. Hal ini sangat mudah diimplementasikan di MySQL tanpa menambah beban komputasi secara signifikan pada fase satu cabang saat ini [ref: 01_project_charter.md, Seksi 9.2 #5].
*   **Penilaian**: **Layak**.

### 4.3. Evaluasi Kapabilitas Tim Pengembang
Kolaborasi tim pengembang tergolong unik dan berpotensi sangat efektif: 1 Junior Programmer (Pemilik Usaha yang bertindak sebagai PM & integrator) dibantu oleh 6 model AI spesialis dengan tugas terstruktur (Gemini 3.1 Pro untuk logika arsitektur berat, Claude Sonnet 4.6 untuk penulisan kode fungsional mendalam, dan Claude Opus untuk keamanan/strategi) [ref: 01_project_charter.md, Seksi 7.1].
*   **Risiko**: Risiko terbesar adalah ketidakcocokan kode program saat Junior Programmer melakukan penggabungan (integrasi) modul-modul FP dari AI yang berbeda [ref: 01_project_charter.md, Seksi 7.1 Anggota 0].
*   **Penilaian**: **Layak dengan Catatan** (Catatan: Junior Programmer harus disiplin melakukan review sintaksis cepat menggunakan Gemini 3 Flash serta mematuhi standardisasi struktur kode di bawah arahan Lead Architect AI [ref: 01_project_charter.md, Seksi 7.1 Anggota 1, Anggota 3]).

### 4.4. Evaluasi Infrastruktur Teknis yang Dibutuhkan
Kebutuhan fisik infrastruktur untuk mendukung topologi Client-Server lokal di toko percetakan sangat minimal [ref: 01_project_charter.md, Seksi 12]:
1.  **Server Lokal**: 1 Unit Mini PC (Core i5, 16GB RAM, SSD 512GB) yang berfungsi sebagai host server database MySQL lokal.
2.  **Klien CLI**: PC Kasir/Operasional yang terhubung via jaringan kabel LAN (UTP Cat6) ke server lokal.
3.  **Daya Cadangan**: 2 Unit UPS untuk melindungi Mini PC Server dan PC Kasir dari kerusakan data database akibat pemadaman listrik tiba-tiba [ref: 01_project_charter.md, Seksi 9.3 #2].
*   **Penilaian**: **Layak** (Infrastruktur ini sangat standar, murah, dan kokoh untuk kebutuhan operasional UMKM).

### 4.5. Risiko Teknis dan Mitigasi

| No | Risiko Teknis | Probabilitas | Dampak | Rencana Mitigasi |
|----|---------------|:------------:|:------:|------------------|
| 1  | **Kebocoran Memori atau Rekursi Tak Terbatas**: Kesalahan logika FP murni (rekursi tak terbatas) di Python yang dapat menyebabkan memori server penuh (*stack overflow*). | 2 | 4 | Batasi kedalaman rekursi di Python, prioritaskan penggunaan iterasi fungsional (`map/filter` atau generator *lazy-evaluation*) yang lebih aman bagi alokasi memori [ref: 01_project_charter.md, Seksi 10 Risiko #4]. |
| 2  | **Korup Data Database Akibat Mati Listrik**: Listrik mati mendadak saat transaksi database MySQL sedang berlangsung. | 3 | 4 | Terapkan transaksi database dengan skema `COMMIT` & `ROLLBACK` yang ketat di MySQL, serta gunakan UPS penstabil daya cadangan untuk Mini PC Server [ref: 01_project_charter.md, Seksi 12 #1]. |
| 3  | **Kesalahan Pembulatan Desimal**: Nilai desimal persediaan bahan baku (panjang/lebar/cairan) tidak sinkron akibat pembulatan *floating point* standar Python. | 3 | 3 | Gunakan modul bawaan `decimal` di Python dengan pengaturan presisi tetap (misal: 4 angka di belakang koma) untuk menjamin akurasi perhitungan matematika inventaris [ref: narasi.txt, baris 96]. |

### 4.6. Kesimpulan Kelayakan Teknis
$$\color{orange}{\textbf{LAYAK DENGAN CATATAN (FEASIBLE WITH CONDITIONS)}}$$

Teknologi yang dipilih (Python CLI + MySQL) sangat matang dan andal untuk mengotomatisasi sistem operasional AbuCom. Catatan utama terletak pada disiplin penerapan paradigma *Functional Programming* murni untuk menghindari efek samping pengolahan data serta penanganan visual antarmuka CLI agar tetap ramah digunakan oleh staf operasional [ref: 01_project_charter.md, Seksi 8.2 N-2.4, 9.2 #2].

---

## 5. Analisis Kelayakan Operasional (Operational Feasibility)

### 5.1. Kesiapan Organisasi dan SDM

#### 5.1.1. Kondisi Operasional Saat Ini (Single-Fighter)
Kondisi saat ini sangat tidak berkelanjutan. Pemilik bertindak sebagai *single point of failure* yang melakukan segalanya secara manual, mulai dari mendesain, mencetak, melayani kasir, hingga memantau stok bahan [ref: narasi.txt, baris 28, 49-70]. Adopsi sistem baru akan memberikan dampak positif yang sangat signifikan bagi pemulihan kesehatan mental pemilik usaha dengan memangkas beban administratif harian [ref: 01_project_charter.md, Seksi 3.3 #4].

#### 5.1.2. Rencana Rekrutmen 7 Posisi Staf
Pemilik telah memiliki rencana pembagian divisi kerja yang solid untuk 7 posisi operasional (Kepala Percetakan, Pramuniaga, Kasir, Desainer, Produksi Cetak, Fotocopy/Print, Staf Gudang) [ref: 01_project_charter.md, Seksi 7.2]. Rencana ini sangat realistis untuk mendukung efisiensi operasional. Namun, kesuksesan operasional sistem bergantung penuh pada keberhasilan rekrutmen staf ini sebelum sistem diterapkan (*Go-Live*) [ref: 01_project_charter.md, Seksi 9.1 #1].

#### 5.1.3. Kesiapan Literasi Digital Pengguna
*   **Pemilik**: Memiliki latar belakang cukup (bertindak sebagai Junior Programmer), sehingga memiliki kesiapan digital yang sangat baik untuk mengelola server basis data [ref: 01_project_charter.md, Seksi 7.1 Anggota 0].
*   **Karyawan Staf Baru**: Latar belakang calon karyawan kemungkinan sangat bervariasi. Penggunaan sistem berbasis teks (CLI) yang tidak memiliki visual tombol grafis berpotensi memicu kesulitan adaptasi awal dan kebingungan input perintah teks [ref: 01_project_charter.md, Seksi 10 Risiko #6].

### 5.2. Dampak Perubahan Proses Bisnis (dari Manual Excel ke CLI)
Transisi dari file Excel manual yang terpisah-pisah [ref: narasi.txt, baris 47] menuju sistem CLI database terpadu akan merevolusi alur kerja:
*   Transaksi kas langsung terhubung dengan pemotongan stok bahan baku secara real-time via skema BOM [ref: narasi.txt, baris 95].
*   Pencatatan limbah produksi (*waste management*) terdokumentasi terpisah untuk rekonsiliasi stok [ref: narasi.txt, baris 87].
*   Dampak awal: Staf operasional akan menghadapi beban kerja tambahan untuk menginput data awal persediaan secara manual dari data Excel lama yang tidak terstruktur [ref: narasi.txt, baris 70]. Namun, setelah fase input selesai, beban operasional harian akan terpangkas hingga **90%** [ref: 01_project_charter.md, Seksi 3.3 #4].

### 5.3. Penerimaan Pengguna (User Acceptance)
Tingkat penerimaan dari pemilik usaha diproyeksikan mencapai **100% (Sangat Tinggi)** karena sistem ini diinisiasi langsung oleh pemilik untuk mengatasi masalah pribadinya (*burnout*) [ref: narasi.txt, baris 28, 74]. Untuk karyawan baru, potensi resistensi dapat dieliminasi melalui struktur menu CLI yang konsisten dan dukungan dokumentasi instruksi yang ringkas [ref: 01_project_charter.md, Seksi 10 Risiko #6].

### 5.4. Kebutuhan Pelatihan dan Manajemen Perubahan
Telah direncanakan program pelatihan sistem selama **3 hari** berupa simulasi operasional penuh (dari melayani pelanggan, input DP, proses antrian, produksi, pencatatan limbah, hingga pelunasan di kasir dan stock opname) [ref: 01_project_charter.md, Seksi 9.4 #3, 10 Risiko #6]. Durasi 3 hari dinilai cukup memadai jika didukung oleh skenario simulasi yang matang dan tersedianya berkas *CLI User Manual* yang mudah dipahami [ref: 01_project_charter.md, Seksi 5.2 #6].

### 5.5. Dukungan Operasional Pasca Go-Live
Junior Programmer (Pemilik) akan memegang peran utama sebagai administrator teknis lokal di toko [ref: 01_project_charter.md, Seksi 6.2]. Tim asisten AI akan selalu siaga mendukung penyelesaian masalah bug perangkat lunak secara asinkron [ref: 01_project_charter.md, Seksi 7.1].
*   **Penilaian**: **Layak**.

### 5.6. Risiko Operasional dan Mitigasi

| No | Risiko Operasional | Probabilitas | Dampak | Rencana Mitigasi |
|----|--------------------|:------------:|:------:|------------------|
| 1  | **Keterlambatan Rekrutmen Karyawan Baru**: Karyawan belum lengkap saat sistem siap go-live, sehingga pemilik terpaksa mengoperasikan CLI sendirian dan tetap mengalami burnout. | 3 | 5 | Lakukan proses rekrutmen staf secara paralel pada Bulan 9-10 saat aplikasi memasuki Fase Implementasi Akhir [ref: 01_project_charter.md, Seksi 11 #5]. |
| 2  | **Human Error Input Perintah CLI**: Karyawan salah menginput kode produk atau perintah teks yang dapat mengacaukan antrian atau transaksi. | 4 | 3 | Implementasikan fitur konfirmasi input (misal: "Apakah data transaksi sudah benar? [Y/N]") dan fungsi pembatalan bertahap (*soft-rollback*) di aplikasi [ref: 01_project_charter.md, Seksi 8.1 F-1.4]. |
| 3  | **Resistensi Budaya Kerjasama Tim**: Karyawan enggan membantu divisi lain (*cross-functional*) karena merasa di luar deskripsi kerja mereka. | 3 | 3 | Gunakan sistem Poin Insentif Karyawan yang adil untuk menghargai setiap bantuan kerja lintas divisi secara transparan [ref: 01_project_charter.md, Seksi 8.1 F-4.4; ref: narasi.txt, baris 43]. |

### 5.7. Kesimpulan Kelayakan Operasional
$$\color{orange}{\textbf{LAYAK DENGAN CATATAN (FEASIBLE WITH CONDITIONS)}}$$

Sistem ini sangat mendesak dan layak untuk membebaskan pemilik dari masalah *burnout* operasional harian. Catatan penting keberhasilan operasional terletak pada **disiplin rekrutmen staf tepat waktu** dan **efektivitas pelatihan simulasi 3 hari** untuk memastikan seluruh staf baru mampu mengoperasikan terminal CLI tanpa kebingungan teknis [ref: 01_project_charter.md, Seksi 10 Risiko #1, #6].

---

## 6. Analisis Kelayakan Ekonomi / Finansial (Economic Feasibility)

### 6.1. Estimasi Biaya Pengembangan (Capital Expenditure - CAPEX)
Berdasarkan data anggaran terstruktur, total investasi awal pengembangan sistem adalah **Rp 40.000.000** [ref: 01_project_charter.md, Seksi 12]. Biaya ini dialokasikan ke 5 komponen berikut:
1.  **Perangkat Keras (Hardware)** (Mini PC Server, PC Kasir, 2 UPS): Rp 15.500.000 [ref: 01_project_charter.md, Seksi 12 #1].
2.  **Infrastruktur Jaringan** (Router, Switch UTP Cat6, Jasa): Rp 2.500.000 [ref: 01_project_charter.md, Seksi 12 #2].
3.  **Biaya Pengembangan Software** (Token API AI & Junior PM): Rp 15.000.000 [ref: 01_project_charter.md, Seksi 12 #3].
4.  **Pelatihan & Operasional Awal** (Cetak manual, konsumsi): Rp 2.500.000 [ref: 01_project_charter.md, Seksi 12 #4].
5.  **Dana Cadangan Darurat (Contingency)**: Rp 4.500.000 [ref: 01_project_charter.md, Seksi 12 #5].
*   **Evaluasi**: Anggaran Rp 40 juta sangat efisien dan realistis untuk ukuran UMKM karena meniadakan biaya lisensi OS/Database berbayar [ref: 01_project_charter.md, Seksi 12 #2].

### 6.2. Estimasi Biaya Operasional Berkelanjutan (Operational Expenditure - OPEX)
`*[ESTIMASI — belum dikonfirmasi pemilik]*`
Biaya operasional bulanan pasca go-live diestimasi mencakup pengeluaran berikut:
*   Listrik Tambahan Server & PC: Rp 150.000 / bulan.
*   Pemeliharaan Jaringan & Hardware: Rp 150.000 / bulan.
*   Token API AI Cadangan (Bug fixing): Rp 200.000 / bulan.
*   **Total OPEX Bulanan**: **Rp 500.000 / bulan** (atau **Rp 6.000.000 / tahun**).

### 6.3. Estimasi Manfaat Finansial (Tangible Benefits)
`*[ESTIMASI — perlu validasi data riil dari pemilik]*`
Penerapan aplikasi ini ditargetkan memberikan penghematan dan peningkatan profitabilitas terukur:
1.  **Penghematan Waktu Pembukuan**: Reduksi waktu rekapitulasi dari 2-3 jam/hari menjadi instan [ref: 01_project_charter.md, Seksi 3.3 #1]. Nilai produktivitas waktu pemilik dialokasikan senilai Rp 1.500.000 / bulan.
2.  **Efisiensi Limbah Bahan Baku (Turun 15%)**: Mencegah kebocoran stok bahan baku cetak yang rusak/salah cetak melalui pencatatan limbah digital yang ketat [ref: 01_project_charter.md, Seksi 3.3 #2; ref: narasi.txt, baris 87]. Diestimasikan menghemat pengadaan bahan sebesar Rp 1.200.000 / bulan.
3.  **Penyelamatan Transaksi Terlewat (Zero-Missed Orders)**: Menyelamatkan rata-rata 3-5 pesanan kustom per bulan (undangan, stempel, baliho) yang sebelumnya terlewat akibat burnout pemilik [ref: 01_project_charter.md, Seksi 3.3 #3; ref: narasi.txt, baris 28]. Nilai transaksi diselamatkan diestimasikan sebesar Rp 2.000.000 / bulan.
*   **Total Manfaat Tangible**: **Rp 4.700.000 / bulan** (atau **Rp 56.400.000 / tahun**).

### 6.4. Estimasi Manfaat Non-Finansial (Intangible Benefits)
*   **Reduksi Stres Pemilik**: Pemulihan kesehatan mental pemilik dari burnout kronis [ref: narasi.txt, baris 28].
*   **Peningkatan Kredibilitas Usaha**: Pelayanan pelanggan menjadi jauh lebih profesional, responsif, dan tepat waktu [ref: 01_project_charter.md, Seksi 2.3].
*   **Keamanan Internal Toko**: Menghilangkan risiko fraud (kecurangan kas/stok) dari staf baru melalui log *Audit Trail* dan RBAC yang ketat [ref: 01_project_charter.md, Seksi 3.3 #4].
*   **Kesiapan Ekspansi**: Memiliki standardisasi sistem yang siap diduplikasi ke cabang baru (*Multi-Branch Ready*) [ref: 01_project_charter.md, Seksi 3.2 S.5].

### 6.5. Analisis Biaya-Manfaat (Cost-Benefit Analysis)
`*[ESTIMASI — berdasarkan proyeksi tahun ke-1]*`

| Deskripsi | Tahun 0 (Pengembangan) | Tahun 1 (Operasional) | Tahun 2 (Operasional) |
|-----------|------------------------|-----------------------|-----------------------|
| **Biaya Investasi (CAPEX)** | Rp 40.000.000 | Rp 0 | Rp 0 |
| **Biaya Operasional (OPEX)** | Rp 0 | Rp 6.000.000 | Rp 6.000.000 |
| **Total Biaya** | **Rp 40.000.000** | **Rp 6.000.000** | **Rp 6.000.000** |
| **Manfaat Finansial** | Rp 0 | Rp 56.400.000 | Rp 56.400.000 |
| **Arus Kas Bersih (Net Benefit)** | **(Rp 40.000.000)** | **Rp 50.400.000** | **Rp 50.400.000** |

### 6.6. Net Present Value (NPV)
`*[ESTIMASI — menggunakan tingkat diskonto 10%]*`
NPV dihitung untuk mengevaluasi kelayakan investasi dengan memperhitungkan nilai waktu dari uang (*time value of money*). Tingkat diskonto wajar untuk suku bunga kredit mikro di Indonesia ditetapkan sebesar **10% per tahun**. Proyeksi NPV atas investasi pengembangan sistem dengan operasional 2 tahun pertama adalah sebagai berikut:
*   Tahun 0 (Aliran Kas): (Rp 40.000.000)
*   Tahun 1 (Present Value dari Rp 50.400.000): Rp 45.818.182
*   Tahun 2 (Present Value dari Rp 50.400.000): Rp 41.652.893
*   Total Present Value dari Manfaat Bersih: Rp 87.471.075

$$\text{NPV} = \text{Total PV of Benefits} - \text{CAPEX}$$
$$\text{NPV} = \text{Rp 87.471.075} - \text{Rp 40.000.000} = \text{Rp 47.471.075}$$

Karena nilai **NPV > 0 (positif Rp 47.471.075)**, proyek ini dinilai sangat menguntungkan dan secara finansial **Sangat Layak** untuk dijalankan.

### 6.7. Estimasi Return on Investment (ROI)
`*[ESTIMASI]*`
Formula ROI Sederhana pada akhir Tahun 1:

$$\text{ROI} = \frac{\text{Net Benefit Tahun 1} - \text{CAPEX}}{\text{CAPEX}} \times 100\%$$
$$\text{ROI} = \frac{\text{Rp 50.400.000} - \text{Rp 40.000.000}}{\text{Rp 40.000.000}} \times 100\% = 26.0\%$$

Proyek memberikan tingkat pengembalian investasi sebesar **26.0%** pada tahun pertama, yang tergolong sangat sehat untuk investasi digital UMKM.

### 6.8. Estimasi Payback Period (Periode Pengembalian Modal)
`*[ESTIMASI]*`

$$\text{Payback Period} = \frac{\text{Total CAPEX}}{\text{Net Benefit Bulanan}} = \frac{\text{Rp 40.000.000}}{\text{Rp 4.200.000 / bulan}} = 9.5 \text{ Bulan}$$

Seluruh modal investasi awal sebesar Rp 40.000.000 diproyeksikan akan **kembali penuh dalam waktu 9,5 bulan** pasca Go-Live aplikasi.

### 6.9. Analisis Titik Impas (Break-Even Point - BEP)
`*[ESTIMASI]*`
Kalkulasi Break-Even Point (BEP) proyek ini dianalisis berdasarkan dua skenario parameter bisnis:
1.  **BEP Berdasarkan Waktu Operasional**: Titik impas akumulasi investasi awal (CAPEX Rp 40.000.000) dan biaya operasional (OPEX Rp 500.000/bulan) dicapai pada **bulan ke-9,5** masa operasional Go-Live.
2.  **BEP Berdasarkan Volume Transaksi Percetakan Kustom**:
    *   Asumsi margin keuntungan rata-rata per transaksi percetakan kustom (undangan, stempel, stiker, baliho) adalah **Rp 50.000 / transaksi**.
    *   *BEP Pengembalian CAPEX*: Untuk menutup investasi awal Rp 40.000.000, sistem harus memproses akumulasi **800 transaksi** percetakan kustom.
    *   *BEP Biaya Operasional (OPEX)*: Untuk menutup biaya operasional bulanan Rp 500.000, sistem harus memproses minimal **10 transaksi** percetakan kustom per bulan. Target ini sangat mudah dicapai mengingat volume transaksi harian AbuCom yang tinggi.

### 6.10. Analisis Sensitivitas (Proyeksi 3 Skenario)
`*[ESTIMASI]*`

*   **Skenario A: Best Case (Semua Lancar)**
    *   Asumsi: Manfaat finansial optimal (Rp 5.500.000/bulan), tidak ada kenaikan biaya.
    *   *Payback Period*: **8 Bulan**.
*   **Skenario B: Base Case (Sesuai Asumsi Normal)**
    *   Asumsi: Manfaat finansial normal (Rp 4.700.000/bulan), OPEX stabil Rp 500.000/bulan.
    *   *Payback Period*: **9,5 Bulan**.
*   **Skenario C: Worst Case (Delay & Biaya Membengkak)**
    *   Asumsi: Manfaat finansial turun (hanya Rp 3.000.000/bulan akibat adopsi lambat), OPEX naik Rp 700.000/bulan, dana cadangan Rp 4.500.000 terpakai habis di awal.
    *   *Payback Period*: **19 Bulan** (Tetap di bawah 2 tahun, masih tergolong layak).

### 6.11. Sumber Pendanaan dan Kemampuan Finansial
1.  **Laba Operasional Usaha**: Dana internal dialokasikan bertahap untuk mendukung operasional [ref: 01_project_charter.md, Seksi 9.2 #5].
2.  **Pinjaman Bank BRI & Mandiri**: Menyediakan likuiditas tetap, namun memiliki beban setoran bulanan tetap [ref: narasi.txt, baris 24, 66].
3.  **Pinjaman Tanpa Bunga Kerabat/Keluarga**: Sumber pendanaan yang sangat fleksibel tanpa bunga [ref: narasi.txt, baris 23].
    *   *Kerentanan*: Dana ini dapat ditarik mendadak, baik sebagian maupun total [ref: narasi.txt, baris 23]. Jika ditarik secara permanen di tengah jalan, hal ini dapat mengancam kelangsungan kas pengembangan proyek [ref: 01_project_charter.md, Seksi 10 Risiko #3].

### 6.12. Risiko Finansial dan Mitigasi

| No | Risiko Finansial | Probabilitas | Dampak | Rencana Mitigasi |
|----|------------------|:------------:|:------:|------------------|
| 1  | **Penarikan Dana Mendadak oleh Sahabat/Keluarga**: Likuiditas kas terganggu karena pinjaman tanpa bunga ditarik tiba-tiba saat pengerjaan modul kritis [ref: narasi.txt, baris 23]. | 3 | 4 | Gunakan alokasi Dana Cadangan Darurat Rp 4.500.000 khusus untuk mengunci biaya teknis software, jangan campur dengan kas toko [ref: 01_project_charter.md, Seksi 12 #5]. |
| 2  | **Kenaikan Harga Hardware Lokal**: Harga Mini PC Server atau PC Kasir naik tajam di pasar Indonesia sebelum sempat dibeli. | 3 | 2 | Lakukan pembelian perangkat keras utama (Mini PC Server & UPS) di Bulan ke-5 (Awal Fase Implementasi) untuk mengunci harga [ref: 01_project_charter.md, Seksi 11 #4]. |
| 3  | **Beban Bunga Bank Mengganggu Operasional**: Aliran kas tersedot untuk membayar setoran bulanan Bank BRI/Mandiri di tengah penurunan omzet sementara. | 2 | 4 | Buat modul pencatatan pengingat jatuh tempo setoran bank bulanan untuk menghindari denda keterlambatan pembayaran [ref: 01_project_charter.md, Seksi 8.1 F-6.2]. |

### 6.13. Kesimpulan Kelayakan Ekonomi
$$\color{orange}{\textbf{LAYAK DENGAN CATATAN (FEASIBLE WITH CONDITIONS)}}$$

Secara finansial, proyek kustom CLI Python ini sangat menguntungkan dengan estimasi *Payback Period* yang cepat (9,5 bulan), ROI tinggi (26%), dan NPV yang sangat positif (Rp 47.471.075). Catatan kelayakan terletak pada **pengelolaan likuiditas modal pinjaman tanpa bunga** yang harus dipisahkan dari modal kerja harian toko untuk mengantisipasi penarikan dana mendadak [ref: narasi.txt, baris 23].

---

## 7. Analisis Kelayakan Jadwal (Schedule Feasibility)

### 7.1. Timeline yang Direncanakan (12 Bulan)
Telah disusun jadwal tingkat tinggi yang terbagi menjadi 8 milestone besar selama 12 bulan [ref: 01_project_charter.md, Seksi 11]:
*   **M.1. Perencanaan (Bulan 1)**: Penyusunan Project Charter (Selesai).
*   **M.2. Analisis Requirements (Bulan 2)**: Penyusunan SRS (Open).
*   **M.3. Desain Sistem & DB (Bulan 3-4)**: SDD & ERD Multi-Branch.
*   **M.4. Implementasi Fase I (Bulan 5-6)**: Boilerplate, JWT, CRM & Transaksi Dasar.
*   **M.5. Implementasi Fase II (Bulan 7-9)**: Persediaan, BOM desimal, Kasbon/SDM, Antrian.
*   **M.6. Implementasi Fase III (Bulan 10)**: Laba/Rugi, Pinjaman, Aset, Audit Trail.
*   **M.7. Integrasi & Pengujian (Bulan 11)**: Skenario Uji & UAT.
*   **M.8. Go-Live & Pelatihan (Bulan 12)**: Input data awal Excel, Pelatihan staf 3 hari.

### 7.2. Evaluasi Kerealistisan Jadwal per Fase
*   **Durasi Keseluruhan (12 Bulan)**: Sangat longgar dan realistis untuk skala aplikasi internal UMKM. Rata-rata pengembangan aplikasi sejenis hanya membutuhkan waktu 4-6 bulan. Alokasi 12 bulan memberikan ruang yang sangat aman bagi pemilik usaha yang bertindak sebagai Junior Programmer di tengah kesibukan mengelola toko [ref: 01_project_charter.md, Seksi 7.1 Anggota 0].
*   **Bulan 7-9 (Implementasi Fase II - Persediaan & SDM)**: Alokasi 3 bulan dinilai sangat realistis untuk menyelesaikan logika terberat (BOM desimal dan skema penggajian otomatis) karena modul-modul ini dikerjakan secara paralel oleh Claude Sonnet 4.6 (spesialis *deep coding*) dan Gemini 3.1 Pro [ref: 01_project_charter.md, Seksi 7.1].
*   **Bulan 11 (Testing & UAT)**: Alokasi 1 month sangat memadai untuk melakukan pengujian manual CLI secara menyeluruh oleh Junior Programmer dan calon staf baru [ref: 01_project_charter.md, Seksi 11 #7].

### 7.3. Identifikasi Jalur Kritis (Critical Path)
Jalur kritis proyek (keterlambatan pada fase ini akan menunda go-live proyek) meliputi:
1.  **Fase 3: Desain Basis Data (Bulan 3-4)**: Skema database *multi-branch ready* harus benar dan matang sejak awal. Jika skema database salah, seluruh implementasi kode program di bulan berikutnya harus dirombak total [ref: 01_project_charter.md, Seksi 3.2 S.5].
2.  **Fase 5: Uji Coba HPP BOM (Bulan 7-9)**: Logika matematika dimensi desimal presisi harus divalidasi keakuratannya sebelum masuk ke modul keuangan terintegrasi [ref: narasi.txt, baris 95].

### 7.4. Faktor yang Dapat Memperlambat Jadwal
*   **Stres dan Burnout Pemilik**: Karena pemilik mengelola toko sendirian selama masa pengembangan, kelelahan fisik dapat menunda sesi klarifikasi kebutuhan atau pengujian modul sprint [ref: 01_project_charter.md, Seksi 10 Risiko #1].
*   **Kerumitan FP di Python**: Menolak OOP dan memaksa menulis kerangka kerja *Functional Programming* murni untuk fitur dinamis berpotensi memicu kendala penulisan kode yang memperlambat pengerjaan Junior Programmer [ref: 01_project_charter.md, Seksi 10 Risiko #4].

### 7.5. Risiko Jadwal dan Mitigasi

| No | Risiko Jadwal | Probabilitas | Dampak | Rencana Mitigasi |
|----|---------------|:------------:|:------:|------------------|
| 1  | **Burnout Pemilik Menghentikan Ulasan Proyek**: Pemilik sakit/kelelahan sehingga tidak sempat mereview hasil sprint coding 2 mingguan. | 3 | 5 | Serahkan penulisan dokumentasi rutin sepenuhnya kepada Gemini 3.1 Pro (Low) dan optimalkan waktu pemilik hanya untuk testing fungsional CLI yang krusial [ref: 01_project_charter.md, Seksi 7.1 Anggota 2]. |
| 2  | **Kerumitan Sintaksis FP Memperlambat Kodifikasi**: Kesulitan merancang alur state fungsional yang bersih dari OOP. | 2 | 4 | Gunakan pustaka standar `functools` dan manfaatkan Claude Sonnet 4.6 secara intensif untuk melakukan refaktorisasi kerangka program sejak awal implementasi [ref: 01_project_charter.md, Seksi 7.1 Anggota 4]. |
| 3  | **Input Data Awal Excel yang Berserakan Memakan Waktu**: Proses menyalin data dari Excel lama ke database MySQL memakan waktu berminggu-minggu [ref: narasi.txt, baris 70]. | 4 | 3 | Buatkan menu import CSV/Excel sederhana pada aplikasi CLI di akhir Fase I untuk mempercepat proses migrasi data awal secara semi-otomatis [ref: 01_project_charter.md, Seksi 9.1 #2]. |

### 7.6. Kesimpulan Kelayakan Jadwal
$$\color{green}{\textbf{LAYAK (FEASIBLE)}}$$

Dengan alokasi total durasi 12 bulan yang didukung metodologi pengembangan Hybrid (Waterfall-Agile) [ref: 01_project_charter.md, Seksi 9.4], serta bantuan intensif dari 6 asisten AI spesialis, jadwal proyek ini dinilai **Sangat Layak** dan aman untuk dicapai tanpa mengganggu kestabilan fisik pemilik usaha.

---

## 8. Analisis Kelayakan Hukum dan Organisasional (Legal & Organizational Feasibility)

### 8.1. Kepatuhan Regulasi dan Perizinan Usaha
`*[BERDASARKAN PENGETAHUAN UMUM — perlu validasi hukum jika diperlukan]*`
Sebagai unit usaha UMKM di Indonesia yang bergerak di bidang percetakan, retail, dan jasa perbaikan, AbuCom tidak memerlukan izin lisensi perangkat lunak khusus dari instansi pemerintah untuk mengoperasikan sistem internal. Namun, pemilik wajib memastikan usaha fisiknya terdaftar secara legal melalui **Nomor Induk Berusaha (NIB)** pada sistem **OSS (Online Single Submission)** Kementerian Investasi RI [ref: 0004_issue_validasi_feasibility_study.md, Seksi 8.1]. Kepemilikan NIB merupakan kewajiban hukum mutlak bagi kepatuhan perizinan berusaha retail & industri mikro di Indonesia guna menjaga legalitas saat melakukan operasional dan rekrutmen staf secara resmi.
*   **Penilaian**: **Layak**.

### 8.2. Kepatuhan Perlindungan Data Pribadi (UU PDP No. 27 Tahun 2022)
Aplikasi AbuCom menyimpan data sensitif pelanggan (Nama, Nomor WhatsApp, Riwayat Transaksi) dalam modul CRM [ref: 01_project_charter.md, Seksi 8.1 F-5.3], data riwayat kasbon karyawan [ref: 01_project_charter.md, Seksi 8.1 F-4.1], serta data keuangan pinjaman bank pemilik [ref: 01_project_charter.md, Seksi 8.1 F-6.2]. Sesuai ketentuan **UU PDP No. 27 Tahun 2022** di Indonesia, pemilik bertindak sebagai pengendali data pribadi pelanggan dan wajib memastikan keamanannya dari kebocoran yang berpotensi memicu sanksi denda hukum administrasi maupun pidana.
*   **Evaluasi Kelayakan**: Sistem telah merancang fitur pengamanan standar industri yang memadai untuk mematuhi UU PDP:
    *   Enkripsi satu arah *bcrypt* untuk kata sandi akun karyawan [ref: 01_project_charter.md, Seksi 8.2 N-2.3].
    *   *JSON Web Token* (JWT) untuk mengamankan session data CLI [ref: 01_project_charter.md, Seksi 8.2 N-2.3].
    *   Sistem pembatasan menu (RBAC) yang sangat ketat: Karyawan tidak diizinkan mengekspor atau melihat menu keuangan sensitif pemilik [ref: 01_project_charter.md, Seksi 8.2 N-2.1].
    *   *Audit Trail* mencatat setiap aktivitas penghapusan atau perubahan data sensitif [ref: 01_project_charter.md, Seksi 8.2 N-2.2].
*   **Penilaian**: **Layak dengan Catatan** (Catatan: Server basis data MySQL lokal harus dilindungi kata sandi root yang sangat kuat dan direktori backup database wajib dienkripsi [ref: 01_project_charter.md, Seksi 8.3 N-3.1]).

### 8.3. Lisensi Perangkat Lunak
Seluruh komponen perangkat lunak yang dipilih aman dari tuntutan pelanggaran hak cipta:
*   Bahasa Python berlisensi PSF (Python Software Foundation License) — 100% bebas biaya dan aman untuk komersial [ref: 01_project_charter.md, Seksi 12 #2].
*   Database MySQL Community Edition berlisensi GPL (General Public License) — 100% bebas biaya untuk penggunaan internal bisnis [ref: 01_project_charter.md, Seksi 12 #2].
*   Pustaka Python (`bcrypt`, `pyjwt`, `mysql-connector-python`) berlisensi open-source MIT/Apache/GPL yang aman [ref: 01_project_charter.md, Seksi 12 #2].
*   **Penilaian**: **Layak** (Bebas biaya lisensi tahunan, mengeliminasi risiko pembajakan software).

### 8.4. Aspek Ketenagakerjaan
`*[BERDASARKAN PENGETAHUAN UMUM — regulasi ketenagakerjaan Indonesia]*`
Rencana rekrutmen 7 staf baru wajib mematuhi regulasi ketenagakerjaan dasar di Indonesia yang diatur dalam undang-undang ketenagakerjaan (termasuk UU Cipta Kerja).
*   **Tantangan**: Pemilik harus menetapkan skema kontrak kerja yang jelas, baik Perjanjian Kerja Waktu Tertentu (**PKWT** untuk staf kasir/gudang kontrak) maupun Perjanjian Kerja Waktu Tidak Tertentu (**PKWTT** untuk posisi tetap Kepala Percetakan) [ref: 0004_issue_validasi_feasibility_study.md, Seksi 8.4]. Pemilik juga harus menghitung standar upah bulanan wajar yang disesuaikan dengan parameter:

    $$\text{Parameter Upah} = \text{*(UMR daerah operasional usaha — diisi oleh Pemilik Usaha berdasarkan Peraturan Gubernur/Bupati/Walikota setempat yang berlaku)*}$$

*   **Dukungan Sistem**: Modul SDM dan penggajian cerdas AbuCom memfasilitasi administrasi yang transparan bagi pemenuhan hak karyawan (perhitungan absensi harian, pemotongan otomatis sisa kasbon, dan akumulasi bonus poin insentif beban kerja) [ref: 01_project_charter.md, Seksi 8.1 F-4.1, F-4.2, F-4.3].
*   **Penilaian**: **Layak dengan Catatan** (Catatan: Pemilik wajib berkonsultasi mengenai standar kontrak kerja dasar untuk menghindari konflik ketenagakerjaan hukum di masa depan).

### 8.5. Struktur Organisasi dan Kesiapan Tata Kelola
Struktur organisasi 7 posisi operasional didukung budaya kerjasama lintas divisi (*cross-functional*) yang fleksibel [ref: narasi.txt, baris 34-43]. Budaya ini sangat baik untuk menambal kekosongan saat divisi lain sibuk.
*   **Kerentanan**: Budaya *cross-functional* tanpa kejelasan wewenang dapat memicu kekacauan pertanggungjawaban kas kasir jika ada karyawan non-kasir yang ikut melakukan transaksi pembayaran di aplikasi [ref: 01_project_charter.md, Seksi 10 Risiko #5].
*   **Solusi**: Aplikasi CLI harus menerapkan kewajiban login session dengan ID unik karyawan untuk setiap kali transaksi diinput ke dalam terminal kasir, guna memastikan integritas log aktivitas (*Audit Trail*) [ref: 01_project_charter.md, Seksi 8.2 N-2.1, N-2.2].
*   **Penilaian**: **Layak**.

### 8.6. Risiko Hukum/Organisasional dan Mitigasi

| No | Risiko Hukum/Organisasional | Probabilitas | Dampak | Rencana Mitigasi |
|----|-----------------------------|:------------:|:------:|------------------|
| 1  | **Pelanggaran UU PDP Akibat Flashdisk Karyawan**: Karyawan menyalin file database cadangan (.sql/.zip) yang berisi data pelanggan secara ilegal [ref: narasi.txt, baris 85]. | 2 | 5 | Kunci akses direktori backup database lokal di sistem operasi Linux Debian 12 hanya untuk user root, serta lakukan enkripsi pada file zip cadangan database menggunakan algoritma AES-256 [ref: 01_project_charter.md, Seksi 8.3 N-3.1]. |
| 2  | **Konflik Selisih Kas akibat Budaya Cross-Functional**: Beberapa staf bergantian menggunakan PC Kasir yang sama sehingga terjadi selisih kas fisik di laci kasir [ref: narasi.txt, baris 43, 83]. | 4 | 4 | Terapkan menu rekonsiliasi kas (*Cash Reconciliation*) wajib di akhir setiap shift/hari kerja, di mana staf kasir aktif harus memasukkan jumlah uang fisik sebelum dapat melakukan penutupan sistem [ref: 01_project_charter.md, Seksi 8.1 F-6.5]. |

### 8.7. Kesimpulan Kelayakan Hukum & Organisasional
$$\color{orange}{\textbf{LAYAK DENGAN CATATAN (FEASIBLE WITH CONDITIONS)}}$$

Proyek ini sepenuhnya aman dari sisi lisensi software open-source dan regulasi bisnis perizinan. Catatan kelayakan kritis terletak pada **disiplin kepatuhan UU PDP** terkait keamanan database pelanggan dari penyalinan ilegal, serta **kejelasan otorisasi sistem kasir** untuk mendukung budaya kerjasama tim tanpa memicu selisih pencatatan kas fisik [ref: 01_project_charter.md, Seksi 8.2 N-2.1, 8.2 N-2.2; ref: narasi.txt, baris 43].

---

## 9. Analisis Alternatif Solusi

Untuk memvalidasi kelayakan solusi yang diusulkan, dilakukan analisis perbandingan objektif terhadap 3 alternatif keputusan bisnis [ref: 0003_issue_feasibility_study.md, Bagian 3 #9]:

### 9.1. Alternatif 1: Tetap Menggunakan Excel (Status Quo / Do Nothing)
*   **Deskripsi**: Mempertahankan operasional harian yang berjalan saat ini dengan mengandalkan rekap manual lembar kerja Microsoft Excel yang berserakan [ref: narasi.txt, baris 47].
*   **Kelebihan**: Bebas investasi finansial awal (CAPEX Rp 0) dan tidak memerlukan waktu pelatihan staf baru [ref: narasi.txt, baris 70].
*   **Kekurangan**: Data inventaris dan keuangan tetap terfragmentasi, limbah produksi tidak terukur [ref: narasi.txt, baris 87], rawan kesalahan ketik manual (*human error*), tidak memiliki hak akses pengaman data sensitif [ref: narasi.txt, baris 89], tidak scalable, dan pemilik usaha dipastikan akan mengalami tingkat *burnout* kronis yang mengancam kesehatan [ref: narasi.txt, baris 28].

### 9.2. Alternatif 2: Menggunakan Aplikasi Siap Pakai (Off-the-Shelf Software)
*   **Deskripsi**: Menggunakan platform Software-as-a-Service (SaaS) ritel/POS berbayar populer di Indonesia seperti Accurate Online, Jurnal.id, Moka POS, atau Pawoon.
*   **Kelebihan**: Cepat diimplementasikan, memiliki antarmuka grafis (GUI) yang sangat ramah pengguna, didukung tim support vendor, serta teruji secara industri ritel.
*   **Kekurangan**:
    1.  **Biaya Berkelanjutan (OPEX) Sangat Tinggi**: Memerlukan biaya langganan bulanan per lisensi user/cabang yang membengkak dalam jangka panjang (UMKM *recurring cost*).
    2.  **Ketidakcocokan Fitur Kritis**: Tidak ada software ritel siap pakai yang mendukung formula HPP kustom berbasis Bill of Materials (BOM) multi-bahan yang presisi desimal untuk percetakan kustom [ref: narasi.txt, baris 95].
    3.  **Tidak Mendukung Penggajian Cerdas & Poin Kustom**: Logika gaji fleksibel berbasis laba dan insentif beban kerja harian AbuCom tidak dapat diakomodasi di sistem POS standard [ref: narasi.txt, baris 77-82].
    4.  **Keterbatasan Kontrol Data**: Data keuangan sensitif dan pinjaman modal pemilik harus disimpan di server pihak ketiga (cloud vendor), melanggar privasi penuh yang diharapkan pemilik [ref: narasi.txt, baris 89].

### 9.3. Alternatif 3: Membangun Aplikasi Kustom CLI (Solusi yang Diusulkan)
*   **Deskripsi**: Membangun aplikasi internal terpadu kustom berbasis CLI menggunakan bahasa pemrograman Python 3.14.2+ dengan database relasional MySQL lokal [ref: 01_project_charter.md, Seksi 1.2].
*   **Kelebihan**:
    1.  **100% Sesuai Kebutuhan Bisnis**: Seluruh logika unik (HPP BOM dimensi desimal, penggajian otomatis, sistem poin, status antrian, dan pengelolaan pinjaman modal) diakomodasi secara presisi [ref: 01_project_charter.md, Seksi 8.1].
    2.  **Biaya Investasi Sekali Bayar (CAPEX)**: Infrastruktur hardware mini PC server dan jaringan menjadi aset fisik milik toko, tanpa biaya langganan bulanan software [ref: 01_project_charter.md, Seksi 12].
    3.  **Kontrol Keamanan Mutlak**: File database disimpan di server lokal fisik di toko, sepenuhnya aman dari akses pihak ketiga luar [ref: 01_project_charter.md, Seksi 8.2 N-2.1].
    4.  **Kesiapan Skalabilitas Ekspansi**: Database dirancang siap menampung ID cabang sejak awal (*Multi-Branch Ready*) [ref: 01_project_charter.md, Seksi 3.2 S.5].
*   **Kekurangan**: Membutuhkan waktu pengembangan selama 12 bulan [ref: 01_project_charter.md, Seksi 1.6], risiko kegagalan teknis coding FP [ref: 01_project_charter.md, Seksi 10 Risiko #4], serta menuntut waktu adaptasi staf terhadap visual teks CLI [ref: 01_project_charter.md, Seksi 10 Risiko #6].

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

Meskipun Alternatif 3 menuntut investasi finansial awal (Rp 40 juta) dan waktu tunggu pengembangan selama 12 bulan, alternatif ini merupakan **satu-satunya solusi** yang mampu mengakomodasi kebutuhan kritis fungsional AbuCom yang sangat spesifik, yaitu formula perhitungan HPP BOM dimensi desimal [ref: narasi.txt, baris 95] dan manajemen penggajian cerdas berbasis insentif poin [ref: narasi.txt, baris 77-82]. Alternatif 2 ditolak secara mutlak karena keterbatasan fitur standard ritel mereka yang tidak dapat dikustomisasi, sementara Alternatif 1 harus segera ditinggalkan untuk mencegah kehancuran kesehatan mental pemilik akibat burnout operasional harian [ref: narasi.txt, baris 28].

---

## 10. Matriks Ringkasan Kelayakan

Berikut adalah rangkuman evaluasi kelayakan komprehensif AbuCom berdasarkan hasil analisis kelima dimensi kelayakan [ref: 0003_issue_feasibility_study.md, Bagian 3 #10]:

| No | Dimensi Kelayakan | Status Kelayakan | Catatan Kunci & Syarat Kelayakan |
|----|-------------------|:----------------:|-----------------------------------|
| 1  | **Kelayakan Teknis** | $$\color{orange}{\textbf{Layak dg Catatan}}$$ | Pustaka & runtime Python/MySQL sangat stabil [ref: 01_project_charter.md, Seksi 12 #2]. Diperlukan kedisiplinan integrasi asisten AI untuk memitigasi kerumitan state management dalam *Functional Programming* [ref: 01_project_charter.md, Seksi 7.1]. |
| 2  | **Kelayakan Operasional** | $$\color{orange}{\textbf{Layak dg Catatan}}$$ | Sistem sangat dibutuhkan untuk mengatasi burnout pemilik [ref: narasi.txt, baris 28]. Rekrutmen 7 staf operasional harus diselesaikan tepat waktu sebelum Go-Live aplikasi [ref: 01_project_charter.md, Seksi 9.1 #1]. |
| 3  | **Kelayakan Ekonomi** | $$\color{orange}{\textbf{Layak dg Catatan}}$$ | Potensi pengembalian modal investasi sangat cepat (~9,5 bulan), ROI tinggi (26%), dan NPV positif (Rp 47.471.075) [ref: Seksi 6.6, 6.7]. Kas pengembangan proyek wajib dilindungi dari penarikan mendadak modal pinjaman tanpa bunga [ref: narasi.txt, baris 23]. |
| 4  | **Kelayakan Jadwal** | $$\color{green}{\textbf{Layak}}$$ | Alokasi waktu keseluruhan 12 bulan sangat longgar dan realistis untuk diselesaikan secara kolaboratif bersama 6 asisten AI spesialis [ref: 01_project_charter.md, Seksi 7.1, 11]. |
| 5  | **Kelayakan Hukum** | $$\color{orange}{\textbf{Layak dg Catatan}}$$ | 100% aman dari masalah biaya lisensi software komersial [ref: 01_project_charter.md, Seksi 12 #2]. Penerapan NIB pada OSS dan kontrak kerja PKWT/PKWTT staf harus diatur legalitasnya. Direktori backup database wajib dienkripsi kuat untuk mematuhi ketentuan UU PDP No. 27/2022 [ref: 01_project_charter.md, Seksi 8.3 N-3.1]. |

---

## 11. Rekomendasi Akhir dan Kesimpulan

### 11.1. Keputusan Kelayakan
Berdasarkan evaluasi komprehensif terhadap seluruh aspek teknis, operasional, finansial, jadwal, dan hukum, proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan** diputuskan **GO DENGAN CATATAN (GO WITH CONDITIONS)**. Keputusan bisnis ini diambil karena manfaat strategis otomatisasi sistem yang akan menyelamatkan kelangsungan usaha dari risiko kegagalan operasional (*burnout* pemilik) jauh lebih besar daripada risiko-risiko teknis atau finansial yang teridentifikasi [ref: narasi.txt, baris 28].

### 11.2. Prasyarat dan Catatan Penting Sebelum Melanjutkan
Sebelum proyek melangkah secara formal ke Fase SDLC berikutnya (Requirements & SRS) [ref: 01_project_charter.md, Seksi 5.2 #2], pemilik usaha wajib memenuhi prasyarat kritis berikut:
1.  **Penguncian Dana Contingency**: Pisahkan dana cadangan darurat sebesar **Rp 4.500.000** ke dalam rekening khusus terpisah untuk menjamin pengerjaan software tidak terganggu jika pinjaman tanpa bunga kerabat ditarik mendadak [ref: 01_project_charter.md, Seksi 12 #5; ref: narasi.txt, baris 23].
2.  **Pemetaan UMR & Standar Upah**: Pemilik wajib menetapkan nominal upah bulanan staf baru disesuaikan dengan regulasi upah setempat berdasarkan formula:
    
    $$\text{Standar Upah} = \text{*(UMR daerah operasional usaha — diisi oleh Pemilik Usaha berdasarkan Peraturan Gubernur/Bupati/Walikota setempat yang berlaku)*}$$
    
    untuk diintegrasikan dalam skema database penggajian cerdas [ref: narasi.txt, baris 67].
3.  **Draft Skenario Uji Awal (BOM)**: Menyusun draf manual data dimensi bahan baku fisik (panjang x lebar stempel flash dan volume cairan tinta) guna keperluan validasi logika formula HPP saat masa coding dimulai [ref: narasi.txt, baris 95-96].

### 11.3. Langkah Selanjutnya (Next Steps)
Setelah dokumen Feasibility Study ini disetujui secara digital oleh pemilik usaha:
1.  Segera inisiasi Fase 2 (Requirements) untuk menyusun dokumen **SRS (Software Requirements Specification)** yang merinci 20+ detail kebutuhan fungsional secara formal [ref: 01_project_charter.md, Seksi 11 #2].
2.  Lakukan proses pembersihan data awal (*cleansing*) pada catatan Excel yang berserakan agar siap diimpor saat sistem selesai dideploy [ref: narasi.txt, baris 70].
3.  Persiapkan skedul rekrutmen staf pramuniaga dan gudang pada Bulan ke-9 pengembangan [ref: 01_project_charter.md, Seksi 11 #5].

---

## 12. Glosarium

Berikut adalah glosarium istilah domain percetakan, retail, teknis, hukum, dan keuangan yang digunakan dalam analisis studi kelayakan ini untuk menyamakan pemahaman pembaca [ref: 01_project_charter.md, Glosarium]:
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
14. **Functional Programming (Pemrograman Fungsional)**: Paradigma pemrograman yang memperlakukan komputasi sebagai evaluasi fungsi matematika dan menghindari perubahan status (*state*) serta data yang dapat dimutasi (*mutable data*).
15. **CAPEX (Capital Expenditure)**: Investasi awal berupa biaya pengeluaran modal untuk pengadaan aset fisik infrastruktur (Mini PC Server, jaringan lokal, PC Kasir) di awal proyek [ref: Seksi 6.1].
16. **OPEX (Operational Expenditure)**: Biaya operasional rutin bulanan/tahunan pasca go-live yang dibutuhkan untuk memelihara kestabilan sistem aplikasi dan infrastruktur server [ref: Seksi 6.2].
17. **ROI (Return on Investment)**: Rasio persentase yang menunjukkan tingkat efisiensi atau profitabilitas dari pengembalian modal investasi yang ditanamkan pada proyek [ref: Seksi 6.6].
18. **Payback Period**: Jangka waktu yang dibutuhkan untuk memperoleh kembali seluruh modal investasi awal (CAPEX) berdasarkan akumulasi arus manfaat bersih tahunan [ref: Seksi 6.7].
19. **Cost-Benefit Analysis**: Metode analisis finansial sistematis yang membandingkan total estimasi biaya dengan total estimasi manfaat yang diperoleh guna menentukan kelayakan ekonomi [ref: Seksi 6.5].
20. **Analisis Sensitivitas**: Analisis simulasi keuangan proyeksi kelayakan ekonomi di bawah pengaruh fluktuasi parameter eksternal (Best Case, Base Case, Worst Case) [ref: Seksi 6.8].
21. **Jalur Kritis (Critical Path)**: Rangkaian aktivitas proyek yang menentukan durasi tercepat penyelesaian keseluruhan proyek, di mana keterlambatan pada jalur ini akan otomatis menunda tanggal selesai proyek [ref: Seksi 7.3].
22. **UU PDP (Undang-Undang Pelindungan Data Pribadi)**: Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 yang mengatur mengenai hak subjek data pribadi, kewajiban pengelola data, dan sanksi hukum atas kebocoran data [ref: Seksi 8.2].
23. **NPV (Net Present Value)**: Selisih antara nilai sekarang dari aliran kas masuk (manfaat) dengan nilai sekarang dari aliran kas keluar (CAPEX) pada periode waktu tertentu dengan memperhitungkan faktor diskonto [ref: Seksi 6.6].
24. **BEP (Break-Even Point)**: Analisis titik impas untuk mengetahui tingkat volume transaksi atau masa operasional di mana total biaya investasi dan operasional sama dengan total pendapatan/manfaat [ref: Seksi 6.9].
25. **NIB (Nomor Induk Berusaha)**: Identitas pelaku usaha resmi di Indonesia yang diterbitkan oleh Lembaga OSS setelah pelaku usaha melakukan pendaftaran usahanya [ref: Seksi 8.1].
26. **OSS (Online Single Submission)**: Sistem perizinan berusaha terintegrasi secara elektronik yang dikelola oleh Kementerian Investasi/BKPM RI untuk memfasilitasi legalitas UMKM dan korporasi di Indonesia [ref: Seksi 8.1].
27. **PKWT (Perjanjian Kerja Waktu Tertentu)**: Perjanjian kerja antara pekerja/buruh dengan pengusaha untuk mengadakan hubungan kerja dalam waktu tertentu atau untuk pekerja yang bersifat tidak tetap/kontrak [ref: Seksi 8.4].
28. **PKWTT (Perjanjian Kerja Waktu Tidak Tertentu)**: Perjanjian kerja antara pekerja/buruh dengan pengusaha untuk mengadakan hubungan kerja yang bersifat tetap [ref: Seksi 8.4].

---

## 13. Referensi Dokumen

Berikut adalah daftar dokumen acuan primer dan sekunder yang digunakan dalam penyusunan Feasibility Study ini [ref: 0003_issue_feasibility_study.md, Bagian 3 #13]:

| # | Nama File                     | Lokasi                                            | Keterangan                                                                    |
|---|-------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------|
| 1 | `01_project_charter.md`       | `docs/sdlc/01_planning/01_project_charter.md`     | Dokumen Project Charter v1.1 — referensi utama data proyek yang tervalidasi.  |
| 2 | `narasi.txt`                  | `docs/sdlc/narasi.txt`                            | Dokumen narasi asli pemilik usaha — referensi pendukung konteks operasional.  |
| 3 | `0003_issue_feasibility_study.md` | `docs/issue/0003_issue_feasibility_study.md`  | Dokumen instruksi issue pembuatan Feasibility Study ini.                      |
| 4 | `0004_issue_validasi_feasibility_study.md` | `docs/issue/0004_issue_validasi_feasibility_study.md` | Dokumen instruksi audit, validasi, dan perbaikan penulisan kelayakan ini. |
