---
issue_id    : 0126
judul       : Feature Dashboard Ringkasan Harian per Role
status      : Open
prioritas   : High
tanggal     : 2026-06-07
penyusun    : Claude Opus 4.6 (Thinking) — Senior Full-Stack Architect & System Integration Strategist
---

# Issue #0126 — Feature Dashboard Ringkasan Harian per Role

## 1. Persona Pelaksana

> **Persona yang WAJIB diadopsi oleh AI/Programmer pelaksana:**
>
> **Senior Python CLI Architect & RBAC-Aware Dashboard Specialist**
>
> Kamu adalah seorang arsitek Python berpengalaman yang ahli dalam membangun dashboard CLI interaktif berbasis terminal menggunakan library `rich` dan `tabulate`. Kamu memahami secara mendalam arsitektur 4-layer AbuCom (Presentation → Logic → Data Access → MySQL), paradigma Functional Programming murni, sistem otorisasi RBAC 8 peran, dan presisi desimal `DECIMAL(15,4)`. Kamu sangat teliti, rapi, dan tidak pernah terburu-buru. Kamu selalu memvalidasi setiap output terhadap dokumen SDLC referensi sebelum menganggap pekerjaan selesai.

---

## 2. Dokumen Referensi yang WAJIB Dibaca

Berikut adalah daftar dokumen referensi **yang harus dibaca dan diekstrak datanya** sebelum memulai implementasi. Baca secara menyeluruh bagian yang relevan, jangan lewatkan detail kecil.

| # | Path File Referensi | Bagian yang Relevan | Alasan Pemilihan |
|---|---|---|---|
| R-01 | `docs/sdlc/02_analysis/03_use_case_diagram.md` | **UC-043**: Melihat Dashboard Ringkasan Harian (Baris 1281-1299) | Sumber utama spesifikasi use case dashboard, alur utama 3 skenario per role, prakondisi, exception flow |
| R-02 | `docs/sdlc/02_analysis/06_access_control_matrix.md` | Bab 4.12 `BASE-003` (Baris 337), Bab 3.1 `MENU-BASE-003` (Baris 208), Bab 5.2 Matriks CRUD tabel (Baris 352-383) | Hak akses ✅ FULL seluruh 8 peran, tabel database yang boleh di-query per role |
| R-03 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | Bab 4.3 Alur Interaksi Dashboard Utama per Role UC-043 (Baris 408-420), Bab 3.2 Deskripsi `MENU-BASE-003` (Baris 232), Bab 3.3 Matriks Visibilitas (Baris 322) | Langkah interaksi detail dashboard, skenario visual per role, konvensi ANSI color |
| R-04 | `docs/sdlc/04_implementation/03_module_structure.md` | Bab 4.2 `cli/dashboard.py` (Baris 312-321) | Spesifikasi file target, fungsi publik, dependensi impor, tabel yang diakses |
| R-05 | `docs/sdlc/04_implementation/01_coding_standard.md` | Bab 2 (FP Murni), Bab 3 (Penamaan), Bab 7 (Type Hints), Bab 8 (Arsitektur & Pattern), Bab 9 (SQL), Bab 10 (Keamanan), Bab 11 (CLI Visual) | Standar penulisan kode, Result Pattern, State Dict Passing, konvensi visual rich/tabulate |
| R-06 | `docs/sdlc/03_design/01_database_schema.sql` | Tabel: `transaksi`, `antrian_kerja`, `shift_handover`, `pengguna`, `barang`, `saldo_ppob`, `pinjaman_bank`, `utang_supplier`, `pengeluaran`, `limbah_produksi`, `poin_insentif`, `stock_opname` | Skema kolom dan tipe data untuk query agregasi dashboard |
| R-07 | `docs/sdlc/03_design/03_system_architecture.md` | Arsitektur 4-layer, koneksi database, multi-cabang | Batasan arsitektural yang harus dipatuhi |
| R-08 | `docs/sdlc/narasi.txt` | Baris 83-86 tentang kehadiran, laporan, rekonsiliasi kas, dan analisis laba/rugi | Konteks kebutuhan bisnis pemilik terkait dashboard |

> [!IMPORTANT]
> File `narasi.txt` masih dibutuhkan sebagai referensi konteks bisnis karena menjelaskan harapan pemilik soal "laporan harian hingga tahunan" dan "rekonsiliasi kas" yang harus tampil di dashboard pemilik.

---

## 3. Rangkuman Detail Data dari Dokumen Referensi

### 3.1. Spesifikasi UC-043 (dari R-01)

| Atribut | Nilai |
|---|---|
| **UC-ID** | UC-043 |
| **Nama** | Melihat Dashboard Ringkasan Harian (Dashboard Utama) |
| **Derivasi** | Tambahan Dasar Operasional |
| **Modul** | Dasar Operasional (M.7) |
| **Prioritas** | High |
| **Aktor Primer** | Semua Aktor Internal (8 peran) |
| **Prakondisi** | Aktor berhasil login ke sistem CLI (UC-041) |
| **Pemicu** | Aktor pertama kali dialihkan ke menu utama pasca login ATAU memilih menu "Dashboard Utama" |

**Alur Utama (3 Skenario):**

1. **Skenario A — Dashboard Pemilik (`pemilik`):**
   - Laba bersih toko hari ini
   - Total kas laci kasir
   - Grafik transaksi 5 divisi (teks tabular)
   - Alert jatuh tempo utang bank/supplier H-3

2. **Skenario B — Dashboard Kasir (`kasir`):**
   - Saldo laci kasir shift aktif
   - Sisa saldo virtual PPOB (2 akun)
   - Jumlah invoice belum lunas (pesanan DP)

3. **Skenario C — Dashboard Desainer/Produksi (`desainer`, `produksi_cetak`):**
   - Jumlah pekerjaan antrian cetak kustom
   - Status job tracking aktif
   - Alert bahan baku habis/kritis

**Exception Flow:**
- `ERR-DB-003`: Koneksi database server terputus permanen setelah 5x retry → hentikan operasi, tampilkan warning keras.

### 3.2. Hak Akses Dashboard (dari R-02)

| Menu ID | pemilik | kepala_percetakan | pramuniaga | kasir | desainer | produksi_cetak | fotocopy_print | gudang |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BASE-003` | ✅ FULL | ✅ FULL | ✅ FULL | ✅ FULL | ✅ FULL | ✅ FULL | ✅ FULL | ✅ FULL |

**Catatan**: Seluruh 8 peran diperbolehkan mengakses dashboard, namun **isi konten visual yang ditampilkan berbeda-beda** sesuai filter RBAC peran masing-masing.

### 3.3. Tabel Database yang Diakses oleh Dashboard (dari R-04)

Sesuai Module Structure Bab 4.2:
- `pengguna` — Data nama pengguna login, role, cabang
- `transaksi` — Ringkasan kas masuk harian, invoice DP belum lunas
- `antrian_kerja` — Status antrian job tracking cetak kustom
- `shift_handover` — Catatan serah terima kasir terakhir

**Tabel tambahan** yang dibutuhkan berdasarkan UC-043 skenario detail:
- `barang` — Deteksi stok bahan baku kritis (re-order alert)
- `saldo_ppob` — Saldo deposit PPOB (2 akun: Pulsa_Data, Token_Tagihan)
- `pinjaman_bank` — Alert jatuh tempo cicilan bank H-3
- `utang_supplier` — Alert jatuh tempo utang supplier H-3
- `detail_transaksi` — Kalkulasi total penjualan per divisi
- `pengeluaran` — Total pengeluaran harian
- `limbah_produksi` — Kerugian limbah harian
- `poin_insentif` — Akumulasi poin staf

### 3.4. Spesifikasi File Target (dari R-04)

```
File              : cli/dashboard.py
Modul Fungsional  : M.7 Keamanan & Hak Akses
Menu ID           : MENU-BASE-003

Fungsi Publik:
  - render_dashboard(session_state: dict) -> None
  - handle_navigation(session_state: dict, pilihan: str) -> dict

Dependensi Impor:
  - cli.menu_transaksi
  - cli.menu_inventaris
  - cli.menu_ppob_service
  - cli.menu_sdm_finansial
  - cli.menu_configs
  - middleware.rbac_guard
  - utils.text_formatter

Hak Akses: Seluruh 8 peran terdaftar (menu terfilter)
```

### 3.5. Konvensi Visual CLI (dari R-05 Bab 11)

- **Header**: Panel `rich` format box double line (`═══`)
- **ANSI Color**:
  - `Green` → Sukses, LUNAS, sehat
  - `Red` → Error, akses ditolak, kritis
  - `Yellow` → Warning, stok kritis, jatuh tempo, BELUM LUNAS
  - `Blue` → Panduan, breadcrumb
  - `Magenta` → Judul utama modul, banner dashboard
- **Tabel Data**: Library `tabulate` dengan grid format
- **Breadcrumb**: `Dashboard` (di baris atas terminal)
- **Navigasi**: Tombol `0` = Kembali, Hotkey numerik = Pilih

### 3.6. Data Kosong / Tidak Tersedia di Referensi

> [!WARNING]
> **Data berikut TIDAK ditemukan secara eksplisit di dokumen referensi dan memerlukan keputusan/klarifikasi:**
>
> 1. **Skenario Dashboard untuk role `kepala_percetakan`**: UC-043 hanya menyebutkan 3 skenario (Pemilik, Kasir, Desainer/Produksi). Tidak ada skenario eksplisit untuk `kepala_percetakan`. **Rekomendasi**: Tampilkan gabungan ringkasan operasional (antrian kerja aktif, staf hadir hari ini, draf stock opname pending approval).
> 2. **Skenario Dashboard untuk role `pramuniaga`**: Tidak disebutkan eksplisit. **Rekomendasi**: Tampilkan jumlah pelanggan CRM baru hari ini, antrian pesanan masuk, dan status job tracking terbaru.
> 3. **Skenario Dashboard untuk role `fotocopy_print`**: Tidak disebutkan eksplisit. **Rekomendasi**: Tampilkan ringkasan transaksi fotocopy/print hari ini.
> 4. **Skenario Dashboard untuk role `gudang`**: Tidak disebutkan eksplisit. **Rekomendasi**: Tampilkan alert stok bahan baku kritis, draf stock opname belum di-approve, dan daftar supplier dengan utang jatuh tempo.
> 5. **Query SQL spesifik** untuk setiap widget dashboard: Belum ada pseudocode SQL di dokumen. Harus dibangun berdasarkan skema DDL (`R-06`).
> 6. **Threshold "stok kritis"**: Tidak ada angka pasti default selain "sisa stok < 7 hari" (ACM Bab 4.3 `M2-006`). Gunakan parameter `system_configs` jika tersedia, atau default fallback.

---

## 4. Batasan, Cakupan & Alur Pengerjaan

### 4.1. Cakupan Issue (IN-SCOPE)

- [ ] Modifikasi file `cli/dashboard.py` — menambahkan panel ringkasan harian per role ke dalam fungsi `render_dashboard()`
- [ ] Pembuatan fungsi-fungsi query agregasi di layer Data Access (`db/query_builder.py`) untuk menarik data ringkasan dashboard
- [ ] Pembuatan fungsi-fungsi pure calculation di layer Logic (jika diperlukan kalkulasi laba rugi instan)
- [ ] Integrasi dengan `middleware.rbac_guard` untuk filter konten per role
- [ ] Tampilan visual menggunakan `rich` Panel dan `tabulate` tabel
- [ ] Penanganan error `ERR-DB-003` jika koneksi database terputus saat memuat dashboard

### 4.2. Di Luar Cakupan (OUT-OF-SCOPE)

> [!CAUTION]
> **Pengerjaan issue ini TIDAK BOLEH menyentuh atau memodifikasi fungsionalitas berikut:**
>
> - Alur login/logout (`cli/__init__.py`, `logic/auth_handler.py`)
> - Navigasi menu modul M.1 s.d M.10 yang sudah berfungsi (`handle_navigation()`, `show_module_submenu()`)
> - Formulir ubah password (`form_ubah_password()`)
> - Fungsi `graceful_exit()`
> - Skema database DDL (`schema.sql`) — TIDAK BOLEH menambah/mengubah tabel
> - Middleware RBAC guard logic (`middleware/rbac_guard.py`) — TIDAK BOLEH mengubah matriks otorisasi
> - File konfigurasi `.env` / `config/settings.py`

### 4.3. Alur Pengerjaan (Workflow)

```
┌────────────────────────────────────────┐
│ FASE 1: Pembacaan & Ekstraksi Referensi │
└────────────────┬───────────────────────┘
                 │
                 v
┌────────────────────────────────────────┐
│ FASE 2: Implementasi Query Agregasi    │
│         (db/query_builder.py)          │
└────────────────┬───────────────────────┘
                 │
                 v
┌────────────────────────────────────────┐
│ FASE 3: Implementasi Logic Kalkulasi   │
│         (logic/ — jika diperlukan)     │
└────────────────┬───────────────────────┘
                 │
                 v
┌────────────────────────────────────────┐
│ FASE 4: Implementasi Visual Dashboard  │
│         (cli/dashboard.py)             │
└────────────────┬───────────────────────┘
                 │
                 v
┌────────────────────────────────────────┐
│ FASE 5: Integrasi & Pengujian          │
└────────────────┬───────────────────────┘
                 │
                 v
┌────────────────────────────────────────┐
│ FASE 6: Review Kualitas & Finalisasi   │
└────────────────────────────────────────┘
```

---

## 5. Instruksi Pengerjaan (Jaminan Kualitas)

> [!IMPORTANT]
> **KAIDAH UTAMA PENGERJAAN:**
>
> 1. **Kerjakan dengan RAPI, BERSIH, TIDAK TERGESA-GESA, dan TIDAK BURU-BURU.** Setiap baris kode harus ditulis dengan penuh pertimbangan agar hasilnya maksimal.
> 2. **Pastikan KELENGKAPAN pengerjaan** sehingga tidak ada yang kurang yang bisa menghambat feature lain atau memerlukan perbaikan ulang.
> 3. **JANGAN menyentuh atau merusak feature lain.** Pastikan seluruh fungsi yang sudah ada (login, logout, navigasi, ubah password) tetap berjalan normal setelah modifikasi.
> 4. **Jika ada data kosong/tidak tersedia** di file referensi, TANDAI dengan komentar `# TODO: Data tidak tersedia di referensi — perlu klarifikasi` dan buat fallback yang masuk akal.
> 5. **Setiap query SQL WAJIB menggunakan parameterized query** (`%s` bindings) — DILARANG menggunakan f-string untuk SQL.
> 6. **Semua nominal uang WAJIB menggunakan `decimal.Decimal`** — DILARANG menggunakan `float`.
> 7. **Setiap fungsi publik WAJIB memiliki docstring PEP 257** dengan Args, Returns, dan referensi SDLC.
> 8. **Patuhi arsitektur 4-layer**: CLI (presentation) → Logic (pure FP) → DB (data access) → MySQL. Dilarang melakukan query database langsung di layer presentation kecuali via wrapper `db/query_builder.py`.

---

## 6. Checklist Implementasi Tahap demi Tahap

### FASE 1: Pembacaan & Ekstraksi Referensi

- [ ] **1.1** Baca file `docs/sdlc/02_analysis/03_use_case_diagram.md` baris 1281-1299 (UC-043). Catat semua skenario dashboard (A, B, C), prakondisi, pemicu, exception flow.
- [ ] **1.2** Baca file `docs/sdlc/03_design/04_cli_interaction_flow.md` baris 408-420 (Bab 4.3). Catat langkah interaksi detail dashboard: step 1 (deteksi role JWT), step 2 (query summary), step 3a/3b/3c (render per role), step 4 (menu navigasi terfilter).
- [ ] **1.3** Baca file `docs/sdlc/02_analysis/06_access_control_matrix.md` baris 337 (`BASE-003`). Pastikan dashboard ✅ FULL untuk semua 8 peran.
- [ ] **1.4** Baca file `docs/sdlc/04_implementation/03_module_structure.md` baris 312-321 (Bab 4.2). Catat fungsi publik, dependensi, dan tabel yang diakses.
- [ ] **1.5** Baca file `docs/sdlc/04_implementation/01_coding_standard.md` — pahami: FP murni (Bab 2), penamaan snake_case (Bab 3), type hints (Bab 7), Result Pattern (Bab 8.7), parameterized SQL (Bab 9), visual CLI (Bab 11).
- [ ] **1.6** Baca file `docs/sdlc/03_design/01_database_schema.sql` — pahami skema tabel: `transaksi` (baris 215-240), `detail_transaksi` (245-259), `antrian_kerja` (264-282), `barang` (116-138), `saldo_ppob` (143-154), `shift_handover` (447-471), `pinjaman_bank` (503-528), `utang_supplier` (480-498), `pengeluaran` (354-370), `limbah_produksi` (375-394), `poin_insentif` (424-442).
- [ ] **1.7** Baca file `docs/sdlc/narasi.txt` baris 83-84 — catat harapan pemilik: "Laporan harus lengkap (harian hingga tahunan) dan ada fitur rekonsiliasi kas".
- [ ] **1.8** Baca file `cli/dashboard.py` yang sudah ada saat ini (515 baris) — pahami struktur existing: `render_dashboard()`, `show_module_submenu()`, `handle_navigation()`, `form_ubah_password()`, `graceful_exit()`. **JANGAN MENGUBAH** fungsi `show_module_submenu()`, `handle_navigation()`, `form_ubah_password()`, `graceful_exit()`.

---

### FASE 2: Implementasi Query Agregasi Dashboard

> **Lokasi file**: `db/query_builder.py`
> **Layer**: Data Access Layer (Layer 3)

- [ ] **2.1** Baca file `db/query_builder.py` yang sudah ada. Pahami pola fungsi yang sudah ada di dalamnya.

- [ ] **2.2** Tambahkan fungsi `query_dashboard_pemilik(db_connection, cabang_id: int, tanggal: str) -> Result` yang menjalankan query berikut secara parameterized:

  ```
  Query yang HARUS dijalankan:
  a) Total pendapatan hari ini:
     SELECT COALESCE(SUM(total_bayar), 0) AS total_pendapatan
     FROM transaksi
     WHERE DATE(tanggal_transaksi) = %s
       AND status_pembayaran IN ('LUNAS','BELUM LUNAS')
       AND cabang_id = %s

  b) Total pengeluaran hari ini:
     SELECT COALESCE(SUM(nominal), 0) AS total_pengeluaran
     FROM pengeluaran
     WHERE tanggal_pengeluaran = %s AND cabang_id = %s

  c) Total kerugian limbah hari ini:
     SELECT COALESCE(SUM(kerugian_nominal), 0) AS total_limbah
     FROM limbah_produksi
     WHERE DATE(tanggal_pencatatan) = %s AND cabang_id = %s

  d) Jumlah transaksi per status pembayaran hari ini:
     SELECT status_pembayaran, COUNT(*) AS jumlah
     FROM transaksi
     WHERE DATE(tanggal_transaksi) = %s AND cabang_id = %s
     GROUP BY status_pembayaran

  e) Alert jatuh tempo pinjaman bank (H-3):
     SELECT tipe_bank, setoran_bulanan, tanggal_jatuh_tempo,
            DATEDIFF(tanggal_jatuh_tempo, CURDATE()) AS sisa_hari
     FROM pinjaman_bank
     WHERE status_pinjaman = 'BELUM LUNAS'
       AND DATEDIFF(tanggal_jatuh_tempo, CURDATE()) <= 3
       AND DATEDIFF(tanggal_jatuh_tempo, CURDATE()) >= 0
       AND cabang_id = %s

  f) Alert jatuh tempo utang supplier (H-3):
     SELECT s.nama_supplier, u.sisa_utang, u.tanggal_jatuh_tempo,
            DATEDIFF(u.tanggal_jatuh_tempo, CURDATE()) AS sisa_hari
     FROM utang_supplier u
     JOIN supplier s ON u.supplier_id = s.id
     WHERE u.status_utang = 'BELUM LUNAS'
       AND DATEDIFF(u.tanggal_jatuh_tempo, CURDATE()) <= 3
       AND DATEDIFF(u.tanggal_jatuh_tempo, CURDATE()) >= 0
       AND u.cabang_id = %s
  ```

  **Aturan**:
  - Return `Result(is_success=True, data=dict_berisi_semua_data, error_msg=None)` jika sukses
  - Return `Result(is_success=False, data=None, error_msg='ERR-DB-...')` jika gagal
  - Gunakan `Decimal` untuk semua nominal uang
  - Tangkap exception database, jangan biarkan crash

- [ ] **2.3** Tambahkan fungsi `query_dashboard_kasir(db_connection, user_id: int, cabang_id: int, tanggal: str) -> Result`:

  ```
  Query yang HARUS dijalankan:
  a) Jumlah & total transaksi shift aktif kasir hari ini:
     SELECT COUNT(*) AS jumlah_nota, COALESCE(SUM(total_bayar), 0) AS total_kas
     FROM transaksi
     WHERE kasir_id = %s AND DATE(tanggal_transaksi) = %s AND cabang_id = %s

  b) Jumlah invoice BELUM LUNAS (pesanan DP):
     SELECT COUNT(*) AS jumlah_belum_lunas
     FROM transaksi
     WHERE status_pembayaran = 'BELUM LUNAS'
       AND DATE(tanggal_transaksi) = %s AND cabang_id = %s

  c) Saldo virtual PPOB (2 akun):
     SELECT akun_tipe, saldo_terakhir
     FROM saldo_ppob WHERE cabang_id = %s
  ```

- [ ] **2.4** Tambahkan fungsi `query_dashboard_operasional(db_connection, cabang_id: int) -> Result`:

  ```
  Query yang HARUS dijalankan:
  a) Jumlah antrian kerja per status:
     SELECT status_antrian, COUNT(*) AS jumlah
     FROM antrian_kerja WHERE cabang_id = %s
     GROUP BY status_antrian

  b) Alert stok bahan baku kritis (stok < minimum yang wajar):
     SELECT nama_barang, stok_saat_ini, satuan_uom
     FROM barang
     WHERE tipe_barang = 'Bahan_Baku'
       AND stok_saat_ini <= 5.0000
       AND cabang_id = %s
     ORDER BY stok_saat_ini ASC
     LIMIT 10
  ```

- [ ] **2.5** Tambahkan fungsi `query_dashboard_kepala(db_connection, cabang_id: int, tanggal: str) -> Result`:

  ```
  Query yang HARUS dijalankan:
  a) Jumlah staf hadir hari ini:
     SELECT COUNT(*) AS jumlah_hadir
     FROM absensi
     WHERE tanggal = %s AND status_kehadiran = 'Hadir' AND cabang_id = %s

  b) Total staf terdaftar:
     SELECT COUNT(*) AS total_staf
     FROM pengguna WHERE cabang_id = %s AND role != 'pemilik'

  c) Draf stock opname pending approval:
     SELECT COUNT(*) AS draf_pending
     FROM stock_opname
     WHERE status_opname = 'DRAFT' AND cabang_id = %s

  d) Antrian kerja aktif (reuse query_dashboard_operasional query a)
  ```

- [ ] **2.6** Tambahkan fungsi `query_dashboard_gudang(db_connection, cabang_id: int) -> Result`:

  ```
  Query yang HARUS dijalankan:
  a) Alert stok bahan baku kritis (reuse query operasional)
  b) Draf stock opname pending:
     SELECT COUNT(*) AS draf_pending
     FROM stock_opname
     WHERE status_opname = 'DRAFT' AND cabang_id = %s
  c) Utang supplier jatuh tempo:
     SELECT s.nama_supplier, u.sisa_utang, u.tanggal_jatuh_tempo
     FROM utang_supplier u
     JOIN supplier s ON u.supplier_id = s.id
     WHERE u.status_utang = 'BELUM LUNAS'
       AND DATEDIFF(u.tanggal_jatuh_tempo, CURDATE()) <= 7
       AND u.cabang_id = %s
     ORDER BY u.tanggal_jatuh_tempo ASC
  ```

- [ ] **2.7** Pastikan SEMUA fungsi query baru:
  - Menggunakan parameterized query (`%s`)
  - Return `Result` NamedTuple
  - Memiliki docstring PEP 257
  - Menutup cursor dengan benar (gunakan try-finally)
  - Menangkap exception `mysql.connector.Error` dan mengembalikan `Result(False, None, error_msg)`
  - Tidak mengimpor modul dari `cli/` (larangan dependensi Layer 3 ke Layer 1)

---

### FASE 3: Implementasi Logic Kalkulasi (jika diperlukan)

> **Lokasi file**: `logic/` (file yang sesuai)
> **Layer**: Business Logic Layer (Layer 2)

- [ ] **3.1** Buat fungsi pure `hitung_laba_bersih_harian(total_pendapatan: Decimal, total_pengeluaran: Decimal, total_limbah: Decimal) -> Decimal` jika diperlukan kalkulasi laba rugi sederhana untuk dashboard pemilik.

  ```python
  def hitung_laba_bersih_harian(
      total_pendapatan: Decimal,
      total_pengeluaran: Decimal,
      total_limbah: Decimal
  ) -> Decimal:
      """Menghitung estimasi laba bersih harian sederhana.

      (Ref: UC-043 Skenario A — Dashboard Pemilik)

      Args:
          total_pendapatan: Total kas masuk transaksi hari ini.
          total_pengeluaran: Total kas keluar pengeluaran hari ini.
          total_limbah: Total kerugian limbah produksi hari ini.

      Returns:
          Decimal: Estimasi laba bersih harian (bisa negatif jika rugi).
      """
      return (total_pendapatan - total_pengeluaran - total_limbah).quantize(
          Decimal('0.0001'), rounding=ROUND_HALF_UP
      )
  ```

- [ ] **3.2** Tempatkan fungsi ini di file logic yang paling sesuai (misalnya `logic/financial_engine.py`) atau buat helper baru jika tidak ada tempat yang cocok. Pastikan:
  - Fungsi adalah pure function (tidak ada side effect)
  - Menggunakan `decimal.Decimal` dan `ROUND_HALF_UP`
  - Memiliki type hints lengkap

---

### FASE 4: Implementasi Visual Dashboard

> **Lokasi file**: `cli/dashboard.py`
> **Layer**: Presentation Layer (Layer 1)

- [ ] **4.1** Buat fungsi internal `_render_summary_panels(session_state: dict) -> None` yang dipanggil di dalam `render_dashboard()` **SEBELUM** menu navigasi modul ditampilkan. Fungsi ini bertanggung jawab menampilkan panel ringkasan harian sesuai role.

- [ ] **4.2** Di dalam `_render_summary_panels()`, implementasikan logika branching per role:

  ```python
  role = session_state.get('role', '')

  if role == 'pemilik':
      _render_dashboard_pemilik(session_state)
  elif role == 'kepala_percetakan':
      _render_dashboard_kepala(session_state)
  elif role == 'kasir':
      _render_dashboard_kasir(session_state)
  elif role in ('desainer', 'produksi_cetak'):
      _render_dashboard_operasional(session_state)
  elif role == 'gudang':
      _render_dashboard_gudang(session_state)
  elif role == 'pramuniaga':
      _render_dashboard_pramuniaga(session_state)
  elif role == 'fotocopy_print':
      _render_dashboard_fotocopy(session_state)
  ```

- [ ] **4.3** Implementasikan `_render_dashboard_pemilik(session_state: dict) -> None`:

  ```
  Tampilan yang HARUS dirender:

  ╔══════════════════════════════════════════════════════╗
  ║  📊 RINGKASAN HARIAN TOKO — [Tanggal Hari Ini]     ║
  ╠══════════════════════════════════════════════════════╣
  ║                                                      ║
  ║  💰 Total Pendapatan    : Rp XX.XXX.XXXX             ║
  ║  💸 Total Pengeluaran   : Rp XX.XXX.XXXX             ║
  ║  🗑️ Kerugian Limbah     : Rp XX.XXX.XXXX             ║
  ║  ────────────────────────────────────                 ║
  ║  📈 Estimasi Laba Bersih: Rp XX.XXX.XXXX  [GREEN]    ║
  ║                            atau            [RED]      ║
  ╠══════════════════════════════════════════════════════╣
  ║  Status Transaksi Hari Ini:                          ║
  ║  ┌──────────────┬────────┐                           ║
  ║  │ Status       │ Jumlah │                           ║
  ║  ├──────────────┼────────┤                           ║
  ║  │ LUNAS        │     12 │                           ║
  ║  │ BELUM LUNAS  │      3 │                           ║
  ║  │ BATAL        │      0 │                           ║
  ║  │ RETUR        │      1 │                           ║
  ║  └──────────────┴────────┘                           ║
  ╠══════════════════════════════════════════════════════╣
  ║  ⚠️ PERINGATAN JATUH TEMPO (H-3):                    ║
  ║  • Bank Mandiri - Cicilan Rp 2.500.000               ║
  ║    Jatuh tempo: 2026-06-09 (2 hari lagi)  [YELLOW]   ║
  ║  • Supplier CV Maju - Utang Rp 1.200.000             ║
  ║    Jatuh tempo: 2026-06-08 (1 hari lagi)  [YELLOW]   ║
  ╚══════════════════════════════════════════════════════╝
  ```

  **Aturan Visual:**
  - Gunakan `rich.panel.Panel` untuk bingkai
  - Gunakan `tabulate` untuk tabel status transaksi
  - Laba bersih positif = warna hijau `[bold green]`
  - Laba bersih negatif = warna merah `[bold red]` dengan teks "RUGI"
  - Alert jatuh tempo = warna kuning `[bold yellow]` berkedip (jika rich mendukung `blink`)
  - Semua nominal diformat Rupiah dengan separator ribuan: `Rp {:,.4f}`
  - Jika tidak ada data transaksi hari ini, tampilkan pesan: "Belum ada transaksi hari ini."
  - Jika tidak ada alert jatuh tempo, tampilkan: "✓ Tidak ada utang jatuh tempo dalam 3 hari."

- [ ] **4.4** Implementasikan `_render_dashboard_kasir(session_state: dict) -> None`:

  ```
  Tampilan yang HARUS dirender:

  ╔══════════════════════════════════════════════════════╗
  ║  🧾 DASHBOARD KASIR — [Username] — [Tanggal]        ║
  ╠══════════════════════════════════════════════════════╣
  ║  Jumlah Nota Hari Ini   : 15 nota                   ║
  ║  Total Kas Masuk        : Rp 2.500.000,0000          ║
  ║  Invoice BELUM LUNAS    : 3 nota  [YELLOW]           ║
  ╠══════════════════════════════════════════════════════╣
  ║  Saldo PPOB:                                         ║
  ║  ┌──────────────────┬────────────────────┐           ║
  ║  │ Akun PPOB        │ Saldo Terakhir     │           ║
  ║  ├──────────────────┼────────────────────┤           ║
  ║  │ Pulsa & Data     │ Rp 450.000,0000    │           ║
  ║  │ Token & Tagihan  │ Rp 180.000,0000 ⚠️ │  [YELLOW] ║
  ║  └──────────────────┴────────────────────┘           ║
  ║  ⚠️ PERINGATAN: Saldo Token & Tagihan < Rp 150.000!  ║
  ╚══════════════════════════════════════════════════════╝
  ```

  **Aturan Visual:**
  - Saldo PPOB < Rp 150.000 → warna kuning + icon ⚠️
  - Invoice belum lunas > 0 → warna kuning
  - Semua nominal format Rupiah

- [ ] **4.5** Implementasikan `_render_dashboard_operasional(session_state: dict) -> None` (untuk `desainer` dan `produksi_cetak`):

  ```
  Tampilan yang HARUS dirender:

  ╔══════════════════════════════════════════════════════╗
  ║  🏭 DASHBOARD OPERASIONAL — [Username] — [Tanggal]  ║
  ╠══════════════════════════════════════════════════════╣
  ║  Status Antrian Kerja:                               ║
  ║  ┌──────────────────┬────────┐                       ║
  ║  │ Status Antrian   │ Jumlah │                       ║
  ║  ├──────────────────┼────────┤                       ║
  ║  │ Antri            │      5 │                       ║
  ║  │ Proses Desain    │      2 │                       ║
  ║  │ Produksi         │      3 │                       ║
  ║  │ Selesai          │      1 │                       ║
  ║  │ Diambil          │      8 │                       ║
  ║  └──────────────────┴────────┘                       ║
  ╠══════════════════════════════════════════════════════╣
  ║  ⚠️ Stok Bahan Baku KRITIS:                          ║
  ║  ┌────────────────────────┬──────────┬────────┐      ║
  ║  │ Nama Barang            │ Sisa     │ Satuan │      ║
  ║  ├────────────────────────┼──────────┼────────┤      ║
  ║  │ Tinta Pigmen Hitam     │   2.5000 │ liter  │      ║
  ║  │ Kertas Buffalo A4      │  10.0000 │ lembar │      ║
  ║  └────────────────────────┴──────────┴────────┘      ║
  ╚══════════════════════════════════════════════════════╝
  ```

- [ ] **4.6** Implementasikan `_render_dashboard_kepala(session_state: dict) -> None` (untuk `kepala_percetakan`):

  ```
  Tampilan:
  - Jumlah staf hadir hari ini vs total staf
  - Antrian kerja aktif (tabel status)
  - Jumlah draf stock opname yang menunggu approval
  ```

- [ ] **4.7** Implementasikan `_render_dashboard_gudang(session_state: dict) -> None`:

  ```
  Tampilan:
  - Alert stok bahan baku kritis (tabel)
  - Draf stock opname pending approval (jumlah)
  - Utang supplier mendekati jatuh tempo (tabel, H-7)
  ```

- [ ] **4.8** Implementasikan `_render_dashboard_pramuniaga(session_state: dict) -> None`:

  ```
  Tampilan ringkasan sederhana:
  - Jumlah antrian pesanan masuk status 'Antri'
  - Pesan selamat bekerja
  ```

- [ ] **4.9** Implementasikan `_render_dashboard_fotocopy(session_state: dict) -> None`:

  ```
  Tampilan ringkasan sederhana:
  - Pesan selamat bekerja
  - Jumlah transaksi fotocopy/print hari ini (jika bisa diidentifikasi)
  ```

- [ ] **4.10** Integrasikan pemanggilan `_render_summary_panels(session_state)` di dalam fungsi `render_dashboard()` yang sudah ada:

  **Posisi pemanggilan:** Setelah render header dashboard (Panel info pengguna) dan SEBELUM render menu navigasi modul.

  ```python
  # Lokasi yang TEPAT di render_dashboard() untuk menyisipkan:
  # Setelah baris: _console.print(Panel(..., title=..., ...))
  # Sebelum baris: _console.print("PILIHAN MODUL:")

  # Sisipkan:
  _render_summary_panels(session_state)
  ```

  > [!CAUTION]
  > **PERHATIAN**: Fungsi `render_dashboard()` sudah memiliki loop `while True` dan logika validasi token, header panel, menu navigasi, dan input handling yang sudah BERFUNGSI. Jangan mengubah logika tersebut. Hanya SISIPKAN pemanggilan `_render_summary_panels()` di posisi yang tepat.

- [ ] **4.11** Pastikan setiap fungsi render dashboard memiliki fallback non-`rich`:
  - Jika `HAS_RICH` bernilai `False`, gunakan `print()` biasa dengan border `═══`
  - Jika `tabulate` tidak tersedia, gunakan format manual string alignment

- [ ] **4.12** Pastikan error handling yang benar:
  - Jika koneksi database gagal saat memuat ringkasan → tampilkan pesan warning kuning tetapi **JANGAN hentikan dashboard**. Lanjutkan render menu navigasi seperti biasa.
  - Jika query mengembalikan data kosong → tampilkan pesan "Belum ada data untuk ditampilkan."

---

### FASE 5: Integrasi & Pengujian

- [ ] **5.1** Jalankan aplikasi dan login sebagai setiap role satu per satu:
  - [ ] Login sebagai `pemilik` → verifikasi dashboard keuangan lengkap tampil
  - [ ] Login sebagai `kasir` → verifikasi dashboard kasir tampil (nota, PPOB, DP)
  - [ ] Login sebagai `desainer` → verifikasi dashboard operasional tampil (antrian, stok)
  - [ ] Login sebagai `produksi_cetak` → verifikasi dashboard operasional tampil
  - [ ] Login sebagai `kepala_percetakan` → verifikasi dashboard supervisor tampil
  - [ ] Login sebagai `gudang` → verifikasi dashboard gudang tampil (stok, opname, utang)
  - [ ] Login sebagai `pramuniaga` → verifikasi dashboard pramuniaga tampil
  - [ ] Login sebagai `fotocopy_print` → verifikasi dashboard fotocopy tampil

- [ ] **5.2** Verifikasi navigasi tetap berfungsi setelah modifikasi:
  - [ ] Pilih modul M.1 s.d M.10 → menu sub-modul tampil normal
  - [ ] Tekan `P` → form ubah password tetap berfungsi
  - [ ] Tekan `0` → proses logout berjalan normal
  - [ ] Tekan `q` → graceful exit berfungsi
  - [ ] Tekan `Ctrl+C` → graceful exit berfungsi

- [ ] **5.3** Verifikasi error handling:
  - [ ] Matikan koneksi database → dashboard tetap tampil (tanpa data ringkasan, dengan pesan warning)
  - [ ] Database kosong (tidak ada transaksi) → dashboard tampil dengan pesan "Belum ada data"

- [ ] **5.4** Verifikasi cross-OS (jika memungkinkan):
  - [ ] Jalankan di Windows 11 → Unicode box characters tampil benar
  - [ ] Jalankan di Linux Debian 12 → ANSI colors tampil benar

---

### FASE 6: Review Kualitas & Finalisasi

- [ ] **6.1** Review ulang kode yang ditulis:
  - [ ] Semua fungsi publik memiliki docstring PEP 257 lengkap (Args, Returns, referensi)
  - [ ] Semua fungsi menggunakan type hints (PEP 484)
  - [ ] Semua query SQL menggunakan parameterized binding `%s`
  - [ ] Tidak ada `float` — semua nominal menggunakan `Decimal`
  - [ ] Tidak ada `class` di alur bisnis
  - [ ] Penamaan variabel dan fungsi konsisten `snake_case`
  - [ ] Konstanta menggunakan `UPPER_SNAKE_CASE`
  - [ ] Import terurut: standard → third-party → local
  - [ ] Tidak ada wildcard import `from x import *`
  - [ ] Panjang baris ≤ 120 karakter
  - [ ] Indentasi 4 spasi (bukan Tab)

- [ ] **6.2** Verifikasi tidak ada feature lain yang rusak:
  - [ ] Fungsi `show_module_submenu()` tidak dimodifikasi
  - [ ] Fungsi `handle_navigation()` tidak dimodifikasi secara substansial
  - [ ] Fungsi `form_ubah_password()` tidak dimodifikasi
  - [ ] Fungsi `graceful_exit()` tidak dimodifikasi
  - [ ] File lain di `cli/` tidak terpengaruh

- [ ] **6.3** Pastikan semua TODO/FIXME yang ditandai telah dicatat:
  - [ ] Buat daftar TODO dengan penjelasan apa yang perlu diklarifikasi
  - [ ] Tandai di komentar kode jika ada data yang tidak tersedia dari referensi

- [ ] **6.4** Jalankan test suite yang sudah ada (jika tersedia):
  ```bash
  python -m pytest tests/ -v
  ```
  Pastikan tidak ada test yang FAIL akibat perubahan.

---

## 7. Instruksi Tambahan Khusus untuk Feature Ini

### 7.1. Format Angka Rupiah

Gunakan helper formatting yang konsisten untuk menampilkan nominal Rupiah di dashboard:

```python
from decimal import Decimal

def format_rupiah(nominal: Decimal) -> str:
    """Format nominal Decimal ke string Rupiah dengan separator ribuan."""
    return f"Rp {nominal:,.4f}"
```

### 7.2. Penentuan Tanggal Hari Ini

Gunakan `datetime.date.today()` untuk menentukan tanggal hari ini pada setiap query dashboard. Jangan hardcode tanggal.

```python
from datetime import date
tanggal_hari_ini = date.today().isoformat()  # '2026-06-07'
```

### 7.3. Koneksi Database

Gunakan pattern yang sudah ada di codebase:

```python
from db.db_connector import get_db_connection

conn_res = get_db_connection()
if not conn_res.is_success:
    # Tampilkan warning tapi jangan crash
    print(f"⚠️ {conn_res.error_msg}")
    return
db_conn = conn_res.data
try:
    # ... jalankan query ...
finally:
    try:
        db_conn.close()
    except Exception:
        pass
```

### 7.4. Cabang ID

Selalu filter query berdasarkan `cabang_id` dari `session_state.get('cabang_id', 1)` untuk mendukung arsitektur multi-cabang.

### 7.5. Performa Query Dashboard

Dashboard harus merender dalam waktu < 2 detik. Gunakan query agregasi (`SUM`, `COUNT`, `GROUP BY`) daripada mengambil semua row lalu menghitung di Python.

### 7.6. Fallback Visual tanpa Rich/Tabulate

Pastikan kode memiliki fallback jika library `rich` atau `tabulate` tidak tersedia (gunakan pengecekan `HAS_RICH` yang sudah ada di file, dan tambahkan pengecekan serupa untuk `tabulate`).

```python
try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False
```

### 7.7. Audit Trail

Dashboard ini adalah fitur READ-ONLY. Tidak perlu mencatat audit trail karena tidak ada modifikasi data. Namun jika di masa depan ada kebutuhan, catat di komentar `# NOTE: Dashboard read-only, tidak memicu audit trail`.

---

## 8. Daftar File yang Akan Dimodifikasi/Dibuat

| # | File | Aksi | Deskripsi Perubahan |
|---|---|---|---|
| 1 | `cli/dashboard.py` | **MODIFY** | Menambahkan fungsi `_render_summary_panels()` dan 7 fungsi render dashboard per role. Menyisipkan pemanggilan di `render_dashboard()`. |
| 2 | `db/query_builder.py` | **MODIFY** | Menambahkan 5 fungsi query agregasi dashboard: `query_dashboard_pemilik()`, `query_dashboard_kasir()`, `query_dashboard_operasional()`, `query_dashboard_kepala()`, `query_dashboard_gudang()`. |
| 3 | `logic/financial_engine.py` | **MODIFY** (opsional) | Menambahkan fungsi `hitung_laba_bersih_harian()` jika belum ada. |

> [!IMPORTANT]
> **TIDAK ADA FILE BARU** yang dibuat. Semua perubahan masuk ke file yang sudah ada sesuai arsitektur modular 4-layer yang telah ditetapkan.

---

## 9. Traceability Matrix

| Deliverable | UC | SRS | BRD | ACM | CLI Flow | Module Structure |
|---|---|---|---|---|---|---|
| Dashboard Pemilik | UC-043 (Skenario A) | SRS-NF-011 | BR-NF-11 | ACM-BASE-003 | Bab 4.3 Step 3a | Bab 4.2 `dashboard.py` |
| Dashboard Kasir | UC-043 (Skenario B) | SRS-NF-011 | BR-NF-11 | ACM-BASE-003 | Bab 4.3 Step 3b | Bab 4.2 `dashboard.py` |
| Dashboard Operasional | UC-043 (Skenario C) | SRS-NF-011 | BR-NF-11 | ACM-BASE-003 | Bab 4.3 Step 3c | Bab 4.2 `dashboard.py` |
| Alert Jatuh Tempo H-3 | UC-029 | SRS-F-027 | BR-F-27 | ACM-M6-003 | Bab 4.3 Step 3a | Bab 4.2 `dashboard.py` |
| Alert Stok Kritis | UC-012 | SRS-F-012 | BR-F-12 | ACM-M2-006 | Bab 4.3 Step 3c | Bab 4.2 `dashboard.py` |
| Alert PPOB Kritis | UC-017 | SRS-F-015 | BR-F-15 | ACM-M3-001 | Bab 4.3 Step 3b | Bab 4.2 `dashboard.py` |

---

## 10. Kriteria Selesai (Definition of Done)

- [ ] Seluruh 8 role menampilkan dashboard ringkasan harian yang relevan dengan perannya
- [ ] Dashboard pemilik menampilkan: laba bersih, status transaksi, alert jatuh tempo
- [ ] Dashboard kasir menampilkan: jumlah nota, kas masuk, saldo PPOB, invoice DP
- [ ] Dashboard operasional menampilkan: antrian kerja, stok kritis
- [ ] Dashboard kepala menampilkan: kehadiran staf, antrian kerja, draf opname pending
- [ ] Dashboard gudang menampilkan: stok kritis, draf opname, utang supplier
- [ ] Navigasi menu modul (M.1-M.10) tetap berfungsi normal
- [ ] Login, logout, ubah password, graceful exit tetap berfungsi normal
- [ ] Tidak ada test suite yang FAIL akibat perubahan
- [ ] Kode mengikuti Coding Standard AbuCom v1.2 (FP murni, parameterized SQL, Decimal, type hints, docstring)
- [ ] Penanganan error database: dashboard tetap tampil meskipun koneksi database gagal
