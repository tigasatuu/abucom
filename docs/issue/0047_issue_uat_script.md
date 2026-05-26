# Pembuatan dan Penyusunan Dokumen UAT Script

| Atribut       | Detail                                                                   |
|---------------|--------------------------------------------------------------------------|
| **Judul**     | Pembuatan dan Penyusunan Dokumen UAT Script (User Acceptance Testing Script) |
| **Dokumen Utama** | UAT Script                                                           |
| **Target File** | `docs/sdlc/05_testing/03_uat_script.md`                              |
| **Prioritas** | High                                                                     |
| **Status**    | Open                                                                     |
| **Tanggal**   | 2026-05-26                                                               |
| **Assignee**  | Junior Programmer / LLM AI Agent (Model Murah)                          |

---

## 1. Persona Pelaksana

**Persona yang ditugaskan:** `Senior UAT Analyst & Business Acceptance Specialist`

**Justifikasi pemilihan persona:**
- UAT Script adalah dokumen yang **berorientasi pada perspektif bisnis pengguna akhir** (Pemilik Usaha & Kepala Percetakan), bukan perspektif teknis programmer.
- Persona ini memiliki otoritas untuk menerjemahkan kebutuhan bisnis operasional harian toko menjadi skenario pengujian penerimaan yang realistis, terstruktur, dan dapat dieksekusi langsung oleh pengguna non-teknis.
- Persona ini memahami standar industri UAT (IEEE 829, ISTQB Foundation Level) dan mampu merancang skrip penerimaan yang menjadi gerbang akhir (*go/no-go gate*) sebelum peluncuran sistem ke produksi (*go-live*).

---

## 2. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca dan dirangkum** sebelum memulai penyusunan dokumen UAT Script. File dipilih berdasarkan relevansi langsung terhadap kebutuhan dokumen ini:

| No | Kode Ref | Nama Dokumen | Path File | Alasan Pemilihan |
|----|----------|--------------|-----------|------------------|
| 1 | **R-TP** | Test Plan v1.1 | `docs/sdlc/05_testing/01_test_plan.md` | **Referensi utama #1.** Sumber definisi strategi UAT (Bab 3.1.4), 44 skenario uji induk, kriteria masuk/keluar pengujian, 7 kriteria sign-off UAT (Bab 13.3), kriteria penerimaan pemilik usaha (Bab 13.1-13.2), lingkungan pengujian (Bab 10), dan daftar error mapping (Bab 12.4). |
| 2 | **R-TC** | Test Cases v1.1 | `docs/sdlc/05_testing/02_test_cases.md` | **Referensi utama #2.** Sumber 70 kasus uji operasional terperinci yang akan diturunkan menjadi langkah-langkah UAT berbasis perspektif pengguna. Menyediakan data uji presisi desimal, prakondisi, langkah uji, dan expected result per modul. |
| 3 | **R-SRS** | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | Spesifikasi kebutuhan fungsional (SRS-F-001 s.d SRS-F-040) dan non-fungsional (SRS-NF-001 s.d SRS-NF-011) sebagai basis verifikasi penerimaan pengguna. |
| 4 | **R-UC** | Use Case Diagram v1.1 | `docs/sdlc/02_analysis/03_use_case_diagram.md` | Alur naratif utama, alur alternatif, dan alur pengecualian dari perspektif interaksi pengguna-sistem untuk 44 use case. |
| 5 | **R-ACM** | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Definisi 8 peran internal dan matriks otorisasi RBAC yang harus diverifikasi oleh pengguna dalam UAT. |
| 6 | **R-CLI** | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur navigasi terminal, rendering visual ANSI, dan format interaksi pengguna yang menjadi acuan langkah-langkah UAT berbasis CLI. |
| 7 | **R-BOM** | BOM & HPP Design v1.1 | `docs/sdlc/03_design/05_bom_hpp_design.md` | Spesifikasi matematika presisi desimal HPP BOM yang harus diverifikasi akurasinya oleh pemilik usaha dalam sesi UAT. |
| 8 | **R-SEC** | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | Parameter keamanan (bcrypt, JWT, rate limiting, enkripsi, UU PDP) yang harus dites dari perspektif pengguna akhir. |
| 9 | **R-WF** | Workflow Diagram v1.1 | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Alur kerja operasional bisnis harian toko yang menjadi basis skenario simulasi UAT end-to-end. |

> **Catatan:** File `narasi.txt` **tidak dipilih** sebagai referensi karena seluruh informasi bisnis dari narasi sudah diserap secara lengkap dan terstruktur ke dalam dokumen SRS, Use Case, BRD, dan dokumen SDLC lainnya di atas. Menggunakan narasi secara langsung berisiko menghasilkan data yang tidak konsisten dengan versi dokumen yang sudah divalidasi (v1.1).

---

## 3. Instruksi Pengerjaan

### 3.1. Instruksi Umum

1. **Rangkum semua data dan informasi** yang ada di dalam setiap file referensi (R-TP, R-TC, R-SRS, R-UC, R-ACM, R-CLI, R-BOM, R-SEC, R-WF). Setiap detail yang relevan dengan UAT Script jangan sampai ada yang terlewat, terutama:
   - 44 skenario uji dari Test Plan
   - 70 kasus uji dari Test Cases
   - 7 kriteria sign-off UAT dari Test Plan Bab 13.3
   - Kriteria penerimaan pengguna dari Test Plan Bab 13.1-13.2
   - Data uji (fixtures) global dari Test Cases Bab 3.3
   - Error mapping dari Test Plan Bab 12.4

2. **Hanya ambil dan rangkum data/informasi yang spesifik dibutuhkan** oleh dokumen UAT Script. Dokumen ini **bukan** duplikasi dari Test Cases. UAT Script berfokus pada:
   - **Perspektif pengguna akhir** (Pemilik Usaha & Kepala Percetakan), bukan perspektif teknis programmer/QA.
   - **Skenario bisnis operasional harian** yang realistis dan dapat dieksekusi langsung di lingkungan produksi.
   - **Langkah-langkah pengujian berbahasa bisnis** (bukan bahasa kode/teknis), yang dapat dipahami oleh pengguna non-teknis.
   - **Formulir penilaian/checklist** yang dapat dicetak dan ditandatangani secara fisik.

3. **Pastikan dokumen ini layak dijadikan referensi, acuan, dan input utama** bagi dokumen fase SDLC selanjutnya, khususnya:
   - **Test Report:** Sebagai basis pengisian hasil eksekusi UAT.
   - **Deployment/Release Document:** Sebagai bukti formal persetujuan go-live.
   - **Training Manual:** Sebagai referensi skenario operasional harian untuk pelatihan staf baru.

4. **Gunakan struktur bahasa Indonesia yang natural**, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau AI model lain yang lebih murah. Hindari:
   - Kalimat pasif berlapis-lapis.
   - Istilah teknis tanpa penjelasan (jika digunakan, berikan definisi di glosarium).
   - Referensi silang yang tidak jelas (selalu sebutkan ID dan nama lengkap dokumen).

5. **Pastikan kualitas kelengkapan isi dokumen tidak dipertanyakan.** Dokumen harus cukup lengkap dan detail sehingga tidak menghambat proses pekerjaan fase tahapan SDLC selanjutnya. Tidak boleh ada bagian yang setengah jadi, ambigu, atau membutuhkan klarifikasi tambahan.

6. **Jika ada data yang kosong/tidak tersedia** pada file referensi, maka tandai secara eksplisit dengan format:
   ```
   [DATA BELUM TERSEDIA - Perlu diisi manual oleh Pemilik Usaha]
   ```

7. **Tambahkan keterangan referensi** di bagian akhir baris paling bawah dokumen berupa tabel daftar file referensi yang digunakan dalam pengerjaan pembuatan dan penyusunan dokumen ini.

8. **Tuangkan semua hasil pengerjaan** ke dalam target file: `docs/sdlc/05_testing/03_uat_script.md`.

### 3.2. Instruksi Spesifik UAT Script

Selain instruksi umum di atas, perhatikan kaidah standar berikut yang khas untuk dokumen UAT Script:

1. **Skrip UAT harus berbasis skenario bisnis end-to-end**, bukan per-fungsi individual. Kelompokkan test cases yang saling berhubungan menjadi skenario alur bisnis harian yang utuh (misalnya: "Skenario Hari Operasional Toko Lengkap" yang dimulai dari buka toko → login → transaksi → opname → tutup shift).

2. **Setiap skrip UAT harus memiliki kriteria kelulusan (pass/fail) yang terukur dan deterministik** — bukan subjektif. Gunakan data angka presisi desimal yang konkret, bukan pernyataan umum seperti "berjalan dengan baik."

3. **Sertakan formulir tanda tangan fisik** pada setiap sesi UAT dan pada bagian akhir keseluruhan dokumen sebagai bukti formal persetujuan go-live.

4. **Sertakan checklist pra-UAT** (UAT Readiness Checklist) yang harus dipenuhi sebelum sesi UAT dimulai, untuk memastikan lingkungan dan data uji telah siap.

5. **Sertakan panduan penanganan temuan (defect)** selama sesi UAT berlangsung, termasuk template pencatatan temuan dan prosedur eskalasi.

6. **Setiap skrip UAT harus menyebutkan secara eksplisit** siapa aktor/penguji (Pemilik Usaha atau Kepala Percetakan), di lingkungan apa (PC Kasir Windows 11, Terminal CLI), dan dengan data uji apa.

---

## 4. Kerangka Struktur Dokumen UAT Script

Gunakan kerangka berikut sebagai standar struktur dokumen. Kerangka ini mengacu pada standar praktik industri **IEEE 829 (Test Procedure Specification)** dan **ISTQB Foundation Level Syllabus** yang diadaptasi untuk konteks UAT:

```
---
dokumen    : UAT Script
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : 2026-05-26
status     : Draft
penyusun   : Senior UAT Analyst & Business Acceptance Specialist
---

# UAT Script — AbuCom

## Riwayat Perubahan Dokumen
(Tabel: Versi | Tanggal | Perubahan | Oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya (Input/Output)
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan

---

## 2. Lingkup dan Tujuan UAT
### 2.1. Tujuan Pengujian Penerimaan Pengguna
### 2.2. Cakupan Modul yang Diuji dalam UAT
### 2.3. Fitur yang Tidak Tercakup (Out-of-Scope UAT)
### 2.4. Kriteria Keberhasilan UAT Keseluruhan

---

## 3. Organisasi dan Peran UAT
### 3.1. Tim Pelaksana UAT
(Tabel: Peran | Nama/Jabatan | Tanggung Jawab)
### 3.2. Jadwal Pelaksanaan UAT
(Tabel: Sesi | Tanggal | Durasi | Penanggung Jawab | Cakupan Modul)

---

## 4. Prasyarat dan Kesiapan UAT (UAT Readiness Checklist)
### 4.1. Checklist Kesiapan Lingkungan
(Checklist [ ] format: hardware, software, jaringan, database, konfigurasi)
### 4.2. Checklist Kesiapan Data Uji
(Checklist [ ] format: akun uji, data master, data transaksi seed)
### 4.3. Checklist Kesiapan Dokumen
(Checklist [ ] format: Test Plan, Test Cases, UAT Script telah disetujui)
### 4.4. Kriteria Masuk UAT (Entry Criteria)

---

## 5. Skenario UAT — Sesi 1: Keamanan, Login, dan Hak Akses
### 5.1. UAT-001: Login Kasir dan Verifikasi Sesi JWT
### 5.2. UAT-002: Pengujian Pembatasan Hak Akses RBAC
### 5.3. UAT-003: Pengujian Lockout Brute-Force (5 kali gagal)
(Setiap skrip berformat tabel: ID UAT | Judul | Aktor Penguji |
Prasyarat | Data Uji | Langkah Pengujian (step-by-step) |
Hasil Diharapkan (terukur) | Hasil Aktual | Status PASS/FAIL |
Tanda Tangan Penguji)

---

## 6. Skenario UAT — Sesi 2: Alur Transaksi Kasir Harian
### 6.1. UAT-004: Penjualan Ritel ATK Tunai Multi-Item
### 6.2. UAT-005: Validasi Harga Dinamis (Retail/Grosir/Mitra)
### 6.3. UAT-006: Pembayaran DP dan Pelunasan Pesanan Kustom
### 6.4. UAT-007: Pembatalan DP dengan Eskalasi Sandi Pemilik
### 6.5. UAT-008: Retur Barang ATK Rusak
### 6.6. UAT-009: Ekspor Nota Struk Thermal (.txt)

---

## 7. Skenario UAT — Sesi 3: Operasional Inventaris dan BOM
### 7.1. UAT-010: Pendaftaran Master Barang dan Bahan Baku Baru
### 7.2. UAT-011: Perhitungan HPP Otomatis BOM (Stempel Flash)
### 7.3. UAT-012: Pencatatan Limbah Produksi
### 7.4. UAT-013: Sinkronisasi ATK Internal
### 7.5. UAT-014: Rekonsiliasi Stock Opname (Draft → Approve)
### 7.6. UAT-015: Analisis Prediksi Re-Order Stok
### 7.7. UAT-016: Price Tracking Supplier
### 7.8. UAT-017: Import CSV Bulk Data
### 7.9. UAT-018: Kelola Utang Supplier Tempo

---

## 8. Skenario UAT — Sesi 4: Layanan PPOB, Keuangan, dan Jasa
### 8.1. UAT-019: Kelola Saldo PPOB dan Alert Limit Kritis
### 8.2. UAT-020: Rekomendasi Biaya Admin E-Wallet Termurah
### 8.3. UAT-021: Registrasi Jasa Service Printer/Laptop

---

## 9. Skenario UAT — Sesi 5: SDM, Payroll, dan Poin Karyawan
### 9.1. UAT-022: Absensi Harian dan Kasbon Karyawan
### 9.2. UAT-023: Smart Payroll Skenario A dan Skenario B
### 9.3. UAT-024: Proteksi Upah Minimum 50% UMR
### 9.4. UAT-025: Pemotongan Kasbon Otomatis saat Payroll
### 9.5. UAT-026: Akumulasi Poin Insentif 4-Tier Karyawan

---

## 10. Skenario UAT — Sesi 6: Antrian, Desain, dan Notifikasi
### 10.1. UAT-027: Transisi Status Antrian Kerja Kustom (5 Tahap)
### 10.2. UAT-028: Perekaman Path Arsip File Desain
### 10.3. UAT-029: Pembuatan Tautan WhatsApp Web Siap Salin

---

## 11. Skenario UAT — Sesi 7: Pinjaman, Aset, dan Pengeluaran
### 11.1. UAT-030: Pencatatan Pinjaman Bank Berbunga
### 11.2. UAT-031: Pencatatan Pinjaman Kerabat Tanpa Bunga
### 11.3. UAT-032: Kalkulasi Depresiasi Garis Lurus Aset
### 11.4. UAT-033: Visualisasi Laba/Rugi Instan per Divisi
### 11.5. UAT-034: Notifikasi Jatuh Tempo Utang H-3
### 11.6. UAT-035: Pengeluaran Besar > Rp 500.000 Eskalasi

---

## 12. Skenario UAT — Sesi 8: CRM, Privasi, dan Multi-Cabang
### 12.1. UAT-036: Pendaftaran CRM dan Enkripsi Fernet WhatsApp
### 12.2. UAT-037: Penghapusan Permanen Data CRM (UU PDP)
### 12.3. UAT-038: Isolasi Data Multi-Cabang (cabang_id)

---

## 13. Skenario UAT — Sesi 9: Konfigurasi, Backup, dan Serah Terima
### 13.1. UAT-039: Modifikasi Parameter Bisnis Runtime
### 13.2. UAT-040: Backup Database ZIP AES-256
### 13.3. UAT-041: Restore Database dari Backup
### 13.4. UAT-042: Serah Terima Shift Kasir Normal
### 13.5. UAT-043: Serah Terima Shift Kasir Anomali (selisih > Rp 10.000)
### 13.6. UAT-044: Fraud Detection Alarm Visual

---

## 14. Skenario UAT — Sesi 10: Skenario Integrasi End-to-End Hari Operasional
### 14.1. UAT-E2E-001: Simulasi Hari Operasional Lengkap
(Skrip skenario panjang dari: buka toko → login → handover awal →
registrasi CRM → transaksi kasir multi-divisi → pengerjaan kustom
→ cetak & potong stok → pencatatan limbah → opname → laporan
laba rugi → tutup shift → rekonsiliasi kas → backup harian)

---

## 15. Pengujian Non-Fungsional UAT
### 15.1. UAT-NF-001: Kecepatan Respon Laporan Laba/Rugi < 2 Detik
### 15.2. UAT-NF-002: Navigasi CLI dan Visual ANSI
### 15.3. UAT-NF-003: Encoding UTF-8 Lintas OS

---

## 16. Prosedur Penanganan Temuan (Defect Handling)
### 16.1. Klasifikasi Tingkat Keparahan Temuan UAT
### 16.2. Template Pencatatan Temuan UAT
### 16.3. Prosedur Eskalasi Temuan

---

## 17. Kriteria Keluar UAT (Exit Criteria) dan Sign-Off
### 17.1. Kriteria Keluar UAT
### 17.2. Checklist Sign-Off UAT (7 Kriteria Terukur)
### 17.3. Formulir Tanda Tangan Persetujuan Go-Live
(Format tanda tangan resmi: Pemilik Usaha & Kepala Percetakan,
tempat, tanggal, status keputusan GO-LIVE / DITOLAK)

---

## 18. Lampiran
### 18.1. Glosarium Istilah UAT
### 18.2. Data Uji UAT (Test Fixtures)
### 18.3. Matriks Ketertelusuran UAT → Test Case → SRS → Use Case

---

## 19. Referensi Dokumen
(Tabel: No | Kode Ref | Nama Dokumen | Path File | Versi)
```

---

## 5. Tahapan Implementasi (Checklist Tugas)

Berikut adalah tahapan detail yang **harus diikuti secara berurutan** oleh pelaksana. Setiap checklist `[ ]` harus ditandai `[x]` setelah selesai dikerjakan.

### Fase 1: Persiapan dan Pembacaan Referensi

- [ ] **T-001:** Baca file `docs/sdlc/05_testing/01_test_plan.md` secara keseluruhan dari awal hingga akhir. Catat dan rangkum semua informasi berikut:
  - [ ] T-001a: Bab 3.1.4 — Definisi dan cakupan User Acceptance Testing (UAT).
  - [ ] T-001b: Bab 4.1 s.d 4.10 — Seluruh 44 skenario uji per modul (ID, deskripsi, SRS, UC, tipe, prioritas).
  - [ ] T-001c: Bab 10 — Spesifikasi lingkungan pengujian (hardware, software, jaringan).
  - [ ] T-001d: Bab 12.4 — Seluruh tabel Error Code → Test Validation Mapping.
  - [ ] T-001e: Bab 13.1 — Kriteria penerimaan pemilik usaha (3 kriteria akurasi, keamanan, kemandirian).
  - [ ] T-001f: Bab 13.2 — Kriteria penerimaan operasional harian (3 kriteria kecepatan, navigasi, alur produksi).
  - [ ] T-001g: Bab 13.3 — Checklist sign-off UAT 7 kriteria terukur beserta format tanda tangan.
  - [ ] T-001h: Bab 3.4 — Kriteria masuk, keluar, penangguhan, dan pelanjutan pengujian.

- [ ] **T-002:** Baca file `docs/sdlc/05_testing/02_test_cases.md` secara keseluruhan dari awal hingga akhir. Catat dan rangkum semua informasi berikut:
  - [ ] T-002a: Bab 2 — Ringkasan cakupan total 70 test cases (distribusi per modul, tipe, prioritas, tingkat pengujian).
  - [ ] T-002b: Bab 3.3 — Data uji global (Test Fixtures) berisi 8 akun penguji dengan username, peran, dan password.
  - [ ] T-002c: Bab 3.4 — Entry & Exit Criteria (5 exit criteria kuantitatif).
  - [ ] T-002d: Bab 3.5 — Ketergantungan eksekusi dan urutan pengujian (dependency map).
  - [ ] T-002e: Bab 4 s.d 13 — Seluruh kasus uji per modul M.1 s.d M.10 (happy path dan unhappy path), termasuk ID kasus uji, skenario asal, referensi SRS/UC, prakondisi, data uji, langkah uji, dan hasil diharapkan.
  - [ ] T-002f: Bab 14 s.d 18 — Seluruh kasus uji khusus (SEC, DEC, INT, CLI, NF) lengkap.
  - [ ] T-002g: Bab 19 — Matriks ketertelusuran test case → skenario test plan.
  - [ ] T-002h: Bab 20 — Data fixtures seed database (tabel pengguna, barang, bahan_baku).

- [ ] **T-003:** Baca file `docs/sdlc/02_analysis/02_software_requirements.md`. Catat dan rangkum:
  - [ ] T-003a: Seluruh kebutuhan fungsional SRS-F-001 s.d SRS-F-040 (ID, deskripsi, modul terkait).
  - [ ] T-003b: Seluruh kebutuhan non-fungsional SRS-NF-001 s.d SRS-NF-011.
  - [ ] T-003c: Batasan input, aturan validasi, dan logika kalkulasi bisnis yang relevan untuk UAT.

- [ ] **T-004:** Baca file `docs/sdlc/02_analysis/03_use_case_diagram.md`. Catat dan rangkum:
  - [ ] T-004a: Daftar 44 use case (UC-001 s.d UC-041) dengan aktor, alur utama, alur alternatif, dan alur pengecualian.
  - [ ] T-004b: Pre-condition dan post-condition setiap use case.

- [ ] **T-005:** Baca file `docs/sdlc/02_analysis/06_access_control_matrix.md`. Catat dan rangkum:
  - [ ] T-005a: Definisi 8 peran internal beserta deskripsi hak aksesnya.
  - [ ] T-005b: Matriks otorisasi menu/tabel CRUD per peran.

- [ ] **T-006:** Baca file `docs/sdlc/03_design/04_cli_interaction_flow.md`. Catat dan rangkum:
  - [ ] T-006a: Alur navigasi terminal CLI (menu utama, sub-menu, breadcrumb, tombol kembali `0`).
  - [ ] T-006b: Format rendering visual ANSI (rich & tabulate), kode warna error/warning/success.
  - [ ] T-006c: Format struk thermal (32 char & 48 char) dan text-wrapping.
  - [ ] T-006d: Format kode error visual `ERR-XXX-YYY`.

- [ ] **T-007:** Baca file `docs/sdlc/03_design/05_bom_hpp_design.md`. Catat dan rangkum:
  - [ ] T-007a: Formula matematika HPP BOM pecahan desimal presisi `Decimal(15,4)`.
  - [ ] T-007b: Aturan pembulatan `ROUND_HALF_UP` dan contoh perhitungan konkret.
  - [ ] T-007c: Mekanisme locking `FOR UPDATE` InnoDB untuk race condition stok.

- [ ] **T-008:** Baca file `docs/sdlc/03_design/06_security_design.md`. Catat dan rangkum:
  - [ ] T-008a: Spesifikasi bcrypt (cost factor 12), JWT (HS256, 8 jam/28.800 detik).
  - [ ] T-008b: Rate limiting (5 kali gagal, lock 10 menit).
  - [ ] T-008c: Enkripsi Fernet (CRM WhatsApp) dan AES-256 (Backup ZIP).
  - [ ] T-008d: Kepatuhan UU PDP No. 27/2022 (Right to Erasure).
  - [ ] T-008e: Sanitasi input CLI (strip ANSI escape codes).
  - [ ] T-008f: Audit Trail JSON (old_value & new_value).

- [ ] **T-009:** Baca file `docs/sdlc/02_analysis/04_workflow_diagram.md`. Catat dan rangkum:
  - [ ] T-009a: Alur kerja operasional harian toko (buka toko, shift handover, transaksi, produksi, tutup toko).
  - [ ] T-009b: Alur transisi status antrian kerja kustom (5 tahapan).
  - [ ] T-009c: Alur rekonsiliasi kas dan stock opname.

### Fase 2: Analisis dan Pemetaan Data

- [ ] **T-010:** Buat pemetaan (mapping) dari 44 skenario uji Test Plan → 70 test cases Test Cases → skrip UAT yang akan disusun. Setiap skenario uji harus terpetakan ke minimal 1 skrip UAT.

- [ ] **T-011:** Kelompokkan test cases yang saling berhubungan menjadi skenario bisnis end-to-end. Gunakan alur workflow operasional harian toko (R-WF) sebagai panduan pengelompokan:
  - [ ] T-011a: Kelompok Keamanan & Login (M.7).
  - [ ] T-011b: Kelompok Transaksi Kasir Harian (M.1).
  - [ ] T-011c: Kelompok Inventaris & BOM (M.2).
  - [ ] T-011d: Kelompok PPOB & Keuangan Digital (M.3).
  - [ ] T-011e: Kelompok SDM & Payroll (M.4).
  - [ ] T-011f: Kelompok Antrian & Desain (M.5).
  - [ ] T-011g: Kelompok Pinjaman & Aset (M.6).
  - [ ] T-011h: Kelompok CRM & Privasi (M.8).
  - [ ] T-011i: Kelompok Multi-Cabang & Config (M.9, M.10).
  - [ ] T-011j: Kelompok Backup, Handover, & Fraud (M.7 lanjutan).
  - [ ] T-011k: Skenario Integrasi End-to-End Hari Operasional Penuh.

- [ ] **T-012:** Identifikasi dan tandai semua data yang **tidak tersedia** di file referensi namun dibutuhkan oleh dokumen UAT Script. Tandai setiap data kosong dengan format:
  ```
  [DATA BELUM TERSEDIA - Perlu diisi manual oleh Pemilik Usaha]
  ```

### Fase 3: Penulisan Dokumen UAT Script

- [ ] **T-013:** Tulis bagian **Front Matter** (metadata YAML header) sesuai kerangka di Bab 4.
  ```yaml
  ---
  dokumen    : UAT Script
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : 2026-05-26
  status     : Draft
  penyusun   : Senior UAT Analyst & Business Acceptance Specialist
  ---
  ```

- [ ] **T-014:** Tulis bagian **Riwayat Perubahan Dokumen** (Tabel versi 1.0 dengan deskripsi inisialisasi awal).

- [ ] **T-015:** Tulis bagian **Bab 1 — Informasi Dokumen** secara lengkap:
  - [ ] T-015a: Bab 1.1 Tujuan Dokumen — jelaskan bahwa dokumen ini adalah skrip pengujian penerimaan pengguna akhir yang menjadi gerbang formal go/no-go sebelum peluncuran sistem.
  - [ ] T-015b: Bab 1.2 Cakupan Dokumen — cakupan total jumlah skrip UAT yang akan disusun.
  - [ ] T-015c: Bab 1.3 Posisi Dokumen dalam SDLC — gambar diagram posisi UAT Script sebagai deliverable ketiga di Fase 05 Testing, setelah Test Plan dan Test Cases.
  - [ ] T-015d: Bab 1.4 Hubungan dengan Dokumen SDLC — sebutkan dokumen input (Test Plan, Test Cases, SRS, UC) dan dokumen output (Test Report, Deployment Document).
  - [ ] T-015e: Bab 1.5 Audiens Target — Pemilik Usaha, Kepala Percetakan, Junior Programmer, AI Testing Agent.
  - [ ] T-015f: Bab 1.6 Definisi, Akronim, dan Singkatan — adopsi dari Test Plan Bab 1.6 dan tambahkan istilah khusus UAT.

- [ ] **T-016:** Tulis bagian **Bab 2 — Lingkup dan Tujuan UAT** secara lengkap:
  - [ ] T-016a: Bab 2.1 — Tujuan pengujian penerimaan (verifikasi kelayakan bisnis operasional harian).
  - [ ] T-016b: Bab 2.2 — Daftar 10 modul yang dicakup UAT beserta ringkasan fitur kunci yang diuji.
  - [ ] T-016c: Bab 2.3 — Fitur yang tidak tercakup UAT (sama dengan Out-of-Scope Test Plan).
  - [ ] T-016d: Bab 2.4 — Kriteria keberhasilan UAT keseluruhan (adopsi dan adaptasi dari Test Plan Bab 13).

- [ ] **T-017:** Tulis bagian **Bab 3 — Organisasi dan Peran UAT**:
  - [ ] T-017a: Bab 3.1 — Tabel tim pelaksana UAT (Pemilik Usaha, Kepala Percetakan, QA Lead, Junior Programmer).
  - [ ] T-017b: Bab 3.2 — Jadwal pelaksanaan UAT per sesi (estimasi 10 sesi berdasarkan pengelompokan modul).

- [ ] **T-018:** Tulis bagian **Bab 4 — Prasyarat dan Kesiapan UAT**:
  - [ ] T-018a: Bab 4.1 — Checklist `[ ]` kesiapan lingkungan (hardware, software, jaringan, database, konfigurasi).
  - [ ] T-018b: Bab 4.2 — Checklist `[ ]` kesiapan data uji (adopsi dari Test Cases Bab 3.3 Test Fixtures).
  - [ ] T-018c: Bab 4.3 — Checklist `[ ]` kesiapan dokumen (Test Plan, Test Cases, UAT Script disetujui).
  - [ ] T-018d: Bab 4.4 — Kriteria masuk UAT (adopsi dan adaptasi dari Test Plan Bab 3.4.1).

- [ ] **T-019:** Tulis bagian **Bab 5 s.d 13 — Skrip UAT per Sesi** sesuai kerangka. Untuk **setiap skrip UAT individual**, gunakan format tabel berikut:

  ```markdown
  | Atribut UAT | Detail |
  |---|---|
  | **ID Skrip UAT** | UAT-XXX |
  | **Judul** | [Judul deskriptif skenario bisnis] |
  | **Skenario Asal (Test Plan)** | M[X]-TC-[XXX] |
  | **Test Case Terkait** | TC-M[X]-[XXX]-[XX] |
  | **Referensi SRS / UC** | SRS-F-[XXX] / UC-[XXX] |
  | **Modul / Fitur** | M.[X] — [Nama Modul] |
  | **Aktor Penguji** | Pemilik Usaha / Kepala Percetakan |
  | **Lingkungan** | PC Kasir Windows 11, Terminal CLI AbuCom, DB abucom_test_db |
  | **Prasyarat** | [Kondisi yang harus dipenuhi sebelum memulai] |
  | **Data Uji** | [Data konkret dengan angka presisi desimal] |
  | **Langkah Pengujian** | 1. [Langkah 1 berbahasa bisnis, bukan teknis]<br>2. [Langkah 2]<br>... |
  | **Hasil Diharapkan** | [Kriteria kelulusan terukur dan deterministik] |
  | **Hasil Aktual** | *[Diisi saat eksekusi UAT]* |
  | **Status** | *[Diisi saat eksekusi: PASS / FAIL]* |
  | **Catatan Temuan** | *[Diisi jika ada temuan/bug]* |
  | **Tanda Tangan Penguji** | _____________ |
  ```

  Pastikan untuk setiap sesi (Bab 5 s.d 13):
  - [ ] T-019a: Tulis semua skrip UAT untuk Sesi 1 (Keamanan, Login, Hak Akses) — min. 3 skrip.
  - [ ] T-019b: Tulis semua skrip UAT untuk Sesi 2 (Transaksi Kasir Harian) — min. 6 skrip.
  - [ ] T-019c: Tulis semua skrip UAT untuk Sesi 3 (Inventaris dan BOM) — min. 9 skrip.
  - [ ] T-019d: Tulis semua skrip UAT untuk Sesi 4 (PPOB, Keuangan, Jasa) — min. 3 skrip.
  - [ ] T-019e: Tulis semua skrip UAT untuk Sesi 5 (SDM, Payroll, Poin) — min. 5 skrip.
  - [ ] T-019f: Tulis semua skrip UAT untuk Sesi 6 (Antrian, Desain, Notifikasi) — min. 3 skrip.
  - [ ] T-019g: Tulis semua skrip UAT untuk Sesi 7 (Pinjaman, Aset, Pengeluaran) — min. 6 skrip.
  - [ ] T-019h: Tulis semua skrip UAT untuk Sesi 8 (CRM, Privasi, Multi-Cabang) — min. 3 skrip.
  - [ ] T-019i: Tulis semua skrip UAT untuk Sesi 9 (Konfigurasi, Backup, Serah Terima) — min. 6 skrip.

- [ ] **T-020:** Tulis bagian **Bab 14 — Skenario Integrasi End-to-End Hari Operasional**:
  - [ ] T-020a: Susun skrip UAT panjang yang mensimulasikan 1 hari operasional toko lengkap, dari buka toko hingga tutup shift dan backup harian.
  - [ ] T-020b: Skrip harus menyebutkan urutan langkah demi langkah, dengan referensi silang ke skrip UAT individual yang sudah ditulis di Bab 5-13.

- [ ] **T-021:** Tulis bagian **Bab 15 — Pengujian Non-Fungsional UAT**:
  - [ ] T-021a: Kecepatan respon laporan laba/rugi < 2 detik (dari perspektif pengguna).
  - [ ] T-021b: Kenyamanan navigasi CLI dan kontras visual ANSI (dari perspektif pengguna).
  - [ ] T-021c: Keterampilan visual UTF-8 lintas OS (dari perspektif pengguna).

- [ ] **T-022:** Tulis bagian **Bab 16 — Prosedur Penanganan Temuan (Defect Handling)**:
  - [ ] T-022a: Bab 16.1 — Klasifikasi tingkat keparahan temuan UAT (Blocker, Critical, Major, Minor, Cosmetic).
  - [ ] T-022b: Bab 16.2 — Template pencatatan temuan UAT (ID Temuan, Judul, Tingkat, Langkah Reproduksi, Hasil Aktual, Hasil Diharapkan, Screenshot/Log).
  - [ ] T-022c: Bab 16.3 — Prosedur eskalasi temuan (siapa yang harus dihubungi, batas waktu perbaikan, proses retest).

- [ ] **T-023:** Tulis bagian **Bab 17 — Kriteria Keluar UAT dan Sign-Off**:
  - [ ] T-023a: Bab 17.1 — Kriteria keluar UAT kuantitatif (adopsi dan adaptasi dari Test Plan Bab 3.4.2).
  - [ ] T-023b: Bab 17.2 — Checklist sign-off UAT 7 kriteria terukur (adopsi dari Test Plan Bab 13.3), format:
    ```
    [ ] Kriteria 1: Seluruh 44 Use Case telah lolos uji kelayakan bisnis tanpa crash.
    [ ] Kriteria 2: Proteksi upah minimum 50% UMR (Rp 1.600.000) Smart Payroll berfungsi.
    [ ] Kriteria 3: Toleransi selisih kas handover kasir Rp 10.000 bekerja presisi desimal.
    [ ] Kriteria 4: Enkripsi nomor WhatsApp CRM pelanggan (Fernet) tersimpan acak di DB.
    [ ] Kriteria 5: Pemotongan stok bahan desimal mendukung sisa stok negatif (alert kuning).
    [ ] Kriteria 6: Kecepatan response time laporan Laba/Rugi instan < 2 detik.
    [ ] Kriteria 7: Ekspor backup database ZIP terenkripsi AES-256 menolak pembongkaran ilegal.
    ```
  - [ ] T-023c: Bab 17.3 — Formulir tanda tangan persetujuan go-live formal:
    ```
    Dibuat di  : [Kota], [Provinsi]
    Pada tanggal: [Tanggal]

    Keputusan UAT:
    [ ] DITERIMA UNTUK PRODUKSI (GO-LIVE)
    [ ] DITOLAK (BUTUH PERBAIKAN)

    Pihak Penyetuju,


    (_______________________)                   (_______________________)
          Pemilik Usaha                            Kepala Percetakan
    ```

- [ ] **T-024:** Tulis bagian **Bab 18 — Lampiran**:
  - [ ] T-024a: Bab 18.1 — Glosarium istilah UAT (adopsi dari Test Plan Bab 1.6 dan 14.1, tambahkan istilah khusus UAT).
  - [ ] T-024b: Bab 18.2 — Data uji UAT (adopsi dari Test Cases Bab 3.3 dan Bab 20).
  - [ ] T-024c: Bab 18.3 — Matriks ketertelusuran UAT → Test Case → SRS → Use Case (tabel lengkap dari UAT-001 s.d UAT-E2E-001).

- [ ] **T-025:** Tulis bagian **Bab 19 — Referensi Dokumen**:
  - [ ] T-025a: Buat tabel referensi lengkap semua file yang digunakan (9 file referensi sesuai daftar di Bab 2 issue ini).

### Fase 4: Validasi dan Finalisasi

- [ ] **T-026:** Validasi kelengkapan dokumen:
  - [ ] T-026a: Pastikan seluruh 44 skenario uji dari Test Plan telah terpetakan ke minimal 1 skrip UAT.
  - [ ] T-026b: Pastikan seluruh 7 kriteria sign-off UAT tercantum di Bab 17.2.
  - [ ] T-026c: Pastikan seluruh 10 modul (M.1 s.d M.10) tercakup dalam skrip UAT.
  - [ ] T-026d: Pastikan tidak ada data placeholder `[DATA BELUM TERSEDIA]` yang sebenarnya sudah tersedia di file referensi.
  - [ ] T-026e: Pastikan semua referensi silang (ID Test Case, ID SRS, ID Use Case) akurat dan konsisten.

- [ ] **T-027:** Validasi format dan bahasa:
  - [ ] T-027a: Pastikan semua tabel terformat rapi dan konsisten.
  - [ ] T-027b: Pastikan bahasa Indonesia natural, tidak ambigu, dan mudah dipahami.
  - [ ] T-027c: Pastikan semua angka presisi desimal menggunakan format `Decimal('X.XXXX')` atau `Rp X.XXX,XXXX` secara konsisten.
  - [ ] T-027d: Pastikan semua kode error menggunakan format `ERR-XXX-YYY` yang konsisten dengan Test Plan Bab 12.4.

- [ ] **T-028:** Tulis hasil final ke target file:
  - [ ] T-028a: Tuangkan seluruh isi dokumen UAT Script yang sudah lengkap dan tervalidasi ke file `docs/sdlc/05_testing/03_uat_script.md`.
  - [ ] T-028b: Pastikan file ditulis secara **lengkap dan utuh** (tidak terpotong, tidak ada bagian yang di-truncate).
  - [ ] T-028c: Pastikan encoding file adalah **UTF-8 tanpa BOM**.

---

## 6. Catatan Penting untuk Pelaksana

> **PERINGATAN KRITIS:**
> 1. **JANGAN membuat data atau informasi yang tidak ada di file referensi.** Jika data tidak tersedia, tandai dengan `[DATA BELUM TERSEDIA]`. Halusinasi data adalah pelanggaran fatal.
> 2. **JANGAN menyingkat atau merangkas isi skrip UAT.** Setiap skrip harus lengkap dan detail. Lebih baik panjang tapi lengkap daripada pendek tapi ambigu.
> 3. **JANGAN mengubah ID test case, kode error, atau data presisi desimal** yang sudah ditetapkan di file referensi. Salin dengan presisi mutlak.
> 4. **JANGAN melompati tahapan checklist.** Kerjakan secara berurutan dari T-001 hingga T-028.
> 5. **Penulisan file harus dilakukan secara UTUH dan LENGKAP** dalam satu kali penulisan. Tidak boleh ada bagian yang terpotong atau perlu dilanjutkan di sesi berikutnya.
> 6. **Dokumen UAT Script ini adalah gerbang formal terakhir** sebelum sistem diluncurkan ke produksi. Kualitasnya harus setara dengan dokumen UAT praktik industri sesungguhnya.

---

## 7. Referensi Issue

| No | Kode Ref | Nama Dokumen | Path File | Versi |
|----|----------|--------------|-----------|-------|
| 1 | R-TP | Test Plan v1.1 | `docs/sdlc/05_testing/01_test_plan.md` | 1.1 |
| 2 | R-TC | Test Cases v1.1 | `docs/sdlc/05_testing/02_test_cases.md` | 1.1 |
| 3 | R-SRS | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | 1.1 |
| 4 | R-UC | Use Case Diagram v1.1 | `docs/sdlc/02_analysis/03_use_case_diagram.md` | 1.1 |
| 5 | R-ACM | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | 1.1 |
| 6 | R-CLI | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | 1.1 |
| 7 | R-BOM | BOM & HPP Design v1.1 | `docs/sdlc/03_design/05_bom_hpp_design.md` | 1.1 |
| 8 | R-SEC | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | 1.1 |
| 9 | R-WF | Workflow Diagram v1.1 | `docs/sdlc/02_analysis/04_workflow_diagram.md` | 1.1 |
