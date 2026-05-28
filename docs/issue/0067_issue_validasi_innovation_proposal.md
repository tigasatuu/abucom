# Validasi & Perbaikan Dokumen Innovation Proposal

## Informasi Issue

| Field              | Detail                                                                    |
|--------------------|---------------------------------------------------------------------------|
| **Judul**          | Validasi, Analisis, dan Perbaikan Komprehensif Dokumen Innovation Proposal |
| **Dokumen Utama**  | Innovation Proposal                                                       |
| **Target File**    | `docs/sdlc/01_planning/05_innovation_proposal.md`                         |
| **Lokasi Referensi** | `docs/sdlc/`                                                            |
| **Versi Saat Ini** | v1.1                                                                      |
| **Versi Target**   | v1.2                                                                      |
| **Prioritas**      | High                                                                      |
| **Tipe**           | Dokumentasi / Validasi                                                    |

---

## Persona Eksekutor

Kamu adalah seorang **Senior Technical Documentation Auditor & Innovation Strategy Analyst** dengan keahlian gabungan:

1. **Domain Expertise Percetakan & Retail UMKM Indonesia**: Menguasai standar operasional toko percetakan fisik (offset, digital, sublimasi, stempel), manajemen stok bahan baku industri (kertas, tinta, bahan kimia), serta ekosistem PPOB dan jasa keuangan agen bank di Indonesia.
2. **SDLC Governance & Documentation Standards**: Berpengalaman mengaudit dokumen SDLC berstandar industri (IEEE 830, ISO/IEC 12207) dan memahami alur dependensi antar dokumen perencanaan (Charter → Feasibility → Stakeholder → Tech Stack → Innovation Proposal → SRS → SDD).
3. **Software Architecture Validator**: Mampu menilai konsistensi antara usulan inovasi fitur dengan keputusan arsitektur teknis (Python Functional Programming murni, MySQL, CLI `rich`, JWT, bcrypt, LAN Server).
4. **Business Innovation Analyst**: Mampu mengevaluasi relevansi, kelengkapan, dan akurasi setiap usulan inovasi terhadap kebutuhan riil bisnis UMKM percetakan yang terdokumentasi.
5. **Bahasa Indonesia Technical Writer**: Mampu menilai dan memperbaiki kualitas bahasa teknis dalam Bahasa Indonesia agar natural, tidak ambigu, tidak bertele-tele, dan mudah dipahami oleh junior programmer atau AI model yang lebih kecil.

Dengan persona ini, lakukan audit yang **ketat, teliti, dan berorientasi pada standar industri sesungguhnya** — bukan sekadar pemeriksaan permukaan.

---

## Konteks Dokumen

Dokumen `05_innovation_proposal.md` adalah dokumen **ke-5 dan terakhir** dalam fase Planning SDLC AbuCom. Posisinya sangat strategis karena:

- Menjadi **jembatan konseptual** antara visi bisnis (Project Charter) dan keputusan teknis (Tech Stack Decision) menuju fase berikutnya (SRS dan SDD).
- Memuat **42 usulan inovasi** yang terbagi atas 30 inovasi terintegrasi (INV-INT), 3 rekomendasi sebelumnya (INV-REC), dan 9 inovasi baru AI (INV-NEW).
- Harus menjadi **input yang langsung dapat dikonsumsi** oleh tim yang mengerjakan SRS (Software Requirements Specification) tanpa memerlukan klarifikasi berulang.

Dokumen referensi yang **wajib dibaca sebelum melakukan validasi**:

| # | File Referensi | Path |
|---|---|---|
| 1 | Project Charter v1.1 | `docs/sdlc/01_planning/01_project_charter.md` |
| 2 | Feasibility Study v1.1 | `docs/sdlc/01_planning/02_feasibility_study.md` |
| 3 | Stakeholder Register v1.1 | `docs/sdlc/01_planning/03_stakeholder_register.md` |
| 4 | Tech Stack Decision v1.1 | `docs/sdlc/01_planning/04_tech_stack_decision.md` |
| 5 | Narasi Pemilik | `docs/sdlc/narasi.txt` |

---

## Tujuan Issue

Melakukan **validasi menyeluruh** terhadap dokumen Innovation Proposal dengan cara:

1. Memeriksa kelengkapan dan akurasi isi terhadap semua dokumen referensi.
2. Memastikan dokumen hanya memuat konten yang relevan dan spesifik untuk Innovation Proposal.
3. Memverifikasi standar struktur dokumen sesuai praktik industri.
4. Memastikan dokumen siap menjadi input andal bagi fase SDLC selanjutnya (SRS, SDD).
5. Memperbaiki kualitas bahasa Indonesia agar natural dan tidak ambigu.
6. Mengisi semua data kosong atau placeholder yang belum terisi.
7. Menimpa (overwrite) file target dengan versi yang telah disempurnakan secara penuh.

---

## Checklist Implementasi (Low-Level)

Ikuti setiap langkah secara berurutan. Jangan melompati langkah. Tandai `[x]` saat setiap tugas selesai dikerjakan.

---

### FASE 0 — Persiapan dan Pembacaan Dokumen

- [ ] **[0.1] Baca target file secara penuh dari baris pertama hingga baris terakhir.**
  - File: `docs/sdlc/01_planning/05_innovation_proposal.md`
  - Tujuan: Memahami seluruh isi, struktur, dan konteks dokumen sebelum melakukan komparasi.
  - Catatan: Jangan lewati satu baris pun. Perhatikan setiap kode inovasi (INV-INT-xx, INV-REC-xx, INV-NEW-xx).

- [ ] **[0.2] Baca dokumen referensi 1: Project Charter.**
  - File: `docs/sdlc/01_planning/01_project_charter.md`
  - Yang dicari: Semua kode modul [M.1]–[M.9], semua kode kebutuhan fungsional [F-x.x], semua kode kebutuhan non-fungsional [N-x.x], SMART Goals, tim pengembang, dan budget awal proyek.

- [ ] **[0.3] Baca dokumen referensi 2: Feasibility Study.**
  - File: `docs/sdlc/01_planning/02_feasibility_study.md`
  - Yang dicari: Analisis kelayakan per modul, proyeksi ROI/NPV/Payback Period, kendala finansial proyek, daftar risiko, dan kesimpulan kelayakan.

- [ ] **[0.4] Baca dokumen referensi 3: Stakeholder Register.**
  - File: `docs/sdlc/01_planning/03_stakeholder_register.md`
  - Yang dicari: Daftar posisi staf dan hak akses RBAC masing-masing peran, matriks modul vs stakeholder, dan regulasi ketenagakerjaan Indonesia yang disebutkan.

- [ ] **[0.5] Baca dokumen referensi 4: Tech Stack Decision.**
  - File: `docs/sdlc/01_planning/04_tech_stack_decision.md`
  - Yang dicari: Semua keputusan teknologi (bahasa, database, library keamanan, framework CLI), justifikasi teknis, versi library, dan keputusan arsitektur (LAN, FP murni, JWT, bcrypt, dll).

- [ ] **[0.6] Baca dokumen referensi 5: Narasi Pemilik.**
  - File: `docs/sdlc/narasi.txt`
  - Yang dicari: Deskripsi kondisi operasional toko, 5 divisi usaha, harapan pemilik terhadap sistem baru (terutama poin 3, 4, 5, 6), dan mandat inovasi di Baris 98.

---

### FASE 1 — Komparasi Mendalam: Kelengkapan Data dari Referensi

> **Tujuan**: Memastikan Innovation Proposal sudah merangkum **semua** data dan informasi penting yang ada di dokumen referensi yang relevan untuk dokumen ini.

- [ ] **[1.1] Komparasi dengan Project Charter.**
  - Periksa apakah semua 9 modul utama [M.1]–[M.9] tercermin dalam inovasi yang terdokumentasi di Bagian 4 dan 7.
  - Periksa apakah semua kebutuhan fungsional kritis [F-x.x] yang memiliki implikasi inovasi teknis sudah direpresentasikan.
  - Periksa apakah semua kebutuhan non-fungsional [N-x.x] yang terkait keamanan dan performa sudah dibuatkan inovasi pendukungnya.
  - Periksa apakah SMART Goals (5 tujuan spesifik) sudah semua tercakup di Bagian 3.3.
  - Periksa apakah ada divisi bisnis dari Project Charter yang belum dibuatkan usulan inovasinya sama sekali.

- [ ] **[1.2] Komparasi dengan Feasibility Study.**
  - Periksa apakah ada temuan risiko dari Feasibility Study yang belum dibuatkan rencana mitigasi inovasi di Bagian 9.
  - Periksa apakah proyeksi kelayakan finansial (ROI/NPV/Payback) dari Feasibility Study sudah disinggung di Bagian 2 (Ringkasan Eksekutif) atau di Bagian 6 sebagai justifikasi prioritas.
  - Periksa apakah estimasi biaya implementasi inovasi konsisten dengan anggaran proyek di Feasibility Study.

- [ ] **[1.3] Komparasi dengan Stakeholder Register.**
  - Periksa apakah inovasi RBAC (INV-INT-15) sudah mencakup semua peran staf yang ada di Stakeholder Register (bukan hanya Pemilik dan Staf generik, tapi juga posisi spesifik seperti kasir, staf gudang, desainer, teknisi).
  - Periksa apakah inovasi Shift Handover Log (INV-NEW-04) sudah menyebutkan posisi staf spesifik dari Stakeholder Register yang terlibat.
  - Periksa apakah regulasi ketenagakerjaan (PKWT/PKWTT) yang ada di Stakeholder Register perlu disinggung di konteks inovasi payroll atau kasbon.

- [ ] **[1.4] Komparasi dengan Tech Stack Decision.**
  - Periksa apakah setiap inovasi yang menyebutkan teknologi spesifik (bcrypt, JWT, rich, decimal, MySQL) konsisten dengan versi dan keputusan yang ada di Tech Stack Decision.
  - Periksa apakah ada keputusan teknologi di Tech Stack Decision yang memiliki implikasi inovasi signifikan namun belum tercantum di Innovation Proposal.
  - Periksa apakah penjelasan teknis inovasi FP Murni (INV-INT-02) sudah konsisten dengan batasan arsitektur di Tech Stack Decision Bagian 3.2.

- [ ] **[1.5] Komparasi dengan Narasi Pemilik.**
  - Periksa apakah semua harapan spesifik pemilik di narasi.txt (terutama poin 3, 4, 5, 6 yang terkait PPOB, jasa keuangan, service, dan pinjaman) sudah dibuatkan inovasi pendukungnya.
  - Periksa apakah kondisi operasional yang dideskripsikan pemilik (5 divisi usaha, pembukuan Excel manual, burnout) sudah tercermin akurat di Bagian 3.1.
  - Periksa apakah kutipan mandat inovasi di Bagian 3.2 sudah sesuai persis dengan teks di narasi.txt Baris 98.

- [ ] **[1.6] Catat semua gap (kekurangan) yang ditemukan** dalam format berikut di scratchpad sementara:
  ```
  [GAP-001] Sumber: <nama referensi> | Bagian: <bagian di referensi> | Kekurangan: <deskripsi singkat>
  ```

---

### FASE 2 — Validasi Relevansi Konten (Kebersihan Dokumen)

> **Tujuan**: Memastikan Innovation Proposal **hanya** memuat konten yang memang spesifik dan relevan untuk dokumen Innovation Proposal. Konten yang bukan tanggung jawab dokumen ini harus diidentifikasi.

- [ ] **[2.1] Periksa Bagian 2 (Ringkasan Eksekutif).**
  - Pastikan ringkasan eksekutif hanya memuat: angka total inovasi, kategori inovasi, dan dampak strategis terukur.
  - Tandai jika ada detail teknis implementasi yang terlalu dalam (yang seharusnya ada di SRS atau SDD, bukan di Innovation Proposal).

- [ ] **[2.2] Periksa setiap entri inovasi di Bagian 4 (30 inovasi terintegrasi).**
  - Setiap entri inovasi harus memiliki 4 field: Deskripsi Teknis, Justifikasi Bisnis, Sumber Data, dan Dampak Bisnis.
  - Tandai entri yang memiliki field yang tidak relevan dengan tanggung jawab Innovation Proposal (misalnya: detail implementasi kode Python spesifik yang seharusnya ada di SDD/Implementation Guide).
  - Tandai entri yang justifikasi bisnisnya lemah atau tidak terhubung langsung ke kebutuhan AbuCom yang terdokumentasi.

- [ ] **[2.3] Periksa setiap entri inovasi di Bagian 5 (12 inovasi tambahan).**
  - Pastikan setiap inovasi tambahan memiliki 5 field: Deskripsi, Justifikasi Bisnis, Dampak Operasional, Kompleksitas Implementasi, dan Fase Implementasi yang Direkomendasikan.
  - Periksa apakah ada inovasi yang terlalu jauh dari ruang lingkup bisnis AbuCom (percetakan UMKM, retail ATK, PPOB, jasa keuangan, jasa service).

- [ ] **[2.4] Periksa Bagian 6 (Matriks Kelayakan).**
  - Pastikan kolom dan baris sudah konsisten dengan jumlah inovasi yang terdaftar (30 inovasi terintegrasi di Tabel 6.1, dan 12 inovasi tambahan di Tabel 6.2).
  - Periksa apakah nilai kelayakan (Layak, Sangat Layak, Layak dengan Catatan) sudah konsisten dengan deskripsi risiko di Bagian 9.

- [ ] **[2.5] Periksa Bagian 7 (Pemetaan Inovasi terhadap Modul Sistem).**
  - Hitung jumlah baris inovasi di matriks — harus berjumlah 42 baris (30 INV-INT + 3 INV-REC + 9 INV-NEW).
  - Periksa apakah ada inovasi yang terdaftar di Bagian 4 dan 5 namun **belum** masuk ke dalam matriks Bagian 7.
  - Periksa konsistensi tanda `✓` dan `—` pada setiap baris — apakah sudah akurat secara logika bisnis (misalnya: INV-INT-25 Rekonsiliasi Kas hanya ditandai `✓` di M.7, apakah ini sudah tepat atau seharusnya juga di M.1?).

- [ ] **[2.6] Periksa Bagian 8 (Dampak terhadap Fase SDLC).**
  - Pastikan setiap sub-bagian (8.1 SRS, 8.2 SDD, 8.3 Implementation, 8.4 Testing, 8.5 Maintenance) menyebutkan instruksi yang cukup spesifik untuk menjadi panduan tim.
  - Konten di Bagian 8 harus berupa "instruksi dampak", bukan pengulangan deskripsi inovasi.

---

### FASE 3 — Validasi Standar Struktur Dokumen

> **Tujuan**: Memastikan Innovation Proposal memiliki standar struktur dokumen yang lengkap, sesuai, dan informatif sebagaimana dokumen praktik industri nyata.

- [ ] **[3.1] Periksa Frontmatter YAML (header dokumen).**
  - Pastikan field berikut ada dan terisi dengan benar:
    - `dokumen` : nama dokumen
    - `proyek` : nama proyek
    - `versi` : versi dokumen (harus diperbarui ke v1.2 setelah validasi selesai)
    - `tanggal` : tanggal penyusunan/revisi
    - `status` : status dokumen
    - `penyusun` : nama penyusun/persona

- [ ] **[3.2] Periksa kelengkapan section-level dokumen.**
  - Pastikan urutan dan keberadaan seksi berikut sudah ada:
    - [ ] Riwayat Perubahan Dokumen (Change Log)
    - [ ] Informasi Dokumen / Pendahuluan
    - [ ] Ringkasan Eksekutif (Executive Summary)
    - [ ] Latar Belakang dan Konteks Inovasi
    - [ ] Inovasi yang Sudah Terintegrasi (INV-INT)
    - [ ] Usulan Inovasi Tambahan / Rekomendasi Baru (INV-REC & INV-NEW)
    - [ ] Analisis Kelayakan Inovasi (Matriks)
    - [ ] Pemetaan Inovasi terhadap Modul Sistem
    - [ ] Dampak Inovasi terhadap Fase SDLC Selanjutnya
    - [ ] Risiko Inovasi dan Rencana Mitigasi
    - [ ] Persetujuan dan Otorisasi
    - [ ] Glosarium
    - [ ] Referensi Dokumen
  - Jika ada seksi yang hilang, tambahkan dengan konten yang sesuai standar dokumen Innovation Proposal industri.

- [ ] **[3.3] Periksa konsistensi penomoran seksi.**
  - Pastikan semua heading (H2, H3, H4) menggunakan penomoran yang hierarkis dan konsisten (1., 1.1., 1.1.1., dst.).
  - Pastikan tidak ada lompatan nomor atau penomoran ganda.

- [ ] **[3.4] Periksa kualitas Tabel Riwayat Perubahan (Change Log).**
  - Pastikan kolom ada: Versi, Tanggal, Perubahan, Oleh.
  - Pastikan setiap versi yang ada di Change Log memiliki deskripsi perubahan yang informatif (bukan hanya "diperbarui").
  - Pastikan kolom "Oleh" terisi dengan nama persona atau tim yang relevan.

- [ ] **[3.5] Periksa standar entri inovasi sebagai unit dokumentasi.**
  - Setiap entri inovasi (INV-INT, INV-REC, INV-NEW) harus memiliki **heading yang konsisten** menggunakan format `#### **[KODE]: [NAMA INOVASI]**`.
  - Setiap entri inovasi INV-INT harus memiliki **minimal 4 field**: Deskripsi Teknis, Justifikasi Bisnis, Sumber Data, Dampak Bisnis.
  - Setiap entri inovasi INV-REC dan INV-NEW harus memiliki **minimal 5 field**: Deskripsi, Justifikasi Bisnis, Dampak Operasional, Kompleksitas Implementasi, Fase Implementasi yang Direkomendasikan.
  - Tandai semua entri yang fieldnya tidak lengkap atau tidak konsisten.

- [ ] **[3.6] Periksa kelengkapan matriks pemetaan modul (Bagian 7).**
  - Pastikan jumlah kolom modul adalah 9 (M.1 hingga M.9).
  - Pastikan jumlah baris inovasi adalah 42 (semua kode dari INV-INT-01 hingga INV-NEW-09).
  - Jika ada baris yang hilang, tambahkan baris tersebut dengan pemetaan yang akurat.

- [ ] **[3.7] Periksa Glosarium (Bagian 11).**
  - Pastikan semua istilah teknis dan bisnis yang digunakan dalam dokumen sudah terdefinisi di Glosarium.
  - Istilah yang harus ada setidaknya: Innovation Proposal, Best Practice, BOM, HPP, PPOB, RBAC, JWT, bcrypt, Audit Trail, Stock Opname, Cash Reconciliation, Scope Creep, Runtime Config, Price Tracking, Fraud Detection, UoM, Pinjaman Bank Berbunga, Pinjaman Kerabat, Jasa Keuangan Agen.
  - Tambahkan definisi jika ada istilah penting yang belum ada.

- [ ] **[3.8] Periksa bagian Persetujuan dan Otorisasi (Bagian 10).**
  - Pastikan tabel otorisasi minimal memiliki 2 baris: Pemilik Usaha dan Tim Pengembang AI.
  - Untuk field yang belum diisi (tanda tangan/tanggal), pastikan placeholder yang digunakan informatif (bukan kosong melainkan teks seperti *"Menunggu Persetujuan Digital"*).
  - Ini adalah dokumen SDLC fase perencanaan yang wajar belum ditandatangani, maka status placeholder sudah cukup — tidak perlu diisi palsu.

---

### FASE 4 — Validasi Kesiapan sebagai Input Fase SDLC Selanjutnya

> **Tujuan**: Memastikan dokumen ini dapat langsung menjadi referensi andal bagi SRS (fase Requirements) dan SDD (fase Design) tanpa menimbulkan pertanyaan atau kebingungan.

- [ ] **[4.1] Uji "Apakah setiap inovasi memiliki output yang jelas untuk SRS?"**
  - Baca ulang setiap entri inovasi. Untuk setiap inovasi, tanyakan: *"Jika saya adalah penulis SRS, apakah saya bisa langsung menuliskan Functional Requirement dari inovasi ini tanpa memerlukan klarifikasi lebih lanjut?"*
  - Tandai entri inovasi yang deskripsinya terlalu abstrak atau ambigu untuk langsung dikonversi menjadi FR di SRS.

- [ ] **[4.2] Uji "Apakah setiap inovasi memiliki informasi teknis yang cukup untuk SDD?"**
  - Baca ulang setiap entri inovasi. Untuk setiap inovasi, tanyakan: *"Jika saya adalah penulis SDD/ERD, apakah saya bisa langsung mengidentifikasi entitas database atau komponen teknis yang perlu dibuat dari inovasi ini?"*
  - Tandai entri inovasi yang tidak menyebutkan komponen teknis minimum (nama tabel, nama field kritis, nama fungsi/modul Python, atau library yang digunakan).

- [ ] **[4.3] Uji "Apakah Bagian 8 (Dampak SDLC) sudah cukup mengarahkan tim SRS?"**
  - Pastikan Bagian 8.1 (Dampak ke SRS) menyebutkan setidaknya 3 instruksi konkret yang dapat langsung dieksekusi oleh penulis SRS.
  - Pastikan Bagian 8.2 (Dampak ke SDD) sudah menyebutkan semua tabel database baru yang perlu dibuat di ERD (minimal: `audit_logs`, `system_configs`, `supplier_prices`, `shift_handover_logs`, `ppob_logs`, `kreditur_logs`).
  - Jika ada tabel yang teridentifikasi dari inovasi baru tapi belum disebutkan di Bagian 8.2, tambahkan.

- [ ] **[4.4] Uji "Apakah matriks kelayakan di Bagian 6 bisa langsung digunakan untuk prioritasi oleh Product Owner?"**
  - Pastikan kolom Prioritas (High/Medium/Low) konsisten dengan narasi prioritasi di Bagian 6.3.
  - Pastikan Fase Implementasi yang Direkomendasikan di setiap inovasi INV-REC dan INV-NEW konsisten dengan timeline proyek (12 bulan) yang ada di dokumen referensi.

- [ ] **[4.5] Uji "Apakah Bagian 9 (Risiko Inovasi) sudah cukup untuk dijadikan input Risk Register di SRS?"**
  - Pastikan setiap risiko memiliki: Nama Risiko, Probabilitas (1-5), Dampak (1-5), dan Rencana Mitigasi yang konkret.
  - Periksa apakah ada risiko inovasi baru yang belum terdaftar namun sudah teridentifikasi dari komparasi di Fase 1, dan tambahkan jika ada.

---

### FASE 5 — Validasi Kualitas Bahasa Indonesia

> **Tujuan**: Memastikan seluruh teks dokumen menggunakan Bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau AI model yang lebih kecil.

- [ ] **[5.1] Periksa terminologi teknis yang dicampur tidak konsisten.**
  - Identifikasi semua istilah teknis Inggris yang digunakan dalam teks (misalnya: *burnout*, *side-effects*, *handover*, *startup alert*, *threshold*).
  - Pastikan setiap istilah asing yang digunakan: (a) dicetak miring (*italic*), dan (b) sudah ada terjemahan atau penjelasan dalam tanda kurung atau di Glosarium.
  - Pastikan penggunaan istilah yang sama menggunakan satu konvensi yang konsisten di seluruh dokumen (misalnya: selalu `bcrypt` bukan kadang `BCrypt` atau `Bcrypt`).

- [ ] **[5.2] Periksa kalimat yang berpotensi ambigu.**
  - Cari kalimat yang mengandung kata ganti ambigu (misalnya: "ini", "tersebut", "hal itu") tanpa referensi yang jelas.
  - Cari kalimat yang terlalu panjang (lebih dari 40 kata dalam satu kalimat) dan pecah menjadi 2 kalimat yang lebih pendek dan jelas.
  - Cari kalimat yang menggunakan kata pasif berlebihan tanpa subjek yang jelas (misalnya: "dilakukan", "dijalankan" tanpa menyebut siapa yang melakukan).

- [ ] **[5.3] Periksa konsistensi penulisan angka dan format.**
  - Pastikan nilai Rupiah menggunakan format `Rp X.XXX.XXX` (bukan `Rp. X.XXX.XXX` atau `IDR X`).
  - Pastikan persentase menggunakan format `X%` (bukan `X %` dengan spasi).
  - Pastikan nomor kode inovasi konsisten menggunakan format `INV-INT-XX`, `INV-REC-XX`, `INV-NEW-XX` (bukan variasi format lain).
  - Pastikan tanggal menggunakan format `YYYY-MM-DD` secara konsisten.

- [ ] **[5.4] Periksa konsistensi penggunaan bullet point dan bold/italic.**
  - Pastikan bold (`**teks**`) hanya digunakan untuk istilah kunci, nama inovasi, dan angka penting — bukan untuk penekanan gaya (dekoratif).
  - Pastikan italic (`*teks*`) hanya digunakan untuk istilah asing/teknis Inggris.
  - Pastikan bullet point menggunakan karakter yang konsisten (`*` atau `-`, pilih satu).

- [ ] **[5.5] Periksa apakah judul seksi dan sub-seksi sudah deskriptif dan informatif.**
  - Setiap heading harus mendeskripsikan isi dengan tepat. Contoh buruk: "Bagian 4.7" tanpa sub-judul. Contoh baik: "4.7. Inovasi Layanan Keuangan Digital dan Administrasi Modal".
  - Pastikan tidak ada heading kosong atau heading yang terlalu generik.

---

### FASE 6 — Validasi Kelengkapan Data (Identifikasi & Pengisian Data Kosong)

> **Tujuan**: Memastikan tidak ada field, placeholder, atau data kosong yang akan menghambat penggunaan dokumen ini sebagai referensi.

- [ ] **[6.1] Identifikasi semua placeholder atau data yang belum terisi.**
  - Cari teks seperti: `[TBD]`, `[TODO]`, `[belum diisi]`, `(kosong)`, `N/A`, atau `*`.
  - Cari tabel dengan sel yang kosong (bukan `—` yang bermakna "tidak berlaku", tapi benar-benar sel tanpa isi).
  - Catat posisi setiap data kosong yang ditemukan.

- [ ] **[6.2] Isi semua data kosong yang masih dalam ruang lingkup Innovation Proposal.**
  - Untuk setiap data kosong, isi dengan data yang:
    - Relevan dan konsisten dengan konteks dokumen.
    - Sesuai dengan parameter yang sudah ada di dokumen referensi.
    - Tidak bersifat asumsi liar — harus berdasar pada informasi yang sudah ada di salah satu file referensi.
  - Contoh pengisian yang tepat: Jika kolom "Sumber Data" pada sebuah inovasi kosong, isi dengan tautan ke bagian yang paling relevan dari dokumen referensi.

- [ ] **[6.3] Verifikasi khusus: Tabel Referensi Dokumen (Bagian 12).**
  - Pastikan semua 5 file referensi yang digunakan sudah terdaftar dengan benar: nama file, path relatif, dan keterangan penggunaan.
  - Jika dalam proses validasi ditemukan file referensi tambahan yang digunakan (namun belum terdaftar), tambahkan di baris bawah tabel Bagian 12.

- [ ] **[6.4] Verifikasi konsistensi jumlah inovasi.**
  - Hitung total inovasi yang disebutkan di Bagian 2 (Ringkasan Eksekutif): harus cocok dengan jumlah entri aktual di Bagian 4 dan 5.
  - Hitung baris di Matriks Kelayakan (Bagian 6.1): harus 30 baris.
  - Hitung baris di Matriks Kelayakan Tambahan (Bagian 6.2): harus 12 baris.
  - Hitung baris di Matriks Pemetaan Modul (Bagian 7): harus 42 baris.
  - Jika ada perbedaan hitungan, identifikasi inovasi mana yang tidak konsisten dan perbaiki.

- [ ] **[6.5] Verifikasi parameter angka bisnis yang spesifik.**
  - Pastikan semua angka bisnis kritis yang disebutkan konsisten antar entri inovasi:
    - Target laba bulanan: **Rp 15.000.000**
    - Persentase gaji berbasis laba: **25%**
    - Limit kasbon karyawan: **Rp 1.000.000** (atau maksimal 30% gaji standar)
    - Threshold saldo PPOB kritis: **Rp 150.000**
    - Top-up PPOB minimum: **Rp 500.000**
    - Toleransi selisih kas kasir: **Rp 10.000**
    - Durasi sesi JWT: **8 jam**
    - Cost factor bcrypt: **12**
    - Durasi penguncian akun: **10 menit** setelah 5 kali gagal login
    - Alert jatuh tempo bank: **H-3** sebelum jatuh tempo
    - Target selisih stok: **< 1.0%**
    - Target kecepatan laporan: **< 5 detik**
  - Jika ada nilai yang tidak konsisten antar bagian, selaraskan berdasarkan nilai yang paling banyak disebut di dokumen referensi.

---

### FASE 7 — Validasi Tambahan Spesifik Innovation Proposal

> **Tujuan**: Melakukan pemeriksaan khusus yang bersifat spesifik untuk dokumen bertipe Innovation Proposal, di luar kriteria umum yang sudah diperiksa di atas.

- [ ] **[7.1] Periksa apakah setiap inovasi sudah memiliki kode unik yang tidak duplikat.**
  - Buat daftar semua kode inovasi: INV-INT-01 s.d. INV-INT-30, INV-REC-01 s.d. INV-REC-03, INV-NEW-01 s.d. INV-NEW-09.
  - Pastikan tidak ada kode yang digunakan dua kali, tidak ada lompatan nomor urut, dan tidak ada kode yang salah tulis.

- [ ] **[7.2] Periksa apakah "Justifikasi Bisnis" setiap inovasi sudah kuat dan berbasis data.**
  - Setiap justifikasi bisnis seharusnya menjawab pertanyaan: *"Mengapa inovasi ini mutlak dibutuhkan oleh AbuCom?"*
  - Justifikasi yang lemah: *"Untuk meningkatkan performa sistem."* (terlalu generik).
  - Justifikasi yang kuat: *"Menghindari kehilangan stok bahan baku senilai hingga 15% per tahun akibat limbah cetak yang tidak tercatat di sistem."*
  - Tandai dan perkuat setiap justifikasi bisnis yang masih terlalu generik atau tidak terhubung ke konteks AbuCom.

- [ ] **[7.3] Periksa apakah "Dampak Bisnis" setiap inovasi sudah terukur (bukan hanya kualitatif).**
  - Dampak bisnis yang baik menyertakan minimal satu indikator terukur: persentase, waktu, atau nilai Rupiah.
  - Contoh baik: *"Menekan kerugian akibat limbah tidak teridentifikasi hingga 15% per tahun."*
  - Contoh buruk: *"Meningkatkan efisiensi staf."*
  - Tambahkan indikator terukur pada setiap dampak bisnis yang masih bersifat kualitatif saja.

- [ ] **[7.4] Periksa apakah seluruh 9 inovasi tambahan baru (INV-NEW) sudah memiliki "Fase Implementasi yang Direkomendasikan" yang realistis.**
  - Periksa apakah fase implementasi yang direkomendasikan tidak bertabrakan dengan milestone proyek (timeline 12 bulan dari Project Charter/Feasibility Study).
  - Periksa apakah ada inovasi dengan kompleksitas "Tinggi" namun direkomendasikan di fase awal tanpa penjelasan yang memadai.

- [ ] **[7.5] Periksa apakah ada inovasi yang saling berketergantungan namun tidak disebutkan dependensinya.**
  - Contoh: INV-NEW-06 (Fraud Detection) bergantung pada INV-INT-16 (Audit Trail) dan INV-INT-25 (Rekonsiliasi Kas).
  - Contoh: INV-NEW-09 (Runtime Config) bergantung pada INV-INT-09 (Smart Payroll) dan INV-INT-11 (Kasbon).
  - Jika ada dependensi kritis yang belum disebutkan di deskripsi inovasi, tambahkan catatan dependensi.

- [ ] **[7.6] Periksa apakah dokumen sudah menyebutkan strategi roll-out atau staging implementasi yang logis.**
  - Bagian 6.3 (Prioritasi Implementasi) harus memberikan gambaran logis tentang urutan pengerjaan yang tidak akan menimbulkan deadlock dependensi teknis.
  - Pastikan inovasi yang menjadi prerequisite teknis (misalnya: INV-INT-16 Audit Trail harus ada sebelum INV-NEW-06 Fraud Detection) mendapatkan prioritas lebih awal.

---

### FASE 8 — Penulisan Ulang Dokumen (Overwrite)

> **Tujuan**: Menuangkan seluruh hasil validasi ke dalam file target dengan cara menimpa (overwrite) dokumen secara penuh.

> **PERINGATAN KRITIS**: Seluruh teks dari baris pertama hingga baris terakhir **HARUS ditulis ulang sepenuhnya**. Tidak boleh ada pemotongan, peringkasan, atau penghilangan konten apapun (no truncation). Dokumen hasil overwrite harus **lebih panjang atau sama** dengan dokumen aslinya, tidak boleh lebih pendek.

- [ ] **[8.1] Siapkan versi dokumen yang sudah tervalidasi secara penuh di memori/scratchpad.**
  - Pastikan semua temuan dari Fase 1–7 sudah diintegrasikan ke dalam draft dokumen baru.
  - Lakukan tinjauan akhir terhadap draft sebelum overwrite.

- [ ] **[8.2] Perbarui Frontmatter YAML.**
  - Ubah `versi` dari `1.1` menjadi `1.2`.
  - Ubah `tanggal` ke tanggal saat revisi dilakukan (tanggal eksekusi issue ini).
  - Ubah `status` menjadi `Validated` (jika sudah validated) atau `In Review` (jika masih ada item yang perlu konfirmasi pemilik).
  - Perbarui `penyusun` dengan persona eksekutor issue ini.

- [ ] **[8.3] Tambahkan entri baru di Tabel Riwayat Perubahan (Change Log).**
  - Tambahkan baris baru untuk `v1.2` dengan kolom:
    - **Versi**: `1.2`
    - **Tanggal**: tanggal eksekusi hari ini
    - **Perubahan**: Deskripsi ringkas semua perbaikan yang dilakukan (misalnya: "Validasi komprehensif v1.2: [daftar perbaikan utama yang dilakukan]").
    - **Oleh**: Nama persona eksekutor issue ini.

- [ ] **[8.4] Tulis ulang seluruh isi dokumen ke file target menggunakan mode overwrite.**
  - File target: `docs/sdlc/01_planning/05_innovation_proposal.md`
  - **Wajib menulis dari baris 1 (frontmatter `---`) hingga baris terakhir (baris referensi dokumen terakhir)**.
  - **Tidak boleh**: memotong konten, meringkas bagian manapun, atau melewati seksi apapun.
  - **Harus**: memastikan semua seksi, tabel, matriks, glosarium, dan referensi tertulis lengkap.

- [ ] **[8.5] Verifikasi hasil penulisan.**
  - Baca kembali file hasil overwrite dari baris pertama hingga baris terakhir.
  - Pastikan:
    - [ ] Frontmatter menunjukkan `versi: 1.2`
    - [ ] Tabel Change Log memiliki entri v1.2
    - [ ] Semua 42 entri inovasi masih ada (tidak ada yang terhapus)
    - [ ] Semua matriks (Bagian 6.1, 6.2, 7) masih lengkap
    - [ ] Glosarium masih lengkap atau bertambah
    - [ ] Bagian 12 (Referensi Dokumen) berisi semua referensi yang digunakan, termasuk referensi baru jika ada
    - [ ] Dokumen tidak berakhir tiba-tiba di tengah seksi manapun

- [ ] **[8.6] Tambahkan referensi baru di Bagian 12 jika ada.**
  - Jika dalam proses validasi kamu menggunakan atau mengacu pada file referensi yang **belum** terdaftar di Bagian 12, tambahkan baris baru di bagian paling bawah tabel referensi.
  - Format baris baru: `| [nomor] | [nama file] | [path relatif sebagai link markdown] | [keterangan penggunaan] |`

---

### FASE 9 — Laporan Hasil Validasi

> **Tujuan**: Mendokumentasikan ringkasan hasil validasi agar dapat digunakan sebagai catatan audit.

- [ ] **[9.1] Buat laporan ringkas hasil validasi.**
  - Tuliskan laporan hasil validasi di bawah ini (atau di file terpisah `docs/issue/0067_hasil_validasi.md` jika kontennya terlalu panjang):

```
## Laporan Hasil Validasi Issue #0067

**Tanggal Eksekusi** : [isi tanggal]
**Eksekutor**        : [isi nama AI/junior programmer]
**Versi Dokumen Awal**: v1.1
**Versi Dokumen Akhir**: v1.2

### Gap yang Ditemukan dan Diperbaiki:
- [GAP-001] ...
- [GAP-002] ...
(lanjutkan sesuai temuan)

### Data Kosong yang Diisi:
- ...

### Perubahan Struktural:
- ...

### Referensi Baru yang Ditambahkan:
- (jika ada)

### Catatan Penting untuk Tim Selanjutnya:
- ...
```

- [ ] **[9.2] Konfirmasi bahwa file target telah berhasil di-overwrite.**
  - Verifikasi ukuran file (`bytes`) setelah overwrite tidak lebih kecil dari sebelumnya.
  - Verifikasi bahwa versi di frontmatter sudah menunjukkan `v1.2`.
  - Nyatakan status: **SELESAI** atau **PERLU TINDAK LANJUT** (jika ada item yang memerlukan konfirmasi pemilik usaha).

---

## Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **SELESAI** jika semua kondisi berikut terpenuhi:

- [x] Semua checklist di Fase 0–9 telah dicentang `[x]`.
- [x] File `docs/sdlc/01_planning/05_innovation_proposal.md` berhasil di-overwrite dengan versi v1.2 yang lebih lengkap dan tervalidasi.
- [x] Tidak ada field kosong, placeholder `[TBD]`, atau data yang hilang di dalam dokumen hasil validasi.
- [x] Semua 42 inovasi masih ada dan tidak ada yang terpotong.
- [x] Bahasa Indonesia seluruh dokumen sudah natural, tidak ambigu, dan mudah dipahami.
- [x] Dokumen sudah dapat langsung digunakan sebagai input andal untuk fase SRS (Requirements) dan SDD (Design) tanpa perlu klarifikasi lebih lanjut.
- [x] Laporan hasil validasi telah ditulis di Fase 9.

---

## Catatan Penting untuk Eksekutor

> **Jangan melakukan overwrite parsial.** Overwrite harus dilakukan sekali untuk seluruh file, bukan section per section.

> **Jika konteks window AI terbatas**, prioritaskan membaca seluruh dokumen target (`05_innovation_proposal.md`) dan seluruh dokumen referensi terlebih dahulu sebelum mulai menulis. Jangan mulai menulis jika belum selesai membaca semua referensi.

> **Jangan menghapus konten yang sudah ada** kecuali konten tersebut benar-benar tidak relevan dan berpotensi menimbulkan kebingungan.

> **Jangan menambahkan konten yang tidak berdasar** — semua penambahan harus dapat ditelusuri ke setidaknya satu dokumen referensi yang terdaftar.

> **Jika menemukan inkonsistensi serius** antara dokumen ini dengan dokumen referensi (misalnya angka finansial yang berbeda jauh), catat di laporan hasil validasi dan pilih nilai yang paling banyak disebut di dokumen referensi sebagai nilai yang benar.

---

*Issue dibuat oleh: Senior Technical Documentation Auditor (AI)*
*Tanggal pembuatan: 2026-05-28*
*Dokumen ini adalah instruksi low-level untuk dieksekusi oleh junior programmer atau AI model yang lebih kecil.*
