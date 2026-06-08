---
issue_id     : "#0138"
judul        : Feature — Catat Riwayat Harga Beli Supplier (Price Tracking)
status       : Open
prioritas    : Medium
modul        : M.2 — Manajemen Inventaris, BOM & Stock Opname
tanggal      : 2026-06-08
penyusun     : Senior Technical Planner & Low-Level Specification Architect
---

# Issue #0138 — Feature: Catat Riwayat Harga Beli Supplier (Price Tracking)

---

## 1. Persona Pelaksana (AI Executor Identity)

**Kamu adalah `Senior Python Backend Engineer & Database Integration Specialist`.**

Kamu bertugas mengimplementasikan fitur pencatatan riwayat harga beli supplier secara end-to-end pada sistem AbuCom CLI Python. Kamu memiliki keahlian mendalam dalam:
- Pemrograman Python 3.14+ dengan paradigma **Functional Programming (FP)** murni.
- Desain query SQL terparameterisasi (`%s` bindings) untuk MySQL 8.x InnoDB.
- Arsitektur 4-layer modular (Presentation → Logic → Data Access → Database).
- Implementasi RBAC, Audit Trail JSON, dan presisi desimal `DECIMAL(15,4)`.

**Perilaku Wajib:**
1. Kamu **DILARANG KERAS** menghapus, mengubah, atau menghapus komentar/docstring yang sudah ada di kode yang tidak terkait dengan pekerjaanmu.
2. Kamu **DILARANG KERAS** memodifikasi tabel database atau kolom yang tidak disebutkan secara eksplisit dalam issue ini.
3. Kamu **WAJIB** mengikuti coding standard proyek AbuCom yang terdokumentasi di `docs/sdlc/04_implementation/01_coding_standard.md`.
4. Kamu **WAJIB** menggunakan `NamedTuple` dari `collections` untuk setiap struktur data imutabel.
5. Kamu **WAJIB** menggunakan modul `decimal.Decimal` dengan pembulatan `ROUND_HALF_UP` untuk seluruh operasi numerik harga.
6. Jika kamu menemukan fitur, logika alur kerja, atau metode keamanan yang belum disebutkan di sini namun secara signifikan dapat meningkatkan kualitas implementasi — kamu **WAJIB** mengusulkannya sebagai komentar `# TODO-INNOVATION:` di dalam kode, bukan mengimplementasikannya langsung.

---

## 2. Dokumen Referensi yang Wajib Dibaca

Sebelum memulai implementasi, kamu **WAJIB** membaca dan mengekstrak detail yang relevan dari seluruh dokumen referensi berikut. **JANGAN** mengarang data atau logika yang tidak ada di dokumen-dokumen ini.

| # | Nama Dokumen | Path Relatif | Bagian yang Wajib Dibaca |
|---|---|---|---|
| R-01 | Software Requirements Specification (SRS) v1.2 | `docs/sdlc/02_analysis/02_software_requirements.md` | **SRS-F-013** (Fitur Riwayat Harga Beli Supplier) — baris ~548-576 |
| R-02 | Business Requirements Document (BRD) v1.2 | `docs/sdlc/02_analysis/01_business_requirements.md` | **BR-F-13** (Fitur Riwayat Harga Beli Supplier Price Tracking) — baris ~364-370 |
| R-03 | Use Case Diagram v1.2 | `docs/sdlc/02_analysis/03_use_case_diagram.md` | **UC-013** (Melacak Riwayat Harga Beli Supplier) |
| R-04 | Workflow Diagram v1.2 | `docs/sdlc/02_analysis/04_workflow_diagram.md` | **WF-M2-07** (Alur Riwayat Harga Beli Supplier) — baris ~681-703 |
| R-05 | Data Dictionary v1.2 | `docs/sdlc/02_analysis/05_data_dictionary.md` | **Tabel 3.26: `riwayat_harga_supplier`** — baris ~1000-1027, dan **Relasi FK #54-56** — baris ~1319-1321 |
| R-06 | Database Schema DDL SQL v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | **[TABEL 28] `riwayat_harga_supplier`** — baris ~704-721, **[TABEL 04] `supplier`** — baris ~98-112, **[TABEL 05] `barang`** — baris ~170-194 |
| R-07 | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | **§6.7 Alur: Melacak Riwayat Harga Supplier (UC-013)** — baris ~893-915 |
| R-08 | Access Control Matrix (ACM) v1.2 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | **M2-007** (Price Tracking Supplier) — baris ~262, **CRUD Tabel #26 `riwayat_harga_supplier`** — baris ~381 |
| R-09 | Module Structure v1.2 | `docs/sdlc/04_implementation/03_module_structure.md` | **§4.4 `cli/menu_inventaris.py`** — baris ~339-358, **§5.2 `logic/bom_hpp.py`** — baris ~416-445, **§15 SRS-to-File Traceability** |
| R-10 | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` | Seluruh dokumen — konvensi penamaan, FP restrictions, Result pattern, layout direktori |

---

## 3. Rangkuman Konteks Teknis dari Dokumen Referensi

Bagian ini merangkum detail data yang diekstrak dari dokumen referensi di atas **hanya** yang relevan dan spesifik untuk fitur ini. Gunakan rangkuman ini sebagai sumber kebenaran utama saat implementasi.

### 3.1. Definisi Kebutuhan Bisnis (BR-F-13)

- **Apa**: Sistem harus merekam riwayat fluktuasi harga beli barang baku atau retail dari setiap supplier fisik setiap kali staf gudang menginput transaksi pengadaan barang masuk.
- **Aktor Terkait**: `gudang`.
- **Aturan Bisnis**: Data disimpan di tabel riwayat harga untuk menyajikan komparasi harga supplier termurah untuk produk sejenis secara real-time.
- **Kriteria Penerimaan Bisnis**: Staf gudang dapat mengakses data barang, melihat daftar harga beli historis dari 3 supplier berbeda, dan memilih supplier paling murah secara cepat.
- **Prioritas**: Medium.

### 3.2. Spesifikasi Teknis (SRS-F-013)

- **Deskripsi Teknis**: Sistem **HARUS** merekam secara kronologis riwayat fluktuasi harga beli barang atau bahan baku dari setiap supplier setiap kali staf gudang menginput data pengadaan barang masuk.
- **Input yang Diperlukan**:
  - `barang_id` (INT) — referensi ke `barang.id`.
  - `supplier_id` (INT) — referensi ke `supplier.id`.
  - `harga_beli_baru` (DECIMAL(15,4)) — harga beli per unit dari supplier.
- **Proses/Logika Bisnis**:
  1. Setiap kali transaksi pembelian inventaris dicatat, simpan entri baru ke tabel `riwayat_harga_supplier`.
  2. Catat `barang_id`, `supplier_id`, `harga_beli_baru`, dan `tanggal_pembelian`.
  3. Sediakan antarmuka pencarian bagi staf gudang untuk melihat komparasi harga historis supplier untuk satu produk sejenis.
- **Output yang Dihasilkan**:
  - Baris baru di tabel `riwayat_harga_supplier`.
  - Tabel daftar harga perbandingan supplier di terminal CLI.
- **Aturan Validasi**: Nilai `harga_beli_baru` **HARUS** berupa angka positif > 0.
- **Penanganan Error**: Jika `supplier_id` tidak valid atau tidak terdaftar, tolak pencatatan, tampilkan: `"ERR-VAL-013: ID supplier tidak terdaftar di database master!"`.
- **Ketergantungan**: `SRS-F-037` (Modul Supplier).
- **Catatan Implementasi**: Pengambilan riwayat diurutkan berdasarkan `tanggal_pembelian DESC`.

### 3.3. Alur Kerja (WF-M2-07)

Alur prosedural sesuai workflow diagram:
1. Staf Gudang menginput transaksi pengadaan barang masuk baru dari supplier ke dalam CLI.
2. Sistem secara otomatis menyimpan harga beli satuan, kuantitas masuk, tanggal transaksi, dan ID Supplier ke dalam tabel `riwayat_harga_supplier`.
3. Saat gudang ingin merencanakan belanja barang di masa depan, staf membuka menu Price Tracking.
4. Sistem mengevaluasi seluruh transaksi pengadaan historis dan menampilkan urutan supplier dari yang menawarkan harga termurah hingga termahal.

### 3.4. Skema Database — Tabel `riwayat_harga_supplier` (Tabel 28)

```sql
CREATE TABLE riwayat_harga_supplier (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    barang_id INT NOT NULL,          -- FK → barang.id
    supplier_id INT NOT NULL,        -- FK → supplier.id
    harga_beli DECIMAL(15,4) NOT NULL,
    tanggal_pembelian DATE NOT NULL,
    cabang_id INT NOT NULL DEFAULT 1, -- FK → cabang.id
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_riwayat_harga_supplier_harga_beli CHECK (harga_beli > 0),
    CONSTRAINT fk_riwayat_harga_supplier_barang_id FOREIGN KEY (barang_id) REFERENCES barang(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_riwayat_harga_supplier_supplier_id FOREIGN KEY (supplier_id) REFERENCES supplier(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_riwayat_harga_supplier_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Kolom Detail:**

| # | Kolom | Tipe | Constraint | Null? | Default | Deskripsi |
|---|---|---|---|:---:|---|---|
| 1 | `id` | INT | PK, AI, NN | NOT NULL | — | ID unik baris riwayat |
| 2 | `barang_id` | INT | FK→`barang.id`, NN | NOT NULL | — | Referensi item barang/bahan baku |
| 3 | `supplier_id` | INT | FK→`supplier.id`, NN | NOT NULL | — | Referensi vendor supplier |
| 4 | `harga_beli` | DECIMAL(15,4) | NN, CHECK > 0 | NOT NULL | 0.0000 | Harga beli per unit (Rupiah) |
| 5 | `tanggal_pembelian` | DATE | NN | NOT NULL | (CURRENT_DATE) | Tanggal transaksi pengadaan |
| 6 | `cabang_id` | INT | FK→`cabang.id`, NN | NOT NULL | 1 | Cabang pencatat |
| 7 | `created_at` | TIMESTAMP | NN | NOT NULL | CURRENT_TIMESTAMP | Waktu pembuatan baris |
| 8 | `updated_at` | TIMESTAMP | NN | NOT NULL | CURRENT_TIMESTAMP ON UPDATE | Waktu update terakhir |

**Relasi Foreign Key:**
- `barang_id` → `barang.id` (Many-to-One, ON DELETE RESTRICT, ON UPDATE CASCADE)
- `supplier_id` → `supplier.id` (Many-to-One, ON DELETE RESTRICT, ON UPDATE CASCADE)
- `cabang_id` → `cabang.id` (Many-to-One, ON DELETE RESTRICT, ON UPDATE CASCADE)

### 3.5. Tabel Terkait yang Dibutuhkan (Read-Only Reference)

**Tabel `supplier` (Tabel 04):**
| Kolom | Tipe | Deskripsi |
|---|---|---|
| `id` | INT, PK, AI | ID unik supplier |
| `nama_supplier` | VARCHAR(100), NN | Nama badan usaha/perorangan vendor |
| `alamat` | TEXT, NN | Alamat kantor/gudang supplier |
| `telp` | VARCHAR(30), NN | Nomor telepon aktif |
| `email` | VARCHAR(100), NN | Email supplier |
| `cabang_id` | INT, FK, NN, DEFAULT 1 | Cabang pencatat |

**Tabel `barang` (Tabel 05) — Kolom Relevan:**
| Kolom | Tipe | Deskripsi |
|---|---|---|
| `id` | INT, PK, AI | ID unik item barang |
| `nama_barang` | VARCHAR(100), NN | Nama komersial barang |
| `tipe_barang` | VARCHAR(20), NN | `'Retail_ATK'` atau `'Bahan_Baku'` |
| `satuan_uom` | VARCHAR(20), NN | Satuan dasar stok |
| `harga_beli` | DECIMAL(15,4), NN, DEFAULT 0.0000 | Harga pengadaan dari supplier |
| `cabang_id` | INT, FK, NN, DEFAULT 1 | Cabang pemilik stok |

### 3.6. Hak Akses RBAC (ACM)

**Menu CLI (MENU-M2-007 — Price Tracking Supplier):**

| Peran | Hak Akses |
|---|---|
| `pemilik` | ✅ FULL (CRUD) |
| `kepala_percetakan` | 📖 READ |
| `gudang` | 📖 READ |
| `pramuniaga` | ⛔ DENY |
| `kasir` | ⛔ DENY |
| `desainer` | ⛔ DENY |
| `produksi_cetak` | ⛔ DENY |
| `fotocopy_print` | ⛔ DENY |

**CRUD Tabel `riwayat_harga_supplier`:**

| Peran | C | R | U | D |
|---|:---:|:---:|:---:|:---:|
| `pemilik` | ✅ | ✅ | ✅ | ✅ |
| `gudang` | ✅ | ✅ | — | — |
| Peran lain | — | — | — | — |

> **PENTING**: Pencatatan riwayat harga (INSERT) dilakukan secara **otomatis oleh sistem** saat staf gudang menginput pengadaan barang masuk (UC-015 / `form_kelola_supplier`). Fitur Price Tracking (UC-013 / MENU-M2-007) adalah fitur **baca-saja** (READ) untuk melihat komparasi harga historis.

### 3.7. Alur CLI Interaction Flow (UC-013)

**Derivasi**: UC-013, SRS-F-013, WF-M2-09, Menu ID: MENU-M2-007.

| No. | Aktor/Sistem | Aksi | Tipe | Contoh Tampilan/Input |
|---|---|---|---|---|
| 1 | Pengguna | Memilih menu "Price Tracking Supplier" di terminal. | Input | `Pilihan menu: 7` |
| 2 | Sistem | Meminta menginput ID Barang/Bahan Baku yang akan dilacak. | Output | `Masukkan ID Barang / Bahan Baku: ` |
| 3 | Pengguna | Mengetikkan ID barang. | Input | `102` (integer) |
| 4 | Sistem | Query ke tabel `riwayat_harga_supplier` untuk menarik kronologi harga beli historis. | Proses | `SELECT r.tanggal_pembelian, s.nama_supplier, r.harga_beli FROM riwayat_harga_supplier r JOIN supplier s ON r.supplier_id = s.id WHERE r.barang_id = %s ORDER BY r.tanggal_pembelian DESC` |
| 5 | Sistem | Menyajikan tabel tren harga beli dari berbagai supplier terurut dari tanggal paling baru. | Output | Tabel visual komparasi fluktuasi harga beli supplier |
| 6 | Sistem | Menandai baris harga termurah dengan indikator warna biru. | Output | `[BLUE] Rekomendasi Supplier Termurah: Supplier Indah (Rp 40.000 / Rim)` |

---

## 4. Batasan dan Cakupan Pekerjaan

### 4.1. Yang TERMASUK dalam Cakupan Issue Ini

- [ ] Implementasi fungsi **INSERT** riwayat harga ke tabel `riwayat_harga_supplier` saat pengadaan barang masuk.
- [ ] Implementasi fungsi **SELECT/READ** komparasi harga historis per barang dari seluruh supplier.
- [ ] Implementasi **menu CLI Price Tracking** (MENU-M2-007) di `cli/menu_inventaris.py`.
- [ ] Implementasi **logika bisnis** pencatatan dan komparasi harga di `logic/bom_hpp.py`.
- [ ] Implementasi **query database** terparameterisasi di `db/query_builder.py`.
- [ ] Implementasi **RBAC guard** untuk menu MENU-M2-007.
- [ ] Implementasi **Audit Trail** untuk setiap INSERT riwayat harga.
- [ ] Implementasi **penanganan data kosong** (saat belum ada riwayat harga untuk suatu barang).
- [ ] Implementasi **validasi input** (harga > 0, barang_id valid, supplier_id valid).
- [ ] Implementasi **update `harga_beli`** pada tabel `barang` saat harga baru dicatat.

### 4.2. Yang TIDAK TERMASUK dalam Cakupan Issue Ini

- ❌ Pembuatan tabel `riwayat_harga_supplier` di MySQL — **tabel sudah ada di DDL schema**.
- ❌ Registrasi supplier baru — sudah di-handle oleh UC-015 (`form_kelola_supplier`).
- ❌ Pencatatan utang usaha supplier — sudah di-handle oleh UC-015.
- ❌ Perubahan struktur tabel `supplier`, `barang`, atau `cabang`.
- ❌ Implementasi fitur import CSV (SRS-F-014).
- ❌ Implementasi fitur stock opname (SRS-F-011).
- ❌ Modifikasi menu dashboard atau modul selain M.2.

---

## 5. Checklist Implementasi Low-Level

### FASE A: Persiapan (Layer 3 — Data Access)

#### A.1. Tambah Query Functions di `db/query_builder.py`

- [ ] **A.1.1.** Buat fungsi `insert_riwayat_harga_supplier(db_connection, data: dict) -> Result`:
  ```python
  # Parameter 'data' berisi:
  #   barang_id: int
  #   supplier_id: int
  #   harga_beli: Decimal
  #   tanggal_pembelian: str (format 'YYYY-MM-DD')
  #   cabang_id: int
  #
  # SQL:
  # INSERT INTO riwayat_harga_supplier
  #   (barang_id, supplier_id, harga_beli, tanggal_pembelian, cabang_id)
  # VALUES (%s, %s, %s, %s, %s)
  #
  # Return: Result(is_success=True, data={'last_insert_id': cursor.lastrowid}, error_msg=None)
  # Atau: Result(is_success=False, data=None, error_msg='ERR-DB-...: ...')
  ```

- [ ] **A.1.2.** Buat fungsi `get_riwayat_harga_by_barang(db_connection, barang_id: int, cabang_id: int) -> Result`:
  ```python
  # SQL:
  # SELECT
  #   r.id,
  #   r.tanggal_pembelian,
  #   s.nama_supplier,
  #   r.harga_beli,
  #   r.supplier_id
  # FROM riwayat_harga_supplier r
  # JOIN supplier s ON r.supplier_id = s.id
  # WHERE r.barang_id = %s AND r.cabang_id = %s
  # ORDER BY r.tanggal_pembelian DESC
  #
  # Return: Result(is_success=True, data=[list of tuples], error_msg=None)
  # Jika tidak ada data: Result(is_success=True, data=[], error_msg=None)
  ```

- [ ] **A.1.3.** Buat fungsi `get_supplier_termurah_by_barang(db_connection, barang_id: int, cabang_id: int) -> Result`:
  ```python
  # SQL:
  # SELECT
  #   s.id AS supplier_id,
  #   s.nama_supplier,
  #   r.harga_beli,
  #   r.tanggal_pembelian
  # FROM riwayat_harga_supplier r
  # JOIN supplier s ON r.supplier_id = s.id
  # WHERE r.barang_id = %s
  #   AND r.cabang_id = %s
  #   AND r.tanggal_pembelian = (
  #       SELECT MAX(r2.tanggal_pembelian)
  #       FROM riwayat_harga_supplier r2
  #       WHERE r2.barang_id = r.barang_id
  #         AND r2.supplier_id = r.supplier_id
  #         AND r2.cabang_id = r.cabang_id
  #   )
  # ORDER BY r.harga_beli ASC
  # LIMIT 1
  #
  # Return: Result(is_success=True, data=tuple or None, error_msg=None)
  ```

- [ ] **A.1.4.** Buat fungsi `update_harga_beli_barang(db_connection, barang_id: int, harga_beli_baru: Decimal) -> Result`:
  ```python
  # SQL:
  # UPDATE barang SET harga_beli = %s WHERE id = %s
  #
  # Catatan: Fungsi ini digunakan untuk mengupdate harga_beli standar
  # pada tabel barang saat transaksi pengadaan baru dicatat.
  # HANYA dipanggil di dalam transaksi ACID bersama insert_riwayat_harga_supplier.
  ```

- [ ] **A.1.5.** Buat fungsi `check_barang_exists(db_connection, barang_id: int, cabang_id: int) -> bool`:
  ```python
  # SQL: SELECT COUNT(1) FROM barang WHERE id = %s AND cabang_id = %s
  # Return: True jika count > 0, False jika tidak.
  ```

- [ ] **A.1.6.** Buat fungsi `check_supplier_exists(db_connection, supplier_id: int, cabang_id: int) -> bool`:
  ```python
  # SQL: SELECT COUNT(1) FROM supplier WHERE id = %s AND cabang_id = %s
  # Return: True jika count > 0, False jika tidak.
  ```

---

### FASE B: Logika Bisnis (Layer 2 — Business Logic)

#### B.1. Tambah Fungsi Logika di `logic/bom_hpp.py`

- [ ] **B.1.1.** Tambahkan NamedTuple baru di bagian atas file (setelah import yang sudah ada):
  ```python
  RiwayatHargaEntry = namedtuple('RiwayatHargaEntry', [
      'id', 'tanggal_pembelian', 'nama_supplier', 'harga_beli', 'supplier_id'
  ])
  ```

- [ ] **B.1.2.** Buat fungsi `validasi_input_harga_beli(harga_beli: Decimal) -> Result`:
  ```python
  # Logika:
  # 1. Cek apakah harga_beli adalah instance Decimal. Jika bukan, konversi.
  # 2. Cek apakah harga_beli > Decimal('0'). Jika tidak, return error:
  #    Result(is_success=False, data=None, error_msg='ERR-VAL-013: Harga beli harus berupa angka positif > 0!')
  # 3. Cek apakah harga_beli <= Decimal('999999999999999.9999') (batas DECIMAL(15,4)).
  # 4. Jika valid: Result(is_success=True, data=harga_beli.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP), error_msg=None)
  ```

- [ ] **B.1.3.** Buat fungsi `proses_catat_riwayat_harga(barang_id: int, supplier_id: int, harga_beli: Decimal, tanggal_pembelian: str, cabang_id: int, db_connection) -> Result`:
  ```python
  # Logika Bisnis:
  # 1. Panggil check_barang_exists(). Jika False → error 'ERR-VAL-013: ID barang tidak terdaftar!'
  # 2. Panggil check_supplier_exists(). Jika False → error 'ERR-VAL-013: ID supplier tidak terdaftar di database master!'
  # 3. Panggil validasi_input_harga_beli(). Jika gagal → return error dari validasi.
  # 4. Validasi format tanggal_pembelian (YYYY-MM-DD). Jika gagal → error.
  # 5. Jalankan dalam ACID transaction block:
  #    a. insert_riwayat_harga_supplier() — simpan riwayat harga.
  #    b. update_harga_beli_barang() — update harga_beli standar di tabel barang.
  #    c. log_audit_trail() — catat perubahan ke audit_logs.
  # 6. Return Result sukses dengan last_insert_id.
  ```

- [ ] **B.1.4.** Buat fungsi `ambil_komparasi_harga_supplier(barang_id: int, cabang_id: int, db_connection) -> Result`:
  ```python
  # Logika Bisnis:
  # 1. Panggil check_barang_exists(). Jika False → error.
  # 2. Panggil get_riwayat_harga_by_barang() dari query_builder.
  # 3. Jika data kosong (list = []):
  #    Return Result(is_success=True, data=[], error_msg=None)
  #    → Biarkan layer presentasi menangani tampilan "Belum ada riwayat harga".
  # 4. Konversi setiap tuple ke NamedTuple RiwayatHargaEntry.
  # 5. Return Result(is_success=True, data=[list of RiwayatHargaEntry], error_msg=None)
  ```

- [ ] **B.1.5.** Buat fungsi `cari_supplier_termurah(barang_id: int, cabang_id: int, db_connection) -> Result`:
  ```python
  # Logika Bisnis:
  # 1. Panggil get_supplier_termurah_by_barang() dari query_builder.
  # 2. Jika data = None: Return Result dengan data=None (belum ada data).
  # 3. Konversi ke NamedTuple dan return.
  ```

---

### FASE C: Antarmuka CLI (Layer 1 — Presentation)

#### C.1. Tambah Menu di `cli/menu_inventaris.py`

- [ ] **C.1.1.** Di dalam fungsi `show_menu_inventaris(session_state: dict)`, tambahkan opsi menu baru:
  ```
  Opsi: [7-Price Tracking Supplier]
  ```
  > **PENTING**: Pastikan nomor opsi menu sesuai dengan penomoran yang sudah ada di file ini. Cek opsi menu yang sudah ada (1-6, 8-11) dan masukkan angka 7 sesuai dengan MENU-M2-007.

- [ ] **C.1.2.** Tambahkan routing di handler navigasi menu untuk mengarahkan pilihan `7` ke fungsi `view_price_tracking_supplier(session_state)`.

- [ ] **C.1.3.** Buat fungsi `view_price_tracking_supplier(session_state: dict) -> None`:
  ```python
  # Alur Interaksi:
  #
  # 1. RBAC Guard: Panggil middleware.rbac_guard.check_menu_permission('MENU-M2-007', session_state['role']).
  #    - Jika DENY → tampilkan pesan error warna merah dan return.
  #    - Jika READ atau FULL → lanjutkan.
  #
  # 2. Tampilkan breadcrumb header:
  #    print("Dashboard > M.2 Inventaris > Price Tracking Supplier")
  #
  # 3. Minta input ID Barang/Bahan Baku:
  #    - Prompt: "Masukkan ID Barang / Bahan Baku: "
  #    - Sanitasi input menggunakan logic.safety_validator.sanitasi_input_cli()
  #    - Konversi ke int. Jika gagal → tampilkan error format dan kembali ke prompt.
  #
  # 4. Panggil logic.bom_hpp.ambil_komparasi_harga_supplier(barang_id, cabang_id, db_conn)
  #
  # 5. Jika Result.is_success == False:
  #    - Tampilkan error message berwarna merah dari Result.error_msg
  #
  # 6. Jika Result.data == [] (kosong / belum ada riwayat):
  #    - Tampilkan: "[YELLOW] ⚠️ Belum ada riwayat harga pembelian untuk barang ini."
  #    - Tampilkan saran: "Riwayat harga akan tercatat otomatis saat Anda menginput pengadaan barang masuk."
  #    - Return ke menu.
  #
  # 7. Jika Result.data berisi data:
  #    a. Format tabel menggunakan library `tabulate` dengan header:
  #       ['No', 'Tanggal Beli', 'Supplier', 'Harga Beli (Rp)', 'Supplier ID']
  #    b. Render tabel berwarna di terminal CLI menggunakan `rich`.
  #
  # 8. Panggil logic.bom_hpp.cari_supplier_termurah(barang_id, cabang_id, db_conn)
  #    a. Jika ditemukan supplier termurah:
  #       Tampilkan rekomendasi berwarna biru:
  #       "[BLUE] Rekomendasi Supplier Termurah: {nama_supplier} (Rp {harga_beli} / {satuan})"
  #    b. Jika tidak ditemukan: skip, tidak perlu tampilkan rekomendasi.
  ```

#### C.2. Integrasi dengan Alur Pengadaan Barang Masuk (UC-015)

- [ ] **C.2.1.** Di dalam fungsi `form_kelola_supplier(session_state: dict)` yang sudah ada (atau yang menangani pencatatan pembelian stok tempo), **tambahkan pemanggilan** fungsi `proses_catat_riwayat_harga()` **setelah** transaksi pengadaan barang masuk berhasil di-commit:
  ```python
  # SETELAH pengadaan barang masuk berhasil dicatat di tabel utang_supplier / stok:
  #
  # 1. Ambil harga_beli per unit dari input staf gudang (sudah ada di flow UC-015).
  # 2. Ambil barang_id dan supplier_id dari konteks transaksi.
  # 3. Panggil: proses_catat_riwayat_harga(barang_id, supplier_id, harga_beli, tanggal, cabang_id, db_conn)
  # 4. Jika berhasil: tampilkan notifikasi sekunder hijau:
  #    "[GREEN] ✓ Riwayat harga beli supplier berhasil dicatat otomatis."
  # 5. Jika gagal: tampilkan warning kuning (non-blocking, jangan hentikan flow utama):
  #    "[YELLOW] ⚠️ Gagal mencatat riwayat harga supplier. Error: {error_msg}"
  ```

  > **KRITIS**: Kegagalan pencatatan riwayat harga **TIDAK BOLEH** menggagalkan transaksi pengadaan utama. Ini adalah fitur sekunder. Gunakan blok try/except terpisah di luar ACID transaction utama pengadaan, atau lakukan INSERT riwayat harga sebagai operasi terpisah setelah COMMIT utama berhasil.

---

### FASE D: Keamanan & Audit (Cross-cutting Concerns)

#### D.1. RBAC Guard

- [ ] **D.1.1.** Di `middleware/rbac_guard.py`, pastikan entri berikut terdaftar di matriks ACM internal kode:
  ```python
  # Menu ID: 'MENU-M2-007'
  # Permissions:
  #   'pemilik': 'FULL',
  #   'kepala_percetakan': 'READ',
  #   'gudang': 'READ',
  #   (semua role lain): 'DENY'
  ```
  > **CATATAN**: Jika matriks sudah menggunakan pola data-driven (dictionary/config), tambahkan entri baru. Jika belum ada file `rbac_guard.py`, buatlah sesuai spesifikasi di Module Structure §7.3.

#### D.2. Audit Trail

- [ ] **D.2.1.** Setiap kali INSERT ke `riwayat_harga_supplier` berhasil, panggil `middleware.audit_logger.log_audit_trail()` dengan parameter:
  ```python
  log_audit_trail(
      pengguna_id=session_state['user_id'],
      action_type='INSERT_RIWAYAT_HARGA',
      target_table='riwayat_harga_supplier',
      old_val=None,  # INSERT, jadi tidak ada old value.
      new_val={
          'barang_id': barang_id,
          'supplier_id': supplier_id,
          'harga_beli': str(harga_beli),
          'tanggal_pembelian': tanggal_pembelian
      },
      cabang_id=session_state['cabang_id'],
      db_connection=db_conn
  )
  ```

- [ ] **D.2.2.** Setiap kali UPDATE ke `barang.harga_beli` terjadi (karena harga baru dari supplier), panggil `log_audit_trail()` dengan:
  ```python
  log_audit_trail(
      pengguna_id=session_state['user_id'],
      action_type='UPDATE_HARGA_BELI_BARANG',
      target_table='barang',
      old_val={'harga_beli': str(harga_beli_lama)},
      new_val={'harga_beli': str(harga_beli_baru)},
      cabang_id=session_state['cabang_id'],
      db_connection=db_conn
  )
  ```

---

### FASE E: Penanganan Data Kosong & Edge Cases

- [ ] **E.1.** Jika tabel `riwayat_harga_supplier` belum memiliki data sama sekali untuk `barang_id` tertentu:
  - Jangan tampilkan tabel kosong atau error.
  - Tampilkan pesan informatif kuning: `"[YELLOW] ⚠️ Belum ada riwayat harga pembelian untuk barang ID {barang_id}. Riwayat harga akan tercatat otomatis saat pengadaan barang masuk berikutnya."`
  - Jangan tampilkan rekomendasi supplier termurah.

- [ ] **E.2.** Jika `barang_id` yang diinput pengguna tidak ada di tabel `barang`:
  - Tampilkan: `"⛔ ERR-VAL-013: ID barang '{barang_id}' tidak terdaftar di database master!"`
  - Kembali ke prompt input.

- [ ] **E.3.** Jika `supplier_id` yang diinput tidak ada di tabel `supplier`:
  - Tampilkan: `"⛔ ERR-VAL-013: ID supplier tidak terdaftar di database master!"`
  - Batalkan pencatatan riwayat harga.

- [ ] **E.4.** Jika `harga_beli` yang diinput bernilai ≤ 0 atau bukan angka:
  - Tampilkan: `"⛔ ERR-VAL-013: Harga beli harus berupa angka positif > 0!"`
  - Kembali ke prompt input harga.

- [ ] **E.5.** Jika `tanggal_pembelian` berformat selain `YYYY-MM-DD`:
  - Tampilkan: `"⛔ ERR-VAL-013: Format tanggal tidak valid! Gunakan format: YYYY-MM-DD."`
  - Kembali ke prompt input tanggal.

- [ ] **E.6.** Jika koneksi database terputus saat proses INSERT:
  - Jalankan rollback otomatis via wrapper ACID.
  - Tampilkan: `"⛔ ERR-DB-TX: Transaksi dibatalkan aman. Detail: {error_detail}"`

---

## 6. Aturan Pencegahan Kerusakan Fitur Lain

> **SANGAT KRITIS**: Fitur riwayat harga supplier adalah fitur **sekunder** yang **TIDAK BOLEH** merusak, mengganggu, atau mengubah perilaku fitur-fitur yang sudah ada.

### 6.1. Daftar File yang Boleh Dimodifikasi

| # | File | Tipe Modifikasi | Catatan |
|---|---|---|---|
| 1 | `db/query_builder.py` | **TAMBAH** fungsi baru | Tambahkan 6 fungsi query baru di bagian bawah file. JANGAN mengubah fungsi yang sudah ada. |
| 2 | `logic/bom_hpp.py` | **TAMBAH** fungsi baru & NamedTuple | Tambahkan di bagian bawah file. JANGAN mengubah fungsi HPP, BOM, limbah yang sudah ada. |
| 3 | `cli/menu_inventaris.py` | **TAMBAH** opsi menu & fungsi baru | Tambahkan opsi 7 dan fungsi `view_price_tracking_supplier()`. JANGAN mengubah fungsi menu 1-6 dan 8-11. |
| 4 | `middleware/rbac_guard.py` | **TAMBAH** entri ACM baru | Tambahkan `MENU-M2-007` ke dictionary matriks. JANGAN mengubah entri ACM yang sudah ada. |

### 6.2. Daftar File yang DILARANG Dimodifikasi

| # | File | Alasan Larangan |
|---|---|---|
| 1 | `cli/menu_transaksi.py` | Bukan domain modul M.2. |
| 2 | `cli/menu_ppob_service.py` | Bukan domain modul M.2. |
| 3 | `cli/menu_sdm_finansial.py` | Bukan domain modul M.2. |
| 4 | `cli/menu_configs.py` | Bukan domain modul M.2. |
| 5 | `cli/dashboard.py` | Tidak ada perubahan dashboard yang diminta. |
| 6 | `logic/smart_payroll.py` | Bukan domain fitur price tracking. |
| 7 | `logic/financial_engine.py` | Bukan domain fitur price tracking. |
| 8 | `middleware/auth_jwt.py` | Tidak ada perubahan autentikasi. |
| 9 | `config/settings.py` | Tidak ada konfigurasi baru yang dibutuhkan. |
| 10 | `docs/sdlc/03_design/01_database_schema.sql` | Tabel sudah ada. JANGAN mengubah skema DDL. |

### 6.3. Aturan ACID Transaction Terpisah

```
┌─────────────────────────────────────────────────────────────────────┐
│  TRANSACTION UTAMA (UC-015: Pengadaan Barang Masuk)                │
│                                                                     │
│  1. UPDATE barang SET stok_saat_ini = stok_saat_ini + qty           │
│  2. INSERT INTO utang_supplier (nominal, jatuh_tempo, ...)          │
│  3. COMMIT ← Ini adalah COMMIT wajib utama.                        │
│                                                                     │
│  Jika GAGAL → ROLLBACK → Tampilkan error → STOP.                   │
└─────────────────────────────────────────────────────────────────────┘
                              │
                     (HANYA jika COMMIT utama SUKSES)
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│  TRANSACTION SEKUNDER (Issue #0138: Riwayat Harga Supplier)        │
│                                                                     │
│  1. INSERT INTO riwayat_harga_supplier (harga_beli, ...)            │
│  2. UPDATE barang SET harga_beli = harga_beli_baru                  │
│  3. INSERT INTO audit_logs (action_type='INSERT_RIWAYAT_HARGA')     │
│  4. COMMIT                                                          │
│                                                                     │
│  Jika GAGAL → ROLLBACK → Tampilkan WARNING kuning → LANJUTKAN.     │
│  (JANGAN hentikan atau batalkan flow utama pengadaan)               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 7. Kriteria Penerimaan (Definition of Done)

### 7.1. Fungsionalitas

- [ ] Staf gudang dapat menginput pengadaan barang masuk, dan riwayat harga **otomatis tercatat** di tabel `riwayat_harga_supplier`.
- [ ] Staf gudang dapat membuka menu Price Tracking (opsi 7 di menu inventaris), menginput ID barang, dan melihat tabel kronologi harga beli dari berbagai supplier.
- [ ] Tabel komparasi harga menampilkan: Tanggal Beli, Nama Supplier, Harga Beli (Rp), terurut dari tanggal terbaru.
- [ ] Sistem menampilkan **rekomendasi supplier termurah** dengan warna biru di bawah tabel.
- [ ] Kolom `harga_beli` pada tabel `barang` **terupdate otomatis** dengan harga beli terbaru dari pengadaan.

### 7.2. Validasi & Error Handling

- [ ] Input `harga_beli` ≤ 0 ditolak dengan pesan error `ERR-VAL-013`.
- [ ] Input `supplier_id` yang tidak terdaftar ditolak dengan pesan error `ERR-VAL-013`.
- [ ] Input `barang_id` yang tidak terdaftar ditolak dengan pesan error `ERR-VAL-013`.
- [ ] Format `tanggal_pembelian` selain `YYYY-MM-DD` ditolak dengan pesan error.
- [ ] Kegagalan database dihandle dengan rollback ACID otomatis.

### 7.3. Keamanan & Audit

- [ ] Menu MENU-M2-007 hanya dapat diakses oleh role: `pemilik` (FULL), `kepala_percetakan` (READ), `gudang` (READ).
- [ ] Seluruh role lain mendapat `ACCESS_DENIED` saat mencoba mengakses menu ini.
- [ ] Setiap INSERT ke `riwayat_harga_supplier` **tercatat** di `audit_logs`.
- [ ] Setiap UPDATE ke `barang.harga_beli` **tercatat** di `audit_logs`.

### 7.4. Edge Cases & Data Kosong

- [ ] Jika belum ada riwayat harga untuk suatu barang, sistem menampilkan pesan informatif kuning — **bukan error**.
- [ ] Jika hanya ada 1 supplier untuk suatu barang, rekomendasi tetap menampilkan supplier tersebut sebagai "termurah".
- [ ] Kegagalan INSERT riwayat harga **TIDAK** menggagalkan transaksi pengadaan utama.

### 7.5. Kualitas Kode

- [ ] Seluruh fungsi baru memiliki docstring Python yang jelas.
- [ ] Seluruh fungsi baru di layer `logic/` bersifat **pure function** (tidak ada `print()` atau `input()`).
- [ ] Seluruh variabel harga menggunakan `decimal.Decimal` — **BUKAN float**.
- [ ] Seluruh query SQL menggunakan parameterisasi `%s` — **BUKAN string concatenation**.
- [ ] Penamaan variabel dan fungsi mengikuti konvensi `snake_case`.
- [ ] Penamaan NamedTuple mengikuti konvensi `PascalCase`.
- [ ] Tidak ada fungsi atau kode yang sudah ada di proyek yang rusak/berubah perilaku akibat penambahan fitur ini.

---

## 8. Catatan Tambahan

### 8.1. Diagram Dependensi File untuk Fitur Ini

```
cli/menu_inventaris.py
  ├── view_price_tracking_supplier()   ← BARU
  │     ├── logic/bom_hpp.py
  │     │     ├── ambil_komparasi_harga_supplier() ← BARU
  │     │     ├── cari_supplier_termurah()          ← BARU
  │     │     └── validasi_input_harga_beli()       ← BARU
  │     ├── db/query_builder.py
  │     │     ├── get_riwayat_harga_by_barang()     ← BARU
  │     │     ├── get_supplier_termurah_by_barang() ← BARU
  │     │     ├── check_barang_exists()             ← BARU
  │     │     └── check_supplier_exists()           ← BARU
  │     ├── middleware/rbac_guard.py
  │     │     └── check_menu_permission('MENU-M2-007') ← TAMBAH ENTRI
  │     └── utils/text_formatter.py (existing)
  │
  └── form_kelola_supplier() ← MODIFIKASI (tambah panggilan)
        └── logic/bom_hpp.py
              └── proses_catat_riwayat_harga()     ← BARU
                    ├── db/query_builder.py
                    │     ├── insert_riwayat_harga_supplier() ← BARU
                    │     └── update_harga_beli_barang()       ← BARU
                    └── middleware/audit_logger.py
                          └── log_audit_trail() (existing)
```

### 8.2. Urutan Pengerjaan yang Direkomendasikan

1. **FASE A** (Data Access) → Kerjakan pertama, karena layer di atasnya bergantung pada query ini.
2. **FASE D** (RBAC Guard entry) → Kerjakan kedua, agar testing menu bisa langsung dilakukan.
3. **FASE B** (Business Logic) → Kerjakan ketiga, karena logika bergantung pada query di FASE A.
4. **FASE C** (CLI Presentation) → Kerjakan keempat, karena ini menghubungkan semua layer.
5. **FASE E** (Edge Cases) → Kerjakan terakhir, sebagai validasi dan polish.

### 8.3. Testing Manual yang Disarankan

Setelah implementasi selesai, lakukan pengujian manual berikut:

1. **Test INSERT otomatis**: Login sebagai `gudang` → Catat pengadaan barang masuk dari supplier → Verifikasi bahwa `riwayat_harga_supplier` memiliki baris baru.
2. **Test READ komparasi**: Login sebagai `gudang` → Buka menu 7 (Price Tracking) → Input ID barang yang sudah ada riwayatnya → Verifikasi tabel tampil terurut.
3. **Test data kosong**: Input ID barang yang belum pernah ada pengadaan → Verifikasi pesan kuning informatif muncul.
4. **Test RBAC DENY**: Login sebagai `kasir` → Coba akses menu 7 → Verifikasi error `ACCESS_DENIED`.
5. **Test validasi harga**: Coba input harga ≤ 0 → Verifikasi error `ERR-VAL-013`.
6. **Test supplier invalid**: Coba gunakan supplier_id yang tidak ada → Verifikasi error `ERR-VAL-013`.
7. **Test non-blocking failure**: Simulasikan error pada INSERT riwayat harga (misal, force disconnect) → Verifikasi bahwa transaksi pengadaan utama tetap berhasil.
8. **Test audit trail**: Setelah pengadaan berhasil → Cek tabel `audit_logs` → Verifikasi ada entri `INSERT_RIWAYAT_HARGA` dan `UPDATE_HARGA_BELI_BARANG`.
