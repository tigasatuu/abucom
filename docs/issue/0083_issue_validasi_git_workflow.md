# Validasi & Penyempurnaan Dokumen Git Workflow

---

## Metadata Issue

| Field              | Nilai                                                                 |
|:-------------------|:----------------------------------------------------------------------|
| **Judul**          | Validasi & Penyempurnaan Dokumen Git Workflow                         |
| **Dokumen Utama**  | `docs/sdlc/04_implementation/04_git_workflow.md`                      |
| **Versi Saat Ini** | v1.1                                                                  |
| **Versi Target**   | v1.2                                                                  |
| **Tanggal Dibuat** | 2026-05-29                                                            |
| **Prioritas**      | TINGGI — Blocker sebelum fase konstruksi kode aktual dimulai          |
| **Assignee**       | Junior Programmer / LLM AI Model (Pelaksana)                         |
| **Lokasi Referensi** | `docs/sdlc/`                                                        |

---

## 1. Persona Pelaksana

Kamu adalah seorang **Principal DevOps Architect & Technical Documentation Auditor** dengan spesialisasi:

- **10+ tahun pengalaman** dalam menyusun, mengaudit, dan memvalidasi standar Git Workflow industri skala enterprise.
- **Ahli standar SDLC**: Familiar dengan konvensi Conventional Commits, GitFlow, Trunk-Based Development, SemVer, dan DORA metrics.
- **Skeptis dan kritis**: Kamu tidak menerima dokumen apa pun yang belum divalidasi secara menyeluruh. Setiap klaim dalam dokumen harus dapat dibuktikan oleh referensi yang dikutipnya.
- **Paham konteks AbuCom**: Sistem manajemen percetakan offline LAN, tim campuran (1 Junior Programmer + 6 AI), dual-OS Windows 11 & Linux Debian 12, tanpa koneksi internet produksi.
- **Teliti hingga level karakter**: Kamu memeriksa konsistensi terminologi, kelengkapan bab, validitas setiap perintah Git, dan kesesuaian struktur bahasa Indonesia profesional.

> **PENTING**: Peran ini bukan sekadar membaca ulang. Kamu `[WAJIB]` melakukan analisis kritis, komparasi silang antar dokumen, deteksi gap, dan penulisan ulang seluruh dokumen hasil validasi secara penuh.

---

## 2. Konteks & Tujuan

Dokumen **Git Workflow** (`04_git_workflow.md`) adalah deliverable ke-4 pada Fase 04 Implementation SDLC AbuCom. Dokumen ini merupakan **gerbang wajib** yang harus dilewati sebelum seluruh tim (Junior Programmer + 6 AI) dapat memulai konstruksi kode aktual modul M.1 hingga M.10.

**Tujuan Issue ini**: Memastikan dokumen Git Workflow telah memenuhi seluruh standar kualitas berikut sebelum digunakan sebagai acuan operasional resmi tim:

1. Kelengkapan isi berdasarkan semua dokumen referensi yang dikutipnya.
2. Relevansi & kebersihan konten — tidak ada informasi di luar cakupan dokumen ini.
3. Struktur dokumen sesuai standar praktik industri.
4. Kesiapan sebagai input valid untuk fase SDLC selanjutnya.
5. Bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami.
6. Kualitas tidak akan dipertanyakan atau menghambat pekerjaan fase berikutnya.
7. Tidak ada data yang kosong, placeholder, atau perlu diisi manual.

---

## 3. Daftar File yang Harus Dibaca Sebelum Memulai

Baca seluruh file berikut secara **berurutan** sebelum melakukan analisis apa pun. Tandai `[x]` setelah selesai membaca setiap file:

- [ ] **[BACA-01]** Baca `docs/sdlc/04_implementation/04_git_workflow.md` (Dokumen Utama — Baca dari baris 1 hingga baris terakhir tanpa melewatkan satu baris pun)
- [ ] **[BACA-02]** Baca `docs/sdlc/04_implementation/01_coding_standard.md` (R-01 — Referensi PRIMER)
- [ ] **[BACA-03]** Baca `docs/sdlc/04_implementation/02_environment_setup.md` (R-02 — Referensi PRIMER)
- [ ] **[BACA-04]** Baca `docs/sdlc/04_implementation/03_module_structure.md` (R-03 — Referensi SEKUNDER)
- [ ] **[BACA-05]** Baca `docs/sdlc/01_planning/04_tech_stack_decision.md` (R-04 — Referensi SEKUNDER)
- [ ] **[BACA-06]** Baca `docs/sdlc/03_design/03_system_architecture.md` (R-05 — Referensi TERSIER)
- [ ] **[BACA-07]** Baca `docs/sdlc/03_design/06_security_design.md` (R-06 — Referensi TERSIER)
- [ ] **[BACA-08]** Baca `docs/sdlc/narasi.txt` (R-07 — Referensi TERSIER)

> **CATATAN PENTING**: Jika saat membaca ditemukan dokumen referensi tambahan yang dikutip di dalam dokumen utama tetapi belum tercantum di daftar di atas, tambahkan ke daftar bacaan dan baca juga dokumen tersebut.

---

## 4. Instruksi Validasi — Tahap Demi Tahap

Laksanakan setiap tahap berikut secara **berurutan**. Jangan melompati tahap. Catat setiap temuan secara eksplisit.

---

### TAHAP 1 — Komparasi Mendalam: Dokumen Utama vs. Seluruh Referensi

**Tujuan**: Memastikan dokumen utama telah merangkum *semua* informasi yang relevan dari seluruh dokumen referensi yang dikutipnya.

- [ ] **[T1-01]** Buka `01_coding_standard.md` (R-01). Baca Bab 15 (Version Control Git), Bab 16 (Larangan Mutlak), dan Bab 17 (Checklist Kepatuhan). Bandingkan poin demi poin dengan isi dokumen utama Bab 5 (Konvensi Commit), Bab 8 (Code Review), Bab 14 (Larangan Mutlak), dan Bab 15 (Checklist). Catat setiap poin dari R-01 yang **belum** tercantum di dokumen utama.

- [ ] **[T1-02]** Buka `02_environment_setup.md` (R-02). Baca Bab 9 (Setup Git lokal) dan Bab 8.5 (Setup .gitignore). Bandingkan dengan isi Bab 3 (Konfigurasi Git Awal) dokumen utama. Pastikan setiap perintah, urutan langkah, dan opsi konfigurasi sudah selaras atau sudah diadaptasi dengan benar. Catat setiap informasi dari R-02 yang **terlewat** di dokumen utama.

- [ ] **[T1-03]** Buka `03_module_structure.md` (R-03). Baca Bab 2.3 (10 modul fungsional), Bab 3.1 (pohon direktori ASCII), dan Bab 13 (Module-to-File mapping). Bandingkan dengan Bab 5.3 (Scope Commit) dokumen utama. Periksa apakah ke-14 scope resmi commit sudah mencakup seluruh modul dan direktori fungsional yang terdapat di R-03. Catat jika ada scope yang missing atau tidak konsisten.

- [ ] **[T1-04]** Buka `04_tech_stack_decision.md` (R-04). Baca bagian yang mendefinisikan platform runtime, versi library yang dikunci, daftar 6 AI spesialis, dan spesifikasi dual-OS. Bandingkan dengan Bab 2.3 (Peran Tim), Bab 3.1 (Instalasi Git), dan Bab 12.1 (Identitas Git AI) dokumen utama. Catat setiap ketidaksesuaian nama model, versi, atau peran AI.

- [ ] **[T1-05]** Buka `03_system_architecture.md` (R-05). Baca bagian topologi LAN offline, isolation level database (repeatable read), dan connection pool `abupool`. Bandingkan dengan Bab 2 (Prinsip Dasar) dan Bab 11 (Backup Recovery) dokumen utama. Catat jika ada spesifikasi teknis infrastruktur yang seharusnya mempengaruhi prosedur Git (misal: cara push ke server LAN, alamat remote, dll.) tetapi tidak disebutkan.

- [ ] **[T1-06]** Buka `06_security_design.md` (R-06). Baca bagian enkripsi backup AES-256 ZIP, chmod 700 server, audit log JSON, brute-force rate-limiting, dan sanitasi CLI. Bandingkan dengan Bab 10 (Keamanan Git) dan Bab 11 (Backup) dokumen utama. Catat setiap spesifikasi keamanan dari R-06 yang seharusnya ada di dokumen utama tetapi belum tercantum.

- [ ] **[T1-07]** Baca `narasi.txt` (R-07). Ekstrak semua informasi tentang: susunan tim (jumlah dan nama AI), cara kerja luring, identitas pemilik, dan konteks operasional toko. Bandingkan dengan Bab 2.3, Bab 12, dan Bab 3.2 dokumen utama. Catat setiap fakta operasional dari narasi yang belum terakomodasi di dokumen utama.

- [ ] **[T1-08]** Buat **Daftar Temuan Gap T1** — daftar semua poin dari referensi yang belum ada atau tidak lengkap di dokumen utama. Format setiap temuan sebagai:
  ```
  [GAP-T1-XXX] Sumber: R-0X Bab Y.Z | Lokasi di Dokumen Utama: Bab A.B | Deskripsi Gap: ...
  ```

---

### TAHAP 2 — Audit Relevansi: Apakah Isi Dokumen Sudah Bersih & Fokus?

**Tujuan**: Memastikan dokumen utama hanya memuat informasi yang memang merupakan tanggung jawab dokumen Git Workflow, tidak menyerap konten yang seharusnya ada di dokumen referensi lain.

- [ ] **[T2-01]** Baca setiap bab dokumen utama dari Bab 1 hingga Bab 16 (Referensi). Untuk setiap paragraf dan tabel, tanyakan: *"Apakah informasi ini benar-benar merupakan bagian dari standar Git Workflow, ataukah ini adalah pengulangan isi dari dokumen lain yang seharusnya cukup direferensikan saja?"*

- [ ] **[T2-02]** Identifikasi apakah ada **duplikasi konten** antara dokumen utama dengan referensi yang bersifat penjelasan ulang panjang yang tidak menambah nilai konteks Git. Misalnya: penjelasan panjang tentang spesifikasi modul bisnis yang seharusnya ada di Module Structure, bukan di Git Workflow.

- [ ] **[T2-03]** Identifikasi apakah ada **konten yang tidak relevan** — informasi yang tidak ada hubungannya langsung dengan pengelolaan version control, branching, commit, merge, review, backup, atau keamanan Git.

- [ ] **[T2-04]** Buat **Daftar Temuan T2** — daftar semua konten yang perlu dihapus, dipangkas, atau diganti dengan referensi tautan saja. Format:
  ```
  [IRRELEVANT-T2-XXX] Lokasi: Bab A.B Paragraf/Tabel ke-Y | Alasan: ... | Rekomendasi: Hapus / Ganti dengan referensi tautan ke Bab X dokumen R-0Z
  ```

---

### TAHAP 3 — Audit Struktur Dokumen: Standar Industri

**Tujuan**: Memastikan struktur hierarki bab dan sub-bab dokumen utama memenuhi standar dokumentasi teknis profesional yang lazim digunakan di industri pengembangan perangkat lunak.

- [ ] **[T3-01]** Periksa apakah **header YAML frontmatter** (baris 1-8) sudah lengkap. Field yang harus ada: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`. Pastikan nilainya akurat sesuai kondisi terkini.

- [ ] **[T3-02]** Periksa apakah **Riwayat Perubahan Dokumen** mencatat semua versi dengan informasi perubahan yang cukup detail untuk dipahami tanpa harus membaca seluruh dokumen.

- [ ] **[T3-03]** Periksa apakah **Bab 1 (Informasi Dokumen)** sudah memuat minimal:
  - Tujuan dokumen yang jelas dan measurable
  - Cakupan yang menyebutkan apa yang **termasuk** DAN apa yang **tidak termasuk** (out-of-scope)
  - Posisi dalam SDLC yang lengkap dengan diagram atau penjelasan
  - Hubungan input/output dengan dokumen lain yang spesifik
  - Daftar audiens target yang lengkap
  - Glosarium istilah teknis yang mencakup semua akronim yang digunakan di seluruh dokumen

- [ ] **[T3-04]** Periksa apakah setiap bab utama (Bab 2 hingga Bab 15) memiliki:
  - Kalimat pembuka yang menjelaskan tujuan bab tersebut
  - Sub-bab yang terorganisir logis dari umum ke spesifik
  - Perintah Git yang eksak (dengan contoh nyata menggunakan nama file/branch AbuCom), bukan contoh abstrak generik
  - Diagram Mermaid (untuk bab yang membutuhkan representasi visual alur kerja)
  - Kotak peringatan/panduan (blockquote `>`) untuk instruksi kritis

- [ ] **[T3-05]** Periksa apakah **Bab 16 (Referensi)** sudah lengkap dan formatnya konsisten: mencantumkan semua dokumen yang benar-benar dikutip di dalam dokumen utama, dengan kolom kode referensi, nama, path relatif, versi, prioritas, dan relevansi spesifik.

- [ ] **[T3-06]** Periksa apakah **urutan bab** secara keseluruhan sudah mengikuti alur logis yang wajar untuk dokumen Git Workflow industri:
  - Informasi Umum → Prinsip → Konfigurasi → Branching → Commit → Workflow → Merge → Code Review → Tagging → Keamanan → Backup → Kolaborasi Tim → Quick Reference → Larangan → Checklist → Referensi
  - Jika urutannya berbeda atau ada bab yang terasa "terpotong" atau "tidak di tempat yang tepat", catat rekomendasi penyesuaiannya.

- [ ] **[T3-07]** Buat **Daftar Temuan T3** — daftar semua masalah struktur dokumen. Format:
  ```
  [STRUKTUR-T3-XXX] Lokasi: Bab A.B | Masalah: ... | Rekomendasi: ...
  ```

---

### TAHAP 4 — Audit Kesiapan sebagai Input Fase Berikutnya

**Tujuan**: Memastikan dokumen ini cukup lengkap, jelas, dan tidak akan mengakibatkan pertanyaan atau ambiguitas yang menghambat tim developer (Junior Programmer atau AI) saat memulai konstruksi kode aktual.

- [ ] **[T4-01]** Simulasikan dirimu sebagai **Junior Programmer yang baru pertama kali membuka dokumen ini**. Periksa apakah kamu bisa langsung tahu:
  - Apa branch yang harus dibuat untuk mengerjakan modul M.1 Transaksi?
  - Bagaimana format commit yang benar untuk file `logic/transaksi.py`?
  - Siapa yang harus melakukan review sebelum merge?
  - Bagaimana cara melakukan backup repositori hari ini?
  - Apa yang harus dilakukan jika terjadi merge conflict?

- [ ] **[T4-02]** Simulasikan dirimu sebagai **Model AI (misalnya Gemini Pro High STK-009)** yang membaca dokumen ini. Periksa apakah instruksi sudah cukup deterministik dan tidak ambigu untuk dieksekusi tanpa harus menebak-nebak:
  - Identitas Git mana yang harus dikonfigurasi?
  - Branch mana yang menjadi tanggung jawab AI ini?
  - Format commit message apa yang harus digunakan untuk file `logic/bom_hpp.py`?
  - Bagaimana cara menyerahkan hasil pekerjaan ke AI berikutnya?

- [ ] **[T4-03]** Periksa apakah dokumen menyertakan **contoh konkret berbasis AbuCom** (bukan contoh generik) untuk setiap prosedur kritis. Contoh konkret harus menggunakan nama file nyata, nama branch nyata, dan nama modul nyata sesuai Module Structure R-03.

- [ ] **[T4-04]** Periksa apakah ada **prosedur yang tidak lengkap** — yaitu prosedur yang disebutkan tapi tidak dijelaskan langkahnya secara detail. Misalnya: "Pemilik melakukan review visual" — tanpa menjelaskan apa yang diperiksa, berapa lama, dan bagaimana hasilnya dicatat.

- [ ] **[T4-05]** Buat **Daftar Temuan T4** — daftar semua hal yang bisa menghambat pekerjaan fase berikutnya. Format:
  ```
  [INPUT-T4-XXX] Konteks: Prosedur / Bab A.B | Masalah: ... | Rekomendasi Perbaikan: ...
  ```

---

### TAHAP 5 — Audit Bahasa Indonesia

**Tujuan**: Memastikan seluruh teks dokumen menggunakan bahasa Indonesia yang natural, profesional, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh Junior Programmer maupun model AI yang lebih kecil.

- [ ] **[T5-01]** Baca setiap kalimat dari Bab 1 hingga Bab 16. Tandai kalimat yang:
  - Menggunakan istilah teknis bahasa Inggris tanpa penjelasan padanannya (padahal ada padanan bahasa Indonesia yang lazim).
  - Kalimatnya terlalu panjang (lebih dari 3 klausa) sehingga sulit dipahami dalam satu kali baca.
  - Menggunakan kata ganti yang ambigu ("ini", "tersebut", "itu") tanpa subjek yang jelas.
  - Menggunakan pasif berlebihan tanpa menyebutkan siapa pelakunya.

- [ ] **[T5-02]** Periksa apakah penggunaan label `[WAJIB]`, `[DILARANG]`, `[DILARANG KERAS]`, `[BAHAYA]` sudah konsisten di seluruh dokumen — tidak ada yang satu tempat pakai `[WAJIB]` tapi tempat lain pakai "harus" tanpa label untuk instruksi yang sama tingkat kekritisannya.

- [ ] **[T5-03]** Periksa apakah istilah teknis yang sama selalu menggunakan terminologi yang konsisten. Contoh: apakah "branch utama" selalu merujuk ke `main`? Apakah "Pemilik Toko", "Junior Programmer", dan "STK-000" digunakan secara konsisten untuk orang yang sama?

- [ ] **[T5-04]** Periksa apakah semua contoh perintah Git, nama file, dan nama branch sudah menggunakan ejaan yang konsisten (tidak ada perbedaan huruf kapital, underscore vs hyphen, dll. untuk objek yang sama).

- [ ] **[T5-05]** Buat **Daftar Temuan T5** — daftar semua masalah bahasa. Format:
  ```
  [BAHASA-T5-XXX] Lokasi: Bab A.B Kalimat/Paragraf ke-Y | Teks Asli: "..." | Masalah: ... | Usulan Perbaikan: "..."
  ```

---

### TAHAP 6 — Audit Data Kosong & Placeholder

**Tujuan**: Memastikan tidak ada data yang masih kosong, belum diisi, atau menggunakan placeholder yang harus diisi manual sebelum dokumen ini siap digunakan.

- [ ] **[T6-01]** Scan seluruh dokumen dari baris pertama hingga baris terakhir. Cari setiap kemunculan:
  - Teks placeholder: `[...]`, `TODO`, `TBD`, `N/A`, `?`, `—` (em dash sebagai penanda kosong), atau tanda lain yang mengindikasikan data belum diisi.
  - Field tabel yang kosong (sel tabel tidak terisi).
  - Perintah Git dengan path atau nama yang bersifat template generik (`/path/to/...`, `<nama-anda>`, dll.) yang seharusnya sudah diisi dengan nilai konkret AbuCom.

- [ ] **[T6-02]** Untuk setiap placeholder yang ditemukan, tentukan nilai yang paling sesuai berdasarkan konteks dokumen AbuCom dan dokumen referensi yang ada. Isi semua placeholder tersebut dengan nilai nyata yang konkret.

- [ ] **[T6-03]** Khusus untuk perintah Git yang masih menggunakan path generik (misal `pip install git-filter-repo --no-index --find-links /path/to/offline/packages`), lengkapi dengan path konkret yang sesuai dengan struktur direktori AbuCom yang didefinisikan di R-03.

- [ ] **[T6-04]** Buat **Daftar Temuan T6** — daftar semua placeholder dan data kosong beserta nilai penggantinya. Format:
  ```
  [DATA-T6-XXX] Lokasi: Bab A.B Baris ke-Y | Teks Placeholder: "..." | Nilai Pengganti: "..." | Sumber Nilai: R-0X Bab Y.Z
  ```

---

### TAHAP 7 — Validasi Teknis Spesifik Git Workflow

**Tujuan**: Memvalidasi aspek-aspek teknis spesifik yang merupakan ciri khas dokumen Git Workflow dan memastikan tidak ada kesalahan faktual atau inkonsistensi teknis.

- [ ] **[T7-01]** **Validasi Perintah Git**: Baca setiap blok kode `bash` atau `cmd` yang berisi perintah Git. Periksa apakah setiap perintah:
  - Sintaksnya benar dan bisa dijalankan tanpa error di Git versi yang digunakan.
  - Menggunakan nama branch/file yang konsisten dengan konvensi yang ditetapkan di dokumen yang sama.
  - Tidak ada perintah yang berbahaya tanpa peringatan yang cukup (misal `--force`, `--hard`).

- [ ] **[T7-02]** **Validasi Diagram Mermaid**: Baca setiap blok kode `mermaid`. Periksa apakah:
  - Sintaks Mermaid valid (tidak ada node yang tidak tertutup, tidak ada edge yang mengarah ke node yang tidak terdefinisi).
  - Alur yang digambarkan konsisten dengan penjelasan prosedural di bab yang sama.
  - Nama branch/node menggunakan konvensi yang sama dengan bab lainnya.

- [ ] **[T7-03]** **Validasi Konsistensi Scope Commit**: Di Bab 5.3, terdapat 14 scope resmi commit: `transaksi`, `inventaris`, `ppob`, `sdm`, `antrian`, `keuangan`, `keamanan`, `crm`, `cabang`, `config`, `db`, `cli`, `middleware`, `utils`. Periksa:
  - Apakah ke-14 scope ini sudah cukup untuk mencakup **semua** jenis file yang ada di Module Structure R-03?
  - Apakah contoh commit di seluruh dokumen (Bab 5.6, Bab 6.2, dll.) sudah menggunakan scope yang terdefinisi — tidak ada scope "ilegal" yang dipakai di contoh tetapi tidak ada di daftar resmi.
  - Apakah scope `sdlc` (yang digunakan di Bab 5.7 untuk commit dokumen) sudah tercantum di daftar 14 scope resmi? Jika tidak, tambahkan.

- [ ] **[T7-04]** **Validasi Kebijakan Merge**: Periksa apakah seluruh aturan merge sudah konsisten di seluruh dokumen — tidak ada kontradiksi antara Bab 4.6 (Siklus Hidup Branch), Bab 6.2 (Langkah Operasional), Bab 7.1 (Kebijakan Merge), dan Bab 15 (Checklist).

- [ ] **[T7-05]** **Validasi Prosedur Backup**: Di Bab 11, perintah `git bundle` menggunakan path `exports/backups/abucom_repo_backup.bundle`. Periksa:
  - Apakah path ini konsisten dengan struktur direktori di R-03?
  - Apakah folder `exports/backups/` sudah tercantum di `.gitignore` (Bab 3.5)?
  - Apakah ada penjelasan enkripsi file bundle sebelum disimpan ke USB (mengingat R-06 menyebutkan enkripsi AES-256)?

- [ ] **[T7-06]** **Validasi Alur Kerja Hotfix**: Di Bab 6.5, prosedur hotfix disebutkan hanya 4 langkah singkat. Periksa apakah prosedur ini sudah cukup lengkap — apakah perlu ada langkah notifikasi ke seluruh AI developer bahwa hotfix sedang berjalan (untuk mencegah merge conflict)?

- [ ] **[T7-07]** **Validasi Identitas Git AI**: Di Bab 12.1, tabel identitas AI menggunakan email format `@abucom.local`. Periksa apakah format ini konsisten dengan spesifikasi di R-04 dan narasi R-07. Pastikan tidak ada AI yang namanya berbeda antara Bab 2.3 dan Bab 12.1.

- [ ] **[T7-08]** **Validasi Integrasi R-01 Bab 16**: Di Bab 14.1, disebutkan ada "10 Larangan Mutlak Coding Standard". Periksa apakah ke-10 larangan yang terdaftar di tabel dokumen utama sudah akurat, tidak ada yang missing, dan tidak ada yang berbeda dengan versi di R-01.

- [ ] **[T7-09]** **Validasi Scope `sdlc` dalam Commit**: Di Bab 5.7 disebutkan contoh `docs(sdlc): tambah berkas spesifikasi git workflow v1.1`. Namun scope `sdlc` tidak terdaftar dalam 14 scope resmi di Bab 5.3. Tandai ini sebagai inkonsistensi dan tambahkan `sdlc` ke daftar scope resmi jika memang dibutuhkan.

- [ ] **[T7-10]** **Validasi Folder `exports/handover/`**: Di Bab 12.4, disebutkan folder `/exports/handover/` dan dimasukkan ke `.gitignore`. Periksa apakah folder ini sudah tercantum di `.gitignore` Bab 3.5 dan apakah sudah ada entri `.gitkeep` untuk menjaga folder ini tetap ada di repositori.

- [ ] **[T7-11]** Buat **Daftar Temuan T7** — daftar semua masalah teknis spesifik. Format:
  ```
  [TEKNIS-T7-XXX] Lokasi: Bab A.B | Masalah Teknis: ... | Koreksi yang Harus Dilakukan: ...
  ```

---

### TAHAP 8 — Konsolidasi Seluruh Temuan

- [ ] **[T8-01]** Gabungkan seluruh Daftar Temuan dari T1 hingga T7 menjadi satu **Master List Temuan** yang terurut berdasarkan prioritas:
  - **KRITIS**: Temuan yang jika tidak diperbaiki akan menyebabkan kebingungan fatal atau kesalahan operasional (misal: perintah Git yang salah, scope commit yang tidak ada di daftar resmi).
  - **MAYOR**: Temuan yang mengurangi kelengkapan atau keandalan dokumen secara signifikan (misal: gap dari referensi PRIMER).
  - **MINOR**: Temuan yang bersifat penyempurnaan bahasa, konsistensi terminologi, atau kelengkapan contoh.

- [ ] **[T8-02]** Hitung total temuan per kategori. Catat ringkasan dalam format:
  ```
  Total Temuan KRITIS : X
  Total Temuan MAYOR  : Y
  Total Temuan MINOR  : Z
  Total Keseluruhan   : W
  ```

---

### TAHAP 9 — Penulisan Ulang Dokumen (Overwrite)

**Tujuan**: Menuangkan seluruh hasil validasi ke dokumen target dengan cara menimpa (overwrite) dokumen yang ada.

> **⚠️ PERINGATAN KRITIS**: Langkah ini adalah langkah penulisan ulang **PENUH**. Seluruh teks dari baris pertama hingga baris terakhir **HARUS** ditulis ulang sepenuhnya. **DILARANG KERAS** melakukan truncation, pemotongan, atau penghilangan bagian apa pun dari dokumen. Jika teks terlalu panjang, teruskan penulisan hingga selesai dalam satu operasi atau beberapa operasi yang sambung-menyambung tanpa gap.

- [ ] **[T9-01]** Buat draft dokumen baru yang sudah menerapkan seluruh perbaikan dari Master List Temuan T8. Draft ini adalah dokumen Git Workflow versi v1.2.

- [ ] **[T9-02]** Pastikan perubahan versi dokumen sudah diperbarui:
  - Header YAML frontmatter: `versi: 1.2`
  - Header YAML frontmatter: `tanggal: [tanggal hari pelaksanaan issue ini]`
  - Header YAML frontmatter: `status: Approved`
  - Tambahkan baris baru di tabel Riwayat Perubahan Dokumen untuk versi **v1.2** dengan deskripsi perubahan yang jelas mencakup seluruh temuan yang diperbaiki.

- [ ] **[T9-03]** Validasi draft sekali lagi sebelum menulis ke file:
  - Semua gap dari T1 sudah diisi.
  - Semua konten tidak relevan dari T2 sudah dihapus atau diganti referensi.
  - Semua masalah struktur dari T3 sudah diperbaiki.
  - Semua masalah kesiapan dari T4 sudah diperbaiki.
  - Semua masalah bahasa dari T5 sudah diperbaiki.
  - Semua placeholder dari T6 sudah diisi nilai konkret.
  - Semua masalah teknis dari T7 sudah dikoreksi.

- [ ] **[T9-04]** Tulis (overwrite) dokumen hasil validasi ke path target:
  ```
  docs/sdlc/04_implementation/04_git_workflow.md
  ```
  Gunakan operasi tulis file dari baris pertama hingga baris terakhir. **TIDAK BOLEH** ada bagian dokumen yang terpotong atau diringkas.

- [ ] **[T9-05]** Setelah penulisan selesai, baca ulang file yang baru ditimpa dari baris pertama hingga baris terakhir untuk memverifikasi bahwa:
  - Tidak ada baris yang terpotong di tengah kalimat.
  - Tidak ada bab yang hilang.
  - Tidak ada tabel yang tidak lengkap.
  - Versi sudah berubah menjadi v1.2.
  - Riwayat perubahan dokumen sudah diperbarui.

---

### TAHAP 10 — Pembaruan Referensi di Bab 16

- [ ] **[T10-01]** Setelah seluruh perbaikan selesai, periksa apakah selama proses perbaikan ada **dokumen referensi baru** yang ditambahkan atau dikutip dalam isi dokumen utama yang belum tercantum di Bab 16 (Referensi Dokumen).

- [ ] **[T10-02]** Jika ada dokumen referensi baru, tambahkan entri baru di tabel Bab 16 dengan mengisi semua kolom:
  - No (nomor urut)
  - Kode Ref (R-08, R-09, dst.)
  - Nama Dokumen Referensi
  - Path Relatif File
  - Versi
  - Prioritas (PRIMER / SEKUNDER / TERSIER)
  - Peran / Relevansi Spesifik

- [ ] **[T10-03]** Pastikan penambahan referensi baru ini sudah tercantum di **baris paling bawah** tabel Bab 16 (setelah entri R-07 yang sudah ada), bukan disisipkan di tengah-tengah tabel.

---

## 5. Kriteria Penyelesaian Issue (Definition of Done)

Issue ini dianggap **SELESAI** jika dan hanya jika seluruh kriteria berikut terpenuhi:

- [ ] Seluruh tahap T1 hingga T10 sudah dilaksanakan dan semua checkbox sudah ditandai `[x]`.
- [ ] File `docs/sdlc/04_implementation/04_git_workflow.md` sudah ditimpa (overwrite) dengan konten versi v1.2 yang lengkap dan penuh tanpa truncation.
- [ ] Versi dokumen di header YAML sudah berubah dari `1.1` menjadi `1.2`.
- [ ] Tabel Riwayat Perubahan Dokumen sudah memiliki entri baru untuk v1.2.
- [ ] Tidak ada satu pun item dari Master List Temuan yang belum diterapkan pada dokumen hasil.
- [ ] Dokumen hasil bisa dibaca dari baris 1 hingga baris terakhir tanpa ada baris yang terpotong, tabel yang tidak lengkap, atau bab yang hilang.
- [ ] Seluruh perintah Git di dokumen hasil sudah valid secara sintaksis dan menggunakan path/nama konkret AbuCom.
- [ ] Scope commit `sdlc` sudah ditambahkan ke daftar 14 scope resmi di Bab 5.3 (jika memang belum ada).
- [ ] Folder `exports/handover/` sudah tercantum di `.gitignore` Bab 3.5 (jika belum ada).
- [ ] Bab 16 (Referensi) sudah mencantumkan semua dokumen referensi yang benar-benar digunakan, termasuk dokumen baru jika ada.

---

## 6. Catatan Tambahan untuk Pelaksana

> **⚠️ PERINGATAN ANTI-HALUSINASI**: Jangan pernah mengisi data, nama file, nama modul, atau perintah Git dengan nilai yang tidak ada di dokumen referensi yang sudah kamu baca. Semua nilai harus dapat ditelusuri ke salah satu dokumen referensi R-01 hingga R-07 atau ke dokumen utama itu sendiri. Jika data tidak ditemukan, tandai sebagai `[PERLU KONFIRMASI MANUAL]` dan jangan mengarang nilai.

> **⚠️ ANTI-TRUNCATION**: Saat menulis ulang dokumen ke file target di T9-04, JANGAN pernah menghentikan penulisan di tengah jalan dengan alasan dokumen terlalu panjang. Jika sistem memiliki batas output, pecah penulisan menjadi beberapa segmen yang sambung-menyambung dan pastikan setiap segmen dimulai dari baris tepat setelah baris terakhir yang berhasil ditulis sebelumnya.

> **📌 URUTAN PRIORITAS**: Jika menemukan konflik antara isi dokumen utama dan isi referensi PRIMER (R-01 atau R-02), selalu utamakan referensi PRIMER. Jika konflik antara dua referensi PRIMER, prioritaskan R-01 (Coding Standard) untuk hal-hal teknis coding, dan R-02 (Environment Setup) untuk hal-hal konfigurasi sistem.

> **📌 SCOPE `sdlc`**: Scope `sdlc` untuk commit dokumen SDLC adalah scope yang sah dan perlu ditambahkan ke daftar resmi scope commit di Bab 5.3 jika belum ada. Ini bukan scope ilegal — ini adalah kebutuhan nyata karena dokumen SDLC dikelola dalam repositori yang sama.

---

## 7. Referensi Issue Terkait

| No | ID Issue | Judul | Relevansi |
|:--:|:---------|:------|:----------|
| 1  | —        | —     | Issue ini adalah issue pertama dalam seri validasi fase 04 Implementation untuk dokumen Git Workflow. |

---

*Issue dibuat oleh: Principal DevOps Architect & Technical Documentation Auditor*
*Tanggal: 2026-05-29*
*Untuk pelaksanaan oleh: Junior Programmer / LLM AI Model*
