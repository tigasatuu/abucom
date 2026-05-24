---
judul     : Validasi & Penyempurnaan Dokumen CLI Interaction Flow
target    : docs/sdlc/03_design/04_cli_interaction_flow.md
referensi : docs/sdlc/
status    : Open
prioritas : High
tanggal   : 2026-05-24
dibuat_oleh: Antigravity IDE — Senior AI Coding Agent
---

# Validasi & Penyempurnaan Dokumen CLI Interaction Flow

## Konteks & Latar Belakang

Dokumen **CLI Interaction Flow v1.0** (`docs/sdlc/03_design/04_cli_interaction_flow.md`) telah dibuat sebagai deliverable keempat Fase 03 Design pada proyek AbuCom. Dokumen ini mencakup ±2.222 baris dan mendokumentasikan 44 use case interaksi CLI untuk 10 modul fungsional toko percetakan.

Sebelum dokumen ini digunakan sebagai acuan mutlak pada **Fase 04 Implementation** dan **Fase 05 Testing**, dokumen ini **wajib divalidasi secara menyeluruh** untuk memastikan kelengkapan, konsistensi, kualitas struktur, dan kesiapan sebagai referensi implementasi.

Issue ini berisi instruksi step-by-step **low-level** yang harus dieksekusi secara berurutan dan lengkap oleh junior programmer atau AI model kecil/murah. Setiap langkah bersifat atomic dan tidak ambigu.

---

## 1. Persona Pelaksana Issue

Sebelum memulai pekerjaan, **aktifkan persona berikut** dan jadikan sebagai kerangka berpikir selama seluruh proses validasi:

> **Anda adalah: Senior CLI UX Architect & SDLC Document Quality Auditor**
>
> Anda memiliki keahlian gabungan sebagai:
> - **Senior Python Terminal UX Designer** dengan pengalaman mendalam merancang antarmuka CLI industri berbasis `rich`, `tabulate`, dan ANSI color untuk sistem kasir retail.
> - **SDLC Document Reviewer** berpengalaman memvalidasi dokumen desain fase-ke-fase (Design → Implementation → Testing) pada proyek perangkat lunak skala UMKM hingga enterprise.
> - **Access Control & Security Expert** yang memahami RBAC, JWT, bcrypt, rate limiting, dan eskalasi otorisasi multi-level pada sistem multi-role.
> - **Bahasa Indonesia Technical Writer** yang memastikan setiap kalimat dalam dokumen teknis bersifat natural, tidak ambigu, dan dapat dipahami oleh junior programmer tanpa penjelasan tambahan.
>
> Standar validasi Anda: **Zero Tolerance terhadap ambiguitas, data kosong, inkonsistensi, dan ketidaksesuaian antar dokumen.** Setiap temuan harus diperbaiki langsung di dokumen, bukan hanya dicatat.

---

## 2. File yang Harus Dibaca Sebelum Memulai

Baca dan pahami seluruh file berikut sebelum melakukan validasi apapun. Jangan lewatkan satu file pun.

- [ ] **[BACA]** `docs/sdlc/03_design/04_cli_interaction_flow.md` — Dokumen target utama yang akan divalidasi (baca dari baris 1 hingga akhir tanpa skip)
- [ ] **[BACA]** `docs/sdlc/02_analysis/03_use_case_diagram.md` — Sumber 44 use case: ID UC, aktor, precondition, postcondition, alur utama, alur alternatif
- [ ] **[BACA]** `docs/sdlc/02_analysis/02_software_requirements.md` — Kode error standar, spesifikasi library visual, constraint teknis tiap requirement
- [ ] **[BACA]** `docs/sdlc/02_analysis/06_access_control_matrix.md` — Tabel RBAC granular: hak akses per role per modul, eskalasi sandi, menu yang diizinkan
- [ ] **[BACA]** `docs/sdlc/03_design/03_system_architecture.md` — Arsitektur 4-layer, state passing JWT, pure functions, presentation layer pattern
- [ ] **[BACA]** `docs/sdlc/02_analysis/04_workflow_diagram.md` — Swimlane alur harian, decision point, exception flow, trigger antar use case
- [ ] **[BACA]** `docs/sdlc/03_design/01_database_schema.sql` — DDL MySQL InnoDB: nama tabel, kolom, tipe data, constraint, nilai default
- [ ] **[BACA]** `docs/sdlc/03_design/02_erd_database.md` — Relasi kardinalitas, Foreign Key, referential integrity antar tabel
- [ ] **[BACA]** `docs/sdlc/02_analysis/05_data_dictionary.md` — Kamus data: tipe data kolom, panjang field, nullable/not null, keterangan bisnis
- [ ] **[BACA]** `docs/sdlc/02_analysis/01_business_requirements.md` — Konteks bisnis, SOP operasional toko, terminologi bisnis percetakan

---

## 3. Validasi 1 — Komparasi Mendalam: Dokumen Utama vs File Referensi

**Tujuan:** Memastikan dokumen utama sudah merangkum SEMUA data dan informasi yang relevan dari setiap file referensi. Tidak ada use case, aktor, error code, hak akses, atau constraint teknis yang terlewat.

### 3.1. Komparasi dengan Use Case Diagram (UCD v1.1)

- [ ] **[PERIKSA]** Hitung total use case yang terdaftar di `03_use_case_diagram.md`. Catat: total UC = ___
- [ ] **[PERIKSA]** Hitung total use case yang didokumentasikan di `04_cli_interaction_flow.md`. Catat: total UC terdokumentasi = ___
- [ ] **[VALIDASI]** Pastikan setiap UC-001 s.d UC-044 memiliki alur interaksi detail (minimal tabel langkah dan tabel error) di dokumen utama
- [ ] **[VALIDASI]** Pastikan setiap use case di dokumen utama mencantumkan: ID UC, Derivasi SRS, Derivasi WF, Aktor Primer, Menu ID, Hak Akses — tidak boleh ada kolom yang kosong
- [ ] **[VALIDASI]** Pastikan aktor yang tercantum di setiap UC pada dokumen utama konsisten dengan aktor yang didefinisikan di UCD. Cek satu per satu UC-001 hingga UC-044
- [ ] **[VALIDASI]** Pastikan precondition dan postcondition setiap UC di dokumen utama tidak bertentangan dengan yang tertulis di UCD
- [ ] **[VALIDASI]** Pastikan setiap UC yang memiliki relasi `<<include>>` atau `<<extend>>` di UCD sudah direfleksikan dalam alur interaksi dokumen utama (misalnya: UC-001 include UC-002, UC-001 include UC-007, dst)
- [ ] **[CATAT]** Jika ditemukan UC yang ada di UCD tetapi tidak ada di dokumen utama → tandai sebagai **TEMUAN-UCD-xxx** dan perbaiki langsung

### 3.2. Komparasi dengan Software Requirements (SRS v1.1)

- [ ] **[PERIKSA]** Buat daftar semua requirement SRS-F-001 s.d SRS-F-044 dari file SRS
- [ ] **[VALIDASI]** Pastikan setiap alur UC di dokumen utama memiliki kolom `Derivasi SRS` yang merujuk requirement SRS yang tepat dan akurat
- [ ] **[VALIDASI]** Pastikan setiap kode error yang disebutkan di dokumen utama (ERR-AUTH-xxx, ERR-VAL-xxx, ERR-STOCK-xxx, ERR-CASH-xxx, ERR-SESSION-xxx, ERR-DB-xxx, ERR-SYS-xxx) sudah terdefinisi di SRS
- [ ] **[VALIDASI]** Pastikan constraint teknis tiap input (tipe data, panjang karakter, format regex, decimal precision) yang disebutkan di dokumen utama konsisten dengan SRS
- [ ] **[VALIDASI]** Pastikan library visual yang disebutkan di dokumen utama (`rich`, `tabulate`, `getpass`, `decimal`, `pathlib`, `PyJWT`, `bcrypt`) konsisten dengan technology stack yang didefinisikan di SRS
- [ ] **[CATAT]** Jika ditemukan requirement SRS yang relevan tetapi tidak tercermin di dokumen utama → tandai sebagai **TEMUAN-SRS-xxx** dan perbaiki langsung

### 3.3. Komparasi dengan Access Control Matrix (ACM v1.1)

- [ ] **[PERIKSA]** Buat daftar seluruh baris ACM: setiap kombinasi role × modul/tabel × hak akses (CREATE/READ/UPDATE/DELETE/DENY)
- [ ] **[VALIDASI]** Periksa setiap tabel atribut UC di dokumen utama (baris **Hak Akses**): pastikan nilainya **identik** dengan ACM. Cek satu per satu semua 44 UC
- [ ] **[VALIDASI]** Periksa Matriks Visibilitas Menu per Role (Bab 3.3 dokumen utama): pastikan setiap sel (Tampil/Sembunyi) untuk 8 role × 44 menu **identik 100%** dengan ACM. Tidak boleh ada satu sel pun yang berbeda
- [ ] **[VALIDASI]** Pastikan setiap use case yang membutuhkan eskalasi sandi supervisor (contoh: UC-004 Retur, UC-006 Struk, UC-023 Potong Kasbon, UC-031 Pengeluaran > Rp500rb, UC-035 Rekonsiliasi) sudah mencantumkan alur eskalasi sandi pemilik/kepala secara eksplisit di langkah interaksi
- [ ] **[VALIDASI]** Pastikan role yang disebutkan di dokumen utama (`pemilik`, `kepala_percetakan`, `pramuniaga`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang`) berjumlah 8 dan namanya identik dengan yang didefinisikan di ACM (case-sensitive)
- [ ] **[CATAT]** Jika ditemukan inkonsistensi hak akses antara dokumen utama dan ACM → tandai sebagai **TEMUAN-ACM-xxx** dan perbaiki langsung

### 3.4. Komparasi dengan System Architecture (SA v1.1)

- [ ] **[VALIDASI]** Pastikan setiap referensi teknis tentang JWT di dokumen utama (pembuatan token, validasi, state passing, expiry) konsisten dengan SA
- [ ] **[VALIDASI]** Pastikan pola Pure Functions FP yang disebutkan di dokumen utama konsisten dengan SA (tidak ada modifikasi global state)
- [ ] **[VALIDASI]** Pastikan referensi Presentation Layer (struktur loop menu, decorator otorisasi, panel `rich`, tabel `tabulate`) konsisten dengan arsitektur 4-layer di SA
- [ ] **[VALIDASI]** Pastikan mekanisme `graceful exit` dan `clear screen` di dokumen utama konsisten dengan SA
- [ ] **[CATAT]** Jika ditemukan inkonsistensi teknis dengan SA → tandai sebagai **TEMUAN-SA-xxx** dan perbaiki langsung

### 3.5. Komparasi dengan Workflow Diagram (WFD v1.1)

- [ ] **[VALIDASI]** Pastikan kolom `Derivasi WF` di setiap alur UC dokumen utama merujuk ID workflow (WF-M1-xx, WF-CROSS-xx, dll) yang benar sesuai WFD
- [ ] **[VALIDASI]** Pastikan decision point di setiap diagram Mermaid flowchart/sequence dokumen utama mencerminkan decision point yang sama dengan WFD
- [ ] **[VALIDASI]** Pastikan exception flow (alur kegagalan) di WFD sudah tercermin sebagai tabel **Pesan Error yang Mungkin Muncul** di dokumen utama
- [ ] **[VALIDASI]** Pastikan trigger antar use case (contoh: UC-001 memicu UC-007, UC-024, UC-022, UC-006) sudah terdokumentasi di diagram alur dokumen utama
- [ ] **[CATAT]** Jika ditemukan alur di WFD yang tidak tercermin di dokumen utama → tandai sebagai **TEMUAN-WFD-xxx** dan perbaiki langsung

### 3.6. Komparasi dengan Database Schema SQL & ERD & Data Dictionary

- [ ] **[VALIDASI]** Pastikan setiap query SQL yang disebutkan secara eksplisit di tabel langkah interaksi (contoh: `UPDATE transaksi SET status_bayar = 'LUNAS' WHERE id = %s`) menggunakan nama tabel dan nama kolom yang **identik** dengan DDL di `01_database_schema.sql`
- [ ] **[VALIDASI]** Pastikan setiap nilai default, constraint NOT NULL, dan tipe data kolom yang disebutkan di dokumen utama konsisten dengan Data Dictionary
- [ ] **[VALIDASI]** Pastikan relasi JOIN antar tabel yang disebutkan dalam proses query dokumen utama konsisten dengan ERD (Foreign Key yang valid)
- [ ] **[VALIDASI]** Pastikan nama-nama tabel yang disebut di dokumen utama (`transaksi`, `barang`, `pengguna`, `audit_logs`, `laci_kasir`, `system_configs`, dst) semuanya ada di database schema dan tidak ada typo
- [ ] **[CATAT]** Jika ditemukan mismatch nama tabel/kolom → tandai sebagai **TEMUAN-DB-xxx** dan perbaiki langsung

### 3.7. Komparasi dengan Business Requirements (BRD v1.1)

- [ ] **[VALIDASI]** Pastikan terminologi bisnis percetakan yang digunakan di dokumen utama (DP, Pelunasan, Retur, Kasbon, Payroll, Opname, PPOB, dll) konsisten dengan definisi di BRD
- [ ] **[VALIDASI]** Pastikan SOP operasional toko (jam kerja, alur shift kasir, prosedur handover, dll) yang direferensikan di dokumen utama tidak bertentangan dengan BRD
- [ ] **[CATAT]** Jika ditemukan inkonsistensi terminologi atau SOP → tandai sebagai **TEMUAN-BRD-xxx** dan perbaiki langsung

---

## 4. Validasi 2 — Kebersihan & Fokus Konten Dokumen

**Tujuan:** Memastikan dokumen utama HANYA berisi informasi yang spesifik relevan dengan CLI Interaction Flow — tidak berlebihan, tidak duplikat, tidak menyimpang ke topik lain.

- [ ] **[PERIKSA]** Identifikasi apakah ada konten yang seharusnya berada di dokumen lain (misal: detail DDL database, penjelasan ERD, narasi BRD) yang masuk ke dokumen utama secara tidak tepat
- [ ] **[PERIKSA]** Identifikasi apakah ada duplikasi informasi di dalam dokumen utama sendiri (informasi yang sama disebutkan lebih dari satu kali di bab berbeda tanpa konteks yang berbeda)
- [ ] **[VALIDASI]** Pastikan setiap diagram Mermaid yang ada di dokumen utama (flowchart, sequenceDiagram) relevan dan spesifik untuk CLI Interaction Flow — bukan diagram arsitektur atau ERD
- [ ] **[VALIDASI]** Pastikan setiap wireframe ASCII yang ada di dokumen utama menggambarkan tampilan terminal CLI, bukan UI web atau UI desktop
- [ ] **[VALIDASI]** Pastikan Traceability Matrix di dokumen utama hanya memetakan UC → SRS → WFD → ACM, tidak memetakan hal di luar cakupan CLI flow
- [ ] **[HAPUS/PINDAHKAN]** Jika ditemukan konten yang tidak relevan dengan CLI Interaction Flow → hapus dari dokumen utama atau beri komentar `[OUT OF SCOPE — REMOVE]`

---

## 5. Validasi 3 — Standar Struktur Dokumen Industri

**Tujuan:** Memastikan dokumen utama memenuhi standar struktur dokumen desain perangkat lunak industri yang lengkap, profesional, dan informatif.

### 5.1. Periksa Bagian Header & Metadata

- [ ] **[VALIDASI]** Pastikan header YAML frontmatter berisi: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun` — tidak ada yang kosong
- [ ] **[VALIDASI]** Pastikan tabel **Riwayat Perubahan Dokumen** ada dan memuat kolom: Versi, Tanggal, Perubahan, Oleh
- [ ] **[VALIDASI]** Pastikan field **Status** dokumen mencerminkan kondisi aktual (Draft/Review/Approved)

### 5.2. Periksa Bagian Informasi Dokumen

- [ ] **[VALIDASI]** Pastikan Bab 1 memuat: Tujuan, Cakupan, Posisi dalam SDLC, Hubungan dengan Dokumen Lain, Audiens Target, Definisi/Akronim
- [ ] **[VALIDASI]** Pastikan semua akronim yang digunakan dalam dokumen sudah terdefinisi di Bab 1.6 Definisi, Akronim & Singkatan dan/atau Bab Glosarium
- [ ] **[VALIDASI]** Pastikan diagram posisi dokumen dalam SDLC (Bab 1.3) mencerminkan posisi yang akurat

### 5.3. Periksa Bagian Prinsip Desain CLI

- [ ] **[VALIDASI]** Pastikan Bab 2 memuat: Filosofi UX, Konvensi Navigasi Global, Konvensi Visual & Library, Konvensi Input & Validasi, Konvensi Pesan Error, Konvensi Aksesibilitas & Portabilitas
- [ ] **[VALIDASI]** Pastikan konvensi navigasi (hotkey, tombol 0 kembali, konfirmasi Y/N, exit darurat) terdefinisi lengkap dan konsisten dengan yang diterapkan di setiap alur UC
- [ ] **[VALIDASI]** Pastikan palet warna ANSI (Green/Red/Yellow/Blue/Magenta) dan penggunaannya terdefinisi jelas dan diimplementasikan konsisten di seluruh pesan output alur UC

### 5.4. Periksa Bagian Peta Hierarki Menu

- [ ] **[VALIDASI]** Pastikan Bab 3 memuat: Diagram Mermaid hierarki menu, Tabel deskripsi singkat setiap node, Matriks Visibilitas Menu per Role
- [ ] **[VALIDASI]** Pastikan diagram Mermaid hierarki menu mencakup SEMUA node menu (44 UC fungsional + 4 UC dasar = 48 total titik navigasi)
- [ ] **[VALIDASI]** Pastikan Matriks Visibilitas (Bab 3.3) memiliki semua 8 kolom role dan semua baris menu ID yang sesuai

### 5.5. Periksa Setiap Alur UC

- [ ] **[VALIDASI]** Pastikan SETIAP alur use case (UC-001 s.d UC-044) memiliki minimal:
  - [ ] Tabel atribut (ID UC, Derivasi SRS, Derivasi WF, Modul, Aktor Primer, Menu ID, Hak Akses)
  - [ ] Diagram alur Mermaid (minimal untuk UC utama yang kompleks; UC sederhana minimal tabel langkah detail)
  - [ ] Tabel langkah-langkah interaksi detail (kolom: No, Aktor/Sistem, Aksi, Tipe, Contoh Tampilan/Input)
  - [ ] Tabel pesan error yang mungkin muncul (kolom: Kode Error, Pemicu, Pesan yang Ditampilkan)
- [ ] **[VALIDASI]** Pastikan kolom "Tipe" di tabel langkah hanya berisi nilai yang valid: `Input`, `Output`, atau `Proses`
- [ ] **[VALIDASI]** Pastikan kolom "Contoh Tampilan/Input" berisi contoh konkret (bukan placeholder seperti `[...TODO...]`, `TBD`, atau kosong)
- [ ] **[VALIDASI]** Pastikan setiap kode error di tabel pesan error menggunakan format standar: `ERR-[KATEGORI]-[NOMOR]`

### 5.6. Periksa Bagian Wireframe ASCII

- [ ] **[VALIDASI]** Pastikan ada bab wireframe ASCII/terminal mockup yang menggambarkan tampilan layout utama (dashboard, menu utama, form input tipikal)
- [ ] **[VALIDASI]** Pastikan wireframe menggunakan karakter Unicode box-drawing yang konsisten (═══, ║, ╔, ╗, dll) sesuai konvensi Bab 2
- [ ] **[VALIDASI]** Pastikan lebar wireframe tidak melebihi standar terminal (maksimal 80 karakter lebar)

### 5.7. Periksa Bagian Traceability Matrix

- [ ] **[VALIDASI]** Pastikan Traceability Matrix mencakup SEMUA 44 UC (UC-001 s.d UC-044) tanpa ada yang terlewat
- [ ] **[VALIDASI]** Pastikan setiap baris Traceability Matrix memiliki kolom: No UC, ID SRS, Nama Fitur, ID WFD, ID ACM, Status
- [ ] **[VALIDASI]** Pastikan tidak ada sel yang kosong di Traceability Matrix

### 5.8. Periksa Bagian Penutup

- [ ] **[VALIDASI]** Pastikan ada bab Sign-Off atau persetujuan dokumen dengan kolom: Peran, Nama, Tanda Tangan, Tanggal
- [ ] **[VALIDASI]** Pastikan ada bab Glosarium yang mendefinisikan semua istilah teknis dan bisnis yang digunakan
- [ ] **[VALIDASI]** Pastikan ada bab Referensi Dokumen yang mencantumkan semua file input dengan kolom: No, Nama Dokumen, Path Relatif, Keterangan Versi

---

## 6. Validasi 4 — Kualitas sebagai Referensi untuk Fase Berikutnya

**Tujuan:** Memastikan dokumen utama cukup lengkap dan detail sehingga dapat langsung digunakan oleh programmer atau AI coding agent sebagai acuan implementasi tanpa perlu bertanya balik.

- [ ] **[VALIDASI]** Pastikan setiap prompt input yang disebutkan di langkah interaksi menyertakan: teks prompt yang tepat, tipe data yang diharapkan, validasi yang akan dilakukan, dan contoh nilai input
- [ ] **[VALIDASI]** Pastikan setiap output yang disebutkan menyertakan: warna ANSI yang digunakan, format teks/tabel yang digunakan, dan contoh tampilan konkret
- [ ] **[VALIDASI]** Pastikan setiap proses yang disebutkan menyertakan: operasi database (nama tabel, nama kolom, tipe query), fungsi Python yang dipanggil, atau algoritma yang digunakan
- [ ] **[VALIDASI]** Pastikan alur interaksi untuk use case yang memerlukan transaksi database (start transaction, commit, rollback) disebutkan secara eksplisit di tabel langkah
- [ ] **[VALIDASI]** Pastikan use case yang membutuhkan audit log disebutkan secara eksplisit langkah penyimpanan audit log-nya (nama tabel `audit_logs`, kolom yang diisi, nilai `action_type` yang digunakan)
- [ ] **[VALIDASI]** Pastikan use case yang bersifat lintas modul (cross-module trigger) memiliki referensi eksplisit ke UC lain yang dipanggil (contoh: "UC-001 memanggil UC-007 dan UC-024")
- [ ] **[VALIDASI]** Pastikan constraint keamanan (bcrypt, JWT, getpass, parameterized query, ANSI injection sanitization) disebutkan di langkah yang relevan, bukan hanya di bab prinsip desain saja
- [ ] **[VALIDASI]** Pastikan setiap use case yang memiliki state berbeda (BELUM LUNAS/LUNAS, DRAFT/APPROVED, PENDING/SELESAI, RETUR) mendefinisikan semua kemungkinan state dan transisinya secara eksplisit

---

## 7. Validasi 5 — Kualitas Bahasa Indonesia

**Tujuan:** Memastikan seluruh teks dokumen menggunakan Bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau AI model lain.

- [ ] **[PERIKSA]** Baca setiap kalimat dalam dokumen. Identifikasi kalimat yang mengandung campuran Bahasa Indonesia dan Bahasa Inggris secara tidak konsisten di dalam satu kalimat (Inggris berlebihan tanpa konteks teknis yang membenarkan)
- [ ] **[VALIDASI]** Pastikan istilah teknis Bahasa Inggris yang dipertahankan (karena tidak ada padanan Indonesia yang tepat) ditulis dengan konsisten dan tidak berubah-ubah ejaannya (contoh: selalu `tabulate`, bukan `Tabulate` atau `TABULATE`)
- [ ] **[VALIDASI]** Pastikan tidak ada kalimat ganda makna (ambigu) di deskripsi langkah interaksi. Setiap kalimat harus memiliki satu interpretasi yang jelas
- [ ] **[VALIDASI]** Pastikan kalimat perintah/instruksi di kolom "Aksi" menggunakan kata kerja aktif yang jelas (contoh: "Menampilkan...", "Meminta...", "Memproses...", "Menghapus...")
- [ ] **[VALIDASI]** Pastikan tidak ada ejaan atau tata bahasa yang salah (typo, kata tidak baku, singkatan tidak umum)
- [ ] **[VALIDASI]** Pastikan pesan error yang ditampilkan kepada pengguna ditulis dalam Bahasa Indonesia yang sopan, informatif, dan dapat dipahami oleh operator kasir awam tanpa latar belakang teknis

---

## 8. Validasi 6 — Kelengkapan Isi (Tidak Ada Data Kosong)

**Tujuan:** Mengidentifikasi dan mengisi semua data kosong, placeholder, atau bagian yang belum terisi di dalam dokumen.

- [ ] **[SCAN]** Cari seluruh dokumen untuk string berikut (case-insensitive) dan tandai setiap kemunculannya:
  - `[Nama ...]`
  - `[TODO]`
  - `[TBD]`
  - `[PENDING]`
  - `...`
  - `____________`
  - `N/A` (jika tidak seharusnya N/A)
  - `(diisi kemudian)`
  - `(menyusul)`
- [ ] **[PERIKSA]** Pada Bab Sign-Off / Persetujuan: identifikasi apakah ada field nama atau tanda tangan yang masih kosong atau menggunakan placeholder
- [ ] **[ISI]** Untuk setiap data kosong yang ditemukan:
  - Jika data tersebut dapat diisi berdasarkan konteks dokumen dan referensi yang tersedia → **isi dengan data yang akurat dan relevan**
  - Jika data memerlukan informasi eksternal yang tidak tersedia (nama pemilik usaha fisik, nomor telepon aktual, dll) → **isi dengan nilai representatif yang logis** sesuai konteks toko percetakan AbuCom
- [ ] **[VALIDASI]** Pastikan kolom `Derivasi SRS` di SETIAP tabel atribut UC terisi dengan kode SRS yang valid (bukan kosong atau placeholder)
- [ ] **[VALIDASI]** Pastikan kolom `Derivasi WF` di SETIAP tabel atribut UC terisi dengan ID workflow yang valid
- [ ] **[VALIDASI]** Pastikan kolom `Menu ID` di SETIAP tabel atribut UC terisi dengan ID yang konsisten dengan daftar di Bab 3.2

---

## 9. Validasi 7 — Konsistensi Internal Dokumen

**Tujuan:** Memastikan tidak ada inkonsistensi antara bagian satu dan bagian lain di dalam dokumen utama sendiri.

- [ ] **[VALIDASI]** Pastikan jumlah UC yang disebutkan di Bab 1.2 (Cakupan) konsisten dengan jumlah alur UC yang terdokumentasi di Bab 5–14
- [ ] **[VALIDASI]** Pastikan setiap ID Menu yang disebutkan di tabel atribut UC (contoh: `MENU-M1-001`) ada di daftar Bab 3.2 dan Bab 3.3
- [ ] **[VALIDASI]** Pastikan setiap kode error yang disebutkan di tabel "Pesan Error" konsisten dengan kategori yang didefinisikan di Bab 2.5
- [ ] **[VALIDASI]** Pastikan nama role yang digunakan di tabel Hak Akses setiap UC konsisten dengan 8 nama role di Bab 3.3
- [ ] **[VALIDASI]** Pastikan setiap UC yang disebutkan dalam diagram alur Mermaid (sebagai node atau referensi) ada dan terdokumentasi lengkap di bab yang sesuai
- [ ] **[VALIDASI]** Pastikan nomor urut bab dan sub-bab konsisten dan tidak ada yang loncat, terduplikasi, atau salah urut
- [ ] **[VALIDASI]** Pastikan Traceability Matrix di bagian akhir dokumen konsisten dengan detail yang ada di setiap tabel atribut alur UC

---

## 10. Validasi 8 — Spesifik Karakteristik Dokumen CLI Interaction Flow

**Tujuan:** Validasi aspek-aspek unik yang hanya berlaku untuk jenis dokumen CLI Interaction Flow, bukan dokumen SDLC generik.

- [ ] **[VALIDASI]** Pastikan semua prompt input di dokumen menggunakan format yang konsisten: teks prompt diakhiri dengan `: ` (titik dua diikuti spasi) sesuai konvensi UX terminal
- [ ] **[VALIDASI]** Pastikan semua referensi tombol navigasi konsisten: tombol `0` selalu berarti "Kembali" ke menu di atasnya, bukan "Exit" atau "Batal" (kecuali di menu utama level 0 dimana `q` adalah exit darurat)
- [ ] **[VALIDASI]** Pastikan setiap use case yang menggunakan konfirmasi `[Y/N]` menyebutkan secara eksplisit bahwa input bersifat case-insensitive
- [ ] **[VALIDASI]** Pastikan tidak ada use case yang menginstruksikan input password tanpa menggunakan `getpass` (setiap input password WAJIB tidak ditampilkan di layar / no echo)
- [ ] **[VALIDASI]** Pastikan setiap use case yang melibatkan nominal Rupiah menggunakan tipe data `Decimal` (bukan `float` atau `int`)
- [ ] **[VALIDASI]** Pastikan setiap use case yang mengubah data kritis (retur, hapus, pembatalan, payroll, opname, restore) memiliki langkah konfirmasi `[Y/N]` sebelum eksekusi
- [ ] **[VALIDASI]** Pastikan use case yang memiliki aksi destruktif atau finansial bernilai besar (retur, payroll, pengeluaran > Rp500rb, rekonsiliasi kas) memiliki langkah eskalasi sandi yang sesuai dengan ACM
- [ ] **[VALIDASI]** Pastikan breadcrumb navigation path disebutkan di langkah pertama setiap use case dengan format yang konsisten: `Dashboard > M.X Nama Modul > Nama Sub-Menu`
- [ ] **[VALIDASI]** Pastikan semua wireframe ASCII yang ada menampilkan elemen wajib: header/banner aplikasi, breadcrumb path, konten utama, menu navigasi di bawah, dan baris prompt input
- [ ] **[VALIDASI]** Pastikan diagram Mermaid yang menggunakan `sequenceDiagram` memiliki direktif `autonumber` untuk memudahkan referensi langkah saat implementasi
- [ ] **[VALIDASI]** Pastikan setiap use case yang melibatkan perubahan stok barang mencantumkan secara eksplisit operasi pengurangan/penambahan stok di tabel/kolom yang tepat (misalnya: `UPDATE barang SET stok = stok - qty WHERE id = %s`)
- [ ] **[VALIDASI]** Pastikan setiap use case yang menangani file fisik (backup ZIP, ekspor nota TXT, arsip desain) mencantumkan path folder tujuan file dan nama file output yang mengikuti konvensi penamaan yang jelas

---

## 11. Penulisan Ulang Dokumen yang Telah Divalidasi

**Tujuan:** Menuangkan seluruh hasil validasi ke dalam file target dengan cara menimpa (overwrite) file asli secara penuh.

> **⚠️ PERINGATAN KRITIS — BACA SEBELUM MENULIS:**
> - Anda WAJIB menulis ulang SELURUH dokumen dari baris pertama hingga baris terakhir
> - **DILARANG KERAS** melakukan truncation, pemotongan, pemendekan, atau penghilangan bagian apapun dari dokumen
> - Dokumen asli memiliki 2.222 baris; hasil tulisan ulang minimal harus memiliki jumlah baris yang sama atau lebih banyak (karena ada penambahan dari perbaikan)
> - Jika tool atau sistem membatasi panjang output dalam satu pemanggilan, **LANJUTKAN** penulisan di pemanggilan berikutnya secara append/berkelanjutan hingga seluruh dokumen tertulis tuntas — **JANGAN BERHENTI DI TENGAH DOKUMEN**

### 11.1. Persiapan Sebelum Menulis Ulang

- [ ] **[KONFIRMASI]** Buat daftar semua perubahan yang akan dilakukan berdasarkan temuan validasi dari Langkah 3–10 (TEMUAN-UCD-xxx, TEMUAN-SRS-xxx, TEMUAN-ACM-xxx, dll)
- [ ] **[KONFIRMASI]** Tetapkan versi baru dokumen: **v1.0 → v1.1**
- [ ] **[KONFIRMASI]** Tetapkan tanggal revisi: gunakan tanggal hari ini dalam format YYYY-MM-DD
- [ ] **[KONFIRMASI]** Siapkan teks deskripsi perubahan yang akan ditulis di baris baru tabel Riwayat Perubahan Dokumen

### 11.2. Perubahan Wajib yang Harus Diterapkan

- [ ] **[UBAH]** Update field `versi` di YAML frontmatter: dari `1.0` menjadi `1.1`
- [ ] **[UBAH]** Update field `tanggal` di YAML frontmatter: isi dengan tanggal hari ini
- [ ] **[UBAH]** Update field `status` di YAML frontmatter: dari `Draft` menjadi `Review`
- [ ] **[TAMBAH]** Tambahkan baris baru di tabel **Riwayat Perubahan Dokumen** untuk versi 1.1 dengan deskripsi lengkap semua perubahan yang dilakukan
- [ ] **[PERBAIKI]** Terapkan semua temuan dari Validasi 1 (komparasi dengan referensi)
- [ ] **[PERBAIKI]** Terapkan semua temuan dari Validasi 2 (kebersihan konten)
- [ ] **[PERBAIKI]** Terapkan semua temuan dari Validasi 3 (standar struktur industri)
- [ ] **[PERBAIKI]** Terapkan semua temuan dari Validasi 4 (kualitas referensi implementasi)
- [ ] **[PERBAIKI]** Terapkan semua temuan dari Validasi 5 (kualitas bahasa Indonesia)
- [ ] **[ISI]** Isi semua data kosong yang ditemukan dari Validasi 6
- [ ] **[PERBAIKI]** Terapkan semua temuan dari Validasi 7 (konsistensi internal)
- [ ] **[PERBAIKI]** Terapkan semua temuan dari Validasi 8 (karakteristik spesifik CLI flow)

### 11.3. Proses Penulisan Ulang File

- [ ] **[TULIS]** Buka file target untuk ditimpa: `docs/sdlc/03_design/04_cli_interaction_flow.md`
- [ ] **[TULIS]** Tulis ulang seluruh isi dokumen dari baris 1 (dimulai dari YAML frontmatter `---`) hingga baris terakhir
- [ ] **[VERIFIKASI]** Setelah penulisan selesai, hitung total baris dokumen hasil revisi. Pastikan jumlahnya **≥ 2.222 baris** (jumlah baris dokumen asli)
- [ ] **[VERIFIKASI]** Baca kembali 50 baris pertama dan 50 baris terakhir dokumen hasil revisi untuk memastikan tidak ada truncation di awal maupun di akhir dokumen
- [ ] **[VERIFIKASI]** Pastikan field `versi` di YAML frontmatter sudah berubah menjadi `1.1`
- [ ] **[VERIFIKASI]** Pastikan tabel Riwayat Perubahan Dokumen sudah memiliki baris entri untuk versi 1.1

---

## 12. Pembaruan Daftar Referensi Dokumen

**Tujuan:** Memastikan semua file referensi yang digunakan dalam proses validasi tercantum di Bab Referensi Dokumen dalam dokumen utama.

- [ ] **[PERIKSA]** Bandingkan daftar referensi di Bab Referensi Dokumen (Bab 19) dengan daftar file yang dibaca di Langkah 2 issue ini
- [ ] **[VALIDASI]** Pastikan semua 9 referensi dokumen berikut sudah ada di Bab Referensi Dokumen:
  - [ ] `docs/sdlc/02_analysis/03_use_case_diagram.md` (UCD v1.1)
  - [ ] `docs/sdlc/02_analysis/02_software_requirements.md` (SRS v1.1)
  - [ ] `docs/sdlc/02_analysis/06_access_control_matrix.md` (ACM v1.1)
  - [ ] `docs/sdlc/03_design/03_system_architecture.md` (SA v1.1)
  - [ ] `docs/sdlc/02_analysis/04_workflow_diagram.md` (WFD v1.1)
  - [ ] `docs/sdlc/03_design/01_database_schema.sql` (Schema v1.1)
  - [ ] `docs/sdlc/03_design/02_erd_database.md` (ERD v1.1)
  - [ ] `docs/sdlc/02_analysis/05_data_dictionary.md` (Dictionary v1.1)
  - [ ] `docs/sdlc/02_analysis/01_business_requirements.md` (BRD v1.1)
- [ ] **[TAMBAH]** Jika dalam proses validasi ditemukan file referensi baru yang digunakan tetapi belum tercantum di Bab Referensi Dokumen → tambahkan di bagian akhir tabel dengan format kolom yang sama: No | Nama Dokumen Referensi | Path Relatif | Keterangan Versi

---

## 13. Kriteria Selesai (Definition of Done)

Issue ini dianggap **SELESAI** jika dan hanya jika **SEMUA** checklist berikut terpenuhi:

- [ ] Semua file referensi pada Langkah 2 telah dibaca sepenuhnya (10 file)
- [ ] Semua item validasi pada Langkah 3–10 (Validasi 1–8) telah diperiksa dan perbaikan telah diterapkan
- [ ] File `docs/sdlc/03_design/04_cli_interaction_flow.md` telah ditulis ulang sepenuhnya (overwrite) tanpa truncation
- [ ] Versi dokumen di file target telah diubah menjadi `v1.1`
- [ ] Field `status` telah diubah dari `Draft` menjadi `Review`
- [ ] Tabel Riwayat Perubahan memiliki entri baris baru untuk v1.1 dengan deskripsi lengkap
- [ ] Tidak ada lagi placeholder, data kosong, atau field `[TODO]`/`[TBD]` di dokumen
- [ ] Daftar Referensi Dokumen sudah lengkap, akurat, dan mencakup semua file yang digunakan
- [ ] Jumlah baris dokumen hasil revisi ≥ 2.222 baris

---

## 14. Catatan Tambahan untuk Pelaksana

> **Urutan Eksekusi Wajib:** Ikuti urutan langkah secara berurutan: Langkah 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13. **Jangan melompat langkah apapun.**

> **Prioritas Resolusi Konflik Antar Referensi:** Jika ditemukan konflik antara dua file referensi (misalnya ACM dan UCD memberikan data yang berbeda), gunakan urutan prioritas otoritas berikut:
> 1. `06_access_control_matrix.md` — ACM v1.1 (otoritatif untuk hak akses dan visibilitas menu)
> 2. `03_use_case_diagram.md` — UCD v1.1 (otoritatif untuk alur use case dan aktor)
> 3. `02_software_requirements.md` — SRS v1.1 (otoritatif untuk requirement teknis dan kode error)
> 4. `04_workflow_diagram.md` — WFD v1.1 (otoritatif untuk decision flow dan exception)
> 5. `01_database_schema.sql` — Schema v1.1 (otoritatif untuk nama tabel/kolom database)
> 6. `05_data_dictionary.md` — Dictionary v1.1 (otoritatif untuk tipe data dan panjang field)

> **Penanganan Ambiguitas:** Jika ada instruksi di issue ini yang masih tidak jelas setelah membaca file referensi, **jangan asumsikan** — pilih opsi yang paling konservatif dan aman (misal: tambahkan validasi daripada menghapus validasi).

> **Batasan Output Tool:** Jika tool penulisan file memiliki batasan panjang output dalam satu pemanggilan, **jangan potong atau ringkas dokumen**. Tulis dalam beberapa pemanggilan berturut-turut (append) hingga seluruh dokumen tertulis sempurna dari baris pertama hingga baris terakhir.

> **Spot Check Kualitas Akhir:** Setelah menyelesaikan penulisan ulang, lakukan pembacaan spot check pada setidaknya 5 UC yang dipilih secara acak (misalnya: UC-001, UC-011, UC-022, UC-034, UC-044) untuk memastikan kualitas dan kelengkapan perbaikan yang diterapkan.

---

_Issue dibuat oleh: Antigravity IDE — Senior AI Coding Agent_
_Tanggal pembuatan: 2026-05-24_
_Target implementasi: Junior Programmer / AI Model Kecil_
