---
issue_id     : "#0136"
judul        : Feature Kelola Data Master Supplier
modul        : M.2 — Manajemen Inventaris, BOM & Stock Opname
prioritas    : High
status       : Open
tanggal      : 2026-06-08
assignee     : Junior Programmer / LLM AI Model
reviewer     : Claude Opus 4.6 (Thinking)
derivasi_srs : SRS-F-015
derivasi_brd : BR-F-39, BR-F-40
---

# Issue #0136 — Feature Kelola Data Master Supplier

## 0. Persona Pelaksana

> [!IMPORTANT]
> **Kamu adalah Senior Backend Developer & Data Master Specialist** yang ahli dalam:
> - Arsitektur aplikasi CLI berbasis Python 3.14+ dengan paradigma **Functional Programming (FP) murni**.
> - Pengelolaan data master CRUD (Create, Read, Update, Delete/Soft-delete) dengan integritas relasional penuh.
> - Penulisan parameterized SQL query (`%s` binding) yang aman dari SQL injection.
> - Implementasi Result Pattern (NamedTuple) sebagai error handling fungsional.
> - Audit trail logging terstruktur JSON untuk setiap modifikasi data sensitif.
> - Desain visual CLI terminal menggunakan pustaka `rich` dan `tabulate`.
> - Kepatuhan penuh terhadap standar SDLC, Coding Standard, dan Module Structure proyek AbuCom.
>
> Kamu bekerja dengan teliti, rapi, bersih, tidak tergesa-gesa, dan memastikan setiap baris kode yang kamu tulis sudah lengkap, teruji, dan tidak menimbulkan gangguan pada fitur lain.

---

## 1. Dokumen Referensi Utama

Bacalah dan ekstrak seluruh informasi yang relevan dari file-file referensi berikut **sebelum memulai pengerjaan**. Jangan lewatkan detail kecil apapun.

| No | File Referensi | Path Relatif | Relevansi |
|----|----------------|--------------|-----------|
| 1 | **Data Dictionary v1.2** | `docs/sdlc/02_analysis/05_data_dictionary.md` | Spesifikasi tabel `supplier` (Bab 3.4), tabel `utang_supplier` (Bab 3.20), tabel `riwayat_harga_supplier` (Bab 3.26), Domain Status Utang (Bab 4.16) |
| 2 | **Software Requirements Specification v1.2** | `docs/sdlc/02_analysis/02_software_requirements.md` | SRS-F-015 (Manajemen Data Supplier & Utang Usaha), SRS-F-013 (Riwayat Harga Beli Supplier/Price Tracking), Error codes ERR-VAL-013 & ERR-VAL-040 |
| 3 | **Database Schema DDL v1.2** | `schema.sql` | DDL fisik tabel `supplier` (TABEL 04, baris 98-111), tabel `utang_supplier` (TABEL 21, baris 532-553), index & constraint |
| 4 | **Module Structure v1.2** | `docs/sdlc/04_implementation/03_module_structure.md` | Fungsi `form_kelola_supplier()` di `cli/menu_inventaris.py` (Bab 4.4), SRS-to-File Mapping (Bab 15), tabel database diakses (Bab 4.4) |
| 5 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | FP murni, Result Pattern, Type Hints, Parameterized Query, Audit Trail, Error Codes, Konvensi penamaan |
| 6 | **Narasi Pemilik** | `docs/sdlc/narasi.txt` | Konteks bisnis manajemen supplier dan hutang usaha (baris 90) |
| 7 | **ERD Database v1.2** | `docs/sdlc/03_design/02_erd_database.md` | Relasi `supplier` → `utang_supplier`, `supplier` → `riwayat_harga_supplier`, `cabang` → `supplier` |
| 8 | **Security Design v1.1** | `docs/sdlc/03_design/06_security_design.md` | RBAC guard, Audit Trail JSON, Sanitasi Input CLI |
| 9 | **Implementasi Existing** | `cli/menu_inventaris.py` | Kode placeholder `form_kelola_supplier()` saat ini (baris 1470-1479), pola implementasi feature lain sebagai contoh referensi |

> [!NOTE]
> File `narasi.txt` **tetap diperlukan** sebagai referensi konteks bisnis. Baris 90 secara eksplisit menyebutkan: *"Saya ingin aplikasi bisa mencatat data vendor/supplier bahan baku, riwayat harga beli (untuk mencari harga termurah), serta mencatat jika saya memiliki hutang pembelian barang ke supplier."*

---

## 2. Rangkuman Data Referensi yang Relevan

### 2.1. Struktur Tabel `supplier` (dari Data Dictionary Bab 3.4 & schema.sql)

| No | Kolom | Tipe Data | Constraint | Null? | Default | Deskripsi |
|----|-------|-----------|------------|:-----:|---------|-----------|
| 1 | `id` | INT | PK, AI, NN | NOT NULL | - | ID unik supplier |
| 2 | `nama_supplier` | VARCHAR(100) | NN | NOT NULL | - | Nama badan usaha/perorangan vendor |
| 3 | `alamat` | TEXT | NN | NOT NULL | - | Alamat kantor/gudang pengiriman |
| 4 | `telp` | VARCHAR(30) | NN | NOT NULL | - | Nomor telepon aktif supplier |
| 5 | `cabang_id` | INT | FK → `cabang.id`, NN | NOT NULL | 1 | Cabang pencatat supplier |
| 6 | `created_at` | TIMESTAMP | NN | NOT NULL | CURRENT_TIMESTAMP | Waktu data dibuat |
| 7 | `updated_at` | TIMESTAMP | NN | NOT NULL | CURRENT_TIMESTAMP ON UPDATE | Waktu data diperbarui |

> [!WARNING]
> **Data Kosong Terdeteksi:** Kolom `email` disebutkan di SRS-F-015 input yang diperlukan (`nama_supplier`, `alamat`, `telp`, `email`) tetapi **TIDAK ADA** di Data Dictionary maupun DDL schema.sql. Ini perlu ditindaklanjuti. **Untuk saat ini, JANGAN tambahkan kolom `email`** karena DDL schema.sql dan Data Dictionary v1.2 adalah SSoT (Single Source of Truth) yang sudah di-approve. Tandai sebagai catatan untuk review berikutnya.

### 2.2. Struktur Tabel `utang_supplier` (dari Data Dictionary Bab 3.20 & schema.sql)

| No | Kolom | Tipe Data | Constraint | Null? | Default | Deskripsi |
|----|-------|-----------|------------|:-----:|---------|-----------|
| 1 | `id` | INT | PK, AI, NN | NOT NULL | - | ID unik utang supplier |
| 2 | `supplier_id` | INT | FK → `supplier.id`, NN | NOT NULL | - | Referensi vendor supplier |
| 3 | `nominal_utang` | DECIMAL(15,4) | NN, CK (>0) | NOT NULL | 0.0000 | Nominal tagihan awal |
| 4 | `sisa_utang` | DECIMAL(15,4) | NN, CK (>=0, <=nominal) | NOT NULL | 0.0000 | Sisa tagihan terutang |
| 5 | `tanggal_utang` | DATE | NN | NOT NULL | (CURRENT_DATE) | Tanggal transaksi nota |
| 6 | `tanggal_jatuh_tempo` | DATE | NN | NOT NULL | - | Batas tenggat pembayaran |
| 7 | `tanggal_pelunasan` | DATE | - | NULL | NULL | Waktu pembayaran pelunasan |
| 8 | `status_utang` | VARCHAR(20) | NN | NOT NULL | 'BELUM LUNAS' | Status pelunasan |
| 9 | `cabang_id` | INT | FK → `cabang.id`, NN | NOT NULL | 1 | Cabang pemilik utang |
| 10 | `created_at` | TIMESTAMP | NN | NOT NULL | CURRENT_TIMESTAMP | Waktu dibuat |
| 11 | `updated_at` | TIMESTAMP | NN | NOT NULL | CURRENT_TIMESTAMP ON UPDATE | Waktu diperbarui |

### 2.3. Domain Status Utang (dari Data Dictionary Bab 4.16)

- `'BELUM LUNAS'`: Utang aktif belum terbayar.
- `'LUNAS'`: Utang telah dilunasi penuh.

### 2.4. Hak Akses (RBAC)

Berdasarkan SRS-F-015 dan Module Structure Bab 4.4:
- **Allowed**: `pemilik`, `kepala_percetakan`, `gudang`
- **Denied**: `pramuniaga`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`

### 2.5. Error Codes yang Relevan (dari SRS v1.2 Bab 8)

| Kode Error | Pesan | Konteks |
|------------|-------|---------|
| `ERR-VAL-013` | `"ID supplier tidak terdaftar di database master!"` | Validasi `supplier_id` saat pencatatan harga beli |
| `ERR-VAL-040` | `"Tanggal jatuh tempo utang tidak boleh tanggal yang sudah lampau!"` | Validasi tanggal jatuh tempo utang supplier |

### 2.6. Lokasi Fungsi dalam Arsitektur

| Layer | File | Fungsi | Keterangan |
|-------|------|--------|------------|
| Presentation (cli/) | `cli/menu_inventaris.py` | `form_kelola_supplier()` | Entry point sub-menu supplier, saat ini PLACEHOLDER |
| Data Access (db/) | `db/query_builder.py` | Query functions baru | Fungsi CRUD parameterized untuk tabel `supplier` dan `utang_supplier` |
| Middleware | `middleware/audit_logger.py` | `log_audit_trail()` | Pencatatan audit trail JSON |
| Middleware | `middleware/rbac_guard.py` | `require_role()` | Guard otorisasi akses menu |

### 2.7. Menu ID Terkait

- `MENU-M2-009`: Menu Kelola Supplier & Utang (sudah terdaftar di navigasi `cli/menu_inventaris.py` baris 139-140)

---

## 3. Batasan, Cakupan & Alur Pengerjaan

### 3.1. Cakupan yang TERMASUK (In-Scope)

- [x] Sub-menu CRUD data master supplier (Tambah, Lihat Daftar, Edit, Hapus/Nonaktifkan)
- [x] Query builder parameterized untuk tabel `supplier`
- [x] Validasi input data supplier (nama, alamat, telp)
- [x] Audit trail logging untuk setiap operasi INSERT/UPDATE/DELETE pada tabel `supplier`
- [x] RBAC guard untuk pembatasan akses menu (pemilik, kepala_percetakan, gudang)
- [x] Sanitasi input CLI menggunakan `sanitasi_input_cli()`
- [x] Penanganan `cabang_id` dari `session_state` untuk multi-branch readiness
- [x] Tampilan visual CLI menggunakan `rich` Panel dan `tabulate` tabel
- [x] Unit test untuk validasi dan query builder supplier

### 3.2. Cakupan yang TIDAK TERMASUK (Out-of-Scope)

> [!CAUTION]
> Feature berikut **BUKAN** bagian dari issue ini. Jangan implementasikan.

- ❌ Pencatatan utang supplier (`utang_supplier`) — akan di-cover issue terpisah
- ❌ Riwayat harga beli supplier / price tracking (`riwayat_harga_supplier`, SRS-F-013) — issue terpisah
- ❌ Import data CSV supplier (`SRS-F-014`) — issue terpisah
- ❌ Notifikasi jatuh tempo H-3 utang supplier (`SRS-F-028`) — issue terpisah
- ❌ Modifikasi tabel database / skema DDL — tabel `supplier` sudah ada di `schema.sql`

### 3.3. Alur Pengerjaan

```
┌─────────────────────────────────────────────┐
│  TAHAP 1: Persiapan & Pembacaan Referensi   │
├─────────────────────────────────────────────┤
│  TAHAP 2: Implementasi Validasi (logic/)    │
├─────────────────────────────────────────────┤
│  TAHAP 3: Implementasi Query Builder (db/)  │
├─────────────────────────────────────────────┤
│  TAHAP 4: Implementasi CLI Menu (cli/)      │
├─────────────────────────────────────────────┤
│  TAHAP 5: Unit Testing (tests/)             │
├─────────────────────────────────────────────┤
│  TAHAP 6: Verifikasi & Review Akhir         │
└─────────────────────────────────────────────┘
```

---

## 4. Instruksi Pengerjaan

> [!IMPORTANT]
> **KAIDAH PENGERJAAN UTAMA:**
> 1. Kerjakan dengan **rapi, bersih, tidak tergesa-gesa dan tidak buru-buru** agar hasilnya maksimal.
> 2. Pastikan **kualitas kelengkapan** pengerjaan agar tidak selalu dipertanyakan atau diinterupsi karena ada yang kurang.
> 3. Pastikan **tidak menyenggol atau merusak** fitur lain yang sudah berjalan.
> 4. Jika ada data yang **kosong atau tidak tersedia** di file referensi, komunikasikan atau tandai dengan komentar `# TODO: DATA KOSONG — perlu konfirmasi` agar bisa ditindaklanjuti.
> 5. Ikuti **100%** standar yang tertulis di Coding Standard v1.2 dan Module Structure v1.2.

---

## 5. Checklist Implementasi Detail (Low-Level)

### TAHAP 1: Persiapan & Pembacaan Referensi

- [ ] Baca file `docs/sdlc/02_analysis/05_data_dictionary.md` Bab 3.4 (tabel `supplier`) — catat semua kolom, tipe data, constraint
- [ ] Baca file `docs/sdlc/02_analysis/02_software_requirements.md` bagian SRS-F-015 (baris 645-672) — catat input, proses, output, validasi, error handling
- [ ] Baca file `schema.sql` baris 98-111 — konfirmasi DDL tabel `supplier` sudah ada dan strukturnya sesuai Data Dictionary
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — pahami aturan FP murni, Result Pattern, type hints, parameterized query, audit trail
- [ ] Baca file `docs/sdlc/04_implementation/03_module_structure.md` Bab 4.4 — pahami spesifikasi `form_kelola_supplier()`, dependensi, dan hak akses
- [ ] Baca file `cli/menu_inventaris.py` baris 1470-1479 — lihat placeholder `form_kelola_supplier()` yang akan di-replace
- [ ] Baca file `cli/menu_inventaris.py` baris 100-160 — pahami pola navigasi menu dan routing `MENU-M2-009`
- [ ] Pelajari pola implementasi fitur **Kelola Master Barang** (`form_kelola_barang()`) dan **Kelola Satuan Ukur** (`form_kelola_satuan_ukur()`) di file `cli/menu_inventaris.py` sebagai referensi pola kode yang konsisten
- [ ] Pelajari pola query builder yang sudah ada di `db/query_builder.py`
- [ ] Pelajari pola validasi yang sudah ada di `logic/safety_validator.py`

---

### TAHAP 2: Implementasi Validasi Supplier (logic/safety_validator.py)

> **File target:** `logic/safety_validator.py`
> **Prinsip:** Pure function, immutable, Result Pattern, tanpa class, tanpa I/O side effect.

- [ ] **2.1.** Buat fungsi validasi `validasi_data_supplier(data_form: dict) -> Result`:
  - [ ] Validasi `nama_supplier`: wajib diisi (NOT NULL), tidak boleh kosong/whitespace only, maks 100 karakter
  - [ ] Validasi `alamat`: wajib diisi (NOT NULL), tidak boleh kosong/whitespace only
  - [ ] Validasi `telp`: wajib diisi (NOT NULL), tidak boleh kosong, maks 30 karakter, format angka/`+`/`-`/spasi yang wajar
  - [ ] Return `Result(is_success=True, data=cleaned_data, error_msg=None)` jika valid
  - [ ] Return `Result(is_success=False, data=None, error_msg="ERR-VAL-XXX: pesan")` jika tidak valid
  - [ ] Gunakan `sanitasi_input_cli()` untuk membersihkan setiap field input dari karakter kontrol
  - [ ] Implementasi `strip()` pada setiap string field sebelum validasi

- [ ] **2.2.** Buat fungsi validasi `validasi_supplier_id(raw_input: str) -> ValidationStatus`:
  - [ ] Validasi bahwa input bisa di-parse ke integer positif
  - [ ] Return `ValidationStatus(is_valid=True, cleaned_data=int_value, error_msg=None)` jika valid
  - [ ] Return `ValidationStatus(is_valid=False, cleaned_data=None, error_msg="...")` jika tidak valid

- [ ] **2.3.** Pastikan semua fungsi validasi baru memiliki:
  - [ ] Docstring PEP 257 Google Style lengkap (deskripsi, Args, Returns, Example)
  - [ ] Type hints lengkap pada parameter dan return value
  - [ ] Tidak ada mutasi state global
  - [ ] Tidak melempar exception yang tidak terkontrol

---

### TAHAP 3: Implementasi Query Builder (db/query_builder.py)

> **File target:** `db/query_builder.py`
> **Prinsip:** Parameterized query `%s`, Result Pattern, transaction ACID safe.

- [ ] **3.1.** Buat fungsi `query_daftar_supplier(db_connection, cabang_id: int) -> Result`:
  - [ ] SQL: `SELECT id, nama_supplier, alamat, telp, created_at, updated_at FROM supplier WHERE cabang_id = %s ORDER BY nama_supplier ASC`
  - [ ] Return `Result(True, list_of_dict, None)` jika berhasil
  - [ ] Return `Result(False, None, error_msg)` jika gagal
  - [ ] Handle empty result dengan return list kosong `[]`, bukan error

- [ ] **3.2.** Buat fungsi `query_detail_supplier(db_connection, supplier_id: int, cabang_id: int) -> Result`:
  - [ ] SQL: `SELECT id, nama_supplier, alamat, telp, cabang_id, created_at, updated_at FROM supplier WHERE id = %s AND cabang_id = %s`
  - [ ] Return dict data supplier jika ditemukan
  - [ ] Return `Result(False, None, "ERR-VAL-013: ...")` jika tidak ditemukan

- [ ] **3.3.** Buat fungsi `query_insert_supplier(db_connection, nama_supplier: str, alamat: str, telp: str, cabang_id: int) -> Result`:
  - [ ] SQL: `INSERT INTO supplier (nama_supplier, alamat, telp, cabang_id) VALUES (%s, %s, %s, %s)`
  - [ ] Return `Result(True, last_insert_id, None)` jika berhasil
  - [ ] Gunakan `cursor.lastrowid` untuk mendapatkan ID
  - [ ] Commit transaction setelah insert

- [ ] **3.4.** Buat fungsi `query_update_supplier(db_connection, supplier_id: int, nama_supplier: str, alamat: str, telp: str, cabang_id: int) -> Result`:
  - [ ] SQL: `UPDATE supplier SET nama_supplier = %s, alamat = %s, telp = %s WHERE id = %s AND cabang_id = %s`
  - [ ] Return `Result(True, rows_affected, None)` jika berhasil
  - [ ] Commit transaction setelah update

- [ ] **3.5.** Buat fungsi `query_delete_supplier(db_connection, supplier_id: int, cabang_id: int) -> Result`:
  - [ ] SQL: `DELETE FROM supplier WHERE id = %s AND cabang_id = %s`
  - [ ] Sebelum delete, cek apakah supplier memiliki relasi ke `utang_supplier` yang masih `BELUM LUNAS`
  - [ ] Jika ada utang aktif, **TOLAK penghapusan** dengan pesan error: `"ERR-REL-136: Supplier tidak dapat dihapus karena masih memiliki utang aktif yang belum lunas!"`
  - [ ] Sebelum delete, cek apakah supplier memiliki relasi ke `riwayat_harga_supplier`
  - [ ] Jika ada riwayat, tampilkan peringatan tapi tetap izinkan delete (dengan konfirmasi ekstra)
  - [ ] Return `Result(True, rows_affected, None)` jika berhasil

- [ ] **3.6.** Buat fungsi `query_cek_nama_supplier_duplikat(db_connection, nama_supplier: str, cabang_id: int, exclude_id: int | None = None) -> Result`:
  - [ ] SQL: Cek apakah `nama_supplier` sudah ada di cabang yang sama (case-insensitive)
  - [ ] Jika `exclude_id` diberikan (untuk edit), exclude ID tersebut dari pengecekan
  - [ ] Return `Result(True, existing_data, None)` jika duplikat ditemukan
  - [ ] Return `Result(True, None, None)` jika tidak duplikat

- [ ] **3.7.** Pastikan semua fungsi query baru memiliki:
  - [ ] Docstring PEP 257 lengkap
  - [ ] Type hints lengkap
  - [ ] Exception handling dengan `try-except` yang mengembalikan Result(False, ...)
  - [ ] Penggunaan parameterized query `%s` binding (DILARANG f-string untuk SQL)
  - [ ] Penutupan cursor di blok `finally`
  - [ ] Tidak ada commit otomatis di dalam fungsi yang bersifat bagian dari transaction chain

---

### TAHAP 4: Implementasi CLI Menu (cli/menu_inventaris.py)

> **File target:** `cli/menu_inventaris.py`
> **Prinsip:** Ganti placeholder `form_kelola_supplier()`, ikuti pola visual yang sudah ada.

- [ ] **4.1.** Hapus/replace placeholder `form_kelola_supplier()` (baris 1470-1479) dengan implementasi penuh

- [ ] **4.2.** Implementasi sub-menu utama `form_kelola_supplier()`:
  ```
  ╔══════════════════════════════════════════╗
  ║    KELOLA DATA MASTER SUPPLIER           ║
  ║    Dashboard > M.2 Inventaris > Supplier ║
  ╚══════════════════════════════════════════╝

    [1] Lihat Daftar Supplier
    [2] Tambah Supplier Baru
    [3] Edit Data Supplier
    [4] Hapus Supplier
    [0] Kembali ke Menu Inventaris
  ```
  - [ ] Gunakan `while True` loop untuk navigasi sub-menu
  - [ ] Terapkan RBAC check di awal fungsi: hanya `pemilik`, `kepala_percetakan`, `gudang` yang boleh akses
  - [ ] Gunakan `sanitasi_input_cli()` pada raw input pilihan menu
  - [ ] Tombol `0` untuk kembali (konsisten dengan standar navigasi)

- [ ] **4.3.** Implementasi `_lihat_daftar_supplier(session_state: dict) -> None`:
  - [ ] Clear terminal
  - [ ] Panel header breadcrumb: `Dashboard > M.2 > Supplier > Lihat Daftar`
  - [ ] Ambil koneksi database via `get_db_connection()`
  - [ ] Panggil `query_daftar_supplier(conn, cabang_id)`
  - [ ] Tampilkan tabel menggunakan `tabulate` dengan kolom: No, ID, Nama Supplier, Alamat, Telepon
  - [ ] Handle empty data: tampilkan pesan kuning `"Belum ada data supplier terdaftar."`
  - [ ] Tutup koneksi di blok `finally`
  - [ ] `input("Tekan Enter untuk kembali...")`

- [ ] **4.4.** Implementasi `_tambah_supplier(session_state: dict) -> None`:
  - [ ] Clear terminal
  - [ ] Panel header breadcrumb: `Dashboard > M.2 > Supplier > Tambah Supplier`
  - [ ] Input interaktif sekuensial:
    - `Masukkan Nama Supplier [0-Batal]: `
    - `Masukkan Alamat Supplier: `
    - `Masukkan Nomor Telepon Supplier: `
  - [ ] Sanitasi setiap input dengan `sanitasi_input_cli()`
  - [ ] Validasi menggunakan `validasi_data_supplier()`
  - [ ] Cek duplikasi nama via `query_cek_nama_supplier_duplikat()`
  - [ ] Tampilkan Panel konfirmasi data sebelum simpan
  - [ ] Konfirmasi `"Simpan data supplier ini? [Y/N]: "`
  - [ ] Jika Y: panggil `query_insert_supplier()`, log audit trail (`action_type='INSERT'`, `target_table='supplier'`), tampilkan pesan sukses hijau
  - [ ] Jika N: tampilkan pesan kuning pembatalan
  - [ ] Tutup koneksi di blok `finally`

- [ ] **4.5.** Implementasi `_edit_supplier(session_state: dict) -> None`:
  - [ ] Clear terminal
  - [ ] Panel header breadcrumb: `Dashboard > M.2 > Supplier > Edit Supplier`
  - [ ] Tampilkan daftar supplier terlebih dahulu (reuse `_lihat_daftar_supplier` atau inline query)
  - [ ] Input `"Masukkan ID Supplier yang akan diedit [0-Batal]: "`
  - [ ] Validasi ID menggunakan `validasi_supplier_id()`
  - [ ] Ambil data existing supplier via `query_detail_supplier()`
  - [ ] Tampilkan Panel data saat ini
  - [ ] Input sekuensial dengan default value (Enter = tetap):
    - `Nama Supplier [Enter=tetap 'xxx']: `
    - `Alamat [Enter=tetap 'xxx']: `
    - `Telepon [Enter=tetap 'xxx']: `
  - [ ] Validasi data baru menggunakan `validasi_data_supplier()`
  - [ ] Cek duplikasi nama baru (exclude ID yang sedang diedit) via `query_cek_nama_supplier_duplikat()`
  - [ ] Tampilkan Panel diff perubahan (data lama vs baru)
  - [ ] Konfirmasi `"Simpan perubahan? [Y/N]: "`
  - [ ] Jika Y: panggil `query_update_supplier()`, log audit trail (`action_type='UPDATE'`, `old_val=data_lama`, `new_val=data_baru`), tampilkan sukses
  - [ ] Tutup koneksi di blok `finally`

- [ ] **4.6.** Implementasi `_hapus_supplier(session_state: dict) -> None`:
  - [ ] Clear terminal
  - [ ] Panel header breadcrumb: `Dashboard > M.2 > Supplier > Hapus Supplier`
  - [ ] Tampilkan daftar supplier
  - [ ] Input `"Masukkan ID Supplier yang akan dihapus [0-Batal]: "`
  - [ ] Validasi ID
  - [ ] Ambil data supplier yang akan dihapus
  - [ ] Tampilkan data yang akan dihapus
  - [ ] Cek relasi utang aktif (query `utang_supplier` WHERE `supplier_id` AND `status_utang = 'BELUM LUNAS'`)
  - [ ] Jika ada utang aktif: tampilkan error merah `"ERR-REL-136: ..."` dan batalkan
  - [ ] Tampilkan peringatan merah `"⚠️ PERINGATAN: Penghapusan supplier bersifat PERMANEN!"`
  - [ ] Konfirmasi `"Konfirmasi hapus? [Y/N]: "`
  - [ ] Jika Y: panggil `query_delete_supplier()`, log audit trail (`action_type='DELETE'`, `old_val=data_dihapus`), tampilkan sukses
  - [ ] Tutup koneksi di blok `finally`

- [ ] **4.7.** Pastikan semua fungsi CLI baru:
  - [ ] Memiliki docstring PEP 257 lengkap
  - [ ] Menggunakan `_prompt_input()` helper yang sudah ada untuk input CLI
  - [ ] Menangani `EOFError` dan `KeyboardInterrupt` dengan graceful
  - [ ] Menggunakan `os.system('cls' if platform.system() == 'Windows' else 'clear')` untuk clear terminal
  - [ ] Menggunakan `console = Console()` dari `rich` untuk output
  - [ ] Menutup koneksi database di blok `finally` tanpa exception
  - [ ] Menggunakan format warna ANSI yang konsisten: hijau (sukses), merah (error), kuning (peringatan/kosong), biru (breadcrumb)

- [ ] **4.8.** Pastikan import tambahan yang diperlukan sudah ditambahkan di bagian atas file:
  - [ ] Import fungsi validasi baru dari `logic/safety_validator.py`
  - [ ] Import fungsi query baru dari `db/query_builder.py`
  - [ ] Jangan duplikasi import yang sudah ada

---

### TAHAP 5: Unit Testing (tests/)

> **File target:** `tests/test_kelola_supplier.py` (file BARU)

- [ ] **5.1.** Buat file test baru `tests/test_kelola_supplier.py`

- [ ] **5.2.** Implementasi test validasi supplier:
  - [ ] `test_validasi_data_supplier_valid()` — data lengkap dan benar
  - [ ] `test_validasi_data_supplier_nama_kosong()` — nama supplier kosong
  - [ ] `test_validasi_data_supplier_nama_terlalu_panjang()` — lebih dari 100 karakter
  - [ ] `test_validasi_data_supplier_alamat_kosong()` — alamat kosong
  - [ ] `test_validasi_data_supplier_telp_kosong()` — telepon kosong
  - [ ] `test_validasi_data_supplier_telp_terlalu_panjang()` — lebih dari 30 karakter
  - [ ] `test_validasi_supplier_id_valid()` — integer positif
  - [ ] `test_validasi_supplier_id_invalid_string()` — non-numeric
  - [ ] `test_validasi_supplier_id_negatif()` — nilai negatif

- [ ] **5.3.** Implementasi test query builder (mock database):
  - [ ] `test_query_daftar_supplier_kosong()` — database kosong returns list kosong
  - [ ] `test_query_insert_supplier_sukses()` — insert berhasil returns last_id
  - [ ] `test_query_detail_supplier_ditemukan()` — ID valid returns data
  - [ ] `test_query_detail_supplier_tidak_ditemukan()` — ID invalid returns error
  - [ ] `test_query_cek_duplikat_nama_ada()` — nama sudah ada
  - [ ] `test_query_cek_duplikat_nama_tidak_ada()` — nama unik

- [ ] **5.4.** Pastikan semua test:
  - [ ] Menggunakan `pytest` sebagai framework
  - [ ] Bersifat deterministik (tidak bergantung database riil, gunakan mock/patch)
  - [ ] Memiliki naming convention `test_<fungsi>_<skenario>()`
  - [ ] File header docstring sesuai template standard

---

### TAHAP 6: Verifikasi & Review Akhir

- [ ] **6.1.** Jalankan seluruh unit test baru:
  ```bash
  python -m pytest tests/test_kelola_supplier.py -v
  ```
  - [ ] Pastikan semua test PASSED tanpa error

- [ ] **6.2.** Jalankan unit test lama yang sudah ada untuk memastikan **tidak ada regresi**:
  ```bash
  python -m pytest tests/ -v --tb=short
  ```
  - [ ] Pastikan TIDAK ADA test yang sebelumnya PASSED menjadi FAILED

- [ ] **6.3.** Review konsistensi kode:
  - [ ] Semua nama fungsi mengikuti `snake_case` verb_noun
  - [ ] Semua variabel sesuai kolom database (e.g. `nama_supplier`, bukan `namaSupplier`)
  - [ ] Semua query menggunakan `%s` binding, bukan f-string
  - [ ] Semua fungsi memiliki docstring PEP 257
  - [ ] Semua fungsi memiliki type hints lengkap
  - [ ] Tidak ada `class` dalam logika bisnis
  - [ ] Tidak ada `float` untuk data keuangan (gunakan `Decimal` jika ada nominal)
  - [ ] Semua `conn.close()` berada dalam blok `finally`

- [ ] **6.4.** Review visual CLI:
  - [ ] Semua Panel memiliki breadcrumb yang benar
  - [ ] Warna ANSI konsisten (hijau/merah/kuning/biru)
  - [ ] Tabel `tabulate` ter-render rapi dan kolom sejajar
  - [ ] Pesan error mengikuti format `"⛔ ERR-XXX-YYY: pesan"`
  - [ ] Pesan sukses mengikuti format `"✓ pesan sukses"`
  - [ ] Navigasi back/batal konsisten (`0` untuk kembali, `0-Batal` di prompt)

- [ ] **6.5.** Review keamanan:
  - [ ] Semua input CLI disanitasi via `sanitasi_input_cli()`
  - [ ] Semua query SQL parameterized (zero SQL injection risk)
  - [ ] Audit trail ter-log untuk setiap INSERT/UPDATE/DELETE
  - [ ] RBAC guard mencegah akses role yang tidak berhak

- [ ] **6.6.** Review integritas fitur lain:
  - [ ] Tidak ada modifikasi pada fungsi-fungsi lain di `menu_inventaris.py` selain `form_kelola_supplier()`
  - [ ] Tidak ada modifikasi DDL/schema database
  - [ ] Import baru tidak menimbulkan circular import
  - [ ] Tidak ada penghapusan kode/komentar existing yang tidak berhubungan

---

## 6. Panduan Pola Kode (Pattern Reference)

### 6.1. Pola Sub-Menu (Referensi: `form_kelola_satuan_ukur`)

```python
def form_kelola_supplier(session_state: dict) -> None:
    """Sub-menu Kelola Data Master Supplier.

    (Ref: Module Structure Bab 4.4 - Modul M.2, SRS-F-015)

    Args:
        session_state (dict): Status sesi aktif pengguna.
    """
    # Otorisasi manual (pemilik, kepala_percetakan, gudang)
    role = session_state.get('role', '')
    if role not in ['pemilik', 'kepala_percetakan', 'gudang']:
        console.print("⛔ ERR-AUTH-003: Akses Ditolak: Hak Akses Gudang/Kepala Percetakan/Pemilik Dibutuhkan!", style="bold red")
        input("Tekan Enter untuk melanjutkan...")
        return

    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        console.print(Panel(
            "[bold white]KELOLA DATA MASTER SUPPLIER[/]\n"
            "[blue]Dashboard > M.2 Inventaris > Kelola Supplier[/]",
            style="bold white",
            expand=False
        ))
        console.print()
        console.print("  [1] Lihat Daftar Supplier")
        console.print("  [2] Tambah Supplier Baru")
        console.print("  [3] Edit Data Supplier")
        console.print("  [4] Hapus Supplier")
        console.print("  [0] Kembali ke Menu Inventaris")
        console.print()

        try:
            raw_pilihan = input("Pilihan Anda: ")
            pilihan = sanitasi_input_cli(raw_pilihan).strip()
        except (EOFError, KeyboardInterrupt):
            return

        if pilihan == '0':
            return
        elif pilihan == '1':
            _lihat_daftar_supplier(session_state)
        elif pilihan == '2':
            _tambah_supplier(session_state)
        elif pilihan == '3':
            _edit_supplier(session_state)
        elif pilihan == '4':
            _hapus_supplier(session_state)
        else:
            console.print("⛔ Pilihan tidak valid.", style="bold red")
            input("Tekan Enter untuk melanjutkan...")
```

### 6.2. Pola Query Builder (Referensi Existing)

```python
def query_daftar_supplier(db_connection, cabang_id: int) -> Result:
    """Mengambil seluruh data supplier berdasarkan cabang.

    Args:
        db_connection: Koneksi database MySQL aktif.
        cabang_id (int): ID cabang filter.

    Returns:
        Result: NamedTuple berisi is_success, data (list[dict]), error_msg.
    """
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = (
            "SELECT id, nama_supplier, alamat, telp, "
            "       created_at, updated_at "
            "FROM supplier "
            "WHERE cabang_id = %s "
            "ORDER BY nama_supplier ASC"
        )
        cursor.execute(query, (cabang_id,))
        rows = cursor.fetchall()
        return Result(True, rows if rows else [], None)
    except Exception as e:
        return Result(False, None, f"ERR-DB-136: Gagal mengambil daftar supplier. Detail: {str(e)}")
    finally:
        cursor.close()
```

### 6.3. Pola Audit Trail (Referensi Existing)

```python
# Setelah insert berhasil:
log_audit_trail(
    pengguna_id=user_id,
    action_type='INSERT',
    target_table='supplier',
    old_val=None,
    new_val={'id': last_id, 'nama_supplier': nama, 'alamat': alamat, 'telp': telp},
    cabang_id=cabang_id,
    db_connection=conn
)
```

---

## 7. Catatan Data Kosong & Inkonsistensi

> [!WARNING]
> **Temuan inkonsistensi yang perlu ditindaklanjuti (JANGAN perbaiki di issue ini):**

| No | Temuan | Sumber | Status |
|----|--------|--------|--------|
| 1 | Kolom `email` disebutkan di SRS-F-015 input yang diperlukan tetapi **tidak ada** di Data Dictionary v1.2 maupun DDL schema.sql | SRS-F-015 vs Data Dictionary 3.4 vs schema.sql | ⚠️ Perlu review — tandai di komentar kode |
| 2 | SRS-F-015 `Derivasi BRD` merujuk ke `BR-F-39` tetapi Data Dictionary merujuk ke `BR-F-40` untuk tabel `supplier` | SRS vs Data Dictionary | ⚠️ Inkonsistensi minor — tidak menghalangi implementasi |
| 3 | Tabel `riwayat_harga_supplier` belum ada di DDL `schema.sql` yang terpasang di root (hanya ada di `docs/sdlc/03_design/01_database_schema.sql`) | schema.sql root vs docs | ⚠️ Perlu verifikasi — diluar cakupan issue ini |

---

## 8. Instruksi Tambahan Spesifik untuk Data Master

> [!TIP]
> **Kaidah khusus untuk implementasi Data Master CRUD yang sering terlewat:**

1. **Pencegahan Duplikasi**: Data master supplier harus dicek duplikasinya berdasarkan `nama_supplier` per `cabang_id` sebelum INSERT. Gunakan case-insensitive comparison (`LOWER(nama_supplier) = LOWER(%s)`).

2. **Integritas Relasional saat Delete**: Sebelum menghapus supplier, wajib cek FK ke `utang_supplier` dan `riwayat_harga_supplier`. Jika ada utang aktif, **TOLAK** penghapusan. Ini mencegah orphaned records.

3. **Soft Delete vs Hard Delete**: Saat ini DDL `supplier` tidak memiliki kolom `is_aktif` (berbeda dengan `satuan_ukur`). Maka gunakan **hard delete** (`DELETE FROM`), bukan soft delete. Jika di kemudian hari ingin soft delete, itu perlu migrasi DDL terpisah.

4. **Audit Payload yang Lengkap**: Setiap field yang berubah harus tercatat di `old_val` dan `new_val` audit trail. Jangan hanya catat ID, catat seluruh row data.

5. **Koneksi Database**: Selalu ambil koneksi baru dari pool di awal setiap sub-flow function (`_lihat_`, `_tambah_`, `_edit_`, `_hapus_`), dan tutup di `finally`. JANGAN share koneksi antar sub-flow.

6. **Encoding & Sanitasi**: Pastikan semua teks yang diinput user disanitasi melalui `sanitasi_input_cli()` sebelum divalidasi dan disimpan. Ini mencegah karakter kontrol ASCII masuk ke database.

---

## 9. File yang Akan Dimodifikasi / Dibuat

| No | Aksi | Path File | Deskripsi Perubahan |
|----|------|-----------|---------------------|
| 1 | **MODIFY** | `logic/safety_validator.py` | Tambah fungsi `validasi_data_supplier()` dan `validasi_supplier_id()` |
| 2 | **MODIFY** | `db/query_builder.py` | Tambah 6 fungsi query CRUD supplier |
| 3 | **MODIFY** | `cli/menu_inventaris.py` | Replace placeholder `form_kelola_supplier()` + 4 sub-flow baru |
| 4 | **NEW** | `tests/test_kelola_supplier.py` | File test baru untuk validasi dan query supplier |

> [!CAUTION]
> **DILARANG** memodifikasi file selain yang tercantum di atas. Jangan modifikasi `schema.sql`, `main.py`, atau file fitur lain.

---

## 10. Kriteria Selesai (Definition of Done)

- [ ] Semua checklist di Tahap 1–6 sudah tercentang `[x]`
- [ ] Sub-menu Kelola Supplier bisa diakses dari menu Inventaris (opsi menu MENU-M2-009)
- [ ] CRUD Supplier (Lihat, Tambah, Edit, Hapus) berfungsi penuh tanpa error
- [ ] Validasi input mencegah data invalid masuk ke database
- [ ] Duplikasi nama supplier per cabang dicegah
- [ ] Penghapusan supplier dengan utang aktif ditolak
- [ ] Setiap operasi INSERT/UPDATE/DELETE tercatat di audit trail
- [ ] RBAC membatasi akses hanya untuk pemilik, kepala_percetakan, gudang
- [ ] Unit test PASSED 100%
- [ ] Tidak ada regresi pada test suite lama
- [ ] Kode mengikuti Coding Standard v1.2 (FP, Result Pattern, parameterized query, type hints)
- [ ] Visual CLI konsisten dengan pattern fitur lain
