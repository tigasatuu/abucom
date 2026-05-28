---
dokumen    : Stakeholder Register
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.2
tanggal    : 2026-05-28
status     : Validated
penyusun   : Senior Project Management Consultant & Stakeholder Governance Specialist
---

# Stakeholder Register — AbuCom

## Riwayat Perubahan Dokumen

| Versi | Tanggal | Perubahan | Oleh |
|---|---|---|---|
| 1.0 | 2026-05-21 | Pembuatan awal dokumen berdasarkan analisis Project Charter, Feasibility Study, dan Narasi Pemilik Usaha. | Senior Stakeholder Analyst & Project Governance Specialist |
| 1.1 | 2026-05-22 | Validasi, analisis, dan penyempurnaan menyeluruh dokumen. Menambahkan Executive Summary, memetakan Hak Akses RBAC & Status Kerja PKWT/PKWTT secara eksplisit, merancang Matriks Pemetaan Modul vs Stakeholder, mengintegrasikan risiko baru (migrasi Excel & FP Python), menyempurnakan format data kosong (placeholder interaktif), menyelaraskan regulasi ketenagakerjaan & perbankan Indonesia, serta mengoreksi bahasa. | Senior Stakeholder Analyst & Project Governance Specialist |
| 1.2 | 2026-05-28 | Validasi dan penyempurnaan komprehensif dokumen sesuai standar PMBOK. Menyelaraskan nilai Power/Interest dengan Influence/Impact, menyempurnakan format instruksi placeholder, menambahkan siklus pembaruan dokumen, melengkapi glosarium (BOM, CAPEX, dll.), memastikan penugasan RACI dan status aktor UAT/Pelatihan secara eksplisit, serta mengintegrasikan referensi Tech Stack dan Innovation Proposal. | Senior Project Management Consultant & Stakeholder Governance Specialist |

---

## 1. Informasi Dokumen

Dokumen **Stakeholder Register** ini dirancang secara khusus untuk mengidentifikasi, menganalisis, mengklasifikasikan, serta menentukan strategi pengelolaan bagi seluruh pihak yang berkepentingan terhadap proyek pembangunan **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**.

Sebagai bagian integral dari fase *Planning* dalam siklus SDLC, dokumen ini bertujuan untuk:
1. **Identifikasi Komprehensif**: Mendokumentasikan seluruh pemangku kepentingan (individu, kelompok, maupun institusi) yang mempengaruhi atau dipengaruhi oleh jalannya proyek.
2. **Analisis Pengaruh & Kepentingan**: Memetakan dinamika kekuasaan (*power*) dan minat (*interest*) masing-masing pemangku kepentingan untuk memprioritaskan upaya tata kelola.
3. **Penyusunan Strategi Pelibatan**: Merancang rencana komunikasi terstruktur dan mitigasi potensi resistensi untuk memastikan transisi operasional yang mulus dari manual berbasis Excel ke sistem digital berbasis CLI.

### Hubungan dengan Dokumen SDLC Lainnya:
* **Project Charter**: Dokumen ini memperluas identifikasi awal stakeholder dan RACI Matrix yang tercantum di Project Charter.
* **Software Requirements Specification (SRS)**: Profil, hak akses (RBAC), dan kebutuhan stakeholder yang tercatat di sini menjadi input utama bagi pembatasan hak akses modul serta kebutuhan fungsional database pelanggan (CRM).
* **System Design Document (SDD)**: Menentukan rancangan logis hak akses database dan log Audit Trail berdasarkan definisi peran.
* **User Acceptance Testing (UAT) & Deployment**: Menjadi acuan bagi penentuan aktor penguji skenario UAT dan target pelatihan operasional.

### 1.1. Ringkasan Eksekutif (Executive Summary)

Berdasarkan analisis kritis dan validasi komprehensif terhadap tata kelola proyek AbuCom, diidentifikasi total **19 pemangku kepentingan (stakeholder)** yang terbagi secara proporsional ke dalam **14 stakeholder internal** dan **5 stakeholder eksternal**. Proyek ini menghadapi tantangan transisi yang unik dari model operasional manual berbasis Excel (*single-fighter*) menuju model organisasi digital terotomatisasi yang didukung oleh **7 staf operasional baru** dan **6 model AI spesialis**.

Wawasan kritis dari tata kelola stakeholder proyek ini meliputi:
* **Faktor Sukses Utama (Single Point of Failure):** Kesuksesan proyek sangat bergantung pada kesiapan fisik dan mental Pemilik Usaha (STK-001) yang bertindak sebagai Manajer Proyek Internal dan integrator kode. Mitigasi kelelahan (*burnout*) pemilik menjadi prioritas tertinggi.
* **Tantangan Adopsi Visual CLI:** Penggunaan antarmuka teks CLI (Command Line Interface) menuntut kesiapan literasi digital yang tinggi dari staf baru. Hal ini dimitigasi melalui standardisasi kontrak kerja (PKWT/PKWTT) dan pelatihan simulasi terstruktur selama 3 hari.
* **Pemisahan Likuiditas dan Pengendalian Finansial:** Risiko penarikan modal mendadak dari Kerabat & Keluarga (STK-019) dimitigasi secara ketat melalui pemisahan rekening Dana Cadangan Darurat sebesar **Rp 4.500.000** dan transparansi saldo piutang terotomatisasi di dalam sistem.
* **Jembatan Konseptual Kebutuhan:** Dokumen ini menetapkan pemetaan Hak Akses RBAC (Role-Based Access Control) dan Matriks Pemetaan Modul vs Stakeholder untuk memastikan keselarasan penuh saat tim AI mentransisikan perencanaan ini ke fase SRS, SDD, dan pengujian UAT.

### 1.2. Siklus Pembaruan Dokumen

Dokumen Stakeholder Register ini bersifat dinamis (*living document*) dan wajib ditinjau serta diperbarui dalam kondisi berikut:
1. Setelah selesainya fase rekrutmen staf baru (untuk memperbarui placeholder kontak dan identitas aktual staf pada STK-002 s.d. STK-008).
2. Ketika terjadi perubahan ruang lingkup operasional, inovasi baru, atau pengenalan modul baru yang berdampak pada peran stakeholder.
3. Saat terjadi perubahan signifikan dalam struktur pendanaan proyek (misal: penambahan pinjaman bank atau perubahan komitmen kerabat).

---

## 2. Daftar Identifikasi Stakeholder

Berikut adalah daftar 19 stakeholder proyek AbuCom yang diklasifikasikan ke dalam kelompok internal (terlibat langsung dalam pengembangan atau operasional harian) dan eksternal (mempengaruhi proyek dari luar batas organisasi).

### 2.1. Stakeholder Internal

| ID | Nama / Jabatan | Peran dalam Proyek | Kategori | Keterangan |
|---|---|---|---|---|
| **STK-001** | Pemilik Usaha AbuCom | Inisiator, Sponsor Utama, Penyedia Pendanaan, Manajer Proyek Internal, Junior Programmer, Key User | Sponsor & Pengguna Utama | Pemilik bisnis tunggal yang memegang keputusan akhir dan bertindak sebagai integrator kode program. |
| **STK-002** | Calon Staf Kepala Percetakan | Pengguna Operasional (End-User) | End-User Operasional | Bertanggung jawab atas koordinasi toko, pemantauan antrian, stok, dan laporan harian. |
| **STK-003** | Calon Staf Pramuniaga | Pengguna Operasional (End-User) | End-User Operasional | Melayani pelanggan di garda depan, mencatat kontak CRM, dan menginput antrian transaksi. |
| **STK-004** | Calon Staf Kasir | Pengguna Operasional (End-User) | End-User Operasional | Menangani pembayaran, pencatatan DP/pelunasan, dan rekonsiliasi uang fisik laci kasir. |
| **STK-005** | Calon Staf Desainer | Pengguna Operasional (End-User) | End-User Operasional | Mengelola antrian desain, memproses berkas desain kustom, dan mencatat lokasi arsip. |
| **STK-006** | Calon Staf Produksi Cetak | Pengguna Operasional (End-User) | End-User Operasional | Eksekusi cetak fisik, pencatatan bahan baku riil, pemantauan limbah produksi (*waste*). |
| **STK-007** | Calon Staf Fotocopy & Print Dokumen | Pengguna Operasional (End-User) | End-User Operasional | Mencatat transaksi cepat fotokopi/print, membantu divisi cetak saat antrian padat. |
| **STK-008** | Calon Staf Gudang | Pengguna Operasional (End-User) | End-User Operasional | Mengelola stok masuk/keluar, pencatatan supplier, utang pembelian, dan Stock Opname berkala. |
| **STK-009** | Gemini 3.1 Pro (High) | Lead Architect & Heavy Logic | Tim Pengembang AI | Merancang arsitektur sistem modular, logika BOM dimensi desimal, dan penggajian cerdas. |
| **STK-010** | Gemini 3.1 Pro (Low) | Routine Coding & Documentation | Tim Pengembang AI | Menulis kode rutin dan menyusun dokumentasi formal (SRS, SDD, User Manual). |
| **STK-011** | Gemini 3 Flash | Fast Reviewer & Debugger | Tim Pengembang AI | Melakukan review cepat, identifikasi kesalahan sintaksis, dan perbaikan bug ringan. |
| **STK-012** | Claude Sonnet 4.6 (Thinking) | Deep Coder & Refactoring Specialist | Tim Pengembang AI | Implementasi kode fungsional kompleks, optimasi CLI, dan refaktorisasi modul kritis. |
| **STK-013** | Claude Opus 4.6 (Thinking) | System Strategist & Security Lead | Tim Pengembang AI | Merancang skema otentikasi (JWT), enkripsi (bcrypt), log Audit Trail, dan privasi data. |
| **STK-014** | GPT-OSS 120B (Medium) | Boilerplate Generator & Dummy Data Specialist | Tim Pengembang AI | Membuat kode boilerplate dasar database dan skrip data awal dummy (*seed SQL*). |

### 2.2. Stakeholder Eksternal

| ID | Nama / Jabatan | Peran dalam Proyek | Kategori | Keterangan |
|---|---|---|---|---|
| **STK-015** | Pelanggan AbuCom | Penerima Manfaat Layanan (Beneficiary) | Indirect Stakeholder / Beneficiary | Pihak yang menggunakan jasa percetakan, ATK, PPOB, jasa keuangan, dan service printer/PC. |
| **STK-016** | Vendor & Supplier Bahan Baku / ATK | Penyedia Pasokan Bahan Baku dan ATK | Indirect Stakeholder / Supply Chain | Pihak ketiga yang menyuplai bahan stempel, kertas, tinta, dan barang retail ATK. |
| **STK-017** | Bank BRI | Kreditur Modal Berbunga (Institusi) | Financial Stakeholder | Lembaga keuangan penyedia pinjaman modal usaha dengan setoran bulanan dan tenor tetap. |
| **STK-018** | Bank Mandiri | Kreditur Modal Berbunga (Institusi) | Financial Stakeholder | Lembaga keuangan penyedia pinjaman modal usaha dengan setoran bulanan dan tenor tetap. |
| **STK-019** | Kerabat & Keluarga | Pemberi Pinjaman Tanpa Bunga (Individu) | Financial Stakeholder | Sahabat, teman, dan keluarga pemilik yang meminjamkan dana modal dengan penarikan fleksibel. |

---

## 3. Profil Detail Stakeholder

### 3.1. [STK-001] Pemilik Usaha AbuCom

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-001 |
| **Nama / Jabatan** | Pemilik Usaha AbuCom |
| **Organisasi / Afiliasi** | UMKM Percetakan AbuCom |
| **Kategori** | Internal |
| **Tipe** | Individu |
| **Peran dalam Proyek** | Inisiator, Sponsor Utama, Penyedia Pendanaan, Manajer Proyek Internal, Junior Programmer, Key User |
| **Kontak / Identifikasi** | `[DIISI OLEH PEMILIK USAHA — Format: "Nama Lengkap Pemilik | Alamat Email | No. WhatsApp Aktif"]` |
| **Hak Akses RBAC** | `Role: pemilik` (Akses administratif penuh terhadap seluruh menu keuangan, tabungan alat, administrasi pinjaman bank/keluarga, penggajian karyawan/payroll, manajemen absensi, CRM, antrian, stock opname, database, serta log Audit Trail lengkap). |

**Kebutuhan dan Ekspektasi Utama**:
* Menghilangkan ketergantungan pada pencatatan manual Microsoft Excel yang tidak terintegrasi dan memicu kelelahan fisik/mental (*burnout*).
* Memiliki laporan keuangan laba/rugi, pengeluaran rutin, dan tabungan aset secara instan (<5 detik) dan akurat untuk memantau performa 5 divisi usaha.
* Mengotomatisasi pemotongan stok bahan baku secara presisi menggunakan komposisi bahan (*Bill of Materials* / BOM) dengan dimensi desimal (panjang x lebar atau volume desimal) setelah transaksi selesai.
* Pengamanan hak akses yang ketat (RBAC) agar data pinjaman bank, tabungan pribadi, dan modul payroll hanya dapat diakses oleh Pemilik Usaha.
* Memantau kehadiran staf, sisa utang kasbon staf, dan perhitungan penggajian cerdas (gaji pokok vs persentase keuntungan) secara otomatis.

**Potensi Pengaruh terhadap Proyek**:
* **Sangat Tinggi (5)**. Pemilik memegang kontrol mutlak atas anggaran proyek (CAPEX Rp 40.000.000), penentuan prioritas ruang lingkup, durasi pengembangan (12 bulan), dan otorisasi persetujuan dokumen SDLC. Bertindak sebagai pengembang junior yang melakukan integrasi akhir kode program.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Sangat Tinggi (5)**. Keberhasilan aplikasi ini akan secara drastis memangkas beban operasional harian pemilik (pembukuan terotomatisasi), memitigasi risiko *burnout*, dan memungkinkan delegasi 90% aktivitas teknis harian ke staf baru dengan aman.

**Fase Keterlibatan Maksimal**:
* Seluruh fase SDLC (Planning, Requirements, Design, Implementation, Testing, Deployment, Operational).

---

### 3.2. [STK-002] Calon Staf Kepala Percetakan

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-002 |
| **Nama / Jabatan** | Calon Staf Kepala Percetakan |
| **Organisasi / Afiliasi** | Toko Percetakan AbuCom (Fase Operasional) |
| **Kategori** | Internal |
| **Tipe** | Individu |
| **Peran dalam Proyek** | Pengguna Operasional (End-User) |
| **Kontak / Identifikasi** | `[DIISI OLEH PEMILIK USAHA setelah rekrutmen — Format: "Nama Lengkap | No. WhatsApp Aktif (contoh: +6281234567890)"]` |
| **Hak Akses RBAC** | `Role: kepala_percetakan` (Akses menengah: mengawasi dashboard antrian/job tracking, memantau persediaan barang di gudang, meluncurkan dan mereview Stock Opname, serta mencatat data absensi staf harian). |
| **Status Ketenagakerjaan** | Karyawan Tetap (**PKWTT** — Perjanjian Kerja Waktu Tidak Tertentu) berdasarkan regulasi PP No. 35 Tahun 2021. |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan antarmuka CLI (*Command Line Interface*) yang logis, menu yang teratur, dan navigasi yang cepat.
* Membutuhkan visualisasi antrian pengerjaan (*job tracking*) yang mudah dipantau untuk mengkoordinasikan tim produksi dan desainer.
* Akses mudah untuk memantau tingkat persediaan bahan baku dan barang retail di gudang guna mencegah kekosongan bahan.
* Memerlukan *CLI User Manual* dan program pelatihan fungsional yang memadai sebelum go-live.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Tidak mempengaruhi arsitektur sistem pada fase pengembangan, namun penting pada operasional.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Tinggi (4)**. Memudahkan pemantauan seluruh aktivitas toko tanpa perlu melakukan pengecekan fisik lembar demi lembar catatan kertas/Excel.

**Fase Keterlibatan Maksimal**:
* Testing (Sebagai Aktor UAT Utama), Deployment (Target Pelatihan Utama), dan Operational.

---

### 3.3. [STK-003] Calon Staf Pramuniaga

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-003 |
| **Nama / Jabatan** | Calon Staf Pramuniaga |
| **Organisasi / Afiliasi** | Toko Percetakan AbuCom (Fase Operasional) |
| **Kategori** | Internal |
| **Tipe** | Individu |
| **Peran dalam Proyek** | Pengguna Operasional (End-User) |
| **Kontak / Identifikasi** | `[DIISI OLEH PEMILIK USAHA setelah rekrutmen — Format: "Nama Lengkap | No. WhatsApp Aktif (contoh: +6281234567890)"]` |
| **Hak Akses RBAC** | `Role: pramuniaga` (Akses transaksi: mencatat transaksi penjualan ritel ATK, menginput order produk kustom ke antrian status `Antri`, mencari harga barang, dan mencatatkan data kontak pelanggan CRM). |
| **Status Ketenagakerjaan** | Karyawan Kontrak (**PKWT** — Perjanjian Kerja Waktu Tertentu) berdasarkan regulasi PP No. 35 Tahun 2021. |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan menu pencatatan transaksi yang cepat saat melayani pelanggan langsung di konter.
* Fitur pencarian harga barang retail ATK, produk percetakan kustom, dan tarif layanan digital (PPOB) yang dinamis sesuai skema harga (retail, grosir, mitra).
* Kemudahan penginputan data kontak pelanggan (CRM) dan spesifikasi pesanan khusus ke dalam sistem antrian.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Sebagai pengguna akhir operasional entry data.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Tinggi (4)**. Mempercepat proses pelayanan pelanggan karena tidak perlu lagi membuka-buka file Excel harga secara manual yang lambat.

**Fase Keterlibatan Maksimal**:
* Testing (Sebagai Aktor UAT), Deployment (Target Pelatihan), dan Operational.

---

### 3.4. [STK-004] Calon Staf Kasir

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-004 |
| **Nama / Jabatan** | Calon Staf Kasir |
| **Organisasi / Afiliasi** | Toko Percetakan AbuCom (Fase Operasional) |
| **Kategori** | Internal |
| **Tipe** | Individu |
| **Peran dalam Proyek** | Pengguna Operasional (End-User) |
| **Kontak / Identifikasi** | `[DIISI OLEH PEMILIK USAHA setelah rekrutmen — Format: "Nama Lengkap | No. WhatsApp Aktif (contoh: +6281234567890)"]` |
| **Hak Akses RBAC** | `Role: kasir` (Akses kasir: melayani transaksi pembayaran tunai/e-wallet, mencatat Down Payment (DP) dan pelunasan, melakukan rekonsiliasi kas laci kasir harian, serta memproses retur/pembatalan transaksi). |
| **Status Ketenagakerjaan** | Karyawan Kontrak (**PKWT** — Perjanjian Kerja Waktu Tertentu) berdasarkan regulasi PP No. 35 Tahun 2021. |

**Kebutuhan dan Ekspektasi Utama**:
* Fitur pencatatan pembayaran yang fleksibel (DP di awal, pelunasan di akhir saat barang diambil).
* Modul khusus rekonsiliasi kas laci fisik (*cash reconciliation*) di akhir shift untuk mendeteksi selisih uang tunai.
* Pilihan otomatis penentuan biaya admin termurah dari 6 e-wallet untuk jasa transfer/tarik tunai.
* Alur penanganan retur barang rusak atau pembatalan transaksi dengan pengembalian DP yang secara otomatis menyinkronkan data kas.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Namun, kepatuhan kasir menginput data menentukan validitas arus kas harian.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Tinggi (4)**. Memberikan keamanan kerja karena rekonsiliasi tercatat secara sistematis di Audit Trail, mengurangi risiko tuduhan kecurangan sepihak.

**Fase Keterlibatan Maksimal**:
* Testing (Sebagai Aktor UAT), Deployment (Target Pelatihan), dan Operational.

---

### 3.5. [STK-005] Calon Staf Desainer

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-005 |
| **Nama / Jabatan** | Calon Staf Desainer |
| **Organisasi / Afiliasi** | Toko Percetakan AbuCom (Fase Operasional) |
| **Kategori** | Internal |
| **Tipe** | Individu |
| **Peran dalam Proyek** | Pengguna Operasional (End-User) |
| **Kontak / Identifikasi** | `[DIISI OLEH PEMILIK USAHA setelah rekrutmen — Format: "Nama Lengkap | No. WhatsApp Aktif (contoh: +6281234567890)"]` |
| **Hak Akses RBAC** | `Role: desainer` (Akses desainer: melihat antrian dengan status `Proses Desain`, memperbarui status menjadi `Produksi`, dan menginput tautan/path direktori arsip berkas desain pelanggan). |
| **Status Ketenagakerjaan** | Karyawan Kontrak (**PKWT** — Perjanjian Kerja Waktu Tertentu) berdasarkan regulasi PP No. 35 Tahun 2021. |

**Kebutuhan dan Ekspektasi Utama**:
* Akses langsung ke modul antrian pekerjaan dengan filter khusus status `Proses Desain`.
* Fitur pencatatan lokasi fisik/digital arsip berkas desain pelanggan (lokasi direktori server lokal) agar mudah dicari untuk cetak ulang (*re-order*).
* Kemudahan mengubah status antrian pekerjaan dari `Proses Desain` ke status `Produksi`.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Pengguna entry data spesifik modul antrian dan arsip.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Tinggi (4)**. Mempercepat proses pengerjaan desain dan menghilangkan kekacauan pelacakan file pelanggan.

**Fase Keterlibatan Maksimal**:
* Testing (Sebagai Aktor UAT), Deployment (Target Pelatihan), dan Operational.

---

### 3.6. [STK-006] Calon Staf Produksi Cetak

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-006 |
| **Nama / Jabatan** | Calon Staf Produksi Cetak |
| **Organisasi / Afiliasi** | Toko Percetakan AbuCom (Fase Operasional) |
| **Kategori** | Internal |
| **Tipe** | Individu |
| **Peran dalam Proyek** | Pengguna Operasional (End-User) |
| **Kontak / Identifikasi** | `[DIISI OLEH PEMILIK USAHA setelah rekrutmen — Format: "Nama Lengkap | No. WhatsApp Aktif (contoh: +6281234567890)"]` |
| **Hak Akses RBAC** | `Role: produksi_cetak` (Akses produksi: melihat antrian dengan status `Produksi`, memperbarui status menjadi `Selesai`, menginput pemakaian bahan baku riil desimal, dan mencatat limbah produksi/waste). |
| **Status Ketenagakerjaan** | Karyawan Kontrak (**PKWT** — Perjanjian Kerja Waktu Tertentu) berdasarkan regulasi PP No. 35 Tahun 2021. |

**Kebutuhan dan Ekspektasi Utama**:
* Akses ke modul antrian status `Produksi` untuk melihat daftar pekerjaan cetak fisik yang siap diproses.
* Fitur pencatatan pemakaian bahan baku riil secara desimal (panjang x lebar) dan pencatatan limbah produksi (*waste management*) jika terjadi kesalahan cetak/bahan rusak.
* Kemudahan pembaruan status antrian ke status `Selesai` setelah proses finishing produk.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Pengguna entry data pemakaian stok riil.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Tinggi (4)**. Akurasi pemotongan stok bahan baku di gudang sangat bergantung pada kedisiplinan staf produksi melakukan input dimensi pemakaian riil dan data limbah cetak.

**Fase Keterlibatan Maksimal**:
* Testing (Sebagai Aktor UAT), Deployment (Target Pelatihan), dan Operational.

---

### 3.7. [STK-007] Calon Staf Fotocopy & Print Dokumen

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-007 |
| **Nama / Jabatan** | Calon Staf Fotocopy & Print Dokumen |
| **Organisasi / Afiliasi** | Toko Percetakan AbuCom (Fase Operasional) |
| **Kategori** | Internal |
| **Tipe** | Individu |
| **Peran dalam Proyek** | Pengguna Operasional (End-User) |
| **Kontak / Identifikasi** | `[DIISI OLEH PEMILIK USAHA setelah rekrutmen — Format: "Nama Lengkap | No. WhatsApp Aktif (contoh: +6281234567890)"]` |
| **Hak Akses RBAC** | `Role: fotocopy_print` (Akses transaksional retail: mencatat penjualan fotokopi per lembar dan print dokumen cepat, serta membantu transaksi kasir/pramuniaga bila ditugaskan secara *cross-functional*). |
| **Status Ketenagakerjaan** | Karyawan Kontrak (**PKWT** — Perjanjian Kerja Waktu Tertentu) berdasarkan regulasi PP No. 35 Tahun 2021. |

**Kebutuhan dan Ekspektasi Utama**:
* Antarmuka cepat untuk mencatat transaksi ritel cepat (fotokopi per lembar dan cetak dokumen hitam-putih/warna).
* Integrasi antarmuka yang sederhana agar dapat dialihkan membantu mencatat pemakaian bahan di divisi produksi cetak jika antrian padat (*cross-functional*).

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Pengguna operasional harian pendukung.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Tinggi (4)**. Memudahkan pencatatan omzet harian dari transaksi retail cepat tanpa repot menulis di buku nota fisik.

**Fase Keterlibatan Maksimal**:
* Testing (Sebagai Aktor UAT), Deployment (Target Pelatihan), dan Operational.

---

### 3.8. [STK-008] Calon Staf Gudang

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-008 |
| **Nama / Jabatan** | Calon Staf Gudang |
| **Organisasi / Afiliasi** | Toko Percetakan AbuCom (Fase Operasional) |
| **Kategori** | Internal |
| **Tipe** | Individu |
| **Peran dalam Proyek** | Pengguna Operasional (End-User) |
| **Kontak / Identifikasi** | `[DIISI OLEH PEMILIK USAHA setelah rekrutmen — Format: "Nama Lengkap | No. WhatsApp Aktif (contoh: +6281234567890)"]` |
| **Hak Akses RBAC** | `Role: gudang` (Akses inventaris: mencatat mutasi barang masuk/keluar, mendaftarkan data supplier/vendor, menginput riwayat harga beli, mencatat utang pembelian barang, dan melaksanakan stock opname fisik). |
| **Status Ketenagakerjaan** | Karyawan Kontrak (**PKWT** — Perjanjian Kerja Waktu Tertentu) berdasarkan regulasi PP No. 35 Tahun 2021. |

**Kebutuhan dan Ekspektasi Utama**:
* Modul pencatatan data supplier, riwayat harga beli bahan baku dari supplier, dan pencatatan utang pembelian tempo.
* Menu fungsional pelaksanaan rekonsiliasi persediaan (*Stock Opname*) berkala untuk mencocokkan stok fisik vs aplikasi.
* Fitur pencatatan pengurangan stok otomatis atas pengambilan barang retail ATK untuk kebutuhan internal divisi produksi.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Keakuratan data gudang fisik vs database sistem dikelola oleh staf ini.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Tinggi (4)**. Meniadakan proses pencatatan stok kartu gudang manual berbasis kertas yang rawan hilang dan basah.

**Fase Keterlibatan Maksimal**:
* Testing (Sebagai Aktor UAT), Deployment (Input data awal & Pelatihan), dan Operational.

---

### 3.9. [STK-009] Gemini 3.1 Pro (High)

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-009 |
| **Nama / Jabatan** | Gemini 3.1 Pro (High) |
| **Organisasi / Afiliasi** | Tim Asisten AI Spesialis |
| **Kategori** | Internal |
| **Tipe** | Kelompok / Model AI |
| **Peran dalam Proyek** | Lead Architect & Heavy Logic Developer |
| **Kontak / Identifikasi** | Terintegrasi melalui API / Interface Google AI Studio |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime (Pengembang Kode)` |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan instruksi prompt yang terstruktur, parameter konteks proyek yang lengkap, dan batasan teknis yang didefinisikan dengan jelas.
* Membutuhkan standardisasi paradigma *Functional Programming* yang konsisten di seluruh modul logika bisnis Python.

**Potensi Pengaruh terhadap Proyek**:
* **Tinggi (3)**. Menentukan kualitas desain arsitektur modular sistem, perancangan algoritma perhitungan BOM desimal, dan logika penggajian cerdas. Kesalahan desain arsitektur akan menghambat skalabilitas multi-cabang.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Sedang (2)**. Tidak terpengaruh secara emosional atau finansial, namun performa pengkodeannya dinilai berdasarkan keberhasilan eksekusi arsitektur.

**Fase Keterlibatan Maksimal**:
* Planning, Requirements, Design, Implementation.

---

### 3.10. [STK-010] Gemini 3.1 Pro (Low)

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-010 |
| **Nama / Jabatan** | Gemini 3.1 Pro (Low) |
| **Organisasi / Afiliasi** | Tim Asisten AI Spesialis |
| **Kategori** | Internal |
| **Tipe** | Kelompok / Model AI |
| **Peran dalam Proyek** | Routine Coding & Documentation Specialist |
| **Kontak / Identifikasi** | Terintegrasi melalui API / Interface Google AI Studio |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime (Pengembang Kode)` |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan skema relasi database yang valid dan instruksi terstruktur untuk menghasilkan dokumen formal SDLC yang sinkron secara bertahap.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Kualitas dokumentasi formal (SRS, SDD, User Manual) bergantung pada ketelitian model ini.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Sedang (2)**. Output dokumen dievaluasi kualitasnya berdasarkan standar kelengkapan industri.

**Fase Keterlibatan Maksimal**:
* Planning, Requirements, Design, Deployment (Dokumentasi).

---

### 3.11. [STK-011] Gemini 3 Flash

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-011 |
| **Nama / Jabatan** | Gemini 3 Flash |
| **Organisasi / Afiliasi** | Tim Asisten AI Spesialis |
| **Kategori** | Internal |
| **Tipe** | Kelompok / Model AI |
| **Peran dalam Proyek** | Fast Reviewer & Debugger |
| **Kontak / Identifikasi** | Terintegrasi melalui API / Interface Google AI Studio |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime (Pengembang Kode)` |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan cuplikan kode spesifik yang bermasalah (*buggy snippet*) disertai pesan error runtime untuk analisis cepat.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Mempercepat siklus perbaikan bug ringan selama masa testing fungsional 2 mingguan.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Sedang (2)**. Memastikan kecepatan respons review kode tetap relevan untuk latensi waktu rendah.

**Fase Keterlibatan Maksimal**:
* Implementation, Testing.

---

### 3.12. [STK-012] Claude Sonnet 4.6 (Thinking)

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-012 |
| **Nama / Jabatan** | Claude Sonnet 4.6 (Thinking) |
| **Organisasi / Afiliasi** | Tim Asisten AI Spesialis |
| **Kategori** | Internal |
| **Tipe** | Kelompok / Model AI |
| **Peran dalam Proyek** | Deep Coder & Refactoring Specialist |
| **Kontak / Identifikasi** | Terintegrasi melalui API / Interface Anthropic Console |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime (Pengembang Kode)` |

**Kebutuhan dan Ekspektasi Utama**:
* Ketersediaan struktur direktori proyek yang jelas, aturan penulisan kode imutabel, dan data input representatif untuk kalkulasi mendalam terkait logika CLI fungsional.

**Potensi Pengaruh terhadap Proyek**:
* **Tinggi (3)**. Menghasilkan kode fungsional Python tingkat tinggi yang murni (*pure functions*), optimasi kode antarmuka CLI (`rich` dan `tabulate`), dan restrukturisasi kode agar efisien.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Sedang (2)**. Keakuratan dan kebersihan kode program diuji menggunakan pengujian unit testing dan analisis statis.

**Fase Keterlibatan Maksimal**:
* Design, Implementation, Testing.

---

### 3.13. [STK-013] Claude Opus 4.6 (Thinking)

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-013 |
| **Nama / Jabatan** | Claude Opus 4.6 (Thinking) |
| **Organisasi / Afiliasi** | Tim Asisten AI Spesialis |
| **Kategori** | Internal |
| **Tipe** | Kelompok / Model AI |
| **Peran dalam Proyek** | System Strategist & Security Lead |
| **Kontak / Identifikasi** | Terintegrasi melalui API / Interface Anthropic Console |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime (Pengembang Kode)` |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan kejelasan regulasi eksternal (UU PDP No. 27 Tahun 2022) dan pemetaan aset sensitif yang harus dilindungi di database MySQL.

**Potensi Pengaruh terhadap Proyek**:
* **Tinggi (3)**. Merancang strategi enkripsi kata sandi (bcrypt cost factor 12), penanganan token otentikasi sesi (JWT 8 jam), desain skema tabel log Audit Trail, perlindungan SQL Injection, dan skema backup file AES-256.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Sedang (2)**. Sistem tata kelola keamanan diuji secara internal untuk menjamin tidak ada celah manipulasi.

**Fase Keterlibatan Maksimal**:
* Design, Implementation, Testing (Security Audit).

---

### 3.14. [STK-014] GPT-OSS 120B (Medium)

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-014 |
| **Nama / Jabatan** | GPT-OSS 120B (Medium) |
| **Organisasi / Afiliasi** | Tim Asisten AI Spesialis |
| **Kategori** | Internal |
| **Tipe** | Kelompok / Model AI |
| **Peran dalam Proyek** | Boilerplate Generator & Dummy Data Specialist |
| **Kontak / Identifikasi** | Terintegrasi melalui Model Open Source yang di-host lokal/server |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime (Pengembang Kode)` |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan skema relasi tabel (ERD) dan tipe data kolom MySQL yang telah disetujui Lead Architect.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Mempercepat setup awal basis data melalui penyediaan template file `schema.sql` dan `seed.sql` inisialisasi yang terformat rapi.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Sedang (2)**. Efisiensi skrip seed data awal dinilai dari kecepatan pemuatan data pengujian dummy ke database.

**Fase Keterlibatan Maksimal**:
* Design, Implementation (Setup Database Awal).

---

### 3.15. [STK-015] Pelanggan AbuCom

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-015 |
| **Nama / Jabatan** | Pelanggan AbuCom |
| **Organisasi / Afiliasi** | Masyarakat Umum / Pelanggan Bisnis |
| **Kategori** | Eksternal |
| **Tipe** | Kelompok / Institusi |
| **Peran dalam Proyek** | Penerima Manfaat Layanan (Beneficiary) |
| **Kontak / Identifikasi** | `[DIISI OLEH SISTEM — Tersimpan otomatis dalam database CRM setelah transaksi awal]` |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime` (Tidak memiliki hak akses terminal CLI langsung. Data transaksi dan arsip desain diakses dan dikelola oleh staf operasional yang berwenang). |

**Kebutuhan dan Ekspektasi Utama**:
* Membutuhkan pelayanan yang cepat, estimasi penyelesaian pengerjaan pesanan yang akurat (melalui Job Tracking), dan kualitas produk cetak yang konsisten.
* Menginginkan data pribadi mereka (nama dan nomor WhatsApp) aman dari penyalahgunaan atau kebocoran pihak luar sesuai regulasi UU PDP No. 27 Tahun 2022.
* Kemudahan melakukan cetak ulang (*re-order*) pesanan kustom masa lalu dengan cepat berkat manajemen arsip desain yang tertib.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (1)**. Tidak terlibat langsung memengaruhi kode arsitektur sistem.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Tinggi (3)**. Mendapatkan pengalaman layanan yang lebih profesional, waktu tunggu yang lebih pendek, antrian yang adil, serta keterjaminan privasi.

**Fase Keterlibatan Maksimal**:
* Operational (Pasca Go-Live).

---

### 3.16. [STK-016] Vendor & Supplier Bahan Baku / ATK

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-016 |
| **Nama / Jabatan** | Vendor & Supplier Bahan Baku / ATK |
| **Organisasi / Afiliasi** | Mitra Pemasok Bahan Baku Percetakan / ATK |
| **Kategori** | Eksternal |
| **Tipe** | Kelompok / Institusi |
| **Peran dalam Proyek** | Penyedia Pasokan Bahan Baku dan ATK |
| **Kontak / Identifikasi** | `[DIISI OLEH STAF GUDANG — Format: "Nama Vendor | Person in Charge (PIC) | No. WhatsApp Aktif"]` |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime` (Riwayat pemesanan, harga beli, dan pelunasan utang usaha diinput oleh Staf Gudang). |

**Kebutuhan dan Ekspektasi Utama**:
* Mengharapkan pembayaran utang pembelian tepat waktu sesuai kesepakatan tenor tempo.
* Membutuhkan pesanan pengadaan bahan yang terjadwal (difasilitasi oleh fitur notifikasi peringatan stok menipis/prediksi *re-order*) dan kuantitas pembelian yang stabil.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (2)**. Keterlambatan suplai bahan baku dari supplier akan menghambat kelancaran proses produksi cetak toko, namun tidak mempengaruhi arsitektur perangkat lunak.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Tinggi (3)**. Sistem inventaris AbuCom merapikan riwayat transaksi pembelian (termasuk modul price tracking) dan riwayat utang usaha yang transparan.

**Fase Keterlibatan Maksimal**:
* Operational (Pasca Go-Live).

---

### 3.17. [STK-017] Bank BRI (Kreditur Berbunga)

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-017 |
| **Nama / Jabatan** | Bank BRI |
| **Organisasi / Afiliasi** | PT Bank Rakyat Indonesia (Persero) Tbk (BUMN) |
| **Kategori** | Eksternal |
| **Tipe** | Institusi |
| **Peran dalam Proyek** | Kreditur Modal Berbunga (Institusi) |
| **Kontak / Identifikasi** | `Contoh: Kontrak KUR Mikro BRI No. 0183-XXXX-XXXX | Tenor: 24 Bulan | CS: Bpk. Andi (BRI Unit Setempat)` *(Nilai riil diisi oleh Pemilik ke dalam modul administrasi)* |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime` (Akses dibatasi penuh secara privat. Laporan cicilan dibukukan oleh Pemilik). |
| **Konteks Regulasi** | Lembaga keuangan negara pemberi Kredit Usaha Rakyat (KUR) mikro berbunga flat dengan agunan legalitas usaha NIB (Nomor Induk Berusaha). |

**Kebutuhan dan Ekspektasi Utama**:
* Menuntut pembayaran cicilan setoran bulanan pokok dan bunga secara penuh dan tepat waktu sebelum tanggal jatuh tempo yang disepakati (dibantu dengan fitur notifikasi *Alert Jatuh Tempo* di CLI).
* Mengharapkan kepatuhan finansial penuh terhadap jadwal tenor yang telah ditandatangani.

**Potensi Pengaruh terhadap Proyek**:
* **Tinggi (4)**. Kegagalan setoran bulanan akibat masalah likuiditas kas operasional dapat menyebabkan denda hukum, penyitaan jaminan aset fisik usaha (printer/PC), atau pemblokiran skor kredit modal usaha.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Rendah (2)**. Sistem manajemen terpadu AbuCom menjamin pelacakan alokasi anggaran operasional toko yang ketat untuk memastikan kewajiban setoran bank bulanan selalu disiapkan.

**Fase Keterlibatan Maksimal**:
* Seluruh durasi proyek (Sebagai penyedia likuiditas finansial eksternal).

---

### 3.18. [STK-018] Bank Mandiri (Kreditur Berbunga)

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-018 |
| **Nama / Jabatan** | Bank Mandiri |
| **Organisasi / Afiliasi** | PT Bank Mandiri (Persero) Tbk (BUMN) |
| **Kategori** | Eksternal |
| **Tipe** | Institusi |
| **Peran dalam Proyek** | Kreditur Modal Berbunga (Institusi) |
| **Kontak / Identifikasi** | `Contoh: KUM Mandiri No. 9921-XXXX-XXXX | Tenor: 36 Bulan | CS: Ibu Rina (Mandiri Cabang Pembantu)` *(Nilai riil diisi oleh Pemilik ke dalam modul administrasi)* |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime` (Akses dibatasi penuh secara privat. Laporan cicilan dibukukan oleh Pemilik). |
| **Konteks Regulasi** | Lembaga perbankan komersial BUMN penyedia pinjaman komersial dengan tenor tetap dan ketentuan denda keterlambatan bulanan yang rigid. |

**Kebutuhan dan Ekspektasi Utama**:
* Menuntut pembayaran cicilan setoran bulanan pokok dan bunga tepat waktu sebelum tanggal jatuh tempo (terlacak oleh modul administrasi utang).
* Mengharapkan operasional toko berjalan stabil agar likuiditas peminjam tetap terjaga.

**Potensi Pengaruh terhadap Proyek**:
* **Tinggi (4)**. Seperti perbankan komersial lainnya, keterlambatan pembayaran dapat mengganggu operasional melalui intervensi penagihan atau denda yang membengkak.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Rendah (2)**. Aplikasi menjamin pengelolaan arus kas harian (*cash flow*) terpantau presisi setiap detik, menurunkan probabilitas kredit macet (NPL).

**Fase Keterlibatan Maksimal**:
* Seluruh durasi proyek (Sebagai penyedia likuiditas finansial eksternal).

---

### 3.19. [STK-019] Kerabat & Keluarga (Pemberi Pinjaman Tanpa Bunga)

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-019 |
| **Nama / Jabatan** | Sahabat, Teman, Keluarga, Orang Tua |
| **Organisasi / Afiliasi** | Kerabat Dekat Pemilik Usaha |
| **Kategori** | Eksternal |
| **Tipe** | Individu / Kelompok |
| **Peran dalam Proyek** | Pemberi Pinjaman Tanpa Bunga |
| **Kontak / Identifikasi** | `[DIISI OLEH PEMILIK USAHA secara privat — Format: "Hubungan (Misal: Orang Tua) | Nama Lengkap | No. WhatsApp"]` |
| **Hak Akses RBAC** | `Akses Sistem: Tidak Ada Akses Runtime` (Tidak memiliki akses login CLI. Riwayat penarikan dana diinput mandiri oleh Pemilik dalam modul pinjaman keluarga). |
| **Konteks Budaya** | Hubungan pinjaman informal yang berlandaskan kearifan lokal gotong royong dan azas kekeluargaan (*social contract*), bebas bunga finansial namun dibebani kewajiban moral transparansi penuh. |

**Kebutuhan dan Ekspektasi Utama**:
* Mengharapkan transparansi mutlak atas posisi sisa saldo pinjaman mereka yang dititipkan untuk modal usaha.
* Menginginkan fleksibilitas penarikan dana titipan mereka kapan saja secara mendadak (sebagian, total, maupun permanen) saat memiliki keperluan darurat (*force majeure* keluarga).

**Potensi Pengaruh terhadap Proyek**:
* **Tinggi (4)**. Sifat penarikan dana yang tidak terprediksi berpotensi sangat tinggi merusak likuiditas arus kas operasional toko atau menghentikan alokasi proyek jika dana Cadangan Darurat Rp 4.500.000 tidak dijaga atau digunakan untuk hal lain.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Tinggi (3)**. Keberadaan modul administrasi pinjaman fleksibel di aplikasi memberikan mereka kepastian matematis terkait jumlah utang piutang, menghindari friksi sosial, dan menjaga keharmonisan relasi personal.

**Fase Keterlibatan Maksimal**:
* Seluruh durasi proyek (Secara pasif sebagai pengaman modal).

---

## 4. Klasifikasi Stakeholder

Untuk menyusun strategi pengelolaan yang efektif, seluruh stakeholder diklasifikasikan berdasarkan kategori keterlibatan, pengaruh terhadap jalannya proyek (*power/influence*), dan tingkat kepentingan serta dampak (*interest/impact*) terhadap hasil akhir proyek.

### 4.1. Berdasarkan Kategori Keterlibatan

| Kategori | ID Stakeholder |
|---|---|
| **Internal — Sponsor & Pengguna Utama** | STK-001 |
| **Internal — End-User Operasional** | STK-002, STK-003, STK-004, STK-005, STK-006, STK-007, STK-008 |
| **Internal — Tim Pengembang AI** | STK-009, STK-010, STK-011, STK-012, STK-013, STK-014 |
| **Eksternal — Beneficiary (Pelanggan)** | STK-015 |
| **Eksternal — Supply Chain (Supplier)** | STK-016 |
| **Eksternal — Financial (Kreditur)** | STK-017, STK-018, STK-019 |

---

### 4.2. Matriks Power/Interest Grid (Pengaruh vs Kepentingan)

Klasifikasi didasarkan pada empat kuadran standar industri PMBOK:
1. **Manage Closely (Kuadran A - High Power / High Interest)**: Fokus utama pengelolaan. Stakeholder yang menentukan arah proyek.
2. **Keep Satisfied (Kuadran B - High Power / Low Interest)**: Harus dijaga kepuasannya agar tidak menghambat jalannya proyek.
3. **Keep Informed (Kuadran C - Low Power / High Interest)**: Perlu diberi informasi secara berkala agar tetap mendukung adopsi sistem.
4. **Monitor (Kuadran D - Low Power / Low Interest)**: Dipantau dengan upaya minimal untuk melihat fluktuasi sikap.

| ID | Stakeholder | Power (1-5) | Interest (1-5) | Kuadran | Strategi Tata Kelola |
|---|---|:---:|:---:|---|---|
| **STK-001** | Pemilik Usaha AbuCom | 5 | 5 | Kuadran A | **Manage Closely** — Pembuat keputusan utama, integrator kode, pengendali anggaran. |
| **STK-002** | Staf Kepala Percetakan | 2 | 4 | Kuadran C | **Keep Informed** — Koordinasikan pelacakan antrian, berikan panduan. |
| **STK-003** | Staf Pramuniaga | 2 | 4 | Kuadran C | **Keep Informed** — Latih input transaksi cepat & CRM secara tepat. |
| **STK-004** | Staf Kasir | 2 | 4 | Kuadran C | **Keep Informed** — Pastikan pemahaman alur DP, pelunasan, & rekonsiliasi. |
| **STK-005** | Staf Desainer | 2 | 4 | Kuadran C | **Keep Informed** — Sosialisasikan pencatatan path arsip berkas desain. |
| **STK-006** | Staf Produksi Cetak | 2 | 4 | Kuadran C | **Keep Informed** — Tekankan pentingnya input pemakaian bahan riil & limbah. |
| **STK-007** | Staf Fotocopy & Print | 2 | 4 | Kuadran C | **Keep Informed** — Latih pencatatan transaksi ritel cepat & cross-functional. |
| **STK-008** | Staf Gudang | 2 | 4 | Kuadran C | **Keep Informed** — Latih skema input supplier, stock opname & utang. |
| **STK-009** | Gemini 3.1 Pro (High) | 3 | 2 | Kuadran D | **Monitor** — Berikan prompt instruksi logika arsitektur & BOM yang jelas. |
| **STK-010** | Gemini 3.1 Pro (Low) | 2 | 2 | Kuadran D | **Monitor** — Arahkan penulisan berkas dokumen formal agar komprehensif. |
| **STK-011** | Gemini 3 Flash | 2 | 2 | Kuadran D | **Monitor** — Gunakan untuk review cepat kesalahan sintaksis harian. |
| **STK-012** | Claude Sonnet 4.6 | 3 | 2 | Kuadran D | **Monitor** — Tugaskan spesifik penulisan modul FP Python tanpa error. |
| **STK-013** | Claude Opus 4.6 | 3 | 2 | Kuadran D | **Monitor** — Fokuskan pada audit keamanan, JWT & Audit Trail. |
| **STK-014** | GPT-OSS 120B | 2 | 2 | Kuadran D | **Monitor** — Gunakan untuk iterasi skrip setup database. |
| **STK-015** | Pelanggan AbuCom | 1 | 3 | Kuadran C | **Keep Informed** — Pastikan komunikasi kesiapan produk sampai ke WA. |
| **STK-016** | Vendor & Supplier | 2 | 3 | Kuadran C | **Keep Informed** — Jaga pemesanan rutin & pelunasan utang sesuai tempo. |
| **STK-017** | Bank BRI | 4 | 2 | Kuadran B | **Keep Satisfied** — Jamin kelancaran cicilan modal bulanan tepat waktu. |
| **STK-018** | Bank Mandiri | 4 | 2 | Kuadran B | **Keep Satisfied** — Jamin kelancaran cicilan modal bulanan tepat waktu. |
| **STK-019** | Kerabat & Keluarga | 4 | 3 | Kuadran B | **Keep Satisfied** — Berikan transparansi saldo & pisahkan dana cadangan. |

---

### 4.3. Matriks Pengaruh/Dampak (Influence/Impact Matrix)

Matriks ini menganalisis tingkat pengaruh pemangku kepentingan terhadap keputusan arah proyek disandingkan dengan besarnya dampak hasil proyek terhadap aktivitas mereka sehari-hari. Evaluasi ini diselaraskan (1:1) dengan parameter Power dan Interest untuk menjamin konsistensi.

| ID | Stakeholder | Pengaruh terhadap Proyek (1-5) | Dampak Proyek terhadap Stakeholder (1-5) | Prioritas Pengelolaan |
|---|---|:---:|:---:|---|
| **STK-001** | Pemilik Usaha AbuCom | 5 | 5 | **Prioritas 1 (Kritis)** |
| **STK-002** | Staf Kepala Percetakan | 2 | 4 | **Prioritas 2 (Tinggi)** |
| **STK-003** | Staf Pramuniaga | 2 | 4 | **Prioritas 2 (Tinggi)** |
| **STK-004** | Staf Kasir | 2 | 4 | **Prioritas 2 (Tinggi)** |
| **STK-005** | Staf Desainer | 2 | 4 | **Prioritas 2 (Tinggi)** |
| **STK-006** | Staf Produksi Cetak | 2 | 4 | **Prioritas 2 (Tinggi)** |
| **STK-007** | Staf Fotocopy & Print | 2 | 4 | **Prioritas 2 (Tinggi)** |
| **STK-008** | Staf Gudang | 2 | 4 | **Prioritas 2 (Tinggi)** |
| **STK-009** | Gemini 3.1 Pro (High) | 3 | 2 | **Prioritas 3 (Sedang)** |
| **STK-010** | Gemini 3.1 Pro (Low) | 2 | 2 | **Prioritas 3 (Sedang)** |
| **STK-011** | Gemini 3 Flash | 2 | 2 | **Prioritas 3 (Sedang)** |
| **STK-012** | Claude Sonnet 4.6 | 3 | 2 | **Prioritas 3 (Sedang)** |
| **STK-013** | Claude Opus 4.6 | 3 | 2 | **Prioritas 3 (Sedang)** |
| **STK-014** | GPT-OSS 120B | 2 | 2 | **Prioritas 3 (Sedang)** |
| **STK-015** | Pelanggan AbuCom | 1 | 3 | **Prioritas 3 (Sedang)** |
| **STK-016** | Vendor & Supplier | 2 | 3 | **Prioritas 3 (Sedang)** |
| **STK-017** | Bank BRI | 4 | 2 | **Prioritas 2 (Tinggi)** |
| **STK-018** | Bank Mandiri | 4 | 2 | **Prioritas 2 (Tinggi)** |
| **STK-019** | Kerabat & Keluarga | 4 | 3 | **Prioritas 2 (Tinggi)** |

---

## 5. Analisis Sikap dan Tingkat Keterlibatan Stakeholder

Bagian ini mengevaluasi sikap pemangku kepentingan saat ini disandingkan dengan tingkat keterlibatan yang diinginkan untuk menjamin keberhasilan implementasi sistem.

### 5.1. Stakeholder Engagement Assessment Matrix

Keterangan tingkat keterlibatan:
* **Unaware**: Tidak menyadari adanya proyek dan potensi dampaknya.
* **Resistant**: Menyadari proyek namun menolak perubahan operasional.
* **Neutral**: Mengetahui proyek, bersikap pasif, tidak mendukung maupun menolak.
* **Supportive**: Mengetahui proyek dan mendukung jalannya perubahan sistem.
* **Leading**: Mengetahui proyek secara aktif memimpin perubahan tata kelola.

Penanda: `C` = Kondisi Saat Ini (*Current*), `D` = Kondisi yang Diharapkan (*Desired*).

| ID Stakeholder | Unaware | Resistant | Neutral | Supportive | Leading |
|---|:---:|:---:|:---:|:---:|:---:|
| **STK-001** | | | | | **C** , **D** |
| **STK-002** | **C** | | | **D** | |
| **STK-003** | **C** | | | **D** | |
| **STK-004** | **C** | | | **D** | |
| **STK-005** | **C** | | | **D** | |
| **STK-006** | **C** | | | **D** | |
| **STK-007** | **C** | | | **D** | |
| **STK-008** | **C** | | | **D** | |
| **STK-009** | | | | **C** | **D** |
| **STK-010** | | | | **C** | **D** |
| **STK-011** | | | | **C** | **D** |
| **STK-012** | | | | **C** | **D** |
| **STK-013** | | | | **C** | **D** |
| **STK-014** | | | | **C** | **D** |
| **STK-015** | **C** | | **D** | | |
| **STK-016** | **C** | | **D** | | |
| **STK-017** | | | **C** , **D** | | |
| **STK-018** | | | **C** , **D** | | |
| **STK-019** | | | **C** | **D** | |

---

### 5.2. Analisis Gap Keterlibatan

Berdasarkan matriks di atas, terdapat beberapa celah keterlibatan (*gap*) yang memerlukan perhatian tata kelola kritis:

1. **Calon Staf Operasional (STK-002 s.d. STK-008)**:
   * **Gap**: `Unaware` (Saat Ini) $\rightarrow$ `Supportive` (Diharapkan).
   * **Analisis**: Karyawan saat ini belum direkrut secara fisik, sehingga statusnya adalah `Unaware`. Risiko transisi terletak pada potensi kebingungan staf baru menghadapi antarmuka CLI yang tidak ramah visual layaknya aplikasi GUI.
   * **Tindakan**: Mengadakan program rekrutmen terencana pada Bulan 9-10, dilanjutkan dengan pelatihan intensif selama 3 hari menggunakan buku manual CLI interaktif sebelum go-live, serta menetapkan mereka sebagai aktor UAT utama untuk membiasakan operasional terminal teks.

2. **Kerabat & Keluarga (STK-019)**:
   * **Gap**: `Neutral` (Saat Ini) $\rightarrow$ `Supportive` (Diharapkan).
   * **Analisis**: Kerabat pemberi pinjaman modal tanpa bunga saat ini bersikap netral dan cenderung melihat dari aspek hubungan kekeluargaan yang cair. Namun, ketidakpastian kebutuhan dana mendadak mereka berpotensi memicu ditariknya kas modal proyek secara tiba-tiba.
   * **Tindakan**: Memberikan transparansi pencatatan saldo utang piutang di sistem administrasi CLI dan rutin menyajikan gambaran performa omzet toko agar mereka merasa modalnya dikelola secara profesional.

3. **Tim Pengembang AI (STK-009 s.d. STK-014)**:
   * **Gap**: `Supportive` (Saat Ini) $\rightarrow$ `Leading` (Diharapkan).
   * **Analisis**: Tim AI saat ini mendukung pembuatan kode program secara pasif (hanya membalas prompt). Untuk menjamin keutuhan arsitektur *Functional Programming*, Tim AI harus memimpin (*Leading*) dalam mengusulkan best-practice kode, inovasi modul (seperti PPOB, Dashboard harian), serta validasi keamanan.
   * **Tindakan**: Junior Programmer wajib memformulasikan perintah prompt secara spesifik yang memberikan keleluasaan inisiatif (mandat inovasi) kepada model AI untuk meninjau dan merestrukturisasi modul aplikasi.

---

## 6. Kebutuhan dan Ekspektasi Stakeholder

### 6.1. Rincian Kebutuhan & Ekspektasi Detail

Tabel di bawah mengkonsolidasikan seluruh kebutuhan fungsional tingkat tinggi dan kriteria kepuasan masing-masing stakeholder sebagai acuan perancangan *Use Case* pada penyusunan dokumen SRS.

| ID | Stakeholder | Kebutuhan Utama (FR High-level) | Ekspektasi terhadap Proyek | Kriteria Kepuasan |
|---|---|---|---|---|
| **STK-001** | Pemilik Usaha | Laporan Laba/Rugi otomatis, BOM desimal stok, RBAC, & Audit Trail. | Mengurangi beban operasional 5 divisi sendirian, mitigasi *burnout*. | 100% laporan keuangan bebas Excel, selisih stok gudang vs sistem <1.0%. |
| **STK-002** | Staf Kepala Percetakan | Navigasi CLI teratur, visual antrian jelas, menu pemantauan stok & absensi. | Memudahkan koordinasi toko tanpa merekap manual laporan tim di akhir hari. | Antrian transisi lancar, tidak ada pesanan kustom yang terlewat pengerjaannya. |
| **STK-003** | Staf Pramuniaga | Entry transaksi ritel cepat, pencarian harga 3 tingkat, input data CRM WhatsApp. | Proses pencatatan pesanan di konter depan menjadi sangat singkat. | Pelanggan terlayani instan tanpa antri panjang di konter kasir. |
| **STK-004** | Staf Kasir | Modul DP/Pelunasan, pencarian Agen termurah e-wallet, rekonsiliasi uang kas fisik laci. | Keamanan data uang di laci kasir terjaga dengan pencatatan mutasi otomatis. | Tidak terjadi perselisihan nominal uang fisik vs nilai di sistem (selisih nol). |
| **STK-005** | Staf Desainer | Filter status `Proses Desain`, kolom input path direktori server lokal arsip pelanggan. | Pencarian arsip desain pelanggan lama sangat cepat untuk keperluan cetak ulang. | File tersimpan rapi berdasarkan ID Pesanan, tidak tercecer di PC desainer. |
| **STK-006** | Staf Produksi Cetak | Filter status `Produksi`, field input dimensi panjang/lebar bahan riil & form limbah (*waste*). | Pemotongan bahan baku di sistem merepresentasikan dimensi fisik sisa bahan secara presisi. | Sisa stok barang meteran/gulungan di gudang sinkron sempurna dengan sistem. |
| **STK-007** | Staf Fotocopy & Print | Pencatatan transaksi retail sangat cepat (hitam/warna), UI minimalis tanpa navigasi panjang. | Kecepatan entry order layanan dasar (*fast moving*) tidak menghambat pekerjaan. | Perekapan jumlah cetakan fotokopi harian tidak memerlukan tulisan nota fisik. |
| **STK-008** | Staf Gudang | Menu formulir data supplier, menu Stock Opname, input utang pembelian barang modal. | Administrasi masuk-keluar barang terpantau otomatis tanpa kartu stok kertas gantung. | Modul Stock Opname dapat menyelesaikan audit fisik harian dalam hitungan menit. |
| **STK-009** | Gemini 3.1 Pro (High) | Konteks proyek utuh, parameter BOM, batas mutlak *Functional Programming*. | Menghasilkan struktur arsitektur dasar modul yang andal untuk diteruskan model lain. | Arsitektur FP awal diuji kokoh, bebas kebocoran memori, dan siap dikembangkan. |
| **STK-010** | Gemini 3.1 Pro (Low) | Skema relasi database terfinalisasi, referensi dari dokumen perencanaan terdahulu. | Dokumen SDLC tersusun runtut, lengkap, dan memenuhi standar industri. | Dokumen (SRS, SDD) lulus tinjauan PMBOK dan bebas dari celah teknis. |
| **STK-011** | Gemini 3 Flash | Log error runtime spesifik, potongan kode yang bug (*buggy snippet*). | Evaluasi review cepat dan ringkas atas perbaikan sintaksis harian. | *Bug* ringan berhasil diperbaiki secara presisi dalam siklus sprint iteratif yang sama. |
| **STK-012** | Claude Sonnet 4.6 | Standardisasi FP Python yang disepakati (tuple/immutable datastructure). | Penulisan *pure functions* berskala besar tanpa *side-effects* yang tersembunyi. | Pengujian tingkat unit (*Unit Testing*) fungsi kalkulasi desimal lolos 100%. |
| **STK-013** | Claude Opus 4.6 | Kebijakan spesifik batasan *roles* menu CLI, referensi mandat perlindungan data pribadi (UU PDP). | Rancangan sistem tahan serangan lokal dan mencegah ekses akses data sensitif. | Enkripsi bcrypt, token JWT stateless, dan Audit Trail bebas celah *bypass*. |
| **STK-014** | GPT-OSS 120B | Rancangan ERD MySQL final, tabel terstruktur, definisi FK (Foreign Key) jelas. | Pembuatan skrip `schema.sql` (inisialisasi) dan `seed.sql` (data dummy awal). | Database dapat dibuat dari nol dengan data awal secara otomatis dan akurat. |
| **STK-015** | Pelanggan AbuCom | Kecepatan pelayanan cetak, arsip desain tidak hilang, privasi data (Nama/WA) terjaga. | Pesanan kustom diselesaikan sesuai janji waktu yang disepakati saat pemesanan (DP). | Tautan WA template notifikasi dikirim segera (akurat) saat pesanan selesai. |
| **STK-016** | Vendor & Supplier | Rekapitulasi jumlah order pembelian barang dan transparansi saldo utang/tempo. | Pemenuhan pembayaran tagihan pelunasan order pasokan dengan tepat waktu. | Siklus repeat-order toko ke vendor tidak terputus akibat utang yang tak terlacak. |
| **STK-017** | Bank BRI | Pelunasan tagihan cicilan pokok & bunga secara mutlak sebelum jatuh tempo setoran bulan. | Memastikan pemilik toko mengelola kewajiban KUR (Kredit Usaha Rakyat) secara tertib. | Cicilan berhasil di-autodebet dari rekening atau disetor tanpa hari keterlambatan. |
| **STK-018** | Bank Mandiri | Pelunasan tagihan cicilan komersial dengan kedisiplinan serupa sebelum batas tanggal tempo. | Menginginkan arus kas bisnis peminjam stabil untuk mencegah peningkatan skor risiko. | Notifikasi alarm (alert) CLI mencegah kelalaian transfer dana pada tanggal krusial. |
| **STK-019** | Kerabat & Keluarga | Modul laporan saldo utang piutang yang dikelola aman, riwayat pencatatan setiap penarikan uang. | Kepastian keamanan alokasi modal dan pemisahan rekening Kas Operasional vs Cadangan. | Transparansi mutlak yang merawat relasi kekerabatan positif dalam jangka panjang. |

---

### 6.2. Matriks Pemetaan Modul vs Stakeholder (Jembatan Kebutuhan)

Matriks ini memetakan hubungan antara 19 pemangku kepentingan dengan 9 modul utama yang dirancang pada fase awal, berfungsi sebagai jembatan analisis menuju penyusunan dokumen SRS:

*   **U (User)**: Stakeholder bertindak sebagai operator/pengguna langsung yang menginput atau memanipulasi data modul di terminal CLI.
*   **D (Impacted)**: Stakeholder tidak mengoperasikan modul secara langsung namun dipengaruhi oleh output, laporan (Audit), atau regulasi modul (termasuk AI yang mendesainnya).
*   **- (Not Involved)**: Stakeholder sama sekali tidak terlibat dalam pengoperasian atau dampak modul.

| ID | Stakeholder | M.1 | M.2 | M.3 | M.4 | M.5 | M.6 | M.7 | M.8 | M.9 |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **STK-001** | Pemilik Usaha AbuCom | **U** | **U** | **U** | **U** | **U** | **U** | **U** | **U** | **U** |
| **STK-002** | Staf Kepala Percetakan | **U** | **U** | **-** | **U** | **U** | **-** | **-** | **U** | **D** |
| **STK-003** | Staf Pramuniaga | **U** | **-** | **-** | **-** | **U** | **-** | **-** | **U** | **D** |
| **STK-004** | Staf Kasir | **U** | **-** | **U** | **-** | **U** | **-** | **-** | **U** | **D** |
| **STK-005** | Staf Desainer | **-** | **-** | **-** | **-** | **U** | **-** | **-** | **-** | **D** |
| **STK-006** | Staf Produksi Cetak | **-** | **U** | **-** | **-** | **U** | **-** | **-** | **U** | **D** |
| **STK-007** | Staf Fotocopy & Print | **U** | **-** | **-** | **-** | **U** | **-** | **-** | **U** | **D** |
| **STK-008** | Staf Gudang | **-** | **U** | **-** | **-** | **-** | **-** | **-** | **U** | **D** |
| **STK-009** | Gemini 3.1 Pro (High) | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** |
| **STK-010** | Gemini 3.1 Pro (Low) | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** |
| **STK-011** | Gemini 3 Flash | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** |
| **STK-012** | Claude Sonnet 4.6 | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** |
| **STK-013** | Claude Opus 4.6 | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** |
| **STK-014** | GPT-OSS 120B | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** | **D** |
| **STK-015** | Pelanggan AbuCom | **D** | **-** | **D** | **-** | **D** | **-** | **D** | **D** | **-** |
| **STK-016** | Vendor & Supplier | **-** | **D** | **-** | **-** | **-** | **-** | **-** | **-** | **-** |
| **STK-017** | Bank BRI | **-** | **-** | **-** | **-** | **-** | **D** | **-** | **-** | **-** |
| **STK-018** | Bank Mandiri | **-** | **-** | **-** | **-** | **-** | **D** | **-** | **-** | **-** |
| **STK-019** | Kerabat & Keluarga | **-** | **-** | **-** | **-** | **-** | **D** | **-** | **-** | **-** |

*Keterangan Modul (Berdasarkan Project Charter v1.1 dan Innovation Proposal v1.1):*
*   **M.1**: Modul Manajemen Transaksi & Kebijakan Harga
*   **M.2**: Modul Manajemen Inventaris, BOM & Stock Opname
*   **M.3**: Modul Keuangan Digital, PPOB, Jasa Keuangan & Service
*   **M.4**: Modul Manajemen SDM, Penggajian & Poin Karyawan
*   **M.5**: Modul Sistem Manajemen Antrian & Pelacakan Desain
*   **M.6**: Modul Administrasi Pinjaman, Aset, & Pengeluaran Rutin
*   **M.7**: Modul Keamanan, Audit Trail & Hak Akses (RBAC)
*   **M.8**: Modul Pembatalan, Retur & CRM
*   **M.9**: Modul Skalabilitas Multi-Cabang (*Multi-Branch Ready*)

---

## 7. Matriks RACI Stakeholder

Matriks RACI ini memperjelas akuntabilitas dan tanggung jawab untuk 10 aktivitas utama di seluruh siklus hidup proyek SDLC AbuCom. Setiap baris aktivitas memiliki minimal satu Penanggung Jawab (*Accountable*) tunggal dan setidaknya satu Pelaksana Utama (*Responsible*).

**Legenda RACI:**
* **R (Responsible)**: Pihak pelaksana yang mengerjakan tugas secara langsung, menulis kode, mendesain UI, atau menginput data.
* **A (Accountable)**: Pihak pemegang keputusan mutlak. Menyetujui dokumen atau menyetujui peluncuran sistem operasional harian.
* **C (Consulted)**: Pihak pakar yang wajib dimintai pendapat/konsultasi mengenai tata letak menu atau algoritma keamanan *sebelum* pelaksanaan selesai.
* **I (Informed)**: Pihak penerima laporan (pasif) atas status *progress* atau peluncuran fungsionalitas tertentu.

**Pemetaan Kolom:**
* **STK-001**: Pemilik Usaha (Berperan sebagai Manajer Proyek Internal dan Junior Programmer).
* **STK-002 s.d. 008**: Staf Karyawan Operasional.
* **STK-009 s.d. 014**: Tim Pengembang AI (LLM / Bot).
* **STK-015**: Pelanggan.
* **STK-016**: Supplier.
* **STK-017 s.d. 018**: Bank Kreditur.
* **STK-019**: Kerabat / Keluarga Peminjam Modal.

| Aktivitas / Tahapan SDLC | STK-001 | STK-002 s.d. 008 | STK-009 s.d. 014 | STK-015 | STK-016 | STK-017 s.d. 018 | STK-019 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1. Perencanaan & Project Charter** | **A / R** | I | R | I | I | I | I |
| **2. Penyusunan Stakeholder Register** | **A** | I | **R** | I | I | I | I |
| **3. Spesifikasi Kebutuhan (SRS)** | **A / R** | C | **R** | I | I | I | I |
| **4. Desain Arsitektur & DB (SDD)** | **A** | I | **R** | I | I | I | I |
| **5. Implementasi Kode Program** | **A / R** | I | **R** | I | I | I | I |
| **6. Pengujian Fungsional & UAT** | **A / R** | **R** | C | I | I | I | I |
| **7. Instalasi & Import Data CSV** | **A / R** | **R** | C | I | I | I | I |
| **8. Pelatihan Staf Operasional** | **A / R** | **R** | C | I | I | I | I |
| **9. Operasional & Rekonsiliasi Harian** | **A** | **R** | I | I | I | I | I |
| **10. Pengelolaan Administrasi Keuangan** | **A / R** | I | I | I | I | C | C / I |

---

## 8. Strategi Pengelolaan dan Komunikasi Stakeholder

### 8.1. Rencana Komunikasi per Stakeholder

Rencana taktis komunikasi ini bertujuan untuk mengatur penyampaian informasi yang selaras selama proyek dan memastikan tidak ada pesan operasional yang terlewat pasca peluncuran (go-live).

| ID | Stakeholder | Metode Komunikasi | Frekuensi | Penanggung Jawab | Informasi yang Dikomunikasikan |
|---|---|---|---|---|---|
| **STK-001** | Pemilik Usaha | Peninjauan berkas Markdown (MD) dokumen SDLC di direktori lokal, pengujian demo input/output program CLI di terminal Windows 11. | Harian / Tiap akhir iterasi modul | Pemilik Usaha (Mandiri) | Status penyelesaian per modul program FP Python, validasi efisiensi sintaksis, review latensi respons, dan konfirmasi keamanan RBAC. |
| **STK-002 s.d. STK-008** | Calon Staf Baru | Briefing kelompok besar tatap muka, simulasi langsung input terminal CLI di PC toko, penyerahan cetak buku saku *CLI User Manual*. | Harian (selama 3 hari masa UAT & training), dilanjutkan evaluasi rutin mingguan pasca go-live | Pemilik Usaha (Sebagai Kepala Atasan) | Skenario UAT antrian pekerjaan `Antri -> Produksi`, pengoperasian menu kasir (DP/Retur), dan aturan rekonsiliasi kas harian yang mengikat. |
| **STK-009 s.d. STK-014** | Tim Pengembang AI | Input baris perintah teks prompt terstruktur yang mengacu pada aturan *pure functions*, lengkap dengan tempelan (paste) blok error terminal. | Insidental (Ratusan kali selama fase iterasi coding dan debugging) | Pemilik Usaha (Sebagai Junior Programmer) | Spesifikasi arsitektur modular yang dimandatkan, permintaan skema ERD/BOM desimal, log error *Stack Overflow* (debugging), dan peninjauan keamanan. |
| **STK-015** | Pelanggan AbuCom | Pesan teks semi-otomatis melalui salin-tempel tautan template WhatsApp Web yang digenerate oleh sistem terminal. | Insidental (Seketika saat pembayaran DP selesai diterima atau pesanan cetak fisik siap diambil di konter) | Staf Kasir / Pramuniaga | Bukti penerimaan pembayaran nominal DP resmi dan/atau pemberitahuan status kesiapan produk kustom yang siap diserahkan. |
| **STK-016** | Vendor & Supplier | Komunikasi pesan WhatsApp personal dan penyampaian bukti mutasi pelunasan transfer bank. | Insidental (Saat sisa persediaan fisik terdeteksi menipis atau jatuh tempo utang usaha tiba) | Staf Gudang | Permintaan estimasi (*quotation*) fluktuasi harga bahan masuk, kuantitas dimensi pesanan (*purchase order*), dan konfirmasi pembayaran. |
| **STK-017 s.d. STK-018** | Bank Mandiri & Bank BRI | Transfer aplikasi perbankan digital *mobile banking* dari rekening operasional toko atau setoran tunai via teller bank. | Bulanan (Tepat sebelum peringatan H-3 jatuh tempo yang dihasilkan notifikasi modul aplikasi) | Pemilik Usaha | Penyetoran angsuran pokok cicilan kredit usaha dan pelunasan komponen bunga bulanan. |
| **STK-019** | Kerabat & Keluarga | Komunikasi tatap muka kasual, penyajian laporan tabel ringkas pencatatan saldo utang piutang (ditarik dari aplikasi). | Insidental (Hanya saat mereka melakukan penarikan mendadak sebagian dana titipan atau pengembalian modal) | Pemilik Usaha | Laporan kepastian keamanan saldo modal yang dititipkan (*Capital Safety*) secara santai, transparan, dan dapat dipertanggungjawabkan matematis. |

---

### 8.2. Strategi Mitigasi Resistensi

1. **Mitigasi Resistensi Staf Operasional Baru terhadap Visual CLI**:
   * **Potensi Hambatan**: Generasi staf muda saat ini terbiasa dengan aplikasi kasir (*Point of Sale*) visual di layar sentuh tablet/Android. Transisi ke layar hitam terminal (CMD/Powershell) yang sarat perintah teks berisiko tinggi memicu syok teknologi, menunda pelayanan, dan memicu penolakan diam-diam.
   * **Strategi Mitigasi**:
     * Merancang alur navigasi menu CLI berbasis nomor konsisten (tidak perlu menghafal perintah bash rumit) dan menyertakan visualisasi blok panel dengan pewarnaan terminal menggunakan pustaka Python `rich` (hijau untuk Sukses, merah untuk Error/DP Kurang).
     * Menyusun buku *CLI User Manual* ringkas (kurang dari 10 halaman) yang menonjolkan diagram pohon (*flowchart*) pemilihan menu.
     * Mengikat kedisiplinan staf lewat poin insentif penggajian otomatis (`Smart Payroll`), yang menghargai setiap pengetikan kode penyelesaian tugas teknis dalam antrian.

2. **Mitigasi Kepanikan Penarikan Dana Mendadak oleh Kerabat/Keluarga**:
   * **Potensi Hambatan**: Sifat pinjaman dana keluarga tidak terikat kontrak hukum tempo, artinya modal tersebut bisa diminta kembali besok pagi tanpa peringatan. Hal ini merupakan bom waktu likuiditas kas operasional harian.
   * **Strategi Mitigasi**:
     * Disiplin mengkarantina dana cadangan proyek (*contingency fund*) mutlak sebesar **Rp 4.500.000** di rekening sekunder yang sama sekali tidak tersentuh operasional kasir.
     * Mengembangkan sub-modul "Administrasi Pinjaman" yang mencatat riwayat nominal sisa dana keluarga secara riil, menenangkan kerabat yang menuntut bukti keamanan penitipan dana.

---

## 9. Risiko Terkait Stakeholder

Berikut adalah risiko-risiko kritis (bersumber dari dokumen Feasibility Study) yang berkaitan secara spesifik dengan perilaku pemangku kepentingan (manusia dan sistem AI pengembang) di proyek AbuCom, dinilai berdasarkan skala Probabilitas (P: 1-5) dan Dampak (D: 1-5).

| No | Risiko Stakeholder | P | D | Rencana Mitigasi Risiko |
|---|---|:---:|:---:|---|
| **9.1** | **Burnout Pemilik Usaha (STK-001)**: Pemilik kelelahan fisik/mental mengelola operasional toko manual dan pengawasan SDLC. | 3 | 5 | Optimalkan pendelegasian perancangan dokumen dan fungsi Python berulang ke tim AI. Batasi rapat review AI maksimal 1-2 jam/hari. |
| **9.2** | **Penarikan Dana Mendadak Kerabat (STK-019)**: Likuiditas kas toko lumpuh akibat modal kekeluargaan ditarik total dalam sehari. | 3 | 4 | Pisahkan rekening dan kunci mutlak dana cadangan (Rp 4.500.000) agar likuiditas mesin produksi/toko retail tidak terdampak. |
| **9.3** | **Kecurangan (Fraud) Saldo oleh Staf Kasir (STK-004)**: Karyawan kontrak memanfaatkan selah retur/pembatalan CLI untuk menilap kas. | 3 | 5 | Terapkan isolasi Hak Akses RBAC pada menu retur dan wajibkan sistem mencatat JSON aktivitas sensitif ini ke dalam log *Audit Trail* otomatis. |
| **9.4** | **Ketidaksesuaian Literasi Digital Staf (STK-002 s.d. 008)**: Staf gagal merespons CLI teks dan menimbulkan antrian pelanggan yang membludak. | 3 | 3 | Buat menu navigasi seragam di semua layar, gunakan warna teks kontras ANSI terminal, dan jalankan simulasi UAT wajib 3 hari purna-waktu. |
| **9.5** | **Keterlambatan Rekrutmen Karyawan (STK-002 s.d. 008)**: SDLC selesai dibangun (Bulan ke-11) namun toko belum mendapatkan staf. | 3 | 5 | Memulai proses kampanye seleksi wawancara pada pertengahan (Bulan ke-9) dan mempekerjakan *part-time* penguji UAT di Bulan 11. |
| **9.6** | **Human Error Input Dimensi Staf Produksi (STK-006)**: Salah menginput pecahan meter lari stempel, merusak HPP laporan kas bersih (laba/rugi). | 4 | 3 | Gunakan fungsi verifikator input *Regex* di tingkat terminal (menolak masukan huruf/simbol koma salah) dan meminta layar penegasan Y/N. |
| **9.7** | **Resistensi Budaya Cross-Functional Operasional (STK-002 s.d. 008)**: Pramuniaga/Fotocopy menolak membantu divisi Cetak di saat antrian meledak. | 3 | 3 | Formulasikan akumulasi "Poin Insentif Tambahan" yang otomatis membagi rata porsi uang lelah bonus bulanan bagi staf lintas divisi. |
| **9.8** | **Konflik Selisih Kas PC Kasir Bersama**: Beberapa staf shift pagi/malam berdebat akibat selisih uang fisik laci tanpa bukti jelas. | 4 | 4 | Kewajiban input modul "Rekonsiliasi Kas Harian" di setiap penghujung shift sebelum tombol Log Out / pergantian sesi token JWT diizinkan. |
| **9.9** | **Kebocoran File Data Pelanggan CRM (STK-015)**: Staf toko mengkopi database `.sql` untuk menjual kontak klien toko atau dieksploitasi pribadi. | 2 | 5 | Mengenkripsi skrip *backup* (.zip) menggunakan algoritma kuat (AES-256) dan membatasi folder root server Linux Debian hanya untuk Pemilik. |
| **9.10** | **Ketidakcocokan Integrasi Kode AI (STK-009 s.d. 014)**: Logika *heavy logic* Gemini 3.1 Pro bertubrukan dengan optimasi *deep coder* Claude Sonnet. | 3 | 4 | Tunjuk Gemini Pro sebagai Lead penentu *Standard Architecture* baku yang dilarang diubah secara drastis oleh LLM model lainnya saat proses. |
| **9.11** | **Migrasi File Excel Acak-acakan (STK-001/008)**: Ribuan baris data Excel warisan masa lalu penuh typo dan gagal dimuat (impor) ke sistem SQL relasional. | 4 | 4 | Menyuntikkan usulan modul tambahan (Inovasi): "Skrip Impor CSV Semiautomatis" yang memuat filter pembersihan teks (*data sanitization*). |
| **9.12** | **Hambatan Sintaksis Functional Programming (STK-001/012)**: Menghindari OOP untuk mengelola State sistem menimbulkan iterasi debugging buntu. | 3 | 4 | Pemilik membatasi diri menjadi penguji dan mendelegasikan 100% perancangan pembungkus session (JWT/State closure) kepada model Claude 4.6. |

---

## 10. Persetujuan dan Otorisasi

Dokumen Stakeholder Register (versi 1.2) ini diajukan sebagai acuan matang tata kelola pelibatan pemangku kepentingan dan menjadi bagian tidak terpisahkan dari basis input bagi dokumen fase analisis spesifikasi teknis perangkat lunak selanjutnya.

| Pihak Penandatangan | Jabatan / Peran | Tanda Tangan | Tanggal Persetujuan |
|---|---|---|---|
| **Pemilik Usaha AbuCom** | Sponsor Utama Proyek | `[MENUNGGU TANDA TANGAN DIGITAL PEMILIK]` | `[____-____-________]` |
| **Pemilik Usaha AbuCom** | Manajer Proyek Internal | `[MENUNGGU TANDA TANGAN DIGITAL PEMILIK]` | `[____-____-________]` |

---

## 11. Glosarium

Berikut adalah penjelasan alfabetis terkait istilah dan singkatan khusus yang digunakan di seluruh dokumen tata kelola pemangku kepentingan ini:

1. **Audit Trail**: Catatan log kronologis aktivitas rekam jejak pengguna dalam sistem operasi untuk pencegahan fraud kasir, disimpan dalam format JSON.
2. **BOM (Bill of Materials)**: Daftar rincian kuantitas/dimensi fisik desimal komponen dasar pembentuk sebuah produk jadi cetak (misalnya panjang karet stempel).
3. **Burnout**: Kondisi keletihan fisik dan emosional kronis (dialami pemilik toko) akibat merangkap peran manajemen, operasional, dan admin harian tanpa jeda.
4. **CAPEX (Capital Expenditure)**: Anggaran investasi modal kerja untuk mendanai aset keras/pengembangan IT proyek jangka panjang.
5. **CLI (Command Line Interface)**: Antarmuka program yang berinteraksi murni melalui terminal teks ketik, efisien dalam eksekusi operasi karena tanpa beban grafis GUI.
6. **CRM (Customer Relationship Management)**: Sistem tabel pengelolaan basis data identitas dan kontak WhatsApp loyalitas pelanggan pasca-transaksi toko.
7. **Cross-Functional**: Budaya gotong royong kerja dimana staf suatu divisi turun langsung membantu staf divisi lain (misal ritel ke produksi) untuk memecah antrian pelanggan.
8. **ERD (Entity Relationship Diagram)**: Diagram cetak biru yang merincikan struktur tabel-tabel data dan cara kolom data tersebut saling berelasi (*Foreign Key*) di basis data.
9. **Financial Stakeholder**: Pemangku kepentingan yang berkontribusi mendanai proyek atau bisnis (kreditur bank, sahabat yang memberikan injeksi modal).
10. **FP (Functional Programming)**: Paradigma merancang perangkat lunak dengan pendekatan fungsi matematis murni (*pure function*) yang kebal terhadap mutasi (perubahan diam-diam) nilai variabel memori sistem.
11. **Indirect Stakeholder**: Pemangku kepentingan yang pasif dalam proses *coding*, namun menanggung dampak paling signifikan dari sukses/gagalnya operasional akhir perangkat lunak.
12. **JWT (JSON Web Token)**: Kunci sesi otentikasi login elektronik tak terlihat yang memiliki hitung mundur kedaluwarsa waktu mandiri (*stateless session timer*).
13. **Keep Informed / Satisfied / Monitor / Manage Closely**: Istilah matriks prioritas intervensi manajemen untuk menenangkan/melibatkan kelompok orang tertentu (*Grid PMBOK*).
14. **Key User / End-User**: Pengguna (karyawan garda depan) yang mengetik/mengoperasikan modul program sehari-hari di toko.
15. **KUR (Kredit Usaha Rakyat)**: Kredit pendanaan berbunga lebih ringan disubsidi perbankan negara, sangat krusial agar tidak ada kredit macet UMKM.
16. **PKWT (Perjanjian Kerja Waktu Tertentu)**: Status ikatan ketenagakerjaan bagi staf kontrak sementara berdasarkan regulasi Cipta Kerja dan PP 35/2021.
17. **PKWTT (Perjanjian Kerja Waktu Tidak Tertentu)**: Status staf organik/tetap di perusahaan (biasanya untuk Kepala Percetakan).
18. **Power/Interest Grid**: Alat analisis matriks kekuasaan-kepentingan pemangku kepentingan (*PMBOK 6th/7th Edition*).
19. **PPOB (Payment Point Online Bank)**: Jasa bayar tagihan, saldo listrik PLN, top-up *e-wallet*, dan pulsa telekomunikasi toko (produk tanpa fisik).
20. **RACI Matrix**: Peta penugasan kerja proyek. Akronim dari fungsi eksekutor *(Responsible)*, pemegang keputusan mutlak *(Accountable)*, narasumber ahli *(Consulted)*, dan penerima laporan progres pasif *(Informed)*.
21. **Role-Based Access Control (RBAC)**: Mekanisme pembatasan tampilan menu dan akses penyimpanan sensitif toko secara otomatis berbasis identitas *Role* profil login staf.
22. **SDD (System Design Document)**: Dokumen desain cetak biru sistem perangkat lunak yang berfokus ke perancangan arsitektur, logis database (SQL), skema pengamanan token, dan diagram infrastruktur LAN server.
23. **SDLC (Software Development Life Cycle)**: Urutan fase baku pembangunan proyek peranti lunak mulai perancangan dokumen konsep awal, penulisan kode sumber, ujicoba bug, hingga hari H peluncuran di lapangan (operasional kasir).
24. **Sponsor**: Pihak tunggal pemegang dana modal finansial proyek (Pemilik Usaha sendiri).
25. **SRS (Software Requirements Specification)**: Dokumen spesifikasi rincian mutlak yang mendefinisikan apa saja tombol-tombol input fungsional (*Use Cases*) dan seberapa cepat *software* harus merespon sebelum sistem ini mulai diprogram.
26. **Stakeholder**: Siapapun individu, kelompok AI (algoritma cerdas), atau pihak luar yang terpengaruh, untung rugi, dan terikat dengan proyek pembangunan ini.
27. **Stakeholder Register**: Induk dokumen yang mendata/meregistrasi semua stakeholder agar tidak ada yang luput dilibatkan (dokumen ini).
28. **UAT (User Acceptance Testing)**: Masa orientasi 3 hari berupa pengujian coba-coba aplikasi oleh calon staf (kasir) untuk memvalidasi apakan sistem sudah bekerja di dunia nyata sesuai ekspektasi pesanan/transaksi aslinya.
29. **UU PDP (Undang-Undang Pelindungan Data Pribadi)**: Undang-Undang Republik Indonesia Nomor 27 Tahun 2022. Memuat sanksi perdata terkait kegagalan mencegah kebocoran/peretasan file nomor WhatsApp & nama pelanggan toko ke tangan pihak ketiga.

---

## 12. Referensi Dokumen

| # | Nama File | Lokasi Path Relatif | Keterangan Penggunaan |
|---|---|---|---|
| 1 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Referensi utama (primer) data tim pengembang AI, struktur organisasi staf, risiko awal, dan RACI awal. |
| 2 | `02_feasibility_study.md` | `docs/sdlc/01_planning/02_feasibility_study.md` | Referensi sekunder data kesiapan rekrutmen staf baru, literasi digital, aspek hukum UU PDP, PKWT/PKWTT, dan mitigasi risiko operasional. |
| 3 | `narasi.txt` | `docs/sdlc/narasi.txt` | Referensi pendukung konteks hubungan personal pemilik dengan kerabat pemberi pinjaman, kondisi emosional pemilik (*burnout*), dan harapan RBAC data sensitif. |
| 4 | `04_tech_stack_decision.md` | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Referensi verifikasi spesifikasi teknis dan nama/versi model AI pengembang (STK-009 s.d. STK-014). |
| 5 | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Referensi validasi kemungkinan stakeholder atau kebutuhan baru yang dimunculkan oleh proposal inovasi sistem. |
