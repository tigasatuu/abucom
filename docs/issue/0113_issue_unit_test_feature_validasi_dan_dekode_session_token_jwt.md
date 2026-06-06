# Issue #0113: Perencanaan Unit-Test Feature Validasi dan Dekode Session Token JWT

## 1. Persona dan Konteks Pengerjaan
- **Persona:** Senior QA Architect & Principal AI Testing Agent (Sangat berotoritas, teliti, menguasai edge-cases keamanan, dan patuh mutlak terhadap standar ketat SDLC AbuCom).
- **Target Implementasi:** Penulisan unit test untuk memvalidasi dan mendekode session token di dalam `middleware/auth_jwt.py`.
- **Lokasi Penyimpanan Test:** Folder `tests/` dengan nama file `test_auth_jwt.py`.

## 2. Referensi Utama Dokumen SDLC
- **Referensi Utama:** `docs/sdlc/05_testing/01_test_plan.md` dan `docs/sdlc/04_implementation/01_coding_standard.md`.
- **Ekstraksi Rangkuman Data Terkait:**
  - Framework pengujian yang diwajibkan adalah `pytest`, integrasi manipulasi objek dengan `pytest-mock`, dan pengukuran melalui `coverage.py`.
  - Target minimum standar *Code Coverage* pada unit test adalah $\ge 90\%$.
  - Konvensi penamaan berkas unit test harus diawali `test_<modul_target>.py`.
  - Spesifikasi bisnis untuk keamanan otentikasi adalah *Stateless JWT HS256* dengan durasi sesi maksimal 8 jam (28.800 detik).
  - Mekanisme penolakan sistem terhadap token usang (expired) atau tidak valid diharapkan terintegrasi dan responsif dengan format *error code* spesifik (misal: `ERR-SESSION-002`).

## 3. Batasan, Cakupan, dan Isolasi Pengujian
- **Cakupan Pengujian:** Memverifikasi logika internal validasi dan ekstraksi/dekode payload JWT secara deterministik murni pada fungsi di dalam `middleware/auth_jwt.py`. Dilarang menguji hal-hal di luar logika token (seperti validasi user password di database).
- **Isolasi Mutlak:** Tes ini harus berjalan di dalam environment yang sepenuhnya terisolasi. Dilarang keras melakukan koneksi nyata (*actual connection*) ke database MySQL. Wajib menggunakan `pytest-mock` (`mocker`) untuk memalsukan data eksternal (*environment variables* seperti `SECRET_KEY`).
- **Clean State (Pembersihan Data):** Setiap fungsi skenario pengujian **wajib** menerapkan prinsip *clean state*. Gunakan `pytest.fixture(autouse=True)` atau *teardown* internal untuk menyetel ulang *environment variables* lokal (mock env) atau *mocking time* sebelum setiap iterasi pengujian agar hasil eksekusi satu pengujian tidak menyebabkan *flaky test* atau mengganggu/merusak state pengujian lainnya.
- **Kualitas Eksekusi:** Pengerjaan harus terjamin 100% kelengkapannya. Sistem menolak implementasi parsial atau *placeholder* (`pass` kosong, `# TODO: implement`).

## 4. Rincian Skenario Pengujian (Test Cases)
Skenario pengujian harus sekomprehensif mungkin, meliputi ranah berikut:
- **Skenario Positif:**
  - Verifikasi bahwa pemanggilan fungsi dekode pada token JWT yang diregistrasi secara sah dapat mengembalikan objek *payload* secara akurat (meliputi properti esensial seperti `user_id`, `role`, atau tipe pengguna yang sesuai kebutuhan bisnis).
- **Skenario Negatif / Edge Cases:**
  - Penolakan tegas atas token usang (*Expired Token*): Waktu pembuatan token disimulasikan mundur melebihi 8 jam. Verifikasi bahwa sistem melempar exception spesifik keamanan otentikasi (misalnya `ExpiredSignatureError`).
  - Penolakan *Invalid Signature*: Mencoba memvalidasi token sah menggunakan kunci rahasia (`SECRET_KEY`) yang berbeda/diretas. Verifikasi exception `InvalidSignatureError`.
  - Format malformed/kotor: Meneruskan string acak seperti `"eyJhbGc...bukan.token.asli"` dan verifikasi sistem dapat menangani format *DecodeError* secara mandiri tanpa menyebabkan aplikasi utama (*host*) terhenti secara fatal.
- **Validasi Input Khusus:**
  - Memverifikasi ketahanan sistem ketika menerima argument string token bertipe `None` atau berwujud string kosong `""`.

## 5. Alur Pengerjaan Teknis (Low-Level Checklist)

Ai/Programmer pengemban tugas ini diwajibkan mengikuti *checklist* implementasi secara runtut di bawah ini agar bebas halusinasi dan tidak ambigu:

### Tahap 1: Inisialisasi dan Persiapan Lingkungan Uji
- [ ] Membaca isi file target fungsional `middleware/auth_jwt.py` untuk menginspeksi alur fungsi utama, nama parameter input, dan struktur kembalian (output) dari fungsi yang bertugas memvalidasi token JWT.
- [ ] Membuat file baru di `tests/test_auth_jwt.py` (jika belum eksis).
- [ ] Mengimpor paket yang diwajibkan: `pytest`, modul/komponen pengujian terkait `pytest-mock`.
- [ ] Mengimpor modul spesifik fungsi target (seperti dari `middleware.auth_jwt`).
- [ ] Mengimpor dependensi bawaan yang mungkin dibutuhkan: `os`, `jwt` (`PyJWT`), dan modul manipulasi waktu `datetime`.

### Tahap 2: Penulisan Fixtures (Clean State) & Mocks
- [ ] Menuliskan fungsi berbasis `pytest.fixture(autouse=True)` untuk mereset dan memalsukan (*mock*) environment lokal variabel rahasia khusus pengujian (misalnya menetapkan `os.environ["JWT_SECRET"] = "secret_untuk_test"`).
- [ ] Mengimplementasikan *mock* fungsionalitas waktu atau memanfaatkan waktu relatif (`datetime.timedelta`) guna menstimulasi perhitungan masa aktif token untuk skenario kedaluwarsa secara presisi tanpa harus menunggu waktu aktual berjalan selama 8 jam.

### Tahap 3: Implementasi Skenario Uji Positif
- [ ] Menulis fungsi unit test, contoh: `test_decode_jwt_valid_token(mocker)`.
- [ ] Menyusun data `payload` valid, kemudian membuat *(encode)* token dummy menggunakan `SECRET_KEY` pengujian.
- [ ] Menjalankan fungsi dekode dari modul target terhadap token dummy.
- [ ] Melakukan verifikasi *Assertion*: `assert payload_hasil == payload_awal`.

### Tahap 4: Implementasi Skenario Uji Negatif & Edge Cases
- [ ] Menulis fungsi uji kedaluwarsa, contoh: `test_decode_jwt_expired_token(mocker)`. Membuat *payload* dengan nilai `exp` yang diset ke masa lampau. Melakukan verifikasi `pytest.raises` terkait penolakan akses.
- [ ] Menulis fungsi uji *signature* palsu, contoh: `test_decode_jwt_invalid_signature()`. Melakukan verifikasi menggunakan kunci enkripsi yang berbeda.
- [ ] Menulis fungsi uji tipe data/string tidak valid, contoh: `test_decode_jwt_malformed_token()`. Meneruskan string acak non-JWT dan menangkap konfirmasi penolakan exception.
- [ ] Menulis fungsi khusus validasi kosong, contoh: `test_decode_jwt_empty_or_none_input()`. Memberikan argumen `None` pada fungsi dekode token dan memastikan adanya penanganan eksepsi bertipe terkelola/graceful.

### Tahap 5: Verifikasi dan Pemastian Kualitas (Coverage Metrics)
- [ ] Menjalankan bash *command*: `pytest tests/test_auth_jwt.py -v` dan memastikan terminal merespons status `PASSED` secara penuh (100% lulus, 0 error).
- [ ] Menjalankan bash *command*: `coverage run -m pytest tests/test_auth_jwt.py && coverage report -m middleware/auth_jwt.py` untuk membuktikan persentase *Coverage Score*.
- [ ] Menginspeksi secara kritis terminal log output, jika *coverage* ternyata $< 90\%$, periksa baris blok kode (*Missing Lines*) yang terlewati dan ulangi penulisan iterasi *test case* di `tests/test_auth_jwt.py` agar target SDLC persentase ketat bisa terpenuhi.
