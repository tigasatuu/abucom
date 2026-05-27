# Pembuatan dan Penyusunan Dokumen Environment Config

---

| Atribut Issue     | Detail                                                                |
|-------------------|-----------------------------------------------------------------------|
| **Judul**         | Pembuatan dan Penyusunan Dokumen Environment Config                   |
| **Tipe**          | Dokumentasi Teknis — Fase 06 Deployment                               |
| **Prioritas**     | 🔴 High                                                              |
| **Dokumen Utama** | Environment Config                                                    |
| **Target File**   | `docs/sdlc/06_deployment/02_environment_config.yaml`                  |
| **Persona**       | **Senior DevOps Engineer & Infrastructure Configuration Specialist**  |
| **Status**        | 🟡 Open — Menunggu Implementasi                                      |
| **Tanggal**       | 2026-05-27                                                            |

---

## 1. Deskripsi Issue

Issue ini berisi instruksi perencanaan low-level untuk membuat dan menyusun dokumen **Environment Config** dalam format YAML. Dokumen ini merupakan deliverable kedua pada **Fase 06 — Deployment** yang berfungsi sebagai **file konfigurasi referensi tunggal (Single Source of Configuration Truth)** untuk seluruh parameter, variabel lingkungan, kredensial, dan konfigurasi infrastruktur yang dibutuhkan dalam deployment sistem AbuCom CLI pada lingkungan produksi luring (offline LAN) toko percetakan fisik.

Dokumen Environment Config ini berbeda secara fundamental dari dokumen SDLC lainnya karena menggunakan **format YAML** (bukan Markdown), yang merupakan standar industri untuk file konfigurasi deklaratif pada sistem deployment dan operasional infrastruktur. YAML dipilih karena sifatnya yang *machine-readable* sekaligus *human-readable*, memungkinkan dokumen ini berfungsi ganda sebagai:
1. **Dokumen referensi teknis** yang bisa dibaca manusia (Junior Programmer / System Administrator).
2. **Blueprint konfigurasi** yang bisa diadaptasi langsung ke skrip otomasi deployment di masa depan.

---

## 2. Penentuan Persona Pelaksana

**Persona yang Ditugaskan**: **Senior DevOps Engineer & Infrastructure Configuration Specialist**

**Justifikasi Pemilihan Persona**:
- Persona ini memiliki otoritas dan keahlian tertinggi dalam hal konfigurasi infrastruktur, variabel lingkungan, parameter jaringan, kredensial keamanan, dan konfigurasi deployment lintas platform (Dual-OS: Linux Debian 12 & Windows 11).
- Dokumen Environment Config secara esensial adalah pemetaan seluruh parameter teknis operasional sistem, yang merupakan domain utama seorang DevOps Engineer.
- Persona ini mampu menjembatani aspek keamanan (hardening, firewall, enkripsi), aspek infrastruktur (jaringan LAN, IP statis, port), dan aspek aplikasi (runtime Python, dependensi, connection pool) ke dalam satu file konfigurasi YAML yang koheren.

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang dipilih sebagai sumber data utama dalam penyusunan dokumen ini. Setiap file dipilih berdasarkan relevansi langsung terhadap konten Environment Config:

| No | Kode Ref | Nama Dokumen Referensi | Path Relatif Berkas | Prioritas | Alasan Pemilihan Spesifik |
|:---:|:---:|---|---|:---:|---|
| 1 | **R-01** | Environment Setup v1.1 | `docs/sdlc/04_implementation/02_environment_setup.md` | **PRIMER** | Sumber data utama paling komprehensif untuk seluruh parameter konfigurasi: IP statis server, port database, variabel `.env`, requirements.txt versi terkunci, path direktori, konfigurasi firewall, MySQL bind-address, character set, isolation level, printer port, connection pool, dan troubleshooting. |
| 2 | **R-02** | Deployment Guide v1.1 | `docs/sdlc/06_deployment/01_deployment_guide.md` | **PRIMER** | Sumber data untuk parameter deployment produksi aktual: nilai `.env` produksi, konfigurasi cron backup, skrip `backup_cron.sh`, path shortcut peluncuran, hardening `/root/.my.cnf`, dan perbedaan lingkungan Development vs Staging vs Production. |
| 3 | **R-03** | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` | **PRIMER** | Sumber data untuk topologi jaringan LAN, spesifikasi hardware server/klien, arsitektur 4-layer, modul-to-table mapping, connection pooling `'abupool'` size 5, retry mechanism, dan diagram deployment fisik. |
| 4 | **R-04** | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | **PRIMER** | Sumber data untuk parameter keamanan: bcrypt cost factor 12, JWT HS256 secret key 32+ hex, lifetime 28800 detik, Fernet key CRM UU PDP, rate limiting 5x/lockout 10 menit, ufw rules, chmod 700, dan kode error keamanan. |
| 5 | **R-05** | Tech Stack Decision v1.1 | `docs/sdlc/01_planning/04_tech_stack_decision.md` | **PRIMER** | Sumber data untuk batasan mandatori runtime Python 3.14.2+, pustaka wajib (mysql-connector-python, python-dotenv, bcrypt, pyjwt), pustaka rekomendasi (rich, tabulate, cryptography), dan versi terkunci requirements.txt. |
| 6 | **R-06** | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` | **SEKUNDER** | Sumber data untuk layout tree direktori proyek standar, konvensi `.gitignore`, format `.env.example`, dan konvensi penamaan modul. |
| 7 | **R-07** | Database Schema v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | **SEKUNDER** | Sumber data untuk nama database produksi (`abucom_db`), database testing (`abucom_test_db`), jumlah tabel (28 tabel InnoDB), dan privilege user aplikasi. |
| 8 | **R-08** | Module Structure v1.1 | `docs/sdlc/04_implementation/03_module_structure.md` | **SEKUNDER** | Sumber data untuk struktur direktori modul CLI, layer separation, dan path file entry point. |
| 9 | **R-09** | Git Workflow v1.1 | `docs/sdlc/04_implementation/04_git_workflow.md` | **TERSIER** | Sumber data untuk konvensi branching, tagging rilis, dan commit message. |

> **Catatan**: File `narasi.txt` **TIDAK** lagi digunakan sebagai referensi karena seluruh informasi bisnis dan teknis yang relevan dari narasi sudah sepenuhnya terabsorpsi ke dalam dokumen-dokumen SDLC formal di atas. Menggunakan narasi akan menyebabkan duplikasi informasi dan potensi inkonsistensi.

---

## 4. Kerangka Struktur Dokumen Environment Config (YAML)

Berikut adalah kerangka struktur standar dokumen Environment Config YAML yang harus diikuti. Struktur ini mengadopsi standar praktik industri untuk file konfigurasi deployment infrastruktur:

```yaml
# ============================================================================
# ENVIRONMENT CONFIG — AbuCom
# Sistem Manajemen Terpadu Usaha Percetakan
# ============================================================================

# --- BAGIAN 1: METADATA DOKUMEN ---
metadata:
  dokumen: ...
  proyek: ...
  versi: ...
  tanggal: ...
  status: ...
  penyusun: ...
  deskripsi: ...
  posisi_sdlc: ...
  format: ...
  referensi_dokumen: [...]

# --- BAGIAN 2: KONFIGURASI LINGKUNGAN (ENVIRONMENTS) ---
environments:
  development:
    deskripsi: ...
    database: { ... }
    security: { ... }
    application: { ... }
    output: { ... }
    logging: { ... }
  staging:
    deskripsi: ...
    database: { ... }
    security: { ... }
    application: { ... }
    output: { ... }
    logging: { ... }
  production:
    deskripsi: ...
    database: { ... }
    security: { ... }
    application: { ... }
    output: { ... }
    logging: { ... }

# --- BAGIAN 3: KONFIGURASI INFRASTRUKTUR FISIK ---
infrastructure:
  network:
    topology: ...
    nodes:
      server: { ... }
      client: { ... }
    devices:
      switch: { ... }
      router: { ... }
      ups: [...]
  hardware:
    server_specs: { ... }
    client_specs: { ... }
    printer: { ... }

# --- BAGIAN 4: KONFIGURASI SISTEM OPERASI ---
operating_systems:
  server:
    os: ...
    hostname: ...
    users: [...]
    network_interface: { ... }
    firewall: { ... }
    ssh: { ... }
    directories: [...]
  client:
    os: ...
    terminal: { ... }
    security: { ... }
    path_env: [...]

# --- BAGIAN 5: KONFIGURASI DATABASE ---
database:
  engine: ...
  version: ...
  service: { ... }
  config_file: ...
  parameters: { ... }
  databases: [...]
  users: [...]
  privileges: { ... }
  schema_files: { ... }

# --- BAGIAN 6: KONFIGURASI RUNTIME PYTHON ---
python_runtime:
  version: ...
  installation:
    server: { ... }
    client: { ... }
  virtual_environment: { ... }
  dependencies:
    mandatory: [...]
    recommended: [...]
    development: [...]

# --- BAGIAN 7: KONFIGURASI APLIKASI ---
application:
  entry_point: ...
  directory_structure: { ... }
  env_template:
    variables: [...]
  env_example: |
    ...

# --- BAGIAN 8: KONFIGURASI KEAMANAN ---
security:
  authentication:
    bcrypt: { ... }
    jwt: { ... }
    rate_limiting: { ... }
  authorization:
    rbac_roles: [...]
  data_protection:
    fernet_crm: { ... }
    backup_encryption: { ... }
    uu_pdp_compliance: { ... }
  os_hardening:
    server: { ... }
    client: { ... }

# --- BAGIAN 9: KONFIGURASI BACKUP DAN RECOVERY ---
backup:
  schedule: { ... }
  encryption: { ... }
  retention: { ... }
  directories: { ... }
  cron_job: { ... }
  disaster_recovery: { ... }

# --- BAGIAN 10: KONFIGURASI VERSION CONTROL ---
version_control:
  system: ...
  identity: { ... }
  branching: { ... }
  commit_convention: { ... }
  gitignore: [...]
  tagging: { ... }

# --- BAGIAN 11: KONFIGURASI PRINTER DAN PERANGKAT ---
peripheral_devices:
  thermal_printer: { ... }
  cash_drawer: { ... }

# --- BAGIAN 12: KONFIGURASI CONNECTION POOL DAN RETRY ---
connection_management:
  pool: { ... }
  retry: { ... }

# --- BAGIAN 13: KONFIGURASI LOGGING DAN MONITORING ---
logging:
  audit_trail: { ... }
  backup_logs: { ... }
  system_logs: { ... }

# --- BAGIAN 14: KONFIGURASI TESTING ---
testing:
  framework: { ... }
  coverage: { ... }
  sandbox: { ... }

# --- BAGIAN 15: KODE ERROR DAN TROUBLESHOOTING ---
error_codes:
  authentication: [...]
  session: [...]
  database: [...]
  file: [...]
  cash: [...]
troubleshooting:
  common_issues: [...]

# --- BAGIAN 16: PARAMETER OPERASIONAL HARIAN ---
operations:
  startup_sop: { ... }
  shutdown_sop: { ... }
  maintenance: { ... }
  escalation: { ... }

# --- BAGIAN 17: REFERENSI DOKUMEN ---
references: [...]
```

---

## 5. Instruksi Implementasi Step-by-Step

### Tahap 1: Persiapan dan Pembacaan File Referensi

> **PENTING**: Baca SELURUH isi file referensi secara lengkap dari baris pertama hingga baris terakhir. Jangan skip atau melewatkan bagian apapun. Setiap detail parameter, nilai konfigurasi, dan spesifikasi teknis yang ada di dalam file referensi harus dirangkum dan dicatat.

- [ ] **1.1.** Baca file referensi **R-01** (`docs/sdlc/04_implementation/02_environment_setup.md`) secara lengkap dari awal hingga akhir. Catat dan rangkum semua informasi berikut:
  - [ ] 1.1.1. Seluruh spesifikasi hardware (server dan klien) beserta detailnya (prosesor, RAM, SSD, port jaringan).
  - [ ] 1.1.2. Seluruh konfigurasi jaringan (IP statis server `192.168.1.200`, gateway, subnet, nama interface).
  - [ ] 1.1.3. Seluruh konfigurasi firewall ufw (rules port 22, port 3306, kebijakan default).
  - [ ] 1.1.4. Seluruh konfigurasi SSH (PermitRootLogin, restart service).
  - [ ] 1.1.5. Seluruh konfigurasi MySQL (bind-address, character set, collation, transaction isolation level, port).
  - [ ] 1.1.6. Seluruh detail database (nama database produksi, testing, user aplikasi, privilege).
  - [ ] 1.1.7. Seluruh variabel `.env.example` dengan nama variabel, deskripsi, dan nilai contoh.
  - [ ] 1.1.8. Seluruh dependensi Python dengan versi terkunci (mandatory, recommended, development).
  - [ ] 1.1.9. Seluruh konfigurasi virtual environment (path, aktivasi Windows/Linux).
  - [ ] 1.1.10. Seluruh konfigurasi Git (identity, branching, commit convention, `.gitignore` entries).
  - [ ] 1.1.11. Seluruh konfigurasi printer thermal (port, width, driver type).
  - [ ] 1.1.12. Seluruh konfigurasi UPS (parameter BATTERYLEVEL, MINUTES, service apcupsd).
  - [ ] 1.1.13. Seluruh konfigurasi router MikroTik (DHCP lease, static bind IP).
  - [ ] 1.1.14. Seluruh konfigurasi backup (direktori, enkripsi AES-256, chmod 700).
  - [ ] 1.1.15. Seluruh konfigurasi testing (database sandbox, `.env.test`, pytest, coverage).
  - [ ] 1.1.16. Seluruh informasi connection pool (`abupool`, size 5, retry mechanism).
  - [ ] 1.1.17. Seluruh helper functions (handle_null_decimal, round_decimal_standard ROUND_HALF_UP).
  - [ ] 1.1.18. Seluruh konfigurasi Windows Terminal (chcp 65001, CMD profile).
  - [ ] 1.1.19. Seluruh konfigurasi keamanan klien (akun Standard User, disable USB AutoRun registry).
  - [ ] 1.1.20. Seluruh layout struktur direktori proyek standar (tree folder lengkap).

- [ ] **1.2.** Baca file referensi **R-02** (`docs/sdlc/06_deployment/01_deployment_guide.md`) secara lengkap dari awal hingga akhir. Catat dan rangkum semua informasi berikut:
  - [ ] 1.2.1. Seluruh perbedaan konfigurasi antar lingkungan (Development vs Staging vs Production).
  - [ ] 1.2.2. Seluruh nilai `.env` produksi konkret yang tercantum (APP_ENV, DB_HOST, JWT_SECRET_KEY, dll).
  - [ ] 1.2.3. Seluruh konfigurasi cron job backup harian (jadwal `0 21 * * *`, path skrip, log file).
  - [ ] 1.2.4. Seluruh isi skrip `backup_cron.sh` (mysqldump, zip enkripsi, rotasi 30 hari, chmod 600).
  - [ ] 1.2.5. Konfigurasi hardening `/root/.my.cnf` (chmod 600, isi konfigurasi client).
  - [ ] 1.2.6. Seluruh konfigurasi shortcut peluncuran aplikasi kasir Windows.
  - [ ] 1.2.7. Seluruh parameter smoke test (ST-01 s.d ST-06).
  - [ ] 1.2.8. Seluruh SOP runbook operasional harian (startup, shutdown, maintenance).
  - [ ] 1.2.9. Seluruh konfigurasi rollback (database restore, git revert, .env.bak).
  - [ ] 1.2.10. Seluruh parameter matriks risiko deployment (RSK-01 s.d RSK-08).
  - [ ] 1.2.11. Seluruh parameter retensi dan rotasi backup (harian 30 hari, bulanan 12 bulan).
  - [ ] 1.2.12. Seluruh konfigurasi disaster recovery (hardware pengganti, path restore).
  - [ ] 1.2.13. Seluruh kontak eskalasi dan waktu layanan darurat.

- [ ] **1.3.** Baca file referensi **R-03** (`docs/sdlc/03_design/03_system_architecture.md`) secara lengkap dari awal hingga akhir. Catat dan rangkum semua informasi berikut:
  - [ ] 1.3.1. Seluruh diagram topologi jaringan dan matriks node komponen.
  - [ ] 1.3.2. Seluruh spesifikasi hardware lengkap (server, klien, switch, router, UPS, printer).
  - [ ] 1.3.3. Seluruh konfigurasi OS server dan klien.
  - [ ] 1.3.4. Strategi portabilitas lintas OS (pathlib, encoding UTF-8, OS detection).
  - [ ] 1.3.5. Seluruh arsitektur 4-layer (presentation, logic, data access, persistence).
  - [ ] 1.3.6. Seluruh pemetaan modul-to-table database (10 modul, 28 tabel).
  - [ ] 1.3.7. Seluruh konfigurasi connection pool dan retry mechanism.
  - [ ] 1.3.8. Seluruh strategi data (ACID, decimal DECIMAL(15,4), multi-branch cabang_id).
  - [ ] 1.3.9. Seluruh arsitektur keamanan (7 layer defense in depth).

- [ ] **1.4.** Baca file referensi **R-04** (`docs/sdlc/03_design/06_security_design.md`) secara lengkap dari awal hingga akhir. Catat dan rangkum semua informasi berikut:
  - [ ] 1.4.1. Seluruh parameter otentikasi (bcrypt cost factor 12, salt dinamis 16-byte).
  - [ ] 1.4.2. Seluruh parameter JWT (HS256, secret key 32+ hex, lifetime 28800 detik, payload fields).
  - [ ] 1.4.3. Seluruh parameter rate limiting (5 kali gagal, lockout 10 menit, kolom tabel pengguna).
  - [ ] 1.4.4. Seluruh aturan RBAC (8 peran, matriks akses modul, eskalasi supervisor).
  - [ ] 1.4.5. Seluruh parameter proteksi data (Fernet key CRM, AES-256 backup, UU PDP compliance).
  - [ ] 1.4.6. Seluruh kode error keamanan (ERR-AUTH, ERR-SESSION, ERR-DB, ERR-FILE, ERR-CASH).
  - [ ] 1.4.7. Seluruh parameter shift handover (threshold selisih kas Rp 10.000).
  - [ ] 1.4.8. Seluruh parameter deteksi anomali fraud.
  - [ ] 1.4.9. Seluruh parameter retensi log audit (12 bulan).
  - [ ] 1.4.10. Seluruh SOP respon insiden keamanan.

- [ ] **1.5.** Baca file referensi **R-05** (`docs/sdlc/01_planning/04_tech_stack_decision.md`) secara lengkap dari awal hingga akhir. Catat dan rangkum semua informasi berikut:
  - [ ] 1.5.1. Seluruh batasan mandatori teknologi (Python 3.14.2+, FP murni, MySQL, pustaka wajib).
  - [ ] 1.5.2. Seluruh prinsip arsitektur panduan (7 prinsip).
  - [ ] 1.5.3. Seluruh pustaka standar Python yang dimanfaatkan (decimal, functools, itertools, dll).
  - [ ] 1.5.4. Seluruh matriks dependensi (versi, lisensi, fungsi, kategori).
  - [ ] 1.5.5. Seluruh konfigurasi arsitektur Client-Server LAN.
  - [ ] 1.5.6. Seluruh strategi requirements.txt.

- [ ] **1.6.** Baca file referensi **R-06** (`docs/sdlc/04_implementation/01_coding_standard.md`) secara lengkap. Catat:
  - [ ] 1.6.1. Layout tree direktori proyek standar lengkap.
  - [ ] 1.6.2. Isi template `.gitignore`.
  - [ ] 1.6.3. Format `.env.example`.
  - [ ] 1.6.4. Konvensi penamaan modul dan file.

- [ ] **1.7.** Baca file referensi **R-07** (`docs/sdlc/03_design/01_database_schema.sql`) secara lengkap. Catat:
  - [ ] 1.7.1. Nama database produksi dan testing.
  - [ ] 1.7.2. Jumlah dan daftar nama 28 tabel InnoDB.
  - [ ] 1.7.3. Nama user database aplikasi dan host-nya.

- [ ] **1.8.** Baca file referensi **R-08** (`docs/sdlc/04_implementation/03_module_structure.md`) secara lengkap. Catat:
  - [ ] 1.8.1. Struktur direktori modul CLI lengkap.
  - [ ] 1.8.2. Path file entry point aplikasi.

- [ ] **1.9.** Baca file referensi **R-09** (`docs/sdlc/04_implementation/04_git_workflow.md`) secara lengkap. Catat:
  - [ ] 1.9.1. Konvensi branching (feature branching, main).
  - [ ] 1.9.2. Konvensi tagging rilis (format tag, misal `v1.0.0`).
  - [ ] 1.9.3. Konvensi commit message (Conventional Commits).

---

### Tahap 2: Penyaringan dan Klasifikasi Data

- [ ] **2.1.** Setelah seluruh data dirangkum dari 9 file referensi, lakukan penyaringan (*filtering*). Hanya ambil data dan informasi yang **spesifik** berkaitan dengan konfigurasi lingkungan, parameter infrastruktur, variabel runtime, dan setting deployment. Buang informasi yang bersifat narasi prosedural murni (langkah-langkah instalasi step-by-step) karena itu sudah tercakup di dokumen Environment Setup dan Deployment Guide.

- [ ] **2.2.** Klasifikasikan seluruh data hasil penyaringan ke dalam 17 bagian (section) sesuai kerangka struktur YAML pada Bagian 4 di atas.

- [ ] **2.3.** Untuk setiap data yang diklasifikasikan, tentukan:
  - Nama key YAML (gunakan `snake_case`).
  - Nilai (*value*) yang spesifik dan konkret (bukan placeholder generik).
  - Komentar YAML (`#`) untuk memberikan deskripsi singkat di samping setiap parameter penting.

---

### Tahap 3: Penulisan Dokumen YAML

- [ ] **3.1.** Tulis header dokumen YAML dengan komentar blok pembuka yang memuat identitas dokumen (nama, proyek, versi, tanggal, penyusun, deskripsi).

- [ ] **3.2.** Tulis **Bagian 1: Metadata Dokumen** (`metadata:`).
  - [ ] 3.2.1. Isi metadata dokumen (nama, proyek, versi 1.0, tanggal, status, penyusun, deskripsi, posisi SDLC).
  - [ ] 3.2.2. Isi daftar referensi dokumen yang digunakan (kode ref, nama, path, versi, prioritas).

- [ ] **3.3.** Tulis **Bagian 2: Konfigurasi Lingkungan** (`environments:`).
  - [ ] 3.3.1. Definisikan 3 lingkungan: `development`, `staging`, `production`.
  - [ ] 3.3.2. Untuk setiap lingkungan, isi sub-konfigurasi: `database`, `security`, `application`, `output`, `logging` dengan nilai yang BERBEDA sesuai tabel perbedaan lingkungan di R-02 Bab 2.3.
  - [ ] 3.3.3. Pastikan nilai `APP_ENV`, `DB_NAME`, `DB_POOL_SIZE`, `JWT_SECRET_KEY`, `FERNET_KEY` berbeda per lingkungan.

- [ ] **3.4.** Tulis **Bagian 3: Konfigurasi Infrastruktur Fisik** (`infrastructure:`).
  - [ ] 3.4.1. Isi topologi jaringan (star topology, offline LAN, media Cat6 Gigabit).
  - [ ] 3.4.2. Isi node server (IP statis `192.168.1.200`, OS, service daemon, role).
  - [ ] 3.4.3. Isi node client (IP DHCP, OS, runtime, driver printer).
  - [ ] 3.4.4. Isi perangkat jaringan (switch hub 8-port Gigabit, router MikroTik hEX lite).
  - [ ] 3.4.5. Isi perangkat pendukung UPS (2 unit, 600VA/360W, justifikasi daya).

- [ ] **3.5.** Tulis **Bagian 4: Konfigurasi Sistem Operasi** (`operating_systems:`).
  - [ ] 3.5.1. Isi konfigurasi server Debian 12 (hostname `abuserver`, user `abuadm`, user `root`).
  - [ ] 3.5.2. Isi konfigurasi network interface server (interface name, address, netmask, gateway, dns).
  - [ ] 3.5.3. Isi konfigurasi firewall ufw (default policy, rules SSH 22, MySQL 3306 dari LAN).
  - [ ] 3.5.4. Isi konfigurasi SSH (PermitRootLogin no, port 22).
  - [ ] 3.5.5. Isi konfigurasi direktori terlindungi (path, owner, permission chmod).
  - [ ] 3.5.6. Isi konfigurasi client Windows 11 (terminal chcp 65001, USB AutoRun registry, akun Standard User).
  - [ ] 3.5.7. Isi konfigurasi PATH environment variable Python di Windows.

- [ ] **3.6.** Tulis **Bagian 5: Konfigurasi Database** (`database:`).
  - [ ] 3.6.1. Isi engine (MySQL Community Server), versi (8.4 LTS), service name (`mysql.service`).
  - [ ] 3.6.2. Isi config file path (`/etc/mysql/mysql.conf.d/mysqld.cnf`).
  - [ ] 3.6.3. Isi parameter mysqld (bind-address, character-set-server, collation-server, transaction-isolation).
  - [ ] 3.6.4. Isi daftar database (nama, character set, collation, tujuan) untuk produksi dan testing.
  - [ ] 3.6.5. Isi daftar user database (nama, host, privilege per database).
  - [ ] 3.6.6. Isi daftar schema files (schema.sql, seed.sql) dengan path dan deskripsi.

- [ ] **3.7.** Tulis **Bagian 6: Konfigurasi Runtime Python** (`python_runtime:`).
  - [ ] 3.7.1. Isi versi wajib (`3.14.2+`).
  - [ ] 3.7.2. Isi metode instalasi server (compile from source, altinstall, path commands).
  - [ ] 3.7.3. Isi metode instalasi client (installer .exe Windows, PATH, for all users).
  - [ ] 3.7.4. Isi konfigurasi virtual environment (nama `venv`, path aktivasi Windows/Linux).
  - [ ] 3.7.5. Isi daftar dependensi mandatory (5 pustaka dengan versi terkunci).
  - [ ] 3.7.6. Isi daftar dependensi recommended (2 pustaka visual CLI dengan versi).
  - [ ] 3.7.7. Isi daftar dependensi development (pytest, coverage dengan versi).
  - [ ] 3.7.8. Isi metode instalasi offline (pip_wheels folder, `--no-index --find-links`).

- [ ] **3.8.** Tulis **Bagian 7: Konfigurasi Aplikasi** (`application:`).
  - [ ] 3.8.1. Isi entry point (`main.py`), requirements file (`requirements.txt`).
  - [ ] 3.8.2. Isi directory structure lengkap (seluruh folder dan file sesuai layout standar).
  - [ ] 3.8.3. Tulis template `.env.example` lengkap dengan SEMUA variabel dan komentar.
  - [ ] 3.8.4. Isi deskripsi setiap variabel `.env` (nama, tipe data, deskripsi, contoh nilai, apakah wajib diisi manual).

- [ ] **3.9.** Tulis **Bagian 8: Konfigurasi Keamanan** (`security:`).
  - [ ] 3.9.1. Isi parameter bcrypt (cost_factor: 12, salt: dynamic 16-byte).
  - [ ] 3.9.2. Isi parameter JWT (algorithm: HS256, secret_key_min_length: 32, lifetime_seconds: 28800, payload_fields).
  - [ ] 3.9.3. Isi parameter rate limiting (max_attempts: 5, lockout_minutes: 10, db_columns).
  - [ ] 3.9.4. Isi daftar 8 peran RBAC dengan level hierarki.
  - [ ] 3.9.5. Isi parameter Fernet CRM (key_length: 32-byte base64, compliance: UU PDP No. 27/2022).
  - [ ] 3.9.6. Isi parameter backup encryption (algorithm: AES-256, format: ZIP).
  - [ ] 3.9.7. Isi parameter OS hardening server (ufw, SSH, chmod, bind-address).
  - [ ] 3.9.8. Isi parameter OS hardening client (Standard User, USB AutoRun disabled).

- [ ] **3.10.** Tulis **Bagian 9: Konfigurasi Backup dan Recovery** (`backup:`).
  - [ ] 3.10.1. Isi jadwal cron backup harian (`0 21 * * *`), path skrip, log file.
  - [ ] 3.10.2. Isi parameter enkripsi (AES-256 ZIP, variabel password dari `.env`).
  - [ ] 3.10.3. Isi parameter retensi (harian 30 hari, bulanan 12 bulan, cold storage).
  - [ ] 3.10.4. Isi path direktori backup server (`/var/lib/mysql-backups/`), permission, owner.
  - [ ] 3.10.5. Isi parameter `/root/.my.cnf` (chmod 600, isi konfigurasi client).
  - [ ] 3.10.6. Isi parameter disaster recovery (hardware pengganti, prosedur restore).

- [ ] **3.11.** Tulis **Bagian 10: Konfigurasi Version Control** (`version_control:`).
  - [ ] 3.11.1. Isi sistem (Git), identity (nama, email — tandai `[HARUS DIISI MANUAL]`).
  - [ ] 3.11.2. Isi strategi branching (feature branch, main stable).
  - [ ] 3.11.3. Isi konvensi commit (Conventional Commits: feat, fix, docs, chore, test).
  - [ ] 3.11.4. Isi daftar `.gitignore` entries lengkap.
  - [ ] 3.11.5. Isi konvensi tagging rilis (format `v{major}.{minor}.{patch}`).

- [ ] **3.12.** Tulis **Bagian 11: Konfigurasi Printer dan Perangkat** (`peripheral_devices:`).
  - [ ] 3.12.1. Isi konfigurasi printer thermal (port COM1/USB001, width 58mm/80mm, driver Generic/Text Only, nama `AbuPrinterNota`).
  - [ ] 3.12.2. Isi konfigurasi cash drawer (koneksi RJ11 ke printer, auto-open on print).

- [ ] **3.13.** Tulis **Bagian 12: Konfigurasi Connection Pool dan Retry** (`connection_management:`).
  - [ ] 3.13.1. Isi parameter pool (pool_name: `abupool`, pool_size: 5 untuk produksi, 2 untuk testing).
  - [ ] 3.13.2. Isi parameter retry (max_retries: 3, backoff: exponential $2^n$ detik, error_codes: [2006, 2013]).

- [ ] **3.14.** Tulis **Bagian 13: Konfigurasi Logging dan Monitoring** (`logging:`).
  - [ ] 3.14.1. Isi konfigurasi audit trail (tabel `audit_logs`, event pemicu, format JSON, retensi 12 bulan).
  - [ ] 3.14.2. Isi konfigurasi backup logs (tabel `backup_logs`).
  - [ ] 3.14.3. Isi konfigurasi system logs (path `/var/log/abucom_backup.log`).

- [ ] **3.15.** Tulis **Bagian 14: Konfigurasi Testing** (`testing:`).
  - [ ] 3.15.1. Isi framework (pytest 8.2.0, coverage 7.5.1).
  - [ ] 3.15.2. Isi target coverage (≥ 90% untuk folder `logic/` dan `db/`).
  - [ ] 3.15.3. Isi konfigurasi sandbox (database `abucom_test_db`, `.env.test` lengkap).

- [ ] **3.16.** Tulis **Bagian 15: Kode Error dan Troubleshooting** (`error_codes:` dan `troubleshooting:`).
  - [ ] 3.16.1. Isi seluruh kode error keamanan dari R-04 Bab 10 (ERR-AUTH-001 s.d ERR-CASH-004).
  - [ ] 3.16.2. Isi daftar masalah umum dan solusi dari R-01 Bab 14 dan R-02 Bab 11.4.

- [ ] **3.17.** Tulis **Bagian 16: Parameter Operasional Harian** (`operations:`).
  - [ ] 3.17.1. Isi SOP startup harian (jadwal, langkah-langkah, penanggung jawab).
  - [ ] 3.17.2. Isi SOP shutdown harian (jadwal, graceful shutdown, urutan perangkat).
  - [ ] 3.17.3. Isi jadwal maintenance berkala (mingguan, bulanan, kuartalan).
  - [ ] 3.17.4. Isi kontak eskalasi darurat (nomor WA, email, waktu layanan).

- [ ] **3.18.** Tulis **Bagian 17: Referensi Dokumen** (`references:`).
  - [ ] 3.18.1. Isi daftar lengkap 9 file referensi yang digunakan (kode ref, nama, path, versi, prioritas, peran).

---

### Tahap 4: Penandaan Data Kosong

- [ ] **4.1.** Periksa seluruh isi dokumen YAML yang sudah ditulis. Identifikasi setiap parameter atau nilai yang **TIDAK DITEMUKAN** di dalam file referensi manapun.

- [ ] **4.2.** Untuk setiap data kosong yang teridentifikasi, tandai menggunakan format berikut dalam komentar YAML:
  ```yaml
  parameter_name: "[HARUS DIISI MANUAL]"  # Data tidak ditemukan di file referensi. Isi secara manual oleh pemilik/admin.
  ```

- [ ] **4.3.** Contoh data yang kemungkinan perlu ditandai `[HARUS DIISI MANUAL]`:
  - Password root server Linux.
  - Password root MySQL.
  - Password user aplikasi `abucom_app`.
  - JWT Secret Key produksi aktual.
  - Fernet Key produksi aktual.
  - Backup ZIP password produksi aktual.
  - Nama dan email Git identity pemilik.
  - Port printer thermal aktual PC Kasir.
  - Gateway IP router MikroTik aktual.
  - Password admin MikroTik.

---

### Tahap 5: Validasi Kualitas Dokumen

- [ ] **5.1.** Validasi **kelengkapan**: Pastikan SEMUA parameter teknis yang tersebar di 9 file referensi sudah terangkum ke dalam dokumen YAML ini. Tidak ada parameter konfigurasi yang terlewatkan.

- [ ] **5.2.** Validasi **konsistensi**: Pastikan SEMUA nilai parameter di dokumen ini KONSISTEN dengan nilai yang tercantum di file referensi. Misalnya:
  - IP server harus konsisten `192.168.1.200` di semua section.
  - Pool name harus konsisten `abupool` di semua section.
  - bcrypt cost factor harus konsisten `12` di semua section.
  - Nama database harus konsisten `abucom_db` dan `abucom_test_db`.

- [ ] **5.3.** Validasi **format YAML**: Pastikan dokumen YAML valid secara sintaks:
  - Indentasi konsisten menggunakan 2 spasi (BUKAN tab).
  - String yang mengandung karakter khusus dibungkus dalam tanda kutip.
  - List menggunakan format `- item`.
  - Multi-line string menggunakan `|` atau `>`.
  - Komentar menggunakan `#`.

- [ ] **5.4.** Validasi **bahasa**: Pastikan seluruh komentar dan deskripsi ditulis dalam bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami.

- [ ] **5.5.** Validasi **kelayakan referensi**: Pastikan dokumen ini dapat dijadikan **input utama** bagi dokumen SDLC fase selanjutnya:
  - User Manual (panduan parameter konfigurasi untuk admin/pemilik).
  - Maintenance & Operations Logbook (referensi parameter operasional harian).
  - Skrip otomasi deployment (parameter machine-readable).

- [ ] **5.6.** Validasi **kekomprehensifan kode error**: Pastikan seluruh kode error yang tercantum di R-04 (Security Design) Bab 10 telah dipetakan secara lengkap ke dalam section kode error YAML.

---

### Tahap 6: Penulisan ke Target File

- [ ] **6.1.** Setelah seluruh tahap validasi selesai, tuangkan seluruh hasil penyusunan dokumen Environment Config ke dalam target file:
  ```
  docs/sdlc/06_deployment/02_environment_config.yaml
  ```

- [ ] **6.2.** Pastikan file ditulis secara LENGKAP dan UTUH dari bagian pertama hingga bagian terakhir. DILARANG memotong atau meringkas isi dokumen.

- [ ] **6.3.** Pastikan baris terakhir file berisi komentar penutup:
  ```yaml
  # --- AKHIR DOKUMEN ---
  # Dokumen Environment Config AbuCom ini dinyatakan sah dan berlaku.
  ```

---

## 6. Instruksi Tambahan Khusus Dokumen Environment Config YAML

Berikut adalah instruksi tambahan yang spesifik untuk ciri khas dokumen Environment Config YAML yang mungkin belum tercakup di atas:

### 6.1. Standar Penulisan YAML
- [ ] Gunakan indentasi **2 spasi** secara konsisten (standar YAML, BUKAN 4 spasi dan BUKAN tab).
- [ ] Gunakan `snake_case` untuk semua nama key YAML.
- [ ] Setiap section utama dipisahkan oleh baris komentar pembatas (`# ---`).
- [ ] Setiap blok konfigurasi penting diberi komentar deskriptif di atasnya menggunakan `#`.
- [ ] Nilai boolean menggunakan `true`/`false` (lowercase YAML standard).
- [ ] Nilai numerik ditulis tanpa tanda kutip.
- [ ] Nilai string yang mengandung karakter khusus (`:`, `{`, `}`, `[`, `]`, `#`, `&`, `*`, `!`, `|`, `>`, `'`, `"`, `%`, `@`, `` ` ``) dibungkus dalam tanda kutip ganda (`"`).
- [ ] Gunakan anchor (`&`) dan alias (`*`) YAML untuk menghindari duplikasi data yang berulang (misalnya parameter server IP yang digunakan di banyak tempat).

### 6.2. Prinsip DRY (Don't Repeat Yourself)
- [ ] Identifikasi parameter yang digunakan berulang di banyak section (misalnya `server_ip: 192.168.1.200`). Definisikan sebagai YAML anchor di section awal, lalu gunakan alias di section lainnya.
- [ ] Contoh penggunaan anchor dan alias:
  ```yaml
  # Definisi anchor
  server_ip: &server_ip "192.168.1.200"
  
  # Penggunaan alias di section lain
  database:
    host: *server_ip
  ```

### 6.3. Pengelompokan Parameter Sensitif
- [ ] Parameter yang berisi kredensial atau kunci rahasia harus ditandai secara eksplisit dengan komentar `# [SENSITIF]` dan nilai `[HARUS DIISI MANUAL]`:
  ```yaml
  jwt_secret_key: "[HARUS DIISI MANUAL]"  # [SENSITIF] Generate via: python -c "import secrets; print(secrets.token_hex(32))"
  ```

### 6.4. Validasi Silang (Cross-Validation)
- [ ] Setelah penulisan selesai, lakukan validasi silang minimal terhadap 5 parameter kritis berikut untuk memastikan konsistensi antar-section:
  1. `server_ip` → harus sama di section infrastructure, database, firewall, dan .env.
  2. `db_name` → harus sama di section database, environments, dan application.
  3. `pool_size` → harus sesuai per lingkungan (5 produksi, 2 testing).
  4. `bcrypt_cost_factor` → harus sama di section security dan application.
  5. `jwt_lifetime_seconds` → harus sama di section security dan .env.

### 6.5. Keterkaitan dengan Deployment Guide
- [ ] Dokumen Environment Config ini berfungsi sebagai **companion document** dari Deployment Guide (R-02). Deployment Guide berisi **prosedur step-by-step**, sedangkan Environment Config berisi **seluruh parameter yang digunakan oleh prosedur tersebut**. Pastikan tidak ada parameter di Deployment Guide yang tidak terwakili di dokumen ini.

---

## 7. Kriteria Selesai (Definition of Done)

Issue ini dianggap **selesai** jika dan hanya jika:

- [ ] Dokumen `docs/sdlc/06_deployment/02_environment_config.yaml` telah terisi lengkap dan utuh.
- [ ] Seluruh 17 bagian (section) kerangka YAML telah tertulis tanpa ada yang terlewat.
- [ ] Seluruh parameter dari 9 file referensi telah terabsorpsi secara lengkap.
- [ ] Seluruh data kosong telah ditandai dengan `[HARUS DIISI MANUAL]`.
- [ ] Format YAML valid secara sintaks (indentasi 2 spasi, tanpa error parsing).
- [ ] Bahasa Indonesia natural, tidak ambigu, mudah dipahami.
- [ ] Komentar deskriptif tersedia untuk setiap parameter penting.
- [ ] Referensi dokumen tercantum di bagian akhir file.
- [ ] File dapat dijadikan acuan tunggal konfigurasi untuk deployment dan operasional sistem AbuCom.

---

## 8. Referensi File yang Digunakan dalam Penyusunan Issue Ini

| No | Nama Dokumen | Path Relatif | Peran dalam Penyusunan Issue |
|:---:|---|---|---|
| 1 | Environment Setup v1.1 | `docs/sdlc/04_implementation/02_environment_setup.md` | Sumber data utama parameter konfigurasi lingkungan, variabel `.env`, dan spesifikasi infrastruktur. |
| 2 | Deployment Guide v1.1 | `docs/sdlc/06_deployment/01_deployment_guide.md` | Sumber data perbedaan lingkungan, nilai produksi aktual, dan SOP operasional. |
| 3 | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` | Sumber data topologi, hardware, arsitektur 4-layer, dan connection pooling. |
| 4 | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | Sumber data parameter keamanan, kode error, dan compliance UU PDP. |
| 5 | Tech Stack Decision v1.1 | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Sumber data batasan mandatori teknologi dan matriks dependensi. |
| 6 | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` | Sumber data layout proyek, `.gitignore`, dan `.env.example`. |
| 7 | Database Schema v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | Sumber data nama database, tabel, dan user MySQL. |
| 8 | Module Structure v1.1 | `docs/sdlc/04_implementation/03_module_structure.md` | Sumber data struktur direktori modul dan entry point. |
| 9 | Git Workflow v1.1 | `docs/sdlc/04_implementation/04_git_workflow.md` | Sumber data branching, tagging, dan commit convention. |
| 10 | Narasi Pemilik | `docs/sdlc/narasi.txt` | **TIDAK digunakan** — seluruh data sudah terabsorpsi ke dokumen formal SDLC. |

---

*Issue ini disusun oleh Antigravity pada 27 Mei 2026 sebagai panduan low-level untuk implementasi oleh Junior Programmer atau model AI lain yang lebih murah.*
