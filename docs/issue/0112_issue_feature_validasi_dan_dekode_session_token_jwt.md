# Issue #0112 — Feature: Validasi dan Dekode Session Token JWT

---
**Nomor Issue** : #0112
**Judul**       : Feature Validasi dan Dekode Session Token JWT
**Tanggal**     : 2026-06-06
**Prioritas**   : Tinggi (Kritikal — Prasyarat Keamanan Seluruh Modul)
**Status**      : Menunggu Implementasi
**Modul Terkait**: M.7 — Keamanan, Audit Trail & Hak Akses
**Target File Kode**: `middleware/auth_jwt.py`

---

## 1. Persona Eksekutor

> **Kamu adalah seorang Senior Security Backend Engineer & Functional Programming Specialist.**
>
> Kamu memiliki keahlian mendalam dalam:
> - Implementasi otentikasi stateless berbasis JWT (JSON Web Token) menggunakan algoritma HMAC-SHA256.
> - Pemrograman fungsional (FP) murni Python 3.14.2+ tanpa class/OOP.
> - Penanganan siklus hidup token (pembuatan, validasi signature, pengecekan kedaluwarsa, dekode payload, dan penghancuran sesi).
> - Keamanan aplikasi CLI lokal offline (LAN) untuk sistem UMKM percetakan.
> - Penulisan kode yang bersih, rapi, terdokumentasi, dan patuh standar PEP 8 / PEP 257.
>
> Kamu bertanggung jawab penuh atas keamanan sesi seluruh 8 peran pengguna dalam sistem AbuCom. Setiap kecacatan pada fitur ini berpotensi membuka celah eskalasi hak akses ilegal (`privilege escalation`) yang membahayakan data keuangan dan privasi pemilik usaha.

---

## 2. Dokumen Referensi Utama

Berikut adalah daftar dokumen SDLC yang **WAJIB** dibaca dan diekstrak informasinya sebelum memulai implementasi. Baca secara menyeluruh, jangan lewatkan detail kecil apapun yang relevan.

| No | Dokumen Referensi | Path Relatif | Alasan Pemilihan |
|:--:|---|---|---|
| R-01 | **Security Design v1.2** | `docs/sdlc/03_design/06_security_design.md` | Sumber utama spesifikasi JWT HS256, payload token, masa aktif 8 jam, handling expiration, error codes `ERR-SESSION-xxx`, dan pseudocode FP keamanan. |
| R-02 | **System Architecture v1.2** | `docs/sdlc/03_design/03_system_architecture.md` | Arsitektur 4-layer, cross-cutting concerns JWT & bcrypt, state dictionary passing, dan sequence diagram login CLI. |
| R-03 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | Aturan FP murni, Result pattern, type hints, penamaan konstanta, encoding UTF-8, docstring PEP 257, dan aturan sesi JWT Bab 10.3. |
| R-04 | **Module Structure v1.2** | `docs/sdlc/04_implementation/03_module_structure.md` | Spesifikasi file `middleware/auth_jwt.py` (Bab 7.2): signature fungsi, dependensi impor, SRS coverage, dan posisi dalam layer cross-cutting. |
| R-05 | **Database Schema (DDL) v1.2** | `docs/sdlc/03_design/01_database_schema.sql` | Skema tabel `pengguna` (kolom `role`, `cabang_id`, `locked_until`, `failed_login_attempts`) dan tabel `audit_logs`. |
| R-06 | **Access Control Matrix v1.1** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Definisi 8 peran internal, matriks hak akses 44 use case, dan aturan eskalasi supervisor. |
| R-07 | **CLI Interaction Flow v1.1** | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Alur navigasi menu CLI setelah login, dan bagaimana validasi sesi dipanggil di setiap pindah menu. |
| R-08 | **Environment Setup v1.1** | `docs/sdlc/04_implementation/02_environment_setup.md` | Konfigurasi `.env` untuk `JWT_SECRET_KEY` dan `JWT_LIFETIME_SECONDS`. |

> [!IMPORTANT]
> File `narasi.txt` **TIDAK** diperlukan sebagai referensi untuk issue ini. Issue ini bersifat teknis keamanan murni dan seluruh spesifikasi sudah didefinisikan lengkap di dokumen SDLC fase 03 dan 04.

---

## 3. Ringkasan Data Relevan dari Dokumen Referensi

Berikut adalah ekstraksi **seluruh detail data** yang spesifik dan relevan untuk pengerjaan issue ini. Jangan lewatkan satupun informasi di bawah ini.

### 3.1. Spesifikasi Token JWT (dari R-01: Security Design Bab 4.2)

| Parameter | Nilai/Spesifikasi |
|---|---|
| **Algoritma Tanda Tangan** | `HS256` (HMAC-SHA256) |
| **Secret Key** | Minimum 32 karakter heksadesimal, dimuat dari `.env` variabel `JWT_SECRET_KEY` |
| **Masa Berlaku Sesi** | Maksimal **28.800 detik (8 jam)**, setara 1 shift kerja staf |
| **Library Python** | `pyjwt==2.8.0` |
| **Payload Token** | `user_id` (int), `username` (str), `role` (str), `cabang_id` (int), `exp` (unix timestamp UTC) |
| **Handling Expiration** | Tangkap `jwt.ExpiredSignatureError`, hapus token dari memori, paksa kembali ke layar login dengan kode `ERR-SESSION-002` |
| **Mid-Transaction Expiry** | Jika token kedaluwarsa di tengah operasi yang berjalan, transaksi harus di-rollback sebelum sesi dihancurkan |

### 3.2. Payload Token JWT (Struktur Wajib)

```json
{
    "user_id": 1,
    "username": "kasir_andi",
    "role": "kasir",
    "cabang_id": 1,
    "exp": 1779928800
}
```

### 3.3. Kode Error Terkait Sesi (dari R-01: Security Design Bab 10.2)

| Kode Error | Pesan CLI | Kondisi Pemicu |
|---|---|---|
| `ERR-SESSION-001` | `Sesi login tidak ditemukan. Harap login terlebih dahulu!` | Mencoba akses menu CLI tanpa session JWT aktif (token kosong/None/tidak ada). |
| `ERR-SESSION-002` | `Sesi login tidak sah/rusak. Harap login kembali!` | Token signature tidak cocok **ATAU** masa aktif 8 jam sudah kedaluwarsa. |

### 3.4. Nilai Valid Peran Pengguna (dari R-05: DDL Tabel `pengguna`, Kolom `role`)

```
'pemilik' | 'kepala_percetakan' | 'pramuniaga' | 'kasir' | 'desainer' | 'produksi_cetak' | 'fotocopy_print' | 'gudang'
```

Total: **8 peran internal** yang bisa tersimpan di payload JWT.

### 3.5. Konfigurasi `.env` Terkait JWT (dari R-08 dan file `.env.example` existing)

```ini
# 3. Kunci Rahasia Otorisasi Sesi JWT (HS256)
JWT_SECRET_KEY=YOUR_JWT_SECRET_KEY_HERE
JWT_LIFETIME_SECONDS=28800
```

### 3.6. State Dictionary Passing (dari R-03: Coding Standard Bab 8.4)

Template `session_state` yang mengalir sebagai parameter ke setiap fungsi menu CLI:

```python
session_state = {
    'user_id': 3,
    'username': 'kasir_andi',
    'role': 'kasir',
    'token': 'jwt_string_token',
    'cabang_id': 1
}
```

### 3.7. Konstanta Keamanan Wajib (dari R-01 dan R-03)

```python
BCRYPT_COST_FACTOR = 12
JWT_ALGORITHM = 'HS256'
JWT_LIFETIME_SECONDS = 28800  # Default 8 jam, override dari .env
```

### 3.8. Pola Desain Wajib (dari R-03: Coding Standard Bab 2.2.6 dan Bab 8.7)

```python
from collections import namedtuple
Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
```

### 3.9. Signature Fungsi Standar (dari R-04: Module Structure Bab 7.2)

```python
def hash_password(password_polos: str) -> str:
    """Mengenkripsi sandi menggunakan bcrypt cost factor = 12."""
    pass

def create_jwt_session(user_id: int, role: str, cabang_id: int) -> str:
    """Membuat token session JWT HS256 masa aktif 8 jam."""
    pass

def verify_jwt_session(token: str) -> dict | None:
    """Validasi token JWT, melempar Exception jika kadaluwarsa."""
    pass
```

> [!NOTE]
> Implementasi existing di `middleware/auth_jwt.py` sudah menambahkan parameter `username: str` pada `create_jwt_session()`. Ini konsisten dengan payload Security Design yang memuat `username`. Pertahankan parameter ini.

### 3.10. Alur Pemanggilan Validasi Sesi di Sistem (Consumer Konteks)

Berdasarkan analisis kode existing, fungsi `validate_session_token()` dipanggil oleh:

1. `middleware/rbac_guard.py` → `require_role()` decorator (sebelum setiap akses menu CLI)
2. `cli/dashboard.py` → Validasi sesi saat render dashboard
3. `tests/test_config_cache.py` → Testing integrasi
4. `tests/unit/logic/test_m10_runtime_config.py` → Testing modul konfigurasi runtime

---

## 4. Batasan dan Cakupan Pengerjaan

### 4.1. Cakupan (IN-SCOPE) — Yang Harus Dikerjakan

- [x] Fungsi `verify_jwt_session(token: str) -> dict | None` — Validasi signature dan decode payload JWT.
- [x] Fungsi `validate_session_token(session_state: dict | None) -> Result` — Guard terpusat validasi sesi sebelum setiap operasi menu CLI.
- [x] Penanganan error `jwt.ExpiredSignatureError` — Token kedaluwarsa harus mengembalikan `None`.
- [x] Penanganan error `jwt.InvalidTokenError` — Token rusak/format salah harus mengembalikan `None`.
- [x] Pengembalian kode error `ERR-SESSION-001` — Saat token tidak ada/kosong.
- [x] Pengembalian kode error `ERR-SESSION-002` — Saat token invalid/kedaluwarsa.
- [x] **Validasi kelengkapan payload** — Memastikan payload yang didekode mengandung 5 klaim wajib: `user_id`, `username`, `role`, `cabang_id`, `exp`.
- [x] **Validasi tipe data payload** — Memastikan `user_id` bertipe `int`, `role` bertipe `str`, `cabang_id` bertipe `int`.
- [x] **Validasi nilai `role` terhadap daftar peran valid** — Memastikan `role` di payload termasuk dalam 8 peran yang sah.
- [x] Unit test komprehensif untuk seluruh skenario validasi dan dekode.

### 4.2. Di Luar Cakupan (OUT-OF-SCOPE) — Yang Tidak Boleh Disentuh

> [!CAUTION]
> Pengerjaan issue ini **DILARANG KERAS** menyentuh atau memodifikasi fitur-fitur berikut:

- ❌ Fungsi `hash_password()` — Sudah final dan teruji.
- ❌ Fungsi `verify_password()` — Sudah final dan teruji.
- ❌ Fungsi `create_jwt_session()` — Sudah final dan teruji.
- ❌ File `config/settings.py` — Sudah final dan teruji.
- ❌ File `middleware/rbac_guard.py` — Bukan cakupan issue ini.
- ❌ File `middleware/audit_logger.py` — Bukan cakupan issue ini.
- ❌ File `db/db_connector.py` — Bukan cakupan issue ini.
- ❌ File `main.py` — Bukan cakupan issue ini.
- ❌ Logika login (`logic/auth_handler.py`) — Bukan cakupan issue ini.
- ❌ Skema database (`schema.sql`) — Bukan cakupan issue ini.
- ❌ Alur bcrypt password hashing/verification — Bukan cakupan issue ini.
- ❌ Alur rate limiting dan lockout — Bukan cakupan issue ini.

### 4.3. Prinsip Non-Destruktif

- Semua perubahan harus **backward-compatible** dengan fungsi dan test yang sudah ada.
- Jangan mengubah signature fungsi existing yang sudah dipanggil oleh modul lain.
- Jangan menghapus komentar atau docstring yang sudah ada kecuali untuk perbaikan faktual.
- Pastikan semua test existing (`test_jwt_session.py`, `test_auth_jwt.py`) tetap PASS setelah perubahan.

---

## 5. Alur Pengerjaan Detail

### 5.1. Diagram Alur Validasi dan Dekode Token JWT

```
[Input: session_state dict]
        |
        v
[Cek: session_state None/bukan dict?] ──YES──> Return Result(False, None, ERR-SESSION-001)
        |
       NO
        v
[Cek: key 'token' ada & tidak kosong?] ──NO──> Return Result(False, None, ERR-SESSION-001)
        |
       YES
        v
[Panggil verify_jwt_session(token)]
        |
        v
[jwt.decode(token, secret_key, algorithms=['HS256'])]
        |
        ├── jwt.ExpiredSignatureError ──> Return None
        ├── jwt.InvalidTokenError ────> Return None
        └── Sukses: payload dict
                |
                v
        [Validasi kelengkapan 5 klaim wajib]
                |
                ├── Klaim hilang ──> Return None
                └── Lengkap
                        |
                        v
                [Validasi tipe data klaim]
                        |
                        ├── Tipe salah ──> Return None
                        └── Valid
                                |
                                v
                        [Validasi role terhadap VALID_ROLES]
                                |
                                ├── Role tidak sah ──> Return None
                                └── Sah
                                        |
                                        v
                                Return payload dict
        |
        v (kembali ke validate_session_token)
[payload is None?] ──YES──> Return Result(False, None, ERR-SESSION-002)
        |
       NO
        v
Return Result(True, payload, None)
```

---

## 6. Instruksi Implementasi Tahap demi Tahap

> [!IMPORTANT]
> Kerjakan setiap tahap secara **rapi, bersih, tidak tergesa-gesa, dan tidak buru-buru**. Pastikan setiap langkah selesai dengan benar sebelum melanjutkan ke langkah berikutnya. Kualitas kelengkapan pengerjaan issue ini harus maksimal agar tidak selalu dipertanyakan dan tidak menghambat feature lain yang bergantung pada validasi sesi JWT.

### Tahap 0: Pembacaan dan Pemahaman Referensi

- [ ] Baca file `docs/sdlc/03_design/06_security_design.md` secara menyeluruh, khusus fokus pada **Bab 4.2** (Manajemen Session CLI JWT HS256), **Bab 10.2** (Kode Error ERR-SESSION-xxx), dan **Bab 12.2** (Pseudocode keamanan).
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` secara menyeluruh, khusus fokus pada **Bab 2.2** (Prinsip FP Murni), **Bab 2.2.6** (Result Pattern), **Bab 8.4** (State Dictionary Passing), **Bab 10.3** (Aturan Sesi JWT HS256).
- [ ] Baca file `docs/sdlc/04_implementation/03_module_structure.md` secara menyeluruh, khusus fokus pada **Bab 7.2** (File `middleware/auth_jwt.py`).
- [ ] Baca file `middleware/auth_jwt.py` yang sudah ada (170 baris) untuk memahami kode existing.
- [ ] Baca file `middleware/rbac_guard.py` yang sudah ada (64 baris) untuk memahami bagaimana `validate_session_token()` dikonsumsi oleh decorator RBAC.
- [ ] Baca file `config/settings.py` yang sudah ada (372 baris) untuk memahami bagaimana `JWT_SECRET_KEY` dan `JWT_LIFETIME_SECONDS` dimuat.
- [ ] Baca file `.env.example` (36 baris) untuk memahami format variabel lingkungan JWT.
- [ ] Baca file `tests/test_jwt_session.py` (337 baris) untuk memahami test existing yang sudah ada dan **TIDAK BOLEH** di-break.
- [ ] Baca file `tests/test_auth_jwt.py` (228 baris) untuk memahami test existing yang sudah ada dan **TIDAK BOLEH** di-break.

### Tahap 1: Definisi Konstanta Validasi Peran

- [ ] Buka file `middleware/auth_jwt.py`.
- [ ] Tambahkan konstanta `VALID_ROLES` (tuple imutabel) yang berisi 8 peran valid tepat setelah baris `JWT_ALGORITHM = 'HS256'` (baris 20) dan sebelum baris `Result = namedtuple(...)` (baris 21).

Konten yang harus ditambahkan:

```python
VALID_ROLES = (
    'pemilik',
    'kepala_percetakan',
    'pramuniaga',
    'kasir',
    'desainer',
    'produksi_cetak',
    'fotocopy_print',
    'gudang',
)

REQUIRED_JWT_CLAIMS = ('user_id', 'username', 'role', 'cabang_id', 'exp')
```

- [ ] Pastikan konstanta menggunakan format `UPPER_SNAKE_CASE` sesuai Coding Standard Bab 3.3.
- [ ] Pastikan menggunakan `tuple` (imutabel) bukan `list` sesuai prinsip FP Coding Standard Bab 2.2.2.

### Tahap 2: Penyempurnaan Fungsi `verify_jwt_session()`

- [ ] Buka file `middleware/auth_jwt.py`.
- [ ] Lokasi: fungsi `verify_jwt_session()` (baris 107-121).
- [ ] Perkuat fungsi ini dengan menambahkan **validasi kelengkapan payload**, **validasi tipe data**, dan **validasi role** setelah decode berhasil.

Implementasi yang harus ditulis (menggantikan isi fungsi existing):

```python
def verify_jwt_session(token: str) -> dict | None:
    """Memvalidasi dan mendekode token JWT session pengguna.

    Melakukan 4 tahap validasi secara berurutan:
    1. Dekode token dan verifikasi signature HS256 terhadap secret key.
    2. Verifikasi masa aktif token belum kedaluwarsa (exp claim).
    3. Validasi kelengkapan 5 klaim wajib di payload.
    4. Validasi tipe data dan nilai klaim (role harus termasuk 8 peran valid).

    (Ref: Security Design v1.2 Bab 4.2, Coding Standard v1.2 Bab 10.3)

    Args:
        token (str): String token JWT dari sesi pengguna aktif.

    Returns:
        dict | None: Dictionary payload klaim JWT jika seluruh validasi lolos,
                     None jika token kedaluwarsa, signature salah, format rusak,
                     klaim tidak lengkap, atau role tidak valid.

    Example:
        >>> payload = verify_jwt_session('eyJhbGciOi...')
        >>> payload['user_id']
        1
        >>> payload['role']
        'kasir'
    """
    settings = load_settings()
    secret_key = settings.jwt_secret_key
    try:
        payload = jwt.decode(token, secret_key, algorithms=[JWT_ALGORITHM])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None

    # Validasi kelengkapan klaim wajib
    for claim in REQUIRED_JWT_CLAIMS:
        if claim not in payload:
            return None

    # Validasi tipe data klaim
    if not isinstance(payload.get('user_id'), int):
        return None
    if not isinstance(payload.get('username'), str):
        return None
    if not isinstance(payload.get('role'), str):
        return None
    if not isinstance(payload.get('cabang_id'), int):
        return None

    # Validasi role terhadap daftar peran valid
    if payload.get('role') not in VALID_ROLES:
        return None

    return payload
```

- [ ] Pastikan docstring menggunakan format PEP 257 Google Style sesuai Coding Standard Bab 6.2.
- [ ] Pastikan menggunakan konstanta `JWT_ALGORITHM` bukan string literal `'HS256'`.
- [ ] Pastikan menggunakan konstanta `REQUIRED_JWT_CLAIMS` bukan hardcoded tuple.
- [ ] Pastikan menggunakan konstanta `VALID_ROLES` bukan hardcoded list/tuple.

### Tahap 3: Verifikasi Fungsi `validate_session_token()` 

- [ ] Buka file `middleware/auth_jwt.py`.
- [ ] Lokasi: fungsi `validate_session_token()` (baris 124-169).
- [ ] **Verifikasi** bahwa fungsi existing sudah benar dan lengkap. Fungsi ini sudah mengimplementasikan:
  - Pengecekan `session_state` None atau bukan dict → `ERR-SESSION-001`
  - Pengecekan key `'token'` tidak ada atau kosong → `ERR-SESSION-001`
  - Pemanggilan `verify_jwt_session(token)` → jika None → `ERR-SESSION-002`
  - Pengembalian `Result(True, payload, None)` jika valid
- [ ] **Jangan ubah** logika fungsi ini kecuali ada bug yang ditemukan.
- [ ] Perbarui docstring jika perlu agar mencerminkan bahwa `verify_jwt_session()` sekarang juga melakukan validasi kelengkapan payload dan validasi role.

Penyesuaian docstring (jika diperlukan):

```python
def validate_session_token(session_state: dict | None) -> Result:
    """Memvalidasi token JWT dari session state pengguna aktif.

    Fungsi guard terpusat yang dipanggil sebelum setiap operasi menu CLI.
    Memeriksa keberadaan token, memverifikasi tanda tangan, masa aktif,
    kelengkapan payload, dan keabsahan role pengguna.

    (Ref: Security Design v1.2 Bab 4.2 & Coding Standard v1.2 Bab 10.3)

    Args:
        session_state (dict | None): Dictionary sesi pengguna berisi kunci 'token'.

    Returns:
        Result: is_success=True dengan data=dict payload JWT jika valid,
                is_success=False dengan error_msg ERR-SESSION-001 jika token kosong,
                is_success=False dengan error_msg ERR-SESSION-002 jika token invalid/
                kedaluwarsa/payload tidak lengkap/role tidak valid.

    Example:
        >>> session = {'token': 'valid_jwt_string', 'user_id': 1, 'role': 'kasir'}
        >>> result = validate_session_token(session)
        >>> result.is_success
        True
    """
```

### Tahap 4: Penulisan Unit Test Tambahan

- [ ] Buat file test baru: `tests/test_verify_jwt_decode.py`.
- [ ] Tulis test cases berikut menggunakan framework `pytest` dan `unittest.mock.patch`.

Test cases yang **WAJIB** ditulis:

```python
"""
Nama Modul: test_verify_jwt_decode.py
Deskripsi: Unit test untuk validasi dan dekode session token JWT,
           mencakup validasi kelengkapan payload, tipe data klaim,
           dan keabsahan role pengguna.
           (Ref: Issue #0112)
Author: [Nama Pengembang / AI]
Tanggal: [YYYY-MM-DD]
"""
```

#### 4.1. Test Validasi Kelengkapan Payload

- [ ] `test_verify_jwt_tolak_token_tanpa_klaim_user_id()` — Buat token manual tanpa `user_id`, verifikasi return `None`.
- [ ] `test_verify_jwt_tolak_token_tanpa_klaim_username()` — Buat token manual tanpa `username`, verifikasi return `None`.
- [ ] `test_verify_jwt_tolak_token_tanpa_klaim_role()` — Buat token manual tanpa `role`, verifikasi return `None`.
- [ ] `test_verify_jwt_tolak_token_tanpa_klaim_cabang_id()` — Buat token manual tanpa `cabang_id`, verifikasi return `None`.
- [ ] `test_verify_jwt_tolak_token_tanpa_klaim_exp()` — Buat token manual tanpa `exp`, verifikasi return `None`.

Contoh cara membuat token manual untuk test:

```python
import jwt
import datetime

def _buat_token_kustom(payload: dict, secret_key: str) -> str:
    """Helper untuk membuat token JWT kustom dengan payload tertentu."""
    return jwt.encode(payload, secret_key, algorithm='HS256')


def test_verify_jwt_tolak_token_tanpa_klaim_user_id(mock_load_settings):
    """Memastikan token tanpa klaim user_id ditolak."""
    payload = {
        'username': 'kasir_andi',
        'role': 'kasir',
        'cabang_id': 1,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=8)
    }
    token = _buat_token_kustom(payload, MOCK_SETTINGS.jwt_secret_key)
    result = verify_jwt_session(token)
    assert result is None
```

#### 4.2. Test Validasi Tipe Data Klaim

- [ ] `test_verify_jwt_tolak_user_id_string()` — Buat token dengan `user_id` bertipe string, verifikasi return `None`.
- [ ] `test_verify_jwt_tolak_cabang_id_string()` — Buat token dengan `cabang_id` bertipe string, verifikasi return `None`.
- [ ] `test_verify_jwt_tolak_role_integer()` — Buat token dengan `role` bertipe integer, verifikasi return `None`.

#### 4.3. Test Validasi Role Terhadap Daftar Valid

- [ ] `test_verify_jwt_tolak_role_tidak_valid()` — Buat token dengan `role` = `'admin'` (tidak ada di daftar 8 peran), verifikasi return `None`.
- [ ] `test_verify_jwt_tolak_role_kosong()` — Buat token dengan `role` = `''`, verifikasi return `None`.
- [ ] `test_verify_jwt_terima_seluruh_8_role_valid()` — Loop melalui 8 peran valid, buat token untuk masing-masing, verifikasi semuanya return dict (bukan None).

#### 4.4. Test Token Valid (Positive Case)

- [ ] `test_verify_jwt_token_valid_mengembalikan_payload_lengkap()` — Buat token valid dengan 5 klaim, verifikasi return dict dengan semua klaim utuh.

#### 4.5. Test Integrasi dengan `validate_session_token()`

- [ ] `test_validate_session_token_payload_tidak_lengkap_return_err_session_002()` — Pastikan token tanpa klaim wajib menghasilkan `ERR-SESSION-002`.
- [ ] `test_validate_session_token_role_tidak_valid_return_err_session_002()` — Pastikan token dengan role invalid menghasilkan `ERR-SESSION-002`.

### Tahap 5: Jalankan Seluruh Test Suite

- [ ] Jalankan perintah: `python -m pytest tests/test_verify_jwt_decode.py -v` untuk menjalankan test baru.
- [ ] Jalankan perintah: `python -m pytest tests/test_jwt_session.py -v` untuk memastikan test existing tetap PASS.
- [ ] Jalankan perintah: `python -m pytest tests/test_auth_jwt.py -v` untuk memastikan test existing tetap PASS.
- [ ] Jalankan perintah: `python -m pytest tests/ -v --tb=short` untuk memastikan seluruh test suite tidak ada yang FAIL.
- [ ] Pastikan **0 (nol) test FAIL** dan **0 (nol) test ERROR**.

### Tahap 6: Validasi Akhir dan Pembersihan

- [ ] Review ulang seluruh perubahan di `middleware/auth_jwt.py`:
  - Pastikan tidak ada import yang tidak terpakai.
  - Pastikan tidak ada variabel global yang dimutasi.
  - Pastikan indentasi konsisten 4 spasi (bukan tab).
  - Pastikan panjang baris tidak melebihi 120 karakter.
  - Pastikan komentar dan docstring menggunakan bahasa yang konsisten.
- [ ] Pastikan file `middleware/auth_jwt.py` tetap memiliki header module docstring sesuai Coding Standard Bab 6.4.
- [ ] Pastikan tidak ada `TODO` atau `FIXME` baru yang ditambahkan tanpa justifikasi.
- [ ] Periksa bahwa file yang dimodifikasi hanya:
  - `middleware/auth_jwt.py` (modifikasi)
  - `tests/test_verify_jwt_decode.py` (file baru)
- [ ] Periksa bahwa **TIDAK ADA** file lain yang termodifikasi.

---

## 7. Kaidah dan Standar Pengerjaan Tambahan

### 7.1. Standar FP Murni (Coding Standard Bab 2.2)

- [x] Fungsi `verify_jwt_session()` harus tetap berupa **pure function** sejauh memungkinkan (input sama → output sama). Efek samping hanya pemanggilan `load_settings()` yang membaca `.env`.
- [x] Tidak boleh mendeklarasikan `class` apapun.
- [x] Tidak boleh menggunakan variabel global mutable.
- [x] Data return harus menggunakan tipe imutabel (`dict` read-only atau `NamedTuple`).

### 7.2. Standar Keamanan (Security Design Bab 2.1)

- [x] Prinsip **Default Deny**: Jika payload tidak lengkap atau role tidak dikenali, token ditolak.
- [x] Prinsip **Fail-Secure**: Jika terjadi exception apapun saat dekode, return `None` (tolak akses).
- [x] Jangan pernah mengekspos detail error internal (seperti traceback atau secret key) ke output CLI.

### 7.3. Standar Type Hints (Coding Standard Bab 7)

- [x] Gunakan `dict | None` (Python 3.10+ pipe syntax), bukan `Optional[dict]`.
- [x] Semua parameter dan return value harus memiliki type hints lengkap.

### 7.4. Standar Docstring (Coding Standard Bab 6)

- [x] Format: PEP 257 Google Style.
- [x] Harus memuat: Deskripsi, Args, Returns, Example.
- [x] Referensi silang ke dokumen SDLC menggunakan format: `(Ref: Security Design v1.2 Bab X.Y)`.

### 7.5. Standar Error Code (Coding Standard Bab 11.5)

- [x] Format: `ERR-[KATEGORI]-[NOMOR]: [Pesan deskriptif bahasa Indonesia]`
- [x] Hanya gunakan kode error yang sudah terdaftar di Security Design Bab 10.2.
- [x] Jangan membuat kode error baru tanpa konsultasi.

### 7.6. Standar Testing (Coding Standard Bab 14)

- [x] Gunakan framework `pytest`.
- [x] Mock `load_settings()` menggunakan `unittest.mock.patch` agar test terisolasi dari file `.env` aktual.
- [x] Setiap test function harus memiliki docstring yang menjelaskan apa yang diuji.
- [x] Nama test function menggunakan format: `test_[fungsi_yang_diuji]_[kondisi]_[ekspektasi]()`.
- [x] Target code coverage: **≥ 90%** untuk fungsi yang dimodifikasi.

---

## 8. Penanganan Data Kosong atau Tidak Tersedia

> [!WARNING]
> Jika kamu menemukan data yang kosong, tidak tersedia, atau ambigu di file referensi saat implementasi, **jangan asumsikan atau buat sendiri**. Tandai dengan komentar berikut di dalam kode:

```python
# [DATA-KOSONG] Deskripsi data yang tidak ditemukan.
# Sumber referensi: [Nama dokumen & Bab]
# Status: Menunggu konfirmasi dari pemilik proyek.
```

Berdasarkan analisis, berikut data yang sudah dikonfirmasi tersedia dan lengkap:

| Data | Status | Sumber |
|---|---|---|
| 8 peran valid (`role`) | ✅ Lengkap | DDL tabel `pengguna`, kolom `role` |
| Payload JWT (5 klaim) | ✅ Lengkap | Security Design Bab 4.2 |
| Kode error `ERR-SESSION-001` | ✅ Lengkap | Security Design Bab 10.2 |
| Kode error `ERR-SESSION-002` | ✅ Lengkap | Security Design Bab 10.2 |
| Secret key source (`.env`) | ✅ Lengkap | `.env.example` baris 21 |
| Lifetime 28800 detik | ✅ Lengkap | `.env.example` baris 22, Security Design Bab 4.2 |
| Library `pyjwt==2.8.0` | ✅ Lengkap | `requirements.txt` |

---

## 9. Catatan Khusus JWT yang Harus Diperhatikan

### 9.1. Penanganan Mid-Transaction Expiry

Sesuai Security Design Bab 4.2:
> "Jika kedaluwarsa terjadi di tengah operasi yang sedang berjalan (*mid-transaction*), transaksi dibatalkan (*rollback*) secara aman sebelum sesi dihancurkan untuk menjaga integritas ACID."

Catatan: Penanganan rollback mid-transaction **bukan** tanggung jawab `verify_jwt_session()` atau `validate_session_token()`. Rollback ditangani oleh `db/query_builder.py` (`execute_acid_transaction()`) yang menangkap exception di level transaction wrapper. Yang harus dilakukan oleh issue ini adalah memastikan `verify_jwt_session()` mengembalikan `None` secara konsisten saat token kedaluwarsa, sehingga caller (RBAC guard/menu CLI) bisa memutuskan untuk membatalkan operasi.

### 9.2. Stateless Nature

Token JWT di AbuCom bersifat **stateless** — tidak ada database session store. Validasi dilakukan murni berdasarkan:
1. Verifikasi signature menggunakan secret key.
2. Verifikasi masa aktif (exp claim).
3. Validasi payload (tambahan dari issue ini).

Tidak perlu query database untuk validasi sesi.

### 9.3. Truncation Bcrypt 72 Bytes

Perhatikan bahwa file existing memiliki `FIXME` pada `hash_password()` dan `verify_password()` tentang truncation 72 bytes. **Jangan sentuh ini** — bukan cakupan issue ini.

---

## 10. Checklist Akhir Sebelum Issue Ditutup

- [ ] Seluruh tahap pada Bagian 6 telah selesai dikerjakan dan di-checklist.
- [ ] Konstanta `VALID_ROLES` dan `REQUIRED_JWT_CLAIMS` sudah ditambahkan dengan benar.
- [ ] Fungsi `verify_jwt_session()` sudah diperkuat dengan validasi payload, tipe data, dan role.
- [ ] Fungsi `validate_session_token()` sudah diverifikasi tetap konsisten.
- [ ] Docstring sudah diperbarui sesuai standar PEP 257 Google Style.
- [ ] File test `tests/test_verify_jwt_decode.py` sudah dibuat dengan minimal 15 test cases.
- [ ] Seluruh test existing (`test_jwt_session.py`, `test_auth_jwt.py`) tetap PASS.
- [ ] Seluruh test baru PASS dengan 0 error.
- [ ] Tidak ada file di luar cakupan yang termodifikasi.
- [ ] Tidak ada `print()` debugging yang tertinggal di kode produksi.
- [ ] Kode sudah direview ulang untuk kebersihan, keterbacaan, dan konsistensi.
- [ ] Semua tag `[DATA-KOSONG]` sudah dikomunikasikan jika ada.

---

*Dokumen issue ini disusun oleh Claude Opus 4.6 (Thinking) selaku Senior Security Architect & Issue Planning Specialist pada tanggal 2026-06-06.*
