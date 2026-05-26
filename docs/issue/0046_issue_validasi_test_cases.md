---
judul         : Validasi & Penyempurnaan Dokumen Test Cases
dokumen_target: docs/sdlc/05_testing/02_test_cases.md
lokasi_ref    : docs/sdlc/
tanggal       : 2026-05-26
status        : Open
prioritas     : High
dibuat_oleh   : Senior QA Architect & SDLC Documentation Lead
---

# Validasi & Penyempurnaan Dokumen Test Cases

## Ringkasan Masalah

Dokumen **Test Cases v1.0** (`docs/sdlc/05_testing/02_test_cases.md`) telah dibuat sebagai penjabaran operasional dari 44 skenario uji yang ada di **Test Plan v1.1**. Sebelum dokumen ini digunakan sebagai acuan utama untuk pembuatan **Test Scripts (pytest)** dan **Test Report**, dokumen ini wajib diaudit secara menyeluruh untuk memastikan kelengkapan, konsistensi, dan kualitasnya memenuhi standar praktik industri perangkat lunak yang sesungguhnya.

Issue ini memerintahkan pelaksana untuk melakukan audit, validasi, perbaikan, dan penulisan ulang penuh (*full overwrite*) dokumen Test Cases ke versi **v1.1**.

---

## Persona Pelaksana

> [!IMPORTANT]
> Sebelum memulai pekerjaan apapun, adopsi dan pertahankan **persona** berikut ini selama keseluruhan proses pelaksanaan issue ini:

Kamu adalah seorang **Principal QA Architect & SDLC Documentation Auditor** dengan pengalaman lebih dari 15 tahun dalam industri pengembangan perangkat lunak keuangan (*fintech*) dan sistem manajemen usaha (*ERP/POS*). Kamu memiliki keahlian mendalam dalam:

- **IEEE 829 Standard** untuk dokumentasi pengujian perangkat lunak.
- **Test Case Design Techniques**: Equivalence Partitioning, Boundary Value Analysis, Decision Table Testing, State Transition Testing.
- **ISTQB (International Software Testing Qualifications Board)** — level Advanced Test Analyst.
- **Python testing ecosystem**: `pytest`, `pytest-mock`, `coverage.py`, `hypothesis` (property-based testing).
- **Validasi presisi desimal** pada sistem keuangan (`Python Decimal`, `ROUND_HALF_UP`, `Decimal(15,4) MySQL`).
- **Audit keamanan RBAC**, JWT token lifecycle, dan audit trail integritas.
- **Kepatuhan regulasi data** (UU PDP Indonesia No. 27 Tahun 2022).

Dengan persona ini, kamu **tidak toleran** terhadap ambiguitas, data kosong yang tidak terisi, error code yang tidak konsisten, atau langkah uji yang tidak dapat dieksekusi secara deterministik oleh siapapun — baik junior programmer maupun AI agent.

---

## Informasi Konteks

| Atribut | Detail |
|---|---|
| **Dokumen Utama (Target)** | `docs/sdlc/05_testing/02_test_cases.md` |
| **Versi Saat Ini** | 1.0 |
| **Versi Target Setelah Revisi** | 1.1 |
| **Posisi dalam SDLC** | Fase 05 — Testing (Deliverable ke-2 setelah Test Plan) |
| **Dokumen Sebelumnya** | Test Plan v1.1 (`docs/sdlc/05_testing/01_test_plan.md`) |
| **Dokumen Sesudahnya** | Test Scripts (pytest) & Test Report |
| **Lokasi Referensi** | `docs/sdlc/` (seluruh subdirektori) |

---

## Daftar File Referensi yang Wajib Dibaca

Berikut adalah seluruh file referensi yang **WAJIB** dibaca sebelum memulai analisis. Tandai setiap file yang telah selesai dibaca.

| No | Kode Ref | Path File | Keterangan |
|----|----------|-----------|------------|
| 1 | **R-TP** | `docs/sdlc/05_testing/01_test_plan.md` | Sumber utama 44 skenario uji, error mapping, fixtures |
| 2 | **R-SRS** | `docs/sdlc/02_analysis/02_software_requirements.md` | Batasan input, logika bisnis, parameter data |
| 3 | **R-UC** | `docs/sdlc/02_analysis/03_use_case_diagram.md` | Alur naratif main, alternatif, dan exception |
| 4 | **R-ACM** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Hak otorisasi RBAC biner per peran |
| 5 | **R-SEC** | `docs/sdlc/03_design/06_security_design.md` | Spesifikasi teknis keamanan sistem |
| 6 | **R-BOM** | `docs/sdlc/03_design/05_bom_hpp_design.md` | Formula HPP dan BOM pemakaian bahan |
| 7 | **R-CLI** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur interaksi CLI, breadcrumb, format struk |
| 8 | **R-DB** | `docs/sdlc/03_design/01_database_schema.sql` | Skema tabel, constraint, tipe data `DECIMAL(15,4)` |
| 9 | **R-ERD** | `docs/sdlc/03_design/02_erd_database.md` | Relasi antar entitas basis data |

> [!NOTE]
> Jika selama proses analisis ditemukan file referensi lain yang relevan di luar daftar di atas (misalnya dokumen arsitektur sistem, API design, atau infrastructure plan), catat dan tambahkan ke daftar referensi di bagian akhir dokumen target.

---

## Instruksi Pelaksanaan — Tahapan Wajib

Ikuti setiap tahapan di bawah ini secara **berurutan dari atas ke bawah**. Jangan melompati tahapan. Setiap tahapan memiliki sub-tugas bertanda checklist `[ ]` yang wajib diselesaikan sebelum melanjutkan ke tahapan berikutnya.

---

### TAHAP 0: Persiapan & Pembacaan Awal

**Tujuan**: Membangun pemahaman menyeluruh tentang dokumen target dan seluruh referensinya sebelum melakukan analisis apapun.

- [ ] **0.1** — Baca dokumen target dari baris pertama hingga terakhir: `docs/sdlc/05_testing/02_test_cases.md`. Jangan lewati bagian apapun. Perhatikan secara khusus:
  - Jumlah total kasus uji yang diklaim (cek konsistensi antara Bab 2 dan kasus uji aktual di Bab 4-18).
  - Seluruh kode error yang digunakan (format `ERR-XXX-YYY`).
  - Seluruh referensi SRS (`SRS-F-XXX`) dan Use Case (`UC-XXX`) yang disebut.
  - Kolom "Hasil / Status Uji" — apakah ada yang kosong atau berisi placeholder.
  - Bagian yang menggunakan format ringkasan (non-tabel) vs. format tabel lengkap.

- [ ] **0.2** — Baca dokumen **R-TP** (`docs/sdlc/05_testing/01_test_plan.md`) dari awal hingga akhir. Catat:
  - Jumlah total skenario uji (target: 44 skenario dari M1 hingga M10 + SEC + DEC + INT + CLI + NF).
  - Daftar lengkap kode error yang terdefinisi di Test Plan.
  - Data fixtures global yang digunakan.
  - Setiap batasan teknis dan parameter spesifik yang disebutkan.

- [ ] **0.3** — Baca dokumen **R-SRS** (`docs/sdlc/02_analysis/02_software_requirements.md`). Catat:
  - Seluruh kode `SRS-F-XXX` yang ada.
  - Batasan input (format, tipe data, range nilai).
  - Aturan bisnis spesifik (threshold, limit, formula kalkulasi).

- [ ] **0.4** — Baca dokumen **R-UC** (`docs/sdlc/02_analysis/03_use_case_diagram.md`). Catat:
  - Seluruh kode `UC-XXX` yang ada.
  - Alur utama (*main flow*), alternatif (*alternative flow*), dan pengecualian (*exception flow*) untuk setiap Use Case.
  - Aktor yang terlibat di setiap Use Case.

- [ ] **0.5** — Baca dokumen **R-ACM** (`docs/sdlc/02_analysis/06_access_control_matrix.md`). Catat:
  - Matriks hak akses setiap peran (pemilik, kepala_percetakan, kasir, desainer, produksi_cetak, gudang, pramuniaga, fotocopy_print).
  - Menu/fitur mana yang restricted per peran.

- [ ] **0.6** — Baca dokumen **R-SEC** (`docs/sdlc/03_design/06_security_design.md`). Catat:
  - Spesifikasi teknis bcrypt (cost factor), JWT (algoritma, expiry).
  - Aturan brute-force lockout (jumlah percobaan, durasi lock).
  - Spesifikasi enkripsi backup (AES-256, ZIP password).
  - Spesifikasi enkripsi data sensitif (Fernet).

- [ ] **0.7** — Baca dokumen **R-BOM** (`docs/sdlc/03_design/05_bom_hpp_design.md`). Catat:
  - Formula kalkulasi HPP BOM secara detail.
  - Contoh data BOM yang ada (nama bahan, pemakaian, harga beli satuan).
  - Presisi desimal yang digunakan dalam formula.

- [ ] **0.8** — Baca dokumen **R-CLI** (`docs/sdlc/03_design/04_cli_interaction_flow.md`). Catat:
  - Format lebar karakter struk thermal (32 char, 48 char, dll.).
  - Konvensi breadcrumb navigasi.
  - Konvensi warna ANSI (hijau = sukses, kuning = peringatan, merah = error).

- [ ] **0.9** — Baca dokumen **R-DB** (`docs/sdlc/03_design/01_database_schema.sql`). Catat:
  - Nama tabel yang benar-benar ada di skema (untuk validasi referensi nama tabel di test cases).
  - Tipe data kolom keuangan (harus `DECIMAL(15,4)`).
  - Constraint yang ada (PRIMARY KEY, UNIQUE KEY, FOREIGN KEY, CHECK).
  - Nama kolom yang tepat (untuk validasi referensi kolom di test cases).

- [ ] **0.10** — Baca dokumen **R-ERD** (`docs/sdlc/03_design/02_erd_database.md`). Catat:
  - Relasi antar tabel yang relevan dengan test cases (misalnya: `transaksi` ↔ `transaksi_item` ↔ `barang`).

---

### TAHAP 1: Validasi Kelengkapan Data vs. Referensi

**Tujuan**: Memastikan dokumen Test Cases merangkum **semua** data dan informasi yang relevan dari seluruh dokumen referensi, dan tidak ada yang terlewat.

- [ ] **1.1** — **Cek kelengkapan cakupan skenario**:
  - Bandingkan daftar 44 skenario di Test Plan (R-TP) dengan skenario yang tercakup di Test Cases (Bab 4-13).
  - Buat daftar skenario yang ada di Test Plan tetapi **tidak** memiliki kasus uji yang terdokumentasi di Test Cases.
  - Contoh yang perlu dicek: M2-TC-003, M2-TC-004, M2-TC-006 s.d M2-TC-009, M3-TC-002, M3-TC-003, M4-TC-004, M4-TC-005, M5-TC-002, M5-TC-003, M6-TC-001 s.d M6-TC-004, M7-TC-003, M7-TC-004, M7-TC-005, M7-TC-007, M8-TC-001, M8-TC-002, M9-TC-001, M10-TC-001 — apakah semuanya sudah terwakili secara memadai?

- [ ] **1.2** — **Cek konsistensi jumlah kasus uji**:
  - Hitung secara manual jumlah kasus uji aktual yang ada di Bab 4-18 (setiap blok tabel atau sub-item bernomor ID dihitung sebagai 1 kasus uji).
  - Bandingkan dengan angka yang diklaim di Bab 2.1 (tabel distribusi per modul) dan Bab 19.5 (coverage summary).
  - Jika ada selisih, catat skenario mana yang menyebabkan diskrepansi jumlah.

- [ ] **1.3** — **Cek kelengkapan kode error**:
  - Bandingkan daftar kode error di Bab 19.4 dengan daftar kode error lengkap yang ada di Test Plan (R-TP).
  - Identifikasi kode error yang ada di Test Plan tetapi belum memiliki kasus uji validasi di Test Cases.
  - Identifikasi kode error yang disebutkan di dalam langkah uji / hasil diharapkan tetapi tidak ada di Bab 19.4.

- [ ] **1.4** — **Cek kelengkapan referensi SRS**:
  - Bandingkan seluruh kode `SRS-F-XXX` yang dirujuk di Test Cases (Bab 4-18) dengan seluruh kode `SRS-F-XXX` yang ada di dokumen SRS (R-SRS).
  - Identifikasi SRS requirement yang tidak memiliki kasus uji sama sekali.

- [ ] **1.5** — **Cek kelengkapan referensi Use Case**:
  - Bandingkan seluruh kode `UC-XXX` yang dirujuk di Test Cases dengan seluruh `UC-XXX` yang ada di dokumen Use Case (R-UC).
  - Identifikasi Use Case yang tidak memiliki kasus uji sama sekali, terutama *exception flow* dan *alternative flow*.

- [ ] **1.6** — **Cek kelengkapan data fixtures**:
  - Bandingkan data test fixtures di Bab 3.3 (8 akun uji) dan Bab 20.2 (seed data tabel) dengan data fixtures yang dirujuk di Test Plan (R-TP).
  - Apakah ada fixtures yang dirujuk dalam kasus uji tetapi tidak didefinisikan di Bab 3.3 atau 20.2?

- [ ] **1.7** — **Cek konsistensi data numerik kritis**:
  - Verifikasi semua nilai kalkulasi desimal yang ada di kasus uji terhadap formula yang ada di R-BOM dan R-SRS:
    - TC-M2-002-01: HPP BOM = `Decimal('4750.0000')` → hitung ulang: `0.0025 × 100000 + 1.0 × 4500 = 250 + 4500 = 4750` ✓
    - TC-M4-002-01: Payroll = `Decimal('600000.0000')` → hitung ulang: `12000000 × 25% / 5 = 3000000 / 5 = 600000` ✓
    - TC-M4-003-01: UMR Protection = `Decimal('1600000.0000')` → `50% × 3200000 = 1600000` ✓
    - TC-DEC-002-01: Pembulatan val1, val2, val3 — verifikasi logika `ROUND_HALF_UP` sudah benar.
    - TC-DEC-003-01: Saldo akhir `Decimal('506980.0000')` → hitung: `500000 + 1523.1234 + 2456.8766 + 3000 = 506980.0000` ✓
  - Tandai setiap kalkulasi yang hasilnya keliru atau ambigu.

---

### TAHAP 2: Validasi Relevansi & Kebersihan Konten

**Tujuan**: Memastikan dokumen Test Cases **hanya** berisi data dan informasi yang spesifik diperlukan oleh dokumen ini — tidak lebih, tidak kurang — sehingga dokumen ini bersih dan fokus.

- [ ] **2.1** — **Cek kesesuaian tipe konten**:
  - Identifikasi apakah ada konten yang seharusnya ada di dokumen lain (misalnya: kode implementasi Python, DDL SQL lengkap, wireframe UI) yang tidak relevan untuk dimasukkan ke dalam Test Cases.
  - Konten yang boleh ada: data uji (test data), langkah uji (test steps), hasil diharapkan (expected results), prakondisi, aktor, referensi SRS/UC.
  - Konten yang **tidak boleh** ada secara berlebihan: dokumentasi arsitektur sistem, kode sumber program, penjelasan mendalam tentang konsep teknis yang bukan bagian dari prosedur uji.

- [ ] **2.2** — **Cek duplikasi konten**:
  - Identifikasi kasus uji yang secara substansial menduplikasi kasus uji lain (langkah uji identik, data uji identik, hasil diharapkan identik) dengan hanya perbedaan minor yang tidak signifikan.
  - Kasus duplikasi yang murni *cross-reference* (misalnya TC-CLI-003 yang merujuk ke TC-M1-007-01) adalah **wajar** dan tidak perlu diubah.

- [ ] **2.3** — **Cek relevansi data uji**:
  - Untuk setiap kasus uji, verifikasi apakah data uji (*test data*) yang diberikan benar-benar relevan dengan skenario yang diuji.
  - Contoh yang perlu dicek: apakah `kode_barang = 'BRG-009'` di TC-M2-001-01 konsisten dengan seed data di Bab 20.2?
  - Apakah nomor `transaksi_id`, `opname_id`, `antrian_id` yang digunakan di kasus uji berbeda tidak saling bertabrakan (collision) satu sama lain?

- [ ] **2.4** — **Cek konsistensi format seksi spesial**:
  - Bab 14-17 (SEC, DEC, INT, CLI) menggunakan format berbeda (bullet point) dibandingkan Bab 4-13 (format tabel). Evaluasi apakah inkonsistensi format ini mengurangi keterbacaan dan kemudahan eksekusi.
  - Pertimbangkan untuk menstandarisasi format kasus uji yang masih menggunakan *bullet point* non-tabel ke format tabel yang konsisten (minimal menyertakan: ID, Langkah Uji, Expected Result secara terstruktur).

- [ ] **2.5** — **Cek kelengkapan atribut setiap kasus uji**:
  - Setiap kasus uji yang menggunakan format tabel harus memiliki semua atribut berikut (tidak boleh ada yang kosong atau berisi `*[Diisi saat eksekusi]*` untuk kolom definitif):
    - `ID Kasus Uji` — harus berformat `TC-[MODUL]-[SKENARIO]-[URUT]`
    - `Skenario Asal` — harus ada referensi ke ID skenario Test Plan
    - `Referensi SRS / UC` — harus ada minimal 1 referensi valid
    - `Modul / Fitur` — harus diisi
    - `Tipe / Tingkat / Pri` — harus diisi (Functional/Security/Precision/Boundary/Database/CLI)
    - `Peran Aktor` — harus diisi dengan peran sistem yang valid
    - `Prakondisi` — harus spesifik dan dapat diverifikasi
    - `Data Uji` — harus berisi nilai konkret (bukan placeholder)
    - `Langkah Uji` — harus deterministik, urut, dan dapat dieksekusi langkah per langkah
    - `Hasil Diharapkan` — harus spesifik, terukur, dan verifiable
    - `Hasil / Status Uji` — boleh berisi `*[Diisi saat eksekusi]*` (ini memang kolom runtime)
  - Tandai setiap atribut yang kosong atau tidak terisi dengan benar.

---

### TAHAP 3: Validasi Standar Struktur Dokumen

**Tujuan**: Memastikan dokumen memiliki struktur yang sesuai standar industri dokumentasi pengujian perangkat lunak (IEEE 829 / ISTQB).

- [ ] **3.1** — **Cek kelengkapan header dokumen**:
  - Pastikan frontmatter YAML berisi: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`.
  - Pastikan `Riwayat Perubahan Dokumen` (changelog) ada dan diisi dengan benar.

- [ ] **3.2** — **Cek kelengkapan Bab 1 (Informasi Dokumen)**:
  - Verifikasi bahwa semua sub-bab berikut ada dan terisi lengkap:
    - 1.1 Tujuan Dokumen
    - 1.2 Cakupan Dokumen
    - 1.3 Posisi Dokumen dalam SDLC
    - 1.4 Hubungan dengan Dokumen SDLC Lainnya
    - 1.5 Audiens Target
    - 1.6 Definisi, Akronim, dan Singkatan
    - 1.7 Konvensi Penulisan Test Case

- [ ] **3.3** — **Cek kelengkapan Bab 2 (Ringkasan Cakupan)**:
  - Verifikasi tabel distribusi kasus uji per modul sudah akurat dan jumlahnya konsisten dengan kasus uji aktual.
  - Verifikasi distribusi per tipe, prioritas, dan tingkat pengujian.

- [ ] **3.4** — **Cek kelengkapan Bab 3 (Lingkungan & Prakondisi Global)**:
  - Spesifikasi lingkungan (OS, Python version, MySQL version, hardware) harus spesifik dan konsisten dengan R-TP.
  - Prakondisi global (inisialisasi DB, seed fixtures, flag `--env=test`) harus dapat dieksekusi secara deterministik.
  - Data fixtures global (Bab 3.3) harus mencakup semua akun uji yang dibutuhkan di seluruh kasus uji.

- [ ] **3.5** — **Cek kelengkapan Bab 19 (Matriks Ketertelusuran)**:
  - Pastikan Bab 19.1 (TC → Test Plan) mencakup **seluruh** kasus uji yang ada di dokumen, bukan hanya sebagian.
  - Pastikan Bab 19.2 (TC → SRS) mencakup referensi yang representatif untuk setiap requirement fungsional kritis.
  - Pastikan Bab 19.3 (TC → Use Case) mencakup mapping yang representatif.
  - Pastikan Bab 19.4 (TC → Kode Error) mencakup **seluruh** kode error yang digunakan di seluruh kasus uji, tidak ada yang tertinggal.
  - Pastikan Bab 19.5 (Coverage Summary) memiliki angka statistik yang akurat dan konsisten.

- [ ] **3.6** — **Cek kelengkapan Bab 20 (Lampiran)**:
  - Pastikan Bab 20.1 (Glosarium) mencakup semua istilah teknis yang digunakan di dokumen ini.
  - Pastikan Bab 20.2 (Seed Data) menyertakan contoh data yang cukup untuk semua modul yang membutuhkan data awal.
  - Pastikan Bab 20.3 (Template Defect Report) lengkap dan dapat langsung digunakan.

- [ ] **3.7** — **Cek kelengkapan Bab 21 (Referensi)**:
  - Pastikan seluruh dokumen yang dijadikan referensi sudah terdaftar di tabel referensi.
  - Pastikan path file sudah benar dan versi dokumen sudah sesuai.

- [ ] **3.8** — **Cek kelengkapan khusus dokumen Test Cases**:
  - Apakah ada bagian **Entry Criteria** dan **Exit Criteria** untuk keseluruhan pengujian? Ini adalah elemen standar ISTQB/IEEE 829 untuk dokumen test cases level sistem.
  - Apakah ada bagian **Test Execution Order / Dependency** yang mendokumentasikan urutan eksekusi yang disarankan (terutama untuk kasus uji yang memiliki dependensi satu sama lain)?
  - Jika belum ada, tambahkan kedua bagian ini.

---

### TAHAP 4: Validasi Kelayakan sebagai Referensi SDLC Berikutnya

**Tujuan**: Memastikan dokumen ini dapat berfungsi sebagai input utama yang andal bagi fase SDLC selanjutnya (Test Scripts & Test Report) tanpa menimbulkan pertanyaan atau keambiguan yang menghambat pekerjaan.

- [ ] **4.1** — **Cek kelayakan sebagai input Test Scripts (pytest)**:
  - Setiap kasus uji harus memiliki `Data Uji` yang cukup konkret untuk diterjemahkan menjadi parameter fungsi `pytest`.
  - Setiap `Langkah Uji` harus dapat dipetakan ke pemanggilan fungsi Python yang spesifik.
  - Setiap `Hasil Diharapkan` harus dapat diformulasikan menjadi assertion `assert` yang definitif.
  - Identifikasi kasus uji yang `Langkah Uji`-nya masih terlalu abstrak atau ambigu untuk diimplementasikan.

- [ ] **4.2** — **Cek kelayakan sebagai input Test Report**:
  - Kolom `Hasil / Status Uji` harus dalam format yang dapat diisi langsung saat eksekusi (`PASS` / `FAIL` / `BLOCKED` / `SKIP`).
  - ID kasus uji harus konsisten dan unik sehingga Test Report dapat merujuk kembali ke Test Cases secara tepat.

- [ ] **4.3** — **Cek kelayakan sebagai referensi UAT (User Acceptance Testing)**:
  - Kasus uji yang bertipe UAT (kelayakan bisnis pemilik) harus ditulis dalam bahasa yang dapat dipahami oleh pemilik usaha non-teknis.
  - Identifikasi kasus uji UAT yang menggunakan jargon teknis berlebihan yang perlu disederhanakan.

- [ ] **4.4** — **Cek dependency antar kasus uji**:
  - Identifikasi kasus uji yang memiliki dependensi pada hasil kasus uji lain (misalnya TC-M1-001-02 bergantung pada TC-INT-001-02).
  - Pastikan dependensi tersebut sudah dicatat di kolom `Catatan Tambahan` dengan format yang jelas.
  - Tambahkan catatan dependensi yang belum terdokumentasi.

---

### TAHAP 5: Validasi Kualitas Bahasa Indonesia

**Tujuan**: Memastikan seluruh teks dokumen menggunakan bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau AI model yang lebih sederhana.

- [ ] **5.1** — **Cek konsistensi terminologi**:
  - Verifikasi bahwa istilah teknis yang sama selalu menggunakan kata yang sama di seluruh dokumen. Contoh:
    - "kasus uji" vs "test case" — pilih satu dan konsisten.
    - "skenario uji" vs "skenario" — pilih satu dan konsisten.
    - "langkah uji" vs "langkah" — pilih satu dan konsisten.
    - "hasil diharapkan" vs "expected result" vs "ekspektasi" — pilih satu dan konsisten.
    - Nama peran pengguna: "kasir" vs "staf kasir" vs "kasir01" — pastikan konteks jelas.

- [ ] **5.2** — **Cek ketepatan instruksi langkah uji**:
  - Setiap langkah uji harus dimulai dengan kata kerja aktif yang jelas (misalnya: Masuk, Input, Klik, Jalankan, Panggil, Verifikasi, Logout).
  - Langkah uji tidak boleh menggunakan kalimat pasif yang ambigu (misalnya: "data dimasukkan" → ubah menjadi "Masukkan data").
  - Langkah uji tidak boleh mengandung kata "dll." atau "dsb." karena membuat instruksi tidak deterministik.

- [ ] **5.3** — **Cek ketepatan hasil diharapkan**:
  - Setiap `Hasil Diharapkan` harus dapat diverifikasi secara objektif (bukan subjektif).
  - Hindari kata-kata seperti "sesuai", "rapi", "benar", "normal" tanpa kriteria yang terukur.
  - Contoh yang perlu diperbaiki: "tabel terformat rapi" → ubah menjadi "tabel me-render dengan lebar kolom tepat [X] karakter dan tanpa overlapping antar kolom".

- [ ] **5.4** — **Cek kejelasan prakondisi**:
  - Setiap `Prakondisi` harus cukup spesifik untuk diset ulang (*reproducible*) oleh siapapun.
  - Prakondisi tidak boleh bergantung pada state global yang tidak terjelaskan (misalnya: "database dalam kondisi bersih" — perlu dijelaskan bagaimana cara mengembalikan ke kondisi bersih).

- [ ] **5.5** — **Cek kejelasan kode error dalam hasil diharapkan**:
  - Setiap kode error yang muncul di `Hasil Diharapkan` harus berformat standar: `⛔ ERR-XXX-YYY: [pesan lengkap error]`.
  - Verifikasi bahwa format dan teks pesan error di kasus uji konsisten dengan definisi error di Test Plan (R-TP).

---

### TAHAP 6: Validasi Ketuntasan & Tidak Ada Placeholder Kosong

**Tujuan**: Memastikan tidak ada bagian kosong, placeholder yang belum diisi, atau data yang perlu diisi manual (selain kolom runtime eksekusi).

- [ ] **6.1** — **Identifikasi seluruh placeholder non-runtime**:
  - Cari semua teks yang mengandung: `*[Diisi ...]*`, `[TBD]`, `[TODO]`, `N/A`, `—` (tanda hubung tunggal sebagai penanda kosong), atau sel tabel yang benar-benar kosong di luar kolom `Hasil / Status Uji`.
  - Daftar placeholder yang ditemukan dan isi dengan data yang sesuai berdasarkan konteks dokumen dan referensi.

- [ ] **6.2** — **Cek kolom "Catatan Tambahan" yang berisi tanda `-`**:
  - Tanda `-` pada kolom `Catatan Tambahan` dapat dipertahankan jika memang tidak ada catatan tambahan yang relevan.
  - Namun, untuk kasus uji yang memiliki karakteristik khusus (misalnya: dependensi, keterbatasan teknis, asumsi khusus), pastikan catatan tersebut sudah ditambahkan.

- [ ] **6.3** — **Cek referensi "Skenario Asal" yang bernilai `-`**:
  - Di Bab 19.1, beberapa kasus uji (TC-DEC-002-01, TC-INT-001-01, dst.) memiliki kolom "Skenario Asal (Test Plan)" yang berisi `-`. 
  - Cari tahu apakah skenario-skenario tersebut sebenarnya memiliki referensi di Test Plan yang terlewat, atau memang murni kasus uji tambahan yang tidak berasal dari skenario Test Plan.
  - Jika ada referensi yang terlewat, isi dengan referensi yang tepat.
  - Jika memang tidak ada, tambahkan keterangan "Kasus uji tambahan (bukan turunan langsung dari skenario Test Plan)" untuk kejelasan.

- [ ] **6.4** — **Cek data uji yang tidak spesifik**:
  - Identifikasi kasus uji yang menggunakan data uji generik seperti "data yang valid", "nilai yang sesuai", atau "data dummy" tanpa nilai konkret.
  - Ganti dengan nilai konkret berdasarkan fixture data yang sudah didefinisikan di Bab 3.3 dan 20.2.

- [ ] **6.5** — **Cek kelengkapan seed data (Bab 20.2)**:
  - Verifikasi bahwa seed data yang ada di Bab 20.2 cukup untuk mendukung semua kasus uji yang ada (terutama untuk `transaksi_id`, `opname_id`, `antrian_id`, `karyawan_id` yang dirujuk di kasus uji).
  - Jika ada ID yang dirujuk tetapi tidak ada di seed data, tambahkan definisi seed data yang sesuai.

---

### TAHAP 7: Validasi Khusus Karakteristik Dokumen Test Cases

**Tujuan**: Memastikan aspek-aspek teknis yang spesifik untuk dokumen test cases sistem keuangan berbasis CLI sudah divalidasi secara komprehensif.

- [ ] **7.1** — **Validasi konsistensi RBAC di kasus uji**:
  - Untuk setiap kasus uji yang melibatkan hak akses, verifikasi bahwa peran aktor yang diuji konsisten dengan matriks RBAC di R-ACM.
  - Pastikan setiap menu/fitur yang diklaim hanya bisa diakses oleh peran tertentu sudah memiliki kasus uji negatif (akses ilegal) yang memadai.
  - Cek: apakah semua 8 peran pengguna (pemilik, kepala_percetakan, kasir, desainer, produksi_cetak, gudang, pramuniaga, fotocopy_print) sudah terwakili sebagai aktor dalam kasus uji?

- [ ] **7.2** — **Validasi kelengkapan kasus uji presisi desimal**:
  - Verifikasi bahwa semua operasi aritmatika keuangan kritis (HPP BOM, Smart Payroll, mutasi kas, pemotongan stok non-integer) sudah memiliki kasus uji presisi desimal.
  - Verifikasi bahwa kasus uji presisi menggunakan notasi `Decimal('X.XXXX')` secara konsisten (bukan `float`).
  - Verifikasi bahwa kasus uji overflow desimal sudah ada (Bab 15.2 TC-DEC-002-01 val3 = `Decimal('99999999999.9999')`).

- [ ] **7.3** — **Validasi kasus uji integrasi lintas modul**:
  - Kasus uji integrasi (TC-INT-003-01) harus mendokumentasikan secara eksplisit data state awal sebelum eksekusi dan state akhir yang diharapkan di seluruh tabel database yang terpengaruh.
  - Verifikasi bahwa kasus uji integrasi tidak saling bergantung pada state yang diubah oleh kasus uji lain tanpa reset yang jelas.

- [ ] **7.4** — **Validasi kasus uji CLI**:
  - Kasus uji CLI (Bab 17) harus mendefinisikan secara spesifik:
    - Versi terminal yang digunakan (Windows Terminal / CMD / bash).
    - Resolusi atau lebar terminal minimum yang diperlukan.
    - Cara mengukur/memverifikasi output visual secara deterministik (misalnya: menangkap output ke string dan bandingkan karakter per karakter).

- [ ] **7.5** — **Validasi kasus uji keamanan**:
  - Kasus uji SQL Injection (TC-SEC-003-01) harus menyebutkan payload SQL injection yang spesifik (bukan generik).
  - Kasus uji ANSI injection (TC-SEC-005-01) harus menyebutkan urutan escape ANSI spesifik yang diuji.
  - Kasus uji brute force (TC-M7-006-01) harus mendefinisikan secara eksplisit bagaimana mereset counter `failed_login_attempts` ke 0 setelah kasus uji selesai (cleanup).

- [ ] **7.6** — **Validasi exit criteria dokumen**:
  - Apakah dokumen mendefinisikan kriteria exit testing yang jelas? (berapa % pass rate minimum yang dianggap acceptable untuk lanjut ke fase berikutnya).
  - Jika belum ada, tambahkan sub-bab baru yang mendefinisikan:
    - Minimum pass rate: ≥ 95% untuk kasus uji bertipe High.
    - 0 FAIL pada kasus uji bertipe Security.
    - 0 FAIL pada kasus uji bertipe Precision.

---

### TAHAP 8: Penulisan Ulang Penuh (Full Overwrite)

**Tujuan**: Menuangkan seluruh hasil analisis, temuan, dan perbaikan ke dalam file target dengan cara menimpa (*overwrite*) penuh.

> [!CAUTION]
> Tahapan ini adalah tahap paling kritis. Bacalah seluruh instruksi di bawah sebelum memulai penulisan.

- [ ] **8.1** — **Siapkan hasil konsolidasi semua temuan**:
  - Kumpulkan semua temuan dari Tahap 1-7 menjadi daftar perbaikan yang terurut.
  - Kelompokkan perbaikan berdasarkan bagian dokumen (Bab 1, Bab 2, Bab 3, Bab 4, dst.).

- [ ] **8.2** — **Tulis ulang dokumen secara penuh ke file target**:
  - Buka file `docs/sdlc/05_testing/02_test_cases.md`.
  - Tulis ulang (*overwrite*) **seluruh konten** file tersebut dari baris pertama hingga baris terakhir.

  > [!IMPORTANT]
  > **ATURAN PENULISAN MUTLAK — DILARANG KERAS DILANGGAR:**
  > 1. **NO TRUNCATION**: Seluruh teks dari baris pertama hingga terakhir harus ditulis ulang sepenuhnya. Dilarang memotong, meringkas, atau menghilangkan bagian apapun dari dokumen yang sudah ada.
  > 2. **FULL CONTENT**: Setiap bab, sub-bab, tabel, dan kode blok harus ditulis secara lengkap sebagaimana adanya, dengan perbaikan yang relevan diterapkan.
  > 3. **PRESERVE STRUCTURE**: Pertahankan seluruh struktur penomoran bab yang sudah ada. Jika ada penambahan sub-bab baru, tambahkan di posisi yang logis tanpa mengubah penomoran bab yang sudah ada secara drastis.
  > 4. **VERSION UPDATE**: Ubah nilai versi dari `1.0` menjadi `1.1` di frontmatter YAML dan di judul riwayat perubahan.
  > 5. **CHANGELOG UPDATE**: Tambahkan baris baru di tabel `Riwayat Perubahan Dokumen` dengan tanggal hari ini, deskripsi singkat perubahan yang dilakukan, dan nama persona pelaksana.

- [ ] **8.3** — **Terapkan seluruh perbaikan berdasarkan temuan Tahap 1-7**:
  - Koreksi data kalkulasi yang salah.
  - Lengkapi kasus uji yang hilang.
  - Perbaiki teks ambigu.
  - Isi placeholder yang kosong.
  - Tambahkan bagian yang belum ada (Entry/Exit Criteria, Dependency Map, dll.).
  - Koreksi inkonsistensi format.

- [ ] **8.4** — **Perbarui Bab 2 (Ringkasan Cakupan)** dengan angka statistik yang akurat setelah semua penambahan/perubahan kasus uji selesai diterapkan.

- [ ] **8.5** — **Perbarui Bab 19 (Matriks Ketertelusuran)** agar mencakup semua kasus uji yang ada (termasuk yang baru ditambahkan).

- [ ] **8.6** — **Perbarui Bab 21 (Referensi Dokumen)** jika selama analisis ditemukan file referensi baru yang digunakan sebagai acuan. Tambahkan file referensi baru tersebut di baris paling bawah tabel referensi.

---

### TAHAP 9: Verifikasi Pasca Penulisan

**Tujuan**: Melakukan pengecekan akhir untuk memastikan penulisan ulang berhasil dan dokumen sudah dalam kondisi yang benar.

- [ ] **9.1** — Baca ulang seluruh dokumen hasil penulisan dari baris pertama hingga terakhir. Pastikan tidak ada bagian yang terpotong atau hilang dibandingkan konten sebelumnya.

- [ ] **9.2** — Verifikasi bahwa versi dokumen di frontmatter YAML sudah berubah menjadi `1.1`.

- [ ] **9.3** — Verifikasi bahwa tabel `Riwayat Perubahan Dokumen` sudah memiliki baris baru untuk versi `1.1`.

- [ ] **9.4** — Verifikasi bahwa jumlah kasus uji di Bab 2.1 konsisten dengan jumlah kasus uji aktual yang dapat dihitung di Bab 4-18.

- [ ] **9.5** — Verifikasi bahwa seluruh kode error yang muncul di kasus uji sudah terdaftar di Bab 19.4.

- [ ] **9.6** — Verifikasi bahwa tidak ada teks `*[Diisi saat eksekusi]*` di kolom `Skenario Asal`, `Referensi SRS / UC`, `Modul / Fitur`, `Tipe / Tingkat / Pri`, `Peran Aktor`, `Prakondisi`, `Data Uji`, `Langkah Uji`, atau `Hasil Diharapkan`.

- [ ] **9.7** — Verifikasi bahwa semua file referensi baru (jika ada) sudah ditambahkan di Bab 21 tabel referensi.

- [ ] **9.8** — Verifikasi bahwa sintaks markdown tidak ada yang rusak (tabel tidak misaligned, blok kode tertutup, heading tidak duplikat).

---

## Kriteria Penyelesaian Issue

Issue ini dinyatakan **SELESAI** dan siap di-*close* jika **seluruh** kondisi berikut terpenuhi:

- [ ] Seluruh 9 tahapan telah dilaksanakan.
- [ ] Seluruh sub-tugas (`[ ]`) dalam setiap tahapan telah ditandai selesai (`[x]`).
- [ ] File `docs/sdlc/05_testing/02_test_cases.md` telah ditimpa (*overwrite*) dengan versi `1.1` yang lengkap.
- [ ] Tidak ada placeholder kosong yang tersisa (kecuali kolom `Hasil / Status Uji` yang memang diisi saat eksekusi).
- [ ] Tidak ada inkonsistensi data numerik yang ditemukan.
- [ ] Tidak ada kode error yang tidak terdefinisi.
- [ ] Dokumen dapat dibaca dari awal hingga akhir tanpa menimbulkan pertanyaan lanjutan yang kritis bagi implementator Test Scripts.

---

## Catatan Penting untuk Pelaksana

> [!WARNING]
> **Tentang Pembacaan File Besar**: Dokumen referensi (terutama R-SRS dan R-TP) memiliki ukuran yang besar (60.000 - 80.000 byte). Baca secara bertahap jika diperlukan. Jangan melewati bagian apapun.

> [!WARNING]
> **Tentang Full Overwrite**: Perintah overwrite berarti menulis **seluruh** konten file dari awal. Jangan hanya mengedit bagian tertentu secara parsial jika ada perbaikan menyeluruh yang perlu dilakukan. Kegagalan menulis seluruh konten (truncation) adalah kegagalan fatal issue ini.

> [!NOTE]
> **Tentang Penambahan Referensi**: Jika Anda menggunakan file referensi di luar 9 file yang terdaftar di awal (misalnya `docs/sdlc/03_design/03_system_architecture.md` atau file lainnya), tambahkan file tersebut ke tabel referensi Bab 21 dokumen target dengan nomor urut berikutnya.

> [!TIP]
> **Urutan Pekerjaan yang Efisien**: Lakukan Tahap 0 (baca semua referensi) terlebih dahulu sebelum membuat catatan temuan. Setelah seluruh referensi dibaca, baru mulai membandingkan (Tahap 1-7). Ini menghindari keharusan membaca ulang referensi berulang kali.

---