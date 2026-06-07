---
issue_id    : "#0134"
judul       : "Feature: Kelola Komposisi BOM Produk Kustom"
prioritas   : High
status      : Open
modul       : M.2 — Inventaris, BOM & Stock Opname
menu_id     : MENU-M2-002
derivasi_uc : UC-007
derivasi_srs: SRS-F-007
target_file : docs/issue/0134_issue_feature_kelola_komposisi_bom_produk_kustom.md
dibuat      : 2026-06-07
---

# Issue #0134 — Feature: Kelola Komposisi BOM Produk Kustom

---

## 1. Persona Pelaksana

Kamu adalah **Senior Python Backend Engineer & Manufacturing Systems Specialist** — seorang ahli arsitektur data relasional MySQL, paradigma Functional Programming (FP) murni Python, dan domain manufaktur Bill of Materials (BOM) untuk sistem percetakan kustom.

Kamu memiliki otoritas penuh dan kompetensi mendalam untuk:
- Menulis pure functions Python tanpa `class` (FP murni) menggunakan `namedtuple` dan `decimal.Decimal`.
- Merancang dan mengeksekusi query SQL terparameter (`%s` binding) pada MySQL InnoDB dengan transaksi ACID dan `FOR UPDATE` locking.
- Mengimplementasikan CRUD (Create, Read, Update, Delete) pada tabel `bom_komposisi` sesuai skema DDL proyek.
- Membangun antarmuka CLI interaktif menggunakan library `rich` dan `tabulate` sesuai pola navigasi proyek.
- Menulis unit test deterministik terisolasi dengan `unittest` dan `unittest.mock`.

---

## 2. Konteks dan Tujuan Issue

### 2.1. Latar Belakang
Sistem AbuCom saat ini sudah memiliki:
- Tabel database `bom_komposisi` (DDL sudah terdefinisi di `docs/sdlc/03_design/01_database_schema.sql`).
- Fungsi pure calculation `hitung_biaya_komponen()` dan `hitung_hpp_produk()` di `logic/bom_hpp.py` yang sudah terimplementasi.
- Pseudocode lengkap untuk `daftar_bom_baru()` di `docs/sdlc/03_design/05_bom_hpp_design.md` Bagian 8.3.
- Fungsi `_lihat_detail_barang()` di `cli/menu_inventaris.py` yang sudah menampilkan komponen BOM (baris 862–886).
- Fungsi stub `form_komposisi_bom()` di `cli/menu_inventaris.py` (baris 897–906) yang masih `TODO: Implementasi form komposisi BOM`.

### 2.2. Tujuan
Mengimplementasikan **fitur CRUD lengkap** untuk mengelola komposisi Bill of Materials (BOM) produk cetak kustom. Fitur ini memungkinkan:
1. **Lihat** daftar komposisi BOM suatu produk induk.
2. **Tambah** komponen bahan baku baru ke formula BOM produk.
3. **Ubah** kuantitas pemakaian bahan baku yang sudah terdaftar di formula.
4. **Hapus** komponen bahan baku dari formula BOM.
5. **Hitung HPP** secara otomatis setelah setiap perubahan komposisi.

### 2.3. Cakupan Perubahan

| Layer | File Target | Jenis Perubahan |
|---|---|---|
| Data Access (db/) | `db/query_builder.py` | Tambah fungsi query CRUD `bom_komposisi` |
| Business Logic (logic/) | `logic/bom_hpp.py` | Tambah fungsi validasi dan pendaftaran BOM baru |
| Presentation (cli/) | `cli/menu_inventaris.py` | Implementasi `form_komposisi_bom()` lengkap |
| Testing (tests/) | `tests/test_bom_hpp.py` | Tambah unit test untuk fungsi-fungsi baru |

---

## 3. Dokumen Referensi

### 3.1. Daftar File Referensi Wajib Dibaca

Berikut adalah file referensi yang **WAJIB** dibaca dan diekstrak datanya sebelum memulai implementasi:

| # | File Referensi | Path Relatif | Relevansi |
|---|---|---|---|
| R-01 | Database Schema DDL | `docs/sdlc/03_design/01_database_schema.sql` | Definisi tabel `bom_komposisi` (baris 252–264) dan tabel `barang` |
| R-02 | BOM & HPP Design | `docs/sdlc/03_design/05_bom_hpp_design.md` | Formula kalkulasi, pseudocode, alur pendaftaran BOM, validasi, error codes |
| R-03 | Coding Standard | `docs/sdlc/04_implementation/01_coding_standard.md` | Aturan FP murni, penamaan, Result pattern, Decimal strategy |
| R-04 | Module Structure | `docs/sdlc/04_implementation/03_module_structure.md` | Spesifikasi file `logic/bom_hpp.py` dan `cli/menu_inventaris.py` |
| R-05 | CLI Interaction Flow | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur M.2 bagian 6.1 (baris 698–724): Menghitung HPP Berbasis BOM |
| R-06 | Access Control Matrix | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Matriks M2-002 (baris 257): hak akses per role |
| R-07 | Source: logic/bom_hpp.py | `logic/bom_hpp.py` | Kode existing: `BOMKomponen`, `Result`, `hitung_biaya_komponen()`, `hitung_hpp_produk()` |
| R-08 | Source: cli/menu_inventaris.py | `cli/menu_inventaris.py` | Stub `form_komposisi_bom()` dan pola implementasi existing |
| R-09 | Source: db/query_builder.py | `db/query_builder.py` | Pola query builder existing, `query_detail_barang()` dengan JOIN BOM |
| R-10 | Source: tests/test_bom_hpp.py | `tests/test_bom_hpp.py` | Test file existing yang perlu diperluas |

### 3.2. Instruksi Ekstraksi Konteks

- [ ] **Baca R-01**: Ekstrak definisi lengkap kolom tabel `bom_komposisi` — perhatikan constraint `uq_bom_komposisi_induk_bahan` (UNIQUE pada `barang_induk_id` + `bahan_baku_id`), FK CASCADE/RESTRICT rules, dan kolom `cabang_id`.
- [ ] **Baca R-02**: Ekstrak dari Bagian 5.2 (Alur Pendaftaran BOM Baru), Bagian 6.1 (Tabel Validasi Input CLI), Bagian 6.2 (Kode Error Standar: `ERR-VAL-007`, `ERR-VAL-008`, `ERR-STOCK-010`, `ERR-DB-007`), dan Bagian 8.3 (Pseudocode `daftar_bom_baru()`).
- [ ] **Baca R-03**: Ekstrak aturan paradigma FP murni — larangan `class`, wajib `namedtuple`, wajib `decimal.Decimal` presisi 4 desimal `ROUND_HALF_UP`, wajib `Result` pattern, wajib parameterized SQL `%s`.
- [ ] **Baca R-04**: Ekstrak spesifikasi file `logic/bom_hpp.py` (Bab 5.2) dan `cli/menu_inventaris.py` (Bab 4.4) — signature fungsi publik, dependensi impor, modul SRS di-cover.
- [ ] **Baca R-05**: Ekstrak alur interaksi CLI dari langkah 1–8 pada bagian 6.1 — perhatikan breadcrumb path `Dashboard > M.2 Inventaris > Penghitungan HPP Berbasis BOM`, format prompt input, dan format output visual hijau.
- [ ] **Baca R-06**: Ekstrak hak akses untuk `M2-002`: `pemilik` = FULL, `kepala_percetakan` = READ, `produksi_cetak` = INPUT, semua staf lain = DENY.
- [ ] **Baca R-07**: Catat NamedTuple `BOMKomponen`, `Result`, dan fungsi existing yang sudah terimplementasi vs yang masih `TODO`.
- [ ] **Baca R-08**: Catat pola implementasi menu existing (`_tambah_barang_baru`, `_lihat_detail_barang`) sebagai template untuk konsistensi — khususnya pola: `os.system('cls')`, `Panel()`, `_prompt_input()`, `get_db_connection()`, `try/finally: conn.close()`, `log_audit_trail()`.
- [ ] **Baca R-09**: Catat pola `Result` return type dari query builder, cara `cursor.execute()` dengan `%s` binding, dan pola `FOR UPDATE` locking.

---

## 4. Ringkasan Data Teknis dari Referensi

### 4.1. Skema Tabel `bom_komposisi` (dari R-01)

```sql
CREATE TABLE bom_komposisi (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    barang_induk_id INT NOT NULL,       -- FK ke barang.id (produk jadi kustom)
    bahan_baku_id INT NOT NULL,         -- FK ke barang.id (komponen bahan baku)
    kuantitas_desimal DECIMAL(15,4) NOT NULL DEFAULT 0.0000,
    cabang_id INT NOT NULL DEFAULT 1,   -- FK ke cabang.id
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT uq_bom_komposisi_induk_bahan UNIQUE (barang_induk_id, bahan_baku_id),
    CONSTRAINT fk_bom_komposisi_barang_induk_id FOREIGN KEY (barang_induk_id) 
        REFERENCES barang(id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_bom_komposisi_bahan_baku_id FOREIGN KEY (bahan_baku_id) 
        REFERENCES barang(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_bom_komposisi_cabang_id FOREIGN KEY (cabang_id) 
        REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Catatan Penting**:
- `ON DELETE CASCADE` pada `barang_induk_id`: hapus produk induk → otomatis hapus semua BOM terkait.
- `ON DELETE RESTRICT` pada `bahan_baku_id`: bahan baku **tidak bisa dihapus** jika masih digunakan di formula BOM.
- Constraint UNIQUE `(barang_induk_id, bahan_baku_id)`: satu produk induk tidak boleh memiliki bahan baku duplikat.

### 4.2. Hak Akses (dari R-06)

| Role | Level Akses | Keterangan |
|---|---|---|
| `pemilik` | ✅ FULL (CRUD) | Akses penuh ke semua operasi BOM |
| `kepala_percetakan` | 📖 READ | Hanya bisa melihat komposisi, tidak bisa mengubah |
| `produksi_cetak` | 📝 INPUT | Hanya bisa melihat komposisi (untuk referensi produksi) |
| Semua staf lain | ⛔ DENY | Akses ditolak sepenuhnya |

### 4.3. Kode Error Relevan (dari R-02)

| Kode | Pesan | Pemicu |
|---|---|---|
| `ERR-VAL-007` | `⛔ ERR-VAL-007: Input kuantitas bahan baku tidak valid (harus angka desimal positif > 0)!` | Kuantitas non-numerik atau ≤ 0 |
| `ERR-VAL-008` | `⛔ ERR-VAL-008: ID bahan baku tidak valid atau tidak terdaftar di database!` | Bahan baku tidak ditemukan |
| `ERR-DB-007` | `⛔ ERR-DB-007: Kegagalan database saat proses penyimpanan formula BOM!` | Error koneksi/transaksi MySQL |
| `ERR-AUTH-003` | `⛔ ERR-AUTH-003: Akses Ditolak: Hak Akses Pemilik Dibutuhkan!` | Role tidak diizinkan |

### 4.4. NamedTuple Existing (dari R-07)

```python
from collections import namedtuple
from decimal import Decimal, ROUND_HALF_UP

BOMKomponen = namedtuple('BOMKomponen', ['bahan_baku_id', 'nama_barang', 'kuantitas', 'harga_beli'])
Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
```

### 4.5. Data yang Kosong / Belum Tersedia

> [!WARNING]
> **Item berikut BELUM tersedia di referensi dan perlu diperhatikan:**
> 1. **Tidak ada `MENU-M2-002` sub-menu khusus "Kelola Komposisi BOM"** di CLI Interaction Flow — yang ada hanya "Hitung HPP BOM Desimal". Fitur CRUD komposisi BOM perlu diintegrasikan sebagai sub-flow dari menu ini, atau sebagai menu terpisah di bawah `form_komposisi_bom()`.
> 2. **Tidak ada query builder existing** untuk operasi INSERT/UPDATE/DELETE pada tabel `bom_komposisi` — hanya ada query SELECT JOIN di `query_detail_barang()`. Semua query CRUD harus dibuat dari nol.
> 3. **File `tests/test_bom_hpp.py` hampir kosong** (444 bytes) — perlu ditulis ulang/diperluas secara komprehensif.

---

## 5. Checklist Implementasi

### Fase A — Persiapan dan Ekstraksi Konteks

- [ ] **A.1** Baca file `docs/sdlc/03_design/01_database_schema.sql` baris 248–264. Catat skema tabel `bom_komposisi` secara lengkap.
- [ ] **A.2** Baca file `docs/sdlc/03_design/05_bom_hpp_design.md` secara keseluruhan. Rangkum:
  - [ ] A.2.1 — Alur Pendaftaran BOM Baru (Bagian 5.2, baris 339–348).
  - [ ] A.2.2 — Aturan Validasi Input (Bagian 6.1, baris 418–426).
  - [ ] A.2.3 — Kode Error Standar (Bagian 6.2, baris 428–436).
  - [ ] A.2.4 — Pseudocode `daftar_bom_baru()` (Bagian 8.3, baris 512–554).
  - [ ] A.2.5 — Self-Referencing FK rules (Bagian 3.4, baris 214–226).
- [ ] **A.3** Baca file `docs/sdlc/04_implementation/01_coding_standard.md`. Catat aturan:
  - [ ] A.3.1 — FP murni: tanpa `class`, wajib `namedtuple`, wajib `decimal.Decimal`.
  - [ ] A.3.2 — Result pattern: `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])`.
  - [ ] A.3.3 — SQL: wajib `%s` binding, dilarang string concatenation.
  - [ ] A.3.4 — Penamaan: `snake_case` untuk fungsi dan variabel, `PascalCase` untuk NamedTuple.
- [ ] **A.4** Baca file `docs/sdlc/04_implementation/03_module_structure.md` baris 416–445. Catat spesifikasi `logic/bom_hpp.py`.
- [ ] **A.5** Baca file `docs/sdlc/03_design/04_cli_interaction_flow.md` baris 698–724. Catat alur interaksi HPP BOM.
- [ ] **A.6** Baca file `docs/sdlc/02_analysis/06_access_control_matrix.md` baris 252–265. Catat matriks akses M.2.
- [ ] **A.7** Baca file `logic/bom_hpp.py`. Catat semua fungsi existing dan NamedTuple yang sudah ada.
- [ ] **A.8** Baca file `cli/menu_inventaris.py` baris 1–50 (imports), baris 153–220 (pola `form_kelola_barang`), dan baris 897–906 (stub `form_komposisi_bom`).
- [ ] **A.9** Baca file `db/query_builder.py` baris 800–860. Catat pola `query_detail_barang()` dan cara JOIN ke `bom_komposisi`.
- [ ] **A.10** Baca file `tests/test_bom_hpp.py`. Catat isi existing.

---

### Fase B — Implementasi Layer 3: Data Access (`db/query_builder.py`)

Tambahkan fungsi-fungsi query CRUD berikut di **akhir** file `db/query_builder.py` (sebelum baris terakhir, jika ada). Setiap fungsi harus:
- Menerima parameter `db_connection` dan `cabang_id`.
- Mengembalikan `Result` namedtuple.
- Menggunakan parameterized SQL (`%s` binding).
- Menangani exception dengan `try/except` dan mengembalikan `Result(False, None, error_msg)`.

#### B.1 — Fungsi `query_daftar_bom_by_induk()`
- [ ] **B.1.1** Tulis fungsi `query_daftar_bom_by_induk(db_connection, barang_induk_id: int, cabang_id: int) -> Result`.
- [ ] **B.1.2** Query SQL:
  ```sql
  SELECT bc.id, bc.bahan_baku_id, b.nama_barang, b.satuan_uom, 
         bc.kuantitas_desimal, b.harga_beli, b.stok_saat_ini,
         bc.created_at, bc.updated_at
  FROM bom_komposisi bc
  JOIN barang b ON bc.bahan_baku_id = b.id
  WHERE bc.barang_induk_id = %s AND bc.cabang_id = %s
  ORDER BY bc.id ASC
  ```
- [ ] **B.1.3** Return `Result(True, list_of_dict, None)` jika berhasil. Setiap dict berisi key: `id`, `bahan_baku_id`, `nama_barang`, `satuan_uom`, `kuantitas_desimal` (sebagai `Decimal`), `harga_beli` (sebagai `Decimal`), `stok_saat_ini` (sebagai `Decimal`), `created_at`, `updated_at`.
- [ ] **B.1.4** Konversi kolom numerik ke `Decimal` menggunakan `Decimal(str(row[x]))`.

#### B.2 — Fungsi `query_insert_bom_komponen()`
- [ ] **B.2.1** Tulis fungsi `query_insert_bom_komponen(db_connection, barang_induk_id: int, bahan_baku_id: int, kuantitas_desimal: Decimal, cabang_id: int) -> Result`.
- [ ] **B.2.2** Query SQL:
  ```sql
  INSERT INTO bom_komposisi (barang_induk_id, bahan_baku_id, kuantitas_desimal, cabang_id)
  VALUES (%s, %s, %s, %s)
  ```
- [ ] **B.2.3** Tangani `IntegrityError` untuk duplikasi constraint `uq_bom_komposisi_induk_bahan` — kembalikan `Result(False, None, "ERR-BOM-001: Bahan baku ini sudah terdaftar dalam formula BOM produk ini!")`.
- [ ] **B.2.4** Return `Result(True, cursor.lastrowid, None)` jika berhasil.
- [ ] **B.2.5** Lakukan `db_connection.commit()` setelah INSERT berhasil.

#### B.3 — Fungsi `query_update_bom_kuantitas()`
- [ ] **B.3.1** Tulis fungsi `query_update_bom_kuantitas(db_connection, bom_id: int, kuantitas_baru: Decimal, cabang_id: int) -> Result`.
- [ ] **B.3.2** Query SQL:
  ```sql
  UPDATE bom_komposisi 
  SET kuantitas_desimal = %s 
  WHERE id = %s AND cabang_id = %s
  ```
- [ ] **B.3.3** Periksa `cursor.rowcount == 0` — kembalikan `Result(False, None, "ERR-BOM-002: Data komposisi BOM tidak ditemukan!")`.
- [ ] **B.3.4** Return `Result(True, bom_id, None)` jika berhasil.
- [ ] **B.3.5** Lakukan `db_connection.commit()` setelah UPDATE berhasil.

#### B.4 — Fungsi `query_delete_bom_komponen()`
- [ ] **B.4.1** Tulis fungsi `query_delete_bom_komponen(db_connection, bom_id: int, cabang_id: int) -> Result`.
- [ ] **B.4.2** Query SQL:
  ```sql
  DELETE FROM bom_komposisi 
  WHERE id = %s AND cabang_id = %s
  ```
- [ ] **B.4.3** Periksa `cursor.rowcount == 0` — kembalikan `Result(False, None, "ERR-BOM-003: Data komposisi BOM tidak ditemukan atau sudah dihapus!")`.
- [ ] **B.4.4** Return `Result(True, bom_id, None)` jika berhasil.
- [ ] **B.4.5** Lakukan `db_connection.commit()` setelah DELETE berhasil.

#### B.5 — Fungsi `query_detail_bom_by_id()`
- [ ] **B.5.1** Tulis fungsi `query_detail_bom_by_id(db_connection, bom_id: int, cabang_id: int) -> Result`.
- [ ] **B.5.2** Query SQL:
  ```sql
  SELECT bc.id, bc.barang_induk_id, bc.bahan_baku_id, b.nama_barang, 
         b.satuan_uom, bc.kuantitas_desimal, b.harga_beli,
         bc.created_at, bc.updated_at
  FROM bom_komposisi bc
  JOIN barang b ON bc.bahan_baku_id = b.id
  WHERE bc.id = %s AND bc.cabang_id = %s
  ```
- [ ] **B.5.3** Return `Result(True, dict_data, None)` jika ditemukan, `Result(False, None, "ERR-BOM-002: ...")` jika tidak.

#### B.6 — Fungsi `query_daftar_barang_bahan_baku()`
- [ ] **B.6.1** Tulis fungsi `query_daftar_barang_bahan_baku(db_connection, cabang_id: int) -> Result`.
- [ ] **B.6.2** Query SQL — ambil daftar barang yang tipe-nya `'Bahan_Baku'` atau `'Retail_ATK'`:
  ```sql
  SELECT id, nama_barang, tipe_barang, satuan_uom, stok_saat_ini, harga_beli
  FROM barang
  WHERE cabang_id = %s AND tipe_barang IN ('Bahan_Baku', 'Retail_ATK')
  ORDER BY nama_barang ASC
  ```
- [ ] **B.6.3** Return `Result(True, list_of_dict, None)`.

#### B.7 — Fungsi `query_validasi_barang_induk()`
- [ ] **B.7.1** Tulis fungsi `query_validasi_barang_induk(db_connection, barang_induk_id: int, cabang_id: int) -> Result`.
- [ ] **B.7.2** Query SQL — validasi bahwa `barang_induk_id` merujuk ke produk cetak kustom yang valid:
  ```sql
  SELECT id, nama_barang, tipe_barang 
  FROM barang 
  WHERE id = %s AND cabang_id = %s
  ```
- [ ] **B.7.3** Return `Result(True, dict_data, None)` jika ditemukan, `Result(False, None, "ERR-VAL-008: Barang induk tidak ditemukan!")` jika tidak.

---

### Fase C — Implementasi Layer 2: Business Logic (`logic/bom_hpp.py`)

Tambahkan fungsi-fungsi logika bisnis berikut di **akhir** file `logic/bom_hpp.py`. Pastikan:
- Semua fungsi adalah **pure functions** (kecuali yang berinteraksi dengan database).
- Semua perhitungan menggunakan `decimal.Decimal` presisi 4 desimal `ROUND_HALF_UP`.
- Tidak ada penggunaan `float` dalam argumen atau kalkulasi.

#### C.1 — Fungsi `validasi_kuantitas_bom()`
- [ ] **C.1.1** Tulis fungsi `validasi_kuantitas_bom(kuantitas_raw: str) -> ValidationResult`.
- [ ] **C.1.2** Validasi:
  - Input tidak boleh kosong/None.
  - Input harus bisa di-parse menjadi `Decimal`.
  - Nilai harus `> Decimal('0.0000')` (positif, tidak boleh nol).
- [ ] **C.1.3** Jika valid: return `ValidationResult(True, decimal_value.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP), None)`.
- [ ] **C.1.4** Jika tidak valid: return `ValidationResult(False, None, "⛔ ERR-VAL-007: Input kuantitas bahan baku tidak valid (harus angka desimal positif > 0)!")`.

#### C.2 — Fungsi `validasi_bahan_baku_id()`
- [ ] **C.2.1** Tulis fungsi `validasi_bahan_baku_id(bahan_baku_id_raw: str) -> ValidationResult`.
- [ ] **C.2.2** Validasi:
  - Input tidak boleh kosong/None.
  - Input harus bisa di-parse menjadi `int`.
  - Nilai harus `> 0`.
- [ ] **C.2.3** Jika valid: return `ValidationResult(True, int_value, None)`.
- [ ] **C.2.4** Jika tidak valid: return `ValidationResult(False, None, "⛔ ERR-VAL-008: ID bahan baku tidak valid!")`.

#### C.3 — Fungsi `buat_audit_payload_bom()`
- [ ] **C.3.1** Tulis fungsi `buat_audit_payload_bom(action_type: str, old_data: dict | None, new_data: dict | None) -> tuple[str, str]`.
- [ ] **C.3.2** Pola sama persis dengan `buat_audit_payload_barang()` yang sudah ada di file ini.
- [ ] **C.3.3** Gunakan `_convert_decimals()` helper yang sudah ada untuk konversi `Decimal` ke `float` sebelum `json.dumps()`.

#### C.4 — Implementasi `proses_pemotongan_stok()` yang Sudah Ada
- [ ] **C.4.1** **PERBAIKI** fungsi `proses_pemotongan_stok()` yang saat ini masih `TODO` (baris 54–66) berdasarkan pseudocode dari R-02 Bagian 8.3 baris 556–607.
- [ ] **C.4.2** Implementasi harus:
  - Menggunakan `FOR UPDATE` locking pada query SELECT stok.
  - Mendukung stok negatif (tetap proses, catat `stok_minus_detected = True`).
  - Menulis audit trail untuk setiap pemotongan stok bahan.
  - Menggunakan transaksi ACID (`start_transaction()`, `commit()`, `rollback()`).
- [ ] **C.4.3** Sesuaikan return type. Tambahkan NamedTuple baru jika diperlukan:
  ```python
  ProcessResult = namedtuple('ProcessResult', ['is_success', 'stok_minus_detected', 'error_msg'])
  ```

---

### Fase D — Implementasi Layer 1: Presentation (`cli/menu_inventaris.py`)

Implementasikan `form_komposisi_bom()` sebagai **sub-menu interaktif** lengkap, menggantikan stub `TODO` di baris 897–906.

#### D.1 — Persiapan Import
- [ ] **D.1.1** Tambahkan import baru di bagian atas file `cli/menu_inventaris.py` (sesuai pola existing):
  ```python
  from logic.bom_hpp import (
      validasi_kuantitas_bom, validasi_bahan_baku_id,
      hitung_hpp_produk, hitung_biaya_komponen, BOMKomponen,
      buat_audit_payload_bom
  )
  from db.query_builder import (
      query_daftar_bom_by_induk, query_insert_bom_komponen,
      query_update_bom_kuantitas, query_delete_bom_komponen,
      query_detail_bom_by_id, query_daftar_barang_bahan_baku,
      query_validasi_barang_induk
  )
  ```
- [ ] **D.1.2** Pastikan tidak ada import duplikat dengan yang sudah ada.

#### D.2 — Implementasi `form_komposisi_bom()` sebagai Sub-Menu
- [ ] **D.2.1** Ganti stub `form_komposisi_bom()` dengan implementasi sub-menu yang berisi loop navigasi:
  ```
  ═══ KELOLA KOMPOSISI BOM PRODUK ═══
  Dashboard > M.2 Inventaris > Kelola Komposisi BOM
  
  Masukkan ID Produk Induk [0-Kembali]:
  
  [Setelah memilih produk induk, tampilkan sub-menu:]
  
  [1] Lihat Komposisi BOM & HPP
  [2] Tambah Komponen Bahan Baku
  [3] Ubah Kuantitas Komponen
  [4] Hapus Komponen dari Formula
  [0] Kembali ke Menu Inventaris
  ```
- [ ] **D.2.2** Otorisasi awal: cek `session_state.get('role')` — hanya `pemilik` dan `kepala_percetakan` boleh masuk. Untuk `produksi_cetak`, hanya tampilkan opsi [1] (Lihat). Staf lain ditolak dengan `ERR-AUTH-003`.
- [ ] **D.2.3** Validasi `barang_induk_id` menggunakan `query_validasi_barang_induk()`. Tampilkan nama produk induk di header sub-menu.

#### D.3 — Sub-fungsi `_lihat_komposisi_bom()`
- [ ] **D.3.1** Tulis fungsi `_lihat_komposisi_bom(session_state: dict, barang_induk_id: int) -> None`.
- [ ] **D.3.2** Panggil `query_daftar_bom_by_induk()`.
- [ ] **D.3.3** Tampilkan tabel `tabulate` dengan kolom: `No`, `ID BOM`, `Bahan Baku`, `Satuan`, `Qty Pakai`, `H.Beli/Satuan`, `Biaya Komponen`, `Stok Tersedia`.
- [ ] **D.3.4** Hitung dan tampilkan baris total HPP di akhir tabel: `TOTAL HPP PRODUK: Rp X.XXXX`.
- [ ] **D.3.5** Gunakan pewarnaan: merah untuk stok ≤ 0, kuning untuk stok ≤ 5.
- [ ] **D.3.6** Jika belum ada komponen: tampilkan `[yellow]Belum ada komponen bahan baku terdaftar untuk produk ini.[/]`.

#### D.4 — Sub-fungsi `_tambah_komponen_bom()`
- [ ] **D.4.1** Tulis fungsi `_tambah_komponen_bom(session_state: dict, barang_induk_id: int) -> None`.
- [ ] **D.4.2** Otorisasi: hanya `pemilik` dan `kepala_percetakan` yang boleh menambah.
- [ ] **D.4.3** Tampilkan daftar bahan baku yang tersedia (panggil `query_daftar_barang_bahan_baku()`) sebagai tabel referensi.
- [ ] **D.4.4** Prompt input:
  - `Masukkan ID Bahan Baku [0-Batal]: ` — validasi dengan `validasi_bahan_baku_id()`.
  - `Masukkan Kuantitas Pemakaian (desimal, contoh: 0.0500): ` — validasi dengan `validasi_kuantitas_bom()`.
- [ ] **D.4.5** Tampilkan konfirmasi sebelum simpan:
  ```
  ══ Konfirmasi Tambah Komponen BOM ══
  Produk Induk : [Nama Produk]
  Bahan Baku   : [Nama Bahan] (ID: X)
  Kuantitas    : X.XXXX [Satuan]
  Biaya        : Rp X.XXXX
  
  Simpan komponen ini? [Y/N]:
  ```
- [ ] **D.4.6** Panggil `query_insert_bom_komponen()`. Tangani error duplikasi.
- [ ] **D.4.7** Catat audit trail menggunakan `log_audit_trail()` dengan `action_type='INSERT'`, `target_table='bom_komposisi'`.
- [ ] **D.4.8** Tampilkan pesan sukses hijau: `[bold green]✓ Komponen bahan baku berhasil ditambahkan ke formula BOM![/]`.

#### D.5 — Sub-fungsi `_ubah_kuantitas_bom()`
- [ ] **D.5.1** Tulis fungsi `_ubah_kuantitas_bom(session_state: dict, barang_induk_id: int) -> None`.
- [ ] **D.5.2** Otorisasi: hanya `pemilik`.
- [ ] **D.5.3** Tampilkan daftar komposisi existing terlebih dahulu (reuse `_lihat_komposisi_bom` atau panggil query langsung).
- [ ] **D.5.4** Prompt input:
  - `Masukkan ID BOM yang akan diubah [0-Batal]: `
  - `Kuantitas Baru (desimal): ` — validasi dengan `validasi_kuantitas_bom()`.
- [ ] **D.5.5** Tampilkan diff perubahan:
  ```
  ══ Perubahan Kuantitas ══
  • Kuantitas: X.XXXX -> Y.YYYY
  • Biaya lama: Rp A.AAAA -> Biaya baru: Rp B.BBBB
  
  Simpan perubahan? [Y/N]:
  ```
- [ ] **D.5.6** Panggil `query_update_bom_kuantitas()`.
- [ ] **D.5.7** Catat audit trail dengan `action_type='UPDATE'`, `target_table='bom_komposisi'`, `old_val` dan `new_val` berisi data sebelum/sesudah.
- [ ] **D.5.8** Tampilkan pesan sukses hijau.

#### D.6 — Sub-fungsi `_hapus_komponen_bom()`
- [ ] **D.6.1** Tulis fungsi `_hapus_komponen_bom(session_state: dict, barang_induk_id: int) -> None`.
- [ ] **D.6.2** Otorisasi: hanya `pemilik`.
- [ ] **D.6.3** Tampilkan daftar komposisi existing terlebih dahulu.
- [ ] **D.6.4** Prompt input:
  - `Masukkan ID BOM yang akan dihapus [0-Batal]: `
- [ ] **D.6.5** Tampilkan konfirmasi penghapusan:
  ```
  ⚠️ PERINGATAN: Penghapusan komponen BOM bersifat PERMANEN!
  Bahan Baku : [Nama Bahan]
  Kuantitas  : X.XXXX [Satuan]
  
  Konfirmasi hapus? [Y/N]:
  ```
- [ ] **D.6.6** Panggil `query_delete_bom_komponen()`.
- [ ] **D.6.7** Catat audit trail dengan `action_type='DELETE'`, `target_table='bom_komposisi'`.
- [ ] **D.6.8** Tampilkan pesan sukses hijau.

---

### Fase E — Implementasi Layer Testing (`tests/test_bom_hpp.py`)

Tulis unit test deterministik untuk fungsi-fungsi baru. Semua test harus:
- Berjalan tanpa koneksi database riil (gunakan `unittest.mock.MagicMock`).
- Menggunakan `decimal.Decimal` (bukan `float`).
- Memvalidasi output sesuai presisi 4 desimal.

#### E.1 — Test `validasi_kuantitas_bom()`
- [ ] **E.1.1** Test input valid: `"0.0500"` → `ValidationResult(True, Decimal('0.0500'), None)`.
- [ ] **E.1.2** Test input valid: `"1.0000"` → valid.
- [ ] **E.1.3** Test input nol: `"0.0000"` → `ValidationResult(False, None, "ERR-VAL-007...")`.
- [ ] **E.1.4** Test input negatif: `"-1.5"` → invalid.
- [ ] **E.1.5** Test input non-numerik: `"abc"` → invalid.
- [ ] **E.1.6** Test input kosong: `""` → invalid.
- [ ] **E.1.7** Test input None: `None` → invalid.

#### E.2 — Test `validasi_bahan_baku_id()`
- [ ] **E.2.1** Test input valid: `"5"` → `ValidationResult(True, 5, None)`.
- [ ] **E.2.2** Test input nol: `"0"` → invalid.
- [ ] **E.2.3** Test input negatif: `"-1"` → invalid.
- [ ] **E.2.4** Test input non-numerik: `"abc"` → invalid.
- [ ] **E.2.5** Test input desimal: `"1.5"` → invalid (harus integer).

#### E.3 — Test `hitung_biaya_komponen()` (existing — perluas)
- [ ] **E.3.1** Test kasus stempel flash: `hitung_biaya_komponen(Decimal('0.0025'), Decimal('100000.0000'))` = `Decimal('250.0000')`.
- [ ] **E.3.2** Test kasus gagang stempel: `hitung_biaya_komponen(Decimal('1.0000'), Decimal('4500.0000'))` = `Decimal('4500.0000')`.
- [ ] **E.3.3** Test kasus pembulatan: `hitung_biaya_komponen(Decimal('0.3333'), Decimal('100.0000'))` — verifikasi pembulatan `ROUND_HALF_UP`.

#### E.4 — Test `hitung_hpp_produk()` (existing — perluas)
- [ ] **E.4.1** Test HPP stempel flash (2 komponen): expected = `Decimal('4750.0000')`.
- [ ] **E.4.2** Test HPP buku yasin (4 komponen): expected = `Decimal('17500.0000')`.
- [ ] **E.4.3** Test daftar kosong: expected = `Decimal('0.0000')`.

#### E.5 — Test `buat_audit_payload_bom()`
- [ ] **E.5.1** Test action INSERT: `old_data=None`, verifikasi `old_json = 'null'`.
- [ ] **E.5.2** Test action DELETE: `new_data=None`, verifikasi `new_json = 'null'`.
- [ ] **E.5.3** Test action UPDATE: verifikasi JSON mengandung field `kuantitas_desimal`.

---

### Fase F — Verifikasi dan Validasi

- [ ] **F.1** Jalankan semua unit test baru: `python -m pytest tests/test_bom_hpp.py -v`.
- [ ] **F.2** Jalankan seluruh test suite untuk memastikan tidak ada regresi: `python -m pytest tests/ -v --tb=short`.
- [ ] **F.3** Verifikasi tidak ada penggunaan `float` di seluruh kode baru (grep untuk `float(` di file yang diubah).
- [ ] **F.4** Verifikasi tidak ada penggunaan `class` di `logic/bom_hpp.py`.
- [ ] **F.5** Verifikasi semua query SQL menggunakan `%s` binding (tidak ada string concatenation).
- [ ] **F.6** Verifikasi semua fungsi baru memiliki docstring lengkap dengan Args dan Returns.
- [ ] **F.7** Verifikasi audit trail dicatat untuk setiap operasi CRUD pada `bom_komposisi`.
- [ ] **F.8** Verifikasi constraint UNIQUE `(barang_induk_id, bahan_baku_id)` ditangani gracefully di UI (pesan error user-friendly, bukan traceback).

---

## 6. Aturan dan Batasan Kritis

> [!CAUTION]
> **ATURAN KERAS yang TIDAK BOLEH dilanggar:**

### 6.1. Paradigma FP Murni
- **DILARANG** menggunakan `class` di `logic/bom_hpp.py`.
- **WAJIB** menggunakan `namedtuple` untuk semua struktur data.
- **WAJIB** menggunakan `decimal.Decimal` untuk semua kalkulasi finansial.
- **DILARANG** menggunakan `float` untuk argumen atau return value finansial.

### 6.2. Integritas Data
- **WAJIB** menggunakan parameterized SQL (`%s` binding) — **DILARANG** string concatenation pada query.
- **WAJIB** menangani transaksi ACID (`start_transaction()`, `commit()`, `rollback()`) pada operasi INSERT/UPDATE/DELETE.
- **WAJIB** menulis audit trail (`log_audit_trail()`) untuk setiap operasi mutasi data.

### 6.3. Presisi Desimal
- **WAJIB** menggunakan presisi 4 desimal: `DECIMAL(15,4)` di MySQL, `.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)` di Python.
- **DILARANG** menyimpan atau mengirim data float ke database.

### 6.4. Multi-Cabang
- **WAJIB** menyertakan `cabang_id` di setiap query CRUD (`WHERE ... AND cabang_id = %s`).
- Ambil `cabang_id` dari `session_state.get('cabang_id', 1)`.

### 6.5. Penanganan Error
- Semua error harus ditangani secara graceful — **TIDAK BOLEH** ada traceback yang terekspos ke pengguna.
- Gunakan kode error standar yang sudah didefinisikan di Bagian 4.3 issue ini.
- Return `Result(False, None, error_msg)` untuk error di layer logic/db.
- Tampilkan panel merah `console.print("⛔ ...", style="bold red")` untuk error di layer CLI.

### 6.6. Konsistensi Pola Kode
- Ikuti pola implementasi yang sudah ada di file-file existing.
- Gunakan `_prompt_input()` untuk input CLI (bukan `input()` langsung).
- Gunakan `os.system('cls' if platform.system() == 'Windows' else 'clear')` untuk clear screen.
- Gunakan `Panel()` dari `rich` untuk header dan konfirmasi.
- Gunakan `tabulate()` untuk tabel data.
- Tangani `(EOFError, KeyboardInterrupt)` di setiap loop menu CLI.

---

## 7. Contoh Alur Interaksi yang Diharapkan

### 7.1. Alur Tambah Komponen BOM (Skenario Sukses)

```
═══════════════════════════════════════════════
  KELOLA KOMPOSISI BOM PRODUK
  Dashboard > M.2 Inventaris > Kelola Komposisi BOM
═══════════════════════════════════════════════

Masukkan ID Produk Induk [0-Kembali]: 15

═══ Produk: Stempel Flash Bulat 40mm (ID: 15) ═══

  [1] Lihat Komposisi BOM & HPP
  [2] Tambah Komponen Bahan Baku
  [3] Ubah Kuantitas Komponen
  [4] Hapus Komponen dari Formula
  [0] Kembali ke Menu Inventaris

Pilihan Anda: 2

══ TAMBAH KOMPONEN BAHAN BAKU ══
Dashboard > M.2 > BOM > Tambah Komponen

Daftar Bahan Baku Tersedia:
+----+----+---------------------------+---------+----------+---------------+
| No | ID | Nama Bahan                | Satuan  |     Stok | H.Beli/Satuan |
+====+====+===========================+=========+==========+===============+
|  1 |  5 | Karet Flash Bulat         | M2      |  10.5000 | Rp 100,000.00 |
|  2 |  6 | Gagang Stempel Flash      | Pcs     |  50.0000 | Rp   4,500.00 |
|  3 |  7 | Tinta Stempel Khusus      | Ml      | 500.0000 | Rp     150.00 |
+----+----+---------------------------+---------+----------+---------------+

Masukkan ID Bahan Baku [0-Batal]: 5
Masukkan Kuantitas Pemakaian (desimal, contoh: 0.0500): 0.0025

══ Konfirmasi Tambah Komponen BOM ══
Produk Induk : Stempel Flash Bulat 40mm
Bahan Baku   : Karet Flash Bulat (ID: 5)
Kuantitas    : 0.0025 M2
Biaya        : Rp 250.0000

Simpan komponen ini? [Y/N]: Y

✓ Komponen bahan baku berhasil ditambahkan ke formula BOM!
```

### 7.2. Alur Lihat Komposisi & HPP

```
══ KOMPOSISI BOM: Stempel Flash Bulat 40mm (ID: 15) ══

+----+--------+---------------------------+---------+-----------+---------------+-----------------+
| No | ID BOM | Bahan Baku                | Satuan  | Qty Pakai | H.Beli/Satuan | Biaya Komponen  |
+====+========+===========================+=========+===========+===============+=================+
|  1 |     12 | Karet Flash Bulat         | M2      |    0.0025 | Rp 100,000.00 | Rp      250.00  |
|  2 |     13 | Gagang Stempel Flash      | Pcs     |    1.0000 | Rp   4,500.00 | Rp    4,500.00  |
+----+--------+---------------------------+---------+-----------+---------------+-----------------+
|    |        | TOTAL HPP PRODUK          |         |           |               | Rp    4,750.00  |
+----+--------+---------------------------+---------+-----------+---------------+-----------------+

[GREEN] HPP Riil Produk: Rp 4,750.0000 per unit
```

---

## 8. Urutan Pengerjaan yang Disarankan

1. **Fase A** (Baca dan ekstrak referensi) — ±15 menit
2. **Fase B** (Query builder) — ±30 menit
3. **Fase C** (Business logic) — ±20 menit
4. **Fase D** (CLI presentation) — ±45 menit
5. **Fase E** (Unit testing) — ±30 menit
6. **Fase F** (Verifikasi) — ±10 menit

**Estimasi total**: ±2.5 jam kerja efektif.

---

## 9. Catatan Penutup

- Implementasi ini merupakan **prasyarat** untuk fitur-fitur berikutnya: Kalkulasi HPP Otomatis saat Antrian Selesai (UC-007 flow trigger), Pencatatan Limbah Produksi (UC-008), dan Sinkronisasi ATK Internal (UC-010).
- Pastikan semua kode yang ditulis bersih, terdokumentasi, dan mengikuti standar proyek tanpa tergesa-gesa.
- Jika ada ambiguitas atau kebutuhan klarifikasi, tandai dengan komentar `# TODO: KLARIFIKASI #0134 — [deskripsi]` di kode.
