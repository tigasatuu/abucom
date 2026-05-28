# Validasi, Analisis & Penyempurnaan Dokumen Use Case Diagram

**Tanggal Dibuat** : 2026-05-28
**Prioritas**      : High
**Status**         : Open
**Assignee**       : Junior Programmer / AI Agent
**Dokumen Utama**  : `docs/sdlc/02_analysis/03_use_case_diagram.md`
**Lokasi Referensi**: `docs/sdlc/`

---

## 1. Latar Belakang

Dokumen **Use Case Diagram (UCD)** `03_use_case_diagram.md` adalah artefak ketiga dan penutup Fase 02 Analysis dalam siklus SDLC AbuCom. Dokumen ini menjadi **jembatan kritis** antara kebutuhan bisnis (BRD) dan kebutuhan teknis (SRS) menuju fase perancangan sistem (Fase 03 Design). Kualitas, kelengkapan, dan presisi dokumen ini secara langsung menentukan kelancaran pembuatan:

- System Design Document (SDD)
- Entity-Relationship Diagram (ERD) & Skema Database
- Test Plan & Test Cases (UAT & Integrasi)

Sebelum dokumen ini digunakan sebagai input pada fase berikutnya, **wajib dilakukan validasi menyeluruh** yang mencakup kelengkapan konten, akurasi komparasi referensi, ketepatan struktur UML, konsistensi bahasa, dan kesiapan sebagai dokumen industri profesional.

---

## 2. Persona Eksekutor

Sebelum memulai implementasi, **adopsi dan pertahankan persona berikut secara ketat sepanjang seluruh pekerjaan ini**:

> **Persona**: *Senior UML Modeling Specialist & Systems Analyst* dengan keahlian mendalam di bidang:
> - **UML 2.x Standards** (OMG Unified Modeling Language Specification): Paham total relasi `<<include>>`, `<<extend>>`, generalisasi aktor, system boundary, dan penulisan use case naratif berstandar IEEE 830.
> - **SDLC & Requirement Engineering**: Berpengalaman memvalidasi artefak analisis (BRD, SRS, UCD, DFD) dalam proyek perangkat lunak skala menengah.
> - **Domain Bisnis Percetakan & Retail**: Memahami alur operasional toko percetakan (kasir, produksi, gudang, SDM, keuangan).
> - **Standar Penulisan Bahasa Indonesia Teknis**: Mampu menilai keterbacaan, ketepatan, dan kejelasan kalimat teknis berbahasa Indonesia untuk konsumsi junior programmer dan AI agent.
> - **Quality Assurance Dokumen Industri**: Berpengalaman melakukan peer review dokumen analisis yang akan dijadikan artefak hukum proyek.

**Tanggung jawab utama persona ini**: Memastikan dokumen UCD yang dihasilkan adalah dokumen yang **tidak akan pernah dipertanyakan ulang kualitasnya** dan **siap digunakan sebagai input tanpa interupsi** pada fase SDLC selanjutnya.

---

## 3. Dokumen Utama & Referensi

### 3.1. Dokumen Utama (Target Validasi & Penulisan Ulang)

| Atribut | Detail |
|---|---|
| **File Target** | `docs/sdlc/02_analysis/03_use_case_diagram.md` |
| **Versi Saat Ini** | v1.1 |
| **Status Saat Ini** | Completed |
| **Jumlah Baris** | ±1.547 baris |
| **Konten Utama** | 8 aktor internal, 4 aktor eksternal, 44 use case, 11 diagram Mermaid, spesifikasi naratif, relasi include/extend, matriks traceability, glosarium |

### 3.2. File Referensi Wajib Dibaca

Baca seluruh file referensi berikut secara menyeluruh **sebelum memulai analisis**:

| # | File Referensi | Path Lengkap | Relevansi untuk UCD |
|---|---|---|---|
| R-01 | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | Sumber pemetaan aktor, hak akses RBAC, kebutuhan bisnis fungsional (BR-F-01 s.d. BR-F-40), dan regulasi bisnis |
| R-02 | `02_software_requirements.md` | `docs/sdlc/02_analysis/02_software_requirements.md` | Sumber spesifikasi teknis fungsional (SRS-F-001 s.d. SRS-F-040), kode error terstandar, dependensi include/extend, dan ERD awal |
| R-03 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Profil 19 stakeholder dan pembagian grid pengaruh/kepentingan |
| R-04 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Visi misi proyek, cakupan 10 modul sistem, dan estimasi tim |
| R-05 | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Rincian inovasi terintegrasi yang mempengaruhi pembagian use case operasional |

---

## 4. Lingkup Validasi

Validasi mencakup **10 dimensi kualitas** berikut secara berurutan:

| Dimensi | Kode | Deskripsi Singkat |
|---|---|---|
| Kelengkapan Komparasi Referensi | D-01 | Semua data referensi tercermin dalam UCD |
| Relevansi & Kebersihan Konten | D-02 | UCD tidak berisi konten di luar scope-nya |
| Standar Struktur Dokumen | D-03 | Struktur sesuai standar industri UCD |
| Kesiapan sebagai Input SDLC Lanjutan | D-04 | Layak digunakan oleh fase design & testing |
| Kualitas Bahasa Indonesia | D-05 | Natural, tidak ambigu, mudah dipahami |
| Kesiapan Eksekusi Tanpa Interupsi | D-06 | Tidak ada celah yang akan menghambat pekerjaan lanjutan |
| Pengisian Data Kosong | D-07 | Semua field yang kosong diisi dengan data valid |
| Validasi Diagram Mermaid | D-08 | Sintaks dan konten 11 diagram valid dan konsisten |
| Konsistensi ID & Traceability | D-09 | Semua ID UC, BRD, SRS konsisten antar bagian |
| Validasi Spesifikasi Naratif Use Case | D-10 | Setiap narasi 44 UC lengkap dan tidak truncated |

---

## 5. Instruksi Implementasi Langkah demi Langkah

> **PERINGATAN MUTLAK**: Eksekusi setiap langkah **secara berurutan**. Jangan melompat atau melewatkan langkah mana pun. Tandai setiap checklist `[ ]` menjadi `[x]` setelah benar-benar selesai dikerjakan.

---

### FASE 0 — PERSIAPAN LINGKUNGAN & PEMBACAAN AWAL

- [ ] **[0.1]** Buka dan **baca tuntas seluruh isi** file dokumen utama: `docs/sdlc/02_analysis/03_use_case_diagram.md` dari baris pertama hingga baris terakhir (1.547 baris). Jangan skip atau asumsikan konten yang belum dibaca.
- [ ] **[0.2]** Buka dan **baca tuntas seluruh isi** file R-01: `docs/sdlc/02_analysis/01_business_requirements.md`.
- [ ] **[0.3]** Buka dan **baca tuntas seluruh isi** file R-02: `docs/sdlc/02_analysis/02_software_requirements.md`.
- [ ] **[0.4]** Buka dan **baca tuntas seluruh isi** file R-03: `docs/sdlc/01_planning/03_stakeholder_register.md`.
- [ ] **[0.5]** Buka dan **baca tuntas seluruh isi** file R-04: `docs/sdlc/01_planning/01_project_charter.md`.
- [ ] **[0.6]** Buka dan **baca tuntas seluruh isi** file R-05: `docs/sdlc/01_planning/05_innovation_proposal.md`.
- [ ] **[0.7]** Setelah semua file dibaca, buat catatan mental atau scratchpad sementara berisi: total aktor yang ditemukan di BRD, total use case yang terderivasi dari SRS, daftar inovasi di Innovation Proposal yang belum terpetakan di UCD, dan profil stakeholder yang belum tercakup di seksi audiens target.

---

### FASE 1 — DIMENSI D-01: KELENGKAPAN KOMPARASI REFERENSI

**Tujuan**: Memastikan **setiap data, kebutuhan, dan entitas** di file referensi sudah terpetakan secara tepat di dalam dokumen UCD.

#### 1.1. Komparasi Aktor Internal vs BRD
- [ ] **[1.1.1]** Buka dokumen utama Seksi 2.1 (Aktor Internal). Buka R-01 (BRD). Bandingkan: apakah **semua 8 peran pengguna** yang disebutkan di BRD (pemilik, kepala_percetakan, pramuniaga, kasir, desainer, produksi_cetak, fotocopy_print, gudang) sudah terdaftar di tabel aktor internal UCD dengan deskripsi dan hak akses yang **akurat dan konsisten** dengan BRD?
- [ ] **[1.1.2]** Verifikasi apakah ada **peran aktor baru** yang disebutkan di BRD atau Stakeholder Register (R-03) yang **belum** tercantum di UCD. Jika ada, catat sebagai temuan.
- [ ] **[1.1.3]** Pastikan **hak akses utama** setiap aktor di tabel UCD sudah mencerminkan pembatasan RBAC yang tersebut di BRD secara akurat.

#### 1.2. Komparasi Aktor Eksternal vs BRD
- [ ] **[1.2.1]** Buka Seksi 2.2 (Aktor Eksternal). Bandingkan dengan BRD: apakah keempat aktor eksternal (Pelanggan, Vendor/Supplier, Institusi Perbankan, Kerabat & Keluarga) sudah terdefinisi dengan **hubungan sistem yang tepat dan lengkap**?
- [ ] **[1.2.2]** Periksa apakah BRD menyebutkan aktor eksternal lain (misal: penyedia platform PPOB, operator telekomunikasi) yang belum tercantum di UCD. Jika ada, catat sebagai temuan.

#### 1.3. Komparasi 44 Use Case vs BRD (BR-F-01 s.d. BR-F-40)
- [ ] **[1.3.1]** Buka Seksi 3.2 (Master Daftar Use Case). Untuk setiap baris di tabel UC, cek kolom "Derivasi BRD" dan verifikasi bahwa ID BR-F yang tertulis **benar-benar ada dan sesuai** dengan konten di R-01.
- [ ] **[1.3.2]** Hitung total BR-F di BRD. Pastikan seluruh 40 BR-F (BR-F-01 hingga BR-F-40) sudah terpetakan ke minimal satu UC. Jika ada BR-F yang belum terpetakan, catat sebagai celah kritis.
- [ ] **[1.3.3]** Periksa apakah 4 Use Case Dasar Operasional (UC-041 Login, UC-042 Logout, UC-043 Dashboard, UC-044 Ubah Password) sudah memiliki justifikasi yang memadai meskipun tidak bersumber dari BR-F tertentu.

#### 1.4. Komparasi 44 Use Case vs SRS (SRS-F-001 s.d. SRS-F-040)
- [ ] **[1.4.1]** Buka Seksi 3.2. Untuk setiap baris UC, cek kolom "Derivasi SRS" dan verifikasi bahwa ID SRS-F yang tertulis **benar-benar ada dan nama teknisnya sesuai** dengan konten di R-02.
- [ ] **[1.4.2]** Pastikan seluruh 40 SRS-F (SRS-F-001 hingga SRS-F-040) sudah terkomputasi di Seksi 7.2 (Matriks UC ↔ SRS) dengan status "Terpenuhi". Jika ada yang belum, catat sebagai temuan.
- [ ] **[1.4.3]** Periksa apakah ada **kode error** (ERR-DB-001, ERR-STOCK-010, ERR-AUTH-011, dll.) di spesifikasi naratif UC yang **tidak sesuai** dengan katalog kode error resmi di SRS v1.1. Jika ditemukan inkonsistensi kode error, catat dan koreksi.

#### 1.5. Komparasi Innovation Proposal (R-05)
- [ ] **[1.5.1]** Baca daftar 43+ inovasi di R-05. Untuk setiap inovasi, verifikasi apakah sudah terpetakan ke minimal satu use case di UCD. Buat daftar inovasi yang belum terpetakan.
- [ ] **[1.5.2]** Jika ada inovasi yang seharusnya menjadi bagian dari use case fungsional tetapi belum terwakili, catat sebagai temuan untuk diintegrasikan.

---

### FASE 2 — DIMENSI D-02: RELEVANSI & KEBERSIHAN KONTEN

**Tujuan**: Memastikan UCD **hanya berisi konten yang merupakan bagian native dari dokumen Use Case Diagram** dan tidak memuat data yang seharusnya ada di dokumen lain (SRS, SDD, ERD, dll.).

- [ ] **[2.1]** Periksa apakah ada bagian dalam UCD yang memuat **detail implementasi teknis tingkat kode** (contoh: nama fungsi Python, nama tabel MySQL secara spesifik) yang seharusnya hanya ada di SDD atau SRS, bukan di UCD. Evaluasi apakah detail teknis tersebut perlu dihapus, dipersingkat, atau cukup dipertahankan sebagai konteks batas sistem.

  > *Catatan*: UCD **boleh** menyebutkan nama tabel (misal: tabel `transaksi`) sebagai referensi batas sistem (system boundary), namun **tidak boleh** mendeskripsikan skema DDL atau query SQL secara mendetail.

- [ ] **[2.2]** Pastikan bagian Spesifikasi Naratif (Seksi 5) hanya memuat konten yang relevan untuk format Use Case Specification standar: UC-ID, Nama, Derivasi, Modul, Prioritas, Aktor Primer, Aktor Sekunder, Deskripsi Singkat, Prakondisi, Pemicu, Alur Utama, Alur Alternatif, Alur Pengecualian, Pasca-Kondisi, Aturan Bisnis Terkait, dan Catatan Khusus. Jika ada atribut yang tidak relevan atau berbeda dari konvensi, evaluasi dan koreksi.
- [ ] **[2.3]** Periksa apakah Seksi 6 (Relasi Include/Extend) sudah **hanya mendefinisikan relasi antar use case** dan tidak bercampur dengan detail desain sistem.
- [ ] **[2.4]** Periksa apakah Seksi 7 (Matriks Traceability) **tidak memuat data yang berulang secara tidak efisien** dengan Seksi 3.2 (Master Daftar UC). Jika ada kolom yang identik dan redundan, evaluasi apakah perlu disederhanakan.
- [ ] **[2.5]** Pastikan **Glosarium** (Seksi 8) hanya mendefinisikan istilah yang benar-benar dipakai dalam dokumen UCD ini, tidak mendefinisikan istilah yang tidak muncul sama sekali dalam dokumen.

---

### FASE 3 — DIMENSI D-03: STANDAR STRUKTUR DOKUMEN

**Tujuan**: Memastikan dokumen UCD memiliki struktur yang **sesuai standar praktik industri** penulisan Use Case Diagram profesional.

#### 3.1. Verifikasi Struktur Seksi Utama
- [ ] **[3.1.1]** Verifikasi bahwa dokumen memiliki minimal seksi-seksi wajib berikut dalam urutan yang logis:
  - [ ] Header/Frontmatter YAML (versi, tanggal, status, penyusun)
  - [ ] Riwayat Perubahan Dokumen (changelog)
  - [ ] Informasi Dokumen (tujuan, cakupan, posisi SDLC, hubungan dokumen lain, audiens target)
  - [ ] Identifikasi Aktor (internal & eksternal + diagram generalisasi)
  - [ ] System Boundary & Master Daftar Use Case
  - [ ] Diagram UCD Visual (overview + per modul)
  - [ ] Spesifikasi Naratif Use Case (seluruh 44 UC)
  - [ ] Pemetaan Relasi Include/Extend
  - [ ] Matriks Traceability (UC↔BRD, UC↔SRS, UC↔Aktor)
  - [ ] Glosarium
  - [ ] Referensi Dokumen
- [ ] **[3.1.2]** Jika ada seksi yang **belum ada** tetapi wajib ada dalam standar UCD industri, tambahkan seksi tersebut dengan konten yang relevan.

#### 3.2. Verifikasi Kelengkapan Frontmatter YAML
- [ ] **[3.2.1]** Pastikan frontmatter YAML di baris 1–8 memiliki field: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`. Pastikan tidak ada field yang kosong atau bernilai placeholder.

#### 3.3. Verifikasi Tabel Header Dokumen Standar
- [ ] **[3.3.1]** Pastikan tabel "Riwayat Perubahan Dokumen" sudah mencantumkan seluruh versi dokumen dengan kolom: Versi, Tanggal, Perubahan, Oleh. Pastikan setiap entri changelog **tidak kosong** di kolom manapun.

#### 3.4. Verifikasi Konvensi Format Tabel
- [ ] **[3.4.1]** Periksa apakah **semua tabel** dalam dokumen memiliki header kolom yang jelas, baris yang terisi penuh, dan tidak ada sel yang berisi `N/A`, `-` tanpa penjelasan, atau dibiarkan benar-benar kosong tanpa alasan. Jika ditemukan sel kosong yang seharusnya berisi data, isi dengan data yang valid dan relevan.

---

### FASE 4 — DIMENSI D-04: KESIAPAN SEBAGAI INPUT SDLC LANJUTAN

**Tujuan**: Memverifikasi bahwa dokumen UCD sudah mengandung semua informasi yang dibutuhkan oleh tim yang akan mengerjakan dokumen pada fase berikutnya.

- [ ] **[4.1]** **Validasi untuk SDD (System Design Document)**:
  Periksa apakah setiap UC memiliki Alur Utama (Main Flow) yang cukup **detail dan berurutan** sehingga seorang programmer dapat menderivasi diagram sequence dari narasi UC tersebut. Minimal harus menggambarkan: (a) siapa aktor yang memulai, (b) input apa yang diberikan ke sistem, (c) logika bisnis apa yang diproses sistem, dan (d) output apa yang dihasilkan sistem.
- [ ] **[4.2]** **Validasi untuk ERD & Skema Database**:
  Periksa apakah narasi use case secara eksplisit menyebutkan **nama entitas data utama** (tabel) yang terlibat dalam tiap transaksi (misal: `transaksi`, `barang`, `satuan_barang`, `limbah_produksi`, `karyawan`, dll.) sehingga database designer dapat mengidentifikasi entitas relasional.
- [ ] **[4.3]** **Validasi untuk Test Plan & Test Cases**:
  Pastikan setiap UC memiliki minimal **satu Alur Utama**, **minimal satu Alur Alternatif atau Alur Pengecualian** yang terdokumentasi. Jika ada UC yang hanya memiliki Alur Utama tanpa Alur Pengecualian sama sekali (ditandai dengan `-` atau kolom kosong), evaluasi apakah memang tidak ada skenario gagal yang mungkin terjadi, atau perlu ditambahkan.
- [ ] **[4.4]** **Validasi Completeness Matriks Traceability**:
  Pastikan kolom "Status" di Matriks UC↔BRD (Seksi 7.1) dan Matriks UC↔SRS (Seksi 7.2) tidak ada yang berstatus selain "Terpenuhi". Jika ada yang belum terpenuhi, catat sebagai celah kritis.

---

### FASE 5 — DIMENSI D-05: KUALITAS BAHASA INDONESIA

**Tujuan**: Memastikan seluruh teks dalam dokumen menggunakan bahasa Indonesia yang natural, tidak ambigu, tidak membingungkan, dan mudah dipahami oleh junior programmer atau AI agent.

- [ ] **[5.1]** Baca ulang seluruh **Seksi 1 (Informasi Dokumen)** dan pastikan setiap kalimat menggunakan **kalimat aktif dengan subjek yang jelas**. Contoh kalimat yang salah: "Dokumen ini digunakan untuk..." → Koreksi menjadi: "Dokumen ini mendefinisikan..." atau "Tim pengembang menggunakan dokumen ini untuk..."
- [ ] **[5.2]** Baca ulang seluruh **Seksi 2 (Identifikasi Aktor)** dan pastikan deskripsi singkat setiap aktor **konsisten menggunakan format kalimat yang sama** (semua kalimat deskriptif, semua menggunakan subjek aktor).
- [ ] **[5.3]** Baca ulang seluruh **Seksi 5 (Spesifikasi Naratif)** untuk setiap dari 44 UC, khususnya kolom "Alur Utama". Pastikan setiap langkah alur:
  - Menggunakan **kalimat aktif** dengan subjek eksplisit: "Aktor memasukkan..." atau "Sistem menampilkan..."
  - **Tidak ambigu**: hindari kata "data tersebut", "hal ini", "informasi yang dimaksud" tanpa referensi jelas.
  - **Tidak redundan**: tidak mengulang informasi yang sama dalam dua langkah yang berbeda.
  - **Tidak menggunakan singkatan tanpa definisi** sebelumnya (contoh: jika menggunakan "BOM", pastikan sudah didefinisikan di glosarium).
- [ ] **[5.4]** Periksa apakah ada **istilah Bahasa Inggris** yang digunakan tanpa terjemahan padahal sudah ada padanan resmi dalam kamus teknologi Bahasa Indonesia. Jika ada istilah teknis yang lebih mudah dipahami dalam bahasa Inggris (seperti "RBAC", "JWT", "BOM"), biarkan dalam bahasa Inggris namun pastikan sudah terdefinisi di glosarium.
- [ ] **[5.5]** Periksa konsistensi penulisan: apakah kata "use case" selalu ditulis konsisten (bukan bergantian "use case" dan "UseCase" atau "usecase"). Lakukan koreksi konsistensi terminologi di seluruh dokumen.
- [ ] **[5.6]** Pastikan **tidak ada kalimat yang terpotong** di tengah (truncated), terutama di dalam kolom tabel yang panjang.

---

### FASE 6 — DIMENSI D-06: KESIAPAN EKSEKUSI TANPA INTERUPSI

**Tujuan**: Memastikan tidak ada "lubang" atau pertanyaan yang akan timbul saat dokumen ini dijadikan referensi kerja.

- [ ] **[6.1]** Periksa apakah **setiap Use Case** memiliki UC-ID yang unik dan berurutan (UC-001 hingga UC-044) tanpa ada yang terduplikat atau loncat nomor.
- [ ] **[6.2]** Periksa apakah **setiap UC dalam Seksi 5** sudah tercantum di **Seksi 3.2** (Master Daftar UC). Dan sebaliknya, setiap UC di Seksi 3.2 sudah memiliki entri narasi di Seksi 5.
- [ ] **[6.3]** Periksa apakah setiap UC yang disebutkan dalam diagram Mermaid (Seksi 4) **konsisten dengan ID dan nama** yang ada di Seksi 3.2 dan Seksi 5. Jangan ada UC yang muncul di diagram Mermaid tetapi tidak terdaftar di master list, atau sebaliknya.
- [ ] **[6.4]** Periksa apakah relasi `<<include>>` dan `<<extend>>` yang disebutkan di Seksi 6 (dan di diagram Mermaid) **sudah konsisten dua arah**: jika UC-001 meng-include UC-022, maka di narasi UC-001 harus menyebutkan UC-022, dan di Seksi 6 harus terdaftar relasi tersebut.
- [ ] **[6.5]** Pastikan tidak ada **referensi maju (forward reference)** yang tidak terdefinisi: jika sebuah narasi UC merujuk ke UC-ID lain, pastikan UC-ID tersebut benar-benar ada di dokumen.
- [ ] **[6.6]** Pastikan **Prakondisi** setiap UC menyebutkan kondisi awal yang **dapat diverifikasi secara konkret** oleh sistem (misal: "Sesi JWT aktif", "Data BOM sudah terdaftar di database"), bukan kondisi yang abstrak dan tidak dapat dicek (misal: "Sistem siap digunakan").

---

### FASE 7 — DIMENSI D-07: PENGISIAN DATA KOSONG

**Tujuan**: Mengidentifikasi dan mengisi setiap field yang kosong, belum diisi, atau berisi placeholder dengan data yang valid, sesuai, dan relevan dalam ruang lingkup UCD.

- [ ] **[7.1]** Periksa seluruh tabel dan kolom di dokumen. Identifikasi sel yang berisi tanda `-`, `N/A`, `TBD`, `(kosong)`, atau string placeholder yang menunjukkan data belum diisi.
- [ ] **[7.2]** Untuk setiap **Alur Alternatif** yang berisi tanda `-` (kosong):
  - Evaluasi apakah use case tersebut memang **benar-benar tidak memiliki** skenario alternatif yang valid.
  - Jika ada skenario alternatif yang masuk akal (misal: input melalui cara berbeda, kondisi data yang berbeda), tambahkan dengan format: `**A[n]. [Nama Skenario]**: [Deskripsi langkah].`
  - Jika memang tidak ada skenario alternatif, biarkan dengan penjelasan singkat: `- (Tidak ada skenario alternatif yang berlaku untuk use case ini.)`
- [ ] **[7.3]** Untuk setiap **Alur Pengecualian** yang berisi tanda `-` (kosong):
  - Evaluasi apakah use case tersebut **memang tidak memiliki** skenario gagal/error yang mungkin.
  - Berdasarkan konteks bisnis (login gagal, koneksi DB putus, input tidak valid, izin akses ditolak), identifikasi skenario error yang relevan dan tambahkan menggunakan kode error dari SRS v1.1.
  - Contoh kode error yang perlu dikonsultasikan dari R-02: `ERR-DB-xxx`, `ERR-AUTH-xxx`, `ERR-VAL-xxx`, `ERR-STOCK-xxx`, `ERR-SYS-xxx`, `ERR-CASH-xxx`, `ERR-INPUT-xxx`.
  - Jika setelah evaluasi mendalam memang tidak ada skenario error, biarkan dengan penjelasan: `- (Tidak ada alur pengecualian spesifik; kegagalan umum ditangani oleh use case UC-032 RBAC dan UC-033 Log Audit.)`
- [ ] **[7.4]** Periksa apakah ada **kolom "Aktor Sekunder"** yang berisi `-` tetapi seharusnya memiliki aktor sekunder berdasarkan narasi Alur Utama (misal: UC yang menyebutkan notifikasi dikirim ke pemilik). Koreksi jika ditemukan inkonsistensi.
- [ ] **[7.5]** Periksa apakah kolom **"Catatan Khusus"** di spesifikasi naratif setiap UC memiliki informasi yang bermakna dan tidak dibiarkan kosong tanpa penjelasan.

---

### FASE 8 — DIMENSI D-08: VALIDASI DIAGRAM MERMAID

**Tujuan**: Memastikan semua 11 diagram Mermaid dalam dokumen valid secara sintaks, akurat secara konten, dan konsisten dengan narasi.

- [ ] **[8.1]** Periksa diagram **Seksi 2.3** (Hierarki Generalisasi Aktor): Pastikan semua 8 aktor internal terpetakan ke node yang benar, dan tidak ada aktor yang hilang atau terduplikat di diagram.
- [ ] **[8.2]** Periksa diagram **Seksi 4.1** (Diagram Utama Overview): Pastikan semua 8 aktor internal sudah memiliki koneksi ke modul yang benar, dan relasi aktor eksternal ditandai dengan garis putus-putus (`-.->`). Verifikasi bahwa relasi aktor ke modul di diagram konsisten dengan tabel hak akses di Seksi 2.1.
- [ ] **[8.3]** Periksa **10 diagram per modul** (Seksi 4.2.1 hingga 4.2.10): Untuk setiap diagram modul:
  - [ ] Pastikan semua UC yang seharusnya ada di modul tersebut sudah tercantum di diagram.
  - [ ] Pastikan semua UC yang ada di diagram konsisten ID-nya dengan Seksi 3.2.
  - [ ] Pastikan relasi `<<include>>` di diagram menggunakan sintaks yang konsisten: `-.->`  dengan label `"<<include>>"`.
  - [ ] Pastikan tidak ada node UC yang `orphan` (terdaftar di diagram tapi tidak terhubung ke aktor manapun).
- [ ] **[8.4]** Periksa apakah ada **label string** dalam diagram Mermaid yang mengandung karakter khusus yang dapat menyebabkan error parsing (seperti `&`, `<`, `>`, `"` tanpa escape). Jika ada, koreksi menggunakan escape character atau kutip string.
- [ ] **[8.5]** Pastikan diagram **Seksi 4.2.6** (Modul M.6) menggunakan nomor UC yang tepat: verifikasi bahwa UC-031 di diagram M.6 merujuk ke "Mengelola Pengeluaran & Biaya" (bukan UC-031 dari M.7 yang merujuk ke "Otorisasi RBAC"). Jika ada konflik nomor UC lintas modul dalam diagram, koreksi dengan menyesuaikan ID atau menambahkan penjelasan disambiguasi.

---

### FASE 9 — DIMENSI D-09: KONSISTENSI ID & TRACEABILITY

**Tujuan**: Memastikan semua ID (UC-ID, BR-F-ID, SRS-F-ID, ACT-ID) konsisten dan saling terhubung dengan benar di seluruh bagian dokumen.

- [ ] **[9.1]** Buat daftar semua UC-ID yang ada di:
  - Seksi 3.2 (Master Daftar Use Case)
  - Seksi 5 (Spesifikasi Naratif)
  - Seksi 6 (Relasi Include/Extend)
  - Seksi 7.1 (Matriks UC↔BRD)
  - Seksi 7.2 (Matriks UC↔SRS)
  - Seksi 7.3 (Matriks UC↔Aktor)
  - Seluruh diagram Mermaid di Seksi 4

  Pastikan **total UC yang terdaftar adalah 44** di setiap lokasi dan tidak ada yang hilang atau tidak konsisten.

- [ ] **[9.2]** Verifikasi bahwa **tidak ada UC-ID yang terduplikat** (misalnya UC-031 muncul untuk dua use case yang berbeda di bagian yang berbeda).
- [ ] **[9.3]** Verifikasi bahwa **semua ACT-ID** (ACT-01 hingga ACT-08, ACT-EXT-01 hingga ACT-EXT-04) di seluruh bagian dokumen konsisten dan tidak ada yang berbeda penulisannya.
- [ ] **[9.4]** Verifikasi bahwa **nama use case** di Seksi 5 (Spesifikasi Naratif) identik dengan nama yang ada di Seksi 3.2 (Master Daftar). Jika ada perbedaan kecil sekalipun (misal: huruf kapital, tanda baca), koreksi agar 100% identik.

---

### FASE 10 — DIMENSI D-10: VALIDASI SPESIFIKASI NARATIF 44 USE CASE

**Tujuan**: Memastikan setiap satu dari 44 Use Case memiliki spesifikasi naratif yang lengkap, tidak truncated, dan sesuai standar.

- [ ] **[10.1]** Iterasi satu per satu seluruh 44 use case (UC-001 hingga UC-044) di Seksi 5. Untuk setiap UC, verifikasi bahwa **semua 11 atribut berikut ada dan terisi**:
  1. `UC-ID`
  2. `Nama Use Case`
  3. `Derivasi` (BR-F dan SRS-F)
  4. `Modul`
  5. `Prioritas`
  6. `Aktor Primer`
  7. `Aktor Sekunder`
  8. `Deskripsi Singkat`
  9. `Prakondisi (Precondition)`
  10. `Pemicu (Trigger)`
  11. `Alur Utama (Main Flow)` — wajib berisi minimal 3 langkah terurut
  12. `Alur Alternatif (Alternative Flow)` — jika `-`, evaluasi di Fase 7
  13. `Alur Pengecualian (Exception Flow)` — jika `-`, evaluasi di Fase 7
  14. `Pasca-Kondisi (Postcondition)`
  15. `Aturan Bisnis Terkait`
  16. `Catatan Khusus`

- [ ] **[10.2]** Khusus untuk **UC-041 (Login)**, **UC-042 (Logout)**, **UC-043 (Dashboard)**, dan **UC-044 (Ubah Password)** yang berstatus "Tambahan" — verifikasi bahwa narasi UC-nya sudah diisi **secara lengkap** dan tidak kurang detail dibandingkan UC-UC fungsional lainnya. Use case dasar operasional ini sangat kritis karena menjadi prasyarat (precondition) semua UC lainnya.

---

### FASE 11 — PENULISAN ULANG DOKUMEN (OVERWRITE)

**Tujuan**: Menuangkan seluruh hasil validasi dan koreksi ke file target dengan cara menimpa (overwrite) sepenuhnya.

> **PERINGATAN KRITIS — WAJIB DIBACA DAN DIPATUHI SECARA MUTLAK**:
> 1. **DILARANG TRUNCATION**: Seluruh teks dari baris pertama hingga baris terakhir **wajib ditulis ulang sepenuhnya**. Tidak ada satu pun paragraf, kalimat, baris tabel, atau baris kode Mermaid yang boleh dipotong, disingkat, diringkas, atau dihilangkan.
> 2. **DILARANG MEMBUANG KONTEN VALID**: Hanya konten yang terbukti salah, tidak relevan, atau perlu diperbarui yang boleh dimodifikasi. Konten yang valid dan benar dipertahankan apa adanya.
> 3. **WAJIB OVERWRITE PENUH**: File ditimpa menggunakan operasi tulis lengkap (overwrite), bukan append atau partial edit.
> 4. **WAJIB INKREMENTASI VERSI**: Ubah versi dokumen dari `1.1` menjadi `1.2` di frontmatter YAML dan di baris changelog.
> 5. **WAJIB TAMBAH ENTRI CHANGELOG**: Tambahkan entri baru di tabel "Riwayat Perubahan Dokumen" dengan format:

```
| 1.2 | [TANGGAL-HARI-INI] | Validasi menyeluruh komprehensif: [ringkasan temuan dan perbaikan utama dalam satu paragraf singkat] | Senior UML Modeling Specialist & Systems Analyst |
```

Langkah-langkah penulisan ulang:

- [ ] **[11.1]** Setelah semua fase validasi (Fase 1 s.d. Fase 10) selesai, **kompilasikan seluruh perubahan** yang telah diidentifikasi dalam satu daftar terurut (apa yang diubah di baris/seksi mana).
- [ ] **[11.2]** Buka file `docs/sdlc/02_analysis/03_use_case_diagram.md` untuk ditulis ulang.
- [ ] **[11.3]** Mulai penulisan dari **baris pertama** (`---` frontmatter YAML). Ubah field `versi` dari `1.1` menjadi `1.2` dan field `tanggal` menjadi tanggal hari ini.
- [ ] **[11.4]** Tulis ulang **Seksi Riwayat Perubahan**: tambahkan entri changelog versi 1.2 di baris paling atas tabel changelog (sebelum entri v1.1).
- [ ] **[11.5]** Lanjutkan menulis ulang **setiap seksi** secara berurutan (Seksi 1, 2, 3, 4, 5, 6, 7, 8, 9) dengan menerapkan seluruh koreksi dari fase validasi, **tanpa melewatkan satu seksi pun**.
- [ ] **[11.6]** Pastikan seluruh **11 diagram Mermaid** ditulis ulang sepenuhnya dengan koreksi yang diperlukan.
- [ ] **[11.7]** Pastikan seluruh **44 spesifikasi naratif UC** ditulis ulang sepenuhnya tanpa ada yang dipotong.
- [ ] **[11.8]** Pastikan **tiga matriks traceability** (UC↔BRD, UC↔SRS, UC↔Aktor) ditulis ulang sepenuhnya.
- [ ] **[11.9]** Tulis ulang **Seksi 8 (Glosarium)**: tambahkan istilah baru jika ada yang digunakan dalam dokumen namun belum terdefinisi.
- [ ] **[11.10]** Tulis ulang **Seksi 9 (Referensi Dokumen)**: jika dalam proses validasi ditemukan bahwa perbaikan dokumen memerlukan data dari file referensi **baru** yang belum tercantum di tabel referensi saat ini, tambahkan file referensi baru tersebut sebagai baris baru di tabel Seksi 9 (paling bawah, setelah baris referensi yang sudah ada). Jangan hapus referensi yang sudah ada.
- [ ] **[11.11]** Setelah penulisan selesai, **verifikasi file output** dengan menghitung jumlah baris dan memastikan tidak ada bagian yang terpotong di akhir file.

---

### FASE 12 — VERIFIKASI PASCA-PENULISAN

**Tujuan**: Memastikan file yang sudah ditulis ulang benar-benar valid dan lengkap.

- [ ] **[12.1]** Baca ulang **baris pertama** file output: pastikan frontmatter YAML dimulai dengan `---` dan berisi versi `1.2`.
- [ ] **[12.2]** Baca ulang **baris terakhir** file output: pastikan file berakhir dengan baris Seksi 9 (Referensi Dokumen) dan tidak terpotong di tengah kalimat.
- [ ] **[12.3]** Hitung jumlah **header seksi** (## dan ###) di file output dan pastikan sudah sesuai dengan struktur yang direncanakan.
- [ ] **[12.4]** Hitung jumlah **blok kode Mermaid** (``` mermaid) di file output dan pastikan berjumlah **11 diagram** (1 diagram generalisasi + 1 overview + 10 per modul).
- [ ] **[12.5]** Hitung jumlah **spesifikasi naratif UC** (## UC-0xx) dan pastikan berjumlah tepat **44 use case** (UC-001 hingga UC-044).
- [ ] **[12.6]** Pastikan **versi di frontmatter YAML** dan **versi di tabel changelog** **identik** (keduanya menampilkan `1.2`).
- [ ] **[12.7]** Pastikan **tidak ada teks placeholder** seperti `[TODO]`, `[FILL IN]`, `TBD`, `...` yang tertinggal di dalam file output.

---

## 6. Kriteria Kelengkapan & Penerimaan (Definition of Done)

Issue ini dianggap **selesai** hanya jika seluruh kondisi berikut terpenuhi tanpa pengecualian:

| # | Kriteria Penerimaan | Status |
|---|---|---|
| K-01 | Semua 44 use case memiliki spesifikasi naratif lengkap (16 atribut) tanpa ada yang truncated | [ ] |
| K-02 | Semua relasi antara BRD, SRS, dan UC sudah divalidasi dan dicatat di matriks traceability | [ ] |
| K-03 | Semua Alur Pengecualian yang sebelumnya kosong sudah diisi dengan kode error yang benar dari SRS v1.1 | [ ] |
| K-04 | Semua 11 diagram Mermaid valid secara sintaks dan akurat secara konten | [ ] |
| K-05 | Tidak ada data kosong, placeholder, atau field yang tidak terisi di seluruh dokumen | [ ] |
| K-06 | Bahasa Indonesia di seluruh dokumen natural, tidak ambigu, dan menggunakan kalimat aktif | [ ] |
| K-07 | Versi dokumen sudah diinkrementasi dari v1.1 menjadi v1.2 | [ ] |
| K-08 | Entri changelog versi v1.2 sudah ditambahkan di tabel Riwayat Perubahan | [ ] |
| K-09 | File ditulis ulang secara penuh (overwrite) dari baris pertama hingga terakhir tanpa truncation | [ ] |
| K-10 | Jika ada referensi baru yang digunakan, sudah ditambahkan di Seksi 9 (Referensi Dokumen) | [ ] |

---

## 7. Catatan Tambahan untuk Eksekutor

### 7.1. Poin Kritis Khusus Dokumen UCD
Berikut adalah hal-hal yang **spesifik** untuk dokumen Use Case Diagram dan sering menjadi sumber kesalahan:

1. **Konflik Penomoran UC-031**: Dalam dokumen ini, UC-031 di Seksi 3.2 adalah "Mengelola Pengeluaran Rutin & Biaya Tak Terduga" (Modul M.6), tetapi dalam beberapa diagram Mermaid, UC-031 dirujuk sebagai "Otorisasi RBAC". Ini adalah sumber ambiguitas yang **wajib** diselesaikan dalam validasi ini. Jika memang ada konflik, perbaiki dengan cara yang paling konsisten.

2. **Ketiadaan Diagram UCD dalam Format Standar UML**: Dokumen ini menggunakan diagram Mermaid sebagai pengganti diagram UML formal. Ini adalah pilihan yang valid untuk konteks pengembangan berbasis teks. Namun, pastikan setiap diagram Mermaid **secara semantik mencerminkan** notasi UML Use Case Diagram yang benar (aktor sebagai ellipse, use case sebagai rectangle rounded, system boundary sebagai rectangle besar).

3. **Validasi Pasca-Kondisi Setiap UC**: Pastikan Pasca-Kondisi tidak hanya menyalin ulang tujuan use case, melainkan mendeskripsikan **kondisi konkret yang terverifikasi** di database atau antarmuka sistem setelah use case selesai.

4. **Alur Utama Harus Interaktif (Dialog)**: Sesuai Konvensi Penulisan di Seksi 5.1 dokumen, setiap Alur Utama harus menggambarkan **dialog interaktif** antara aktor dan sistem CLI. Langkah yang hanya menyebutkan aksi sistem (tanpa input dari aktor) atau hanya aksi aktor (tanpa respons sistem) dianggap tidak lengkap.

### 7.2. Pola Penulisan Kode Error yang Benar
Seluruh kode error dalam Alur Pengecualian **wajib** mengikuti format yang sudah distandarkan di SRS v1.1. Format penulisan yang benar:

```
**E[n]. [KODE-ERROR] ([Nama Singkat Error])**: [Deskripsi kondisi pemicu error]. [Tindakan yang diambil sistem sebagai respons].
```

Contoh yang benar:
```
**E1. ERR-DB-001 (Koneksi Terputus)**: Jika koneksi MySQL terputus saat menyimpan data, sistem melakukan rollback transaksi, menampilkan pesan kegagalan, dan mencatat log lokal.
```

### 7.3. Larangan Mutlak
- **DILARANG** mempersingkat atau merangkum konten yang sudah panjang dengan alasan "terlalu detail".
- **DILARANG** mengganti konten valid dengan placeholder `[...]` atau `(dst)` atau sejenisnya.
- **DILARANG** menghilangkan diagram Mermaid dengan alasan kompleksitas.
- **DILARANG** menghapus baris dari tabel matriks traceability meski dianggap redundan.
- **DILARANG** menimpa file dengan konten yang lebih pendek dari konten aslinya tanpa alasan validasi yang jelas dan terdokumentasi.

---

## 8. Referensi untuk Eksekutor Issue Ini

| # | Nama Dokumen | Path | Relevansi untuk Issue Ini |
|---|---|---|---|
| 1 | `03_use_case_diagram.md` | `docs/sdlc/02_analysis/03_use_case_diagram.md` | **TARGET VALIDASI** — File yang akan dianalisis dan ditulis ulang |
| 2 | `01_business_requirements.md` | `docs/sdlc/02_analysis/01_business_requirements.md` | Sumber kebenaran aktor, RBAC, dan kebutuhan bisnis fungsional |
| 3 | `02_software_requirements.md` | `docs/sdlc/02_analysis/02_software_requirements.md` | Sumber kebenaran SRS-F, kode error, dan spesifikasi teknis |
| 4 | `03_stakeholder_register.md` | `docs/sdlc/01_planning/03_stakeholder_register.md` | Profil stakeholder untuk validasi audiens target |
| 5 | `01_project_charter.md` | `docs/sdlc/01_planning/01_project_charter.md` | Visi misi dan cakupan sistem untuk validasi system boundary |
| 6 | `05_innovation_proposal.md` | `docs/sdlc/01_planning/05_innovation_proposal.md` | Daftar inovasi untuk validasi kelengkapan use case |
