# Pembuatan Dokumen Workflow Diagram

---

| Atribut        | Nilai |
|----------------|-------|
| **Judul**      | Pembuatan dan Penyusunan Dokumen Workflow Diagram — Fase 02 Analysis |
| **Prioritas**  | High |
| **Status**     | Open |
| **Tanggal**    | 2026-05-23 |
| **Target File**| `docs/sdlc/02_analysis/04_workflow_diagram.md` |
| **Estimasi**   | 1 sesi kerja penuh |
| **Assignee**   | Junior Programmer / LLM AI Model (Low-Tier) |

---

## 1. Deskripsi Issue

Issue ini menginstruksikan pembuatan dan penyusunan dokumen **Workflow Diagram** untuk proyek AbuCom. Dokumen ini merupakan artefak keempat dan penutup pada **Fase 02 Analysis** dalam siklus SDLC AbuCom. Workflow Diagram berfungsi untuk memodelkan seluruh alur kerja operasional bisnis dan sistem secara visual menggunakan diagram alir (flowchart/activity diagram) dalam sintaks Mermaid, mencakup alur proses end-to-end dari setiap divisi dan modul fungsional AbuCom CLI.

Dokumen ini akan menjadi jembatan visual kritis antara Fase 02 Analysis dan Fase 03 Design, memastikan seluruh alur logika bisnis tergambar jelas sebelum masuk ke perancangan arsitektur sistem (SDD), Entity Relationship Diagram (ERD), dan skema database.

---

## 2. Persona Penyusun Dokumen

Gunakan persona berikut sebagai identitas penyusun dokumen ini:

> **Senior Business Process Analyst & Workflow Modeling Specialist**

Persona ini dipilih karena:
- Memiliki otoritas dan keahlian dalam memodelkan proses bisnis operasional ke dalam diagram alir standar industri (BPMN-style / Activity Diagram).
- Mampu mengidentifikasi swimlane per aktor, decision point, parallel flow, dan exception handling dalam setiap alur kerja.
- Memiliki kompetensi memetakan transisi status, aturan bisnis kondisional, dan integrasi antar-modul secara visual.

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca dan dirangkum** sebagai dasar utama penyusunan dokumen ini, diurutkan berdasarkan tingkat prioritas:

| # | Prioritas | Nama Berkas | Lokasi Path Relatif | Alasan Pemilihan |
|---|-----------|-------------|----------------------|------------------|
| 1 | **PRIMER** | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | Berisi alur kerja As-Is dan To-Be seluruh divisi (Bab 4), aturan bisnis fungsional 40+ kebutuhan, matriks RBAC, dan pain points operasional yang menjadi fondasi utama diagram workflow. |
| 2 | **PRIMER** | `02_software_requirements.md` | `docs/sdlc/02_analysis/02_software_requirements.md` | Berisi spesifikasi teknis input/proses/output setiap fungsi (SRS-F-001 s.d SRS-F-040+), logika kondisional, aturan validasi, dan exception handling yang mendefinisikan alur sistem secara detail. |
| 3 | **PRIMER** | `03_use_case_diagram.md` | `docs/sdlc/02_analysis/03_use_case_diagram.md` | Berisi 44 use case dengan Main Flow, Alternative Flow, dan Exception Flow yang menjadi basis langsung pemetaan langkah-langkah sekuensial pada setiap workflow diagram. |
| 4 | **SEKUNDER** | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Berisi definisi ruang lingkup 10 modul, struktur organisasi 7 staf, dan cakupan divisi bisnis yang menentukan pembagian swimlane workflow. |
| 5 | **SEKUNDER** | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Berisi 43 inovasi (integrated, recommended, new) yang mempengaruhi percabangan dan fitur tambahan pada alur kerja To-Be. |
| 6 | **TERSIER** | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Berisi profil 19 stakeholder dan matriks Power/Interest untuk memvalidasi siapa aktor yang terlibat di setiap swimlane workflow. |
| 7 | **TERSIER** | `04_tech_stack_decision.md` | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Berisi batasan teknis (CLI, Python FP, MySQL) yang mempengaruhi representasi boundary dan constraint pada diagram. |
| 8 | **TERSIER** | `narasi.txt` | `docs/sdlc/narasi.txt` | Berisi narasi asli pemilik usaha yang menggambarkan alur kerja manual (As-Is) setiap divisi secara naratif. Digunakan sebagai cross-check untuk memastikan tidak ada alur operasional yang terlewat. |

---

## 4. Kerangka Struktur Dokumen Utama

Berikut adalah kerangka dokumen Workflow Diagram yang **wajib diikuti**. Struktur ini mengikuti standar praktik industri Business Process Modeling dan Workflow Documentation:

```
---
(Front Matter YAML: dokumen, proyek, versi, tanggal, status, penyusun)
---

# Workflow Diagram — AbuCom

## Riwayat Perubahan Dokumen
(Tabel versi, tanggal, perubahan, oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target
### 1.6. Konvensi Notasi Diagram

---

## 2. Ringkasan Alur Kerja Sistem (Executive Workflow Overview)
### 2.1. Diagram Alur Kerja Makro Keseluruhan Sistem
(Diagram Mermaid flowchart tingkat tinggi yang menggambarkan alur kerja
end-to-end keseluruhan sistem AbuCom dari pelanggan datang hingga laporan
akhir hari, mencakup interaksi antar 10 modul)

### 2.2. Peta Keterhubungan Workflow antar Modul
(Diagram Mermaid yang menunjukkan bagaimana output workflow satu modul
menjadi input bagi modul lain)

---

## 3. Workflow Diagram Proses Bisnis As-Is (Kondisi Saat Ini — Manual)
### 3.1. Workflow As-Is: Divisi Produk Percetakan Kustom
### 3.2. Workflow As-Is: Divisi Penjualan Retail ATK
### 3.3. Workflow As-Is: Divisi Layanan Pulsa & PPOB
### 3.4. Workflow As-Is: Divisi Jasa Keuangan (Transfer & Tarik Tunai)
### 3.5. Workflow As-Is: Divisi Jasa Teknis (Service & Install)
### 3.6. Workflow As-Is: Administrasi Pinjaman, SDM & Pengeluaran
(Setiap sub-bab berisi diagram Mermaid flowchart/activity diagram
yang memodelkan proses manual saat ini)

---

## 4. Workflow Diagram Proses Bisnis To-Be (Kondisi Target — Sistem AbuCom CLI)

### 4.1. Workflow Operasional Harian Toko (Daily Operation Master Workflow)
(Diagram Mermaid swimlane/flowchart keseluruhan operasi harian toko
dari pembukaan shift hingga penutupan shift, mencakup login → dashboard
→ transaksi → rekonsiliasi → logout)

### 4.2. Workflow Modul M.1 — Manajemen Transaksi & Kebijakan Harga
#### 4.2.1. Alur Pencatatan Transaksi Penjualan Multi-Divisi
#### 4.2.2. Alur Penentuan Skema Harga Dinamis (Retail/Grosir/Mitra)
#### 4.2.3. Alur Pembayaran Bertahap (DP & Pelunasan)
#### 4.2.4. Alur Pembatalan Transaksi & Retur Barang
#### 4.2.5. Alur Pelacakan Margin Keuntungan per Produk
#### 4.2.6. Alur Ekspor Struk Nota Thermal

### 4.3. Workflow Modul M.2 — Manajemen Inventaris, BOM & Stock Opname
#### 4.3.1. Alur Perhitungan HPP Otomatis Berbasis BOM Desimal
#### 4.3.2. Alur Pencatatan Limbah Produksi (Waste Management)
#### 4.3.3. Alur Manajemen Satuan & Konversi UoM
#### 4.3.4. Alur Sinkronisasi Pengambilan ATK Internal
#### 4.3.5. Alur Rekonsiliasi Stok Berkala (Stock Opname)
#### 4.3.6. Alur Analisis Prediksi Re-Order Stok
#### 4.3.7. Alur Riwayat Harga Beli Supplier (Price Tracking)
#### 4.3.8. Alur Import Data CSV Semiautomatis
#### 4.3.9. Alur Manajemen Data Supplier & Pencatatan Utang Usaha
#### 4.3.10. Alur Backup & Restore Database

### 4.4. Workflow Modul M.3 — Layanan Digital, PPOB & Jasa Service
#### 4.4.1. Alur Manajemen Saldo PPOB & Alert Deposit
#### 4.4.2. Alur Optimalisasi Biaya Admin Jasa Keuangan (6 Akun)
#### 4.4.3. Alur Pencatatan Jasa Service & Teknisi

### 4.5. Workflow Modul M.4 — Manajemen SDM, Penggajian & Poin Karyawan
#### 4.5.1. Alur Manajemen Data Karyawan, Absensi & Kasbon
#### 4.5.2. Alur Penggajian Cerdas (Smart Payroll)
#### 4.5.3. Alur Akumulasi Poin Insentif Karyawan
#### 4.5.4. Alur Pemotongan Gaji Otomatis atas Kasbon

### 4.6. Workflow Modul M.5 — Sistem Antrian & Pelacakan Desain
#### 4.6.1. Alur Manajemen Antrian Digital (Job Tracking 5 Status)
#### 4.6.2. Alur Pengelolaan Arsip Desain Pelanggan
#### 4.6.3. Alur Pembuatan Link Notifikasi WhatsApp

### 4.7. Workflow Modul M.6 — Administrasi Pinjaman, Aset & Pengeluaran
#### 4.7.1. Alur Pengelolaan Pinjaman Modal (Bank & Keluarga)
#### 4.7.2. Alur Penyajian Laporan Laba/Rugi Instan per Divisi
#### 4.7.3. Alur Notifikasi Jatuh Tempo Utang H-3
#### 4.7.4. Alur Pengelolaan Aset Tetap, Depresiasi & Tabungan
#### 4.7.5. Alur Pengelolaan Pengeluaran Rutin & Biaya Tak Terduga

### 4.8. Workflow Modul M.7 — Keamanan, Audit Trail & Hak Akses
#### 4.8.1. Alur Otentikasi Login & Manajemen Session JWT
#### 4.8.2. Alur Pembatasan Akses Menu RBAC Multi-Level
#### 4.8.3. Alur Pencatatan Audit Trail Log JSON
#### 4.8.4. Alur Serah Terima Shift Karyawan
#### 4.8.5. Alur Rekonsiliasi Kas Harian Laci Kasir
#### 4.8.6. Alur Pemantauan Anomali Transaksi (Fraud Detection)
#### 4.8.7. Alur Input Data Awal dari Excel (Setup)

### 4.9. Workflow Modul M.8 — CRM & Riwayat Pelanggan
#### 4.9.1. Alur Pengelolaan Database CRM Pelanggan

### 4.10. Workflow Modul M.9 — Skalabilitas Multi-Cabang
#### 4.10.1. Alur Penerapan Identifikasi Multi-Cabang

### 4.11. Workflow Modul M.10 — Konfigurasi Sistem Runtime
#### 4.11.1. Alur Konfigurasi Parameter Bisnis Runtime

---

## 5. Workflow Diagram Proses Lintas Modul (Cross-Module Integration Workflow)
### 5.1. Workflow Pesanan Cetak Kustom End-to-End
(Alur lengkap dari pelanggan memesan → pramuniaga input → desainer proses
→ produksi cetak → BOM + limbah → kasir pelunasan → poin insentif →
rekonsiliasi kas → audit trail → laporan)

### 5.2. Workflow Pengadaan Barang & Manajemen Supplier End-to-End
(Alur lengkap dari prediksi re-order → gudang cek supplier →
price tracking → pembelian → utang tempo → barang masuk →
stok update → stock opname)

### 5.3. Workflow Penutupan Hari Operasional (End-of-Day)
(Alur lengkap dari rekonsiliasi kas → serah terima shift →
pencatatan absensi → akumulasi poin → laporan harian pemilik)

---

## 6. Matriks Traceability Workflow ↔ Use Case ↔ BRD ↔ SRS
(Tabel mapping setiap workflow diagram terhadap UC-ID, BR-F-XX,
dan SRS-F-XXX untuk menjamin kelengkapan dan ketelusuran)

---

## 7. Penanganan Kondisi Khusus & Percabangan Pengecualian
### 7.1. Daftar Decision Point Kritis
(Tabel daftar seluruh titik keputusan/percabangan penting pada
diagram workflow beserta kondisi true/false dan aksi yang diambil)

### 7.2. Daftar Exception Flow pada Workflow
(Tabel daftar seluruh penanganan error/pengecualian pada workflow
beserta kode error SRS dan aksi recovery)

---

## 8. Glosarium Istilah Workflow
(Daftar alfabetis penjelasan istilah khusus modeling workflow,
notasi diagram, dan domain bisnis percetakan yang digunakan)

---

## 9. Referensi Dokumen
(Tabel daftar berkas referensi yang digunakan)
```

---

## 5. Instruksi Detail Tahapan Eksekusi

### FASE A — Persiapan & Pembacaan File Referensi

Pada fase ini, kamu akan membaca dan merangkum semua data yang relevan dari file referensi. **Jangan mulai menulis dokumen utama sebelum semua file referensi selesai dibaca dan dirangkum.**

- [ ] **A.1.** Baca file `docs/sdlc/narasi.txt` secara keseluruhan (115 baris). Rangkum semua informasi alur kerja manual per divisi yang diceritakan pemilik usaha (khususnya bagian "Detail Pekerjaan dan Alur Kerja" di baris 45-70). Catat setiap langkah kerja manual, setiap aktor yang terlibat, dan setiap decision point yang tersirat.

- [ ] **A.2.** Baca file `docs/sdlc/02_analysis/01_business_requirements.md` secara keseluruhan (868 baris). Rangkum data berikut:
  - [ ] A.2.1. Bagian **3.2 Struktur Organisasi** — catat 7 posisi staf dan peran masing-masing.
  - [ ] A.2.2. Bagian **3.3 Kategori Produk & Layanan** — catat 5 divisi bisnis.
  - [ ] A.2.3. Bagian **3.4 Budaya Kerja** — catat kebijakan cross-functional.
  - [ ] A.2.4. Bagian **4.1 Proses Bisnis Saat Ini (As-Is)** — catat secara detail setiap langkah alur kerja dari 6 sub-bagian (4.1.1 s.d 4.1.6). Ini adalah sumber utama untuk Bab 3 dokumen.
  - [ ] A.2.5. Bagian **4.2 Identifikasi Titik Kelemahan (Pain Points)** — catat semua pain points yang harus diatasi dalam workflow To-Be.
  - [ ] A.2.6. Bagian **4.3 Proses Bisnis yang Diharapkan (To-Be)** — catat diagram mermaid dan 7 poin penjelasan alur baru. Ini adalah sumber utama untuk Bab 4 dokumen.
  - [ ] A.2.7. Bagian **5. Pemangku Kepentingan** — catat 8 aktor internal, 4 aktor eksternal, dan matriks RBAC per peran.
  - [ ] A.2.8. Bagian **7. Kebutuhan Bisnis Fungsional** — catat seluruh 40+ kebutuhan bisnis (BR-F-01 s.d BR-F-40), khususnya deskripsi, aturan bisnis, aktor terkait, dan kriteria penerimaan. Ini menentukan logika percabangan pada diagram.

- [ ] **A.3.** Baca file `docs/sdlc/02_analysis/02_software_requirements.md` secara keseluruhan (2241 baris). Rangkum data berikut:
  - [ ] A.3.1. Bagian **3. Spesifikasi Kebutuhan Fungsional** — catat setiap SRS-F-XXX beserta Input, Proses/Logika Bisnis, Output, Aturan Validasi, dan Penanganan Pengecualian. Data ini menentukan langkah-langkah detail dan percabangan keputusan pada setiap workflow diagram.
  - [ ] A.3.2. Bagian **4. Kebutuhan Non-Fungsional** — catat setiap SRS-NF-XXX yang mempengaruhi workflow (misal: SRS-NF terkait session timeout, rate limiting, presisi desimal).
  - [ ] A.3.3. Bagian **5. Model Data Konseptual / ERD** — catat entitas dan relasi yang berpengaruh pada alur data workflow.
  - [ ] A.3.4. Bagian **RTM (Requirements Traceability Matrix)** — catat pemetaan SRS → BRD untuk validasi kelengkapan.

- [ ] **A.4.** Baca file `docs/sdlc/02_analysis/03_use_case_diagram.md` secara keseluruhan (1547 baris). Rangkum data berikut:
  - [ ] A.4.1. Bagian **3.2 Master Daftar Use Case** — catat semua 44 use case (UC-001 s.d UC-044) beserta modul, aktor primer/sekunder, dan derivasi BRD/SRS.
  - [ ] A.4.2. Bagian **5. Spesifikasi Naratif Use Case** — catat setiap use case beserta Main Flow, Alternative Flow, dan Exception Flow-nya. Main Flow setiap use case menjadi basis langkah-langkah sekuensial pada workflow diagram. Alternative Flow menjadi percabangan. Exception Flow menjadi penanganan error.
  - [ ] A.4.3. Bagian **6. Relasi Dependensi** — catat semua relasi `<<include>>` dan `<<extend>>` karena ini menentukan sub-workflow yang dipanggil.
  - [ ] A.4.4. Bagian **7. Matriks Traceability** — catat untuk validasi kelengkapan.

- [ ] **A.5.** Baca file `docs/sdlc/01_planning/01_project_charter.md`. Rangkum data berikut:
  - [ ] A.5.1. Daftar 10 modul fungsional beserta deskripsinya.
  - [ ] A.5.2. Struktur organisasi dan pembagian tim.
  - [ ] A.5.3. Scope dan batasan proyek.

- [ ] **A.6.** Baca file `docs/sdlc/01_planning/05_innovation_proposal.md`. Rangkum data berikut:
  - [ ] A.6.1. Daftar 43 inovasi (integrated, recommended, new) beserta modul terkait dan dampaknya terhadap alur kerja operasional.

- [ ] **A.7.** Baca file `docs/sdlc/01_planning/03_stakeholder_register.md`. Rangkum data berikut:
  - [ ] A.7.1. Profil 19 stakeholder dan matriks Power/Interest grid.
  - [ ] A.7.2. Hak akses dan ekspektasi setiap stakeholder.

- [ ] **A.8.** Baca file `docs/sdlc/01_planning/04_tech_stack_decision.md`. Rangkum data berikut:
  - [ ] A.8.1. Batasan teknologi yang mempengaruhi workflow (CLI only, FP paradigm, MySQL lokal, LAN topology).

---

### FASE B — Penyusunan Konten Dokumen

Pada fase ini, kamu akan menulis dokumen berdasarkan rangkuman data yang telah dikumpulkan di Fase A. Ikuti kerangka struktur di Bab 4 issue ini secara berurutan.

- [ ] **B.1. Front Matter YAML** — Tulis metadata dokumen dengan format yang konsisten dengan dokumen SDLC AbuCom lainnya:
  ```yaml
  ---
  dokumen    : Workflow Diagram
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [tanggal pengerjaan, format YYYY-MM-DD]
  status     : Draft
  penyusun   : Senior Business Process Analyst & Workflow Modeling Specialist
  ---
  ```

- [ ] **B.2. Riwayat Perubahan Dokumen** — Buat tabel versi perubahan. Untuk versi 1.0, tuliskan catatan pembuatan awal dokumen beserta sumber referensi yang digunakan.

- [ ] **B.3. Bab 1 — Informasi Dokumen** — Tulis setiap sub-bab:
  - [ ] B.3.1. **1.1 Tujuan Dokumen**: Jelaskan bahwa dokumen ini memodelkan seluruh alur kerja operasional bisnis AbuCom (As-Is dan To-Be) secara visual menggunakan diagram alir Mermaid. Jelaskan tujuannya sebagai jembatan visual sebelum memasuki Fase 03 Design.
  - [ ] B.3.2. **1.2 Cakupan Dokumen**: Jelaskan cakupan meliputi workflow As-Is (6 divisi manual), workflow To-Be (10 modul sistem), workflow lintas modul, matriks traceability, dan daftar decision point.
  - [ ] B.3.3. **1.3 Posisi Dokumen dalam Siklus SDLC**: Jelaskan bahwa dokumen ini adalah artefak keempat dan penutup pada Fase 02 Analysis. Tampilkan diagram posisi SDLC serupa dengan dokumen sebelumnya.
  - [ ] B.3.4. **1.4 Hubungan dengan Dokumen SDLC Lainnya**: Jelaskan input (BRD, SRS, UCD) dan output (SDD, ERD, Test Cases) dokumen ini.
  - [ ] B.3.5. **1.5 Audiens Target**: Daftar pembaca formal (Pemilik Usaha, Tim AI, Calon Staf).
  - [ ] B.3.6. **1.6 Konvensi Notasi Diagram**: Jelaskan simbol-simbol yang digunakan pada diagram Mermaid (start/end node, process node, decision diamond, swimlane, subprocess, dll). Sediakan legenda visual singkat agar pembaca tidak ambigu.

- [ ] **B.4. Bab 2 — Ringkasan Alur Kerja Sistem** — Tulis:
  - [ ] B.4.1. **2.1 Diagram Alur Kerja Makro**: Buat satu diagram Mermaid flowchart tingkat tinggi (high-level) yang menggambarkan alur kerja keseluruhan sistem dari pelanggan datang → pilih layanan → proses per modul → pembayaran → rekonsiliasi → laporan. Diagram ini harus menunjukkan bagaimana 10 modul saling terhubung.
  - [ ] B.4.2. **2.2 Peta Keterhubungan Workflow antar Modul**: Buat diagram Mermaid yang menunjukkan relasi input-output antar modul (misal: output M.1 Transaksi menjadi input M.5 Antrian dan M.4 Poin Insentif).

- [ ] **B.5. Bab 3 — Workflow Diagram Proses Bisnis As-Is** — Untuk setiap divisi (6 sub-bab):
  - [ ] B.5.1. Buat diagram Mermaid flowchart yang memodelkan alur kerja **manual saat ini** berdasarkan data dari BRD Bagian 4.1 dan narasi.txt.
  - [ ] B.5.2. Setiap diagram harus menunjukkan: aktor tunggal (pemilik), langkah kerja berurutan, penggunaan Excel manual, dan titik kelemahan (pain point) yang ditandai dengan warna/catatan khusus.
  - [ ] B.5.3. Di bawah setiap diagram, tambahkan paragraf naratif singkat yang menjelaskan bottleneck dan pain point spesifik pada alur tersebut.

- [ ] **B.6. Bab 4 — Workflow Diagram Proses Bisnis To-Be** — Ini adalah **inti utama** dokumen. Untuk setiap modul dan sub-alurnya:
  - [ ] B.6.1. **4.1 Workflow Operasional Harian Toko**: Buat diagram master alur operasi harian (opening → login → dashboard → transaksi → closing → rekonsiliasi → logout).
  - [ ] B.6.2. **4.2 s.d 4.11 — Workflow per Modul**: Untuk setiap modul (M.1 s.d M.10), buat diagram Mermaid per sub-alur berdasarkan data dari:
    - Main Flow setiap Use Case terkait (dari UCD).
    - Logika Proses/Bisnis dari setiap SRS-F-XXX terkait (dari SRS).
    - Aturan Bisnis dari setiap BR-F-XX terkait (dari BRD).
  - [ ] B.6.3. Setiap diagram workflow **wajib memuat**:
    - **Aktor/Swimlane** yang jelas (siapa yang melakukan langkah tersebut).
    - **Decision Diamond** untuk setiap percabangan logika (if/else).
    - **Subprocess** yang mereferensikan workflow lain jika ada relasi `<<include>>`.
    - **Exception Path** untuk penanganan error (merujuk kode error SRS).
    - **Status Transisi** (khususnya untuk Job Tracking 5 status di M.5).
    - **Catatan Aturan Bisnis** yang relevan di dalam diagram (misal: ambang batas Rp 150.000 untuk alert PPOB).
  - [ ] B.6.4. Di bawah setiap diagram, tambahkan **narasi prosedural** yang menjelaskan langkah demi langkah alur tersebut dalam bentuk numbered list.
  - [ ] B.6.5. Cantumkan **referensi derivasi** (UC-ID, BR-F-XX, SRS-F-XXX) untuk setiap workflow.

- [ ] **B.7. Bab 5 — Workflow Diagram Proses Lintas Modul** — Tulis 3 workflow integrasi:
  - [ ] B.7.1. **5.1 Pesanan Cetak Kustom End-to-End**: Buat diagram alur lengkap yang menghubungkan M.1 → M.5 → M.2 → M.4 → M.7 → M.6. Ini menggambarkan alur pesanan kustom dari awal hingga akhir melewati banyak modul.
  - [ ] B.7.2. **5.2 Pengadaan Barang & Manajemen Supplier End-to-End**: Buat diagram alur yang menghubungkan M.2 (prediksi re-order → supplier → price tracking → pembelian → utang → barang masuk → stock opname).
  - [ ] B.7.3. **5.3 Penutupan Hari Operasional (End-of-Day)**: Buat diagram alur dari M.7 (rekonsiliasi kas → serah terima shift) → M.4 (absensi → poin) → M.6 (laporan harian pemilik).

- [ ] **B.8. Bab 6 — Matriks Traceability Workflow** — Buat tabel mapping dua arah:
  - [ ] B.8.1. Kolom: ID Workflow Diagram, Nama Workflow, UC-ID Terkait, BR-F-XX Terkait, SRS-F-XXX Terkait, Modul, Status Kelengkapan.
  - [ ] B.8.2. Pastikan setiap UC dari UCD (UC-001 s.d UC-044) tercakup minimal dalam satu workflow diagram.
  - [ ] B.8.3. Pastikan setiap BR-F dari BRD tercakup minimal dalam satu workflow diagram.

- [ ] **B.9. Bab 7 — Penanganan Kondisi Khusus & Percabangan Pengecualian** — Tulis:
  - [ ] B.9.1. **7.1 Daftar Decision Point Kritis**: Buat tabel yang mencantumkan setiap titik keputusan penting pada diagram, kondisi percabangan (true/false), dan aksi yang diambil sistem.
  - [ ] B.9.2. **7.2 Daftar Exception Flow pada Workflow**: Buat tabel yang mencantumkan kode error SRS (misal: ERR-DB-001, ERR-STOCK-010), nama workflow terkait, dan aksi recovery yang dilakukan.

- [ ] **B.10. Bab 8 — Glosarium Istilah Workflow** — Tulis daftar alfabetis istilah workflow modeling dan domain bisnis percetakan yang digunakan dalam dokumen (misal: Activity Diagram, Swimlane, Decision Node, Flowchart, BPMN, Subprocess, Pain Point, As-Is, To-Be, dll). Pastikan tidak menduplikasi definisi yang sudah ada di dokumen sebelumnya kecuali konteksnya berbeda.

- [ ] **B.11. Bab 9 — Referensi Dokumen** — Tulis tabel daftar berkas referensi yang digunakan. Formatnya konsisten dengan dokumen SDLC sebelumnya:
  | # | Nama Berkas Referensi | Lokasi Path Relatif | Keterangan |
  |---|---|---|---|
  | ... | ... | ... | ... |

---

### FASE C — Validasi & Penulisan ke Target File

- [ ] **C.1.** Lakukan validasi kelengkapan: periksa apakah setiap UC (UC-001 s.d UC-044) sudah tercakup dalam minimal satu workflow diagram. Jika ada yang terlewat, tambahkan workflow-nya.

- [ ] **C.2.** Lakukan validasi kelengkapan: periksa apakah setiap BR-F (BR-F-01 s.d BR-F-40) sudah tercakup dalam minimal satu workflow diagram. Jika ada yang terlewat, tambahkan workflow-nya.

- [ ] **C.3.** Lakukan validasi konsistensi: periksa apakah aktor pada setiap swimlane workflow sesuai dengan matriks RBAC di BRD dan matriks UC ↔ Aktor di UCD.

- [ ] **C.4.** Lakukan validasi: pastikan setiap diagram Mermaid memiliki sintaks yang valid dan bisa di-render tanpa error (node IDs tidak duplikat, label tidak mengandung karakter khusus yang merusak rendering, subgraph tertutup dengan `end`).

- [ ] **C.5.** Lakukan validasi: pastikan tidak ada data yang hilang. Jika ada data tertentu yang **tidak ditemukan** di file referensi namun diperlukan oleh dokumen ini, tandai dengan format berikut:
  ```
  > ⚠️ DATA TIDAK TERSEDIA: [Deskripsi data yang kosong dan perlu diisi manual oleh pemilik usaha atau didefinisikan di tahap selanjutnya.]
  ```

- [ ] **C.6.** Lakukan review bahasa: pastikan seluruh narasi menggunakan **Bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan**, dan mudah dipahami. Hindari kalimat panjang berbelit-belit. Gunakan kalimat aktif dengan subjek yang jelas.

- [ ] **C.7.** Tulis seluruh hasil dokumen final ke target file: `docs/sdlc/02_analysis/04_workflow_diagram.md`

- [ ] **C.8.** Verifikasi bahwa file sudah tertulis dengan benar di lokasi yang tepat.

---

## 6. Instruksi Tambahan Spesifik Workflow Diagram

Berikut adalah instruksi tambahan yang **wajib dipatuhi** karena merupakan kaidah standar dan ciri khas khusus dokumen Workflow Diagram:

### 6.1. Kaidah Pembuatan Diagram Mermaid
- [ ] Gunakan **sintaks `flowchart TD`** (Top-Down) sebagai default untuk workflow vertikal sekuensial.
- [ ] Gunakan **sintaks `flowchart LR`** (Left-Right) untuk workflow horizontal yang menunjukkan interaksi antar-modul atau swimlane.
- [ ] Untuk diagram yang kompleks, pertimbangkan menggunakan **`subgraph`** Mermaid untuk mewakili swimlane per aktor atau per modul.
- [ ] Gunakan bentuk node yang konsisten: `[Proses]` untuk aksi, `{Keputusan}` untuk decision, `([Start/End])` untuk terminal, `[[Subprocess]]` untuk pemanggilan workflow lain.
- [ ] Berikan **styling warna** yang konsisten untuk membedakan aktor/peran (misal: pemilik = hijau, kasir = biru, gudang = oranye, sistem = abu-abu).
- [ ] Setiap diagram workflow wajib memiliki **satu node Start dan minimal satu node End** yang jelas.

### 6.2. Kaidah Konsistensi Naming
- [ ] Berikan **ID unik** pada setiap workflow diagram (misal: `WF-M1-01`, `WF-M2-03`, `WF-CROSS-01`) untuk referensi pada matriks traceability.
- [ ] Gunakan penamaan node yang deskriptif dan konsisten di seluruh dokumen.

### 6.3. Kaidah Perbandingan As-Is vs To-Be
- [ ] Pada Bab 3 (As-Is), tunjukkan secara visual **titik-titik kelemahan** (pain points) dengan catatan merah atau penanda khusus pada diagram.
- [ ] Pada Bab 4 (To-Be), tunjukkan bagaimana **setiap pain point tersebut teratasi** oleh alur kerja baru yang diotomasi sistem.
- [ ] Pastikan ada korelasi yang jelas dan dapat ditelusuri antara setiap workflow As-Is dan workflow To-Be pasangannya.

### 6.4. Kaidah Kelengkapan Isi
- [ ] Pastikan kualitas dan kelengkapan isi dokumen ini **final dan definitif** sehingga tidak menimbulkan pertanyaan atau interupsi di fase SDLC selanjutnya.
- [ ] Dokumen ini harus **layak menjadi referensi, acuan, dan input utama** bagi:
  - System Design Document (SDD) — Fase 03 Design
  - Entity Relationship Diagram (ERD) — Fase 03 Design
  - Database Schema — Fase 03 Design
  - Sequence Diagram — Fase 03 Design
  - Test Plan & Test Cases — Fase 05 Testing
- [ ] Setiap alur yang melibatkan **transaksi keuangan** (kas laci, pinjaman, penggajian, retur) harus menunjukkan secara eksplisit di mana uang masuk dan uang keluar pada diagram.
- [ ] Setiap alur yang melibatkan **perubahan stok** (BOM, limbah, opname, ATK internal) harus menunjukkan secara eksplisit di mana stok bertambah atau berkurang.

### 6.5. Kaidah Kualitas Produksi
- [ ] Hindari diagram yang terlalu padat. Jika satu diagram memiliki lebih dari 15-20 node, pecah menjadi beberapa sub-diagram yang saling mereferensikan via node `[[Subprocess]]`.
- [ ] Setiap diagram yang menggambarkan proses yang sama di modul berbeda harus **konsisten** dalam level detail dan gaya visual.

---

## 7. Kriteria Penerimaan Dokumen (Definition of Done)

Dokumen Workflow Diagram dinyatakan **selesai dan layak** jika memenuhi seluruh kriteria berikut:

| # | Kriteria | Status |
|---|----------|--------|
| 1 | Seluruh 6 alur kerja As-Is (BRD Bab 4.1) termodelkan dalam diagram Mermaid. | `[ ]` |
| 2 | Seluruh alur kerja To-Be mencakup 10 modul fungsional (M.1 s.d M.10). | `[ ]` |
| 3 | Setiap workflow To-Be memiliki diagram Mermaid yang valid dan renderabel. | `[ ]` |
| 4 | Setiap workflow To-Be memiliki narasi prosedural penjelasan langkah. | `[ ]` |
| 5 | Seluruh 44 Use Case (UC-001 s.d UC-044) tercakup dalam matriks traceability. | `[ ]` |
| 6 | Seluruh BR-F (BR-F-01 s.d BR-F-40) tercakup dalam matriks traceability. | `[ ]` |
| 7 | Minimal 3 workflow lintas modul (cross-module) disusun lengkap. | `[ ]` |
| 8 | Daftar decision point kritis dan exception flow terisi lengkap. | `[ ]` |
| 9 | Data yang tidak tersedia ditandai dengan format `⚠️ DATA TIDAK TERSEDIA`. | `[ ]` |
| 10 | Bahasa Indonesia natural, tidak ambigu, dan mudah dipahami. | `[ ]` |
| 11 | Front matter YAML, riwayat perubahan, dan referensi terisi lengkap. | `[ ]` |
| 12 | File tertulis di lokasi: `docs/sdlc/02_analysis/04_workflow_diagram.md`. | `[ ]` |

---

## 8. Catatan Penting

> **PERHATIAN UNTUK PELAKSANA (Junior Programmer / LLM AI):**
>
> 1. **Jangan mengarang data.** Seluruh konten harus bersumber dari file referensi yang disebutkan di Bab 3. Jika data tidak ditemukan, gunakan penanda `⚠️ DATA TIDAK TERSEDIA`.
> 2. **Jangan melewatkan detail.** Setiap langkah dalam Main Flow, Alternative Flow, dan Exception Flow dari UCD harus tergambar dalam workflow diagram.
> 3. **Jangan menyederhanakan diagram secara berlebihan.** Diagram harus cukup detail untuk menjadi acuan perancangan sistem, namun tidak boleh terlalu rumit sehingga tidak terbaca.
> 4. **Pastikan konsistensi istilah.** Gunakan nama aktor, status, dan kode yang sama persis dengan yang digunakan di BRD, SRS, dan UCD.
> 5. **Ikuti urutan eksekusi.** Kerjakan FASE A (baca semua referensi) terlebih dahulu sebelum mulai menulis FASE B, dan validasi di FASE C setelah penulisan selesai.
> 6. **File ini menandai selesainya Fase 02 Analysis.** Kualitasnya harus setara dan konsisten dengan 3 dokumen analysis sebelumnya (BRD, SRS, UCD).

---