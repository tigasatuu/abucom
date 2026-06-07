---
issue_id: 0129
title: Unit Test Feature Ubah Password Akun Sendiri
assignee: "Junior Programmer / AI Agent"
persona: "Senior QA Automation Engineer & Principal Python Testing Architect"
reference: "docs/sdlc/05_testing/01_test_plan.md", "docs/sdlc/04_implementation/01_coding_standard.md"
---

# Issue: Perencanaan Unit Test Fitur Ubah Password Akun Sendiri

**Persona Pengeksekusi:** Kamu bertindak sebagai **Senior QA Automation Engineer & Principal Python Testing Architect** yang sangat detail, mematuhi ketat standar SDLC, dan memastikan 100% *code coverage* serta fungsionalitas logika bisnis murni Python berjalan deterministik tanpa efek samping (*side effects*).

## 1. Referensi SDLC
- **Dokumen Utama:** `docs/sdlc/05_testing/01_test_plan.md`
- **Dokumen Pendukung:** `docs/sdlc/04_implementation/01_coding_standard.md`
*(Catatan: File `narasi.txt` diabaikan karena tidak relevan secara spesifik untuk penyusunan pengujian otomatis unit-test logikal).*

### Rangkuman Detail Referensi Spesifik:
1. **Framework Pengujian:** Mewajibkan pemakaian `pytest` sebagai framework penguji utama dan `coverage.py` untuk mengukur tingkat *code coverage* (minimum $\ge 90\%$).
2. **Standard Keamanan:** Pemrosesan otentikasi (seperti ubah password) wajib diverifikasi menggunakan `bcrypt` dengan Hash Cost Factor 12.
3. **Pola Fungsional (FP) & Error Handling:** Fungsi yang diuji dilarang keras berbasis Class/OOP. Penanganan error wajib menggunakan NamedTuple *Result Pattern* (`is_success`, `data`, `error_msg`) dan *state dictionary passing* (`session_state`).
4. **Isolasi Database:** Pengujian unit (*Unit Test*) wajib dipisahkan ketat secara mutlak dari efek I/O database, menggunakan isolasi penuh/mocking data yang deterministik tanpa menyentuh *database* aktual operasional.
5. **Konvensi Penamaan (PEP 8):**
   - File test wajib disimpan di direktori `tests/` dengan nama standar (misal: `tests/test_ubah_password.py` atau digabungkan ke `tests/test_auth_jwt.py`).
   - Penamaan fungsi unit test wajib menggunakan `snake_case` diawali kata `test_`.

## 2. Batasan, Cakupan, dan Alur Pengerjaan
- **Cakupan:** Verifikasi penuh unit test terhadap proses validasi pergantian *password* oleh akun mandiri (validasi *password* lama, syarat policy *password* baru, perbandingan konfirmasi, dan keluaran *bcrypt*).
- **Batasan:** Dilarang mengganggu, merusak, atau menyenggol unit test dari modul lain, termasuk fitur *login* eksisting. Pengujian murni difokuskan pada isolasi modul/fungsi ubah password tersebut.
- **Alur:** Tahapan mengikuti Fase Implementasi 04 menuju Fase Testing 05, wajib memenuhi *Entry* dan *Exit Criteria*.

## 3. Ketentuan Mocking & Isolasi Data (Clean State)
- Setiap skenario uji (Test Case) **WAJIB** menerapkan prinsip *Clean State*.
- Gunakan dekorator fungsi bawaan `@pytest.fixture` untuk menyediakan dan membersihkan (*teardown*) status simulasi awal pada masing-masing tes, sehingga seluruh hasil tes bersifat konsisten dan idempoten jika dijalankan berulang kali.
- Pastikan interaksi baca/tulis terhadap database fisik tidak terjadi di level unit test. Gunakan `unittest.mock` (`patch` atau `MagicMock`) untuk memalsukan koneksi/kursor query (misal `db_connection`) jika alur fungsinya beririsan dengan *layer logic*.

## 4. Lokasi Penyimpanan Unit Test
- **Folder Root:** `tests/`
- **File Target Uji:** `tests/test_[nama_modul_pengubah_password].py`

## 5. Skenario Pengujian (Test Cases)

Semua skenario pengujian komprehensif ini wajib diselesaikan:

### A. Skenario Positif (Positive Cases)
- [ ] **Skenario:** *Password* lama diinput benar, *password* baru memenuhi standar kebijakan minimum dan konfirmasi *password* persis sama. Hasil mengembalikan `Result(is_success=True, ...)` disertai *hash bcrypt cost 12* yang tergenerate sempurna.

### B. Skenario Negatif / Edge Cases (Negative Cases)
- [ ] **Skenario:** Input *password* lama **salah/tidak cocok** dengan data tersimpan di memori saat ini (wajib mengembalikan error `ERR-AUTH`).
- [ ] **Skenario:** Input konfirmasi *password* baru **berbeda** dengan input *password* baru (wajib ditolak program secara instan).
- [ ] **Skenario:** Input *password* baru **sama persis** nilainya dengan *password* lama (harus ditolak, memicu pesan error tidak ada perubahan).

### C. Validasi Input (Input Validation)
- [ ] **Skenario:** *Password* baru kurang dari batas minimal karakter (misalnya kurang dari 6 karakter).
- [ ] **Skenario:** Terdapat input string kosong, nilai *None*, atau *whitespace* murni pada parameter input saat pengubahan *password*.
- [ ] **Skenario:** *Password* melebihi limit batas logis normal yang dapat di-*hashing* (opsional menyesuaikan batasan panjang bcrypt standar jika diperlukan).

## 6. Kualitas Kelengkapan Pengerjaan (Quality Assurance)
- Pengerjaan ini **DILARANG KERAS** menyisakan fungsi bernilai sekadar `pass`, meninggalkan komentar `# TODO:`, atau instruksi yang menggantung/belum sempurna.
- Eksekusi wajib utuh secara tuntas menggunakan asersi logis bawaan pytest (`assert`) untuk mencocokkan tiap kondisi harapan terhadap hasil nyata `Result.is_success` dan `Result.error_msg`.

---

## 7. Checklist Tahapan Pengerjaan Low-Level (Langkah Eksekusi)

*(Ikuti langkah berikut secara linier, dan beri tanda `[x]` untuk mengkonfirmasi keberhasilan eksekusi).*

### Fase 1: Persiapan dan Inisialisasi
- [ ] Lakukan inisialisasi awal (*discovery*) dan baca file sumber fungsi pengubah *password* di dalam *layer* `logic/`.
- [ ] Buat file unit test baru di lokasi `tests/` atau modifikasi file uji eksisting yang menaungi modul otentikasi.
- [ ] Deklarasikan *import* wajib: pustaka dasar bawaan Python, `pytest`, utilitas enkripsi sandi (*bcrypt/crypto helper* lokal), tipe kembalian data (`Result`), dan fungsi *logic* bisnis murni yang akan dites.
- [ ] Buat *mock data* `dummy_session_state` menggunakan `@pytest.fixture` untuk merepresentasikan sesi akun *user* aktif yang valid secara semu (*dummy JWT-like claims*).
- [ ] Buat utilitas `@pytest.fixture` atau `mock_db_cursor` jika implementasi dari modul aslinya mengharuskan injeksi dependensi kursor akses data.

### Fase 2: Penulisan Skenario Tes
- [ ] **Kode Skenario Positif:** Implementasikan `test_ubah_password_sukses()`. Asersikan (*assert*) `is_success == True` dan pastikan data barunya berisi *password hash* `bcrypt` sah (diawali dengan penanda prefix hash baku `$2b$12$...`).
- [ ] **Kode Skenario Sandi Lama Salah:** Implementasikan `test_ubah_password_gagal_sandi_lama_salah()`. Asersikan gagal beserta kembalian valid `ERR-AUTH` terkait penolakan kredensial.
- [ ] **Kode Skenario Konfirmasi Beda:** Implementasikan `test_ubah_password_gagal_konfirmasi_tidak_cocok()`. Asersikan gagal pada ketidakcocokan nilai sandi baru.
- [ ] **Kode Skenario Sama Persis:** Implementasikan `test_ubah_password_gagal_sandi_baru_sama_dengan_lama()`. Asersikan error spesifik sesuai panduan bisnis/logic fungsi aslinya.
- [ ] **Kode Skenario Validasi String Kosong:** Implementasikan `test_ubah_password_gagal_input_kosong()`. Asersikan validasi kegagalan untuk field *password* tidak boleh kosong.
- [ ] **Kode Skenario Validasi Panjang Teks:** Implementasikan `test_ubah_password_gagal_panjang_minimal()`. Asersikan validasi batas huruf minimum.

### Fase 3: Verifikasi Konsistensi (*Clean State*) & Finalisasi
- [ ] Lakukan *code checking* menyeluruh untuk memastikan sama sekali **TIDAK ADA** *state global* variabel di luar lingkup fungsional yang berubah/termutasi oleh eksekusi.
- [ ] Verifikasi dan pastikan eksepsi tak tertangani (`unhandled exceptions`) tidak bocor. Semua kesalahan bisnis harus ditangkap dan dienkapsulasi dengan tenang dalam instansiasi tipe data *Result pattern*.
- [ ] Jalankan manual pengujian (secara simulatif via *test command*) menggunakan *CLI bash* `pytest tests/[nama_file_test].py -v` lalu pastikan *All Passed* berwarna hijau.
- [ ] (Opsional) Lakukan validasi tingkat jangkauan dengan *CLI* `pytest --cov=logic tests/` untuk memastikan bahwa coverage skenario menyentuh seluruh percabangan `if/else` pada fungsi "ubah password akun sendiri".

---
**-- END OF PLANNING --**
