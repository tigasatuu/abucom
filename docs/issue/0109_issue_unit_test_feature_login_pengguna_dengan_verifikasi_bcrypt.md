# Issue: Unit Test Feature Login Pengguna dengan Verifikasi Bcrypt

## 1. Persona Eksekutor
**Peran:** Senior QA Automation Engineer / Principal SDET (Software Development Engineer in Test) spesialis Python & Pytest.
**Tanggung Jawab:** Merancang, menulis, dan memvalidasi *unit test* deterministik untuk fungsi logika *login* dengan verifikasi *bcrypt*, menjamin *coverage* minimal 90%, dan memastikan tidak ada koneksi fisik ke *database* atau *filesystem* selama pengujian berlangsung.

## 2. Referensi Utama
Pengembangan unit test ini wajib mematuhi standar yang telah ditetapkan dalam dokumen SDLC berikut:
- `docs/sdlc/05_testing/01_test_plan.md` (Strategi dan metodologi Unit Testing, target *coverage*)
- `docs/sdlc/04_implementation/01_coding_standard.md` (Aturan Unit Testing Pure Functions, larangan koneksi fisik DB, penggunaan mock `NamedTuples`)
- `docs/sdlc/04_implementation/02_environment_setup.md` (Pustaka `pytest`, `pytest-mock`, `coverage`)
- `docs/sdlc/06_deployment/02_environment_config.yaml` (Konfigurasi `bcrypt_cost_factor` untuk testing)

## 3. Ekstraksi Detail Referensi SDLC
- **Framework Utama:** Menggunakan `pytest`.
- **Target Coverage:** *Code coverage* untuk fungsi yang diuji harus mencapai $\ge 90\%$ yang dibuktikan secara kuantitatif melalui library `coverage`.
- **Aturan Isolasi (Pure Functions):** Unit testing bersifat **deterministik** dan **terisolasi penuh**. **DILARANG KERAS** melakukan koneksi fisik ke database MySQL (baik lokal maupun *testing db*) atau sistem *file* (*filesystem*).
- **Penggunaan Mock:** Data state (seperti objek *user* dari *database*) WAJIB disimulasikan (di-*mock*) dan diteruskan ke fungsi sebagai argumen, idealnya menggunakan struktur imutabel seperti `NamedTuples` atau struktur data standar *dictionary* tanpa status tersembunyi (*hidden state*).
- **Optimasi Bcrypt:** Saat pengujian otomatis berjalan, `bcrypt_cost_factor` harus direkayasa menjadi minimal (misal bernilai `4`) agar eksekusi *unit test* berjalan sangat cepat dan tidak *bottleneck* di komputasi *hash*.

## 4. Batasan, Cakupan, dan Alur Pengerjaan
**Cakupan:**
- Memvalidasi fungsi verifikasi *password* *bcrypt* dan logika *login* secara independen.
- Tidak mencakup pengujian integrasi CLI, API, atau koneksi *database* nyata. Murni *testing* terhadap *business logic* (Pure FP).
- Operasi login harus terisolasi tanpa merusak *state* global.

**Alur Pengerjaan:**
1. Inisialisasi *setup* test dan *fixtures*.
2. Penulisan *mock objects* / fungsi deterministik palsu (sebagai pengganti *repository* atau akses *database*).
3. Pembuatan skenario positif.
4. Pembuatan skenario negatif dan *edge cases*.
5. Menjalankan *test suite* dan mengukur *coverage*.

## 5. Direktori Penyimpanan
Unit test harus disimpan dalam folder `tests/` di *root directory*. 
Nama *file* yang direkomendasikan: `tests/test_login_bcrypt.py` (atau `tests/test_pengguna.py` jika disatukan ke test module *pengguna*).
Dependensi pengujian yang digunakan: `pytest`, `pytest-mock`, `coverage`.

## 6. Skenario Uji (Test Scenarios)
Setiap skenario **wajib** melakukan *reset state/clean state* pada setiap inisialisasi agar eksekusi antar test independen dan konsisten.

### A. Skenario Positif (Positive Cases)
- [ ] Login berhasil dengan *username* dan *password* valid (memastikan *bcrypt hash matcher* me-*return* nilai *True*/*Sukses*).
- [ ] Pastikan tidak bocor/tersisanya parameter rahasia di *return object* (seperti penghilangan *password_hash* di *response* login).

### B. Skenario Negatif (Negative Cases)
- [ ] Gagal login karena *password* salah (mengembalikan *error/exception* otentikasi gagal).
- [ ] Gagal login karena *username* tidak ditemukan dalam basis data (sistem menerima `None` dari fungsi *mock repository* pencari user).

### C. Edge Cases & Validasi Input
- [ ] Penolakan login saat *password* kosong (string kosong `""`).
- [ ] Penolakan login saat *username* kosong (`""` atau string spasi `   `).
- [ ] Validasi error ketika tipe data kredensial tidak sesuai (contoh: *input password* berupa `integer` atau `None`).
- [ ] Penanganan dan *Assertion* perilaku aplikasi ketika panjang *password* melebihi batas byte internal dari `bcrypt` (misalnya \> 72 *bytes*).
- [ ] Memastikan `bcrypt` mengembalikan kesalahan jika skema *hash* yang direkam di *database mock* adalah nilai acak/rusak (*malformed hash*).

## 7. Instruksi Eksekusi Tingkat Rendah (Low-Level Checklist)

Eksekutor (Junior Programmer atau Agen LLM) **WAJIB** mencentang dan menyelesaikan daftar periksa ini secara berurutan secara terstruktur tanpa ruang halusinasi:

### Tahap 1: Setup dan Clean State
- [ ] Import pustaka utama: `pytest`, `bcrypt` dan fungsi *pure logic* target (misalnya dari `logic/pengguna.py` atau `logic/auth_handler.py`).
- [ ] Konfigurasi *fixture* `@pytest.fixture` untuk *clean state* yang menyiapkan *Mock Data/NamedTuple* berisi `username` dan simulasi `password_hash` otentik `bcrypt`. Pastikan reset data per skenario.
- [ ] *Mock* nilai *work factor/cost factor bcrypt* (jika menggunakan variabel *env*) menjadi batas terkecil (misalnya `4`) untuk mengakselerasi test otomatis.
- [ ] Pastikan bahwa fungsi pencarian *user* ke *database* di-*mock* sepenuhnya atau diinjeksi via parameter (contoh: `find_user_by_username_mock(username)`).

### Tahap 2: Implementasi Kode Skenario Uji (Sesuai Konvensi Naming Pytest)
- [ ] Tulis `test_login_berhasil_dengan_kredensial_valid()` yang mensimulasikan pencocokan *hash bcrypt* berhasil, lalu lakukan *Assertion* respon yang sukses.
- [ ] Tulis `test_login_gagal_karena_password_salah()` yang memverifikasi bahwa sistem melontarkan *error/exception* saat *password text* salah disandingkan dengan *hash mock*.
- [ ] Tulis `test_login_gagal_user_tidak_ditemukan()` yang mendemonstrasikan kelakuan saat `find_user_mock` mengembalikan hasil kosong (None), wajib di-*Assert* sebagai `User Not Found` *error*.
- [ ] Tulis serangkaian *test case* menggunakan paramaterisasi (`@pytest.mark.parametrize`) untuk *Edge Cases* yang berisi *username/password* kosong, panjang 80+ karakter, dan nilai *None/Integer*.

### Tahap 3: Verifikasi Kualitas Eksekusi
- [ ] Cek secara ketat agar **TIDAK ADA** satupun komentar `TODO`, `pass`, atau blok `# fixme` yang ditinggalkan di dalam fungsi *test*.
- [ ] Eksekusi `pytest tests/[nama_file_test].py -v` secara mandiri dan pastikan output seluruhnya `PASSED`.
- [ ] Verifikasi ketat *Code Coverage* dengan menjalankan `coverage run -m pytest tests/[nama_file_test].py` dilanjutkan dengan `coverage report -m`. Pastikan area fungsi otentikasi mendapatkan coverage $\ge 90\%$.
- [ ] Pastikan file *test* ini terisolasi dan tidak merusak fungsi *test* sebelumnya (misal tidak mengganti variabel global).
