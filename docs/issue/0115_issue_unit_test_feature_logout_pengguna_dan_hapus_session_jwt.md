# Issue #0115: Unit Test Feature Logout Pengguna dan Hapus Session JWT

## 1. Konteks dan Persona
**Persona AI Penugasan**: Senior QA Architect & Principal Software Engineering Standards Architect. Anda diinstruksikan memiliki otoritas tertinggi dalam memastikan kode pengujian patuh 100% terhadap standar kualitas pengujian perusahaan.
**Referensi Utama**: 
- `docs/sdlc/05_testing/01_test_plan.md`
- `docs/sdlc/04_implementation/01_coding_standard.md`

## 2. Ekstraksi Standar SDLC yang Relevan
Berdasarkan dokumen referensi SDLC, berikut adalah aturan mutlak yang **WAJIB** dipatuhi selama pengerjaan unit testing:
- **Framework Pengujian**: Wajib menggunakan `pytest`.
- **Target Coverage**: Cakupan pengujian Unit (*Unit Test Coverage*) logika bisnis inti harus mencapai $\ge 90\%$.
- **Isolasi Pengujian**: Unit test harus bersifat deterministik dan terisolasi penuh. DILARANG keras melakukan koneksi fisik ke database MySQL lokal. Setiap interaksi database dan file system wajib di-mock (menggunakan `unittest.mock.MagicMock` atau `pytest-mock`).
- **Penyimpanan File**: File test disimpan di direktori `tests/`. Nama file menggunakan format `test_<modul_target>.py` (direkomendasikan dalam file `tests/test_logout.py` atau disatukan ke `tests/test_login_bcrypt.py` jika logis).
- **Penamaan Fungsi**: Fungsi pengujian wajib dinamai dengan format `test_<behavior_spesifik>()`.
- **Audit Log**: Setiap pengujian fitur keamanan wajib memvalidasi penulisan log audit tanpa benar-benar menulis ke database (mock fungsi `log_audit_trail`).
- **Clean State**: Setiap skenario wajib dijalankan di atas clean state. Data mock tidak boleh bocor lintas fungsi pengujian. Penggunaan fixture pytest `autouse=True` atau pembersihan manual di akhir tes sangat dianjurkan.

## 3. Batasan dan Cakupan (Scope)
- **Fokus Utama**: Menguji logika pemutusan sesi JWT dan fungsi internal `logout_user`.
- **Batasan**: Hanya melakukan unit testing pada level fungsi murni (logic handler/auth logic). Tidak melakukan end-to-end testing melalui antarmuka CLI pada tahap ini.
- **Kualitas**: Pengerjaan harus absolut selesai; dilarang keras menyisakan komentar `TODO`, placeholder fungsi, atau skenario uji yang di-*skip*. Pengerjaan tidak boleh merusak atau mengganggu fungsi login atau fitur eksisting lainnya.

## 4. Skenario Pengujian (Test Cases)
Skenario pengujian harus mencakup tiga pilar utama:
1. **Skenario Positif**:
   - `test_logout_user_sukses`: Menguji `session_state` valid dapat memicu respons fungsi berhasil dengan pengembalian `Result(is_success=True)`.
   - `test_logout_audit_trail_tercatat`: Memastikan fungsi pencatat log audit terpanggil presisi pada event `LOGOUT`.
2. **Skenario Validasi Input**:
   - `test_logout_session_kosong_atau_minimal`: Menguji jika data sesi yang diteruskan hanya berisi field wajib, memastikan tidak terjadi `KeyError`.
   - `test_logout_session_state_invalid_type`: Input `session_state` yang tidak sesuai tipe (misalnya `None`, `Integer`, `String`), untuk membuktikan sistem menangkap error (misalnya melemparkan `TypeError` atau `AttributeError`).
3. **Skenario Negatif / Edge Cases**:
   - `test_logout_audit_trail_gagal_database_terganggu`: Simulasi di mana database terputus / *crash* (`mock_cursor.execute.side_effect = Exception`) saat menulis log audit. Tes harus membuktikan aplikasi tidak ikut crash, error ditangani *gracefully*, dan koneksi ditutup dengan aman (`mock_cursor.close()`).

## 5. Low-Level Execution Checklist
Kerjakan tahapan berikut secara berurutan dan ketat:

### A. Tahap Inisialisasi & Persiapan
- [ ] Baca ulang panduan standar pytest pada `docs/sdlc/05_testing/01_test_plan.md`.
- [ ] Pindai struktur direktori `tests/` dan baca file test autentikasi terkait seperti `tests/test_login_bcrypt.py` untuk mengadopsi pola fixture dan mocking yang sudah ada.
- [ ] Buat file test baru (contoh `tests/test_logout.py`) atau tambahkan ke file test yang ada dengan standar Docstring PEP 257 (Nama Modul, Deskripsi, Author, Tanggal).
- [ ] Lakukan impor modul dependency wajib: `import pytest`, `from unittest.mock import MagicMock`, dan impor fungsi `logout_user`.

### B. Setup Fixture & Mocking (Enforcing Clean State)
- [ ] Buat `@pytest.fixture` bernama `mock_db_conn` yang mengembalikan `MagicMock()` untuk mencegah koneksi fisik ke database produksi/development.
- [ ] Pastikan tidak ada data global statis yang dimutasi antartes. Gunakan variabel objek baru di dalam tiap tes untuk menjamin independensi *clean state*.

### C. Penulisan Kode Skenario Pengujian
- [ ] **Skenario Positif**: Tulis `test_logout_user_sukses()`.
  - Buat dictionary mock `session_state` lengkap.
  - Lakukan `mocker.patch` pada dependensi internal seperti audit logger.
  - Assert `logout_user(session_state, mock_db_conn)` me-return sukses tanpa error message.
- [ ] **Skenario Positif Validasi**: Tulis `test_logout_user_dengan_session_state_minimal()`.
  - Buat mock `session_state` dengan minimum parameter (hilangkan key tidak wajib jika ada).
  - Assert proses logout berjalan normal dan audit logging merekam status `LOGOUT`.
- [ ] **Skenario Validasi Input**: Tulis pengujian berbasis `@pytest.mark.parametrize` untuk tipe invalid.
  - Inject tipe nilai `None` atau tipe data tak terduga.
  - Panggil `pytest.raises(ExceptionType)` untuk memastikan fungsi yang diuji dengan elegan menangkap kesalahan tipe.
- [ ] **Skenario Edge Case**: Tulis `test_logout_user_audit_trail_gagal_database_terganggu()`.
  - Lakukan *mocking* kursor: `mock_cursor = MagicMock()`, lalu ubah eksekusinya melempar Exception.
  - *Patch* nilai kembalian `mock_db_conn.cursor.return_value = mock_cursor`.
  - Jalankan pemanggilan fungsi dan assert sistem tetap sukses berkat try-except internal.
  - Assert pemanggilan metode `close()` pada kursor dipanggil minimal sekali.

### D. Verifikasi & Kualitas Akhir
- [ ] Jalankan perintah `pytest tests/ -v` melalui shell. Pastikan seluruh uji pada modul logout me-return `PASSED`.
- [ ] Opsional: Jalankan `pytest --cov=logic tests/` untuk memvalidasi metrik tercapai $\ge 90\%$.
- [ ] Verifikasi dan bersihkan kode dari skrip/print debugging tambahan, *dead code*, dan *unused imports*.
- [ ] Pastikan tidak ada fungsi fiktif berupa indikator komentar `TODO`. Semua skenario harus riil dan bisa berjalan deterministik.
