# Validasi & Penyempurnaan Dokumen Use Case Diagram

---

## Informasi Issue

| Atribut         | Detail                                                                 |
|-----------------|------------------------------------------------------------------------|
| **Judul**       | Validasi, Analisis, dan Penyempurnaan Dokumen Use Case Diagram (UCD)   |
| **Dokumen Utama** | Use Case Diagram (UCD)                                               |
| **Target File** | `docs/sdlc/02_analysis/03_use_case_diagram.md`                         |
| **Lokasi Referensi** | `docs/sdlc/`                                                      |
| **Prioritas**   | High                                                                   |
| **Status**      | Open                                                                   |
| **Tanggal Dibuat** | 2026-05-23                                                          |
| **Dibuat Oleh** | Senior Systems Analyst & Documentation Lead                            |

---

## Latar Belakang

Dokumen `03_use_case_diagram.md` adalah **artefak ketiga dan penutup** pada **Fase 02 Analysis** dalam siklus SDLC AbuCom. Dokumen ini menjadi jembatan kritis antara BRD v1.1, SRS v1.1, dan seluruh dokumen fase desain (SDD, ERD, Skema Database) serta fase pengujian (Test Plan & UAT). Oleh karena itu, kualitas, kelengkapan, konsistensi, dan kebenaran isinya harus divalidasi secara menyeluruh dan ketat sebelum digunakan sebagai referensi primer oleh dokumen SDLC fase selanjutnya.

Issue ini mendefinisikan langkah-langkah validasi dan penyempurnaan dokumen tersebut secara **low-level dan terurut**, sehingga dapat dieksekusi secara mandiri oleh junior programmer atau LLM model AI lain yang lebih kecil tanpa ambiguitas.

---

## Persona Eksekutor

> **Anda adalah**: Senior Business Analyst & UML Modeling Specialist yang berpengalaman minimal 10 tahun di industri pengembangan perangkat lunak enterprise berbasis SDLC terstruktur. Anda memiliki keahlian mendalam dalam:
> - UML 2.5 (khususnya Use Case Diagram, notasi include/extend, system boundary, actor hierarchy)
> - Penulisan Use Case Specification naratif berkualitas industri (level IEEE 830 / Cockburn Style)
> - Validasi traceability matrix antar dokumen SDLC (BRD ↔ SRS ↔ UCD ↔ SDD)
> - Standar dokumentasi teknis berbahasa Indonesia yang natural, baku, dan tidak ambigu
> - Praktik RBAC, desain basis data ACID MySQL, dan arsitektur sistem CLI berbasis Python
>
> **Tugas utama Anda**: Memeriksa, menganalisis, memvalidasi, dan menyempurnakan dokumen Use Case Diagram ini sehingga memenuhi standar industri yang sesungguhnya dan siap dijadikan referensi primer yang tidak akan dipertanyakan oleh dokumen SDLC fase selanjutnya.

---

## Daftar Tugas Implementasi (Checklist)

> **PENTING — Baca seluruh issue ini terlebih dahulu sebelum mulai mengeksekusi tugas apapun.**
> Eksekusi setiap tugas **secara berurutan dari atas ke bawah**. Jangan melompati langkah.
> Tandai setiap tugas dengan `[x]` setelah selesai dikerjakan.

---

### FASE 0 — Persiapan & Pembacaan Dokumen

- [ ] **[BACA-01]** Baca seluruh isi file target dari baris pertama hingga baris terakhir:
  - File: `docs/sdlc/02_analysis/03_use_case_diagram.md`
  - Tujuan: Memahami keseluruhan struktur, konten, versi, dan status dokumen saat ini sebelum melakukan analisis apapun.

- [ ] **[BACA-02]** Baca seluruh isi file referensi utama berikut dari baris pertama hingga baris terakhir:
  - File 1: `docs/sdlc/02_analysis/01_business_requirements.md` (BRD)
  - File 2: `docs/sdlc/02_analysis/02_software_requirements.md` (SRS)
  - Tujuan: Mendapatkan data ground truth lengkap agar dapat dilakukan komparasi mendalam terhadap dokumen UCD.

- [ ] **[BACA-03]** Baca seluruh isi file referensi pendukung berikut:
  - File 3: `docs/sdlc/01_planning/03_stakeholder_register.md`
  - File 4: `docs/sdlc/01_planning/01_project_charter.md`
  - File 5: `docs/sdlc/01_planning/05_innovation_proposal.md`
  - Tujuan: Mendapatkan konteks bisnis, daftar stakeholder, cakupan 10 modul sistem, dan 43 inovasi yang memengaruhi desain use case.

- [ ] **[BACA-04]** Baca narasi konteks proyek tambahan jika ada:
  - File: `docs/sdlc/narasi.txt`
  - Tujuan: Mendapatkan narasi bisnis tambahan yang mungkin belum tercakup di BRD/SRS.

---

### FASE 1 — Validasi Kelengkapan (Completeness Check)

> Tujuan fase ini: Memastikan **tidak ada data penting dari dokumen referensi yang terlewat** di dalam dokumen UCD.

- [ ] **[VAL-01]** Buat catatan kerja sementara (di memori atau scratch) berisi:
  - Daftar semua ID kebutuhan bisnis fungsional dari BRD (contoh: BR-F-01 s.d BR-F-40).
  - Daftar semua ID spesifikasi teknis fungsional dari SRS (contoh: SRS-F-001 s.d SRS-F-040+).
  - Daftar semua aktor yang disebutkan di BRD dan SRS (nama, role, hak akses).

- [ ] **[VAL-02]** Periksa apakah **setiap** ID kebutuhan bisnis fungsional dari BRD (BR-F-xx) sudah memiliki satu atau lebih use case yang men-derivasinya di kolom `Derivasi BRD` pada tabel Master Daftar Use Case (Bagian 3.2). Catat seluruh ID yang tidak terpetakan (gap/missing).

- [ ] **[VAL-03]** Periksa apakah **setiap** ID spesifikasi fungsional dari SRS (SRS-F-xxx) sudah terpetakan di kolom `Derivasi SRS` pada tabel Master Daftar Use Case (Bagian 3.2). Catat seluruh ID yang tidak terpetakan.

- [ ] **[VAL-04]** Periksa apakah seluruh **aktor** (nama dan role sistem) yang disebutkan di BRD dan SRS sudah terdefinisi lengkap di Bagian 2 (Identifikasi Aktor) dokumen UCD. Catat aktor yang hilang atau namanya berbeda.

- [ ] **[VAL-05]** Periksa apakah seluruh **hak akses per aktor** (RBAC) yang didefinisikan di BRD sudah tercermin secara akurat di kolom `Hak Akses Utama` pada Tabel 2.1 dan di kolom `Aktor Primer`/`Aktor Sekunder` pada Tabel 3.2.

- [ ] **[VAL-06]** Periksa apakah seluruh **relasi `<<include>>` dan `<<extend>>`** antar use case yang disebutkan di SRS sudah dimuat secara konsisten di:
  - Diagram Mermaid per modul (Bagian 4.2).
  - Bagian 6 (Relasi Dependensi Use Case).
  Catat relasi yang tidak konsisten atau belum ada.

- [ ] **[VAL-07]** Periksa apakah seluruh **inovasi** yang didefinisikan di `05_innovation_proposal.md` yang berdampak langsung pada fungsionalitas sistem (khususnya yang memunculkan use case baru) sudah ter-representasi dalam dokumen UCD.

- [ ] **[VAL-08]** Periksa apakah **Matriks Traceability** (Bagian 7) sudah mencakup seluruh 44 use case (UC-001 s.d UC-044) dan seluruh 12 aktor (8 internal + 4 eksternal). Catat baris atau kolom yang hilang.

---

### FASE 2 — Validasi Relevansi & Fokus (Relevance & Scope Check)

> Tujuan fase ini: Memastikan dokumen **hanya berisi** konten yang memang merupakan domain Use Case Diagram, tidak lebih dan tidak kurang.

- [ ] **[REL-01]** Periksa apakah ada konten yang **terlalu teknis/implementatif** untuk level dokumen UCD (misalnya: detail schema SQL, konfigurasi server, pseudocode implementasi Python). Jika ada, tandai untuk dihapus atau dipindahkan ke keterangan minimal.
  - Standar: Dokumen UCD **boleh** menyebutkan tipe data teknis sebagai catatan (`Catatan Khusus`) namun **tidak boleh** memuat spesifikasi implementasi yang seharusnya ada di SDD atau ERD.

- [ ] **[REL-02]** Periksa apakah ada konten yang **lebih cocok di BRD** (seperti deskripsi narasi bisnis panjang, aturan bisnis yang tidak relevan dengan alur use case). Tandai untuk dipadatkan atau dihapus.

- [ ] **[REL-03]** Periksa apakah setiap **Use Case Specification** (Bagian 5) benar-benar berfokus pada **interaksi aktor-sistem** dalam konteks terminal CLI, bukan pada detail implementasi basis data atau pseudocode algoritma.

- [ ] **[REL-04]** Periksa apakah **Diagram Mermaid** (Bagian 4) sudah konsisten merepresentasikan **Use Case Diagram UML** (bukan sequence diagram, class diagram, atau flowchart proses bisnis). Pastikan elemen aktor, system boundary, dan use case sudah benar secara notasi UML.

- [ ] **[REL-05]** Periksa apakah **Glosarium** (Bagian 8) hanya memuat istilah yang benar-benar digunakan di dalam dokumen UCD ini, tidak memuat istilah yang hanya relevan di dokumen lain (SRS atau SDD).

---

### FASE 3 — Validasi Standar Struktur Dokumen (Structure & Format Check)

> Tujuan fase ini: Memastikan dokumen memiliki **struktur standar industri** yang lengkap, konsisten, dan informatif.

- [ ] **[STR-01]** Periksa **front matter** (metadata YAML di baris 1–8) apakah sudah memuat: dokumen, proyek, versi, tanggal, status, dan penyusun. Pastikan tidak ada field yang kosong atau tidak konsisten dengan isi dokumen.

- [ ] **[STR-02]** Periksa apakah **Riwayat Perubahan Dokumen** sudah ada dan formatnya lengkap (kolom: Versi, Tanggal, Perubahan, Oleh). Pastikan entri riwayat konsisten dengan versi di front matter.

- [ ] **[STR-03]** Periksa apakah **Bagian 1 (Informasi Dokumen)** memuat minimal:
  - 1.1 Tujuan Dokumen
  - 1.2 Cakupan Dokumen
  - 1.3 Posisi Dokumen dalam SDLC (dengan diagram ASCII/Mermaid)
  - 1.4 Hubungan dengan Dokumen SDLC Lainnya (input & output)
  - 1.5 Audiens Target

- [ ] **[STR-04]** Periksa apakah **Bagian 2 (Identifikasi Aktor)** memuat:
  - 2.1 Tabel Aktor Internal (dengan kolom: ID Aktor, Nama, Role Sistem, Deskripsi, Hak Akses Utama)
  - 2.2 Tabel Aktor Eksternal (dengan kolom: ID Aktor, Nama, Deskripsi, Hubungan dengan Sistem)
  - 2.3 Diagram Generalisasi Hierarki Aktor (Mermaid)

- [ ] **[STR-05]** Periksa apakah **Bagian 3 (System Boundary & Daftar Use Case)** memuat:
  - 3.1 Definisi System Boundary (apa yang di dalam dan di luar batas sistem)
  - 3.2 Master Daftar Use Case (tabel dengan kolom: UC-ID, Nama, Modul, Aktor Primer, Aktor Sekunder, Prioritas, Derivasi BRD, Derivasi SRS)

- [ ] **[STR-06]** Periksa apakah **Bagian 4 (Use Case Diagram Visual)** memuat:
  - 4.1 Diagram Overview Keseluruhan Sistem
  - 4.2.1 s.d 4.2.10 Diagram per Modul (M.1 s.d M.10)
  - Setiap diagram harus menampilkan: aktor yang relevan, use case dalam system boundary, dan relasi include/extend yang berlaku.

- [ ] **[STR-07]** Periksa apakah **Bagian 5 (Use Case Specification)** memuat narasi untuk **seluruh 44 use case** dengan atribut lengkap per use case:
  - UC-ID, Nama Use Case, Derivasi, Modul, Prioritas
  - Aktor Primer, Aktor Sekunder
  - Deskripsi Singkat
  - Prakondisi (Precondition)
  - Pemicu (Trigger)
  - Alur Utama (Main Flow) — minimal 4 langkah sekuensial
  - Alur Alternatif (Alternative Flow)
  - Alur Pengecualian (Exception Flow) — dengan kode error eksplisit
  - Pasca-Kondisi (Postcondition)
  - Aturan Bisnis Terkait
  - Catatan Khusus
  - Catat setiap use case yang atributnya kurang lengkap.

- [ ] **[STR-08]** Periksa apakah **Bagian 6 (Relasi Dependensi Use Case)** memuat:
  - Tabel atau daftar semua relasi `<<include>>` dengan format: use case pemanggil → use case di-include, beserta alasan ketergantungan.
  - Tabel atau daftar semua relasi `<<extend>>` dengan format: use case dasar ← use case ekstensi, beserta kondisi trigger ekstensi.

- [ ] **[STR-09]** Periksa apakah **Bagian 7 (Matriks Traceability)** memuat:
  - Matriks dengan baris = UC-ID dan kolom = seluruh aktor (P/S/-)
  - Matriks atau tabel dengan referensi silang UC-ID ↔ BR-F-xx ↔ SRS-F-xxx

- [ ] **[STR-10]** Periksa apakah **Bagian 8 (Glosarium)** memuat semua istilah teknis domain UML dan domain bisnis percetakan yang digunakan di dalam dokumen.

- [ ] **[STR-11]** Periksa apakah **Bagian 9 (Referensi Dokumen)** memuat tabel referensi dengan semua file yang digunakan sebagai sumber data, dengan kolom: No, Nama Berkas, Lokasi Path Relatif, Keterangan.

---

### FASE 4 — Validasi Kesiapan sebagai Input SDLC Berikutnya (Downstream Readiness Check)

> Tujuan fase ini: Memastikan dokumen ini **layak dan cukup** sebagai referensi primer untuk dokumen fase berikutnya.

- [ ] **[DOWN-01]** Validasi kesiapan untuk **System Design Document (SDD)**:
  - Apakah setiap use case sudah cukup menjelaskan alur interaksi aktor-sistem sehingga tim desain dapat mengidentifikasi pure functions Python yang diperlukan?
  - Apakah Main Flow setiap use case cukup detail untuk dijadikan basis sequence diagram?
  - Catat use case yang main flow-nya masih terlalu abstrak atau tidak operasional.

- [ ] **[DOWN-02]** Validasi kesiapan untuk **ERD & Skema Database**:
  - Apakah setiap use case yang melibatkan operasi data sudah menyebutkan nama tabel database yang terlibat (setidaknya di bagian Pasca-Kondisi atau Catatan Khusus)?
  - Apakah entitas bisnis kunci (pelanggan, transaksi, barang, karyawan, dll.) sudah dapat diidentifikasi dari dokumen UCD?
  - Catat use case yang sama sekali tidak menyebut entitas data yang relevan.

- [ ] **[DOWN-03]** Validasi kesiapan untuk **Test Plan & UAT**:
  - Apakah setiap use case sudah memiliki minimal 1 Exception Flow dengan kode error yang eksplisit (format ERR-xxx-xxx)?
  - Apakah Prakondisi dan Pasca-Kondisi sudah testable (dapat dijadikan test assertion)?
  - Catat use case yang exception flow-nya masih kosong atau tidak memiliki kode error.

- [ ] **[DOWN-04]** Validasi kesiapan untuk **dokumen downstream** secara umum:
  - Apakah semua singkatan, kode referensi (BR-F-xx, SRS-F-xxx, UC-xxx), dan ID aktor konsisten antara Bagian 2, 3, 4, 5, 6, 7, dan 9?
  - Apakah tidak ada kontradiksi antara hak akses aktor di Bagian 2 dengan daftar aktor primer di Bagian 3 dan 5?

---

### FASE 5 — Validasi Bahasa Indonesia (Language Quality Check)

> Tujuan fase ini: Memastikan bahasa yang digunakan **natural, tidak ambigu, dan mudah dipahami** oleh junior programmer atau LLM model AI lain yang lebih kecil.

- [ ] **[LANG-01]** Periksa setiap kalimat dalam deskripsi use case (kolom Deskripsi Singkat, Main Flow, Alternative Flow, Exception Flow) apakah:
  - Menggunakan Bahasa Indonesia baku yang natural (bukan bahasa campuran tidak perlu atau kalimat terbalik).
  - Tidak mengandung kata ganti yang ambigu ("itu", "tersebut", "yang ini") tanpa referensi subjek yang jelas.
  - Tidak menggunakan istilah teknis bahasa Inggris yang tidak perlu jika tersedia padanan Indonesia yang baku.

- [ ] **[LANG-02]** Periksa konsistensi penulisan istilah teknis di seluruh dokumen. Contoh yang harus konsisten:
  - "Uang Muka" vs "DP" (pilih satu atau definisikan kedua istilah secara eksplisit).
  - "Stok" vs "Stock" (pilih penulisan konsisten).
  - "Aktor Primer" vs "Aktor Utama" (pilih satu istilah di semua bagian).
  - "Main Flow" vs "Alur Utama" (konsisten antara header dan isi tabel).
  - Catat semua inkonsistensi terminologi yang ditemukan.

- [ ] **[LANG-03]** Periksa apakah langkah-langkah **Main Flow** ditulis dalam format yang seragam:
  - Harus diawali dengan subjek yang jelas (Aktor/Sistem).
  - Harus berupa kalimat aktif yang menggambarkan aksi konkret dan terukur.
  - Bukan kalimat pasif yang ambigu.

- [ ] **[LANG-04]** Periksa apakah **judul bagian dan sub-bagian** konsisten menggunakan format yang sama (kapital, urutan penomoran, gaya bahasa).

- [ ] **[LANG-05]** Periksa apakah setiap istilah baru yang digunakan pertama kali di dokumen sudah didefinisikan atau ada padanannya di **Bagian 8 (Glosarium)**.

---

### FASE 6 — Validasi Kelayakan Isi (Content Quality Check)

> Tujuan fase ini: Memastikan isi dokumen **tidak akan selalu dipertanyakan** sehingga tidak menghambat pekerjaan fase SDLC selanjutnya.

- [ ] **[QUAL-01]** Periksa apakah **setiap use case memiliki deskripsi singkat** yang langsung menjawab pertanyaan: "Siapa melakukan apa, dalam kondisi apa, dengan hasil apa?" Perbaiki deskripsi yang masih terlalu generik atau tidak informatif.

- [ ] **[QUAL-02]** Periksa apakah **tidak ada use case yang duplikat** (fungsionalitas yang sama tetapi memiliki dua ID UC yang berbeda). Jika ditemukan, konsolidasikan.

- [ ] **[QUAL-03]** Periksa apakah **tidak ada use case yang hilang** yang seharusnya ada berdasarkan BRD/SRS tetapi tidak memiliki entri di Bagian 3.2 maupun Bagian 5.

- [ ] **[QUAL-04]** Periksa apakah **klaim angka di Bagian 1.2** (cakupan dokumen) konsisten dengan konten aktual dokumen:
  - Jumlah aktor internal yang disebutkan (klaim: 8) vs yang terdaftar di Bagian 2.1.
  - Jumlah aktor eksternal (klaim: 4) vs yang terdaftar di Bagian 2.2.
  - Jumlah total use case (klaim: 44) vs yang terdaftar di Bagian 3.2 dan Bagian 5.
  - Jumlah diagram Mermaid (klaim: 11 diagram = 1 overview + 10 sub-modul) vs yang aktual ada di Bagian 4.

- [ ] **[QUAL-05]** Periksa apakah **nomor UC di diagram Mermaid** konsisten dengan nomor UC di Bagian 3.2 dan Bagian 5. Tidak boleh ada use case yang ada di diagram tetapi tidak ada spesifikasi naratifnya (atau sebaliknya).

- [ ] **[QUAL-06]** Periksa apakah ada **kolom atau field yang kosong, bernilai "N/A" tanpa alasan, atau masih berisi placeholder** yang belum diisi. Jika ada, isi dengan data yang sesuai berdasarkan konteks BRD, SRS, dan dokumen referensi lainnya.

- [ ] **[QUAL-07]** Periksa apakah **tingkat prioritas (High/Medium/Low)** setiap use case di Bagian 3.2 konsisten dan masuk akal dari sudut pandang bisnis. Prioritas "High" harus diberikan kepada use case yang memblokir fungsi inti jika tidak diimplementasikan.

- [ ] **[QUAL-08]** Periksa apakah **Diagram Mermaid** di Bagian 4 memiliki sintaks yang valid dan tidak akan menyebabkan render error. Pastikan:
  - Tidak ada karakter khusus tanpa escaping yang benar.
  - Setiap node yang direferensikan dalam relasi sudah dideklarasikan.
  - Label relasi menggunakan format yang benar (`-.->|"<<include>>"| UC-xxx`).

---

### FASE 7 — Validasi Data Kosong & Pengisian (Data Completeness Fill-in)

> Tujuan fase ini: Mengidentifikasi dan **mengisi data yang kosong** dengan data yang relevan dan sesuai.

- [ ] **[FILL-01]** Buat daftar semua field/kolom yang ditemukan kosong atau tidak lengkap pada hasil Fase 1 s.d Fase 6 di atas.

- [ ] **[FILL-02]** Untuk setiap **Use Case Specification yang Alur Alternatif-nya kosong** (berisi `"-"`):
  - Analisis apakah benar-benar tidak ada alur alternatif yang valid untuk use case tersebut berdasarkan konteks BRD/SRS.
  - Jika ada alur alternatif yang terlewat, tambahkan dengan format: `A1. [Nama Kondisi]: [Deskripsi langkah alternatif]`.
  - Jika memang tidak ada, biarkan tetap `"-"` namun pastikan sudah dianalisis dan diverifikasi.

- [ ] **[FILL-03]** Untuk setiap **Use Case Specification yang Exception Flow-nya kosong atau generik**:
  - Tambahkan minimal satu kode error eksplisit berformat `ERR-[KATEGORI]-[NOMOR]`.
  - Deskripsi exception flow harus mencakup: kondisi pemicu error, aksi sistem, dan pesan yang ditampilkan ke pengguna.

- [ ] **[FILL-04]** Untuk setiap **Aturan Bisnis Terkait yang masih generik** (tidak spesifik):
  - Isi dengan aturan bisnis yang konkret dan dapat diverifikasi, berdasarkan data dari BRD atau SRS.

- [ ] **[FILL-05]** Pastikan semua **referensi silang BR-F-xx dan SRS-F-xxx** di kolom Derivasi BRD/SRS sudah benar dan merujuk pada ID yang sesungguhnya ada di dokumen BRD dan SRS (bukan ID fiktif).

---

### FASE 8 — Konsolidasi Temuan & Penulisan Ulang (Revision & Overwrite)

> Tujuan fase ini: **Menuangkan kembali seluruh dokumen yang telah divalidasi dan diperbaiki** ke file target.

- [ ] **[REVISI-01]** Buat ringkasan internal (di memori) dari **semua temuan dan perbaikan** dari Fase 1 s.d Fase 7, meliputi:
  - Daftar gap kelengkapan yang ditemukan dan cara pengisiannya.
  - Daftar inkonsistensi yang ditemukan dan cara perbaikannya.
  - Daftar data yang diisi (field kosong yang sudah diisi).
  - Daftar perubahan bahasa yang dilakukan.

- [ ] **[REVISI-02]** Tulis ulang **versi dokumen** dari `1.0` menjadi `1.1` di:
  - Field `versi` pada front matter YAML (baris paling atas dokumen).
  - Baris pertama tabel **Riwayat Perubahan Dokumen**: tambahkan entri baru versi `1.1` dengan:
    - Tanggal: tanggal hari ini saat revisi dilakukan.
    - Kolom Perubahan: deskripsi singkat seluruh perbaikan yang dilakukan.
    - Kolom Oleh: `Senior Business Analyst & UML Modeling Specialist`.

- [ ] **[REVISI-03]** Tulis ulang dokumen **secara menyeluruh dan lengkap** dengan cara **menimpa (overwrite)** file target:
  - File target: `docs/sdlc/02_analysis/03_use_case_diagram.md`
  - **WAJIB**: Tuliskan **seluruh teks dari baris pertama (front matter) hingga baris terakhir (Bagian 9 Referensi)** secara penuh.
  - **DILARANG KERAS**: Memotong, meringkas, menghilangkan, atau menyingkat bagian manapun dari dokumen (`no truncation`).
  - Semua perbaikan dari Fase 1–7 harus sudah terintegrasi ke dalam konten yang ditulis ulang.
  - Pastikan format Markdown tetap rapi dan konsisten.

- [ ] **[REVISI-04]** Jika dalam proses validasi ditemukan **file referensi tambahan** (di luar 5 referensi yang sudah terdaftar di Bagian 9) yang digunakan sebagai sumber data perbaikan, tambahkan file tersebut ke tabel **Bagian 9 (Referensi Dokumen)** di bagian baris paling bawah tabel, dengan mengisi semua kolom (No, Nama Berkas, Lokasi Path Relatif, Keterangan).

---

### FASE 9 — Verifikasi Akhir (Final Verification)

> Tujuan fase ini: Memastikan file hasil overwrite sudah benar dan tidak ada data yang hilang.

- [ ] **[VER-01]** Baca ulang file hasil overwrite dari baris pertama hingga akhir:
  - File: `docs/sdlc/02_analysis/03_use_case_diagram.md`
  - Verifikasi bahwa versi di front matter sudah berubah menjadi `1.1`.
  - Verifikasi bahwa entri riwayat perubahan versi `1.1` sudah ada di tabel Riwayat.

- [ ] **[VER-02]** Verifikasi kelengkapan struktur dokumen hasil revisi:
  - [ ] Bagian 1 (Informasi Dokumen) — ada dan lengkap
  - [ ] Bagian 2 (Identifikasi Aktor) — ada, tabel lengkap, diagram hierarki ada
  - [ ] Bagian 3 (System Boundary & Daftar UC) — ada, tabel UC-001 s.d UC-044 semua ada
  - [ ] Bagian 4 (Diagram Visual Mermaid) — ada, 1 overview + 10 diagram per modul
  - [ ] Bagian 5 (Use Case Specification) — ada, semua 44 UC memiliki spesifikasi naratif lengkap
  - [ ] Bagian 6 (Relasi Dependensi) — ada, tabel include dan extend lengkap
  - [ ] Bagian 7 (Matriks Traceability) — ada, semua UC dan semua aktor tercakup
  - [ ] Bagian 8 (Glosarium) — ada, semua istilah kunci terdefinisi
  - [ ] Bagian 9 (Referensi Dokumen) — ada, semua file referensi terdaftar

- [ ] **[VER-03]** Verifikasi bahwa jumlah use case di dokumen hasil revisi **tetap 44** (atau lebih jika ditemukan use case yang seharusnya ada dari BRD/SRS namun belum terdaftar). Hitung jumlah use case di Bagian 3.2 dan Bagian 5, pastikan konsisten.

- [ ] **[VER-04]** Verifikasi bahwa tidak ada **konten terpotong** di akhir dokumen. File harus diakhiri dengan tabel Referensi Dokumen (Bagian 9) yang lengkap, diikuti newline akhir yang bersih.

- [ ] **[VER-05]** Laporkan **ringkasan hasil validasi** secara singkat dalam format berikut (tuliskan sebagai komentar atau sebagai output terminal, bukan ditambahkan ke dalam file target):
  ```
  === LAPORAN VALIDASI ISSUE-0016 ===
  File Target    : docs/sdlc/02_analysis/03_use_case_diagram.md
  Versi Sebelum  : 1.0
  Versi Sesudah  : 1.1
  Total UC       : [jumlah]
  Gap BRD        : [daftar ID atau "Tidak ada"]
  Gap SRS        : [daftar ID atau "Tidak ada"]
  Data Diisi     : [jumlah field yang diisi]
  Inkonsistensi  : [jumlah temuan]
  Ref Baru       : [nama file atau "Tidak ada"]
  Status         : SELESAI / ADA HAMBATAN
  ===================================
  ```

---

## Aturan Mutlak Pelaksanaan

> Baca dan patuhi aturan berikut **tanpa pengecualian**:

1. **Urutan Eksekusi**: Lakukan semua tugas **secara berurutan** sesuai nomor fase. Jangan mengerjakan FASE 8 sebelum FASE 1–7 selesai.
2. **No Truncation**: Saat menulis ulang file target (REVISI-03), **seluruh dokumen harus ditulis penuh** dari baris pertama hingga terakhir. Tidak boleh ada bagian yang disingkat, dipotong, atau diringkas dengan kalimat seperti "... (konten lainnya tetap sama) ...".
3. **Overwrite, Bukan Append**: Penulisan ke file target dilakukan dengan **menimpa (overwrite)** seluruh konten file, bukan menambahkan di akhir file.
4. **Data Berdasarkan Referensi**: Setiap data yang ditambahkan atau diubah **harus dapat ditelusuri** ke salah satu dokumen referensi (BRD, SRS, Stakeholder Register, Project Charter, atau Innovation Proposal). Jangan mengarang data yang tidak ada dasar referensinya.
5. **Jangan Ubah Struktur Bagian**: Nomor dan urutan bagian (Bagian 1 s.d Bagian 9) **tidak boleh diubah**. Perbaikan dilakukan pada konten di dalam bagian tersebut.
6. **Konsistensi ID**: ID use case, ID aktor, ID kebutuhan BRD/SRS, dan kode error **tidak boleh diubah** kecuali ditemukan ada ID yang salah merujuk (harus dicatat dan diperbaiki sesuai dokumen referensi aslinya).
7. **Versi Dokumen**: Setiap revisi yang mengubah konten apapun **wajib menaikkan versi** dokumen (dari `1.0` ke `1.1`) dan **wajib menambahkan baris baru di tabel Riwayat Perubahan**.

---

## Kriteria Penyelesaian Issue

Issue ini dinyatakan **SELESAI** apabila **seluruh** kondisi berikut terpenuhi:

- [ ] Seluruh 9 fase validasi (FASE 0 s.d FASE 9) telah dilaksanakan dan semua checklist ditandai `[x]`.
- [ ] File `docs/sdlc/02_analysis/03_use_case_diagram.md` telah ditulis ulang secara penuh (overwrite) tanpa truncation.
- [ ] Versi dokumen di front matter berubah dari `1.0` menjadi `1.1`.
- [ ] Baris riwayat perubahan versi `1.1` sudah ditambahkan di tabel Riwayat Perubahan.
- [ ] Tidak ada field kosong, placeholder, atau data yang hilang di dokumen hasil revisi.
- [ ] Laporan validasi (VER-05) sudah dibuat dan dilaporkan.

---

## Referensi File untuk Issue Ini

| # | Nama Berkas | Lokasi Path Relatif | Peran dalam Issue |
|---|---|---|---|
| 1 | `03_use_case_diagram.md` | `docs/sdlc/02_analysis/03_use_case_diagram.md` | **Target File** — dokumen yang divalidasi dan ditulis ulang |
| 2 | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | Referensi utama BRD — sumber ground truth BR-F-xx dan aktor |
| 3 | `02_software_requirements.md` | `docs/sdlc/02_analysis/02_software_requirements.md` | Referensi utama SRS — sumber ground truth SRS-F-xxx dan relasi include/extend |
| 4 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Referensi profil aktor dan stakeholder |
| 5 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Referensi visi misi, cakupan 10 modul, dan tim proyek |
| 6 | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Referensi 43 inovasi yang memengaruhi use case operasional |
| 7 | `narasi.txt` | `docs/sdlc/narasi.txt` | Referensi narasi konteks bisnis tambahan |
