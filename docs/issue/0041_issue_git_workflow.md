# Pembuatan Dokumen Git Workflow

---

| Atribut       | Detail                                                                 |
|:---           |:---                                                                    |
| **Judul**     | Pembuatan dan Penyusunan Dokumen Git Workflow                          |
| **Dokumen Utama** | Git Workflow                                                       |
| **Target File** | `docs/sdlc/04_implementation/04_git_workflow.md`                    |
| **Fase SDLC** | Fase 04 — Implementation (Konstruksi)                                  |
| **Prioritas** | High                                                                   |
| **Status**    | Open                                                                   |
| **Tanggal**   | 2026-05-26                                                             |

---

## 1. Konteks dan Latar Belakang

Dokumen **Git Workflow** merupakan deliverable ke-4 pada **Fase 04 — Implementation** dalam siklus SDLC proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**. Dokumen ini bertujuan untuk mendefinisikan secara formal, rinci, dan mengikat seluruh standar, prosedur, dan kebijakan pengelolaan version control Git yang akan digunakan oleh seluruh tim pengembang (Junior Programmer dan 6 Model AI) selama proses konstruksi kode program AbuCom.

Dokumen ini harus menjadi panduan utama yang mengatur bagaimana kode program dikelola, dibranching, di-commit, di-review, di-merge, dan di-tag secara terstruktur agar kualitas dan integritas codebase terjaga.

### 1.1. Posisi Dokumen dalam SDLC

```
+-----------------------------------+
|    Fase 04: Coding Standard       |
|       (Deliverable ke-1)          |
+-----------------------------------+
                  |
                  v
+-----------------------------------+
|    Fase 04: Environment Setup     |
|       (Deliverable ke-2)          |
+-----------------------------------+
                  |
                  v
+-----------------------------------+
|    Fase 04: Module Structure      |
|       (Deliverable ke-3)          |
+-----------------------------------+
                  |
                  v
+===================================+
|    Fase 04: Git Workflow [INI]    |  <-- POSISI DELIVERABLE INI
|       (Deliverable ke-4)          |
+===================================+
                  |
                  v
+-----------------------------------+
|    Fase 04: Konstruksi Kode       |
|    Aktual per Modul (M.1 - M.10) |
+-----------------------------------+
```

---

## 2. Persona Pelaksana

| Atribut               | Detail                                                                 |
|:---                   |:---                                                                    |
| **Persona**           | **Senior DevOps Engineer & Git Workflow Architect**                     |
| **Justifikasi**       | Persona ini dipilih karena memiliki otoritas dan keahlian paling relevan untuk mendefinisikan standar version control, strategi branching, kebijakan merge/conflict resolution, konvensi commit, dan prosedur release management. Persona ini juga memiliki pemahaman mendalam tentang kolaborasi tim campuran (manusia + AI) yang menjadi ciri khas proyek AbuCom. |
| **Tone Penulisan**    | Formal, instruktif, deterministik, dan menggunakan bahasa Indonesia yang natural, tidak ambigu, serta mudah dipahami oleh Junior Programmer atau AI model yang lebih murah. |

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **WAJIB** dibaca dan dirangkum sebagai dasar utama penyusunan dokumen Git Workflow. File-file ini dipilih berdasarkan relevansi kontennya terhadap substansi dokumen Git Workflow.

| No | Kode Ref | Nama Dokumen Referensi                    | Path Relatif File                                        | Prioritas    | Alasan Pemilihan / Relevansi Spesifik                                                                 |
|:---:|:---:     |:---                                        |:---                                                      |:---:         |:---                                                                                                    |
| 1  | R-01     | **Coding Standard**                        | `docs/sdlc/04_implementation/01_coding_standard.md`      | **PRIMER**   | Berisi Bab 15 "Standar Version Control (Git)" yang mendefinisikan strategi branching, konvensi penamaan branch, konvensi commit message, aturan `.gitignore`, dan aturan code review. Ini adalah sumber data utama yang harus dielaborasi dan diperluas secara menyeluruh. |
| 2  | R-02     | **Environment Setup**                      | `docs/sdlc/04_implementation/02_environment_setup.md`    | **PRIMER**   | Berisi Bab 9 "Setup Version Control (Git)" yang mendefinisikan instalasi Git, konfigurasi Git identity, inisialisasi repository, strategi branching, dan konvensi commit message. Juga berisi konfigurasi `.gitignore` di Bab 8.5. |
| 3  | R-03     | **Module Structure**                       | `docs/sdlc/04_implementation/03_module_structure.md`     | **SEKUNDER** | Berisi pemetaan 10 modul fungsional ke file-file spesifik, yang menjadi dasar untuk mendefinisikan strategi branch per modul dan aturan scope commit. |
| 4  | R-04     | **Tech Stack Decision**                    | `docs/sdlc/01_planning/04_tech_stack_decision.md`        | **SEKUNDER** | Berisi keputusan tentang platform development, tim pengembang AI (6 model + 1 Junior Programmer), dan kebutuhan kolaborasi lintas platform yang berimplikasi pada workflow Git. |
| 5  | R-05     | **System Architecture**                    | `docs/sdlc/03_design/03_system_architecture.md`          | **TERSIER**  | Berisi diagram arsitektur 4-layer dan 10 modul fungsional yang menjadi konteks untuk aturan scope branch dan organisasi commit. |
| 6  | R-06     | **Security Design**                        | `docs/sdlc/03_design/06_security_design.md`              | **TERSIER**  | Berisi aturan keamanan yang berimplikasi pada Git workflow (misalnya: `.env` tidak boleh di-commit, audit trail, dan proteksi kredensial). |
| 7  | R-07     | **Narasi Pemilik**                         | `docs/sdlc/narasi.txt`                                  | **TERSIER**  | Berisi konteks bisnis, susunan tim pengembang AI, dan mandat inovasi dari pemilik usaha yang mempengaruhi pola kolaborasi Git. |

> **Catatan**: File `narasi.txt` masih dipilih sebagai referensi karena mengandung informasi tentang susunan tim pengembang (6 model AI + Junior Programmer) yang sangat relevan untuk menentukan pola kolaborasi Git.

---

## 4. Kerangka Struktur Dokumen Utama

Berikut adalah kerangka (outline) struktur dokumen `04_git_workflow.md` yang harus digunakan. Kerangka ini disusun berdasarkan standar praktik industri terbaik untuk dokumen Git Workflow.

```
---
dokumen    : Git Workflow
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [TANGGAL PENGERJAAN]
status     : Draft
penyusun   : Senior DevOps Engineer & Git Workflow Architect
---

# Git Workflow — AbuCom

## Riwayat Perubahan Dokumen
(Tabel: Versi | Tanggal | Perubahan | Oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya (Input & Output)
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan

---

## 2. Prinsip Dasar Pengelolaan Version Control
### 2.1. Filosofi Version Control AbuCom
### 2.2. Aturan Umum Penggunaan Git
### 2.3. Peran dan Tanggung Jawab Tim dalam Git Workflow
   (Memetakan 7 anggota tim: Junior Programmer + 6 Model AI ke peran Git masing-masing)

---

## 3. Konfigurasi Git Awal
### 3.1. Instalasi Git (Windows 11 & Linux Debian 12)
### 3.2. Konfigurasi Git Identity (user.name, user.email)
### 3.3. Konfigurasi Global Git (core.autocrlf, core.editor, default branch)
### 3.4. Inisialisasi Repository Lokal
### 3.5. Konfigurasi File .gitignore (Lengkap)
### 3.6. Konfigurasi File .gitattributes (Line Ending Cross-OS)

---

## 4. Strategi Branching
### 4.1. Model Branching yang Diadopsi (Feature Branching Model)
### 4.2. Diagram Alur Branching (Mermaid)
### 4.3. Daftar Branch dan Fungsinya
   (Tabel: Nama Branch | Tujuan | Siapa yang Membuat | Kebijakan Merge)
   - main (Branch Produksi Stabil)
   - develop (Branch Integrasi Pengembangan) — jika diperlukan
   - feature/<nama-modul> (Branch Fitur per Modul)
   - bugfix/<deskripsi-bug> (Branch Perbaikan Bug)
   - hotfix/<deskripsi-hotfix> (Branch Perbaikan Darurat Produksi)
   - docs/<nama-dokumen> (Branch Dokumentasi)
   - test/<nama-test> (Branch Pengujian)
### 4.4. Konvensi Penamaan Branch
   (Tabel: Tipe | Format | Contoh Benar | Contoh Salah)
### 4.5. Aturan Proteksi Branch (Branch Protection Rules)
### 4.6. Siklus Hidup Branch (Branch Lifecycle)
   (Kapan dibuat, kapan di-merge, kapan dihapus)

---

## 5. Konvensi Commit
### 5.1. Format Commit Message (Conventional Commits)
   (Struktur: <type>(<scope>): <description>)
### 5.2. Daftar Tipe Commit yang Diizinkan
   (Tabel: Tipe | Deskripsi | Contoh)
   - feat, fix, docs, chore, test, refactor, style, perf, ci, build, revert
### 5.3. Aturan Scope Commit
   (Scope berdasarkan modul: transaksi, inventaris, payroll, keamanan, db, cli, dll.)
### 5.4. Aturan Deskripsi Commit
   (Bahasa, panjang karakter, imperative mood)
### 5.5. Aturan Body dan Footer Commit (Opsional)
   (Breaking changes, referensi issue, co-authored-by untuk AI)
### 5.6. Contoh Commit Message Lengkap (Benar vs Salah)
### 5.7. Aturan Atomisitas Commit (Atomic Commits)
   (Satu commit = satu perubahan logis tunggal)

---

## 6. Alur Kerja Pengembangan (Development Workflow)
### 6.1. Diagram Alur Kerja Lengkap (Mermaid — Flowchart)
### 6.2. Langkah-Langkah Detail Alur Kerja
   (Step-by-step: Buat branch → Koding → Commit → Push → Review → Merge)
### 6.3. Alur Kerja untuk Penambahan Fitur Baru (Feature Workflow)
### 6.4. Alur Kerja untuk Perbaikan Bug (Bugfix Workflow)
### 6.5. Alur Kerja untuk Perbaikan Darurat (Hotfix Workflow)
### 6.6. Alur Kerja untuk Pembaruan Dokumentasi (Docs Workflow)

---

## 7. Strategi Merge dan Conflict Resolution
### 7.1. Kebijakan Merge (Merge Policy)
   (Fast-forward vs Merge commit vs Squash merge)
### 7.2. Prosedur Merge Branch Fitur ke Main/Develop
### 7.3. Prosedur Penanganan Merge Conflict
   (Step-by-step resolusi konflik)
### 7.4. Diagram Alur Resolusi Konflik (Mermaid)
### 7.5. Aturan Pencegahan Konflik (Preventive Rules)
   (Sering pull/rebase, scope kecil, komunikasi antar-AI)

---

## 8. Code Review dan Quality Gate
### 8.1. Prosedur Code Review Sebelum Merge
### 8.2. Peran Reviewer dalam Tim AbuCom
   (Gemini 3 Flash sebagai reviewer cepat — sesuai narasi)
### 8.3. Checklist Code Review (Pre-Merge Checklist)
   (Integrasi dengan Checklist Kepatuhan Coding Standard Bab 17)
### 8.4. Kriteria Lulus Quality Gate
   (Unit test pass, code coverage ≥ 90% logic/, coding standard compliance, no security violation)

---

## 9. Strategi Tagging dan Versioning
### 9.1. Standar Semantic Versioning (SemVer)
   (Format: MAJOR.MINOR.PATCH)
### 9.2. Konvensi Penamaan Tag
   (Format: v<MAJOR>.<MINOR>.<PATCH>)
### 9.3. Kapan Membuat Tag Baru
### 9.4. Prosedur Pembuatan Tag Release

---

## 10. Pengelolaan File Sensitif dan Keamanan Git
### 10.1. Daftar File yang WAJIB Dikecualikan (.gitignore)
### 10.2. Daftar File yang WAJIB Di-track
### 10.3. Prosedur Darurat Jika Kredensial Tercommit
   (git filter-branch / BFG Repo Cleaner / rotasi key)
### 10.4. Aturan Perlindungan Rahasia (.env, JWT Key, Fernet Key)

---

## 11. Prosedur Backup dan Recovery Repository
### 11.1. Strategi Backup Repository Git Lokal
### 11.2. Prosedur Clone/Mirror ke Media Eksternal
### 11.3. Prosedur Recovery Repository dari Backup

---

## 12. Panduan Git untuk Tim Campuran (Manusia + AI)
### 12.1. Konvensi Identitas Git untuk Setiap Model AI
   (Tabel: Model AI | Git user.name | Git user.email | Peran Git)
### 12.2. Aturan Kolaborasi Branch Antar-AI
### 12.3. Aturan Atribusi Commit untuk Kontribusi AI
   (Co-authored-by, Signed-off-by)
### 12.4. Prosedur Handover Pekerjaan Antar-AI via Git

---

## 13. Perintah Git yang Sering Digunakan (Quick Reference)
### 13.1. Perintah Dasar Sehari-hari
   (Tabel: Perintah | Fungsi | Contoh Penggunaan)
### 13.2. Perintah Branching dan Merge
### 13.3. Perintah Inspeksi dan Troubleshooting
### 13.4. Perintah Undo dan Recovery

---

## 14. Larangan Mutlak (Prohibited Practices)
   (Tabel: No | Praktik yang Dilarang | Dampak Negatif | Solusi yang Benar)

---

## 15. Checklist Kepatuhan Git Workflow
   (Format: - [ ] item checklist)

---

## 16. Referensi Dokumen
   (Tabel: No | Nama Dokumen | Path | Versi | Prioritas | Peran dalam Penyusunan)
```

> **Catatan Kerangka**: Struktur di atas disesuaikan dengan ciri khas spesifik dokumen Git Workflow dan konteks unik proyek AbuCom (tim campuran manusia + AI, offline LAN, dual-OS). Bab 12 tentang "Panduan Git untuk Tim Campuran" merupakan tambahan yang **sangat penting** karena mencerminkan realitas kolaborasi proyek AbuCom yang unik.

---

## 5. Instruksi Detail Tahapan Pengerjaan

Berikut adalah tahapan pengerjaan yang harus dilakukan secara berurutan. Setiap tahapan memiliki checklist spesifik yang harus diselesaikan.

### Tahap 1: Persiapan dan Pembacaan File Referensi

> **Tujuan**: Mengumpulkan dan merangkum semua data dan informasi yang relevan dari file referensi.

- [ ] **1.1.** Baca file referensi **R-01** (`docs/sdlc/04_implementation/01_coding_standard.md`).
  - [ ] 1.1.1. Cari dan rangkum Bab 15 "Standar Version Control (Git)" secara lengkap (Bab 15.1 s.d 15.5).
  - [ ] 1.1.2. Rangkum detail strategi Feature Branching (Bab 15.1).
  - [ ] 1.1.3. Rangkum konvensi penamaan branch: prefix `feature/` dan `bugfix/` beserta contohnya (Bab 15.2).
  - [ ] 1.1.4. Rangkum konvensi commit message: format `<tipe-commit>: <deskripsi>` dan tipe commit yang didefinisikan yaitu `feat`, `fix`, `docs` (Bab 15.3).
  - [ ] 1.1.5. Rangkum aturan `.gitignore`: file `.env`, `__pycache__/`, `*.pyc`, `.pytest_cache/`, `exports/backups/`, `exports/receipts/` (Bab 15.4).
  - [ ] 1.1.6. Rangkum aturan code review: peran Gemini 3 Flash sebagai reviewer kode otomatis sebelum merge ke `main` (Bab 15.5).
  - [ ] 1.1.7. Rangkum Bab 17 "Checklist Kepatuhan Coding Standard" sebagai referensi pre-merge quality gate (12 checklist item).

- [ ] **1.2.** Baca file referensi **R-02** (`docs/sdlc/04_implementation/02_environment_setup.md`).
  - [ ] 1.2.1. Cari dan rangkum Bab 9 "Setup Version Control (Git)" secara lengkap (Bab 9.1 s.d 9.5).
  - [ ] 1.2.2. Rangkum instruksi instalasi Git di Windows (Bab 9.1).
  - [ ] 1.2.3. Rangkum konfigurasi Git identity: `git config --global user.name` dan `user.email` beserta catatan manual (Bab 9.2).
  - [ ] 1.2.4. Rangkum langkah inisialisasi repository: `git init`, `git add`, `git commit` (Bab 9.3).
  - [ ] 1.2.5. Rangkum strategi Feature Branching: branch `main` sebagai stable release, pengerjaan modul wajib di branch fitur, contoh perintah `git checkout -b` (Bab 9.4).
  - [ ] 1.2.6. Rangkum konvensi commit message: format `type(scope): description` dan contoh 5 tipe commit yaitu `feat`, `fix`, `docs`, `chore`, `test` (Bab 9.5).
  - [ ] 1.2.7. Rangkum konfigurasi `.gitignore` dari Bab 8.5 secara lengkap (termasuk `.env`, `.env.test`, `__pycache__/`, `*.pyc`, `*.pyo`, `*.pyd`, `.pytest_cache/`, `.coverage`, `htmlcov/`, `venv/`, `ENV/`, `Thumbs.db`, `Desktop.ini`, `.DS_Store`).
  - [ ] 1.2.8. Rangkum checklist verifikasi Bab 13.5 item terkait Git: "Repositori Git diinisialisasi lokal, identitas diatur, dan commit baseline berhasil dibuat" serta ".gitignore terbuat sukses".

- [ ] **1.3.** Baca file referensi **R-03** (`docs/sdlc/04_implementation/03_module_structure.md`).
  - [ ] 1.3.1. Rangkum daftar 10 modul fungsional beserta file yang terkait (Bab 2.3 dan Bab 13).
  - [ ] 1.3.2. Rangkum layout direktori proyek lengkap (Bab 3.1) untuk memahami scope commit dan branch.
  - [ ] 1.3.3. Rangkum matriks pemetaan modul-to-file (Bab 13) untuk mendefinisikan scope commit message.

- [ ] **1.4.** Baca file referensi **R-04** (`docs/sdlc/01_planning/04_tech_stack_decision.md`).
  - [ ] 1.4.1. Rangkum informasi tentang susunan tim pengembang (6 model AI + Junior Programmer).
  - [ ] 1.4.2. Rangkum informasi tentang peran spesifik masing-masing model AI.
  - [ ] 1.4.3. Rangkum kebutuhan portabilitas dual-OS (Windows 11 & Linux Debian 12) yang berimplikasi pada konfigurasi Git (`core.autocrlf`, `.gitattributes`).

- [ ] **1.5.** Baca file referensi **R-05** (`docs/sdlc/03_design/03_system_architecture.md`).
  - [ ] 1.5.1. Rangkum arsitektur 4-layer dan diagram dependensi antar-layer sebagai konteks untuk scope branching.
  - [ ] 1.5.2. Rangkum daftar 10 modul fungsional dan peta dependensi antar-modul (Bab 5).

- [ ] **1.6.** Baca file referensi **R-06** (`docs/sdlc/03_design/06_security_design.md`).
  - [ ] 1.6.1. Rangkum aturan keamanan yang berkaitan dengan Git: file `.env` WAJIB dikecualikan, kredensial tidak boleh hardcoded, proteksi secret key.
  - [ ] 1.6.2. Rangkum implikasi keamanan jika file sensitif tercommit ke Git secara tidak sengaja.

- [ ] **1.7.** Baca file referensi **R-07** (`docs/sdlc/narasi.txt`).
  - [ ] 1.7.1. Rangkum susunan tim pengembang: "0. Junior Programmer: Saya sendiri. 1. Gemini 3.1 Pro (High). 2. Gemini 3.1 Pro (Low). 3. Gemini 3 Flash. 4. Claude Sonnet 4.6 (Thinking). 5. Claude Opus 4.6 (Thinking). 6. GPT-OSS 120B (Medium)."
  - [ ] 1.7.2. Rangkum peran masing-masing AI dan implikasinya terhadap Git workflow (siapa yang mengerjakan modul apa, siapa reviewer, dll.).

### Tahap 2: Konsolidasi dan Analisis Data

> **Tujuan**: Menyatukan semua rangkuman dari Tahap 1 menjadi satu kesatuan informasi yang koheren, dan mengidentifikasi data yang kosong.

- [ ] **2.1.** Gabungkan rangkuman data dari R-01 Bab 15 dan R-02 Bab 9 menjadi satu kesatuan informasi version control yang komprehensif. Identifikasi jika ada inkonsistensi atau perbedaan antara kedua sumber, dan gunakan R-01 (Coding Standard) sebagai prioritas utama karena bersifat **normatif** (aturan mengikat).
- [ ] **2.2.** Petakan setiap anggota tim (7 orang) ke peran Git yang sesuai:
  - Junior Programmer → Peran: Integrator utama, pemilik branch `main`.
  - Gemini 3.1 Pro (High) → Peran: Pengerjaan modul arsitektur kompleks, branch `feature/`.
  - Gemini 3.1 Pro (Low) → Peran: Pengerjaan rutin & dokumentasi, branch `feature/` dan `docs/`.
  - Gemini 3 Flash → Peran: Reviewer cepat & debugging ringan, tanpa branch sendiri.
  - Claude Sonnet 4.6 (Thinking) → Peran: Deep coding & refactoring, branch `feature/` dan `refactor/`.
  - Claude Opus 4.6 (Thinking) → Peran: Strategi sistem & keamanan, branch `feature/`.
  - GPT-OSS 120B (Medium) → Peran: Pembuatan boilerplate & data dummy, branch `feature/` dan `chore/`.
- [ ] **2.3.** Identifikasi data yang **TIDAK ADA** di dalam file referensi dan tandai dengan penanda `⚠️ [DATA KOSONG — PERLU DIISI MANUAL]`. Data yang kemungkinan kosong meliputi:
  - Konfigurasi `core.autocrlf` untuk cross-OS (perlu ditetapkan berdasarkan best practice).
  - Isi file `.gitattributes` (belum ada di referensi manapun).
  - Detail prosedur darurat jika kredensial tercommit (belum ada di referensi).
  - Strategi backup repository Git lokal secara berkala (belum ada di referensi).
  - Konvensi Git identity (user.name, user.email) untuk masing-masing model AI (belum ada di referensi).
- [ ] **2.4.** Untuk setiap data kosong di atas, tandai di dalam dokumen dengan format:
  ```
  > ⚠️ **[DATA KOSONG — PERLU DIISI MANUAL]**: [Deskripsi data yang perlu diisi dan alasan mengapa data ini diperlukan].
  ```
- [ ] **2.5.** Pastikan hanya data dan informasi yang spesifik relevan untuk dokumen Git Workflow yang diambil. Jangan menyertakan informasi yang sudah dicakup secara komprehensif oleh dokumen lain (misalnya: detail teknis `.env.example` sudah ada di Environment Setup, detail checklist coding sudah ada di Coding Standard).

### Tahap 3: Penyusunan Dokumen Utama

> **Tujuan**: Menulis dokumen `04_git_workflow.md` berdasarkan kerangka di Bab 4 dan data konsolidasi dari Tahap 2.

- [ ] **3.1.** Buat file target `docs/sdlc/04_implementation/04_git_workflow.md`.
- [ ] **3.2.** Tulis **Header Metadata** dokumen (frontmatter YAML):
  ```yaml
  ---
  dokumen    : Git Workflow
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [TANGGAL PENGERJAAN AKTUAL]
  status     : Draft
  penyusun   : Senior DevOps Engineer & Git Workflow Architect
  ---
  ```
- [ ] **3.3.** Tulis **Riwayat Perubahan Dokumen** dengan format tabel markdown:
  ```
  | Versi | Tanggal | Perubahan | Oleh |
  ```
- [ ] **3.4.** Tulis **Bab 1: Informasi Dokumen** secara lengkap:
  - [ ] 3.4.1. Tulis Tujuan Dokumen: jelaskan bahwa dokumen ini mendefinisikan standar pengelolaan version control Git untuk proyek AbuCom.
  - [ ] 3.4.2. Tulis Cakupan Dokumen: sebutkan semua area yang dicakup (branching, commit, merge, review, tagging, keamanan, kolaborasi tim AI).
  - [ ] 3.4.3. Tulis Posisi Dokumen dalam SDLC: deliverable ke-4 pada Fase 04 Implementation, dengan diagram posisi ASCII.
  - [ ] 3.4.4. Tulis Hubungan dengan Dokumen SDLC Lainnya: daftar input (acuan) dan output (penerima manfaat) menggunakan format bullet list dengan link relatif.
  - [ ] 3.4.5. Tulis Audiens Target: Junior Programmer (Pemilik Usaha) dan Tim Pengembang AI.
  - [ ] 3.4.6. Tulis Definisi, Akronim, dan Singkatan: termasuk Git, Branch, Commit, Merge, Tag, SemVer, PR, CI, dll.

- [ ] **3.5.** Tulis **Bab 2: Prinsip Dasar Pengelolaan Version Control**:
  - [ ] 3.5.1. Definisikan filosofi: "Traceability, Collaboration, and Code Integrity".
  - [ ] 3.5.2. Tulis aturan umum: setiap perubahan WAJIB tercatat di Git, dilarang memodifikasi langsung branch `main`, setiap kontribusi harus melalui branch terpisah.
  - [ ] 3.5.3. Tulis tabel peran dan tanggung jawab 7 anggota tim dalam Git workflow berdasarkan data Tahap 2.2.

- [ ] **3.6.** Tulis **Bab 3: Konfigurasi Git Awal**:
  - [ ] 3.6.1. Tulis instruksi instalasi Git (cross-reference ke R-02 Bab 9.1).
  - [ ] 3.6.2. Tulis instruksi konfigurasi identity dengan perintah `git config`.
  - [ ] 3.6.3. Tulis konfigurasi global: `core.autocrlf=true` (Windows) / `core.autocrlf=input` (Linux) untuk menjamin konsistensi line ending lintas OS.
  - [ ] 3.6.4. Tulis instruksi inisialisasi repository (cross-reference ke R-02 Bab 9.3).
  - [ ] 3.6.5. Tulis isi file `.gitignore` secara lengkap dan komprehensif (gabungan dari R-01 Bab 15.4 dan R-02 Bab 8.5), tambahkan entry yang belum ada: `exports/backups/`, `exports/receipts/`, `exports/designs/`, `pip_wheels/`, `*.log`, `*.bak`.
  - [ ] 3.6.6. Tulis isi file `.gitattributes` untuk menangani line ending cross-OS:
    ```
    * text=auto
    *.py text eol=lf
    *.md text eol=lf
    *.sql text eol=lf
    *.txt text eol=lf
    *.bat text eol=crlf
    ```

- [ ] **3.7.** Tulis **Bab 4: Strategi Branching**:
  - [ ] 3.7.1. Jelaskan model Feature Branching yang diadopsi (sesuai R-01 Bab 15.1 dan R-02 Bab 9.4).
  - [ ] 3.7.2. Buat diagram Mermaid yang mengilustrasikan alur branching (main ← feature branches).
  - [ ] 3.7.3. Tulis tabel daftar branch lengkap dengan fungsi, pembuat, dan kebijakan merge.
  - [ ] 3.7.4. Tulis konvensi penamaan branch dalam format tabel berikut:
    - `feature/<nama-modul-atau-fitur>` — Penambahan fungsionalitas baru.
    - `bugfix/<deskripsi-bug>` — Perbaikan kesalahan program.
    - `hotfix/<deskripsi-hotfix>` — Perbaikan darurat produksi.
    - `docs/<nama-dokumen>` — Pembaruan dokumentasi.
    - `test/<nama-test>` — Penambahan pengujian.
    - `refactor/<deskripsi>` — Refactoring tanpa menambah fitur.
    - `chore/<deskripsi>` — Perubahan konfigurasi/dependensi.
  - [ ] 3.7.5. Tulis aturan proteksi branch `main`: dilarang push langsung, wajib melalui merge dari branch fitur, wajib code review.
  - [ ] 3.7.6. Tulis siklus hidup branch: kapan dibuat, kapan di-merge, kapan dihapus.

- [ ] **3.8.** Tulis **Bab 5: Konvensi Commit**:
  - [ ] 3.8.1. Tulis format Conventional Commits: `<type>(<scope>): <description>`.
  - [ ] 3.8.2. Tulis tabel daftar tipe commit yang diizinkan (elaborasi dari R-01 Bab 15.3 dan R-02 Bab 9.5):
    - `feat` — Penambahan fitur bisnis baru.
    - `fix` — Perbaikan bug atau celah keamanan.
    - `docs` — Perubahan dokumentasi.
    - `chore` — Perubahan konfigurasi, dependensi, atau `.gitignore`.
    - `test` — Penambahan atau modifikasi unit test.
    - `refactor` — Restrukturisasi kode tanpa mengubah perilaku.
    - `style` — Perubahan formatting, whitespace, tanpa mengubah logika.
    - `perf` — Peningkatan performa.
    - `revert` — Pembatalan commit sebelumnya.
  - [ ] 3.8.3. Tulis aturan scope berdasarkan modul fungsional (gunakan data dari R-03):
    - Scope yang valid: `transaksi`, `inventaris`, `ppob`, `sdm`, `antrian`, `keuangan`, `keamanan`, `crm`, `cabang`, `config`, `db`, `cli`, `middleware`, `utils`.
  - [ ] 3.8.4. Tulis aturan deskripsi commit: huruf kecil, imperative mood bahasa Indonesia, maksimal 72 karakter.
  - [ ] 3.8.5. Tulis aturan body dan footer (opsional): breaking changes, referensi issue, `Co-authored-by`.
  - [ ] 3.8.6. Tulis contoh commit message yang benar dan salah dalam format tabel perbandingan.
  - [ ] 3.8.7. Tulis aturan atomisitas commit: satu commit harus merepresentasikan satu perubahan logis tunggal.

- [ ] **3.9.** Tulis **Bab 6: Alur Kerja Pengembangan**:
  - [ ] 3.9.1. Buat diagram flowchart Mermaid yang mengilustrasikan alur kerja lengkap.
  - [ ] 3.9.2. Tulis langkah-langkah detail alur kerja secara step-by-step dengan perintah Git yang tepat.
  - [ ] 3.9.3. Tulis alur kerja untuk: Feature, Bugfix, Hotfix, dan Docs workflow secara terpisah.

- [ ] **3.10.** Tulis **Bab 7: Strategi Merge dan Conflict Resolution**:
  - [ ] 3.10.1. Tentukan kebijakan merge yang digunakan (rekomendasi: merge commit `--no-ff` untuk menjaga riwayat branch).
  - [ ] 3.10.2. Tulis prosedur merge step-by-step.
  - [ ] 3.10.3. Tulis prosedur penanganan merge conflict step-by-step.
  - [ ] 3.10.4. Buat diagram Mermaid untuk alur resolusi konflik.
  - [ ] 3.10.5. Tulis aturan pencegahan konflik.

- [ ] **3.11.** Tulis **Bab 8: Code Review dan Quality Gate**:
  - [ ] 3.11.1. Tulis prosedur code review sebelum merge.
  - [ ] 3.11.2. Definisikan Gemini 3 Flash sebagai reviewer cepat sesuai R-01 Bab 15.5.
  - [ ] 3.11.3. Integrasikan 12 checklist kepatuhan dari Coding Standard sebagai pre-merge quality gate.
  - [ ] 3.11.4. Tulis kriteria lulus quality gate (unit test pass, coverage ≥ 90%, coding standard compliance).

- [ ] **3.12.** Tulis **Bab 9: Strategi Tagging dan Versioning**:
  - [ ] 3.12.1. Definisikan standar Semantic Versioning (SemVer).
  - [ ] 3.12.2. Tulis konvensi penamaan tag: `v<MAJOR>.<MINOR>.<PATCH>`.
  - [ ] 3.12.3. Tulis kapan membuat tag baru dan prosedurnya.

- [ ] **3.13.** Tulis **Bab 10: Pengelolaan File Sensitif dan Keamanan Git**:
  - [ ] 3.13.1. Tulis daftar file yang WAJIB dikecualikan dari Git (cross-reference R-06).
  - [ ] 3.13.2. Tulis daftar file yang WAJIB di-track di Git.
  - [ ] 3.13.3. Tulis prosedur darurat jika kredensial tercommit secara tidak sengaja.
  - [ ] 3.13.4. Tulis aturan perlindungan rahasia.

- [ ] **3.14.** Tulis **Bab 11: Prosedur Backup dan Recovery Repository**:
  - [ ] 3.14.1. Tulis strategi backup repository Git lokal secara berkala.
  - [ ] 3.14.2. Tulis prosedur clone/mirror ke media eksternal (USB flashdisk).
  - [ ] 3.14.3. Tulis prosedur recovery repository dari backup.

- [ ] **3.15.** Tulis **Bab 12: Panduan Git untuk Tim Campuran (Manusia + AI)**:
  - [ ] 3.15.1. Tulis tabel konvensi identitas Git untuk setiap model AI:
    | Model AI                      | Git user.name                  | Git user.email                          | Peran Git                         |
    |:---                           |:---                            |:---                                     |:---                               |
    | Junior Programmer             | Junior Programmer              | ⚠️ [HARUS DIISI MANUAL]                | Integrator, Pemilik branch main   |
    | Gemini 3.1 Pro (High)         | Gemini-Pro-High                | gemini-pro-high@abucom.local            | Feature Developer (Arsitektur)    |
    | Gemini 3.1 Pro (Low)          | Gemini-Pro-Low                 | gemini-pro-low@abucom.local             | Feature Developer (Rutin & Docs)  |
    | Gemini 3 Flash                | Gemini-Flash                   | gemini-flash@abucom.local               | Code Reviewer                     |
    | Claude Sonnet 4.6 (Thinking)  | Claude-Sonnet                  | claude-sonnet@abucom.local              | Feature Developer (Deep Coding)   |
    | Claude Opus 4.6 (Thinking)    | Claude-Opus                    | claude-opus@abucom.local                | Feature Developer (Strategi)      |
    | GPT-OSS 120B (Medium)         | GPT-OSS-Medium                 | gpt-oss-medium@abucom.local             | Boilerplate & Data Dummy          |
  - [ ] 3.15.2. Tulis aturan kolaborasi branch antar-AI: satu branch per AI per tugas, dilarang dua AI bekerja pada branch yang sama secara simultan.
  - [ ] 3.15.3. Tulis aturan atribusi commit AI menggunakan trailer `Co-authored-by` atau `Signed-off-by`.
  - [ ] 3.15.4. Tulis prosedur handover pekerjaan antar-AI melalui Git.

- [ ] **3.16.** Tulis **Bab 13: Perintah Git yang Sering Digunakan**:
  - [ ] 3.16.1. Tulis tabel quick reference perintah dasar (git add, commit, push, pull, status, log, diff, branch, checkout, merge, tag).
  - [ ] 3.16.2. Tulis perintah branching dan merge.
  - [ ] 3.16.3. Tulis perintah inspeksi dan troubleshooting (git log --oneline --graph, git reflog, git stash).
  - [ ] 3.16.4. Tulis perintah undo dan recovery (git reset, git revert, git checkout -- file).

- [ ] **3.17.** Tulis **Bab 14: Larangan Mutlak**:
  - [ ] 3.17.1. Tulis tabel larangan dalam format: No | Praktik yang Dilarang | Dampak Negatif | Solusi yang Benar. Minimal 8 larangan:
    1. Push langsung ke branch `main`.
    2. Commit file `.env` atau kredensial sensitif.
    3. Force push (`git push --force`) ke branch bersama.
    4. Commit file binary besar (gambar, video, database dump).
    5. Commit message tidak deskriptif ("fix", "update", "wip").
    6. Mengerjakan banyak fitur dalam satu branch.
    7. Merge tanpa code review.
    8. Mengabaikan merge conflict tanpa resolusi manual.

- [ ] **3.18.** Tulis **Bab 15: Checklist Kepatuhan Git Workflow**:
  - [ ] 3.18.1. Buat checklist markdown `- [ ]` untuk verifikasi kepatuhan sebelum merge, minimal 10 item.

- [ ] **3.19.** Tulis **Bab 16: Referensi Dokumen**:
  - [ ] 3.19.1. Tulis tabel referensi dokumen lengkap dalam format:
    | No | Nama Dokumen Referensi | Path Relatif File | Versi | Prioritas | Peran dalam Penyusunan |
  - [ ] 3.19.2. Masukkan semua 7 file referensi yang digunakan (R-01 s.d R-07) sesuai tabel di Bab 3 issue ini.

### Tahap 4: Validasi dan Finalisasi

> **Tujuan**: Memastikan kualitas dan kelengkapan dokumen sebelum finalisasi.

- [ ] **4.1.** Validasi bahwa **SEMUA bab** dalam kerangka struktur (Bab 4 issue ini) sudah terisi konten di dokumen target.
- [ ] **4.2.** Validasi bahwa **SEMUA data** dari 7 file referensi yang relevan dengan Git Workflow sudah terangkum dan tercantum di dokumen target. Tidak boleh ada data penting yang terlewat.
- [ ] **4.3.** Validasi bahwa setiap data yang kosong / tidak tersedia di file referensi sudah ditandai dengan penanda `⚠️ [DATA KOSONG — PERLU DIISI MANUAL]`.
- [ ] **4.4.** Validasi bahwa bahasa Indonesia yang digunakan bersifat natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh Junior Programmer atau AI model lain.
- [ ] **4.5.** Validasi bahwa dokumen ini layak untuk dijadikan referensi dan acuan utama bagi:
  - Konstruksi kode aktual per modul (Fase 04 selanjutnya).
  - Proses code review dan quality assurance.
  - Onboarding anggota tim baru (baik manusia maupun AI).
- [ ] **4.6.** Validasi bahwa format markdown konsisten: heading hierarchy benar (h1 > h2 > h3), tabel terformat rapi, kode blok menggunakan syntax highlighting, dan diagram Mermaid valid secara sintaksis.
- [ ] **4.7.** Validasi bahwa bagian "Referensi Dokumen" (Bab 16) sudah terisi lengkap dengan 7 file referensi.
- [ ] **4.8.** Pastikan semua hasil pengerjaan sudah dituangkan ke dalam target file: `docs/sdlc/04_implementation/04_git_workflow.md`.

### Tahap 5: Penulisan ke Target File

> **Tujuan**: Menuangkan semua hasil pengerjaan ke target file yang sudah ditentukan.

- [ ] **5.1.** Tulis seluruh konten dokumen yang sudah disusun ke dalam file target `docs/sdlc/04_implementation/04_git_workflow.md`.
- [ ] **5.2.** Verifikasi bahwa file target tidak kosong dan berisi dokumen yang lengkap.
- [ ] **5.3.** Verifikasi bahwa encoding file adalah UTF-8.

---

## 6. Instruksi Tambahan Khusus Dokumen Git Workflow

Berikut adalah instruksi tambahan yang spesifik terhadap ciri khas dokumen Git Workflow dan belum tercakup pada kriteria umum di atas:

### 6.1. Line Ending Cross-OS (CRLF vs LF)
- [ ] Pastikan dokumen secara eksplisit mendefinisikan aturan line ending karena proyek AbuCom berjalan di dual-OS (Windows 11 dan Linux Debian 12). Konfigurasi `core.autocrlf` dan `.gitattributes` WAJIB dibahas secara mendetail untuk mencegah bug line ending yang sulit di-debug.

### 6.2. Git Hooks (Opsional — Rekomendasi Best Practice)
- [ ] Pertimbangkan untuk menambahkan bab tentang Git Hooks yang relevan:
  - `pre-commit`: Validasi otomatis format kode (PEP 8), cek `.env` tidak ter-stage.
  - `commit-msg`: Validasi format commit message sesuai Conventional Commits.
  - **Catatan**: Bab ini bersifat opsional/rekomendasi (`DIREKOMENDASIKAN`), bukan wajib.

### 6.3. Git Stash Workflow
- [ ] Tambahkan panduan penggunaan `git stash` untuk menyimpan perubahan sementara saat perlu berpindah branch, karena ini sangat umum terjadi dalam kolaborasi multi-AI.

### 6.4. Diagram Mermaid
- [ ] Pastikan setiap diagram Mermaid yang dibuat memiliki sintaksis yang valid. Gunakan quote pada label node yang mengandung karakter khusus (tanda kurung, ampersand, dll.).

### 6.5. Tingkat Kepatuhan (Compliance Levels)
- [ ] Gunakan tingkat kepatuhan yang sama dengan Coding Standard (RFC 2119):
  - `[WAJIB]` / `MUST` — Tidak dapat dinegosiasikan.
  - `[DILARANG]` / `MUST NOT` — Praktik yang dilarang keras.
  - `[DIREKOMENDASIKAN]` / `SHOULD` — Best practice yang sangat disarankan.
  - `[OPSIONAL]` / `MAY` — Pilihan fleksibel.

---

## 7. Catatan Akhir untuk Pelaksana

1. **Jangan mengarang data**. Jika informasi tidak ditemukan di file referensi, tandai sebagai `⚠️ [DATA KOSONG — PERLU DIISI MANUAL]` dan jangan membuat asumsi sendiri.
2. **Jangan menyertakan informasi di luar scope**. Dokumen ini hanya membahas Git Workflow. Jangan mengulang penjelasan detail tentang arsitektur sistem, database schema, atau coding standard yang sudah dibahas di dokumen lain. Cukup cross-reference saja.
3. **Gunakan bahasa Indonesia yang natural**. Hindari terjemahan literal dari bahasa Inggris yang kaku. Gunakan kalimat yang mengalir dan mudah dipahami.
4. **Pastikan konsistensi format**. Ikuti pola format dokumen yang sudah ada di R-01, R-02, dan R-03 (frontmatter YAML, heading hierarchy, tabel, code block, diagram Mermaid).
5. **Kualitas harus final**. Dokumen yang dihasilkan harus siap digunakan tanpa perlu revisi besar. Kelengkapan isi tidak boleh selalu dipertanyakan dan tidak boleh menghambat proses pekerjaan fase SDLC selanjutnya.
6. **Referensi harus tercantum**. Bagian akhir dokumen WAJIB berisi tabel referensi file yang digunakan dalam penyusunan.

---

*Issue ini dibuat pada 2026-05-26 sebagai perencanaan low-level untuk eksekusi oleh Junior Programmer atau LLM model AI lain.*
