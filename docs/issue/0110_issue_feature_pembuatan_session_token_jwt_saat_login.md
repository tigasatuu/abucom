---
issue      : "#0110"
judul      : Feature Pembuatan Session Token JWT Saat Login
prioritas  : Tinggi
status     : Backlog
tanggal    : 2026-06-06
penyusun   : Claude Opus 4.6 (Thinking) — Strategi Sistem & Keamanan
pelaksana  : Junior Programmer / LLM Model AI (Gemini 3.1 Pro Low / GPT-OSS 120B)
---

# Issue #0110 — Feature Pembuatan Session Token JWT Saat Login

---

## 1. Persona Pelaksana

**Persona yang WAJIB diadopsi oleh pelaksana issue ini:**

> **Kamu adalah Senior Security Engineer & Python Functional Programming Specialist** yang berpengalaman dalam implementasi otentikasi stateless berbasis JWT (JSON Web Token) pada aplikasi CLI Python. Kamu memahami prinsip Defense in Depth, Fail-Secure, dan OWASP Authentication Best Practices. Kamu menulis kode yang bersih, fungsional murni (tanpa class/OOP), menggunakan NamedTuple imutabel, Result pattern, parameterized queries, dan selalu mematuhi standar coding AbuCom (PEP 8, PEP 257, PEP 484 type hints). Kamu sangat teliti terhadap detail keamanan: secret key dari `.env`, algoritma HS256, masa aktif 8 jam, penanganan `ExpiredSignatureError`, dan pencatatan audit trail untuk setiap event otentikasi.

---

## 2. Informasi Konteks Issue

### 2.1. Deskripsi Singkat
Issue ini mencakup **verifikasi kelengkapan, penyempurnaan, dan integrasi penuh** mekanisme pembuatan session token JWT (JSON Web Token) yang dihasilkan saat proses login berhasil. Token JWT ini berfungsi sebagai bukti otentikasi stateless yang melekat pada `session_state` pengguna aktif dan diverifikasi ulang pada setiap perpindahan menu CLI.

### 2.2. Latar Belakang
Saat ini, sistem AbuCom sudah memiliki sebagian implementasi JWT:
- File `middleware/auth_jwt.py` sudah memiliki fungsi `create_jwt_session()` dan `verify_jwt_session()`.
- File `logic/auth_handler.py` sudah memanggil `create_jwt_session()` dalam alur `login_user()` dan menyimpan token ke dalam `session_state` dict.

**Namun, terdapat celah kritis yang belum terselesaikan:**
1. **Validasi JWT di setiap akses menu** — `verify_jwt_session()` belum dipanggil di `cli/dashboard.py` atau navigasi menu lainnya sebelum menjalankan aksi menu.
2. **Penanganan `ExpiredSignatureError` mid-navigation** — Jika token kadaluwarsa saat pengguna sedang di dalam menu, sistem belum memaksa logout dan redirect ke login.
3. **Integrasi logout** — Fungsi `logout_user()` di `logic/auth_handler.py` mencatat audit trail, tetapi CLI belum memanggil fungsi ini dan belum menghancurkan `session_state`.
4. **Session guard terpusat** — Belum ada fungsi guard terpusat yang memvalidasi token JWT sebelum setiap operasi menu.

### 2.3. Tujuan Akhir
Setelah issue ini selesai dikerjakan:
- Token JWT diterbitkan saat login berhasil dan disimpan di `session_state['token']` ✅ (sudah ada)
- Setiap kali pengguna mengakses/berpindah menu, token divalidasi melalui `verify_jwt_session()` ✅ (harus dibuat)
- Jika token kadaluwarsa/invalid, sesi dihancurkan dan pengguna dipaksa kembali ke layar login ✅ (harus dibuat)
- Logout secara eksplisit menghancurkan `session_state` dan mencatat audit trail ✅ (harus diintegrasikan)
- Semua unit test terkait JWT session berjalan hijau ✅ (harus dibuat)

---

## 3. Dokumen Referensi

### 3.1. File Referensi yang WAJIB Dibaca

Berikut adalah daftar file referensi yang **WAJIB** dibaca dan diekstrak informasinya sebelum memulai pengerjaan:

| No | File Referensi | Path Relatif | Alasan Relevansi |
|:--:|---|---|---|
| 1 | **Security Design v1.2** | `docs/sdlc/03_design/06_security_design.md` | **Referensi utama.** Bab 4.2 (JWT HS256), Bab 4.4 (Prosedur Logout), Bab 9.1 (Sequence Diagram Login), Bab 12.2 (Pseudocode JWT). |
| 2 | **Module Structure v1.2** | `docs/sdlc/04_implementation/03_module_structure.md` | Bab 7.2 (spesifikasi `middleware/auth_jwt.py`), signature fungsi `create_jwt_session`, `verify_jwt_session`. |
| 3 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | Bab 10.3 (aturan JWT HS256), Bab 2.2 (FP murni, Result pattern), Bab 8.4 (State Dict Passing). |
| 4 | **Tech Stack Decision v1.1** | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Parameter bcrypt cost 12, JWT HS256, `pyjwt==2.8.0`, `.env` key. |
| 5 | **CLI Interaction Flow v1.1** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur navigasi menu, logout (MENU-BASE-002), session handling. |

### 3.2. File Kode Existing yang WAJIB Dibaca

| No | File Kode | Path | Status Saat Ini |
|:--:|---|---|---|
| 1 | `middleware/auth_jwt.py` | `middleware/auth_jwt.py` | ✅ Sudah ada `create_jwt_session()`, `verify_jwt_session()`, `hash_password()`, `verify_password()`. |
| 2 | `logic/auth_handler.py` | `logic/auth_handler.py` | ✅ Sudah ada `login_user()` yang memanggil `create_jwt_session()`, `logout_user()` yang mencatat audit trail. |
| 3 | `cli/__init__.py` | `cli/__init__.py` | ⚠️ Sudah ada alur login tetapi BELUM ada validasi JWT di setiap iterasi menu. |
| 4 | `cli/dashboard.py` | `cli/dashboard.py` | ⚠️ Placeholder kosong. BELUM ada verifikasi JWT sebelum render dashboard. |
| 5 | `middleware/rbac_guard.py` | `middleware/rbac_guard.py` | ⚠️ RBAC guard belum memvalidasi token JWT. Hanya cek `role` dari `session_state`. |
| 6 | `middleware/audit_logger.py` | `middleware/audit_logger.py` | ✅ Sudah berfungsi. Digunakan oleh `login_user()` dan `logout_user()`. |
| 7 | `config/settings.py` | `config/settings.py` | ✅ Sudah memuat `jwt_secret_key` dan `jwt_lifetime_seconds` dari `.env`. |
| 8 | `db/pengguna_repository.py` | `db/pengguna_repository.py` | ✅ Sudah ada fungsi CRUD pengguna. |
| 9 | `.env` | `.env` | ✅ Sudah ada `JWT_SECRET_KEY` dan `JWT_LIFETIME_SECONDS=28800`. |
| 10 | `requirements.txt` | `requirements.txt` | ✅ Sudah ada `pyjwt==2.8.0`. |

### 3.3. File Referensi yang TIDAK Dibutuhkan
- `docs/sdlc/narasi.txt` — Tidak diperlukan. Konteks bisnis umum sudah tercakup di dokumen SDLC teknis di atas.

---

## 4. Rangkuman Data Relevan dari Dokumen Referensi

### 4.1. Spesifikasi JWT dari Security Design (Bab 4.2)
- **Algoritma Tanda Tangan**: `HS256` (HMAC-SHA256).
- **Secret Key**: Minimum 32 karakter heksadesimal dari variabel `.env` → `JWT_SECRET_KEY`.
- **Payload Token** (wajib mengandung 5 klaim):
  ```json
  {
    "user_id": 1,
    "username": "kasir_andi",
    "role": "kasir",
    "cabang_id": 1,
    "exp": 1779928800
  }
  ```
- **Masa Berlaku Sesi**: `28800 detik` (8 jam = 1 shift kerja).
- **Handling Expiration**: Setiap kali menu CLI dipicu, validator sesi menangkap `jwt.ExpiredSignatureError`. Jika terpicu:
  1. Hapus token JWT dari memori lokal (variabel `session_state`).
  2. Putus alur program.
  3. Paksa terminal kembali ke layar login dengan kode `ERR-SESSION-002`.
  4. Jika kadaluwarsa terjadi di tengah transaksi (*mid-transaction*), transaksi dibatalkan (*rollback*) secara aman.

### 4.2. Prosedur Logout dari Security Design (Bab 4.4)
Saat pengguna memilih menu `BASE-002 (Logout)`:
1. Hapus token JWT string dari dictionary `session_state` → `{'user_id': None, 'role': None, 'token': None}`.
2. Tulis entri audit log jenis `LOGOUT` ke tabel `audit_logs`.
3. Bersihkan layar terminal dan render kembali prompt login kosong.

### 4.3. Kode Error Relevan (Security Design Bab 10.2)
| Kode Error | Pesan | Pemicu |
|---|---|---|
| `ERR-SESSION-001` | `Sesi login tidak ditemukan. Harap login terlebih dahulu!` | Akses menu CLI tanpa session JWT aktif. |
| `ERR-SESSION-002` | `Sesi login tidak sah/rusak. Harap login kembali!` | Token signature JWT tidak cocok atau kadaluwarsa. |

### 4.4. Signature Fungsi dari Module Structure (Bab 7.2)
```python
# middleware/auth_jwt.py
def create_jwt_session(user_id: int, role: str, cabang_id: int) -> str:
    """Membuat token session JWT HS256 masa aktif 8 jam."""

def verify_jwt_session(token: str) -> dict | None:
    """Validasi token JWT, mengembalikan None jika kadaluwarsa."""
```
**Catatan:** Implementasi aktual di `middleware/auth_jwt.py` sudah menambahkan parameter `username` pada `create_jwt_session()`. Ini sudah sesuai dengan payload JWT yang diharapkan.

### 4.5. State Dictionary Passing (Coding Standard Bab 8.4)
```python
session_state = {
    'user_id': 3,
    'username': 'kasir_andi',
    'role': 'kasir',
    'token': 'jwt_string_token',
    'cabang_id': 1
}
```

### 4.6. Audit Trail Events Terkait JWT (Security Design Bab 7.2)
Event yang WAJIB memicu pencatatan audit:
- `LOGIN_SUCCESS` — Saat token JWT berhasil diterbitkan.
- `LOGIN_FAILED` — Saat password salah.
- `ACCOUNT_LOCKOUT` — Saat akun dikunci (5x gagal berturut-turut).
- `LOGOUT` — Saat pengguna logout eksplisit atau session kadaluwarsa.

---

## 5. Batasan, Cakupan, dan Alur Pengerjaan

### 5.1. Batasan (Scope Boundaries)

**DALAM cakupan issue ini:**
- [x] Verifikasi dan penyempurnaan `create_jwt_session()` di `middleware/auth_jwt.py`.
- [x] Verifikasi dan penyempurnaan `verify_jwt_session()` di `middleware/auth_jwt.py`.
- [x] Pembuatan fungsi session guard terpusat yang memvalidasi JWT sebelum aksi menu.
- [x] Integrasi session guard ke dalam alur navigasi `cli/__init__.py` dan `cli/dashboard.py`.
- [x] Integrasi logout yang menghancurkan `session_state` dan kembali ke login.
- [x] Penanganan `ExpiredSignatureError` di level navigasi menu.
- [x] Pembuatan unit test untuk seluruh fungsi JWT yang baru/diubah.

**DI LUAR cakupan issue ini (JANGAN DIKERJAKAN):**
- ❌ Implementasi isi dashboard per role (M.1 — M.10) — itu issue terpisah.
- ❌ Implementasi RBAC guard decorator lengkap (44 use case) — itu issue terpisah.
- ❌ Implementasi idle timeout 30 menit — itu enhancement terpisah.
- ❌ Modifikasi tabel database `pengguna` atau `audit_logs` — skema sudah final.
- ❌ Modifikasi `config/settings.py` — sudah final dan teruji.
- ❌ Modifikasi `db/pengguna_repository.py` — sudah final dan teruji.
- ❌ Modifikasi `middleware/audit_logger.py` — sudah final dan teruji.

### 5.2. Alur Pengerjaan (Execution Flow)

```
[TAHAP 1] Pembacaan & Pemahaman Referensi
        ↓
[TAHAP 2] Audit Kode Existing
        ↓
[TAHAP 3] Penyempurnaan middleware/auth_jwt.py
        ↓
[TAHAP 4] Pembuatan Session Guard Terpusat
        ↓
[TAHAP 5] Integrasi ke CLI (cli/__init__.py & cli/dashboard.py)
        ↓
[TAHAP 6] Penulisan Unit Test
        ↓
[TAHAP 7] Verifikasi Akhir & Validasi
```

---

## 6. Instruksi Keamanan Feature Lain

> **PERINGATAN KRITIS:** Pastikan pengerjaan issue ini **TIDAK** menyentuh atau merusak feature lain yang sudah berjalan.

### 6.1. File yang TIDAK BOLEH Diubah
- `config/settings.py` — Sudah final, teruji di `tests/test_settings.py` (85KB test).
- `db/pengguna_repository.py` — Sudah final, teruji di `tests/test_registrasi_pengguna.py`.
- `db/db_connector.py` — Sudah final, teruji di `tests/test_db_connector.py` dan `tests/test_unit_db_connector.py`.
- `db/schema_initializer.py` — Sudah final.
- `db/seed_data.py` — Sudah final.
- `db/config_cache.py` — Sudah final.
- `middleware/audit_logger.py` — Sudah final.
- `main.py` — Tidak perlu diubah untuk issue ini.
- `requirements.txt` — Sudah memiliki `pyjwt==2.8.0`.
- `.env` — Sudah memiliki `JWT_SECRET_KEY` dan `JWT_LIFETIME_SECONDS`.

### 6.2. File yang BOLEH Diubah (dengan berhati-hati)
- `middleware/auth_jwt.py` — Boleh ditambahkan fungsi baru, JANGAN ubah signature fungsi yang sudah ada.
- `middleware/rbac_guard.py` — Boleh ditambahkan validasi JWT, JANGAN ubah `RBAC_MATRIX` yang sudah ada.
- `logic/auth_handler.py` — Boleh ditambahkan fungsi baru, JANGAN ubah `login_user()` dan `logout_user()` yang sudah ada dan teruji.
- `cli/__init__.py` — Boleh dimodifikasi alur navigasi, JANGAN hapus logika login yang sudah berfungsi.
- `cli/dashboard.py` — Boleh diimplementasikan penuh (saat ini placeholder).

### 6.3. Prosedur Verifikasi Non-Breaking
Setelah selesai, jalankan seluruh test suite yang sudah ada untuk memastikan tidak ada regresi:
```bash
python -m pytest tests/ -v --tb=short
```
Semua test yang sebelumnya hijau **WAJIB** tetap hijau.

---

## 7. Instruksi Kualitas dan Kedisiplinan Pengerjaan

> **KAIDAH EMAS:** Kerjakan dengan **rapi, bersih, tidak tergesa-gesa, dan tidak buru-buru**. Setiap baris kode yang ditulis harus memenuhi standar Coding Standard v1.2 tanpa pengecualian.

### 7.1. Standar Kualitas Kode
- [ ] Setiap fungsi baru WAJIB memiliki docstring PEP 257 Google Style lengkap (Args, Returns, Example).
- [ ] Setiap fungsi baru WAJIB memiliki type hints PEP 484 lengkap pada parameter dan return value.
- [ ] Setiap file yang dimodifikasi WAJIB memiliki header module docstring yang diperbarui.
- [ ] DILARANG keras menggunakan class/OOP — gunakan fungsi murni (pure functions).
- [ ] Gunakan `NamedTuple` `Result` pattern untuk return value fungsi bisnis.
- [ ] Urutan import: Standard Library → Third-Party → Local Modules.
- [ ] Gunakan single quote (`'`) untuk string internal, double quote (`"`) untuk display CLI.
- [ ] Batas panjang baris maksimum 120 karakter.
- [ ] Indentasi 4 spasi, DILARANG menggunakan Tab.

### 7.2. Standar Keamanan Kode
- [ ] Secret key JWT WAJIB dimuat dari `.env` via `config/settings.py`, DILARANG di-hardcode.
- [ ] DILARANG menggunakan f-string untuk menyusun query SQL.
- [ ] Semua query ke database WAJIB menggunakan parameterized queries (`%s`).
- [ ] Penanganan error WAJIB menggunakan Result pattern, BUKAN exception yang tidak terkontrol.

### 7.3. Kelengkapan yang WAJIB Dipenuhi
Agar issue ini tidak dipertanyakan dan tidak menghambat feature lain:
- [ ] Semua fungsi JWT (`create`, `verify`, `guard`) telah diimplementasikan dan diuji.
- [ ] Integrasi ke CLI telah berfungsi end-to-end (login → token → dashboard → validasi → logout/expired).
- [ ] Unit test mencakup minimal 90% code coverage untuk kode JWT baru.
- [ ] Semua kode error (`ERR-SESSION-001`, `ERR-SESSION-002`) telah diimplementasikan sesuai katalog.
- [ ] Semua test suite existing tetap hijau (zero regression).

---

## 8. Penanganan Data Kosong / Data Tidak Lengkap

Jika ada data yang kosong atau tidak ditemukan dalam file referensi, **tandai dengan komentar berikut** di dalam kode:

```python
# [DATA-KOSONG] Deskripsi data yang hilang. Perlu konfirmasi dari pemilik proyek.
```

**Data kosong yang sudah teridentifikasi saat penulisan issue ini:**
1. **`ip_address` pada `audit_logs`**: Pseudocode di Security Design Bab 12.2 menggunakan hardcode `'192.168.1.10'`. Implementasi aktual di `middleware/audit_logger.py` TIDAK mengirim `ip_address` (kolom di-skip). Ini sudah benar karena `ip_address` di DDL memiliki `NULL DEFAULT NULL`. **Tidak perlu ditindaklanjuti.**
2. **Idle timeout 30 menit**: Disebutkan di Security Design Bab 4.4, tetapi BELUM ada spesifikasi detail implementasinya. **Ditandai sebagai enhancement terpisah, BUKAN bagian dari issue ini.**

---

## 9. Instruksi Tambahan Spesifik JWT

### 9.1. Kekhasan JWT yang Harus Diperhatikan
- **Stateless**: JWT tidak disimpan di server/database. Validasi dilakukan murni berdasarkan tanda tangan kriptografis.
- **Timezone-aware**: Gunakan `datetime.datetime.now(datetime.timezone.utc)` untuk menghindari bug timezone saat perbandingan waktu kadaluwarsa (`exp` claim).
- **Truncation bcrypt**: Library `bcrypt>=4.1.0` membatasi input password ke 72 bytes. Fungsi `hash_password()` dan `verify_password()` di `middleware/auth_jwt.py` sudah menangani ini dengan `[:72]` truncation.
- **Thread-safety**: `session_state` diteruskan sebagai parameter fungsi (State Dict Passing), bukan variabel global mutable.

### 9.2. Kaidah SDLC Tambahan yang Relevan
- **Fail-Secure** (Security Design Bab 2.1): Jika terjadi crash/error saat validasi JWT, sistem WAJIB mencabut session dan kembali ke login.
- **Default Deny** (Security Design Bab 5.6): Jika peran pengguna tidak dikenal atau token invalid, akses DITOLAK secara otomatis.
- **Audit Trail** (Security Design Bab 7.2): Event `LOGOUT` wajib dicatat ke `audit_logs` baik saat logout eksplisit maupun saat session kadaluwarsa.

---

## 10. Tahapan Implementasi Detail (Checklist)

---

### TAHAP 1: Pembacaan dan Pemahaman Referensi

- [ ] Baca file `docs/sdlc/03_design/06_security_design.md` — Fokus pada:
  - [ ] Bab 4.2: Manajemen Session CLI (JWT HS256) — Catat parameter (HS256, 28800 detik, payload 5 klaim).
  - [ ] Bab 4.4: Prosedur Logout dan Penghancuran Session — Catat 3 langkah logout.
  - [ ] Bab 9.1: Sequence Diagram Login CLI — Pahami alur end-to-end.
  - [ ] Bab 10.2: Kode Error `ERR-SESSION-001` dan `ERR-SESSION-002` — Catat string pesan dan pemicunya.
  - [ ] Bab 12.2: Pseudocode fungsi `login_user()` — Pahami alur penerbitan JWT setelah bcrypt verify.
- [ ] Baca file `docs/sdlc/04_implementation/03_module_structure.md` — Fokus pada:
  - [ ] Bab 7.2: Spesifikasi `middleware/auth_jwt.py` — Catat signature fungsi `create_jwt_session`, `verify_jwt_session`.
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — Fokus pada:
  - [ ] Bab 10.3: Aturan Sesi JWT HS256 — Catat aturan kedaluwarsa, redirect, pembersihan sesi.
  - [ ] Bab 2.2.6: Monad-like Result Pattern — Pahami template `Result = namedtuple(...)`.
  - [ ] Bab 8.4: Pola State Dictionary Passing — Pahami format `session_state` dict.

---

### TAHAP 2: Audit Kode Existing

- [ ] Baca file `middleware/auth_jwt.py` dan verifikasi:
  - [ ] Fungsi `create_jwt_session()` sudah membuat payload dengan 5 klaim (`user_id`, `username`, `role`, `cabang_id`, `exp`).
  - [ ] Fungsi `create_jwt_session()` sudah menggunakan `settings.jwt_secret_key` dari `.env`.
  - [ ] Fungsi `create_jwt_session()` sudah menggunakan `datetime.timezone.utc` untuk `exp`.
  - [ ] Fungsi `verify_jwt_session()` sudah menangkap `jwt.ExpiredSignatureError` dan `jwt.InvalidTokenError`.
  - [ ] Fungsi `verify_jwt_session()` mengembalikan `dict` payload jika valid atau `None` jika invalid.
- [ ] Baca file `logic/auth_handler.py` dan verifikasi:
  - [ ] Fungsi `login_user()` memanggil `create_jwt_session()` setelah password terverifikasi.
  - [ ] Fungsi `login_user()` menyimpan token ke `session_state['token']`.
  - [ ] Fungsi `login_user()` mencatat audit trail `LOGIN_SUCCESS`.
  - [ ] Fungsi `logout_user()` mencatat audit trail `LOGOUT`.
- [ ] Baca file `cli/__init__.py` dan identifikasi:
  - [ ] Di mana `session_state` didapat setelah login berhasil (baris sekitar 154).
  - [ ] Di mana `render_dashboard()` dipanggil (baris sekitar 165).
  - [ ] Apakah ada validasi JWT sebelum masuk dashboard → **Jawaban: BELUM ADA**.
  - [ ] Apakah ada mekanisme logout dari dashboard → **Jawaban: BELUM ADA** (dashboard masih placeholder).
- [ ] Baca file `cli/dashboard.py` dan identifikasi:
  - [ ] Status implementasi `render_dashboard()` → **Jawaban: Placeholder kosong (TODO)**.
  - [ ] Status implementasi `handle_navigation()` → **Jawaban: Placeholder kosong (TODO)**.
- [ ] Baca file `middleware/rbac_guard.py` dan identifikasi:
  - [ ] Apakah `require_role()` decorator memvalidasi JWT token → **Jawaban: BELUM, hanya cek `role` string**.

---

### TAHAP 3: Penyempurnaan `middleware/auth_jwt.py`

**Tujuan:** Menambahkan fungsi `validate_session_token()` sebagai session guard terpusat.

- [ ] Buka file `middleware/auth_jwt.py`.
- [ ] Tambahkan import `namedtuple` dari `collections` (jika belum ada).
- [ ] Tambahkan definisi `Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])`.
- [ ] Tambahkan fungsi baru `validate_session_token()` dengan spesifikasi berikut:

```python
def validate_session_token(session_state: dict) -> Result:
    """Memvalidasi token JWT dari session state pengguna aktif.

    Fungsi guard terpusat yang dipanggil sebelum setiap operasi menu CLI.
    Memeriksa keberadaan token dan memverifikasi tanda tangan serta masa aktifnya.

    (Ref: Security Design Bab 4.2 & Coding Standard Bab 10.3)

    Args:
        session_state (dict): Dictionary sesi pengguna berisi kunci 'token'.

    Returns:
        Result: is_success=True dengan data=dict payload JWT jika valid,
                is_success=False dengan error_msg ERR-SESSION-001 jika token kosong,
                is_success=False dengan error_msg ERR-SESSION-002 jika token invalid/kadaluwarsa.

    Example:
        >>> session = {'token': 'valid_jwt_string', 'user_id': 1, 'role': 'kasir'}
        >>> result = validate_session_token(session)
        >>> result.is_success
        True
    """
```

- [ ] Implementasi logika di dalam `validate_session_token()`:
  - [ ] Cek apakah `session_state` ada dan berisi key `'token'`.
  - [ ] Jika `session_state` kosong/None atau `'token'` tidak ada/kosong → return `Result(False, None, 'ERR-SESSION-001: ...')`.
  - [ ] Panggil `verify_jwt_session(session_state['token'])` yang sudah ada.
  - [ ] Jika return `None` → return `Result(False, None, 'ERR-SESSION-002: ...')`.
  - [ ] Jika return dict payload → return `Result(True, payload, None)`.
- [ ] **JANGAN** mengubah fungsi `create_jwt_session()`, `verify_jwt_session()`, `hash_password()`, atau `verify_password()` yang sudah ada.
- [ ] Verifikasi kembali bahwa import dan type hints sudah benar.

---

### TAHAP 4: Penyempurnaan `middleware/rbac_guard.py`

**Tujuan:** Menambahkan validasi JWT token ke dalam RBAC guard agar otorisasi menu selalu didasarkan pada token yang sah.

- [ ] Buka file `middleware/rbac_guard.py`.
- [ ] Tambahkan import: `from middleware.auth_jwt import validate_session_token`.
- [ ] Modifikasi fungsi `require_role()` decorator agar:
  - [ ] Sebelum cek `RBAC_MATRIX`, panggil `validate_session_token(session_state)`.
  - [ ] Jika token invalid/kadaluwarsa → cetak pesan error `ERR-SESSION-002` dan return `None`.
  - [ ] Jika token valid → lanjutkan ke pengecekan `RBAC_MATRIX` yang sudah ada.
- [ ] **JANGAN** mengubah `RBAC_MATRIX` dictionary yang sudah ada.
- [ ] **JANGAN** mengubah logika `check_menu_permission()` yang sudah ada.
- [ ] Tambahkan docstring yang diperbarui pada `require_role()`.

---

### TAHAP 5: Integrasi ke CLI

#### TAHAP 5A: Penyempurnaan `cli/dashboard.py`

**Tujuan:** Mengimplementasikan loop dashboard dengan validasi JWT di setiap iterasi.

- [ ] Buka file `cli/dashboard.py`.
- [ ] Tambahkan import:
  ```python
  from middleware.auth_jwt import validate_session_token
  from logic.auth_handler import logout_user
  from db.db_connector import get_db_connection
  ```
- [ ] Implementasikan `render_dashboard()` dengan fitur:
  - [ ] Di awal setiap iterasi loop menu dashboard, panggil `validate_session_token(session_state)`.
  - [ ] Jika token invalid → cetak error, jalankan logout (audit trail), dan `return` (kembali ke login loop di `cli/__init__.py`).
  - [ ] Tampilkan info pengguna aktif: username, role, cabang_id.
  - [ ] Tampilkan opsi menu dasar: `[0] Logout`.
  - [ ] Jika pengguna memilih `0` → jalankan `logout_user()` dengan koneksi DB, cetak pesan logout, dan `return`.
- [ ] Implementasikan `handle_navigation()` dengan fitur:
  - [ ] Validasi JWT sebelum routing ke sub-menu.
  - [ ] Jika token kadaluwarsa saat navigasi → return session state yang sudah di-null-kan.
- [ ] Perbarui header module docstring.

#### TAHAP 5B: Penyempurnaan `cli/__init__.py`

**Tujuan:** Menambahkan penanganan sesi kadaluwarsa setelah dashboard `return`.

- [ ] Buka file `cli/__init__.py`.
- [ ] Setelah `render_dashboard(session_state)` selesai (baris ~165), tambahkan:
  - [ ] Pembersihan `session_state` → set ke `None` atau dict kosong.
  - [ ] Log pesan info "Sesi berakhir. Kembali ke layar login." (opsional).
  - [ ] `continue` — sehingga loop kembali ke layar login.
- [ ] Pastikan koneksi DB di-close setelah dashboard selesai (jika dashboard menggunakan DB).
- [ ] **JANGAN** mengubah logika input username/password dan pemanggilan `login_user()` yang sudah ada.

---

### TAHAP 6: Penulisan Unit Test

**Tujuan:** Menulis unit test komprehensif untuk seluruh fungsi JWT yang baru/diubah.

- [ ] Buat file baru `tests/test_jwt_session.py`.
- [ ] Tambahkan header module docstring:
  ```python
  """
  Nama Modul: test_jwt_session.py
  Deskripsi: Unit test untuk feature pembuatan dan validasi session token JWT.
             (Ref: Issue #0110)
  Author: [Nama Pelaksana]
  Tanggal: [YYYY-MM-DD]
  """
  ```
- [ ] Import dependencies:
  ```python
  import datetime
  import pytest
  from unittest.mock import patch, MagicMock
  from middleware.auth_jwt import (
      create_jwt_session,
      verify_jwt_session,
      validate_session_token,
  )
  ```

#### Test Cases yang WAJIB Diimplementasikan:

**Kelompok A: Test `create_jwt_session()` (Verifikasi existing)**
- [ ] `test_create_jwt_session_menghasilkan_token_string` — Verifikasi return type adalah `str`.
- [ ] `test_create_jwt_session_payload_mengandung_5_klaim` — Decode token dan verifikasi 5 klaim (user_id, username, role, cabang_id, exp).
- [ ] `test_create_jwt_session_exp_8_jam_dari_sekarang` — Verifikasi `exp` claim = now + 28800 detik (dengan toleransi ±5 detik).
- [ ] `test_create_jwt_session_algoritma_hs256` — Decode header dan verifikasi `alg` = `HS256`.

**Kelompok B: Test `verify_jwt_session()` (Verifikasi existing)**
- [ ] `test_verify_jwt_session_token_valid_mengembalikan_dict` — Buat token valid, verifikasi return dict.
- [ ] `test_verify_jwt_session_token_kadaluwarsa_mengembalikan_none` — Buat token dengan `exp` di masa lalu, verifikasi return `None`.
- [ ] `test_verify_jwt_session_token_signature_salah_mengembalikan_none` — Buat token dengan secret key berbeda, verifikasi return `None`.
- [ ] `test_verify_jwt_session_token_string_acak_mengembalikan_none` — Kirim string bukan JWT, verifikasi return `None`.

**Kelompok C: Test `validate_session_token()` (Fungsi baru)**
- [ ] `test_validate_session_token_valid_mengembalikan_result_sukses` — Session state dengan token valid → `Result(True, payload, None)`.
- [ ] `test_validate_session_token_tanpa_kunci_token_mengembalikan_err_session_001` — Session state tanpa key `'token'` → `Result(False, None, 'ERR-SESSION-001:...')`.
- [ ] `test_validate_session_token_session_none_mengembalikan_err_session_001` — `session_state=None` → `Result(False, None, 'ERR-SESSION-001:...')`.
- [ ] `test_validate_session_token_token_kosong_mengembalikan_err_session_001` — `session_state={'token': ''}` → `Result(False, None, 'ERR-SESSION-001:...')`.
- [ ] `test_validate_session_token_token_kadaluwarsa_mengembalikan_err_session_002` — Token expired → `Result(False, None, 'ERR-SESSION-002:...')`.
- [ ] `test_validate_session_token_token_invalid_mengembalikan_err_session_002` — Token corrupt → `Result(False, None, 'ERR-SESSION-002:...')`.

**Kelompok D: Test Integrasi Login → JWT → Verify (Opsional tetapi disarankan)**
- [ ] `test_integrasi_login_menghasilkan_token_yang_bisa_diverifikasi` — Mock DB, login berhasil, ambil `session_state['token']`, verifikasi dengan `verify_jwt_session()`.

---

### TAHAP 7: Verifikasi Akhir dan Validasi

- [ ] Jalankan **seluruh** test suite untuk memastikan zero regression:
  ```bash
  python -m pytest tests/ -v --tb=short
  ```
- [ ] Jalankan test JWT baru secara spesifik:
  ```bash
  python -m pytest tests/test_jwt_session.py -v --tb=long
  ```
- [ ] Jalankan coverage report untuk file JWT:
  ```bash
  python -m pytest tests/test_jwt_session.py --cov=middleware/auth_jwt --cov-report=term-missing
  ```
- [ ] Verifikasi coverage minimal 90% pada `middleware/auth_jwt.py`.
- [ ] Pastikan semua test yang sebelumnya hijau tetap hijau:
  - [ ] `tests/test_login_bcrypt.py` — WAJIB tetap hijau.
  - [ ] `tests/test_settings.py` — WAJIB tetap hijau.
  - [ ] `tests/test_db_connector.py` — WAJIB tetap hijau.
  - [ ] `tests/test_auth_login.py` — WAJIB tetap hijau.
- [ ] Review kembali seluruh kode yang ditulis:
  - [ ] Apakah ada hardcode secret key? → **HARUS TIDAK ADA**.
  - [ ] Apakah ada class/OOP? → **HARUS TIDAK ADA**.
  - [ ] Apakah ada f-string SQL? → **HARUS TIDAK ADA**.
  - [ ] Apakah semua fungsi punya docstring PEP 257? → **HARUS YA**.
  - [ ] Apakah semua fungsi punya type hints PEP 484? → **HARUS YA**.

---

## 11. Ringkasan File yang Akan Disentuh

| No | File | Aksi | Risiko |
|:--:|---|---|---|
| 1 | `middleware/auth_jwt.py` | **TAMBAH** fungsi `validate_session_token()` | Rendah — tidak mengubah fungsi existing |
| 2 | `middleware/rbac_guard.py` | **MODIFIKASI** `require_role()` — tambah validasi JWT | Sedang — perlu perhatian backward compatibility |
| 3 | `cli/dashboard.py` | **IMPLEMENTASI** penuh (saat ini placeholder) | Rendah — tidak ada kode aktif yang terpengaruh |
| 4 | `cli/__init__.py` | **MODIFIKASI** — tambah cleanup session setelah dashboard | Sedang — perlu perhatian terhadap loop login existing |
| 5 | `tests/test_jwt_session.py` | **BUAT BARU** — unit test JWT session | Rendah — file baru |

---

## 12. Kriteria Selesai (Definition of Done)

- [ ] Fungsi `validate_session_token()` di `middleware/auth_jwt.py` diimplementasikan dan berfungsi.
- [ ] Decorator `require_role()` di `middleware/rbac_guard.py` memvalidasi JWT sebelum cek RBAC.
- [ ] `cli/dashboard.py` memvalidasi JWT di setiap iterasi loop menu dan menangani expired/invalid.
- [ ] Logout dari dashboard menghancurkan session dan mencatat audit trail.
- [ ] `cli/__init__.py` membersihkan session setelah dashboard return.
- [ ] File `tests/test_jwt_session.py` berisi minimal 13 test cases dan coverage ≥ 90%.
- [ ] Semua test existing tetap hijau (zero regression).
- [ ] Tidak ada hardcode secret key, class/OOP, atau f-string SQL.
- [ ] Setiap fungsi baru memiliki docstring PEP 257 dan type hints PEP 484 lengkap.

---

*Dokumen issue ini disusun pada 2026-06-06 oleh Claude Opus 4.6 (Thinking) berdasarkan analisis mendalam terhadap 5 dokumen SDLC dan 10 file kode existing.*
