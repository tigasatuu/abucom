---
title: "Unit Test Feature Catat Riwayat Harga Beli Supplier"
assignee: "@junior_programmer / @ai_agent"
labels: ["unit-test", "qa", "backend"]
---

## 1. Persona Eksekutor
**Senior QA Automation Engineer & Python Backend Expert**. Anda memiliki otoritas penuh dalam memastikan kualitas kode, sangat ketat terhadap standar *Test-Driven Development* (TDD), teliti terhadap *edge-cases*, serta sangat ahli dalam menggunakan framework `pytest` dan teknik *mocking* di ekosistem Python.

## 2. Referensi Dokumen SDLC
Pengerjaan issue ini wajib berpedoman pada dokumen berikut:
- `docs/sdlc/04_implementation/01_coding_standard.md` (Bagian 14: Aturan Unit Testing & Framework)
- `docs/sdlc/05_testing/01_test_plan.md` (Bagian 11.3.1: Framework Unit Testing)

## 3. Rangkuman Detail & Aturan Standar Eksekusi (Berdasarkan SDLC)
- **Framework Utama**: Wajib menggunakan `pytest==8.2.1` (atau versi stabil terbaru di venv).
- **Target Coverage**: Kerapatan jangkauan pengujian unit (*Code Coverage*) **MUST** mencapai minimal **90%** untuk keseluruhan baris logika bisnis.
- **Isolasi Penuh**: Unit testing untuk *pure functions* **MUST** bersifat deterministik, terisolasi penuh, dan **DILARANG KERAS** melakukan koneksi fisik ke database MySQL lokal maupun *file system*. Data uji disuplai melalui teknik *mocking* (misalnya menggunakan *NamedTuples* atau `unittest.mock`).
- **Lokasi Penyimpanan**: Seluruh berkas pengujian unit wajib ditempatkan di dalam folder `tests/`.
- **Konvensi Penamaan**: Fungsi pengujian wajib diawali dengan prefix `test_`.
- **No Side Effects**: Wajib menghindari mutasi data global (*side effects*) yang dapat memicu anomali. Setiap skenario pengujian harus dapat berjalan secara independen tanpa bergantung pada urutan eksekusi.

## 4. Batasan & Cakupan Pengerjaan
- Pengerjaan issue ini murni **hanya** berfokus pada perancangan dan penulisan **Unit Test** untuk fitur "Catat Riwayat Harga Beli Supplier".
- Pastikan pengerjaan issue ini terisolasi dan **tidak menyenggol atau merusak** *feature* lain. Jika ada kebergantungan (dependency) ke modul lain, wajib gunakan *mocking*.
- Kualitas kelengkapan pengerjaan **harus 100% komplit**. Dilarang meninggalkan fungsi *dummy*, fungsi yang hanya berisi `pass`, atau tag `TODO` yang menggantung agar tidak menghambat pengembangan *feature* lainnya.

## 5. Skenario Pengujian Minimum (Wajib Dicakup)
Silakan kembangkan lebih lanjut sesuai kebutuhan logika fungsi utama, namun setidaknya skenario-skenario di bawah ini **wajib** dicover:

### A. Skenario Positif
- [ ] Menyimpan data riwayat harga beli supplier baru dengan parameter input yang valid.
- [ ] Mengambil daftar/list riwayat harga beli berdasarkan `ID_Supplier` tertentu secara akurat.
- [ ] Menambahkan *update* riwayat harga baru ke supplier yang sudah ada, dan memastikan *historical data* (riwayat lama) tetap utuh/tercatat.

### B. Skenario Negatif & Edge Cases
- [ ] Mencoba menyimpan riwayat harga dengan `ID_Supplier` yang tidak terdaftar, kosong, atau *fiktif*.
- [ ] Mengambil riwayat harga dari supplier yang belum pernah memiliki transaksi/riwayat sama sekali (sistem harus mengembalikan struktur data kosong atau merespons dengan state yang benar tanpa *crash*).
- [ ] Menginput harga beli dengan nilai tidak wajar/ekstrem (misal: harga `0`, angka negatif, atau panjang digit maksimal yang harus ditolak secara gracefully oleh sistem).
- [ ] Menyimulasikan kondisi error internal (misal: database/sistem gagal memproses) menggunakan *mocking* untuk melihat apakah *exception handling* sudah tertangani dengan baik.

### C. Validasi Input
- [ ] Menguji penyimpanan data dengan tipe data *field* yang salah (misalnya parameter harga diisi tipe *string* "seribu", bukan *float/integer*).
- [ ] Menguji penyimpanan data jika terdapat *mandatory fields* (kolom wajib) yang disuplai dengan nilai `None` atau kosong.

## 6. Persyaratan Eksekusi Test (Clean State)
Setiap skenario test **WAJIB** melakukan pembersihan/reset data terlebih dahulu (*clean state* / *teardown*) sebelum maupun sesudah dijalankan agar hasilnya selalu konsisten (*idempotent*). 
- Gunakan fitur *fixture* dari `pytest` (misalnya *yield* dengan *teardown* logic, atau blok `setUp/tearDown` dari `unittest`) untuk membersihkan *mock state* yang digunakan di setiap test.

---

## 7. Low-Level Checklist Pengerjaan [ ]
Bagi eksekutor, ikuti tahapan checklist *low-level* berikut secara terurut agar implementasi terstruktur dan menghindari halusinasi/ambiguitas kode:

- [ ] **Tahap 1: Inisialisasi & Persiapan Lingkungan**
  - [ ] Identifikasi dan baca logika fungsi "Catat Riwayat Harga Beli Supplier" yang ada di dalam *source code* (misal di folder `logic/` atau `middleware/`). Pahami alur I/O-nya.
  - [ ] Pastikan environment *testing* sudah aktif dan `pytest` siap digunakan.
  - [ ] Buat atau buka file pengujian unit yang dituju, yaitu `tests/test_riwayat_harga_supplier.py`.

- [ ] **Tahap 2: Setup Mocking & Fixtures (Sangat Penting)**
  - [ ] Implementasikan *fixture* di bagian paling atas untuk menginisialisasi *clean state* setiap kali satu fungsi `test_` hendak dijalankan.
  - [ ] Siapkan objek *mock* data yang valid (seperti input payload dictionary/NamedTuples) untuk simulasi suplai data ke fungsi utama.
  - [ ] Injeksi *mock/patch* pada fungsi database atau ketergantungan eksternal lainnya yang ada di dalam fungsi riwayat harga, agar tes tidak menyentuh database `abucom_test_db` secara langsung jika itu adalah *pure function test*.

- [ ] **Tahap 3: Penulisan Kode Skenario Positif**
  - [ ] Implementasikan fungsi `test_simpan_riwayat_harga_valid()`.
  - [ ] Implementasikan fungsi `test_ambil_riwayat_harga_berdasarkan_supplier()`.
  - [ ] Tulis *assertion* yang secara ketat memvalidasi output/kembalian objek (tipe data maupun nilai yang eksak).

- [ ] **Tahap 4: Penulisan Kode Skenario Negatif & Validasi**
  - [ ] Implementasikan fungsi `test_simpan_riwayat_harga_supplier_tidak_valid()`.
  - [ ] Implementasikan fungsi `test_simpan_riwayat_harga_negatif_atau_nol()`.
  - [ ] Implementasikan fungsi `test_simpan_riwayat_tipe_data_salah()`.
  - [ ] Tulis *assertion* untuk menangkap ekspektasi *Error/Exception* menggunakan blok `with pytest.raises(ExpectedError):`.

- [ ] **Tahap 5: Verifikasi Kualitas & Clean-up**
  - [ ] Cek kembali keseluruhan baris kode, pastikan **TIDAK ADA** fungsi/blok bersyarat dengan perintah `pass` atau `TODO` yang tersisa.
  - [ ] Jalankan pengujian di terminal menggunakan eksekutor: `pytest tests/test_riwayat_harga_supplier.py -v`. Pastikan 100% *PASSED*.
  - [ ] Jalankan laporan coverage: `pytest --cov=logic tests/test_riwayat_harga_supplier.py` (sesuaikan target foldernya) dan pastikan hasil coverage indikator minimum mencapai angka 90%.
  - [ ] Pastikan tidak ada fungsi dari modul/fitur lain di luar riwayat harga yang rusak (terguncang) akibat *side effects* *mocking*.
