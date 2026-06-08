---
judul_issue: "Unit-Test Feature Kelola Data Master Supplier"
target_file: "docs/issue/0137_issue_unit_test_feature_kelola_data_master_supplier.md"
---

# Issue: Pembuatan Unit Test untuk Feature Kelola Data Master Supplier

## 1. Persona Eksekutor
**Senior QA Automation Engineer / Lead SDET (Software Development Engineer in Test)**
Persona ini memiliki otoritas mutlak dalam mendefinisikan, mengarahkan, dan mengeksekusi standar kualitas pengujian perangkat lunak tingkat tinggi. Fokus utamanya adalah pada akurasi, determinisme, isolasi pengujian, dan pencapaian *code coverage* komprehensif ($\ge 90\%$) menggunakan praktik *Functional Programming* murni tanpa efek samping yang tak terkontrol.

## 2. Referensi Utama
Pengembangan unit test ini wajib berpegang pada dokumen standar (SDLC) berikut:
- **`docs/sdlc/03_design/01_database_schema.sql`**: Untuk struktur dan batasan entitas `supplier`.
- **`docs/sdlc/05_testing/01_test_plan.md`**: Untuk standar pengujian (metodologi, alat, dan kriteria).
*(Catatan: File narasi.txt tidak relevan untuk konteks unit test murni ini sehingga diabaikan).*

## 3. Ekstraksi Detail Konteks Berdasarkan Referensi
Berdasarkan dokumen referensi, berikut adalah batasan teknis yang harus dipenuhi oleh kode unit test:

**Struktur Tabel `supplier` (Acuan Mocking/Test DB):**
- `id` (INT, PK, Auto Increment)
- `nama_supplier` (VARCHAR 100, NOT NULL)
- `alamat` (TEXT, NOT NULL)
- `telp` (VARCHAR 30, NOT NULL)
- `email` (VARCHAR 100, NOT NULL)
- `cabang_id` (INT, NOT NULL, DEFAULT 1, FK ke `cabang`)

**Standar Unit Testing (Sesuai SDLC Bab 3.1.1 & Bab 10):**
- **Framework/Dependency:** Wajib menggunakan `pytest` dan `coverage.py`.
- **Pendekatan:** Bersifat deterministik menggunakan *mock data structures* atau database sandbox uji coba terisolasi (`abucom_test_db`).
- **Pembersihan Data (Clean State):** Setiap *test case* **wajib** melakukan *setup* dan *teardown* (menghapus data sebelum dan sesudah eksekusi) agar tidak mengotori *state* dari eksekusi *test case* lainnya. Isolasi *database rollback* per transaksi uji (*ACID compliance*) sangat disarankan.

## 4. Batasan & Cakupan Pengerjaan
1. **Lokasi File:** File pengujian wajib disimpan di folder `tests/unit/` (contoh: `tests/unit/test_master_supplier.py`).
2. **Kemandirian (Isolation):** Pengujian hanya ditujukan pada fungsi bisnis kelola supplier murni. Gunakan **mocking** untuk antarmuka CLI atau koneksi I/O lain di luar *domain logic*. Jangan sampai eksekusi ini menyenggol data transaksional atau stok barang.
3. **Konvensi Penamaan:** Gunakan pola standar pytest `test_<nama_fungsi>_<skenario>`.
4. **Kelengkapan Mutlak:** Tidak boleh ada satupun *stub*, *placeholder*, atau komentar `// TO-DO`. Setiap *test case* wajib terisi penuh dengan *Assertion* yang valid.
5. **Coverage:** *Logic* terkait *supplier* (Create, Read, Update, Delete dan Validatornya) harus memiliki 100% *pass rate* di *Positive* maupun *Negative cases*.

## 5. Skenario Pengujian Minimum
Setiap skenario wajib melakukan pengujian fungsi murni untuk *return value* dan *exception* yang dilempar.

**A. Skenario Positif (Happy Path)**
- [ ] Penambahan data supplier baru dengan input yang lengkap dan valid.
- [ ] Pembacaan/Pencarian data supplier berdasarkan `id` yang valid.
- [ ] Pembacaan list (daftar) seluruh supplier (harus mengembalikan *array/list* kosong jika awal `setup`, dan mengembalikan data yang benar setelah *insert*).
- [ ] Perubahan data (Update) pada `nama_supplier` dan `telp` pada `id` yang valid.
- [ ] Penghapusan data (Delete) supplier berdasarkan `id` yang valid.

**B. Skenario Negatif (Edge Cases & Exception Handling)**
- [ ] Penambahan data dengan `nama_supplier` kosong atau *null*. Harus melempar *error validation*.
- [ ] Penambahan data dengan `telp` kosong. Harus melempar *error*.
- [ ] Penambahan data dengan format `email` yang salah (misal: "supplier-at-gmail"). Harus ditolak.
- [ ] Penambahan data tanpa `cabang_id` (wajib diisi otomatis dengan *default* 1 atau melempar *error* jika disengaja *null* bergantung *logic* bisnis).
- [ ] Pencarian atau Perubahan (Update) data supplier dengan `id` fiktif yang tidak ada di *database* / *mock*. Wajib mengembalikan error `Not Found`.
- [ ] Penghapusan (Delete) data supplier dengan `id` fiktif. Wajib mengembalikan error `Not Found`.

**C. Validasi Input Ekstrem**
- [ ] *Max Length Test*: Input `nama_supplier` berisi lebih dari 100 karakter string. Wajib ditolak.
- [ ] *Max Length Test*: Input `telp` berisi lebih dari 30 karakter karakter. Wajib ditolak.
- [ ] *Injection Sanitization*: Input string yang berpotensi *SQL Injection* (misal `' OR '1'='1`) harus diverifikasi ditangani aman oleh *parameterized queries* (diverifikasi melalui fungsi penyusun *query* atau *mock* panggilannya).

---

## 6. Checklist Eksekusi Low-Level untuk AI Implementer

Berikut adalah tahapan *low-level* pasti yang **TIDAK BOLEH** dilompati:

- [ ] **Inisialisasi Lingkungan Uji:**
  - Pastikan file `test_master_supplier.py` dibuat di folder `tests/unit/`.
  - Lakukan *import* modul `pytest`, `mock` (jika dibutuhkan), dan *logic* master supplier.
- [ ] **Persiapan Fixture & Clean State:**
  - Buat `pytest.fixture` yang mengeksekusi inisialisasi basis data *sandbox* atau struktur data *mock*.
  - Di dalam `fixture`, instruksikan `TRUNCATE TABLE supplier` (jika menggunakan DB tes) atau kosongkan *list dictionary* di setiap awal. Pastikan ada proses *yield* lalu *teardown cleanup*.
- [ ] **Penulisan Logic Uji Skenario Positif:**
  - Tulis fungsi `test_create_supplier_success()`.
  - Tulis fungsi `test_read_supplier_by_id_success()`.
  - Tulis fungsi `test_update_supplier_success()`.
  - Tulis fungsi `test_delete_supplier_success()`.
  - *Assert* setiap hasil fungsi mengembalikan entitas atau boolean `True` sesuai desain arsitektur fungsi.
- [ ] **Penulisan Logic Uji Skenario Negatif & Validator:**
  - Tulis fungsi `test_create_supplier_empty_name_fails()`, *Assert* adanya `Exception` atau `ValueError`.
  - Tulis fungsi `test_create_supplier_invalid_email_fails()`, *Assert* adanya validasi *email regex*.
  - Tulis fungsi `test_update_supplier_not_found()`, *Assert* penanganan jika ID tidak ada.
  - Tulis fungsi `test_delete_supplier_not_found()`, *Assert* bahwa penghapusan ID palsu tidak men-crash program.
- [ ] **Penulisan Validasi Input & Keamanan:**
  - Tulis fungsi `test_supplier_max_length_validation()`.
  - Tulis fungsi `test_supplier_sql_injection_sanitization_handling()`.
- [ ] **Verifikasi & Eksekusi Uji:**
  - Review kode dan pastikan 100% *komplit* (tidak ada *to-do*).
  - Simulasikan *run command* (misal: `pytest tests/unit/test_master_supplier.py -v --cov`).
  - Pastikan setiap fungsi *assert*-nya benar-benar memeriksa kondisi yang krusial.
