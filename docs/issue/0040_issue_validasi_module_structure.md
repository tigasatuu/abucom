---
judul      : Validasi, Audit, dan Penulisan Ulang Dokumen Module Structure
target_file: docs/sdlc/04_implementation/03_module_structure.md
dibuat_oleh: Senior Software Architect & Module Decomposition Specialist
tanggal    : 2026-05-26
status     : Open
prioritas  : Tinggi
---

# Validasi, Audit, dan Penulisan Ulang Dokumen Module Structure

## 1. Latar Belakang dan Konteks

Dokumen **Module Structure** (`docs/sdlc/04_implementation/03_module_structure.md`) adalah deliverable teknis ketiga pada **Fase 04 — Implementation** dalam SDLC proyek AbuCom. Dokumen ini berperan sebagai cetak biru teknis file-level (technical blueprint) yang akan menjadi referensi utama bagi seluruh proses konstruksi kode Python, penulisan skenario uji, dan dokumen-dokumen SDLC fase selanjutnya.

Dokumen ini **WAJIB** divalidasi secara menyeluruh sebelum digunakan sebagai acuan implementasi. Tujuan issue ini adalah memastikan kelengkapan, keakuratan, kejelasan bahasa, dan kelayakan dokumen sebagai input deterministik bagi proses pembangunan sistem, baik oleh programmer manusia maupun oleh AI model lain.

---

## 2. Persona Validator

> **PENTING**: Implementor yang mengerjakan issue ini WAJIB memosisikan diri sebagai persona berikut selama seluruh proses validasi.

Kamu adalah seorang **Principal Software Architect** dengan spesialisasi **Python Modular System Design** dan **SDLC Technical Documentation Auditor**, dengan pengalaman lebih dari 15 tahun membangun sistem perangkat lunak enterprise skala menengah-besar di industri ritel dan manufaktur. Kamu memiliki keahlian mendalam dalam:

- Dekomposisi arsitektur berlapis (layered architecture) Python.
- Audit ketertelusuran (traceability) antara dokumen kebutuhan (SRS), desain arsitektur, dan rancangan modul.
- Verifikasi kelengkapan schema database relasional (DDL) terhadap pemetaan kode.
- Standar dokumentasi teknis industri (IEEE 1016, ISO/IEC 26514).
- Pemrograman fungsional murni (pure FP) Python dengan NamedTuple, Decimal, type hints PEP 484.
- Standar keamanan perangkat lunak: bcrypt, JWT, RBAC, enkripsi Fernet.
- Kaidah bahasa Indonesia teknis yang natural, tidak ambigu, dan mudah dipahami.

Sebagai persona ini, kamu **tidak boleh toleran** terhadap ketidaklengkapan, ambiguitas, inkonsistensi referensi silang, data kosong, atau bahasa yang membingungkan.

---

## 3. Informasi Dokumen Target

| Atribut | Nilai |
| --- | --- |
| **Nama Dokumen** | Module Structure |
| **Target File** | `docs/sdlc/04_implementation/03_module_structure.md` |
| **Versi Saat Ini** | v1.0 |
| **Versi Target Setelah Revisi** | v1.1 |
| **Status Saat Ini** | Draft |
| **Jumlah Baris** | 977 baris |
| **Posisi dalam SDLC** | Fase 04 — Implementation, Deliverable Ke-3 |

---

## 4. Dokumen Referensi yang Harus Dibaca

Sebelum memulai validasi, implementor **WAJIB** membaca seluruh file referensi berikut secara lengkap dari baris pertama hingga terakhir:

| No | Nama Dokumen | Path File |
| :---: | --- | --- |
| R-01 | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| R-02 | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` |
| R-03 | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` |
| R-04 | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` |
| R-05 | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` |
| R-06 | BOM & HPP Design v1.1 | `docs/sdlc/03_design/05_bom_hpp_design.md` |
| R-07 | Database Schema DDL SQL v1.1 | `docs/sdlc/03_design/01_database_schema.sql` |
| R-08 | Environment Setup v1.1 | `docs/sdlc/04_implementation/02_environment_setup.md` |

---

## 5. Kriteria Validasi

Implementor WAJIB menjalankan **semua** kriteria validasi berikut secara berurutan. Setiap kriteria menghasilkan temuan (findings) yang harus diperbaiki langsung pada dokumen output akhir.

---

### Kriteria V-01 — Komparasi Mendalam dengan File Referensi

**Tujuan**: Memastikan dokumen utama secara akurat merepresentasikan dan merangkum data dari seluruh file referensi R-01 s.d R-08.

**Instruksi validasi**:

1. Baca dokumen target (`docs/sdlc/04_implementation/03_module_structure.md`) dari baris pertama hingga terakhir secara menyeluruh.
2. Baca setiap file referensi R-01 s.d R-08 dari baris pertama hingga terakhir.
3. Untuk setiap file referensi, periksa dan tandai apakah seluruh data dan informasi berikut sudah tercermin secara akurat di dokumen target:

   **Dari R-01 (SRS)**:
   - [ ] Seluruh 10 modul fungsional (M.1 s.d M.10) sudah didefinisikan dengan benar nama dan tanggung jawabnya.
   - [ ] Seluruh ID kebutuhan fungsional SRS (SRS-F-001 s.d SRS-F-040 + SRS-F-ADD-01 s.d SRS-F-ADD-05) terpetakan ke minimal satu file handler di Matriks SRS-to-File (Seksi 14).
   - [ ] Error codes standar dari SRS sudah disinggung/didokumentasikan (contoh: ERR-DB-007).
   - [ ] Seluruh 8 peran pengguna (pemilik, kepala_percetakan, kasir, pramuniaga, gudang, desainer, produksi_cetak, fotocopy_print) sudah tercantum pada kolom hak akses spesifikasi file CLI.

   **Dari R-02 (System Architecture)**:
   - [ ] Diagram 4-layer logis (Presentation, Business Logic, Data Access, Persistence) sudah tergambar dengan benar.
   - [ ] Aturan dependensi searah top-down sudah tercantum secara eksplisit.
   - [ ] Spesifikasi connection pooling (`pool_name="abupool"`, `pool_size=5`) dan exponential backoff retry sudah termuat.
   - [ ] Prinsip multi-branch via `cabang_id` sudah tercermin.
   - [ ] Prinsip presisi desimal (Decimal) dan data protection (bcrypt, JWT HS256, Fernet) sudah tercermin.

   **Dari R-03 (Coding Standard)**:
   - [ ] Konvensi penamaan `snake_case` untuk fungsi/variabel dan `PascalCase` untuk NamedTuple sudah tercantum.
   - [ ] Aturan pure FP (tanpa class mutable, tanpa global state, tanpa efek samping di layer logic) sudah tercantum.
   - [ ] Penggunaan Result Pattern (NamedTuple `is_success`, `data`, `error_msg`) sudah termuat.
   - [ ] Aturan type hints PEP 484 wajib sudah tercantum.
   - [ ] Aturan layout direktori proyek sesuai Coding Standard sudah konsisten.

   **Dari R-04 (Access Control Matrix)**:
   - [ ] Semua 44 Use Case (UC-001 s.d UC-044) tercakup/termetakan dalam Matriks SRS-to-File atau spesifikasi menu file CLI.
   - [ ] Otorisasi DENY per peran per menu sudah tercantum pada setiap spesifikasi file `cli/`.
   - [ ] Menu IDs (MENU-BASE-001, MENU-M1-001, dst.) sudah konsisten dengan Access Control Matrix.

   **Dari R-05 (CLI Interaction Flow)**:
   - [ ] Semua menu navigasi (MENU-BASE dan MENU-Mx) sudah terpetakan ke file CLI yang tepat.
   - [ ] Konvensi visual `rich` dan `tabulate` sudah disebut dalam tanggung jawab file CLI.
   - [ ] Konvensi navigasi tombol `0` (kembali/keluar) sudah tercantum.

   **Dari R-06 (BOM & HPP Design)**:
   - [ ] Formula HPP desimal (presisi 4 desimal, `ROUND_HALF_UP`) sudah termuat.
   - [ ] Logika limbah/waste produksi cetak sudah termuat.
   - [ ] Sinkronisasi ATK internal sudah termuat di `logic/bom_hpp.py`.
   - [ ] Formula kalkulasi stempel flash dan yasin sudah disinggung.

   **Dari R-07 (Database Schema DDL)**:
   - [ ] Semua 28 nama tabel InnoDB MySQL terdaftar di Matriks Table-to-File (Seksi 15).
   - [ ] Tidak ada tabel dari DDL yang terlewat dalam pemetaan.
   - [ ] Nama tabel di dokumen konsisten persis dengan nama tabel di file DDL SQL (case-sensitive, gunakan `snake_case`).

   **Dari R-08 (Environment Setup)**:
   - [ ] Library yang tercantum di `requirements.txt` (Seksi 10.2) konsisten dengan yang sudah terdokumentasi di Environment Setup.
   - [ ] Versi library spesifik sudah tercantum dan tidak bertentangan.
   - [ ] Konfigurasi variabel `.env.example` (Seksi 10.3) konsisten dengan yang ada di Environment Setup.

4. Catat semua ketidaksesuaian, kekosongan, atau inkonsistensi yang ditemukan sebagai daftar temuan.
5. Perbaiki semua temuan tersebut secara langsung pada naskah dokumen yang akan ditulis ulang.

---

### Kriteria V-02 — Fokus dan Relevansi Konten

**Tujuan**: Memastikan dokumen utama hanya memuat data dan informasi yang memang seharusnya ada dalam dokumen Module Structure — tidak lebih, tidak kurang.

**Instruksi validasi**:

- [ ] Periksa apakah ada bagian atau sub-bagian yang memuat konten yang seharusnya masuk ke dokumen lain (contoh: detail implementasi bisnis mendalam yang seharusnya ada di SRS, atau detail query SQL penuh yang seharusnya ada di DDL).
- [ ] Periksa apakah setiap tabel pemetaan (Module-to-File, SRS-to-File, Table-to-File, Import Matrix) hanya mencakup data yang relevan untuk level abstraksi Module Structure (file-level, bukan code-level penuh).
- [ ] Periksa apakah signature fungsi contoh yang ditampilkan cukup untuk panduan implementasi tanpa terlalu verbose atau terlalu ringkas.
- [ ] Pastikan diagram Mermaid hanya menggambarkan informasi yang relevan pada scope dokumen ini (dekomposisi layer, dependensi impor, alur modul) — bukan detail implementasi internal fungsi.
- [ ] Tandai dan hapus atau ringkas konten yang tidak relevan atau berlebihan.
- [ ] Tandai dan tambahkan konten yang memang seharusnya ada namun belum ada.

---

### Kriteria V-03 — Standar Struktur Dokumen Industri

**Tujuan**: Memastikan dokumen memiliki struktur yang lengkap, terorganisasi, dan sesuai standar dokumen teknis industri (setara IEEE 1016 Software Design Description).

**Instruksi validasi**:

- [ ] Periksa apakah dokumen memiliki **front matter** (metadata YAML: nama dokumen, proyek, versi, tanggal, status, penyusun).
- [ ] Periksa apakah ada **Riwayat Perubahan Dokumen** (change log) dengan format tabel berisi versi, tanggal, deskripsi perubahan, dan nama editor.
- [ ] Periksa apakah ada **Seksi Informasi Dokumen** (tujuan, cakupan, posisi SDLC, hubungan dengan dokumen lain, audiens, definisi/akronim).
- [ ] Periksa apakah ada **Arsitektur Overview** lengkap (diagram berlapis, aturan dependensi, ringkasan modul fungsional, diagram dekomposisi).
- [ ] Periksa apakah ada **Spesifikasi Detail per File** pada setiap layer (Presentation, Business Logic, Data Access, Middleware, Config, Utils, Entry Point, Testing, Exports) yang memuat minimal: tujuan, modul fungsional, daftar fungsi publik, dependensi impor, use case/menu ID, tabel database diakses, dan hak akses.
- [ ] Periksa apakah ada **Matriks Ketertelusuran** lengkap: Module-to-File, SRS-to-File, Table-to-File, Import Matrix.
- [ ] Periksa apakah ada **Diagram Mermaid** yang fungsional dan tidak rusak sintaksnya: diagram 4-layer, diagram dekomposisi modul, diagram import matrix, diagram alur modul.
- [ ] Periksa apakah ada **Seksi Persetujuan dan Otorisasi**.
- [ ] Periksa apakah ada **Glosarium** yang mendefinisikan semua akronim dan istilah teknis yang digunakan dalam dokumen.
- [ ] Periksa apakah ada **Tabel Referensi Dokumen** yang mencantumkan semua sumber yang digunakan.
- [ ] Pastikan semua nomor seksi (1., 1.1., 1.2., dst.) berurutan dan tidak ada yang lompat atau terduplikasi.
- [ ] Pastikan semua tabel memiliki header kolom yang jelas dan format yang konsisten.
- [ ] Perbaiki semua kekurangan struktur yang ditemukan.

---

### Kriteria V-04 — Kelayakan sebagai Referensi SDLC Selanjutnya

**Tujuan**: Memastikan dokumen ini mampu menjadi input yang memadai dan self-contained bagi dokumen dan proses SDLC fase selanjutnya (konstruksi kode, testing plan, deployment guide).

**Instruksi validasi**:

- [ ] Periksa apakah setiap file Python yang didefinisikan memiliki **daftar fungsi publik yang cukup** (minimal signature + docstring singkat) agar programmer dapat langsung membuat boilerplate kode tanpa perlu membuka dokumen lain.
- [ ] Periksa apakah setiap file CLI memiliki informasi **hak akses per peran yang spesifik** (menyebutkan nama peran secara eksplisit mana yang ALLOW dan mana yang DENY).
- [ ] Periksa apakah setiap file logic memiliki **contoh signature NamedTuple** yang digunakan sehingga tipe data jelas untuk implementasi.
- [ ] Periksa apakah Matriks SRS-to-File **menutupi seluruh ID SRS** yang ada di R-01 tanpa ada yang terlewat.
- [ ] Periksa apakah Matriks Table-to-File **menutupi semua 28 tabel** dari R-07 tanpa ada yang terlewat.
- [ ] Periksa apakah **diagram dependensi impor** cukup akurat sehingga programmer dapat menyusun `import` statement dengan benar.
- [ ] Periksa apakah dokumen ini cukup **self-contained** — artinya, seseorang yang belum pernah membaca SRS atau System Architecture tetap dapat memahami struktur modul dari dokumen ini saja.
- [ ] Verifikasi bahwa setiap nama fungsi publik yang dicantumkan **konsisten** antara: spesifikasi file (Seksi 4–11) ↔ Matriks SRS-to-File (Seksi 14) ↔ Diagram Import Matrix (Seksi 16).
- [ ] Verifikasi bahwa nama tabel database yang dicantumkan pada spesifikasi file CLI (kolom "Tabel Database diakses") **konsisten** dengan Matriks Table-to-File (Seksi 15).

---

### Kriteria V-05 — Kualitas Bahasa Indonesia Teknis

**Tujuan**: Memastikan seluruh teks dokumen menggunakan Bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau AI model yang lebih sederhana.

**Instruksi validasi**:

- [ ] Baca setiap kalimat di seluruh dokumen. Tandai kalimat yang:
  - Ambigu (dapat diinterpretasikan lebih dari satu cara).
  - Terlalu panjang dan berbelit-belit (lebih dari 3 klausa dalam satu kalimat).
  - Menggunakan campuran Bahasa Indonesia dan Inggris yang tidak konsisten atau tidak perlu.
  - Menggunakan istilah teknis tanpa penjelasan padahal tidak ada di glosarium.
  - Menggunakan kata "biner" secara tidak tepat (catatan: kata "biner" berarti sistem bilangan basis 2 — periksa apakah penggunaannya tepat dalam konteks kalimat, atau seharusnya diganti dengan kata lain yang lebih tepat seperti "langsung", "otomatis", atau dihapus).
- [ ] Periksa apakah judul setiap seksi dan sub-seksi sudah deskriptif dan informatif.
- [ ] Pastikan seluruh instruksi ditulis dalam bentuk kalimat aktif yang jelas (subjek → predikat → objek).
- [ ] Perbaiki semua kalimat yang bermasalah.

---

### Kriteria V-06 — Kelengkapan Kualitas Konten (Tidak Perlu Selalu Diinterupsi)

**Tujuan**: Memastikan dokumen ini memiliki tingkat kelengkapan yang cukup sehingga tidak akan menghambat pekerjaan fase SDLC selanjutnya akibat informasi yang kurang atau menggantung.

**Instruksi validasi**:

- [ ] Periksa apakah ada bagian yang menyebut "TBD", "TODO", "akan ditentukan kemudian", atau kalimat dengan isi yang tidak selesai.
- [ ] Periksa apakah ada sel tabel yang kosong yang seharusnya diisi (bukan memang kosong karena tidak relevan).
- [ ] Periksa apakah setiap fungsi publik yang dicantumkan memiliki docstring singkat yang menjelaskan apa yang dilakukan fungsi tersebut.
- [ ] Periksa apakah ada spesifikasi file yang tidak memiliki kolom "Tabel Database diakses" — jika memang tidak mengakses tabel, tulis secara eksplisit "Tidak ada" agar tidak menimbulkan pertanyaan.
- [ ] Periksa apakah ada spesifikasi file yang tidak memiliki kolom "Hak Akses / Peran" — jika memang tidak ada pembatasan, tulis "Seluruh peran" agar tidak ambigu.
- [ ] Pastikan setiap modul fungsional M.1 s.d M.10 terwakili di minimal satu file CLI, satu file logic (kecuali modul yang memang tidak memerlukan logic terpisah), dan satu file db/.
- [ ] Periksa apakah ada Use Case di R-04 (Access Control Matrix) yang belum dipetakan ke Menu ID di spesifikasi file CLI mana pun.
- [ ] Periksa apakah kolom "Modul SRS di-cover" pada setiap spesifikasi file logic sudah mencantumkan semua SRS ID yang relevan (tidak hanya satu atau dua).

---

### Kriteria V-07 — Pengisian Data Kosong atau Placeholder

**Tujuan**: Memastikan tidak ada data yang kosong, tidak tersedia, atau perlu diisi manual yang tertinggal dalam dokumen.

**Instruksi validasi**:

- [ ] Periksa tabel **Riwayat Perubahan Dokumen** — pastikan semua kolom terisi: versi, tanggal, deskripsi perubahan yang spesifik (bukan hanya "inisialisasi"), dan nama penyusun.
- [ ] Periksa tabel **Persetujuan dan Otorisasi** (Seksi 18) — pastikan nama, status otorisasi, dan tanggal terisi semua. Jika ada yang kosong, isi dengan data yang masuk akal dan relevan dalam konteks proyek AbuCom.
- [ ] Periksa **seluruh sel di setiap tabel matriks** — jika ada sel kosong yang seharusnya berisi data, isi dengan data yang tepat berdasarkan konteks referensi.
- [ ] Periksa **signature fungsi** di setiap spesifikasi file — jika ada fungsi yang namanya disebutkan di Matriks SRS-to-File tetapi tidak ada signature-nya di spesifikasi file, tambahkan signature minimal beserta docstring.
- [ ] Periksa apakah ada **nama tabel database** di Matriks Table-to-File yang kolom "File Logika Bisnis" -nya kosong atau tidak relevan — jika demikian, koreksi dengan file logic yang paling tepat.
- [ ] Periksa **konfigurasi variabel `.env.example`** di Seksi 10.3 — jika ada variabel yang disinggung di bagian lain dokumen tapi belum tercantum di sini, tambahkan.
- [ ] Periksa **versi library** di `requirements.txt` (Seksi 10.2) — jika ada library yang digunakan di spesifikasi file (seperti `getpass`, `decimal`, `collections`, `typing`) namun tidak ada di requirements karena merupakan library built-in, beri keterangan eksplisit bahwa library tersebut adalah built-in Python.

---

### Kriteria V-08 — Validasi Konsistensi Internal Silang (Cross-Reference)

**Tujuan**: Memastikan tidak ada inkonsistensi antara bagian-bagian dalam dokumen itu sendiri.

**Instruksi validasi**:

- [ ] Periksa apakah nama file yang disebutkan di **Seksi 3 (Layout Direktori)** konsisten persis dengan nama file pada **Seksi 4–11 (Spesifikasi Modul)**.
- [ ] Periksa apakah nama file pada **Diagram Mermaid Seksi 2.4 (Dekomposisi)** konsisten dengan **Seksi 3 (Direktori Tree)** dan **Seksi 4–11 (Spesifikasi)**.
- [ ] Periksa apakah nama fungsi publik pada **Seksi 4–11 (Spesifikasi File)** konsisten persis dengan nama fungsi pada **Seksi 14 (Matriks SRS-to-File)** kolom "Lokasi Fungsi Spesifik".
- [ ] Periksa apakah nama tabel database pada spesifikasi file CLI (sub-seksi "Tabel Database diakses") konsisten persis dengan nama tabel pada **Seksi 15 (Matriks Table-to-File)**.
- [ ] Periksa apakah **Diagram Import Matrix (Seksi 16)** konsisten dengan **kolom "Dependensi Impor"** pada setiap spesifikasi file di Seksi 4–11.
- [ ] Periksa apakah **Modul SRS di-cover** pada setiap spesifikasi file logic konsisten dengan **Matriks SRS-to-File (Seksi 14)** — tidak ada SRS ID yang tercantum di spesifikasi file tapi tidak ada di matriks, dan sebaliknya.
- [ ] Periksa apakah **Menu ID** pada spesifikasi file CLI (sub-seksi "Hubungan Use Case / Menu ID") konsisten dengan yang ada di R-05 (CLI Interaction Flow).
- [ ] Perbaiki semua inkonsistensi yang ditemukan.

---

### Kriteria V-09 — Validasi Diagram Mermaid

**Tujuan**: Memastikan seluruh diagram Mermaid dalam dokumen valid secara sintaksis dan akurat secara konten.

**Instruksi validasi**:

- [ ] Baca setiap blok diagram Mermaid dalam dokumen (ada 4 diagram: Seksi 2.1, 2.4, 16, 17).
- [ ] Periksa apakah setiap node/edge pada diagram memiliki label yang jelas dan tidak ada karakter yang dapat merusak sintaks Mermaid (seperti tanda `&` yang perlu di-escape, tanda kurung dalam label node, dll.).
- [ ] Periksa apakah koneksi antar-node dalam diagram **akurat secara logika** — misalnya, alur dependensi impor harus searah top-down sesuai aturan arsitektur (cli → logic → db, bukan sebaliknya).
- [ ] Periksa apakah diagram **Seksi 2.4 (Dekomposisi Modul ke Layer)** sudah mencakup semua file yang terdaftar di Seksi 3 (Direktori Tree).
- [ ] Periksa apakah diagram **Seksi 16 (Import Matrix)** sudah mencakup semua file Python yang terdaftar dan mencerminkan seluruh dependensi impor yang tercantum di spesifikasi file.
- [ ] Perbaiki semua masalah sintaks atau konten pada diagram.

---

### Kriteria V-10 — Validasi Tambahan Spesifik Dokumen Module Structure

**Tujuan**: Memastikan aspek-aspek spesifik yang unik untuk dokumen Module Structure sudah terpenuhi dengan benar.

**Instruksi validasi**:

- [ ] **Kelengkapan Spesifikasi Entry Point (`main.py`)**: Periksa apakah tanggung jawab `main.py` sudah cukup detail — minimal mencakup: inisialisasi `.env`, validasi startup, pengecekan koneksi database LAN, dan peluncuran CLI loop. Jika ada yang kurang, tambahkan.
- [ ] **Kelengkapan Spesifikasi Testing**: Periksa apakah spesifikasi file `tests/` sudah menyebutkan framework testing yang digunakan (contoh: `pytest`), standar coverage minimum, dan jenis pengujian (unit vs integration).
- [ ] **Konvensi `__init__.py`**: Pastikan setiap direktori Python (`cli/`, `logic/`, `db/`, `middleware/`, `config/`, `utils/`, `tests/`) memiliki spesifikasi `__init__.py` yang menjelaskan apa yang di-expose, bukan hanya "Re-export".
- [ ] **Validasi Nama Modul Fungsional**: Periksa konsistensi nama modul (M.1 s.d M.10) antara Seksi 2.3 (tabel ringkasan), Seksi 4–11 (spesifikasi file), dan Seksi 13 (Module-to-File Mapping). Nama harus identik persis di setiap bagian.
- [ ] **Validasi Layer Assignment**: Pastikan tidak ada file yang salah di-assign ke layer yang salah (contoh: fungsi perhitungan keuangan di layer `cli/`, atau fungsi I/O di layer `logic/`).
- [ ] **Kelengkapan Cross-Cutting Concerns**: Pastikan `config/settings.py` sudah menyebutkan semua variabel environment yang digunakan oleh file lain dalam dokumen (contoh: `FERNET_KEY` untuk `utils/crypto.py`, `JWT_SECRET_KEY` untuk `middleware/auth_jwt.py`).
- [ ] **Konsistensi Versi Dokumen Referensi**: Periksa apakah versi dokumen referensi yang dicantumkan di Seksi 20 (Referensi Dokumen) konsisten dengan versi yang disebutkan di Seksi 1.4 (Hubungan dengan Dokumen SDLC Lainnya).

---

## 6. Prosedur Implementasi Step-by-Step

> **PERHATIAN**: Implementor WAJIB mengikuti langkah-langkah berikut secara berurutan dari atas ke bawah. Jangan melompat atau melewatkan langkah apapun. Jangan mengubah file apapun sebelum langkah persiapan selesai.

---

### Fase A — Persiapan (Baca Semua File Terlebih Dahulu)

- [ ] **A-01**: Baca file `docs/sdlc/04_implementation/03_module_structure.md` dari baris 1 hingga baris terakhir (977 baris). Catat versi dokumen saat ini (v1.0), jumlah seksi, dan struktur umum dokumen.
- [ ] **A-02**: Baca file `docs/sdlc/02_analysis/02_software_requirements.md` dari baris 1 hingga baris terakhir. Catat: jumlah modul fungsional, daftar lengkap ID SRS (SRS-F-001 dst.), nama-nama 8 peran pengguna, dan error codes.
- [ ] **A-03**: Baca file `docs/sdlc/03_design/03_system_architecture.md` dari baris 1 hingga baris terakhir. Catat: nama 4 layer, aturan dependensi, spesifikasi connection pool, multi-branch, teknologi keamanan.
- [ ] **A-04**: Baca file `docs/sdlc/04_implementation/01_coding_standard.md` dari baris 1 hingga baris terakhir. Catat: aturan penamaan, aturan pure FP, Result Pattern, type hints, layout direktori.
- [ ] **A-05**: Baca file `docs/sdlc/02_analysis/06_access_control_matrix.md` dari baris 1 hingga baris terakhir. Catat: semua 44 Use Case ID, semua Menu ID, dan matriks ALLOW/DENY per peran per menu.
- [ ] **A-06**: Baca file `docs/sdlc/03_design/04_cli_interaction_flow.md` dari baris 1 hingga baris terakhir. Catat: semua Menu ID (MENU-BASE dan MENU-Mx), konvensi visual rich/tabulate, navigasi tombol 0.
- [ ] **A-07**: Baca file `docs/sdlc/03_design/05_bom_hpp_design.md` dari baris 1 hingga baris terakhir. Catat: formula HPP desimal, aturan limbah, sinkronisasi ATK, presisi kalkulasi.
- [ ] **A-08**: Baca file `docs/sdlc/03_design/01_database_schema.sql` dari baris 1 hingga baris terakhir. Catat: nama lengkap semua 28 tabel InnoDB secara persis (case-sensitive).
- [ ] **A-09**: Baca file `docs/sdlc/04_implementation/02_environment_setup.md` dari baris 1 hingga baris terakhir. Catat: nama dan versi library, variabel `.env`, konfigurasi database.

---

### Fase B — Audit dan Analisis

- [ ] **B-01**: Jalankan **Kriteria V-01** (Komparasi Mendalam). Buat daftar temuan: data apa dari referensi yang belum ada di dokumen target, data apa yang tidak akurat.
- [ ] **B-02**: Jalankan **Kriteria V-02** (Fokus dan Relevansi). Buat daftar temuan: konten apa yang berlebihan dan konten apa yang masih kurang.
- [ ] **B-03**: Jalankan **Kriteria V-03** (Standar Struktur). Buat daftar temuan: seksi apa yang kurang, format tabel mana yang tidak konsisten, nomor seksi mana yang bermasalah.
- [ ] **B-04**: Jalankan **Kriteria V-04** (Kelayakan Referensi). Buat daftar temuan: informasi apa yang kurang untuk kebutuhan implementasi.
- [ ] **B-05**: Jalankan **Kriteria V-05** (Kualitas Bahasa). Buat daftar kalimat yang ambigu atau bermasalah.
- [ ] **B-06**: Jalankan **Kriteria V-06** (Kelengkapan Konten). Buat daftar placeholder, TBD, atau sel kosong yang ditemukan.
- [ ] **B-07**: Jalankan **Kriteria V-07** (Pengisian Data Kosong). Buat daftar data kosong yang perlu diisi.
- [ ] **B-08**: Jalankan **Kriteria V-08** (Konsistensi Internal Silang). Buat daftar inkonsistensi yang ditemukan antar-seksi.
- [ ] **B-09**: Jalankan **Kriteria V-09** (Diagram Mermaid). Periksa semua 4 diagram Mermaid.
- [ ] **B-10**: Jalankan **Kriteria V-10** (Validasi Spesifik Module Structure). Buat daftar aspek spesifik yang belum terpenuhi.

---

### Fase C — Penyusunan Dokumen Revisi

- [ ] **C-01**: Siapkan naskah lengkap dokumen revisi dalam memori kerja (working memory). Mulai dari baris pertama (front matter YAML) hingga baris terakhir (tabel referensi dokumen).
- [ ] **C-02**: Ubah versi dokumen dari `v1.0` menjadi `v1.1` pada **front matter YAML** (baris metadata di awal dokumen).
- [ ] **C-03**: Tambahkan baris baru di tabel **Riwayat Perubahan Dokumen** dengan entri: `v1.1 | [tanggal hari ini] | [deskripsi ringkas perubahan validasi yang dilakukan] | Principal Software Architect`.
- [ ] **C-04**: Terapkan semua perbaikan dari Fase B secara menyeluruh pada seluruh bagian dokumen. Urutan pengerjaan perbaikan:
  - [ ] **C-04a**: Perbaiki front matter, riwayat perubahan, dan Seksi 1 (Informasi Dokumen).
  - [ ] **C-04b**: Perbaiki Seksi 2 (Arsitektur Modular Overview) termasuk semua diagram Mermaid.
  - [ ] **C-04c**: Perbaiki Seksi 3 (Layout Direktori).
  - [ ] **C-04d**: Perbaiki Seksi 4 (Spesifikasi Layer Presentation / cli/).
  - [ ] **C-04e**: Perbaiki Seksi 5 (Spesifikasi Layer Business Logic / logic/).
  - [ ] **C-04f**: Perbaiki Seksi 6 (Spesifikasi Layer Data Access / db/).
  - [ ] **C-04g**: Perbaiki Seksi 7 (Spesifikasi Middleware).
  - [ ] **C-04h**: Perbaiki Seksi 8 (Spesifikasi Config).
  - [ ] **C-04i**: Perbaiki Seksi 9 (Spesifikasi Utils).
  - [ ] **C-04j**: Perbaiki Seksi 10 (Entry Point & Root Config).
  - [ ] **C-04k**: Perbaiki Seksi 11 (Testing).
  - [ ] **C-04l**: Perbaiki Seksi 12 (Output Directories).
  - [ ] **C-04m**: Perbaiki Seksi 13 (Module-to-File Mapping Matrix).
  - [ ] **C-04n**: Perbaiki Seksi 14 (SRS-to-File Traceability Matrix).
  - [ ] **C-04o**: Perbaiki Seksi 15 (Table-to-File Mapping Matrix).
  - [ ] **C-04p**: Perbaiki Seksi 16 (Inter-File Import Matrix / Diagram Mermaid).
  - [ ] **C-04q**: Perbaiki Seksi 17 (Module Dependency Flow Diagram / Mermaid).
  - [ ] **C-04r**: Perbaiki Seksi 18 (Persetujuan dan Otorisasi).
  - [ ] **C-04s**: Perbaiki Seksi 19 (Glosarium) — tambahkan istilah baru jika ada yang digunakan dalam dokumen tapi belum ada di glosarium.
  - [ ] **C-04t**: Perbaiki Seksi 20 (Referensi Dokumen) — pastikan semua file referensi yang digunakan dalam proses validasi ini tercantum.
- [ ] **C-05**: Jika dalam proses validasi ditemukan file referensi tambahan yang tidak ada di Seksi 20 namun digunakan sebagai dasar perbaikan, **tambahkan file referensi tersebut** sebagai baris baru di tabel Seksi 20 (Referensi Dokumen) di bagian paling bawah tabel.

---

### Fase D — Penulisan Ulang File (Overwrite)

> **PERINGATAN KRITIS**: Langkah ini bersifat destruktif (overwrite). Pastikan naskah dokumen revisi sudah **100% lengkap dan siap** sebelum menjalankan langkah D-01. Tidak ada jalan kembali setelah file ditimpa.

- [ ] **D-01**: Tulis ulang seluruh isi file `docs/sdlc/04_implementation/03_module_structure.md` dengan naskah dokumen revisi yang sudah disiapkan di Fase C. Metode penulisan:
  - Gunakan operasi **overwrite** (timpa seluruh isi file dari awal hingga akhir).
  - Tuliskan **seluruh teks dari baris pertama hingga baris terakhir** tanpa ada yang dipotong, diringkas, dipersingkat, atau dihilangkan.
  - **DILARANG KERAS** menggunakan frasa seperti "... (konten sebelumnya tetap sama) ...", "... (bagian ini tidak berubah) ...", atau sejenisnya. Seluruh isi dokumen HARUS ditulis ulang secara penuh dan eksplisit.
  - Pastikan file hasil overwrite dimulai dari `---` (front matter YAML) dan diakhiri dengan baris terakhir tabel Referensi Dokumen (Seksi 20), termasuk semua referensi tambahan jika ada.
- [ ] **D-02**: Setelah penulisan selesai, baca kembali file `docs/sdlc/04_implementation/03_module_structure.md` yang sudah ditimpa dari baris 1 hingga baris terakhir untuk **memverifikasi** bahwa:
  - [ ] Versi dokumen sudah berubah menjadi `v1.1`.
  - [ ] Riwayat perubahan sudah memiliki baris entri baru untuk `v1.1`.
  - [ ] Tidak ada baris yang terpotong atau hilang di tengah-tengah dokumen.
  - [ ] Semua tabel masih memiliki format Markdown yang valid (tanda `|` dan `---` pada baris header).
  - [ ] Semua blok kode (``` ``` ```) dan blok diagram Mermaid masih terbuka dan tertutup dengan benar.
  - [ ] Jumlah seksi utama (level `##`) sudah sesuai dengan yang direncanakan.

---

### Fase E — Pelaporan Hasil

- [ ] **E-01**: Tulis ringkasan singkat hasil validasi yang mencakup:
  - Total jumlah temuan per kriteria (V-01 s.d V-10).
  - Daftar perubahan signifikan yang dilakukan pada dokumen.
  - Konfirmasi bahwa dokumen `v1.1` sudah berhasil ditulis ke file target.
- [ ] **E-02**: Tandai issue ini sebagai **Closed / Done** setelah file target berhasil ditulis ulang dan diverifikasi.

---

## 7. Kriteria Penerimaan (Acceptance Criteria)

Issue ini dinyatakan **Selesai (Done)** jika dan hanya jika seluruh kondisi berikut terpenuhi:

- [ ] **AC-01**: File `docs/sdlc/04_implementation/03_module_structure.md` berisi versi `v1.1`.
- [ ] **AC-02**: Tabel Riwayat Perubahan memiliki entri baru untuk `v1.1` dengan deskripsi perubahan yang spesifik.
- [ ] **AC-03**: Seluruh 28 tabel database dari DDL SQL (R-07) terdaftar di Matriks Table-to-File (Seksi 15).
- [ ] **AC-04**: Seluruh ID SRS dari SRS (R-01) — minimal SRS-F-001 s.d SRS-F-040 + SRS-F-ADD-01 s.d SRS-F-ADD-05 — terpetakan di Matriks SRS-to-File (Seksi 14).
- [ ] **AC-05**: Semua 8 peran pengguna disebutkan secara eksplisit pada kolom "Hak Akses / Peran" di setiap spesifikasi file CLI (Seksi 4).
- [ ] **AC-06**: Semua diagram Mermaid (Seksi 2.1, 2.4, 16, 17) valid secara sintaksis dan akurat secara konten.
- [ ] **AC-07**: Tidak ada kalimat ambigu, placeholder "TBD", atau sel tabel yang kosong tanpa keterangan yang tersisa di dokumen.
- [ ] **AC-08**: Semua referensi yang digunakan dalam proses validasi tercantum di Seksi 20 (Referensi Dokumen).
- [ ] **AC-09**: Dokumen hasil overwrite lengkap dari baris pertama hingga terakhir — tidak ada bagian yang terpotong atau hilang.
- [ ] **AC-10**: Nama fungsi publik konsisten antara Seksi 4–11 ↔ Seksi 14 ↔ Seksi 16.

---

## 8. Catatan Penting untuk Implementor

> [!IMPORTANT]
> **Jangan memulai penulisan ke file sebelum seluruh Fase A dan B selesai.** Menulis lebih dulu sebelum audit lengkap akan menghasilkan dokumen yang tidak akurat.

> [!WARNING]
> **Operasi overwrite (D-01) bersifat permanen.** Pastikan naskah revisi sudah final sebelum melakukan overwrite. Jika menggunakan LLM/AI, generate seluruh dokumen dalam satu output dan tulis sekaligus — jangan menulis bertahap per bagian karena berpotensi menghasilkan dokumen yang tidak konsisten.

> [!CAUTION]
> **Dilarang keras memotong, meringkas, atau menghilangkan konten.** Instruksi "no truncation" bersifat mutlak. Jika terkendala batas token/output, bagi penulisan menjadi beberapa operasi `append` yang berurutan, bukan memotong konten.

> [!NOTE]
> **Kata "biner"** digunakan secara tidak tepat di beberapa bagian dokumen v1.0 (contoh: "stateless token tanda tangan HS256 kedaluwarsa 8 jam biner"). Dalam proses validasi, ganti atau hapus kata "biner" dari konteks yang tidak tepat tersebut.

> [!TIP]
> Jika ragu apakah suatu informasi harus ditambahkan atau tidak, gunakan prinsip: **"Apakah junior programmer dapat mulai menulis kode Python untuk file ini hanya berdasarkan informasi di dokumen ini?"** Jika jawabannya tidak, tambahkan informasi yang kurang.

---


