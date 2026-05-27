# Pembuatan dan Penyusunan Dokumen Bug Report Template

---

## 1. Informasi Issue

| Atribut | Keterangan |
|---|---|
| **Judul** | Pembuatan dan Penyusunan Dokumen Bug Report Template |
| **Dokumen Utama** | Bug Report Template |
| **Target File** | `docs/sdlc/05_testing/04_bug_report_template.md` |
| **Prioritas** | High |
| **Status** | Open |
| **Tanggal Dibuat** | 2026-05-27 |
| **Fase SDLC** | Fase 05 — Testing |
| **Estimasi Kompleksitas** | Medium |

---

## 2. Persona Pelaksana

| Atribut Persona | Detail |
|---|---|
| **Nama Persona** | **Senior QA Engineer & Defect Management Specialist** |
| **Otoritas** | Bertanggung jawab penuh atas standardisasi proses pelaporan cacat (defect reporting), klasifikasi tingkat keparahan bug, alur eskalasi perbaikan, dan memastikan setiap temuan bug terdokumentasi secara akurat, lengkap, dan dapat direproduksi oleh programmer yang ditugaskan memperbaikinya. |
| **Justifikasi Pemilihan** | Dokumen Bug Report Template adalah dokumen operasional pengujian yang berfungsi sebagai formulir standar pencatatan temuan cacat selama fase testing (unit test, integration test, system test, dan UAT). Persona Senior QA Engineer dipilih karena memiliki kompetensi langsung dalam mendefinisikan standar kualitas pelaporan bug yang terstruktur, memiliki pemahaman mendalam tentang severity & priority classification, serta memahami kebutuhan informasi yang dibutuhkan developer untuk mereproduksi dan memperbaiki bug secara efisien. |

---

## 3. File Referensi yang Dipilih

Berikut adalah daftar file referensi yang **wajib dibaca seluruhnya tanpa ada yang terlewat** sebelum memulai penyusunan dokumen utama. File-file ini dipilih berdasarkan relevansi langsung terhadap kebutuhan informasi dalam Bug Report Template.

### 3.1. Referensi Primer (Wajib Dibaca Tuntas)

| No | Kode Ref | Nama Dokumen | Path File | Justifikasi Pemilihan |
|----|----------|--------------|-----------|---|
| 1 | **R-TP** | Test Plan v1.1 | `docs/sdlc/05_testing/01_test_plan.md` | Sumber utama 44 skenario uji, kode error mapping (15 kode `ERR-XXX-YYY`), strategi pengujian, pemetaan modul M.1 s.d M.10, kriteria masuk/keluar pengujian, template Test Report, dan lingkungan pengujian. Bug report harus selaras dengan seluruh terminologi dan ID skenario yang didefinisikan di sini. |
| 2 | **R-TC** | Test Cases v1.1 | `docs/sdlc/05_testing/02_test_cases.md` | Sumber 70 kasus uji operasional terperinci (happy path, unhappy path, boundary), data uji global (test fixtures), template Defect Report yang sudah ada di Lampiran 20.3, dan konvensi penamaan TC-[MODUL]-[SKENARIO]-[URUT]. Bug report harus merujuk ID test case secara tepat. |
| 3 | **R-UAT** | UAT Script v1.1 | `docs/sdlc/05_testing/03_uat_script.md` | Sumber 44 skrip UAT + 1 E2E + 3 NF, prosedur defect handling (Bab 16), template pencatatan temuan UAT-BUG, klasifikasi keparahan (Blocker/Critical/Major/Minor/Cosmetic), dan alur eskalasi perbaikan. Bug report harus kompatibel dan sinkron dengan prosedur ini. |
| 4 | **R-SRS** | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | Sumber spesifikasi kebutuhan fungsional (SRS-F-001 s.d SRS-F-040) dan non-fungsional (SRS-NF-001 s.d SRS-NF-011). Setiap bug yang dilaporkan harus bisa di-trace balik ke spesifikasi SRS yang dilanggar. |
| 5 | **R-SEC** | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | Sumber spesifikasi keamanan (bcrypt, JWT, RBAC, audit log, rate limiting, UU PDP, enkripsi Fernet/AES-256). Bug keamanan memiliki klasifikasi khusus dan memerlukan informasi konteks keamanan yang spesifik dalam laporan bug. |

### 3.2. Referensi Sekunder (Dibaca untuk Konteks Pelengkap)

| No | Kode Ref | Nama Dokumen | Path File | Justifikasi Pemilihan |
|----|----------|--------------|-----------|---|
| 6 | **R-CLI** | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Sumber format visual kode error CLI (`ERR-XXX-YYY`), rendering ANSI, breadcrumb navigasi. Laporan bug pada antarmuka CLI memerlukan konteks interaksi layar terminal. |
| 7 | **R-ACM** | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Sumber definisi 8 peran internal dan matriks otorisasi. Laporan bug terkait hak akses memerlukan identifikasi peran aktor yang terdampak. |
| 8 | **R-DB** | Database Schema v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | Sumber struktur tabel database untuk konteks bug terkait integritas data. |
| 9 | **R-BOM** | BOM & HPP Design v1.1 | `docs/sdlc/03_design/05_bom_hpp_design.md` | Sumber spesifikasi presisi desimal `Decimal(15,4)` dan `ROUND_HALF_UP`. Bug presisi keuangan memerlukan data kalkulasi yang presisi dalam laporan. |
| 10 | **R-NAR** | Narasi Proyek | `docs/sdlc/narasi.txt` | Sumber konteks bisnis umum, struktur organisasi 7 jabatan, dan lingkungan operasional toko. Digunakan sebagai konteks latar belakang pengguna akhir dan ekosistem kerja toko yang mempengaruhi skenario bug. |

### 3.3. Justifikasi Pemilihan narasi.txt

File `narasi.txt` **masih dibutuhkan** sebagai referensi konteks bisnis karena:
- Menyediakan gambaran 7 jabatan operasional toko yang menjadi aktor potensial pelapor bug.
- Menyediakan konteks jenis layanan usaha (percetakan, ATK, PPOB, jasa keuangan, service) yang menentukan kategori modul terdampak dalam laporan bug.
- Menyediakan konteks lingkungan kerja (CLI, LAN offline, multi-OS) yang relevan dengan informasi lingkungan reproduksi bug.

---

## 4. Kerangka Struktur Dokumen Utama

Berikut adalah kerangka lengkap dokumen **Bug Report Template** yang harus disusun. Kerangka ini mengadopsi standar praktik industri **IEEE 1044 (Standard Classification for Software Anomalies)** dan **ISTQB Foundation Level — Defect Management** yang disesuaikan dengan konteks proyek AbuCom.

```
---
(YAML Front Matter: dokumen, proyek, versi, tanggal, status, penyusun)
---

# Bug Report Template — AbuCom

## Riwayat Perubahan Dokumen
(Tabel versi, tanggal, deskripsi perubahan, oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya (Input/Output)
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan
### 1.7. Konvensi Penamaan ID Bug

---

## 2. Klasifikasi Tingkat Keparahan Bug (Severity Classification)
### 2.1. Definisi Tingkat Keparahan
### 2.2. Tabel Klasifikasi Severity
### 2.3. Contoh Konkret Severity per Level (Konteks AbuCom)

---

## 3. Klasifikasi Prioritas Perbaikan (Priority Classification)
### 3.1. Definisi Tingkat Prioritas
### 3.2. Tabel Klasifikasi Priority
### 3.3. Matriks Severity vs Priority

---

## 4. Siklus Hidup Bug (Bug Lifecycle)
### 4.1. Diagram Status Bug (State Transition Diagram)
### 4.2. Deskripsi Setiap Status
### 4.3. Aturan Transisi Antar Status

---

## 5. Kategori Bug (Bug Category/Type)
### 5.1. Tabel Kategori Bug
### 5.2. Pemetaan Kategori Bug ke Modul AbuCom (M.1 s.d M.10)

---

## 6. Template Formulir Laporan Bug (Bug Report Form)
### 6.1. Template Formulir Utama (Tabel Format)
### 6.2. Panduan Pengisian Setiap Field
### 6.3. Contoh Pengisian Bug Report — Bug Fungsional (Happy Path Failure)
### 6.4. Contoh Pengisian Bug Report — Bug Keamanan (Security Vulnerability)
### 6.5. Contoh Pengisian Bug Report — Bug Presisi Desimal (Calculation Error)
### 6.6. Contoh Pengisian Bug Report — Bug Antarmuka CLI (Visual/Rendering Error)

---

## 7. Prosedur Pelaporan dan Eskalasi Bug
### 7.1. Alur Pelaporan Bug (Flowchart)
### 7.2. Peran dan Tanggung Jawab dalam Manajemen Bug
### 7.3. SLA Penanganan Bug per Severity Level
### 7.4. Prosedur Eskalasi Khusus Bug Keamanan

---

## 8. Integrasi dengan Proses Pengujian
### 8.1. Hubungan Bug Report dengan Test Case
### 8.2. Hubungan Bug Report dengan UAT Script
### 8.3. Ketertelusuran Bug → Test Case → SRS → Use Case

---

## 9. Metrik dan Pelaporan Agregat Bug
### 9.1. Template Ringkasan Statistik Bug (Bug Summary Dashboard)
### 9.2. Metrik Kualitas yang Dilacak

---

## 10. Lampiran
### 10.1. Glosarium Istilah Manajemen Bug
### 10.2. Daftar Kode Error Sistem AbuCom (Error Code Registry)
### 10.3. Template Bug Report Kosong (Siap Cetak/Salin)
### 10.4. Checklist Kelengkapan Bug Report

---

## 11. Referensi Dokumen
(Tabel referensi file yang digunakan dalam penyusunan dokumen ini)
```

---

## 5. Instruksi Implementasi Detail (Low-Level Checklist)

> **PENTING:** Instruksi di bawah ini disusun untuk dieksekusi oleh junior programmer atau LLM model AI yang lebih kecil/murah. Ikuti setiap langkah secara berurutan. Jangan melewatkan satupun langkah. Jangan mengarang data yang tidak ada di file referensi.

---

### Tahap 1: Pembacaan dan Perangkuman File Referensi

Baca seluruh file referensi secara tuntas, satu per satu. Rangkum semua data dan informasi yang relevan untuk Bug Report Template. Pastikan setiap detail yang berkaitan dengan pelaporan bug, klasifikasi keparahan, kode error, prosedur defect handling, dan informasi lingkungan pengujian tidak ada yang terlewat.

- [ ] **1.1.** Baca file `docs/sdlc/05_testing/01_test_plan.md` secara lengkap dari awal hingga akhir. Rangkum data berikut:
  - [ ] Daftar 44 skenario uji beserta ID skenario (`M1-TC-001` s.d `M10-TC-001`).
  - [ ] Daftar 15 kode error sistem (`ERR-AUTH-001`, `ERR-AUTH-002`, `ERR-AUTH-003`, `ERR-AUTH-011`, `ERR-AUTH-029`, `ERR-SESSION-001`, `ERR-SESSION-002`, `ERR-DB-001`, `ERR-DB-002`, `ERR-FILE-001`, `ERR-FILE-039`, `ERR-CASH-001`, `ERR-CASH-004`, `ERR-STOCK-010`, `ERR-VAL-007`) beserta pesan error dan skenario validasinya (Bab 12.4).
  - [ ] Daftar 10 modul fungsional utama (M.1 s.d M.10) beserta nama dan cakupannya (Bab 4).
  - [ ] Strategi pengujian: 4 tingkat pengujian (Unit, Integration, System, UAT) dan 7 tipe pengujian (Bab 3).
  - [ ] Spesifikasi lingkungan pengujian: hardware, software, database sandbox `abucom_test_db` (Bab 10).
  - [ ] Definisi, akronim, dan singkatan (Bab 1.6).
  - [ ] Template Test Report di Lampiran 14.3 (distribusi bug Critical/Major/Minor/Trivial).
  - [ ] Posisi dokumen dalam siklus SDLC dan hubungannya dengan dokumen lain (Bab 1.3 dan 1.4).

- [ ] **1.2.** Baca file `docs/sdlc/05_testing/02_test_cases.md` secara lengkap dari awal hingga akhir. Rangkum data berikut:
  - [ ] Konvensi penamaan ID test case: `TC-[MODUL]-[SKENARIO]-[URUT]` (Bab 1.7).
  - [ ] Distribusi 70 test case per modul, tipe, prioritas, dan tingkat pengujian (Bab 2).
  - [ ] Data uji global (test fixtures): 8 akun uji dengan username, peran, dan password (Bab 3.3).
  - [ ] Template Defect Report di Lampiran 20.3 — ini adalah template bug report awal yang sudah ada. **Catat seluruh field dan formatnya sebagai basis pengembangan template yang lebih lengkap**.
  - [ ] Entry/Exit Criteria pengujian (Bab 3.4).
  - [ ] Ketergantungan eksekusi test case (Bab 3.5).

- [ ] **1.3.** Baca file `docs/sdlc/05_testing/03_uat_script.md` secara lengkap dari awal hingga akhir. Rangkum data berikut:
  - [ ] Prosedur defect handling lengkap (Bab 16): klasifikasi keparahan UAT (Blocker/Critical/Major/Minor/Cosmetic).
  - [ ] Template pencatatan temuan UAT-BUG (Bab 16.2): seluruh field yang ada (ID Temuan, Judul, ID Skrip Asal, Tingkat Keparahan, Langkah Reproduksi, Hasil Aktual, Hasil Diharapkan, Nama Penguji, Status Temuan).
  - [ ] Alur eskalasi temuan bug dalam bentuk flowchart (Bab 16.3): langkah 1 s.d 7.
  - [ ] Tim pelaksana UAT: 4 peran (Senior UAT Analyst, Pemilik Usaha, Kepala Percetakan, QA Lead/Junior Dev) beserta tanggung jawab masing-masing (Bab 3.1).
  - [ ] Kriteria keluar UAT dan checklist sign-off 7 kriteria (Bab 17).

- [ ] **1.4.** Baca file `docs/sdlc/02_analysis/02_software_requirements.md`. Rangkum data berikut:
  - [ ] Daftar ID kebutuhan fungsional (SRS-F-001 s.d SRS-F-040) — hanya ID dan judul singkatnya saja sebagai referensi traceability.
  - [ ] Daftar ID kebutuhan non-fungsional (SRS-NF-001 s.d SRS-NF-011) — hanya ID dan judul singkatnya.

- [ ] **1.5.** Baca file `docs/sdlc/03_design/06_security_design.md`. Rangkum data berikut:
  - [ ] Spesifikasi keamanan yang relevan untuk bug keamanan: bcrypt cost factor 12, JWT HS256 8 jam, RBAC 8 peran, rate limiting 5 kali, audit log JSON, sanitasi CLI, enkripsi Fernet CRM, AES-256 backup, kepatuhan UU PDP No. 27/2022.
  - [ ] Catat SOP insiden keamanan jika ada — untuk prosedur eskalasi bug keamanan.

- [ ] **1.6.** Baca file `docs/sdlc/03_design/04_cli_interaction_flow.md`. Rangkum data berikut:
  - [ ] Format standar kode error visual CLI: `⛔ ERR-XXX-YYY: [Pesan Error]`.
  - [ ] Konteks rendering ANSI (rich & tabulate), breadcrumb navigasi, wrapping thermal 32/48 karakter.
  - [ ] Informasi yang relevan untuk mendeskripsikan bug pada antarmuka CLI.

- [ ] **1.7.** Baca file `docs/sdlc/02_analysis/06_access_control_matrix.md`. Rangkum data berikut:
  - [ ] Daftar 8 peran internal beserta level otoritasnya.
  - [ ] Matriks hak akses menu yang relevan untuk identifikasi peran terdampak bug otorisasi.

- [ ] **1.8.** Baca file `docs/sdlc/03_design/01_database_schema.sql`. Rangkum data berikut:
  - [ ] Nama-nama tabel utama yang relevan untuk identifikasi bug terkait integritas data.
  - [ ] Tabel `audit_logs` — struktur kolomnya untuk konteks pelacakan bug melalui audit trail.

- [ ] **1.9.** Baca file `docs/sdlc/03_design/05_bom_hpp_design.md`. Rangkum data berikut:
  - [ ] Spesifikasi presisi desimal `Decimal(15,4)` dan metode pembulatan `ROUND_HALF_UP`.
  - [ ] Konteks yang relevan untuk melaporkan bug terkait kesalahan kalkulasi keuangan.

- [ ] **1.10.** Baca file `docs/sdlc/narasi.txt` secara lengkap. Rangkum data berikut:
  - [ ] Daftar 7 jabatan operasional toko: Kepala Percetakan, Pramuniaga, Kasir, Desainer, Produksi Cetak, Fotocopy & Print, Gudang.
  - [ ] Jenis layanan usaha: percetakan, ATK, PPOB, jasa keuangan, jasa service.
  - [ ] Konteks lingkungan operasional: CLI, LAN offline, dual-OS (Windows 11 & Debian 12).
  - [ ] Susunan tim pengembang AI (6 model + 1 junior programmer).

---

### Tahap 2: Penyaringan Data yang Relevan

Setelah semua rangkuman selesai, lakukan penyaringan agar hanya data yang **spesifik dibutuhkan** oleh Bug Report Template yang masuk ke dokumen utama. Dokumen ini bukan tempat menampung seluruh informasi testing, melainkan hanya yang berkaitan langsung dengan:

- [ ] **2.1.** Pilih hanya data yang berkaitan dengan **pelaporan, pencatatan, dan pengelolaan bug/cacat** (defect). Buang informasi tentang langkah uji detail (itu milik Test Cases) atau prosedur UAT step-by-step (itu milik UAT Script).
- [ ] **2.2.** Pastikan informasi berikut **masuk** ke dokumen utama:
  - [ ] Definisi dan klasifikasi severity & priority bug.
  - [ ] Siklus hidup bug (lifecycle/state transition).
  - [ ] Kategori/tipe bug yang relevan untuk AbuCom.
  - [ ] Template formulir bug report yang lengkap dan terstandar.
  - [ ] Contoh pengisian nyata bug report (minimal 4 contoh berdasarkan tipe bug berbeda).
  - [ ] Prosedur pelaporan dan eskalasi bug.
  - [ ] Peran dan tanggung jawab dalam manajemen bug.
  - [ ] SLA penanganan per tingkat keparahan.
  - [ ] Ketertelusuran (traceability) bug ke test case, SRS, dan use case.
  - [ ] Daftar kode error sistem AbuCom yang valid.
  - [ ] Metrik dan ringkasan statistik bug.
  - [ ] Template kosong yang siap digunakan langsung.
- [ ] **2.3.** Pastikan informasi berikut **TIDAK masuk** ke dokumen utama (karena sudah dibahas di dokumen lain):
  - [ ] Langkah-langkah eksekusi test case (milik Test Cases).
  - [ ] Skrip pengujian UAT terperinci (milik UAT Script).
  - [ ] Detail strategi pengujian lengkap (milik Test Plan).
  - [ ] Spesifikasi kebutuhan fungsional detail (milik SRS).
  - [ ] Desain teknis security detail (milik Security Design).

---

### Tahap 3: Penyusunan YAML Front Matter dan Header

- [ ] **3.1.** Buat YAML front matter di bagian paling atas file dengan format berikut:
  ```yaml
  ---
  dokumen    : Bug Report Template
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [ISI TANGGAL PENGERJAAN FORMAT YYYY-MM-DD]
  status     : Draft
  penyusun   : Senior QA Engineer & Defect Management Specialist
  ---
  ```
- [ ] **3.2.** Buat heading utama: `# Bug Report Template — AbuCom`
- [ ] **3.3.** Buat tabel Riwayat Perubahan Dokumen dengan 1 entri versi 1.0 yang mendeskripsikan pembuatan awal dokumen.

---

### Tahap 4: Penyusunan Bab 1 — Informasi Dokumen

- [ ] **4.1.** Tulis Bab 1.1 (Tujuan Dokumen): Jelaskan bahwa dokumen ini menyediakan template standar dan prosedur baku untuk pencatatan, klasifikasi, pelacakan, dan pengelolaan temuan cacat (bug) selama seluruh fase pengujian sistem AbuCom CLI. Jelaskan bahwa dokumen ini menjadi jembatan komunikasi formal antara tim penguji (QA, UAT Tester, Pemilik Usaha) dan tim pengembang (Junior Programmer, AI Agent) untuk memastikan setiap bug terdokumentasi secara lengkap, dapat direproduksi, dan terselesaikan secara terstruktur.
- [ ] **4.2.** Tulis Bab 1.2 (Cakupan Dokumen): Nyatakan cakupan mencakup template formulir bug report, klasifikasi severity & priority, siklus hidup bug, prosedur eskalasi, contoh pengisian, metrik pelaporan, dan integrasi dengan dokumen testing lainnya.
- [ ] **4.3.** Tulis Bab 1.3 (Posisi Dokumen dalam Siklus SDLC): Gambarkan diagram ASCII sederhana menunjukkan posisi Bug Report Template sebagai deliverable keempat di Fase 05 — Testing, setelah Test Plan, Test Cases, dan UAT Script. Gunakan format diagram ASCII yang konsisten dengan dokumen SDLC sebelumnya.
- [ ] **4.4.** Tulis Bab 1.4 (Hubungan dengan Dokumen SDLC Lainnya):
  - [ ] Dokumen Input: Test Plan v1.1, Test Cases v1.1, UAT Script v1.1, SRS v1.1, Security Design v1.1, CLI Interaction Flow v1.1.
  - [ ] Dokumen Output: Test Report (sebagai sumber data distribusi bug saat eksekusi), Deployment/Release Document.
- [ ] **4.5.** Tulis Bab 1.5 (Audiens Target): 3 audiens (Junior Programmer, AI Testing Agent & QA Engineer, Pemilik Usaha & Kepala Percetakan) beserta penjelasan kebutuhan masing-masing terhadap dokumen ini.
- [ ] **4.6.** Tulis Bab 1.6 (Definisi, Akronim, dan Singkatan): Kumpulkan seluruh istilah relevan dari file referensi yang berkaitan dengan manajemen bug. Minimal mencakup: Bug/Defect, Severity, Priority, Regression, Hotfix, Patch, Workaround, Root Cause, Reproducibility, SLA, Blocker, Critical, Major, Minor, Trivial/Cosmetic, dan akronim teknis (SRS, TC, UAT, RBAC, JWT, CLI, ACID, dll).
- [ ] **4.7.** Tulis Bab 1.7 (Konvensi Penamaan ID Bug): Definisikan format ID bug yang konsisten dan sinkron dengan konvensi dokumen testing lain. Gunakan format:
  ```
  DEF-[MODUL]-[NOMOR_URUT]
  ```
  - `DEF`: Singkatan Defect.
  - `[MODUL]`: Kode modul (M1, M2, ..., M10, SEC, DEC, INT, CLI, NF).
  - `[NOMOR_URUT]`: Nomor urut 3-digit dalam modul tersebut (001, 002, dst).
  - Contoh: `DEF-M1-001`, `DEF-SEC-003`, `DEF-CLI-002`.
  - Untuk bug yang ditemukan saat UAT: `UAT-BUG-[NOMOR_URUT]`.

---

### Tahap 5: Penyusunan Bab 2 — Klasifikasi Tingkat Keparahan Bug (Severity)

- [ ] **5.1.** Tulis Bab 2.1 (Definisi Tingkat Keparahan): Jelaskan bahwa severity mengukur dampak teknis bug terhadap fungsionalitas sistem. Severity ditentukan oleh penguji (tester/QA) yang menemukan bug, berdasarkan tingkat gangguan yang ditimbulkan.
- [ ] **5.2.** Tulis Bab 2.2 (Tabel Klasifikasi Severity): Buat tabel dengan 5 level severity berikut:

  | Level | Nama | Definisi | Dampak pada Sistem |
  |---|---|---|---|
  | S1 | Blocker | Bug menyebabkan crash total / sistem tidak bisa dijalankan | Sistem mati total, pengujian tidak bisa dilanjutkan |
  | S2 | Critical | Bug pada fitur inti yang menyebabkan kehilangan data / keamanan | Fungsi kritis gagal, tidak ada workaround |
  | S3 | Major | Bug pada fitur utama yang mengganggu alur bisnis | Fungsi utama rusak, tersedia workaround |
  | S4 | Minor | Bug pada fitur penunjang yang tidak menghentikan operasi | Gangguan kecil, tidak mempengaruhi alur utama |
  | S5 | Cosmetic/Trivial | Bug visual/tampilan yang tidak mempengaruhi fungsionalitas | Estetika/typo, fungsionalitas 100% normal |

- [ ] **5.3.** Tulis Bab 2.3 (Contoh Konkret Severity per Level untuk AbuCom): Berikan minimal 1 contoh nyata per level severity yang diambil dari konteks modul AbuCom. Contoh:
  - **Blocker:** Aplikasi AbuCom CLI crash saat startup karena file `.env` tidak ditemukan (`ERR-FILE-001`).
  - **Critical:** Kalkulasi HPP BOM menghasilkan nilai `float` bukan `Decimal`, menyebabkan selisih harga produksi kumulatif.
  - **Major:** Menu Stock Opname Approval bisa diakses oleh peran `gudang` (seharusnya hanya `kepala_percetakan`).
  - **Minor:** Breadcrumb navigasi menampilkan path yang salah pada sub-menu Layanan PPOB.
  - **Cosmetic:** Typo pada label menu "Administarsi" seharusnya "Administrasi".

---

### Tahap 6: Penyusunan Bab 3 — Klasifikasi Prioritas Perbaikan (Priority)

- [ ] **6.1.** Tulis Bab 3.1 (Definisi Tingkat Prioritas): Jelaskan bahwa priority mengukur urgensi bisnis untuk perbaikan bug. Priority ditentukan oleh Project Lead / Pemilik Usaha, berdasarkan dampak terhadap jadwal dan kebutuhan bisnis.
- [ ] **6.2.** Tulis Bab 3.2 (Tabel Klasifikasi Priority): Buat tabel dengan 4 level priority:

  | Level | Nama | Target SLA Perbaikan | Deskripsi |
  |---|---|---|---|
  | P1 | Urgent | ≤ 4 jam | Harus diperbaiki segera, menghentikan seluruh pengujian |
  | P2 | High | ≤ 1 hari kerja | Harus diperbaiki dalam siklus uji berjalan |
  | P3 | Medium | ≤ 3 hari kerja | Diperbaiki sebelum rilis berikutnya |
  | P4 | Low | Backlog / rilis berikutnya | Diperbaiki saat ada waktu luang |

- [ ] **6.3.** Tulis Bab 3.3 (Matriks Severity vs Priority): Buat tabel matriks 5x4 yang memetakan kombinasi severity dan priority, beserta aksi yang diambil untuk setiap kombinasi.

---

### Tahap 7: Penyusunan Bab 4 — Siklus Hidup Bug (Bug Lifecycle)

- [ ] **7.1.** Tulis Bab 4.1 (Diagram Status Bug): Buat diagram menggunakan format Mermaid `stateDiagram-v2` atau ASCII art yang menggambarkan state transition bug:
  ```
  New → Open → Assigned → In Progress → Fixed → Re-Test → Closed
                                                    ↓
                                                 Reopened → Assigned
  Juga tambahkan: New → Rejected (Invalid/Duplicate)
                  New → Deferred (Ditunda)
  ```
- [ ] **7.2.** Tulis Bab 4.2 (Deskripsi Setiap Status): Jelaskan arti setiap status bug secara detail:
  - **New**: Bug baru dilaporkan oleh tester, belum ditelaah.
  - **Open**: Bug sudah ditelaah dan dikonfirmasi valid oleh QA Lead.
  - **Assigned**: Bug sudah dialokasikan ke programmer/AI agent tertentu untuk diperbaiki.
  - **In Progress**: Programmer sedang mengerjakan perbaikan.
  - **Fixed**: Programmer selesai memperbaiki, menunggu verifikasi ulang.
  - **Re-Test**: QA/Tester melakukan pengujian ulang terhadap perbaikan.
  - **Closed**: Bug sudah terverifikasi selesai diperbaiki dengan benar.
  - **Reopened**: Bug muncul kembali setelah dinyatakan fixed (re-test gagal).
  - **Rejected**: Bug dinyatakan tidak valid / duplikat / bukan bug (working as designed).
  - **Deferred**: Bug valid tetapi ditunda perbaikannya ke rilis mendatang.
- [ ] **7.3.** Tulis Bab 4.3 (Aturan Transisi): Jelaskan siapa yang berhak mengubah status bug pada setiap transisi (misal: hanya QA yang bisa mengubah dari Fixed ke Closed atau Reopened, hanya Project Lead yang bisa mengubah ke Deferred).

---

### Tahap 8: Penyusunan Bab 5 — Kategori Bug (Bug Category)

- [ ] **8.1.** Tulis Bab 5.1 (Tabel Kategori Bug): Definisikan minimal 8 kategori bug yang relevan untuk AbuCom:

  | Kode Kategori | Nama Kategori | Deskripsi |
  |---|---|---|
  | CAT-FUNC | Fungsional | Bug pada logika bisnis atau alur kerja yang tidak sesuai spesifikasi SRS |
  | CAT-SEC | Keamanan | Bug pada otentikasi, otorisasi RBAC, enkripsi, audit log, atau kepatuhan UU PDP |
  | CAT-DEC | Presisi Desimal | Bug pada kalkulasi `Decimal(15,4)`, pembulatan `ROUND_HALF_UP`, HPP, payroll, depresiasi |
  | CAT-DB | Integritas Database | Bug pada constraint, foreign key, ACID transaction, atau data korupsi |
  | CAT-CLI | Antarmuka CLI | Bug pada rendering ANSI, breadcrumb, struk thermal, encoding UTF-8, atau navigasi |
  | CAT-PERF | Performa | Bug pada response time > 2 detik, memory leak, atau degradasi kecepatan |
  | CAT-COMPAT | Kompatibilitas | Bug pada portabilitas lintas OS (Windows 11 vs Debian 12) |
  | CAT-CONFIG | Konfigurasi | Bug pada pembacaan `.env`, parameter `system_configs`, atau connection pooling |

- [ ] **8.2.** Tulis Bab 5.2 (Pemetaan Kategori ke Modul): Buat tabel yang memetakan kategori bug mana saja yang paling mungkin muncul di setiap modul (M.1 s.d M.10).

---

### Tahap 9: Penyusunan Bab 6 — Template Formulir Bug Report

- [ ] **9.1.** Tulis Bab 6.1 (Template Formulir Utama): Buat template tabel formulir bug report yang lengkap dengan field berikut:

  | Field | Deskripsi | Contoh |
  |---|---|---|
  | **ID Bug** | ID unik sesuai konvensi Bab 1.7 | `DEF-M1-001` |
  | **Judul Bug** | Deskripsi singkat, jelas, dan spesifik tentang bug | `Kalkulasi HPP BOM karet flash menghasilkan float bukan Decimal` |
  | **Tanggal Pelaporan** | Tanggal bug ditemukan (YYYY-MM-DD) | `2026-06-01` |
  | **Pelapor** | Nama tester/agent yang menemukan bug | `kasir01 (UAT Sesi 3)` |
  | **Versi Aplikasi** | Versi build AbuCom yang diuji | `v1.1` |
  | **Modul Terdampak** | Kode dan nama modul yang terdampak | `M.2 — Inventaris, BOM & Opname` |
  | **Kategori Bug** | Kode kategori sesuai Bab 5 | `CAT-DEC` |
  | **Severity** | Level S1–S5 sesuai Bab 2 | `S2 — Critical` |
  | **Priority** | Level P1–P4 sesuai Bab 3 | `P1 — Urgent` |
  | **Referensi SRS** | ID kebutuhan SRS yang dilanggar | `SRS-F-007` |
  | **Referensi Use Case** | ID use case terkait | `UC-007` |
  | **Referensi Test Case** | ID test case yang gagal | `TC-M2-002-01` |
  | **Peran Aktor** | Peran login saat bug terjadi | `kepala_percetakan` |
  | **Lingkungan** | OS, terminal, versi Python, database | `Windows 11, Terminal CLI, Python 3.14.2, abucom_test_db` |
  | **Prasyarat/Prakondisi** | Kondisi data sebelum bug terjadi | `Stok karet flash = 5.0000 m², BOM stempel terdaftar` |
  | **Langkah Reproduksi** | Langkah demi langkah untuk mereproduksi bug (numbered) | `1. Login sebagai kepala...` `2. Masuk menu BOM...` `3. ...` |
  | **Hasil Diharapkan** | Perilaku yang seharusnya terjadi sesuai spesifikasi | `HPP = Decimal('4750.0000')` |
  | **Hasil Aktual** | Perilaku menyimpang yang terjadi | `HPP = 4750.000000001 (float)` |
  | **Lampiran** | Screenshot CLI, stacktrace, log error, query SQL | `[Lampirkan screenshot/log]` |
  | **Ditugaskan Ke** | Programmer/Agent yang ditugaskan memperbaiki | `[Diisi oleh QA Lead]` |
  | **Status** | Status saat ini sesuai lifecycle Bab 4 | `New` |
  | **Tanggal Perbaikan** | Tanggal bug selesai diperbaiki | `[Diisi saat Fixed]` |
  | **Catatan Perbaikan** | Deskripsi teknis solusi yang diterapkan | `[Diisi oleh programmer]` |
  | **Tanggal Verifikasi** | Tanggal re-test berhasil | `[Diisi saat Closed]` |

- [ ] **9.2.** Tulis Bab 6.2 (Panduan Pengisian Setiap Field): Jelaskan aturan penulisan untuk setiap field secara detail. Berikan panduan khusus:
  - [ ] Judul Bug: Harus mengandung kata kerja + lokasi spesifik + dampak. Contoh format: `[Apa yang salah] pada [di mana] menyebabkan [dampak]`.
  - [ ] Langkah Reproduksi: Harus dimulai dari kondisi awal (login sebagai siapa), setiap langkah harus atomik (1 aksi per langkah), sertakan data input yang tepat.
  - [ ] Hasil Diharapkan vs Aktual: Harus spesifik, kuantitatif jika memungkinkan (angka presisi desimal, kode error persis).
  - [ ] Lampiran: Wajib menyertakan screenshot layar CLI jika bug terkait visual, atau stacktrace Python jika bug terkait crash.

- [ ] **9.3.** Tulis Bab 6.3 (Contoh Bug Fungsional): Buat contoh pengisian lengkap untuk bug fungsional. Gunakan skenario dari Test Cases, misalnya: "Menu Pelunasan DP menerima nominal kurang dari sisa tagihan tanpa menampilkan error `ERR-VAL-003`". Isi seluruh field template dengan data konkret.
- [ ] **9.4.** Tulis Bab 6.4 (Contoh Bug Keamanan): Buat contoh pengisian lengkap untuk bug keamanan. Gunakan skenario misalnya: "Peran `desainer` berhasil mengakses menu Smart Payroll tanpa diblokir oleh RBAC, error `ERR-AUTH-003` tidak muncul". Isi seluruh field template.
- [ ] **9.5.** Tulis Bab 6.5 (Contoh Bug Presisi Desimal): Buat contoh pengisian lengkap untuk bug kalkulasi. Gunakan skenario misalnya: "Perhitungan depresiasi aset bulanan printer menghasilkan `166666.6666` bukan `166666.6667` (salah pembulatan `ROUND_HALF_UP`)". Isi seluruh field template.
- [ ] **9.6.** Tulis Bab 6.6 (Contoh Bug CLI Visual): Buat contoh pengisian lengkap untuk bug antarmuka. Gunakan skenario misalnya: "Garis pemisah struk thermal 58mm berjumlah 31 karakter (seharusnya 32 karakter), menyebabkan misalignment kolom harga". Isi seluruh field template.

---

### Tahap 10: Penyusunan Bab 7 — Prosedur Pelaporan dan Eskalasi

- [ ] **10.1.** Tulis Bab 7.1 (Alur Pelaporan Bug): Buat flowchart menggunakan diagram Mermaid yang menggambarkan alur dari penemuan bug hingga penutupan. Adaptasi dan perluas dari alur eskalasi UAT Script Bab 16.3. Pastikan mencakup jalur normal dan jalur eskalasi untuk bug Blocker/Critical.
- [ ] **10.2.** Tulis Bab 7.2 (Peran dan Tanggung Jawab): Definisikan peran dalam manajemen bug:
  - **Penguji (Tester/QA/UAT Tester):** Menemukan, mendokumentasikan, dan melaporkan bug. Melakukan re-test setelah perbaikan.
  - **QA Lead / Senior UAT Analyst:** Menelaah validitas bug, menentukan severity, mengarahkan eskalasi.
  - **Junior Programmer / AI Agent Developer:** Menerima assignment, menganalisis root cause, melakukan perbaikan (hotfix/patch), mendokumentasikan solusi.
  - **Project Lead / Pemilik Usaha:** Menentukan priority bisnis, menyetujui penundaan (deferred), menandatangani penutupan bug kritis.
- [ ] **10.3.** Tulis Bab 7.3 (SLA Penanganan Bug per Severity):

  | Severity | SLA Respon Awal | SLA Perbaikan Selesai | SLA Re-Test |
  |---|---|---|---|
  | S1 — Blocker | ≤ 1 jam | ≤ 4 jam | ≤ 2 jam setelah Fixed |
  | S2 — Critical | ≤ 2 jam | ≤ 8 jam (1 hari kerja) | ≤ 4 jam setelah Fixed |
  | S3 — Major | ≤ 4 jam | ≤ 24 jam (3 hari kerja) | ≤ 1 hari setelah Fixed |
  | S4 — Minor | ≤ 1 hari | ≤ 5 hari kerja | Batch re-test mingguan |
  | S5 — Cosmetic | ≤ 2 hari | Backlog rilis berikutnya | Batch re-test rilis |

- [ ] **10.4.** Tulis Bab 7.4 (Prosedur Eskalasi Khusus Bug Keamanan): Jelaskan prosedur khusus untuk bug bertipe `CAT-SEC`:
  - Bug keamanan otomatis mendapat minimal priority P1 atau P2.
  - Wajib dilaporkan langsung ke Pemilik Usaha selain ke QA Lead.
  - Informasi bug keamanan bersifat konfidensial dan tidak boleh disebarkan ke staf non-otoritatif.
  - Perbaikan wajib menyertakan bukti pengujian ulang keamanan (re-test security).

---

### Tahap 11: Penyusunan Bab 8 — Integrasi dengan Proses Pengujian

- [ ] **11.1.** Tulis Bab 8.1 (Hubungan Bug Report dengan Test Case): Jelaskan bahwa setiap bug yang ditemukan selama eksekusi test case harus merujuk ID test case yang gagal (field `Referensi Test Case` pada formulir). Jelaskan alur: Test Case FAIL → Bug Report dibuat → Bug Fixed → Test Case di-rerun.
- [ ] **11.2.** Tulis Bab 8.2 (Hubungan Bug Report dengan UAT Script): Jelaskan bahwa bug yang ditemukan saat UAT menggunakan ID format `UAT-BUG-XXX` dan harus merujuk ID skrip UAT asal. Jelaskan integrasi dengan prosedur defect handling UAT Script Bab 16.
- [ ] **11.3.** Tulis Bab 8.3 (Ketertelusuran Bug): Buat contoh tabel matriks ketertelusuran:

  | ID Bug | Test Case Gagal | Skenario Asal | SRS Dilanggar | Use Case Terkait | Modul | Status |
  |---|---|---|---|---|---|---|
  | `DEF-M2-001` | `TC-M2-002-01` | `M2-TC-002` | `SRS-F-007` | `UC-007` | M.2 | Open |

---

### Tahap 12: Penyusunan Bab 9 — Metrik dan Pelaporan Agregat Bug

- [ ] **12.1.** Tulis Bab 9.1 (Template Ringkasan Statistik Bug): Buat template dashboard ringkasan yang mencakup:
  ```
  Laporan Ringkasan Statistik Bug (Bug Summary Dashboard)
  =======================================================
  Tanggal Laporan    : [Diisi saat pelaporan]
  Periode Pelaporan  : [Tanggal Mulai] s.d [Tanggal Selesai]
  Versi Aplikasi     : v1.1

  1. Total Bug Ditemukan    : [Diisi saat eksekusi]
  2. Distribusi per Severity:
     * S1 Blocker  : [_] Open | [_] Fixed | [_] Closed
     * S2 Critical : [_] Open | [_] Fixed | [_] Closed
     * S3 Major    : [_] Open | [_] Fixed | [_] Closed
     * S4 Minor    : [_] Open | [_] Fixed | [_] Closed
     * S5 Cosmetic : [_] Open | [_] Fixed | [_] Closed

  3. Distribusi per Modul:
     * M.1 Transaksi    : [_] Bug
     * M.2 Inventaris   : [_] Bug
     * ...dst s.d M.10

  4. Bug Resolution Rate  : [_]% (Closed / Total)
  5. Bug Reopen Rate      : [_]% (Reopened / Total Closed)
  6. Mean Time to Resolve : [_] jam (rata-rata waktu perbaikan)
  ```

- [ ] **12.2.** Tulis Bab 9.2 (Metrik Kualitas yang Dilacak): Definisikan minimal 5 metrik:
  - Bug Discovery Rate (jumlah bug baru per hari/sesi).
  - Bug Fix Rate (jumlah bug diperbaiki per hari).
  - Bug Reopen Rate (persentase bug yang dibuka kembali).
  - Mean Time to Resolve / MTTR (rata-rata waktu perbaikan per severity).
  - Defect Density (jumlah bug per modul / per 1000 LOC).

---

### Tahap 13: Penyusunan Bab 10 — Lampiran

- [ ] **13.1.** Tulis Bab 10.1 (Glosarium): Kumpulkan seluruh istilah yang digunakan dalam dokumen, susun secara alfabet.
- [ ] **13.2.** Tulis Bab 10.2 (Daftar Kode Error Sistem AbuCom): Salin seluruh 15 kode error dari Test Plan Bab 12.4 ke dalam tabel yang mudah dirujuk:

  | Kode Error | Pesan Error | Konteks/Trigger |
  |---|---|---|
  | `ERR-AUTH-001` | `Kredensial tidak valid. Silakan coba kembali!` | Login username/password salah |
  | `ERR-AUTH-002` | `Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!` | 5x gagal login berturut-turut |
  | ... | ... | ... |

  Salin seluruh 15 kode error secara lengkap tanpa ada yang terlewat.

- [ ] **13.3.** Tulis Bab 10.3 (Template Bug Report Kosong Siap Cetak): Salin ulang template formulir Bab 6.1 dalam format code block yang rapi, siap disalin-tempel langsung oleh penguji tanpa perlu modifikasi struktur.
- [ ] **13.4.** Tulis Bab 10.4 (Checklist Kelengkapan Bug Report): Buat checklist yang digunakan penguji/QA untuk memverifikasi apakah bug report yang dibuat sudah lengkap:
  - [ ] ID Bug terisi dengan format yang benar.
  - [ ] Judul bug deskriptif dan spesifik.
  - [ ] Severity dan Priority sudah ditentukan.
  - [ ] Langkah reproduksi lengkap dan atomik.
  - [ ] Hasil diharapkan dan aktual terisi dengan data spesifik.
  - [ ] Referensi SRS / Test Case / Use Case terisi.
  - [ ] Informasi lingkungan (OS, versi, database) terisi.
  - [ ] Screenshot/log dilampirkan (jika relevan).

---

### Tahap 14: Penyusunan Bab 11 — Referensi Dokumen

- [ ] **14.1.** Tulis tabel referensi dokumen yang digunakan dalam penyusunan dokumen ini. Masukkan semua file referensi primer dan sekunder yang disebutkan di Bab 3 issue ini:

  | No | Kode Ref | Nama Dokumen | Path File | Versi |
  |----|----------|--------------|-----------|---|
  | 1 | R-TP | Test Plan v1.1 | `docs/sdlc/05_testing/01_test_plan.md` | 1.1 |
  | 2 | R-TC | Test Cases v1.1 | `docs/sdlc/05_testing/02_test_cases.md` | 1.1 |
  | 3 | R-UAT | UAT Script v1.1 | `docs/sdlc/05_testing/03_uat_script.md` | 1.1 |
  | 4 | R-SRS | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | 1.1 |
  | 5 | R-SEC | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | 1.1 |
  | 6 | R-CLI | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | 1.1 |
  | 7 | R-ACM | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | 1.1 |
  | 8 | R-DB | Database Schema v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | 1.1 |
  | 9 | R-BOM | BOM & HPP Design v1.1 | `docs/sdlc/03_design/05_bom_hpp_design.md` | 1.1 |
  | 10 | R-NAR | Narasi Proyek | `docs/sdlc/narasi.txt` | - |

---

### Tahap 15: Penandaan Data Kosong

- [ ] **15.1.** Setelah seluruh dokumen selesai disusun, lakukan pemeriksaan akhir terhadap seluruh isi dokumen.
- [ ] **15.2.** Jika ada data atau informasi yang **tidak tersedia** di dalam file referensi dan memerlukan keputusan manual dari Pemilik Usaha atau QA Lead, tandai dengan placeholder berikut:
  ```
  [DATA BELUM TERSEDIA - Perlu diisi manual oleh <PERAN YANG BERTANGGUNG JAWAB>]
  ```
- [ ] **15.3.** Kumpulkan seluruh placeholder `[DATA BELUM TERSEDIA]` di akhir Bab 10 atau di catatan khusus agar mudah ditemukan dan diisi secara manual.

---

### Tahap 16: Penulisan ke Target File

- [ ] **16.1.** Setelah seluruh konten dokumen selesai disusun dan diperiksa, tulis seluruh hasil penyusunan ke target file:
  ```
  docs/sdlc/05_testing/04_bug_report_template.md
  ```
- [ ] **16.2.** Pastikan file ditulis dalam encoding UTF-8 tanpa BOM.
- [ ] **16.3.** Pastikan format markdown valid dan konsisten (heading, tabel, code block, list).
- [ ] **16.4.** Pastikan seluruh hyperlink ke dokumen referensi menggunakan path relatif yang konsisten dengan dokumen SDLC lainnya.

---

### Tahap 17: Validasi Akhir

- [ ] **17.1.** Periksa ulang bahwa seluruh 11 bab (sesuai kerangka Bab 4 issue ini) telah tertulis lengkap tanpa ada bab yang terlewat.
- [ ] **17.2.** Periksa ulang bahwa setiap contoh pengisian bug report (Bab 6.3 s.d 6.6) mengisi **seluruh field** template tanpa ada yang kosong.
- [ ] **17.3.** Periksa ulang bahwa seluruh 15 kode error di Lampiran 10.2 tersalin lengkap dari Test Plan.
- [ ] **17.4.** Periksa ulang bahwa semua istilah, akronim, dan konvensi penamaan konsisten dengan dokumen SDLC lainnya.
- [ ] **17.5.** Periksa ulang bahwa tabel Referensi Dokumen (Bab 11) mencantumkan seluruh 10 file referensi.
- [ ] **17.6.** Periksa ulang bahwa bahasa Indonesia yang digunakan natural, tidak ambigu, dan mudah dipahami.
- [ ] **17.7.** Periksa ulang bahwa dokumen ini cukup lengkap dan layak dijadikan referensi bagi fase SDLC selanjutnya (khususnya Test Report dan Deployment Document) tanpa perlu interupsi atau klarifikasi tambahan.

---

## 6. Instruksi Tambahan (Kaidah Standar Bug Report Template)

Berikut adalah instruksi tambahan yang merupakan kaidah standar pembuatan Bug Report Template yang belum disebutkan secara eksplisit di atas, namun penting untuk kelengkapan dan kualitas dokumen:

- [ ] **6.1. Prinsip "Good Bug Report":** Di dalam Bab 6.2 (Panduan Pengisian), tambahkan panduan prinsip penulisan bug report yang baik:
  - **Spesifik:** Satu bug report hanya membahas satu bug. Jangan menggabungkan beberapa bug dalam satu laporan.
  - **Dapat Direproduksi (Reproducible):** Langkah reproduksi harus cukup detail sehingga programmer yang belum pernah melihat bug tersebut dapat mereproduksinya secara mandiri.
  - **Tidak Ambigu:** Gunakan bahasa yang presisi. Hindari kata-kata seperti "kadang-kadang", "sepertinya", atau "mungkin". Gunakan data kuantitatif jika memungkinkan.
  - **Objektif:** Laporkan fakta, bukan opini. Jelaskan apa yang terjadi, bukan mengapa itu terjadi (root cause analysis adalah tugas programmer).

- [ ] **6.2. Penanganan Bug Duplikat:** Tambahkan panduan di Bab 7 tentang prosedur penanganan bug duplikat:
  - Sebelum membuat bug report baru, cek apakah bug yang sama sudah pernah dilaporkan.
  - Jika duplikat, tambahkan catatan referensi ke bug report asli dan ubah status menjadi `Rejected (Duplicate)` dengan referensi ID bug asli.

- [ ] **6.3. Penanganan Bug Regression:** Tambahkan panduan tentang bug regresi:
  - Bug regresi adalah bug yang muncul di area yang sebelumnya berfungsi normal, akibat perubahan kode baru.
  - Bug regresi otomatis mendapat minimal severity S3 (Major) dan priority P2 (High).
  - Wajib menyertakan informasi versi terakhir yang masih berfungsi normal.

- [ ] **6.4. Informasi Lingkungan yang Wajib Dicantumkan:** Standarkan field lingkungan minimal mencakup:
  - Sistem Operasi dan versinya (Windows 11 / Debian 12 Bookworm).
  - Terminal yang digunakan (Windows Terminal, CMD, GNOME Terminal, bash).
  - Versi Python runtime (3.14.2+).
  - Nama database sandbox (`abucom_test_db`).
  - Node koneksi (Server/Klien).

- [ ] **6.5. Penomoran Langkah Reproduksi:** Standarkan format langkah reproduksi menggunakan numbered list (1, 2, 3, ...) dengan format konsisten:
  ```
  1. Login sebagai [peran] menggunakan username [username].
  2. Masuk menu [Nama Menu] > [Sub-Menu].
  3. Input [nama field] = [nilai input].
  4. Klik/Pilih [aksi].
  5. Perhatikan [lokasi tampilan].
  ```

---

## 7. Ringkasan Deliverable

| No | Deliverable | Status |
|----|------------|--------|
| 1 | Seluruh file referensi dibaca dan dirangkum | `[ ]` |
| 2 | Data yang relevan disaring dan dipilih | `[ ]` |
| 3 | YAML Front Matter dan header dokumen ditulis | `[ ]` |
| 4 | Bab 1 — Informasi Dokumen ditulis lengkap | `[ ]` |
| 5 | Bab 2 — Klasifikasi Severity ditulis lengkap | `[ ]` |
| 6 | Bab 3 — Klasifikasi Priority ditulis lengkap | `[ ]` |
| 7 | Bab 4 — Siklus Hidup Bug ditulis lengkap | `[ ]` |
| 8 | Bab 5 — Kategori Bug ditulis lengkap | `[ ]` |
| 9 | Bab 6 — Template Formulir + 4 Contoh ditulis lengkap | `[ ]` |
| 10 | Bab 7 — Prosedur Pelaporan & Eskalasi ditulis lengkap | `[ ]` |
| 11 | Bab 8 — Integrasi dengan Proses Pengujian ditulis lengkap | `[ ]` |
| 12 | Bab 9 — Metrik & Pelaporan Agregat ditulis lengkap | `[ ]` |
| 13 | Bab 10 — Lampiran (Glosarium, Kode Error, Template Kosong, Checklist) ditulis lengkap | `[ ]` |
| 14 | Bab 11 — Referensi Dokumen ditulis lengkap | `[ ]` |
| 15 | Data kosong ditandai dengan placeholder `[DATA BELUM TERSEDIA]` | `[ ]` |
| 16 | Hasil akhir ditulis ke `docs/sdlc/05_testing/04_bug_report_template.md` | `[ ]` |
| 17 | Validasi akhir 7 poin checklist selesai | `[ ]` |
