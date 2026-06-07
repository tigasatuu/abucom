---
judul: "Unit Test Feature Kelola Komposisi BOM Produk Kustom"
target_file: "tests/test_bom_hpp.py"
---

# Issue: Unit Test Feature Kelola Komposisi BOM Produk Kustom

## 1. Persona Eksekutor
**Senior QA Architect & FP Code Quality Lead AI**
Anda adalah entitas AI yang memiliki otoritas teknis tertinggi dalam penjaminan kualitas kode (QA) dan arsitektur pengujian sistem fungsional murni (FP). Tugas Anda adalah mengeksekusi pembuatan Unit Test untuk fitur Kelola Komposisi BOM (Bill of Materials) Produk Kustom dengan tingkat ketelitian presisi finansial yang absolut dan deterministik.

## 2. Basis Dokumen Referensi Utama
Pengujian ini secara ketat mengacu pada dokumen SDLC berikut:
1. `docs/sdlc/05_testing/01_test_plan.md` (Terutama skenario M2-TC-002 dan Presisi Desimal)
2. `docs/sdlc/05_testing/02_test_cases.md` (Terutama kasus uji operasional TC-M2-002-01)
3. `docs/sdlc/04_implementation/01_coding_standard.md` (Bab 2 FP Murni, Bab 7 Type Hints, Bab 8 NamedTuple, Bab 14 Unit Testing)

## 3. Ekstraksi dan Rangkuman Data Konteks (Spesifik BOM)
- **Modul**: M.2 (Manajemen Inventaris & BOM).
- **Target Fungsi**: Logika murni FP kalkulasi HPP produk kustom (misal perhitungan pemakaian `BOMItem` pada fungsi pengelola BOM).
- **Format Data Numerik**: Wajib menggunakan `decimal.Decimal` presisi tetap 4 digit di belakang koma (`0.0000`) dengan aturan pembulatan `ROUND_HALF_UP`.
- **Struktur Data**: Harus bersifat *immutable* menggunakan `collections.namedtuple` (contoh: `BOMItem = namedtuple('BOMItem', ['bahan_baku_id', 'qty_pemakaian', 'harga_beli'])` atau sesuai implementasi sesungguhnya).
- **Formula Bisnis Kalkulasi HPP BOM**: Total HPP = $\sum (\text{Pemakaian} \times \text{Harga Beli})$.
- **Target Mutu**: Mencapai Code Coverage minimal 90% pada logic bisnis komputasi.

## 4. Batasan, Cakupan & Alur Pengerjaan
- **Unit Testing Murni**: Pengujian fungsionalitas harus 100% terisolasi dari operasi I/O nyata (seperti koneksi fisik Database MySQL, pemanggilan eksternal, atau baca-tulis berkas).
- **Data Mocking Terisolasi**: Pengkondisian sistem (state) dan input data harus diinjeksi ke fungsi secara manual dan deterministik menggunakan objek tiruan yang statis (Mock/Fixtures).
- **Kelengkapan Fitur Kode Uji**: Solusi yang dihasilkan harus berspesifikasi *production-ready*. Dilarang menyisakan tugas berstatus 'to-do', meninggalkan fungsi uji tak berdaging (`pass`), atau menghasilkan *false-positive assertions*.

## 5. Lokasi dan Pengaturan Modul Uji
- **Folder dan Berkas Penyimpanan Unit Test**: `tests/test_bom_hpp.py` (Memenuhi aturan penamaan skrip tes).
- **File Target Asal Pengujian**: `logic/bom_hpp.py` (Asumsi modul diimplementasikan di sini).
- **Dependency**: Library framework testing (disarankan standar `pytest` atau `unittest`), serta modul pustaka standar `decimal`.

## 6. Skenario Uji Komprehensif (Wajib Diimplementasikan Lengkap)
Susun minimal metode fungsi pengujian fungsionalitas berikut beserta validasi *assertion* yang presisi:
- [ ] **Skenario Positif (Happy Path)**
  - Uji penghitungan HPP BOM yang sukses dengan multikomponen.
  - *Data referensi (Test Plan TC-M2-002-01)*: Komponen Karet Flash (Pemakaian `0.0025`, Harga `100000.0000`) dan Gagang Stempel (Pemakaian `1.0000`, Harga `4500.0000`).
  - *Asersi*: Perhitungan Total HPP bernilai akurat menghasilkan `Decimal('4750.0000')`.
- [ ] **Skenario Negatif / Edge Cases / Validasi Presisi (Unhappy Path)**
  - Menguji penolakan (exception atau object `Result` error) terhadap *array* BOM kosong tanpa bahan sama sekali.
  - Menguji penolakan validasi input nominal negatif pada argumen pemakaian maupun harga beli bahan baku (contoh harga `-5000`).
  - Menguji penolakan *type mismatch* bawaan (contoh: input nilai uang diberikan dalam tipe `float`, sistem harus mendeteksinya jika validasi ketat atau melempar pengecualian tipe data).
  - Validasi pembulatan *Round-Half-Up* untuk nilai desimal yang menjangkau batas ujung (misal nilai perhitungan pemakaian `0.00005` ke `0.0001`).

## 7. Instruksi Penanganan *Clean State*
- Sesuai prinsip paradigma *Functional Programming*, setiap metode fungsi uji (`test_...`) **WAJIB** memulai pengerjaan dari state yang segar dan independen (*Clean State*).
- Dilarang mendaur ulang data memori mutabel secara global antar fungsi uji. Segala instansiasi *test data* (seperti `BOMItem` dan parameter lainnya) wajib direkonstruksi di dalam cakupan (*scope*) fungsional tiap test case, memastikan tak ada *side-effect* lintas skenario yang memicu hasil manipulatif tak konsisten.

## 8. Checklist Pengerjaan Low-Level (Wajib Diceklis Eksekutor)
Lakukan instruksi tahapan pengerjaan operasional di bawah ini satu-demi-satu dengan standar mutu absolut, tanpa ambiguitas maupun halusinasi fungsi eksternal yang tidak relevan:

- [ ] Lakukan inspeksi struktur pada kode program asal `logic/bom_hpp.py` guna mengidentifikasi *signature* fungsi perhitungan BOM, anotasi argumen, dan nilai pengembalian yang disuplai (`Result` pattern atau sekadar return parameter).
- [ ] Buat dan/atau inisialisasi berkas tes baru di path `tests/test_bom_hpp.py`.
- [ ] Deklarasikan impor seluruh dependensi absolut dan lokal di urutan teratas file (`pytest`, `Decimal`, `ROUND_HALF_UP`, `BOMItem`, dan fungsi target pada file asal).
- [ ] Susun *mock data initialization* deterministik yang direset otomatis di setiap scope eksekusi fungsi.
- [ ] Rancang dan tulis skrip *Skenario Positif* ke dalam blok fungsional khusus (`test_kalkulasi_hpp_bom_sukses`). Pastikan asersi tipe `Decimal` berjalan persis pada kecocokan 4 digit presisi koma.
- [ ] Rancang dan tulis skrip *Skenario Presisi Desimal* ke dalam blok fungsional khusus (`test_kalkulasi_hpp_bom_pembulatan_boundary`) guna menangani pembulatan aritmatika per digit eceran terkecil.
- [ ] Rancang dan tulis skrip *Skenario Validasi Negatif* (`test_kalkulasi_hpp_bom_list_kosong`, `test_kalkulasi_hpp_bom_harga_negatif`). Pasangkan blok `pytest.raises` atau validasi respons status struktur datanya jika memakai wrapper tipe `Result`.
- [ ] Lakukan verifikasi konvensi penamaan (`snake_case`) pada kelas/metode skrip uji sesuai dengan BAB 3 Coding Standard.
- [ ] Simulasikan eksekusi tes dan pastikan seluruh cakupan tercapai.
