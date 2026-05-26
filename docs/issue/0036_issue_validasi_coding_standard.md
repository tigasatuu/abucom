# Validasi, Komparasi, dan Penyempurnaan Dokumen Coding Standard

---

## Metadata Issue

| Field          | Nilai                                                              |
| -------------- | ------------------------------------------------------------------ |
| **Judul**      | Validasi, Komparasi Mendalam, dan Penyempurnaan Dokumen Coding Standard |
| **Target File**| `docs/sdlc/04_implementation/01_coding_standard.md`               |
| **Prioritas**  | 🔴 Tinggi                                                          |
| **Status**     | 🟡 Open                                                            |
| **Tanggal**    | 2026-05-26                                                         |
| **Assignee**   | Junior Programmer / AI Model                                       |

---

## 1. Persona yang Harus Digunakan

**Sebelum memulai pekerjaan apapun**, adopsi dan pertahankan persona berikut ini sepanjang seluruh proses validasi:

> **Persona: Principal Software Engineering Standards Architect & Python Code Quality Lead**
>
> Kamu adalah seorang **Principal Software Engineer** dengan spesialisasi di bidang:
> - **Code Quality & Standards Enforcement** untuk sistem Python Functional Programming (FP) skala produksi.
> - **SDLC Documentation Auditor** yang terbiasa memvalidasi dokumen standar pengkodean industri (ISO 9001, CMMI Level 3+).
> - **Financial Systems Security Specialist** yang paham konsekuensi teknis dari standar yang tidak ketat terhadap integritas data keuangan.
> - **Python 3.14+ Expert** dengan penguasaan mendalam terhadap PEP 8, PEP 257, PEP 484, paradigma FP murni, arsitektur berlapis, dan keamanan aplikasi.
>
> Kamu **tidak mentoleransi** ambiguitas, celah standar, data kosong, informasi yang tidak konsisten, atau dokumen yang tidak layak dijadikan referensi teknis untuk fase SDLC berikutnya. Kamu akan memeriksa setiap baris dokumen dengan ketelitian seorang auditor teknis bersertifikat.

---

## 2. Latar Belakang dan Konteks Issue

Dokumen **Coding Standard** (`docs/sdlc/04_implementation/01_coding_standard.md`) adalah deliverable pertama pada **Fase 04 — Implementation** dalam SDLC proyek AbuCom. Dokumen ini berfungsi sebagai:

- **Acuan mutlak** bagi seluruh generasi kode Python yang akan ditulis oleh Junior Programmer atau AI Model.
- **Instruksi pengkodean** yang ditransformasi dari hasil rancangan di Fase 03 (System Design).
- **Kontrak kualitas kode** yang memastikan integritas finansial, keamanan, portabilitas, dan kemudahan pemeliharaan sistem.

Dokumen ini **HARUS** divalidasi secara menyeluruh sebelum fase konstruksi kode dimulai, agar tidak ada standar yang ambigu, tidak konsisten, atau tidak lengkap yang dapat menghambat proses implementasi.

---

## 3. Daftar File yang Wajib Dibaca

Sebelum memulai validasi apapun, **baca dan pahami seluruh file berikut secara lengkap dari baris pertama hingga terakhir**:

### 3.1. File Target (Dokumen Utama yang Divalidasi)
- [ ] **Baca** `docs/sdlc/04_implementation/01_coding_standard.md` — Dokumen utama yang menjadi objek validasi.

### 3.2. File Referensi Primer (Prioritas Baca Tertinggi)
- [ ] **Baca** `docs/sdlc/01_planning/04_tech_stack_decision.md` — SSoT Python 3.14.2+, dependensi terkunci, dual-OS.
- [ ] **Baca** `docs/sdlc/03_design/03_system_architecture.md` — Blueprint arsitektur 4-layer, ACID, connection pool.
- [ ] **Baca** `docs/sdlc/03_design/06_security_design.md` — Spesifikasi bcrypt, JWT, RBAC, UU PDP, audit trail.

### 3.3. File Referensi Sekunder (Prioritas Baca Menengah)
- [ ] **Baca** `docs/sdlc/03_design/05_bom_hpp_design.md` — Pseudocode FP murni, NamedTuple, desimal.
- [ ] **Baca** `docs/sdlc/03_design/04_cli_interaction_flow.md` — Standar visual CLI, warna ANSI, navigasi, error codes.
- [ ] **Baca** `docs/sdlc/02_analysis/02_software_requirements.md` — Spesifikasi non-fungsional, target performa, code coverage.

### 3.4. File Referensi Tersier (Prioritas Baca Pelengkap)
- [ ] **Baca** `docs/sdlc/03_design/01_database_schema.sql` — Konvensi penamaan tabel/kolom MySQL, DDL, InnoDB.
- [ ] **Baca** `docs/sdlc/03_design/02_erd_database.md` — Entity mapping Python ↔ Database.

> **⚠️ PENTING**: Jangan melewati satupun file di atas. Pembacaan yang tidak lengkap akan menyebabkan validasi yang tidak akurat dan bias.

---

## 4. Instruksi Validasi — Tahapan Demi Tahapan

Lakukan seluruh tahapan validasi berikut ini secara **berurutan** dari Tahap A hingga Tahap I. **Jangan melompati tahapan apapun**. Catat seluruh temuan pada setiap tahap di dalam memori kerja sebelum melanjutkan ke tahap berikutnya.

---

### TAHAP A — Komparasi Mendalam: Dokumen Utama vs. File Referensi

**Tujuan**: Memastikan setiap klaim, aturan, angka, nama fungsi, atau standar teknis yang ditulis di dokumen utama **bersumber dan konsisten** dengan data yang ada di file-file referensi.

#### Instruksi Teknis:

- [ ] **A.1.** Buka dokumen utama (`01_coding_standard.md`) dan file `04_tech_stack_decision.md` secara berdampingan.
  - Verifikasi: Apakah **versi Python (3.14.2+)** yang disebutkan di dokumen utama konsisten dengan Tech Stack Decision?
  - Verifikasi: Apakah **versi seluruh library** (mysql-connector-python, python-dotenv, bcrypt, pyjwt, rich, tabulate) di Bab 13 dokumen utama cocok tepat dengan versi yang ditetapkan di Tech Stack Decision?
  - Verifikasi: Apakah **strategi dual-OS (Windows 11 & Linux Debian 12)** sudah dipetakan dengan benar ke aturan di Bab 12?
  - Catat: Setiap versi library yang berbeda, hilang, atau tidak dikonfirmasi.

- [ ] **A.2.** Buka dokumen utama dan file `03_system_architecture.md` secara berdampingan.
  - Verifikasi: Apakah **arsitektur 4-layer** (`cli/` → `logic/` → `db/` → MySQL) di Bab 8 dokumen utama sesuai dengan blueprint arsitektur?
  - Verifikasi: Apakah **nama folder dan file** di Bab 4 (layout direktori) identik 100% dengan yang ada di System Architecture?
  - Verifikasi: Apakah **spesifikasi connection pool** (`pool_size=5`, `pool_name="abupool"`) konsisten?
  - Verifikasi: Apakah **retry mechanism** (exponential backoff, 3 kali percobaan, error code 2006 & 2013) sudah dijabarkan lengkap di Bab 9?
  - Verifikasi: Apakah **modul-modul bisnis (M.1 s.d. M.10)** yang disebutkan di layout direktori sudah mencakup seluruh modul yang ada di System Architecture? Cek apakah ada modul yang hilang dari layout folder di Bab 4.
  - Catat: Setiap ketidakkonsistenan nama, angka, atau konsep.

- [ ] **A.3.** Buka dokumen utama dan file `06_security_design.md` secara berdampingan.
  - Verifikasi: Apakah **bcrypt cost factor (12)** di Bab 10.2 konsisten dengan Security Design?
  - Verifikasi: Apakah **JWT HS256, masa aktif 8 jam (28.800 detik)** di Bab 10.3 konsisten?
  - Verifikasi: Apakah **RBAC Matrix** di Bab 10.4 — apakah semua `menu_id` yang tercantum di kode contoh (`MENU-M1-001`, dst.) konsisten dengan matriks otorisasi di Security Design?
  - Verifikasi: Apakah **Fernet key 32-byte** untuk enkripsi WhatsApp di Bab 10.7 sudah disebutkan dengan benar, konsisten dengan Security Design?
  - Verifikasi: Apakah **audit trail schema** (field `old_value`, `new_value`, tabel `audit_logs`) di Bab 10.6 konsisten dengan DDL database dan Security Design?
  - Verifikasi: Apakah **sanitasi input** (karakter di bawah `\x20`) di Bab 10.5 sesuai dengan spesifikasi di Security Design?
  - Verifikasi: Apakah **rate limiting & brute-force lockout** (yang ada di Security Design) sudah tercermin dalam standar di dokumen utama?
  - Catat: Setiap spesifikasi keamanan yang belum terwakili di dokumen utama.

- [ ] **A.4.** Buka dokumen utama dan file `05_bom_hpp_design.md` secara berdampingan.
  - Verifikasi: Apakah **NamedTuple pattern** (`BOMItem`, `KalkulasiResult`) di contoh kode Bab 8.3 dan 7.4 konsisten dengan nama dan field yang digunakan di BOM & HPP Design?
  - Verifikasi: Apakah **`ROUND_HALF_UP`** sebagai standar pembulatan desimal disebutkan secara eksplisit di Bab 2.4 (bukan hanya `quantize`)? Verifikasi apakah BOM & HPP Design juga menggunakan standar yang sama.
  - Verifikasi: Apakah **contoh kode fungsi** di Bab 7.4 (`proses_kalkulasi_hpp`) sudah menggunakan `ROUND_HALF_UP` secara eksplisit, atau hanya `quantize` saja?
  - Catat: Setiap inkonsistensi pseudocode atau naming convention.

- [ ] **A.5.** Buka dokumen utama dan file `04_cli_interaction_flow.md` secara berdampingan.
  - Verifikasi: Apakah **format error code** (`ERR-[KATEGORI]-[NOMOR]`) di Bab 11.5 konsisten dengan daftar error code yang ada di CLI Interaction Flow?
  - Verifikasi: Apakah **hotkey `0` untuk back** dan **breadcrumb navigation** di Bab 11.3 sesuai dengan ketentuan di CLI Interaction Flow?
  - Verifikasi: Apakah **warna ANSI** (Hijau/Merah/Kuning/Biru) di Bab 11.1 sesuai dan lengkap dengan standar warna yang ditetapkan di CLI Interaction Flow?
  - Verifikasi: Apakah ada **konvensi CLI lainnya** yang ada di `04_cli_interaction_flow.md` namun belum tercakup di Bab 11 dokumen utama?
  - Catat: Setiap konvensi CLI yang hilang atau tidak konsisten.

- [ ] **A.6.** Buka dokumen utama dan file `02_software_requirements.md` secara berdampingan.
  - Verifikasi: Apakah **target code coverage ≥ 90%** di Bab 14.2 sesuai dengan spesifikasi SRS?
  - Verifikasi: Apakah ada persyaratan **non-fungsional lain** dari SRS (performa, skalabilitas, ketersediaan) yang relevan dan seharusnya tercermin di Coding Standard namun belum ada?
  - Catat: Setiap requirement non-fungsional yang seharusnya mendapat aturan coding namun terlewat.

- [ ] **A.7.** Buka dokumen utama dan file `01_database_schema.sql` serta `02_erd_database.md` secara berdampingan.
  - Verifikasi: Apakah **nama tabel dan nama kolom** yang disebutkan di dokumen utama (contoh: `pengguna`, `failed_login_attempts`, `audit_logs`, `pelanggan`) identik 100% dengan nama yang ada di DDL SQL?
  - Verifikasi: Apakah **tipe data `DECIMAL(15,4)`** di Bab 9.7 sesuai dengan deklarasi kolom di DDL SQL?
  - Catat: Setiap nama tabel/kolom yang tidak konsisten atau berbeda.

---

### TAHAP B — Validasi Kelengkapan: Apakah Ada Yang Terlewat?

**Tujuan**: Memastikan dokumen utama telah **merangkum semua data dan informasi penting** dari seluruh file referensi yang relevan bagi coding standard, tidak ada yang terlewat.

#### Instruksi Teknis:

- [ ] **B.1.** Periksa apakah **standar penanganan `ROUND_HALF_UP`** diimplementasikan secara eksplisit di setiap contoh kode Decimal di dokumen utama (bukan hanya disebutkan di Bab 2.4). Jika ada contoh kode yang hanya menggunakan `quantize()` tanpa `ROUND_HALF_UP`, tandai sebagai temuan.

- [ ] **B.2.** Periksa apakah **mekanisme brute-force lockout** (misalnya: kolom `failed_login_attempts`, `lockout_until` di tabel `pengguna`) dari Security Design sudah memiliki aturan pengkodean yang eksplisit di dokumen utama. Jika tidak ada, tandai sebagai temuan.

- [ ] **B.3.** Periksa apakah **standar penulisan kode untuk backup terenkripsi** (`AES-256` di `utils/backup.py`) sudah memiliki sub-bab atau aturan coding di dokumen utama. Jika tidak ada, tandai sebagai temuan.

- [ ] **B.4.** Periksa apakah **10 modul bisnis (M.1 s.d. M.10)** yang disebutkan di System Architecture semuanya terwakili atau ada yang hilang dari layout direktori di Bab 4 (hanya M.1, M.2, M.3, M.4, M.6 yang terlihat di layout `cli/`).

- [ ] **B.5.** Periksa apakah **standar penamaan & format modul `config/`** (yang disebutkan di Bab 1.4 sebagai penerima manfaat: `config/`) memiliki aturan coding-nya sendiri atau penjelasan kontennya di dokumen utama.

- [ ] **B.6.** Periksa apakah ada **standar penulisan file `main.py`** (entry point aplikasi) yang dibutuhkan, seperti bagaimana inisialisasi pool database, loading `.env`, dan startup validation harus dilakukan.

- [ ] **B.7.** Periksa apakah **standar `frozen=True` dataclass** (yang disebut di Bab 3.5 sebagai alternatif NamedTuple) sudah dicontohkan penggunaannya atau dijelaskan kapan menggunakannya vs. NamedTuple.

- [ ] **B.8.** Periksa apakah **standar penulisan `__init__.py`** untuk setiap package (selain disebutkan wajib ada) sudah dijelaskan isinya (apakah harus kosong, atau boleh berisi re-export).

- [ ] **B.9.** Periksa apakah **penanganan `csv` bulk import** (Bab 13.4 menyebut `csv` sebagai modul yang dimanfaatkan) sudah memiliki aturan pengkodeannya sendiri (misalnya: encoding, delimiter, validasi baris per baris).

- [ ] **B.10.** Periksa apakah **standar error code untuk setiap kategori** (`ERR-STOCK-`, `ERR-DB-`, `ERR-AUTH-`, `ERR-FILE-`, dst.) sudah didefinisikan secara lengkap atau hanya dicontohkan sporadis.

---

### TAHAP C — Validasi Relevansi dan Fokus: Apakah Ada Data yang Tidak Relevan?

**Tujuan**: Memastikan dokumen utama **hanya memuat informasi yang memang merupakan standar pengkodean**. Tidak ada informasi yang seharusnya menjadi ranah dokumen lain (misalnya: spesifikasi bisnis, wireframe, atau deskripsi fitur).

#### Instruksi Teknis:

- [ ] **C.1.** Baca ulang Bab 4 (Struktur Direktori). Periksa apakah deskripsi direktori di Bab 4.2 terlalu panjang menjabarkan logika bisnis, atau cukup menjelaskan tanggung jawab layer. Jika ada deskripsi yang lebih cocok berada di System Architecture, tandai.

- [ ] **C.2.** Baca ulang Bab 8 (Arsitektur Kode). Periksa apakah Bab 8 sudah dalam batas "standar coding" dan tidak terlalu dalam masuk ke wilayah "architecture decision" yang seharusnya ada di System Architecture. Tentukan apakah setiap sub-bab di Bab 8 adalah **aturan coding** (cara menulis kode) bukan **desain arsitektur** (alasan arsitektural).

- [ ] **C.3.** Baca ulang Bab 10 (Secure Coding Standard). Periksa apakah ada spesifikasi keamanan yang sifatnya **desain** (yang seharusnya ada di Security Design) bukan **coding standard** (cara mengimplementasikan keamanan dalam kode). Pertahankan hanya aturan "bagaimana cara menulis kode keamanan yang benar".

- [ ] **C.4.** Periksa apakah seluruh **contoh kode (code snippet)** yang ada di dokumen ini memang merupakan contoh implementasi, bukan pseudocode fiktif yang tidak bisa dijalankan. Pastikan setiap contoh kode secara sintaksis valid untuk Python 3.14.2+.

- [ ] **C.5.** Periksa apakah **Bab 15 (Version Control)** cukup relevan sebagai bagian dari Coding Standard, atau apakah ada konten di dalamnya yang lebih tepat berada di dokumen terpisah (misalnya: Contribution Guide). Tentukan sub-bab mana yang harus dipertahankan dan mana yang bisa dipangkas atau dipindahkan.

---

### TAHAP D — Validasi Struktur Dokumen: Apakah Struktur Sudah Standar Industri?

**Tujuan**: Memastikan dokumen ini memiliki **struktur, hierarki heading, dan kelengkapan metadata** yang setara dengan dokumen coding standard di industri profesional.

#### Instruksi Teknis:

- [ ] **D.1.** Verifikasi apakah **frontmatter YAML** di bagian atas dokumen sudah lengkap dan informasinya akurat (dokumen, proyek, versi, tanggal, status, penyusun).

- [ ] **D.2.** Verifikasi apakah **Riwayat Perubahan Dokumen** (change log) format tabelnya sudah benar dan setiap kolom terisi dengan informasi yang spesifik (bukan generik).

- [ ] **D.3.** Verifikasi apakah **urutan hierarki bab** sudah logis dan mengalir dari umum ke khusus:
  - Informasi Dokumen → Prinsip Dasar → Konvensi Penamaan → Struktur Direktori → Gaya Kode → Dokumentasi → Type Hints → Arsitektur → Database → Keamanan → CLI → Portabilitas → Dependensi → Testing → Version Control → Larangan → Checklist → Referensi
  - Jika ada bab yang urutan logisnya tidak tepat, tandai dan usulkan urutan yang lebih baik.

- [ ] **D.4.** Verifikasi apakah setiap bab memiliki **tingkat kedalaman yang seimbang** (tidak ada bab yang terlalu dangkal hanya berisi 1-2 baris, sementara bab lain sangat panjang). Identifikasi bab yang perlu diperluas.

- [ ] **D.5.** Verifikasi apakah **label compliance level** (`[WAJIB]`, `[DILARANG]`, `[DIREKOMENDASIKAN]`, `[OPSIONAL]`) digunakan secara konsisten di setiap aturan di seluruh dokumen, tidak ada aturan yang "mengambang" tanpa label.

- [ ] **D.6.** Verifikasi apakah **diagram Mermaid** di Bab 8.1 dapat dirender dengan benar (sintaksis valid, tidak ada karakter khusus yang merusak). Jika ada masalah, perbaiki.

- [ ] **D.7.** Verifikasi apakah **diagram teks ASCII** di Bab 1.3 (posisi dokumen dalam SDLC) sudah akurat mencerminkan posisi dokumen ini, dan apakah perlu ditambahkan visualisasi tambahan di bab lain.

- [ ] **D.8.** Verifikasi apakah **Checklist Kepatuhan** di Bab 17 sudah mencakup semua aturan `[WAJIB]` yang disebutkan di seluruh bab. Hitung jumlah item `[WAJIB]` di seluruh dokumen, lalu bandingkan dengan jumlah item di Checklist. Jika ada yang terlewat, tambahkan.

- [ ] **D.9.** Verifikasi apakah **Tabel Referensi Dokumen** di Bab 18 sudah mencantumkan semua file referensi yang benar-benar digunakan sebagai acuan di dalam teks dokumen (cross-reference antara teks dan tabel referensi).

---

### TAHAP E — Validasi Kelayakan sebagai Acuan Fase SDLC Berikutnya

**Tujuan**: Memastikan dokumen ini **cukup lengkap, konkret, dan tidak ambigu** untuk dijadikan instruksi langsung oleh Junior Programmer atau AI Model dalam menghasilkan kode Python produksi.

#### Instruksi Teknis:

- [ ] **E.1.** Uji simulasi: Ambil satu skenario implementasi, misalnya **"Membuat fungsi hitung_hpp_bom di logic/bom_hpp.py"**. Periksa apakah dengan hanya membaca dokumen Coding Standard ini (tanpa membaca file referensi lain), seorang Junior Programmer dapat mengetahui: (a) format nama fungsi, (b) tipe data parameter, (c) format return type, (d) format docstring, (e) cara menangani error, (f) di file mana harus ditempatkan. Jika ada informasi yang tidak bisa ditemukan hanya dari dokumen ini, tandai sebagai gap.

- [ ] **E.2.** Uji simulasi: Ambil skenario implementasi **"Membuat file db/db_connector.py"**. Periksa apakah dokumen ini memberikan instruksi yang cukup tentang: (a) format header file, (b) cara inisialisasi connection pool, (c) cara implementasi retry mechanism, (d) cara menangani error koneksi. Tandai gap jika ada.

- [ ] **E.3.** Uji simulasi: Ambil skenario implementasi **"Membuat endpoint autentikasi login di middleware/auth_jwt.py"**. Periksa apakah dokumen ini memberikan instruksi yang cukup tentang: (a) cara hash password dengan bcrypt, (b) cara generate JWT token, (c) cara verifikasi token, (d) cara implementasi rate limiting. Tandai gap jika ada.

- [ ] **E.4.** Periksa apakah setiap **contoh kode** di dokumen ini sudah dilengkapi penjelasan kontekstual yang cukup (tidak hanya kode mentah tanpa narasi). Pastikan setiap blok kode memiliki komentar inline yang menjelaskan baris-baris kritisnya.

- [ ] **E.5.** Periksa apakah ada **aturan yang saling bertentangan** di dalam dokumen ini. Misalnya: di satu tempat disebutkan "gunakan `namedtuple`", di tempat lain disebutkan "gunakan `frozen dataclass`" tanpa panduan kapan menggunakan masing-masing. Jika ada ambiguitas, perjelas dengan menambahkan panduan kapan menggunakan masing-masing pilihan.

---

### TAHAP F — Validasi Bahasa Indonesia: Natural, Tidak Ambigu, Mudah Dipahami

**Tujuan**: Memastikan seluruh teks naratif ditulis dalam Bahasa Indonesia yang **baku, natural, tidak ambigu**, dan mudah dipahami oleh Junior Programmer awam atau AI Model bahasa kecil.

#### Instruksi Teknis:

- [ ] **F.1.** Baca ulang seluruh kalimat naratif (bukan kode) di setiap bab. Identifikasi kalimat yang:
  - Terlalu panjang dan sulit dipahami sekali baca (lebih dari 40 kata dalam satu kalimat).
  - Menggunakan istilah teknis tanpa penjelasan dan tidak ada di Bab 1.6 (Definisi & Akronim).
  - Mencampur Bahasa Indonesia dan Bahasa Inggris dalam satu kalimat tanpa keperluan yang jelas.
  - Ambigu atau bisa ditafsirkan dengan lebih dari satu cara.

- [ ] **F.2.** Periksa apakah **Bab 1.6 (Definisi, Akronim, dan Singkatan)** sudah mencakup semua istilah teknis yang digunakan di seluruh dokumen. Daftar istilah yang mungkin perlu ditambahkan: `SSoT`, `ACID`, `InnoDB`, `DDL`, `DML`, `ANSI`, `CLI`, `BOM`, `HPP`, `ATK`, `LAN`, `PEP`, `HOF`, `CRUD`, dsb.

- [ ] **F.3.** Periksa konsistensi penggunaan kata ganti dan istilah:
  - Apakah "program" vs. "aplikasi" vs. "sistem" digunakan secara konsisten?
  - Apakah "berkas" vs. "file" vs. "dokumen" digunakan secara konsisten?
  - Apakah "staf" vs. "karyawan" vs. "pengguna" digunakan secara konsisten?
  - Apakah "basis data" vs. "database" digunakan secara konsisten?

- [ ] **F.4.** Periksa apakah **penulisan singkatan dan akronim** mengikuti kaidah (pertama kali muncul ditulis lengkap, kemudian disingkat dalam tanda kurung). Misalnya: "Functional Programming (FP)" pertama kali, lalu "FP" saja setelahnya.

- [ ] **F.5.** Periksa apakah **label aturan** (`[WAJIB]`, `[DILARANG]`, `[DIREKOMENDASIKAN]`, `[OPSIONAL]`) digunakan dengan benar sesuai definisi RFC 2119 yang sudah ditetapkan di Bab 1.7.

---

### TAHAP G — Validasi Anti-Interupsi: Dokumen Tidak Akan Selalu Dipertanyakan

**Tujuan**: Memastikan dokumen ini **mandiri** (self-contained) dan tidak akan menimbulkan pertanyaan berulang yang menghambat proses implementasi.

#### Instruksi Teknis:

- [ ] **G.1.** Identifikasi setiap aturan yang **tidak disertai justifikasi teknis** (mengapa aturan ini ada). Untuk setiap aturan `[WAJIB]` yang belum memiliki kalimat justifikasi, tambahkan minimal satu kalimat justifikasi singkat.

- [ ] **G.2.** Identifikasi setiap aturan yang **tidak disertai contoh kode** padahal contoh kode diperlukan untuk menghilangkan ambiguitas. Prioritaskan:
  - Aturan yang bersifat "bagaimana cara melakukan X" (how-to) → wajib ada contoh kode.
  - Aturan yang bersifat "jangan lakukan X" (prohibition) → wajib ada contoh kode salah (❌) dan benar (✅).

- [ ] **G.3.** Identifikasi setiap **referensi silang (cross-reference)** ke dokumen lain yang format linknya tidak konsisten atau path-nya salah. Format yang benar: `[Nama Dokumen](path/relatif/ke/file.md)`. Perbaiki semua link yang tidak valid.

- [ ] **G.4.** Identifikasi apakah ada **pertanyaan yang mungkin akan selalu diajukan** oleh Junior Programmer atau AI Model:
  - "Kapan menggunakan `namedtuple` vs `frozen dataclass`?"
  - "Bagaimana format pesan error yang benar untuk setiap kategori error?"
  - "Apa yang harus saya lakukan jika koneksi database gagal lebih dari 3 kali?"
  - "Bagaimana cara menulis fungsi yang membutuhkan lebih dari 5 parameter?"
  - Jika pertanyaan-pertanyaan ini tidak terjawab di dokumen, tambahkan jawabannya.

- [ ] **G.5.** Verifikasi apakah **Bab 16 (Daftar Larangan Mutlak)** sudah mencakup semua larangan kritis. Periksa apakah ada larangan penting yang disebutkan di bab-bab lain namun tidak masuk ke tabel Bab 16.

- [ ] **G.6.** Verifikasi apakah **Bab 17 (Checklist Kepatuhan)** bisa benar-benar dijadikan checklist sebelum code merge, atau masih terlalu generik. Setiap item checklist harus dapat dijawab dengan "Ya" atau "Tidak" secara biner, tanpa interpretasi.

---

### TAHAP H — Validasi Data Kosong dan Pengisian Otomatis

**Tujuan**: Memastikan **tidak ada placeholder kosong, `TBD`, `TODO`, atau data yang belum diisi** di seluruh dokumen.

#### Instruksi Teknis:

- [ ] **H.1.** Lakukan pencarian (`Ctrl+F` atau grep) terhadap kata kunci berikut di seluruh dokumen:
  - `TBD`, `TODO`, `FIXME`, `[...]`, `[diisi kemudian]`, `[placeholder]`, `???`, `N/A` (jika ada yang belum terisi)
  - Jika ditemukan, isi dengan data yang sesuai, relevan, dan masih dalam ruang lingkup dokumen coding standard ini.

- [ ] **H.2.** Periksa **Tabel Ringkasan Konvensi Penamaan** di Bab 3.8. Pastikan semua entitas kode yang relevan sudah ada dalam tabel (periksa apakah ada entitas yang disebutkan di Bab 3 namun tidak ada di tabel ringkasan).

- [ ] **H.3.** Periksa apakah **semua contoh error code** yang disebutkan sudah memiliki nomor yang konsisten dan tidak ada duplikasi. Buat tabel referensi error code jika belum ada.

- [ ] **H.4.** Periksa apakah **contoh kode di Bab 8.8 (ACID Transaction Boilerplate)** sudah menggunakan `from typing import Any` secara eksplisit, karena `Any` digunakan dalam type hints fungsi `execute_acid_transaction`. Jika ada import yang hilang dalam contoh kode, tambahkan.

- [ ] **H.5.** Periksa apakah **field `status` di frontmatter** masih bernilai `Draft`. Jika dokumen sudah divalidasi dan siap digunakan, pertimbangkan untuk mengubah ke `Active` atau `Approved`.

---

### TAHAP I — Verifikasi Kualitas Spesifik Dokumen Coding Standard

**Tujuan**: Melakukan pengecekan akhir terhadap aspek-aspek yang **khas** untuk sebuah dokumen Coding Standard profesional.

#### Instruksi Teknis:

- [ ] **I.1.** Verifikasi bahwa setiap **contoh kode Python** di seluruh dokumen menggunakan Python 3.14.2+ syntax yang valid:
  - Tidak ada penggunaan `typing.List`, `typing.Dict`, `typing.Tuple` (sudah deprecated di Python 3.9+; gunakan `list[...]`, `dict[...]`, `tuple[...]`).
  - Tidak ada penggunaan `Union[X, Y]` (gunakan `X | Y` di Python 3.10+).
  - Catatan: Di Bab 8.8 terdapat `from typing import Callable, list` — ini salah, `list` adalah built-in, bukan dari `typing`. Ini HARUS diperbaiki.

- [ ] **I.2.** Verifikasi bahwa **`ROUND_HALF_UP`** diimpor dari `decimal` dan digunakan secara eksplisit di setiap contoh kode yang menggunakan `quantize()`:
  ```python
  # Contoh yang benar:
  from decimal import Decimal, ROUND_HALF_UP
  nilai.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
  ```
  Perbaiki semua contoh kode yang hanya menggunakan `quantize(Decimal('0.0001'))` tanpa `ROUND_HALF_UP`.

- [ ] **I.3.** Verifikasi bahwa **contoh `session_state` dictionary** di Bab 8.4 konsisten dengan field-field yang disebutkan di Security Design (misalnya: apakah perlu field `exp` untuk expiry JWT? Apakah field `cabang_id` sudah sesuai dengan skema database?).

- [ ] **I.4.** Verifikasi bahwa **matriks RBAC** di Bab 10.4 hanya berisi contoh, bukan matriks lengkap. Tambahkan catatan eksplisit bahwa matriks lengkap ada di `06_security_design.md` dan fungsi `check_permission()` harus membaca matriks dari sumber terpusat, bukan hardcode di dalam fungsi (karena ini bertentangan dengan prinsip SRP dan maintainability).

- [ ] **I.5.** Verifikasi bahwa **standar penanganan `NULL` dari database MySQL** ke Python sudah dibahas. Kolom MySQL yang bernilai `NULL` akan menjadi `None` di Python — apakah ada aturan eksplisit tentang bagaimana menangani `None` dari query hasil database?

- [ ] **I.6.** Verifikasi apakah ada standar untuk **pengelolaan konfigurasi runtime** (selain `.env`): misalnya apakah ada berkas `config/settings.py` yang mengagregasi semua konfigurasi dari `.env`? Jika iya, bagaimana standar penulisannya?

- [ ] **I.7.** Verifikasi apakah **standar logging aplikasi** (selain audit trail transaksional di Bab 10.6) sudah ada. Misalnya: apakah ada standar untuk debug logging, info logging, atau error logging menggunakan modul `logging` Python standar?

---

## 5. Instruksi Penulisan Ulang Dokumen

Setelah seluruh Tahap A hingga I selesai dilakukan dan semua temuan sudah terkumpul, lakukan penulisan ulang dokumen.

### 5.1. Pra-Penulisan Ulang

- [ ] **Pre-1.** Susun daftar temuan dari Tahap A s.d. I secara terstruktur dalam memori kerja sebelum mulai menulis.
- [ ] **Pre-2.** Kelompokkan temuan berdasarkan jenis: (a) Inkonsistensi data, (b) Informasi hilang/kurang, (c) Kesalahan sintaksis kode, (d) Masalah bahasa, (e) Masalah struktur dokumen.
- [ ] **Pre-3.** Buat daftar perubahan yang akan dilakukan (change summary) sebelum memulai penulisan ulang. Ini akan dimasukkan ke bagian Riwayat Perubahan Dokumen.

### 5.2. Aturan Penulisan Ulang (WAJIB DIPATUHI TANPA PENGECUALIAN)

> **⛔ PERHATIAN KRITIS**: Seluruh aturan di bawah ini bersifat MUTLAK dan TIDAK DAPAT DINEGOSIASIKAN.

- [ ] **Write-1.** Tulis ulang seluruh dokumen ke file target yang SAMA dengan cara **menimpa (overwrite)** file lama:
  - **Path file target**: `docs/sdlc/04_implementation/01_coding_standard.md`
  - **Tidak boleh** membuat file baru dengan nama berbeda.
  - **Tidak boleh** menyimpan di lokasi lain.

- [ ] **Write-2.** **SELURUH TEKS** dari baris pertama (frontmatter `---`) hingga baris terakhir (baris terakhir Bab 18) **HARUS DITULIS ULANG SEPENUHNYA** tanpa perkecualian.
  - **DILARANG KERAS**: Memotong isi dokumen (`[...truncated...]`).
  - **DILARANG KERAS**: Meringkas bagian dokumen yang dianggap tidak berubah.
  - **DILARANG KERAS**: Menghilangkan bagian apapun dari dokumen asli yang valid dan tidak perlu dihapus.
  - **DILARANG KERAS**: Menulis output sebagian dan meminta konfirmasi untuk melanjutkan.
  - **WAJIB**: Tulis dari baris 1 hingga baris terakhir dalam satu output penuh dan kontinu.

- [ ] **Write-3.** **Ubah versi dokumen** dari `v1.0` menjadi `v1.1` di:
  - Field `versi` di frontmatter YAML.
  - Tabel Riwayat Perubahan Dokumen (tambahkan baris baru untuk v1.1).
  - Diagram teks ASCII di Bab 1.3 (ubah label `Coding Standard v1.0` menjadi `v1.1`).

- [ ] **Write-4.** **Tambahkan entri baru** di tabel **Riwayat Perubahan Dokumen** untuk v1.1 dengan format:
  - Versi: `1.1`
  - Tanggal: (tanggal hari ini saat melakukan validasi)
  - Perubahan: Deskripsi singkat namun spesifik dari seluruh perubahan yang dilakukan (berdasarkan daftar temuan dari Pra-Penulisan Ulang).
  - Oleh: `Principal Software Engineering Standards Architect & FP Code Quality Lead`

- [ ] **Write-5.** **Ubah field `tanggal`** di frontmatter menjadi tanggal hari ini.

- [ ] **Write-6.** **Terapkan semua perbaikan** dari Tahap A s.d. I secara menyeluruh ke seluruh teks dokumen.

- [ ] **Write-7.** **Pertahankan seluruh format Markdown** yang sudah ada (heading levels, bold/italic, code blocks, tables, mermaid diagrams, checklist items) kecuali ada format yang memang perlu diperbaiki sebagai bagian dari temuan validasi.

- [ ] **Write-8.** **Pertahankan seluruh konten yang valid** dari dokumen asli. Jangan hapus bagian yang sudah benar — hanya perbaiki yang perlu diperbaiki.

### 5.3. Pasca-Penulisan Ulang

- [ ] **Post-1.** Setelah file berhasil ditulis, **verifikasi** bahwa file target sudah berubah dengan cara membaca ulang minimal 50 baris pertama dan 50 baris terakhir dari file yang baru ditulis.
- [ ] **Post-2.** Verifikasi bahwa **versi dokumen sudah berubah** menjadi `v1.1` di frontmatter.
- [ ] **Post-3.** Verifikasi bahwa **Riwayat Perubahan** sudah berisi entri baru untuk `v1.1`.
- [ ] **Post-4.** Verifikasi bahwa **tidak ada truncation** — dokumen baru harus memiliki jumlah baris yang **sama atau lebih banyak** dari dokumen asli (803 baris). Jika jumlah baris lebih sedikit secara signifikan, ada yang dipotong — ulangi penulisan.

---

## 6. Instruksi Tambahan Referensi Baru

- [ ] **Ref-1.** Jika dalam proses validasi kamu menemukan bahwa ada **file referensi baru** yang tidak ada di Bab 18 dokumen utama namun faktanya digunakan sebagai acuan dalam perbaikan dokumen ini, maka **WAJIB** tambahkan file tersebut ke tabel referensi di Bab 18.

- [ ] **Ref-2.** Format penambahan referensi baru di tabel Bab 18:
  - Nomor urut baru (lanjutkan dari nomor terakhir yang ada).
  - Nama dokumen referensi.
  - Path relatif file.
  - Versi dokumen (cek di frontmatter file tersebut).
  - Prioritas (PRIMER / SEKUNDER / TERSIER) berdasarkan seberapa penting acuan tersebut bagi Coding Standard.
  - Peran dalam penyusunan (deskripsi singkat).

- [ ] **Ref-3.** Tambahan referensi harus **diletakkan di bagian paling bawah tabel** Bab 18, setelah entri yang sudah ada (nomor 8).

---

## 7. Ringkasan Kriteria Kualitas Akhir (Definition of Done)

Pekerjaan ini dianggap selesai (`Done`) **hanya jika** seluruh kriteria berikut ini terpenuhi:

| No | Kriteria | Status |
|----|----------|--------|
| 1  | Seluruh 9 file referensi telah dibaca dari baris pertama hingga terakhir | ☐ |
| 2  | Tahap A s.d. I telah dieksekusi seluruhnya tanpa ada yang dilewati | ☐ |
| 3  | Tidak ada inkonsistensi data antara dokumen utama dan file referensi | ☐ |
| 4  | Tidak ada informasi penting yang hilang dari dokumen utama | ☐ |
| 5  | Dokumen utama tidak berisi informasi yang tidak relevan dengan coding standard | ☐ |
| 6  | Struktur dokumen sesuai standar industri coding standard profesional | ☐ |
| 7  | Dokumen layak dan cukup sebagai referensi tunggal untuk fase konstruksi kode | ☐ |
| 8  | Bahasa Indonesia natural, tidak ambigu, dan mudah dipahami | ☐ |
| 9  | Tidak ada data kosong, TBD, atau placeholder yang belum diisi | ☐ |
| 10 | Seluruh contoh kode Python sintaksis valid untuk Python 3.14.2+ | ☐ |
| 11 | File target berhasil ditimpa (overwrite) dengan konten baru yang lengkap | ☐ |
| 12 | Versi dokumen berubah dari v1.0 menjadi v1.1 | ☐ |
| 13 | Riwayat perubahan sudah diperbarui dengan entri v1.1 | ☐ |
| 14 | Jumlah baris dokumen baru ≥ jumlah baris dokumen asli (803 baris) | ☐ |
| 15 | Referensi baru (jika ada) sudah ditambahkan di Bab 18 | ☐ |

---

## 8. Hal-Hal yang DILARANG Dilakukan

Selama proses implementasi issue ini, hal-hal berikut **DILARANG KERAS**:

- ❌ **Dilarang** memulai validasi tanpa membaca seluruh file referensi terlebih dahulu.
- ❌ **Dilarang** menulis ulang hanya sebagian dokumen (partial overwrite).
- ❌ **Dilarang** menggunakan `[...truncated...]` atau `[...dst...]` atau singkatan apapun dalam output dokumen akhir.
- ❌ **Dilarang** membuat asumsi tentang konten dokumen tanpa memverifikasi dari file referensi yang ada.
- ❌ **Dilarang** menambahkan konten baru yang tidak bersumber dari file referensi yang sudah ada di `docs/sdlc/`.
- ❌ **Dilarang** mengubah format konvensi yang sudah benar hanya karena terlihat berbeda dari kebiasaan.
- ❌ **Dilarang** melakukan commit atau push ke Git selama proses validasi (hanya baca dan tulis file lokal).
- ❌ **Dilarang** mengakhiri pekerjaan sebelum seluruh kriteria Definition of Done terpenuhi.

---

*Issue ini dibuat pada: 2026-05-26 | Proyek: AbuCom — Sistem Manajemen Terpadu Usaha Percetakan*
