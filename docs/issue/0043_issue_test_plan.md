# Pembuatan & Penyusunan Dokumen Test Plan

---

| Atribut         | Nilai                                                                      |
|-----------------|----------------------------------------------------------------------------|
| **Judul**       | Pembuatan & Penyusunan Dokumen Test Plan — AbuCom                          |
| **Dokumen Utama** | Test Plan                                                                |
| **Target File** | `docs/sdlc/05_testing/01_test_plan.md`                                     |
| **Prioritas**   | High                                                                       |
| **Status**      | Open                                                                       |
| **Tanggal**     | 2026-05-26                                                                 |
| **Persona**     | **Senior QA Lead & Test Strategy Architect**                               |

---

## 1. Deskripsi Issue

Issue ini menginstruksikan pembuatan dan penyusunan dokumen **Test Plan** secara lengkap, komprehensif, dan sesuai standar praktik industri (mengacu pada **IEEE 829** / **ISO/IEC/IEEE 29119**). Dokumen Test Plan merupakan deliverable pertama pada **Fase 05 — Testing** dalam siklus SDLC proyek AbuCom. Dokumen ini berperan sebagai cetak biru strategi pengujian menyeluruh yang akan menjadi acuan utama bagi pembuatan test cases, test scripts, dan laporan hasil pengujian pada fase selanjutnya.

---

## 2. Persona yang Ditugaskan

**Persona**: `Senior QA Lead & Test Strategy Architect`

**Justifikasi Pemilihan Persona**:
- Persona ini memiliki otoritas dan kompetensi tertinggi dalam merancang strategi pengujian perangkat lunak yang mencakup seluruh aspek fungsional, non-fungsional, keamanan, performa, dan kepatuhan regulasi.
- Persona ini mampu memetakan seluruh kebutuhan fungsional (SRS-F-001 s.d SRS-F-040+) dan non-fungsional (SRS-NF-001 s.d SRS-NF-011) menjadi skenario pengujian terstruktur yang dapat dieksekusi oleh QA Engineer junior.
- Persona ini memahami konteks arsitektur Client-Server LAN offline, paradigma Functional Programming (FP) murni, presisi desimal keuangan, dan keamanan RBAC/JWT/bcrypt yang menjadi ciri khas unik sistem AbuCom.

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **WAJIB** dibaca dan dirangkum secara menyeluruh sebagai dasar utama penyusunan dokumen Test Plan. Urutan pembacaan disusun berdasarkan prioritas relevansi terhadap dokumen Test Plan:

### 3.1. Referensi PRIMER (Wajib Dibaca Penuh — Setiap Detail)

| No | Kode Ref | Nama Dokumen | Path File | Justifikasi |
|----|----------|--------------|-----------|-------------|
| R-01 | SRS v1.1 | Software Requirements Specification | `docs/sdlc/02_analysis/02_software_requirements.md` | Sumber utama seluruh kebutuhan fungsional (SRS-F-001 s.d SRS-F-040+), kebutuhan non-fungsional (SRS-NF-001 s.d SRS-NF-011), kode error, dan aturan validasi yang menjadi basis test case. |
| R-02 | UCD v1.1 | Use Case Diagram | `docs/sdlc/02_analysis/03_use_case_diagram.md` | Sumber 44 use case (UC-001 s.d UC-044) beserta alur utama (Main Flow), alur alternatif (Alternative Flow), dan alur pengecualian (Exception Flow) yang menjadi basis skenario pengujian fungsional. |
| R-03 | ACM v1.1 | Access Control Matrix | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Sumber matriks otorisasi RBAC granular 8 peran terhadap 44 use case dan 28 tabel CRUD, eskalasi supervisor, dan rate limiting untuk pengujian keamanan. |
| R-04 | SecDes v1.1 | Security Design | `docs/sdlc/03_design/06_security_design.md` | Sumber spesifikasi teknis keamanan (bcrypt, JWT, RBAC, sanitasi CLI, audit trail, UU PDP, threat model) untuk pengujian penetrasi dan kepatuhan. |

### 3.2. Referensi SEKUNDER (Wajib Dibaca — Fokus pada Bagian yang Relevan)

| No | Kode Ref | Nama Dokumen | Path File | Justifikasi |
|----|----------|--------------|-----------|-------------|
| R-05 | SysArch v1.1 | System Architecture | `docs/sdlc/03_design/03_system_architecture.md` | Arsitektur 4-layer, topologi LAN, connection pooling, retry mechanism, presisi desimal, dan ACID transactions untuk pengujian integrasi dan performa. |
| R-06 | DDL v1.1 | Database Schema | `docs/sdlc/03_design/01_database_schema.sql` | Skema fisik 28 tabel InnoDB, constraint CHECK, foreign key, dan tipe data DECIMAL(15,4) untuk pengujian integritas data dan database. |
| R-07 | ERD v1.1 | ERD Database | `docs/sdlc/03_design/02_erd_database.md` | Relasi visual 58 foreign key dan kardinalitas untuk validasi referensial integritas. |
| R-08 | BOM v1.1 | BOM & HPP Design | `docs/sdlc/03_design/05_bom_hpp_design.md` | Formula kalkulasi HPP desimal, limbah, dan sinkronisasi ATK untuk pengujian presisi aritmatika. |
| R-09 | CLI v1.1 | CLI Interaction Flow | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur navigasi menu terminal, konvensi visual rich/tabulate, dan kode error untuk pengujian antarmuka pengguna. |

### 3.3. Referensi TERSIER (Dibaca Seperlunya — Data Pendukung)

| No | Kode Ref | Nama Dokumen | Path File | Justifikasi |
|----|----------|--------------|-----------|-------------|
| R-10 | CodStd v1.1 | Coding Standard | `docs/sdlc/04_implementation/01_coding_standard.md` | Aturan FP murni, Result Pattern, type hints, dan standar testing (coverage ≥ 90%) untuk pengujian kualitas kode. |
| R-11 | EnvSetup v1.1 | Environment Setup | `docs/sdlc/04_implementation/02_environment_setup.md` | Lingkungan development vs production, database testing sandbox, dan konfigurasi .env untuk pengujian lingkungan. |
| R-12 | ModStruct v1.1 | Module Structure | `docs/sdlc/04_implementation/03_module_structure.md` | Peta modul ke file, SRS-to-File traceability, dan dependensi impor untuk pengujian unit dan integrasi level file. |
| R-13 | GitWF v1.1 | Git Workflow | `docs/sdlc/04_implementation/04_git_workflow.md` | Prosedur branching, commit convention, dan code review untuk pengujian regresi dan version control. |
| R-14 | DevRoad v1.1 | Development Roadmap | `docs/sdlc/04_implementation/05_development_roadmap.md` | Milestone dan sprint planning untuk penjadwalan siklus pengujian. |
| R-15 | BRD v1.1 | Business Requirements Document | `docs/sdlc/02_analysis/01_business_requirements.md` | Konteks bisnis dan aturan operasional toko untuk validasi penerimaan pengguna (UAT). |
| R-16 | TSD v1.1 | Tech Stack Decision | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Batasan teknologi (Python 3.14.2, MySQL 8.4, FP murni, dual-OS) untuk pengujian kompatibilitas. |
| R-17 | WFD v1.1 | Workflow Diagram | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Alur kerja operasional harian toko untuk pengujian end-to-end scenario. |
| R-18 | DD v1.1 | Data Dictionary | `docs/sdlc/02_analysis/05_data_dictionary.md` | Definisi field, tipe data, dan constraint untuk validasi input/output. |

> **Catatan**: File `docs/sdlc/narasi.txt` **TIDAK** digunakan sebagai referensi untuk dokumen ini karena seluruh informasi dari narasi sudah terabsorpsi dan terstruktur lebih baik di dalam dokumen-dokumen SDLC formal di atas.

---

## 4. Kerangka Struktur Dokumen Test Plan

Dokumen Test Plan **WAJIB** disusun mengikuti kerangka struktur berikut, yang diadaptasi dari standar **IEEE 829** dan **ISO/IEC/IEEE 29119-3** serta disesuaikan dengan konteks spesifik proyek AbuCom:

```
---
dokumen    : Test Plan
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [TANGGAL PENGERJAAN]
status     : Draft
penyusun   : Senior QA Lead & Test Strategy Architect
---

# Test Plan — AbuCom

## Riwayat Perubahan Dokumen
(Tabel riwayat versi)

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya (Input & Output)
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan
### 1.7. Referensi Dokumen SDLC

## 2. Cakupan Pengujian (Test Scope)
### 2.1. Fitur yang Diuji (In-Scope)
### 2.2. Fitur yang Tidak Diuji (Out-of-Scope)
### 2.3. Asumsi Pengujian
### 2.4. Risiko dan Mitigasi Pengujian

## 3. Strategi Pengujian (Test Strategy)
### 3.1. Tingkat Pengujian (Test Levels)
#### 3.1.1. Unit Testing
#### 3.1.2. Integration Testing
#### 3.1.3. System Testing
#### 3.1.4. User Acceptance Testing (UAT)
### 3.2. Tipe Pengujian (Test Types)
#### 3.2.1. Functional Testing
#### 3.2.2. Non-Functional Testing (Performance, Usability)
#### 3.2.3. Security Testing
#### 3.2.4. Regression Testing
#### 3.2.5. Compatibility Testing (Dual-OS)
#### 3.2.6. Database Integrity Testing
#### 3.2.7. Decimal Precision Testing (Keuangan & Stok)
### 3.3. Pendekatan Pengujian (Test Approach)
#### 3.3.1. Black-Box Testing
#### 3.3.2. White-Box Testing
#### 3.3.3. Exploratory Testing
### 3.4. Kriteria Masuk dan Keluar Pengujian (Entry & Exit Criteria)
#### 3.4.1. Entry Criteria (Kapan Pengujian Dimulai)
#### 3.4.2. Exit Criteria (Kapan Pengujian Selesai)
#### 3.4.3. Suspension Criteria (Kapan Pengujian Ditangguhkan)
#### 3.4.4. Resumption Criteria (Kapan Pengujian Dilanjutkan)

## 4. Pemetaan Cakupan Pengujian per Modul
### 4.1. Modul M.1 — Manajemen Transaksi & Kebijakan Harga
### 4.2. Modul M.2 — Manajemen Inventaris, BOM & Stock Opname
### 4.3. Modul M.3 — Layanan Keuangan Digital, PPOB & Jasa Service
### 4.4. Modul M.4 — Manajemen SDM, Penggajian & Poin Karyawan
### 4.5. Modul M.5 — Sistem Manajemen Antrian & Pelacakan Desain
### 4.6. Modul M.6 — Administrasi Pinjaman, Aset & Pengeluaran
### 4.7. Modul M.7 — Keamanan, Audit Trail & Hak Akses
### 4.8. Modul M.8 — Pembatalan, Retur & CRM
### 4.9. Modul M.9 — Skalabilitas Multi-Cabang
### 4.10. Modul M.10 — Konfigurasi Sistem Runtime

## 5. Pengujian Keamanan (Security Testing Plan)
### 5.1. Pengujian Otentikasi (bcrypt & JWT)
### 5.2. Pengujian Otorisasi (RBAC 8 Peran)
### 5.3. Pengujian SQL Injection (Parameterized Queries)
### 5.4. Pengujian Rate Limiting & Lockout
### 5.5. Pengujian Sanitasi Input CLI
### 5.6. Pengujian Audit Trail JSON
### 5.7. Pengujian Enkripsi Data (AES-256 Backup & Fernet CRM)
### 5.8. Pengujian Kepatuhan UU PDP No. 27/2022

## 6. Pengujian Presisi Desimal (Decimal Precision Testing)
### 6.1. Pengujian Kalkulasi HPP BOM Desimal
### 6.2. Pengujian Pembulatan Keuangan (ROUND_HALF_UP)
### 6.3. Pengujian Mutasi Kas & Rekonsiliasi
### 6.4. Pengujian Pemotongan Stok Desimal
### 6.5. Pengujian Smart Payroll & Depresiasi Aset

## 7. Pengujian Integrasi & Konektivitas
### 7.1. Pengujian Connection Pooling & Retry Mechanism
### 7.2. Pengujian ACID Transaction Block
### 7.3. Pengujian Lintas Modul (Cross-Module Integration)
### 7.4. Pengujian Konektivitas LAN Client-Server
### 7.5. Pengujian Portabilitas Dual-OS (Windows 11 & Debian 12)

## 8. Pengujian Antarmuka Pengguna CLI
### 8.1. Pengujian Navigasi Menu & Breadcrumb
### 8.2. Pengujian Rendering Visual (rich & tabulate)
### 8.3. Pengujian Format Struk Thermal (58mm & 80mm)
### 8.4. Pengujian Encoding UTF-8 Lintas OS
### 8.5. Pengujian Kode Error Visual (ERR-XXX-YYY)

## 9. Pengujian Non-Fungsional
### 9.1. Pengujian Performa (Response Time < 2 detik)
### 9.2. Pengujian Ketersediaan (Uptime & UPS Graceful Shutdown)
### 9.3. Pengujian Backup & Restore Database
### 9.4. Pengujian Import CSV Bulk Data
### 9.5. Pengujian Kapasitas Data (Skalabilitas)

## 10. Lingkungan Pengujian (Test Environment)
### 10.1. Spesifikasi Hardware Pengujian
### 10.2. Spesifikasi Software Pengujian
### 10.3. Database Pengujian (abucom_test_db)
### 10.4. Data Pengujian (Test Data / Fixtures)
### 10.5. Konfigurasi .env Pengujian

## 11. Manajemen Pengujian
### 11.1. Peran dan Tanggung Jawab Tim Pengujian
### 11.2. Jadwal Pengujian (Test Schedule)
### 11.3. Alat Bantu Pengujian (Testing Tools)
#### 11.3.1. Framework Unit Testing (pytest / unittest)
#### 11.3.2. Pengukuran Code Coverage (coverage.py)
#### 11.3.3. Alat Pelaporan Defect
### 11.4. Prosedur Pelaporan Defect
#### 11.4.1. Klasifikasi Severity Defect
#### 11.4.2. Template Laporan Defect
#### 11.4.3. Siklus Hidup Defect (Defect Lifecycle)
### 11.5. Metrik Kualitas Pengujian (Test Metrics)

## 12. Matriks Ketertelusuran Pengujian (Test Traceability Matrix)
### 12.1. SRS Fungsional → Test Scope Mapping
### 12.2. SRS Non-Fungsional → Test Scope Mapping
### 12.3. Use Case (UC) → Test Scenario Mapping
### 12.4. Kode Error → Test Validation Mapping

## 13. Kriteria Penerimaan Pengguna (User Acceptance Criteria)
### 13.1. Kriteria Penerimaan Pemilik Usaha
### 13.2. Kriteria Penerimaan Operasional Harian
### 13.3. Checklist Sign-Off UAT

## 14. Lampiran
### 14.1. Glosarium Istilah Pengujian
### 14.2. Template Test Case
### 14.3. Template Test Report

## 15. Referensi Dokumen
(Daftar lengkap file referensi yang digunakan dalam penyusunan dokumen ini)
```

> **Catatan Penting tentang Kerangka**: Kerangka di atas merupakan struktur minimum yang **WAJIB** ada. Jika selama penyusunan ditemukan kebutuhan sub-bab tambahan yang relevan (misalnya pengujian khusus WhatsApp link generator, pengujian printer thermal, dll.), maka **WAJIB** ditambahkan ke dalam kerangka di atas.

---

## 5. Instruksi Penyusunan Konten

### 5.1. Instruksi Perangkuman Data Referensi
- [ ] Baca dan rangkum **SELURUH** data dan informasi dari setiap file referensi (R-01 s.d R-18) yang tercantum di Bagian 3.
- [ ] Pastikan **setiap detail** dari file referensi dirangkum tanpa ada yang terlewat, terutama: kode SRS-F, kode UC, kode error (ERR-XXX-YYY), nilai numerik threshold, formula kalkulasi, aturan validasi, matriks RBAC, dan spesifikasi teknis.
- [ ] Catat semua data numerik penting: bcrypt cost factor 12, JWT 8 jam (28800 detik), pool_size=5, retry 3x, toleransi kas Rp 10.000, deposit PPOB Rp 150.000, pengeluaran eskalasi Rp 500.000, UMR Rp 3.200.000, DECIMAL(15,4), dll.

### 5.2. Instruksi Selektivitas Konten
- [ ] **HANYA** ambil, rangkum, dan tuangkan data serta informasi yang **secara spesifik dibutuhkan** oleh dokumen Test Plan.
- [ ] **JANGAN** menyalin ulang seluruh isi dokumen referensi ke dalam Test Plan. Transformasikan informasi referensi menjadi strategi pengujian, cakupan pengujian, dan skenario pengujian.
- [ ] Fokuskan konten pada **"apa yang harus diuji"**, **"bagaimana cara mengujinya"**, **"kapan diuji"**, **"oleh siapa"**, dan **"apa kriteria keberhasilannya"**.
- [ ] Pastikan dokumen ini bersih dan hanya berisi data yang memang seharusnya ada di dalam dokumen Test Plan, bukan duplikasi dari SRS atau Security Design.

### 5.3. Instruksi Kualitas Standar Industri
- [ ] Susun dokumen dengan standar struktur **IEEE 829** / **ISO/IEC/IEEE 29119** yang diadaptasi untuk konteks UMKM AbuCom.
- [ ] Pastikan setiap bab memiliki konten yang substansial, informatif, dan dapat dieksekusi (actionable), bukan hanya judul kosong.
- [ ] Sertakan **diagram Mermaid** yang relevan untuk memvisualisasikan: alur strategi pengujian, siklus hidup defect, dan pemetaan test traceability.
- [ ] Sertakan **tabel-tabel terstruktur** untuk: matriks ketertelusuran, klasifikasi severity, jadwal pengujian, dan metrik kualitas.

### 5.4. Instruksi Sebagai Input Fase Selanjutnya
- [ ] Pastikan isi dokumen Test Plan ini **layak dijadikan acuan dan input utama** bagi pembuatan dokumen Test Cases, Test Scripts, dan Test Report pada fase SDLC selanjutnya.
- [ ] Pastikan setiap skenario pengujian yang didefinisikan di Test Plan dapat diturunkan menjadi test case detail yang spesifik dan terukur.
- [ ] Pastikan matriks ketertelusuran (Traceability Matrix) di Bab 12 memetakan **setiap** kebutuhan SRS dan use case ke skenario pengujian yang sesuai, tanpa ada kebutuhan yang terlewat.

### 5.5. Instruksi Bahasa dan Keterbacaan
- [ ] Gunakan **Bahasa Indonesia** yang natural, formal, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau AI model lain yang lebih murah.
- [ ] Hindari penggunaan kalimat pasif yang panjang dan berbelit. Gunakan kalimat aktif yang jelas subjek, predikat, dan objeknya.
- [ ] Untuk istilah teknis berbahasa Inggris yang sudah umum di industri (seperti: test case, regression testing, code coverage, dll.), tuliskan istilah asli bahasa Inggris dalam format *italic* diikuti terjemahan/penjelasan bahasa Indonesia jika diperlukan.
- [ ] Gunakan format **tebal (bold)** untuk menekankan kata kunci penting dan istilah kritis.

### 5.6. Instruksi Kelengkapan dan Kualitas
- [ ] Pastikan kualitas kelengkapan isi dokumen ini tidak akan dipertanyakan dan tidak akan menghambat proses pengerjaan fase SDLC selanjutnya.
- [ ] Dokumen ini harus bersifat **self-contained**: siapa pun yang membaca dokumen ini harus bisa memahami seluruh strategi pengujian AbuCom tanpa perlu membaca dokumen referensi lain terlebih dahulu (meskipun referensi tetap dicantumkan).

### 5.7. Instruksi Penandaan Data Kosong
- [ ] Jika ada data atau informasi yang **tidak ditemukan** di dalam file referensi tetapi **dibutuhkan** oleh dokumen Test Plan, maka tandai bagian tersebut dengan format:
  ```
  > ⚠️ **[DATA BELUM TERSEDIA]**: [Deskripsi data yang dibutuhkan dan alasannya].
  ```
- [ ] Penandaan ini memungkinkan pemilik proyek atau tim untuk mengisi data tersebut secara manual di kemudian hari.

### 5.8. Instruksi Referensi di Akhir Dokumen
- [ ] Di bagian akhir baris paling bawah dokumen (Bab 15), tambahkan daftar lengkap **semua** file referensi yang digunakan dalam pengerjaan pembuatan dan penyusunan dokumen ini, dengan format tabel:

  | No | Kode Ref | Nama Dokumen | Path File | Versi |
  |----|----------|--------------|-----------|-------|

### 5.9. Instruksi Target File Output
- [ ] Tuangkan **SELURUH** hasil pengerjaan pembuatan dan penyusunan dokumen Test Plan ke dalam target file: `docs/sdlc/05_testing/01_test_plan.md`.
- [ ] Gunakan format front-matter YAML metadata di baris teratas file (konsisten dengan format dokumen SDLC lainnya).
- [ ] Pastikan file ditulis menggunakan encoding **UTF-8** tanpa BOM.

---

## 6. Instruksi Tambahan Spesifik Dokumen Test Plan

Berikut adalah instruksi tambahan yang **spesifik** untuk ciri khas dokumen Test Plan proyek AbuCom dan belum tercantum di atas:

### 6.1. Pengujian Spesifik Paradigma Functional Programming (FP)
- [ ] Tambahkan bagian khusus dalam strategi pengujian yang menjelaskan cara menguji **pure functions** secara deterministik tanpa koneksi database.
- [ ] Definisikan standar pengujian yang memvalidasi bahwa fungsi logika bisnis di folder `logic/` tidak memiliki efek samping (*side effects*) dan bersifat imutabel.
- [ ] Sertakan contoh pola pengujian menggunakan mock NamedTuple sebagai test data.

### 6.2. Pengujian Spesifik Presisi Desimal Keuangan
- [ ] Tambahkan skenario pengujian khusus yang memvalidasi bahwa **tidak ada** operasi aritmatika keuangan menggunakan tipe data `float` Python.
- [ ] Definisikan test case edge-case untuk pembulatan desimal (ROUND_HALF_UP) pada kalkulasi HPP, margin, payroll, depresiasi, dan poin insentif.
- [ ] Sertakan contoh nilai numerik spesifik untuk boundary testing (misalnya: `Decimal('0.00005')`, `Decimal('99999999999.9999')`).

### 6.3. Pengujian Spesifik Lingkungan Offline LAN
- [ ] Tambahkan skenario pengujian yang memvalidasi bahwa sistem berfungsi **100% tanpa koneksi internet**.
- [ ] Definisikan test case untuk simulasi gangguan jaringan LAN: kabel dicabut, switch mati, server restart.
- [ ] Sertakan pengujian retry mechanism (exponential backoff 3x) saat koneksi database terputus (error 2006/2013).

### 6.4. Pengujian Spesifik Multi-Branch Readiness
- [ ] Tambahkan skenario pengujian yang memvalidasi bahwa **setiap** query database menggunakan filter `cabang_id` secara konsisten.
- [ ] Definisikan test case dengan `cabang_id = 1` (default toko pusat) dan `cabang_id = 2` (simulasi cabang masa depan) untuk memvalidasi isolasi data antar cabang.

### 6.5. Pengujian Spesifik Eskalasi Otorisasi Supervisor
- [ ] Tambahkan skenario pengujian untuk 4 operasi kritis yang memerlukan eskalasi sandi pemilik: pembatalan transaksi, retur DP, pengeluaran > Rp 500.000, dan restorasi database.
- [ ] Definisikan skenario negatif: apa yang terjadi jika sandi supervisor salah, jika akun supervisor terkunci, atau jika session JWT supervisor sudah kedaluwarsa.

### 6.6. Pengujian Spesifik Serah Terima Shift Kasir
- [ ] Tambahkan skenario pengujian untuk rekonsiliasi kas laci fisik vs kas sistem dengan batas toleransi Rp 10.000.
- [ ] Definisikan skenario normal (selisih ≤ Rp 10.000) dan skenario anomali (selisih > Rp 10.000) beserta prosedur otorisasi kepala percetakan.

### 6.7. Pengujian Spesifik Fraud Detection & Audit Trail
- [ ] Tambahkan skenario pengujian yang memvalidasi deteksi anomali: selisih kas berturut-turut 3 shift, frekuensi retur > 5 kali/minggu, login gagal > 10 kali/jam dari 1 IP.
- [ ] Definisikan pengujian integritas log audit: pastikan setiap operasi CRUD pada tabel sensitif memicu pencatatan audit_logs dengan `old_value` dan `new_value` yang akurat.

### 6.8. Pengujian Spesifik Template Struk Thermal
- [ ] Tambahkan skenario pengujian untuk format struk thermal 58mm (32 karakter) dan 80mm (48 karakter).
- [ ] Validasikan text wrapping nama barang panjang, alignment nominal rupiah rata kanan, dan encoding UTF-8 pada file `.txt` output.

---

## 7. Checklist Tahapan Implementasi

Berikut adalah tahapan implementasi yang **WAJIB** diikuti secara berurutan. Setiap tahapan dipecah menjadi tugas-tugas atomik level rendah agar tidak ada ambiguitas.

### Tahap 1: Persiapan dan Pembacaan File Referensi

- [ ] **1.1.** Baca file referensi R-01: `docs/sdlc/02_analysis/02_software_requirements.md` — Baca secara penuh dari baris pertama hingga baris terakhir.
- [ ] **1.2.** Rangkum dari R-01: Daftar semua kode SRS-F-001 s.d SRS-F-040 dan SRS-F-ADD-01 s.d SRS-F-ADD-05 beserta nama kebutuhan, modul terkait, prioritas, aktor, aturan validasi, dan kode error.
- [ ] **1.3.** Rangkum dari R-01: Daftar semua kebutuhan non-fungsional SRS-NF-001 s.d SRS-NF-011 beserta metrik target terukur.
- [ ] **1.4.** Baca file referensi R-02: `docs/sdlc/02_analysis/03_use_case_diagram.md` — Baca secara penuh.
- [ ] **1.5.** Rangkum dari R-02: Daftar semua 44 use case (UC-001 s.d UC-044) beserta Main Flow, Alternative Flow, Exception Flow, Precondition, dan Postcondition.
- [ ] **1.6.** Baca file referensi R-03: `docs/sdlc/02_analysis/06_access_control_matrix.md` — Baca secara penuh.
- [ ] **1.7.** Rangkum dari R-03: Matriks RBAC lengkap 8 peran × 44 use case, matriks CRUD 8 peran × 28 tabel, aturan eskalasi supervisor, dan rate limiting.
- [ ] **1.8.** Baca file referensi R-04: `docs/sdlc/03_design/06_security_design.md` — Baca secara penuh.
- [ ] **1.9.** Rangkum dari R-04: Threat model (8 ancaman), konfigurasi bcrypt/JWT/RBAC, sanitasi CLI, audit trail triggers, fraud detection rules, SOP insiden keamanan, dan semua kode error keamanan.
- [ ] **1.10.** Baca file referensi R-05: `docs/sdlc/03_design/03_system_architecture.md` — Fokus pada Bab 4 (Logical Architecture), Bab 6 (Data Architecture), Bab 7 (Security Architecture), dan Bab 8 (Communication Architecture).
- [ ] **1.11.** Rangkum dari R-05: Connection pooling (pool_size=5), retry mechanism (3x exponential backoff), ACID transaction block, presisi DECIMAL(15,4), multi-branch cabang_id, dan migration strategy.
- [ ] **1.12.** Baca file referensi R-06: `docs/sdlc/03_design/01_database_schema.sql` — Baca secara penuh.
- [ ] **1.13.** Rangkum dari R-06: Daftar 28 tabel, foreign key constraints, CHECK constraints, tipe data kolom (terutama DECIMAL), dan default values.
- [ ] **1.14.** Baca file referensi R-07: `docs/sdlc/03_design/02_erd_database.md` — Fokus pada relasi FK dan kardinalitas.
- [ ] **1.15.** Rangkum dari R-07: 58 relasi foreign key, kardinalitas (1:1, 1:N, N:M), dan tabel dependensi.
- [ ] **1.16.** Baca file referensi R-08: `docs/sdlc/03_design/05_bom_hpp_design.md` — Baca secara penuh.
- [ ] **1.17.** Rangkum dari R-08: Formula HPP BOM desimal, contoh numerik stempel flash, formula limbah, formula sinkronisasi ATK, dan formula margin keuntungan.
- [ ] **1.18.** Baca file referensi R-09: `docs/sdlc/03_design/04_cli_interaction_flow.md` — Fokus pada navigasi menu, kode menu (MENU-BASE, MENU-Mx), dan kode error visual.
- [ ] **1.19.** Rangkum dari R-09: Daftar kode menu, konvensi navigasi (tombol 0 = back), breadcrumb, warna ANSI, dan format error `ERR-XXX-YYY`.
- [ ] **1.20.** Baca file referensi R-10 s.d R-18 — Baca secara seperlunya sesuai kebutuhan.
- [ ] **1.21.** Rangkum dari R-10: Target code coverage ≥ 90%, konvensi penamaan test file `test_<modul>.py`, aturan unit testing pure functions tanpa DB, dan integration testing dengan `abucom_test_db`.
- [ ] **1.22.** Rangkum dari R-11: Perbedaan lingkungan Development vs Production, konfigurasi `.env.test`, dan database bayangan `abucom_test_db`.
- [ ] **1.23.** Rangkum dari R-12: Peta SRS-to-File traceability dan Module-to-File mapping.
- [ ] **1.24.** Rangkum dari R-15 s.d R-18: Aturan bisnis operasional harian dari BRD, batasan teknologi dari TSD, alur kerja workflow, dan definisi field data dictionary.

### Tahap 2: Penyusunan Kerangka Dokumen

- [ ] **2.1.** Buat file target: `docs/sdlc/05_testing/01_test_plan.md`.
- [ ] **2.2.** Tulis front-matter YAML metadata di baris teratas file (dokumen, proyek, versi, tanggal, status, penyusun).
- [ ] **2.3.** Tulis judul dokumen: `# Test Plan — AbuCom`.
- [ ] **2.4.** Tulis tabel Riwayat Perubahan Dokumen dengan entry versi 1.0.
- [ ] **2.5.** Tulis kerangka seluruh bab dan sub-bab sesuai struktur yang didefinisikan di Bagian 4 issue ini.
- [ ] **2.6.** Pastikan setiap bab memiliki heading markdown yang benar (`##`, `###`, `####`).

### Tahap 3: Pengisian Konten Bab 1 — Informasi Dokumen

- [ ] **3.1.** Tulis Bab 1.1 (Tujuan Dokumen): Jelaskan tujuan Test Plan sebagai cetak biru strategi pengujian AbuCom, posisinya dalam SDLC, dan manfaatnya bagi tim.
- [ ] **3.2.** Tulis Bab 1.2 (Cakupan Dokumen): Daftarkan cakupan aspek pengujian yang didokumentasikan.
- [ ] **3.3.** Tulis Bab 1.3 (Posisi Dokumen dalam SDLC): Sertakan diagram ASCII posisi deliverable Test Plan di Fase 05.
- [ ] **3.4.** Tulis Bab 1.4 (Hubungan dengan Dokumen SDLC Lainnya): Daftarkan dokumen input (R-01 s.d R-18) dan dokumen output (Test Cases, Test Report).
- [ ] **3.5.** Tulis Bab 1.5 (Audiens Target): Junior Programmer, Tim AI, Kepala Percetakan.
- [ ] **3.6.** Tulis Bab 1.6 (Definisi, Akronim, Singkatan): Daftarkan semua istilah teknis pengujian.
- [ ] **3.7.** Tulis Bab 1.7 (Referensi Dokumen SDLC): Tabel referensi lengkap dengan path file dan versi.

### Tahap 4: Pengisian Konten Bab 2 — Cakupan Pengujian

- [ ] **4.1.** Tulis Bab 2.1 (In-Scope): Daftarkan seluruh 10 modul fungsional (M.1 s.d M.10) beserta ringkasan fitur yang diuji.
- [ ] **4.2.** Tulis Bab 2.2 (Out-of-Scope): Daftarkan fitur yang tidak diuji (misalnya: GUI web, koneksi internet, WhatsApp API, mobile banking).
- [ ] **4.3.** Tulis Bab 2.3 (Asumsi Pengujian): Daftarkan asumsi lingkungan, data, dan infrastruktur.
- [ ] **4.4.** Tulis Bab 2.4 (Risiko dan Mitigasi): Daftarkan risiko pengujian (misalnya: database sandbox tidak konsisten, keterbatasan LAN) dan rencana mitigasinya.

### Tahap 5: Pengisian Konten Bab 3 — Strategi Pengujian

- [ ] **5.1.** Tulis Bab 3.1 (Tingkat Pengujian): Definisikan 4 level pengujian (Unit, Integration, System, UAT) beserta penjelasan, cakupan, dan contoh untuk konteks AbuCom.
- [ ] **5.2.** Tulis Bab 3.2 (Tipe Pengujian): Definisikan 7 tipe pengujian beserta metode, tools, dan target modul.
- [ ] **5.3.** Tulis Bab 3.3 (Pendekatan Pengujian): Definisikan 3 pendekatan testing dan kapan masing-masing digunakan.
- [ ] **5.4.** Tulis Bab 3.4 (Entry & Exit Criteria): Definisikan kriteria kapan pengujian dimulai, selesai, ditangguhkan, dan dilanjutkan.

### Tahap 6: Pengisian Konten Bab 4 — Pemetaan Cakupan per Modul

- [ ] **6.1.** Untuk setiap modul M.1 s.d M.10, tulis: daftar fitur yang diuji, daftar SRS-F terkait, daftar UC terkait, daftar kode error yang divalidasi, tipe pengujian yang diterapkan, dan prioritas.
- [ ] **6.2.** Gunakan format tabel terstruktur untuk setiap modul.
- [ ] **6.3.** Pastikan tidak ada SRS-F atau UC yang terlewat dari pemetaan.

### Tahap 7: Pengisian Konten Bab 5 — Pengujian Keamanan

- [ ] **7.1.** Tulis 8 sub-bab pengujian keamanan berdasarkan rangkuman dari R-04 (Security Design) dan R-03 (ACM).
- [ ] **7.2.** Sertakan skenario pengujian positif (berhasil) dan negatif (gagal) untuk setiap aspek keamanan.
- [ ] **7.3.** Sertakan referensi kode error keamanan yang divalidasi di setiap skenario.

### Tahap 8: Pengisian Konten Bab 6 — Pengujian Presisi Desimal

- [ ] **8.1.** Tulis 5 sub-bab pengujian presisi desimal berdasarkan rangkuman dari R-08 (BOM Design) dan R-01 (SRS).
- [ ] **8.2.** Sertakan contoh nilai numerik spesifik untuk boundary testing dan edge cases.
- [ ] **8.3.** Sertakan formula matematis yang divalidasi (HPP, margin, payroll, depresiasi).

### Tahap 9: Pengisian Konten Bab 7 — Pengujian Integrasi

- [ ] **9.1.** Tulis 5 sub-bab pengujian integrasi berdasarkan rangkuman dari R-05 (System Architecture).
- [ ] **9.2.** Sertakan skenario simulasi gangguan (network failure, DB restart) dan hasil yang diharapkan.

### Tahap 10: Pengisian Konten Bab 8 — Pengujian CLI

- [ ] **10.1.** Tulis 5 sub-bab pengujian CLI berdasarkan rangkuman dari R-09 (CLI Interaction Flow).
- [ ] **10.2.** Sertakan skenario pengujian rendering visual, navigasi, dan format output.

### Tahap 11: Pengisian Konten Bab 9 — Pengujian Non-Fungsional

- [ ] **11.1.** Tulis 5 sub-bab pengujian non-fungsional berdasarkan rangkuman SRS-NF dari R-01.
- [ ] **11.2.** Sertakan metrik target terukur untuk setiap pengujian (response time, throughput, capacity).

### Tahap 12: Pengisian Konten Bab 10 — Lingkungan Pengujian

- [ ] **12.1.** Tulis spesifikasi hardware dan software lingkungan pengujian berdasarkan rangkuman dari R-11 (Environment Setup).
- [ ] **12.2.** Tulis konfigurasi database pengujian `abucom_test_db` dan data fixtures.
- [ ] **12.3.** Tulis konfigurasi `.env.test` yang dibutuhkan.

### Tahap 13: Pengisian Konten Bab 11 — Manajemen Pengujian

- [ ] **13.1.** Tulis peran dan tanggung jawab tim pengujian (Pemilik, AI Engineer, Kepala Percetakan).
- [ ] **13.2.** Tulis jadwal pengujian yang diselaraskan dengan Development Roadmap (R-14).
- [ ] **13.3.** Tulis alat bantu pengujian (pytest, coverage.py).
- [ ] **13.4.** Tulis prosedur pelaporan defect: klasifikasi severity (Critical, Major, Minor, Trivial), template laporan, dan siklus hidup defect.
- [ ] **13.5.** Tulis metrik kualitas pengujian (defect density, pass rate, coverage percentage).

### Tahap 14: Pengisian Konten Bab 12 — Matriks Ketertelusuran

- [ ] **14.1.** Buat tabel pemetaan **SRS-F → Test Scope**: Setiap SRS-F-001 s.d SRS-F-040+ dipetakan ke skenario pengujian yang relevan.
- [ ] **14.2.** Buat tabel pemetaan **SRS-NF → Test Scope**: Setiap SRS-NF-001 s.d SRS-NF-011 dipetakan ke skenario pengujian non-fungsional.
- [ ] **14.3.** Buat tabel pemetaan **UC → Test Scenario**: Setiap UC-001 s.d UC-044 dipetakan ke skenario pengujian fungsional.
- [ ] **14.4.** Buat tabel pemetaan **Kode Error → Test Validation**: Setiap kode ERR-XXX-YYY dipetakan ke test case validasi.
- [ ] **14.5.** Pastikan **tidak ada** SRS-F, SRS-NF, UC, atau kode error yang tidak memiliki pemetaan pengujian.

### Tahap 15: Pengisian Konten Bab 13 — Kriteria Penerimaan

- [ ] **15.1.** Tulis kriteria penerimaan dari perspektif pemilik usaha (akurasi laporan keuangan, keamanan data, kemudahan operasional).
- [ ] **15.2.** Tulis kriteria penerimaan operasional harian (kecepatan transaksi, stabilitas sistem, ketersediaan struk).
- [ ] **15.3.** Tulis checklist sign-off UAT yang harus ditandatangani pemilik sebelum go-live.

### Tahap 16: Pengisian Konten Bab 14 — Lampiran

- [ ] **16.1.** Tulis glosarium istilah pengujian yang digunakan dalam dokumen.
- [ ] **16.2.** Tulis template test case standar (ID, Nama, Precondition, Steps, Expected Result, Actual Result, Status).
- [ ] **16.3.** Tulis template test report standar.

### Tahap 17: Pengisian Konten Bab 15 — Referensi

- [ ] **17.1.** Tulis tabel daftar lengkap semua file referensi (R-01 s.d R-18) yang digunakan, dengan kolom: No, Kode Ref, Nama Dokumen, Path File, dan Versi.

### Tahap 18: Review dan Finalisasi

- [ ] **18.1.** Baca ulang seluruh dokumen dari baris pertama hingga baris terakhir.
- [ ] **18.2.** Periksa konsistensi penomoran bab, sub-bab, dan tabel.
- [ ] **18.3.** Periksa konsistensi penggunaan kode referensi (SRS-F, UC, ERR, MENU) terhadap dokumen sumber.
- [ ] **18.4.** Periksa tidak ada placeholder `[TODO]` atau `[TBD]` yang tertinggal tanpa penandaan `⚠️ [DATA BELUM TERSEDIA]`.
- [ ] **18.5.** Periksa semua diagram Mermaid dapat di-render tanpa error sintaks.
- [ ] **18.6.** Periksa semua link file referensi menggunakan path relatif yang benar.
- [ ] **18.7.** Pastikan file tersimpan dengan encoding UTF-8 tanpa BOM.
- [ ] **18.8.** Verifikasi bahwa kerangka dokumen mencakup seluruh bab yang didefinisikan di Bagian 4 issue ini.

---

## 8. Kriteria Selesai (Definition of Done)

Issue ini dianggap selesai jika dan hanya jika:

1. ✅ File `docs/sdlc/05_testing/01_test_plan.md` telah terisi penuh dengan konten substantif (bukan kerangka kosong).
2. ✅ Seluruh 15 bab utama dan sub-babnya telah terisi konten yang informatif dan actionable.
3. ✅ Matriks ketertelusuran (Bab 12) memetakan **100%** SRS-F, SRS-NF, UC, dan kode error ke skenario pengujian.
4. ✅ Tidak ada SRS-F, UC, atau kode error yang terlewat tanpa skenario pengujian.
5. ✅ Semua data numerik threshold dan formula matematis dari referensi tercantum akurat.
6. ✅ Semua diagram Mermaid valid dan dapat di-render.
7. ✅ Bahasa Indonesia natural, formal, dan tidak ambigu.
8. ✅ Daftar referensi di Bab 15 mencakup seluruh file yang digunakan.
9. ✅ File menggunakan encoding UTF-8.
10. ✅ Seluruh checklist di Bagian 7 telah di-checklist `[x]`.

---

## 9. Referensi Pembuatan Issue Ini

| No | Kode Ref | Nama Dokumen | Path File | Versi |
|----|----------|--------------|-----------|-------|
| 1 | SRS v1.1 | Software Requirements Specification | `docs/sdlc/02_analysis/02_software_requirements.md` | 1.1 |
| 2 | UCD v1.1 | Use Case Diagram | `docs/sdlc/02_analysis/03_use_case_diagram.md` | 1.1 |
| 3 | ACM v1.1 | Access Control Matrix | `docs/sdlc/02_analysis/06_access_control_matrix.md` | 1.1 |
| 4 | SecDes v1.1 | Security Design | `docs/sdlc/03_design/06_security_design.md` | 1.1 |
| 5 | SysArch v1.1 | System Architecture | `docs/sdlc/03_design/03_system_architecture.md` | 1.1 |
| 6 | DDL v1.1 | Database Schema | `docs/sdlc/03_design/01_database_schema.sql` | 1.1 |
| 7 | ERD v1.1 | ERD Database | `docs/sdlc/03_design/02_erd_database.md` | 1.1 |
| 8 | BOM v1.1 | BOM & HPP Design | `docs/sdlc/03_design/05_bom_hpp_design.md` | 1.1 |
| 9 | CLI v1.1 | CLI Interaction Flow | `docs/sdlc/03_design/04_cli_interaction_flow.md` | 1.1 |
| 10 | CodStd v1.1 | Coding Standard | `docs/sdlc/04_implementation/01_coding_standard.md` | 1.1 |
| 11 | EnvSetup v1.1 | Environment Setup | `docs/sdlc/04_implementation/02_environment_setup.md` | 1.1 |
| 12 | ModStruct v1.1 | Module Structure | `docs/sdlc/04_implementation/03_module_structure.md` | 1.1 |
| 13 | GitWF v1.1 | Git Workflow | `docs/sdlc/04_implementation/04_git_workflow.md` | 1.1 |
| 14 | DevRoad v1.1 | Development Roadmap | `docs/sdlc/04_implementation/05_development_roadmap.md` | 1.1 |
| 15 | BRD v1.1 | Business Requirements Document | `docs/sdlc/02_analysis/01_business_requirements.md` | 1.1 |
| 16 | TSD v1.1 | Tech Stack Decision | `docs/sdlc/01_planning/04_tech_stack_decision.md` | 1.1 |
| 17 | WFD v1.1 | Workflow Diagram | `docs/sdlc/02_analysis/04_workflow_diagram.md` | 1.1 |
| 18 | DD v1.1 | Data Dictionary | `docs/sdlc/02_analysis/05_data_dictionary.md` | 1.1 |
| 19 | Narasi | Narasi Proyek | `docs/sdlc/narasi.txt` | - |
