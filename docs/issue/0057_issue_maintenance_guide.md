# Pembuatan dan Penyusunan Dokumen Maintenance Guide

---

## Metadata Issue

| Atribut             | Nilai                                                                |
|---------------------|----------------------------------------------------------------------|
| **Judul**           | Pembuatan dan Penyusunan Dokumen Maintenance Guide AbuCom            |
| **Tipe**            | Dokumentasi — Fase 07 Maintenance                                    |
| **Prioritas**       | High                                                                 |
| **Dokumen Utama**   | Maintenance Guide                                                    |
| **Target File**     | `docs/sdlc/07_maintenance/01_maintenance_guide.md`                   |
| **Status**          | Open                                                                 |
| **Dibuat Oleh**     | Claude Opus 4.6 (Thinking) — System Strategist & Security Lead       |
| **Tanggal Dibuat**  | 2026-05-27                                                           |
| **Ditugaskan Ke**   | Junior Programmer / LLM Model AI (Gemini 3.1 Pro Low / GPT-OSS 120B)|

---

## 1. Deskripsi Issue

Issue ini berisi perencanaan low-level untuk pembuatan dan penyusunan dokumen **Maintenance Guide** pada Fase 07 — Maintenance dari siklus SDLC proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**. Dokumen Maintenance Guide adalah panduan teknis operasional resmi yang mendokumentasikan seluruh prosedur pemeliharaan rutin, pemeliharaan korektif, pemeliharaan preventif, pemeliharaan adaptif, dan pemeliharaan perfektif dari sistem aplikasi AbuCom CLI pasca Go-Live.

Dokumen ini merupakan deliverable pertama pada Fase 07 — Maintenance yang menerima estafet langsung dari seluruh output Fase 06 — Deployment (Deployment Guide, Environment Config, Release Notes). Dokumen ini harus dapat berdiri sendiri sebagai referensi, acuan, dan input utama bagi aktivitas operasional pemeliharaan harian, mingguan, bulanan, dan tahunan oleh Pemilik Usaha, Kepala Percetakan, System Administrator, dan Tim Pengembang AI.

---

## 2. Persona Pelaksana Penyusunan

**Persona yang WAJIB digunakan saat menyusun dokumen ini:**

> **Senior IT Service Manager & Maintenance Operations Architect**

**Justifikasi pemilihan persona:**
- Persona ini memiliki otoritas dan keahlian tertinggi dalam merancang strategi pemeliharaan sistem informasi pasca-produksi yang mencakup aspek teknis (hardware, software, database, jaringan) maupun aspek operasional (SOP harian, jadwal pemeliharaan, eskalasi masalah, disaster recovery).
- Persona ini berwenang menentukan kategori pemeliharaan (korektif, preventif, adaptif, perfektif), menetapkan SLA respon, mengatur jadwal rotasi backup, merancang prosedur penanganan insiden, dan memastikan keberlangsungan operasional bisnis toko percetakan AbuCom secara berkelanjutan.
- Persona ini memahami standar ITIL (Information Technology Infrastructure Library) dan ISO/IEC 20000 untuk manajemen layanan IT yang relevan dengan konteks UMKM.

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **WAJIB** dibaca secara utuh dan dirangkum datanya sebelum menyusun dokumen Maintenance Guide. File-file ini dipilih berdasarkan relevansi langsung terhadap kebutuhan informasi dokumen pemeliharaan.

### 3.1. Referensi Primer (WAJIB Dibaca Secara Menyeluruh)

| No | Kode Ref | Nama Dokumen                 | Path Relatif                                              | Alasan Relevansi                                                                                         |
|:--:|:--------:|------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1  | **R-01** | Deployment Guide v1.1        | `docs/sdlc/06_deployment/01_deployment_guide.md`          | Sumber utama SOP runbook harian (startup/shutdown), prosedur backup cron, disaster recovery, troubleshooting, konfigurasi hardware/jaringan, dan eskalasi masalah yang akan diadopsi dan diperluas di Maintenance Guide. |
| 2  | **R-02** | System Architecture v1.1     | `docs/sdlc/03_design/03_system_architecture.md`           | Sumber informasi arsitektur fisik (topologi LAN, spesifikasi hardware server/klien, UPS), arsitektur software berlapis (4-layer), arsitektur modular (10 modul), arsitektur data (28 tabel, connection pooling, retry), dan arsitektur keamanan yang wajib dipelihara. |
| 3  | **R-03** | Security Design v1.1         | `docs/sdlc/03_design/06_security_design.md`               | Sumber kebijakan keamanan (bcrypt, JWT, RBAC, audit trail, UU PDP), SOP respon insiden keamanan, retensi log audit 12 bulan, rotasi kunci JWT/Fernet 6 bulan, dan prosedur pengelolaan akun pengguna pasca-produksi. |
| 4  | **R-04** | Environment Config v1.1      | `docs/sdlc/06_deployment/02_environment_config.yaml`      | Sumber parameter konfigurasi runtime produksi (database, keamanan, printer, backup) yang wajib dipelihara dan diaudit berkala. |
| 5  | **R-05** | Release Notes v1.1           | `docs/sdlc/06_deployment/03_release_notes.md`             | Sumber informasi fitur aktif v1.0.0 (10 modul, 40+ SRS), batasan diketahui (known limitations), masalah diketahui (known issues), roadmap fitur mendatang, dan parameter konfigurasi dinamis runtime. |

### 3.2. Referensi Sekunder (Dibaca Bagian yang Relevan)

| No | Kode Ref | Nama Dokumen                 | Path Relatif                                              | Alasan Relevansi                                                                                         |
|:--:|:--------:|------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 6  | **R-06** | Environment Setup v1.1       | `docs/sdlc/04_implementation/02_environment_setup.md`     | Sumber prosedur teknis setup environment (kompilasi Python, MySQL, venv, .env, dependensi) yang diperlukan saat pemeliharaan adaptif (upgrade runtime/library) atau disaster recovery. |
| 7  | **R-07** | Bug Report Template v1.1     | `docs/sdlc/05_testing/04_bug_report_template.md`          | Sumber format standar pelaporan bug pasca-produksi, klasifikasi severity/priority, SLA perbaikan, dan siklus hidup bug yang harus diikuti saat corrective maintenance. |
| 8  | **R-08** | Test Plan v1.1               | `docs/sdlc/05_testing/01_test_plan.md`                    | Sumber prosedur regression testing yang wajib dijalankan setelah setiap perbaikan bug atau update kode di lingkungan produksi. |
| 9  | **R-09** | Coding Standard v1.1         | `docs/sdlc/04_implementation/01_coding_standard.md`       | Sumber standar penulisan kode FP Python yang wajib dipatuhi saat melakukan maintenance coding (patch, hotfix, refactoring). |
| 10 | **R-10** | Git Workflow v1.1             | `docs/sdlc/04_implementation/04_git_workflow.md`          | Sumber alur kerja Git (branching, commit, tagging, merge) yang wajib diikuti saat merilis patch pemeliharaan. |
| 11 | **R-11** | Tech Stack Decision v1.1     | `docs/sdlc/01_planning/04_tech_stack_decision.md`         | Sumber batasan mutlak tech stack (Python 3.14.2+, MySQL 8.4 LTS, pustaka wajib) yang tidak boleh dilanggar saat pemeliharaan adaptif. |

### 3.3. Referensi Tersier (Dibaca untuk Konteks Bisnis)

| No | Kode Ref | Nama Dokumen                 | Path Relatif                                              | Alasan Relevansi                                                                                         |
|:--:|:--------:|------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 12 | **R-12** | SRS v1.1                     | `docs/sdlc/02_analysis/02_software_requirements.md`       | Sumber spesifikasi fungsional (SRS-F) dan non-fungsional (SRS-NF) yang menjadi acuan validasi saat pemeliharaan. |
| 13 | **R-13** | Database Schema v1.1         | `docs/sdlc/03_design/01_database_schema.sql`              | Sumber skema fisik 28 tabel InnoDB yang menjadi acuan saat maintenance schema migration dan data integrity check. |
| 14 | **R-14** | Module Structure v1.1        | `docs/sdlc/04_implementation/03_module_structure.md`      | Sumber peta modul kode program yang perlu dipahami saat melakukan patch atau update modul spesifik. |

> **CATATAN**: File `narasi.txt` **TIDAK diperlukan** lagi sebagai referensi karena seluruh informasi konteks bisnis yang relevan sudah terangkum lengkap di dalam dokumen-dokumen SDLC fase sebelumnya (R-01 s.d R-14).

---

## 4. Kerangka Struktur Dokumen Utama

Berikut adalah kerangka bab dan sub-bab dokumen Maintenance Guide yang **WAJIB** diikuti secara tepat. Kerangka ini mengadopsi standar praktik industri **ITIL Service Operation** dan **IEEE 14764** (Software Maintenance) yang disesuaikan dengan konteks UMKM toko percetakan luring.

```
---
dokumen    : Maintenance Guide
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : 2026-05-27
status     : Draft
penyusun   : Senior IT Service Manager & Maintenance Operations Architect
---

# Maintenance Guide — AbuCom

## Riwayat Perubahan Dokumen
(Tabel versi, tanggal, perubahan, oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya (Input & Output)
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan

---

## 2. Ringkasan Arsitektur Sistem yang Dipelihara
### 2.1. Diagram Arsitektur Deployment Produksi (Mermaid)
### 2.2. Matriks Komponen per Node (Server, Klien, Jaringan)
### 2.3. Daftar Modul Fungsional Aktif (M.1 s.d M.10)
### 2.4. Daftar Tabel Database (28 Tabel InnoDB)
### 2.5. Daftar Pustaka Dependensi dan Versi Terkunci

---

## 3. Kategori Pemeliharaan Sistem
### 3.1. Pemeliharaan Korektif (Corrective Maintenance)
  - Definisi dan cakupan
  - Contoh kasus spesifik AbuCom
### 3.2. Pemeliharaan Preventif (Preventive Maintenance)
  - Definisi dan cakupan
  - Contoh kasus spesifik AbuCom
### 3.3. Pemeliharaan Adaptif (Adaptive Maintenance)
  - Definisi dan cakupan
  - Contoh kasus spesifik AbuCom
### 3.4. Pemeliharaan Perfektif (Perfective Maintenance)
  - Definisi dan cakupan
  - Contoh kasus spesifik AbuCom
### 3.5. Pemeliharaan Darurat (Emergency Maintenance)
  - Definisi dan cakupan
  - Contoh kasus spesifik AbuCom

---

## 4. SOP Pemeliharaan Rutin Harian
### 4.1. SOP Startup Harian Sistem (Buka Toko)
### 4.2. SOP Shutdown Harian Sistem (Tutup Toko)
### 4.3. SOP Serah Terima Shift Kasir
### 4.4. SOP Verifikasi Backup Harian Otomatis (Cron Job 21:00 WIB)
### 4.5. SOP Pemantauan Dashboard Anomali Pemilik
### 4.6. Checklist Pemeliharaan Harian (Format Centang)

---

## 5. SOP Pemeliharaan Rutin Mingguan
### 5.1. Pemeriksaan Fisik Hardware (Server, Kasir, UPS, Printer)
### 5.2. Verifikasi Konektivitas Jaringan LAN (Ping, Port Test)
### 5.3. Pemeriksaan Status Firewall Server (ufw status)
### 5.4. Pembersihan Filter Udara Mini PC Server
### 5.5. Verifikasi Ketersediaan Kertas Struk Printer Thermal
### 5.6. Checklist Pemeliharaan Mingguan (Format Centang)

---

## 6. SOP Pemeliharaan Rutin Bulanan
### 6.1. Rotasi Log File Lokal (Klien Kasir)
### 6.2. Audit Integritas Tabel Database (CHECK TABLE)
### 6.3. Verifikasi Kapasitas Penyimpanan Server (Disk Usage)
### 6.4. Pemindahan Backup Bulanan ke Cold Storage Fisik
### 6.5. Pemeriksaan Status UPS dan Kapasitas Baterai
### 6.6. Audit Log Audit Trail (Deteksi Anomali Fraud)
### 6.7. Verifikasi Enkripsi WhatsApp CRM Pelanggan (UU PDP)
### 6.8. Checklist Pemeliharaan Bulanan (Format Centang)

---

## 7. SOP Pemeliharaan Rutin Kuartalan (3 Bulanan)
### 7.1. Simulasi Disaster Recovery Restore Database
### 7.2. Pengujian Validitas Berkas Backup Terenkripsi
### 7.3. Review dan Purging Log Audit > 12 Bulan
### 7.4. Verifikasi Kinerja Jaringan dan Latensi LAN
### 7.5. Update Dokumentasi Aset dan Inventaris Hardware
### 7.6. Checklist Pemeliharaan Kuartalan (Format Centang)

---

## 8. SOP Pemeliharaan Rutin Semesteran (6 Bulanan)
### 8.1. Rotasi Kunci Keamanan JWT Secret Key
### 8.2. Rotasi Kunci Enkripsi Fernet CRM (UU PDP Compliance)
### 8.3. Rotasi Kata Sandi Database User Aplikasi
### 8.4. Review Kebijakan Hak Akses RBAC (8 Peran)
### 8.5. Evaluasi Performa Sistem dan Kapasitas Planning
### 8.6. Checklist Pemeliharaan Semesteran (Format Centang)

---

## 9. SOP Pemeliharaan Rutin Tahunan
### 9.1. Audit Keamanan Menyeluruh (Security Audit)
### 9.2. Review Kepatuhan UU PDP No. 27/2022
### 9.3. Evaluasi End-of-Life Perangkat Keras
### 9.4. Review Relevansi Parameter system_configs
### 9.5. Perencanaan Upgrade Versi dan Roadmap
### 9.6. Checklist Pemeliharaan Tahunan (Format Centang)

---

## 10. Prosedur Pemeliharaan Korektif (Bug Fix & Patching)
### 10.1. Alur Pelaporan Bug Pasca-Produksi
### 10.2. Klasifikasi Severity dan Priority (Referensi Bug Report Template)
### 10.3. Prosedur Analisis Akar Masalah (Root Cause Analysis)
### 10.4. Prosedur Pengembangan dan Pengujian Patch
### 10.5. Prosedur Deployment Patch ke Produksi
### 10.6. Prosedur Rollback Patch (Jika Gagal)
### 10.7. Diagram Alur Patching (Mermaid Flowchart)
### 10.8. SLA Penanganan Bug per Severity Level

---

## 11. Prosedur Pemeliharaan Adaptif (Upgrade & Migrasi)
### 11.1. Prosedur Upgrade Versi Python Runtime
### 11.2. Prosedur Upgrade Versi Pustaka Dependensi
### 11.3. Prosedur Migrasi Skema Database (Schema Migration)
### 11.4. Prosedur Upgrade Sistem Operasi Server/Klien
### 11.5. Prosedur Penambahan Node Klien Baru (Ekspansi)
### 11.6. Checklist Pre-Upgrade dan Post-Upgrade

---

## 12. Prosedur Backup, Restore, dan Disaster Recovery
### 12.1. Strategi Backup (Harian, Bulanan, Tahunan)
### 12.2. Prosedur Backup Otomatis Harian (Cron Job)
### 12.3. Prosedur Backup Manual On-Demand
### 12.4. Prosedur Restore Database dari Backup
### 12.5. Prosedur Disaster Recovery (Kegagalan Total Server)
### 12.6. Strategi Retensi dan Rotasi Backup
### 12.7. Diagram Alur Backup dan Restore (Mermaid Flowchart)

---

## 13. Prosedur Penanganan Insiden dan Eskalasi
### 13.1. Definisi dan Klasifikasi Insiden
### 13.2. Matriks Eskalasi Insiden (Level 1, 2, 3)
### 13.3. Prosedur Deteksi Insiden
### 13.4. Prosedur Respon Insiden (Isolasi, Pelaporan, Pemulihan)
### 13.5. Prosedur Penanganan Insiden Keamanan Khusus
### 13.6. SOP Graceful Shutdown saat Mati Listrik (UPS)
### 13.7. Kontak Darurat dan Jalur Eskalasi
### 13.8. Diagram Alur Eskalasi Insiden (Mermaid Flowchart)

---

## 14. Pemeliharaan Keamanan Sistem
### 14.1. Jadwal Rotasi Kunci dan Kredensial
### 14.2. Prosedur Pengelolaan Akun Pengguna (Tambah/Nonaktif/Reset)
### 14.3. Prosedur Pemantauan Log Audit Trail
### 14.4. Prosedur Penanganan Insiden Fraud (Selisih Kas, Retur Abnormal)
### 14.5. Prosedur Verifikasi Hardening OS dan Firewall
### 14.6. Prosedur Kepatuhan Berkala UU PDP No. 27/2022

---

## 15. Pemeliharaan Database
### 15.1. Prosedur Pemeriksaan Integritas Tabel (CHECK TABLE / REPAIR)
### 15.2. Prosedur Optimasi Performa Query (ANALYZE TABLE / OPTIMIZE)
### 15.3. Prosedur Pemantauan Kapasitas Disk Database
### 15.4. Prosedur Purging Data Log Audit Lama (> 12 Bulan)
### 15.5. Prosedur Verifikasi Connection Pool dan Retry Mechanism
### 15.6. Prosedur Migrasi Data Antar Cabang (Multi-Branch Ready)

---

## 16. Pemeliharaan Hardware dan Infrastruktur
### 16.1. Jadwal Pemeriksaan Hardware Berkala
### 16.2. Prosedur Penggantian Komponen Server (SSD, RAM, UPS)
### 16.3. Prosedur Penggantian Kabel LAN dan Switch Hub
### 16.4. Prosedur Penggantian Printer Thermal
### 16.5. Prosedur Penggantian Baterai UPS
### 16.6. Daftar Inventaris Hardware dan Umur Pakai

---

## 17. Troubleshooting Guide
### 17.1. Masalah Koneksi Database (ERR-DB-001 / ERR-DB-002)
### 17.2. Masalah Otentikasi Login (ERR-AUTH-001 / ERR-AUTH-002)
### 17.3. Masalah Sesi Expired (ERR-SESSION-001 / ERR-SESSION-002)
### 17.4. Masalah Backup Gagal (ERR-FILE-001 / ERR-FILE-039)
### 17.5. Masalah Selisih Kas Kasir (ERR-CASH-001 / ERR-CASH-004)
### 17.6. Masalah Rendering CLI (ANSI Glitch / Mojibake)
### 17.7. Masalah Printer Thermal (Struk Acak / Laci Tidak Membuka)
### 17.8. Masalah Performa Query Lambat (> 2 Detik)
### 17.9. Masalah Stok Desimal Tidak Sinkron

---

## 18. Matriks Risiko Pemeliharaan
### 18.1. Identifikasi Risiko Operasional Pasca-Produksi
### 18.2. Tabel Matriks Risiko (Probabilitas, Dampak, Skor, Mitigasi)
### 18.3. Rencana Kontingensi per Risiko

---

## 19. Peran dan Tanggung Jawab Pemeliharaan
### 19.1. Matriks RACI Pemeliharaan
### 19.2. Tanggung Jawab Pemilik Usaha
### 19.3. Tanggung Jawab Kepala Percetakan
### 19.4. Tanggung Jawab Kasir dan Staf Operasional
### 19.5. Tanggung Jawab System Administrator
### 19.6. Tanggung Jawab Tim Pengembang AI (Support)

---

## 20. Jadwal Pemeliharaan Konsolidasi (Maintenance Calendar)
### 20.1. Kalender Pemeliharaan Tahunan (Tabel Visual)
### 20.2. Ringkasan Frekuensi Aktivitas Pemeliharaan

---

## 21. Glosarium

---

## 22. Referensi Dokumen
(Tabel daftar semua file referensi yang digunakan dalam penyusunan)
```

---

## 5. Instruksi Detail Tahapan Implementasi

### Tahap 1: Persiapan dan Pembacaan File Referensi

> **Tujuan**: Membaca dan merangkum semua data serta informasi dari file referensi. Setiap detail jangan sampai ada yang terlewat.

- [ ] **1.1.** Baca file referensi **R-01** (`docs/sdlc/06_deployment/01_deployment_guide.md`) secara utuh dari awal sampai akhir.
  - [ ] 1.1.1. Rangkum seluruh isi Bab 10 (Prosedur Backup dan Disaster Recovery Produksi) — ini menjadi input utama untuk Bab 12 dokumen utama.
  - [ ] 1.1.2. Rangkum seluruh isi Bab 11 (Runbook Operasional Harian) — ini menjadi input utama untuk Bab 4, 5, 6, 13 dokumen utama.
  - [ ] 1.1.3. Rangkum seluruh isi Bab 12 (Keamanan Deployment) — ini menjadi input utama untuk Bab 14 dokumen utama.
  - [ ] 1.1.4. Rangkum seluruh isi Bab 13 (Matriks Risiko Deployment) — ini menjadi input utama untuk Bab 18 dokumen utama.
  - [ ] 1.1.5. Rangkum seluruh isi Bab 8 (Prosedur Rollback Deployment) — ini menjadi input untuk Bab 10 dokumen utama.
  - [ ] 1.1.6. Rangkum seluruh isi Bab 2 (Ringkasan Arsitektur Deployment) — ini menjadi input untuk Bab 2 dokumen utama.
  - [ ] 1.1.7. Rangkum semua spesifikasi hardware server, klien, jaringan dari Bab 3-6 — ini menjadi input untuk Bab 16 dokumen utama.
  - [ ] 1.1.8. Catat semua kode error yang disebutkan (ERR-DB-001, ERR-AUTH-xxx, dll.) — ini menjadi input untuk Bab 17 dokumen utama.

- [ ] **1.2.** Baca file referensi **R-02** (`docs/sdlc/03_design/03_system_architecture.md`) secara utuh dari awal sampai akhir.
  - [ ] 1.2.1. Rangkum arsitektur fisik (topologi LAN, spesifikasi hardware, konfigurasi OS dual-OS) dari Bab 3.
  - [ ] 1.2.2. Rangkum arsitektur software berlapis (4-layer FP) dari Bab 4.
  - [ ] 1.2.3. Rangkum arsitektur modular (10 modul M.1-M.10) dan peta modul ke tabel dari Bab 5.
  - [ ] 1.2.4. Rangkum arsitektur data (connection pooling, retry mechanism, ACID, decimal strategy) dari Bab 6.
  - [ ] 1.2.5. Rangkum arsitektur keamanan (6 lapis defense in depth) dari Bab 7.
  - [ ] 1.2.6. Rangkum prosedur backup dan pencadangan dari Bab 9.

- [ ] **1.3.** Baca file referensi **R-03** (`docs/sdlc/03_design/06_security_design.md`) secara utuh dari awal sampai akhir.
  - [ ] 1.3.1. Rangkum seluruh model ancaman (threat model 8 ancaman THR-001 s.d THR-008) dari Bab 2.2.
  - [ ] 1.3.2. Rangkum klasifikasi sensitivitas data (3 tingkat: Sangat Sensitif, Sensitif, Operasional) dari Bab 2.3.
  - [ ] 1.3.3. Rangkum desain otentikasi (bcrypt cost 12, JWT HS256 8 jam, rate limiting 5x/10 menit) dari Bab 4.
  - [ ] 1.3.4. Rangkum desain otorisasi RBAC (8 peran, 4 eskalasi pemilik, otorisasi kepala) dari Bab 5.
  - [ ] 1.3.5. Rangkum desain proteksi data (AES-256 backup, Fernet CRM, UU PDP) dari Bab 6.
  - [ ] 1.3.6. Rangkum desain audit trail (skema tabel, event pemicu, format JSON, retensi 12 bulan) dari Bab 7.
  - [ ] 1.3.7. Rangkum prosedur serah terima shift, backup/restore aman, dan pengelolaan akun dari Bab 8.
  - [ ] 1.3.8. Rangkum prosedur respon insiden keamanan (5 jenis insiden, fase deteksi, isolasi, pemulihan) dari Bab 10.6.
  - [ ] 1.3.9. Rangkum seluruh kode error keamanan (ERR-AUTH, ERR-SESSION, ERR-DB, ERR-FILE, ERR-CASH) dari Bab 10.
  - [ ] 1.3.10. Rangkum seluruh jadwal rotasi kunci (JWT 6 bulan, Fernet 6 bulan, password DB) dari Bab 8 dan Bab 6.

- [ ] **1.4.** Baca file referensi **R-04** (`docs/sdlc/06_deployment/02_environment_config.yaml`) secara utuh.
  - [ ] 1.4.1. Rangkum semua parameter konfigurasi runtime produksi (database, keamanan, printer, backup).
  - [ ] 1.4.2. Rangkum semua parameter `system_configs` yang tersimpan di database MySQL.

- [ ] **1.5.** Baca file referensi **R-05** (`docs/sdlc/06_deployment/03_release_notes.md`) secara utuh.
  - [ ] 1.5.1. Rangkum daftar 10 modul fungsional aktif dan fitur SRS terkait dari Bab 4.
  - [ ] 1.5.2. Rangkum fitur keamanan rilis dari Bab 5.
  - [ ] 1.5.3. Rangkum batasan yang diketahui (known limitations) dari Bab 7.
  - [ ] 1.5.4. Rangkum masalah yang diketahui (known issues — DEF-COMPAT-001, DEF-PERF-001) dari Bab 8.
  - [ ] 1.5.5. Rangkum parameter konfigurasi default rilis dari Bab 10.
  - [ ] 1.5.6. Rangkum roadmap fitur rilis mendatang dari Bab 15.
  - [ ] 1.5.7. Rangkum matriks risiko rilis dari Bab 13.

- [ ] **1.6.** Baca file referensi **R-06** (`docs/sdlc/04_implementation/02_environment_setup.md`) — bagian yang relevan.
  - [ ] 1.6.1. Rangkum prosedur instalasi Python 3.14.2+ (compile from source di Debian, installer di Windows).
  - [ ] 1.6.2. Rangkum prosedur instalasi dan konfigurasi MySQL Server (mysql_secure_installation, bind address, character set, transaction isolation).
  - [ ] 1.6.3. Rangkum prosedur pembuatan virtual environment dan instalasi dependensi (offline wheels).
  - [ ] 1.6.4. Rangkum daftar dependensi dan versi terkunci.

- [ ] **1.7.** Baca file referensi **R-07** (`docs/sdlc/05_testing/04_bug_report_template.md`) — bagian yang relevan.
  - [ ] 1.7.1. Rangkum format template formulir laporan bug (Bab 6.1).
  - [ ] 1.7.2. Rangkum klasifikasi severity 5 level (S1-S5) dari Bab 2.
  - [ ] 1.7.3. Rangkum klasifikasi priority 4 level (P1-P4) dari Bab 3.
  - [ ] 1.7.4. Rangkum SLA penanganan bug per severity level dari Bab 7.3.
  - [ ] 1.7.5. Rangkum diagram siklus hidup bug (bug lifecycle) dari Bab 4.

- [ ] **1.8.** Baca file referensi **R-08** (`docs/sdlc/05_testing/01_test_plan.md`) — bagian yang relevan.
  - [ ] 1.8.1. Rangkum prosedur regression testing yang relevan untuk maintenance.
  - [ ] 1.8.2. Rangkum exit criteria testing yang harus dipenuhi setelah patching.

- [ ] **1.9.** Baca file referensi **R-09** (`docs/sdlc/04_implementation/01_coding_standard.md`) — bagian yang relevan.
  - [ ] 1.9.1. Rangkum standar penulisan kode FP Python yang wajib dipatuhi saat maintenance coding.
  - [ ] 1.9.2. Rangkum konvensi penamaan file, fungsi, dan variabel.

- [ ] **1.10.** Baca file referensi **R-10** (`docs/sdlc/04_implementation/04_git_workflow.md`) — bagian yang relevan.
  - [ ] 1.10.1. Rangkum alur branching Git untuk hotfix dan patch maintenance.
  - [ ] 1.10.2. Rangkum konvensi penamaan commit message dan tagging rilis.

- [ ] **1.11.** Baca file referensi **R-11** (`docs/sdlc/01_planning/04_tech_stack_decision.md`) — bagian yang relevan.
  - [ ] 1.11.1. Rangkum batasan mutlak platform (Python 3.14.2+, MySQL 8.4 LTS, FP murni).
  - [ ] 1.11.2. Rangkum daftar pustaka wajib dan versi terkunci.

- [ ] **1.12.** Baca file referensi **R-12** (`docs/sdlc/02_analysis/02_software_requirements.md`) — bagian yang relevan.
  - [ ] 1.12.1. Rangkum spesifikasi non-fungsional performa (response time < 2 detik, coverage >= 90%).
  - [ ] 1.12.2. Rangkum spesifikasi ketersediaan dan keandalan sistem.

- [ ] **1.13.** Baca file referensi **R-13** (`docs/sdlc/03_design/01_database_schema.sql`) — bagian yang relevan.
  - [ ] 1.13.1. Rangkum daftar 28 tabel InnoDB beserta relasi utamanya.
  - [ ] 1.13.2. Rangkum constraint kritis (UNIQUE, CHECK, FOREIGN KEY).

- [ ] **1.14.** Baca file referensi **R-14** (`docs/sdlc/04_implementation/03_module_structure.md`) — bagian yang relevan.
  - [ ] 1.14.1. Rangkum struktur direktori proyek dan peta file modul.

---

### Tahap 2: Penyusunan Konten Dokumen

> **Tujuan**: Menulis konten dokumen Maintenance Guide menggunakan data yang sudah dirangkum, dengan memastikan setiap bab berisi informasi yang lengkap, substantif, dan spesifik konteks AbuCom.

- [ ] **2.1.** Tulis **front matter YAML** (metadata dokumen) di bagian paling atas file.

- [ ] **2.2.** Tulis **Riwayat Perubahan Dokumen** versi 1.0 (inisialisasi awal).

- [ ] **2.3.** Tulis **Bab 1 — Informasi Dokumen**:
  - [ ] 2.3.1. Tulis tujuan dokumen yang menjelaskan Maintenance Guide sebagai panduan pemeliharaan pasca Go-Live.
  - [ ] 2.3.2. Tulis cakupan dokumen (pemeliharaan korektif, preventif, adaptif, perfektif, darurat).
  - [ ] 2.3.3. Tulis posisi dokumen dalam SDLC (Fase 07 Maintenance, deliverable ke-1) dengan diagram ASCII.
  - [ ] 2.3.4. Tulis hubungan dokumen dengan dokumen SDLC lainnya — sebutkan secara eksplisit semua 14 dokumen referensi (R-01 s.d R-14) sebagai input, dan sebutkan output (SOP harian, log pemeliharaan, laporan insiden).
  - [ ] 2.3.5. Tulis audiens target (Pemilik Usaha, Kepala Percetakan, System Administrator, Tim AI).
  - [ ] 2.3.6. Tulis definisi, akronim, dan singkatan (ITIL, SLA, MTTR, MTBF, FP, CLI, JWT, RBAC, ACID, LAN, UPS, BOM, HPP, UU PDP, dll.).

- [ ] **2.4.** Tulis **Bab 2 — Ringkasan Arsitektur Sistem yang Dipelihara**:
  - [ ] 2.4.1. Sertakan diagram Mermaid arsitektur deployment produksi (ambil dari R-01 Bab 2.1 atau R-05 Bab 12.1).
  - [ ] 2.4.2. Sertakan tabel matriks komponen per node (Server Debian 12 vs Klien Windows 11).
  - [ ] 2.4.3. Sertakan daftar 10 modul fungsional aktif (M.1-M.10) beserta nama dan tabel terkait (ambil dari R-02 Bab 5).
  - [ ] 2.4.4. Sertakan daftar 28 tabel database InnoDB (5 kelompok) (ambil dari R-02 Bab 6.1).
  - [ ] 2.4.5. Sertakan daftar pustaka dependensi dan versi terkunci (ambil dari R-05 Bab 3.2.3 atau R-06 Bab 7.3).

- [ ] **2.5.** Tulis **Bab 3 — Kategori Pemeliharaan Sistem**:
  - [ ] 2.5.1. Definisikan pemeliharaan korektif dan berikan contoh konkret AbuCom (misal: perbaikan bug DEF-COMPAT-001 mojibake CMD, perbaikan bug kalkulasi HPP).
  - [ ] 2.5.2. Definisikan pemeliharaan preventif dan berikan contoh konkret (misal: pembersihan debu Mini PC, rotasi log bulanan, simulasi DR kuartalan).
  - [ ] 2.5.3. Definisikan pemeliharaan adaptif dan berikan contoh konkret (misal: upgrade Python 3.14.x ke 3.15.x, upgrade MySQL 8.4 ke 8.5, penambahan node klien kasir baru).
  - [ ] 2.5.4. Definisikan pemeliharaan perfektif dan berikan contoh konkret (misal: optimasi query laporan laba rugi > 2 detik, penambahan fitur GUI di masa depan).
  - [ ] 2.5.5. Definisikan pemeliharaan darurat dan berikan contoh konkret (misal: hotfix crash program saat startup, database korupsi, UPS rusak).

- [ ] **2.6.** Tulis **Bab 4 — SOP Pemeliharaan Rutin Harian** (adoptasi dan perluas dari R-01 Bab 11):
  - [ ] 2.6.1. Tulis SOP startup harian dengan langkah-langkah detail (jam, aktor, perintah terminal).
  - [ ] 2.6.2. Tulis SOP shutdown harian dengan langkah-langkah detail (jam, aktor, perintah terminal).
  - [ ] 2.6.3. Tulis SOP serah terima shift kasir dengan detail prosedur rekonsiliasi kas (threshold Rp 10.000, eskalasi).
  - [ ] 2.6.4. Tulis SOP verifikasi backup harian (cara mengecek log `/var/log/abucom_backup.log`).
  - [ ] 2.6.5. Tulis SOP pemantauan dashboard anomali pemilik (deteksi brute force, retur abnormal, selisih kas).
  - [ ] 2.6.6. Buat checklist pemeliharaan harian menggunakan format `- [ ]`.

- [ ] **2.7.** Tulis **Bab 5 — SOP Pemeliharaan Rutin Mingguan**:
  - [ ] 2.7.1. Tulis prosedur pemeriksaan fisik hardware (cek kabel, lampu indikator, suhu).
  - [ ] 2.7.2. Tulis prosedur verifikasi konektivitas jaringan (perintah `ping`, `Test-NetConnection`).
  - [ ] 2.7.3. Tulis prosedur pemeriksaan firewall (perintah `ufw status verbose`).
  - [ ] 2.7.4. Tulis prosedur pembersihan filter udara Mini PC Server.
  - [ ] 2.7.5. Tulis prosedur verifikasi kertas struk printer thermal.
  - [ ] 2.7.6. Buat checklist pemeliharaan mingguan menggunakan format `- [ ]`.

- [ ] **2.8.** Tulis **Bab 6 — SOP Pemeliharaan Rutin Bulanan**:
  - [ ] 2.8.1. Tulis prosedur rotasi log file lokal klien kasir (langkah-langkah detail, perintah terminal).
  - [ ] 2.8.2. Tulis prosedur audit integritas tabel database (perintah `CHECK TABLE`, `REPAIR TABLE`).
  - [ ] 2.8.3. Tulis prosedur verifikasi kapasitas disk server (perintah `df -h`, `du -sh`).
  - [ ] 2.8.4. Tulis prosedur pemindahan backup bulanan ke cold storage fisik (external HDD/flashdisk).
  - [ ] 2.8.5. Tulis prosedur pemeriksaan UPS dan kapasitas baterai.
  - [ ] 2.8.6. Tulis prosedur audit log audit trail (deteksi pola anomali fraud dari tabel `audit_logs`).
  - [ ] 2.8.7. Tulis prosedur verifikasi enkripsi WhatsApp CRM (query tabel `pelanggan` kolom `whatsapp`).
  - [ ] 2.8.8. Buat checklist pemeliharaan bulanan menggunakan format `- [ ]`.

- [ ] **2.9.** Tulis **Bab 7 — SOP Pemeliharaan Rutin Kuartalan** (adoptasi dari R-01 Bab 11.3):
  - [ ] 2.9.1. Tulis prosedur simulasi disaster recovery restore database (langkah-langkah detail).
  - [ ] 2.9.2. Tulis prosedur pengujian validitas berkas backup terenkripsi (uji dekripsi dan restore ke sandbox).
  - [ ] 2.9.3. Tulis prosedur review dan purging log audit > 12 bulan (adoptasi dari R-03 Bab 7.5).
  - [ ] 2.9.4. Tulis prosedur verifikasi kinerja jaringan dan latensi LAN.
  - [ ] 2.9.5. Tulis prosedur update dokumentasi aset dan inventaris hardware.
  - [ ] 2.9.6. Buat checklist pemeliharaan kuartalan menggunakan format `- [ ]`.

- [ ] **2.10.** Tulis **Bab 8 — SOP Pemeliharaan Rutin Semesteran** (adoptasi dari R-03 dan R-01):
  - [ ] 2.10.1. Tulis prosedur rotasi kunci JWT Secret Key (langkah-langkah generasi kunci baru, update `.env`).
  - [ ] 2.10.2. Tulis prosedur rotasi kunci Fernet CRM (langkah-langkah generasi, re-enkripsi data pelanggan).
  - [ ] 2.10.3. Tulis prosedur rotasi kata sandi database user aplikasi `abucom_app`.
  - [ ] 2.10.4. Tulis prosedur review kebijakan hak akses RBAC (verifikasi matriks 8 peran).
  - [ ] 2.10.5. Tulis prosedur evaluasi performa sistem dan capacity planning.
  - [ ] 2.10.6. Buat checklist pemeliharaan semesteran menggunakan format `- [ ]`.

- [ ] **2.11.** Tulis **Bab 9 — SOP Pemeliharaan Rutin Tahunan**:
  - [ ] 2.11.1. Tulis prosedur audit keamanan menyeluruh (verifikasi seluruh layer defense in depth).
  - [ ] 2.11.2. Tulis prosedur review kepatuhan UU PDP No. 27/2022 (verifikasi enkripsi, right to erasure).
  - [ ] 2.11.3. Tulis prosedur evaluasi end-of-life hardware (SSD, RAM, UPS, switch hub).
  - [ ] 2.11.4. Tulis prosedur review relevansi parameter `system_configs` di database.
  - [ ] 2.11.5. Tulis prosedur perencanaan upgrade versi dan roadmap (sesuai R-05 Bab 15).
  - [ ] 2.11.6. Buat checklist pemeliharaan tahunan menggunakan format `- [ ]`.

- [ ] **2.12.** Tulis **Bab 10 — Prosedur Pemeliharaan Korektif**:
  - [ ] 2.12.1. Tulis alur pelaporan bug pasca-produksi (adoptasi format dari R-07).
  - [ ] 2.12.2. Tulis klasifikasi severity dan priority (ringkasan dari R-07 Bab 2 dan 3).
  - [ ] 2.12.3. Tulis prosedur root cause analysis.
  - [ ] 2.12.4. Tulis prosedur pengembangan patch (branching Git, coding standard FP, unit test).
  - [ ] 2.12.5. Tulis prosedur deployment patch ke produksi (update kode, restart, smoke test).
  - [ ] 2.12.6. Tulis prosedur rollback patch jika gagal (git checkout tag stabil).
  - [ ] 2.12.7. Buat diagram alur patching menggunakan Mermaid flowchart.
  - [ ] 2.12.8. Tulis tabel SLA penanganan bug per severity level (adoptasi dari R-07 Bab 7.3).

- [ ] **2.13.** Tulis **Bab 11 — Prosedur Pemeliharaan Adaptif**:
  - [ ] 2.13.1. Tulis prosedur upgrade versi Python runtime (adoptasi dari R-06 Bab 4.4-4.5).
  - [ ] 2.13.2. Tulis prosedur upgrade versi pustaka dependensi (pip install, offline wheels).
  - [ ] 2.13.3. Tulis prosedur migrasi skema database (ALTER TABLE, ADD COLUMN, backup sebelum migrasi).
  - [ ] 2.13.4. Tulis prosedur upgrade sistem operasi server/klien.
  - [ ] 2.13.5. Tulis prosedur penambahan node klien baru (ekspansi — Multi-Branch Ready).
  - [ ] 2.13.6. Buat checklist pre-upgrade dan post-upgrade.

- [ ] **2.14.** Tulis **Bab 12 — Prosedur Backup, Restore, dan Disaster Recovery** (adoptasi dan perluas dari R-01 Bab 10):
  - [ ] 2.14.1. Tulis strategi backup 3 tier (harian=cron otomatis, bulanan=cold storage, tahunan=arsip permanen).
  - [ ] 2.14.2. Tulis prosedur backup otomatis harian (skrip bash cron, adoptasi dari R-01 Bab 10.1).
  - [ ] 2.14.3. Tulis prosedur backup manual on-demand (adoptasi dari R-01 Bab 10.2).
  - [ ] 2.14.4. Tulis prosedur restore database dari backup (adoptasi dari R-01 Bab 8.2).
  - [ ] 2.14.5. Tulis prosedur disaster recovery (adoptasi dari R-01 Bab 10.4).
  - [ ] 2.14.6. Tulis strategi retensi dan rotasi backup (30 hari server, 12 bulan cold storage).
  - [ ] 2.14.7. Buat diagram alur backup dan restore menggunakan Mermaid flowchart.

- [ ] **2.15.** Tulis **Bab 13 — Prosedur Penanganan Insiden dan Eskalasi** (adoptasi dari R-03 Bab 10.6 dan R-01 Bab 11.5-11.6):
  - [ ] 2.15.1. Tulis definisi dan klasifikasi 5 jenis insiden keamanan (adoptasi dari R-03 Bab 10.6.A).
  - [ ] 2.15.2. Tulis matriks eskalasi insiden 3 level (staf kasir → kepala percetakan → pemilik/DevOps).
  - [ ] 2.15.3. Tulis prosedur deteksi insiden (otomatis via dashboard, manual via staf).
  - [ ] 2.15.4. Tulis prosedur respon insiden (isolasi, pelaporan, pemulihan).
  - [ ] 2.15.5. Tulis prosedur penanganan insiden keamanan khusus (brute-force, selisih kas berulang, akses fisik ilegal).
  - [ ] 2.15.6. Tulis SOP graceful shutdown saat mati listrik UPS (adoptasi dari R-01 Bab 11.6).
  - [ ] 2.15.7. Tulis kontak darurat dan jalur eskalasi (nomor WA, email, waktu layanan).
  - [ ] 2.15.8. Buat diagram alur eskalasi insiden menggunakan Mermaid flowchart.

- [ ] **2.16.** Tulis **Bab 14 — Pemeliharaan Keamanan Sistem** (adoptasi dari R-03):
  - [ ] 2.16.1. Tulis jadwal rotasi kunci dan kredensial (tabel: item, frekuensi, prosedur).
  - [ ] 2.16.2. Tulis prosedur pengelolaan akun pengguna (tambah, nonaktifkan, reset password — adoptasi dari R-03 Bab 8.3).
  - [ ] 2.16.3. Tulis prosedur pemantauan log audit trail (query SQL contoh untuk deteksi anomali).
  - [ ] 2.16.4. Tulis prosedur penanganan insiden fraud (selisih kas berulang, retur abnormal — adoptasi dari R-03 Bab 7.4).
  - [ ] 2.16.5. Tulis prosedur verifikasi hardening OS dan firewall (checklist ufw, SSH, chmod, bind-address).
  - [ ] 2.16.6. Tulis prosedur kepatuhan berkala UU PDP No. 27/2022 (verifikasi Fernet, right to erasure).

- [ ] **2.17.** Tulis **Bab 15 — Pemeliharaan Database**:
  - [ ] 2.17.1. Tulis prosedur CHECK TABLE dan REPAIR TABLE (perintah SQL detail untuk 28 tabel).
  - [ ] 2.17.2. Tulis prosedur ANALYZE TABLE dan OPTIMIZE TABLE (untuk performa query).
  - [ ] 2.17.3. Tulis prosedur pemantauan kapasitas disk database (perintah `df`, `du`, `SHOW TABLE STATUS`).
  - [ ] 2.17.4. Tulis prosedur purging data log audit lama > 12 bulan (backup lama → compress → delete).
  - [ ] 2.17.5. Tulis prosedur verifikasi connection pool dan retry mechanism (pool_size=5, retry 3x).
  - [ ] 2.17.6. Tulis prosedur migrasi data antar cabang (Multi-Branch Ready, `cabang_id`).

- [ ] **2.18.** Tulis **Bab 16 — Pemeliharaan Hardware dan Infrastruktur**:
  - [ ] 2.18.1. Tulis jadwal pemeriksaan hardware berkala (tabel: komponen, frekuensi, metode pemeriksaan).
  - [ ] 2.18.2. Tulis prosedur penggantian SSD, RAM, dan komponen server.
  - [ ] 2.18.3. Tulis prosedur penggantian kabel LAN Cat6 dan switch hub.
  - [ ] 2.18.4. Tulis prosedur penggantian printer thermal (konfigurasi ulang driver Generic/Text Only).
  - [ ] 2.18.5. Tulis prosedur penggantian baterai UPS.
  - [ ] 2.18.6. Tulis daftar inventaris hardware dan estimasi umur pakai (tabel: item, tanggal beli, estimasi umur, status).

- [ ] **2.19.** Tulis **Bab 17 — Troubleshooting Guide** (adoptasi dan perluas dari R-01 Bab 11.4):
  - [ ] 2.19.1. Tulis panduan troubleshooting ERR-DB-001/002 (koneksi database terputus/integritas).
  - [ ] 2.19.2. Tulis panduan troubleshooting ERR-AUTH-001/002/003 (login gagal, brute-force, akses ditolak).
  - [ ] 2.19.3. Tulis panduan troubleshooting ERR-SESSION-001/002 (sesi tidak ada/rusak/expired).
  - [ ] 2.19.4. Tulis panduan troubleshooting ERR-FILE-001/039 (file .env hilang, backup korup).
  - [ ] 2.19.5. Tulis panduan troubleshooting ERR-CASH-001/004 (selisih kas, saldo tidak cukup).
  - [ ] 2.19.6. Tulis panduan troubleshooting rendering CLI (ANSI glitch, mojibake di CMD Windows).
  - [ ] 2.19.7. Tulis panduan troubleshooting printer thermal (struk acak, laci tidak buka).
  - [ ] 2.19.8. Tulis panduan troubleshooting performa query lambat (> 2 detik, indexing, EXPLAIN ANALYZE).
  - [ ] 2.19.9. Tulis panduan troubleshooting stok desimal tidak sinkron (decimal precision, stock opname).
  - [ ] 2.19.10. Setiap masalah harus memiliki format: **Gejala**, **Kemungkinan Penyebab**, **Langkah Solusi**, **Pencegahan**.

- [ ] **2.20.** Tulis **Bab 18 — Matriks Risiko Pemeliharaan** (adoptasi dan perluas dari R-01 Bab 13 dan R-05 Bab 13):
  - [ ] 2.20.1. Identifikasi minimal 10 risiko operasional pasca-produksi.
  - [ ] 2.20.2. Buat tabel matriks risiko (ID, Komponen, Deskripsi, Probabilitas 1-5, Dampak 1-5, Skor, Mitigasi, Kontingensi).
  - [ ] 2.20.3. Tulis rencana kontingensi per risiko.

- [ ] **2.21.** Tulis **Bab 19 — Peran dan Tanggung Jawab Pemeliharaan**:
  - [ ] 2.21.1. Buat matriks RACI pemeliharaan (tabel: aktivitas vs peran).
  - [ ] 2.21.2. Tulis tanggung jawab detail setiap peran (Pemilik, Kepala Percetakan, Kasir/Staf, SysAdmin, Tim AI).

- [ ] **2.22.** Tulis **Bab 20 — Jadwal Pemeliharaan Konsolidasi**:
  - [ ] 2.22.1. Buat kalender pemeliharaan tahunan dalam format tabel visual (bulan vs aktivitas).
  - [ ] 2.22.2. Buat ringkasan frekuensi aktivitas pemeliharaan (tabel: aktivitas, frekuensi, pelaksana, durasi estimasi).

- [ ] **2.23.** Tulis **Bab 21 — Glosarium** (minimal 25 istilah teknis yang digunakan dalam dokumen).

- [ ] **2.24.** Tulis **Bab 22 — Referensi Dokumen**:
  - [ ] 2.24.1. Buat tabel daftar seluruh 14 file referensi (R-01 s.d R-14) yang digunakan dalam penyusunan, lengkap dengan kode referensi, nama dokumen, path relatif, dan peran/hubungan dalam penyusunan.

---

### Tahap 3: Validasi dan Penulisan ke Target File

> **Tujuan**: Memastikan kualitas dan kelengkapan dokumen sebelum ditulis ke target file.

- [ ] **3.1.** Validasi kelengkapan konten:
  - [ ] 3.1.1. Pastikan semua 22 bab sudah ditulis secara lengkap dan substantif.
  - [ ] 3.1.2. Pastikan semua diagram Mermaid yang disebutkan (minimal 5 diagram: arsitektur deployment, alur patching, alur backup/restore, alur eskalasi insiden, alur disaster recovery) sudah dibuat.
  - [ ] 3.1.3. Pastikan semua checklist pemeliharaan (harian, mingguan, bulanan, kuartalan, semesteran, tahunan) sudah dibuat menggunakan format markdown `- [ ]`.
  - [ ] 3.1.4. Pastikan semua tabel (matriks komponen, matriks risiko, matriks RACI, kalender pemeliharaan, jadwal rotasi kunci, inventaris hardware) sudah dibuat.

- [ ] **3.2.** Validasi konsistensi data:
  - [ ] 3.2.1. Pastikan semua spesifikasi hardware konsisten dengan R-01 dan R-02 (IP server 192.168.1.200, port 3306, UPS 600VA, dll.).
  - [ ] 3.2.2. Pastikan semua kode error konsisten dengan R-03 dan R-07 (ERR-AUTH-xxx, ERR-DB-xxx, dll.).
  - [ ] 3.2.3. Pastikan semua parameter konfigurasi konsisten dengan R-04 dan R-05.
  - [ ] 3.2.4. Pastikan semua nama modul konsisten dengan R-02 dan R-05 (M.1 s.d M.10).
  - [ ] 3.2.5. Pastikan semua jadwal rotasi kunci konsisten dengan R-03 (JWT 6 bulan, Fernet 6 bulan).

- [ ] **3.3.** Validasi data kosong:
  - [ ] 3.3.1. Untuk setiap data yang **TIDAK ditemukan** di file referensi, tandai dengan label:
    ```
    > ⚠️ **[DATA BELUM TERSEDIA — HARUS DIISI MANUAL]**: [Deskripsi data yang diperlukan].
    ```
  - [ ] 3.3.2. Jangan mengarang atau mengasumsikan data yang tidak ada. Biarkan placeholder label di atas sebagai penanda.

- [ ] **3.4.** Validasi bahasa:
  - [ ] 3.4.1. Pastikan seluruh isi dokumen menggunakan bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami.
  - [ ] 3.4.2. Hindari istilah teknis yang tidak umum tanpa penjelasan — jika harus menggunakan istilah teknis, berikan penjelasan dalam kurung.
  - [ ] 3.4.3. Gunakan kalimat aktif dan instruksi langkah demi langkah yang jelas.

- [ ] **3.5.** Tulis seluruh konten dokumen utama yang sudah divalidasi ke target file:
  - [ ] 3.5.1. **Target File**: `docs/sdlc/07_maintenance/01_maintenance_guide.md`
  - [ ] 3.5.2. Pastikan file ditulis secara **UTUH dan LENGKAP dari awal sampai akhir** — DILARANG KERAS memotong (truncate) konten di tengah jalan.
  - [ ] 3.5.3. Pastikan file berisi minimal 22 bab sesuai kerangka yang ditentukan di Bagian 4 issue ini.
  - [ ] 3.5.4. Pastikan file diakhiri dengan bab **Referensi Dokumen** yang berisi tabel seluruh file referensi yang digunakan.

---

## 6. Instruksi Tambahan

### 6.1. Standar Kualitas Konten Spesifik Maintenance Guide
- Dokumen Maintenance Guide memiliki ciri khas yang membedakannya dari dokumen SDLC fase lain: **dokumen ini bersifat prosedural operasional yang akan digunakan berulang kali secara harian oleh staf non-teknis**. Oleh karena itu:
  - Setiap SOP harus ditulis dalam format langkah bernomor yang sangat detail (step-by-step numbered list).
  - Setiap perintah terminal/SQL harus dilengkapi label OS (`# [LINUX DEBIAN 12 — Server]` atau `# [WINDOWS 11 — Klien]`).
  - Setiap checklist harus menggunakan format markdown `- [ ]` agar bisa di-centang.
  - Setiap prosedur harus menyebutkan **siapa** (aktor/peran yang bertanggung jawab), **kapan** (waktu/jadwal), dan **bagaimana** (langkah-langkah teknis).

### 6.2. Standar Diagram Mermaid
- Gunakan minimal **5 diagram Mermaid** dalam dokumen ini:
  1. Diagram arsitektur deployment produksi (graph TD).
  2. Diagram alur patching korektif (flowchart TD).
  3. Diagram alur backup dan restore (flowchart TD).
  4. Diagram alur eskalasi insiden (flowchart TD).
  5. Diagram kalender pemeliharaan atau diagram alur disaster recovery (flowchart TD).

### 6.3. Pastikan Dokumen Layak Dijadikan Referensi
- Dokumen ini harus **self-contained** — seseorang yang membaca dokumen ini saja (tanpa membaca dokumen lain) harus dapat memahami dan menjalankan seluruh prosedur pemeliharaan sistem AbuCom.
- Dokumen ini harus menjadi **single source of truth** untuk semua aktivitas pemeliharaan pasca Go-Live.
- Kualitas dokumen ini harus setara atau melebihi standar Deployment Guide (R-01) dalam hal kelengkapan, kedalaman teknis, dan kejelasan instruksi.

### 6.4. Kaidah Penulisan Front Matter
- Tulis front matter YAML di baris pertama file dengan format yang sama persis dengan dokumen SDLC lainnya (lihat contoh di R-01 baris 1-10).

### 6.5. Integrasi Data Known Issues
- Pastikan known issues dari Release Notes (DEF-COMPAT-001: mojibake CMD, DEF-PERF-001: latensi query > 2 detik) disebutkan di Bab 17 Troubleshooting sebagai masalah yang sudah diidentifikasi beserta workaround-nya.

### 6.6. Integrasi Roadmap Maintenance
- Pastikan fitur yang direncanakan pada roadmap Release Notes v1.1.0, v1.2.0, dan v2.0.0 (jika ada di R-05 Bab 15) disebutkan di Bab 11 (Pemeliharaan Adaptif) sebagai rencana upgrade masa depan.

---

## 7. Ringkasan Deliverable

| No | Item Deliverable                                                    | Status     |
|:--:|---------------------------------------------------------------------|:----------:|
| 1  | Membaca dan merangkum 14 file referensi (R-01 s.d R-14)            | `[ ]`      |
| 2  | Menulis 22 bab dokumen Maintenance Guide sesuai kerangka            | `[ ]`      |
| 3  | Membuat minimal 5 diagram Mermaid                                   | `[ ]`      |
| 4  | Membuat 6 set checklist pemeliharaan (harian s.d tahunan)           | `[ ]`      |
| 5  | Membuat minimal 5 tabel matriks (komponen, risiko, RACI, dll.)      | `[ ]`      |
| 6  | Menandai data kosong dengan label `[DATA BELUM TERSEDIA]`           | `[ ]`      |
| 7  | Validasi konsistensi data dengan file referensi                     | `[ ]`      |
| 8  | Menulis seluruh konten ke target file secara utuh tanpa pemotongan  | `[ ]`      |

---

## 8. Catatan untuk Pelaksana (Junior Programmer / AI Model)

1. **JANGAN** mengarang data, angka, atau parameter teknis yang tidak ditemukan di file referensi. Gunakan label `[DATA BELUM TERSEDIA — HARUS DIISI MANUAL]` jika data tidak ditemukan.
2. **JANGAN** memotong (truncate) konten dokumen di tengah jalan. Seluruh 22 bab harus ditulis lengkap dari awal sampai akhir.
3. **JANGAN** mengubah kerangka bab yang sudah ditentukan di Bagian 4 tanpa persetujuan.
4. **PASTIKAN** semua perintah terminal (bash/cmd/SQL) yang ditulis sudah benar secara sintaks dan bisa dieksekusi langsung.
5. **PASTIKAN** semua referensi path file menggunakan format relatif dari root `docs/` yang konsisten.
6. **OVERWRITE** file target `docs/sdlc/07_maintenance/01_maintenance_guide.md` secara keseluruhan dengan konten yang baru dibuat.
7. **PRIORITAS**: Fokus pada konten yang substantif, lengkap, dan dapat langsung digunakan sebagai panduan operasional — bukan konten yang generik atau boilerplate kosong.

---

*Issue ini disusun oleh **System Strategist & Security Lead** pada tanggal **27 Mei 2026** sebagai panduan low-level untuk pembuatan dokumen Maintenance Guide proyek AbuCom.*
