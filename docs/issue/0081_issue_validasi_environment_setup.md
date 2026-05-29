# Validasi Menyeluruh Dokumen Environment Setup

## 1. Konteks Tugas

| Atribut         | Detail                                                                               |
|:----------------|:-------------------------------------------------------------------------------------|
| **Dokumen Utama**   | Environment Setup                                                                |
| **Target File**     | `docs/sdlc/04_implementation/02_environment_setup.md`                            |
| **Versi Saat Ini**  | v1.1                                                                             |
| **Versi Target**    | v1.2                                                                             |
| **Lokasi Referensi**| `docs/sdlc/`                                                                     |
| **Status Issue**    | OPEN                                                                             |
| **Prioritas**       | TINGGI — Prasyarat mutlak sebelum eksekusi pengkodean modul dimulai              |

### Deskripsi Singkat
Lakukan audit, analisis, dan validasi ketat terhadap dokumen `docs/sdlc/04_implementation/02_environment_setup.md` (selanjutnya disebut **Dokumen Utama**). Tugas ini mencakup komparasi mendalam dengan seluruh file referensi yang dirujuk, pemeriksaan kelengkapan, relevansi konten, kualitas bahasa, struktur dokumen, dan penulisan ulang penuh hasil validasi ke file target yang sama dengan versi diperbarui (v1.2). Seluruh tahapan harus diselesaikan secara berurutan dan tidak ada langkah yang boleh dilewati.

---

## 2. Persona yang Harus Diadopsi

> **INSTRUKSI WAJIB**: Sebelum memulai pekerjaan apa pun, kamu harus mengadopsi dan mempertahankan persona berikut ini sepanjang seluruh proses eksekusi issue ini.

Kamu adalah **Senior DevOps Engineer & Technical Documentation Architect** dengan spesialisasi ganda:

1. **Infrastructure Specialist**: Memiliki pengalaman 10+ tahun dalam setup lingkungan server Linux (Debian/Ubuntu), administrasi database MySQL/PostgreSQL, konfigurasi jaringan LAN enterprise, keamanan sistem (firewall, SSH hardening, enkripsi), dan orkestrasi lingkungan development Python di skala produksi.

2. **SDLC Technical Writer**: Memiliki keahlian dalam standar penulisan dokumen teknis industri (IEEE 1063, ISO/IEC 26511), spesifikasi panduan operasional (*operational manual*), dan kemampuan untuk menilai apakah sebuah dokumen mampu berfungsi sebagai panduan teknis tunggal yang mandiri, tidak ambigu, dan dapat dieksekusi tanpa pertanyaan lanjutan.

**Otoritas Audit**: Kamu memiliki kewenangan penuh untuk:
- Menolak konten yang tidak akurat secara teknis, ambigu, atau tidak lengkap.
- Menambahkan konten yang hilang dan kritis namun belum ada dalam dokumen.
- Menghapus konten yang tidak relevan atau di luar cakupan dokumen.
- Memperbaiki struktur bahasa Indonesia yang tidak natural atau membingungkan.
- Mengisi seluruh placeholder data kosong dengan data riil yang sesuai.

---

## 3. File yang Harus Dibaca

Baca **seluruh** file berikut secara lengkap sebelum memulai proses validasi. Jangan lewati satu pun file.

### 3.1. Dokumen Utama (Target Validasi)
- [ ] **[BACA]** `docs/sdlc/04_implementation/02_environment_setup.md` — Baca dari baris pertama hingga baris terakhir. Catat secara mental seluruh bab, sub-bab, kode snippet, checklist, tabel, dan referensi yang ada.

### 3.2. File Referensi Primer (Wajib Dikomparasi)
- [ ] **[BACA]** `docs/sdlc/01_planning/04_tech_stack_decision.md` — Baca seluruh keputusan platform runtime, versi pustaka, dan justifikasi teknologi.
- [ ] **[BACA]** `docs/sdlc/03_design/03_system_architecture.md` — Baca seluruh topologi jaringan LAN, alokasi IP, spesifikasi hardware, dan connection pool.
- [ ] **[BACA]** `docs/sdlc/03_design/06_security_design.md` — Baca seluruh spesifikasi bcrypt, JWT, hak akses user DB, enkripsi Fernet, dan kode error.
- [ ] **[BACA]** `docs/sdlc/04_implementation/01_coding_standard.md` — Baca seluruh layout direktori proyek, template `.gitignore`, `.env.example`, dan connection pool factory.

### 3.3. File Referensi Sekunder (Wajib Dikomparasi)
- [ ] **[BACA]** `docs/sdlc/03_design/01_database_schema.sql` — Baca DDL fisik: nama tabel, kolom, tipe data, dan relasi untuk memverifikasi konsistensi instruksi migrasi schema.
- [ ] **[BACA]** `docs/sdlc/02_analysis/02_software_requirements.md` — Baca spesifikasi non-fungsional performa, kompatibilitas dual-OS, dan kebutuhan sistem.
- [ ] **[BACA]** `docs/sdlc/02_analysis/06_access_control_matrix.md` — Baca pembagian 8 peran karyawan dan eskalasi hak akses.

### 3.4. File Referensi Tersier
- [ ] **[BACA]** `docs/sdlc/narasi.txt` — Baca konteks bisnis owner, mandat runtime Python, lisensi pustaka, dan target dual-OS.

---

## 4. Tahapan Validasi — Eksekusi Secara Berurutan

Setelah seluruh file dibaca, jalankan tahapan validasi berikut satu per satu. Tandai `[x]` setiap sub-tugas yang selesai dikerjakan.

---

### TAHAP 1 — Komparasi Mendalam: Dokumen Utama vs. File Referensi

**Tujuan**: Memastikan Dokumen Utama tidak kehilangan satu pun data atau keputusan teknis kritis dari file referensi yang seharusnya tercermin dalam panduan setup lingkungan ini.

#### 1.1. Komparasi dengan Tech Stack Decision
- [ ] Buka `docs/sdlc/01_planning/04_tech_stack_decision.md`.
- [ ] Verifikasi: Apakah **versi Python** yang disebutkan di Dokumen Utama (3.14.2+) konsisten dengan keputusan di Tech Stack Decision?
- [ ] Verifikasi: Apakah **versi MySQL** yang disebutkan (8.4 LTS) konsisten?
- [ ] Verifikasi: Apakah **seluruh nama library dan versi terkunci** di `requirements.txt` (Bab 7.3) konsisten 100% dengan daftar di Tech Stack Decision? Periksa satu per satu:
  - [ ] `mysql-connector-python` — versi match?
  - [ ] `python-dotenv` — versi match?
  - [ ] `bcrypt` — versi match?
  - [ ] `pyjwt` — versi match?
  - [ ] `cryptography` — versi match?
  - [ ] `rich` — versi match?
  - [ ] `tabulate` — versi match?
  - [ ] `pytest` — versi match?
  - [ ] `coverage` — versi match?
- [ ] Verifikasi: Apakah ada library di Tech Stack Decision yang **belum masuk** ke daftar requirements.txt Dokumen Utama? Jika ada, tambahkan.
- [ ] Verifikasi: Apakah spesifikasi visual CLI (Rich, Tabulate) sudah dijelaskan alasan penggunaannya di Dokumen Utama?
- [ ] Catat temuan perbedaan atau ketidakkonsistenan.

#### 1.2. Komparasi dengan System Architecture
- [ ] Buka `docs/sdlc/03_design/03_system_architecture.md`.
- [ ] Verifikasi: Apakah **topologi jaringan** (star network, switch hub, router MikroTik) di Dokumen Utama konsisten dengan diagram arsitektur?
- [ ] Verifikasi: Apakah **IP statis server** (`192.168.1.200`) konsisten?
- [ ] Verifikasi: Apakah **spesifikasi hardware Mini PC Server** (prosesor, RAM, SSD) konsisten dengan yang didefinisikan di System Architecture?
- [ ] Verifikasi: Apakah **spesifikasi hardware PC Kasir** konsisten?
- [ ] Verifikasi: Apakah **konfigurasi connection pool** (`pool_name='abupool'`, `pool_size=5`) disebutkan dan diimplementasikan dengan benar di Dokumen Utama? Cek apakah ada contoh kode inisialisasi pool.
- [ ] Verifikasi: Apakah **printer thermal** (58mm/80mm, USB/Serial) dan **laci kasir** (RJ11) sudah lengkap terdokumentasi?
- [ ] Verifikasi: Apakah **UPS** (2 unit, 600VA/360W) dengan justifikasi teknis konsisten?
- [ ] Catat temuan perbedaan atau ketidakkonsistenan.

#### 1.3. Komparasi dengan Security Design
- [ ] Buka `docs/sdlc/03_design/06_security_design.md`.
- [ ] Verifikasi: Apakah **cost factor bcrypt** (harus `12`) disebutkan secara eksplisit di Dokumen Utama?
- [ ] Verifikasi: Apakah **JWT lifetime** (`28800` detik = 8 jam) konsisten di `.env.example` dan `.env.test`?
- [ ] Verifikasi: Apakah **hak akses granular user database `abucom_app`** (privilege produksi vs. testing) konsisten dengan Security Design?
- [ ] Verifikasi: Apakah **enkripsi Fernet untuk WhatsApp CRM** dan kepatuhan **UU PDP No. 27/2022** sudah dijelaskan dengan lengkap?
- [ ] Verifikasi: Apakah folder backup `chmod 700` (hak akses direktori) sesuai dengan yang ditetapkan Security Design?
- [ ] Verifikasi: Apakah **kode error standar** (`ERR-DB-001`, `ERR-DB-013`) yang disebut di Bab 14 (Troubleshooting) sudah terdefinisi dan konsisten dengan katalog kode error di Security Design?
- [ ] Verifikasi: Apakah **retry mechanism** (3 kali, exponential backoff, MySQL error 2006/2013) sesuai dengan Security Design?
- [ ] Verifikasi: Apakah **`PermitRootLogin no`** untuk SSH hardening sudah tercakup?
- [ ] Catat temuan perbedaan atau ketidakkonsistenan.

#### 1.4. Komparasi dengan Coding Standard
- [ ] Buka `docs/sdlc/04_implementation/01_coding_standard.md`.
- [ ] Verifikasi: Apakah **struktur direktori proyek** (tree di Bab 8.1) konsisten 100% dengan layout yang ditetapkan Coding Standard? Periksa setiap folder dan file:
  - [ ] `cli/` — semua file ada?
  - [ ] `logic/` — semua file ada?
  - [ ] `db/` — semua file ada?
  - [ ] `middleware/` — semua file ada?
  - [ ] `config/` — semua file ada?
  - [ ] `utils/` — semua file ada?
  - [ ] `exports/` — sub-folder lengkap?
  - [ ] `tests/` — semua file ada?
- [ ] Verifikasi: Apakah konten **`.gitignore`** (Bab 8.5) konsisten dengan template di Coding Standard? Ada yang terlewat?
- [ ] Verifikasi: Apakah konten **`.env.example`** (Bab 8.2.1) konsisten dengan template di Coding Standard?
- [ ] Verifikasi: Apakah **konvensi commit message** (Conventional Commits) sudah konsisten dengan yang ditetapkan Coding Standard?
- [ ] Verifikasi: Apakah **connection pool factory** (fungsi `get_connection()` atau `db_connector.py`) sudah dijelaskan cara inisialisasinya?
- [ ] Catat temuan perbedaan atau ketidakkonsistenan.

#### 1.5. Komparasi dengan Database Schema
- [ ] Buka `docs/sdlc/03_design/01_database_schema.sql`.
- [ ] Verifikasi: Apakah jumlah tabel yang disebut di Dokumen Utama (**28 tabel relasional InnoDB**) sesuai dengan jumlah tabel aktual di file schema.sql? Hitung jumlah statement `CREATE TABLE` di file tersebut.
- [ ] Verifikasi: Apakah prosedur eksekusi `schema.sql` (Bab 6.7) sudah mencakup eksekusi ke **kedua** database (`abucom_db` dan `abucom_test_db`)?
- [ ] Verifikasi: Apakah ada **`seed.sql`** yang perlu juga dieksekusi ke `abucom_test_db` untuk data awal testing? Jika ada di schema.sql atau disebutkan di referensi lain, tambahkan instruksi migrasi seed ke testing database.
- [ ] Catat temuan perbedaan atau ketidakkonsistenan.

#### 1.6. Komparasi dengan Software Requirements & Access Control Matrix
- [ ] Buka `docs/sdlc/02_analysis/02_software_requirements.md`.
- [ ] Verifikasi: Apakah persyaratan non-fungsional **performa** (latensi < 1ms LAN) sudah tercakup di Dokumen Utama?
- [ ] Verifikasi: Apakah persyaratan **kompatibilitas dual-OS** (Linux Debian 12 + Windows 11) sudah direpresentasikan dengan lengkap?
- [ ] Buka `docs/sdlc/02_analysis/06_access_control_matrix.md`.
- [ ] Verifikasi: Apakah **8 peran karyawan** yang disebutkan di konteks access control sudah konsisten dengan penjelasan audiens target di Bab 1.5?
- [ ] Catat temuan perbedaan atau ketidakkonsistenan.

---

### TAHAP 2 — Validasi Kelengkapan Konten

**Tujuan**: Memastikan tidak ada informasi yang seharusnya ada dalam panduan setup ini namun terlewat.

#### 2.1. Kelengkapan Instruksi Setup Server
- [ ] Apakah instalasi Debian 12 mencakup langkah **verifikasi checksum ISO** sebelum pembuatan bootable USB?
- [ ] Apakah ada penjelasan mengenai **alokasi partisi swap** yang direkomendasikan untuk server database dengan RAM 16GB?
- [ ] Apakah ada instruksi **update sistem Debian** pasca instalasi (`apt update && apt upgrade -y`) sebelum pemasangan paket lain?
- [ ] Apakah ada instruksi **instalasi paket `sudo`** dan konfigurasi user `abuadm` sebagai sudoer setelah instalasi?
- [ ] Apakah ada penjelasan **verifikasi waktu sistem server** (`timedatectl`) untuk memastikan timestamp log dan audit database konsisten?
- [ ] Apakah ada instruksi **setting timezone** server ke `Asia/Makassar` (WIT) atau zona waktu toko yang relevan?
- [ ] Apakah ada penjelasan konfigurasi `logrotate` atau mekanisme manajemen log server untuk mencegah penuhnya disk?

#### 2.2. Kelengkapan Instruksi Setup Database
- [ ] Apakah ada instruksi konfigurasi **`max_connections`** MySQL (batas koneksi maksimum) di `mysqld.cnf` yang relevan dengan connection pool size 5?
- [ ] Apakah ada instruksi konfigurasi **`innodb_buffer_pool_size`** untuk optimasi performa MySQL di server RAM 16GB?
- [ ] Apakah ada instruksi konfigurasi **`slow_query_log`** untuk membantu debugging query lambat di production?
- [ ] Apakah ada **contoh kode Python** inisialisasi connection pool `mysql.connector.pooling.MySQLConnectionPool` dengan parameter `pool_name='abupool'` dan `pool_size=5` yang sudah terisi lengkap (host, port, user, password, database)?
- [ ] Apakah prosedur **eksekusi seed.sql** ke `abucom_test_db` sudah terdokumentasi (tidak hanya ke `abucom_db`)?

#### 2.3. Kelengkapan Instruksi Setup Python & Keamanan
- [ ] Apakah ada penjelasan perbedaan perintah aktivasi venv antara **Windows CMD** (`venv\Scripts\activate`) vs. **Windows PowerShell** (`venv\Scripts\Activate.ps1`)? Ini kritis karena Windows Terminal dapat menggunakan keduanya.
- [ ] Apakah ada instruksi konfigurasi **`BACKUP_ZIP_PASSWORD`** di `.env` (cara generate password backup yang kuat)?
- [ ] Apakah ada penjelasan **cara memverifikasi Fernet Key** yang sudah digenerate (uji enkripsi/dekripsi cepat)?
- [ ] Apakah ada penjelasan bahwa file `.env` **TIDAK BOLEH** pernah di-commit ke Git (cross-reference dengan `.gitignore`)?

#### 2.4. Kelengkapan Bagian Troubleshooting
- [ ] Apakah ada panduan troubleshooting untuk kasus **Python 3.14 tidak ditemukan di PATH** setelah instalasi di Windows (`python` vs `python3` vs `py`)?
- [ ] Apakah ada panduan troubleshooting untuk kasus **koneksi SSH ke server gagal** (port 22 blocked, kunci host tidak dikenal)?
- [ ] Apakah ada panduan troubleshooting untuk kasus **error MySQL `Access denied for user 'abucom_app'`** (privilege belum di-FLUSH, whitelist IP salah)?
- [ ] Apakah ada panduan untuk kasus **virtual environment tidak teraktivasi** (ciri: tidak ada `(venv)` di prompt)?

---

### TAHAP 3 — Validasi Relevansi Konten (Pembersihan)

**Tujuan**: Memastikan Dokumen Utama hanya berisi informasi yang relevan dan spesifik untuk panduan *environment setup*, bukan informasi yang seharusnya berada di dokumen lain.

- [ ] Baca ulang **Bab 8.3** (Penanganan NULL MySQL ke Python None) dan **Bab 8.4** (Standar Presisi Desimal ROUND_HALF_UP). Nilai apakah kedua sub-bab ini secara logis merupakan bagian dari *environment setup* atau lebih tepat berada di *Coding Standard*. Jika sudah ada di Coding Standard, pertimbangkan apakah perlu dipertahankan sebagai *quick reference* yang diperlukan developer sebelum mulai coding, atau dihapus dengan menambahkan hyperlink cross-reference ke dokumen sumber.
- [ ] Baca ulang **Bab 12.4** (Prosedur Pemulihan/Restore Manual). Nilai apakah snipper SQL `DECLARE...CURSOR` yang ada di sana sudah lengkap dan operasional, atau justru menyesatkan karena belum selesai (hanya ada komentar `-- Pemicuan kill connection loop...`). Jika belum lengkap dan dapat menyesatkan, lengkapi atau hapus dan arahkan ke dokumen pemulihan terpisah jika ada.
- [ ] Periksa seluruh bab: Apakah ada konten yang merupakan **duplikasi** antara dua sub-bab berbeda? Misalnya, konten yang disebutkan di Bab 4 muncul lagi identik di Bab 13 tanpa tambahan nilai. Jika ditemukan, konsolidasi atau beri cross-reference.
- [ ] Periksa: Apakah **Bab 15 (Lampiran)** hanya berisi ringkasan/copy dari konten yang sudah ada di bab utama? Nilai apakah lampiran ini menambah nilai atau hanya redundan. Jika redundan, pastikan setidaknya ada hyperlink internal yang berguna.

---

### TAHAP 4 — Validasi Standar Struktur Dokumen

**Tujuan**: Memastikan dokumen memenuhi standar dokumentasi teknis industri yang profesional dan lengkap.

- [ ] Periksa **header YAML front-matter**: Apakah atribut `dokumen`, `proyek`, `versi`, `tanggal`, `status`, dan `penyusun` sudah lengkap dan akurat?
- [ ] Periksa **Riwayat Perubahan Dokumen**: Apakah tabel riwayat sudah mencantumkan semua versi secara berurutan dan deskripsi perubahannya informatif?
- [ ] Periksa **Bab 1 (Informasi Dokumen)**: Apakah sub-bab 1.1 s/d 1.7 sudah lengkap? Apakah ada definisi/akronim baru yang digunakan dalam dokumen namun belum terdaftar di Bab 1.6?
- [ ] Periksa **diagram Mermaid** (Bab 2.1): Apakah diagram dapat di-render tanpa error? Apakah diagram sudah menggambarkan topologi dengan akurat sesuai System Architecture?
- [ ] Periksa **tabel matriks** (Bab 2.2 dan 2.3): Apakah tabel sudah berisi data yang akurat dan tidak ada sel yang kosong atau berisi placeholder?
- [ ] Periksa **setiap blok kode**: Apakah setiap blok kode sudah:
  - [ ] Memiliki label platform yang jelas (`# [LINUX DEBIAN 12 — Server]` atau `# [WINDOWS 11 — Klien]`)?
  - [ ] Menggunakan sintaks bahasa yang benar (bash, cmd, sql, python, ini)?
  - [ ] Dapat dieksekusi langsung tanpa perlu modifikasi (kecuali bagian yang memang harus diisi manual dan sudah diberi penanda `[HARUS DIISI MANUAL]`)?
- [ ] Periksa **seluruh checklist verifikasi akhir** (Bab 13): Apakah semua item checklist sudah merepresentasikan *seluruh* konfigurasi kritis yang dibahas di bab-bab sebelumnya? Apakah ada item penting yang terlewat?
- [ ] Periksa **Bab 16 (Referensi Dokumen)**: Apakah seluruh file yang direferensikan sudah terdaftar? Apakah ada file baru yang menjadi referensi setelah proses validasi ini namun belum terdaftar?
- [ ] Periksa konsistensi **penomoran bab**: Tidak ada nomor bab yang loncat, duplikat, atau tidak berurutan.
- [ ] Periksa konsistensi **format tabel**: Semua tabel menggunakan format Markdown yang valid dan konsisten.

---

### TAHAP 5 — Validasi Kualitas sebagai Dokumen Input SDLC Selanjutnya

**Tujuan**: Memastikan dokumen ini dapat menjadi input yang solid dan tidak ambigu untuk fase SDLC berikutnya (pengkodean modul).

- [ ] Evaluasi: Apakah seorang Junior Programmer yang **baru bergabung** dapat mengikuti panduan ini dari awal hingga akhir tanpa perlu bertanya kepada senior?
- [ ] Evaluasi: Apakah seorang model AI yang akan **menulis kode modul** dapat menggunakan dokumen ini sebagai sumber kebenaran tunggal untuk:
  - [ ] Mengetahui cara menginisialisasi koneksi database (pool name, size, host, port)?
  - [ ] Mengetahui versi dan nama library yang boleh diimport?
  - [ ] Mengetahui struktur folder tempat menyimpan file kode?
  - [ ] Mengetahui variabel environment apa saja yang tersedia di `settings.py`?
  - [ ] Mengetahui cara menangani error koneksi database (kode error, retry)?
- [ ] Evaluasi: Apakah setiap instruksi konfigurasi sudah memiliki **langkah verifikasi** yang dapat dilakukan untuk memastikan konfigurasi berhasil (bukan hanya instruksi, tapi juga cara mengeceknya)?
- [ ] Evaluasi: Apakah ada **keputusan teknis yang bergantung pada kondisi toko** (IP gateway, port printer, nama akun) yang sudah diberi penanda `[HARUS DIISI MANUAL]` yang jelas?

---

### TAHAP 6 — Validasi Kualitas Bahasa Indonesia

**Tujuan**: Memastikan dokumen menggunakan Bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami oleh Junior Programmer atau model AI murah.

- [ ] Baca ulang seluruh dokumen dengan fokus pada kalimat-kalimat instruksi. Tandai kalimat yang:
  - [ ] Mengandung istilah teknis bahasa Inggris yang digunakan tanpa penjelasan (padahal belum ada di Bab 1.6).
  - [ ] Ambigu — dapat diinterpretasikan lebih dari satu cara.
  - [ ] Terlalu panjang sehingga sulit dipahami dalam satu kali baca.
  - [ ] Menggunakan kata ganti orang yang tidak konsisten (campuran "kita", "anda", "kamu").
- [ ] Periksa: Apakah **notasi peringatan** (`⚠️ [HARUS DIISI MANUAL]`, `[KRITIS]`, `[CATATAN OFFLINE-ONLY LAN]`, `[JUSTIFIKASI TEKNIS]`) sudah konsisten digunakan di seluruh dokumen untuk membantu pembaca mengidentifikasi bagian penting?
- [ ] Periksa: Apakah penulisan nama teknologi asing sudah konsisten (misalnya: `mysql_secure_installation` selalu dalam format `code`)?
- [ ] Perbaiki setiap kalimat yang ditemukan bermasalah secara langsung.

---

### TAHAP 7 — Validasi Kelengkapan dan Pengisian Data Kosong

**Tujuan**: Menemukan dan mengisi seluruh placeholder, data kosong, atau informasi yang perlu dilengkapi agar dokumen bersifat self-contained.

- [ ] Cari seluruh kemunculan teks `YOUR_*_HERE` di Dokumen Utama. Untuk setiap kemunculan:
  - [ ] `YOUR_DB_PASSWORD_HERE` — Ini memang harus diisi manual oleh pemilik. Pastikan ada instruksi cara memilih password kuat yang terdokumentasi di sekitarnya. Jika belum ada instruksi spesifik (misalnya panjang minimum, karakter yang diperlukan), tambahkan.
  - [ ] `YOUR_JWT_SECRET_KEY_HERE` — Pastikan ada perintah generator yang siap dijalankan (sudah ada di Bab 8.2.3, verifikasi masih benar).
  - [ ] `YOUR_FERNET_KEY_HERE` — Pastikan ada perintah generator yang siap dijalankan (sudah ada di Bab 8.2.4, verifikasi masih benar).
  - [ ] `YOUR_BACKUP_ZIP_PASSWORD_HERE` — Apakah ada instruksi cara generate password backup yang kuat? Jika belum ada, tambahkan contoh perintah generator.
- [ ] Periksa **Bab 12.4 (Prosedur Pemulihan)**: Blok kode SQL `DECLARE...CURSOR` berakhir dengan komentar `-- Pemicuan kill connection loop...` yang tidak lengkap. Ini adalah **data kosong kritis**. Lengkapi blok kode SQL tersebut dengan implementasi penuh prosedur `KILL` connection, atau hapus snippet yang menyesatkan dan gantikan dengan penjelasan narasi yang lengkap tentang langkah restore yang aman.
- [ ] Periksa **Bab 9.2 (Konfigurasi Git Identity)**: Email placeholder `donsise@example.com` — Apakah ini sudah diberi penanda `[HARUS DIISI MANUAL]`? Jika belum, tambahkan.
- [ ] Periksa **Bab 7.1 (Pembuatan venv)**: Path `C:\\Users\\donsise\\Documents\\abucom` — Apakah ini sudah diberi penanda bahwa path ini bersifat contoh dan harus disesuaikan? Jika belum, tambahkan catatan.
- [ ] Periksa **Bab 5.2 (Instalasi Python di Windows)**: Langkah 3 berbunyi `[KRITIS — WAJIB] Pada layar instalasi awal, centang checkbox berikut di bagian bawah layar:` tetapi **tidak ada item checkbox yang disebutkan** (kalimat tergantung). Ini adalah data kosong kritis. Tambahkan item checkbox yang seharusnya ada: `☑ Add Python 3.14 to PATH`.
- [ ] Periksa seluruh tabel: Apakah ada sel tabel yang berisi teks `—`, `TBD`, `N/A`, atau kosong yang seharusnya berisi data? Isi dengan data yang sesuai.
- [ ] Periksa **Bab 11.3 (`.env.test`)**: Nilai `FERNET_KEY` di file `.env.test` adalah `H_v3b02_vG7Y88c2b7n9mK8V9c2bL0n9mKw8V_c2bG7=`. Ini adalah key dummy yang terlihat seperti key valid namun belum tentu valid secara format Fernet (32 byte base64 URL-safe). Verifikasi apakah format ini valid, atau gantikan dengan key dummy yang jelas-jelas valid (bisa digenerate sekali dan dijadikan contoh permanen testing).

---

### TAHAP 8 — Pemeriksaan Konsistensi Teknis Spesifik

**Tujuan**: Melakukan pemeriksaan teknis mendalam terhadap detail-detail kritis yang unik untuk dokumen Environment Setup ini.

- [ ] **Cek Konfigurasi Offline vs Online**: Pastikan setiap instruksi yang memerlukan internet (wget, apt install, pip install) sudah dilengkapi dengan prosedur **offline alternatif** yang jelas. Verifikasi:
  - [ ] Instalasi dependensi build Python di Debian (Bab 4.4) — offline deb tercakup?
  - [ ] Download Python 3.14 tarball (Bab 4.4) — offline USB tercakup?
  - [ ] Instalasi MySQL (Bab 6.1) — offline dpkg tercakup?
  - [ ] Instalasi pip packages (Bab 7.2) — offline wheels tercakup?
  - [ ] Instalasi apcupsd (Bab 10.2) — offline deb tercakup?
  - [ ] Instalasi zip/unzip (Bab 12.2) — offline deb tercakup?
- [ ] **Cek Konsistensi IP**: Cari semua kemunculan IP address dalam dokumen. Pastikan semuanya menggunakan `192.168.1.200` untuk server dan `192.168.1.0/24` untuk subnet LAN secara konsisten.
- [ ] **Cek Konsistensi Nama Entitas**: Pastikan nama-nama berikut konsisten di seluruh dokumen:
  - [ ] Database produksi: `abucom_db` (bukan `abucom` atau variasi lain).
  - [ ] Database testing: `abucom_test_db`.
  - [ ] User database: `abucom_app`.
  - [ ] Pool name: `'abupool'`.
  - [ ] Hostname server: `abuserver`.
  - [ ] User admin server: `abuadm`.
- [ ] **Cek Urutan Eksekusi**: Validasi bahwa urutan bab-bab setup sudah logis dan tidak ada ketergantungan yang mengharuskan melakukan langkah di bab yang lebih belakang sebelum langkah di bab yang lebih depan.
- [ ] **Cek Kelengkapan Checklist Akhir (Bab 13)**: Cocokkan setiap item checklist di Bab 13.1 s/d 13.5 dengan instruksi yang ada di bab-bab sebelumnya. Pastikan tidak ada konfigurasi yang diinstruksikan di bab sebelumnya namun tidak ada di checklist akhir. Tambahkan item yang kurang.

---

### TAHAP 9 — Penulisan Ulang Dokumen (Overwrite)

> ⚠️ **INSTRUKSI KRITIS — WAJIB DIIKUTI TANPA KOMPROMI**

Setelah seluruh Tahap 1 hingga Tahap 8 selesai dieksekusi dan seluruh temuan dicatat, lakukan penulisan ulang dokumen target dengan aturan mutlak berikut:

#### 9.1. Aturan Penulisan Ulang
- [ ] **[BACA ATURAN INI SEBELUM MENULIS]** Seluruh isi dokumen dari baris pertama hingga baris terakhir **HARUS ditulis ulang sepenuhnya** menggunakan tool `write_to_file` atau setara dengan parameter overwrite `true`.
- [ ] **[DILARANG]** Memotong, meringkas, atau menghilangkan konten yang sudah valid dan benar. **NO TRUNCATION**.
- [ ] **[DILARANG]** Menggunakan kata-kata seperti `[lanjutan...]`, `[konten yang sama...]`, `[...isi sebelumnya...]`, atau sejenisnya. Setiap baris harus ditulis eksplisit.
- [ ] Perbarui **versi dokumen** dari `v1.1` menjadi `v1.2` di:
  - [ ] Header YAML front-matter (`versi: 1.2`).
  - [ ] Tabel **Riwayat Perubahan Dokumen**: Tambahkan baris baru v1.2 di paling atas tabel dengan tanggal hari ini dan ringkasan seluruh perubahan yang dilakukan.
- [ ] Terapkan **seluruh perbaikan** yang ditemukan di Tahap 1 s/d 8 ke dalam dokumen yang ditulis ulang.
- [ ] Pastikan dokumen hasil overwrite dapat dibuka dan dibaca tanpa error format Markdown.

#### 9.2. Pembaruan Tabel Riwayat
Tambahkan baris baru di paling atas tabel riwayat dengan format:

```markdown
| **1.2** | [TANGGAL_HARI_INI] | [Ringkasan perubahan: sebutkan minimal 5 poin utama perubahan yang dilakukan, misalnya: melengkapi langkah instalasi checkbox Python di Windows, melengkapi prosedur SQL restore manual, menambahkan instruksi timezone server, dst.] | [Nama Pelaksana / Model AI] |
```

#### 9.3. Pembaruan Tabel Referensi (Bab 16)
- [ ] Jika selama proses validasi ditemukan bahwa ada file referensi **baru** yang digunakan sebagai dasar perbaikan namun belum terdaftar di Bab 16, tambahkan file tersebut ke tabel referensi di baris paling bawah tabel.
- [ ] Format penambahan referensi baru:

```markdown
| [No] | [Nama Dokumen] | `[path/relatif/ke/file]` | [versi] | **[PRIMER/SEKUNDER/TERSIER]** | [Deskripsi peran referensi dalam penyusunan] |
```

---

## 5. Kriteria Keberhasilan

Tugas ini dinyatakan **SELESAI DAN BERHASIL** jika dan hanya jika seluruh kondisi berikut terpenuhi:

- [ ] Seluruh checklist di Tahap 1 hingga Tahap 8 telah ditandai `[x]`.
- [ ] File `docs/sdlc/04_implementation/02_environment_setup.md` telah di-overwrite dengan konten baru versi v1.2.
- [ ] Versi dokumen di header YAML dan tabel riwayat sudah diperbarui ke `v1.2`.
- [ ] Tidak ada satu baris pun konten yang valid dipotong atau dihilangkan dari dokumen hasil.
- [ ] Seluruh placeholder `YOUR_*_HERE` sudah dilengkapi dengan instruksi generator yang dapat dieksekusi atau catatan `[HARUS DIISI MANUAL]` yang jelas.
- [ ] Inkonsistensi teknis antara Dokumen Utama dengan file referensi sudah diperbaiki.
- [ ] Data kosong kritis (terutama Bab 5.2 langkah 3 dan Bab 12.4 blok SQL) sudah dilengkapi atau diperbaiki.
- [ ] Jika ada referensi baru, sudah ditambahkan di bagian akhir Bab 16 tabel referensi.

---

## 6. Catatan Penting untuk Pelaksana

> **[KEPADA JUNIOR PROGRAMMER / MODEL AI PELAKSANA]**

1. **Jangan skip membaca file referensi**. Kualitas validasi sangat bergantung pada pemahaman penuh terhadap seluruh dokumen referensi. Membaca sebagian saja akan menghasilkan validasi yang tidak lengkap.

2. **Jangan melakukan asumsi**. Jika ada informasi yang tidak dapat ditemukan di file referensi manapun, tandai dengan `[PERLU KLARIFIKASI OWNER]` dan jangan mengarang data.

3. **Prioritaskan keamanan data**. Seluruh instruksi yang berkaitan dengan password, kunci enkripsi, dan hak akses harus divalidasi ulang secara sangat teliti. Kesalahan kecil di sini dapat berdampak besar pada keamanan sistem produksi toko.

4. **Jaga semangat dokumen**. Dokumen ini ditujukan untuk Junior Programmer (pemilik usaha) yang tidak memiliki latar belakang teknis mendalam dan untuk model AI berbiaya rendah. Setiap instruksi harus dapat dipahami dan dieksekusi **tanpa pengetahuan sebelumnya** tentang sistem.

5. **Jangan partial write**. Ketika menulis ulang file (Tahap 9), pastikan seluruh konten berhasil tertulis dalam satu operasi penuh. Verifikasi setelah selesai menulis dengan membaca ulang file yang baru ditulis untuk memastikan tidak ada konten yang terpotong di akhir.

---

*Issue ini dibuat pada: 2026-05-29 | Dibuat oleh: Antigravity (Senior AI Engineer)*
*Ditugaskan kepada: Junior Programmer / Model AI Pelaksana*
