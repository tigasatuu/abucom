---
judul      : Validasi, Review & Revisi Dokumen Module Structure
target_file: docs/sdlc/04_implementation/03_module_structure.md
prioritas  : Tinggi
tipe       : Documentation Review & Validation
dibuat_oleh: Senior Software Architect & Module Decomposition Specialist
tanggal    : 2026-05-29
status     : Open
---

# Validasi, Review & Revisi Dokumen Module Structure

## Ringkasan Issue

Lakukan pemeriksaan, analisis, dan validasi menyeluruh terhadap dokumen **Module Structure** (`docs/sdlc/04_implementation/03_module_structure.md`) dengan cara membandingkannya secara mendalam dengan seluruh dokumen referensi yang tercantum di dalamnya. Setelah validasi selesai, tuangkan kembali dokumen yang telah diperbaiki ke **file yang sama** (overwrite/timpa), pastikan seluruh konten ditulis ulang sepenuhnya dari baris pertama hingga terakhir tanpa ada pemotongan, dan ubah nomor versi sebagai tanda telah direvisi.

---

## Persona Eksekutor

> **PENTING:** Sebelum memulai pekerjaan apa pun, adopsi dan pertahankan persona berikut selama seluruh proses pengerjaan issue ini.

Kamu adalah seorang **Principal Software Architect & Technical Documentation Auditor** dengan spesialisasi di bidang:
- Arsitektur sistem berlapis (*layered architecture*) untuk aplikasi Python CLI berbasis *Functional Programming* murni.
- *SDLC (Software Development Life Cycle)* standar industri, khususnya fase Implementation dan hubungannya dengan fase Design & Analysis.
- Standar penulisan dokumen teknis industri perangkat lunak (IEEE 1016, ISO/IEC 26512).
- Ketertelusuran (*traceability*) kebutuhan dari SRS hingga implementasi kode file-level.
- Kepatuhan regulasi privasi data (UU PDP No. 27/2022) dalam konteks sistem ERP usaha kecil-menengah.
- Penulisan spesifikasi yang tidak ambigu dan dapat langsung dieksekusi oleh junior programmer maupun model AI yang lebih kecil.

Gunakan sudut pandang auditor yang kritis, teliti, dan tidak mentoleransi kelalaian sekecil apapun.

---

## Informasi Konteks

| Atribut | Detail |
| --- | --- |
| **Dokumen Utama (Target File)** | `docs/sdlc/04_implementation/03_module_structure.md` |
| **Versi Saat Ini** | v1.1 |
| **Versi Setelah Revisi** | v1.2 |
| **Fase SDLC** | 04 — Implementation (Deliverable ke-3) |
| **Posisi dalam SDLC** | Setelah Coding Standard & Environment Setup; sebelum Konstruksi Kode Aktual |

---

## Dokumen Referensi yang Wajib Dibaca

Baca seluruh dokumen referensi berikut sebelum memulai validasi apapun. Ini adalah sumber kebenaran (*source of truth*) yang akan dijadikan dasar perbandingan.

| No | Kode Ref | Nama Dokumen | Path File |
| :---: | :---: | --- | --- |
| 1 | R-01 | Software Requirements Specification v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| 2 | R-02 | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` |
| 3 | R-03 | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` |
| 4 | R-04 | Access Control Matrix v1.1 | `docs/sdlc/02_analysis/06_access_control_matrix.md` |
| 5 | R-05 | CLI Interaction Flow v1.1 | `docs/sdlc/03_design/04_cli_interaction_flow.md` |
| 6 | R-06 | BOM & HPP Design v1.1 | `docs/sdlc/03_design/05_bom_hpp_design.md` |
| 7 | R-07 | Database Schema DDL SQL v1.1 | `docs/sdlc/03_design/01_database_schema.sql` |
| 8 | R-08 | Environment Setup v1.1 | `docs/sdlc/04_implementation/02_environment_setup.md` |

---

## Tahapan Implementasi (Step-by-Step — Low Level)

Ikuti tahapan berikut secara **berurutan**. Jangan lewati satu pun tahap. Tandai setiap checklist `[ ]` menjadi `[x]` di dalam catatan kerja kamu saat selesai menyelesaikannya.

---

### TAHAP 0 — Persiapan & Pembacaan Awal

- [ ] **T0.1** Baca seluruh isi `docs/sdlc/04_implementation/03_module_structure.md` dari baris 1 hingga baris terakhir. Pastikan tidak ada bagian yang dilewati. Catat: total jumlah baris, jumlah section utama, dan versi dokumen saat ini.
- [ ] **T0.2** Baca seluruh isi **R-01** (`docs/sdlc/02_analysis/02_software_requirements.md`). Catat: daftar seluruh ID SRS (SRS-F-xxx dan SRS-F-ADD-xxx), jumlah total modul fungsional, dan jumlah total Use Case (UC-xxx).
- [ ] **T0.3** Baca seluruh isi **R-02** (`docs/sdlc/03_design/03_system_architecture.md`). Catat: nama dan jumlah layer arsitektur, aturan dependensi antar-layer, spesifikasi connection pooling, retry mechanism, dan konfigurasi multi-branch.
- [ ] **T0.4** Baca seluruh isi **R-03** (`docs/sdlc/04_implementation/01_coding_standard.md`). Catat: konvensi penamaan (snake_case/PascalCase), aturan pure FP, aturan result pattern, aturan type hints, dan layout direktori yang distandarkan.
- [ ] **T0.5** Baca seluruh isi **R-04** (`docs/sdlc/02_analysis/06_access_control_matrix.md`). Catat: daftar 8 peran internal, daftar seluruh Use Case dengan ID-nya (UC-001 s.d UC-044), dan matriks CRUD per tabel.
- [ ] **T0.6** Baca seluruh isi **R-05** (`docs/sdlc/03_design/04_cli_interaction_flow.md`). Catat: seluruh Menu ID (MENU-BASE-xxx, MENU-Mx-xxx), konvensi visual rich/tabulate, dan pola navigasi menu.
- [ ] **T0.7** Baca seluruh isi **R-06** (`docs/sdlc/03_design/05_bom_hpp_design.md`). Catat: formula HPP desimal, aturan pembulatan, penanganan limbah, dan sinkronisasi ATK.
- [ ] **T0.8** Baca seluruh isi **R-07** (`docs/sdlc/03_design/01_database_schema.sql`). Catat: daftar nama seluruh 28 tabel InnoDB beserta nama kolom kunci (primary key, foreign key, kolom `cabang_id`).
- [ ] **T0.9** Baca seluruh isi **R-08** (`docs/sdlc/04_implementation/02_environment_setup.md`). Catat: daftar nama library dan versi yang dikunci di `requirements.txt`, struktur `.env.example`, dan konfigurasi `venv`.

---

### TAHAP 1 — Validasi Kelengkapan Isi vs. Dokumen Referensi (Criteria #2 & #3)

> **Tujuan:** Memastikan tidak ada data penting dari referensi yang terlewat dicantumkan di dokumen utama.

#### 1.A — Komparasi Modul Fungsional (vs. R-01)

- [ ] **T1.A.1** Bandingkan daftar 10 modul fungsional (M.1–M.10) di Tabel Section 2.3 dengan daftar modul di R-01. Verifikasi: apakah semua nama modul dan tanggung jawab utamanya sudah sesuai dan lengkap? Catat setiap ketidaksesuaian.
- [ ] **T1.A.2** Verifikasi apakah jumlah total Use Case (UC) yang disebutkan di dokumen (44 Use Case) sudah sesuai dengan data di R-04. Jika tidak sesuai, catat perbedaannya dan angka yang benar.
- [ ] **T1.A.3** Periksa Matriks SRS-to-File (Section 14). Bandingkan satu per satu setiap ID SRS dari daftar yang dicatat di T0.2 dengan baris di matriks Section 14. Cari ID SRS yang ada di R-01 tetapi **tidak tercantum** di Section 14. Catat semua yang hilang.
- [ ] **T1.A.4** Periksa apakah semua ID SRS yang tercantum di Section 14 sudah memiliki kolom `Berkas Handler Utama` dan `Lokasi Fungsi Spesifik` yang terisi (tidak kosong). Catat baris yang datanya kosong atau generik (contoh: "TBD", "-", atau "N/A" tanpa penjelasan).

#### 1.B — Komparasi Layer Arsitektur (vs. R-02)

- [ ] **T1.B.1** Periksa Section 2.1 (Diagram 4-Layer). Bandingkan nama dan definisi ke-4 layer dengan R-02. Verifikasi apakah ada layer atau komponen lintas-layer (*cross-cutting concerns*) yang ada di R-02 tetapi tidak tergambar di dokumen utama.
- [ ] **T1.B.2** Periksa Section 2.2 (Aturan Dependensi). Bandingkan aturan dependensi satu arah (top-down) di dokumen utama dengan aturan yang didefinisikan di R-02. Verifikasi tidak ada aturan yang hilang atau bertentangan.
- [ ] **T1.B.3** Periksa apakah spesifikasi `db_connector.py` (Section 6.2) sudah mencantumkan detail `pool_name`, `pool_size`, retry mechanism, dan kode error MySQL (`2006`, `2013`) yang ada di R-02 dan R-08.

#### 1.C — Komparasi Standar Kode (vs. R-03)

- [ ] **T1.C.1** Periksa setiap contoh signature fungsi di Section 5 (logic/) dan Section 7 (middleware/). Verifikasi apakah semua parameter dan return type sudah menggunakan type hints sesuai standar PEP 484 yang ditetapkan di R-03.
- [ ] **T1.C.2** Periksa apakah penggunaan `typing.list` vs `list` (Python 3.9+) sudah konsisten di seluruh contoh signature. R-03 mendefinisikan standar mana yang digunakan; ikuti standar tersebut.
- [ ] **T1.C.3** Periksa apakah pola `Result Pattern` (NamedTuple dengan field `is_success`, `data`, `error_msg`) sudah diterapkan secara konsisten di seluruh contoh signature fungsi yang mengembalikan hasil operasi. Catat setiap fungsi yang seharusnya menggunakan Result Pattern tetapi tidak melakukannya.
- [ ] **T1.C.4** Periksa apakah layout direktori di Section 3.1 sudah identik dengan layout yang ditetapkan di R-03. Catat setiap perbedaan nama folder, file, atau urutan.

#### 1.D — Komparasi Hak Akses (vs. R-04)

- [ ] **T1.D.1** Periksa setiap sub-section file `cli/` (Section 4.1–4.7). Untuk setiap file, bandingkan daftar peran **Allowed** dan **Denied** dengan matriks hak akses di R-04. Verifikasi apakah ada peran yang salah ditempatkan, hilang, atau berlebihan.
- [ ] **T1.D.2** Periksa Section 13 (Module-to-File Mapping). Verifikasi apakah semua 10 modul fungsional (M.1–M.10) sudah terpetakan ke file yang tepat di semua kolom layer.

#### 1.E — Komparasi Menu ID (vs. R-05)

- [ ] **T1.E.1** Periksa setiap kolom `Hubungan Use Case / Menu ID` di Section 4.1–4.7. Bandingkan semua Menu ID yang tercantum (MENU-BASE-xxx, MENU-Mx-xxx) dengan daftar lengkap Menu ID di R-05. Catat Menu ID yang ada di R-05 tetapi tidak tercantum di dokumen utama, atau Menu ID di dokumen utama yang tidak ada di R-05 (tidak valid).

#### 1.F — Komparasi Formula BOM/HPP (vs. R-06)

- [ ] **T1.F.1** Periksa spesifikasi `logic/bom_hpp.py` (Section 5.2). Verifikasi apakah semua fungsi kalkulasi yang disebutkan di R-06 (formula HPP desimal, penanganan limbah, sinkronisasi ATK) sudah tercantum sebagai contoh signature atau deskripsi fungsi. Catat fungsi yang hilang.
- [ ] **T1.F.2** Verifikasi apakah aturan presisi desimal (`ROUND_HALF_UP`, 4 desimal) yang disebutkan di Section 5.2 sudah konsisten dengan spesifikasi di R-06.

#### 1.G — Komparasi Tabel Database (vs. R-07)

- [ ] **T1.G.1** Periksa Matriks Table-to-File (Section 15). Hitung jumlah tabel yang terdaftar. Bandingkan setiap nama tabel di Section 15 dengan skema DDL di R-07. Verifikasi: (a) jumlah total tabel harus **tepat 28**, (b) tidak ada nama tabel yang salah eja, (c) tidak ada tabel di R-07 yang tidak terdapat di Section 15.
- [ ] **T1.G.2** Periksa setiap `Tabel Database diakses` di Section 4 (cli/). Verifikasi apakah semua nama tabel yang disebutkan ada di skema DDL R-07 dengan nama yang persis sama (case-sensitive).
- [ ] **T1.G.3** Verifikasi apakah kolom `cabang_id` sebagai mekanisme multi-branch (R-02 dan R-07) sudah disebutkan secara eksplisit dalam konteks yang relevan di dokumen utama (misalnya di Section 5.2 pada fungsi `proses_pemotongan_stok`).

#### 1.H — Komparasi Environment & Library (vs. R-08)

- [ ] **T1.H.1** Periksa Section 10.2 (requirements.txt). Bandingkan seluruh nama library dan versi yang tercantum dengan daftar locked requirements di R-08. Catat setiap library yang hilang, versi yang berbeda, atau library di R-08 yang tidak ada di dokumen utama.
- [ ] **T1.H.2** Periksa Section 8.2 (config/settings.py). Bandingkan daftar variabel `.env` yang dikelola dengan daftar di `.env.example` di R-08. Catat variabel yang hilang atau tidak sesuai.

---

### TAHAP 2 — Validasi Fokus & Relevansi Konten (Criteria #4)

> **Tujuan:** Memastikan dokumen hanya berisi informasi yang memang menjadi domain dan tanggung jawab dokumen Module Structure.

- [ ] **T2.1** Baca ulang Section 1.2 (Cakupan Dokumen). Verifikasi apakah seluruh poin cakupan yang disebutkan memang benar-benar dibahas di section-section selanjutnya. Jika ada poin cakupan yang disebutkan tetapi tidak dibahas, catat. Jika ada pembahasan yang tidak termasuk dalam cakupan yang dideklarasikan, catat sebagai konten berlebih.
- [ ] **T2.2** Periksa Section 5 (Business Logic). Pastikan tidak ada penjelasan detail implementasi kode yang terlalu dalam (bukan level spesifikasi file, melainkan level coding tutorial). Dokumen Module Structure cukup mendefinisikan: tujuan, modul terkait, dependensi impor, aturan FP, dan contoh signature—bukan implementasi lengkap.
- [ ] **T2.3** Periksa Section 6 (Data Access). Pastikan tidak ada query SQL literal yang tertanam di dokumen ini (query SQL adalah domain dokumen Database Schema, bukan Module Structure). Hanya pola wrapper/transaction pattern yang boleh ada sebagai ilustrasi.
- [ ] **T2.4** Verifikasi bahwa diagram Mermaid (Section 2.1, 2.4, 16, 17) hanya berisi informasi arsitektur level modul/file—bukan detail implementasi baris kode.
- [ ] **T2.5** Periksa apakah ada informasi redundan (duplikat) yang muncul lebih dari sekali di section berbeda dengan konten identik. Jika ada, catat dan rekomendasikan penggabungan atau penghapusan salah satunya.

---

### TAHAP 3 — Validasi Standar Struktur Dokumen (Criteria #5)

> **Tujuan:** Memastikan dokumen memiliki struktur yang sesuai standar dokumen teknis industri.

- [ ] **T3.1** Verifikasi bahwa bagian **front matter** (header YAML di baris 1–8) sudah memiliki semua field wajib: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`. Verifikasi juga bahwa nilainya tidak kosong atau placeholder.
- [ ] **T3.2** Verifikasi bahwa **Riwayat Perubahan Dokumen** (Section awal) sudah memiliki kolom: `Versi`, `Tanggal`, `Perubahan`, `Oleh`. Pastikan setiap versi tercatat dengan deskripsi perubahan yang informatif.
- [ ] **T3.3** Periksa apakah Section **1. Informasi Dokumen** sudah lengkap dengan semua sub-section standar: Tujuan, Cakupan, Posisi SDLC, Hubungan dengan Dokumen Lain (Input & Output), Audiens Target, dan Definisi/Akronim.
- [ ] **T3.4** Verifikasi bahwa Section **Definisi, Akronim, dan Singkatan** (Section 1.6) sudah mencakup semua singkatan dan istilah teknis yang digunakan di seluruh dokumen. Baca seluruh dokumen dan catat semua istilah teknis/akronim unik, kemudian cek apakah semuanya ada di Section 1.6. Tambahkan yang hilang.
- [ ] **T3.5** Verifikasi bahwa setiap section spesifikasi file (Section 4–9) memiliki sub-field yang konsisten: `Tujuan/Tanggung Jawab`, `Modul Fungsional`, `Dependensi Impor`, `Contoh Signature Fungsi` (jika relevan), dan `Modul SRS di-cover`. Catat sub-field yang hilang di setiap file.
- [ ] **T3.6** Verifikasi bahwa Section **Persetujuan dan Otorisasi** (Section 18) ada dan sudah diisi dengan nama, peran stakeholder, dan status persetujuan yang valid (bukan kosong atau "TBD").
- [ ] **T3.7** Verifikasi bahwa Section **Glosarium** (Section 19) ada dan cukup komprehensif. Tambahkan istilah penting yang muncul di dokumen tetapi tidak ada di glosarium.
- [ ] **T3.8** Verifikasi bahwa Section **Referensi Dokumen** (Section 20) ada, lengkap, dan mencantumkan semua dokumen yang benar-benar dirujuk di dalam dokumen. Format tabel harus memiliki kolom: `No`, `Nama Dokumen`, `Lokasi Path Relatif`, `Keterangan Penggunaan`.
- [ ] **T3.9** Periksa konsistensi nomor section. Verifikasi bahwa tidak ada section yang bernomor sama (duplikat) atau section yang nomornya loncat. Urutan harus berurutan dari Section 1 hingga Section akhir.
- [ ] **T3.10** Verifikasi bahwa semua diagram Mermaid (Section 2.1, 2.4, 16, 17) dapat di-render tanpa error sintaks. Periksa secara manual: tidak ada label node yang mengandung karakter khusus Mermaid tanpa di-escape, tidak ada edge yang tidak terhubung ke node yang dideklarasikan.

---

### TAHAP 4 — Validasi Kelayakan sebagai Referensi Fase SDLC Berikutnya (Criteria #6)

> **Tujuan:** Memastikan dokumen cukup lengkap dan presisi untuk dijadikan input utama fase konstruksi kode.

- [ ] **T4.1** Simulasikan perspektif developer yang akan membuat file `logic/bom_hpp.py` dari nol hanya menggunakan dokumen ini. Periksa apakah Section 5.2 sudah cukup memberikan: (a) nama fungsi yang harus dibuat, (b) parameter dan tipe datanya, (c) return type, (d) docstring pendek, dan (e) modul SRS yang di-cover. Catat informasi yang kurang.
- [ ] **T4.2** Simulasikan perspektif developer yang akan membuat file `middleware/auth_jwt.py`. Periksa Section 7.2 dengan kriteria yang sama seperti T4.1.
- [ ] **T4.3** Simulasikan perspektif developer yang akan membuat file `db/db_connector.py`. Periksa Section 6.2: apakah `pool_name`, `pool_size`, kode error MySQL, dan formula backoff ($2^n$ detik) sudah cukup spesifik untuk diimplementasikan tanpa harus membuka dokumen lain?
- [ ] **T4.4** Periksa apakah setiap file CLI (Section 4.2–4.7) sudah mendefinisikan dengan jelas: (a) daftar fungsi publik beserta signature-nya, (b) tabel database yang diakses, dan (c) hak akses per peran. Catat file yang informasinya masih ambigu atau tidak lengkap.
- [ ] **T4.5** Periksa apakah matriks ketertelusuran (Section 13, 14, 15) cukup komprehensif sehingga seorang developer dapat dengan mudah menemukan: "SRS mana yang ditangani oleh file ini?" dan "File mana yang menangani SRS ini?" tanpa ambiguitas.
- [ ] **T4.6** Verifikasi apakah Section 3.3 (Aturan Penempatan File Baru) cukup eksplisit dan operasional. Aturan harus menjawab: "Jika saya membuat file baru X yang berfungsi Y, saya harus menaruhnya di folder Z."

---

### TAHAP 5 — Validasi Bahasa Indonesia & Keterbacaan (Criteria #7)

> **Tujuan:** Memastikan dokumen menggunakan bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau model AI murah.

- [ ] **T5.1** Baca ulang seluruh teks narasi di dokumen (bukan kode/tabel). Identifikasi kalimat yang:
  - (a) Terlalu panjang dan beranak-pinak (lebih dari 3 klausa dalam 1 kalimat).
  - (b) Menggunakan istilah teknis bahasa Inggris tanpa padanan/penjelasan bahasa Indonesia.
  - (c) Ambigu: bisa diinterpretasikan lebih dari satu cara.
  - (d) Menggunakan kata ganti orang yang tidak jelas subjeknya.
  Catat nomor baris dan kalimat bermasalah beserta saran perbaikannya.
- [ ] **T5.2** Verifikasi konsistensi penggunaan istilah. Contoh: apakah "pure function" dan "fungsi murni" digunakan secara bergantian tanpa penjelasan bahwa keduanya merujuk hal yang sama? Pilih satu istilah dominan dan konsistensikan.
- [ ] **T5.3** Periksa apakah semua singkatan atau akronim yang pertama kali muncul di teks naratif sudah diperkenalkan dengan kepanjangannya (misalnya: "RBAC (*Role-Based Access Control*)").
- [ ] **T5.4** Periksa judul setiap section dan sub-section. Pastikan judulnya informatif dan mencerminkan isi section tersebut. Hindari judul yang terlalu generik seperti "Lainnya" atau "Miscellaneous".
- [ ] **T5.5** Verifikasi bahwa instruksi-instruksi bersifat imperatif (*wajib*, *dilarang keras*, *harus*) sudah ditulis dengan tegas dan tidak bisa disalah-tafsirkan. Kalimat yang berisi batasan keras harus menggunakan kata yang eksplisit, bukan kata yang ambigu seperti "sebaiknya" atau "dianjurkan" jika maksudnya adalah wajib.

---

### TAHAP 6 — Validasi Kelengkapan & Anti-Interupsi (Criteria #8)

> **Tujuan:** Memastikan kualitas dokumen tidak akan memicu pertanyaan atau interupsi berulang dari tim developer selama fase konstruksi.

- [ ] **T6.1** Identifikasi semua pertanyaan yang mungkin muncul dari seorang junior developer ketika membaca dokumen ini untuk pertama kali. Pertanyaan-pertanyaan umum yang harus sudah dijawab dokumen:
  - "Apa yang harus saya impor untuk membuat file X?"
  - "Library apa versi berapa yang harus saya gunakan?"
  - "Bagaimana cara saya tahu apakah fungsi ini sudah benar?"
  - "Apa yang terjadi jika koneksi database gagal?"
  - "Bagaimana cara saya menambahkan fitur baru tanpa merusak arsitektur?"
  Jika ada pertanyaan yang belum terjawab, identifikasi section mana yang harus diperbarui untuk menjawabnya.
- [ ] **T6.2** Periksa apakah Section 3.3 (Aturan Penempatan File Baru) sudah cukup lengkap dengan contoh konkret. Minimal harus ada contoh: "Jika membuat helper baru → taruh di `utils/`; jika membuat kalkulasi bisnis baru → taruh di `logic/`."
- [ ] **T6.3** Periksa apakah standar error code yang disebutkan di dokumen (seperti `ERR-DB-007`, `ERR-DB-TX`) sudah cukup dijelaskan konteksnya sehingga developer tahu kapan harus melempar/menangkap error tersebut.
- [ ] **T6.4** Verifikasi apakah ada ketergantungan implisit antar-file yang belum dinyatakan secara eksplisit. Contoh: apakah `logic/bom_hpp.py` membutuhkan `config/settings.py` secara tidak langsung? Jika ya, apakah ini sudah tercantum di `Dependensi Impor`?
- [ ] **T6.5** Verifikasi apakah ada edge case penting yang perlu disebutkan di spesifikasi fungsi. Contoh: "Apa yang terjadi jika `komponen_list` kosong pada `hitung_hpp_produk()`?" Minimal harus ada keterangan apakah fungsi melempar exception atau mengembalikan nilai default via Result Pattern.

---

### TAHAP 7 — Validasi & Pengisian Data Kosong (Criteria #9)

> **Tujuan:** Mengisi semua placeholder, data kosong, atau field yang belum diisi dengan data yang sesuai dan relevan.

- [ ] **T7.1** Scan seluruh dokumen untuk mencari string-string berikut yang menandakan data belum terisi: `"TBD"`, `"TODO"`, `"[DIISI]"`, `"N/A"`, `"-"`, `"???"`, `"[placeholder]"`, kolom tabel yang benar-benar kosong. Catat lokasi (nomor baris) setiap temuan.
- [ ] **T7.2** Untuk setiap fungsi dengan body `pass` di contoh signature (misalnya `def hitung_biaya_komponen(...): pass`), verifikasi apakah minimal ada docstring yang menjelaskan apa yang fungsi tersebut harus lakukan. Jika docstring tidak ada atau tidak informatif, tambahkan docstring yang jelas berdasarkan informasi dari referensi terkait.
- [ ] **T7.3** Periksa Section 5.1 (`logic/__init__.py`), Section 6.1 (`db/__init__.py`), Section 7.1 (`middleware/__init__.py`), Section 8.1 (`config/__init__.py`), dan Section 9.1 (`utils/__init__.py`). Verifikasi apakah deskripsi `Tujuan/Tanggung Jawab`-nya sudah cukup informatif. Jika hanya 1 kalimat generik, perkaya dengan menyebutkan konkret fungsi/class apa yang di-re-export.
- [ ] **T7.4** Periksa Section 10 (Entry Point & Root). Verifikasi apakah Section 10.1 (`main.py`) sudah memiliki contoh signature fungsi `main()` dengan deskripsi alur startup (baca `.env` → cek koneksi DB → launch CLI). Jika belum ada, tambahkan.
- [ ] **T7.5** Periksa Section 11 (Testing). Verifikasi apakah sudah ada keterangan tentang: (a) framework testing yang digunakan (pytest?), (b) cara menjalankan test, (c) target code coverage minimum. Jika belum ada, tambahkan berdasarkan standar di R-03 dan R-08.
- [ ] **T7.6** Periksa apakah Section 15 (Table-to-File Mapping) memiliki semua 28 tabel. Jika jumlahnya kurang dari 28, identifikasi tabel mana yang hilang berdasarkan R-07 dan tambahkan baris yang kurang.

---

### TAHAP 8 — Validasi Spesifik Ciri Khas Dokumen Module Structure

> **Tujuan:** Validasi tambahan yang spesifik untuk jenis dokumen Module Structure (tidak ada di kriteria umum).

- [ ] **T8.1** **Konsistensi Arah Impor (Import Direction Consistency):** Bandingkan semua `Dependensi Impor` yang tercantum di Section 4–9 dengan diagram Mermaid Section 16 (Inter-File Import Matrix). Verifikasi: tidak boleh ada file yang mengimpor modul dari layer di atasnya (aturan top-down). Contoh yang dilarang: `logic/bom_hpp.py` mengimpor `cli/menu_inventaris.py`. Catat setiap pelanggaran.
- [ ] **T8.2** **Kelengkapan NamedTuple:** Untuk setiap modul Logic (Section 5), verifikasi apakah semua NamedTuple yang digunakan di signature fungsi sudah dideklarasikan eksplisit di contoh kode (tidak ada NamedTuple yang dipakai tapi tidak dideklarasikan). Tambahkan deklarasi yang hilang.
- [ ] **T8.3** **Konsistensi `cabang_id` sebagai Parameter Multi-Branch:** Verifikasi apakah setiap fungsi di `logic/` yang melakukan query database sudah mencantumkan parameter `cabang_id: int` di signature-nya. Ini adalah persyaratan multi-branch dari R-02.
- [ ] **T8.4** **Kelengkapan Hak Akses di Setiap File CLI:** Untuk setiap file `cli/` (Section 4.2–4.7), verifikasi bahwa daftar peran **Allowed** + **Denied** bila dijumlahkan mencakup tepat 8 peran internal: `pemilik`, `kepala_percetakan`, `pramuniaga`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang`. Tidak boleh ada peran yang tidak disebutkan (ambigu). Catat setiap file yang aksesnya tidak lengkap.
- [ ] **T8.5** **Konsistensi Modul Fungsional di Header Setiap File:** Untuk setiap file yang dispesifikasikan (Section 4–9), verifikasi bahwa field `Modul Fungsional` sudah mencantumkan kode modul yang benar (M.1–M.10) dan nama modul yang konsisten dengan Tabel 2.3. Catat ketidaksesuaian.
- [ ] **T8.6** **Verifikasi Signature `session_state: dict`:** Dokumen menetapkan bahwa semua fungsi menu CLI menerima `session_state: dict` sebagai parameter utama state-passing. Verifikasi bahwa SEMUA fungsi publik di Section 4 (cli/) yang memiliki contoh signature sudah menggunakan parameter ini. Catat yang tidak konsisten.
- [ ] **T8.7** **Verifikasi Penggunaan `Decimal` (bukan `float`):** Setiap fungsi kalkulasi keuangan di Section 5 harus menggunakan `Decimal` dari modul `decimal`, bukan `float`. Periksa seluruh contoh signature dan catat yang masih menggunakan `float`.
- [ ] **T8.8** **Kelayakan Contoh Kode sebagai Boilerplate:** Untuk setiap contoh signature fungsi, verifikasi apakah kode yang diberikan sudah cukup sebagai boilerplate starter (import statements, NamedTuple deklarasi, signature lengkap dengan docstring). Seorang developer harus bisa langsung copy-paste dan mulai mengisi implementasi. Catat yang masih kurang lengkap.

---

### TAHAP 9 — Konsolidasi Temuan & Penyusunan Dokumen Revisi

- [ ] **T9.1** Kompilasi seluruh temuan dari Tahap 1–8 menjadi daftar terstruktur. Kelompokkan temuan berdasarkan jenis: (a) Data hilang/kurang, (b) Data tidak akurat/salah, (c) Inkonsistensi, (d) Masalah bahasa, (e) Masalah struktur.
- [ ] **T9.2** Tentukan prioritas perbaikan: **Kritis** (berdampak langsung pada implementasi), **Penting** (berpotensi menyebabkan ambiguitas), **Minor** (kosmetik dan konsistensi gaya penulisan).
- [ ] **T9.3** Susun draf dokumen yang telah direvisi secara menyeluruh. Pastikan semua temuan kritis dan penting sudah diperbaiki. Untuk temuan minor, terapkan jika waktu memungkinkan.
- [ ] **T9.4** Pastikan draf revisi sudah memenuhi semua kriteria berikut sebelum ditulis ke file:
  - [ ] Header YAML diperbarui: `versi: 1.2`, `tanggal: [tanggal hari ini]`, `status: Revised`.
  - [ ] Riwayat Perubahan ditambah baris baru untuk versi 1.2 dengan deskripsi perubahan yang dilakukan.
  - [ ] Seluruh temuan dari Tahap 1–8 sudah diatasi.
  - [ ] Tidak ada field kosong, "TBD", atau placeholder yang tersisa.
  - [ ] Semua contoh signature sudah memiliki docstring yang informatif.
  - [ ] Seluruh teks narasi menggunakan Bahasa Indonesia yang natural dan tidak ambigu.

---

### TAHAP 10 — Penulisan Dokumen ke File (Overwrite)

> **PERINGATAN KRITIS:** Baca seluruh instruksi di tahap ini dengan sangat teliti sebelum menulis apapun ke file.

- [ ] **T10.1** Pastikan draf revisi sudah selesai dan diverifikasi 100% sebelum menulis ke file.
- [ ] **T10.2** Buka file target: `docs/sdlc/04_implementation/03_module_structure.md`.
- [ ] **T10.3** Tulis ulang seluruh isi file dari **baris pertama hingga baris terakhir** menggunakan konten draf revisi yang telah disiapkan. Ini adalah operasi **overwrite/timpa penuh** — tidak boleh ada append atau partial edit.
- [ ] **T10.4** **DILARANG KERAS:** Memotong, meringkas, memenggal, atau menghilangkan bagian apapun dari dokumen. Seluruh section dari Section 1 hingga Section 20 (atau lebih jika ada section baru) harus ditulis ulang sepenuhnya.
- [ ] **T10.5** **DILARANG KERAS:** Menggunakan komentar seperti `[... konten sama seperti sebelumnya ...]`, `[lanjutan dari versi sebelumnya]`, `[dst.]`, atau singkatan apapun sebagai pengganti teks asli.
- [ ] **T10.6** Verifikasi hasil penulisan: setelah file berhasil ditulis, baca kembali 50 baris pertama dan 50 baris terakhir dokumen untuk memastikan tidak ada truncation di awal atau akhir file.
- [ ] **T10.7** Hitung total baris dokumen yang baru ditulis. Jumlah baris versi 1.2 **harus sama atau lebih banyak** dari versi 1.1 (1.008 baris) karena proses ini adalah penambahan/perbaikan, bukan pengurangan.
- [ ] **T10.8** Verifikasi bahwa header YAML di baris 1–8 sudah menunjukkan `versi: 1.2` dan `status: Revised`.

---

### TAHAP 11 — Pembaruan Referensi Dokumen (Criteria #11)

- [ ] **T11.1** Setelah penulisan selesai, periksa kembali apakah selama proses validasi (Tahap 1–8) ada dokumen referensi **baru** (di luar R-01 s.d. R-08) yang ditemukan, dibaca, atau dirujuk.
- [ ] **T11.2** Jika ada dokumen referensi baru yang ditemukan, tambahkan baris baru di tabel Section 20 (Referensi Dokumen) di bagian akhir dokumen dengan format:

  ```
  | [nomor urut baru] | **[Nama Dokumen vX.X]** | `[path/relatif/dokumen.md]` | [keterangan singkat penggunaan dokumen ini dalam konteks Module Structure] |
  ```

- [ ] **T11.3** Jika tidak ada dokumen referensi baru, lewati T11.2 dan tandai T11.2 sebagai `[x]` (tidak berlaku).
- [ ] **T11.4** Jika ada penambahan referensi, pastikan dokumen di-overwrite ulang untuk menyertakan perubahan ini. Kembali ke T10.3–T10.8.

---

### TAHAP 12 — Verifikasi Akhir (Final QA Check)

- [ ] **T12.1** Baca ulang sekali lagi seluruh dokumen hasil revisi dari awal hingga akhir untuk memastikan tidak ada inkonsistensi yang tertinggal.
- [ ] **T12.2** Verifikasi checklist akhir:
  - [ ] `versi` di header sudah `1.2`
  - [ ] `status` di header sudah `Revised`
  - [ ] Baris baru di Riwayat Perubahan sudah ada untuk versi 1.2
  - [ ] Tidak ada baris yang berisi "TBD", "TODO", "[DIISI]", atau placeholder sejenis
  - [ ] Semua 28 tabel database tercantum di Section 15
  - [ ] Semua 45 ID SRS (SRS-F-001 s.d SRS-F-040 + SRS-F-ADD-01 s.d SRS-F-ADD-05) tercantum di Section 14
  - [ ] Semua diagram Mermaid bebas error sintaks
  - [ ] Setiap file CLI memiliki daftar Allowed/Denied yang mencakup tepat 8 peran
  - [ ] Semua fungsi kalkulasi keuangan menggunakan `Decimal`, bukan `float`
  - [ ] Tidak ada pelanggaran aturan dependensi top-down (layer bawah tidak mengimpor layer atas)
  - [ ] Dokumen ditulis dalam Bahasa Indonesia yang natural dan tidak ambigu
- [ ] **T12.3** Tandai issue ini sebagai **Done** dan laporkan ringkasan temuan dan perubahan yang telah dilakukan.

---

## Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **selesai** apabila seluruh kondisi berikut terpenuhi:

1. Semua checklist dari Tahap 0 hingga Tahap 12 sudah ditandai `[x]`.
2. File `docs/sdlc/04_implementation/03_module_structure.md` sudah diperbarui ke versi `1.2`.
3. Dokumen versi 1.2 telah ditulis ulang sepenuhnya tanpa truncation (jumlah baris >= 1.008 baris).
4. Semua temuan **Kritis** dan **Penting** dari Tahap 1–8 sudah diperbaiki di dalam dokumen.
5. Dokumen sudah merepresentasikan kebenaran tunggal (*single source of truth*) yang dapat langsung dijadikan panduan implementasi kode oleh developer tanpa perlu bertanya lebih lanjut.
6. Laporan ringkasan temuan dan perubahan sudah dibuat.

---

## Catatan Penting untuk Eksekutor

> [!IMPORTANT]
> **Jangan mengandalkan ingatan atau asumsi.** Setiap klaim tentang data (nama tabel, ID SRS, versi library, peran pengguna) HARUS diverifikasi langsung dari file referensi yang dibaca di Tahap 0. Jika ragu, baca kembali file referensinya.

> [!WARNING]
> **Jangan menulis ke file sebelum seluruh Tahap 0–9 selesai.** Penulisan ke file hanya dilakukan SEKALI pada Tahap 10 dengan konten yang sudah final dan terverifikasi.

> [!CAUTION]
> **Operasi penulisan adalah OVERWRITE PENUH.** Pastikan seluruh konten dokumen dari baris 1 hingga akhir ada di dalam draf sebelum menulis. Jika tools yang digunakan memiliki batas panjang output, bagi penulisan menjadi beberapa bagian chunk berurutan, tetapi pastikan tidak ada konten yang terlewat di antara chunk.

---

*Issue dibuat oleh: Senior Software Architect & Module Decomposition Specialist*
*Tanggal pembuatan: 2026-05-29*
*Ditujukan kepada: Junior Programmer / AI Model Eksekutor*
