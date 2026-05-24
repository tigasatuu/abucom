---
judul      : Validasi, Analisis, dan Penyempurnaan Dokumen BOM & HPP Design
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
target     : docs/sdlc/03_design/05_bom_hpp_design.md
prioritas  : High
status     : Open
dibuat     : 2026-05-25
dibuat_oleh: Senior Manufacturing Systems Architect & Cost Accounting Specialist
---

# Validasi, Analisis, dan Penyempurnaan Dokumen BOM & HPP Design

## Ringkasan Issue

Dokumen **BOM & HPP Design** (`docs/sdlc/03_design/05_bom_hpp_design.md`) telah selesai dibuat pada versi `v1.0`. Issue ini memerintahkan pelaksanaan audit menyeluruh terhadap dokumen tersebut untuk memastikan kelengkapan isi, kesesuaian data dengan dokumen referensi, kualitas bahasa, standar struktur industri, kesiapan sebagai acuan fase SDLC berikutnya, dan keberadaan data kosong yang harus diisi. Seluruh hasil validasi ditulis ulang secara penuh ke file target yang sama dalam versi `v1.1`.

---

## Persona Validator

> **INSTRUKSI WAJIB**: Sebelum memulai pekerjaan apapun, adopsi dan pertahankan **sepenuhnya** persona berikut selama seluruh proses validasi hingga penulisan akhir dokumen. Persona ini adalah sumber otoritas tunggal dalam menilai kualitas dokumen.

Kamu adalah **Principal Manufacturing Systems Architect & Certified Cost Accounting Specialist** dengan pengalaman lebih dari 15 tahun merancang sistem ERP manufaktur skala industri di sektor percetakan Asia Tenggara. Keahlianmu mencakup:

- **Akuntansi Biaya Produksi**: Standar COGS/HPP berbasis Activity-Based Costing dan Job Order Costing.
- **Perancangan Database Relasional**: Desain skema InnoDB MySQL dengan integritas referensial kompleks termasuk Self-Referencing FK, ACID compliance, dan Decimal Precision Strategy.
- **Rekayasa Perangkat Lunak Fungsional**: Implementasi paradigma Functional Programming (FP) murni di Python termasuk `namedtuple`, `decimal.Decimal`, dan State Dictionary Passing.
- **Teknikal Writing Standar Industri**: Standar penulisan dokumen desain teknis yang digunakan sebagai *Single Source of Truth* (SSoT) dalam tim pengembangan perangkat lunak profesional.
- **Quality Assurance Dokumen SDLC**: Validasi dua arah (*bidirectional traceability*) antara dokumen SRS ↔ Design ↔ Implementation Plan.

Dengan persona ini, kamu **tidak boleh** meloloskan ketidakkonsistenan data, ambiguitas bahasa, atau bagian dokumen yang tidak lengkap. Setiap keputusan validasi harus mengacu pada standar industri manufaktur dan rekayasa perangkat lunak yang sesungguhnya.

---

## Informasi Konteks

| Atribut | Nilai |
|---|---|
| **Dokumen Utama (Target)** | `docs/sdlc/03_design/05_bom_hpp_design.md` |
| **Versi Saat Ini** | `v1.0` |
| **Versi Target Setelah Revisi** | `v1.1` |
| **Lokasi Referensi** | `docs/sdlc/` |
| **Fase SDLC** | Fase 03 — Design (Perancangan Sistem) |

---

## Dokumen Referensi yang Harus Dibaca

Sebelum melakukan validasi apapun, baca seluruh file referensi berikut secara lengkap dari baris pertama hingga terakhir:

| # | Path File Referensi | Prioritas | Keterangan |
|---|---|---|---|
| 1 | `docs/sdlc/03_design/01_database_schema.sql` | **PRIMER** | DDL fisik seluruh tabel: `bom_komposisi`, `barang`, `detail_transaksi`, `limbah_produksi`, `pengeluaran`, `transaksi`, `audit_logs` |
| 2 | `docs/sdlc/03_design/02_erd_database.md` | **PRIMER** | Peta kardinalitas ERD, batasan FK, dan anotasi relasi antar entitas |
| 3 | `docs/sdlc/03_design/03_system_architecture.md` | **PRIMER** | Paradigma FP murni, State Dictionary Passing, dan arsitektur modular sistem |
| 4 | `docs/sdlc/02_analysis/02_software_requirements.md` | **PRIMER** | SRS lengkap: SRS-F-005, SRS-F-007, SRS-F-008, SRS-F-009, SRS-F-010 dan seluruh ketergantungan modul M.2 |
| 5 | `docs/sdlc/03_design/04_cli_interaction_flow.md` | **SEKUNDER** | Alur interaksi CLI menu BOM/HPP: `MENU-M2-001`, `MENU-M2-002`, `MENU-M2-003`, `MENU-M2-004` |

---

## Daftar Tugas Implementasi (Checklist Low-Level)

Ikuti checklist ini secara **berurutan** dari atas ke bawah. Jangan melompati langkah. Tandai setiap tugas sebagai selesai sebelum melanjutkan ke tugas berikutnya.

---

### FASE 0 — Persiapan dan Pembacaan File

- [ ] **[BACA-0.1]** Buka dan baca seluruh konten `docs/sdlc/03_design/05_bom_hpp_design.md` dari baris 1 hingga baris terakhir tanpa pengecualian. Catat versi dokumen saat ini, tanggal, jumlah bagian (section), dan daftar referensi yang sudah ada di dalam dokumen.

- [ ] **[BACA-0.2]** Buka dan baca seluruh konten `docs/sdlc/03_design/01_database_schema.sql`. Fokus identifikasi: definisi kolom tabel `bom_komposisi`, `barang`, `detail_transaksi`, `limbah_produksi`, `pengeluaran`, `transaksi`, dan `audit_logs`. Catat nama kolom, tipe data, constraint, dan komentar kolom yang ada di file ini.

- [ ] **[BACA-0.3]** Buka dan baca seluruh konten `docs/sdlc/03_design/02_erd_database.md`. Fokus identifikasi: seluruh relasi kardinalitas yang melibatkan tabel `bom_komposisi`, `barang`, `detail_transaksi`, `limbah_produksi`, dan `pengeluaran`. Catat setiap batasan FK dan notasi Crow's Foot yang relevan.

- [ ] **[BACA-0.4]** Buka dan baca seluruh konten `docs/sdlc/03_design/03_system_architecture.md`. Fokus identifikasi: aturan paradigma Functional Programming (FP) murni, pola State Dictionary Passing, konvensi penamaan modul Python, dan standar penanganan koneksi database.

- [ ] **[BACA-0.5]** Buka dan baca seluruh konten `docs/sdlc/02_analysis/02_software_requirements.md`. Fokus identifikasi: **SRS-F-005**, **SRS-F-007**, **SRS-F-008**, **SRS-F-009**, **SRS-F-010** secara lengkap mencakup: deskripsi teknis, input, proses/logika bisnis, output, aturan validasi, penanganan exception, ketergantungan, dan catatan implementasi.

- [ ] **[BACA-0.6]** Buka dan baca seluruh konten `docs/sdlc/03_design/04_cli_interaction_flow.md`. Fokus identifikasi: seluruh menu dan alur interaksi yang berkaitan dengan modul M.2 BOM & HPP (menu `MENU-M2-001` hingga `MENU-M2-004`), termasuk urutan prompt, tampilan output, dan respons error di terminal CLI.

---

### FASE 1 — Komparasi Mendalam: Dokumen Utama vs Referensi

> **Tujuan**: Memastikan tidak ada data atau informasi penting dari file referensi yang semestinya ada di dokumen utama tetapi terlewat.

- [ ] **[KOMPARASI-1.1]** Bandingkan DDL tabel `bom_komposisi` di dokumen utama (Bagian 3.2) dengan DDL aktual di `01_database_schema.sql`. Verifikasi: apakah setiap kolom, tipe data, constraint (PRIMARY KEY, UNIQUE, FK, CHECK), dan komentar kolom sudah sesuai 100%? Catat setiap perbedaan.

- [ ] **[KOMPARASI-1.2]** Bandingkan DDL tabel `barang` (Bagian 3.3) di dokumen utama dengan DDL aktual di `01_database_schema.sql`. Khusus perhatikan: apakah **seluruh kolom** yang relevan untuk kalkulasi BOM/HPP sudah ditampilkan? Apakah ada kolom penting (misalnya `harga_grosir`, `harga_mitra`, `min_grosir`, `tipe_barang` nilai enum-nya) yang harusnya ada tetapi tidak disebutkan? Catat setiap perbedaan.

- [ ] **[KOMPARASI-1.3]** Bandingkan ERD Mermaid di dokumen utama (Bagian 3.1) dengan ERD di `02_erd_database.md`. Verifikasi: apakah semua entitas yang berpartisipasi dalam alur BOM/HPP (termasuk `pengguna`, `stock_opname`, `riwayat_harga_supplier`) sudah terwakili dengan tepat? Apakah arah relasi dan notasi kardinalitas sudah konsisten?

- [ ] **[KOMPARASI-1.4]** Bandingkan prinsip FP murni yang diterapkan dalam pseudocode Python (Bagian 8.3) dokumen utama dengan standar arsitektur yang ditetapkan di `03_system_architecture.md`. Verifikasi: apakah pola State Dictionary Passing, konvensi penamaan fungsi, penanganan koneksi database, dan struktur return value sudah selaras?

- [ ] **[KOMPARASI-1.5]** Bandingkan seluruh isi dokumen utama dengan spesifikasi **SRS-F-007** (kalkulasi HPP otomatis). Verifikasi point by point:
  - Apakah formula matematis di Bagian 4 dokumen utama identik dengan formula di SRS?
  - Apakah aturan validasi `kuantitas_pemakaian > 0` sudah tercakup di Bagian 6?
  - Apakah penanganan exception stok minus (alert kuning) sudah terdokumentasi lengkap?
  - Apakah catatan implementasi SRS (`DECIMAL(15,4)`, `decimal.Decimal`) sudah dijabarkan di Bagian 8?

- [ ] **[KOMPARASI-1.6]** Bandingkan seluruh isi dokumen utama dengan spesifikasi **SRS-F-008** (pencatatan limbah produksi). Verifikasi point by point:
  - Apakah alur 4-langkah di Bagian 5.5 dokumen utama selaras dengan logika bisnis SRS-F-008?
  - Apakah field input `transaksi_id`, `bahan_baku_id`, `kuantitas_limbah`, `alasan_kerusakan` semua tercantum?
  - Apakah formula `kerugian_nominal = kuantitas_limbah × harga_beli` ada di dokumen?
  - Apakah relasi ke tabel `pengeluaran` dengan flag `disetujui_pemilik = TRUE` sudah didokumentasikan?

- [ ] **[KOMPARASI-1.7]** Bandingkan dokumen utama dengan spesifikasi **SRS-F-009** (manajemen satuan UoM) dan **SRS-F-010** (sinkronisasi ATK internal). Verifikasi: apakah mekanisme konversi satuan (Rim → Lembar, Liter → Ml) dan mekanisme pemotongan stok ATK untuk produksi internal sudah dijelaskan dengan cukup detail di dokumen utama?

- [ ] **[KOMPARASI-1.8]** Bandingkan Matriks Ketertelusuran di Bagian 9 dokumen utama dengan daftar SRS yang ada di `02_software_requirements.md`. Verifikasi: apakah referensi UC, SRS, WF, dan MENU sudah akurat dan konsisten? Apakah ada SRS yang relevan dengan modul BOM/HPP yang belum masuk matriks?

- [ ] **[KOMPARASI-1.9]** Periksa apakah dokumen utama sudah membahas interaksi dengan tabel `detail_transaksi` secara memadai: apakah ada penjelasan kolom mana yang di-UPDATE saat HPP dikalkulasi (`subtotal`, `harga_jual`)? Bandingkan dengan DDL aktual di `01_database_schema.sql`.

- [ ] **[KOMPARASI-1.10]** Periksa apakah dokumen utama sudah membahas tabel `audit_logs` dalam konteks BOM/HPP: apakah setiap operasi INSERT/UPDATE formula BOM dan pemotongan stok bahan harus direkam di `audit_logs`? Bandingkan dengan `03_system_architecture.md` mengenai standar audit trail.

---

### FASE 2 — Validasi Kelengkapan Isi Dokumen

> **Tujuan**: Memastikan dokumen hanya berisi informasi yang relevan dengan domain BOM & HPP, tidak berlebihan, tidak kurang.

- [ ] **[KELENGKAPAN-2.1]** Periksa Bagian 2 (Konsep Dasar). Validasi: apakah penjelasan konsep BOM dan HPP sudah cukup untuk dipahami oleh junior programmer yang belum pernah bekerja di industri percetakan? Apakah ada konsep kritis (misalnya perbedaan antara HPP dan harga jual, kapan HPP dihitung vs kapan struk dibuat) yang belum dijelaskan?

- [ ] **[KELENGKAPAN-2.2]** Periksa Bagian 3 (Skema Database). Validasi: apakah penjelasan constraint `ON DELETE CASCADE` vs `ON DELETE RESTRICT` sudah cukup kontekstual? Apakah penjelasan unique constraint komposit (`uq_bom_komposisi_induk_bahan`) sudah mencantumkan implikasi bisnis jika constraint ini dilanggar?

- [ ] **[KELENGKAPAN-2.3]** Periksa Bagian 4 (Formula dan Logika Kalkulasi). Validasi: apakah sudah ada contoh kalkulasi numerik yang mencakup skenario `Retail_ATK` yang diambil untuk produksi? Apakah semua formula menggunakan notasi LaTeX yang konsisten dan tidak ambigu?

- [ ] **[KELENGKAPAN-2.4]** Periksa Bagian 5 (Alur Data dan Proses). Validasi: apakah kelima alur (BOM entry, kalkulasi HPP, pemotongan stok, pencatatan limbah, sinkronisasi ATK) sudah memiliki penjelasan prakondisi, aktor, dan urutan langkah yang jelas? Apakah ada alur yang masih terlalu abstrak dan perlu dijabarkan lebih detail?

- [ ] **[KELENGKAPAN-2.5]** Periksa Bagian 6 (Aturan Validasi dan Exception). Validasi: apakah semua kode error (`ERR-VAL-007`, `ERR-VAL-008`, `ERR-STOCK-010`, `ERR-DB-007`) sudah konsisten dengan kode error di SRS? Apakah ada kasus error penting yang belum dicantumkan (misalnya: error jika `barang_induk_id` tidak memiliki BOM sama sekali saat produksi selesai)?

- [ ] **[KELENGKAPAN-2.6]** Periksa Bagian 7 (Integrasi Lintas Modul). Validasi: apakah semua 6 integrasi (M.1, M.5, M.1 Margin, M.6, M.7, M.9) sudah menjelaskan mekanisme teknis integrasi secara cukup? Apakah referensi nomor SRS di setiap integrasi sudah akurat?

- [ ] **[KELENGKAPAN-2.7]** Periksa Bagian 8 (Spesifikasi Implementasi Teknis). Validasi: apakah pseudocode Python yang ada sudah mencakup semua fungsi kritis (hitung_biaya_komponen, hitung_hpp_produk, proses_pemotongan_stok, proses_limbah_produksi)? Apakah ada fungsi penting yang belum ada pseudocode-nya (misalnya: fungsi pendaftaran BOM baru, fungsi sinkronisasi ATK internal)?

- [ ] **[KELENGKAPAN-2.8]** Periksa Bagian 9 (Matriks Ketertelusuran). Validasi: apakah semua use case yang relevan sudah masuk ke matriks? Apakah kolom "CLI Menu Terkait" sudah terisi dengan nama menu yang akurat sesuai `04_cli_interaction_flow.md`?

- [ ] **[KELENGKAPAN-2.9]** Periksa Bagian 10 (Glosarium). Validasi: apakah semua istilah teknis penting yang digunakan di dalam dokumen sudah terdefinisi di glosarium? Apakah ada istilah yang digunakan di dalam dokumen tetapi tidak terdaftar di glosarium (misalnya: OPEX, ACID, InnoDB, pure function, namedtuple, ROUND_HALF_UP)?

- [ ] **[KELENGKAPAN-2.10]** Periksa apakah dokumen memiliki penjelasan tentang **trigger timing** kalkulasi HPP yang sangat spesifik: HPP dihitung bukan saat pembuatan nota, melainkan saat status antrian berubah menjadi `'Selesai'`. Pastikan ini dijelaskan cukup tegas dan tidak ambigu di dokumen.

---

### FASE 3 — Validasi Standar Struktur Dokumen Industri

> **Tujuan**: Memastikan dokumen memenuhi standar struktur dokumen teknis industri perangkat lunak yang sesungguhnya.

- [ ] **[STRUKTUR-3.1]** Validasi **Front Matter (Header YAML)**. Periksa: apakah metadata dokumen (judul, proyek, target, prioritas, status, dibuat, penyusun) sudah lengkap dan informatif? Apakah status dokumen (`Final`) sudah tepat mengingat dokumen ini masih dalam tahap validasi?

- [ ] **[STRUKTUR-3.2]** Validasi **Riwayat Perubahan Dokumen**. Periksa: apakah tabel riwayat sudah ada? Apakah sudah mencantumkan versi, tanggal, deskripsi perubahan, dan nama penyusun? Pastikan kolom dan format tabel konsisten dengan dokumen SDLC lainnya.

- [ ] **[STRUKTUR-3.3]** Validasi **Bagian 1 — Informasi Dokumen**. Periksa kelengkapan sub-bagian:
  - 1.1 Tujuan Dokumen: sudah ada ✓/✗
  - 1.2 Cakupan Dokumen: sudah ada ✓/✗
  - 1.3 Posisi Dokumen dalam SDLC: sudah ada (termasuk diagram ASCII) ✓/✗
  - 1.4 Hubungan dengan Dokumen Lain (Input & Output): sudah ada ✓/✗
  - 1.5 Audiens Target: sudah ada ✓/✗
  - 1.6 Definisi, Akronim, dan Singkatan: sudah ada ✓/✗
  - Apakah ada sub-bagian standar yang belum ada dan perlu ditambahkan?

- [ ] **[STRUKTUR-3.4]** Validasi **penomoran bagian dan sub-bagian**. Periksa: apakah seluruh heading menggunakan format penomoran yang konsisten (Bagian 1, 1.1, 1.2, dst.)? Apakah tidak ada gap nomor atau duplikat nomor?

- [ ] **[STRUKTUR-3.5]** Validasi **konsistensi format tabel**. Periksa: apakah semua tabel di dokumen menggunakan format header dan alignment yang konsisten? Apakah tabel validasi (Bagian 6.1) dan tabel error (Bagian 6.2) sudah mengikuti format standar dokumentasi teknis industri?

- [ ] **[STRUKTUR-3.6]** Validasi **konsistensi format kode**. Periksa: apakah semua blok kode (SQL DDL, Python pseudocode, Mermaid diagram) menggunakan syntax highlighting yang tepat? Apakah kode SQL sudah menggunakan konvensi `UPPER CASE` untuk keyword SQL?

- [ ] **[STRUKTUR-3.7]** Validasi **kelengkapan diagram**. Periksa apakah sudah ada:
  - ERD Mermaid fokus BOM/HPP ✓/✗
  - Flowchart end-to-end ✓/✗
  - Sequence Diagram kalkulasi HPP ✓/✗
  - Diagram integrasi lintas modul ✓/✗
  - Diagram klasifikasi barang ✓/✗
  - Apakah ada diagram tambahan yang lazim ada di dokumen desain industri yang belum ada?

- [ ] **[STRUKTUR-3.8]** Validasi **Matriks Ketertelusuran (Traceability Matrix)**. Ini adalah komponen wajib di setiap dokumen desain teknis industri yang serius. Periksa: apakah kolom-kolom matriks sudah cukup (ID Use Case, Kode SRS, Workflow, CLI Menu, Bagian Dokumen)? Apakah semua baris sudah terisi tanpa ada sel yang kosong?

- [ ] **[STRUKTUR-3.9]** Validasi **Glosarium**. Periksa: apakah glosarium ditempatkan di bagian akhir dokumen (posisi lazim di dokumen teknis industri)? Apakah format definisi konsisten (istilah dicetak tebal, diikuti tanda titik dua, diikuti definisi)?

- [ ] **[STRUKTUR-3.10]** Periksa apakah dokumen memiliki **separator horizontal** (`---`) yang konsisten di antara bagian utama untuk memudahkan navigasi pembaca.

---

### FASE 4 — Validasi Kesiapan sebagai Referensi Fase SDLC Berikutnya

> **Tujuan**: Memastikan dokumen ini layak menjadi input utama bagi Fase 04 Implementation dan Fase 05 Testing.

- [ ] **[REFERENSI-4.1]** Validasi kesiapan untuk **Fase 04 Implementation** (penulisan kode `logic/bom_hpp.py`). Periksa: apakah seorang junior programmer atau AI coding agent dapat langsung menulis kode Python berdasarkan dokumen ini tanpa perlu membuka dokumen lain? Identifikasi bagian yang masih terlalu abstrak dan perlu dijabarkan lebih konkret (misalnya: signature fungsi, parameter, return value, tipe data Python yang digunakan).

- [ ] **[REFERENSI-4.2]** Validasi kesiapan untuk **Fase 05 Testing** (penulisan test cases). Periksa: apakah ada cukup data numerik konkret (contoh kalkulasi dengan angka nyata) agar tim QA dapat membuat test case tanpa menebak-nebak nilai yang diharapkan? Apakah semua skenario edge case (stok minus, BOM kosong, bahan tidak terdaftar) sudah terdokumentasi?

- [ ] **[REFERENSI-4.3]** Validasi apakah **path file modul** sudah disebutkan secara eksplisit: `logic/bom_hpp.py`. Verifikasi apakah path ini konsisten dengan arsitektur proyek yang didefinisikan di `03_system_architecture.md`.

- [ ] **[REFERENSI-4.4]** Validasi apakah semua **dependency library Python** yang digunakan dalam implementasi BOM/HPP sudah disebutkan di dokumen: `decimal`, `collections.namedtuple`, `mysql-connector-python`. Apakah versi library konsisten dengan yang ada di SRS (Bagian 2.4 SRS)?

- [ ] **[REFERENSI-4.5]** Validasi apakah ada **contoh query SQL** yang cukup untuk panduan implementasi: SELECT dari `bom_komposisi`, UPDATE `detail_transaksi`, UPDATE `barang` (pemotongan stok), INSERT `limbah_produksi`, INSERT `pengeluaran`. Pastikan semua query menggunakan parameterized query (`%s`) sesuai standar keamanan.

- [ ] **[REFERENSI-4.6]** Validasi apakah dokumen sudah menjelaskan **mekanisme `FOR UPDATE` locking** dalam konteks transaksi InnoDB saat pemotongan stok untuk mencegah race condition pada sistem multi-kasir.

---

### FASE 5 — Validasi Kualitas Bahasa Indonesia

> **Tujuan**: Memastikan bahasa yang digunakan natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau LLM berbiaya rendah.

- [ ] **[BAHASA-5.1]** Baca seluruh dokumen sekali lagi dari awal dengan fokus pada kualitas bahasa. Identifikasi kalimat atau paragraf yang:
  - Menggunakan kalimat pasif berlebihan yang menyamarkan subjek pelaku.
  - Menggunakan istilah teknis tanpa penjelasan di konteks penggunaannya.
  - Mengandung ambigu tentang subjek (siapa yang melakukan apa).
  - Terlalu panjang dan bisa dipecah menjadi kalimat lebih pendek.

- [ ] **[BAHASA-5.2]** Validasi konsistensi penggunaan terminologi. Pastikan istilah yang sama selalu mengacu pada konsep yang sama di seluruh dokumen:
  - "Bahan Baku" vs "bahan_baku" vs "komponen" — pilih satu terminologi dan konsisten.
  - "Barang Induk" vs "produk jadi" vs "barang kustom" — pastikan tidak ambigu.
  - "pemotongan stok" vs "pengurangan stok" vs "debit stok" — pilih terminologi resmi.

- [ ] **[BAHASA-5.3]** Validasi kejelasan instruksi prosedural di setiap alur (Bagian 5). Pastikan setiap langkah menggunakan format yang jelas: nomor urut, subjek yang jelas (Sistem/Staf/Pemilik), kata kerja aktif, dan objek yang spesifik. Contoh format yang baik: *"3. Sistem memverifikasi kombinasi (`barang_induk_id`, `bahan_baku_id`) tidak duplikat melalui constraint `uq_bom_komposisi_induk_bahan`."*

- [ ] **[BAHASA-5.4]** Validasi apakah kalimat pada bagian **Aturan Validasi** (Bagian 6.1) menggunakan kata modal yang tepat: "HARUS", "WAJIB", "TIDAK BOLEH", "DILARANG" secara konsisten sesuai tingkat kepentingannya. Hindari kata "sebaiknya" atau "disarankan" untuk aturan yang bersifat wajib.

- [ ] **[BAHASA-5.5]** Periksa semua **pesan error** di tabel kode error (Bagian 6.2). Pastikan:
  - Pesan error ditulis dalam Bahasa Indonesia yang mudah dipahami staf toko non-teknis.
  - Pesan error bersifat informatif (menjelaskan apa yang salah dan apa yang harus dilakukan).
  - Format kode error konsisten (`ERR-[KATEGORI]-[NOMOR]`).

---

### FASE 6 — Validasi Kelengkapan dan Pengisian Data Kosong

> **Tujuan**: Mengidentifikasi dan mengisi semua data yang kosong, belum tersedia, atau menggunakan placeholder.

- [ ] **[DATA-6.1]** Scan seluruh dokumen untuk mencari placeholder yang belum diisi, ditandai dengan pola seperti: `[PLACEHOLDER]`, `[TBD]`, `[TODO]`, `N/A`, `—`, atau sel tabel yang kosong. Catat lokasi (bagian dan nomor baris) setiap placeholder yang ditemukan.

- [ ] **[DATA-6.2]** Untuk setiap placeholder yang ditemukan di [DATA-6.1], isi dengan data yang akurat, relevan, dan sesuai konteks dokumen ini. Data harus konsisten dengan informasi yang ada di dokumen referensi. Jangan mengosongkan data apapun.

- [ ] **[DATA-6.3]** Periksa apakah tabel **Matriks Ketertelusuran** (Bagian 9) memiliki sel kosong. Jika ada, isi berdasarkan referensi silang dengan SRS dan `04_cli_interaction_flow.md`.

- [ ] **[DATA-6.4]** Periksa apakah Sequence Diagram di Bagian 5.3 mencantumkan **nama tabel database yang tepat** (bukan nama generik). Verifikasi nama tabel dengan `01_database_schema.sql`.

- [ ] **[DATA-6.5]** Periksa apakah pseudocode Python di Bagian 8.3 mencantumkan **nama kolom database yang tepat** sesuai DDL aktual (misalnya: nama kolom di `detail_transaksi` yang di-UPDATE saat HPP dikalkulasi). Isi jika ada yang generik atau kosong.

- [ ] **[DATA-6.6]** Periksa apakah dokumen sudah menyebutkan **nama database** dan **nama schema** yang digunakan oleh sistem AbuCom. Jika belum, cari di `01_database_schema.sql` dan tambahkan di bagian yang relevan.

- [ ] **[DATA-6.7]** Periksa apakah ada **nilai numerik default** yang perlu disebutkan (misalnya: nilai default `cabang_id = 1` untuk sistem single-branch, nilai `DECIMAL(15,4)` presisi tetap). Pastikan semua nilai default ini eksplisit tertulis di dokumen.

---

### FASE 7 — Penulisan Ulang Dokumen Final (Overwrite)

> **PERINGATAN KRITIS**: Fase ini adalah fase paling krusial. Ikuti setiap instruksi dengan presisi absolut tanpa pengecualian.

- [ ] **[TULIS-7.1]** Sebelum menulis, buat **daftar kompilasi seluruh temuan** dari Fase 1 hingga Fase 6 secara terstruktur:
  - Daftar ketidaksesuaian data dengan referensi beserta koreksinya.
  - Daftar informasi yang hilang (missing) beserta konten tambahannya.
  - Daftar konten yang tidak relevan dan perlu dihapus.
  - Daftar masalah bahasa beserta perbaikannya.
  - Daftar data kosong beserta isian yang tepat.

- [ ] **[TULIS-7.2]** **UPDATE versi dokumen** dari `v1.0` menjadi `v1.1`. Perbarui baris versi di:
  - Header YAML front matter: `versi: v1.1` (jika ada) atau pastikan tercantum dengan jelas.
  - Diagram ASCII posisi dokumen: ganti `BOM & HPP Design v1.0` menjadi `BOM & HPP Design v1.1`.
  - Tabel riwayat perubahan: tambahkan baris baru untuk `v1.1` dengan tanggal hari ini, deskripsi perubahan lengkap (sebutkan semua perbaikan yang dilakukan), dan nama penyusun `Principal Manufacturing Systems Architect & Certified Cost Accounting Specialist`.

- [ ] **[TULIS-7.3]** Tulis ulang **seluruh dokumen** menggunakan tool `write_file` atau `overwrite file` ke path target `docs/sdlc/03_design/05_bom_hpp_design.md`. Pastikan:
  - Tulis dari **baris 1 hingga baris terakhir** tanpa pengecualian.
  - **DILARANG KERAS** memotong, meringkas, atau menghilangkan bagian manapun dari dokumen.
  - **DILARANG KERAS** menggunakan frasa seperti `[... konten sebelumnya tetap sama ...]` atau `[... dst ...]`.
  - Setiap kata, kalimat, tabel, blok kode, dan diagram harus ditulis ulang secara penuh dan eksplisit.
  - Dokumen yang dituliskan harus **lebih lengkap dan lebih baik** dari dokumen `v1.0` sebelumnya.

- [ ] **[TULIS-7.4]** Setelah penulisan selesai, lakukan **verifikasi panjang dokumen**. Dokumen `v1.1` harus memiliki **jumlah baris yang sama atau lebih banyak** dari dokumen `v1.0` (590 baris). Jika hasilnya lebih sedikit dari 590 baris, itu berarti ada konten yang terpotong — batalkan dan ulangi penulisan.

- [ ] **[TULIS-7.5]** Jika dalam proses validasi Fase 1–6 ditemukan kebutuhan untuk **merujuk file referensi tambahan** yang belum tercantum di Bagian 1.4 dokumen utama, tambahkan referensi baru tersebut di **bagian akhir baris paling bawah** dokumen `v1.1` dengan format:

  ```markdown
  ---
  
  ## Referensi Tambahan (Ditambahkan saat Revisi v1.1)
  
  | # | Path File | Keterangan |
  |---|---|---|
  | 1 | `[path/ke/file/referensi/baru]` | [Alasan ditambahkan] |
  ```

- [ ] **[TULIS-7.6]** Lakukan **pembacaan final** terhadap dokumen `v1.1` yang baru ditulis. Verifikasi:
  - Semua hasil temuan dari Fase 1–6 sudah terimplementasi.
  - Versi dokumen sudah berubah menjadi `v1.1` di semua tempat yang relevan.
  - Tidak ada teks yang terpotong di tengah kalimat atau blok kode.
  - Semua tabel menutup dengan benar (tidak ada tabel yang tidak memiliki baris penutup).
  - Semua blok kode (````` ``` `````) membuka dan menutup dengan benar.
  - Semua diagram Mermaid valid secara sintaks.

---

## Kriteria Keberhasilan (Definition of Done)

Issue ini dianggap **selesai** jika dan hanya jika seluruh kondisi berikut terpenuhi:

| # | Kriteria | Verifikasi |
|---|---|---|
| 1 | Semua 6 fase checklist telah diselesaikan tanpa ada tugas yang dilewati | Semua `[ ]` berubah menjadi `[x]` |
| 2 | Dokumen `05_bom_hpp_design.md` versi `v1.1` berhasil dituliskan ke path target | File berhasil di-overwrite |
| 3 | Jumlah baris dokumen `v1.1` ≥ 590 baris (tidak ada konten yang terpotong) | Verifikasi jumlah baris |
| 4 | Tabel riwayat perubahan mencantumkan entri baru untuk versi `v1.1` | Baris baru di tabel riwayat |
| 5 | Semua data kosong/placeholder sudah terisi dengan data yang akurat | Tidak ada cell kosong di dokumen |
| 6 | Seluruh konten konsisten dengan dokumen referensi primer | Tidak ada kontradiksi data |
| 7 | Bahasa Indonesia yang digunakan natural, tidak ambigu, dan mudah dipahami | Tidak ada kalimat yang membingungkan |
| 8 | Jika ada referensi file baru, sudah ditambahkan di bagian akhir dokumen | Bagian referensi tambahan ada |

---

## Batasan dan Larangan Keras

> Seluruh poin berikut adalah **larangan mutlak** yang tidak boleh dilanggar:

1. **DILARANG** menulis ulang dokumen secara parsial (hanya bagian tertentu). Dokumen harus ditulis ulang seluruhnya dari baris 1.
2. **DILARANG** menggunakan frasa seperti `[konten tetap]`, `[dst]`, `[...]`, atau sejenisnya yang mengindikasikan pemotongan konten.
3. **DILARANG** menambahkan konten yang tidak relevan dengan domain BOM & HPP (misalnya konten tentang modul M.1 Transaksi, M.4 Payroll, atau M.3 PPOB secara mendalam).
4. **DILARANG** mengubah fakta atau spesifikasi teknis yang sudah benar di dokumen `v1.0` tanpa ada bukti dari dokumen referensi.
5. **DILARANG** melewati fase pembacaan dokumen referensi (Fase 0). Pembacaan referensi adalah prasyarat mutlak.
6. **DILARANG** mengganti diagram Mermaid yang sudah ada dengan versi yang lebih sederhana atau tidak lengkap.
7. **DILARANG** menghapus bagian glosarium, matriks ketertelusuran, atau riwayat perubahan dokumen.

---

## Catatan Teknis Tambahan untuk Implementer

> Poin-poin berikut adalah perhatian teknis spesifik yang harus diperhatikan berdasarkan karakteristik unik dokumen BOM & HPP Design ini:

### Tentang Presisi Desimal
Dokumen ini berkaitan erat dengan kalkulasi keuangan dan stok bahan baku yang menggunakan presisi `DECIMAL(15,4)`. Setiap kali Anda menyebut nilai numerik dalam dokumen (contoh kalkulasi, nilai default, threshold), pastikan nilai tersebut selalu ditulis dengan **4 angka di belakang koma** (contoh: `Rp 4.750,0000` bukan `Rp 4.750`).

### Tentang Penomoran Kode Error
Kode error di dokumen ini menggunakan sistem `ERR-[KATEGORI]-[NOMOR]`. Pastikan setiap kode error yang Anda temukan atau tambahkan konsisten dengan kode yang ada di SRS. Jangan membuat kode error baru yang tidak ada di SRS kecuali kode tersebut memang diperlukan untuk skenario yang belum dicakup SRS.

### Tentang Terminologi Tipe Barang
Nilai enum `tipe_barang` di database harus ditulis sesuai DDL aktual di `01_database_schema.sql`. Pastikan tidak ada inkonsistensi penulisan antara `'Bahan_Baku'`, `'Retail_ATK'`, dan `'Barang'` (dengan underscore sesuai nilai enum di database).

### Tentang ACID dan Transaksi InnoDB
Setiap alur yang melibatkan operasi tulis ke database (`INSERT`, `UPDATE`) harus selalu disebutkan dalam konteks transaksi InnoDB (`START TRANSACTION ... COMMIT / ROLLBACK`). Ini adalah invariant arsitektur yang tidak boleh diabaikan di dokumen ini.

### Tentang Trigger Waktu Kalkulasi HPP
Poin kritis yang sering disalahpahami: HPP **tidak dikalkulasi saat pembuatan nota/struk**, melainkan **saat staf mengubah status antrian kerja menjadi `'Selesai'`**. Pastikan poin ini dijelaskan dengan tegas di minimal dua tempat yang berbeda dalam dokumen (termasuk di Bagian 1 Tujuan/Cakupan dan di Bagian 5 Alur Proses).

---

*Issue ini dibuat oleh: Senior Manufacturing Systems Architect & Cost Accounting Specialist*
*Tanggal pembuatan issue: 2026-05-25*
*Target penyelesaian: Sesegera mungkin setelah issue di-assign*
