# Issue: Unit-Test Feature Pencatatan Audit Trail Format JSON

## 1. Persona Eksekutor
**Persona:** Principal QA Automation Engineer & Python SDET (Software Development Engineer in Test).
**Tugas Anda:** Mengeksekusi perencanaan tingkat rendah (low-level planning) ini untuk menghasilkan test suite `pytest` dengan cakupan kode (code coverage) minimal 90%, fungsionalitas pengujian murni yang terisolasi ketat, dan mematuhi standar arsitektur AbuCom (Functional Programming murni).

## 2. Referensi Utama & Ekstraksi Data SDLC
*   **Dokumen Acuan:** `docs/sdlc/05_testing/01_test_plan.md`
*   **Modul Referensi (SDLC):** Modul M.7 (Keamanan, Audit Trail & Hak Akses).
*   **ID Skenario Utama:** M7-TC-003.
*   **Ekstraksi Aturan SDLC:**
    *   **Standar Framework:** Menggunakan `pytest` untuk *test runner* dan `coverage.py` untuk mengukur *code coverage*.
    *   **Target Mutu:** Persentase cakupan kode (coverage) untuk logika bisnis inti wajib $\ge 90\%$.
    *   **Standar Logika Bisnis:** Pemrograman berparadigma *Functional Programming* murni tanpa OOP/class untuk logika inti. Test suite yang ditulis harus mendemonstrasikan pengujian fungsi yang deterministik.
    *   **Persyaratan Log:** Wajib merekam perubahan status data ke dalam format terstruktur JSON (merepresentasikan komparasi detail presisi `old_value` dan `new_value`).

## 3. Batasan, Cakupan & Pedoman Kualitas
*   **Cakupan Pengerjaan:** Membangun test-suite komprehensif khusus untuk menguji logika fungsional dari pembentukan format log JSON, komparasi payload data, sanitasi nilai, serta perakitan objek Audit Trail.
*   **Isolasi Penuh (Mocking):** Karena ini berada pada level *Unit Test*, pengujian HARUS terisolasi dari *side-effects* luar. Dilarang keras berinteraksi dengan database MySQL, Network, atau File System secara nyata. Wajib gunakan `unittest.mock` (seperti `patch` atau `MagicMock`) untuk memalsukan koneksi/interaksi luar.
*   **Kualitas & Ketuntasan:** Eksekusi issue ini wajib memegang prinsip kualitas kode tingkat tinggi. Fungsi test yang dikembangkan tidak boleh cacat. Dilarang keras meninggalkan kode yang diakhiri `pass`, blok `to-do`, fungsi tanpa assertion, atau *fallback* yang tidak tuntas. Seluruh skenario uji harus terimplementasi 100% tuntas.

## 4. Lokasi File Unit Test
*   **Direktori Test:** Sesuai standar struktur pengujian `pytest`, letakkan berkas test di folder `tests/unit/`.
*   **Nama File Target:** Sesuaikan dengan *naming convention* pytest, misalnya `tests/unit/test_audit_trail.py` atau `tests/unit/test_audit_log_json.py`.

---

## 5. Low-Level Checklist Pengerjaan

Silakan berikan tanda `[x]` pada checklist di bawah ini untuk setiap tahapan yang berhasil dieksekusi.

### A. Inisialisasi & Persiapan File Test
- [ ] Buat berkas baru (misal `tests/unit/test_audit_trail.py`) di struktur *testing environment*.
- [ ] Deklarasikan impor *library* bawaan (`pytest`, `json`, `unittest.mock`).
- [ ] Lakukan impor *function under test* (fungsi logika pembentuk audit trail) dari *source file* terkait.
- [ ] Siapkan data statis *mock* dan *fixture* statis berupa representasi *NamedTuple* / *Dictionary* Python murni yang mencerminkan *state* transaksi/data (misal profil pengguna, kasbon, dsb).

### B. Clean State Management (Konsistensi Kondisi Uji)
- [ ] Pastikan mengimplementasikan fitur `setup` / `teardown` murni dari `pytest` (menggunakan `@pytest.fixture(autouse=True)` atau *yield fixture* khusus) yang menginstruksikan reset total *mock object*, *cache variables*, dan pembersihan variabel memori sebelum dan sesudah setiap satu fungsi test dijalankan (Mencegah state-leakage).

### C. Penulisan Skenario Test (Fungsional)

#### C.1. Skenario Positif (Positive Path)
- [ ] **Test Logika Update Standar:** Uji fungsi generator audit dengan memasukkan *old_value* dan *new_value* yang memiliki perbedaan valid (contoh: kuantitas stok dari `10.0` menjadi `5.0`).
- [ ] Verifikasi (assert) *return value* adalah representasi data string/obyek JSON yang sah (`json.loads` berhasil).
- [ ] Verifikasi JSON payload memuat field `old_value` dan `new_value` yang isinya memetakan perbedaan properti secara eksak.
- [ ] **Test Rekaman Meta Data:** Pastikan data pengguna (user pelaksana, timestamp, nama tabel target) ikut terepresentasi ke dalam payload audit log.

#### C.2. Skenario Negatif & Edge Cases (Boundary Path)
- [ ] **Test Insert Data Baru (Null Handling):** Uji fungsi jika data awal (`old_value`) adalah sekadar parameter `None` atau kosong (simulasi pembuatan data baru).
- [ ] Verifikasi bahwa representasi output *old_value* dirender dengan aman menjadi *null* pada standar JSON, tanpa melempar kegagalan (seperti `KeyError` atau `TypeError`).
- [ ] **Test Delete Data (Final State Null):** Uji fungsi ketika data (`new_value`) diset `None` (simulasi *hard delete*).
- [ ] Verifikasi format JSON menyematkan nilai *new_value* sebagai *null* secara eksak, namun tetap mempertahankan detail utuh *old_value*.
- [ ] **Test Tidak Ada Perubahan (Identical Payload):** Uji fungsi ketika *old_value* dan *new_value* adalah representasi struktur yang sama persis 100%.
- [ ] Verifikasi sistem merespons skenario identik ini secara efisien, misalnya tidak membentuk JSON (mengembalikan string kosong, obyek log nihil, atau penanda `NO_CHANGES`).
- [ ] **Test Tipe Parameter Tidak Lazim:** Masukkan obyek list sederhana alih-alih `dict` pada payload awal.
- [ ] Verifikasi sistem memicu penanganan *Exception Handling* (seperti `ValueError`) yang aman secara standar FP dan ditangkap (assert) oleh `pytest.raises`.

#### C.3. Skenario Validasi Input Khusus & Presisi Lanjutan
- [ ] **Test Format Desimal & Mata Uang:** Uji fungsi komparasi dengan menyuntikkan obyek tipe `Decimal` Python (misalnya Decimal `100.0005`), karena ini umum pada arsitektur presisi SDLC aplikasi (misal nilai stok desimal/margin keuntungan).
- [ ] Verifikasi bahwa *serializer* JSON tidak *crash* terhadap representasi *Decimal* dengan menerapkan *custom json encoder* yang mengonversi `Decimal` ke string presisi tinggi (`'100.0005'`) di memori output log.
- [ ] **Test Sanitasi Karakter Escape (Injection Defense):** Uji input yang memuat karakter kontrol ANSI/escape (`\n`, `\x1b[31m`).
- [ ] Verifikasi output log JSON tersanitasi secara aman (atau tetap menyimpan escape karakter standar format JSON) tanpa merusak *parser*.

### D. Verifikasi & Sign-off Mutu (QA Cleanup)
- [ ] Lakukan eksekusi test runner lokal pada modul unit audit trail saja (misal via eksekusi command line simulasi) untuk melihat progres.
- [ ] Validasi *Code Coverage* modul fitur tersebut minimal mencapai rasio **>= 90%** (menggunakan *coverage.py*).
- [ ] Verifikasi ulang tidak ada deklarasi fungsi yang buntu / belum terselesaikan, komentar sisa *debugging* dan instruksi *"To-Do"*, semua *Test Case* berstatus **PASS** / **SUCCESS** hijau.

---
*Dokumen ini diterbitkan khusus bagi arsitek uji AI untuk dieksekusi secara otonom dalam alur pengujian FP Python.*
