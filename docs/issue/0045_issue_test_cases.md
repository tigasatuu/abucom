---
judul      : Pembuatan dan Penyusunan Dokumen Test Cases — AbuCom
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
tanggal    : 2026-05-26
status     : Open
prioritas  : High
target     : docs/sdlc/05_testing/02_test_cases.md
assignee   : Junior Programmer / AI Model Agent
---

# Pembuatan dan Penyusunan Dokumen Test Cases

## 1. Ringkasan Issue

Issue ini berisi perencanaan low-level untuk pembuatan dan penyusunan dokumen **Test Cases** proyek AbuCom CLI. Dokumen Test Cases merupakan deliverable kedua pada **Fase 05 — Testing** dalam siklus SDLC. Dokumen ini menjabarkan kasus uji terperinci (*detailed test cases*) yang diturunkan langsung dari skenario pengujian (*test scenarios*) yang telah didefinisikan di dalam dokumen Test Plan v1.1.

**Posisi dalam SDLC:**
```
FASE 05: TESTING — Test Plan v1.1 [SELESAI]
                        |
                        v
FASE 05: TESTING — Test Cases [DOKUMEN INI — TARGET PEMBUATAN]
                        |
                        v
FASE 05: TESTING — Test Scripts & Execution
```

---

## 2. Persona Pelaksana

**Persona:** `Senior QA Engineer & Test Case Design Specialist`

**Justifikasi pemilihan persona:**
- Persona ini memiliki otoritas dan keahlian utama dalam menerjemahkan skenario pengujian strategis (dari Test Plan) menjadi kasus uji operasional yang granular, terstruktur, dan dapat dieksekusi.
- Persona ini memahami standar penulisan test case industri (IEEE 829 / ISO/IEC/IEEE 29119-3), mampu mendefinisikan prakondisi, langkah uji deterministik, data uji presisi desimal, expected result yang terukur, dan kriteria kelulusan per kasus uji.
- Persona ini mampu memastikan ketertelusuran (*traceability*) dua arah dari setiap test case kembali ke skenario Test Plan, Use Case (UC), dan kebutuhan fungsional SRS.

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca dan dirangkum** secara menyeluruh untuk pembuatan dokumen Test Cases ini. File diurutkan berdasarkan tingkat relevansi (PRIMER → TERSIER):

### 3.1. Referensi PRIMER (Wajib — Sumber Data Utama)

| No | Kode | Nama Dokumen | Path File | Kegunaan |
|----|------|--------------|-----------|----------|
| 1 | **R-TP** | Test Plan v1.1 | `docs/sdlc/05_testing/01_test_plan.md` | **Referensi utama #1** — Sumber definisi 44 skenario uji (Bab 4), strategi pengujian (Bab 3), template test case (Bab 14.2), kriteria masuk/keluar (Bab 3.4), matriks ketertelusuran (Bab 12), kode error mapping (Bab 12.4), data pengujian/fixtures (Bab 10.4), dan lingkungan uji (Bab 10). |
| 2 | **R-SRS** | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | **Referensi utama #2** — Sumber spesifikasi teknis setiap kebutuhan fungsional (SRS-F-001 s.d SRS-F-040+), input/output, aturan validasi, proses logika bisnis, dan kode error penanganan pengecualian yang menjadi basis penulisan expected result test case. |
| 3 | **R-UC** | Use Case Diagram v1.1 | `docs/sdlc/02_analysis/03_use_case_diagram.md` | **Referensi utama #3** — Sumber alur utama (Main Flow), alur alternatif (Alternative Flow), alur pengecualian (Exception Flow), prakondisi, dan pasca-kondisi dari 44 use case yang menjadi basis penulisan langkah uji (test steps). |

### 3.2. Referensi SEKUNDER (Wajib — Detail Teknis Pendukung)

| No | Kode | Nama Dokumen | Path File | Kegunaan |
|----|------|--------------|-----------|----------|
| 4 | **R-ACM** | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Matriks otorisasi RBAC 8 peran untuk menetapkan aktor/peran pada setiap test case dan menyusun test case negatif otorisasi ilegal. |
| 5 | **R-SEC** | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | Spesifikasi bcrypt cost 12, JWT HS256 8 jam, rate limiting 5x/lock 10 menit, Fernet CRM, AES-256 backup, audit log JSON, sanitasi CLI, dan kepatuhan UU PDP untuk penulisan test case keamanan. |
| 6 | **R-BOM** | BOM & HPP Design v1.1 | `docs/sdlc/03_design/05_bom_hpp_design.md` | Spesifikasi kalkulasi presisi desimal HPP BOM, formula `Decimal(15,4)`, `ROUND_HALF_UP`, locking `FOR UPDATE`, dan sinkronisasi ATK untuk penulisan test case presisi desimal. |
| 7 | **R-CLI** | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur navigasi terminal, breadcrumb, ANSI formatting `rich` & `tabulate`, thermal print wrapping, dan visual error `ERR-XXX-YYY` untuk penulisan test case antarmuka CLI. |
| 8 | **R-DB** | Database Schema v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | Definisi DDL tabel, constraint, tipe data kolom `DECIMAL(15,4)`, foreign key, dan CHECK constraint untuk memastikan expected result database akurat. |
| 9 | **R-ERD** | ERD Database v1.1 | `docs/sdlc/03_design/02_erd_database.md` | Diagram relasi antar-entitas untuk memahami alur data lintas tabel saat menyusun test case integrasi dan verifikasi database. |

### 3.3. Referensi TERSIER (Opsional — Konteks Tambahan)

| No | Kode | Nama Dokumen | Path File | Kegunaan |
|----|------|--------------|-----------|----------|
| 10 | **R-SA** | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` | Arsitektur client-server LAN, pooling, retry mechanism, untuk konteks test case konektivitas. |
| 11 | **R-CS** | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` | Standar FP pure functions, penamaan, dan aturan kode untuk memahami boundary white-box. |
| 12 | **R-MS** | Module Structure v1.1 | `docs/sdlc/04_implementation/03_module_structure.md` | Susunan folder dan modul Python untuk pemetaan lokasi logic yang diuji. |
| 13 | **R-DD** | Data Dictionary v1.1 | `docs/sdlc/02_analysis/05_data_dictionary.md` | Definisi atribut data dan tipe kolom untuk validasi expected result pada level data. |
| 14 | **R-WF** | Workflow Diagram v1.1 | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Alur kerja bisnis antar-modul untuk memahami cross-module integration test. |
| 15 | **R-ENV** | Environment Setup v1.1 | `docs/sdlc/04_implementation/02_environment_setup.md` | Konfigurasi lingkungan untuk verifikasi prakondisi test environment. |
| 16 | **R-BRD** | Business Requirements Document v1.1 | `docs/sdlc/02_analysis/01_business_requirements.md` | Kebutuhan bisnis dasar untuk konteks validasi UAT test case. |

> **Catatan:** File `narasi.txt` (`docs/sdlc/narasi.txt`) **TIDAK diperlukan lagi** sebagai referensi langsung untuk pembuatan dokumen Test Cases ini, karena seluruh data yang relevan dari narasi sudah diserap dan diformalisasikan di dalam dokumen SRS v1.1, Use Case Diagram v1.1, dan Test Plan v1.1.

---

## 4. Kerangka Struktur Dokumen Test Cases

Berikut adalah kerangka struktur standar dokumen Test Cases yang harus diikuti. Kerangka ini mengadopsi standar IEEE 829 / ISO/IEC/IEEE 29119-3 yang disesuaikan untuk konteks proyek AbuCom:

```
---
(Front Matter / Metadata YAML)
---

# Test Cases — AbuCom

## Riwayat Perubahan Dokumen
(Tabel versi, tanggal, deskripsi perubahan, dan persona pelaksana)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan
### 1.7. Konvensi Penulisan Test Case
    (Penjelasan format tabel yang dipakai, arti kolom, cara membaca)

---

## 2. Ringkasan Cakupan Test Case
### 2.1. Total Test Case per Modul (Tabel Ringkasan Kuantitatif)
### 2.2. Distribusi Test Case per Tipe Pengujian
### 2.3. Distribusi Test Case per Prioritas
### 2.4. Distribusi Test Case per Tingkat Pengujian (Unit/Integration/System/UAT)

---

## 3. Lingkungan Pengujian & Prakondisi Global
### 3.1. Spesifikasi Lingkungan (Ringkas dari Test Plan Bab 10)
### 3.2. Prakondisi Global (Berlaku untuk Semua Test Case)
### 3.3. Data Uji Global (Test Fixtures — Daftar Data Seed)

---

## 4. Test Cases — Modul M.1: Manajemen Transaksi & Kebijakan Harga
### 4.1. TC-M1-001: [Nama Test Case dari Skenario M1-TC-001]
    (Tabel test case detail per atribut)
### 4.2. TC-M1-002: ...
### 4.3. TC-M1-003: ...
    (... lanjut untuk semua skenario M1-TC-001 s.d M1-TC-007)
    (Setiap skenario BISA memiliki lebih dari 1 test case —
     misal: 1 test case positif + 1 test case negatif + 1 test case boundary)

---

## 5. Test Cases — Modul M.2: Manajemen Inventaris, BOM & Stock Opname
### 5.1. TC-M2-001: ...
    (... lanjut untuk semua skenario M2-TC-001 s.d M2-TC-010)

---

## 6. Test Cases — Modul M.3: Layanan Keuangan Digital, PPOB & Jasa Service
### 6.1. TC-M3-001: ...
    (... lanjut untuk semua skenario M3-TC-001 s.d M3-TC-003)

---

## 7. Test Cases — Modul M.4: Manajemen SDM, Penggajian & Poin Karyawan
### 7.1. TC-M4-001: ...
    (... lanjut untuk semua skenario M4-TC-001 s.d M4-TC-005)

---

## 8. Test Cases — Modul M.5: Sistem Manajemen Antrian & Pelacakan Desain
### 8.1. TC-M5-001: ...
    (... lanjut untuk semua skenario M5-TC-001 s.d M5-TC-003)

---

## 9. Test Cases — Modul M.6: Administrasi Pinjaman, Aset & Pengeluaran
### 9.1. TC-M6-001: ...
    (... lanjut untuk semua skenario M6-TC-001 s.d M6-TC-005)

---

## 10. Test Cases — Modul M.7: Keamanan, Audit Trail & Hak Akses
### 10.1. TC-M7-001: ...
    (... lanjut untuk semua skenario M7-TC-001 s.d M7-TC-007)

---

## 11. Test Cases — Modul M.8: CRM & Perlindungan Data Pelanggan
### 11.1. TC-M8-001: ...
    (... lanjut untuk semua skenario M8-TC-001 s.d M8-TC-002)

---

## 12. Test Cases — Modul M.9: Skalabilitas Multi-Cabang
### 12.1. TC-M9-001: ...
    (... lanjut untuk skenario M9-TC-001)

---

## 13. Test Cases — Modul M.10: Konfigurasi Sistem Runtime
### 13.1. TC-M10-001: ...
    (... lanjut untuk skenario M10-TC-001)

---

## 14. Test Cases — Pengujian Keamanan (Security Testing)
### 14.1. TC-SEC-001: Pengujian Otentikasi bcrypt & JWT
### 14.2. TC-SEC-002: Pengujian Otorisasi RBAC Ilegal
### 14.3. TC-SEC-003: Pengujian SQL Injection
### 14.4. TC-SEC-004: Pengujian Rate Limiting & Lockout
### 14.5. TC-SEC-005: Pengujian Sanitasi Input CLI
### 14.6. TC-SEC-006: Pengujian Audit Trail JSON
### 14.7. TC-SEC-007: Pengujian Enkripsi AES-256 & Fernet
### 14.8. TC-SEC-008: Pengujian Kepatuhan UU PDP

---

## 15. Test Cases — Pengujian Presisi Desimal (Decimal Precision Testing)
### 15.1. TC-DEC-001: Kalkulasi HPP BOM Desimal
### 15.2. TC-DEC-002: Pembulatan ROUND_HALF_UP Boundary
### 15.3. TC-DEC-003: Mutasi Kas & Rekonsiliasi Presisi
### 15.4. TC-DEC-004: Pemotongan Stok Desimal Non-Integer
### 15.5. TC-DEC-005: Smart Payroll & Depresiasi Aset

---

## 16. Test Cases — Pengujian Integrasi & Konektivitas
### 16.1. TC-INT-001: Connection Pooling & Retry Mechanism
### 16.2. TC-INT-002: ACID Transaction Block Rollback
### 16.3. TC-INT-003: Cross-Module Integration (M.5 → M.2 → M.1 → M.7)
### 16.4. TC-INT-004: Konektivitas LAN Client-Server
### 16.5. TC-INT-005: Portabilitas Dual-OS (Windows 11 & Debian 12)

---

## 17. Test Cases — Pengujian Antarmuka CLI
### 17.1. TC-CLI-001: Navigasi Menu & Breadcrumb
### 17.2. TC-CLI-002: Rendering Visual rich & tabulate
### 17.3. TC-CLI-003: Format Struk Thermal (58mm & 80mm)
### 17.4. TC-CLI-004: Encoding UTF-8 Lintas OS
### 17.5. TC-CLI-005: Kode Error Visual ERR-XXX-YYY

---

## 18. Test Cases — Pengujian Non-Fungsional
### 18.1. TC-NF-001: Performa Response Time < 2 Detik
### 18.2. TC-NF-002: Ketersediaan Uptime & UPS Graceful Shutdown
### 18.3. TC-NF-003: Backup & Restore Database
### 18.4. TC-NF-004: Import CSV Bulk Data
### 18.5. TC-NF-005: Kapasitas Data 50.000 Record

---

## 19. Matriks Ketertelusuran Test Case (Test Case Traceability Matrix)
### 19.1. Test Case → Skenario Test Plan Mapping
### 19.2. Test Case → SRS Fungsional Mapping
### 19.3. Test Case → Use Case Mapping
### 19.4. Test Case → Kode Error Mapping
### 19.5. Ringkasan Statistik Cakupan (Coverage Summary)

---

## 20. Lampiran
### 20.1. Glosarium Istilah Pengujian
### 20.2. Contoh Data Seed Test Fixtures (Tabel Representatif)
### 20.3. Template Defect Report (Referensi Silang Test Plan Bab 11.4)

---

## 21. Referensi Dokumen
(Daftar lengkap file referensi yang digunakan dalam penyusunan dokumen ini)
```

### Format Tabel Test Case per Item

Setiap test case **wajib** ditulis dalam format tabel berikut (mengadopsi template dari Test Plan Bab 14.2 dan diperluas):

```markdown
| Atribut Uji | Spesifikasi Uji Detail |
|---|---|
| **ID Kasus Uji** | TC-M1-001-01 |
| **Nama Kasus Uji** | [Nama deskriptif test case] |
| **Skenario Asal (Test Plan)** | M1-TC-001 |
| **Referensi SRS** | SRS-F-001 |
| **Referensi Use Case** | UC-001 |
| **Modul / Fitur** | M.1 — Transaksi & Kasir |
| **Tipe Pengujian** | Functional / Security / Precision / Boundary / Database / CLI / Integration / Integrity |
| **Tingkat Pengujian** | Unit / Integration / System / UAT |
| **Prioritas** | High / Medium / Low |
| **Peran Aktor** | `kasir` |
| **Prakondisi** | [Daftar bernomor kondisi awal yang harus terpenuhi sebelum eksekusi] |
| **Data Uji (Test Data)** | [Nilai input spesifik, angka, string, ID — BUKAN placeholder abstrak] |
| **Langkah Uji (Test Steps)** | [Daftar bernomor langkah-langkah eksekusi yang deterministik] |
| **Hasil Diharapkan (Expected Result)** | [Daftar bernomor hasil terukur, nilai database, pesan CLI, kode error spesifik] |
| **Hasil Aktual (Actual Result)** | *[Diisi saat eksekusi pengujian]* |
| **Status Uji** | *[Diisi saat eksekusi pengujian: PASS / FAIL / BLOCKED / SKIPPED]* |
| **Catatan Tambahan** | [Catatan khusus, ketergantungan, atau informasi krusial] |
```

### Konvensi Penamaan ID Test Case

Format: `TC-[MODUL]-[SKENARIO]-[NOMOR_URUT]`

- **TC** = Test Case
- **MODUL** = Kode modul (M1, M2, ..., M10, SEC, DEC, INT, CLI, NF)
- **SKENARIO** = Nomor skenario dari Test Plan (001, 002, dst.)
- **NOMOR_URUT** = Nomor urut test case dalam skenario tersebut (01, 02, 03...)

Contoh:
- `TC-M1-001-01` = Test Case positif pertama untuk skenario M1-TC-001
- `TC-M1-001-02` = Test Case negatif kedua untuk skenario M1-TC-001
- `TC-SEC-001-01` = Test Case pertama untuk pengujian otentikasi bcrypt
- `TC-DEC-001-01` = Test Case pertama untuk kalkulasi HPP BOM desimal

### Ekspansi Test Case per Skenario

Setiap skenario dari Test Plan **harus** di-ekspansi menjadi minimal:
1. **1 Test Case Positif (Happy Path):** Alur utama berhasil tanpa error.
2. **1 Test Case Negatif (Unhappy Path):** Input salah, hak akses ditolak, atau kondisi error.
3. **1 Test Case Boundary (jika relevan):** Nilai batas minimum, maksimum, dan edge case.

Untuk skenario yang kompleks (misal: Smart Payroll memiliki Skenario A dan B), boleh menambahkan test case tambahan sesuai kebutuhan.

---

## 5. Instruksi Detail Pembuatan Dokumen

### 5.1. Fase 1 — Persiapan dan Pembacaan File Referensi

> **Tujuan:** Membaca dan memahami seluruh file referensi yang menjadi basis penulisan test case.

- [ ] **Tugas 1.1:** Baca file **Test Plan v1.1** (`docs/sdlc/05_testing/01_test_plan.md`) secara menyeluruh dari Bab 1 hingga Bab 15. Fokus utama pada:
  - [ ] Bab 4 (Pemetaan Cakupan Pengujian per Modul) — Catat semua 44 skenario uji (ID, deskripsi, SRS terkait, UC terkait, tipe test, prioritas).
  - [ ] Bab 3 (Strategi Pengujian) — Catat kriteria masuk/keluar (entry/exit criteria), tingkat pengujian, dan pendekatan pengujian.
  - [ ] Bab 5-9 (Pengujian Keamanan, Presisi Desimal, Integrasi, CLI, Non-Fungsional) — Catat setiap detail skenario pengujian beserta angka-angka spesifiknya.
  - [ ] Bab 10 (Lingkungan Pengujian) — Catat spesifikasi hardware, software, database test, fixtures, dan konfigurasi .env.
  - [ ] Bab 12 (Matriks Ketertelusuran) — Catat semua mapping SRS → Test, UC → Test, dan Kode Error → Test.
  - [ ] Bab 14.2 (Template Test Case) — Catat format template resmi yang menjadi acuan.
  - [ ] Bab 12.4 (Kode Error → Test Validation Mapping) — Catat seluruh 15 kode error dan pesan terkait.

- [ ] **Tugas 1.2:** Baca file **SRS v1.1** (`docs/sdlc/02_analysis/02_software_requirements.md`) secara menyeluruh. Fokus pada:
  - [ ] Bab 3 (Spesifikasi Kebutuhan Fungsional SRS-F-001 s.d SRS-F-040+) — Untuk setiap SRS-F, catat: input, proses/logika bisnis, output, aturan validasi, penanganan pengecualian (kode error), dan ketergantungan.
  - [ ] Bab 4 (Kebutuhan Non-Fungsional SRS-NF-001 s.d SRS-NF-011) — Catat metrik terukur setiap kebutuhan non-fungsional.
  - [ ] Bab 3.x (SRS-F-ADD-01 s.d SRS-F-ADD-05) — Catat kebutuhan fungsional tambahan (startup validation, auto-logout, pooling, retry, AES-256).

- [ ] **Tugas 1.3:** Baca file **Use Case Diagram v1.1** (`docs/sdlc/02_analysis/03_use_case_diagram.md`) secara menyeluruh. Fokus pada:
  - [ ] Bab 5 (Spesifikasi Naratif Use Case) — Untuk setiap UC (UC-001 s.d UC-044), catat: alur utama (main flow), alur alternatif (alternative flow), alur pengecualian (exception flow), prakondisi, pasca-kondisi, dan aturan bisnis.

- [ ] **Tugas 1.4:** Baca file **Access Control Matrix v1.1** (`docs/sdlc/02_analysis/06_access_control_matrix.md`). Catat:
  - [ ] Matriks otorisasi 8 peran (pemilik, kepala_percetakan, pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang) terhadap menu dan operasi CRUD.

- [ ] **Tugas 1.5:** Baca file **Security Design v1.1** (`docs/sdlc/03_design/06_security_design.md`). Catat:
  - [ ] Detail spesifikasi bcrypt cost 12, JWT HS256 expiry 28.800 detik, rate limiting 5 kali/lock 10 menit, Fernet CRM, AES-256 backup, audit log JSON schema, sanitasi CLI, dan prosedur kepatuhan UU PDP.

- [ ] **Tugas 1.6:** Baca file **BOM & HPP Design v1.1** (`docs/sdlc/03_design/05_bom_hpp_design.md`). Catat:
  - [ ] Formula kalkulasi HPP BOM desimal, tipe data `Decimal(15,4)`, aturan pembulatan `ROUND_HALF_UP`, mekanisme locking `FOR UPDATE` InnoDB, contoh kalkulasi numerik, dan sinkronisasi ATK.

- [ ] **Tugas 1.7:** Baca file **CLI Interaction Flow v1.1** (`docs/sdlc/03_design/04_cli_interaction_flow.md`). Catat:
  - [ ] Alur navigasi terminal, format breadcrumb, rendering ANSI `rich` & `tabulate`, layout struk thermal wrapping (32 char / 48 char), dan format visual kode error `ERR-XXX-YYY`.

- [ ] **Tugas 1.8:** Baca file **Database Schema v1.1** (`docs/sdlc/03_design/01_database_schema.sql`). Catat:
  - [ ] Definisi DDL tabel utama (transaksi, detail_transaksi, barang, pengguna, audit_logs, kasbon, stock_opname, backup_logs, pelanggan, pinjaman, aset, pengeluaran, karyawan, system_configs, dll).
  - [ ] Nama kolom, tipe data `DECIMAL(15,4)`, constraint CHECK, foreign key, dan default values yang relevan untuk expected result.

- [ ] **Tugas 1.9:** Baca file **ERD Database v1.1** (`docs/sdlc/03_design/02_erd_database.md`). Catat:
  - [ ] Relasi antar-tabel yang relevan untuk test case integrasi dan verifikasi cascade/restrict.

- [ ] **Tugas 1.10:** Baca file referensi TERSIER sesuai kebutuhan (System Architecture, Coding Standard, Module Structure, Data Dictionary, Workflow Diagram, Environment Setup, BRD) untuk melengkapi detail konteks yang diperlukan.

---

### 5.2. Fase 2 — Penyusunan Rangkuman Data Referensi

> **Tujuan:** Merangkum seluruh data dan informasi yang dibutuhkan spesifik oleh dokumen Test Cases dari file referensi.

- [ ] **Tugas 2.1:** Buat rangkuman 44 skenario uji dari Test Plan Bab 4, lengkap dengan:
  - ID skenario, deskripsi, SRS terkait, UC terkait, tipe test, dan prioritas.

- [ ] **Tugas 2.2:** Buat rangkuman detail skenario pengujian dari Test Plan Bab 5-9 (Keamanan, Presisi Desimal, Integrasi, CLI, Non-Fungsional), lengkap dengan:
  - Tujuan pengujian, skenario detail, nilai data uji numerik spesifik, dan expected behavior.

- [ ] **Tugas 2.3:** Buat rangkuman spesifikasi teknis dari SRS v1.1 untuk setiap SRS-F, meliputi:
  - Input yang diperlukan (nama field, tipe data, batasan), proses logika bisnis (formula kalkulasi), output yang dihasilkan, aturan validasi, dan kode error penanganan pengecualian.

- [ ] **Tugas 2.4:** Buat rangkuman alur interaksi dari Use Case v1.1 untuk setiap UC, meliputi:
  - Prakondisi, alur utama (langkah bernomor), alur alternatif, alur pengecualian (kode error + pesan), dan pasca-kondisi.

- [ ] **Tugas 2.5:** Buat rangkuman mapping kode error dari Test Plan Bab 12.4, meliputi:
  - 15 kode error + string pesan kesalahan + skenario validasi yang relevan.

- [ ] **Tugas 2.6:** Buat rangkuman data lingkungan pengujian dari Test Plan Bab 10, meliputi:
  - Hardware, software, database test `abucom_test_db`, data fixtures, dan konfigurasi `.env.test`.

- [ ] **Tugas 2.7:** Buat rangkuman matriks otorisasi dari ACM v1.1 untuk keperluan penulisan test case RBAC positif dan negatif.

- [ ] **Tugas 2.8:** Pastikan hanya mengambil data dan informasi yang secara spesifik dibutuhkan oleh dokumen Test Cases ini. **JANGAN** memasukkan data yang bukan ranah test case (seperti jadwal proyek, anggaran, atau deskripsi business case).

---

### 5.3. Fase 3 — Penulisan Dokumen Test Cases

> **Tujuan:** Menulis dokumen Test Cases lengkap sesuai kerangka struktur di Bab 4 issue ini.

#### Tahap 3A — Front Matter dan Informasi Dokumen (Bab 1)

- [ ] **Tugas 3A.1:** Tulis front matter YAML (dokumen, proyek, versi 1.0, tanggal, status, penyusun = `Senior QA Engineer & Test Case Design Specialist`).
- [ ] **Tugas 3A.2:** Tulis tabel Riwayat Perubahan Dokumen (versi 1.0 awal).
- [ ] **Tugas 3A.3:** Tulis Bab 1.1 Tujuan Dokumen — Jelaskan bahwa dokumen ini mendefinisikan kasus uji terperinci yang diturunkan dari Test Plan v1.1 untuk dieksekusi oleh QA dan AI Testing Agent.
- [ ] **Tugas 3A.4:** Tulis Bab 1.2 Cakupan Dokumen — Jelaskan total test case yang tercakup, jumlah modul, dan tipe pengujian.
- [ ] **Tugas 3A.5:** Tulis Bab 1.3 Posisi Dokumen dalam Siklus SDLC — Buat diagram posisi (setelah Test Plan, sebelum Test Scripts).
- [ ] **Tugas 3A.6:** Tulis Bab 1.4 Hubungan dengan Dokumen SDLC Lainnya — Sebutkan dokumen input (Test Plan, SRS, UC, ACM, Security Design, BOM Design, CLI Flow, DB Schema, ERD) dan dokumen output (Test Scripts, Test Report).
- [ ] **Tugas 3A.7:** Tulis Bab 1.5 Audiens Target (Junior Programmer, AI Testing Agent, Kepala Percetakan).
- [ ] **Tugas 3A.8:** Tulis Bab 1.6 Definisi, Akronim, dan Singkatan — Salin dan sesuaikan dari Test Plan Bab 1.6 + tambahkan istilah spesifik test case.
- [ ] **Tugas 3A.9:** Tulis Bab 1.7 Konvensi Penulisan Test Case — Jelaskan format tabel, konvensi penamaan ID, status uji (PASS/FAIL/BLOCKED/SKIPPED), dan cara membaca dokumen ini.

#### Tahap 3B — Ringkasan Cakupan (Bab 2) dan Lingkungan (Bab 3)

- [ ] **Tugas 3B.1:** Tulis Bab 2.1 Total Test Case per Modul — Buat tabel ringkasan kuantitatif (Modul, Jumlah Skenario, Jumlah Test Case Positif, Negatif, Boundary, Total).
- [ ] **Tugas 3B.2:** Tulis Bab 2.2 Distribusi Test Case per Tipe Pengujian (Functional, Security, Precision, Boundary, Database, CLI, Integration, Integrity).
- [ ] **Tugas 3B.3:** Tulis Bab 2.3 Distribusi Test Case per Prioritas (High, Medium, Low).
- [ ] **Tugas 3B.4:** Tulis Bab 2.4 Distribusi Test Case per Tingkat Pengujian (Unit, Integration, System, UAT).
- [ ] **Tugas 3B.5:** Tulis Bab 3.1 Spesifikasi Lingkungan — Rangkum dari Test Plan Bab 10 (hardware, software, library).
- [ ] **Tugas 3B.6:** Tulis Bab 3.2 Prakondisi Global — Definisikan prakondisi yang berlaku untuk SEMUA test case (misalnya: database `abucom_test_db` sudah ter-setup, `.env.test` terkonfigurasi, 8 akun staf ter-seed, dll).
- [ ] **Tugas 3B.7:** Tulis Bab 3.3 Data Uji Global (Test Fixtures) — Daftar data seed yang representatif (8 akun pengguna, contoh barang retail, bahan baku desimal, supplier, parameter system_configs).

#### Tahap 3C — Penulisan Test Case per Modul Fungsional (Bab 4-13)

> **Instruksi penting:** Untuk setiap skenario uji di Test Plan Bab 4, buat minimal 2-3 test case (positif, negatif, dan boundary jika relevan). Gunakan format tabel test case yang sudah didefinisikan di Bab 4 issue ini.

- [ ] **Tugas 3C.1:** Tulis Bab 4 — Test Cases Modul M.1 (Transaksi & Harga):
  - [ ] Ekspansi skenario M1-TC-001 (Transaksi multi-divisi) → minimal 2 test case (positif: transaksi sukses kas; negatif: koneksi DB putus ERR-DB-001).
  - [ ] Ekspansi skenario M1-TC-002 (Harga dinamis) → minimal 3 test case (positif Retail; positif Grosir threshold; negatif harga NULL ERR-VAL-002).
  - [ ] Ekspansi skenario M1-TC-003 (DP & Pelunasan) → minimal 3 test case (positif DP parsial + pelunasan; positif DP 100%; negatif pelunasan kurang ERR-VAL-003).
  - [ ] Ekspansi skenario M1-TC-004 (Pembatalan DP) → minimal 2 test case (positif pembatalan sukses + sandi pemilik; negatif sandi salah).
  - [ ] Ekspansi skenario M1-TC-005 (Retur ATK) → minimal 2 test case (positif retur stok kembali; negatif kas kurang ERR-CASH-004).
  - [ ] Ekspansi skenario M1-TC-006 (Margin produk) → minimal 2 test case (positif margin kalkulasi akurat; boundary harga jual = 0).
  - [ ] Ekspansi skenario M1-TC-007 (Struk thermal) → minimal 2 test case (positif 58mm wrapping; positif 80mm wrapping).

- [ ] **Tugas 3C.2:** Tulis Bab 5 — Test Cases Modul M.2 (Inventaris, BOM & Opname):
  - [ ] Ekspansi skenario M2-TC-001 s.d M2-TC-010 → masing-masing minimal 2-3 test case.
  - [ ] Perhatikan khusus: M2-TC-002 (HPP BOM desimal) harus mencantumkan angka kalkulasi presisi `Decimal('4750.0000')` dari Test Plan Bab 6.1.
  - [ ] Perhatikan khusus: M2-TC-005 (Stock Opname) harus mencakup test case positif approval supervisor dan negatif peran non-supervisor ERR-AUTH-011.
  - [ ] Perhatikan khusus: M2-TC-010 (Backup/Restore) harus mencakup positif backup sukses, positif restore sukses, dan negatif berkas korup ERR-FILE-039.

- [ ] **Tugas 3C.3:** Tulis Bab 6 — Test Cases Modul M.3 (PPOB & Jasa Service):
  - [ ] Ekspansi skenario M3-TC-001 s.d M3-TC-003 → masing-masing minimal 2 test case.

- [ ] **Tugas 3C.4:** Tulis Bab 7 — Test Cases Modul M.4 (SDM & Payroll):
  - [ ] Ekspansi skenario M4-TC-001 s.d M4-TC-005 → masing-masing minimal 2-3 test case.
  - [ ] Perhatikan khusus: M4-TC-002 (Smart Payroll) harus dibuat test case terpisah untuk Skenario A (laba ≥ Rp 15 juta) dan Skenario B (laba < Rp 15 juta) dengan angka kalkulasi spesifik dari Test Plan Bab 6.5.
  - [ ] Perhatikan khusus: M4-TC-003 (Proteksi minimum UMR) harus mencantumkan angka Rp 1.600.000 dan kalkulasi proteksi dari Test Plan Bab 6.5.

- [ ] **Tugas 3C.5:** Tulis Bab 8 — Test Cases Modul M.5 (Antrian & Desain):
  - [ ] Ekspansi skenario M5-TC-001 s.d M5-TC-003 → masing-masing minimal 2 test case.

- [ ] **Tugas 3C.6:** Tulis Bab 9 — Test Cases Modul M.6 (Pinjaman, Aset & Pengeluaran):
  - [ ] Ekspansi skenario M6-TC-001 s.d M6-TC-005 → masing-masing minimal 2 test case.
  - [ ] Perhatikan khusus: M6-TC-005 (Pengeluaran eskalasi) harus mencakup test case positif di bawah Rp 500.000 dan negatif di atas Rp 500.000 dengan sandi salah ERR-AUTH-029.

- [ ] **Tugas 3C.7:** Tulis Bab 10 — Test Cases Modul M.7 (Keamanan & Audit):
  - [ ] Ekspansi skenario M7-TC-001 s.d M7-TC-007 → masing-masing minimal 2-3 test case.
  - [ ] Perhatikan khusus: M7-TC-001 (Login bcrypt/JWT) harus test case positif login sukses, negatif login gagal ERR-AUTH-001, dan boundary kedaluwarsa JWT 8 jam ERR-SESSION-002.
  - [ ] Perhatikan khusus: M7-TC-002 (RBAC) harus memuat test case untuk setiap skenario peran ilegal (desainer akses payroll, pramuniaga akses stock opname approve, dll) dari Test Plan Bab 5.2.

- [ ] **Tugas 3C.8:** Tulis Bab 11 — Test Cases Modul M.8 (CRM & PDP):
  - [ ] Ekspansi skenario M8-TC-001 s.d M8-TC-002 → masing-masing minimal 2 test case.
  - [ ] Perhatikan khusus: M8-TC-001 (CRM Fernet) harus verifikasi string database teracak biner.
  - [ ] Perhatikan khusus: M8-TC-002 (UU PDP) harus verifikasi hard delete bukan soft delete.

- [ ] **Tugas 3C.9:** Tulis Bab 12 — Test Cases Modul M.9 (Multi-Cabang):
  - [ ] Ekspansi skenario M9-TC-001 → minimal 2 test case (positif isolasi data benar; negatif tanpa cabang_id).

- [ ] **Tugas 3C.10:** Tulis Bab 13 — Test Cases Modul M.10 (Runtime Config):
  - [ ] Ekspansi skenario M10-TC-001 → minimal 2 test case (positif load parameter; positif modifikasi parameter).

#### Tahap 3D — Penulisan Test Case Khusus (Bab 14-18)

- [ ] **Tugas 3D.1:** Tulis Bab 14 — Test Cases Pengujian Keamanan:
  - [ ] Konversi setiap skenario dari Test Plan Bab 5.1-5.8 menjadi test case detail (TC-SEC-001 s.d TC-SEC-008).
  - [ ] Pastikan setiap test case keamanan memuat data uji konkret (misal: string injeksi `' OR '1'='1'`, string ANSI escape `\x1b[31mBarang Palsu`, dll).

- [ ] **Tugas 3D.2:** Tulis Bab 15 — Test Cases Pengujian Presisi Desimal:
  - [ ] Konversi setiap skenario dari Test Plan Bab 6.1-6.5 menjadi test case detail (TC-DEC-001 s.d TC-DEC-005).
  - [ ] Pastikan setiap test case presisi desimal memuat angka kalkulasi spesifik (misal: `Decimal('0.0025')`, `Decimal('4750.0000')`, `Decimal('100.00005')` → `Decimal('100.0001')`, dll).

- [ ] **Tugas 3D.3:** Tulis Bab 16 — Test Cases Pengujian Integrasi & Konektivitas:
  - [ ] Konversi setiap skenario dari Test Plan Bab 7.1-7.5 menjadi test case detail (TC-INT-001 s.d TC-INT-005).
  - [ ] Pastikan test case ACID memuat simulasi crash dan verifikasi rollback.

- [ ] **Tugas 3D.4:** Tulis Bab 17 — Test Cases Pengujian Antarmuka CLI:
  - [ ] Konversi setiap skenario dari Test Plan Bab 8.1-8.5 menjadi test case detail (TC-CLI-001 s.d TC-CLI-005).
  - [ ] Pastikan test case struk thermal memuat contoh nama barang panjang dari Test Plan Bab 8.3.

- [ ] **Tugas 3D.5:** Tulis Bab 18 — Test Cases Pengujian Non-Fungsional:
  - [ ] Konversi setiap skenario dari Test Plan Bab 9.1-9.5 menjadi test case detail (TC-NF-001 s.d TC-NF-005).
  - [ ] Pastikan test case performa memuat batas waktu terukur (`< 2 detik`, `< 5 detik`).

#### Tahap 3E — Penulisan Matriks Ketertelusuran dan Lampiran (Bab 19-21)

- [ ] **Tugas 3E.1:** Tulis Bab 19.1 — Tabel mapping Test Case → Skenario Test Plan.
- [ ] **Tugas 3E.2:** Tulis Bab 19.2 — Tabel mapping Test Case → SRS Fungsional.
- [ ] **Tugas 3E.3:** Tulis Bab 19.3 — Tabel mapping Test Case → Use Case.
- [ ] **Tugas 3E.4:** Tulis Bab 19.4 — Tabel mapping Test Case → Kode Error.
- [ ] **Tugas 3E.5:** Tulis Bab 19.5 — Ringkasan statistik cakupan:
  - Total skenario: 44 (dari Test Plan)
  - Total test case: [hitung total aktual]
  - Cakupan SRS-F: 100%
  - Cakupan UC: 100%
  - Cakupan kode error: 100%
- [ ] **Tugas 3E.6:** Tulis Bab 20 — Lampiran:
  - [ ] 20.1 Glosarium — Salin dan perluas dari Test Plan Bab 14.1.
  - [ ] 20.2 Contoh Data Seed — Buat tabel representatif data fixtures.
  - [ ] 20.3 Template Defect Report — Referensi silang ke Test Plan Bab 11.4.
- [ ] **Tugas 3E.7:** Tulis Bab 21 — Referensi Dokumen:
  - Buat tabel daftar lengkap file referensi yang digunakan dalam penyusunan (sesuai Bab 3 issue ini).

---

### 5.4. Fase 4 — Penulisan ke Target File

> **Tujuan:** Menuangkan seluruh hasil penulisan ke target file yang sudah ditentukan.

- [ ] **Tugas 4.1:** Tulis seluruh konten dokumen Test Cases ke file target: `docs/sdlc/05_testing/02_test_cases.md`.
- [ ] **Tugas 4.2:** Pastikan file ditulis secara **overwrite penuh** (bukan append), sehingga isi file menjadi utuh dan lengkap dari awal hingga akhir.
- [ ] **Tugas 4.3:** Pastikan encoding file menggunakan **UTF-8 tanpa BOM**.

---

### 5.5. Fase 5 — Verifikasi dan Validasi Akhir

> **Tujuan:** Memastikan kualitas dokumen sebelum dianggap selesai.

- [ ] **Tugas 5.1:** Verifikasi **kelengkapan cakupan**: Pastikan semua 44 skenario uji dari Test Plan Bab 4 sudah di-ekspansi menjadi test case detail.
- [ ] **Tugas 5.2:** Verifikasi **ketertelusuran**: Pastikan setiap test case memiliki referensi balik ke skenario Test Plan, SRS, dan Use Case yang valid.
- [ ] **Tugas 5.3:** Verifikasi **konsistensi data numerik**: Pastikan angka-angka kalkulasi (HPP BOM, Smart Payroll, depresiasi, threshold kas, dll) konsisten persis dengan yang tercantum di Test Plan dan SRS.
- [ ] **Tugas 5.4:** Verifikasi **konsistensi kode error**: Pastikan string pesan error di expected result test case **identik persis** dengan kode error yang tercantum di Test Plan Bab 12.4 dan SRS.
- [ ] **Tugas 5.5:** Verifikasi **format dan struktur**: Pastikan semua tabel test case mengikuti format yang sudah didefinisikan. Pastikan heading berjenjang rapi (##, ###, ####).
- [ ] **Tugas 5.6:** Verifikasi **bahasa Indonesia**: Pastikan seluruh dokumen ditulis dalam bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami.
- [ ] **Tugas 5.7:** Verifikasi **data kosong**: Jika ada data yang tidak tersedia atau tidak ditemukan di file referensi, tandai dengan format: `[DATA BELUM TERSEDIA — Perlu diisi manual: <deskripsi data yang dibutuhkan>]`.
- [ ] **Tugas 5.8:** Verifikasi **referensi dokumen di baris akhir**: Pastikan Bab 21 (Referensi Dokumen) telah terisi lengkap dan benar sesuai file referensi aktual yang dibaca.
- [ ] **Tugas 5.9:** Verifikasi **kualitas kelayakan sebagai input fase selanjutnya**: Pastikan dokumen ini cukup detail dan lengkap untuk dijadikan referensi utama dalam pembuatan Test Scripts (skrip pytest otomatis) dan Test Report pada fase testing selanjutnya, tanpa perlu kembali mempertanyakan kelengkapannya.
- [ ] **Tugas 5.10:** Hitung dan tulis total test case aktual yang dihasilkan di Bab 2.1 dan Bab 19.5.

---

## 6. Instruksi Tambahan Spesifik Dokumen Test Cases

Berikut adalah instruksi tambahan yang merupakan kaidah standar pembuatan dokumen Test Cases yang **wajib dipatuhi**:

### 6.1. Kaidah Penulisan Data Uji (Test Data)

- [ ] Setiap test case **wajib** mencantumkan data uji **konkret dan spesifik**, bukan placeholder abstrak. Contoh:
  - ✅ BENAR: `barang_id = 101, kuantitas = Decimal('5.0000'), metode_pembayaran = 'Kas'`
  - ❌ SALAH: `masukkan barang_id yang valid`

### 6.2. Kaidah Penulisan Expected Result

- [ ] Expected result **wajib** bersifat **terukur dan dapat diverifikasi** secara objektif. Contoh:
  - ✅ BENAR: `Kolom status_pembayaran di tabel transaksi berubah menjadi 'LUNAS'`
  - ❌ SALAH: `Transaksi berhasil diproses`
- [ ] Expected result yang melibatkan database **wajib** menyebutkan nama tabel dan nama kolom yang diverifikasi.
- [ ] Expected result yang melibatkan CLI **wajib** menyebutkan string pesan error/sukses yang harus muncul di layar.

### 6.3. Kaidah Penulisan Langkah Uji (Test Steps)

- [ ] Setiap langkah uji **wajib** ditulis sebagai perintah aksi yang deterministik dan berurutan. Contoh:
  - ✅ BENAR: `1. Login sebagai kasir (username: kasir01, password: K@sir2026!)`
  - ❌ SALAH: `Login ke sistem`
- [ ] Setiap langkah uji **wajib** menyebutkan peran aktor yang menjalankan aksi tersebut.

### 6.4. Kaidah Penulisan Prakondisi

- [ ] Prakondisi **wajib** menyebutkan state awal database, sesi login aktif, dan data yang harus sudah tersedia sebelum eksekusi.

### 6.5. Kaidah Presisi Desimal

- [ ] Setiap angka desimal dalam data uji dan expected result **wajib** ditulis dalam notasi `Decimal('X.XXXX')` untuk menunjukkan presisi 4 digit.
- [ ] Setiap formula kalkulasi dalam expected result **wajib** menunjukkan langkah perhitungan dan hasil akhir.

### 6.6. Kaidah Test Case Negatif dan Boundary

- [ ] Setiap test case negatif **wajib** memverifikasi kode error spesifik (contoh: `ERR-AUTH-001`, `ERR-DB-001`), string pesan error, dan bahwa data database **TIDAK** berubah (rollback sukses).
- [ ] Setiap test case boundary **wajib** menguji nilai minimum, maksimum, dan tepat di ambang batas (*threshold*).

### 6.7. Kaidah Independensi Test Case

- [ ] Setiap test case **harus** dapat dieksekusi secara independen tanpa bergantung pada hasil test case lain, kecuali jika dependensi di-deklarasikan secara eksplisit di kolom `Catatan Tambahan`.

### 6.8. Kaidah Cross-Reference

- [ ] Setiap test case yang memiliki dependensi lintas modul **wajib** mencantumkan ID test case terkait di kolom `Catatan Tambahan`.

---

## 7. Penandaan Data Kosong

Jika pada saat pembacaan file referensi ditemukan data yang kosong, tidak tersedia, atau ambigu, **wajib** ditandai dengan format berikut di dalam dokumen Test Cases:

```markdown
[DATA BELUM TERSEDIA — Perlu diisi manual: <deskripsi jelas data yang dibutuhkan>]
```

Contoh:
- `[DATA BELUM TERSEDIA — Perlu diisi manual: nilai seed data akun gudang (username dan password)]`
- `[DATA BELUM TERSEDIA — Perlu diisi manual: URL path arsip file desain default di PC klien]`

---

## 8. Checklist Ringkasan Eksekusi Issue

Berikut adalah checklist ringkasan keseluruhan untuk memastikan issue ini terimplementasi secara lengkap:

### Fase 1 — Pembacaan File Referensi
- [ ] Baca Test Plan v1.1 (seluruh 15 bab)
- [ ] Baca SRS v1.1 (seluruh SRS-F-001 s.d SRS-F-040+ dan SRS-NF-001 s.d SRS-NF-011)
- [ ] Baca Use Case Diagram v1.1 (seluruh UC-001 s.d UC-044)
- [ ] Baca Access Control Matrix v1.1
- [ ] Baca Security Design v1.1
- [ ] Baca BOM & HPP Design v1.1
- [ ] Baca CLI Interaction Flow v1.1
- [ ] Baca Database Schema v1.1
- [ ] Baca ERD Database v1.1
- [ ] Baca file referensi tersier sesuai kebutuhan

### Fase 2 — Rangkuman Data
- [ ] Rangkum 44 skenario uji dari Test Plan
- [ ] Rangkum detail skenario pengujian khusus (keamanan, desimal, integrasi, CLI, non-fungsional)
- [ ] Rangkum spesifikasi teknis SRS per SRS-F
- [ ] Rangkum alur interaksi UC per UC
- [ ] Rangkum mapping kode error
- [ ] Rangkum data lingkungan pengujian
- [ ] Rangkum matriks otorisasi ACM

### Fase 3 — Penulisan Dokumen
- [ ] Tulis Front Matter + Bab 1 (Informasi Dokumen)
- [ ] Tulis Bab 2 (Ringkasan Cakupan) + Bab 3 (Lingkungan & Prakondisi)
- [ ] Tulis Bab 4-13 (Test Cases per Modul M.1 s.d M.10)
- [ ] Tulis Bab 14 (Test Cases Keamanan)
- [ ] Tulis Bab 15 (Test Cases Presisi Desimal)
- [ ] Tulis Bab 16 (Test Cases Integrasi)
- [ ] Tulis Bab 17 (Test Cases CLI)
- [ ] Tulis Bab 18 (Test Cases Non-Fungsional)
- [ ] Tulis Bab 19 (Matriks Ketertelusuran)
- [ ] Tulis Bab 20 (Lampiran) + Bab 21 (Referensi)

### Fase 4 — Penulisan ke Target File
- [ ] Tulis ke `docs/sdlc/05_testing/02_test_cases.md` (overwrite penuh)
- [ ] Pastikan encoding UTF-8 tanpa BOM

### Fase 5 — Verifikasi Akhir
- [ ] Verifikasi kelengkapan cakupan 44 skenario
- [ ] Verifikasi ketertelusuran (test case → skenario → SRS → UC)
- [ ] Verifikasi konsistensi data numerik
- [ ] Verifikasi konsistensi kode error
- [ ] Verifikasi format dan struktur tabel
- [ ] Verifikasi bahasa Indonesia natural
- [ ] Verifikasi penandaan data kosong
- [ ] Verifikasi referensi dokumen di baris akhir
- [ ] Verifikasi kualitas kelayakan sebagai input fase selanjutnya
- [ ] Hitung dan tulis total test case aktual

---

## 9. Referensi Dokumen yang Digunakan dalam Penyusunan Issue Ini

| No | Nama Dokumen | Path File | Kegunaan dalam Issue |
|----|--------------|-----------|----------------------|
| 1 | Test Plan v1.1 | `docs/sdlc/05_testing/01_test_plan.md` | Sumber utama definisi skenario, template, matriks, strategi, dan lingkungan pengujian |
| 2 | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | Sumber spesifikasi fungsional dan non-fungsional |
| 3 | Use Case Diagram v1.1 | `docs/sdlc/02_analysis/03_use_case_diagram.md` | Sumber alur interaksi dan skenario naratif use case |
| 4 | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Matriks otorisasi RBAC 8 peran |
| 5 | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | Spesifikasi keamanan (bcrypt, JWT, rate limiting, enkripsi) |
| 6 | BOM & HPP Design v1.1 | `docs/sdlc/03_design/05_bom_hpp_design.md` | Spesifikasi kalkulasi presisi desimal |
| 7 | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur navigasi terminal dan visual rendering |
| 8 | Database Schema v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | Definisi DDL tabel dan constraint database |
| 9 | ERD Database v1.1 | `docs/sdlc/03_design/02_erd_database.md` | Diagram relasi antar-entitas |
| 10 | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` | Arsitektur client-server LAN |
| 11 | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` | Standar FP pure functions |
| 12 | Module Structure v1.1 | `docs/sdlc/04_implementation/03_module_structure.md` | Susunan folder dan modul Python |
| 13 | Data Dictionary v1.1 | `docs/sdlc/02_analysis/05_data_dictionary.md` | Definisi atribut data |
| 14 | Workflow Diagram v1.1 | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Alur kerja bisnis antar-modul |
| 15 | Environment Setup v1.1 | `docs/sdlc/04_implementation/02_environment_setup.md` | Konfigurasi lingkungan |
| 16 | Business Requirements Document v1.1 | `docs/sdlc/02_analysis/01_business_requirements.md` | Kebutuhan bisnis dasar |
