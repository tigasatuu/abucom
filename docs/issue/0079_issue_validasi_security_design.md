---
judul      : Validasi & Penyempurnaan Dokumen Security Design
target_file: docs/sdlc/03_design/06_security_design.md
referensi  : docs/sdlc/
prioritas  : Tinggi
status     : Open
dibuat_oleh: Senior Security Architect & Cybersecurity Compliance Specialist
tanggal    : 2026-05-29
---

# Validasi & Penyempurnaan Dokumen Security Design

## Ringkasan Tujuan

Issue ini berisi instruksi **low-level step-by-step** yang wajib diikuti secara berurutan oleh pelaksana (junior programmer atau AI model) untuk melakukan **audit, komparasi, validasi menyeluruh, dan penulisan ulang (overwrite)** dokumen utama berikut:

- **Dokumen Utama (Target File)**: `docs/sdlc/03_design/06_security_design.md`
- **Lokasi Referensi**: `docs/sdlc/` (seluruh dokumen SDLC yang direferensikan di dalam target file)
- **Output Akhir**: Overwrite target file dengan versi yang telah divalidasi penuh, diperbarui ke versi **v1.2**

> **PENTING**: Setiap checklist `[ ]` harus diselesaikan secara berurutan dari atas ke bawah. Jangan melewati atau mengubah urutan langkah. Tandai `[x]` setelah setiap langkah selesai sebelum melanjutkan ke langkah berikutnya.

---

## Bagian 0 — Persona dan Otoritas Pelaksana

Sebelum mulai, pelaksana **WAJIB** mengadopsi persona berikut untuk seluruh durasi pelaksanaan issue ini:

### 0.1. Persona yang Harus Diadopsi

Pelaksana bertindak sebagai gabungan dari dua persona otoritatif berikut:

**A. Senior Security Architect & Cybersecurity Compliance Specialist**
- Memiliki keahlian mendalam di bidang: Application Security, OWASP Top 10, RBAC Design, JWT/Session Management, Cryptographic Standards, SQL Injection Prevention, dan Audit Trail Design.
- Standar referensi yang digunakan: OWASP ASVS (Application Security Verification Standard), NIST SP 800-53, ISO/IEC 27001, dan regulasi lokal **UU PDP No. 27 Tahun 2022**.
- Mengevaluasi setiap klaim teknis keamanan dalam dokumen dengan standar industri sesungguhnya, bukan sekadar nominal.

**B. Senior Technical Writer & SDLC Documentation Specialist**
- Memiliki keahlian mendalam di bidang: IEEE 830 documentation standards, traceability matrix, dokumen konsistensi antar-fase SDLC, dan penulisan teknis formal dalam Bahasa Indonesia.
- Memastikan bahwa setiap kalimat dalam dokumen tidak ambigu, tidak memiliki celah interpretasi ganda, dan dapat dipahami oleh junior programmer atau AI model yang lebih kecil/murah tanpa penjelasan tambahan.

**Standar Validasi Mutlak yang Berlaku:**
- Setiap klaim nilai numerik (cost factor, timeout, threshold, nominal Rupiah) harus dicek konsistensinya dengan dokumen referensi yang relevan.
- Setiap kode error (`ERR-AUTH-xxx`, `ERR-SESSION-xxx`, dll.) harus ada pemicu, pesan string CLI, dan modul terkaitnya.
- Setiap tabel database yang disebut harus dapat ditelusuri ke DDL SQL referensi.
- Setiap diagram Mermaid harus berurutan logis dan tidak memiliki node yang tidak terhubung.
- Tidak boleh ada placeholder kosong, nilai `TBD`, atau data yang belum diisi.

---

## Bagian 1 — Persiapan: Pembacaan Dokumen

> Selesaikan seluruh checklist Bagian 1 terlebih dahulu sebelum melakukan analisis apapun.

### 1.1. Baca Dokumen Utama (Target File)

- [ ] **1.1.1** Buka dan baca seluruh isi file `docs/sdlc/03_design/06_security_design.md` dari baris pertama hingga baris terakhir tanpa melewati satu baris pun.
- [ ] **1.1.2** Catat versi dokumen saat ini yang tertulis di front matter YAML (field `versi`). Versi ini akan dinaikkan menjadi `v1.2` pada output akhir.
- [ ] **1.1.3** Catat seluruh judul Bab (H2) dan Sub-bab (H3, H4) yang ada dalam dokumen. Ini akan menjadi acuan verifikasi kelengkapan struktur di Bagian 3.
- [ ] **1.1.4** Identifikasi dan catat semua nama file referensi yang disebutkan di Bab 16 (Referensi Dokumen) dokumen utama. Daftar file referensi yang harus dibaca adalah:
  - `docs/sdlc/02_analysis/06_access_control_matrix.md`
  - `docs/sdlc/03_design/03_system_architecture.md`
  - `docs/sdlc/02_analysis/02_software_requirements.md`
  - `docs/sdlc/01_planning/04_tech_stack_decision.md`
  - `docs/sdlc/03_design/01_database_schema.sql`
  - `docs/sdlc/03_design/02_erd_database.md`
  - `docs/sdlc/02_analysis/01_business_requirements.md`
  - `docs/sdlc/02_analysis/04_workflow_diagram.md`

### 1.2. Baca Seluruh Dokumen Referensi

Baca setiap file referensi berikut **secara utuh** sebelum melanjutkan ke Bagian 2. Tujuan pembacaan adalah memahami konten asli referensi agar dapat digunakan sebagai dasar komparasi:

- [ ] **1.2.1** Buka dan baca seluruh isi `docs/sdlc/02_analysis/06_access_control_matrix.md`. Fokus pada: definisi 8 peran, matriks hak akses menu, aturan eskalasi pemilik, rate limiting, konfigurasi JWT session.
- [ ] **1.2.2** Buka dan baca seluruh isi `docs/sdlc/03_design/03_system_architecture.md`. Fokus pada: topologi LAN offline, konfigurasi OS Debian/Windows, bind-address MySQL, database isolation level, backup/restore.
- [ ] **1.2.3** Buka dan baca seluruh isi `docs/sdlc/02_analysis/02_software_requirements.md`. Fokus pada: spesifikasi fungsional M.7 (Keamanan), daftar kode error keamanan, kebutuhan non-fungsional (performa, keamanan, privasi).
- [ ] **1.2.4** Buka dan baca seluruh isi `docs/sdlc/01_planning/04_tech_stack_decision.md`. Fokus pada: parameter bcrypt (cost factor), library JWT, parameterized query, sanitasi input, file `.env`, `requirements.txt`.
- [ ] **1.2.5** Buka dan baca seluruh isi `docs/sdlc/03_design/01_database_schema.sql`. Fokus pada: definisi kolom tabel `pengguna`, `audit_logs`, `backup_logs`, `shift_handover`, `system_configs`, `pelanggan`; constraint CHECK; foreign key.
- [ ] **1.2.6** Buka dan baca seluruh isi `docs/sdlc/03_design/02_erd_database.md`. Fokus pada: relasi foreign key tabel yang terkait keamanan (pengguna, audit_logs, shift_handover).
- [ ] **1.2.7** Buka dan baca seluruh isi `docs/sdlc/02_analysis/01_business_requirements.md`. Fokus pada: kebutuhan bisnis keamanan (BR-F-30 s.d BR-F-34 atau nomor setaranya), privasi data pelanggan.
- [ ] **1.2.8** Buka dan baca seluruh isi `docs/sdlc/02_analysis/04_workflow_diagram.md`. Fokus pada: alur otorisasi kasir, alur serah terima shift, alur eskalasi pemilik.
- [ ] **1.2.9** Periksa apakah ada dokumen SDLC lain dalam direktori `docs/sdlc/` yang **belum** terdaftar di Bab 16 tetapi secara konten memiliki keterkaitan dengan topik keamanan (misalnya: `04_cli_interaction_flow.md` di folder `03_design/`). Catat temuan ini untuk divalidasi di Bagian 6.

---

## Bagian 2 — Komparasi Mendalam: Target File vs. Referensi

> Lakukan komparasi satu per satu antara konten dokumen utama dengan setiap file referensi. Catat semua temuan (data yang hilang, tidak konsisten, atau berlebihan) menggunakan catatan sementara sebelum menuliskannya ke dokumen.

### 2.1. Komparasi dengan Access Control Matrix (ACM)

- [ ] **2.1.1** Verifikasi bahwa **8 peran** yang didefinisikan di Bab 5.1 dokumen utama (`pemilik`, `kepala_percetakan`, `pramuniaga`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang`) **identik 100%** dengan daftar peran di ACM. Jika ada perbedaan nama, tambahkan/koreksi.
- [ ] **2.1.2** Verifikasi bahwa **hierarki 3-level RBAC** di diagram Mermaid Bab 5.1 konsisten dengan hierarki yang didefinisikan ACM. Periksa semua edge (panah) antar node.
- [ ] **2.1.3** Verifikasi bahwa **matriks akses modul** di Bab 5.3 (10 modul M.1 s.d M.10) menggunakan simbol yang identik dengan matriks di ACM untuk setiap kombinasi Modul × Peran. Jika ada sel yang berbeda, koreksi mengikuti ACM sebagai sumber kebenaran.
- [ ] **2.1.4** Verifikasi bahwa **4 operasi kritis eskalasi pemilik** di Bab 5.4 konsisten dengan daftar operasi eskalasi di ACM Bab 6.1. Periksa apakah ada operasi yang ada di ACM tetapi tidak ada di dokumen utama.
- [ ] **2.1.5** Verifikasi bahwa **3 aturan otorisasi kepala percetakan** di Bab 5.5 konsisten dengan ACM Bab 6.2. Periksa nilai toleransi selisih kas (Rp 10.000) dan status `'DRAFT'` → `'APPROVED'`.
- [ ] **2.1.6** Verifikasi bahwa **parameter rate limiting** di Bab 4.3 (5 kali gagal, 10 menit suspensi) konsisten dengan ACM Bab 6.5.
- [ ] **2.1.7** Verifikasi bahwa **format kode error** kegagalan otorisasi (`ERR-AUTH-003`, `ERR-AUTH-011`, `ERR-CASH-001`, dll.) yang disebutkan dalam dokumen utama konsisten dengan daftar kode error yang ada di ACM.

### 2.2. Komparasi dengan System Architecture

- [ ] **2.2.1** Verifikasi bahwa **topologi jaringan LAN offline** di Bab 3.2 (IP server `192.168.1.200`, subnet `192.168.1.0/24`, router MikroTik) konsisten dengan arsitektur jaringan di System Architecture.
- [ ] **2.2.2** Verifikasi bahwa **konfigurasi firewall ufw** di Bab 3.2 dan 12.4 (`ufw allow from 192.168.1.0/24 to any port 3306 proto tcp`) konsisten dengan perintah firewall yang tertera di System Architecture.
- [ ] **2.2.3** Verifikasi bahwa **konfigurasi MySQL bind-address** di Bab 3.3 (`bind-address = 192.168.1.200`) konsisten dengan konfigurasi OS server di System Architecture.
- [ ] **2.2.4** Verifikasi bahwa **MySQL isolation level Repeatable Read** di Bab 3.4 konsisten dengan konfigurasi database di System Architecture.
- [ ] **2.2.5** Verifikasi bahwa **prosedur backup** (format ZIP AES-256, folder `/var/lib/mysql-backups/`, `chmod 700`) di Bab 8.2 dan 12.4 konsisten dengan spesifikasi backup di System Architecture.
- [ ] **2.2.6** Periksa apakah ada elemen arsitektur keamanan dari System Architecture (mis. konfigurasi SSH, UPS, pengaturan akun Windows) yang **belum tercakup** di dokumen utama tetapi relevan untuk Security Design. Tambahkan jika ditemukan.

### 2.3. Komparasi dengan Software Requirements Specification (SRS)

- [ ] **2.3.1** Verifikasi bahwa **seluruh kode error keamanan** yang didaftarkan di Bab 10 dokumen utama (`ERR-AUTH-xxx`, `ERR-SESSION-xxx`, `ERR-DB-xxx`, `ERR-FILE-xxx`, `ERR-CASH-xxx`) konsisten dengan katalog kode error di SRS. Periksa apakah ada kode error di SRS yang **belum masuk** ke dokumen utama.
- [ ] **2.3.2** Verifikasi bahwa **spesifikasi fungsional Modul M.7 (Keamanan)** di SRS telah sepenuhnya tercakup dalam dokumen utama. Identifikasi fitur keamanan yang mungkin ada di SRS M.7 tetapi tidak ada penjelasannya di dokumen utama.
- [ ] **2.3.3** Verifikasi bahwa **kebutuhan non-fungsional keamanan** di SRS (mis. performa autentikasi, waktu respons, ketersediaan sistem) telah direferensikan atau dijelaskan dalam dokumen utama.
- [ ] **2.3.4** Verifikasi bahwa **daftar pustaka Python** yang relevan keamanan (mis. `bcrypt`, `PyJWT`, `cryptography`, `mysql-connector-python`) yang disebutkan dalam dokumen utama sesuai dengan `requirements.txt` yang ada di SRS atau Tech Stack Decision.
- [ ] **2.3.5** Periksa apakah **matriks ketertelusuran Bab 13.1** (Security Design ke SRS) menyertakan semua kebutuhan keamanan kritis yang ada di SRS. Tambahkan baris mapping yang hilang jika ada.

### 2.4. Komparasi dengan Tech Stack Decision (TSD)

- [ ] **2.4.1** Verifikasi bahwa **bcrypt cost factor 12** di Bab 4.1 dan pseudocode Bab 12.2 konsisten dengan keputusan teknis di TSD.
- [ ] **2.4.2** Verifikasi bahwa **algoritma JWT HS256** dan **masa berlaku 8 jam (28.800 detik)** di Bab 4.2 konsisten dengan keputusan teknis di TSD.
- [ ] **2.4.3** Verifikasi bahwa **penggunaan `%s` parameterized query** dan larangan f-string SQL di Bab 3.4 dan 6.4 konsisten dengan standar coding di TSD.
- [ ] **2.4.4** Verifikasi bahwa **parameter konfigurasi `.env`** di Bab 12.3 (DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, JWT_SECRET_KEY, FERNET_KEY, BACKUP_ZIP_PASSWORD) konsisten dengan parameter yang didefinisikan di TSD.
- [ ] **2.4.5** Verifikasi bahwa **modul Python keamanan** (`middleware/rbac.py`, `middleware/logger.py`, `utils/backup.py`, `utils/crypto.py`) di Bab 12.1 konsisten dengan struktur direktori yang didefinisikan di TSD.
- [ ] **2.4.6** Verifikasi bahwa **matriks ketertelusuran Bab 13.3** (Security Design ke TSD) menyertakan semua keputusan teknis keamanan dari TSD. Tambahkan baris yang hilang jika ada.

### 2.5. Komparasi dengan Database Schema SQL (DDL)

- [ ] **2.5.1** Verifikasi bahwa **definisi DDL tabel `audit_logs`** di Bab 7.1 dokumen utama identik dengan definisi DDL yang ada di `01_database_schema.sql`. Periksa setiap nama kolom, tipe data, constraint (NOT NULL, DEFAULT, COMMENT), dan foreign key.
- [ ] **2.5.2** Verifikasi bahwa **kolom-kolom keamanan tabel `pengguna`** yang disebutkan di dokumen utama (`password_hash`, `failed_login_attempts`, `locked_until`, `role`, `cabang_id`) ada dan tipenya sesuai dengan DDL.
- [ ] **2.5.3** Verifikasi bahwa **kolom `whatsapp`** di tabel `pelanggan` ada di DDL dan tipenya mendukung penyimpanan ciphertext Fernet (VARCHAR panjang cukup, bukan INT atau tipe kecil).
- [ ] **2.5.4** Verifikasi bahwa **tabel `backup_logs`** yang dirujuk di pseudocode Bab 12.2 (kolom: `nama_file`, `status_backup`, `pengguna_id`, `ukuran_file_kb`, `cabang_id`) ada dan kolom-kolomnya sesuai dengan DDL.
- [ ] **2.5.5** Verifikasi bahwa **tabel `shift_handover`** yang dirujuk di Bab 8.1 dan diagram Mermaid Bab 9.4 (kolom: `kas_fisik`, `kas_sistem`, `selisih`, `status_handover`, `supervisor_id`, `catatan_alasan`, `kasir_keluar_id`, `timestamp_handover`) ada dan konsisten dengan DDL.
- [ ] **2.5.6** Verifikasi bahwa **5 tabel "Sangat Sensitif"** yang disebutkan di Bab 2.3 (`pinjaman_bank`, `pinjaman_kerabat`, `payroll`, `system_configs`, `backup_logs`) semuanya terdefinisi dalam DDL.
- [ ] **2.5.7** Verifikasi bahwa **7 tabel "Sensitif"** yang disebutkan di Bab 2.3 (`transaksi`, `pengeluaran`, `audit_logs`, `shift_handover`, `utang_supplier`, `limbah_produksi`, `stock_opname`) semuanya ada dalam DDL.
- [ ] **2.5.8** Verifikasi bahwa **total 28 tabel** yang disebutkan di Bab 2.3 sesuai dengan jumlah aktual tabel yang didefinisikan dalam DDL. Jika berbeda, koreksi angkanya.

### 2.6. Komparasi dengan ERD Database

- [ ] **2.6.1** Verifikasi bahwa **foreign key `pengguna_id`** pada tabel `audit_logs` yang disebutkan di Bab 7.1 sesuai dengan relasi yang digambarkan di ERD.
- [ ] **2.6.2** Verifikasi bahwa **foreign key `cabang_id`** pada tabel `audit_logs` dan `shift_handover` sesuai dengan relasi yang digambarkan di ERD.
- [ ] **2.6.3** Periksa apakah ada relasi keamanan kritis lain yang terlihat di ERD tetapi tidak dibahas di dokumen utama. Tambahkan penjelasannya jika relevan.

### 2.7. Komparasi dengan Business Requirements Document (BRD)

- [ ] **2.7.1** Verifikasi bahwa **kebutuhan bisnis keamanan** (perlindungan kas kasir, privasi data pelanggan, integritas stok) yang ada di BRD telah diadresir secara penuh dalam dokumen utama.
- [ ] **2.7.2** Verifikasi bahwa **model ancaman Bab 2.2** (THR-001 s.d THR-008) mencakup semua ancaman bisnis yang diidentifikasi dalam BRD sebagai risiko utama usaha percetakan UMKM.
- [ ] **2.7.3** Verifikasi bahwa **implementasi Hak Penghapusan Data (Right to Erasure)** di Bab 6.3 sesuai dengan kebutuhan bisnis yang ada di BRD terkait kepatuhan UU PDP No. 27/2022.
- [ ] **2.7.4** Periksa apakah **matriks ketertelusuran Bab 13** perlu ditambahkan mapping ke BRD (sekarang hanya ada mapping ke SRS, ACM, TSD, dan Use Case). Tambahkan sub-bab 13.5 jika memang ada kebutuhan bisnis keamanan dari BRD yang belum termapping.

### 2.8. Komparasi dengan Workflow Diagram

- [ ] **2.8.1** Verifikasi bahwa **alur serah terima shift** di Bab 8.1 dan diagram Mermaid Bab 9.4 konsisten dengan alur yang tergambar di Workflow Diagram, termasuk urutan langkah, kondisi percabangan, dan aktor yang terlibat.
- [ ] **2.8.2** Verifikasi bahwa **alur eskalasi otorisasi pemilik** di diagram Mermaid Bab 9.3 konsisten dengan alur yang ada di Workflow Diagram.
- [ ] **2.8.3** Periksa apakah ada **alur keamanan spesifik** lain yang tergambar di Workflow Diagram (mis. alur login, alur stock opname) tetapi belum direpresentasikan dalam salah satu dari 6 diagram Mermaid di Bab 9. Tambahkan diagram baru jika ada alur penting yang hilang.

---

## Bagian 3 — Validasi Kelengkapan Data dan Isi Dokumen

> Validasi setiap sub-bab dokumen utama untuk memastikan tidak ada data yang kosong, placeholder, atau informasi yang tidak lengkap.

### 3.1. Periksa Data Kosong dan Placeholder

- [ ] **3.1.1** Cari seluruh teks dalam dokumen utama yang mengandung string: `TBD`, `TODO`, `PLACEHOLDER`, `[isi di sini]`, `[belum ditentukan]`, `N/A` (yang bukan merupakan nilai valid), atau sel tabel yang benar-benar kosong. Jika ada, isi dengan data yang sesuai dan relevan.
- [ ] **3.1.2** Periksa **tabel Riwayat Perubahan Dokumen** di bagian awal. Pastikan semua kolom (Versi, Tanggal, Perubahan, Oleh) terisi lengkap untuk semua baris.
- [ ] **3.1.3** Periksa **tabel Persetujuan dan Otorisasi** di Bab 14. Pastikan semua kolom (Peran Stakeholder, Nama Terang, Tanda Tangan, Tanggal) terisi dengan data yang konsisten dan tidak hanya berisi teks generik yang tidak informatif.
- [ ] **3.1.4** Periksa apakah **matriks analisis risiko** di Bab 11.1 memiliki nilai numerik yang logis dan konsisten untuk semua 10 risiko (RSK-SEC-001 s.d RSK-SEC-010). Nilai Skor Risiko harus = Probabilitas × Dampak. Verifikasi perhitungan setiap baris.
- [ ] **3.1.5** Periksa apakah **contoh payload JWT** di Bab 4.2 menggunakan nilai `exp` (Unix timestamp) yang logis dan realistis. Jika nilai `1779928800` tidak masuk akal untuk konteks 2026, koreksi dengan nilai yang lebih representatif dan tambahkan komentar penjelasan.
- [ ] **3.1.6** Periksa apakah **contoh konfigurasi .env** di Bab 12.3 menggunakan nilai credential yang benar-benar terlihat seperti contoh/dummy yang aman (tidak menggunakan nilai yang terlalu sederhana atau mudah ditebak). Jika ada, tambahkan komentar `# GANTI DENGAN NILAI ASLI SEBELUM PRODUKSI`.
- [ ] **3.1.7** Periksa apakah **pseudocode di Bab 12.2** menggunakan `secret_key` hardcoded dengan komentar bahwa nilai ini harus diambil dari `.env`. Pastikan ada catatan eksplisit di pseudocode yang menunjukkan cara mengambil nilai dari `.env` menggunakan `os.getenv('JWT_SECRET_KEY')`.

### 3.2. Periksa Konsistensi Nilai Numerik dan Parameter

- [ ] **3.2.1** Audit seluruh dokumen dan buat daftar semua nilai numerik keamanan yang muncul: cost factor bcrypt, durasi JWT session (jam dan detik), threshold brute-force (jumlah percobaan), durasi lockout (menit), nilai toleransi selisih kas (Rupiah), nilai batas pengeluaran untuk eskalasi (Rupiah), durasi retensi log audit (bulan). Verifikasi bahwa setiap nilai muncul dengan nilai yang **sama dan konsisten** di seluruh dokumen.
- [ ] **3.2.2** Verifikasi bahwa pernyataan "28.800 detik (8 jam)" di Bab 4.2 secara matematis benar (28800 / 3600 = 8). Jika salah, koreksi.
- [ ] **3.2.3** Verifikasi bahwa pernyataan JWT_EXPIRATION_SECONDS di Bab 12.3 nilainya sama dengan yang disebutkan di Bab 4.2.
- [ ] **3.2.4** Verifikasi bahwa nilai idle timeout yang disebutkan di Bab 4.4 (30 menit tanpa aktivitas keyboard) tidak bertentangan dengan session timeout JWT (8 jam). Jika ada potensi ambiguitas antara keduanya, tambahkan penjelasan yang memperjelas perbedaan mekanismenya.

### 3.3. Periksa Konsistensi Kode Error

- [ ] **3.3.1** Buat daftar lengkap semua kode error yang **disebutkan/digunakan** dalam teks narasi, diagram Mermaid, matriks eskalasi, dan pseudocode di seluruh dokumen utama.
- [ ] **3.3.2** Buat daftar lengkap semua kode error yang **didefinisikan** di tabel Bab 10 (10.1 s.d 10.5).
- [ ] **3.3.3** Bandingkan dua daftar tersebut. Jika ada kode error yang **digunakan dalam narasi/diagram tetapi tidak didefinisikan** di Bab 10, tambahkan entri definisinya di tabel Bab 10 yang sesuai.
- [ ] **3.3.4** Jika ada kode error yang **didefinisikan di Bab 10 tetapi tidak pernah direferensikan** di mana pun dalam dokumen, evaluasi apakah entri tersebut relevan. Jika relevan, tambahkan referensinya ke bagian yang tepat. Jika tidak relevan, hapus untuk menjaga kebersihan dokumen.

### 3.4. Periksa Diagram Mermaid

- [ ] **3.4.1** Verifikasi bahwa dokumen memiliki **tepat 6 diagram Mermaid** sebagaimana diklaim di Bab 1.2. Hitung jumlah blok ```mermaid``` yang ada. Jika berbeda dari 6, perbaiki klaim di Bab 1.2 atau tambahkan/hapus diagram sesuai kebutuhan.
- [ ] **3.4.2** Verifikasi diagram Mermaid **Bab 3.1** (Defense in Depth): semua node terhubung secara berurutan, tidak ada node terisolasi, label node jelas dan tidak ambigu.
- [ ] **3.4.3** Verifikasi diagram Mermaid **Bab 5.1** (Hierarki RBAC): semua 8 peran tercantum, edge hierarki akurat, tidak ada node duplikat.
- [ ] **3.4.4** Verifikasi diagram Mermaid **Bab 9.1** (Sequence Login): semua langkah autentikasi tercakup (termasuk lockout, reset attempts, JWT generation, audit log), semua branch (alt/else) memiliki label yang jelas.
- [ ] **3.4.5** Verifikasi diagram Mermaid **Bab 9.2** (Sequence Transaksi Kasir): alur dari pemilihan menu hingga pencetakan nota tergambar lengkap, RBAC guard check ada di posisi awal alur.
- [ ] **3.4.6** Verifikasi diagram Mermaid **Bab 9.3** (Sequence Eskalasi Retur): alur eskalasi pemilik tergambar lengkap, percabangan sandi benar/salah ada, ACID transaction wrap ada.
- [ ] **3.4.7** Verifikasi diagram Mermaid **Bab 9.4** (Sequence Shift Handover): semua kondisi (Normal dan Anomali) tergambar, verifikasi sandi kepala percetakan via bcrypt ada.
- [ ] **3.4.8** Verifikasi diagram Mermaid **Bab 9.5** (Flowchart Stock Opname): semua node tersambung, percabangan pemeriksaan sandi supervisor ada, update tabel `barang` dan `audit_logs` ada.
- [ ] **3.4.9** Verifikasi diagram Mermaid **Bab 9.6** (Flowchart Backup/Restore): kedua alur (Backup dan Restore) tergambar terpisah, verifikasi sandi pemilik pada alur Restore ada, shutdown paksa sesi JWT ada.

---

## Bagian 4 — Validasi Fokus dan Relevansi Konten

> Pastikan dokumen hanya berisi informasi yang sesuai lingkup Security Design dan tidak "bocor" ke domain dokumen lain.

### 4.1. Identifikasi Konten Tidak Relevan

- [ ] **4.1.1** Baca ulang **Bab 12.2 (Pseudocode FP Murni)**. Pastikan pseudocode yang ada hanya menggambarkan **modul keamanan inti** (`login_user`, `require_permission`, `write_audit_log`, `encrypt_wa`, `decrypt_wa`, `run_backup`, `validate_env_config`). Jika ada fungsi bisnis non-keamanan yang ikut tercantum, hapus atau pindahkan ke dokumen yang lebih tepat.
- [ ] **4.1.2** Pastikan **Bab 5.3 (Matriks Akses Modul)** hanya menampilkan ringkasan matriks otorisasi yang cukup sebagai konteks keamanan, bukan mengulangi seluruh detail yang sudah ada di ACM. Periksa apakah ada level detail yang berlebihan yang seharusnya cukup direferensikan ke ACM saja.
- [ ] **4.1.3** Pastikan dokumen **tidak membahas logika bisnis** (cara menghitung HPP, cara menghitung poin insentif, dll.) yang bukan bagian dari desain keamanan. Jika ada, hapus atau pindahkan ke dokumen yang lebih tepat.
- [ ] **4.1.4** Pastikan **Bab 12.4 (Konfigurasi Server dan Firewall)** hanya berisi konfigurasi yang secara langsung berkaitan dengan keamanan sistem (ufw, chmod, bind-address), bukan konfigurasi performa atau operasional umum yang lebih cocok di System Architecture.

### 4.2. Identifikasi Konten Penting yang Hilang (Security-Specific)

- [ ] **4.2.1** **Kebijakan Rotasi Kredensial**: Periksa apakah dokumen memiliki penjelasan tentang kapan dan bagaimana JWT Secret Key, FERNET_KEY, dan BACKUP_ZIP_PASSWORD harus dirotasi/diperbarui. Jika tidak ada, tambahkan sub-bab pendek di Bab 6.5 atau 8 tentang kebijakan rotasi kredensial.
- [ ] **4.2.2** **Kebijakan Kompleksitas Sandi Pengguna**: Periksa apakah dokumen mendefinisikan aturan minimum kompleksitas kata sandi staf (panjang minimum, karakter campuran). Jika ada di SRS atau TSD, pastikan direferensikan di sini. Jika belum ada di mana pun, tambahkan ketentuan dasarnya di Bab 4 atau 8.3.
- [ ] **4.2.3** **Prosedur Onboarding Staf Baru (Security Aspect)**: Periksa apakah Bab 8.3 sudah mencakup aspek keamanan yang cukup untuk onboarding staf baru: pembatasan peran awal, wajib ganti sandi, audit log penciptaan akun. Jika kurang detail, lengkapi.
- [ ] **4.2.4** **Keamanan File Cadangan (Backup Security)**: Periksa apakah ada penjelasan tentang verifikasi integritas file cadangan (misalnya: pengecekan ukuran file, simulasi restore berkala). Bab 8.2 hanya membahas prosedur backup/restore, bukan verifikasi integritas. Tambahkan jika belum ada.
- [ ] **4.2.5** **Logging Akses Tabel Sangat Sensitif**: Periksa apakah Bab 7.2 menyebutkan secara eksplisit bahwa akses **SELECT** (bukan hanya INSERT/UPDATE/DELETE) pada tabel Sangat Sensitif (`payroll`, `pinjaman_bank`) juga dipicu audit log. Jika tidak ada, klarifikasi kebijakan ini.
- [ ] **4.2.6** **Penanganan Token JWT Kedaluwarsa saat Operasi Sedang Berjalan**: Periksa apakah dokumen menjelaskan apa yang terjadi jika token JWT kedaluwarsa di tengah proses transaksi aktif (misalnya: mid-transaction). Jika tidak ada, tambahkan penjelasan di Bab 4.2 atau 4.4.

---

## Bagian 5 — Validasi Standar Struktur Dokumen Industri

### 5.1. Periksa Kelengkapan Struktur Dokumen

- [ ] **5.1.1** Verifikasi bahwa **front matter YAML** di bagian paling atas dokumen memiliki semua field yang diperlukan: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`. Jika ada field yang hilang, tambahkan.
- [ ] **5.1.2** Verifikasi bahwa **Bab 1 (Informasi Dokumen)** memuat semua sub-bab standar: Tujuan Dokumen (1.1), Cakupan Dokumen (1.2), Posisi dalam SDLC (1.3), Hubungan dengan Dokumen Lain (1.4), Audiens Target (1.5), Definisi & Akronim (1.6). Jika ada sub-bab yang hilang, tambahkan.
- [ ] **5.1.3** Verifikasi bahwa **Bab 15 (Glosarium)** mencakup semua istilah teknis keamanan yang digunakan dalam dokumen. Jika ada istilah kunci yang digunakan dalam narasi tetapi tidak ada di glosarium (misalnya: `Fernet`, `ACID`, `Repeatable Read`, `Defense in Depth`), tambahkan entri glosariumnya.
- [ ] **5.1.4** Verifikasi bahwa **Bab 16 (Referensi Dokumen)** mencantumkan semua file referensi dengan path yang akurat dan versi yang tepat. Jika ditemukan referensi tambahan di Bagian 1.2.9, tambahkan ke Bab 16.
- [ ] **5.1.5** Verifikasi bahwa **urutan Bab** dalam dokumen mengikuti alur logis Security Design industri: Prinsip → Arsitektur → Autentikasi → Otorisasi → Proteksi Data → Audit Trail → Operasional → Diagram → Error Handling → Analisis Risiko → Implementasi Teknis → Traceability → Persetujuan → Glosarium → Referensi. Jika ada bab yang posisinya tidak logis, pindahkan.

### 5.2. Periksa Kelengkapan Matriks Ketertelusuran (Traceability)

- [ ] **5.2.1** Verifikasi bahwa **Bab 13.1** (Security Design ke SRS) memuat semua fitur keamanan utama dari SRS. Tambahkan baris yang hilang.
- [ ] **5.2.2** Verifikasi bahwa **Bab 13.2** (Security Design ke ACM) memuat semua aturan kontrol akses dari ACM. Tambahkan baris yang hilang.
- [ ] **5.2.3** Verifikasi bahwa **Bab 13.3** (Security Design ke TSD) memuat semua keputusan teknologi keamanan dari TSD. Tambahkan baris yang hilang.
- [ ] **5.2.4** Verifikasi bahwa **Bab 13.4** (Security Design ke Use Case) mencantumkan semua use case yang memiliki komponen keamanan signifikan. Periksa apakah UC-041 (Login), UC-042 (Logout), UC-004 (Retur/Batal), UC-011 (Opname), UC-016 (Backup/Restore) sudah ada dan konsisten dengan SRS.
- [ ] **5.2.5** Evaluasi apakah perlu menambahkan **Bab 13.5** untuk mapping Security Design ke BRD (Business Requirements). Jika ada kebutuhan bisnis keamanan di BRD yang tidak terpetakan di bab traceability yang ada, buat sub-bab 13.5 dan isi.

---

## Bagian 6 — Validasi Kualitas Bahasa Indonesia

### 6.1. Periksa Naturalisasi Bahasa

- [ ] **6.1.1** Baca ulang **Bab 2 (Prinsip dan Strategi Keamanan)** secara keseluruhan. Pastikan setiap kalimat dapat dibaca dengan lancar oleh seseorang yang baru pertama kali membaca dokumen ini. Perbaiki kalimat yang terlalu panjang (lebih dari 3 anak kalimat), menggunakan kata serapan asing yang tidak perlu, atau memiliki urutan kata yang tidak natural dalam Bahasa Indonesia.
- [ ] **6.1.2** Periksa penggunaan **istilah teknis asing yang tidak dikursifkan**. Semua istilah teknis asing yang tidak memiliki padanan Bahasa Indonesia baku harus ditulis dengan *italic* dan dijelaskan pada kemunculan pertamanya atau di Glosarium. Contoh: *brute-force*, *stateless session*, *parameterized query*.
- [ ] **6.1.3** Periksa konsistensi penggunaan **kata "wajib", "harus", "perlu"**. Dalam konteks spesifikasi teknis, gunakan "wajib" untuk hal yang bersifat mandatory (MUST), "perlu" untuk hal yang direkomendasikan (SHOULD), dan "dapat" untuk hal yang opsional (MAY). Pastikan penggunaan ketiga kata ini konsisten di seluruh dokumen.
- [ ] **6.1.4** Cari dan perbaiki kalimat yang menggunakan **konstruksi pasif berlebihan** yang membuat kalimat ambigu tentang siapa yang bertanggung jawab melakukan suatu aksi (mis. "data akan dienkripsi" menjadi "sistem mengenkripsi data"). Konteks teknis membutuhkan subjek yang jelas.
- [ ] **6.1.5** Periksa konsistensi penulisan nama entitas sistem: `pengguna`, `kasir`, `pemilik`, `audit_logs`, `shift_handover` — pastikan setiap nama yang merujuk ke tabel database menggunakan format `kode` (backtick), sementara nama peran manusia menggunakan format teks biasa.

### 6.2. Periksa Ambiguitas dan Kejelasan Instruksi

- [ ] **6.2.1** Baca ulang **Bab 8 (Desain Keamanan Operasional)** secara keseluruhan dan identifikasi setiap prosedur yang instruksinya bisa ditafsirkan lebih dari satu cara oleh junior programmer. Perjelas dengan menambahkan urutan langkah bernomor atau contoh konkret jika perlu.
- [ ] **6.2.2** Baca ulang **Bab 10.6 (SOP Respon Insiden)** dan verifikasi bahwa setiap fase (Deteksi, Penahanan, Analisis, Pemulihan, Pembelajaran) memiliki langkah-langkah yang cukup spesifik untuk dapat dieksekusi secara mandiri oleh pemilik toko tanpa memerlukan konsultasi tambahan.
- [ ] **6.2.3** Verifikasi bahwa setiap **tabel dalam dokumen** memiliki header kolom yang cukup jelas dan deskriptif, tidak hanya berisi singkatan yang tidak dijelaskan.

---

## Bagian 7 — Validasi Kesiapan sebagai Referensi Fase SDLC Berikutnya

### 7.1. Kesiapan untuk Fase 04 — Implementation

- [ ] **7.1.1** Verifikasi bahwa **Bab 12.1 (Penempatan Modul Keamanan)** mendefinisikan dengan jelas nama file, path relatif, dan tanggung jawab setiap modul keamanan Python. Seorang junior programmer harus bisa langsung tahu file mana yang harus dibuat dan fungsi apa yang harus ada di dalamnya.
- [ ] **7.1.2** Verifikasi bahwa **pseudocode di Bab 12.2** cukup detail untuk dapat diterjemahkan langsung menjadi kode Python yang berfungsi tanpa perlu menebak-nebak logika. Semua fungsi keamanan inti (`login_user`, `require_permission`, `write_audit_log`, `encrypt_wa`, `run_backup`, `validate_env_config`) harus ada pseudocodenya.
- [ ] **7.1.3** Verifikasi bahwa **semua dependency Python** yang dibutuhkan oleh pseudocode (import statement di Bab 12.2) sudah tercantum secara eksplisit: `bcrypt`, `jwt`, `datetime`, `subprocess`, `collections.namedtuple`, `typing.Callable`, `cryptography.fernet.Fernet`. Pastikan versi library tidak bertentangan dengan yang ada di `requirements.txt`.
- [ ] **7.1.4** Periksa apakah ada **edge case keamanan** yang belum ditangani dalam pseudocode: misalnya, apa yang terjadi jika `db_conn` adalah `None` saat `write_audit_log` dipanggil? Tambahkan penanganan error untuk edge case yang kritis.

### 7.2. Kesiapan untuk Fase 05 — Testing

- [ ] **7.2.1** Verifikasi bahwa **Bab 1.4 (Dokumen Output)** menyebutkan dengan jelas bahwa dokumen ini menjadi panduan pembuatan test case QA untuk: (a) Penetration testing RBAC, (b) SQL Injection test, (c) Session expiration test, (d) Brute-force lockout test. Jika ada jenis pengujian keamanan yang relevan tetapi tidak disebutkan, tambahkan.
- [ ] **7.2.2** Periksa apakah setiap **kode error di Bab 10** memiliki pemicu yang cukup spesifik sehingga tim QA dapat membuat test case yang memverifikasi bahwa kode error tersebut muncul pada kondisi yang tepat.
- [ ] **7.2.3** Periksa apakah **matriks risiko di Bab 11** dapat digunakan langsung sebagai dasar pembuatan test scenario security testing. Setiap risiko harus memiliki mitigasi teknis yang cukup konkret untuk diuji.

---

## Bagian 8 — Periksa Referensi Tambahan

- [ ] **8.1** Berdasarkan hasil pembacaan di Bagian 1.2.9, jika ditemukan file `docs/sdlc/03_design/04_cli_interaction_flow.md` atau dokumen lain yang tidak terdaftar di Bab 16 namun memiliki konten relevan dengan keamanan (misalnya: alur navigasi menu CLI yang memengaruhi implementasi RBAC guard), tambahkan ke daftar referensi Bab 16 dengan keterangan yang tepat.
- [ ] **8.2** Periksa apakah perlu menambahkan referensi ke **OWASP ASVS** atau **UU PDP No. 27/2022** sebagai referensi eksternal standar industri di Bab 16. Jika ya, tambahkan baris dengan keterangan "Referensi Eksternal Standar Industri".
- [ ] **8.3** Verifikasi bahwa **semua path file referensi** di Bab 16 akurat dan konsisten (menggunakan forward slash `/`, path relatif dari root proyek, dan ekstensi file yang benar). Jika ada path yang salah atau file yang tidak ada, koreksi atau hapus.

---

## Bagian 9 — Penulisan Ulang Dokumen (Overwrite)

> **PERINGATAN KRITIS**: Bagian ini adalah langkah final dan tidak dapat dibatalkan. Pastikan semua Bagian 1–8 telah diselesaikan secara lengkap sebelum mengeksekusi Bagian 9.

### 9.1. Persiapan Penulisan Ulang

- [ ] **9.1.1** Kompilasikan seluruh temuan dari Bagian 2, 3, 4, 5, 6, 7, dan 8 ke dalam catatan internal. Pastikan setiap perbaikan, penambahan, dan koreksi sudah jelas dan siap untuk diterapkan.
- [ ] **9.1.2** Siapkan versi dokumen yang akan ditulis. Versi dokumen yang baru adalah **v1.2**. Tanggal dokumen yang baru adalah **tanggal hari ini saat issue ini dieksekusi**. Status dokumen yang baru adalah `Review`.
- [ ] **9.1.3** Siapkan entri baru untuk tabel **Riwayat Perubahan Dokumen** yang akan ditambahkan di atas baris v1.1. Entri baru harus merangkum secara singkat semua perubahan yang dilakukan berdasarkan temuan validasi issue ini.

### 9.2. Eksekusi Penulisan Ulang (Overwrite)

- [ ] **9.2.1** Tulis ulang **seluruh dokumen** `docs/sdlc/03_design/06_security_design.md` dari baris pertama (front matter YAML) hingga baris terakhir (Bab 16 Referensi Dokumen) dengan menimpa (overwrite) file yang ada.
- [ ] **9.2.2** **ATURAN MUTLAK — NO TRUNCATION**: Seluruh teks dari baris pertama hingga terakhir HARUS ditulis ulang sepenuhnya. Tidak boleh ada bab, sub-bab, tabel, blok kode, diagram Mermaid, atau kalimat yang dipotong, diringkas, atau dihilangkan. Semua konten yang sudah valid dan benar harus tetap ada; hanya konten yang bermasalah (berdasarkan temuan Bagian 2–8) yang diubah/ditambah/diperbaiki.
- [ ] **9.2.3** Pastikan **versi dokumen** di front matter YAML berubah dari versi sebelumnya menjadi `1.2`.
- [ ] **9.2.4** Pastikan **tanggal dokumen** di front matter YAML diperbarui ke tanggal hari ini.
- [ ] **9.2.5** Pastikan **entri v1.2** di tabel Riwayat Perubahan Dokumen ditambahkan sebagai baris paling atas, di atas baris v1.1.
- [ ] **9.2.6** Pastikan **semua perbaikan** dari Bagian 2, 3, 4, 5, 6, 7, dan 8 telah diterapkan ke dalam dokumen yang ditulis ulang.
- [ ] **9.2.7** Pastikan **referensi baru** yang ditemukan di Bagian 8 (jika ada) ditambahkan sebagai baris baru di bagian paling bawah tabel **Bab 16 Referensi Dokumen**, dengan nomor urut yang dilanjutkan dari baris terakhir yang sudah ada.

### 9.3. Verifikasi Pasca-Penulisan Ulang

- [ ] **9.3.1** Buka kembali file `docs/sdlc/03_design/06_security_design.md` yang baru ditulis dan verifikasi bahwa versi di front matter YAML sudah `1.2`.
- [ ] **9.3.2** Verifikasi bahwa baris pertama dokumen adalah `---` (awal front matter YAML) dan baris terakhir dokumen adalah baris terakhir dari Bab 16 (Referensi Dokumen) — bukan baris kosong berlebihan, bukan terpotong, bukan hanya sebagian bab.
- [ ] **9.3.3** Hitung ulang jumlah baris dokumen. Dokumen hasil overwrite seharusnya memiliki jumlah baris yang **lebih banyak atau sama** dibandingkan dokumen versi sebelumnya (karena ada penambahan konten), bukan lebih sedikit.
- [ ] **9.3.4** Verifikasi bahwa **semua 6 (atau lebih, jika ditambahkan) blok diagram Mermaid** masih ada dan sintaksnya valid (setiap blok diawali ` ```mermaid ` dan diakhiri ` ``` `).
- [ ] **9.3.5** Verifikasi bahwa **Bab 16 Referensi Dokumen** mencantumkan semua referensi yang dibutuhkan, termasuk referensi baru yang mungkin ditambahkan.

---

## Bagian 10 — Ringkasan Kriteria Kelulusan Validasi

Dokumen dinyatakan **LULUS** validasi dan siap digunakan sebagai referensi fase SDLC berikutnya apabila semua kriteria berikut terpenuhi:

| No | Kriteria Kelulusan | Status |
|:--:|---|:--:|
| 1 | Seluruh data dari 8 dokumen referensi telah dikomparasi dan perbedaan/kesenjangan telah diatasi | `[ ]` |
| 2 | Tidak ada nilai numerik yang tidak konsisten antar bab dalam dokumen | `[ ]` |
| 3 | Tidak ada kode error yang digunakan tetapi tidak didefinisikan, atau didefinisikan tetapi tidak pernah digunakan | `[ ]` |
| 4 | Jumlah diagram Mermaid sesuai dengan klaim di Bab 1.2, semua diagram valid dan akurat | `[ ]` |
| 5 | Tidak ada data kosong, placeholder TBD, atau sel tabel yang tidak terisi | `[ ]` |
| 6 | Semua DDL tabel keamanan di Bab 7.1 identik dengan DDL di `01_database_schema.sql` | `[ ]` |
| 7 | Matriks ketertelusuran (Bab 13) mencakup semua mapping ke SRS, ACM, TSD, dan Use Case | `[ ]` |
| 8 | Bahasa Indonesia yang digunakan natural, tidak ambigu, dan tidak memiliki kalimat pasif berlebihan | `[ ]` |
| 9 | Dokumen memiliki konten yang cukup spesifik untuk dijadikan panduan implementasi fase 04 dan testing fase 05 | `[ ]` |
| 10 | Versi dokumen telah diperbarui ke v1.2 dan tabel Riwayat Perubahan telah diisi | `[ ]` |
| 11 | File berhasil di-overwrite secara penuh tanpa ada truncation | `[ ]` |
| 12 | Referensi baru (jika ada) telah ditambahkan di Bab 16 | `[ ]` |

---

## Catatan Tambahan untuk Pelaksana

### Hal-hal Khusus Dokumen Security Design yang Perlu Perhatian Lebih

1. **Verifikasi Kriptografi**: Pastikan semua klaim kriptografi dalam dokumen (bcrypt, JWT HS256, AES-256 ZIP, Fernet) menggunakan library Python yang aktif dirawat (bukan deprecated). Verifikasi kompatibilitas versi dari `requirements.txt`.

2. **Konsistensi Nama Fungsi Pseudocode vs. Implementasi**: Nama fungsi dalam pseudocode Bab 12.2 (`login_user`, `require_permission`, `write_audit_log`, `encrypt_wa`, `decrypt_wa`, `run_backup`, `validate_env_config`) harus dijaga konsistensinya dengan nama fungsi yang akan diimplementasikan di `middleware/rbac.py`, `middleware/logger.py`, `utils/backup.py`, `utils/crypto.py`.

3. **Ancaman Spesifik UMKM**: Model ancaman di Bab 2.2 harus tetap fokus pada ancaman **lokal yang realistis** untuk toko percetakan UMKM offline, bukan ancaman enterprise atau internet. Hindari menambahkan ancaman yang tidak relevan hanya untuk terlihat komprehensif.

4. **Integritas ACID pada Konteks Kasir**: Setiap kali dokumen membahas operasi keuangan (transaksi, retur, pengeluaran), harus ada referensi eksplisit ke ACID transaction (`START TRANSACTION` / `COMMIT` / `ROLLBACK`). Pastikan tidak ada deskripsi operasi multi-tabel yang menghilangkan konteks transaksi database.

5. **Dokumen ini adalah Blueprint Keamanan — Bukan Panduan Umum**: Setiap bab harus dapat menjawab pertanyaan: "Bagaimana sistem AbuCom mengamankan [aspek ini]?" Jika sebuah bab tidak menjawab pertanyaan tersebut secara konkret, bab tersebut perlu diperkuat.

---

*Issue ini dibuat pada 2026-05-29 oleh Senior Security Architect & Cybersecurity Compliance Specialist untuk deksekusi oleh junior programmer atau AI model yang lebih kecil/murah dalam kerangka SDLC AbuCom — Sistem Manajemen Terpadu Usaha Percetakan.*
