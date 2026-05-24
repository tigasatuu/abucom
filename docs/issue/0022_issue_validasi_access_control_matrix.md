---
judul     : Validasi, Analisis, dan Perbaikan Dokumen Access Control Matrix (ACM)
target    : docs/sdlc/02_analysis/06_access_control_matrix.md
prioritas : High
status    : Open
tanggal   : 2026-05-24
assignee  : Junior Programmer / LLM Agent
---

# Validasi, Analisis, dan Perbaikan Dokumen Access Control Matrix (ACM)

## Ringkasan Issue

Dokumen **Access Control Matrix (ACM)** pada path `docs/sdlc/02_analysis/06_access_control_matrix.md` (versi 1.0) perlu divalidasi secara menyeluruh dan ketat sebelum digunakan sebagai referensi utama bagi fase SDLC selanjutnya (Fase 03 Design). Validasi mencakup kelengkapan konten, akurasi komparasi terhadap file referensi, kualitas bahasa, kelengkapan struktur, serta kebergunaan dokumen sebagai input bagi dokumen-dokumen fase desain sistem.

---

## Persona yang Harus Diasumsikan

> **PENTING**: Kamu WAJIB mengerjakan seluruh issue ini dengan mengadopsi persona berikut secara konsisten dari awal hingga akhir.

Kamu adalah seorang **Senior Software Architect & RBAC Security Specialist** berpengalaman 15+ tahun yang memiliki keahlian gabungan di bidang:

- **Information Security Architecture**: Pakar dalam merancang sistem otorisasi Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), dan Zero Trust Architecture untuk sistem enterprise.
- **SDLC Documentation Expert**: Pakar dalam standar dokumentasi industri nyata (IEEE 830, ISO/IEC 25010, OWASP ASVS), terbiasa mengaudit dokumen persyaratan keamanan lintas fase SDLC (Analysis → Design → Testing).
- **Database Security Specialist**: Memahami implikasi keamanan pada level database (privilege separation, row-level security, audit trail) dan konsistensinya dengan dokumen ACM.
- **Compliance & Regulatory Expert**: Memahami implementasi kepatuhan UU Pelindungan Data Pribadi (UU PDP No. 27/2022) dalam konteks desain sistem informasi.
- **Technical Writer**: Mampu menilai kualitas bahasa Indonesia teknis yang tidak ambigu, natural, dan mudah dipahami oleh junior programmer maupun LLM AI generatif.

Dengan persona ini, kamu akan memeriksa, menganalisa, dan memvalidasi dokumen dengan **standar industri yang sesungguhnya** — tidak toleran terhadap ketidaklengkapan, ambiguitas, atau inkonsistensi data.

---

## Konteks Issue

### Informasi Dokumen Utama
- **Nama Dokumen** : Access Control Matrix (ACM)
- **Target File**   : `docs/sdlc/02_analysis/06_access_control_matrix.md`
- **Versi Saat Ini**: v1.0
- **Status Saat Ini**: Draft
- **Posisi SDLC**  : Dokumen ke-6 (terakhir) Fase 02 Analysis — menjadi input utama Fase 03 Design

### File Referensi yang Harus Dibaca
Dokumen utama ini secara eksplisit mendefinisikan sumber referensinya di Bab 11 (Referensi Dokumen). Seluruh file berikut **wajib** dibaca sebelum validasi:

| No | Nama File Referensi | Path Relatif |
|----|---------------------|--------------|
| 1  | Business Requirements Document (BRD) | `docs/sdlc/02_analysis/01_business_requirements.md` |
| 2  | Software Requirements Specification (SRS) | `docs/sdlc/02_analysis/02_software_requirements.md` |
| 3  | Use Case Diagram (UCD) | `docs/sdlc/02_analysis/03_use_case_diagram.md` |
| 4  | Workflow Diagram (WFD) | `docs/sdlc/02_analysis/04_workflow_diagram.md` |
| 5  | Data Dictionary | `docs/sdlc/02_analysis/05_data_dictionary.md` |
| 6  | Stakeholder Register | `docs/sdlc/01_planning/03_stakeholder_register.md` |
| 7  | Innovation Proposal | `docs/sdlc/01_planning/05_innovation_proposal.md` |

---

## Tahapan Implementasi (Step-by-Step — Low Level)

Ikuti setiap langkah di bawah ini **secara berurutan**. Tandai checklist `[x]` setelah setiap sub-tugas selesai dikerjakan. **Jangan melewati atau menggabungkan langkah.**

---

### FASE A — Persiapan: Pembacaan dan Pemahaman Konteks

#### A.1. Baca Dokumen Utama (Target File)

- [ ] **A.1.1** Buka dan baca seluruh isi file `docs/sdlc/02_analysis/06_access_control_matrix.md` dari baris pertama hingga terakhir tanpa ada bagian yang dilewati.
- [ ] **A.1.2** Catat dalam memori kerja: berapa bab utama yang ada, berapa total peran yang didefinisikan, berapa total use case yang dicantumkan, berapa total tabel database yang tercantum.
- [ ] **A.1.3** Identifikasi dan catat semua referensi dokumen yang disebutkan di dalam dokumen utama ini (lihat Bab 11 atau bagian Referensi).
- [ ] **A.1.4** Identifikasi dan catat semua data yang kosong, bertanda `[TBD]`, `[N/A]`, `[belum diisi]`, atau field yang memiliki nilai placeholder tidak valid.

#### A.2. Baca Seluruh File Referensi

- [ ] **A.2.1** Buka dan baca seluruh isi file `docs/sdlc/02_analysis/01_business_requirements.md`. Catat: jumlah total kebutuhan bisnis (BR-F-XXX), daftar lengkap 8 peran pengguna, dan tabel hak akses ringkas jika ada.
- [ ] **A.2.2** Buka dan baca seluruh isi file `docs/sdlc/02_analysis/02_software_requirements.md`. Catat: daftar lengkap SRS-F-XXX, parameter teknis JWT (algoritma, durasi), bcrypt (cost factor), rate limiting (jumlah percobaan, durasi suspensi), dan spesifikasi RBAC.
- [ ] **A.2.3** Buka dan baca seluruh isi file `docs/sdlc/02_analysis/03_use_case_diagram.md`. Catat: daftar lengkap seluruh Use Case (UC-XXX) dengan nama dan aktor yang terlibat. Verifikasi total jumlah use case.
- [ ] **A.2.4** Buka dan baca seluruh isi file `docs/sdlc/02_analysis/04_workflow_diagram.md`. Catat: seluruh alur kerja (workflow) yang didefinisikan beserta peran yang terlibat di setiap swimlane dan titik keputusan otorisasi.
- [ ] **A.2.5** Buka dan baca seluruh isi file `docs/sdlc/02_analysis/05_data_dictionary.md`. Catat: daftar lengkap 28 tabel database MySQL, nama kolom kritis per tabel, dan operasi CRUD yang diizinkan per tabel.
- [ ] **A.2.6** Buka dan baca seluruh isi file `docs/sdlc/01_planning/03_stakeholder_register.md`. Catat: daftar lengkap peran stakeholder internal dan eksternal beserta level Power/Interest-nya.
- [ ] **A.2.7** Buka dan baca seluruh isi file `docs/sdlc/01_planning/05_innovation_proposal.md`. Catat: seluruh parameter inovasi keamanan yang disebutkan (enkripsi, JWT, bcrypt, dll.) yang relevan dengan ACM.

---

### FASE B — Validasi: Komparasi Mendalam Dokumen Utama vs File Referensi

#### B.1. Komparasi: Peran Pengguna (Roles)

- [ ] **B.1.1** Bandingkan daftar 8 peran pengguna internal yang tercantum di Bab 2.1 dokumen utama dengan daftar peran yang ada di BRD (Bab 5.1 atau setara) dan Stakeholder Register. Pastikan nama peran, kode sistem, dan level hierarki konsisten di semua dokumen.
- [ ] **B.1.2** Periksa apakah ada peran yang disebutkan di BRD atau Stakeholder Register tetapi **tidak tercantum** di dokumen utama. Jika ada, catat sebagai temuan (FINDING).
- [ ] **B.1.3** Periksa apakah ada peran yang tercantum di dokumen utama tetapi **tidak ada** di BRD atau Stakeholder Register. Jika ada, catat sebagai temuan (FINDING).
- [ ] **B.1.4** Bandingkan daftar 4 aktor eksternal (ACT-EXT-01 s.d ACT-EXT-04) di Bab 2.3 dengan data aktor eksternal di BRD dan Stakeholder Register. Pastikan tidak ada aktor eksternal yang terlewat.

#### B.2. Komparasi: Use Case Coverage

- [ ] **B.2.1** Bandingkan daftar 44 Use Case yang ada di Bab 8.3 (Pemetaan ACM terhadap Use Case Diagram) dengan daftar lengkap use case di file `03_use_case_diagram.md`. Verifikasi apakah setiap UC-001 hingga UC-044 telah terpetakan.
- [ ] **B.2.2** Periksa apakah ada Use Case di `03_use_case_diagram.md` yang **belum** tercantum di Bab 4 (Matriks Kontrol Akses Utama) sebagai baris menu. Jika ada, catat sebagai temuan (FINDING).
- [ ] **B.2.3** Periksa apakah ada baris di Bab 4 (Matriks Akses) yang **tidak memiliki** kode UC yang sesuai di Bab 8.3. Jika ada, catat sebagai temuan (FINDING).
- [ ] **B.2.4** Verifikasi bahwa aktor/peran yang ditugaskan ke setiap Use Case di `03_use_case_diagram.md` konsisten dengan pemberian hak akses di Bab 4 dokumen utama.

#### B.3. Komparasi: Tabel Database (CRUD Matrix)

- [ ] **B.3.1** Buat daftar seluruh nama tabel dari `05_data_dictionary.md`. Bandingkan satu per satu dengan daftar 28 tabel yang ada di Bab 5.2 dokumen utama.
- [ ] **B.3.2** Periksa apakah ada tabel di Data Dictionary yang **tidak** tercantum di Bab 5.2 matriks CRUD. Jika ada, catat sebagai temuan (FINDING).
- [ ] **B.3.3** Periksa apakah ada tabel di Bab 5.2 yang **tidak ada** di Data Dictionary. Jika ada, catat sebagai temuan (FINDING).
- [ ] **B.3.4** Untuk setiap tabel yang ada, verifikasi apakah hak akses CRUD per peran di Bab 5.2 **konsisten logis** dengan definisi operasi yang diizinkan di Data Dictionary. Contoh: jika Data Dictionary mendefinisikan tabel `payroll` sebagai read-only untuk semua staf, pastikan Bab 5.2 mencerminkan hal tersebut.
- [ ] **B.3.5** Periksa konsistensi antara Bab 3.2 (Daftar Tabel yang Dilindungi berdasarkan sensitivitas) dengan hak akses aktual di Bab 5.2. Pastikan tabel kategori "Sangat Sensitif" benar-benar terkunci hanya untuk `pemilik`.

#### B.4. Komparasi: Parameter Teknis Keamanan

- [ ] **B.4.1** Bandingkan parameter teknis keamanan di Bab 6.4 (JWT: algoritma HS256, durasi 28.800 detik / 8 jam) dengan spesifikasi di SRS. Pastikan nilai numerik dan nama algoritma identik.
- [ ] **B.4.2** Bandingkan parameter bcrypt di Bab 6.5 (cost factor = 12) dengan nilai yang disebutkan di SRS. Pastikan nilainya konsisten.
- [ ] **B.4.3** Bandingkan parameter rate limiting di Bab 6.5 (maks 5 kali, suspensi 600 detik) dengan spesifikasi di SRS. Pastikan nilainya identik.
- [ ] **B.4.4** Bandingkan aturan eskalasi di Bab 6.1 dan 6.2 dengan alur kerja di `04_workflow_diagram.md`. Pastikan setiap operasi kritis yang memerlukan eskalasi di ACM ada swimlane-nya di Workflow Diagram dan vice versa.
- [ ] **B.4.5** Verifikasi bahwa kode error yang disebutkan di Bab 6.1 dan 6.2 (mis. `ERR-AUTH-003`, `ERR-AUTH-011`, `ERR-CASH-001`, dll.) **konsisten** dengan kode error yang didefinisikan di SRS.

#### B.5. Komparasi: Traceability Matrix (BRD & SRS)

- [ ] **B.5.1** Verifikasi Bab 8.1 (Pemetaan ACM terhadap BRD): Pastikan setiap `BR-F-XXX` yang dirujuk benar-benar **ada dan bernomor sama** di file `01_business_requirements.md`. Jika ada nomor yang tidak cocok, catat sebagai temuan (FINDING).
- [ ] **B.5.2** Verifikasi Bab 8.2 (Pemetaan ACM terhadap SRS): Pastikan setiap `SRS-F-XXX` yang dirujuk benar-benar **ada dan bernomor sama** di file `02_software_requirements.md`. Jika ada nomor yang tidak cocok, catat sebagai temuan (FINDING).
- [ ] **B.5.3** Periksa apakah ada `BR-F-XXX` di BRD yang **tidak tercantum** di Bab 8.1. Jika ada requirement bisnis yang belum terpetakan di ACM, catat sebagai temuan kritis (CRITICAL FINDING).
- [ ] **B.5.4** Periksa apakah ada `SRS-F-XXX` di SRS yang **tidak tercantum** di Bab 8.2. Jika ada, catat sebagai temuan (FINDING).

#### B.6. Komparasi: Workflow Mapping

- [ ] **B.6.1** Cocokkan 5 diagram alur otorisasi Mermaid di Bab 7 dengan alur kerja yang ada di `04_workflow_diagram.md`. Pastikan tidak ada alur otorisasi kritis yang diagramkan di WFD tetapi **tidak direpresentasikan** di Bab 7 ACM.
- [ ] **B.6.2** Periksa apakah diagram Mermaid di Bab 7 menggunakan nama peran yang konsisten dengan Bab 2.1 (gunakan `kode_peran` yang sama persis, bukan nama alternatif).
- [ ] **B.6.3** Verifikasi apakah ada alur otorisasi penting lainnya yang belum terwakili di Bab 7 namun perlu ditambahkan berdasarkan temuan dari WFD.

---

### FASE C — Validasi: Pemeriksaan Standar Dokumen Industri

#### C.1. Pemeriksaan Kelengkapan Struktur Dokumen

- [ ] **C.1.1** Verifikasi apakah front matter (YAML header: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`) sudah terisi semua dan bernilai valid (tidak ada yang kosong atau placeholder).
- [ ] **C.1.2** Periksa apakah tabel **Riwayat Perubahan Dokumen** (Changelog) sudah terisi lengkap dengan kolom: Versi, Tanggal, Perubahan, Oleh. Pastikan tidak ada baris yang kosong.
- [ ] **C.1.3** Verifikasi bahwa Bab 1 (Informasi Dokumen) mencakup minimal: Tujuan, Cakupan, Posisi dalam SDLC, Hubungan dengan Dokumen Lain, Audiens Target, dan Konvensi Notasi.
- [ ] **C.1.4** Verifikasi bahwa Bab 2 (Definisi Subjek Akses) mencakup: daftar peran internal dengan ID, nama, kode, deskripsi, level hierarki; diagram hierarki; dan daftar aktor eksternal.
- [ ] **C.1.5** Verifikasi bahwa Bab 3 (Definisi Objek Akses) mencakup: daftar menu CLI per modul, daftar tabel database dengan kategorisasi sensitivitas, dan daftar fungsi/operasi bisnis kritis.
- [ ] **C.1.6** Verifikasi bahwa Bab 4 (Matriks Kontrol Akses Utama) memiliki sub-bab untuk **setiap** modul (M.1 s.d M.10) dan Use Case Dasar, serta kolom `Catatan Keamanan / Khusus` terisi di setiap baris.
- [ ] **C.1.7** Verifikasi bahwa Bab 5 (Matriks Akses Level Database) memiliki tabel CRUD yang mencakup semua 28 tabel dengan penjelasan di kolom `Catatan Integritas Data` untuk setiap baris.
- [ ] **C.1.8** Verifikasi bahwa Bab 6 (Aturan Otorisasi Khusus dan Eskalasi) memiliki semua sub-bab: Eskalasi Pemilik, Verifikasi Kepala Percetakan, Pembatasan Data Sensitif, Aturan Session JWT, Rate Limiting, dan Audit Trail Pelanggaran.
- [ ] **C.1.9** Verifikasi bahwa Bab 7 (Workflow Mapping) berisi minimal 5 diagram Mermaid untuk alur otorisasi kritis.
- [ ] **C.1.10** Verifikasi bahwa Bab 8 (Traceability Matrix) memiliki pemetaan ke BRD, SRS, dan Use Case Diagram.
- [ ] **C.1.11** Verifikasi bahwa Bab 9 (Ringkasan Statistik) berisi tabel kuantitatif yang mencakup semua 8 peran pengguna.
- [ ] **C.1.12** Verifikasi bahwa Bab 10 (Glosarium) mendefinisikan semua istilah teknis kunci yang digunakan dalam dokumen.
- [ ] **C.1.13** Verifikasi bahwa Bab 11 (Referensi Dokumen) mencantumkan semua file referensi dengan path relatif yang benar.

#### C.2. Pemeriksaan Data Kosong dan Placeholder

- [ ] **C.2.1** Cari di seluruh dokumen apakah ada sel tabel yang kosong (tidak ada nilai apa pun, atau hanya berisi spasi) di kolom yang seharusnya terisi. Jika ada, catat lokasi pastinya (nama bab, nomor baris tabel).
- [ ] **C.2.2** Cari di seluruh dokumen apakah ada teks placeholder seperti `[TBD]`, `[TODO]`, `[PLACEHOLDER]`, `[...segera diisi...]`, atau sejenisnya. Jika ada, catat lokasi pastinya.
- [ ] **C.2.3** Periksa kolom `Catatan Keamanan / Khusus` di setiap baris matriks Bab 4. Pastikan tidak ada baris yang memiliki catatan kosong atau hanya bertuliskan `-`.
- [ ] **C.2.4** Periksa kolom `Catatan Integritas Data` di setiap baris matriks Bab 5.2. Pastikan tidak ada baris yang memiliki catatan kosong.
- [ ] **C.2.5** Periksa tabel statistik di Bab 9. Verifikasi apakah angka jumlah fungsi CLI dan jumlah tabel DB yang dapat diakses per peran sudah **akurat** dengan menghitung secara manual dari Bab 4 dan Bab 5.

#### C.3. Pemeriksaan Konsistensi Internal Dokumen

- [ ] **C.3.1** Periksa apakah simbol akses di Bab 4 sesuai dengan legenda yang didefinisikan di Bab 1.6 dan Bab 4.1. Tidak boleh ada simbol yang digunakan tanpa didefinisikan di legenda.
- [ ] **C.3.2** Periksa apakah semua `ID Menu` yang disebut di Bab 3.1 (mis. `MENU-M1-001`) memiliki baris yang sesuai di Bab 4 (mis. `M1-001`). Pastikan tidak ada menu yang didaftar di Bab 3.1 tetapi tidak ada di Bab 4 dan vice versa.
- [ ] **C.3.3** Periksa konsistensi antara kategori sensitivitas tabel di Bab 3.2 dengan hak akses CRUD di Bab 5.2. Jika Bab 3.2 menyatakan suatu tabel "Sangat Sensitif (Pemilik Sahaja)", maka di Bab 5.2 semua kolom selain `pemilik` harus bernilai `----`.
- [ ] **C.3.4** Verifikasi bahwa jumlah use case yang disebutkan di Bab 1.2 (Cakupan Dokumen) konsisten dengan jumlah aktual baris di Bab 4 dan jumlah baris di Bab 8.3.
- [ ] **C.3.5** Verifikasi bahwa jumlah tabel database yang disebutkan di Bab 1.2 (28 tabel) konsisten dengan jumlah aktual baris di Bab 5.2 dan daftar di Bab 3.2.

---

### FASE D — Validasi: Kelayakan Dokumen sebagai Input SDLC Fase Selanjutnya

#### D.1. Pemeriksaan Kecukupan sebagai Input Fase 03 Design

- [ ] **D.1.1** Evaluasi apakah Bab 4 (Matriks Akses Menu CLI) sudah cukup detail dan tidak ambigu untuk dijadikan pedoman implementasi decorator `@require_role` di Python oleh developer junior. Pertimbangkan: apakah setiap baris menu memiliki informasi yang cukup untuk menentukan daftar role yang diizinkan (`ALLOWED_ROLES = [...]`)?
- [ ] **D.1.2** Evaluasi apakah Bab 5 (Matriks CRUD Database) sudah cukup detail untuk dijadikan pedoman implementasi data access layer di Python. Pertimbangkan: apakah notasi CRUD per tabel per peran sudah cukup untuk membuat query SQL terparameterisasi yang aman?
- [ ] **D.1.3** Evaluasi apakah Bab 6 (Aturan Otorisasi Khusus) sudah menyediakan semua informasi yang dibutuhkan untuk mengimplementasikan logika eskalasi password Pemilik dalam kode Python. Pertimbangkan: apakah alur verifikasi sudah cukup jelas (input → verifikasi bcrypt → sukses/gagal → efek)?
- [ ] **D.1.4** Evaluasi apakah Bab 7 (Workflow Mapping) menyediakan diagram alur yang cukup untuk panduan pembuatan Test Plan & Test Cases fase pengujian. Pertimbangkan: apakah semua skenario positif dan negatif (happy path & error path) sudah tergambar di diagram?
- [ ] **D.1.5** Evaluasi apakah ada celah informasi di dokumen ini yang **pasti akan menghambat** pekerjaan fase selanjutnya (Design atau Testing) karena informasi kritis tidak tersedia. Jika ada, catat sebagai CRITICAL FINDING dan wajib diperbaiki.

#### D.2. Pemeriksaan Kelayakan sebagai Dokumen Audit Keamanan

- [ ] **D.2.1** Evaluasi apakah dokumen ini sudah cukup membuktikan kepatuhan terhadap prinsip **Least Privilege** dengan adanya tabel matriks yang menunjukkan pembatasan akses minimum per peran.
- [ ] **D.2.2** Evaluasi apakah dokumen ini sudah cukup membuktikan implementasi **Separation of Duties** — terutama untuk operasi kritis yang memerlukan dua peran berbeda (mis. kasir + pemilik untuk retur, gudang + kepala untuk stock opname).
- [ ] **D.2.3** Evaluasi apakah dokumen ini sudah cukup membuktikan kepatuhan **UU PDP No. 27/2022** — terutama terkait proteksi data pribadi pelanggan (nomor WhatsApp terenkripsi di tabel `pelanggan`).

---

### FASE E — Validasi: Kualitas Bahasa dan Keterbacaan

#### E.1. Pemeriksaan Kualitas Bahasa Indonesia

- [ ] **E.1.1** Baca ulang seluruh narasi (bukan tabel/kode) dalam dokumen. Identifikasi kalimat yang **ambigu** — yaitu kalimat yang dapat diinterpretasikan lebih dari satu cara oleh pembaca berbeda. Catat nomor bab dan paragraf kalimat ambigu tersebut.
- [ ] **E.1.2** Identifikasi istilah teknis asing (Bahasa Inggris) yang digunakan **tanpa terjemahan atau penjelasan** dan tidak tercantum di Glosarium (Bab 10). Catat daftarnya.
- [ ] **E.1.3** Periksa konsistensi penulisan istilah: apakah satu konsep selalu ditulis dengan cara yang sama di seluruh dokumen? Contoh: apakah "eskalasi otorisasi" kadang ditulis "privilege escalation" dan kadang "eskalasi sandi" tanpa konsistensi?
- [ ] **E.1.4** Periksa apakah instruksi atau aturan yang ditulis dalam narasi Bab 6 sudah jelas dan tidak membingungkan bagi programmer junior yang akan mengimplementasikannya.
- [ ] **E.1.5** Identifikasi kata atau kalimat yang berulang (redundan) dan tidak menambah nilai informatif pada dokumen.

#### E.2. Pemeriksaan Kelengkapan Glosarium

- [ ] **E.2.1** Buat daftar semua istilah teknis yang digunakan di seluruh dokumen (dari teks narasi, tabel, dan diagram).
- [ ] **E.2.2** Bandingkan daftar tersebut dengan istilah yang sudah ada di Bab 10 (Glosarium). Identifikasi istilah teknis penting yang **belum** tercantum di Glosarium.
- [ ] **E.2.3** Jika ada istilah penting yang belum didefinisikan di Glosarium, tambahkan definisinya ke Bab 10 dalam versi dokumen yang direvisi.

---

### FASE F — Eksekusi: Perbaikan dan Penulisan Dokumen Final

#### F.1. Konsolidasi Seluruh Temuan

- [ ] **F.1.1** Kompilasi seluruh temuan dari FASE B, C, D, dan E menjadi satu daftar terstruktur dengan format:
  ```
  [FINDING-XXX] Kategori: [CRITICAL/MAJOR/MINOR]
  Lokasi: [Bab X.Y / Tabel / Baris No.]
  Masalah: [Deskripsi singkat masalah]
  Tindakan: [Apa yang akan diperbaiki]
  ```
- [ ] **F.1.2** Urutkan temuan berdasarkan kritikalitas: CRITICAL → MAJOR → MINOR.
- [ ] **F.1.3** Tentukan tindakan korektif untuk setiap temuan. Untuk data yang kosong atau tidak ada di referensi, **derivasikan** nilainya dari file referensi yang sudah dibaca di FASE A, sesuai konteks dan logika bisnis AbuCom.

#### F.2. Penerapan Perbaikan pada Dokumen

- [ ] **F.2.1** Mulai proses penulisan ulang dokumen. Buka editor teks untuk file `docs/sdlc/02_analysis/06_access_control_matrix.md`.
- [ ] **F.2.2** **Ubah versi dokumen**: Pada YAML front matter, ubah `versi: 1.0` menjadi `versi: 1.1`. Ubah juga `status: Draft` menjadi `status: Review`.
- [ ] **F.2.3** **Tambahkan baris di tabel Riwayat Perubahan Dokumen** (Changelog) dengan data:
  - Versi: `1.1`
  - Tanggal: `[tanggal eksekusi hari ini dalam format YYYY-MM-DD]`
  - Perubahan: Deskripsi singkat seluruh perubahan yang dilakukan (referensi temuan F.1.1)
  - Oleh: `Senior Software Architect & RBAC Security Specialist (Issue #0022)`
- [ ] **F.2.4** Terapkan seluruh perbaikan konten dari daftar temuan di langkah F.1.1, satu per satu secara berurutan dari CRITICAL → MAJOR → MINOR.
- [ ] **F.2.5** Jika ada data yang kosong atau perlu diisi, isi dengan data yang **relevan, akurat, dan konsisten** dengan informasi dari file referensi. Jangan membuat data fiktif yang tidak ada landasan di dokumen referensi manapun.
- [ ] **F.2.6** Jika ada istilah baru yang perlu ditambahkan ke Glosarium, tambahkan di Bab 10 dengan format yang konsisten (nomor urut, istilah bold, definisi).
- [ ] **F.2.7** Jika ada file referensi baru yang ditemukan atau ditambahkan selama proses perbaikan (yang tidak ada di Bab 11 sebelumnya), tambahkan file tersebut ke tabel Bab 11 (Referensi Dokumen) di **baris paling bawah tabel** dengan format yang konsisten.
- [ ] **F.2.8** Lakukan review akhir: baca ulang keseluruhan dokumen yang telah direvisi untuk memastikan tidak ada inkonsistensi baru yang timbul akibat perbaikan.

#### F.3. Penulisan Ulang File (Overwrite)

- [ ] **F.3.1** Tulis ulang seluruh isi dokumen yang telah direvisi ke file `docs/sdlc/02_analysis/06_access_control_matrix.md` menggunakan operasi **overwrite (timpa)**.
- [ ] **F.3.2** **WAJIB**: Pastikan bahwa **seluruh teks dari baris pertama hingga baris terakhir ditulis ulang sepenuhnya**. Tidak boleh ada bagian dokumen yang:
  - Dipotong (`truncated`)
  - Diringkas (`summarized`)
  - Digantikan dengan placeholder seperti `[... isi sebelumnya tetap ...]`
  - Dihilangkan (`omitted`)
- [ ] **F.3.3** Setelah penulisan selesai, buka kembali file hasil overwrite dan verifikasi bahwa:
  - Baris pertama dokumen dimulai dengan `---` (YAML front matter opening)
  - Baris terakhir dokumen adalah baris terakhir tabel Referensi Dokumen (Bab 11)
  - Tidak ada konten yang terputus di tengah kalimat atau tabel
  - Total jumlah baris tidak jauh berkurang dari versi sebelumnya (penghapusan sah hanya jika ada konten yang memang redundan atau salah)
- [ ] **F.3.4** Verifikasi bahwa versi dokumen di YAML front matter sudah tertulis `1.1` (bukan `1.0`).
- [ ] **F.3.5** Verifikasi bahwa tabel Riwayat Perubahan memiliki dua baris: baris `1.0` (original) dan baris `1.1` (revisi baru).

---

### FASE G — Verifikasi Final

#### G.1. Verifikasi Pasca-Penulisan

- [ ] **G.1.1** Buka kembali file `docs/sdlc/02_analysis/06_access_control_matrix.md` yang baru saja ditulis ulang.
- [ ] **G.1.2** Verifikasi bahwa total jumlah peran di Bab 2.1 tetap berjumlah **8 peran internal**.
- [ ] **G.1.3** Verifikasi bahwa total jumlah baris menu di Bab 4 (di semua sub-bab M.1 s.d M.10 dan Use Case Dasar) berjumlah **44 baris** (sesuai 44 Use Case).
- [ ] **G.1.4** Verifikasi bahwa total jumlah baris tabel di Bab 5.2 berjumlah **28 baris** (sesuai 28 tabel database).
- [ ] **G.1.5** Verifikasi bahwa total baris di Bab 8.1 berjumlah sesuai dengan total kebutuhan bisnis di BRD.
- [ ] **G.1.6** Verifikasi bahwa total baris di Bab 8.2 berjumlah sesuai dengan total kebutuhan sistem di SRS.
- [ ] **G.1.7** Verifikasi bahwa total baris di Bab 8.3 berjumlah **44 baris** (sesuai 44 Use Case).
- [ ] **G.1.8** Verifikasi bahwa diagram Mermaid di Bab 7 valid secara sintaks (tidak ada tag yang belum ditutup, tidak ada karakter ilegal di dalam node label).
- [ ] **G.1.9** Laporkan hasil akhir: issue ini dinyatakan **selesai (DONE)** hanya jika seluruh checklist di FASE A hingga FASE G sudah ditandai `[x]` dan tidak ada CRITICAL FINDING yang belum diselesaikan.

---

## Kriteria Penerimaan (Acceptance Criteria)

Issue ini dinyatakan **berhasil** apabila seluruh kondisi berikut terpenuhi:

| # | Kriteria | Indikator Keberhasilan |
|---|----------|------------------------|
| 1 | Komparasi dengan file referensi selesai | Tidak ada Use Case, Tabel DB, atau BR/SRS requirement yang terlewat di dokumen utama |
| 2 | Tidak ada data kosong atau placeholder | Semua sel tabel dan field dokumen terisi nilai yang valid dan informatif |
| 3 | Konsistensi internal terjaga | Tidak ada kontradiksi antara Bab 3, Bab 4, Bab 5, dan Bab 9 |
| 4 | Parameter teknis terverifikasi | Nilai JWT, bcrypt, rate limit di Bab 6 identik dengan SRS |
| 5 | Kode error tervalidasi | Semua kode error di Bab 6 konsisten dengan definisi di SRS |
| 6 | Kualitas bahasa terjaga | Tidak ada kalimat ambigu atau istilah tidak terdefinisi |
| 7 | Glosarium lengkap | Semua istilah teknis penting terdefinisi di Bab 10 |
| 8 | Traceability lengkap | Semua BRD, SRS, dan UC terpetakan di Bab 8 |
| 9 | Dokumen ditulis ulang sempurna | File dioverwrite tanpa truncation; versi berubah ke v1.1 |
| 10 | Referensi baru ditambahkan | Jika ada referensi baru, tercantum di Bab 11 baris paling bawah |

---

## Catatan Penting untuk Implementor

> **PERINGATAN KRITIS #1 — ANTI TRUNCATION**
> Saat menulis ulang dokumen ke file (Langkah F.3.1), kamu **DILARANG KERAS** memotong, meringkas, atau menghilangkan bagian manapun dari dokumen. Jika kapasitas konteks kamu terbatas, lakukan penulisan dalam beberapa segmen berurutan, tetapi pastikan **tidak ada satu karakter pun** yang hilang di antara segmen.

> **PERINGATAN KRITIS #2 — NO HALLUCINATION**
> Jangan pernah menginventarisir, menambahkan, atau mengubah data (nama peran, kode UC, nama tabel, nilai parameter teknis) tanpa landasan eksplisit dari salah satu file referensi yang disebutkan di atas. Jika informasi tidak ditemukan di referensi manapun, tandai dengan `[PERLU KONFIRMASI: <alasan>]` dan jangan membuat data fiktif.

> **PERINGATAN KRITIS #3 — SEQUENTIAL EXECUTION**
> Laksanakan setiap langkah secara berurutan. Jangan melompat ke FASE F sebelum FASE B, C, D, dan E selesai sepenuhnya. Urutan yang benar memastikan tidak ada temuan yang terlewat.

> **CATATAN KHUSUS — SPESIFIK DOKUMEN ACM**
> Dokumen Access Control Matrix memiliki ciri khas:
> - Setiap sel matriks di Bab 4 dan Bab 5 memiliki makna keamanan yang sangat spesifik. Perubahan satu nilai CRUD atau satu simbol hak akses dapat membuka celah privilege escalation atau menutup akses yang sah.
> - Diagram Mermaid di Bab 7 harus merepresentasikan skenario nyata operasional bisnis, bukan skenario hipotetis.
> - Kolom "Catatan Keamanan / Khusus" di Bab 4 dan "Catatan Integritas Data" di Bab 5 adalah sumber informasi kritis untuk developer — jangan biarkan kosong.

---

*Issue ini dibuat pada: 2026-05-24*
*Dibuat oleh: Senior Software Architect & RBAC Security Specialist*
