---
issue_id   : 0130
judul      : Feature — Kelola Data Master Barang Retail dan Bahan Baku
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
prioritas  : High
status     : Open
modul      : M.2 — Manajemen Inventaris, BOM & Stock Opname
versi      : 1.0
tanggal    : 2026-06-07
penyusun   : Principal Full-Stack Python Engineer & Inventory Domain Specialist
---

# Issue #0130 — Feature: Kelola Data Master Barang Retail dan Bahan Baku

---

## 1. Persona Eksekutor

### 1.1. Identitas Persona AI Eksekutor

| Atribut | Nilai |
|---|---|
| **Nama Persona** | Senior Python Backend Engineer & Inventory Management Specialist |
| **Keahlian Utama** | Implementasi CRUD fungsional murni (Pure FP) Python 3.14+, CLI terminal interaktif `rich`/`tabulate`, query transaksional MySQL InnoDB `DECIMAL(15,4)`, dan validasi input desimal presisi tinggi. |
| **Otoritas Teknis** | Memiliki otoritas penuh untuk mengimplementasikan seluruh fungsi pada 3 layer (Presentation `cli/`, Business Logic `logic/`, dan Data Access `db/`) khusus fitur kelola data master barang sesuai arsitektur 4-layer AbuCom. |
| **Batasan Tegas** | **DILARANG KERAS** menggunakan paradigma OOP/`class` pada alur bisnis inti. **DILARANG KERAS** menggunakan tipe `float` untuk kalkulasi nominal keuangan/stok. **WAJIB** menggunakan `decimal.Decimal` dan `namedtuple` secara konsisten. |

### 1.2. Tanggung Jawab Eksekutor
1. Mengekstrak dan memahami seluruh spesifikasi dari dokumen referensi SDLC yang telah ditentukan.
2. Mengimplementasikan kode Python fungsional murni yang **100% patuh** terhadap Coding Standard v1.1 dan Module Structure v1.1.
3. Menulis unit test dengan code coverage minimum **90%** untuk seluruh pure functions kalkulasi.
4. Memastikan setiap manipulasi data master barang dicatat ke `audit_logs` secara transaksional.
5. Memastikan setiap query menyertakan filter `cabang_id` untuk kepatuhan multi-cabang (M.9).

---

## 2. Dokumen Referensi Wajib

### 2.1. Daftar File Referensi (Prioritas Terurut)

Eksekutor **WAJIB** membaca, mengekstrak, dan merangkum seluruh detail data dari setiap dokumen referensi berikut **SEBELUM** menulis satu baris kode pun:

| # | Nama Dokumen | Path Relatif | Prioritas | Alasan Pemilihan |
|:---:|---|---|:---:|---|
| R-01 | **Database Schema DDL SQL v1.2** | `schema.sql` | **PRIMER** | SSoT (Single Source of Truth) skema fisik tabel `barang` dan `bom_komposisi`. Berisi definisi kolom, tipe data `DECIMAL(15,4)`, CHECK constraints (`harga_beli >= 0`, `min_grosir > 0`), FK ke `cabang`, dan komentar kolom. |
| R-02 | **Module Structure v1.2** | `docs/sdlc/04_implementation/03_module_structure.md` | **PRIMER** | Blueprint file-level: penempatan fungsi pada `cli/menu_inventaris.py` (Bab 4.4), `logic/bom_hpp.py` (Bab 5.2), `db/query_builder.py` (Bab 6.3). Berisi signature fungsi publik dan aturan dependensi layer. |
| R-03 | **Coding Standard v1.1** | `docs/sdlc/04_implementation/01_coding_standard.md` | **PRIMER** | Aturan FP murni, snake_case, Result Pattern `namedtuple`, type hints PEP 484, `decimal.Decimal` presisi 4, dan layout direktori. |
| R-04 | **Software Requirements Specification v1.2** | `docs/sdlc/02_analysis/02_software_requirements.md` | **PRIMER** | Spesifikasi teknis SRS-F-009 (Manajemen Satuan & Atribut Barang), SRS-F-002 (Multi-Skema Harga Dinamis), dan SRS-F-012 (Prediksi Re-Order Stok). |
| R-05 | **CLI Interaction Flow v1.2** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | **SEKUNDER** | Alur interaksi detail menu `MENU-M2-001` (Kelola Barang & UoM) — langkah-langkah prompt input, validasi, dan response error. |
| R-06 | **Access Control Matrix v1.2** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | **SEKUNDER** | Matriks otorisasi RBAC menu `M2-001`: `pemilik` (✅ FULL), `kepala_percetakan` (✅ FULL), `produksi_cetak` (📖 READ), `gudang` (✅ FULL). Staf lain ⛔ DENY. |
| R-07 | **BOM & HPP Design v1.2** | `docs/sdlc/03_design/05_bom_hpp_design.md` | **SEKUNDER** | Klasifikasi 3 jenis barang (`Retail_ATK`, `Bahan_Baku`, Barang Induk), Self-Referencing FK pada `bom_komposisi`, dan formula HPP desimal. |
| R-08 | **Data Dictionary v1.1** | `docs/sdlc/02_analysis/05_data_dictionary.md` | **TERSIER** | Deskripsi entitas `barang` dan `bom_komposisi` beserta kardinalitas dan business rules terkait. |

### 2.2. Instruksi Ekstraksi Referensi

Eksekutor **WAJIB** melakukan langkah-langkah berikut untuk setiap dokumen referensi:
1. **Baca** seluruh dokumen secara menyeluruh (bukan hanya bagian yang disebutkan).
2. **Ekstrak** setiap spesifikasi yang relevan dengan tabel `barang`: nama kolom, tipe data, constraint, default value, validasi, dan error code.
3. **Rangkum** dalam catatan kerja internal sebelum mulai coding agar tidak ada detail yang terlewat.
4. **Cross-reference** setiap spesifikasi dengan kode implementasi yang sudah ada pada codebase saat ini untuk mendeteksi inkonsistensi.

---

## 3. Rangkuman Data Referensi Hasil Ekstraksi

### 3.1. Skema Tabel `barang` (Dari R-01: schema.sql, Baris 116-138)

```sql
CREATE TABLE barang (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nama_barang VARCHAR(100) NOT NULL,
    tipe_barang VARCHAR(20) NOT NULL,       -- 'Retail_ATK' | 'Bahan_Baku'
    satuan_uom VARCHAR(20) NOT NULL,        -- 'Rim', 'Lembar', 'Pcs', 'Ml', 'Meter_Persegi'
    stok_saat_ini DECIMAL(15,4) NOT NULL DEFAULT 0.0000,
    harga_beli DECIMAL(15,4) NOT NULL DEFAULT 0.0000,
    harga_retail DECIMAL(15,4) NOT NULL DEFAULT 0.0000,
    harga_grosir DECIMAL(15,4) NOT NULL DEFAULT 0.0000,
    min_grosir DECIMAL(15,4) NOT NULL DEFAULT 1.0000,
    harga_mitra DECIMAL(15,4) NOT NULL DEFAULT 0.0000,
    cabang_id INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    -- CHECK Constraints:
    CONSTRAINT chk_barang_harga_beli CHECK (harga_beli >= 0),
    CONSTRAINT chk_barang_harga_retail CHECK (harga_retail >= 0),
    CONSTRAINT chk_barang_harga_grosir CHECK (harga_grosir >= 0),
    CONSTRAINT chk_barang_harga_mitra CHECK (harga_mitra >= 0),
    CONSTRAINT chk_barang_min_grosir CHECK (min_grosir > 0),
    CONSTRAINT fk_barang_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id)
) ENGINE=InnoDB;
```

### 3.2. Klasifikasi Tipe Barang (Dari R-07: BOM & HPP Design, Bagian 2.4)

| Tipe Barang | Nilai `tipe_barang` | Deskripsi Peran | Kolom Harga Relevan |
|---|---|---|---|
| **Retail ATK** | `'Retail_ATK'` | Barang eceran yang dijual langsung ke pelanggan (kertas HVS, tinta printer) DAN bisa diambil untuk produksi internal. | `harga_beli`, `harga_retail`, `harga_grosir`, `harga_mitra`, `min_grosir` |
| **Bahan Baku** | `'Bahan_Baku'` | Material mentah untuk produksi cetak kustom (karet stempel, gagang stempel). TIDAK dijual langsung ke pelanggan. | `harga_beli` saja (harga jual retail/grosir/mitra = `0.0000`) |

### 3.3. Matriks Hak Akses MENU-M2-001 (Dari R-06: ACM v1.2, Bab 4.3)

| Peran | Level Akses | Operasi Diizinkan |
|---|---|---|
| `pemilik` | ✅ FULL | Create, Read, Update, Delete |
| `kepala_percetakan` | ✅ FULL | Create, Read, Update, Delete |
| `gudang` | ✅ FULL | Create, Read, Update, Delete |
| `produksi_cetak` | 📖 READ | Read Only (lihat data barang saja) |
| `pramuniaga` | ⛔ DENY | Tidak bisa mengakses menu ini |
| `kasir` | ⛔ DENY | Tidak bisa mengakses menu ini |
| `desainer` | ⛔ DENY | Tidak bisa mengakses menu ini |
| `fotocopy_print` | ⛔ DENY | Tidak bisa mengakses menu ini |

### 3.4. Satuan UoM yang Didukung (Dari R-04: SRS-F-009)

Nilai valid untuk kolom `satuan_uom`:
- `'Rim'` — Satuan kertas grosir (1 Rim = 500 Lembar)
- `'Lembar'` — Satuan kertas eceran
- `'Pcs'` — Satuan barang fisik individual (gagang, cover)
- `'Ml'` — Satuan volume cairan (tinta)
- `'Meter_Persegi'` — Satuan area dimensi (karet stempel, bahan baliho)

### 3.5. Kode Error Relevan (Dari R-04 & R-05)

| Kode Error | Pemicu | Pesan |
|---|---|---|
| `ERR-VAL-009` | Input kuantitas stok non-numerik atau format desimal salah | `⛔ ERR-VAL-009: Input kuantitas harus berupa angka desimal valid (contoh: 12.50)!` |
| `ERR-VAL-002` | Data harga barang bernilai NULL di database | `⛔ ERR-VAL-002: Data harga barang tidak valid. Hubungi Pemilik.` |
| `ERR-AUTH-003` | Staf tanpa hak akses mencoba membuka menu M2-001 | `⛔ ERR-AUTH-003: Akses Ditolak: Anda tidak memiliki hak akses untuk menu ini!` |
| `ERR-DB-002` | Kegagalan eksekusi query SQL | `⛔ ERR-DB-002: Eksekusi query gagal.` |

---

## 4. Cakupan Fitur yang Diimplementasikan

### 4.1. Fitur Utama (Scope In)

Fitur "Kelola Data Master Barang Retail dan Bahan Baku" mencakup **operasi CRUD lengkap** pada tabel `barang`:

| # | Sub-Fitur | Operasi | Deskripsi |
|:---:|---|---|---|
| F-01 | **Lihat Daftar Barang** | READ | Menampilkan seluruh item barang dalam tabel `tabulate` terformat dengan filter berdasarkan `tipe_barang` dan pencarian nama. |
| F-02 | **Tambah Barang Baru** | CREATE | Formulir input tambah barang retail ATK atau bahan baku baru ke database dengan validasi lengkap. |
| F-03 | **Ubah Data Barang** | UPDATE | Formulir edit kolom-kolom master barang yang sudah ada (nama, harga, satuan, stok awal). |
| F-04 | **Hapus Barang** | DELETE | Penghapusan barang dari master dengan perlindungan FK (ON DELETE RESTRICT pada `bom_komposisi`). |
| F-05 | **Lihat Detail Barang** | READ | Menampilkan detail lengkap satu barang beserta info BOM terkait (jika ada). |

### 4.2. Fitur di Luar Cakupan (Scope Out)

Fitur-fitur berikut **TIDAK** termasuk dalam issue ini dan akan dikerjakan pada issue terpisah:
- ❌ Hitung HPP BOM Desimal (`MENU-M2-002`) — Issue terpisah
- ❌ Stock Opname (`MENU-M2-005`) — Issue terpisah
- ❌ Import CSV (`MENU-M2-008`) — Issue terpisah
- ❌ Kelola Supplier & Utang (`MENU-M2-009`) — Issue terpisah
- ❌ Sinkronisasi ATK Internal (`MENU-M2-004`) — Issue terpisah
- ❌ Price Tracking Supplier (`MENU-M2-007`) — Issue terpisah

---

## 5. Panduan Implementasi Langkah-demi-Langkah

### 5.1. TAHAP 1 — Data Access Layer (`db/query_builder.py`)

**Tujuan**: Menambahkan fungsi-fungsi query SQL terparameter khusus untuk operasi CRUD tabel `barang`.

**Aturan Layer**: File `db/query_builder.py` **HANYA** berisi wrapper eksekusi SQL. TIDAK BOLEH berisi logika bisnis, kalkulasi harga, atau formatting visual.

#### Checklist Implementasi:

- [ ] **5.1.1. Fungsi `query_daftar_barang`**

  ```python
  def query_daftar_barang(
      db_connection,
      cabang_id: int,
      tipe_barang: str | None = None,
      keyword: str | None = None
  ) -> Result:
      """Mengambil daftar master barang dengan filter opsional.

      Args:
          db_connection: Objek koneksi database aktif dari pool.
          cabang_id (int): ID cabang untuk filter multi-branch.
          tipe_barang (str | None): Filter opsional 'Retail_ATK' atau 'Bahan_Baku'.
          keyword (str | None): Kata kunci pencarian parsial pada kolom nama_barang.

      Returns:
          Result: NamedTuple (is_success, data: list[dict], error_msg).
      """
  ```
  - Query SQL:
    ```sql
    SELECT id, nama_barang, tipe_barang, satuan_uom, stok_saat_ini,
           harga_beli, harga_retail, harga_grosir, min_grosir, harga_mitra
    FROM barang
    WHERE cabang_id = %s
      [AND tipe_barang = %s]          -- opsional
      [AND nama_barang LIKE %s]       -- opsional, gunakan CONCAT('%', %s, '%')
    ORDER BY tipe_barang ASC, nama_barang ASC
    ```
  - Konversi semua kolom `DECIMAL` ke `decimal.Decimal` Python di dalam fungsi.
  - Gunakan parameterized query (`%s`) untuk mencegah SQL injection.

- [ ] **5.1.2. Fungsi `query_detail_barang`**

  ```python
  def query_detail_barang(
      db_connection,
      barang_id: int,
      cabang_id: int
  ) -> Result:
      """Mengambil detail lengkap satu barang beserta info BOM terkait.

      Args:
          db_connection: Objek koneksi database aktif.
          barang_id (int): ID barang yang akan ditampilkan.
          cabang_id (int): ID cabang untuk filter multi-branch.

      Returns:
          Result: NamedTuple (is_success, data: dict | None, error_msg).
      """
  ```
  - Query SQL Utama:
    ```sql
    SELECT id, nama_barang, tipe_barang, satuan_uom, stok_saat_ini,
           harga_beli, harga_retail, harga_grosir, min_grosir, harga_mitra,
           created_at, updated_at
    FROM barang
    WHERE id = %s AND cabang_id = %s
    ```
  - Query BOM Terkait (jika barang ini adalah barang induk kustom):
    ```sql
    SELECT bc.id, bc.bahan_baku_id, b.nama_barang AS nama_bahan,
           bc.kuantitas_desimal, b.harga_beli, b.satuan_uom
    FROM bom_komposisi bc
    JOIN barang b ON bc.bahan_baku_id = b.id
    WHERE bc.barang_induk_id = %s AND bc.cabang_id = %s
    ```
  - Gabungkan kedua hasil query ke dalam satu dict `{'barang': {...}, 'bom_komponen': [...]}`.

- [ ] **5.1.3. Fungsi `query_insert_barang`**

  ```python
  def query_insert_barang(
      db_connection,
      data_barang: dict
  ) -> Result:
      """Menyisipkan satu baris data barang baru ke tabel master.

      Args:
          db_connection: Objek koneksi database aktif.
          data_barang (dict): Dictionary berisi kolom-kolom barang.
              Keys wajib: nama_barang, tipe_barang, satuan_uom, stok_saat_ini,
                          harga_beli, harga_retail, harga_grosir, min_grosir,
                          harga_mitra, cabang_id.

      Returns:
          Result: NamedTuple (is_success, data: int (lastrowid), error_msg).
      """
  ```
  - Gunakan `execute_insert()` yang sudah ada di `query_builder.py`.
  - Query SQL:
    ```sql
    INSERT INTO barang (
        nama_barang, tipe_barang, satuan_uom, stok_saat_ini,
        harga_beli, harga_retail, harga_grosir, min_grosir, harga_mitra, cabang_id
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ```

- [ ] **5.1.4. Fungsi `query_update_barang`**

  ```python
  def query_update_barang(
      db_connection,
      barang_id: int,
      data_update: dict,
      cabang_id: int
  ) -> Result:
      """Memperbarui kolom-kolom master data barang yang sudah ada.

      Args:
          db_connection: Objek koneksi database aktif.
          barang_id (int): ID barang target update.
          data_update (dict): Dictionary berisi kolom yang diubah beserta nilai barunya.
          cabang_id (int): Filter multi-branch wajib pada klausa WHERE.

      Returns:
          Result: NamedTuple (is_success, data: int (rowcount), error_msg).
      """
  ```
  - Bangun klausa `SET` secara dinamis berdasarkan key di `data_update`.
  - Query SQL (contoh):
    ```sql
    UPDATE barang
    SET nama_barang = %s, harga_beli = %s, ...
    WHERE id = %s AND cabang_id = %s
    ```

- [ ] **5.1.5. Fungsi `query_delete_barang`**

  ```python
  def query_delete_barang(
      db_connection,
      barang_id: int,
      cabang_id: int
  ) -> Result:
      """Menghapus satu baris barang dari tabel master.

      Args:
          db_connection: Objek koneksi database aktif.
          barang_id (int): ID barang yang akan dihapus.
          cabang_id (int): Filter multi-branch wajib pada klausa WHERE.

      Returns:
          Result: NamedTuple (is_success, data: int (rowcount), error_msg).

      Catatan:
          - Jika barang masih direferensikan oleh bom_komposisi (sebagai bahan_baku_id),
            MySQL akan melemparkan error FK RESTRICT. Tangkap error ini dan kembalikan
            Result(False, None, "ERR-FK-005: Barang tidak dapat dihapus karena masih
            digunakan dalam formula BOM!").
      """
  ```
  - Query SQL:
    ```sql
    DELETE FROM barang WHERE id = %s AND cabang_id = %s
    ```
  - Tangkap `mysql.connector.Error` dengan errno `1451` (FK constraint fails) untuk memberikan pesan error yang user-friendly.

- [ ] **5.1.6. Fungsi `query_cek_nama_barang_duplikat`**

  ```python
  def query_cek_nama_barang_duplikat(
      db_connection,
      nama_barang: str,
      cabang_id: int,
      exclude_id: int | None = None
  ) -> Result:
      """Mengecek apakah nama barang sudah terdaftar di cabang yang sama.

      Args:
          db_connection: Objek koneksi database aktif.
          nama_barang (str): Nama barang yang akan dicek keunikannya.
          cabang_id (int): ID cabang untuk scope pengecekan.
          exclude_id (int | None): ID barang yang dikecualikan (untuk skenario update).

      Returns:
          Result: NamedTuple (is_success, data: bool (True jika duplikat), error_msg).
      """
  ```

---

### 5.2. TAHAP 2 — Business Logic Layer (`logic/bom_hpp.py`)

**Tujuan**: Menambahkan fungsi-fungsi validasi bisnis murni (pure functions) untuk kelola data master barang.

**Aturan Layer**: File `logic/bom_hpp.py` **HANYA** berisi fungsi murni (pure functions). TIDAK BOLEH memiliki efek samping I/O (`print()`, `input()`). TIDAK BOLEH menggunakan `class`. **WAJIB** menggunakan `namedtuple` untuk struktur data.

#### Checklist Implementasi:

- [ ] **5.2.1. Definisi NamedTuple Baru**

  Tambahkan definisi berikut di bagian atas file `logic/bom_hpp.py` (setelah import statements):

  ```python
  from decimal import Decimal, ROUND_HALF_UP
  from collections import namedtuple

  BarangRecord = namedtuple('BarangRecord', [
      'nama_barang', 'tipe_barang', 'satuan_uom', 'stok_saat_ini',
      'harga_beli', 'harga_retail', 'harga_grosir', 'min_grosir',
      'harga_mitra', 'cabang_id'
  ])

  ValidationResult = namedtuple('ValidationResult', [
      'is_valid', 'cleaned_data', 'error_msg'
  ])
  ```

- [ ] **5.2.2. Fungsi `validasi_data_barang`**

  ```python
  def validasi_data_barang(data: dict) -> ValidationResult:
      """Fungsi murni untuk memvalidasi dan membersihkan data input barang baru/edit.

      Args:
          data (dict): Dictionary mentah dari input CLI yang belum divalidasi.

      Returns:
          ValidationResult: NamedTuple berisi status validasi, data bersih, dan pesan error.

      Aturan Validasi Bisnis:
          1. nama_barang: wajib diisi, tidak boleh kosong, maks 100 karakter.
          2. tipe_barang: wajib bernilai 'Retail_ATK' atau 'Bahan_Baku'.
          3. satuan_uom: wajib bernilai salah satu dari ['Rim', 'Lembar', 'Pcs', 'Ml', 'Meter_Persegi'].
          4. stok_saat_ini: wajib numerik desimal >= 0 (parsing ke Decimal).
          5. harga_beli: wajib numerik desimal >= 0.
          6. harga_retail: wajib numerik desimal >= 0 (untuk Bahan_Baku boleh 0).
          7. harga_grosir: wajib numerik desimal >= 0 (untuk Bahan_Baku boleh 0).
          8. min_grosir: wajib numerik desimal > 0 (default 1.0000).
          9. harga_mitra: wajib numerik desimal >= 0 (untuk Bahan_Baku boleh 0).
         10. Jika tipe_barang == 'Bahan_Baku', set harga_retail, harga_grosir,
             harga_mitra = Decimal('0.0000') secara otomatis (bahan baku tidak dijual langsung).
      """
  ```
  - Setiap validasi numerik harus menggunakan `try/except` untuk menangkap `decimal.InvalidOperation`.
  - Setiap nilai desimal harus di-quantize ke 4 digit: `.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)`.

- [ ] **5.2.3. Fungsi `buat_audit_payload_barang`**

  ```python
  def buat_audit_payload_barang(
      action_type: str,
      old_data: dict | None,
      new_data: dict | None
  ) -> tuple[str, str]:
      """Fungsi murni untuk menyusun payload JSON audit trail perubahan data barang.

      Args:
          action_type (str): Tipe aksi ('INSERT', 'UPDATE', 'DELETE').
          old_data (dict | None): Data sebelum perubahan (None untuk INSERT).
          new_data (dict | None): Data setelah perubahan (None untuk DELETE).

      Returns:
          tuple[str, str]: (old_value_json, new_value_json) siap INSERT ke audit_logs.
      """
  ```
  - Gunakan `json.dumps()` untuk membentuk string JSON.
  - Konversi `Decimal` ke `float` hanya untuk serialisasi JSON.

- [ ] **5.2.4. Fungsi `hitung_margin_barang`**

  ```python
  def hitung_margin_barang(harga_jual: Decimal, harga_beli: Decimal) -> Decimal:
      """Fungsi murni untuk menghitung persentase margin keuntungan kotor.

      Formula: Margin (%) = ((harga_jual - harga_beli) / harga_jual) * 100
      Mitigasi: Jika harga_jual == 0, return Decimal('0.00').

      Args:
          harga_jual (Decimal): Harga jual satuan (retail/grosir/mitra).
          harga_beli (Decimal): Harga pengadaan/beli dari supplier.

      Returns:
          Decimal: Persentase margin keuntungan, dibulatkan 2 desimal.
      """
  ```

---

### 5.3. TAHAP 3 — Presentation Layer (`cli/menu_inventaris.py`)

**Tujuan**: Mengimplementasikan antarmuka CLI interaktif untuk fitur kelola data master barang.

**Aturan Layer**: File `cli/menu_inventaris.py` **DIPERBOLEHKAN** memiliki efek samping I/O (`print()`, `input()`). TIDAK BOLEH melakukan kalkulasi bisnis langsung. TIDAK BOLEH membangun string query SQL.

#### Checklist Implementasi:

- [ ] **5.3.1. Import Dependencies**

  Tambahkan import berikut di bagian atas `cli/menu_inventaris.py`:
  ```python
  from decimal import Decimal, InvalidOperation
  from rich.console import Console
  from rich.panel import Panel
  from rich.table import Table
  from tabulate import tabulate

  from db.db_connector import get_db_connection
  from db.query_builder import (
      query_daftar_barang, query_detail_barang, query_insert_barang,
      query_update_barang, query_delete_barang, query_cek_nama_barang_duplikat
  )
  from logic.bom_hpp import validasi_data_barang, buat_audit_payload_barang
  from logic.safety_validator import sanitasi_input_cli
  from middleware.rbac_guard import require_role
  from middleware.audit_logger import log_audit_trail

  console = Console()
  ```

- [ ] **5.3.2. Implementasi `form_kelola_barang` (CRUD Hub)**

  Ubah fungsi placeholder `form_kelola_barang` menjadi implementasi penuh. Fungsi ini bertindak sebagai **hub navigasi CRUD** yang menampilkan sub-menu:

  ```
  ╔══════════════════════════════════════════════════╗
  ║     Dashboard > M.2 Inventaris > Kelola Barang   ║
  ╚══════════════════════════════════════════════════╝

  [1] Lihat Daftar Barang
  [2] Tambah Barang Baru
  [3] Ubah Data Barang
  [4] Hapus Barang
  [5] Lihat Detail Barang
  [0] Kembali ke Menu Inventaris

  Pilihan Anda [0-5]:
  ```

  **Alur interaksi detail:**
  1. Tampilkan breadcrumb header menggunakan `rich.Panel`.
  2. Tampilkan daftar sub-menu numerik.
  3. Tangkap input pilihan, sanitasi menggunakan `sanitasi_input_cli()`.
  4. Routing ke fungsi handler yang sesuai berdasarkan pilihan.
  5. Setelah handler selesai, kembali ke sub-menu ini (loop).
  6. Pilihan `0` kembali ke `show_menu_inventaris`.

- [ ] **5.3.3. Implementasi Sub-Fitur: Lihat Daftar Barang (F-01)**

  ```python
  def _lihat_daftar_barang(session_state: dict) -> None:
      """Menampilkan tabel daftar master barang terformat tabulate.

      Alur:
          1. Tampilkan prompt filter: [1-Semua, 2-Retail ATK, 3-Bahan Baku].
          2. Tampilkan prompt pencarian opsional: "Cari nama barang (Enter=skip):".
          3. Panggil query_daftar_barang() dari db layer.
          4. Format output menggunakan tabulate dengan kolom:
             | No | ID | Nama Barang | Tipe | Satuan | Stok | H.Beli | H.Retail | H.Grosir | H.Mitra |
          5. Terapkan warna: stok <= 5 tampilkan warna kuning, stok <= 0 warna merah.
          6. Jika data kosong, tampilkan "[YELLOW] Tidak ada data barang ditemukan."
      """
  ```

- [ ] **5.3.4. Implementasi Sub-Fitur: Tambah Barang Baru (F-02)**

  ```python
  def _tambah_barang_baru(session_state: dict) -> None:
      """Formulir input tambah barang retail ATK atau bahan baku baru.

      Alur:
          1. Tampilkan header: "Dashboard > M.2 > Kelola Barang > Tambah Barang Baru"
          2. Prompt Tipe Barang: [1-Retail ATK, 2-Bahan Baku] [0-Batal]
          3. Prompt Nama Barang: (VARCHAR max 100 char, wajib)
          4. Prompt Satuan UoM: [1-Rim, 2-Lembar, 3-Pcs, 4-Ml, 5-Meter_Persegi]
          5. Prompt Stok Awal: (DECIMAL, wajib, >= 0. Contoh: 12.5000)
          6. Prompt Harga Beli/HPP: (DECIMAL, wajib, >= 0)
          7. JIKA tipe = 'Retail_ATK':
             a. Prompt Harga Retail: (DECIMAL, wajib, >= 0)
             b. Prompt Harga Grosir: (DECIMAL, wajib, >= 0)
             c. Prompt Min Grosir: (DECIMAL, wajib, > 0, default 1.0000)
             d. Prompt Harga Mitra: (DECIMAL, wajib, >= 0)
          8. JIKA tipe = 'Bahan_Baku': set harga retail/grosir/mitra = 0 otomatis.
          9. Panggil validasi_data_barang() dari logic layer.
         10. Jika validasi gagal: tampilkan error merah, kembali ke awal form.
         11. Cek duplikasi nama via query_cek_nama_barang_duplikat().
         12. Tampilkan ringkasan data dan konfirmasi [Y/N].
         13. Jika Y: panggil query_insert_barang(), catat audit trail, tampilkan sukses hijau.
         14. Jika N: batalkan dan kembali ke sub-menu.
      """
  ```

  **Validasi Input per Field:**
  - Nama Barang: Tidak boleh kosong, tidak boleh hanya spasi, maks 100 karakter.
  - Semua input numerik: Tangkap `decimal.InvalidOperation` dan tampilkan `ERR-VAL-009`.
  - Setiap prompt wajib menjalankan `sanitasi_input_cli()` terlebih dahulu.

- [ ] **5.3.5. Implementasi Sub-Fitur: Ubah Data Barang (F-03)**

  ```python
  def _ubah_data_barang(session_state: dict) -> None:
      """Formulir edit master data barang yang sudah ada.

      Alur:
          1. Prompt ID Barang yang akan diubah.
          2. Panggil query_detail_barang() untuk mengambil data saat ini.
          3. Jika tidak ditemukan: tampilkan "ERR-VAL-009: ID barang tidak ditemukan."
          4. Tampilkan data saat ini dalam panel rich.
          5. Untuk setiap field, tampilkan:
             "Nama Barang [Enter=tetap 'Kertas HVS A4']: "
             - Jika user tekan Enter: pertahankan nilai lama.
             - Jika user mengetik nilai baru: gunakan nilai baru.
          6. JANGAN izinkan mengubah tipe_barang (Read-Only setelah dibuat).
          7. Panggil validasi_data_barang() untuk data gabungan (lama + baru).
          8. Cek duplikasi nama via query_cek_nama_barang_duplikat() dengan exclude_id.
          9. Tampilkan perbandingan data lama vs baru (diff).
         10. Konfirmasi [Y/N].
         11. Jika Y: panggil query_update_barang(), catat audit trail (old_value & new_value).
         12. Tampilkan sukses hijau.
      """
  ```

- [ ] **5.3.6. Implementasi Sub-Fitur: Hapus Barang (F-04)**

  ```python
  def _hapus_barang(session_state: dict) -> None:
      """Penghapusan barang dari master data.

      Alur:
          1. Prompt ID Barang yang akan dihapus.
          2. Panggil query_detail_barang() untuk menampilkan data yang akan dihapus.
          3. Jika tidak ditemukan: tampilkan error.
          4. Tampilkan PERINGATAN MERAH:
             "⚠️ PERINGATAN: Penghapusan data master barang bersifat PERMANEN!"
          5. Konfirmasi ganda: "Ketik nama barang persis untuk konfirmasi hapus: "
             - Hanya hapus jika user mengetik nama barang yang persis sama.
          6. Jika konfirmasi valid: panggil query_delete_barang().
          7. Tangkap error FK RESTRICT (errno 1451):
             - Tampilkan: "ERR-FK-005: Barang tidak dapat dihapus karena masih
               digunakan sebagai bahan baku dalam formula BOM!"
          8. Jika berhasil: catat audit trail (DELETE) dan tampilkan sukses hijau.
      """
  ```

- [ ] **5.3.7. Implementasi Sub-Fitur: Lihat Detail Barang (F-05)**

  ```python
  def _lihat_detail_barang(session_state: dict) -> None:
      """Menampilkan detail lengkap satu barang beserta info BOM.

      Alur:
          1. Prompt ID Barang.
          2. Panggil query_detail_barang() dari db layer.
          3. Tampilkan panel rich dengan informasi lengkap:
             - Header: Nama Barang, Tipe, Satuan UoM
             - Stok: Stok Saat Ini (warna kuning jika <= 5, merah jika <= 0)
             - Harga: Beli, Retail, Grosir (Min), Mitra
             - Margin: Hitung margin retail menggunakan hitung_margin_barang()
             - Timestamp: Created At, Updated At
          4. Jika barang ini adalah barang induk BOM:
             - Tampilkan tabel komponen BOM terkait:
               | No | Bahan Baku | Satuan | Qty Pakai | H.Beli | Biaya Komponen |
             - Tampilkan Total HPP di baris terakhir.
          5. Tombol Enter untuk kembali.
      """
  ```

---

### 5.4. TAHAP 4 — Integrasi Audit Trail (`middleware/audit_logger.py`)

**Tujuan**: Memastikan setiap operasi CREATE, UPDATE, DELETE pada tabel `barang` dicatat ke `audit_logs`.

#### Checklist Implementasi:

- [ ] **5.4.1. Panggil `log_audit_trail` Setelah INSERT Barang Baru**

  ```python
  log_audit_trail(
      pengguna_id=session_state['user_id'],
      action_type='INSERT',
      target_table='barang',
      old_val=None,
      new_val={'id': lastrowid, 'nama_barang': '...', 'tipe_barang': '...', ...},
      cabang_id=session_state['cabang_id'],
      db_connection=conn
  )
  ```

- [ ] **5.4.2. Panggil `log_audit_trail` Setelah UPDATE Barang**

  ```python
  log_audit_trail(
      pengguna_id=session_state['user_id'],
      action_type='UPDATE',
      target_table='barang',
      old_val={'nama_barang': 'Lama', 'harga_retail': 45000, ...},
      new_val={'nama_barang': 'Baru', 'harga_retail': 48000, ...},
      cabang_id=session_state['cabang_id'],
      db_connection=conn
  )
  ```

- [ ] **5.4.3. Panggil `log_audit_trail` Setelah DELETE Barang**

  ```python
  log_audit_trail(
      pengguna_id=session_state['user_id'],
      action_type='DELETE',
      target_table='barang',
      old_val={'id': 102, 'nama_barang': '...', ...},
      new_val=None,
      cabang_id=session_state['cabang_id'],
      db_connection=conn
  )
  ```

---

### 5.5. TAHAP 5 — Integrasi RBAC Guard (`middleware/rbac_guard.py`)

**Tujuan**: Memastikan hanya peran yang berhak yang dapat mengakses fitur kelola barang.

#### Checklist Implementasi:

- [ ] **5.5.1. Terapkan Decorator RBAC pada Entry Point**

  Pada fungsi `form_kelola_barang`, terapkan pengecekan peran sebelum menampilkan sub-menu:

  ```python
  def form_kelola_barang(session_state: dict) -> None:
      # Cek otorisasi RBAC
      role = session_state.get('role', '')
      allowed_roles_full = ('pemilik', 'kepala_percetakan', 'gudang')
      allowed_roles_read = ('produksi_cetak',)

      if role not in allowed_roles_full and role not in allowed_roles_read:
          console.print("⛔ ERR-AUTH-003: Akses Ditolak!", style="bold red")
          # Catat ke audit_logs dengan action_type='ACCESS_DENIED'
          return

      # Jika role hanya READ, hanya tampilkan opsi [1] dan [5]
      is_read_only = role in allowed_roles_read
      # ... tampilkan sub-menu dengan filter sesuai hak akses
  ```

- [ ] **5.5.2. Blokir Operasi Tulis untuk Peran Read-Only**

  Jika `produksi_cetak` mencoba memilih opsi Tambah/Ubah/Hapus, tampilkan:
  ```
  ⛔ ERR-AUTH-003: Akses Ditolak: Peran Anda hanya diizinkan melihat data barang!
  ```

---

### 5.6. TAHAP 6 — Unit Testing (`tests/test_kelola_barang.py`)

**Tujuan**: Menulis unit test untuk seluruh pure functions pada logic layer.

#### Checklist Implementasi:

- [ ] **5.6.1. Buat File Test Baru: `tests/test_kelola_barang.py`**

  ```python
  """
  Nama Modul: test_kelola_barang.py
  Deskripsi: Unit testing deterministic terisolasi penuh (tanpa koneksi DB riil)
             untuk fungsi validasi data master barang pada logic/bom_hpp.py.
  """
  import unittest
  from decimal import Decimal
  from logic.bom_hpp import validasi_data_barang, hitung_margin_barang, buat_audit_payload_barang
  ```

- [ ] **5.6.2. Test Cases untuk `validasi_data_barang`:**
  - ✅ Data Retail ATK valid lengkap → `is_valid = True`
  - ✅ Data Bahan Baku valid → auto-set harga retail/grosir/mitra = 0
  - ❌ Nama barang kosong → `is_valid = False`, error msg
  - ❌ Nama barang > 100 karakter → `is_valid = False`
  - ❌ Tipe barang selain 'Retail_ATK'/'Bahan_Baku' → `is_valid = False`
  - ❌ Satuan UoM tidak valid → `is_valid = False`
  - ❌ Stok negatif → `is_valid = False`
  - ❌ Harga beli negatif → `is_valid = False`
  - ❌ Min grosir = 0 → `is_valid = False`
  - ❌ Input non-numerik pada field harga → `is_valid = False`

- [ ] **5.6.3. Test Cases untuk `hitung_margin_barang`:**
  - ✅ Margin normal: harga_jual=100, harga_beli=60 → margin=40.00%
  - ✅ Margin 0%: harga_jual=100, harga_beli=100 → margin=0.00%
  - ✅ Harga jual = 0: → margin=0.00% (mitigasi division by zero)
  - ✅ Margin negatif (rugi): harga_jual=50, harga_beli=80 → margin=-60.00%

- [ ] **5.6.4. Test Cases untuk `buat_audit_payload_barang`:**
  - ✅ INSERT action: old_data=None → old_value_json = 'null'
  - ✅ DELETE action: new_data=None → new_value_json = 'null'
  - ✅ UPDATE action: keduanya terisi JSON valid

---

## 6. Batasan dan Larangan Teknis

### 6.1. Larangan Mutlak (Hard Constraints)

| # | Larangan | Alasan |
|:---:|---|---|
| L-01 | **DILARANG** menggunakan `class` / OOP pada `logic/` dan `db/` | Coding Standard v1.1: Pure FP murni tanpa OOP pada alur bisnis |
| L-02 | **DILARANG** menggunakan tipe `float` untuk angka keuangan/stok | SRS v1.2: Wajib `decimal.Decimal` presisi DECIMAL(15,4) |
| L-03 | **DILARANG** menulis query SQL string mentah tanpa `%s` binding | Security Design: Parameterized query wajib untuk cegah SQL Injection |
| L-04 | **DILARANG** memanggil `print()`/`input()` di `logic/` atau `db/` | Module Structure: Efek samping I/O hanya di `cli/` (Layer 1) |
| L-05 | **DILARANG** mengimpor modul `cli/` dari `logic/` atau `db/` | Dependensi searah top-down: `cli → logic → db` |
| L-06 | **DILARANG** menghapus docstring dan komentar yang sudah ada | Coding Standard: Preserve existing documentation |
| L-07 | **DILARANG** menulis query tanpa filter `cabang_id` pada WHERE | Multi-Branch Ready (M.9): Setiap query wajib scope ke cabang |
| L-08 | **DILARANG** hardcode separator path (`/` atau `\`) | OS Constraints: Wajib gunakan `pathlib` untuk cross-platform |

### 6.2. Standar Kode Wajib (Mandatory Code Standards)

| # | Standar | Detail |
|:---:|---|---|
| S-01 | **Penamaan** | `snake_case` untuk fungsi dan variabel, `PascalCase` untuk NamedTuple |
| S-02 | **Type Hints** | Seluruh parameter fungsi dan return value wajib di-type hint (PEP 484) |
| S-03 | **Docstring** | Seluruh fungsi publik wajib memiliki docstring format Google Style |
| S-04 | **Result Pattern** | Seluruh fungsi DB wajib mengembalikan `Result(is_success, data, error_msg)` |
| S-05 | **Presisi Desimal** | `Decimal('0.0001')` dengan `ROUND_HALF_UP` untuk semua kalkulasi |
| S-06 | **Import Ordering** | 1. Standard Library, 2. Third-Party, 3. Local Modules |
| S-07 | **Error Codes** | Gunakan kode error standar dari SRS (ERR-VAL-xxx, ERR-DB-xxx, ERR-AUTH-xxx) |
| S-08 | **Koneksi DB** | Selalu ambil dari pool (`get_db_connection()`), selalu kembalikan (`conn.close()`) di `finally` |

---

## 7. Rencana Verifikasi

### 7.1. Automated Tests

```bash
# Jalankan unit test khusus kelola barang
python -m pytest tests/test_kelola_barang.py -v --tb=short

# Jalankan seluruh test suite untuk memastikan tidak ada regresi
python -m pytest tests/ -v --tb=short
```

### 7.2. Manual Verification Checklist

- [ ] Login sebagai `pemilik` → Buka M.2 → Kelola Barang → Semua 5 sub-fitur tersedia
- [ ] Login sebagai `gudang` → Buka M.2 → Kelola Barang → Semua 5 sub-fitur tersedia
- [ ] Login sebagai `produksi_cetak` → Buka M.2 → Kelola Barang → Hanya Lihat Daftar & Detail
- [ ] Login sebagai `kasir` → Buka M.2 → Kelola Barang → Ditolak (ERR-AUTH-003)
- [ ] Tambah barang Retail ATK → Verifikasi data di database → Verifikasi audit_logs
- [ ] Tambah barang Bahan Baku → Verifikasi harga retail/grosir/mitra = 0 otomatis
- [ ] Edit barang → Verifikasi data lama vs baru di audit_logs
- [ ] Hapus barang tanpa BOM → Berhasil
- [ ] Hapus barang yang dipakai di BOM → Ditolak (ERR-FK-005)
- [ ] Input harga dengan format salah (abc, -100) → Ditolak (ERR-VAL-009)
- [ ] Input nama barang duplikat di cabang yang sama → Ditolak

---

## 8. Daftar File yang Dimodifikasi

| # | File | Tipe Perubahan | Layer |
|:---:|---|---|---|
| 1 | `db/query_builder.py` | MODIFY — Tambah 6 fungsi query baru | Data Access (L3) |
| 2 | `logic/bom_hpp.py` | MODIFY — Tambah 3 fungsi validasi + 1 NamedTuple | Business Logic (L2) |
| 3 | `cli/menu_inventaris.py` | MODIFY — Implementasi `form_kelola_barang` + 5 sub-handler | Presentation (L1) |
| 4 | `tests/test_kelola_barang.py` | NEW — File unit test baru | Testing |

---

## 9. Catatan Industri & Rekomendasi Proaktif

### 9.1. Rekomendasi Standar Industri yang Belum Disebutkan dalam Dokumen SDLC

Berdasarkan analisis standar industri pengelolaan inventaris ritel modern, eksekutor **DISARANKAN** mempertimbangkan dan menambahkan fitur-fitur berikut (jika belum ada di issue lain):

| # | Rekomendasi | Justifikasi Industri | Prioritas |
|:---:|---|---|:---:|
| REC-01 | **Barcode/SKU Field** | Standar industri ritel menggunakan kode SKU (Stock Keeping Unit) unik per barang untuk identifikasi cepat di scanner. Pertimbangkan menambahkan kolom `sku_kode VARCHAR(50) UNIQUE` di tabel `barang` pada issue DDL terpisah. | Medium |
| REC-02 | **Kategori Barang** | Mengelompokkan barang ke dalam kategori (ATK, Kertas, Tinta, Aksesoris Stempel) memudahkan filtering dan laporan. Pertimbangkan tabel `kategori_barang` terpisah. | Low |
| REC-03 | **Minimum Stock Alert Level** | Kolom `stok_minimum DECIMAL(15,4)` per barang agar threshold re-order bisa dikonfigurasi per-item (bukan hardcode 5.0000 di query). | Medium |
| REC-04 | **Soft Delete (is_active)** | Menghapus barang secara lunak (`is_active BOOLEAN DEFAULT TRUE`) mencegah kehilangan riwayat transaksi historis. Barang non-aktif disembunyikan dari form transaksi kasir tetapi tetap tampil di laporan historis. | Medium |

> **PENTING**: Rekomendasi di atas adalah saran tambahan. Eksekutor **TIDAK WAJIB** mengimplementasikannya di issue ini jika memerlukan perubahan skema DDL. Dokumentasikan sebagai catatan untuk issue masa depan.

---

## 10. Kriteria Penerimaan (Acceptance Criteria)

Issue ini dinyatakan **SELESAI** jika dan hanya jika:

- [x] Seluruh 5 sub-fitur CRUD (F-01 s.d F-05) berfungsi pada terminal CLI
- [x] Validasi input desimal presisi 4 digit bekerja konsisten
- [x] RBAC membatasi akses sesuai ACM v1.2 (4 peran diizinkan, 4 ditolak)
- [x] Setiap operasi CREATE/UPDATE/DELETE dicatat ke `audit_logs`
- [x] Seluruh query menyertakan filter `cabang_id`
- [x] Tidak ada penggunaan `float`, `class`, atau query tanpa parameterized binding
- [x] Unit test `tests/test_kelola_barang.py` pass 100% dengan coverage ≥ 90%
- [x] Tidak ada regresi pada test suite yang sudah ada (`tests/`)
- [x] Kode mematuhi 100% Coding Standard v1.1 (snake_case, type hints, docstring)

---

*Dokumen Issue ini disusun oleh **Principal Full-Stack Python Engineer & Inventory Domain Specialist** dan siap dieksekusi oleh AI model pengembang atau junior programmer.*
