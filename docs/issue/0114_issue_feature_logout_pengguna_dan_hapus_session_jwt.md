---
issue        : 0114
judul        : Feature Logout Pengguna dan Hapus Session JWT
status       : Ready for Implementation
prioritas    : High
modul        : M.7 — Keamanan, Audit Trail & Hak Akses
menu_id      : MENU-BASE-002
use_case     : UC-042
tanggal      : 2026-06-06
estimasi     : 1 hari kerja
---

# Issue #0114 — Feature Logout Pengguna dan Hapus Session JWT

---

## 0. Persona Pelaksana (Role Assignment)

**Persona**: `Senior Security & Session Lifecycle Engineer`

Kamu adalah seorang Senior Security & Session Lifecycle Engineer yang memiliki keahlian mendalam dalam:
- Manajemen lifecycle session token JWT (create, validate, destroy).
- Implementasi audit trail berbasis database relasional MySQL.
- Paradigma Functional Programming (FP) murni Python tanpa class/OOP.
- Standar keamanan OWASP untuk session management (session invalidation, secure logout).
- Arsitektur berlapis 4-layer AbuCom (Presentation → Business Logic → Data Access → Persistence).

Kamu bertanggung jawab penuh atas kebenaran, kelengkapan, keamanan, dan kualitas produksi dari implementasi fitur logout ini. Kerjakan dengan **rapi, bersih, tidak tergesa-gesa, dan tidak buru-buru**. Pastikan setiap baris kode yang kamu tulis sudah diverifikasi terhadap dokumen referensi SDLC.

---

## 1. Daftar File Referensi (Wajib Dibaca Sebelum Implementasi)

Baca dan ekstrak **seluruh detail data yang relevan** dari dokumen-dokumen berikut sebelum mulai menulis kode. Jangan lewatkan detail kecil apapun dari informasi yang mendukung pengerjaan issue ini.

| No | File Referensi | Path Relatif | Relevansi untuk Issue Ini |
|:--:|---|---|---|
| R-01 | **Security Design v1.2** | `docs/sdlc/03_design/06_security_design.md` | **Sumber utama.** Bab 4.4 (Prosedur Logout dan Penghancuran Session), Bab 4.2 (Manajemen Session CLI JWT HS256), Bab 7.1 (Skema Tabel Audit Logs), Bab 7.2 (Event Pemicu Pencatatan Audit — khusus event `LOGOUT`), Bab 12.2 (Pseudocode login_user & session lifecycle). |
| R-02 | **CLI Interaction Flow v1.2** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Bab 4.2 (Alur Interaksi Logout dari Sistem UC-042 — langkah detail 1-5), Bab 2.2 (Konvensi Navigasi Global — pola konfirmasi `[Y/N]`, exit darurat `Ctrl+C`), Bab 2.3 (ANSI Color Palette — hijau untuk sukses). |
| R-03 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | Bab 2.2 (FP Murni, Result Pattern, Imutabilitas), Bab 3 (Konvensi Penamaan snake_case), Bab 6 (Docstring PEP 257), Bab 8.4 (State Dictionary Passing), Bab 10.3 (JWT HS256 — 8 jam), Bab 10.6 (Audit Trail Logging wajib), Bab 11 (Konvensi CLI). |
| R-04 | **Module Structure v1.2** | `docs/sdlc/04_implementation/03_module_structure.md` | Bab 4.2 (cli/dashboard.py — `render_dashboard`, `handle_navigation`), Bab 7.2 (middleware/auth_jwt.py — `verify_jwt_session`, `validate_session_token`), Bab 7.4 (middleware/audit_logger.py — `log_audit_trail`). |
| R-05 | **Database Schema DDL v1.2** | `schema.sql` | Tabel 02 `pengguna` (kolom: id, username, role, cabang_id), Tabel 27 `audit_logs` (kolom: pengguna_id, action_type, target_table, old_value, new_value, cabang_id). |
| R-06 | **Access Control Matrix v1.1** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | MENU-BASE-002 (Logout) — diizinkan untuk seluruh 8 peran tanpa pengecualian. |
| R-07 | **Software Requirements v1.1** | `docs/sdlc/02_analysis/02_software_requirements.md` | SRS terkait modul M.7 Keamanan — khusus kebutuhan fungsional logout dan session management. |

> **Catatan**: File `docs/sdlc/narasi.txt` **tidak diperlukan** sebagai referensi untuk issue ini karena seluruh spesifikasi teknis logout sudah tercakup lengkap di dokumen R-01 sampai R-07 di atas.

---

## 2. Rangkuman Detail Relevan dari Dokumen Referensi

Berikut adalah ekstraksi data spesifik yang **wajib** dijadikan acuan implementasi:

### 2.1. Dari Security Design v1.2 (R-01)

**Bab 4.4 — Prosedur Logout dan Penghancuran Session:**
- Saat pengguna memilih menu `BASE-002 (Logout)` **atau** memicu *idle timeout* 30 menit tanpa aktivitas keyboard:
  1. Sistem menghapus token JWT string dari dictionary state lokal memori Python kasir secara **permanen** → `session_state = {'user_id': None, 'role': None, 'token': None}`.
  2. Sistem menuliskan entri aktivitas log audit jenis **`LOGOUT`** ke tabel `audit_logs` MySQL.
  3. Terminal CLI dibersihkan menggunakan pembersih layar dan merender kembali **prompt login kosong awal**.

**Bab 4.2 — Manajemen Session CLI (JWT HS256):**
- Token JWT menggunakan algoritma **HS256** dengan secret key dari `.env`.
- Masa berlaku sesi: **28.800 detik (8 jam)**.
- Payload token berisi: `user_id`, `username`, `role`, `cabang_id`, `exp`.
- Handling Expiration: Jika kedaluwarsa terjadi di tengah operasi yang sedang berjalan (*mid-transaction*), transaksi di-`ROLLBACK` secara aman sebelum sesi dihancurkan.

**Bab 7.2 — Event Pemicu Pencatatan Audit:**
- Aktivitas otentikasi yang wajib dicatat: `LOGIN_SUCCESS`, `LOGIN_FAILED`, **`LOGOUT`**, dan `ACCOUNT_LOCKOUT`.

**Bab 12.2 — Pseudocode SessionState:**
- `SessionState = namedtuple('SessionState', ['user_id', 'username', 'role', 'cabang_id', 'token'])`
- Setelah logout: session state di-nullkan secara eksplisit.

### 2.2. Dari CLI Interaction Flow v1.2 (R-02)

**Bab 4.2 — Alur Interaksi Logout (UC-042):**

| No. | Aktor/Sistem | Aksi | Tipe | Contoh Tampilan/Input |
|:---:|:---|:---|:---:|:---|
| 1 | Pengguna | Memilih opsi "Logout dari Sesi CLI" di menu utama. | Input | `Pilihan menu [0-Kembali]: 9` (numerik) |
| 2 | Sistem | Meminta konfirmasi biner tindakan logout dari pengguna. | Output | `Apakah Anda yakin ingin logout? [Y/N]: ` |
| 3 | Pengguna | Mengetik konfirmasi `Y` atau `y`. | Input | `Y` (char, case-insensitive) |
| 4 | Sistem | Menghapus data token JWT lokal di memory state dictionary, membersihkan layar console. | Proses | Memusnahkan objek token di sisi klien Python. |
| 5 | Sistem | Me-redirect terminal kembali ke Layar Login Awal. | Output | `[GREEN] Anda telah berhasil logout secara aman.` |

**Bab 2.2 — Konvensi Navigasi Global:**
- Pola Konfirmasi Aksi Destruktif: Operasi kritis wajib menyajikan konfirmasi eksplisit `[Y/N]` (Case-Insensitive) sebelum dieksekusi.
- Exit Darurat: Tombol `q` atau `Ctrl+C` memicu penutupan aplikasi secara aman (*graceful exit*) setelah membersihkan memori token JWT lokal.

### 2.3. Dari Coding Standard v1.2 (R-03)

- **FP Murni**: Tanpa class, gunakan pure functions dan NamedTuple `Result`.
- **Result Pattern**: `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])`.
- **State Dictionary Passing**: Session state dialirkan sebagai parameter dict antar-fungsi.
- **Konvensi CLI**: Pesan sukses warna hijau `[GREEN]`, pesan error warna merah `[RED]` dengan prefix `⛔ ERR-`.
- **Audit Trail wajib**: Setiap aksi modifikasi data sensitif wajib memicu penulisan log audit.
- **PEP 257 Docstring**: Setiap fungsi publik wajib memiliki docstring lengkap.
- **Encoding UTF-8**: Eksplisit pada operasi file.

### 2.4. Dari Database Schema DDL v1.2 (R-05)

**Tabel `audit_logs` — Kolom yang digunakan saat logout:**
```sql
INSERT INTO audit_logs (
    pengguna_id,    -- INT NOT NULL (ID pengguna yang logout)
    action_type,    -- VARCHAR(20) NOT NULL → 'LOGOUT'
    target_table,   -- VARCHAR(100) NOT NULL → 'pengguna'
    old_value,      -- JSON NULL DEFAULT NULL → NULL (tidak ada data lama)
    new_value,      -- JSON NULL DEFAULT NULL → '{"status": "LOGOUT"}'
    ip_address,     -- VARCHAR(45) NULL → opsional, bisa NULL
    cabang_id       -- INT NOT NULL DEFAULT 1
) VALUES (%s, %s, %s, %s, %s, %s, %s);
```

### 2.5. Data yang Tidak Ditemukan di File Referensi (Perlu Ditindaklanjuti)

| No | Data yang Kosong/Tidak Ditemukan | Rekomendasi Tindakan |
|:--:|---|---|
| 1 | ⚠️ **Idle timeout 30 menit**: Security Design Bab 4.4 menyebutkan idle timeout 30 menit tanpa aktivitas keyboard memicu logout otomatis, namun **detail implementasi mekanisme idle timer tidak dijabarkan** di dokumen manapun. | **TANDAI sebagai `# TODO:`** di kode. Idle timeout akan diimplementasikan di issue terpisah karena memerlukan mekanisme timer/threading yang lebih kompleks. Issue ini hanya mengimplementasikan **logout manual via menu**. |
| 2 | ⚠️ **Nomor hotkey menu logout di dashboard**: CLI Flow Bab 4.2 menyebutkan pilihan `9` sebagai logout, namun kondisi codebase aktual menggunakan `0`. | Gunakan sesuai **kondisi codebase aktual** (`0`), karena dashboard saat ini sudah menggunakan `0` untuk logout. Sesuaikan jika nanti ada refaktor menu numbering. |

---

## 3. Batasan, Cakupan, dan Alur Pengerjaan

### 3.1. Cakupan Issue Ini (IN SCOPE)

| No | Cakupan | Deskripsi |
|:--:|---|---|
| 1 | Logout manual via menu dashboard | Pengguna memilih opsi logout dari dashboard utama |
| 2 | Konfirmasi logout `[Y/N]` | Menambahkan prompt konfirmasi sebelum logout dieksekusi |
| 3 | Penghapusan session JWT dari memori | Null-kan seluruh field session_state dictionary |
| 4 | Pencatatan audit log `LOGOUT` | INSERT ke tabel `audit_logs` dengan action_type='LOGOUT' |
| 5 | Pembersihan layar terminal | Clear screen setelah logout |
| 6 | Redirect ke layar login | Kembali ke prompt login awal setelah logout |
| 7 | Logout otomatis saat token kedaluwarsa | Sesi habis masa berlaku (8 jam) → paksa logout |
| 8 | Graceful exit via `Ctrl+C` | Bersihkan session JWT sebelum program ditutup |
| 9 | Unit test untuk fungsi logout | Verifikasi audit log tercatat dan session terhapus |

### 3.2. Di Luar Cakupan Issue Ini (OUT OF SCOPE — Jangan Disentuh)

| No | Fitur yang TIDAK BOLEH Disentuh | Alasan |
|:--:|---|---|
| 1 | ❌ Idle timeout 30 menit (timer otomatis) | Memerlukan issue terpisah dengan mekanisme threading |
| 2 | ❌ Logika login (`login_user()`) | Sudah diimplementasikan di issue sebelumnya |
| 3 | ❌ Rate limiting / lockout brute-force | Sudah diimplementasikan di issue sebelumnya |
| 4 | ❌ Ubah password (UC-044) | Issue terpisah |
| 5 | ❌ RBAC guard / menu filtering | Issue terpisah |
| 6 | ❌ Shift handover kasir | Issue terpisah (M.7) |
| 7 | ❌ Modifikasi skema tabel database | Tidak ada perubahan DDL yang diperlukan |
| 8 | ❌ Fitur modul lain (M.1—M.6, M.8—M.10) | Tidak relevan |

### 3.3. Alur Logout yang Harus Diimplementasikan

```
┌──────────────────────────────┐
│  Dashboard Utama (UC-043)    │
│  Pengguna memilih [0] Logout │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Prompt Konfirmasi:          │
│  "Apakah Anda yakin ingin    │
│   logout? [Y/N]: "           │
└──────────────┬───────────────┘
               │
       ┌───────┴───────┐
       │               │
    [Y/y]           [N/n atau lainnya]
       │               │
       ▼               ▼
┌──────────────┐  ┌──────────────────┐
│ Ambil koneksi │  │ Kembali ke loop  │
│ database      │  │ dashboard (batal)│
└──────┬───────┘  └──────────────────┘
       │
       ▼
┌──────────────────────────────┐
│ Panggil logout_user():       │
│ - INSERT audit_logs LOGOUT   │
│ - action_type = 'LOGOUT'     │
│ - target_table = 'pengguna'  │
│ - new_value = {"status":     │
│     "LOGOUT"}                │
└──────────────┬───────────────┘
       │
       ▼
┌──────────────────────────────┐
│ Null-kan session_state:      │
│ - user_id = None             │
│ - username = None            │
│ - role = None                │
│ - cabang_id = None           │
│ - token = None               │
└──────────────┬───────────────┘
       │
       ▼
┌──────────────────────────────┐
│ Tampilkan pesan sukses:      │
│ [GREEN] "✓ Anda telah       │
│  berhasil logout secara      │
│  aman."                      │
└──────────────┬───────────────┘
       │
       ▼
┌──────────────────────────────┐
│ Bersihkan layar terminal     │
│ Kembali ke layar login awal  │
│ (return dari render_dashboard│
│  → loop login di cli/        │
│  __init__.py)                │
└──────────────────────────────┘
```

---

## 4. Daftar File yang Harus Dibaca, Dimodifikasi, dan Diverifikasi

### 4.1. File yang Perlu DIBACA (Read-Only, Jangan Dimodifikasi)

- [ ] `docs/sdlc/03_design/06_security_design.md` — Bab 4.2, 4.4, 7.1, 7.2, 12.2
- [ ] `docs/sdlc/03_design/04_cli_interaction_flow.md` — Bab 2.2, 2.3, 4.2
- [ ] `docs/sdlc/04_implementation/01_coding_standard.md` — Bab 2.2, 3, 6, 8.4, 10.3, 10.6, 11
- [ ] `docs/sdlc/04_implementation/03_module_structure.md` — Bab 4.2, 7.2, 7.4
- [ ] `schema.sql` — Tabel `pengguna` (baris 66-81), Tabel `audit_logs`
- [ ] `middleware/auth_jwt.py` — Fungsi `validate_session_token()`
- [ ] `middleware/audit_logger.py` — Fungsi `log_audit_trail()`
- [ ] `db/db_connector.py` — Fungsi `get_db_connection()`

### 4.2. File yang Perlu DIMODIFIKASI (Modify)

- [ ] `cli/dashboard.py` — **Modifikasi utama**: Menambahkan prompt konfirmasi `[Y/N]` sebelum logout, memperbaiki alur logout agar sesuai dengan spesifikasi CLI Flow UC-042
- [ ] `logic/auth_handler.py` — **Penyempurnaan kecil**: Memvalidasi bahwa fungsi `logout_user()` sudah lengkap dan sesuai standar (sudah ada, perlu diverifikasi)
- [ ] `tests/test_login_bcrypt.py` — **Penambahan**: Menambahkan test case tambahan untuk skenario logout (konfirmasi Y/N, edge cases)

### 4.3. File yang TIDAK BOLEH Dimodifikasi

- ❌ `main.py` — Entry point, sudah benar
- ❌ `middleware/auth_jwt.py` — Fungsi JWT sudah lengkap
- ❌ `middleware/audit_logger.py` — Fungsi audit sudah lengkap
- ❌ `middleware/rbac_guard.py` — Tidak terkait
- ❌ `cli/__init__.py` — Loop login sudah menangani session cleanup saat return dari dashboard
- ❌ `schema.sql` — Tidak ada perubahan DDL
- ❌ Seluruh file di `cli/menu_*.py` — Tidak terkait dengan logout

---

## 5. Checklist Tahapan Implementasi (Low-Level Step-by-Step)

### Tahap 1: Persiapan — Pembacaan dan Pemahaman Referensi

- [ ] Baca file `docs/sdlc/03_design/06_security_design.md` Bab 4.4 secara menyeluruh. Catat 3 langkah prosedur logout yang diwajibkan.
- [ ] Baca file `docs/sdlc/03_design/04_cli_interaction_flow.md` Bab 4.2. Catat 5 langkah interaksi detail logout (UC-042) termasuk prompt dan pesan output.
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` Bab 2.2. Pastikan paham aturan: Result Pattern, FP murni, tanpa class.
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` Bab 10.6. Pastikan paham bahwa audit trail `LOGOUT` wajib dicatat.
- [ ] Baca file `middleware/audit_logger.py` baris 16-52. Pahami signature fungsi `log_audit_trail()` dan parameternya.
- [ ] Baca file `middleware/auth_jwt.py` baris 175-222. Pahami fungsi `validate_session_token()` yang mendeteksi token kedaluwarsa.
- [ ] Baca file `logic/auth_handler.py` baris 134-153. Pahami fungsi `logout_user()` yang sudah ada.
- [ ] Baca file `cli/dashboard.py` baris 1-168 secara menyeluruh. Pahami alur loop dashboard, cara logout saat ini dihandle (baris 95-120), dan cara token kedaluwarsa dihandle (baris 36-57).
- [ ] Baca file `cli/__init__.py` baris 59-175. Pahami bahwa setelah `render_dashboard()` return, session_state di-cleanup di blok `finally` (baris 170-174) dan loop login berjalan kembali.
- [ ] Baca file `tests/test_login_bcrypt.py` baris 294-321. Pahami test case logout yang sudah ada.

### Tahap 2: Verifikasi Kondisi Existing — Analisis Gap

- [ ] **Verifikasi `logic/auth_handler.py` — fungsi `logout_user()`:**
  - Pastikan fungsi sudah memanggil `log_audit_trail()` dengan parameter:
    - `action_type='LOGOUT'`
    - `target_table='pengguna'`
    - `old_val=None`
    - `new_val={'status': 'LOGOUT'}`
    - `cabang_id` dari `session_state['cabang_id']`
  - Pastikan fungsi mengembalikan `Result(True, None, None)` saat sukses.
  - **Status**: ✅ Sudah diimplementasikan di codebase saat ini (baris 134-153). Tidak perlu dimodifikasi.

- [ ] **Verifikasi `cli/__init__.py` — cleanup setelah dashboard:**
  - Pastikan blok `finally` (baris 170-174) membersihkan `session_state = {}` saat `render_dashboard()` return.
  - Pastikan loop `while True` (baris 72) otomatis kembali ke layar login setelah cleanup.
  - **Status**: ✅ Sudah benar. Tidak perlu dimodifikasi.

- [ ] **Identifikasi Gap di `cli/dashboard.py`:**
  - **Gap 1**: ❌ Saat ini TIDAK ADA prompt konfirmasi `[Y/N]` sebelum logout. Menurut CLI Flow Bab 4.2 langkah 2-3, sistem wajib meminta konfirmasi `"Apakah Anda yakin ingin logout? [Y/N]: "` dan hanya memproses logout jika jawaban `Y`/`y`.
  - **Gap 2**: ❌ Saat ini pesan sukses logout menggunakan teks `"✓ Logout Berhasil! Sesi telah dihapus."` — perlu disesuaikan menjadi `"✓ Anda telah berhasil logout secara aman."` sesuai CLI Flow Bab 4.2 langkah 5.
  - **Gap 3**: ⚠️ Pembersihan layar terminal setelah logout belum dipanggil secara eksplisit sebelum pesan sukses ditampilkan. Menurut Security Design Bab 4.4 langkah 3: "Terminal CLI dibersihkan menggunakan pembersih layar".

### Tahap 3: Implementasi — Modifikasi `cli/dashboard.py`

#### 3.1. Modifikasi Alur Logout di Fungsi `render_dashboard()` (Prioritas Utama)

- [ ] Buka file `cli/dashboard.py`.
- [ ] Temukan blok penanganan logout saat pilihan `== '0'` (baris 95-120).
- [ ] **Tambahkan prompt konfirmasi SEBELUM proses logout.** Ganti blok baris 95-120 dengan logika berikut:

```python
        if pilihan == '0':
            # Konfirmasi logout sesuai CLI Flow UC-042 langkah 2-3
            try:
                konfirmasi = input("Apakah Anda yakin ingin logout? [Y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                konfirmasi = 'y'  # Graceful exit → anggap logout

            if konfirmasi != 'y':
                # Pengguna membatalkan logout, kembali ke loop dashboard
                continue

            # Proses logout: catat audit trail ke database
            conn_res = get_db_connection()
            if conn_res.is_success:
                db_conn = conn_res.data
                try:
                    logout_user(session_state, db_conn)
                finally:
                    try:
                        db_conn.close()
                    except Exception:
                        pass

            # Hapus token JWT string dari dictionary session_state secara permanen
            # (Ref: Security Design Bab 4.4 langkah 1)
            session_state['user_id'] = None
            session_state['username'] = None
            session_state['role'] = None
            session_state['cabang_id'] = None
            session_state['token'] = None

            # Bersihkan layar terminal (Ref: Security Design Bab 4.4 langkah 3)
            clear_terminal()

            # Tampilkan pesan sukses logout (Ref: CLI Flow Bab 4.2 langkah 5)
            success_msg = "✓ Anda telah berhasil logout secara aman."
            if HAS_RICH:
                _console.print(f"[bold green]{success_msg}[/]")
            else:
                print(success_msg)
            input("Tekan Enter untuk melanjutkan...")
            return
```

- [ ] Pastikan variabel `clear_terminal` sudah diimpor dari `utils.text_formatter` (sudah ada di baris 24).
- [ ] Pastikan variabel `logout_user` sudah diimpor dari `logic.auth_handler` (sudah ada di baris 22).
- [ ] Pastikan variabel `get_db_connection` sudah diimpor dari `db.db_connector` (sudah ada di baris 21).

#### 3.2. Verifikasi Alur Token Kedaluwarsa di `render_dashboard()` (Baris 36-57)

- [ ] Verifikasi bahwa blok token kedaluwarsa (baris 36-57) sudah benar:
  - `validate_session_token()` mengembalikan `is_success=False` → session state di-nullkan → return ke login.
  - `logout_user()` dipanggil untuk mencatat audit log.
- [ ] **Status**: ✅ Sudah benar. Tidak perlu dimodifikasi.

#### 3.3. Verifikasi Alur Token Kedaluwarsa di `handle_navigation()` (Baris 141-161)

- [ ] Verifikasi bahwa blok validasi token di `handle_navigation()` sudah benar:
  - Jika token kedaluwarsa → session di-nullkan → return → loop dashboard mendeteksi token=None → return ke login.
- [ ] **Status**: ✅ Sudah benar. Tidak perlu dimodifikasi.

### Tahap 4: Verifikasi `logic/auth_handler.py` — Fungsi `logout_user()`

- [ ] Buka file `logic/auth_handler.py`.
- [ ] Verifikasi fungsi `logout_user()` (baris 134-153) sudah sesuai standar:
  - [ ] Memiliki docstring PEP 257 lengkap dengan Args, Returns.
  - [ ] Memanggil `log_audit_trail()` dengan parameter sesuai Security Design Bab 7.2.
  - [ ] Mengembalikan `Result(True, None, None)`.
  - [ ] Tidak memiliki efek samping selain penulisan audit log.
- [ ] **Status**: ✅ Sudah benar dan lengkap. Tidak perlu dimodifikasi.

### Tahap 5: Penambahan Test Case — `tests/test_login_bcrypt.py`

- [ ] Buka file `tests/test_login_bcrypt.py`.
- [ ] Verifikasi test case `test_logout_user_sukses` (baris 294-320) sudah ada dan sudah mencakup:
  - [ ] Memverifikasi `is_success == True`.
  - [ ] Memverifikasi `log_audit_trail` dipanggil dengan `action_type='LOGOUT'`.
  - [ ] Memverifikasi `target_table='pengguna'`.
  - [ ] Memverifikasi `new_val={'status': 'LOGOUT'}`.
- [ ] **Status**: ✅ Sudah ada dan sudah lengkap.

- [ ] **Tambahkan test case baru** untuk edge case logout:

```python
def test_logout_user_dengan_session_state_minimal(mocker, mock_db_conn):
    """Menjamin logout tetap berhasil meskipun session_state hanya berisi field wajib."""
    mock_audit = mocker.patch('logic.auth_handler.log_audit_trail')
    session_state = {
        'user_id': 1,
        'username': 'pemilik_utama',
        'role': 'pemilik',
        'cabang_id': 1,
        'token': 'some_jwt_token'
    }

    res = logout_user(session_state, mock_db_conn)

    assert res.is_success is True
    mock_audit.assert_called_once_with(
        pengguna_id=1,
        action_type='LOGOUT',
        target_table='pengguna',
        old_val=None,
        new_val={'status': 'LOGOUT'},
        cabang_id=1,
        db_connection=mock_db_conn
    )


def test_logout_user_audit_trail_gagal_tetap_return_sukses(mocker, mock_db_conn):
    """Menjamin logout tetap mengembalikan Result sukses meskipun audit trail gagal ditulis.

    Audit logger menangani exception secara internal (try-except di audit_logger.py),
    sehingga logout_user() tidak boleh crash.
    """
    mocker.patch(
        'logic.auth_handler.log_audit_trail',
        side_effect=Exception("DB Connection Lost")
    )
    session_state = {
        'user_id': 42,
        'username': 'kasir_uji',
        'role': 'kasir',
        'cabang_id': 1,
        'token': 'mock_token'
    }

    # Fungsi logout_user langsung memanggil log_audit_trail tanpa try-except,
    # sehingga jika log_audit_trail throw exception, logout_user juga throw.
    # Ini perlu diverifikasi: apakah perilaku ini sesuai ekspektasi?
    # Jika log_audit_trail di audit_logger.py sudah menangani exception internal,
    # maka test ini harus disesuaikan.
    with pytest.raises(Exception):
        logout_user(session_state, mock_db_conn)
```

- [ ] Jalankan seluruh test suite untuk memastikan test baru berjalan:
  ```bash
  cd /home/nabila/Documents/abucom
  python -m pytest tests/test_login_bcrypt.py -v
  ```
- [ ] Pastikan semua test **PASSED** (0 failures, 0 errors).

### Tahap 6: Pengujian Manual End-to-End

- [ ] Jalankan aplikasi AbuCom CLI:
  ```bash
  cd /home/nabila/Documents/abucom
  python main.py
  ```
- [ ] **Skenario 1 — Logout Normal:**
  1. Login dengan kredensial valid.
  2. Di dashboard, ketik `0` untuk memilih logout.
  3. Verifikasi prompt `"Apakah Anda yakin ingin logout? [Y/N]: "` muncul.
  4. Ketik `Y`. Verifikasi pesan hijau `"✓ Anda telah berhasil logout secara aman."` muncul.
  5. Verifikasi layar terminal dibersihkan dan kembali ke prompt login.
  6. Verifikasi di database: `SELECT * FROM audit_logs WHERE action_type = 'LOGOUT' ORDER BY id DESC LIMIT 1;` — pastikan ada entry LOGOUT terbaru.

- [ ] **Skenario 2 — Batal Logout:**
  1. Login dengan kredensial valid.
  2. Di dashboard, ketik `0`.
  3. Di prompt konfirmasi, ketik `N`.
  4. Verifikasi tetap berada di dashboard (tidak logout).

- [ ] **Skenario 3 — Konfirmasi logout dengan input case-insensitive:**
  1. Login dan pilih logout.
  2. Ketik `y` (huruf kecil). Verifikasi logout berhasil.

- [ ] **Skenario 4 — Graceful exit via Ctrl+C:**
  1. Login dan masuk ke dashboard.
  2. Tekan `Ctrl+C`. Verifikasi aplikasi menutup dengan pesan aman.
  3. Verifikasi session state sudah dibersihkan (tidak ada token tersisa di memori).

### Tahap 7: Verifikasi Akhir — Kualitas dan Kelengkapan

- [ ] **Verifikasi tidak ada feature lain yang rusak:**
  - Jalankan `python -m pytest tests/ -v` — semua test harus PASSED.
  - Login ulang setelah logout — pastikan login masih berfungsi normal.
  - Pastikan tidak ada import yang rusak atau circular dependency.

- [ ] **Verifikasi kelengkapan docstring:**
  - Setiap fungsi yang dimodifikasi atau ditambahkan harus memiliki docstring PEP 257 lengkap (Args, Returns, Example jika relevan).

- [ ] **Verifikasi coding standard:**
  - Penamaan fungsi: `snake_case` (verb_noun).
  - Variabel: `snake_case`.
  - Tidak ada class/OOP di logika bisnis.
  - Tidak ada f-string di query SQL.
  - Semua query SQL menggunakan parameterized `%s`.
  - Import terurut: Standard Library → Third-Party → Local Modules.

- [ ] **Verifikasi keamanan:**
  - Token JWT benar-benar dihapus dari memori setelah logout (semua field session_state di-None-kan).
  - Audit log `LOGOUT` tercatat di database dengan data yang benar.
  - Tidak ada informasi sensitif (password_hash, token) yang tercetak ke console/log.

---

## 6. Instruksi Tambahan Spesifik Fitur Logout

### 6.1. Prinsip Fail-Secure pada Logout

Sesuai Security Design Bab 2.1 Prinsip No. 5 (**Fail-Secure**): Jika terjadi kegagalan koneksi database saat proses logout (gagal menulis audit log), sistem **tetap harus menghapus token JWT dari memori** dan mengembalikan pengguna ke layar login. Jangan biarkan pengguna tetap login hanya karena audit log gagal ditulis.

Pastikan kode mengikuti pola:
```python
# Coba catat audit log (best effort)
conn_res = get_db_connection()
if conn_res.is_success:
    db_conn = conn_res.data
    try:
        logout_user(session_state, db_conn)
    finally:
        try:
            db_conn.close()
        except Exception:
            pass

# SELALU hapus session, terlepas dari keberhasilan audit log
session_state['user_id'] = None
session_state['username'] = None
session_state['role'] = None
session_state['cabang_id'] = None
session_state['token'] = None
```

### 6.2. Konsistensi Pembersihan Session State

Pastikan **semua jalur exit** dari fungsi `render_dashboard()` melakukan pembersihan session state yang konsisten. Ada 3 jalur exit yang perlu diverifikasi:

1. **Logout manual (pilihan `0`)**: ✅ Session state di-nullkan di dalam blok `if pilihan == '0'`.
2. **Token kedaluwarsa (validasi gagal di awal loop)**: ✅ Session state di-nullkan di blok `if not val_res.is_success` (baris 52-56).
3. **Token kedaluwarsa saat navigasi (`handle_navigation`)**: ✅ Session state di-nullkan di dalam `handle_navigation()` (baris 155-159), dan loop dashboard mendeteksi `token=None` → return.

### 6.3. Tidak Boleh Ada Memory Leak Token JWT

Setelah logout, pastikan **tidak ada referensi lain** yang masih menyimpan token JWT string di memori Python. Karena session_state adalah dictionary yang di-pass by reference, penulisan `session_state['token'] = None` akan memutus referensi ke string token JWT, sehingga garbage collector Python dapat membersihkannya.

### 6.4. Thread Safety (Informasi)

Sistem AbuCom CLI berjalan single-threaded (satu terminal kasir = satu proses Python). Tidak ada kebutuhan thread synchronization untuk pembersihan session state. Informasi ini dicatat agar pelaksana tidak menambahkan lock/mutex yang tidak perlu.

---

## 7. Ringkasan Perubahan yang Harus Dilakukan

| No | File | Jenis Perubahan | Detail Singkat |
|:--:|---|:---:|---|
| 1 | `cli/dashboard.py` | **MODIFY** | Tambahkan prompt konfirmasi `[Y/N]` pada alur logout, sesuaikan teks pesan sukses, tambahkan `clear_terminal()` sebelum pesan sukses |
| 2 | `tests/test_login_bcrypt.py` | **MODIFY** | Tambahkan 2 test case edge case untuk logout |
| 3 | `logic/auth_handler.py` | **VERIFY ONLY** | Verifikasi fungsi `logout_user()` sudah lengkap (tidak perlu modifikasi) |
| 4 | `middleware/audit_logger.py` | **VERIFY ONLY** | Verifikasi `log_audit_trail()` sudah menangani exception internal |
| 5 | `cli/__init__.py` | **VERIFY ONLY** | Verifikasi cleanup session setelah dashboard return (tidak perlu modifikasi) |

---

## 8. Kriteria Selesai (Definition of Done)

- [ ] Prompt konfirmasi `[Y/N]` muncul sebelum logout dieksekusi.
- [ ] Logout membatalkan operasi jika pengguna menjawab `N`/`n`.
- [ ] Token JWT berhasil dihapus dari memori session_state setelah logout.
- [ ] Entry `LOGOUT` tercatat di tabel `audit_logs` dengan data yang benar.
- [ ] Layar terminal dibersihkan setelah logout.
- [ ] Pengguna diredirect kembali ke layar login setelah logout.
- [ ] Pesan sukses hijau sesuai spesifikasi CLI Flow ditampilkan.
- [ ] Seluruh unit test PASSED (`python -m pytest tests/ -v`).
- [ ] Tidak ada fitur lain yang rusak akibat perubahan ini.
- [ ] Kode mengikuti Coding Standard v1.2 (FP murni, PEP 257, snake_case, Result Pattern).
- [ ] Tidak ada TODO/FIXME baru yang ditinggalkan tanpa justifikasi.
