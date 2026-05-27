---
judul       : Validasi, Perbaikan, dan Penyempurnaan Dokumen Maintenance Guide
target_file : docs/sdlc/07_maintenance/01_maintenance_guide.md
dibuat_oleh : Senior Antigravity AI Architect
tanggal     : 2026-05-27
prioritas   : HIGH
status      : OPEN
---

# Validasi, Perbaikan, dan Penyempurnaan Dokumen Maintenance Guide

## Ringkasan Issue

Dokumen **Maintenance Guide** (`docs/sdlc/07_maintenance/01_maintenance_guide.md`) versi `1.0` telah selesai disusun pada fase implementasi awal. Issue ini memerintahkan pelaksana untuk melakukan validasi menyeluruh, audit komparatif mendalam, dan penyempurnaan akhir dokumen tersebut sebelum ditetapkan sebagai dokumen panduan operasional resmi yang sah dan siap digunakan dalam fase SDLC selanjutnya.

Seluruh pekerjaan dalam issue ini harus diselesaikan secara **mandiri, sistematis, dan tuntas** tanpa memerlukan konfirmasi atau interupsi dari pihak lain. Implementasi issue ini **harus diselesaikan hingga tahap overwrite file** dengan versi dokumen yang telah direvisi menjadi `v1.1`.

---

## Persona Pelaksana (WAJIB DIBACA SEBELUM MEMULAI)

> **[INSTRUKSI PERSONA — WAJIB DIPATUHI SECARA MUTLAK]**
>
> Kamu adalah seorang **Senior IT Service Management Auditor & Technical Documentation Specialist** dengan spesialisasi:
> - **ITIL v4 Expert** — Ahli validasi panduan manajemen layanan IT (service management lifecycle).
> - **IEEE 14764 Software Maintenance Practitioner** — Ahli standar internasional pemeliharaan perangkat lunak.
> - **DevOps Documentation Reviewer** — Ahli audit runbook operasional sistem dual-OS CLI offline LAN.
> - **Indonesian Technical Writing Specialist** — Ahli penulisan dokumen teknis berbahasa Indonesia yang presisi, natural, tidak ambigu, dan mudah dipahami oleh junior programmer maupun LLM AI model yang lebih murah.
>
> Tugasmu adalah **memeriksa, menganalisa, dan memvalidasi** dokumen Maintenance Guide secara sangat ketat menggunakan 11 dimensi validasi yang dijabarkan di bawah ini. Kamu **tidak boleh** berhenti di tengah jalan, tidak boleh menghasilkan output terpotong (truncated), dan tidak boleh melewatkan satu baris pun saat melakukan overwrite dokumen akhir.

---

## Konteks Dokumen

| Item | Detail |
|---|---|
| **Dokumen Utama (Target)** | `docs/sdlc/07_maintenance/01_maintenance_guide.md` |
| **Versi Saat Ini** | v1.0 (Draft) |
| **Versi Setelah Revisi** | v1.1 (Revised & Validated) |
| **Jumlah Bab** | 22 Bab Utama |
| **Jumlah Baris Saat Ini** | ±1.305 baris |
| **Lokasi Referensi** | `docs/sdlc/` |
| **Jumlah Referensi (R-01 s.d R-14)** | 14 Dokumen Formal SDLC |

### Daftar Dokumen Referensi (14 File)

| Kode | Path File Referensi |
|:---:|---|
| R-01 | `docs/sdlc/06_deployment/01_deployment_guide.md` |
| R-02 | `docs/sdlc/03_design/03_system_architecture.md` |
| R-03 | `docs/sdlc/03_design/06_security_design.md` |
| R-04 | `docs/sdlc/06_deployment/02_environment_config.yaml` |
| R-05 | `docs/sdlc/06_deployment/03_release_notes.md` |
| R-06 | `docs/sdlc/04_implementation/02_environment_setup.md` |
| R-07 | `docs/sdlc/05_testing/04_bug_report_template.md` |
| R-08 | `docs/sdlc/05_testing/01_test_plan.md` |
| R-09 | `docs/sdlc/04_implementation/01_coding_standard.md` |
| R-10 | `docs/sdlc/04_implementation/04_git_workflow.md` |
| R-11 | `docs/sdlc/01_planning/04_tech_stack_decision.md` |
| R-12 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| R-13 | `docs/sdlc/03_design/01_database_schema.sql` |
| R-14 | `docs/sdlc/04_implementation/03_module_structure.md` |

---

## Tahapan Implementasi Issue (LOW-LEVEL STEP-BY-STEP)

> **[PERINGATAN KERAS]** Ikuti setiap langkah secara berurutan dari atas ke bawah. Jangan melompati langkah. Jangan membuat asumsi. Setiap checklist `[ ]` harus ditandai `[x]` secara mental sebelum lanjut ke langkah berikutnya.

---

### FASE 1 — PERSIAPAN DAN PEMBACAAN MENYELURUH

#### Langkah 1.1 — Baca Dokumen Utama Secara Lengkap
- [ ] Buka dan baca **seluruh isi** file `docs/sdlc/07_maintenance/01_maintenance_guide.md` dari baris 1 hingga baris terakhir (±1.305 baris).
- [ ] Catat secara internal struktur dokumen: berapa bab, sub-bab, tabel, checklist, diagram mermaid, dan blok kode yang ada.
- [ ] Catat nomor versi dokumen saat ini: `1.0`, tanggal penyusunan, dan nama penyusun.
- [ ] Catat semua kode referensi yang disebutkan dalam dokumen (R-01 s.d R-14) dan path filenya di Bab 22.

#### Langkah 1.2 — Baca Seluruh 14 Dokumen Referensi
Baca seluruh referensi berikut secara berurutan dan catat poin-poin kunci masing-masing:

- [ ] Baca `docs/sdlc/06_deployment/01_deployment_guide.md` (R-01) — catat: prosedur startup/shutdown server, backup otomatis, restore, dan disaster recovery.
- [ ] Baca `docs/sdlc/03_design/03_system_architecture.md` (R-02) — catat: diagram deployment, daftar 28 tabel InnoDB, 10 modul, connection pool, retry mechanism, dan spesifikasi node.
- [ ] Baca `docs/sdlc/03_design/06_security_design.md` (R-03) — catat: ufw rules, bcrypt cost factor, JWT durasi, Fernet key, hardening OS, kamus kode error (ERR-DB, ERR-AUTH, ERR-SESSION, ERR-FILE, ERR-CASH), dan audit logs format JSON.
- [ ] Baca `docs/sdlc/06_deployment/02_environment_config.yaml` (R-04) — catat: semua parameter runtime (DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, JWT_SECRET_KEY, FERNET_KEY, PRINTER_PORT, PRINTER_WIDTH_MM, APP_CABANG_ID, BACKUP_ZIP_PASSWORD, dan parameter lainnya).
- [ ] Baca `docs/sdlc/06_deployment/03_release_notes.md` (R-05) — catat: daftar 10 modul aktif, known limitations, known issues (DEF-COMPAT-001, DEF-PERF-001), dan roadmap versi v1.1.0 dan v1.2.0.
- [ ] Baca `docs/sdlc/04_implementation/02_environment_setup.md` (R-06) — catat: prosedur kompilasi Python luring, setup MySQL Server, instalasi requirements.txt, dan prosedur luring dependensi.
- [ ] Baca `docs/sdlc/05_testing/04_bug_report_template.md` (R-07) — catat: severity level S1-S5, priority level P1-P4, SLA pemulihan per severity, dan format form bug report.
- [ ] Baca `docs/sdlc/05_testing/01_test_plan.md` (R-08) — catat: test exit criteria, code coverage target, regression testing, dan daftar test case Smoke Test (ST-01 s.d ST-06).
- [ ] Baca `docs/sdlc/04_implementation/01_coding_standard.md` (R-09) — catat: aturan FP Python murni, explicit UTF-8, larangan float polos, Decimal(15,4) ROUND_HALF_UP, dan aturan .gitignore.
- [ ] Baca `docs/sdlc/04_implementation/04_git_workflow.md` (R-10) — catat: alur branching (main, patch/, hotfix/), Git commit standard, tagging rilis, dan merge strategy.
- [ ] Baca `docs/sdlc/01_planning/04_tech_stack_decision.md` (R-11) — catat: platform locked (Python 3.14.2+, MySQL 8.4 LTS, Debian 12, Windows 11), alasan pemilihan, dan batasan luring.
- [ ] Baca `docs/sdlc/02_analysis/02_software_requirements.md` (R-12) — catat: spesifikasi non-fungsional (response time ≤ 2 detik, uptime, portabilitas dual-OS, ketersediaan 6 hari/minggu).
- [ ] Baca `docs/sdlc/03_design/01_database_schema.sql` (R-13) — catat: DDL lengkap 28 tabel InnoDB, nama tabel per kelompok (A, B, C, D, E), tipe kolom kritis (DECIMAL(15,4), BIGINT, VARCHAR), dan semua constraint foreign key.
- [ ] Baca `docs/sdlc/04_implementation/03_module_structure.md` (R-14) — catat: peta direktori module di PC klien, nama file Python tiap modul (M.1–M.10), dan path file konfigurasi.

---

### FASE 2 — VALIDASI DIMENSI 1: KELENGKAPAN KOMPARASI REFERENSI

> **Tujuan**: Memastikan dokumen utama telah merangkum **semua** data dan informasi penting yang ada di 14 dokumen referensi, dan tidak ada detail kritis yang terlewat.

- [ ] **[V1-01]** Bandingkan diagram deployment Mermaid di Bab 2.1 dokumen utama dengan diagram di R-02. Pastikan semua komponen node (Server, Kasir, UPS, Switch, Router, Printer) dan atribut teknisnya (IP, OS, runtime, port) konsisten identik antara kedua dokumen.
- [ ] **[V1-02]** Bandingkan Matriks Komponen per Node di Bab 2.2 dengan spesifikasi node di R-02 dan R-04. Pastikan semua kolom (OS, Runtime, Service Daemon, Pustaka Utama, Penyimpanan Berkas, Akses Jaringan) terisi lengkap dan akurat.
- [ ] **[V1-03]** Bandingkan daftar 10 modul fungsional di Bab 2.3 dengan R-02 dan R-05. Pastikan nama modul (M.1–M.10), deskripsi fungsi ringkas, dan fitur utama tiap modul konsisten dan tidak ada modul yang hilang.
- [ ] **[V1-04]** Bandingkan daftar 28 tabel database di Bab 2.4 dengan DDL di R-13. Pastikan nama seluruh 28 tabel tertera benar dan pengelompokannya (Kelompok A, B, C, D, E) sesuai DDL.
- [ ] **[V1-05]** Bandingkan daftar pustaka dependensi dan versi di Bab 2.5 dengan `requirements.txt` yang disebutkan di R-06 dan R-11. Pastikan 7 pustaka (`mysql-connector-python`, `python-dotenv`, `bcrypt`, `pyjwt`, `cryptography`, `rich`, `tabulate`) beserta versi terkunci (`==`) sudah sesuai.
- [ ] **[V1-06]** Bandingkan SOP Startup Harian di Bab 4.1 dan SOP Shutdown di Bab 4.2 dengan runbook harian di R-01. Pastikan urutan langkah, waktu (Pukul 07:45 WIB startup, 21:00 WIB backup cron, 21:05 WIB shutdown server), dan perintah bash/cmd identik.
- [ ] **[V1-07]** Bandingkan skrip cron backup di Bab 12.2 dengan skrip di R-01 dan parameter di R-04. Pastikan `BACKUP_DIR`, `DB_NAME`, path `/root/.my.cnf`, flag `--single-transaction --quick --lock-tables=false`, enkripsi ZIP AES-256, rotasi 30 hari, `chmod 600`, dan format log `[SUCCESS]/[ERROR]` semuanya konsisten.
- [ ] **[V1-08]** Bandingkan kamus kode error di Bab 17 (ERR-DB-001, ERR-DB-002, ERR-AUTH-001, ERR-AUTH-002, ERR-SESSION-001, ERR-SESSION-002, ERR-FILE-001, ERR-FILE-039, ERR-CASH-001, ERR-CASH-004) dengan kamus kode error di R-03. Pastikan tidak ada kode error dari R-03 yang belum masuk ke Bab 17.
- [ ] **[V1-09]** Bandingkan klasifikasi severity S1–S5 dan priority P1–P4 di Bab 10.2 dengan R-07. Pastikan nama, definisi, dan SLA setiap level identik dengan template bug report resmi.
- [ ] **[V1-10]** Bandingkan tabel SLA di Bab 10.8 dengan SLA yang ditetapkan di R-07. Pastikan target respon dan MTTR setiap severity level (S1–S5) sesuai secara presisi.
- [ ] **[V1-11]** Bandingkan prosedur branching dan tagging Git di Bab 10.4 dan 10.5 dengan R-10. Pastikan nama branch convention (`patch/`, `hotfix/`), perintah `git checkout -b`, `git merge`, `git tag -a` beserta formatnya konsisten.
- [ ] **[V1-12]** Bandingkan prosedur upgrade Python runtime di Bab 11.1 dengan R-06. Pastikan perintah kompilasi (`./configure --enable-optimizations --with-ensurepip=install`, `make -j$(nproc)`, `sudo make altinstall`) konsisten.
- [ ] **[V1-13]** Bandingkan prosedur migrasi skema DDL di Bab 11.3 dengan struktur tabel di R-13. Pastikan contoh `ALTER TABLE` menggunakan tipe data yang sesuai dengan DDL (DECIMAL(15,4) bukan FLOAT).
- [ ] **[V1-14]** Bandingkan prosedur rotasi JWT Secret Key dan Fernet Key di Bab 8.1 dan 8.2 dengan R-03 dan R-04. Pastikan panjang key (32-byte hex untuk JWT, Fernet.generate_key() untuk Fernet), parameter `.env` (`JWT_SECRET_KEY`, `FERNET_KEY`), dan nama skrip (`utils/rotate_fernet.py`) konsisten.
- [ ] **[V1-15]** Bandingkan prosedur hardening OS di Bab 14.5 dengan R-03. Pastikan semua item hardening dari R-03 tercakup: `PermitRootLogin no`, `/root/.my.cnf` permission `600`, dan registry `NoDriveTypeAutoRun = FF`.
- [ ] **[V1-16]** Bandingkan matriks RACI di Bab 19.1 dengan deskripsi peran di R-02 dan R-03. Pastikan semua 8 aktivitas pemeliharaan dan 5 peran aktor terisi tanpa sel kosong yang tidak valid.
- [ ] **[V1-17]** Bandingkan roadmap upgrade di Bab 9.5 dengan roadmap versi di R-05. Pastikan versi roadmap (v1.1.0 dan v1.2.0) dan fitur rencananya konsisten dengan Release Notes.
- [ ] **[V1-18]** Periksa apakah ada parameter konfigurasi kritis dari R-04 (Environment Config) yang **belum** disebutkan atau digunakan dalam prosedur di dokumen utama. Jika ada, identifikasi bab yang relevan dan tambahkan referensi parameter tersebut.

---

### FASE 3 — VALIDASI DIMENSI 2: RELEVANSI DAN FOKUS KONTEN

> **Tujuan**: Memastikan dokumen utama hanya memuat data dan informasi yang memang **relevan dan dibutuhkan** spesifik oleh Maintenance Guide, dan tidak mengandung konten yang seharusnya masuk ke dokumen SDLC lain.

- [ ] **[V2-01]** Periksa apakah ada blok kode atau prosedur di dokumen utama yang seharusnya hanya ada di Deployment Guide (R-01) dan tidak perlu diulang secara verbatim di Maintenance Guide. Jika ada, ringkas dengan referensi ke R-01 alih-alih duplikasi penuh.
- [ ] **[V2-02]** Periksa apakah ada deskripsi spesifikasi fungsional modul (detail fitur bisnis) yang terlalu panjang dan tidak relevan bagi konteks pemeliharaan. Maintenance Guide hanya perlu menyebut nama modul dan dampak operasionalnya terhadap pemeliharaan—bukan spesifikasi bisnis lengkapnya.
- [ ] **[V2-03]** Periksa apakah ada prosedur di Bab 11 (Adaptive Maintenance) yang tumpang tindih secara berlebihan dengan Environment Setup (R-06). Jika ada tumpang tindih, pastikan dokumen utama mengacu ke R-06 sebagai sumber utama dan hanya menuliskan langkah pemeliharaan tambahan yang spesifik untuk konteks maintenance.
- [ ] **[V2-04]** Periksa apakah seluruh 22 Bab yang ada di dokumen utama memang berisi konten yang **relevan dengan domain maintenance** (operasional, pemeliharaan, troubleshooting, keamanan, hardware, jadwal). Tandai bab mana pun yang terasa keluar dari cakupan maintenance.
- [ ] **[V2-05]** Periksa apakah tidak ada pengulangan (*redundancy*) prosedur yang sama antara sub-bab yang berbeda. Misalnya, prosedur `CHECK TABLE` disebutkan di Bab 6.2 (Bulanan) dan Bab 15.1 (Database Maintenance) — pastikan tidak ada kontradiksi antara keduanya, atau jika memang disebut dua kali, pastikan ada alasan yang jelas (konteks berbeda: jadwal vs prosedur teknis).

---

### FASE 4 — VALIDASI DIMENSI 3: STANDAR STRUKTUR DOKUMEN INDUSTRI

> **Tujuan**: Memastikan dokumen utama memiliki struktur yang sesuai dengan standar dokumen teknis operasional industri IT (ITIL v4 / IEEE 14764).

- [ ] **[V3-01]** Periksa apakah **frontmatter YAML** di baris 1–8 dokumen utama sudah memuat semua field wajib: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, dan `penyusun`. Jika ada field yang kosong atau kurang informatif, lengkapi.
- [ ] **[V3-02]** Periksa apakah tabel **Riwayat Perubahan Dokumen** (Bab/section paling atas) sudah mencantumkan kolom: `Versi`, `Tanggal`, `Deskripsi Perubahan`, dan `Oleh`. Pastikan format tabel rapi dan konsisten.
- [ ] **[V3-03]** Periksa apakah Bab 1 (Informasi Dokumen) mencakup semua sub-bab standar sebuah technical manual: Tujuan Dokumen, Cakupan Dokumen, Posisi dalam SDLC, Hubungan dengan Dokumen Lain (Input & Output), Audiens Target, dan Definisi/Akronim.
- [ ] **[V3-04]** Periksa apakah setiap SOP Pemeliharaan Rutin (Bab 4–9) memiliki **checklist penutup** (`### X.Y. Checklist Pemeliharaan`) yang merekapitulasi seluruh tugas pada bab tersebut. Jika ada bab SOP yang tidak memiliki checklist, tambahkan.
- [ ] **[V3-05]** Periksa apakah setiap prosedur troubleshooting di Bab 17 mengikuti format 4-poin standar: `Gejala`, `Kemungkinan Penyebab`, `Langkah Solusi`, dan `Pencegahan`. Jika ada sub-bab yang tidak mengikuti format ini, tambahkan poin yang kurang.
- [ ] **[V3-06]** Periksa apakah dokumen memiliki Bab **Glosarium** yang komprehensif. Pastikan semua akronim teknis yang digunakan dalam dokumen (ITIL, IEEE 14764, SLA, MTTR, MTBF, FP, CLI, JWT, RBAC, ACID, LAN, UPS, BOM, HPP, UU PDP, brute-force, mojibake, graceful shutdown, dll.) sudah didefinisikan di Glosarium.
- [ ] **[V3-07]** Periksa apakah Bab terakhir adalah **Referensi Dokumen** yang memuat tabel lengkap semua referensi (R-01 s.d R-14) dengan kolom: Kode Ref, Nama Dokumen, Path Berkas, Prioritas, dan Peran/Hubungan. Pastikan tidak ada referensi yang hilang.
- [ ] **[V3-08]** Periksa apakah seluruh **diagram Mermaid** (flowchart patching di Bab 10.7, diagram eskalasi insiden di Bab 13.8, diagram arsitektur deployment di Bab 2.1) memiliki label yang jelas, node yang lengkap, dan tidak ada syntax error (node tanpa label, edge putus, atau karakter khusus yang tidak dikutip).
- [ ] **[V3-09]** Periksa apakah seluruh **tabel data** dalam dokumen (Matriks Komponen, Tabel SLA, Tabel Risiko, RACI Matrix, Inventaris Hardware, Kalender Pemeliharaan) memiliki header kolom yang jelas, data yang lengkap di setiap sel, dan tidak ada sel yang kosong tanpa alasan yang jelas.
- [ ] **[V3-10]** Periksa apakah seluruh **blok kode** (bash, sql, cmd, python) memiliki komentar konteks di baris pertama yang menjelaskan di OS mana perintah tersebut dijalankan (contoh: `# [LINUX DEBIAN 12 — Server]` atau `# [WINDOWS 11 — Klien]`).
- [ ] **[V3-11]** Periksa apakah urutan 22 bab sudah logis dan mengalir dengan baik dari yang umum ke khusus: Informasi Dokumen → Arsitektur Sistem → Kategori Pemeliharaan → SOP Rutin → Prosedur Korektif/Adaptif → Backup/Recovery → Tanggap Darurat → Keamanan → Database → Hardware → Troubleshooting → Risiko → RACI → Kalender → Glosarium → Referensi.
- [ ] **[V3-12]** Periksa apakah ada **bab yang judul atau nomor urunya tidak konsisten** (misal sub-bab melompat dari 4.3 langsung ke 4.6 tanpa 4.4 dan 4.5). Koreksi urutan penomoran jika ditemukan inkonsistensi.

---

### FASE 5 — VALIDASI DIMENSI 4: KELAYAKAN SEBAGAI REFERENSI FASE SDLC SELANJUTNYA

> **Tujuan**: Memastikan dokumen ini dapat berdiri sendiri sebagai **input dan acuan utama** bagi dokumen-dokumen yang mungkin dibuat pada fase pasca-maintenance (misalnya dokumen audit akhir tahun, laporan kinerja sistem, atau evaluation report).

- [ ] **[V4-01]** Periksa apakah **SLA** pada Bab 10.8 sudah cukup spesifik dan terukur (ada angka waktu respon dan MTTR yang jelas), sehingga bisa dijadikan kontrak acuan bagi stakeholder non-teknis.
- [ ] **[V4-02]** Periksa apakah **Matriks Risiko** di Bab 18.2 sudah mencakup semua 10 risiko yang disebutkan di Bab 18.1, dengan nilai probabilitas, dampak, skor, dan rencana mitigasi yang terisi lengkap—bukan sekadar contoh parsial.
- [ ] **[V4-03]** Periksa apakah **Kalender Pemeliharaan** di Bab 20.1 dan 20.2 sudah mencakup semua aktivitas pemeliharaan dari Bab 4 hingga Bab 9 (Harian, Mingguan, Bulanan, Kuartalan, Semesteran, Tahunan), dan tidak ada aktivitas yang hilang dari kalender.
- [ ] **[V4-04]** Periksa apakah dokumen utama sudah menyediakan **output template** yang cukup (Maintenance Logbook, Incident Report Form, Patch Release Notes) yang disebutkan di Bab 1.4. Jika hanya disebutkan nama outputnya tanpa format, pertimbangkan untuk menambahkan contoh format minimal (header kolom) agar dokumen ini lebih actionable sebagai referensi.
- [ ] **[V4-05]** Periksa apakah prosedur **Disaster Recovery** di Bab 12.4 dan 12.5 cukup lengkap dan tidak bergantung pada pengetahuan di luar dokumen ini. Seorang administrator baru yang baru pertama kali membaca dokumen ini harus bisa mengeksekusi disaster recovery tanpa harus membuka dokumen lain.
- [ ] **[V4-06]** Periksa apakah **Bab 22 Referensi** menyebutkan kolom "Prioritas" (PRIMER/SEKUNDER/TERSIER) yang membantu pembaca mengetahui mana dokumen yang paling kritis untuk dibaca terlebih dahulu.

---

### FASE 6 — VALIDASI DIMENSI 5: KUALITAS BAHASA INDONESIA

> **Tujuan**: Memastikan bahasa yang digunakan natural, tidak ambigu, tidak membingungkan, dan dapat dipahami oleh junior programmer atau LLM AI model yang lebih murah.

- [ ] **[V5-01]** Periksa apakah ada kalimat yang terlalu panjang (lebih dari 3 klausa bersambung) yang berpotensi menimbulkan ambiguitas makna. Pecah kalimat panjang menjadi kalimat-kalimat pendek yang lebih jelas.
- [ ] **[V5-02]** Periksa apakah ada penggunaan kata teknis bahasa Inggris yang sudah ada padanan bahasa Indonesia-nya tetapi tidak didefinisikan di Glosarium dan tidak dicetak miring (italic). Standar: kata asing pertama kali muncul harus dicetak miring dan didefinisikan.
- [ ] **[V5-03]** Periksa konsistensi penggunaan istilah sepanjang dokumen. Contoh: apakah "PC Kasir", "klien kasir", "terminal kasir", dan "PC Desktop Kasir" digunakan secara konsisten untuk merujuk entitas yang sama? Jika tidak konsisten, standarkan satu istilah utama dan gunakan itu secara konsisten.
- [ ] **[V5-04]** Periksa apakah kata penghubung "and" (bahasa Inggris) masih tersisa di dalam kalimat berbahasa Indonesia. Ganti semua "and" dengan "dan" kecuali yang ada di dalam blok kode atau perintah terminal.
- [ ] **[V5-05]** Periksa apakah ada instruksi SOP yang menggunakan kata kerja pasif yang ambigu (misalnya "dilakukan" tanpa menyebut siapa yang melakukan). Ganti dengan kalimat aktif yang menyebutkan aktor pelaksana secara eksplisit.
- [ ] **[V5-06]** Periksa apakah ada typo, kesalahan ejaan, atau penggunaan tanda baca yang salah (misal tanda koma sebelum "dan", atau tanda titik ganda "..").
- [ ] **[V5-07]** Periksa apakah setiap langkah SOP diawali dengan kata kerja imperatif yang jelas (misal: "Buka", "Jalankan", "Periksa", "Pastikan", "Login", "Catat") sehingga tidak ada langkah yang ambigu.
- [ ] **[V5-08]** Periksa apakah ada pengulangan kata yang berlebihan dalam satu kalimat (misalnya "nota nota", "kasir kasir", "debu debu") yang muncul karena kesalahan copy-paste. Hapus duplikat kata tersebut.

---

### FASE 7 — VALIDASI DIMENSI 6: KELENGKAPAN DATA (TIDAK ADA DATA KOSONG / PLACEHOLDER)

> **Tujuan**: Memastikan tidak ada sel tabel, parameter, nilai, nama, nomor, atau informasi kritis yang masih berupa placeholder, dikosongkan, atau perlu diisi manual.

- [ ] **[V6-01]** Cari semua pola placeholder umum di seluruh dokumen: `[NAMA]`, `[NOMOR]`, `[TANGGAL]`, `[TBD]`, `[TODO]`, `XXXX`, `????`, `___`, `<...>`, atau tanda kurung kosong `()`. Jika ditemukan, isi dengan data yang sesuai berdasarkan konteks dokumen dan referensi yang tersedia.
- [ ] **[V6-02]** Periksa tabel **Inventaris Hardware** di Bab 16.6. Pastikan semua kolom (ID Aset, Deskripsi, Tanggal Pembelian, Estimasi Umur Pakai, Lokasi Fisik, Status Kesehatan) terisi dengan data nyata AbuCom—bukan data fiktif generik.
- [ ] **[V6-03]** Periksa kontak darurat di Bab 13.7. Jika nomor WhatsApp (`+62-812-3456-7890`) dan email (`support@abucom.com`) adalah data placeholder, tandai sebagai `[DIISI PEMILIK USAHA]` agar jelas bahwa ini perlu konfirmasi manual dari Alfatih.
- [ ] **[V6-04]** Periksa parameter di skrip cron backup Bab 12.2. Pastikan nilai `ZIP_PASSWORD` tidak di-hardcode secara polos di dalam skrip—melainkan harus dibaca dari variabel environment atau file konfigurasi terenkripsi, sesuai dengan praktik keamanan R-03 dan R-04. Jika ditemukan hardcode password, beri catatan `[PERINGATAN KEAMANAN]` dan koreksi logika skrip agar membaca dari `.env` atau `/root/.my.cnf`.
- [ ] **[V6-05]** Periksa apakah nilai parameter konfigurasi kritis di seluruh dokumen (IP server `192.168.1.200`, port `3306`, durasi JWT `8 jam / 28.800 detik`, bcrypt cost `12`, pool size `5`, threshold selisih kas `Rp 10.000`, batas pengeluaran `Rp 500.000`, target laba `Rp 15 juta`) konsisten antara dokumen utama dan referensi R-02, R-03, R-04. Jika ada nilai yang berbeda, sesuaikan mengikuti referensi primer.
- [ ] **[V6-06]** Periksa apakah versi dokumen di frontmatter YAML (`versi: 1.0`) dan di tabel Riwayat Perubahan sudah disiapkan untuk diupdate menjadi `1.1` saat overwrite.

---

### FASE 8 — VALIDASI DIMENSI 7: TIDAK ADA INTERUPSI PADA FASE SDLC BERIKUTNYA

> **Tujuan**: Memastikan kualitas dan kelengkapan dokumen ini tidak akan menghambat atau selalu dipertanyakan oleh pelaksana fase SDLC berikutnya.

- [ ] **[V7-01]** Simulasikan pertanyaan yang mungkin diajukan oleh junior programmer atau LLM yang membaca dokumen ini untuk pertama kalinya: "Apa yang harus dilakukan jika terjadi X?". Pastikan setiap skenario kritis (database crash, mati listrik, backup gagal, printer rusak, selisih kas, brute-force login) memiliki prosedur penanganan yang jelas di dokumen ini.
- [ ] **[V7-02]** Periksa apakah ada referensi ke bab lain dalam dokumen yang merujuk nomor bab yang salah atau tidak ada (misalnya "lihat Bab 13" padahal yang dimaksud adalah "Bab 15"). Koreksi semua referensi silang antar bab yang salah.
- [ ] **[V7-03]** Periksa apakah ada instruksi yang bergantung pada pengetahuan implisit ("lakukan seperti biasa", "ikuti prosedur standar") tanpa menyebutkan prosedur konkret atau referensi bab yang spesifik. Ganti dengan instruksi eksplisit atau tambahkan referensi bab.
- [ ] **[V7-04]** Periksa apakah setiap **checklist pemeliharaan** (Bab 4.6, 5.6, 6.8, 7.6, 8.6, 9.6) benar-benar merangkum **semua** langkah SOP pada bab tersebut—bukan hanya sebagian. Tambahkan poin checklist yang terlewat.
- [ ] **[V7-05]** Periksa apakah Bab 18 (Matriks Risiko) sudah menyediakan **rencana kontingensi** yang cukup detail untuk setiap risiko berskor tinggi (skor ≥ 10). Risiko berskor tinggi tidak boleh hanya memiliki mitigasi satu kalimat tanpa referensi prosedur konkret.

---

### FASE 9 — VALIDASI DIMENSI 8: PEMERIKSAAN SPESIFIK CIRI KHAS DOKUMEN MAINTENANCE GUIDE

> **Tujuan**: Memeriksa aspek-aspek teknis yang spesifik dan unik pada dokumen Maintenance Guide—hal-hal yang tidak diperiksa oleh dokumen SDLC lain.

- [ ] **[V8-01]** Periksa apakah **strategi backup 3-tier** (Tier 1 Harian Otomatis, Tier 2 Bulanan Manual, Tier 3 Tahunan Arsip) sudah mencakup skenario kegagalan di setiap tier dan bagaimana cara memulihkannya.
- [ ] **[V8-02]** Periksa apakah prosedur **Graceful Shutdown saat Mati Listrik** (Bab 13.6) sudah mencantumkan batas waktu kritis: UPS mampu menyangga ≥ 15 menit, dan administrator harus menyelesaikan graceful shutdown dalam < 10 menit sebelum baterai UPS drop total.
- [ ] **[V8-03]** Periksa apakah prosedur **rotasi kunci keamanan** sudah mencakup semua 5 item kredensial yang wajib dirotasi (JWT Secret Key, Fernet Key, Database Password User App, Sandi Root Server, Sandi Supervisor) beserta frekuensinya masing-masing di Bab 14.1.
- [ ] **[V8-04]** Periksa apakah **Bab Troubleshooting** (Bab 17) sudah mencakup setidaknya 9 kategori masalah: koneksi database (ERR-DB), otentikasi (ERR-AUTH), sesi expired (ERR-SESSION), backup gagal (ERR-FILE), selisih kas (ERR-CASH), rendering CLI (mojibake), printer thermal, performa query lambat, dan stok desimal tidak sinkron.
- [ ] **[V8-05]** Periksa apakah **prosedur penanganan fraud internal** (selisih kas berulang, retur abnormal) sudah mencakup 3 fase: Isolasi Sementara → Penelusuran Audit → Rekonsiliasi Fisik.
- [ ] **[V8-06]** Periksa apakah **prosedur UU PDP No. 27/2022** sudah mengakomodasi 2 aspek wajib: (a) verifikasi 100% data WhatsApp pelanggan terenkripsi Fernet di database, dan (b) simulasi hard delete CRM pelanggan dengan cascade yang aman tanpa merusak integritas relasi transaksi historis.
- [ ] **[V8-07]** Periksa apakah **prosedur penambahan node klien baru** (Bab 11.5) sudah mencakup langkah konfigurasi `APP_CABANG_ID` dan `PRINTER_PORT` di `.env` klien baru, serta Smoke Test akhir (ST-01 s.d ST-06) sebelum operasional.
- [ ] **[V8-08]** Periksa apakah **koneksi pool database** dan **retry mechanism** (Bab 15.5) sudah menjelaskan: nama pool (`'abupool'`), ukuran pool (`pool_size = 5`), jumlah retry (3 kali), dan strategi backoff (exponential backoff 2^n detik) sebelum melempar `ERR-DB-001`.
- [ ] **[V8-09]** Periksa apakah seluruh prosedur yang melibatkan **dual-OS** (Debian 12 server dan Windows 11 klien) sudah secara eksplisit menyebutkan di OS mana perintah dijalankan, sehingga tidak ada potensi kesalahan eksekusi perintah Linux di Windows atau sebaliknya.
- [ ] **[V8-10]** Periksa apakah ada instruksi pemeliharaan untuk **sistem laci kasir RJ11** (konektor pemicu buka laci secara elektrik melalui printer thermal) yang perlu diverifikasi koneksinya secara berkala sebagai bagian dari SOP mingguan atau bulanan.

---

### FASE 10 — KOMPILASI TEMUAN DAN PENYUSUNAN DOKUMEN REVISI

> **Tujuan**: Menuangkan seluruh hasil validasi ke dalam dokumen revisi final yang akan dituliskan ke target file.

- [ ] **[KOMPILASI-01]** Buat daftar internal semua temuan dari Fase 2 hingga Fase 9 yang memerlukan koreksi atau penambahan konten. Kategorikan menjadi: (a) Koreksi Minor (ejaan, formatting, kata "and"), (b) Koreksi Data (nilai parameter, nama tabel, path), (c) Penambahan Konten (poin checklist yang kurang, prosedur yang belum ada), (d) Restrukturisasi (urutan bab, format sub-bab).
- [ ] **[KOMPILASI-02]** Terapkan **semua koreksi dan penambahan** dari daftar temuan ke dalam draft dokumen revisi yang siap dituliskan.
- [ ] **[KOMPILASI-03]** Perbarui **Riwayat Perubahan Dokumen**: tambahkan baris baru di tabel dengan versi `1.1`, tanggal revisi hari ini, deskripsi perubahan yang komprehensif (sebutkan jumlah temuan yang diperbaiki dan dimensi validasi yang dilakukan), dan nama penyusun/revisor.
- [ ] **[KOMPILASI-04]** Perbarui **frontmatter YAML** di baris paling atas dokumen: ubah `versi: 1.0` menjadi `versi: 1.1`, perbarui `tanggal` menjadi tanggal revisi hari ini, dan ubah `status` dari `Draft` menjadi `Revised`.
- [ ] **[KOMPILASI-05]** Jika dalam proses validasi ditemukan bahwa dokumen memerlukan referensi file tambahan di luar R-01 s.d R-14 yang sudah ada (misalnya ditemukan ada dokumen SDLC lain yang relevan tetapi belum direferensikan), tambahkan referensi tersebut sebagai baris baru di **Bab 22 Referensi** di bagian paling bawah tabel.

---

### FASE 11 — PENULISAN OVERWRITE FILE (WAJIB TUNTAS TANPA PEMOTONGAN)

> **[PERINGATAN KERAS — INSTRUKSI MUTLAK]**
> Fase ini adalah fase paling kritis. Kamu WAJIB menuliskan seluruh isi dokumen hasil revisi ke dalam file target dengan ketentuan sebagai berikut:

- [ ] **[OW-01]** Tuliskan **seluruh isi dokumen hasil revisi** ke file `docs/sdlc/07_maintenance/01_maintenance_guide.md` menggunakan mode **overwrite** (timpa isi lama sepenuhnya).
- [ ] **[OW-02]** **DILARANG KERAS** memotong, meringkas, menghilangkan, atau menggunakan placeholder seperti `[... konten sebelumnya ...]` atau `[lanjutan]` di bagian mana pun. Seluruh teks dari baris pertama hingga baris terakhir **HARUS ditulis ulang sepenuhnya**.
- [ ] **[OW-03]** Pastikan dokumen hasil overwrite dimulai dengan frontmatter YAML yang telah diperbarui (versi `1.1`) dan diakhiri dengan baris penutup yang sama seperti dokumen aslinya (baris footer `*Dokumen panduan teknis operasional...`).
- [ ] **[OW-04]** Setelah penulisan selesai, lakukan **verifikasi cepat** dengan membaca ulang minimal 10 baris pertama dan 10 baris terakhir file yang baru ditulis untuk memastikan tidak ada truncation di awal atau akhir file.
- [ ] **[OW-05]** Periksa **jumlah baris total** file hasil overwrite. File hasil revisi diperkirakan memiliki jumlah baris yang **sama atau lebih banyak** dari file asli (≥ 1.305 baris). Jika jumlah baris lebih sedikit dari 1.200, ini adalah indikasi truncation dan penulisan harus diulang dari awal.
- [ ] **[OW-06]** Jika dalam proses validasi ditemukan penambahan file referensi baru, pastikan referensi tersebut sudah ditambahkan di **bagian akhir baris paling bawah tabel Bab 22** sebelum baris footer dokumen.

---

### FASE 12 — VERIFIKASI AKHIR PASCA-OVERWRITE

- [ ] **[VERIFY-01]** Baca ulang **Bab 1 (Informasi Dokumen)** hasil revisi. Pastikan frontmatter sudah menampilkan `versi: 1.1` dan `status: Revised`.
- [ ] **[VERIFY-02]** Baca ulang **tabel Riwayat Perubahan**. Pastikan baris v1.1 sudah muncul dengan deskripsi perubahan yang informatif.
- [ ] **[VERIFY-03]** Baca ulang **Bab 22 Referensi**. Pastikan semua 14 referensi (R-01 s.d R-14) masih ada, dan jika ada referensi tambahan, sudah ditambahkan dengan kode ref baru (R-15 dst.).
- [ ] **[VERIFY-04]** Pastikan semua **blok kode** (bash, sql, cmd) masih memiliki tag bahasa yang benar (` ```bash `, ` ```sql `, ` ```cmd `) dan tidak ada yang kehilangan baris pembuka atau penutup blok kode.
- [ ] **[VERIFY-05]** Pastikan semua **diagram Mermaid** masih memiliki tag ` ```mermaid ` yang benar dan tidak ada node atau edge yang hilang.
- [ ] **[VERIFY-06]** Laporkan secara singkat di akhir proses: berapa banyak temuan yang diperbaiki, apa saja temuan terpenting, dan konfirmasi bahwa dokumen sudah siap sebagai referensi fase SDLC selanjutnya.

---

## Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **SELESAI** jika dan hanya jika seluruh kondisi berikut terpenuhi:

| No | Kriteria | Status |
|:---:|---|:---:|
| 1 | Seluruh 14 dokumen referensi (R-01 s.d R-14) sudah dibaca dan dipahami | `[ ]` |
| 2 | Semua 18 item komparasi referensi (V1-01 s.d V1-18) sudah diperiksa | `[ ]` |
| 3 | Semua 5 item relevansi konten (V2-01 s.d V2-05) sudah diperiksa | `[ ]` |
| 4 | Semua 12 item standar struktur (V3-01 s.d V3-12) sudah diperiksa | `[ ]` |
| 5 | Semua 6 item kelayakan referensi (V4-01 s.d V4-06) sudah diperiksa | `[ ]` |
| 6 | Semua 8 item kualitas bahasa (V5-01 s.d V5-08) sudah diperiksa | `[ ]` |
| 7 | Semua 6 item kelengkapan data (V6-01 s.d V6-06) sudah diperiksa | `[ ]` |
| 8 | Semua 5 item kelancaran SDLC (V7-01 s.d V7-05) sudah diperiksa | `[ ]` |
| 9 | Semua 10 item ciri khas maintenance (V8-01 s.d V8-10) sudah diperiksa | `[ ]` |
| 10 | Draft revisi sudah dikompilasi dengan semua koreksi diterapkan | `[ ]` |
| 11 | File target berhasil di-overwrite dengan dokumen revisi v1.1 secara penuh tanpa truncation | `[ ]` |
| 12 | Verifikasi akhir pasca-overwrite (VERIFY-01 s.d VERIFY-06) sudah dilakukan | `[ ]` |
| 13 | Versi dokumen sudah berubah dari `v1.0` menjadi `v1.1` | `[ ]` |
| 14 | Status dokumen sudah berubah dari `Draft` menjadi `Revised` | `[ ]` |

---

## Catatan Penting untuk Pelaksana

> **[CATATAN 1 — LARANGAN INTERUPSI]**
> Kamu **tidak diperbolehkan** berhenti di tengah proses untuk meminta konfirmasi atau persetujuan dari siapa pun. Seluruh keputusan teknis dalam lingkup validasi dan perbaikan dokumen ini adalah tanggung jawabmu sepenuhnya. Eksekusi issue ini hingga selesai secara mandiri.

> **[CATATAN 2 — LARANGAN TRUNCATION]**
> Jangan pernah menghasilkan output yang mengandung kalimat seperti "... (konten lanjutan sama seperti sebelumnya) ...", "... (terpotong karena panjang) ...", atau "... (lihat file asli untuk kelanjutan) ...". Semua isi harus ditulis ulang secara lengkap tanpa pengecualian.

> **[CATATAN 3 — PRIORITAS SUMBER KEBENARAN]**
> Jika terdapat konflik data antara dokumen utama dengan dokumen referensi, prioritas sumber kebenaran adalah: **R-04 (Environment Config) > R-03 (Security Design) > R-02 (System Architecture) > R-01 (Deployment Guide) > R-05 (Release Notes)**.

> **[CATATAN 4 — PENANGANAN DATA TIDAK TERSEDIA]**
> Jika ada data yang genuinely tidak tersedia di seluruh referensi yang ada (misalnya nomor kontak support, atau detail inventaris hardware yang tidak disebutkan di dokumen mana pun), tandai data tersebut dengan format: `[DATA: DIISI OLEH PEMILIK USAHA — Alfatih]` agar jelas dan tidak membingungkan pembaca berikutnya.

> **[CATATAN 5 — TAMBAHAN REFERENSI BARU]**
> Jika dalam proses validasi kamu menemukan bahwa dokumen ini perlu mereferensikan file SDLC lain yang belum masuk ke daftar R-01 s.d R-14, tambahkan referensi baru tersebut di Bab 22 dengan kode ref R-15, R-16, dst. Pastikan penambahan ini dicatat di tabel Riwayat Perubahan.

---

*Issue ini dibuat oleh: Senior Antigravity AI Architect — 2026-05-27*
*Untuk dieksekusi oleh: Junior Programmer atau LLM AI Model (Small/Cheap)*
