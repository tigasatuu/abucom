---
judul      : Pembuatan dan Penyusunan Dokumen Software Requirements Specification (SRS)
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
prioritas  : High
status     : Open
tanggal    : 2026-05-23
target     : docs/sdlc/02_analysis/02_software_requirements.md
assignee   : Junior Programmer / LLM AI Model (Routine Coding & Documentation)
---

# Pembuatan dan Penyusunan Dokumen Software Requirements Specification (SRS)

## 1. Ringkasan Issue

Issue ini berisi instruksi perencanaan low-level yang sangat detail dan eksplisit untuk pembuatan dokumen **Software Requirements Specification (SRS)** proyek AbuCom. Dokumen SRS ini merupakan dokumen kedua dan terakhir pada **Fase 02 Analysis** dalam siklus SDLC AbuCom. Dokumen ini menjembatani kebutuhan bisnis (BRD) yang sudah didokumentasikan menuju spesifikasi teknis perangkat lunak yang siap diimplementasikan pada **Fase 03 Design (SDD/ERD)** dan **Fase 04 Implementation (Source Code)**.

**Tujuan utama issue ini** adalah memastikan siapapun yang mengeksekusi (junior programmer atau LLM AI model yang lebih murah/kecil) dapat mengerjakan pembuatan dokumen SRS ini **tanpa ambiguitas, tanpa halusinasi, dan tanpa interpretasi yang salah** terhadap data dan informasi yang ada pada file referensi.

**Perbedaan kritis SRS vs BRD**:
- **BRD** menjawab pertanyaan: *"APA yang dibutuhkan bisnis?"* — berfokus pada kebutuhan bisnis dan operasional.
- **SRS** menjawab pertanyaan: *"BAGAIMANA perangkat lunak harus berperilaku untuk memenuhi kebutuhan bisnis?"* — berfokus pada spesifikasi teknis fungsional & non-fungsional perangkat lunak secara detail.

---

## 2. Persona Pelaksana

### 2.1. Persona yang Ditugaskan
**Senior Software Requirements Engineer & Systems Analyst**

### 2.2. Alasan Pemilihan Persona
Persona ini dipilih karena alasan berikut:
1. **Otoritas Domain Teknis**: Software Requirements Engineer adalah persona standar industri yang paling kompeten dalam menerjemahkan kebutuhan bisnis tingkat tinggi (dari BRD) menjadi spesifikasi teknis perangkat lunak yang presisi, terukur, dan dapat diimplementasikan langsung oleh programmer.
2. **Keahlian Analisis Sistem**: Persona ini memiliki kemampuan untuk menguraikan setiap kebutuhan bisnis menjadi use case, spesifikasi input/output, aturan validasi, format data, batasan teknis, dan skenario pengecualian (*exception handling*) yang sangat detail.
3. **Jembatan BRD-ke-Kode**: Software Requirements Engineer berperan sebagai jembatan yang menerjemahkan bahasa bisnis pemilik usaha pada BRD menjadi bahasa teknis yang langsung dapat dipahami dan dieksekusi oleh tim pengembang AI dan Junior Programmer pada fase Design dan Implementation.
4. **Standar IEEE/ISO**: Persona ini memahami standar industri penyusunan SRS (IEEE 830-1998 / ISO/IEC/IEEE 29148:2018) dan mampu menerapkannya secara kontekstual sesuai skala proyek UMKM AbuCom.

### 2.3. Gaya Penulisan yang Wajib Dipatuhi
- Gunakan **Bahasa Indonesia** yang natural, formal namun mudah dipahami oleh junior programmer atau AI model lain yang lebih murah.
- Hindari kalimat ambigu, jargon tidak umum tanpa penjelasan, atau instruksi yang membuka ruang interpretasi ganda.
- Setiap spesifikasi kebutuhan perangkat lunak **harus menggunakan kata "HARUS" (SHALL/MUST)** untuk kebutuhan wajib, dan **"SEBAIKNYA" (SHOULD)** untuk kebutuhan opsional/rekomendasi.
- Setiap kebutuhan fungsional dan non-fungsional **wajib memiliki ID unik** untuk traceability (pelacakan ketertelusuran) ke BRD dan ke fase berikutnya.

---

## 3. File Referensi yang Dipilih

### 3.1. Daftar File Referensi (Diurutkan berdasarkan Prioritas Relevansi)

| # | Prioritas | Nama File Referensi | Lokasi Path Relatif | Alasan Pemilihan |
|---|:---------:|---|---|---|
| 1 | **PRIMER** | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | **INPUT UTAMA TUNGGAL** — Dokumen BRD v1.1 ini adalah sumber data primer yang berisi 40 kebutuhan bisnis fungsional (BR-F-01 s.d BR-F-40), 11 kebutuhan non-fungsional (BR-NF-01 s.d BR-NF-11), aturan bisnis numerik eksplisit, matriks RBAC 8 peran, profil 19 stakeholder, proses bisnis As-Is/To-Be, dan kriteria penerimaan bisnis. Seluruh spesifikasi SRS **wajib diderivasi langsung** dari dokumen ini. |
| 2 | **SEKUNDER** | `04_tech_stack_decision.md` | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Menyediakan spesifikasi teknis arsitektur (Python 3.14.2+, MySQL, FP Murni, CLI, bcrypt, JWT, RBAC, Audit Trail, AES-256) yang menjadi batasan mandatori implementasi. SRS harus mereferensikan batasan teknis ini untuk memastikan setiap spesifikasi perangkat lunak kompatibel dengan tech stack yang diputuskan. |
| 3 | **SEKUNDER** | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Menyediakan konteks ruang lingkup proyek (in-scope/out-of-scope), milestone jadwal, estimasi anggaran, RACI matrix, dan tujuan SMART goals. SRS harus konsisten dengan batas cakupan dan deliverables yang ditetapkan di Project Charter. |
| 4 | **TERSIER** | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Menyediakan daftar 42+ inovasi (INV-INT, INV-REC, INV-NEW) beserta prioritas implementasi dan relasi modul. SRS mereferensikan proposal inovasi ini untuk memastikan semua inovasi yang disetujui telah ter-spesifikasi secara teknis. |
| 5 | **TERSIER** | `02_feasibility_study.md` | `docs/sdlc/01_planning/02_feasibility_study.md` | Menyediakan data kelayakan ekonomi (ROI 26%, NPV Rp 47.471.075, BEP 9,5 bulan, CAPEX Rp 40.000.000, OPEX Rp 500.000/bulan) dan batasan prasyarat teknis. SRS mereferensikan batasan kelayakan ini untuk justifikasi prioritas fitur. |
| 6 | **TERSIER** | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Menyediakan profil detail 19 stakeholder, matriks Power/Interest, dan strategi pengelolaan. SRS mereferensikan data ini untuk pemetaan aktor use case. |

### 3.2. File yang TIDAK Dipilih dan Alasannya

| Nama File | Alasan Tidak Dipilih |
|---|---|
| `narasi.txt` | **TIDAK DIPERLUKAN LAGI** — Seluruh data operasional, workflow manual divisi, harapan pemilik, dan mandat inovasi dari narasi asli pemilik usaha sudah terangkum secara komprehensif dan terstruktur di dalam BRD v1.1 (referensi primer #1). Menggunakan `narasi.txt` secara langsung pada tahap SRS akan menyebabkan duplikasi data dan risiko inkonsistensi dengan dokumen BRD yang sudah tervalidasi. |

---

## 4. Kerangka Struktur Dokumen SRS

Kerangka struktur berikut disusun berdasarkan adaptasi standar **IEEE 830-1998** dan **ISO/IEC/IEEE 29148:2018** yang disesuaikan secara kontekstual dengan skala proyek UMKM AbuCom. Setiap bagian **wajib diisi secara lengkap** tanpa ada yang dilewati.

```
---
(YAML Front Matter: dokumen, proyek, versi, tanggal, status, penyusun)
---

# Software Requirements Specification (SRS) — AbuCom

## Riwayat Perubahan Dokumen
(Tabel riwayat versi: Versi, Tanggal, Perubahan, Oleh)

---

## 1. Pendahuluan
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Produk Perangkat Lunak
### 1.3. Definisi, Akronim, dan Singkatan
### 1.4. Referensi Dokumen SDLC
### 1.5. Posisi Dokumen dalam Siklus SDLC
### 1.6. Audiens Target dan Petunjuk Pembacaan

---

## 2. Deskripsi Umum Sistem
### 2.1. Perspektif Produk (Arsitektur Tingkat Tinggi)
### 2.2. Fungsi Utama Produk (Ringkasan 10 Modul)
### 2.3. Karakteristik dan Klasifikasi Pengguna (Aktor Sistem)
### 2.4. Lingkungan Operasi (Runtime Environment)
### 2.5. Batasan Desain dan Implementasi
### 2.6. Asumsi dan Ketergantungan Teknis

---

## 3. Spesifikasi Kebutuhan Fungsional
### 3.1. Modul Manajemen Transaksi & Kebijakan Harga (M.1)
#### SRS-F-001: [Judul Spesifikasi]
#### SRS-F-002: [Judul Spesifikasi]
#### ... (dst untuk setiap BR-F dari BRD)

### 3.2. Modul Manajemen Inventaris, BOM & Stock Opname (M.2)
#### SRS-F-0xx: [Judul Spesifikasi]
#### ... (dst)

### 3.3. Modul Layanan Keuangan Digital, PPOB, Jasa Keuangan & Service (M.3)
#### SRS-F-0xx: [Judul Spesifikasi]
#### ... (dst)

### 3.4. Modul Manajemen SDM, Penggajian & Poin Karyawan (M.4)
#### SRS-F-0xx: [Judul Spesifikasi]
#### ... (dst)

### 3.5. Modul Sistem Manajemen Antrian & Pelacakan Desain (M.5)
#### SRS-F-0xx: [Judul Spesifikasi]
#### ... (dst)

### 3.6. Modul Administrasi Pinjaman, Aset, & Pengeluaran Rutin (M.6)
#### SRS-F-0xx: [Judul Spesifikasi]
#### ... (dst)

### 3.7. Modul Keamanan, Audit Trail & Hak Akses (M.7)
#### SRS-F-0xx: [Judul Spesifikasi]
#### ... (dst)

### 3.8. Modul Pembatalan, Retur & CRM (M.8)
#### SRS-F-0xx: [Judul Spesifikasi]
#### ... (dst)

### 3.9. Modul Skalabilitas Multi-Cabang (M.9)
#### SRS-F-0xx: [Judul Spesifikasi]
#### ... (dst)

### 3.10. Modul Konfigurasi Sistem Runtime (M.10)
#### SRS-F-0xx: [Judul Spesifikasi]
#### ... (dst)

---

## 4. Spesifikasi Kebutuhan Non-Fungsional
### 4.1. Keamanan dan Privasi Data
### 4.2. Keandalan dan Integritas Sistem
### 4.3. Kinerja dan Waktu Respons
### 4.4. Portabilitas Lintas Sistem Operasi
### 4.5. Skalabilitas (Multi-Branch Ready)
### 4.6. Kemudahan Penggunaan (Usability)
### 4.7. Kepatuhan Regulasi (UU PDP No. 27/2022)
### 4.8. Pemeliharaan dan Testabilitas (Maintainability)

---

## 5. Spesifikasi Antarmuka Sistem
### 5.1. Antarmuka Pengguna (CLI User Interface)
### 5.2. Antarmuka Perangkat Keras (Hardware Interface)
### 5.3. Antarmuka Perangkat Lunak (Software Interface)
### 5.4. Antarmuka Komunikasi (Network Interface)

---

## 6. Spesifikasi Model Data Konseptual
### 6.1. Entitas Utama dan Atribut Kunci
### 6.2. Relasi Antar-Entitas
### 6.3. Diagram ER Konseptual (Mermaid)

---

## 7. Matriks Ketertelusuran Kebutuhan (Requirements Traceability Matrix)
### 7.1. Pemetaan BRD → SRS (Traceability Forward)
### 7.2. Pemetaan SRS → Modul/Komponen Target (Traceability Backward)

---

## 8. Kriteria Penerimaan Perangkat Lunak (Software Acceptance Criteria)

---

## 9. Prioritas Implementasi dan Penjadwalan Modul

---

## 10. Lampiran
### 10.1. Daftar Parameter Konfigurasi Sistem (Runtime Config)
### 10.2. Daftar Kode Status dan Pesan Error Sistem
### 10.3. Contoh Alur Interaksi CLI (Wireframe Teks)

---

## 11. Referensi Dokumen
(Tabel daftar berkas referensi yang digunakan)
```

---

## 5. Instruksi Detail Format Penulisan Setiap Kebutuhan Fungsional

Setiap spesifikasi kebutuhan fungsional pada Bagian 3 **wajib mengikuti format template standar** berikut ini tanpa pengecualian:

```markdown
#### SRS-F-XXX: [Judul Spesifikasi Teknis]

| Atribut | Nilai |
|---|---|
| **ID** | SRS-F-XXX |
| **Derivasi BRD** | BR-F-XX (Judul kebutuhan bisnis asal) |
| **Modul** | M.X — [Nama Modul] |
| **Prioritas** | High / Medium / Low |
| **Aktor** | [Daftar role pengguna yang terlibat] |

*   **Deskripsi Teknis**: [Penjelasan teknis detail tentang BAGAIMANA perangkat lunak harus berperilaku. Gunakan kata "HARUS" untuk kebutuhan wajib.]
*   **Input yang Diperlukan**: [Daftar eksplisit field input data yang diterima sistem, termasuk tipe data dan batasan validasi.]
*   **Proses/Logika Bisnis**: [Langkah-langkah proses internal sistem. Rumus perhitungan eksplisit jika ada. Referensikan aturan bisnis dari BRD.]
*   **Output yang Dihasilkan**: [Hasil yang ditampilkan di CLI atau disimpan ke database.]
*   **Aturan Validasi**: [Daftar validasi input/output yang wajib diterapkan: tipe data, batas minimum/maksimum, format regex, penanganan nilai kosong/null.]
*   **Penanganan Pengecualian (Exception Handling)**: [Skenario error yang mungkin terjadi dan bagaimana sistem harus merespons.]
*   **Ketergantungan**: [Daftar SRS-F lain atau tabel database yang menjadi prasyarat fungsional.]
*   **Catatan Implementasi**: [Panduan teknis spesifik: pustaka Python, tipe data MySQL, paradigma FP, presisi Decimal, dsb.]
```

---

## 6. Instruksi Tambahan Spesifik SRS

### 6.1. Instruksi Khusus Derivasi BRD → SRS
- Setiap kebutuhan bisnis fungsional dari BRD (BR-F-01 s.d BR-F-40) **wajib diturunkan menjadi minimal 1 spesifikasi SRS** yang lebih teknis dan detail. Satu BR-F pada BRD boleh dipecah menjadi beberapa SRS-F jika kompleksitasnya tinggi.
- Setiap kebutuhan bisnis non-fungsional dari BRD (BR-NF-01 s.d BR-NF-11) **wajib diturunkan menjadi spesifikasi SRS non-fungsional** (SRS-NF-XXX) pada Bagian 4 dengan batasan teknis yang presisi.
- Jika ditemukan kebutuhan teknis implisit yang **belum dicakup oleh BRD** namun secara logis diperlukan untuk implementasi perangkat lunak (misalnya: mekanisme session management, error logging, database connection pooling, startup initialization), maka spesifikasi SRS tambahan **wajib dibuat** dengan keterangan derivasi: `[SRS-TAMBAHAN: Kebutuhan teknis implisit untuk integritas sistem]`.

### 6.2. Instruksi Spesifikasi Model Data Konseptual
- Pada Bagian 6, buatlah daftar entitas utama database MySQL yang akan dibutuhkan beserta atribut kunci (primary key, foreign key, tipe data konseptual).
- Sertakan diagram Entity-Relationship (ER) konseptual menggunakan format **Mermaid erDiagram** yang menunjukkan relasi antar-entitas utama.
- Model data ini bersifat **konseptual** (bukan skema fisik akhir), sebagai panduan bagi System Design Document (SDD) di fase berikutnya.
- Pastikan setiap tabel utama memiliki kolom `cabang_id` (Multi-Branch Ready) sesuai BRD BR-F-37.

### 6.3. Instruksi Matriks Ketertelusuran (Traceability Matrix)
- Pada Bagian 7, buatlah tabel matriks ketertelusuran **dua arah**:
  - **Forward Traceability**: Pemetaan setiap BR-F / BR-NF dari BRD → SRS-F / SRS-NF di SRS.
  - **Backward Traceability**: Pemetaan setiap SRS-F / SRS-NF → Modul target, komponen Python, dan tabel database target.
- Tujuan: Memastikan **tidak ada satu pun kebutuhan BRD yang terlewat** dan **tidak ada spesifikasi SRS yang muncul tanpa dasar BRD**.

### 6.4. Instruksi Contoh Alur Interaksi CLI (Wireframe Teks)
- Pada Bagian 10.3, buatlah minimal **3 contoh wireframe teks** yang menunjukkan alur interaksi pengguna dengan terminal CLI secara step-by-step.
- Contoh wireframe yang wajib dibuat:
  1. Alur login pengguna dan navigasi menu utama berdasarkan role.
  2. Alur pencatatan transaksi penjualan produk percetakan kustom (termasuk BOM, DP, dan job tracking).
  3. Alur rekonsiliasi kas kasir di akhir shift.
- Format wireframe menggunakan blok kode teks (```` ```text ```` ) yang mensimulasikan tampilan terminal CLI.

### 6.5. Instruksi Daftar Parameter Konfigurasi Sistem
- Pada Bagian 10.1, buatlah tabel lengkap semua parameter konfigurasi dinamis yang tersimpan di tabel `system_configs` database, berdasarkan referensi BRD BR-F-38.
- Format tabel: `Nama Parameter | Tipe Data | Nilai Default | Deskripsi | Sumber BRD`.

### 6.6. Instruksi Daftar Kode Status dan Pesan Error
- Pada Bagian 10.2, buatlah daftar kode status sistem dan pesan error standar yang wajib ditampilkan oleh aplikasi CLI.
- Contoh: kode error otorisasi RBAC, kode error login gagal, kode error validasi input, kode error koneksi database, dsb.

### 6.7. Instruksi Penandaan Data Kosong
- Jika ada data atau informasi spesifik yang **tidak ditemukan di dalam file referensi** namun diperlukan untuk kelengkapan SRS, maka data tersebut **wajib ditandai** dengan format berikut:
  ```
  > ⚠️ PERLU DIISI PEMILIK: [Deskripsi data spesifik yang dibutuhkan dan alasan mengapa data ini diperlukan untuk SRS.]
  ```
  atau
  ```
  > ⚠️ PERLU KEPUTUSAN TEKNIS: [Deskripsi keputusan teknis yang belum terdokumentasi dan perlu diputuskan oleh System Architect atau Pemilik.]
  ```

---

## 7. Tahapan Implementasi (Step-by-Step Checklist)

Berikut adalah tahapan detail yang **wajib diikuti secara berurutan** oleh pelaksana (junior programmer atau LLM AI model). Setiap checklist `[ ]` adalah satu tugas atomik yang harus diselesaikan sebelum melanjutkan ke tugas berikutnya.

### Tahap 1: Persiapan dan Pembacaan File Referensi

- [ ] **1.1.** Adopsi persona **Senior Software Requirements Engineer & Systems Analyst** sebagai identitas penyusun dokumen. Seluruh gaya penulisan, kedalaman teknis, dan penggunaan terminologi harus konsisten dengan persona ini.

- [ ] **1.2.** Baca file referensi **PRIMER** secara menyeluruh:
  - [ ] Baca **SELURUH ISI** file `docs/sdlc/02_analysis/01_business_requirements.md` (BRD v1.1) dari baris pertama hingga baris terakhir.
  - [ ] Catat dan rangkum secara internal **setiap detail** berikut dari BRD:
    - [ ] Seluruh 40 kebutuhan bisnis fungsional (BR-F-01 s.d BR-F-40): deskripsi, aktor, aturan bisnis, kriteria penerimaan, prioritas, dan sumber data.
    - [ ] Seluruh 11 kebutuhan bisnis non-fungsional (BR-NF-01 s.d BR-NF-11): deskripsi, kriteria penerimaan, prioritas, dan sumber data.
    - [ ] Seluruh aturan bisnis numerik eksplisit (Bagian 9): skema harga, DP, smart payroll, kasbon, poin insentif, PPOB, rekonsiliasi kas, keamanan akun.
    - [ ] Matriks RBAC 8 peran pengguna (Bagian 5.3): hak akses per modul per peran.
    - [ ] Profil 5 divisi bisnis AbuCom (Bagian 3.3).
    - [ ] Proses bisnis As-Is dan To-Be (Bagian 4.1 s.d 4.3).
    - [ ] 8 aktor internal pengguna sistem dan 4 aktor eksternal (Bagian 5.1 s.d 5.4).
    - [ ] 6 tujuan bisnis SMART Goals (Bagian 6.2).
    - [ ] Inovasi dan rekomendasi best practice (Bagian 10).
    - [ ] Batasan, asumsi, ketergantungan, dan risiko bisnis (Bagian 11 dan 12).
    - [ ] Kriteria penerimaan bisnis (Bagian 13).
    - [ ] Glosarium istilah domain percetakan (Bagian 14).

- [ ] **1.3.** Baca file referensi **SEKUNDER** secara menyeluruh:
  - [ ] Baca **SELURUH ISI** file `docs/sdlc/01_planning/04_tech_stack_decision.md` (Tech Stack Decision v1.1).
  - [ ] Catat dan rangkum secara internal **setiap detail** batasan teknis berikut:
    - [ ] Python 3.14.2+ (Mandatory), paradigma Functional Programming murni.
    - [ ] MySQL Community Server LTS, engine InnoDB, collation utf8mb4_unicode_ci, Transaction Isolation REPEATABLE READ.
    - [ ] 4 pustaka wajib: mysql-connector-python, python-dotenv, bcrypt, pyjwt.
    - [ ] 2 pustaka rekomendasi: rich, tabulate.
    - [ ] Modul Python standar yang digunakan: decimal, functools, itertools, operator, os, pathlib, json, csv, datetime, typing, getpass, textwrap, shutil.
    - [ ] Arsitektur Client-Server LAN lokal (Dual-OS: Linux Debian 12 Server + Windows 11 Client).
    - [ ] CLI berbasis teks (ANSI, rich, tabulate).
    - [ ] Strategi keamanan: bcrypt Cost 12, JWT HS256 8 jam, RBAC, Audit Trail JSON, AES-256 backup, SQL Injection prevention, Rate Limiting 5x/10min, Input validation CLI.
    - [ ] Strategi infrastruktur: requirements.txt, schema.sql, seed.sql, Git Feature Branching.
    - [ ] Strategi pengujian: Unit Testing Pure Functions dengan pytest.

  - [ ] Baca **SELURUH ISI** file `docs/sdlc/01_planning/01_project_charter.md` (Project Charter v1.1).
  - [ ] Catat dan rangkum secara internal:
    - [ ] Ruang lingkup proyek: 10 modul in-scope dan item out-of-scope.
    - [ ] Milestone jadwal 12 bulan (8 fase).
    - [ ] Estimasi anggaran CAPEX Rp 40.000.000.
    - [ ] RACI Matrix pembagian peran.
    - [ ] 7 posisi struktur organisasi staf operasional.
    - [ ] Metodologi pengembangan Hybrid (Waterfall + Agile).

- [ ] **1.4.** Baca file referensi **TERSIER** secara menyeluruh:
  - [ ] Baca **SELURUH ISI** file `docs/sdlc/01_planning/05_innovation_proposal.md` (Innovation Proposal v1.1).
  - [ ] Catat dan rangkum: 42+ daftar inovasi (INV-INT, INV-REC, INV-NEW), prioritas implementasi, dan relasi modul target.

  - [ ] Baca **SELURUH ISI** file `docs/sdlc/01_planning/02_feasibility_study.md` (Feasibility Study v1.1).
  - [ ] Catat dan rangkum: ROI 26%, NPV Rp 47.471.075, BEP 9,5 bulan (800 transaksi), CAPEX Rp 40.000.000, OPEX Rp 500.000/bulan, prasyarat teknis kelayakan.

  - [ ] Baca **SELURUH ISI** file `docs/sdlc/01_planning/03_stakeholder_register.md` (Stakeholder Register v1.1).
  - [ ] Catat dan rangkum: Profil 19 stakeholder (STK-001 s.d STK-019), matriks Power/Interest, strategi komunikasi, dan ekspektasi per stakeholder.

- [ ] **1.5.** **JANGAN** membaca file `docs/sdlc/narasi.txt` — file ini sudah tidak diperlukan lagi karena seluruh isinya sudah terangkum di BRD v1.1.

### Tahap 2: Analisis dan Pemetaan Kebutuhan

- [ ] **2.1.** Buat pemetaan internal derivasi **setiap** kebutuhan bisnis fungsional BRD → spesifikasi SRS:
  - [ ] Petakan BR-F-01 s.d BR-F-06 (M.1 Transaksi & Harga) → SRS-F-001 s.d SRS-F-0xx.
  - [ ] Petakan BR-F-07 s.d BR-F-14, BR-F-40 (M.2 Inventaris & BOM) → SRS-F-0xx s.d SRS-F-0xx.
  - [ ] Petakan BR-F-15 s.d BR-F-17 (M.3 PPOB & Jasa Keuangan) → SRS-F-0xx s.d SRS-F-0xx.
  - [ ] Petakan BR-F-18 s.d BR-F-21 (M.4 SDM & Penggajian) → SRS-F-0xx s.d SRS-F-0xx.
  - [ ] Petakan BR-F-22 s.d BR-F-24 (M.5 Antrian & Desain) → SRS-F-0xx s.d SRS-F-0xx.
  - [ ] Petakan BR-F-25 s.d BR-F-29 (M.6 Pinjaman & Aset) → SRS-F-0xx s.d SRS-F-0xx.
  - [ ] Petakan BR-F-30 s.d BR-F-35 (M.7 Keamanan & Audit) → SRS-F-0xx s.d SRS-F-0xx.
  - [ ] Petakan BR-F-36 (M.8 CRM) → SRS-F-0xx.
  - [ ] Petakan BR-F-37 (M.9 Multi-Cabang) → SRS-F-0xx.
  - [ ] Petakan BR-F-38 (M.10 Konfigurasi) → SRS-F-0xx.

- [ ] **2.2.** Buat pemetaan internal derivasi **setiap** kebutuhan bisnis non-fungsional BRD → spesifikasi SRS:
  - [ ] Petakan BR-NF-01 s.d BR-NF-11 → SRS-NF-001 s.d SRS-NF-0xx.

- [ ] **2.3.** Identifikasi kebutuhan teknis implisit yang **belum ada di BRD** namun diperlukan untuk SRS:
  - [ ] Identifikasi kebutuhan startup/inisialisasi aplikasi CLI.
  - [ ] Identifikasi kebutuhan database connection management (pooling, retry, timeout).
  - [ ] Identifikasi kebutuhan session lifecycle management (login, token refresh, logout, auto-logout).
  - [ ] Identifikasi kebutuhan error logging dan penanganan exception global.
  - [ ] Identifikasi kebutuhan perintah navigasi CLI standar (kembali, keluar, help).
  - [ ] Identifikasi kebutuhan format tampilan data (pagination, sorting, filtering tabel CLI).
  - [ ] Identifikasi kebutuhan backup/restore database otomatis.
  - [ ] Identifikasi kebutuhan input data migrasi awal (CSV import workflow).
  - [ ] Tandai setiap kebutuhan tambahan dengan `[SRS-TAMBAHAN]`.

- [ ] **2.4.** Identifikasi entitas utama database MySQL yang dibutuhkan berdasarkan seluruh spesifikasi SRS:
  - [ ] Daftarkan minimal entitas: pengguna, cabang, pelanggan, supplier, barang, bom_komposisi, transaksi, detail_transaksi, antrian_kerja, absensi, kasbon, pinjaman_bank, pinjaman_kerabat, aset, pengeluaran, tabungan, saldo_ppob, saldo_ewallet, poin_insentif, payroll, audit_log, system_configs, shift_handover, rekonsiliasi_kas, limbah_produksi, stock_opname, riwayat_harga_supplier, utang_supplier.
  - [ ] Tentukan atribut kunci (PK, FK, tipe data konseptual) untuk setiap entitas.

### Tahap 3: Penyusunan Dokumen SRS

- [ ] **3.1.** Tulis **YAML Front Matter** dokumen:
  ```yaml
  ---
  dokumen    : Software Requirements Specification (SRS)
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : 2026-05-23
  status     : Draft
  penyusun   : Senior Software Requirements Engineer & Systems Analyst
  ---
  ```

- [ ] **3.2.** Tulis **Riwayat Perubahan Dokumen** (1 baris: v1.0, tanggal, deskripsi pembuatan awal, oleh persona).

- [ ] **3.3.** Tulis **Bagian 1: Pendahuluan**:
  - [ ] 1.1. Tujuan Dokumen: Jelaskan bahwa SRS ini mendefinisikan spesifikasi teknis perangkat lunak yang diderivasi dari BRD v1.1 untuk digunakan sebagai acuan fase Design dan Implementation.
  - [ ] 1.2. Cakupan Produk: Jelaskan nama produk (AbuCom CLI), lingkup 10 modul fungsional, dan batasan platform (Python 3.14.2+, MySQL, CLI, Dual-OS).
  - [ ] 1.3. Definisi, Akronim, Singkatan: Buat tabel glosarium teknis lengkap (SRS-spesifik + inherit dari BRD). Tambahkan istilah teknis SRS yang baru: Use Case, Parameterized Query, Connection Pooling, ACID, InnoDB, Foreign Key, Primary Key, CRUD, JWT, HS256, bcrypt, AES-256, dsb.
  - [ ] 1.4. Referensi Dokumen SDLC: Daftar 6 file referensi yang digunakan (sesuai Bagian 3.1 issue ini).
  - [ ] 1.5. Posisi Dokumen dalam SDLC: Jelaskan bahwa SRS adalah output terakhir Fase 02 Analysis, diderivasi dari BRD, dan menjadi input primer untuk SDD (Fase 03 Design) dan Test Plan (Fase 05 Testing).
  - [ ] 1.6. Audiens Target: Pemilik Usaha (Junior PM), Tim Pengembang AI, dan referensi untuk Fase Design/Implementation/Testing.

- [ ] **3.4.** Tulis **Bagian 2: Deskripsi Umum Sistem**:
  - [ ] 2.1. Perspektif Produk: Gambarkan arsitektur sistem tingkat tinggi (Client-Server LAN, Python CLI → MySQL). Sertakan diagram arsitektur menggunakan Mermaid.
  - [ ] 2.2. Fungsi Utama Produk: Rangkum 10 modul (M.1 s.d M.10) secara ringkas dengan referensi ke bagian SRS detail.
  - [ ] 2.3. Klasifikasi Pengguna: Definisikan 8 aktor internal (pemilik, kepala_percetakan, pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang) dengan deskripsi peran teknis masing-masing di CLI.
  - [ ] 2.4. Lingkungan Operasi: Spesifikasikan runtime environment secara detail (Python version, MySQL version, OS, hardware minimum, jaringan LAN).
  - [ ] 2.5. Batasan Desain: Daftarkan semua constraint teknis (FP murni, no OOP di bisnis logic, CLI only, no API eksternal, presisi Decimal, utf-8 encoding, dsb).
  - [ ] 2.6. Asumsi dan Ketergantungan Teknis: Derivasi dari BRD Bagian 11.3 dan 11.4.

- [ ] **3.5.** Tulis **Bagian 3: Spesifikasi Kebutuhan Fungsional** — INI ADALAH BAGIAN TERPENTING DAN TERBESAR:
  - [ ] Untuk **setiap** kebutuhan bisnis fungsional dari BRD (BR-F-01 s.d BR-F-40):
    - [ ] Turunkan menjadi spesifikasi SRS menggunakan template format di Bagian 5 issue ini.
    - [ ] Tambahkan detail teknis: tipe data MySQL, validasi input, rumus perhitungan eksplisit, format output CLI, penanganan error.
    - [ ] Referensikan batasan teknis dari Tech Stack Decision jika relevan (misalnya: Decimal untuk kalkulasi keuangan, parameterized query untuk SQL, bcrypt untuk password).
    - [ ] Pastikan setiap field input memiliki: nama field, tipe data (VARCHAR, INT, DECIMAL(15,4), DATE, TIMESTAMP, JSON, dsb), batasan panjang/range, apakah wajib/opsional, dan nilai default jika ada.
    - [ ] Pastikan setiap aturan validasi memiliki: kondisi validasi, pesan error yang ditampilkan jika gagal, dan aksi sistem jika gagal.
    - [ ] Pastikan setiap proses perhitungan memiliki: rumus matematika eksplisit, contoh numerik sederhana, dan presisi desimal yang digunakan.

- [ ] **3.6.** Tulis **Bagian 4: Spesifikasi Kebutuhan Non-Fungsional**:
  - [ ] Untuk **setiap** kebutuhan non-fungsional dari BRD (BR-NF-01 s.d BR-NF-11):
    - [ ] Turunkan menjadi spesifikasi SRS-NF dengan metrik terukur yang presisi.
    - [ ] Tentukan metode pengukuran/pengujian untuk setiap metrik non-fungsional.

- [ ] **3.7.** Tulis **Bagian 5: Spesifikasi Antarmuka Sistem**:
  - [ ] 5.1. Antarmuka Pengguna CLI: Jelaskan standar navigasi menu, layout tabel, pewarnaan ANSI, format input prompt, format pesan error, dan format struk teks.
  - [ ] 5.2. Antarmuka Hardware: Jelaskan interaksi dengan printer thermal struk 58mm/80mm.
  - [ ] 5.3. Antarmuka Software: Jelaskan interaksi Python ↔ MySQL (driver, connection string, parameterized query), interaksi dengan .env file, dan interaksi dengan file system (arsip desain, backup, CSV import).
  - [ ] 5.4. Antarmuka Komunikasi: Jelaskan topologi jaringan LAN client-server, protokol koneksi MySQL TCP/IP, dan port default.

- [ ] **3.8.** Tulis **Bagian 6: Model Data Konseptual**:
  - [ ] 6.1. Daftarkan seluruh entitas utama database MySQL dengan atribut kunci.
  - [ ] 6.2. Jelaskan relasi antar-entitas (one-to-many, many-to-many, dsb).
  - [ ] 6.3. Buat diagram ER konseptual menggunakan Mermaid `erDiagram`.
  - [ ] Pastikan setiap tabel memiliki kolom `cabang_id` (Multi-Branch Ready).

- [ ] **3.9.** Tulis **Bagian 7: Matriks Ketertelusuran (Traceability Matrix)**:
  - [ ] 7.1. Buat tabel Forward Traceability: BR-F-XX / BR-NF-XX → SRS-F-XXX / SRS-NF-XXX.
  - [ ] 7.2. Buat tabel Backward Traceability: SRS-F-XXX / SRS-NF-XXX → Modul, Komponen Python, dan Tabel Database target.
  - [ ] Verifikasi bahwa **setiap BR-F dan BR-NF dari BRD** memiliki minimal 1 pemetaan SRS.
  - [ ] Verifikasi bahwa **tidak ada SRS yang muncul tanpa derivasi dari BRD** (kecuali yang ditandai `[SRS-TAMBAHAN]`).

- [ ] **3.10.** Tulis **Bagian 8: Kriteria Penerimaan Perangkat Lunak**:
  - [ ] Derivasi dari BRD Bagian 13, tetapi tambahkan kriteria teknis perangkat lunak yang presisi (unit test coverage, integration test scenario, performance benchmark).

- [ ] **3.11.** Tulis **Bagian 9: Prioritas Implementasi dan Penjadwalan Modul**:
  - [ ] Susun urutan prioritas implementasi modul berdasarkan ketergantungan teknis dan prioritas bisnis.
  - [ ] Sesuaikan dengan milestone jadwal 12 bulan dari Project Charter.

- [ ] **3.12.** Tulis **Bagian 10: Lampiran**:
  - [ ] 10.1. Buat tabel lengkap parameter konfigurasi sistem (referensi BRD BR-F-38).
  - [ ] 10.2. Buat daftar kode status dan pesan error standar sistem.
  - [ ] 10.3. Buat minimal 3 contoh wireframe teks interaksi CLI:
    - [ ] Wireframe 1: Alur login dan navigasi menu utama role pemilik vs role kasir.
    - [ ] Wireframe 2: Alur transaksi cetak kustom (input pesanan → BOM → DP → job tracking → produksi → pelunasan).
    - [ ] Wireframe 3: Alur rekonsiliasi kas kasir di akhir shift.

- [ ] **3.13.** Tulis **Bagian 11: Referensi Dokumen**:
  - [ ] Buat tabel daftar 6 file referensi yang digunakan dalam penyusunan SRS ini (sesuai Bagian 3.1 issue ini).
  - [ ] Format tabel: No, Nama Berkas Referensi, Lokasi Path Relatif, Keterangan.

### Tahap 4: Validasi dan Finalisasi

- [ ] **4.1.** Lakukan validasi kelengkapan dokumen:
  - [ ] Verifikasi bahwa **seluruh 40 BR-F** dari BRD telah terpetakan ke SRS-F.
  - [ ] Verifikasi bahwa **seluruh 11 BR-NF** dari BRD telah terpetakan ke SRS-NF.
  - [ ] Verifikasi bahwa matriks traceability (Bagian 7) **lengkap dan konsisten** tanpa ada kebutuhan yang terlewat.
  - [ ] Verifikasi bahwa diagram ER konseptual (Bagian 6.3) mencakup **seluruh entitas** yang direferensikan oleh spesifikasi SRS.
  - [ ] Verifikasi bahwa semua parameter konfigurasi dari BRD BR-F-38 tercantum di lampiran (Bagian 10.1).

- [ ] **4.2.** Lakukan validasi konsistensi lintas dokumen:
  - [ ] Verifikasi bahwa seluruh angka numerik (nominal Rupiah, persentase, batas toleransi, threshold) di SRS **100% konsisten** dengan angka di BRD.
  - [ ] Verifikasi bahwa seluruh batasan teknis di SRS **100% konsisten** dengan keputusan di Tech Stack Decision.
  - [ ] Verifikasi bahwa ruang lingkup modul di SRS **100% konsisten** dengan cakupan in-scope Project Charter.

- [ ] **4.3.** Lakukan validasi kualitas penulisan:
  - [ ] Verifikasi bahwa setiap kebutuhan fungsional SRS menggunakan format template yang konsisten (sesuai Bagian 5 issue ini).
  - [ ] Verifikasi bahwa bahasa Indonesia yang digunakan natural, tidak ambigu, dan mudah dipahami.
  - [ ] Verifikasi bahwa setiap data yang kosong/tidak tersedia ditandai dengan `⚠️ PERLU DIISI PEMILIK` atau `⚠️ PERLU KEPUTUSAN TEKNIS`.
  - [ ] Verifikasi bahwa ID unik (SRS-F-XXX, SRS-NF-XXX) berjalan secara berurutan tanpa gap.

- [ ] **4.4.** Lakukan validasi kesiapan sebagai input fase berikutnya:
  - [ ] Verifikasi bahwa Bagian 6 (Model Data Konseptual) cukup detail untuk dijadikan input langsung bagi System Design Document (SDD).
  - [ ] Verifikasi bahwa setiap SRS-F memiliki "Catatan Implementasi" yang cukup spesifik untuk dijadikan panduan programmer.
  - [ ] Verifikasi bahwa contoh wireframe CLI (Bagian 10.3) cukup detail untuk dijadikan referensi desain UI CLI.

### Tahap 5: Penulisan ke Target File

- [ ] **5.1.** Tulis **SELURUH** hasil penyusunan dokumen SRS ke dalam target file:
  ```
  docs/sdlc/02_analysis/02_software_requirements.md
  ```

- [ ] **5.2.** Pastikan file yang ditulis berisi **dokumen lengkap tanpa potongan, tanpa ringkasan, dan tanpa truncation**. Seluruh bagian dari Bagian 1 hingga Bagian 11 harus tertulis penuh di dalam file target.

- [ ] **5.3.** Pastikan format markdown (heading, tabel, blok kode, diagram mermaid, blockquote peringatan) ter-render dengan benar dan konsisten.

---

## 8. Aturan dan Larangan Penting

### 8.1. WAJIB Dilakukan
1. **WAJIB** membaca SELURUH isi setiap file referensi yang ditentukan sebelum mulai menulis SRS.
2. **WAJIB** mengikuti format template penulisan spesifikasi fungsional yang sudah ditentukan (Bagian 5 issue ini) secara konsisten untuk semua SRS-F.
3. **WAJIB** menulis dokumen SRS dalam Bahasa Indonesia yang natural, formal, dan mudah dipahami.
4. **WAJIB** memastikan setiap kebutuhan bisnis dari BRD (BR-F dan BR-NF) memiliki pemetaan ke SRS.
5. **WAJIB** menyertakan matriks traceability dua arah (forward dan backward).
6. **WAJIB** menyertakan diagram ER konseptual menggunakan Mermaid.
7. **WAJIB** menyertakan minimal 3 wireframe teks CLI.
8. **WAJIB** menulis dokumen final yang LENGKAP dan UTUH tanpa potongan apapun.
9. **WAJIB** menandai data kosong/tidak tersedia dengan penanda `⚠️`.
10. **WAJIB** mencantumkan referensi file di bagian akhir dokumen.

### 8.2. DILARANG Dilakukan
1. **DILARANG** mengarang data, angka, atau informasi yang tidak ada di file referensi (anti-halusinasi).
2. **DILARANG** melewatkan satu pun kebutuhan bisnis dari BRD tanpa pemetaan SRS.
3. **DILARANG** memotong, meringkas, atau men-truncate isi dokumen SRS. Dokumen harus ditulis LENGKAP.
4. **DILARANG** mengubah angka numerik yang sudah ditetapkan di BRD atau Tech Stack Decision.
5. **DILARANG** menambahkan spesifikasi teknis yang bertentangan dengan batasan mandatori Tech Stack Decision.
6. **DILARANG** menggunakan `narasi.txt` sebagai referensi langsung — gunakan BRD v1.1 sebagai satu-satunya sumber data primer.
7. **DILARANG** menggunakan bahasa yang ambigu, tidak jelas, atau membuka ruang interpretasi ganda.
8. **DILARANG** menulis spesifikasi tanpa ID unik (setiap kebutuhan HARUS memiliki ID SRS-F-XXX atau SRS-NF-XXX).

---

## 9. Referensi Issue

| # | Nama Berkas Referensi | Lokasi Path Relatif | Peran dalam Issue |
|---|---|---|---|
| 1 | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | Input data PRIMER — sumber derivasi utama seluruh spesifikasi SRS. |
| 2 | `04_tech_stack_decision.md` | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Input data SEKUNDER — sumber batasan teknis arsitektur dan keamanan. |
| 3 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Input data SEKUNDER — sumber ruang lingkup, milestone, dan anggaran. |
| 4 | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Input data TERSIER — sumber daftar inovasi dan prioritas implementasi. |
| 5 | `02_feasibility_study.md` | `docs/sdlc/01_planning/02_feasibility_study.md` | Input data TERSIER — sumber kelayakan ekonomi dan prasyarat teknis. |
| 6 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Input data TERSIER — sumber profil stakeholder dan pemetaan aktor. |
