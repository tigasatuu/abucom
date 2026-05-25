# Pembuatan Dokumen Security Design

---

| Atribut         | Nilai                                                        |
|-----------------|--------------------------------------------------------------|
| **Judul**       | Pembuatan dan Penyusunan Dokumen Security Design             |
| **Target File** | `docs/sdlc/03_design/06_security_design.md`                  |
| **Prioritas**   | High                                                         |
| **Status**      | Open                                                         |
| **Tanggal**     | 2026-05-25                                                   |
| **Fase SDLC**   | Fase 03 — Design (Perancangan Sistem)                        |

---

## 1. Persona Pelaksana

**Persona yang ditugaskan**: **Senior Security Architect & Cybersecurity Compliance Specialist**

**Justifikasi pemilihan persona**:
- Dokumen Security Design adalah dokumen keamanan menyeluruh yang menuntut keahlian mendalam di bidang arsitektur keamanan sistem, kriptografi, manajemen otorisasi (RBAC), kepatuhan regulasi (UU PDP No. 27/2022), dan strategi pertahanan berlapis (*Defense in Depth*).
- Persona ini memiliki otoritas penuh untuk menetapkan kebijakan keamanan, mekanisme enkripsi, standar audit trail, dan prosedur mitigasi ancaman yang akan menjadi acuan mutlak bagi seluruh fase implementasi dan pengujian keamanan berikutnya.
- Persona ini relevan dengan peran **Claude Opus 4.6 (Thinking)** yang ditugaskan sebagai *System Strategist & Security Lead* (STK-013) dalam susunan tim pengembang proyek AbuCom.

---

## 2. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca** dan **dirangkum** sebagai dasar utama pengerjaan dokumen Security Design ini. File-file dipilih berdasarkan relevansi langsung terhadap aspek keamanan, otorisasi, proteksi data, dan arsitektur sistem.

| No | File Referensi | Path Relatif | Alasan Pemilihan | Prioritas |
|----|---------------|--------------|-------------------|-----------|
| 1 | **Access Control Matrix (ACM) v1.1** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Sumber utama definisi 8 peran RBAC, matriks hak akses 44 use case, matriks CRUD 28 tabel, aturan eskalasi supervisor, rate limiting, dan session JWT. Dokumen ini adalah fondasi utama Security Design. | **PRIMER** |
| 2 | **System Architecture v1.1** | `docs/sdlc/03_design/03_system_architecture.md` | Sumber arsitektur keamanan berlapis (Defense in Depth Bab 7), otentikasi bcrypt/JWT, otorisasi RBAC, proteksi data (SQL Injection, sanitasi CLI, AES-256 backup, UU PDP), audit trail JSON, dan infrastruktur fisik LAN. | **PRIMER** |
| 3 | **Software Requirements Specification (SRS) v1.1** | `docs/sdlc/02_analysis/02_software_requirements.md` | Sumber spesifikasi fungsional Modul M.7 (Keamanan, Audit Trail & Hak Akses), parameter teknis JWT/bcrypt, kode error keamanan, dan kebutuhan non-fungsional keamanan. | **PRIMER** |
| 4 | **Tech Stack Decision v1.1** | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Sumber keputusan teknologi keamanan (bcrypt cost 12, PyJWT HS256, python-dotenv, parameterized queries, rate limiting, sanitasi input CLI, kepatuhan UU PDP, AES-256). | **PRIMER** |
| 5 | **Database Schema (DDL SQL) v1.1** | `docs/sdlc/03_design/01_database_schema.sql` | Sumber skema fisik tabel keamanan (`pengguna`, `audit_logs`, `shift_handover`, `backup_logs`, `system_configs`) termasuk kolom `password_hash`, `failed_login_attempts`, `locked_until`, constraint CHECK, dan sensitivitas data per tabel. | **SEKUNDER** |
| 6 | **ERD Database v1.1** | `docs/sdlc/03_design/02_erd_database.md` | Sumber relasi visual antar-tabel keamanan dan kardinalitas FK untuk memahami aliran data audit dan otorisasi. | **SEKUNDER** |
| 7 | **Business Requirements (BRD) v1.1** | `docs/sdlc/02_analysis/01_business_requirements.md` | Sumber kebutuhan bisnis keamanan asli (BR-F-30 RBAC, BR-F-31 Audit Trail, BR-F-34 Fraud Detection, BR-F-39 Backup/Restore) dan konteks otorisasi pemilik. | **SEKUNDER** |
| 8 | **Workflow Diagram v1.1** | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Sumber alur kerja operasional yang membutuhkan checkpoint otorisasi keamanan (transaksi kasir, shift handover, stock opname, retur). | **TERSIER** |
| 9 | **CLI Interaction Flow v1.1** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Sumber detail alur interaksi terminal CLI yang membutuhkan proteksi keamanan (login flow, menu RBAC, eskalasi supervisor). | **TERSIER** |
| 10 | **Stakeholder Register v1.1** | `docs/sdlc/01_planning/03_stakeholder_register.md` | Sumber identifikasi peran stakeholder dan level akses yang dibutuhkan per aktor. | **TERSIER** |

> **Catatan**: File `narasi.txt` (`docs/sdlc/narasi.txt`) **tidak lagi diperlukan** sebagai referensi langsung karena seluruh informasi keamanan yang relevan dari narasi awal pemilik sudah terabstraksi secara lengkap ke dalam dokumen BRD, SRS, ACM, dan System Architecture di atas.

---

## 3. Kerangka Struktur Dokumen Security Design

Berikut adalah kerangka dokumen Security Design dengan standar struktur industri yang lengkap dan informatif, mengikuti praktik terbaik *OWASP Security Design Guidelines* dan *NIST Cybersecurity Framework* yang diadaptasi untuk konteks aplikasi CLI lokal UMKM:

```
---
dokumen    : Security Design
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [TANGGAL PENGERJAAN]
status     : Draft
penyusun   : Senior Security Architect & Cybersecurity Compliance Specialist
---

# Security Design — AbuCom

## Riwayat Perubahan Dokumen
(Tabel riwayat versi dokumen)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan

---

## 2. Prinsip dan Strategi Keamanan Sistem
### 2.1. Prinsip Keamanan Utama (Security Principles)
    (Least Privilege, Defense in Depth, Separation of Duties,
     Default Deny, Fail-Secure, Data Minimization)
### 2.2. Model Ancaman (Threat Model)
    (Identifikasi ancaman spesifik untuk toko percetakan CLI LAN lokal:
     fraud karyawan, brute-force login, SQL injection, pencurian
     fisik server, kebocoran data pelanggan, manipulasi stok, dll.)
### 2.3. Klasifikasi Tingkat Sensitivitas Data
    (Sangat Sensitif, Sensitif, Operasional — sesuai ACM Bab 3.2)

---

## 3. Arsitektur Keamanan (Security Architecture)
### 3.1. Diagram Keamanan Berlapis (Defense in Depth)
    (Mermaid diagram: Jaringan Fisik → OS Hardening → Otentikasi →
     Otorisasi → Proteksi Aplikasi → Proteksi Data)
### 3.2. Keamanan Jaringan Fisik (Network Security)
    (LAN offline, firewall ufw, IP statis server, UPS)
### 3.3. Keamanan Sistem Operasi (OS Hardening)
    (chmod 700 backup, bind-address MySQL, user privilege minimization)
### 3.4. Keamanan Koneksi Database (Database Security)
    (Parameterized queries, connection pooling, firewall port 3306,
     REPEATABLE READ isolation, credential management)

---

## 4. Desain Otentikasi (Authentication Design)
### 4.1. Enkripsi Kata Sandi (bcrypt Cost Factor 12)
    (Alur hashing, verifikasi, parameter konfigurasi, diagram sequence)
### 4.2. Manajemen Session CLI (JWT HS256)
    (Payload token, lifecycle 8 jam, validasi signature, expiration
     handling, penyimpanan token di memori lokal)
### 4.3. Rate Limiting dan Penguncian Akun
    (5 percobaan, lockout 10 menit, counter reset, kolom database)
### 4.4. Alur Login Lengkap (Sequence Diagram)
    (Mermaid sequence diagram end-to-end dari input credential
     hingga pembuatan token JWT dan audit log login)
### 4.5. Alur Logout dan Penghancuran Session
    (Prosedur pembersihan token dari memori lokal)

---

## 5. Desain Otorisasi (Authorization Design)
### 5.1. Model RBAC Multi-Level (8 Peran)
    (Definisi hierarki: Level 1 Pemilik, Level 2 Supervisor,
     Level 3 Staf Operasional — sesuai ACM)
### 5.2. Implementasi Decorator/Guard Otorisasi
    (Pseudocode FP untuk check_permission, @require_role decorator,
     state dict role checking)
### 5.3. Matriks Akses Modul per Peran (Ringkasan)
    (Tabel ringkasan 10 modul × 8 peran dari ACM)
### 5.4. Aturan Eskalasi Otorisasi Pemilik
    (4 operasi kritis yang memerlukan sandi pemilik: retur DP,
     retur barang, pengeluaran besar, restorasi database)
### 5.5. Aturan Otorisasi Kepala Percetakan
    (3 operasi verifikasi: stock opname, shift handover normal,
     shift handover anomali)
### 5.6. Kebijakan Default Deny
    (Implementasi teknis: setiap menu yang tidak secara eksplisit
     diberikan izin = ditolak otomatis)

---

## 6. Desain Proteksi Data (Data Protection Design)
### 6.1. Enkripsi Data at Rest
    (AES-256 backup ZIP, bcrypt password hash, enkripsi WhatsApp pelanggan)
### 6.2. Proteksi Data in Transit
    (LAN lokal kabel UTP Cat6, TCP/IP Port 3306, tanpa internet)
### 6.3. Kepatuhan UU PDP No. 27/2022
    (Enkripsi reversible nomor WhatsApp pelanggan CRM,
     pembatasan akses data pribadi, hak penghapusan data)
### 6.4. Proteksi Input Aplikasi (Input Validation)
    (Sanitasi terminal control characters, parameterized queries SQL,
     length bounds validation, regex format validation)
### 6.5. Manajemen Kredensial dan Secrets
    (File .env, .gitignore exclusion, JWT secret key 32+ char hex,
     startup validator untuk keberadaan .env)
### 6.6. Klasifikasi dan Perlindungan Tabel Database
    (5 tabel Sangat Sensitif, 7 tabel Sensitif, 16 tabel Operasional
     — implementasi perlindungan per klasifikasi)

---

## 7. Desain Audit Trail dan Monitoring
### 7.1. Skema Tabel Audit Logs
    (Struktur kolom: pengguna_id, action_type, target_table,
     old_value JSON, new_value JSON, ip_address, action_timestamp)
### 7.2. Event Pemicu Pencatatan Audit
    (INSERT/UPDATE/DELETE data sensitif, ACCESS_DENIED,
     login/logout, eskalasi otorisasi, backup/restore)
### 7.3. Format Pencatatan JSON (old_value / new_value)
    (Contoh format JSON untuk setiap tipe action)
### 7.4. Deteksi Anomali dan Fraud (Fraud Detection)
    (Alert indikator visual anomali kasir harian — selisih kas,
     frekuensi retur abnormal, login gagal berulang)
### 7.5. Retensi dan Pemeliharaan Log Audit
    (Kebijakan retensi 12 bulan, arsip cold storage, log rotation)

---

## 8. Desain Keamanan Operasional
### 8.1. Prosedur Serah Terima Shift (Shift Handover Security)
    (Alur rekonsiliasi kas, toleransi selisih Rp 10.000,
     otorisasi supervisor pada anomali, diagram sequence)
### 8.2. Prosedur Backup dan Restore Aman
    (mysqldump terjadwal, enkripsi AES-256 ZIP, chmod 700,
     verifikasi sandi pemilik saat restore, diagram alur)
### 8.3. Prosedur Pengelolaan Akun Pengguna
    (Pembuatan akun staf baru oleh pemilik, perubahan password mandiri,
     penonaktifan akun, reset lockout)
### 8.4. Keamanan Fisik Server dan Infrastruktur
    (Penempatan Mini PC Server di area aman toko, UPS,
     pembatasan akses fisik ke perangkat jaringan)

---

## 9. Alur Keamanan Kritis (Security Flow Diagrams)
### 9.1. Alur Otentikasi Login CLI (Sequence Diagram)
### 9.2. Alur Otorisasi Transaksi Kasir (Sequence Diagram)
### 9.3. Alur Eskalasi Retur/Pembatalan (Sequence Diagram)
### 9.4. Alur Rekonsiliasi Kas dan Shift Handover (Sequence Diagram)
### 9.5. Alur Stock Opname dengan Otorisasi Supervisor (Flowchart)
### 9.6. Alur Backup dan Restore Database (Flowchart)

---

## 10. Penanganan Error dan Kode Keamanan
### 10.1. Tabel Kode Error Keamanan (ERR-AUTH-xxx)
### 10.2. Tabel Kode Error Session (ERR-SESSION-xxx)
### 10.3. Tabel Kode Error Database Keamanan (ERR-DB-xxx)
### 10.4. Tabel Kode Error File/Backup (ERR-FILE-xxx)
### 10.5. Tabel Kode Error Kas (ERR-CASH-xxx)
### 10.6. Prosedur Respon Insiden Keamanan

---

## 11. Analisis Risiko Keamanan
### 11.1. Matriks Risiko Keamanan
    (Tabel: ID Risiko, Komponen, Deskripsi Ancaman, Probabilitas,
     Dampak, Skor, Rencana Mitigasi Teknis)
### 11.2. Rencana Mitigasi per Risiko
### 11.3. Kriteria Evaluasi Ulang Keamanan

---

## 12. Spesifikasi Implementasi Teknis Keamanan
### 12.1. Penempatan Modul Keamanan
    (middleware/rbac.py, middleware/logger.py, utils/backup.py, dll.)
### 12.2. Pseudocode Fungsi Keamanan (FP Murni)
    (check_permission, validate_jwt, hash_password, verify_password,
     log_audit_trail, sanitize_input, encrypt_backup)
### 12.3. Konfigurasi File .env (Parameter Keamanan)
### 12.4. Konfigurasi Server dan Firewall

---

## 13. Matriks Ketertelusuran Keamanan (Security Traceability Matrix)
### 13.1. Mapping Security Design ke SRS
### 13.2. Mapping Security Design ke ACM
### 13.3. Mapping Security Design ke Tech Stack Decision
### 13.4. Mapping Security Design ke Use Case

---

## 14. Persetujuan dan Otorisasi Dokumen
(Tabel persetujuan formal oleh Pemilik dan Arsitek)

---

## 15. Glosarium Istilah Keamanan
(Definisi semua istilah keamanan yang digunakan dalam dokumen)

---

## 16. Referensi Dokumen
(Tabel berkas referensi yang digunakan dalam penyusunan dokumen ini)
```

---

## 4. Instruksi Detail Tahapan Pengerjaan

### Tahap 1 — Persiapan dan Pembacaan File Referensi

- [ ] **1.1.** Baca dan pahami keseluruhan isi file `docs/sdlc/02_analysis/06_access_control_matrix.md` (ACM v1.1). Rangkum semua data berikut tanpa ada yang terlewat:
  - [ ] 1.1.1. Definisi 8 peran internal sistem (Bab 2.1) beserta kode peran, deskripsi, dan level hierarki.
  - [ ] 1.1.2. Definisi 4 aktor eksternal (Bab 2.3) beserta strategi perlindungan keamanan.
  - [ ] 1.1.3. Konvensi notasi hak akses (Bab 1.6): FULL, READ, INPUT, DENY, ESCALATE, RITEL.
  - [ ] 1.1.4. Seluruh matriks akses modul M.1 sampai M.10 dan Use Case Dasar (Bab 4.2 — 4.12).
  - [ ] 1.1.5. Seluruh matriks CRUD per tabel database — 28 tabel (Bab 5.2).
  - [ ] 1.1.6. Aturan eskalasi otorisasi Pemilik — 4 operasi kritis (Bab 6.1).
  - [ ] 1.1.7. Aturan otorisasi Kepala Percetakan — 3 operasi verifikasi (Bab 6.2).
  - [ ] 1.1.8. Aturan pembatasan akses data sensitif dan UU PDP (Bab 6.3).
  - [ ] 1.1.9. Aturan session JWT dan timeout (Bab 6.4).
  - [ ] 1.1.10. Aturan rate limiting dan penguncian akun (Bab 6.5).
  - [ ] 1.1.11. Aturan pencatatan audit trail pada pelanggaran akses (Bab 6.6).
  - [ ] 1.1.12. Diagram alur otorisasi Mermaid — 5 diagram (Bab 7.1 — 7.5).
  - [ ] 1.1.13. Statistik ringkasan hak akses per peran (Bab 9).
  - [ ] 1.1.14. Glosarium istilah keamanan (Bab 10).

- [ ] **1.2.** Baca dan pahami keseluruhan isi file `docs/sdlc/03_design/03_system_architecture.md` (System Architecture v1.1). Rangkum semua data berikut tanpa ada yang terlewat:
  - [ ] 1.2.1. Arsitektur keamanan berlapis / Defense in Depth (Bab 7) — seluruh sub-bab.
  - [ ] 1.2.2. Otentikasi: bcrypt cost 12 (Bab 7.2.1), JWT HS256 8 jam (Bab 7.2.2), rate limiting (Bab 7.2.3).
  - [ ] 1.2.3. Otorisasi RBAC 8 peran dan matriks akses modul per role (Bab 7.3).
  - [ ] 1.2.4. Proteksi data: parameterized queries (Bab 7.4.1), sanitasi input CLI (Bab 7.4.2), enkripsi backup AES-256 (Bab 7.4.3), kepatuhan UU PDP (Bab 7.4.4).
  - [ ] 1.2.5. Audit trail: struktur log JSON (Bab 7.5.1), pemicu pencatatan (Bab 7.5.2).
  - [ ] 1.2.6. Topologi jaringan LAN dan infrastruktur fisik (Bab 3).
  - [ ] 1.2.7. Konfigurasi OS server dan klien (Bab 3.3).
  - [ ] 1.2.8. Strategi backup & disaster recovery (Bab 9.3).
  - [ ] 1.2.9. Analisis risiko arsitektur terkait keamanan (Bab 12).
  - [ ] 1.2.10. Konfigurasi file .env (Bab 9.2.4).
  - [ ] 1.2.11. Diagram sequence login & JWT (Bab 8.3.1).
  - [ ] 1.2.12. Diagram sequence shift handover (Bab 8.3.4).
  - [ ] 1.2.13. Penanganan error dan kode ERR (Bab 8.3.5).

- [ ] **1.3.** Baca dan pahami bagian keamanan dari file `docs/sdlc/02_analysis/02_software_requirements.md` (SRS v1.1). Rangkum data berikut:
  - [ ] 1.3.1. Spesifikasi SRS-F-030 (RBAC Multi-Level).
  - [ ] 1.3.2. Spesifikasi SRS-F-031 (Audit Trail Log JSON).
  - [ ] 1.3.3. Spesifikasi SRS-F-032 (Serah Terima Shift / Handover).
  - [ ] 1.3.4. Spesifikasi SRS-F-033 (Rekonsiliasi Kas Harian).
  - [ ] 1.3.5. Spesifikasi SRS-F-034 (Fraud Detection / Deteksi Anomali).
  - [ ] 1.3.6. Spesifikasi SRS-F-035 (Setup Awal Wizard).
  - [ ] 1.3.7. Spesifikasi SRS-F-039 (Database Backup & Restore).
  - [ ] 1.3.8. Seluruh kebutuhan non-fungsional terkait keamanan (SRS-NF-xxx di Bab 4).
  - [ ] 1.3.9. Seluruh kode error kategori ERR-AUTH-xxx yang didefinisikan di SRS.
  - [ ] 1.3.10. Daftar pustaka keamanan (bcrypt, pyjwt) dan versinya (Bab 2.4).

- [ ] **1.4.** Baca dan pahami bagian keamanan dari file `docs/sdlc/01_planning/04_tech_stack_decision.md` (Tech Stack v1.1). Rangkum data berikut:
  - [ ] 1.4.1. Strategi enkripsi kata sandi bcrypt (Bab 8.1) — alur hashing dan verifikasi.
  - [ ] 1.4.2. Strategi autentikasi session JWT (Bab 8.2) — algoritma, payload, lifecycle.
  - [ ] 1.4.3. Strategi hak akses RBAC (Bab 8.3) — daftar peran dan pembatasan menu.
  - [ ] 1.4.4. Strategi audit trail (Bab 8.4) — skema kolom dan trigger event.
  - [ ] 1.4.5. Strategi perlindungan data UU PDP (Bab 8.5) — AES-256, chmod 700, root password.
  - [ ] 1.4.6. Proteksi SQL Injection (Bab 8.6) — parameterized queries, larangan f-string.
  - [ ] 1.4.7. Rate limiting login CLI (Bab 8.7) — mekanisme, durasi, pencatatan status.
  - [ ] 1.4.8. Validasi input terminal CLI (Bab 8.8) — sanitasi, length bounds, regex.
  - [ ] 1.4.9. Konfigurasi `requirements.txt` dan `.env` (Bab 9.4 dan Bab 5.2).

- [ ] **1.5.** Baca dan pahami bagian keamanan dari file `docs/sdlc/03_design/01_database_schema.sql` (Database Schema v1.1). Rangkum data berikut:
  - [ ] 1.5.1. Struktur tabel `pengguna` — kolom `password_hash`, `role`, `failed_login_attempts`, `locked_until`, constraint CHECK.
  - [ ] 1.5.2. Struktur tabel `audit_logs` — seluruh kolom, komentar, dan engine.
  - [ ] 1.5.3. Struktur tabel `shift_handover` — kolom `status_handover`, `supervisor_id`, `selisih`, `catatan_alasan`.
  - [ ] 1.5.4. Struktur tabel `backup_logs` — seluruh kolom.
  - [ ] 1.5.5. Struktur tabel `system_configs` — parameter runtime keamanan.
  - [ ] 1.5.6. Klasifikasi sensitivitas data per tabel (dari komentar tabel di DDL: "Sangat Sensitif", "Sensitif", "Operasional").
  - [ ] 1.5.7. Data seed keamanan: default 8 peran, seed `system_configs` parameter keamanan.

- [ ] **1.6.** Baca dan pahami bagian keamanan dari file referensi sekunder dan tersier:
  - [ ] 1.6.1. ERD Database (`docs/sdlc/03_design/02_erd_database.md`) — relasi tabel keamanan.
  - [ ] 1.6.2. BRD (`docs/sdlc/02_analysis/01_business_requirements.md`) — kebutuhan bisnis keamanan asli (BR-F-30, BR-F-31, BR-F-34, BR-F-39).
  - [ ] 1.6.3. Workflow Diagram (`docs/sdlc/02_analysis/04_workflow_diagram.md`) — checkpoint otorisasi di alur operasional.
  - [ ] 1.6.4. CLI Interaction Flow (`docs/sdlc/03_design/04_cli_interaction_flow.md`) — detail interaksi login, menu RBAC, eskalasi.
  - [ ] 1.6.5. Stakeholder Register (`docs/sdlc/01_planning/03_stakeholder_register.md`) — grid power/interest peran keamanan.

### Tahap 2 — Analisis dan Konsolidasi Data Keamanan

- [ ] **2.1.** Konsolidasikan semua data otentikasi dari seluruh file referensi menjadi satu rangkuman terpadu:
  - [ ] 2.1.1. Parameter bcrypt: cost factor, alur hashing, alur verifikasi, contoh kode.
  - [ ] 2.1.2. Parameter JWT: algoritma HS256, payload (user_id, username, role, cabang_id, exp), secret key, masa berlaku 8 jam, handling expiration.
  - [ ] 2.1.3. Rate limiting: batas 5 kali, lockout 10 menit, kolom database, reset counter.
  - [ ] 2.1.4. Alur login lengkap: dari input username/password → verifikasi → pembuatan token → audit log.

- [ ] **2.2.** Konsolidasikan semua data otorisasi dari seluruh file referensi:
  - [ ] 2.2.1. Hierarki 3 level RBAC (Pemilik → Supervisor → Staf).
  - [ ] 2.2.2. Matriks hak akses ringkasan 10 modul × 8 peran.
  - [ ] 2.2.3. 4 aturan eskalasi otorisasi Pemilik (dengan ERR code).
  - [ ] 2.2.4. 3 aturan otorisasi Kepala Percetakan (dengan ERR code).
  - [ ] 2.2.5. Implementasi teknis decorator/guard RBAC di paradigma FP.

- [ ] **2.3.** Konsolidasikan semua data proteksi data:
  - [ ] 2.3.1. Enkripsi at rest: AES-256 backup, bcrypt password, enkripsi WhatsApp.
  - [ ] 2.3.2. Proteksi in transit: LAN offline, port 3306, firewall ufw.
  - [ ] 2.3.3. SQL Injection prevention: parameterized queries, larangan f-string.
  - [ ] 2.3.4. Input validation: sanitasi ASCII control, length bounds, regex.
  - [ ] 2.3.5. Kepatuhan UU PDP No. 27/2022.
  - [ ] 2.3.6. Klasifikasi sensitivitas 28 tabel database.

- [ ] **2.4.** Konsolidasikan semua data audit trail dan monitoring:
  - [ ] 2.4.1. Skema tabel `audit_logs` lengkap.
  - [ ] 2.4.2. Event pemicu pencatatan audit (INSERT, UPDATE, DELETE, ACCESS_DENIED).
  - [ ] 2.4.3. Format JSON old_value / new_value.
  - [ ] 2.4.4. Fraud detection: deteksi anomali kasir, selisih kas, frekuensi retur.
  - [ ] 2.4.5. Retensi log: kebijakan 12 bulan, purging, cold storage.

- [ ] **2.5.** Konsolidasikan semua data keamanan operasional:
  - [ ] 2.5.1. Alur shift handover (normal dan anomali).
  - [ ] 2.5.2. Alur backup dan restore aman.
  - [ ] 2.5.3. Pengelolaan akun pengguna.
  - [ ] 2.5.4. Keamanan fisik infrastruktur.

- [ ] **2.6.** Konsolidasikan seluruh kode error keamanan dari SRS, ACM, dan System Architecture:
  - [ ] 2.6.1. Kumpulkan semua kode ERR-AUTH-xxx.
  - [ ] 2.6.2. Kumpulkan semua kode ERR-SESSION-xxx.
  - [ ] 2.6.3. Kumpulkan semua kode ERR-DB-xxx yang terkait keamanan.
  - [ ] 2.6.4. Kumpulkan semua kode ERR-FILE-xxx.
  - [ ] 2.6.5. Kumpulkan semua kode ERR-CASH-xxx.

- [ ] **2.7.** Identifikasi data yang **tidak tersedia** (kosong) di file referensi dan tandai dengan placeholder:
  - [ ] 2.7.1. Tandai dengan format `**[DATA BELUM TERSEDIA — PERLU DIISI MANUAL]**` pada setiap data yang tidak ditemukan.
  - [ ] 2.7.2. Contoh data yang mungkin belum tersedia: detail prosedur respon insiden keamanan, kebijakan rotasi secret key JWT, kebijakan penghapusan data pelanggan (hak UU PDP), SLA pemulihan sistem, dll.

### Tahap 3 — Penulisan Dokumen Security Design

- [ ] **3.1.** Buat header metadata dokumen (YAML frontmatter) sesuai format standar proyek AbuCom:
  - [ ] 3.1.1. Isi field: dokumen, proyek, versi (1.0), tanggal, status (Draft), penyusun.

- [ ] **3.2.** Tulis **Riwayat Perubahan Dokumen** (tabel versi).

- [ ] **3.3.** Tulis **Bab 1 — Informasi Dokumen**:
  - [ ] 3.3.1. Tujuan dokumen: jelaskan bahwa dokumen ini adalah cetak biru keamanan komprehensif untuk sistem AbuCom.
  - [ ] 3.3.2. Cakupan: daftar aspek keamanan yang dicakup (otentikasi, otorisasi, proteksi data, audit, operasional).
  - [ ] 3.3.3. Posisi dalam SDLC: dokumen ke-6 pada Fase 03 Design, setelah BOM & HPP Design dan sebelum Implementation.
  - [ ] 3.3.4. Hubungan dokumen: input (ACM, System Arch, SRS, TSD, DB Schema, ERD) dan output (Implementation, Test Plan).
  - [ ] 3.3.5. Audiens target: Tim pengembang AI, Junior Programmer, Pemilik Usaha.
  - [ ] 3.3.6. Definisi dan akronim: daftar semua istilah keamanan yang digunakan.

- [ ] **3.4.** Tulis **Bab 2 — Prinsip dan Strategi Keamanan Sistem**:
  - [ ] 3.4.1. Tulis 6 prinsip keamanan utama beserta penjelasan dan contoh penerapan di AbuCom.
  - [ ] 3.4.2. Tulis model ancaman (*Threat Model*) spesifik untuk toko percetakan CLI LAN lokal — identifikasi minimal 8 ancaman potensial.
  - [ ] 3.4.3. Tulis klasifikasi tingkat sensitivitas data (3 kategori) dengan daftar tabel per kategori.

- [ ] **3.5.** Tulis **Bab 3 — Arsitektur Keamanan**:
  - [ ] 3.5.1. Buat diagram Mermaid keamanan berlapis Defense in Depth (adaptasi dari System Architecture Bab 7.1).
  - [ ] 3.5.2. Tulis detail keamanan jaringan fisik.
  - [ ] 3.5.3. Tulis detail hardening OS.
  - [ ] 3.5.4. Tulis detail keamanan koneksi database.

- [ ] **3.6.** Tulis **Bab 4 — Desain Otentikasi**:
  - [ ] 3.6.1. Tulis detail bcrypt cost 12 dengan pseudocode FP Python.
  - [ ] 3.6.2. Tulis detail JWT HS256 dengan pseudocode FP Python.
  - [ ] 3.6.3. Tulis detail rate limiting dengan pseudocode FP Python.
  - [ ] 3.6.4. Buat diagram sequence Mermaid alur login lengkap.
  - [ ] 3.6.5. Tulis prosedur logout dan penghancuran session.

- [ ] **3.7.** Tulis **Bab 5 — Desain Otorisasi**:
  - [ ] 3.7.1. Tulis model RBAC multi-level dengan diagram Mermaid hierarki peran.
  - [ ] 3.7.2. Tulis pseudocode FP implementasi decorator/guard otorisasi.
  - [ ] 3.7.3. Tulis tabel matriks akses ringkasan 10 modul × 8 peran.
  - [ ] 3.7.4. Tulis detail 4 aturan eskalasi otorisasi Pemilik.
  - [ ] 3.7.5. Tulis detail 3 aturan otorisasi Kepala Percetakan.
  - [ ] 3.7.6. Tulis kebijakan Default Deny dan implementasinya.

- [ ] **3.8.** Tulis **Bab 6 — Desain Proteksi Data**:
  - [ ] 3.8.1. Tulis detail enkripsi at rest (AES-256, bcrypt, enkripsi WhatsApp).
  - [ ] 3.8.2. Tulis detail proteksi in transit (LAN, port 3306, firewall).
  - [ ] 3.8.3. Tulis detail kepatuhan UU PDP No. 27/2022.
  - [ ] 3.8.4. Tulis detail proteksi input (sanitasi, parameterized queries, validation).
  - [ ] 3.8.5. Tulis detail manajemen kredensial (.env, .gitignore, JWT secret).
  - [ ] 3.8.6. Tulis tabel klasifikasi dan perlindungan per tabel database.

- [ ] **3.9.** Tulis **Bab 7 — Desain Audit Trail dan Monitoring**:
  - [ ] 3.9.1. Tulis skema lengkap tabel `audit_logs`.
  - [ ] 3.9.2. Tulis daftar event pemicu pencatatan audit.
  - [ ] 3.9.3. Tulis contoh format JSON untuk setiap tipe action.
  - [ ] 3.9.4. Tulis detail mekanisme fraud detection.
  - [ ] 3.9.5. Tulis kebijakan retensi dan pemeliharaan log.

- [ ] **3.10.** Tulis **Bab 8 — Desain Keamanan Operasional**:
  - [ ] 3.10.1. Tulis prosedur shift handover security.
  - [ ] 3.10.2. Tulis prosedur backup dan restore aman.
  - [ ] 3.10.3. Tulis prosedur pengelolaan akun pengguna.
  - [ ] 3.10.4. Tulis keamanan fisik server dan infrastruktur.

- [ ] **3.11.** Tulis **Bab 9 — Alur Keamanan Kritis**:
  - [ ] 3.11.1. Buat diagram sequence Mermaid alur otentikasi login CLI.
  - [ ] 3.11.2. Buat diagram sequence Mermaid alur otorisasi transaksi kasir.
  - [ ] 3.11.3. Buat diagram sequence Mermaid alur eskalasi retur/pembatalan.
  - [ ] 3.11.4. Buat diagram sequence Mermaid alur rekonsiliasi kas & shift handover.
  - [ ] 3.11.5. Buat flowchart Mermaid alur stock opname dengan otorisasi supervisor.
  - [ ] 3.11.6. Buat flowchart Mermaid alur backup dan restore database.

- [ ] **3.12.** Tulis **Bab 10 — Penanganan Error dan Kode Keamanan**:
  - [ ] 3.12.1. Tulis tabel kode error ERR-AUTH-xxx (dari SRS dan ACM).
  - [ ] 3.12.2. Tulis tabel kode error ERR-SESSION-xxx.
  - [ ] 3.12.3. Tulis tabel kode error ERR-DB-xxx terkait keamanan.
  - [ ] 3.12.4. Tulis tabel kode error ERR-FILE-xxx.
  - [ ] 3.12.5. Tulis tabel kode error ERR-CASH-xxx.
  - [ ] 3.12.6. Tulis prosedur respon insiden keamanan.

- [ ] **3.13.** Tulis **Bab 11 — Analisis Risiko Keamanan**:
  - [ ] 3.13.1. Tulis matriks risiko keamanan (minimal 10 risiko) dengan format: ID, Komponen, Deskripsi Ancaman, Probabilitas (1-5), Dampak (1-5), Skor, Rencana Mitigasi.
  - [ ] 3.13.2. Tulis rencana mitigasi per risiko.
  - [ ] 3.13.3. Tulis kriteria evaluasi ulang keamanan.

- [ ] **3.14.** Tulis **Bab 12 — Spesifikasi Implementasi Teknis Keamanan**:
  - [ ] 3.14.1. Tulis penempatan modul keamanan (middleware/rbac.py, middleware/logger.py, dll.).
  - [ ] 3.14.2. Tulis pseudocode FP murni untuk fungsi-fungsi keamanan inti.
  - [ ] 3.14.3. Tulis konfigurasi `.env` (parameter keamanan).
  - [ ] 3.14.4. Tulis konfigurasi server dan firewall.

- [ ] **3.15.** Tulis **Bab 13 — Matriks Ketertelusuran Keamanan**:
  - [ ] 3.15.1. Buat tabel mapping Security Design → SRS (SRS-F-030 s.d SRS-F-035, SRS-F-039).
  - [ ] 3.15.2. Buat tabel mapping Security Design → ACM Entry ID.
  - [ ] 3.15.3. Buat tabel mapping Security Design → Tech Stack Decision.
  - [ ] 3.15.4. Buat tabel mapping Security Design → Use Case (UC-032 s.d UC-037, UC-041 s.d UC-044).

- [ ] **3.16.** Tulis **Bab 14 — Persetujuan dan Otorisasi**:
  - [ ] 3.16.1. Buat tabel persetujuan formal (Pemilik Usaha dan Arsitek Keamanan).

- [ ] **3.17.** Tulis **Bab 15 — Glosarium Istilah Keamanan**:
  - [ ] 3.17.1. Daftar minimal 15 istilah keamanan dengan definisi bahasa Indonesia yang jelas.

- [ ] **3.18.** Tulis **Bab 16 — Referensi Dokumen**:
  - [ ] 3.18.1. Buat tabel berisi semua file referensi yang digunakan (sesuai Bagian 2 issue ini) dengan kolom: No, Nama Berkas Referensi, Lokasi Path Relatif, Keterangan Versi.

### Tahap 4 — Validasi dan Finalisasi

- [ ] **4.1.** Periksa kembali seluruh isi dokumen terhadap kelengkapan kerangka Bab 1–16.
- [ ] **4.2.** Pastikan semua data yang diambil dari file referensi akurat dan sesuai — periksa setiap angka, kode error, nama kolom, dan parameter konfigurasi.
- [ ] **4.3.** Pastikan semua diagram Mermaid menggunakan sintaks yang benar dan dapat di-render.
- [ ] **4.4.** Pastikan semua pseudocode Python menggunakan paradigma FP murni (tanpa class, tanpa mutasi global).
- [ ] **4.5.** Pastikan setiap data yang tidak ditemukan di referensi ditandai dengan `**[DATA BELUM TERSEDIA — PERLU DIISI MANUAL]**`.
- [ ] **4.6.** Pastikan bahasa Indonesia yang digunakan natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau AI model lain.
- [ ] **4.7.** Pastikan dokumen tidak memiliki duplikasi informasi antar-bab yang tidak perlu.
- [ ] **4.8.** Pastikan tabel matriks ketertelusuran (Bab 13) meng-cover semua kebutuhan keamanan dari SRS, ACM, dan Tech Stack Decision.

### Tahap 5 — Penulisan ke Target File

- [ ] **5.1.** Tuangkan seluruh hasil pengerjaan dokumen Security Design ke dalam target file: `docs/sdlc/03_design/06_security_design.md`.
- [ ] **5.2.** Pastikan file ditulis dengan encoding UTF-8.
- [ ] **5.3.** Pastikan format markdown benar dan konsisten dengan dokumen SDLC lainnya dalam proyek.

---

## 5. Instruksi Tambahan Spesifik untuk Dokumen Security Design

Berikut adalah instruksi tambahan yang khas dan relevan untuk ciri khas dokumen Security Design:

- [ ] **5.1. Threat Modeling**: Dokumen ini **WAJIB** menyertakan analisis model ancaman (*Threat Model*) yang spesifik untuk konteks operasional AbuCom sebagai toko percetakan UMKM dengan LAN lokal offline. Threat model harus mencakup: fraud internal karyawan, brute-force login terminal fisik, SQL injection lokal, pencurian fisik server Mini PC, kebocoran data pelanggan via flashdisk staf, manipulasi stok gudang, pemalsuan session JWT, dan akses tidak sah ke terminal kasir yang ditinggalkan.

- [ ] **5.2. Pseudocode Keamanan FP**: Setiap mekanisme keamanan teknis (hashing, JWT generation/validation, RBAC check, audit logging, input sanitization) **WAJIB** disertai pseudocode implementasi Python yang mengikuti paradigma Functional Programming murni — tanpa class, tanpa mutasi state global, menggunakan namedtuple untuk data imutabel dan Result pattern untuk error handling.

- [ ] **5.3. Diagram Keamanan**: Dokumen ini **WAJIB** menyertakan minimal 6 diagram Mermaid yang menggambarkan alur keamanan kritis. Diagram harus memperlihatkan titik-titik pemeriksaan otorisasi (RBAC guard), pencatatan audit, dan penanganan kegagalan secara visual.

- [ ] **5.4. Kepatuhan Regulasi**: Setiap bagian yang berkaitan dengan proteksi data pribadi pelanggan **WAJIB** merujuk secara eksplisit pada **UU PDP No. 27 Tahun 2022** dan menjelaskan bagaimana sistem AbuCom mematuhi regulasi tersebut.

- [ ] **5.5. Konsistensi Kode Error**: Semua kode error keamanan yang tercantum dalam dokumen **WAJIB** konsisten dan sinkron 100% dengan kode error yang sudah didefinisikan di SRS v1.1 dan ACM v1.1. Jangan membuat kode error baru yang bertentangan.

- [ ] **5.6. Konsistensi Parameter Teknis**: Semua parameter teknis keamanan (bcrypt cost factor, JWT expiry, rate limit count, lockout duration, secret key length, backup encryption algorithm) **WAJIB** konsisten dengan nilai yang sudah ditetapkan di Tech Stack Decision v1.1 dan System Architecture v1.1.

- [ ] **5.7. Kelayakan sebagai Input Fase Selanjutnya**: Pastikan isi dokumen ini cukup detail dan lengkap untuk dijadikan referensi, acuan, dan input utama bagi:
  - Fase 04 Implementation — khususnya penulisan modul `middleware/rbac.py`, `middleware/logger.py`, dan `utils/backup.py`.
  - Fase 05 Testing — khususnya pembuatan test suite penetration testing RBAC dan security audit.

- [ ] **5.8. Tidak Membingungkan**: Pastikan setiap instruksi keamanan ditulis secara eksplisit dan tidak ambigu. Gunakan contoh konkret jika diperlukan. Misalnya, jangan hanya menulis "enkripsi data sensitif", tetapi tulis "nomor WhatsApp pelanggan di kolom `whatsapp` tabel `pelanggan` dienkripsi menggunakan algoritma enkripsi simetris reversible di sisi Python sebelum disimpan ke database MySQL".

---

## 6. Ringkasan Deliverable

| No | Deliverable | Target | Status |
|----|------------|--------|--------|
| 1 | Dokumen Security Design lengkap (16 bab) | `docs/sdlc/03_design/06_security_design.md` | `[ ]` Belum Dikerjakan |
| 2 | Minimal 6 diagram Mermaid keamanan | Di dalam dokumen | `[ ]` Belum Dikerjakan |
| 3 | Pseudocode FP fungsi keamanan | Di dalam dokumen | `[ ]` Belum Dikerjakan |
| 4 | Matriks ketertelusuran keamanan | Di dalam dokumen | `[ ]` Belum Dikerjakan |
| 5 | Matriks risiko keamanan | Di dalam dokumen | `[ ]` Belum Dikerjakan |
| 6 | Referensi dokumen lengkap | Di dalam dokumen | `[ ]` Belum Dikerjakan |

---