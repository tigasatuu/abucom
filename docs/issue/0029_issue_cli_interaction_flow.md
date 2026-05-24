# Pembuatan & Penyusunan Dokumen CLI Interaction Flow

---

## Informasi Issue

| Atribut            | Nilai                                                            |
| :----------------- | :--------------------------------------------------------------- |
| **Judul**          | Pembuatan & Penyusunan Dokumen CLI Interaction Flow              |
| **Dokumen Utama**  | CLI Interaction Flow                                             |
| **Target File**    | `docs/sdlc/03_design/04_cli_interaction_flow.md`                 |
| **Prioritas**      | High                                                             |
| **Status**         | Open                                                             |
| **Tanggal Dibuat** | 2026-05-24                                                       |
| **Dibuat Oleh**    | Senior Solutions Architect & System Design Lead (Antigravity IDE) |

---

## 1. Persona Pelaksana

**Persona yang WAJIB digunakan saat mengerjakan issue ini:**

> **Senior UX/CLI Interaction Designer & Terminal Interface Architect**

**Deskripsi Peran:**
Seorang spesialis perancangan antarmuka pengguna berbasis terminal (CLI/TUI) dengan keahlian mendalam dalam merancang hierarki menu navigasi, alur interaksi pengguna step-by-step, pemetaan input/output terminal, validasi UX accessibility keyboard-only, dan standarisasi pola navigasi konsisten di seluruh modul sistem. Persona ini memiliki otoritas penuh untuk menentukan:

1. **Struktur hierarki menu CLI** — Bagaimana menu utama, sub-menu, dan menu tertinggi diorganisir secara logis berdasarkan 10 modul fungsional dan 8 peran pengguna (RBAC).
2. **Alur interaksi step-by-step** — Urutan prompt input, output tampilan, feedback visual, pesan error, dan navigasi kembali untuk setiap use case (UC-001 s.d UC-044).
3. **Pola desain UX terminal** — Standar hotkey navigasi (`0` = kembali), layout tabel `rich`/`tabulate`, format prompt input `getpass`, indikator warna status ANSI, dan pola konfirmasi aksi destruktif.
4. **Matriks interaksi per-role** — Pemetaan menu mana saja yang ditampilkan/disembunyikan berdasarkan role JWT session aktif.
5. **Wireframe terminal teks (mockup ASCII/ANSI)** — Contoh representasi visual tampilan layar CLI untuk setiap screen kritis.

---

## 2. File Referensi yang WAJIB Dibaca

Berikut adalah daftar file referensi yang **WAJIB** dibaca secara menyeluruh sebelum memulai penyusunan dokumen utama. Urutan pembacaan menunjukkan prioritas relevansi:

| No | File Referensi                   | Path Relatif                                           | Prioritas    | Alasan Penggunaan                                                                                                                                                    |
| :-: | :------------------------------- | :----------------------------------------------------- | :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | **Use Case Diagram v1.1**        | `docs/sdlc/02_analysis/03_use_case_diagram.md`         | **PRIMER**   | Sumber utama 44 use case (UC-001 s.d UC-044) beserta spesifikasi naratif Main Flow, Alternative Flow, dan Exception Flow yang menjadi dasar alur interaksi CLI.      |
| 2  | **Software Requirements (SRS) v1.1** | `docs/sdlc/02_analysis/02_software_requirements.md`    | **PRIMER**   | Spesifikasi teknis input/output/validasi setiap fungsionalitas, 8 aktor sistem, wireframe terminal CLI contoh, dan kode error standar `ERR-[KATEGORI]-[NOMOR]`.     |
| 3  | **Access Control Matrix v1.1**   | `docs/sdlc/02_analysis/06_access_control_matrix.md`    | **PRIMER**   | Matriks granular hak akses 8 peran terhadap 44 menu CLI dan 28 tabel database. Penentu utama menu mana yang ditampilkan/disembunyikan per role.                      |
| 4  | **System Architecture v1.1**     | `docs/sdlc/03_design/03_system_architecture.md`        | **SEKUNDER** | Arsitektur 4-layer (Presentation Layer sebagai CLI), pola FP, sequence diagram alur login/transaksi/shift handover, dan diagram deployment dual-OS.                  |
| 5  | **Workflow Diagram v1.1**        | `docs/sdlc/02_analysis/04_workflow_diagram.md`         | **SEKUNDER** | 38 alur kerja To-Be per modul yang menggambarkan langkah-langkah operasional harian, decision points, dan subprocess calls antar workflow.                           |
| 6  | **Database Schema v1.1**         | `docs/sdlc/03_design/01_database_schema.sql`           | **TERSIER**  | Skema fisik 28 tabel untuk memahami field input yang harus diminta di form CLI (nama kolom, tipe data, constraint NOT NULL, default values).                         |
| 7  | **ERD Database v1.1**            | `docs/sdlc/03_design/02_erd_database.md`               | **TERSIER**  | Visualisasi relasi antar tabel untuk memahami dependensi data yang mempengaruhi alur navigasi menu (misal: transaksi butuh pelanggan_id dari CRM).                   |
| 8  | **Data Dictionary v1.1**         | `docs/sdlc/02_analysis/05_data_dictionary.md`          | **TERSIER**  | Kamus data lengkap setiap kolom tabel (tipe, panjang, deskripsi) untuk menyusun label prompt input CLI secara akurat.                                                |
| 9  | **Business Requirements (BRD) v1.1** | `docs/sdlc/02_analysis/01_business_requirements.md`    | **TERSIER**  | Konteks kebutuhan bisnis pemilik untuk memastikan alur interaksi CLI selaras dengan harapan operasional nyata di toko.                                                |

> **Catatan**: File `narasi.txt` (`docs/sdlc/narasi.txt`) **TIDAK lagi digunakan** sebagai referensi langsung karena seluruh informasi naratif pemilik telah diserap dan dikonsolidasi secara formal ke dalam dokumen BRD v1.1, SRS v1.1, dan UCD v1.1.

---

## 3. Kerangka Struktur Dokumen Utama

Dokumen `04_cli_interaction_flow.md` **WAJIB** disusun mengikuti kerangka struktur berikut. Kerangka ini mengacu pada standar praktik industri perancangan antarmuka CLI (*CLI Design Specification*) yang digabungkan dengan elemen *User Interaction Flow Document* dan *Screen Flow Diagram*:

```
---
dokumen    : CLI Interaction Flow
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : [TANGGAL PENGERJAAN]
status     : Draft
penyusun   : Senior UX/CLI Interaction Designer & Terminal Interface Architect
---

# CLI Interaction Flow — AbuCom

## Riwayat Perubahan Dokumen
(Tabel versi, tanggal, perubahan, oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target
### 1.6. Definisi, Akronim, dan Singkatan

---

## 2. Prinsip Desain Interaksi CLI
### 2.1. Filosofi UX Terminal AbuCom
### 2.2. Konvensi Navigasi Global
   (Tombol 0 = Kembali, hotkey numerik, pola konfirmasi Y/N, dsb)
### 2.3. Konvensi Visual & Pustaka Tampilan
   (Penggunaan `rich` panels, `tabulate` tabel, warna ANSI, ikon status)
### 2.4. Konvensi Input & Validasi
   (Pola input `getpass`, sanitasi ASCII, format desimal, regex pattern)
### 2.5. Konvensi Pesan Error & Feedback
   (Format kode error ERR-[KATEGORI]-[NOMOR], warna merah/kuning)
### 2.6. Konvensi Aksesibilitas & Portabilitas
   (Keyboard-only, UTF-8, dual-OS Windows/Debian, `chcp 65001`)

---

## 3. Peta Hierarki Menu CLI Global
### 3.1. Diagram Hierarki Menu Utama (Mermaid Tree)
### 3.2. Deskripsi Singkat Setiap Node Menu
### 3.3. Matriks Visibilitas Menu per Role (8 Peran)
   (Tabel menu x role → Tampil/Sembunyi berdasarkan ACM v1.1)

---

## 4. Alur Interaksi Dasar Sistem (Use Case Dasar)
### 4.1. Alur Interaksi: Login ke Sistem (UC-041)
   (Step-by-step prompt, getpass, bcrypt verify, JWT generate, rate limiting)
### 4.2. Alur Interaksi: Logout dari Sistem (UC-042)
   (Konfirmasi, hapus token JWT, clear screen, redirect login)
### 4.3. Alur Interaksi: Dashboard Utama per Role (UC-043)
   (Tampilan dashboard berbeda per role, ringkasan harian, alert)
### 4.4. Alur Interaksi: Ubah Password Akun Sendiri (UC-044)
   (Verifikasi password lama, input baru 2x, bcrypt re-hash)

---

## 5. Alur Interaksi Modul M.1 — Transaksi & Kebijakan Harga
### 5.1. Alur: Mencatat Transaksi Penjualan Multi-Divisi (UC-001)
### 5.2. Alur: Mengubah Skema Harga Otomatis (UC-002)
### 5.3. Alur: Mengelola Pembayaran DP & Pelunasan (UC-003)
### 5.4. Alur: Memproses Pembatalan & Retur (UC-004)
### 5.5. Alur: Melacak Margin Keuntungan per Produk (UC-005)
### 5.6. Alur: Mengekspor Struk Nota Thermal (UC-006)

---

## 6. Alur Interaksi Modul M.2 — Inventaris, BOM & Stock Opname
### 6.1. Alur: Menghitung HPP Otomatis Berbasis BOM (UC-007)
### 6.2. Alur: Mencatat Limbah Produksi (UC-008)
### 6.3. Alur: Mengelola Satuan & Atribut Barang UoM (UC-009)
### 6.4. Alur: Sinkronisasi Pengambilan ATK Internal (UC-010)
### 6.5. Alur: Memproses Rekonsiliasi Stok / Stock Opname (UC-011)
### 6.6. Alur: Menganalisis Prediksi Re-Order Stok (UC-012)
### 6.7. Alur: Melacak Riwayat Harga Supplier (UC-013)
### 6.8. Alur: Mengimpor Data CSV Semiautomatis (UC-014)
### 6.9. Alur: Mengelola Supplier & Utang Usaha (UC-015)
### 6.10. Alur: Backup & Restore Database (UC-016)

---

## 7. Alur Interaksi Modul M.3 — Keuangan Digital, PPOB & Service
### 7.1. Alur: Mengelola Saldo PPOB & Alert Deposit (UC-017)
### 7.2. Alur: Menentukan Akun Jasa Keuangan Terhemat (UC-018)
### 7.3. Alur: Mencatat Transaksi Jasa Service (UC-019)

---

## 8. Alur Interaksi Modul M.4 — SDM, Penggajian & Poin
### 8.1. Alur: Mengelola Data Karyawan, Absensi & Kasbon (UC-020)
### 8.2. Alur: Memproses Smart Payroll (UC-021)
### 8.3. Alur: Mengakumulasi Poin Insentif Karyawan (UC-022)
### 8.4. Alur: Memotong Gaji Otomatis atas Kasbon (UC-023)

---

## 9. Alur Interaksi Modul M.5 — Antrian & Pelacakan Desain
### 9.1. Alur: Melacak Status Antrian Pekerjaan (UC-024)
### 9.2. Alur: Mengelola Arsip Desain Pelanggan (UC-025)
### 9.3. Alur: Membuat Link Notifikasi WhatsApp (UC-026)

---

## 10. Alur Interaksi Modul M.6 — Pinjaman, Aset & Pengeluaran
### 10.1. Alur: Mengelola Pinjaman Modal (UC-027)
### 10.2. Alur: Melihat Laporan Laba/Rugi Instan per Divisi (UC-028)
### 10.3. Alur: Menerima Notifikasi Jatuh Tempo H-3 (UC-029)
### 10.4. Alur: Mengelola Aset Tetap & Depresiasi (UC-030)
### 10.5. Alur: Mengelola Pengeluaran Rutin (UC-031)

---

## 11. Alur Interaksi Modul M.7 — Keamanan, Audit & Hak Akses
### 11.1. Alur: Mengakses Menu RBAC Multi-Level (UC-032)
### 11.2. Alur: Mengaudit Log Audit Trail JSON (UC-033)
### 11.3. Alur: Serah Terima Shift Karyawan (UC-034)
### 11.4. Alur: Rekonsiliasi Kas Harian (UC-035)
### 11.5. Alur: Memantau Peringatan Anomali / Fraud Detection (UC-036)
### 11.6. Alur: Menginput Data Awal Setup Wizard (UC-037)

---

## 12. Alur Interaksi Modul M.8 — CRM Pelanggan
### 12.1. Alur: Mengelola Database CRM & Riwayat Pelanggan (UC-038)

---

## 13. Alur Interaksi Modul M.9 — Multi-Cabang
### 13.1. Alur: Menerapkan Identifikasi Multi-Cabang (UC-039)

---

## 14. Alur Interaksi Modul M.10 — Konfigurasi Runtime
### 14.1. Alur: Mengonfigurasi Parameter Bisnis Runtime (UC-040)

---

## 15. Wireframe Terminal Teks (Mockup Representasi Layar CLI)
### 15.1. Wireframe: Layar Login
### 15.2. Wireframe: Dashboard Utama (per Role)
### 15.3. Wireframe: Form Input Transaksi Kasir
### 15.4. Wireframe: Tabel Daftar Barang / Stok Gudang
### 15.5. Wireframe: Struk Nota Thermal Preview (58mm / 80mm)
### 15.6. Wireframe: Layar Rekonsiliasi Kas Shift Handover
### 15.7. Wireframe: Layar Laporan Laba/Rugi
### 15.8. Wireframe: Layar Audit Trail Log Viewer

---

## 16. Matriks Ketertelusuran (Traceability Matrix)
### 16.1. Mapping Alur Interaksi CLI ke Use Case Diagram (UCD v1.1)
### 16.2. Mapping Alur Interaksi CLI ke SRS v1.1
### 16.3. Mapping Alur Interaksi CLI ke Workflow Diagram v1.1

---

## 17. Persetujuan dan Otorisasi
(Tabel stakeholder, nama, tanda tangan, tanggal)

---

## 18. Glosarium
(Daftar istilah teknis spesifik dokumen ini)

---

## 19. Referensi Dokumen
(Tabel daftar file referensi yang digunakan dalam penyusunan dokumen ini)
```

---

## 4. Instruksi Detail Tahapan Pengerjaan (Checklist Implementasi)

### FASE 1: Persiapan dan Pembacaan Referensi

- [ ] **1.1.** Adopsi persona **Senior UX/CLI Interaction Designer & Terminal Interface Architect**. Seluruh keputusan desain, gaya penulisan, dan sudut pandang dokumen WAJIB menggunakan perspektif persona ini.
- [ ] **1.2.** Baca file referensi No. 1: `docs/sdlc/02_analysis/03_use_case_diagram.md` — **BACA SELURUHNYA DARI AWAL SAMPAI AKHIR TANPA TERPOTONG**. Catat dan rangkum:
  - [ ] 1.2.1. Daftar lengkap 44 Use Case (UC-001 s.d UC-044) beserta nama, modul, aktor primer, dan aktor sekunder.
  - [ ] 1.2.2. Setiap spesifikasi naratif use case: Main Flow, Alternative Flow, Exception Flow, Precondition, Postcondition, dan Trigger.
  - [ ] 1.2.3. Relasi `<<include>>` dan `<<extend>>` antar use case.
  - [ ] 1.2.4. Diagram UCD per modul (11 diagram Mermaid).
- [ ] **1.3.** Baca file referensi No. 2: `docs/sdlc/02_analysis/02_software_requirements.md` — **BACA SELURUHNYA DARI AWAL SAMPAI AKHIR TANPA TERPOTONG**. Catat dan rangkum:
  - [ ] 1.3.1. Deskripsi teknis setiap SRS-F-001 s.d SRS-F-040, terutama bagian **Input yang Diperlukan**, **Proses/Logika Bisnis**, **Output yang Dihasilkan**, dan **Aturan Validasi**.
  - [ ] 1.3.2. Daftar 8 aktor sistem lengkap dengan hak akses utama masing-masing (Bab 2.3).
  - [ ] 1.3.3. Contoh wireframe terminal CLI (jika ada di dalam SRS).
  - [ ] 1.3.4. Daftar lengkap kode error standar: `ERR-DB-xxx`, `ERR-VAL-xxx`, `ERR-AUTH-xxx`, `ERR-STOCK-xxx`, `ERR-SYS-xxx`.
  - [ ] 1.3.5. Batasan desain FP murni, presisi `decimal`, dan CLI-only interface (Bab 2.5).
  - [ ] 1.3.6. Spesifikasi dependency libraries: `rich`, `tabulate`, `getpass`, dan versinya.
- [ ] **1.4.** Baca file referensi No. 3: `docs/sdlc/02_analysis/06_access_control_matrix.md` — **BACA SELURUHNYA DARI AWAL SAMPAI AKHIR TANPA TERPOTONG**. Catat dan rangkum:
  - [ ] 1.4.1. Seluruh matriks akses per modul (Bab 4.2 s.d 4.12): menu mana yang `✅ FULL`, `📖 READ`, `📝 INPUT`, `🔒 RTL`, `⛔ DENY`, atau `🔐 ESC` untuk setiap peran.
  - [ ] 1.4.2. Aturan otorisasi eskalasi supervisor (Bab 6.1, 6.2): operasi mana yang memerlukan sandi pemilik atau kepala percetakan.
  - [ ] 1.4.3. Aturan session JWT, rate limiting, dan pencatatan audit trail pelanggaran akses (Bab 6.4, 6.5, 6.6).
  - [ ] 1.4.4. Daftar 44 menu CLI per modul beserta ID menu-nya (`MENU-M1-001` s.d `MENU-BASE-004`).
- [ ] **1.5.** Baca file referensi No. 4: `docs/sdlc/03_design/03_system_architecture.md` — **BACA SELURUHNYA DARI AWAL SAMPAI AKHIR TANPA TERPOTONG**. Catat dan rangkum:
  - [ ] 1.5.1. Deskripsi **Presentation Layer (CLI Interface)** — Bab 4.3.1: tanggung jawab, pustaka utama (`rich`, `tabulate`, `getpass`), dan batasan FP.
  - [ ] 1.5.2. Pola desain FP: State Dictionary Passing untuk session JWT, nested closures, error handling Either/Result pattern (Bab 4.4).
  - [ ] 1.5.3. Sequence diagram alur kritis: Login JWT (Bab 8.3.1), Transaksi Kasir (Bab 8.3.2), Produksi BOM (Bab 8.3.3), Shift Handover (Bab 8.3.4).
  - [ ] 1.5.4. Pola penanganan error & format kode `ERR-[KATEGORI]-[NOMOR]` (Bab 8.3.5).
  - [ ] 1.5.5. ADR-003: Keputusan CLI vs GUI/Web dan konsekuensinya (Bab 10.3).
  - [ ] 1.5.6. Atribut non-fungsional UX CLI: keyboard friendly, consistent navigation tombol `0`, response time < 1 detik (Bab 11.7).
- [ ] **1.6.** Baca file referensi No. 5: `docs/sdlc/02_analysis/04_workflow_diagram.md` — **BACA SELURUHNYA DARI AWAL SAMPAI AKHIR TANPA TERPOTONG**. Catat dan rangkum:
  - [ ] 1.6.1. Alur kerja makro harian toko (WF-OVERVIEW-01, WF-OP-01): dari buka shift hingga tutup shift.
  - [ ] 1.6.2. Seluruh 38 alur To-Be per modul (WF-M1-01 s.d WF-M10-01): decision points, subprocess calls, narasi prosedural.
  - [ ] 1.6.3. 3 alur lintas modul (Cross-Module) untuk Cetak Kustom, Pengadaan Barang, dan Penutupan Hari.
  - [ ] 1.6.4. Tabel decision points dan exception handling.
- [ ] **1.7.** Baca file referensi No. 6: `docs/sdlc/03_design/01_database_schema.sql` — **BACA SELURUHNYA**. Catat dan rangkum:
  - [ ] 1.7.1. Nama kolom, tipe data, dan constraint `NOT NULL`/`DEFAULT` dari tabel-tabel yang terkait input CLI (terutama: `transaksi`, `detail_transaksi`, `barang`, `pelanggan`, `pengguna`, `antrian_kerja`, `absensi`, `kasbon`, `pengeluaran`, `shift_handover`).
  - [ ] 1.7.2. Field mana saja yang di-generate otomatis oleh sistem (AUTO_INCREMENT, DEFAULT CURRENT_TIMESTAMP) sehingga TIDAK perlu diminta dari input CLI.
- [ ] **1.8.** Baca file referensi No. 7: `docs/sdlc/03_design/02_erd_database.md` — Baca secukupnya untuk memahami relasi antar tabel. Catat relasi kunci yang mempengaruhi alur navigasi menu.
- [ ] **1.9.** Baca file referensi No. 8: `docs/sdlc/02_analysis/05_data_dictionary.md` — Baca secukupnya untuk memahami label dan deskripsi setiap field data. Gunakan untuk menentukan label prompt input CLI.
- [ ] **1.10.** Baca file referensi No. 9: `docs/sdlc/02_analysis/01_business_requirements.md` — Baca secukupnya untuk konteks bisnis. Pastikan alur interaksi CLI mencerminkan harapan operasional nyata pemilik.

### FASE 2: Penyusunan Bab Informasi Dokumen (Bab 1)

- [ ] **2.1.** Tulis metadata frontmatter (dokumen, proyek, versi 1.0, tanggal, status Draft, penyusun persona).
- [ ] **2.2.** Tulis tabel Riwayat Perubahan Dokumen (1 baris untuk versi 1.0).
- [ ] **2.3.** Tulis Bab 1.1 Tujuan Dokumen — Jelaskan bahwa dokumen ini memetakan seluruh alur interaksi pengguna dengan antarmuka CLI AbuCom secara step-by-step, dari prompt pertama hingga feedback terakhir, untuk setiap use case.
- [ ] **2.4.** Tulis Bab 1.2 Cakupan Dokumen — Sebutkan cakupan: prinsip desain CLI, hierarki menu global, 44 alur interaksi detail, wireframe mockup terminal, dan matriks traceability.
- [ ] **2.5.** Tulis Bab 1.3 Posisi Dokumen dalam SDLC — Posisikan sebagai **deliverable keempat pada Fase 03 Design**, setelah Database Schema, ERD, dan System Architecture. Sertakan diagram ASCII posisi dokumen.
- [ ] **2.6.** Tulis Bab 1.4 Hubungan dengan Dokumen SDLC Lainnya — Jelaskan dokumen input (UCD, SRS, ACM, SA, WFD) dan output (SDD Fase 04, Test Cases Fase 05).
- [ ] **2.7.** Tulis Bab 1.5 Audiens Target — Junior Programmer, Tim AI, dan Calon Staf Toko.
- [ ] **2.8.** Tulis Bab 1.6 Definisi, Akronim, dan Singkatan — Sertakan istilah spesifik CLI interaction (hotkey, prompt, wireframe, breadcrumb, screen flow, dsb).

### FASE 3: Penyusunan Prinsip Desain Interaksi CLI (Bab 2)

- [ ] **3.1.** Tulis Bab 2.1 Filosofi UX Terminal — Deskripsikan prinsip: kecepatan (< 1 detik response), keyboard-only, minimalis, konsisten, dan informatif.
- [ ] **3.2.** Tulis Bab 2.2 Konvensi Navigasi Global:
  - [ ] 3.2.1. Tombol `0` = selalu kembali ke menu sebelumnya di setiap level.
  - [ ] 3.2.2. Nomor menu (1, 2, 3...) = pilih opsi secara numerik.
  - [ ] 3.2.3. Pola konfirmasi aksi destruktif: `[Y/N]` sebelum delete/cancel/retur.
  - [ ] 3.2.4. Pola `Enter` tanpa input = ulangi prompt/default value.
  - [ ] 3.2.5. Shortcut `q` atau `Ctrl+C` = keluar darurat (graceful exit).
- [ ] **3.3.** Tulis Bab 2.3 Konvensi Visual & Pustaka Tampilan — Deskripsikan penggunaan `rich` untuk panel, progress bar, tree, dan `tabulate` untuk tabel data. Jelaskan kode warna ANSI: hijau (sukses), merah (error), kuning (warning), biru (info), magenta (header).
- [ ] **3.4.** Tulis Bab 2.4 Konvensi Input & Validasi:
  - [ ] 3.4.1. Sanitasi karakter kontrol ASCII < `\x20` (khususnya `\x1b`).
  - [ ] 3.4.2. Input password menggunakan `getpass.getpass()` (no echo).
  - [ ] 3.4.3. Input numerik desimal divalidasi ke `decimal.Decimal`.
  - [ ] 3.4.4. Input tanggal divalidasi ke format `YYYY-MM-DD`.
  - [ ] 3.4.5. Input ID (integer) divalidasi ke `int()` positif.
- [ ] **3.5.** Tulis Bab 2.5 Konvensi Pesan Error & Feedback — Jelaskan format standar: `"ERR-[KATEGORI]-[NOMOR]: [Pesan deskriptif]"` dengan warna merah. Feedback sukses: warna hijau. Warning: warna kuning.
- [ ] **3.6.** Tulis Bab 2.6 Konvensi Aksesibilitas & Portabilitas — Keyboard-only, UTF-8, `chcp 65001` Windows, `pathlib` cross-OS, `clear_screen()` platform-aware.

### FASE 4: Penyusunan Peta Hierarki Menu CLI Global (Bab 3)

- [ ] **4.1.** Tulis Bab 3.1 Diagram Hierarki Menu Utama — Buat diagram Mermaid `graph TD` yang menggambarkan tree hierarki:
  - [ ] 4.1.1. Root node: `Layar Login`
  - [ ] 4.1.2. Level 1: `Dashboard Utama`
  - [ ] 4.1.3. Level 2: 10 menu modul utama (M.1 s.d M.10) + menu dasar (Ubah Password, Logout)
  - [ ] 4.1.4. Level 3: Sub-menu per modul sesuai daftar menu di ACM v1.1 (MENU-M1-001 s.d MENU-M10-001)
  - [ ] 4.1.5. Level 4: Form input / detail screen jika ada sub-sub-menu
- [ ] **4.2.** Tulis Bab 3.2 Deskripsi Singkat Setiap Node Menu — Tabel berisi: ID Menu, Nama Menu, Deskripsi 1-2 kalimat, Level Hierarki.
- [ ] **4.3.** Tulis Bab 3.3 Matriks Visibilitas Menu per Role — Buat tabel besar yang memetakan setiap menu (44 + 4 dasar = 48 baris) terhadap 8 peran. Kolom isi: `Tampil` / `Sembunyi`. **Data WAJIB diambil 100% dari matriks ACM v1.1 Bab 4**. Menu dengan status `⛔ DENY` = `Sembunyi`. Semua status lain = `Tampil`.

### FASE 5: Penyusunan Alur Interaksi Dasar Sistem (Bab 4)

- [ ] **5.1.** Tulis Bab 4.1 Alur Interaksi Login (UC-041):
  - [ ] 5.1.1. Buat diagram flowchart/sequence Mermaid alur login lengkap.
  - [ ] 5.1.2. Tulis step-by-step interaksi:
    - Langkah 1: Sistem menampilkan banner ASCII AbuCom dan prompt `Username: `.
    - Langkah 2: Pengguna mengetik username.
    - Langkah 3: Sistem menampilkan prompt `Password: ` (input tersembunyi via `getpass`).
    - Langkah 4: Sistem memvalidasi ke database (bcrypt.checkpw).
    - Langkah 5a: Jika valid → generate JWT token, tampilkan pesan sukses hijau, redirect ke Dashboard.
    - Langkah 5b: Jika salah → increment `failed_login_attempts`, tampilkan `ERR-AUTH-001`, jika >= 5 kali → lockout 10 menit `ERR-AUTH-002`.
  - [ ] 5.1.3. Sertakan contoh tampilan terminal (wireframe teks).
- [ ] **5.2.** Tulis Bab 4.2 Alur Interaksi Logout (UC-042) — Step-by-step, hapus JWT, clear screen, redirect login.
- [ ] **5.3.** Tulis Bab 4.3 Alur Interaksi Dashboard Utama (UC-043) — Deskripsikan tampilan dashboard yang BERBEDA per role berdasarkan ACM. Sertakan wireframe dashboard per role (minimal 3 contoh: pemilik, kasir, gudang).
- [ ] **5.4.** Tulis Bab 4.4 Alur Interaksi Ubah Password (UC-044) — Step-by-step: input password lama, input baru 2x, validasi match, bcrypt re-hash, update database.

### FASE 6: Penyusunan Alur Interaksi per Modul (Bab 5 s.d Bab 14)

Untuk **setiap** use case (UC-001 s.d UC-040), tulis alur interaksi dengan format konsisten sebagai berikut:

- [ ] **6.1.** Untuk setiap sub-bab alur interaksi, gunakan format penulisan berikut:

```
### X.Y. Alur: [Nama Use Case] (UC-[NNN])

| Atribut           | Nilai                                   |
| :----------------- | :--------------------------------------- |
| **Derivasi UC**    | UC-[NNN]                                 |
| **Derivasi SRS**   | SRS-F-[NNN]                              |
| **Derivasi WF**    | WF-[Modul]-[NN]                          |
| **Modul**          | M.[N] — [Nama Modul]                    |
| **Aktor Primer**   | [role1], [role2]                         |
| **Menu ID**        | MENU-M[N]-[NNN]                          |
| **Hak Akses**      | (Tabel mini per role: FULL/READ/INPUT/DENY/ESC) |

#### Diagram Alur Interaksi (Mermaid)
(Flowchart atau sequence diagram alur step-by-step)

#### Langkah-Langkah Interaksi Detail
| No. | Aktor/Sistem | Aksi                         | Tipe        | Contoh Tampilan/Input                |
|-----|-------------|-------------------------------|-------------|--------------------------------------|
| 1   | Sistem      | Tampilkan header menu         | Output      | `═══ TRANSAKSI PENJUALAN ═══`       |
| 2   | Pengguna    | Pilih tipe pelanggan          | Input       | `Tipe pelanggan [1-Retail/2-Grosir/3-Mitra]: ` |
| 3   | Sistem      | Validasi input                | Proses      | Jika input bukan 1/2/3 → tampilkan ERR-VAL-xxx |
| ... | ...         | ...                           | ...         | ...                                  |

#### Pesan Error yang Mungkin Muncul
| Kode Error       | Pemicu                          | Pesan yang Ditampilkan                                  |
|------------------|---------------------------------|---------------------------------------------------------|
| ERR-VAL-xxx      | [kondisi]                       | "[pesan error lengkap]"                                 |
| ERR-AUTH-xxx     | [kondisi]                       | "[pesan error lengkap]"                                 |

#### Contoh Wireframe Tampilan Terminal
(Representasi ASCII/ANSI mockup layar terminal untuk screen utama alur ini)
```

- [ ] **6.2.** Tulis alur interaksi lengkap untuk semua 6 UC di **Modul M.1** (Bab 5):
  - [ ] 6.2.1. UC-001: Transaksi Penjualan Multi-Divisi
  - [ ] 6.2.2. UC-002: Skema Harga Otomatis
  - [ ] 6.2.3. UC-003: DP & Pelunasan
  - [ ] 6.2.4. UC-004: Pembatalan & Retur
  - [ ] 6.2.5. UC-005: Margin Keuntungan
  - [ ] 6.2.6. UC-006: Struk Nota Thermal
- [ ] **6.3.** Tulis alur interaksi lengkap untuk semua 10 UC di **Modul M.2** (Bab 6):
  - [ ] 6.3.1. UC-007 s.d UC-016 (HPP BOM, Limbah, UoM, ATK Internal, Stock Opname, Re-Order, Price Tracking, Import CSV, Supplier & Utang, Backup/Restore)
- [ ] **6.4.** Tulis alur interaksi lengkap untuk semua 3 UC di **Modul M.3** (Bab 7):
  - [ ] 6.4.1. UC-017 s.d UC-019 (PPOB, Akun Terhemat, Jasa Service)
- [ ] **6.5.** Tulis alur interaksi lengkap untuk semua 4 UC di **Modul M.4** (Bab 8):
  - [ ] 6.5.1. UC-020 s.d UC-023 (Absensi/Kasbon, Smart Payroll, Poin Insentif, Potongan Kasbon)
- [ ] **6.6.** Tulis alur interaksi lengkap untuk semua 3 UC di **Modul M.5** (Bab 9):
  - [ ] 6.6.1. UC-024 s.d UC-026 (Job Tracking, Arsip Desain, Link WA)
- [ ] **6.7.** Tulis alur interaksi lengkap untuk semua 5 UC di **Modul M.6** (Bab 10):
  - [ ] 6.7.1. UC-027 s.d UC-031 (Pinjaman, Laba/Rugi, Jatuh Tempo, Aset/Depresiasi, Pengeluaran)
- [ ] **6.8.** Tulis alur interaksi lengkap untuk semua 6 UC di **Modul M.7** (Bab 11):
  - [ ] 6.8.1. UC-032 s.d UC-037 (RBAC, Audit Log, Shift Handover, Rekonsiliasi Kas, Fraud Detection, Setup Wizard)
- [ ] **6.9.** Tulis alur interaksi untuk UC di **Modul M.8** (Bab 12):
  - [ ] 6.9.1. UC-038 (CRM Pelanggan)
- [ ] **6.10.** Tulis alur interaksi untuk UC di **Modul M.9** (Bab 13):
  - [ ] 6.10.1. UC-039 (Multi-Cabang)
- [ ] **6.11.** Tulis alur interaksi untuk UC di **Modul M.10** (Bab 14):
  - [ ] 6.11.1. UC-040 (Konfigurasi Runtime)

### FASE 7: Penyusunan Wireframe Terminal Teks (Bab 15)

- [ ] **7.1.** Tulis Bab 15.1 Wireframe Layar Login — Contoh representasi layar menggunakan format code block:
  ```
  ╔══════════════════════════════════╗
  ║       🏪  AbuCom CLI v1.0       ║
  ║  Sistem Manajemen Terpadu Toko  ║
  ╚══════════════════════════════════╝

  Username : _______________
  Password : ***************

  [Tekan ENTER untuk Login]
  ```
- [ ] **7.2.** Tulis wireframe Dashboard Utama per role (minimal 3 variasi: pemilik, kasir, gudang).
- [ ] **7.3.** Tulis wireframe Form Input Transaksi Kasir (keranjang belanja + subtotal).
- [ ] **7.4.** Tulis wireframe Tabel Daftar Barang / Stok Gudang (menggunakan format `tabulate`).
- [ ] **7.5.** Tulis wireframe Struk Nota Thermal Preview (58mm = 32 char dan 80mm = 48 char).
- [ ] **7.6.** Tulis wireframe Layar Rekonsiliasi Kas Shift Handover.
- [ ] **7.7.** Tulis wireframe Layar Laporan Laba/Rugi Instan.
- [ ] **7.8.** Tulis wireframe Layar Audit Trail Log Viewer.

### FASE 8: Penyusunan Matriks Ketertelusuran (Bab 16)

- [ ] **8.1.** Tulis Bab 16.1 Mapping ke UCD v1.1 — Buat tabel: | Bab Alur CLI | UC-ID | Nama UC | Status Mapping |. Pastikan semua 44 UC tercakup.
- [ ] **8.2.** Tulis Bab 16.2 Mapping ke SRS v1.1 — Buat tabel: | Bab Alur CLI | SRS-F-ID | Nama SRS | Status Mapping |. Pastikan SRS-F-001 s.d SRS-F-040 tercakup.
- [ ] **8.3.** Tulis Bab 16.3 Mapping ke WFD v1.1 — Buat tabel: | Bab Alur CLI | WF-ID | Nama Workflow | Status Mapping |. Pastikan seluruh workflow To-Be tercakup.

### FASE 9: Penyusunan Bab Penutup (Bab 17, 18, 19)

- [ ] **9.1.** Tulis Bab 17 Persetujuan dan Otorisasi — Tabel stakeholder (Pemilik Usaha + persona arsitektur).
- [ ] **9.2.** Tulis Bab 18 Glosarium — Daftar minimal 15 istilah teknis spesifik CLI interaction design.
- [ ] **9.3.** Tulis Bab 19 Referensi Dokumen — Tabel berisi semua file referensi yang digunakan (No, Nama Dokumen, Path Relatif, Keterangan Penggunaan). **Data diambil dari tabel di Bab 2 issue ini.**

### FASE 10: Penulisan Hasil ke Target File

- [ ] **10.1.** Tuangkan seluruh hasil pengerjaan ke dalam file target: `docs/sdlc/03_design/04_cli_interaction_flow.md`.
- [ ] **10.2.** Pastikan dokumen ditulis **LENGKAP DARI AWAL SAMPAI AKHIR** tanpa ada bagian yang terpotong, diringkas, atau diwakili placeholder `...` atau `[LANJUTAN]`.
- [ ] **10.3.** Pastikan setiap bab terisi penuh dengan konten substantif. **DILARANG** menulis kalimat seperti "akan diisi nanti", "lihat referensi", atau "TBD".
- [ ] **10.4.** Jika ada data spesifik yang **TIDAK DITEMUKAN** di file referensi, tandai dengan format: `⚠️ **[DATA TIDAK TERSEDIA DI REFERENSI — PERLU DIISI MANUAL]**`.
- [ ] **10.5.** Pastikan format markdown valid: heading hierarchy benar, tabel rapi, code block tertutup, diagram Mermaid valid.

### FASE 11: Verifikasi dan Validasi Akhir

- [ ] **11.1.** Verifikasi bahwa **semua 44 use case** (UC-001 s.d UC-044) telah memiliki alur interaksi detail di dalam dokumen.
- [ ] **11.2.** Verifikasi bahwa **semua 48 menu CLI** (44 modul + 4 dasar) telah tercakup dalam peta hierarki menu.
- [ ] **11.3.** Verifikasi bahwa matriks visibilitas menu per role **100% konsisten** dengan ACM v1.1.
- [ ] **11.4.** Verifikasi bahwa semua kode error yang disebut dalam alur **konsisten** dengan daftar error di SRS v1.1.
- [ ] **11.5.** Verifikasi bahwa semua diagram Mermaid **valid secara sintaks** (tidak ada error node atau edge yang tidak terdefinisi).
- [ ] **11.6.** Verifikasi bahwa tabel traceability di Bab 16 **lengkap tanpa gap** — tidak boleh ada UC, SRS, atau WF yang tidak ter-mapping.
- [ ] **11.7.** Verifikasi bahwa **Bab 19 Referensi Dokumen** terisi lengkap di baris paling bawah dokumen.
- [ ] **11.8.** Verifikasi bahwa bahasa Indonesia yang digunakan **natural, tidak ambigu, dan mudah dipahami** oleh junior programmer atau AI model yang lebih murah.

---

## 5. Instruksi Tambahan Spesifik CLI Interaction Flow

### 5.1. Standar Penulisan Alur Interaksi
- Setiap langkah interaksi WAJIB menyebutkan **siapa yang bertindak** (Pengguna atau Sistem).
- Setiap input dari pengguna WAJIB menyebutkan **format yang diharapkan** (contoh: `integer > 0`, `string max 100 char`, `YYYY-MM-DD`).
- Setiap output dari sistem WAJIB menyebutkan **format tampilan** (contoh: tabel `tabulate`, panel `rich`, teks polos).
- Setiap titik keputusan (*decision point*) WAJIB memiliki minimal 2 cabang (sukses dan gagal).

### 5.2. Standar Penulisan Wireframe
- Wireframe WAJIB menggunakan format code block markdown (```) untuk mempertahankan alignment karakter monospace.
- Gunakan karakter box-drawing Unicode (╔ ╗ ╚ ╝ ║ ═ ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼) untuk border.
- Wireframe WAJIB menunjukkan **posisi prompt input** dan **area output data**.

### 5.3. Standar Diagram Mermaid
- Gunakan `flowchart TD` untuk alur navigasi dan decision.
- Gunakan `sequenceDiagram` untuk interaksi multi-aktor (misal: kasir → sistem → database → kasir).
- Sertakan styling warna node sesuai konvensi Workflow Diagram v1.1 (hijau = start/end, biru = kasir, ungu = produksi, oranye = gudang, abu = sistem, merah = exception).

### 5.4. Konsistensi dengan State Dictionary Passing (FP)
- Dalam setiap alur yang melibatkan navigasi menu berlapis, **jelaskan secara eksplisit** bahwa state session (user_id, role, cabang_id, token JWT) diteruskan sebagai parameter fungsi menu, bukan disimpan sebagai variabel global.

### 5.5. Pola Navigasi Breadcrumb
- Setiap layar sub-menu WAJIB menampilkan **breadcrumb path** yang menunjukkan posisi pengguna saat ini dalam hierarki menu. Contoh: `Dashboard > M.1 Transaksi > Input Transaksi Baru`.

---

## 6. Catatan Penting untuk Pelaksana

> ⚠️ **PERINGATAN KRITIS**:
> 1. **JANGAN PERNAH** memotong, menyingkat, atau meringkas isi dokumen. Setiap bab dan sub-bab WAJIB terisi penuh dengan konten substantif.
> 2. **JANGAN PERNAH** menuliskan placeholder seperti `[TODO]`, `[TBD]`, `[Lanjutan]`, `[dst]`, `[sama seperti di atas]`, atau `...` sebagai pengganti konten.
> 3. **JANGAN PERNAH** membuat data atau informasi yang tidak ada di file referensi (halusinasi). Jika data tidak ditemukan, gunakan penanda `⚠️ [DATA TIDAK TERSEDIA]`.
> 4. **WAJIB** membaca setiap file referensi secara **PENUH dari baris pertama sampai baris terakhir** sebelum mulai menulis.
> 5. **WAJIB** menggunakan bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami.
> 6. **WAJIB** memastikan dokumen ini cukup lengkap dan detail sehingga bisa menjadi referensi utama bagi fase SDLC selanjutnya (SDD, Implementation, dan Testing) tanpa perlu kembali bertanya ke fase sebelumnya.

---

## 7. Referensi File yang Digunakan dalam Penyusunan Issue Ini

| No | Nama Dokumen                             | Path Relatif                                           | Keterangan Penggunaan                                                        |
| :-: | :--------------------------------------- | :----------------------------------------------------- | :--------------------------------------------------------------------------- |
| 1  | Use Case Diagram v1.1                    | `docs/sdlc/02_analysis/03_use_case_diagram.md`         | Basis 44 use case, spesifikasi naratif, dan diagram aktor-fungsionalitas.    |
| 2  | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md`    | Spesifikasi teknis input/output/validasi, kode error, dan wireframe contoh.  |
| 3  | Access Control Matrix v1.1               | `docs/sdlc/02_analysis/06_access_control_matrix.md`    | Matriks hak akses 8 peran terhadap 44 menu CLI dan 28 tabel database.        |
| 4  | System Architecture v1.1                 | `docs/sdlc/03_design/03_system_architecture.md`        | Arsitektur 4-layer, sequence diagram, ADR-003 CLI, dan atribut UX.           |
| 5  | Workflow Diagram v1.1                    | `docs/sdlc/02_analysis/04_workflow_diagram.md`         | 38 alur To-Be per modul, decision points, dan narasi prosedural.             |
| 6  | Database Schema DDL SQL v1.1             | `docs/sdlc/03_design/01_database_schema.sql`           | Skema fisik 28 tabel untuk mengetahui field input yang diperlukan di CLI.     |
| 7  | ERD Database v1.1                        | `docs/sdlc/03_design/02_erd_database.md`               | Relasi antar tabel untuk dependensi navigasi menu.                           |
| 8  | Data Dictionary v1.1                     | `docs/sdlc/02_analysis/05_data_dictionary.md`          | Kamus data kolom untuk label prompt input CLI.                               |
| 9  | Business Requirements Document v1.1      | `docs/sdlc/02_analysis/01_business_requirements.md`    | Konteks kebutuhan bisnis pemilik dan harapan operasional.                     |
