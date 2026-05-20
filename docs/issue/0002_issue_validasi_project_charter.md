---
issue_id   : 0002
judul      : Validasi, Analisis, dan Penyempurnaan Dokumen Project Charter
target_file: docs/sdlc/01_planning/01_project_charter.md
fase_sdlc  : 01 — Planning
prioritas  : Tinggi
status     : Open
dibuat_oleh: Senior Project Manager / Lead Business Analyst
tanggal    : 2026-05-21
---

# Validasi, Analisis, dan Penyempurnaan Dokumen Project Charter

## Deskripsi Singkat

Issue ini berisi instruksi low-level yang harus diikuti langkah demi langkah untuk memeriksa, menganalisis, memvalidasi, dan menyempurnakan dokumen **Project Charter** (`docs/sdlc/01_planning/01_project_charter.md`) agar memenuhi standar kualitas industri dan siap dijadikan acuan utama fase SDLC berikutnya.

---

## Persona yang Harus Diambil

Sebelum memulai pekerjaan apa pun, ambillah dan terapkan persona berikut secara penuh:

> **Kamu adalah seorang Principal Business Analyst & Senior Technical Project Manager** dengan pengalaman lebih dari 15 tahun dalam menyusun, mengaudit, dan mengesahkan dokumen perencanaan proyek perangkat lunak skala UMKM hingga enterprise. Kamu memiliki keahlian mendalam dalam metodologi SDLC (Waterfall, Agile, Hybrid), standar dokumentasi IEEE 830 / PMBoK, serta pemahaman domain bisnis retail, percetakan, dan sistem informasi manajemen. Kamu dikenal sangat teliti, tidak mentoleransi ambiguitas, dan selalu memastikan setiap dokumen yang kamu hasilkan dapat dipahami oleh junior programmer maupun AI model lain tanpa pertanyaan lanjutan yang menghambat pekerjaan.

---

## Lokasi File yang Terlibat

| Peran | Path |
|---|---|
| **Target File (dokumen utama)** | `docs/sdlc/01_planning/01_project_charter.md` |
| **Referensi Primer** | `docs/sdlc/narasi.txt` |
| **Direktori Referensi SDLC** | `docs/sdlc/` |

---

## Tahapan Implementasi (Checklist)

Ikuti setiap langkah secara berurutan. Jangan melompati langkah. Tandai `[x]` setiap item setelah selesai dikerjakan.

---

### TAHAP 0 — Persiapan & Pembacaan File

- [ ] **0.1** Baca seluruh isi file `docs/sdlc/01_planning/01_project_charter.md` dari baris pertama hingga baris terakhir tanpa melewati satu baris pun. Catat versi dokumen saat ini (field `versi` pada frontmatter).
- [ ] **0.2** Baca seluruh isi file `docs/sdlc/narasi.txt` dari baris pertama hingga baris terakhir tanpa melewati satu baris pun.
- [ ] **0.3** Catat semua file referensi yang tercantum di dalam bagian **Referensi Dokumen** (Seksi 15) pada `01_project_charter.md`. Pastikan kamu sudah membaca semua file referensi tersebut sebelum melanjutkan ke tahap berikutnya.
- [ ] **0.4** Scan seluruh direktori `docs/sdlc/` untuk memastikan tidak ada file referensi tambahan yang belum tercantum di dalam dokumen utama.

---

### TAHAP 1 — Validasi Kelengkapan Data dari Referensi

**Tujuan**: Memastikan semua informasi penting dari `narasi.txt` telah tercermin di dalam Project Charter.

- [ ] **1.1** Bandingkan setiap poin pada `narasi.txt` dengan konten di `01_project_charter.md`. Buat daftar internal (mental atau scratch) poin mana yang sudah ada dan poin mana yang belum tercantum di dokumen utama.
- [ ] **1.2** Periksa apakah informasi berikut dari `narasi.txt` sudah termuat di dokumen utama:
  - [ ] 1.2.a — Lima kategori produk & layanan usaha (baris 3–18 narasi.txt)
  - [ ] 1.2.b — Dua jenis pinjaman modal: tanpa bunga (kerabat) dan berbunga bank BRI & Mandiri (baris 22–24)
  - [ ] 1.2.c — Kondisi burnout / single-fighter pemilik (baris 28)
  - [ ] 1.2.d — Struktur organisasi 7 posisi staf (baris 34–41)
  - [ ] 1.2.e — Alur kerja manual Excel per divisi (baris 47–70)
  - [ ] 1.2.f — Semua 20+ poin harapan aplikasi (baris 74–98), termasuk: kebijakan harga, penggajian otomatis, sistem poin, rekonsiliasi kas, analisis laba/rugi per divisi, audit trail, job tracking, limbah produksi, arsip desain, RBAC, supplier & hutang usaha, pembatalan & retur, CRM, stock opname, manajemen aset, HPP & BOM dimensi desimal, manajemen satuan barang, multi-branch ready, mandat inovasi.
  - [ ] 1.2.g — Spesifikasi teknis: Python 3.14.2+, Functional Programming, MySQL, library, OS (baris 102–106)
  - [ ] 1.2.h — Susunan tim pengembang AI (baris 108–115)
- [ ] **1.3** Jika ditemukan informasi dari `narasi.txt` yang **belum** tercantum di dokumen utama dan informasi tersebut relevan untuk level Project Charter, tandai sebagai **[GAP]** dan siapkan konten pengisinya.

---

### TAHAP 2 — Validasi Relevansi & Fokus Dokumen

**Tujuan**: Memastikan dokumen hanya memuat informasi yang memang seharusnya ada di Project Charter, bukan detail level SRS atau SDD.

- [ ] **2.1** Periksa apakah ada konten di `01_project_charter.md` yang terlalu detail dan seharusnya menjadi bagian dari dokumen SRS (Fase 2) atau SDD (Fase 3). Contoh: detail skema tabel database, pseudocode, atau spesifikasi UI/UX.
- [ ] **2.2** Periksa apakah ada konten yang duplikat atau redundan di antara seksi-seksi dalam dokumen utama.
- [ ] **2.3** Pastikan level abstraksi setiap seksi sudah sesuai dengan standar Project Charter, yaitu: **tingkat tinggi (high-level)**, bukan implementasi detail.
- [ ] **2.4** Tandai konten yang tidak relevan sebagai **[OUT-OF-SCOPE]** untuk dipertimbangkan dihapus atau dipindahkan ke dokumen yang lebih tepat.

---

### TAHAP 3 — Validasi Struktur Dokumen

**Tujuan**: Memastikan struktur dokumen sesuai standar industri Project Charter yang profesional.

- [ ] **3.1** Verifikasi keberadaan dan kelengkapan seksi-seksi wajib berikut dalam dokumen utama:
  - [ ] 3.1.a — Frontmatter / metadata dokumen (nama proyek, versi, tanggal, status, penyusun)
  - [ ] 3.1.b — Riwayat perubahan dokumen (document history / changelog)
  - [ ] 3.1.c — Informasi umum proyek (nama, deskripsi, sponsor, PM, tanggal mulai & selesai)
  - [ ] 3.1.d — Latar belakang dan justifikasi proyek (current state, problem statement, dampak)
  - [ ] 3.1.e — Tujuan proyek (umum dan SMART goals)
  - [ ] 3.1.f — Ruang lingkup (in-scope & out-of-scope)
  - [ ] 3.1.g — Deliverables per fase SDLC
  - [ ] 3.1.h — Daftar stakeholder dan RACI Matrix
  - [ ] 3.1.i — Tim proyek dan struktur organisasi
  - [ ] 3.1.j — Kebutuhan bisnis tingkat tinggi (fungsional & non-fungsional)
  - [ ] 3.1.k — Asumsi dan batasan
  - [ ] 3.1.l — Identifikasi risiko awal (initial risks)
  - [ ] 3.1.m — Milestone dan jadwal tingkat tinggi
  - [ ] 3.1.n — Estimasi anggaran tingkat tinggi
  - [ ] 3.1.o — Kriteria keberhasilan proyek
  - [ ] 3.1.p — Persetujuan dan otorisasi
  - [ ] 3.1.q — Referensi dokumen
  - [ ] 3.1.r — Glosarium istilah domain
- [ ] **3.2** Periksa apakah ada seksi penting standar Project Charter yang **tidak ada** di dokumen saat ini. Seksi tambahan yang umum di industri namun perlu dipertimbangkan:
  - [ ] 3.2.a — **Manfaat Bisnis yang Terukur** (measurable business benefits): apakah sudah tersisip di dalam tujuan atau perlu seksi tersendiri?
  - [ ] 3.2.b — **Dependensi Proyek** (project dependencies): apakah ada ketergantungan terhadap pihak, sistem, atau infrastruktur eksternal yang perlu didokumentasikan?
  - [ ] 3.2.c — **Pendekatan / Metodologi Proyek** (project approach & methodology): apakah sudah disebutkan metodologi SDLC yang digunakan (Waterfall, Agile, atau Hybrid)?
- [ ] **3.3** Verifikasi bahwa setiap seksi memiliki judul yang jelas, hierarki heading yang konsisten (H1 > H2 > H3), dan nomor urut yang benar.
- [ ] **3.4** Verifikasi bahwa tabel, daftar, dan format markdown digunakan secara konsisten dan dapat dirender dengan baik.

---

### TAHAP 4 — Validasi Kesiapan sebagai Acuan SDLC Berikutnya

**Tujuan**: Memastikan dokumen cukup kuat sebagai input utama bagi dokumen SRS (Fase 2) dan dokumen SDLC fase berikutnya.

- [ ] **4.1** Periksa apakah setiap modul fungsional (M.1 s.d. M.9) sudah cukup dideskripsikan di level high-level sehingga penyusun SRS dapat menguraikannya lebih detail tanpa harus bertanya ulang ke pemilik proyek.
- [ ] **4.2** Periksa apakah kebutuhan non-fungsional (N-2.1 s.d. N-2.6) sudah cukup jelas untuk dijadikan batasan teknis di dokumen SRS dan SDD.
- [ ] **4.3** Periksa apakah stakeholder dan RACI Matrix sudah cukup jelas untuk mengidentifikasi siapa yang harus dikonsultasi dalam fase analisis kebutuhan (SRS).
- [ ] **4.4** Periksa apakah milestone dan jadwal tingkat tinggi sudah cukup memberikan konteks bagi tim pengembang untuk merencanakan sprint atau iterasi pada fase implementasi.
- [ ] **4.5** Periksa apakah setiap kebutuhan bisnis high-level sudah dapat dipetakan ke minimal satu fitur atau modul dalam ruang lingkup (in-scope). Jika ada kebutuhan bisnis yang tidak punya padanan di ruang lingkup, tandai sebagai **[UNMAPPED]**.

---

### TAHAP 5 — Validasi Bahasa & Keterbacaan

**Tujuan**: Memastikan dokumen menggunakan Bahasa Indonesia yang natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau AI model lain.

- [ ] **5.1** Baca ulang seluruh dokumen dari atas ke bawah dengan perspektif sebagai pembaca baru yang belum mengenal proyek AbuCom.
- [ ] **5.2** Periksa apakah ada kalimat yang ambigu, bermakna ganda, atau dapat disalahartikan. Tandai dan perbaiki.
- [ ] **5.3** Periksa apakah ada istilah teknis (bahasa Inggris atau jargon industri) yang digunakan tanpa penjelasan, sementara istilah tersebut **tidak ada** di bagian Glosarium. Jika ada, tambahkan ke Glosarium.
- [ ] **5.4** Periksa apakah ada akronim atau singkatan yang muncul pertama kali tanpa kepanjangan/penjelasannya. Perbaiki dengan menyertakan kepanjangan di kemunculan pertama.
- [ ] **5.5** Pastikan semua kalimat aktif, ringkas, dan tidak bertele-tele. Kalimat yang terlalu panjang harus dipecah menjadi lebih pendek.
- [ ] **5.6** Periksa konsistensi penulisan nama proyek, nama modul, nama teknologi, dan nama persona di seluruh dokumen. Contoh: pastikan "AbuCom" tidak ditulis "Abucom" atau "abucom" di tempat lain.

---

### TAHAP 6 — Validasi Kualitas & Kelengkapan Akhir

**Tujuan**: Memastikan tidak ada data yang kosong, placeholder, atau field yang perlu diisi manual yang belum terisi.

- [ ] **6.1** Cari semua teks yang mengandung pola berikut di dalam dokumen:
  - `[BELUM DITENTUKAN]`
  - `[ISI MANUAL]`
  - `**[ISI MANUAL]**`
  - `TBD`, `TODO`, atau placeholder serupa
- [ ] **6.2** Untuk setiap placeholder yang ditemukan, evaluasi apakah datanya **bisa diisi** berdasarkan informasi yang sudah tersedia di `narasi.txt` atau konteks proyek yang ada. Jika bisa, isi dengan data yang relean dan realistis.
- [ ] **6.3** Untuk placeholder yang **tidak dapat diisi** karena membutuhkan keputusan pemilik usaha secara langsung (misalnya: tanda tangan persetujuan, anggaran yang belum diputuskan), biarkan dengan catatan penjelasan yang lebih informatif daripada sekadar `[ISI MANUAL]`. Ganti dengan keterangan seperti: `*(Diisi oleh Pemilik Usaha setelah persetujuan dokumen ini)*`.
- [ ] **6.4** Khusus untuk **Seksi 12 (Estimasi Anggaran)**: Isi tabel komponen biaya dengan estimasi yang masuk akal dan realistis berdasarkan konteks UMKM percetakan skala kecil-menengah di Indonesia. Cantumkan asumsi estimasi secara eksplisit dalam catatan di bawah tabel. Gunakan satuan Rupiah (Rp).
- [ ] **6.5** Khusus untuk **Seksi 1.4 (Manajer Proyek)**: Berdasarkan konteks dokumen di mana pemilik usaha bertindak sebagai Junior Programmer dan pengambil keputusan bisnis, isi field ini dengan data yang konsisten dengan Seksi 6 (Stakeholder) dan Seksi 7 (Tim Proyek).
- [ ] **6.6** Periksa apakah semua tautan internal (format `file: docs/...`) sudah benar dan mengacu ke file yang benar-benar ada.

---

### TAHAP 7 — Pengecekan Standar Tambahan Spesifik Project Charter

**Tujuan**: Memastikan aspek-aspek penting khas dokumen Project Charter yang sering terlewat sudah terpenuhi.

- [ ] **7.1** **Konsistensi SMART Goals dengan Ruang Lingkup**: Verifikasi bahwa setiap SMART Goal (S.1 s.d. S.5) di Seksi 3.2 memiliki modul atau fitur yang mendukungnya di Seksi 4.1. Jika ada SMART Goal yang tidak didukung oleh fitur apapun, tambahkan fitur yang relevan atau revisi SMART Goal-nya.
- [ ] **7.2** **Konsistensi Risiko dengan Mitigasi**: Periksa apakah setiap risiko di Seksi 10 memiliki rencana mitigasi yang konkret dan dapat dieksekusi. Mitigasi yang terlalu umum harus diperjelas.
- [ ] **7.3** **Konsistensi Milestone dengan Deliverables**: Pastikan setiap milestone di Seksi 11 memiliki deliverable yang jelas yang tercantum di Seksi 5.2. Jika ada milestone tanpa deliverable yang terdefinisi, tambahkan.
- [ ] **7.4** **Kelengkapan Out-of-Scope**: Pastikan batasan Out-of-Scope di Seksi 4.2 cukup jelas untuk mencegah scope creep. Jika ada area yang berpotensi ambigu antara in-scope dan out-of-scope, tambahkan klarifikasinya.
- [ ] **7.5** **Metodologi Pengembangan**: Periksa apakah dokumen sudah menyebutkan secara eksplisit metodologi SDLC yang digunakan (Waterfall, Agile, atau Hybrid). Jika belum, tambahkan di seksi yang paling relevan (misalnya di Seksi 1 atau sebagai subseksi baru).
- [ ] **7.6** **Kriteria Penerimaan Dokumen (Definition of Done)**: Pastikan Seksi 13 (Kriteria Keberhasilan) mendefinisikan kriteria yang dapat diverifikasi secara objektif, bukan hanya pernyataan kualitatif. Setiap kriteria harus memiliki indikator yang terukur (angka, persentase, atau kondisi biner Ya/Tidak).

---

### TAHAP 8 — Penulisan Ulang Dokumen Final (Overwrite)

**Tujuan**: Menuangkan seluruh hasil validasi dan penyempurnaan ke file target secara lengkap.

> **PERINGATAN KRITIS — BACA SEBELUM EKSEKUSI:**
> Langkah ini akan menimpa (overwrite) seluruh isi file `docs/sdlc/01_planning/01_project_charter.md`. Pastikan semua tahap validasi (Tahap 1 s.d. 7) sudah selesai sebelum menjalankan langkah ini.

- [ ] **8.1** Susun dokumen final yang telah disempurnakan di dalam memori/buffer kerja kamu. Dokumen ini adalah gabungan dari dokumen asli yang telah diperbaiki berdasarkan seluruh temuan di Tahap 1 s.d. 7.
- [ ] **8.2** Pastikan perubahan versi dokumen diterapkan di **dua lokasi** berikut:
  - [ ] 8.2.a — Field `versi` pada frontmatter YAML (contoh: dari `1.0` menjadi `1.1`)
  - [ ] 8.2.b — Field `tanggal` pada frontmatter diperbarui ke tanggal hari ini (format `YYYY-MM-DD`)
  - [ ] 8.2.c — Seksi **Riwayat Perubahan Dokumen**: tambahkan baris baru yang mencatat versi baru, tanggal hari ini, ringkasan perubahan, dan nama persona pelaksana issue ini.
- [ ] **8.3** Sebelum menulis, verifikasi bahwa dokumen final yang sudah disusun memuat **semua seksi** dari dokumen asli tanpa ada yang dihilangkan atau diringkas. Tidak boleh ada seksi yang dipotong, diringkas menjadi `[...]`, atau dihapus kecuali memang terbukti tidak relevan berdasarkan Tahap 2.
- [ ] **8.4** Tulis ulang seluruh isi dokumen final ke file `docs/sdlc/01_planning/01_project_charter.md` dengan cara **overwrite penuh** (timpa dari baris pertama hingga baris terakhir).
- [ ] **8.5** Verifikasi hasil penulisan dengan membaca kembali file yang baru ditulis. Pastikan:
  - [ ] 8.5.a — Versi dokumen sudah berubah (misalnya menjadi `v1.1`)
  - [ ] 8.5.b — Riwayat perubahan sudah diperbarui
  - [ ] 8.5.c — Semua placeholder `[ISI MANUAL]` yang bisa diisi sudah terisi
  - [ ] 8.5.d — Tidak ada konten yang terpotong atau hilang di bagian akhir file
  - [ ] 8.5.e — Format markdown dapat dirender dengan benar (heading, tabel, list, bold, italic konsisten)

---

### TAHAP 9 — Pembaruan Referensi Dokumen

**Tujuan**: Memastikan semua file yang dijadikan referensi dalam proses validasi ini tercatat di bagian Referensi Dokumen.

- [ ] **9.1** Periksa bagian **Referensi Dokumen (Seksi 15)** pada dokumen yang baru ditulis.
- [ ] **9.2** Jika dalam proses validasi kamu menggunakan atau menemukan file referensi tambahan selain yang sudah tercantum, tambahkan file tersebut ke tabel Referensi Dokumen di baris paling bawah tabel.
- [ ] **9.3** Format penambahan referensi mengikuti format tabel yang sudah ada:
  ```
  | [nomor urut] | `nama_file.ext` | [path/ke/file](file: path/ke/file) | Keterangan singkat isi dan relevansi file ini |
  ```
- [ ] **9.4** Pastikan seluruh path referensi menggunakan path relatif terhadap root proyek (bukan path absolut sistem operasi).

---

## Kriteria Selesai (Definition of Done)

Issue ini dinyatakan **selesai** apabila semua kondisi berikut terpenuhi:

- [ ] Semua checklist dari Tahap 0 hingga Tahap 9 sudah ditandai `[x]`.
- [ ] File `docs/sdlc/01_planning/01_project_charter.md` sudah berhasil ditimpa dengan konten yang telah disempurnakan.
- [ ] Versi dokumen sudah berubah dari `v1.0` menjadi `v1.1` (atau lebih tinggi jika diperlukan).
- [ ] Tidak ada lagi placeholder `[ISI MANUAL]` atau `[BELUM DITENTUKAN]` yang dapat diisi secara logis.
- [ ] Tidak ada seksi dokumen yang hilang, terpotong, atau diringkas.
- [ ] Dokumen dapat dibaca dari awal hingga akhir oleh junior programmer atau AI model lain tanpa perlu mengajukan pertanyaan klarifikasi yang menghambat pekerjaan fase SDLC berikutnya.

---

## Catatan Penting untuk Pelaksana

1. **Jangan asumsikan data yang tidak ada** — jika kamu tidak menemukan informasi yang diperlukan di `narasi.txt` maupun di dokumen utama, jangan mengarang data. Tandai dengan keterangan `*(Memerlukan konfirmasi dari Pemilik Usaha)*`.
2. **Jangan mengubah substansi bisnis** — kamu boleh memperbaiki bahasa, melengkapi data yang kosong, dan menambah seksi yang kurang, tetapi **dilarang mengubah keputusan bisnis** yang sudah ditetapkan oleh pemilik (misalnya: paradigma Functional Programming, stack teknologi Python + MySQL, jangka waktu 12 bulan).
3. **Jangan memotong atau meringkas** — penulisan ulang di Tahap 8 harus menghasilkan dokumen yang **sama panjang atau lebih panjang** dari dokumen asli, karena proses ini bersifat penyempurnaan dan pengayaan, bukan pemangkasan.
4. **Gunakan format markdown yang konsisten** — seluruh heading, tabel, list, bold, italic, dan code block harus mengikuti format yang sudah ada di dokumen asli.
5. **Baca referensi sebelum menulis** — jangan menulis ulang dokumen sebelum kamu benar-benar selesai membaca semua file referensi yang tercantum di Tahap 0.

---

## Referensi Issue Terkait

| Issue ID | Judul | Keterangan |
|---|---|---|
| `0001` | Pembuatan Dokumen Project Charter | Issue pembuatan pertama dokumen yang menjadi target validasi issue ini. |
