# Issue — Feature: Konfigurasi Parameter Bisnis Runtime Dinamis (M.10)

---

## 0. Metadata Issue

| Atribut | Nilai |
|:---|:---|
| **Judul** | Feature: Konfigurasi Parameter Bisnis Runtime Dinamis |
| **Modul** | M.10 — Konfigurasi Sistem Runtime |
| **Prioritas** | High |
| **Status** | Open |
| **Tanggal Dibuat** | 2026-06-05 |
| **Estimasi Kompleksitas** | Medium (1 file CLI baru + 1 file DB baru + 2 file modifikasi) |
| **Branch Git** | `feature/m10-runtime-config` |
| **Derivasi Kebutuhan** | BR-F-38 → SRS-F-040 → UC-040 → MENU-M10-001 |
| **Derivasi Tambahan** | SRS-F-ADD-01 (Startup Init muat config cache) |

---

## 1. Persona Pelaksana (AI / Junior Programmer)

**Persona**: _Senior Python Functional Programming Engineer & CLI Systems Integrator_

**Justifikasi Pemilihan Persona**:
Fitur M.10 Runtime Config menuntut kemampuan teknis yang mencakup:
1.  Penguasaan paradigma **Functional Programming murni** (pure functions, NamedTuple imutabel, Result pattern) — karena seluruh logika bisnis AbuCom dilarang keras menggunakan `class`/OOP.
2.  Pemahaman mendalam terhadap **arsitektur berlapis 4-layer** (cli/ → logic/ → db/ → MySQL) dan aturan dependensi searah.
3.  Kemampuan membangun **config cache reader** yang membaca tabel `system_configs` MySQL saat startup dan menyimpannya ke memori lokal sesi program.
4.  Penguasaan **RBAC Absolute Lockdown** — hanya peran `pemilik` yang boleh mengakses menu ini.
5.  Kemampuan integrasi **ACID transactional update** ke database MySQL menggunakan parameterized queries (`%s` binding).
6.  Pemahaman terhadap format **visual CLI `rich` dan `tabulate`** untuk rendering tabel parameter runtime.

**Instruksi Ketat untuk Persona**:
- `[WAJIB]` Patuh 100% terhadap Coding Standard v1.2 (Ref: `docs/sdlc/04_implementation/01_coding_standard.md`).
- `[WAJIB]` Gunakan paradigma FP murni — dilarang keras mendeklarasikan `class` di alur bisnis.
- `[WAJIB]` Seluruh nominal keuangan menggunakan `decimal.Decimal` presisi 4 desimal dengan `ROUND_HALF_UP`.
- `[WAJIB]` Seluruh query SQL menggunakan parameterized queries `%s` binding — dilarang keras f-string SQL.
- `[WAJIB]` Setiap fungsi publik memiliki docstring PEP 257 Google Style dan type hints PEP 484 lengkap.
- `[WAJIB]` Setiap file `.py` baru memiliki header module docstring standar AbuCom.

---

## 2. Dokumen Referensi yang Dipilih

Berikut adalah daftar dokumen SDLC yang dijadikan acuan utama dalam pengerjaan issue ini, diurutkan berdasarkan relevansi tertinggi:

| No. | Dokumen Referensi | Path Relatif | Justifikasi Pemilihan |
|:---:|:---|:---|:---|
| R-01 | Software Requirements Specification v1.2 | `docs/sdlc/02_analysis/02_software_requirements.md` | **Sumber primer** — Berisi spesifikasi teknis SRS-F-040 (config dinamis tanpa hardcode), SRS-F-ADD-01 (startup init), daftar 13 parameter, aturan validasi, dan error codes. |
| R-02 | Business Requirements Document v1.2 | `docs/sdlc/02_analysis/01_business_requirements.md` | Berisi BR-F-38 (aturan bisnis parameter dinamis), kriteria penerimaan, dan konteks kebutuhan pemilik usaha. |
| R-03 | Database Schema DDL SQL v1.2 | `docs/sdlc/03_design/01_database_schema.sql` | **Sumber DDL** — Definisi fisik tabel `system_configs` (7 kolom, FK ke `cabang`), seed data 13 parameter default, dan constraint. |
| R-04 | CLI Interaction Flow v1.2 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | **Sumber alur UI** — Bab 14.1 berisi langkah-langkah interaksi detail UC-040 (10 langkah), error codes ERR-VAL-038, dan wireframe. |
| R-05 | Module Structure v1.2 | `docs/sdlc/04_implementation/03_module_structure.md` | **Sumber dekomposisi file** — Bab 4.7 (`cli/menu_configs.py`), matriks Module-to-File, SRS-to-File, dan diagram dependensi. |
| R-06 | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` | **Sumber standar kode** — Aturan FP murni, snake_case, Result pattern, ACID wrapper, RBAC decorator, error code catalog. |
| R-07 | System Architecture v1.2 | `docs/sdlc/03_design/03_system_architecture.md` | Konteks arsitektur 4-layer, pola config reader, dan pemetaan tabel per modul. |
| R-08 | Test Plan v1.2 & Test Cases v1.2 | `docs/sdlc/05_testing/01_test_plan.md`, `docs/sdlc/05_testing/02_test_cases.md` | Skenario pengujian M10-TC-001 dan TC-M10-001-01 (dinamis parameter loading & modifikasi). |
| R-09 | ERD Database v1.2 | `docs/sdlc/03_design/02_erd_database.md` | Relasi FK `system_configs.cabang_id` → `cabang.id`, dan klasifikasi tabel Kelompok B. |
| R-10 | Security Design v1.2 | `docs/sdlc/03_design/06_security_design.md` | Klasifikasi sensitivitas tabel `system_configs` = **Sangat Sensitif**, dan aturan audit trail. |
| R-11 | Use Case Diagram v1.2 | `docs/sdlc/02_analysis/03_use_case_diagram.md` | UC-040 (Mengonfigurasi Parameter Bisnis Runtime), aktor `pemilik`, prioritas High. |

> **Catatan**: Dokumen `narasi.txt` (`docs/sdlc/narasi.txt`) **TIDAK** dipilih sebagai referensi untuk issue ini karena seluruh kebutuhan bisnis runtime config telah secara lengkap dan formal dituangkan dalam dokumen BRD (BR-F-38) dan SRS (SRS-F-040). Narasi pemilik hanya berisi pain points umum yang sudah terabsorpsi ke dalam dokumen analisis.

---

## 3. Rangkuman Ekstraksi Detail dari Dokumen Referensi

### 3.1. Dari BRD — BR-F-38 (Ref: R-02, Bab 7.10)

| Atribut | Detail Terekstrak |
|:---|:---|
| **Deskripsi Bisnis** | Sistem harus menyediakan menu pengelolaan parameter regulasi bisnis yang tersimpan secara dinamis di database agar dapat dimodifikasi oleh pemilik usaha tanpa intervensi pembaruan aplikasi. |
| **Aktor** | `pemilik` (eksklusif) |
| **Parameter Dinamis** | Target laba Smart Payroll bulanan (**Rp 15.000.000**), persentase penggajian gaji laba (**25,0%**), limit kasbon karyawan (**Rp 1.000.000**), threshold deposit PPOB (**Rp 150.000**), batas toleransi selisih kas (**Rp 10.000**), dan nilai konversi poin insentif. |
| **Kriteria Penerimaan** | Pemilik mengubah target laba bulanan dari Rp 15.000.000 menjadi Rp 18.000.000 di menu pengaturan, sistem menyimpan konfigurasi baru, dan komputasi payroll langsung mengevaluasi angka tersebut pada siklus berikutnya. |
| **Prioritas** | High |
| **Sumber Inovasi** | Innovation Proposal v1.1 [INV-NEW-09] |

### 3.2. Dari SRS — SRS-F-040 (Ref: R-01, Bab 3.10)

| Atribut | Detail Terekstrak |
|:---|:---|
| **ID Kebutuhan** | SRS-F-040 |
| **Derivasi BRD** | BR-F-38 |
| **Modul** | M.10 — Konfigurasi Sistem Runtime |
| **Prioritas** | High |
| **Aktor** | `pemilik` |
| **Deskripsi Teknis** | Sistem **HARUS** menyimpan dan mengelola seluruh parameter regulasi bisnis di tabel basis data `system_configs` agar dapat dimodifikasi oleh pemilik usaha secara dinamis di menu CLI tanpa merombak kode program. |
| **Input** | `parameter_key` (VARCHAR), `parameter_value` (VARCHAR) |
| **Proses/Logika Bisnis** | (1) Tarik seluruh parameter dinamis bisnis dari tabel `system_configs` saat startup program. (2) Simpan nilai parameter ke cache memori lokal sesi program klien. (3) Jika pemilik mengedit nilai di menu CLI, simpan perubahan ke database dan perbarui cache memori lokal secara sinkron. |
| **Output** | Pembaruan nilai parameter di tabel `system_configs` MySQL. Perubahan perilaku kalkulasi bisnis real-time setelah penyimpanan. |
| **Aturan Validasi** | Akses mengedit parameter regulasi bisnis **HARUS** dikunci rapat hanya untuk level peran `pemilik`. |
| **Error Code** | `ERR-VAL-038`: Format tipe data nilai parameter baru tidak valid! |
| **Ketergantungan** | `SRS-F-031` (RBAC), `SRS-F-ADD-01` (Startup Init) |
| **Catatan Implementasi** | Parameter database disimpan dengan format tipe data asli di kolom database untuk mempermudah casting tipe di Python. |

### 3.3. Dari SRS — SRS-F-ADD-01 (Ref: R-01, Bab 3.11)

| Atribut | Detail Terekstrak |
|:---|:---|
| **Relevansi** | Startup init wajib memuat config cache dari `system_configs` setelah validasi `.env` dan koneksi database berhasil. |
| **Proses Terkait** | Setelah cek `.env` → koneksi DB → **muat `system_configs` ke cache memori** → tampilkan layar login. |

### 3.4. Dari Database Schema — Tabel `system_configs` (Ref: R-03, Tabel 08)

```sql
CREATE TABLE system_configs (
    id              INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    parameter_key   VARCHAR(100) NOT NULL UNIQUE,
    parameter_value VARCHAR(255) NOT NULL,
    tipe_data       VARCHAR(30)  NOT NULL DEFAULT 'VARCHAR',
    deskripsi       TEXT NOT NULL,
    cabang_id       INT NOT NULL DEFAULT 1,
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_system_configs_cabang_id FOREIGN KEY (cabang_id)
        REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
  COMMENT='Parameter runtime regulasi bisnis | Sensitivitas: Sangat Sensitif | Modul: M.10';
```

**Kolom-Kolom Tabel `system_configs`:**

| No. | Nama Kolom | Tipe Data MySQL | Constraint | Deskripsi |
|:---:|:---|:---|:---|:---|
| 1 | `id` | INT AUTO_INCREMENT | PRIMARY KEY | Identifikasi unik baris parameter config. |
| 2 | `parameter_key` | VARCHAR(100) | NOT NULL, UNIQUE | Kunci string parameter regulasi (tanpa spasi). |
| 3 | `parameter_value` | VARCHAR(255) | NOT NULL | Nilai parameter yang dimuat ke program CLI. |
| 4 | `tipe_data` | VARCHAR(30) | NOT NULL, DEFAULT 'VARCHAR' | Penentu pemandu casting tipe di program Python. |
| 5 | `deskripsi` | TEXT | NOT NULL | Penjelasan aturan bisnis terkait parameter. |
| 6 | `cabang_id` | INT | NOT NULL, DEFAULT 1, FK → `cabang.id` | Cabang berlakunya pengaturan parameter bisnis. |
| 7 | `created_at` | TIMESTAMP | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Tanggal & waktu baris data dibuat. |
| 8 | `updated_at` | TIMESTAMP | NOT NULL, DEFAULT CURRENT_TIMESTAMP ON UPDATE | Tanggal & waktu terakhir baris data diperbarui. |

### 3.5. Seed Data Awal — 13 Parameter Bisnis Default (Ref: R-03, Baris 703-718)

| No. | `parameter_key` | `parameter_value` | `tipe_data` | `deskripsi` |
|:---:|:---|:---|:---|:---|
| 1 | `target_laba_payroll` | `15000000.0000` | DECIMAL | Target laba bersih bulanan untuk skema gaji tetap (Skenario A Smart Payroll) |
| 2 | `porsi_gaji_laba` | `0.2500` | DECIMAL | Persentase alokasi laba bersih untuk pool gaji karyawan (Skenario B Smart Payroll) |
| 3 | `limit_kasbon_staf` | `1000000.0000` | DECIMAL | Pagu maksimal utang kasbon aktif kumulatif per staf |
| 4 | `threshold_saldo_ppob` | `150000.0000` | DECIMAL | Batas saldo minimum PPOB yang memicu alert deposit |
| 5 | `min_topup_ppob` | `500000.0000` | DECIMAL | Nominal minimum deposit topup saldo PPOB |
| 6 | `toleransi_selisih_kas` | `10000.0000` | DECIMAL | Batas toleransi selisih kas kasir sebelum status ANOMALI |
| 7 | `poin_tier_1_rupiah` | `500.0000` | DECIMAL | Nilai rupiah per poin insentif Tier 1 (transaksi mudah) |
| 8 | `poin_tier_2_rupiah` | `1500.0000` | DECIMAL | Nilai rupiah per poin insentif Tier 2 (jasa dasar) |
| 9 | `poin_tier_3_rupiah` | `2500.0000` | DECIMAL | Nilai rupiah per poin insentif Tier 3 (produk kustom) |
| 10 | `poin_tier_4_rupiah` | `5000.0000` | DECIMAL | Nilai rupiah per poin insentif Tier 4 (pekerjaan berat/teknis) |
| 11 | `threshold_pengeluaran` | `500000.0000` | DECIMAL | Batas nominal pengeluaran yang memerlukan otorisasi pemilik |
| 12 | `umr_daerah` | `3200000.0000` | DECIMAL | Upah Minimum Regional daerah sebagai batas proteksi gaji minimum staf |
| 13 | `dana_cadangan_darurat` | `4500000.0000` | DECIMAL | Cadangan kas darurat minimal yang harus dijaga di laci kasir |

### 3.6. Dari CLI Interaction Flow — UC-040 (Ref: R-04, Bab 14.1)

**Alur Interaksi 10 Langkah:**

| No. | Aktor/Sistem | Aksi | Tipe | Contoh Tampilan/Input |
|:---:|:---|:---|:---|:---|
| 1 | Sistem | Memeriksa hak akses (RBAC). Hanya Pemilik yang diizinkan (Absolute Lockdown). | Proses | Security guard check |
| 2 | Sistem | Menampilkan header path menu Config. | Output | `Dashboard > M.10 Config > Konfigurasi Parameter Runtime` |
| 3 | Sistem | Membaca parameter regulasi bisnis dinamis dari database `system_configs` MySQL, memuatnya sebagai runtime static memory. | Proses | Query `SELECT parameter_key, parameter_value FROM system_configs` |
| 4 | Sistem | Menyajikan tabel visual konfigurasi aktif `rich` visual di layar CLI pemilik. | Output | Tabel parameter runtime system_configs aktif |
| 5 | Pengguna | Memilih ID Parameter yang akan disesuaikan nilainya. | Input | `Masukkan nomor opsi parameter yang akan diubah: ` |
| 6 | Pengguna | Mengetikkan pilihan parameter. | Input | `1` (Limit Kasbon Staf) |
| 7 | Sistem | Meminta memasukkan nilai baru (format desimal). | Output | `Masukkan nilai baru untuk Limit Kasbon Staf: Rp ` |
| 8 | Pengguna | Mengetikkan angka nilai parameter baru. | Input | `1200000` (decimal) |
| 9 | Sistem | Memvalidasi input desimal, start transaction, meng-update parameter ke database MySQL, commit data. | Proses | `UPDATE system_configs SET parameter_value = %s WHERE id = %s` |
| 10 | Sistem | Menampilkan visual sukses hijau, dan status nilai baru terupdate. | Output | `[GREEN] Konfigurasi Sukses! Parameter 'Limit Kasbon Staf' diubah = Rp 1.200.000. Tersimpan di database.` |

**Error Code Terdaftar:**

| Kode Error | Pemicu | Pesan yang Ditampilkan |
|:---|:---|:---|
| `ERR-VAL-038` | Nilai parameter baru yang dimasukkan diinput non-numerik atau bernilai Rupiah negatif. | `⛔ ERR-VAL-038: Input Salah: Nilai parameter baru harus diisi berupa angka positif desimal!` |

### 3.7. Dari Module Structure — Dekomposisi File (Ref: R-05, Bab 4.7)

| Atribut | Detail Terekstrak |
|:---|:---|
| **File CLI** | `cli/menu_configs.py` |
| **Fungsi Publik** | `show_menu_configs(session_state: dict) -> None`, `form_update_parameter(session_state: dict) -> None` |
| **Dependensi Impor** | `db.query_builder`, `middleware.rbac_guard` |
| **Menu ID** | `MENU-M10-001` |
| **Tabel Diakses** | `system_configs` (via Layer 3) |
| **Hak Akses** | `pemilik`: Absolute Lockdown. Seluruh peran lain: DENY. |

### 3.8. Dari SRS Traceability — File Handler (Ref: R-01, Bab 7)

| ID SRS | Modul | File Handler | Tabel Terkait |
|:---|:---|:---|:---|
| **SRS-F-040** | M.10 Config Runtime | `database/config_cache.py` | `system_configs` |
| **SRS-F-ADD-01** | M.10 Config Runtime | `main.py` | — |

> **Catatan Penting**: SRS memetakan file handler ke `database/config_cache.py`, namun arsitektur direktori proyek yang berlaku (Coding Standard & Module Structure) menggunakan folder `db/` bukan `database/`. Maka file yang **HARUS** dibuat adalah: `db/config_cache.py`.

### 3.9. Dari Test Plan & Test Cases — Skenario M.10 (Ref: R-08)

| ID Skenario | Deskripsi | SRS | UC | Tipe | Prioritas |
|:---|:---|:---|:---|:---|:---|
| **M10-TC-001** | Dinamis parameter bisnis loading & modifikasi pada tabel `system_configs`. | SRS-F-038 | UC-040 | Database | High |

**Test Case TC-M10-001-01:**
- **Prakondisi**: Sesi login pemilik aktif. Tabel `system_configs` memiliki parameter `threshold_saldo_ppob = 150000`.
- **Data Uji**: `config_key = 'threshold_saldo_ppob'`, `new_value = '200000'`.
- **Langkah Uji**: Masuk menu Pengaturan Sistem → Parameter Bisnis → Pilih config_key → Ubah nilai → Simpan.
- **Expected Result**: Nilai parameter diperbarui di DB MySQL. Sesi program kasir lain memuat nilai baru secara dinamis pada transaksi berikutnya.

---

## 4. Analisis Dampak dan Ketergantungan

### 4.1. Modul-Modul yang Mengkonsumsi Parameter Runtime

| Parameter Key | Modul Konsumen | Fungsi yang Membaca | Dampak Jika Berubah |
|:---|:---|:---|:---|
| `target_laba_payroll` | M.4 Smart Payroll | `logic/smart_payroll.py::hitung_gaji_bagi_hasil()` | Threshold laba untuk menentukan Skenario A vs B berubah. |
| `porsi_gaji_laba` | M.4 Smart Payroll | `logic/smart_payroll.py::hitung_gaji_bagi_hasil()` | Persentase bagi hasil pool gaji berubah. |
| `limit_kasbon_staf` | M.4 SDM | `cli/menu_sdm_finansial.py::form_absensi_kasbon()` | Pagu batas utang kasbon berubah. |
| `threshold_saldo_ppob` | M.3 PPOB | `cli/menu_ppob_service.py::form_ppob_deposit()` | Batas alert deposit PPOB berubah. |
| `min_topup_ppob` | M.3 PPOB | `cli/menu_ppob_service.py::form_ppob_deposit()` | Minimal topup deposit PPOB berubah. |
| `toleransi_selisih_kas` | M.7 Handover | `cli/dashboard.py`, `logic/handover` | Toleransi ANOMALI handover kasir berubah. |
| `poin_tier_1_rupiah` s.d `poin_tier_4_rupiah` | M.4 Poin Insentif | `logic/smart_payroll.py::hitung_komisi_poin()` | Nilai konversi poin-ke-rupiah berubah. |
| `threshold_pengeluaran` | M.6 Pengeluaran | `cli/menu_sdm_finansial.py::form_pengeluaran_rutin()` | Batas eskalasi sandi pemilik berubah. |
| `umr_daerah` | M.4 Smart Payroll | `logic/smart_payroll.py::hitung_gaji_bagi_hasil()` | Batas proteksi gaji minimum 50% UMR berubah. |
| `dana_cadangan_darurat` | M.6 Keuangan | `logic/financial_engine.py` | Batas kas darurat minimum berubah. |

### 4.2. Prinsip Non-Destruktif

- `[WAJIB]` Implementasi fitur M.10 **TIDAK BOLEH** mengubah signature fungsi publik yang sudah ada di modul lain.
- `[WAJIB]` Config cache harus bersifat **read-only** bagi semua modul konsumen — hanya `cli/menu_configs.py` yang boleh melakukan operasi tulis (update).
- `[WAJIB]` Jika modul konsumen saat ini menggunakan hardcoded constant, **JANGAN** refactor modul konsumen dalam issue ini. Refactoring konsumen akan dilakukan di issue terpisah setelah M.10 stabil.

---

## 5. File yang Akan Dimodifikasi dan Dibuat

### 5.1. Ringkasan Perubahan

| No. | Aksi | File Target | Layer | Deskripsi |
|:---:|:---:|:---|:---|:---|
| 1 | `[NEW]` | `db/config_cache.py` | Layer 3 — Data Access | Modul config cache reader/writer untuk tabel `system_configs`. |
| 2 | `[MODIFY]` | `cli/menu_configs.py` | Layer 1 — Presentation | Implementasi penuh UI menu konfigurasi parameter runtime. |
| 3 | `[MODIFY]` | `main.py` | Entry Point | Tambahkan pemanggilan config cache loader saat startup setelah koneksi DB berhasil. |
| 4 | `[NEW]` | `tests/test_config_cache.py` | Testing | Unit test untuk fungsi config cache. |

---

## 6. Instruksi Implementasi Low-Level (Checklist)

### TAHAP 1: Membuat File `db/config_cache.py` (Config Cache Reader/Writer)

- [ ] **1.1.** Buat file baru `db/config_cache.py` di direktori `db/`.
- [ ] **1.2.** Tulis header module docstring standar AbuCom:
    ```python
    """
    Nama Modul: config_cache.py
    Deskripsi: Modul Data Access Layer untuk membaca, menyimpan ke cache memori,
               dan memperbarui parameter regulasi bisnis runtime dari tabel
               database system_configs (Modul M.10).
    Author: [Nama Pelaksana / AI]
    Tanggal: [YYYY-MM-DD]
    """
    ```
- [ ] **1.3.** Tambahkan import sesuai urutan standar:
    ```python
    # 1. Standard Library
    import logging
    from collections import namedtuple
    from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

    # 2. Third-Party (Tidak ada)

    # 3. Local Modules
    from db.query_builder import execute_query, execute_update
    ```
- [ ] **1.4.** Definisikan NamedTuple imutabel `ConfigParam`:
    ```python
    ConfigParam = namedtuple('ConfigParam', [
        'id', 'parameter_key', 'parameter_value', 'tipe_data', 'deskripsi'
    ])
    ```
- [ ] **1.5.** Definisikan NamedTuple imutabel `Result` (atau impor dari modul yang sudah ada):
    ```python
    Result = namedtuple('Result', ['is_success', 'data', 'error_msg'])
    ```
- [ ] **1.6.** Definisikan variabel modul-level untuk menyimpan cache:
    ```python
    # Cache memori lokal sesi — dictionary parameter_key -> parameter_value (string)
    _config_cache: dict[str, str] = {}
    ```
    > **Catatan**: Variabel `_config_cache` menggunakan prefix underscore karena bersifat privat. Akses dari luar modul wajib melalui fungsi publik `get_config_value()`.
- [ ] **1.7.** Implementasikan fungsi `load_all_configs()`:
    ```python
    def load_all_configs(db_connection, cabang_id: int) -> Result:
        """Memuat seluruh parameter runtime dari tabel system_configs ke cache memori.

        Fungsi ini dipanggil SATU KALI saat startup program (main.py) setelah
        koneksi database berhasil. Seluruh baris parameter di-load ke dictionary
        _config_cache untuk diakses cepat oleh modul-modul konsumen.

        Args:
            db_connection: Koneksi database MySQL aktif dari pool.
            cabang_id (int): ID cabang aktif dari settings.

        Returns:
            Result: NamedTuple berisi status success/failure dan jumlah parameter dimuat.
        """
    ```
    - [ ] **1.7.1.** Di dalam fungsi, tulis query: `SELECT id, parameter_key, parameter_value, tipe_data, deskripsi FROM system_configs WHERE cabang_id = %s ORDER BY id ASC`.
    - [ ] **1.7.2.** Gunakan `cursor.execute(query, (cabang_id,))` — parameterized query.
    - [ ] **1.7.3.** Iterasi `cursor.fetchall()`, isi `_config_cache[row['parameter_key']] = row['parameter_value']` untuk setiap baris.
    - [ ] **1.7.4.** Return `Result(True, len(_config_cache), None)` jika sukses.
    - [ ] **1.7.5.** Tangkap exception database, return `Result(False, None, f"ERR-DB-010: Gagal memuat config runtime: {str(e)}")`.
    - [ ] **1.7.6.** Log jumlah parameter yang berhasil dimuat menggunakan `_logger.info(...)`.
- [ ] **1.8.** Implementasikan fungsi `get_config_value()`:
    ```python
    def get_config_value(key: str, default: str | None = None) -> str | None:
        """Mengambil nilai parameter runtime dari cache memori lokal.

        Args:
            key (str): Kunci parameter (e.g. 'target_laba_payroll').
            default (str | None): Nilai fallback jika key tidak ditemukan di cache.

        Returns:
            str | None: Nilai parameter sebagai string, atau default.
        """
        return _config_cache.get(key, default)
    ```
- [ ] **1.9.** Implementasikan fungsi `get_config_decimal()`:
    ```python
    def get_config_decimal(key: str, default: Decimal = Decimal('0.0000')) -> Decimal:
        """Mengambil nilai parameter runtime dan meng-cast ke Decimal presisi 4.

        Args:
            key (str): Kunci parameter.
            default (Decimal): Nilai fallback Decimal jika key tidak ditemukan.

        Returns:
            Decimal: Nilai parameter ter-cast ke Decimal 4 desimal.
        """
    ```
    - [ ] **1.9.1.** Ambil nilai string dari `_config_cache`.
    - [ ] **1.9.2.** Lakukan casting: `Decimal(value).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)`.
    - [ ] **1.9.3.** Tangkap `InvalidOperation` dan `ValueError`, return `default`.
- [ ] **1.10.** Implementasikan fungsi `get_all_configs_list()`:
    ```python
    def get_all_configs_list(db_connection, cabang_id: int) -> Result:
        """Mengambil seluruh parameter runtime sebagai list of ConfigParam NamedTuple.

        Fungsi ini digunakan oleh cli/menu_configs.py untuk menampilkan tabel
        parameter ke layar pemilik secara visual.

        Args:
            db_connection: Koneksi database MySQL aktif.
            cabang_id (int): ID cabang aktif.

        Returns:
            Result: NamedTuple berisi list[ConfigParam] atau error.
        """
    ```
    - [ ] **1.10.1.** Query: `SELECT id, parameter_key, parameter_value, tipe_data, deskripsi FROM system_configs WHERE cabang_id = %s ORDER BY id ASC`.
    - [ ] **1.10.2.** Konversi setiap row ke `ConfigParam` NamedTuple.
    - [ ] **1.10.3.** Return `Result(True, list_config_params, None)`.
- [ ] **1.11.** Implementasikan fungsi `update_config_value()`:
    ```python
    def update_config_value(db_connection, config_id: int, new_value: str, cabang_id: int) -> Result:
        """Memperbarui nilai parameter di database dan sinkronisasi cache memori.

        Args:
            db_connection: Koneksi database MySQL aktif.
            config_id (int): ID baris parameter di tabel system_configs.
            new_value (str): Nilai baru parameter (sudah divalidasi).
            cabang_id (int): ID cabang aktif.

        Returns:
            Result: NamedTuple berisi status success/failure.
        """
    ```
    - [ ] **1.11.1.** Mulai transaksi ACID: `db_connection.start_transaction()`.
    - [ ] **1.11.2.** Query SELECT sebelum update untuk mendapatkan `old_value` dan `parameter_key`: `SELECT parameter_key, parameter_value FROM system_configs WHERE id = %s AND cabang_id = %s`.
    - [ ] **1.11.3.** Jalankan query UPDATE: `UPDATE system_configs SET parameter_value = %s WHERE id = %s AND cabang_id = %s`.
    - [ ] **1.11.4.** Commit transaksi: `db_connection.commit()`.
    - [ ] **1.11.5.** Perbarui cache memori lokal: `_config_cache[parameter_key] = new_value`.
    - [ ] **1.11.6.** Return `Result(True, {'old_value': old_value, 'new_value': new_value, 'parameter_key': parameter_key}, None)`.
    - [ ] **1.11.7.** Pada exception, rollback dan return `Result(False, None, f"ERR-DB-011: Gagal update config: {str(e)}")`.
- [ ] **1.12.** Tambahkan `db/config_cache.py` ke daftar re-export di `db/__init__.py` (jika ada pola re-export).

---

### TAHAP 2: Implementasi Penuh `cli/menu_configs.py` (Presentasi Menu)

- [ ] **2.1.** Buka file `cli/menu_configs.py` yang sudah ada (saat ini berisi placeholder TODO).
- [ ] **2.2.** Perbarui header module docstring (pertahankan, sesuaikan author dan tanggal).
- [ ] **2.3.** Tambahkan import sesuai urutan standar:
    ```python
    # 1. Standard Library
    from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

    # 2. Third-Party
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel

    # 3. Local Modules
    from db.config_cache import get_all_configs_list, update_config_value
    from db.db_connector import get_db_connection
    from middleware.rbac_guard import require_role
    from middleware.audit_logger import log_audit_trail
    ```
- [ ] **2.4.** Definisikan console instance: `_console = Console()`.
- [ ] **2.5.** Implementasikan fungsi `show_menu_configs()`:
    - [ ] **2.5.1.** Terapkan dekorator RBAC: `@require_role('MENU-M10-001')` — hanya `pemilik`.
    - [ ] **2.5.2.** Tampilkan header breadcrumb: `Dashboard > M.10 Config > Konfigurasi Parameter Runtime`.
    - [ ] **2.5.3.** Panggil `get_all_configs_list(db_connection, cabang_id)` untuk mengambil seluruh parameter.
    - [ ] **2.5.4.** Jika `result.is_success is False`, tampilkan pesan error dan return.
    - [ ] **2.5.5.** Render tabel parameter menggunakan `rich.table.Table()`:
        - Kolom: `No.`, `Parameter Key`, `Nilai Saat Ini`, `Tipe Data`, `Deskripsi`
        - Untuk parameter bertipe DECIMAL, format nilai dengan prefix `Rp ` dan pemisah ribuan jika nilainya >= 1000.
    - [ ] **2.5.6.** Tampilkan prompt pilihan: `Masukkan nomor opsi parameter yang akan diubah [0-Kembali]: `.
    - [ ] **2.5.7.** Jika input == `'0'`, kembali ke dashboard.
    - [ ] **2.5.8.** Jika input valid (angka 1-13), panggil `form_update_parameter()` dengan config terpilih.
    - [ ] **2.5.9.** Jika input tidak valid, tampilkan error dan ulangi prompt.
- [ ] **2.6.** Implementasikan fungsi `form_update_parameter()`:
    - [ ] **2.6.1.** Tampilkan informasi parameter terpilih (key, nilai lama, tipe data, deskripsi).
    - [ ] **2.6.2.** Tampilkan prompt input: `Masukkan nilai baru untuk {deskripsi}: `.
    - [ ] **2.6.3.** Lakukan validasi input berdasarkan `tipe_data`:
        - Jika `tipe_data == 'DECIMAL'`:
            - [ ] Coba cast ke `Decimal(input_value)`.
            - [ ] Pastikan nilai >= 0 (tidak boleh negatif).
            - [ ] Quantize ke 4 desimal: `.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)`.
            - [ ] Jika gagal cast atau negatif, tampilkan: `⛔ ERR-VAL-038: Input Salah: Nilai parameter baru harus diisi berupa angka positif desimal!`
        - Jika `tipe_data == 'VARCHAR'`:
            - [ ] Pastikan string tidak kosong.
        - Jika `tipe_data == 'INTEGER'`:
            - [ ] Coba cast ke `int(input_value)`.
            - [ ] Pastikan >= 0.
    - [ ] **2.6.4.** Tampilkan konfirmasi perubahan:
        ```
        Konfirmasi perubahan parameter:
          Parameter  : {parameter_key}
          Nilai Lama : {old_value}
          Nilai Baru : {new_value}
        Lanjutkan? [Y/N]:
        ```
    - [ ] **2.6.5.** Jika pengguna mengetik `'Y'` atau `'y'`:
        - [ ] Panggil `update_config_value(db_connection, config_id, new_value_str, cabang_id)`.
        - [ ] Jika sukses, tampilkan pesan hijau: `[GREEN] Konfigurasi Sukses! Parameter '{parameter_key}' diubah = {formatted_value}. Tersimpan di database.`
        - [ ] Panggil `log_audit_trail()` untuk mencatat perubahan ke `audit_logs`:
            - `action_type = 'UPDATE'`
            - `target_table = 'system_configs'`
            - `old_val = {'parameter_key': key, 'parameter_value': old_value}`
            - `new_val = {'parameter_key': key, 'parameter_value': new_value}`
    - [ ] **2.6.6.** Jika pengguna mengetik `'N'` atau `'n'`, batalkan dan kembali ke daftar parameter.
    - [ ] **2.6.7.** Tampilkan `[Tekan ENTER untuk kembali ke Daftar Parameter]`.

---

### TAHAP 3: Modifikasi `main.py` (Integrasi Startup Config Loader)

- [ ] **3.1.** Buka file `main.py` di root proyek.
- [ ] **3.2.** Tambahkan import baru:
    ```python
    from db.config_cache import load_all_configs
    ```
- [ ] **3.3.** Temukan blok kode yang menjalankan inisialisasi startup **SETELAH** koneksi database berhasil dan **SEBELUM** tampilan layar login.
- [ ] **3.4.** Sisipkan pemanggilan config loader di posisi tersebut:
    ```python
    # Muat parameter runtime bisnis dari database ke cache memori lokal
    config_result = load_all_configs(db_connection, app_config.app_cabang_id)
    if not config_result.is_success:
        _logger.error(config_result.error_msg)
        print(f"⛔ {config_result.error_msg}")
        sys.exit(1)
    _logger.info(f"Config runtime: {config_result.data} parameter berhasil dimuat ke cache.")
    ```
- [ ] **3.5.** Pastikan urutan startup adalah:
    1. Validasi `.env` (SRS-F-ADD-01) ✅ sudah ada
    2. Inisialisasi koneksi database pool ✅ sudah ada
    3. **[BARU] Muat `system_configs` ke cache memori** ← Tambahkan di sini
    4. Tampilkan layar login ✅ sudah ada
- [ ] **3.6.** Jangan mengubah logika startup lainnya — hanya **sisipkan** (insert) kode baru di posisi yang tepat.

---

### TAHAP 4: Unit Testing `tests/test_config_cache.py`

- [ ] **4.1.** Buat file baru `tests/test_config_cache.py`.
- [ ] **4.2.** Tulis header module docstring.
- [ ] **4.3.** Implementasikan test case berikut:

| No. | Nama Test Function | Skenario | Expected Result |
|:---:|:---|:---|:---|
| 1 | `test_get_config_decimal_valid` | Panggil `get_config_decimal('target_laba_payroll')` setelah cache terisi. | Return `Decimal('15000000.0000')`. |
| 2 | `test_get_config_decimal_not_found` | Panggil `get_config_decimal('nonexistent_key')`. | Return default `Decimal('0.0000')`. |
| 3 | `test_get_config_value_valid` | Panggil `get_config_value('limit_kasbon_staf')` setelah cache terisi. | Return string `'1000000.0000'`. |
| 4 | `test_get_config_value_default` | Panggil `get_config_value('nonexistent', 'fallback')`. | Return `'fallback'`. |
| 5 | `test_validate_decimal_input_negative` | Simulasikan input negatif `-500` di form. | Validasi menolak, error `ERR-VAL-038`. |
| 6 | `test_validate_decimal_input_non_numeric` | Simulasikan input `'abc'` di form. | Validasi menolak, error `ERR-VAL-038`. |
| 7 | `test_validate_decimal_input_valid` | Simulasikan input `'1200000'` di form. | Validasi sukses, value = `Decimal('1200000.0000')`. |

- [ ] **4.4.** Gunakan mock untuk `db_connection` agar test berjalan tanpa database riil.
- [ ] **4.5.** Pastikan semua test berjalan dengan `pytest tests/test_config_cache.py -v`.

---

## 7. Standar Kualitas Kode yang Harus Dipenuhi

### 7.1. Checklist Kepatuhan Coding Standard

- [ ] Tidak ada deklarasi `class` di alur bisnis utama (FP murni).
- [ ] Seluruh fungsi publik memiliki docstring PEP 257 lengkap (Args, Returns, Raises, Example).
- [ ] Seluruh fungsi publik memiliki type hints PEP 484 lengkap.
- [ ] Seluruh query SQL menggunakan parameterized queries `%s` binding.
- [ ] Seluruh nominal keuangan menggunakan `decimal.Decimal` dengan `ROUND_HALF_UP`.
- [ ] Penamaan file, fungsi, dan variabel menggunakan `snake_case`.
- [ ] Penamaan NamedTuple menggunakan `PascalCase`.
- [ ] Konstanta menggunakan `UPPER_SNAKE_CASE`.
- [ ] Urutan import: Standard Library → Third-Party → Local Modules.
- [ ] Tidak ada wildcard import (`from module import *`).
- [ ] Panjang baris kode ≤ 120 karakter.
- [ ] Indentasi 4 spasi (tanpa Tab).
- [ ] Error handling menggunakan Result pattern NamedTuple (bukan throw exception langsung).
- [ ] RBAC decorator diterapkan pada fungsi menu CLI.
- [ ] Audit trail dicatat untuk setiap operasi UPDATE pada `system_configs`.
- [ ] Setiap file `.py` baru memiliki header module docstring.
- [ ] Path file menggunakan `pathlib` (bukan hardcoded separator).

### 7.2. Checklist Integritas Fitur

- [ ] Parameter config ter-load di startup dan tersedia di cache sebelum login.
- [ ] Hanya peran `pemilik` yang dapat mengakses menu M.10.
- [ ] Tabel parameter ditampilkan menggunakan `rich` / `tabulate`.
- [ ] Update parameter menggunakan transaksi ACID (start_transaction → commit/rollback).
- [ ] Cache memori lokal di-sinkronisasi setelah update berhasil.
- [ ] Input non-numerik atau negatif ditolak dengan error `ERR-VAL-038`.
- [ ] Perubahan parameter dicatat di `audit_logs` (old_value & new_value JSON).
- [ ] Navigasi tombol `0` berfungsi untuk kembali ke menu sebelumnya.
- [ ] Header breadcrumb ditampilkan: `Dashboard > M.10 Config > Konfigurasi Parameter Runtime`.
- [ ] Konfirmasi `[Y/N]` sebelum menyimpan perubahan.

---

## 8. Rencana Verifikasi & Pengujian

### 8.1. Automated Testing

```bash
# Jalankan unit test khusus modul config cache
pytest tests/test_config_cache.py -v --tb=short

# Jalankan semua test suite untuk memastikan tidak ada regresi
pytest tests/ -v --tb=short

# Ukur code coverage (target: >= 90% untuk db/config_cache.py)
pytest tests/test_config_cache.py --cov=db/config_cache --cov-report=term-missing
```

### 8.2. Manual Testing Checklist (Skenario TC-M10-001-01)

- [ ] **8.2.1.** Login sebagai `pemilik`. Masuk ke menu `[10] M.10 Parameter Runtime Config`.
- [ ] **8.2.2.** Verifikasi tabel 13 parameter ditampilkan lengkap di layar terminal.
- [ ] **8.2.3.** Pilih parameter `threshold_saldo_ppob` (No. 4).
- [ ] **8.2.4.** Input nilai baru: `200000`. Konfirmasi: `Y`.
- [ ] **8.2.5.** Verifikasi pesan sukses hijau muncul.
- [ ] **8.2.6.** Verifikasi di database: `SELECT parameter_value FROM system_configs WHERE parameter_key = 'threshold_saldo_ppob'` → harus mengembalikan `'200000.0000'`.
- [ ] **8.2.7.** Verifikasi cache memori: Panggil `get_config_decimal('threshold_saldo_ppob')` → harus return `Decimal('200000.0000')`.
- [ ] **8.2.8.** Verifikasi audit trail: `SELECT * FROM audit_logs ORDER BY id DESC LIMIT 1` → harus mencatat update system_configs.
- [ ] **8.2.9.** Login sebagai `kasir`. Coba akses menu `[10]`. Verifikasi error `ERR-AUTH-003: Akses Ditolak`.
- [ ] **8.2.10.** Uji input invalid: Masukkan `'abc'` sebagai nilai baru → Verifikasi error `ERR-VAL-038`.
- [ ] **8.2.11.** Uji input negatif: Masukkan `-500` sebagai nilai baru → Verifikasi error `ERR-VAL-038`.
- [ ] **8.2.12.** Uji konfirmasi batal: Masukkan nilai valid, lalu jawab `N` → Verifikasi tidak ada perubahan di database.

---

## 9. Matriks Ketertelusuran (Traceability Matrix)

### 9.1. BRD → SRS → UC → File → Test

| BRD | SRS | UC | Menu ID | File Handler | Test ID |
|:---|:---|:---|:---|:---|:---|
| BR-F-38 | SRS-F-040 | UC-040 | MENU-M10-001 | `cli/menu_configs.py`, `db/config_cache.py` | TC-M10-001-01 |
| — | SRS-F-ADD-01 | — | — | `main.py` (startup config load) | — |

### 9.2. Fungsi → SRS → Tabel Database

| Fungsi | SRS | Tabel MySQL | Operasi |
|:---|:---|:---|:---|
| `load_all_configs()` | SRS-F-040 | `system_configs` | SELECT |
| `get_config_value()` | SRS-F-040 | — (cache memori) | READ |
| `get_config_decimal()` | SRS-F-040 | — (cache memori) | READ + CAST |
| `get_all_configs_list()` | SRS-F-040 | `system_configs` | SELECT |
| `update_config_value()` | SRS-F-040 | `system_configs` | UPDATE |
| `show_menu_configs()` | SRS-F-040 | `system_configs` (via cache) | DISPLAY |
| `form_update_parameter()` | SRS-F-040 | `system_configs`, `audit_logs` | UPDATE, INSERT |

---

## 10. Catatan Tambahan & Best Practice Industri

### 10.1. Pattern: Configuration Cache with Write-Through

Implementasi ini menggunakan pola **Write-Through Cache**:
- **Read**: Semua modul membaca dari cache memori (cepat, O(1) dictionary lookup).
- **Write**: Saat pemilik mengubah parameter, data ditulis ke database terlebih dahulu (sumber kebenaran), lalu cache memori diperbarui secara sinkron.
- **Startup**: Cache di-populate dari database saat startup program.

Pola ini dipilih karena:
1.  Arsitektur AbuCom adalah **single-process CLI** (bukan web server multi-instance), sehingga cache memori per-proses sudah cukup.
2.  Menghindari query database berulang setiap kali modul konsumen membutuhkan nilai parameter.
3.  Konsisten dengan spesifikasi SRS-F-040 poin 2: _"Simpan nilai parameter ke cache memori lokal sesi program klien."_

### 10.2. Pertimbangan Multi-Cabang

- Parameter `system_configs` sudah memiliki kolom `cabang_id` (FK → `cabang.id`).
- Query SELECT dan UPDATE **HARUS** selalu memfilter `WHERE cabang_id = %s` untuk menjamin isolasi data antar cabang.
- Nilai `cabang_id` diambil dari `AppConfig.app_cabang_id` yang dibaca dari `.env` saat startup.

### 10.3. Keamanan: Klasifikasi Tabel Sangat Sensitif

- Tabel `system_configs` diklasifikasikan sebagai **Sangat Sensitif** (Ref: Security Design).
- Setiap operasi UPDATE **WAJIB** dicatat di `audit_logs` dengan `old_value` dan `new_value` dalam format JSON.
- Akses menu **WAJIB** menggunakan RBAC Absolute Lockdown — hanya peran `pemilik`.

### 10.4. Data Kosong / Placeholder yang Perlu Ditindaklanjuti

| No. | Item | Status | Tindakan yang Diperlukan |
|:---:|:---|:---|:---|
| 1 | Error code `ERR-DB-010` (gagal muat config) | `[DATA-BARU]` | Belum ada di katalog resmi Coding Standard. Usulkan penambahan ke katalog error. |
| 2 | Error code `ERR-DB-011` (gagal update config) | `[DATA-BARU]` | Belum ada di katalog resmi Coding Standard. Usulkan penambahan ke katalog error. |
| 3 | Mapping SRS ke file handler di SRS v1.2 menggunakan path `database/config_cache.py` | `[INKONSISTEN]` | Path aktual proyek menggunakan folder `db/` bukan `database/`. Implementasi menggunakan `db/config_cache.py`. Perlu sinkronisasi dokumen SRS. |

---

## 11. Referensi Dokumen SDLC Lengkap

| Kode | Dokumen | Path |
|:---|:---|:---|
| R-01 | Software Requirements Specification v1.2 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| R-02 | Business Requirements Document v1.2 | `docs/sdlc/02_analysis/01_business_requirements.md` |
| R-03 | Database Schema DDL SQL v1.2 | `docs/sdlc/03_design/01_database_schema.sql` |
| R-04 | CLI Interaction Flow v1.2 | `docs/sdlc/03_design/04_cli_interaction_flow.md` |
| R-05 | Module Structure v1.2 | `docs/sdlc/04_implementation/03_module_structure.md` |
| R-06 | Coding Standard v1.2 | `docs/sdlc/04_implementation/01_coding_standard.md` |
| R-07 | System Architecture v1.2 | `docs/sdlc/03_design/03_system_architecture.md` |
| R-08 | Test Plan v1.2 / Test Cases v1.2 | `docs/sdlc/05_testing/01_test_plan.md`, `docs/sdlc/05_testing/02_test_cases.md` |
| R-09 | ERD Database v1.2 | `docs/sdlc/03_design/02_erd_database.md` |
| R-10 | Security Design v1.2 | `docs/sdlc/03_design/06_security_design.md` |
| R-11 | Use Case Diagram v1.2 | `docs/sdlc/02_analysis/03_use_case_diagram.md` |
