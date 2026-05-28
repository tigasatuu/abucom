# Validasi, Audit, dan Penyempurnaan Dokumen CLI Interaction Flow

---

## Informasi Issue

| Atribut        | Nilai                                                                    |
| :------------- | :----------------------------------------------------------------------- |
| **Judul**      | Validasi, Audit, dan Penyempurnaan Dokumen CLI Interaction Flow          |
| **Dokumen Utama** | CLI Interaction Flow                                                  |
| **Target File** | `docs/sdlc/03_design/04_cli_interaction_flow.md`                        |
| **Lokasi Referensi** | `docs/sdlc/`                                                       |
| **Tipe Issue** | Audit & Validasi Dokumen SDLC                                            |
| **Prioritas**  | Tinggi                                                                   |
| **Status**     | Open                                                                     |
| **Dibuat Pada**| 2026-05-29                                                               |
| **Ditugaskan Kepada** | Junior Programmer / AI Coding Agent                             |

---

## Persona yang Harus Diasumsikan

> **PENTING**: Sebelum memulai pekerjaan apa pun, implementor WAJIB mengasumsikan dan beroperasi sepenuhnya dalam persona berikut ini selama keseluruhan proses eksekusi issue ini.

Anda adalah seorang **Senior CLI UX Architect & SDLC Documentation Quality Auditor** dengan spesialisasi ganda:

1. **Sebagai Arsitek UX CLI Terminal**: Anda memiliki keahlian mendalam dalam merancang antarmuka berbasis teks (*Command Line Interface*) untuk sistem POS/ERP skala UKM, termasuk konvensi navigasi keyboard-only, hierarki menu RBAC multi-peran, wireframe ASCII, dan implementasi pustaka Python seperti `rich` dan `tabulate`. Anda memahami seluk-beluk alur interaksi terminal secara teknis dan operasional.

2. **Sebagai Auditor Kualitas Dokumen SDLC**: Anda menerapkan standar dokumentasi industri yang ketat, memastikan setiap dokumen dalam siklus SDLC bersifat *self-contained*, konsisten lintas referensi, tidak ambigu, dan mampu berdiri sebagai input utama bagi fase berikutnya tanpa memerlukan klarifikasi tambahan. Anda menolak dokumen yang berisi placeholder kosong, data tidak lengkap, atau inkonsistensi terminologi.

**Standar kualitas Anda**: Dokumen dinyatakan lulus validasi hanya jika ia dapat langsung digunakan oleh junior programmer atau AI model yang lebih kecil sebagai acuan implementasi kode Presentation Layer Python, **tanpa harus menebak atau menginterpretasikan informasi yang tidak tercantum eksplisit.**

---

## Latar Belakang dan Konteks

Dokumen `docs/sdlc/03_design/04_cli_interaction_flow.md` (selanjutnya disebut sebagai **Dokumen Utama**) adalah deliverable keempat pada **Fase 03 Design** dalam siklus SDLC proyek **AbuCom — Sistem Manajemen Terpadu Usaha Percetakan**. Dokumen ini berfungsi sebagai:

- Panduan teknis tunggal bagi Developer/AI Coding Agent dalam menyusun seluruh Presentation Layer CLI berbasis Python.
- Acuan skenario pengujian UAT bagi tim Quality Assurance.
- Representasi visual alur operasional toko untuk validasi oleh Pemilik Usaha.

Dokumen ini memetakan 44 Use Case (UC-001 s.d. UC-044), mencakup 10 modul fungsional, hierarki menu, matriks visibilitas RBAC untuk 8 peran, wireframe ASCII, dan matriks ketertelusuran ke UCD, SRS, dan WFD.

**Alasan issue ini dibuat**: Dokumen versi saat ini (v1.1) perlu divalidasi secara menyeluruh untuk memastikan konsistensi, kelengkapan, akurasi lintas referensi, serta kesiapannya sebagai input utama Fase 04 Implementation.

---

## Daftar File Referensi yang Harus Dibaca

Sebelum melakukan analisis apa pun, implementor **WAJIB membaca seluruh file referensi berikut terlebih dahulu** dari awal hingga akhir (baris pertama hingga terakhir):

| No | Nama Dokumen                   | Path Relatif dari Root Proyek                        |
| :-: | :----------------------------- | :--------------------------------------------------- |
| 1  | **Dokumen Utama (Target)**     | `docs/sdlc/03_design/04_cli_interaction_flow.md`     |
| 2  | Use Case Diagram v1.1 (UCD)    | `docs/sdlc/02_analysis/03_use_case_diagram.md`       |
| 3  | Software Requirements (SRS) v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` |
| 4  | Access Control Matrix v1.1 (ACM) | `docs/sdlc/02_analysis/06_access_control_matrix.md` |
| 5  | System Architecture v1.1 (SA)  | `docs/sdlc/03_design/03_system_architecture.md`      |
| 6  | Workflow Diagram v1.1 (WFD)    | `docs/sdlc/02_analysis/04_workflow_diagram.md`       |
| 7  | Database Schema SQL v1.1       | `docs/sdlc/03_design/01_database_schema.sql`         |
| 8  | ERD Database v1.1              | `docs/sdlc/03_design/02_erd_database.md`             |
| 9  | Data Dictionary v1.1           | `docs/sdlc/02_analysis/05_data_dictionary.md`        |
| 10 | Business Requirements (BRD) v1.1 | `docs/sdlc/02_analysis/01_business_requirements.md` |
| 11 | BOM & HPP Design               | `docs/sdlc/03_design/05_bom_hpp_design.md`           |
| 12 | Security Design                | `docs/sdlc/03_design/06_security_design.md`          |

---

## Checklist Tahapan Eksekusi Issue

Eksekusi issue ini harus dilakukan secara **berurutan dari atas ke bawah**. Jangan lompati tahapan. Tandai setiap item dengan `[x]` setelah selesai dikerjakan.

---

### TAHAP 1 — Persiapan dan Pembacaan Dokumen

- [ ] **[BACA-01]** Buka dan baca seluruh isi Dokumen Utama `docs/sdlc/03_design/04_cli_interaction_flow.md` dari baris pertama hingga baris terakhir. Catat versi dokumen saat ini, jumlah total bab, jumlah UC yang terdokumentasi, dan daftar file referensi yang tercantum di bagian akhir.
- [ ] **[BACA-02]** Buka dan baca seluruh isi `docs/sdlc/02_analysis/03_use_case_diagram.md` (UCD v1.1). Catat total jumlah Use Case yang terdefinisi, daftar lengkap UC-ID beserta nama dan aktor primernya.
- [ ] **[BACA-03]** Buka dan baca seluruh isi `docs/sdlc/02_analysis/02_software_requirements.md` (SRS v1.1). Catat semua ID kebutuhan fungsional (SRS-F-xxx) beserta nama dan spesifikasi teknisnya.
- [ ] **[BACA-04]** Buka dan baca seluruh isi `docs/sdlc/02_analysis/06_access_control_matrix.md` (ACM v1.1). Catat semua peran (role) yang terdefinisi, hak akses per modul/tabel, dan aturan eskalasi sandi yang berlaku.
- [ ] **[BACA-05]** Buka dan baca seluruh isi `docs/sdlc/03_design/03_system_architecture.md` (SA v1.1). Catat arsitektur layer yang ditetapkan, konvensi state passing JWT, spesifikasi Functional Programming (FP), dan spesifikasi Presentation Layer.
- [ ] **[BACA-06]** Buka dan baca seluruh isi `docs/sdlc/02_analysis/04_workflow_diagram.md` (WFD v1.1). Catat semua WF-ID, titik keputusan (decision points), dan alur exception workflow yang relevan dengan CLI.
- [ ] **[BACA-07]** Buka dan baca seluruh isi `docs/sdlc/03_design/01_database_schema.sql` (Database Schema v1.1). Catat nama-nama tabel, nama kolom yang relevan dengan input form pada setiap UC (terutama nama kolom status, enum values, tipe data DECIMAL, dan nama kolom ID).
- [ ] **[BACA-08]** Buka dan baca seluruh isi `docs/sdlc/03_design/02_erd_database.md` (ERD v1.1). Catat relasi Foreign Key antar tabel yang relevan untuk memvalidasi konsistensi query SQL di Dokumen Utama.
- [ ] **[BACA-09]** Buka dan baca seluruh isi `docs/sdlc/02_analysis/05_data_dictionary.md` (Data Dictionary v1.1). Catat tipe data, panjang karakter, dan batasan nilai (constraints) setiap kolom yang muncul dalam instruksi input form di Dokumen Utama.
- [ ] **[BACA-10]** Buka dan baca seluruh isi `docs/sdlc/02_analysis/01_business_requirements.md` (BRD v1.1). Catat konteks bisnis, SOP operasional, dan rule bisnis spesifik percetakan yang harus tercermin dalam alur CLI.
- [ ] **[BACA-11]** Buka dan baca seluruh isi `docs/sdlc/03_design/05_bom_hpp_design.md`. Catat spesifikasi teknis perhitungan BOM dan HPP yang harus selaras dengan alur interaksi UC-007 (Hitung HPP BOM).
- [ ] **[BACA-12]** Buka dan baca seluruh isi `docs/sdlc/03_design/06_security_design.md`. Catat standar keamanan yang berlaku — termasuk spesifikasi JWT, bcrypt cost factor, enkripsi, mekanisme eskalasi sandi — yang harus konsisten dengan yang dituliskan di Dokumen Utama.

---

### TAHAP 2 — Validasi Kelengkapan: Apakah Semua Data dari Referensi Sudah Terserap?

*Tujuan: Memastikan tidak ada data/informasi penting dari file referensi yang terlewat atau hilang dalam Dokumen Utama.*

- [ ] **[VAL-01]** Bandingkan daftar UC-ID di UCD v1.1 (hasil BACA-02) dengan daftar UC yang terdokumentasi dalam Dokumen Utama. **Buat daftar UC yang ada di UCD tetapi BELUM memiliki Bab alur interaksi di Dokumen Utama**. Jika ada yang terlewat, tandai sebagai gap yang harus diperbaiki.
- [ ] **[VAL-02]** Verifikasi bahwa setiap UC di Dokumen Utama memiliki atribut header lengkap: `Derivasi UC`, `Derivasi SRS`, `Derivasi WF`, `Modul`, `Aktor Primer`, `Menu ID`, dan `Hak Akses`. Buat daftar UC yang memiliki atribut kosong atau tidak lengkap.
- [ ] **[VAL-03]** Bandingkan semua SRS-F-ID yang terdaftar di SRS v1.1 (hasil BACA-03) dengan SRS-F-ID yang tercantum dalam Traceability Matrix Bab 16 Dokumen Utama. **Identifikasi SRS-F-ID yang ada di SRS tetapi tidak terpetakan di Bab 16.2**. Jika ada gap, tambahkan baris yang hilang.
- [ ] **[VAL-04]** Bandingkan semua WF-ID yang terdaftar di WFD v1.1 (hasil BACA-06) dengan WF-ID yang tercantum dalam Traceability Matrix Bab 16.3 Dokumen Utama. **Identifikasi WF-ID yang belum terpetakan**. Jika ada gap, tambahkan baris yang hilang.
- [ ] **[VAL-05]** Periksa apakah seluruh kode error standar yang terdefinisi di SRS v1.1 (hasil BACA-03) sudah tercantum dalam tabel pesan error yang relevan pada setiap UC di Dokumen Utama. Identifikasi kode error yang ada di SRS tetapi tidak muncul di UC yang sesuai.
- [ ] **[VAL-06]** Periksa apakah setiap query SQL yang ditampilkan dalam langkah interaksi (contoh: `SELECT`, `UPDATE`, `INSERT`) sudah menggunakan nama tabel dan nama kolom yang **persis sama** dengan yang terdefinisi di Database Schema SQL v1.1 (hasil BACA-07). Buat daftar inkonsistensi nama tabel/kolom yang ditemukan.
- [ ] **[VAL-07]** Periksa apakah nilai-nilai enum yang digunakan dalam query SQL di Dokumen Utama (contoh: `'LUNAS'`, `'BELUM LUNAS'`, `'RETUR'`, `'KASBON'`, `'DIAMBIL'`, dll.) sudah sesuai persis dengan nilai enum yang terdefinisi di Database Schema SQL v1.1 dan Data Dictionary v1.1 (hasil BACA-07 dan BACA-09).
- [ ] **[VAL-08]** Verifikasi apakah aturan hak akses per UC yang tercantum dalam kolom "Hak Akses" pada atribut header setiap UC sudah selaras dengan aturan yang terdefinisi di ACM v1.1 (hasil BACA-04). Buat daftar ketidaksesuaian yang ditemukan.
- [ ] **[VAL-09]** Verifikasi apakah Matriks Visibilitas Menu per Role (Bab 3.3) sudah konsisten dengan data akses yang terdefinisi di ACM v1.1. Periksa setiap baris menu untuk semua 8 peran apakah nilai `Tampil`/`Sembunyi` sudah akurat.
- [ ] **[VAL-10]** Periksa apakah spesifikasi teknis Presentation Layer yang disebutkan di Dokumen Utama (penggunaan `rich`, `tabulate`, `getpass`, `pathlib`, ANSI Color, bcrypt cost factor, JWT HS256, dsb.) sudah selaras dengan spesifikasi yang ditetapkan di SA v1.1 (hasil BACA-05) dan Security Design (hasil BACA-12).
- [ ] **[VAL-11]** Periksa apakah formula dan logika bisnis yang disebutkan dalam langkah interaksi (contoh: formula margin, logika smart payroll bagi hasil, formula prediksi re-order, logika tier insentif, logika straight-line depreciation) sudah selaras dengan spesifikasi yang ada di SRS v1.1, BRD v1.1, dan BOM HPP Design.
- [ ] **[VAL-12]** Verifikasi kelengkapan Glosarium (Bab 18): Pastikan semua istilah teknis kunci yang digunakan dalam Dokumen Utama (termasuk istilah yang muncul di bab-bab alur interaksi seperti `eskalasi sandi`, `laci kasir`, `status_pengambilan`, dll.) sudah terdefinisi di Glosarium. Tambahkan entri yang belum ada.

---

### TAHAP 3 — Validasi Relevansi: Apakah Dokumen Sudah Bersih dan Fokus?

*Tujuan: Memastikan Dokumen Utama tidak memuat konten yang tidak relevan atau di luar cakupannya sebagai dokumen CLI Interaction Flow.*

- [ ] **[REL-01]** Periksa apakah ada bagian atau sub-bab yang berisi penjelasan arsitektur sistem (misalnya detail implementasi layering, detail desain database skema) yang seharusnya hanya ada di SA v1.1 atau Database Schema. Jika ada, nilai apakah penjelasan tersebut memang diperlukan sebagai konteks CLI atau cukup diganti dengan referensi ke dokumen yang tepat.
- [ ] **[REL-02]** Periksa apakah ada query SQL yang ditampilkan secara penuh tetapi sebenarnya terlalu detail untuk konteks dokumen Interaction Flow (seharusnya cukup menyebutkan operasi database yang dilakukan, bukan query literal DDL). Nilai apakah level detail ini konsisten dan perlu dipertahankan untuk kepentingan implementasi.
- [ ] **[REL-03]** Periksa apakah ada informasi yang duplikat antara satu UC dengan UC lain tanpa menambah nilai (misalnya penjelasan cara kerja RBAC yang diulang identik di setiap UC). Nilai apakah bagian tersebut perlu dikonsolidasi ke Bab Prinsip Desain atau cukup dirujuk saja.
- [ ] **[REL-04]** Periksa apakah Bab Wireframe ASCII (Bab 15) hanya mencakup layar-layar yang memang perlu divisualisasikan khusus (layar login, dashboard utama, dan layar kritis lainnya) dan bukan merupakan pengulangan informasi yang sudah ada di langkah interaksi detail.

---

### TAHAP 4 — Validasi Standar Struktur Dokumen

*Tujuan: Memastikan dokumen memiliki struktur yang sesuai standar industri, lengkap, dan informatif.*

- [ ] **[STR-01]** Periksa apakah header YAML frontmatter (bagian antara `---`) sudah lengkap dengan field: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, dan `penyusun`. Nilai apakah field `status` sudah mencerminkan kondisi terkini dokumen (apakah `Draft`, `Review`, atau `Approved`).
- [ ] **[STR-02]** Periksa apakah Riwayat Perubahan Dokumen (Bab di awal) mencatat semua versi dokumen dengan kolom: `Versi`, `Tanggal`, `Perubahan`, dan `Oleh`. Pastikan tidak ada versi yang terlewat.
- [ ] **[STR-03]** Periksa apakah Bab 1 (Informasi Dokumen) memiliki semua sub-bab yang diperlukan: Tujuan, Cakupan, Posisi dalam SDLC, Hubungan dengan Dokumen SDLC Lain (Input dan Output), Audiens Target, dan Definisi/Akronim/Singkatan. Nilai kelengkapan isi setiap sub-bab.
- [ ] **[STR-04]** Periksa apakah setiap Bab Alur Interaksi (Bab 4 s.d. Bab 14) memiliki struktur yang **konsisten**: (a) tabel atribut header UC, (b) diagram Mermaid alur interaksi (setidaknya untuk UC utama/kritis), (c) tabel langkah-langkah interaksi detail, dan (d) tabel pesan error. Identifikasi UC yang struktur babnya tidak lengkap.
- [ ] **[STR-05]** Periksa apakah kolom pada tabel langkah-langkah interaksi detail sudah konsisten di seluruh dokumen: `No.`, `Aktor/Sistem`, `Aksi`, `Tipe` (Input/Output/Proses), `Contoh Tampilan/Input`. Identifikasi tabel yang menggunakan format kolom berbeda.
- [ ] **[STR-06]** Periksa apakah kolom pada tabel pesan error sudah konsisten di seluruh dokumen: `Kode Error`, `Pemicu`, `Pesan yang Ditampilkan`. Identifikasi tabel yang menggunakan format kolom berbeda atau tidak konsisten.
- [ ] **[STR-07]** Periksa apakah Bab 16 (Matriks Ketertelusuran) memiliki ketiga tabel mapping yang diperlukan: (a) ke UCD, (b) ke SRS, dan (c) ke WFD. Nilai apakah kolom status mapping sudah terisi dengan benar.
- [ ] **[STR-08]** Periksa apakah Bab 17 (Persetujuan dan Otorisasi) sudah menggunakan nama stakeholder yang nyata dan bukan placeholder seperti `[Nama Pemilik]`. Jika masih ada placeholder, ganti dengan nama yang sesuai (Nama pemilik: **Hadi Wibowo**).
- [ ] **[STR-09]** Periksa apakah Bab 18 (Glosarium) sudah mencakup semua istilah teknis kunci dari seluruh dokumen secara alfabetis atau terurut logis. Periksa apakah ada entri yang tidak konsisten dengan definisi yang digunakan dalam badan teks.
- [ ] **[STR-10]** Periksa apakah Bab 19 (Referensi Dokumen) sudah memuat semua file referensi yang benar-benar dirujuk dalam Dokumen Utama, dengan kolom: `No`, `Nama Dokumen Referensi`, `Path Relatif`, dan `Keterangan Versi`. Verifikasi bahwa path file yang tercantum adalah path yang valid dan benar di repositori proyek.

---

### TAHAP 5 — Validasi Kesiapan sebagai Input Fase Berikutnya

*Tujuan: Memastikan Dokumen Utama dapat langsung digunakan sebagai acuan implementasi Fase 04 dan skenario pengujian Fase 05 tanpa memerlukan klarifikasi tambahan.*

- [ ] **[INPUT-01]** Untuk setiap UC, periksa apakah contoh input/output yang disajikan dalam langkah interaksi sudah **konkret dan spesifik**. Contoh yang baik mencantumkan: tipe data Python (string, int, Decimal), panjang karakter maksimum, format nilai (contoh: `YYYY-MM-DD`), dan nilai contoh yang nyata (bukan placeholder seperti `[nilai]`). Identifikasi langkah yang masih menggunakan contoh abstrak/generik.
- [ ] **[INPUT-02]** Periksa apakah setiap tabel pesan error sudah mencantumkan **semua kemungkinan error** yang dapat terjadi pada alur UC tersebut (termasuk error koneksi database ERR-DB-xxx, error validasi input ERR-VAL-xxx, error sesi ERR-SESSION-xxx). Identifikasi UC yang tabel errornya tidak lengkap.
- [ ] **[INPUT-03]** Periksa apakah alur interaksi untuk UC yang memerlukan **eskalasi sandi supervisor** (contoh: UC-004 Retur, UC-021 Payroll, UC-031 Pengeluaran Rutin) sudah mencantumkan langkah eskalasi secara eksplisit dengan: (a) pemicu kondisi eskalasi, (b) prompt yang ditampilkan, (c) proses validasi bcrypt, dan (d) error jika sandi salah.
- [ ] **[INPUT-04]** Periksa apakah alur interaksi untuk UC yang memerlukan **konfirmasi destruktif `[Y/N]`** (contoh: UC-011 Stock Opname, UC-016 Backup/Restore, UC-021 Payroll, UC-034 Handover) sudah mencantumkan langkah konfirmasi secara eksplisit.
- [ ] **[INPUT-05]** Periksa apakah setiap UC yang memodifikasi data (INSERT/UPDATE/DELETE) sudah menyebutkan bahwa operasi database dilakukan dalam **transaksi ACID** (START TRANSACTION / COMMIT / ROLLBACK) dan bahwa **audit log** dicatat setelah operasi berhasil.
- [ ] **[INPUT-06]** Periksa apakah diagram hierarki menu (Bab 3.1) sudah konsisten dengan nomor urut hotkey numerik yang ditampilkan dalam langkah interaksi setiap UC. Verifikasi bahwa nomor sub-menu yang disebutkan di langkah interaksi sesuai dengan posisi di Mermaid tree.
- [ ] **[INPUT-07]** Periksa apakah Bab 2 (Prinsip Desain) sudah menjelaskan **semua konvensi** yang digunakan dalam langkah interaksi di seluruh dokumen: konvensi format breadcrumb, konvensi format prompt input, konvensi tombol `0` untuk kembali, konvensi format kode error, dan konvensi ANSI Color. Tambahkan sub-bab atau poin yang masih kurang.
- [ ] **[INPUT-08]** Periksa apakah Bab Wireframe ASCII (Bab 15) sudah mencakup layar-layar yang paling kritis bagi implementasi Presentation Layer: (a) Layar Login, (b) Dashboard per role minimal untuk role pemilik dan kasir, (c) minimal satu contoh tampilan form input, dan (d) minimal satu contoh tampilan tabel data/laporan. Tambahkan wireframe yang masih kurang jika diperlukan.
- [ ] **[INPUT-09]** Periksa apakah alur interaksi untuk **UC lintas modul** (contoh: UC-001 yang memanggil UC-007, UC-022, UC-006; UC-003 yang terhubung dengan UC-024) sudah mencantumkan langkah pemanggilan UC lain secara eksplisit beserta kondisi yang memicunya.

---

### TAHAP 6 — Validasi Kualitas Bahasa Indonesia

*Tujuan: Memastikan seluruh teks menggunakan Bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami.*

- [ ] **[LANG-01]** Baca ulang Bab 1 (Informasi Dokumen) secara saksama. Periksa apakah ada kalimat yang menggunakan campuran Bahasa Indonesia dan Bahasa Inggris yang tidak perlu, kalimat pasif yang ambigu, atau istilah teknis tanpa penjelasan pertama kali muncul. Perbaiki kalimat yang ditemukan.
- [ ] **[LANG-02]** Baca ulang Bab 2 (Prinsip Desain). Periksa konsistensi penulisan nama-nama pustaka dan modul Python: apakah selalu ditulis dalam format `backtick` (contoh: `rich`, `tabulate`, `getpass`). Periksa apakah semua konvensi dijelaskan dengan bahasa imperatif yang jelas (gunakan kata kerja aktif: "sistem menampilkan", "pengguna mengetikkan", bukan "ditampilkan" tanpa subjek yang jelas).
- [ ] **[LANG-03]** Sampel acak 5 UC dari bab alur interaksi berbeda (pilih UC dari modul M.1, M.4, M.7, M.8, dan M.10). Baca langkah-langkah interaksinya dan periksa: (a) apakah kolom `Aksi` sudah mendeskripsikan aksi secara aktif dan spesifik, (b) apakah kolom `Contoh Tampilan/Input` sudah menggunakan contoh nyata dan bukan placeholder, (c) apakah ada istilah yang digunakan tidak konsisten dengan Glosarium (Bab 18).
- [ ] **[LANG-04]** Periksa seluruh tabel pesan error di Dokumen Utama. Pastikan kolom "Pesan yang Ditampilkan" menggunakan Bahasa Indonesia yang jelas, deskriptif, dan informatif bagi pengguna kasir. Pesan tidak boleh menggunakan jargon teknis yang tidak dipahami oleh staf kasir biasa.
- [ ] **[LANG-05]** Periksa apakah ada inkonsistensi penulisan nama peran pengguna (role) di seluruh dokumen. Nama role harus konsisten menggunakan format lowercase dengan underscore seperti yang terdefinisi di Database Schema: `pemilik`, `kepala_percetakan`, `pramuniaga`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang`. Buat daftar inkonsistensi yang ditemukan dan perbaiki.

---

### TAHAP 7 — Validasi Kecukupan untuk Mencegah Interupsi Fase Berikutnya

*Tujuan: Memastikan tidak ada "lubang informasi" yang akan memaksa tim implementasi berhenti dan menanyakan hal-hal yang seharusnya sudah tercantum di dokumen ini.*

- [ ] **[STOP-01]** Lakukan review akhir dengan memposisikan diri sebagai junior programmer yang baru pertama kali membaca dokumen ini. Tanyakan: "Apakah ada aksi atau kondisi dalam alur UC yang tidak jelas bagaimana penanganannya?" Buat daftar pertanyaan yang muncul, lalu pastikan setiap pertanyaan tersebut sudah terjawab di dalam Dokumen Utama. Jika belum, tambahkan penjelasan yang diperlukan.
- [ ] **[STOP-02]** Periksa apakah semua UC yang memiliki kondisi bersyarat (IF/ELSE/ALT) sudah mendokumentasikan **semua cabang kondisi** secara eksplisit. Contoh: UC-001 harus mendokumentasikan skenario barang kustom (BOM) DAN barang retail; UC-003 harus mendokumentasikan skenario input DP baru DAN skenario proses pelunasan. Identifikasi UC yang hanya mendokumentasikan satu cabang kondisi.
- [ ] **[STOP-03]** Periksa apakah nilai-nilai batas (threshold) yang disebutkan dalam langkah interaksi sudah diverifikasi keakuratannya terhadap referensi: (a) Batas minimal saldo PPOB alert: Rp 150.000 (SRS-F-015), (b) Batas eskalasi pengeluaran rutin: Rp 500.000 (SRS-F-029), (c) Batas gagal login lockout: 5 kali / 10 menit (SA/Security), (d) Bcrypt cost factor: 12 (Security Design), (e) JWT expiry: 8 jam (SA), (f) Target re-order H-7 dan H-3. Koreksi nilai yang tidak sesuai referensi.
- [ ] **[STOP-04]** Periksa apakah semua nama file output yang disebutkan dalam dokumen (contoh: format file nota thermal, format file ZIP backup, format nama file audit log JSON) sudah terdefinisi secara konsisten dan spesifik, termasuk konvensi penamaan file dan direktori penyimpanannya.

---

### TAHAP 8 — Validasi dan Pengisian Data Kosong/Placeholder

*Tujuan: Memastikan tidak ada data yang dibiarkan kosong, bertanda `[TBD]`, atau berupa placeholder yang belum diisi.*

- [ ] **[FILL-01]** Lakukan pencarian (`Ctrl+F` / `grep`) di seluruh Dokumen Utama untuk menemukan string-string placeholder berikut: `[TBD]`, `[TODO]`, `[PENDING]`, `[?]`, `[Nama]`, `[...]`, `..........`, `#FIXME`, `N/A` (yang bermakna "belum tersedia"), dan `placeholder`. Catat baris dan konteksnya.
- [ ] **[FILL-02]** Untuk setiap placeholder yang ditemukan pada FILL-01, isi dengan data yang akurat, relevan, dan sesuai dengan konteks dokumen dan data dari file referensi. Jika data tidak dapat ditentukan dari referensi yang ada, gunakan data yang paling logis dan konsisten dalam ruang lingkup proyek AbuCom.
- [ ] **[FILL-03]** Periksa apakah Bab 17 (Persetujuan dan Otorisasi) masih memiliki kolom "Tanda Tangan" yang kosong. Ini adalah field yang memang kosong secara by design (menunggu tanda tangan fisik/digital), sehingga tidak perlu diisi tetapi perlu dipastikan formatnya sudah benar.
- [ ] **[FILL-04]** Periksa apakah ada UC yang atribut header-nya memiliki nilai kosong pada kolom `Derivasi WF`. Jika sebuah UC memang tidak memiliki WF-ID yang eksplisit terkait (karena hanya merupakan subprocess), nilai harus diisi dengan keterangan yang jelas, misalnya: `N/A (Subprocess internal dari UC-XXX)` atau `WF-XX-XX (Subprocess)`.
- [ ] **[FILL-05]** Periksa apakah data konfigurasi toko yang muncul dalam contoh-contoh (nama toko, nama pemilik, data laci kasir awal, batas threshold) sudah menggunakan data yang relevan dan konsisten dengan yang terdefinisi di BRD v1.1 dan Database Schema v1.1.

---

### TAHAP 9 — Validasi Spesifik Ciri Khas Dokumen CLI Interaction Flow

*Tujuan: Memvalidasi aspek-aspek unik yang hanya relevan untuk dokumen jenis CLI Interaction Flow.*

- [ ] **[CLI-01]** **Konsistensi Breadcrumb Path**: Periksa apakah format breadcrumb yang ditampilkan dalam contoh langkah interaksi di seluruh UC sudah konsisten dan mencerminkan hierarki menu yang benar sesuai Bab 3.1. Format yang benar: `Dashboard > M.X NamaModul > Nama Sub-Menu UC`. Identifikasi UC yang breadcrumb-nya tidak konsisten atau salah.
- [ ] **[CLI-02]** **Konsistensi Prompt Input**: Periksa apakah semua prompt input berakhir dengan titik dua dan spasi (`: `), sesuai konvensi yang ditetapkan. Identifikasi prompt yang tidak mengikuti konvensi ini.
- [ ] **[CLI-03]** **Konvensi Tombol `0` Kembali**: Periksa apakah setiap layar sub-menu atau form input di seluruh UC sudah menyebutkan opsi `[0-Kembali]` atau `[0-Batal]` dalam prompt pilihannya. Identifikasi UC yang tidak menyertakan opsi keluar ini.
- [ ] **[CLI-04]** **Konsistensi Format Nomor Invoice**: Periksa apakah format ID invoice yang disebutkan dalam contoh (contoh: `INV-20260524-001`) sudah konsisten di seluruh dokumen dan sesuai dengan konvensi yang ditetapkan di SRS v1.1 atau Database Schema.
- [ ] **[CLI-05]** **Validasi Diagram Mermaid**: Periksa apakah semua blok diagram Mermaid dalam dokumen menggunakan sintaks yang valid dan konsisten (tidak ada karakter ilegal, label node tidak terlalu panjang, arrow style yang konsisten). Identifikasi diagram yang berpotensi tidak dapat di-render.
- [ ] **[CLI-06]** **Kelengkapan Diagram Mermaid per UC Kritis**: Verifikasi apakah UC-UC berikut yang bersifat kompleks dan kritis sudah memiliki diagram Mermaid alur interaksi (bukan hanya tabel langkah): UC-041 (Login), UC-001 (Transaksi), UC-004 (Retur), UC-011 (Stock Opname), UC-021 (Payroll), UC-034 (Handover), UC-035 (Rekonsiliasi Kas). Tambahkan diagram yang belum ada.
- [ ] **[CLI-07]** **Konsistensi Kode Error Format**: Periksa apakah semua kode error di seluruh dokumen menggunakan format yang benar: `ERR-[KATEGORI]-[NOMOR]` (contoh: `ERR-AUTH-001`, `ERR-VAL-003`). Pastikan kategori yang digunakan hanya yang terdefinisi di Bab 2.5. Identifikasi kode error yang menggunakan format berbeda.
- [ ] **[CLI-08]** **Konsistensi ANSI Color Usage**: Periksa apakah semua contoh output dalam langkah interaksi yang menggunakan warna sudah menggunakan warna yang sesuai konvensi Bab 2.3: Hijau untuk sukses, Merah untuk error kritis, Kuning untuk peringatan/konfirmasi, Biru untuk panduan input, Magenta untuk judul modul. Identifikasi ketidaksesuaian.
- [ ] **[CLI-09]** **Validasi Nomor UC di Hierarki Menu**: Periksa ulang apakah semua node dalam diagram Mermaid Bab 3.1 dan tabel Bab 3.2 sudah mencantumkan UC-ID yang benar dan konsisten dengan yang terdefinisi di UCD v1.1. Verifikasi tidak ada UC-ID yang salah nomor atau tertukar.
- [ ] **[CLI-10]** **Kelengkapan Alur UC-041 s.d. UC-044 (Use Case Dasar)**: UC dasar ini adalah fondasi operasional sistem. Periksa apakah alur Login (UC-041) sudah mencakup: banner ASCII, getpass, bcrypt verify, JWT encode, dan state passing ke dashboard. Periksa apakah Dashboard (UC-043) sudah mendeskripsikan tampilan spesifik untuk **minimal 3 role berbeda** (pemilik, kasir, gudang).

---

### TAHAP 10 — Penulisan Ulang Dokumen Final (Overwrite)

*Tujuan: Menuangkan kembali seluruh dokumen yang telah divalidasi dan diperbaiki ke file target yang sama.*

- [ ] **[WRITE-01]** Setelah seluruh tahap validasi (Tahap 1 s.d. 9) selesai dikerjakan dan semua temuan sudah diperbaiki, buka file target: `docs/sdlc/03_design/04_cli_interaction_flow.md`.
- [ ] **[WRITE-02]** Perbarui field `versi` pada YAML frontmatter (baris pertama dokumen): ubah dari versi saat ini ke versi berikutnya. Aturan: jika versi saat ini adalah `1.1`, maka ubah menjadi `1.2`. Jika `1.2`, ubah menjadi `1.3`, dan seterusnya.
- [ ] **[WRITE-03]** Perbarui field `tanggal` pada YAML frontmatter dengan tanggal eksekusi issue ini (tanggal hari ini dalam format `YYYY-MM-DD`).
- [ ] **[WRITE-04]** Tambahkan baris baru pada tabel Riwayat Perubahan Dokumen (di bagian awal setelah frontmatter). Baris baru ini harus mencantumkan: versi baru, tanggal hari ini, ringkasan singkat seluruh perubahan yang dilakukan dalam proses validasi ini, dan persona penyusun.
- [ ] **[WRITE-05]** Tulis ulang **seluruh isi dokumen** dari baris pertama hingga baris terakhir ke file `docs/sdlc/03_design/04_cli_interaction_flow.md` dengan cara **overwrite (menimpa)**. **PERHATIAN KRITIS**:
  - **DILARANG KERAS** memotong, meringkas, atau menghilangkan bagian apa pun dari dokumen.
  - **DILARANG KERAS** menggantikan konten yang panjang dengan komentar seperti `[... konten sama ...]`, `[... dst ...]`, `[sisa konten tidak berubah ...]`, atau sejenisnya.
  - Seluruh teks dari baris pertama (YAML frontmatter `---`) hingga baris terakhir (baris setelah Bab 19 Referensi) **HARUS ditulis ulang sepenuhnya** tanpa ada yang dipotong.
  - Jika ukuran dokumen sangat besar dan tidak muat dalam satu operasi tulis, pecah menjadi beberapa operasi tulis berurutan (append), tetapi pastikan tidak ada konten yang terlewat.
- [ ] **[WRITE-06]** Setelah penulisan selesai, baca kembali 30 baris pertama dan 30 baris terakhir file yang baru ditulis untuk memverifikasi bahwa file berhasil ditulis dengan benar (tidak terpotong di tengah, tidak ada error encoding).
- [ ] **[WRITE-07]** Verifikasi bahwa ukuran file (total bytes/jumlah baris) hasil penulisan tidak lebih kecil dari ukuran file sebelum divalidasi (sebagai indikator bahwa tidak ada konten yang terpotong). Jika file hasil lebih kecil, ini adalah tanda kuat adanya konten yang hilang — lakukan penulisan ulang.

---

### TAHAP 11 — Pembaruan Referensi Dokumen (Bab 19)

*Tujuan: Memastikan semua file referensi yang digunakan dalam proses validasi ini sudah tercatat di bagian akhir Dokumen Utama.*

- [ ] **[REF-01]** Setelah penulisan ulang (WRITE-05) selesai, periksa kembali Bab 19 (Referensi Dokumen) pada file yang telah ditulis. Bandingkan dengan daftar file referensi yang digunakan dalam proses validasi ini (lihat TAHAP 1).
- [ ] **[REF-02]** Jika selama proses validasi ditemukan bahwa dokumen lain (yang tidak ada dalam daftar referensi awal di Bab 19) juga berkontribusi sebagai sumber informasi atau acuan validasi, tambahkan dokumen tersebut sebagai baris baru di tabel Bab 19 dengan format kolom yang sama: `No`, `Nama Dokumen Referensi`, `Path Relatif`, `Keterangan Versi`.
- [ ] **[REF-03]** Pastikan semua path file referensi yang tercantum di Bab 19 menggunakan path relatif yang valid (dapat diakses dari root proyek). Koreksi path yang salah atau tidak valid.
- [ ] **[REF-04]** Nomor urut baris di tabel Bab 19 harus berurutan dari 1 tanpa loncat. Jika ada baris yang ditambahkan, pastikan penomoran diperbarui.

---

## Kriteria Keberhasilan (Definition of Done)

Issue ini dinyatakan **SELESAI** jika dan hanya jika seluruh kondisi berikut terpenuhi:

- [ ] Semua checkbox pada Tahap 1 s.d. 11 telah ditandai `[x]`.
- [ ] File `docs/sdlc/03_design/04_cli_interaction_flow.md` berhasil ditimpa dengan konten yang telah divalidasi, diperbaiki, dan diperbaharui versinya.
- [ ] Versi dokumen dalam YAML frontmatter telah meningkat (contoh: dari `1.1` menjadi `1.2`).
- [ ] Tabel Riwayat Perubahan telah diperbarui dengan entri versi baru.
- [ ] Tidak ada satu pun placeholder kosong, data `[TBD]`, atau field yang belum terisi yang tersisa di dokumen final.
- [ ] Seluruh bab dan sub-bab dalam dokumen final tidak ada yang terpotong, diringkas, atau hilang dibandingkan dokumen awal (sebelum validasi), ditambah dengan konten perbaikan dan penambahan baru.
- [ ] Tidak ada inkonsistensi antara nama tabel/kolom SQL dalam dokumen dengan Database Schema v1.1.
- [ ] Tidak ada inkonsistensi hak akses menu dengan ACM v1.1.
- [ ] Semua UC yang terdaftar di UCD v1.1 sudah terdokumentasikan dalam Dokumen Utama.
- [ ] Jika ada file referensi baru yang digunakan selama validasi, sudah ditambahkan di Bab 19 Referensi Dokumen.

---

## Catatan Penting untuk Implementor

> [!IMPORTANT]
> **Jangan pernah meringkas atau menghilangkan konten.** Jika Anda adalah AI model dengan batas panjang output, pecah penulisan dokumen menjadi beberapa bagian berurutan menggunakan operasi append, bukan replace. Pastikan setiap bagian langsung disambung tanpa celah atau duplikasi.

> [!WARNING]
> **Verifikasi nama kolom database secara teliti.** Nama kolom seperti `status_pembayaran`, `status_pengambilan`, `status_kasbon`, `jumlah_kasbon`, `nominal_kasbon`, `sisa_tagihan`, `id_cabang`, `cabang_id` sering menjadi sumber inkonsistensi. Selalu cross-check dengan `docs/sdlc/03_design/01_database_schema.sql` sebagai sumber kebenaran tunggal (Single Source of Truth / SSoT).

> [!CAUTION]
> **Jangan mengubah logika bisnis yang sudah benar.** Tugas Anda adalah memvalidasi dan melengkapi, bukan mendesain ulang. Jika Anda menemukan sesuatu yang tampak "aneh" tetapi konsisten dengan SRS dan BRD, itu kemungkinan adalah rule bisnis yang disengaja. Tandai untuk dikonfirmasi, tetapi jangan mengubahnya tanpa dasar referensi yang jelas.

> [!NOTE]
> **Prioritas perbaikan**: Jika menemukan banyak temuan, prioritaskan dalam urutan berikut: (1) inkonsistensi nama kolom/tabel SQL, (2) UC yang belum terdokumentasikan, (3) data placeholder kosong, (4) inkonsistensi hak akses, (5) perbaikan bahasa dan format.

---

## Referensi Issue Terkait

| No | Issue ID | Keterkaitan |
| :-: | :--- | :--- |
| 1 | ISSUE-0074 | Validasi Database Schema SQL — SSoT nama kolom dan tipe data |
| 2 | ISSUE-0075 | Validasi ERD Database — Referensi relasi tabel dan FK |
| 3 | ISSUE-0076 | Validasi System Architecture — Acuan spesifikasi Presentation Layer |

---

*Dokumen issue ini dibuat pada 2026-05-29 sebagai bagian dari siklus quality assurance dokumentasi SDLC proyek AbuCom.*
