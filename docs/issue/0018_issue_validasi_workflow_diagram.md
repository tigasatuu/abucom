---
judul         : Validasi, Audit & Perbaikan Dokumen Workflow Diagram
target_file   : docs/sdlc/02_analysis/04_workflow_diagram.md
prioritas     : Tinggi
status        : Open
dibuat_oleh   : Senior Business Analyst & SDLC Document Architect
tanggal       : 2026-05-23
---

# Validasi, Audit & Perbaikan Dokumen Workflow Diagram

## Ringkasan Issue

Lakukan pemeriksaan, analisis, dan validasi menyeluruh terhadap dokumen **Workflow Diagram** AbuCom (`docs/sdlc/02_analysis/04_workflow_diagram.md`). Dokumen ini merupakan artefak penutup Fase 02 Analysis yang menjadi fondasi visual utama bagi seluruh dokumen Fase 03 Design (SDD, ERD, Sequence Diagram, Test Plan). Kualitasnya harus dijamin benar-benar solid, lengkap, bebas ambiguitas, dan konsisten dengan seluruh dokumen referensi sebelumnya. Seluruh hasil revisi dituangkan kembali ke file yang sama dengan cara **overwrite** penuh tanpa pemotongan satu baris pun.

---

## Persona Pelaksana

> **Kamu berperan sebagai: Senior Business Process Analyst & Workflow Modeling Specialist**
>
> Kamu adalah seorang analis proses bisnis senior berpengalaman 10+ tahun dalam bidang pemodelan workflow sistem informasi untuk UMKM dan enterprise. Kamu mahir dalam notasi Mermaid.js, standar BPMN, pemodelan alur kerja As-Is/To-Be, analisis cross-module dependency, serta validasi konsistensi dokumen SDLC. Kamu memiliki standar dokumen industri yang sangat tinggi, tidak mentoleransi ambiguitas, data kosong, atau inkonsistensi sekecil apa pun. Kamu bekerja dengan teliti, sistematis, dan mengacu pada sumber kebenaran primer (file referensi), bukan asumsi.

---

## Informasi Konteks

| Atribut             | Nilai                                                                      |
|---------------------|----------------------------------------------------------------------------|
| **Dokumen Utama**   | Workflow Diagram                                                            |
| **Target File**     | `docs/sdlc/02_analysis/04_workflow_diagram.md`                             |
| **Versi Saat Ini**  | v1.0                                                                       |
| **Versi Target**    | v1.1 (setelah direvisi)                                                    |
| **Lokasi Referensi**| `docs/sdlc/` (seluruh subdirektori)                                        |

---

## Daftar File Referensi yang Wajib Dibaca

Baca **semua** file berikut secara penuh sebelum memulai validasi. Jangan lewatkan satu pun.

| No. | File Referensi                                                                | Keterangan Singkat                                                       |
|-----|-------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| 1   | `docs/sdlc/01_planning/01_project_charter.md`                                 | Definisi modul fungsional M.1–M.10 dan cakupan organisasi proyek         |
| 2   | `docs/sdlc/01_planning/03_stakeholder_register.md`                            | Profil 19 stakeholder, peran aktor, dan matriks hak akses dasar          |
| 3   | `docs/sdlc/01_planning/04_tech_stack_decision.md`                             | Batasan mandatori: Python, MySQL, bcrypt, JWT, pustaka `decimal`         |
| 4   | `docs/sdlc/01_planning/05_innovation_proposal.md`                             | 43 inovasi fungsional yang harus tercermin di alur kerja To-Be           |
| 5   | `docs/sdlc/02_analysis/01_business_requirements.md`                           | BRD v1.1 — 40+ kebutuhan bisnis, aturan numerik eksplisit, matriks RBAC |
| 6   | `docs/sdlc/02_analysis/02_software_requirements.md`                           | SRS v1.1 — spesifikasi teknis input/proses/output, non-fungsional        |
| 7   | `docs/sdlc/02_analysis/03_use_case_diagram.md`                                | UCD v1.1 — 44 use case naratif dengan Main/Alternative/Exception Flow    |
| 8   | `docs/sdlc/narasi.txt`                                                        | Narasi asli pemilik usaha — sumber kebenaran alur bisnis manual As-Is    |

---

## Checklist Tugas Implementasi

Ikuti setiap langkah secara **berurutan**. Tandai `[x]` setiap tugas yang sudah selesai. Jangan melompati langkah.

---

### FASE 0 — Persiapan & Pembacaan File

- [ ] **[BACA-0.1]** Baca seluruh isi file target utama dari baris pertama hingga terakhir:
  ```
  docs/sdlc/02_analysis/04_workflow_diagram.md
  ```
  Catat dalam memori: jumlah total modul, jumlah diagram workflow, jumlah use case yang terdaftar di matriks traceability, dan daftar file referensi yang disebutkan di Bagian 9 dokumen.

- [ ] **[BACA-0.2]** Baca seluruh isi 8 file referensi yang tercantum di tabel "Daftar File Referensi" di atas, satu per satu. Urutan: file no. 1 → 8.

- [ ] **[BACA-0.3]** Setelah membaca semua referensi, buat catatan internal (dalam memori kerja) tentang:
  - Total Use Case yang ada di UCD (seharusnya 44 UC-001 s.d UC-044)
  - Total Business Requirements di BRD (BR-F-01 s.d BR-F-40, ditambah persyaratan tambahan)
  - Total SRS requirement (SRS-F-001 s.d SRS-F-040, ditambah SRS-F-ADD-xx)
  - Nama-nama 10 modul (M.1 s.d M.10) beserta tanggung jawab fungsionalnya
  - Nama-nama inovasi di Innovation Proposal yang relevan terhadap workflow diagram
  - Aturan bisnis numerik eksplisit dari BRD (nominal batas, formula, threshold)

---

### FASE 1 — Validasi Kelengkapan & Cakupan Referensi

> **Tujuan**: Pastikan tidak ada data penting dari file referensi yang terlewat atau tidak tercermin dalam dokumen utama.

- [ ] **[VAL-1.1] Validasi Cakupan Use Case (UC Coverage)**
  - Periksa matriks traceability (Bagian 6 dokumen utama).
  - Pastikan seluruh 44 use case (UC-001 s.d UC-044) terpetakan ke minimal satu ID Workflow.
  - Jika ada UC yang belum terpetakan: tambahkan workflow baru atau perbarui matriks traceability yang ada.
  - Catat semua UC yang belum terpetakan: `[ ] UC-xxx belum memiliki workflow diagram`.

- [ ] **[VAL-1.2] Validasi Cakupan Business Requirement (BR Coverage)**
  - Periksa kolom "BRD Terkait" di matriks traceability.
  - Pastikan seluruh BR-F-01 s.d BR-F-40 terpetakan ke minimal satu workflow.
  - Jika ada BR yang belum terpetakan: perbarui matriks dan/atau tambahkan narasi prosedural yang mencerminkan aturan bisnis tersebut.

- [ ] **[VAL-1.3] Validasi Cakupan SRS Requirement (SRS Coverage)**
  - Periksa kolom "SRS Terkait" di matriks traceability.
  - Pastikan seluruh SRS-F-001 s.d SRS-F-040 dan SRS-F-ADD-xx terpetakan.
  - Jika ada SRS yang belum terpetakan: perbarui matriks.

- [ ] **[VAL-1.4] Validasi Cakupan Inovasi (Innovation Proposal Coverage)**
  - Buka `docs/sdlc/01_planning/05_innovation_proposal.md` kembali.
  - Periksa satu per satu apakah setiap inovasi fungsional yang relevan sudah tercermin dalam alur To-Be yang ada.
  - Inovasi yang relevan secara langsung (bukan hanya konseptual) namun belum ada diagramnya wajib ditambahkan atau dicatat ketidakhadirannya dalam narasi prosedural workflow terkait.

- [ ] **[VAL-1.5] Validasi Alur As-Is vs Narasi Pemilik**
  - Buka `docs/sdlc/narasi.txt` kembali.
  - Periksa apakah seluruh proses manual yang disebutkan pemilik dalam narasi tercermin di Bagian 3 (Workflow As-Is).
  - Pastikan pain point analisis pada setiap As-Is workflow akurat dan tidak ada yang terlewat berdasarkan narasi pemilik.

- [ ] **[VAL-1.6] Validasi Aktor & Peran (Stakeholder Register)**
  - Buka `docs/sdlc/01_planning/03_stakeholder_register.md` kembali.
  - Periksa apakah seluruh aktor yang bertindak dalam diagram workflow (Pemilik, Kasir, Desainer, Produksi Cetak, Gudang, Teknisi, Pramuniaga, Kepala Percetakan) sudah sesuai dengan profil stakeholder yang terdaftar.
  - Pastikan tidak ada aktor asing atau tidak konsisten yang muncul dalam diagram.

---

### FASE 2 — Validasi Fokus & Relevansi Konten

> **Tujuan**: Pastikan dokumen hanya memuat konten yang memang menjadi tanggung jawab dokumen Workflow Diagram, tidak memuat konten yang seharusnya ada di dokumen lain.

- [ ] **[VAL-2.1] Validasi Fokus Konten Workflow Diagram**
  - Periksa setiap seksi dokumen apakah ada konten yang seharusnya berada di dokumen lain:
    - Spesifikasi teknis database schema → seharusnya di ERD, **bukan** di sini.
    - Detail API endpoint / HTTP method → seharusnya di SDD, **bukan** di sini.
    - Test case skenario detail → seharusnya di Test Plan, **bukan** di sini.
    - Persyaratan non-fungsional (performa, keamanan infrastruktur) yang tidak terkait dengan alur kerja → seharusnya di SRS, **bukan** di sini.
  - Jika ditemukan konten tidak relevan: hapus atau pindahkan ke catatan di footnote saja tanpa membuatnya jadi bagian utama.

- [ ] **[VAL-2.2] Validasi Notasi Diagram yang Konsisten**
  - Periksa seluruh diagram Mermaid.js dalam dokumen.
  - Pastikan setiap diagram menggunakan notasi yang sesuai dengan legenda di Bagian 1.6:
    - `([Teks])` untuk Start/End Terminal (warna hijau gelap `#1b5e20`)
    - `[Teks]` untuk Process Node (warna slate `#37474f`)
    - `{Teks}` untuk Decision Node (warna oranye `#e65100`)
    - `[[Teks]]` untuk Subprocess/Panggilan ke workflow lain (warna ungu `#4a148c`)
    - `([Teks])` untuk Exception Node (warna merah `#b71c1c`)
  - Periksa warna aktor (swimlane coloring) sesuai legenda peran di Bagian 1.6:
    - Pemilik Toko: `#1b5e20`
    - Kasir: `#0d47a1`
    - Desainer: `#004d40`
    - Produksi Cetak: `#4a148c`
    - Gudang: `#e65100`
  - Tandai setiap ketidakkonsistenan notasi yang ditemukan dan perbaiki.

- [ ] **[VAL-2.3] Validasi Kelengkapan Subprocess Reference**
  - Setiap node `[[...]]` (subprocess call) dalam satu diagram harus merujuk ke ID workflow yang valid dan terdaftar.
  - Contoh: jika ada `[[Panggilan Subprocess - WF-M2-01]]`, pastikan diagram WF-M2-01 benar-benar ada dan ID-nya konsisten.
  - Buat daftar semua subprocess reference yang ada dan cocokkan dengan ID workflow yang tersedia.
  - Jika ada subprocess yang dirujuk namun diagramnya tidak ada: tambahkan diagramnya atau perbaiki referensinya.

- [ ] **[VAL-2.4] Validasi Referensi Kode Error**
  - Setiap kode error yang disebutkan dalam narasi prosedural atau diagram (misal `ERR-AUTH-001`) harus terdaftar di Bagian 7.2 (Daftar Exception Flow).
  - Setiap kode error di Bagian 7.2 harus disebutkan juga dalam diagram atau narasi workflow terkait.
  - Periksa konsistensi dua arah ini. Perbaiki jika ada yang tidak konsisten.

---

### FASE 3 — Validasi Standar Struktur Dokumen

> **Tujuan**: Pastikan dokumen memenuhi standar dokumen analisis proses bisnis industri yang sesungguhnya.

- [ ] **[VAL-3.1] Validasi Header & Metadata Dokumen**
  - Periksa blok YAML header (baris 1–8): apakah semua field terisi lengkap dan akurat?
    - `dokumen`, `proyek`, `versi`, `tanggal`, `status`, `penyusun` harus ada dan terisi.
  - Periksa tabel Riwayat Perubahan Dokumen: apakah kolom `Versi | Tanggal | Perubahan | Oleh` terisi lengkap?

- [ ] **[VAL-3.2] Validasi Kelengkapan Bagian Dokumen**
  - Periksa apakah semua bagian berikut ada dan terisi dengan konten substantif (bukan placeholder kosong):
    - [ ] Bagian 1: Informasi Dokumen (1.1 Tujuan, 1.2 Cakupan, 1.3 Posisi SDLC, 1.4 Hubungan Dokumen, 1.5 Audiens, 1.6 Notasi)
    - [ ] Bagian 2: Ringkasan Alur Kerja Makro (WF-OVERVIEW-01, WF-REL-01)
    - [ ] Bagian 3: Workflow As-Is (minimal 6 workflow sesuai 6 divisi bisnis)
    - [ ] Bagian 4: Workflow To-Be per Modul (M.1 s.d M.10, seluruh sub-workflow)
    - [ ] Bagian 5: Workflow Cross-Module (minimal 3 workflow lintas modul)
    - [ ] Bagian 6: Matriks Traceability (semua workflow terpetakan ke UC, BR, SRS)
    - [ ] Bagian 7: Penanganan Exception (Decision Point dan Exception Flow)
    - [ ] Bagian 8: Glosarium Istilah
    - [ ] Bagian 9: Referensi Dokumen

- [ ] **[VAL-3.3] Validasi Narasi Prosedural Setiap Workflow**
  - Setiap diagram Mermaid.js **wajib** diikuti oleh **Narasi Prosedural** berbentuk daftar bernomor.
  - Narasi prosedural harus menjelaskan langkah demi langkah alur yang digambarkan diagram.
  - Narasi tidak boleh mengulang isi diagram kata per kata, melainkan menjelaskan konteks bisnis, kondisi, dan keputusan yang terjadi.
  - Periksa setiap diagram: apakah sudah ada narasi prosedural? Jika belum, tambahkan.

- [ ] **[VAL-3.4] Validasi Derivasi (Traceability Link) Setiap Workflow**
  - Setiap diagram To-Be **wajib** memiliki baris `* **Derivasi**: UC-xxx, BR-F-xx, SRS-F-xxx.` tepat di atas blok kode diagram.
  - Periksa setiap workflow: apakah baris derivasi sudah ada dan ID-nya akurat?
  - Jika derivasi tidak ada atau salah: tambahkan atau perbaiki.

- [ ] **[VAL-3.5] Validasi Matriks Traceability (Bagian 6)**
  - Pastikan tabel matriks mencakup semua ID Workflow yang ada di dokumen.
  - Pastikan kolom `ID Workflow`, `Nama Workflow Diagram`, `Use Case Terkait`, `BRD Terkait`, `SRS Terkait`, dan `Status Kelengkapan` terisi semua tanpa ada sel yang kosong.
  - Jika ada workflow yang ada di dokumen namun tidak ada di matriks: tambahkan barisnya.
  - Jika ada baris di matriks yang workflow diagramnya tidak ada di dokumen: tambahkan diagramnya atau hapus baris tersebut.

- [ ] **[VAL-3.6] Validasi Glosarium (Bagian 8)**
  - Periksa apakah semua istilah teknis dan bisnis yang muncul dalam dokumen sudah terdaftar di Glosarium.
  - Istilah kunci yang wajib ada antara lain: As-Is, To-Be, Flowchart, BPMN, Swimlane, Subprocess, Decision Diamond, Exception Flow, HPP, BOM, RBAC, JWT, UoM, Audit Trail, Stock Opname.
  - Jika ada istilah penting yang belum terdaftar: tambahkan definisinya.

---

### FASE 4 — Validasi Kelayakan sebagai Referensi Fase Berikutnya

> **Tujuan**: Pastikan dokumen ini mampu menjadi referensi yang solid, mandiri, dan tidak ambigu bagi dokumen SDD, ERD, Sequence Diagram, dan Test Plan di Fase 03.

- [ ] **[VAL-4.1] Validasi Kelengkapan Decision Point untuk ERD**
  - Periksa Bagian 7.1 (Daftar Decision Point Kritis).
  - Setiap percabangan logika kondisional dalam diagram yang melibatkan perubahan status data atau evaluasi nilai numerik harus terdaftar di sini.
  - Pastikan kondisi evaluasi (kolom "Kondisi Yang Dievaluasi") menggunakan nilai numerik eksplisit yang diambil dari BRD (bukan estimasi). Contoh: "Laba Bersih >= Rp 15.000.000" harus konsisten dengan angka di BRD v1.1.
  - Bandingkan satu per satu dengan aturan bisnis numerik yang tercatat di BRD. Perbaiki jika ada ketidaksesuaian nilai.

- [ ] **[VAL-4.2] Validasi Status Transisi untuk Implementasi**
  - Identifikasi seluruh status transisi yang muncul dalam diagram (contoh: ANTRI → PROSES DESAIN → PRODUKSI → SELESAI → DIAMBIL).
  - Pastikan setiap status terdefinisi dengan jelas dan konsisten antar workflow.
  - Buat atau periksa apakah ada ringkasan daftar status transisi per entitas data (Transaksi, Antrian Job, Utang, Service). Jika belum ada, tambahkan sub-bagian ringkas di Bagian 7 atau Bagian 2.

- [ ] **[VAL-4.3] Validasi Kelengkapan Alur Lintas Modul (Cross-Module)**
  - Periksa Bagian 5: apakah 3 workflow cross-module sudah menggambarkan alur integrasi antar modul secara lengkap dan tidak terputus?
  - Setiap node dalam workflow cross-module harus secara eksplisit menyebutkan modul mana yang bertanggung jawab (misal: `Sistem M.1:`, `Sistem M.2:`).
  - Pastikan diagram WF-REL-01 (Peta Keterhubungan Workflow antar Modul) di Bagian 2.2 konsisten dengan alur cross-module yang ada di Bagian 5.

- [ ] **[VAL-4.4] Validasi Konsistensi Aturan Bisnis Numerik**
  - Kumpulkan semua nilai numerik bisnis yang tersebut dalam diagram dan narasi prosedural:
    - Batas saldo PPOB kritis: Rp 150.000
    - Minimal deposit PPOB: Rp 500.000
    - Plafon kasbon: Rp 1.000.000 atau 30% gaji
    - Target laba Smart Payroll: Rp 15.000.000
    - Jaminan minimum gaji karyawan: Rp 1.600.000 (50% UMR Rp 3.200.000)
    - Batas peringatan jatuh tempo utang: H-3
    - Batas re-order stok: 7 hari ketersediaan
    - Batas budget pengeluaran bulanan: Rp 4.500.000
    - Plafon pinjaman bank: Rp 50.000.000
    - Batas karakter struk 58mm: 32 karakter; 80mm: 48 karakter
  - Bandingkan setiap nilai di atas dengan yang tertulis di BRD dan SRS. Jika ada ketidaksesuaian: perbaiki sesuai BRD/SRS sebagai sumber kebenaran.

---

### FASE 5 — Validasi Bahasa & Keterbacaan

> **Tujuan**: Pastikan bahasa Indonesia yang digunakan natural, tidak ambigu, dan mudah dipahami oleh junior programmer atau AI model lain yang lebih sederhana.

- [ ] **[VAL-5.1] Validasi Kejelasan Bahasa Indonesia**
  - Baca ulang setiap kalimat dalam narasi prosedural dan deskripsi seksi.
  - Periksa:
    - Apakah ada kalimat yang terlalu panjang (lebih dari 3 klausa) yang bisa membingungkan? → Pecah menjadi kalimat yang lebih pendek.
    - Apakah ada istilah teknis bahasa Inggris yang tidak dijelaskan dan tidak ada di glosarium? → Tambahkan ke glosarium atau beri keterangan singkat inline.
    - Apakah ada kalimat yang ambigu (bisa diinterpretasikan lebih dari satu cara)? → Perbaiki dengan kalimat yang lebih spesifik.
    - Apakah ada kata ganti yang merujuk pada subjek yang tidak jelas? → Ganti dengan nama peran/modul yang spesifik.

- [ ] **[VAL-5.2] Validasi Konsistensi Terminologi**
  - Pastikan satu konsep hanya menggunakan satu istilah secara konsisten di seluruh dokumen. Contoh:
    - "Pramuniaga" vs "Staf Kasir" vs "Kasir" — pastikan peran yang dimaksud konsisten.
    - "Saldo kas laci" vs "kas laci kasir" vs "uang laci" — pilih satu terminologi.
    - "Status SELESAI" vs "status Selesai" vs "status selesai" — gunakan satu format yang konsisten (HURUF KAPITAL atau Title Case).
    - "Pelunasan" vs "pembayaran lunas" — standarkan.
  - Periksa judul setiap Workflow ID (WF-xxx) apakah sudah konsisten formatnya.

- [ ] **[VAL-5.3] Validasi Label dalam Diagram Mermaid.js**
  - Baca label setiap node dalam setiap diagram.
  - Pastikan label node menggunakan format: `[Aktor: Deskripsi Aksi Singkat]` untuk process node yang melibatkan aktor, dan `[Sistem: Deskripsi Aksi Singkat]` untuk node otomatis sistem.
  - Pastikan label decision node menggunakan format pertanyaan dengan tanda tanya: `{Kondisi yang dievaluasi?}`.
  - Perbaiki label yang tidak informatif, terlalu panjang (>60 karakter), atau tidak konsisten formatnya.

---

### FASE 6 — Validasi Kelengkapan Data & Pengisian Data Kosong

> **Tujuan**: Pastikan tidak ada kolom kosong, placeholder, atau data "TBD" yang masih tertinggal.

- [ ] **[VAL-6.1] Identifikasi Seluruh Data Kosong**
  - Baca seluruh dokumen dari awal hingga akhir, tandai semua:
    - Sel tabel yang kosong (tidak ada nilainya)
    - Kolom derivasi yang hanya terisi sebagian (misal hanya ada UC tapi tidak ada BR atau SRS)
    - Kode error yang disebutkan tapi tidak ada di Bagian 7.2
    - Referensi ke "Bagian X" yang tidak ada di dokumen
    - Nomor atau nilai yang tertulis generik (misal "Rp X.000.000" tanpa nilai konkret)

- [ ] **[VAL-6.2] Isi Semua Data Kosong yang Teridentifikasi**
  - Untuk setiap data kosong yang ditemukan di VAL-6.1:
    - Cari nilai yang tepat dari file referensi (BRD, SRS, UCD).
    - Isi dengan data yang sesuai, cocok, dan relevan dalam ruang lingkup dokumen ini.
    - Jika data tidak dapat ditemukan di referensi manapun: tandai dengan komentar `<!-- TODO: [nama_data] perlu diisi — tidak ditemukan di referensi -->` agar dapat dilacak.

- [ ] **[VAL-6.3] Validasi Bagian 9 (Referensi Dokumen)**
  - Periksa tabel referensi dokumen di Bagian 9.
  - Pastikan semua 8 file referensi yang digunakan dalam penyusunan dokumen ini sudah terdaftar.
  - Pastikan kolom `Lokasi Path Relatif` akurat dan path-nya benar-benar ada (sesuai struktur direktori `docs/sdlc/`).
  - Jika dalam proses validasi ini ditemukan file referensi tambahan yang digunakan: tambahkan ke Bagian 9.

---

### FASE 7 — Penyusunan Dokumen Revisi Final

> **Tujuan**: Tuangkan seluruh hasil validasi dan perbaikan ke dalam file target dengan cara overwrite penuh.

- [ ] **[TULIS-7.1] Siapkan Dokumen Revisi Final di Memori**
  - Gabungkan seluruh hasil perbaikan dari Fase 1–6 menjadi satu dokumen utuh yang lengkap.
  - Pastikan struktur dokumen tetap mengikuti urutan bagian yang sudah ada (Bagian 1 s.d Bagian 9).
  - Jangan menambah bagian baru yang tidak relevan dengan karakteristik dokumen Workflow Diagram.

- [ ] **[TULIS-7.2] Perbarui Metadata Header**
  - Ubah `versi` dari `1.0` menjadi `1.1`.
  - Ubah `tanggal` menjadi tanggal eksekusi issue ini (tanggal hari ini saat penulisan).
  - Ubah `status` tetap `Final` jika tidak ada perubahan signifikan struktur, atau `Draft Revisi` jika ada perubahan substansial.

- [ ] **[TULIS-7.3] Perbarui Tabel Riwayat Perubahan Dokumen**
  - Tambahkan baris baru di tabel Riwayat Perubahan Dokumen (jangan hapus baris lama):
    ```
    | 1.1 | [tanggal-hari-ini] | [Ringkasan perubahan yang dilakukan: sebutkan perbaikan spesifik apa saja] | Senior Business Process Analyst & Workflow Modeling Specialist |
    ```
  - Isi kolom "Perubahan" dengan ringkasan konkret dari perbaikan yang dilakukan (misal: "Penambahan validasi aturan numerik, perbaikan konsistensi terminologi, penambahan 2 decision point yang terlewat, perbaikan 3 label node diagram, perbarui Bagian 9 dengan 1 referensi tambahan").

- [ ] **[TULIS-7.4] Tulis Ulang Seluruh Dokumen ke Target File (OVERWRITE)**
  - **PENTING**: Tulis ulang **seluruh dokumen** dari baris pertama hingga terakhir ke file:
    ```
    docs/sdlc/02_analysis/04_workflow_diagram.md
    ```
  - Gunakan metode **overwrite** (timpa seluruh isi file).
  - **LARANGAN KERAS**: Dilarang memotong, meringkas, atau menghilangkan bagian apa pun dari dokumen. Seluruh diagram Mermaid.js, seluruh narasi prosedural, seluruh tabel, dan seluruh glosarium harus ditulis ulang sepenuhnya dalam satu file utuh.
  - Verifikasi setelah penulisan: jumlah baris file baru harus >= jumlah baris file asli (karena ada penambahan konten, bukan pengurangan).

- [ ] **[TULIS-7.5] Tambahkan Referensi Baru di Bagian 9 (Jika Ada)**
  - Jika dalam proses validasi ditemukan bahwa dokumen tambahan di luar 8 referensi awal turut digunakan (misal `02_feasibility_study.md`): tambahkan di baris paling bawah tabel Bagian 9.
  - Format penambahan:
    ```
    | [nomor] | `[nama_file]` | `[path_relatif]` | [keterangan singkat] |
    ```

---

### FASE 8 — Verifikasi Akhir (Self-Check)

- [ ] **[CHECK-8.1]** Baca ulang dokumen yang baru ditulis dari awal hingga akhir untuk memastikan tidak ada kalimat yang terpotong, tabel yang rusak, atau diagram Mermaid.js yang sintaksnya tidak lengkap.

- [ ] **[CHECK-8.2]** Verifikasi bahwa metadata header sudah berubah menjadi `versi: 1.1`.

- [ ] **[CHECK-8.3]** Verifikasi bahwa tabel Riwayat Perubahan Dokumen sudah memiliki baris v1.1 yang terisi lengkap.

- [ ] **[CHECK-8.4]** Verifikasi bahwa jumlah ID Workflow dalam matriks traceability (Bagian 6) sama dengan jumlah workflow diagram aktual yang ada di Bagian 4 dan Bagian 5.

- [ ] **[CHECK-8.5]** Verifikasi bahwa setiap kode error yang disebutkan dalam diagram dan narasi ada di Bagian 7.2, dan sebaliknya.

- [ ] **[CHECK-8.6]** Verifikasi bahwa tidak ada sel kosong yang tersisa di matriks traceability, tabel decision point, dan tabel exception flow.

- [ ] **[CHECK-8.7]** Verifikasi bahwa Bagian 9 sudah mencantumkan semua file referensi yang benar-benar digunakan (termasuk tambahan jika ada).

---

## Instruksi Tambahan Khusus Dokumen Workflow Diagram

Selain instruksi umum di atas, perhatikan hal-hal berikut yang spesifik untuk dokumen Workflow Diagram:

### A. Konsistensi Diagram Mermaid.js
- Pastikan setiap blok kode Mermaid.js diawali dengan ` ```mermaid ` dan diakhiri dengan ` ``` ` tanpa spasi tambahan.
- Pastikan setiap diagram menggunakan `flowchart TD` (top-down) untuk workflow per modul, dan `flowchart LR` (left-right) hanya untuk diagram relasi modul seperti WF-REL-01.
- Pastikan setiap diagram memiliki setidaknya satu node `Start` dan satu node `End`.
- Pastikan setiap `style` yang didefinisikan merujuk ke ID node yang benar-benar ada dalam diagram tersebut.

### B. Konsistensi ID Workflow
- Format ID Workflow harus mengikuti pola yang sudah ada: `WF-[KODE]-[NOMOR]`.
  - Contoh valid: `WF-M1-01`, `WF-ASIS-01`, `WF-CROSS-01`, `WF-OP-01`.
- Setiap ID Workflow harus unik dalam seluruh dokumen.
- Referensi silang antar workflow (subprocess call) harus menyebutkan ID yang tepat.

### C. Kelengkapan Pain Point Analisis (As-Is)
- Setiap workflow As-Is (Bagian 3) wajib memiliki blok `> **Analisis Bottleneck & Pain Point**` setelah diagram.
- Pain point harus disebutkan secara konkret (bukan generik), berdasarkan narasi asli pemilik di `narasi.txt`.

### D. Konsistensi Format Derivasi (To-Be)
- Baris derivasi ditulis persis sebagai:
  ```
  *   **Derivasi**: UC-xxx, BR-F-xx, SRS-F-xxx.
  ```
- Diletakkan tepat setelah judul sub-bagian dan sebelum blok kode Mermaid.js.

### E. Validasi Kelengkapan Modul M.8, M.9, M.10
- Dokumen mencakup modul M.1 s.d M.10. Perhatikan modul M.8 (CRM), M.9 (Multi-Cabang), dan M.10 (Runtime Config) yang biasanya kurang representatif dalam diagram karena cakupannya lebih kecil.
- Pastikan masing-masing modul minimal memiliki satu workflow diagram yang representatif dan lengkap dengan narasi prosedural.

---

## Kriteria Diterima (Acceptance Criteria)

Issue ini dianggap selesai dan dokumen siap diterima jika **semua** kondisi berikut terpenuhi:

| No. | Kriteria | Cara Verifikasi |
|-----|----------|-----------------|
| 1   | Semua 44 UC terpetakan di matriks traceability | Hitung baris di Bagian 6, pastikan ada 44 UC unik |
| 2   | Semua BR-F-01 s.d BR-F-40 terpetakan | Periksa kolom BRD di matriks traceability |
| 3   | Semua SRS-F-001 s.d SRS-F-040 terpetakan | Periksa kolom SRS di matriks traceability |
| 4   | Versi dokumen berubah menjadi v1.1 | Cek header YAML dan tabel riwayat perubahan |
| 5   | Tidak ada sel kosong di matriks traceability | Baca tabel di Bagian 6 baris per baris |
| 6   | Semua kode error konsisten (diagram ↔ Bagian 7.2) | Cek silang Bagian 7.2 dengan seluruh narasi dan diagram |
| 7   | Semua nilai numerik bisnis sesuai dengan BRD | Bandingkan daftar angka di Fase 4 Check VAL-4.4 |
| 8   | Setiap diagram diikuti narasi prosedural | Periksa setelah setiap blok ```mermaid``` |
| 9   | Seluruh file ditulis ulang penuh tanpa pemotongan | Jumlah baris file baru >= jumlah baris file asli |
| 10  | Bahasa Indonesia yang digunakan natural dan tidak ambigu | Baca narasi, tidak ada kalimat yang membingungkan |

---

## Catatan Penting untuk Pelaksana

> [!IMPORTANT]
> **Jangan** mengandalkan memori atau asumsi saat mengisi data. Selalu rujuk ke file referensi yang sudah ditentukan sebelum menulis nilai apapun.

> [!IMPORTANT]
> **Jangan** menggunakan singkatan atau akronim baru yang tidak ada di glosarium dokumen. Jika perlu menambahkan istilah baru, daftarkan dulu di Bagian 8.

> [!WARNING]
> Saat melakukan overwrite file, pastikan seluruh konten dari baris pertama (`---`) hingga baris terakhir (baris referensi terakhir di Bagian 9) ditulis ulang sepenuhnya. Kegagalan penulisan parsial (file terpotong di tengah) akan merusak dokumen dan harus diulang dari awal.

> [!CAUTION]
> Jangan mengubah struktur penomoran bagian yang sudah ada (Bagian 1 s.d 9). Penambahan konten dilakukan di dalam seksi yang sudah ada, bukan membuat bagian baru dengan nomor yang berbeda.

---

*Issue ini dibuat sebagai panduan eksekusi low-level terstruktur untuk validasi dan perbaikan dokumen SDLC AbuCom. Seluruh checklist harus diselesaikan secara berurutan sebelum dokumen dinyatakan siap untuk digunakan sebagai referensi Fase 03 Design.*
