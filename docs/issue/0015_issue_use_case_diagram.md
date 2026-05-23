# Issue #0015 — Pembuatan Dokumen Use Case Diagram

---
judul        : Pembuatan dan Penyusunan Dokumen Use Case Diagram
dokumen      : Use Case Diagram (UCD)
target file  : docs/sdlc/02_analysis/03_use_case_diagram.md
status       : Open
prioritas    : High
tanggal      : 2026-05-23
---

## 1. Ringkasan Issue

Buatlah dokumen **Use Case Diagram (UCD)** yang lengkap dan komprehensif untuk proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**. Dokumen ini merupakan output ketiga dan terakhir pada **Fase 02 Analysis** dalam siklus SDLC AbuCom. Use Case Diagram berfungsi sebagai representasi visual dan naratif mengenai **interaksi antara aktor (pengguna sistem) dengan fungsionalitas sistem** yang telah didefinisikan di dalam BRD v1.1 dan SRS v1.1. Dokumen ini menjadi jembatan kritis sebelum masuk ke **Fase 03 Design** (System Design Document, ERD, Database Schema).

---

## 2. Persona Pelaksana

**Persona**: `Senior Systems Analyst & UML Modeling Specialist`

**Alasan pemilihan persona**:
- Use Case Diagram adalah artefak UML standar yang membutuhkan keahlian pemodelan sistem berorientasi aktor-fungsionalitas.
- Persona ini memiliki otoritas untuk mendefinisikan boundary system, mengidentifikasi aktor primer/sekunder, memodelkan relasi `<<include>>`, `<<extend>>`, dan generalisasi aktor, serta menyusun narasi use case (use case specification/description) yang presisi sesuai standar industri rekayasa perangkat lunak.
- Persona ini mampu menerjemahkan kebutuhan fungsional (BR-F-xx / SRS-F-xxx) menjadi diagram interaksi visual yang terstruktur dan tidak ambigu.

---

## 3. File Referensi yang Digunakan

Berikut adalah file referensi yang **wajib dibaca dan dirangkum** sebagai basis data utama dalam pengerjaan dokumen ini:

| # | File Referensi | Lokasi Path Relatif | Prioritas | Alasan Penggunaan |
|---|---|---|---|---|
| 1 | `01_business_requirements.md` (BRD v1.1) | `docs/sdlc/02_analysis/01_business_requirements.md` | **PRIMER** | Sumber utama daftar kebutuhan bisnis fungsional (BR-F-01 s.d BR-F-40), daftar 8 aktor internal + 4 aktor eksternal, matriks RBAC, aturan bisnis, dan 10 modul sistem. |
| 2 | `02_software_requirements.md` (SRS v1.1) | `docs/sdlc/02_analysis/02_software_requirements.md` | **PRIMER** | Sumber utama spesifikasi teknis fungsional (SRS-F-001 s.d SRS-F-040+), klasifikasi aktor sistem (8 role), relasi antar modul, dan detail input/output/proses setiap fungsionalitas. |
| 3 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | **SEKUNDER** | Referensi profil 19 stakeholder, klasifikasi Power/Interest, dan peran otoritas masing-masing aktor. |
| 4 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | **TERSIER** | Referensi ruang lingkup modul dan fitur utama yang telah ditetapkan dalam piagam proyek. |
| 5 | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | **TERSIER** | Referensi fitur inovasi tambahan yang telah disetujui untuk diintegrasikan ke dalam sistem. |

> **Catatan**: File `narasi.txt` (`docs/sdlc/narasi.txt`) **tidak lagi diperlukan** sebagai referensi langsung untuk dokumen ini, karena seluruh informasi dari narasi asli pemilik usaha telah diekstraksi, divalidasi, dan distrukturkan secara lengkap di dalam BRD v1.1 dan SRS v1.1. Menggunakan narasi mentah berpotensi menimbulkan inkonsistensi dengan data yang sudah tervalidasi.

---

## 4. Instruksi Umum Pengerjaan

### 4.1. Prinsip Perangkuman Data Referensi
- [ ] Baca **seluruh isi** dari setiap file referensi yang tercantum di Bagian 3 tanpa ada yang terlewat.
- [ ] Rangkum **semua data dan informasi** yang ada di dalam file referensi tersebut. Setiap detail mengenai aktor, fungsionalitas, aturan bisnis, modul, dan relasi antar komponen **jangan sampai ada yang terlewat**.
- [ ] **Hanya ambil dan rangkum** data serta informasi yang **secara spesifik dibutuhkan** oleh dokumen Use Case Diagram ini. Data yang tidak relevan (seperti detail teknis implementasi kode Python, konfigurasi server, versi library, detail arsitektur infrastruktur LAN) **tidak perlu dimasukkan** ke dalam dokumen ini agar dokumen tetap bersih dan fokus.

### 4.2. Prinsip Kualitas Konten
- [ ] Pastikan isi dokumen ini **layak dijadikan referensi, acuan, dan input utama** bagi dokumen-dokumen pada fase tahapan SDLC selanjutnya, khususnya:
  - System Design Document (SDD) — Fase 03 Design
  - Entity Relationship Diagram (ERD) — Fase 03 Design
  - Test Plan & Test Cases — Fase 05 Testing
- [ ] Pastikan **kualitas kelengkapan isi** dokumen ini tidak memerlukan interupsi atau pertanyaan balik yang menghambat proses pekerjaan fase SDLC selanjutnya. Dokumen ini harus **self-contained** dan **self-explanatory**.
- [ ] Gunakan **bahasa Indonesia yang natural**, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau AI model lain yang lebih murah.
- [ ] Jika ada data yang **kosong atau tidak tersedia** pada file referensi, tandai dengan format berikut agar mudah dikenali untuk diisi secara manual:
  ```
  > ⚠️ PERLU DIISI PEMILIK: [Deskripsi data yang dibutuhkan]
  ```

---

## 5. Kerangka Struktur Dokumen Use Case Diagram

Susunlah dokumen target file `docs/sdlc/02_analysis/03_use_case_diagram.md` dengan **struktur kerangka dokumen** berikut ini. Struktur ini mengikuti standar industri praktik pembuatan dokumen Use Case Diagram yang lengkap dan informatif:

```
---
(metadata dokumen: dokumen, proyek, versi, tanggal, status, penyusun)
---

# Use Case Diagram — AbuCom

## Riwayat Perubahan Dokumen
(tabel versi, tanggal, perubahan, oleh)

---

## 1. Informasi Dokumen
### 1.1. Tujuan Dokumen
### 1.2. Cakupan Dokumen
### 1.3. Posisi Dokumen dalam Siklus SDLC
### 1.4. Hubungan dengan Dokumen SDLC Lainnya
### 1.5. Audiens Target

---

## 2. Identifikasi Aktor Sistem
### 2.1. Aktor Internal (Pengguna Sistem)
(tabel: ID Aktor, Nama Aktor, Role Sistem, Deskripsi Singkat, Hak Akses Utama)
### 2.2. Aktor Eksternal (Non-Pengguna Sistem)
(tabel: ID Aktor, Nama Aktor, Deskripsi Singkat, Hubungan dengan Sistem)
### 2.3. Diagram Hierarki Generalisasi Aktor (Mermaid)
(diagram mermaid yang menunjukkan hubungan generalisasi/spesialisasi antar aktor)

---

## 3. System Boundary dan Daftar Use Case
### 3.1. Definisi System Boundary
### 3.2. Master Daftar Use Case
(tabel komprehensif: UC-ID, Nama Use Case, Modul, Aktor Primer, Aktor Sekunder, Prioritas, Derivasi BRD/SRS)

---

## 4. Use Case Diagram (Visual Mermaid)
### 4.1. Diagram Use Case Utama — Keseluruhan Sistem
(diagram mermaid overview seluruh use case dan aktor)
### 4.2. Diagram Use Case per Modul
#### 4.2.1. Modul M.1 — Manajemen Transaksi & Kebijakan Harga
#### 4.2.2. Modul M.2 — Manajemen Inventaris, BOM & Stock Opname
#### 4.2.3. Modul M.3 — Layanan Keuangan Digital, PPOB & Jasa Service
#### 4.2.4. Modul M.4 — Manajemen SDM, Penggajian & Poin Karyawan
#### 4.2.5. Modul M.5 — Sistem Manajemen Antrian & Pelacakan Desain
#### 4.2.6. Modul M.6 — Administrasi Pinjaman, Aset & Pengeluaran
#### 4.2.7. Modul M.7 — Keamanan, Audit Trail & Hak Akses
#### 4.2.8. Modul M.8 — Pembatalan, Retur & CRM
#### 4.2.9. Modul M.9 — Skalabilitas Multi-Cabang
#### 4.2.10. Modul M.10 — Konfigurasi Sistem Runtime

---

## 5. Spesifikasi Naratif Use Case (Use Case Description)
### 5.1. Konvensi Penulisan
(penjelasan format penulisan use case specification yang digunakan)

### 5.2. Spesifikasi Use Case per Modul
(untuk SETIAP use case di daftar Bagian 3.2, tuliskan spesifikasi naratif lengkap berikut):

#### UC-XXX: [Nama Use Case]
| Atribut | Nilai |
|---|---|
| **UC-ID** | UC-XXX |
| **Nama Use Case** | [Nama] |
| **Derivasi** | BR-F-XX / SRS-F-XXX |
| **Modul** | M.X — [Nama Modul] |
| **Prioritas** | High / Medium / Low |
| **Aktor Primer** | [aktor yang menginisiasi] |
| **Aktor Sekunder** | [aktor yang terlibat / di-notify] |
| **Deskripsi Singkat** | [1-2 kalimat tujuan use case] |
| **Prakondisi (Precondition)** | [kondisi yang harus terpenuhi sebelum use case dimulai] |
| **Pemicu (Trigger)** | [aksi yang memicu dimulainya use case] |
| **Alur Utama (Main Flow / Basic Flow)** | (langkah-langkah sekuensial bernomor) |
| **Alur Alternatif (Alternative Flow)** | (variasi dari alur utama) |
| **Alur Pengecualian (Exception Flow)** | (skenario error / gagal) |
| **Pasca-Kondisi (Postcondition)** | [kondisi setelah use case berhasil selesai] |
| **Aturan Bisnis Terkait** | [aturan bisnis yang berlaku] |
| **Catatan Khusus** | [informasi tambahan] |

(ulangi format di atas untuk setiap use case)

---

## 6. Relasi Antar Use Case
### 6.1. Relasi <<include>>
(tabel dan penjelasan setiap relasi include antar use case)
### 6.2. Relasi <<extend>>
(tabel dan penjelasan setiap relasi extend antar use case)
### 6.3. Generalisasi Use Case
(jika ada use case yang merupakan generalisasi/spesialisasi dari use case lain)

---

## 7. Matriks Traceability Use Case
### 7.1. Matriks UC ↔ BRD
(tabel mapping: UC-ID ↔ BR-F-XX)
### 7.2. Matriks UC ↔ SRS
(tabel mapping: UC-ID ↔ SRS-F-XXX)
### 7.3. Matriks UC ↔ Aktor
(tabel mapping: UC-ID ↔ Aktor yang terlibat)

---

## 8. Glosarium
(daftar istilah UML dan domain bisnis yang digunakan dalam dokumen ini)

---

## 9. Referensi Dokumen
(tabel daftar file referensi yang digunakan dalam pengerjaan dokumen ini)
```

---

## 6. Instruksi Detail Tahapan Pengerjaan (Low-Level Checklist)

Berikut adalah tahapan-tahapan yang **WAJIB** dilakukan secara berurutan. Setiap langkah sudah dipecah menjadi checklist operasional agar tidak ada ambiguitas.

---

### Tahap 1: Pembacaan dan Perangkuman File Referensi

> **Tujuan**: Mengumpulkan dan merangkum seluruh data relevan dari file referensi.

- [ ] **1.1.** Baca file `docs/sdlc/02_analysis/01_business_requirements.md` (BRD v1.1) secara **keseluruhan dari awal sampai akhir**.
  - [ ] 1.1.1. Rangkum semua **aktor internal** (8 peran) beserta deskripsi dan hak akses dari Bagian 5.1 dan tabel RBAC Bagian 5.3.
  - [ ] 1.1.2. Rangkum semua **aktor eksternal** (4 aktor: Pelanggan, Supplier, Bank BRI/Mandiri, Kerabat) dari Bagian 5.4.
  - [ ] 1.1.3. Rangkum **seluruh kebutuhan bisnis fungsional** (BR-F-01 s.d BR-F-40) dari Bagian 7, catat: ID, nama, deskripsi, aktor terkait, aturan bisnis, dan prioritas masing-masing.
  - [ ] 1.1.4. Rangkum **10 modul sistem** (M.1 s.d M.10) dan pengelompokan fitur per modul.
  - [ ] 1.1.5. Rangkum **aturan bisnis numerik** dari Bagian 9 (skema harga, Smart Payroll, kasbon, poin insentif, PPOB, rekonsiliasi kas, keamanan akun).
  - [ ] 1.1.6. Rangkum **proses bisnis To-Be** dari Bagian 4.3 (alur kerja yang diharapkan setelah sistem diterapkan).

- [ ] **1.2.** Baca file `docs/sdlc/02_analysis/02_software_requirements.md` (SRS v1.1) secara **keseluruhan dari awal sampai akhir**.
  - [ ] 1.2.1. Rangkum **semua spesifikasi kebutuhan fungsional** (SRS-F-001 s.d SRS-F-040+, termasuk SRS-F-ADD-xx jika ada), catat: ID, nama, derivasi BRD, modul, prioritas, aktor, input yang diperlukan, proses/logika bisnis, output, dan aturan validasi.
  - [ ] 1.2.2. Rangkum **klasifikasi dan karakteristik 8 aktor pengguna** dari Bagian 2.3.
  - [ ] 1.2.3. Rangkum **ketergantungan antar SRS-F** (kolom "Ketergantungan" di setiap spesifikasi) untuk mengidentifikasi relasi `<<include>>` dan `<<extend>>`.
  - [ ] 1.2.4. Rangkum **kebutuhan non-fungsional** (SRS-NF-xxx) yang relevan dengan perilaku aktor di sistem (misal: RBAC, Audit Trail, session JWT).

- [ ] **1.3.** Baca file `docs/sdlc/01_planning/03_stakeholder_register.md` secara **keseluruhan**.
  - [ ] 1.3.1. Rangkum **profil 19 stakeholder**, klasifikasi Power/Interest Grid, dan relevansi masing-masing stakeholder terhadap penggunaan sistem.

- [ ] **1.4.** Baca file `docs/sdlc/01_planning/01_project_charter.md` secara **keseluruhan**.
  - [ ] 1.4.1. Rangkum **daftar modul dan fitur utama** yang tertulis di bagian ruang lingkup proyek.
  - [ ] 1.4.2. Rangkum informasi tambahan yang belum tercakup di BRD/SRS (jika ada).

- [ ] **1.5.** Baca file `docs/sdlc/01_planning/05_innovation_proposal.md` secara **keseluruhan**.
  - [ ] 1.5.1. Rangkum **daftar inovasi yang telah disetujui** (INV-INT-xx, INV-REC-xx, INV-NEW-xx) yang mempengaruhi fungsionalitas use case.

---

### Tahap 2: Identifikasi dan Pendefinisian Aktor

> **Tujuan**: Mendefinisikan secara lengkap seluruh aktor yang berinteraksi dengan sistem.

- [ ] **2.1.** Berdasarkan rangkuman Tahap 1, susun **daftar aktor internal** (pengguna yang login ke sistem) dengan format tabel:
  - ID Aktor (misal: ACT-01)
  - Nama Aktor (misal: Pemilik Usaha)
  - Role Sistem (misal: `pemilik`)
  - Deskripsi Singkat (1-2 kalimat)
  - Hak Akses Utama (ringkasan dari matriks RBAC BRD Bagian 5.3)

- [ ] **2.2.** Susun **daftar aktor eksternal** (entitas luar yang tidak login tetapi menjadi bagian interaksi bisnis) dengan format tabel:
  - ID Aktor (misal: ACT-EXT-01)
  - Nama Aktor (misal: Pelanggan AbuCom)
  - Deskripsi Singkat
  - Hubungan dengan Sistem (bagaimana aktor ini berinteraksi walaupun tidak login)

- [ ] **2.3.** Identifikasi apakah ada **relasi generalisasi antar aktor**. Contoh potensi generalisasi:
  - Aktor umum `Staf Operasional` yang merupakan generalisasi dari `pramuniaga`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang`.
  - Aktor umum `Supervisor` yang merupakan generalisasi dari `kepala_percetakan` dan `pemilik`.
  - Evaluasi apakah generalisasi ini membantu menyederhanakan diagram tanpa kehilangan detail penting.

- [ ] **2.4.** Buat **diagram hierarki generalisasi aktor** menggunakan sintaks Mermaid.

---

### Tahap 3: Identifikasi dan Penyusunan Daftar Use Case

> **Tujuan**: Memetakan seluruh fungsionalitas sistem menjadi daftar use case terstruktur.

- [ ] **3.1.** Definisikan **system boundary** (batas sistem AbuCom CLI). Jelaskan apa yang berada di dalam dan di luar boundary.

- [ ] **3.2.** Berdasarkan rangkuman BR-F-xx dari BRD v1.1 dan SRS-F-xxx dari SRS v1.1, susun **master daftar use case** dalam format tabel komprehensif:
  - UC-ID (misal: UC-001)
  - Nama Use Case (misal: "Mencatat Transaksi Penjualan Multi-Divisi")
  - Modul (misal: M.1)
  - Aktor Primer (aktor yang menginisiasi use case)
  - Aktor Sekunder (aktor lain yang terlibat atau menerima notifikasi)
  - Prioritas (High / Medium)
  - Derivasi BRD (BR-F-XX)
  - Derivasi SRS (SRS-F-XXX)

- [ ] **3.3.** Pastikan **setiap BR-F-xx** di BRD v1.1 (BR-F-01 s.d BR-F-40) memiliki **minimal satu UC** yang berkorespondensi. Jika satu BR-F memiliki beberapa skenario interaksi yang berbeda antar aktor, pecah menjadi beberapa UC terpisah.

- [ ] **3.4.** Identifikasi apakah ada **use case tambahan** yang belum secara eksplisit tercantum di BRD/SRS tetapi secara logis dibutuhkan oleh sistem. Contoh:
  - UC Login ke Sistem
  - UC Logout dari Sistem
  - UC Melihat Dashboard Ringkasan Harian
  - UC Mengubah Password Sendiri

- [ ] **3.5.** Kelompokkan seluruh UC berdasarkan **10 modul** (M.1 s.d M.10).

---

### Tahap 4: Pembuatan Diagram Use Case Visual (Mermaid)

> **Tujuan**: Membuat diagram visual Use Case menggunakan sintaks Mermaid.

- [ ] **4.1.** Buat **1 diagram Use Case utama (overview)** yang menampilkan seluruh aktor dan seluruh use case dalam satu system boundary. Gunakan **blok kode Mermaid** (format ```` ```mermaid ````). Jika diagram terlalu besar/padat, pecah menjadi beberapa sub-diagram per kelompok modul.

- [ ] **4.2.** Buat **10 diagram Use Case per modul** (M.1 s.d M.10) yang masing-masing menampilkan:
  - Aktor yang berinteraksi dengan use case di modul tersebut
  - Daftar use case spesifik modul tersebut
  - Relasi `<<include>>` dan `<<extend>>` antar use case (jika ada)
  - Relasi generalisasi aktor (jika ada)

- [ ] **4.3.** Gunakan **konvensi visual Mermaid** yang konsisten:
  - Aktor digambar sebagai entitas di luar boundary
  - Use case digambar di dalam boundary
  - Relasi `<<include>>` dan `<<extend>>` menggunakan notasi panah putus-putus dengan label
  - Berikan label yang jelas dan ringkas pada setiap elemen

- [ ] **4.4.** Pastikan **setiap diagram** dapat di-render dengan benar oleh parser Mermaid standar. Hindari karakter khusus atau sintaks yang tidak didukung.

---

### Tahap 5: Penulisan Spesifikasi Naratif Use Case

> **Tujuan**: Menulis deskripsi naratif lengkap untuk setiap use case.

- [ ] **5.1.** Tentukan **konvensi format penulisan** spesifikasi use case yang akan digunakan secara konsisten di seluruh dokumen (lihat template format di Bagian 5 kerangka di atas).

- [ ] **5.2.** Untuk **setiap use case** yang terdaftar di master daftar (Tahap 3), tuliskan spesifikasi naratif lengkap dengan mengisi **semua atribut** dalam template:
  - [ ] UC-ID dan Nama Use Case
  - [ ] Derivasi (BR-F-XX / SRS-F-XXX)
  - [ ] Modul terkait
  - [ ] Prioritas
  - [ ] Aktor Primer dan Sekunder
  - [ ] Deskripsi Singkat (1-2 kalimat tujuan use case)
  - [ ] Prakondisi (Precondition) — kondisi yang harus terpenuhi sebelum use case dimulai
  - [ ] Pemicu (Trigger) — aksi spesifik yang memulai use case
  - [ ] Alur Utama (Main Flow / Basic Flow) — langkah-langkah bernomor yang menggambarkan interaksi normal antara aktor dan sistem
  - [ ] Alur Alternatif (Alternative Flow) — variasi sah dari alur utama
  - [ ] Alur Pengecualian (Exception Flow) — skenario kegagalan atau error
  - [ ] Pasca-Kondisi (Postcondition) — keadaan setelah use case berhasil selesai
  - [ ] Aturan Bisnis Terkait — merujuk ke aturan bisnis numerik dari BRD Bagian 9
  - [ ] Catatan Khusus — informasi tambahan jika ada

- [ ] **5.3.** Pastikan **alur utama** ditulis dalam format langkah-langkah sekuensial bernomor yang menggambarkan **dialog interaksi bolak-balik** antara aktor dan sistem. Contoh format:
  ```
  1. Aktor [Kasir] memilih menu "Transaksi Baru" di terminal CLI.
  2. Sistem menampilkan formulir input transaksi dengan kolom: barang, kuantitas, tipe pelanggan.
  3. Aktor [Kasir] memasukkan ID barang dan kuantitas.
  4. Sistem menghitung subtotal berdasarkan skema harga yang berlaku.
  5. ...
  ```

- [ ] **5.4.** Pastikan setiap **alur pengecualian** mereferensikan kode error yang sudah didefinisikan di SRS v1.1 (misal: `ERR-DB-001`, `ERR-VAL-002`, dst.).

---

### Tahap 6: Identifikasi Relasi Antar Use Case

> **Tujuan**: Memetakan relasi `<<include>>`, `<<extend>>`, dan generalisasi antar use case.

- [ ] **6.1.** Identifikasi **relasi `<<include>>`** — use case yang secara wajib memanggil/menyertakan use case lain. Contoh potensi:
  - UC "Mencatat Transaksi" `<<include>>` UC "Memvalidasi Login Session (JWT)"
  - UC "Memproses Retur Barang" `<<include>>` UC "Memverifikasi Otorisasi Pemilik"
  - UC "Menyelesaikan Produksi" `<<include>>` UC "Menghitung HPP BOM"
  - UC "Memproses Payroll Bulanan" `<<include>>` UC "Menghitung Laba Bersih Bulanan"

- [ ] **6.2.** Identifikasi **relasi `<<extend>>`** — use case yang secara opsional memperluas perilaku use case lain berdasarkan kondisi tertentu. Contoh potensi:
  - UC "Mencatat Transaksi" `<<extend>>` UC "Mengirim Notifikasi WhatsApp" (hanya jika pesanan kustom selesai)
  - UC "Mencatat Transaksi" `<<extend>>` UC "Mencetak Struk Nota Thermal" (hanya jika kasir memilih cetak)
  - UC "Login ke Sistem" `<<extend>>` UC "Menampilkan Alert Jatuh Tempo H-3" (hanya jika level pemilik dan ada jatuh tempo mendekat)
  - UC "Merekam Limbah Produksi" `<<extend>>` UC "Menampilkan Alert Stok Kritis" (hanya jika stok menipis)

- [ ] **6.3.** Identifikasi **generalisasi use case** (jika ada use case induk yang merupakan bentuk umum dari beberapa use case spesifik).

- [ ] **6.4.** Susun hasilnya dalam **tabel relasi** yang jelas:
  - Tabel `<<include>>`: UC Induk → UC yang Di-include → Alasan
  - Tabel `<<extend>>`: UC Dasar → UC Ekstensi → Kondisi Pemicu Ekstensi

---

### Tahap 7: Penyusunan Matriks Traceability

> **Tujuan**: Membuat pemetaan silang dua arah untuk menjamin kelengkapan cakupan.

- [ ] **7.1.** Buat **Matriks UC ↔ BRD**: Tabel yang memetakan setiap UC-ID ke BR-F-XX yang diderivasi. Pastikan **tidak ada BR-F-XX yang tidak memiliki UC** (kecuali yang non-fungsional).

- [ ] **7.2.** Buat **Matriks UC ↔ SRS**: Tabel yang memetakan setiap UC-ID ke SRS-F-XXX yang berkorespondensi.

- [ ] **7.3.** Buat **Matriks UC ↔ Aktor**: Tabel yang memetakan setiap UC-ID ke aktor-aktor yang terlibat (primer dan sekunder).

- [ ] **7.4.** Lakukan **validasi silang**: Pastikan setiap baris di matriks konsisten — tidak ada UC yang tidak memiliki aktor, tidak ada UC yang tidak memiliki derivasi BRD/SRS.

---

### Tahap 8: Penulisan Bagian Pendukung Dokumen

> **Tujuan**: Melengkapi bagian-bagian non-inti dokumen.

- [ ] **8.1.** Tulis **metadata dokumen** (header YAML) sesuai konvensi dokumen SDLC AbuCom yang sudah ada:
  ```yaml
  ---
  dokumen    : Use Case Diagram (UCD)
  proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
  versi      : 1.0
  tanggal    : [tanggal pengerjaan]
  status     : Draft
  penyusun   : Senior Systems Analyst & UML Modeling Specialist
  ---
  ```

- [ ] **8.2.** Tulis **Riwayat Perubahan Dokumen** (tabel versi).

- [ ] **8.3.** Tulis **Bagian 1: Informasi Dokumen** (tujuan, cakupan, posisi SDLC, hubungan dengan dokumen lain, audiens target).

- [ ] **8.4.** Tulis **Glosarium** yang berisi istilah UML dan domain bisnis percetakan yang digunakan di dokumen ini. Minimal mencakup:
  - Use Case, Aktor, System Boundary, Precondition, Postcondition, Trigger
  - Include, Extend, Generalization
  - Main Flow, Alternative Flow, Exception Flow
  - Istilah domain yang sudah ada di BRD (BOM, HPP, RBAC, PPOB, dll.)

- [ ] **8.5.** Tulis **Bagian Referensi Dokumen** di bagian akhir paling bawah yang mencantumkan tabel daftar semua file referensi yang digunakan dalam pengerjaan dokumen ini, dengan format:

  | # | Nama Berkas Referensi | Lokasi Path Relatif | Keterangan |
  |---|---|---|---|
  | 1 | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | BRD v1.1 — Referensi primer daftar aktor, kebutuhan fungsional, dan aturan bisnis. |
  | 2 | `02_software_requirements.md` | `docs/sdlc/02_analysis/02_software_requirements.md` | SRS v1.1 — Referensi primer spesifikasi teknis fungsional dan klasifikasi aktor. |
  | ... | ... | ... | ... |

---

### Tahap 9: Penulisan ke Target File

> **Tujuan**: Menuangkan seluruh hasil pengerjaan ke dalam target file.

- [ ] **9.1.** Tulis **seluruh isi dokumen** yang telah disusun ke dalam file target: `docs/sdlc/02_analysis/03_use_case_diagram.md`.
- [ ] **9.2.** Pastikan format markdown valid dan konsisten (heading, tabel, code block mermaid, list).
- [ ] **9.3.** Pastikan semua diagram Mermaid menggunakan blok kode yang benar (` ```mermaid `).
- [ ] **9.4.** Pastikan tidak ada bagian yang kosong atau placeholder generik (seperti `[TODO]`, `[TBD]`) kecuali penanda `⚠️ PERLU DIISI PEMILIK` untuk data yang memang tidak tersedia.
- [ ] **9.5.** Pastikan dokumen **tidak terpotong** — tulis dari awal hingga akhir secara utuh.

---

### Tahap 10: Validasi Akhir

> **Tujuan**: Memverifikasi kualitas dan kelengkapan dokumen.

- [ ] **10.1.** Verifikasi bahwa **seluruh 8 aktor internal** (pemilik, kepala_percetakan, pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang) telah terdaftar dan terpetakan ke use case masing-masing.
- [ ] **10.2.** Verifikasi bahwa **seluruh 4 aktor eksternal** (Pelanggan, Supplier, Bank BRI/Mandiri, Kerabat/Keluarga) telah terdaftar.
- [ ] **10.3.** Verifikasi bahwa **seluruh BR-F-01 s.d BR-F-40** dari BRD v1.1 memiliki minimal 1 use case yang berkorespondensi di matriks traceability.
- [ ] **10.4.** Verifikasi bahwa **setiap use case** memiliki spesifikasi naratif lengkap (tidak ada atribut yang kosong).
- [ ] **10.5.** Verifikasi bahwa **setiap diagram Mermaid** memiliki sintaks yang valid dan dapat di-render.
- [ ] **10.6.** Verifikasi bahwa **bagian referensi dokumen** di akhir file sudah lengkap.
- [ ] **10.7.** Verifikasi bahwa **bahasa Indonesia** yang digunakan natural, tidak ambigu, dan mudah dipahami.
- [ ] **10.8.** Verifikasi bahwa **tidak ada data yang hilang** dari file referensi — cross-check dengan rangkuman Tahap 1.

---

## 7. Instruksi Tambahan Khusus Use Case Diagram

Berikut adalah instruksi tambahan yang **spesifik** untuk ciri khas dokumen Use Case Diagram yang mungkin belum tercakup di atas:

### 7.1. Penamaan Use Case
- [ ] Gunakan **kata kerja aktif** sebagai awalan nama use case. Contoh: "Mencatat Transaksi", "Menghitung HPP", "Memverifikasi Login", "Menampilkan Laporan".
- [ ] Hindari penamaan yang terlalu teknis atau menggunakan istilah pemrograman. Gunakan istilah yang bermakna bisnis.
- [ ] Penamaan harus konsisten di seluruh dokumen (diagram, tabel, dan narasi).

### 7.2. Granularitas Use Case
- [ ] Tentukan **tingkat granularitas** yang tepat. Use case harus cukup detail untuk menggambarkan satu unit interaksi bermakna antara aktor dan sistem, tetapi tidak terlalu detail hingga menjadi langkah prosedural teknis.
- [ ] Jika satu BR-F memiliki **beberapa skenario interaksi yang melibatkan aktor berbeda**, pecah menjadi use case terpisah.
- [ ] Jika beberapa BR-F berkaitan erat dan selalu dijalankan bersama oleh aktor yang sama, pertimbangkan untuk menggabungkannya menjadi satu use case dengan alur alternatif.

### 7.3. Aktor Primer vs Sekunder
- [ ] **Aktor Primer**: Aktor yang secara aktif menginisiasi (memulai) use case.
- [ ] **Aktor Sekunder**: Aktor yang dilibatkan oleh sistem selama eksekusi use case (misal: pemilik diminta verifikasi sandi saat kasir memproses retur, atau sistem mengirim notifikasi ke kepala percetakan).
- [ ] Pastikan pembedaan ini konsisten di seluruh dokumen.

### 7.4. Konsistensi dengan RBAC
- [ ] Pastikan **aktor yang ditugaskan ke setiap use case** konsisten dengan **matriks RBAC** di BRD v1.1 Bagian 5.3. Misalnya: use case "Melihat Laporan Laba/Rugi" hanya boleh memiliki aktor primer `pemilik` karena kolom "Keuangan & Laba/Rugi" pada RBAC menunjukkan bahwa semua peran staf memiliki status `Ditolak`.

### 7.5. Penanganan Use Case Otomatis (System-Initiated)
- [ ] Identifikasi use case yang dipicu secara **otomatis oleh sistem** (bukan oleh aktor manusia). Contoh:
  - "Menjalankan Backup Database Harian Otomatis" (dipicu oleh scheduler pukul 21:00)
  - "Mengevaluasi Alert Jatuh Tempo saat Login" (dipicu saat startup login pemilik)
  - "Menampilkan Alert Stok Kritis" (dipicu saat stok bahan baku melewati batas minimum)
- [ ] Untuk use case system-initiated, aktor primer dapat dituliskan sebagai `Sistem (Otomatis)` atau `Timer/Scheduler`.

### 7.6. Kualitas Diagram Mermaid
- [ ] Gunakan **layout yang rapi dan mudah dibaca**. Hindari crossing lines yang berlebihan.
- [ ] Jika diagram per modul memiliki terlalu banyak use case (> 8), pertimbangkan memecahnya menjadi sub-diagram.
- [ ] Berikan **komentar/label** pada relasi `<<include>>` dan `<<extend>>` agar pembaca memahami alasan relasi tersebut.

---

## 8. Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **selesai** apabila:

1. ✅ File `docs/sdlc/02_analysis/03_use_case_diagram.md` telah terisi lengkap sesuai kerangka struktur di Bagian 5.
2. ✅ Seluruh 8 aktor internal dan 4 aktor eksternal telah terdokumentasi.
3. ✅ Seluruh kebutuhan fungsional BRD (BR-F-01 s.d BR-F-40) telah dipetakan ke minimal 1 use case.
4. ✅ Setiap use case memiliki spesifikasi naratif lengkap (precondition, trigger, main flow, alternative flow, exception flow, postcondition).
5. ✅ Diagram Mermaid (overview + per modul) dapat di-render dengan benar.
6. ✅ Matriks traceability (UC ↔ BRD, UC ↔ SRS, UC ↔ Aktor) lengkap dan konsisten.
7. ✅ Relasi `<<include>>` dan `<<extend>>` antar use case telah diidentifikasi dan didokumentasikan.
8. ✅ Bagian referensi dokumen di akhir file telah terisi lengkap.
9. ✅ Bahasa Indonesia natural, tidak ambigu, dan mudah dipahami.
10. ✅ Tidak ada placeholder generik (`[TODO]`, `[TBD]`) kecuali penanda `⚠️ PERLU DIISI PEMILIK`.

---

## 9. Referensi File untuk Issue Ini

| # | Nama Berkas | Lokasi Path Relatif | Keterangan |
|---|---|---|---|
| 1 | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | BRD v1.1 — Sumber primer aktor, kebutuhan fungsional, RBAC, dan aturan bisnis. |
| 2 | `02_software_requirements.md` | `docs/sdlc/02_analysis/02_software_requirements.md` | SRS v1.1 — Sumber primer spesifikasi teknis fungsional, input/output, dan error handling. |
| 3 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Stakeholder Register v1.1 — Profil 19 stakeholder dan klasifikasi Power/Interest. |
| 4 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Project Charter v1.1 — Ruang lingkup modul dan fitur utama proyek. |
| 5 | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Innovation Proposal v1.1 — Daftar 43 inovasi terintegrasi yang mempengaruhi fungsionalitas. |
