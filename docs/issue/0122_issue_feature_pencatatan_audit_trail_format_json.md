# Issue #0122 — Feature: Pencatatan Audit Trail Format JSON

---
**Nomor Issue** : #0122
**Judul**       : Feature Pencatatan Audit Trail Format JSON
**Prioritas**   : 🔴 Critical (Keamanan & Compliance)
**Modul**       : M.7 — Keamanan, Audit Trail & Hak Akses
**Status**      : 📋 Ready for Implementation
**Tanggal**     : 2026-06-07
**Estimasi**    : 3–5 hari kerja
---

## 1. Persona Pelaksana

Kamu adalah **Senior Security & Compliance Engineer** yang memiliki keahlian mendalam dalam:
- Perancangan sistem audit trail dan forensik digital untuk aplikasi bisnis UMKM.
- Pemrograman fungsional murni (Functional Programming) Python 3.14.2+ tanpa `class`.
- Integrasi database transaksional MySQL InnoDB dengan integritas ACID.
- Kepatuhan regulasi keamanan data (OWASP, UU PDP No. 27/2022, NIST).
- Penulisan kode yang bersih, terdokumentasi, dan mudah dipelihara oleh Junior Programmer.

**Mandatmu adalah:**
- Mengimplementasikan fitur pencatatan audit trail format JSON yang **lengkap, akurat, dan presisi** sesuai spesifikasi dokumen SDLC.
- Memastikan **setiap modifikasi data sensitif** tercatat secara kronologis tanpa celah.
- Menjaga **integritas feature lain** yang sudah ada — tidak boleh ada feature yang rusak akibat implementasi ini.
- Bekerja dengan **rapi, bersih, tidak tergesa-gesa** agar hasilnya maksimal dan berkualitas tinggi.

---

## 2. File Referensi Utama (Wajib Dibaca)

Berikut adalah daftar file referensi yang **wajib** dibaca dan diekstrak informasinya **sebelum** memulai implementasi. Urutkan pembacaan sesuai urutan di bawah ini:

| No | File Referensi | Path Relatif | Relevansi untuk Issue Ini |
|:--:|---|---|---|
| 1 | **Security Design v1.2** | `docs/sdlc/03_design/06_security_design.md` | **Sumber utama #1**: Bab 7 (Desain Audit Trail dan Monitoring) — skema tabel `audit_logs`, event pemicu, format JSON `old_value`/`new_value`, deteksi anomali fraud, retensi log 12 bulan, pseudocode fungsi `write_audit_log()`. Bab 2.3 (Klasifikasi sensitivitas data 3-tier). Bab 12 (Pseudocode implementasi FP). |
| 2 | **Coding Standard v1.2** | `docs/sdlc/04_implementation/01_coding_standard.md` | **Sumber utama #2**: Bab 10.6 (Aturan Audit Trail Logging wajib), Bab 10.8 (System Logging standar Python `logging`), standar FP murni, Result Pattern, parameterized query `%s`, type hints PEP 484, naming snake_case. |
| 3 | **Module Structure v1.2** | `docs/sdlc/04_implementation/03_module_structure.md` | Bab 7.4 — spesifikasi file `middleware/audit_logger.py`: tanggung jawab, signature fungsi `log_audit_trail()`, modul SRS di-cover (`SRS-F-031`). |
| 4 | **Database Schema DDL v1.2** | `docs/sdlc/03_design/01_database_schema.sql` | TABEL 25 `audit_logs`: definisi kolom fisik (`id`, `pengguna_id`, `action_timestamp`, `action_type`, `target_table`, `old_value` JSON, `new_value` JSON, `ip_address`, `cabang_id`), constraint FK, dan engine InnoDB. |
| 5 | **Software Requirements v1.1** | `docs/sdlc/02_analysis/02_software_requirements.md` | Kebutuhan fungsional `SRS-F-031` (Audit Trail JSON granular) dan `SRS-F-034` (Deteksi Fraud). |
| 6 | **Access Control Matrix v1.1** | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Bab 6.6 — aturan audit trail pelanggaran akses `ACCESS_DENIED`, hak akses tabel `audit_logs` per role. |
| 7 | **System Architecture v1.1** | `docs/sdlc/03_design/03_system_architecture.md` | Arsitektur 4-layer, posisi middleware sebagai cross-cutting concern. |

> [!IMPORTANT]
> File `docs/sdlc/narasi.txt` **tidak perlu** dijadikan referensi utama untuk issue ini. Narasi sudah diturunkan ke dokumen-dokumen SDLC di atas yang lebih terstruktur dan spesifik.

---

## 3. Ringkasan Data Relevan dari Dokumen Referensi

Baca dan ekstrak secara teliti seluruh informasi berikut dari file referensi. **Jangan lewatkan detail kecil apapun.**

### 3.1. Skema Tabel `audit_logs` (Sumber: DDL SQL — Tabel 25)

```sql
CREATE TABLE audit_logs (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pengguna_id INT NOT NULL,
    action_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    action_type VARCHAR(20) NOT NULL,        -- 'INSERT' | 'UPDATE' | 'DELETE' | 'ACCESS_DENIED'
    target_table VARCHAR(100) NOT NULL,
    old_value JSON NULL DEFAULT NULL,
    new_value JSON NULL DEFAULT NULL,
    ip_address VARCHAR(45) NULL DEFAULT NULL,
    cabang_id INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_audit_logs_pengguna_id FOREIGN KEY (pengguna_id)
        REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_audit_logs_cabang_id FOREIGN KEY (cabang_id)
        REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Kolom penting yang harus diperhatikan:**
- `action_type`: Hanya 4 nilai valid → `'INSERT'`, `'UPDATE'`, `'DELETE'`, `'ACCESS_DENIED'`
- `old_value` & `new_value`: Tipe data **JSON** MySQL — menyimpan snapshot state lengkap baris data sebelum dan sesudah modifikasi
- `ip_address`: Alamat IP klien terminal (default LAN: `'192.168.1.x'`)
- `cabang_id`: Wajib ada untuk dukungan multi-cabang

### 3.2. Event Pemicu Pencatatan Audit (Sumber: Security Design Bab 7.2)

Peristiwa-peristiwa berikut **WAJIB** memicu penulisan log audit:

| No | Event Kategori | action_type | Deskripsi Detail |
|:--:|---|---|---|
| 1 | Modifikasi data pada 5 tabel **Sangat Sensitif** | `INSERT`/`UPDATE`/`DELETE` | Tabel: `pinjaman_bank`, `pinjaman_kerabat`, `payroll`, `system_configs`, `backup_logs`, `aset` |
| 2 | Modifikasi data pada 7 tabel **Sensitif** | `INSERT`/`UPDATE`/`DELETE` | Tabel: `transaksi`, `pengeluaran`, `audit_logs`, `shift_handover`, `utang_supplier`, `limbah_produksi`, `stock_opname` |
| 3 | Akses menu CLI ditolak RBAC | `ACCESS_DENIED` | Saat dekorator otorisasi mendeteksi peran ilegal |
| 4 | Login berhasil | `LOGIN_SUCCESS` (dalam new_value) | Rekam user_id, role, cabang_id, timestamp |
| 5 | Login gagal | `LOGIN_FAILED` (dalam new_value) | Rekam username yang dicoba, IP terminal |
| 6 | Logout pengguna | `LOGOUT` (dalam new_value) | Rekam user_id, durasi sesi |
| 7 | Penguncian akun brute-force | `ACCOUNT_LOCKOUT` (dalam new_value) | Saat failed_login_attempts >= 5 |
| 8 | Eskalasi operasi kritis | `UPDATE` | Retur DP, retur ATK, pengeluaran > Rp 500.000, restore database |
| 9 | Eksekusi backup database | `INSERT` | Rekam nama file, ukuran, status |
| 10 | Eksekusi restore database | `UPDATE` | Rekam sumber file restore |

### 3.3. Format Pencatatan JSON (Sumber: Security Design Bab 7.3)

**Contoh `UPDATE` pada tabel kasbon:**
```json
// old_value
{"id": 3, "pengguna_id": 4, "sisa_utang": 500000.0000, "status_kasbon": "AKTIF"}

// new_value
{"id": 3, "pengguna_id": 4, "sisa_utang": 0.0000, "status_kasbon": "LUNAS"}
```

**Contoh `ACCESS_DENIED`:**
```json
// old_value
{"attempted_menu": "MENU-M4-002", "args": {"bulan": "05-2026"}}

// new_value
{"status": "ILLEGAL_ACCESS_PREVENTED", "resolved_action": "TERMINATED"}
```

**Contoh `LOGIN_SUCCESS`:**
```json
// old_value
null

// new_value
{"status": "SUCCESS"}
```

### 3.4. Klasifikasi Sensitivitas Data (Sumber: Security Design Bab 2.3)

| Level | Klasifikasi | Tabel | Aturan Audit |
|:--:|---|---|---|
| 1 | **Sangat Sensitif** | `pinjaman_bank`, `pinjaman_kerabat`, `payroll`, `system_configs`, `backup_logs`, `aset` | Setiap akses (SELECT) DAN modifikasi WAJIB dicatat |
| 2 | **Sensitif** | `transaksi`, `pengeluaran`, `audit_logs`, `shift_handover`, `utang_supplier`, `limbah_produksi`, `stock_opname` | Setiap modifikasi (INSERT/UPDATE/DELETE) WAJIB dicatat |
| 3 | **Operasional** | Sisa 15 tabel lainnya | Dilindungi parameterized query, TIDAK wajib audit trail |

### 3.5. Deteksi Anomali dan Fraud (Sumber: Security Design Bab 7.4)

Sistem harus mendukung query analisis anomali berikut dari data `audit_logs`:
- **Selisih Kas Rekonsiliasi**: 3 shift berturut-turut selisih > Rp 10.000
- **Frekuensi Retur Abnormal**: > 5 kali eskalasi retur dalam 1 minggu
- **Login Gagal Berulang**: > 10 kali gagal login dari 1 IP dalam 1 jam

### 3.6. Retensi dan Pemeliharaan Log (Sumber: Security Design Bab 7.5)

- Data log audit wajib disimpan **minimal 12 bulan**
- Log > 12 bulan dapat dipindahkan ke arsip file dingin (cold storage) ZIP terenkripsi
- Utilitas purging dijalankan awal bulan oleh `pemilik`

### 3.7. Signature Fungsi Target (Sumber: Module Structure Bab 7.4)

```python
def log_audit_trail(
    pengguna_id: int,
    action_type: str,
    target_table: str,
    old_val: dict | None,
    new_val: dict | None,
    cabang_id: int,
    db_connection: Any
) -> None:
    """Menyimpan berkas log audit terstruktur JSON ke MySQL."""
```

### 3.8. Standar Kode yang WAJIB Dipatuhi (Sumber: Coding Standard v1.2)

- `[WAJIB]` Paradigma FP murni — tanpa `class`
- `[WAJIB]` Parameterized query `%s` bindings — **DILARANG** f-string SQL
- `[WAJIB]` Result Pattern menggunakan NamedTuple
- `[WAJIB]` Type hints PEP 484 pada semua fungsi publik
- `[WAJIB]` Docstring PEP 257 Google Style pada setiap fungsi
- `[WAJIB]` Penamaan `snake_case` untuk fungsi dan variabel
- `[WAJIB]` Header module docstring di baris teratas file
- `[WAJIB]` Presisi `Decimal('0.0001')` untuk nilai numerik keuangan dalam JSON
- `[WAJIB]` Format error `ERR-DB-XXX` untuk kegagalan database
- `[WAJIB]` System logging via modul standar Python `logging`

---

## 4. Batasan dan Cakupan (Scope)

### 4.1. ✅ DALAM Cakupan (In-Scope)

- [ ] Menyempurnakan fungsi `log_audit_trail()` di `middleware/audit_logger.py` sesuai spesifikasi Security Design Bab 7 dan Bab 12.
- [ ] Menambahkan kolom `ip_address` pada INSERT query audit (saat ini belum ada di implementasi).
- [ ] Menambahkan fungsi helper `build_audit_json()` untuk membangun snapshot JSON dari data baris database secara konsisten.
- [ ] Menambahkan fungsi helper `get_client_ip()` untuk mengambil IP address terminal aktif secara lintas-OS.
- [ ] Menambahkan validasi `action_type` agar hanya menerima 4 nilai valid (`INSERT`, `UPDATE`, `DELETE`, `ACCESS_DENIED`) plus 4 tipe otentikasi (`LOGIN_SUCCESS`, `LOGIN_FAILED`, `LOGOUT`, `ACCOUNT_LOCKOUT`).
- [ ] Menambahkan fungsi `query_audit_logs()` untuk membaca data log audit dengan filter berdasarkan: pengguna_id, action_type, target_table, rentang tanggal, dan cabang_id.
- [ ] Menambahkan fungsi `detect_fraud_anomalies()` untuk deteksi 3 pola anomali fraud (Bab 7.4).
- [ ] Menambahkan fungsi `purge_old_audit_logs()` untuk membersihkan log > 12 bulan ke arsip.
- [ ] Memastikan integrasi pemanggilan `log_audit_trail()` sudah benar di seluruh titik yang **sudah ada** (`logic/auth_handler.py`, `middleware/rbac_guard.py`, `cli/menu_configs.py`).
- [ ] Menambahkan unit test untuk semua fungsi baru di `tests/test_audit_logger.py`.
- [ ] Menambahkan docstring dan header module yang memenuhi standar Coding Standard v1.2.

### 4.2. ❌ DI LUAR Cakupan (Out-of-Scope)

- **TIDAK** mengubah skema DDL tabel `audit_logs` di database (tabel sudah ada dan sudah benar).
- **TIDAK** mengubah signature fungsi `log_audit_trail()` yang sudah dipanggil di modul lain.
- **TIDAK** mengubah file `middleware/auth_jwt.py`, `middleware/rbac_guard.py`, atau `logic/auth_handler.py` kecuali untuk memperbaiki parameter pemanggilan `log_audit_trail()` jika ada yang belum sesuai.
- **TIDAK** menambahkan menu CLI baru (menu tampilan audit trail akan di-issue terpisah).
- **TIDAK** mengubah tabel database lain selain penulisan ke `audit_logs`.

### 4.3. ⚠️ Zona Bahaya — Feature Lain yang TIDAK BOLEH Tersenggol

> [!CAUTION]
> Feature berikut sudah berjalan dan sudah memiliki test suite. Jangan sampai implementasi issue ini merusak salah satu dari feature ini:

| Feature | File yang Berkaitan | Test Suite |
|---|---|---|
| Login/Logout bcrypt + JWT | `logic/auth_handler.py`, `middleware/auth_jwt.py` | `tests/test_login_bcrypt.py`, `tests/test_logout.py`, `tests/test_jwt_session.py` |
| Rate Limiting Lockout | `logic/auth_handler.py` | `tests/test_rate_limiting_login.py`, `tests/test_unit_rate_limiting_lockout.py` |
| RBAC Guard | `middleware/rbac_guard.py` | `tests/test_rbac_security.py` |
| Config Cache & Menu Configs | `db/config_cache.py`, `cli/menu_configs.py` | `tests/test_config_cache.py`, `tests/unit/logic/test_m10_runtime_config.py` |

**Cara memastikan tidak merusak**: Setelah implementasi, jalankan **seluruh** test suite yang ada dan pastikan semua PASS.

---

## 5. Alur Pengerjaan dan Checklist Implementasi

### FASE 0: Persiapan dan Pembacaan Referensi

- [ ] Baca file `docs/sdlc/03_design/06_security_design.md` — fokus pada **Bab 7** (Desain Audit Trail), **Bab 2.3** (Klasifikasi Sensitivitas), dan **Bab 12** (Pseudocode FP)
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — fokus pada **Bab 10.6** (Aturan Audit Trail), **Bab 10.8** (System Logging), **Bab 2** (FP Murni), **Bab 8.7** (Result Pattern), **Bab 9** (Parameterized Query)
- [ ] Baca file `docs/sdlc/04_implementation/03_module_structure.md` — fokus pada **Bab 7.4** (middleware/audit_logger.py)
- [ ] Baca file `docs/sdlc/03_design/01_database_schema.sql` — fokus pada **TABEL 25 audit_logs** (sekitar baris 584-602)
- [ ] Baca file `middleware/audit_logger.py` — pahami implementasi saat ini
- [ ] Baca file `logic/auth_handler.py` — pahami bagaimana `log_audit_trail()` sudah dipanggil
- [ ] Baca file `middleware/rbac_guard.py` — pahami bagaimana `log_audit_trail()` sudah dipanggil pada `ACCESS_DENIED`
- [ ] Baca file `cli/menu_configs.py` — pahami bagaimana `log_audit_trail()` sudah dipanggil untuk perubahan config
- [ ] Baca file `db/query_builder.py` — pahami wrapper ACID transaction yang tersedia
- [ ] Rangkum seluruh temuan ke dalam catatan internal sebelum mulai menulis kode

### FASE 1: Penyempurnaan Fungsi Utama `log_audit_trail()`

**Target file**: `middleware/audit_logger.py`

- [ ] **Backup mental**: Catat state kode awal sebelum modifikasi.
- [ ] Perbarui header module docstring sesuai template Coding Standard Bab 6.4:
  ```python
  """
  Nama Modul: audit_logger.py
  Deskripsi: Middleware pencatatan audit trail terstruktur format JSON ke tabel
             audit_logs MySQL. Merekam old_value dan new_value untuk setiap
             modifikasi data sensitif (Modul M.7).
  Author: [Nama Pengembang / AI Asisten]
  Tanggal: [YYYY-MM-DD]
  """
  ```
- [ ] Tambahkan import yang diperlukan:
  ```python
  import json
  import logging
  import socket
  import platform
  from collections import namedtuple
  from decimal import Decimal
  from typing import Any
  ```
- [ ] Definisikan konstanta valid action types:
  ```python
  VALID_ACTION_TYPES = (
      'INSERT', 'UPDATE', 'DELETE', 'ACCESS_DENIED',
      'LOGIN_SUCCESS', 'LOGIN_FAILED', 'LOGOUT', 'ACCOUNT_LOCKOUT',
  )
  ```
- [ ] Definisikan NamedTuple Result Pattern:
  ```python
  Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
  ```
- [ ] Buat fungsi helper `_serialize_value_to_json(value: dict | None) -> str | None`:
  - Konversi dictionary Python ke string JSON
  - Handle `None` → return `None`
  - Handle `Decimal` → konversi ke `float` untuk kompatibilitas JSON
  - Handle `datetime` → konversi ke ISO format string
  - Tambahkan docstring PEP 257

- [ ] Buat fungsi helper `get_client_ip() -> str`:
  - Ambil hostname lokal via `socket.gethostname()`
  - Resolve ke IP via `socket.gethostbyname()`
  - Fallback ke `'127.0.0.1'` jika gagal
  - Kompatibel lintas-OS (Windows & Debian)
  - Tambahkan docstring PEP 257

- [ ] Refactor fungsi utama `log_audit_trail()`:
  - Tambahkan **validasi parameter** `action_type` terhadap `VALID_ACTION_TYPES`
  - Tambahkan **parameter `ip_address`** ke INSERT query:
    ```sql
    INSERT INTO audit_logs
    (pengguna_id, action_type, target_table, old_value, new_value, ip_address, cabang_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ```
  - Gunakan `_serialize_value_to_json()` untuk konversi `old_val` dan `new_val`
  - Gunakan `get_client_ip()` untuk mendapatkan IP address secara otomatis
  - Ubah return type dari `None` ke `Result` agar konsisten dengan Result Pattern
  - Tambahkan handling `cursor.close()` di blok `finally`
  - Tambahkan system logging via `_logger.info()` pada sukses dan `_logger.error()` pada gagal
  - Tambahkan docstring PEP 257 lengkap (Args, Returns, Raises, Example)

> [!WARNING]
> **JANGAN mengubah nama fungsi `log_audit_trail` atau urutan parameter yang sudah ada** (pengguna_id, action_type, target_table, old_val, new_val, cabang_id, db_connection). Boleh menambahkan parameter baru dengan **default value** agar backward-compatible.

### FASE 2: Fungsi Query Pembacaan Audit Log

**Target file**: `middleware/audit_logger.py` (tambahkan di bawah fungsi `log_audit_trail`)

- [ ] Buat fungsi `query_audit_logs()`:
  ```python
  def query_audit_logs(
      db_connection: Any,
      cabang_id: int,
      pengguna_id: int | None = None,
      action_type: str | None = None,
      target_table: str | None = None,
      tanggal_mulai: str | None = None,
      tanggal_akhir: str | None = None,
      limit: int = 100
  ) -> Result:
  ```
  - Query menggunakan parameterized `%s` — **DILARANG** f-string SQL
  - Filter opsional: pengguna_id, action_type, target_table, rentang tanggal
  - Default limit 100 baris untuk mencegah overload memori
  - Return `Result(True, list[dict], None)` pada sukses
  - Return `Result(False, None, 'ERR-DB-xxx')` pada gagal
  - Tambahkan docstring PEP 257 lengkap

### FASE 3: Fungsi Deteksi Anomali Fraud

**Target file**: `middleware/audit_logger.py` (tambahkan di bawah fungsi `query_audit_logs`)

- [ ] Buat fungsi `detect_kas_anomaly()`:
  - Query tabel `shift_handover` untuk mencari 3 shift berturut-turut dengan `selisih > 10000`
  - Return daftar kasir_id dan detail shift yang anomali
  - Gunakan parameterized query `%s`

- [ ] Buat fungsi `detect_retur_anomaly()`:
  - Query tabel `audit_logs` untuk mencari akun kasir dengan eskalasi retur > 5x dalam 7 hari
  - Filter `action_type = 'UPDATE'` dan `target_table = 'transaksi'` dan `new_value` mengandung `"status_pembayaran": "RETUR"` atau `"status_pembayaran": "BATAL"`
  - Return daftar kasir mencurigakan

- [ ] Buat fungsi `detect_login_brute_force()`:
  - Query tabel `audit_logs` untuk mencari > 10 `LOGIN_FAILED` dari 1 IP dalam 1 jam
  - Return daftar IP dan jumlah percobaan

- [ ] Buat fungsi wrapper `detect_fraud_anomalies()`:
  ```python
  def detect_fraud_anomalies(db_connection: Any, cabang_id: int) -> Result:
  ```
  - Memanggil ketiga fungsi deteksi di atas
  - Menggabungkan hasilnya ke dalam satu dictionary terstruktur
  - Return `Result(True, {...}, None)`

### FASE 4: Fungsi Pemeliharaan dan Retensi Log

**Target file**: `middleware/audit_logger.py` (tambahkan di bawah fungsi deteksi)

- [ ] Buat fungsi `count_audit_logs()`:
  - Menghitung total baris audit_logs per cabang
  - Return jumlah baris sebagai integer

- [ ] Buat fungsi `purge_old_audit_logs()`:
  ```python
  def purge_old_audit_logs(
      db_connection: Any,
      cabang_id: int,
      retention_months: int = 12
  ) -> Result:
  ```
  - Hitung tanggal cutoff: `NOW() - INTERVAL {retention_months} MONTH`
  - **SEBELUM menghapus**: Hitung jumlah baris yang akan dihapus (SELECT COUNT)
  - **SEBELUM menghapus**: Log aktivitas purging ke `audit_logs` sendiri (meta-audit)
  - DELETE baris yang lebih tua dari cutoff
  - Return `Result(True, {'purged_count': n}, None)`

> [!NOTE]
> Fungsi purging ini hanya menghapus dari database. Ekspor ke file ZIP cold storage akan dihandle oleh utilitas `utils/backup.py` di issue terpisah.

### FASE 5: Verifikasi Integrasi dengan Modul Existing

**Target file**: Periksa — JANGAN ubah kecuali ada yang salah

- [ ] Periksa `logic/auth_handler.py`:
  - Verifikasi bahwa `log_audit_trail()` dipanggil dengan parameter yang benar pada:
    - Login berhasil → `action_type='LOGIN_SUCCESS'`, `target_table='pengguna'`
    - Login gagal → `action_type='LOGIN_FAILED'`, `target_table='pengguna'`
    - Account lockout → `action_type='ACCOUNT_LOCKOUT'`, `target_table='pengguna'`
    - Logout → `action_type='LOGOUT'`, `target_table='pengguna'`
  - Jika ada ketidaksesuaian antara `action_type` yang digunakan vs `VALID_ACTION_TYPES`, sesuaikan **nilai string action_type di pemanggil** agar cocok
  - **JANGAN** mengubah logika login/logout yang sudah berfungsi

- [ ] Periksa `middleware/rbac_guard.py`:
  - Verifikasi bahwa `log_audit_trail()` dipanggil dengan `action_type='ACCESS_DENIED'`
  - Verifikasi format `old_value` berisi `{"attempted_menu": "...", "role": "..."}`
  - **JANGAN** mengubah logika RBAC guard yang sudah berfungsi

- [ ] Periksa `cli/menu_configs.py`:
  - Verifikasi bahwa `log_audit_trail()` dipanggil saat `system_configs` diubah
  - Pastikan `old_value` dan `new_value` berisi data konfigurasi sebelum dan sesudah perubahan
  - **JANGAN** mengubah logika menu configs yang sudah berfungsi

- [ ] Buat catatan tertulis (komentar `# TODO:` atau file catatan):
  - Daftar modul yang **BELUM** mengintegrasikan `log_audit_trail()` tapi **SEHARUSNYA** (berdasarkan Bab 7.2 Security Design). Misalnya: operasi CRUD pada tabel Sangat Sensitif dan Sensitif yang belum ada.
  - Tandai sebagai **backlog** untuk issue berikutnya.

### FASE 6: Penulisan Unit Test

**Target file**: `tests/test_audit_logger.py` (file BARU)

- [ ] Buat file baru `tests/test_audit_logger.py` dengan header module
- [ ] Tulis test case menggunakan `pytest` dan `unittest.mock`:

**Test Cases Wajib:**

| No | Nama Test | Deskripsi | Assertion |
|:--:|---|---|---|
| 1 | `test_log_audit_trail_insert_success` | Pencatatan INSERT berhasil ke DB | Verifikasi `cursor.execute()` dipanggil dengan query dan parameter benar |
| 2 | `test_log_audit_trail_update_with_old_new_value` | Pencatatan UPDATE dengan old_value dan new_value JSON | Verifikasi `json.dumps()` menghasilkan string JSON valid |
| 3 | `test_log_audit_trail_delete_old_value_only` | Pencatatan DELETE (new_value = None) | Verifikasi parameter new_value = NULL |
| 4 | `test_log_audit_trail_access_denied` | Pencatatan ACCESS_DENIED | Verifikasi action_type = 'ACCESS_DENIED' dan format old_value benar |
| 5 | `test_log_audit_trail_invalid_action_type` | Reject action_type yang tidak valid (misal: 'HACK') | Verifikasi return Result(False, ...) atau raise ValueError |
| 6 | `test_log_audit_trail_db_error_handling` | Simulasi exception database saat INSERT | Verifikasi tidak crash, return error Result, dan logging.error dipanggil |
| 7 | `test_log_audit_trail_none_values` | old_val=None dan new_val=None | Verifikasi JSON NULL dikirim ke DB |
| 8 | `test_log_audit_trail_decimal_serialization` | old_val berisi Decimal('500000.0000') | Verifikasi Decimal terkonversi ke JSON tanpa error |
| 9 | `test_serialize_value_to_json_happy_path` | Konversi dict → JSON string | Verifikasi output adalah string JSON valid |
| 10 | `test_serialize_value_to_json_none` | Input None → return None | Verifikasi return None |
| 11 | `test_get_client_ip_returns_string` | Fungsi mengembalikan IP string | Verifikasi return type str dan format IP valid |
| 12 | `test_query_audit_logs_basic` | Query tanpa filter opsional | Verifikasi SQL SELECT benar dan limit diterapkan |
| 13 | `test_query_audit_logs_with_filters` | Query dengan filter pengguna_id dan tanggal | Verifikasi WHERE clause dinamis benar |
| 14 | `test_detect_fraud_anomalies_no_anomaly` | Database bersih tanpa anomali | Verifikasi return Result(True, {...}, None) dengan list kosong |
| 15 | `test_purge_old_audit_logs_success` | Hapus log > 12 bulan | Verifikasi DELETE query benar dan count dikembalikan |

- [ ] Pastikan semua mock menggunakan `unittest.mock.patch` sesuai pola yang sudah ada di test suite lain
- [ ] Pastikan **TIDAK** ada koneksi database nyata dalam unit test (semua di-mock)

### FASE 7: Validasi dan Quality Assurance

- [ ] Jalankan `python -m pytest tests/test_audit_logger.py -v` — pastikan semua test PASS
- [ ] Jalankan **SELURUH** test suite existing untuk memastikan tidak ada regresi:
  ```bash
  python -m pytest tests/ -v --tb=short
  ```
- [ ] Pastikan hasil: **SEMUA test PASS**, **TIDAK ADA test yang FAIL**
- [ ] Periksa ulang file `middleware/audit_logger.py`:
  - Apakah semua fungsi publik memiliki docstring PEP 257?
  - Apakah semua fungsi publik memiliki type hints lengkap?
  - Apakah semua query SQL menggunakan `%s` parameterized?
  - Apakah tidak ada `class` di file ini?
  - Apakah penamaan fungsi dan variabel menggunakan `snake_case`?
  - Apakah konstanta menggunakan `UPPER_SNAKE_CASE`?
  - Apakah baris kode tidak melebihi 120 karakter?
- [ ] Lakukan review keamanan:
  - Apakah ada risiko SQL injection? (Jawaban harus: **TIDAK**)
  - Apakah error handling sudah menangkap semua exception tanpa crash? (Jawaban harus: **YA**)
  - Apakah data sensitif ter-log di system logging? (Jawaban harus: **TIDAK** — jangan log password/token)

---

## 6. Instruksi Tambahan Spesifik Audit Trail

### 6.1. Penanganan Tipe Data Khusus dalam JSON

Kolom `old_value` dan `new_value` di MySQL bertipe **JSON**. Python `json.dumps()` tidak bisa meng-handle tipe data khusus secara default. Buat custom JSON encoder:

```python
import json
from decimal import Decimal
from datetime import datetime, date

class AuditJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder yang mendukung Decimal dan datetime."""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)
```

Atau gunakan pendekatan FP murni (tanpa class) sebagai alternatif:
```python
def _audit_json_serializer(obj):
    """Serializer kustom untuk json.dumps() agar mendukung Decimal dan datetime."""
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Tipe {type(obj)} tidak bisa diserialisasi ke JSON")
```

> [!TIP]
> Karena Coding Standard mewajibkan FP murni, **gunakan pendekatan fungsi `_audit_json_serializer`** dengan parameter `default=_audit_json_serializer` pada `json.dumps()`, **bukan** class `AuditJSONEncoder`. Kecuali custom encoder berada di layer utility (`utils/`), maka class diperbolehkan.

### 6.2. Atomicity Pencatatan Audit

- Pencatatan audit trail **TIDAK BOLEH** gagal secara diam-diam (silent failure) tanpa logging.
- Jika `INSERT INTO audit_logs` gagal, **WAJIB** log error ke system logger Python (`logging.error()`).
- Pencatatan audit **TIDAK BOLEH** menyebabkan rollback transaksi bisnis utama. Gunakan `try-except` terpisah.
- Artinya: jika transaksi kasir berhasil COMMIT tapi pencatatan audit gagal, transaksi tetap sah TAPI error audit harus ter-log.

### 6.3. Thread Safety dan Connection Handling

- Setiap pemanggilan `log_audit_trail()` harus membuat cursor sendiri.
- Cursor harus ditutup di blok `finally`.
- Jangan menyimpan cursor atau connection di variabel global.

### 6.4. Kompatibilitas IP Address Lintas-OS

- **Windows 11**: `socket.gethostbyname(socket.gethostname())` biasanya mengembalikan IP LAN.
- **Linux Debian 12**: Sama, tetapi mungkin mengembalikan `127.0.1.1` jika hostname di-resolve ke localhost.
- Fallback ke `'127.0.0.1'` jika resolusi gagal.

---

## 7. Data Kosong atau Tidak Tersedia

> [!WARNING]
> Berikut adalah data/informasi yang **tidak ditemukan** atau **belum terdefinisi** di dokumen referensi SDLC dan perlu ditindaklanjuti:

| No | Data yang Kosong/Tidak Ada | Impact | Rekomendasi Tindak Lanjut |
|:--:|---|---|---|
| 1 | **Format detail `old_value` untuk `LOGIN_SUCCESS`** — Security Design Bab 7.3 hanya menunjukkan `new_value: {"status": "SUCCESS"}` tetapi tidak mendefinisikan secara spesifik apakah `old_value` harus berisi data login attempts sebelumnya atau `null`. | Rendah | Gunakan `null` untuk `old_value` pada LOGIN_SUCCESS (konsisten dengan pseudocode Bab 12). |
| 2 | **Spesifikasi detail `new_value` untuk `LOGOUT`** — tidak ada contoh JSON eksplisit untuk event LOGOUT di Bab 7.3. | Rendah | Gunakan format: `{"status": "LOGOUT", "session_duration_seconds": X}` jika duration tersedia, atau `{"status": "LOGOUT"}` jika tidak. |
| 3 | **Daftar lengkap modul yang sudah mengintegrasikan `log_audit_trail()`** — tidak ada tracking terpusat di dokumen SDLC mana saja modul yang sudah vs belum integrasi. | Sedang | Buat catatan backlog di akhir issue ini. Daftar integrasi diidentifikasi di Fase 5. |
| 4 | **Threshold waktu retention log** — Security Design menyebut 12 bulan tetapi tidak menjelaskan apakah ini berdasarkan `action_timestamp` atau `created_at`. | Rendah | Gunakan `action_timestamp` karena itu mewakili waktu kejadian aktual (bukan waktu insert yang bisa berbeda karena delay). |
| 5 | **Format cold storage export** — Bab 7.5 menyebut "arsip file dingin ZIP terenkripsi" tapi detail implementasi di-handle oleh `utils/backup.py`, bukan scope issue ini. | Rendah | Tandai sebagai out-of-scope, serahkan ke issue backup/restore. |

---

## 8. Kaidah Kualitas dan Kelengkapan

> [!IMPORTANT]
> Ikuti kaidah berikut agar hasil implementasi **tidak dipertanyakan kelengkapannya** dan **tidak menghambat feature lain**:

1. **Kelengkapan Docstring**: Setiap fungsi publik **WAJIB** memiliki docstring yang menjelaskan Args, Returns, Raises, dan Example. Jangan ada fungsi tanpa docstring.

2. **Kelengkapan Type Hints**: Setiap parameter dan return value **WAJIB** memiliki type hints. Gunakan `|` untuk union type (contoh: `dict | None`), bukan `Optional`.

3. **Kelengkapan Test**: Setiap fungsi publik yang baru dibuat **WAJIB** memiliki minimal 2 test case (happy path dan error path).

4. **Kelengkapan Logging**: Setiap branch error di `except` **WAJIB** memanggil `_logger.error()` dengan pesan deskriptif.

5. **Kelengkapan Validasi**: Setiap parameter input **WAJIB** divalidasi tipenya sebelum diproses. Jangan asumsikan input selalu benar.

6. **Konsistensi dengan Existing Code**: Ikuti pola dan gaya kode yang sudah ada di `logic/auth_handler.py` dan `middleware/rbac_guard.py`. Jangan memperkenalkan pola baru yang inkonsisten.

7. **Backward Compatibility**: Jangan mengubah signature fungsi yang sudah dipanggil di modul lain tanpa menambahkan default value.

---

## 9. Instruksi Perilaku Pelaksana

1. **Kerjakan dengan rapi dan bersih.** Jangan tergesa-gesa. Baca seluruh referensi terlebih dahulu sebelum menulis satu baris kode pun.

2. **Jangan asumsikan.** Jika ada informasi yang ambigu di referensi, tandai sebagai `# TODO: [Klarifikasi Dibutuhkan]` di kode dan lanjutkan dengan pendekatan paling aman (defensif).

3. **Jangan lakukan halusinasi.** Jangan mengarang nama kolom database, nama fungsi, atau konstanta yang tidak ada di referensi. Selalu verifikasi terhadap DDL SQL dan source code existing.

4. **Jangan mengubah yang tidak perlu diubah.** Jika sebuah file tidak disebutkan dalam scope, JANGAN sentuh file itu.

5. **Test dahulu, commit kemudian.** Jalankan semua test setelah setiap fase selesai, bukan hanya di akhir.

6. **Komunikasikan temuan.** Jika menemukan bug atau inkonsistensi di kode existing saat pengerjaan, catat sebagai komentar `# FIXME:` dan laporkan, JANGAN perbaiki sendiri di luar scope.

---

## 10. Referensi Silang dan Traceability

| Kebutuhan | ID Referensi | Lokasi Dokumen |
|---|---|---|
| Audit Trail JSON granular | SRS-F-031 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| Deteksi Fraud kasir | SRS-F-034 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| Desain Audit Trail | Security Design Bab 7 | `docs/sdlc/03_design/06_security_design.md` |
| Pseudocode FP write_audit_log | Security Design Bab 12 | `docs/sdlc/03_design/06_security_design.md` |
| Aturan Audit Trail Logging | Coding Standard Bab 10.6 | `docs/sdlc/04_implementation/01_coding_standard.md` |
| Spesifikasi audit_logger.py | Module Structure Bab 7.4 | `docs/sdlc/04_implementation/03_module_structure.md` |
| Skema tabel audit_logs | Database Schema Tabel 25 | `docs/sdlc/03_design/01_database_schema.sql` |
| Matriks akses audit_logs | ACM Bab 6.6 | `docs/sdlc/02_analysis/06_access_control_matrix.md` |
| Hak akses modul M.7 | ACM Bab 4 (M.7) | `docs/sdlc/02_analysis/06_access_control_matrix.md` |

---

## 11. Definition of Done (Kriteria Selesai)

Issue ini dianggap **selesai** jika dan hanya jika:

- [ ] File `middleware/audit_logger.py` telah diperbarui dengan semua fungsi sesuai Fase 1–4.
- [ ] Fungsi `log_audit_trail()` mendukung pencatatan `ip_address` dan validasi `action_type`.
- [ ] Fungsi `query_audit_logs()` dapat memfilter log berdasarkan 5 kriteria.
- [ ] Fungsi `detect_fraud_anomalies()` dapat mendeteksi 3 pola anomali.
- [ ] Fungsi `purge_old_audit_logs()` dapat membersihkan log lama > 12 bulan.
- [ ] File test `tests/test_audit_logger.py` memiliki minimal 15 test case dan semua PASS.
- [ ] **SELURUH** test suite existing (`tests/`) PASS tanpa regresi.
- [ ] Semua fungsi publik memiliki docstring PEP 257 dan type hints PEP 484 lengkap.
- [ ] Tidak ada `class` di `middleware/audit_logger.py` (FP murni).
- [ ] Tidak ada f-string SQL di seluruh file (parameterized `%s` only).
- [ ] Catatan backlog integrasi modul lain sudah didokumentasikan.

---

*Dokumen ini disusun berdasarkan analisis mendalam terhadap 7 dokumen referensi SDLC AbuCom v1.2 dan source code existing pada tanggal 2026-06-07.*
