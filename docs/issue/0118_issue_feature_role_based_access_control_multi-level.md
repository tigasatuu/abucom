---
issue_id    : 0118
judul       : Feature — Role Based Access Control (RBAC) Multi-Level
prioritas   : High
status      : Open (Belum Dikerjakan)
estimasi    : 8–12 jam kerja
target_file : middleware/rbac_guard.py, cli/dashboard.py, middleware/audit_logger.py
tanggal     : 2026-06-07
---

# Issue #0118 — Feature Role Based Access Control (RBAC) Multi-Level

---

## 0. Persona Pelaksana (AI / Programmer)

**Peran yang WAJIB diadopsi oleh pelaksana issue ini:**

> Kamu adalah **Senior Security Architect & RBAC Implementation Specialist** yang berpengalaman dalam merancang dan mengimplementasikan sistem otorisasi berbasis peran (Role-Based Access Control) untuk aplikasi CLI Python. Kamu memiliki pemahaman mendalam tentang prinsip keamanan **Least Privilege**, **Default Deny**, **Separation of Duties**, dan **Fail-Secure**. Kamu bekerja dengan paradigma **Functional Programming (FP) murni** tanpa class, menggunakan `NamedTuple` / `namedtuple` untuk data imutabel, `Result Pattern` untuk error handling, dan parameterized queries `%s` untuk akses database. Kamu sangat teliti, tidak tergesa-gesa, dan mengutamakan kelengkapan serta kualitas pengerjaan agar tidak ada celah keamanan yang terlewat.

---

## 1. Daftar Dokumen Referensi (WAJIB Dibaca Sebelum Memulai)

Sebelum menulis satu baris kode pun, pelaksana **WAJIB** membaca, mengekstrak, dan merangkum seluruh detail data yang relevan dari dokumen-dokumen berikut. Jangan lewatkan detail kecil dari informasi yang relevan.

| # | Nama Dokumen Referensi | Path Relatif | Alasan Relevansi |
|---|---|---|---|
| **R-01** | Access Control Matrix (ACM) v1.2 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | **SSoT UTAMA** — Sumber kebenaran tunggal definisi 8 peran internal, matriks hak akses 44 Use Case (10 modul + 4 base), matriks CRUD 28 tabel, aturan eskalasi supervisor, default deny, inheritance policy, rate limiting, audit trail pelanggaran. |
| **R-02** | Security Design v1.2 | `docs/sdlc/03_design/06_security_design.md` | Desain arsitektur RBAC multi-level 3-tier, implementasi decorator/guard otorisasi, pseudocode FP Python untuk `require_permission()`, `write_audit_log()`, model ancaman, aturan eskalasi, kode error keamanan. |
| **R-03** | Module Structure v1.2 | `docs/sdlc/04_implementation/03_module_structure.md` | Spesifikasi file `middleware/rbac_guard.py` (Bab 7.3), spesifikasi `middleware/audit_logger.py` (Bab 7.4), diagram dependensi impor, aturan penempatan file, dan function signatures. |
| **R-04** | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` | Standar decorator RBAC (Bab 10.4), aturan FP murni, Result Pattern, type hints, penamaan snake_case, header modul, docstring PEP 257, Error Code Catalog, dan standar keamanan kode. |
| **R-05** | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Daftar Menu ID (MENU-BASE-xxx, MENU-Mx-xxx), alur navigasi menu per peran, dan konvensi visual error ANSI. |
| **R-06** | Database Schema (DDL) v1.2 | `schema.sql` (root) atau `docs/sdlc/03_design/01_database_schema.sql` | Skema fisik tabel `pengguna` (kolom `role`, `failed_login_attempts`, `locked_until`), tabel `audit_logs` (struktur kolom), dan tabel `system_configs`. |
| **R-07** | Narasi Pemilik | `docs/sdlc/narasi.txt` | Konteks bisnis: kebutuhan privasi data (pinjaman bank, tabungan pribadi hanya untuk Pemilik), struktur 7 posisi karyawan, dan mandat keamanan Audit Trail. |

> **⚠️ PENTING:** Jika ada data yang dibutuhkan tetapi TIDAK ditemukan di file referensi di atas, tandai dengan komentar `# DATA_KOSONG: [deskripsi data yang dibutuhkan] — Perlu ditindaklanjuti` di dalam kode atau di catatan akhir issue ini.

---

## 2. Rangkuman Data Relevan dari Dokumen Referensi

Berikut adalah rangkuman detail data dari dokumen referensi yang **spesifik** mendukung pengerjaan RBAC. Pelaksana WAJIB memverifikasi ulang data ini terhadap file aslinya sebelum digunakan.

### 2.1. Definisi 8 Peran Internal (Sumber: ACM Bab 2.1)

| ID Aktor | Nama Peran | Kode Peran di DB (`role`) | Level Hierarki |
|---|---|---|---|
| ACT-01 | Pemilik Usaha | `pemilik` | Level 1 (Super Admin) |
| ACT-02 | Kepala Percetakan | `kepala_percetakan` | Level 2 (Supervisor) |
| ACT-03 | Staf Pramuniaga | `pramuniaga` | Level 3 (Staf Operasional) |
| ACT-04 | Staf Kasir | `kasir` | Level 3 (Staf Operasional) |
| ACT-05 | Staf Desainer | `desainer` | Level 3 (Staf Operasional) |
| ACT-06 | Staf Produksi Cetak | `produksi_cetak` | Level 3 (Staf Operasional) |
| ACT-07 | Staf Fotocopy & Print | `fotocopy_print` | Level 3 (Staf Operasional) |
| ACT-08 | Staf Gudang | `gudang` | Level 3 (Staf Operasional) |

### 2.2. Matriks Akses Lengkap 44 Menu CLI (Sumber: ACM Bab 4.2 – 4.12)

Pelaksana WAJIB mendefinisikan dictionary `RBAC_MATRIX` yang memetakan SETIAP peran ke SETIAP menu ID yang diizinkan, beserta **level akses** (`FULL`, `READ`, `INPUT`, `INPUT_READ`, `RTL`, `ESC`).

**Modul M.1 — Transaksi & Kebijakan Harga:**

| Menu ID | Fungsi | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MENU-M1-001` | Catat Transaksi | FULL | READ | INPUT | FULL | DENY | DENY | RTL | DENY |
| `MENU-M1-002` | Ubah Skema Harga | FULL | READ | READ | READ | DENY | DENY | DENY | DENY |
| `MENU-M1-003` | Kelola DP & Pelunasan | FULL | DENY | DENY | FULL | DENY | DENY | DENY | DENY |
| `MENU-M1-004` | Pembatalan & Retur | FULL | DENY | DENY | ESC | DENY | DENY | DENY | DENY |
| `MENU-M1-005` | Margin per Produk | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |
| `MENU-M1-006` | Ekspor Struk Thermal | FULL | DENY | DENY | FULL | DENY | DENY | DENY | DENY |

**Modul M.2 — Inventaris, BOM & Stock Opname:**

| Menu ID | Fungsi | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MENU-M2-001` | Kelola Barang & UoM | FULL | FULL | DENY | DENY | DENY | READ | DENY | FULL |
| `MENU-M2-002` | Hitung HPP BOM Desimal | FULL | READ | DENY | DENY | DENY | INPUT | DENY | DENY |
| `MENU-M2-003` | Mencatat Limbah | FULL | READ | DENY | DENY | DENY | INPUT | DENY | DENY |
| `MENU-M2-004` | Sinkronisasi ATK Internal | FULL | FULL | DENY | DENY | DENY | INPUT | DENY | INPUT |
| `MENU-M2-005` | Rekonsiliasi Stok | FULL | ESC | DENY | DENY | DENY | DENY | DENY | INPUT |
| `MENU-M2-006` | Prediksi Re-Order Stok | FULL | READ | DENY | DENY | DENY | DENY | DENY | READ |
| `MENU-M2-007` | Price Tracking Supplier | FULL | READ | DENY | DENY | DENY | DENY | DENY | READ |
| `MENU-M2-008` | Impor Data CSV | FULL | DENY | DENY | DENY | DENY | DENY | DENY | INPUT |
| `MENU-M2-009` | Kelola Supplier & Utang | FULL | FULL | DENY | DENY | DENY | DENY | DENY | FULL |
| `MENU-M2-010` | Backup & Restore DB | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |

**Modul M.3 — Layanan Keuangan, PPOB & Jasa Service:**

| Menu ID | Fungsi | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MENU-M3-001` | Kelola Saldo PPOB | FULL | DENY | DENY | INPUT_READ | DENY | DENY | DENY | DENY |
| `MENU-M3-002` | Akun Keuangan Terhemat | FULL | DENY | DENY | READ | DENY | DENY | DENY | DENY |
| `MENU-M3-003` | Transaksi Jasa Service | FULL | DENY | INPUT | FULL | DENY | DENY | DENY | DENY |

**Modul M.4 — SDM, Penggajian & Poin Karyawan:**

| Menu ID | Fungsi | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MENU-M4-001` | Kelola Absensi & Kasbon | FULL | FULL | INPUT | INPUT | INPUT | INPUT | INPUT | INPUT |
| `MENU-M4-002` | Memproses Gaji | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |
| `MENU-M4-003` | Poin Insentif Karyawan | FULL | DENY | DENY | READ | DENY | DENY | DENY | DENY |
| `MENU-M4-004` | Potongan Gaji Kasbon | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |

**Modul M.5 — Antrian & Pelacakan Desain:**

| Menu ID | Fungsi | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MENU-M5-001` | Pelacakan Status Antrian | FULL | FULL | INPUT | INPUT | INPUT | INPUT | DENY | DENY |
| `MENU-M5-002` | Mengelola Arsip Desain | FULL | DENY | READ | DENY | FULL | DENY | DENY | DENY |
| `MENU-M5-003` | Link WhatsApp Web | FULL | DENY | INPUT | INPUT | DENY | DENY | DENY | DENY |

**Modul M.6 — Pinjaman, Aset & Pengeluaran:**

| Menu ID | Fungsi | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MENU-M6-001` | Pinjaman Modal | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |
| `MENU-M6-002` | Laba/Rugi per Divisi | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |
| `MENU-M6-003` | Alert Jatuh Tempo Utang | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |
| `MENU-M6-004` | Depresiasi & Tabungan Aset | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |
| `MENU-M6-005` | Pengeluaran Rutin & Tak Terduga | FULL | INPUT | DENY | INPUT | DENY | DENY | DENY | DENY |

**Modul M.7 — Keamanan, Audit Trail & Hak Akses:**

| Menu ID | Fungsi | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MENU-M7-001` | Akses RBAC CLI | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |
| `MENU-M7-002` | Audit Log Trail JSON | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |
| `MENU-M7-003` | Serah Terima Shift | FULL | ESC | DENY | INPUT | DENY | DENY | DENY | DENY |
| `MENU-M7-004` | Rekonsiliasi Kas | FULL | READ | DENY | INPUT | DENY | DENY | DENY | DENY |
| `MENU-M7-005` | Fraud Detection | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |
| `MENU-M7-006` | Setup Awal Wizard | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |

**Modul M.8 — CRM Pelanggan:**

| Menu ID | Fungsi | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MENU-M8-001` | Database CRM | FULL | DENY | FULL | FULL | DENY | DENY | DENY | DENY |

**Modul M.9 — Skalabilitas Multi-Cabang:**

| Menu ID | Fungsi | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MENU-M9-001` | Multi-Cabang | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |

**Modul M.10 — Konfigurasi Sistem Runtime:**

| Menu ID | Fungsi | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MENU-M10-001` | Parameter Runtime | FULL | DENY | DENY | DENY | DENY | DENY | DENY | DENY |

**Use Case Dasar (Akses Seluruh Peran):**

| Menu ID | Fungsi | Semua 8 Peran |
|---|---|:---:|
| `MENU-BASE-001` | Melakukan Login | FULL |
| `MENU-BASE-002` | Melakukan Logout | FULL |
| `MENU-BASE-003` | Dashboard Utama | FULL |
| `MENU-BASE-004` | Mengubah Password | FULL |

### 2.3. Aturan Eskalasi Otorisasi (Sumber: ACM Bab 6.1 & 6.2)

**Eskalasi Pemilik (memerlukan input sandi pemilik secara fisik):**

| No | Operasi Kritis | Peran Pemohon | Peran Penyetuju | Error Jika Gagal |
|---|---|---|---|---|
| 1 | Pembatalan Transaksi (Retur DP) | `kasir` | `pemilik` | `ERR-AUTH-003` |
| 2 | Retur Barang Retail ATK | `kasir` | `pemilik` | `ERR-AUTH-003` |
| 3 | Pengeluaran Besar (> Rp 500.000) | `kasir` / `kepala_percetakan` | `pemilik` | `ERR-AUTH-029` |
| 4 | Restorasi Database Manual | `gudang` | `pemilik` | `ERR-FILE-039` |

**Eskalasi Kepala Percetakan:**

| No | Operasi Verifikasi | Peran Pemohon | Peran Penyetuju | Error Jika Gagal |
|---|---|---|---|---|
| 1 | Persetujuan Stock Opname (DRAFT → APPROVED) | `gudang` | `kepala_percetakan` | `ERR-AUTH-011` |
| 2 | Serah Terima Shift (Normal) | `kasir` | `kepala_percetakan` | `ERR-AUTH-011` |
| 3 | Serah Terima Shift (Anomali selisih > Rp 10.000) | `kasir` | `kepala_percetakan` + memo | `ERR-CASH-001` |

### 2.4. Kebijakan RBAC Kritis (Sumber: ACM Bab 6.7, 6.8, 6.9)

- **Default Deny Policy**: Segala akses DITOLAK secara baku. Hanya yang terdaftar eksplisit di RBAC_MATRIX yang diizinkan.
- **No Inheritance**: Peran Level 2 (`kepala_percetakan`) TIDAK mewarisi hak akses Level 3. Setiap peran memiliki domain akses terisolasi.
- **Review Berkala**: ACM di-review setiap 6 bulan atau setiap rilis mayor.

### 2.5. Audit Trail pada Pelanggaran Akses (Sumber: ACM Bab 6.6 & Security Design Bab 7.2)

Setiap kali RBAC menolak akses, sistem WAJIB menulis log ke `audit_logs`:
- `pengguna_id` = ID Staf pelanggar
- `action_type` = `'ACCESS_DENIED'`
- `target_table` = Nama modul / menu target
- `old_value` = JSON: `{"attempted_menu": "MENU-Mx-xxx", "role": "nama_role"}`
- `new_value` = `'ILLEGAL_ACCESS_PREVENTED'`

---

## 3. Batasan, Cakupan & Alur Pengerjaan

### 3.1. Cakupan Issue Ini (IN SCOPE)

- [x] Melengkapi matriks RBAC di `middleware/rbac_guard.py` agar mencakup **SELURUH 44 Menu ID** + **4 Use Case Dasar** sesuai ACM v1.2 Bab 4.
- [x] Memperkaya dictionary RBAC agar menyimpan **level akses** (`FULL`, `READ`, `INPUT`, `INPUT_READ`, `RTL`, `ESC`, `DENY`) — bukan hanya daftar menu yang diperbolehkan.
- [x] Memperbaiki fungsi `check_menu_permission()` agar mengembalikan **level akses** (bukan hanya boolean).
- [x] Memperbaiki decorator `require_role()` agar:
  - Mencatat audit trail `ACCESS_DENIED` ke database via `audit_logger.py`.
  - Mengembalikan `Result` pattern, bukan hanya `None`.
  - Menampilkan kode error yang benar (`ERR-AUTH-003`).
- [x] Menambahkan fungsi `verify_supervisor_escalation()` untuk mekanisme eskalasi sandi Pemilik dan Kepala Percetakan.
- [x] Menambahkan fungsi helper `get_visible_menus()` agar dashboard dapat memfilter menu yang ditampilkan sesuai peran.
- [x] Memperbarui `cli/dashboard.py` agar menampilkan menu berdasarkan hak akses peran aktif (bukan menampilkan semua menu).
- [x] Menulis unit test dasar di `tests/test_rbac_security.py`.

### 3.2. Yang TIDAK Dicakup Issue Ini (OUT OF SCOPE)

- ❌ Implementasi logika bisnis di dalam masing-masing menu (M.1 – M.10).
- ❌ Perubahan skema database / DDL SQL.
- ❌ Implementasi login/logout (sudah dikerjakan di issue sebelumnya).
- ❌ Implementasi backup/restore, payroll, dan fitur lain di luar RBAC guard.

### 3.3. File yang Akan Dimodifikasi

| No | File | Aksi | Keterangan |
|---|---|---|---|
| 1 | `middleware/rbac_guard.py` | **MODIFY** (Utama) | Melengkapi RBAC_MATRIX, memperbaiki `check_menu_permission()`, `require_role()`, menambah `verify_supervisor_escalation()` & `get_visible_menus()`. |
| 2 | `middleware/audit_logger.py` | **VERIFY** | Pastikan fungsi `log_audit_trail()` sudah benar dan bisa dipanggil dari `rbac_guard.py`. Jika belum lengkap, perbaiki. |
| 3 | `cli/dashboard.py` | **MODIFY** | Integrasikan `get_visible_menus()` untuk menampilkan menu terfilter sesuai peran aktif. |
| 4 | `tests/test_rbac_security.py` | **NEW / MODIFY** | Tulis test cases untuk validasi matriks RBAC dan penolakan akses. |

### 3.4. File yang TIDAK BOLEH Disentuh

- `middleware/auth_jwt.py` — Sudah final dan berfungsi.
- `schema.sql` — Tidak ada perubahan DDL.
- `config/settings.py` — Tidak relevan.
- `logic/*.py` — Di luar cakupan RBAC.
- `main.py` — Tidak relevan untuk issue ini.
- `db/db_connector.py` — Tidak relevan.
- `db/query_builder.py` — Tidak relevan.

---

## 4. Instruksi Pengerjaan Detail (Low-Level Checklist)

> **⚠️ PERHATIAN:** Kerjakan dengan **rapi, bersih, tidak tergesa-gesa, dan tidak buru-buru**. Pastikan setiap langkah selesai dengan benar sebelum melanjutkan ke langkah berikutnya. Kualitas kelengkapan pengerjaan harus maksimal agar tidak selalu dipertanyakan atau diinterupsi karena ada yang kurang.

---

### TAHAP 1: Pembacaan & Validasi Referensi

- [ ] **1.1** Baca file `docs/sdlc/02_analysis/06_access_control_matrix.md` (R-01) secara menyeluruh. Ekstrak dan catat:
  - [ ] Seluruh 8 definisi peran internal dari Bab 2.1
  - [ ] Seluruh matriks akses menu CLI dari Bab 4.2 s.d 4.12 (44 menu + 4 base)
  - [ ] Aturan eskalasi Pemilik dari Bab 6.1 (4 operasi kritis)
  - [ ] Aturan otorisasi Kepala Percetakan dari Bab 6.2 (3 operasi verifikasi)
  - [ ] Aturan Default Deny Policy dari Bab 6.7
  - [ ] Aturan No Inheritance Policy dari Bab 6.8
  - [ ] Format audit trail pelanggaran akses dari Bab 6.6
- [ ] **1.2** Baca file `docs/sdlc/03_design/06_security_design.md` (R-02). Ekstrak dan catat:
  - [ ] Pseudocode FP Python untuk `require_permission()` dari Bab 12.2
  - [ ] Pseudocode `write_audit_log()` dari Bab 12.2
  - [ ] Diagram alur otorisasi dari Bab 9.1 s.d 9.6
  - [ ] Kode error keamanan dari Bab 10.1 s.d 10.5
  - [ ] Fungsi `verify_supervisor()` dari Bab 9.3 (eskalasi retur)
- [ ] **1.3** Baca file `docs/sdlc/04_implementation/01_coding_standard.md` (R-04). Catat:
  - [ ] Standar decorator RBAC dari Bab 10.4
  - [ ] Template Result Pattern dari Bab 2.2.6
  - [ ] Header modul template dari Bab 6.4
  - [ ] Aturan type hints dari Bab 7
  - [ ] Error Code Catalog dari Bab 11.5
- [ ] **1.4** Baca file `docs/sdlc/04_implementation/03_module_structure.md` (R-03). Catat:
  - [ ] Spesifikasi `middleware/rbac_guard.py` dari Bab 7.3
  - [ ] Spesifikasi `middleware/audit_logger.py` dari Bab 7.4
  - [ ] Function signatures yang diharapkan
- [ ] **1.5** Baca file kode sumber yang sudah ada:
  - [ ] `middleware/rbac_guard.py` — Analisis kode saat ini, identifikasi kekurangan
  - [ ] `middleware/auth_jwt.py` — Pahami cara kerja `validate_session_token()`
  - [ ] `middleware/audit_logger.py` — Pahami `log_audit_trail()`
  - [ ] `cli/dashboard.py` — Pahami cara render dashboard saat ini
  - [ ] `schema.sql` — Perhatikan tabel `pengguna` (kolom `role`) dan `audit_logs`

---

### TAHAP 2: Implementasi `middleware/rbac_guard.py`

#### 2A — Definisi Konstanta & Data RBAC

- [ ] **2A.1** Perbarui header modul sesuai template Coding Standard Bab 6.4:
  ```python
  """
  Nama Modul: rbac_guard.py
  Deskripsi: Interceptor otorisasi akses menu CLI berbasis matriks peran RBAC Multi-Level.
             Mendefinisikan matriks akses 8 peran x 44 Menu + 4 Base Use Case.
             (Ref: ACM v1.2 Bab 4, Security Design v1.2 Bab 5, Module Structure v1.2 Bab 7.3)
  Author: [Nama Pelaksana]
  Tanggal: [YYYY-MM-DD]
  """
  ```

- [ ] **2A.2** Definisikan konstanta level akses menggunakan string konstan `UPPER_SNAKE_CASE`:
  ```python
  ACCESS_FULL = 'FULL'
  ACCESS_READ = 'READ'
  ACCESS_INPUT = 'INPUT'
  ACCESS_INPUT_READ = 'INPUT_READ'
  ACCESS_RTL = 'RTL'
  ACCESS_ESC = 'ESC'
  ACCESS_DENY = 'DENY'
  ```

- [ ] **2A.3** Definisikan tuple peran valid (sinkron dengan `auth_jwt.py`):
  ```python
  VALID_ROLES = (
      'pemilik', 'kepala_percetakan', 'pramuniaga', 'kasir',
      'desainer', 'produksi_cetak', 'fotocopy_print', 'gudang',
  )
  ```

- [ ] **2A.4** Bangun dictionary `RBAC_MATRIX` yang LENGKAP. Struktur yang digunakan:
  ```python
  # Kunci utama: menu_id (str)
  # Nilai: dict peran → level akses
  # Jika peran tidak ada di dict inner → Default Deny
  RBAC_MATRIX = {
      # === USE CASE DASAR ===
      'MENU-BASE-001': {role: ACCESS_FULL for role in VALID_ROLES},
      'MENU-BASE-002': {role: ACCESS_FULL for role in VALID_ROLES},
      'MENU-BASE-003': {role: ACCESS_FULL for role in VALID_ROLES},
      'MENU-BASE-004': {role: ACCESS_FULL for role in VALID_ROLES},
      # === MODUL M.1 — Transaksi & Kebijakan Harga ===
      'MENU-M1-001': {
          'pemilik': ACCESS_FULL,
          'kepala_percetakan': ACCESS_READ,
          'pramuniaga': ACCESS_INPUT,
          'kasir': ACCESS_FULL,
          'fotocopy_print': ACCESS_RTL,
      },
      # ... (lanjutkan untuk SELURUH 44 menu sesuai tabel Bab 2.2 issue ini)
  }
  ```
  - [ ] Validasi: pastikan SETIAP Menu ID dari `MENU-M1-001` s.d `MENU-M10-001` ada di dictionary.
  - [ ] Validasi: pastikan total ada **48 kunci** (44 menu + 4 base) di `RBAC_MATRIX`.
  - [ ] Pastikan peran yang tidak disebutkan di matriks TIDAK dimasukkan (Default Deny otomatis karena key tidak ada).

- [ ] **2A.5** Definisikan dictionary operasi kritis yang memerlukan eskalasi:
  ```python
  # Sumber: ACM Bab 6.1
  ESCALATION_PEMILIK = {
      'MENU-M1-004': {'trigger': 'Pembatalan/Retur', 'error_code': 'ERR-AUTH-003'},
      'MENU-M6-005': {'trigger': 'Pengeluaran > Rp 500.000', 'error_code': 'ERR-AUTH-029'},
      'MENU-M2-010': {'trigger': 'Restorasi Database', 'error_code': 'ERR-FILE-039'},
  }

  # Sumber: ACM Bab 6.2
  ESCALATION_KEPALA = {
      'MENU-M2-005': {'trigger': 'Persetujuan Stock Opname', 'error_code': 'ERR-AUTH-011'},
      'MENU-M7-003': {'trigger': 'Serah Terima Shift', 'error_code': 'ERR-AUTH-011'},
  }
  ```

#### 2B — Implementasi Fungsi-Fungsi RBAC

- [ ] **2B.1** Implementasikan fungsi `check_menu_permission()` yang mengembalikan level akses:
  ```python
  def check_menu_permission(menu_id: str, active_role: str) -> str:
      """Memeriksa level akses suatu peran terhadap Menu ID tertentu.

      Menerapkan Default Deny Policy (ACM Bab 6.7): jika peran tidak terdaftar
      pada matriks menu, akses ditolak secara otomatis.

      Args:
          menu_id (str): Kode identifikasi menu CLI (contoh: MENU-M1-001).
          active_role (str): Peran aktif dari sesi pengguna.

      Returns:
          str: Level akses (ACCESS_FULL, ACCESS_READ, dll.) atau ACCESS_DENY.
      """
      menu_permissions = RBAC_MATRIX.get(menu_id, {})
      return menu_permissions.get(active_role, ACCESS_DENY)
  ```

- [ ] **2B.2** Implementasikan decorator `require_role()` sesuai standar Coding Standard Bab 10.4 & Security Design Bab 5.2:
  ```python
  def require_role(menu_id: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
      """Decorator fungsional pembungkus fungsi menu CLI untuk proteksi akses.

      Alur pemeriksaan:
      1. Validasi keabsahan token JWT via validate_session_token().
      2. Cek otorisasi peran terhadap RBAC_MATRIX (Default Deny).
      3. Jika ditolak: catat audit trail ACCESS_DENIED, tampilkan ERR-AUTH-003.
      4. Jika diterima: eksekusi fungsi target.

      (Ref: Security Design v1.2 Bab 5.2, ACM v1.2 Bab 6.6 & 6.7)

      Args:
          menu_id (str): Kode identifikasi menu CLI yang diproteksi.

      Returns:
          Callable: Decorator fungsi pembungkus otorisasi.
      """
      def decorator(func):
          @wraps(func)
          def wrapper(session_state, *args, **kwargs):
              # 1. Validasi token sesi JWT
              val_res = validate_session_token(session_state)
              if not val_res.is_success:
                  print(f"⛔ {val_res.error_msg}")
                  return Result(False, None, val_res.error_msg)

              # 2. Cek otorisasi menu berdasarkan peran
              active_role = session_state.get('role', 'guest')
              access_level = check_menu_permission(menu_id, active_role)

              if access_level == ACCESS_DENY:
                  # 3. Catat audit trail pelanggaran keamanan
                  _log_access_denied(session_state, menu_id, active_role)
                  error_msg = "ERR-AUTH-003: Akses Ditolak: Hak Akses Pemilik Dibutuhkan!"
                  print(f"⛔ {error_msg}")
                  return Result(False, None, error_msg)

              # 4. Eksekusi fungsi target dengan level akses tersedia
              return func(session_state, *args, access_level=access_level, **kwargs)
          return wrapper
      return decorator
  ```

- [ ] **2B.3** Implementasikan fungsi internal `_log_access_denied()`:
  ```python
  def _log_access_denied(session_state: dict, menu_id: str, active_role: str) -> None:
      """Mencatat insiden pelanggaran akses ke audit_logs via audit_logger.

      (Ref: ACM v1.2 Bab 6.6, Security Design v1.2 Bab 7.2)
      """
      import json
      from db.db_connector import get_db_connection
      from middleware.audit_logger import log_audit_trail

      user_id = session_state.get('user_id', 0)
      cabang_id = session_state.get('cabang_id', 1)
      old_val = {'attempted_menu': menu_id, 'role': active_role}
      new_val = {'status': 'ILLEGAL_ACCESS_PREVENTED', 'resolved_action': 'TERMINATED'}

      conn_res = get_db_connection()
      if conn_res.is_success:
          db_conn = conn_res.data
          try:
              log_audit_trail(
                  pengguna_id=user_id,
                  action_type='ACCESS_DENIED',
                  target_table=menu_id,
                  old_val=old_val,
                  new_val=new_val,
                  cabang_id=cabang_id,
                  db_connection=db_conn
              )
          finally:
              try:
                  db_conn.close()
              except Exception:
                  pass
  ```

- [ ] **2B.4** Implementasikan fungsi `verify_supervisor_escalation()`:
  ```python
  def verify_supervisor_escalation(
      supervisor_role: str,
      db_connection: Any
  ) -> Result:
      """Memverifikasi sandi supervisor (Pemilik/Kepala Percetakan) untuk eskalasi otorisasi.

      Digunakan saat operasi kritis yang membutuhkan kehadiran fisik supervisor
      untuk mengetik kata sandinya langsung di terminal.

      (Ref: ACM v1.2 Bab 6.1 & 6.2, Security Design v1.2 Bab 5.4 & 5.5)

      Args:
          supervisor_role (str): Peran supervisor target ('pemilik' atau 'kepala_percetakan').
          db_connection: Koneksi database aktif.

      Returns:
          Result: is_success=True jika sandi cocok, False jika tidak.
      """
      import getpass
      from middleware.auth_jwt import verify_password

      # Ambil password hash supervisor dari database
      cursor = db_connection.cursor(dictionary=True)
      query = "SELECT id, password_hash, cabang_id FROM pengguna WHERE role = %s LIMIT 1"
      cursor.execute(query, (supervisor_role,))
      supervisor = cursor.fetchone()
      cursor.close()

      if not supervisor:
          return Result(False, None, f"ERR-AUTH-003: Akun supervisor '{supervisor_role}' tidak ditemukan!")

      # Minta input sandi secara aman (karakter tersembunyi)
      print(f"\n🔐 Operasi ini memerlukan otorisasi {supervisor_role}.")
      password_input = getpass.getpass(f"Masukkan sandi {supervisor_role}: ")

      # Verifikasi sandi menggunakan bcrypt
      if verify_password(password_input, supervisor['password_hash']):
          return Result(True, {'supervisor_id': supervisor['id'], 'cabang_id': supervisor['cabang_id']}, None)
      else:
          return Result(False, None, "ERR-AUTH-003: Akses Ditolak: Sandi supervisor salah!")
  ```

- [ ] **2B.5** Implementasikan fungsi `get_visible_menus()`:
  ```python
  def get_visible_menus(active_role: str) -> list[tuple[str, str, str]]:
      """Mengembalikan daftar menu yang terlihat oleh peran aktif untuk dashboard.

      Mengembalikan hanya menu yang peran aktif miliki akses selain DENY.
      Digunakan oleh cli/dashboard.py untuk memfilter tampilan menu.

      (Ref: ACM v1.2 Bab 4, Module Structure v1.2 Bab 4.2)

      Args:
          active_role (str): Peran aktif dari sesi pengguna.

      Returns:
          list[tuple[str, str, str]]: Daftar tuple (menu_id, nama_menu, level_akses).
      """
      visible = []
      for menu_id, permissions in RBAC_MATRIX.items():
          access_level = permissions.get(active_role, ACCESS_DENY)
          if access_level != ACCESS_DENY:
              menu_label = MENU_LABELS.get(menu_id, menu_id)
              visible.append((menu_id, menu_label, access_level))
      return visible
  ```

- [ ] **2B.6** Definisikan dictionary `MENU_LABELS` untuk label tampilan menu:
  ```python
  MENU_LABELS = {
      'MENU-BASE-001': 'Login',
      'MENU-BASE-002': 'Logout',
      'MENU-BASE-003': 'Dashboard Utama',
      'MENU-BASE-004': 'Ubah Password',
      'MENU-M1-001': 'Catat Transaksi Penjualan',
      'MENU-M1-002': 'Ubah Skema Harga',
      # ... (lengkapi untuk seluruh 48 menu)
  }
  ```
  - [ ] Pastikan SETIAP kunci di `RBAC_MATRIX` memiliki label yang sesuai di `MENU_LABELS`.

---

### TAHAP 3: Verifikasi `middleware/audit_logger.py`

- [ ] **3.1** Baca kode `middleware/audit_logger.py` yang sudah ada.
- [ ] **3.2** Verifikasi bahwa fungsi `log_audit_trail()`:
  - [ ] Menerima parameter `pengguna_id`, `action_type`, `target_table`, `old_val`, `new_val`, `cabang_id`, `db_connection` sesuai dengan Module Structure Bab 7.4.
  - [ ] Melakukan INSERT ke tabel `audit_logs` dengan parameterized query `%s`.
  - [ ] Menangani exception tanpa crash (fail-secure).
- [ ] **3.3** Jika `log_audit_trail()` sudah benar → **JANGAN UBAH** file ini.
- [ ] **3.4** Jika ada ketidaksesuaian (misal: parameter nama berbeda) → perbaiki **hanya** yang tidak sesuai, sisanya **JANGAN DIUBAH**.

---

### TAHAP 4: Update `cli/dashboard.py`

- [ ] **4.1** Tambahkan import `get_visible_menus` dari `middleware.rbac_guard`:
  ```python
  from middleware.rbac_guard import get_visible_menus
  ```
- [ ] **4.2** Di dalam fungsi `render_dashboard()`, setelah render header, panggil `get_visible_menus()`:
  ```python
  visible_menus = get_visible_menus(role)
  ```
- [ ] **4.3** Render daftar menu secara dinamis berdasarkan `visible_menus`:
  - Kelompokkan menu berdasarkan modul (M.1, M.2, dst.).
  - Tampilkan nomor urut sebagai hotkey navigasi.
  - Tampilkan indikator level akses (misal: `[📖]` untuk READ, `[📝]` untuk INPUT).
  - Tambahkan opsi `[0] Logout` di akhir daftar (selalu terlihat untuk semua peran).
- [ ] **4.4** Di dalam fungsi `handle_navigation()`, petakan pilihan pengguna ke `menu_id` dari `visible_menus`:
  - Jika menu belum diimplementasikan → tampilkan placeholder: `"Menu ini belum diimplementasikan."`.
  - Jika menu sudah diimplementasikan → panggil fungsi terkait dengan decorator `@require_role`.
- [ ] **4.5** Pastikan tidak ada perubahan pada logika logout yang sudah ada.
- [ ] **4.6** Pastikan tidak ada perubahan pada validasi token yang sudah ada.

---

### TAHAP 5: Implementasi Test Cases

- [ ] **5.1** Buat atau perbarui file `tests/test_rbac_security.py`:
  ```python
  """
  Nama Modul: test_rbac_security.py
  Deskripsi: Unit & Integration testing untuk validasi matriks RBAC Multi-Level.
             (Ref: Module Structure v1.2 Bab 11.3, ACM v1.2)
  Author: [Nama Pelaksana]
  Tanggal: [YYYY-MM-DD]
  """
  ```
- [ ] **5.2** Tulis test case: `test_rbac_matrix_completeness()` — Pastikan RBAC_MATRIX memiliki tepat 48 entry.
- [ ] **5.3** Tulis test case: `test_pemilik_has_full_access_all_menus()` — Peran `pemilik` memiliki `ACCESS_FULL` di semua 48 menu.
- [ ] **5.4** Tulis test case: `test_default_deny_unknown_role()` — Peran `guest` atau role tidak dikenal mendapat `ACCESS_DENY` di semua menu.
- [ ] **5.5** Tulis test case: `test_kasir_denied_payroll()` — `kasir` terblokir dari `MENU-M4-002`.
- [ ] **5.6** Tulis test case: `test_gudang_denied_transaksi()` — `gudang` terblokir dari `MENU-M1-001`.
- [ ] **5.7** Tulis test case: `test_desainer_access_arsip_desain()` — `desainer` memiliki `ACCESS_FULL` di `MENU-M5-002`.
- [ ] **5.8** Tulis test case: `test_kepala_no_inheritance()` — `kepala_percetakan` TIDAK bisa akses `MENU-M1-003` (Kelola DP), sesuai No Inheritance Policy.
- [ ] **5.9** Tulis test case: `test_fotocopy_print_rtl_access()` — `fotocopy_print` memiliki `ACCESS_RTL` di `MENU-M1-001`.
- [ ] **5.10** Tulis test case: `test_get_visible_menus_kasir()` — Fungsi `get_visible_menus('kasir')` hanya mengembalikan menu yang kasir boleh akses.
- [ ] **5.11** Tulis test case: `test_get_visible_menus_pemilik_returns_all()` — Fungsi `get_visible_menus('pemilik')` mengembalikan semua 48 menu.
- [ ] **5.12** Jalankan seluruh test: `python -m pytest tests/test_rbac_security.py -v`
- [ ] **5.13** Pastikan semua test PASS tanpa error.

---

### TAHAP 6: Verifikasi & Validasi Akhir

- [ ] **6.1** Jalankan `python -m pytest tests/ -v` untuk memastikan tidak ada test yang rusak di seluruh suite.
- [ ] **6.2** Verifikasi bahwa `RBAC_MATRIX` memiliki tepat **48 kunci** (hitung manual).
- [ ] **6.3** Cross-check setiap entry di `RBAC_MATRIX` dengan tabel matriks di Bab 2.2 issue ini. Pastikan tidak ada **mismatch** antara dictionary dan tabel.
- [ ] **6.4** Verifikasi bahwa `MENU_LABELS` memiliki label untuk setiap kunci di `RBAC_MATRIX` (tidak ada key yang hilang).
- [ ] **6.5** Verifikasi bahwa `_log_access_denied()` dipanggil di decorator `require_role()` dan berjalan tanpa crash.
- [ ] **6.6** Verifikasi bahwa `cli/dashboard.py` menampilkan menu berbeda untuk peran `pemilik` vs `kasir` vs `gudang`.
- [ ] **6.7** Verifikasi bahwa kode TIDAK menggunakan f-string untuk query SQL.
- [ ] **6.8** Verifikasi bahwa semua fungsi publik memiliki docstring PEP 257 lengkap.
- [ ] **6.9** Verifikasi bahwa semua fungsi publik memiliki type hints lengkap.
- [ ] **6.10** Verifikasi bahwa tidak ada penggunaan `class` di seluruh kode baru.
- [ ] **6.11** Verifikasi import order: Standard Library → Third-Party → Local Modules.
- [ ] **6.12** Pastikan tidak ada fitur lain yang rusak akibat perubahan ini (regression check).

---

## 5. Instruksi Tambahan Spesifik RBAC

### 5.1. Prinsip Least Privilege dalam Implementasi
- Setiap peran hanya mendapat akses **minimum** yang diperlukan. Jika ragu apakah suatu peran perlu akses ke menu tertentu, **defaultnya adalah DENY**.
- Jangan pernah menambahkan akses "karena mungkin berguna nanti". Ikuti ACM v1.2 secara harfiah.

### 5.2. Penanganan Menu dengan Level Akses Berbeda
- Level `READ` berarti fungsi menu hanya menampilkan data, tombol edit/hapus disembunyikan.
- Level `INPUT` berarti fungsi menu hanya menampilkan form input baru, tanpa edit/hapus.
- Level `INPUT_READ` berarti fungsi menu bisa input baru dan melihat data, tanpa edit/hapus.
- Level `RTL` berarti akses retail terbatas (hanya transaksi sederhana eceran fotocopy/print).
- Level `ESC` berarti memerlukan eskalasi sandi supervisor sebelum aksi diproses.
- Pelaksana hanya perlu mendefinisikan level ini di RBAC_MATRIX. Penanganan per-level di dalam masing-masing fungsi menu **bukan** cakupan issue ini.

### 5.3. Penanganan Escalation (ESC)
- Untuk menu yang bertanda `ESC`, decorator `require_role()` tetap mengizinkan akses (bukan DENY).
- Fungsi menu target yang memerlukan eskalasi akan memanggil `verify_supervisor_escalation()` secara mandiri di dalam logika bisnisnya masing-masing (di issue terpisah).
- Di issue ini, cukup pastikan `ACCESS_ESC` terdefinisi dan `verify_supervisor_escalation()` tersedia sebagai utility.

### 5.4. Sinkronisasi dengan `auth_jwt.py`
- Tuple `VALID_ROLES` di `rbac_guard.py` HARUS identik dengan `VALID_ROLES` di `auth_jwt.py`. Jika ada perbedaan, gunakan yang di `auth_jwt.py` sebagai sumber kebenaran, atau lebih baik import langsung:
  ```python
  from middleware.auth_jwt import VALID_ROLES
  ```

### 5.5. Kode Error yang Digunakan

| Kode Error | Pesan | Kapan Digunakan |
|---|---|---|
| `ERR-AUTH-003` | Akses Ditolak: Hak Akses Pemilik Dibutuhkan! | Peran mencoba akses menu yang di-DENY. |
| `ERR-AUTH-011` | Hak akses supervisor dibutuhkan untuk menyetujui Stock Opname! | Eskalasi Kepala Percetakan gagal. |
| `ERR-AUTH-029` | Verifikasi sandi Pemilik gagal. Pengeluaran besar dibatalkan! | Eskalasi pengeluaran > Rp 500.000 gagal. |
| `ERR-FILE-039` | Gagal memulihkan data. Berkas cadangan korup atau sandi salah! | Eskalasi restorasi database gagal. |
| `ERR-SESSION-001` | Sesi login tidak ditemukan. Harap login terlebih dahulu! | Token JWT tidak ada. |
| `ERR-SESSION-002` | Sesi login tidak sah/rusak. Harap login kembali! | Token JWT expired/invalid. |

---

## 6. Catatan Data Kosong / Belum Tersedia

Jika selama pengerjaan ditemukan data yang kosong atau tidak ada di file referensi, tandai di sini:

- [ ] `# DATA_KOSONG: [deskripsi]` — Komunikasikan ke pemilik proyek.

> **Saat ini belum teridentifikasi data kosong. Seluruh matriks RBAC tersedia lengkap di ACM v1.2.**

---

## 7. Kriteria Selesai (Definition of Done)

Issue ini dianggap **SELESAI** jika dan hanya jika:

1. ✅ `RBAC_MATRIX` di `middleware/rbac_guard.py` memiliki tepat **48 entry** (44 menu + 4 base) yang 100% sinkron dengan ACM v1.2.
2. ✅ Setiap entry berisi level akses granular (`FULL`/`READ`/`INPUT`/`INPUT_READ`/`RTL`/`ESC`) — bukan hanya boolean.
3. ✅ Fungsi `check_menu_permission()` mengembalikan level akses (string), bukan boolean.
4. ✅ Decorator `require_role()` mencatat audit trail `ACCESS_DENIED` ke database.
5. ✅ Fungsi `verify_supervisor_escalation()` tersedia dan fungsional.
6. ✅ Fungsi `get_visible_menus()` tersedia dan digunakan oleh `cli/dashboard.py`.
7. ✅ Dashboard menampilkan menu berbeda untuk peran berbeda.
8. ✅ Seluruh test di `tests/test_rbac_security.py` PASS.
9. ✅ Tidak ada feature lain yang rusak (regression test pass).
10. ✅ Kode mengikuti standar: FP murni, Result Pattern, type hints, docstring, snake_case, parameterized query.

---

## 8. Referensi Silang (Traceability)

| Item Issue | ACM Ref | Security Design Ref | Module Structure Ref | Coding Standard Ref |
|---|---|---|---|---|
| RBAC_MATRIX | Bab 4.2 – 4.12 | Bab 5.3 | Bab 7.3 | Bab 10.4 |
| Default Deny | Bab 6.7 | Bab 5.6 | — | — |
| No Inheritance | Bab 6.8 | — | — | — |
| Eskalasi Pemilik | Bab 6.1 | Bab 5.4 | — | — |
| Eskalasi Kepala | Bab 6.2 | Bab 5.5 | — | — |
| Audit ACCESS_DENIED | Bab 6.6 | Bab 7.2 | Bab 7.4 | Bab 10.6 |
| require_role() | — | Bab 5.2 & 12.2 | Bab 7.3 | Bab 10.4 |
| Test RBAC | — | — | Bab 11.3 | — |

---

*Dokumen issue ini disusun oleh Claude Opus 4.6 (Thinking) pada 2026-06-07 berdasarkan analisis mendalam terhadap 7 dokumen referensi SDLC AbuCom.*
