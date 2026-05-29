---
judul       : Validasi, Audit, dan Penyempurnaan Dokumen BOM & HPP Design
target_file : docs/sdlc/03_design/05_bom_hpp_design.md
prioritas   : High
status      : Open
dibuat      : 2026-05-29
assignee    : Junior Programmer / AI Coding Agent
---

# Validasi, Audit, dan Penyempurnaan Dokumen BOM & HPP Design

## 1. Konteks dan Latar Belakang

Dokumen **BOM & HPP Design** (`docs/sdlc/03_design/05_bom_hpp_design.md`) adalah deliverable kelima pada Fase 03 Design dalam siklus SDLC proyek AbuCom. Dokumen ini berfungsi sebagai **Single Source of Truth (SSoT)** bagi pengembang backend dalam mengimplementasikan modul `logic/bom_hpp.py`, dan menjadi acuan utama tim QA dalam merancang integration test suite untuk validasi kalkulasi HPP dan transaksional stok.

Issue ini menginstruksikan untuk melakukan audit menyeluruh, validasi mendalam, dan penyempurnaan dokumen tersebut sebelum fase implementasi kode dimulai. Seluruh pekerjaan harus dilakukan **secara bertahap, terurut, dan terdokumentasi** menggunakan checklist di bawah ini.

---

## 2. Persona yang Harus Diterapkan

Sebelum memulai pekerjaan, **adopsi secara penuh** persona berikut:

> **Anda adalah seorang Principal Manufacturing Systems Architect & Certified Cost Accounting Specialist** dengan pengalaman lebih dari 15 tahun merancang sistem ERP manufaktur berbasis SQL dan Python. Anda memiliki keahlian mendalam dalam:
> - Perancangan skema database relasional (DDL/ERD) untuk sistem inventaris dan BOM manufaktur.
> - Standar akuntansi biaya produksi (Cost Accounting) dan COGS calculation.
> - Paradigma Functional Programming (FP) murni di Python dengan presisi `decimal.Decimal`.
> - Penulisan dokumen teknis SDLC tingkat industri yang digunakan sebagai referensi utama tim developer dan QA.
> - Audit ketertelusuran dokumen (Traceability Matrix) antar fase SDLC.
>
> Anda dikenal **sangat kritis, tidak toleran terhadap ambiguitas**, dan memastikan setiap dokumen desain yang Anda validasi tidak akan menimbulkan pertanyaan saat diimplementasikan oleh developer yang lebih junior.

---

## 3. File yang Harus Dibaca (Wajib Sebelum Memulai)

Baca seluruh file berikut secara berurutan dan **pahami isinya secara menyeluruh** sebelum melakukan analisis apapun. Jangan melakukan modifikasi apapun pada tahap ini.

- [ ] **[BACA]** `docs/sdlc/03_design/05_bom_hpp_design.md` — Dokumen utama target validasi (baca seluruh isinya dari baris pertama hingga terakhir, jangan ada yang dilewati).
- [ ] **[BACA]** `docs/sdlc/03_design/01_database_schema.sql` — Skema fisik DDL database SSoT (acuan utama untuk validasi DDL di dokumen target).
- [ ] **[BACA]** `docs/sdlc/03_design/02_erd_database.md` — ERD Crow's Foot database (acuan integritas relasional dan kardinalitas entitas).
- [ ] **[BACA]** `docs/sdlc/03_design/03_system_architecture.md` — Panduan arsitektur sistem (acuan paradigma FP murni, connection handling, State Dictionary Passing, dan struktur direktori proyek).
- [ ] **[BACA]** `docs/sdlc/03_design/04_cli_interaction_flow.md` — Alur interaksi CLI (acuan mapping menu, kode perintah CLI, dan alur penggunaan modul BOM & HPP dari sisi antarmuka).
- [ ] **[BACA]** `docs/sdlc/02_analysis/02_software_requirements.md` — SRS lengkap (acuan validasi kode SRS-F yang direferensikan di dokumen target: SRS-F-005, SRS-F-007, SRS-F-008, SRS-F-009, SRS-F-010).
- [ ] **[BACA]** `docs/sdlc/02_analysis/04_workflow_diagram.md` — Workflow Diagram To-Be (acuan alur proses bisnis yang harus selaras dengan flowchart di dokumen target).
- [ ] **[BACA]** `docs/sdlc/02_analysis/05_data_dictionary.md` — Data Dictionary (acuan definisi kolom, tipe data, dan constraint yang harus konsisten dengan DDL di dokumen target).
- [ ] **[BACA]** `docs/sdlc/02_analysis/03_use_case_diagram.md` — Use Case Diagram (acuan daftar use case yang harus tercakup di Matriks Ketertelusuran dokumen target).

---

## 4. Checklist Validasi dan Audit (Eksekusi Berurutan)

Lakukan setiap pemeriksaan di bawah ini secara berurutan. Setiap temuan **harus dicatat** beserta nomor bagian atau baris yang bermasalah dan solusi perbaikannya sebelum dilanjutkan ke langkah berikutnya. Jangan melompat ke Tahap G sebelum Tahap A sampai F selesai seluruhnya.

---

### TAHAP A — Validasi Kelengkapan Data terhadap File Referensi

> **Tujuan**: Memastikan dokumen target sudah merangkum **semua** data dan informasi kritis dari file referensi yang relevan dengan lingkup BOM & HPP. Tidak ada detail penting yang terlewat.

- [ ] **[A-01]** Bandingkan seluruh DDL tabel `bom_komposisi` di Bagian 3.2 dokumen target dengan DDL aktual di `01_database_schema.sql`. Periksa setiap kolom: nama kolom, tipe data, constraint (`NOT NULL`, `DEFAULT`, `UNIQUE`, `FOREIGN KEY`, `ON DELETE`, `ON UPDATE`), dan isi `COMMENT` setiap kolom. Catat setiap perbedaan sekecil apapun.

- [ ] **[A-02]** Bandingkan DDL tabel `barang` di Bagian 3.3 dokumen target dengan DDL aktual di `01_database_schema.sql`. Pastikan seluruh kolom yang berdampak pada kalkulasi HPP tercantum dengan tipe data yang akurat: `harga_beli DECIMAL(15,4)`, `harga_grosir DECIMAL(15,4)`, `harga_mitra DECIMAL(15,4)`, `min_grosir DECIMAL(15,4)`, `stok_saat_ini DECIMAL(15,4)`, `tipe_barang VARCHAR(20)`. Periksa juga semua `CHECK CONSTRAINT` pada tabel `barang`.

- [ ] **[A-03]** Periksa apakah tabel-tabel pendukung yang direferensikan dalam diagram ERD di Bagian 3.1 (`detail_transaksi`, `limbah_produksi`, `pengeluaran`, `audit_logs`, `riwayat_harga_supplier`, `stock_opname`) sudah memiliki kolom-kolom yang relevan terhadap BOM & HPP sesuai DDL aktual di `01_database_schema.sql`. Khususnya periksa:
  - Kolom `subtotal` dan `harga_jual` pada `detail_transaksi`: tipe data dan constraint.
  - Kolom `tipe_pengeluaran`, `disetujui_pemilik`, `nominal` pada `pengeluaran`: tipe data dan nilai valid enum-nya.
  - Kolom `action_type`, `old_value`, `new_value`, `target_table` pada `audit_logs`: tipe data (apakah `old_value` dan `new_value` bertipe JSON atau TEXT).
  - Kolom `harga_beli`, `tanggal_efektif` pada `riwayat_harga_supplier`: tipe data dan relasinya.
  - Kolom `kuantitas_limbah`, `kerugian_nominal`, `alasan_kerusakan` pada `limbah_produksi`: tipe data.

- [ ] **[A-04]** Verifikasi setiap kode SRS yang disebutkan di dokumen target (`SRS-F-005`, `SRS-F-007`, `SRS-F-008`, `SRS-F-009`, `SRS-F-010`) ada di `02_software_requirements.md` dan deskripsinya selaras dengan apa yang dijelaskan di dokumen target. Periksa juga apakah ada kode SRS lain yang relevan dengan BOM & HPP namun tidak direferensikan di dokumen target — jika ada, catat untuk ditambahkan.

- [ ] **[A-05]** Verifikasi seluruh kode workflow (`WF-M2-01`, `WF-M2-02`, `WF-M2-03`, `WF-M2-04`) yang tercantum di Matriks Ketertelusuran (Bagian 9) ada di `04_workflow_diagram.md`. Periksa nama workflow, aktor yang terlibat, trigger pemicu, dan urutan langkah prosesnya sudah selaras.

- [ ] **[A-06]** Verifikasi apakah kode menu CLI (`MENU-M2-001`, `MENU-M2-002`, `MENU-M2-003`, `MENU-M2-004`, `MENU-M1-005`) yang tercantum di Bagian 9 ada dan konsisten namanya dengan `04_cli_interaction_flow.md`. Pastikan hierarki navigasi menu dan hak akses per role (pemilik / kepala / kasir / staf produksi) untuk setiap menu tersebut selaras.

- [ ] **[A-07]** Periksa apakah pseudocode Pure Functions di Bagian 8.3 sudah mencakup semua use case fungsional yang disebutkan di SRS dan workflow diagram. Bandingkan signature fungsi (`hitung_biaya_komponen`, `hitung_hpp_produk`, `daftar_bom_baru`, `proses_pemotongan_stok`, `proses_limbah_produksi`, `sinkronisasi_atk_internal`) dan parameternya dengan kebutuhan aktual di file referensi. Catat jika ada fungsi yang hilang atau parameternya tidak lengkap.

- [ ] **[A-08]** Periksa apakah kolom `pengguna_id` yang di-hardcode sebagai nilai `1` pada INSERT audit log di pseudocode `daftar_bom_baru` (Bagian 8.3) sudah konsisten dengan mekanisme pengelolaan sesi `State Dictionary Passing` yang didefinisikan di `03_system_architecture.md`. Nilai `pengguna_id` seharusnya diambil dari state dictionary pengguna yang sedang login, bukan hardcode. Jika tidak konsisten, catat perbaikannya.

- [ ] **[A-09]** Periksa apakah penjelasan di Bagian 3.7 tentang penggunaan `riwayat_harga_supplier` untuk menarik data HPP historis sudah cukup teknis dan spesifik. Seharusnya dijelaskan: query JOIN apa yang digunakan, kolom apa yang dijoin, dan bagaimana filter periode waktu diterapkan. Jika kurang, catat penambahan yang diperlukan.

- [ ] **[A-10]** Periksa apakah diagram ERD di Bagian 3.1 sudah mencakup entitas `supplier` dan relasinya ke `riwayat_harga_supplier`, serta entitas `pengguna` dan relasinya ke `audit_logs` dan `pengeluaran`. Bandingkan entitas yang ada di ERD dokumen target dengan entitas di `02_erd_database.md`. Catat jika ada entitas relevan yang terlewat.

---

### TAHAP B — Validasi Relevansi dan Fokus Dokumen

> **Tujuan**: Memastikan dokumen target **hanya** memuat data dan informasi yang relevan dan dibutuhkan spesifik untuk modul BOM & HPP. Tidak ada konten yang masuk tetapi seharusnya menjadi domain dokumen lain.

- [ ] **[B-01]** Periksa apakah Bagian 3.1 (Diagram ERD) hanya menampilkan entitas dan relasi yang benar-benar berpartisipasi aktif dalam proses BOM & HPP, pencatatan limbah, pemotongan stok, dan sinkronisasi ATK. Jika ada entitas yang diikutsertakan tetapi tidak memiliki peran langsung (misalnya tabel murni domain modul lain yang tidak bersentuhan dengan kalkulasi biaya), catat untuk dihapus atau disesuaikan.

- [ ] **[B-02]** Periksa apakah penjelasan kolom `harga_retail`, `harga_grosir`, dan `harga_mitra` di Bagian 3.3 tetap dalam lingkup BOM & HPP, yaitu konteksnya adalah: mengapa kolom tersebut ada di tabel `barang` dan bagaimana relevansinya dengan kalkulasi margin keuntungan (SRS-F-005). Pastikan tidak melampaui ke penjelasan kebijakan harga yang merupakan domain dokumen modul Transaksi.

- [ ] **[B-03]** Periksa apakah Bagian 7 (Integrasi Lintas Modul) hanya mendeskripsikan titik integrasi yang bersifat **ketergantungan langsung** terhadap modul BOM & HPP (data yang dikirim ke modul ini atau data yang dihasilkan oleh modul ini). Pastikan tidak menjelaskan logika internal modul lain secara redundan dengan dokumen desain modul masing-masing.

- [ ] **[B-04]** Periksa apakah Bagian 6.2 (Tabel Kode Error) hanya mencantumkan kode error yang secara spesifik dipicu oleh logika modul BOM & HPP (validasi kuantitas BOM, validasi ID bahan baku, deteksi stok minus, kegagalan koneksi DB saat kalkulasi HPP). Jika ada kode error generik yang seharusnya didefinisikan di dokumen arsitektur sistem, catat untuk dihapus dari dokumen ini dan direferensikan saja ke dokumen yang tepat.

- [ ] **[B-05]** Periksa apakah Bagian 8.3 (Pseudocode) tidak memuat implementasi detail presentation layer CLI: logika input/output terminal, pewarnaan teks Rich library (`[yellow]`, `[green]`), navigasi menu, atau routing antarmuka. Pseudocode di dokumen design harus murni logika bisnis domain `logic/bom_hpp.py`. Catat setiap baris yang melanggar prinsip ini.

---

### TAHAP C — Validasi Standar Struktur Dokumen

> **Tujuan**: Memastikan dokumen target memiliki struktur yang lengkap, informatif, dan sesuai standar dokumen desain teknis industri manufaktur nyata.

- [ ] **[C-01]** Periksa frontmatter YAML (baris 1–10 dokumen) sudah lengkap dengan semua field standar: `id`, `judul`, `proyek`, `target`, `prioritas`, `status`, `versi`, `dibuat`, `penyusun`. Jika ada field yang hilang atau nilainya masih placeholder/kosong, catat.

- [ ] **[C-02]** Periksa apakah tabel Riwayat Perubahan Dokumen memiliki kolom lengkap: `Versi`, `Tanggal`, `Perubahan`, `Oleh`. Pastikan semua entri yang ada (`v1.0`, `v1.1`) sudah terisi dengan deskripsi perubahan yang informatif dan bukan placeholder kosong atau singkatan yang tidak jelas.

- [ ] **[C-03]** Periksa apakah setiap bagian utama (Bagian 1 s/d Bagian 10) memiliki: heading yang deskriptif, dan setidaknya satu paragraf pengantar yang menjelaskan tujuan bagian tersebut sebelum masuk ke tabel, daftar, atau diagram. Bagian yang langsung diawali tabel atau kode tanpa pengantar narasi harus diperbaiki.

- [ ] **[C-04]** Periksa sintaks dan kelengkapan label semua diagram Mermaid di dokumen (ERD Bagian 3.1, Flowchart Bagian 5.1, Sequence Diagram Bagian 5.3, Integration Diagram Bagian 7). Pastikan: tidak ada node tanpa label, tidak ada relasi tanpa keterangan, dan semua aktor/entitas yang disebutkan di narasi dokumen tercermin di diagram.

- [ ] **[C-05]** Periksa Bagian 10 (Glosarium): semua istilah teknis yang digunakan di seluruh dokumen harus terdaftar. Buat daftar istilah yang muncul di Bagian 2 s/d 9 yang belum ada di Bagian 1.6 maupun Bagian 10. Setiap istilah yang absen harus ditambahkan dengan definisi yang tepat dan tidak ambigu.

- [ ] **[C-06]** Periksa apakah dokumen memiliki bagian **Asumsi dan Keterbatasan** (Assumptions & Constraints). Bagian ini harus mendokumentasikan asumsi teknis yang digunakan saat merancang modul, minimal mencakup:
  - Satu barang induk hanya memiliki satu versi BOM aktif per cabang pada satu waktu.
  - Harga beli (`harga_beli`) di tabel `barang` selalu tersedia dan bernilai > 0 sebelum kalkulasi HPP dijalankan.
  - Trigger kalkulasi HPP hanya dipicu dari perubahan status antrian kerja menjadi `'Selesai'`, bukan dari kasir saat input transaksi.
  - Koneksi database yang diterima fungsi sudah aktif dan telah diautentikasi (bukan tanggung jawab fungsi BOM/HPP untuk membuka koneksi baru).
  
  Jika bagian ini belum ada, catat sebagai temuan dan siapkan kontennya untuk ditambahkan.

- [ ] **[C-07]** Periksa apakah dokumen memiliki bagian **Referensi File** (atau nama setara) di bagian paling akhir dokumen yang mencantumkan semua file referensi yang benar-benar dirujuk dalam isi dokumen. Pastikan formatnya konsisten (path relatif dari root proyek) dan semua file yang dirujuk di Bagian 1.4 dan di tempat lain dalam dokumen tercantum di sini.

---

### TAHAP D — Validasi Kualitas sebagai Referensi Fase SDLC Selanjutnya

> **Tujuan**: Memastikan dokumen ini cukup layak dan detail sebagai input utama bagi Fase 04 (Implementation) dan Fase 05 (Testing) tanpa menimbulkan pertanyaan yang menghambat pekerjaan.

- [ ] **[D-01]** Verifikasi apakah nama dan path file modul implementasi `logic/bom_hpp.py` yang disebutkan di Bagian 8.1 sudah konsisten dengan struktur direktori proyek yang didefinisikan di `03_system_architecture.md`. Pastikan path-nya akurat dan bukan asumsi saja.

- [ ] **[D-02]** Periksa setiap docstring fungsi di pseudocode Bagian 8.3. Setiap docstring harus memuat setidaknya: (1) tujuan singkat fungsi, (2) setiap parameter input beserta tipe data dan aturan validasinya, (3) nilai kembalian (return type dan makna setiap field `namedtuple`), (4) kode error yang dapat dipicu. Jika docstring belum memuat keempat elemen ini, catat baris mana yang harus diperbarui.

- [ ] **[D-03]** Periksa apakah setiap alur prosedural (Bagian 5.2 s/d 5.6) sudah cukup detail untuk diimplementasikan langsung oleh junior developer. Setiap alur minimal harus memuat: aktor dan role-nya, prakondisi yang harus terpenuhi, langkah-langkah berurutan yang bernomor, query SQL yang dieksekusi (dengan parameter), kondisi error dan penanganannya (kode error), dan output atau hasil akhir yang diharapkan.

- [ ] **[D-04]** Periksa apakah ada **skenario uji minimum** (happy path dan error path) yang disertakan atau setidaknya disebutkan sebagai catatan untuk Tim QA di dokumen ini. Dokumen desain tingkat industri biasanya menyertakan contoh skenario pengujian minimal untuk setiap alur utama agar tim QA memiliki patokan awal. Jika belum ada, catat sebagai kekurangan dan siapkan minimal 2 skenario uji per alur (satu happy path, satu error path) untuk ditambahkan.

- [ ] **[D-05]** Verifikasi bahwa formula matematis di Bagian 4 (terutama 4.1, 4.2, dan 4.6) ditulis dalam notasi yang tidak ambigu, disertai keterangan variabel yang lengkap di bawah setiap formula, dan dapat dipahami oleh junior programmer tanpa latar belakang akuntansi biaya.

- [ ] **[D-06]** Periksa apakah Matriks Ketertelusuran (Bagian 9) mencakup **semua** use case yang relevan dengan modul BOM & HPP. Buka `03_use_case_diagram.md` dari folder `02_analysis` dan bandingkan daftar use case terkait BOM, HPP, Limbah, ATK Sinkronisasi, dan Margin. Catat use case yang ada di use case diagram tetapi belum muncul di Bagian 9 dokumen target.

- [ ] **[D-07]** Periksa apakah strategi persistensi HPP yang dijelaskan di Bagian 3.7 sudah cukup detail dan tidak ambigu bagi developer implementasi maupun developer laporan keuangan (M.6). Pastikan: dijelaskan kapan tepatnya `harga_beli` barang induk diupdate, apa yang terjadi jika `harga_beli` bahan baku berubah setelah transaksi selesai, dan bagaimana laporan M.6 mengambil nilai HPP historis.

---

### TAHAP E — Validasi Kualitas Bahasa Indonesia

> **Tujuan**: Memastikan seluruh teks dokumen menggunakan Bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau AI model lain yang lebih murah.

- [ ] **[E-01]** Baca ulang seluruh teks naratif (di luar blok kode SQL, pseudocode Python, dan diagram Mermaid) dari Bagian 1 hingga Bagian 10. Identifikasi dan catat nomor baris setiap kalimat yang:
  - Menggunakan istilah teknis bahasa Inggris tanpa padanan atau penjelasan Bahasa Indonesia yang cukup di konteks tersebut.
  - Terlalu panjang dan beranak-cucu sehingga maknanya menjadi ambigu.
  - Menggunakan kata ganti yang tidak jelas rujukannya (misalnya: "hal ini", "nilai tersebut", "proses ini" tanpa anteseden yang jelas di kalimat sebelumnya).
  - Menggunakan kalimat pasif berlebihan yang membingungkan siapa pelakunya.

- [ ] **[E-02]** Periksa apakah setiap istilah domain teknis (BOM, HPP, UoM, COGS, FP, ACID, InnoDB, OPEX, SSoT, dan lainnya) sudah diperkenalkan dengan definisi singkat saat pertama kali muncul di dokumen, atau setidaknya tercantum di Bagian 1.6 (Definisi, Akronim, Singkatan) dan Bagian 10 (Glosarium). Tidak boleh ada istilah yang "muncul begitu saja" tanpa ada definisinya di salah satu dari dua bagian tersebut.

- [ ] **[E-03]** Periksa konsistensi penulisan istilah teknis di seluruh dokumen:
  - Nama tabel database harus selalu ditulis dalam format backtick: `bom_komposisi`, `barang`, `detail_transaksi`.
  - Nama kolom database harus selalu ditulis dalam format backtick: `harga_beli`, `stok_saat_ini`, `tipe_barang`.
  - Nama konsep bisnis (bukan kode) ditulis dalam teks biasa dengan huruf kapital: *Formula BOM*, *Harga Pokok Penjualan*, *Limbah Produksi*.
  - Nilai enum database ditulis dalam format backtick dan tanda kutip: `'Bahan_Baku'`, `'Retail_ATK'`, `'Selesai'`.
  - Catat setiap inkonsistensi beserta nomor barisnya.

- [ ] **[E-04]** Periksa apakah heading setiap bagian dan sub-bagian (Bagian 1 s/d 10 dan seluruh sub-bagiannya) menggunakan bahasa yang jelas, deskriptif, dan spesifik terhadap isi bagian tersebut. Hindari heading yang terlalu generik yang tidak memberi informasi tentang isi.

---

### TAHAP F — Validasi Kelayakan Produksi dan Pengisian Data Kosong

> **Tujuan**: Memastikan tidak ada data kosong, placeholder, atau informasi yang hilang yang dapat menghambat fase kerja selanjutnya. Jika ditemukan, isi langsung dengan data yang sesuai.

- [ ] **[F-01]** Cari di seluruh dokumen teks yang mengandung placeholder seperti: `[TBD]`, `[TODO]`, `[FILL]`, `N/A`, `...`, `(isi kemudian)`, atau sel tabel yang kosong tanpa penjelasan mengapa kosong. Jika ditemukan, isi langsung dengan data yang sesuai, relevan, dan masih dalam ruang lingkup dokumen ini. Jangan biarkan satu placeholder pun tersisa.

- [ ] **[F-02]** Periksa tabel Aturan Validasi Input CLI (Bagian 6.1): pastikan tidak ada field input dari alur prosedural (Bagian 5.2 s/d 5.6) yang terlewat. Buat daftar semua input yang diterima dari user di setiap alur (Pendaftaran BOM, Kalkulasi HPP, Pemotongan Stok, Pencatatan Limbah, Sinkronisasi ATK) lalu bandingkan dengan baris di tabel Bagian 6.1. Tambahkan baris yang belum ada.

- [ ] **[F-03]** Periksa tabel Kode Error (Bagian 6.2): setiap kondisi error yang disebutkan di alur prosedural (Bagian 5) dan pseudocode (Bagian 8.3) harus memiliki kode error formal yang terdaftar di tabel ini. Identifikasi semua string error (`ERR-VAL-007`, `ERR-VAL-008`, `ERR-STOCK-010`, `ERR-DB-007`) dan pastikan semua sudah terdaftar dengan pesan visual terminal yang tepat. Tambahkan baris baru jika ada kondisi error yang belum punya kode formal.

- [ ] **[F-04]** Verifikasi aritmatika contoh kalkulasi numerik di Bagian 4.3 (Stempel Flash) dan Bagian 4.4 (Buku Yasin Hardcover): hitung ulang secara manual setiap `kuantitas_desimal × harga_beli_satuan` untuk setiap komponen, lalu jumlahkan hasilnya dan bandingkan dengan HPP Total yang tertulis di dokumen. Jika ada kesalahan hitung, perbaiki. Pastikan semua nilai menggunakan presisi 4 digit desimal.

- [ ] **[F-05]** Periksa apakah Bagian 1.3 (Posisi Dokumen dalam SDLC) dan diagram ASCII-art flowchart-nya sudah akurat merepresentasikan posisi dokumen ini relatif terhadap dokumen-dokumen lain yang benar-benar ada di folder `docs/sdlc/`. Pastikan nama fase, nomor dokumen, dan urutan sudah konsisten dengan struktur direktori aktual proyek.

- [ ] **[F-06]** Periksa apakah ada instruksi atau penjelasan tentang cara **menghapus atau menonaktifkan formula BOM** (misalnya ketika produk kustom sudah tidak dijual lagi). Mekanisme `ON DELETE CASCADE` pada `barang_induk_id` di `bom_komposisi` memiliki implikasi operasional yang penting — jika baris `barang` dihapus, seluruh formula BOM-nya ikut terhapus. Jika ini belum dijelaskan di dokumen, catat sebagai kekurangan dan tambahkan penjelasan singkat tentang implikasi ini di Bagian yang paling relevan (misal Bagian 3.5 atau Bagian 5).

- [ ] **[F-07]** Periksa apakah ada penjelasan tentang alur **update formula BOM** (mengubah kuantitas komponen yang sudah ada di `bom_komposisi`). Karena ada `UNIQUE CONSTRAINT` pada kombinasi (`barang_induk_id`, `bahan_baku_id`), operasi ini harus menggunakan `UPDATE` (bukan `INSERT` yang akan melanggar constraint). Jika alur ini belum didokumentasikan, catat sebagai kekurangan dan tambahkan penjelasannya.

- [ ] **[F-08]** Periksa apakah ada penjelasan yang cukup mengenai **dampak perubahan `harga_beli` bahan baku terhadap HPP historis**: jika harga beli bahan baku naik setelah transaksi selesai, apakah HPP transaksi lama berubah atau tetap? Ini adalah pertanyaan fundamental yang sering menimbulkan kebingungan saat implementasi. Pastikan ada klarifikasi yang gamblang di dokumen, khususnya mengaitkannya dengan peran tabel `riwayat_harga_supplier` dalam menyimpan harga historis.

- [ ] **[F-09]** Periksa apakah ada penjelasan mengenai **perilaku sistem saat `bom_komposisi` kosong** (barang induk belum punya formula BOM yang terdaftar) ketika sistem mencoba menghitung HPP. Apakah sistem mengembalikan HPP = 0, melempar error, atau memblokir status antrian menjadi `'Selesai'`? Jika perilaku ini belum terdokumentasi, catat dan tambahkan klausul penanganannya.

---

### TAHAP G — Penulisan Ulang Dokumen (Overwrite)

> **Tujuan**: Menuangkan seluruh hasil validasi dan perbaikan ke dalam dokumen target dengan cara menimpa (overwrite) file asli. Tidak ada satu baris pun yang boleh dipotong, diringkas, atau dihilangkan.

- [ ] **[G-01]** Setelah seluruh temuan dari Tahap A hingga F dicatat dan solusi perbaikannya dirumuskan, buat **draft revisi lengkap** dari seluruh dokumen terlebih dahulu dalam memori kerja sebelum menulis ke file. Pastikan semua perbaikan sudah terintegrasi ke dalam draft ini.

- [ ] **[G-02]** Terapkan seluruh kategori perbaikan berikut pada draft revisi:
  - Koreksi semua deviasi DDL antara dokumen dan `01_database_schema.sql` (Tahap A).
  - Hapus atau sesuaikan konten yang di luar lingkup BOM & HPP (Tahap B).
  - Tambahkan bagian yang kurang: Asumsi & Keterbatasan, Referensi File, skenario uji minimum (Tahap C dan D).
  - Perkuat detail alur prosedural dan docstring pseudocode (Tahap D).
  - Perbaiki seluruh kalimat bermasalah dan inkonsistensi terminologi (Tahap E).
  - Isi semua placeholder dan tambahkan penjelasan yang masih kurang (Tahap F).

- [ ] **[G-03]** Perbarui **versi dokumen** di frontmatter YAML: ubah nilai `versi` dari `v1.1` menjadi `v1.2`.

- [ ] **[G-04]** Tambahkan baris baru di bagian atas tabel **Riwayat Perubahan Dokumen** dengan data berikut:
  - Versi: `1.2`
  - Tanggal: tanggal pelaksanaan hari ini dalam format `YYYY-MM-DD`
  - Perubahan: ringkasan singkat dan padat (maks. 3 kalimat) dari seluruh perbaikan yang dilakukan
  - Oleh: `Principal Manufacturing Systems Architect & Certified Cost Accounting Specialist`

- [ ] **[G-05]** Tulis ulang seluruh isi dokumen yang telah direvisi ke file `docs/sdlc/03_design/05_bom_hpp_design.md` menggunakan operasi **overwrite penuh** (timpa seluruh isi file dari baris pertama hingga terakhir). Aturan mutlak yang wajib dipatuhi:
  - **DILARANG KERAS** memotong, meringkas, atau menghilangkan bagian apapun dari dokumen asli.
  - **DILARANG KERAS** menggunakan placeholder seperti `[... bagian ini dipertahankan ...]`, `[lihat versi sebelumnya]`, atau sejenisnya sebagai pengganti teks asli.
  - Seluruh teks dari baris pertama (`---` frontmatter) hingga baris terakhir dokumen (termasuk Glosarium, Referensi Tambahan, dan semua bagian baru yang ditambahkan) **HARUS** ditulis ulang sepenuhnya dan lengkap.
  - Seluruh blok kode SQL, pseudocode Python, diagram Mermaid, tabel Markdown, dan diagram ASCII-art **HARUS** ditulis ulang secara verbatim (kata per kata, karakter per karakter) dengan perbaikan yang diperlukan saja — tidak boleh ada yang dipersingkat.
  - Jumlah baris dokumen hasil revisi harus **lebih besar atau sama dengan** jumlah baris dokumen asli (755 baris), karena operasi ini bersifat penambahan dan penyempurnaan, bukan pemangkasan.

- [ ] **[G-06]** Setelah operasi write berhasil, **segera baca kembali file** yang sudah ditulis untuk memverifikasi integritasnya. Periksa poin-poin berikut satu per satu:
  - Nilai `versi` di frontmatter sudah berubah menjadi `v1.2`.
  - Baris pertama dokumen adalah `---` (awal frontmatter YAML) dan terbaca dengan benar.
  - Baris terakhir dokumen tidak terpotong di tengah kalimat atau di tengah blok kode.
  - Semua heading Bagian 1 s/d Bagian 10 beserta seluruh sub-bagiannya masih ada.
  - Tabel Riwayat Perubahan memuat baris versi `1.2`.
  - Tidak ada blok kode SQL, pseudocode Python, atau diagram Mermaid yang terpotong di tengah.
  - Bagian baru yang ditambahkan (Asumsi & Keterbatasan, Referensi File, Referensi Tambahan) sudah ada.

---

### TAHAP H — Pembaruan Referensi File

> **Tujuan**: Memastikan semua file referensi yang digunakan selama proses perbaikan tercantum di bagian referensi dokumen target.

- [ ] **[H-01]** Buat daftar semua file referensi **tambahan** yang digunakan atau dirujuk selama proses validasi dan perbaikan di Tahap A–F, yaitu file-file yang tidak tercantum di Bagian 1.4 dokumen asli (misalnya `03_use_case_diagram.md`, `05_data_dictionary.md`, atau `06_access_control_matrix.md` jika digunakan).

- [ ] **[H-02]** Jika ada file referensi tambahan, tambahkan ke dalam bagian **Referensi Tambahan** di **baris paling bawah** dokumen target (setelah Bagian 10 atau bagian terakhir yang sudah ada). Gunakan format berikut:

  ```markdown
  ---

  ## Referensi Tambahan

  *File-file berikut digunakan sebagai acuan tambahan dalam proses validasi dan revisi dokumen ini (v1.2):*

  - [Nama File](path/relatif/dari/root/proyek) — Penjelasan singkat mengapa file ini dirujuk.
  ```

- [ ] **[H-03]** Jika tidak ada file referensi tambahan (semua sudah tercantum di Bagian 1.4), lewati langkah H-02 dan catat secara eksplisit di log kerja Anda: `KONFIRMASI: Tidak ada referensi tambahan di luar Bagian 1.4.`

---

## 5. Aturan Pelaksanaan Umum

Berikut adalah aturan umum yang **HARUS** dipatuhi selama seluruh proses pelaksanaan issue ini:

1. **Urutan Eksekusi Wajib**: Lakukan tahap A → B → C → D → E → F → G → H secara berurutan tanpa melompati tahap. Jika sebuah tahap menghasilkan temuan, temuan tersebut harus dimasukkan ke draft revisi sebelum melanjutkan ke tahap berikutnya.

2. **Tidak Ada Modifikasi Parsial**: Jangan menulis perubahan apapun ke file target sebelum seluruh Tahap A–F selesai sepenuhnya dan draft revisi lengkap sudah siap (G-01 dan G-02 selesai).

3. **Satu Operasi Write Tunggal**: File target hanya boleh ditulis **satu kali** yaitu di Tahap G-05 menggunakan operasi overwrite penuh. Dilarang melakukan partial edit, append bertahap, atau beberapa kali operasi write.

4. **Verifikasi Pasca-Write Wajib**: Selalu lakukan pembacaan ulang file setelah write (Tahap G-06) untuk memastikan integritas konten sebelum menyatakan pekerjaan selesai.

5. **Tidak Ada Halusinasi Data**: Semua data yang ditambahkan ke dokumen (nilai kolom DDL, kode SRS, kode error, contoh nilai numerik, nama menu CLI) **HARUS** bersumber dari file referensi yang dibaca di Tahap 3 atau dari analisis logis yang dapat dibuktikan dari isi file referensi tersebut. Dilarang keras mengarang data yang tidak dapat diverifikasi.

6. **Presisi Desimal Wajib**: Semua nilai numerik dalam contoh kalkulasi dan DDL harus menggunakan presisi `DECIMAL(15,4)` — yaitu 4 digit di belakang koma — tanpa pengecualian. Contoh: `Rp 4.750,0000` bukan `Rp 4.750`.

7. **Konsistensi Terminologi dengan SSoT**: Gunakan terminologi yang identik dengan yang digunakan di file referensi SSoT (`01_database_schema.sql`, `02_software_requirements.md`). Jika ada perbedaan terminologi antara dua file referensi, ikuti yang ada di `01_database_schema.sql` untuk hal-hal yang menyangkut nama tabel dan kolom database.

---

## 6. Definisi Selesai (Definition of Done)

Issue ini dianggap **selesai** apabila seluruh kondisi berikut terpenuhi tanpa pengecualian:

- [ ] Semua checklist di Tahap A, B, C, D, E, F, G, dan H sudah ditandai `[x]` (selesai).
- [ ] File `docs/sdlc/03_design/05_bom_hpp_design.md` sudah diperbarui dengan nilai versi `v1.2` di frontmatter.
- [ ] Tabel Riwayat Perubahan Dokumen sudah memuat baris baru untuk versi `v1.2`.
- [ ] Tidak ada placeholder, data kosong, atau informasi ambigu yang tersisa di seluruh dokumen.
- [ ] Seluruh DDL di dokumen (tabel `bom_komposisi`, `barang`, dan tabel pendukung yang disebutkan) 100% sinkron dengan `01_database_schema.sql`.
- [ ] Seluruh kode SRS yang direferensikan sudah terverifikasi ada di `02_software_requirements.md`.
- [ ] Dokumen memiliki bagian Asumsi & Keterbatasan yang lengkap.
- [ ] Dokumen memiliki bagian Referensi File yang mencantumkan semua file yang dirujuk.
- [ ] Bahasa Indonesia di seluruh narasi dokumen natural, tidak ambigu, dan mudah dipahami oleh junior developer tanpa latar belakang akuntansi.
- [ ] Jumlah baris dokumen revisi lebih besar atau sama dengan 755 baris (jumlah baris dokumen asli).
- [ ] Reviewer (pemilik issue / senior engineer) dapat membaca dokumen dari awal hingga akhir tanpa harus membuka file referensi lain untuk memahami konteks modul BOM & HPP secara keseluruhan.

---

*Issue ini dibuat pada 2026-05-29 oleh AI Coding Agent (Antigravity) atas permintaan pemilik proyek AbuCom.*
