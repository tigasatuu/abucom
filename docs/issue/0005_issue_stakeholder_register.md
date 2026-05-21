---
issue       : 0005
judul       : Pembuatan dan Penyusunan Dokumen Stakeholder Register
dokumen     : Stakeholder Register
target file : docs/sdlc/01_planning/03_stakeholder_register.md
prioritas   : High
status      : Open
tanggal     : 2026-05-21
---

# Pembuatan dan Penyusunan Dokumen Stakeholder Register

## 1. Ringkasan Issue

Issue ini berisi perencanaan low-level lengkap untuk pembuatan dan penyusunan dokumen **Stakeholder Register** proyek AbuCom. Dokumen Stakeholder Register adalah dokumen resmi fase Planning dalam siklus SDLC yang berfungsi sebagai **daftar identifikasi, klasifikasi, analisis, dan strategi pengelolaan** seluruh pihak yang berkepentingan (stakeholder) terhadap proyek pembangunan sistem manajemen terpadu AbuCom.

Dokumen ini menjadi acuan penting bagi fase SDLC selanjutnya (Requirements, Design, Implementation, Testing, Deployment) untuk memastikan setiap keputusan proyek mempertimbangkan kebutuhan, ekspektasi, dan pengaruh dari masing-masing stakeholder secara terstruktur.

---

## 2. Persona Pelaksana

**Persona yang ditugaskan**: **Senior Stakeholder Analyst & Project Governance Specialist**

**Alasan pemilihan persona**:
- Stakeholder Register adalah dokumen tata kelola proyek (*project governance*) yang membutuhkan kemampuan analisis hubungan interpersonal, pemetaan kepentingan bisnis, dan strategi komunikasi.
- Persona ini memiliki otoritas dan keahlian dalam mengidentifikasi, mengklasifikasikan, dan menyusun strategi pengelolaan stakeholder berdasarkan standar PMBOK (*Project Management Body of Knowledge*).
- Persona ini memahami dinamika kekuasaan (*power dynamics*), tingkat kepentingan (*interest level*), dan potensi pengaruh (*influence*) setiap pihak terhadap keberhasilan proyek.

**Instruksi**: Saat menyusun dokumen, posisikan dirimu sebagai seorang **Senior Stakeholder Analyst & Project Governance Specialist** yang berpengalaman dalam manajemen proyek IT untuk UMKM. Gunakan sudut pandang profesional, analitis, dan strategis dalam setiap bagian dokumen.

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca secara menyeluruh** sebelum memulai penyusunan dokumen. Setiap file memiliki peran spesifik sebagai sumber data:

| # | File Referensi | Lokasi Path Relatif | Peran dalam Penyusunan | Prioritas |
|---|----------------|---------------------|------------------------|-----------|
| 1 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | **Referensi Utama (Primer)**. Sumber data terlengkap untuk identifikasi stakeholder. Mengandung: daftar stakeholder (Bagian 6), RACI Matrix (Bagian 6.2), susunan tim pengembang dan spesialisasi (Bagian 7.1), struktur organisasi operasional staf (Bagian 7.2), risiko terkait stakeholder (Bagian 10), dan persetujuan/otorisasi proyek (Bagian 14). | Wajib |
| 2 | `02_feasibility_study.md` | `docs/sdlc/01_planning/02_feasibility_study.md` | **Referensi Sekunder**. Sumber data pendukung untuk analisis kelayakan operasional terkait stakeholder. Mengandung: stakeholder utama (Bagian 3.4), kesiapan SDM dan literasi digital staf baru (Bagian 5.1), aspek ketenagakerjaan hukum PKWT/PKWTT (Bagian 8.4), risiko operasional staf baru (Bagian 5.6), dan risiko hukum/organisasional (Bagian 8.6). | Wajib |
| 3 | `narasi.txt` | `docs/sdlc/narasi.txt` | **Referensi Pendukung Konteks**. Sumber data asli narasi pemilik usaha yang masih dibutuhkan untuk konteks relasi personal stakeholder yang tidak tercakup secara eksplisit di dokumen lain. Mengandung: hubungan emosional pemilik dengan pemberi pinjaman tanpa bunga (sahabat, kerabat, teman, keluarga, orang tua), dinamika penarikan dana mendadak, serta konteks budaya kerja *cross-functional* yang diharapkan pemilik dari karyawan. | Wajib |

---

## 4. Kerangka Struktur Dokumen Stakeholder Register

Gunakan kerangka struktur berikut sebagai **struktur final** dokumen Stakeholder Register. Kerangka ini disusun berdasarkan standar praktik industri PMBOK 7th Edition dan disesuaikan dengan konteks proyek AbuCom:

```
---
(Front Matter / Metadata YAML)
---

# Stakeholder Register — AbuCom

## Riwayat Perubahan Dokumen
(Tabel versi, tanggal, perubahan, oleh)

---

## 1. Informasi Dokumen
   (Tujuan dokumen, ruang lingkup identifikasi, hubungan dengan dokumen lain)

---

## 2. Daftar Identifikasi Stakeholder
   ### 2.1. Stakeholder Internal
      (Tabel: ID, Nama/Jabatan, Peran dalam Proyek, Kategori, Kontak/Keterangan)
   ### 2.2. Stakeholder Eksternal
      (Tabel: ID, Nama/Jabatan, Peran dalam Proyek, Kategori, Kontak/Keterangan)

---

## 3. Profil Detail Stakeholder
   ### 3.1. [STK-001] Pemilik Usaha AbuCom
      (Sub-bagian: Identitas, Peran Ganda, Kebutuhan & Ekspektasi, Potensi Pengaruh, Fase Keterlibatan Maksimal)
   ### 3.2. [STK-002] Calon Staf Kepala Percetakan
      (... dst untuk setiap stakeholder)
   ### 3.3. [STK-003] Calon Staf Pramuniaga
   ### 3.4. [STK-004] Calon Staf Kasir
   ### 3.5. [STK-005] Calon Staf Desainer
   ### 3.6. [STK-006] Calon Staf Produksi Cetak
   ### 3.7. [STK-007] Calon Staf Fotocopy & Print Dokumen
   ### 3.8. [STK-008] Calon Staf Gudang
   ### 3.9. [STK-009] Pelanggan AbuCom
   ### 3.10. [STK-010] Vendor & Supplier Bahan Baku / ATK
   ### 3.11. [STK-011] Bank BRI (Kreditur Berbunga)
   ### 3.12. [STK-012] Bank Mandiri (Kreditur Berbunga)
   ### 3.13. [STK-013] Kerabat & Keluarga (Pemberi Pinjaman Tanpa Bunga)
   ### 3.14. [STK-014] Tim Pengembang AI — Gemini 3.1 Pro (High)
   ### 3.15. [STK-015] Tim Pengembang AI — Gemini 3.1 Pro (Low)
   ### 3.16. [STK-016] Tim Pengembang AI — Gemini 3 Flash
   ### 3.17. [STK-017] Tim Pengembang AI — Claude Sonnet 4.6 (Thinking)
   ### 3.18. [STK-018] Tim Pengembang AI — Claude Opus 4.6 (Thinking)
   ### 3.19. [STK-019] Tim Pengembang AI — GPT-OSS 120B (Medium)

---

## 4. Klasifikasi Stakeholder
   ### 4.1. Berdasarkan Kategori Keterlibatan
      (Tabel: Internal vs Eksternal, Langsung vs Tidak Langsung)
   ### 4.2. Matriks Power/Interest Grid (Pengaruh vs Kepentingan)
      (Tabel klasifikasi 4 kuadran: Manage Closely, Keep Satisfied, Keep Informed, Monitor)
   ### 4.3. Matriks Pengaruh/Dampak (Influence/Impact Matrix)
      (Tabel tambahan untuk memperjelas prioritas pengelolaan)

---

## 5. Analisis Sikap dan Tingkat Keterlibatan Stakeholder
   ### 5.1. Stakeholder Engagement Assessment Matrix
      (Tabel: ID Stakeholder, Tingkat Saat Ini [C], Tingkat yang Diinginkan [D])
      (Skala: Unaware, Resistant, Neutral, Supportive, Leading)
   ### 5.2. Analisis Gap Keterlibatan
      (Penjelasan naratif gap antara kondisi saat ini vs kondisi yang diharapkan)

---

## 6. Kebutuhan dan Ekspektasi Stakeholder
   (Tabel konsolidasi: ID, Stakeholder, Kebutuhan Utama, Ekspektasi terhadap Proyek, Kriteria Kepuasan)

---

## 7. Matriks RACI Stakeholder
   (Tabel RACI lengkap: Aktivitas/Deliverable vs Semua Stakeholder teridentifikasi)

---

## 8. Strategi Pengelolaan dan Komunikasi Stakeholder
   ### 8.1. Rencana Komunikasi per Stakeholder
      (Tabel: ID, Stakeholder, Metode Komunikasi, Frekuensi, Penanggung Jawab, Informasi yang Dikomunikasikan)
   ### 8.2. Strategi Mitigasi Resistensi
      (Penjelasan strategi untuk stakeholder yang berpotensi resisten)

---

## 9. Risiko Terkait Stakeholder
   (Tabel: No, Risiko, Stakeholder Terkait, Probabilitas, Dampak, Rencana Mitigasi)

---

## 10. Persetujuan dan Otorisasi
   (Tabel: Pihak Penandatangan, Jabatan, Tanda Tangan, Tanggal)

---

## 11. Glosarium
   (Daftar istilah khusus stakeholder management yang digunakan dalam dokumen ini)

---

## 12. Referensi Dokumen
   (Tabel: #, Nama File, Lokasi Path, Keterangan penggunaan dalam penyusunan)
```

---

## 5. Instruksi Detail Tahapan Pelaksanaan

### TAHAP 1: Persiapan dan Pembacaan File Referensi

> **Tujuan**: Membaca dan merangkum semua data serta informasi dari file referensi yang relevan dengan dokumen Stakeholder Register. Setiap detail jangan sampai ada yang terlewat.

- [ ] **1.1.** Baca file `docs/sdlc/01_planning/01_project_charter.md` secara menyeluruh dari baris pertama hingga baris terakhir.
- [ ] **1.2.** Dari file Project Charter, rangkum dan catat data berikut secara lengkap:
  - [ ] **1.2.1.** Bagian 1.3 (Sponsor/Pemilik Proyek): Catat nama, peran ganda (Inisiator, Sponsor, Penyedia Pendanaan, Key User).
  - [ ] **1.2.2.** Bagian 1.4 (Manajer Proyek): Catat bahwa pemilik bertindak sebagai Junior Programmer & Manajer Proyek Internal.
  - [ ] **1.2.3.** Bagian 6.1 (Daftar Stakeholder): Catat semua 6 kategori stakeholder yang teridentifikasi beserta deskripsi perannya masing-masing.
  - [ ] **1.2.4.** Bagian 6.2 (RACI Matrix): Catat seluruh isi tabel RACI secara lengkap (7 baris aktivitas × 4 kolom pihak) beserta legenda R/A/C/I.
  - [ ] **1.2.5.** Bagian 7.1 (Susunan Tim Pengembang): Catat data seluruh 7 anggota tim (Anggota 0-6), meliputi nama model AI, peran utama, dan deskripsi spesialisasi.
  - [ ] **1.2.6.** Bagian 7.2 (Struktur Organisasi Staf Operasional): Catat seluruh 7 posisi staf operasional beserta deskripsi tanggung jawab masing-masing.
  - [ ] **1.2.7.** Bagian 10 (Risiko Awal): Catat semua risiko yang berkaitan langsung dengan stakeholder, yaitu: Risiko 1 (Burnout Pemilik), Risiko 3 (Penarikan Dana Mendadak Kerabat), Risiko 5 (Kecurangan Karyawan), dan Risiko 6 (Ketidaksesuaian Literasi Karyawan Baru).
  - [ ] **1.2.8.** Bagian 14 (Persetujuan dan Otorisasi): Catat pihak yang menandatangani persetujuan.

- [ ] **1.3.** Baca file `docs/sdlc/01_planning/02_feasibility_study.md` secara menyeluruh dari baris pertama hingga baris terakhir.
- [ ] **1.4.** Dari file Feasibility Study, rangkum dan catat data berikut secara lengkap:
  - [ ] **1.4.1.** Bagian 3.4 (Stakeholder Utama): Catat ringkasan 3 kategori stakeholder (Pemilik, Calon Staf, Kreditur).
  - [ ] **1.4.2.** Bagian 5.1.2 (Rencana Rekrutmen 7 Posisi): Catat analisis kesiapan rekrutmen dan ketergantungan pada keberhasilan rekrutmen sebelum go-live.
  - [ ] **1.4.3.** Bagian 5.1.3 (Kesiapan Literasi Digital): Catat penilaian literasi digital pemilik (Junior Programmer, kesiapan baik) vs karyawan baru (literasi bervariasi, potensi kesulitan CLI).
  - [ ] **1.4.4.** Bagian 5.3 (Penerimaan Pengguna): Catat proyeksi penerimaan pemilik (100%) dan strategi penerimaan karyawan baru.
  - [ ] **1.4.5.** Bagian 5.4 (Kebutuhan Pelatihan): Catat rencana pelatihan 3 hari untuk 7 staf baru.
  - [ ] **1.4.6.** Bagian 5.6 (Risiko Operasional): Catat 3 risiko operasional yang terkait stakeholder (Keterlambatan Rekrutmen, Human Error CLI, Resistensi Cross-Functional).
  - [ ] **1.4.7.** Bagian 8.4 (Aspek Ketenagakerjaan): Catat informasi kewajiban PKWT/PKWTT dan parameter UMR daerah.
  - [ ] **1.4.8.** Bagian 8.6 (Risiko Hukum/Organisasional): Catat 2 risiko (Pelanggaran UU PDP oleh karyawan, Konflik selisih kas cross-functional).

- [ ] **1.5.** Baca file `docs/sdlc/narasi.txt` secara menyeluruh dari baris pertama hingga baris terakhir.
- [ ] **1.6.** Dari file Narasi, rangkum dan catat data berikut secara lengkap:
  - [ ] **1.6.1.** Bagian "Pengelolaan Modal dan Pinjaman": Catat detail hubungan personal pemilik dengan pemberi pinjaman tanpa bunga (sahabat, kerabat, teman, keluarga, orang tua), sifat fleksibilitas penarikan dana mendadak (sebagian, total, permanen), dan kewajiban setoran bulanan ke Bank BRI dan Bank Mandiri.
  - [ ] **1.6.2.** Bagian "Kondisi Operasional Saat Ini": Catat konteks emosional pemilik (stres, burnout, pusing) dan fakta bahwa semua beban ada di pundak pemilik sendiri.
  - [ ] **1.6.3.** Bagian "Rencana Struktur Organisasi dan Budaya Kerja": Catat 7 posisi yang direncanakan beserta deskripsi singkatnya, serta budaya kerja *cross-functional* yang diharapkan pemilik.
  - [ ] **1.6.4.** Bagian "Harapan untuk Aplikasi Baru" poin tentang Manajemen Hak Akses: Catat bahwa pemilik secara eksplisit menginginkan pembedaan hak akses antara "Pemilik" dan "Karyawan" karena ada data sensitif (pinjaman bank, tabungan pribadi).
  - [ ] **1.6.5.** Bagian "Kebutuhan Teknis dan Tim": Catat susunan tim pengembang (Anggota 0-6) beserta pembagian perannya.

---

### TAHAP 2: Penyusunan Front Matter dan Bagian Awal Dokumen

> **Tujuan**: Menulis metadata dokumen, riwayat perubahan, dan informasi dokumen.

- [ ] **2.1.** Tulis blok **Front Matter YAML** di bagian paling atas file target dengan format berikut:
  ```yaml
  ---
  dokumen    : Stakeholder Register
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [ISI TANGGAL HARI INI DALAM FORMAT YYYY-MM-DD]
  status     : Draft
  penyusun   : Senior Stakeholder Analyst & Project Governance Specialist
  ---
  ```

- [ ] **2.2.** Tulis judul dokumen: `# Stakeholder Register — AbuCom`

- [ ] **2.3.** Tulis tabel **Riwayat Perubahan Dokumen** dengan kolom: Versi, Tanggal, Perubahan, Oleh. Isi baris pertama dengan versi 1.0, tanggal hari ini, keterangan "Pembuatan awal dokumen berdasarkan analisis Project Charter, Feasibility Study, dan Narasi Pemilik", oleh "Senior Stakeholder Analyst & Project Governance Specialist".

- [ ] **2.4.** Tulis **Bagian 1: Informasi Dokumen** yang menjelaskan:
  - Tujuan penyusunan Stakeholder Register ini (identifikasi, klasifikasi, analisis pengaruh, dan strategi pengelolaan seluruh pemangku kepentingan proyek AbuCom).
  - Ruang lingkup identifikasi stakeholder (mencakup stakeholder internal proyek, stakeholder operasional pasca go-live, stakeholder finansial, dan stakeholder eksternal bisnis).
  - Hubungan dokumen ini dengan dokumen SDLC lain (sebagai input utama bagi penyusunan SRS pada fase Requirements untuk menentukan prioritas kebutuhan fungsional berdasarkan kepentingan stakeholder, serta sebagai acuan bagi fase Testing/UAT untuk menentukan skenario pengujian penerimaan pengguna).

---

### TAHAP 3: Penyusunan Daftar Identifikasi Stakeholder

> **Tujuan**: Menyusun daftar lengkap semua stakeholder yang teridentifikasi dari seluruh file referensi, dibagi menjadi Stakeholder Internal dan Stakeholder Eksternal.

- [ ] **3.1.** Tulis **Bagian 2: Daftar Identifikasi Stakeholder**.

- [ ] **3.2.** Tulis **Sub-bagian 2.1: Stakeholder Internal** dalam format tabel dengan kolom:
  | ID | Nama / Jabatan | Peran dalam Proyek | Kategori | Keterangan |

  Isi tabel dengan stakeholder internal berikut (data diambil dari Project Charter Bagian 6, 7.1, 7.2):
  - [ ] **3.2.1.** `STK-001`: Pemilik Usaha AbuCom — Sponsor, Manajer Proyek, Junior Programmer, Key User — Kategori: Sponsor & Pengguna Utama
  - [ ] **3.2.2.** `STK-002`: Calon Staf Kepala Percetakan — Pengguna Operasional — Kategori: End-User Operasional
  - [ ] **3.2.3.** `STK-003`: Calon Staf Pramuniaga — Pengguna Operasional — Kategori: End-User Operasional
  - [ ] **3.2.4.** `STK-004`: Calon Staf Kasir — Pengguna Operasional — Kategori: End-User Operasional
  - [ ] **3.2.5.** `STK-005`: Calon Staf Desainer — Pengguna Operasional — Kategori: End-User Operasional
  - [ ] **3.2.6.** `STK-006`: Calon Staf Produksi Cetak — Pengguna Operasional — Kategori: End-User Operasional
  - [ ] **3.2.7.** `STK-007`: Calon Staf Fotocopy & Print Dokumen — Pengguna Operasional — Kategori: End-User Operasional
  - [ ] **3.2.8.** `STK-008`: Calon Staf Gudang — Pengguna Operasional — Kategori: End-User Operasional
  - [ ] **3.2.9.** `STK-009`: Tim AI — Gemini 3.1 Pro (High) — Lead Architect & Heavy Logic — Kategori: Tim Pengembang
  - [ ] **3.2.10.** `STK-010`: Tim AI — Gemini 3.1 Pro (Low) — Routine Coding & Documentation — Kategori: Tim Pengembang
  - [ ] **3.2.11.** `STK-011`: Tim AI — Gemini 3 Flash — Fast Reviewer & Debugger — Kategori: Tim Pengembang
  - [ ] **3.2.12.** `STK-012`: Tim AI — Claude Sonnet 4.6 (Thinking) — Deep Coder & Refactoring Specialist — Kategori: Tim Pengembang
  - [ ] **3.2.13.** `STK-013`: Tim AI — Claude Opus 4.6 (Thinking) — System Strategist & Security Lead — Kategori: Tim Pengembang
  - [ ] **3.2.14.** `STK-014`: Tim AI — GPT-OSS 120B (Medium) — Boilerplate Generator & Dummy Data Specialist — Kategori: Tim Pengembang

- [ ] **3.3.** Tulis **Sub-bagian 2.2: Stakeholder Eksternal** dalam format tabel yang sama:
  - [ ] **3.3.1.** `STK-015`: Pelanggan AbuCom — Penerima Layanan — Kategori: Indirect Stakeholder / Beneficiary
  - [ ] **3.3.2.** `STK-016`: Vendor & Supplier Bahan Baku / ATK — Penyedia Pasokan — Kategori: Indirect Stakeholder / Supply Chain
  - [ ] **3.3.3.** `STK-017`: Bank BRI — Kreditur Modal Berbunga — Kategori: Financial Stakeholder
  - [ ] **3.3.4.** `STK-018`: Bank Mandiri — Kreditur Modal Berbunga — Kategori: Financial Stakeholder
  - [ ] **3.3.5.** `STK-019`: Kerabat & Keluarga (Sahabat/Teman/Orang Tua) — Pemberi Pinjaman Tanpa Bunga — Kategori: Financial Stakeholder

---

### TAHAP 4: Penyusunan Profil Detail Setiap Stakeholder

> **Tujuan**: Membuat profil mendalam untuk setiap stakeholder yang sudah teridentifikasi. Profil ini harus informatif dan menjadi referensi utama bagi dokumen fase SDLC selanjutnya.

- [ ] **4.1.** Tulis **Bagian 3: Profil Detail Stakeholder**.

- [ ] **4.2.** Untuk **setiap** stakeholder dari STK-001 hingga STK-019, tulis sub-bagian profil detail dengan struktur sebagai berikut:

  ```markdown
  ### 3.X. [STK-XXX] Nama Stakeholder

  | Atribut | Detail |
  |---------|--------|
  | **ID Stakeholder** | STK-XXX |
  | **Nama / Jabatan** | ... |
  | **Organisasi / Afiliasi** | ... |
  | **Kategori** | Internal / Eksternal |
  | **Tipe** | Individu / Kelompok / Institusi |
  | **Peran dalam Proyek** | ... |
  | **Kontak / Identifikasi** | ... (jika tidak ada data, tandai: `*[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha]*`) |

  **Kebutuhan dan Ekspektasi Utama**:
  (Daftar bullet point kebutuhan spesifik stakeholder ini terhadap proyek)

  **Potensi Pengaruh terhadap Proyek**:
  (Jelaskan bagaimana stakeholder ini bisa mempengaruhi keberhasilan atau kegagalan proyek)

  **Potensi Dampak Proyek terhadap Stakeholder**:
  (Jelaskan bagaimana hasil proyek ini akan berdampak pada stakeholder ini)

  **Fase Keterlibatan Maksimal**:
  (Sebutkan fase SDLC di mana stakeholder ini paling banyak terlibat)
  ```

- [ ] **4.3.** Tulis profil detail **STK-001 (Pemilik Usaha AbuCom)** dengan data berikut:
  - Peran ganda: Inisiator Proyek, Sponsor Utama, Penyedia Pendanaan, Manajer Proyek Internal, Junior Programmer, dan Key User.
  - Kebutuhan: Otomatisasi seluruh operasional untuk menghilangkan burnout, laporan keuangan instan, kontrol penuh data sensitif (pinjaman, tabungan), delegasi 90% operasional ke staf baru.
  - Pengaruh: SANGAT TINGGI — pemegang keputusan mutlak atas seluruh aspek proyek (anggaran, scope, timeline, persetujuan deliverable).
  - Fase Keterlibatan Maksimal: Seluruh fase SDLC (Planning hingga Deployment).
  - Catatan khusus: Risiko burnout selama masa pengembangan karena masih menjalankan operasional toko sendirian (data dari narasi.txt dan Project Charter Risiko #1).

- [ ] **4.4.** Tulis profil detail **STK-002 hingga STK-008 (7 Posisi Calon Staf)** dengan data berikut untuk masing-masing:
  - Sumber data utama: Project Charter Bagian 7.2 (deskripsi tanggung jawab), Feasibility Study Bagian 5.1.2 dan 5.1.3.
  - Untuk setiap posisi staf, uraikan:
    - Tanggung jawab operasional spesifik mereka di dalam aplikasi CLI.
    - Kebutuhan mereka terhadap sistem (antarmuka CLI yang mudah, pelatihan, manual pengguna).
    - Ekspektasi mereka (sistem yang tidak menyulitkan pekerjaan mereka, insentif poin yang transparan).
    - Potensi pengaruh (rendah terhadap keputusan proyek, tinggi terhadap keberhasilan adopsi sistem).
    - Fase Keterlibatan Maksimal: Testing (UAT) dan Deployment.
  - Jika ada data kontak atau identitas personal yang belum tersedia, tandai: `*[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha setelah rekrutmen]*`

- [ ] **4.5.** Tulis profil detail **STK-009 hingga STK-014 (6 Tim Pengembang AI)** dengan data berikut:
  - Sumber data: Project Charter Bagian 7.1 (tabel tim pengembang).
  - Untuk setiap anggota tim AI, uraikan:
    - Spesialisasi teknis dan tanggung jawab spesifik.
    - Kebutuhan mereka (spesifikasi teknis yang jelas, instruksi kode yang rinci, standar coding FP yang konsisten).
    - Pengaruh terhadap proyek (tinggi — kualitas kode dan arsitektur bergantung pada output mereka).
    - Fase Keterlibatan Maksimal: Design, Implementation, Testing.

- [ ] **4.6.** Tulis profil detail **STK-015 (Pelanggan AbuCom)** dengan data berikut:
  - Sumber data: Narasi.txt (jenis layanan yang digunakan pelanggan), Project Charter Bagian 4.1 (modul CRM, Job Tracking, Arsip Desain).
  - Kebutuhan: Layanan cepat, pesanan tidak terlewat, kualitas cetak konsisten, kemudahan cetak ulang (arsip desain).
  - Pengaruh: Rendah (tidak terlibat langsung dalam proyek), namun kepuasan mereka adalah indikator utama keberhasilan proyek.
  - Kontak: `*[DATA BELUM TERSEDIA — akan tersedia setelah modul CRM diimplementasikan]*`

- [ ] **4.7.** Tulis profil detail **STK-016 (Vendor & Supplier)** dengan data berikut:
  - Sumber data: Narasi.txt (pengadaan bahan baku), Project Charter Bagian 4.1 (modul inventaris, riwayat harga beli, hutang supplier).
  - Kebutuhan: Pembayaran tepat waktu, volume pembelian konsisten.
  - Pengaruh: Sedang — ketersediaan bahan baku dari supplier mempengaruhi kelancaran produksi.

- [ ] **4.8.** Tulis profil detail **STK-017 dan STK-018 (Bank BRI & Bank Mandiri)** dengan data berikut:
  - Sumber data: Narasi.txt (pinjaman berbunga, setoran bulanan), Project Charter Bagian 6.1.
  - Kebutuhan: Setoran bulanan tepat waktu, kepatuhan terhadap jadwal tenor.
  - Pengaruh: Sedang-Tinggi — keterlambatan pembayaran dapat mempengaruhi likuiditas operasional proyek.

- [ ] **4.9.** Tulis profil detail **STK-019 (Kerabat & Keluarga)** dengan data berikut:
  - Sumber data: Narasi.txt (penjelasan detail tentang pinjaman tanpa bunga yang fleksibel), Project Charter Risiko #3.
  - Kebutuhan: Transparansi pencatatan saldo pinjaman, kemudahan penarikan dana kapan saja.
  - Pengaruh: TINGGI — penarikan dana mendadak dapat mengganggu arus kas pengembangan proyek secara serius.
  - Catatan khusus: Pola penarikan sangat tidak terprediksi (sebagian, total, permanen). Hubungan bersifat personal/emosional, bukan kontraktual formal.

---

### TAHAP 5: Penyusunan Klasifikasi Stakeholder

> **Tujuan**: Mengklasifikasikan semua stakeholder berdasarkan kategori standar industri dan menyusun matriks Power/Interest Grid.

- [ ] **5.1.** Tulis **Bagian 4: Klasifikasi Stakeholder**.

- [ ] **5.2.** Tulis **Sub-bagian 4.1: Berdasarkan Kategori Keterlibatan** dalam format tabel:
  | Kategori | ID Stakeholder |
  |----------|----------------|
  | Internal — Sponsor & Pengguna Utama | STK-001 |
  | Internal — End-User Operasional | STK-002 s.d. STK-008 |
  | Internal — Tim Pengembang | STK-009 s.d. STK-014 |
  | Eksternal — Beneficiary (Pelanggan) | STK-015 |
  | Eksternal — Supply Chain (Supplier) | STK-016 |
  | Eksternal — Financial (Kreditur) | STK-017, STK-018, STK-019 |

- [ ] **5.3.** Tulis **Sub-bagian 4.2: Matriks Power/Interest Grid** dalam format tabel 4 kuadran:

  Klasifikasikan setiap stakeholder ke dalam salah satu dari 4 kuadran berikut:
  - **Kuadran A (High Power / High Interest) — Manage Closely**: STK-001 (Pemilik Usaha)
  - **Kuadran B (High Power / Low Interest) — Keep Satisfied**: STK-017 (Bank BRI), STK-018 (Bank Mandiri), STK-019 (Kerabat & Keluarga)
  - **Kuadran C (Low Power / High Interest) — Keep Informed**: STK-002 s.d. STK-008 (Staf Operasional), STK-009 s.d. STK-014 (Tim AI)
  - **Kuadran D (Low Power / Low Interest) — Monitor**: STK-015 (Pelanggan), STK-016 (Supplier)

  Sajikan dalam format tabel:
  | ID | Stakeholder | Power (1-5) | Interest (1-5) | Kuadran | Strategi |

- [ ] **5.4.** Tulis **Sub-bagian 4.3: Matriks Pengaruh/Dampak** dalam format tabel:
  | ID | Stakeholder | Pengaruh terhadap Proyek (1-5) | Dampak Proyek terhadap Stakeholder (1-5) | Prioritas Pengelolaan |

---

### TAHAP 6: Penyusunan Analisis Sikap dan Keterlibatan

> **Tujuan**: Mengevaluasi tingkat keterlibatan saat ini vs yang diinginkan untuk setiap stakeholder.

- [ ] **6.1.** Tulis **Bagian 5: Analisis Sikap dan Tingkat Keterlibatan Stakeholder**.

- [ ] **6.2.** Tulis **Sub-bagian 5.1: Stakeholder Engagement Assessment Matrix** dalam format tabel:
  | ID | Stakeholder | Unaware | Resistant | Neutral | Supportive | Leading |

  Gunakan penanda `C` (Current/Saat Ini) dan `D` (Desired/Diinginkan) di kolom yang sesuai untuk setiap stakeholder. Contoh:
  - STK-001: Current = Leading, Desired = Leading
  - STK-002 s.d. STK-008: Current = Unaware (belum direkrut), Desired = Supportive
  - STK-009 s.d. STK-014: Current = Supportive, Desired = Leading
  - STK-015: Current = Unaware, Desired = Neutral
  - STK-019: Current = Neutral, Desired = Supportive

- [ ] **6.3.** Tulis **Sub-bagian 5.2: Analisis Gap Keterlibatan**. Jelaskan secara naratif gap yang signifikan, khususnya:
  - Gap terbesar pada STK-002 s.d. STK-008 (staf belum ada, perlu proses rekrutmen dan pelatihan).
  - Gap pada STK-019 (kerabat/keluarga yang perlu diyakinkan bahwa proyek ini bernilai investasi, agar tidak menarik dana mendadak).

---

### TAHAP 7: Penyusunan Kebutuhan, RACI, dan Strategi Komunikasi

> **Tujuan**: Menyusun tabel konsolidasi kebutuhan, matriks RACI yang diperluas, dan rencana komunikasi.

- [ ] **7.1.** Tulis **Bagian 6: Kebutuhan dan Ekspektasi Stakeholder** dalam format tabel konsolidasi:
  | ID | Stakeholder | Kebutuhan Utama | Ekspektasi terhadap Proyek | Kriteria Kepuasan |

  Isi untuk seluruh 19 stakeholder. Data diambil dari profil detail yang sudah disusun di Tahap 4.

- [ ] **7.2.** Tulis **Bagian 7: Matriks RACI Stakeholder**. Perluas matriks RACI dari Project Charter (Bagian 6.2) dengan memasukkan kolom untuk semua stakeholder yang teridentifikasi. Aktivitas/Deliverable yang harus dicakup:
  - [ ] Perencanaan & Project Charter
  - [ ] Penyusunan Stakeholder Register
  - [ ] Spesifikasi Kebutuhan (SRS)
  - [ ] Desain Arsitektur & DB (SDD)
  - [ ] Implementasi Kode Program
  - [ ] Pengujian Fungsional & UAT
  - [ ] Instalasi & Input Data Excel
  - [ ] Pelatihan Staf Operasional
  - [ ] Operasional & Rekonsiliasi Harian
  - [ ] Pengelolaan Pinjaman & Keuangan

- [ ] **7.3.** Tulis **Bagian 8: Strategi Pengelolaan dan Komunikasi Stakeholder**.

- [ ] **7.4.** Tulis **Sub-bagian 8.1: Rencana Komunikasi per Stakeholder** dalam format tabel:
  | ID | Stakeholder | Metode Komunikasi | Frekuensi | Penanggung Jawab | Informasi yang Dikomunikasikan |

  Tentukan metode komunikasi yang sesuai untuk masing-masing stakeholder:
  - STK-001 (Pemilik): Review langsung via CLI & dokumen SDLC, frekuensi harian/per sprint.
  - STK-002 s.d. STK-008 (Staf): Briefing operasional & User Manual CLI, frekuensi per go-live & harian.
  - STK-009 s.d. STK-014 (Tim AI): Issue/Prompt teknis terstruktur, frekuensi per sprint 2 mingguan.
  - STK-015 (Pelanggan): Tidak dikomunikasikan secara langsung tentang proyek (indirect).
  - STK-016 (Supplier): Komunikasi terkait pengadaan rutin, tidak terkait proyek langsung.
  - STK-017, STK-018 (Bank): Laporan keuangan & setoran bulanan, frekuensi bulanan.
  - STK-019 (Kerabat): Transparansi informal tentang perkembangan usaha, frekuensi insidental.

- [ ] **7.5.** Tulis **Sub-bagian 8.2: Strategi Mitigasi Resistensi** untuk stakeholder yang berpotensi resisten:
  - Karyawan baru (STK-002 s.d. STK-008): Pelatihan 3 hari, User Manual sederhana, sistem poin insentif sebagai motivasi.
  - Kerabat/Keluarga (STK-019): Transparansi pencatatan saldo, laporan usaha berkala agar merasa dana mereka aman dan dikelola dengan baik.

---

### TAHAP 8: Penyusunan Risiko, Persetujuan, Glosarium, dan Referensi

> **Tujuan**: Melengkapi bagian penutup dokumen.

- [ ] **8.1.** Tulis **Bagian 9: Risiko Terkait Stakeholder** dalam format tabel:
  | No | Risiko | Stakeholder Terkait | Probabilitas (1-5) | Dampak (1-5) | Rencana Mitigasi |

  Masukkan minimal risiko berikut (sumber: Project Charter Bagian 10 dan Feasibility Study Bagian 5.6 & 8.6):
  - [ ] **8.1.1.** Burnout pemilik menghambat proses klarifikasi kebutuhan (STK-001) — Prob: 3, Dampak: 5
  - [ ] **8.1.2.** Penarikan dana mendadak oleh kerabat/keluarga (STK-019) — Prob: 3, Dampak: 4
  - [ ] **8.1.3.** Kecurangan karyawan terhadap saldo digital/kas (STK-002 s.d. STK-008) — Prob: 3, Dampak: 5
  - [ ] **8.1.4.** Ketidaksesuaian literasi digital karyawan baru dengan CLI (STK-002 s.d. STK-008) — Prob: 3, Dampak: 3
  - [ ] **8.1.5.** Keterlambatan rekrutmen karyawan sebelum go-live (STK-002 s.d. STK-008) — Prob: 3, Dampak: 5
  - [ ] **8.1.6.** Human error input CLI oleh karyawan (STK-002 s.d. STK-008) — Prob: 4, Dampak: 3
  - [ ] **8.1.7.** Resistensi budaya cross-functional antar staf (STK-002 s.d. STK-008) — Prob: 3, Dampak: 3
  - [ ] **8.1.8.** Konflik selisih kas akibat cross-functional di PC kasir (STK-004) — Prob: 4, Dampak: 4
  - [ ] **8.1.9.** Kebocoran data pelanggan oleh karyawan yang menyalin database (STK-015 sebagai korban, STK-002 s.d. STK-008 sebagai pelaku) — Prob: 2, Dampak: 5
  - [ ] **8.1.10.** Ketidakcocokan kode saat integrasi modul dari AI berbeda (STK-009 s.d. STK-014) — Prob: 3, Dampak: 4

- [ ] **8.2.** Tulis **Bagian 10: Persetujuan dan Otorisasi** dalam format tabel:
  | Pihak Penandatangan | Jabatan / Peran | Tanda Tangan | Tanggal Persetujuan |
  Isi dengan: Pemilik Usaha AbuCom sebagai Sponsor Proyek dan Manajer Proyek Internal. Tanda tangan: *(Menunggu Persetujuan Digital)*. Tanggal: *(Belum disetujui)*.

- [ ] **8.3.** Tulis **Bagian 11: Glosarium** yang menjelaskan istilah khusus stakeholder management yang digunakan dalam dokumen ini. Minimal mencakup istilah berikut:
  - Stakeholder
  - Stakeholder Register
  - Power/Interest Grid
  - RACI Matrix (Responsible, Accountable, Consulted, Informed)
  - Stakeholder Engagement Assessment Matrix
  - Sponsor
  - Key User / End-User
  - Indirect Stakeholder
  - Financial Stakeholder
  - PKWT (Perjanjian Kerja Waktu Tertentu)
  - PKWTT (Perjanjian Kerja Waktu Tidak Tertentu)
  - Cross-Functional
  - Burnout
  - Role-Based Access Control (RBAC)
  - Audit Trail
  - UU PDP (UU Pelindungan Data Pribadi No. 27/2022)

- [ ] **8.4.** Tulis **Bagian 12: Referensi Dokumen** dalam format tabel:
  | # | Nama File | Lokasi Path Relatif | Keterangan Penggunaan |

  Isi dengan:
  - [ ] `01_project_charter.md` — `docs/sdlc/01_planning/01_project_charter.md` — Referensi utama data stakeholder, RACI, tim pengembang, struktur organisasi staf, dan risiko proyek.
  - [ ] `02_feasibility_study.md` — `docs/sdlc/01_planning/02_feasibility_study.md` — Referensi pendukung analisis kesiapan SDM, literasi digital, aspek ketenagakerjaan, dan risiko operasional/hukum.
  - [ ] `narasi.txt` — `docs/sdlc/narasi.txt` — Referensi konteks hubungan personal pemilik dengan pemberi pinjaman, kondisi emosional pemilik, dan budaya kerja yang diharapkan.

---

### TAHAP 9: Penulisan ke Target File dan Validasi Akhir

> **Tujuan**: Menuangkan seluruh hasil penyusunan ke dalam file target dan melakukan validasi kelengkapan.

- [ ] **9.1.** Tulis seluruh konten dokumen Stakeholder Register yang telah disusun dari Tahap 2 hingga Tahap 8 ke dalam file target: `docs/sdlc/01_planning/03_stakeholder_register.md`

- [ ] **9.2.** Validasi kelengkapan dokumen dengan checklist berikut:
  - [ ] **9.2.1.** Pastikan Front Matter YAML ada dan lengkap (dokumen, proyek, versi, tanggal, status, penyusun).
  - [ ] **9.2.2.** Pastikan Riwayat Perubahan Dokumen ada dan terisi.
  - [ ] **9.2.3.** Pastikan Bagian 1 (Informasi Dokumen) menjelaskan tujuan, ruang lingkup, dan hubungan dengan dokumen SDLC lain.
  - [ ] **9.2.4.** Pastikan seluruh 19 stakeholder teridentifikasi di Bagian 2 (tidak ada yang terlewat).
  - [ ] **9.2.5.** Pastikan seluruh 19 stakeholder memiliki profil detail di Bagian 3.
  - [ ] **9.2.6.** Pastikan Matriks Power/Interest Grid di Bagian 4 mencakup semua 19 stakeholder.
  - [ ] **9.2.7.** Pastikan Stakeholder Engagement Assessment Matrix di Bagian 5 mencakup semua 19 stakeholder.
  - [ ] **9.2.8.** Pastikan tabel Kebutuhan dan Ekspektasi di Bagian 6 mencakup semua 19 stakeholder.
  - [ ] **9.2.9.** Pastikan Matriks RACI di Bagian 7 mencakup semua aktivitas/deliverable yang relevan.
  - [ ] **9.2.10.** Pastikan Rencana Komunikasi di Bagian 8 mencakup semua 19 stakeholder.
  - [ ] **9.2.11.** Pastikan minimal 10 risiko terkait stakeholder ada di Bagian 9.
  - [ ] **9.2.12.** Pastikan Glosarium mencakup minimal 15 istilah.
  - [ ] **9.2.13.** Pastikan Referensi Dokumen mencantumkan 3 file sumber.
  - [ ] **9.2.14.** Pastikan semua data yang tidak tersedia ditandai dengan format: `*[DATA BELUM TERSEDIA — keterangan]*`
  - [ ] **9.2.15.** Pastikan tidak ada bagian yang berisi placeholder generik atau teks "Lorem Ipsum".
  - [ ] **9.2.16.** Pastikan seluruh isi dokumen menggunakan bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami.
  - [ ] **9.2.17.** Pastikan format Markdown valid (heading hierarchy, tabel, bullet points).

---

## 6. Instruksi Tambahan Khusus Dokumen Stakeholder Register

Berikut adalah instruksi tambahan yang merupakan kaidah standar pembuatan Stakeholder Register berdasarkan praktik industri terbaik. Instruksi ini **wajib dipatuhi** selain instruksi utama di atas:

### 6.1. Prinsip Kelengkapan dan Konsistensi Data
- [ ] Pastikan **setiap** stakeholder yang disebutkan di dokumen Project Charter Bagian 6 dan Bagian 7 tercantum di dalam Stakeholder Register ini. Jangan ada yang terlewat.
- [ ] Pastikan **ID Stakeholder** (STK-001 s.d. STK-019) digunakan secara konsisten di seluruh bagian dokumen (profil, klasifikasi, matriks, strategi komunikasi).
- [ ] Jika ada informasi yang bertentangan antara file referensi, **prioritaskan data dari Project Charter** (karena merupakan dokumen yang sudah divalidasi v1.1).

### 6.2. Prinsip Kualitas untuk Referensi SDLC Selanjutnya
- [ ] Pastikan setiap profil stakeholder memiliki informasi **Kebutuhan dan Ekspektasi** yang cukup spesifik agar bisa diterjemahkan menjadi kebutuhan fungsional di dokumen SRS nantinya.
- [ ] Pastikan matriks RACI diperluas dengan aktivitas yang mencakup **seluruh fase SDLC** (dari Planning hingga Deployment), bukan hanya fase yang ada di Project Charter saat ini.
- [ ] Pastikan strategi komunikasi stakeholder mencakup **fase pasca go-live (operasional)**, bukan hanya selama masa pengembangan.

### 6.3. Prinsip Penandaan Data Kosong
- [ ] Untuk setiap field yang datanya tidak tersedia di file referensi, gunakan format penandaan: `*[DATA BELUM TERSEDIA — <keterangan spesifik apa yang harus diisi dan oleh siapa>]*`
- [ ] Contoh: `*[DATA BELUM TERSEDIA — nama lengkap dan kontak staf perlu diisi manual oleh Pemilik Usaha setelah proses rekrutmen selesai]*`
- [ ] Jangan membuat data fiktif atau berasumsi. Jika tidak ada data, tandai saja.

### 6.4. Prinsip Bahasa dan Keterbacaan
- [ ] Gunakan bahasa Indonesia yang natural dan baku. Hindari kalimat yang terlalu panjang dan bertele-tele.
- [ ] Gunakan istilah teknis bahasa Inggris hanya jika sudah lazim digunakan di industri IT Indonesia (misal: stakeholder, sprint, go-live, RACI).
- [ ] Setiap istilah teknis yang digunakan pertama kali harus ada penjelasan singkat dalam kurung atau sudah tercantum di Glosarium.
- [ ] Hindari penggunaan kata ambigu seperti "mungkin", "barangkali", "sepertinya". Gunakan pernyataan definitif atau tandai sebagai estimasi.

### 6.5. Pemisahan Stakeholder Fase Pengembangan vs Fase Operasional
- [ ] Beri catatan eksplisit di dokumen bahwa **STK-002 s.d. STK-008 (Calon Staf)** saat ini belum direkrut dan keterlibatan aktif mereka baru dimulai pada Fase Testing (UAT) dan Fase Deployment (Go-Live).
- [ ] Beri catatan eksplisit bahwa **STK-009 s.d. STK-014 (Tim AI)** adalah stakeholder aktif selama Fase Design hingga Fase Testing, dan keterlibatan mereka menurun drastis setelah Go-Live (hanya bug fixing insidental).

### 6.6. Analisis Hubungan Antar-Stakeholder
- [ ] Tambahkan narasi singkat (bisa di dalam Bagian 4 atau Bagian 5) tentang hubungan kunci antar-stakeholder yang perlu diperhatikan:
  - **STK-001 ↔ STK-019**: Hubungan personal (keluarga/sahabat) yang berdampak finansial langsung pada proyek. Penarikan dana oleh STK-019 berdampak pada kemampuan STK-001 membiayai proyek.
  - **STK-001 ↔ STK-002 s.d. STK-008**: Hubungan atasan-bawahan. STK-001 harus berhasil merekrut dan melatih staf agar proyek berhasil secara operasional.
  - **STK-001 ↔ STK-009 s.d. STK-014**: Hubungan kolaborasi teknis. STK-001 sebagai integrator harus mampu menggabungkan output dari 6 AI berbeda.
  - **STK-004 (Kasir) ↔ STK-008 (Gudang)**: Hubungan operasional erat. Transaksi kasir langsung mempengaruhi stok gudang via BOM otomatis.

---

## 7. Catatan Penting untuk Pelaksana

> **PERINGATAN**: Instruksi di bawah ini wajib dipatuhi untuk menghindari kesalahan implementasi.

1. **JANGAN** mengarang data yang tidak ada di file referensi. Jika data tidak tersedia, tandai sesuai instruksi di Bagian 6.3.
2. **JANGAN** memodifikasi, menghapus, atau menimpa file referensi (`01_project_charter.md`, `02_feasibility_study.md`, `narasi.txt`). File-file tersebut hanya untuk **dibaca**.
3. **JANGAN** mengubah struktur kerangka dokumen yang sudah ditentukan di Bagian 4 issue ini, kecuali ada penambahan sub-bagian yang memperkaya informasi.
4. **PASTIKAN** file output ditulis ke lokasi yang benar: `docs/sdlc/01_planning/03_stakeholder_register.md`
5. **PASTIKAN** dokumen yang dihasilkan bisa langsung digunakan sebagai referensi oleh fase SDLC selanjutnya (Requirements/SRS) tanpa perlu revisi besar.
6. **PASTIKAN** seluruh tabel Markdown terformat dengan benar dan rapi (tidak ada kolom yang geser atau baris yang putus).
7. **GUNAKAN** separator `---` (horizontal rule) antar setiap bagian utama (## heading) untuk memudahkan pembacaan visual.
8. **PASTIKAN** kualitas kelengkapan isi dokumen ini sudah final dan tidak memerlukan interupsi berulang yang akan menghambat proses pekerjaan fase SDLC selanjutnya.

---

## 8. Ringkasan Checklist Eksekusi

Berikut adalah ringkasan singkat seluruh tahapan yang harus diselesaikan:

| Tahap | Deskripsi | Jumlah Sub-tugas |
|-------|-----------|:----------------:|
| **Tahap 1** | Pembacaan dan Perangkuman File Referensi | 19 sub-tugas |
| **Tahap 2** | Penyusunan Front Matter dan Bagian Awal | 4 sub-tugas |
| **Tahap 3** | Penyusunan Daftar Identifikasi Stakeholder | 18 sub-tugas |
| **Tahap 4** | Penyusunan Profil Detail Setiap Stakeholder | 9 sub-tugas |
| **Tahap 5** | Penyusunan Klasifikasi Stakeholder | 4 sub-tugas |
| **Tahap 6** | Penyusunan Analisis Sikap dan Keterlibatan | 3 sub-tugas |
| **Tahap 7** | Penyusunan Kebutuhan, RACI, dan Strategi Komunikasi | 5 sub-tugas |
| **Tahap 8** | Penyusunan Risiko, Persetujuan, Glosarium, dan Referensi | 4 sub-tugas |
| **Tahap 9** | Penulisan ke Target File dan Validasi Akhir | 19 sub-tugas |
| **Total** | | **85 sub-tugas** |

---

