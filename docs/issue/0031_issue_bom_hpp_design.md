---
judul      : Penyusunan Dokumen BOM & HPP Design (05_bom_hpp_design.md)
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
target     : docs/sdlc/03_design/05_bom_hpp_design.md
prioritas  : High
status     : Open
dibuat     : 2026-05-24
persona    : Senior Manufacturing Systems Architect & Cost Accounting Specialist
---

# Penyusunan Dokumen BOM & HPP Design

## 1. Ringkasan Tugas

Buatlah dokumen desain teknis komprehensif berjudul **BOM & HPP Design** yang menjabarkan seluruh arsitektur, logika kalkulasi, alur data, dan spesifikasi implementasi modul **Bill of Materials (BOM)** dan **Harga Pokok Penjualan (HPP)** pada sistem AbuCom. Dokumen ini merupakan deliverable kelima pada **Fase 03 Design** dan menjadi panduan mutlak bagi tim pengembang dalam mengimplementasikan fitur inti perhitungan biaya produksi cetak kustom berbasis presisi desimal.

---

## 2. Persona Pelaksana

**Senior Manufacturing Systems Architect & Cost Accounting Specialist** — Seorang ahli perancangan sistem manufaktur yang menguasai secara mendalam konsep Bill of Materials (BOM), kalkulasi Harga Pokok Penjualan (HPP), manajemen inventaris presisi desimal, dan integrasi alur produksi ke pencatatan keuangan. Persona ini memiliki otoritas penuh dalam menentukan formula kalkulasi biaya, skema dekomposisi komponen bahan baku, dan alur pemotongan stok transaksional.

---

## 3. Daftar File Referensi Wajib

Sebelum memulai penyusunan dokumen, Anda **WAJIB** membaca, merangkum, dan memahami secara menyeluruh setiap detail dari file-file referensi berikut. Jangan ada satupun informasi yang terlewat.

| No | File Referensi | Path Relatif | Alasan Pemilihan |
|:--:|:--|:--|:--|
| 1 | **Database Schema (DDL SQL)** | `docs/sdlc/03_design/01_database_schema.sql` | Sumber kebenaran tunggal (SSoT) untuk struktur fisik tabel `bom_komposisi`, `barang`, `detail_transaksi`, `transaksi`, `limbah_produksi`, `pengeluaran`, dan seluruh constraint, foreign key, serta tipe data `DECIMAL(15,4)` yang menjadi fondasi kalkulasi HPP. |
| 2 | **ERD Database** | `docs/sdlc/03_design/02_erd_database.md` | Peta visual relasi antar-entitas, khususnya pola **self-referencing FK** pada `barang` → `bom_komposisi` (barang_induk_id & bahan_baku_id merujuk ke tabel `barang` yang sama), unique constraint komposit, dan kebijakan CASCADE/RESTRICT. |
| 3 | **System Architecture** | `docs/sdlc/03_design/03_system_architecture.md` | Arsitektur teknis keseluruhan sistem: paradigma Functional Programming (FP) murni, pola State Dictionary Passing, struktur layer (Presentation → Logic → Data Access), dan konvensi penulisan pure functions yang wajib diterapkan pada logika BOM/HPP. |
| 4 | **CLI Interaction Flow** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur interaksi pengguna pada menu MENU-M2-002 (Hitung HPP BOM Desimal), MENU-M2-003 (Limbah Produksi), serta integrasi BOM ke alur transaksi cetak kustom (UC-001 → UC-007). Khususnya Bab 6.1 dan Bab 6.2. |
| 5 | **Software Requirements Specification** | `docs/sdlc/02_analysis/02_software_requirements.md` | Spesifikasi fungsional SRS-F-007 (HPP BOM Desimal), SRS-F-008 (Limbah), SRS-F-005 (Margin Produk), SRS-F-009 (UoM), SRS-F-010 (Sinkronisasi ATK), wireframe BOM, formula matematika HPP, aturan validasi, dan penanganan exception. |
| 6 | **Workflow Diagram** | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Diagram alur kerja WF-M2-01 (HPP BOM Desimal), WF-M2-02 (Limbah), WF-M2-04 (Sinkronisasi ATK), WF-CROSS-01 (Alur Cetak Kustom Lintas Modul), dan narasi prosedural step-by-step. |
| 7 | **Narasi Operasional Pemilik** | `docs/sdlc/narasi.txt` | Konteks bisnis asli dari pemilik usaha, khususnya poin tentang: komposisi bahan baku (contoh stempel flash: gagang + tinta + kertas buffalo + karet flash), kebutuhan pemakaian stok berdasarkan satuan dimensi (panjang × lebar) atau volume, dan integrasi stok ATK retail untuk produksi internal. |

---

## 4. Instruksi Pengerjaan Detail

Kerjakan setiap langkah di bawah ini secara berurutan. Gunakan format checklist markdown (`- [ ]`) untuk setiap sub-langkah agar progres pengerjaan dapat dilacak.

---

### Langkah 1 — Baca dan Rangkum Seluruh File Referensi

- [ ] Buka dan baca file `docs/sdlc/03_design/01_database_schema.sql` secara lengkap dari baris pertama hingga baris terakhir.
- [ ] Rangkum secara detail struktur tabel-tabel berikut beserta seluruh kolom, tipe data, constraint, foreign key, dan comment-nya:
  - [ ] Tabel `barang` (TABEL 05): perhatikan kolom `tipe_barang` ('Retail_ATK' | 'Bahan_Baku'), `stok_saat_ini` DECIMAL(15,4), `harga_beli` DECIMAL(15,4), `satuan_uom`, dan constraint CHECK.
  - [ ] Tabel `bom_komposisi` (TABEL 09): perhatikan kolom `barang_induk_id`, `bahan_baku_id`, `kuantitas_desimal` DECIMAL(15,4), unique constraint `uq_bom_komposisi_induk_bahan`, dan kebijakan ON DELETE CASCADE pada `barang_induk_id` vs ON DELETE RESTRICT pada `bahan_baku_id`.
  - [ ] Tabel `detail_transaksi` (TABEL 11): perhatikan kolom `subtotal` DECIMAL(15,4), `harga_jual`, `kuantitas`, dan relasi ke `barang` dan `transaksi`.
  - [ ] Tabel `transaksi` (TABEL 10): perhatikan kolom `total_bayar`, `dp_bayar`, `status_pembayaran`, dan constraint `chk_transaksi_dp_bayar`.
  - [ ] Tabel `limbah_produksi`: perhatikan kolom kuantitas limbah, biaya kerugian, alasan kerusakan, dan relasi ke `bom_komposisi` dan `barang`.
  - [ ] Tabel `pengeluaran`: perhatikan kolom `tipe_pengeluaran`, `nominal`, dan `disetujui_pemilik` untuk pencatatan biaya limbah sebagai OPEX.
- [ ] Buka dan baca file `docs/sdlc/03_design/02_erd_database.md` secara lengkap.
- [ ] Rangkum pola **self-referencing FK** pada `barang` → `bom_komposisi`, termasuk diagram Mermaid ER dan tabel matriks foreign key (baris 8, 9, 10 dari matriks FK).
- [ ] Buka dan baca file `docs/sdlc/03_design/03_system_architecture.md` secara lengkap.
- [ ] Rangkum arsitektur layer yang relevan: pola pure function untuk logika kalkulasi BOM/HPP, konvensi State Dictionary Passing, dan penempatan modul di `logic/bom_hpp.py`.
- [ ] Buka dan baca file `docs/sdlc/03_design/04_cli_interaction_flow.md` Bab 6.1 (baris 697-724) dan Bab 6.2 (baris 726-753) secara lengkap.
- [ ] Rangkum 8 langkah interaksi CLI pada menu Hitung HPP BOM (MENU-M2-002) dan 11 langkah pada menu Limbah Produksi (MENU-M2-003).
- [ ] Buka dan baca file `docs/sdlc/02_analysis/02_software_requirements.md` Bagian SRS-F-007 (baris 352-384) dan SRS-F-008 (baris 388-418) secara lengkap.
- [ ] Rangkum formula matematika HPP: `Biaya Komponen = kuantitas_pemakaian × harga_beli_satuan` dan `HPP Produk = Σ(Biaya Komponen)`.
- [ ] Rangkum aturan validasi: wajib `decimal.Decimal` Python, dilarang `float`, kuantitas harus positif > 0, dan penanganan stok minus (tetap proses + alert kuning).
- [ ] Buka dan baca file `docs/sdlc/02_analysis/04_workflow_diagram.md` Bagian WF-M2-01 (baris 524-548) secara lengkap.
- [ ] Rangkum 5 langkah prosedural narasi alur HPP BOM dari trigger status antrian → fetch BOM → hitung HPP → simpan → potong stok.
- [ ] Buka dan baca file `docs/sdlc/narasi.txt` secara lengkap (115 baris).
- [ ] Rangkum poin-poin spesifik BOM/HPP dari narasi pemilik: komposisi bahan baku stempel (gagang + karet flash + tinta + kertas buffalo), pemakaian berdasarkan dimensi panjang × lebar atau volume, kebutuhan integrasi stok ATK retail ↔ produksi, dan kebutuhan presisi desimal.

---

### Langkah 2 — Ekstraksi Data yang Relevan dengan BOM & HPP

Dari rangkuman Langkah 1, ambil **HANYA** data dan informasi yang secara langsung berkaitan dengan topik BOM dan HPP. Abaikan informasi yang tidak relevan (misalnya: PPOB, e-wallet, payroll, CRM, dsb.). Data yang harus diekstrak meliputi:

- [ ] **Struktur data BOM**: Definisi tabel `bom_komposisi` lengkap, relasi self-referencing ke `barang`, unique constraint, dan kebijakan FK.
- [ ] **Struktur data HPP**: Kolom-kolom terkait HPP di `barang` (`harga_beli`), `detail_transaksi` (`subtotal`, `harga_jual`), dan bagaimana nilai HPP disimpan.
- [ ] **Formula kalkulasi**: Rumus matematika perhitungan biaya komponen dan HPP total produk kustom.
- [ ] **Alur trigger HPP**: Kapan dan bagaimana proses HPP dipicu (status antrian cetak kustom → 'Selesai' → auto-compute HPP).
- [ ] **Mekanisme pemotongan stok desimal**: Query UPDATE yang memotong `stok_saat_ini` di tabel `barang` secara transaksional.
- [ ] **Integrasi limbah produksi**: Bagaimana limbah bahan baku (waste) tercatat, mengurangi stok, dan terbukukan sebagai OPEX di tabel `pengeluaran`.
- [ ] **Integrasi sinkronisasi ATK**: Bagaimana barang retail ATK (`tipe_barang = 'Retail_ATK'`) diambil untuk produksi internal dan dicatat sebagai pengeluaran operasional.
- [ ] **Integrasi margin produk**: Bagaimana HPP BOM digunakan untuk menghitung margin keuntungan kotor: `Margin (%) = ((Harga Jual - HPP) / Harga Jual) × 100`.
- [ ] **Integrasi laporan laba/rugi**: Bagaimana HPP BOM masuk ke komponen biaya dalam laporan keuangan: `Laba Kotor = Total Pendapatan - Total HPP`.
- [ ] **Aturan presisi desimal**: Kewajiban penggunaan `DECIMAL(15,4)` di MySQL dan `decimal.Decimal` di Python, larangan `float`.
- [ ] **Contoh produk nyata**: Data contoh stempel flash (gagang, karet, tinta), buku yasin (kertas, tinta, lem, cover), dan produk kustom lain dari narasi.

---

### Langkah 3 — Susun Struktur Dokumen

Susun dokumen `05_bom_hpp_design.md` dengan struktur berikut. Setiap bagian harus ditulis secara komprehensif, detail, dan tidak ambigu.

- [ ] **Header Metadata YAML**: Sama dengan format dokumen design lain (`dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`).
- [ ] **Judul Dokumen**: `BOM & HPP Design — AbuCom`
- [ ] **Riwayat Perubahan Dokumen**: Tabel versi 1.0 dengan deskripsi pembuatan awal.

#### Bagian 1 — Informasi Dokumen
- [ ] Tujuan Dokumen: Jelaskan bahwa dokumen ini menjabarkan seluruh arsitektur, formula, alur data, dan spesifikasi teknis modul BOM & HPP.
- [ ] Cakupan Dokumen: Sebutkan secara spesifik apa saja yang dicakup (definisi BOM, formula HPP, alur data, skema database, aturan validasi, integrasi antar-modul, dll.).
- [ ] Posisi Dokumen dalam Siklus SDLC: Deliverable ke-5 pada Fase 03 Design, setelah CLI Interaction Flow.
- [ ] Hubungan dengan Dokumen SDLC Lainnya: Sebutkan dokumen input (SRS, WFD, DB Schema, ERD, System Architecture, CLI Flow) dan dokumen output (Implementation Code, Test Plan).
- [ ] Audiens Target: Developer/AI Coding Agent, QA Team, Pemilik Usaha.
- [ ] Definisi, Akronim, dan Singkatan: BOM, HPP, UoM, COGS, FP, SSoT, ACID, FK, dsb.

#### Bagian 2 — Konsep Dasar BOM & HPP
- [ ] Definisi Bill of Materials (BOM): Jelaskan konsep BOM sebagai daftar komposisi bahan baku pembentuk satu unit produk cetak kustom. Gunakan analogi dan contoh nyata dari operasional toko AbuCom.
- [ ] Definisi Harga Pokok Penjualan (HPP): Jelaskan konsep HPP sebagai total biaya modal produksi riil yang dihitung dari penjumlahan seluruh biaya komponen BOM.
- [ ] Hubungan BOM ↔ HPP: Jelaskan bahwa BOM adalah **input** dan HPP adalah **output** dari proses kalkulasi biaya produksi.
- [ ] Klasifikasi Barang dalam Konteks BOM:
  - [ ] `Barang Induk` (Produk Jadi Kustom): Produk akhir yang dijual ke pelanggan (stempel flash, buku yasin, undangan, baliho, dll.). Tipe = entri pada `barang` yang memiliki child di `bom_komposisi`.
  - [ ] `Bahan Baku` (Komponen Pembentuk): Material mentah yang dikonsumsi dalam proses produksi (karet flash, gagang stempel, tinta, kertas, lem, dll.). Tipe = `'Bahan_Baku'` pada kolom `tipe_barang` di tabel `barang`.
  - [ ] `Retail ATK` (Dual-Purpose): Barang retail yang juga dapat digunakan sebagai bahan baku produksi internal (kertas HVS, tinta printer, dll.). Tipe = `'Retail_ATK'` pada kolom `tipe_barang`.

#### Bagian 3 — Skema Database BOM & HPP
- [ ] Diagram ER Fokus BOM: Buat diagram Mermaid ER yang memvisualisasikan **hanya** entitas dan relasi yang relevan dengan BOM & HPP (`barang`, `bom_komposisi`, `detail_transaksi`, `transaksi`, `limbah_produksi`, `pengeluaran`).
- [ ] DDL Tabel `bom_komposisi`: Salin definisi lengkap CREATE TABLE dari database schema, sertakan penjelasan detail setiap kolom, constraint, dan foreign key.
- [ ] DDL Tabel `barang` (kolom relevan BOM): Salin kolom-kolom yang relevan (`harga_beli`, `stok_saat_ini`, `tipe_barang`, `satuan_uom`), jelaskan peran masing-masing dalam konteks BOM.
- [ ] Penjelasan Self-Referencing FK: Jelaskan pola di mana `bom_komposisi.barang_induk_id` dan `bom_komposisi.bahan_baku_id` keduanya merujuk ke `barang.id` — ini memungkinkan satu produk kustom memiliki banyak komponen bahan baku dari tabel master barang yang sama.
- [ ] Kebijakan CASCADE vs RESTRICT: Jelaskan mengapa `barang_induk_id` menggunakan ON DELETE CASCADE (hapus BOM jika produk dihapus) sedangkan `bahan_baku_id` menggunakan ON DELETE RESTRICT (lindungi bahan baku yang masih digunakan dalam formula BOM aktif).
- [ ] Unique Constraint Komposit: Jelaskan `uq_bom_komposisi_induk_bahan` yang mencegah duplikasi bahan baku yang sama untuk satu produk kustom.

#### Bagian 4 — Formula dan Logika Kalkulasi HPP
- [ ] Formula Biaya per Komponen: Jabarkan rumus `Biaya Komponen = kuantitas_desimal × harga_beli` dengan penjelasan setiap variabel.
- [ ] Formula HPP Total Produk: Jabarkan rumus `HPP Produk = Σ(Biaya Komponen)` sebagai penjumlahan seluruh biaya komponen bahan dalam satu BOM.
- [ ] Contoh Kalkulasi Numerik Stempel Flash:
  - [ ] Komponen 1: Karet Flash — dimensi 0.05m × 0.05m = 0.0025 m², harga Rp 100.000/m² → Biaya = Rp 250.
  - [ ] Komponen 2: Gagang Stempel — 1 Pcs, harga Rp 4.500/Pcs → Biaya = Rp 4.500.
  - [ ] HPP Total = Rp 250 + Rp 4.500 = Rp 4.750.
- [ ] Contoh Kalkulasi Numerik Buku Yasin (buat contoh realistis berdasarkan konteks percetakan).
- [ ] Presisi Desimal: Jelaskan secara tegas bahwa semua operasi aritmatika **WAJIB** menggunakan `decimal.Decimal` di Python dan `DECIMAL(15,4)` di MySQL. Berikan contoh kode pseudocode FP murni.
- [ ] Formula Margin Keuntungan: Jabarkan rumus `Margin (%) = ((Harga Jual - HPP) / Harga Jual) × 100` dan bagaimana HPP BOM digunakan dalam perhitungan margin per produk (SRS-F-005).

#### Bagian 5 — Alur Data dan Proses BOM & HPP
- [ ] Diagram Alur Utama (Mermaid Flowchart): Buat diagram yang menggambarkan alur end-to-end dari pendaftaran BOM hingga HPP tercatat di laporan keuangan.
- [ ] Alur 1 — Pendaftaran Formula BOM Baru:
  - [ ] Aktor: `pemilik` atau `kepala_percetakan`.
  - [ ] Input: `barang_induk_id`, daftar `bahan_baku_id` + `kuantitas_desimal`.
  - [ ] Proses: INSERT ke `bom_komposisi` dengan validasi unique constraint.
  - [ ] Output: Formula BOM tersimpan dan siap digunakan untuk kalkulasi HPP.
- [ ] Alur 2 — Kalkulasi HPP saat Produksi Selesai (Trigger Utama):
  - [ ] Trigger: Status antrian cetak kustom diubah ke `'Selesai'` oleh staf `produksi_cetak`.
  - [ ] Proses: Sistem auto-fetch BOM → query harga beli → hitung HPP desimal → simpan ke detail transaksi → potong stok bahan baku.
  - [ ] Buat Sequence Diagram Mermaid yang menggambarkan interaksi antar-komponen (CLI → Logic Layer → Database).
- [ ] Alur 3 — Pemotongan Stok Bahan Baku Desimal:
  - [ ] Query: `UPDATE barang SET stok_saat_ini = stok_saat_ini - %s WHERE id = %s`.
  - [ ] Jelaskan bahwa pemotongan dilakukan di dalam blok `START TRANSACTION ... COMMIT` MySQL InnoDB untuk menjamin atomicity.
  - [ ] Penanganan stok minus: jika `stok_saat_ini` menjadi negatif, proses tetap dilanjutkan tetapi sistem wajib mencatat status minus dan menampilkan alert visual kuning di CLI.
- [ ] Alur 4 — Pencatatan Limbah Produksi (Waste):
  - [ ] Input: `transaksi_id`, `bahan_baku_id`, `kuantitas_limbah`, `alasan_kerusakan`.
  - [ ] Proses: hitung biaya kerugian → potong stok → catat ke `limbah_produksi` → bukukan OPEX ke `pengeluaran`.
  - [ ] Relasi ke BOM: limbah hanya boleh dicatat untuk bahan baku yang terdaftar di komponen BOM pesanan terkait.
- [ ] Alur 5 — Sinkronisasi ATK Internal:
  - [ ] Proses: ambil barang retail ATK untuk keperluan produksi → potong stok ATK → catat HPP ATK sebagai pengeluaran operasional.
  - [ ] Jelaskan perbedaan alur ini dengan alur BOM biasa (ATK bukan bagian dari formula BOM, melainkan pengambilan ad-hoc).

#### Bagian 6 — Aturan Validasi dan Penanganan Exception
- [ ] Tabel aturan validasi input:
  - [ ] `kuantitas_desimal` HARUS > 0.
  - [ ] `bahan_baku_id` HARUS terdaftar di tabel `barang` dengan `tipe_barang` = 'Bahan_Baku' atau 'Retail_ATK'.
  - [ ] `barang_induk_id` HARUS merujuk ke produk kustom yang valid.
  - [ ] Kombinasi (`barang_induk_id`, `bahan_baku_id`) HARUS unik (enforced by DB constraint).
  - [ ] Semua input numerik HARUS divalidasi ke format `decimal.Decimal` sebelum proses.
- [ ] Tabel kode error:
  - [ ] `ERR-VAL-007`: Input kuantitas bahan baku tidak valid (bukan angka positif).
  - [ ] `ERR-VAL-008`: ID bahan baku tidak valid untuk transaksi pesanan kustom ini.
  - [ ] `ERR-STOCK-010`: Stok bahan baku tidak mencukupi (alert kuning, proses tetap jalan).
  - [ ] `ERR-DB-007`: Kegagalan koneksi database saat proses kalkulasi HPP.
- [ ] Penanganan stok negatif: Dokumentasikan bahwa sistem **TIDAK** menolak proses jika stok menjadi minus — sistem tetap memproses tetapi wajib mencatatkan status stok negatif dan menampilkan peringatan visual.

#### Bagian 7 — Integrasi Lintas Modul
- [ ] Diagram Integrasi BOM/HPP (Mermaid): Buat diagram yang menggambarkan bagaimana modul BOM/HPP terhubung dengan modul lain.
- [ ] Integrasi ke M.1 Transaksi: Saat transaksi cetak kustom dibuat, item barang kustom di keranjang belanja memicu kalkulasi HPP BOM saat status produksi selesai.
- [ ] Integrasi ke M.5 Antrian: Status antrian `'Selesai'` menjadi trigger utama proses kalkulasi HPP dan pemotongan stok.
- [ ] Integrasi ke M.1 Margin Produk (SRS-F-005): Nilai HPP BOM digunakan untuk menghitung margin keuntungan kotor per produk di menu Pemilik.
- [ ] Integrasi ke M.6 Laporan Laba/Rugi (SRS-F-028): Total HPP BOM dan biaya limbah menjadi komponen pengurang pendapatan dalam laporan keuangan.
- [ ] Integrasi ke M.7 Audit Trail: Setiap operasi BOM (create/update/delete formula, kalkulasi HPP, pencatatan limbah) wajib direkam ke `audit_logs` dengan old_value/new_value.
- [ ] Integrasi ke Multi-Cabang (M.9): Setiap baris `bom_komposisi` memiliki `cabang_id`, memungkinkan formula BOM berbeda per cabang di masa depan.

#### Bagian 8 — Spesifikasi Implementasi Teknis
- [ ] Penempatan Modul: `logic/bom_hpp.py` sebagai lokasi pure functions kalkulasi BOM/HPP sesuai System Architecture.
- [ ] Paradigma FP Murni: Semua fungsi kalkulasi HPP WAJIB ditulis sebagai pure functions (tanpa side effects, tanpa mutasi state global), menggunakan `tuples`/`namedtuples` untuk imutabilitas data.
- [ ] Pseudocode Pure Function: Tulis pseudocode untuk fungsi-fungsi utama:
  - [ ] `hitung_biaya_komponen(kuantitas_desimal, harga_beli_satuan) → Decimal`
  - [ ] `hitung_hpp_produk(daftar_komponen) → Decimal`
  - [ ] `proses_pemotongan_stok(daftar_komponen, connection) → Result`
  - [ ] `proses_limbah_produksi(transaksi_id, bahan_baku_id, kuantitas_limbah, alasan, connection) → Result`
- [ ] Konfigurasi Runtime: Dokumentasikan parameter `system_configs` yang relevan dengan BOM/HPP (jika ada, misalnya: toleransi stok minus, ambang batas re-order HPP, dll.).

#### Bagian 9 — Matriks Ketertelusuran (Traceability Matrix)
- [ ] Tabel pemetaan Use Case ↔ SRS ↔ Workflow ↔ CLI Flow ↔ Bagian Dokumen ini:
  - [ ] UC-007 ↔ SRS-F-007 ↔ WF-M2-01 ↔ Bab 6.1 CLI ↔ Bagian 4, 5.
  - [ ] UC-008 ↔ SRS-F-008 ↔ WF-M2-02 ↔ Bab 6.2 CLI ↔ Bagian 5.4.
  - [ ] UC-005 ↔ SRS-F-005 ↔ WF-M1-05 ↔ Bab 5.5 CLI ↔ Bagian 4.6, 7.
  - [ ] UC-009 ↔ SRS-F-009 ↔ WF-M2-03 ↔ Bab 6.3 CLI ↔ Bagian 2.4.
  - [ ] UC-010 ↔ SRS-F-010 ↔ WF-M2-04 ↔ Bab 6.4 CLI ↔ Bagian 5.5.

#### Bagian 10 — Glosarium
- [ ] Definisi istilah teknis yang digunakan dalam dokumen: BOM, HPP, COGS, UoM, FP, SSoT, ACID, FK, Self-Referencing, OPEX, Decimal Precision, Fixed-Point Arithmetic, Pure Function, State Dictionary, dll.

---

### Langkah 4 — Penulisan Konten Dokumen

- [ ] Tulis konten untuk **setiap bagian** yang telah didefinisikan di Langkah 3, satu per satu secara berurutan.
- [ ] Pastikan setiap klaim, angka, nama kolom, nama tabel, tipe data, dan constraint yang ditulis **benar-benar sesuai** dengan data di file referensi. Jangan mengarang data yang tidak ada di referensi.
- [ ] Gunakan bahasa Indonesia yang natural, formal, dan tidak ambigu.
- [ ] Sertakan diagram Mermaid (ER Diagram, Flowchart, Sequence Diagram) di bagian yang membutuhkan visualisasi.
- [ ] Sertakan contoh kalkulasi numerik yang realistis berdasarkan konteks usaha percetakan AbuCom.
- [ ] Gunakan format tabel markdown untuk data terstruktur (definisi kolom, matriks validasi, kode error, traceability).

---

### Langkah 5 — Validasi Silang (Cross-Validation)

Setelah dokumen selesai ditulis, lakukan validasi silang berikut:

- [ ] Pastikan setiap nama tabel yang disebutkan dalam dokumen **ADA** di `01_database_schema.sql`.
- [ ] Pastikan setiap nama kolom yang disebutkan dalam dokumen **COCOK PERSIS** dengan definisi di `01_database_schema.sql` (case-sensitive, termasuk underscore).
- [ ] Pastikan setiap tipe data yang disebutkan (misalnya `DECIMAL(15,4)`, `VARCHAR(20)`, `INT`) **SESUAI** dengan DDL aktual.
- [ ] Pastikan setiap foreign key constraint yang disebutkan **BENAR** nama dan target-nya.
- [ ] Pastikan setiap kode SRS (SRS-F-007, dll.) yang direferensikan **ADA** di `02_software_requirements.md`.
- [ ] Pastikan setiap kode UC (UC-007, dll.) yang direferensikan **KONSISTEN** dengan dokumen UCD dan CLI Flow.
- [ ] Pastikan setiap kode WF (WF-M2-01, dll.) yang direferensikan **ADA** di `04_workflow_diagram.md`.
- [ ] Pastikan formula matematika HPP **IDENTIK** dengan yang ada di SRS-F-007.
- [ ] Pastikan tidak ada informasi yang **BERTENTANGAN** antar-referensi (jika ada, prioritaskan Database Schema sebagai SSoT).

---

### Langkah 6 — Finalisasi dan Penulisan File

- [ ] Tulis seluruh konten dokumen final ke file target: `docs/sdlc/03_design/05_bom_hpp_design.md`.
- [ ] Pastikan file menggunakan encoding UTF-8.
- [ ] Pastikan format markdown valid dan dapat di-render dengan benar.
- [ ] Pastikan semua diagram Mermaid memiliki sintaks yang valid.

---

## 5. Aturan dan Batasan Pengerjaan

| No | Aturan | Penjelasan |
|:--:|:--|:--|
| 1 | **Dilarang Mengarang Data** | Seluruh informasi (nama tabel, nama kolom, tipe data, constraint, formula, kode error) HARUS bersumber dari file referensi yang sudah ditentukan. Jangan membuat data fiktif. |
| 2 | **Database Schema adalah SSoT** | Jika terjadi kontradiksi antara file referensi, prioritaskan `01_database_schema.sql` sebagai sumber kebenaran tunggal untuk aspek struktur data. |
| 3 | **Presisi Desimal Wajib** | Setiap kali menyebut tipe data numerik keuangan atau stok, gunakan `DECIMAL(15,4)` (MySQL) dan `decimal.Decimal` (Python). Jangan pernah menyebutkan `float` atau `double`. |
| 4 | **Paradigma FP Murni** | Semua pseudocode dan contoh logika kalkulasi WAJIB mengikuti paradigma Functional Programming murni: pure functions, tanpa class/OOP, immutable data. |
| 5 | **Bahasa Indonesia** | Seluruh dokumen ditulis dalam bahasa Indonesia yang natural dan formal. Istilah teknis boleh dalam bahasa Inggris jika sudah lazim (BOM, HPP, DECIMAL, Foreign Key, dsb.). |
| 6 | **Format Checklist** | Gunakan format checklist markdown (`- [ ]`) untuk langkah-langkah prosedural dalam dokumen. |
| 7 | **Jangan Interupsi Alur SDLC** | Jangan menambahkan fitur, tabel, kolom, atau logika baru yang tidak ada di file referensi. Dokumen ini adalah **desain berdasarkan spesifikasi yang sudah ada**, bukan perancangan baru. |
| 8 | **Multi-Cabang Ready** | Setiap kali menjelaskan skema data, selalu sertakan konteks `cabang_id` sebagai filter multi-cabang. |

---

## 6. Kriteria Penerimaan (Definition of Done)

- [ ] File `docs/sdlc/03_design/05_bom_hpp_design.md` sudah terisi lengkap dengan seluruh 10 bagian.
- [ ] Setiap diagram Mermaid (ER, Flowchart, Sequence) valid dan dapat di-render.
- [ ] Setiap nama tabel, kolom, tipe data, dan constraint sudah divalidasi silang terhadap Database Schema.
- [ ] Setiap referensi SRS, UC, dan WF sudah diverifikasi keberadaannya di dokumen asli.
- [ ] Formula HPP identik dengan SRS-F-007.
- [ ] Contoh kalkulasi numerik stempel flash menghasilkan HPP = Rp 4.750 (sesuai wireframe SRS).
- [ ] Dokumen ditulis dalam bahasa Indonesia yang natural, formal, dan tidak ambigu.
- [ ] Tidak ada data yang dikarang/dihalusinasi — seluruhnya bersumber dari file referensi.
