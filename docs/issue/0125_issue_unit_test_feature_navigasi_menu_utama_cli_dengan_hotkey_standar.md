# Issue #0125: Unit-Test Feature Navigasi Menu Utama CLI dengan Hotkey Standar

## 1. Persona Eksekutor
**Persona:** Senior QA Automation Engineer & SDLC Testing Specialist.
**Karakteristik:** Sangat teliti, analitis, memiliki pemahaman mendalam tentang framework `pytest`, ahli dalam membuat arsitektur *Functional Programming* (FP) pengujian murni, mahir dalam melakukan teknik *mocking* untuk mengisolasi *side-effects* I/O terminal dan instruksi *database*, serta patuh mutlak terhadap standar prosedur kualitas (SDLC).

## 2. Dokumen Referensi Utama
Dalam mengerjakan issue ini, eksekutor wajib merujuk secara ketat pada dokumen-dokumen internal berikut:
1. `docs/sdlc/05_testing/01_test_plan.md` - (Pedoman utama metodologi dan strategi *System/Unit Testing*, serta aturan presisi pengujian).
2. `docs/sdlc/04_implementation/01_coding_standard.md` - (Pedoman konvensi penamaan fungsi dan standar *clean code* khusus *testing* Python).
3. `docs/sdlc/narasi.txt` - (Sebagai rujukan alur logika bisnis dan arsitektur aplikasi kasir luring untuk merancang *data mock*).
4. *(Referensi Fitur)* `docs/issue/0124_issue_implementasi_cli_hotkey_navigation.md` atau berkas source code implementasi fitur terkait - (Sebagai dasar memahami fitur yang akan diuji fungsionalitasnya).

## 3. Instruksi Analisis dan Ekstraksi Referensi
Sebelum melakukan penulisan *source code*, lakukan pembacaan dan asimilasi secara menyeluruh terhadap dokumen referensi.
*   **Ekstrak Kriteria SDLC Fase 05:** Tangkap poin kewajiban penggunaan framework `pytest`, pengecekan kualitas via `coverage`, kewajiban meletakkan pengujian *pure logic* secara deterministik, serta kewajiban bebas dari koneksi DB langsung.
*   **Pahami Fitur Navigasi:** Pastikan semua target uji pada modul Navigasi CLI dipahami: *breadcrumb* *path*, *filter* peran (RBAC), pemilihan navigasi via *hotkey* standar angka/huruf, penanganan karakter masuk tak terduga, serta prosedur *graceful shutdown* (`q` atau menekan `Ctrl+C`).

## 4. Batasan, Cakupan, dan Standar Pengerjaan
*   **Cakupan Target:** Pekerjaan difokuskan secara eksklusif hanya untuk pembuatan *Unit Test* terhadap komponen logika navigasi CLI (menu utama, submenu, validasi hak akses navigasi, dan perpindahan *state* antar antarmuka).
*   **Tools:** Wajib menggunakan `pytest` murni tanpa intervensi pustaka unit testing tambahan pihak ketiga di luar yang diijinkan spesifikasi *environment setup*.
*   **Target Mutu:** Memastikan target pencapaian *code coverage* dari pengujian unit pada logic menu utama adalah $\ge 90\%$ tanpa kebohongan pengukuran.
*   **Folder Penyimpanan:** Seluruh *script* pengujian wajib diletakkan di dalam direktori absolut `tests/` sesuai keseragaman arsitektur proyek.
*   **Konvensi Penamaan Unit Test:**
    *   Nama file harus di-prefix dengan `test_` (misalnya: `test_cli_navigation.py`).
    *   Nama fungsi pengujian (method) harus menggunakan bahasa yang deskriptif dan di-prefix `test_` (contoh: `test_navigasi_menu_utama_masuk_inventaris_berhasil()`).

## 5. Isolasi Lingkungan Uji (Mocking Rules)
*   **Isolasi Mutlak:** Pekerjaan ini WAJIB terisolasi. Program *test* dilarang keras memodifikasi, menimpa (*overwrite*), memanggil modul operasi produksi langsung, atau terhubung secara aktif ke server MySQL berjalan.
*   **Mocking:** Gunakan teknik *mocking* internal Python (`unittest.mock.patch` atau *fixture* `pytest`) untuk:
    *   Mengelabui / *bypass* perenderan terminal visual dan *blocking input keyboard* (misalnya: mem-*mock* fungsi `input()` atau fungsi baca *keystroke* agar mengembalikan tombol *hotkey* spesifik).
    *   Mengisolasi proses verifikasi otorisasi matriks peran RBAC menggunakan simulasi objek *dummy session state user* (misal sesi *mock* untuk `kasir` atau `pemilik`).
    *   Meniadakan *side-effects* I/O (seperti penulisan *log file*, *database query*, atau pemanggilan `sys.exit` secara harfiah).

## 6. Skenario Pengujian (Test Scenarios)
Rancang skenario secara mendalam dan mencakup segala kemungkinan (*exhaustive*). Dilarang menyisakan komentar instruksional `to-do` atau `pass` kosong.
Cakupan skenario pengujian WAJIB memenuhi 3 pilar:

1.  **Skenario Positif (Happy Path):**
    *   Validasi menekan tombol *hotkey* valid pada menu utama menuju representasi fungsi Sub-Menu yang tepat.
    *   Validasi fungsi mundur/kembali (misalnya *hotkey* `0` atau tombol back) sukses mengembalikan *state* CLI ke struktur satu tingkat di atasnya (Parent Menu).
    *   Validasi UI *breadcrumb* navigasi (contoh: `Dashboard Utama > Inventaris & BOM`) ter-update dengan string rute yang presisi pasca menekan tombol *hotkey*.

2.  **Skenario Negatif dan Edge Cases (Robustness):**
    *   Validasi *invalid key:* Menekan *hotkey* angka/huruf acak tak terdaftar tidak boleh menyebabkan aplikasi *crash*. Sistem harus mempertahankan *loop* navigasi dan mengembalikan status *error* penolakan input.
    *   Validasi *RBAC Filter:* Simulasi agen berlisensi rendah (misalnya: 'kasir') menekan tombol *hotkey* sub-menu manajerial (misal menu 'Laba Rugi'). *Test* harus membuktikan bahwa *state* menu diblokir pindah, memicu peringatan visul, serta memanggil fungsi *log* otorisasi dengan status akses ditolak.
    *   Validasi *Input Validation:* Menangani input berisi *escape character* atau tombol fungsional aneh yang disanitasi secara utuh.

3.  **Pengujian Penutupan (Graceful Exit / Shutdown):**
    *   Simulasi eksekusi penghentian aplikasi melalui interaksi wajar (menekan tombol `q` untuk keluar).
    *   Simulasi eksekusi penghentian secara mendadak (meniru pemicuan blok `KeyboardInterrupt` / `Ctrl+C`). Verifikasi bahwa metode pembersihan akhir berjalan aman tanpa jejak *stack trace error* mencemari terminal.

## 7. Kebijakan Reset State (Clean State / Fixtures)
Setiap skenario unit-test WAJIB diisolasi *state*-nya dari unit-test lain untuk menghindari distorsi/kebocoran data lintasan tes (*state leakage*).
*   Implementasikan pembersihan status mutlak (*clean state*) sebelum skenario pengujian baru dijalankan menggunakan kapabilitas `@pytest.fixture` (baik melalui inisialisasi awal maupun *teardown*).
*   Reset secara paksa seluruh jejak variabel *dummy user*, susunan hirarki menu navigasi tiruan, dan isi dari string *breadcrumb* pada awal eksekusi tiap fungsi tes untuk menjaga konsistensi dan integritas hasil.

## 8. Langkah Eksekusi Berbasis Checklist

Agar model AI LLM/Junior Programmer tereksekusi tanpa risiko halusinasi atau ambiguitas, wajib melaksanakan tahap berurutan secara presisi di bawah ini:

- [ ] **1. Persiapan, Analisis Referensi & Lingkungan**
  - [ ] Lakukan ekstraksi metadata dan pemahaman aturan di `docs/sdlc/05_testing/01_test_plan.md` dan `docs/sdlc/04_implementation/01_coding_standard.md`.
  - [ ] Pahami arsitektur spesifikasi dari *issue* navigasi CLI sebelumnya (identifikasi fitur *hotkey*, bentuk string *breadcrumb*, pemblokiran RBAC, dan respons `Ctrl+C`).
- [ ] **2. Persiapan Struktur Folder & File Uji**
  - [ ] Verifikasi ketersediaan direktori `tests/` di root *repository* proyek.
  - [ ] Buat file unit test mandiri baru yang disesuaikan, misalnya `tests/test_cli_navigation.py` (patuhi konvensi penamaan standar Python).
- [ ] **3. Inisialisasi Mocking & Setup Fixtures (Pembersihan State)**
  - [ ] Rancang dan definisikan `pytest fixture` untuk mem-*mock* hierarki susunan Menu Utama dan Sub-Menu yang digunakan dalam skenario.
  - [ ] Rancang dan definisikan *fixture* untuk *User Session* (membuat objek sampel *User* dengan otorisasi `Pemilik` dan otorisasi `Kasir`).
  - [ ] Rancang dan definisikan *auto-use fixture* agar *breadcrumb state* direntangkan bersih (kosong/inisial) di setiap perputaran iterasi pengujian (Setup dan Teardown).
- [ ] **4. Konstruksi Kode Skenario Pengujian Positif (Happy Path)**
  - [ ] Implementasikan `test_navigasi_hotkey_valid_ke_submenu()` lengkap dengan instruksi *assert* pindah rute menu.
  - [ ] Implementasikan `test_navigasi_mundur_ke_menu_parent()` untuk verifikasi pergerakan balik satu level menu.
  - [ ] Implementasikan `test_pembaruan_teks_breadcrumb()` untuk memastikan visibilitas UI string jalan terminal yang akurat.
- [ ] **5. Konstruksi Kode Skenario Pengujian Negatif (Edge Case & RBAC)**
  - [ ] Implementasikan `test_navigasi_menolak_hotkey_invalid()` disertai `assert` status *loop error*.
  - [ ] Implementasikan `test_navigasi_memblokir_akses_submenu_di_luar_izin_rbac()` beserta verifikasi pemanggilan peringatan visual penolakan.
  - [ ] Implementasikan `test_navigasi_sanitasi_spesial_karakter()` untuk menguji pencegahan interupsi karakter nyeleneh.
- [ ] **6. Konstruksi Kode Skenario Pengujian Shutdown Program**
  - [ ] Implementasikan `test_navigasi_graceful_shutdown_tombol_q()` lengkap dengan *mock* agar tidak mengeksekusi iterasi menu lanjutan.
  - [ ] Implementasikan `test_navigasi_graceful_shutdown_ctrl_c()` guna memverifikasi tangkapan `KeyboardInterrupt` tanpa pemicuan jejak galat sistem murni.
- [ ] **7. Verifikasi Kualitas Akhir Eksekusi & Inspeksi Logika**
  - [ ] Inspeksi mandiri terhadap sintaks kode dan pastikan bebas dari eror sintaks awal.
  - [ ] Verifikasi setiap instruksi `assert` memiliki argumen perbandingan status yang koheren, nyata, spesifik dan tidak ambigu.
  - [ ] Teliti semua blok fungsi pengujian dan singkirkan bagian *placeholder dummy* atau kode kosong semacam `pass`, `TODO`, dan `FIXME`.
  - [ ] Simulasikan alur verifikasi alur test (mental model *dry run*) di dalam *context prompt* sebelum melakukan tahap final.
