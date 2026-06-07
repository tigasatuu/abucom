---
issue_id     : 0124
judul        : Feature Navigasi Menu Utama CLI dengan Hotkey Standar
status       : Open
prioritas    : High
tanggal      : 2026-06-07
tipe         : Feature Implementation
modul_target : Presentation Layer (cli/dashboard.py) & Cross-cutting (middleware/rbac_guard.py)
estimasi     : 3-5 jam kerja
---

# Issue #0124 — Feature Navigasi Menu Utama CLI dengan Hotkey Standar

---

## 1. Persona Pelaksana (Executor Persona)

**Kamu adalah `Senior CLI UX Architect & Terminal Navigation Specialist`.**

Kamu memiliki keahlian mendalam dalam:
- Arsitektur navigasi menu CLI berbasis keyboard-only (hotkey numerik).
- Implementasi Presentation Layer menggunakan Python `rich` library dan `tabulate`.
- Penerapan standar Functional Programming (FP) murni tanpa class di alur bisnis.
- Penerapan pola State Dictionary Passing untuk navigasi menu bersarang (nested).
- Integrasi RBAC (Role-Based Access Control) pada filter visibilitas menu per peran.
- Konvensi UX terminal: breadcrumb, ANSI color, sanitasi input, dan error code standar.

**Instruksi kepribadian:**
- Kamu WAJIB bekerja secara rapi, bersih, tidak tergesa-gesa, dan tidak buru-buru.
- Kamu WAJIB memastikan setiap baris kode yang kamu tulis sesuai dengan standar SDLC yang sudah ditetapkan.
- Kamu WAJIB menghasilkan pekerjaan yang lengkap dan tuntas agar tidak menghambat feature lain.
- Jika ada data yang kosong atau tidak tersedia pada file referensi, kamu WAJIB menandainya dengan komentar `# DATA_KOSONG: [deskripsi]` agar bisa ditindaklanjuti.

---

## 2. Dokumen Referensi Utama

Berikut adalah daftar file referensi yang **WAJIB** dibaca dan diekstrak secara menyeluruh sebelum memulai implementasi. Jangan lewatkan detail kecil apapun yang relevan.

### 2.1. File Referensi Wajib (MUST READ)

| No | Path Relatif File | Alasan Relevansi |
|:--:|:---|:---|
| R-01 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | **SSoT (Single Source of Truth)** untuk konvensi navigasi global, hierarki menu, peta menu, matriks visibilitas per role, hotkey numerik, tombol `0` kembali, tombol `q` exit, breadcrumb, ANSI color palette, wireframe dashboard, dan alur interaksi dasar (login, logout, dashboard, ubah password). |
| R-02 | `docs/sdlc/03_design/03_system_architecture.md` | Blueprint arsitektur 4-layer logis, pola State Dictionary Passing, pola Nested Closures untuk breadcrumb, dan pola error handling Result Pattern. |
| R-03 | `docs/sdlc/04_implementation/03_module_structure.md` | Spesifikasi file-level `cli/dashboard.py` (fungsi `render_dashboard`, `handle_navigation`), mapping modul-to-file, dan dependensi impor yang diizinkan. |
| R-04 | `docs/sdlc/04_implementation/01_coding_standard.md` | Aturan penamaan, format kode PEP 8, FP murni, type hints, konvensi visual `rich`/`tabulate`, konvensi navigasi menu (hotkey, breadcrumb, back/exit), template Result Pattern, standar error codes, dan template header module. |
| R-05 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | SSoT otorisasi menu per role (8 peran) untuk filter visibilitas menu di dashboard. |

### 2.2. File Referensi Pendukung (SHOULD READ)

| No | Path Relatif File | Alasan Relevansi |
|:--:|:---|:---|
| S-01 | `docs/sdlc/03_design/06_security_design.md` | Aturan sanitasi input CLI, JWT session validation, dan audit trail untuk navigasi. |
| S-02 | `docs/sdlc/02_analysis/02_software_requirements.md` | Kebutuhan fungsional SRS terkait navigasi (SRS-F-ADD-01 startup checks). |

### 2.3. File Referensi Narasi

| No | Path Relatif File | Status |
|:--:|:---|:---|
| N-01 | `docs/sdlc/narasi.txt` | **TIDAK DIBUTUHKAN** untuk issue ini. Narasi berisi konteks bisnis umum yang sudah terabstraksi ke dalam dokumen SDLC fase 02-04. Issue ini fokus pada implementasi teknis navigasi CLI yang sudah terdefinisi lengkap di R-01 s.d R-05. |

---

## 3. Rangkuman Detail Data Referensi yang Relevan

Berikut adalah ekstraksi seluruh detail data dari dokumen referensi yang **spesifik mendukung** pengerjaan issue ini. Baca dan pahami setiap poin sebelum mulai coding.

### 3.1. Konvensi Navigasi Global (Sumber: R-01, Bab 2.2)

1. **Tombol `0` (Kembali):** Di setiap layar sub-menu atau form input, tombol `0` secara konsisten berfungsi untuk membatalkan proses dan kembali ke menu setingkat di atasnya.
2. **Hotkey Numerik:** Pilihan menu utama dan sub-menu WAJIB dipicu menggunakan angka berurutan (`1`, `2`, `3`, dst).
3. **Pola Konfirmasi Aksi Destruktif:** Operasi kritis (retur, hapus, pembatalan, opname, payroll, restore) WAJIB menyajikan konfirmasi eksplisit `[Y/N]` (Case-Insensitive) sebelum data disimpan.
4. **Pola Enter Kosong:** Menekan `Enter` tanpa mengetikkan nilai pada prompt input opsional akan mengisi nilai bawaan (*default value*) atau mengulangi prompt jika field bersifat mandatory.
5. **Exit Darurat:** Tombol `q` pada menu utama atau penekanan shortcut keyboard `Ctrl+C` akan memicu penutupan aplikasi secara aman (*graceful exit*) setelah membersihkan memori token JWT lokal.

### 3.2. Hierarki Menu Utama (Sumber: R-01, Bab 3.1)

Dashboard utama setelah login menampilkan **10 modul utama** + **2 aksi dasar** (Ubah Password, Logout):

```
Dashboard Utama (UC-043)
├── [1-10] Modul M.1 s.d M.10 (terfilter oleh RBAC per role)
├── [P]    Ubah Password (UC-044)     ← Aksi dasar, bukan modul
├── [0]    Logout (UC-042)            ← Tombol kembali/keluar
└── [q]    Exit Darurat               ← Graceful shutdown
```

Penomoran modul di dashboard:

| Hotkey | Menu ID | Nama Menu | Cakupan |
|:------:|:--------|:----------|:--------|
| 1 | M.1 | Transaksi & Harga | 6 sub-menu (UC-001 s.d UC-006) |
| 2 | M.2 | Inventaris & BOM | 10 sub-menu (UC-007 s.d UC-016) |
| 3 | M.3 | PPOB & Service | 3 sub-menu (UC-017 s.d UC-019) |
| 4 | M.4 | SDM & Payroll | 4 sub-menu (UC-020 s.d UC-023) |
| 5 | M.5 | Antrian & Desain | 3 sub-menu (UC-024 s.d UC-026) |
| 6 | M.6 | Pinjaman & Laba-Rugi | 5 sub-menu (UC-027 s.d UC-031) |
| 7 | M.7 | Keamanan & Audit | 6 sub-menu (UC-032 s.d UC-037) |
| 8 | M.8 | CRM Pelanggan | 1 sub-menu (UC-038) |
| 9 | M.9 | Multi-Cabang | 1 sub-menu (UC-039) |
| 10 | M.10 | Config Runtime | 1 sub-menu (UC-040) |

### 3.3. Matriks Visibilitas Menu per Role (Sumber: R-01, Bab 3.3 & R-05)

Menu yang **TIDAK diizinkan** (`DENY`) untuk suatu role WAJIB **disembunyikan** dari tampilan console. Penomoran hotkey numerik harus **dinamis** (berurut mulai dari 1) berdasarkan menu yang terlihat saja.

Contoh:
- **Role `kasir`:** Hanya melihat menu M.1, M.3, M.4 (absensi saja), M.5 (sebagian), M.6 (pengeluaran saja), M.7 (shift handover & rekonsiliasi kas). Modul yang tidak terlihat tidak ditampilkan dan tidak diberi hotkey.
- **Role `pemilik`:** Melihat seluruh 10 modul lengkap.

### 3.4. Konvensi Visual (Sumber: R-01, Bab 2.3 & R-04, Bab 11)

- **Panel Visual (`rich` library):** Header menu dan dashboard dibungkus dalam panel `rich` dengan border double line (`═══`).
- **ANSI Color Palette:**
  - `Green` (hijau): Sukses, status LUNAS.
  - `Red` (merah): Error, akses ditolak.
  - `Yellow` (kuning): Peringatan, konfirmasi.
  - `Blue` (biru): Panduan, breadcrumb.
  - `Magenta` (magenta): Judul utama modul dan banner dashboard.
- **Tabel Menu (`tabulate`):** Daftar menu ditampilkan rapi menggunakan `tabulate` atau format `rich` grid.

### 3.5. Alur Interaksi Dashboard (Sumber: R-01, Bab 4.3)

| No. | Aktor/Sistem | Aksi | Tipe |
|:---:|:---|:---|:---:|
| 1 | Sistem | Mendeteksi payload `role` dari parameter session JWT. | Proses |
| 2 | Sistem | Menarik data ringkasan harian spesifik dari database MySQL. | Proses |
| 3 | Sistem | Menampilkan panel dashboard sesuai role (Pemilik, Kasir, Gudang, dll). | Output |
| 4 | Sistem | Menampilkan menu navigasi yang filternya disesuaikan (hanya memunculkan menu yang diizinkan ACM). | Output |

### 3.6. Alur Interaksi Logout (Sumber: R-01, Bab 4.2)

| No. | Aksi |
|:---:|:---|
| 1 | Pengguna memilih opsi logout di menu utama. |
| 2 | Sistem meminta konfirmasi `[Y/N]`. |
| 3 | Pengguna mengkonfirmasi `Y`. |
| 4 | Sistem menghapus token JWT dari memori state dictionary. |
| 5 | Sistem membersihkan layar dan redirect ke layar login. |

### 3.7. Pola State Dictionary Passing (Sumber: R-02, Bab 4.4.2 & R-04, Bab 8.4)

```python
session_state = {
    'user_id': 3,
    'username': 'kasir_andi',
    'role': 'kasir',
    'token': 'jwt_string_token',
    'cabang_id': 1
}
```

State ini dialirkan sebagai parameter ke setiap fungsi menu secara berurutan.

### 3.8. Pola Nested Closures untuk Breadcrumb (Sumber: R-04, Bab 8.5)

```python
from typing import Callable

def make_navigation(current_path: str) -> Callable[[str], str]:
    def add_subpath(subpath: str) -> str:
        return f"{current_path} > {subpath}"
    return add_subpath
```

### 3.9. File Target dan Dependensi (Sumber: R-03, Bab 4.2)

**File utama yang dimodifikasi:** `cli/dashboard.py`

| Atribut | Nilai |
|:---|:---|
| **Fungsi Publik** | `render_dashboard(session_state: dict) -> None`, `handle_navigation(session_state: dict, pilihan: str) -> dict` |
| **Dependensi Impor** | `cli.menu_transaksi`, `cli.menu_inventaris`, `cli.menu_ppob_service`, `cli.menu_sdm_finansial`, `cli.menu_configs`, `middleware.rbac_guard`, `utils.text_formatter` |
| **Menu ID** | `MENU-BASE-003` |
| **Tabel Database diakses** | `pengguna`, `transaksi`, `antrian_kerja`, `shift_handover` (via `db.query_builder`) |
| **Hak Akses** | Seluruh 8 peran (visualisasi menu terfilter RBAC) |

### 3.10. Kondisi Kode Saat Ini (Current State)

Berdasarkan pembacaan file-file yang ada:

1. **`cli/dashboard.py`** — **SUDAH ADA**, berisi implementasi dasar:
   - `render_dashboard()` sudah memiliki loop utama, validasi token, render header, filter menu via `get_visible_menus()`, logika logout, dan pemanggilan `handle_navigation()`.
   - `handle_navigation()` sudah memiliki routing untuk `MENU-M10-001` (menu configs). Menu lain menampilkan placeholder.
   - **MASALAH:** Navigasi saat ini menggunakan penomoran indeks flat (1, 2, 3...) TANPA pengelompokan per modul yang jelas. Menu ditampilkan sebagai daftar datar (flat list), bukan terstruktur per modul. Sub-menu belum diimplementasikan sebagai level navigasi terpisah.

2. **`middleware/rbac_guard.py`** — **SUDAH ADA**, berisi:
   - `RBAC_MATRIX` lengkap 48 entri (44 use case + 4 base).
   - `MENU_LABELS` lengkap untuk semua menu ID.
   - `get_visible_menus()` sudah memfilter menu berdasarkan role, tetapi mengembalikan daftar flat tanpa pengelompokan modul.
   - `check_menu_permission()` dan decorator `require_role()` sudah fungsional.

3. **`cli/menu_*.py`** — **SUDAH ADA** sebagai skeleton/placeholder:
   - `menu_transaksi.py`: Fungsi `show_menu_transaksi()` berisi placeholder TODO.
   - `menu_inventaris.py`: Fungsi `show_menu_inventaris()` berisi placeholder TODO.
   - `menu_ppob_service.py`: Fungsi `show_menu_ppob_service()` berisi placeholder TODO.
   - `menu_sdm_finansial.py`: Fungsi `show_menu_sdm_finansial()` berisi placeholder TODO.
   - `menu_configs.py`: Fungsi `show_menu_configs()` **SUDAH DIIMPLEMENTASIKAN** penuh.
   - `menu_laporan.py`: Skeleton minimal.

4. **`cli/__init__.py`** — **SUDAH ADA**, berisi alur login lengkap yang memanggil `render_dashboard()`.

---

## 4. Batasan dan Cakupan Issue

### 4.1. Cakupan (IN-SCOPE) ✅

Issue ini mencakup **HANYA** implementasi navigasi menu utama CLI di level **Dashboard → Modul (Level 1) → Daftar Sub-Menu Modul (Level 2)**, yaitu:

1. **Perbaikan tampilan Dashboard utama** — Menampilkan daftar 10 modul yang terfilter RBAC dengan penomoran hotkey numerik dinamis, panel `rich`, breadcrumb path, dan aksi dasar (Ubah Password, Logout, Exit).
2. **Implementasi navigasi 2 level** — Dari dashboard ke level modul, dari level modul ke daftar sub-menu modul, dan kembali ke dashboard menggunakan tombol `0`.
3. **Implementasi routing `handle_navigation()`** — Menghubungkan setiap menu ID ke fungsi `show_menu_*()` yang sudah ada di file `cli/menu_*.py`.
4. **Implementasi sub-menu loop per modul** — Setiap modul (M.1 s.d M.10) menampilkan daftar sub-menu yang terfilter RBAC dengan hotkey numerik, breadcrumb, dan tombol `0` kembali.
5. **Implementasi aksi Ubah Password (UC-044)** — Form interaktif ubah password di menu dashboard.
6. **Penyesuaian `get_visible_menus()`** — Mengelompokkan menu berdasarkan modul untuk mendukung navigasi 2 level.
7. **Implementasi breadcrumb path** di setiap level navigasi.
8. **Implementasi exit darurat `q`** dan `Ctrl+C` graceful shutdown.
9. **Penanganan input invalid** — Menampilkan pesan error standar dan mengulangi prompt.

### 4.2. Di Luar Cakupan (OUT-OF-SCOPE) ❌

Issue ini **TIDAK** mencakup:

1. ❌ Implementasi logika bisnis di dalam sub-menu (formulir transaksi, kalkulasi HPP, dll). Sub-menu yang belum diimplementasikan tetap menampilkan pesan placeholder.
2. ❌ Implementasi dashboard ringkasan data harian (grafik teks, panel laba rugi, alert stok kritis). Dashboard data akan menjadi issue terpisah.
3. ❌ Modifikasi file di `logic/`, `db/`, atau `middleware/auth_jwt.py`.
4. ❌ Penambahan tabel database baru atau modifikasi schema SQL.
5. ❌ Unit testing atau integration testing untuk navigasi menu.

### 4.3. Alur Navigasi yang Harus Dibangun

```
LEVEL 0: Layar Login
    ↓ (login sukses)
LEVEL 1: Dashboard Utama
    ├── [1-N]  Pilih Modul (hotkey numerik dinamis, terfilter RBAC)
    │     ↓
    │   LEVEL 2: Sub-Menu Modul (misal M.1 Transaksi)
    │     ├── [1-N]  Pilih Sub-Menu (hotkey numerik, terfilter RBAC)
    │     │     ↓
    │     │   LEVEL 3: Fungsi Target (misal form_pencatatan_transaksi)
    │     │     └── [0] Kembali ke Sub-Menu Modul
    │     ├── [0]    Kembali ke Dashboard
    │     └── [q]    Exit Darurat
    ├── [P]    Ubah Password (UC-044)
    ├── [0]    Logout (UC-042) + konfirmasi [Y/N]
    └── [q]    Exit Darurat (graceful shutdown)
```

---

## 5. Instruksi Keamanan dan Kompatibilitas

### 5.1. Pastikan Tidak Menyenggol Feature Lain

- [ ] **JANGAN** mengubah signature fungsi publik yang sudah ada di `cli/menu_*.py`. Fungsi `show_menu_transaksi(session_state)`, `show_menu_inventaris(session_state)`, dll. HARUS tetap bisa dipanggil dengan argumen `session_state: dict` saja.
- [ ] **JANGAN** mengubah logika internal `middleware/rbac_guard.py` selain menambah fungsi helper baru (misalnya fungsi pengelompokan menu per modul).
- [ ] **JANGAN** mengubah `cli/__init__.py` (alur login) kecuali benar-benar diperlukan dan minimal.
- [ ] **JANGAN** mengubah `middleware/auth_jwt.py`, `middleware/audit_logger.py`, `db/db_connector.py`, atau file apapun di `logic/`.
- [ ] **JANGAN** mengubah `main.py`.
- [ ] **PASTIKAN** semua fungsi placeholder `show_menu_*()` yang berisi `# TODO` di `cli/menu_*.py` tetap bisa dipanggil tanpa error.
- [ ] **PASTIKAN** `cli/menu_configs.py` yang sudah diimplementasikan penuh tetap berfungsi normal.

### 5.2. Standar Kualitas

- [ ] Setiap fungsi publik baru WAJIB memiliki docstring PEP 257 Google Style lengkap (deskripsi, Args, Returns).
- [ ] Setiap fungsi publik baru WAJIB memiliki type hints lengkap (PEP 484).
- [ ] Setiap file yang dimodifikasi WAJIB memiliki header module sesuai template standar.
- [ ] Semua input pengguna WAJIB disanitasi melalui `sanitasi_input_cli()` dari `logic/safety_validator.py`.
- [ ] Semua pesan error WAJIB menggunakan format: `⛔ ERR-[KATEGORI]-[NOMOR]: [Pesan deskriptif bahasa Indonesia]`.
- [ ] Kode WAJIB kompatibel lintas OS (Windows 11 dan Linux Debian 12).
- [ ] Indentasi WAJIB 4 spasi, baris maksimum 120 karakter.
- [ ] String internal gunakan single quote (`'`), string display gunakan double quote (`"`).
- [ ] DILARANG menggunakan `class` atau OOP.
- [ ] DILARANG menggunakan variabel global mutable.
- [ ] DILARANG menggunakan `from module import *`.

---

## 6. Tahapan Implementasi Detail (Low-Level Checklist)

### Fase 1: Pembacaan dan Pemahaman Referensi

- [ ] Baca file `docs/sdlc/03_design/04_cli_interaction_flow.md` secara LENGKAP, terutama:
  - [ ] Bab 2.2 — Konvensi Navigasi Global (tombol `0`, hotkey numerik, pola konfirmasi `[Y/N]`, Enter kosong, exit darurat `q`/`Ctrl+C`).
  - [ ] Bab 2.3 — Konvensi Visual & Pustaka Tampilan (panel `rich`, tabel `tabulate`, ANSI color palette).
  - [ ] Bab 2.4 — Konvensi Input & Validasi (sanitasi ASCII, password masking).
  - [ ] Bab 2.5 — Konvensi Pesan Error & Feedback (format `⛔ ERR-[KATEGORI]-[NOMOR]`).
  - [ ] Bab 3.1 — Diagram Hierarki Menu Utama (Mermaid Tree).
  - [ ] Bab 3.2 — Deskripsi Singkat Setiap Node Menu (44 + 4 menu).
  - [ ] Bab 3.3 — Matriks Visibilitas Menu per Role (8 peran).
  - [ ] Bab 4.2 — Alur Interaksi Logout (UC-042).
  - [ ] Bab 4.3 — Alur Interaksi Dashboard Utama (UC-043).
  - [ ] Bab 4.4 — Alur Interaksi Ubah Password (UC-044).
- [ ] Baca file `docs/sdlc/04_implementation/03_module_structure.md`, terutama:
  - [ ] Bab 4.2 — Spesifikasi `cli/dashboard.py` (fungsi, dependensi, hak akses).
  - [ ] Bab 4.3 s.d 4.7 — Spesifikasi semua file `cli/menu_*.py` (fungsi publik dan mapping menu ID).
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md`, terutama:
  - [ ] Bab 2.2 — Prinsip FP Murni (pure functions, immutability, tanpa class).
  - [ ] Bab 8.4 — Pola State Dictionary Passing.
  - [ ] Bab 8.5 — Pola Nested Closures untuk breadcrumb.
  - [ ] Bab 11.1 s.d 11.7 — Standar Penulisan Kode CLI (visual `rich`, `tabulate`, navigasi, getpass, error, clear terminal, encoding).
- [ ] Baca file `middleware/rbac_guard.py` untuk memahami struktur `RBAC_MATRIX`, `MENU_LABELS`, dan fungsi `get_visible_menus()`.
- [ ] Baca file `cli/dashboard.py` untuk memahami implementasi saat ini.
- [ ] Baca file `cli/__init__.py` untuk memahami bagaimana `render_dashboard()` dipanggil.
- [ ] Baca file `cli/menu_configs.py` sebagai contoh modul yang sudah diimplementasikan penuh — pelajari pola sub-menu loop, breadcrumb, dan input handling yang digunakan di sana.

### Fase 2: Penambahan Fungsi Helper di `middleware/rbac_guard.py`

**File target:** `middleware/rbac_guard.py`

- [ ] Tambahkan fungsi baru `get_visible_modules(active_role: str) -> list[tuple[str, str]]` yang:
  - [ ] Membaca `RBAC_MATRIX` dan mengelompokkan menu berdasarkan prefix modul (`M1`, `M2`, ..., `M10`).
  - [ ] Mengembalikan daftar tuple `(module_key, module_name)` dari modul yang memiliki **minimal 1 sub-menu** yang diizinkan untuk `active_role`.
  - [ ] Menggunakan `MODULE_NAMES` (yang saat ini terdefinisi di `dashboard.py`) sebagai sumber label modul — **PINDAHKAN** konstanta `MODULE_NAMES` dari `dashboard.py` ke `rbac_guard.py` agar terpusat.
  - [ ] Contoh output untuk role `kasir`: `[('M1', 'Modul M.1 — Transaksi & Harga'), ('M3', 'Modul M.3 — ...'), ...]`.
- [ ] Tambahkan fungsi baru `get_module_submenus(module_key: str, active_role: str) -> list[tuple[str, str, str]]` yang:
  - [ ] Mengembalikan daftar tuple `(menu_id, menu_label, access_level)` dari sub-menu di dalam modul tertentu yang diizinkan untuk `active_role`.
  - [ ] `module_key` adalah string seperti `'M1'`, `'M2'`, dst.
  - [ ] Contoh output untuk modul `'M1'` dan role `kasir`: `[('MENU-M1-001', 'Mencatat Transaksi Penjualan', 'FULL'), ('MENU-M1-003', 'Mengelola DP & Pelunasan', 'FULL'), ...]`.
- [ ] Pastikan type hints dan docstring PEP 257 lengkap pada kedua fungsi baru.
- [ ] Pastikan `MODULE_NAMES` yang dipindahkan dari `dashboard.py` LENGKAP untuk 10 modul:
  ```python
  MODULE_NAMES = {
      'M1': 'Modul M.1 — Transaksi & Kebijakan Harga',
      'M2': 'Modul M.2 — Inventaris, BOM & Stock Opname',
      'M3': 'Modul M.3 — Layanan Keuangan, PPOB & Jasa Service',
      'M4': 'Modul M.4 — SDM, Penggajian & Poin Karyawan',
      'M5': 'Modul M.5 — Antrian & Pelacakan Desain',
      'M6': 'Modul M.6 — Pinjaman, Aset & Pengeluaran',
      'M7': 'Modul M.7 — Keamanan, Audit Trail & Hak Akses',
      'M8': 'Modul M.8 — CRM Pelanggan',
      'M9': 'Modul M.9 — Skalabilitas Multi-Cabang',
      'M10': 'Modul M.10 — Konfigurasi Sistem Runtime'
  }
  ```
- [ ] **JANGAN** mengubah fungsi `get_visible_menus()` yang sudah ada — tambahkan fungsi baru tanpa menghapus yang lama, agar jika ada kode lain yang memanggilnya tidak terganggu.
- [ ] **JANGAN** mengubah `RBAC_MATRIX`, `MENU_LABELS`, `check_menu_permission()`, `require_role()`, atau `verify_supervisor_escalation()`.

### Fase 3: Refaktor `cli/dashboard.py` — Dashboard Utama

**File target:** `cli/dashboard.py`

- [ ] **Hapus** konstanta `MODULE_NAMES` dari file ini (sudah dipindahkan ke `rbac_guard.py` di Fase 2).
- [ ] **Update import** untuk mengambil `get_visible_modules`, `get_module_submenus`, dan `MODULE_NAMES` dari `middleware.rbac_guard`.
- [ ] Refaktor fungsi `render_dashboard(session_state: dict) -> None` agar:
  - [ ] **Header Dashboard:** Menampilkan panel `rich` berisi judul `"DASHBOARD UTAMA — AbuCom"` dengan warna `bold magenta`, info pengguna (username, role, cabang), dan breadcrumb `"Dashboard"`.
  - [ ] **Daftar Modul Terfilter:** Menampilkan daftar modul yang diizinkan untuk role aktif menggunakan `get_visible_modules(role)`, dengan hotkey numerik dinamis berurutan dimulai dari `1`.
  - [ ] **Format Tampilan Modul:**
    ```
    ═══════════════════════════════════════════════════
      DASHBOARD UTAMA — AbuCom
      Pengguna: kasir_andi | Peran: kasir | Cabang: 1
    ═══════════════════════════════════════════════════
    Navigasi: Dashboard

    PILIHAN MODUL:
      [1] M.1 — Transaksi & Kebijakan Harga
      [3] M.3 — Layanan Keuangan, PPOB & Jasa Service
      [4] M.4 — SDM, Penggajian & Poin Karyawan
      ...

    AKSI:
      [P] Ubah Password
      [0] Logout
      [q] Keluar Aplikasi

    Pilih Menu [1-N / P / 0 / q]:
    ```
  - [ ] **Penomoran modul:** Gunakan penomoran asli modul (1 untuk M.1, 2 untuk M.2, dst) untuk konsistensi, BUKAN penomoran berurut. Modul yang disembunyikan memang tidak ditampilkan, tetapi nomor modul yang tampil tetap sesuai dengan identitas modulnya (M.1 = 1, M.3 = 3, dst). Ini agar pengguna mudah mengingat.
  - [ ] **Input Handling:**
    - [ ] Input `1` s.d `10`: Panggil `show_module_submenu(session_state, module_key)` (fungsi baru di Fase 4).
    - [ ] Input `P` atau `p`: Panggil fungsi `form_ubah_password(session_state)` (fungsi baru di Fase 5).
    - [ ] Input `0`: Jalankan alur logout (sudah ada, pertahankan logika yang ada).
    - [ ] Input `q`: Jalankan graceful exit (hapus token, bersihkan layar, tampilkan pesan keluar).
    - [ ] Input invalid: Tampilkan `⛔ Pilihan tidak valid. Harap masukkan angka 1-10, P, 0, atau q.` dan kembali ke prompt.
  - [ ] **Validasi Token:** Pertahankan validasi `validate_session_token()` di awal setiap iterasi loop (sudah ada).
  - [ ] **Sanitasi Input:** Pertahankan sanitasi input via `sanitasi_input_cli()` (sudah ada).
  - [ ] **Clear Terminal:** Pertahankan `clear_terminal()` di awal setiap iterasi (sudah ada).
  - [ ] **Graceful Ctrl+C:** Pertahankan penanganan `KeyboardInterrupt` dan `EOFError` (sudah ada).
  - [ ] Pastikan loop dashboard tidak pernah terputus kecuali logout, exit, atau token kedaluwarsa.
- [ ] Refaktor fungsi `handle_navigation(session_state: dict, menu_id: str) -> dict` agar:
  - [ ] Melakukan routing ke fungsi `show_menu_*()` yang sesuai berdasarkan prefix `menu_id`:
    ```python
    # Mapping Menu ID prefix ke fungsi handler
    if menu_id.startswith('MENU-M1-') or menu_id.startswith('MENU-M8-'):
        from cli.menu_transaksi import show_menu_transaksi
        show_menu_transaksi(session_state)
    elif menu_id.startswith('MENU-M2-') or menu_id.startswith('MENU-M5-'):
        from cli.menu_inventaris import show_menu_inventaris
        show_menu_inventaris(session_state)
    elif menu_id.startswith('MENU-M3-'):
        from cli.menu_ppob_service import show_menu_ppob_service
        show_menu_ppob_service(session_state)
    elif menu_id.startswith('MENU-M4-') or menu_id.startswith('MENU-M6-'):
        from cli.menu_sdm_finansial import show_menu_sdm_finansial
        show_menu_sdm_finansial(session_state)
    elif menu_id.startswith('MENU-M7-'):
        # M.7 ditangani oleh dashboard langsung atau module handler terpisah
        ...
    elif menu_id.startswith('MENU-M9-'):
        # Multi-Cabang
        ...
    elif menu_id.startswith('MENU-M10-'):
        from cli.menu_configs import show_menu_configs
        show_menu_configs(session_state)
    ```
  - [ ] Sesuaikan mapping module-to-file berdasarkan tabel di R-03, Bab 14 (Module-to-File Mapping).
  - [ ] Pertahankan validasi token di awal fungsi (sudah ada).
  - [ ] Tampilkan placeholder jika fungsi target belum diimplementasikan: `"Menu ini belum diimplementasikan. Tekan Enter untuk kembali."`.

### Fase 4: Implementasi Sub-Menu Loop per Modul di `cli/dashboard.py`

**File target:** `cli/dashboard.py`

- [ ] Tambahkan fungsi baru `show_module_submenu(session_state: dict, module_key: str) -> None` yang:
  - [ ] Mengambil daftar sub-menu yang diizinkan menggunakan `get_module_submenus(module_key, role)`.
  - [ ] Jika daftar kosong (tidak ada sub-menu yang diizinkan), tampilkan `⛔ ERR-AUTH-003: Anda tidak memiliki akses ke modul ini.` dan kembali.
  - [ ] Menampilkan panel sub-menu dengan:
    - [ ] **Breadcrumb:** `"Dashboard > M.1 Transaksi & Kebijakan Harga"` (menggunakan pola Nested Closures atau f-string sederhana).
    - [ ] **Daftar sub-menu** dengan hotkey numerik dinamis berurut (1, 2, 3, ...).
    - [ ] **Tombol `0`** untuk kembali ke dashboard.
    - [ ] **Tombol `q`** untuk exit darurat.
  - [ ] Format tampilan sub-menu:
    ```
    ═══════════════════════════════════════════════════
      M.1 — Transaksi & Kebijakan Harga
    ═══════════════════════════════════════════════════
    Navigasi: Dashboard > M.1 Transaksi & Kebijakan Harga

    SUB-MENU:
      [1] Mencatat Transaksi Penjualan      [FULL]
      [2] Mengelola DP & Pelunasan           [FULL]
      [3] Pembatalan & Retur                 [ESC]
      [4] Ekspor Struk Thermal              [FULL]

      [0] Kembali ke Dashboard
      [q] Keluar Aplikasi

    Pilih Sub-Menu [1-N / 0 / q]:
    ```
  - [ ] **Input Handling:**
    - [ ] Input `1` s.d `N`: Panggil `handle_navigation(session_state, selected_menu_id)` dengan menu ID yang sesuai.
    - [ ] Input `0`: Kembali ke dashboard (return dari fungsi).
    - [ ] Input `q`: Graceful exit (sama seperti di dashboard).
    - [ ] Input invalid: Tampilkan error dan ulangi prompt.
  - [ ] **Loop sub-menu** HARUS berjalan terus sampai pengguna memilih `0` (kembali) atau `q` (exit).
  - [ ] Sanitasi input via `sanitasi_input_cli()`.
  - [ ] Penanganan `KeyboardInterrupt` dan `EOFError`.
  - [ ] Clear terminal di awal setiap iterasi loop sub-menu.
  - [ ] Pastikan level akses (`[FULL]`, `[READ]`, `[INPUT]`, `[ESC]`, dll) ditampilkan di sebelah nama sub-menu sesuai matriks RBAC.
- [ ] Pastikan fungsi ini memiliki docstring PEP 257 dan type hints lengkap.

### Fase 5: Implementasi Ubah Password (UC-044) di `cli/dashboard.py`

**File target:** `cli/dashboard.py`

- [ ] Tambahkan fungsi baru `form_ubah_password(session_state: dict) -> None` yang:
  - [ ] Menampilkan breadcrumb: `"Dashboard > Ubah Password"`.
  - [ ] Langkah 1: Meminta input password lama menggunakan `getpass.getpass("Masukkan Password Lama: ")`.
  - [ ] Langkah 2: Memverifikasi password lama terhadap hash di database.
    - [ ] Ambil koneksi database via `get_db_connection()`.
    - [ ] Query: `SELECT password_hash FROM pengguna WHERE id = %s` menggunakan `session_state['user_id']`.
    - [ ] Gunakan `middleware.auth_jwt.verify_password()` untuk verifikasi bcrypt.
    - [ ] Jika salah: Tampilkan `⛔ ERR-AUTH-044: Otorisasi Gagal: Kata sandi lama yang Anda masukkan tidak valid!` dan kembali.
  - [ ] Langkah 3: Meminta input password baru: `getpass.getpass("Masukkan Password Baru: ")`.
  - [ ] Langkah 4: Meminta konfirmasi ulang password baru: `getpass.getpass("Masukkan Kembali Password Baru: ")`.
  - [ ] Langkah 5: Validasi password baru:
    - [ ] Minimal 8 karakter.
    - [ ] Password baru harus sama dengan konfirmasi.
    - [ ] Jika tidak valid: Tampilkan `⛔ ERR-VAL-044: Konvalidasi Gagal: Kata sandi baru minimal harus 8 karakter dan bernilai cocok pada kedua input!` dan kembali.
  - [ ] Langkah 6: Hash password baru menggunakan `middleware.auth_jwt.hash_password()` (bcrypt cost 12).
  - [ ] Langkah 7: Update database: `UPDATE pengguna SET password_hash = %s WHERE id = %s`.
  - [ ] Langkah 8: Catat ke audit trail via `middleware.audit_logger.log_audit_trail()` dengan `action_type='UPDATE'`, `target_table='pengguna'`, `old_value={'field': 'password_hash', 'note': '***REDACTED***'}`, `new_value={'field': 'password_hash', 'note': '***REDACTED***'}`.
  - [ ] Langkah 9: Tampilkan pesan sukses hijau: `"✓ Password berhasil diubah! Gunakan sandi baru Anda pada login berikutnya."`.
  - [ ] Langkah 10: Kembali ke dashboard.
- [ ] Pastikan semua koneksi database ditutup dengan benar di blok `finally`.
- [ ] Pastikan fungsi ini memiliki docstring PEP 257 dan type hints lengkap.
- [ ] Gunakan `getpass` untuk semua input password (karakter tersembunyi).

### Fase 6: Implementasi Graceful Exit `q`

**File target:** `cli/dashboard.py`

- [ ] Tambahkan fungsi baru `graceful_exit(session_state: dict) -> None` yang:
  - [ ] Langkah 1: Menghapus token JWT dari `session_state` (set semua key ke `None`).
  - [ ] Langkah 2: Mencatat logout ke audit trail (best effort, jangan gagalkan exit jika audit gagal).
  - [ ] Langkah 3: Membersihkan layar terminal via `clear_terminal()`.
  - [ ] Langkah 4: Menampilkan pesan: `"Aplikasi dihentikan secara aman. Sampai jumpa!"` (warna kuning jika `rich` tersedia).
  - [ ] Langkah 5: Memanggil `sys.exit(0)` untuk menghentikan program sepenuhnya.
- [ ] Pastikan fungsi ini dipanggil dari:
  - [ ] Dashboard utama saat pengguna mengetik `q`.
  - [ ] Sub-menu modul saat pengguna mengetik `q`.
  - [ ] Penanganan `Ctrl+C` (`KeyboardInterrupt`).

### Fase 7: Verifikasi dan Validasi

- [ ] **Verifikasi alur navigasi lengkap:**
  - [ ] Login → Dashboard → Pilih Modul → Sub-Menu → Kembali ke Dashboard → Logout.
  - [ ] Login → Dashboard → Pilih Modul → Sub-Menu → Pilih Sub-Menu → Placeholder → Kembali ke Sub-Menu → Kembali ke Dashboard.
  - [ ] Login → Dashboard → Ubah Password → Kembali ke Dashboard.
  - [ ] Login → Dashboard → Exit (`q`) → Program berhenti.
  - [ ] Login → Dashboard → Ctrl+C → Program berhenti aman.
  - [ ] Login → Dashboard → Input invalid → Error → Prompt ulang.
- [ ] **Verifikasi RBAC:**
  - [ ] Login sebagai `pemilik`: Pastikan semua 10 modul tampil di dashboard.
  - [ ] Login sebagai `kasir`: Pastikan hanya modul yang diizinkan yang tampil (M.1, M.3, M.4, M.5 sebagian, M.6 sebagian, M.7 sebagian, M.8).
  - [ ] Login sebagai `gudang`: Pastikan hanya M.2, M.4 (absensi) yang tampil.
  - [ ] Login dengan role apapun: Pastikan Ubah Password dan Logout selalu tersedia.
- [ ] **Verifikasi sub-menu per modul:**
  - [ ] Masuk ke M.1 sebagai `kasir`: Pastikan hanya sub-menu yang diizinkan yang tampil.
  - [ ] Masuk ke M.2 sebagai `gudang`: Pastikan hanya sub-menu yang diizinkan yang tampil.
  - [ ] Masuk ke M.10 sebagai `pemilik`: Pastikan `show_menu_configs()` dipanggil dan berfungsi normal.
- [ ] **Verifikasi breadcrumb:**
  - [ ] Dashboard: `"Dashboard"`.
  - [ ] Sub-menu M.1: `"Dashboard > M.1 Transaksi & Kebijakan Harga"`.
  - [ ] Ubah Password: `"Dashboard > Ubah Password"`.
- [ ] **Verifikasi kompatibilitas:**
  - [ ] Jalankan di Windows 11 (PowerShell/Terminal) — pastikan panel `rich` dan karakter Unicode tampil benar.
  - [ ] Pastikan fallback teks polos berfungsi jika `rich` tidak terinstal (`HAS_RICH = False`).
- [ ] **Verifikasi bahwa `cli/menu_configs.py` tetap berfungsi normal** setelah refaktor.
- [ ] **Verifikasi bahwa `get_visible_menus()` yang lama tetap berfungsi** (tidak ada kode lain yang terganggu).

### Fase 8: Finalisasi dan Dokumentasi

- [ ] Pastikan header module di semua file yang dimodifikasi sudah terupdate (Author, Tanggal).
- [ ] Pastikan tidak ada `print()` debugging yang tertinggal (hapus semua debug prints).
- [ ] Pastikan tidak ada import yang tidak terpakai.
- [ ] Pastikan semua `# TODO:` yang terkait navigasi menu utama sudah terselesaikan.
- [ ] Pastikan komentar `# DATA_KOSONG:` ditambahkan jika ada data referensi yang tidak ditemukan.
- [ ] Review terakhir: Baca ulang seluruh kode yang ditulis, pastikan:
  - [ ] Tidak ada variabel global mutable.
  - [ ] Tidak ada class/OOP.
  - [ ] Semua string SQL menggunakan `%s` binding.
  - [ ] Semua input disanitasi.
  - [ ] Semua koneksi database ditutup di `finally`.
  - [ ] Semua password di-input via `getpass`.

---

## 7. File yang Akan Dimodifikasi/Dibuat

| No | Path File | Aksi | Deskripsi Perubahan |
|:--:|:---|:---:|:---|
| 1 | `cli/dashboard.py` | **MODIFY** | Refaktor tampilan dashboard, implementasi sub-menu loop, routing handle_navigation, form ubah password, graceful exit. |
| 2 | `middleware/rbac_guard.py` | **MODIFY** | Tambah fungsi `get_visible_modules()`, `get_module_submenus()`, dan pindahkan `MODULE_NAMES` dari `dashboard.py`. |

> **Catatan:** Tidak ada file baru yang perlu dibuat. Semua perubahan dilakukan pada file yang sudah ada.

---

## 8. Instruksi Tambahan Spesifik CLI Navigation

### 8.1. Penanganan Modul yang Digabung di Satu File

Beberapa modul digabung dalam satu file `cli/menu_*.py` (Ref: R-03 Bab 14):
- `menu_transaksi.py` menangani **M.1** (Transaksi) dan **M.8** (CRM).
- `menu_inventaris.py` menangani **M.2** (Inventaris) dan **M.5** (Antrian).
- `menu_sdm_finansial.py` menangani **M.4** (SDM) dan **M.6** (Keuangan).

Namun di dashboard, **M.1, M.2, M.4, M.5, M.6, dan M.8** tetap ditampilkan sebagai modul terpisah. Routing hanya perlu memanggil fungsi `show_menu_*()` yang sesuai, dan fungsi tersebut di masa depan akan menangani pengelompokan sub-menu internalnya sendiri.

Untuk saat ini di `handle_navigation()`, gunakan pendekatan berikut:
- Jika pengguna memilih Modul M.1 dari dashboard, panggil fungsi `show_menu_transaksi(session_state)`.
- Jika pengguna memilih Modul M.8 dari dashboard, panggil juga fungsi `show_menu_transaksi(session_state)` (karena CRM ditangani oleh file yang sama).
- Sama halnya untuk M.2/M.5 dan M.4/M.6.

Atau, alternatif yang lebih baik: **Implementasikan sub-menu loop langsung di `show_module_submenu()`** di `dashboard.py` tanpa memanggil `show_menu_*()` untuk level modul. Panggil `show_menu_*()` hanya untuk aksi sub-menu individual. Ini lebih konsisten dengan arsitektur navigasi 3-level.

### 8.2. Penanganan Data Kosong

Jika dalam proses implementasi kamu menemukan:
- Fungsi yang disebutkan di referensi tapi tidak ada di kode aktual → Tandai: `# DATA_KOSONG: Fungsi [nama_fungsi] belum ada, perlu diimplementasikan di issue terpisah.`
- Label menu yang tidak konsisten antara referensi dan `MENU_LABELS` → Gunakan data dari `MENU_LABELS` di `rbac_guard.py` sebagai SSoT karena itu yang sudah diimplementasikan di kode aktual.
- Access level yang berbeda antara referensi dan `RBAC_MATRIX` → Gunakan data dari `RBAC_MATRIX` di `rbac_guard.py` sebagai SSoT.

### 8.3. Rich Library Fallback

Seluruh tampilan visual **WAJIB** memiliki fallback jika library `rich` tidak tersedia:
```python
try:
    from rich.console import Console
    from rich.panel import Panel
    _console = Console()
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

# Penggunaan:
if HAS_RICH:
    _console.print(Panel("Header", border_style="bold green"))
else:
    print("═" * 60)
    print("  Header")
    print("═" * 60)
```

### 8.4. Pola Input Loop Standar

Gunakan pola berikut untuk setiap prompt input di menu:
```python
try:
    raw_input = input("Pilih Menu: ")
    pilihan = sanitasi_input_cli(raw_input).strip()
except (EOFError, KeyboardInterrupt):
    # Graceful exit saat Ctrl+C
    graceful_exit(session_state)
    return
```

---

## 9. Ringkasan Checklist Final

Sebelum menandai issue ini sebagai `Done`, pastikan SELURUH item berikut terpenuhi:

- [ ] Semua 8 fase checklist di Bab 6 sudah tercentang `[x]`.
- [ ] `cli/dashboard.py` sudah menampilkan modul terfilter RBAC dengan hotkey numerik.
- [ ] Sub-menu per modul sudah menampilkan daftar sub-menu terfilter RBAC.
- [ ] Tombol `0` berfungsi untuk kembali di setiap level navigasi.
- [ ] Tombol `q` berfungsi untuk graceful exit di setiap level navigasi.
- [ ] `Ctrl+C` menjalankan graceful exit.
- [ ] Ubah Password (UC-044) sudah diimplementasikan dan berfungsi.
- [ ] Breadcrumb ditampilkan di setiap level navigasi.
- [ ] `cli/menu_configs.py` tetap berfungsi normal setelah refaktor.
- [ ] Tidak ada feature lain yang terganggu.
- [ ] Kode sudah bersih, rapi, dan sesuai standar.
- [ ] Tidak ada `# DATA_KOSONG:` yang belum ditindaklanjuti (atau sudah ditandai untuk issue terpisah).

---

## 10. Catatan Komunikasi

Jika selama pengerjaan kamu menemukan:
1. **Inkonsistensi antara dokumen referensi** → Prioritaskan data dari file kode aktual (`rbac_guard.py`, `dashboard.py`) sebagai SSoT, lalu tandai inkonsistensi di komentar kode.
2. **Fungsi yang belum ada** → Jangan membuat fungsi baru di luar cakupan issue ini. Tandai dengan `# TODO: Implementasi di issue [xxx]`.
3. **Bug pada kode existing** → Jangan perbaiki bug yang tidak terkait navigasi. Tandai dengan `# FIXME: [deskripsi bug]`.
4. **Kebutuhan library baru** → Issue ini **TIDAK BOLEH** menambahkan library baru ke `requirements.txt`. Gunakan hanya library yang sudah ada.

---

*Dokumen issue ini disusun oleh Claude Opus 4.6 (Thinking) — Senior System Architect & Strategic Planner.*
*Tanggal: 2026-06-07*
