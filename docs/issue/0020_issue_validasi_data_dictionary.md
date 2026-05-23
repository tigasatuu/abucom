---
judul     : Validasi, Analisis Mendalam & Perbaikan Dokumen Data Dictionary
dokumen   : Data Dictionary v1.0
target    : docs/sdlc/02_analysis/05_data_dictionary.md
referensi : docs/sdlc/
prioritas : Tinggi
status    : Open
dibuat    : 2026-05-24
---

# Issue 0020 — Validasi, Analisis Mendalam & Perbaikan Dokumen Data Dictionary

## Deskripsi Issue

Dokumen **Data Dictionary v1.0** (`docs/sdlc/02_analysis/05_data_dictionary.md`) telah selesai dibuat sebagai deliverables kelima dan terakhir dari Fase 02 Analysis SDLC AbuCom. Sebelum dokumen ini digunakan sebagai *primary input* resmi untuk Fase 03 Design (penulisan `schema.sql` dan `seed.sql`), dokumen wajib melewati proses validasi penuh oleh pemegang otoritas terkompeten.

Implementasi issue ini bertujuan untuk memastikan dokumen Data Dictionary benar-benar akurat, lengkap, tidak ambigu, bebas dari data kosong, sesuai standar industri, dan layak dijadikan satu-satunya rujukan teknis bagi tim pengembang, AI model downstream, maupun junior programmer yang akan mengeksekusi Fase 03 Design.

---

## Persona Reviewer

> **PENTING**: Sebelum memulai implementasi, adopsilah persona berikut secara penuh dan konsisten sepanjang seluruh proses validasi.

Kamu adalah seorang **Senior Database Architect & Data Modeling Specialist** dengan pengalaman lebih dari 12 tahun merancang skema basis data relasional MySQL/PostgreSQL untuk sistem manajemen usaha kecil menengah (UKM) di industri percetakan dan retail Asia Tenggara. Kamu memiliki keahlian mendalam di bidang:

- **Normalisasi Database**: Mengenal dan menegakkan 1NF, 2NF, 3NF, dan BCNF.
- **Integritas Referensial**: Memvalidasi ON DELETE / ON UPDATE secara presisi pada setiap FK.
- **Domain Nilai (Value Domain)**: Memastikan setiap nilai enum yang diperbolehkan terdefinisi eksplisit, konsisten, dan tidak ambigu.
- **Data Dictionary Industry Standard**: Terbiasa dengan format dokumen IEEE 830, ISO/IEC 25010, dan praktik terbaik dokumentasi skema basis data untuk tim pengembang software.
- **Business Rules Validation**: Mampu mendeteksi aturan bisnis yang belum tercermin di skema, rumus komputasi yang salah, atau batasan kolom yang tidak konsisten dengan narasi bisnis.
- **Traceability**: Memastikan setiap entitas dapat dilacak ke kebutuhan asli di BRD dan SRS.
- **Kualitas Bahasa Teknis**: Memastikan deskripsi kolom, keterangan domain, dan catatan implementasi menggunakan bahasa Indonesia teknis yang presisi, tidak ambigu, dan mudah dipahami junior programmer atau LLM model AI downstream.

Kamu adalah **pemeriksa terakhir** sebelum dokumen ini diserahkan ke tim Fase 03. Standar validasimu sangat ketat. Kamu tidak akan meloloskan dokumen yang memiliki satu pun data kosong, ketidakkonsistenan, ambiguitas, atau kekurangan informasi yang dapat menghambat implementasi teknis.

---

## Dokumen Utama yang Divalidasi

- **Path**: `docs/sdlc/02_analysis/05_data_dictionary.md`
- **Versi Saat Ini**: v1.0
- **Target Versi Setelah Revisi**: v1.1

## Dokumen Referensi yang Harus Dibaca

Baca seluruh dokumen berikut **sebelum** mulai memvalidasi. Ini adalah sumber kebenaran primer yang menjadi dasar perbandingan:

| No | Dokumen Referensi | Path |
|---|---|---|
| 1 | Business Requirements Document (BRD) v1.1 | `docs/sdlc/02_analysis/01_business_requirements.md` |
| 2 | Software Requirements Specification (SRS) v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| 3 | Use Case Diagram v1.1 | `docs/sdlc/02_analysis/03_use_case_diagram.md` |
| 4 | Workflow Diagram v1.1 | `docs/sdlc/02_analysis/04_workflow_diagram.md` |
| 5 | Tech Stack Decision v1.1 | `docs/sdlc/01_planning/04_tech_stack_decision.md` |
| 6 | Innovation Proposal v1.1 | `docs/sdlc/01_planning/05_innovation_proposal.md` |
| 7 | Stakeholder Register v1.1 | `docs/sdlc/01_planning/03_stakeholder_register.md` |
| 8 | Feasibility Study v1.1 | `docs/sdlc/01_planning/02_feasibility_study.md` |
| 9 | Project Charter v1.1 | `docs/sdlc/01_planning/01_project_charter.md` |

---

## Checklist Implementasi (Low-Level Step-by-Step)

Ikuti seluruh checklist berikut **secara berurutan dari atas ke bawah**. Jangan melompati langkah. Tandai setiap tugas dengan `[x]` setelah selesai dikerjakan. Jika ada temuan masalah dalam satu langkah, catat temuan tersebut dan lanjutkan ke langkah berikutnya; perbaikan dilakukan pada **Langkah 10**.

---

### FASE 1 — PERSIAPAN: Pembacaan Seluruh Dokumen

- [ ] **1.1** Buka dan baca dokumen utama secara lengkap dari baris pertama hingga terakhir:
  - File: `docs/sdlc/02_analysis/05_data_dictionary.md`
  - Tujuan: Memahami struktur, isi, dan konteks keseluruhan dokumen sebelum melakukan perbandingan.

- [ ] **1.2** Buka dan baca dokumen referensi **BRD v1.1** secara lengkap:
  - File: `docs/sdlc/02_analysis/01_business_requirements.md`
  - Fokus pada: Bab 5 (Persyaratan Fungsional), Bab 7 (Domain Nilai & Aturan Bisnis), Bab 9 (Konfigurasi Parameter), Bab 12 (Keamanan & Risiko).
  - Catat: Setiap entitas, atribut, domain nilai, dan aturan bisnis yang disebutkan.

- [ ] **1.3** Buka dan baca dokumen referensi **SRS v1.1** secara lengkap:
  - File: `docs/sdlc/02_analysis/02_software_requirements.md`
  - Fokus pada: Bab 2.3 (Role/Aktor), Bab 3 (Kebutuhan Fungsional), Bab 6 (Entitas Data / Model Konseptual), Bab 10 (Batasan Teknis & Performa).
  - Catat: Setiap entitas database yang disebutkan, atributnya, dan SRS-ID terkait (misal: SRS-F-001).

- [ ] **1.4** Buka dan baca dokumen referensi **Use Case Diagram v1.1**:
  - File: `docs/sdlc/02_analysis/03_use_case_diagram.md`
  - Fokus pada: Setiap use case yang melibatkan operasi data (CREATE, READ, UPDATE, DELETE). Catat jika ada entitas atau atribut yang disebutkan di use case tetapi tidak ada di Data Dictionary.

- [ ] **1.5** Buka dan baca dokumen referensi **Workflow Diagram v1.1**:
  - File: `docs/sdlc/02_analysis/04_workflow_diagram.md`
  - Fokus pada: Alur perpindahan status (misal: status antrian, status pembayaran), alur kas masuk/keluar, dan alur pergantian shift. Catat apakah seluruh perubahan status tersebut tercermin di domain nilai Data Dictionary.

- [ ] **1.6** Buka dan baca dokumen referensi **Tech Stack Decision v1.1**:
  - File: `docs/sdlc/01_planning/04_tech_stack_decision.md`
  - Fokus pada: Engine database yang dipilih (MySQL versi berapa), batasan teknis storage engine (InnoDB), library Python yang digunakan, dan implikasinya pada tipe data atau constraint kolom.

- [ ] **1.7** Buka dan baca dokumen referensi **Stakeholder Register v1.1**:
  - File: `docs/sdlc/01_planning/03_stakeholder_register.md`
  - Fokus pada: Daftar peran aktor internal (8 role staf). Bandingkan dengan domain nilai `role` pada tabel `pengguna` di Data Dictionary.

- [ ] **1.8** Buka dan baca dokumen referensi **Feasibility Study v1.1**:
  - File: `docs/sdlc/01_planning/02_feasibility_study.md`
  - Fokus pada: Parameter ekonomi default (UMR, laba target, batas kasbon, dll). Bandingkan dengan nilai default pada tabel `system_configs` di Data Dictionary.

- [ ] **1.9** Buka dan baca dokumen referensi **Innovation Proposal v1.1** dan **Project Charter v1.1**:
  - File: `docs/sdlc/01_planning/05_innovation_proposal.md` dan `docs/sdlc/01_planning/01_project_charter.md`
  - Fokus pada: Ruang lingkup 10 modul sistem, fitur inovatif yang dijanjikan, dan apakah ada entitas data pendukung fitur inovatif yang belum ada di Data Dictionary.

---

### FASE 2 — VALIDASI KELENGKAPAN: Komparasi Mendalam Dokumen vs Referensi

> **Instruksi Umum Fase 2**: Untuk setiap sub-langkah di bawah, lakukan perbandingan baris per baris antara isi dokumen utama dengan dokumen referensi. Jika menemukan ketidaksesuaian, item yang terlewat, atau data yang tidak akurat, **catat temuan** tersebut dengan format berikut:
>
> `[TEMUAN-XX] | Lokasi: <bab/tabel/baris> | Masalah: <deskripsi masalah> | Rekomendasi: <solusi yang diusulkan>`

- [ ] **2.1** **Validasi Kelengkapan Daftar Tabel (Bab 2.1)**:
  - Periksa: Apakah seluruh 28 tabel yang terdaftar di Daftar Master Entitas (Bab 2.1) benar-benar memiliki spesifikasi detail di Bab 3?
  - Cara: Bandingkan nomor tabel di Bab 2.1 dengan sub-bab di Bab 3 (3.1 s/d 3.28). Pastikan tidak ada tabel yang terdaftar di Bab 2.1 namun tidak memiliki spesifikasi di Bab 3 atau sebaliknya.
  - Periksa juga: Apakah kolom `Jumlah Kolom` di Bab 2.1 akurat? Hitung manual jumlah kolom di setiap tabel Bab 3 dan bandingkan. Ingat, `created_at` dan `updated_at` adalah kolom yang termasuk dalam hitungan.

- [ ] **2.2** **Validasi Kelengkapan Entitas dari SRS**:
  - Baca kembali SRS v1.1 Bab 3 dan Bab 6. Buat daftar **semua entitas database** yang disebutkan di SRS (baik eksplisit maupun implisit dari narasi fungsional).
  - Periksa: Apakah setiap entitas dari SRS sudah ada tabelnya di Data Dictionary?
  - Periksa: Apakah ada kebutuhan fungsional di SRS (misal: SRS-F-XXX) yang membutuhkan entitas data tetapi entitasnya tidak ada di Data Dictionary?
  - Catat semua entitas yang ada di SRS tapi tidak ada di Data Dictionary sebagai TEMUAN.

- [ ] **2.3** **Validasi Kelengkapan Atribut Tiap Tabel vs SRS/BRD**:
  - Untuk setiap 28 tabel, periksa apakah atribut/kolom yang terdefinisi sudah menangkap **seluruh data yang dibutuhkan** oleh fungsionalitas SRS terkait.
  - Khususnya periksa tabel-tabel berikut dengan seksama karena memiliki banyak atribut bisnis:
    - `transaksi`: Apakah ada atribut metode pembayaran (`metode_pembayaran`) yang harusnya tercatat di level header transaksi? Periksa SRS-F-001.
    - `pengguna`: Apakah atribut `nama_lengkap` atau `no_telp` karyawan dibutuhkan oleh payroll atau audit? Periksa SRS-F-030.
    - `payroll`: Apakah ada atribut `metode_bayar_gaji` (transfer/tunai) yang dibutuhkan? Periksa SRS-F-019.
    - `utang_supplier`: Apakah ada atribut `tanggal_jatuh_tempo` dan `tanggal_pelunasan` yang dibutuhkan oleh alur workflow? Periksa SRS-F-040.
    - `kasbon`: Apakah ada atribut `cicilan_per_bulan` yang perlu didefinisikan? Periksa SRS-F-021.
    - `shift_handover`: Periksa apakah seluruh 12 kolom yang diklaim ada sudah terdefinisi lengkap di Bab 3.19.
    - `poin_insentif`: Periksa apakah seluruh 9 kolom yang diklaim ada sudah terdefinisi lengkap di Bab 3.18.
  - Catat setiap atribut yang ditemukan di SRS/BRD tetapi tidak ada di tabel terkait di Data Dictionary.

- [ ] **2.4** **Validasi Domain Nilai (Bab 4) vs Referensi**:
  - Bandingkan setiap domain nilai di Bab 4 dengan dokumen SRS dan BRD yang menjadi sumbernya.
  - Periksa:
    - Apakah semua nilai yang valid sudah tercantum dan tidak ada yang terlewat?
    - Apakah ada nilai enum yang disebutkan di SRS/BRD tapi tidak ada di kamus domain Bab 4?
    - Apakah ada nilai domain yang tidak relevan atau sudah tidak berlaku?
  - Khususnya periksa:
    - **Domain Status Antrian Kerja (4.5)**: Nilai `status_opname` juga disebut di domain ini, namun tabel `stock_opname` memiliki logika status yang berbeda (DRAFT/Approved). Apakah perlu domain nilai terpisah untuk `status_opname`?
    - **Domain Metode Pembayaran (4.11)**: Domain ini disebutkan berlaku pada "form transaksi kasir" tetapi tidak ada kolom `metode_pembayaran` di tabel `transaksi`. Apakah kolom ini memang tidak perlu disimpan di database atau ada yang terlewat?
    - **Domain Tipe Pinjaman (4.15)**: Nilai tipe pinjaman di domain ini tidak ada kolom yang menyimpannya di tabel `pinjaman_bank` dan `pinjaman_kerabat`. Apakah ini redundan atau ada kolom yang terlewat?

- [ ] **2.5** **Validasi Matriks FK (Bab 5.1) vs Spesifikasi Tabel (Bab 3)**:
  - Buat checklist: Untuk setiap FK yang ada di spesifikasi tabel Bab 3, pastikan FK tersebut terdaftar di matriks Bab 5.1.
  - Buat checklist kebalikannya: Untuk setiap FK di matriks Bab 5.1, pastikan FK tersebut memang ada di spesifikasi tabel Bab 3.
  - Periksa khusus: Nilai total 58 FK di matriks — apakah sesuai dengan total FK aktual yang didefinisikan di Bab 3?
  - Periksa konsistensi: Apakah nama kolom FK di matriks Bab 5.1 persis sama dengan nama kolom di tabel Bab 3? (contoh: `kasir_id` vs `user_id` di `backup_logs` — apakah konsisten?)

- [ ] **2.6** **Validasi ERD Mermaid (Bab 2.2) vs Matriks FK (Bab 5.1)**:
  - Periksa: Apakah setiap relasi yang tergambar di diagram ERD Mermaid Bab 2.2 sudah tercermin di Matriks FK Bab 5.1?
  - Periksa: Apakah ada relasi di Matriks FK Bab 5.1 yang tidak tergambar di ERD Mermaid?
  - Periksa: Di ERD Bab 2.2, terdapat notasi `SHIFT-HANDOVER` (dengan tanda minus) dan `SHIFT_HANDOVER` (dengan underscore). Pastikan konsistensi nama entitas.
  - Periksa: Apakah kardinalitas relasi (One-to-One, One-to-Many, Many-to-Many) di ERD sesuai dengan tipe relasi di matriks FK?

- [ ] **2.7** **Validasi Aturan Bisnis (Bab 6) vs SRS/BRD**:
  - Periksa Bab 6.1 (Aturan Validasi Input): Apakah semua aturan validasi input yang disebutkan di SRS sudah tercantum di sini?
  - Periksa Bab 6.2 (Formula Komputasi): Bandingkan setiap formula dengan SRS/BRD. Periksa apakah formulanya akurat secara matematis.
    - Formula Smart Payroll: Apakah formula proporsional sudah sesuai dengan narasi bisnis di SRS? Apakah batas minimum UMR sudah dirumuskan dengan benar?
    - Formula Rekonsiliasi Kas: Apakah semua komponen kas sudah masuk dalam formula (Kas Awal, DP, Pelunasan, Ritel, Retur, Beban)?
  - Periksa Bab 6.3 (Constraint Database): Apakah batasan `failed_login_attempts` (maks 5) sudah sesuai dengan SRS? Apakah batasan `limit_kasbon_staf` (Rp 1.000.000 atau 30% UMR) sudah sesuai dengan BRD?
  - Periksa Bab 6.4 (Default Value): Bandingkan setiap nilai default dengan Feasibility Study v1.1. Apakah angka-angka ini akurat dan sesuai konteks bisnis?

- [ ] **2.8** **Validasi Matriks Traceability (Bab 8) vs Referensi**:
  - Periksa Bab 8.1: Apakah pemetaan setiap tabel ke modul (M.1 s/d M.10) sudah akurat? Misalnya: tabel `pengeluaran` hanya dipetakan ke M.2 dan M.6 — apakah ada modul lain yang seharusnya terpetakan?
  - Periksa Bab 8.2: Apakah setiap pasangan referensi BRD ID dan SRS ID sudah akurat? Verifikasi dengan membaca langsung dokumen BRD dan SRS.
  - Periksa: Apakah ada entitas di tabel yang tidak memiliki referensi BRD/SRS yang valid (ID tidak ditemukan di dokumen aslinya)?

- [ ] **2.9** **Validasi Glosarium (Bab 9) vs Isi Dokumen**:
  - Periksa: Apakah semua istilah teknis yang digunakan di dalam dokumen sudah terdefinisi di Bab 9?
  - Periksa: Apakah ada istilah di Bab 9 yang tidak muncul di bagian manapun dalam dokumen (istilah orphan)?
  - Identifikasi istilah teknis penting yang muncul di dokumen namun belum ada di Bab 9 (misalnya: `PPOB`, `UMR`, `DP`, `HPP`, `UoM`, `AES-256`, `bcrypt`, `Smart Payroll`, `RBAC`, dll.) dan rekomendasikan penambahan.

- [ ] **2.10** **Validasi Referensi Dokumen (Bab 10) vs File Aktual**:
  - Periksa: Apakah semua 9 path file referensi yang tercantum di Bab 10 benar-benar ada di filesystem proyek?
  - Cara memeriksa: Baca daftar di Bab 10 dan verifikasi setiap path file satu per satu.
  - Periksa: Apakah ada dokumen referensi yang digunakan sebagai acuan dalam dokumen tetapi tidak tercantum di Bab 10?

---

### FASE 3 — VALIDASI RELEVANSI: Cek Fokus & Ruang Lingkup Dokumen

- [ ] **3.1** **Cek Data/Informasi yang Tidak Relevan**:
  - Periksa setiap bagian dokumen. Apakah ada data, keterangan, atau sub-bab yang **bukan merupakan bagian dari cakupan Data Dictionary**?
  - Data Dictionary yang baik hanya berisi: definisi tabel, definisi kolom (nama, tipe, constraint, domain nilai, deskripsi), relasi antar tabel, aturan bisnis data, dan traceability. Data Dictionary **bukan** tempat untuk mendokumentasikan arsitektur sistem, alur proses bisnis secara naratif, atau wireframe tampilan CLI.
  - Jika ada konten yang tidak relevan, catat sebagai TEMUAN dan rekomendasikan dipindahkan ke dokumen yang tepat atau dihapus.

- [ ] **3.2** **Cek Duplikasi Informasi**:
  - Periksa apakah ada informasi yang diulang (duplikat) antara Bab 2, Bab 3, Bab 4, Bab 5, dan Bab 6 tanpa memberikan nilai tambah.
  - Contoh yang perlu dicek: Bab 5.2 hanya merujuk ke Bab 2.2 — apakah ini cukup atau perlu dihapus salah satunya?
  - Catat duplikasi yang merugikan keringkasan dokumen sebagai TEMUAN.

- [ ] **3.3** **Cek Kelengkapan Informasi Spesifik Data Dictionary**:
  - Periksa apakah ada elemen standar sebuah Data Dictionary profesional yang **belum ada** di dokumen ini, yaitu:
    - [ ] Apakah ada **Composite Unique Constraint** yang perlu didefinisikan secara eksplisit? (Misalnya: `absensi(pengguna_id, tanggal)` harusnya UNIQUE composite — sudah ada di indeks Bab 7.3, tapi apakah sudah didefinisikan sebagai constraint di spesifikasi tabel Bab 3.10?)
    - [ ] Apakah ada **CHECK Constraint** MySQL yang perlu didefinisikan? (Misalnya: `gaji_bersih >= 0`, `stok_saat_ini >= -batas_tertentu`, `failed_login_attempts BETWEEN 0 AND 5`)
    - [ ] Apakah **Composite Index** pada Bab 7.3 sudah cukup atau ada index tambahan yang dibutuhkan berdasarkan pola query di SRS?
    - [ ] Apakah ada **View** atau **Stored Procedure** yang direncanakan? (Jika ada di SRS, dokumentasikan sebagai catatan di Data Dictionary)
    - [ ] Apakah **seed data awal** (data contoh/dummy) untuk tabel `system_configs` dan `cabang` sudah tertuang atau setidaknya direferensikan?

---

### FASE 4 — VALIDASI STANDAR STRUKTUR DOKUMEN

- [ ] **4.1** **Cek Kelengkapan Header Dokumen**:
  - Periksa metadata header (`dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`): Apakah semua field terisi dengan nilai yang benar?
  - Periksa Riwayat Perubahan (Bab 1 bagian paling atas): Apakah tabel riwayat sudah ada dan terisi lengkap?

- [ ] **4.2** **Cek Konsistensi Struktur Bab**:
  - Periksa apakah setiap spesifikasi tabel di Bab 3 memiliki struktur yang konsisten:
    - [ ] Tabel metadata tabel (Nama Tabel, Deskripsi, Modul Terkait, Derivasi SRS, Derivasi BRD, Engine, Charset, Collation).
    - [ ] Heading `#### Tabel Detail Atribut/Kolom`.
    - [ ] Tabel kolom dengan header: `No | Nama Kolom | Tipe Data MySQL | Constraint | Null? | Default | Deskripsi Bisnis | Domain Nilai`.
    - [ ] Catatan Implementasi (jika relevan).
  - Catat tabel mana saja yang strukturnya tidak konsisten (misal: ada yang menggunakan `| Atribut | Nilai |` dan ada yang menggunakan `| Atribut Tabel | Nilai |`).

- [ ] **4.3** **Cek Nomor Urut Kolom**:
  - Periksa setiap tabel di Bab 3. Apakah nomor urut kolom (kolom `No`) sudah berurutan dengan benar dari 1 hingga n?
  - Catat tabel mana saja yang memiliki kesalahan penomoran.

- [ ] **4.4** **Cek Konvensi Penamaan (Bab 1.6)**:
  - Periksa: Apakah semua nama tabel menggunakan `snake_case` singular?
  - Periksa: Apakah semua nama kolom menggunakan `snake_case`?
  - Periksa: Apakah semua FK mengikuti pola `[nama_tabel_referensi]_id`? (Contoh: di `backup_logs`, kolom FK ke `pengguna` menggunakan `user_id` — apakah ini seharusnya `pengguna_id` agar konsisten dengan tabel lain?)
  - Periksa: Apakah ada inkonsistensi simbol constraint? (PK, FK, UQ, NN, AI)

- [ ] **4.5** **Cek Kelengkapan Bab Wajib Dokumen Data Dictionary**:
  - Periksa apakah dokumen memiliki minimal bab-bab berikut yang wajib ada dalam Data Dictionary standar industri:
    - [ ] Informasi Dokumen (Tujuan, Cakupan, Posisi SDLC, Audiens, Konvensi) ✓
    - [ ] Ringkasan Model Data (Daftar Entitas, ERD, Statistik) ✓
    - [ ] Spesifikasi Entitas & Atribut Detail ✓
    - [ ] Kamus Domain Nilai ✓
    - [ ] Matriks Relasi FK & Constraint Integritas ✓
    - [ ] Aturan Bisnis Data ✓
    - [ ] Indeks & Optimasi ✓
    - [ ] Matriks Traceability ✓
    - [ ] Glosarium ✓
    - [ ] Referensi Dokumen ✓
    - [ ] **Apakah ada bab yang masih diperlukan tetapi belum ada?** (Misalnya: Rencana Migrasi Data Awal / Seed Data, atau Kebijakan Retensi Data)

---

### FASE 5 — VALIDASI KELAYAKAN SEBAGAI INPUT FASE 03 DESIGN

- [ ] **5.1** **Cek Kelengkapan Informasi untuk Penulisan `schema.sql`**:
  - Simulasikan: Bayangkan kamu seorang junior programmer yang hanya punya dokumen ini dan harus menulis DDL `schema.sql`. Apakah semua informasi yang dibutuhkan sudah tersedia tanpa harus menebak atau membaca dokumen lain?
  - Periksa untuk setiap tabel:
    - [ ] Apakah nama tabel jelas?
    - [ ] Apakah tipe data setiap kolom sudah ditentukan secara spesifik? (Tidak ada yang hanya ditulis "INT" tanpa konteks UNSIGNED atau signed)
    - [ ] Apakah constraint setiap kolom sudah lengkap (PK, FK, UQ, NN, AI, DEFAULT)?
    - [ ] Apakah nilai DEFAULT sudah ditentukan untuk setiap kolom yang memiliki default?
    - [ ] Apakah perilaku ON DELETE dan ON UPDATE setiap FK sudah terdefinisi di Matriks FK Bab 5.1?
    - [ ] Apakah Engine, Charset, dan Collation sudah didefinisikan per tabel?
    - [ ] Apakah Composite Unique Constraint (misal pada `absensi`) sudah terdefinisi secara eksplisit?

- [ ] **5.2** **Cek Kelengkapan Informasi untuk Penulisan `seed.sql`**:
  - Periksa: Apakah ada data seed (data awal/dummy) minimal yang perlu didefinisikan agar sistem bisa langsung berjalan?
  - Data seed minimal yang wajib ada:
    - Minimal 1 baris di tabel `cabang` (cabang default).
    - Minimal 1 baris di tabel `pengguna` (akun pemilik/admin pertama).
    - Baris-baris default di tabel `system_configs` (seluruh 9 parameter yang tercantum di Bab 6.4).
    - Baris-baris default di tabel `saldo_ppob` (2 tipe PPOB).
    - Baris-baris default di tabel `saldo_ewallet` (6 akun e-wallet).
  - Periksa: Apakah nilai seed data untuk `cabang` (Bab 3.1 Catatan Implementasi) sudah lengkap (id, nama, alamat, telp)?
  - Periksa: Apakah nilai default `system_configs` di Bab 6.4 sudah mencakup **seluruh** parameter yang diperlukan oleh 10 modul sistem?

- [ ] **5.3** **Cek Potensi Pertanyaan yang Akan Mengganggu Proses Fase 03**:
  - Simulasikan: Bayangkan seorang programmer sedang membuat `schema.sql` berdasarkan dokumen ini dan menemukan kebingungan. Apakah ada hal-hal berikut yang masih tidak jelas?
    - [ ] Apakah urutan pembuatan tabel (tabel parent sebelum child) bisa dipahami dari ERD?
    - [ ] Apakah ada circular dependency antara tabel yang bisa menyebabkan masalah saat eksekusi DDL?
    - [ ] Apakah kolom `metode_pembayaran` pada transaksi akan memengaruhi rekonsiliasi kas di `shift_handover`? Apakah relasinya sudah jelas?
    - [ ] Bagaimana cara membedakan `barang` bertipe `Retail_ATK` vs `Bahan_Baku` secara programatik — apakah sudah cukup jelas hanya dengan `tipe_barang`?

---

### FASE 6 — VALIDASI KUALITAS BAHASA INDONESIA

- [ ] **6.1** **Cek Kejelasan Deskripsi Bisnis Kolom**:
  - Baca ulang kolom `Deskripsi Bisnis` di setiap tabel Bab 3. Apakah deskripsi sudah:
    - [ ] Menjelaskan **fungsi bisnis** kolom tersebut (bukan hanya nama teknis)?
    - [ ] Tidak ambigu (tidak menimbulkan tafsiran ganda)?
    - [ ] Menggunakan bahasa Indonesia yang natural dan baku?
    - [ ] Cukup informatif sehingga junior programmer atau AI model bisa memahami konteks penggunaan kolom tersebut?
  - Tandai kolom yang deskripsinya masih terlalu teknis, terlalu singkat, atau ambigu.

- [ ] **6.2** **Cek Konsistensi Terminologi**:
  - Periksa apakah istilah yang sama selalu merujuk ke konsep yang sama di seluruh dokumen:
    - "kasir" vs "staf kasir" vs "pengguna kasir" — apakah konsisten?
    - "bahan baku" vs "komponen bahan" vs "material" — apakah konsisten?
    - "nota" vs "transaksi" vs "invoice" — apakah konteks penggunaannya jelas dan tidak membingungkan?
    - "opname" vs "stock opname" vs "rekonsiliasi stok" — apakah konsisten?
  - Catat inkonsistensi terminologi sebagai TEMUAN.

- [ ] **6.3** **Cek Catatan Implementasi**:
  - Baca setiap Catatan Implementasi di Bab 3. Apakah:
    - [ ] Catatannya relevan dan spesifik untuk tabel tersebut?
    - [ ] Bahasanya jelas dan actionable untuk developer?
    - [ ] Tidak bertentangan dengan informasi di SRS atau BRD?

- [ ] **6.4** **Cek Deskripsi Bab Pembuka**:
  - Baca Bab 1 (Informasi Dokumen). Apakah:
    - [ ] Tujuan dokumen sudah jelas dan spesifik?
    - [ ] Cakupan dokumen sudah akurat (28 tabel, 18 domain nilai, 103 FK — apakah angka ini akurat?)?
    - [ ] Posisi dokumen dalam SDLC sudah benar dan informatif?
    - [ ] Daftar audiens target sudah lengkap dan relevan?

---

### FASE 7 — VALIDASI DATA KOSONG & PLACEHOLDER

- [ ] **7.1** **Cek Kolom Default Kosong atau Tidak Tersedia**:
  - Periksa setiap baris di kolom `Default` pada tabel spesifikasi Bab 3. Apakah ada yang:
    - Bernilai `-` (tanda strip) pada kolom yang seharusnya memiliki default value?
    - Bernilai kosong, `N/A`, atau `TBD`?
    - Tidak konsisten dengan constraint `NN` (misalnya: kolom `NOT NULL` tetapi defaultnya `-` dan tidak ada keterangan bagaimana nilai awalnya diisi)?
  - Isi semua default value yang kosong dengan nilai yang sesuai dan relevan secara bisnis.

- [ ] **7.2** **Cek Domain Nilai Kosong**:
  - Periksa kolom `Domain Nilai` di setiap tabel spesifikasi Bab 3. Apakah ada kolom yang domain nilainya:
    - Hanya ditulis `Free text` tanpa memberikan contoh atau batasan lebih lanjut, padahal sebenarnya ada batasan bisnis?
    - Mereferensikan "Domain XYZ" yang tidak ada di Bab 4?
    - Bertentangan antara domain di Bab 3 dan definisi di Bab 4?
  - Lengkapi domain nilai yang kosong atau kurang informatif.

- [ ] **7.3** **Cek Referensi yang Hilang (Broken References)**:
  - Periksa setiap referensi ke ID SRS (SRS-F-XXX) dan BRD (BR-F-XX) di dokumen. Apakah semua ID referensi tersebut benar-benar ada di dokumen SRS dan BRD?
  - Caranya: Ambil setiap ID referensi, buka dokumen SRS/BRD, dan cari apakah ID tersebut ada.
  - Tandai ID yang tidak ditemukan sebagai broken reference dan perbaiki dengan ID yang benar atau tandai sebagai derivasi.

- [ ] **7.4** **Cek Data Spesifik Tabel yang Berpotensi Kosong**:
  - Periksa tabel-tabel berikut yang berisiko memiliki definisi tidak lengkap:
    - **`shift_handover` (Bab 3.19)**: Tabel ini diklaim memiliki 12 kolom. Hitung manual dan pastikan semua 12 kolom sudah terdefinisi lengkap dengan tipe data, constraint, default, dan deskripsi.
    - **`utang_supplier` (Bab 3.20)**: Tabel ini diklaim memiliki 8 kolom. Hitung manual dan pastikan semua 8 kolom sudah terdefinisi.
    - **`poin_insentif` (Bab 3.18)**: Tabel ini diklaim memiliki 9 kolom. Hitung manual dan pastikan semua 9 kolom sudah terdefinisi, termasuk kolom `status_poin` yang terdefinisi di domain nilai 4.13.
    - **`barang` (Bab 3.5)**: Tabel ini diklaim memiliki 11 kolom. Hitung manual. Perhatikan apakah kolom `harga_beli` (harga pengadaan dari supplier) perlu ada, karena SRS mungkin memerlukan ini untuk kalkulasi HPP.

---

### FASE 8 — VALIDASI TAMBAHAN SPESIFIK DATA DICTIONARY

> Fase ini berisi pemeriksaan yang tidak selalu disebutkan secara eksplisit di requirements tetapi merupakan standar best practice validasi dokumen Data Dictionary profesional.

- [ ] **8.1** **Cek Normalisasi Database (1NF, 2NF, 3NF)**:
  - Periksa setiap tabel apakah ada pelanggaran bentuk normal:
    - **1NF**: Apakah ada kolom yang menyimpan lebih dari satu nilai (kolom multi-nilai)? Misalnya kolom yang menyimpan "Gopay, Dana, OVO" dalam satu string.
    - **2NF**: Apakah ada kolom non-key yang hanya bergantung pada sebagian dari composite primary key?
    - **3NF**: Apakah ada kolom yang bergantung secara transitif pada kolom non-key? Misalnya: `gaji_bersih = gaji_pokok + bonus_insentif - potongan_kasbon` di tabel `payroll` — kolom `gaji_bersih` adalah kolom kalkulasi (derived attribute). Apakah ini perlu disimpan atau cukup dihitung di runtime?
  - Catat pelanggaran normalisasi sebagai TEMUAN dan berikan rekomendasi.

- [ ] **8.2** **Cek Konsistensi Tipe Data antar Kolom yang Saling Merujuk**:
  - Periksa: Apakah semua kolom FK bertipe `INT`? Apakah semua PK yang dirujuk bertipe `INT`? Tipe data FK dan PK yang dirujuk harus identik.
  - Periksa: Apakah semua kolom yang menyimpan nominal uang menggunakan `DECIMAL(15,4)`? Apakah ada yang menggunakan `FLOAT` atau `DOUBLE` yang rawan presisi floating-point?
  - Periksa: Apakah tipe `BOOLEAN` sudah konsisten penggunaannya? (Di MySQL, `BOOLEAN` adalah alias `TINYINT(1)`; pastikan deskripsinya sudah mencatat ini dan nilainya adalah `TRUE/FALSE` atau `1/0`).

- [ ] **8.3** **Cek Potensi Masalah Performa dan Skalabilitas**:
  - Periksa: Apakah tabel `audit_logs` (yang bisa tumbuh sangat besar) sudah memiliki strategi partisi atau kebijakan retensi data (purging)?
  - Periksa: Apakah tabel `detail_transaksi` yang merupakan tabel paling sering ditulis sudah memiliki indeks yang optimal?
  - Periksa: Apakah kolom `path_desain` di `antrian_kerja` bertipe `VARCHAR(255)` — apakah panjang 255 karakter cukup untuk path file di sistem operasi Windows yang bisa mencapai 260 karakter? Apakah perlu `TEXT`?

- [ ] **8.4** **Cek Konsistensi Kebijakan `updated_at` di Tabel Audit-Sensitif**:
  - Tabel `audit_logs` adalah tabel log yang seharusnya **immutable** (tidak boleh diubah setelah INSERT). Apakah memiliki kolom `updated_at` merupakan desain yang tepat untuk tabel log audit?
  - Tabel `backup_logs` juga merupakan log yang immutable. Apakah kolom `updated_at` perlu ada?
  - Berikan rekomendasi apakah kolom `updated_at` perlu dihapus dari tabel log, atau justru perlu dipertahankan dengan keterangan yang jelas.

- [ ] **8.5** **Cek Kelengkapan Keterangan Derivasi Tabel**:
  - Terdapat 7 tabel derivasi yang ditandai dengan notasi `⚠️ [DERIVASI]`. Periksa apakah keterangan derivasi sudah menjelaskan **mengapa** tabel ini perlu diturunkan, bukan hanya menyatakan bahwa tabelnya merupakan derivasi.
  - Periksa apakah 21 tabel SRS-langsung sudah memiliki referensi SRS-ID yang valid dan spesifik.

- [ ] **8.6** **Cek Completeness Statistik (Bab 2.3)**:
  - Klaim di Bab 2.3:
    - Total tabel: 28
    - Total kolom/atribut: 234
    - Persentase Multi-Cabang Ready: 100%
    - Persentase Audit Trail Ready: 100%
  - Verifikasi: Hitung total kolom aktual dari seluruh 28 tabel di Bab 3 dan bandingkan dengan klaim 234.
  - Verifikasi: Apakah benar 100% tabel memiliki `cabang_id`? Apakah benar 100% tabel memiliki `created_at` dan `updated_at`?

---

### FASE 9 — KOMPILASI TEMUAN & PERSIAPAN DOKUMEN FINAL

- [ ] **9.1** **Kompilasi Seluruh Temuan**:
  - Kumpulkan semua catatan TEMUAN dari Fase 2 hingga Fase 8.
  - Kelompokkan temuan berdasarkan kategori:
    - **KRITIS** (harus diperbaiki, bisa menyebabkan DDL salah atau sistem error): Kolom hilang, tipe data salah, FK missing, default value kosong pada kolom NN.
    - **PENTING** (harus diperbaiki, tapi tidak langsung crash): Inkonsistensi nama kolom, domain nilai tidak lengkap, referensi ID salah.
    - **MINOR** (disarankan diperbaiki demi kualitas dokumen): Deskripsi kurang informatif, inkonsistensi terminologi, istilah belum ada di glosarium.

- [ ] **9.2** **Susun Rencana Perbaikan**:
  - Untuk setiap TEMUAN KRITIS dan PENTING, tentukan:
    - Apa yang harus ditambah/diubah/dihapus.
    - Di baris/bagian mana di dokumen perubahan dilakukan.
    - Nilai yang tepat untuk mengisi data kosong atau memperbaiki data yang salah.

---

### FASE 10 — PENULISAN ULANG DOKUMEN FINAL (OVERWRITE)

- [ ] **10.1** **Tulis Ulang Seluruh Dokumen ke Target File**:
  - Berdasarkan seluruh temuan dan rencana perbaikan dari Fase 9, tulis ulang **seluruh dokumen** dari baris pertama hingga baris terakhir.
  - **Target file**: `docs/sdlc/02_analysis/05_data_dictionary.md`
  - **MUTLAK**: Seluruh teks dari baris pertama hingga terakhir **harus ditulis ulang sepenuhnya**. Tidak ada satu pun bagian yang boleh dipotong, diringkas, atau dihilangkan. No truncation. No ellipsis. No `...dst`.
  - **MUTLAK**: Dokumen yang ditulis ulang harus lebih panjang atau minimal sama panjangnya dengan dokumen asli, karena proses validasi ini sifatnya memperbaiki dan melengkapi, bukan memotong.

- [ ] **10.2** **Update Versi Dokumen**:
  - Ubah nilai `versi` di header dokumen dari `1.0` menjadi `1.1`.
  - Tambahkan baris baru di tabel **Riwayat Perubahan Dokumen** dengan format:
    ```
    | 1.1 | [tanggal-hari-ini] | [ringkasan perubahan yang dilakukan berdasarkan temuan validasi] | Senior Database Architect & Data Modeling Specialist |
    ```

- [ ] **10.3** **Validasi Hasil Penulisan Ulang**:
  - Setelah file berhasil ditulis ulang, buka kembali file tersebut dan verifikasi:
    - [ ] Versi sudah berubah menjadi `1.1`.
    - [ ] Tabel Riwayat Perubahan sudah ada entri baru untuk v1.1.
    - [ ] Seluruh bab dari Bab 1 hingga Bab 10 masih ada dan tidak ada yang terpotong.
    - [ ] Semua temuan KRITIS dan PENTING sudah diperbaiki dalam dokumen baru.
    - [ ] Tidak ada teks `...`, `dst.`, `[lanjutan]`, atau indikasi truncation apapun.
    - [ ] Jika ada referensi dokumen baru yang ditambahkan dalam proses perbaikan, pastikan sudah tercantum di bagian akhir Bab 10.

- [ ] **10.4** **Tambahkan Referensi Baru (Jika Ada)**:
  - Jika dalam proses validasi ditemukan bahwa ada dokumen referensi tambahan yang digunakan sebagai acuan perbaikan (di luar 9 dokumen yang sudah terdaftar), tambahkan referensi tersebut di **bagian paling bawah Bab 10** setelah entri terakhir yang ada, mengikuti format penomoran yang sudah ada.

---

## Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **selesai** jika dan hanya jika seluruh kondisi berikut terpenuhi:

1. ✅ Seluruh checklist dari Fase 1 hingga Fase 10 sudah ditandai `[x]`.
2. ✅ File `docs/sdlc/02_analysis/05_data_dictionary.md` sudah diperbarui dengan versi `1.1`.
3. ✅ Tidak ada data kosong, placeholder, atau `TBD` yang tertinggal di seluruh dokumen.
4. ✅ Tidak ada inkonsistensi antara Bab 2 (Daftar Tabel), Bab 3 (Spesifikasi Detail), Bab 4 (Domain Nilai), Bab 5 (Matriks FK), Bab 6 (Aturan Bisnis), dan Bab 8 (Traceability).
5. ✅ Seluruh teks dokumen ditulis ulang lengkap dari baris pertama hingga terakhir tanpa ada yang dipotong atau dihilangkan.
6. ✅ Dokumen telah diverifikasi layak digunakan sebagai satu-satunya referensi teknis untuk menulis `schema.sql` dan `seed.sql` pada Fase 03 Design.

---

## Catatan Penting untuk Implementer

> **PERINGATAN**: Jangan melakukan perubahan parsial atau incremental pada dokumen. Proses penulisan ulang harus dilakukan sekaligus (atomic overwrite) untuk menghindari dokumen setengah jadi yang tidak konsisten.
>
> **PERINGATAN**: Jika kapasitas konteks (context window) tidak cukup untuk menulis ulang seluruh dokumen dalam satu kali operasi, bagi dokumen menjadi segmen-segmen logis (misalnya: Bab 1-3 dulu, lalu Bab 4-6, lalu Bab 7-10), tulis masing-masing segmen ke file sementara, lalu gabungkan semuanya ke `05_data_dictionary.md` dalam satu operasi overwrite terakhir.
>
> **PERINGATAN**: Jangan pernah menggunakan karakter ellipsis (`...`) atau frasa seperti "dst.", "dan seterusnya", "[isi selanjutnya sama]", atau sejenisnya di dalam dokumen output. Semua teks harus eksplisit dan lengkap.
>
> **PERINGATAN**: Seluruh isi dari baris pertama sampai baris terakhir dokumen yang sudah ada sebelumnya harus dipertahankan dan disempurnakan. Tidak ada bab, sub-bab, tabel, atau paragraf yang boleh dihapus tanpa alasan yang sangat kuat dan terdokumentasi sebagai TEMUAN.
