---
dokumen    : Git Workflow
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : 2026-05-26
status     : Draft
penyusun   : Senior DevOps Engineer & Git Workflow Architect
---

# Git Workflow — AbuCom

## Riwayat Perubahan Dokumen

| Versi | Tanggal | Perubahan | Oleh |
|:---:|:---:|:---|:---|
| **1.0** | 2026-05-26 | Inisialisasi awal penyusunan dokumen *Git Workflow* secara komprehensif. Menyelaraskan seluruh spesifikasi versi 1.1 dari Coding Standard, Environment Setup, Module Structure, Tech Stack Decision, System Architecture, Security Design, dan Narasi Pemilik. Mendefinisikan strategi feature branching, konvensi commit message, merge policy, code review quality gate, tagging, versioning, keamanan file sensitif, backup lokal, kolaborasi tim campuran (staf manusia + 6 AI), quick reference commands, dan checklist kepatuhan. | Senior DevOps Engineer & Git Workflow Architect |

---

## 1. Informasi Dokumen

### 1.1. Tujuan Dokumen
Dokumen **Git Workflow** ini disusun untuk mendefinisikan secara formal, rinci, dan mengikat seluruh standar, prosedur, dan kebijakan pengelolaan version control Git yang akan digunakan oleh seluruh tim pengembang (Junior Programmer dan 6 Model AI) selama proses konstruksi kode program **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**. Standardisasi ini dirancang untuk menjaga kualitas, ketertelusuran (*traceability*), kolaborasi yang harmonis, dan integritas codebase guna meminimalkan risiko selisih stok finansial, fraud data, atau kegagalan Dual-OS (Windows 11 & Linux Debian 12) pada laci kasir luring.

### 1.2. Cakupan Dokumen
Cakupan aturan dalam dokumen Git Workflow ini meliputi:
*   Prinsip dasar pengelolaan version control lokal offline LAN.
*   Konfigurasi Git awal (Instalasi, Identity, Global Setting, .gitignore, dan .gitattributes).
*   Strategi branching (Feature Branching Model, diagram Mermaid, konvensi penamaan branch, dan proteksi branch).
*   Konvensi commit (Conventional Commits, tipe, scope valid berbasis modul, deskripsi imperative, dan contoh commit Benar vs Salah).
*   Alur kerja pengembangan (flowchart Mermaid, alur kerja feature/bugfix/hotfix/docs).
*   Strategi merge dan conflict resolution (merge policy `--no-ff`, flowchart resolusi konflik, dan aturan preventif).
*   Code review dan quality gate (integrasi 12 checklist Coding Standard R-01, peran Gemini 3 Flash, kriteria kelulusan).
*   Tagging dan versioning (Semantic Versioning SemVer, konvensi tag `vX.Y.Z`).
*   Pengelolaan file sensitif dan keamanan Git (keamanan credentials, audit trail).
*   Prosedur backup dan recovery repository lokal secara offline LAN.
*   Panduan Git khusus untuk tim campuran (Junior Programmer + 6 Model AI).
*   Perintah Git yang sering digunakan (Quick Reference).
*   Checklist kepatuhan pre-merge.

### 1.3. Posisi Dokumen dalam Siklus SDLC
Dalam siklus pengembangan sistem (*System Development Life Cycle* — SDLC) AbuCom, dokumen ini merupakan deliverable keempat pada **Fase 04 — Implementation (Fase Konstruksi)**. Dokumen ini bertindak sebagai panduan operasional wajib guna mematangkan cara pengelolaan kode program yang dihasilkan pada Fase 04 ini.

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
|    Aktual per Modul (M.1 - M.10)  |
+-----------------------------------+
```

### 1.4. Hubungan dengan Dokumen SDLC Lainnya (Input & Output)
*   **Dokumen Input (Acuan)**:
    - [Coding Standard v1.1](docs/sdlc/04_implementation/01_coding_standard.md): Acuan Bab 15 (Version Control Git), Bab 17 (Checklist Kepatuhan), standardisasi desimal `decimal.Decimal` dan FP murni.
    - [Environment Setup v1.1](docs/sdlc/04_implementation/02_environment_setup.md): Acuan Bab 9 (Setup Git lokal), Bab 8.5 (Setup .gitignore), credentials setup (.env.example).
    - [Module Structure v1.1](docs/sdlc/04_implementation/03_module_structure.md): Acuan Bab 2.3 (10 modul fungsional), Bab 3.1 (ASCII direktori pohon proyek), Bab 13 (Module-to-File mapping) untuk penentuan scope commit.
    - [Tech Stack Decision v1.1](docs/sdlc/01_planning/04_tech_stack_decision.md): SSoT untuk platform runtime, locked library version, dan dual-OS portabilitas.
    - [System Architecture v1.1](docs/sdlc/03_design/03_system_architecture.md): Diagram topologi LAN offline, isolation level repeatable read, dan connection pool 'abupool'.
    - [Security Design v1.1](docs/sdlc/03_design/06_security_design.md): Spesifikasi UU PDP (whatsapp CRM), enkripsi backup AES-256 ZIP, chmod 700 server, audit log JSON, brute-force rate-limiting, and sanitasi CLI.
    - [Narasi Pemilik](docs/sdlc/narasi.txt): Konteks tim campuran (Junior Programmer + 6 Model AI spesialis).
*   **Dokumen Output (Penerima Manfaat)**:
    - Seluruh proses pengerjaan konstruksi kode fungsional `.py` per modul pada repositori lokal `abucom/`.
    - Unit testing fungsional (`tests/`) and proses QA integrasi database testing.

### 1.5. Audiens Target
*   **Junior Programmer (Pemilik Toko)**: Sebagai panduan operasional integrasi branch, backup database lokal, dan peninjau kode (*reviewer*) utama.
*   **Model AI Pengembang (6 Asisten AI)**: Sebagai instruksi deterministik dan kaku mengenai cara pengerjaan branch, pembuatan pesan commit, atribusi kepemilikan, dan aturan merge.

### 1.6. Definisi, Akronim, dan Singkatan
*   **Branch**: Cabang independen dari codebase program untuk pengerjaan fitur terpisah.
*   **Commit**: Perekaman snapshot perubahan kode secara kronologis di Git.
*   **Merge**: Penggabungan riwayat perubahan dari branch fitur ke branch utama.
*   **SemVer**: *Semantic Versioning* (Format standar penamaan rilis vMAJOR.MINOR.PATCH).
*   **Conventional Commits**: Konvensi penulisan commit message terstruktur (`type(scope): description`).
*   **FP**: *Functional Programming* (Paradigma pemrograman fungsional murni tanpa class).
*   **LAN**: *Local Area Network* (Jaringan offline lokal toko tanpa koneksi luar).

---

## 2. Prinsip Dasar Pengelolaan Version Control

### 2.1. Filosofi Version Control AbuCom
Filosofi pengelolaan Git di AbuCom berlandaskan tiga pilar utama: **"Traceability, Collaboration, and Code Integrity"** (Keterlacakan, Kolaborasi, dan Integritas Kode). 
Setiap perubahan baris kode wajib tercatat dengan jelas siapa pembuatnya (AI mana atau pemilik), apa tujuannya, bagian mana yang berubah (scope modul), dan wajib mempertahankan keselarasan 100% terhadap Coding Standard tanpa merusak state database luring.

### 2.2. Aturan Umum Penggunaan Git
1.  `[WAJIB]` Seluruh pengerjaan kode program (fungsional, utilitas, CLI, middleware, konfigurasi, test suite) wajib dilacak menggunakan repositori Git lokal.
2.  `[DILARANG]` Melakukan push langsung atau mengedit secara instan kode program di branch utama `main`.
3.  `[WAJIB]` Setiap tugas pengembangan wajib dikerjakan pada branch terpisah (*Feature Branch*) sebelum digabungkan melalui proses *code review* formal.
4.  `[WAJIB]` Seluruh pesan commit wajib mematuhi standar *Conventional Commits* menggunakan bahasa Indonesia profesional.

### 2.3. Peran dan Tanggung Jawab Tim dalam Git Workflow
Kolaborasi pengembangan AbuCom terdiri atas 1 Junior Programmer (manusia) dan 6 Model AI spesialis. Tabel berikut memetakan wewenang Git masing-masing peran secara formal:

| Anggota Tim | Kode Peran | Peran Git dalam Workflow | Cakupan Pekerjaan & Wewenang |
|:---|:---:|:---|:---|
| **Junior Programmer** (Pemilik Usaha) | `STK-000` | Owner, Integrator, Release Manager | Pemilik mutlak branch `main`, verifikator pre-merge quality gate, penilai merger, pengelola backup & tagging rilis. |
| **Gemini 3.1 Pro (High)** | `STK-009` | Heavy Logic Developer | Pengerjaan branch `feature/` modul berat (BOM M.2, Smart Payroll M.4, Financial M.6). |
| **Gemini 3.1 Pro (Low)** | `STK-010` | Routine Developer & Documenter | Pengerjaan branch `feature/` rutin, pembuatan branch `docs/` dokumen SDLC. |
| **Gemini 3 Flash** | `STK-011` | Automated Reviewer & Debugger | Reviewer cepat pre-merge quality gate, pengerjaan branch `bugfix/` atau `hotfix/` ringan. |
| **Claude Sonnet 4.6 (Thinking)**| `STK-012` | Deep Coder & UI Specialist | Pengerjaan branch `feature/` FP tingkat tinggi, optimasi CLI `rich` (M.1 & M.5), branch `refactor/`. |
| **Claude Opus 4.6 (Thinking)** | `STK-013` | Security & Cryptography Lead | Pengerjaan branch `feature/` middleware keamanan (M.7), enkripsi Fernet WA (M.8), AES-256 backup. |
| **GPT-OSS 120B (Medium)** | `STK-014` | Boilerplate & Dummy Data Provider | Penyusunan branch `chore/` awal, inisialisasi `schema.sql` dan `seed.sql`. |

---

## 3. Konfigurasi Git Awal

### 3.1. Instalasi Git (Windows 11 & Linux Debian 12)
*   **Windows 11 (Klien Kasir)**:
    1.  Unduh installer resmi *Git for Windows* dari `git-scm.com`.
    2.  Jalankan instalasi dengan memilih opsi default, pastikan opsi *Git Bash* dan *Add to PATH* tercentang.
*   **Linux Debian 12 (Server Database)**:
    1.  Sebagai administrator (root), pasang Git secara luring menggunakan berkas `.deb` lokal atau repositori luring:
        `apt-get install git -y`

### 3.2. Konfigurasi Git Identity (user.name, user.email)
Setiap pengembang (staf manusia) wajib mendaftarkan identitas globalnya di mesin masing-masing:
```bash
git config --global user.name "Junior Programmer"
git config --global user.email "donsise@example.com"
```
> ⚠️ **[DATA KOSONG — PERLU DIISI MANUAL]**: Ganti string `"Junior Programmer"` dan `"donsise@example.com"` di atas menggunakan nama asli pemilik usaha dan email personal riil yang aktif! Identitas ini penting agar log audit Git melacak penanggung jawab fisik dengan valid.

### 3.3. Konfigurasi Global Git (core.autocrlf, core.editor, default branch)
Untuk mencegah anomali sintaksis akibat perbedaan line ending sistem operasi dual-OS (Windows 11 menggunakan CRLF `\r\n` sedangkan Debian 12 menggunakan LF `\n`):
1.  **Konfigurasi core.autocrlf**:
    *   Pada Windows Klien Kasir:
        `git config --global core.autocrlf true`
    *   Pada Debian Server Database:
        `git config --global core.autocrlf input`
2.  **Konfigurasi Default Branch**:
    `git config --global init.defaultBranch main`
3.  **Konfigurasi Default Editor**:
    `git config --global core.editor nano`

> ⚠️ **[DATA KOSONG — PERLU DIISI MANUAL]**: Konfigurasi global `core.autocrlf` di atas wajib dieksekusi secara manual pada console terminal masing-masing OS klien dan server sebelum melakukan clone atau commit pertama guna menolak kecacatan formatting visual.

### 3.4. Inisialisasi Repository Lokal
Buka Windows Terminal (CMD/Bash) di PC Kasir, masuk ke folder proyek dan inisialisasi repositori Git:
```cmd
cd C:\Users\donsise\Documents\abucom
git init
```

### 3.5. Konfigurasi File .gitignore (Lengkap)
Buat file `.gitignore` pada root direktori proyek `C:\Users\donsise\Documents\abucom\.gitignore` (gabungan R-01 Bab 15.4 & R-02 Bab 8.5) untuk mencegah kebocoran credentials atau berkas sampah ter-track:
```
# ==============================================================================
# KONFIGURASI PENGABAIAN GIT ABUCOM
# ==============================================================================

# 1. Konfigurasi Rahasia & Kredensial (KEAMANAN SANGAT SENSITIF)
.env
.env.test

# 2. Python Cache, Compiler & Runtime Environments
__pycache__/
*.pyc
*.pyo
*.pyd
.pytest_cache/
.coverage
htmlcov/
venv/
ENV/
pip_wheels/

# 3. Hasil Backup, Desain & Struk Kasir Lokal (DILARANG TRACK BULK FILES)
exports/backups/*
exports/designs/*
exports/receipts/*
!exports/backups/.gitkeep
!exports/designs/.gitkeep
!exports/receipts/.gitkeep

# 4. Berkas Temporary Sistem Operasi & IDE
Thumbs.db
Desktop.ini
.DS_Store
.vscode/
.idea/
*.log
*.bak
```

### 3.6. Konfigurasi File .gitattributes (Line Ending Cross-OS)
Buat file `.gitattributes` pada root direktori proyek `C:\Users\donsise\Documents\abucom\.gitattributes` untuk memaksa penanganan line ending yang konsisten lintas platform Dual-OS secara kaku:
```
# ==============================================================================
# ATRIBUSI LINE ENDING DUAL-OS ABUCOM
# ==============================================================================

# Atur default penanganan teks secara otomatis
* text=auto

# Paksa file Python, Markdown, SQL, dan Teks menggunakan line-feed (LF) khas Linux
*.py text eol=lf
*.md text eol=lf
*.sql text eol=lf
*.txt text eol=lf

# Paksa file batch script Windows menggunakan carriage-return + line-feed (CRLF)
*.bat text eol=crlf
*.cmd text eol=crlf
```
> ⚠️ **[DATA KOSONG — PERLU DIISI MANUAL]**: Berkas `.gitattributes` di atas belum tercantum pada berkas rancangan SDLC awal manapun. Pengembang wajib menuangkan berkas ini di root proyek untuk memproteksi integritas visual terminal rich.

---

## 4. Strategi Branching

### 4.1. Model Branching yang Diadopsi (Feature Branching Model)
Sistem AbuCom mengadopsi model **Feature Branching**. Model ini membatasi branch utama `main` agar selalu berada dalam keadaan bersih, steril, stabil, dan siap dirilis ke komputer kasir riil toko harian. Seluruh pengerjaan modul, perbaikan bug, atau penyusunan dokumen SDLC wajib diisolasi di branch-branch fitur tersendiri.

### 4.2. Diagram Alur Branching (Mermaid)

```mermaid
gitGraph
    commit id: "chore: initial commit (v0.1.0)"
    branch feature/modul-transaksi
    checkout feature/modul-transaksi
    commit id: "feat(transaksi): add logic"
    commit id: "feat(transaksi): add invoice print"
    checkout main
    branch docs/git-workflow
    checkout docs/git-workflow
    commit id: "docs(sdlc): draft git workflow"
    checkout main
    merge docs/git-workflow tag: "v1.0.0-docs"
    checkout feature/modul-transaksi
    commit id: "test(transaksi): unit test pass"
    checkout main
    merge feature/modul-transaksi tag: "v1.1.0-beta"
    branch hotfix/pembulatan-kasbon
    checkout hotfix/pembulatan-kasbon
    commit id: "fix(sdm): rounding payroll UMR"
    checkout main
    merge hotfix/pembulatan-kasbon tag: "v1.1.1"
```

### 4.3. Daftar Branch dan Fungsinya

| Nama Branch | Tujuan / Tanggung Jawab Utama | Pembuat Branch | Kebijakan Merge ke `main` |
|:---|:---|:---|:---|
| **`main`** | Baseline produksi steril, menampung kode stabil yang sedang berjalan aktif di toko. | `STK-000` (Eksklusif) | Dilarang keras push langsung. Hanya boleh menerima merge dari branch fitur setelah lolos quality gate. |
| **`feature/<nama-modul>`** | Pengembangan use case baru modul fungsional (M.1 s.d M.10). | Model AI Coder (`STK-009`, `STK-012`, dll.) | Wajib melalui *Pull Request/Merge Request* dengan verifikasi code review Gemini 3 Flash. |
| **`bugfix/<deskripsi-bug>`** | Perbaikan kesalahan atau celah logika yang ditemukan pada lingkungan development. | `STK-011` (Gemini Flash) / Developer terkait | Penggabungan normal setelah unit testing perbaikan dinyatakan sukses. |
| **`hotfix/<deskripsi-hotfix>`**| Perbaikan darurat atas anomali data di lingkungan produksi yang menghambat operasional toko. | `STK-000` atau Coder Keamanan (`STK-013`) | Penggabungan cepat setelah diverifikasi mandiri oleh pemilik. |
| **`docs/<nama-dokumen>`** | Penyusunan draf atau revisi dokumen SDLC di subfolder `docs/`. | `STK-010` (Gemini Pro Low) | Penggabungan langsung setelah disetujui format bahasanya oleh pemilik. |
| **`refactor/<deskripsi>`** | Restrukturisasi struktur logic/ atau db/ tanpa merubah output fungsi bisnis. | `STK-012` (Claude Sonnet) | Wajib lolos 100% regression testing logic. |
| **`chore/<deskripsi>`** | Pemeliharaan berkas konfigurasi, ignore list, requirements.txt, or seed.sql. | `STK-014` (GPT-OSS) / Developer terkait | Penggabungan normal. |

### 4.4. Konvensi Penamaan Branch

| Tipe | Format Penamaan | Contoh Benar (✅) | Contoh Salah (❌) |
|:---|:---|:---|:---|
| **Feature** | `feature/modul-<nama-modul-singkat>` | `feature/modul-transaksi` | `feature/M1-Transaksi-Baru` |
| **Bugfix** | `bugfix/<nama-fitur-terkait>` | `bugfix/stok-minus-opname` | `bugfix/stok-error` |
| **Hotfix** | `hotfix/<deskripsi-singkat-darurat>` | `hotfix/jwt-expire-crash` | `hotfix/maling-stok` |
| **Docs** | `docs/<nama-dokumen-singkat>` | `docs/git-workflow` | `docs/workflowgit` |
| **Refactor**| `refactor/<modul-dan-bagian>` | `refactor/db-connector-pool` | `refactor/perapihan-kode` |
| **Chore** | `chore/<deskripsi-tugas>` | `chore/update-requirements` | `chore/requirements` |

### 4.5. Aturan Proteksi Branch (Branch Protection Rules)
1.  `[DILARANG]` Melakukan modifikasi langsung, commit mentah, or force-push (`git push --force`) pada branch `main`.
2.  `[WAJIB]` Setiap proses penggabungan branch fitur ke `main` wajib berstatus bebas konflik (*conflict-free*).
3.  `[WAJIB]` Setiap merge ke `main` wajib dilampiri review persetujuan dari Gemini 3 Flash (`STK-011`) dan ditandatangani manual oleh pemilik (`STK-000`).

### 4.6. Siklus Hidup Branch (Branch Lifecycle)
1.  **Dibuat**: Branch fitur diturunkan langsung dari status commit `main` terbaru (`git checkout -b feature/modul-x main`).
2.  **Koding & Commit**: Pengembang melakukan pengerjaan, commit berkala di branch fitur, dan push ke server testing LAN.
3.  **Merge & Hapus**: Setelah branch fitur disetujui, pemilik melakukan merge ke `main` menggunakan kebijakan `--no-ff`. Branch fitur lokal dan remote wajib **langsung dihapus** (`git branch -d feature/modul-x`) untuk menjaga codebase tetap rapi.

---

## 5. Konvensi Commit

### 5.1. Format Commit Message (Conventional Commits)
Setiap pesan commit wajib ditulis terstruktur menggunakan format **Conventional Commits** standar industri dalam bahasa Indonesia profesional:
```
<type>(<scope>): <description>

[Optional Body]

[Optional Footer / Co-authored attribution]
```

### 5.2. Daftar Tipe Commit yang Diizinkan

| Tipe Commit | Kategori / Tanggung Jawab Perubahan | Contoh Pesan Commit (Bahasa Indonesia) |
|:---:|:---|:---|
| **`feat`** | Penambahan fungsionalitas bisnis baru. | `feat(transaksi): tambah kalkulasi harga grosir M1` |
| **`fix`** | Perbaikan bug, kesalahan logika, or celah keamanan. | `fix(sdm): koreksi pembulatan pembagian gaji UMR M4` |
| **`docs`** | Pembaruan draf dokumen SDLC or inline docstrings Python.| `docs(sdlc): susun spesifikasi git workflow v1.0` |
| **`chore`** | Pemeliharaan config, .gitignore, dependencies, DDL. | `chore(config): tambah dependensi cryptography di requirements` |
| **`test`** | Pembuatan or perbaikan unit/integration tests suite. | `test(inventaris): tambah unit test logic bom hpp` |
| **`refactor`**| Restrukturisasi kode tanpa merubah logika luar. | `refactor(db): optimasi connection pool factory db_connector` |
| **`style`** | Whitespace, formatting PEP 8, without logic changes. | `style(cli): perbaiki indentasi panel menu transaksi` |
| **`perf`** | Peningkatan efisiensi waktu eksekusi kode. | `perf(keuangan): kompresi pemrosesan query laba rugi instan` |
| **`revert`** | Membatalkan / me-rollback commit sebelumnya. | `revert: batalkan commit feat transaksi grosir` |
| **`ci`** | Perubahan konfigurasi alur integrasi CI/CD. | `ci: tambah script test checking linter` |
| **`build`** | Perubahan sistem build, setup wheels offline. | `build: setup local deb package installer` |

### 5.3. Aturan Scope Commit
Scope commit mendefinisikan bagian modul logis mana yang dimodifikasi. Pengembang **MUST** menggunakan salah satu dari 14 scope resmi berikut (sesuai Module Structure R-03):
`transaksi`, `inventaris`, `ppob`, `sdm`, `antrian`, `keuangan`, `keamanan`, `crm`, `cabang`, `config`, `db`, `cli`, `middleware`, `utils`.

### 5.4. Aturan Deskripsi Commit
*   Menggunakan huruf kecil di awal deskripsi (kecuali nama singkatan standard).
*   Menggunakan kata kerja bernada *imperative* (perintah) dalam bahasa Indonesia (misal: `tambah`, `koreksi`, `hapus`, `optimasi`, bukan *menambah*, *memperbaiki*).
*   Panjang deskripsi baris pertama maksimal **72 karakter** demi keterbacaan split-screen.

### 5.5. Aturan Body dan Footer Commit (Opsional)
*   **Body**: Menjelaskan konteks "mengapa" perubahan dilakukan dan "bagaimana" cara kerjanya jika kompleks.
*   **Footer**: Merekam pemutusan breaking changes (`BREAKING CHANGE:`) or referensi issue terkait (misal: `Resolves: #0041`).
*   **Co-authored-by**: Atribusi wajib untuk AI (Detail di Bab 12).

### 5.6. Contoh Commit Message Lengkap (Benar vs Salah)

| Contoh Benar (✅) | Contoh Salah (❌) | Alasan Penolakan Salah |
|:---|:---|:---|
| `feat(transaksi): tambah uang muka DP pesanan kustom` | `Menambahkan fitur DP di menu kasir` | Tanpa tipe semantic, bahasa non-imperative, tidak ada scope. |
| `fix(sdm): koreksi sisa kasbon potong payroll` | `FIX BUG GAJI KASIR` | Huruf kapital penuh, tanpa scope, deskripsi tidak deskriptif. |
| `docs(sdlc): draft git workflow` | `docs: up` | Deskripsi terlalu pendek, scope tidak didefinisikan. |
| `chore(db): migrasi schema sql InnoDB` | `update schema.sql` | Tanpa tipe semantic, format berantakan. |

### 5.7. Aturan Atomisitas Commit (Atomic Commits)
Setiap commit **MUST** merepresentasikan **satu perubahan logis tunggal yang utuh**. Dilarang keras menggabungkan dua fitur yang berbeda (misal: perbaikan absensi M.4 and input opname M.2) di dalam satu commit yang sama karena menyulitkan proses rollback darurat.

---

## 6. Alur Kerja Pengembangan (Development Workflow)

### 6.1. Diagram Alur Kerja Lengkap (Mermaid — Flowchart)

```mermaid
flowchart TD
    A[Start: Tugas Baru Ditugaskan] --> B[Tarik commit main terbaru dari server LAN]
    B --> C[Buat branch baru: feature/modul-x]
    C --> D[Konstruksi Kode Pure FP & Type Hints lengkap]
    D --> E[Lakukan Commit Atomis ter-Conventional Commits]
    E --> F[Jalankan Unit Testing lokal: unittest / pytest]
    F --> G{Apakah Unit Test Lolos & Coverage >= 90%?}
    G -->|Tidak| D
    G -->|Ya| H[Push Branch Fitur ke Server local LAN]
    H --> I[Picu Gemini 3 Flash: Cek Kepatuhan Coding Standard R-01]
    I --> J{Apakah Lolos Linter & Coding Standard?}
    J -->|Tidak| D
    J -->|Ya| K[Pemilik Toko review manual & Verifikasi Fisik]
    K --> L{Apakah Disetujui Pemilik?}
    L -->|Tidak| D
    L -->|Ya| M[Merge ke main menggunakan --no-ff]
    M --> N[Hapus Branch Fitur & Rilis Versi Tag Baru]
    N --> O[End: Tugas Selesai]
```

### 6.2. Langkah-Langkah Detail Alur Kerja
1.  **Sinkronisasi**: Pastikan branch `main` lokal Anda sinkron dengan server database LAN.
    `git checkout main && git pull`
2.  **Isolasi**: Buat branch fitur baru yang representatif.
    `git checkout -b feature/modul-inventaris`
3.  **Koding & Commit**: Terapkan pure fungsional murni Python 3.14.2+, selaraskan mapping data desimal, type hints, docstring PEP 257. Commit secara berkala dengan Conventional Commits.
4.  **Verifikasi Lokal**: Jalankan pengujian unittest fungsional, ukur code coverage logic minimal 90%.
5.  **Quality Check**: Minta review otomatis dari Gemini 3 Flash, disusul review visual pemilik.
6.  **Integrasi**: Gabungkan branch fitur dan berikan tag rilis.

### 6.3. Alur Kerja untuk Penambahan Fitur Baru (Feature Workflow)
Wajib mematuhi alur step-by-step di atas secara kaku. Semua file logic bisnis baru dilarang ditaruh langsung di root folder melainkan diletakkan rapi pada folder layer-nya (misal `logic/` or `cli/`).

### 6.4. Alur Kerja untuk Perbaikan Bug (Bugfix Workflow)
1.  Buat branch perbaikan dari main terbaru: `git checkout -b bugfix/stok-opname-minus`.
2.  Perbaiki kode logika, buat unit test baru khusus untuk menangkap kasus edge case tersebut.
3.  Commit dengan tipe `fix`, jalankan review, dan merge kembali ke main.

### 6.5. Alur Kerja untuk Perbaikan Darurat (Hotfix Workflow)
1.  Ditransmisikan saat server produksi offline di toko mengalami crash fatal.
2.  Buka branch hotfix: `git checkout -b hotfix/jwt-signature-key`.
3.  Perbaiki nilai parameter rahasia di `.env` (atau perbaikan middleware).
4.  Commit `fix(keamanan): perbaiki token validation`, merge langsung ke main, dan tag sebagai patch rilis.

### 6.6. Alur Kerja untuk Pembaruan Dokumentasi (Docs Workflow)
1.  Turunkan branch dokumentasi: `git checkout -b docs/audit-logs`.
2.  Edit file `.md` terkait di folder `docs/`.
3.  Commit `docs(sdlc): perbarui tabel audit logs`, merge ke main.

---

## 7. Strategi Merge dan Conflict Resolution

### 7.1. Kebijakan Merge (Merge Policy)
Sistem AbuCom menerapkan kebijakan **Merge Commit non-fast-forward (`--no-ff`)** untuk setiap penggabungan branch fitur ke branch utama.
*   **Justifikasi**: Kebijakan `--no-ff` memaksa Git untuk selalu membuat commit merger baru. Hal ini sangat penting untuk menjaga keterbacaan pohon sejarah repositori (*history graph*) secara terstruktur, sehingga Junior Programmer dapat melacak kapan satu fitur modul spesifik diintegrasikan secara utuh.
*   `[DILARANG]` Menggunakan perintah rebase (`git rebase`) pada branch bersama karena merusak integritas garis waktu kontribusi AI.

### 7.2. Prosedur Merge Branch Fitur ke Main
Saat penggabungan siap dieksekusi oleh Pemilik Toko (`STK-000`):
```bash
# Pindah ke branch main
git checkout main

# Pastikan main lokal terupdate
git pull origin main

# Lakukan penggabungan dengan mematikan fast-forward
git merge --no-ff feature/modul-inventaris -m "chore(db): gabungkan modul inventaris M2"
```

### 7.3. Prosedur Penanganan Merge Conflict
Jika dua pengembang AI mengubah baris file Python yang sama dan memicu *Merge Conflict*:
1.  Sistem Git akan menghentikan proses merge dan menandai bagian file yang konflik menggunakan tag `<<<<<<< HEAD` dan `>>>>>>>`.
2.  Programer manusia (Junior Programmer) **MUST** turun tangan secara langsung melakukan resolusi konflik secara manual menggunakan editor kode.
3.  Pilih logika kode fungsional yang paling patuh terhadap Coding Standard (prioritaskan imutabilitas data dan presisi desimal `ROUND_HALF_UP`).
4.  Simpan file hasil resolusi, bersihkan terminal, tambahkan file ke area staging, dan selesaikan commit merge:
    ```bash
    git add logic/bom_hpp.py
    git commit -m "fix(conflict): resolusi konflik penggabungan stok desimal M2"
    ```

### 7.4. Diagram Alur Resolusi Konflik (Mermaid)

```mermaid
flowchart TD
    A[Sistem Git mendeteksi Merge Conflict] --> B[Hentikan proses merge otomatis]
    B --> C[Junior Programmer buka file konflik di IDE]
    C --> D[Cari blok tanda <<<<<<< HEAD dan >>>>>>>]
    D --> E[Komparasikan baris logika yang bertabrakan]
    E --> F{Logika mana yang patuh Coding Standard?}
    F -->|Logic A murni FP| G[Pilih baris Logic A, hapus penanda konflik Git]
    F -->|Logic B mutable| H[Ganti Logic B menjadi fungsional murni & pilih]
    G --> I[Simpan file ter-resolusi]
    H --> I
    I --> J[Jalankan git add <file>]
    J --> K[Jalankan git commit untuk selesaikan merger commit]
    K --> L[Lakukan pengujian unit test ulang]
    L --> M[Selesai]
```

### 7.5. Aturan Pencegahan Konflik (Preventive Rules)
1.  **Sering Pull**: Lakukan sinkronisasi `git pull` secara berkala sebelum memulai menulis baris kode baru.
2.  **Scope Terisolasi**: Batasi modifikasi file hanya pada matriks tanggung jawab modul Anda (Sesuai Bab 13 Module Structure R-03). Jangan menyentuh file milik modul lain tanpa izin.
3.  **Koordinasi AI**: Model-model AI wajib membaca status branch aktif sebelum meluncurkan pengerjaan.

---

## 8. Code Review dan Quality Gate

### 8.1. Prosedur Code Review Sebelum Merge
Setiap branch fitur yang telah diselesaikan wajib melalui tinjauan kode (*code review*) di repositori lokal LAN sebelum diperbolehkan menyatu ke `main`:
1.  Developer AI memicu pengajuan tinjauan ke Junior Programmer.
2.  Tinjauan otomatis dijalankan terlebih dahulu untuk menyaring kesalahan sintaksis kasat mata.
3.  Pemilik Toko melakukan review visual akhir secara manual pada berkas diff perubahan.

### 8.2. Peran Reviewer dalam Tim AbuCom
*   **Reviewer Otomatis (Gemini 3 Flash — `STK-011`)**: Bertanggung jawab mengecek kepatuhan sintaksis terhadap Coding Standard R-01, mendeteksi jika ada pendefinisian `class` ilegal, mengecek presisi desimal uang, and memfilter credentials hardcoded.
*   **Reviewer Akhir (Junior Programmer — `STK-000`)**: Pemilik toko memverifikasi kecocokan fungsi terhadap workflow operasional kasir fisik dan menandatangani persetujuan merger.

### 8.3. Checklist Code Review (Pre-Merge Checklist)
Setiap tinjauan wajib memastikan 12 checklist dari Coding Standard (R-01 Bab 17) bernilai **YA**:
1.  `[WAJIB]` Bebas dari kata kunci `class` di alur bisnis utama (`logic/` terbebas dari OOP)?
2.  `[WAJIB]` Anotasi Type Hints PEP 484 dan docstring PEP 257 Args/Returns lengkap?
3.  `[WAJIB]` Komputasi nominal Rupiah & stok menggunakan `decimal.Decimal` dan pembulatan `ROUND_HALF_UP` eksplisit?
4.  `[WAJIB]` Query basis data MySQL menggunakan parameterized placeholders `%s`, bebas f-string?
5.  `[WAJIB]` Operasi multi-tabel dibungkus di dalam ACID transaction (commit/rollback) InnoDB?
6.  `[WAJIB]` Berkas rahasia `.env` telah dipastikan aman ter-ignore oleh berkas `.gitignore`?
7.  `[WAJIB]` Path berkas lokal dikelola menggunakan modul `pathlib` secara aman lintas OS?
8.  `[WAJIB]` CLI menggunakan rich panels dan tabulate tabular?
9.  `[WAJIB]` Berjalan Dual-OS (Windows CMD chcp 65001 & Linux Debian 12)?
10. `[WAJIB]` Seluruh dependencies dikunci versinya di requirements.txt?
11. `[WAJIB]` Code coverage logic test suite minimal 90%?
12. `[WAJIB]` Data pribadi nomor WhatsApp CRM terenkripsi simetris Fernet?

### 8.4. Kriteria Lulus Quality Gate
Suatu branch fitur dinyatakan **LULUS** quality gate dan layak digabungkan jika:
*   [x] 100% unit tests fungsional berstatus lolos (*pass*).
*   [x] Persentase jangkauan pengujian (*code coverage*) logic folder `logic/` &ge; 90%.
*   [x] Zero violation terhadap 12 checklist pre-merge.
*   [x] Sintaksis diagram alur Mermaid dinyatakan valid.

---

## 9. Strategi Tagging dan Versioning

### 9.1. Standar Semantic Versioning (SemVer)
Sistem rilis aplikasi AbuCom mematuhi standar **Semantic Versioning (SemVer)** dengan format penamaan versi:
`v<MAJOR>.<MINOR>.<PATCH>`
*   **MAJOR**: Rilis versi besar yang memuat perubahan arsitektur dasar masif (misal migrasi database dari offline ke multi-cabang terintegrasi online).
*   **MINOR**: Rilis penambahan modul fungsional baru (misal M.3 PPOB selesai).
*   **PATCH**: Rilis perbaikan bug darurat (*hotfix*) yang tidak merubah fungsi bisnis luar.

### 9.2. Konvensi Penamaan Tag
Setiap tag Git wajib diawali huruf kecil `v` diikuti digit SemVer:
*   *Contoh rilis produksi*: `v1.0.0`, `v1.1.0`, `v1.1.2`.
*   *Contoh rilis beta/development*: `v1.0.0-beta.1`.

### 9.3. Kapan Membuat Tag Baru
*   **Tag Minor/Major**: Dibuat setiap akhir siklus Sprint (2 mingguan) saat satu modul fungsional dinyatakan lulus uji QA dan siap dideploy ke PC kasir toko.
*   **Tag Patch**: Dibuat seketika setelah hotfix darurat selesai digabungkan ke `main`.

### 9.4. Prosedur Pembuatan Tag Release
Pembuatan tag release dieksekusi eksklusif oleh Pemilik Toko (`STK-000`) pada branch main:
```bash
# Pindah ke main
git checkout main

# Buat tag ber-annotated pesan formal
git tag -a v1.1.0 -m "release: modul transaksi M1 dan CRM M8 stabil siap pakai"

# Tampilkan daftar tag aktif
git tag -n
```

---

## 10. Pengelolaan File Sensitif dan Keamanan Git

### 10.1. Daftar File yang WAJIB Dikecualikan (.gitignore)
Untuk mencegah kebocoran credentials rahasia ke repositori bersama, file-file berikut **MUST NOT** di-track oleh Git:
*   `.env` (Credentials produksi).
*   `.env.test` (Credentials testing).
*   `venv/` (Virtual environment lokal).
*   `__pycache__/` (Cache compile Python).
*   `*.log` (Log aplikasi).
*   `exports/backups/*.zip` (Cadangan database riil terenkripsi).
*   `exports/receipts/*.txt` (Nota belanja kasir fisik).

### 10.2. Daftar File yang WAJIB Di-track
File-file administrasi baseline berikut **WAJIB** masuk ke repositori Git:
*   `requirements.txt` (Kunci library).
*   `.env.example` (Templat kosong `.env`).
*   `.gitignore` (Ignore rules).
*   `.gitattributes` (Line ending settings).
*   `schema.sql` (Migrasi skema database).
*   `seed.sql` (Data inisial master).

### 10.3. Prosedur Darurat Jika Kredensial Tercommit
Jika terjadi kecelakaan di mana file rahasia `.env` (atau kata sandi database riil) tidak sengaja tercommit ke riwayat Git:
1.  **Rotasi Seketika**: Ganti kata sandi database MySQL root, user `abucom_app` di server Debian, dan generate ulang Fernet key serta secret key JWT di `.env` lokal.
2.  **Pembersihan Riwayat Repositori**:
    Gunakan utilitas `git-filter-repo` (atau BFG Repo-Cleaner) untuk menghapus file secara permanen dari seluruh sejarah commit Git agar tidak bisa ditarik kembali:
    ```bash
    git filter-branch --force --index-filter \
    "git rm --cached --ignore-unmatch .env" \
    --prune-empty --tag-name-filter cat -- --all
    ```
3.  **Catat Insiden**: Rekam kejadian bocornya credentials ke log audit manual pemilik dengan status `'SECURITY_BREACH_RESOLVED'`.

> ⚠️ **[DATA KOSONG — PERLU DIISI MANUAL]**: Prosedur darurat pembersihan riwayat Git menggunakan `git filter-branch` di atas belum pernah didokumentasikan di SDLC sebelumnya. Pemilik Toko wajib memastikan tools `git-filter-repo` terinstal offline pada PC kasir untuk kebutuhan penanggulangan darurat.

### 10.4. Aturan Perlindungan Rahasia (.env, JWT Key, Fernet Key)
Dilarang keras menuliskan credentials, pass database, secret key JWT, or Fernet key UU PDP secara hardcoded (string statis) di dalam file Python. Seluruh rahasia wajib dipanggil dinamis via `os.environ` menggunakan perantara casting `config/settings.py` (R-03 Bab 8.2).

---

## 11. Prosedur Backup dan Recovery Repository

### 11.1. Strategi Backup Repository Git Lokal
Karena proyek AbuCom berjalan offline LAN luring tanpa server cloud eksternal (AWS/GCP ditolak di R-04 Bab 6.3), pencadangan repositori Git dilakukan secara berkala pada media fisik eksternal:
1.  Pencadangan dilakukan setiap akhir hari operasional toko (pukul 21:00 WIB) setelah proses *shift handover* kasir selesai.
2.  Gunakan perintah `git bundle` untuk membuat salinan file tunggal (*bundle file*) yang memampatkan seluruh riwayat commit repositori secara utuh.

### 11.2. Prosedur Clone/Mirror ke Media Eksternal
1.  Hubungkan USB Flashdisk khusus backup milik pemilik (terformat NTFS/ext4) ke PC Kasir.
2.  Jalankan perintah pembuatan bundle Git di root proyek:
    ```bash
    git bundle create exports/backups/abucom_repo_backup.bundle --all
    ```
3.  Salin file `abucom_repo_backup.bundle` tersebut ke dalam USB Flashdisk eksternal.
4.  Batasi wewenang fisik flashdisk backup, simpan di brankas terkunci toko.

### 11.3. Prosedur Recovery Repository dari Backup
Jika PC Kasir Utama mengalami kerusakan SSD fatal:
1.  Pasang sistem operasi Windows 11 baru, instal runtime Python 3.14.2+ dan Git.
2.  Hubungkan USB Flashdisk backup pemilik.
3.  Lakukan restorasi repositori menggunakan clone langsung dari berkas bundle:
    ```bash
    git clone C:/path/to/flashdisk/abucom_repo_backup.bundle C:/Users/donsise/Documents/abucom
    ```
4.  Repositori Git akan kembali pulih 100% beserta seluruh sejarah commit dan branch-nya.

> ⚠️ **[DATA KOSONG — PERLU DIISI MANUAL]**: Strategi backup repositori Git menggunakan `git bundle` luring ke media flashdisk di atas merupakan data baru yang ditambahkan berdasarkan best practice luring. Pemilik Toko wajib menyiapkan 2 unit USB Flashdisk khusus (kapasitas min 32GB) yang dilabeli secara fisik untuk cadangan harian.

---

## 12. Panduan Git untuk Tim Campuran (Manusia + AI)

### 12.1. Konvensi Identitas Git untuk Setiap Model AI
Untuk memelihara audit kepemilikan kode program yang dihasilkan, setiap model AI pengembang wajib menggunakan konfigurasi identitas Git (name & email) yang unik dan konsisten sesuai profil peran mereka:

| Model AI | Nama Pengembang (Git `user.name`) | Alamat Email Git (Git `user.email`) | Peran Khusus di Repositori |
|:---|:---|:---|:---|
| **Junior Programmer** (Owner) | `Junior Programmer` | ⚠️ `[HARUS DIISI MANUAL]` | Integrator Utama, Pengelola Rilis |
| **Gemini 3.1 Pro (High)** | `gemini-pro-high` | `gemini-pro-high@abucom.local` | Pembuat Logika Berat logic/ |
| **Gemini 3.1 Pro (Low)** | `gemini-pro-low` | `gemini-pro-low@abucom.local` | Routine Coder & Documenter |
| **Gemini 3 Flash** | `gemini-flash` | `gemini-flash@abucom.local` | Automated Linter & Tester |
| **Claude Sonnet 4.6 (Thinking)**| `claude-sonnet` | `claude-sonnet@abucom.local` | UI & CLI UI Specialist |
| **Claude Opus 4.6 (Thinking)** | `claude-opus` | `claude-opus@abucom.local` | Security Middleware Developer |
| **GPT-OSS 120B (Medium)** | `gpt-oss-medium` | `gpt-oss-medium@abucom.local` | Boilerplate & Seed DDL Provider |

> ⚠️ **[DATA KOSONG — PERLU DIISI MANUAL]**: Konvensi email dan identitas Git untuk model-model AI di atas belum didefinisikan secara baku pada SDLC terdahulu. Pemilik Toko wajib menyalin berkas config identitas AI ini ke sistem otomasi subagent masing-masing agar setiap commit terekam dengan atribusi yang valid.

### 12.2. Aturan Kolaborasi Branch Antar-AI
1.  `[DILARANG]` Dua model AI bekerja pada satu branch fitur yang sama secara simultan. Hal ini memicu merge conflict yang rumit.
2.  Setiap model AI wajib membuat sub-branch fitur sendiri untuk tugas spesifiknya (misal: `feature/modul-transaksi-cli` khusus untuk Claude Sonnet dan `feature/modul-transaksi-db` khusus untuk Gemini Pro High).
3.  Penggabungan antar sub-branch fitur dikelola secara formal menggunakan pull request lokal.

### 12.3. Aturan Atribusi Commit untuk Kontribusi AI (Co-authored-by)
Jika suatu fungsi Python dibangun secara kolaboratif (misal Claude Sonnet menulis logika CLI and Gemini Pro High menyempurnakan kalkulasi desimal HPP-nya), commit message wajib menyertakan trailer **`Co-authored-by:`** di bagian footer pesan commit untuk menghormati atribusi hak cipta biner AI:
```
feat(inventaris): selesaikan formula HPP stempel flash desimal

tambahkan penyesuaian volume cairan karet stempel flash di logic M2.

Co-authored-by: gemini-pro-high <gemini-pro-high@abucom.local>
Signed-off-by: Junior Programmer <donsise@example.com>
```

### 12.4. Prosedur Handover Pekerjaan Antar-AI via Git
Saat satu model AI menyelesaikan tugas dasar (misal GPT-OSS membuat boilerplate DDL database) dan perlu diserahterjemahkan ke model AI berikutnya (misal Claude Opus memasang rbac guard):
1.  Model AI pertama (`GPT-OSS`) wajib melakukan commit dan push branch fitur target ke repositori lokal:
    `git commit -m "chore(db): initial boilerplate tables"` dan `git push`.
2.  Model AI pertama menuliskan berkas catatan status program (`handover_notes.txt`) di folder draf.
3.  Model AI kedua (`Claude Opus`) melakukan checkout branch tersebut, membaca `handover_notes.txt`, and melanjutkan konstruksi pengkodean aspek keamanan.

---

## 13. Perintah Git yang Sering Digunakan (Quick Reference)

### 13.1. Perintah Dasar Sehari-hari

| Perintah Git | Fungsi Utama | Contoh Penggunaan Aktual |
|:---|:---|:---|
| **`git status`** | Memeriksa status file (staged, unstaged, untracked). | `git status` |
| **`git add <file>`** | Menambahkan file spesifik ke area staging. | `git add logic/bom_hpp.py` |
| **`git commit -m "<msg>"`** | Merekam snapshot perubahan ke sejarah Git. | `git commit -m "feat(inventaris): add BOM HPP M2"`|
| **`git diff`** | Memeriksa perubahan baris kode sebelum commit. | `git diff logic/smart_payroll.py` |
| **`git log --oneline`** | Melihat daftar riwayat commit ringkas satu baris. | `git log --oneline -n 5` |

### 13.2. Perintah Branching dan Merge

| Perintah Git | Fungsi Utama | Contoh Penggunaan Aktual |
|:---|:---|:---|
| **`git branch`** | Menampilkan daftar branch lokal yang aktif. | `git branch` |
| **`git checkout -b <name>`**| Membuat branch baru dan langsung berpindah ke sana. | `git checkout -b feature/modul-transaksi` |
| **`git checkout <branch>`** | Berpindah ke branch target yang sudah ada. | `git checkout main` |
| **`git merge --no-ff <name>`**| Menggabungkan branch fitur dengan memaksa merge commit.| `git merge --no-ff feature/modul-transaksi` |
| **`git branch -d <name>`** | Menghapus branch lokal yang sudah tidak digunakan. | `git branch -d feature/modul-transaksi` |

### 13.3. Perintah Inspeksi dan Troubleshooting

| Perintah Git | Fungsi Utama | Contoh Penggunaan Aktual |
|:---|:---|:---|
| **`git log --graph`** | Melihat pohon riwayat commit secara visual grafis. | `git log --graph --oneline --all` |
| **`git reflog`** | Melacak sejarah pergerakan HEAD (penyelamat data). | `git reflog` |
| **`git stash`** | Menyimpan sementara perubahan unstaged agar branch bersih.| `git stash push -m "simpan kasir logic"` |
| **`git stash pop`** | Mengembalikan perubahan yang disimpan dari stash. | `git stash pop` |

### 13.4. Perintah Undo dan Recovery

| Perintah Git | Fungsi Utama | Contoh Penggunaan Aktual |
|:---|:---|:---|
| **`git checkout -- <file>`**| Membatalkan perubahan unstaged pada file spesifik. | `git checkout -- logic/bom_hpp.py` |
| **`git reset --soft HEAD~1`**| Membatalkan 1 commit terakhir, file kembali ke staged. | `git reset --soft HEAD~1` |
| **`git reset --hard HEAD~1`**| `[BAHAYA]` Menghapus mutlak 1 commit & perubahan file. | `git reset --hard HEAD~1` |
| **`git revert <commit-hash>`**| Membuat commit baru pembatalan commit target (aman). | `git revert a1b2c3d4` |

---

## 14. Larangan Mutlak (Prohibited Practices)

Praktik-praktik berikut **DILARANG KERAS (MUST NOT)** diimplementasikan oleh seluruh tim pengembang di dalam repositori Git AbuCom:

| No | Praktik yang DILARANG MUTLAK | Dampak Negatif Kritis | Solusi / Standar yang Benar |
|:---:|:---|:---|:---|
| 1 | Melakukan push langsung ke branch `main`. | Codebase produksi tidak stabil, berisiko merusak sistem laci kasir riil toko. | Wajib menggunakan branch `feature/` and melalui pre-merge quality gate. |
| 2 | Commit file rahasia `.env` or kata sandi db. | Kebocoran kunci rahasia finansial dan credentials database ke riwayat Git. | Wajib memasukkan `.env` ke ignore list `.gitignore` sejak awal. |
| 3 | Melakukan force-push (`git push --force`). | Merusak sejarah commit pengembang AI lain, menghapus sejarah kontribusi. | Dilarang keras. Gunakan penggabungan merge normal. |
| 4 | Commit file binary besar (PDF desain, zip backup).| Ukuran repositori membengkak secara eksponensial pada server offline LAN. | Wajib meletakkan data di folder `/exports/` yang di-ignore Git. |
| 5 | Menulis commit message tidak informatif ("fix").| Menyulitkan proses tracking bug dan audit forensik internal pemilik. | Wajib mengikuti standar Conventional Commits terstruktur. |
| 6 | Mengerjakan multi-fitur di satu branch. | Rollback darurat tidak bisa dilakukan secara atomik, kode berantakan. | Satu branch khusus untuk satu tugas modular use case. |
| 7 | Merge ke `main` tanpa proses code review. | Masuknya bug pembulatan desimal or OOP class ilegal ke codebase steril. | Wajib review otomatis Gemini 3 Flash dan tanda tangan Pemilik. |
| 8 | Force checkout menghapus merge conflict kasar. | Kehilangan baris logika transaksional ACID yang krusial untuk integritas database. | Selesaikan konflik secara manual dan teliti di editor kode. |

---

## 15. Checklist Kepatuhan Git Workflow

Staf pengembang dan pemilik toko **MUST** memastikan checklist berikut bernilai **YA** sebelum branch fitur diperbolehkan menyatu ke branch utama `main`:

*   [ ] **1.** Apakah branch fitur didelegasikan dari branch `main` terbaru dan dinamai sesuai konvensi prefix (misal `feature/modul-transaksi`)?
*   [ ] **2.** Apakah seluruh pesan commit pada branch fitur telah mematuhi standar *Conventional Commits* format semantic (misal `feat(transaksi): ...`)?
*   [ ] **3.** Apakah berkas rahasia `.env` dan `.env.test` telah dipastikan aman ter-ignore oleh berkas `.gitignore`?
*   [ ] **4.** Apakah berkas `.gitattributes` telah terbuat dan diatur untuk memaksa line ending LF lintas platform Dual-OS?
*   [ ] **5.** Apakah seluruh pengujian unit test fungsional pada folder `tests/` dinyatakan lolos 100% tanpa error?
*   [ ] **6.** Apakah persentase jangkauan pengujian (*code coverage*) logika bisnis utama di folder `logic/` telah mencapai minimal 90%?
*   [ ] **7.** Apakah review otomatis dari Gemini 3 Flash (`STK-011`) telah dipicu and menyatakan kode 100% patuh terhadap Coding Standard (zero violation)?
*   [ ] **8.** Apakah proses penggabungan branch dipastikan menggunakan kebijakan merge commit `--no-ff` (non-fast-forward)?
*   [ ] **9.** Apakah setiap commit yang dikerjakan secara kolaboratif telah mencantumkan atribusi `Co-authored-by` untuk model AI terkait?
*   [ ] **10.** Apakah branch fitur yang telah sukses digabungkan langsung dihapus secara lokal dan remote demi kebersihan repositori?

---

## 16. Referensi Dokumen

Berikut adalah daftar dokumen referensi formal versi 1.1 yang digunakan sebagai dasar penyusunan spesifikasi teknis Git Workflow ini:

| No | Kode Ref | Nama Dokumen Referensi | Path Relatif File | Versi | Prioritas | Peran / Relevansi Spesifik |
|:---:|:---:|:---|:---|:---:|:---:|:---|
| 1 | R-01 | **Coding Standard** | `docs/sdlc/04_implementation/01_coding_standard.md` | v1.1 | **PRIMER** | Sumber aturan Bab 15 (Version Control Git), Bab 16 (Larangan), Bab 17 (Checklist), serta standardisasi desimal. |
| 2 | R-02 | **Environment Setup** | `docs/sdlc/04_implementation/02_environment_setup.md` | v1.1 | **PRIMER** | Sumber spesifikasi Bab 9 (Setup Git lokal), Bab 8.5 (ignore rules), dan verifikasi credentials. |
| 3 | R-03 | **Module Structure** | `docs/sdlc/04_implementation/03_module_structure.md` | v1.1 | **SEKUNDER** | Peta direktori standar proyek, daftar 10 modul fungsional, and matriks pemetaan file untuk scope commit. |
| 4 | R-04 | **Tech Stack Decision**| `docs/sdlc/01_planning/04_tech_stack_decision.md` | v1.1 | **SEKUNDER** | Batasan runtime, locked requirements, dual-OS portabilitas, and spesifikasi asisten AI. |
| 5 | R-05 | **System Architecture**| `docs/sdlc/03_design/03_system_architecture.md` | v1.1 | **TERSIER** | Konfigurasi physical server, local LAN offline, connection pool size 5, dan repeatable read isolation level. |
| 6 | R-06 | **Security Design** | `docs/sdlc/03_design/06_security_design.md` | v1.1 | **TERSIER** | Keamanan credentials, enkripsi backups AES-256 ZIP, chmod 700 server, dan audit log JSON structure. |
| 7 | R-07 | **Narasi Pemilik** | `docs/sdlc/narasi.txt` | v1.1 | **TERSIER** | Konteks operasional, susunan tim campuran (Junior Programmer + 6 Model AI spesialis), dan kolaborasi luring. |
