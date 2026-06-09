# Issue: Unit-Test Feature Enkripsi dan Dekripsi Nomor WhatsApp Pelanggan

## 1. Informasi Konteks
- **Judul Issue:** Unit-Test Feature Enkripsi dan Dekripsi Nomor WhatsApp Pelanggan
- **Target Pengerjaan:** Eksekusi penyusunan file unit test untuk fungsionalitas enkripsi dan dekripsi Fernet.

## 2. Persona Instruksi Eksekutor
**Instruksi untuk AI:**
Kamu akan bertindak sebagai **Claude Sonnet 4.6 (Thinking)** (berdasarkan narasi.txt: _Deep coding & refactoring_) dengan peran sebagai **Senior QA Engineer & Test Strategy Architect**. Kamu diotorisasi penuh untuk memimpin, mengeksekusi, dan memastikan integritas serta reliabilitas logika kriptografi pada sistem ini secara mutlak.

## 3. Ekstraksi Dasar Referensi dan Standar SDLC
Berdasarkan dokumen `docs/sdlc/05_testing/01_test_plan.md` (dan wawasan dari `docs/sdlc/narasi.txt`), terdapat beberapa kaidah ketat yang wajib diimplementasikan:
- **Framework & Alat Uji:** Wajib menggunakan `pytest` dan `coverage.py`.
- **Target Kualitas:** Persentase cakupan kode (*code coverage*) wajib minimal $\ge 90\%$.
- **Metode Pengujian:** Pengujian *Unit Testing* diarahkan khusus pada logika bisnis murni (*pure logic*) tanpa efek samping.
- **Kriptografi CRM (Modul M.8):** Enkripsi menggunakan library `Fernet` (simetris dua arah).
- **Keamanan dan Privasi:** Mendukung standar privasi CRM sejalan dengan amanat UU PDP (Undang-Undang Perlindungan Data Pribadi).

## 4. Batasan, Cakupan, dan Kualitas Pengerjaan
- **Fokus Utama:** Merancang unit test untuk memastikan fungsi-fungsi pemroses enkripsi dan dekripsi nomor WA berjalan sempurna dan gagal secara elegan bila terjadi anomali.
- **Isolasi Mutlak (Mocking):** Modul ini harus terisolasi. Jika fungsi utama bergantung pada variabel kunci dari `system_configs` database MySQL atau `.env`, ketergantungan ini **wajib** disimulasikan menggunakan `unittest.mock` atau `pytest-mock`. Dilarang keras menyinggung database riil yang dapat menyebabkan *side-effect* merusak pada operasional data aplikasi atau feature lainnya.
- **Kualitas Eksekusi:** *No To-Do Left Behind*. Seluruh skrip harus komplit, fungsional penuh, dan tidak ada ruang untuk fungsi *placeholder* yang belum selesai.

## 5. Lokasi Penyimpanan Unit Test
Unit test wajib disimpan secara hierarkis ke dalam *directory* *testing*, menyesuaikan dengan target fungsionalnya (logic bisnis murni):
**Target File Uji:** `tests/logic/test_whatsapp_encryption.py` (atau menyesuaikan nama file/module yang diuji dari folder aslinya).

## 6. Skenario Uji Wajib (Test Cases)
Harap penuhi spesifikasi skenario secara mendetail dan sebanyak mungkin.

**A. Skenario Positif (Positive Cases):**
- [ ] Enkripsi: Nomor WhatsApp berformat standar string (contoh: `'081234567890'`) berhasil diubah menjadi bentuk biner token (atau string `str`) token Fernet yang aman.
- [ ] Dekripsi: Pemulihan dari token Fernet (ciphertext) valid dapat diekstrak mutlak mengembalikan nilai awal string yang identik tanpa ada perubahan karakter atau spasi.
- [ ] Integritas Dua Arah: Data dari `decrypt(encrypt(data))` == `data`.

**B. Skenario Negatif & Edge Cases (Negative/Edge Cases):**
- [ ] *Invalid Token:* Proses dekripsi terhadap token yang rusak, token asimetris asal-asalan, atau token yang mengalami manipulasi (*tampered*) harus menggagalkan diri secara eksplisit (misal: melempar eksepsi `InvalidToken`).
- [ ] *Wrong Key:* Proses dekripsi menggunakan *Secret Key Fernet* yang keliru/berbeda harus teridentifikasi gagal mutlak, menunjukkan sistem kedap dari dekripsi ilegal.
- [ ] *Empty String:* Proses enkripsi pada string kosong (`""`). Apakah menghasilkan enkripsi yang wajar dan dapat dikembalikan sebagai `""`.
- [ ] *Boundary Length:* Uji pada nomor yang sangat pendek (`"123"`) dan panjang absurd.

**C. Skenario Validasi Input (Input Validation):**
- [ ] Input bukan *string*: Fungsi diinjeksi dengan `Integer` (contoh: `081234567890` yang menjadi oktal atau int murni). Fungsi harus merespons penolakan elegan/TypeError.
- [ ] Input *Null/NoneType*: Memastikan sistem tidak *crash/segfault* akibat unhandled exception, melainkan di-*raise* menjadi respons keamanan yang logis.
- [ ] Input karakter ilegal: Sanitasi dan *handling* input karakter tak terduga (contoh simbol-simbol khusus) sebelum enkripsi berlangsung.

## 7. Standarisasi Clean State
- **Setup & Teardown Wajib:** Seluruh state uji harus tereset dari nol sebelum setiap fungsi `test_...` dipanggil.
- **Fixture:** Implementasikan `@pytest.fixture` yang *stateless*. *Mock key* yang di-*inject* dalam fixture bersifat independen per fungsi agar tidak ada token palsu yang bocor lintas uji.

## 8. Low-Level Checklist Tahapan Pengerjaan Markdown (Bagi AI Eksekutor)
Ikuti rute pengerjaan tahap-demi-tahap di bawah ini. Harap centang/tandai saat langkah telah dieksekusi secara nyata, dan jangan berhalusinasi.

- [ ] **Pembacaan Kode Utama:** Identifikasi, *search*, dan amati file asal yang menyimpan *source code* fungsi enkripsi dan dekripsi Fernet untuk WhatsApp di repositori.
- [ ] **Inisialisasi File:** Buat/buka `tests/logic/test_whatsapp_encryption.py` dan deklarasikan instalasi dependensi (contoh: `import pytest`, modul cryptography, modul target, dan library mock terkait).
- [ ] **Penyusunan Fixture (Mocking):** Rangkai `pytest.fixture` untuk menduplikasi lingkungan (pengganti pemanggilan kunci asli dari database/env lokal). Pastikan ia mengaktifkan *clean state*.
- [ ] **Penulisan Blok Skenario Positif:** Tuliskan konvensi fungsi Python yang baik, misalnya: `test_encrypt_whatsapp_returns_valid_token()`, `test_decrypt_token_returns_original_string()`.
- [ ] **Penulisan Blok Skenario Negatif:** Gunakan penanganan error bawaan (contoh: `with pytest.raises(InvalidToken):`) dalam fungsi uji `test_decrypt_invalid_token_raises_exception()` maupun kunci palsu.
- [ ] **Penulisan Blok Validasi Input:** Susun test case untuk *Null/None* dan tipe numerik.
- [ ] **Pembersihan (Cleanup) & Refactoring Akhir:** Pastikan tidak ada fungsi yang menyisakan tag `TO-DO`. Atur docstring standar dan dokumentasi internal di setiap skenario.
- [ ] **Verifikasi (Assertion):** Sertakan skrip shell terminal sederhana (misal: `pytest tests/logic/test_whatsapp_encryption.py -v --cov=logic.nama_file`) untuk di-eksekusi user setelahnya agar menjustifikasi *coverage* unit mencapai standar $\ge 90\%$.
