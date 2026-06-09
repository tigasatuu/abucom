---
issue_id      : 0142
judul         : Feature Enkripsi dan Dekripsi Nomor WhatsApp Pelanggan
status        : Open
prioritas     : High
modul_terkait : M.7 (Keamanan), M.8 (CRM Pelanggan)
file_terdampak: utils/crypto.py, cli/menu_transaksi.py, config/settings.py, tests/test_crm_crypto.py, tests/logic/test_crm_encryption.py
tanggal       : 2026-06-10
---

# Issue #0142 — Feature Enkripsi dan Dekripsi Nomor WhatsApp Pelanggan

## 1. Persona Pelaksana

**Kamu adalah Senior Cryptography & Data Privacy Engineer** yang memiliki keahlian khusus dalam:
- Implementasi enkripsi simetris reversibel (Fernet/AES) untuk perlindungan data pribadi.
- Kepatuhan regulasi UU PDP No. 27 Tahun 2022 Republik Indonesia.
- Paradigma Functional Programming (FP) murni Python tanpa class/OOP.
- Integrasi modul keamanan dengan layer CLI, Database, dan Middleware pada arsitektur 4-layer AbuCom.
- Pengujian deterministik unit testing menggunakan `pytest` untuk fungsi kriptografi.

Kamu bertanggung jawab penuh atas **integritas, kelengkapan, ketepatan, dan keamanan** seluruh alur enkripsi/dekripsi nomor WhatsApp pelanggan, mulai dari validasi input, enkripsi sebelum penyimpanan ke database, dekripsi saat visualisasi di terminal CLI, hingga penanganan error dan audit trail.

---

## 2. Dokumen Referensi Utama

Berikut adalah file referensi yang **WAJIB** dibaca, dipahami, dan diekstrak informasinya sebelum memulai pengerjaan:

| No | Dokumen Referensi | Lokasi Path Relatif | Alasan Relevansi |
|:---:|---|---|---|
| 1 | **Security Design v1.2** | `docs/sdlc/03_design/06_security_design.md` | **Referensi utama**. Berisi spesifikasi lengkap enkripsi Fernet WhatsApp (Bab 6.1, 6.3, 6.4), pseudocode fungsi `encrypt_wa()` dan `decrypt_wa()` (Bab 12.2 nomor 4), konfigurasi `FERNET_KEY` di `.env` (Bab 12.3), validasi regex WhatsApp `^08[0-9]{8,11}$` (Bab 6.4), dan model ancaman THR-008 pencurian data WhatsApp CRM oleh staf. |
| 2 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | Standar penulisan kode FP murni, naming conventions, Result Pattern, aturan proteksi data pribadi UU PDP Fernet (Bab 10.7), dan standar system logging (Bab 10.8). |
| 3 | **Module Structure v1.2** | `docs/sdlc/04_implementation/03_module_structure.md` | Spesifikasi file `utils/crypto.py` (Bab 9.2) dengan signature fungsi `encrypt_whatsapp_number()` dan `decrypt_whatsapp_number()`, serta mapping Modul M.8 CRM ke `cli/menu_transaksi.py`. |
| 4 | **Database Schema DDL v1.2** | `docs/sdlc/03_design/01_database_schema.sql` | Struktur tabel `pelanggan` (TABEL 03), khususnya kolom `whatsapp VARCHAR(100) NOT NULL UNIQUE` yang menyimpan data terenkripsi. |
| 5 | **Access Control Matrix v1.1** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Matriks hak akses CRM: hanya `pemilik`, `pramuniaga`, `kasir` yang boleh akses M.8 CRM; staf `desainer`, `produksi_cetak`, `gudang` **DITOLAK MUTLAK**. |
| 6 | **CLI Interaction Flow v1.1** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur interaksi menu CRM `MENU-M8-001`, alur pendaftaran pelanggan baru, pencarian berdasarkan WhatsApp, dan edit profil pelanggan. |

> **Catatan**: File `docs/sdlc/narasi.txt` **tetap** digunakan sebagai referensi konteks bisnis. Pada Bab "Database Pelanggan (CRM)" (baris 92) dijelaskan kebutuhan menyimpan data kontak pelanggan (nama/WA) untuk kebutuhan promosi dan riwayat pesanan. Pada Bab "Manajemen Hak Akses (Privasi)" (baris 89) dijelaskan pembedaan hak akses antara Pemilik dan Karyawan.

---

## 3. Rangkuman Detail Data dari Dokumen Referensi

### 3.1. Spesifikasi Teknis Enkripsi WhatsApp (dari Security Design v1.2)

- **Algoritma**: Enkripsi simetris reversibel menggunakan modul `cryptography.fernet` Python.
- **Kunci Enkripsi**: Fernet key 32-byte statis dimuat dari variabel lingkungan `.env` dengan nama `FERNET_KEY`.
- **Tujuan Kepatuhan**: UU Perlindungan Data Pribadi No. 27 Tahun 2022.
- **Model Ancaman Relevan**: `THR-008` — Staf pramuniaga mencuri data keanggotaan nomor WhatsApp CRM pelanggan untuk spamming pihak ketiga.
- **Klasifikasi Sensitivitas**: Tabel `pelanggan` termasuk klasifikasi **Operasional** (Bab 2.3), namun kolom `whatsapp` **WAJIB** dienkripsi reversible sebelum penyimpanan ke database.
- **Risiko Keamanan**: `RSK-SEC-007` — Kebocoran data pribadi (Nomor WA) keanggotaan CRM pelanggan toko. Probabilitas: 2, Dampak: 4, Skor: **8**.
- **Pseudocode Acuan** (Security Design Bab 12.2 nomor 4):
  ```python
  from cryptography.fernet import Fernet

  def encrypt_wa(nomor_wa: str, fernet_key: bytes) -> str:
      f = Fernet(fernet_key)
      return f.encrypt(nomor_wa.encode('utf-8')).decode('utf-8')

  def decrypt_wa(ciphertext: str, fernet_key: bytes) -> str:
      f = Fernet(fernet_key)
      return f.decrypt(ciphertext.encode('utf-8')).decode('utf-8')
  ```
- **Kebijakan Dekripsi**: Nomor WA pelanggan **hanya** didekripsi di memori Python saat visualisasi menu CRM. Tidak boleh tersimpan dalam bentuk teks polos di database.
- **Validasi Input WhatsApp** (Bab 6.4):
  - Regex format: `^08[0-9]{8,11}$`
  - Panjang maksimal: 20 karakter
  - Filter karakter ASCII kontrol di bawah `\x20`

### 3.2. Konfigurasi `.env` Terkait (dari Security Design Bab 12.3 & `.env.example`)

```bash
# 4. Kunci Enkripsi WhatsApp CRM Pelanggan (Fernet Cryptography)
# [HARUS DIISI MANUAL] Hasilkan kunci dengan:
# python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode('utf-8'))"
FERNET_KEY=YOUR_FERNET_KEY_HERE
```

- Kunci **WAJIB** di-generate menggunakan `Fernet.generate_key()`.
- Kunci **WAJIB** masuk validasi startup `.env` (ERR-FILE-001 jika kosong/tidak ada).
- Kebijakan rotasi: setiap 6 bulan atau jika dicurigai bocor.

### 3.3. Struktur Tabel Database `pelanggan` (dari DDL Tabel 03)

```sql
CREATE TABLE pelanggan (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nama_pelanggan VARCHAR(100) NOT NULL,
    whatsapp VARCHAR(100) NOT NULL UNIQUE,  -- Data terenkripsi Fernet
    tanggal_terdaftar DATE NOT NULL DEFAULT (CURRENT_DATE),
    cabang_id INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_pelanggan_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id)
);
```

- Kolom `whatsapp` bertipe `VARCHAR(100)` karena output Fernet ciphertext lebih panjang dari nomor WA polos.
- Kolom memiliki constraint `UNIQUE` — artinya satu nomor WA terenkripsi tidak boleh duplikat.
- **PENTING**: Karena Fernet menghasilkan ciphertext berbeda setiap kali (menggunakan timestamp + IV acak), pencarian pelanggan berdasarkan WhatsApp **TIDAK BISA** menggunakan `WHERE whatsapp = %s` dengan ciphertext baru. Mekanisme pencarian harus mengambil semua data lalu mencocokkan secara dekripsi di memori Python, ATAU menggunakan pendekatan deterministik hash tambahan.

### 3.4. Hak Akses CRM (dari Access Control Matrix)

| Peran | Akses M.8 CRM |
|---|---|
| `pemilik` | ✅ FULL |
| `pramuniaga` | ✅ FULL |
| `kasir` | ✅ FULL |
| `kepala_percetakan` | ⛔ DENY |
| `desainer` | ⛔ DENY |
| `produksi_cetak` | ⛔ DENY |
| `fotocopy_print` | ⛔ DENY |
| `gudang` | ⛔ DENY |

### 3.5. File Kode yang Sudah Ada (Kondisi Saat Ini)

| File | Status Saat Ini | Catatan |
|---|---|---|
| `utils/crypto.py` | ✅ **Sudah ada** (69 baris) | Berisi `encrypt_whatsapp_number()` dan `decrypt_whatsapp_number()` dengan penanganan error via logging. Sudah sesuai coding standard (FP murni, type hints, docstring PEP 257). |
| `cli/menu_transaksi.py` | ✅ **Sudah ada** (600 baris) | Berisi CRM menu (`form_crm_pelanggan`, `_form_daftar_pelanggan_baru`, `_form_cari_riwayat_pelanggan`, `_form_lihat_daftar_pelanggan`, `_form_edit_pelanggan`). **⚠️ KRITIS: Import `encrypt_whatsapp_number` dan `decrypt_whatsapp_number` dari `utils.crypto` TIDAK ADA di bagian import!** Fungsi dipanggil di baris 249, 326, 350, 449, 526, 557 tanpa import yang sesuai. Ini akan menyebabkan `NameError` saat runtime. |
| `tests/test_crm_crypto.py` | ✅ **Sudah ada** (66 baris) | Unit test dasar roundtrip, different output, wrong key, empty string, empty key, invalid key format. |
| `tests/logic/test_crm_encryption.py` | ✅ **Sudah ada** | Test tambahan dengan coverage lebih luas. |
| `config/settings.py` | ✅ **Sudah ada** | Memuat `FERNET_KEY` dari `.env` dan melakukan validasi format Fernet key. |
| `.env.example` | ✅ **Sudah ada** | Sudah memuat template `FERNET_KEY=YOUR_FERNET_KEY_HERE`. |

---

## 4. Batasan, Cakupan, dan Alur Pengerjaan

### 4.1. Cakupan Issue (IN-SCOPE)

Issue ini mencakup **validasi, perbaikan, dan penguatan** fitur enkripsi/dekripsi nomor WhatsApp pelanggan pada seluruh titik sentuh (touchpoint) berikut:

1. **Perbaikan bug import yang hilang** di `cli/menu_transaksi.py`.
2. **Validasi kualitas fungsi `utils/crypto.py`** terhadap spesifikasi Security Design.
3. **Validasi kelengkapan penanganan error** di setiap pemanggilan fungsi enkripsi/dekripsi.
4. **Validasi kelengkapan unit test** di `tests/test_crm_crypto.py` dan `tests/logic/test_crm_encryption.py`.
5. **Validasi mekanisme pencarian pelanggan berdasarkan WhatsApp terenkripsi** — memastikan pencarian masih fungsional meskipun Fernet menghasilkan ciphertext non-deterministik.
6. **Validasi kepatuhan audit trail** — pastikan log audit mencatat `'[ENCRYPTED]'` bukan nomor WA polos.
7. **Validasi startup `.env`** — pastikan `FERNET_KEY` tervalidasi saat startup aplikasi.
8. **Validasi hak penghapusan data (Right to Erasure)** sesuai UU PDP.

### 4.2. Di Luar Cakupan (OUT-OF-SCOPE)

- ❌ Perubahan skema database (DDL) tabel `pelanggan`.
- ❌ Implementasi fitur baru yang tidak disebutkan dalam dokumen SDLC.
- ❌ Modifikasi modul keamanan lain (bcrypt, JWT, RBAC) yang tidak terkait langsung.
- ❌ Perubahan dependensi library (`requirements.txt`) kecuali jika ditemukan versi yang tidak kompatibel.

### 4.3. Alur Pengerjaan

```
[1] Baca & Pahami Dokumen Referensi
         ↓
[2] Audit File Kode yang Sudah Ada
         ↓
[3] Perbaiki Bug Import yang Hilang
         ↓
[4] Validasi & Perkuat utils/crypto.py
         ↓
[5] Validasi & Perbaiki Mekanisme Pencarian WA
         ↓
[6] Validasi Penanganan Error & Audit Trail
         ↓
[7] Validasi & Lengkapi Unit Test
         ↓
[8] Validasi Startup .env (FERNET_KEY)
         ↓
[9] Jalankan Test Suite & Verifikasi
         ↓
[10] Review Akhir & Dokumentasi Perubahan
```

---

## 5. Instruksi Pengamanan Feature Lain

> **PERINGATAN KERAS**: Saat mengerjakan issue ini, kamu **WAJIB** memastikan hal-hal berikut:

1. **JANGAN** mengubah signature fungsi publik yang sudah dipanggil oleh modul lain kecuali menambahkan parameter opsional baru.
2. **JANGAN** mengubah logika bisnis di `cli/menu_transaksi.py` selain yang terkait langsung dengan enkripsi/dekripsi WhatsApp.
3. **JANGAN** mengubah format atau kolom tabel `audit_logs` — hanya pastikan data WhatsApp selalu dilog sebagai `'[ENCRYPTED]'`, bukan dalam bentuk teks polos.
4. **JANGAN** mengubah logika RBAC, JWT, atau bcrypt yang sudah berjalan di `middleware/`.
5. **JANGAN** menghapus atau memodifikasi test case yang sudah PASS. Hanya **tambahkan** test case baru jika perlu.
6. **JANGAN** mengubah file `main.py`, `config/settings.py`, atau `db/query_builder.py` kecuali ada bug yang teridentifikasi secara spesifik terkait issue ini.
7. **Pastikan** semua perubahan kompatibel dengan Python 3.14.2+ dan berjalan di Dual-OS (Windows 11 & Linux Debian 12).

---

## 6. Instruksi Kualitas Pengerjaan

1. **Kerjakan dengan rapi, bersih, tidak tergesa-gesa, dan tidak buru-buru.** Setiap baris kode harus diteliti ulang sebelum dianggap selesai.
2. **Setiap perubahan harus memiliki justifikasi** — tidak boleh ada perubahan spekulatif atau "just in case".
3. **Pastikan setiap fungsi yang dimodifikasi tetap memiliki docstring PEP 257 lengkap** dengan Args, Returns, Raises, dan contoh Example jika relevan.
4. **Pastikan setiap fungsi memiliki type hints lengkap** sesuai PEP 484 dan Python 3.14+ (gunakan `str | None` bukan `Optional[str]`).
5. **Pastikan Result Pattern** (`namedtuple('Result', ['is_success', 'data', 'error_msg'])`) digunakan secara konsisten untuk penanganan error, bukan exception throwing.
6. **Pastikan kode menggunakan logging standar** (`logging.getLogger()`) untuk debugging, bukan `print()` di layer logic/utils.

---

## 7. Instruksi Kelengkapan & Penandaan Data Kosong

1. **Jika ditemukan data atau informasi yang kosong/tidak ada** pada file referensi yang seharusnya ada, **TANDAI** dengan komentar di kode:
   ```python
   # TODO(#0142): Data [nama_data] tidak ditemukan di dokumen referensi [nama_dokumen].
   #              Harap konfirmasi ke pemilik proyek.
   ```
2. **Jika ditemukan inkonsistensi** antara dokumen referensi yang satu dengan yang lain, **TANDAI** dan **KOMUNIKASIKAN** dalam commit message atau komentar kode.
3. **Jika ada parameter konfigurasi yang belum didefinisikan** di `.env.example`, tambahkan dengan komentar penjelasan dan instruksi generate-nya.

---

## 8. Instruksi Tambahan Spesifik Kriptografi

Berikut adalah instruksi tambahan yang spesifik untuk ciri khas issue ini (enkripsi/dekripsi):

### 8.1. Penanganan Non-Deterministic Ciphertext Fernet

Fernet menggunakan timestamp dan IV acak pada setiap operasi enkripsi, sehingga `encrypt("08123")` menghasilkan ciphertext berbeda setiap kali dipanggil. Ini berdampak pada:

- **Pencarian pelanggan berdasarkan WhatsApp** — Tidak bisa langsung `WHERE whatsapp = %s` dengan hasil enkripsi baru.
- **Constraint UNIQUE pada kolom `whatsapp`** — Dua pendaftaran dengan nomor WA sama akan menghasilkan ciphertext berbeda, sehingga constraint UNIQUE di MySQL **TIDAK AKAN** menangkap duplikasi secara otomatis.

**Solusi yang sudah diimplementasikan** di `cli/menu_transaksi.py` (fungsi `_form_cari_riwayat_pelanggan`): sistem mengenkripsi nomor WA input, lalu mencari menggunakan `cari_pelanggan_by_whatsapp()`. **Pastikan** fungsi `cari_pelanggan_by_whatsapp()` di `db/query_builder.py` melakukan pendekatan yang benar (mengambil semua data lalu mencocokkan via dekripsi di memori, ATAU menggunakan hashing deterministik tambahan).

### 8.2. Perlindungan Kunci Fernet di Memori

- Kunci Fernet **WAJIB** dimuat dari `.env` melalui `config/settings.py`, **BUKAN** di-hardcode.
- Kunci **TIDAK BOLEH** dicetak ke terminal CLI (`print()`) atau dilog ke `audit_logs`.
- Setelah operasi enkripsi/dekripsi selesai, referensi kunci di variabel lokal akan di-garbage-collect oleh Python secara otomatis.

### 8.3. Kepatuhan UU PDP No. 27/2022

Pastikan implementasi memenuhi 3 pilar kepatuhan UU PDP:
1. **Enkripsi Reversible WhatsApp**: Kolom `whatsapp` di database **selalu** terenkripsi.
2. **Pembatasan Hak Baca**: Hanya peran `pemilik`, `pramuniaga`, `kasir` yang bisa melihat data CRM (sudah dijaga oleh RBAC decorator `@require_role('MENU-M8-001')`).
3. **Hak Penghapusan Data (Right to Erasure)**: **Pastikan ada** mekanisme bagi Pemilik untuk menghapus data pribadi pelanggan secara permanen dari database master atas permintaan pelanggan.

### 8.4. Penanganan Rotasi Kunci Fernet

Jika `FERNET_KEY` di `.env` dirotasi (diganti dengan kunci baru), maka **seluruh data WhatsApp yang sudah terenkripsi dengan kunci lama tidak bisa didekripsi dengan kunci baru**. Pastikan:
- Ada komentar WARNING di `utils/crypto.py` yang menjelaskan risiko rotasi kunci.
- Jika rotasi kunci dilakukan, **WAJIB** dilakukan re-enkripsi seluruh data `whatsapp` di tabel `pelanggan` menggunakan utilitas migrasi khusus.

---

## 9. Checklist Implementasi Low-Level (Step-by-Step)

### Fase 1: Pembacaan dan Pemahaman Dokumen Referensi

- [ ] Baca file `docs/sdlc/03_design/06_security_design.md` — fokus pada Bab 2.1 (prinsip Data Minimization), Bab 2.2 (THR-008), Bab 6.1 (Enkripsi Data at Rest), Bab 6.3 (UU PDP), Bab 6.4 (Validasi Input), Bab 12.2 nomor 4 (pseudocode), dan Bab 12.3 (`.env` config).
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — fokus pada Bab 2.2 (FP Murni), Bab 2.2.6 (Result Pattern), Bab 3 (Naming Conventions), Bab 6 (Docstring PEP 257), Bab 7 (Type Hints), Bab 10.7 (UU PDP Compliance), dan Bab 10.8 (System Logging).
- [ ] Baca file `docs/sdlc/04_implementation/03_module_structure.md` — fokus pada Bab 9.2 (`utils/crypto.py` signature) dan Bab 4.3 (`cli/menu_transaksi.py` M.8 CRM).
- [ ] Baca file `docs/sdlc/03_design/01_database_schema.sql` — fokus pada TABEL 03 `pelanggan` (baris 86-96).
- [ ] Baca file `docs/sdlc/narasi.txt` — fokus pada baris 92 (Database Pelanggan CRM) dan baris 89 (Manajemen Hak Akses Privasi).

### Fase 2: Audit dan Identifikasi Bug pada Kode yang Sudah Ada

- [ ] Buka file `utils/crypto.py` — verifikasi bahwa:
  - [ ] Fungsi `encrypt_whatsapp_number(wa_number: str, fernet_key: str) -> str` sudah ada dan signature-nya sesuai Module Structure Bab 9.2.
  - [ ] Fungsi `decrypt_whatsapp_number(encrypted_wa: str, fernet_key: str) -> str` sudah ada dan signature-nya sesuai.
  - [ ] Penanganan error (input kosong, kunci kosong, kunci invalid, exception Fernet) sudah komprehensif.
  - [ ] Docstring PEP 257 lengkap dengan Args, Returns.
  - [ ] Type hints lengkap sesuai Python 3.14+.
  - [ ] Header module docstring ada dan lengkap.
  - [ ] Logging menggunakan `logging.getLogger()`, bukan `print()`.
  - [ ] **CATAT** temuan: apakah ada kekurangan? Misalnya, apakah fungsi mengembalikan `Result` namedtuple atau string biasa?

- [ ] Buka file `cli/menu_transaksi.py` — verifikasi bahwa:
  - [ ] **KRITIS: Periksa apakah `from utils.crypto import encrypt_whatsapp_number, decrypt_whatsapp_number` ada di bagian import (baris 22-31).** Jika TIDAK ADA, ini adalah bug yang harus diperbaiki.
  - [ ] Fungsi `_form_daftar_pelanggan_baru()` memanggil `encrypt_whatsapp_number()` dengan benar (baris 249).
  - [ ] Fungsi `_form_cari_riwayat_pelanggan()` memanggil `encrypt_whatsapp_number()` untuk pencarian (baris 326) dan `decrypt_whatsapp_number()` untuk tampilan (baris 350).
  - [ ] Fungsi `_form_lihat_daftar_pelanggan()` memanggil `decrypt_whatsapp_number()` untuk setiap pelanggan di loop (baris 449).
  - [ ] Fungsi `_form_edit_pelanggan()` memanggil `decrypt_whatsapp_number()` untuk menampilkan data lama (baris 526) dan `encrypt_whatsapp_number()` untuk menyimpan data baru (baris 557).
  - [ ] Audit trail log menggunakan `'[ENCRYPTED]'` untuk value WhatsApp, bukan nomor polos (baris 279, 574, 580).
  - [ ] `FERNET_KEY` dimuat dari `config/settings.py` melalui `load_settings()`, bukan di-hardcode.
  - [ ] Decorator `@require_role('MENU-M8-001')` terpasang pada `form_crm_pelanggan()` (baris 154).

- [ ] Buka file `config/settings.py` — verifikasi bahwa:
  - [ ] `FERNET_KEY` dimuat dari `.env` dan divalidasi format Fernet-nya.
  - [ ] Jika `FERNET_KEY` kosong atau tidak valid, startup gagal dengan kode error `ERR-FILE-001`.

- [ ] Buka file `tests/test_crm_crypto.py` — verifikasi kelengkapan test case:
  - [ ] Test roundtrip (enkripsi lalu dekripsi = original).
  - [ ] Test different output (enkripsi 2x menghasilkan ciphertext berbeda).
  - [ ] Test wrong key (dekripsi dengan kunci salah).
  - [ ] Test empty input string.
  - [ ] Test empty key.
  - [ ] Test invalid key format.

- [ ] Buka file `tests/logic/test_crm_encryption.py` — verifikasi kelengkapan test case tambahan.

### Fase 3: Perbaikan Bug Import yang Hilang

- [ ] Buka file `cli/menu_transaksi.py`.
- [ ] Pada bagian `# 3. Local Modules` (sekitar baris 22-31), tambahkan baris import berikut **jika belum ada**:
  ```python
  from utils.crypto import encrypt_whatsapp_number, decrypt_whatsapp_number
  ```
- [ ] Tempatkan import ini sesuai urutan import standar (Bab 5.4.1 Coding Standard):
  1. Standard Library
  2. Third-Party
  3. Local Modules (di sini, setelah import local modules lainnya)
- [ ] Simpan file.
- [ ] Jalankan `python -c "from cli.menu_transaksi import form_crm_pelanggan"` untuk memverifikasi import tidak error.

### Fase 4: Validasi dan Penguatan `utils/crypto.py`

- [ ] Periksa apakah fungsi sudah mengembalikan `Result` namedtuple sesuai Coding Standard Bab 2.2.6, **ATAU** apakah fungsi mengembalikan string biasa (yang juga diperbolehkan untuk helper utility sederhana). Jika mengembalikan string biasa, pastikan penanganan error (return `""`) konsisten.
- [ ] Pastikan komentar WARNING tentang rotasi kunci ada:
  ```python
  # WARNING: Jika FERNET_KEY dirotasi, seluruh data whatsapp terenkripsi
  # di tabel pelanggan harus di-re-enkripsi menggunakan utilitas migrasi.
  # Lihat: Security Design Bab 6.5 — Kebijakan Rotasi Kredensial.
  ```
- [ ] Pastikan `_logger` menggunakan prefix `'abucom.utils.crypto'` — **sudah sesuai** di kode saat ini.
- [ ] Pastikan encoding `'utf-8'` digunakan secara eksplisit di `encode()` dan `decode()` — **sudah sesuai** di kode saat ini.
- [ ] Periksa apakah perlu menambahkan validasi format nomor WhatsApp (regex `^08[0-9]{8,11}$`) **di dalam** fungsi enkripsi, atau cukup di layer CLI (`validasi_nomor_whatsapp()`). Sesuai arsitektur 4-layer, validasi input **seharusnya** dilakukan di Presentation Layer (CLI), jadi **TIDAK PERLU** ditambahkan di `utils/crypto.py`. Namun tambahkan komentar penjelasan:
  ```python
  # CATATAN: Validasi format nomor WA dilakukan di layer CLI
  # (logic/safety_validator.py -> validasi_nomor_whatsapp)
  # sebelum memanggil fungsi ini. Fungsi ini hanya bertanggung jawab
  # atas operasi kriptografi, bukan validasi bisnis.
  ```

### Fase 5: Validasi Mekanisme Pencarian WhatsApp Terenkripsi

- [ ] Buka file `db/query_builder.py` dan cari fungsi `cari_pelanggan_by_whatsapp()`.
- [ ] Analisis bagaimana pencarian dilakukan:
  - **Skenario A**: Jika pencarian menggunakan `WHERE whatsapp = %s` dengan ciphertext baru — ini **TIDAK AKAN BERHASIL** karena Fernet non-deterministik. Ini adalah **bug**.
  - **Skenario B**: Jika pencarian mengambil semua pelanggan lalu mencocokkan via dekripsi di memori — ini **BENAR** tapi berat secara performa jika data banyak.
  - **Skenario C**: Jika ada kolom hash tambahan (misal `whatsapp_hash`) untuk pencarian deterministik — ini **OPTIMAL** tapi mungkin belum ada di DDL.
- [ ] **Jika Skenario A ditemukan**: Tandai sebagai bug dan perbaiki dengan pendekatan Skenario B (dekripsi di memori) sebagai solusi sementara, karena skala data UMKM lokal masih kecil (ratusan pelanggan). Tambahkan komentar:
  ```python
  # CATATAN: Pencarian dilakukan via dekripsi di memori karena Fernet
  # menghasilkan ciphertext non-deterministik. Untuk skala > 10.000
  # pelanggan, pertimbangkan menambah kolom whatsapp_hash (SHA-256)
  # untuk pencarian O(1).
  ```
- [ ] **Jika Skenario B sudah diimplementasikan**: Verifikasi bahwa dekripsi dilakukan dengan benar dan error handling ada.
- [ ] **Catat temuan** sebagai komentar `# TODO(#0142)` jika perlu perubahan skema database di masa depan.

### Fase 6: Validasi Penanganan Error dan Audit Trail

- [ ] Di `cli/menu_transaksi.py` fungsi `_form_daftar_pelanggan_baru()`:
  - [ ] Pastikan jika `encrypt_whatsapp_number()` mengembalikan string kosong `""`, ada penanganan error yang menampilkan `ERR-CRM-CRYPTO` ke CLI dan **TIDAK** menyimpan data kosong ke database.
  - [ ] Pastikan audit trail log menggunakan `'[ENCRYPTED]'` sebagai value WhatsApp di `new_val` dict.

- [ ] Di `cli/menu_transaksi.py` fungsi `_form_cari_riwayat_pelanggan()`:
  - [ ] Pastikan jika `decrypt_whatsapp_number()` mengembalikan string kosong (misalnya kunci salah), ada fallback yang menampilkan `'[GAGAL DEKRIPSI]'` atau pesan informatif ke pengguna.

- [ ] Di `cli/menu_transaksi.py` fungsi `_form_lihat_daftar_pelanggan()`:
  - [ ] Pastikan jika dekripsi gagal untuk satu pelanggan, loop tidak crash dan pelanggan tersebut tetap ditampilkan dengan nomor WA bertuliskan `'[GAGAL DEKRIPSI]'`.

- [ ] Di `cli/menu_transaksi.py` fungsi `_form_edit_pelanggan()`:
  - [ ] Pastikan data lama `old_val` di audit trail tetap menggunakan `'[ENCRYPTED]'`, bukan nomor WA polos yang baru saja didekripsi di memori.
  - [ ] Pastikan jika enkripsi WA baru gagal, perubahan **TIDAK** disimpan ke database.

### Fase 7: Validasi dan Lengkapi Unit Test

- [ ] Buka file `tests/test_crm_crypto.py` dan pastikan semua test case PASS:
  ```bash
  python -m pytest tests/test_crm_crypto.py -v
  ```
- [ ] Buka file `tests/logic/test_crm_encryption.py` dan pastikan semua test case PASS:
  ```bash
  python -m pytest tests/logic/test_crm_encryption.py -v
  ```
- [ ] Evaluasi apakah test case berikut sudah ada. Jika belum, **TAMBAHKAN**:
  - [ ] **Test nomor WA sangat panjang** (20 karakter, batas maksimal sesuai Security Design Bab 6.4).
  - [ ] **Test nomor WA dengan karakter non-numerik** — pastikan enkripsi tetap berhasil (validasi format ada di layer CLI, bukan di crypto).
  - [ ] **Test ciphertext yang dirusak/korup** — pastikan dekripsi mengembalikan string kosong, bukan exception.
  - [ ] **Test dengan kunci Fernet valid tapi berbeda panjang** — pastikan penanganan error konsisten.
  - [ ] **Test multiple roundtrip** — enkripsi dan dekripsi 100 nomor berbeda dalam satu test, pastikan semua cocok.

### Fase 8: Validasi Startup `.env` (FERNET_KEY)

- [ ] Buka file `config/settings.py`.
- [ ] Verifikasi bahwa `FERNET_KEY` dimuat dari `.env` menggunakan `os.getenv('FERNET_KEY')` atau `dotenv`.
- [ ] Verifikasi bahwa ada validasi format Fernet key (harus base64 44 karakter yang valid).
- [ ] Verifikasi bahwa jika `FERNET_KEY` kosong atau invalid, startup gagal dengan kode error `ERR-FILE-001`.
- [ ] Buka file `.env.example` dan pastikan instruksi generate kunci sudah ada:
  ```bash
  # python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode('utf-8'))"
  ```

### Fase 9: Jalankan Test Suite dan Verifikasi

- [ ] Jalankan **seluruh** test suite terkait:
  ```bash
  python -m pytest tests/test_crm_crypto.py tests/logic/test_crm_encryption.py -v --tb=short
  ```
- [ ] Pastikan **semua test PASS** tanpa exception.
- [ ] Jalankan test **keseluruhan** untuk memastikan tidak ada regresi:
  ```bash
  python -m pytest tests/ -v --tb=short
  ```
- [ ] Jika ada test yang FAIL karena perubahan yang dilakukan, **analisis** dan **perbaiki** tanpa mengubah test case yang sudah ada (kecuali test tersebut memang salah/outdated).

### Fase 10: Review Akhir dan Dokumentasi Perubahan

- [ ] Lakukan review visual terakhir pada setiap file yang dimodifikasi:
  - [ ] `utils/crypto.py` — apakah sudah rapi dan lengkap?
  - [ ] `cli/menu_transaksi.py` — apakah import sudah benar dan semua pemanggilan enkripsi/dekripsi sudah aman?
  - [ ] `tests/test_crm_crypto.py` — apakah coverage sudah memadai?
  - [ ] `config/settings.py` — apakah validasi FERNET_KEY sudah ada?
- [ ] Pastikan **tidak ada** nomor WhatsApp polos yang tertulis dalam:
  - [ ] Kode sumber (kecuali di test case dengan data dummy).
  - [ ] Log audit trail database (`audit_logs`).
  - [ ] Output `print()` atau `console.print()` di CLI (kecuali saat ditampilkan ke pengguna yang berhak).
- [ ] Buat commit message yang jelas:
  ```
  fix(#0142): tambah import crypto yang hilang di menu_transaksi.py
  feat(#0142): perkuat penanganan error dekripsi WhatsApp di CRM
  test(#0142): tambah test case untuk ciphertext korup dan multiple roundtrip
  ```
- [ ] **Dokumentasikan** semua temuan dan perubahan yang dilakukan.

---

## 10. Ringkasan Temuan Awal (Pre-Audit)

Berikut adalah temuan awal yang teridentifikasi sebelum pengerjaan dimulai:

| No | Temuan | Severity | File Terdampak | Status |
|:---:|---|:---:|---|:---:|
| 1 | **Import `encrypt_whatsapp_number` dan `decrypt_whatsapp_number` TIDAK ADA** di bagian import `cli/menu_transaksi.py`. Fungsi dipanggil di baris 249, 326, 350, 449, 526, 557 tanpa import. Ini akan menyebabkan `NameError` saat runtime. | 🔴 CRITICAL | `cli/menu_transaksi.py` | Belum diperbaiki |
| 2 | Mekanisme pencarian pelanggan by WhatsApp (`cari_pelanggan_by_whatsapp`) perlu diverifikasi apakah kompatibel dengan Fernet non-deterministik. | 🟡 HIGH | `db/query_builder.py` | Perlu audit |
| 3 | Belum ada komentar WARNING tentang risiko rotasi kunci Fernet di `utils/crypto.py`. | 🟢 LOW | `utils/crypto.py` | Perlu ditambahkan |
| 4 | Hak Penghapusan Data (Right to Erasure) sesuai UU PDP — perlu diverifikasi apakah menu penghapusan data pelanggan permanen sudah ada untuk peran Pemilik. | 🟡 HIGH | `cli/menu_transaksi.py` | Perlu audit |
| 5 | Test case untuk ciphertext korup, nomor WA sangat panjang, dan multiple roundtrip belum ada. | 🟢 LOW | `tests/test_crm_crypto.py` | Perlu ditambahkan |

---

## 11. Catatan Penutup

- **Kerjakan dengan teliti.** Setiap kali menyentuh file, baca keseluruhan konteks file tersebut terlebih dahulu. Jangan langsung mengedit tanpa memahami alur lengkap.
- **Jangan asumsikan.** Jika ada hal yang ambigu, tandai dengan `# TODO(#0142)` dan lanjutkan ke tugas berikutnya.
- **Pastikan backward compatibility.** Fungsi yang sudah ada dan dipanggil oleh modul lain tidak boleh berubah signature-nya secara breaking.
- **Dokumentasi adalah bagian dari pengerjaan.** Setiap fungsi yang disentuh harus keluar dengan docstring yang lebih baik dari sebelumnya.
- **Test adalah bukti keberhasilan.** Jangan anggap pekerjaan selesai sebelum semua test PASS.
