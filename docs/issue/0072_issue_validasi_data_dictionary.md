# Validasi, Analisis & Revisi Dokumen Data Dictionary

## Informasi Issue

| Field | Detail |
|---|---|
| **Judul** | Validasi, Analisis & Revisi Mendalam Dokumen Data Dictionary |
| **Dokumen Utama** | Data Dictionary |
| **Target File** | `docs/sdlc/02_analysis/05_data_dictionary.md` |
| **Lokasi Referensi** | `docs/sdlc/` |
| **Versi Dokumen Saat Ini** | v1.1 |
| **Versi Target Setelah Revisi** | v1.2 |
| **Prioritas** | 🔴 Tinggi — Prasyarat Mutlak Fase 03 Design |
| **Dibuat Tanggal** | 2026-05-28 |
| **Dibuat Oleh** | Antigravity AI (Senior Planning Agent) |
| **Assigned To** | Junior Programmer / AI Model Kecil |

---

## 1. Latar Belakang & Konteks

Dokumen `05_data_dictionary.md` adalah **deliverables ke-5 dan terakhir dari Fase 02 Analysis** dalam SDLC AbuCom. Dokumen ini berfungsi sebagai *Single Source of Truth* teknis untuk seluruh spesifikasi skema basis data MySQL relasional yang akan diimplementasikan pada Fase 03 Design dalam bentuk berkas `schema.sql` dan `seed.sql`.

Kualitas dokumen ini **sangat kritis** karena:
- Menjadi **input primer** bagi seluruh dokumen Fase 03 Design (SDD, schema.sql, seed.sql).
- Menjadi **acuan validasi** bagi seluruh query Python yang akan ditulis oleh tim backend developer.
- Menjadi **referensi operasional** bagi kepala percetakan dalam memahami alur data tanpa membuka source code.

Dokumen ini harus melalui satu sesi **validasi menyeluruh** sebelum Fase 03 dimulai untuk memastikan tidak ada ambiguitas, kekosongan data, inkonsistensi relasi, atau penyimpangan dari standar industri yang akan menghambat pekerjaan di fase selanjutnya.

---

## 2. Persona yang Harus Diasumsikan

> **INSTRUKSI WAJIB**: Sebelum memulai pekerjaan apa pun, kamu HARUS mengasumsikan dirimu sebagai persona berikut dan mempertahankan sudut pandang ini sepanjang seluruh proses validasi.

Kamu adalah seorang **Senior Database Architect & Data Modeling Specialist** dengan spesialisasi sebagai berikut:
- Lebih dari **15 tahun pengalaman** merancang skema basis data relasional MySQL untuk aplikasi bisnis skala UKM hingga enterprise.
- Ahli dalam standar **normalisasi database (1NF, 2NF, 3NF, BCNF)**, desain ERD, penulisan DDL SQL yang bersih, dan integritas referensial.
- Pakar dalam standar dokumentasi data industri seperti **IEEE 830**, **DAMA-DMBOK (Data Management Body of Knowledge)**, dan praktik terbaik *data dictionary* modern.
- Memiliki kewenangan untuk **menolak, merevisi, dan memvalidasi** setiap klaim teknis dalam dokumen ini.
- Berpengalaman dalam **audit kualitas dokumen** untuk proyek pengembangan software berbasis Python + MySQL di lingkungan LAN lokal.
- Paham konteks bisnis usaha percetakan (printing business) mencakup: manajemen produksi cetak, rantai pasok ATK, kasbon staf, payroll, PPOB, dan manajemen aset tetap.

---

## 3. Daftar File yang Harus Dibaca (Wajib Sebelum Validasi)

Kamu WAJIB membaca seluruh file berikut secara berurutan sebelum memulai proses validasi. Jangan melewati satu pun file.

- [ ] **[BACA PERTAMA]** `docs/sdlc/02_analysis/05_data_dictionary.md` ← Dokumen Utama yang akan divalidasi
- [ ] **[BACA KEDUA]** `docs/sdlc/02_analysis/01_business_requirements.md` ← BRD v1.1 (Sumber aturan bisnis, RBAC, domain nilai, parameter default, manajemen risiko modal)
- [ ] **[BACA KETIGA]** `docs/sdlc/02_analysis/02_software_requirements.md` ← SRS v1.1 (Sumber definisi entitas konseptual, relasi ERD awal, wireframe navigasi, parameter input/output CLI)
- [ ] **[BACA KEEMPAT]** `docs/sdlc/02_analysis/03_use_case_diagram.md` ← Use Case Diagram v1.1 (Acuan alur data keluar/masuk interaksi aktor staf)
- [ ] **[BACA KELIMA]** `docs/sdlc/02_analysis/04_workflow_diagram.md` ← Workflow Diagram v1.1 (Acuan alur transaksional keuangan dan sirkulasi logistik)
- [ ] **[BACA KEENAM]** `docs/sdlc/01_planning/04_tech_stack_decision.md` ← Tech Stack Decision v1.1 (Acuan batasan engine MySQL 8.4 LTS, LAN local, bcrypt/JWT)
- [ ] **[BACA KETUJUH]** `docs/sdlc/01_planning/05_innovation_proposal.md` ← Innovation Proposal v1.1 (Acuan prioritas fungsional modul)
- [ ] **[BACA KEDELAPAN]** `docs/sdlc/01_planning/03_stakeholder_register.md` ← Stakeholder Register v1.1 (Acuan pemetaan peran/hak akses 8 aktor)
- [ ] **[BACA KESEMBILAN]** `docs/sdlc/01_planning/02_feasibility_study.md` ← Feasibility Study v1.1 (Acuan parameter ekonomi default system configs)
- [ ] **[BACA KESEPULUH]** `docs/sdlc/01_planning/01_project_charter.md` ← Project Charter v1.1 (Acuan ruang lingkup 10 modul)

---

## 4. Ruang Lingkup Validasi

### 4.1. Yang Termasuk dalam Validasi Ini
- Seluruh 28 definisi tabel dan 282+ kolom atribut.
- Seluruh 19 kamus domain nilai (value domain dictionary).
- Seluruh 58 relasi foreign key dalam matriks relasi.
- Diagram ERD Mermaid konseptual dan relasional.
- Seluruh aturan bisnis data (komputasi, validasi input, constraint, default value).
- Spesifikasi indeks dan optimasi database.
- Matriks ketertelusuran (traceability matrix) ke BRD dan SRS.
- Glosarium istilah data.
- Spesifikasi data seed awal minimum dan kebijakan retensi.

### 4.2. Yang TIDAK Termasuk dalam Validasi Ini
- Implementasi kode SQL aktual (`schema.sql`, `seed.sql`) — itu adalah tugas Fase 03 Design.
- Perubahan arsitektur sistem secara fundamental (menambah/menghapus modul AbuCom).
- Perubahan stack teknologi (tetap MySQL 8.4 LTS + Python).

---

## 5. Checklist Validasi — Tahap demi Tahap

Eksekusi checklist berikut **secara berurutan dari atas ke bawah**. Jangan melompati langkah. Tandai setiap item `[x]` setelah selesai.

---

### TAHAP A: Persiapan & Pembacaan

- [ ] **A.1** Baca dokumen utama `docs/sdlc/02_analysis/05_data_dictionary.md` dari baris 1 hingga baris terakhir tanpa melewati bagian mana pun. Catat semua anomali, kekosongan, atau kejanggalan dalam memori kerja.
- [ ] **A.2** Baca `docs/sdlc/02_analysis/01_business_requirements.md` (BRD v1.1). Identifikasi: semua ID fitur (BR-F-XX), aturan bisnis, parameter default, dan domain nilai yang disebutkan.
- [ ] **A.3** Baca `docs/sdlc/02_analysis/02_software_requirements.md` (SRS v1.1). Identifikasi: semua ID fungsional (SRS-F-XXX), entitas data yang disebutkan, relasi antar entitas, dan wireframe input/output.
- [ ] **A.4** Baca `docs/sdlc/02_analysis/03_use_case_diagram.md`. Identifikasi: semua aktor, use case, dan data yang mengalir dalam setiap interaksi.
- [ ] **A.5** Baca `docs/sdlc/02_analysis/04_workflow_diagram.md`. Identifikasi: semua state data, kondisi transisi, dan entitas database yang digunakan dalam alur kerja.
- [ ] **A.6** Baca `docs/sdlc/01_planning/04_tech_stack_decision.md`. Catat: batasan teknis MySQL (versi, engine, charset), constraint Python library, dan arsitektur deployment LAN.
- [ ] **A.7** Baca semua file perencanaan lainnya (Innovation Proposal, Stakeholder Register, Feasibility Study, Project Charter) untuk memvalidasi parameter ekonomi dan scope modul.

---

### TAHAP B: Validasi Kelengkapan vs. Dokumen Referensi

> **Tujuan**: Memastikan dokumen utama tidak melewatkan satu pun data/entitas/aturan bisnis yang disebutkan dalam file referensi.

- [ ] **B.1** Buat daftar semua **entitas/tabel** yang disebutkan di SRS v1.1 (Bab 3, 6, 10). Bandingkan satu per satu dengan 28 tabel yang terdaftar di Bab 2.1 Data Dictionary. Apakah ada tabel yang disebutkan di SRS tetapi **tidak ada** di Data Dictionary? Jika ada, catat untuk ditambahkan.
- [ ] **B.2** Buat daftar semua **ID fitur SRS (SRS-F-XXX)** yang disebutkan di SRS. Verifikasi bahwa setiap SRS-F-XXX telah dipetakan ke minimal satu tabel di Bab 8.2 (Matriks Ketertelusuran). Identifikasi SRS-F yang belum terpetakan.
- [ ] **B.3** Buat daftar semua **ID fitur BRD (BR-F-XX)** yang disebutkan di BRD. Verifikasi bahwa setiap BR-F-XX telah dipetakan ke minimal satu tabel di Bab 8.2. Identifikasi BR-F yang belum terpetakan.
- [ ] **B.4** Verifikasi semua **domain nilai status** yang disebutkan dalam SRS/BRD telah didefinisikan di Bab 4 (Kamus Domain Nilai). Contoh: apakah semua nilai `status_antrian`, `status_kasbon`, dll. di SRS sudah ada dan lengkap di domain dictionary?
- [ ] **B.5** Verifikasi semua **kolom atribut** yang disebutkan dalam narasi SRS (misal: "sistem menyimpan nama lengkap, nomor WA, tanggal daftar pelanggan") sudah ada sebagai kolom dalam definisi tabel terkait. Jika ada kolom yang tersebut di SRS tetapi tidak ada di Data Dictionary, catat untuk ditambahkan.
- [ ] **B.6** Verifikasi semua **aturan bisnis** (formula kalkulasi, threshold, parameter default) yang disebutkan dalam BRD Bab 9 dan SRS Lampiran sudah tercermin dalam Bab 6 (Aturan Bisnis Data) dan Bab 6.4 (Aturan Default Value/system_configs). Apakah ada parameter yang disebutkan di referensi tetapi belum ada di `system_configs`?
- [ ] **B.7** Verifikasi semua **peran pengguna (role)** yang disebutkan dalam Stakeholder Register v1.1 sudah terdaftar lengkap dalam Domain Peran Pengguna di Bab 4.10. Pastikan tidak ada role yang tercantum di referensi tetapi hilang dari domain dictionary.
- [ ] **B.8** Verifikasi **alur pengambilan data** yang disebutkan dalam Workflow Diagram (misal: alur handover kasir, alur produksi cetak, alur PPOB) sudah terdukung secara struktural oleh kolom-kolom tabel yang didefinisikan. Apakah ada alur workflow yang tidak bisa ditracking dengan skema saat ini?
- [ ] **B.9** Verifikasi semua **use case dalam Use Case Diagram** yang membutuhkan penyimpanan atau pembacaan data sudah terpetakan ke tabel yang relevan. Apakah ada use case yang membutuhkan tabel baru yang belum ada?

---

### TAHAP C: Validasi Kekhususan Dokumen (Tidak Ada Data Asing)

> **Tujuan**: Memastikan dokumen ini hanya memuat data yang memang relevan dan dibutuhkan spesifik oleh sebuah Data Dictionary — tidak ada konten "salah tempat" yang seharusnya ada di dokumen lain.

- [ ] **C.1** Periksa apakah ada **narasi bisnis panjang** (penjelasan *mengapa* suatu fitur ada, bukan *apa* yang disimpan) yang seharusnya ada di BRD/SRS, bukan di Data Dictionary. Hapus atau ringkas bagian yang tidak relevan.
- [ ] **C.2** Periksa apakah ada **wireframe atau deskripsi UI/UX** yang tidak relevan dengan spesifikasi data. Data Dictionary tidak boleh memuat detail tampilan antarmuka.
- [ ] **C.3** Periksa apakah ada **kode implementasi Python** atau pseudocode yang seharusnya ada di SDD atau berkas teknis lainnya. Data Dictionary cukup menyebut mekanisme pada level logika bisnis, bukan implementasi kode.
- [ ] **C.4** Periksa apakah ada **duplikasi definisi** yang sama persis antara dua bab berbeda. Jika ada, konsolidasikan ke satu tempat dan beri referensi silang.
- [ ] **C.5** Verifikasi bahwa setiap tabel yang didefinisikan memang **memiliki peran yang berbeda dan tidak overlap**. Apakah ada dua tabel yang menyimpan data yang sama (potensi redundansi desain)?

---

### TAHAP D: Validasi Standar Struktur Dokumen

> **Tujuan**: Memastikan dokumen memiliki struktur yang sesuai standar Data Dictionary industri yang profesional.

- [ ] **D.1** Verifikasi **header dokumen** (frontmatter YAML) memuat: dokumen, proyek, versi, tanggal, status, dan penyusun. Semua field harus terisi.
- [ ] **D.2** Verifikasi **Riwayat Perubahan Dokumen** (change log) ada dan mencatat versi, tanggal, ringkasan perubahan, dan nama penyusun secara kronologis dari versi lama ke baru.
- [ ] **D.3** Verifikasi **Bab 1 (Informasi Dokumen)** memuat: tujuan, cakupan, posisi SDLC, hubungan dengan dokumen lain, audiens target, dan konvensi penulisan. Periksa apakah ada sub-bab yang perlu ditambahkan.
- [ ] **D.4** Verifikasi **Bab 2 (Ringkasan Model Data)** memuat: daftar master entitas (tabel dengan metadata lengkap), diagram ERD Mermaid, dan statistik ringkasan. Periksa kelengkapan kolom di tabel daftar entitas (No, Nama Tabel, Deskripsi, Modul, Jumlah Kolom, Derivasi SRS).
- [ ] **D.5** Verifikasi **setiap definisi tabel di Bab 3** mengikuti format standar yang konsisten:
  - Tabel metadata tabel (Nama Tabel, Deskripsi, Modul Terkait, Derivasi SRS, Derivasi BRD, Engine, Charset, Collation).
  - Tabel detail kolom dengan kolom: No, Nama Kolom, Tipe Data MySQL, Constraint, Null?, Default, Deskripsi Bisnis, Domain Nilai.
  - Catatan Table-Level Constraints & Checks (jika ada).
  - Catatan Implementasi (jika ada).
- [ ] **D.6** Periksa apakah **ada tabel yang formatnya tidak konsisten** dengan format standar di atas (D.5). Jika ada, seragamkan formatnya. Khususnya perhatikan: apakah semua tabel memiliki header metadata tabel yang lengkap, termasuk kolom "Derivasi BRD".
- [ ] **D.7** Verifikasi **Bab 4 (Kamus Domain Nilai)** untuk setiap domain memuat: nama domain, kolom terkait beserta nama tabelnya, daftar nilai valid dengan deskripsi yang jelas, dan sumber referensi SRS/BRD. Periksa konsistensi format antar domain.
- [ ] **D.8** Verifikasi **Bab 5 (Relasi Antar-Entitas)** memuat: matriks foreign key lengkap dengan kolom Tabel Asal, Kolom FK, Tabel Referensi, Kolom PK, Tipe Relasi, ON DELETE, ON UPDATE. Semua relasi harus terdokumentasi.
- [ ] **D.9** Verifikasi **Bab 6 (Aturan Bisnis Data)** memuat: aturan validasi input, aturan komputasi & formula (dengan notasi matematis), aturan constraint database, dan aturan default value dengan tabel `system_configs`.
- [ ] **D.10** Verifikasi **Bab 7 (Indeks dan Optimasi)** memuat: daftar primary key, daftar unique constraint, dan rekomendasi composite index dengan justifikasi performa yang spesifik.
- [ ] **D.11** Verifikasi **Bab 8 (Matriks Ketertelusuran)** memuat: pemetaan tabel ke modul fungsional (M.1-M.10) dan pemetaan tabel ke referensi BRD/SRS. Pastikan setiap tabel memiliki keterangan hubungan aturan bisnis yang informatif.
- [ ] **D.12** Verifikasi **Bab 9 (Glosarium)** mendefinisikan semua istilah teknis yang digunakan dalam dokumen. Apakah ada istilah yang dipakai dalam bab lain tetapi belum ada di glosarium? Tambahkan jika ada.
- [ ] **D.13** Verifikasi **Bab 10 (Referensi Dokumen)** mencantumkan semua file yang digunakan sebagai referensi, lengkap dengan path file dan deskripsi peran referensinya.
- [ ] **D.14** Verifikasi **Bab 11 (Data Seed Awal & Kebijakan Retensi)** memuat spesifikasi seed data minimum yang cukup untuk bootstrap sistem, dan kebijakan retensi log keamanan yang operasional.

---

### TAHAP E: Validasi Kelayakan sebagai Input Fase 03 Design

> **Tujuan**: Memastikan dokumen ini cukup lengkap dan presisi sehingga tim Fase 03 (yang menulis `schema.sql`) tidak perlu kembali bertanya ke dokumen lain.

- [ ] **E.1** Verifikasi setiap **tipe data MySQL** yang digunakan sudah tepat dan konsisten di seluruh 28 tabel:
  - `INT` untuk ID/foreign key integer.
  - `DECIMAL(15,4)` untuk semua nominal rupiah dan kuantitas desimal.
  - `VARCHAR(n)` dengan panjang `n` yang masuk akal untuk setiap kolom string.
  - `TEXT` untuk kolom yang tidak dibatasi panjangnya (alamat, deskripsi, alasan).
  - `TIMESTAMP` untuk waktu dengan sinkronisasi UTC.
  - `DATE` untuk tanggal saja (tanpa jam).
  - `BOOLEAN` (alias TINYINT(1)) untuk flag boolean.
  - `JSON` untuk log audit yang dinamis.
- [ ] **E.2** Verifikasi setiap kolom **Default Value** sudah didefinisikan dengan benar dan tidak ada kolom yang nilainya bisa menjadi `NULL` tanpa alasan logis bisnis yang jelas.
- [ ] **E.3** Verifikasi setiap **Foreign Key** sudah memiliki ON DELETE dan ON UPDATE action yang tepat sesuai dengan logika bisnis:
  - `RESTRICT` untuk data master yang tidak boleh dihapus jika masih direferensi.
  - `CASCADE` untuk detail yang harus ikut terhapus jika induknya dihapus.
  - `SET NULL` untuk kolom nullable yang boleh kehilangan referensinya.
- [ ] **E.4** Verifikasi semua **CHECK constraint** sudah logis dan tidak kontradiktif. Contoh: apakah CHECK `sisa_utang >= 0 AND sisa_utang <= nominal_pinjaman` sudah ada di semua tabel utang yang relevan (`kasbon`, `utang_supplier`, `pinjaman_bank`, `pinjaman_kerabat`)?
- [ ] **E.5** Verifikasi diagram **ERD Mermaid di Bab 2.2** sudah merepresentasikan semua 28 tabel dan semua relasi signifikan. Apakah ada tabel atau relasi yang hilang dari diagram?
- [ ] **E.6** Verifikasi **statistik di Bab 2.3** (total tabel, total kolom, persentase multi-cabang, dll.) masih akurat setelah proses revisi. Jika ada penambahan/pengurangan kolom, update angka statistiknya.
- [ ] **E.7** Verifikasi bahwa setiap **tabel derivasi (7 tabel)** sudah diberi penanda peringatan `⚠️ [DERIVASI]` yang jelas, dan sudah dijelaskan alasan derivasinya serta sumber referensi yang mendasarinya.
- [ ] **E.8** Verifikasi **Bab 11.1 (Seed Data)** sudah cukup untuk menginisialisasi database sehingga aplikasi CLI bisa langsung dijalankan tanpa error: cabang default, pengguna pemilik, saldo PPOB awal, saldo e-wallet awal, dan 13 parameter system_configs dengan nilai aktual.
- [ ] **E.9** Pastikan tidak ada **kolom "placeholder"** yang masih kosong seperti: "-", "TBD", "TODO", "N/A" tanpa penjelasan, atau kolom yang bernilai kosong/tidak tersedia di seluruh dokumen.
- [ ] **E.10** Verifikasi bahwa kolom `no_invoice` pada tabel `transaksi` sudah memiliki **spesifikasi format nomor invoice** yang lengkap dan eksplisit (format: `INV/YYYYMMDD/XXXX`) di deskripsi bisnis dan/atau catatan implementasinya.

---

### TAHAP F: Validasi Konsistensi Penamaan & Konvensi

> **Tujuan**: Memastikan dokumen menggunakan konvensi penamaan yang konsisten di seluruh bagian sehingga tidak membingungkan implementor.

- [ ] **F.1** Verifikasi semua nama tabel menggunakan **snake_case singular** (bukan plural) dan huruf kecil semua. Contoh: `transaksi` ✅ bukan `Transaksis` ❌.
- [ ] **F.2** Verifikasi semua nama kolom menggunakan **snake_case** huruf kecil semua. Tidak ada camelCase atau PascalCase di seluruh tabel.
- [ ] **F.3** Verifikasi pola **Foreign Key** konsisten menggunakan format `[nama_tabel_referensi]_id`. Khusus untuk FK yang merujuk ke `pengguna.id` dengan nama kolom berbeda (contoh: `kasir_id`, `desainer_id`, `teknisi_id`, `supervisor_id`, `produksi_id`), pastikan sudah terdokumentasi dengan jelas bahwa itu adalah FK ke `pengguna.id`.
- [ ] **F.4** Verifikasi simbol constraint (**PK, FK, UQ, NN, AI, CK**) digunakan secara konsisten di seluruh kolom tabel detail atribut.
- [ ] **F.5** Verifikasi **kolom `cabang_id`** ada di semua 28 tabel (sesuai klaim 100% multi-cabang ready di Bab 2.3). Temukan tabel mana yang belum punya `cabang_id` dan tambahkan jika memang seharusnya ada.
- [ ] **F.6** Verifikasi **kolom `created_at` dan `updated_at`** ada di semua 28 tabel (sesuai klaim 100% audit trail ready di Bab 2.3). Temukan tabel mana yang belum punya kedua kolom ini.
- [ ] **F.7** Verifikasi **jumlah kolom** di kolom "Jumlah Kolom" pada tabel daftar master entitas (Bab 2.1) sudah akurat dan sesuai dengan hitungan kolom aktual dalam definisi tabel di Bab 3. Hitung manual satu per satu untuk setiap tabel.
- [ ] **F.8** Verifikasi **referensi silang antar bab** konsisten. Jika Bab 4 menyebut suatu domain digunakan pada kolom tertentu, pastikan di definisi tabel di Bab 3 kolom tersebut juga mereferensikan domain yang sama di kolom "Domain Nilai".
- [ ] **F.9** Verifikasi **nilai domain** yang disebutkan dalam kolom "Domain Nilai" di Bab 3 konsisten (sama persis, tidak berbeda ejaan atau huruf kapital) dengan nilai yang didefinisikan di Bab 4. Contoh: jika Bab 4 mendefinisikan `'AKTIF'` (kapital), maka di Bab 3 domain nilainya juga harus `'AKTIF'`.
- [ ] **F.10** Khusus pada tabel `stock_opname` Bab 3.25, verifikasi kolom `user_id` apakah sudah menggunakan nama `pengguna_id` (sesuai konvensi pola FK yang dipakai konsisten di seluruh dokumen). Jika berbeda, seragamkan menjadi `pengguna_id` dan perbarui juga di matriks FK Bab 5.1.
- [ ] **F.11** Verifikasi konsistensi penggunaan nama kolom `status_opname` pada tabel `stock_opname` — di Bab 4.5 (Domain Status Antrian Kerja) disebutkan domain ini juga digunakan untuk `status_opname`, namun di Bab 4.19 ada Domain Status Opname tersendiri. Pastikan di Bab 3.25 kolom `status_opname` merujuk ke domain yang benar (Bab 4.19, bukan Bab 4.5).

---

### TAHAP G: Validasi Bahasa & Keterbacaan

> **Tujuan**: Memastikan dokumen menggunakan Bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau AI model kecil.

- [ ] **G.1** Periksa seluruh teks narasi apakah ada **kalimat yang ambigu** atau memiliki dua makna berbeda yang bisa disalahtafsirkan. Tulis ulang kalimat tersebut agar lebih eksplisit.
- [ ] **G.2** Periksa apakah ada **istilah teknis** yang digunakan tanpa dijelaskan terlebih dahulu dan tidak ada di Glosarium Bab 9. Tambahkan ke glosarium jika perlu.
- [ ] **G.3** Periksa seluruh **Deskripsi Bisnis** kolom di setiap tabel apakah sudah cukup informatif untuk menjelaskan: (a) apa isi kolom ini, (b) kapan kolom ini diisi, dan (c) bagaimana kaitannya dengan logika bisnis. Jika hanya satu kalimat generik, perjelas.
- [ ] **G.4** Periksa apakah ada **istilah campuran Bahasa Indonesia dan Bahasa Inggris** yang tidak konsisten dalam kalimat yang sama. Gunakan satu bahasa yang dominan secara konsisten, atau gunakan cetak miring untuk istilah teknis asing.
- [ ] **G.5** Periksa apakah setiap **Catatan Implementasi** (blockquote `>`) sudah memberikan panduan yang cukup jelas bagi implementor agar tidak perlu melakukan asumsi mandiri.
- [ ] **G.6** Periksa ejaan dan tanda baca dalam seluruh dokumen. Koreksi kesalahan ketik (typo) dan kalimat yang tidak lengkap.
- [ ] **G.7** Periksa apakah **judul bab dan sub-bab** konsisten dalam penggunaan huruf kapital dan format penomoran hierarkis.
- [ ] **G.8** Verifikasi bahwa deskripsi di kolom "Keterangan Hubungan Aturan Bisnis" pada Bab 8.2 sudah informatif dan tidak hanya berisi satu kata. Perbaiki yang terlalu singkat.

---

### TAHAP H: Validasi Data Kosong & Pengisian

> **Tujuan**: Menemukan dan mengisi semua data yang kosong, tidak tersedia, atau perlu diisi dengan data yang relevan dan realistis.

- [ ] **H.1** Cari seluruh kolom **Derivasi BRD** di setiap definisi tabel (Bab 3). Jika ada yang masih kosong atau menggunakan placeholder "-", isi dengan ID BR-F yang relevan berdasarkan pembacaan BRD v1.1.
- [ ] **H.2** Cari seluruh kolom **Derivasi SRS** di setiap definisi tabel. Jika ada yang masih kosong atau tidak lengkap, tambahkan semua ID SRS-F yang relevan.
- [ ] **H.3** Cari kolom **Domain Nilai** di tabel detail atribut yang nilainya masih "Free text" padahal seharusnya merujuk ke domain terstandarisasi yang sudah ada di Bab 4. Ganti dengan referensi domain yang tepat.
- [ ] **H.4** Cari kolom **Default** yang nilainya "-" (tidak ada default) — verifikasi apakah memang tidak boleh ada default (karena kolom ini wajib diisi user) atau terlewat. Tambahkan default jika diperlukan.
- [ ] **H.5** Periksa apakah **Catatan Implementasi** pada tabel `pengguna` sudah memuat informasi yang jelas tentang: (a) kebijakan brute force (locked_until logic, durasi suspensi 10 menit setelah 5 kali gagal), (b) library bcrypt Cost 12 untuk hashing password. Jika belum, tambahkan.
- [ ] **H.6** Periksa apakah **formula matematika** di Bab 6.2 sudah lengkap dan tidak ada variabel yang tidak terdefinisi. Setiap variabel dalam formula harus bisa dilacak ke kolom tabel yang spesifik di Bab 3.
- [ ] **H.7** Periksa apakah **Bab 6.3 (Aturan Constraint Database)** sudah mencakup penjelasan tentang aturan `limit_kasbon_staf` (maksimal Rp 1.000.000 atau 30% UMR) dengan referensi ke `system_configs`. Lengkapi jika kurang detail.
- [ ] **H.8** Periksa apakah **komposit index** di Bab 7.3 sudah mencakup semua pola query kritis yang diidentifikasi dalam Workflow Diagram dan Use Case Diagram. Contoh: apakah ada index untuk `utang_supplier(status_utang, cabang_id)` untuk laporan utang tempo? Jika ada index yang terlewat dan penting, tambahkan dengan justifikasi.
- [ ] **H.9** Periksa apakah nilai **saldo awal seed data** untuk tabel `saldo_ewallet` di Bab 11.1 sudah realistis sesuai konteks bisnis percetakan skala UKM. Lengkapi jika ada kolom yang belum diisi nilainya.
- [ ] **H.10** Periksa apakah **13 parameter system_configs** di Bab 6.4 sudah semua tercantum dengan nilai aktual (bukan placeholder) dan apakah nilainya konsisten dengan dokumen referensi Feasibility Study dan BRD.

---

### TAHAP I: Validasi Spesifik Ciri Khas Data Dictionary

> **Tujuan**: Memeriksa aspek teknis khusus yang merupakan ciri khas standar profesional Data Dictionary untuk database relasional MySQL.

- [ ] **I.1** **Verifikasi Normalisasi 1NF**: Pastikan tidak ada kolom yang menyimpan data komposit/multi-nilai dalam satu sel. Semua nilai harus atomik. Contoh: kolom `metode_pembayaran` hanya boleh menyimpan satu nilai string, bukan daftar metode.
- [ ] **I.2** **Verifikasi Kunci Fungsional (2NF & 3NF)**: Pastikan setiap kolom non-kunci bergantung penuh pada Primary Key, dan tidak ada dependensi transitif. Jika ada tabel yang menyimpan data yang lebih cocok dipecah menjadi tabel terpisah, catat rekomendasinya sebagai catatan revisor.
- [ ] **I.3** **Verifikasi Atomisitas Transaksi (ACID)**: Pastikan Bab 5.3 (Aturan Integritas Referensial) sudah menjelaskan dengan jelas perilaku ON DELETE/ON UPDATE untuk semua skenario penghapusan data kritis, tidak hanya beberapa contoh umum.
- [ ] **I.4** **Verifikasi Pembatasan Panjang VARCHAR**: Periksa semua kolom VARCHAR — apakah panjang maksimum yang ditentukan (n) sudah masuk akal dan tidak terlalu kecil sehingga bisa truncate data nyata? Contoh kasus: `VARCHAR(20)` untuk `status_pembayaran` dengan nilai terpanjang `'BELUM LUNAS'` (11 karakter) sudah aman. Verifikasi semua kolom status serupa.
- [ ] **I.5** **Verifikasi Skalabilitas Multi-Cabang**: Pastikan semua tabel yang menggunakan `cabang_id = 1` sebagai default sudah benar secara semantik — bahwa default ini hanya berlaku sebagai fallback untuk instalasi single-branch dan tidak mengunci data ke satu cabang.
- [ ] **I.6** **Verifikasi Keamanan Data Sensitif**: Pastikan kolom sensitif (nomor WA pelanggan `pelanggan.whatsapp`, password `pengguna.password_hash`) sudah memiliki catatan implementasi enkripsi yang jelas, lengkap dengan library Python yang digunakan dan mekanismenya (bcrypt untuk password, library `cryptography` reversibel untuk WA).
- [ ] **I.7** **Verifikasi Konsistensi ERD**: Bandingkan relasi yang digambar di ERD Mermaid (Bab 2.2) dengan definisi FK aktual di matriks relasi (Bab 5.1). Pastikan tidak ada relasi yang ada di ERD tetapi tidak ada di matriks FK, atau sebaliknya. Jika ada inkonsistensi, sesuaikan ERD mengikuti matriks FK sebagai sumber kebenaran.
- [ ] **I.8** **Verifikasi Urutan Definisi Tabel**: Pastikan urutan definisi tabel di Bab 3 mengikuti urutan dependensi (tabel induk/master didefinisikan lebih dulu sebelum tabel anak/transaksional). Urutan yang benar: `cabang` → `pengguna`, `pelanggan`, `supplier`, `barang` → `bom_komposisi`, `transaksi` → `detail_transaksi`, `antrian_kerja`, dst.
- [ ] **I.9** **Verifikasi Dokumentasi Indeks Unik Komposit**: Semua UNIQUE constraint komposit (seperti `UNIQUE(pengguna_id, tanggal)` di tabel `absensi`, `UNIQUE(barang_induk_id, bahan_baku_id)` di tabel `bom_komposisi`) harus terdokumentasi di bagian Table-Level Constraints & Checks pada definisi tabelnya masing-masing.
- [ ] **I.10** **Verifikasi Kebijakan Enkripsi & Backup**: Pastikan Bab 11.2 (Kebijakan Retensi) sudah mencakup: (a) ketentuan bahwa file backup ZIP AES-256 harus disimpan di lokasi terpisah dari direktori aplikasi, (b) prosedur verifikasi integritas file (checksum MD5/SHA256), dan (c) siapa yang bertanggung jawab dan berapa frekuensi minimum backup.
- [ ] **I.11** **Verifikasi Dokumentasi Trigger/Stored Procedure Level Logika**: Jika ada logika bisnis yang disebutkan harus dijalankan di level DB trigger MySQL (seperti imutabilitas `audit_logs`), pastikan hal ini terdokumentasi eksplisit di Bab 6 atau Bab 11.2, bukan hanya disebutkan secara tersirat.
- [ ] **I.12** **Verifikasi Kelengkapan Kamus Domain untuk Tabel Derivasi**: Pastikan semua tabel derivasi (No. 22-28) yang memiliki kolom status/tipe sudah memiliki kamus domain yang terdefinisi di Bab 4. Khususnya: apakah `tipe_bank` di tabel `pinjaman_bank` sudah terdokumentasi sebagai domain atau hanya disebutkan inline?

---

### TAHAP J: Menulis Ulang & Overwrite Dokumen

> **PERHATIAN KRITIS**: Tahap ini hanya boleh dimulai setelah Tahap A sampai I **seluruhnya selesai** dan semua temuan sudah dianalisis. Jangan memulai penulisan sebelum seluruh validasi selesai.

- [ ] **J.1** Kompilasikan semua temuan dari Tahap B sampai I menjadi daftar perubahan yang akan dilakukan pada dokumen. Kategorikan sebagai: (a) Penambahan konten baru, (b) Perbaikan konten yang ada, (c) Penghapusan konten tidak relevan.
- [ ] **J.2** Perbarui **header frontmatter YAML** dokumen:
  - Ubah `versi` dari `1.1` menjadi `1.2`.
  - Perbarui `tanggal` ke tanggal eksekusi validasi ini.
  - Pertahankan `status: Approved`.
  - Pertahankan `penyusun: Senior Database Architect & Data Modeling Specialist`.
- [ ] **J.3** Tambahkan baris baru di **Riwayat Perubahan Dokumen** sebagai baris paling atas tabel (sebelum baris v1.1):
  - Kolom Versi: `1.2`
  - Kolom Tanggal: tanggal eksekusi validasi ini.
  - Kolom Perubahan: Ringkasan singkat semua perubahan yang dilakukan (maksimal 5-7 poin utama).
  - Kolom Oleh: `Senior Database Architect & Data Modeling Specialist`.
- [ ] **J.4** Terapkan seluruh perbaikan yang ditemukan dari Tahap B hingga I ke dalam konten dokumen. Lakukan secara sistematis bab per bab, dari Bab 1 hingga Bab 11. Jangan melewati satu bab pun.
- [ ] **J.5** Jika dalam proses validasi ditemukan kebutuhan untuk **menambahkan referensi file baru** (file yang tidak ada di Bab 10 tetapi digunakan sebagai acuan dalam validasi ini), tambahkan entri baru di **bagian paling bawah Bab 10** dengan nomor urut selanjutnya dan format yang konsisten.
- [ ] **J.6** Perbarui **statistik Bab 2.3** jika ada perubahan jumlah kolom akibat penambahan atau penghapusan kolom (Total Tabel, Total Kolom/Atribut, dll.).
- [ ] **J.7** Perbarui **Matriks Ketertelusuran Bab 8** jika ada perubahan pemetaan tabel ke modul atau ke referensi BRD/SRS.
- [ ] **J.8** **Tulis ulang seluruh dokumen ke file target yang sama** dengan cara menimpa (overwrite) menggunakan perintah penulisan file. Gunakan path persis: `docs/sdlc/02_analysis/05_data_dictionary.md`.
- [ ] **J.9** **LARANGAN MUTLAK — NO TRUNCATION**: Pastikan seluruh teks dokumen dari baris pertama hingga baris terakhir ditulis ulang sepenuhnya. **Dilarang keras** memotong, meringkas, menghilangkan, atau mengganti konten yang tidak berubah dengan komentar seperti `"... (konten selanjutnya sama) ..."` atau `"... (truncated) ..."`. Setiap karakter dokumen harus hadir dalam output akhir.
- [ ] **J.10** Setelah penulisan selesai, **verifikasi ulang** file yang baru ditulis: baca kembali dari baris 1 hingga baris terakhir untuk memastikan tidak ada konten yang terpotong, versi sudah berubah menjadi `1.2`, dan semua perubahan sudah teraplikasikan dengan benar.

---

## 6. Kriteria Keberhasilan

Dokumen revisi `05_data_dictionary.md` v1.2 dinyatakan **BERHASIL** dan siap menjadi input Fase 03 Design apabila memenuhi semua kriteria berikut:

| No | Kriteria | Cara Verifikasi |
|---|---|---|
| 1 | Versi dokumen sudah diperbarui menjadi **v1.2** | Cek header frontmatter YAML |
| 2 | Semua entitas SRS yang relevan sudah terdokumentasi sebagai tabel | Cek Bab 2.1 vs SRS v1.1 |
| 3 | Semua ID SRS-F dan BR-F terpetakan di Bab 8 | Cek Bab 8.2 |
| 4 | Tidak ada kolom kosong/placeholder tanpa nilai | Grep untuk "-", "TBD", "TODO", "N/A" |
| 5 | Semua 28 tabel memiliki `cabang_id` dan kolom audit trail | Cek setiap definisi tabel di Bab 3 |
| 6 | Semua FK terdokumentasi di Bab 5.1 dengan ON DELETE/UPDATE | Cek Bab 5.1 |
| 7 | Nama kolom `user_id` di `stock_opname` sudah diseragamkan menjadi `pengguna_id` | Cek Bab 3.25 dan Bab 5.1 |
| 8 | ERD Mermaid konsisten dengan matriks FK | Bandingkan Bab 2.2 dan Bab 5.1 |
| 9 | Domain Status Opname (Bab 4.19) dirujuk oleh kolom `status_opname` di Bab 3.25 | Cek referensi silang domain |
| 10 | Bahasa Indonesia natural, tidak ambigu, tidak ada kalimat terpotong | Review manual seluruh teks |
| 11 | Dokumen tidak truncated — semua Bab 1-11 hadir lengkap | Cek jumlah baris sebelum vs sesudah |

---

## 7. Batasan & Aturan Eksekusi

1. **Jangan membuat file baru** — semua perubahan ditulis kembali ke `docs/sdlc/02_analysis/05_data_dictionary.md` yang sama dengan cara overwrite.
2. **Jangan mengubah arsitektur** sistem (menambah/menghapus modul AbuCom, mengganti stack teknologi).
3. **Jangan mengubah data seed** yang sudah ditetapkan (nama toko, nomor telepon, alamat) kecuali ditemukan inkonsistensi yang terbukti dengan dokumen referensi.
4. **Jangan menghapus bab atau sub-bab** yang sudah ada — jika ada konten yang tidak relevan, pindahkan ke catatan kaki atau hapus hanya setelah yakin tidak dibutuhkan.
5. **Dokumentasikan semua keputusan** perubahan signifikan di Riwayat Perubahan Dokumen.
6. **Jika tidak yakin** apakah suatu perubahan perlu dilakukan atau tidak, tetap pertahankan konten lama dan tambahkan catatan `> **[CATATAN REVISOR]**: ...` sebagai markup sementara untuk ditinjau oleh Senior Architect.

---

## 8. Referensi Cepat

### File yang Diubah
- **Target (overwrite)**: `docs/sdlc/02_analysis/05_data_dictionary.md`

### File yang Hanya Dibaca (Tidak Diubah)
- `docs/sdlc/02_analysis/01_business_requirements.md`
- `docs/sdlc/02_analysis/02_software_requirements.md`
- `docs/sdlc/02_analysis/03_use_case_diagram.md`
- `docs/sdlc/02_analysis/04_workflow_diagram.md`
- `docs/sdlc/01_planning/01_project_charter.md`
- `docs/sdlc/01_planning/02_feasibility_study.md`
- `docs/sdlc/01_planning/03_stakeholder_register.md`
- `docs/sdlc/01_planning/04_tech_stack_decision.md`
- `docs/sdlc/01_planning/05_innovation_proposal.md`

---

*Issue ini dibuat oleh Antigravity AI Planning Agent pada 2026-05-28 untuk proyek AbuCom — Sistem Manajemen Terpadu Usaha Percetakan.*
