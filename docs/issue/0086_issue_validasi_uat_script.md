# Issue: Validasi Dokumen UAT Script v1.1

**Target File** : `docs/sdlc/05_testing/03_uat_script.md`  
**Tipe Issue**  : Validasi & Audit Dokumen SDLC  
**Prioritas**   : Tinggi  
**Status**      : Open  
**Dibuat**      : 2026-05-29  

---

## 1. Persona Auditor

Anda adalah **Senior UAT Engineer & SQA Lead (Software Quality Assurance Lead)** yang memiliki:

- Keahlian mendalam dalam metodologi *User Acceptance Testing* (UAT), penyusunan UAT Script standar industri, dan proses sign-off formal go-live.
- Kemampuan membaca dan memvalidasi kesesuaian antara dokumen UAT Script dengan dokumen sumber SDLC (Test Plan, Test Cases, SRS, Use Case, Security Design, dll.).
- Ketelitian tinggi terhadap presisi data numerik desimal, kode ID (UAT ID, SRS ID, UC ID, TC ID), dan keterkaitan lintas-dokumen yang diverifikasi secara silang (*cross-reference*).
- Pemahaman kuat terhadap standar perlindungan data pribadi (UU PDP No. 27/2022), keamanan sistem (bcrypt, JWT, RBAC, AES-256), dan validasi kalkulasi akuntansi/keuangan (Decimal, ROUND_HALF_UP, HPP, Payroll).
- Kemampuan memastikan setiap skrip UAT ditulis dalam bahasa bisnis Indonesia yang natural, tidak ambigu, dan dapat dipahami oleh penguji non-teknis (Pemilik Usaha, Kepala Percetakan) maupun junior programmer.

---

## 2. Latar Belakang dan Konteks

Dokumen target yang akan divalidasi adalah:

- **Nama Dokumen:** UAT Script — AbuCom
- **Path File Target:** `docs/sdlc/05_testing/03_uat_script.md`
- **Versi Saat Ini:** v1.1
- **Status Saat Ini:** Reviewed

Dokumen UAT Script ini adalah deliverable ketiga pada **Fase 05 — Testing** dalam SDLC proyek AbuCom. Dokumen ini berisi 44 skrip UAT individual (UAT-001 s.d. UAT-044), 1 skrip integrasi End-to-End (UAT-E2E-001), 3 skrip non-fungsional (UAT-NF-001 s.d. UAT-NF-003), prosedur defect handling, kriteria sign-off, glosarium, test fixtures, dan matriks ketertelusuran dua arah.

---

## 3. Dokumen Referensi Wajib Dibaca

Sebelum memulai validasi, baca dan pahami **seluruh** dokumen referensi berikut secara lengkap dari baris pertama hingga terakhir:

| No | Kode Ref | Path File | Keterangan |
|----|----------|-----------|------------|
| 1 | **R-TP** | `docs/sdlc/05_testing/01_test_plan.md` | Sumber 44 skenario uji induk, error mapping, kriteria sign-off UAT |
| 2 | **R-TC** | `docs/sdlc/05_testing/02_test_cases.md` | Sumber langkah uji terperinci, entry/exit criteria, test fixtures akun penguji |
| 3 | **R-SRS** | `docs/sdlc/02_analysis/02_software_requirements.md` | Spesifikasi batasan input, aturan validasi, logika bisnis (SRS-F-001 s.d. SRS-F-040) |
| 4 | **R-UC** | `docs/sdlc/02_analysis/03_use_case_diagram.md` | Alur naratif utama, alternatif, pengecualian (UC-001 s.d. UC-041) |
| 5 | **R-ACM** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Definisi 8 peran internal dan otorisasi menu |
| 6 | **R-CLI** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Navigasi terminal, rendering ANSI, format kode error |
| 7 | **R-BOM** | `docs/sdlc/03_design/05_bom_hpp_design.md` | Spesifikasi kalkulasi desimal HPP dan locking stok |
| 8 | **R-SEC** | `docs/sdlc/03_design/06_security_design.md` | Spesifikasi bcrypt, JWT, rate limiting brute-force, UU PDP |
| 9 | **R-WF** | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Alur kerja operasional bisnis harian toko |

---

## 4. Dimensi Validasi

Lakukan validasi dokumen target secara menyeluruh menggunakan **10 dimensi validasi** berikut:

### Dimensi 1 — Kelengkapan Serapan Data dari Dokumen Referensi
Verifikasi apakah seluruh data dan informasi yang tersedia di dokumen referensi (R-TP, R-TC, R-SRS, R-UC, R-ACM, R-CLI, R-BOM, R-SEC, R-WF) sudah terserapkan dengan benar dan lengkap ke dalam dokumen target. Tidak boleh ada skenario UAT, kode ID, data uji, langkah pengujian, atau kriteria kelulusan yang terlewat dari referensi tersebut.

**Poin spesifik yang harus diperiksa:**
- Semua 44 skenario UAT individual ada dan ID-nya berurutan tanpa loncatan (UAT-001 hingga UAT-044).
- Setiap UAT merujuk Test Case ID yang valid sesuai R-TC (contoh: `TC-M7-001-01`, `TC-DEC-001-01`).
- Setiap UAT merujuk SRS ID yang valid sesuai R-SRS (contoh: `SRS-F-001` s.d. `SRS-F-040`).
- Setiap UAT merujuk Use Case ID yang valid sesuai R-UC (contoh: `UC-001` s.d. `UC-041`).
- Data uji numerik desimal (HPP, payroll, depresiasi, nominal transaksi) konsisten dengan nilai yang ada di R-BOM dan R-TC.
- 8 akun penguji (test fixtures) di Lampiran 18.2 konsisten dengan data yang ada di R-TC.

### Dimensi 2 — Relevansi dan Fokus Konten Spesifik Dokumen UAT Script
Verifikasi apakah dokumen ini hanya memuat data dan informasi yang memang seharusnya ada dalam sebuah UAT Script. Dokumen tidak boleh memuat konten teknis implementasi kode program, detail desain database internal, atau spesifikasi arsitektur yang tidak relevan dengan perspektif pengujian penerimaan pengguna bisnis.

**Poin spesifik yang harus diperiksa:**
- Langkah pengujian ditulis dari sudut pandang *end-user* (Pemilik Usaha/Kepala Percetakan), bukan dari sudut pandang developer.
- Hasil diharapkan berfokus pada output fungsional bisnis yang terukur dan deterministik, bukan detail implementasi internal.
- Tidak ada duplikasi konten yang tidak perlu atau konten yang merupakan salinan mentah dari Test Cases.

### Dimensi 3 — Standar Struktur Dokumen UAT Script Industri
Verifikasi apakah struktur dokumen sudah memenuhi standar industri dokumen UAT Script formal. Struktur yang benar setidaknya mencakup:

- Header dokumen (nama proyek, versi, tanggal, status, penyusun).
- Riwayat perubahan dokumen (changelog).
- Informasi dokumen: tujuan, cakupan, posisi dalam SDLC, relasi input/output, audiens target, dan definisi akronim.
- Lingkup dan tujuan UAT: tujuan pengujian, cakupan modul, fitur out-of-scope, kriteria keberhasilan keseluruhan.
- Organisasi dan peran UAT: tim pelaksana dan jadwal pelaksanaan.
- Prasyarat dan checklist kesiapan UAT (readiness checklist).
- Skrip UAT individual dengan atribut lengkap (ID, judul, skenario asal, test case terkait, referensi SRS/UC, modul, aktor, lingkungan, prasyarat, data uji, langkah pengujian, hasil diharapkan, hasil aktual, status, catatan temuan, tanda tangan penguji).
- Skrip integrasi End-to-End.
- Skrip pengujian non-fungsional.
- Prosedur defect handling (klasifikasi, template pencatatan, eskalasi).
- Kriteria keluar UAT (exit criteria) dan sign-off (checklist terukur + formulir tanda tangan formal).
- Lampiran: glosarium, test fixtures, matriks ketertelusuran.
- Referensi dokumen.

### Dimensi 4 — Kelayakan sebagai Input SDLC Fase Berikutnya
Verifikasi apakah dokumen ini cukup lengkap dan informatif untuk dijadikan sebagai acuan utama bagi dokumen SDLC berikutnya, yaitu:
- **UAT Test Report:** Apakah kolom "Hasil Aktual" dan "Status" sudah tersedia di setiap skrip UAT sebagai area pencatatan eksekusi?
- **Deployment/Release Document:** Apakah kriteria sign-off dan formulir go-live sudah memadai sebagai bukti formal persetujuan?
- **Training Manual:** Apakah skenario operasional bisnis yang dideskripsikan cukup representatif dan realistis untuk dijadikan acuan pelatihan?

### Dimensi 5 — Kualitas Bahasa Indonesia
Verifikasi apakah seluruh teks dokumen menggunakan bahasa Indonesia yang natural, baku, tidak ambigu, dan mudah dipahami oleh penguji non-teknis (Pemilik Usaha, Kepala Percetakan) maupun junior programmer atau AI model yang lebih murah.

**Poin spesifik yang harus diperiksa:**
- Tidak ada kalimat yang rancu atau multi-interpretasi.
- Istilah teknis asing (UAT, BOM, HPP, RBAC, JWT, dll.) sudah dijelaskan di bagian glosarium/akronim.
- Langkah pengujian ditulis dalam kalimat imperatif yang jelas dan dapat langsung diikuti.
- Tidak ada campuran bahasa Indonesia-Inggris yang tidak konsisten pada bagian yang sama.
- Ejaan dan tanda baca mengikuti PUEBI (Pedoman Umum Ejaan Bahasa Indonesia).

### Dimensi 6 — Kelengkapan dan Ketuntasan Dokumen (Tidak Membutuhkan Interupsi)
Verifikasi apakah dokumen ini sudah cukup mandiri sehingga pelaksana UAT (Pemilik Usaha, Kepala Percetakan) dapat menjalankan pengujian tanpa harus terus-menerus bertanya atau membutuhkan klarifikasi tambahan di luar dokumen.

**Poin spesifik yang harus diperiksa:**
- Setiap prasyarat (precondition) per skrip UAT cukup spesifik dan dapat dipersiapkan secara mandiri.
- Setiap data uji sudah tercantum dengan nilai konkret (bukan placeholder kosong).
- Langkah pengujian ditulis dengan detail yang cukup (tidak terlalu abstrak hingga membingungkan).
- Kriteria kelulusan (expected result) bersifat deterministik dan terukur, bukan subjektif.
- Tidak ada langkah yang merujuk pada informasi yang tidak ada dalam dokumen.

### Dimensi 7 — Pengisian Data Kosong dan Placeholder
Identifikasi seluruh field yang masih kosong, berisi placeholder belum diisi, atau membutuhkan data konkret. Kemudian isi dengan data yang sesuai, relevan, dan masih dalam ruang lingkup dokumen UAT Script ini.

**Field yang harus diidentifikasi dan diisi:**
- Placeholder `[Diisi manual saat pelaksanaan UAT]` pada kolom Tanggal di tabel Jadwal Pelaksanaan UAT (Bab 3.2) — **biarkan sebagai placeholder**, ini memang harus diisi manual saat pelaksanaan UAT berlangsung karena tanggal aktual belum diketahui. Pastikan placeholder ini memiliki keterangan yang jelas mengapa masih kosong.
- Placeholder `[Diisi Nama UAT Analyst / Senior QA]`, `[Diisi Nama Kepala Percetakan]`, `[Diisi Nama Programmer/QA]` pada tabel Tim Pelaksana UAT (Bab 3.1) — **biarkan sebagai placeholder** karena nama personel aktual adalah data operasional yang diisi saat kontrak proyek dimulai. Pastikan ada catatan yang cukup jelas.
- Placeholder `[DATA BELUM TERSEDIA - Perlu diisi manual oleh Pemilik Usaha]` pada Formulir Tanda Tangan Persetujuan Go-Live (Bab 17.3) — **biarkan sebagai placeholder** karena merupakan data yang diisi saat eksekusi go-live. Pastikan ada catatan instruksi yang jelas.
- Verifikasi apakah ada placeholder lain yang tersembunyi di bagian manapun dari dokumen yang seharusnya sudah bisa diisi dengan data konkret dari referensi.

### Dimensi 8 — Konsistensi dan Akurasi ID Referensi Silang
Verifikasi konsistensi dan akurasi seluruh ID referensi yang digunakan dalam dokumen:

**Poin spesifik yang harus diperiksa:**
- ID UAT di matriks ketertelusuran (Bab 18.3) konsisten dengan ID di badan skrip UAT.
- Setiap `Skenario Asal` (misal: `M7-TC-001`, `M1-TC-005`) merujuk ke ID skenario yang valid di R-TP.
- Setiap `Test Case Terkait` (misal: `TC-M7-001-01`, `TC-DEC-001-01`) merujuk ke ID yang valid di R-TC.
- Setiap `Referensi SRS / UC` (misal: `SRS-F-030 / UC-041`) merujuk ke ID yang valid di R-SRS dan R-UC.
- Anchor link internal dalam skrip E2E (Bab 14) mengarah ke heading yang benar.
- Diagram mermaid E2E mencantumkan referensi UAT ID yang konsisten dengan badan dokumen.

### Dimensi 9 — Akurasi Kalkulasi Numerik Desimal
Verifikasi akurasi seluruh kalkulasi numerik desimal yang tercantum dalam dokumen:

**Poin spesifik yang harus diperiksa:**
- HPP BOM Stempel Flash: `(0.0025 × 100.000,0000) + (1.0000 × 4.500,0000) = Rp 4.750,0000` ✓
- Bunga pinjaman bank: `(10.000.000 × 10%) / 12 = Rp 83.333,3333` per bulan — verifikasi presisi ROUND_HALF_UP.
- Depresiasi garis lurus: `10.000.000 / 60 = Rp 166.666,6667` per bulan — verifikasi presisi ROUND_HALF_UP.
- Smart Payroll batas bawah: 50% UMR Rp 3.200.000 = Rp 1.600.000,0000.
- Skenario E2E: verifikasi bahwa pergerakan saldo laci kas dalam setiap langkah simulasi akurat dan konsisten secara akuntansi (Rp 500.000 → Rp 600.000 → Rp 650.000 → Rp 750.000).
- Brute-force lockout: 5 kali gagal, durasi 600 detik (10 menit) — verifikasi konsistensi.
- Sisa stok HVS pada skenario E2E: stok awal 10 Rim → setelah penjualan 2 Rim → 8 Rim → setelah opname selisih 2 Rim → 6 Rim — verifikasi akurasi pergerakan stok.
- Limbah karet flash: `0.0005 × Rp 100.000,0000 = Rp 50,0000` ✓.

### Dimensi 10 — Aspek Spesifik UAT Script (Tambahan Kritis)
Verifikasi aspek-aspek yang secara khusus berlaku untuk dokumen UAT Script:

**Poin spesifik yang harus diperiksa:**
- Setiap skrip UAT memiliki kolom **"Hasil Aktual"** dan **"Status"** yang diisi *[Diisi saat eksekusi UAT]* — ini adalah placeholder yang **BENAR** dan **HARUS** dibiarkan kosong, karena diisi saat eksekusi nyata.
- Setiap skrip UAT memiliki kolom **"Tanda Tangan Penguji"** sebagai bukti formal.
- Langkah pengujian skrip UAT menggunakan perspektif bisnis end-user, bukan perspektif developer (verifikasi tidak ada langkah yang meminta penguji "edit kode program" atau "ubah konfigurasi server secara langsung").
- Khusus untuk simulasi teknis yang memang dibutuhkan (seperti simulasi sesi JWT expired, simulasi waktu berlalu untuk brute-force), pastikan langkah tersebut ditandai dengan label jelas "[Simulasi oleh QA]" agar tidak membingungkan Pemilik Usaha/Kepala Percetakan.
- Skrip E2E (UAT-E2E-001) mencakup satu siklus hari operasional bisnis yang **lengkap dan berurutan** (buka toko → absensi → transaksi → produksi → opname → handover → backup).
- Tabel matriks ketertelusuran (Bab 18.3) mencakup semua 44 UAT tanpa ada yang terlewat.
- Checklist sign-off (Bab 17.2) berisi 7 kriteria terukur yang relevan dengan fitur-fitur kritis AbuCom.

---

## 5. Tahapan Implementasi (Low-Level Checklist)

Ikuti tahapan berikut **secara berurutan dari atas ke bawah**. Tandai setiap tugas dengan `[x]` setelah selesai dikerjakan. **Jangan melompati atau melewatkan satu pun langkah.**

---

### FASE A — PERSIAPAN DAN PEMBACAAN DOKUMEN

- [ ] **A.1** Buka dan baca file target secara lengkap dari baris pertama hingga terakhir:
  ```
  Baca file: docs/sdlc/05_testing/03_uat_script.md
  ```

- [ ] **A.2** Buka dan baca dokumen referensi R-TP secara lengkap:
  ```
  Baca file: docs/sdlc/05_testing/01_test_plan.md
  ```
  Catat: daftar seluruh skenario uji induk (M1-TC-001 dst.), kriteria sign-off UAT, dan error mapping yang terdokumentasi.

- [ ] **A.3** Buka dan baca dokumen referensi R-TC secara lengkap:
  ```
  Baca file: docs/sdlc/05_testing/02_test_cases.md
  ```
  Catat: daftar seluruh ID Test Case (TC-M1-001-01 dst.), entry/exit criteria, data uji konkret, dan data fixtures akun penguji.

- [ ] **A.4** Buka dan baca dokumen referensi R-SRS secara lengkap:
  ```
  Baca file: docs/sdlc/02_analysis/02_software_requirements.md
  ```
  Catat: daftar seluruh ID kebutuhan fungsional (SRS-F-001 s.d. SRS-F-040) beserta deskripsi singkatnya.

- [ ] **A.5** Buka dan baca dokumen referensi R-UC secara lengkap:
  ```
  Baca file: docs/sdlc/02_analysis/03_use_case_diagram.md
  ```
  Catat: daftar seluruh ID use case (UC-001 s.d. UC-041) beserta nama dan aktor terkaitnya.

- [ ] **A.6** Buka dan baca dokumen referensi R-ACM secara lengkap:
  ```
  Baca file: docs/sdlc/02_analysis/06_access_control_matrix.md
  ```
  Catat: daftar 8 peran internal dan otorisasi menu masing-masing peran.

- [ ] **A.7** Buka dan baca dokumen referensi R-CLI secara lengkap:
  ```
  Baca file: docs/sdlc/03_design/04_cli_interaction_flow.md
  ```
  Catat: format kode error (ERR-AUTH-002, ERR-SESSION-002, dll.), format navigasi breadcrumb, dan spesifikasi rendering ANSI.

- [ ] **A.8** Buka dan baca dokumen referensi R-BOM secara lengkap:
  ```
  Baca file: docs/sdlc/03_design/05_bom_hpp_design.md
  ```
  Catat: formula HPP desimal, contoh kalkulasi konkret, dan mekanisme locking stok.

- [ ] **A.9** Buka dan baca dokumen referensi R-SEC secara lengkap:
  ```
  Baca file: docs/sdlc/03_design/06_security_design.md
  ```
  Catat: spesifikasi bcrypt cost factor, JWT 8 jam (28.800 detik), rate limiting 5x gagal/10 menit, enkripsi Fernet, dan AES-256.

- [ ] **A.10** Buka dan baca dokumen referensi R-WF secara lengkap:
  ```
  Baca file: docs/sdlc/02_analysis/04_workflow_diagram.md
  ```
  Catat: alur kerja operasional bisnis harian (buka toko → absensi → transaksi → produksi → opname → handover → tutup toko).

---

### FASE B — ANALISIS DAN VALIDASI DOKUMEN

- [ ] **B.1 — Validasi Struktur Dokumen (Dimensi 3)**
  Periksa apakah dokumen memiliki semua bagian/bab berikut. Tandai yang ada (`✓`) dan yang tidak ada (`✗`):
  - [ ] Header dokumen (nama proyek, versi, tanggal, status, penyusun) → Bab: bagian YAML header
  - [ ] Riwayat perubahan dokumen (changelog) → Bab: Riwayat Perubahan Dokumen
  - [ ] Tujuan dokumen → Bab 1.1
  - [ ] Cakupan dokumen → Bab 1.2
  - [ ] Posisi dalam SDLC (diagram) → Bab 1.3
  - [ ] Relasi input/output dengan dokumen SDLC lain → Bab 1.4
  - [ ] Audiens target → Bab 1.5
  - [ ] Definisi, akronim, dan singkatan → Bab 1.6
  - [ ] Tujuan pengujian penerimaan → Bab 2.1
  - [ ] Cakupan modul yang diuji → Bab 2.2
  - [ ] Fitur out-of-scope → Bab 2.3
  - [ ] Kriteria keberhasilan UAT keseluruhan → Bab 2.4
  - [ ] Tim pelaksana UAT → Bab 3.1
  - [ ] Jadwal pelaksanaan UAT → Bab 3.2
  - [ ] Checklist kesiapan lingkungan → Bab 4.1
  - [ ] Checklist kesiapan data uji → Bab 4.2
  - [ ] Checklist kesiapan dokumen → Bab 4.3
  - [ ] Kriteria masuk UAT (entry criteria) → Bab 4.4
  - [ ] 44 Skrip UAT individual (UAT-001 s.d. UAT-044) → Bab 5 s.d. Bab 13
  - [ ] Skrip integrasi E2E (UAT-E2E-001) → Bab 14
  - [ ] 3 Skrip non-fungsional (UAT-NF-001 s.d. UAT-NF-003) → Bab 15
  - [ ] Prosedur defect handling (klasifikasi + template + eskalasi) → Bab 16
  - [ ] Kriteria keluar UAT (exit criteria) → Bab 17.1
  - [ ] Checklist sign-off 7 kriteria terukur → Bab 17.2
  - [ ] Formulir tanda tangan persetujuan go-live → Bab 17.3
  - [ ] Glosarium → Bab 18.1
  - [ ] Test fixtures (data akun penguji) → Bab 18.2
  - [ ] Matriks ketertelusuran UAT → TC → SRS → UC → Bab 18.3
  - [ ] Referensi dokumen → Bab 19

- [ ] **B.2 — Validasi Kelengkapan Skrip UAT (Dimensi 1)**
  Buat daftar seluruh UAT ID yang ada dalam dokumen. Pastikan:
  - [ ] Ada tepat 44 skrip UAT individual berurutan dari UAT-001 hingga UAT-044 tanpa loncatan.
  - [ ] Ada 1 skrip E2E: UAT-E2E-001.
  - [ ] Ada 3 skrip non-fungsional: UAT-NF-001, UAT-NF-002, UAT-NF-003.

- [ ] **B.3 — Validasi Atribut Setiap Skrip UAT (Dimensi 1 & 6)**
  Untuk setiap skrip UAT (UAT-001 s.d. UAT-044), verifikasi bahwa semua atribut berikut sudah terisi (bukan kosong atau N/A tanpa alasan):
  - [ ] ID Skrip UAT
  - [ ] Judul
  - [ ] Skenario Asal (Kode skenario dari R-TP)
  - [ ] Test Case Terkait (ID dari R-TC)
  - [ ] Referensi SRS / UC (ID dari R-SRS dan R-UC)
  - [ ] Modul / Fitur
  - [ ] Aktor Penguji
  - [ ] Lingkungan
  - [ ] Prasyarat (konkret dan spesifik)
  - [ ] Data Uji (nilai numerik konkret, bukan "nilai dummy")
  - [ ] Langkah Pengujian (minimal 3 langkah deskriptif)
  - [ ] Hasil Diharapkan (deterministik dan terukur)
  - [ ] Hasil Aktual (boleh `*[Diisi saat eksekusi UAT]*`)
  - [ ] Status (boleh `*[Diisi saat eksekusi: PASS / FAIL]*`)
  - [ ] Catatan Temuan (boleh `*[Diisi jika ada temuan/bug]*`)
  - [ ] Tanda Tangan Penguji (boleh garis kosong)

- [ ] **B.4 — Validasi Cross-Reference ID (Dimensi 8)**
  Lakukan pemeriksaan silang untuk setiap skrip UAT:
  - [ ] Cocokkan setiap `Skenario Asal` (misal: `M1-TC-001`) dengan daftar skenario di R-TP. Pastikan ID-nya valid dan ada.
  - [ ] Cocokkan setiap `Test Case Terkait` (misal: `TC-M1-001-01`) dengan daftar test case di R-TC. Pastikan ID-nya valid dan ada.
  - [ ] Cocokkan setiap `Referensi SRS` (misal: `SRS-F-001`) dengan daftar kebutuhan di R-SRS. Pastikan ID-nya valid dan ada.
  - [ ] Cocokkan setiap `Referensi UC` (misal: `UC-001`) dengan daftar use case di R-UC. Pastikan ID-nya valid dan ada.
  - [ ] Cocokkan setiap entri di matriks ketertelusuran (Bab 18.3) dengan skrip UAT terkait. Pastikan tidak ada inkonsistensi.

- [ ] **B.5 — Validasi Akurasi Kalkulasi Numerik (Dimensi 9)**
  Hitung ulang secara manual setiap nilai numerik berikut dan verifikasi keakuratannya:
  - [ ] **HPP BOM Stempel Flash (UAT-011):** `(0.0025 × 100.000,0000) + (1.0000 × 4.500,0000)`. Hasil harus = `Rp 4.750,0000`.
  - [ ] **Bunga Pinjaman Bank (UAT-030):** `(10.000.000 × 10%) / 12`. Hasil harus = `Rp 83.333,3333` (ROUND_HALF_UP, 4 desimal).
  - [ ] **Depresiasi Garis Lurus (UAT-032):** `10.000.000 / 60`. Hasil harus = `Rp 166.666,6667` (ROUND_HALF_UP, 4 desimal).
  - [ ] **Smart Payroll batas bawah (UAT-023/024):** `50% × Rp 3.200.000,0000 = Rp 1.600.000,0000`.
  - [ ] **Limbah Produksi (UAT-012):** `0.0005 × Rp 100.000,0000 = Rp 50,0000`.
  - [ ] **ATK Internal (UAT-013):** `2.0000 × Rp 2.000,0000 = Rp 4.000,0000`.
  - [ ] **Re-order prediksi (UAT-015):** `0.0100 / 0.0020 = 5 hari`.
  - [ ] **Handover shift normal (UAT-042):** `Kas awal Rp 500.000 + Penjualan Rp 300.000 = Rp 800.000. Fisik laci Rp 800.000. Selisih = Rp 0,0000`.
  - [ ] **Handover shift anomali (UAT-043):** `Rp 800.000 (target) - Rp 780.000 (fisik) = selisih minus Rp 20.000,0000 (> batas Rp 10.000)`.
  - [ ] **Skenario E2E pergerakan saldo kas:** Buka toko Rp 500.000 → (+Rp 100.000 penjualan ATK) → Rp 600.000 → (+Rp 50.000 DP kustom) → Rp 650.000 → (+Rp 100.000 pelunasan) → Rp 750.000.
  - [ ] **Skenario E2E pergerakan stok HVS:** Stok awal 10 Rim → (-2 Rim penjualan) → 8 Rim → (opname fisik 6 Rim, selisih -2 Rim) → 6 Rim.
  - [ ] **JWT session expiry:** `8 jam = 28.800 detik`. Verifikasi konsistensi penyebutan di seluruh dokumen.
  - [ ] **Brute-force lockout:** `5 kali gagal → lockout 600 detik (10 menit)`. Verifikasi konsistensi.
  - [ ] **PPOB saldo limit kritis:** saldo virtual < Rp 150.000 memicu alert (UAT-019).

- [ ] **B.6 — Validasi Kode Error CLI (Dimensi 8)**
  Cocokkan setiap kode error yang disebutkan dalam dokumen target dengan spesifikasi di R-CLI:
  - [ ] `ERR-SESSION-002` (Login expired) — verifikasi ada di R-CLI.
  - [ ] `ERR-AUTH-003` (Akses Ditolak RBAC) — verifikasi ada di R-CLI.
  - [ ] `ERR-AUTH-002` (Brute-force lockout) — verifikasi ada di R-CLI.
  - [ ] `ERR-AUTH-029` (Verifikasi sandi Pemilik gagal) — verifikasi ada di R-CLI.
  - [ ] `ERR-VAL-007` (Input tidak valid) — verifikasi ada di R-CLI.
  - [ ] `ERR-VAL-003` (Nominal pelunasan kurang) — verifikasi ada di R-CLI.
  - [ ] `ERR-DB-002` (Pelanggaran integritas DB) — verifikasi ada di R-CLI.
  - [ ] `ERR-FILE-039` (Berkas cadangan korup) — verifikasi ada di R-CLI.
  - [ ] Seluruh kode error lain yang ditemukan dalam dokumen — cocokkan dengan R-CLI.

- [ ] **B.7 — Validasi Akun Penguji / Test Fixtures (Dimensi 1)**
  Cocokkan tabel akun penguji di Bab 18.2 dengan data fixtures di R-TC:
  - [ ] Jumlah akun: pastikan ada tepat 8 akun penguji.
  - [ ] Username: `pemilik`, `kepala`, `kasir01`, `desain01`, `prod01`, `gudang01`, `pramu01`, `foto01` — verifikasi semua ada.
  - [ ] Peran setiap akun konsisten dengan R-ACM.
  - [ ] Password default `'SandiStaf2026!'` dengan bcrypt cost factor 12 tersebut konsisten dengan R-TC dan R-SEC.

- [ ] **B.8 — Validasi Kesiapan UAT sebagai Input Fase Berikutnya (Dimensi 4)**
  Verifikasi kelayakan dokumen untuk menjadi input fase berikutnya:
  - [ ] Setiap skrip UAT memiliki kolom "Hasil Aktual" dan "Status" yang siap diisi saat eksekusi.
  - [ ] Formulir tanda tangan go-live (Bab 17.3) sudah tersedia secara formal.
  - [ ] Prosedur defect handling (Bab 16) cukup untuk menjadi panduan pencatatan bug bagi UAT Test Report.
  - [ ] Matriks ketertelusuran (Bab 18.3) lengkap dan dapat digunakan sebagai laporan ketertelusuran pasca-eksekusi.

- [ ] **B.9 — Validasi Bahasa Indonesia (Dimensi 5)**
  Baca ulang seluruh dokumen dan identifikasi:
  - [ ] Kalimat yang ambigu atau multi-interpretasi — catat baris dan kalimatnya.
  - [ ] Penggunaan istilah teknis tanpa definisi glosarium — catat istilah yang hilang.
  - [ ] Campuran bahasa yang tidak konsisten — catat contohnya.
  - [ ] Kesalahan ejaan atau tanda baca yang signifikan — catat dan perbaiki.
  - [ ] Kalimat yang terlalu panjang/kompleks hingga sulit dipahami penguji non-teknis — sederhanakan.

- [ ] **B.10 — Identifikasi Placeholder dan Data Kosong (Dimensi 7)**
  Cari seluruh teks berikut dalam dokumen dan evaluasi setiap kemunculannya:
  - [ ] `[Diisi Nama` — evaluasi apakah perlu diisi atau memang harus dibiarkan.
  - [ ] `[Diisi manual` — evaluasi apakah perlu diisi atau memang harus dibiarkan.
  - [ ] `[DATA BELUM TERSEDIA` — evaluasi apakah perlu diisi atau memang harus dibiarkan.
  - [ ] `*[Diisi saat eksekusi UAT]*` — ini BENAR dan HARUS dibiarkan (field eksekusi).
  - [ ] `*[Diisi saat eksekusi: PASS / FAIL]*` — ini BENAR dan HARUS dibiarkan (field eksekusi).
  - [ ] `*[Diisi jika ada temuan/bug]*` — ini BENAR dan HARUS dibiarkan (field eksekusi).
  - [ ] Identifikasi apakah ada data lain yang kosong tanpa keterangan jelas mengapa kosong — isi dengan data yang sesuai dari dokumen referensi.

- [ ] **B.11 — Validasi Relevansi Konten (Dimensi 2)**
  Periksa apakah ada konten yang tidak seharusnya ada dalam dokumen UAT Script:
  - [ ] Identifikasi langkah pengujian yang meminta penguji mengubah kode program secara langsung (bukan operasi melalui antarmuka CLI).
  - [ ] Identifikasi konten yang merupakan salinan mentah dari Test Cases tanpa adaptasi ke perspektif end-user bisnis.
  - [ ] Identifikasi detail teknis implementasi internal yang tidak relevan untuk penguji bisnis.
  - [ ] Jika ada, susun rekomendasi perbaikannya.

- [ ] **B.12 — Validasi Aspek Spesifik UAT Script (Dimensi 10)**
  Periksa aspek-aspek khusus UAT Script:
  - [ ] Langkah simulasi teknis (JWT expired, percepatan waktu brute-force) sudah diberi label jelas `[Simulasi oleh QA]` atau kalimat setara.
  - [ ] Skenario E2E (UAT-E2E-001) mencakup siklus hari operasional lengkap (12 langkah: login → absensi → CRM → transaksi ATK → DP kustom → antrian → BOM → limbah → pelunasan → opname → handover → backup).
  - [ ] Diagram mermaid E2E menampilkan alur yang konsisten dengan 12 langkah tersebut.
  - [ ] Anchor link di tabel skenario E2E merujuk ke heading yang benar (misal: `#51-uat-001-login-kasir-dan-verifikasi-sesi-jwt`).
  - [ ] 3 skrip non-fungsional (NF-001, NF-002, NF-003) menggunakan format yang berbeda dari skrip individual (format bullet list, bukan tabel atribut) — verifikasi ini sudah konsisten.
  - [ ] Checklist sign-off Bab 17.2 mencantumkan tepat 7 kriteria yang terukur secara kuantitatif.

---

### FASE C — PENYUSUNAN CATATAN TEMUAN

- [ ] **C.1** Buat catatan lengkap berisi daftar semua temuan dari Fase B, dikelompokkan per dimensi validasi. Untuk setiap temuan, catat:
  - Nomor temuan
  - Dimensi validasi terkait
  - Lokasi dalam dokumen (bab/baris/skrip UAT terkait)
  - Deskripsi masalah yang ditemukan
  - Rekomendasi perbaikan konkret

- [ ] **C.2** Kelompokkan temuan ke dalam kategori:
  - **Kritis:** Kesalahan ID referensi silang, kalkulasi numerik salah, konten hilang yang wajib ada.
  - **Signifikan:** Placeholder yang perlu diisi, kalimat ambigu, atribut UAT tidak lengkap.
  - **Kosmetik:** Ejaan, tanda baca, inkonsistensi format minor.

---

### FASE D — PERBAIKAN DAN PENULISAN ULANG DOKUMEN

- [ ] **D.1** Berdasarkan seluruh temuan di Fase C, lakukan perbaikan atas dokumen target. **Urutan perbaikan yang disarankan:**
  1. Perbaiki kesalahan ID referensi silang terlebih dahulu (kritis).
  2. Perbaiki kesalahan kalkulasi numerik (kritis).
  3. Perbaiki atribut skrip UAT yang tidak lengkap (signifikan).
  4. Isi placeholder yang memang bisa dan perlu diisi dengan data dari referensi (signifikan).
  5. Perbaiki kalimat ambigu dan bahasa yang tidak natural (signifikan).
  6. Perbaiki ejaan, tanda baca, dan format minor (kosmetik).
  7. Tambahkan konten yang hilang jika ada (misalnya: skrip UAT yang terlewat, bab yang tidak ada).
  8. Hapus atau revisi konten yang tidak relevan (jika ditemukan pada B.11).

- [ ] **D.2** Perbarui bagian **Riwayat Perubahan Dokumen** dengan menambahkan entri baru versi berikutnya (misal dari v1.1 menjadi v1.2):
  ```
  | **v1.2** | [tanggal-hari-ini] | [Ringkasan seluruh perubahan yang dilakukan] | Senior UAT Engineer & SQA Lead |
  ```
  Ganti `[tanggal-hari-ini]` dengan tanggal aktual saat penulisan ulang dilakukan.
  Ganti `[Ringkasan seluruh perubahan yang dilakukan]` dengan deskripsi singkat dan padat semua perbaikan yang dilakukan.

- [ ] **D.3** Perbarui field `versi` pada header YAML dari `1.1` menjadi `1.2` (atau versi berikutnya sesuai increment).

- [ ] **D.4** Perbarui field `tanggal` pada header YAML dengan tanggal aktual saat penulisan ulang dilakukan.

- [ ] **D.5** Perbarui field `status` pada header YAML menjadi `Reviewed` atau `Updated` sesuai hasil validasi.

- [ ] **D.6** Jika dalam proses validasi ditemukan bahwa dokumen ini merujuk pada file referensi yang belum tercantum di Bab 19 (Referensi Dokumen), tambahkan baris baru di tabel referensi (Bab 19) di bagian akhir sesuai format tabel yang sudah ada.

---

### FASE E — PENULISAN ULANG TOTAL KE FILE TARGET

- [ ] **E.1** Tulis ulang seluruh isi dokumen yang telah divalidasi dan diperbaiki ke file target berikut dengan cara **menimpa (overwrite) seluruh isi file**:
  ```
  Target file: docs/sdlc/05_testing/03_uat_script.md
  ```

- [ ] **E.2** **WAJIB:** Pastikan penulisan ulang mencakup **seluruh teks dari baris pertama hingga baris terakhir** tanpa ada yang dipotong, diringkas, atau dihilangkan. Seluruh 44 skrip UAT individual, 1 skrip E2E, 3 skrip non-fungsional, seluruh lampiran, dan seluruh referensi **harus ditulis ulang sepenuhnya (no truncation)**.

- [ ] **E.3** Verifikasi bahwa file hasil penulisan ulang memiliki jumlah baris yang **sama atau lebih banyak** dari file asli (tidak lebih sedikit, kecuali ada konten yang sengaja dihapus karena tidak relevan dan sudah dicatat alasannya di catatan temuan).

- [ ] **E.4** Verifikasi bahwa nomor versi pada header YAML dan tabel riwayat perubahan sudah **diperbarui** (bukan tetap v1.1).

- [ ] **E.5** Baca ulang file hasil penulisan secara cepat (scan) untuk memastikan tidak ada truncation di bagian akhir dokumen. Pastikan Bab 19 (Referensi Dokumen) dan seluruh tabel referensi masih ada dan lengkap di baris-baris terakhir file.

---

### FASE F — VERIFIKASI AKHIR

- [ ] **F.1** Buka file hasil penulisan ulang dan verifikasi bagian-bagian kritis berikut masih ada dan benar:
  - [ ] Header YAML (baris 1-8) dengan versi yang sudah diperbarui.
  - [ ] Bab 1 (Informasi Dokumen) lengkap dengan semua sub-bab.
  - [ ] Bab 2 (Lingkup dan Tujuan UAT) lengkap.
  - [ ] Bab 3 (Organisasi dan Peran UAT) lengkap.
  - [ ] Bab 4 (Prasyarat dan Kesiapan UAT) lengkap.
  - [ ] Bab 5 s.d. Bab 13 (44 skrip UAT individual) semua ada dan lengkap.
  - [ ] Bab 14 (Skenario E2E) ada dan lengkap.
  - [ ] Bab 15 (Pengujian Non-Fungsional) ada dan lengkap.
  - [ ] Bab 16 (Prosedur Defect Handling) ada dan lengkap.
  - [ ] Bab 17 (Kriteria Keluar dan Sign-Off) ada dan lengkap.
  - [ ] Bab 18 (Lampiran: Glosarium, Test Fixtures, Matriks Ketertelusuran) ada dan lengkap.
  - [ ] Bab 19 (Referensi Dokumen) ada dan lengkap di akhir file.

- [ ] **F.2** Lakukan penghitungan akhir: pastikan tabel matriks ketertelusuran (Bab 18.3) memiliki tepat **44 baris data** (UAT-001 s.d. UAT-044), tidak lebih, tidak kurang.

- [ ] **F.3** Pastikan seluruh perubahan sudah terangkum dalam baris changelog versi terbaru di tabel Riwayat Perubahan Dokumen.

---

## 6. Catatan Penting untuk Pelaksana

> **PERINGATAN — NO TRUNCATION:** Saat menimpa (overwrite) file target di Fase E, pastikan **seluruh** konten dokumen ditulis ulang secara lengkap. Jangan pernah menghentikan penulisan di tengah dokumen atau merangkum bagian manapun. Dokumen UAT Script ini memiliki lebih dari 1.400 baris — seluruhnya harus ditulis ulang tanpa satu baris pun yang terlewat.

> **PERINGATAN — PLACEHOLDER EKSEKUSI:** Field `Hasil Aktual`, `Status`, dan `Catatan Temuan` pada setiap skrip UAT **HARUS** tetap diisi dengan teks placeholder eksekusi (contoh: `*[Diisi saat eksekusi UAT]*`). Jangan pernah mengisi field ini dengan data fiktif atau asumsi, karena field ini hanya boleh diisi saat eksekusi UAT berlangsung secara nyata.

> **PERINGATAN — VERSI DOKUMEN:** Setelah selesai direvisi, versi dokumen **HARUS** dinaikkan dari v1.1 menjadi v1.2 (atau increment berikutnya), baik pada header YAML maupun pada tabel Riwayat Perubahan Dokumen. Ini adalah tanda formal bahwa dokumen telah direvisi.

> **PERINGATAN — REFERENSI BARU:** Jika dalam proses validasi Anda menemukan file referensi tambahan yang dirujuk dalam isi dokumen tetapi belum tercantum di Bab 19 (Referensi Dokumen), tambahkan file tersebut sebagai baris baru di tabel referensi di Bab 19. Jangan tinggalkan referensi yang terpakai tanpa dokumentasi.

---

## 7. Referensi File Issue Terdahulu yang Relevan

Sebagai tambahan konteks, issue validasi dokumen SDLC yang sudah dikerjakan sebelumnya pada fase testing ini adalah:

| No | Nomor Issue | Target Dokumen | Path Issue |
|----|-------------|----------------|------------|
| 1 | 0084 | Test Plan v1.1 | `docs/issue/0084_issue_validasi_test_plan.md` |
| 2 | 0085 | Test Cases v1.1 | `docs/issue/0085_issue_validasi_test_cases.md` |

---

*Issue ini dibuat secara otomatis oleh Antigravity AI pada 2026-05-29 untuk dieksekusi oleh Junior Programmer atau AI model yang lebih murah/kecil.*
