---
dokumen    : Issue Planning Unit Test
judul      : unit-test feature role based access control multi-level
target_file: docs/issue/0119_issue_unit_test_feature_role_based_access_control_multi-level.md
---

# Issue: Unit-Test Feature Role Based Access Control Multi-Level

Dokumen perencanaan eksekusi ini ditujukan bagi junior programmer atau agen AI LLM untuk mengembangkan unit test fitur keamanan RBAC. Seluruh instruksi bersifat deterministik, berbasis SDLC AbuCom, dan siap dieksekusi.

## 1. Persona Eksekutor AI / Programmer
**Senior QA Automation Engineer & Python Testing Specialist**
Memiliki otoritas penuh dan pemahaman arsitektural mutlak terkait Pytest, *code coverage*, pengujian *pure functional programming* (FP), serta keamanan siber (Security Testing). Eksekutor memahami implementasi standar otentikasi (JWT stateless, bcrypt) dan otorisasi *Least Privilege* sesuai standar enterprise.

## 2. Pemilihan Referensi Utama (SSoT)
Referensi utama yang diderivasi dari direktori `docs/sdlc/`:
1.  **`docs/sdlc/05_testing/01_test_plan.md`**: Sebagai standar pengujian unit (Bab 3.1.1 Unit Testing, Bab 5.2 Pengujian Otorisasi, target cakupan $\ge 90\%$).
2.  **`docs/sdlc/02_analysis/06_access_control_matrix.md`**: Sebagai SSoT (Single Source of Truth) logika kontrol akses 8 peran, *Default Deny Policy*, kebijakan pewarisan (inheritance), dan kode *error* sistem.
3.  **`docs/sdlc/04_implementation/01_coding_standard.md`**: Sebagai standar konvensi penamaan kode, *clean code*, fungsi murni, penulisan error code (`ERR-AUTH-003`), dan arsitektur pengujian.

*(Catatan: File `narasi.txt` diabaikan karena kebutuhan sistem yang terstruktur sudah tercover sepenuhnya di tiga dokumen formal di atas.)*

## 3. Rangkuman Detail Referensi untuk Fitur Ini
Poin-poin spesifik yang wajib diimplementasikan dari SDLC untuk RBAC Unit Test:
*   **Kebijakan Otorisasi**: Implementasikan tes untuk *Least Privilege* berdasarkan 8 peran baku (`pemilik`, `kepala_percetakan`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang`, `pramuniaga`).
*   **Kode Kesalahan (Error Codes)**: Setiap penolakan otorisasi harus diverifikasi menghasilkan pesan kegagalan spesifik, seperti `ERR-AUTH-003` (Akses ditolak), `ERR-AUTH-002` (Brute force), `ERR-AUTH-029` (Sandi eskalasi salah), `ERR-SESSION-002` (Sesi JWT lebih dari 8 jam/28.800 detik).
*   **Audit Trail**: Verifikasi bahwa penolakan otomatis memicu (lewat *mocking*) pencatatan log dengan argumen spesifik: `action_type='ACCESS_DENIED'`.
*   **Default Deny Policy**: Akses tanpa rute yang jelas atau peran yang tidak terdefinisi wajib ditolak mutlak secara biner, tanpa terkecuali. Tidak ada pewarisan/cascade peran antar hierarki.

## 4. Batasan & Cakupan Pengerjaan
*   Cakupan fungsi difokuskan pada unit logika dari decorator RBAC (contohnya komponen `middleware/rbac_guard.py` atau ekuivalennya).
*   **Tanpa I/O Database**: Seluruh pengujian wajib dilakukan secara lokal pada memori tanpa side-effects.
*   **Isolasi Menggunakan Mocking**: Modul pemanggil koneksi `db/db_connector.py` atau `audit_logger.py` **WAJIB** di-*mock* penuh agar tidak merusak data seed sistem development.
*   **Kualitas & Kelengkapan Ketat**: File test case harus komplit, siap di-*run*, tanpa placeholder, tanpa kode stub `# TODO`, atau parameter fungsi yang menggantung.

## 5. Kaidah Standar Spesifik Unit-Test
*   **Penyimpanan Test**: Berkas disimpan di dalam path direktori `tests/` dengan nama standar (misalnya `tests/test_rbac_security.py`).
*   **Konvensi Penamaan**: Semua method test wajib berformat `snake_case` dan diawali dengan `test_` (contoh: `test_kasir_ditolak_akses_laba_rugi()`). Gunakan konvensi penamaan yang deskriptif.
*   **Pola Pengujian (Clean State)**: Wajib mengimplementasikan `pytest.fixture` dengan metode *yield* atau struktur *teardown* untuk menjamin sesi *state* di-reset ulang ke kondisi kosong (clean state) di setiap pembukaan skenario test.

## 6. Skenario Pengujian Wajib (Test Scenarios)
Setiap skenario di bawah ini harus dikembangkan kodenya secara riil:

*   **Skenario Positif (Positive Testing)**
    *   Pengujian otorisasi `pemilik` terhadap menu kritikal finansial (misal `MENU-M4-002` Smart Payroll) yang wajib tereksekusi utuh tanpa hambatan.
    *   Pengujian operasional `kasir` terhadap pemrosesan transaksi normal (`MENU-M1-001`), dan verifikasi bahwa *wrapper* melanjutkan alur ke fungsi target.

*   **Skenario Negatif / Boundary Cases (Negative Testing)**
    *   Pengujian peran terlarang: `desainer` mengakses `MENU-M1-005` (Margin Produk). Harus digagalkan dan melempar *response* yang menampung `ERR-AUTH-003`.
    *   Pengujian *Default Deny Policy*: Memasukkan `session_state` kotor (tanpa *key* `role` atau dengan role `'hacker'`). Harus digagalkan mutlak.
    *   Pengujian Boundary Kedaluwarsa Sesi JWT: Simulasi *timestamp* melebihi batas 28.800 detik. Wajib menghasilkan penolakan otentikasi dengan standar `ERR-SESSION-002`.

*   **Validasi Input & Anomali Sistem (Edge Cases)**
    *   Memastikan struktur *dictionary state* tetap dikelola utuh dan tidak bermutasi (prinsip *pure function*) usai melewati decorator RBAC.
    *   Pengujian eskalasi penolakan (contoh: fungsi `require_supervisor`) apabila simulasi input sandi (mock via `getpass`) dinyatakan salah, yang akan menghasilkan `ERR-AUTH-029`.

## 7. Tahapan Eksekusi Low-Level Checklist
Jalankan dan tandai (centang `[x]`) tahapan berikut ini di *mind state* eksekutor tanpa ada yang dilompati. Dilarang berhalusinasi mengimpor *library* yang tidak standar.

- [ ] **1. Persiapan Lingkungan & Arsitektur**
  - [ ] Menentukan target modul RBAC (misal: memuat fungsi/decorator `require_role` dari lapis `middleware/`).
  - [ ] Membuat file baru di `tests/test_rbac_security.py`.
  - [ ] Melakukan deklarasi `import pytest` dan objek utilitas *mocking* bawaan standar Python (`from unittest.mock import patch, MagicMock`).

- [ ] **2. Inisialisasi Fixture & Clean State**
  - [ ] Menulis `pytest.fixture` pertama untuk membangun *mock* `session_state` berbagai peran secara dinamis.
  - [ ] Menulis fungsi *dummy* sebagai wadah palsu (misal `dummy_action()`) yang dibalut decorator RBAC.
  - [ ] Mengonfigurasi mekanisme *clean up* / peresetan variabel state di akhir proses setiap fungsi fixture (memastikan isolasi *side effect*).

- [ ] **3. Implementasi Kode Skenario Positif**
  - [ ] Menulis fungsi `test_pemilik_akses_kritis_diterima()` menggunakan *dummy action*.
  - [ ] Melakukan `assert` biner bahwa nilai *return* sesuai dengan keluaran fungsional murni.

- [ ] **4. Implementasi Kode Skenario Negatif & Default Deny**
  - [ ] Menulis fungsi `test_desainer_ditolak_pada_menu_finansial()`.
  - [ ] Menyisipkan `patch` pada `print` CLI terminal, dan melakukan `assert` spesifik mencocokkan kemunculan teks *substring* `ERR-AUTH-003`.
  - [ ] Menulis fungsi `test_default_deny_policy_untuk_unrecognized_role()`, memastikan *behavior* penguncian secara *default* terjadi.

- [ ] **5. Implementasi Kode Validasi Eskalasi & Boundary JWT**
  - [ ] Menulis uji khusus JWT *expiration boundary* untuk memastikan *state* terblokir saat durasi lebih dari 8 jam.
  - [ ] Menulis uji fungsi verifikasi sandi eksekutif (eskalasi *supervisor*) dengan *input* palsu, mengecek verifikasi tangkapan `ERR-AUTH-029`.

- [ ] **6. Verifikasi Audit Logger Call & Keamanan DB**
  - [ ] Melalui `unittest.mock.patch`, pantau modul pencatat log JSON lokal.
  - [ ] Tambahkan perintah `mock_audit.assert_called_with()` pada uji penolakan akses untuk memastikan *key* `action_type='ACCESS_DENIED'` dikirimkan dari dalam decorator.
  - [ ] Verifikasi tidak adanya pemanggilan interaksi langsung ke I/O Database fisik MySQL di seantero *test script*.

- [ ] **7. Penilaian Kualitas (Quality Assurance)**
  - [ ] Membersihkan berkas Python uji dari seluruh stub `# TODO`.
  - [ ] (Secara konsep eksekusi) mensimulasikan hasil via `pytest tests/test_rbac_security.py --cov=middleware.rbac_guard` untuk memastikan tidak ada cabang logika `if-else` yang luput ter-cover. Target: Minimal $\ge 90\%$.
