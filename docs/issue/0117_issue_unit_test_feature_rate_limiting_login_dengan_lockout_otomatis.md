# Issue: Perencanaan Unit Test Feature Rate Limiting Login dengan Lockout Otomatis

**Target Pelaksana:** AI Model (Claude Sonnet 4.6 / Gemini 3.1 Pro / Junior Programmer)  
**Persona Instruksi:** Senior QA Architect & Test Automation Lead  
**Referensi:** `docs/sdlc/05_testing/01_test_plan.md` dan `docs/sdlc/narasi.txt`

## 1. Konteks dan Tujuan
Berdasarkan spesifikasi SDLC, pengujian fitur *rate limiting login* berfokus pada mitigasi serangan *brute-force* dengan kriteria ketat:
*   Maksimal kegagalan berturut-turut adalah 5 kali.
*   Akun ditangguhkan (lockout) otomatis selama 10 menit (600 detik).
*   Visual Error Code spesifik saat lockout: `ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!`.
*   Standar coverage pengujian SDLC adalah $\ge 90\%$ untuk fungsi logika bisnis murni.

Tujuan dokumen ini adalah memberikan panduan teknis level-rendah (*low-level*) agar pelaksana/AI dapat membuat pengujian fungsional unit secara komprehensif, deterministik, dan kebal dari halusinasi.

## 2. Batasan dan Cakupan Pengujian
*   **Isolasi Mutlak (Mocking):** Pengujian HANYA memvalidasi aliran *pure business logic*. DILARANG KERAS menembak server database MySQL. Gunakan *dependency injection* atau utilitas `unittest.mock.patch` / `pytest-mock` untuk mensimulasikan nilai balik (return value) fungsi kueri database dan pergerakan waktu komputasi (`datetime.now()`).
*   **Clean State Consistency:** Setiap fungsi skenario pengujian wajib me-reset _state_. Gunakan instrumen `@pytest.fixture(autouse=True)` atau blok `teardown/yield` untuk menghentikan seluruh _side-effects_ dari patch agar tidak mencemari memori pengujian lainnya.
*   **Kualitas Tanpa Kompromi:** Dilarang meletakkan sintaks *placeholder* (`pass`, `TODO`, `...`). Seluruh fungsi uji harus komplit, dapat dipanggil, dan memiliki klausa asersi (*assert*) spesifik.
*   **Lokasi File Test:** File wajib disimpan di dalam folder root `tests/` sesuai konvensi Python Pytest.

## 3. Checklist Alur Eksekusi (Low-Level Implementation)

Pelaksana WAJIB memproses seluruh poin *checklist* ini tanpa terkecuali:

### Fase A: Inisialisasi Environment & Fixtures
- [ ] Buat file unit test baru di `tests/test_unit_rate_limiting_lockout.py`.
- [ ] Lakukan impor framework dan pustaka pengujian utama: `import pytest`.
- [ ] Lakukan impor utilitas mocking bawaan Python: `from unittest.mock import patch, MagicMock`.
- [ ] Lakukan impor modul penanganan waktu: `from datetime import datetime, timedelta`.
- [ ] Lakukan impor fungsi kontrol autentikasi/rate-limiting dari modul `logic` yang diuji.
- [ ] Susun `pytest.fixture(autouse=True)` yang bernama `clean_state()` dan letakkan konfigurasi pembersihan patch/mock di dalam blok _yield_ atau blok _finally_.

### Fase B: Skenario Pengujian Positif (Positive Cases)
- [ ] **Skenario 1: Login sukses pada percobaan pertama (0 gagal sebelumnya)**
  - [ ] *Setup Mock:* Mock interaksi fungsi DB agar me-return *user object* dengan `failed_login_attempts=0`, `locked_until=None`, dan mock fungsi verifikasi bcrypt me-return `True`.
  - [ ] *Eksekusi:* Lakukan eksekusi fungsi autentikasi login.
  - [ ] *Assertion (Verifikasi):* Pastikan logic login tidak melempar error dan nilai _return_ valid. Pastikan fungsi database untuk _reset attempts_ kembali ke 0 terpanggil.
- [ ] **Skenario 2: Login sukses setelah masa durasi lockout kedaluwarsa (10 menit usai)**
  - [ ] *Setup Mock:* Mock waktu sekarang `datetime.now()` ke momen `T`. Mock fungsi DB agar me-return `locked_until` pada waktu `T - timedelta(minutes=10, seconds=1)`. Mock verifikasi sandi ke `True`.
  - [ ] *Eksekusi:* Lakukan eksekusi autentikasi login.
  - [ ] *Assertion (Verifikasi):* Pastikan penjagaan (*gatekeeper*) meloloskan login, lalu memanggil rutinitas query untuk me-reset ulang status (failed = 0, locked = None).

### Fase C: Skenario Pengujian Negatif (Negative/Edge Cases)
- [ ] **Skenario 3: Percobaan gagal wajar (Kegagalan ke-1 hingga ke-4)**
  - [ ] *Setup Mock:* Mock DB mengembalikan nilai `failed_login_attempts=2`. Mock verifikasi kata sandi menjadi `False`.
  - [ ] *Eksekusi:* Lakukan eksekusi autentikasi login.
  - [ ] *Assertion (Verifikasi):* Memastikan logic melempar eksepsi error umum login (`ERR-AUTH-001`). Memastikan logic memicu fungsi pembaruan *increment* kegagalan ke database dengan _argument_ angka `3`, dan pastikan argumen untuk `locked_until` bernilai kosong (NULL/None).
- [ ] **Skenario 4: Menembus Batas Maksimal (Percobaan Gagal ke-5)**
  - [ ] *Setup Mock:* Mock akumulasi gagal saat ini menjadi `4`. Mock sandi kembali `False`. Mock statis waktu sekarang di titik `T`.
  - [ ] *Eksekusi:* Lakukan eksekusi autentikasi login.
  - [ ] *Assertion (Verifikasi):* Logic wajib memperbarui ke database dengan argumen `failed_login_attempts=5`, dan argumen pembaruan `locked_until` diisi nilai absolut masa depan yakni `T + timedelta(minutes=10)`.
- [ ] **Skenario 5: Berusaha login di tengah masa lockout aktif, dengan sandi BENAR**
  - [ ] *Setup Mock:* Mock field `locked_until` ke posisi waktu di depan (masih masa blokir). Mock rutinitas verifikasi sandi me-return `True`.
  - [ ] *Eksekusi:* Lakukan eksekusi autentikasi login.
  - [ ] *Assertion (Verifikasi):* Sistem WAJIB melempar eksepsi kode spesifik `ERR-AUTH-002: Sandi Gagal: Akun ditangguhkan selama 10 menit akibat brute-force!`. Sistem dilarang memberikan akses (*early return*) walau sandi yang diinput valid.
- [ ] **Skenario 6: Berusaha login di tengah masa lockout aktif, dengan sandi SALAH**
  - [ ] *Setup Mock:* Konfigurasi lockout sama seperti Skenario 5. Mock verifikasi sandi menjadi `False`.
  - [ ] *Eksekusi:* Lakukan eksekusi autentikasi login.
  - [ ] *Assertion (Verifikasi):* Sistem wajib melempar eksepsi `ERR-AUTH-002`. Sangat Kritis: Pastikan query untuk proses *increment* akumulasi gagal **TIDAK TERPANGGIL** (nilai `failed_login_attempts` tidak boleh jadi 6, terkunci statis di 5).

### Fase D: Validasi Input (Input Validation Handling)
- [ ] **Skenario 7: Data kotor pada akumulasi percobaan gagal**
  - [ ] *Setup Mock:* Berikan simulasi response database yang anomali, seperti `failed_login_attempts=None` atau bertipe *string kosong*.
  - [ ] *Assertion (Verifikasi):* Buktikan mekanisme *casting / fallback* aplikasi berfungsi, men-sanitize input kotor tersebut ke angka absolut `0` sebelum diproses logika *increment*, guna melindungi aplikasi dari *TypeError* yang memicu *crash* internal.

### Fase E: Verifikasi Kualitas Akhir
- [ ] **Instruksi Akhir:** Dokumentasikan perintah terminal yang wajib dijalankan oleh pelaksana (*executor*) guna menghasilkan laporan komprehensif *Code Coverage*:
  ```bash
  pytest tests/test_unit_rate_limiting_lockout.py -v --cov=logic --cov-report=term-missing
  ```
- [ ] Lakukan evaluasi mandiri memastikan seluruh _branch logic_ dan blok kode yang berkaitan dengan kondisi lockout tereksekusi tanpa absen.
