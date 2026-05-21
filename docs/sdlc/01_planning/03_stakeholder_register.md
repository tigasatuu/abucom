---
dokumen    : Stakeholder Register
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : 2026-05-21
status     : Draft
penyusun   : Senior Stakeholder Analyst & Project Governance Specialist
---

# Stakeholder Register — AbuCom

## Riwayat Perubahan Dokumen

| Versi | Tanggal | Perubahan | Oleh |
|---|---|---|---|
| 1.0 | 2026-05-21 | Pembuatan awal dokumen berdasarkan analisis Project Charter, Feasibility Study, dan Narasi Pemilik Usaha. | Senior Stakeholder Analyst & Project Governance Specialist |

---

## 1. Informasi Dokumen

Dokumen **Stakeholder Register** ini dirancang secara khusus untuk mengidentifikasi, menganalisis, mengklasifikasikan, serta menentukan strategi pengelolaan bagi seluruh pihak yang berkepentingan terhadap proyek pembangunan **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**.

Sebagai bagian integral dari fase *Planning* dalam siklus SDLC, dokumen ini bertujuan untuk:
1. **Identifikasi Komprehensif**: Mendokumentasikan seluruh pemangku kepentingan (individu, kelompok, maupun institusi) yang mempengaruhi atau dipengaruhi oleh jalannya proyek.
2. **Analisis Pengaruh & Kepentingan**: Memetakan dinamika kekuasaan (*power*) dan minat (*interest*) masing-masing pemangku kepentingan untuk memprioritaskan upaya tata kelola.
3. **Penyusunan Strategi Pelibatan**: Merancang rencana komunikasi terstruktur dan mitigasi potensi resistensi untuk memastikan transisi operasional yang mulus dari manual berbasis Excel ke sistem digital berbasis CLI.

### Hubungan dengan Dokumen SDLC Lainnya:
* **Project Charter**: Dokumen ini memperluas identifikasi awal stakeholder (Bagian 6.1) dan RACI Matrix (Bagian 6.2) yang tercantum di Project Charter v1.1.
* **Software Requirements Specification (SRS)**: Profil, hak akses (RBAC), dan kebutuhan stakeholder yang tercatat di sini menjadi input utama bagi pembatasan hak akses modul serta kebutuhan fungsional database pelanggan (CRM).
* **System Design Document (SDD)**: Menentukan rancangan logis hak akses database dan log Audit Trail.
* **User Acceptance Testing (UAT) & Deployment**: Menjadi acuan bagi penentuan aktor penguji skenario UAT dan target pelatihan operasional.

---

## 2. Daftar Identifikasi Stakeholder

Berikut adalah daftar seluruh stakeholder proyek AbuCom yang diklasifikasikan ke dalam kelompok internal (terlibat langsung dalam pengembangan atau operasional harian) dan eksternal (mempengaruhi proyek dari luar batas organisasi).

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
| **STK-015** | Pelanggan AbuCom | Penerima Manfaat Layanan (Beneficiary) | Indirect Stakeholder / Beneficiary | Pihak yang menggunakan jasa percetakan, ATK, PPOB, keuangan, dan service printer/PC. |
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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Menghilangkan ketergantungan pada pencatatan manual Microsoft Excel yang tidak terintegrasi dan memicu kelelahan fisik/mental.
* Memiliki laporan keuangan laba/rugi, pengeluaran rutin, dan tabungan aset secara instan (<5 detik) dan akurat untuk memantau performa 5 divisi usaha.
* Mengotomatisasi pemotongan stok bahan baku secara presisi menggunakan komposisi bahan (*Bill of Materials* / BOM) dengan dimensi desimal (panjang x lebar atau volume desimal) setelah transaksi selesai.
* Pengamanan hak akses yang ketat (RBAC) agar data pinjaman bank, tabungan pribadi, dan modul payroll hanya dapat diakses oleh Pemilik Usaha.
* Memantau kehadiran staf, sisa utang kasbon staf, dan perhitungan penggajian cerdas (gaji pokok vs persentase keuntungan) secara otomatis.

**Potensi Pengaruh terhadap Proyek**:
* **Sangat Tinggi**. Pemilik memegang kontrol mutlak atas anggaran proyek (CAPEX Rp 40.000.000), penentuan prioritas ruang lingkup, durasi pengembangan (12 bulan), dan otorisasi persetujuan dokumen SDLC. Bertindak sebagai pengembang junior yang melakukan integrasi akhir kode program.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Sangat Tinggi**. Keberhasilan aplikasi ini akan secara drastis memangkas beban operasional harian pemilik (pembukuan terotomatisasi), memitigasi risiko *burnout*, dan memungkinkan delegasi 90% aktivitas teknis harian ke staf baru dengan aman.

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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha setelah proses rekrutmen selesai]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan antarmuka CLI (Command Line Interface) yang logis, menu yang teratur, dan navigasi yang cepat.
* Membutuhkan visualisasi antrian pengerjaan (*job tracking*) yang mudah dipantau untuk mengkoordinasikan tim produksi dan desainer.
* Akses mudah untuk memantau tingkat persediaan bahan baku dan barang retail di gudang guna mencegah kekosongan bahan.
* Memerlukan *CLI User Manual* dan program pelatihan fungsional yang memadai sebelum go-live.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (Fase Pengembangan)**: Tidak mempengaruhi arsitektur sistem.
* **Tinggi (Fase Operasional)**: Menentukan keberhasilan koordinasi operasional harian toko pasca penerapan.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Memudahkan pemantauan seluruh aktivitas toko tanpa perlu melakukan pengecekan fisik lembar demi lembar catatan kertas/Excel.

**Fase Keterlibatan Maksimal**:
* Testing (UAT), Deployment (Pelatihan), dan Operational.

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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha setelah proses rekrutmen selesai]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan menu pencatatan transaksi yang cepat saat melayani pelanggan langsung di konter.
* Fitur pencarian harga barang retail ATK, produk percetakan kustom, dan tarif layanan digital (PPOB) yang dinamis sesuai skema harga (retail, grosir, mitra).
* Kemudahan penginputan data kontak pelanggan (CRM) dan spesifikasi pesanan khusus ke dalam sistem antrian.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah**. Sebagai pengguna akhir operasional entry data.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Mempercepat proses pelayanan pelanggan karena tidak perlu lagi membuka-buka file Excel harga secara manual yang lambat.

**Fase Keterlibatan Maksimal**:
* Testing (UAT), Deployment, dan Operational.

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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha setelah proses rekrutmen selesai]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Fitur pencatatan pembayaran yang fleksibel (DP di awal, pelunasan di akhir saat barang diambil).
* Modul khusus rekonsiliasi kas laci fisik (*cash reconciliation*) di akhir shift untuk mendeteksi selisih uang tunai.
* Pilihan otomatis penentuan biaya admin termurah dari 6 e-wallet (Mandiri, Dana, Gopay, LinkAja, ShopeePay, OVO) untuk jasa transfer/tarik tunai.
* Alur penanganan retur barang rusak atau pembatalan transaksi dengan pengembalian DP yang secara otomatis menyinkronkan data kas.

**Potensi Pengaruh terhadap Proyek**:
* **Sedang-Tinggi (Operasional)**: Kepatuhan kasir menginput data menentukan validitas seluruh laporan arus kas harian.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Memberikan keamanan kerja karena rekonsiliasi tercatat secara sistematis di Audit Trail, mengurangi risiko tuduhan kecurangan sepihak.

**Fase Keterlibatan Maksimal**:
* Testing (UAT), Deployment, dan Operational.

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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha setelah proses rekrutmen selesai]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Akses langsung ke modul antrian pekerjaan dengan filter khusus status `Proses Desain`.
* Fitur pencatatan lokasi fisik/digital arsip berkas desain pelanggan (lokasi direktori server lokal) agar mudah dicari untuk cetak ulang (*re-order*).
* Kemudahan mengubah status antrian pekerjaan dari `Proses Desain` ke status `Produksi`.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah**. Pengguna entry data spesifik modul antrian dan arsip.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Mempercepat proses pengerjaan desain dan menghilangkan kekacauan pelacakan file pelanggan.

**Fase Keterlibatan Maksimal**:
* Testing (UAT), Deployment, dan Operational.

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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha setelah proses rekrutmen selesai]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Akses ke modul antrian status `Produksi` untuk melihat daftar pekerjaan cetak fisik yang siap diproses.
* Fitur pencatatan pemakaian bahan baku riil dan pencatatan limbah produksi (*waste management*) jika terjadi kesalahan cetak/bahan rusak.
* Kemudahan pembaruan status antrian ke status `Selesai` setelah proses finishing produk.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah**. Pengguna entry data pemakaian stok riil.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Akurasi pemotongan stok bahan baku di gudang sangat bergantung pada kedisiplinan staf produksi melakukan input dimensi pemakaian riil dan data limbah cetak.

**Fase Keterlibatan Maksimal**:
* Testing (UAT), Deployment, dan Operational.

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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha setelah proses rekrutmen selesai]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Antarmuka cepat untuk mencatat transaksi ritel cepat (fotokopi per lembar dan cetak dokumen hitam-putih/warna).
* Integrasi antarmuka yang sederhana agar dapat dialihkan membantu mencatat pemakaian bahan di divisi produksi cetak jika antrian padat (*cross-functional*).

**Potensi Pengaruh terhadap Proyek**:
* **Rendah**. Pengguna operasional harian.

**Potency Dampak Proyek terhadap Stakeholder**:
* Memudahkan pencatatan omzet harian dari transaksi retail cepat tanpa repot menulis di buku nota fisik.

**Fase Keterlibatan Maksimal**:
* Testing (UAT), Deployment, dan Operational.

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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha setelah proses rekrutmen selesai]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Modul pencatatan data supplier, riwayat harga beli bahan baku dari supplier, dan pencatatan utang pembelian tempo.
* Menu fungsional pelaksanaan rekonsiliasi persediaan (*Stock Opname*) berkala untuk mencocokkan stok fisik vs aplikasi.
* Fitur pencatatan pengurangan stok otomatis atas pengambilan barang retail ATK untuk kebutuhan internal divisi produksi.

**Potensi Pengaruh terhadap Proyek**:
* **Sedang-Tinggi (Operasional)**: Keakuratan data gudang fisik vs database sistem dikelola oleh staf ini.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Meniadakan proses pencatatan stok kartu gudang manual berbasis kertas yang rawan hilang dan basah.

**Fase Keterlibatan Maksimal**:
* Testing (UAT), Deployment (Input data awal), dan Operational.

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
| **Kontak / Identifikasi** | Terintegrasi melalui API/Interface Google AI Studio / Gemini |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan instruksi prompt yang terstruktur, parameter konteks proyek yang lengkap, dan batasan teknis yang didefinisikan dengan jelas.
* Membutuhkan standardisasi paradigma *Functional Programming* yang konsisten di seluruh modul logika bisnis Python.

**Potensi Pengaruh terhadap Proyek**:
* **Tinggi**. Menentukan kualitas desain arsitektur modular sistem, perancangan algoritma perhitungan BOM desimal, dan logika penggajian cerdas. Kesalahan desain arsitektur akan menghambat skalabilitas multi-cabang.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Tidak terpengaruh secara emosional atau finansial, namun performa pengkodeannya dinilai berdasarkan keberhasilan eksekusi arsitektur.

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
| **Kontak / Identifikasi** | Terintegrasi melalui API/Interface Google AI Studio / Gemini |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan skema database yang valid dan dokumentasi terstruktur untuk menghasilkan dokumen formal SDLC yang sinkron.

**Potensi Pengaruh terhadap Proyek**:
* **Sedang**. Kualitas dokumentasi formal (SRS, SDD, User Manual) bergantung pada model ini agar dokumen referensi fase selanjutnya tetap konsisten.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Output dokumen diuji kelengkapannya terhadap checklist kepatuhan standar industri.

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
| **Kontak / Identifikasi** | Terintegrasi melalui API/Interface Google AI Studio / Gemini |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan cuplikan kode spesifik yang bermasalah (*buggy snippet*) disertai pesan error runtime untuk analisis cepat.

**Potensi Pengaruh terhadap Proyek**:
* **Sedang**. Mempercepat siklus perbaikan bug ringan selama masa testing fungsional 2 mingguan.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Memastikan kecepatan respons review kode tetap berada dalam batas latensi milidetik.

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
| **Kontak / Identifikasi** | Terintegrasi melalui API/Interface Anthropic |

**Kebutuhan dan Ekspektasi Utama**:
* Ketersediaan struktur direktori proyek, aturan penulisan kode imutabel, dan data input representatif untuk kalkulasi mendalam.

**Potensi Pengaruh terhadap Proyek**:
* **Tinggi**. Menghasilkan kode fungsional Python tingkat tinggi yang murni (*pure functions*), optimasi kode antarmuka CLI, dan restrukturisasi kode agar efisien dari kebocoran memori.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Keakuratan dan kebersihan kode program diuji menggunakan pengujian unit testing dan analisis statis.

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
| **Kontak / Identifikasi** | Terintegrasi melalui API/Interface Anthropic |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan kejelasan regulasi eksternal (UU PDP) dan pemetaan aset sensitif yang harus dilindungi di database MySQL.

**Potensi Pengaruh terhadap Proyek**:
* **Tinggi**. Merancang strategi enkripsi kata sandi (bcrypt), penanganan token otentikasi JWT, desain tabel log Audit Trail, dan perlindungan direktori database cadangan.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Sistem tata kelola keamanan diuji dengan simulasi percobaan penetrasi internal (UAT).

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
| **Kontak / Identifikasi** | Terintegrasi melalui Model Open Source lokal/server |

**Kebutuhan dan Ekspektasi Utama**:
* Memerlukan skema relasi tabel (ERD) dan tipe data kolom MySQL yang telah disetujui Lead Architect.

**Potensi Pengaruh terhadap Proyek**:
* **Sedang**. Mempercepat setup awal basis data melalui penyediaan template SQL inisialisasi yang terformat rapi.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Efisiensi skrip seed data awal diuji terhadap kecepatan loading data awal aplikasi.

**Fase Keterlibatan Maksimal**:
* Design, Implementation (Setup).

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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — data kontak tersimpan di modul CRM setelah transaksi awal]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Membutuhkan pelayanan yang cepat, estimasi penyelesaian pengerjaan pesanan yang akurat, dan kualitas produk cetak yang konsisten.
* Menginginkan data pribadi mereka (nama dan nomor WhatsApp) aman dari penyalahgunaan atau kebocoran pihak luar (UU PDP).
* Kemudahan melakukan cetak ulang (*re-order*) pesanan kustom masa lalu dengan cepat tanpa mendesain ulang dari awal.

**Potensi Pengaruh terhadap Proyek**:
* **Rendah (Fase Pengembangan)**: Tidak terlibat langsung dalam siklus pengembangan.
* **Sangat Tinggi (Fase Operasional)**: Kepuasan mereka merupakan indikator utama keberhasilan bisnis secara keseluruhan.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Sedang**. Mendapatkan pengalaman layanan yang lebih profesional, tepat waktu, dan terjaga kerahasiaan datanya.

**Fase Keterlibatan Maksimal**:
* Pasca Go-Live (Operasional).

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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — daftar supplier perlu diisi manual oleh Pemilik Usaha di modul inventaris]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Mengharapkan pembayaran utang pembelian tepat waktu sesuai kesepakatan tenor tempo.
* Membutuhkan pesanan pengadaan bahan yang terjadwal dan kuantitas pembelian yang stabil untuk menjaga loyalitas mitra.

**Potensi Pengaruh terhadap Proyek**:
* **Sedang**. Keterlambatan suplai bahan baku dari supplier fisik akan menghambat kelancaran proses produksi cetak toko, yang berdampak pada validitas antrian.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Sistem inventaris AbuCom akan membantu merapikan riwayat transaksi pembelian supplier dan riwayat utang usaha yang transparan.

**Fase Keterlibatan Maksimal**:
* Pasca Go-Live (Operasional).

---

### 3.17. [STK-017] Bank BRI (Kreditur Berbunga)

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-017 |
| **Nama / Jabatan** | Bank BRI |
| **Organisasi / Afiliasi** | PT Bank Rakyat Indonesia (Persero) Tbk |
| **Kategori** | Eksternal |
| **Tipe** | Institusi |
| **Peran dalam Proyek** | Kreditur Modal Berbunga (Institusi) |
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — nomor kontrak pinjaman bank perlu diisi oleh Pemilik Usaha]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Menuntut pembayaran cicilan setoran bulanan pokok dan bunga tepat waktu sebelum tanggal jatuh tempo.
* Mengharapkan kepatuhan penuh terhadap jadwal tenor yang telah ditandatangani.

**Potensi Pengaruh terhadap Proyek**:
* **Sedang-Tinggi (Finansial)**: Kegagalan setoran bulanan akibat masalah likuiditas kas toko dapat menyebabkan denda hukum, penyitaan jaminan aset fisik usaha, atau pemblokiran kredit modal masa depan.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Sistem manajemen terpadu menjamin pengelolaan anggaran kas operasional toko yang terkendali untuk memastikan kewajiban setoran bank bulanan terbayar aman.

**Fase Keterlibatan Maksimal**:
* Seluruh durasi proyek (sebagai kewajiban finansial luar).

---

### 3.18. [STK-018] Bank Mandiri (Kreditur Berbunga)

| Atribut | Detail |
|---|---|
| **ID Stakeholder** | STK-018 |
| **Nama / Jabatan** | Bank Mandiri |
| **Organisasi / Afiliasi** | PT Bank Mandiri (Persero) Tbk |
| **Kategori** | Eksternal |
| **Tipe** | Institusi |
| **Peran dalam Proyek** | Kreditur Modal Berbunga (Institusi) |
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — nomor kontrak pinjaman bank perlu diisi oleh Pemilik Usaha]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Menuntut pembayaran cicilan setoran bulanan pokok dan bunga tepat waktu sebelum tanggal jatuh tempo.
* Mengharapkan kepatuhan penuh terhadap jadwal tenor yang telah ditandatangani.

**Potensi Pengaruh terhadap Proyek**:
* **Sedang-Tinggi (Finansial)**: Kegagalan setoran bulanan akibat masalah likuiditas kas toko dapat menyebabkan denda hukum, penyitaan jaminan aset fisik usaha, atau pemblokiran kredit modal masa depan.

**Potensi Dampak Proyek terhadap Stakeholder**:
* Sistem manajemen terpadu menjamin pengelolaan anggaran kas operasional toko yang terkendali untuk memastikan kewajiban setoran bank bulanan terbayar aman.

**Fase Keterlibatan Maksimal**:
* Seluruh durasi proyek (sebagai kewajiban finansial luar).

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
| **Kontak / Identifikasi** | `*[DATA BELUM TERSEDIA — catatan nama/kontak kerabat perlu diisi manual oleh Pemilik Usaha]*` |

**Kebutuhan dan Ekspektasi Utama**:
* Mengharapkan transparansi mutlak atas sisa saldo pinjaman mereka yang dititipkan pada pemilik usaha.
* Menginginkan fleksibilitas penarikan dana titipan mereka kapan saja secara mendadak (sebagian, total, maupun permanen) saat mereka memiliki keperluan darurat.

**Potensi Pengaruh terhadap Proyek**:
* **Tinggi**. Sifat penarikan dana yang tidak terprediksi dan mendadak dapat secara serius mengganggu arus kas pengembangan proyek jika dana cadangan darurat (*contingency fund* Rp 4.500.000) dicampuradukkan dengan kas operasional harian toko.

**Potensi Dampak Proyek terhadap Stakeholder**:
* **Sedang**. Memberikan rasa aman dan percaya karena pencatatan saldo utang piutang pemilik usaha terstruktur dengan transparan di dalam aplikasi baru, menghindari perselisihan relasi kekeluargaan.

**Fase Keterlibatan Maksimal**:
* Seluruh durasi proyek.

---

## 4. Klasifikasi Stakeholder

Untuk menyusun strategi pengelolaan yang efektif, seluruh stakeholder diklasifikasikan berdasarkan kategori keterlibatan, pengaruh terhadap jalannya proyek (*power*), dan tingkat kepentingan (*interest*) terhadap hasil akhir proyek.

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
|---|---|---|---|---|---|
| **STK-001** | Pemilik Usaha AbuCom | 5 | 5 | Kuadran A | **Manage Closely** — Pembuat keputusan utama, integrator kode, pengendali anggaran. |
| **STK-002** | Staf Kepala Percetakan | 2 | 4 | Kuadran C | **Keep Informed** — Koordinasikan pelacakan antrian, berikan panduan. |
| **STK-003** | Staf Pramuniaga | 2 | 4 | Kuadran C | **Keep Informed** — Latih input transaksi cepat & CRM secara tepat. |
| **STK-004** | Staf Kasir | 2 | 4 | Kuadran C | **Keep Informed** — Pastikan pemahaman alur DP, pelunasan, & rekonsiliasi. |
| **STK-005** | Staf Desainer | 2 | 4 | Kuadran C | **Keep Informed** — Sosialisasikan pencatatan path arsip berkas desain. |
| **STK-006** | Staf Produksi Cetak | 2 | 4 | Kuadran C | **Keep Informed** — Tekankan pentingnya input pemakaian bahan riil & limbah. |
| **STK-007** | Staf Fotocopy & Print | 2 | 4 | Kuadran C | **Keep Informed** — Latih pencatatan transaksi ritel cepat & cross-functional. |
| **STK-008** | Staf Gudang | 2 | 4 | Kuadran C | **Keep Informed** — Latih skema input supplier, stock opname & utang. |
| **STK-009** | Gemini 3.1 Pro (High) | 3 | 4 | Kuadran C | **Keep Informed** — Berikan prompt instruksi logika arsitektur & BOM. |
| **STK-010** | Gemini 3.1 Pro (Low) | 2 | 4 | Kuadran C | **Keep Informed** — Berikan arahan detail penulisan berkas dokumen formal. |
| **STK-011** | Gemini 3 Flash | 2 | 4 | Kuadran C | **Keep Informed** — Gunakan untuk review cepat kesalahan sintaksis. |
| **STK-012** | Claude Sonnet 4.6 | 3 | 4 | Kuadran C | **Keep Informed** — Tugaskan khusus penulisan modul FP Python kompleks. |
| **STK-013** | Claude Opus 4.6 | 3 | 4 | Kuadran C | **Keep Informed** — Fokuskan pada audit keamanan, enkripsi & Audit Trail. |
| **STK-014** | GPT-OSS 120B | 2 | 4 | Kuadran C | **Keep Informed** — Gunakan untuk setup database & data dummy awal. |
| **STK-015** | Pelanggan AbuCom | 1 | 2 | Kuadran D | **Monitor** — Pantau respon kepuasan waktu pelayanan di toko. |
| **STK-016** | Vendor & Supplier | 2 | 2 | Kuadran D | **Monitor** — Jaga stabilitas supply bahan baku & transaksi utang. |
| **STK-017** | Bank BRI | 4 | 2 | Kuadran B | **Keep Satisfied** — Jamin kelancaran cicilan modal bulanan tepat waktu. |
| **STK-018** | Bank Mandiri | 4 | 2 | Kuadran B | **Keep Satisfied** — Jamin kelancaran cicilan modal bulanan tepat waktu. |
| **STK-019** | Kerabat & Keluarga | 4 | 3 | Kuadran B | **Keep Satisfied** — Berikan transparansi saldo & pisahkan dana cadangan. |

---

### 4.3. Matriks Pengaruh/Dampak (Influence/Impact Matrix)

Matriks ini menganalisis tingkat pengaruh pemangku kepentingan terhadap keputusan arah proyek disandingkan dengan besarnya dampak hasil proyek terhadap aktivitas mereka sehari-hari.

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
| **STK-015** | Pelanggan AbuCom | 1 | 3 | **Prioritas 4 (Rendah)** |
| **STK-016** | Vendor & Supplier | 2 | 3 | **Prioritas 4 (Rendah)** |
| **STK-017** | Bank BRI | 4 | 1 | **Prioritas 3 (Sedang)** |
| **STK-018** | Bank Mandiri | 4 | 1 | **Prioritas 3 (Sedang)** |
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
   * **Analisis**: Karyawan saat ini belum direkrut secara fisik, sehingga statusnya adalah `Unaware`. Risiko transisi terletak pada potensi kebingungan staf baru menghadapi antarmuka CLI yang tidak ramah visual.
   * **Tindakan**: Mengadakan program rekrutmen terencana pada Bulan 9-10, dilanjutkan dengan pelatihan intensif selama 3 hari menggunakan buku manual CLI yang interaktif sebelum go-live.

2. **Kerabat & Keluarga (STK-019)**:
   * **Gap**: `Neutral` (Saat Ini) $\rightarrow$ `Supportive` (Diharapkan).
   * **Analisis**: Kerabat pemberi pinjaman modal tanpa bunga saat ini bersikap netral dan cenderung melihat dari aspek hubungan kekeluargaan. Namun, ketidakpastian kebutuhan dana mendadak mereka berpotensi memicu ditariknya kas proyek secara tiba-tiba.
   * **Tindakan**: Memberikan transparansi pencatatan saldo utang piutang di sistem dan menyajikan performa perkembangan bisnis yang sehat agar mereka merasa aman atas dana yang dipinjamkan.

3. **Tim Pengembang AI (STK-009 s.d. STK-014)**:
   * **Gap**: `Supportive` (Saat Ini) $\rightarrow$ `Leading` (Diharapkan).
   * **Analisis**: Tim AI saat ini mendukung pembuatan kode program secara pasif. Untuk menjamin performa modular *Functional Programming*, Tim AI harus memimpin (*Leading*) dalam memberikan usulan perbaikan standardisasi arsitektur dan mitigasi celah keamanan (Audit Trail/bcrypt).
   * **Tindakan**: Junior Programmer memformulasikan perintah prompt secara spesifik dan memprioritaskan integrasi kode program sesuai arsitektur Lead Architect AI.

---

## 6. Kebutuhan dan Ekspektasi Stakeholder

Tabel di bawah mengkonsolidasikan seluruh kebutuhan fungsional dan kriteria kepuasan masing-masing stakeholder terhadap proyek AbuCom.

| ID | Stakeholder | Kebutuhan Utama | Ekspektasi terhadap Proyek | Kriteria Kepuasan |
|---|---|---|---|---|
| **STK-001** | Pemilik Usaha | Laporan Laba/Rugi otomatis per divisi, BOM desimal stok, RBAC, & Audit Trail. | Mengurangi beban operasional harian toko, mitigasi burnout. | 100% laporan keuangan bebas Excel, selisih persediaan fisik vs sistem <1.0%. |
| **STK-002** | Staf Kepala Percetakan | CLI teratur, visual antrian yang jelas, pemantauan stok. | Memudahkan koordinasi toko tanpa rekap manual. | Antrian transisi lancar, tidak ada pesanan terlewat. |
| **STK-003** | Staf Pramuniaga | Entry transaksi cepat, pencarian harga, input data CRM. | Proses input pelanggan dan order cepat. | Pelanggan terlayani cepat di konter. |
| **STK-004** | Staf Kasir | Pembayaran DP/Pelunasan, penentu Agen termurah, rekonsiliasi kas. | Keamanan data uang laci kasir terjaga otomatis. | Tidak terjadi selisih kas fisik vs sistem di akhir hari. |
| **STK-005** | Staf Desainer | Filter status `Proses Desain`, pencatatan direktori arsip desain. | Pencarian desain pelanggan cepat untuk re-order. | Lokasi arsip tersimpan rapi, mudah dicari. |
| **STK-006** | Staf Produksi Cetak | Filter status `Produksi`, input pemakaian bahan riil & limbah. | Bahan baku diproduksi presisi sesuai pesanan. | Sisa stok bahan di sistem sinkron dengan fisik. |
| **STK-007** | Staf Fotocopy & Print | Pencatatan transaksi retail cepat, fleksibilitas cross-functional. | Kecepatan entry order fotokopi tinggi. | Rekap transaksi ritel harian tersimpan aman. |
| **STK-008** | Staf Gudang | Menu input supplier, stock opname berkala, utang pembelian. | Stok terkontrol tanpa kartu stok kertas. | Stock Opname harian berjalan cepat. |
| **STK-009** | Gemini 3.1 Pro (High) | Konteks proyek yang utuh, batasan FP Python yang jelas. | Menghasilkan struktur modular yang andal. | Kode arsitektur lolos review modularitas. |
| **STK-010** | Gemini 3.1 Pro (Low) | Skema relasi database terfinalisasi. | Dokumen SDLC tersusun lengkap tanpa typo. | Berkas SRS & SDD disetujui formal. |
| **STK-011** | Gemini 3 Flash | Potongan kode error dan log runtime. | Uji sintaksis cepat & deteksi bug ringan. | Error teratasi dalam sprint berjalan. |
| **STK-012** | Claude Sonnet 4.6 | Standardisasi FP Python yang disepakati. | Penulisan fungsi murni tanpa efek samping. | Pengujian unit testing fungsi matematika lolos 100%. |
| **STK-013** | Claude Opus 4.6 | Kebijakan hak akses menu dan aturan UU PDP. | Sistem aman dari bypass kata sandi & manipulasi. | Enkripsi bcrypt & token JWT berjalan aman. |
| **STK-014** | GPT-OSS 120B | Rancangan ERD MySQL. | Skrip inisialisasi tabel SQL bebas sintaks error. | database terbuat dengan data seed realistis. |
| **STK-015** | Pelanggan AbuCom | Kecepatan cetak, arsip desain teratur, privasi data WA. | Pesanan selesai tepat waktu, data aman. | WA link template dikirim cepat saat pesanan siap. |
| **STK-016** | Vendor & Supplier | Rekapitulasi transaksi pembelian, saldo utang usaha. | Pembayaran piutang tepat waktu. | Pembayaran dilakukan sesuai jatuh tempo utang tempo. |
| **STK-017** | Bank BRI | Pembayaran cicilan bulanan tepat waktu. | Penurunan risiko kredit macet. | Setoran bulanan terbayar otomatis sebelum jatuh tempo. |
| **STK-018** | Bank Mandiri | Pembayaran cicilan bulanan tepat waktu. | Penurunan risiko kredit macet. | Setoran bulanan terbayar otomatis sebelum jatuh tempo. |
| **STK-019** | Kerabat & Keluarga | Laporan saldo pinjaman transparan & fleksibel. | Dana aman dan dapat ditarik saat darurat. | Keamanan relasi personal terjaga baik. |

---

## 7. Matriks RACI Stakeholder

Matriks RACI ini memperjelas akuntabilitas dan tanggung jawab untuk 10 aktivitas utama di seluruh siklus hidup proyek AbuCom.

**Legenda RACI:**
* **R (Responsible)**: Pihak yang melakukan pekerjaan secara langsung untuk menyelesaikan tugas.
* **A (Accountable)**: Pihak yang memegang tanggung jawab penuh atas hasil akhir pekerjaan dan memiliki keputusan mutlak.
* **C (Consulted)**: Pihak yang dimintai masukan atau keahlian sebelum pekerjaan diselesaikan.
* **I (Informed)**: Pihak yang diberi tahu mengenai perkembangan pekerjaan setelah selesai.

**Pemetaan Kolom:**
* **STK-001**: Pemilik Usaha
* **STK-002 s.d. 008**: Karyawan Staf (Kepala Percetakan, Pramuniaga, Kasir, Desainer, Produksi, Fotocopy, Gudang)
* **STK-009 s.d. 014**: Tim Pengembang AI (Gemini 3.1, Claude 4.6, GPT-OSS)
* **STK-015 s.d. 019**: Pihak Eksternal (Pelanggan, Supplier, Kreditur Bank/Kerabat)

| Aktivitas / Deliverables | STK-001 | STK-002 s.d. 008 | STK-009 s.d. 014 | STK-015 | STK-016 | STK-017 s.d. 018 | STK-019 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1. Perencanaan & Project Charter** | **A / R** | I | R | I | I | I | I |
| **2. Penyusunan Stakeholder Register** | **A** | I | **R** | I | I | I | I |
| **3. Spesifikasi Kebutuhan (SRS)** | **A / R** | C | **R** | I | I | I | I |
| **4. Desain Arsitektur & DB (SDD)** | **A** | I | **R** | I | I | I | I |
| **5. Implementasi Kode Program** | **A / R** | I | **R** | I | I | I | I |
| **6. Pengujian Fungsional & UAT** | **A / R** | **R** | C | I | I | I | I |
| **7. Instalasi & Input Data Excel** | **A / R** | **R** | C | I | I | I | I |
| **8. Pelatihan Staf Operasional** | **A / R** | **R** | C | I | I | I | I |
| **9. Operasional & Rekonsiliasi Harian** | **A** | **R** | I | I | I | I | I |
| **10. Pengelolaan Pinjaman & Keuangan** | **A / R** | I | I | I | I | C | C / I |

---

## 8. Strategi Pengelolaan dan Komunikasi Stakeholder

### 8.1. Rencana Komunikasi per Stakeholder

Rencana ini merinci metode, frekuensi, dan penanggung jawab komunikasi baik selama fase pengembangan proyek maupun setelah fase operasional go-live.

| ID | Stakeholder | Metode Komunikasi | Frekuensi | Penanggung Jawab | Informasi yang Dikomunikasikan |
|---|---|---|---|---|---|
| **STK-001** | Pemilik Usaha | Peninjauan berkas dokumen SDLC langsung di direktori lokal, pengujian demo menu CLI di terminal. | Harian / Tiap akhir sprint 2 mingguan | Pemilik Usaha (Mandiri) | Status penyelesaian modul program, validasi logika bisnis keuangan, dan review kemajuan jadwal. |
| **STK-002 s.d. STK-008** | Calon Staf Baru | Briefing kelompok secara tatap muka, simulasi pengoperasian CLI, pembagian cetak fisik buku panduan User Manual. | Harian selama 3 hari masa pelatihan, rutin harian pasca go-live | Pemilik Usaha (sebagai atasan) | Panduan operasional CLI per modul, transisi status antrian pekerjaan, dan aturan pencatatan uang laci kasir. |
| **STK-009 s.d. STK-014** | Tim Pengembang AI | Input perintah prompt teknis terstruktur melalui file interface (seperti `.md` atau `.txt` dalam Workspace). | Insidental / Tiap kali iterasi coding dan penyusunan dokumen | Pemilik Usaha (sebagai Junior Programmer) | Spesifikasi arsitektur modular, skema ERD database MySQL, penggalan kode program yang error, dan instruksi penulisan. |
| **STK-015** | Pelanggan AbuCom | Salin-tempel template tautan pesan WhatsApp Web secara manual oleh staf kasir. | Insidental (Saat DP diterima, pesanan selesai siap diambil, atau retur disetujui) | Staf Kasir / Pramuniaga | Status kesiapan pengambilan pesanan cetak dan bukti nominal pembayaran DP/pelunasan. |
| **STK-016** | Vendor & Supplier | Komunikasi tatap muka / pesan WhatsApp terkait nota fisik pembelian bahan. | Insidental (Setiap pemesanan bahan baku atau pencatatan pelunasan utang usaha) | Staf Gudang | Spesifikasi kuantitas bahan yang dipesan, riwayat fluktuasi harga beli, dan pembayaran utang tempo. |
| **STK-017 s.d. STK-018** | Bank Mandiri & Bank BRI | Setoran tunai di teller / transfer aplikasi mobile banking bank resmi. | Bulanan (Sebelum tanggal jatuh tempo setoran bank) | Pemilik Usaha | Bukti pembayaran angsuran modal bulanan usaha. |
| **STK-019** | Kerabat & Keluarga | Komunikasi tatap muka personal, penyajian informal catatan saldo utang piutang. | Insidental (Setiap terjadi penarikan dana mendadak atau setoran pengembalian) | Pemilik Usaha | Laporan saldo sisa utang pinjaman keluarga secara kekeluargaan dan transparan. |

---

### 8.2. Strategi Mitigasi Resistensi

1. **Mitigasi Resistensi Staf Operasional Baru terhadap Visual CLI**:
   * **Potensi Hambatan**: Staf baru terbiasa dengan aplikasi POS berbasis visual grafis (GUI) di tablet/PC, sehingga merasa kesulitan mengoperasikan teks perintah CLI di terminal.
   * **Strategi Mitigasi**:
     * Merancang alur navigasi menu CLI yang konsisten dan menyertakan visualisasi tabel yang rapi serta penggunaan kode warna ANSI (hijau untuk sukses/selesai, kuning untuk antrian/proses, merah untuk error/DP kurang).
     * Menyusun buku *CLI User Manual* yang sangat ringkas, memuat peta jalan menu (*flowchart* menu), dan daftar perintah cepat (*hotkeys*).
     * Mengadakan program pelatihan simulasi transisi dari input Excel manual ke CLI selama 3 hari berturut-turut dengan skenario data riil sebelum go-live.
     * Mengintegrasikan sistem Poin Insentif Karyawan yang adil di dalam sistem penggajian untuk memotivasi staf melakukan entry data pemakaian bahan secara presisi guna mendapatkan bonus.

2. **Mitigasi Penarikan Dana Mendadak oleh Kerabat/Keluarga**:
   * **Potensi Hambatan**: Relasi kekeluargaan bersifat informal sehingga penarikan dana titipan bisa dilakukan kapan saja, berisiko menghentikan likuiditas modal pengembangan proyek di tengah jalan.
   * **Strategi Mitigasi**:
     * Menerapkan disiplin pemisahan keuangan: Dana cadangan darurat (*contingency fund*) sebesar **Rp 4.500.000** wajib disimpan di rekening bank terpisah yang tidak tersentuh oleh kas operasional toko.
     * Mengembangkan modul keuangan dengan fitur pencatatan saldo utang keluarga yang selalu terupdate real-time sehingga pemilik usaha dapat memberikan laporan saldo kapan saja dengan cepat.

---

## 9. Risiko Terkait Stakeholder

Berikut adalah risiko-risiko kritis yang berkaitan langsung dengan dinamika pemangku kepentingan proyek AbuCom beserta probabilitas (P: 1-5), dampak (D: 1-5), dan rencana mitigasinya.

| No | Risiko Stakeholder | P | D | Rencana Mitigasi Risiko |
|---|---|:---:|:---:|---|
| **9.1** | **Burnout Pemilik Usaha (STK-001)**: Pemilik kelelahan fisik/mental mengelola toko sendirian selama masa pengembangan, menunda ulasan dokumen/sprint. | 3 | 5 | Optimalkan penulisan kode fungsional dan dokumen SDLC menggunakan Tim AI. Sesi review bersama pemilik dibatasi maksimal 1 jam per sprint dengan agenda yang padat. |
| **9.2** | **Penarikan Dana Mendadak Kerabat (STK-019)**: Kas proyek terganggu akibat pinjaman tanpa bunga ditarik mendadak oleh keluarga. | 3 | 4 | Kunci alokasi Dana Cadangan Rp 4.500.000 khusus untuk biaya token API AI dan hardware di awal proyek, jangan dicampur dengan modal operasional harian toko. |
| **9.3** | **Kecurangan Saldo/Uang Kasir oleh Staf (STK-004)**: Karyawan melakukan penggelapan uang laci kasir atau pencatatan transaksi fiktif. | 3 | 5 | Batasi akses menu keuangan sensitif hanya untuk Pemilik (RBAC), aktifkan pencatatan Audit Trail untuk setiap edit/hapus transaksi, dan wajibkan rekonsiliasi kas harian. |
| **9.4** | **Ketidaksesuaian Literasi Digital Staf (STK-002 s.d. 008)**: Staf baru tidak mampu mengoperasikan terminal CLI teks dengan lancar. | 3 | 3 | Sediakan menu bantuan instruksi cepat di dalam CLI, buat buku panduan cetak yang sederhana, dan jalankan simulasi training 3 hari sebelum go-live. |
| **9.5** | **Keterlambatan Rekrutmen Karyawan**: Karyawan belum siap saat aplikasi selesai dikembangkan, memperpanjang burnout pemilik. | 3 | 5 | Mulai proses rekrutmen staf secara paralel pada Bulan 9-10 masa implementasi modul persediaan, sehingga proses onboarding selesai tepat waktu. |
| **9.6** | **Human Error Input Dimensi Bahan (STK-006)**: Staf produksi salah memasukkan panjang/lebar pemakaian bahan stempel, mengacaukan kalkulasi HPP. | 4 | 3 | Implementasikan regex validator pada input CLI dan tampilkan layar konfirmasi detail pemotongan bahan baku sebelum transaksi disimpan ke basis data MySQL. |
| **9.7** | **Resistensi Budaya Cross-Functional (STK-002 s.d. 008)**: Staf enggan saling membantu antar-divisi karena merasa di luar tanggung jawab aslinya. | 3 | 3 | Sosialisasikan budaya kerja saling membantu sejak masa rekrutmen, dan dukung dengan fitur perhitungan Poin Insentif transparan di aplikasi. |
| **9.8** | **Konflik Selisih Kas PC Kasir Bersama**: Beberapa staf bergantian menggunakan PC Kasir sehingga terjadi selisih uang fisik tanpa diketahui penanggung jawabnya. | 4 | 4 | Wajibkan setiap kasir melakukan login dengan akun unik masing-masing sebelum melakukan transaksi. Sistem mencatat ID User aktif pada setiap baris log Audit Trail. |
| **9.9** | **Kebocoran Data Database Pelanggan (STK-015)**: Staf menyalin file cadangan database (.sql) berisi data kontak WhatsApp pelanggan secara ilegal. | 2 | 5 | Kunci hak akses direktori penyimpanan backup database di Linux Debian 12 hanya untuk user root, serta terapkan enkripsi AES-256 pada file zip cadangan database. |
| **9.10** | **Ketidakcocokan Kode Integrasi AI (STK-009 s.d. 014)**: Junior Programmer kesulitan menggabungkan kode fungsional yang dihasilkan dari model AI yang berbeda. | 3 | 4 | Disiplin menerapkan standardisasi struktur kode di bawah arahan Lead Architect AI, lakukan review sintaksis cepat menggunakan Gemini 3 Flash sebelum integrasi. |

---

## 10. Persetujuan dan Otorisasi

Dokumen Stakeholder Register ini diajukan oleh Tim Pengembang AI dan disetujui secara formal oleh Pemilik Usaha sebagai dasar acuan tata kelola pelibatan pemangku kepentingan untuk fase SDLC selanjutnya.

| Pihak Penandatangan | Jabatan / Peran | Tanda Tangan | Tanggal Persetujuan |
|---|---|---|---|
| **Pemilik Usaha AbuCom** | Sponsor Utama Proyek | *(Menunggu Persetujuan Digital)* | *(Belum disetujui)* |
| **Pemilik Usaha AbuCom** | Manajer Proyek & Junior Programmer | *(Menunggu Persetujuan Digital)* | *(Belum disetujui)* |

---

## 11. Glosarium

Berikut adalah penjelasan istilah-istilah khusus terkait manajemen stakeholder dan domain proyek AbuCom yang digunakan dalam dokumen ini:

1. **Stakeholder**: Semua pihak (individu, kelompok, atau organisasi) yang memiliki kepentingan, dapat mempengaruhi, atau dipengaruhi oleh keputusan, aktivitas, atau hasil akhir dari suatu proyek.
2. **Stakeholder Register**: Dokumen manajemen proyek yang berisi identifikasi, analisis profil, klasifikasi, dan rencana pengelolaan strategis seluruh pemangku kepentingan.
3. **Power/Interest Grid**: Alat analisis pemetaan stakeholder yang mengelompokkan mereka berdasarkan tingkat kekuasaan (*Power*) untuk mempengaruhi hasil proyek dan tingkat kepentingan (*Interest*) terhadap proyek ke dalam 4 kuadran.
4. **Manage Closely**: Strategi pengelolaan untuk stakeholder Kuadran A (High Power/High Interest) yang membutuhkan komunikasi intensif dan pelibatan aktif dalam pengambilan keputusan.
5. **Keep Satisfied**: Strategi pengelolaan untuk stakeholder Kuadran B (High Power/Low Interest) dengan menjaga kepuasan mereka agar tidak menghambat jalannya proyek.
6. **Keep Informed**: Strategi pengelolaan untuk stakeholder Kuadran C (Low Power/High Interest) dengan memberikan informasi kemajuan secara berkala untuk menjaga dukungan mereka.
7. **Monitor**: Strategi pengelolaan untuk stakeholder Kuadran D (Low Power/Low Interest) dengan pemantauan upaya minimal terhadap perubahan sikap mereka.
8. **RACI Matrix**: Matriks yang mendefinisikan peran pemangku kepentingan terhadap aktivitas proyek menggunakan empat parameter: *Responsible* (Pelaksana), *Accountable* (Penanggung Jawab Utama), *Consulted* (Konsultan masukan), dan *Informed* (Penerima Laporan).
9. **Sponsor**: Pihak yang menyediakan pendanaan, otorisasi, serta dukungan kepemimpinan tingkat tinggi bagi keberhasilan proyek.
10. **Key User / End-User**: Pengguna utama yang akan mengoperasikan sistem secara langsung dalam aktivitas harian bisnis pasca go-live.
11. **Indirect Stakeholder**: Pemangku kepentingan yang tidak terlibat langsung dalam operasional proyek namun menerima dampak atau manfaat dari hasil akhir proyek (misal: Pelanggan).
12. **Financial Stakeholder**: Pemangku kepentingan yang mempengaruhi proyek dari aspek ketersediaan likuiditas modal pendanaan (kreditur bank atau kerabat).
13. **PKWT (Perjanjian Kerja Waktu Tertentu)**: Perjanjian kerja antara karyawan kontrak dengan pemilik usaha untuk jangka waktu tertentu.
14. **PKWTT (Perjanjian Kerja Waktu Tidak Tertentu)**: Perjanjian kerja antara karyawan tetap dengan pemilik usaha yang tidak dibatasi oleh masa berlaku kontrak.
15. **Cross-Functional**: Budaya kerjasama tim yang menuntut karyawan dari divisi yang berbeda untuk saling membantu mengisi kekosongan beban kerja demi kelancaran operasional.
16. **Burnout**: Kondisi keletihan fisik, mental, dan emosional yang ekstrem akibat stres berkepanjangan (dalam konteks ini dialami pemilik usaha akibat mengelola 5 divisi sendirian secara manual).
17. **Role-Based Access Control (RBAC)**: Mekanisme pembatasan hak akses menu aplikasi berdasarkan peran (*role*) yang diberikan kepada pengguna (misal: menu Pemilik vs menu Staf).
18. **Audit Trail**: Catatan log kronologis yang merekam riwayat seluruh aktivitas perubahan data sensitif di database MySQL untuk mencegah kecurangan (*fraud*).
19. **UU PDP (Undang-Undang Pelindungan Data Pribadi)**: UU No. 27 Tahun 2022 di Indonesia yang mengatur perlindungan data pribadi subjek data dari kebocoran atau penyalahgunaan.

---

## 12. Referensi Dokumen

| # | Nama File | Lokasi Path Relatif | Keterangan Penggunaan |
|---|---|---|---|
| 1 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Referensi utama (primer) data tim pengembang AI, struktur organisasi staf, risiko awal, dan RACI awal. |
| 2 | `02_feasibility_study.md` | `docs/sdlc/01_planning/02_feasibility_study.md` | Referensi sekunder data kesiapan rekrutmen staf baru, literasi digital, aspek hukum UU PDP, PKWT/PKWTT, dan mitigasi risiko operasional. |
| 3 | `narasi.txt` | `docs/sdlc/narasi.txt` | Referensi pendukung konteks hubungan personal pemilik dengan kerabat pemberi pinjaman, kondisi emosional pemilik (*burnout*), dan harapan RBAC data sensitif. |
