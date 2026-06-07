---
judul      : Unit-Test Feature Dashboard Ringkasan Harian per Role
target_file: tests/logic/test_dashboard_ringkasan_harian.py
referensi  : docs/sdlc/05_testing/01_test_plan.md, docs/sdlc/02_analysis/
persona    : Senior QA Engineer / SDET (Software Development Engineer in Test)
---

# Issue: Pembuatan Unit Test untuk Feature Dashboard Ringkasan Harian per Role

## 1. Konteks dan Persona
**Persona Eksekutor:** Senior QA Engineer / SDET (Software Development Engineer in Test) yang memiliki pemahaman mendalam tentang ekosistem `pytest`, teknik *mocking* secara terisolasi, dan berorientasi pada standar kualitas tinggi tanpa halusinasi.

**Tujuan:** Mengimplementasikan *unit test* yang komprehensif untuk fitur "Dashboard Ringkasan Harian per Role" (mencakup 8 peran: pemilik, kepala_percetakan, kasir, desainer, produksi_cetak, fotocopy_print, gudang, teknisi/pramuniaga). Pengujian ini berfokus pada logika bisnis (berada di lapisan `logic/`) secara terisolasi.

## 2. Referensi & Standar SDLC Utama
Berdasarkan `docs/sdlc/05_testing/01_test_plan.md`, standar pembuatan *unit test* yang wajib dipatuhi:
- **Framework:** `pytest`
- **Coverage:** Wajib menggunakan `coverage.py` dengan target kualitas metrik *code coverage* logika bisnis inti $\ge 90\%$.
- **Karakteristik Pengujian:** *White-Box Testing* untuk menguji jalur logika (*control flow*), penanganan *exception handling*, dan *boundary cases*. Pengujian dilakukan secara deterministik (*pure functions*) yang terbebas dari efek samping I/O database, menggunakan *mock data structures* (NamedTuple/Tuples/MagicMock).
- **Isolasi & State:** 100% *unit test* dilarang melakukan koneksi langsung ke MySQL `abucom_test_db`. Gunakan injeksi *mock* untuk menggantikan fungsi database connector. Setiap skenario wajib berada dalam *clean state* (bersihkan parameter/mock sebelum skenario dijalankan via *pytest fixture*).

## 3. Cakupan dan Batasan Pengerjaan
1. Hanya berfokus pada pembuatan *unit test* untuk *logic* penyajian ringkasan harian dashboard, bukan *integration test*.
2. Pengujian bersifat terisolasi: Tidak menyenggol fitur lain. Gunakan `unittest.mock` atau `pytest-mock` untuk *mocking* pemanggilan ke fungsi *layer* database.
3. Kualitas Ketat: Penyelesaian kode harus **KOMPLIT**, dilarang keras meninggalkan komentar `TODO` atau *placeholder* yang belum diimplementasi. Jika ada kasus *edge-case*, implementasikan asersi-nya secara langsung.
4. Folder Penyimpanan: Letakkan berkas *unit test* di dalam folder `tests/logic/` dengan konvensi penamaan standar Python `test_<nama_modul>.py`.

## 4. Alur Kerja dan Skenario Pengujian (Test Scenarios)

Implementasikan skenario pengujian dengan lengkap. Wajib mencakup kategori berikut:

**A. Skenario Positif:**
- Verifikasi output dashboard untuk masing-masing 8 role dengan data transaksi aktif yang ter-mock sempurna.
- Verifikasi filter/agregasi data berjalan benar (misal: Kasir hanya melihat kas shift berjalan, Pemilik melihat Laba/Rugi keseluruhan).

**B. Skenario Negatif / Edge Cases:**
- Verifikasi dashboard untuk *role* dengan data harian kosong (*zero state*/tidak ada transaksi hari ini).
- Verifikasi perilaku fungsi jika terdapat role yang tidak dikenali (*invalid role* / belum ada otorisasi).
- Verifikasi perhitungan desimal atau uang dengan nilai sangat kecil / pecahan (pembulatan `ROUND_HALF_UP`).
- Verifikasi penanganan ketika terjadi kesalahan dari fungsi database ter-mock (misal fungsi *fetch* melempar exception).

**C. Validasi Input:**
- Verifikasi keamanan input terhadap injeksi karakter tidak valid pada parameter pemanggilan fungsi *logic*.

---

## 5. Checklist Tahapan Eksekusi Low-Level

Silakan ikuti instruksi *checklist* ini tahap demi tahap secara berurutan. Dilarang melompati *checklist* untuk menghindari error atau halusinasi sistem.

- [ ] **1. Persiapan Lingkungan dan Impor (Initialization)**
  - [ ] Buat berkas baru di `tests/logic/test_dashboard_ringkasan_harian.py`.
  - [ ] Impor modul `pytest`.
  - [ ] Impor fungsi *logic* dashboard yang akan diuji dari modul sumber (misal `logic.dashboard`).
  - [ ] Impor utilitas `unittest.mock.patch` atau `MagicMock` untuk *mocking*.

- [ ] **2. Pembuatan Fixtures (Clean State Initialization)**
  - [ ] Buat *fixture* pytest (`@pytest.fixture`) bernama `clean_mock_data` untuk mereset dan menyiapkan set data *mock* yang bersih (*clean state*).
  - [ ] Buat *fixture* untuk merepresentasikan session JWT per peran (8 role) yang dikirim ke *logic*.

- [ ] **3. Implementasi Skenario Positif (Positive Cases)**
  - [ ] Tulis `test_dashboard_pemilik_sukses`: *Mock* data omset, kas, L/R harian. *Assert* bahwa *logic* mengembalikan struktur data ringkasan utuh (semua parameter terisi untuk pemilik).
  - [ ] Tulis `test_dashboard_kepala_percetakan_sukses`: *Assert* pengembalian antrian desain dan stok limit.
  - [ ] Tulis `test_dashboard_kasir_sukses`: *Assert* perhitungan uang di laci dan mutasi kasir yang sedang *login*.
  - [ ] Tulis `test_dashboard_desainer_sukses`: *Assert* data khusus untuk KPI atau antrian khusus desain.
  - [ ] Tulis `test_dashboard_produksi_cetak_sukses`: *Assert* antrian siap produksi/cetak.
  - [ ] Tulis `test_dashboard_fotocopy_print_sukses`: *Assert* output ringkasan ritel cepat.
  - [ ] Tulis `test_dashboard_gudang_sukses`: *Assert* informasi *stock opname* dan barang hampir habis (< 7 hari).
  - [ ] Tulis `test_dashboard_teknisi_pramuniaga_sukses`: *Assert* antrian servis PPOB atau servis unit.

- [ ] **4. Implementasi Skenario Edge Cases (Zero State & Boundary)**
  - [ ] Tulis `test_dashboard_transaksi_kosong`: *Mock* fungsi *fetch* mengembalikan tabel kosong. *Assert* bahwa output menunjukkan angka 0 secara konsisten (tidak melempar error *NoneType* / deviasi).
  - [ ] Tulis `test_dashboard_pembulatan_desimal_hpp`: *Mock* data uang pecahan. *Assert* `ROUND_HALF_UP` bekerja mengembalikan desimal presisi tetap 4 angka di belakang koma.

- [ ] **5. Implementasi Skenario Negatif (Exception & Invalid Input)**
  - [ ] Tulis `test_dashboard_invalid_role`: Kirimkan token dengan peran `'anonim'` atau string kosong. *Assert* bahwa sistem melempar Exception yang sesuai (misal error otorisasi/RBAC).
  - [ ] Tulis `test_dashboard_database_mock_error`: Paksa *mock* fungsi *fetch* melempar `DatabaseError`. *Assert* *logic* menangkapnya dan mengembalikan struktur error terstandardisasi atau di-*raise* dengan benar.

- [ ] **6. Verifikasi & Asersi Final**
  - [ ] Pastikan seluruh blok *test* memanggil *fixture* pembersih.
  - [ ] Jalankan modul uji secara mental (*dry-run logic*) pastikan konvensi nama dimulai dengan `test_`.
  - [ ] Pastikan tidak ada fungsi yang ditinggal dengan isi `pass` atau `TODO`.

## 6. Kriteria Penerimaan Selesai (Definition of Done)
1. Berkas unit test tercipta sesuai letak target.
2. Skenario positif untuk 8 role, *zero-state*, desimal, dan exception sudah diimplementasikan semua (100% *coverage* yang diharapkan tercapai dari unit test ini).
3. Menggunakan *mocking* terisolasi tanpa query database fisik.
4. Siap dijalankan (*runnable*) dengan perintah `pytest tests/logic/test_dashboard_ringkasan_harian.py --cov=logic`.
