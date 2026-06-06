---
issue_id     : 0116
judul        : Feature Rate Limiting Login dengan Lockout Otomatis
prioritas    : TINGGI (Keamanan)
status       : OPEN
modul        : M.7 — Keamanan, Audit & Handover
tanggal      : 2026-06-06
penyusun     : Claude Opus 4.6 (Thinking) — Strategi Sistem & Keamanan
pelaksana    : Junior Programmer / LLM Model AI (Level Implementasi)
estimasi     : 4–6 jam kerja
---

# Issue #0116 — Feature Rate Limiting Login dengan Lockout Otomatis

---

## 1. Persona Pelaksana

**Persona yang WAJIB diadopsi oleh pelaksana issue ini:**

> **Senior Security Backend Engineer** — Seorang ahli keamanan backend yang teliti, disiplin, dan memahami mendalam tentang mekanisme pertahanan brute-force, pengelolaan state otentikasi, penulisan query database terparameter, pencatatan audit trail, dan paradigma pemrograman fungsional (FP) murni Python. Persona ini TIDAK tergesa-gesa, mengutamakan ketepatan logika di atas kecepatan, dan selalu memvalidasi setiap perubahan terhadap dampaknya pada fitur lain yang sudah ada.

---

## 2. Dokumen Referensi Utama

Berikut adalah dokumen SDLC yang **WAJIB** dibaca dan diekstrak informasinya sebelum memulai implementasi:

| No | Dokumen Referensi | Path Relatif | Alasan Pemilihan |
|:---:|---|---|---|
| 1 | **Security Design v1.2** | `docs/sdlc/03_design/06_security_design.md` | **Sumber utama (SSoT)** — Bab 4.3 (Rate Limiting & Penguncian Akun), Bab 4.1 (bcrypt), Bab 4.2 (JWT Session), Bab 7.2 (Audit Trail), Bab 9.1 (Alur Login Sequence Diagram), Bab 10.1 (Kode Error ERR-AUTH), Bab 12.2 (Pseudocode login_user) |
| 2 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | Standar FP murni, Result Pattern, type hints, naming convention, sanitasi input, secure coding, error code catalog |
| 3 | **Database Schema v1.2** | `docs/sdlc/03_design/01_database_schema.sql` (atau `schema.sql` di root) | DDL tabel `pengguna` — kolom `failed_login_attempts`, `locked_until`, constraint CHECK |
| 4 | **Module Structure v1.1** | `docs/sdlc/04_implementation/03_module_structure.md` | Penempatan file sesuai arsitektur 4-layer |
| 5 | **Test Plan v1.1** | `docs/sdlc/05_testing/01_test_plan.md` | Standar unit testing dan test case |
| 6 | **CLI Interaction Flow v1.1** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur navigasi login di terminal CLI |
| 7 | **Access Control Matrix v1.1** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Aturan rate limiting login — ACM Bab 6.5 |

> **Catatan**: File `narasi.txt` (`docs/sdlc/narasi.txt`) **TIDAK** diperlukan sebagai referensi langsung untuk issue ini karena issue ini bersifat teknis keamanan murni yang spesifikasinya sudah lengkap di dokumen Security Design. Narasi hanya memberikan konteks bisnis umum.

---

## 3. Rangkuman Detail Data dari Dokumen Referensi

Berikut adalah **seluruh detail data** yang relevan dan spesifik untuk fitur rate limiting login, diekstrak dari dokumen referensi.

### 3.1. Spesifikasi Rate Limiting Login (Security Design Bab 4.3)

| Parameter | Nilai | Keterangan |
|---|---|---|
| **Threshold kegagalan maksimal** | **5 kali berturut-turut** | Percobaan login salah yang diizinkan sebelum lockout |
| **Durasi suspensi (lockout)** | **10 menit** | Akun ditangguhkan selama 10 menit setelah kegagalan ke-5 |
| **Kolom counter di DB** | `failed_login_attempts` | Tipe: `INT NOT NULL DEFAULT 0`, Constraint: `CHECK (BETWEEN 0 AND 5)` |
| **Kolom lockout di DB** | `locked_until` | Tipe: `TIMESTAMP NULL DEFAULT NULL` |
| **Update saat gagal ke-5** | `failed_login_attempts = 5`, `locked_until = DATE_ADD(NOW(), INTERVAL 10 MINUTE)` | Menandai akun terkunci |
| **Reset saat login sukses** | `failed_login_attempts = 0`, `locked_until = NULL` | Membersihkan counter dan lockout |
| **Kode error lockout** | `ERR-AUTH-002` | `"Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!"` |
| **Kode error kredensial salah** | `ERR-AUTH-001` | `"Kredensial tidak valid. Silakan coba kembali!"` |

### 3.2. Alur Login Lengkap (Security Design Bab 9.1 — Sequence Diagram)

```
1. Staf masukkan username & password (getpass)
2. Panggil login_user(username, password)
3. SELECT password_hash, role, locked_until, failed_login_attempts FROM pengguna WHERE username = %s
4. IF akun ditangguhkan (locked_until > NOW):
     → Tampilkan ERR-AUTH-002 (Akun Ditangguhkan 10 Mnt)
5. ELSE (akun terbuka):
     → Verifikasi sandi via bcrypt.checkpw()
     5a. IF sandi SALAH:
         → UPDATE failed_login_attempts = attempts + 1
         → IF kegagalan ke-5:
             → UPDATE locked_until = NOW() + 10 MINUTE
             → INSERT audit_logs (action_type='ACCOUNT_LOCKOUT')
         → ELSE:
             → INSERT audit_logs (action_type='LOGIN_FAILED')
         → Tampilkan ERR-AUTH-001
     5b. IF sandi BENAR:
         → UPDATE failed_login_attempts = 0, locked_until = NULL
         → Generate JWT Token (HS256, exp 8 jam)
         → INSERT audit_logs (action_type='LOGIN_SUCCESS')
         → Return session_state dict
```

### 3.3. Struktur Tabel `pengguna` (DDL Relevan)

```sql
CREATE TABLE pengguna (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nama_lengkap VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(30) NOT NULL,
    failed_login_attempts INT NOT NULL DEFAULT 0,
    locked_until TIMESTAMP NULL DEFAULT NULL,
    cabang_id INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_pengguna_failed_login_attempts CHECK (failed_login_attempts BETWEEN 0 AND 5),
    CONSTRAINT fk_pengguna_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id)
) ENGINE=InnoDB;
```

### 3.4. Audit Trail yang WAJIB Dicatat (Security Design Bab 7.2)

| Event | action_type di audit_logs | Kapan Dipicu |
|---|---|---|
| Login berhasil | `LOGIN_SUCCESS` | Setelah password valid & JWT terbit |
| Login gagal (password salah) | `LOGIN_FAILED` | Setiap kali password salah (percobaan 1–4) |
| Akun terkunci | `ACCOUNT_LOCKOUT` | Saat kegagalan ke-5 yang memicu lockout |

### 3.5. Fraud Detection Terkait (Security Design Bab 7.4)

> **Deteksi Anomali Login Gagal Berulang**: Terjadinya kegagalan login berturut-turut sebanyak **> 10 kali** pada satu alamat IP kasir yang sama dalam durasi **1 jam** harus memicu tanda peringatan visual pada dashboard Pemilik.

### 3.6. Kode Error Relevan (Security Design Bab 10.1)

| Kode | Pesan CLI | Pemicu |
|---|---|---|
| `ERR-AUTH-001` | `ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!` | Username salah ATAU password salah |
| `ERR-AUTH-002` | `ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!` | Kegagalan login ke-5 berturut-turut |

### 3.7. Standar Pemrograman yang WAJIB Dipatuhi (Coding Standard v1.2)

- **FP Murni**: Tanpa `class` di alur bisnis utama
- **Result Pattern**: Return `NamedTuple('Result', ['is_success', 'data', 'error_msg'])`
- **Parameterized Query**: Wajib `%s` binding, DILARANG f-string SQL
- **Type Hints**: Wajib PEP 484 pada semua fungsi publik
- **Docstring**: Wajib PEP 257 Google Style multi-baris
- **Sanitasi Input**: Buang karakter kontrol ASCII < `\x20`
- **Immutability**: NamedTuple / frozen dataclass untuk data internal
- **Error Handling**: Result pattern, BUKAN exception abuse
- **Naming**: `snake_case` untuk fungsi/variabel, `UPPER_SNAKE_CASE` untuk konstanta
- **Audit Trail**: Wajib catat `old_value`/`new_value` dalam format JSON

---

## 4. Batasan, Cakupan & Alur Pengerjaan

### 4.1. Cakupan (IN-SCOPE)

- [ ] Verifikasi dan validasi bahwa logika rate limiting di `logic/auth_handler.py` → fungsi `login_user()` sudah lengkap dan benar sesuai spesifikasi Security Design Bab 4.3
- [ ] Verifikasi dan validasi bahwa repository layer di `db/pengguna_repository.py` → fungsi `update_failed_login()` dan `reset_failed_login()` sudah lengkap dan benar
- [ ] Verifikasi dan validasi bahwa layer CLI di `cli/__init__.py` → fungsi `start_cli_app()` menampilkan pesan error lockout dengan benar
- [ ] Verifikasi bahwa audit trail `LOGIN_FAILED`, `ACCOUNT_LOCKOUT`, dan `LOGIN_SUCCESS` tercatat dengan benar ke tabel `audit_logs`
- [ ] Implementasi unit test komprehensif untuk seluruh skenario rate limiting di `tests/test_rate_limiting_login.py`
- [ ] Pastikan skenario edge case ditangani: lockout yang sudah expired, counter reset setelah login sukses, percobaan saat lockout masih aktif
- [ ] Verifikasi kesesuaian antara constraint database (`CHECK BETWEEN 0 AND 5`) dengan logika Python
- [ ] Pastikan pesan error yang ditampilkan sesuai dengan katalog error code di Security Design Bab 10.1

### 4.2. Di Luar Cakupan (OUT-OF-SCOPE)

- ❌ Fraud detection dashboard pemilik (> 10 kali gagal dalam 1 jam) — akan dikerjakan di issue terpisah
- ❌ Modifikasi skema database (kolom `failed_login_attempts` dan `locked_until` sudah tersedia)
- ❌ Fitur idle timeout 30 menit (bukan bagian dari rate limiting login)
- ❌ Perubahan pada fitur logout
- ❌ Perubahan pada RBAC/otorisasi menu
- ❌ Perubahan pada fitur registrasi pengguna baru

### 4.3. Alur Pengerjaan Bertahap

```
Tahap 1: BACA & PAHAMI     → Baca semua file referensi yang sudah dipilih
Tahap 2: AUDIT KODE        → Audit kode existing apakah sudah sesuai spesifikasi
Tahap 3: PERBAIKAN/PENAMBAHAN → Perbaiki jika ada gap, tambahkan jika ada yang kurang
Tahap 4: UNIT TEST         → Tulis test komprehensif
Tahap 5: VALIDASI          → Jalankan test, pastikan 100% pass
Tahap 6: REVIEW AKHIR      → Cross-check ulang terhadap spesifikasi
```

---

## 5. Instruksi Perlindungan Fitur Lain

> **PERINGATAN KRITIS**: Implementasi fitur rate limiting login **TIDAK BOLEH** menyentuh atau merusak fitur lain yang sudah berjalan.

Berikut checklist perlindungan:

- [ ] **JANGAN** mengubah signature fungsi `login_user()` yang sudah dipanggil oleh `cli/__init__.py`
- [ ] **JANGAN** mengubah signature fungsi `logout_user()` di `logic/auth_handler.py`
- [ ] **JANGAN** mengubah signature atau perilaku fungsi `hash_password()` dan `verify_password()` di `middleware/auth_jwt.py`
- [ ] **JANGAN** mengubah signature fungsi `create_jwt_session()` dan `verify_jwt_session()` di `middleware/auth_jwt.py`
- [ ] **JANGAN** mengubah signature fungsi `log_audit_trail()` di `middleware/audit_logger.py`
- [ ] **JANGAN** mengubah skema DDL tabel `pengguna` atau tabel lainnya
- [ ] **JANGAN** mengubah fungsi `get_pengguna_by_username()` kecuali ada gap yang ditemukan
- [ ] **JANGAN** mengubah file `config/settings.py` atau `.env`
- [ ] **JANGAN** menambahkan dependensi baru ke `requirements.txt`
- [ ] Setelah implementasi, **JALANKAN** seluruh test suite yang sudah ada untuk memastikan tidak ada regresi:
  ```bash
  python -m pytest tests/ -v --tb=short
  ```

---

## 6. Instruksi Kualitas Pengerjaan

> **KAIDAH UTAMA**: Kerjakan dengan **RAPI**, **BERSIH**, **TIDAK TERGESA-GESA**, dan **TIDAK BURU-BURU**. Kualitas di atas kecepatan. Setiap baris kode harus memiliki tujuan yang jelas.

- [ ] Setiap fungsi baru/modifikasi **WAJIB** memiliki docstring PEP 257 lengkap (deskripsi, Args, Returns, Example)
- [ ] Setiap fungsi baru/modifikasi **WAJIB** memiliki type hints PEP 484
- [ ] Setiap query SQL **WAJIB** menggunakan parameterized query `%s`
- [ ] Setiap percabangan logika **WAJIB** memiliki komentar penjelasan singkat
- [ ] Kode **WAJIB** mengikuti Result Pattern (`NamedTuple('Result', ['is_success', 'data', 'error_msg'])`)
- [ ] Variabel **WAJIB** menggunakan `snake_case` yang deskriptif dan selaras dengan nama kolom DB
- [ ] Konstanta **WAJIB** menggunakan `UPPER_SNAKE_CASE`
- [ ] Import **WAJIB** diurutkan: stdlib → third-party → local modules
- [ ] Indentasi **WAJIB** 4 spasi, batas baris maksimal 120 karakter
- [ ] **WAJIB** menutup cursor database di blok `finally`

---

## 7. Instruksi Kelengkapan Pengerjaan

> **KAIDAH**: Pastikan pengerjaan issue ini **LENGKAP** dan **TUNTAS** sehingga tidak perlu diinterupsi atau dipertanyakan ulang karena ada bagian yang kurang.

Checklist kelengkapan final:

- [ ] Logika rate limiting di `login_user()` sudah handle semua skenario (lihat Tahap 2 detail di bawah)
- [ ] Pesan error sesuai katalog (`ERR-AUTH-001`, `ERR-AUTH-002`)
- [ ] Audit trail tercatat untuk ketiga event (`LOGIN_FAILED`, `ACCOUNT_LOCKOUT`, `LOGIN_SUCCESS`)
- [ ] Counter `failed_login_attempts` ter-reset ke 0 setelah login sukses
- [ ] Kolom `locked_until` ter-set ke `NULL` setelah login sukses
- [ ] Lockout yang sudah expired memperbolehkan login kembali
- [ ] Unit test mencakup minimal 10+ skenario (lihat detail di Tahap 4)
- [ ] Semua test yang sudah ada sebelumnya tetap PASS (tidak ada regresi)
- [ ] Tidak ada `TODO` atau `FIXME` baru yang dibiarkan tanpa penjelasan

---

## 8. Instruksi Penanganan Data Kosong

> Jika ada data spesifik yang **TIDAK DITEMUKAN** di file referensi atau kode sumber, **KOMUNIKASIKAN** dengan menambahkan komentar di kode dan catatan di bagian akhir issue ini.

Format penandaan:

```python
# ⚠️ DATA_KOSONG: [Deskripsi data yang tidak ditemukan]
# Referensi: [Nama dokumen yang seharusnya memuat data ini]
# Tindak Lanjut: [Saran tindakan — tanyakan ke pemilik / buat issue baru]
```

---

## 9. Instruksi Tambahan Khusus Rate Limiting

### 9.1. Pertimbangan Keamanan Tambahan

- [ ] **Timing Attack Prevention**: Pastikan waktu respon antara "username salah" dan "password salah" tidak berbeda signifikan. Jika username tidak ditemukan, tetap return `ERR-AUTH-001` (bukan pesan khusus "username tidak ditemukan") agar penyerang tidak bisa menebak username valid.
- [ ] **Timezone Consistency**: Pastikan perbandingan `locked_until > NOW()` menggunakan timezone yang konsisten (baik keduanya timezone-aware atau keduanya timezone-naive). Perhatikan bahwa MySQL `TIMESTAMP` menyimpan dalam UTC.
- [ ] **Atomic Operation**: Pastikan update `failed_login_attempts` dan `locked_until` dilakukan dalam satu transaksi ACID agar tidak terjadi race condition.
- [ ] **Counter Increment Accuracy**: Pastikan counter `failed_login_attempts` di-increment berdasarkan nilai terbaru dari database (bukan dari cache), untuk menghindari situasi concurrent login attempts.

### 9.2. Pertimbangan Pengalaman Pengguna (UX) CLI

- [ ] Saat akun terkunci, tampilkan informasi berapa menit tersisa sebelum lockout expired (jika memungkinkan)
- [ ] Gunakan warna merah ANSI tebal untuk pesan error lockout (sesuai Coding Standard Bab 11.5)
- [ ] Setelah gagal login (tapi belum lockout), tampilkan informasi sisa percobaan yang tersisa (contoh: "Anda memiliki 2 percobaan tersisa sebelum akun dikunci.")

---

## 10. Tahapan Implementasi Detail (Low-Level Checklist)

### Tahap 1: Pembacaan dan Pemahaman Dokumen Referensi

- [ ] Baca file `docs/sdlc/03_design/06_security_design.md` — fokus pada:
  - [ ] Bab 4.3 (Rate Limiting dan Penguncian Akun) — catat semua parameter numerik
  - [ ] Bab 9.1 (Alur Otentikasi Login CLI — Sequence Diagram) — pahami setiap langkah
  - [ ] Bab 7.2 (Event Pemicu Pencatatan Audit) — catat jenis audit yang wajib dicatat
  - [ ] Bab 10.1 (Kategori ERR-AUTH-xxx) — catat pesan error yang tepat
  - [ ] Bab 12.2 (Pseudocode login_user) — gunakan sebagai baseline referensi
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — fokus pada:
  - [ ] Bab 2.2 (FP Murni, Result Pattern, tanpa class)
  - [ ] Bab 10.1–10.6 (Secure Coding Standard)
  - [ ] Bab 11.5 (Error Code Catalog & format visual)
- [ ] Baca file `schema.sql` (atau `docs/sdlc/03_design/01_database_schema.sql`) — fokus pada:
  - [ ] Definisi tabel `pengguna` — perhatikan kolom `failed_login_attempts`, `locked_until`, dan constraint CHECK
  - [ ] Definisi tabel `audit_logs` — perhatikan kolom `action_type`, `old_value`, `new_value`

### Tahap 2: Audit Kode Existing — Validasi Kesesuaian dengan Spesifikasi

**File 1: `logic/auth_handler.py` → fungsi `login_user()`**

- [ ] Baca seluruh isi file `logic/auth_handler.py`
- [ ] Verifikasi: Apakah fungsi memeriksa status lockout (`locked_until > now`) SEBELUM verifikasi password?
  - ✅ Sudah ada di baris 51–62
- [ ] Verifikasi: Apakah counter `failed_login_attempts` di-increment dengan benar (dari DB, bukan hardcode)?
  - ✅ Sudah ada di baris 69: `attempts = user['failed_login_attempts'] + 1`
- [ ] Verifikasi: Apakah lockout dipicu pada kegagalan ke-5 (`attempts >= 5`)?
  - ✅ Sudah ada di baris 70: `if attempts >= 5:`
- [ ] Verifikasi: Apakah `locked_until` di-set ke `NOW() + 10 MINUTE`?
  - ✅ Sudah ada di baris 71: `locked_until = datetime.datetime.now() + datetime.timedelta(minutes=10)`
- [ ] Verifikasi: Apakah audit trail `ACCOUNT_LOCKOUT` dicatat saat lockout terpicu?
  - ✅ Sudah ada di baris 74–82
- [ ] Verifikasi: Apakah audit trail `LOGIN_FAILED` dicatat saat password salah (percobaan 1–4)?
  - ✅ Sudah ada di baris 91–99
- [ ] Verifikasi: Apakah audit trail `LOGIN_SUCCESS` dicatat saat login berhasil?
  - ✅ Sudah ada di baris 114–122
- [ ] Verifikasi: Apakah counter di-reset (`failed_login_attempts = 0`, `locked_until = NULL`) setelah login sukses?
  - ✅ Sudah ada di baris 103: `reset_failed_login(user['id'], db_conn)`
- [ ] Verifikasi: Apakah username tidak ditemukan mengembalikan `ERR-AUTH-001` (bukan pesan spesifik "tidak ditemukan")?
  - ✅ Sudah ada di baris 47: mengembalikan `ERR-AUTH-001`
- [ ] Verifikasi: Apakah input username disanitasi dari karakter kontrol ASCII?
  - ✅ Sudah ada di baris 36: `sanitasi_input_cli(username)`
- [ ] **GAP DITEMUKAN 1**: Timezone handling — baris 52 menggunakan `datetime.datetime.now()` (timezone-naive), sedangkan baris 55–56 melakukan pengecekan `locked_until.tzinfo`. Perlu diverifikasi bahwa perbandingan timezone konsisten antara Python dan MySQL.
- [ ] **GAP DITEMUKAN 2**: Sisa percobaan login — tidak ada informasi ke pengguna tentang berapa sisa percobaan yang tersisa sebelum lockout. Ini bersifat UX enhancement dan opsional.
- [ ] **GAP DITEMUKAN 3**: Sisa waktu lockout — saat akun terkunci, tidak ada informasi berapa menit tersisa. Ini bersifat UX enhancement dan opsional.

**File 2: `db/pengguna_repository.py`**

- [ ] Baca seluruh isi file `db/pengguna_repository.py`
- [ ] Verifikasi: Apakah `get_pengguna_by_username()` mengambil kolom `failed_login_attempts` dan `locked_until`?
  - ✅ Sudah ada di baris 144: query SELECT menyertakan kedua kolom
- [ ] Verifikasi: Apakah `update_failed_login()` mengupdate `failed_login_attempts` DAN `locked_until` secara transaksional?
  - ✅ Sudah ada di baris 182–186: menggunakan `start_transaction()` + `commit()`
- [ ] Verifikasi: Apakah `reset_failed_login()` mereset counter ke 0 dan `locked_until` ke NULL secara transaksional?
  - ✅ Sudah ada di baris 219–223: menggunakan `start_transaction()` + `commit()`
- [ ] Verifikasi: Apakah cursor ditutup di blok `finally`?
  - ✅ Sudah ada di semua fungsi

**File 3: `middleware/audit_logger.py`**

- [ ] Baca seluruh isi file `middleware/audit_logger.py`
- [ ] Verifikasi: Apakah `log_audit_trail()` menerima `action_type` string dan menyimpan `old_value`/`new_value` dalam JSON?
  - ✅ Sudah ada: menggunakan `json.dumps()` untuk serialisasi
- [ ] Verifikasi: Apakah error pada pencatatan audit trail ditangani tanpa menghentikan alur login?
  - ✅ Sudah ada: menggunakan `try-except` dan hanya logging error

**File 4: `cli/__init__.py` → fungsi `start_cli_app()`**

- [ ] Baca seluruh isi file `cli/__init__.py`
- [ ] Verifikasi: Apakah pesan error dari `login_user()` ditampilkan ke pengguna CLI?
  - ✅ Sudah ada di baris 139–151: menampilkan `login_result.error_msg`
- [ ] Verifikasi: Apakah format pesan error menggunakan prefix `⛔` dan warna merah?
  - ✅ Sudah ada di baris 143–148
- [ ] Verifikasi: Apakah koneksi database ditutup setelah percobaan login (berhasil maupun gagal)?
  - ✅ Sudah ada di baris 134–137: menggunakan `finally` block

**File 5: `middleware/auth_jwt.py`**

- [ ] Baca seluruh isi file `middleware/auth_jwt.py`
- [ ] Verifikasi: Apakah `verify_password()` menggunakan `bcrypt.checkpw()` dengan time-safe comparison?
  - ✅ Sudah ada
- [ ] Verifikasi: Apakah ada truncation ke 72 bytes untuk kompatibilitas bcrypt?
  - ✅ Sudah ada di baris 81: `password_bytes = password_polos.encode('utf-8')[:72]`

### Tahap 3: Perbaikan Gap yang Ditemukan (Jika Ada)

Berdasarkan audit di Tahap 2, berikut perbaikan yang **PERLU** dilakukan:

#### 3A. Perbaikan Timezone Consistency di `logic/auth_handler.py`

- [ ] Buka file `logic/auth_handler.py`
- [ ] Periksa baris 52: `now = datetime.datetime.now()` dan baris 55–56 yang memeriksa `locked_until.tzinfo`
- [ ] Pastikan logika berikut sudah benar:
  ```python
  # Jika locked_until dari MySQL timezone-aware, gunakan UTC now
  # Jika locked_until dari MySQL timezone-naive, gunakan local now
  now = datetime.datetime.now()
  if user['locked_until']:
      locked_until = user['locked_until']
      if locked_until.tzinfo is not None:
          now = datetime.datetime.now(datetime.timezone.utc)
      if locked_until > now:
          return Result(False, None, 'ERR-AUTH-002: ...')
  ```
- [ ] Verifikasi bahwa kode yang ada sudah mengimplementasikan logika ini dengan benar
- [ ] Jika sudah benar, **JANGAN UBAH**. Jika ada gap, perbaiki dengan hati-hati.

#### 3B. (OPSIONAL) Enhancement: Informasi Sisa Percobaan Login

- [ ] Pertimbangkan menambahkan informasi sisa percobaan ke pesan error saat login gagal (percobaan 1–4)
- [ ] Contoh implementasi:
  ```python
  sisa_percobaan = 5 - attempts
  return Result(
      False, None,
      f'ERR-AUTH-001: Kredensial tidak valid. Sisa percobaan: {sisa_percobaan}. Silakan coba kembali!'
  )
  ```
- [ ] **PERINGATAN**: Perubahan ini mengubah format pesan `ERR-AUTH-001` dari spesifikasi asli Security Design. **Konsultasikan** dengan pemilik proyek sebelum mengimplementasikan, atau tandai sebagai `# TODO` untuk konfirmasi nanti.
  ```python
  # ⚠️ DATA_KOSONG: Spesifikasi Security Design Bab 10.1 tidak menentukan apakah pesan ERR-AUTH-001
  # boleh menyertakan informasi sisa percobaan login.
  # Referensi: docs/sdlc/03_design/06_security_design.md Bab 10.1
  # Tindak Lanjut: Konfirmasi ke pemilik proyek apakah enhancement ini diinginkan.
  ```

#### 3C. (OPSIONAL) Enhancement: Informasi Sisa Waktu Lockout

- [ ] Pertimbangkan menambahkan informasi sisa waktu lockout ke pesan error `ERR-AUTH-002`
- [ ] Contoh implementasi:
  ```python
  sisa_detik = int((locked_until - now).total_seconds())
  sisa_menit = max(1, sisa_detik // 60)
  return Result(
      False, None,
      f'ERR-AUTH-002: Akun ditangguhkan. Silakan coba lagi dalam {sisa_menit} menit.'
  )
  ```
- [ ] **PERINGATAN**: Sama seperti 3B, ini mengubah format pesan dari spesifikasi asli. Tandai sebagai `# TODO` jika belum ada konfirmasi.

### Tahap 4: Penulisan Unit Test — `tests/test_rate_limiting_login.py`

- [ ] **Buat file baru**: `tests/test_rate_limiting_login.py`
- [ ] Tambahkan header modul sesuai Coding Standard Bab 6.4:
  ```python
  """
  Nama Modul: test_rate_limiting_login.py
  Deskripsi: Unit test komprehensif untuk fitur rate limiting login
             dan lockout otomatis (Issue #0116).
             (Ref: Security Design v1.2 Bab 4.3, Test Plan v1.1)
  Author: [Nama Pelaksana]
  Tanggal: [YYYY-MM-DD]
  """
  ```
- [ ] Import modul yang diperlukan:
  ```python
  import datetime
  from unittest.mock import MagicMock, patch, call
  from collections import namedtuple
  import pytest
  
  from logic.auth_handler import login_user
  ```
- [ ] Buat mock fixture untuk `db_conn`:
  ```python
  @pytest.fixture
  def mock_db_conn():
      """Mock koneksi database MySQL."""
      conn = MagicMock()
      return conn
  ```

**Skenario Test yang WAJIB Ditulis:**

- [ ] **Test 1**: Login sukses — password benar, counter dan lockout harus di-reset
  ```
  Given: User exists, password correct, failed_login_attempts=0, locked_until=None
  When: login_user(username, password, db_conn) dipanggil
  Then: Result.is_success == True, session_state dict berisi user_id/username/role/token
  Verify: reset_failed_login() dipanggil, audit LOGIN_SUCCESS dicatat
  ```

- [ ] **Test 2**: Login gagal — password salah, percobaan pertama (counter 0 → 1)
  ```
  Given: User exists, password wrong, failed_login_attempts=0
  When: login_user(username, wrong_password, db_conn) dipanggil
  Then: Result.is_success == False, error_msg berisi 'ERR-AUTH-001'
  Verify: update_failed_login(user_id, 1, None, db_conn) dipanggil, audit LOGIN_FAILED dicatat
  ```

- [ ] **Test 3**: Login gagal — password salah, percobaan ke-4 (counter 3 → 4)
  ```
  Given: User exists, password wrong, failed_login_attempts=3
  When: login_user(username, wrong_password, db_conn) dipanggil
  Then: Result.is_success == False, error_msg berisi 'ERR-AUTH-001'
  Verify: update_failed_login(user_id, 4, None, db_conn) dipanggil, audit LOGIN_FAILED dicatat
  ```

- [ ] **Test 4**: Login gagal — password salah, percobaan ke-5 (counter 4 → 5, LOCKOUT TERPICU)
  ```
  Given: User exists, password wrong, failed_login_attempts=4
  When: login_user(username, wrong_password, db_conn) dipanggil
  Then: Result.is_success == False, error_msg berisi 'ERR-AUTH-002'
  Verify: update_failed_login(user_id, 5, <locked_until_datetime>, db_conn) dipanggil
  Verify: audit ACCOUNT_LOCKOUT dicatat
  ```

- [ ] **Test 5**: Login ditolak — akun sedang terkunci (lockout masih aktif)
  ```
  Given: User exists, locked_until = now + 5 menit (masih aktif)
  When: login_user(username, password, db_conn) dipanggil
  Then: Result.is_success == False, error_msg berisi 'ERR-AUTH-002'
  Verify: verify_password TIDAK dipanggil (login ditolak sebelum verifikasi password)
  ```

- [ ] **Test 6**: Login sukses — lockout sudah expired (locked_until < now)
  ```
  Given: User exists, password correct, locked_until = now - 1 menit (sudah expired)
  When: login_user(username, password, db_conn) dipanggil
  Then: Result.is_success == True
  Verify: reset_failed_login() dipanggil, counter dan lockout di-reset
  ```

- [ ] **Test 7**: Login gagal — username tidak ditemukan
  ```
  Given: Username tidak ada di database
  When: login_user(unknown_username, password, db_conn) dipanggil
  Then: Result.is_success == False, error_msg berisi 'ERR-AUTH-001'
  Verify: Pesan yang sama seperti password salah (timing attack prevention)
  ```

- [ ] **Test 8**: Login gagal — username kosong atau hanya whitespace
  ```
  Given: Username = '' atau '   '
  When: login_user('', password, db_conn) dipanggil
  Then: Result.is_success == False, error_msg berisi 'ERR-AUTH-001'
  ```

- [ ] **Test 9**: Login gagal — username melebihi batas panjang (> 50 karakter)
  ```
  Given: Username = 'a' * 51
  When: login_user(long_username, password, db_conn) dipanggil
  Then: Result.is_success == False, error_msg berisi 'ERR-AUTH-001'
  ```

- [ ] **Test 10**: Login sukses setelah beberapa kali gagal (counter > 0 lalu sukses)
  ```
  Given: User exists, password correct, failed_login_attempts=3 (sebelumnya pernah gagal 3x)
  When: login_user(username, correct_password, db_conn) dipanggil
  Then: Result.is_success == True
  Verify: reset_failed_login() dipanggil — counter kembali ke 0
  ```

- [ ] **Test 11**: Login gagal — database error saat query user
  ```
  Given: get_pengguna_by_username() mengembalikan error database
  When: login_user(username, password, db_conn) dipanggil
  Then: Result.is_success == False, error_msg berisi 'ERR-DB'
  ```

- [ ] **Test 12**: Sanitasi input — username mengandung karakter kontrol ASCII
  ```
  Given: Username = '\x1b[31mhacker\x1b[0m'
  When: login_user(dirty_username, password, db_conn) dipanggil
  Then: Username disanitasi menjadi '[31mhacker[0m' (karakter kontrol dibuang)
  ```

- [ ] **Test 13**: Audit trail — verifikasi format JSON pada `old_value` dan `new_value`
  ```
  Given: Login gagal yang memicu ACCOUNT_LOCKOUT
  When: log_audit_trail dipanggil
  Then: action_type == 'ACCOUNT_LOCKOUT', new_val berisi {'status': 'LOCKED'}
  ```

**Pola Mocking yang WAJIB Digunakan:**

```python
# Gunakan @patch untuk mengisolasi dependency
@patch('logic.auth_handler.get_pengguna_by_username')
@patch('logic.auth_handler.verify_password')
@patch('logic.auth_handler.reset_failed_login')
@patch('logic.auth_handler.update_failed_login')
@patch('logic.auth_handler.log_audit_trail')
@patch('logic.auth_handler.create_jwt_session')
def test_nama_skenario(
    mock_create_jwt,
    mock_log_audit,
    mock_update_failed,
    mock_reset_failed,
    mock_verify_pw,
    mock_get_user,
    mock_db_conn,
):
    # Setup mock return values
    # ...
    # Execute
    result = login_user('kasir_andi', 'PasswordSalah1!', mock_db_conn)
    # Assert
    assert result.is_success == False
    assert 'ERR-AUTH-001' in result.error_msg
```

### Tahap 5: Eksekusi dan Validasi Test

- [ ] Jalankan unit test yang baru dibuat:
  ```bash
  python -m pytest tests/test_rate_limiting_login.py -v --tb=long
  ```
- [ ] Pastikan **SEMUA test PASS** (0 failures, 0 errors)
- [ ] Jalankan seluruh test suite untuk memastikan tidak ada regresi:
  ```bash
  python -m pytest tests/ -v --tb=short
  ```
- [ ] Catat hasil test (jumlah passed, failed, errors) di laporan pengerjaan

### Tahap 6: Review Akhir dan Cross-Check

- [ ] Baca ulang Security Design Bab 4.3 — pastikan semua parameter sudah sesuai:
  - [ ] Threshold: 5 kali ✅
  - [ ] Durasi lockout: 10 menit ✅
  - [ ] Reset counter saat sukses ✅
  - [ ] Audit trail: LOGIN_FAILED, ACCOUNT_LOCKOUT, LOGIN_SUCCESS ✅
- [ ] Baca ulang Coding Standard — pastikan kode mematuhi:
  - [ ] FP murni (tanpa class) ✅
  - [ ] Result Pattern ✅
  - [ ] Parameterized query ✅
  - [ ] Type hints & docstring ✅
- [ ] Verifikasi tidak ada file yang termodifikasi di luar cakupan:
  ```bash
  git diff --name-only
  ```
  Hanya file berikut yang boleh berubah:
  - `tests/test_rate_limiting_login.py` (BARU)
  - `logic/auth_handler.py` (HANYA jika ada perbaikan gap timezone)
- [ ] Pastikan tidak ada `print()` debugging yang tertinggal
- [ ] Pastikan tidak ada import yang tidak digunakan

---

## 11. File yang Terdampak (Impact Analysis)

| File | Tipe Perubahan | Keterangan |
|---|---|---|
| `tests/test_rate_limiting_login.py` | **BARU** | File unit test baru untuk rate limiting |
| `logic/auth_handler.py` | **AUDIT/MINOR FIX** | Audit kesesuaian + perbaikan timezone jika ditemukan gap |
| `db/pengguna_repository.py` | **AUDIT SAJA** | Verifikasi kesesuaian, kemungkinan besar TIDAK ada perubahan |
| `middleware/audit_logger.py` | **AUDIT SAJA** | Verifikasi kesesuaian, TIDAK ada perubahan |
| `middleware/auth_jwt.py` | **AUDIT SAJA** | Verifikasi kesesuaian, TIDAK ada perubahan |
| `cli/__init__.py` | **AUDIT SAJA** | Verifikasi tampilan error, TIDAK ada perubahan |

---

## 12. Catatan dan Temuan Awal

### 12.1. Temuan Positif (Sudah Sesuai Spesifikasi)

Berdasarkan audit awal, implementasi rate limiting di codebase **SUDAH CUKUP LENGKAP**. Berikut ringkasan kesesuaian:

| Aspek | Status | File |
|---|---|---|
| Counter increment per kegagalan | ✅ Sesuai | `logic/auth_handler.py` baris 69 |
| Lockout setelah 5x gagal | ✅ Sesuai | `logic/auth_handler.py` baris 70–72 |
| Durasi lockout 10 menit | ✅ Sesuai | `logic/auth_handler.py` baris 71 |
| Reset counter saat login sukses | ✅ Sesuai | `logic/auth_handler.py` baris 103 |
| Cek lockout sebelum verifikasi password | ✅ Sesuai | `logic/auth_handler.py` baris 51–62 |
| Audit trail LOGIN_FAILED | ✅ Sesuai | `logic/auth_handler.py` baris 91–99 |
| Audit trail ACCOUNT_LOCKOUT | ✅ Sesuai | `logic/auth_handler.py` baris 74–82 |
| Audit trail LOGIN_SUCCESS | ✅ Sesuai | `logic/auth_handler.py` baris 114–122 |
| Parameterized query di repository | ✅ Sesuai | `db/pengguna_repository.py` |
| Sanitasi input username | ✅ Sesuai | `logic/auth_handler.py` baris 36 |
| Error code ERR-AUTH-001/002 | ✅ Sesuai | `logic/auth_handler.py` |

### 12.2. Area yang Memerlukan Perhatian

| Area | Detail | Severity |
|---|---|---|
| Timezone consistency | Perbandingan `locked_until > now` perlu dipastikan konsisten | MEDIUM |
| Informasi sisa percobaan | Tidak ada — bersifat UX enhancement opsional | LOW |
| Informasi sisa waktu lockout | Tidak ada — bersifat UX enhancement opsional | LOW |
| Unit test rate limiting | **BELUM ADA** — ini adalah deliverable utama issue ini | HIGH |

### 12.3. Data yang Tidak Ditemukan (Ditandai untuk Tindak Lanjut)

| Data | Referensi yang Diperiksa | Status |
|---|---|---|
| Apakah pesan ERR-AUTH-001 boleh menyertakan sisa percobaan | Security Design Bab 10.1 | ⚠️ Tidak disebutkan eksplisit — **perlu konfirmasi pemilik** |
| Apakah pesan ERR-AUTH-002 boleh menyertakan sisa waktu lockout | Security Design Bab 10.1 | ⚠️ Tidak disebutkan eksplisit — **perlu konfirmasi pemilik** |
| IP address dinamis untuk audit trail (saat ini hardcode `192.168.1.10`) | Security Design Bab 7.1 | ⚠️ Kolom `ip_address` di DDL `audit_logs` ada, tapi `audit_logger.py` saat ini TIDAK mengirimkan ip_address (parameternya tidak ada). Ini mungkin issue terpisah. |

---

## 13. Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **SELESAI** jika dan hanya jika:

- [ ] Seluruh skenario rate limiting berjalan sesuai spesifikasi Security Design Bab 4.3
- [ ] File `tests/test_rate_limiting_login.py` sudah dibuat dengan minimal 10+ test case
- [ ] Semua test di `tests/test_rate_limiting_login.py` **PASS** (0 failures)
- [ ] Semua test yang sudah ada sebelumnya **TETAP PASS** (0 regresi)
- [ ] Tidak ada file di luar cakupan yang termodifikasi tanpa justifikasi
- [ ] Kode mematuhi seluruh standar di Coding Standard v1.2
- [ ] Docstring dan type hints lengkap pada semua fungsi baru/modifikasi
- [ ] Tidak ada `TODO`/`FIXME` yang dibiarkan tanpa penjelasan atau rencana tindak lanjut
- [ ] Area yang memerlukan konfirmasi pemilik sudah ditandai dengan jelas

---

*Dokumen issue ini disusun pada 2026-06-06 oleh Claude Opus 4.6 (Thinking) — Strategi Sistem & Keamanan, berdasarkan analisis mendalam terhadap 7 dokumen SDLC dan 6 file kode sumber existing.*
