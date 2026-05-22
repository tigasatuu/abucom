---
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
target     : docs/sdlc/01_planning/04_tech_stack_decision.md
prioritas  : High
status     : Open
tanggal    : 2026-05-22
---

# Pembuatan dan Penyusunan Dokumen Tech Stack Decision

## 1. Ringkasan Issue

Issue ini berisi instruksi perencanaan low-level yang sangat detail untuk pembuatan dan penyusunan dokumen **Tech Stack Decision** proyek AbuCom. Dokumen ini merupakan dokumen ke-4 pada fase *Planning* dalam siklus SDLC yang mendokumentasikan secara formal seluruh keputusan pemilihan teknologi, justifikasi teknis di balik setiap pilihan, evaluasi alternatif yang dipertimbangkan, serta analisis risiko dan strategi mitigasi dari setiap komponen teknologi yang dipilih.

**Tujuan Dokumen Utama**: Menyediakan satu sumber kebenaran (*Single Source of Truth*) yang otoritatif mengenai seluruh keputusan arsitektur teknologi proyek AbuCom, sehingga seluruh anggota tim pengembang (manusia maupun AI) memiliki acuan yang seragam dan tidak ambigu saat memasuki fase SDLC berikutnya (Requirements, Design, dan Implementation).

---

## 2. Persona Pelaksana (Penyusun Dokumen)

**Persona yang ditugaskan**: **Senior Technical Architect & Technology Evaluation Specialist**

**Justifikasi pemilihan persona**:
- Dokumen Tech Stack Decision adalah dokumen keputusan arsitektur teknologi yang membutuhkan keahlian evaluasi komparatif terhadap berbagai teknologi, pemahaman mendalam tentang kelebihan dan kekurangan setiap komponen teknis, serta kemampuan memberikan justifikasi teknis yang kuat dan terukur.
- Persona ini memiliki otoritas dan kapabilitas untuk memberikan rekomendasi teknologi yang bersifat mengikat (*binding*) bagi seluruh fase SDLC berikutnya.
- Persona ini mampu mengevaluasi aspek kinerja, keamanan, portabilitas, skalabilitas, dan kompatibilitas setiap komponen tech stack secara objektif.

---

## 3. File Referensi yang Digunakan

Berikut adalah file referensi yang **wajib dibaca dan dirangkum** sebelum memulai penyusunan dokumen utama. File-file ini dipilih berdasarkan relevansi data yang dibutuhkan oleh dokumen Tech Stack Decision:

| # | File Referensi | Lokasi Path Relatif | Prioritas | Alasan Pemilihan |
|---|---|---|---|---|
| 1 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | **Primer (Utama)** | Sumber data utama yang berisi keputusan teknologi inti (Python 3.14.2+, MySQL, paradigma FP, pustaka utama, platform OS, tipe antarmuka CLI), ruang lingkup modul fungsional, kebutuhan non-fungsional (keamanan, portabilitas, kecepatan), dan tim pengembang AI. |
| 2 | `02_feasibility_study.md` | `docs/sdlc/01_planning/02_feasibility_study.md` | **Primer (Utama)** | Sumber data evaluasi teknis mendalam per komponen teknologi (Python FP, MySQL, pustaka, CLI, infrastruktur), evaluasi kompleksitas fitur, risiko teknis dan mitigasinya, serta analisis alternatif solusi (Excel vs SaaS vs Kustom CLI). |
| 3 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | **Sekunder** | Data profil tim pengembang AI (spesialisasi teknis per model), hak akses RBAC yang mempengaruhi kebutuhan keamanan teknologi, dan pemetaan modul vs stakeholder. |
| 4 | `narasi.txt` | `docs/sdlc/narasi.txt` | **Pendukung** | Konteks teknis dasar dari pemilik usaha: spesifikasi Python, paradigma FP, pustaka utama, target OS, dan susunan tim AI. Masih dibutuhkan sebagai sumber data asli yang belum terolah. |

---

## 4. Kerangka Struktur Dokumen Utama

Berikut adalah kerangka struktur dokumen `04_tech_stack_decision.md` yang **wajib diikuti**. Kerangka ini disusun berdasarkan standar praktik industri dokumen *Technology Decision Record* / *Architecture Decision Record* (ADR) yang disesuaikan dengan konteks proyek AbuCom:

```
---
dokumen    : Tech Stack Decision
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [DIISI TANGGAL PENGERJAAN]
status     : Draft
penyusun   : Senior Technical Architect & Technology Evaluation Specialist
---

# Tech Stack Decision — AbuCom

## Riwayat Perubahan Dokumen
(Tabel: Versi, Tanggal, Perubahan, Oleh)

---

## 1. Informasi Dokumen
- Tujuan penyusunan dokumen ini
- Hubungan dan posisi dokumen ini terhadap dokumen SDLC lainnya
- Cakupan keputusan teknologi yang didokumentasikan

### 1.1. Ringkasan Eksekutif (Executive Summary)
- Ikhtisar seluruh keputusan tech stack yang diambil dalam 1-2 paragraf padat
- Daftar ringkas seluruh komponen teknologi yang dipilih

---

## 2. Konteks dan Latar Belakang Keputusan Teknologi
- Konteks bisnis yang mempengaruhi pemilihan teknologi
- Batasan dan constraint utama yang membatasi opsi teknologi
- Prinsip-prinsip arsitektur yang menjadi panduan pemilihan

### 2.1. Batasan Teknologi dari Pemilik Proyek (Mandatory Constraints)
- Daftar teknologi yang WAJIB digunakan (non-negotiable) sesuai arahan pemilik
- Paradigma pemrograman yang diwajibkan
- Versi minimum runtime yang diwajibkan

### 2.2. Prinsip Arsitektur Panduan (Guiding Architecture Principles)
- Prinsip-prinsip teknis yang memandu seluruh keputusan (misal: portabilitas, keamanan, modularitas, skalabilitas, FP murni)

---

## 3. Keputusan Tech Stack — Bahasa Pemrograman

### 3.1. Keputusan: Python 3.14.2+
- Status keputusan (Disetujui/Ditolak)
- Justifikasi pemilihan secara detail
- Versi spesifik dan alasan pemilihan versi
- Kelebihan teknis untuk konteks proyek AbuCom
- Keterbatasan dan tantangan yang teridentifikasi
- Risiko teknis dan rencana mitigasi

### 3.2. Keputusan: Paradigma Functional Programming (FP) Murni
- Status keputusan
- Justifikasi pemilihan paradigma FP di atas OOP
- Dampak paradigma FP terhadap arsitektur kode
- Modul dan pustaka Python pendukung FP (functools, operator, itertools, dll.)
- Strategi pengelolaan state management tanpa OOP
- Risiko teknis dan rencana mitigasi

### 3.3. Alternatif yang Dipertimbangkan dan Ditolak
- Tabel perbandingan bahasa alternatif (misal: Go, Node.js, Java) — alasan penolakan

---

## 4. Keputusan Tech Stack — Sistem Basis Data

### 4.1. Keputusan: MySQL Community Server
- Status keputusan
- Justifikasi pemilihan MySQL
- Versi yang direkomendasikan
- Kelebihan teknis (ACID, relasional, kinerja, gratis, skalabilitas)
- Konfigurasi kunci yang direkomendasikan (charset, collation, engine, isolation level)
- Strategi desain Multi-Branch Ready pada skema database
- Risiko teknis dan rencana mitigasi

### 4.2. Alternatif yang Dipertimbangkan dan Ditolak
- Tabel perbandingan database alternatif (misal: PostgreSQL, SQLite, MariaDB) — alasan penolakan

---

## 5. Keputusan Tech Stack — Pustaka dan Dependensi Utama

### 5.1. Keputusan: mysql-connector-python
- Justifikasi, versi, lisensi, alternatif yang ditolak

### 5.2. Keputusan: python-dotenv
- Justifikasi, versi, lisensi, alternatif yang ditolak

### 5.3. Keputusan: bcrypt
- Justifikasi, versi, lisensi, konteks keamanan enkripsi sandi
- Perbandingan dengan alternatif hashing (argon2, scrypt, pbkdf2)

### 5.4. Keputusan: PyJWT
- Justifikasi, versi, lisensi, konteks autentikasi session CLI
- Konfigurasi algoritma JWT yang direkomendasikan (HS256/RS256)
- Strategi pengelolaan token (expiry, refresh, revocation)

### 5.5. Pustaka Standar Python yang Dimanfaatkan
- Daftar modul bawaan Python yang direncanakan (decimal, functools, itertools, operator, hashlib, os, pathlib, json, csv, datetime, typing, dll.)
- Justifikasi penggunaan masing-masing modul

### 5.6. Evaluasi Pustaka Tambahan yang Direkomendasikan [REKOMENDASI]
- Pustaka potensial yang direkomendasikan tim AI untuk dipertimbangkan (misal: rich/colorama untuk warna CLI, tabulate untuk tabel CLI, click/typer untuk CLI framework)
- Justifikasi dan analisis manfaat vs risiko

### 5.7. Ringkasan Matriks Dependensi
- Tabel ringkasan seluruh pustaka: nama, versi, lisensi, fungsi utama, status keputusan

---

## 6. Keputusan Tech Stack — Platform dan Sistem Operasi

### 6.1. Keputusan: Dual-OS (Linux Debian 12 Bookworm & Windows 11)
- Justifikasi dukungan dual-OS
- Peran masing-masing OS dalam arsitektur (Server vs Client)
- Strategi portabilitas kode Python lintas OS
- Perbedaan perilaku yang harus diantisipasi (path separator, encoding, terminal)

### 6.2. Keputusan: Arsitektur Client-Server Lokal (LAN)
- Topologi jaringan yang dipilih
- Spesifikasi hardware server dan client
- Strategi konektivitas (UTP Cat6, Switch, Router)

### 6.3. Alternatif yang Dipertimbangkan dan Ditolak
- Cloud-hosted vs Lokal — alasan penolakan hosting cloud

---

## 7. Keputusan Tech Stack — Antarmuka Pengguna

### 7.1. Keputusan: Command Line Interface (CLI) Berbasis Teks
- Justifikasi pemilihan CLI di atas GUI/Web
- Kelebihan CLI untuk konteks operasional AbuCom (kecepatan, ringan, hotkey)
- Keterbatasan CLI (estetika, learning curve)
- Strategi peningkatan UX CLI (kode warna ANSI, tabel terformat, menu navigasi konsisten)
- Risiko teknis dan rencana mitigasi

### 7.2. Alternatif yang Dipertimbangkan dan Ditolak
- GUI Desktop (Tkinter/PyQt) — alasan penolakan
- Web Interface (Flask/Django) — alasan penolakan

---

## 8. Keputusan Tech Stack — Keamanan dan Autentikasi

### 8.1. Strategi Enkripsi Kata Sandi (bcrypt)
- Konfigurasi cost factor yang direkomendasikan
- Alur proses hashing dan verifikasi

### 8.2. Strategi Autentikasi Session (JWT)
- Algoritma signing yang dipilih
- Strategi token lifecycle (pembuatan, validasi, expiry, invalidasi)
- Penanganan session di lingkungan CLI

### 8.3. Strategi Hak Akses (RBAC)
- Arsitektur RBAC tingkat tinggi
- Daftar role yang dirancang dan hubungannya dengan teknologi

### 8.4. Strategi Audit Trail
- Teknologi pencatatan log audit (tabel MySQL)
- Format data yang dicatat

### 8.5. Strategi Perlindungan Data (UU PDP)
- Enkripsi backup database (AES-256)
- Pembatasan akses direktori server

---

## 9. Keputusan Tech Stack — Infrastruktur Pengembangan

### 9.1. Alat Pengembangan dan Kolaborasi
- Editor/IDE yang digunakan
- Version Control System (Git)
- Strategi branching dan code review

### 9.2. Tim Pengembang dan Pembagian Teknologi per Anggota
- Tabel pemetaan anggota tim AI terhadap komponen teknologi yang menjadi tanggung jawabnya

### 9.3. Metodologi Pengembangan
- Pendekatan Hybrid (Waterfall & Agile) dalam konteks keputusan teknologi

---

## 10. Matriks Ringkasan Tech Stack Decision

Tabel ringkasan seluruh keputusan teknologi dalam satu halaman:

| # | Komponen | Teknologi Dipilih | Versi | Lisensi | Status | Justifikasi Utama |
|---|---|---|---|---|---|---|

---

## 11. Analisis Risiko Teknis Terintegrasi

Tabel konsolidasi seluruh risiko teknis dari setiap komponen teknologi:

| # | Komponen Teknologi | Risiko | Probabilitas | Dampak | Mitigasi |
|---|---|---|---|---|---|

---

## 12. Kompatibilitas Tech Stack dengan Modul Fungsional

Matriks pemetaan komponen tech stack terhadap 9 modul fungsional AbuCom:

| Komponen Tech Stack | M.1 | M.2 | M.3 | M.4 | M.5 | M.6 | M.7 | M.8 | M.9 |
|---|---|---|---|---|---|---|---|---|---|

---

## 13. Kriteria Evaluasi Ulang (Technology Re-evaluation Triggers)
- Kondisi yang memicu peninjauan ulang keputusan teknologi
- Proses eskalasi jika ditemukan ketidakcocokan di fase SDLC selanjutnya

---

## 14. Persetujuan dan Otorisasi

Tabel persetujuan dokumen.

---

## 15. Glosarium

Penjelasan istilah teknis yang digunakan dalam dokumen ini.

---

## 16. Referensi Dokumen

Tabel file referensi yang digunakan dalam penyusunan dokumen ini.
```

---

## 5. Instruksi Pelaksanaan — Tahapan Detail (Low-Level Checklist)

### Fase A: Persiapan dan Pembacaan File Referensi

- [ ] **A.1.** Baca dan pahami seluruh isi file `docs/sdlc/narasi.txt` (115 baris). Fokus pada bagian:
  - [ ] A.1.1. Bagian "Kebutuhan Teknis dan Tim" (baris 100-115): Catat spesifikasi sistem (Python 3.14.2+, paradigma FP, pustaka utama, OS target, antarmuka CLI).
  - [ ] A.1.2. Bagian "Susunan Tim Pengembang" (baris 108-115): Catat daftar lengkap anggota tim AI dan spesialisasinya.
  - [ ] A.1.3. Buat rangkuman tertulis dari data yang relevan untuk Tech Stack Decision.

- [ ] **A.2.** Baca dan pahami seluruh isi file `docs/sdlc/01_planning/01_project_charter.md` (449 baris). Fokus pada bagian:
  - [ ] A.2.1. Bagian 1.2 "Deskripsi Singkat Proyek" (baris 27-28): Catat deskripsi teknologi yang digunakan.
  - [ ] A.2.2. Bagian 4.1.2 "Platform & Teknologi" (baris 146-151): Catat seluruh spesifikasi platform dan teknologi yang dipilih secara verbatim.
  - [ ] A.2.3. Bagian 7.1 "Susunan Tim Pengembang" (baris 219-231): Catat tabel lengkap 7 anggota tim dan spesialisasi mereka.
  - [ ] A.2.4. Bagian 8.1 "Kebutuhan Fungsional Utama" (baris 246-288): Rangkum kebutuhan fungsional yang berdampak pada pilihan teknologi (BOM desimal, RBAC, Audit Trail, multi-skema harga, rekonsiliasi).
  - [ ] A.2.5. Bagian 8.2 "Kebutuhan Non-Fungsional Utama" (baris 289-296): Catat seluruh kebutuhan non-fungsional yang secara langsung mempengaruhi keputusan teknologi (keamanan bcrypt/JWT, RBAC, FP murni, portabilitas OS, kecepatan <5 detik).
  - [ ] A.2.6. Bagian 8.3 "Rekomendasi Inovasi & Best Practice" (baris 297-302): Catat rekomendasi teknologi tambahan (backup otomatis, WA template link, prediksi re-order).
  - [ ] A.2.7. Bagian 9 "Asumsi dan Batasan" (baris 305-333): Catat batasan teknologi yang rigid (CLI, FP murni, Python 3.14.2+, MySQL).
  - [ ] A.2.8. Bagian 10 "Risiko Awal" (baris 336-348): Catat risiko teknis yang berhubungan dengan teknologi (rekursi FP, migrasi data, paradigma FP).
  - [ ] A.2.9. Bagian 12 "Estimasi Anggaran" (baris 368-388): Catat komponen biaya infrastruktur teknis (Mini PC Server, jaringan, UPS).
  - [ ] A.2.10. Buat rangkuman tertulis dari data yang relevan untuk Tech Stack Decision.

- [ ] **A.3.** Baca dan pahami seluruh isi file `docs/sdlc/01_planning/02_feasibility_study.md` (552 baris). Fokus pada bagian:
  - [ ] A.3.1. Bagian 4.1 "Evaluasi Teknologi yang Dipilih" (baris 78-100): Catat seluruh evaluasi per komponen teknologi (Python/FP, MySQL, pustaka, platform, CLI) beserta penilaian kelayakannya.
  - [ ] A.3.2. Bagian 4.2 "Evaluasi Kompleksitas Fitur Utama" (baris 102-138): Catat evaluasi teknis per modul fungsional dan hubungannya dengan teknologi.
  - [ ] A.3.3. Bagian 4.3 "Evaluasi Kapabilitas Tim Pengembang" (baris 140-143): Catat penilaian risiko integrasi kode dari multi-AI.
  - [ ] A.3.4. Bagian 4.4 "Evaluasi Infrastruktur Teknis" (baris 145-150): Catat spesifikasi hardware server dan jaringan.
  - [ ] A.3.5. Bagian 4.5 "Risiko Teknis dan Mitigasi" (baris 152-158): Catat tabel risiko teknis (memory leak, database corrupt, pembulatan desimal).
  - [ ] A.3.6. Bagian 9 "Analisis Alternatif Solusi" (baris 423-469): Catat perbandingan alternatif (Excel vs SaaS vs Kustom CLI Python) dan matriks skor perbandingan.
  - [ ] A.3.7. Buat rangkuman tertulis dari data yang relevan untuk Tech Stack Decision.

- [ ] **A.4.** Baca dan pahami bagian relevan dari file `docs/sdlc/01_planning/03_stakeholder_register.md` (980 baris). Fokus pada bagian:
  - [ ] A.4.1. Bagian 3.9 sampai 3.14 "Profil Tim AI" (baris 330-490): Catat spesialisasi teknis setiap model AI dan platform/API yang digunakan.
  - [ ] A.4.2. Bagian 6.2 "Matriks Pemetaan Modul vs Stakeholder" (baris 805-844): Catat pemetaan modul untuk memahami cakupan teknologi.
  - [ ] A.4.3. Buat rangkuman tertulis dari data yang relevan untuk Tech Stack Decision.

- [ ] **A.5.** Verifikasi kelengkapan rangkuman. Pastikan seluruh data berikut sudah terangkum:
  - [ ] A.5.1. Bahasa pemrograman yang dipilih dan versinya.
  - [ ] A.5.2. Paradigma pemrograman yang diwajibkan.
  - [ ] A.5.3. Sistem database yang dipilih.
  - [ ] A.5.4. Daftar lengkap 4 pustaka utama (nama, fungsi).
  - [ ] A.5.5. Platform OS target (Linux dan Windows).
  - [ ] A.5.6. Tipe antarmuka yang dipilih (CLI).
  - [ ] A.5.7. Spesifikasi hardware infrastruktur (Mini PC, PC Kasir, UPS, jaringan).
  - [ ] A.5.8. Arsitektur topologi (Client-Server LAN).
  - [ ] A.5.9. Komponen keamanan (bcrypt, JWT, RBAC, Audit Trail, enkripsi backup).
  - [ ] A.5.10. Susunan dan spesialisasi tim pengembang AI.
  - [ ] A.5.11. Evaluasi kelayakan teknis per komponen dari Feasibility Study.
  - [ ] A.5.12. Risiko teknis dan rencana mitigasi.
  - [ ] A.5.13. Analisis alternatif yang ditolak dan justifikasinya.
  - [ ] A.5.14. Kebutuhan non-fungsional yang mempengaruhi pemilihan teknologi.

---

### Fase B: Penyusunan Dokumen Utama

- [ ] **B.1.** Buat file baru di lokasi `docs/sdlc/01_planning/04_tech_stack_decision.md`.

- [ ] **B.2.** Tulis bagian **Front Matter (Header YAML)** menggunakan format berikut:
  ```yaml
  ---
  dokumen    : Tech Stack Decision
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [ISI DENGAN TANGGAL PENGERJAAN FORMAT YYYY-MM-DD]
  status     : Draft
  penyusun   : Senior Technical Architect & Technology Evaluation Specialist
  ---
  ```

- [ ] **B.3.** Tulis bagian **Riwayat Perubahan Dokumen**:
  - [ ] B.3.1. Buat tabel riwayat versi dengan kolom: Versi, Tanggal, Perubahan, Oleh.
  - [ ] B.3.2. Isi baris pertama dengan versi 1.0, tanggal pengerjaan, deskripsi "Pembuatan awal dokumen", dan nama persona penyusun.

- [ ] **B.4.** Tulis bagian **1. Informasi Dokumen**:
  - [ ] B.4.1. Jelaskan tujuan dokumen ini secara formal (mendokumentasikan keputusan teknologi proyek).
  - [ ] B.4.2. Jelaskan hubungan dokumen ini dengan dokumen SDLC lain (Project Charter, Feasibility Study, Stakeholder Register, SRS, SDD).
  - [ ] B.4.3. Jelaskan cakupan keputusan teknologi yang tercakup dalam dokumen ini.
  - [ ] B.4.4. Tulis sub-bagian **1.1. Ringkasan Eksekutif**: Rangkum seluruh keputusan tech stack dalam 1-2 paragraf padat dan sebuah daftar ringkas komponen teknologi.

- [ ] **B.5.** Tulis bagian **2. Konteks dan Latar Belakang Keputusan Teknologi**:
  - [ ] B.5.1. Jelaskan konteks bisnis AbuCom yang mempengaruhi pemilihan teknologi (UMKM percetakan, single-fighter, burnout, 5 divisi usaha, pencatatan manual Excel).
  - [ ] B.5.2. Tulis sub-bagian **2.1. Batasan Teknologi dari Pemilik Proyek (Mandatory Constraints)**:
    - [ ] Daftar: Python 3.14.2+ (wajib), Paradigma FP murni (wajib), MySQL (wajib), 4 pustaka utama (wajib), CLI (wajib), Dual-OS Linux Debian 12 & Windows 11 (wajib).
    - [ ] Tandai setiap item sebagai `[MANDATORY — Non-Negotiable]`.
  - [ ] B.5.3. Tulis sub-bagian **2.2. Prinsip Arsitektur Panduan**:
    - [ ] Daftar prinsip: Portabilitas lintas OS, Keamanan data maksimal, Modularitas FP, Skalabilitas multi-cabang, Kinerja <5 detik, Imutabilitas data, Presisi desimal.

- [ ] **B.6.** Tulis bagian **3. Keputusan Tech Stack — Bahasa Pemrograman**:
  - [ ] B.6.1. Tulis **3.1. Keputusan: Python 3.14.2+**: Status Disetujui, justifikasi lengkap (ekosistem matang, pustaka standar melimpah, portabilitas tinggi, dukungan FP). Ambil data dari Feasibility Study bagian 4.1.1 dan Project Charter bagian 4.1.2. Tuliskan versi spesifik dan alasan versi minimum. Tuliskan kelebihan, keterbatasan, risiko, dan mitigasi.
  - [ ] B.6.2. Tulis **3.2. Keputusan: Paradigma Functional Programming (FP) Murni**: Status Disetujui, justifikasi (keamanan, testabilitas, eliminasi side-effects). Ambil data dari Feasibility Study bagian 4.1.1. Jelaskan dampak terhadap arsitektur kode, modul Python pendukung FP (functools, operator, itertools, typing), strategi state management tanpa OOP (nested closures, imutable data structures, monad-like patterns), risiko dan mitigasi (learning curve, bantuan Claude Sonnet 4.6).
  - [ ] B.6.3. Tulis **3.3. Alternatif yang Dipertimbangkan dan Ditolak**: Buat tabel perbandingan minimal 3 bahasa alternatif (misal: Go, Node.js, Java/Kotlin). Berikan alasan penolakan yang spesifik dan objektif untuk masing-masing.

- [ ] **B.7.** Tulis bagian **4. Keputusan Tech Stack — Sistem Basis Data**:
  - [ ] B.7.1. Tulis **4.1. Keputusan: MySQL Community Server**: Status Disetujui, justifikasi (ACID compliance, relasional, gratis, industri-grade, stabil). Ambil data dari Feasibility Study bagian 4.1.2. Tuliskan versi yang direkomendasikan, kelebihan teknis, konfigurasi kunci (charset utf8mb4, collation utf8mb4_unicode_ci, engine InnoDB, isolation level REPEATABLE READ). Jelaskan strategi desain Multi-Branch Ready (kolom cabang_id). Tuliskan risiko dan mitigasi (corrupt data, mati listrik, UPS).
  - [ ] B.7.2. Tulis **4.2. Alternatif yang Dipertimbangkan dan Ditolak**: Buat tabel perbandingan minimal 3 database alternatif (PostgreSQL, SQLite, MariaDB). Berikan alasan penolakan yang spesifik.

- [ ] **B.8.** Tulis bagian **5. Keputusan Tech Stack — Pustaka dan Dependensi Utama**:
  - [ ] B.8.1. Tulis **5.1. Keputusan: mysql-connector-python**: Justifikasi (driver resmi Oracle, kompatibel MySQL), versi stabil terbaru, lisensi GPL, alternatif yang ditolak (PyMySQL, mysqlclient).
  - [ ] B.8.2. Tulis **5.2. Keputusan: python-dotenv**: Justifikasi (pemisahan kredensial dari kode sumber), versi, lisensi BSD, alternatif yang ditolak.
  - [ ] B.8.3. Tulis **5.3. Keputusan: bcrypt**: Justifikasi (enkripsi satu arah standar industri untuk kata sandi), versi, lisensi Apache 2.0, konteks keamanan (cost factor rekomendasi 12). Perbandingan dengan argon2, scrypt, pbkdf2 — alasan bcrypt dipilih (keseimbangan keamanan dan kecepatan verifikasi di hardware UMKM).
  - [ ] B.8.4. Tulis **5.4. Keputusan: PyJWT**: Justifikasi (autentikasi session CLI tanpa state server-side yang berat), versi, lisensi MIT, algoritma signing yang direkomendasikan (HS256 untuk single-server), strategi pengelolaan token (expiry 8 jam per shift kerja, invalidasi saat logout).
  - [ ] B.8.5. Tulis **5.5. Pustaka Standar Python yang Dimanfaatkan**: Daftar modul bawaan Python yang direncanakan:
    - `decimal` — presisi perhitungan HPP BOM dan stok desimal
    - `functools` — higher-order functions, partial, reduce
    - `itertools` — iterasi fungsional efisien
    - `operator` — operator fungsional
    - `hashlib` — fallback hashing jika diperlukan
    - `os` dan `pathlib` — portabilitas path lintas OS
    - `json` — serialisasi konfigurasi
    - `csv` — import data awal Excel/CSV
    - `datetime` — timestamp transaksi dan Audit Trail
    - `typing` — type hints untuk kejelasan FP
    - `getpass` — input kata sandi aman di terminal CLI
    - `textwrap` dan `shutil` — format tampilan CLI
  - [ ] B.8.6. Tulis **5.6. Evaluasi Pustaka Tambahan yang Direkomendasikan [REKOMENDASI]**: Evaluasi pustaka potensial seperti:
    - `rich` atau `colorama` — pewarnaan output CLI (ANSI codes)
    - `tabulate` atau `prettytable` — format tabel di terminal
    - `click` atau `typer` — framework CLI terstruktur
    - Untuk setiap pustaka, tuliskan: justifikasi, manfaat, risiko dependensi, dan rekomendasi (Direkomendasikan / Opsional / Ditolak).
  - [ ] B.8.7. Tulis **5.7. Ringkasan Matriks Dependensi**: Buat tabel ringkasan semua pustaka (wajib dan rekomendasi) dengan kolom: Nama, Versi, Lisensi, Fungsi Utama, Kategori (Wajib/Rekomendasi), Status Keputusan.

- [ ] **B.9.** Tulis bagian **6. Keputusan Tech Stack — Platform dan Sistem Operasi**:
  - [ ] B.9.1. Tulis **6.1. Keputusan: Dual-OS**: Justifikasi (Linux Debian 12 untuk server database, Windows 11 untuk PC Kasir/Operasional). Jelaskan peran masing-masing OS. Strategi portabilitas kode (gunakan os.path / pathlib, hindari hardcode path separator, gunakan encoding UTF-8 eksplisit). Daftar perbedaan perilaku lintas OS yang harus diantisipasi.
  - [ ] B.9.2. Tulis **6.2. Keputusan: Arsitektur Client-Server Lokal (LAN)**: Jelaskan topologi jaringan, spesifikasi hardware (Mini PC Server Core i5 16GB RAM SSD 512GB, PC Kasir, 2 UPS, Router MikroTik, Switch Hub 8-Port, UTP Cat6). Ambil data dari Project Charter bagian 12 dan Feasibility Study bagian 4.4.
  - [ ] B.9.3. Tulis **6.3. Alternatif yang Dipertimbangkan dan Ditolak**: Jelaskan mengapa hosting cloud (AWS/GCP/VPS) ditolak (kontrol data penuh, biaya langganan, ketergantungan internet, UU PDP).

- [ ] **B.10.** Tulis bagian **7. Keputusan Tech Stack — Antarmuka Pengguna**:
  - [ ] B.10.1. Tulis **7.1. Keputusan: CLI Berbasis Teks**: Status Disetujui, justifikasi (ringan, cepat, hemat resource, hotkey). Ambil data dari Feasibility Study bagian 4.1.5. Tuliskan kelebihan (kecepatan <1 detik, tanpa overhead rendering, minimal resource), keterbatasan (estetika minim, learning curve), strategi peningkatan UX (kode warna ANSI, tabel terformat, petunjuk input, konfirmasi Y/N, flowchart menu), risiko dan mitigasi (pelatihan 3 hari, User Manual cetak).
  - [ ] B.10.2. Tulis **7.2. Alternatif yang Dipertimbangkan dan Ditolak**: GUI Desktop (Tkinter/PyQt) — alasan penolakan (kompleksitas development, resource hardware besar, keluar dari batasan pemilik). Web Interface (Flask/Django) — alasan penolakan (memerlukan web server, browser, tambahan dependensi, keluar dari batasan pemilik).

- [ ] **B.11.** Tulis bagian **8. Keputusan Tech Stack — Keamanan dan Autentikasi**:
  - [ ] B.11.1. Tulis **8.1. Strategi Enkripsi Kata Sandi (bcrypt)**: Cost factor rekomendasi 12, alur hashing (registrasi) dan verifikasi (login). Ambil data dari Project Charter bagian 8.2 (N-2.3) dan Feasibility Study bagian 4.2.7.
  - [ ] B.11.2. Tulis **8.2. Strategi Autentikasi Session (JWT)**: Algoritma HS256, secret key dari .env, token payload (user_id, role, cabang_id, exp), durasi token 8 jam (1 shift kerja), invalidasi saat logout CLI. Strategi penanganan token expired di sesi CLI.
  - [ ] B.11.3. Tulis **8.3. Strategi Hak Akses (RBAC)**: Arsitektur 2 level role (Pemilik dan Staf dengan sub-role). Ambil data dari Stakeholder Register bagian profil hak akses RBAC per stakeholder (STK-001 s.d. STK-008). Daftar role: pemilik, kepala_percetakan, pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang.
  - [ ] B.11.4. Tulis **8.4. Strategi Audit Trail**: Format log (ID User, Timestamp, Tipe Aksi, Tabel Target, Nilai Lama, Nilai Baru). Ambil data dari Project Charter bagian 8.2 (N-2.2).
  - [ ] B.11.5. Tulis **8.5. Strategi Perlindungan Data (UU PDP)**: Enkripsi backup database AES-256, akses direktori backup hanya root Linux, kata sandi root MySQL yang kuat. Ambil data dari Feasibility Study bagian 8.2 dan Stakeholder Register risiko 9.9.

- [ ] **B.12.** Tulis bagian **9. Keputusan Tech Stack — Infrastruktur Pengembangan**:
  - [ ] B.12.1. Tulis **9.1. Alat Pengembangan dan Kolaborasi**: Editor/IDE (sesuai preferensi junior programmer), Version Control (Git), strategi branching (feature branch per modul), strategi code review (Gemini 3 Flash).
  - [ ] B.12.2. Tulis **9.2. Tim Pengembang dan Pembagian Teknologi per Anggota**: Buat tabel pemetaan anggota tim AI vs komponen teknologi yang dikuasai. Ambil data dari Project Charter bagian 7.1 dan Stakeholder Register bagian 3.9-3.14.
  - [ ] B.12.3. Tulis **9.3. Metodologi Pengembangan**: Ringkas pendekatan Hybrid (Waterfall untuk Planning-Design, Agile 2-minggu sprint untuk Implementation-Testing). Ambil data dari Project Charter bagian 9.4.

- [ ] **B.13.** Tulis bagian **10. Matriks Ringkasan Tech Stack Decision**:
  - [ ] B.13.1. Buat tabel ringkasan semua keputusan teknologi dengan kolom: No, Komponen, Teknologi Dipilih, Versi, Lisensi, Status (Disetujui/Rekomendasi), Justifikasi Utama (1 kalimat).
  - [ ] B.13.2. Pastikan mencakup minimal 15 komponen (bahasa, paradigma, database, 4 pustaka wajib, modul standar utama, OS server, OS client, antarmuka, bcrypt, JWT, RBAC, topologi jaringan).

- [ ] **B.14.** Tulis bagian **11. Analisis Risiko Teknis Terintegrasi**:
  - [ ] B.14.1. Buat tabel konsolidasi seluruh risiko teknis dari setiap komponen teknologi (gabungkan dari Project Charter bagian 10 dan Feasibility Study bagian 4.5). Kolom: No, Komponen Teknologi, Risiko, Probabilitas (1-5), Dampak (1-5), Rencana Mitigasi.
  - [ ] B.14.2. Pastikan mencakup minimal 8 risiko teknis spesifik.

- [ ] **B.15.** Tulis bagian **12. Kompatibilitas Tech Stack dengan Modul Fungsional**:
  - [ ] B.15.1. Buat matriks pemetaan komponen tech stack utama terhadap 9 modul fungsional AbuCom (M.1 s.d. M.9). Tandai dengan ✓ jika komponen tersebut digunakan langsung oleh modul, dan — jika tidak.
  - [ ] B.15.2. Ambil data modul dari Project Charter bagian 4.1.1.

- [ ] **B.16.** Tulis bagian **13. Kriteria Evaluasi Ulang (Technology Re-evaluation Triggers)**:
  - [ ] B.16.1. Daftar kondisi yang memicu peninjauan ulang keputusan teknologi (misal: Python versi baru dengan breaking changes, MySQL discontinue, pustaka deprecated, performa <5 detik tidak tercapai, kerentanan keamanan kritis ditemukan di pustaka).
  - [ ] B.16.2. Jelaskan proses eskalasi dan mekanisme pengambilan keputusan ulang.

- [ ] **B.17.** Tulis bagian **14. Persetujuan dan Otorisasi**:
  - [ ] B.17.1. Buat tabel persetujuan: Pihak Penandatangan, Jabatan/Peran, Tanda Tangan, Tanggal Persetujuan.
  - [ ] B.17.2. Isi dengan Pemilik Usaha AbuCom sebagai pihak penandatangan, status "*(Menunggu Persetujuan Digital)*".

- [ ] **B.18.** Tulis bagian **15. Glosarium**:
  - [ ] B.18.1. Daftar dan jelaskan seluruh istilah teknis yang digunakan dalam dokumen ini (minimal 20 istilah). Prioritaskan istilah yang mungkin tidak dipahami oleh junior programmer.
  - [ ] B.18.2. Contoh istilah yang WAJIB ada: Functional Programming, ACID, RBAC, Audit Trail, CLI, JWT, bcrypt, BOM, CAPEX, LAN, Client-Server, InnoDB, ANSI codes, Higher-order Function, Imutabilitas, Pure Function, Side-effect, PKWT, UU PDP, ADR, Multi-Branch Ready.

- [ ] **B.19.** Tulis bagian **16. Referensi Dokumen**:
  - [ ] B.19.1. Buat tabel referensi file yang digunakan dengan kolom: No, Nama File, Lokasi Path Relatif, Keterangan Penggunaan.
  - [ ] B.19.2. Masukkan keempat file referensi dari bagian 3 issue ini.

---

### Fase C: Validasi dan Finalisasi

- [ ] **C.1.** Validasi kelengkapan konten dokumen:
  - [ ] C.1.1. Periksa apakah semua 16 bagian dari kerangka struktur sudah terisi lengkap.
  - [ ] C.1.2. Periksa apakah semua data dari file referensi yang relevan sudah dimasukkan.
  - [ ] C.1.3. Periksa apakah tidak ada bagian yang hanya berisi placeholder generik atau kalimat kosong.

- [ ] **C.2.** Validasi konsistensi data lintas dokumen:
  - [ ] C.2.1. Pastikan nama teknologi, versi, dan lisensi konsisten dengan data di Project Charter.
  - [ ] C.2.2. Pastikan evaluasi kelayakan teknis konsisten dengan kesimpulan di Feasibility Study.
  - [ ] C.2.3. Pastikan daftar tim AI dan spesialisasinya konsisten dengan data di Stakeholder Register.

- [ ] **C.3.** Validasi penandaan data kosong:
  - [ ] C.3.1. Periksa apakah ada data yang tidak tersedia di file referensi.
  - [ ] C.3.2. Tandai setiap data kosong dengan format: `[DATA KOSONG — PERLU DIISI MANUAL OLEH PEMILIK USAHA: deskripsi data yang dibutuhkan]`.

- [ ] **C.4.** Validasi kualitas bahasa:
  - [ ] C.4.1. Periksa apakah seluruh konten ditulis dalam bahasa Indonesia yang natural dan tidak ambigu.
  - [ ] C.4.2. Periksa apakah istilah teknis berbahasa Inggris sudah dijelaskan artinya dalam konteks proyek.
  - [ ] C.4.3. Periksa apakah kalimat instruksi tidak membingungkan bagi junior programmer.

- [ ] **C.5.** Validasi kualitas dokumen sebagai referensi fase SDLC selanjutnya:
  - [ ] C.5.1. Pastikan dokumen ini cukup detail untuk menjadi input dokumen SRS (spesifikasi teknologi yang digunakan).
  - [ ] C.5.2. Pastikan dokumen ini cukup detail untuk menjadi input dokumen SDD (desain arsitektur dan pemilihan komponen).
  - [ ] C.5.3. Pastikan dokumen ini cukup detail untuk menjadi acuan coding style dan standardisasi kode saat fase Implementation.

- [ ] **C.6.** Tulis hasil akhir ke target file:
  - [ ] C.6.1. Simpan seluruh hasil penyusunan dokumen ke lokasi: `docs/sdlc/01_planning/04_tech_stack_decision.md`.
  - [ ] C.6.2. Pastikan file tersimpan dengan encoding UTF-8.

---

## 6. Instruksi Tambahan (Kaidah Khusus Dokumen Tech Stack Decision)

Berikut adalah instruksi tambahan yang spesifik untuk ciri khas dokumen Tech Stack Decision dan standar praktik industri yang harus dipatuhi:

### 6.1. Kaidah Penulisan Keputusan Teknologi (ADR Pattern)
- [ ] Setiap keputusan teknologi WAJIB ditulis mengikuti pola *Architecture Decision Record* (ADR) yang mencakup: **Konteks** (mengapa keputusan ini perlu diambil), **Keputusan** (teknologi apa yang dipilih), **Status** (Disetujui/Ditolak/Rekomendasi), **Konsekuensi** (dampak positif dan negatif dari keputusan ini), dan **Alternatif** (opsi lain yang dipertimbangkan dan alasan penolakannya).

### 6.2. Kaidah Evaluasi Alternatif
- [ ] Setiap komponen teknologi utama (bahasa, database, antarmuka) WAJIB memiliki minimal 2-3 alternatif yang dievaluasi dan ditolak. Penolakan harus disertai alasan teknis yang spesifik dan objektif (bukan opini subjektif).

### 6.3. Kaidah Versi dan Lisensi
- [ ] Setiap pustaka dan teknologi pihak ketiga WAJIB mencantumkan versi spesifik (atau minimal versi yang direkomendasikan) dan jenis lisensi open-source nya (MIT, Apache 2.0, GPL, BSD, PSF, dll.). Ini penting untuk menjamin kepatuhan lisensi dan reprodusibilitas lingkungan pengembangan.

### 6.4. Kaidah Traceability (Ketertelusuran)
- [ ] Setiap keputusan teknologi WAJIB dapat ditelusuri ke kebutuhan bisnis atau kebutuhan non-fungsional yang menjadi alasan pemilihannya. Misalnya: "bcrypt dipilih untuk memenuhi kebutuhan N-2.3 (Keamanan Data Kredensial) di Project Charter."

### 6.5. Kaidah Forward Compatibility
- [ ] Dokumen ini WAJIB mempertimbangkan bagaimana setiap keputusan teknologi berdampak pada kemungkinan pengembangan di masa depan (misal: migrasi dari CLI ke GUI, upgrade Python versi mayor, penambahan pustaka baru, ekspansi multi-cabang).

### 6.6. Kaidah Mandat Inovasi
- [ ] Sesuai arahan pemilik proyek (narasi.txt baris 98), jika ditemukan teknologi, pustaka, atau praktik terbaik yang belum disebutkan oleh pemilik namun secara signifikan dapat meningkatkan kualitas sistem, efisiensi, atau keamanan, maka WAJIB diusulkan dalam dokumen ini dengan penandaan `[REKOMENDASI]`.

### 6.7. Kaidah Presisi Desimal
- [ ] Dokumen ini WAJIB membahas secara eksplisit strategi penanganan presisi desimal untuk perhitungan BOM (menggunakan modul `decimal` Python, bukan `float` standar) mengingat ini adalah kebutuhan kritis bisnis percetakan AbuCom.

---

## 7. Kriteria Penerimaan (Acceptance Criteria)

Dokumen `04_tech_stack_decision.md` dinyatakan selesai dan diterima jika memenuhi seluruh kriteria berikut:

- [ ] **AC-1.** Seluruh 16 bagian dari kerangka struktur (Bagian 4 issue ini) sudah terisi lengkap tanpa ada bagian yang kosong atau hanya berisi placeholder generik.
- [ ] **AC-2.** Seluruh data dari 4 file referensi yang relevan sudah diekstraksi dan diintegrasikan ke dalam dokumen.
- [ ] **AC-3.** Setiap komponen teknologi utama memiliki minimal 2 alternatif yang dievaluasi dan ditolak dengan alasan teknis spesifik.
- [ ] **AC-4.** Matriks Ringkasan Tech Stack Decision (Bagian 10) mencakup minimal 15 komponen teknologi.
- [ ] **AC-5.** Analisis Risiko Teknis Terintegrasi (Bagian 11) mencakup minimal 8 risiko teknis spesifik.
- [ ] **AC-6.** Glosarium (Bagian 15) mencakup minimal 20 istilah teknis.
- [ ] **AC-7.** Seluruh data yang tidak tersedia di file referensi sudah ditandai dengan format `[DATA KOSONG — ...]`.
- [ ] **AC-8.** Bagian Referensi Dokumen (Bagian 16) mencantumkan seluruh file referensi yang digunakan.
- [ ] **AC-9.** Dokumen ditulis dalam bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami.
- [ ] **AC-10.** Dokumen sudah tersimpan di lokasi: `docs/sdlc/01_planning/04_tech_stack_decision.md`.
- [ ] **AC-11.** Konten dokumen layak dijadikan referensi dan input utama bagi dokumen SRS, SDD, dan fase Implementation.

---

## 8. Referensi Issue

| # | Nama File | Lokasi Path Relatif | Keterangan |
|---|---|---|---|
| 1 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Sumber data primer teknologi, modul, dan kebutuhan non-fungsional. |
| 2 | `02_feasibility_study.md` | `docs/sdlc/01_planning/02_feasibility_study.md` | Sumber data primer evaluasi teknis, risiko, dan analisis alternatif. |
| 3 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Sumber data sekunder profil tim AI dan pemetaan modul. |
| 4 | `narasi.txt` | `docs/sdlc/narasi.txt` | Sumber data pendukung spesifikasi teknis asli pemilik usaha. |
