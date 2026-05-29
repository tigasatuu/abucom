---
judul      : Validasi, Audit, dan Perbaikan Dokumen Release Notes AbuCom
target_file: docs/sdlc/06_deployment/03_release_notes.md
prioritas  : HIGH
status     : OPEN
dibuat_oleh: Antigravity (Senior DevOps Lead)
tanggal    : 2026-05-30
---

# Validasi, Audit, dan Perbaikan Dokumen Release Notes AbuCom

## Konteks Issue

| Atribut | Detail |
|---|---|
| **Dokumen Utama** | Release Notes |
| **Target File** | `docs/sdlc/06_deployment/03_release_notes.md` |
| **Versi Dokumen Saat Ini** | `v1.1` |
| **Versi Target Setelah Revisi** | `v1.2` |
| **Lokasi Referensi** | `docs/sdlc/` |
| **Fase SDLC** | Fase 06 — Deployment (Deliverable ke-3) |
| **Total Referensi Terdaftar** | 16 berkas (`R-01` s.d `R-16`) |

---

## Tujuan Issue

Issue ini bertujuan untuk mengorkestrasi audit menyeluruh terhadap dokumen `03_release_notes.md` sebagai catatan rilis resmi produk **AbuCom CLI v1.0.0**. Dokumen ini adalah dokumen **akhir Fase 06 — Deployment** yang menjadi pintu gerbang menuju Fase 07 — Maintenance dan serah terima sistem kepada Pemilik Usaha. Kualitasnya harus bebas dari ambiguitas, inkonsistensi data, dan kekosongan informasi.

---

## Persona Implementor

> **WAJIB DIBACA SEBELUM MEMULAI PEKERJAAN**

Kamu adalah seorang **Senior Release Manager & Quality Assurance Lead** yang memiliki keahlian gabungan sebagai:
- **Technical Documentation Auditor** berpengalaman 10+ tahun dalam menyusun dan memvalidasi dokumen rilis industri perangkat lunak (Release Notes, Change Log, BAST).
- **Senior DevOps Engineer** yang memahami seluk-beluk deployment, topologi jaringan LAN offline, konfigurasi server Linux/Windows, enkripsi, dan prosedur backup/restore.
- **Python Backend Developer** yang menguasai ekosistem: `mysql-connector-python`, `bcrypt`, `pyjwt`, `cryptography` (Fernet), `rich`, `tabulate`, serta paradigma *Functional Programming* murni.
- **Business Analyst** yang memahami alur bisnis percetakan (BOM, HPP, payroll dinamis, poin insentif, kas harian) agar dapat mendeteksi ketidaksesuaian data bisnis.
- **Compliance Officer** yang memahami kepatuhan **UU PDP No. 27 Tahun 2022** dan standar keamanan RBAC 8 peran.

Kamu **tidak boleh berasumsi**. Setiap klaim data dalam dokumen utama **wajib diverifikasi** dengan membandingkannya secara langsung terhadap file referensi yang tertulis di Bab 19 dokumen target.

---

## Instruksi Implementasi (Step-by-Step)

Ikuti setiap langkah di bawah ini **secara berurutan**. Jangan melompati langkah. Tandai setiap checklist `[ ]` menjadi `[x]` saat selesai dikerjakan.

---

### FASE 0 — PERSIAPAN & PEMBACAAN DOKUMEN

- [ ] **0.1** Baca seluruh isi `docs/sdlc/06_deployment/03_release_notes.md` dari **baris pertama hingga baris terakhir** tanpa melewati satu bab pun. Catat secara mental bab-bab utama: 1 (Info Dokumen), 2 (Summary Rilis), 3 (System Requirements), 4 (New Features), 5 (Security), 6 (Bug Fixes), 7 (Known Limitations), 8 (Known Issues), 9 (Panduan Instalasi), 10 (Default Config), 11 (QA Summary), 12 (Arsitektur), 13 (Matriks Risiko), 14 (Tim Pengembang), 15 (Roadmap), 16 (Dukungan Teknis), 17 (Persetujuan), 18 (Glosarium), 19 (Referensi).

- [ ] **0.2** Baca seluruh isi **16 file referensi** yang terdaftar di Bab 19 dokumen target, satu per satu secara lengkap:
  - [ ] **R-01** `docs/sdlc/01_planning/01_project_charter.md`
  - [ ] **R-02** `docs/sdlc/02_analysis/02_software_requirements.md`
  - [ ] **R-03** `docs/sdlc/06_deployment/01_deployment_guide.md`
  - [ ] **R-04** `docs/sdlc/06_deployment/02_environment_config.yaml`
  - [ ] **R-05** `docs/sdlc/05_testing/01_test_plan.md`
  - [ ] **R-06** `docs/sdlc/03_design/03_system_architecture.md`
  - [ ] **R-07** `docs/sdlc/03_design/06_security_design.md`
  - [ ] **R-08** `docs/sdlc/01_planning/04_tech_stack_decision.md`
  - [ ] **R-09** `docs/sdlc/03_design/01_database_schema.sql`
  - [ ] **R-10** `docs/sdlc/04_implementation/03_module_structure.md`
  - [ ] **R-11** `docs/sdlc/04_implementation/04_git_workflow.md`
  - [ ] **R-12** `docs/sdlc/05_testing/02_test_cases.md`
  - [ ] **R-13** `docs/sdlc/05_testing/03_uat_script.md`
  - [ ] **R-14** `docs/sdlc/05_testing/04_bug_report_template.md`
  - [ ] **R-15** `docs/sdlc/02_analysis/06_access_control_matrix.md`
  - [ ] **R-16** `docs/sdlc/04_implementation/01_coding_standard.md`

- [ ] **0.3** Catat setiap **ketidaksesuaian, data kosong, placeholder yang belum diisi, atau klaim yang terasa janggal** yang kamu temukan selama pembacaan, sebelum memulai analisis formal.

---

### FASE 1 — AUDIT KELENGKAPAN DATA (COVERAGE CHECK)

> **Tujuan:** Memastikan dokumen utama sudah menyerap semua data dan informasi penting dari seluruh 16 file referensi yang relevan dan spesifik bagi sebuah Release Notes.

- [ ] **1.1 — Verifikasi Fitur vs SRS (R-02)**
  - [ ] Buka `docs/sdlc/02_analysis/02_software_requirements.md`.
  - [ ] Buat daftar seluruh kebutuhan fungsional (`SRS-F-001` s.d `SRS-F-040` dan `SRS-F-ADD-01` s.d `SRS-F-ADD-05`) yang tercantum di SRS.
  - [ ] Periksa satu per satu: apakah **setiap** item SRS tersebut sudah tercakup di Bab 4 (Fitur Baru) dokumen release notes? Jika ada yang belum tercakup, catat kodenya.
  - [ ] Periksa apakah **nama modul** (M.1 s.d M.10) di release notes **selaras** dengan nama modul yang tertulis di SRS. Jika ada perbedaan penamaan, catat.
  - [ ] Periksa apakah **deskripsi singkat setiap fitur** di Bab 4 release notes **konsisten** (tidak bertentangan) dengan deskripsi di SRS. Catat ketidaksesuaian data numerik (misalnya: limit kasbon, nilai UMR, tier poin, dll.).

- [ ] **1.2 — Verifikasi System Requirements vs System Architecture (R-06)**
  - [ ] Buka `docs/sdlc/03_design/03_system_architecture.md`.
  - [ ] Periksa apakah spesifikasi hardware di Bab 3.1 release notes (processor, RAM, storage) **identik** dengan yang tertulis di dokumen arsitektur. Catat jika ada perbedaan.
  - [ ] Periksa apakah topologi jaringan di Bab 12 (IP statis `192.168.1.200`, segmen `192.168.1.0/24`, star topology) **selaras** dengan dokumen arsitektur.
  - [ ] Periksa apakah `connection pool size = 5` dan `retry 3x exponential backoff` di Bab 12 **sesuai** dengan yang tertulis di arsitektur.

- [ ] **1.3 — Verifikasi Security Features vs Security Design (R-07)**
  - [ ] Buka `docs/sdlc/03_design/06_security_design.md`.
  - [ ] Periksa apakah nilai `bcrypt cost factor = 12`, `salt length = 16 bytes`, `JWT lifetime = 28800 detik (8 jam)`, `algoritma JWT = HS256`, `rate limit lockout = 5x gagal login 10 menit` di Bab 5 dan Bab 10 release notes **identik** dengan yang tertulis di Security Design.
  - [ ] Periksa apakah penyebutan `Fernet (cryptography) 32-byte Base64 key` dan kepatuhan `UU PDP No. 27 Tahun 2022` **sesuai** dengan Security Design.
  - [ ] Periksa apakah `AES-256 ZIP backup`, `retensi 30 hari`, `cold storage 12 bulan`, dan jadwal cron `0 21 * * *` **sesuai** dengan Security Design. Jika ada perbedaan, catat.
  - [ ] Periksa apakah **8 peran RBAC** di Bab 5.2 release notes (pemilik, kepala_percetakan, kasir, desainer, produksi_cetak, gudang, pramuniaga, fotocopy_print) **identik** dengan yang tertulis di dokumen Security Design dan Access Control Matrix (R-15).

- [ ] **1.4 — Verifikasi Matriks RBAC vs Access Control Matrix (R-15)**
  - [ ] Buka `docs/sdlc/02_analysis/06_access_control_matrix.md`.
  - [ ] Periksa setiap sel matriks hak akses di Bab 5.2 release notes. Pastikan setiap tanda `X` (memiliki akses) dan tanda `—` (tidak memiliki akses) **persis sama** dengan data di Access Control Matrix resmi. Catat setiap sel yang berbeda.

- [ ] **1.5 — Verifikasi Runtime & Dependensi vs Tech Stack Decision (R-08)**
  - [ ] Buka `docs/sdlc/01_planning/04_tech_stack_decision.md`.
  - [ ] Periksa apakah versi library di Bab 3.2.3 release notes (`mysql-connector-python==8.4.0`, `python-dotenv==1.0.1`, `bcrypt==4.1.0`, `pyjwt==2.8.0`, `cryptography==42.0.5`, `rich==13.7.0`, `tabulate==0.9.0`, `pytest==8.2.0`, `coverage==7.5.1`) **identik** dengan yang terdaftar di Tech Stack Decision. Catat perbedaan versi.
  - [ ] Periksa apakah versi `Python 3.14.2+` dan `MySQL Community Server 8.4 LTS` **sesuai** dengan yang ada di Tech Stack Decision.

- [ ] **1.6 — Verifikasi Hasil Pengujian vs Test Plan & Test Cases (R-05, R-12, R-13)**
  - [ ] Buka `docs/sdlc/05_testing/01_test_plan.md`.
  - [ ] Periksa apakah angka **44 skenario uji**, **70 kasus uji**, **94.2% code coverage**, dan **7 exit criteria** di Bab 11 release notes **identik** dengan yang tertulis di Test Plan. Catat perbedaan.
  - [ ] Buka `docs/sdlc/05_testing/02_test_cases.md`. Verifikasi angka 70 kasus uji.
  - [ ] Buka `docs/sdlc/05_testing/03_uat_script.md`. Verifikasi angka **44 skrip UAT individual** dan **1 skrip UAT E2E** serta **nama pelaksana UAT** (Bpk. Abu dan Bpk. Cetak).
  - [ ] Periksa apakah **7 exit criteria** di Bab 11.4 release notes lengkap dan urutannya **sesuai** dengan Test Plan.

- [ ] **1.7 — Verifikasi Prosedur Instalasi vs Deployment Guide (R-03)**
  - [ ] Buka `docs/sdlc/06_deployment/01_deployment_guide.md`.
  - [ ] Periksa apakah **8 langkah setup server** di Bab 9.1.1 dan **5 langkah setup klien kasir** di Bab 9.1.2 release notes **konsisten** dengan Deployment Guide. Jika urutan atau detail langkah berbeda, catat.
  - [ ] Periksa apakah prosedur rollback di Bab 9.3 release notes **selaras** dengan runbook rollback yang ada di Deployment Guide.
  - [ ] Periksa apakah **8 risiko** di Bab 13 Matriks Risiko release notes **identik** (deskripsi, prob, dampak, skor, mitigasi, kontingensi) dengan matriks risiko di Deployment Guide. Catat setiap perbedaan.

- [ ] **1.8 — Verifikasi Parameter Default vs Environment Config (R-04)**
  - [ ] Buka `docs/sdlc/06_deployment/02_environment_config.yaml`.
  - [ ] Periksa apakah seluruh nilai parameter di Bab 10 (Konfigurasi Default Rilis) release notes — termasuk: DB host, port, pool size, retry attempts, bcrypt cost, JWT lifetime, rate limit, backup retensi, dan 13 baris tabel `system_configs` — **identik** dengan yang ada di `environment_config.yaml`. Catat setiap perbedaan nilai.
  - [ ] Periksa apakah **SOP startup pukul 07:45 WIB** dan **SOP shutdown pukul 20:45–21:05 WIB** serta **modal awal Rp 200.000** di Bab 10.3 **sesuai** dengan yang tertulis di environment config atau deployment guide.

- [ ] **1.9 — Verifikasi Known Issues vs Bug Report Template (R-14)**
  - [ ] Buka `docs/sdlc/05_testing/04_bug_report_template.md`.
  - [ ] Periksa apakah **2 known issues** (`DEF-COMPAT-001` dan `DEF-PERF-001`) di Bab 8 release notes **sudah selaras** dengan format ID dan deskripsi bug yang ada di bug report template.
  - [ ] Periksa apakah angka performa latensi **8.75 detik** pada `DEF-PERF-001` (data volume > 50.000 record) tercatat atau dapat dikonfirmasi dari Test Cases (R-12).

- [ ] **1.10 — Verifikasi Tim Pengembang & RACI Matrix vs Project Charter (R-01)**
  - [ ] Buka `docs/sdlc/01_planning/01_project_charter.md`.
  - [ ] Periksa apakah **7 anggota tim** di Bab 14.1 dan **peran masing-masing** sesuai dengan Project Charter. Catat perbedaan nama, model AI, atau peran.
  - [ ] Periksa apakah **RACI Matrix** di Bab 14.2 release notes **konsisten** dengan RACI di Project Charter (jika ada).

- [ ] **1.11 — Verifikasi Roadmap vs Project Charter (R-01)**
  - [ ] Periksa apakah **fitur roadmap** di Bab 15 (GUI, Mobile Admin, WhatsApp Gateway, QRIS, PPOB otomatis) **selaras** dengan roadmap atau milestone yang tertulis di Project Charter.

- [ ] **1.12 — Verifikasi Database Schema (R-09)**
  - [ ] Buka `docs/sdlc/03_design/01_database_schema.sql`.
  - [ ] Periksa apakah nama database `abucom_db` (dan `abucom_test_db` untuk sandbox) **sesuai** dengan yang ada di schema.
  - [ ] Periksa apakah nama tabel `system_configs`, `pelanggan`, nama kolom `cabang_id`, `whatsapp` yang disebut di release notes **ada dan sesuai** dengan DDL di database schema.
  - [ ] Periksa apakah klaim **28 tabel DDL InnoDB** di tabel referensi Bab 19 (R-09) **sesuai** dengan jumlah tabel aktual di `database_schema.sql`.

- [ ] **1.13 — Verifikasi Module Structure & Git Workflow (R-10, R-11)**
  - [ ] Buka `docs/sdlc/04_implementation/03_module_structure.md`. Periksa apakah path `exports/receipts/` yang disebut di SRS-F-006 **ada** di struktur modul. Periksa apakah path `utils/backup_cron.sh` yang disebut di Bab 9.1.1 **ada** di struktur modul.
  - [ ] Buka `docs/sdlc/04_implementation/04_git_workflow.md`. Periksa apakah perintah rollback `git checkout v0.9.0-stable` di Bab 9.3.2 **sesuai** dengan konvensi Git tagging yang ditetapkan di Git Workflow.

---

### FASE 2 — AUDIT RELEVANSI DATA (FOKUS & KEBERSIHAN KONTEN)

> **Tujuan:** Memastikan dokumen utama **tidak memuat data yang tidak seharusnya ada** dalam sebuah Release Notes (tidak ada scope creep data dari dokumen SDLC lain).

- [ ] **2.1** Periksa apakah Bab 3 (System Requirements) **hanya memuat** ringkasan kebutuhan sistem yang relevan untuk pengguna akhir rilis, bukan detail teknis mendalam yang seharusnya hanya ada di Deployment Guide atau Architecture Design.

- [ ] **2.2** Periksa apakah Bab 9 (Panduan Instalasi) bersifat **ringkasan / high-level** yang cukup sebagai panduan cepat, dan **tidak menduplikasi** seluruh isi Deployment Guide secara verbatim. Release Notes bukanlah Deployment Guide.

- [ ] **2.3** Periksa apakah Bab 10 (Konfigurasi Default) hanya menampilkan **nilai-nilai default yang paling kritis dan relevan** bagi pembaca rilis, dan tidak mencantumkan detail konfigurasi yang terlalu teknis hingga seharusnya berada di `environment_config.yaml`.

- [ ] **2.4** Periksa apakah Bab 4 (Fitur Baru) **tidak memuat detail implementasi teknis kode** (seperti contoh SQL query, kode Python, atau diagram flowchart modul) yang seharusnya berada di SRS atau SDD, bukan di Release Notes.

- [ ] **2.5** Periksa apakah Bab 12 (Arsitektur) hanya menampilkan **diagram deployment tingkat tinggi** yang relevan untuk pengguna rilis, bukan diagram detail arsitektur internal yang seharusnya berada di System Architecture Document.

- [ ] **2.6** Periksa apakah Bab 18 (Glosarium) hanya memuat **istilah yang benar-benar muncul dan digunakan** di dalam dokumen release notes ini, dan **tidak memuat** istilah yang tidak pernah disebutkan dalam dokumen ini.

---

### FASE 3 — AUDIT STRUKTUR DOKUMEN (STANDAR INDUSTRI)

> **Tujuan:** Memastikan dokumen memiliki struktur yang sesuai dengan standar industri Release Notes perangkat lunak profesional.

- [ ] **3.1** Periksa apakah **front matter YAML** di baris 1–10 sudah lengkap: `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun`, `reviewer`, `approved_by`. Pastikan nilainya tidak ada yang kosong atau placeholder.

- [ ] **3.2** Periksa apakah **Riwayat Perubahan Dokumen** (Change Log) di bagian awal memuat minimal: versi dokumen, tanggal, deskripsi perubahan, dan penulis — **untuk setiap versi yang pernah ada**. Pastikan versi `v1.0` dan `v1.1` kedua-duanya tercatat.

- [ ] **3.3** Periksa apakah setiap bab memiliki **nomor bab yang berurutan dan konsisten** tanpa ada yang lompat atau terduplikasi (Bab 1 s.d Bab 19).

- [ ] **3.4** Periksa apakah **Bab 1 (Informasi Dokumen)** sudah lengkap memuat: tujuan, cakupan, posisi dalam SDLC, hubungan input/output dengan dokumen lain, audiens target, dan definisi/akronim.

- [ ] **3.5** Periksa apakah **Bab 2 (Ringkasan Rilis)** sudah memuat: nama produk, versi, tanggal rilis, tipe rilis, deskripsi umum, dan highlight fitur utama — sesuai standar Release Notes industri.

- [ ] **3.6** Periksa apakah **Bab 8 (Known Issues)** menggunakan format tabel yang standar: ID masalah, modul, deskripsi, dampak, dan rencana mitigasi (workaround).

- [ ] **3.7** Periksa apakah **Bab 13 (Matriks Risiko)** menggunakan format tabel yang standar: ID risiko, komponen, deskripsi, probabilitas, dampak, skor, mitigasi, dan kontingensi — dan apakah **skor risiko** dihitung dengan benar (Prob × Dampak).
  - Contoh verifikasi: RSK-01 (Prob=3, Dampak=5) → Skor harus = 15. RSK-02 (Prob=3, Dampak=4) → Skor harus = 12. Verifikasi semua 8 baris.

- [ ] **3.8** Periksa apakah **Bab 17 (Persetujuan dan Otorisasi)** memuat tabel dengan: posisi stakeholder, nama lengkap, tanda tangan/status, dan tanggal persetujuan — untuk **semua pihak** yang relevan.

- [ ] **3.9** Periksa apakah **Bab 19 (Referensi Dokumen)** memuat tabel dengan kolom: nomor, kode referensi, nama dokumen, path relatif, versi, prioritas, dan peran/hubungan dalam penyusunan — untuk **semua 16 referensi yang diklaim**.

- [ ] **3.10** Periksa apakah semua **path referensi** di Bab 19 menggunakan format yang konsisten (path relatif dari root proyek) dan **tidak ada path yang salah** atau mengarah ke file yang tidak ada.
  - Buka setiap path file referensi tersebut secara langsung untuk memverifikasi keberadaannya di filesystem.

- [ ] **3.11** Periksa apakah **diagram Mermaid** di Bab 12.1 dapat dirender tanpa error sintaks (tidak ada kurung yang tidak tutup, tidak ada spasi yang aneh dalam label node, semua `classDef` terdefinisi).

- [ ] **3.12** Periksa apakah dokumen sudah memiliki **separator horizontal** (`---`) yang konsisten antar bab untuk memisahkan secara visual setiap bagian besar.

---

### FASE 4 — AUDIT KELAYAKAN SEBAGAI REFERENSI FASE SDLC BERIKUTNYA

> **Tujuan:** Memastikan dokumen ini layak menjadi input bagi fase SDLC setelah deployment (Fase 07 — Maintenance, User Manual, Serah Terima Formal).

- [ ] **4.1** Periksa apakah **Bab 2.2 (Tanggal Rilis)** sudah diisi dengan tanggal konkret atau memiliki catatan yang jelas jika masih estimasi. Pastikan status estimasi tidak membingungkan pembaca dokumen di Fase 07.

- [ ] **4.2** Periksa apakah **Bab 11.4 (Exit Criteria)** memuat pernyataan yang cukup kuat sebagai dasar bahwa UAT sign-off telah selesai dan sistem **siap go-live**. Dokumen Maintenance tidak boleh meragukan kelayakan go-live setelah membaca bab ini.

- [ ] **4.3** Periksa apakah **Bab 16 (Dukungan Teknis)** memuat informasi kontak yang cukup detail dan operasional — termasuk nomor WhatsApp, email, jam layanan, dan prosedur eskalasi 3 fase — agar tim maintenance dan pengguna dapat mengandalkan dokumen ini sebagai panduan pertama saat terjadi insiden.

- [ ] **4.4** Periksa apakah **Bab 7 (Known Limitations)** dan **Bab 8 (Known Issues)** sudah cukup jelas dan tidak ambigu, sehingga tim maintenance tidak perlu membaca ulang semua 16 dokumen referensi hanya untuk memahami batasan sistem.

- [ ] **4.5** Periksa apakah **Bab 15 (Roadmap)** memberikan gambaran yang cukup jelas tentang fitur yang direncanakan untuk versi berikutnya (v1.1.0, v2.0.0), sehingga dapat dijadikan acuan *backlog* awal untuk fase maintenance dan pengembangan selanjutnya.

- [ ] **4.6** Periksa apakah **semua cross-reference** antar bab dalam dokumen (misalnya "lihat Bab 10.4", "lihat Bab 5.2") sudah **mengarah ke nomor bab yang benar** dan konsisten dengan nomor bab aktual di dokumen.

---

### FASE 5 — AUDIT BAHASA INDONESIA

> **Tujuan:** Memastikan seluruh teks ditulis dalam bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau LLM AI yang lebih kecil.

- [ ] **5.1** Periksa apakah **semua istilah teknis** yang pertama kali disebutkan sudah diikuti padanan singkatan atau penjelasan singkat dalam tanda kurung. Contoh: "LAN (Local Area Network)", "JWT (JSON Web Token)". Jika tidak, tambahkan.

- [ ] **5.2** Periksa apakah **Bab 1.6 (Definisi dan Akronim)** memuat **semua** istilah teknis yang digunakan di seluruh dokumen dan tidak ada yang terlewat.

- [ ] **5.3** Periksa apakah **Bab 18 (Glosarium)** sudah sinkron dengan **Bab 1.6 (Definisi dan Akronim)** — tidak ada istilah yang ada di satu bab tetapi tidak ada di bab lainnya, kecuali memang ada alasan yang jelas.

- [ ] **5.4** Periksa seluruh kalimat di dokumen ini. Jika ada kalimat yang:
  - Terlalu panjang dan bertumpuk (lebih dari 3 anak kalimat berurutan tanpa pemisah yang jelas),
  - Menggunakan bahasa yang ambigu (bisa ditafsirkan lebih dari satu cara),
  - Menggunakan istilah yang saling bertentangan antara satu bab dengan bab lain,
  - Menggunakan campuran bahasa Inggris dan Indonesia yang tidak perlu,
  maka perbaiki kalimat tersebut agar lebih natural dan mudah dipahami.

- [ ] **5.5** Periksa apakah **judul bab dan sub-bab** menggunakan format yang konsisten: Bahasa Indonesia sebagai judul utama, dengan keterangan bahasa Inggris dalam tanda kurung untuk istilah industri standar (contoh: `## 4. Fitur Baru (New Features)`).

- [ ] **5.6** Periksa apakah **penulisan angka mata uang Rupiah** menggunakan format yang konsisten di seluruh dokumen. Contoh: `Rp 15.000.000` (bukan `Rp15000000` atau `Rp 15,000,000`).

- [ ] **5.7** Periksa apakah **penulisan tanggal** menggunakan format yang konsisten di seluruh dokumen. Contoh: `2026-05-27` (ISO 8601) atau `27 Mei 2026` (format Indonesia). Pastikan tidak ada pencampuran format dalam konteks yang sama.

---

### FASE 6 — AUDIT KELENGKAPAN & DATA KOSONG

> **Tujuan:** Memastikan tidak ada placeholder, data kosong, atau field yang belum diisi yang akan menghambat pekerjaan Fase SDLC selanjutnya.

- [ ] **6.1** Periksa **front matter YAML** (baris 1–10): apakah semua nilai sudah diisi? Khususnya periksa `tanggal`, `status`, `penyusun`, `reviewer`, `approved_by`. Jika ada yang masih berupa placeholder seperti `[DIISI]` atau `TBD`, isi dengan nilai yang sesuai berdasarkan konteks dokumen.

- [ ] **6.2** Periksa **Bab 2.2 (Tanggal Rilis)**: nilai `2027-05-20` dengan keterangan *(Estimasi, konfirmasi setelah UAT sign-off selesai)* — evaluasi apakah keterangan ini masih relevan mengingat Bab 11.3 menyatakan UAT sudah selesai dengan status PASS 100%. Jika UAT sudah selesai, maka tanggal rilis tidak lagi berstatus "estimasi". Perbaiki teks penjelasannya agar tidak bertentangan.

- [ ] **6.3** Periksa **Bab 11.3**: apakah nama **"Bpk. Abu (Pemilik Usaha / Sponsor)"** dan **"Bpk. Cetak (Kepala Percetakan / Key User)"** sebagai pelaksana UAT sudah konsisten dengan nama yang tertera di **Bab 17 (Persetujuan)** yaitu `Alfatih` dan `Donsise`? Jika ada ketidaksesuaian nama, selaraskan — gunakan nama resmi yang tercatat di Project Charter (R-01) sebagai acuan.

- [ ] **6.4** Periksa **Bab 16.1 (Kontak Dukungan Teknis)**: apakah nomor WhatsApp `+62-812-3456-7890` dan email `support@abucom.com` merupakan data **placeholder** atau data nyata? Jika ini adalah placeholder, evaluasi apakah perlu diganti dengan data yang lebih representatif sesuai konteks proyek AbuCom (misalnya mengacu pada nomor kontak pemilik usaha di Project Charter), atau tambahkan catatan eksplisit bahwa ini adalah data placeholder yang wajib diisi sebelum go-live.

- [ ] **6.5** Periksa **Bab 9.3.2 (Rollback Kode Klien Kasir)**: perintah `git checkout v0.9.0-stable` mengimplikasikan adanya versi sebelumnya. Karena ini adalah rilis perdana v1.0.0, periksa apakah prosedur rollback ini **relevan dan valid** atau perlu diklarifikasi/diubah (misalnya: menjadi prosedur uninstall dan reinstall clean).

- [ ] **6.6** Periksa **Bab 9.4 (Referensi Deployment Guide)**: apakah teks dan link path yang tercantum di bab ini sudah benar dan mengarah ke file yang tepat.

- [ ] **6.7** Periksa seluruh dokumen untuk menemukan kemunculan kata atau frasa berikut yang menandakan data belum diisi: `[DIISI]`, `[TBD]`, `[PLACEHOLDER]`, `TODO`, `N/A` (yang tidak disengaja), `xxx`, atau tanda tanya tanpa konteks `?`. Jika ditemukan, isi dengan data yang sesuai berdasarkan konteks dokumen dan referensi yang ada.

- [ ] **6.8** Periksa apakah **Bab 6 (Bug Fixes & Improvements)** sudah cukup untuk sebuah rilis perdana. Evaluasi apakah perlu menambahkan catatan bahwa structural gap nomor SRS yang disebutkan (SRS-F-039 dan SRS-F-040) sudah terselesaikan, dengan merujuk pada SRS versi final (R-02).

---

### FASE 7 — AUDIT KHUSUS CIRI KHAS RELEASE NOTES

> **Tujuan:** Memeriksa aspek-aspek yang spesifik hanya berlaku untuk dokumen Release Notes dan tidak ada di dokumen SDLC lain.

- [ ] **7.1 — SemVer Consistency:** Periksa apakah format versi produk `v1.0.0` mengikuti konvensi **Semantic Versioning (SemVer)** dengan benar: `MAJOR.MINOR.PATCH`. Untuk rilis perdana, nilai yang tepat adalah `1.0.0` (bukan `1.0` atau `1`). Periksa di semua bab apakah penulisan versi konsisten.

- [ ] **7.2 — Changelog & Traceability:** Periksa apakah setiap fitur baru di Bab 4 memiliki referensi kode SRS (misalnya `[SRS-F-001]`) yang memungkinkan pembaca melacak kembali fitur ke dokumen spesifikasi. Ini adalah standar traceability Release Notes yang baik.

- [ ] **7.3 — Known Issues Format:** Pastikan Bab 8 menggunakan **ID unik** untuk setiap masalah (format `DEF-XXXX-NNN`) dan tabel sudah mencakup kolom: `ID Masalah`, `Modul`, `Deskripsi`, `Dampak Teknis`, `Rencana Mitigasi (Workaround)`.

- [ ] **7.4 — Upgrade Path:** Periksa apakah Bab 9.2 (Upgrade dari Versi Sebelumnya) sudah secara eksplisit menyatakan bahwa ini adalah **rilis perdana** dan **tidak ada prosedur upgrade** dari versi sebelumnya. Teks ini harus jelas dan tidak membingungkan.

- [ ] **7.5 — Release Approval Gate:** Periksa apakah Bab 17 (Persetujuan dan Otorisasi) merepresentasikan sebuah **approval gate** yang sah — yaitu ada pernyataan eksplisit bahwa rilis ini disetujui untuk didistribusikan — bukan hanya daftar tanda tangan tanpa konteks.

- [ ] **7.6 — Exit Criteria Completeness:** Periksa 7 Exit Criteria di Bab 11.4. Evaluasi apakah ada exit criteria yang penting namun **belum tercantum** untuk sebuah rilis perdana sistem kasir, seperti: verifikasi integritas backup awal, verifikasi konfigurasi firewall berhasil diaktifkan, atau konfirmasi pelatihan staf telah selesai. Jika ada yang relevan, tambahkan.

- [ ] **7.7 — Risk Score Validation:** Verifikasi secara matematis semua 8 nilai skor risiko di Bab 13:
  - RSK-01: 3 × 5 = 15 ✓
  - RSK-02: 3 × 4 = 12 ✓
  - RSK-03: 2 × 5 = 10 ✓
  - RSK-04: 2 × 4 = 8 ✓
  - RSK-05: 3 × 3 = 9 ✓
  - RSK-06: 3 × 3 = 9 ✓
  - RSK-07: 1 × 5 = 5 ✓
  - RSK-08: 2 × 4 = 8 ✓
  - Jika ada nilai yang salah, koreksi.

- [ ] **7.8 — Hypercare Period:** Periksa apakah dokumen menyebutkan adanya **periode Hypercare** pasca go-live (masa pendampingan intensif setelah deployment). Ini adalah praktik industri standar untuk rilis perdana. Bab 13 RSK-06 menyebutkan "DevOps Engineer bersiaga luring selama masa Hypercare" namun tidak ada bab atau sub-bab yang mendefinisikan durasi dan ruang lingkup Hypercare. Jika tidak ada, tambahkan sub-bab singkat di Bab 16 atau buat catatan di Bab 2 tentang periode Hypercare.

---

### FASE 8 — PENULISAN ULANG DOKUMEN (OVERWRITE)

> **PERHATIAN KRITIS — BACA BAIK-BAIK SEBELUM MENULIS**

- [ ] **8.1 — Kompilasi Temuan:** Sebelum menulis, kompilasi semua temuan dari Fase 1 s.d 7 menjadi daftar perubahan yang terstruktur: (a) data yang perlu dikoreksi, (b) kalimat yang perlu diperbaiki, (c) konten yang perlu ditambahkan, (d) konten yang perlu dihapus karena tidak relevan.

- [ ] **8.2 — Update Versi Dokumen:** Ubah versi dokumen dari `v1.1` menjadi **`v1.2`** di:
  - [ ] Baris front matter YAML (`versi: 1.2`).
  - [ ] Judul utama dokumen (`# Release Notes — AbuCom v1.0.0` tidak berubah — ini versi *produk*, bukan versi *dokumen*).
  - [ ] Tabel Riwayat Perubahan Dokumen: tambahkan baris baru untuk `v1.2` dengan tanggal hari ini (`2026-05-30`), deskripsi perubahan yang dilakukan, dan nama reviewer.

- [ ] **8.3 — Update Tanggal:** Ubah nilai `tanggal` di front matter menjadi **`2026-05-30`** (tanggal revisi saat ini).

- [ ] **8.4 — Terapkan Semua Koreksi:** Terapkan seluruh koreksi yang sudah dikompilasi dari Fase 1 s.d 7 ke dalam naskah dokumen. Tidak ada perbaikan yang boleh dilewatkan.

- [ ] **8.5 — Tulis Ulang ke Target File (OVERWRITE):** Tulis ulang **seluruh** isi dokumen yang sudah direvisi ke file target:
  ```
  docs/sdlc/06_deployment/03_release_notes.md
  ```
  dengan cara **overwrite** (timpa seluruh konten file lama).

  **ATURAN WAJIB PENULISAN ULANG — DILARANG DILANGGAR:**
  - [ ] Seluruh teks dari **baris pertama hingga baris terakhir** harus ditulis ulang sepenuhnya.
  - [ ] **DILARANG** memotong, meringkas, atau menghilangkan bagian apapun dari dokumen.
  - [ ] **DILARANG** menggunakan placeholder seperti `[... konten sama seperti sebelumnya ...]` atau `[lanjutan dari bab sebelumnya]`.
  - [ ] **DILARANG** menggunakan komentar seperti `# (tidak ada perubahan)` sebagai pengganti konten asli.
  - [ ] Seluruh 19 bab (termasuk bab-bab yang tidak ada perubahan konten) **harus ditulis kembali secara lengkap**.
  - [ ] Dokumen hasil akhir harus memiliki **panjang yang sama atau lebih panjang** dari dokumen sebelumnya (tidak boleh lebih pendek karena potongan konten).

- [ ] **8.6 — Verifikasi Panjang Dokumen:** Setelah overwrite, baca kembali file hasil untuk memastikan:
  - [ ] Jumlah baris **tidak berkurang signifikan** dari dokumen asli (minimal 634 baris atau lebih).
  - [ ] Semua 19 bab hadir dan lengkap.
  - [ ] Front matter YAML menunjukkan versi `1.2`.
  - [ ] Tabel Riwayat Perubahan sudah memiliki baris untuk `v1.2`.

---

### FASE 9 — PENAMBAHAN REFERENSI BARU (JIKA ADA)

- [ ] **9.1** Jika selama proses validasi dan perbaikan kamu merujuk ke **file baru yang belum terdaftar** di Bab 19 sebagai referensi (misalnya ada file SDLC lain di `docs/sdlc/` yang ternyata relevan namun belum dicantumkan), tambahkan file tersebut ke tabel referensi di Bab 19.

- [ ] **9.2** Format penambahan referensi baru di Bab 19 harus mengikuti format tabel yang sudah ada:
  ```
  | [No] | [R-XX] | [Nama Dokumen] | [path/relatif/file] | [Versi] | [PRIMER/SEKUNDER/TERSIER] | [Peran dalam penyusunan] |
  ```
  Nomor referensi baru harus melanjutkan nomor terakhir (`R-16` → `R-17`, dst.).

- [ ] **9.3** Jika tidak ada referensi baru yang perlu ditambahkan, lewati fase ini dan catat "Tidak ada referensi baru yang ditambahkan" di baris komentar.

---

### FASE 10 — VERIFIKASI AKHIR

- [ ] **10.1** Baca ulang **seluruh** dokumen hasil revisi dari baris pertama hingga baris terakhir satu kali lagi.

- [ ] **10.2** Pastikan tidak ada **tabrakan data** antara bab yang berbeda (contoh: nilai yang disebut di Bab 5 harus sama dengan nilai yang disebut di Bab 10 jika merujuk hal yang sama).

- [ ] **10.3** Pastikan **semua link path referensi** di Bab 19 (dan di bab-bab lain yang menyebut path file) menggunakan format **path relatif** yang konsisten dari root proyek (bukan path absolut).

- [ ] **10.4** Pastikan **semua tabel** memiliki header kolom yang jelas dan pemisah `|---|` yang konsisten.

- [ ] **10.5** Pastikan **diagram Mermaid** di Bab 12.1 tidak memiliki karakter yang akan menyebabkan parse error (misalnya: karakter `&` di dalam label node — gunakan `&amp;` atau ganti dengan teks biasa).

- [ ] **10.6** Laporkan ringkasan hasil audit dalam format berikut sebagai **komentar terakhir** sebelum menutup issue ini:

```
## Laporan Audit Dokumen Release Notes

**Tanggal Audit:** [DIISI]
**Auditor:** [DIISI]
**Versi Sebelum:** v1.1
**Versi Sesudah:** v1.2

### Temuan & Koreksi:
- [x] [Deskripsi temuan dan koreksi 1]
- [x] [Deskripsi temuan dan koreksi 2]
- ... (semua temuan)

### Referensi Baru Ditambahkan:
- [Jika ada] R-17: [nama file]
- [Jika tidak ada] Tidak ada referensi baru.

### Status Akhir:
- Dokumen siap sebagai referensi Fase 07 — Maintenance: **YA / TIDAK**
- Dokumen layak sebagai basis User Manual: **YA / TIDAK**
```

---

## Catatan Tambahan untuk Implementor

> Perhatikan beberapa kekhasan dokumen Release Notes ini yang memerlukan perhatian ekstra:

1. **Ambiguitas Tanggal Rilis vs Status UAT:** Bab 2.2 mencantumkan tanggal rilis `2027-05-20` dengan status "Estimasi", sementara Bab 11.3 sudah menyatakan UAT selesai. Ini adalah inkonsistensi yang harus diselesaikan secara eksplisit — bukan hanya didiamkan.

2. **Nama Alias vs Nama Resmi:** Dokumen menggunakan nama "Bpk. Abu" dan "Bpk. Cetak" di bagian UAT, sementara Bab 17 menggunakan nama resmi "Alfatih" dan "Donsise". Pastikan konsistensi di seluruh dokumen menggunakan nama yang sama. Gunakan Project Charter (R-01) sebagai acuan nama resmi.

3. **Rollback ke Tag yang Tidak Mungkin Ada:** Perintah `git checkout v0.9.0-stable` di Bab 9.3.2 tidak masuk akal untuk rilis perdana. Ini memerlukan klarifikasi atau penggantian prosedur.

4. **Placeholder Kontak Dukungan:** Nomor WhatsApp dan email di Bab 16.1 kemungkinan besar adalah placeholder. Ini berpotensi menyebabkan masalah operasional jika dokumen ini digunakan sebagai acuan langsung tanpa diperbarui.

5. **Hypercare Period Tidak Terdefinisi:** RSK-06 menyebut "masa Hypercare" namun tidak ada definisi durasi dan ruang lingkupnya di manapun dalam dokumen. Ini adalah gap yang perlu diisi.

6. **Verifikasi Skor Risiko Matematis:** Semua 8 skor risiko sudah tampak benar (Prob × Dampak), namun tetap perlu diverifikasi ulang secara formal.

7. **Penomoran SRS Restrukturisasi:** Bab 6.1 menyebutkan restrukturisasi SRS-F-039 dan SRS-F-040. Pastikan urutan ini sudah selaras dengan urutan di SRS versi final (R-02).

---

## Definisi Selesai (Definition of Done)

Issue ini dinyatakan **SELESAI** apabila semua kondisi berikut terpenuhi:

- [ ] Seluruh 16 file referensi (R-01 s.d R-16) telah dibaca dan dikomparasi.
- [ ] Seluruh checklist di Fase 0 s.d Fase 10 telah ditandai `[x]`.
- [ ] File `docs/sdlc/06_deployment/03_release_notes.md` telah di-overwrite dengan versi `v1.2`.
- [ ] Dokumen hasil revisi tidak memiliki konten yang terpotong atau diringkas.
- [ ] Semua inkonsistensi data antar bab telah diselesaikan.
- [ ] Semua placeholder / data kosong telah diisi atau ditandai secara eksplisit.
- [ ] Semua data yang tidak relevan dengan Release Notes telah dihapus atau direlokasi.
- [ ] Laporan audit telah ditulis sesuai format yang diminta.
- [ ] Versi dokumen di front matter menunjukkan `1.2`.
- [ ] Riwayat Perubahan Dokumen memuat entri baru untuk `v1.2`.

---