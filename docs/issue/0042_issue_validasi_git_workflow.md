---
judul     : Validasi, Analisis, dan Penyempurnaan Dokumen Git Workflow
target    : docs/sdlc/04_implementation/04_git_workflow.md
referensi : docs/sdlc/
dibuat    : 2026-05-26
status    : Open
prioritas : Tinggi
assignee  : Junior Programmer / LLM Pelaksana
---

# Validasi, Analisis, dan Penyempurnaan Dokumen Git Workflow

## Latar Belakang

Dokumen `docs/sdlc/04_implementation/04_git_workflow.md` (versi 1.0) adalah deliverable keempat
Fase 04 — Implementation dalam siklus SDLC proyek AbuCom. Dokumen ini menjadi **acuan operasional
wajib** bagi seluruh tim campuran (Junior Programmer + 6 Model AI) dalam mengelola version control
Git secara lokal offline LAN.

Sebelum dokumen ini digunakan sebagai **input utama** untuk proses konstruksi kode aktual (M.1
hingga M.10), dokumen wajib divalidasi secara ketat agar:

1. Tidak ada informasi penting dari file referensi yang terlewat.
2. Tidak ada informasi yang tidak relevan atau off-scope yang mengotori dokumen.
3. Struktur dan gaya bahasa memenuhi standar dokumen industri profesional.
4. Dokumen dapat berfungsi sebagai referensi mandiri tanpa ambiguitas bagi LLM model kecil
   atau junior programmer sekalipun.

---

## Persona Validator

> **INSTRUKSI PERTAMA — WAJIB DIBACA DAN DIINTERNALISASI SEBELUM MELAKUKAN TINDAKAN APA PUN.**

Sebelum memulai seluruh proses di bawah ini, Anda **WAJIB** mengadopsi secara penuh persona
berikut sebagai identitas kerja Anda sepanjang pelaksanaan issue ini:

```
PERSONA: Principal DevOps Engineer & Technical Documentation Architect
SPESIALISASI:
  - Git workflow enterprise (GitFlow, Trunk-Based, Feature Branching)
  - SDLC documentation standards (IEEE 829, ISO/IEC 12207)
  - Offline/LAN-only version control systems
  - Mixed-team collaboration (human + AI agent pipelines)
  - Python project toolchain (PEP 8, PEP 257, Conventional Commits)
  - Security-aware Git practices (credential hygiene, audit trails)
OTORITAS:
  - Validator dokumen teknis dengan standar kualitas "production-ready"
  - Penilai kelengkapan, konsistensi, dan relevansi konten
  - Penjamin kejelasan bahasa untuk target pembaca LLM murah + junior programmer
SIKAP:
  - Sangat teliti dan tidak kompromi terhadap ketidaklengkapan
  - Berorientasi pada kejelasan instruksional (zero ambiguity)
  - Skeptis terhadap klaim "sudah lengkap" tanpa bukti konkret
```

Anda bertindak **bukan sebagai pelaksana kreatif**, melainkan sebagai **auditor teknis yang ketat**
terhadap kualitas dokumen. Seluruh penilaian Anda harus berbasis bukti: kutip baris spesifik dari
dokumen dan referensi untuk mendukung temuan Anda.

---

## Pra-Syarat Sebelum Memulai

Sebelum memulai pekerjaan apa pun, pastikan semua kondisi berikut terpenuhi:

- [ ] **PRA-01** — Konfirmasi Anda memiliki akses baca ke file target:
      `docs/sdlc/04_implementation/04_git_workflow.md`
- [ ] **PRA-02** — Konfirmasi Anda memiliki akses baca ke seluruh 7 file referensi yang
      tercantum di Bab 16 dokumen target (lihat daftar di bawah).
- [ ] **PRA-03** — Konfirmasi Anda memiliki akses tulis (overwrite) ke file target.
- [ ] **PRA-04** — Baca dan pahami seluruh instruksi issue ini dari baris pertama hingga
      terakhir **sebelum** mulai membaca dokumen target.

**Daftar 7 file referensi (wajib dibaca semua):**

| Kode Ref | Path File Referensi |
|:---:|:---|
| R-01 | `docs/sdlc/04_implementation/01_coding_standard.md` |
| R-02 | `docs/sdlc/04_implementation/02_environment_setup.md` |
| R-03 | `docs/sdlc/04_implementation/03_module_structure.md` |
| R-04 | `docs/sdlc/01_planning/04_tech_stack_decision.md` |
| R-05 | `docs/sdlc/03_design/03_system_architecture.md` |
| R-06 | `docs/sdlc/03_design/06_security_design.md` |
| R-07 | `docs/sdlc/narasi.txt` |

---

## Tahapan Pelaksanaan (Step-by-Step — Low Level)

Ikuti **setiap tahap** secara berurutan. Jangan melompat atau menggabungkan tahap. Tandai `[x]`
pada setiap checkbox segera setelah langkah tersebut selesai dieksekusi sepenuhnya.

---

### TAHAP 1 — Pembacaan dan Pemahaman Dokumen Target

- [ ] **T1-01** — Buka dan baca file `docs/sdlc/04_implementation/04_git_workflow.md` dari
      baris pertama hingga baris terakhir tanpa melewati satu baris pun. Catat jumlah total
      baris dan jumlah bab/sub-bab yang ditemukan.
- [ ] **T1-02** — Identifikasi dan catat daftar lengkap seluruh bab (##) dan sub-bab (###)
      yang ada dalam dokumen target. Periksa apakah penomoran bab berurutan dan konsisten
      (tidak ada nomor yang terlewat atau duplikat).
- [ ] **T1-03** — Identifikasi seluruh data yang ditandai `[DATA KOSONG — PERLU DIISI MANUAL]`
      atau `[HARUS DIISI MANUAL]` atau `⚠️` di dalam dokumen target. Buat daftar lengkap
      lokasi (nomor bab/sub-bab) dari setiap penanda tersebut.
- [ ] **T1-04** — Identifikasi seluruh tabel, diagram Mermaid, blok kode bash/cmd, dan
      checklist yang ada di dalam dokumen. Catat lokasinya (nomor bab/sub-bab).

---

### TAHAP 2 — Pembacaan Seluruh File Referensi

- [ ] **T2-01** — Buka dan baca file **R-01** (`01_coding_standard.md`) secara lengkap.
      Fokus khusus pada:
      - Bab 15 (Version Control Git): ekstrak semua aturan, perintah, dan konfigurasi yang
        tercantum.
      - Bab 16 (Larangan Mutlak): ekstrak semua larangan Git yang terdaftar.
      - Bab 17 (Checklist Kepatuhan): ekstrak seluruh item checklist.
      - Standardisasi `decimal.Decimal` dan `ROUND_HALF_UP` yang terkait scope commit.
      Catat semua temuan dalam memori kerja Anda.

- [ ] **T2-02** — Buka dan baca file **R-02** (`02_environment_setup.md`) secara lengkap.
      Fokus khusus pada:
      - Bab 9 (Setup Git lokal): ekstrak seluruh langkah konfigurasi Git, perintah eksak,
        dan nilai parameter yang disebutkan.
      - Bab 8.5 (Setup .gitignore): ekstrak daftar lengkap pola ignore yang direkomendasikan.
      - Seksi credentials setup dan `.env.example`.
      Catat semua temuan dalam memori kerja Anda.

- [ ] **T2-03** — Buka dan baca file **R-03** (`03_module_structure.md`) secara lengkap.
      Fokus khusus pada:
      - Bab 2.3 (10 modul fungsional): ekstrak seluruh nama modul dan kode modul (M.1 - M.10).
      - Bab 3.1 (ASCII direktori pohon proyek): ekstrak struktur direktori lengkap.
      - Bab 13 (Module-to-File mapping): ekstrak peta file per modul untuk scope commit.
      Catat semua temuan dalam memori kerja Anda.

- [ ] **T2-04** — Buka dan baca file **R-04** (`04_tech_stack_decision.md`) secara lengkap.
      Fokus khusus pada:
      - Spesifikasi platform runtime (Python versi eksak, OS dual-platform).
      - Daftar library dengan versi terkunci (*locked version*).
      - Profil 6 model AI pengembang dan spesialisasinya.
      Catat semua temuan dalam memori kerja Anda.

- [ ] **T2-05** — Buka dan baca file **R-05** (`03_system_architecture.md`) secara lengkap.
      Fokus khusus pada:
      - Diagram topologi LAN offline.
      - Konfigurasi isolation level database (repeatable read).
      - Connection pool `abupool` dan ukurannya.
      - Konfigurasi fisik server Debian (path, chmod, user).
      Catat semua temuan dalam memori kerja Anda.

- [ ] **T2-06** — Buka dan baca file **R-06** (`06_security_design.md`) secara lengkap.
      Fokus khusus pada:
      - Spesifikasi enkripsi backup (AES-256 ZIP).
      - Chmod 700 server dan kebijakan akses file.
      - Struktur format audit log JSON.
      - Penanganan UU PDP untuk data WhatsApp CRM.
      - Prosedur brute-force rate-limiting.
      - Sanitasi input CLI.
      Catat semua temuan dalam memori kerja Anda.

- [ ] **T2-07** — Buka dan baca file **R-07** (`narasi.txt`) secara lengkap.
      Fokus khusus pada:
      - Detail tim campuran: nama, kode peran, dan spesialisasi tiap model AI.
      - Konteks operasional toko (jam buka, alur kasir, skala bisnis).
      - Kebutuhan khusus kolaborasi offline LAN.
      Catat semua temuan dalam memori kerja Anda.

---

### TAHAP 3 — Analisis Komparasi: Kelengkapan Dokumen Target vs. Referensi

> **Tujuan**: Memastikan tidak ada data atau informasi penting dari referensi yang terlewat
> dalam dokumen target.

Untuk setiap poin di bawah, bandingkan isi dokumen target dengan isi referensi yang relevan.
Catat setiap **kesenjangan (gap)** sebagai temuan yang harus diperbaiki.

- [ ] **T3-01** — Komparasi R-01 Bab 15 vs. dokumen target:
      Periksa apakah **setiap** aturan version control Git yang disebutkan di R-01 Bab 15
      sudah tercermin di dokumen target. Jika ada aturan di R-01 yang hilang, catat sebagai
      **TEMUAN-GAP-01** beserta keterangan detail bab/baris di R-01 yang belum tercakup.

- [ ] **T3-02** — Komparasi R-01 Bab 16 (Larangan) vs. Bab 14 dokumen target:
      Periksa apakah seluruh larangan mutlak di R-01 sudah tertuang di Bab 14 dokumen target.
      Jika ada larangan di R-01 yang tidak tercantum di Bab 14, catat sebagai **TEMUAN-GAP-02**.

- [ ] **T3-03** — Komparasi R-01 Bab 17 (Checklist) vs. Bab 8.3 dan Bab 15 dokumen target:
      Periksa apakah seluruh 12 item checklist dari R-01 Bab 17 sudah tercermin lengkap di
      Bab 8.3 (Code Review Checklist) dan Bab 15 (Checklist Kepatuhan). Jika ada item yang
      kurang, catat sebagai **TEMUAN-GAP-03**.

- [ ] **T3-04** — Komparasi R-02 Bab 9 (Setup Git) vs. Bab 3 dokumen target:
      Periksa apakah semua langkah konfigurasi Git dari R-02 sudah tercermin di Bab 3 dokumen
      target. Bandingkan nilai-nilai konfigurasi eksak (misal: nama editor, nilai autocrlf).
      Jika ada ketidakcocokan atau data yang hilang, catat sebagai **TEMUAN-GAP-04**.

- [ ] **T3-05** — Komparasi R-02 Bab 8.5 (.gitignore) vs. Bab 3.5 dokumen target:
      Bandingkan pola `.gitignore` di R-02 dengan yang ada di Bab 3.5 dokumen target baris
      per baris. Jika ada pola ignore di R-02 yang hilang dari Bab 3.5, catat sebagai
      **TEMUAN-GAP-05**.

- [ ] **T3-06** — Komparasi R-03 daftar 10 modul vs. Bab 5.3 (Scope Commit) dokumen target:
      Periksa apakah seluruh 10 nama modul dari R-03 sudah terdaftar sebagai scope commit
      yang valid di Bab 5.3. Periksa juga apakah 14 scope resmi di Bab 5.3 konsisten dengan
      daftar modul dan lapisan arsitektur di R-03. Catat ketidakcocokan sebagai **TEMUAN-GAP-06**.

- [ ] **T3-07** — Komparasi R-04 (profil 6 AI) vs. Bab 2.3 dan Bab 12.1 dokumen target:
      Bandingkan nama, kode peran (STK-xxx), dan spesialisasi tiap AI di R-04 dengan tabel
      di Bab 2.3 dan Bab 12.1. Periksa apakah ada AI yang profil atau spesialisasinya
      berbeda antara R-04 dan dokumen target. Catat sebagai **TEMUAN-GAP-07**.

- [ ] **T3-08** — Komparasi R-05 (arsitektur LAN) vs. konteks di seluruh dokumen target:
      Periksa apakah informasi topologi LAN, ukuran connection pool, dan isolation level
      database yang dirujuk di dokumen target konsisten dengan nilai-nilai di R-05.
      Catat ketidakcocokan sebagai **TEMUAN-GAP-08**.

- [ ] **T3-09** — Komparasi R-06 (security design) vs. Bab 10 dan Bab 11 dokumen target:
      Periksa apakah prosedur keamanan Git di Bab 10 dan prosedur backup di Bab 11 sudah
      mencerminkan spesifikasi dari R-06 (enkripsi AES-256, format audit log JSON, chmod 700,
      dll.). Catat ketidakcocokan atau data yang hilang sebagai **TEMUAN-GAP-09**.

- [ ] **T3-10** — Komparasi R-07 (narasi pemilik) vs. konteks tim di seluruh dokumen target:
      Periksa apakah konteks operasional toko, jumlah AI, dan detail kolaborasi luring
      yang disebutkan di R-07 sudah tercermin secara akurat di dokumen target.
      Catat ketidakcocokan sebagai **TEMUAN-GAP-10**.

---

### TAHAP 4 — Analisis Relevansi: Apakah Dokumen Bebas dari Konten Off-Scope?

> **Tujuan**: Memastikan dokumen target hanya memuat informasi yang **spesifik dan relevan**
> untuk topik Git Workflow. Konten dari domain lain yang "ikut masuk" tanpa alasan yang jelas
> harus diidentifikasi dan dievaluasi.

- [ ] **T4-01** — Baca ulang setiap bab dokumen target dan evaluasi apakah setiap paragraf,
      tabel, atau blok kode **secara langsung berkaitan** dengan pengelolaan Git Workflow.
      Tandai setiap blok konten yang tampak tidak pada tempatnya (misal: penjelasan bisnis
      toko yang terlalu detail, spesifikasi teknis database yang duplikasi dari R-05, dll.).

- [ ] **T4-02** — Untuk setiap konten yang dicurigai off-scope di T4-01:
      - Tentukan apakah konten tersebut **perlu dipertahankan** karena memberikan konteks
        kritis untuk Git Workflow (contoh: menyebut `decimal.Decimal` karena terkait aturan
        code review).
      - Tentukan apakah konten tersebut **perlu dihapus atau diringkas** karena duplikasi
        penuh dari dokumen referensi lain.
      - Catat keputusan Anda sebagai **TEMUAN-RELEVANSI-xx**.

- [ ] **T4-03** — Periksa apakah setiap referensi ke dokumen lain (R-01 s.d. R-07) di dalam
      teks dokumen target menggunakan **path relatif yang valid** dan **versi dokumen yang
      benar (v1.1)**. Catat referensi yang salah path atau salah versi sebagai
      **TEMUAN-RELEVANSI-REF**.

---

### TAHAP 5 — Analisis Struktur Dokumen

> **Tujuan**: Memastikan dokumen memiliki struktur yang sesuai dengan standar dokumen
> teknis industri (setara dokumen IEEE/ISO untuk proyek perangkat lunak profesional).

- [ ] **T5-01** — Periksa kelengkapan **front matter** (bagian header YAML di baris 1-8):
      Apakah semua field berikut sudah terisi dengan nilai yang akurat dan konsisten?
      - `dokumen`: nama dokumen yang deskriptif
      - `proyek`: nama proyek lengkap
      - `versi`: nomor versi dokumen
      - `tanggal`: tanggal pembuatan/revisi terakhir
      - `status`: status dokumen (Draft/Final/Approved)
      - `penyusun`: identitas penyusun yang jelas
      Catat field yang kosong atau tidak akurat sebagai **TEMUAN-STRUKTUR-01**.

- [ ] **T5-02** — Periksa kelengkapan **Riwayat Perubahan Dokumen** (Bab di bagian atas):
      Apakah tabel riwayat mencakup kolom: Versi, Tanggal, Perubahan, dan Oleh?
      Apakah ada entri riwayat untuk setiap versi dokumen yang pernah ada?
      Catat kekurangan sebagai **TEMUAN-STRUKTUR-02**.

- [ ] **T5-03** — Periksa struktur **Bab 1 (Informasi Dokumen)**:
      Apakah Bab 1 memuat semua sub-bab wajib berikut?
      - 1.1 Tujuan Dokumen
      - 1.2 Cakupan Dokumen
      - 1.3 Posisi dalam SDLC
      - 1.4 Hubungan dengan Dokumen Lain (Input & Output)
      - 1.5 Audiens Target
      - 1.6 Definisi, Akronim, dan Singkatan
      Apakah daftar akronim di 1.6 mencakup semua singkatan teknis yang digunakan di seluruh
      dokumen? Catat akronim yang digunakan di dokumen tetapi tidak didefinisikan di 1.6
      sebagai **TEMUAN-STRUKTUR-03**.

- [ ] **T5-04** — Periksa apakah setiap bab utama (##) memiliki pengantar kalimat pembuka
      sebelum masuk ke sub-bab pertama. Bab yang langsung lompat ke sub-bab tanpa kalimat
      pengantar dianggap kurang informatif. Catat bab yang tidak memiliki pengantar sebagai
      **TEMUAN-STRUKTUR-04**.

- [ ] **T5-05** — Periksa apakah semua diagram Mermaid di dokumen dapat diparsing tanpa error
      sintaksis. Validasi secara manual sintaksis `gitGraph`, `flowchart TD`, dan elemen
      lainnya. Catat diagram yang berpotensi error sebagai **TEMUAN-STRUKTUR-05**.

- [ ] **T5-06** — Periksa apakah Bab terakhir adalah **Bab Referensi Dokumen** yang berisi
      tabel dengan kolom: No, Kode Ref, Nama Dokumen, Path, Versi, Prioritas, Relevansi.
      Apakah tabel referensi ini mencakup semua dokumen yang dirujuk di seluruh isi dokumen?
      Catat referensi yang digunakan dalam teks tetapi tidak ada di tabel Bab Referensi
      sebagai **TEMUAN-STRUKTUR-06**.

- [ ] **T5-07** — Periksa konsistensi penggunaan **tag kewajiban** di seluruh dokumen:
      - `[WAJIB]` untuk kewajiban
      - `[DILARANG]` untuk larangan
      - `[MUST]` (apakah digunakan konsisten atau perlu distandarisasi ke bahasa Indonesia?)
      - `[MUST NOT]` (apakah perlu dikonversi?)
      Catat inkonsistensi penggunaan tag sebagai **TEMUAN-STRUKTUR-07**.

---

### TAHAP 6 — Analisis Kelayakan sebagai Input Dokumen SDLC Selanjutnya

> **Tujuan**: Memastikan dokumen ini benar-benar siap digunakan sebagai acuan operasional
> oleh LLM model kecil atau junior programmer tanpa harus bertanya balik atau menebak.

- [ ] **T6-01** — Evaluasi apakah **Bab 4 (Strategi Branching)** memberikan instruksi yang
      cukup spesifik sehingga seorang programmer pemula dapat langsung mengetahui:
      - Branch apa yang harus dibuat untuk tugas pengembangan modul M.3 (PPOB)?
      - Siapa yang bertanggung jawab membuat branch tersebut (berdasarkan STK-xxx)?
      - Perintah Git eksak apa yang harus dijalankan?
      Jika tidak cukup spesifik, catat kekurangan sebagai **TEMUAN-KELAYAKAN-01**.

- [ ] **T6-02** — Evaluasi apakah **Bab 5 (Konvensi Commit)** memberikan panduan yang cukup
      untuk skenario berikut tanpa ambigu:
      - Seorang AI membuat commit untuk perubahan pada file `logic/transaksi.py` dan
        `cli/kasir_menu.py` sekaligus. Apakah boleh dijadikan satu commit?
      - Bagaimana format commit yang benar untuk penambahan file dokumentasi SDLC baru?
      Jika terdapat celah panduan, catat sebagai **TEMUAN-KELAYAKAN-02**.

- [ ] **T6-03** — Evaluasi apakah **Bab 6 (Development Workflow)** memberikan instruksi
      langkah-langkah yang cukup eksplisit sehingga seorang LLM model kecil dapat mengikuti
      alur dari "mulai tugas" hingga "merge ke main" tanpa memerlukan penjelasan tambahan.
      Apakah setiap langkah menyebut perintah Git yang eksak? Catat celah sebagai
      **TEMUAN-KELAYAKAN-03**.

- [ ] **T6-04** — Evaluasi apakah **Bab 7 (Merge dan Conflict Resolution)** cukup eksplisit
      untuk skenario berikut:
      - Bagaimana prosedur jika terjadi conflict pada file yang sama diubah oleh dua AI
        yang berbeda secara bersamaan?
      - Apakah ada prosedur eskalasi jika Junior Programmer tidak bisa memutuskan mana
        logika yang benar?
      Catat celah sebagai **TEMUAN-KELAYAKAN-04**.

- [ ] **T6-05** — Evaluasi apakah **Bab 8 (Code Review & Quality Gate)** dapat dieksekusi
      secara mandiri oleh LLM tanpa informasi tambahan:
      - Apakah instruksi untuk memicu review Gemini 3 Flash sudah dijelaskan secara operasional
        (bukan hanya disebutkan)?
      - Apakah format laporan review sudah didefinisikan?
      Catat celah sebagai **TEMUAN-KELAYAKAN-05**.

- [ ] **T6-06** — Evaluasi apakah **Bab 12 (Tim Campuran)** memberikan panduan handover
      yang cukup spesifik:
      - Format file `handover_notes.txt` — apakah sudah didefinisikan strukturnya?
      - Lokasi penyimpanan `handover_notes.txt` — apakah direktori spesifik sudah disebutkan?
      Catat celah sebagai **TEMUAN-KELAYAKAN-06**.

---

### TAHAP 7 — Analisis Kualitas Bahasa Indonesia

> **Tujuan**: Memastikan seluruh isi dokumen menggunakan bahasa Indonesia yang natural,
> tidak ambigu, tidak membingungkan, dan mudah dipahami oleh pembaca teknis junior.

- [ ] **T7-01** — Baca ulang seluruh dokumen target dan identifikasi:
      - Kalimat yang terlalu panjang (lebih dari 3 anak kalimat dalam satu kalimat tunggal).
      - Kalimat pasif yang ambigu (tidak jelas siapa subjek pelakunya).
      - Istilah teknis bahasa Inggris yang digunakan tanpa penjelasan padanannya.
      - Penggunaan kata `or` dan `and` dalam kalimat bahasa Indonesia (seharusnya `atau`
        dan `dan`).
      Catat semua temuan sebagai **TEMUAN-BAHASA-01**.

- [ ] **T7-02** — Periksa apakah **setiap akronim/singkatan teknis** dijelaskan setidaknya
      sekali (pada kemunculan pertamanya) di dalam dokumen, atau terdapat di Bab 1.6.
      Catat akronim yang tidak pernah dijelaskan sebagai **TEMUAN-BAHASA-02**.

- [ ] **T7-03** — Periksa apakah gaya penulisan **konsisten** di seluruh dokumen:
      - Apakah label kewajiban menggunakan bahasa yang seragam (`WAJIB` vs. `MUST`)?
      - Apakah penulisan nama model AI konsisten (ejaan, huruf besar/kecil)?
      - Apakah penulisan nama branch konsisten menggunakan format `backtick`?
      Catat inkonsistensi sebagai **TEMUAN-BAHASA-03**.

---

### TAHAP 8 — Analisis Interruptibilitas (Apakah Dokumen Akan Memicu Pertanyaan Berulang?)

> **Tujuan**: Memastikan dokumen tidak mengandung ambiguitas yang akan menyebabkan
> LLM model kecil atau junior programmer berhenti bekerja dan meminta klarifikasi berulang,
> yang menghambat proses konstruksi kode SDLC berikutnya.

- [ ] **T8-01** — Identifikasi setiap **instruksi atau aturan yang tidak memiliki contoh
      konkret** di dekatnya. Aturan tanpa contoh berpotensi diinterpretasikan berbeda-beda.
      Catat aturan yang perlu ditambahi contoh sebagai **TEMUAN-INTERUPSI-01**.

- [ ] **T8-02** — Identifikasi setiap **tabel atau daftar yang tidak lengkap** (misal: ada
      kolom kosong, ada sel tabel yang berisi tanda `?` atau tanda `-` tanpa penjelasan).
      Catat sebagai **TEMUAN-INTERUPSI-02**.

- [ ] **T8-03** — Identifikasi apakah ada **kondisi percabangan logika** (misal: "jika kondisi
      A maka lakukan X, jika kondisi B maka lakukan Y") yang hanya mendefinisikan satu
      cabang tetapi tidak mendefinisikan cabang lainnya. Catat sebagai **TEMUAN-INTERUPSI-03**.

- [ ] **T8-04** — Identifikasi apakah ada **referensi silang (cross-reference)** ke bab atau
      sub-bab lain yang tidak ada atau penomorannya salah. Catat sebagai
      **TEMUAN-INTERUPSI-04**.

---

### TAHAP 9 — Pengisian Data Kosong

> **Tujuan**: Mengisi semua placeholder data kosong dengan data yang sesuai, relevan,
> dan masih dalam ruang lingkup dokumen Git Workflow — tanpa perlu konfirmasi manual
> ke pemilik toko untuk data yang bersifat teknis/non-personal.

Berdasarkan daftar dari T1-03, untuk setiap penanda `[DATA KOSONG]` atau `[HARUS DIISI MANUAL]`:

- [ ] **T9-01** — **Bab 3.2 — Git Identity (`user.name` dan `user.email` pemilik)**:
      Data ini bersifat **personal/sensitif** dan tidak bisa diisi secara otomatis.
      Tetap pertahankan placeholder-nya tetapi **ubah redaksi pesan peringatan** menjadi
      lebih jelas dan tidak ambigu: instruksikan secara eksplisit bahwa nilai ini WAJIB
      diisi oleh pemilik fisik sebelum commit pertama, dan apa konsekuensi jika tidak diisi.

- [ ] **T9-02** — **Bab 3.3 — Peringatan `core.autocrlf`**:
      Peringatan ini sebenarnya bukan "data kosong" melainkan instruksi pengingat.
      Evaluasi ulang: apakah peringatan ini perlu dipertahankan sebagai catatan atau
      bisa diintegrasikan ke dalam langkah instruksi (numbered list) sehingga tidak terkesan
      sebagai data yang belum diisi.

- [ ] **T9-03** — **Bab 3.6 — Peringatan `.gitattributes`**:
      Peringatan menyebutkan bahwa berkas ini belum tercantum di SDLC awal.
      Evaluasi: informasi ini sudah informatif. Perkuat dengan menambahkan **perintah eksak**
      untuk memverifikasi bahwa `.gitattributes` sudah aktif:
      ```bash
      git check-attr eol -- logic/transaksi.py
      # Output yang diharapkan: logic/transaksi.py: eol: lf
      ```

- [ ] **T9-04** — **Bab 10.3 — Peringatan `git-filter-repo`**:
      Tambahkan instruksi instalasi offline `git-filter-repo` yang konkret untuk konteks
      offline LAN, misalnya dengan mengunduh dan menginstal secara manual dari package
      `.deb` yang sudah diunduh sebelumnya atau melalui pip offline:
      ```bash
      pip install git-filter-repo --no-index --find-links /path/to/offline/packages
      ```
      Ganti placeholder `[DATA KOSONG]` dengan instruksi teknis yang konkret.

- [ ] **T9-05** — **Bab 11.3 — Peringatan backup USB**:
      Informasi tentang kebutuhan 2 unit USB Flashdisk adalah instruksi operasional yang
      valid. Perkuat dengan menambahkan **prosedur rotasi backup** (misal: USB-A untuk
      hari ganjil, USB-B untuk hari genap) agar backup tidak overwrite satu sama lain.

- [ ] **T9-06** — **Bab 12.1 — Email Junior Programmer `[HARUS DIISI MANUAL]`**:
      Sama dengan T9-01, data ini personal/sensitif. Pertahankan placeholder tetapi ubah
      redaksi menjadi instruksi yang lebih eksplisit tentang format email yang harus digunakan
      (misal: apakah email Gmail pribadi, email khusus proyek, atau email lokal domain
      `@abucom.local`?). Tentukan rekomendasi terbaik berdasarkan konteks offline LAN.

- [ ] **T9-07** — **Periksa apakah ada data kosong lainnya** yang tidak tertangkap di T1-03
      (misal: nilai default yang masih menggunakan contoh placeholder seperti `example.com`,
      nilai port database yang belum disebutkan di konteks yang relevan, dll.).
      Isi semua data teknis yang bisa ditentukan berdasarkan konteks referensi R-01 s.d. R-07.

---

### TAHAP 10 — Penambahan Konten yang Terindentifikasi Kurang

> **Tujuan**: Berdasarkan semua temuan dari Tahap 3 s.d. 9, tambahkan atau sempurnakan
> konten yang kurang — TANPA menghapus konten yang sudah benar.

Untuk setiap TEMUAN yang dicatat pada tahap-tahap sebelumnya:

- [ ] **T10-01** — Resolusi semua **TEMUAN-GAP** (dari Tahap 3):
      Tambahkan konten yang hilang ke bab/sub-bab yang paling relevan. Jika konten baru
      memerlukan sub-bab baru, buat sub-bab baru dengan penomoran yang konsisten.

- [ ] **T10-02** — Resolusi semua **TEMUAN-RELEVANSI** (dari Tahap 4):
      - Hapus atau ringkas konten yang terbukti off-scope dan duplikatif.
      - Perbaiki path referensi yang salah.

- [ ] **T10-03** — Resolusi semua **TEMUAN-STRUKTUR** (dari Tahap 5):
      - Lengkapi front matter yang kurang.
      - Tambahkan kalimat pengantar bab yang hilang.
      - Perbaiki sintaksis diagram Mermaid yang berpotensi error.
      - Tambahkan akronim yang hilang ke Bab 1.6.
      - Standarisasi tag kewajiban (`[WAJIB]`/`[DILARANG]` dalam bahasa Indonesia).

- [ ] **T10-04** — Resolusi semua **TEMUAN-KELAYAKAN** (dari Tahap 6):
      Tambahkan contoh konkret, format file yang hilang (misal struktur `handover_notes.txt`),
      dan instruksi perintah eksak yang kurang.

- [ ] **T10-05** — Resolusi semua **TEMUAN-BAHASA** (dari Tahap 7):
      Perbaiki kalimat yang terlalu panjang, ubah `or`/`and` menjadi `atau`/`dan`,
      dan tambahkan penjelasan akronim pada kemunculan pertamanya.

- [ ] **T10-06** — Resolusi semua **TEMUAN-INTERUPSI** (dari Tahap 8):
      Tambahkan contoh untuk aturan yang tidak memiliki contoh, lengkapi tabel yang tidak
      lengkap, definisikan cabang kondisi yang hilang, dan perbaiki referensi silang yang
      salah nomor.

- [ ] **T10-07** — Resolusi semua **TEMUAN dari Tahap 9 (Data Kosong)**:
      Terapkan semua perbaikan redaksi placeholder dan penambahan instruksi teknis
      yang telah diidentifikasi di Tahap 9.

---

### TAHAP 11 — Penulisan Ulang Dokumen Final ke File Target (Overwrite)

> **TAHAP PALING KRITIS — Baca seluruh instruksi ini dengan saksama sebelum menulis.**

- [ ] **T11-01** — Sebelum menulis, lakukan **review akhir mental** terhadap seluruh konten
      yang akan ditulis. Pastikan:
      - Seluruh temuan dari Tahap 3 s.d. 10 sudah diintegrasikan ke dalam draf akhir.
      - Tidak ada konten baru yang ditambahkan di luar cakupan issue ini.
      - Versi dokumen sudah diubah dari `1.0` menjadi `1.1` di front matter dan di tabel
        Riwayat Perubahan Dokumen.
      - Tanggal di front matter sudah diperbarui ke tanggal eksekusi issue ini.
      - Entri baru di tabel Riwayat Perubahan sudah ditambahkan (baris baru di bawah
        entri v1.0), menjelaskan perubahan apa saja yang dilakukan pada revisi v1.1.

- [ ] **T11-02** — Tulis ulang seluruh isi dokumen ke file target menggunakan mekanisme
      **overwrite** (timpa seluruh konten lama):
      - **File target**: `docs/sdlc/04_implementation/04_git_workflow.md`
      - **Aturan penulisan ABSOLUT**:
        - `[DILARANG KERAS]` Memotong, meringkas, atau menghilangkan bagian mana pun
          dari dokumen yang sudah ada dan sudah benar.
        - `[DILARANG KERAS]` Menggunakan placeholder seperti `[... konten sebelumnya ...]`
          atau `[dst]` atau `(lanjutan)` atau tanda ellipsis (`...`) untuk merepresentasikan
          bagian yang tidak ditulis ulang.
        - `[WAJIB]` Seluruh teks dari baris pertama hingga baris terakhir ditulis ulang
          secara penuh dan eksplisit tanpa pengecualian.
        - `[WAJIB]` Urutan bab dan sub-bab dipertahankan atau ditingkatkan (tidak boleh
          dikurangi).

- [ ] **T11-03** — Setelah proses overwrite selesai, baca ulang file hasil overwrite dari
      awal hingga akhir untuk memverifikasi:
      - Tidak ada konten yang terpotong di tengah kalimat atau tabel.
      - Tidak ada bab yang hilang dibandingkan draf akhir.
      - Versi dokumen sudah berubah menjadi `1.1`.
      - Semua perintah bash/cmd masih berada dalam blok kode yang benar (tidak lepas
        ke teks biasa).
      - Semua tabel Markdown masih terbentuk dengan benar (pipe `|` sejajar).

---

### TAHAP 12 — Pembaruan Daftar Referensi

> **Tujuan**: Jika selama proses validasi dan penyempurnaan ditemukan bahwa dokumen
> membutuhkan referensi tambahan di luar 7 referensi yang sudah ada (R-01 s.d. R-07),
> referensi baru tersebut wajib dicatat.

- [ ] **T12-01** — Periksa apakah selama proses analisis (Tahap 3 s.d. 10) Anda merujuk
      atau mengutip sumber informasi dari file mana pun di luar daftar R-01 s.d. R-07.

- [ ] **T12-02** — Jika ada file referensi baru yang digunakan:
      - Tentukan Kode Ref baru (misal: R-08, R-09, dst.).
      - Tambahkan baris baru di tabel Bab 16 (Referensi Dokumen) **di bagian paling bawah**
        tabel tersebut.
      - Isi semua kolom: No, Kode Ref, Nama Dokumen, Path Relatif, Versi, Prioritas, Relevansi.

- [ ] **T12-03** — Jika tidak ada referensi baru, tetap periksa apakah tabel referensi
      yang sudah ada sudah mencantumkan versi dokumen yang benar untuk semua R-01 s.d. R-07.
      Perbarui jika ada versi yang salah.

---

### TAHAP 13 — Verifikasi Final

- [ ] **T13-01** — Jalankan pengecekan berikut terhadap file hasil overwrite:
      - Hitung jumlah bab (##) dan sub-bab (###): apakah sama atau lebih banyak dari
        dokumen asli (bukan berkurang)?
      - Verifikasi bahwa versi `1.1` sudah muncul di: front matter, judul tabel
        Riwayat Perubahan (entri baru), dan nama dokumen jika disebutkan.
      - Verifikasi bahwa tidak ada teks `[TAHAP X]` atau instruksi internal issue ini
        yang ikut tertulis ke dalam dokumen target (dokumen target harus bersih dari
        konten meta issue).

- [ ] **T13-02** — Buat **ringkasan eksekusi** dalam format berikut dan simpan sebagai
      komentar di baris paling akhir file issue ini (opsional, jika environment mendukung):

      ```
      RINGKASAN EKSEKUSI ISSUE #0042
      Tanggal Eksekusi    : [isi tanggal]
      Eksekutor           : [nama LLM atau programmer]
      Total Temuan Gap    : [jumlah]
      Total Temuan Struktur: [jumlah]
      Total Temuan Bahasa : [jumlah]
      Total Temuan Interupsi: [jumlah]
      Data Kosong Diisi   : [jumlah]
      Referensi Baru      : [jumlah, atau "Tidak ada"]
      Versi Akhir Dokumen : 1.1
      Status Issue        : Closed
      ```

---

## Aturan Tambahan yang Wajib Dipatuhi Sepanjang Pelaksanaan

> Aturan berikut berlaku secara universal untuk seluruh tahapan di atas.

1. **Zero Hallucination**: Jangan menambahkan informasi teknis yang tidak dapat dikonfirmasi
   dari salah satu dari 7 file referensi yang ada (R-01 s.d. R-07) atau dari isi dokumen
   target itu sendiri. Jika ada informasi yang perlu ditambahkan tetapi tidak ada di referensi
   mana pun, catat sebagai "memerlukan konfirmasi pemilik" alih-alih mengarang data.

2. **Bukti Berbasis Teks**: Setiap temuan harus disertai kutipan spesifik (nama file dan
   nomor bab/baris) sebagai bukti. Hindari pernyataan umum tanpa rujukan.

3. **Presisi Teknis**: Semua perintah Git, konfigurasi, dan nilai parameter yang ditambahkan
   atau diperbaiki harus sintaksis yang valid dan sudah teruji secara konseptual.

4. **Konsistensi Internal**: Setiap penambahan konten harus konsisten dengan konvensi gaya
   penulisan, terminologi, dan format yang sudah digunakan di dokumen target.

5. **Scope Git Workflow Only**: Jangan menambahkan konten yang seharusnya berada di dokumen
   SDLC lain (misal: detail implementasi bisnis modul, detail skema database, dll.). Jika
   relevansi terhadap Git Workflow tidak dapat dijelaskan secara langsung, konten tersebut
   tidak boleh ditambahkan.

6. **Tidak Ada Pemotongan (No Truncation)**: Saat menulis ulang dokumen di Tahap 11,
   seluruh konten harus ditulis penuh. Ini adalah aturan absolut dan tidak dapat dikompromikan
   meskipun konten dokumen sangat panjang.

7. **Bahasa Indonesia Konsisten**: Seluruh penambahan konten menggunakan bahasa Indonesia
   profesional. Istilah teknis internasional (Git, branch, commit, merge, dll.) boleh
   dipertahankan dalam bahasa aslinya tetapi wajib ditulis menggunakan format yang konsisten
   (misal: selalu italic *merge* atau selalu backtick `merge`).

---

## Kriteria Selesai (Definition of Done)

Issue #0042 dinyatakan **SELESAI** jika dan hanya jika **semua kondisi berikut terpenuhi**:

- [ ] **DOD-01** — Semua checkbox dari T1-01 hingga T13-02 sudah ditandai `[x]`.
- [ ] **DOD-02** — File `docs/sdlc/04_implementation/04_git_workflow.md` sudah diperbarui
      dengan versi `1.1` dan berisi seluruh perbaikan hasil validasi.
- [ ] **DOD-03** — Tidak ada data kosong (placeholder `[HARUS DIISI MANUAL]` untuk data
      teknis) yang tersisa di dokumen final — kecuali data personal pemilik yang memang
      harus diisi secara manual oleh pemilik.
- [ ] **DOD-04** — Dokumen final tidak mengandung konten yang terpotong, tabel yang rusak,
      atau diagram Mermaid yang sintaksisnya tidak valid.
- [ ] **DOD-05** — Bab 16 (Referensi) sudah diperbarui jika ada referensi baru yang
      ditambahkan selama proses validasi.
- [ ] **DOD-06** — Kualitas bahasa Indonesia di seluruh dokumen sudah memenuhi standar
      "dapat dipahami oleh LLM model kecil tanpa pertanyaan lanjutan".

---

## Referensi Issue Ini

| No | Nama File | Path |
|:---:|:---|:---|
| 1 | Git Workflow (Target) | `docs/sdlc/04_implementation/04_git_workflow.md` |
| 2 | Coding Standard (R-01) | `docs/sdlc/04_implementation/01_coding_standard.md` |
| 3 | Environment Setup (R-02) | `docs/sdlc/04_implementation/02_environment_setup.md` |
| 4 | Module Structure (R-03) | `docs/sdlc/04_implementation/03_module_structure.md` |
| 5 | Tech Stack Decision (R-04) | `docs/sdlc/01_planning/04_tech_stack_decision.md` |
| 6 | System Architecture (R-05) | `docs/sdlc/03_design/03_system_architecture.md` |
| 7 | Security Design (R-06) | `docs/sdlc/03_design/06_security_design.md` |
| 8 | Narasi Pemilik (R-07) | `docs/sdlc/narasi.txt` |
