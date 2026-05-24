---
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
target     : docs/sdlc/02_analysis/06_access_control_matrix.md
prioritas  : High
status     : Open
tanggal    : 2026-05-24
assignee   : Junior Programmer / LLM AI Model (Gemini 3.1 Pro Low / GPT-OSS 120B Medium)
---

# Pembuatan Dokumen Access Control Matrix (ACM)

## 1. Ringkasan Issue

Issue ini berisi perencanaan dan instruksi low-level (langkah demi langkah) untuk membuat dan menyusun dokumen **Access Control Matrix (ACM)** — sebuah dokumen matriks kontrol akses yang memetakan secara eksplisit dan granular hubungan antara setiap **peran pengguna (role)** sistem dengan setiap **objek/sumber daya (resource)** yang dilindungi di dalam sistem AbuCom CLI.

Dokumen ini berbeda dari tabel RBAC ringkas di BRD (Bagian 5.3) karena ACM bersifat **lebih granular, lebih detail, dan lebih operasional**. ACM akan merinci hak akses hingga ke level **aksi spesifik per fungsi/menu CLI** (Create, Read, Update, Delete — CRUD), bukan hanya per modul/kategori umum seperti di BRD.

---

## 2. Persona Penyusun

**Persona yang ditugaskan**: **Senior Security Analyst & RBAC Specialist**

Alasan pemilihan persona:
- Dokumen Access Control Matrix adalah artefak keamanan (*security artifact*) yang memerlukan keahlian khusus dalam perancangan sistem otorisasi berbasis peran (RBAC).
- Persona ini memiliki otoritas dan pemahaman mendalam terhadap prinsip *Least Privilege*, *Separation of Duties*, dan *Defense in Depth* yang wajib diterapkan dalam matriks akses.
- Persona ini mampu memastikan dokumen ACM selaras dengan standar kepatuhan regulasi perlindungan data (UU PDP No. 27/2022) yang diwajibkan oleh proyek AbuCom.

---

## 3. File Referensi yang Digunakan

Berikut adalah daftar file referensi yang **wajib dibaca dan dirangkum** sebelum memulai penyusunan dokumen ACM. File dipilih berdasarkan tingkat relevansi spesifik terhadap kebutuhan data kontrol akses:

| # | Prioritas | Nama File Referensi | Lokasi Path Relatif | Alasan Relevansi |
|---|---|---|---|---|
| 1 | **PRIMER** | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | Sumber utama definisi 8 peran aktor internal (Bab 5.1), tabel hak akses RBAC per modul (Bab 5.3 - Tabel Matriks), dan seluruh 43 kebutuhan bisnis fungsional yang memuat aktor terkait. |
| 2 | **PRIMER** | `02_software_requirements.md` | `docs/sdlc/02_analysis/02_software_requirements.md` | Sumber utama spesifikasi teknis 40+ kebutuhan fungsional SRS yang merinci aktor, input, proses, aturan validasi, dan exception handling per fungsi sistem. Memuat SRS-F-030 (RBAC), SRS-F-031 (Audit Trail), dan kode error otorisasi. |
| 3 | **PRIMER** | `03_use_case_diagram.md` | `docs/sdlc/02_analysis/03_use_case_diagram.md` | Sumber pemetaan 44 use case (UC-001 s.d UC-044) dengan aktor primer/sekunder, alur utama, alur alternatif, dan alur pengecualian (termasuk kode error otorisasi ERR-AUTH). |
| 4 | **SEKUNDER** | `04_workflow_diagram.md` | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Sumber visualisasi alur kerja antar peran yang menunjukkan titik-titik interaksi otorisasi dan validasi antar staf dalam proses bisnis operasional. |
| 5 | **SEKUNDER** | `05_data_dictionary.md` | `docs/sdlc/02_analysis/05_data_dictionary.md` | Sumber definisi tabel `pengguna` (kolom `role`), domain nilai peran pengguna, dan tabel `audit_logs` yang merekam aktivitas modifikasi data sensitif berdasarkan peran. |
| 6 | **TERSIER** | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Sumber profil 19 pemangku kepentingan dan tingkat pengaruh/kepentingan setiap stakeholder terhadap sistem. |
| 7 | **TERSIER** | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Sumber informasi inovasi keamanan terintegrasi (RBAC, Audit Trail, Rate Limiting, Fraud Detection) yang mempengaruhi pola otorisasi. |

> **Catatan**: File `narasi.txt` (`docs/sdlc/narasi.txt`) **tidak lagi diperlukan** sebagai referensi langsung untuk dokumen ini karena seluruh informasi relevan dari narasi asli pemilik usaha telah diabstraksi, divalidasi, dan didokumentasikan secara formal di dalam dokumen BRD v1.1 dan SRS v1.1 yang jauh lebih terstruktur dan akurat.

---

## 4. Instruksi Pelaksanaan (Low-Level Step-by-Step)

### Fase 1: Pembacaan dan Pengumpulan Data Referensi

Baca setiap file referensi secara menyeluruh. Rangkum semua data dan informasi yang ada di dalam file referensi — setiap detail jangan sampai ada yang terlewat. Namun, **hanya ambil dan rangkum data yang sesuai dan dibutuhkan spesifik oleh dokumen Access Control Matrix**, agar dokumen bersih dan hanya fokus pada data dan informasi yang memang seharusnya ada.

#### Checklist Pembacaan File Referensi:

- [ ] **Baca file `01_business_requirements.md`** (docs/sdlc/02_analysis/01_business_requirements.md)
  - [ ] Rangkum **Bab 5.1 (Aktor Internal Pengguna Sistem)**: Catat seluruh 8 peran aktor internal beserta deskripsi peran, role sistem, dan tanggung jawab utama masing-masing.
  - [ ] Rangkum **Bab 5.3 (Tabel Hak Akses RBAC)**: Salin seluruh isi tabel matriks hak akses per peran (pemilik, kepala_percetakan, pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang) terhadap 8 kategori modul (Transaksi & Kasir, Antrian & Desain, Gudang & Opname, Absensi Staf, Keuangan & Laba/Rugi, Pinjaman & Aset, Payroll Gaji, Audit Trail). Catat level akses: Akses Penuh, Lihat-Saja, Hanya Input, Hanya Ritel, Ditolak.
  - [ ] Rangkum **Bab 5.4 dan 5.5 (Aktor Eksternal)**: Catat 4 aktor eksternal dan hubungan mereka dengan sistem.
  - [ ] Rangkum **Bab 7 (Kebutuhan Bisnis Fungsional)**: Untuk setiap kebutuhan fungsional (BR-F-01 s.d BR-F-40), catat **Aktor Terkait** yang disebutkan secara eksplisit.
  - [ ] Rangkum **Bab 9 (Aturan Bisnis)**: Catat aturan bisnis terkait keamanan akun CLI (poin 8), termasuk rate limiting 5 kali, penguncian 10 menit, dan session JWT 8 jam.

- [ ] **Baca file `02_software_requirements.md`** (docs/sdlc/02_analysis/02_software_requirements.md)
  - [ ] Rangkum **Bab 2.3 (Karakteristik dan Klasifikasi Pengguna)**: Catat deskripsi teknis hak akses setiap aktor hingga level menu CLI spesifik yang diizinkan/dilarang.
  - [ ] Rangkum **SRS-F-030 (RBAC Multi-Level CLI)**: Catat deskripsi teknis, aturan validasi, penanganan pengecualian, dan kode error otorisasi.
  - [ ] Rangkum **SRS-F-031 (Audit Trail JSON)**: Catat detail field log audit (ID User, Timestamp, Action Type, Target Table, old_value, new_value).
  - [ ] Rangkum **SRS-F-032 (Shift Handover Log)**: Catat aturan validasi serah terima shift kasir.
  - [ ] Rangkum **SRS-F-033 (Rekonsiliasi Kas)**: Catat aturan validasi batas toleransi selisih kas Rp 10.000.
  - [ ] Rangkum **SRS-F-034 (Fraud Detection)**: Catat indikator anomali dan mekanisme notifikasi pemilik.
  - [ ] Rangkum **seluruh SRS-F-001 s.d SRS-F-040**: Untuk setiap spesifikasi, catat kolom **Aktor** yang secara eksplisit disebutkan, serta catat apakah fungsi tersebut memerlukan **otorisasi supervisor/pemilik** dalam aturan validasinya.

- [ ] **Baca file `03_use_case_diagram.md`** (docs/sdlc/02_analysis/03_use_case_diagram.md)
  - [ ] Rangkum **Bab 2.1 (Aktor Internal)**: Catat tabel 8 aktor internal dengan kolom Hak Akses Utama per aktor.
  - [ ] Rangkum **Bab 3.2 (Master Daftar Use Case)**: Salin seluruh 44 baris tabel use case, perhatikan kolom **Aktor Primer** dan **Aktor Sekunder** untuk setiap UC.
  - [ ] Rangkum **Diagram Use Case per Modul (Bab 4.2)**: Catat relasi `<<include>>` dan `<<extend>>` antar use case, terutama yang melibatkan UC-032 (RBAC) dan UC-033 (Audit Trail).
  - [ ] Rangkum **Spesifikasi Naratif Use Case (Bab 5)**: Untuk setiap UC, catat **Prakondisi**, **Alur Pengecualian (Exception Flow)** terkait otorisasi (kode error ERR-AUTH), dan **Aturan Bisnis Terkait** yang menyinggung pembatasan RBAC.

- [ ] **Baca file `04_workflow_diagram.md`** (docs/sdlc/02_analysis/04_workflow_diagram.md)
  - [ ] Rangkum setiap workflow diagram yang menunjukkan interaksi antar peran (role), khususnya titik-titik di mana terjadi validasi otorisasi, eskalasi ke supervisor/pemilik, dan pembatasan akses antar swimlane.
  - [ ] Catat setiap decision point di workflow yang memerlukan verifikasi peran pengguna (misal: persetujuan retur oleh pemilik, otorisasi Stock Opname oleh Kepala Percetakan).

- [ ] **Baca file `05_data_dictionary.md`** (docs/sdlc/02_analysis/05_data_dictionary.md)
  - [ ] Rangkum **Tabel `pengguna`** (Bab 3.2): Catat definisi kolom `role` beserta Domain Nilai Peran Pengguna yang valid.
  - [ ] Rangkum **Tabel `audit_logs`** (Bab 3.14): Catat struktur kolom log audit (pengguna_id, action_type, target_table, old_value, new_value).
  - [ ] Rangkum **Tabel `shift_handover`** (Bab 3.19): Catat kolom FK untuk kasir penyerah, kasir penerima, dan supervisor penyetuju.
  - [ ] Rangkum **Domain Nilai terkait keamanan**: Cari dan catat domain nilai untuk `role`, `action_type`, dan status terkait otorisasi.
  - [ ] Rangkum seluruh **28 tabel database**: Identifikasi setiap tabel dan catat operasi CRUD apa saja yang bisa dilakukan terhadap tabel tersebut beserta peran yang berhak melakukannya.

- [ ] **Baca file `03_stakeholder_register.md`** (docs/sdlc/01_planning/03_stakeholder_register.md)
  - [ ] Rangkum profil stakeholder internal yang menjadi pengguna sistem, khususnya tingkat Power/Interest Grid dan ekspektasi keamanan data dari masing-masing stakeholder.

- [ ] **Baca file `05_innovation_proposal.md`** (docs/sdlc/01_planning/05_innovation_proposal.md)
  - [ ] Rangkum inovasi yang terkait dengan keamanan dan kontrol akses, khususnya: INV-INT-15 (RBAC), INV-INT-16 (Audit Trail), INV-INT-17 (bcrypt), INV-INT-18 (JWT), INV-INT-19 (SQL Injection), INV-INT-20 (Rate Limiting), INV-INT-21 (Enkripsi Backup), INV-NEW-04 (Shift Handover), INV-NEW-06 (Fraud Detection).

---

### Fase 2: Penyusunan Kerangka Dokumen

Setelah seluruh data terkumpul, susun dokumen Access Control Matrix dengan kerangka standar dokumen praktik industri berikut. Kerangka ini dirancang agar **lengkap, informatif, dan layak dijadikan referensi utama bagi dokumen fase SDLC selanjutnya** (Fase 03 Design — System Design Document dan Database Schema).

- [ ] **Buat file baru** di lokasi target: `docs/sdlc/02_analysis/06_access_control_matrix.md`

- [ ] **Tulis metadata dokumen** (front matter YAML) dengan format:
  ```yaml
  ---
  dokumen    : Access Control Matrix (ACM)
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [tanggal pengerjaan, format: YYYY-MM-DD]
  status     : Draft
  penyusun   : Senior Security Analyst & RBAC Specialist
  ---
  ```

- [ ] **Tulis kerangka bab dokumen** sesuai struktur berikut:

#### Kerangka Struktur Dokumen ACM:

```
# Access Control Matrix (ACM) — AbuCom

## Riwayat Perubahan Dokumen
(Tabel riwayat versi: Versi, Tanggal, Perubahan, Oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target
### 1.6. Konvensi Notasi Hak Akses

---

## 2. Definisi Subjek Akses (Aktor/Peran)
### 2.1. Daftar Peran Internal Sistem
### 2.2. Hierarki dan Generalisasi Peran
### 2.3. Peran Eksternal (Non-Sistem)

---

## 3. Definisi Objek Akses (Sumber Daya yang Dilindungi)
### 3.1. Daftar Menu CLI per Modul
### 3.2. Daftar Tabel Database yang Dilindungi
### 3.3. Daftar Fungsi/Operasi Bisnis Kritis

---

## 4. Matriks Kontrol Akses Utama
### 4.1. Konvensi Simbol Akses (Legenda)
### 4.2. Matriks Akses: Modul M.1 — Transaksi & Kebijakan Harga
### 4.3. Matriks Akses: Modul M.2 — Inventaris, BOM & Stock Opname
### 4.4. Matriks Akses: Modul M.3 — Layanan Keuangan, PPOB & Jasa Service
### 4.5. Matriks Akses: Modul M.4 — SDM, Penggajian & Poin Karyawan
### 4.6. Matriks Akses: Modul M.5 — Antrian & Pelacakan Desain
### 4.7. Matriks Akses: Modul M.6 — Pinjaman, Aset & Pengeluaran
### 4.8. Matriks Akses: Modul M.7 — Keamanan, Audit Trail & Hak Akses
### 4.9. Matriks Akses: Modul M.8 — CRM Pelanggan
### 4.10. Matriks Akses: Modul M.9 — Skalabilitas Multi-Cabang
### 4.11. Matriks Akses: Modul M.10 — Konfigurasi Sistem Runtime
### 4.12. Matriks Akses: Use Case Dasar Operasional (UC-041 s.d UC-044)

---

## 5. Matriks Akses Level Database (Tabel CRUD)
### 5.1. Konvensi Operasi CRUD
### 5.2. Matriks CRUD per Tabel Database

---

## 6. Aturan Otorisasi Khusus dan Eskalasi
### 6.1. Aturan Otorisasi Supervisor (Eskalasi Pemilik)
### 6.2. Aturan Otorisasi Kepala Percetakan
### 6.3. Aturan Pembatasan Akses Data Sensitif
### 6.4. Aturan Session dan Timeout Akses (JWT)
### 6.5. Aturan Rate Limiting dan Penguncian Akun
### 6.6. Aturan Pencatatan Audit Trail pada Pelanggaran Akses

---

## 7. Pemetaan Akses terhadap Alur Kerja (Workflow Mapping)
### 7.1. Alur Otorisasi pada Transaksi Kasir
### 7.2. Alur Otorisasi pada Proses Produksi Cetak
### 7.3. Alur Otorisasi pada Stock Opname
### 7.4. Alur Otorisasi pada Retur/Pembatalan
### 7.5. Alur Otorisasi pada Penggajian (Smart Payroll)

---

## 8. Matriks Ketertelusuran Kebutuhan (Traceability Matrix)
### 8.1. Pemetaan ACM terhadap BRD
### 8.2. Pemetaan ACM terhadap SRS
### 8.3. Pemetaan ACM terhadap Use Case Diagram

---

## 9. Ringkasan Statistik Hak Akses
(Tabel ringkasan: jumlah fungsi per peran, persentase akses, dsb.)

---

## 10. Glosarium Istilah Keamanan & Kontrol Akses

---

## 11. Referensi Dokumen
(Tabel daftar file referensi yang digunakan)
```

---

### Fase 3: Pengisian Konten Detail per Bab

Instruksi pengisian konten untuk setiap bab:

#### Bab 1: Informasi Dokumen

- [ ] **Tulis Bab 1.1 (Tujuan Dokumen)**: Jelaskan bahwa ACM ini disusun untuk mendefinisikan secara eksplisit, granular, dan tidak ambigu seluruh hak akses yang dimiliki oleh setiap peran pengguna terhadap setiap fungsi, menu, dan tabel database dalam sistem AbuCom CLI. Sebutkan bahwa dokumen ini menjadi referensi utama bagi implementasi logika RBAC di kode Python dan menjadi dasar pengujian keamanan (penetration testing otorisasi).

- [ ] **Tulis Bab 1.2 (Cakupan Dokumen)**: Sebutkan secara kuantitatif cakupan dokumen: jumlah peran, jumlah fungsi/menu yang dimatriks, jumlah tabel database yang dipetakan CRUD, dan jumlah aturan otorisasi khusus.

- [ ] **Tulis Bab 1.3 (Posisi Dokumen dalam Siklus SDLC)**: Jelaskan bahwa ACM ini merupakan dokumen keenam (dan penutup/terakhir) pada Fase 02 Analysis setelah BRD, SRS, Use Case Diagram, Workflow Diagram, dan Data Dictionary. Buat diagram teks sederhana menunjukkan posisi ACM dalam alur SDLC.

- [ ] **Tulis Bab 1.4 (Hubungan dengan Dokumen SDLC Lainnya)**: Jelaskan input (BRD, SRS, UCD, WFD, Data Dictionary) dan output (System Design Document — Fase 03 Design, Test Plan & Test Cases — Fase 05 Testing). ACM menjadi acuan utama untuk implementasi decorator/guard RBAC di kode Python dan skenario pengujian otorisasi.

- [ ] **Tulis Bab 1.5 (Audiens Target)**: Tentukan audiens: (1) Tim Pengembang AI sebagai implementor logika RBAC, (2) Junior Programmer/Pemilik Usaha sebagai validator kebijakan akses, (3) Calon Kepala Percetakan sebagai supervisor yang harus memahami batas otoritasnya.

- [ ] **Tulis Bab 1.6 (Konvensi Notasi Hak Akses)**: Definisikan simbol/legenda yang digunakan dalam matriks. Gunakan simbol berikut secara konsisten:
  - `✅ FULL` = Akses Penuh (Create, Read, Update, Delete)
  - `📖 READ` = Hanya Baca (Read Only)
  - `📝 INPUT` = Hanya Input/Buat Baru (Create Only)
  - `📝+📖 INPUT+READ` = Input dan Baca (Create + Read)
  - `🔒 RITEL` = Hanya Akses Ritel Terbatas (fungsi khusus sub-set)
  - `⛔ DENY` = Akses Ditolak Sepenuhnya
  - `🔐 ESCALATE` = Memerlukan Otorisasi Supervisor/Pemilik (Eskalasi)

#### Bab 2: Definisi Subjek Akses

- [ ] **Tulis Bab 2.1 (Daftar Peran Internal Sistem)**: Buat tabel berisi 8 peran internal sistem yang diambil dari BRD Bab 5.1 dan SRS Bab 2.3. Kolom tabel: ID Aktor, Nama Peran, Kode Role Sistem, Deskripsi Singkat Peran, Level Hierarki (Pemilik/Supervisor/Staf Operasional).

- [ ] **Tulis Bab 2.2 (Hierarki dan Generalisasi Peran)**: Buat diagram hierarki peran menggunakan Mermaid yang menunjukkan 3 level: (1) Pemilik → akses absolut, (2) Supervisor/Kepala Percetakan → akses operasional terbatas, (3) Staf Operasional (pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang) → akses sangat terbatas. Jelaskan prinsip *Least Privilege* dan *Separation of Duties* yang diterapkan.

- [ ] **Tulis Bab 2.3 (Peran Eksternal)**: Buat tabel berisi 4 aktor eksternal (Pelanggan, Supplier, Institusi Bank, Kerabat/Keluarga). Jelaskan bahwa aktor eksternal **tidak memiliki akses login ke sistem CLI** namun datanya dikelola oleh peran internal tertentu.

#### Bab 3: Definisi Objek Akses

- [ ] **Tulis Bab 3.1 (Daftar Menu CLI per Modul)**: Susun daftar lengkap menu/fungsi CLI yang tersedia di setiap modul (M.1 s.d M.10 + fungsi dasar). Setiap menu harus memiliki ID unik (misal: `MENU-M1-001`), nama menu, deskripsi singkat, dan derivasi UC/SRS terkait. Ambil data dari daftar Use Case UC-001 s.d UC-044.

- [ ] **Tulis Bab 3.2 (Daftar Tabel Database yang Dilindungi)**: Salin daftar 28 tabel dari Data Dictionary Bab 2.1. Kelompokkan per tingkat sensitivitas data: (1) Sangat Sensitif (pinjaman_bank, pinjaman_kerabat, payroll, system_configs), (2) Sensitif (transaksi, pengeluaran, audit_logs, shift_handover), (3) Operasional (barang, pelanggan, antrian_kerja, absensi, dll.).

- [ ] **Tulis Bab 3.3 (Daftar Fungsi/Operasi Bisnis Kritis)**: Identifikasi dan daftarkan operasi bisnis kritis yang memerlukan otorisasi eskalasi atau pembatasan khusus, seperti: hapus transaksi, retur/batal, stock opname approval, proses payroll, konfigurasi parameter runtime, backup/restore database.

#### Bab 4: Matriks Kontrol Akses Utama

Ini adalah inti utama dari dokumen. Untuk setiap modul (M.1 s.d M.10), buat tabel matriks yang granular.

- [ ] **Tulis Bab 4.1 (Konvensi Simbol Akses)**: Salin legenda simbol dari Bab 1.6 dan tambahkan penjelasan detail kapan setiap simbol berlaku.

- [ ] **Tulis Bab 4.2 (Matriks Akses: Modul M.1)**: Buat tabel matriks dengan:
  - Baris: Setiap fungsi/menu di modul M.1 (misal: Mencatat Transaksi Penjualan, Mengubah Skema Harga, Mengelola DP & Pelunasan, Memproses Pembatalan & Retur, Melacak Margin Produk, Mengekspor Struk Thermal).
  - Kolom: 8 peran internal (pemilik, kepala_percetakan, pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang).
  - Isi sel: Simbol akses yang sesuai (✅, 📖, 📝, ⛔, 🔐, dll.).
  - Sertakan kolom **Catatan Khusus** di ujung kanan untuk menjelaskan pembatasan spesifik (misal: "kasir memerlukan otorisasi pemilik untuk retur").
  - Derivasikan data dari BRD Bab 5.3, SRS Bab 3.1, dan UCD UC-001 s.d UC-006.

- [ ] **Tulis Bab 4.3 (Matriks Akses: Modul M.2)**: Terapkan format yang sama untuk modul M.2.
  - Fungsi: HPP BOM, Limbah Produksi, Satuan & UoM, Sinkronisasi ATK Internal, Stock Opname, Prediksi Re-Order, Price Tracking, Import CSV, Supplier & Utang, Backup & Restore.
  - Perhatikan: Stock Opname memerlukan otorisasi `kepala_percetakan`. Backup/Restore khusus `pemilik`.

- [ ] **Tulis Bab 4.4 (Matriks Akses: Modul M.3)**: Terapkan format yang sama.
  - Fungsi: Saldo PPOB & Alert, Akun Keuangan Terhemat, Transaksi Jasa Service.

- [ ] **Tulis Bab 4.5 (Matriks Akses: Modul M.4)**: Terapkan format yang sama.
  - Fungsi: Data Karyawan & Absensi & Kasbon, Smart Payroll, Poin Insentif, Potongan Kasbon Otomatis.
  - Perhatikan: Smart Payroll dan Potongan Kasbon khusus `pemilik`.

- [ ] **Tulis Bab 4.6 (Matriks Akses: Modul M.5)**: Terapkan format yang sama.
  - Fungsi: Job Tracking, Arsip Desain, Link WhatsApp.
  - Perhatikan: Desainer hanya bisa mengubah status dari `Proses Desain` ke `Produksi`. Produksi_cetak hanya bisa mengubah dari `Produksi` ke `Selesai`.

- [ ] **Tulis Bab 4.7 (Matriks Akses: Modul M.6)**: Terapkan format yang sama.
  - Fungsi: Pinjaman Modal, Laba/Rugi, Jatuh Tempo, Aset & Depresiasi, Pengeluaran Rutin.
  - Perhatikan: Seluruh fungsi di modul ini (kecuali Pengeluaran Rutin) **eksklusif pemilik**. Pengeluaran Rutin bisa diinput oleh `kepala_percetakan` untuk pengeluaran biasa, pengeluaran besar memerlukan otorisasi pemilik.

- [ ] **Tulis Bab 4.8 (Matriks Akses: Modul M.7)**: Terapkan format yang sama.
  - Fungsi: Akses RBAC, Audit Trail, Serah Terima Shift, Rekonsiliasi Kas, Fraud Detection, Input Data Awal.
  - Perhatikan: Audit Trail eksklusif `pemilik`. Shift Handover dan Rekonsiliasi Kas diinput `kasir` dan divalidasi `kepala_percetakan`.

- [ ] **Tulis Bab 4.9 (Matriks Akses: Modul M.8)**: CRM Pelanggan — akses untuk `pramuniaga`, `kasir`, `pemilik`.

- [ ] **Tulis Bab 4.10 (Matriks Akses: Modul M.9)**: Multi-Cabang — konfigurasi eksklusif `pemilik`.

- [ ] **Tulis Bab 4.11 (Matriks Akses: Modul M.10)**: Runtime Config — konfigurasi eksklusif `pemilik`.

- [ ] **Tulis Bab 4.12 (Matriks Akses: Use Case Dasar)**: Login, Logout, Dashboard, Ubah Password — akses untuk semua peran.

#### Bab 5: Matriks Akses Level Database (Tabel CRUD)

- [ ] **Tulis Bab 5.1 (Konvensi Operasi CRUD)**: Definisikan konvensi simbol CRUD:
  - `C` = Create (INSERT)
  - `R` = Read (SELECT)
  - `U` = Update (UPDATE)
  - `D` = Delete (DELETE)
  - `-` = Tidak Ada Akses
  - `*` = Melalui Sistem Otomatis (bukan input manual user)

- [ ] **Tulis Bab 5.2 (Matriks CRUD per Tabel Database)**: Buat tabel matriks besar dengan:
  - Baris: 28 tabel database (dari Data Dictionary).
  - Kolom: 8 peran internal, masing-masing dibagi sub-kolom CRUD (C/R/U/D).
  - Isi sel: Simbol CRUD yang sesuai berdasarkan analisis data dari BRD, SRS, dan Use Case.
  - Contoh: Tabel `pinjaman_bank` → pemilik: CRUD, semua peran lain: ---- (tidak ada akses).
  - Contoh: Tabel `transaksi` → kasir: CR--, pramuniaga: C-R-, pemilik: CRUD.
  - Jika suatu tabel memiliki akses terbatas yang kompleks, tambahkan catatan kaki di bawah tabel.

#### Bab 6: Aturan Otorisasi Khusus dan Eskalasi

- [ ] **Tulis Bab 6.1 (Aturan Otorisasi Supervisor — Eskalasi Pemilik)**: Daftarkan semua operasi yang memerlukan input kata sandi pemilik sebagai otorisasi eskalasi. Ambil dari SRS-F-004 (Retur/Batal memerlukan verifikasi pemilik), SRS-F-029 (Pengeluaran besar memerlukan persetujuan pemilik). Gunakan format tabel: No, Operasi, Pemicu Eskalasi, Peran Peminta, Peran Penyetuju, Kode Error Jika Ditolak.

- [ ] **Tulis Bab 6.2 (Aturan Otorisasi Kepala Percetakan)**: Daftarkan operasi yang memerlukan persetujuan Kepala Percetakan. Ambil dari SRS-F-011 (Stock Opname memerlukan otorisasi kepala_percetakan), SRS-F-032 (Shift Handover validasi).

- [ ] **Tulis Bab 6.3 (Aturan Pembatasan Akses Data Sensitif)**: Jelaskan secara eksplisit data apa saja yang diklasifikasikan sebagai data sensitif pemilik (pinjaman bank, pinjaman kerabat, tabungan aset, payroll gaji, audit trail, konfigurasi runtime) dan mengapa data tersebut dilarang keras diakses oleh peran staf operasional. Kaitkan dengan kepatuhan UU PDP No. 27/2022 untuk data pelanggan (CRM).

- [ ] **Tulis Bab 6.4 (Aturan Session dan Timeout Akses)**: Jelaskan mekanisme JWT 8 jam, auto-logout setelah session expired, dan implikasinya terhadap kontrol akses. Ambil dari SRS-NF-05 (JWT 8 jam) dan BRD Bab 9 Poin 8.

- [ ] **Tulis Bab 6.5 (Aturan Rate Limiting dan Penguncian Akun)**: Jelaskan mekanisme brute-force protection: 5 kali gagal login → kunci 10 menit. Ambil dari SRS-NF-06. Jelaskan bahwa mekanisme ini berlaku untuk semua peran tanpa pengecualian.

- [ ] **Tulis Bab 6.6 (Aturan Pencatatan Audit Trail pada Pelanggaran Akses)**: Jelaskan bahwa setiap percobaan akses yang ditolak oleh sistem RBAC wajib dicatat ke tabel `audit_logs` dengan `action_type = 'ACCESS_DENIED'`. Ambil dari SRS-F-030 dan SRS-F-031.

#### Bab 7: Pemetaan Akses terhadap Alur Kerja

- [ ] **Tulis Bab 7.1 s.d 7.5**: Untuk setiap alur kerja kritis (Transaksi Kasir, Produksi Cetak, Stock Opname, Retur/Pembatalan, Smart Payroll), buat diagram Mermaid *flowchart* atau *sequence diagram* sederhana yang menunjukkan titik-titik di mana validasi RBAC terjadi. Tandai setiap decision point dengan simbol kunci (🔐) dan kode error otorisasi terkait.

#### Bab 8: Matriks Ketertelusuran Kebutuhan

- [ ] **Tulis Bab 8.1 (Pemetaan ACM terhadap BRD)**: Buat tabel traceability dua arah: kolom ACM Entry ID → kolom BRD Requirement ID (BR-F-XX). Pastikan setiap entri ACM dapat ditelusuri kembali ke kebutuhan bisnis BRD.

- [ ] **Tulis Bab 8.2 (Pemetaan ACM terhadap SRS)**: Buat tabel traceability dua arah: kolom ACM Entry ID → kolom SRS Requirement ID (SRS-F-XXX). Pastikan setiap entri ACM dapat ditelusuri ke spesifikasi teknis SRS.

- [ ] **Tulis Bab 8.3 (Pemetaan ACM terhadap Use Case Diagram)**: Buat tabel traceability: kolom ACM Entry ID → kolom UC-ID. Pastikan setiap fungsi di matriks akses memiliki use case yang berkorespondensi.

#### Bab 9: Ringkasan Statistik Hak Akses

- [ ] **Tulis ringkasan kuantitatif**: Buat tabel ringkasan statistik yang memuat:
  - Jumlah total fungsi/menu yang dimatriks.
  - Jumlah fungsi yang diakses oleh setiap peran.
  - Persentase akses per peran (misal: pemilik = 100%, fotocopy_print = X%).
  - Jumlah operasi yang memerlukan eskalasi.
  - Jumlah tabel database yang bersifat eksklusif pemilik.

#### Bab 10: Glosarium

- [ ] **Tulis glosarium istilah keamanan** yang digunakan dalam dokumen (RBAC, ACM, CRUD, Least Privilege, Separation of Duties, Eskalasi, JWT, bcrypt, Audit Trail, Rate Limiting, Brute-Force, Session Timeout, UU PDP, ACID, dll.). Susun secara alfabetis.

#### Bab 11: Referensi Dokumen

- [ ] **Tulis tabel referensi** yang digunakan dalam penyusunan dokumen ACM ini. Format tabel: No, Nama Berkas Referensi, Lokasi Path Relatif, Keterangan. Isi dengan 7 file referensi dari Bab 3 issue ini.

---

### Fase 4: Validasi dan Penyelesaian

- [ ] **Validasi kelengkapan matriks**: Periksa kembali setiap sel di matriks akses utama (Bab 4) dan matriks CRUD (Bab 5) untuk memastikan tidak ada sel yang kosong tanpa keterangan. Jika ada data yang **tidak ditemukan** di file referensi, tandai sel tersebut dengan penanda:
  ```
  ⚠️ DATA BELUM TERSEDIA — Perlu diisi manual oleh Pemilik
  ```

- [ ] **Validasi konsistensi silang**: Pastikan data hak akses di ACM konsisten dengan tabel RBAC di BRD Bab 5.3, klasifikasi aktor di SRS Bab 2.3, dan aktor primer/sekunder di setiap use case di UCD. Jika ditemukan inkonsistensi, pilih data yang bersumber dari SRS v1.1 (sebagai dokumen teknis paling detail) dan tambahkan catatan penjelasan inkonsistensi.

- [ ] **Validasi bahasa**: Pastikan seluruh kalimat dalam dokumen menggunakan **bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan**, dan mudah dipahami oleh junior programmer atau AI model lain yang lebih murah. Hindari kalimat pasif yang berbelit-belit. Gunakan kalimat aktif dan instruksi langsung.

- [ ] **Validasi kelayakan sebagai referensi**: Pastikan isi dokumen ACM ini **layak untuk dijadikan referensi, acuan, dan input utama** bagi dokumen fase SDLC selanjutnya (System Design Document, Test Plan) tanpa perlu kembali membuka dokumen BRD/SRS untuk mencari informasi kontrol akses. Kualitas kelengkapan isi tidak boleh menimbulkan pertanyaan atau interupsi yang menghambat proses pekerjaan fase berikutnya.

- [ ] **Tulis seluruh hasil pengerjaan** ke dalam target file: `docs/sdlc/02_analysis/06_access_control_matrix.md`

---

## 5. Instruksi Tambahan Khusus untuk Dokumen ACM

Berikut adalah instruksi tambahan yang **spesifik** untuk ciri khas dokumen Access Control Matrix dan kaidah standar pembuatan dokumen ACM di industri:

- [ ] **Prinsip Least Privilege (Hak Akses Terkecil)**: Dalam menyusun setiap sel matriks, terapkan prinsip bahwa setiap peran **hanya diberikan hak akses minimum** yang diperlukan untuk menjalankan tugas pekerjaannya. Jangan memberikan akses lebih dari yang dibutuhkan.

- [ ] **Prinsip Separation of Duties (Pemisahan Tugas)**: Identifikasi dan dokumentasikan secara eksplisit fungsi-fungsi yang memerlukan **pemisahan tugas** (misalnya: kasir yang menginput transaksi tidak boleh sekaligus menyetujui retur/pembatalan). Ini mencegah fraud internal.

- [ ] **Prinsip Default Deny**: Jelaskan di dalam dokumen bahwa kebijakan default akses adalah **DENY** (ditolak). Setiap peran mulai dari tidak memiliki akses, lalu diberikan akses secara eksplisit sesuai kebutuhannya. Ini berlawanan dengan prinsip "default allow" yang tidak aman.

- [ ] **Penanganan Konflik Hak Akses**: Jika suatu peran memiliki akses yang tampak bertentangan (misal: kasir bisa menginput transaksi tetapi tidak bisa menghapus), jelaskan bahwa **pembatasan selalu menang** atas pemberian. Dokumentasikan setiap konflik yang ditemukan dan resolusinya.

- [ ] **Pemetaan ke Kode Error**: Untuk setiap sel dengan status `⛔ DENY` atau `🔐 ESCALATE`, petakan ke kode error SRS terkait (misal: `ERR-AUTH-011: Hak Akses Pemilik Dibutuhkan`) agar tim pengembang dapat langsung mengimplementasikan pesan error yang sesuai.

- [ ] **Deskripsi Granular Status Antrian (Job Tracking)**: Khusus untuk Modul M.5 (Antrian), jabarkan hak akses hingga level **perubahan status antrian spesifik**, bukan hanya "akses penuh" atau "ditolak". Contoh: desainer hanya boleh mengubah status dari `Proses Desain` → `Produksi`, produksi_cetak hanya dari `Produksi` → `Selesai`, kasir hanya dari `Selesai` → `Diambil`.

- [ ] **Compliance UU PDP No. 27/2022**: Tambahkan catatan kepatuhan regulasi di bab yang relevan bahwa akses ke data CRM pelanggan (nama, nomor WhatsApp) dibatasi dan diproteksi sesuai Undang-Undang Pelindungan Data Pribadi Republik Indonesia.

---

## 6. Kriteria Selesai (Definition of Done)

Issue ini dianggap selesai jika seluruh checklist di atas telah terpenuhi dan file target `docs/sdlc/02_analysis/06_access_control_matrix.md` berisi dokumen ACM yang:

1. ✅ Memiliki metadata front matter YAML yang lengkap.
2. ✅ Memiliki riwayat perubahan dokumen.
3. ✅ Memiliki seluruh 11 bab sesuai kerangka yang ditentukan.
4. ✅ Memiliki matriks akses yang mencakup seluruh 44 use case dan 28 tabel database.
5. ✅ Menggunakan notasi simbol akses yang konsisten di seluruh matriks.
6. ✅ Memiliki aturan otorisasi khusus yang jelas dan terdokumentasi.
7. ✅ Memiliki matriks ketertelusuran dua arah (BRD ↔ ACM ↔ SRS ↔ UCD).
8. ✅ Menggunakan bahasa Indonesia yang natural dan tidak ambigu.
9. ✅ Data yang kosong/belum tersedia ditandai dengan penanda `⚠️ DATA BELUM TERSEDIA`.
10. ✅ Memiliki tabel referensi dokumen di bab terakhir.
11. ✅ Kualitas kelengkapan isi tidak menimbulkan pertanyaan yang menghambat fase SDLC selanjutnya.

---

## 7. Referensi File yang Digunakan dalam Penyusunan Issue Ini

| # | Nama Berkas Referensi | Lokasi Path Relatif | Keterangan |
|---|---|---|---|
| 1 | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | BRD v1.1 — Sumber utama tabel RBAC ringkas (Bab 5.3), 8 aktor internal, 43 kebutuhan fungsional, dan aturan bisnis keamanan. |
| 2 | `02_software_requirements.md` | `docs/sdlc/02_analysis/02_software_requirements.md` | SRS v1.1 — Sumber spesifikasi teknis RBAC (SRS-F-030), Audit Trail (SRS-F-031), JWT (SRS-NF-05), Rate Limiting (SRS-NF-06), dan kode error otorisasi. |
| 3 | `03_use_case_diagram.md` | `docs/sdlc/02_analysis/03_use_case_diagram.md` | UCD v1.1 — Sumber pemetaan 44 use case dengan aktor primer/sekunder dan alur otorisasi Exception Flow. |
| 4 | `04_workflow_diagram.md` | `docs/sdlc/02_analysis/04_workflow_diagram.md` | WFD v1.1 — Sumber visualisasi alur kerja operasional antar peran dan titik validasi otorisasi. |
| 5 | `05_data_dictionary.md` | `docs/sdlc/02_analysis/05_data_dictionary.md` | Data Dictionary v1.1 — Sumber definisi 28 tabel database, domain nilai peran pengguna, dan struktur audit_logs. |
| 6 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Stakeholder Register v1.1 — Sumber profil pemangku kepentingan dan Power/Interest Grid. |
| 7 | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Innovation Proposal v1.1 — Sumber parameter inovasi keamanan (RBAC, Audit Trail, Rate Limiting, Fraud Detection). |
