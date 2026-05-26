---
judul     : Validasi, Analisis, dan Penyempurnaan Dokumen Test Plan
dokumen   : Test Plan
target    : docs/sdlc/05_testing/01_test_plan.md
referensi : docs/sdlc/
tanggal   : 2026-05-26
status    : Open
prioritas : High
---

# Validasi, Analisis, dan Penyempurnaan Dokumen Test Plan

## Latar Belakang

Dokumen **Test Plan** (`docs/sdlc/05_testing/01_test_plan.md`) adalah deliverable pertama dan paling kritis pada **Fase 05 — Testing** dalam SDLC AbuCom. Dokumen ini berfungsi sebagai **cetak biru pengujian formal** yang akan menjadi acuan langsung dalam pembuatan Test Cases, Test Scripts, dan Test Report pada fase berikutnya.

Karena perannya sebagai **input utama fase selanjutnya**, kualitas dokumen ini harus dijamin secara ketat: lengkap, tidak ambigu, bebas data kosong, dan memenuhi standar dokumen praktik industri yang sesungguhnya. Setiap kekurangan pada dokumen ini **akan langsung menghambat dan mempermasalahkan proses kerja fase berikutnya**.

Issue ini menginstruksikan dilakukannya validasi menyeluruh, penyempurnaan, dan penulisan ulang penuh dokumen Test Plan ke versi yang telah direvisi (v1.1).

---

## Persona Pelaksana

Sebelum memulai pekerjaan apa pun, adopsi dan pertahankan persona berikut ini secara konsisten dari awal hingga akhir implementasi issue ini:

> **Anda adalah: Senior QA Architect & SDLC Documentation Specialist**
>
> Seorang pakar pengujian perangkat lunak berpengalaman 10+ tahun yang telah menyusun Test Plan untuk sistem keuangan skala UMKM hingga enterprise. Anda memiliki keahlian mendalam dalam: IEEE 829 (standar dokumentasi pengujian), strategi pengujian berbasis risiko, traceability matrix SRS-ke-TestCase, keamanan aplikasi CLI berbasis Python/MySQL, dan standar dokumentasi teknis formal Bahasa Indonesia. Anda bersikap **kritis, teliti, dan zero-tolerance terhadap ambiguitas, data kosong, atau inkonsistensi** dalam dokumen teknis yang akan digunakan sebagai referensi operasional.

---

## Tujuan Issue

1. Memastikan dokumen Test Plan telah merangkum **seluruh** data dan informasi relevan dari semua dokumen referensinya tanpa ada yang terlewat.
2. Memastikan dokumen Test Plan hanya berisi data yang **memang seharusnya ada** dalam dokumen Test Plan (tidak memuat konten yang seharusnya berada di dokumen lain).
3. Memastikan dokumen Test Plan memenuhi **standar struktur industri** yang lengkap dan informatif layaknya dokumen IEEE 829 / best-practice QA profesional.
4. Memastikan dokumen Test Plan **layak sebagai input dan referensi utama** bagi fase SDLC selanjutnya (Test Cases, Test Scripts, Test Report).
5. Memastikan dokumen Test Plan menggunakan **Bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami** oleh junior programmer atau LLM AI model lain yang lebih kecil/murah.
6. Memastikan **tidak ada data kosong, placeholder, atau konten yang perlu diisi manual** yang masih tersisa tanpa konten substantif.
7. Menuangkan kembali seluruh hasil dokumen yang telah divalidasi dan disempurnakan ke **target file yang sama dengan cara overwrite penuh** (v1.1).

---

## Daftar Tugas Implementasi (Low-Level Checklist)

Ikuti setiap langkah di bawah ini secara **berurutan dari atas ke bawah**. Jangan melompati langkah. Centang `[x]` setiap tugas setelah selesai dikerjakan.

---

### FASE 1: PERSIAPAN & PEMBACAAN DOKUMEN

- [ ] **1.1.** Baca secara penuh dan seksama file target utama:
  - File: `docs/sdlc/05_testing/01_test_plan.md`
  - Baca dari baris pertama hingga baris terakhir tanpa melewati bagian mana pun.
  - Catat dalam memori: versi dokumen saat ini, struktur bab, jumlah referensi yang tertulis, dan seluruh ID SRS/UC/ERR yang disebutkan.

- [ ] **1.2.** Identifikasi dan catat daftar lengkap semua **dokumen referensi** yang disebutkan di dalam dokumen target (terutama pada Bab 1.4, Bab 1.7, dan Bab 15). Pastikan daftar ini mencakup setidaknya:
  - `R-01`: `docs/sdlc/02_analysis/02_software_requirements.md`
  - `R-02`: `docs/sdlc/02_analysis/03_use_case_diagram.md`
  - `R-03`: `docs/sdlc/02_analysis/06_access_control_matrix.md`
  - `R-04`: `docs/sdlc/03_design/06_security_design.md`
  - `R-05`: `docs/sdlc/03_design/03_system_architecture.md`
  - `R-06`: `docs/sdlc/03_design/01_database_schema.sql`
  - `R-07`: `docs/sdlc/03_design/02_erd_database.md`
  - `R-08`: `docs/sdlc/03_design/05_bom_hpp_design.md`
  - `R-09`: `docs/sdlc/03_design/04_cli_interaction_flow.md`
  - `R-10`: `docs/sdlc/04_implementation/01_coding_standard.md`
  - `R-11`: `docs/sdlc/04_implementation/02_environment_setup.md`
  - `R-12`: `docs/sdlc/04_implementation/03_module_structure.md`
  - `R-13`: `docs/sdlc/04_implementation/04_git_workflow.md`
  - `R-14`: `docs/sdlc/04_implementation/05_development_roadmap.md`
  - `R-15`: `docs/sdlc/02_analysis/01_business_requirements.md`
  - `R-16`: `docs/sdlc/01_planning/04_tech_stack_decision.md`
  - `R-17`: `docs/sdlc/02_analysis/04_workflow_diagram.md`
  - `R-18`: `docs/sdlc/02_analysis/05_data_dictionary.md`
  - `narasi.txt`: `docs/sdlc/narasi.txt`

- [ ] **1.3.** Baca satu per satu setiap file referensi yang **ada secara fisik** di dalam repositori. Untuk setiap file, lakukan:
  - Baca dari baris pertama hingga baris terakhir.
  - Catat: poin-poin data kunci, entitas, angka, istilah teknis, aturan bisnis, batasan sistem, ID (SRS-F, SRS-NF, UC, ERR, tabel DB, constraint) yang ada di dalamnya.
  - Tandai referensi mana yang **[TIDAK ADA SECARA FISIK]** di repositori (seperti R-14 Development Roadmap) — ini penting untuk langkah validasi berikutnya.

- [ ] **1.4.** Untuk referensi yang **tidak ada secara fisik** (contoh: R-14 Development Roadmap), catat dengan jelas bahwa data tersebut tidak dapat diverifikasi secara langsung dan tandai item terkait dalam dokumen untuk penanganan khusus.

---

### FASE 2: VALIDASI KRITERIA 1 — KELENGKAPAN PENYERAPAN DATA REFERENSI

> **Tujuan:** Memastikan tidak ada data penting dari referensi yang terlewat untuk masuk ke dokumen Test Plan.

- [ ] **2.1.** Bandingkan daftar **SRS Fungsional (SRS-F-XXX)** dari file R-01 (`02_software_requirements.md`) dengan **Bab 4 (Pemetaan Cakupan Pengujian per Modul)** dan **Bab 12.1 (Traceability Matrix SRS → Test Scope)** di dokumen target.
  - Periksa: Apakah **setiap** ID SRS-F yang ada di R-01 sudah memiliki skenario pengujian yang dipetakan?
  - Jika ada SRS-F yang belum dipetakan: **Tambahkan skenario uji** yang sesuai ke modul yang relevan dan tambahkan barisnya di Bab 12.1.

- [ ] **2.2.** Bandingkan daftar **SRS Non-Fungsional (SRS-NF-XXX)** dari file R-01 dengan **Bab 12.2** di dokumen target.
  - Periksa: Apakah semua SRS-NF sudah terpetakan ke skenario pengujian yang spesifik?
  - Jika ada yang belum terpetakan: **Tambahkan baris** ke Bab 12.2 dengan kriteria pengujian yang relevan.

- [ ] **2.3.** Bandingkan daftar **Use Case (UC-XXX)** dari file R-02 (`03_use_case_diagram.md`) dengan **Bab 12.3** di dokumen target.
  - Periksa: Apakah setiap UC sudah memiliki skenario uji terkait?
  - Jika ada UC yang belum terpetakan: **Tambahkan baris** yang sesuai ke Bab 12.3.

- [ ] **2.4.** Bandingkan **matriks otorisasi 8 peran** dari file R-03 (`06_access_control_matrix.md`) dengan **Bab 5.2 (Pengujian Otorisasi RBAC)** dan skenario uji M7-TC-002.
  - Periksa: Apakah seluruh 8 peran (pemilik, kepala_percetakan, kasir, desainer, operator_produksi, gudang, pramuniaga, teknisi) sudah tercakup dalam skenario uji RBAC?
  - Jika ada peran yang belum diuji: **Tambahkan skenario uji** yang spesifik untuk peran tersebut.

- [ ] **2.5.** Bandingkan spesifikasi keamanan dari file R-04 (`06_security_design.md`) — terutama: bcrypt, JWT, rate limiting, sanitasi CLI, audit logs JSON, SOP insiden, enkripsi Fernet CRM, AES-256 backup, UU PDP — dengan **Bab 5 (Pengujian Keamanan)** di dokumen target.
  - Periksa: Apakah setiap mekanisme keamanan yang terdefinisi di R-04 sudah memiliki skenario uji tersendiri?
  - Jika ada mekanisme keamanan yang terlewat: **Tambahkan sub-bab pengujian** yang sesuai di Bab 5.

- [ ] **2.6.** Bandingkan spesifikasi matematika presisi desimal dari file R-08 (`05_bom_hpp_design.md`) — terutama: `Decimal(15,4)`, `ROUND_HALF_UP`, `FOR UPDATE` InnoDB, formula BOM, limbah, sinkronisasi ATK — dengan **Bab 6 (Pengujian Presisi Desimal)** di dokumen target.
  - Periksa: Apakah setiap formula kritis dan boundary case desimal dari R-08 sudah tercakup dalam skenario uji Bab 6?
  - Jika ada formula atau edge case yang terlewat: **Tambahkan sub-skenario** yang sesuai.

- [ ] **2.7.** Bandingkan alur navigasi CLI, format ANSI, thermal print, dan kode error `ERR-XXX-YYY` dari file R-09 (`04_cli_interaction_flow.md`) dengan **Bab 8 (Pengujian Antarmuka CLI)** dan **Bab 12.4 (Kode Error Mapping)** di dokumen target.
  - Periksa: Apakah semua kode error penting dari R-09 sudah masuk ke Bab 12.4?
  - Jika ada kode error yang terlewat: **Tambahkan baris** ke Bab 12.4.

- [ ] **2.8.** Periksa file R-05 (`03_system_architecture.md`) untuk memastikan arsitektur LAN client-server (Mini PC server Debian + PC klien Windows), connection pooling, retry mechanism, dan firewall UFW sudah tercermin di **Bab 7 (Pengujian Integrasi & Konektivitas)** dan **Bab 10 (Lingkungan Pengujian)**.
  - Jika ada detail arsitektur yang terlewat: **Tambahkan informasi** yang relevan ke bab yang sesuai.

- [ ] **2.9.** Periksa file R-06 (`01_database_schema.sql`) dan R-07 (`02_erd_database.md`) untuk memastikan:
  - Tabel-tabel utama yang diuji (misal: `pengguna`, `transaksi`, `bahan_baku`, `audit_logs`, `kasbon`, `pelanggan`, `system_configs`, `cabang_id`) sudah disebut secara eksplisit di skenario uji yang relevan.
  - Constraint database (CHECK, FOREIGN KEY, UNIQUE, DEFAULT) sudah masuk ke skenario Database Integrity Testing.
  - Jika ada tabel atau constraint penting yang terlewat: **Tambahkan ke skenario uji** yang relevan.

- [ ] **2.10.** Periksa file R-15 (`01_business_requirements.md`) untuk memastikan semua kebutuhan bisnis level tinggi (multi-divisi toko, sistem offline LAN, keamanan kas, payroll UMKM) sudah tercermin di **Bab 1 (Informasi Dokumen)**, **Bab 2 (Cakupan Pengujian)**, dan **Bab 13 (Kriteria Penerimaan Pengguna)**.

- [ ] **2.11.** Periksa file R-16 (`04_tech_stack_decision.md`) untuk memastikan tech stack yang diputuskan (Python 3.14.2, MySQL 8.4 LTS, `mysql-connector-python`, `bcrypt`, `pyjwt`, `rich`, `tabulate`) sudah tercantum dengan versi yang akurat di **Bab 10.2 (Spesifikasi Software Pengujian)**.

- [ ] **2.12.** Periksa file R-17 (`04_workflow_diagram.md`) untuk memastikan alur kerja operasional bisnis harian (buka toko, shift kasir, transaksi, stock opname, tutup kas) sudah tercermin di **Bab 3.1.4 (UAT)** dan **Bab 13.2 (Kriteria Penerimaan Operasional)**.

- [ ] **2.13.** Periksa file R-18 (`05_data_dictionary.md`) untuk memastikan terminologi dan definisi field database penting (tipe data, constraint, enum values) sudah konsisten dengan yang digunakan di skenario-skenario pengujian dalam dokumen target.

- [ ] **2.14.** Periksa file `narasi.txt` (`docs/sdlc/narasi.txt`) untuk mengidentifikasi apakah ada konteks bisnis, fitur, atau aturan operasional khusus AbuCom yang **belum tercermin** di dokumen target tetapi seharusnya ada.

---

### FASE 3: VALIDASI KRITERIA 2 — RELEVANSI & FOKUS KONTEN

> **Tujuan:** Memastikan dokumen Test Plan HANYA berisi konten yang memang seharusnya ada dalam dokumen Test Plan, sesuai standar industri.

- [ ] **3.1.** Periksa setiap bab dan sub-bab dokumen. Identifikasi apakah ada konten yang **seharusnya tidak ada** di Test Plan tetapi ternyata ada (misalnya: detail implementasi kode, DDL database, desain UI/UX, spesifikasi arsitektur yang terlalu detail, konten yang seharusnya ada di Test Cases saja).
  - Jika ditemukan konten yang tidak relevan: **Hapus atau ringkas** konten tersebut, ganti dengan referensi ke dokumen yang seharusnya memuat konten itu.

- [ ] **3.2.** Periksa **Bab 5 (Pengujian Keamanan)**: Pastikan isinya adalah **rencana pengujian** (tujuan, skenario langkah demi langkah, expected result), bukan penjelasan cara kerja mekanisme keamanan itu sendiri. Jika ada bagian yang berubah menjadi dokumentasi teknis keamanan: **Ubah** ke format rencana pengujian yang tepat.

- [ ] **3.3.** Periksa **Bab 6 (Pengujian Presisi Desimal)**: Pastikan isinya adalah **skenario boundary testing** dengan nilai input konkret, kalkulasi yang diharapkan, dan expected database value. Jangan memuat penjelasan teori matematika yang panjang.

- [ ] **3.4.** Periksa **Bab 12 (Matriks Ketertelusuran)**: Pastikan setiap baris matriks memiliki kolom Status yang terisi dengan nilai yang konkret (`Cocok` / `Tidak Terpetakan` / `Perlu Ditambah`), bukan placeholder kosong.

- [ ] **3.5.** Periksa **Bab 14 (Lampiran)**: Pastikan template Test Case dan template Test Report yang ada sudah cukup representatif dan tidak membingungkan implementor. Jika ada field dalam template yang ambigu: **Perjelas** dengan contoh nilai atau keterangan.

---

### FASE 4: VALIDASI KRITERIA 3 — STANDAR STRUKTUR DOKUMEN INDUSTRI

> **Tujuan:** Memastikan struktur dokumen Test Plan memenuhi standar industri (best practice IEEE 829 / ISTQB).

- [ ] **4.1.** Periksa apakah dokumen memiliki bab-bab wajib berikut. Jika ada yang tidak ada atau kurang lengkap, **tambahkan**:
  - [ ] Informasi Dokumen (Tujuan, Cakupan, Posisi SDLC, Hubungan Dokumen, Audiens, Definisi/Akronim, Referensi)
  - [ ] Cakupan Pengujian (In-Scope, Out-of-Scope, Asumsi, Risiko & Mitigasi)
  - [ ] Strategi Pengujian (Test Levels, Test Types, Test Approach, Entry/Exit/Suspension/Resumption Criteria)
  - [ ] Pemetaan Cakupan per Modul (tabel ID Skenario, Deskripsi, SRS, UC, Tipe, Prioritas)
  - [ ] Pengujian Keamanan (Security Testing Plan)
  - [ ] Pengujian Presisi Desimal (Decimal Precision Testing)
  - [ ] Pengujian Integrasi & Konektivitas
  - [ ] Pengujian Antarmuka CLI
  - [ ] Pengujian Non-Fungsional
  - [ ] Lingkungan Pengujian (Hardware, Software, DB, Test Data, Config .env)
  - [ ] Manajemen Pengujian (Peran, Jadwal, Tools, Prosedur Defect, Metrik)
  - [ ] Matriks Ketertelusuran (SRS-F, SRS-NF, UC, Error Code)
  - [ ] Kriteria Penerimaan Pengguna (UAT Criteria, Sign-Off Checklist)
  - [ ] Lampiran (Glosarium, Template Test Case, Template Test Report)
  - [ ] Referensi Dokumen (tabel lengkap dengan kode ref, nama, path, versi)

- [ ] **4.2.** Periksa **Riwayat Perubahan Dokumen** di bagian paling atas. Pastikan tabel perubahan versi sudah ada dan terisi dengan benar.

- [ ] **4.3.** Periksa apakah ada **bab yang hilang** yang umum ada dalam dokumen Test Plan industri namun belum ada di dokumen ini:
  - [ ] **Bab "Pengujian Performa & Skalabilitas"** — pastikan ini sudah ada (bukan hanya masuk di non-fungsional saja, tetapi memiliki sub-bab khusus yang cukup detail).
  - [ ] **Bab "Manajemen Risiko Pengujian"** — apakah risiko pengujian (Bab 2.4) sudah cukup detail, atau perlu diperluas? Minimal harus ada 4 risiko teridentifikasi beserta strategi mitigasinya yang konkret.
  - [ ] **Bab "Kriteria Kualitas / Definition of Done"** — apakah ada definisi yang jelas kapan sebuah test case dianggap DONE? Jika belum ada, **tambahkan** sebagai sub-bab di Bab 11 atau Bab 13.

- [ ] **4.4.** Periksa apakah **header YAML frontmatter** di baris paling atas dokumen sudah lengkap dan akurat (dokumen, proyek, versi, tanggal, status, penyusun).

- [ ] **4.5.** Periksa apakah **diagram ASCII** yang ada (Bab 1.3 posisi SDLC, Bab 3.1 test levels, Bab 10 environment) masih akurat dan informatif. Jika ada yang perlu diperbarui atau diperbaiki, lakukan.

---

### FASE 5: VALIDASI KRITERIA 4 — KELAYAKAN SEBAGAI REFERENSI FASE BERIKUTNYA

> **Tujuan:** Memastikan dokumen ini cukup lengkap dan konkret untuk menjadi input utama pembuatan Test Cases, Test Scripts, dan Test Report.

- [ ] **5.1.** Periksa setiap skenario pengujian di **Bab 4 (Pemetaan Cakupan per Modul)**. Setiap skenario harus minimal memiliki:
  - ID Skenario yang unik dan konsisten (format: `MX-TC-NNN`)
  - Deskripsi skenario yang cukup jelas sehingga junior programmer dapat langsung membuat Test Case tanpa perlu membaca ulang dokumen SRS.
  - Referensi SRS terkait (ID SRS-F atau SRS-NF).
  - Referensi Use Case terkait (ID UC).
  - Tipe pengujian (Functional / Precision / Security / Database / CLI / Boundary / Integration / Integrity).
  - Prioritas (High / Medium / Low).
  - Jika ada kolom yang kosong: **Isi** dengan nilai yang sesuai.

- [ ] **5.2.** Periksa **Bab 5 (Pengujian Keamanan)**: Setiap sub-bab harus memiliki langkah-langkah pengujian yang **cukup detail dan berurutan** sehingga siapa pun yang membacanya dapat langsung mengeksekusi pengujian tersebut tanpa bertanya lebih lanjut.
  - Jika ada langkah yang terlalu abstrak/ambigu: **Perjelas** dengan langkah yang lebih spesifik dan konkret.

- [ ] **5.3.** Periksa **Bab 6 (Pengujian Presisi Desimal)**: Setiap skenario harus memiliki **nilai input konkret**, **kalkulasi yang diharapkan** (lengkap dengan angka), dan **expected database value** yang tertulis secara eksplisit.
  - Jika ada skenario yang masih abstrak: **Tambahkan nilai konkret** yang sesuai.

- [ ] **5.4.** Periksa **Bab 10 (Lingkungan Pengujian)**: Pastikan semua detail environment sudah cukup spesifik sehingga siapapun dapat me-reproduce environment pengujian yang identik. Minimum harus mencakup:
  - Spesifikasi hardware (CPU, RAM, Storage, Network).
  - Spesifikasi software (OS, versi Python, versi MySQL, versi semua library dependency).
  - Konfigurasi database sandbox (`abucom_test_db`).
  - Isi lengkap file konfigurasi `.env.test`.
  - Deskripsi test data / fixtures yang diperlukan.

- [ ] **5.5.** Periksa **Bab 11.2 (Jadwal Pengujian)**: Jika data R-14 (Development Roadmap) tidak tersedia, pastikan jadwal yang ada sudah **cukup realistis dan terstruktur** (ada siklus pengujian dengan durasi yang masuk akal dan fokus yang jelas per siklus).

- [ ] **5.6.** Periksa **Bab 14.2 (Template Test Case)** dan **Bab 14.3 (Template Test Report)**: Pastikan template sudah memiliki semua field yang diperlukan dan contoh pengisian yang tidak membingungkan.

---

### FASE 6: VALIDASI KRITERIA 5 — KUALITAS BAHASA INDONESIA

> **Tujuan:** Memastikan bahasa yang digunakan natural, tidak ambigu, dan mudah dipahami.

- [ ] **6.1.** Baca ulang seluruh dokumen dari Bab 1 hingga Bab 15. Untuk setiap kalimat atau paragraf yang:
  - Ambigu (bisa ditafsirkan lebih dari satu cara)
  - Menggunakan campuran Bahasa Indonesia dan Inggris yang tidak konsisten
  - Terlalu panjang dan berbelit (lebih dari 3 klausa dalam satu kalimat)
  - Menggunakan istilah teknis tanpa penjelasan padahal tidak ada di Bab 1.6 (Definisi/Akronim)
  
  **Ubah** kalimat tersebut menjadi lebih jelas, ringkas, dan tidak ambigu.

- [ ] **6.2.** Periksa konsistensi penggunaan istilah teknis di seluruh dokumen. Contoh:
  - Apakah "luring" dan "offline" digunakan secara konsisten?
  - Apakah "kasir" dan "klien" digunakan secara konsisten?
  - Apakah penulisan nama modul (M.1, M.2, dst.) konsisten di seluruh dokumen?
  - Jika ada inkonsistensi: **Standardisasi** penggunaan istilah di seluruh dokumen.

- [ ] **6.3.** Periksa **Bab 1.6 (Definisi, Akronim, dan Singkatan)**. Pastikan semua akronim dan istilah teknis yang digunakan di seluruh dokumen sudah terdaftar di sini. Jika ada istilah yang digunakan tapi belum terdaftar: **Tambahkan** ke Bab 1.6.
  - Periksa khususnya: `ACID`, `LAN`, `CLI`, `UAT`, `PPOB`, `OPEX`, `FP`, `UoM`, `BOM`, `HPP`, `RBAC`, `JWT`, `UU PDP`, `CRM`, `CSV`, `UPS`, `ATK`, `ERD`, `SRS`, `UC`, `SDLC`, `IEEE`, `ISTQB`.

- [ ] **6.4.** Periksa apakah ada **kalimat pasif yang membingungkan** yang dapat menimbulkan ambiguitas tentang siapa yang melakukan apa. Contoh: "Data akan diverifikasi" (oleh siapa? kapan?) → ubah menjadi "QA memverifikasi data dengan cara..." .

---

### FASE 7: VALIDASI KRITERIA 6 — TIDAK ADA DATA KOSONG / PLACEHOLDER

> **Tujuan:** Memastikan tidak ada data yang masih kosong, placeholder, atau bertanda "[DATA BELUM TERSEDIA]" yang belum diselesaikan.

- [ ] **7.1.** Cari semua teks yang mengandung pola berikut di seluruh dokumen (termasuk di dalam tabel dan kode block):
  - `[DATA BELUM TERSEDIA]`
  - `[TANGGAL]`
  - `[NAMA]`
  - `[Diisi Pasca Eksekusi]`
  - `[PASS / FAIL]`
  - `[DATA TIDAK DIKETAHUI]`
  - Atau pola serupa yang menunjukkan data yang belum diisi.

- [ ] **7.2.** Untuk setiap placeholder yang ditemukan, lakukan salah satu dari berikut:
  - **Jika data dapat disimpulkan dari konteks atau referensi yang ada**: Isi dengan data yang akurat dan relevan.
  - **Jika data terkait dengan referensi yang tidak tersedia (misal R-14)**: Ganti placeholder dengan pernyataan yang jelas menjelaskan kondisi tersebut DAN tambahkan nilai estimasi atau nilai tentatif yang masuk akal berdasarkan konteks proyek yang tersedia.
  - **Jika placeholder adalah bagian dari template** (seperti template Test Case atau Test Report yang memang harus diisi saat eksekusi): **Biarkan** dan tambahkan keterangan `*[Diisi saat eksekusi pengujian]*` yang jelas di sampingnya agar tidak membingungkan.

- [ ] **7.3.** Secara khusus, tangani item berikut yang teridentifikasi sebagai data belum tersedia:
  - **R-14 (Development Roadmap)** di Bab 11.2 dan Bab 15: Karena R-14 belum ada, Bab 11.2 Jadwal Pengujian harus diganti dari ketergantungan pada R-14 menjadi jadwal estimasi tentatif yang masuk akal berbasis scope modul yang sudah terdefinisi (M.1 s.d. M.10). Gunakan durasi total yang realistis untuk skala proyek AbuCom (UMKM, single developer/QA).

- [ ] **7.4.** Periksa **Bab 12 (Matriks Ketertelusuran)**: Pastikan tidak ada baris di tabel matriks yang memiliki kolom kosong (terutama kolom Status dan kolom Skenario Uji). Jika ada yang kosong: **Isi** atau **tandai dengan justifikasi yang jelas**.

- [ ] **7.5.** Periksa **Bab 11.3 (Alat Bantu Pengujian)**: Pastikan daftar tools yang disebutkan sudah lengkap dan termasuk:
  - `pytest` (framework unit test) beserta versi yang digunakan.
  - `coverage.py` (code coverage) beserta versi yang digunakan.
  - Tools untuk defect logging (berkas internal repositori).
  - Jika ada tool tambahan yang digunakan dalam environment pengujian (misalnya tool port scanning untuk uji firewall, tool load testing untuk uji connection pooling): **Tambahkan** ke sub-bab ini.

---

### FASE 8: VALIDASI KRITERIA TAMBAHAN — SPESIFIK DOKUMEN TEST PLAN

> **Tujuan:** Memeriksa aspek-aspek spesifik yang khas dari dokumen Test Plan dan sering terlewat dalam validasi standar.

- [ ] **8.1.** Periksa **konsistensi ID skenario uji** di seluruh dokumen:
  - Format ID harus konsisten: `MX-TC-NNN` (misalnya `M1-TC-001`, `M7-TC-007`).
  - Setiap ID yang disebutkan di Bab 4 harus muncul dengan ID yang identik di Bab 12.1 (Traceability Matrix).
  - Lakukan cross-check: catat semua ID yang ada di Bab 4, bandingkan dengan Bab 12.1. Jika ada ID yang ada di Bab 4 tetapi tidak ada di Bab 12.1 (atau sebaliknya): **Perbaiki** inkonsistensinya.

- [ ] **8.2.** Periksa apakah **total jumlah skenario uji** yang disebutkan di mana-mana sudah konsisten:
  - Hitung manual total skenario uji dari Bab 4 (M1-TC + M2-TC + M3-TC + M4-TC + M5-TC + M6-TC + M7-TC + M8-TC + M9-TC + M10-TC).
  - Bandingkan dengan angka yang disebutkan di Bab 13.3 (`Seluruh 44 Use Case`) dan Bab 14.3 template (`Total Kasus Uji Direncana: 45`).
  - Jika ada angka yang tidak konsisten: **Perbaiki** semua angka agar konsisten dengan total aktual skenario yang ada.

- [ ] **8.3.** Periksa apakah **Bab 2.4 (Risiko dan Mitigasi Pengujian)** sudah mencakup setidaknya risiko-risiko berikut (minimal 4 risiko):
  - Risiko Race Condition (sudah ada).
  - Risiko Gangguan LAN (sudah ada).
  - **Risiko Data Test Fixture Tidak Representatif**: Data seed tidak mencerminkan skenario bisnis nyata sehingga bug edge-case lolos.
  - **Risiko Ketergantungan Tool Eksternal**: Jika tool pengujian (pytest, coverage.py) mengalami masalah kompatibilitas dengan Python versi baru.
  - Jika risiko-risiko tambahan di atas belum ada: **Tambahkan** ke Bab 2.4 dengan format yang konsisten.

- [ ] **8.4.** Periksa apakah skenario uji untuk **pengujian negatif (negative testing)** sudah cukup terwakili di setiap modul:
  - Setiap modul kritis (M.1, M.2, M.4, M.7) harus memiliki minimal satu skenario uji negatif (input tidak valid, bypass akses, kondisi batas bawah/atas yang terlewat).
  - Jika ada modul yang kekurangan skenario uji negatif: **Tambahkan** skenario uji negatif yang relevan.

- [ ] **8.5.** Periksa apakah **kode error di Bab 12.4** sudah mencakup semua kode error yang disebutkan di skenario-skenario pengujian lainnya (Bab 5, Bab 6, Bab 7, Bab 8):
  - Buat daftar semua kode error `ERR-XXX-YYY` yang disebutkan di seluruh dokumen.
  - Bandingkan dengan tabel di Bab 12.4. Jika ada kode error yang disebutkan di bab lain tetapi tidak ada di Bab 12.4: **Tambahkan** ke tabel Bab 12.4.
  - Kode error yang sudah teridentifikasi dan harus ada: `ERR-AUTH-001`, `ERR-AUTH-002`, `ERR-AUTH-003`, `ERR-AUTH-011`, `ERR-AUTH-029`, `ERR-SESSION-001`, `ERR-SESSION-002`, `ERR-DB-001`, `ERR-DB-002`, `ERR-FILE-001`, `ERR-FILE-039`, `ERR-CASH-001`, `ERR-CASH-004`, `ERR-STOCK-010`, `ERR-VAL-007`.

- [ ] **8.6.** Periksa **Bab 3.4 (Entry & Exit Criteria)**: Pastikan setiap kriteria sudah **terukur secara kuantitatif** (ada angka atau kondisi yang dapat diverifikasi secara objektif), bukan hanya pernyataan kualitatif yang ambigu.
  - Contoh kriteria yang sudah terukur: "Unit Test Coverage ≥ 90%", "Tidak ada defect Critical/Major yang Open".
  - Contoh kriteria yang ambigu: "Sistem sudah siap" → **Ubah** menjadi kriteria yang terukur.

- [ ] **8.7.** Periksa apakah **Bab 13.3 (Checklist Sign-Off UAT)** sudah memuat semua kriteria penerimaan yang kritis. Minimal harus ada 7 kriteria yang dapat diverifikasi secara objektif oleh Pemilik Usaha dan Kepala Percetakan. Jika checklist saat ini kurang dari 7 kriteria: **Tambahkan** kriteria yang relevan.

- [ ] **8.8.** Periksa apakah ada **referensi silang yang putus** (broken reference) di dalam dokumen: yaitu, ketika dokumen menyebut "lihat Bab X" atau "sesuai SRS-F-XXX" tetapi bab atau ID tersebut tidak ada atau nomor babnya salah.
  - Lakukan verifikasi cross-reference untuk setiap rujukan internal yang ada.
  - Jika ada referensi yang putus: **Perbaiki** nomor bab atau ID yang salah.

- [ ] **8.9.** Periksa **Bab 14.3 (Template Test Report)**: Field-field yang ada dalam template harus mencerminkan metrik yang sudah didefinisikan di Bab 11.5. Pastikan template Test Report memiliki field untuk melaporkan semua metrik kualitas yang sudah ditetapkan (Defect Density, Test Pass Rate, Code Coverage).

---

### FASE 9: PENULISAN ULANG DAN OVERWRITE DOKUMEN

> **PENTING**: Fase ini adalah fase penulisan ulang final. Seluruh konten dokumen harus ditulis ulang sepenuhnya ke file target. Tidak ada pemotongan, peringkasan, atau penghilangan konten.

- [ ] **9.1.** Sebelum menulis, susun daftar semua perubahan yang akan dilakukan berdasarkan temuan dari Fase 1 hingga Fase 8. Kategorikan menjadi:
  - **Penambahan**: Konten baru yang akan ditambahkan (bab baru, baris tabel baru, skenario uji baru, entri glosarium baru).
  - **Perubahan**: Konten yang ada yang akan diubah atau diperbaiki.
  - **Penghapusan**: Konten yang tidak relevan yang akan dihapus atau diganti.

- [ ] **9.2.** Tulis ulang seluruh dokumen dari awal. Mulai dari baris pertama (YAML frontmatter) hingga baris terakhir (tabel Referensi Dokumen). Pastikan:
  - **Versi dokumen diubah** dari `1.0` menjadi `1.1` pada YAML frontmatter.
  - **Tanggal dokumen diperbarui** ke tanggal revisi saat ini.
  - **Status dokumen diubah** dari `Draft` menjadi `Reviewed` (atau status yang sesuai berdasarkan hasil validasi).
  - **Tabel Riwayat Perubahan Dokumen** (di Bab awal setelah frontmatter) ditambahkan baris baru untuk versi 1.1 yang mencatat apa saja yang direvisi pada sesi ini.

- [ ] **9.3.** Saat menulis ulang, ikuti ketentuan berikut secara ketat:
  - **DILARANG memotong** (truncate) bagian manapun dari dokumen, termasuk tabel, kode block, diagram ASCII, atau lampiran.
  - **DILARANG meringkas** konten yang sudah ada menjadi lebih pendek kecuali memang diperintahkan di langkah validasi sebelumnya.
  - **DILARANG menghilangkan** bab atau sub-bab yang sudah ada kecuali secara eksplisit diperintahkan di langkah validasi sebelumnya.
  - Seluruh perubahan dari hasil validasi Fase 1 s.d. Fase 8 harus **terintegrasi penuh** ke dalam tulisan ulang ini.

- [ ] **9.4.** Simpan dokumen yang telah ditulis ulang ke file:
  - **Path target**: `docs/sdlc/05_testing/01_test_plan.md`
  - **Mode penulisan**: Overwrite penuh (timpa seluruh isi file lama).
  - **Encoding**: UTF-8 tanpa BOM.

- [ ] **9.5.** Setelah selesai menulis, hitung jumlah total baris dokumen yang baru. Pastikan jumlah baris dokumen baru **tidak lebih sedikit** dari jumlah baris dokumen lama (912 baris), kecuali jika ada penghapusan konten yang memang disengaja berdasarkan hasil validasi.

---

### FASE 10: VERIFIKASI PASCA-PENULISAN

- [ ] **10.1.** Baca ulang dokumen yang baru ditulis dari baris 1 hingga baris terakhir untuk memastikan:
  - Tidak ada baris yang terpotong di tengah kalimat atau tabel.
  - Tidak ada bab yang hilang.
  - Struktur heading markdown (`#`, `##`, `###`) sudah konsisten dan hirarki yang benar.
  - Semua tabel markdown formatnya sudah valid (kolom sejajar, tidak ada sel kosong yang tidak disengaja).

- [ ] **10.2.** Verifikasi bahwa **versi dokumen di YAML frontmatter** dan **versi di Tabel Riwayat Perubahan** sama-sama sudah berubah menjadi `1.1`.

- [ ] **10.3.** Verifikasi bahwa **semua referensi file baru** yang ditambahkan selama proses validasi (jika ada file referensi tambahan yang ditemukan relevan) sudah ditambahkan ke **Bab 15 (Referensi Dokumen)** di baris paling bawah tabel referensi, dengan format kolom yang konsisten (No, Kode Ref, Nama Dokumen, Path File, Versi).

- [ ] **10.4.** Lakukan pengecekan akhir terhadap seluruh ID silang:
  - Cari semua ID skenario (MX-TC-NNN) di Bab 4 dan pastikan masing-masing muncul di Bab 12.1.
  - Cari semua ID SRS-F di Bab 12.1 dan pastikan sudah ada skenario ujinya di Bab 4.
  - Cari semua ID UC di Bab 12.3 dan pastikan konsisten dengan referensi di skenario uji.

- [ ] **10.5.** Laporkan ringkasan singkat hasil validasi dan perubahan yang dilakukan, dalam format:
  ```
  === RINGKASAN VALIDASI ISSUE 0044 ===
  Tanggal Eksekusi    : [TANGGAL]
  Pelaksana           : [NAMA / AI AGENT]
  Versi Sebelum       : v1.0
  Versi Sesudah       : v1.1
  
  Perubahan Utama:
  - [Daftar perubahan signifikan yang dilakukan]
  
  Referensi Tambahan:
  - [Daftar file referensi baru yang ditambahkan, jika ada]
  
  Status: SELESAI
  =====================================
  ```

---

## Catatan Penting untuk Pelaksana

> [!IMPORTANT]
> **Urutan eksekusi adalah wajib.** Jangan melompati fase atau mengerjakan secara paralel. Setiap fase bergantung pada hasil fase sebelumnya.

> [!WARNING]
> **Tidak ada truncation.** Saat menulis ulang dokumen di Fase 9, seluruh teks dari baris pertama hingga terakhir harus ditulis ulang sepenuhnya. Jika kapasitas output terbatas, bagi penulisan menjadi beberapa bagian berurutan (bagian 1, bagian 2, dst.) hingga seluruh dokumen selesai ditulis.

> [!CAUTION]
> **Jangan menggunakan konten dari memori atau pengetahuan umum** untuk mengisi data yang kosong. Semua data yang ditambahkan harus berasal dari dokumen referensi yang tersedia di `docs/sdlc/` atau dapat disimpulkan secara logis dari konteks proyek AbuCom yang sudah terdefinisi di dokumen-dokumen tersebut.

> [!NOTE]
> **File R-14 (Development Roadmap)** diketahui belum tersedia secara fisik. Tangani dengan membuat jadwal estimasi tentatif yang masuk akal berdasarkan scope yang sudah diketahui, dan catat secara eksplisit bahwa jadwal tersebut bersifat tentatif sampai R-14 tersedia.

---

## Output yang Diharapkan

Setelah issue ini diimplementasikan dengan benar, file `docs/sdlc/05_testing/01_test_plan.md` harus:

1. **Versi berubah** dari `v1.0` menjadi `v1.1`.
2. **Tidak ada placeholder** `[DATA BELUM TERSEDIA]` atau `[NAMA]` yang belum diselesaikan (kecuali yang memang merupakan bagian dari template eksekusi).
3. **Semua SRS-F dan SRS-NF** dari R-01 terpetakan di Bab 12.1 dan 12.2.
4. **Semua UC** dari R-02 terpetakan di Bab 12.3.
5. **Semua kode error** yang disebutkan di seluruh dokumen terdaftar di Bab 12.4.
6. **Risiko pengujian** minimal 4 risiko dengan mitigasi konkret di Bab 2.4.
7. **Checklist Sign-Off UAT** minimal 7 kriteria terukur di Bab 13.3.
8. **Glosarium** di Bab 14.1 mencakup semua akronim yang digunakan di seluruh dokumen.
9. **Referensi dokumen** di Bab 15 lengkap dan semua file referensi tambahan yang digunakan sudah ditambahkan.
10. **Bahasa Indonesia** yang konsisten, natural, dan tidak ambigu di seluruh dokumen.
11. **Total baris dokumen** tidak lebih sedikit dari dokumen versi sebelumnya (912 baris).

---

*Issue dibuat oleh: Senior QA Architect & SDLC Documentation Specialist*
*Tanggal pembuatan issue: 2026-05-26*
*Target implementasi: Junior Programmer / AI LLM Model*
