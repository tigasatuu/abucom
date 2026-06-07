# Issue: Unit Test Feature Kelola Data Master Barang Retail dan Bahan Baku

## 1. Persona Eksekutor
**Target Persona:** Senior QA Automation Engineer / Lead SDET (Software Development Engineer in Test) AI.
**Karakteristik:** Otoritatif, sangat teliti (detail-oriented), memiliki pemahaman pakar tentang praktik *Test-Driven Development (TDD)*, arsitektur Pemrograman Fungsional (FP) murni, *edge-cases boundary analysis*, dan kepatuhan absolut terhadap standarisasi *Coding Standard* industri (khususnya keamanan, isolasi testing, dan presisi finansial).

## 2. Referensi Utama
Proses pengerjaan issue ini wajib didasari oleh dan tunduk sepenuhnya pada dokumen:
1. `docs/sdlc/05_testing/01_test_plan.md`
2. `docs/sdlc/04_implementation/01_coding_standard.md` (Terutama Bab 14: Standar Pengujian)
3. `docs/sdlc/narasi.txt` (Menjadi basis konteks domain bisnis: pembedaan barang retail ATK, perhitungan komposisi bahan baku percetakan, multi-satuan, ukuran dimensi panjang x lebar).

## 3. Ekstraksi dan Rangkuman Detail SDLC (Konteks Unit Test)
Berdasarkan dokumen referensi SDLC, berikut adalah aturan mutlak yang wajib diterapkan dalam pengerjaan pengujian unit:
* **Framework:** Wajib menggunakan `pytest`.
* **Cakupan Pengujian (Coverage):** Eksekusi *unit test* wajib mencapai minimum **90%** jangkauan baris kode (*Code Coverage*) untuk modul fungsi terkait.
* **Isolasi Penuh (Pure Functions Testing):** Unit testing untuk fungsi logika murni **DILARANG KERAS** melakukan koneksi ke database MySQL fisik atau berinteraksi dengan *file system* lokal (Aturan 14.4 `01_coding_standard.md`).
* **Mocking & Imutabilitas:** Seluruh suplai data atau state (seperti *Session State* atau rincian barang) wajib dilakukan melalui metode injeksi memori menggunakan objek yang sepenuhnya imutabel, yaitu `NamedTuple` atau *dictionary data passing*.
* **Presisi Finansial dan Volume:** Kalkulasi harga, total nilai barang, dan dimensi volume bahan baku **WAJIB** dikonversi menggunakan tipe `decimal.Decimal` presisi 4 desimal (`'0.0000'`) dengan metode pembulatan `ROUND_HALF_UP`.
* **Penanganan Error (Result Pattern):** Pengujian wajib memverifikasi bentuk kembalian fungsi berupa NamedTuple `Result(is_success, data, error_msg)` dan bukan menggunakan *try-except abuse* (*exception runtime*).
* **Lokasi Penyimpanan:** Semua berkas pengujian wajib disimpan di direktori `tests/`.

## 4. Batasan dan Cakupan Pengerjaan (Scope of Work)
* **In-Scope:** Pembuatan rangkaian *unit test logic* murni (pure function) untuk aktivitas pendaftaran, validasi, dan konversi dimensi komputasi barang retail (ATK) maupun bahan baku mentah.
* **Out-of-Scope:** Pengujian *Integration Testing* yang menggunakan layer database (`db_connector.py`) maupun antarmuka visual CLI (Layer 1 Presentation). Issue ini 100% fokus pada *Layer 2 Business Logic*.
* **Kualitas Pengerjaan (Strict Completeness):** Pekerjaan harus selesai secara **KOMPLIT 100%**. Dilarang meninggalkan stub fungsi kosong, komentar *"to-do"*, atau fungsionalitas yang masih menggantung. Hal ini penting agar integrasi dengan modul *Supply Chain* lain tidak terhambat.

## 5. Skenario Pengujian (Test Scenarios)
Setiap pengujian **WAJIB** menerapkan pembersihan/reset data atau instansiasi *clean state* terlebih dahulu di awal fungsi (menggunakan pytest `@pytest.fixture`) agar hasil pengujian konsisten dan tidak terkena efek samping *state pollution*. Skenario harus komprehensif, mencakup (namun tidak terbatas pada):

1. **Skenario Positif:**
   * Validasi fungsi berhasil memproses pembuatan barang retail baru dengan data yang valid.
   * Validasi fungsi berhasil menghitung dimensi bahan baku (panjang x lebar) dengan presisi `Decimal` dengan pembulatan yang benar.
2. **Skenario Negatif / Edge Cases:**
   * Validasi penolakan saat atribut harga beli atau kuantitas bernilai negatif (`< 0`).
   * Validasi sistem berhasil menolak (*is_success=False*) dan memberikan pesan pencegahan `ZeroDivisionError` apabila terjadi perhitungan rasio harga dibagi kuantitas yang bernilai nol.
3. **Validasi Input:**
   * Validasi input menolak karakter *escape* ilegal pada nama barang.
   * Validasi batas karakter (`max_length`) untuk field deskripsi/nama.
   * Pengecekan tipe data yang memastikan argumen finansial tidak diinput menggunakan `float`.

## 6. Checklist Eksekusi Low-Level Markdown
Eksekutor wajib mematuhi *checklist* tahapan detail berikut guna memastikan tidak terjadi halusinasi implementasi dan bebas ambiguitas:

- [ ] **1. Inisialisasi Environment dan Analisis Modul Target**
  - [ ] Baca fungsi-fungsi logika target di direktori `logic/` yang berhubungan dengan kelola master barang.
  - [ ] Pastikan bahwa fungsi target adalah *pure functions* yang mendasari perhitungan bisnis (bukan antarmuka).
- [ ] **2. Pembuatan File dan Konvensi Nama**
  - [ ] Buat berkas baru bernama `tests/test_kelola_master_barang.py` (atau sesuaikan spesifik dengan target modul).
  - [ ] Lakukan impor modul standar yang relevan: `pytest`, `decimal.Decimal`, `collections.namedtuple`, tipe `Result`, dan fungsi target.
- [ ] **3. Pembuatan Fixture (Clean State & Mocking)**
  - [ ] Susun *fixture* `pytest` (`@pytest.fixture`) yang mereturn *state session* atau data struktur dasar barang *mock* (`NamedTuple`).
  - [ ] Pastikan bahwa *fixture* tersebut mengembalikan instansi baru (*fresh object*) di setiap pemanggilan test.
- [ ] **4. Penulisan Kode: Skenario Positif**
  - [ ] Tulis `test_tambah_barang_retail_sukses(fixture_data)` yang menyuplai data valid. Lakukan `assert result.is_success is True`.
  - [ ] Tulis `test_kalkulasi_dimensi_bahan_baku_presisi()` untuk memverifikasi kalkulasi perkalian desimal (15,4).
- [ ] **5. Penulisan Kode: Skenario Negatif & Boundary**
  - [ ] Tulis `test_tambah_barang_harga_negatif_gagal()`. Lakukan `assert result.is_success is False` dan periksa keberadaan *Error Code* (misalnya `ERR-VAL-XXX`) di `result.error_msg`.
  - [ ] Tulis `test_tambah_barang_nama_kosong_gagal()` untuk validasi argumen *string* kosong.
  - [ ] Tulis `test_validasi_pembagian_nol_bahan_baku()` untuk memastikan logika tidak melempar eksepsi *runtime* ketika qty bernilai `Decimal('0.0000')`.
- [ ] **6. Verifikasi Kualitas Akhir dan Assertion**
  - [ ] Periksa ulang apakah nama seluruh fungsi tes telah mematuhi aturan konvensi: `test_<behavior_spesifik>`.
  - [ ] Jalankan modul pengujian (`pytest tests/test_kelola_master_barang.py -v`) dan pastikan `100% PASSED`.
  - [ ] Hitung secara lokal menggunakan `coverage.py`, pastikan rasio minimum menembus `>= 90%`.
  - [ ] Teliti semua baris; pastikan absolut tidak ada fungsi `# TODO` maupun import koneksi DB (misal `db_connector`) di dalam *file test* murni ini.
