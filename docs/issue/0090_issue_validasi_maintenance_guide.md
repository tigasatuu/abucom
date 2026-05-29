---
judul         : Validasi, Audit, dan Penyempurnaan Dokumen Maintenance Guide
target_file   : docs/sdlc/07_maintenance/01_maintenance_guide.md
lokasi_ref    : docs/sdlc/
prioritas     : Tinggi
status        : Open
dibuat_pada   : 2026-05-30
dibuat_oleh   : Senior IT Service Manager & Maintenance Operations Architect
---

# Validasi, Audit, dan Penyempurnaan Dokumen Maintenance Guide

## 1. Ringkasan Issue

Dokumen **Maintenance Guide** (`docs/sdlc/07_maintenance/01_maintenance_guide.md`) adalah panduan teknis operasional pemeliharaan sistem AbuCom pasca Go-Live yang menjadi **deliverable pertama dan satu-satunya pada Fase 07 — Maintenance** dalam siklus SDLC. Dokumen ini menjadi acuan tunggal bagi pemilik usaha, kepala percetakan, kasir, system administrator, dan tim pengembang AI dalam menjalankan seluruh prosedur pemeliharaan rutin, korektif, adaptif, perfektif, dan darurat.

Mengingat dokumen ini berfungsi sebagai **Single Source of Truth (SSoT)** untuk seluruh kegiatan operasional pemeliharaan jangka panjang, dokumen ini wajib divalidasi secara menyeluruh untuk memastikan:
- Kelengkapan dan akurasi penyerapan data dari **14 dokumen referensi (R-01 s.d R-14)**.
- Kepatuhan terhadap standar struktur dokumen praktik industri nyata (ITIL v4, IEEE 14764).
- Kemampuannya sebagai sumber referensi yang andal bagi fase SDLC pasca-maintenance (misalnya Changelog, Backup & Recovery Procedure).
- Kejelasan bahasa Indonesia yang tidak ambigu bagi staf operasional non-teknis maupun LLM model yang lebih kecil.

---

## 2. Persona Validator

> **Persona yang wajib digunakan selama seluruh proses validasi ini:**
>
> Kamu adalah seorang **Senior IT Service Manager & Maintenance Operations Architect** dengan pengalaman lebih dari 15 tahun dalam merancang, mengimplementasikan, dan mengaudit prosedur operasional pemeliharaan sistem informasi retail skala UMKM dan enterprise di lingkungan luring (*offline-first*).
>
> Keahlianmu mencakup:
> - **Standar ITIL v4** (Service Operation, Continual Service Improvement) dan **IEEE 14764** (Software Maintenance Standard).
> - Desain **SOP Runbook** harian, mingguan, bulanan, kuartalan, semesteran, dan tahunan beserta checklist operasional yang bisa diaudit.
> - **Disaster Recovery Planning (DRP)** dan **Business Continuity Planning (BCP)** untuk sistem database dual-OS luring offline.
> - Audit keamanan teknis pada lapisan OS hardening, firewall, kredensial enkripsi, dan RBAC berbasis peran staf toko.
> - Penulisan dokumentasi teknis operasional yang bersih, tegas, tidak ambigu, dan dapat dieksekusi secara langsung oleh staf non-teknis maupun LLM model AI dengan konteks terbatas.
>
> Kamu sangat teliti, kritis, dan tidak akan meloloskan dokumen yang memiliki data kosong, instruksi ambigu, atau informasi yang tidak relevan dengan lingkup pemeliharaan sistem informasi toko percetakan AbuCom CLI berbasis Python FP luring LAN.

---

## 3. Konteks Teknis Dokumen Target

Sebelum memulai validasi, pahami konteks berikut sebagai landasan analisis:

| Atribut | Detail |
|---|---|
| **Nama Dokumen** | Maintenance Guide |
| **Target File** | `docs/sdlc/07_maintenance/01_maintenance_guide.md` |
| **Versi Saat Ini** | v1.1 |
| **Status** | Revised |
| **Fase SDLC** | Fase 07 — Maintenance (Deliverable #1) |
| **Dokumen Input** | 14 Referensi (R-01 s.d R-14) dari Fase 01 s.d 06 |
| **Dokumen Output** | Maintenance Logbook, Incident Report Form, Patch Release Notes |
| **Sistem yang Dipelihara** | AbuCom CLI — Sistem dual-OS (Debian 12 + Windows 11), Python 3.14.2+, MySQL 8.4 LTS, 10 Modul, 28 Tabel InnoDB, offline-only LAN |
| **Audiens Dokumen** | Pemilik Usaha, Kepala Percetakan, Kasir, SysAdmin, Tim Pengembang AI |

---

## 4. Daftar Referensi yang Wajib Dibaca

Sebelum memulai validasi, baca seluruh file referensi berikut **secara menyeluruh**. Catat poin data kritis yang relevan dengan lingkup pemeliharaan dari masing-masing referensi.

| Kode | Path File Referensi | Prioritas |
|:---:|---|:---:|
| **R-01** | `docs/sdlc/06_deployment/01_deployment_guide.md` | PRIMER |
| **R-02** | `docs/sdlc/03_design/03_system_architecture.md` | PRIMER |
| **R-03** | `docs/sdlc/03_design/06_security_design.md` | PRIMER |
| **R-04** | `docs/sdlc/06_deployment/02_environment_config.yaml` | PRIMER |
| **R-05** | `docs/sdlc/06_deployment/03_release_notes.md` | PRIMER |
| **R-06** | `docs/sdlc/04_implementation/02_environment_setup.md` | SEKUNDER |
| **R-07** | `docs/sdlc/05_testing/04_bug_report_template.md` | SEKUNDER |
| **R-08** | `docs/sdlc/05_testing/01_test_plan.md` | SEKUNDER |
| **R-09** | `docs/sdlc/04_implementation/01_coding_standard.md` | SEKUNDER |
| **R-10** | `docs/sdlc/04_implementation/04_git_workflow.md` | SEKUNDER |
| **R-11** | `docs/sdlc/01_planning/04_tech_stack_decision.md` | SEKUNDER |
| **R-12** | `docs/sdlc/02_analysis/02_software_requirements.md` | TERSIER |
| **R-13** | `docs/sdlc/03_design/01_database_schema.sql` | TERSIER |
| **R-14** | `docs/sdlc/04_implementation/03_module_structure.md` | TERSIER |

---

## 5. Kriteria Validasi dan Instruksi Pemeriksaan

Lakukan validasi secara **berurutan** sesuai kriteria di bawah ini. Setiap kriteria adalah dimensi analisis yang independen dan harus diperiksa secara menyeluruh.

---

### Kriteria 1 — Komparasi Mendalam: Dokumen Utama vs. File Referensi

**Tujuan**: Memastikan bahwa seluruh data dan informasi penting yang ada di 14 file referensi telah terserap dengan tepat ke dalam dokumen utama, dan tidak ada detail kritis yang terlewat.

**Instruksi pemeriksaan**:

Untuk setiap referensi (R-01 s.d R-14), lakukan perbandingan biner antara isi referensi dan dokumen utama:

1. **R-01 (Deployment Guide)**: Verifikasi apakah prosedur runbook startup/shutdown server, skrip cron backup otomatis `backup_cron.sh`, parameter jaringan IP statis `192.168.1.200`, dan prosedur disaster recovery sudah disadur secara akurat. Periksa apakah skrip `backup_cron.sh` pada dokumen sudah menggunakan `/root/.my.cnf` dan variabel `$ZIP_PASSWORD` yang membaca dari file `.env` (bukan kata sandi hardcoded langsung di skrip). Periksa juga apakah seluruh prosedur Smoke Test (ST-01 s.d ST-06) sudah tertera.
2. **R-02 (System Architecture)**: Verifikasi apakah diagram arsitektur deployment, matriks node (server Debian + klien Windows 11), daftar 10 modul fungsional (M.1 s.d M.10), daftar 28 tabel InnoDB dalam 5 kelompok, daftar pustaka dependensi, mekanisme connection pooling, dan retry mechanism sudah akurat dan lengkap.
3. **R-03 (Security Design)**: Verifikasi apakah seluruh kode error keamanan (`ERR-AUTH-001` s.d `ERR-AUTH-029`, `ERR-SESSION-001`, `ERR-SESSION-002`, `ERR-DB-001`, `ERR-DB-002`, `ERR-FILE-001`, `ERR-FILE-039`, `ERR-CASH-001`, `ERR-CASH-004`) sudah terdokumentasi dalam Troubleshooting Guide. Periksa juga apakah prosedur hardening OS (PermitRootLogin, AutoPlay Windows, chmod 600 `.my.cnf`) sudah tercakup. Pastikan semua lapisan *defense in depth* (6 layer) disebutkan secara konsisten.
4. **R-04 (Environment Config)**: Verifikasi apakah semua variabel `.env` kritis (`DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `JWT_SECRET_KEY`, `FERNET_KEY`, `BACKUP_ZIP_PASSWORD`, `PRINTER_PORT`, `PRINTER_WIDTH_MM`) sudah disebutkan dengan benar dalam konteks pemeliharaan, rotasi kredensial, dan troubleshooting.
5. **R-05 (Release Notes)**: Verifikasi apakah daftar modul aktif (M.1 s.d M.10), known issues (`DEF-COMPAT-001`, `DEF-PERF-001`), known limitations, dan roadmap upgrade versi sudah terintegrasi dalam dokumen utama pada bagian yang relevan (troubleshooting, perencanaan upgrade).
6. **R-06 (Environment Setup)**: Verifikasi apakah prosedur setup ulang Python 3.14.2+, MySQL Server 8.4 LTS pada server baru (Disaster Recovery), dan instalasi dependensi luring dari `requirements.txt` sudah tercakup di bagian Pemeliharaan Adaptif dan Disaster Recovery.
7. **R-07 (Bug Report Template)**: Verifikasi apakah klasifikasi severity (S1-S5), priority (P1-P4), SLA penanganan bug, dan format form tiket bug sudah diterapkan secara akurat pada Bab 10 (Pemeliharaan Korektif).
8. **R-08 (Test Plan)**: Verifikasi apakah kriteria exit pengujian (pass rate 100%, coverage ≥ 90%), prosedur regression test pytest, dan daftar Smoke Test (ST-01 s.d ST-06) sudah tercantum di bagian Deployment Patch.
9. **R-09 (Coding Standard)**: Verifikasi apakah constraint FP Python murni (no class, no global state, explicit UTF-8), penggunaan `decimal.Decimal` dengan `ROUND_HALF_UP`, dan standar gitignore sudah disebut pada bagian Prosedur Pengembangan Patch.
10. **R-10 (Git Workflow)**: Verifikasi apakah alur branching (`patch/`, `hotfix/`), format commit message, merge ke `main`, dan tagging rilis (e.g., `v1.0.1`) sudah dijelaskan pada prosedur deployment patch dengan tepat.
11. **R-11 (Tech Stack Decision)**: Verifikasi apakah batasan teknologi yang terkunci (`Python 3.14.2+`, `MySQL 8.4 LTS`, `requirements.txt` offline wheels) sudah konsisten disebutkan pada prosedur pemeliharaan adaptif dan upgrade.
12. **R-12 (SRS)**: Verifikasi apakah spesifikasi non-fungsional (performa response time ≤ 2 detik, ketersediaan, portabilitas dual-OS) sudah tercermin dalam SLA, matriks risiko, dan checklist pemeliharaan.
13. **R-13 (Database Schema)**: Verifikasi apakah 28 tabel InnoDB yang disebutkan di dokumen sudah sesuai dengan DDL skema database aktual. Periksa apakah kelompok tabel (A, B, C, D, E) dan nama-nama tabel sudah benar dan tidak ada yang kurang atau kelebihan.
14. **R-14 (Module Structure)**: Verifikasi apakah struktur direktori modul pada klien Windows (`C:\Users\kasir\Documents\abucom\`) sudah konsisten disebut di seluruh bagian prosedur yang relevan (rotasi log, direktori backup manual).

**Tandai temuan** dengan format berikut:
- `[KURANG]` — data/informasi dari referensi yang belum ada di dokumen utama.
- `[TIDAK AKURAT]` — data yang ada namun bertentangan atau tidak sinkron dengan referensi.
- `[OK]` — data yang sudah akurat dan lengkap.

---

### Kriteria 2 — Kebersihan Konten: Relevansi dan Fokus Dokumen

**Tujuan**: Memastikan dokumen utama hanya memuat data dan informasi yang memang relevan dan dibutuhkan oleh sebuah **Maintenance Guide** operasional, bukan menjadi duplikasi dokumen lain.

**Instruksi pemeriksaan**:

Periksa setiap bab dan sub-bab dokumen:

1. Apakah ada konten yang seharusnya berada di dokumen lain (misalnya: spesifikasi fungsional detail yang seharusnya di SRS, detail DDL database yang seharusnya di Database Schema, atau kode sumber lengkap yang seharusnya di Coding Standard)?
2. Apakah ada pengulangan konten yang identik antara dua atau lebih sub-bab tanpa tambahan nilai informasi?
3. Apakah setiap bagian dari dokumen ini memiliki tujuan operasional yang jelas bagi aktor pemeliharaan (pemilik, kepala, kasir, SysAdmin, tim AI)?
4. Apakah diagram Mermaid (arsitektur, flowchart patching, flowchart backup/restore, flowchart eskalasi insiden) sudah cukup jelas dan tidak berlebihan dalam detail?
5. Apakah ada sub-bab atau kalimat yang dapat dihapus tanpa mengurangi nilai operasional dokumen ini?

Jika ditemukan konten yang tidak relevan, **hapus atau kondensasikan** konten tersebut agar dokumen tetap bersih dan fokus.

---

### Kriteria 3 — Standar Struktur Dokumen Industri

**Tujuan**: Memastikan struktur dokumen memenuhi standar praktik industri pemeliharaan sistem informasi (ITIL v4, IEEE 14764) dan bersifat informatif.

**Instruksi pemeriksaan**:

Verifikasi keberadaan dan kelengkapan elemen-elemen struktur dokumen berikut:

1. **Header dokumen (front matter YAML)**: Pastikan memuat `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`.
2. **Riwayat Perubahan Dokumen (Changelog Tabel)**: Pastikan ada tabel dengan kolom `Versi`, `Tanggal`, `Deskripsi Perubahan`, dan `Oleh`.
3. **Informasi Dokumen (Bab 1)**: Pastikan ada sub-bab `Tujuan`, `Cakupan`, `Posisi dalam SDLC`, `Hubungan Input/Output`, `Audiens Target`, `Definisi/Akronim`, dan **Templat Format Output** (logbook, incident report, patch release notes).
4. **Ringkasan Arsitektur Sistem (Bab 2)**: Pastikan ada diagram deployment aktual, matriks komponen per node, daftar modul fungsional, daftar tabel database, dan daftar dependensi terkunci.
5. **Kategori Pemeliharaan (Bab 3)**: Pastikan 5 kategori IEEE 14764 hadir: Korektif, Preventif, Adaptif, Perfektif, dan Darurat — masing-masing dengan definisi dan contoh kasus spesifik AbuCom.
6. **SOP Runbook Berkala (Bab 4–9)**: Pastikan runbook Harian, Mingguan, Bulanan, Kuartalan, Semesteran, dan Tahunan masing-masing memiliki checklist akhir yang dapat dicentang.
7. **Pemeliharaan Korektif (Bab 10)**: Pastikan ada alur pelaporan bug, klasifikasi severity/priority, RCA, prosedur patch, deployment, rollback, SLA table, dan diagram flowchart.
8. **Pemeliharaan Adaptif (Bab 11)**: Pastikan ada prosedur upgrade Python runtime, upgrade MySQL, upgrade dependensi offline, dan prosedur penambahan node klien baru. Verifikasi apakah semua prosedur ini cukup lengkap dan actionable.
9. **Backup & Restore (Bab 12)**: Pastikan ada skrip `backup_cron.sh` lengkap, prosedur backup manual, prosedur restore, prosedur disaster recovery server baru, strategi retensi/rotasi backup, dan diagram flowchart.
10. **Penanganan Insiden & Eskalasi (Bab 13)**: Pastikan ada definisi insiden, matriks eskalasi level 1/2/3, prosedur deteksi, prosedur respon, SOP UPS, kontak darurat, dan diagram flowchart.
11. **Keamanan Sistem (Bab 14)**: Pastikan ada jadwal rotasi kredensial, prosedur manajemen akun RBAC, audit trail, penanganan fraud, hardening OS, dan UU PDP compliance.
12. **Database Maintenance (Bab 15)**: Pastikan ada prosedur CHECK TABLE/REPAIR, ANALYZE/OPTIMIZE TABLE, monitoring disk, purging log audit, verifikasi connection pool, dan migrasi multi-cabang.
13. **Hardware & Infrastruktur (Bab 16)**: Pastikan ada jadwal pemeriksaan hardware berkala, prosedur penggantian komponen (SSD, RAM, UPS, kabel LAN, printer thermal), dan tabel inventaris aset.
14. **Troubleshooting Guide (Bab 17)**: Pastikan setiap kasus troubleshooting memiliki: Gejala, Kemungkinan Penyebab, Langkah Solusi step-by-step, dan Pencegahan.
15. **Matriks Risiko (Bab 18)**: Pastikan ada identifikasi risiko operasional, tabel matriks risiko (probabilitas, dampak, skor), dan rencana kontingensi per risiko.
16. **RACI Matrix (Bab 19)**: Pastikan ada matriks RACI untuk seluruh aktivitas pemeliharaan utama, beserta narasi tanggung jawab per peran (5 peran).
17. **Kalender Pemeliharaan (Bab 20)**: Pastikan ada tabel kalender tahunan visual dan ringkasan frekuensi aktivitas.
18. **Glosarium (Bab 21)**: Pastikan semua akronim dan istilah teknis yang digunakan di dokumen ini sudah terdefinisi di glosarium.
19. **Referensi Dokumen (Bab 22)**: Pastikan 14 referensi terdaftar lengkap dengan path, prioritas, dan peran masing-masing.

---

### Kriteria 4 — Kualitas sebagai Referensi Fase SDLC Selanjutnya

**Tujuan**: Memastikan dokumen ini dapat menjadi referensi yang andal bagi dokumen-dokumen lain dalam ekosistem SDLC AbuCom, khususnya dokumen-dokumen dalam fase pemeliharaan (Changelog, Backup & Recovery Procedure).

**Instruksi pemeriksaan**:

1. Periksa apakah dokumen ini mendefinisikan dengan jelas **format dan standar Maintenance Logbook** (harian/mingguan/bulanan) yang dapat langsung digunakan oleh dokumen Changelog (`02_changelog.md`).
2. Periksa apakah prosedur **Backup & Restore** sudah cukup detail dan akurat untuk dijadikan referensi utama oleh dokumen `03_backup_recovery_procedure.md` di folder yang sama.
3. Periksa apakah **SLA, klasifikasi severity, dan format Incident Report** sudah terdefinisi cukup terperinci agar dapat dijadikan sumber acuan tunggal bagi staf operasional.
4. Periksa apakah **Matriks RACI** dan **Kalender Pemeliharaan** cukup komprehensif sebagai panduan manajemen operasional jangka panjang.
5. Periksa apakah **Troubleshooting Guide** sudah mencakup seluruh kode error yang teridentifikasi di R-03 (Security Design), dan apakah setiap langkah solusi dapat dieksekusi tanpa dokumen tambahan.
6. Periksa apakah **Prosedur Pemeliharaan Adaptif (Bab 11)** sudah cukup mendetail sebagai panduan upgrade mandiri tanpa perlu membaca ulang dokumen Environment Setup (R-06) secara keseluruhan.
7. Identifikasi apakah ada celah informasi yang akan menyebabkan LLM model kecil atau junior programmer harus bertanya atau menginterupsi proses kerja mereka saat mengeksekusi prosedur ini.

---

### Kriteria 5 — Kualitas Bahasa Indonesia

**Tujuan**: Memastikan seluruh teks menggunakan Bahasa Indonesia yang natural, tidak ambigu, konsisten, dan dapat dipahami oleh staf non-teknis maupun LLM model AI dengan kemampuan bahasa terbatas.

**Instruksi pemeriksaan**:

1. **Konsistensi istilah**: Periksa apakah istilah teknis yang sama digunakan secara konsisten di seluruh dokumen (misalnya: selalu "laci kasir" bukan bergantian "cash drawer" atau "drawer kasir"; selalu "pengembang AI" bukan bergantian "developer" atau "tim dev").
2. **Kata serapan asing**: Periksa apakah ada kata asing yang tidak perlu dan dapat diganti dengan padanan Bahasa Indonesia yang sudah baku (misalnya: "backup" yang sudah lazim dipertahankan, tetapi "error" sebaiknya "eror" sesuai KBBI dalam konteks teknis informal).
3. **Struktur kalimat**: Periksa apakah ada kalimat yang terlalu panjang (lebih dari 3 klausa), ambigu, atau memiliki subjek yang tidak jelas.
4. **Instruksi prosedural**: Setiap langkah prosedur (SOP) harus diawali dengan kata kerja aktif imperatif yang jelas (misalnya: "Buka", "Jalankan", "Pastikan", "Verifikasi", "Eksekusi").
5. **Konsistensi format**: Periksa apakah penomoran bab, sub-bab, dan daftar butir sudah konsisten di seluruh dokumen. Periksa apakah kode error selalu ditulis dalam format backtick (`` `ERR-XXX-XXX` ``).
6. **Komentar blok kode**: Periksa apakah setiap blok kode sudah memiliki komentar penanda OS/konteks di baris pertama (format: `# [LINUX DEBIAN 12 — Server]` atau `# [WINDOWS 11 — Klien]` atau `-- [LINUX DEBIAN 12 — Server] — MySQL Console`).
7. **Tidak ada kata hubung bahasa asing**: Pastikan tidak ada kata hubung asing seperti "and", "or", "with", "for", "via" yang berdiri sendiri tanpa konteks teknis. Gantikan dengan "dan", "atau", "dengan", "untuk", "lewat".

---

### Kriteria 6 — Pemeriksaan Data Kosong dan Placeholder

**Tujuan**: Mengidentifikasi dan mengisi semua data yang kosong, placeholder belum terisi, atau keterangan "diisi manual" yang menghambat operasional dokumen.

**Instruksi pemeriksaan**:

Lakukan pencarian menyeluruh (baca baris demi baris) untuk menemukan pola berikut:
- Teks yang mengandung `[DATA: DIISI OLEH...]`
- Teks yang mengandung `[TBD]`, `[TODO]`, `[...]`, `[BELUM TERSEDIA]`
- Tabel dengan sel kosong yang seharusnya berisi data
- Variabel atau parameter yang membutuhkan nilai konkret namun masih berupa placeholder

**Khusus untuk data kontak darurat (Bab 13.7)**:

Saat ini Bab 13.7 "Kontak Darurat dan Jalur Eskalasi" berisi placeholder berikut yang belum terisi:
```
DevOps Technical Support Line : [DATA: DIISI OLEH PEMILIK USAHA — Alfatih]
Email Dukungan Resmi          : [DATA: DIISI OLEH PEMILIK USAHA — Alfatih]
```

Karena data ini bersifat personal dan rahasia (nomor telepon dan email nyata pemilik usaha), **jangan diisi dengan data palsu**. Namun, **wajib ditambahkan** sub-bab **"Prosedur Pengisian Kontak Darurat"** dengan instruksi yang jelas tentang kapan dan bagaimana Pemilik Usaha (Alfatih) harus mengisi data ini, beserta format contoh pengisian yang bisa diikuti. Ini untuk memastikan dokumen tidak menggantung dengan placeholder yang tidak pernah diisi.

**Untuk data lain yang kosong**: Isi dengan data yang sesuai, relevan, dan masih dalam ruang lingkup dokumen Maintenance Guide ini. Jangan mengarang data yang tidak bisa diverifikasi.

---

### Kriteria 7 — Pemeriksaan Khusus Spesifik Maintenance Guide

**Tujuan**: Memvalidasi aspek-aspek teknis yang spesifik untuk dokumen Maintenance Guide sistem AbuCom yang tidak tercakup dalam kriteria umum di atas.

**Instruksi pemeriksaan**:

1. **Keamanan Skrip Cron Backup**: Verifikasi bahwa skrip `backup_cron.sh` (Bab 12.2) **tidak** menuliskan kata sandi root MySQL secara langsung (*hardcoded*) dalam argumen perintah `mysqldump`. Pastikan sudah menggunakan mekanisme `/root/.my.cnf` dengan `--defaults-extra-file` untuk keamanan. Periksa juga apakah variabel `$ZIP_PASSWORD` sudah membaca nilai dari file `.env` (bukan hardcoded).

2. **Konsistensi Versi Referensi**: Verifikasi apakah versi dokumen referensi yang disebutkan (misal: "Deployment Guide v1.1") sudah konsisten dengan versi aktual dokumen referensi yang ada di file system.

3. **Kelengkapan Kode Error Troubleshooting**: Dokumen ini memiliki Bab 17 (Troubleshooting Guide) dengan 12 kasus. Verifikasi apakah seluruh kode error yang didefinisikan di R-03 (Security Design) sudah tercakup. Jika ada kode error dari R-03 yang belum ada sub-babnya di Bab 17, tambahkan sub-bab baru.

4. **Kelengkapan Bab Pemeliharaan Adaptif (Bab 11)**: Baca ulang bab ini secara khusus. Pastikan ada prosedur detail untuk: (a) upgrade Python runtime secara offline dari source, (b) upgrade MySQL 8.4 LTS secara offline, (c) update `requirements.txt` dengan wheel baru, dan (d) prosedur penambahan node klien kasir baru ke jaringan LAN. Jika prosedur ini tidak cukup detail dan actionable, perluas kontennya.

5. **Integritas Internal Referensi Silang (Cross-reference)**: Pastikan setiap referensi silang antar bab dalam dokumen ini akurat (misalnya: "Bab 12" yang disebut di Bab 13 benar-benar merujuk ke bab yang tepat).

6. **Validasi Nomor Port dan IP**: Pastikan semua nomor port (3306 MySQL), alamat IP (192.168.1.200 server, 192.168.1.1 gateway), dan segment subnet (192.168.1.0/24) konsisten di seluruh dokumen dan sesuai dengan R-02 dan R-04.

7. **Validasi Nama Tabel Database**: Pastikan seluruh nama tabel database yang disebutkan dalam perintah SQL di dokumen ini konsisten dengan 28 tabel yang terdaftar di Bab 2.4 dan di R-13 (Database Schema).

8. **Validasi Nama Variabel .env**: Pastikan semua nama variabel `.env` yang disebutkan (e.g., `DB_HOST`, `JWT_SECRET_KEY`, `FERNET_KEY`, `BACKUP_ZIP_PASSWORD`, `PRINTER_PORT`) konsisten dengan yang ada di R-04 (Environment Config).

9. **Glosarium vs. Bab 1.6**: Pastikan tidak ada istilah yang terdefinisi di Bab 1.6 (Definisi, Akronim, dan Singkatan) namun tidak ada di Glosarium (Bab 21), dan sebaliknya. Keduanya harus saling melengkapi, bukan duplikat satu sama lain.

10. **SLA Table Konsistensi**: Verifikasi bahwa waktu respon SLA yang disebutkan di Tabel SLA Bab 10.8, Matriks Eskalasi Bab 13.2, dan narasi teks lainnya sudah konsisten satu sama lain.

---

## 6. Tahapan Implementasi Issue (Step-by-Step Checklist)

Ikuti tahapan berikut **secara berurutan**. Jangan melompat ke langkah berikutnya sebelum langkah sebelumnya selesai sepenuhnya. Setiap langkah memiliki sub-tugas yang harus diselesaikan semua.

---

### Tahap 0 — Persiapan dan Pembacaan Awal

- [ ] **0.1** Baca seluruh file target dari baris pertama hingga terakhir:
  ```
  docs/sdlc/07_maintenance/01_maintenance_guide.md
  ```
  Catat jumlah total bab, sub-bab, dan baris dokumen. Pahami struktur keseluruhan sebelum mulai mengubah apapun.

- [ ] **0.2** Baca file referensi prioritas PRIMER secara menyeluruh:
  - [ ] **0.2.a** Baca `docs/sdlc/06_deployment/01_deployment_guide.md` (R-01). Catat: prosedur backup cron, skrip `backup_cron.sh`, prosedur disaster recovery, Smoke Test list.
  - [ ] **0.2.b** Baca `docs/sdlc/03_design/03_system_architecture.md` (R-02). Catat: diagram deployment, spesifikasi node, 28 tabel InnoDB, daftar dependensi, connection pool.
  - [ ] **0.2.c** Baca `docs/sdlc/03_design/06_security_design.md` (R-03). Catat: semua kode error (ERR-*), prosedur hardening OS, 6 layer defense in depth, RBAC 8 peran.
  - [ ] **0.2.d** Baca `docs/sdlc/06_deployment/02_environment_config.yaml` (R-04). Catat: semua nama variabel `.env`, nilai default, dan parameter runtime.
  - [ ] **0.2.e** Baca `docs/sdlc/06_deployment/03_release_notes.md` (R-05). Catat: modul aktif, known issues, known limitations, roadmap versi.

- [ ] **0.3** Baca file referensi prioritas SEKUNDER secara menyeluruh:
  - [ ] **0.3.a** Baca `docs/sdlc/04_implementation/02_environment_setup.md` (R-06). Catat: prosedur instalasi Python offline, MySQL setup, dependensi wheels.
  - [ ] **0.3.b** Baca `docs/sdlc/05_testing/04_bug_report_template.md` (R-07). Catat: format severity S1-S5, priority P1-P4, SLA table, form bug report.
  - [ ] **0.3.c** Baca `docs/sdlc/05_testing/01_test_plan.md` (R-08). Catat: exit criteria pytest, coverage target, daftar Smoke Test ST-01 s.d ST-06.
  - [ ] **0.3.d** Baca `docs/sdlc/04_implementation/01_coding_standard.md` (R-09). Catat: aturan FP murni, decimal.Decimal, explicit UTF-8, gitignore rules.
  - [ ] **0.3.e** Baca `docs/sdlc/04_implementation/04_git_workflow.md` (R-10). Catat: alur branching patch/hotfix, format commit, merge ke main, tagging.
  - [ ] **0.3.f** Baca `docs/sdlc/01_planning/04_tech_stack_decision.md` (R-11). Catat: platform locked (Python 3.14.2+, MySQL 8.4, FP murni).

- [ ] **0.4** Baca file referensi prioritas TERSIER:
  - [ ] **0.4.a** Baca `docs/sdlc/02_analysis/02_software_requirements.md` (R-12). Catat: spesifikasi non-fungsional (performa ≤ 2 detik, ketersediaan, portabilitas).
  - [ ] **0.4.b** Baca `docs/sdlc/03_design/01_database_schema.sql` (R-13). Catat: 28 nama tabel lengkap, kelompok A–E, dan constraints utama.
  - [ ] **0.4.c** Baca `docs/sdlc/04_implementation/03_module_structure.md` (R-14). Catat: struktur direktori klien Windows, path log files.

- [ ] **0.5** Buat catatan kerja sementara di memori/konteksmu tentang semua temuan dari langkah 0.2–0.4. Kelompokkan berdasarkan kategori: `[KURANG]`, `[TIDAK AKURAT]`, `[OK]`.

---

### Tahap 1 — Validasi Kriteria 1: Komparasi dengan Referensi

- [ ] **1.1** Periksa Bab 12 (Backup & Restore) terhadap R-01:
  - [ ] **1.1.a** Verifikasi skrip `backup_cron.sh`: Apakah variabel `$ZIP_PASSWORD` membaca dari `.env` (bukan hardcoded)?
  - [ ] **1.1.b** Verifikasi apakah ada daftar Smoke Test lengkap (ST-01 s.d ST-06) di bagian deployment patch.
  - [ ] **1.1.c** Verifikasi prosedur disaster recovery server baru (Bab 12.5) terhadap prosedur di R-01.

- [ ] **1.2** Periksa Bab 2 (Arsitektur Sistem) terhadap R-02:
  - [ ] **1.2.a** Verifikasi jumlah dan nama 28 tabel InnoDB di Bab 2.4 terhadap R-13.
  - [ ] **1.2.b** Verifikasi daftar 10 modul (M.1 s.d M.10) di Bab 2.3 terhadap R-02.
  - [ ] **1.2.c** Verifikasi daftar dependensi dan versi di Bab 2.5 terhadap R-04 dan R-02.
  - [ ] **1.2.d** Verifikasi mekanisme connection pool (pool_size=5, retry 3x, exponential backoff) di Bab 15.5 terhadap R-02.

- [ ] **1.3** Periksa Bab 17 (Troubleshooting) terhadap R-03:
  - [ ] **1.3.a** Buat daftar lengkap semua kode error yang ada di R-03 (Security Design).
  - [ ] **1.3.b** Cocokkan satu per satu dengan kasus troubleshooting di Bab 17.
  - [ ] **1.3.c** Tandai kode error dari R-03 yang belum ada sub-babnya di Bab 17 sebagai `[KURANG]`.

- [ ] **1.4** Periksa seluruh penyebutan variabel `.env` terhadap R-04:
  - [ ] **1.4.a** Buat daftar semua nama variabel `.env` yang ada di R-04.
  - [ ] **1.4.b** Periksa konsistensi nama variabel di seluruh dokumen utama.
  - [ ] **1.4.c** Tandai variabel yang tidak konsisten atau salah nama sebagai `[TIDAK AKURAT]`.

- [ ] **1.5** Periksa Bab 3 (Kategori Pemeliharaan) dan Bab 17 (Troubleshooting) terhadap R-05:
  - [ ] **1.5.a** Verifikasi known issues (`DEF-COMPAT-001`, `DEF-PERF-001`) sudah masuk di bagian yang relevan.
  - [ ] **1.5.b** Verifikasi known limitations dan roadmap upgrade disebut di Bab 9.5.

- [ ] **1.6** Periksa Bab 11 (Pemeliharaan Adaptif) terhadap R-06, R-11:
  - [ ] **1.6.a** Verifikasi prosedur upgrade Python runtime offline sudah ada dan detail.
  - [ ] **1.6.b** Verifikasi prosedur upgrade MySQL 8.4 LTS sudah ada.
  - [ ] **1.6.c** Verifikasi prosedur update `requirements.txt` dengan wheel offline sudah ada.
  - [ ] **1.6.d** Verifikasi prosedur penambahan node klien kasir baru sudah ada.

- [ ] **1.7** Periksa Bab 10 (Pemeliharaan Korektif) terhadap R-07, R-08, R-09, R-10:
  - [ ] **1.7.a** Verifikasi klasifikasi severity S1-S5 dan priority P1-P4 di Bab 10.2 akurat sesuai R-07.
  - [ ] **1.7.b** Verifikasi SLA table di Bab 10.8 konsisten dengan R-07.
  - [ ] **1.7.c** Verifikasi exit criteria pytest (pass rate 100%, coverage ≥ 90%) ada di Bab 10.4.
  - [ ] **1.7.d** Verifikasi alur branching Git (`patch/`, `hotfix/`) di Bab 10.4 sesuai R-10.
  - [ ] **1.7.e** Verifikasi aturan FP Python (no class, decimal.Decimal) disebut di Bab 10.4 sesuai R-09.

---

### Tahap 2 — Validasi Kriteria 2: Kebersihan Konten

- [ ] **2.1** Baca ulang Bab 2 (Arsitektur Sistem): Apakah ada detail DDL atau kode sumber yang seharusnya tidak ada di sini? Jika ya, catat dan kondensasikan.

- [ ] **2.2** Periksa apakah ada pengulangan prosedur yang identik antara dua sub-bab berbeda (misalnya prosedur purging log di Bab 7.3 dan Bab 15.4 — boleh ada tetapi harus berbeda konteks/frekuensinya). Jika identik tanpa perbedaan nilai, konsensasikan dengan referensi silang.

- [ ] **2.3** Periksa apakah diagram Mermaid di Bab 2.1, 10.7, 12.7, dan 13.8 sudah informatif dan tidak berlebihan. Verifikasi sintaks Mermaid valid (tidak ada node tanpa label, tidak ada edge yang menggantung).

- [ ] **2.4** Periksa apakah setiap bab memiliki tujuan yang unik dan tidak tumpang tindih dengan bab lainnya secara berlebihan.

---

### Tahap 3 — Validasi Kriteria 3: Standar Struktur Dokumen

- [ ] **3.1** Verifikasi keberadaan dan kelengkapan header YAML (baris 1–8).

- [ ] **3.2** Verifikasi Riwayat Perubahan Dokumen (tabel di awal dokumen). Pastikan ada entri untuk v1.0 dan v1.1 minimal.

- [ ] **3.3** Verifikasi Bab 1 (Informasi Dokumen): Pastikan sub-bab 1.1 s.d 1.7 semuanya hadir dan lengkap.

- [ ] **3.4** Verifikasi setiap bab SOP berkala (Bab 4, 5, 6, 7, 8, 9) memiliki checklist akhir yang dapat dicentang (format `- [ ]`).

- [ ] **3.5** Verifikasi Bab 10 memiliki: alur pelaporan, severity/priority, RCA, prosedur patch, deployment, rollback, SLA table, dan diagram flowchart.

- [ ] **3.6** Verifikasi Bab 11 (Pemeliharaan Adaptif) memiliki prosedur yang cukup actionable untuk: upgrade Python offline, upgrade MySQL offline, update dependensi offline, dan tambah node klien baru.

- [ ] **3.7** Verifikasi Bab 12 memiliki: skrip `backup_cron.sh`, backup manual, prosedur restore, disaster recovery, strategi retensi, dan diagram flowchart.

- [ ] **3.8** Verifikasi Bab 13 memiliki: definisi insiden, matriks eskalasi, prosedur deteksi, prosedur respon, SOP UPS, kontak darurat (meski placeholder), dan diagram flowchart.

- [ ] **3.9** Verifikasi Bab 14 memiliki jadwal rotasi kredensial (tabel), manajemen akun, audit trail, penanganan fraud, hardening OS, dan UU PDP compliance.

- [ ] **3.10** Verifikasi Bab 15 memiliki prosedur CHECK TABLE/REPAIR, ANALYZE/OPTIMIZE, monitoring disk, purging log, connection pool, dan migrasi multi-cabang.

- [ ] **3.11** Verifikasi Bab 16 memiliki tabel jadwal pemeriksaan hardware, prosedur penggantian per komponen, dan tabel inventaris aset dengan 7 item (AST-HW-001 s.d AST-HW-007).

- [ ] **3.12** Verifikasi Bab 17 memiliki minimal 12 kasus troubleshooting, masing-masing dengan Gejala, Kemungkinan Penyebab, Langkah Solusi, dan Pencegahan.

- [ ] **3.13** Verifikasi Bab 18 memiliki 10 identifikasi risiko, tabel matriks risiko dengan skor, dan rencana kontingensi.

- [ ] **3.14** Verifikasi Bab 19 memiliki tabel RACI dan narasi tanggung jawab per peran (5 peran: Pemilik, Kepala Percetakan, Kasir & Staf, SysAdmin, Tim AI).

- [ ] **3.15** Verifikasi Bab 20 memiliki tabel kalender tahunan dan tabel ringkasan frekuensi.

- [ ] **3.16** Verifikasi Bab 21 (Glosarium) memuat minimal semua istilah yang didefinisikan di Bab 1.6, ditambah istilah teknis kunci lainnya yang digunakan di seluruh dokumen.

- [ ] **3.17** Verifikasi Bab 22 (Referensi) memuat 14 referensi R-01 s.d R-14 dengan path, prioritas, dan peran yang lengkap.

---

### Tahap 4 — Validasi Kriteria 4: Kualitas sebagai Referensi SDLC

- [ ] **4.1** Periksa apakah **Templat Maintenance Logbook** (Bab 1.7.1) sudah cukup komprehensif untuk dijadikan acuan oleh dokumen `02_changelog.md`.

- [ ] **4.2** Periksa apakah **Bab 12 (Backup & Restore)** sudah cukup detail dan actionable untuk dijadikan referensi utama `03_backup_recovery_procedure.md`. Jika ada prosedur yang hanya disebutkan singkat tanpa langkah detail, perluas.

- [ ] **4.3** Periksa apakah **Templat Incident Report** (Bab 1.7.2) dan **Matriks Eskalasi** (Bab 13.2) sudah konsisten dan bisa dijadikan acuan tunggal operasional.

- [ ] **4.4** Identifikasi celah informasi yang akan menyebabkan eksekutor (junior programmer atau LLM kecil) bertanya atau berhenti di tengah prosedur. Tambahkan keterangan yang diperlukan.

---

### Tahap 5 — Validasi Kriteria 5: Kualitas Bahasa Indonesia

- [ ] **5.1** Lakukan pencarian dan penggantian masif pada seluruh dokumen untuk kata hubung asing yang berdiri sendiri:
  - Ganti " and " → " dan " (perhatikan konteks teknis, jangan ganti di dalam blok kode atau nama variabel).
  - Ganti " or " → " atau " (perhatikan konteks).
  - Ganti " with " → " dengan " (perhatikan konteks).

- [ ] **5.2** Periksa konsistensi istilah teknis utama di seluruh dokumen:
  - Selalu "laci kasir" (bukan "cash drawer").
  - Selalu "eror" (bukan "error") saat digunakan dalam kalimat narasi Bahasa Indonesia (kecuali dalam blok kode atau nama variabel konstanta).
  - Selalu "cadangan" atau "backup" (pilih salah satu dan konsisten dalam satu konteks).
  - Selalu "Server Debian" atau "Mini PC Server" (konsisten).

- [ ] **5.3** Periksa semua kalimat instruksional (SOP) sudah diawali kata kerja aktif imperatif.

- [ ] **5.4** Verifikasi semua blok kode memiliki komentar penanda OS di baris pertama blok:
  - `# [LINUX DEBIAN 12 — Server]` untuk perintah Bash di server.
  - `# [WINDOWS 11 — Klien]` untuk perintah CMD/PowerShell di klien kasir.
  - `# [ANY OS — Development]` untuk perintah Git yang bisa dijalankan di mana saja.
  - `-- [LINUX DEBIAN 12 — Server] — MySQL Console` untuk perintah SQL.

- [ ] **5.5** Periksa kode error selalu ditulis dalam backtick: `` `ERR-DB-001` ``, bukan tanpa format atau dengan format lain.

---

### Tahap 6 — Validasi Kriteria 6: Data Kosong dan Placeholder

- [ ] **6.1** Lakukan pencarian di seluruh dokumen untuk string: `[DATA`, `[TBD`, `[TODO`, `[BELUM`, `[...]`.

- [ ] **6.2** Untuk **Bab 13.7 (Kontak Darurat)**:
  - [ ] **6.2.a** Pertahankan baris placeholder `[DATA: DIISI OLEH PEMILIK USAHA — Alfatih]` apa adanya karena data ini bersifat personal.
  - [ ] **6.2.b** **Tambahkan** sub-bab baru `13.7.1. Prosedur Pengisian Kontak Darurat` tepat di bawah baris placeholder tersebut, berisi instruksi langkah-langkah bagi Pemilik Usaha (Alfatih) untuk mengisi data kontak darurat, kapan data ini harus diisi, dan contoh format pengisian yang bisa diikuti.

- [ ] **6.3** Periksa apakah ada sel tabel yang kosong tanpa keterangan "—" (tanda tidak berlaku). Pastikan setiap sel tabel yang kosong diisi "—" jika memang tidak berlaku, atau diisi data yang relevan jika seharusnya ada data.

- [ ] **6.4** Periksa apakah ada deskripsi prosedur yang belum lengkap (misalnya "lihat Bab X" tetapi Bab X yang dirujuk tidak ada atau tidak membahas hal tersebut).

---

### Tahap 7 — Validasi Kriteria 7: Aspek Spesifik Maintenance Guide

- [ ] **7.1** Baca ulang skrip `backup_cron.sh` di Bab 12.2 secara khusus:
  - [ ] **7.1.a** Verifikasi `mysqldump` menggunakan `--defaults-extra-file=/root/.my.cnf` (bukan argumen `-u root -p` dengan kata sandi inline).
  - [ ] **7.1.b** Verifikasi variabel `$ZIP_PASSWORD` didefinisikan dengan membaca dari file `.env` di awal skrip (menggunakan `source` atau parsing isi `.env`), bukan menggunakan nilai hardcoded literal.
  - [ ] **7.1.c** Jika ditemukan ketidakamanan, perbaiki skrip tersebut dengan mekanisme yang aman.

- [ ] **7.2** Verifikasi konsistensi versi: pastikan semua penyebutan "v1.1" pada referensi (R-01 s.d R-14) sudah sesuai dengan versi dokumen referensi yang aktual.

- [ ] **7.3** Kumpulkan semua kode error dari R-03 dan cocokkan dengan Bab 17. Untuk setiap kode error yang belum memiliki sub-bab di Bab 17, **buat sub-bab baru** dengan format standar (Gejala, Kemungkinan Penyebab, Langkah Solusi, Pencegahan).

- [ ] **7.4** Baca ulang **Bab 11 (Pemeliharaan Adaptif)** secara utuh:
  - [ ] **7.4.a** Jika prosedur upgrade Python runtime offline belum detail (tanpa langkah compile dari source), perluas dengan langkah yang actionable.
  - [ ] **7.4.b** Jika prosedur upgrade MySQL 8.4 LTS belum ada langkah konkretnya, tambahkan.
  - [ ] **7.4.c** Jika prosedur update `requirements.txt` dengan wheel offline belum ada, tambahkan.
  - [ ] **7.4.d** Jika prosedur penambahan node klien kasir baru belum ada, tambahkan (termasuk: instalasi Python, konfigurasi `.env`, bind IP DHCP statis di MikroTik).

- [ ] **7.5** Periksa seluruh referensi silang antar bab (contoh: "lihat Bab 12", "Bab 16", dsb.). Verifikasi setiap referensi menunjuk ke bab yang tepat dan ada.

- [ ] **7.6** Verifikasi konsistensi teknis:
  - IP Server: selalu `192.168.1.200`.
  - Port MySQL: selalu `3306`.
  - Gateway: selalu `192.168.1.1`.
  - Subnet: selalu `192.168.1.0/24`.
  - Pool size: selalu `5`.
  - Retry count: selalu `3 kali`.
  - Backoff: selalu `exponential (2^n detik)`.

- [ ] **7.7** Verifikasi konsistensi nama tabel database di semua perintah SQL di dokumen ini terhadap daftar 28 tabel di Bab 2.4. Tidak boleh ada nama tabel yang tidak terdaftar.

- [ ] **7.8** Verifikasi nama variabel `.env` di seluruh dokumen konsisten dengan yang ada di R-04. Tidak boleh ada variabel yang dikarang sendiri.

- [ ] **7.9** Periksa Bab 1.6 (Definisi/Akronim) dan Bab 21 (Glosarium). Pastikan tidak ada istilah yang ada di 1.6 namun tidak ada di 21, atau sebaliknya. Keduanya harus saling melengkapi.

- [ ] **7.10** Periksa SLA table di Bab 10.8 dan waktu respon di Bab 13.2. Pastikan nilainya konsisten (tidak ada perbedaan SLA yang tidak disengaja antara kedua bab tersebut).

---

### Tahap 8 — Kompilasi Semua Temuan dan Perbaikan

- [ ] **8.1** Kompilasi seluruh temuan dari Tahap 1–7 ke dalam satu daftar perubahan terstruktur di memori/konteksmu. Kelompokkan berdasarkan: Penambahan, Koreksi, Penghapusan.

- [ ] **8.2** Susun seluruh isi dokumen baru yang telah diperbaiki dalam memori/konteksmu secara utuh dari baris pertama hingga terakhir. **Jangan mulai menulis ke file sebelum seluruh konten sudah tersusun lengkap dalam memori**.

- [ ] **8.3** Pastikan hal-hal berikut sudah tercermin dalam dokumen baru:
  - [ ] **8.3.a** Versi dokumen sudah diubah dari `1.1` menjadi `1.2` di header YAML (baris `versi`).
  - [ ] **8.3.b** Tanggal dokumen sudah diperbarui menjadi tanggal eksekusi issue ini.
  - [ ] **8.3.c** Status dokumen sudah diubah menjadi `Revised`.
  - [ ] **8.3.d** Riwayat Perubahan Dokumen sudah ditambahkan entri baru untuk v1.2, berisi ringkasan seluruh perubahan yang dilakukan beserta nama penyusun.
  - [ ] **8.3.e** Jika ada referensi file baru yang digunakan dalam perbaikan (yang belum terdaftar di Bab 22), tambahkan ke tabel referensi di Bab 22 dengan kode referensi baru (misalnya R-15, R-16, dst.).

---

### Tahap 9 — Penulisan Ulang ke File Target (Overwrite)

> **⚠️ PERHATIAN KRITIS**: Langkah ini adalah operasi penimpaan (overwrite) total. Pastikan seluruh konten dokumen sudah sempurna di memori sebelum melanjutkan.

- [ ] **9.1** Buka file target untuk ditulis ulang:
  ```
  docs/sdlc/07_maintenance/01_maintenance_guide.md
  ```

- [ ] **9.2** Tulis ulang **seluruh** isi dokumen dari **baris pertama hingga baris terakhir** secara lengkap.
  - **WAJIB**: Tidak ada satu pun bagian yang dipotong, diringkas, atau dihilangkan (*no truncation*).
  - **WAJIB**: Seluruh bab yang sudah ada (Bab 1 s.d Bab 22) harus ditulis ulang sepenuhnya dengan perbaikan yang telah dilakukan.
  - **WAJIB**: Bab atau sub-bab baru yang ditambahkan harus ditulis lengkap, bukan hanya judul tanpa konten.
  - **DILARANG**: Menulis hanya bagian yang berubah saja. Dokumen harus ditulis ulang 100% penuh dari awal hingga akhir.

- [ ] **9.3** Setelah penulisan selesai, verifikasi file:
  - [ ] **9.3.a** Baca kembali 10 baris pertama file. Pastikan header YAML memuat `versi: 1.2`.
  - [ ] **9.3.b** Baca kembali 10 baris terakhir file. Pastikan Bab 22 (Referensi) sudah tertulis lengkap dan tidak terpotong.
  - [ ] **9.3.c** Hitung jumlah baris file hasil. Jumlah baris hasil harus **sama dengan atau lebih banyak** dari jumlah baris sebelumnya (karena ada penambahan konten). Jika jumlah baris berkurang signifikan (lebih dari 5%), ulangi penulisan — ada konten yang terpotong.

- [ ] **9.4** Verifikasi akhir: Pastikan entri v1.2 pada tabel Riwayat Perubahan Dokumen memuat ringkasan yang jelas tentang apa yang diubah dalam proses validasi ini.

---

## 7. Kriteria Keberhasilan (Definition of Done)

Issue ini dinyatakan **selesai** apabila seluruh kondisi berikut terpenuhi:

- [ ] Seluruh 14 file referensi sudah dibaca dan dikomparasi secara menyeluruh dengan dokumen utama.
- [ ] Tidak ada data dari referensi yang relevan dan seharusnya ada di dokumen ini yang terlewat.
- [ ] Tidak ada konten yang tidak relevan dengan lingkup Maintenance Guide yang tersisa di dokumen.
- [ ] Struktur dokumen memenuhi standar ITIL v4 dan IEEE 14764 dengan 22 bab lengkap.
- [ ] Bab 11 (Pemeliharaan Adaptif) memuat prosedur yang cukup detail dan actionable untuk 4 skenario upgrade/perluasan.
- [ ] Bab 17 (Troubleshooting) mencakup seluruh kode error yang didefinisikan di R-03 (Security Design).
- [ ] Skrip `backup_cron.sh` di Bab 12.2 sudah menggunakan mekanisme aman (`--defaults-extra-file` dan variabel `$ZIP_PASSWORD` dari `.env`).
- [ ] Bab 13.7 sudah dilengkapi dengan sub-bab prosedur pengisian kontak darurat.
- [ ] Tidak ada placeholder `[DATA: DIISI OLEH...]`, `[TBD]`, atau `[TODO]` yang tersisa tanpa penanganan.
- [ ] Seluruh blok kode memiliki komentar penanda OS di baris pertama.
- [ ] Bahasa Indonesia konsisten, tidak ambigu, dan tidak mengandung kata hubung asing yang tidak perlu.
- [ ] Versi dokumen sudah diubah menjadi `v1.2` dengan entri Riwayat Perubahan yang lengkap.
- [ ] File target sudah ditulis ulang sepenuhnya (overwrite) tanpa truncation dari baris pertama hingga terakhir.
- [ ] Jumlah baris file hasil sama dengan atau lebih banyak dari sebelum validasi.
- [ ] Jika ada referensi baru yang digunakan, sudah ditambahkan di Bab 22 (Referensi Dokumen).

---

## 8. Catatan Tambahan untuk Eksekutor

1. **Jangan berasumsi**: Jika ada informasi yang tidak bisa diverifikasi dari file referensi yang ada (R-01 s.d R-14), jangan karang sendiri. Gunakan kalimat deskriptif yang generik namun tetap relevan, atau tandai sebagai "sesuai spesifikasi operasional toko percetakan AbuCom".

2. **Prioritaskan akurasi di atas kecepatan**: Lebih baik lambat dan benar daripada cepat namun ada data yang salah atau kode error yang terlewat.

3. **Jaga konteks dual-OS**: Selalu ingat bahwa sistem AbuCom berjalan di dua OS secara bersamaan — **Debian 12 (server)** dan **Windows 11 (klien kasir)**. Setiap prosedur harus jelas menyebutkan di OS mana perintah tersebut dijalankan.

4. **Jaga konteks offline-only LAN**: Sistem AbuCom beroperasi tanpa koneksi internet sama sekali. Jangan ada instruksi yang bergantung pada internet (misalnya `pip install`, `apt update` dari internet). Semua instalasi harus dari media offline (USB, wheel cache lokal).

5. **Jaga konsistensi terminologi persona staf**: Selalu gunakan nama dan peran yang konsisten: "Pemilik Usaha (Alfatih)", "Kepala Percetakan (Donsise)", "Kasir", "System Administrator", dan "Tim Pengembang AI (Support)".

6. **Tidak menambahkan opini pribadi**: Dokumen ini adalah panduan teknis operasional. Jangan tambahkan komentar evaluatif atau opini yang tidak bersumber dari referensi.

7. **Format markdown yang ketat**: Pastikan seluruh heading, tabel, blok kode, dan checklist menggunakan format Markdown yang valid dan konsisten. Tidak boleh ada heading level yang loncat (misalnya dari `##` langsung ke `####`).

---

*Issue ini dibuat pada: 2026-05-30 | Dibuat oleh: Senior IT Service Manager & Maintenance Operations Architect*
