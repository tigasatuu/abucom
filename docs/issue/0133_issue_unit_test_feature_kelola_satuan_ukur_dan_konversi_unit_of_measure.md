# Issue: Unit-Test Feature Kelola Satuan Ukur dan Konversi Unit of Measure

## 1. Persona Ekskutor
**Peran:** Senior QA Automation Engineer & AI Testing Agent
**Deskripsi:** Anda adalah pakar pengujian perangkat lunak tingkat lanjut yang menguasai implementasi `pytest`, pengujian murni fungsi logika (Functional Programming), mocking data deterministik, dan Boundary Value Analysis (khususnya untuk presisi desimal `Decimal(15,4)`). Anda memiliki standar tinggi dengan target *code coverage* $\ge 90\%$ tanpa ada kode yang dibiarkan 'to-do' atau menggantung.

## 2. Referensi Utama
- **Dokumen Basis:** `docs/sdlc/05_testing/01_test_plan.md`
- *Catatan: Dokumen `narasi.txt` diabaikan karena rujukan di dalam `01_test_plan.md` sudah sangat komprehensif terkait prosedur dan batasan pengujian (Bab 3.1.1 Unit Testing, Bab 6 Presisi Desimal).*

## 3. Ekstraksi dan Rangkuman Detail Referensi
Dari dokumen referensi `01_test_plan.md`, standar pengujian unit yang wajib diikuti meliputi:
- **Framework Utama:** Menggunakan `pytest` dan `coverage.py`.
- **Target Coverage:** Wajib $\ge 90\%$ untuk modul logika murni.
- **Pendekatan (White-Box Testing):** Pengujian unit dikhususkan pada *pure logic functions* (terbebas dari efek samping database/I/O).
- **Struktur Data:** Menggunakan *mock data structures* seperti `NamedTuple`/`Tuples` untuk menjamin hasil yang deterministik.
- **Presisi Desimal:** Semua perhitungan rasio konversi unit (misal: lembar ke rim, liter ke ml, meter persegi) WAJIB menggunakan tipe data `Decimal` dari modul built-in Python, bukan `float`. Format standar adalah `Decimal(15,4)` dengan pembulatan `ROUND_HALF_UP`.
- **Integritas:** Test suite tidak boleh bergantung pada file eksternal selain konfigurasi *mock* saat testing.

## 4. Batasan, Cakupan, dan Alur Pengerjaan
**Cakupan (In-Scope):**
- Fungsi pembuatan dan validasi master satuan ukur (Unit of Measure / UoM).
- Fungsi perhitungan logika konversi UoM ke UoM turunan/dasarnya (misal: Rim -> Lembar, Meter Persegi -> CM Persegi).
- Validasi batasan presisi desimal saat rasio konversi sangat kecil atau sangat besar.

**Batasan (Out-of-Scope):**
- Tidak perlu melakukan koneksi ke database MySQL betulan (`abucom_test_db`).
- Tidak menguji antarmuka pengguna UI/CLI secara visual.

**Alur Pengerjaan:**
1. Inisialisasi struktur *mocking* untuk UoM.
2. Penulisan test case berdasarkan *boundary analysis* dan standar bisnis.
3. Eksekusi pengujian dengan `pytest`.
4. Pelaporan dan pengecekan tingkat *coverage*.

## 5. Isolasi dan Keamanan Lingkungan Uji
Setiap kasus uji (test case) wajib **terisolasi secara ketat**.
- Dilarang keras melakukan manipulasi *state* variabel global tanpa *teardown* yang memadai.
- Wajib menggunakan fitur `@pytest.fixture` atau blok `setup/teardown` khusus untuk memastikan inisialisasi data UoM *mock* terbebas dari intervensi test case lain.
- Test ini dijamin tidak menyenggol logika modul lain (seperti modul transaksi kasir atau modul produksi).

## 6. Jaminan Kualitas dan Kelengkapan
- Eksekutor wajib menulis seluruh kodenya hingga beroperasi sempurna. Dilarang keras menggunakan implementasi parsial.
- Dilarang meninggalkan blok komentar kode seperti `# TODO: tambahkan skenario ini nanti`.
- Pastikan semua *exceptions* ter-handle dan divalidasi pelemarannya menggunakan `with pytest.raises(...)` yang sesuai dengan standar error kode (seperti `ERR-VAL-XXX`).

## 7. Lokasi Penyimpanan Unit Test
Simpan file skenario pengujian unit ini ke dalam direktori terstruktur:
`tests/unit/test_uom_conversion.py`
*(Jika folder hirarki `tests/unit/` belum ada di root proyek, eksekutor wajib membuatnya terlebih dahulu)*

## 8. Skenario Pengujian (Wajib Dikerjakan Seluruhnya)
Berikut adalah daftar skenario yang wajib diimplementasikan secara teknis:

### A. Skenario Positif (Happy Path)
1. Konversi satuan rasio integer bulat (contoh: 1 Rim = 500 Lembar).
2. Konversi satuan pecahan desimal standar (contoh: 1 Liter = 1000 Ml, 0.5 Liter = 500 Ml).
3. Pembuatan objek data UoM baru dengan karakter string nama yang valid ("Rim", "Lembar", "Meter Persegi").
4. Konversi multi-step/rantai satuan jika struktur hirarkinya mendukung (A -> B, B -> C).

### B. Skenario Negatif / Edge Cases
1. **Konversi Presisi Ekstrim:** Pengujian batas nilai desimal sangat kecil seperti `Decimal('0.0025')` (lihat skenario karet stempel di SDLC Bab 6.1).
2. **Boundary Batas Atas / Overflow:** Mengonversi rasio atau kuantitas dengan nilai finansial/besaran masif mendekati batas `Decimal('99999999999.9999')`.
3. **Pembulatan Uang/Presisi (Round Half Up):** Validasi ketat bahwa konversi yang menghasilkan desimal seperti `.00005` membulat secara benar menjadi `.0001`.
4. **Pembagian dengan Nol (Division by Zero):** Menangani proteksi jika perhitungan algoritma konversi UoM berisiko membagi dengan angka basis/rasio nol.

### C. Validasi Input (Input Validation)
1. **Input Tipe Data Salah:** Memasukkan parameter kuantitas berupa tipe string (contoh: `"10"`) atau `float` standar ke dalam argumen logika konversi yang menghendaki tipe instance `Decimal`.
2. **Kuantitas Negatif:** Validasi bahwa sistem logika menolak mentah-mentah konversi bernilai minus dan otomatis melempar exception spesifik (misal nilai `-5.00` Lembar dilarang).
3. **Nama UoM Ilegal:** Penambahan master UoM dengan nama string kosong `""`, None, atau menggunakan karakter kontrol terminal tak terduga.

## 9. Kebijakan "Clean State"
Seluruh *test function* (fungsi uji) wajib dijalankan secara independen dengan kondisi awal yang bersih (Clean State).
**Instruksi:** Manfaatkan *decorator* `@pytest.fixture` Python bawaan untuk menciptakan *fresh instance* memori terhadap objek "UoM Manager", daftar satuan, maupun tabel rasionya sebelum fungsi `test_...` dijalankan. Jangan gunakan variabel mutabel instansi level-class yang dapat menyusup antar file pengujian sehingga merusak konsistensi hasil.

---

## 10. Low-Level Checklist Pengerjaan (Untuk Eksekutor AI/Junior Programmer)

Wajib mengisi centang `[x]` pada daftar di bawah ini sewaktu mengerjakan implementasi fisik kode untuk mencegah halusinasi tahapan:

- [ ] Membaca parameter dan struktur code base riil dari *feature* "kelola satuan ukur" (file sumber logic-nya) guna mengidentifikasi *function signature* yang akan dites.
- [ ] Memastikan lingkungan *virtual environment* (`venv`) sudah aktif.
- [ ] Menyiapkan folder struktur `tests/unit/` jika direktori tersebut belum eksis.
- [ ] Membuat file pengujian kosong bernama `test_uom_conversion.py` di dalam folder tersebut.
- [ ] **Import Requirements:** Melakukan baris *import* untuk modul `pytest`, library `decimal.Decimal`, beserta file/module logika UoM utama milik aplikasi (contoh: `from logic.uom_manager import ...`).
- [ ] **Setup Fixtures:** Menulis kode `@pytest.fixture` untuk inisialisasi kumpulan mock memori UoM (misal: men-setup dictionary simulasi "Rim" <-> "Lembar" yang nilai rasionya tetap = 500).
- [ ] **Penulisan Test Positif 1:** Membuat fungsi `test_uom_conversion_integer_valid(...)`. Mengimplementasikan `assert` untuk memastikan `1 Rim` berubah tepat menjadi `500 Lembar`.
- [ ] **Penulisan Test Positif 2:** Membuat fungsi `test_uom_conversion_decimal_valid(...)` untuk pengujian unit pengukuran berbasis pecahan.
- [ ] **Penulisan Test Negatif 1:** Membuat fungsi `test_uom_conversion_extreme_decimal(...)` guna menguji input `Decimal('0.0025')` secara akurat.
- [ ] **Penulisan Test Negatif 2:** Membuat fungsi `test_uom_conversion_overflow(...)` guna menguji batas maksimal atas memori kalkulasi.
- [ ] **Penulisan Test Negatif 3:** Membuat fungsi `test_uom_conversion_rounding(...)` untuk jaminan akurasi pembulatan *Round Half Up*.
- [ ] **Penulisan Validasi 1:** Membuat fungsi `test_uom_invalid_string_input(...)` yang dikondisikan melempar error menggunakan blok `with pytest.raises(...)`.
- [ ] **Penulisan Validasi 2:** Membuat fungsi `test_uom_negative_quantity_input(...)` yang diekspektasikan melempar penolakan validasi bisnis nilai minus.
- [ ] **Verifikasi Menjalankan Tes:** Menjalankan perintah terminal `pytest tests/unit/test_uom_conversion.py -v --cov=lokasi/module/logic/uom` untuk memicu tes riil.
- [ ] **Inspeksi Hasil Coverage:** Mengevaluasi log output terminal untuk menjamin persentase skor *coverage* telah sentuh garis hijau aman minimal $\ge 90\%$.
- [ ] **Finalisasi:** Melakukan sanitasi kode tes (membuang `print()` debug sisa, membersihkan *whitespace*, memastikan nama fungsi deskriptif dan konsisten mengikuti *snake_case* PEP-8).
