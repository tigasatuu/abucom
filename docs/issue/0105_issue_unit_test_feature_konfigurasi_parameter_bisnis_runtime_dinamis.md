# Issue Planner: Unit-Test Feature Konfigurasi Parameter Bisnis Runtime Dinamis

**Persona Pendelegasi:** Senior QA Automation Engineer & Test Strategy Architect
**Ditugaskan Kepada:** Junior Programmer / AI Testing Agent
**Status:** DRAFT / OPEN
**Prioritas:** HIGH
**Target Modul:** M.10 Configs (Konfigurasi Sistem Runtime)
**Referensi Dokumen Utama:** 
- `docs/sdlc/05_testing/01_test_plan.md`
- `docs/sdlc/05_testing/02_test_cases.md`
- `docs/sdlc/03_design/04_cli_interaction_flow.md`
- `docs/sdlc/02_analysis/06_access_control_matrix.md`

---

## 1. Konteks & Ringkasan Spesifikasi
Issue ini bertujuan untuk mengimplementasikan *Unit Testing* pada logika fungsional Modul M.10 (Konfigurasi Parameter Bisnis Runtime Dinamis). Berdasarkan dokumen SDLC, fitur ini mengatur nilai-nilai vital aplikasi seperti UMR, Limit Pengeluaran, dan Harga (Use Case: UC-040, Kebutuhan Fungsional: SRS-F-038).
Sesuai rancangan *Access Control Matrix* (ACM-M10-001), pengelolaan modul ini dikunci ketat khusus untuk peran otorisasi `pemilik`. Unit test ini harus memastikan fungsionalitas dan keamanan dari sisi *logic business* terpenuhi.

## 2. Batasan, Aturan, dan Standar Pengerjaan
Berdasarkan Test Plan SDLC, pengerjaan unit test harus mematuhi kaidah ketat berikut:
1. **Testing Paradigma Fungsional Murni (FP):** Unit test hanya difokuskan pada pengujian *pure functions* (logika bisnis inti). Dilarang keras melakukan koneksi database atau I/O fisik selama *unit test* berjalan.
2. **Isolasi Penuh (Mocking):** Semua panggilan yang berhubungan dengan tabel database `system_configs` atau operasi eksternal WAJIB dilakukan melalui sistem simulasi (menggunakan `pytest-mock` atau library sejenis). Hal ini agar tidak merusak data *test environment* (sandbox) maupun fitur lainnya.
3. **Clean State Wajib:** Setiap test function harus dipastikan terbebas dari sisa *state* test sebelumnya. Wajib melakukan inisialisasi ulang (*setup*) dan pembersihan data/mock (*teardown*) sebelum menjalankan *assertion*.
4. **Target Code Coverage Minimum:** Setiap *pull request* yang berhubungan dengan issue ini, harus menghasilkan persentase cakupan kode minimal $\ge 90\%$.
5. **No TO-DO Allowed:** Pekerjaan harus tuntas, bersih, serta memverifikasi dengan ketat semua nilai pengembalian *(return value)*. Tidak boleh ada implementasi *testing* yang di-*pass* atau diberi status "TODO".
6. **Konvensi Penamaan (Naming Convention):** Semua file test dan nama method harus menggunakan prefix `test_`. Penamaan fungsi test sebaiknya representatif, seperti: `test_<nama_fungsi>_<skenario_kondisi>_<hasil_yang_diharapkan>()`.
7. **Standar Desimal:** Verifikasi dengan teliti ketelitian kalkulasi atau param desimal menggunakan `Decimal` dari library Python dengan tipe `Decimal(15,4)` sesuai parameter SDLC.

## 3. Lokasi Penyimpanan (*Repository File Structure*)
Unit Test wajib ditempatkan pada path yang terstruktur rapi sesuai standar `pytest`:
* **Path Destinasi Unit Test:** `tests/unit/logic/test_m10_runtime_config.py` (Sesuaikan sub-folder jika struktur framework proyek memisahkan lokasi logic secara khusus).
* Jika membuat file *mock data/fixture* pembantu, letakkan pada file khusus misalnya `tests/unit/conftest.py`.

## 4. Skenario Pengujian Minimal (Test Scenarios)
Tuliskan test case di dalam kode sesuai dengan daftar minimal berikut (tambahkan mandiri jika ada *edge-case* yang krusial):

**A. Skenario Positif (Happy Path):**
1. Mampu mengambil *(load)* seluruh data `system_configs` dari *mock cache* / memori tanpa kesalahan format tipe data.
2. Mampu memperbarui *(update)* parameter bisnis spesifik (contoh: menaikkan batas UMR dan memverifikasi nilainya kembali tercatat dalam format `Decimal`).
3. Mampu menolak parameter yang direquest apabila validasi di dalam mock state valid.

**B. Skenario Negatif (Edge Cases & Keamanan):**
1. Uji pemanggilan ubah *(update)* oleh skenario profil pengguna dengan izin **BUKAN** `pemilik` (misal kasir / desainer) -> Ekspektasi harus digagalkan *(Access Denied)*.
2. Uji permintaan pengubahan struktur konfigurasi key yang **TIDAK TERDAFTAR** di dalam daftar `system_configs` standar -> Ekspektasi memicu pelemparan Error spesifik atau menolak update data.
3. Menguji *error handler* internal agar tidak memecah terminal (*crash application*) saat *mock module* mensimulasikan kegagalan I/O.

**C. Skenario Validasi Input (Boundary Validations):**
1. Validasi untuk menolak *update* yang menggunakan nilai string atau huruf saat field sebenarnya bertipe Integer (misalnya untuk batas jumlah hari).
2. Validasi menolak nominal rupiah yang berjumlah **NEGATIF** pada variabel konfigurasi *Limit OPEX*.

---

## 5. Low-Level Execution Checklist (Panduan Implementasi Langkah demi Langkah)
Bagi eksekutor, ikuti tahapan instruksi berikut untuk menyelesaikan issue ini:

- [ ] **Baca Dokumen Kode Sumber:** Pahami fungsionalitas murni modul M.10 di dalam direktori `logic/` (atau direktori bersangkutan) sebelum mulai menulis test.
- [ ] **Buat File Test Target:** Buat file baru pada alamat rute referensi `tests/unit/logic/test_m10_runtime_config.py`.
- [ ] **Import Library Standar:** Lakukan impor pustaka standar (`pytest`, modul `mock`, dan spesifik modul M.10).
- [ ] **Inisialisasi Data Bersih (Fixtures):** Susun fungsi fixture di `pytest` yang mereset dan mem-*mock* kembalian simulasi `system_configs` menjadi format data awal standard yang belum terjamah.
- [ ] **Tulis Skenario A1-A3:** Implementasikan fungsi test blok **Skenario Positif** (load parameter valid, ubah parameter, tes persentase). Tambahkan perintah `assert` yang memvalidasi perbandingan *Old Value* dan *New Value*.
- [ ] **Tulis Skenario B1-B3:** Implementasikan fungsi test blok **Skenario Negatif**. Gunakan blok `pytest.raises` atau periksa pengembalian nilai standar `ERR-AUTH` yang sudah ada untuk mengecek fungsi *RBAC*.
- [ ] **Tulis Skenario C1-C2:** Implementasikan skenario perlindungan input boundary, kirim nilai negatif dan string ke fungsi dan lakukan verifikasi kegagalan secara wajar (*Graceful Error Handling*).
- [ ] **Eksekusi Lokal Terisolasi:** Jalankan perintah `pytest -v tests/unit/logic/test_m10_runtime_config.py`. Pastikan seluruh baris warna hijau (Passed).
- [ ] **Generate Report Coverage:** Eksekusi `pytest` bersama *Coverage Generator* (misal dengan `pytest --cov=logic ...`). Verifikasi hasil menunjukan persentase cakupan kode fungsional $\ge 90\%$.
- [ ] **Penyelesaian:** Bersihkan komentar tak berguna, tidak boleh ada statemen logika `TODO` di dalam berkas unit-test, siapkan commit.
