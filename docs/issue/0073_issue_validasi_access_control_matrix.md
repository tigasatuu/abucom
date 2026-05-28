# Validasi, Audit, dan Penyempurnaan Dokumen Access Control Matrix (ACM)

---

## Metadata Issue

| Field              | Detail                                                                              |
|--------------------|-------------------------------------------------------------------------------------|
| **Judul**          | Validasi, Audit, dan Penyempurnaan Dokumen Access Control Matrix (ACM)              |
| **Tipe**           | Documentation Quality Assurance / Security Review                                   |
| **Prioritas**      | 🔴 Critical                                                                         |
| **Target File**    | `docs/sdlc/02_analysis/06_access_control_matrix.md`                                 |
| **Dibuat Pada**    | 2026-05-28                                                                          |
| **Status**         | Open                                                                                |
| **Assignee**       | Junior Programmer / AI Model                                                        |

---

## 1. Latar Belakang dan Tujuan

Dokumen **Access Control Matrix (ACM)** di path `docs/sdlc/02_analysis/06_access_control_matrix.md` adalah dokumen **penutup dan terakhir** dari Fase 02 Analysis dalam SDLC proyek AbuCom. Dokumen ini menjadi **landasan keamanan utama** yang harus dikonsumsi oleh Fase 03 Design (System Design Document, Database Schema), Fase 04 Implementation (decorator RBAC Python `@require_role`, middleware JWT), dan Fase 05 Testing (UAT penetration testing otorisasi).

Karena posisi strategisnya sebagai **gerbang penutup Fase 02** dan **pintu masuk utama Fase 03**, setiap ketidakakuratan, ketidaklengkapan, atau ambiguitas pada dokumen ini **secara langsung akan merusak kualitas seluruh fase SDLC berikutnya** dan menyebabkan halusinasi atau kesalahan fatal pada implementasi kode keamanan.

Issue ini memerintahkan untuk melakukan **audit ketat, menyeluruh, dan tidak toleran** terhadap dokumen ACM tersebut sebelum dokumen ini digunakan sebagai acuan fase berikutnya.

---

## 2. Persona yang Harus Diemban

> ⚠️ **WAJIB DIBACA DAN DIEMBAN SEBELUM MEMULAI PEKERJAAN**

Kamu adalah **Senior Security Architect & RBAC Specialist** dengan keahlian berlapis:

1. **Pakar Keamanan Aplikasi (AppSec)**: Berpengalaman merancang sistem RBAC (Role-Based Access Control) berbasis Least Privilege dan Separation of Duties untuk aplikasi bisnis enterprise.
2. **Analis Sistem Senior (System Analyst)**: Mahir menelaah kelengkapan, konsistensi, dan ketertelusuran (traceability) antar dokumen SDLC.
3. **Arsitek Database**: Paham skema CRUD MySQL, sensitivitas data, dan implikasi hak akses level tabel terhadap integritas data.
4. **Ahli Kepatuhan Regulasi**: Memahami implementasi teknis kepatuhan terhadap **UU Pelindungan Data Pribadi (UU PDP No. 27/2022)** Indonesia.
5. **Technical Writer Senior**: Memastikan setiap kalimat, tabel, dan diagram di dalam dokumen bebas dari ambiguitas dan dapat dipahami secara tidak ambigu oleh junior programmer atau AI model yang lebih kecil.

Dengan persona ini, kamu **tidak boleh toleran** terhadap:
- Inkonsistensi data antar bab dalam dokumen yang sama.
- Data yang tidak tercantum dalam referensi tetapi dimuat di dokumen.
- Data referensi yang ada tetapi **tidak** termuat di dokumen.
- Kalimat ambigu yang bisa menimbulkan lebih dari satu tafsiran implementasi.
- Simbol hak akses yang tidak konsisten dengan legenda yang didefinisikan.
- Statistik numerik yang tidak dapat diverifikasi secara manual.
- Operasi eskalasi yang tidak terdefinisi error code-nya dengan jelas.

---

## 3. Dokumen Referensi yang Wajib Dibaca

Sebelum melakukan validasi, **baca terlebih dahulu seluruh dokumen berikut secara penuh (full read)**. Dokumen-dokumen ini adalah sumber kebenaran (*source of truth*) yang harus diperbandingkan secara mendalam dengan dokumen utama (ACM):

| No | File Referensi                        | Path Lengkap                                               | Aspek yang Relevan untuk ACM |
|----|---------------------------------------|------------------------------------------------------------|-------------------------------|
| 1  | `01_business_requirements.md`         | `docs/sdlc/02_analysis/01_business_requirements.md`        | Daftar 8 peran (Bab 5.1), tabel hak akses ringkas RBAC (Bab 5.3), 43–44 kebutuhan bisnis (BR-F-xxx). |
| 2  | `02_software_requirements.md`         | `docs/sdlc/02_analysis/02_software_requirements.md`        | Parameter JWT (durasi, algoritma), bcrypt cost factor, rate limiting, kode error ERR-xxx, SRS-F-xxx. |
| 3  | `03_use_case_diagram.md`              | `docs/sdlc/02_analysis/03_use_case_diagram.md`             | Daftar lengkap 44 Use Case (UC-001 s.d UC-044) beserta aktor yang terlibat per use case. |
| 4  | `04_workflow_diagram.md`              | `docs/sdlc/02_analysis/04_workflow_diagram.md`             | Swimlane alur kerja setiap peran, titik interaksi antar peran, dan operasi yang memerlukan eskalasi. |
| 5  | `05_data_dictionary.md`              | `docs/sdlc/02_analysis/05_data_dictionary.md`              | Daftar lengkap 28 tabel MySQL, kolom per tabel, tipe data, dan constraint FK/PK. |
| 6  | `03_stakeholder_register.md`          | `docs/sdlc/01_planning/03_stakeholder_register.md`         | Grid Power/Interest pelibatan dan deskripsi otoritatif setiap peran stakeholder. |
| 7  | `05_innovation_proposal.md`           | `docs/sdlc/01_planning/05_innovation_proposal.md`          | Parameter inovasi keamanan terintegrasi (enkripsi, multi-cabang, tabungan virtual, PPOB). |

---

## 4. Checklist Implementasi (Step-by-Step — Wajib Diikuti Urut)

> **PENTING**: Ikuti checklist ini **secara berurutan dari atas ke bawah**. Jangan melompat langkah. Tandai setiap tugas dengan `[x]` setelah selesai dikerjakan. Jangan mulai menulis ulang file sebelum semua checklist validasi (Langkah 1–9) selesai.

---

### 🔵 LANGKAH 0 — PERSIAPAN AWAL (Wajib Dilakukan Sebelum Segalanya)

- [ ] **0.1** Buka dan baca penuh (full read dari baris pertama hingga terakhir) file target:
  `docs/sdlc/02_analysis/06_access_control_matrix.md`
  > Catatan: File ini memiliki ±751 baris. Pastikan kamu membaca **seluruhnya** tanpa skip.

- [ ] **0.2** Buka dan baca penuh file referensi **[1]** `01_business_requirements.md`.
  > Fokus pada: Bab Definisi Peran, Tabel RBAC Ringkas, dan semua ID kebutuhan `BR-F-xxx`.

- [ ] **0.3** Buka dan baca penuh file referensi **[2]** `02_software_requirements.md`.
  > Fokus pada: Semua ID `SRS-F-xxx`, parameter keamanan JWT, bcrypt, rate limiting, dan kode error `ERR-xxx`.

- [ ] **0.4** Buka dan baca penuh file referensi **[3]** `03_use_case_diagram.md`.
  > Fokus pada: Daftar lengkap Use Case `UC-001` s.d `UC-044` beserta aktor yang terlibat di setiap use case.

- [ ] **0.5** Buka dan baca penuh file referensi **[4]** `04_workflow_diagram.md`.
  > Fokus pada: Swimlane diagram per alur kerja, peran yang terlibat, dan titik eskalasi otorisasi.

- [ ] **0.6** Buka dan baca penuh file referensi **[5]** `05_data_dictionary.md`.
  > Fokus pada: Daftar 28 tabel MySQL beserta deskripsi kolom, tipe data, dan tingkat sensitivitas data.

- [ ] **0.7** Buka dan baca penuh file referensi **[6]** `03_stakeholder_register.md`.
  > Fokus pada: Deskripsi peran, level otoritas, dan Power/Interest grid setiap stakeholder.

- [ ] **0.8** Buka dan baca penuh file referensi **[7]** `05_innovation_proposal.md`.
  > Fokus pada: Fitur keamanan inovatif (enkripsi data, multi-cabang, threshold keuangan, PPOB alert).

- [ ] **0.9** Buat **catatan kerja sementara** (boleh di memori atau scratch pad) yang merangkum temuan-temuan penting dari setiap referensi sebelum mulai validasi.

---

### 🟡 LANGKAH 1 — VALIDASI KELENGKAPAN KOMPARASI REFERENSI

> **Tujuan**: Memastikan ACM tidak melewatkan data penting dari dokumen referensi.

#### Validasi 1A — Kelengkapan Peran dari BRD
- [ ] **1A.1** Ambil daftar peran internal dari `01_business_requirements.md` (Bab Definisi Peran / Bab 5.1).
  Bandingkan dengan Tabel di **Bab 2.1** dokumen ACM.
  - Pertanyaan validasi: Apakah semua 8 peran (`pemilik`, `kepala_percetakan`, `pramuniaga`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang`) sudah tercantum di ACM Bab 2.1?
  - Apakah ada peran di BRD yang **tidak ada** di ACM? → Jika ada, catat sebagai `[MISSING_ROLE]`.
  - Apakah ada peran di ACM yang **tidak ada** di BRD? → Jika ada, catat sebagai `[ORPHAN_ROLE]`.
  - Apakah kode peran sistem (`pemilik`, `kasir`, dll.) di ACM konsisten dengan nama kode di BRD? → Jika tidak konsisten, catat sebagai `[INCONSISTENT_ROLE_CODE]`.

- [ ] **1A.2** Ambil daftar **aktor eksternal** dari BRD.
  Bandingkan dengan Tabel di **Bab 2.3** dokumen ACM.
  - Apakah semua aktor eksternal (Pelanggan, Supplier, Institusi Perbankan, Kerabat) sudah tercantum? → Jika ada yang tidak ada, catat sebagai `[MISSING_EXT_ACTOR]`.

#### Validasi 1B — Kelengkapan Use Case dari UCD
- [ ] **1B.1** Ambil daftar lengkap use case dari `03_use_case_diagram.md`.
  Hitung total use case yang ada. Bandingkan jumlah total dengan klaim dokumen ACM di **Bab 1.2** (disebutkan 44 Use Case UC-001 s.d UC-044).
  - Apakah jumlah use case di UCD sama persis dengan yang diklaim ACM? → Jika berbeda, catat sebagai `[UC_COUNT_MISMATCH]`.

- [ ] **1B.2** Ambil seluruh ID use case `UC-001` s.d `UC-044` dari UCD.
  Bandingkan satu per satu dengan **Tabel Bab 8.3** di dokumen ACM (Pemetaan ACM ↔ UCD).
  - Apakah ada use case di UCD yang **tidak terpetakan** di Tabel 8.3 ACM? → Jika ada, catat sebagai `[MISSING_UC_MAPPING]` beserta ID use case yang hilang.
  - Apakah ada ID use case di ACM Tabel 8.3 yang **tidak ada** di UCD? → Jika ada, catat sebagai `[PHANTOM_UC]`.

- [ ] **1B.3** Untuk setiap use case yang ada di UCD, periksa apakah **aktor yang terlibat** di use case tersebut sudah tercermin secara konsisten di matriks hak akses **Bab 4** dokumen ACM.
  - Contoh: Jika di UCD, use case UC-001 (Mencatat Transaksi) melibatkan `kasir` dan `pramuniaga`, maka di Bab 4.2 baris `M1-001`, kedua peran tersebut harus memiliki hak akses bukan `⛔ DENY`.
  - Jika ada inkonsistensi, catat sebagai `[ACTOR_ACCESS_MISMATCH]` beserta ID use case dan peran yang bermasalah.

#### Validasi 1C — Kelengkapan Tabel Database dari Data Dictionary
- [ ] **1C.1** Ambil daftar lengkap nama tabel dari `05_data_dictionary.md`.
  Hitung total tabel. Bandingkan dengan klaim **Bab 1.2** dan **Bab 3.2** dokumen ACM (diklaim 28 tabel).
  - Apakah jumlah tabel di Data Dictionary sama persis dengan yang diklaim ACM? → Jika berbeda, catat sebagai `[TABLE_COUNT_MISMATCH]`.

- [ ] **1C.2** Ambil semua nama tabel dari Data Dictionary. Bandingkan satu per satu dengan daftar tabel di **Bab 3.2** dan **Matriks CRUD Bab 5.2** dokumen ACM.
  - Apakah ada tabel di Data Dictionary yang **tidak ada** di Bab 3.2 atau Bab 5.2 ACM? → Catat sebagai `[MISSING_TABLE]`.
  - Apakah ada tabel di Bab 5.2 ACM yang **tidak ada** di Data Dictionary? → Catat sebagai `[PHANTOM_TABLE]`.

- [ ] **1C.3** Periksa konsistensi **nama tabel** antara ACM dan Data Dictionary.
  - Apakah ada perbedaan penulisan nama tabel (misalnya `jasa_service` vs `jasa_servis`)? → Catat sebagai `[TABLE_NAME_TYPO]`.

- [ ] **1C.4** Untuk setiap tabel di Bab 5.2 ACM, periksa apakah **tingkat sensitivitas** tabel tersebut (Sangat Sensitif / Sensitif / Operasional) di Bab 3.2 sudah konsisten dengan hak akses CRUD yang diberikan di Bab 5.2.
  - Contoh: Tabel yang dikategorikan "Sangat Sensitif" seharusnya hanya memiliki CRUD untuk `pemilik`, semua peran lain harus `----`.
  - Jika tidak konsisten, catat sebagai `[SENSITIVITY_MISMATCH]` beserta nama tabel dan peran yang bermasalah.

#### Validasi 1D — Kelengkapan Kode Error dari SRS
- [ ] **1D.1** Ambil semua kode error `ERR-xxx` yang didefinisikan di `02_software_requirements.md`.
  Bandingkan dengan semua kode error yang digunakan di **Bab 6** dokumen ACM.
  - Apakah semua kode error di ACM Bab 6 ada dan konsisten dengan definisi di SRS? → Jika ada kode yang tidak cocok, catat sebagai `[ERR_CODE_MISMATCH]` beserta kode yang bermasalah.
  - Khususnya periksa: `ERR-AUTH-003`, `ERR-AUTH-029`, `ERR-FILE-039`, `ERR-AUTH-011`, `ERR-SESSION-002`, `ERR-AUTH-002`, `ERR-CASH-001`, `ERR-AUTH-030`.

- [ ] **1D.2** Ambil semua parameter keamanan teknis dari SRS (durasi JWT, cost factor bcrypt, batas rate limiting).
  Bandingkan dengan Bab 6.4 dan Bab 6.5 dokumen ACM.
  - JWT duration: Apakah `28800 detik (8 jam)` sesuai dengan SRS?
  - JWT algorithm: Apakah `HS256` sesuai dengan SRS?
  - bcrypt cost factor: Apakah `12` sesuai dengan SRS?
  - Rate limiting: Apakah `5 kali gagal = 600 detik (10 menit)` sesuai dengan SRS?
  - Jika ada yang tidak sesuai, catat sebagai `[PARAM_MISMATCH]`.

#### Validasi 1E — Kelengkapan Pemetaan BRD ID dari BRD
- [ ] **1E.1** Ambil semua ID kebutuhan bisnis `BR-F-xxx` dari `01_business_requirements.md`.
  Bandingkan satu per satu dengan **Tabel Bab 8.1** di dokumen ACM (Pemetaan ACM ↔ BRD).
  - Apakah ada `BR-F-xxx` dari BRD yang **tidak ada** di Tabel 8.1 ACM? → Catat sebagai `[MISSING_BRD_MAPPING]`.
  - Apakah ada `BR-F-xxx` di Tabel 8.1 ACM yang **tidak ada** di BRD? → Catat sebagai `[PHANTOM_BRD_ID]`.

- [ ] **1E.2** Periksa kesesuaian nama fungsi menu di Tabel 8.1 ACM dengan nama yang ada di BRD.
  - Apakah deskripsi singkat nama fungsi di kolom "Menu / Fungsi Target" Tabel 8.1 konsisten dengan BRD? → Jika tidak, catat sebagai `[FUNC_NAME_MISMATCH]`.

#### Validasi 1F — Kelengkapan Pemetaan SRS ID dari SRS
- [ ] **1F.1** Ambil semua ID `SRS-F-xxx` dari `02_software_requirements.md`.
  Bandingkan satu per satu dengan **Tabel Bab 8.2** di dokumen ACM (Pemetaan ACM ↔ SRS).
  - Apakah ada `SRS-F-xxx` yang relevan dengan hak akses/keamanan di SRS yang **tidak ada** di Tabel 8.2 ACM? → Catat sebagai `[MISSING_SRS_MAPPING]`.
  - Apakah ada `SRS-F-xxx` di Tabel 8.2 ACM yang **tidak ada** di SRS? → Catat sebagai `[PHANTOM_SRS_ID]`.

- [ ] **1F.2** Periksa nama modul kode target di kolom "Modul Kode Target" Tabel 8.2.
  - Apakah penamaan file Python (`.py`) di Tabel 8.2 konsisten dengan konvensi penamaan yang ditetapkan di SRS (jika ada)? → Jika tidak konsisten, catat sebagai `[MODULE_NAME_INCONSISTENCY]`.

#### Validasi 1G — Kelengkapan dari Workflow Diagram
- [ ] **1G.1** Ambil semua alur kerja (workflow) yang ada di `04_workflow_diagram.md`.
  Identifikasi seluruh titik di mana terdapat **perpindahan tanggung jawab antar peran** (handover point) atau **operasi yang memerlukan otorisasi lebih tinggi**.
  Bandingkan dengan daftar operasi eskalasi di **Bab 6.1** dan **Bab 6.2** dokumen ACM.
  - Apakah ada operasi eskalasi di Workflow Diagram yang **tidak tercatat** di Bab 6.1 atau 6.2 ACM? → Catat sebagai `[MISSING_ESCALATION_RULE]`.

- [ ] **1G.2** Periksa apakah **5 diagram alur Mermaid** di Bab 7 dokumen ACM (7.1 s.d 7.5) sudah merepresentasikan alur kerja yang paling kritis dan paling relevan dari Workflow Diagram.
  - Apakah ada alur kritis dari WFD yang **belum memiliki** diagram Mermaid di Bab 7 ACM? → Jika ada, catat sebagai `[MISSING_WORKFLOW_DIAGRAM]` dan tentukan apakah perlu ditambahkan atau cukup dideskripsikan dalam teks.

#### Validasi 1H — Kelengkapan dari Stakeholder Register
- [ ] **1H.1** Ambil deskripsi otoritatif setiap peran dari `03_stakeholder_register.md`.
  Bandingkan dengan deskripsi di kolom "Deskripsi Peran" dan "Level Hierarki" di **Tabel Bab 2.1** dokumen ACM.
  - Apakah ada perbedaan signifikan pada deskripsi peran antara Stakeholder Register dan ACM? → Jika ada, catat sebagai `[ROLE_DESC_MISMATCH]` dan selaraskan dengan Stakeholder Register sebagai sumber kebenaran.

---

### 🟡 LANGKAH 2 — VALIDASI RELEVANSI DAN FOKUS DOKUMEN (KEBERSIHAN KONTEN)

> **Tujuan**: Memastikan ACM hanya berisi informasi yang memang seharusnya ada dalam dokumen ACM, tidak lebih dan tidak kurang.

- [ ] **2.1** Baca ulang setiap bab dokumen ACM. Untuk setiap konten yang ada, tanyakan pada diri sendiri:
  *"Apakah konten ini adalah informasi tentang SIAPA yang boleh mengakses APA dengan hak akses SEPERTI APA?"*
  - Jika jawabannya **TIDAK** dan konten tersebut lebih cocok berada di dokumen lain (misalnya detail implementasi kode lebih cocok di SDD, atau detail skema tabel lebih cocok di Data Dictionary), maka **catat sebagai konten yang perlu dievaluasi** untuk dikurangi atau diringkas.

- [ ] **2.2** Periksa **Bab 7 (Workflow Mapping)** — Apakah diagram Mermaid di Bab 7 memberikan nilai tambah spesifik untuk pemahaman otorisasi ACM?
  - Diagram Mermaid di ACM seharusnya **hanya menampilkan titik pemeriksaan RBAC (guard point)** dan **konsekuensi ALLOW/DENY**, bukan detail alur bisnis secara penuh (alur bisnis lengkap ada di Workflow Diagram).
  - Jika ada diagram yang terlalu detail tentang alur bisnis (bukan otorisasi), catat sebagai `[DIAGRAM_SCOPE_CREEP]` dan sederhanakan fokusnya ke aspek otorisasi.

- [ ] **2.3** Periksa **Bab 10 (Glosarium)** — Apakah semua istilah yang ada di glosarium benar-benar digunakan di dalam dokumen ACM?
  - Jika ada istilah di glosarium yang tidak digunakan di body dokumen, catat sebagai `[UNUSED_GLOSSARY_TERM]`.
  - Apakah ada istilah penting yang digunakan di body dokumen tetapi **tidak** ada di glosarium? → Catat sebagai `[MISSING_GLOSSARY_TERM]` dan tambahkan definisinya.

- [ ] **2.4** Periksa apakah ada **duplikasi informasi** yang tidak perlu antar bab:
  - Informasi yang sama ditulis ulang secara verbatim di dua bab berbeda tanpa ada nilai tambah → Catat sebagai `[DUPLICATE_CONTENT]`.
  - Contoh: Legenda simbol hak akses didefinisikan di Bab 1.6 dan juga di Bab 4.1 — periksa apakah salah satunya adalah duplikasi yang bisa direferensikan saja.

---

### 🟡 LANGKAH 3 — VALIDASI STRUKTUR DOKUMEN (STANDAR INDUSTRI)

> **Tujuan**: Memastikan struktur dokumen ACM memenuhi standar praktik industri untuk dokumen keamanan RBAC/ACM.

- [ ] **3.1** Periksa apakah **header YAML frontmatter** di baris pertama dokumen (baris 1–8) sudah lengkap:
  - Field yang wajib ada: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`.
  - Apakah semua field sudah terisi (tidak ada yang kosong atau `N/A`)? → Jika ada yang kosong, catat sebagai `[MISSING_FRONTMATTER_FIELD]`.

- [ ] **3.2** Periksa apakah **Riwayat Perubahan Dokumen** (Bab pertama setelah header) sudah ada dan terisi dengan benar:
  - Apakah tabel riwayat perubahan mencantumkan: Versi, Tanggal, Perubahan, Oleh? → Jika kolom tidak ada, catat sebagai `[MISSING_CHANGELOG_COLUMN]`.
  - Apakah setiap entri riwayat perubahan informatif dan deskriptif? → Jika ada entri yang terlalu singkat/generik, catat sebagai `[VAGUE_CHANGELOG_ENTRY]`.

- [ ] **3.3** Periksa kelengkapan **Bab 1 — Informasi Dokumen**. Bab ini wajib memiliki minimal:
  - [x] Sub-bab Tujuan Dokumen
  - [x] Sub-bab Cakupan Dokumen
  - [x] Sub-bab Posisi dalam SDLC
  - [x] Sub-bab Hubungan dengan Dokumen Lain (Input/Output)
  - [x] Sub-bab Audiens Target
  - [x] Sub-bab Konvensi Notasi/Legenda
  > Jika ada sub-bab yang **hilang** dari standar di atas, catat sebagai `[MISSING_CHAPTER_SECTION]` dan tambahkan.

- [ ] **3.4** Periksa kelengkapan **Bab 2 — Definisi Subjek Akses**. Bab ini wajib memiliki:
  - [x] Tabel peran internal beserta ID, Nama, Kode Sistem, Deskripsi, Level Hierarki.
  - [x] Diagram hierarki peran (misalnya Mermaid graph).
  - [x] Tabel aktor eksternal beserta strategi perlindungan data.
  > Jika ada sub-bab yang **hilang**, catat sebagai `[MISSING_CHAPTER_SECTION]`.

- [ ] **3.5** Periksa kelengkapan **Bab 3 — Definisi Objek Akses**. Bab ini wajib memiliki:
  - [x] Daftar menu CLI per modul (M.1 s.d M.10 + Use Case Dasar) beserta ID menu.
  - [x] Daftar tabel database yang dilindungi beserta kategorisasi sensitivitas.
  - [x] Daftar fungsi/operasi bisnis kritis yang berisiko tinggi.
  > Jika ada yang hilang atau tidak lengkap, catat sebagai `[MISSING_OBJECT_DEFINITION]`.

- [ ] **3.6** Periksa kelengkapan **Bab 4 — Matriks Kontrol Akses Utama**. Bab ini wajib memiliki:
  - [x] Legenda simbol akses yang jelas.
  - [x] Satu tabel matriks per modul (M.1 s.d M.10) beserta Use Case Dasar.
  - [x] Kolom untuk semua 8 peran internal di setiap tabel.
  - [x] Kolom "Catatan Keamanan / Khusus" di setiap tabel.
  > Jika ada tabel modul yang **hilang** atau **tidak memiliki** salah satu kolom peran, catat sebagai `[MISSING_ACCESS_MATRIX]`.

- [ ] **3.7** Periksa apakah ada **standar industri ACM** yang belum diterapkan pada dokumen ini:
  - **Kebijakan Default Deny**: Apakah sudah dinyatakan secara eksplisit bahwa sistem menggunakan kebijakan `DEFAULT DENY` (semua akses ditolak kecuali diberikan secara eksplisit)? → Jika belum ada pernyataan eksplisit ini di Bab 1 atau Bab 6, catat sebagai `[MISSING_DEFAULT_DENY_POLICY]` dan tambahkan.
  - **Kebijakan Inheritance/Pewarisan Hak Akses**: Apakah dokumen sudah menjelaskan apakah ada hak akses yang diwarisi dari level hierarki yang lebih tinggi? → Jika belum ada penjelasan ini, catat sebagai `[MISSING_INHERITANCE_POLICY]`.
  - **Kebijakan Review Berkala ACM**: Untuk dokumen keamanan tingkat industri, seharusnya ada pernyataan kapan ACM ini harus di-review ulang (misalnya: setiap ada perubahan peran atau penambahan fitur baru). → Jika belum ada, catat sebagai `[MISSING_REVIEW_POLICY]` dan tambahkan sub-bab singkat.

---

### 🟡 LANGKAH 4 — VALIDASI KESIAPAN SEBAGAI REFERENSI FASE BERIKUTNYA

> **Tujuan**: Memastikan dokumen ACM dapat langsung digunakan sebagai input Fase 03 Design tanpa dipertanyakan lagi.

- [ ] **4.1** Simulasikan dirimu sebagai **developer yang akan mengimplementasikan decorator `@require_role` Python** berdasarkan dokumen ACM ini.
  Periksa apakah informasi berikut sudah tersedia dengan jelas dan tidak ambigu:
  - Nama kode peran yang harus digunakan sebagai parameter decorator (contoh: `@require_role(['kasir', 'pramuniaga'])`). → Cek di Bab 2.1 kolom "Kode Peran Sistem".
  - Daftar menu/fungsi yang harus diproteksi beserta ID-nya. → Cek di Bab 3.1.
  - Hak akses spesifik per peran per menu. → Cek di Bab 4.
  - Pesan error yang harus ditampilkan jika akses ditolak. → Cek di Bab 6.
  - Jika ada informasi yang **tidak jelas** atau **tidak ditemukan**, catat sebagai `[MISSING_IMPL_INFO]`.

- [ ] **4.2** Simulasikan dirimu sebagai **DBA (Database Administrator) yang akan mengimplementasikan hak akses level database** berdasarkan Bab 5.2 ACM.
  Periksa apakah informasi berikut sudah tersedia:
  - Nama tabel yang tepat (harus sama persis dengan Data Dictionary).
  - Operasi CRUD yang diizinkan per peran per tabel.
  - Catatan tentang operasi yang dilakukan oleh sistem secara otomatis (`*`).
  - Jika ada ambiguitas, catat sebagai `[DB_IMPL_AMBIGUITY]`.

- [ ] **4.3** Simulasikan dirimu sebagai **QA Engineer yang akan menulis test cases untuk penetration testing RBAC** berdasarkan dokumen ACM ini.
  Periksa apakah dokumen ini sudah memberikan cukup informasi untuk membuat test case:
  - Test case "positive path": Peran yang berhak → harus ALLOWED.
  - Test case "negative path": Peran yang tidak berhak → harus DENIED dengan pesan error yang spesifik.
  - Test case eskalasi: Operasi eskalasi → harus meminta sandi supervisor, salah → tampil ERR code yang tepat, benar → dieksekusi.
  - Jika ada test case yang tidak bisa dibuat karena informasi di ACM tidak cukup, catat sebagai `[TESTABILITY_GAP]`.

- [ ] **4.4** Periksa apakah **Bab 8 (Traceability Matrix)** sudah mencakup semua dimensi ketertelusuran yang dibutuhkan:
  - Apakah ada pemetaan **ACM ↔ Data Dictionary** yang menunjukkan bahwa setiap tabel di CRUD Matrix (Bab 5) berasal dari Data Dictionary? → Jika tidak ada, pertimbangkan untuk **menambahkan sub-bab 8.4** khusus pemetaan ini.
  - Apakah ada pemetaan **ACM ↔ Workflow Diagram** yang menunjukkan bahwa setiap diagram otorisasi di Bab 7 berasal dari Workflow Diagram? → Jika tidak ada, pertimbangkan untuk **menambahkan sub-bab 8.5** khusus pemetaan ini.

---

### 🟡 LANGKAH 5 — VALIDASI BAHASA INDONESIA (KEJELASAN DAN KETERBACAAN)

> **Tujuan**: Memastikan setiap kalimat dan istilah dalam dokumen tidak ambigu dan mudah dipahami.

- [ ] **5.1** Baca ulang setiap paragraf naratif (bukan tabel/kode) di dokumen ACM.
  Tandai setiap kalimat yang:
  - Menggunakan kata atau frasa yang maknanya bisa ditafsirkan lebih dari satu cara → Catat sebagai `[AMBIGUOUS_SENTENCE]`.
  - Menggunakan campuran bahasa Inggris dan Indonesia yang tidak konsisten tanpa alasan yang jelas → Catat sebagai `[INCONSISTENT_LANGUAGE_MIXING]`.
  - Terlalu panjang (lebih dari 40 kata dalam satu kalimat) sehingga sulit dipahami → Catat sebagai `[OVERLY_LONG_SENTENCE]` dan pecah menjadi dua kalimat.

- [ ] **5.2** Periksa apakah terminologi teknis yang digunakan **konsisten** di seluruh dokumen:
  - "Hak Akses", "Otorisasi", "Izin" → Apakah digunakan secara konsisten untuk makna yang sama? Pilih satu istilah utama dan gunakan secara konsisten.
  - "Peran", "Role" → Apakah ada pencampuran yang membingungkan? Tetapkan konvensi.
  - "Eskalasi", "Supervisor Approval" → Pastikan konsisten.

- [ ] **5.3** Periksa apakah **Catatan Keamanan** di kolom terakhir setiap tabel matriks Bab 4:
  - Ditulis dengan kalimat yang jelas, singkat, dan tidak ambigu.
  - Menggunakan kata kerja aktif, bukan pasif yang membingungkan.
  - Konsisten dalam penggunaan tanda baca (titik, koma, tanda kurung).

- [ ] **5.4** Periksa ejaan dan tata bahasa Indonesia yang benar menggunakan kaidah KBBI:
  - Kata-kata yang sering salah dieja: "berulang" bukan "berulang-ulang" (jika reduplikasi tidak diperlukan), "diotorisasi" bukan "di-otorisasi", dll.
  - Kata depan yang harus disambung: "di" sebagai kata depan (di tabel, di database) harus dipisah dari kata benda.
  - Kata depan yang harus dipisah: "di-" sebagai awalan verba harus disambung (dicatat, diproses).

---

### 🟡 LANGKAH 6 — VALIDASI KUALITAS DAN KELENGKAPAN KONTEN (ZERO-INTERRUPT QUALITY)

> **Tujuan**: Memastikan dokumen ACM tidak akan dipertanyakan atau diinterupsi oleh engineer yang menggunakannya.

- [ ] **6.1** Verifikasi **Statistik Numerik di Bab 9** secara matematis manual:
  - Untuk setiap baris peran di Tabel Bab 9, hitung secara manual berapa menu yang dapat diakses (bukan `⛔ DENY`) dari seluruh tabel matriks di Bab 4 (M.1 s.d M.10 + BASE).
  - Total menu = 6 (M1) + 10 (M2) + 3 (M3) + 4 (M4) + 3 (M5) + 5 (M6) + 6 (M7) + 1 (M8) + 1 (M9) + 1 (M10) + 4 (BASE) = 44 menu.
  - Hitung satu per satu untuk setiap peran dan bandingkan dengan angka di Tabel Bab 9.
  - Khususnya periksa perhitungan `kasir` (diklaim 20/44 = 45.5%), `kepala_percetakan` (diklaim 18/44 = 40.9%), dan `fotocopy_print` (diklaim 6/44 = 13.6%).
  - Jika ada angka yang tidak cocok, catat sebagai `[STATS_CALCULATION_ERROR]` beserta koreksinya.

- [ ] **6.2** Verifikasi **Statistik Tabel CRUD di Bab 9** secara manual:
  - Untuk setiap baris peran di Tabel Bab 9, hitung secara manual berapa tabel yang dapat diakses (minimal satu operasi CRUD yang bukan `-`) dari Matriks CRUD Bab 5.2.
  - Total tabel = 28 tabel.
  - Bandingkan hasil perhitungan manual dengan angka di kolom "Jumlah Tabel DB Diakses (CRUD)" Tabel Bab 9.
  - Jika ada angka yang tidak cocok, catat sebagai `[DB_STATS_CALCULATION_ERROR]` beserta koreksinya.

- [ ] **6.3** Verifikasi konsistensi **simbol hak akses** di seluruh Bab 4:
  - Semua simbol yang digunakan harus berasal dari legenda di Bab 1.6 dan Bab 4.1.
  - Apakah ada simbol yang tidak tercantum di legenda tetapi digunakan di tabel? → Catat sebagai `[UNDEFINED_SYMBOL]`.
  - Apakah ada variasi penulisan simbol yang berbeda untuk makna yang sama (misalnya `📝+📖` vs `📝 + 📖`)? → Standarisasi menjadi satu penulisan yang konsisten.

- [ ] **6.4** Periksa **Bab 3.3 — Fungsi/Operasi Bisnis Kritis**:
  - Apakah semua operasi kritis yang terdaftar di Bab 3.3 sudah memiliki **aturan eskalasi yang terdefinisi** di Bab 6.1 atau Bab 6.2?
  - Jika ada operasi kritis di Bab 3.3 yang **tidak ada** di Bab 6.1 atau 6.2, catat sebagai `[CRITICAL_OP_WITHOUT_ESCALATION_RULE]`.

- [ ] **6.5** Periksa apakah **Matriks CRUD Bab 5.2** memiliki catatan yang cukup informatif di kolom terakhir untuk setiap tabel:
  - Apakah catatan integritas data menjelaskan secara singkat mengapa hak akses tersebut diberikan demikian?
  - Apakah tabel yang memiliki operasi otomatis (`*`) sudah mencantumkannya dan sudah dijelaskan dipicu oleh apa?
  - Jika ada tabel yang catatannya terlalu singkat atau tidak ada, catat sebagai `[MISSING_TABLE_NOTE]` dan isi dengan catatan yang relevan.

- [ ] **6.6** Periksa **konsistensi lintas-referensi internal** di dalam dokumen ACM sendiri:
  - Apakah ID menu di Bab 3.1 (`MENU-M1-001`) konsisten dengan ID yang digunakan di Bab 4 (ditulis `M1-001` tanpa prefix `MENU-`)? Apakah inkonsistensi ini disengaja atau perlu distandarisasi?
  - Apakah ID ACM Entry (`ACM-M1-001`) di Tabel 8.1, 8.2, dan 8.3 konsisten untuk entri yang sama?
  - Jika ada inkonsistensi, catat sebagai `[INTERNAL_REFERENCE_INCONSISTENCY]` dan pilih satu format yang konsisten.

---

### 🟡 LANGKAH 7 — VALIDASI DATA KOSONG DAN PENISIAN DATA

> **Tujuan**: Memastikan tidak ada placeholder, tanda tanya, atau data kosong yang belum diisi.

- [ ] **7.1** Scan seluruh dokumen ACM dari baris pertama hingga terakhir untuk mencari:
  - Sel tabel yang kosong (tidak ada nilai sama sekali) → Catat baris dan kolom yang kosong.
  - Teks placeholder seperti `[TODO]`, `[TBD]`, `[FILL IN]`, `N/A`, `...`, `???` → Catat sebagai `[EMPTY_PLACEHOLDER]`.
  - Komentar yang belum dihapus seperti `<!-- TODO: ... -->` → Catat sebagai `[UNFILLED_COMMENT]`.

- [ ] **7.2** Untuk setiap data kosong yang ditemukan di Langkah 7.1, isi dengan data yang sesuai dan relevan:
  - Isi berdasarkan informasi dari dokumen referensi (BRD, SRS, UCD, WFD, Data Dictionary).
  - Jika tidak ada referensi yang tersedia, isi berdasarkan konteks bisnis AbuCom yang sudah dipahami.
  - Jangan biarkan ada data kosong yang tidak terisi setelah langkah ini.

- [ ] **7.3** Periksa apakah ada **nilai hak akses yang tidak konsisten** antara Bab 4 (Matriks Menu) dengan Bab 5 (Matriks CRUD):
  - Contoh: Jika di Bab 4 peran `pramuniaga` diberi `📝 INPUT` untuk menu M1-001 (Mencatat Transaksi), maka di Bab 5.2 tabel `transaksi`, peran `pramuniaga` harus minimal memiliki `C` (Create). Jika tidak konsisten, ini adalah anomali yang harus diperbaiki.
  - Lakukan pengecekan ini untuk semua menu yang memiliki hak akses bukan `⛔ DENY`.

- [ ] **7.4** Periksa apakah **Bab 6.3 — Aturan Pembatasan Akses Data Sensitif** sudah cukup spesifik:
  - Apakah kolom `whatsapp` yang disebutkan dienkripsi sudah jelas nama tabel dan nama kolomnya? → Harus menyebutkan tabel `pelanggan` kolom `whatsapp`.
  - Apakah disebutkan teknik enkripsi yang digunakan secara spesifik? → Harus menyebutkan modul `cryptography` Python dengan teknik Fernet symmetric encryption (atau teknik spesifik lainnya sesuai SRS).
  - Jika kurang spesifik, tambahkan detail yang diperlukan.

---

### 🟡 LANGKAH 8 — PEMERIKSAAN TAMBAHAN SPESIFIK DOKUMEN ACM

> **Tujuan**: Memeriksa aspek-aspek yang bersifat khas dan unik untuk dokumen ACM, yang tidak tercantum di instruksi umum.

- [ ] **8.1** **Verifikasi Prinsip Least Privilege**: Untuk setiap peran di Level 3 (Staf Operasional), lakukan spot-check:
  - Apakah ada peran yang mendapat hak akses `✅ FULL` untuk menu yang seharusnya tidak perlu akses penuh?
  - Contoh: `pramuniaga` mendapat `📝 INPUT` untuk menu Transaksi (membuat transaksi baru) — ini benar karena pramuniaga membuat pesanan, tetapi tidak seharusnya mendapat `✅ FULL` (yang artinya bisa menghapus transaksi orang lain).
  - Tandai setiap potensi pelanggaran Least Privilege sebagai `[LEAST_PRIVILEGE_VIOLATION]`.

- [ ] **8.2** **Verifikasi Prinsip Separation of Duties**: Identifikasi pasangan peran yang berpotensi kolusi jika diberi hak akses yang terlalu tumpang tindih:
  - Apakah `kasir` dan `pramuniaga` tidak memiliki overlap hak akses yang memungkinkan satu orang mengelola transaksi end-to-end tanpa pengawasan?
  - Apakah `gudang` tidak memiliki hak akses ke modul keuangan (`transaksi`, `payroll`, `pengeluaran`) yang memungkinkan penyalahgunaan?
  - Tandai setiap potensi pelanggaran Separation of Duties sebagai `[SOD_VIOLATION]`.

- [ ] **8.3** **Verifikasi Konsistensi Diagram Mermaid**: Baca ulang semua 5 diagram Mermaid di Bab 2.2 dan Bab 7.
  - Apakah **sintaks Mermaid** setiap diagram valid (tidak ada error yang akan menyebabkan diagram tidak ter-render)?
  - Apakah label pada diagram menggunakan bahasa yang konsisten?
  - Apakah kondisi `alt/else` dan `if/else` pada diagram sequence/flowchart sudah mencakup semua kemungkinan path (happy path dan error path)?
  - Jika ada diagram yang tidak lengkap pathnya, catat sebagai `[INCOMPLETE_DIAGRAM_PATH]` dan lengkapi.

- [ ] **8.4** **Verifikasi Penomoran dan Urutan Konsistensi**:
  - Apakah ID menu di Bab 3.1 sudah berurutan dan tidak ada nomor yang terlewat atau duplikat?
  - Apakah nomor bab sudah berurutan (1, 2, 3, ... 11) tanpa ada yang terlewat?
  - Apakah ID ACM Entry di Tabel 8.1, 8.2, 8.3 sudah berurutan dari M1-001 hingga M10-001 kemudian BASE-001 hingga BASE-004?
  - Jika ada yang tidak berurutan atau ada duplikat, catat sebagai `[NUMBERING_ERROR]` dan perbaiki.

- [ ] **8.5** **Verifikasi Kelengkapan Tabel Bab 9 (Ringkasan Statistik)**:
  - Apakah Tabel Bab 9 sudah memiliki semua 8 baris peran?
  - Apakah kolom "Keterangan Batasan Keamanan" sudah informatif dan mendeskripsikan konteks keamanan masing-masing peran dengan tepat?
  - Apakah angka-angka di bawah tabel (Total Operasi Kritis, Total Operasi Verifikasi, Tabel Eksklusif Pemilik) sudah akurat? Verifikasi dengan menghitung dari Bab 6.1 dan Bab 6.2.

- [ ] **8.6** **Verifikasi Tabel Referensi di Bab 11**:
  - Apakah semua 7 dokumen referensi yang terdaftar di Bab 11 benar-benar digunakan/dirujuk di dalam body dokumen ACM?
  - Apakah path file referensi sudah benar (path relatif dari root proyek)?
  - Apakah versi dokumen referensi (misalnya "v1.1") sudah sesuai dengan versi dokumen referensi yang aktual?
  - Jika ada referensi yang tidak dirujuk dalam body, pertimbangkan untuk menghapus atau justru menambahkan rujukan ke body dokumen.

- [ ] **8.7** **Verifikasi Keamanan Data Sensitif di Bab 3.2** (Kategorisasi Sensitivitas Tabel):
  - Periksa apakah tabel `aset` sudah dikategorikan dengan benar (saat ini ada di Bab 5.2 baris 24 dengan semua akses `CRUD / ---- / ---- / ...`). Apakah ini sudah konsisten dengan kategori sensitivitas di Bab 3.2?
  - Periksa apakah tabel `audit_logs` yang merupakan tabel sangat sensitif memang hanya bisa dilihat oleh `pemilik` di seluruh ACM.
  - Catat setiap inkonsistensi sebagai `[SENSITIVITY_CATEGORIZATION_ERROR]`.

---

### 🔴 LANGKAH 9 — KONSOLIDASI TEMUAN DAN PERENCANAAN PERBAIKAN

> **Tujuan**: Membuat ringkasan semua temuan dan menetapkan tindakan perbaikan sebelum menulis ulang dokumen.

- [ ] **9.1** Kumpulkan semua catatan temuan dari Langkah 1 hingga 8 ke dalam satu daftar konsolidasi.
  Untuk setiap temuan, tentukan:
  - **Jenis Temuan** (kode temuan seperti `[MISSING_TABLE]`, `[STATS_CALCULATION_ERROR]`, dll.)
  - **Lokasi** (Bab berapa, baris berapa, atau tabel mana)
  - **Deskripsi Masalah** (apa yang salah/hilang)
  - **Tindakan Perbaikan** (apa yang harus dilakukan untuk memperbaikinya)
  - **Tingkat Keparahan** (Critical / High / Medium / Low)

- [ ] **9.2** Tentukan urutan perbaikan berdasarkan tingkat keparahan:
  - **Critical**: Data salah yang berdampak langsung pada implementasi kode (error kode ERR salah, statistik sangat meleset, peran tidak konsisten).
  - **High**: Data hilang yang menyebabkan gap implementasi.
  - **Medium**: Inkonsistensi yang bisa membingungkan.
  - **Low**: Masalah kosmetik (ejaan, tanda baca, format).

- [ ] **9.3** Jika ada temuan tambahan referensi baru yang harus ditambahkan (file yang dirujuk dalam perbaikan tetapi belum ada di Bab 11), catat file referensi baru tersebut beserta path dan alasan penambahannya.

---

### 🔴 LANGKAH 10 — PENULISAN ULANG DOKUMEN (OVERWRITE TARGET FILE)

> **PERINGATAN KRITIS**: Langkah ini hanya boleh dimulai setelah **seluruh** Langkah 0 hingga 9 selesai dikerjakan dan semua perbaikan sudah ditetapkan. Jangan menulis ulang dokumen secara parsial atau bertahap per bagian.

- [ ] **10.1** Siapkan konten lengkap dokumen baru yang telah diperbaiki secara menyeluruh di memori/scratch:
  - Versi dokumen harus **diubah** dari versi saat ini (misal `v1.1` menjadi `v1.2`) di header YAML frontmatter.
  - Tanggal dokumen harus **diperbarui** menjadi tanggal pelaksanaan tugas ini.
  - Entri baru harus **ditambahkan** di Tabel Riwayat Perubahan dengan deskripsi yang merangkum semua perubahan yang dilakukan.

- [ ] **10.2** **Tulis ulang (overwrite) file target secara penuh dan atomik**:
  - Path target: `docs/sdlc/02_analysis/06_access_control_matrix.md`
  - **WAJIB**: Tulis ulang **seluruh isi dokumen dari baris pertama hingga baris terakhir** dalam satu operasi tulis.
  - **DILARANG KERAS**: Memotong (truncate), meringkas, atau menghilangkan bagian manapun dari dokumen yang sudah ada.
  - **DILARANG KERAS**: Hanya menimpa sebagian baris. Harus overwrite seluruh file.
  - **DILARANG KERAS**: Mengganti tabel dengan kalimat ringkasan seperti "Data sama seperti sebelumnya".
  - Seluruh tabel matriks Bab 4 (44 baris use case) dan Bab 5 (28 baris tabel CRUD) **wajib** ditulis ulang lengkap, bukan diringkas.
  - Seluruh diagram Mermaid **wajib** ditulis ulang lengkap, bukan diringkas.

- [ ] **10.3** Setelah overwrite selesai, lakukan **verifikasi pasca-tulis**:
  - Buka kembali file yang baru ditulis.
  - Periksa apakah baris pertama adalah header YAML frontmatter yang benar.
  - Periksa apakah versi sudah berubah (contoh: dari `v1.1` menjadi `v1.2`).
  - Periksa apakah Tabel Riwayat Perubahan sudah memiliki entri baru.
  - Periksa apakah baris terakhir adalah Tabel Referensi Bab 11 yang lengkap (tidak terpotong).
  - Hitung total baris file baru dan pastikan jumlahnya **lebih banyak atau sama** dengan file sebelumnya (751 baris). Jika lebih sedikit, file kemungkinan terpotong → **ULANGI LANGKAH 10.2**.

---

### 🔴 LANGKAH 11 — PEMBARUAN REFERENSI BARU (JIKA ADA)

> **Tujuan**: Memastikan setiap referensi baru yang digunakan dalam perbaikan dokumen dicatat di Bab 11.

- [ ] **11.1** Periksa kembali daftar temuan dari Langkah 9.3 — apakah ada dokumen referensi baru yang digunakan selama proses perbaikan yang belum ada di Tabel Bab 11?

- [ ] **11.2** Jika ada referensi baru, **tambahkan** baris baru di Tabel Bab 11 (Referensi Dokumen) di bagian **paling bawah** tabel, dengan format:
  ```
  | [Nomor urut] | `[nama_file.md]` | `docs/sdlc/[path/ke/file.md]` | [Nama Dokumen] v[Versi] — [Alasan penambahan referensi ini]. |
  ```

- [ ] **11.3** Pastikan setelah penambahan referensi baru, file target sudah di-overwrite ulang (kembali ke Langkah 10.2) untuk memasukkan pembaruan Tabel Bab 11 ke dalam file.

---

## 5. Kriteria Penerimaan (Definition of Done)

Issue ini dianggap **selesai dan tuntas (DONE)** hanya jika seluruh kondisi berikut terpenuhi:

- [ ] **DOD-01**: Semua checklist dari Langkah 0 hingga 11 sudah ditandai `[x]` (selesai dikerjakan).
- [ ] **DOD-02**: File `docs/sdlc/02_analysis/06_access_control_matrix.md` sudah berisi versi terbaru (minimal `v1.2`).
- [ ] **DOD-03**: Tabel Riwayat Perubahan di dokumen sudah mencantumkan entri baru yang deskriptif untuk versi terbaru.
- [ ] **DOD-04**: Semua inkonsistensi data yang ditemukan antara ACM dan dokumen referensi sudah diperbaiki.
- [ ] **DOD-05**: Semua statistik numerik di Bab 9 sudah diverifikasi kebenarannya secara matematis.
- [ ] **DOD-06**: Semua kode error (`ERR-xxx`) di Bab 6 sudah diselaraskan dengan SRS.
- [ ] **DOD-07**: Tidak ada sel tabel yang kosong, placeholder, atau data yang belum diisi.
- [ ] **DOD-08**: Dokumen ditulis ulang **secara penuh tanpa truncation** dari baris pertama hingga terakhir.
- [ ] **DOD-09**: Jika ada referensi baru yang digunakan, sudah dicantumkan di Tabel Bab 11.
- [ ] **DOD-10**: Dokumen menggunakan bahasa Indonesia yang natural, tidak ambigu, dan konsisten di seluruh bagian.

---

## 6. Batasan Pekerjaan (Out of Scope)

Hal-hal berikut **TIDAK boleh dilakukan** dalam issue ini:

- ❌ Menambahkan peran baru yang belum ada di dokumen referensi BRD.
- ❌ Menambahkan modul atau menu baru yang belum ada di UCD atau BRD.
- ❌ Mengubah kebijakan bisnis (seperti mengubah threshold Rp 500.000 untuk eskalasi pengeluaran).
- ❌ Menulis ulang file referensi (BRD, SRS, UCD, WFD, Data Dictionary) — hanya file target ACM yang boleh dimodifikasi.
- ❌ Menambahkan bab baru yang tidak relevan dengan cakupan dokumen ACM (misalnya menambahkan panduan instalasi atau deployment).

---

## 7. Peringatan Anti-Halusinasi

> ⛔ **BACA DAN PATUHI DENGAN KETAT**

1. **JANGAN mengarang data** yang tidak ada di dokumen referensi. Semua data harus bersumber dari salah satu dari 7 file referensi yang disebutkan di Bagian 3.
2. **JANGAN mengisi kolom hak akses** berdasarkan asumsi logis semata. Setiap penetapan hak akses harus dapat ditelusuri ke BRD, SRS, atau UCD sebagai justifikasi.
3. **JANGAN meringkas tabel** dengan alasan "terlalu panjang". Seluruh tabel harus ditulis lengkap.
4. **JANGAN berhenti di tengah penulisan**. Jika kapasitas konteks hampir habis, selesaikan bab yang sedang dikerjakan terlebih dahulu sebelum berhenti.
5. **JANGAN mengubah kode error** (`ERR-xxx`) kecuali kamu sudah membaca dan memverifikasi dari `02_software_requirements.md` bahwa kode tersebut memang salah.
6. **JANGAN mengubah nilai hak akses** (mengubah `⛔ DENY` menjadi `✅ FULL` atau sebaliknya) kecuali kamu sudah menemukan bukti inkonsistensi yang jelas dari dokumen referensi.
7. **JANGAN menghilangkan diagram Mermaid**. Jika diagram sudah ada dan benar secara konten, pertahankan. Hanya perbaiki jika ada error sintaks atau konten yang tidak akurat.

---

## 8. Referensi Tambahan untuk Pelaksana

- Panduan RBAC industri: [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) (sebagai referensi konsep, bukan implementasi wajib)
- Panduan UU PDP Indonesia: UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi
- Standar dokumentasi keamanan: OWASP Security Documentation Best Practices
- Format kode error yang digunakan proyek ini: Lihat `docs/sdlc/02_analysis/02_software_requirements.md` Bab Error Codes

---

*Issue ini dibuat pada: 2026-05-28 | Dibuat oleh: Antigravity AI (Senior Planning Agent) | Untuk dieksekusi oleh: Junior Programmer / AI Model*
