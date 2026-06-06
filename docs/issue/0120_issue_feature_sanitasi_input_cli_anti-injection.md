---
issue      : #0120
judul      : Feature Sanitasi Input CLI Anti-Injection
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
tanggal    : 2026-06-07
status     : Open
prioritas  : High
modul      : M.7 — Keamanan, Audit Trail & Hak Akses
assignee   : [Junior Programmer / AI Coding Agent]
---

# Issue #0120 — Feature Sanitasi Input CLI Anti-Injection

---

## 1. Persona Pelaksana

> **Persona yang WAJIB diadopsi oleh pelaksana issue ini:**
>
> **Kamu adalah Senior Defensive Security Engineer & Input Validation Specialist** — seorang ahli keamanan defensif yang sangat teliti, metodis, dan tidak pernah terburu-buru. Kamu memiliki pengalaman mendalam dalam proteksi sistem CLI berbasis terminal terhadap serangan injection (SQL Injection, ANSI Escape Injection, Command Injection, dan Unicode Abuse). Kamu sangat memahami paradigma Functional Programming (FP) murni Python 3.14.2+, presisi desimal `Decimal(15,4)`, dan sistem keamanan berlapis (Defense in Depth). Kamu WAJIB menulis kode yang bersih, rapi, terdokumentasi lengkap (PEP 257 docstring), dan patuh 100% terhadap seluruh standar SDLC AbuCom tanpa mengorbankan fitur lain yang sudah berjalan.

---

## 2. Dokumen Referensi Utama

Berikut adalah daftar file referensi yang **WAJIB** dibaca secara menyeluruh dan diekstrak informasinya sebelum memulai implementasi:

| No | Dokumen Referensi | Path Relatif | Alasan Pemilihan |
|:---:|---|---|---|
| **R-01** | Security Design v1.2 | `docs/sdlc/03_design/06_security_design.md` | **SSoT (Single Source of Truth)** utama untuk seluruh spesifikasi sanitasi input, model ancaman (THR-005), proteksi input CLI (Bab 6.4), parameterized queries (Bab 3.4), dan kode error keamanan (Bab 10). |
| **R-02** | CLI Interaction Flow v1.2 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Referensi alur interaksi input pengguna di seluruh 44 Use Case, konvensi sanitasi kontrol ASCII (Bab 2.4), konvensi validasi regex (Bab 2.4), dan format error visual (Bab 2.5). |
| **R-03** | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` | Standar penulisan kode FP murni (Bab 2.2), sanitasi input CLI (Bab 10.5), parameterized queries (Bab 9.1-9.2), Result Pattern (Bab 2.2.6), type hints (Bab 7), dan penamaan (Bab 3). |
| **R-04** | Module Structure v1.2 | `docs/sdlc/04_implementation/03_module_structure.md` | Pemetaan file `logic/safety_validator.py` (Bab 5.5), dependensi impor, dan arsitektur berlapis 4-layer. |
| **R-05** | Tech Stack Decision v1.1 | `docs/sdlc/01_planning/04_tech_stack_decision.md` | Parameter sanitasi input CLI (Bab 8.8), requirements.txt, dan spesifikasi Python 3.14.2+. |
| **R-06** | Test Plan v1.2 | `docs/sdlc/05_testing/01_test_plan.md` | Skenario pengujian sanitasi input CLI (Bab 5.5), pengujian SQL Injection (Bab 5.3), dan target code coverage ≥ 90%. |
| **R-07** | Software Requirements Spec v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | Kebutuhan fungsional M.7 Keamanan (SRS-F-030), standar kode error, dan kebutuhan non-fungsional keamanan. |
| **R-08** | narasi.txt | `docs/sdlc/narasi.txt` | Konteks bisnis toko percetakan, kebutuhan keamanan dari sudut pandang pemilik usaha (Bab: Keamanan — Audit Trail), serta spesifikasi teknis Python 3.14.2+ dan library wajib. |

---

## 3. Rangkuman Detail Data Relevan dari Dokumen Referensi

Berikut adalah **seluruh** data spesifik yang WAJIB diekstrak dan dipahami dari dokumen referensi sebelum implementasi. **Jangan lewatkan satu pun detail kecil**.

### 3.1. Dari Security Design v1.2 (R-01)

#### 3.1.1. Model Ancaman Relevan (Bab 2.2)
- **THR-005** — Penyerangan lokal via input form CLI menggunakan untaian karakter injeksi SQL (`' OR '1'='1`).
  - **Dampak**: Kerusakan basis data, bypass login, kebocoran tabel keuangan.
  - **Mitigasi Wajib**: Parameterized Queries (`%s` bindings), pelarangan f-string SQL, input length bounds, sanitasi terminal ASCII.

#### 3.1.2. Proteksi Input Aplikasi (Bab 6.4)
Empat lapis proteksi input yang WAJIB diimplementasikan:
1. **ASCII Control Characters Filter**: Karakter kontrol ASCII di bawah `\x20` (termasuk escape code ANSI `\x1b`) harus dibuang otomatis dari input keyboard terminal.
2. **Length Bounds Validation**: Membatasi panjang karakter input formulir di memori Python:
   - Nama pengguna (username): ≤ 50 karakter
   - Nomor WhatsApp: ≤ 20 karakter
   - *(Implementor wajib menambahkan length bounds untuk seluruh field input lainnya sesuai constraint DDL database)*
3. **Regex Format Validation**: Masukan WhatsApp disaring menggunakan regex `^08[0-9]{8,11}$` sebelum query SQL diproses.
4. **Anti-SQL Injection Parameterized**: Melarang penggunaan f-string, concatenations, atau dynamic formatting `%` pada instruksi SQL program, wajib menggunakan placeholder `%s`.

#### 3.1.3. Risiko Keamanan (Bab 11.1)
- **RSK-SEC-004** — Percobaan injeksi perintah SQL Injection lokal via CLI.
  - Probabilitas: 2/5, Dampak: 5/5, Skor: **10/25** (Tinggi)
  - Mitigasi: Wajib Parameterized Query `%s`, larangan f-string SQL.

#### 3.1.4. Kode Error Relevan (Bab 10)
| Kode Error | Pesan | Pemicu |
|---|---|---|
| `ERR-VAL-001` | `ERR-VAL-001: Input Salah: ID barang tidak valid atau kuantitas harus diisi berupa angka positif!` | Input non-numerik atau ID tidak terdaftar |
| `ERR-VAL-044` | `ERR-VAL-044: Konvalidasi Gagal: Kata sandi baru minimal harus 8 karakter...` | Password gagal validasi |
| `ERR-AUTH-001` | `ERR-AUTH-001: Kredensial tidak valid. Silakan coba kembali!` | Username/password salah (termasuk input injeksi yang diterima sebagai literal) |

### 3.2. Dari CLI Interaction Flow v1.2 (R-02)

#### 3.2.1. Konvensi Input & Validasi (Bab 2.4)
1. **Sanitasi Kontrol ASCII**: Menghapus byte escape ANSI berbahaya (karakter kontrol < `\x20` seperti `\x1b`) untuk melindungi konsol dari injeksi kode visual terminal.
2. **Password Masking**: Input kata sandi wajib ditangkap menggunakan modul `getpass` Python (tanpa memancarkan visual ketikan ke layar kasir).
3. **Fixed-Point Decimal**: Input nominal Rupiah dan persediaan bahan baku desimal divalidasi ke format `decimal.Decimal` Python sebelum dikirim ke database.
4. **Validasi Regex**: Format tanggal divalidasi `^\d{4}-\d{2}-\d{2}$` (YYYY-MM-DD), dan nomor telepon di CRM disanitasi menggunakan regex pembersih nomor WhatsApp lokal.

#### 3.2.2. Konvensi Pesan Error (Bab 2.5)
Format wajib: `[RED] ⛔ ERR-[KATEGORI]-[NOMOR]: [Pesan deskriptif fungsional berbahasa Indonesia]`

Kategori kode error yang relevan:
- `ERR-VAL-xxx`: Kegagalan validasi input data, format parsing desimal/tanggal salah.
- `ERR-AUTH-xxx`: Kegagalan login, otorisasi eskalasi supervisor, lockout brute-force.

#### 3.2.3. Konvensi Navigasi (Bab 2.2)
- Tombol `0`: Kembali ke menu setingkat di atas.
- Pola Konfirmasi `[Y/N]`: Untuk operasi kritis (case-insensitive).
- Pola Enter Kosong: Default value atau ulangi prompt jika mandatory.

### 3.3. Dari Coding Standard v1.2 (R-03)

#### 3.3.1. Standar Sanitasi Input CLI (Bab 10.5)
> `[WAJIB]` Bersihkan ketikan masukan dari keyboard CLI dengan membuang karakter kontrol biner di bawah byte `\x20` (seperti `\x1b` ANSI escape) untuk mencegah perusakan visual terminal. (Ref: Security Design Bab 6.4)

#### 3.3.2. Standar Parameterized Queries (Bab 9.1-9.2)
> `[WAJIB]` Seluruh pemicuan query dinamis SQL **MUST** menggunakan placeholder bind resmi `%s` bawaan driver MySQL.
> `[DILARANG]` Dilarang keras menggabungkan variabel program ke instruksi query SQL menggunakan *f-string*, operator format `%`, atau fungsi `.format()`.

#### 3.3.3. Standar Result Pattern (Bab 2.2.6)
Semua fungsi validasi wajib mengembalikan `NamedTuple Result` berisi `is_success`, `data`, `error_msg`.

#### 3.3.4. Standar FP Murni (Bab 2.2)
- Tanpa `class` di alur bisnis utama
- Pure functions: input sama → output sama
- Imutabilitas via `NamedTuple`
- Type hints lengkap (PEP 484, Python 3.14+ style: `list[...]`, `dict[...]`, pipe `|`)

#### 3.3.5. Standar Penamaan (Bab 3)
- Fungsi: `snake_case` format `verb_noun` (contoh: `sanitasi_input_cli`, `validasi_format_tanggal`)
- NamedTuple: `PascalCase` (contoh: `ValidationStatus`, `SanitizedInput`)
- Konstanta: `UPPER_SNAKE_CASE` (contoh: `MAX_USERNAME_LENGTH = 50`)
- Variabel: `snake_case` deskriptif

#### 3.3.6. Standar Docstring (Bab 6.2)
Template PEP 257 Google Style wajib pada setiap fungsi publik, dengan Args, Returns, Raises, dan Example.

### 3.4. Dari Module Structure v1.2 (R-04)

#### 3.4.1. File Target Utama: `logic/safety_validator.py` (Bab 5.5)
- **Tanggung Jawab**: Sanitasi input terminal CLI (filter ASCII di bawah `\x20`), pencegahan peretasan control character, password strength validator (panjang >= 8, uppercase/lowercase, numerik, spesial), lockout rate limiting check.
- **Modul Fungsional**: M.7 Keamanan & Hak Akses.
- **Dependensi Impor**: `None` (Pure standalone utility).
- **Aturan FP Murni**: Imutabel NamedTuple `ValidationStatus`.

### 3.5. Dari Test Plan v1.2 (R-06)

#### 3.5.1. Skenario Pengujian Sanitasi Input CLI (Bab 5.5)
> 1. Pada kolom input nama barang baru, ketikkan karakter escape terminal ANSI: `\x1b[31mBarang Palsu`.
> 2. Verifikasi logic parser memangkas kode visual tersebut secara programatis biner di Python sebelum disimpan, sehingga nama barang tersimpan steril di database sebagai `'Barang Palsu'`.

#### 3.5.2. Skenario Pengujian SQL Injection (Bab 5.3)
> 1. Pada layar login terminal CLI username, ketikkan string injeksi: `' OR '1'='1`. Ketik sandi sembarang.
> 2. Verifikasi sistem menangkap string murni sebagai nama username literal terfilter, menolak login aman, dan menampilkan `ERR-AUTH-001`.
> 3. Pemeriksaan baris kode: Pastikan 100% database query di program menggunakan placeholder driver `%s`.

#### 3.5.3. Target Code Coverage
Unit test coverage logika bisnis inti wajib ≥ 90%.

### 3.6. Dari narasi.txt (R-08)
- Sistem CLI berbasis terminal, Python 3.14.2+, paradigma Functional Programming.
- Library wajib: `mysql-connector-python`, `python-dotenv`, `bcrypt`, `pyjwt`.
- Sistem berjalan offline di LAN lokal toko percetakan.
- Input berasal dari keyboard terminal kasir fisik — ancaman utama adalah staf internal atau orang yang memiliki akses fisik ke terminal.

---

## 4. Batasan, Cakupan, dan Alur Pengerjaan

### 4.1. Cakupan Pengerjaan (In-Scope)

Issue ini mencakup implementasi **LIMA** komponen sanitasi input berikut:

| No | Komponen Sanitasi | Deskripsi | File Target |
|:---:|---|---|---|
| **S-01** | ASCII Control Character Filter | Membuang karakter kontrol ASCII < `\x20` (termasuk `\x1b` ANSI escape) dari seluruh input CLI | `logic/safety_validator.py` |
| **S-02** | Length Bounds Validation | Memvalidasi panjang maksimum input berdasarkan constraint kolom database (username ≤ 50, WhatsApp ≤ 20, nama barang ≤ 100, alamat ≤ 200, dsb.) | `logic/safety_validator.py` |
| **S-03** | Regex Format Validation | Validasi format input spesifik: WhatsApp `^08[0-9]{8,11}$`, tanggal `^\d{4}-\d{2}-\d{2}$`, email, numerik positif, desimal positif | `logic/safety_validator.py` |
| **S-04** | Decimal Input Validation | Validasi dan konversi input nominal Rupiah dan kuantitas stok ke `decimal.Decimal` dengan presisi 4 desimal `ROUND_HALF_UP` | `logic/safety_validator.py` |
| **S-05** | SQL Injection Audit (Kode Review) | Verifikasi bahwa **100%** query SQL di seluruh codebase menggunakan parameterized `%s`, tidak ada f-string/concatenation SQL | Seluruh file `db/`, `logic/`, `middleware/` |
| **S-06** | Integrasi Sanitasi ke Presentation Layer | Memanggil fungsi sanitasi di setiap titik `input()` pada seluruh file `cli/` | `cli/__init__.py`, `cli/dashboard.py`, `cli/menu_*.py` |
| **S-07** | Unit Test Sanitasi | Menulis test suite komprehensif untuk seluruh fungsi sanitasi | `tests/test_sanitasi_input.py` |

### 4.2. Di Luar Cakupan (Out-of-Scope)

- ❌ Modifikasi skema database (DDL) — tidak boleh mengubah tabel/kolom apapun.
- ❌ Modifikasi logika RBAC (`middleware/rbac_guard.py`) — sudah ada dan berjalan.
- ❌ Modifikasi logika otentikasi (`middleware/auth_jwt.py`, `logic/auth_handler.py`) — sudah ada.
- ❌ Modifikasi logika bisnis keuangan (`logic/bom_hpp.py`, `logic/smart_payroll.py`, `logic/financial_engine.py`).
- ❌ Penambahan library/dependency baru di `requirements.txt`.

### 4.3. Alur Pengerjaan

```
[FASE 1] Pembacaan & Ekstraksi Referensi
         ↓
[FASE 2] Implementasi Fungsi Sanitasi di logic/safety_validator.py
         ↓
[FASE 3] Audit SQL Injection di Seluruh Codebase
         ↓
[FASE 4] Integrasi Sanitasi ke Presentation Layer (cli/)
         ↓
[FASE 5] Penulisan Unit Test (tests/test_sanitasi_input.py)
         ↓
[FASE 6] Eksekusi Test & Verifikasi
         ↓
[FASE 7] Penandaan Data Kosong / Gap
```

---

## 5. Instruksi Proteksi Feature Lain

> [!CAUTION]
> **JANGAN** menyentuh, mengubah, atau merusak fitur lain yang sudah berjalan. Pastikan hal-hal berikut:

- [ ] **JANGAN** mengubah signature atau return type fungsi yang sudah ada di `logic/safety_validator.py` (`sanitasi_input_cli` dan `validasi_kekuatan_sandi`). Kamu boleh **memperluas** (menambahkan fungsi baru), tetapi TIDAK BOLEH mengubah fungsi yang sudah ada secara breaking.
- [ ] **JANGAN** menghapus atau mengubah komentar/docstring yang sudah ada di file manapun yang tidak terkait perubahan ini.
- [ ] **JANGAN** mengubah file `middleware/rbac_guard.py`, `middleware/auth_jwt.py`, `middleware/audit_logger.py`, `logic/auth_handler.py`, `logic/pengguna.py`, `logic/bom_hpp.py`, `logic/smart_payroll.py`, `logic/financial_engine.py` — kecuali untuk menambahkan pemanggilan fungsi sanitasi pada titik input.
- [ ] **JANGAN** mengubah skema database (`schema.sql`), file `.env`, atau `requirements.txt`.
- [ ] Setelah implementasi, jalankan **seluruh** test suite yang sudah ada (`pytest tests/`) untuk memastikan tidak ada regresi.
- [ ] Pastikan pemanggilan `sanitasi_input_cli()` yang sudah ada di codebase tetap berfungsi seperti sebelumnya (backward compatible).

---

## 6. Instruksi Kualitas Pengerjaan

> [!IMPORTANT]
> **Kerjakan dengan RAPI, BERSIH, TIDAK TERGESA-GESA, dan TIDAK BURU-BURU.** Kualitas maksimal adalah prioritas utama.

1. **Teliti setiap baris**: Periksa ulang setiap fungsi sebelum melanjutkan ke fungsi berikutnya. Jangan copy-paste tanpa pemahaman.
2. **Docstring lengkap**: Setiap fungsi publik WAJIB memiliki docstring PEP 257 Google Style dengan Args, Returns, Raises, dan Example.
3. **Type hints lengkap**: Setiap parameter dan return value WAJIB memiliki anotasi tipe data (PEP 484, Python 3.14+ style).
4. **Test setiap fungsi**: Setiap fungsi yang ditambahkan WAJIB memiliki minimal 3 test case (positif, negatif, boundary).
5. **Kode konsisten**: Ikuti pola dan gaya kode yang sudah ada di `logic/safety_validator.py`.
6. **Jangan hardcode**: Konstanta length bounds harus didefinisikan sebagai `UPPER_SNAKE_CASE` konstanta, bukan angka ajaib inline.

---

## 7. Instruksi Kelengkapan

> [!WARNING]
> **Pastikan kelengkapan pengerjaan ini TIDAK PERNAH dipertanyakan.** Jangan sampai ada yang terlewat.

Checklist kelengkapan yang WAJIB dipenuhi sebelum issue ini dinyatakan selesai:

- [ ] Seluruh 4 lapis proteksi input (ASCII filter, length bounds, regex validation, decimal validation) telah diimplementasikan.
- [ ] Seluruh file `cli/` telah diintegrasikan dengan fungsi sanitasi.
- [ ] Audit SQL injection telah dilakukan dan dilaporkan hasilnya.
- [ ] Unit test telah ditulis dengan code coverage ≥ 90% untuk `logic/safety_validator.py`.
- [ ] Seluruh test suite lama tetap PASS (tidak ada regresi).
- [ ] Seluruh fungsi baru memiliki docstring PEP 257 lengkap dan type hints.
- [ ] Data kosong/gap telah ditandai dengan format `# DATA_GAP: [deskripsi]`.

---

## 8. Instruksi Penandaan Data Kosong

Jika dalam proses implementasi ditemukan data yang **kosong, tidak tersedia, atau ambigu** pada file referensi (misalnya: panjang maksimum field tertentu tidak tercantum di DDL, format regex untuk field tertentu tidak didefinisikan, dsb.), maka:

1. **Tandai** dalam kode dengan komentar format: `# DATA_GAP: [deskripsi detail gap]`
2. **Catat** dalam laporan di bagian akhir file test sebagai komentar blok.
3. **JANGAN** menebak atau mengasumsikan nilai — gunakan nilai konservatif sementara (misal: max length = 255) dan tandai sebagai gap.

---

## 9. Instruksi Tambahan Khusus Anti-Injection

Berikut adalah instruksi tambahan yang spesifik untuk ciri khas issue sanitasi input anti-injection:

### 9.1. Whitelist vs Blacklist Approach
- **GUNAKAN** pendekatan **whitelist** (hanya mengizinkan karakter yang valid) sebisa mungkin, bukan blacklist (memblokir karakter tertentu).
- Untuk field numerik: hanya izinkan digit `0-9`, titik desimal `.`, dan tanda minus `-` di awal.
- Untuk field nama: izinkan huruf alfabet, spasi, titik, koma, dan tanda hubung.

### 9.2. Defense in Depth — Prinsip Berlapis
Sanitasi input BUKAN satu-satunya pertahanan. Arsitektur keamanan AbuCom menerapkan pertahanan berlapis:
1. **Layer 1 (Presentation)**: Sanitasi input CLI → filter karakter kontrol, length bounds.
2. **Layer 2 (Business Logic)**: Validasi format dan tipe data → regex, decimal parsing.
3. **Layer 3 (Data Access)**: Parameterized queries → `%s` placeholder, larangan f-string SQL.
4. **Layer 4 (Database)**: CHECK constraint, foreign key, NOT NULL — sudah ada di DDL.

### 9.3. Penanganan Edge Cases
Implementasi WAJIB menangani edge case berikut:
- Input string kosong (`""`) — kembalikan string kosong, jangan error.
- Input hanya whitespace (`"   "`) — setelah strip, kembalikan string kosong.
- Input sangat panjang (> 10.000 karakter) — potong ke batas maksimum, jangan crash.
- Input mengandung null byte (`\x00`) — buang null byte.
- Input mengandung karakter Unicode valid (huruf Indonesia, simbol Rupiah) — JANGAN buang, hanya buang control characters.
- Input mengandung tab (`\t`) — tab ada di bawah `\x20`, akan dibuang oleh filter. (**Catatan**: `\n` dan `\r` juga harus dibuang karena < `\x20`).

### 9.4. Konsistensi dengan Kode Existing
Fungsi `sanitasi_input_cli()` yang sudah ada di `logic/safety_validator.py` saat ini hanya membuang karakter < `\x20`. Ini sudah sesuai spesifikasi dasar. Issue ini memperluas cakupan dengan menambahkan fungsi-fungsi validasi **tambahan** yang berdiri sendiri di file yang sama.

---

## 10. Checklist Implementasi Tahap demi Tahap

### FASE 1: Pembacaan & Ekstraksi Referensi

- [ ] Baca file `docs/sdlc/03_design/06_security_design.md` — ekstrak Bab 2.2 (THR-005), Bab 6.4 (Proteksi Input), Bab 10 (Kode Error), Bab 11.1 (RSK-SEC-004).
- [ ] Baca file `docs/sdlc/03_design/04_cli_interaction_flow.md` — ekstrak Bab 2.4 (Konvensi Input & Validasi), Bab 2.5 (Format Error).
- [ ] Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — ekstrak Bab 2.2 (FP), Bab 3 (Naming), Bab 9.1-9.2 (SQL), Bab 10.5 (Sanitasi).
- [ ] Baca file `docs/sdlc/04_implementation/03_module_structure.md` — ekstrak Bab 5.5 (safety_validator.py).
- [ ] Baca file `docs/sdlc/05_testing/01_test_plan.md` — ekstrak Bab 5.3 (SQL Injection), Bab 5.5 (Sanitasi CLI).
- [ ] Baca file `docs/sdlc/03_design/01_database_schema.sql` — ekstrak seluruh constraint `VARCHAR(n)` untuk menentukan length bounds setiap field.
- [ ] Baca file `logic/safety_validator.py` — pahami kode existing yang sudah ada, jangan ubah.
- [ ] Baca file `cli/__init__.py` — pahami pola input existing di login flow.
- [ ] Baca file `cli/dashboard.py` — pahami pola input di dashboard navigation.
- [ ] Baca seluruh file `cli/menu_*.py` — identifikasi semua titik `input()` yang perlu diintegrasikan sanitasi.

---

### FASE 2: Implementasi Fungsi Sanitasi di `logic/safety_validator.py`

#### Langkah 2.1 — Tambahkan Import dan Konstanta

- [ ] Buka file `logic/safety_validator.py` untuk diedit.
- [ ] Tambahkan import `from decimal import Decimal, ROUND_HALF_UP, InvalidOperation` di bagian atas (jika belum ada).
- [ ] Tambahkan import `import datetime` di bagian atas (jika belum ada).
- [ ] Definisikan konstanta length bounds berikut berdasarkan DDL schema database:

```python
# ============================================================
# KONSTANTA LENGTH BOUNDS INPUT CLI
# (Ref: Security Design Bab 6.4 — Length Bounds Validation)
# (Ref: Database Schema DDL — VARCHAR constraint)
# ============================================================
MAX_USERNAME_LENGTH = 50
MAX_PASSWORD_LENGTH = 128
MAX_WHATSAPP_LENGTH = 20
MAX_NAMA_BARANG_LENGTH = 100
MAX_NAMA_PENGGUNA_LENGTH = 100
MAX_ALAMAT_LENGTH = 200
MAX_DESKRIPSI_LENGTH = 500
MAX_CATATAN_LENGTH = 500
MAX_GENERIC_INPUT_LENGTH = 255
MAX_KODE_LENGTH = 20
MAX_MEMO_LENGTH = 1000
```

> **Catatan**: Nilai-nilai di atas WAJIB diverifikasi terhadap DDL `docs/sdlc/03_design/01_database_schema.sql`. Jika ada perbedaan, gunakan nilai dari DDL dan tandai perbedaan dengan `# DATA_GAP: diverifikasi dari DDL`.

#### Langkah 2.2 — Tambahkan NamedTuple Baru

- [ ] Tambahkan `SanitizedInput` NamedTuple untuk validasi yang lebih komprehensif:

```python
SanitizedInput = namedtuple('SanitizedInput', ['is_valid', 'cleaned_value', 'error_msg'])
```

#### Langkah 2.3 — Implementasi Fungsi `validasi_panjang_input()`

- [ ] Tulis fungsi `validasi_panjang_input()` dengan spesifikasi berikut:

```python
def validasi_panjang_input(raw_input: str, max_length: int, field_name: str) -> SanitizedInput:
    """Memvalidasi panjang input tidak melebihi batas maksimum field.

    (Ref: Security Design Bab 6.4 — Length Bounds Validation)

    Args:
        raw_input (str): String input yang sudah disanitasi karakter kontrol.
        max_length (int): Batas maksimum karakter yang diizinkan.
        field_name (str): Nama field untuk pesan error deskriptif.

    Returns:
        SanitizedInput: NamedTuple berisi is_valid (bool), cleaned_value (str),
                        dan error_msg (str | None).

    Example:
        >>> validasi_panjang_input('kasir_01', 50, 'username')
        SanitizedInput(is_valid=True, cleaned_value='kasir_01', error_msg=None)
        >>> validasi_panjang_input('x' * 51, 50, 'username')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-LEN: ...')
    """
```

- [ ] Logika: jika `len(raw_input) > max_length`, return error `ERR-VAL-LEN: Input {field_name} melebihi batas maksimum {max_length} karakter!`.
- [ ] Jika valid, return `SanitizedInput(True, raw_input, None)`.

#### Langkah 2.4 — Implementasi Fungsi `validasi_format_whatsapp()`

- [ ] Tulis fungsi `validasi_format_whatsapp()` dengan regex `^08[0-9]{8,11}$`:

```python
def validasi_format_whatsapp(nomor_wa: str) -> SanitizedInput:
    """Memvalidasi format nomor WhatsApp Indonesia.

    (Ref: Security Design Bab 6.4 — Regex Format Validation)
    Format valid: Diawali '08', diikuti 8-11 digit angka.

    Args:
        nomor_wa (str): String nomor WhatsApp mentah.

    Returns:
        SanitizedInput: NamedTuple validasi format nomor WhatsApp.

    Example:
        >>> validasi_format_whatsapp('081234567890')
        SanitizedInput(is_valid=True, cleaned_value='081234567890', error_msg=None)
        >>> validasi_format_whatsapp('0812')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-WA: ...')
    """
```

- [ ] Gunakan `re.match(r'^08[0-9]{8,11}$', nomor_wa)`.
- [ ] Jika gagal, return error `ERR-VAL-WA: Format nomor WhatsApp tidak valid! Gunakan format 08xxxxxxxxxx (10-13 digit).`.

#### Langkah 2.5 — Implementasi Fungsi `validasi_format_tanggal()`

- [ ] Tulis fungsi `validasi_format_tanggal()` dengan regex `^\d{4}-\d{2}-\d{2}$`:

```python
def validasi_format_tanggal(tanggal_str: str) -> SanitizedInput:
    """Memvalidasi format tanggal YYYY-MM-DD dan keabsahan kalender.

    (Ref: CLI Interaction Flow Bab 2.4 — Validasi Regex)

    Args:
        tanggal_str (str): String tanggal mentah dari input CLI.

    Returns:
        SanitizedInput: NamedTuple validasi format tanggal.

    Example:
        >>> validasi_format_tanggal('2026-05-29')
        SanitizedInput(is_valid=True, cleaned_value='2026-05-29', error_msg=None)
        >>> validasi_format_tanggal('2026-13-45')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-DATE: ...')
    """
```

- [ ] Validasi 2 tahap: (1) regex format, (2) `datetime.datetime.strptime()` untuk keabsahan kalender.
- [ ] Jika gagal, return error `ERR-VAL-DATE: Format tanggal tidak valid! Gunakan format YYYY-MM-DD (contoh: 2026-01-31).`.

#### Langkah 2.6 — Implementasi Fungsi `validasi_input_numerik_positif()`

- [ ] Tulis fungsi untuk validasi input integer positif (ID barang, kuantitas, dsb.):

```python
def validasi_input_numerik_positif(raw_input: str, field_name: str) -> SanitizedInput:
    """Memvalidasi input sebagai bilangan bulat positif (integer > 0).

    (Ref: CLI Interaction Flow Bab 5.1 — Input ID Barang & Qty)

    Args:
        raw_input (str): String input mentah dari CLI.
        field_name (str): Nama field untuk pesan error deskriptif.

    Returns:
        SanitizedInput: NamedTuple validasi, cleaned_value berisi string angka.

    Example:
        >>> validasi_input_numerik_positif('102', 'ID Barang')
        SanitizedInput(is_valid=True, cleaned_value='102', error_msg=None)
        >>> validasi_input_numerik_positif('-5', 'ID Barang')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-NUM: ...')
    """
```

- [ ] Logika: coba `int(raw_input)`, pastikan > 0.
- [ ] Jika gagal, return error `ERR-VAL-NUM: Input {field_name} harus berupa angka bulat positif!`.

#### Langkah 2.7 — Implementasi Fungsi `validasi_input_desimal_positif()`

- [ ] Tulis fungsi untuk validasi input desimal positif (nominal Rupiah, kuantitas stok):

```python
def validasi_input_desimal_positif(raw_input: str, field_name: str) -> SanitizedInput:
    """Memvalidasi dan mengonversi input ke Decimal positif presisi 4 desimal.

    (Ref: CLI Interaction Flow Bab 2.4 — Fixed-Point Decimal)
    (Ref: Coding Standard Bab 2.4 — Decimal-First Policy)

    Args:
        raw_input (str): String input nominal dari CLI.
        field_name (str): Nama field untuk pesan error deskriptif.

    Returns:
        SanitizedInput: NamedTuple validasi, cleaned_value berisi string Decimal.

    Example:
        >>> validasi_input_desimal_positif('100000', 'Nominal Rupiah')
        SanitizedInput(is_valid=True, cleaned_value='100000.0000', error_msg=None)
        >>> validasi_input_desimal_positif('abc', 'Nominal Rupiah')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-DEC: ...')
    """
```

- [ ] Logika: coba `Decimal(raw_input).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)`, pastikan > 0.
- [ ] Tangkap `InvalidOperation` untuk input non-numerik.
- [ ] Jika gagal, return error `ERR-VAL-DEC: Input {field_name} harus berupa angka desimal positif!`.

#### Langkah 2.8 — Implementasi Fungsi `validasi_konfirmasi_yn()`

- [ ] Tulis fungsi untuk validasi input konfirmasi Y/N:

```python
def validasi_konfirmasi_yn(raw_input: str) -> SanitizedInput:
    """Memvalidasi input konfirmasi biner Y/N (case-insensitive).

    (Ref: CLI Interaction Flow Bab 2.2 — Pola Konfirmasi Aksi Destruktif)

    Args:
        raw_input (str): String input konfirmasi dari CLI.

    Returns:
        SanitizedInput: NamedTuple validasi, cleaned_value berisi 'Y' atau 'N'.

    Example:
        >>> validasi_konfirmasi_yn('y')
        SanitizedInput(is_valid=True, cleaned_value='Y', error_msg=None)
        >>> validasi_konfirmasi_yn('maybe')
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-YN: ...')
    """
```

- [ ] Logika: `raw_input.strip().upper()` harus `in ('Y', 'N')`.
- [ ] Jika gagal, return error `ERR-VAL-YN: Input konfirmasi tidak valid! Ketik Y atau N.`.

#### Langkah 2.9 — Implementasi Fungsi `validasi_pilihan_menu()`

- [ ] Tulis fungsi untuk validasi input pilihan menu numerik:

```python
def validasi_pilihan_menu(raw_input: str, min_val: int, max_val: int) -> SanitizedInput:
    """Memvalidasi input pilihan menu numerik dalam rentang yang diizinkan.

    (Ref: CLI Interaction Flow Bab 2.2 — Hotkey Numerik)

    Args:
        raw_input (str): String input pilihan menu dari CLI.
        min_val (int): Nilai minimum pilihan yang valid (biasanya 0).
        max_val (int): Nilai maksimum pilihan yang valid.

    Returns:
        SanitizedInput: NamedTuple validasi, cleaned_value berisi string angka.

    Example:
        >>> validasi_pilihan_menu('3', 0, 10)
        SanitizedInput(is_valid=True, cleaned_value='3', error_msg=None)
        >>> validasi_pilihan_menu('99', 0, 10)
        SanitizedInput(is_valid=False, cleaned_value='', error_msg='ERR-VAL-MENU: ...')
    """
```

- [ ] Jika gagal, return error `ERR-VAL-MENU: Pilihan menu tidak valid! Masukkan angka {min_val}-{max_val}.`.

#### Langkah 2.10 — Implementasi Fungsi Wrapper `sanitasi_dan_validasi_input()`

- [ ] Tulis fungsi wrapper utama yang menggabungkan sanitasi + length bounds:

```python
def sanitasi_dan_validasi_input(raw_input: str, max_length: int, field_name: str) -> SanitizedInput:
    """Menjalankan sanitasi karakter kontrol DAN validasi panjang input secara berurutan.

    Pipeline: raw_input → sanitasi_input_cli() → strip() → validasi_panjang_input()

    (Ref: Security Design Bab 6.4 — Defense in Depth Input Validation)

    Args:
        raw_input (str): String mentah dari input keyboard CLI.
        max_length (int): Batas maksimum karakter setelah sanitasi.
        field_name (str): Nama field untuk pesan error deskriptif.

    Returns:
        SanitizedInput: NamedTuple berisi hasil sanitasi dan validasi.

    Example:
        >>> sanitasi_dan_validasi_input('\\x1bNama Barang', 100, 'Nama Barang')
        SanitizedInput(is_valid=True, cleaned_value='Nama Barang', error_msg=None)
    """
```

- [ ] Logika pipeline:
  1. Panggil `sanitasi_input_cli(raw_input)` — buang karakter kontrol.
  2. `.strip()` — buang whitespace di awal/akhir.
  3. Panggil `validasi_panjang_input(cleaned, max_length, field_name)` — cek panjang.
  4. Return hasilnya.

---

### FASE 3: Audit SQL Injection di Seluruh Codebase

- [ ] Buka file `db/query_builder.py` — periksa bahwa SEMUA query menggunakan `%s` placeholder.
- [ ] Buka file `db/db_connector.py` — periksa tidak ada f-string SQL.
- [ ] Buka file `logic/auth_handler.py` — periksa query login menggunakan `%s`.
- [ ] Buka file `logic/pengguna.py` — periksa query CRUD pengguna menggunakan `%s`.
- [ ] Buka file `middleware/audit_logger.py` — periksa query audit log menggunakan `%s`.
- [ ] Buka file `middleware/auth_jwt.py` — periksa query JWT/session menggunakan `%s`.
- [ ] Buka file `middleware/rbac_guard.py` — periksa query RBAC menggunakan `%s`.
- [ ] Buka file `cli/menu_configs.py` — periksa query config menggunakan `%s`.
- [ ] Buka file `cli/menu_transaksi.py` — periksa semua query menggunakan `%s`.
- [ ] Buka file `cli/menu_inventaris.py` — periksa semua query menggunakan `%s`.
- [ ] Buka file `cli/menu_ppob_service.py` — periksa semua query menggunakan `%s`.
- [ ] Buka file `cli/menu_sdm_finansial.py` — periksa semua query menggunakan `%s`.
- [ ] Catat hasil audit: jumlah file diperiksa, jumlah query ditemukan, jumlah yang PATUH `%s`, jumlah yang MELANGGAR (jika ada).
- [ ] Jika ditemukan pelanggaran f-string/concatenation SQL, **perbaiki** langsung dan catat dalam komentar `# FIX-0120: Diubah dari f-string ke parameterized query %s`.

---

### FASE 4: Integrasi Sanitasi ke Presentation Layer

#### Langkah 4.1 — Integrasi ke `cli/__init__.py`

- [ ] Buka file `cli/__init__.py`.
- [ ] Tambahkan import: `from logic.safety_validator import sanitasi_input_cli, sanitasi_dan_validasi_input, MAX_USERNAME_LENGTH`.
- [ ] Pada baris `username = input("Username: ").strip()` (sekitar baris 81):
  - Ubah menjadi:
    ```python
    raw_username = input("Username: ")
    username = sanitasi_input_cli(raw_username).strip()
    ```
- [ ] Pastikan input username juga divalidasi panjangnya (≤ 50 karakter). Jika lebih, tampilkan error dan ulangi prompt.

#### Langkah 4.2 — Integrasi ke `cli/dashboard.py`

- [ ] Buka file `cli/dashboard.py`.
- [ ] Tambahkan import: `from logic.safety_validator import sanitasi_input_cli`.
- [ ] Pada baris `pilihan = input("Pilih Menu: ").strip()` (sekitar baris 141):
  - Ubah menjadi:
    ```python
    raw_pilihan = input("Pilih Menu: ")
    pilihan = sanitasi_input_cli(raw_pilihan).strip()
    ```
- [ ] Pada baris `konfirmasi = input("Apakah Anda yakin ingin logout? [Y/N]: ").strip().lower()` (sekitar baris 148):
  - Ubah menjadi:
    ```python
    raw_konfirmasi = input("Apakah Anda yakin ingin logout? [Y/N]: ")
    konfirmasi = sanitasi_input_cli(raw_konfirmasi).strip().lower()
    ```

#### Langkah 4.3 — Integrasi ke `cli/menu_configs.py`

- [ ] Buka file `cli/menu_configs.py`.
- [ ] Tambahkan import `sanitasi_input_cli` dari `logic.safety_validator`.
- [ ] Terapkan `sanitasi_input_cli()` pada SETIAP titik `input()` di file ini.

#### Langkah 4.4 — Integrasi ke `cli/menu_transaksi.py`

- [ ] Buka file `cli/menu_transaksi.py`.
- [ ] Tambahkan import `sanitasi_input_cli` dari `logic.safety_validator`.
- [ ] Terapkan `sanitasi_input_cli()` pada SETIAP titik `input()` di file ini.

#### Langkah 4.5 — Integrasi ke `cli/menu_inventaris.py`

- [ ] Buka file `cli/menu_inventaris.py`.
- [ ] Tambahkan import `sanitasi_input_cli` dari `logic.safety_validator`.
- [ ] Terapkan `sanitasi_input_cli()` pada SETIAP titik `input()` di file ini.

#### Langkah 4.6 — Integrasi ke `cli/menu_ppob_service.py`

- [ ] Buka file `cli/menu_ppob_service.py`.
- [ ] Tambahkan import `sanitasi_input_cli` dari `logic.safety_validator`.
- [ ] Terapkan `sanitasi_input_cli()` pada SETIAP titik `input()` di file ini.

#### Langkah 4.7 — Integrasi ke `cli/menu_sdm_finansial.py`

- [ ] Buka file `cli/menu_sdm_finansial.py`.
- [ ] Tambahkan import `sanitasi_input_cli` dari `logic.safety_validator`.
- [ ] Terapkan `sanitasi_input_cli()` pada SETIAP titik `input()` di file ini.

#### Langkah 4.8 — Integrasi ke `cli/menu_laporan.py`

- [ ] Buka file `cli/menu_laporan.py`.
- [ ] Tambahkan import `sanitasi_input_cli` dari `logic.safety_validator` (jika file memiliki titik `input()`).
- [ ] Terapkan `sanitasi_input_cli()` pada SETIAP titik `input()` di file ini (jika ada).

---

### FASE 5: Penulisan Unit Test

- [ ] Buat file baru `tests/test_sanitasi_input.py`.
- [ ] Tambahkan header modul docstring standar AbuCom.
- [ ] Tulis test cases berikut:

#### Test Group 1: `sanitasi_input_cli()` (Fungsi Existing)

- [ ] `test_sanitasi_input_normal` — Input normal tanpa karakter kontrol → output sama.
- [ ] `test_sanitasi_input_ansi_escape` — Input `\x1b[31mBarang Palsu` → output `[31mBarang Palsu` (hapus `\x1b` saja).

  > **Koreksi penting**: `\x1b` (escape, ord 27) < `\x20` (space, ord 32), jadi dibuang. Tapi `[`, `3`, `1`, `m` semuanya >= `\x20`, jadi TIDAK dibuang. Output yang benar adalah `[31mBarang Palsu`.
  > **Catatan**: Ini sesuai spesifikasi Security Design. Untuk menangani rangkaian ANSI escape sequence secara lengkap (termasuk `[31m`), diperlukan regex tambahan. Implementasikan jika dianggap perlu dan tandai sebagai enhancement.

- [ ] `test_sanitasi_input_null_byte` — Input `Barang\x00Palsu` → output `BarangPalsu` (null byte `\x00` < `\x20`).
- [ ] `test_sanitasi_input_tab_newline` — Input `Barang\t\nPalsu` → output `BarangPalsu` (tab `\x09` dan newline `\x0a` < `\x20`).
- [ ] `test_sanitasi_input_empty` — Input `""` → output `""`.
- [ ] `test_sanitasi_input_unicode_valid` — Input `Kertas HVS Ä4 — Premium` → output sama (karakter Unicode valid tetap dipertahankan).
- [ ] `test_sanitasi_input_sql_injection_string` — Input `' OR '1'='1` → output sama (karakter SQL injection >= `\x20`, TIDAK dibuang oleh sanitasi — pertahanan SQL Injection ada di layer parameterized query).

#### Test Group 2: `validasi_panjang_input()`

- [ ] `test_panjang_input_valid` — Input 10 karakter, max 50 → valid.
- [ ] `test_panjang_input_boundary_exact` — Input tepat 50 karakter, max 50 → valid.
- [ ] `test_panjang_input_exceeded` — Input 51 karakter, max 50 → invalid, error `ERR-VAL-LEN`.
- [ ] `test_panjang_input_empty` — Input kosong, max 50 → valid (empty string masih di bawah batas).

#### Test Group 3: `validasi_format_whatsapp()`

- [ ] `test_whatsapp_valid_10digit` — `'0812345678'` (10 digit) → valid.
- [ ] `test_whatsapp_valid_13digit` — `'0812345678901'` (13 digit) → valid.
- [ ] `test_whatsapp_invalid_prefix` — `'6281234567890'` → invalid (tidak diawali `08`).
- [ ] `test_whatsapp_invalid_short` — `'081234'` (6 digit setelah 08, kurang) → invalid.
- [ ] `test_whatsapp_invalid_alpha` — `'08123abcde'` → invalid.
- [ ] `test_whatsapp_empty` — `''` → invalid.

#### Test Group 4: `validasi_format_tanggal()`

- [ ] `test_tanggal_valid` — `'2026-05-29'` → valid.
- [ ] `test_tanggal_invalid_format` — `'29-05-2026'` → invalid.
- [ ] `test_tanggal_invalid_calendar` — `'2026-13-45'` → invalid (bulan/hari tidak ada).
- [ ] `test_tanggal_invalid_leap` — `'2025-02-29'` → invalid (2025 bukan tahun kabisat).
- [ ] `test_tanggal_empty` — `''` → invalid.

#### Test Group 5: `validasi_input_numerik_positif()`

- [ ] `test_numerik_valid` — `'102'` → valid.
- [ ] `test_numerik_zero` — `'0'` → invalid (harus > 0).
- [ ] `test_numerik_negative` — `'-5'` → invalid.
- [ ] `test_numerik_float` — `'3.14'` → invalid (bukan integer).
- [ ] `test_numerik_alpha` — `'abc'` → invalid.

#### Test Group 6: `validasi_input_desimal_positif()`

- [ ] `test_desimal_valid_integer` — `'100000'` → valid, cleaned `'100000.0000'`.
- [ ] `test_desimal_valid_fraction` — `'0.0025'` → valid, cleaned `'0.0025'`.
- [ ] `test_desimal_zero` — `'0'` → invalid (harus > 0).
- [ ] `test_desimal_negative` — `'-500'` → invalid.
- [ ] `test_desimal_alpha` — `'abc'` → invalid.
- [ ] `test_desimal_boundary_precision` — `'0.00005'` → valid, cleaned `'0.0001'` (ROUND_HALF_UP).

#### Test Group 7: `validasi_konfirmasi_yn()`

- [ ] `test_yn_valid_y` — `'y'` → valid, cleaned `'Y'`.
- [ ] `test_yn_valid_N` — `'N'` → valid, cleaned `'N'`.
- [ ] `test_yn_invalid` — `'maybe'` → invalid.
- [ ] `test_yn_empty` — `''` → invalid.

#### Test Group 8: `validasi_pilihan_menu()`

- [ ] `test_menu_valid` — `'3'`, min=0, max=10 → valid.
- [ ] `test_menu_zero` — `'0'`, min=0, max=10 → valid (kembali).
- [ ] `test_menu_out_of_range` — `'99'`, min=0, max=10 → invalid.
- [ ] `test_menu_alpha` — `'abc'`, min=0, max=10 → invalid.

#### Test Group 9: `sanitasi_dan_validasi_input()`

- [ ] `test_pipeline_normal` — Input normal → sanitasi + validasi panjang sukses.
- [ ] `test_pipeline_control_chars` — Input dengan `\x1b` → karakter kontrol dibuang, lalu panjang divalidasi.
- [ ] `test_pipeline_too_long` — Input > max length setelah sanitasi → error panjang.

---

### FASE 6: Eksekusi Test & Verifikasi

- [ ] Jalankan perintah: `python -m pytest tests/test_sanitasi_input.py -v` — pastikan 100% PASS.
- [ ] Jalankan perintah: `python -m pytest tests/ -v` — pastikan SELURUH test suite lama tetap PASS (tidak ada regresi).
- [ ] Jalankan perintah: `python -m pytest tests/test_sanitasi_input.py --cov=logic/safety_validator --cov-report=term-missing` — pastikan coverage ≥ 90%.
- [ ] Lakukan pengujian manual:
  - [ ] Jalankan `python main.py` (jika database tersedia).
  - [ ] Di prompt username, ketik `\x1b[31mtest` — pastikan karakter kontrol dibuang.
  - [ ] Di prompt username, ketik `' OR '1'='1` — pastikan ditolak sebagai username literal, bukan SQL injection.
  - [ ] Di prompt username, ketik string > 50 karakter — pastikan ditolak atau dipotong.

---

### FASE 7: Penandaan Data Kosong / Gap

- [ ] Periksa apakah ada field input di `cli/` yang belum memiliki definisi `MAX_LENGTH` di DDL.
- [ ] Periksa apakah ada format regex yang belum didefinisikan untuk field tertentu (misalnya: email, alamat).
- [ ] Tandai semua gap yang ditemukan dengan format `# DATA_GAP: [deskripsi]` di dalam kode.
- [ ] Buat ringkasan gap di bagian akhir file `tests/test_sanitasi_input.py` sebagai komentar blok:

```python
# ============================================================
# DATA GAP REPORT — Issue #0120
# ============================================================
# 1. [Contoh] MAX_LENGTH untuk field 'alamat_supplier' tidak ditemukan di DDL.
#    → Menggunakan nilai konservatif 200 karakter sebagai placeholder.
# 2. [Contoh] Regex validasi untuk field 'email' belum didefinisikan di SDLC.
#    → Ditandai untuk tindak lanjut di issue berikutnya.
# ============================================================
```

---

## 11. Ringkasan File yang Akan Diubah/Dibuat

| No | Aksi | File | Deskripsi Perubahan |
|:---:|:---:|---|---|
| 1 | **MODIFY** | `logic/safety_validator.py` | Menambahkan 9 fungsi validasi baru, konstanta length bounds, dan NamedTuple `SanitizedInput`. Fungsi existing TIDAK diubah. |
| 2 | **MODIFY** | `cli/__init__.py` | Integrasi `sanitasi_input_cli()` pada input username dan password. |
| 3 | **MODIFY** | `cli/dashboard.py` | Integrasi `sanitasi_input_cli()` pada input pilihan menu dan konfirmasi logout. |
| 4 | **MODIFY** | `cli/menu_configs.py` | Integrasi `sanitasi_input_cli()` pada seluruh titik `input()`. |
| 5 | **MODIFY** | `cli/menu_transaksi.py` | Integrasi `sanitasi_input_cli()` pada seluruh titik `input()`. |
| 6 | **MODIFY** | `cli/menu_inventaris.py` | Integrasi `sanitasi_input_cli()` pada seluruh titik `input()`. |
| 7 | **MODIFY** | `cli/menu_ppob_service.py` | Integrasi `sanitasi_input_cli()` pada seluruh titik `input()`. |
| 8 | **MODIFY** | `cli/menu_sdm_finansial.py` | Integrasi `sanitasi_input_cli()` pada seluruh titik `input()`. |
| 9 | **MODIFY** | `cli/menu_laporan.py` | Integrasi `sanitasi_input_cli()` pada titik `input()` (jika ada). |
| 10 | **NEW** | `tests/test_sanitasi_input.py` | Suite unit test komprehensif dengan 40+ test cases. |

---

## 12. Kriteria Penerimaan (Acceptance Criteria)

Issue ini dinyatakan **SELESAI** jika dan hanya jika:

- [ ] ✅ Seluruh 9 fungsi validasi baru telah diimplementasikan di `logic/safety_validator.py`.
- [ ] ✅ Seluruh file `cli/` telah diintegrasikan dengan `sanitasi_input_cli()` di setiap titik `input()`.
- [ ] ✅ Audit SQL injection telah dilakukan di seluruh codebase — hasilnya 100% PATUH parameterized `%s`.
- [ ] ✅ File `tests/test_sanitasi_input.py` telah dibuat dengan 40+ test cases.
- [ ] ✅ Coverage `logic/safety_validator.py` ≥ 90%.
- [ ] ✅ Seluruh test suite lama (test yang sudah ada) tetap PASS — 0% regresi.
- [ ] ✅ Seluruh fungsi baru memiliki docstring PEP 257, type hints, dan mengikuti Result Pattern.
- [ ] ✅ Tidak ada `class` dalam kode baru — semuanya FP murni.
- [ ] ✅ Tidak ada library baru ditambahkan ke `requirements.txt`.
- [ ] ✅ Data gap (jika ada) telah ditandai dengan format `# DATA_GAP:`.
- [ ] ✅ Tidak ada fitur lain yang rusak atau berubah perilakunya.

---

## 13. Catatan Penutup

> [!NOTE]
> Issue ini dirancang agar implementor (junior programmer atau AI model yang lebih murah) dapat mengerjakan secara **deterministik** — langkah demi langkah, tanpa perlu menebak atau mengasumsikan apapun. Setiap detail telah diuraikan secara eksplisit. Jika ada yang ambigu, **berhenti dan tandai sebagai DATA_GAP**, jangan berhalusinasi.

---

*Issue dibuat oleh: Claude Opus 4.6 (Thinking) — Senior Defensive Security Engineer Persona*
*Tanggal: 2026-06-07*
*Status: Open*
