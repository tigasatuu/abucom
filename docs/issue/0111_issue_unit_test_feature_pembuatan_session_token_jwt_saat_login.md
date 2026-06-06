# Issue: Unit Test Feature Pembuatan Session Token JWT Saat Login

## 1. Persona Eksekutor
**Senior QA Automation Engineer & Principal Software Engineering Standards Architect**
AI yang mengeksekusi issue ini harus bertindak sangat teliti, berfokus pada detail edge cases, mematuhi standar pengkodean murni (Functional Programming/FP), serta sangat ketat terhadap code coverage (minimum 90%) dan isolasi data. Tidak ada toleransi untuk manipulasi state yang bocor antar eksekusi test.

## 2. Referensi Utama
*   `docs/sdlc/05_testing/01_test_plan.md` (Dasar arsitektur testing, isolasi sandbox, dan target coverage)
*   `docs/sdlc/04_implementation/01_coding_standard.md` (Konvensi penamaan test, letak folder, dan kaidah pure function)
*   `docs/sdlc/narasi.txt` (Referensi alat dependensi spesifik: `pytest`, `pyjwt`, `bcrypt`)

## 3. Ekstraksi Detail Konteks dari Dokumen SDLC
Berdasarkan dokumen referensi, berikut adalah standar mutlak pengerjaan unit testing pada project ini:
*   **Framework**: Wajib menggunakan `pytest`.
*   **Coverage**: Target persentase cakupan pengujian unit baris kode (Code Coverage) $\ge 90\%$.
*   **Isolasi Lingkungan**: Pengujian logic murni (pure functions) **DILARANG** melakukan koneksi fisik ke database produksi maupun environment nyata. 
*   **Dependensi Terkait**: `pyjwt` untuk manipulasi JWT, `pytest` untuk framework pengujian otomatis, dan `bcrypt` jika integrasi password hashing terlibat.
*   **Konvensi Penamaan**: 
    * File test harus berawalan `test_` dan mutlak diletakkan di dalam folder `tests/`.
    * Fungsi pengujian harus bernama deskriptif dengan format: `test_<behavior_spesifik>()` (contoh: `test_generate_jwt_session_sukses()`).

## 4. Batasan, Cakupan, dan Alur Pengerjaan
*   **Cakupan**: Pengujian difokuskan murni pada fungsionalitas logika pembuatan session token JWT ketika proses login sukses, memvalidasi struktur serta isi *payload* JWT (seperti `user_id`, `role`, expiry `exp`), dan validasi penanganan kondisi *error* ketika token dibuat.
*   **Batasan**: Pengujian sepenuhnya terisolasi dan tidak boleh menyentuh atau memodifikasi modul fungsional yang sudah berjalan. Hanya kode unit test yang ditambahkan.

## 5. Instruksi Keamanan dan Isolasi (Mocking)
*   Sesuai kaidah dari SDLC, eksekutor **WAJIB menggunakan Mocking** (misalnya via `unittest.mock.patch` atau fixture `pytest`) untuk seluruh pengambilan data user dari layer repositori database. Gunakan struktur data *NamedTuple*, *Dataclass*, atau *Dictionary* statis untuk merespresentasikan data database.
*   **Clean State Rule**: Setiap skenario test WAJIB didahului dengan pembersihan atau *reset state* lingkungan secara otomatis menggunakan *teardown* atau *yield fixture* dari `pytest`. Pastikan *environment variable* palsu (mock `.env` seperti rahasia `JWT_SECRET_KEY`) dibersihkan agar hasil pengujian sepenuhnya deterministik dan konsisten tanpa kebocoran memori atau variable antar test.

## 6. Skenario Pengujian (Test Cases)
Buatlah kode skenario pengujian dengan cakupan selengkap mungkin:

### Skenario Positif (Positive Path)
*   `test_generate_jwt_valid_credentials_sukses()`: Memastikan JWT token berbentuk tipe data `str` yang benar dan dikembalikan saat kredensial valid disuplai.
*   `test_jwt_payload_contains_correct_claims()`: Memastikan hasil generate token berhasil di-decode ulang dan mengandung payload data mutlak seperti (`user_id`, hak akses/`role`, tipe session, dan format tanggal kedaluwarsa yang akurat).

### Skenario Negatif dan Edge Cases
*   `test_generate_jwt_invalid_secret_key()`: Memastikan error/exception jenis `jwt.exceptions.InvalidSignatureError` terlempar ketika memverifikasi token yang ditandatangani oleh *secret key* yang salah/berbeda.
*   `test_jwt_token_expiration()`: Memastikan fungsionalitas batas waktu kedaluwarsa token benar-benar bekerja. Token harus expired setelah *Time to Live (TTL)* terlewati (gunakan teknik *mock time* / time freeze untuk memajukan waktu komputasi secara logis).
*   `test_generate_jwt_with_missing_mandatory_payload()`: Memastikan pengujian menangkap error `ValueError` atau kegagalan yang sesuai jika mencoba men-generate JWT namun terdapat parameter esensial (misal `role` user) yang bernilai `None`.

### Validasi Input 
*   `test_login_empty_input_returns_error()`: Memastikan skenario parameter kosong (username atau password) pada fungsi wrapper login berhasil digagalkan dengan memberikan *error handling* yang proper sebelum masuk ke proses enkripsi JWT.

## 7. Checklist Tahapan Pengerjaan Low-Level
Eksekutor wajib mengikuti panduan ini langkah demi langkah tanpa mengabaikan detail, dan tidak meninggalkan fungsi berstatus *to-do*.

- [ ] **Persiapan & Analisis**
  - [ ] Verifikasi dan baca spesifikasi file sumber (source code) tempat fungsi generate JWT dan logika Login bersemayam.
  - [ ] Pastikan bahwa framework `pytest` dan lib `pyjwt` sudah tercatat di dalam dependensi aktif proyek.
- [ ] **Inisialisasi File Test**
  - [ ] Buat file unit test baru di path penyimpanan standar: `tests/test_auth_jwt.py` (atau sesuaikan dengan nama modul terkait).
  - [ ] Lakukan *import* dependensi `pytest`, library `jwt`, fungsi target yang diuji, serta fungsi mocking.
- [ ] **Penulisan Fixture Mocking (Clean State & Determinisme)**
  - [ ] Tulis *fixture* pytest yang akan mem-mocking dan mengatur (set/unset) variabel `JWT_SECRET_KEY` ke nilai *dummy string* agar fungsi tidak menyentuh file `.env` asli.
  - [ ] Implementasikan mekanisme `yield` pada fixture untuk me-reset ulang modifikasi *environment/mock* setiap kali satu fungsi test selesai dieksekusi.
  - [ ] Buat *dummy payload data* statis menggunakan dictionary untuk mensimulasikan hasil data user setelah verifikasi *bcrypt* berhasil.
- [ ] **Penulisan Kode: Skenario Positif**
  - [ ] Implementasikan `test_generate_jwt_valid_credentials_sukses()` dengan menyuplai *dummy data* ke dalam fungsi login dan memeriksa bahwa *return value* bukan `None` serta bertipe string token.
  - [ ] Implementasikan `test_jwt_payload_contains_correct_claims()` dengan menggunakan fungsi `jwt.decode` (dengan spesifikasi *mock secret key* yang sama) dan me-lakukan verifikasi nilai *claims*.
- [ ] **Penulisan Kode: Skenario Negatif & Edge Cases**
  - [ ] Implementasikan `test_jwt_token_expiration()` dengan bantuan *mock datetime* agar pengecekan kedaluwarsa token dapat diisolasi dan divalidasi.
  - [ ] Implementasikan error handling test untuk menanggkap exception saat *secret key* di-decode secara asal-asalan.
- [ ] **Penulisan Kode: Validasi Input**
  - [ ] Buat kode test yang menyuntikkan argumen kosong `""` atau nilai `None` pada form username/password, dan pastikan memicu status error atau validasi fail sebelum JWT sempat memprosesnya.
- [ ] **Verifikasi & Assertions Ketat**
  - [ ] Cek dan periksa ulang semua baris *assertion* (`assert ... == ...`, `pytest.raises()`) dan pastikan mengecek nilai serta tipe data.
  - [ ] Tambahkan anotasi tipe data (*type hinting*) standar PEP 484 pada semua deklarasi *variable* test.
- [ ] **Finalisasi Eksekusi (Kualitas Ekstra Ketat)**
  - [ ] Pastikan **TIDAK ADA SATU PUN** baris kode sisa atau fungsionalitas yang masih berstatus `pass` atau `TO-DO`.
  - [ ] Kualitas pengujian harus sempurna dan lulus deterministik; uji semua dengan perintah pytest lokal sebelum dinyatakan selesai.
