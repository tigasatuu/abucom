# Pembuatan dan Penyusunan Dokumen Changelog

---

| Atribut          | Nilai                                                                 |
|:-----------------|:----------------------------------------------------------------------|
| **Judul**        | Pembuatan dan Penyusunan Dokumen Changelog AbuCom v1.0.0              |
| **Tipe**         | Documentation — New Document                                          |
| **Prioritas**    | High                                                                  |
| **Status**       | Open                                                                  |
| **Target File**  | `docs/sdlc/07_maintenance/02_changelog.md`                            |
| **Tanggal Buat** | 2026-05-27                                                            |
| **Dibuat Oleh**  | Antigravity (Claude Opus 4.6 Thinking — System Strategist)            |
| **Ditugaskan Ke**| Junior Programmer / LLM AI Model (Executor)                          |

---

## 1. Konteks dan Latar Belakang

### 1.1. Deskripsi Singkat Issue
Issue ini berisi instruksi perencanaan low-level untuk membuat dan menyusun dokumen **Changelog** proyek AbuCom secara lengkap, akurat, dan sesuai standar praktik industri. Dokumen Changelog merupakan deliverable kedua pada **Fase 07 — Maintenance** dalam siklus SDLC AbuCom, yang berfungsi sebagai catatan perubahan kronologis resmi seluruh rilis perangkat lunak, perbaikan bug, penambahan fitur, dan perubahan arsitektur sistem dari waktu ke waktu.

### 1.2. Mengapa Dokumen Ini Penting
- **Ketertelusuran Perubahan (Traceability):** Changelog menjadi sumber kebenaran tunggal (*Single Source of Truth*) untuk melacak apa saja yang berubah, kapan berubah, dan mengapa berubah di setiap rilis aplikasi AbuCom.
- **Referensi Rollback & Debugging:** Ketika terjadi bug di produksi, tim pengembang dapat menelusuri changelog untuk mengidentifikasi rilis mana yang memperkenalkan perubahan tertentu.
- **Kepatuhan Standar Industri:** Changelog merupakan artefak wajib dalam praktik SDLC modern, mematuhi konvensi [Keep a Changelog](https://keepachangelog.com/) dan terintegrasi dengan [Semantic Versioning (SemVer)](https://semver.org/) yang sudah diadopsi proyek ini.
- **Input untuk Fase Selanjutnya:** Dokumen ini menjadi acuan bagi Release Notes versi berikutnya, audit kualitas, dan perencanaan roadmap.

### 1.3. Posisi Dokumen dalam SDLC

```text
+-------------------------------------------------------+
|              Fase 07 — Maintenance                     |
|                                                        |
|  Deliverable 1: Maintenance Guide [SELESAI v1.1]      |
|  Deliverable 2: Changelog [ISSUE INI — TARGET]        |
+-------------------------------------------------------+
```

---

## 2. Persona Pelaksana

### 2.1. Persona yang Ditugaskan
**Senior Configuration Manager & Release Documentation Specialist**

### 2.2. Justifikasi Pemilihan Persona
Persona ini dipilih karena:
- Changelog adalah dokumen manajemen konfigurasi dan rilis, bukan dokumen teknis arsitektur atau panduan operasional. Oleh karena itu, persona seorang **Configuration Manager** yang menguasai *version control*, *release management*, dan *change tracking* adalah yang paling relevan dan otoritatif.
- Persona ini memiliki keahlian dalam menyusun catatan perubahan yang presisi, terstruktur berdasarkan versi SemVer, dan mengikuti konvensi Conventional Commits.
- Persona ini memahami bagaimana memetakan setiap perubahan kode/fitur ke nomor versi rilis, kategori perubahan (Added, Changed, Fixed, Deprecated, Removed, Security), dan kode referensi SRS.

### 2.3. Gaya Bahasa dan Penulisan
- Bahasa Indonesia formal, profesional, dan teknis.
- Setiap entri changelog ditulis dalam kalimat pendek, padat, dan deskriptif menggunakan kata kerja lampau (contoh: "Ditambahkan", "Diperbaiki", "Dihapus").
- Hindari kata-kata ambigu atau penjelasan yang terlalu panjang per entri.

---

## 3. File Referensi yang Digunakan

### 3.1. Daftar File Referensi (Urut Prioritas)

Berikut adalah daftar file referensi yang **wajib dibaca secara menyeluruh** sebelum menyusun dokumen Changelog. Setiap file memiliki peran spesifik dalam menyediakan data yang dibutuhkan.

| No | Kode Ref | Nama Dokumen | Path Relatif | Prioritas | Data yang Diambil |
|:--:|:--------:|:-------------|:-------------|:---------:|:------------------|
| 1 | **R-01** | Release Notes v1.1 | `docs/sdlc/06_deployment/03_release_notes.md` | **PRIMER** | Seluruh daftar fitur baru (Bab 4), fitur keamanan (Bab 5), bug fixes & improvements (Bab 6), known limitations (Bab 7), known issues (Bab 8), konfigurasi default (Bab 10), QA summary (Bab 11), arsitektur deployment (Bab 12), risiko rilis (Bab 13), roadmap (Bab 15), dan versi dependencies (Bab 3.2.3). |
| 2 | **R-02** | Maintenance Guide v1.1 | `docs/sdlc/07_maintenance/01_maintenance_guide.md` | **PRIMER** | Daftar modul fungsional aktif (Bab 2.3), daftar tabel database (Bab 2.4), pustaka dependensi (Bab 2.5), kategori pemeliharaan (Bab 3), prosedur patching (Bab 10), dan SLA bug (Bab 10.8). |
| 3 | **R-03** | Git Workflow v1.1 | `docs/sdlc/04_implementation/04_git_workflow.md` | **PRIMER** | Konvensi Conventional Commits (Bab 5), Semantic Versioning SemVer (Bab 9), strategi tagging (Bab 9.3-9.4), dan scope commit valid (Bab 5.3). |
| 4 | **R-04** | Project Charter v1.1 | `docs/sdlc/01_planning/01_project_charter.md` | **SEKUNDER** | Nama proyek, deskripsi produk, versi awal, timeline milestone, susunan tim pengembang, dan informasi sponsor proyek. |
| 5 | **R-05** | Software Requirements Spec v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | **SEKUNDER** | Kode referensi kebutuhan fungsional (SRS-F-001 s.d SRS-F-040) dan kebutuhan non-fungsional untuk memetakan entri changelog ke spesifikasi. |
| 6 | **R-06** | Database Schema v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | **SEKUNDER** | Daftar 28 tabel InnoDB dan constraint untuk kategori "Database" pada changelog. |
| 7 | **R-07** | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` | **SEKUNDER** | Arsitektur deployment, topologi LAN, dan connection pooling. |
| 8 | **R-08** | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | **SEKUNDER** | Fitur keamanan (bcrypt, JWT, Fernet, RBAC, audit trail, AES-256 backup) untuk kategori "Security" pada changelog. |
| 9 | **R-09** | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` | **TERSIER** | Standar paradigma FP murni, PEP 8/257/484, presisi Decimal. |
| 10 | **R-10** | Module Structure v1.1 | `docs/sdlc/04_implementation/03_module_structure.md` | **TERSIER** | Peta modul dan file mapping untuk scope referensi changelog. |
| 11 | **R-11** | Test Plan v1.1 | `docs/sdlc/05_testing/01_test_plan.md` | **TERSIER** | Hasil testing untuk keterangan QA status changelog. |
| 12 | **R-12** | Deployment Guide v1.1 | `docs/sdlc/06_deployment/01_deployment_guide.md` | **TERSIER** | Prosedur instalasi dan konfigurasi yang terdokumentasi. |
| 13 | **R-13** | Tech Stack Decision v1.1 | `docs/sdlc/01_planning/04_tech_stack_decision.md` | **TERSIER** | Keputusan teknologi terpilih dan batasan platform. |
| 14 | **R-14** | Bug Report Template v1.1 | `docs/sdlc/05_testing/04_bug_report_template.md` | **TERSIER** | Format pelaporan bug dan known issues. |

> **CATATAN:** File `docs/sdlc/narasi.txt` **TIDAK DIGUNAKAN** sebagai referensi untuk dokumen ini. Changelog adalah dokumen teknis perubahan perangkat lunak yang seluruh datanya bersumber dari dokumen SDLC formal yang sudah ada (R-01 s.d R-14). Narasi pemilik usaha tidak relevan secara langsung untuk catatan perubahan versi software.

---

## 4. Kerangka Struktur Dokumen Changelog

### 4.1. Standar yang Diadopsi
Dokumen ini mengadopsi standar **[Keep a Changelog v1.1.0](https://keepachangelog.com/)** yang dikombinasikan dengan **Semantic Versioning (SemVer)** dan **Conventional Commits** yang sudah distandarkan dalam Git Workflow AbuCom (R-03).

### 4.2. Struktur Kerangka Wajib

Berikut adalah kerangka lengkap yang **WAJIB** diikuti secara ketat dalam penyusunan dokumen Changelog:

```markdown
---
(Front Matter YAML: dokumen, proyek, versi, tanggal, status, penyusun)
---

# Changelog — AbuCom

## Riwayat Perubahan Dokumen
(Tabel versi dokumen ini sendiri)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya (Input & Output)
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan
### 1.7. Konvensi Format Entri Changelog

---

## 2. Panduan Pembacaan Changelog
### 2.1. Format Versi (Semantic Versioning)
### 2.2. Kategori Perubahan (Change Types)
### 2.3. Format Entri Changelog
### 2.4. Kode Referensi Terkait (SRS-F-XXX)
### 2.5. Penanda Status Entri

---

## 3. Changelog — Rilis Terbaru

### [1.0.0] — YYYY-MM-DD (Rilis Perdana / Initial Release)

#### Ditambahkan (Added)
(Seluruh fitur baru yang diperkenalkan di v1.0.0, dikelompokkan per modul M.1 s.d M.10)

#### Keamanan (Security)
(Seluruh fitur dan mekanisme keamanan yang diterapkan)

#### Infrastruktur (Infrastructure)
(Perubahan arsitektur, database, deployment, dan konfigurasi lingkungan)

#### Dokumentasi (Documentation)
(Daftar dokumen SDLC yang disusun sebagai bagian dari rilis)

#### Batasan yang Diketahui (Known Limitations)
(Fitur yang sengaja dibatasi atau out-of-scope pada rilis ini)

#### Masalah yang Diketahui (Known Issues)
(Bug atau keterbatasan teknis yang teridentifikasi dan belum diperbaiki)

---

## 4. Rilis yang Direncanakan (Upcoming Releases)

### [1.1.0] — Planned
(Ringkasan fitur yang direncanakan untuk rilis minor berikutnya)

### [2.0.0] — Planned
(Ringkasan fitur yang direncanakan untuk rilis major berikutnya)

---

## 5. Pedoman Penulisan Entri Changelog Baru
### 5.1. Prosedur Penambahan Entri
### 5.2. Template Entri Changelog Baru
### 5.3. Aturan Penomoran dan Urutan
### 5.4. Integrasi dengan Git Workflow dan Conventional Commits

---

## 6. Glosarium

---

## 7. Referensi Dokumen
(Tabel referensi file SDLC yang digunakan)

---
(Keterangan sahnya dokumen)
```

### 4.3. Penjelasan Setiap Bab

| Bab | Konten yang Harus Diisi |
|:----|:------------------------|
| **Bab 1** | Informasi dokumen standar (tujuan, cakupan, posisi SDLC, hubungan input/output, audiens, akronim, dan konvensi format). Struktur bab ini sama dengan dokumen SDLC AbuCom lainnya untuk konsistensi. |
| **Bab 2** | Panduan teknis cara membaca changelog: format SemVer `vMAJOR.MINOR.PATCH`, penjelasan 6 kategori perubahan (Added, Changed, Fixed, Deprecated, Removed, Security), format penulisan setiap entri, dan kode referensi SRS. |
| **Bab 3** | **Inti utama dokumen.** Catatan perubahan kronologis per versi rilis, dimulai dari v1.0.0 (rilis perdana). Setiap entri harus mencantumkan kode referensi SRS-F-XXX jika ada, deskripsi ringkas, dan modul terkait. |
| **Bab 4** | Ringkasan rilis yang direncanakan berdasarkan roadmap di Release Notes (R-01 Bab 15), termasuk v1.1.0 (GUI, WhatsApp API) dan v2.0.0 (Mobile App, QRIS). |
| **Bab 5** | Panduan prosedural untuk tim pengembang tentang cara menambahkan entri changelog baru pada rilis berikutnya. Termasuk template, aturan penomoran, dan integrasi dengan Git Workflow Conventional Commits. |
| **Bab 6** | Glosarium istilah teknis spesifik yang digunakan dalam dokumen ini. |
| **Bab 7** | Tabel referensi file SDLC yang digunakan dalam penyusunan dokumen. |

---

## 5. Instruksi Detail Tahapan Implementasi

### Fase A — Persiapan dan Pembacaan File Referensi

> **PERINGATAN:** Jangan menulis satu pun baris konten dokumen changelog sebelum SELURUH file referensi di bawah ini selesai dibaca dan dirangkum. Setiap file harus dibaca secara menyeluruh tanpa ada bagian yang dilewati.

- [ ] **A.1.** Baca file `docs/sdlc/06_deployment/03_release_notes.md` (R-01) secara menyeluruh dari baris pertama hingga baris terakhir.
  - [ ] A.1.1. Catat semua fitur baru dari Bab 4 (Modul M.1 s.d M.10, beserta kode SRS-F-001 s.d SRS-F-040 dan SRS-F-ADD-01 s.d ADD-05).
  - [ ] A.1.2. Catat semua fitur keamanan dari Bab 5 (bcrypt, JWT, RBAC, Fernet, AES-256, audit trail, fraud detection).
  - [ ] A.1.3. Catat semua bug fixes dan peningkatan dari Bab 6 (termasuk DEF-COMPAT-001, DEF-PERF-001).
  - [ ] A.1.4. Catat semua known limitations dari Bab 7 (CLI-only, manual PPOB, FP constraint, WhatsApp manual).
  - [ ] A.1.5. Catat semua known issues dari Bab 8 (mojibake CMD, latensi laporan L/R).
  - [ ] A.1.6. Catat konfigurasi default rilis dari Bab 10 (parameter database, keamanan, operasional, runtime config).
  - [ ] A.1.7. Catat hasil QA testing dari Bab 11 (unit test, integration test, UAT, exit criteria).
  - [ ] A.1.8. Catat arsitektur deployment dari Bab 12 (diagram, matriks komponen, topologi LAN).
  - [ ] A.1.9. Catat roadmap rilis selanjutnya dari Bab 15 (v1.1.0, v2.0.0).
  - [ ] A.1.10. Catat versi dependencies dari Bab 3.2.3 (requirements.txt locked versions).
  - [ ] A.1.11. Catat informasi tim pengembang dari Bab 14.

- [ ] **A.2.** Baca file `docs/sdlc/07_maintenance/01_maintenance_guide.md` (R-02) secara menyeluruh.
  - [ ] A.2.1. Catat daftar 10 modul fungsional aktif dari Bab 2.3.
  - [ ] A.2.2. Catat daftar 28 tabel database dari Bab 2.4.
  - [ ] A.2.3. Catat daftar pustaka dependensi dari Bab 2.5.
  - [ ] A.2.4. Catat kategori pemeliharaan dari Bab 3 (korektif, preventif, adaptif, perfektif, darurat).

- [ ] **A.3.** Baca file `docs/sdlc/04_implementation/04_git_workflow.md` (R-03) secara menyeluruh.
  - [ ] A.3.1. Catat format Conventional Commits dari Bab 5 (tipe commit: feat, fix, docs, chore, test, refactor, style, perf, revert, ci, build).
  - [ ] A.3.2. Catat daftar 14 scope commit valid dari Bab 5.3.
  - [ ] A.3.3. Catat standar Semantic Versioning dari Bab 9 (MAJOR, MINOR, PATCH).
  - [ ] A.3.4. Catat prosedur tagging rilis dari Bab 9.3-9.4.

- [ ] **A.4.** Baca file `docs/sdlc/01_planning/01_project_charter.md` (R-04) secara menyeluruh.
  - [ ] A.4.1. Catat nama proyek, deskripsi, dan versi dari Bab 1.
  - [ ] A.4.2. Catat susunan tim pengembang dari Bab 7.1.
  - [ ] A.4.3. Catat timeline milestone dari Bab 11.
  - [ ] A.4.4. Catat informasi sponsor dari Bab 1.3.

- [ ] **A.5.** Baca file `docs/sdlc/02_analysis/02_software_requirements.md` (R-05) secara menyeluruh.
  - [ ] A.5.1. Catat seluruh kode kebutuhan fungsional (SRS-F-001 s.d SRS-F-040) beserta deskripsi ringkasnya.
  - [ ] A.5.2. Catat seluruh kebutuhan non-fungsional.

- [ ] **A.6.** Baca file `docs/sdlc/03_design/01_database_schema.sql` (R-06).
  - [ ] A.6.1. Catat daftar nama semua tabel yang didefinisikan (CREATE TABLE).
  - [ ] A.6.2. Catat jumlah total tabel dan engine yang digunakan (InnoDB).

- [ ] **A.7.** Baca file `docs/sdlc/03_design/03_system_architecture.md` (R-07).
  - [ ] A.7.1. Catat arsitektur deployment dan topologi jaringan.
  - [ ] A.7.2. Catat spesifikasi hardware server dan klien.

- [ ] **A.8.** Baca file `docs/sdlc/03_design/06_security_design.md` (R-08).
  - [ ] A.8.1. Catat seluruh mekanisme keamanan yang diimplementasikan.
  - [ ] A.8.2. Catat kode error keamanan (ERR-AUTH-XXX, ERR-DB-XXX, dll).

- [ ] **A.9.** Baca file `docs/sdlc/04_implementation/01_coding_standard.md` (R-09).
  - [ ] A.9.1. Catat standar paradigma FP murni dan presisi Decimal.

- [ ] **A.10.** Baca file `docs/sdlc/04_implementation/03_module_structure.md` (R-10).
  - [ ] A.10.1. Catat peta modul dan file mapping (modul-to-file).

- [ ] **A.11.** Baca file `docs/sdlc/05_testing/01_test_plan.md` (R-11).
  - [ ] A.11.1. Catat strategi pengujian dan exit criteria.

- [ ] **A.12.** Baca file `docs/sdlc/06_deployment/01_deployment_guide.md` (R-12).
  - [ ] A.12.1. Catat prosedur deployment dan konfigurasi produksi.

- [ ] **A.13.** Baca file `docs/sdlc/01_planning/04_tech_stack_decision.md` (R-13).
  - [ ] A.13.1. Catat keputusan teknologi (Python 3.14.2+, MySQL 8.4, FP murni, locked deps).

- [ ] **A.14.** Baca file `docs/sdlc/05_testing/04_bug_report_template.md` (R-14).
  - [ ] A.14.1. Catat format severity dan priority level.

---

### Fase B — Perangkuman dan Pemilahan Data

> **PERINGATAN:** Pada fase ini, hanya rangkum dan pilah data yang **SPESIFIK dibutuhkan** oleh dokumen Changelog. Jangan memasukkan data yang tidak relevan (misalnya: SOP harian operasional toko, prosedur shift handover kasir, detail prosedur penggajian — itu milik dokumen lain).

- [ ] **B.1.** Dari data R-01 (Release Notes), kelompokkan seluruh fitur baru v1.0.0 ke dalam kategori **"Ditambahkan (Added)"** dan organisasikan per modul (M.1 s.d M.10).
  - [ ] B.1.1. Setiap entri fitur harus mencantumkan kode SRS-F-XXX jika tersedia.
  - [ ] B.1.2. Tulis deskripsi ringkas (1-2 kalimat) per fitur, bukan paragraf panjang.

- [ ] **B.2.** Dari data R-01 dan R-08, kelompokkan seluruh fitur keamanan ke dalam kategori **"Keamanan (Security)"**.
  - [ ] B.2.1. Termasuk: bcrypt cost 12, JWT HS256 8 jam, RBAC 8 peran, Fernet CRM, AES-256 backup, audit trail JSON, fraud detection, rate limiting, UU PDP compliance.

- [ ] **B.3.** Dari data R-01 Bab 6, kelompokkan perbaikan bug dan peningkatan ke dalam kategori **"Diperbaiki (Fixed)"** dan **"Ditingkatkan (Improved)"**.
  - [ ] B.3.1. Termasuk: composite index query L/R, ANSI Rich CLI dashboard.

- [ ] **B.4.** Dari data R-06 dan R-07, kelompokkan seluruh perubahan infrastruktur ke dalam kategori **"Infrastruktur (Infrastructure)"**.
  - [ ] B.4.1. Termasuk: 28 tabel InnoDB, topologi LAN offline, dual-OS deployment, hardware specs, connection pooling.

- [ ] **B.5.** Dari data semua file referensi SDLC, buat daftar seluruh dokumen yang disusun sebagai bagian dari rilis v1.0.0 ke dalam kategori **"Dokumentasi (Documentation)"**.
  - [ ] B.5.1. Daftar semua 28+ dokumen SDLC lengkap dengan path dan versinya.

- [ ] **B.6.** Dari data R-01 Bab 7, salin seluruh known limitations ke dalam kategori **"Batasan yang Diketahui (Known Limitations)"**.

- [ ] **B.7.** Dari data R-01 Bab 8, salin seluruh known issues ke dalam kategori **"Masalah yang Diketahui (Known Issues)"**.
  - [ ] B.7.1. Termasuk: DEF-COMPAT-001 (mojibake CMD) dan DEF-PERF-001 (latensi L/R >50k record).

- [ ] **B.8.** Dari data R-01 Bab 15, rangkum rencana rilis v1.1.0 dan v2.0.0 untuk bagian **"Rilis yang Direncanakan"**.

- [ ] **B.9.** Dari data R-03 (Git Workflow), rangkum prosedur penambahan entri changelog baru untuk bagian **"Pedoman Penulisan Entri Changelog Baru"**.
  - [ ] B.9.1. Integrasikan format Conventional Commits ke template entri changelog.
  - [ ] B.9.2. Definisikan prosedur: kapan entri ditambahkan, siapa yang menambahkan, dan bagaimana format penomorannya.

- [ ] **B.10.** Verifikasi bahwa tidak ada data yang terlewat dari seluruh file referensi.
  - [ ] B.10.1. Bandingkan daftar fitur di changelog dengan daftar SRS-F-001 s.d SRS-F-040 — pastikan semua tercakup.
  - [ ] B.10.2. Bandingkan daftar fitur keamanan di changelog dengan Security Design (R-08) — pastikan semua tercakup.

---

### Fase C — Penulisan Dokumen Changelog

> **PERINGATAN:** Tulis dokumen secara LENGKAP dari awal hingga akhir. DILARANG memotong, meringkas, atau menyingkat konten dengan kalimat seperti "dan seterusnya", "dst.", "sisanya sama", atau "(lanjutan)". Setiap bab, sub-bab, tabel, dan entri harus ditulis secara utuh tanpa terpotong (non-truncated).

- [ ] **C.1.** Tulis **Front Matter YAML** sesuai format standar dokumen AbuCom:
  ```yaml
  ---
  dokumen    : Changelog
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [TANGGAL_HARI_INI]
  status     : Draft
  penyusun   : Senior Configuration Manager & Release Documentation Specialist
  ---
  ```

- [ ] **C.2.** Tulis **Judul Dokumen**: `# Changelog — AbuCom`

- [ ] **C.3.** Tulis **Riwayat Perubahan Dokumen** dalam tabel standar AbuCom (Versi, Tanggal, Deskripsi Perubahan, Oleh).

- [ ] **C.4.** Tulis **Bab 1 — Informasi Dokumen** secara lengkap:
  - [ ] C.4.1. **Bab 1.1 Tujuan Dokumen:** Jelaskan tujuan changelog sebagai catatan perubahan kronologis resmi setiap rilis AbuCom.
  - [ ] C.4.2. **Bab 1.2 Cakupan Dokumen:** Jelaskan bahwa dokumen mencakup seluruh rilis software (v1.0.0, v1.1.0, v2.0.0, dst) dan setiap entri perubahan di dalamnya.
  - [ ] C.4.3. **Bab 1.3 Posisi Dokumen dalam SDLC:** Gambarkan posisi sebagai Deliverable ke-2 pada Fase 07 — Maintenance. Gunakan diagram teks ASCII.
  - [ ] C.4.4. **Bab 1.4 Hubungan dengan Dokumen SDLC:** Jelaskan dokumen input (Release Notes, Git Workflow, SRS, Maintenance Guide) dan dokumen output (Patch Release Notes, Audit Log Rilis, Roadmap).
  - [ ] C.4.5. **Bab 1.5 Audiens Target:** Pemilik Usaha, Tim Pengembang AI, System Administrator, Kepala Percetakan.
  - [ ] C.4.6. **Bab 1.6 Definisi, Akronim, dan Singkatan:** Tulis daftar akronim yang digunakan spesifik dalam dokumen ini (SemVer, Conventional Commits, changelog, SDLC, SRS, BOM, HPP, RBAC, JWT, LAN, CLI, dll).
  - [ ] C.4.7. **Bab 1.7 Konvensi Format Entri Changelog:** Jelaskan format standar penulisan entri, termasuk simbol penanda, kode referensi, dan contoh visual.

- [ ] **C.5.** Tulis **Bab 2 — Panduan Pembacaan Changelog** secara lengkap:
  - [ ] C.5.1. **Bab 2.1 Format Versi (SemVer):** Jelaskan format `vMAJOR.MINOR.PATCH` dan kapan masing-masing digit berubah.
  - [ ] C.5.2. **Bab 2.2 Kategori Perubahan:** Jelaskan 6+ kategori standar:
    - `Ditambahkan (Added)` — Fitur baru.
    - `Diubah (Changed)` — Perubahan pada fitur yang sudah ada.
    - `Diperbaiki (Fixed)` — Perbaikan bug.
    - `Dihapus (Removed)` — Fitur atau kode yang dihapus.
    - `Tidak Digunakan Lagi (Deprecated)` — Fitur yang akan dihapus di rilis mendatang.
    - `Keamanan (Security)` — Perbaikan atau penambahan keamanan.
    - `Infrastruktur (Infrastructure)` — Perubahan arsitektur, deployment, atau konfigurasi.
    - `Dokumentasi (Documentation)` — Perubahan dokumen SDLC.
  - [ ] C.5.3. **Bab 2.3 Format Entri Changelog:** Berikan contoh format standar entri:
    ```
    - **[SRS-F-001]** Ditambahkan pencatatan transaksi penjualan multi-divisi untuk 5 kategori usaha. *(Modul M.1)*
    ```
  - [ ] C.5.4. **Bab 2.4 Kode Referensi Terkait:** Jelaskan keterkaitan entri changelog dengan kode SRS-F-XXX, DEF-XXX, dan commit hash Git.
  - [ ] C.5.5. **Bab 2.5 Penanda Status Entri:** Jelaskan penanda jika ada data kosong, yaitu menggunakan `[DATA BELUM TERSEDIA]` dengan warna/format yang mudah dicari.

- [ ] **C.6.** Tulis **Bab 3 — Changelog Rilis Terbaru** secara lengkap dan mendetail:

  - [ ] C.6.1. Tulis header rilis: `### [1.0.0] — [TANGGAL_RILIS_ESTIMASI]` (ambil dari R-01 Bab 2.2, yaitu `2027-05-20 — Estimasi`).
  - [ ] C.6.2. Tulis ringkasan rilis 1 paragraf (Major Release, rilis perdana, migrasi dari Excel ke CLI).

  - [ ] C.6.3. Tulis sub-kategori **"Ditambahkan (Added)"** dikelompokkan per modul:
    - [ ] C.6.3.1. **M.1 — Manajemen Transaksi & Kebijakan Harga:** Tulis semua entri SRS-F-001 s.d SRS-F-006.
    - [ ] C.6.3.2. **M.2 — Manajemen Inventaris, BOM & Stock Opname:** Tulis semua entri SRS-F-007 s.d SRS-F-014, SRS-F-039, SRS-F-040.
    - [ ] C.6.3.3. **M.3 — Layanan Keuangan Digital, PPOB & Jasa Service:** Tulis semua entri SRS-F-015 s.d SRS-F-017.
    - [ ] C.6.3.4. **M.4 — Manajemen SDM, Penggajian & Poin Karyawan:** Tulis semua entri SRS-F-018 s.d SRS-F-021.
    - [ ] C.6.3.5. **M.5 — Sistem Manajemen Antrian & Pelacakan Desain:** Tulis semua entri SRS-F-022 s.d SRS-F-024.
    - [ ] C.6.3.6. **M.6 — Administrasi Pinjaman, Aset & Pengeluaran:** Tulis semua entri SRS-F-025 s.d SRS-F-029.
    - [ ] C.6.3.7. **M.7 — Keamanan, Audit Trail & Hak Akses:** Tulis semua entri SRS-F-030 s.d SRS-F-035.
    - [ ] C.6.3.8. **M.8 — Pembatalan, Retur & CRM:** Tulis entri SRS-F-036.
    - [ ] C.6.3.9. **M.9 — Skalabilitas Multi-Cabang:** Tulis entri SRS-F-037.
    - [ ] C.6.3.10. **M.10 — Konfigurasi Sistem Runtime:** Tulis entri SRS-F-038.
    - [ ] C.6.3.11. **Kebutuhan Teknis Tambahan:** Tulis semua entri SRS-F-ADD-01 s.d SRS-F-ADD-05.

  - [ ] C.6.4. Tulis sub-kategori **"Keamanan (Security)":**
    - [ ] C.6.4.1. Entri: Otentikasi bcrypt Blowfish cost factor 12 dengan salt 16 bytes.
    - [ ] C.6.4.2. Entri: Sesi stateless JWT HS256 lifetime 8 jam (28.800 detik).
    - [ ] C.6.4.3. Entri: Otorisasi RBAC 8 peran (pemilik, kepala_percetakan, kasir, desainer, produksi_cetak, gudang, pramuniaga, fotocopy_print).
    - [ ] C.6.4.4. Entri: Enkripsi simetris Fernet CRM WhatsApp pelanggan (UU PDP No. 27/2022).
    - [ ] C.6.4.5. Entri: Backup database terenkripsi AES-256 ZIP via cron harian 21:00 WIB.
    - [ ] C.6.4.6. Entri: Audit trail kronologis format JSON (old_value, new_value).
    - [ ] C.6.4.7. Entri: Fraud detection sederhana (brute-force >5x, pembatalan DP >3x, selisih kas >Rp 10.000).
    - [ ] C.6.4.8. Entri: Rate limiting lockout 5x gagal login selama 10 menit.
    - [ ] C.6.4.9. Entri: OS hardening (ufw firewall, SSH PermitRootLogin no, chmod 700 backup, Windows AutoPlay disabled).
    - [ ] C.6.4.10. Entri: Proteksi eskalasi transaksi sensitif (retur, pengeluaran ≥Rp 500.000) wajib sandi pemilik fisik.

  - [ ] C.6.5. Tulis sub-kategori **"Infrastruktur (Infrastructure)":**
    - [ ] C.6.5.1. Entri: Database MySQL 8.4 LTS InnoDB 28 tabel, isolation level REPEATABLE READ.
    - [ ] C.6.5.2. Entri: Topologi LAN offline star topology (Mini PC Server Debian 12, PC Kasir Windows 11, Switch Hub Gigabit, Router MikroTik).
    - [ ] C.6.5.3. Entri: Connection pool size 5 dengan auto-retry 3x exponential backoff.
    - [ ] C.6.5.4. Entri: Arsitektur data Multi-Branch Ready (kolom `cabang_id` di setiap tabel).
    - [ ] C.6.5.5. Entri: Runtime Python 3.14.2+ paradigma Functional Programming murni.
    - [ ] C.6.5.6. Entri: 7 pustaka dependensi terkunci (mysql-connector-python, python-dotenv, bcrypt, pyjwt, cryptography, rich, tabulate).
    - [ ] C.6.5.7. Entri: Sistem konfigurasi dinamis via tabel `system_configs` (13 parameter runtime).
    - [ ] C.6.5.8. Entri: Dual-OS deployment support (Linux Debian 12 Server + Windows 11 Klien Kasir).

  - [ ] C.6.6. Tulis sub-kategori **"Dokumentasi (Documentation)":**
    - [ ] C.6.6.1. Daftarkan seluruh dokumen SDLC yang disusun untuk rilis v1.0.0, termasuk:
      - Fase 01 Planning: Project Charter, Feasibility Study, Stakeholder Register, Tech Stack Decision, Innovation Proposal.
      - Fase 02 Analysis: Business Requirements, Software Requirements, Use Case Diagram, Workflow Diagram, Data Dictionary, Access Control Matrix.
      - Fase 03 Design: Database Schema, ERD Database, System Architecture, CLI Interaction Flow, BOM HPP Design, Security Design.
      - Fase 04 Implementation: Coding Standard, Environment Setup, Module Structure, Git Workflow.
      - Fase 05 Testing: Test Plan, Test Cases, UAT Script, Bug Report Template.
      - Fase 06 Deployment: Deployment Guide, Environment Config, Release Notes.
      - Fase 07 Maintenance: Maintenance Guide, Changelog (dokumen ini).

  - [ ] C.6.7. Tulis sub-kategori **"Batasan yang Diketahui (Known Limitations)":**
    - [ ] C.6.7.1. CLI-only interface (tanpa GUI, web, atau mobile).
    - [ ] C.6.7.2. Administrasi keuangan digital bersifat manual.
    - [ ] C.6.7.3. FP constraint (tanpa class OOP di logic bisnis).
    - [ ] C.6.7.4. Runtime kritis Python 3.14.2+ wajib.
    - [ ] C.6.7.5. WhatsApp Web manual link (tanpa API berbayar).
    - [ ] C.6.7.6. Payment gateway manual (tanpa QRIS API).
    - [ ] C.6.7.7. Out-of-scope: sinkronisasi marketplace, mobile app, GUI.

  - [ ] C.6.8. Tulis sub-kategori **"Masalah yang Diketahui (Known Issues)"** dalam format tabel:
    - [ ] C.6.8.1. DEF-COMPAT-001: Mojibake rendering box-drawing pada CMD cp1252 lawas.
    - [ ] C.6.8.2. DEF-PERF-001: Latensi laporan L/R semester >2 detik pada >50.000 record.

- [ ] **C.7.** Tulis **Bab 4 — Rilis yang Direncanakan** berdasarkan roadmap R-01 Bab 15:
  - [ ] C.7.1. **[1.1.0] — Planned:** GUI Tkinter/PyQt, WhatsApp API Gateway, Analisis Re-Order ML.
  - [ ] C.7.2. **[2.0.0] — Planned:** Mobile App Admin, QRIS Payment Gateway, Otomatisasi PPOB API.

- [ ] **C.8.** Tulis **Bab 5 — Pedoman Penulisan Entri Changelog Baru:**
  - [ ] C.8.1. Prosedur kapan menambahkan entri (setiap kali branch fitur di-merge ke main).
  - [ ] C.8.2. Template format entri baru yang wajib diikuti.
  - [ ] C.8.3. Aturan penomoran versi mengikuti SemVer.
  - [ ] C.8.4. Integrasi dengan Conventional Commits dan Git Workflow (referensi R-03).
  - [ ] C.8.5. Siapa yang bertanggung jawab menambahkan entri (Junior Programmer / STK-000).

- [ ] **C.9.** Tulis **Bab 6 — Glosarium** dengan minimal 15 istilah teknis yang relevan spesifik untuk changelog.

- [ ] **C.10.** Tulis **Bab 7 — Referensi Dokumen** dalam format tabel standar AbuCom:
  - [ ] C.10.1. Cantumkan seluruh 14 file referensi (R-01 s.d R-14) dengan kolom: Kode Ref, Nama Dokumen, Path Relatif, Prioritas, Peran/Hubungan.

- [ ] **C.11.** Tulis kalimat penutup sahnya dokumen di baris terakhir:
  ```
  *Dokumen Changelog AbuCom ini dinyatakan sah dan berlaku sebagai catatan perubahan resmi seluruh rilis sistem.*
  ```

---

### Fase D — Penandaan Data Kosong

- [ ] **D.1.** Periksa seluruh isi dokumen yang sudah ditulis.
- [ ] **D.2.** Jika ada data yang **tidak ditemukan** di dalam file referensi manapun, tandai dengan format berikut:
  ```
  [DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha]
  ```
- [ ] **D.3.** Contoh data yang kemungkinan perlu ditandai:
  - Tanggal rilis aktual v1.0.0 (saat ini masih estimasi 2027-05-20).
  - Commit hash Git rilis pertama (belum tersedia karena kode belum dikonstruksi).
  - Nomor tiket bug report aktual (belum ada insiden produksi karena belum Go-Live).
- [ ] **D.4.** Pastikan setiap penanda `[DATA BELUM TERSEDIA]` mudah dicari dengan fitur Ctrl+F agar bisa diisi secara manual di kemudian hari.

---

### Fase E — Verifikasi Kualitas Akhir

- [ ] **E.1.** Verifikasi bahwa **seluruh bab** dalam kerangka (Bab 1 s.d Bab 7) sudah ditulis lengkap tanpa ada bab yang kosong atau terpotong.
- [ ] **E.2.** Verifikasi bahwa **seluruh 40 fitur fungsional** (SRS-F-001 s.d SRS-F-040) sudah tercantum di bagian "Ditambahkan (Added)".
- [ ] **E.3.** Verifikasi bahwa **seluruh 5 fitur tambahan** (SRS-F-ADD-01 s.d SRS-F-ADD-05) sudah tercantum.
- [ ] **E.4.** Verifikasi bahwa **seluruh fitur keamanan** (minimal 10 entri) sudah tercantum di bagian "Keamanan (Security)".
- [ ] **E.5.** Verifikasi bahwa **seluruh 28+ dokumen SDLC** sudah terdaftar di bagian "Dokumentasi".
- [ ] **E.6.** Verifikasi bahwa **seluruh known limitations** dan **known issues** sudah tercantum.
- [ ] **E.7.** Verifikasi bahwa format penulisan bahasa Indonesia natural, tidak ambigu, tidak membingungkan, dan konsisten di seluruh dokumen.
- [ ] **E.8.** Verifikasi bahwa tidak ada campuran bahasa Inggris-Indonesia yang tidak perlu (kecuali istilah teknis standar yang memang tidak punya padanan Indonesia).
- [ ] **E.9.** Verifikasi bahwa tabel referensi di Bab 7 sudah mencantumkan seluruh 14 file referensi.
- [ ] **E.10.** Verifikasi bahwa front matter YAML, heading markdown, dan formatting konsisten.
- [ ] **E.11.** Verifikasi bahwa dokumen ini layak menjadi referensi untuk:
  - Release Notes versi berikutnya (v1.1.0, v2.0.0).
  - Audit kualitas rilis.
  - Debugging dan rollback jika terjadi masalah di produksi.
  - Perencanaan roadmap.

---

### Fase F — Penulisan ke Target File

- [ ] **F.1.** Tuangkan seluruh hasil dokumen Changelog yang sudah selesai ke dalam target file:
  ```
  docs/sdlc/07_maintenance/02_changelog.md
  ```
- [ ] **F.2.** Pastikan file ditulis secara **OVERWRITE penuh** (bukan append) karena file target saat ini masih kosong.
- [ ] **F.3.** Pastikan file yang ditulis **TIDAK TERPOTONG** (non-truncated). Seluruh konten dari Bab 1 hingga baris terakhir harus tertulis utuh.
- [ ] **F.4.** Verifikasi akhir bahwa file sudah tertulis dengan membaca ulang 10 baris pertama dan 10 baris terakhir file untuk memastikan integritas.

---

## 6. Instruksi Tambahan Khusus Changelog

### 6.1. Prinsip Penulisan Changelog yang Baik
Berikut adalah prinsip-prinsip yang **WAJIB** dipatuhi dalam penulisan dokumen ini, sesuai dengan kaidah standar industri changelog:

1. **Untuk Manusia, Bukan Mesin:** Changelog ditulis agar mudah dibaca oleh manusia (pemilik usaha, tim pengembang, sysadmin), bukan untuk dikonsumsi oleh parser otomatis.
2. **Urutan Kronologis Terbalik (Newest First):** Rilis terbaru selalu ditempatkan paling atas, rilis lama di bawahnya. Versi `[1.0.0]` saat ini ada di paling atas karena baru satu rilis.
3. **Satu Entri Per Perubahan:** Setiap perubahan tunggal diwakili oleh satu bullet point. Jangan menggabungkan beberapa perubahan berbeda ke dalam satu entri.
4. **Referensi Kode SRS:** Setiap entri fitur fungsional WAJIB mencantumkan kode referensi SRS-F-XXX di depan deskripsi agar mudah dilacak ke spesifikasi asli.
5. **Pengelompokan per Modul:** Pada bagian "Ditambahkan (Added)", entri dikelompokkan per modul (M.1 s.d M.10) untuk memudahkan pembaca menemukan perubahan spesifik per area fungsional.
6. **Tanggal Menggunakan Format ISO 8601:** Format tanggal yang digunakan adalah `YYYY-MM-DD` (contoh: `2027-05-20`).

### 6.2. Ciri Khas Dokumen Changelog vs Release Notes
Perhatikan perbedaan berikut agar tidak terjadi duplikasi konten yang berlebihan:

| Aspek | Changelog | Release Notes |
|:------|:----------|:--------------|
| **Tujuan** | Catatan perubahan teknis kronologis per versi | Ringkasan eksekutif rilis untuk stakeholder |
| **Audiens Utama** | Developer, SysAdmin, QA | Semua stakeholder (termasuk non-teknis) |
| **Level Detail** | Ringkas (1-2 kalimat per entri) | Deskriptif (paragraf + tabel + diagram) |
| **Format** | Daftar bullet terstruktur per kategori | Bab-bab naratif lengkap |
| **Persistensi** | Akumulatif (semua versi dalam 1 file) | Per-rilis (1 file per major release) |
| **Update** | Diupdate setiap kali ada merge ke main | Diupdate setiap ada rilis formal |

### 6.3. Handling Data Duplikat dengan Release Notes
Meskipun banyak data yang sama antara Changelog dan Release Notes, tulis entri changelog dengan gaya ringkas dan teknis. **JANGAN** menyalin paragraf panjang dari Release Notes. Contoh:

- ❌ **SALAH (terlalu panjang, gaya Release Notes):**
  > Sistem mendukung pencatatan transaksi penjualan multi-divisi untuk 5 kategori usaha: produk percetakan, retail ATK, e-wallet jasa keuangan, pulsa PPOB, dan jasa perbaikan teknis melalui antarmuka CLI kasir teks cepat.

- ✅ **BENAR (ringkas, gaya Changelog):**
  > **[SRS-F-001]** Ditambahkan pencatatan transaksi penjualan multi-divisi CLI untuk 5 kategori usaha. *(Modul M.1)*

---

## 7. Kriteria Keberhasilan (Definition of Done)

Issue ini dianggap selesai (**DONE**) jika dan hanya jika seluruh syarat berikut terpenuhi:

- [ ] Seluruh 14 file referensi (R-01 s.d R-14) sudah dibaca dan dirangkum.
- [ ] Seluruh bab (Bab 1 s.d Bab 7) sudah ditulis lengkap tanpa ada yang kosong.
- [ ] Seluruh 40 kebutuhan fungsional (SRS-F-001 s.d SRS-F-040) tercantum di entri changelog.
- [ ] Seluruh 5 kebutuhan tambahan (SRS-F-ADD-01 s.d ADD-05) tercantum.
- [ ] Seluruh fitur keamanan (minimal 10 entri) tercantum.
- [ ] Seluruh 28+ dokumen SDLC tercantum di bagian dokumentasi.
- [ ] Known Limitations dan Known Issues tercantum lengkap.
- [ ] Roadmap rilis v1.1.0 dan v2.0.0 tercantum.
- [ ] Pedoman penulisan entri changelog baru tersedia dan jelas.
- [ ] Data kosong ditandai dengan `[DATA BELUM TERSEDIA]`.
- [ ] Tabel referensi (R-01 s.d R-14) tercantum di Bab 7.
- [ ] File telah ditulis ke `docs/sdlc/07_maintenance/02_changelog.md` secara utuh (non-truncated).
- [ ] Bahasa Indonesia natural, konsisten, dan tidak ambigu di seluruh dokumen.

---

*Issue ini disusun oleh Antigravity sebagai perencanaan low-level untuk dieksekusi oleh junior programmer atau LLM AI model executor.*
