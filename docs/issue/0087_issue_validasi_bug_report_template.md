# Issue: Validasi & Audit Komprehensif Dokumen Bug Report Template v1.1

## Metadata Issue

| Atribut         | Nilai                                                                      |
|-----------------|----------------------------------------------------------------------------|
| **Judul**       | Validasi & Audit Komprehensif Dokumen Bug Report Template                  |
| **Target File** | `docs/sdlc/05_testing/04_bug_report_template.md`                           |
| **Lokasi Referensi** | `docs/sdlc/`                                                          |
| **Tipe**        | Documentation Audit & Validation                                           |
| **Prioritas**   | High                                                                       |
| **Fase SDLC**   | Fase 05 — Testing                                                          |
| **Dibuat**      | 2026-05-29                                                                 |
| **Ditugaskan Ke** | Junior Programmer / AI Agent                                             |

---

## 1. Persona Auditor

Anda adalah **Principal QA Architect & SDLC Documentation Auditor** — seorang ahli senior yang memiliki kompetensi gabungan antara:

- **Quality Assurance Engineering** (IEEE 1044 Defect Classification, Bug Lifecycle Management, SLA-based defect tracking, Test Case traceability).
- **Software Documentation Standards** (IEEE 829, ISO/IEC/IEEE 29119, standar penulisan dokumen teknis industri perangkat lunak).
- **Domain Percetakan & Sistem Kasir** (memahami konteks bisnis AbuCom: transaksi kasir, kalkulasi HPP desimal, BOM stempel, RBAC multi-peran, dual-OS Windows/Linux, dan CLI-based interface).
- **Bahasa Indonesia Teknis** (mampu menilai kejelasan, ambiguitas, dan kealamiahan kalimat bahasa Indonesia dalam konteks dokumentasi teknis).

Sebagai auditor, Anda **tidak boleh toleran** terhadap:
- Data atau referensi yang tidak konsisten antar dokumen.
- Field template yang masih berisi placeholder instruksi bukan data riil.
- Informasi dari referensi yang relevan namun tidak diserap oleh dokumen ini.
- Konten yang tidak relevan, mubazir, atau tidak sesuai dengan scope Bug Report Template.
- Kalimat bahasa Indonesia yang ambigu, kaku, tidak natural, atau membingungkan pelaksana junior.

---

## 2. Latar Belakang & Tujuan Issue

Dokumen `04_bug_report_template.md` saat ini berada pada versi `v1.1` (status: Reviewed). Dokumen ini adalah deliverable keempat pada Fase 05 Testing dan menjadi **acuan formal tunggal** bagi seluruh tim (QA Engineer, Junior Programmer, UAT Tester, Pemilik Usaha) dalam memformat, mencatat, mengklasifikasi, dan mengelola siklus hidup temuan cacat (*defect*) sistem AbuCom.

Issue ini menginstruksikan pelaksanaan audit menyeluruh untuk memastikan:
1. Dokumen menyerap **seluruh** data relevan dari semua file referensi yang dicantumkan.
2. Dokumen **hanya** memuat konten yang memang sesuai dengan scope Bug Report Template (tidak ada konten asing).
3. Dokumen memiliki struktur yang memenuhi **standar industri** (IEEE 829, ISO/IEC/IEEE 29119).
4. Dokumen **layak** dijadikan input bagi fase SDLC selanjutnya (Test Execution, Defect Log, Test Summary Report).
5. Dokumen menggunakan **Bahasa Indonesia teknis** yang natural, tidak ambigu, dan mudah dipahami junior.
6. Dokumen **tidak memiliki data kosong** atau placeholder yang perlu diisi secara manual oleh pembaca.
7. Seluruh hasil perbaikan dituangkan kembali ke file target dengan **overwrite penuh tanpa pemotongan**.

---

## 3. Daftar File Referensi yang Wajib Dibaca

Sebelum memulai audit, bacalah dan pahami **seluruh** file referensi berikut. Setiap file harus dibaca dari baris pertama hingga baris terakhir:

| No | Kode Ref | Path File Referensi | Poin Utama yang Harus Diserap |
|----|----------|---------------------|-------------------------------|
| 1 | **R-TP** | `docs/sdlc/05_testing/01_test_plan.md` | Daftar 10 modul (M.1–M.10) beserta nama resminya, 44 skenario uji, nama database sandbox `abucom_test_db`, spesifikasi lingkungan testing, kriteria sign-off, dan definisi scope pengujian. |
| 2 | **R-TC** | `docs/sdlc/05_testing/02_test_cases.md` | 70 kasus uji operasional, konvensi penamaan TC (`TC-[MODUL]-[SKENARIO]-[URUT]`), data fixtures 8 akun uji beserta username/password/peran, dan format Test Case Registry. |
| 3 | **R-UAT** | `docs/sdlc/05_testing/03_uat_script.md` | Prosedur defect handling UAT, klasifikasi tingkat keparahan UAT, alur eskalasi temuan UAT, format ID `UAT-BUG-XXX`, kriteria keluar UAT (exit criteria), dan definisi sign-off UAT. |
| 4 | **R-SRS** | `docs/sdlc/02_analysis/02_software_requirements.md` | Daftar lengkap ID kebutuhan fungsional (SRS-F-001 s.d SRS-F-040) dan non-fungsional (SRS-NF-001 s.d SRS-NF-011) yang dapat dilanggar oleh bug. |
| 5 | **R-SEC** | `docs/sdlc/03_design/06_security_design.md` | Spesifikasi keamanan: bcrypt cost factor 12, JWT 8 jam, RBAC 8 peran, audit log JSON, enkripsi Fernet, SOP insiden keamanan, dan protokol pelaporan celah keamanan. |
| 6 | **R-CLI** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Format kode error visual terminal `⛔ ERR-XXX-YYY`, seluruh 30 kode error sistem beserta pesan dan skenario pemicunya, formatting `rich`/`tabulate`, dan spesifikasi struk thermal 32/48 karakter. |
| 7 | **R-ACM** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Matriks kontrol akses: 8 peran pengguna, hak akses per menu/modul, dan daftar akun fixture dengan peran masing-masing. |
| 8 | **R-DB** | `docs/sdlc/03_design/01_database_schema.sql` | Nama kolom tabel yang kritis (terutama `depresiasi_bulanan` di tabel `aset`), constraint DDL (Unique Key, FK, CHECK), dan nama tabel yang terlibat dalam skenario bug DB. |
| 9 | **R-BOM** | `docs/sdlc/03_design/05_bom_hpp_design.md` | Logika kalkulasi HPP, rumus BOM stempel kustom, spesifikasi presisi `Decimal(15,4)` dan `ROUND_HALF_UP`. |
| 10 | **R-NAR** | `docs/sdlc/narasi.txt` | Narasi proyek AbuCom: konteks bisnis, deskripsi modul, dan teknologi stack yang digunakan. |

---

## 4. Instruksi Audit — Tahapan Demi Tahapan

Ikuti seluruh langkah di bawah ini secara **berurutan**. Tandai setiap checkbox `[ ]` menjadi `[x]` saat selesai dikerjakan. **Jangan melompati langkah.**

---

### TAHAP 0 — Persiapan Lingkungan Kerja

- [ ] **T0-1**: Baca seluruh isi file target `docs/sdlc/05_testing/04_bug_report_template.md` dari baris 1 hingga baris terakhir. Pastikan tidak ada bagian yang dilewati.
- [ ] **T0-2**: Baca seluruh isi `docs/sdlc/05_testing/01_test_plan.md` (R-TP). Catat: nama resmi 10 modul M.1–M.10, spesifikasi database sandbox, jumlah skenario uji, dan kriteria sign-off.
- [ ] **T0-3**: Baca seluruh isi `docs/sdlc/05_testing/02_test_cases.md` (R-TC). Catat: 8 akun fixture (username, password, peran), konvensi penamaan TC, dan jumlah total Test Cases.
- [ ] **T0-4**: Baca seluruh isi `docs/sdlc/05_testing/03_uat_script.md` (R-UAT). Catat: format ID bug UAT, alur defect handling UAT, kriteria exit UAT, dan definisi sign-off UAT.
- [ ] **T0-5**: Baca seluruh isi `docs/sdlc/02_analysis/02_software_requirements.md` (R-SRS). Catat: range ID SRS-F dan SRS-NF yang valid beserta deskripsinya.
- [ ] **T0-6**: Baca seluruh isi `docs/sdlc/03_design/06_security_design.md` (R-SEC). Catat: spesifikasi teknis keamanan yang relevan untuk klasifikasi bug CAT-SEC.
- [ ] **T0-7**: Baca seluruh isi `docs/sdlc/03_design/04_cli_interaction_flow.md` (R-CLI). Catat: seluruh kode error `ERR-XXX-YYY` (harus berjumlah 30), format pesan error, dan spesifikasi rendering terminal.
- [ ] **T0-8**: Baca seluruh isi `docs/sdlc/02_analysis/06_access_control_matrix.md` (R-ACM). Catat: 8 peran pengguna dan daftar akun fixture dengan hak akses masing-masing.
- [ ] **T0-9**: Baca seluruh isi `docs/sdlc/03_design/01_database_schema.sql` (R-DB). Catat: nama kolom kritis (khususnya tabel `aset`), tipe data Decimal, dan constraint DDL yang relevan untuk bug CAT-DB dan CAT-DEC.
- [ ] **T0-10**: Baca seluruh isi `docs/sdlc/03_design/05_bom_hpp_design.md` (R-BOM). Catat: rumus HPP, spesifikasi Decimal(15,4), dan logika ROUND_HALF_UP.
- [ ] **T0-11**: Baca seluruh isi `docs/sdlc/narasi.txt` (R-NAR). Pahami konteks bisnis percetakan dan teknologi stack AbuCom.

---

### TAHAP 1 — Validasi Kelengkapan: Komparasi Mendalam Dokumen vs Referensi

> **Tujuan**: Memastikan dokumen telah menyerap **semua** data dan informasi yang relevan dari seluruh file referensi. Tidak boleh ada data penting yang terlewat.

- [ ] **T1-1** *(vs R-TP)*: Verifikasi bahwa 10 modul pada **Bab 5.2** (Pemetaan Kategori Bug ke Modul) menggunakan **nama resmi yang persis sama** dengan yang tercantum di Test Plan v1.1. Jika ada perbedaan nama, catat perbaikannya.
- [ ] **T1-2** *(vs R-TP)*: Verifikasi bahwa diagram posisi dokumen pada **Bab 1.3** sudah merepresentasikan urutan deliverable yang benar (Test Plan → Test Cases → UAT Script → Bug Report Template → Test Execution).
- [ ] **T1-3** *(vs R-TP)*: Verifikasi bahwa jumlah skenario uji yang disebutkan di **Bab 1.4** (44 skenario) dan jumlah modul (10 modul M.1–M.10) konsisten dengan Test Plan v1.1.
- [ ] **T1-4** *(vs R-TC)*: Verifikasi bahwa jumlah Test Cases yang disebutkan di **Bab 1.4** (70 kasus uji) dan jumlah akun fixture (8 akun) konsisten dengan Test Cases v1.1.
- [ ] **T1-5** *(vs R-TC)*: Verifikasi bahwa username dan peran akun fixture yang digunakan di seluruh 7 contoh laporan bug (**Bab 6.3 – 6.9**) sudah konsisten dengan data fixtures aktual di Test Cases v1.1.
- [ ] **T1-6** *(vs R-UAT)*: Verifikasi bahwa **Bab 8.2** (Hubungan Bug Report dengan UAT Script) sudah merujuk Bab yang benar dari UAT Script v1.1 mengenai alur defect handling UAT.
- [ ] **T1-7** *(vs R-UAT)*: Verifikasi bahwa kriteria penutupan UAT yang disebutkan di **Bab 8.2** (tidak boleh ada Blocker/Critical/Major terbuka) konsisten dengan exit criteria UAT Script v1.1.
- [ ] **T1-8** *(vs R-SRS)*: Verifikasi bahwa seluruh referensi SRS ID (`SRS-F-XXX`, `SRS-NF-XXX`) yang dikutip di **7 contoh laporan bug** (Bab 6.3–6.9) dan **Bab 8.3** (Matriks Traceability) sudah valid dan sesuai dengan cakupan kebutuhan di SRS v1.1.
- [ ] **T1-9** *(vs R-SRS)*: Verifikasi bahwa range SRS yang disebutkan di **Bab 1.4** (SRS-F-001 s.d SRS-F-040 dan SRS-NF-001 s.d SRS-NF-011) akurat.
- [ ] **T1-10** *(vs R-SEC)*: Verifikasi bahwa spesifikasi keamanan yang disebutkan di seluruh dokumen (bcrypt cost factor 12, JWT 8 jam, RBAC, audit log JSON, enkripsi Fernet) sudah konsisten dengan Security Design v1.1.
- [ ] **T1-11** *(vs R-CLI)*: Verifikasi bahwa **Bab 10.2** (Daftar Kode Error Sistem AbuCom) mencantumkan **tepat 30 kode error** sesuai dengan CLI Interaction Flow v1.1. Bandingkan satu per satu: kode error, string pesan, dan skenario pemicu. Jika ada yang tidak cocok atau kurang, catat perbaikannya.
- [ ] **T1-12** *(vs R-CLI)*: Verifikasi bahwa format kode error visual `⛔ ERR-XXX-YYY` yang dikutip di seluruh contoh laporan bug sudah konsisten dengan format yang didefinisikan di CLI Interaction Flow v1.1.
- [ ] **T1-13** *(vs R-CLI)*: Verifikasi bahwa spesifikasi lebar struk thermal (32 dan 48 karakter) yang disebutkan di contoh bug DEF-CLI-001 (**Bab 6.6**) sesuai dengan spesifikasi rendering di CLI Interaction Flow v1.1.
- [ ] **T1-14** *(vs R-ACM)*: Verifikasi bahwa 8 peran pengguna yang disebutkan di **Bab 5.2** dan seluruh contoh laporan bug sudah konsisten dengan ACM v1.1 (nama peran tidak boleh berbeda huruf besar/kecil).
- [ ] **T1-15** *(vs R-DB)*: Verifikasi bahwa nama kolom `depresiasi_bulanan` yang digunakan di **Bab 5.2** (M.6) dan contoh bug DEF-DEC-001 (**Bab 6.5**) sesuai dengan nama kolom aktual di DDL database schema.
- [ ] **T1-16** *(vs R-DB)*: Verifikasi bahwa nama-nama tabel database yang disebutkan di seluruh contoh bug (`transaksi`, `aset`, `audit_logs`, `system_configs`, dll.) sesuai dengan tabel yang didefinisikan di DDL database schema.
- [ ] **T1-17** *(vs R-BOM)*: Verifikasi bahwa rumus dan spesifikasi presisi desimal yang disebutkan di contoh bug DEF-DEC-001 (**Bab 6.5**) — yaitu `Decimal('166666.6667')` dengan `ROUND_HALF_UP` 4 desimal — konsisten dengan logika kalkulasi di BOM & HPP Design v1.1.
- [ ] **T1-18** *(vs R-NAR)*: Verifikasi bahwa deskripsi konteks bisnis AbuCom yang ada di **Bab 1.1** dan **Bab 1.2** konsisten dengan narasi proyek.

---

### TAHAP 2 — Validasi Relevansi: Cek Kesesuaian & Fokus Konten

> **Tujuan**: Memastikan dokumen **hanya** memuat konten yang relevan dan spesifik untuk Bug Report Template. Identifikasi konten asing, duplikat, atau konten yang lebih cocok berada di dokumen lain.

- [ ] **T2-1**: Periksa apakah ada subbab atau paragraf yang membahas topik di luar scope Bug Report Template (misalnya: prosedur coding, konfigurasi server, panduan instalasi). Jika ada, tandai untuk dihapus atau dipindahkan ke dokumen yang tepat.
- [ ] **T2-2**: Periksa apakah **Bab 2** (Klasifikasi Severity) dan **Bab 3** (Klasifikasi Priority) hanya memuat informasi yang relevan untuk kebutuhan pelaporan bug. Pastikan tidak ada duplikasi dengan definisi yang sudah ada di Test Plan atau UAT Script, kecuali memang diperlukan sebagai referensi mandiri.
- [ ] **T2-3**: Periksa apakah **Bab 4** (Siklus Hidup Bug) mencakup semua status bug yang relevan untuk konteks proyek AbuCom dan tidak memuat status yang tidak digunakan.
- [ ] **T2-4**: Periksa apakah **Bab 5** (Kategori Bug) hanya memuat kategori yang memang relevan dengan risiko bug sistem AbuCom. Verifikasi apakah ada kategori yang perlu ditambahkan berdasarkan referensi (R-SRS, R-DB, R-SEC).
- [ ] **T2-5**: Periksa apakah **Bab 6** (Template Formulir) mencakup semua field yang dibutuhkan oleh siklus manajemen defect AbuCom. Bandingkan dengan field yang dirujuk di UAT Script v1.1 untuk temuan UAT-BUG.
- [ ] **T2-6**: Periksa apakah **Bab 7** (Prosedur Eskalasi) relevan dan cukup operasional untuk tim AbuCom. Pastikan tidak ada prosedur yang terlalu umum dan tidak spesifik terhadap konteks toko percetakan.
- [ ] **T2-7**: Periksa apakah **Bab 8** (Integrasi dengan Proses Pengujian) tidak menduplikasi konten yang sudah ada di Test Cases v1.1 atau UAT Script v1.1 secara berlebihan.
- [ ] **T2-8**: Periksa apakah **Bab 9** (Metrik dan Pelaporan) hanya memuat metrik yang relevan untuk manajemen defect, bukan metrik pengujian umum yang lebih cocok di Test Plan.
- [ ] **T2-9**: Periksa apakah **Bab 10.1** (Glosarium) hanya mendefinisikan istilah yang memang digunakan di dalam dokumen ini dan tidak mendefinisikan istilah yang tidak muncul sama sekali di dokumen.
- [ ] **T2-10**: Periksa apakah **Bab 10.2** (Daftar Kode Error) merupakan konten yang tepat ada di dokumen ini sebagai alat bantu pelaporan bug, bukan konten yang harusnya eksklusif di CLI Interaction Flow.

---

### TAHAP 3 — Validasi Struktur: Standar Dokumen Industri

> **Tujuan**: Memastikan dokumen memiliki struktur, hierarki, dan kelengkapan elemen yang sesuai dengan standar dokumen defect management industri perangkat lunak (IEEE 829, ISO/IEC/IEEE 29119-3).

- [ ] **T3-1**: Verifikasi bahwa header YAML frontmatter (baris 1–11) sudah terisi lengkap dan benar: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`, `fase_sdlc`, `reviewer`, `disetujui_oleh`.
- [ ] **T3-2**: Verifikasi bahwa **Bab 1** (Informasi Dokumen) memuat semua sub-elemen standar: tujuan, cakupan, posisi SDLC, hubungan input/output, audiens target, definisi akronim, dan konvensi penamaan.
- [ ] **T3-3**: Verifikasi apakah konvensi penamaan ID Bug di **Bab 1.7** sudah mencakup semua tipe ID yang digunakan di seluruh dokumen (DEF-[MODUL]-[NOMOR_URUT] dan UAT-BUG-[NOMOR_URUT]).
- [ ] **T3-4**: Verifikasi bahwa **Bab 2** (Severity Classification) mencantumkan standar referensi yang dipakai (IEEE 1044) dan tabel severity sudah memiliki 5 level (S1–S5) lengkap dengan contoh konkret konteks AbuCom.
- [ ] **T3-5**: Verifikasi bahwa **Bab 3** (Priority Classification) memiliki tabel priority (P1–P4) dengan SLA yang jelas dan matriks Severity vs Priority yang komprehensif.
- [ ] **T3-6**: Verifikasi bahwa **Bab 4** (Bug Lifecycle) memiliki: (a) diagram state transition yang valid (menggunakan Mermaid `stateDiagram-v2`), (b) deskripsi semua status, dan (c) aturan transisi antar status beserta peran yang berwenang.
- [ ] **T3-7**: Verifikasi bahwa **Bab 5** (Bug Category) memiliki: (a) tabel kategori dengan kode, nama, dan deskripsi teknis, dan (b) matriks pemetaan kategori ke modul.
- [ ] **T3-8**: Verifikasi bahwa **Bab 6** (Template Formulir) memiliki semua sub-elemen wajib: (a) tabel template field lengkap, (b) panduan pengisian (4 prinsip Good Bug Report), (c) standar penulisan langkah reproduksi, dan (d) **minimal 7 contoh pengisian konkret** yang mencakup berbagai kategori bug (Fungsional, Keamanan, Desimal, CLI, DB, Performa, Kompatibilitas).
- [ ] **T3-9**: Verifikasi bahwa **Bab 7** (Prosedur Eskalasi) memiliki: (a) flowchart alur pelaporan Mermaid yang valid, (b) peran dan tanggung jawab yang terdefinisi jelas, (c) tabel SLA per severity level, dan (d) protokol khusus bug keamanan.
- [ ] **T3-10**: Verifikasi bahwa **Bab 8** (Integrasi Pengujian) memiliki: (a) hubungan dengan Test Case, (b) hubungan dengan UAT Script, dan (c) matriks traceability Bug → Test Case → SRS → Use Case yang mencakup semua 7 contoh bug.
- [ ] **T3-11**: Verifikasi bahwa **Bab 9** (Metrik) memiliki: (a) template dashboard statistik bug yang dapat langsung dipakai, dan (b) daftar semua metrik kualitas yang dilacak dengan definisi jelas (minimal 7 metrik: Bug Discovery Rate, Resolution Rate, Reopen Rate, MTTR, Defect Density, Escaped Defect Rate, MTTD).
- [ ] **T3-12**: Verifikasi bahwa **Bab 10** (Lampiran) memiliki: (a) glosarium istilah manajemen bug, (b) daftar 30 kode error sistem yang lengkap, (c) template bug report kosong siap-salin, dan (d) checklist kelengkapan laporan bug (minimal 10 poin).
- [ ] **T3-13**: Verifikasi bahwa **Bab 11** (Referensi Dokumen) memuat tabel referensi dengan kolom: No, Kode Ref, Nama Dokumen, Path Berkas Relatif, dan Versi untuk **semua** dokumen yang dirujuk dalam penyusunan dokumen ini.
- [ ] **T3-14**: Verifikasi bahwa **Bab 12** (Lembar Validasi Dokumen) sudah ada dan memuat: (a) catatan persetujuan formal, (b) kolom keputusan validasi, dan (c) tanda tangan formal Pemilik Usaha dan Kepala Percetakan.
- [ ] **T3-15**: Verifikasi bahwa **Riwayat Perubahan Dokumen** (di bagian awal) sudah mencatat semua versi perubahan dengan kolom: Versi, Tanggal, Deskripsi Perubahan, dan Oleh.

---

### TAHAP 4 — Validasi Kelayakan sebagai Referensi Fase SDLC Selanjutnya

> **Tujuan**: Memastikan dokumen ini cukup lengkap dan jelas untuk dijadikan input formal bagi proses Test Execution, Defect Log, dan Test Summary Report.

- [ ] **T4-1**: Verifikasi apakah **template formulir bug** (Bab 6.1 dan 10.3) sudah cukup operasional untuk langsung digunakan tanpa perlu konsultasi dokumen lain. Semua field harus memiliki aturan pengisian yang jelas.
- [ ] **T4-2**: Verifikasi apakah **konvensi ID Bug** (Bab 1.7) sudah cukup jelas untuk memungkinkan AI Agent atau Junior Programmer menghasilkan ID yang unik dan konsisten tanpa ambiguitas.
- [ ] **T4-3**: Verifikasi apakah **kriteria kelayakan Go-Live** berdasarkan status bug sudah terdefinisi secara eksplisit. Pastikan ada pernyataan yang jelas tentang kondisi apa yang harus terpenuhi sebelum sistem dinyatakan layak rilis.
- [ ] **T4-4**: Verifikasi apakah **format Lampiran/Evidence** (field di Bab 6.1) cukup jelas menjelaskan format dan lokasi penyimpanan file bukti (screenshot, stacktrace log).
- [ ] **T4-5**: Verifikasi apakah **matriks traceability** di Bab 8.3 sudah cukup lengkap untuk digunakan sebagai dasar rekonsiliasi data defect di Test Summary Report.
- [ ] **T4-6**: Verifikasi apakah **template Bug Summary Dashboard** di Bab 9.1 sudah memuat semua metrik yang dibutuhkan untuk keputusan Go-Live (termasuk status kelayakan yang eksplisit).
- [ ] **T4-7**: Verifikasi apakah **checklist kelengkapan bug report** di Bab 10.4 sudah memuat kriteria yang cukup untuk memastikan kualitas laporan bug yang dikirimkan ke QA Lead.
- [ ] **T4-8**: Verifikasi apakah setiap contoh laporan bug (Bab 6.3–6.9) sudah cukup mewakili **skenario kritis** yang perlu diantisipasi selama testing AbuCom, mencakup: Fungsional (S2-Critical), Keamanan (S2-Critical), Desimal (S2-Critical), CLI (S5-Cosmetic), Database (S2-Critical), Performa (S3-Major), dan Kompatibilitas (S5-Cosmetic).

---

### TAHAP 5 — Validasi Bahasa Indonesia

> **Tujuan**: Memastikan dokumen ditulis dalam Bahasa Indonesia teknis yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh Junior Programmer atau AI Agent yang lebih kecil.

- [ ] **T5-1**: Baca seluruh dokumen sekali lagi secara khusus dari sudut pandang kejelasan bahasa. Identifikasi kalimat yang terasa janggal, kaku (terjemahan harfiah dari bahasa Inggris), atau sulit dipahami tanpa konteks tambahan.
- [ ] **T5-2**: Periksa apakah istilah teknis yang pertama kali muncul selalu didefinisikan atau diberi keterangan dalam tanda kurung (misalnya: *severity (tingkat keparahan)*). Istilah yang sudah masuk Glosarium Bab 10.1 tidak perlu didefinisikan ulang di setiap kemunculan.
- [ ] **T5-3**: Periksa apakah **Bab 6.2** (Panduan Pengisian) menggunakan bahasa yang cukup operasional dan instruktif. Pastikan tidak ada instruksi yang membingungkan seorang penguji pertama kali.
- [ ] **T5-4**: Periksa apakah **Bab 4.3** (Aturan Transisi Status) menggunakan bahasa yang tidak ambigu tentang siapa boleh melakukan apa. Semua aturan harus menggunakan kalimat aktif dan eksplisit.
- [ ] **T5-5**: Periksa apakah ada penggunaan kata "dll.", "dan lain-lain", atau "dsb." yang tidak diikuti oleh daftar lengkap. Dalam dokumen teknis, ambiguitas seperti ini harus dieleminasi dengan menuliskan daftar lengkapnya.
- [ ] **T5-6**: Periksa konsistensi penulisan istilah bilingual: pastikan setiap istilah teknis bahasa Inggris yang memiliki terjemahan resmi dalam dokumen ini selalu ditulis konsisten (tidak berganti-ganti antara versi Inggris dan Indonesia dalam satu paragraf yang sama).
- [ ] **T5-7**: Periksa apakah kalimat-kalimat dalam **Bab 7.1** (Flowchart Prosedur) dan deskripsi node diagram Mermaid sudah cukup deskriptif untuk dipahami tanpa harus melihat diagram.
- [ ] **T5-8**: Periksa apakah ada kalimat yang terlalu panjang (lebih dari 3 anak kalimat) yang bisa dipecah menjadi kalimat-kalimat lebih pendek tanpa kehilangan makna.

---

### TAHAP 6 — Validasi Kualitas & Kelengkapan Data (Anti-Interupsi)

> **Tujuan**: Memastikan tidak ada pertanyaan yang akan menghambat proses fase SDLC selanjutnya akibat data yang tidak lengkap, ambigu, atau memerlukan klarifikasi.

- [ ] **T6-1**: Periksa seluruh dokumen dari baris pertama hingga terakhir. Identifikasi setiap field atau kalimat yang masih menggunakan placeholder generik seperti `[DIISI]`, `[TBD]`, `[TODO]`, `[Nama]`, `[Tanggal]`, atau format serupa yang menunjukkan data belum diisi.
- [ ] **T6-2**: Untuk setiap placeholder yang ditemukan pada **Bab 12** (Lembar Validasi Dokumen — kolom "Dibuat di" dan "Pada tanggal"): Evaluasi apakah placeholder ini memang **harus** diisi secara dinamis oleh Pemilik Usaha saat pengesahan, atau apakah ada nilai default yang bisa diisi. Jika placeholder ini adalah instruksi dinamis yang sah (bukan data yang bisa disimpulkan), biarkan tetapi pastikan teks instruksinya jelas.
- [ ] **T6-3**: Periksa apakah **Bab 12** (Lembar Validasi) memiliki data yang cukup untuk diisi: apakah nama pihak penandatangan sudah disebutkan secara eksplisit (bukan hanya posisi/jabatan)?
- [ ] **T6-4**: Verifikasi bahwa **Bab 9.1** (Bug Summary Dashboard) menggunakan data contoh yang konsisten dengan 7 contoh laporan bug yang ada di Bab 6 (total 7 bug, distribusi severity dan modul harus sesuai).
- [ ] **T6-5**: Verifikasi bahwa seluruh referensi internal lintas-bab di dalam dokumen ini (misalnya "lihat Bab X.Y", "sesuai klasifikasi Bab 5.1") menunjuk ke bab yang benar dan ada.
- [ ] **T6-6**: Verifikasi bahwa semua path file yang disebutkan di dalam dokumen (misalnya di kolom Lampiran/Evidence pada contoh bug: `exports/receipts/evidence_def_m1_001.png`) menggunakan konvensi path yang konsisten.
- [ ] **T6-7**: Verifikasi bahwa **Bab 1.7** (Konvensi Penamaan) mencakup semua kode modul yang digunakan: M1–M10, SEC, DEC, INT, CLI, NF. Pastikan semua kode ini konsisten dengan yang digunakan di Bab 5.1 dan seluruh contoh laporan bug.
- [ ] **T6-8**: Verifikasi bahwa nilai numerik yang disebutkan di **Bab 7.3** (SLA Tabel) konsisten dengan nilai yang disebutkan di **Bab 3.2** (Target SLA Priority) dan tidak ada inkonsistensi (misalnya: S1-Blocker SLA Respon ≤ 30 menit vs P1-Urgent SLA ≤ 4 jam).

---

### TAHAP 7 — Validasi Khusus Bug Report Template (Ciri Khas Dokumen)

> **Tujuan**: Memeriksa elemen-elemen yang spesifik untuk dokumen bertipe Bug Report Template, yang tidak dicakup oleh checklist umum.

- [ ] **T7-1**: **Konsistensi Contoh Bug**: Verifikasi bahwa seluruh 7 contoh laporan bug (DEF-M1-001, DEF-SEC-001, DEF-DEC-001, DEF-CLI-001, DEF-DB-001, DEF-PERF-001, DEF-COMPAT-001) memiliki seluruh 25 field formulir yang terisi lengkap dan tidak ada field yang kosong atau berisi placeholder.
- [ ] **T7-2**: **Validitas Test Case ID**: Verifikasi bahwa semua ID Test Case yang dikutip di contoh bug (TC-M1-003-02, TC-M7-002-02, TC-M6-002-01, TC-CLI-003-01, TC-INT-002-01, TC-NF-001-01, TC-CLI-002-01) sudah sesuai dengan konvensi penamaan TC di Test Cases v1.1 dan ID tersebut benar-benar ada.
- [ ] **T7-3**: **Validitas Use Case ID**: Verifikasi bahwa semua ID Use Case yang dikutip di contoh bug dan matriks traceability (UC-003, UC-032, UC-030, UC-006, UC-028, UC-043) valid berdasarkan SRS v1.1 atau dokumen Use Case yang ada.
- [ ] **T7-4**: **Representasi Contoh Bug**: Pastikan 7 contoh bug sudah mencakup semua 8 kategori bug yang didefinisikan di Bab 5.1 (CAT-FUNC, CAT-SEC, CAT-DEC, CAT-DB, CAT-CLI, CAT-PERF, CAT-COMPAT, CAT-CONFIG). Jika kategori CAT-CONFIG belum direpresentasikan dalam contoh, catat apakah perlu ditambahkan contoh baru atau cukup dengan keterangan.
- [ ] **T7-5**: **Template Kosong Bab 10.3**: Verifikasi bahwa template kosong di Bab 10.3 sudah mencakup semua field wajib yang ada di template tabel Bab 6.1, termasuk 4 field baru (Frekuensi Kemunculan, Apakah Ini Regression?, Workaround Tersedia?, OS/Platform Spesifik). Jika belum, tambahkan field yang kurang.
- [ ] **T7-6**: **Checklist Bab 10.4**: Verifikasi bahwa 10 poin checklist kelengkapan bug report di Bab 10.4 sudah mencakup: ID unik, judul deskriptif, traceability, severity & priority, langkah reproduksi, kontras hasil, lampiran, data fixtures, lingkungan sandbox, dan bebas placeholder.
- [ ] **T7-7**: **Matriks Traceability Bab 8.3**: Verifikasi bahwa kolom "Skenario Asal" di matriks traceability sudah menggunakan format ID skenario yang konsisten dengan Test Cases v1.1.
- [ ] **T7-8**: **Protokol Keamanan Bab 7.4**: Verifikasi bahwa 4 prinsip protokol keamanan (Konfidensialitas, Prioritas Otomatis, Eskalasi Langsung, Verifikasi Security Re-test) sudah lengkap dan operasional untuk konteks toko percetakan AbuCom.
- [ ] **T7-9**: **Kelengkapan Kode Error Bab 10.2**: Lakukan penghitungan ulang — pastikan tabel di Bab 10.2 benar-benar memiliki **30 baris** kode error (tidak lebih, tidak kurang). Jika ada ketidaksesuaian dengan CLI Interaction Flow v1.1, sinkronkan.
- [ ] **T7-10**: **Kolom Status RTM**: Verifikasi bahwa seluruh 30 baris di tabel kode error Bab 10.2 memiliki nilai kolom "Status RTM" yang terisi (tidak boleh kosong). Nilai yang diperbolehkan: `Cocok`, `Tidak Cocok`, atau `Perlu Verifikasi`.

---

### TAHAP 8 — Penyusunan Daftar Temuan & Perbaikan

> **Tujuan**: Mendokumentasikan semua temuan dari Tahap 1–7 sebelum menerapkan perbaikan ke file.

- [ ] **T8-1**: Buat daftar tertulis semua temuan audit dari Tahap 1–7 dengan format:
  ```
  [ID-Temuan] | [Tahap] | [Bab/Bagian] | [Deskripsi Masalah] | [Tindakan Perbaikan]
  ```
  Contoh:
  ```
  T1-01 | Tahap 1 | Bab 5.2, Baris M.3 | Nama modul "Layanan Keuangan, PPOB & Jasa Service" tidak sesuai nama resmi di Test Plan | Ubah nama sesuai Test Plan v1.1
  ```
- [ ] **T8-2**: Kategorikan temuan ke dalam tipe: (a) **Inkonsistensi Data** (data tidak cocok antar dokumen), (b) **Konten Kurang** (informasi relevan yang belum diserap), (c) **Konten Tidak Relevan** (informasi yang tidak seharusnya ada), (d) **Masalah Struktur** (hierarki atau urutan bab), (e) **Masalah Bahasa** (kalimat ambigu/kaku), (f) **Data Kosong** (field/placeholder yang perlu diisi).
- [ ] **T8-3**: Tentukan prioritas perbaikan: (a) **Kritis** — harus diperbaiki agar dokumen valid, (b) **Penting** — perbaikan signifikan untuk kualitas, (c) **Minor** — perbaikan kecil/estetika.
- [ ] **T8-4**: Hitung total temuan. Jika total temuan = 0 (dokumen sudah sempurna), lanjut ke Tahap 9 dengan menyatakan "Tidak ada perubahan konten, hanya pembaruan versi."

---

### TAHAP 9 — Penulisan Ulang Dokumen (Overwrite Penuh)

> **Tujuan**: Menerapkan semua perbaikan dan menuangkan kembali seluruh dokumen yang telah divalidasi ke file target.

> ⚠️ **PERHATIAN KRITIS**: Instruksi penulisan di Tahap 9 ini bersifat **MUTLAK dan TIDAK BOLEH DILANGGAR**. Kegagalan mengikuti instruksi ini akan menghasilkan dokumen yang tidak valid dan rusak.

- [ ] **T9-1**: Susun dokumen hasil validasi yang sudah diperbaiki secara **lengkap dan utuh** — dari baris pertama (baris `---` header YAML) hingga baris terakhir (baris tanda tangan **Kepala Percetakan**). Tidak ada satu baris pun yang boleh dihilangkan, diringkas, atau dipotong.
- [ ] **T9-2**: Perbarui field **versi** di YAML frontmatter: ubah dari `versi: 1.1` menjadi `versi: 1.2`.
- [ ] **T9-3**: Perbarui field **tanggal** di YAML frontmatter: isi dengan tanggal hari eksekusi audit ini (format `YYYY-MM-DD`).
- [ ] **T9-4**: Perbarui field **status** di YAML frontmatter: ubah dari `Reviewed` menjadi `Validated`.
- [ ] **T9-5**: Tambahkan baris baru di tabel **Riwayat Perubahan Dokumen**:
  ```
  | **1.2** | [TANGGAL-AUDIT] | Hasil validasi komprehensif sesuai issue 0087. [Deskripsi singkat semua perbaikan yang dilakukan]. | Principal QA Architect & SDLC Documentation Auditor |
  ```
  Isi `[TANGGAL-AUDIT]` dengan tanggal eksekusi, dan `[Deskripsi singkat...]` dengan ringkasan temuan yang diperbaiki.
- [ ] **T9-6**: Terapkan seluruh perbaikan yang telah diidentifikasi di Tahap 8 ke dalam konten dokumen yang sesuai.
- [ ] **T9-7**: Jika dalam proses perbaikan digunakan dokumen referensi **baru** (yang belum ada di tabel Bab 11), tambahkan dokumen tersebut sebagai baris baru di tabel **Bab 11 (Referensi Dokumen)** di bagian akhir tabel.
- [ ] **T9-8**: Tulis ulang **seluruh isi dokumen yang sudah diperbaiki** ke file target menggunakan perintah **overwrite** (bukan append):
  - **Path file target**: `docs/sdlc/05_testing/04_bug_report_template.md`
  - **Metode penulisan**: Overwrite — timpa seluruh konten file dari baris 1 hingga EOF.
  - **Verifikasi**: Setelah penulisan selesai, baca ulang file yang baru ditulis untuk memastikan konten tidak terpotong di bagian tengah maupun akhir.
- [ ] **T9-9**: Baca ulang file `docs/sdlc/05_testing/04_bug_report_template.md` setelah overwrite. Verifikasi bahwa:
  - Baris pertama adalah `---` (header YAML).
  - Baris terakhir adalah baris tanda tangan `Kepala Percetakan`.
  - Versi dokumen di YAML frontmatter sudah berubah menjadi `1.2`.
  - Total baris file baru ≥ total baris file lama (tidak ada konten yang hilang).

---

### TAHAP 10 — Verifikasi Akhir

- [ ] **T10-1**: Hitung dan catat jumlah total temuan yang diperbaiki.
- [ ] **T10-2**: Konfirmasi bahwa setiap temuan dari daftar di Tahap 8 sudah diterapkan perbaikannya.
- [ ] **T10-3**: Konfirmasi bahwa versi dokumen sudah berubah menjadi `v1.2`.
- [ ] **T10-4**: Konfirmasi bahwa tidak ada data kosong atau placeholder yang belum terisi di seluruh dokumen (kecuali placeholder yang memang sah sebagai instruksi dinamis, seperti field tanggal di Lembar Validasi Bab 12).
- [ ] **T10-5**: Konfirmasi bahwa semua referensi silang internal dalam dokumen (misalnya "lihat Bab 3.3") menunjuk ke bab yang benar dan tidak ada referensi rusak akibat penambahan atau penggeseran bab.
- [ ] **T10-6**: Tulis laporan ringkas hasil audit dengan format:
  ```
  ## Laporan Ringkas Audit Issue 0087
  - Tanggal Audit: [TANGGAL]
  - Versi Sebelum: v1.1
  - Versi Sesudah: v1.2
  - Total Temuan: [N]
  - Temuan Kritis: [N] | Temuan Penting: [N] | Temuan Minor: [N]
  - Semua Temuan Diperbaiki: Ya / Tidak
  - Referensi Baru Ditambahkan: Ya ([daftar]) / Tidak
  - Status Akhir: SELESAI / PERLU REVIEW ULANG
  ```

---

## 5. Batasan & Larangan Keras

> **Bacalah batasan ini sebelum memulai eksekusi. Pelanggaran terhadap aturan ini akan menghasilkan output yang tidak dapat diterima.**

1. **DILARANG** menghapus bab atau sub-bab yang sudah ada kecuali ada bukti jelas bahwa konten tersebut tidak relevan dan konfirmasi eksplisit dari kriteria audit.
2. **DILARANG** meringkas, memotong, atau menyingkat bagian mana pun dari dokumen saat menulis ulang ke file target. Seluruh teks harus ditulis ulang sepenuhnya.
3. **DILARANG** mengganti contoh laporan bug yang sudah ada dengan contoh yang lebih pendek/ringkas. Contoh yang ada sudah dirancang untuk kelengkapan operasional.
4. **DILARANG** mengubah format ID Bug yang sudah ada (`DEF-M1-001`, `UAT-BUG-001`, dll.) tanpa alasan teknis yang kuat dan terdokumentasi.
5. **DILARANG** menghapus atau mengubah tabel kode error di Bab 10.2 tanpa memverifikasi terlebih dahulu dengan CLI Interaction Flow v1.1.
6. **DILARANG** mengisi field "Dibuat di" dan "Pada tanggal" di Bab 12 dengan data fiktif. Field ini hanya boleh diisi oleh Pemilik Usaha saat pengesahan resmi.
7. **DILARANG** menghentikan penulisan file sebelum mencapai baris terakhir dokumen (tanda tangan Kepala Percetakan). Jika terjadi error saat penulisan, mulai ulang dari awal, bukan melanjutkan dari tengah.

---

## 6. Kriteria Keberhasilan Issue

Issue ini dinyatakan **SELESAI** jika dan hanya jika seluruh kondisi berikut terpenuhi:

- [ ] Seluruh 74 checklist (T0 s.d T10) sudah ditandai `[x]` selesai.
- [ ] File `docs/sdlc/05_testing/04_bug_report_template.md` sudah diperbarui menjadi **versi `v1.2`**.
- [ ] Tidak ada data kosong atau placeholder yang belum terisi secara tepat di seluruh dokumen.
- [ ] Semua inkonsistensi data antara dokumen target dan file referensi sudah diselesaikan.
- [ ] Dokumen tetap memiliki **struktur yang tidak terpotong** (dari header YAML hingga lembar validasi).
- [ ] Laporan ringkas audit (T10-6) sudah ditulis dan dikonfirmasi.

---

## 7. Catatan Tambahan untuk Pelaksana

> **Untuk Junior Programmer atau AI Agent yang melaksanakan issue ini:**

1. **Bacalah seluruh instruksi issue ini terlebih dahulu** sebelum membuka file apapun. Pahami keseluruhan alur sebelum memulai eksekusi.
2. **Kerjakan tahap secara berurutan** — jangan melompati tahap atau mengerjakan secara paralel. Setiap tahap membangun pemahaman yang dibutuhkan tahap berikutnya.
3. **Jika menemukan inkonsistensi yang tidak tercover dalam instruksi ini**, catat sebagai temuan baru di Tahap 8 dan terapkan penilaian terbaik Anda berdasarkan konteks dokumen referensi.
4. **Jika file referensi tidak dapat dibaca** (path tidak ditemukan, file kosong, atau error akses), hentikan eksekusi dan laporkan error ini sebelum melanjutkan.
5. **Gunakan bahasa Indonesia yang sama** dengan yang sudah digunakan di dokumen target. Jangan mengubah gaya penulisan secara drastis kecuali ada temuan bahasa yang tidak natural.
6. **Simpan progress secara berkala** — setelah setiap Tahap selesai, catat temuan sebelum lanjut ke Tahap berikutnya agar tidak kehilangan hasil analisis jika terjadi gangguan.
