---
judul      : Validasi, Analisis, dan Penyempurnaan Dokumen Security Design
target     : docs/sdlc/03_design/06_security_design.md
referensi  : docs/sdlc/
prioritas  : Tinggi
status     : Open
dibuat_pada: 2026-05-25
---

# Issue 0034 — Validasi, Analisis, dan Penyempurnaan Dokumen Security Design

## 1. Latar Belakang dan Tujuan Issue

Dokumen **Security Design** (`docs/sdlc/03_design/06_security_design.md`) telah disusun pada fase sebelumnya sebagai *blueprint* keamanan sistem AbuCom. Issue ini bertujuan untuk melakukan audit menyeluruh dan validasi ketat terhadap dokumen tersebut sebelum dokumen ini resmi dijadikan acuan utama pada **Fase 04 — Implementation** dan **Fase 05 — Testing**.

Implementor issue ini **wajib** menjalankan seluruh tahapan secara berurutan, satu per satu, tanpa melewati satu pun langkah, hingga seluruh checklist bertanda `[x]`.

> **Penting**: Seluruh instruksi di sini bersifat **deterministik** dan **low-level**. Jangan membuat asumsi atau keputusan mandiri di luar yang tertera. Jika menemukan ambiguitas, ikuti instruksi yang paling konservatif (tidak menghapus data kecuali diperintahkan secara eksplisit).

---

## 2. Persona Pelaksana

Jalankan seluruh tugas ini dengan menginternalisasi persona gabungan berikut secara simultan:

- **Senior Security Architect** — Berpengalaman dalam threat modeling, desain RBAC multi-level, penerapan enkripsi at-rest/in-transit, dan standar regulasi perlindungan data (ISO 27001, OWASP, UU PDP No. 27/2022). Tugasnya memastikan setiap detail teknis keamanan sudah benar, lengkap, dan tidak ambigu.
- **Technical Writer Senior (Bahasa Indonesia)** — Ahli penulisan dokumentasi teknis industri berbahasa Indonesia yang natural, baku, tidak ambigu, dan mudah dipahami oleh junior programmer maupun model AI yang lebih kecil. Tugasnya memastikan setiap kalimat dalam dokumen tidak berpotensi disalahartikan.
- **QA Analyst SDLC** — Bertugas memastikan dokumen ini bebas dari celah informasi yang akan memaksa implementor fase selanjutnya menghentikan pekerjaan karena ketidaklengkapan dokumen.

---

## 3. Peta File yang Terlibat

Baca dan pahami seluruh file berikut sebelum memulai validasi. File bertanda **[TARGET]** adalah dokumen yang akan dimodifikasi. File bertanda **[REF]** adalah referensi yang hanya dibaca, tidak boleh dimodifikasi.

| Status | Path File | Keterangan |
|---|---|---|
| **[TARGET]** | `docs/sdlc/03_design/06_security_design.md` | Dokumen utama yang divalidasi dan di-overwrite |
| **[REF-01]** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Sumber definisi 8 peran RBAC, eskalasi, rate limiting, session JWT, audit trail |
| **[REF-02]** | `docs/sdlc/03_design/03_system_architecture.md` | Sumber topologi LAN, OS hardening, isolation level DB, backup, sequence diagram login |
| **[REF-03]** | `docs/sdlc/02_analysis/02_software_requirements.md` | Sumber kebutuhan fungsional M.7 Keamanan, non-fungsional, pustaka dependency, kode error |
| **[REF-04]** | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Sumber parameter bcrypt cost 12, JWT HS256, parameterized queries, .env, requirements.txt |
| **[REF-05]** | `docs/sdlc/03_design/01_database_schema.sql` | Sumber DDL fisik tabel pengguna, audit_logs, shift_handover, backup_logs, system_configs |
| **[REF-06]** | `docs/sdlc/03_design/02_erd_database.md` | Sumber relasi FK visual untuk penelusuran data audit |
| **[REF-07]** | `docs/sdlc/02_analysis/01_business_requirements.md` | Sumber kebutuhan bisnis keamanan asli (BR-F-30 s.d BR-F-34) |
| **[REF-08]** | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Sumber visualisasi otorisasi kasir dan serah terima shift harian |

---

## 4. Tahapan Implementasi (Checklist Berurutan)

Kerjakan setiap tahap secara berurutan dari atas ke bawah. Tandai `[x]` setelah setiap sub-tugas selesai dikerjakan. **Jangan lanjut ke tahap berikutnya sebelum tahap sebelumnya selesai seluruhnya.**

---

### TAHAP 0 — Persiapan Lingkungan Kerja

- [ ] **T0.1** — Baca seluruh isi file **[TARGET]** `docs/sdlc/03_design/06_security_design.md` dari baris pertama hingga baris terakhir dan simpan seluruh isinya ke dalam memori kerja sesi ini (context window). Jangan skip atau truncate saat membaca.
- [ ] **T0.2** — Baca seluruh isi **[REF-01]** `docs/sdlc/02_analysis/06_access_control_matrix.md` dari baris pertama hingga baris terakhir. Simpan semua data penting ke dalam memori kerja.
- [ ] **T0.3** — Baca seluruh isi **[REF-02]** `docs/sdlc/03_design/03_system_architecture.md` dari baris pertama hingga baris terakhir. Simpan semua data penting ke dalam memori kerja.
- [ ] **T0.4** — Baca seluruh isi **[REF-03]** `docs/sdlc/02_analysis/02_software_requirements.md` dari baris pertama hingga baris terakhir. Simpan semua data penting ke dalam memori kerja.
- [ ] **T0.5** — Baca seluruh isi **[REF-04]** `docs/sdlc/01_planning/04_tech_stack_decision.md` dari baris pertama hingga baris terakhir. Simpan semua data penting ke dalam memori kerja.
- [ ] **T0.6** — Baca seluruh isi **[REF-05]** `docs/sdlc/03_design/01_database_schema.sql` dari baris pertama hingga baris terakhir. Fokus pada DDL tabel: `pengguna`, `audit_logs`, `backup_logs`, `shift_handover`, `system_configs`. Simpan semua data penting ke dalam memori kerja.
- [ ] **T0.7** — Baca seluruh isi **[REF-06]** `docs/sdlc/03_design/02_erd_database.md` dari baris pertama hingga baris terakhir. Simpan semua data penting ke dalam memori kerja.
- [ ] **T0.8** — Baca seluruh isi **[REF-07]** `docs/sdlc/02_analysis/01_business_requirements.md` dari baris pertama hingga baris terakhir. Fokus pada klausa kebutuhan keamanan (BR-F-30 s.d BR-F-34). Simpan semua data penting ke dalam memori kerja.
- [ ] **T0.9** — Baca seluruh isi **[REF-08]** `docs/sdlc/02_analysis/04_workflow_diagram.md` dari baris pertama hingga baris terakhir. Fokus pada diagram yang berkaitan dengan alur otorisasi, shift handover, dan login. Simpan semua data penting ke dalam memori kerja.
- [ ] **T0.10** — Konfirmasi bahwa seluruh 9 file (1 target + 8 referensi) telah dibaca lengkap sebelum memulai Tahap 1.

---

### TAHAP 1 — Validasi Kelengkapan Data dari File Referensi

**Tujuan**: Memastikan dokumen [TARGET] tidak melewatkan satu pun data atau informasi penting yang ada di dalam file referensi dan relevan untuk dokumen Security Design.

Untuk setiap sub-tugas di bawah, lakukan pemeriksaan silang (*cross-check*) antara isi dokumen [TARGET] dengan data yang ada di file referensi terkait. Catat setiap temuan ketidaklengkapan di Bagian 7 (Catatan Temuan).

#### 1.A — Validasi terhadap REF-01 (Access Control Matrix)

- [ ] **T1.A.1** — Periksa apakah semua **8 peran RBAC** yang tercantum di REF-01 sudah terdaftar di dokumen target pada Bab 5. Pastikan tidak ada peran yang hilang atau berbeda nama. Nama 8 peran yang valid: `pemilik`, `kepala_percetakan`, `pramuniaga`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang`.
- [ ] **T1.A.2** — Periksa apakah **matriks hak akses** di Bab 5.3 dokumen target sudah mencakup semua 10 modul (M.1 s.d M.10) sesuai dengan matriks ACM di REF-01. Pastikan simbol akses (`✅ FULL`, `📖 READ`, `📝 INPUT`, `🔒 RTL`, `🔐 ESC`, `⛔ DENY`) untuk setiap kombinasi peran-modul sudah konsisten dan tidak ada yang berbeda.
- [ ] **T1.A.3** — Periksa apakah **aturan eskalasi pemilik** (Bab 5.4) sudah memuat seluruh pemicu eskalasi yang ada di ACM Bab 6.1. Pastikan tidak ada operasi kritis yang terlewat.
- [ ] **T1.A.4** — Periksa apakah **aturan otorisasi kepala percetakan** (Bab 5.5) sudah mencakup seluruh item otorisasi supervisor dari ACM Bab 6.2.
- [ ] **T1.A.5** — Periksa apakah **parameter rate limiting** (Bab 4.3) sudah konsisten dengan nilai di ACM Bab 6.5: threshold 5 kali gagal, suspensi 10 menit, kolom database `failed_login_attempts` dan `locked_until`.
- [ ] **T1.A.6** — Periksa apakah **format audit log ACCESS_DENIED** (Bab 7) sudah konsisten dengan spesifikasi yang ada di ACM Bab 6.6.
- [ ] **T1.A.7** — Periksa apakah ada **aturan sesi JWT** (payload, masa berlaku, klaim khusus) yang tertulis di REF-01 tetapi belum terdokumentasi di Bab 4.2 dokumen target. Jika ada, catat sebagai temuan gap di Bagian 7.

#### 1.B — Validasi terhadap REF-02 (System Architecture)

- [ ] **T1.B.1** — Periksa apakah **konfigurasi jaringan LAN** (Bab 3.2) di dokumen target sudah sinkron dengan detail topologi di REF-02: IP server statis `192.168.1.200`, aturan ufw, bind-address MySQL, dan jenis kabel UTP Cat6.
- [ ] **T1.B.2** — Periksa apakah **konfigurasi OS hardening** (Bab 3.3) sudah mencakup seluruh langkah hardening yang ada di REF-02 untuk Debian 12 server dan Windows 11 klien, termasuk konfigurasi SSH (`PermitRootLogin no`), `chmod 700` direktori backup, dan penonaktifan USB autorun Windows.
- [ ] **T1.B.3** — Periksa apakah **spesifikasi database isolation level** `REPEATABLE READ` (Bab 3.4) sudah selaras dengan konfigurasi di REF-02. Catat jika ada perbedaan nama atau nilai.
- [ ] **T1.B.4** — Periksa apakah **prosedur backup** (Bab 8.2) sudah mencerminkan jadwal, mekanisme, dan lokasi folder backup yang ditetapkan di REF-02, termasuk folder `/exports/backups/` dan format file `.zip`.
- [ ] **T1.B.5** — Periksa apakah ada **diagram sequence login** di REF-02 yang memiliki langkah atau entitas yang berbeda dari diagram di Bab 9.1 dokumen target. Jika ada perbedaan, tandai sebagai temuan inkonsistensi di Bagian 7.

#### 1.C — Validasi terhadap REF-03 (Software Requirements Specification)

- [ ] **T1.C.1** — Periksa apakah semua **kode error keamanan** yang terdefinisi di kamus error SRS (ERR-AUTH-xxx, ERR-SESSION-xxx, ERR-DB-xxx, ERR-FILE-xxx, ERR-CASH-xxx) sudah terdokumentasi seluruhnya di Bab 10 dokumen target. Tidak boleh ada satu kode pun yang terlewat. Buat daftar kode error di SRS, lalu bandingkan satu per satu dengan yang ada di Bab 10.
- [ ] **T1.C.2** — Periksa apakah **kebutuhan fungsional M.7 Keamanan** dari SRS sudah sepenuhnya dijabarkan di dokumen target. Lakukan inventarisasi setiap item di SRS dan cocokkan dengan bab yang relevan di dokumen target.
- [ ] **T1.C.3** — Periksa apakah **kebutuhan non-fungsional keamanan** di SRS (termasuk SRS-NF-001 dan SRS-NF-002) sudah terdokumentasi dan terpetakan di matriks Bab 13.1 dokumen target.
- [ ] **T1.C.4** — Periksa apakah **daftar pustaka / dependency** yang berkaitan dengan keamanan (seperti `bcrypt`, `PyJWT`, `cryptography`, `mysql-connector-python`) dari SRS sudah disebutkan di dokumen target pada bagian yang relevan (Bab 4 atau Bab 6).
- [ ] **T1.C.5** — Periksa apakah **matriks ketertelusuran (traceability)** di Bab 13 dokumen target sudah mencakup seluruh ID SRS yang terkait keamanan (SRS-F-030, SRS-F-031, SRS-F-032, SRS-F-033, SRS-F-034, SRS-F-039, SRS-NF-001, SRS-NF-002). Tidak boleh ada ID yang terlewat.

#### 1.D — Validasi terhadap REF-04 (Tech Stack Decision)

- [ ] **T1.D.1** — Periksa apakah **parameter teknis bcrypt** di Bab 4.1 konsisten dengan TSD: cost factor `12`, dynamic salt generation menggunakan `bcrypt.gensalt(12)`.
- [ ] **T1.D.2** — Periksa apakah **parameter teknis JWT** di Bab 4.2 konsisten dengan TSD: algoritma `HS256`, durasi `8 jam / 28.800 detik`, penyimpanan secret key di berkas `.env`.
- [ ] **T1.D.3** — Periksa apakah **larangan f-string SQL** dan kewajiban **parameterized query `%s`** di Bab 3.4 dan 6.4 konsisten dengan yang ditetapkan di TSD.
- [ ] **T1.D.4** — Periksa apakah **spesifikasi variabel berkas `.env`** (nama-nama variabel yang wajib ada) di Bab 6.5 dokumen target sudah lengkap sesuai TSD. Buat daftar variabel `.env` di TSD, bandingkan dengan yang disebutkan di Bab 6.5. Jika ada variabel yang disebutkan di TSD tapi tidak ada di dokumen target, tandai sebagai gap.
- [ ] **T1.D.5** — Periksa apakah **nama library/modul keamanan** yang disebutkan di dokumen target (`bcrypt`, `PyJWT`, `cryptography.fernet`) sudah ada dalam daftar `requirements.txt` yang disebutkan di TSD. Pastikan tidak ada inkonsistensi nama paket.

#### 1.E — Validasi terhadap REF-05 (Database Schema SQL)

- [ ] **T1.E.1** — Buka DDL tabel `pengguna` di REF-05. Bandingkan setiap kolom yang dirujuk di dokumen target (kolom `failed_login_attempts`, `locked_until`, `password_hash`, `role`, `cabang_id`) dengan DDL fisik. Periksa tipe data, nilai DEFAULT, dan constraint secara eksak. Catat perbedaan.
- [ ] **T1.E.2** — Bandingkan **DDL tabel `audit_logs`** yang dijabarkan di Bab 7.1 dokumen target dengan DDL fisik di REF-05, kolom per kolom: `id`, `pengguna_id`, `action_timestamp`, `action_type`, `target_table`, `old_value`, `new_value`, `ip_address`, `cabang_id`. Periksa tipe data, COMMENT, FOREIGN KEY, dan ENGINE. Catat perbedaan.
- [ ] **T1.E.3** — Buka DDL tabel `shift_handover` di REF-05. Periksa apakah semua kolom yang direferensikan di Bab 8.1 dokumen target (`status_handover`, `kas_fisik`, `kas_sistem`, `selisih`, `supervisor_id`, `memo_anomali`) ada secara eksak di DDL fisik. Catat perbedaan nama atau tipe data.
- [ ] **T1.E.4** — Buka DDL tabel `backup_logs` di REF-05. Periksa apakah semua kolom yang dirujuk di Bab 8.2 dokumen target ada di DDL fisik. Catat perbedaan.
- [ ] **T1.E.5** — Verifikasi bahwa semua **nama tabel** dalam klasifikasi "Sangat Sensitif" di Bab 2.3 (`pinjaman_bank`, `pinjaman_kerabat`, `payroll`, `system_configs`, `backup_logs`) ada di DDL REF-05. Jika ada nama tabel yang berbeda, tandai sebagai inkonsistensi.

#### 1.F — Validasi terhadap REF-06, REF-07, REF-08

- [ ] **T1.F.1** — Periksa apakah **relasi FK** yang disebutkan di dokumen target (khususnya FK di tabel `audit_logs` ke `pengguna` dan `cabang`) sudah konsisten dengan ERD di REF-06. Catat jika ada entitas atau relasi yang berbeda.
- [ ] **T1.F.2** — Buka REF-07 (BRD) dan buat daftar semua kebutuhan bisnis keamanan (BR-F-30 s.d BR-F-34). Untuk setiap BR, identifikasi bab mana di dokumen target yang mencakupnya. Jika ada BR yang tidak tercakup, catat sebagai gap.
- [ ] **T1.F.3** — Buka REF-08 (Workflow Diagram) dan periksa diagram alur otorisasi kasir serta diagram shift handover. Bandingkan dengan Sequence Diagram di Bab 9.2 dan Bab 9.4 dokumen target. Periksa apakah ada langkah alur yang berbeda atau actor yang hilang/berbeda.

---

### TAHAP 2 — Validasi Kesesuaian Konten dengan Domain Security Design

**Tujuan**: Memastikan dokumen ini hanya memuat konten yang memang merupakan domain Security Design, tidak memuat konten yang seharusnya berada di dokumen SDLC lain.

- [ ] **T2.1** — Baca ulang judul dan isi setiap bab dan sub-bab dokumen target. Identifikasi apakah ada konten yang bukan merupakan domain dokumen Security Design. Contoh konten yang **TIDAK** seharusnya ada: detail desain UI/UX, logika bisnis non-keamanan, kalkulasi HPP/BOM, desain antrian kerja, desain rincian transaksi yang tidak berkaitan dengan keamanan. Catat setiap temuan di Bagian 7.
- [ ] **T2.2** — Untuk setiap bab utama (Bab 2 s.d Bab 15), pastikan kontennya memiliki relevansi langsung dengan salah satu dari aspek keamanan berikut: (a) Ancaman/Threat Modeling, (b) Kontrol Teknis Keamanan, (c) Kebijakan Akses dan Otorisasi, (d) Perlindungan dan Enkripsi Data, (e) Audit dan Monitoring, (f) Prosedur Keamanan Operasional, (g) Respons Insiden Keamanan. Jika ada bab yang tidak jelas relevansinya, tandai sebagai temuan.
- [ ] **T2.3** — Periksa apakah **Bab 12 (Pseudocode)** berisi pseudocode yang spesifik untuk modul keamanan inti saja: `middleware/rbac.py`, `middleware/logger.py`, `utils/crypto.py`, `utils/backup.py`. Jika ditemukan pseudocode untuk modul non-keamanan, tandai sebagai tidak relevan.
- [ ] **T2.4** — Periksa apakah **Bab 11 (Analisis Risiko)** hanya memuat risiko yang berkaitan dengan keamanan teknis sistem (bukan risiko bisnis umum seperti risiko pasar, risiko SDM non-keamanan, atau risiko operasional non-teknis). Jika ada risiko yang tidak relevan, tandai.

---

### TAHAP 3 — Validasi Standar Struktur Dokumen Industri

**Tujuan**: Memastikan dokumen ini memenuhi standar struktur dokumentasi Security Design industri perangkat lunak.

Dokumen Security Design yang baik untuk UMKM harus memiliki setidaknya elemen struktur berikut. Periksa satu per satu:

- [ ] **T3.1** — **Frontmatter / Header Dokumen**: Pastikan ada blok metadata YAML di bagian paling atas. Verifikasi semua field terisi: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`.
- [ ] **T3.2** — **Riwayat Perubahan Dokumen (Changelog)**: Pastikan ada tabel riwayat versi yang mencatat setiap perubahan. Verifikasi formatnya lengkap: kolom Versi, Tanggal, Perubahan, Oleh.
- [ ] **T3.3** — **Tujuan dan Cakupan Dokumen**: Pastikan Bab 1.1 (Tujuan) dan 1.2 (Cakupan) sudah menjelaskan dengan spesifik apa yang dicakup dokumen ini. Verifikasi semua poin di Bab 1.2 sudah benar-benar terwakili oleh bab-bab dalam dokumen (lakukan mapping: poin cakupan → bab).
- [ ] **T3.4** — **Definisi, Akronim, dan Singkatan**: Periksa apakah ada istilah teknis yang digunakan di badan dokumen tetapi tidak terdefinisi di Bab 1.6 atau Bab 15 (Glosarium). Buat daftar istilah yang perlu ditambahkan.
- [ ] **T3.5** — **Prinsip Keamanan** (Bab 2.1): Verifikasi keenam prinsip (Least Privilege, Defense in Depth, Separation of Duties, Default Deny, Fail-Secure, Data Minimization) sudah dijabarkan dengan jelas dan tidak ambigu.
- [ ] **T3.6** — **Model Ancaman** (Bab 2.2): Verifikasi tabel threat model sudah memuat semua kolom wajib: ID Ancaman, Sumber Ancaman, Deskripsi Ancaman, Dampak, Rencana Mitigasi. Hitung jumlah baris ancaman. Pastikan setidaknya mencakup 8 ancaman utama yang sudah ada.
- [ ] **T3.7** — **Arsitektur Keamanan Berlapis** (Bab 3.1): Verifikasi diagram Mermaid `graph TD` dapat di-render dengan benar secara sintaks (periksa manual: setiap node sudah tertutup kurung, setiap panah menggunakan `-->` yang benar, tidak ada karakter yang tidak valid).
- [ ] **T3.8** — **Desain Otentikasi** (Bab 4): Verifikasi semua sub-bab ada dan terisi: 4.1 bcrypt, 4.2 JWT, 4.3 Rate Limiting, 4.4 Logout. Tidak boleh ada sub-bab yang kosong atau hanya berisi judul tanpa konten.
- [ ] **T3.9** — **Desain Otorisasi** (Bab 5): Verifikasi semua sub-bab ada dan terisi: 5.1 RBAC, 5.2 Guard/Decorator, 5.3 Matriks Akses, 5.4 Eskalasi Pemilik, 5.5 Otorisasi Kepala Percetakan, 5.6 Default Deny.
- [ ] **T3.10** — **Desain Perlindungan Data** (Bab 6): Verifikasi semua sub-bab ada dan terisi: 6.1 Data at Rest, 6.2 Data in Transit, 6.3 Kepatuhan UU PDP, 6.4 Input Validation, 6.5 Manajemen Kredensial, 6.6 Klasifikasi Tabel.
- [ ] **T3.11** — **Desain Audit Trail** (Bab 7): Verifikasi semua sub-bab ada dan terisi: 7.1 Skema Tabel, 7.2 Event Pemicu, 7.3 Format JSON, 7.4 Deteksi Anomali, 7.5 Retensi Log.
- [ ] **T3.12** — **Prosedur Operasional Keamanan** (Bab 8): Verifikasi semua sub-bab ada dan terisi: 8.1 Shift Handover, 8.2 Backup dan Restore, 8.3 Pengelolaan Akun, 8.4 Keamanan Fisik Server.
- [ ] **T3.13** — **Diagram Alur Keamanan** (Bab 9): Hitung secara manual jumlah blok kode ` ```mermaid ` di seluruh dokumen. Verifikasi jumlahnya tepat **6 diagram**. Verifikasi keenam diagram tidak ada yang kosong: 9.1 Login, 9.2 Otorisasi Transaksi, 9.3 Retur/Pembatalan, 9.4 Shift Handover, 9.5 Stock Opname, 9.6 Backup/Restore.
- [ ] **T3.14** — **Kamus Kode Error** (Bab 10): Verifikasi semua kategori kode error ada: ERR-AUTH-xxx, ERR-SESSION-xxx, ERR-DB-xxx, ERR-FILE-xxx, ERR-CASH-xxx. Setiap kode error harus memiliki 4 kolom: Kode, Pesan Kesalahan CLI, Pemicu, Modul Terkait.
- [ ] **T3.15** — **Prosedur Respon Insiden** (Bab 10.6): Pastikan sub-bab ini ada dan bukan placeholder. Jika masih placeholder, wajib diisi pada Tahap 5. Verifikasi SOP mencakup minimal: Definisi Insiden, Deteksi, Penahanan, Analisis, Pemulihan, Pembelajaran.
- [ ] **T3.16** — **Analisis Risiko** (Bab 11): Verifikasi matriks risiko memiliki kolom: ID Risiko, Komponen Sistem, Deskripsi Ancaman, Probabilitas (1-5), Dampak (1-5), Skor Risiko (1-25), Rencana Mitigasi. Hitung baris data (bukan header). Catat jumlahnya.
- [ ] **T3.17** — **Pseudocode** (Bab 12): Verifikasi semua fungsi keamanan utama sudah dicontohkan. Buat daftar fungsi yang ada di Bab 12 saat ini.
- [ ] **T3.18** — **Matriks Ketertelusuran** (Bab 13): Verifikasi semua sub-bab ada: 13.1 ke SRS, 13.2 ke ACM, 13.3 ke TSD, 13.4 ke Use Case. Verifikasi setiap sel tabel sudah terisi dan tidak ada sel kosong.
- [ ] **T3.19** — **Persetujuan Dokumen** (Bab 14): Verifikasi tabel sign-off ada dan semua kolomnya terisi: Peran, Nama, Tanda Tangan/Persetujuan, Tanggal.
- [ ] **T3.20** — **Glosarium** (Bab 15): Buat daftar semua istilah teknis yang muncul di badan dokumen (istilah asing, akronim, dll.). Bandingkan dengan daftar di Bab 15. Tambahkan istilah yang kurang.
- [ ] **T3.21** — **Daftar Referensi** (Bab 16): Verifikasi semua referensi yang dikutip di dalam badan dokumen sudah terdaftar di tabel Bab 16. Tabel harus memiliki kolom: No, Nama Berkas, Lokasi Path Relatif, Keterangan Versi.
- [ ] **T3.22** — **Konsistensi Penomoran Bab**: Periksa penomoran bab dari Bab 1 hingga Bab 16. Catat jika ada lompatan nomor, duplikasi, atau sub-bab yang tidak berurutan.
- [ ] **T3.23** — **Verifikasi Klaim Bab 1.2**: Klaim Bab 1.2 menyebutkan "6 diagram Mermaid". Bandingkan hasil hitung dari T3.13. Jika tidak tepat 6, perbaiki kalimat klaim di Bab 1.2 sesuai jumlah aktual.

---

### TAHAP 4 — Validasi Kualitas sebagai Referensi Fase SDLC Berikutnya

**Tujuan**: Memastikan dokumen ini dapat dijadikan input yang cukup bagi implementor Fase 04 (Implementation) dan Fase 05 (Testing) tanpa perlu pertanyaan klarifikasi tambahan.

- [ ] **T4.1** — Untuk setiap **pseudocode di Bab 12**, periksa apakah sudah mencantumkan: (a) nama fungsi yang eksak, (b) parameter input dengan tipe data Python, (c) nilai return dan tipe returnnya, (d) penanganan error/exception, dan (e) referensi ke tabel database atau modul Python eksternal yang digunakan. Jika ada pseudocode yang tidak memenuhi semua syarat, tandai.
- [ ] **T4.2** — Untuk setiap **kode error di Bab 10**, pastikan sudah ada: (a) kode string eksak (misal: `ERR-AUTH-001`), (b) pesan string lengkap yang harus ditampilkan di CLI, (c) kondisi pemicu yang spesifik dan tidak ambigu, dan (d) modul terkait (M.1 s.d M.10). Jika ada kode error yang kolomnya tidak lengkap, lengkapi.
- [ ] **T4.3** — Periksa apakah **Bab 12 (Pseudocode)** sudah mencakup keenam fungsi keamanan inti berikut. Jika ada yang belum ada, tambahkan pseudocode-nya:
  - [ ] **T4.3.a** — Fungsi `login_user(username: str, password: str, db_conn) -> dict | None` — mencakup bcrypt `checkpw`, update `failed_login_attempts`, JWT issuance, INSERT `audit_logs LOGIN_SUCCESS`.
  - [ ] **T4.3.b** — Fungsi `require_permission(menu_id: str, session_state: dict, action_func: callable) -> callable` — decorator/guard RBAC yang memeriksa `session_state['role']` terhadap matriks akses, INSERT `audit_logs ACCESS_DENIED` jika ditolak.
  - [ ] **T4.3.c** — Fungsi `write_audit_log(pengguna_id: int, action_type: str, target_table: str, old_value: dict, new_value: dict, cabang_id: int, db_conn) -> None` — INSERT ke tabel `audit_logs` menggunakan parameterized query.
  - [ ] **T4.3.d** — Fungsi `encrypt_wa(nomor_wa: str, fernet_key: bytes) -> str` dan `decrypt_wa(ciphertext: str, fernet_key: bytes) -> str` menggunakan `cryptography.fernet.Fernet`.
  - [ ] **T4.3.e** — Fungsi `run_backup(db_config: dict, backup_dir: str, zip_password: str) -> bool` — eksekusi `mysqldump` via `subprocess.run`, kompres ke ZIP AES-256, INSERT ke `backup_logs`.
  - [ ] **T4.3.f** — Fungsi `validate_env_config(required_keys: list) -> bool` — memeriksa keberadaan berkas `.env` dan semua variabel wajib. Jika gagal, cetak `ERR-FILE-001` dan batalkan startup.
- [ ] **T4.4** — Untuk setiap **diagram Mermaid di Bab 9**, verifikasi bahwa semua actor sudah didefinisikan di baris `actor` atau `participant` dan tidak ada langkah yang ambigu (setiap panah punya label aksi yang jelas).
- [ ] **T4.5** — Periksa apakah **Bab 3.4 (Database Security)** sudah menyebutkan: (a) nama akun database operasional yang spesifik (`abucom_app`), (b) daftar hak privilege yang **diizinkan** secara eksplisit (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), dan (c) daftar hak yang **dilarang** (`DROP`, `ALTER`, `CREATE`, `GRANT`). Jika salah satu belum ada, tambahkan.
- [ ] **T4.6** — Cari seluruh dokumen untuk nilai-nilai yang **masih bersifat generik atau placeholder** seperti "nilai X", "sesuai kebutuhan", atau "disesuaikan". Ganti semua nilai yang seharusnya sudah diketahui berdasarkan referensi yang ada dengan nilai konkret.
- [ ] **T4.7** — Periksa apakah **Bab 6.1 (Enkripsi Data at Rest)** sudah menyebutkan nama variabel `.env` yang spesifik untuk: (a) kunci enkripsi Fernet CRM (`FERNET_KEY` atau nama yang digunakan di TSD), dan (b) sandi enkripsi ZIP backup AES-256 (`BACKUP_ZIP_PASSWORD` atau nama yang digunakan di TSD). Tambahkan jika belum ada.
- [ ] **T4.8** — Periksa apakah **Bab 8.3 (Pengelolaan Akun)** sudah mencantumkan mekanisme teknis penonaktifan akun: nama kolom atau field yang diubah (misal: `is_active = FALSE`), cara pencabutan token JWT yang sedang aktif, dan apakah DDL tabel `pengguna` di REF-05 mendukung mekanisme ini. Sesuaikan dengan DDL yang ada.

---

### TAHAP 5 — Pengisian Data Kosong dan Placeholder

**Tujuan**: Mengisi semua bagian dokumen yang masih kosong, bertanda placeholder, atau bertanda `[DATA BELUM TERSEDIA]`.

- [ ] **T5.1** — Lakukan pencarian teks di seluruh dokumen target untuk string-string berikut (satu per satu): `[DATA BELUM TERSEDIA]`, `[PERLU DIISI]`, `[TODO]`, `TBD`. Buat daftar semua temuan beserta nama bab dan nomor baris-nya.
- [ ] **T5.2** — Isi **Bab 10.6 (Prosedur Respon Insiden Keamanan)** yang saat ini masih memiliki placeholder. Tulis SOP Respon Insiden yang lengkap dan sesuai dengan konteks AbuCom (toko percetakan UMKM, LAN offline lokal, tanpa koneksi internet). SOP **wajib** mencakup seluruh elemen berikut:
  - [ ] **T5.2.a** — **Definisi Insiden Keamanan** dalam konteks AbuCom: daftar peristiwa yang dikategorikan sebagai "insiden keamanan" (minimal 5 jenis insiden spesifik seperti: brute-force berhasil, selisih kas berulang > 3 shift, akses fisik tidak sah ke server, kegagalan backup, ketidakcocokan checksum file backup).
  - [ ] **T5.2.b** — **Fase Deteksi** (*Detection*): daftar indikator-indikator spesifik yang menandakan terjadinya insiden. Setiap indikator harus mencantumkan: (a) sinyal awal yang terlihat, (b) sumber data deteksi (tabel `audit_logs`, dashboard, laporan harian), (c) query SQL contoh untuk mengambil data insiden dari `audit_logs`. Minimal 5 indikator.
  - [ ] **T5.2.c** — **Fase Penahanan** (*Containment*): urutan langkah teknis yang harus dilakukan segera setelah insiden terdeteksi. Setiap langkah harus spesifik dan actionable (misalnya: "Cabut kabel UTP Cat6 dari port switch hub server Debian", "Jalankan menu `MENU-M7-001` untuk menonaktifkan akun yang dicurigai", "Matikan daemon mysqld di server Debian dengan perintah `sudo systemctl stop mysql`").
  - [ ] **T5.2.d** — **Fase Analisis** (*Investigation*): cara membaca dan menginterpretasikan data `audit_logs` untuk forensik internal. Sertakan minimal 3 query SQL contoh (parameterized) untuk mengambil: (a) semua log ACCESS_DENIED dalam 24 jam terakhir, (b) semua aksi pada tabel sensitif oleh pengguna tertentu, (c) riwayat login gagal berturut-turut.
  - [ ] **T5.2.e** — **Fase Pemulihan** (*Recovery*): urutan langkah eksak restore dari backup AES-256 menggunakan menu CLI yang tersedia (`MENU-M2-010` Restore), termasuk verifikasi integritas data setelah restore (cek rowcount tabel kritis, validasi format JSON `audit_logs`).
  - [ ] **T5.2.f** — **Fase Pembelajaran** (*Lessons Learned*): langkah dokumentasi temuan dan perbaikan kontrol keamanan setelah insiden ditangani.
  - [ ] **T5.2.g** — **Tabel Ringkasan Insiden**: buat tabel dengan kolom: Jenis Insiden | Tanda Awal | Langkah Pertama | Penanggung Jawab. Isi minimal 5 baris.
- [ ] **T5.3** — Setelah mengisi semua placeholder, ulangi pencarian untuk memastikan tidak ada lagi teks placeholder yang tersisa di seluruh dokumen. Konfirmasi hasil pencarian mengembalikan 0 hasil.

---

### TAHAP 6 — Validasi Bahasa Indonesia

**Tujuan**: Memastikan dokumen menggunakan bahasa Indonesia yang natural, baku, tidak ambigu, dan mudah dipahami oleh junior programmer atau model AI yang lebih kecil.

- [ ] **T6.1** — Baca ulang seluruh dokumen target dari baris pertama hingga terakhir. Fokus pada kalimat-kalimat deskriptif (bukan tabel, kode, atau blok Mermaid). Tandai setiap kalimat yang: (a) terlalu panjang dan kompleks (lebih dari 3 klausa dalam satu kalimat tanpa tanda baca pemisah yang jelas), (b) menggunakan istilah ambigu yang bisa disalahartikan, (c) menggunakan bentuk pasif yang tidak jelas subjeknya, atau (d) menggunakan logika kondisional yang tidak eksplisit. Catat minimal 5 kalimat bermasalah jika ada.
- [ ] **T6.2** — Periksa konsistensi penulisan istilah teknis di seluruh dokumen. Pilih satu bentuk dan ganti seluruh kemunculannya secara konsisten:
  - [ ] **T6.2.a** — `autentikasi` vs `otentikasi`: pilih **`otentikasi`** (sesuai mayoritas penggunaan di dokumen). Ganti semua kemunculan `autentikasi` menjadi `otentikasi`.
  - [ ] **T6.2.b** — `autorisasi` vs `otorisasi`: gunakan **`otorisasi`** secara konsisten di seluruh dokumen.
  - [ ] **T6.2.c** — Periksa konsistensi penulisan nama peran: gunakan format `code` (backtick) untuk semua nama peran seperti `pemilik`, `kasir`, `kepala_percetakan` di seluruh dokumen.
- [ ] **T6.3** — Periksa apakah setiap **istilah teknis berbahasa Inggris** yang digunakan dalam teks narasi sudah ditulis dalam huruf miring (*italic*). Contoh: *brute-force*, *stateless*, *middleware*, *blueprint*, *at rest*, *in transit*, *payload*. Tambahkan tanda miring pada istilah yang belum.
- [ ] **T6.4** — Perbaiki semua temuan dari T6.1, T6.2, dan T6.3. Catat setiap perbaikan di Bagian 7 (Catatan Temuan).

---

### TAHAP 7 — Validasi Kualitas Akhir (Final Quality Gate)

**Tujuan**: Memastikan dokumen sudah berada pada kualitas yang tidak akan menghambat fase SDLC selanjutnya.

- [ ] **T7.1** — Lakukan simulasi "pembaca baru": bacalah dokumen seolah-olah Anda adalah junior programmer yang baru bergabung. Buat daftar pertanyaan yang mungkin muncul (minimal 5 pertanyaan potensial). Verifikasi setiap pertanyaan sudah terjawab secara eksplisit di dalam dokumen. Jika ada yang belum terjawab, tambahkan penjelasan di bab yang relevan.
- [ ] **T7.2** — Verifikasi **referensi silang antar bab** di dalam dokumen target. Pilih minimal 10 referensi silang yang ada (contoh: "lihat ACM Bab 6.1", "Bab 9.3", "ERR-AUTH-003") dan verifikasi satu per satu bahwa target referensi tersebut ada dan kontennya sesuai dengan yang diklaim.
- [ ] **T7.3** — Verifikasi **formula matematis shift handover** di Bab 8.1. Pastikan formula `Kas Sistem = Kas Awal + Σ(Transaksi Tunai) - Σ(Pengeluaran Tunai)` konsisten dengan alur diagram di Bab 9.4 (setiap variabel dalam formula terwakili oleh langkah di diagram).
- [ ] **T7.4** — Cari semua kemunculan nilai numerik berikut di seluruh dokumen dan pastikan nilainya sama persis di setiap kemunculan (tidak boleh ada yang berbeda):
  - [ ] Durasi sesi JWT: harus konsisten sebagai **8 jam / 28.800 detik** di semua bab.
  - [ ] Threshold brute-force: harus konsisten sebagai **5 kali gagal** di semua bab.
  - [ ] Durasi suspensi: harus konsisten sebagai **10 menit** di semua bab.
  - [ ] Toleransi selisih kas shift: harus konsisten sebagai **Rp 10.000** di semua bab.
  - [ ] Cost factor bcrypt: harus konsisten sebagai **12** di semua bab.
- [ ] **T7.5** — Hitung jumlah baris data di **tabel matriks risiko Bab 11.1** (tidak termasuk baris header). Klaim Bab 1.2 menyebutkan "10 analisis risiko utama". Jika jumlah baris kurang dari 10, tambahkan risiko-risiko keamanan yang relevan hingga berjumlah tepat 10. Risiko tambahan harus bersumber dari konteks AbuCom (ancaman UMKM offline) dan memiliki nilai probabilitas, dampak, dan skor yang masuk akal.
- [ ] **T7.6** — Verifikasi **Bab 16 (Referensi Dokumen)** sudah memuat semua 8 file referensi yang digunakan dalam proses validasi ini. Pastikan path relatif setiap file sudah benar dan file-nya benar-benar ada di filesystem. Jika selama validasi ditemukan referensi baru yang digunakan, tambahkan di baris paling bawah tabel.

---

### TAHAP 8 — Penulisan Ulang dan Overwrite Dokumen Target

**Tujuan**: Menerapkan seluruh hasil perbaikan ke dalam file target dengan cara menimpa (overwrite) secara penuh.

> ⚠️ **PERINGATAN KRITIS — BACA SEBELUM MENGEKSEKUSI**:
> Tahap ini adalah tahap destruktif. Pastikan seluruh Tahap 0 hingga 7 sudah selesai 100% dan semua perbaikan sudah diintegrasikan ke dalam satu draf dokumen lengkap di memori kerja sebelum menjalankan overwrite.
> Kesalahan pada tahap ini dapat mengakibatkan hilangnya konten dokumen. Tidak ada undo setelah overwrite dilakukan.

- [ ] **T8.1** — Susun seluruh konten dokumen yang telah divalidasi dan diperbaiki menjadi satu blok teks lengkap di memori kerja. Pastikan semua hasil perbaikan dari Tahap 1 hingga 7 sudah terintegrasi ke dalam blok teks ini. Dokumen harus memuat semua bab dari Bab 1 s.d Bab 16 secara lengkap.
- [ ] **T8.2** — **Perbarui versi dokumen**: Ubah nilai `versi` di frontmatter dari `1.0` menjadi `1.1`.
- [ ] **T8.3** — **Perbarui tanggal dokumen**: Ubah nilai `tanggal` di frontmatter menjadi tanggal saat issue ini dieksekusi (format: `YYYY-MM-DD`).
- [ ] **T8.4** — **Tambahkan entri di tabel Riwayat Perubahan**: Tambahkan baris baru di tabel changelog (tepat di bawah baris versi `1.0`) dengan format kolom yang sama:
  ```
  | **1.1** | [TANGGAL_EKSEKUSI] | Validasi menyeluruh v1.1: komparasi mendalam terhadap 8 dokumen referensi (ACM, SysArch, SRS, TSD, DDL, ERD, BRD, Workflow), pengisian SOP Respon Insiden Bab 10.6, verifikasi konsistensi kode error, sinkronisasi DDL tabel database, perbaikan bahasa Indonesia, validasi konsistensi nilai numerik, dan pembaruan referensi. | Senior Security Architect & Cybersecurity Compliance Specialist |
  ```
- [ ] **T8.5** — Lakukan pengecekan akhir sebelum overwrite: konfirmasi bahwa draf dokumen di memori kerja sudah memuat seluruh bab dari Bab 1 hingga Bab 16 tanpa ada yang dipotong atau diringkas. Konfirmasi tidak ada bab yang hilang.
- [ ] **T8.6** — Tulis ulang seluruh konten dokumen yang sudah divalidasi ke file `docs/sdlc/03_design/06_security_design.md` dengan cara **overwrite penuh** (*full overwrite*). Aturan wajib:
  - Penulisan dilakukan dari **baris pertama hingga baris terakhir** tanpa pemotongan (*no truncation*).
  - **Seluruh teks harus ditulis ulang sepenuhnya**. Dilarang menggunakan komentar singkat seperti `... (isi tetap sama) ...` atau `[konten sebelumnya]` sebagai pengganti konten yang sebenarnya.
  - Jika alat tulis memiliki batasan panjang output, bagi penulisan menjadi beberapa segmen berurutan (Bab 1-5, Bab 6-10, Bab 11-16), namun **pastikan setiap segmen disambung tepat** tanpa ada baris yang hilang di antara segmen.
- [ ] **T8.7** — Setelah overwrite selesai, baca kembali file `docs/sdlc/03_design/06_security_design.md` dari baris pertama hingga baris terakhir untuk memverifikasi bahwa:
  - [ ] Versi di frontmatter sudah berubah menjadi `1.1`.
  - [ ] Tabel riwayat perubahan sudah memuat entri baru versi `1.1`.
  - [ ] Bab 10.6 sudah terisi lengkap dengan SOP Respon Insiden (tidak ada placeholder).
  - [ ] Semua perbaikan dari Tahap 1–7 sudah tercermin di dalam file.
  - [ ] Semua bab dari Bab 1 hingga Bab 16 hadir dan lengkap.
  - [ ] Jumlah baris total file tidak lebih sedikit dari versi sebelumnya (kecuali ada penghapusan yang disengaja dan terdokumentasi).

---

### TAHAP 9 — Pembaruan Referensi (Jika Ada Referensi Baru)

- [ ] **T9.1** — Jika selama proses validasi ditemukan file referensi **baru** yang relevan dan digunakan sebagai sumber data perbaikan (di luar 8 file yang sudah terdaftar di Bagian 3), tambahkan file tersebut ke dalam **tabel Bab 16 (Referensi Dokumen)** di dokumen target, pada baris paling bawah. Format tambahan: `| [No Urut] | [nama_file] | [path_relatif_dari_root_proyek] | [Keterangan Versi dan Relevansi] |`.
- [ ] **T9.2** — Sebelum menambahkan referensi baru, verifikasi bahwa file yang dimaksud benar-benar ada di filesystem dengan melakukan pembacaan file tersebut. Jangan menambahkan referensi yang tidak dapat dikonfirmasi keberadaannya.

---

## 5. Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **SELESAI** jika dan hanya jika seluruh kondisi berikut terpenuhi:

- [ ] Seluruh checklist dari Tahap 0 hingga Tahap 9 sudah bertanda `[x]`.
- [ ] File `docs/sdlc/03_design/06_security_design.md` sudah berversi `1.1` dengan tanggal diperbarui.
- [ ] Tidak ada satu pun teks placeholder (`[DATA BELUM TERSEDIA]`, `[TODO]`, `TBD`) yang tersisa di dokumen.
- [ ] Bab 10.6 (Prosedur Respon Insiden) sudah terisi lengkap dengan konten nyata (bukan placeholder).
- [ ] Semua inkonsistensi data antara dokumen target dan file referensi sudah diselesaikan dan terdokumentasi di Bagian 7.
- [ ] Dokumen dapat dibaca dari awal hingga akhir oleh junior programmer tanpa pertanyaan klarifikasi lebih lanjut.
- [ ] Jumlah diagram Mermaid tepat 6 dan semua dapat di-render dengan benar.
- [ ] Semua kode error di Bab 10 memiliki 4 kolom yang terisi lengkap.

---

## 6. Batasan dan Larangan Keras

> Pelaksana **DILARANG** melakukan hal-hal berikut selama mengeksekusi issue ini:

- ❌ **Dilarang** mengubah konten teknis (nilai parameter, nama tabel, logika alur keamanan) yang sudah **terbukti sinkron** dengan file referensi tanpa alasan teknis yang jelas dan terdokumentasi.
- ❌ **Dilarang** menghapus bab atau sub-bab yang sudah ada — tandai sebagai temuan di Bagian 7 dan diskusikan saja, jangan hapus.
- ❌ **Dilarang** memodifikasi file referensi ([REF-01] hingga [REF-08]) dalam bentuk apapun.
- ❌ **Dilarang** menulis ulang dokumen secara parsial (sebagian bab saja). Overwrite harus dilakukan untuk **seluruh dokumen** sekaligus dalam satu operasi tulis.
- ❌ **Dilarang** memotong, meringkas, atau menghilangkan konten yang sudah ada saat melakukan overwrite. Setiap kalimat dari versi sebelumnya harus hadir di versi baru, kecuali perubahan yang memang secara eksplisit diidentifikasi dalam proses validasi.
- ❌ **Dilarang** menambahkan konten yang tidak bersumber dari file referensi yang terdaftar atau dari domain pengetahuan keamanan sistem yang sudah terbukti. Dilarang mengarang data teknis.
- ❌ **Dilarang** melanjutkan ke tahap berikutnya sebelum tahap saat ini selesai 100%.

---

## 7. Catatan Temuan (Diisi oleh Pelaksana saat Eksekusi)

*Bagian ini diisi oleh pelaksana issue saat mengeksekusi. Catat setiap temuan inkonsistensi, gap, atau perbaikan yang dilakukan.*

| No | Tahap | Kode Tugas | Temuan | Tindakan yang Diambil | Status |
|---|---|---|---|---|---|
| 1 | - | - | *(diisi saat eksekusi)* | - | - |

---