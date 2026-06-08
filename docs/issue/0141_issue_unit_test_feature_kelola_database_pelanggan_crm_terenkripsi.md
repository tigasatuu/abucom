# Issue: Unit Test Feature Kelola Database Pelanggan CRM Terenkripsi

**Persona:** Senior QA Engineer & Test Automation Expert (Expert in Python, `pytest`, Cryptography Testing, dan Clean Architecture).

## 1. Konteks & Referensi Utama
* **Dokumen Referensi Utama:** 
  * `docs/sdlc/05_testing/01_test_plan.md` (Bab 3.1.1 Unit Testing, Bab 4.8 Modul M.8, Bab 5.7 Enkripsi Fernet, Bab 5.8 UU PDP)
  * `docs/sdlc/narasi.txt` (Untuk pemahaman alur bisnis secara umum jika diperlukan).
* **Target Direktori Test:** Folder `tests/` (disarankan `tests/logic/` atau `tests/unit/`) menggunakan framework **`pytest`** dan `coverage.py` seperti yang diamanatkan dalam dokumen SDLC.

## 2. Ringkasan Kebutuhan Berdasarkan SDLC
Ekstraksi dari dokumen SDLC (terutama Test Plan v1.2):
* **Fokus Modul:** Modul M.8 (CRM Database Pelanggan).
* **ID Skenario Utama:**
  * **M8-TC-001:** Pendaftaran pelanggan CRM & proteksi nomor WhatsApp terenkripsi Fernet dua arah biner.
  * **M8-TC-002:** Hak penghapusan data CRM privat secara permanen (UU PDP) secara *hard-delete*.
* **Standar Unit Testing:**
  * Wajib menggunakan `pytest`.
  * Harus terisolasi dari *side effect* I/O database langsung (menggunakan *mocking* objek atau *in-memory data structures* / *dependency injection*).
  * Cakupan tes (*code coverage*) wajib $\ge 90\%$.
  * Penamaan fungsi test harus deskriptif (misal: `test_encrypt_whatsapp_number_success`).

## 3. Batasan dan Aturan Pengerjaan
1. **Isolasi Penuh (Mocking):** Jangan melakukan koneksi ke database fisik MySQL (`abucom_test_db`) untuk *pure unit test*. Gunakan *mock* (misal: `unittest.mock.MagicMock` atau `pytest-mock`) untuk simulasi penyimpanan ke database, pembacaan `.env` (Fernet Key), dan log audit JSON.
2. **Clean State:** Setiap fungsi test wajib berjalan dari state yang bersih (*clean state*). Gunakan *fixture* `pytest` (misalnya `setup` / `teardown` atau `yield` di fixture) untuk me-reset mock dan state internal setiap kali sebelum dan sesudah test berjalan.
3. **Kualitas Pengerjaan:** Kode test harus 100% komplit. Dilarang meninggalkan komentar `TODO` atau fungsi yang tidak diimplementasikan.
4. **Keamanan:** Kunci enkripsi *Fernet* di dalam unit test harus menggunakan kunci *dummy/mock* yang valid formatnya secara terisolasi, BUKAN kunci *production*.

## 4. Skenario Unit Test (Test Cases)

### A. Skenario Positif
* [ ] Memastikan fungsi enkripsi berhasil mengubah format nomor WhatsApp `081234567890` menjadi *ciphertext* *Fernet* biner.
* [ ] Memastikan fungsi dekripsi berhasil mengembalikan *ciphertext* kembali menjadi plaintext `081234567890` menggunakan kunci yang sama.
* [ ] Memastikan proses penyimpanan pelanggan (Mock DB) berhasil memanggil fungsi insert dengan *ciphertext* (bukan *plaintext*).
* [ ] Memastikan fungsi penghapusan akun (*Right to Erasure* / UU PDP) secara benar memanggil perintah eksekusi query `DELETE` pada database (Mock DB), bukan sekadar update flag `is_deleted` (*soft-delete*).

### B. Skenario Negatif / Edge Cases
* [ ] Memastikan dekripsi gagal (raise *Exception/Error*) jika menggunakan kunci *Fernet* yang berbeda/salah (Invalid Token).
* [ ] Memastikan sistem menolak pendaftaran jika nomor WhatsApp kosong atau berisi karakter *non-numeric* (selain `+` atau angka).
* [ ] Memastikan sistem menangani dengan benar saat mencoba mendekripsi data yang nilainya `None` atau *empty string*.
* [ ] Memastikan fungsi *hard-delete* menangani kasus dengan aman (tidak *crash*) jika ID Pelanggan yang ingin dihapus tidak ditemukan.

### C. Validasi Input (Format WhatsApp Indonesia)
* [ ] Memastikan sistem menolak prefix yang tidak valid (misal: `09xxx` atau huruf).
* [ ] Memastikan panjang karakter nomor WhatsApp tervalidasi (misal: minimal 10 digit, maksimal 14 digit).
* [ ] Memastikan sanitasi input berhasil menghapus spasi atau tanda strip `-` (misal `0812-3456-7890` menjadi `081234567890`).

## 5. Checklist Pengerjaan (Low-Level Implementation Steps)

Eksekusi tahapan berikut secara berurutan tanpa halusinasi:

* [ ] **Tahap 1: Analisis & Persiapan**
  * [ ] Membaca modul kode sumber CRM saat ini (lokasi fungsi registrasi, enkripsi, dekripsi, dan penghapusan).
  * [ ] Menyiapkan file test baru, misal di `tests/logic/test_crm_encryption.py` (atau struktur folder sejenis).
  * [ ] Melakukan inisialisasi *import* yang dibutuhkan (`pytest`, library `cryptography.fernet`, objek/fungsi sumber yang akan dites, dan `patch`/`MagicMock` dari `unittest.mock`).

* [ ] **Tahap 2: Pembuatan Fixtures (Clean State)**
  * [ ] Membuat `pytest.fixture` untuk men-generate dan me-return kunci Fernet *dummy* statis.
  * [ ] Membuat `pytest.fixture` untuk me-reset state *mock* DB dan konfigurasi `os.environ` sebelum setiap test case dieksekusi.

* [ ] **Tahap 3: Implementasi Skenario Validasi & Sanitasi Input**
  * [ ] Menulis fungsi `def test_validate_whatsapp_format_valid():` beserta *assertion*-nya.
  * [ ] Menulis fungsi `def test_validate_whatsapp_format_invalid_length():` beserta *assertion* `pytest.raises`.
  * [ ] Menulis fungsi `def test_validate_whatsapp_format_invalid_chars():` beserta *assertion* `pytest.raises`.

* [ ] **Tahap 4: Implementasi Skenario Enkripsi & Dekripsi (Fernet)**
  * [ ] Menulis fungsi `def test_fernet_encryption_process():` memastikan hasil enkripsi berbeda dengan teks asli.
  * [ ] Menulis fungsi `def test_fernet_decryption_process():` memastikan hasil dekripsi mengembalikan ke teks asli secara utuh.
  * [ ] Menulis fungsi `def test_fernet_decryption_invalid_key_fails():` memastikan `pytest.raises(InvalidToken)` dari pustaka `cryptography`.

* [ ] **Tahap 5: Implementasi Skenario Isolasi DB & Penghapusan Permanen (UU PDP)**
  * [ ] Menulis fungsi `def test_register_customer_saves_encrypted_data():` melakukan *mock* terhadap eksekutor kueri dan memastikan *value* dari parameter SQL yang di-*pass* adalah versi terenkripsi.
  * [ ] Menulis fungsi `def test_delete_customer_performs_hard_delete():` melakukan *mock* terhadap koneksi DB dan memastikan metode kueri SQL memanggil argumen yang berawalan `DELETE FROM` (bukan `UPDATE`).

* [ ] **Tahap 6: Verifikasi Kode & Kualitas**
  * [ ] Memastikan tidak ada satupun fungsi *dummy* berlabel `TODO` atau sekadar berisi `pass`.
  * [ ] Memastikan setiap exception/error handling pada tes sudah di-assert secara presisi dan akurat.
  * [ ] Memastikan semua tes berjalan deterministik dan konsisten (*idempotent*) walau dijalankan berulang kali berkat *fixture clean state*.
