---
issue_id  : 0107
judul     : Unit Test — Feature Registrasi Akun Pengguna dengan Enkripsi bcrypt
tipe      : unit-testing
prioritas : High
status    : Open
dibuat    : 2026-06-06
target_file_output : tests/unit/logic/test_unit_registrasi_pengguna.py
dokumen_referensi_utama:
  - docs/sdlc/04_implementation/01_coding_standard.md (v1.2)
  - docs/sdlc/05_testing/01_test_plan.md (v1.2)
  - docs/sdlc/05_testing/02_test_cases.md (v1.2)
file_implementasi_target:
  - logic/pengguna.py
  - middleware/auth_jwt.py
  - logic/safety_validator.py
  - db/pengguna_repository.py
---

# Issue 0107 — Unit Test: Feature Registrasi Akun Pengguna dengan Enkripsi bcrypt

---

## 🎭 Persona AI Pelaksana

Kamu adalah seorang **Principal QA Engineer & Python Unit Test Specialist** yang berspesialisasi pada pengujian sistem keamanan autentikasi berbasis `bcrypt` dan paradigma **Functional Programming (FP) murni**. Kamu memiliki keahlian mendalam dalam:

- Menulis unit test Python yang deterministik, terisolasi penuh, dan bebas efek samping I/O.
- Merancang skenario pengujian keamanan autentikasi (hashing, password strength, RBAC).
- Menerapkan teknik `unittest.mock` dan `MagicMock` untuk mengisolasi dependensi database.
- Membaca dan menerapkan standar SDLC AbuCom secara ketat tanpa improvisasi yang tidak diperlukan.
- Menulis kode Python 3.14.2+ yang sepenuhnya patuh pada PEP 8, PEP 257, dan PEP 484.

**Otoritasmu** adalah menghasilkan test suite yang **komplit, berjalan hijau (passing), dan bebas fungsi `TODO` atau fungsi menggantung**, serta memastikan coverage logika bisnis target ≥ 90%.

---

## 📚 Dokumen Referensi Utama

Sebelum mengerjakan issue ini, kamu **WAJIB** membaca dan memahami secara menyeluruh dokumen-dokumen berikut. Seluruh keputusan teknis, konvensi penamaan, dan standar kode yang kamu tulis harus berlandaskan dokumen-dokumen ini:

| No | Dokumen | Path | Bab Relevan |
|:---:|---|---|---|
| **1** | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | Bab 14 (Testing Standards), Bab 3 (Naming Conventions), Bab 2 (FP Principles), Bab 10 (Secure Coding) |
| **2** | **Test Plan v1.2** | `docs/sdlc/05_testing/01_test_plan.md` | Bab 3.1 (Unit Testing), Bab 5.1 (bcrypt Testing), Bab 5.4 (Rate Limiting) |
| **3** | **Test Cases v1.2** | `docs/sdlc/05_testing/02_test_cases.md` | Bab 10 (Modul M.7 — Keamanan & Audit Trail) |

> **PENTING:** `narasi.txt` tidak dibutuhkan untuk pengerjaan issue ini. Cukup gunakan tiga dokumen di atas sebagai fondasi pengerjaan.

---

## 🎯 Tujuan Issue

Membuat **test suite unit test otomatis** yang menguji secara menyeluruh seluruh fungsi logika bisnis pada fitur registrasi akun pengguna baru dengan enkripsi `bcrypt` Cost Factor 12. Test suite ini mencakup empat modul implementasi yang sudah ada, yaitu:

| Modul | File | Fungsi yang Diuji |
|---|---|---|
| **Business Logic** | `logic/pengguna.py` | `validasi_role()`, `validasi_nama_lengkap()`, `validasi_username()`, `registrasi_pengguna()` |
| **Security Middleware** | `middleware/auth_jwt.py` | `hash_password()`, `verify_password()` |
| **Input Validator** | `logic/safety_validator.py` | `validasi_kekuatan_sandi()`, `sanitasi_input_cli()` |
| **Data Access Layer** | `db/pengguna_repository.py` | `cek_username_unik()`, `insert_pengguna()` |

---

## 🗂️ Ekstraksi & Ringkasan Detail Data dari Dokumen Referensi

Sebelum menulis kode apapun, ekstrak dan rangkum semua detail teknis berikut dari dokumen referensi:

### A. Dari `docs/sdlc/04_implementation/01_coding_standard.md`

- **[WAJIB]** Unit test **HARUS** menggunakan `unittest` (modul standar Python) atau `pytest` (Bab 14.1).
- **[WAJIB]** Berkas test file **HARUS** dinamai `test_<modul_target>.py` (Bab 14.3). Target file untuk issue ini: `test_unit_registrasi_pengguna.py`.
- **[WAJIB]** Fungsi test **HARUS** dinamai `test_<behavior_spesifik>()` dengan format `snake_case` — contoh: `test_hash_password_menghasilkan_prefix_bcrypt_valid()` (Bab 14.3 & Bab 3.2).
- **[WAJIB]** Unit test pure functions **DILARANG** melakukan koneksi fisik database MySQL atau file system (Bab 14.4). Seluruh dependensi DB di-mock menggunakan `unittest.mock.MagicMock`.
- **[WAJIB]** Target code coverage logika bisnis inti ≥ **90%** (Bab 14.2).
- **[WAJIB]** Header file modul `.py` wajib mengikuti template PEP 257 (Bab 6.4).
- **[WAJIB]** Setiap fungsi test publik wajib dilengkapi docstring singkat yang menjelaskan behavior yang diuji (Bab 6.1).
- **[WAJIB]** Import diurutkan: Standard Library → Third-Party → Local Modules (Bab 5.4.1).
- **[WAJIB]** Indentasi 4 spasi, batas baris maks 120 karakter (Bab 5.2, 5.3).
- **[WAJIB]** Gunakan single quote (`'`) untuk string internal kode (Bab 5.5).
- **[DILARANG]** Wildcard import `from module import *` (Bab 5.4.2).
- **[DILARANG]** Menggunakan `class` atau OOP di logika bisnis utama; test boleh menggunakan `unittest.TestCase` (Bab 2.2.3).
- **Konstanta keamanan yang harus diverifikasi:** `BCRYPT_COST_FACTOR = 12` (Bab 10.2).
- **Enkripsi sandi:** `bcrypt.gensalt(rounds=12)` + `bcrypt.hashpw(...)` → decode ke `str` UTF-8 (Bab 10.2).
- **Verifikasi sandi:** `bcrypt.checkpw(...)` (Bab 10.2).
- **Pola Result NamedTuple:** `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])` wajib dikembalikan oleh semua fungsi bisnis (Bab 8.7).
- **Katalog Error Code** yang relevan untuk issue ini (Bab 11.5):
  - `ERR-VAL-001`: Sandi lemah / tidak memenuhi kriteria.
  - `ERR-VAL-002`: Role tidak valid / tidak terdaftar di RBAC.
  - `ERR-VAL-003`: Nama lengkap kosong atau terlalu panjang.
  - `ERR-VAL-004`: Username kosong, terlalu panjang, atau format salah.
  - `ERR-VAL-005`: Konfirmasi password tidak cocok.
  - `ERR-DB-002`: Pelanggaran integritas DB (username duplikat / insert gagal).

### B. Dari `docs/sdlc/05_testing/01_test_plan.md`

- **Unit Testing** ditargetkan pada **pure functions** di folder `logic/` (Bab 3.1.1).
- Pendekatan pengujian pure functions: **data disuplai via mock NamedTuples/structures** (Bab 3.1.1).
- **White-Box Testing** digunakan untuk unit test: memverifikasi jalur logika internal, exception handling, dan coverage (Bab 3.3).
- **Skenario bcrypt spesifik dari Test Plan (Bab 5.1):**
  - Lakukan registrasi akun baru, verifikasi string hash diawali prefix `$2b$12$...`.
  - Password polos asli **sama sekali tidak boleh terbaca** (tidak disimpan polos).
  - Dua pemanggilan `hash_password()` dengan password yang sama **harus menghasilkan hash yang berbeda** (salt dinamis).
- **Skenario Rate Limiting** (Bab 5.4) — relevan untuk pengujian field `locked_until` & `failed_login_attempts` di `insert_pengguna()`:
  - Field `failed_login_attempts` harus diinisialisasi ke `0` saat registrasi baru.
  - Field `locked_until` harus `NULL` saat registrasi baru.
- **Risiko testing yang harus dimitigasi (Bab 2.4):** Data mock/fixture wajib representatif dan deterministik.

### C. Dari `docs/sdlc/05_testing/02_test_cases.md`

- **Skenario M7-TC-001** (Bab 10.1): Verifikasi login bcrypt cost factor 12 → referensi untuk `hash_password()` dan `verify_password()`.
- **Format fixture test global (Bab 3.3):** Password standar staf `'SandiStaf2026!'` memenuhi semua kriteria kekuatan sandi.
- **8 Peran RBAC valid** (Bab 3.3): `pemilik`, `kepala_percetakan`, `pramuniaga`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang`.

---

## 📐 Batasan, Cakupan, dan Alur Pengerjaan

### Batasan (Constraints)
- **HANYA** menulis kode test. Jangan modifikasi file implementasi (`logic/pengguna.py`, `middleware/auth_jwt.py`, dll.) kecuali ada bug yang eksplisit ditemukan dan wajib dilaporkan sebagai komentar `# FIXME:`.
- **HANYA** menguji fungsi-fungsi yang terdaftar di tabel "Fungsi yang Diuji" di atas.
- **TIDAK** boleh melakukan koneksi jaringan, baca/tulis file, atau akses database nyata.
- **TIDAK** boleh mengubah file lain di luar target output.

### Cakupan (Scope)
- **In-Scope:** `hash_password()`, `verify_password()`, `validasi_kekuatan_sandi()`, `sanitasi_input_cli()`, `validasi_role()`, `validasi_nama_lengkap()`, `validasi_username()`, `cek_username_unik()`, `insert_pengguna()`, `registrasi_pengguna()`.
- **Out-of-Scope:** `create_jwt_session()`, `verify_jwt_session()` (bertanda `TODO` di implementasi — tidak boleh diuji fungsi yang belum diimplementasi).

### Alur Pengerjaan
1. Baca semua dokumen referensi yang disebutkan.
2. Baca semua file implementasi target untuk memahami kontrak fungsi.
3. Siapkan struktur direktori dan file test.
4. Tulis seluruh skenario test dari kelas per kelas.
5. Pastikan semua test bisa dijalankan dan passing.
6. Verifikasi coverage target ≥ 90%.

---

## 🛡️ Isolasi & Mocking

**[WAJIB]** Test suite ini **HARUS** sepenuhnya terisolasi dari database fisik dan sistem eksternal. Gunakan strategi berikut:

- **`unittest.mock.MagicMock`**: Untuk mensimulasikan objek koneksi database (`db_conn`), cursor, dan return value-nya.
- **`unittest.mock.patch`**: Untuk menggantikan fungsi yang memiliki side effects (koneksi DB, hashing bcrypt pada skenario tertentu).
- **Immutable `namedtuple`**: Untuk membuat mock data fixture yang deterministik dan tidak dapat dimutasi selama test berjalan.
- **Contoh pola mock yang sudah ada di codebase** (`tests/test_registrasi_pengguna.py`):
  ```python
  from unittest.mock import MagicMock, patch
  mock_conn = MagicMock()
  mock_cursor = MagicMock()
  mock_cursor.fetchone.return_value = {'jumlah': 0}
  mock_conn.cursor.return_value = mock_cursor
  ```
- **PENTING:** Setiap fungsi test yang memerlukan `mock_conn` **HARUS** membuat instance `MagicMock()` baru di dalam fungsi tersebut (bukan menggunakan shared state antar test) untuk menjamin clean state.

---

## ✅ Kualitas & Kelengkapan Pengerjaan

**[WAJIB]** Pengerjaan dinyatakan **SELESAI** hanya jika seluruh kondisi berikut terpenuhi:

- [ ] **Tidak ada fungsi test dengan body `pass`, `raise NotImplementedError`, atau komentar `# TODO`.**
- [ ] Setiap fungsi test memiliki **minimal 1 assertion** yang bermakna (`assertEqual`, `assertTrue`, `assertFalse`, `assertIn`, `assertIsNone`, `assertIsInstance`, `assertRaises`, `assertNotEqual`).
- [ ] Semua 10 fungsi implementasi target tercakup oleh minimal 1 test positif.
- [ ] Semua skenario negatif / error path tercakup.
- [ ] File test dapat dijalankan dengan `python -m pytest tests/unit/logic/test_unit_registrasi_pengguna.py -v` **tanpa error apapun**.
- [ ] **Code coverage** untuk modul target ≥ 90% (verifikasi dengan `coverage run -m pytest tests/unit/logic/test_unit_registrasi_pengguna.py && coverage report`).

---

## 📁 Folder Penyimpanan & Konvensi Penamaan

### Lokasi File Test
```
abucom/
└── tests/
    └── unit/
        └── logic/
            └── test_unit_registrasi_pengguna.py  ← TARGET OUTPUT FILE INI
```

### Konvensi Penamaan (wajib diikuti secara ketat)
- **Nama file:** `test_unit_registrasi_pengguna.py` (sesuai Coding Standard Bab 14.3).
- **Nama kelas test:** `PascalCase` dimulai dengan `Test` → contoh: `TestHashPassword`, `TestValidasiKekuatanSandi`.
- **Nama fungsi test:** `snake_case` dimulai dengan `test_` diikuti deskripsi behavior spesifik → contoh: `test_hash_password_menghasilkan_prefix_bcrypt_valid()`.
- **Nama variabel mock:** `snake_case` deskriptif → `mock_conn`, `mock_cursor`, `mock_hash_fn`.
- **Nama konstanta test fixture:** `UPPER_SNAKE_CASE` → `PASSWORD_VALID`, `USERNAME_VALID`, `ROLE_KASIR`.

---

## 🧪 Skenario Test Lengkap

> **[ATURAN CLEAN STATE]** Setiap fungsi test WAJIB menginisialisasi ulang seluruh data fixture, mock object, dan variabel lokal yang dibutuhkan DI DALAM body fungsi tersebut. Dilarang menggunakan variabel test fixture yang dibagi antar test (shared state) tanpa mekanisme reset eksplisit di `setUp()`.

---

### 📦 KELAS 1: `TestHashPassword`
**Target:** `middleware/auth_jwt.py` → fungsi `hash_password()`

#### Skenario 1.1 — Positif: Format Prefix bcrypt Valid
- **ID:** `test_hash_password_menghasilkan_prefix_bcrypt_valid`
- **Clean State:** Import ulang fungsi, buat password baru.
- **Langkah:**
  - [ ] Import `hash_password` dari `middleware.auth_jwt`.
  - [ ] Panggil `hash_password('SandiKuat123!')`.
  - [ ] Simpan hasilnya ke variabel `result`.
- **Assertion:**
  - [ ] `self.assertTrue(result.startswith('$2b$12$'))` — membuktikan bcrypt cost factor 12 terpakai.

#### Skenario 1.2 — Positif: Salt Dinamis (Dua Hash Berbeda untuk Password Sama)
- **ID:** `test_hash_password_salt_dinamis_menghasilkan_hash_berbeda`
- **Clean State:** Import ulang, siapkan satu password string.
- **Langkah:**
  - [ ] Panggil `hash_password('SamePass123!')` dua kali berturut-turut.
  - [ ] Simpan ke `hash1` dan `hash2`.
- **Assertion:**
  - [ ] `self.assertNotEqual(hash1, hash2)` — membuktikan salt dinamis, bukan hash deterministik.

#### Skenario 1.3 — Positif: Tipe Data Return adalah String
- **ID:** `test_hash_password_mengembalikan_tipe_string`
- **Langkah:**
  - [ ] Panggil `hash_password('TestPassword123!')`.
- **Assertion:**
  - [ ] `self.assertIsInstance(result, str)` — memastikan output bukan `bytes`.

#### Skenario 1.4 — Positif: Panjang Hash bcrypt Tepat 60 Karakter
- **ID:** `test_hash_password_panjang_hash_tepat_60_karakter`
- **Langkah:**
  - [ ] Panggil `hash_password('TestPassword123!')`.
- **Assertion:**
  - [ ] `self.assertEqual(len(result), 60)`.

#### Skenario 1.5 — Negatif/Edge Case: Password Sangat Panjang (72+ Karakter)
- **ID:** `test_hash_password_password_sangat_panjang_tetap_berhasil`
- **Referensi:** bcrypt memotong input di 72 byte — fungsi tetap harus berhasil (tidak crash).
- **Langkah:**
  - [ ] Buat `long_password = 'A' * 72 + 'b1!'` (lebih dari 72 karakter).
  - [ ] Panggil `hash_password(long_password)`.
- **Assertion:**
  - [ ] `self.assertTrue(result.startswith('$2b$12$'))` — fungsi tidak crash, menghasilkan hash valid.

#### Skenario 1.6 — Negatif/Edge Case: Password String Kosong
- **ID:** `test_hash_password_password_kosong_tetap_menghasilkan_hash`
- **Catatan:** `hash_password('')` secara teknis menghasilkan hash — ini adalah perilaku bcrypt yang valid. Validasi kekosongan ada di layer `validasi_kekuatan_sandi()`, bukan di `hash_password()`.
- **Langkah:**
  - [ ] Panggil `hash_password('')`.
- **Assertion:**
  - [ ] `self.assertIsInstance(result, str)` — fungsi tidak crash.
  - [ ] `self.assertTrue(result.startswith('$2b$'))` — menghasilkan hash bcrypt valid.

---

### 📦 KELAS 2: `TestVerifyPassword`
**Target:** `middleware/auth_jwt.py` → fungsi `verify_password()`

#### Skenario 2.1 — Positif: Password Benar Terverifikasi (True)
- **ID:** `test_verify_password_password_benar_mengembalikan_true`
- **Clean State:** Generate hash baru di dalam test.
- **Langkah:**
  - [ ] Import `hash_password` dan `verify_password`.
  - [ ] Generate `hashed = hash_password('PasswordBenar123!')`.
  - [ ] Panggil `result = verify_password('PasswordBenar123!', hashed)`.
- **Assertion:**
  - [ ] `self.assertTrue(result)`.

#### Skenario 2.2 — Negatif: Password Salah Ditolak (False)
- **ID:** `test_verify_password_password_salah_mengembalikan_false`
- **Langkah:**
  - [ ] Generate `hashed = hash_password('PasswordBenar123!')`.
  - [ ] Panggil `verify_password('PasswordSalah456!', hashed)`.
- **Assertion:**
  - [ ] `self.assertFalse(result)`.

#### Skenario 2.3 — Negatif: Password Kosong vs Hash Valid
- **ID:** `test_verify_password_password_kosong_mengembalikan_false`
- **Langkah:**
  - [ ] Generate `hashed = hash_password('PasswordBenar123!')`.
  - [ ] Panggil `verify_password('', hashed)`.
- **Assertion:**
  - [ ] `self.assertFalse(result)`.

#### Skenario 2.4 — Negatif/Edge Case: Uppercase vs Lowercase (Case Sensitive)
- **ID:** `test_verify_password_case_sensitive_mengembalikan_false`
- **Langkah:**
  - [ ] Generate `hashed = hash_password('SandiKuat123!')`.
  - [ ] Panggil `verify_password('sandikuat123!', hashed)` (all lowercase).
- **Assertion:**
  - [ ] `self.assertFalse(result)` — bcrypt bersifat case-sensitive.

#### Skenario 2.5 — Validasi Input: Password dengan Karakter Unicode
- **ID:** `test_verify_password_password_unicode_diverifikasi_benar`
- **Langkah:**
  - [ ] Buat `password_unicode = 'Sandi123!™'` (mengandung karakter non-ASCII).
  - [ ] Generate `hashed = hash_password(password_unicode)`.
  - [ ] Panggil `verify_password(password_unicode, hashed)`.
- **Assertion:**
  - [ ] `self.assertTrue(result)`.

---

### 📦 KELAS 3: `TestValidasiKekuatanSandi`
**Target:** `logic/safety_validator.py` → fungsi `validasi_kekuatan_sandi()`

#### Skenario 3.1 — Positif: Password Kuat Memenuhi 5 Kriteria
- **ID:** `test_validasi_sandi_password_kuat_lolos_semua_kriteria`
- **Langkah:**
  - [ ] Import `validasi_kekuatan_sandi` dari `logic.safety_validator`.
  - [ ] Panggil `validasi_kekuatan_sandi('SandiKuat123!')`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_valid)`.
  - [ ] `self.assertIsNone(result.error_msg)`.
  - [ ] `self.assertEqual(result.sanitized_data, 'SandiKuat123!')`.

#### Skenario 3.2 — Negatif: Password Terlalu Pendek (< 8 Karakter)
- **ID:** `test_validasi_sandi_password_terlalu_pendek_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_kekuatan_sandi('Ab1!')` (4 karakter).
- **Assertion:**
  - [ ] `self.assertFalse(result.is_valid)`.
  - [ ] `self.assertIn('ERR-VAL-001', result.error_msg)`.
  - [ ] `self.assertIn('8 karakter', result.error_msg)`.

#### Skenario 3.3 — Negatif: Password Tanpa Huruf Besar
- **ID:** `test_validasi_sandi_tanpa_huruf_besar_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_kekuatan_sandi('sandikuat123!')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_valid)`.
  - [ ] `self.assertIn('huruf besar', result.error_msg)`.

#### Skenario 3.4 — Negatif: Password Tanpa Huruf Kecil
- **ID:** `test_validasi_sandi_tanpa_huruf_kecil_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_kekuatan_sandi('SANDIKUAT123!')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_valid)`.
  - [ ] `self.assertIn('huruf kecil', result.error_msg)`.

#### Skenario 3.5 — Negatif: Password Tanpa Angka
- **ID:** `test_validasi_sandi_tanpa_angka_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_kekuatan_sandi('SandiKuat!!!')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_valid)`.
  - [ ] `self.assertIn('angka', result.error_msg)`.

#### Skenario 3.6 — Negatif: Password Tanpa Karakter Spesial
- **ID:** `test_validasi_sandi_tanpa_karakter_spesial_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_kekuatan_sandi('SandiKuat123')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_valid)`.
  - [ ] `self.assertIn('karakter spesial', result.error_msg)`.

#### Skenario 3.7 — Edge Case: Password Tepat 8 Karakter (Batas Minimum Valid)
- **ID:** `test_validasi_sandi_tepat_8_karakter_lolos_batas_minimum`
- **Langkah:**
  - [ ] Panggil `validasi_kekuatan_sandi('Sd123!aB')` (tepat 8 karakter, memenuhi semua kriteria).
- **Assertion:**
  - [ ] `self.assertTrue(result.is_valid)`.

#### Skenario 3.8 — Edge Case: Password Tepat 7 Karakter (Batas Minimum Gagal)
- **ID:** `test_validasi_sandi_7_karakter_gagal_batas_minimum`
- **Langkah:**
  - [ ] Panggil `validasi_kekuatan_sandi('Sd12!aB')` (7 karakter).
- **Assertion:**
  - [ ] `self.assertFalse(result.is_valid)`.
  - [ ] `self.assertIn('ERR-VAL-001', result.error_msg)`.

#### Skenario 3.9 — Negatif: Password Hanya Angka
- **ID:** `test_validasi_sandi_hanya_angka_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_kekuatan_sandi('12345678')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_valid)`.
  - [ ] `self.assertIn('ERR-VAL-001', result.error_msg)`.

#### Skenario 3.10 — Negatif: Password Kosong String
- **ID:** `test_validasi_sandi_password_kosong_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_kekuatan_sandi('')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_valid)`.
  - [ ] `self.assertIn('ERR-VAL-001', result.error_msg)`.

---

### 📦 KELAS 4: `TestSantasiInputCli`
**Target:** `logic/safety_validator.py` → fungsi `sanitasi_input_cli()`

#### Skenario 4.1 — Positif: Input Normal Tanpa Karakter Kontrol
- **ID:** `test_sanitasi_input_cli_input_normal_tidak_berubah`
- **Langkah:**
  - [ ] Import `sanitasi_input_cli` dari `logic.safety_validator`.
  - [ ] Panggil `sanitasi_input_cli('Budi Santoso')`.
- **Assertion:**
  - [ ] `self.assertEqual(result, 'Budi Santoso')`.

#### Skenario 4.2 — Negatif: Karakter ANSI Escape Code Dihapus
- **ID:** `test_sanitasi_input_cli_ansi_escape_code_dihapus`
- **Referensi:** Coding Standard Bab 10.5 — buang karakter di bawah `\x20`.
- **Langkah:**
  - [ ] Panggil `sanitasi_input_cli('\x1b[31mBarang Palsu')`.
- **Assertion:**
  - [ ] `self.assertEqual(result, '[31mBarang Palsu')` — karakter `\x1b` (ESC) terbuang, karakter `[`, `3`, `1`, `m` yang nilainya ≥ 0x20 tetap ada.

#### Skenario 4.3 — Negatif: Karakter Kontrol Null dan Bell Dihapus
- **ID:** `test_sanitasi_input_cli_karakter_kontrol_null_dihapus`
- **Langkah:**
  - [ ] Panggil `sanitasi_input_cli('Nama\x00Barang\x07Test')` (`\x00` = NULL, `\x07` = BEL).
- **Assertion:**
  - [ ] `self.assertEqual(result, 'NamaBarangTest')`.

#### Skenario 4.4 — Edge Case: String Kosong Tetap Kosong
- **ID:** `test_sanitasi_input_cli_string_kosong_tetap_kosong`
- **Langkah:**
  - [ ] Panggil `sanitasi_input_cli('')`.
- **Assertion:**
  - [ ] `self.assertEqual(result, '')`.

#### Skenario 4.5 — Edge Case: Input Hanya Karakter Kontrol Menghasilkan String Kosong
- **ID:** `test_sanitasi_input_cli_semua_karakter_kontrol_menghasilkan_string_kosong`
- **Langkah:**
  - [ ] Panggil `sanitasi_input_cli('\x00\x01\x1b\x1f')`.
- **Assertion:**
  - [ ] `self.assertEqual(result, '')`.

---

### 📦 KELAS 5: `TestValidasiRole`
**Target:** `logic/pengguna.py` → fungsi `validasi_role()`

#### Skenario 5.1 — Positif: Role 'kasir' Valid
- **ID:** `test_validasi_role_kasir_diterima_sebagai_valid`
- **Langkah:**
  - [ ] Import `validasi_role` dari `logic.pengguna`.
  - [ ] Panggil `validasi_role('kasir')`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertEqual(result.data, 'kasir')`.
  - [ ] `self.assertIsNone(result.error_msg)`.

#### Skenario 5.2 — Positif: Role Case-Insensitive ('PEMILIK' → 'pemilik')
- **ID:** `test_validasi_role_uppercase_dinormalisasi_ke_lowercase`
- **Langkah:**
  - [ ] Panggil `validasi_role('PEMILIK')`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertEqual(result.data, 'pemilik')`.

#### Skenario 5.3 — Positif: Seluruh 8 Role RBAC Valid Diterima
- **ID:** `test_validasi_role_semua_8_role_rbac_valid_diterima`
- **Langkah:**
  - [ ] Import `VALID_ROLES` dari `logic.pengguna`.
  - [ ] Loop setiap role dalam `VALID_ROLES`, panggil `validasi_role(role)` untuk masing-masing.
- **Assertion (di dalam loop):**
  - [ ] `self.assertTrue(result.is_success, f'Role {role} seharusnya diterima sebagai valid')`.

#### Skenario 5.4 — Negatif: Role Tidak Terdaftar Ditolak
- **ID:** `test_validasi_role_tidak_terdaftar_ditolak_dengan_error_code`
- **Langkah:**
  - [ ] Panggil `validasi_role('admin_palsu')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-002', result.error_msg)`.
  - [ ] `self.assertIsNone(result.data)`.

#### Skenario 5.5 — Negatif: Role String Kosong Ditolak
- **ID:** `test_validasi_role_string_kosong_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_role('')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-002', result.error_msg)`.

#### Skenario 5.6 — Negatif: Role dengan Spasi Extra Dinormalisasi
- **ID:** `test_validasi_role_dengan_spasi_leading_trailing_dinormalisasi`
- **Langkah:**
  - [ ] Panggil `validasi_role('  kasir  ')`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertEqual(result.data, 'kasir')`.

---

### 📦 KELAS 6: `TestValidasiNamaLengkap`
**Target:** `logic/pengguna.py` → fungsi `validasi_nama_lengkap()`

#### Skenario 6.1 — Positif: Nama Lengkap Valid Diterima
- **ID:** `test_validasi_nama_lengkap_nama_valid_diterima`
- **Langkah:**
  - [ ] Import `validasi_nama_lengkap` dari `logic.pengguna`.
  - [ ] Panggil `validasi_nama_lengkap('Budi Santoso')`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertEqual(result.data, 'Budi Santoso')`.

#### Skenario 6.2 — Negatif: Nama Kosong (Hanya Whitespace) Ditolak
- **ID:** `test_validasi_nama_lengkap_nama_kosong_ditolak_dengan_error_val_003`
- **Langkah:**
  - [ ] Panggil `validasi_nama_lengkap('   ')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-003', result.error_msg)`.

#### Skenario 6.3 — Negatif: Nama Terlalu Panjang (> 100 Karakter) Ditolak
- **ID:** `test_validasi_nama_lengkap_nama_melebihi_100_karakter_ditolak`
- **Langkah:**
  - [ ] Buat `nama_panjang = 'A' * 101`.
  - [ ] Panggil `validasi_nama_lengkap(nama_panjang)`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-003', result.error_msg)`.

#### Skenario 6.4 — Edge Case: Nama Tepat 100 Karakter (Batas Maksimum Valid)
- **ID:** `test_validasi_nama_lengkap_tepat_100_karakter_diterima`
- **Langkah:**
  - [ ] Buat `nama_100 = 'A' * 100`.
  - [ ] Panggil `validasi_nama_lengkap(nama_100)`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.

#### Skenario 6.5 — Edge Case: Nama Tepat 101 Karakter (Batas Maksimum Gagal)
- **ID:** `test_validasi_nama_lengkap_101_karakter_ditolak`
- **Langkah:**
  - [ ] Buat `nama_101 = 'A' * 101`.
  - [ ] Panggil `validasi_nama_lengkap(nama_101)`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.

#### Skenario 6.6 — Edge Case: Nama dengan Whitespace Awal/Akhir Di-strip
- **ID:** `test_validasi_nama_lengkap_whitespace_di_strip`
- **Langkah:**
  - [ ] Panggil `validasi_nama_lengkap('  Budi Santoso  ')`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertEqual(result.data, 'Budi Santoso')` — whitespace di-strip.

---

### 📦 KELAS 7: `TestValidasiUsername`
**Target:** `logic/pengguna.py` → fungsi `validasi_username()`

#### Skenario 7.1 — Positif: Username Valid dengan Underscore Diterima
- **ID:** `test_validasi_username_format_valid_dengan_underscore_diterima`
- **Langkah:**
  - [ ] Import `validasi_username` dari `logic.pengguna`.
  - [ ] Panggil `validasi_username('kasir_02')`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertEqual(result.data, 'kasir_02')`.

#### Skenario 7.2 — Positif: Username Uppercase Dinormalisasi ke Lowercase
- **ID:** `test_validasi_username_uppercase_dinormalisasi_ke_lowercase`
- **Langkah:**
  - [ ] Panggil `validasi_username('Kasir_02')`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertEqual(result.data, 'kasir_02')`.

#### Skenario 7.3 — Negatif: Username Kosong Ditolak
- **ID:** `test_validasi_username_username_kosong_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_username('')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-004', result.error_msg)`.

#### Skenario 7.4 — Negatif: Username dengan Karakter Spesial (`@`) Ditolak
- **ID:** `test_validasi_username_karakter_spesial_at_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_username('kasir@02')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-004', result.error_msg)`.

#### Skenario 7.5 — Negatif: Username dengan Spasi Ditolak
- **ID:** `test_validasi_username_dengan_spasi_ditolak`
- **Langkah:**
  - [ ] Panggil `validasi_username('kasir 02')`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-004', result.error_msg)`.

#### Skenario 7.6 — Negatif: Username Terlalu Panjang (> 50 Karakter) Ditolak
- **ID:** `test_validasi_username_melebihi_50_karakter_ditolak`
- **Langkah:**
  - [ ] Buat `username_panjang = 'a' * 51`.
  - [ ] Panggil `validasi_username(username_panjang)`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-004', result.error_msg)`.

#### Skenario 7.7 — Edge Case: Username Tepat 50 Karakter Diterima
- **ID:** `test_validasi_username_tepat_50_karakter_diterima`
- **Langkah:**
  - [ ] Buat `username_50 = 'a' * 50`.
  - [ ] Panggil `validasi_username(username_50)`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.

#### Skenario 7.8 — Validasi Input: Username Hanya Angka Diterima (Format Valid)
- **ID:** `test_validasi_username_hanya_angka_diterima`
- **Langkah:**
  - [ ] Panggil `validasi_username('12345')`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertEqual(result.data, '12345')`.

---

### 📦 KELAS 8: `TestCekUsernameUnik`
**Target:** `db/pengguna_repository.py` → fungsi `cek_username_unik()`

> **[ATURAN MOCK]** Seluruh test di kelas ini WAJIB menggunakan `MagicMock` untuk objek `db_conn`. DILARANG menggunakan koneksi database nyata.

#### Skenario 8.1 — Positif: Username Belum Terdaftar (Unik) → Sukses
- **ID:** `test_cek_username_unik_username_belum_ada_mengembalikan_sukses`
- **Clean State:** Buat `mock_conn` dan `mock_cursor` baru di dalam fungsi.
- **Langkah:**
  - [ ] Import `cek_username_unik` dari `db.pengguna_repository`.
  - [ ] Buat `mock_conn = MagicMock()`.
  - [ ] Buat `mock_cursor = MagicMock()`.
  - [ ] Set `mock_cursor.fetchone.return_value = {'jumlah': 0}` (username belum ada).
  - [ ] Set `mock_conn.cursor.return_value = mock_cursor`.
  - [ ] Panggil `result = cek_username_unik('user_baru', mock_conn)`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertIsNone(result.error_msg)`.
  - [ ] `mock_conn.cursor.assert_called_once_with(dictionary=True)` — memastikan cursor dibuat dengan benar.
  - [ ] `mock_cursor.execute.assert_called_once()` — memastikan query dijalankan.
  - [ ] `mock_cursor.close.assert_called_once()` — memastikan cursor ditutup.

#### Skenario 8.2 — Negatif: Username Sudah Terdaftar (Duplikat) → Gagal
- **ID:** `test_cek_username_unik_username_duplikat_mengembalikan_gagal`
- **Clean State:** Buat mock baru.
- **Langkah:**
  - [ ] Set `mock_cursor.fetchone.return_value = {'jumlah': 1}` (username sudah ada).
  - [ ] Panggil `cek_username_unik('user_duplikat', mock_conn)`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-DB-002', result.error_msg)`.
  - [ ] `self.assertIsNone(result.data)`.

#### Skenario 8.3 — Negatif: Exception Database → Gagal Aman
- **ID:** `test_cek_username_unik_exception_database_ditangani_dengan_aman`
- **Langkah:**
  - [ ] Set `mock_conn.cursor.side_effect = Exception('Database connection lost')`.
  - [ ] Panggil `cek_username_unik('user_error', mock_conn)`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-DB-002', result.error_msg)`.

#### Skenario 8.4 — Validasi Input: Verifikasi Query Menggunakan Parameterized Query (bukan f-string)
- **ID:** `test_cek_username_unik_query_menggunakan_parameterized_query`
- **Referensi:** Coding Standard Bab 9.1 — wajib menggunakan placeholder `%s`.
- **Langkah:**
  - [ ] Set `mock_cursor.fetchone.return_value = {'jumlah': 0}`.
  - [ ] Panggil `cek_username_unik('test_user', mock_conn)`.
  - [ ] Ambil argumen pemanggilan `mock_cursor.execute.call_args`.
- **Assertion:**
  - [ ] `self.assertIn('%s', call_args[0][0])` — query string mengandung placeholder `%s`.
  - [ ] `self.assertEqual(call_args[0][1], ('test_user',))` — username dilewatkan sebagai tuple terpisah.

---

### 📦 KELAS 9: `TestInsertPengguna`
**Target:** `db/pengguna_repository.py` → fungsi `insert_pengguna()`

> **[ATURAN MOCK]** Gunakan `MagicMock` untuk semua interaksi database.

#### Skenario 9.1 — Positif: Insert Berhasil Mengembalikan ID Baru
- **ID:** `test_insert_pengguna_berhasil_mengembalikan_id_pengguna_baru`
- **Clean State:** Buat mock baru, set `lastrowid`.
- **Langkah:**
  - [ ] Import `insert_pengguna` dari `db.pengguna_repository`.
  - [ ] Buat `mock_conn = MagicMock()` dan `mock_cursor = MagicMock()`.
  - [ ] Set `mock_cursor.lastrowid = 42`.
  - [ ] Set `mock_conn.cursor.return_value = mock_cursor`.
  - [ ] Panggil `result = insert_pengguna('Budi Santoso', 'budi_01', '$2b$12$hash...', 'kasir', 1, mock_conn)`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertEqual(result.data, 42)` — ID pengguna baru.
  - [ ] `self.assertIsNone(result.error_msg)`.
  - [ ] `mock_conn.start_transaction.assert_called_once()` — transaksi ACID dimulai.
  - [ ] `mock_conn.commit.assert_called_once()` — transaksi di-commit.
  - [ ] `mock_cursor.close.assert_called_once()` — cursor ditutup.

#### Skenario 9.2 — Negatif: Exception saat Execute → Rollback Dipanggil
- **ID:** `test_insert_pengguna_exception_memicu_rollback_dan_gagal`
- **Langkah:**
  - [ ] Set `mock_cursor.execute.side_effect = Exception('Insert DB error')`.
  - [ ] Panggil `insert_pengguna('Budi', 'budi_01', 'hash', 'kasir', 1, mock_conn)`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-DB-002', result.error_msg)`.
  - [ ] `mock_conn.rollback.assert_called_once()` — rollback dipanggil untuk menjaga integritas ACID.
  - [ ] `mock_cursor.close.assert_called_once()` — cursor tetap ditutup meski exception.

#### Skenario 9.3 — Validasi Input: Inisialisasi `failed_login_attempts = 0` dan `locked_until = NULL`
- **ID:** `test_insert_pengguna_menginisialisasi_failed_login_dan_locked_until_ke_nilai_aman`
- **Referensi:** Coding Standard Bab 10.2, Test Plan Bab 5.4 — field brute force protection harus diinisialisasi.
- **Langkah:**
  - [ ] Set `mock_cursor.lastrowid = 10`.
  - [ ] Panggil `insert_pengguna('Budi', 'budi_01', 'hash', 'kasir', 1, mock_conn)`.
  - [ ] Ambil argumen `mock_cursor.execute.call_args`.
  - [ ] Ekstrak string SQL query dan tuple parameter dari argumen tersebut.
- **Assertion:**
  - [ ] Verifikasi bahwa string SQL query mengandung `'failed_login_attempts'`.
  - [ ] Verifikasi bahwa string SQL query mengandung `'locked_until'`.

#### Skenario 9.4 — Validasi Input: Query Menggunakan Parameterized Placeholder `%s`
- **ID:** `test_insert_pengguna_query_menggunakan_parameterized_placeholder`
- **Langkah:**
  - [ ] Set `mock_cursor.lastrowid = 5`.
  - [ ] Panggil `insert_pengguna('Sari', 'sari_01', 'bcrypt_hash', 'gudang', 2, mock_conn)`.
  - [ ] Ambil argumen `mock_cursor.execute.call_args`.
- **Assertion:**
  - [ ] `self.assertIn('%s', call_args[0][0])` — query menggunakan placeholder.
  - [ ] `self.assertNotIn('sari_01', call_args[0][0])` — username tidak di-hardcode langsung ke string SQL.

---

### 📦 KELAS 10: `TestRegistrasiPengguna`
**Target:** `logic/pengguna.py` → fungsi `registrasi_pengguna()`

> **[ATURAN MOCK]** Fungsi `cek_username_unik`, `insert_pengguna`, dan `hash_password` **WAJIB di-mock** menggunakan `patch` untuk mengisolasi logika orkestrasi dari dependensi eksternal. Seluruh mock dibuat baru di setiap test.

#### Skenario 10.1 — Positif: Registrasi Lengkap Berhasil End-to-End
- **ID:** `test_registrasi_pengguna_semua_input_valid_mengembalikan_sukses`
- **Clean State:** Buat `mock_conn` baru, buat `mock_cursor` baru.
- **Langkah:**
  - [ ] Import `registrasi_pengguna` dari `logic.pengguna`.
  - [ ] Buat `mock_conn = MagicMock()`, `mock_cursor = MagicMock()`.
  - [ ] Set `mock_conn.cursor.return_value = mock_cursor`.
  - [ ] Gunakan `patch` untuk mock `logic.pengguna.cek_username_unik` → return `Result(True, None, None)`.
  - [ ] Gunakan `patch` untuk mock `logic.pengguna.insert_pengguna` → return `Result(True, 99, None)`.
  - [ ] Gunakan `patch` untuk mock `logic.pengguna.hash_password` → return `'$2b$12$mocked_hash'`.
  - [ ] Panggil `registrasi_pengguna('Budi Santoso', 'budi_01', 'SandiKuat123!', 'SandiKuat123!', 'kasir', 1, mock_conn, 1)`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)`.
  - [ ] `self.assertEqual(result.data, 99)` — ID pengguna baru dari mock insert.
  - [ ] `self.assertIsNone(result.error_msg)`.
  - [ ] Verifikasi `mock_cursor.execute` dipanggil minimal 1x (untuk audit log).
  - [ ] Verifikasi `mock_conn.commit` dipanggil minimal 1x (untuk commit audit log).

#### Skenario 10.2 — Negatif: Nama Lengkap Kosong → Error ERR-VAL-003 (Short-Circuit)
- **ID:** `test_registrasi_pengguna_nama_kosong_ditolak_sebelum_proses_lanjut`
- **Langkah:**
  - [ ] Buat `mock_conn = MagicMock()`.
  - [ ] Panggil `registrasi_pengguna('', 'budi_01', 'SandiKuat123!', 'SandiKuat123!', 'kasir', 1, mock_conn, 1)`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-003', result.error_msg)`.

#### Skenario 10.3 — Negatif: Username Kosong → Error ERR-VAL-004
- **ID:** `test_registrasi_pengguna_username_kosong_ditolak`
- **Langkah:**
  - [ ] Panggil dengan `username=''`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-004', result.error_msg)`.

#### Skenario 10.4 — Negatif: Konfirmasi Password Tidak Cocok → Error ERR-VAL-005
- **ID:** `test_registrasi_pengguna_password_tidak_cocok_ditolak`
- **Langkah:**
  - [ ] Panggil dengan `password='SandiKuat123!'` dan `konfirmasi_password='BerbedaSandi456!'`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-005', result.error_msg)`.

#### Skenario 10.5 — Negatif: Password Lemah → Error ERR-VAL-001
- **ID:** `test_registrasi_pengguna_password_lemah_ditolak`
- **Langkah:**
  - [ ] Panggil dengan `password='lemah'` dan `konfirmasi_password='lemah'`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-001', result.error_msg)`.

#### Skenario 10.6 — Negatif: Role Tidak Valid → Error ERR-VAL-002
- **ID:** `test_registrasi_pengguna_role_tidak_valid_ditolak`
- **Langkah:**
  - [ ] Panggil dengan `role='superadmin'`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-002', result.error_msg)`.

#### Skenario 10.7 — Negatif: Username Sudah Terdaftar (Duplikat) → Error ERR-DB-002
- **ID:** `test_registrasi_pengguna_username_duplikat_ditolak`
- **Langkah:**
  - [ ] Gunakan `patch('logic.pengguna.cek_username_unik')` → return `Result(False, None, 'ERR-DB-002: ...')`.
  - [ ] Panggil `registrasi_pengguna` dengan input valid.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-DB-002', result.error_msg)`.

#### Skenario 10.8 — Negatif: Insert Database Gagal → Error ERR-DB-002
- **ID:** `test_registrasi_pengguna_insert_database_gagal_mengembalikan_error`
- **Langkah:**
  - [ ] Patch `cek_username_unik` → return sukses.
  - [ ] Patch `insert_pengguna` → return `Result(False, None, 'ERR-DB-002: Gagal menyimpan ...')`.
  - [ ] Patch `hash_password` → return `'$2b$12$mocked'`.
  - [ ] Panggil `registrasi_pengguna` dengan input valid.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-DB-002', result.error_msg)`.

#### Skenario 10.9 — Edge Case: Audit Log Gagal TIDAK Membatalkan Registrasi
- **ID:** `test_registrasi_pengguna_kegagalan_audit_log_tidak_membatalkan_registrasi`
- **Referensi:** Alur `registrasi_pengguna()` — exception pada audit log ditangkap dan diabaikan.
- **Langkah:**
  - [ ] Buat `mock_conn = MagicMock()`, `mock_cursor = MagicMock()`.
  - [ ] Set `mock_conn.cursor.return_value = mock_cursor`.
  - [ ] Set `mock_cursor.execute.side_effect = Exception('Audit log DB error')` — simulasi audit log gagal.
  - [ ] Patch `cek_username_unik` → sukses, `insert_pengguna` → `Result(True, 77, None)`, `hash_password` → `'mocked'`.
  - [ ] Panggil `registrasi_pengguna`.
- **Assertion:**
  - [ ] `self.assertTrue(result.is_success)` — registrasi tetap berhasil meski audit log gagal.
  - [ ] `self.assertEqual(result.data, 77)`.

#### Skenario 10.10 — Negatif: Username dengan Format Karakter Spesial Ditolak
- **ID:** `test_registrasi_pengguna_username_format_salah_ditolak`
- **Langkah:**
  - [ ] Panggil dengan `username='budi@01'`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-004', result.error_msg)`.

#### Skenario 10.11 — Negatif: Nama Terlalu Panjang Ditolak
- **ID:** `test_registrasi_pengguna_nama_terlalu_panjang_ditolak`
- **Langkah:**
  - [ ] Buat `nama = 'B' * 101`.
  - [ ] Panggil dengan `nama_lengkap=nama`.
- **Assertion:**
  - [ ] `self.assertFalse(result.is_success)`.
  - [ ] `self.assertIn('ERR-VAL-003', result.error_msg)`.

#### Skenario 10.12 — Positif: Seluruh 8 Role RBAC Valid Dapat Diregistrasikan
- **ID:** `test_registrasi_pengguna_semua_8_role_rbac_dapat_diregistrasikan`
- **Langkah:**
  - [ ] Import `VALID_ROLES` dari `logic.pengguna`.
  - [ ] Loop setiap role, patch semua dependency → sukses.
  - [ ] Panggil `registrasi_pengguna` untuk setiap role.
- **Assertion (dalam loop):**
  - [ ] `self.assertTrue(result.is_success, f'Registrasi dengan role {role} seharusnya berhasil')`.

---

## 🗂️ Struktur File yang Dihasilkan

File test yang dihasilkan harus mengikuti struktur berikut (wajib patuh pada template header PEP 257):

```python
"""
Nama Modul: test_unit_registrasi_pengguna.py
Deskripsi: Unit test suite untuk fitur registrasi akun pengguna dengan enkripsi
           bcrypt. Mencakup validasi input, hashing password, verifikasi password,
           validasi RBAC, operasi database (dengan mocking), dan orkestrasi
           fungsi registrasi pengguna secara end-to-end.
           (Ref: Coding Standard v1.2 Bab 14, Test Plan v1.2 Bab 3.1 & 5.1)
Author   : [Nama Pengembang / AI Asisten]
Tanggal  : [YYYY-MM-DD]
"""

# 1. Standard Library
import unittest
from collections import namedtuple
from unittest.mock import MagicMock, patch

# 2. Tidak ada Third-Party langsung (bcrypt digunakan melalui middleware)

# 3. Local Modules (diimport di dalam setiap fungsi test untuk isolasi)


# ===========================================================================
# KELAS 1: TestHashPassword
# ===========================================================================
class TestHashPassword(unittest.TestCase):
    ...

# ===========================================================================
# KELAS 2: TestVerifyPassword
# ===========================================================================
class TestVerifyPassword(unittest.TestCase):
    ...

# (dan seterusnya hingga KELAS 10)

if __name__ == '__main__':
    unittest.main()
```

---

## 📋 Low-Level Checklist Eksekusi (Step-by-Step untuk AI/Junior Programmer)

### FASE 0: Persiapan & Pembacaan Konteks

- [ ] **0.1** Buka dan baca tuntas `docs/sdlc/04_implementation/01_coding_standard.md` — fokus pada Bab 2, 3, 5, 6, 10, 14.
- [ ] **0.2** Buka dan baca tuntas `docs/sdlc/05_testing/01_test_plan.md` — fokus pada Bab 3.1, 5.1, 5.4.
- [ ] **0.3** Baca `docs/sdlc/05_testing/02_test_cases.md` — fokus pada Bab 10 (M.7).
- [ ] **0.4** Baca file `logic/pengguna.py` — pahami seluruh signature, alur, konstanta `VALID_ROLES`, dan Result pattern.
- [ ] **0.5** Baca file `middleware/auth_jwt.py` — pahami `BCRYPT_COST_FACTOR = 12`, `hash_password()`, `verify_password()`.
- [ ] **0.6** Baca file `logic/safety_validator.py` — pahami 5 kriteria `validasi_kekuatan_sandi()` dan `sanitasi_input_cli()`.
- [ ] **0.7** Baca file `db/pengguna_repository.py` — pahami alur ACID `insert_pengguna()` dan `cek_username_unik()`.
- [ ] **0.8** Baca file `tests/test_registrasi_pengguna.py` yang sudah ada sebagai referensi pola penulisan yang sudah terbukti benar di proyek ini.

### FASE 1: Inisialisasi File Test

- [ ] **1.1** Verifikasi direktori `tests/unit/logic/` sudah ada. Jika belum, buat direktori tersebut.
- [ ] **1.2** Verifikasi file `tests/unit/logic/__init__.py` ada (boleh kosong). Jika belum, buat.
- [ ] **1.3** Buat file baru: `tests/unit/logic/test_unit_registrasi_pengguna.py`.
- [ ] **1.4** Tulis header modul PEP 257 di baris paling atas file (ikuti template pada bagian "Struktur File yang Dihasilkan" di atas).
- [ ] **1.5** Tulis blok import di bawah header: `import unittest`, `from collections import namedtuple`, `from unittest.mock import MagicMock, patch`.
- [ ] **1.6** Tambahkan baris `if __name__ == '__main__': unittest.main()` di bagian paling bawah file.

### FASE 2: Implementasi Test — Kelas per Kelas

- [ ] **2.1** Buat kelas `TestHashPassword(unittest.TestCase)` dengan seluruh 6 skenario (1.1 - 1.6).
  - [ ] **2.1.a** Setiap fungsi test: tambahkan docstring singkat satu baris.
  - [ ] **2.1.b** Import `hash_password` di dalam setiap fungsi test (bukan di level modul) untuk isolasi.
  - [ ] **2.1.c** Jalankan tes parsial: `python -m pytest tests/unit/logic/test_unit_registrasi_pengguna.py::TestHashPassword -v`. Pastikan **SEMUA HIJAU** sebelum lanjut.
- [ ] **2.2** Buat kelas `TestVerifyPassword(unittest.TestCase)` dengan seluruh 5 skenario (2.1 - 2.5).
  - [ ] **2.2.a** Setiap test: generate hash baru di dalam body test (`hashed = hash_password(...)`).
  - [ ] **2.2.b** Jalankan tes parsial kelas ini. Pastikan **SEMUA HIJAU**.
- [ ] **2.3** Buat kelas `TestValidasiKekuatanSandi(unittest.TestCase)` dengan seluruh 10 skenario (3.1 - 3.10).
  - [ ] **2.3.a** Jalankan tes parsial. Pastikan **SEMUA HIJAU**.
- [ ] **2.4** Buat kelas `TestSantasiInputCli(unittest.TestCase)` dengan seluruh 5 skenario (4.1 - 4.5).
  - [ ] **2.4.a** Jalankan tes parsial. Pastikan **SEMUA HIJAU**.
- [ ] **2.5** Buat kelas `TestValidasiRole(unittest.TestCase)` dengan seluruh 6 skenario (5.1 - 5.6).
  - [ ] **2.5.a** Jalankan tes parsial. Pastikan **SEMUA HIJAU**.
- [ ] **2.6** Buat kelas `TestValidasiNamaLengkap(unittest.TestCase)` dengan seluruh 6 skenario (6.1 - 6.6).
  - [ ] **2.6.a** Jalankan tes parsial. Pastikan **SEMUA HIJAU**.
- [ ] **2.7** Buat kelas `TestValidasiUsername(unittest.TestCase)` dengan seluruh 8 skenario (7.1 - 7.8).
  - [ ] **2.7.a** Jalankan tes parsial. Pastikan **SEMUA HIJAU**.
- [ ] **2.8** Buat kelas `TestCekUsernameUnik(unittest.TestCase)` dengan seluruh 4 skenario (8.1 - 8.4).
  - [ ] **2.8.a** Pastikan setiap test membuat `mock_conn = MagicMock()` baru (clean state).
  - [ ] **2.8.b** Jalankan tes parsial. Pastikan **SEMUA HIJAU**.
- [ ] **2.9** Buat kelas `TestInsertPengguna(unittest.TestCase)` dengan seluruh 4 skenario (9.1 - 9.4).
  - [ ] **2.9.a** Pastikan `mock_conn.start_transaction.assert_called_once()` dan `mock_conn.rollback.assert_called_once()` digunakan pada skenario yang tepat.
  - [ ] **2.9.b** Jalankan tes parsial. Pastikan **SEMUA HIJAU**.
- [ ] **2.10** Buat kelas `TestRegistrasiPengguna(unittest.TestCase)` dengan seluruh 12 skenario (10.1 - 10.12).
  - [ ] **2.10.a** Untuk setiap test yang menggunakan `patch`, pastikan context manager `with patch(...) as mock_xxx:` digunakan dengan benar.
  - [ ] **2.10.b** Untuk Skenario 10.12 (loop 8 role), pastikan mock direset di setiap iterasi loop.
  - [ ] **2.10.c** Jalankan tes parsial. Pastikan **SEMUA HIJAU**.

### FASE 3: Verifikasi Final

- [ ] **3.1** Jalankan **SEMUA** test suite sekaligus:
  ```bash
  python -m pytest tests/unit/logic/test_unit_registrasi_pengguna.py -v
  ```
  Pastikan output menampilkan **0 failed, 0 error**. Jumlah test yang lolos harus ≥ 56 test case.

- [ ] **3.2** Jalankan pengukuran code coverage:
  ```bash
  coverage run -m pytest tests/unit/logic/test_unit_registrasi_pengguna.py
  coverage report --include="logic/pengguna.py,middleware/auth_jwt.py,logic/safety_validator.py,db/pengguna_repository.py"
  ```
  Pastikan output `TOTAL` coverage ≥ **90%**.

- [ ] **3.3** Scan seluruh file test yang dihasilkan. Pastikan **TIDAK ADA** baris yang mengandung:
  - `pass` di dalam body fungsi test.
  - `raise NotImplementedError`.
  - Komentar `# TODO:` atau `# FIXME:` yang belum diselesaikan.
  - Import `*` (wildcard import).
  - String SQL yang mengandung variabel langsung (f-string SQL).

- [ ] **3.4** Verifikasi konvensi penamaan:
  - [ ] Nama file: `test_unit_registrasi_pengguna.py` ✓.
  - [ ] Semua nama kelas dimulai dengan `Test` dan menggunakan `PascalCase` ✓.
  - [ ] Semua nama fungsi test dimulai dengan `test_` dan menggunakan `snake_case` ✓.
  - [ ] Semua konstanta test fixture menggunakan `UPPER_SNAKE_CASE` jika ada ✓.

- [ ] **3.5** Verifikasi header modul PEP 257 ada di baris pertama file dan berisi field: Nama Modul, Deskripsi, Author, Tanggal.

- [ ] **3.6** Verifikasi urutan import sudah benar: Standard Library → Third-Party → Local Modules (sesuai Coding Standard Bab 5.4.1).

---

## 🚫 Larangan Mutlak (MUST NOT)

Hal-hal berikut **dilarang keras** dilakukan selama pengerjaan issue ini:

| No | Larangan | Dampak |
|:---:|---|---|
| 1 | Melakukan koneksi database MySQL nyata di dalam test | Test tidak terisolasi, tergantung environment eksternal |
| 2 | Menggunakan wildcard import `from module import *` | Mengotori namespace, melanggar Coding Standard Bab 5.4.2 |
| 3 | Memodifikasi file implementasi (`logic/`, `middleware/`, `db/`) | Scope creep, dapat memecah feature lain |
| 4 | Meninggalkan fungsi test dengan body `pass` atau `NotImplementedError` | Kualitas coverage palsu — melanggar syarat kelengkapan |
| 5 | Menggunakan `float` untuk perbandingan nilai numerik dalam assertion | Potensi floating point precision error |
| 6 | Berbagi variabel mock antar fungsi test tanpa reset eksplisit | Kontaminasi state antar test (flaky test) |
| 7 | Menulis SQL query langsung (tanpa mock) di dalam test | Melanggar prinsip unit test isolated |
| 8 | Menguji fungsi `create_jwt_session()` dan `verify_jwt_session()` | Fungsi bertanda `# TODO` — belum diimplementasi |

---

## 📎 Catatan Tambahan & Kaidah Standar

### Konvensi Khusus Unit Test AbuCom (dari Coding Standard Bab 14)
- **Deterministik:** Input yang sama harus selalu menghasilkan hasil yang sama. Gunakan nilai fixture yang statis, bukan nilai dinamis seperti `datetime.now()` dalam assertion.
- **Terisolasi penuh:** Setiap test harus dapat dijalankan sendiri tanpa bergantung pada urutan eksekusi atau state dari test lain.
- **Cepat:** Unit test tidak boleh lambat. Hindari `time.sleep()` di dalam test.
- **Pola `setUp()` opsional:** Jika ada data fixture yang digunakan di banyak test dalam satu kelas, boleh gunakan `setUp(self)` — namun **wajib** menggunakan `mock_conn = MagicMock()` baru di setiap `setUp()` agar clean state terjaga antar test.

### Konvensi Error Assertion
- Untuk memverifikasi error code, selalu gunakan `self.assertIn('ERR-XXX-YYY', result.error_msg)` — jangan `self.assertEqual(result.error_msg, 'ERR-VAL-001: ...')` karena pesan bisa berubah.
- Selalu verifikasi `result.is_success` (True/False) **sebelum** memeriksa konten `result.data` atau `result.error_msg`.

### Konvensi Import di Dalam Fungsi Test
- Import modul target dilakukan **di dalam setiap fungsi test** (bukan di level modul) untuk:
  1. Memudahkan debugging ketika sebuah import gagal.
  2. Memastikan test tetap berjalan meski modul lain ada error.
  3. Memperjelas dependensi setiap test case secara eksplisit.

### Kaidah Tambahan: Verifikasi Mock Calls
- Selalu verifikasi bahwa mock function dipanggil dengan argumen yang benar menggunakan `assert_called_once_with(...)` atau `assert_called_with(...)` untuk membuktikan kontrak pemanggilan fungsi.
- Untuk verifikasi bahwa suatu mock **tidak dipanggil** (dalam skenario short-circuit), gunakan `mock_fn.assert_not_called()`.

---

*Issue ini dibuat berdasarkan dokumen SDLC AbuCom: Coding Standard v1.2, Test Plan v1.2, dan Test Cases v1.2.*
*Tanggal pembuatan: 2026-06-06*
