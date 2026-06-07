# Issue: Unit-Test Feature Sanitasi Input CLI Anti-Injection

## 1. Persona Pelaksana
**Senior QA Automation Engineer & Security Tester**
(Bertanggung jawab penuh, berotoritas, teliti dalam pengungkapan celah keamanan, dan ahli merancang *Unit Test* murni menggunakan paradigma Pemrograman Fungsional dan Pytest).

## 2. Referensi Dokumen Utama (SSoT)
Gunakan dokumen-dokumen berikut di dalam direktori `docs/sdlc/` sebagai pedoman standar mutlak:
- `docs/sdlc/05_testing/01_test_plan.md`
- `docs/sdlc/05_testing/02_test_cases.md`
- `docs/sdlc/04_implementation/01_coding_standard.md` (Khusus Bab 14. Standar Pengujian, Bab 10.5 Aturan Sanitasi Input CLI, dan Pola Error Handling Fungsional Bab 2.2.6)

*(Catatan: Abaikan file `narasi.txt` karena konteks ini lebih bersifat perancangan teknis pengujian unit di level sistem).*

## 3. Ekstraksi Standar & Rangkuman Detail 
Instruksi mendasar yang perlu dipatuhi berdasarkan referensi:
- **Framework & Coverage**: Wajib menggunakan framework `pytest` murni dan `coverage`. Target *code coverage* dari fungsi target (sanitasi) minimal mencapai $\ge 90\%$.
- **Paradigma**: Wajib menerapkan Pemrograman Fungsional murni. Unit test tidak boleh menggunakan kelas (OOP), terisolasi seratus persen, deterministik, dan tanpa menyentuh *I/O (print)* atau modul eksternal.
- **Pola Penanganan Kesalahan**: Fungsi dari layer logic/utils harus selalu me-return pola *Result* (NamedTuple berupa `is_success`, `data`, `error_msg`) alih-alih melempar exception `try-except`. Oleh karena itu, *assertion* unit test harus ditargetkan ke dalam tupel ini.
- **Konvensi Nama File & Fungsi**: File test wajib diawali `test_<nama_file>.py` dan penamaan fungsi wajib detail dan menggunakan format `snake_case` contoh: `test_sanitasi_hilangkan_ansi_escape_sukses()`.

## 4. Batasan, Cakupan, dan Alur Pengerjaan
- **Cakupan**: Hanya menguji komponen *pure function* pengaman input terminal yang bertanggung jawab menetralisir pola bahaya (karakter ANSI escape `< \x20` dan percobaan injeksi muatan karakter ilegal SQL).
- **Batasan**: Dilarang mengimpor atau melibatkan instansiasi dari database riil (`db_connector.py`) maupun terminal *UI rich* dari direktori `cli/`. Modul tes benar-benar hanya mensimulasikan nilai *string* di memori RAM dan menguji keluarannya.
- **Alur Pengerjaan**:
  1. Siapkan struktur *fixture* dummy dan impor fungsional target dari layer `logic/`.
  2. Implementasikan skenario *Positif*, *Negatif*, dan *Anti-Injection*.
  3. Lakukan proses *assertions*.
  4. Lakukan pembersihan status agar pengujian tidak bersentuhan.
  5. Verifikasi kualitas lewat pembacaan laporan `coverage`.

## 5. Isolasi Mutlak dan Penggunaan Mocking
- Pekerjaan diwajibkan menjamin fitur lain tidak "tersenggol". Tes berjalan sangat terisolasi.
- Jika ada parameter *state* dari objek lain yang diperlukan, wajib gunakan pembuatan *Mock Data* tipe `NamedTuple` yang *immutable* (hanya dibaca). Modifikasi data hanya dalam memori tanpa menyentuh keadaan sistem di luar pengujian.

## 6. Jaminan Kualitas Kelengkapan
- Pengerjaan issue harus tuntas di dalam satu proses eksekusi kode.
- **DILARANG KERAS**: Meninggalkan blok kode `pass`, metode penanda *TODO*, fungsi setengah jadi, atau kode pengujian dengan indikator *SKIP*. Seluruh skenario wajib direalisasikan agar tidak menahan pergerakan penyelesaian fitur utama berikutnya. Exit code `pytest` harus bernilai absolut kelulusan mutlak (0 Error, 0 Failure).

## 7. Lokasi Penyimpanan & Dependencies
- **Folder Penyimpanan**: Di dalam direktori standar `tests/`
- **Target File**: Sesuaikan dengan format konvensi (misalnya `tests/test_safety_validator.py` atau `tests/test_sanitizer.py`).
- **Dependency Utama**: `pytest` dan `coverage` (pastikan kompatibel dengan versi yang terkunci di dalam file `requirements.txt`).

## 8. Skenario Pengujian Unit (Test Scenarios)
Bangun dan siapkan ragam kasus uji komprehensif, sedikitnya mencakup:

### A. Skenario Positif (Normal Workflow)
- Input berupa karakter alfanumerik biasa (seperti `"nama", "123", "budi santoso"`). Pastikan output dikembalikan tanpa dipangkas/diganggu.
- Assert return wajib mengembalikan `Result(is_success=True, data="...", error_msg=None)`.

### B. Skenario Negatif / Edge Cases (Abnormal/Type Errors)
- Input bernilai *string* kosong `""` atau berisi sepasi tak terlihat `"    "`.
- Input yang tipe datanya tidak sesuai parameter (*None*, *Integer*, *List*). Fungsi target wajib secara aman memberikan return `Result` berisi `is_success=False` dan terdapat awalan kode standar error seperti `ERR-VAL-XXX`.
- Panjang input di atas batas kewajaran maksimum parameter memori.

### C. Validasi Anti-Injection (Security Target)
- Mengandung muatan berbahaya karakter pelarian ANSI *Escape Terminal* (*contoh: `\x1b[31m`, karakter `\033`, atau `Null Byte \x00`*). Pastikan karakter direstriksi (*stripped*) oleh *filter byte* `< \x20`.
- Memasukkan string *SQL Injection payload* tingkat dasar hingga menengah (contoh: `' OR 1=1 --`, `'; DROP TABLE pengguna;--`, `" UNION SELECT * FROM--`). Pastikan string ini dibersihkan, ditolak secara total, atau dibuktikan telah lolos validasi aman (*escaped*) di dalam status respons pengujian.

## 9. Kebijakan Clean State Eksekusi Test
- Setiap fungsi tes **WAJIB** berada di dalam titik nol dan *Clean State*.
- Sisipkan inisialisasi reset variabel sebelum memanggil ulang fungsi (atau gunakan fungsionalitas `pytest.fixture(autouse=True)`) agar jejak memori pada sesi pengujian injeksi SQL di langkah sebelumnya tidak membocorkan state kepada skenario tes uji *Edge Case* selanjutnya, demi mempertahankan *pure functions*.

## 10. Kaidah dan Konvensi Koding (Unit Test Spesifik)
- Penggunaan Type Hints PEP 484 mutlak di dalam file pengujian (Misal: `def test_nama_fungsi() -> None:`).
- *Assertion* error tidak mengecek `Exception Error / raise ValueError`, melainkan melakukan asersi parameter `error_msg` pada struktur *NamedTuple* `Result` program AbuCom.
- Nama fungsi asersi gunakan bahasa deskriptif penuh: `test_ketika_input_injeksi_diberikan_maka_return_false_dan_err_val()`.

---

## 11. Low-Level Checklist Eksekusi (Panduan Sistematis)
Instruksi mendetail berikut bertujuan menghindari asisten/junior developer dari halusinasi dan kebingungan. Tandai checkbox saat eksekusi.

- [ ] **1. Inisialisasi dan Penyelidikan Struktur**
  - [ ] Temukan posisi dan lakukan tinjauan langsung (baca file) implementasi file sanitasi di `logic/`.
  - [ ] Petakan seluruh *signature* input dan bentuk kembalian (*Return tuple Result*) dari fungsi tersebut.
- [ ] **2. Setup Kerangka Tes Dasar**
  - [ ] Buat satu file pengujian baru secara eksplisit di direktori `tests/` sesuai penamaan konvensi sistem `test_... .py`.
  - [ ] Lakukan impor komponen penanganan logis `Result`, `Decimal` (jika ada), serta fungsi dari modul `logic`.
  - [ ] Tambahkan komentar *Docstring module* sesuai standar PEP 257.
- [ ] **3. Implementasi State Manajemen (Clean State)**
  - [ ] Siapkan konfigurasi `setup` fungsi tes atau dekorator `@pytest.fixture` untuk mereset dan memanggil status awal objek tiruan (mock dummy).
- [ ] **4. Penyusunan Skenario Positif**
  - [ ] Definisikan `def test_sanitasi_teks_alfanumerik_normal_return_true() -> None:`
  - [ ] Buat asersi perbandingan bahwa string aktual di dalam parameter `Result.data` sama persis dengan yang dikirim dan `Result.is_success` bernilai `True`.
- [ ] **5. Penyusunan Skenario Negatif (Edge Case)**
  - [ ] Eksekusi pemanggilan input `None`, variabel kosong `""`, dan integer rawan.
  - [ ] Asersi terhadap `Result.is_success` berstatus `False` dan mengecek format string deskriptif `Result.error_msg`.
- [ ] **6. Penyusunan Celah Anti-Injection & Pembersihan ANSI**
  - [ ] Uji dan tembak fungsi tersebut dengan `payload = "\x1b[31minput_kotor\x00"` dan pastikan data hasil return bebas dari byte ANSI tersebut.
  - [ ] Susun *SQL Injection queries text* ke argumen dan validasi bahwa modul pengaman sukses menetralisirnya.
- [ ] **7. Verifikasi dan Evaluasi Kebersihan Tes**
  - [ ] Tinjau seluruh skrip, pastikan tanpa sisa baris kode fungsi `to-do` atau impor modul terminal layer / koneksi database.
- [ ] **8. Proses *Run* Eksekusi & Validasi**
  - [ ] Jalankan modul pengujian melalui terminal instruksi murni secara lokal: `pytest tests/test_nama_file.py -v`.
  - [ ] Bangkitkan dan baca cakupan baris lewat command: `coverage run -m pytest tests/` lalu `coverage report -m`.
  - [ ] Jika baris instruksi logika belum ter-cover $\ge 90\%$, perbaiki dan tambahkan simulasi skenario lain hingga lengkap.
