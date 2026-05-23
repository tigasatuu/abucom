# Validasi, Analisis & Penyempurnaan Software Requirements Specification (SRS)

---

## Metadata Issue

| Atribut            | Nilai                                                                 |
|--------------------|-----------------------------------------------------------------------|
| **Judul**          | Validasi, Analisis & Penyempurnaan Software Requirements Specification |
| **Dokumen Utama**  | `docs/sdlc/02_analysis/02_software_requirements.md`                  |
| **Tipe Pekerjaan** | Validasi & Penyempurnaan Dokumen SDLC                                 |
| **Prioritas**      | Critical                                                              |
| **Status**         | Open                                                                  |
| **Dibuat Pada**    | 2026-05-23                                                            |
| **Dikerjakan Oleh**| Junior Programmer / AI Model Lain                                     |

---

## 1. Latar Belakang & Konteks

Dokumen **Software Requirements Specification (SRS)** versi 1.0 telah berhasil disusun pada fase sebelumnya. Dokumen ini merupakan penerjemah teknis dari *Business Requirements Document* (BRD) ke dalam spesifikasi teknis formal yang wajib digunakan sebagai acuan implementasi kode dan desain database.

Namun, sebelum dokumen ini dijadikan rujukan utama pada **Fase 03 Design** (SDD/ERD/Schema SQL), **Fase 04 Implementation** (penulisan kode Python), dan **Fase 05 Testing** (penyusunan test cases), dokumen ini **WAJIB** divalidasi, diaudit, dan disempurnakan secara menyeluruh oleh persona yang otoritatif.

Issue ini mendefinisikan langkah-langkah validasi yang harus dilakukan secara **berurutan, tuntas, dan tanpa pengecualian**.

---

## 2. Persona Pelaksana

**Kamu adalah seorang Principal Systems Analyst & Senior Software Requirements Engineer** dengan spesialisasi:
- Memformulasikan dokumen SRS formal berkelas industri (IEEE 830 / ISO/IEC/IEEE 29148:2018).
- Melakukan rekayasa kebutuhan (*requirements engineering*) untuk sistem manajemen bisnis multi-modul berbasis CLI.
- Mengaudit ketuntasan, konsistensi, dan keterlacakan kebutuhan (*requirements traceability*) dua arah antara dokumen BRD dan SRS.
- Memvalidasi kelayakan teknis spesifikasi sistem Python berbasis Functional Programming (FP) Murni, database MySQL InnoDB, dan arsitektur client-server LAN.
- Mengidentifikasi celah, inkonsistensi, ambiguitas, dan data kosong dalam dokumen teknis.
- Menjamin dokumen bebas dari halusinasi teknis, placeholder tidak terisi, dan ketidaksesuaian numerik.

**Kamu bertindak sebagai pengaudit paling ketat dan tidak memberikan toleransi terhadap:**
- Kebutuhan teknis yang tidak lengkap, tidak terukur, atau tidak dapat diuji (*non-testable*).
- Ketidaksesuaian numerik atau penamaan antara SRS dan dokumen referensi.
- Placeholder kosong (`[DIISI]`, `TBD`, `N/A`) yang seharusnya dapat diisi dari dokumen referensi.
- Bahasa yang ambigu, membingungkan, atau tidak natural dalam Bahasa Indonesia formal.

---

## 3. Daftar File yang Harus Dibaca

Sebelum melakukan validasi apa pun, baca **seluruh isi** file-file berikut secara **berurutan** dari atas hingga baris terakhir. Jangan skip.

### 3.1. Dokumen Utama (Target Validasi)

- [ ] **Baca penuh** `docs/sdlc/02_analysis/02_software_requirements.md` — dokumen SRS v1.0 yang akan divalidasi dan ditulis ulang.

### 3.2. Dokumen Referensi Primer (Paling Penting — WAJIB DIBACA TUNTAS)

- [ ] **Baca penuh** `docs/sdlc/02_analysis/01_business_requirements.md` — BRD v1.1 sumber derivasi utama seluruh kebutuhan fungsional dan non-fungsional SRS.
- [ ] **Baca penuh** `docs/sdlc/01_planning/04_tech_stack_decision.md` — Tech Stack Decision v1.1, sumber batasan implementasi teknis (Python FP, MySQL InnoDB, Library versi, dll.).

### 3.3. Dokumen Referensi Sekunder (WAJIB DIBACA TUNTAS)

- [ ] **Baca penuh** `docs/sdlc/01_planning/01_project_charter.md` — Project Charter v1.1, untuk validasi lingkup, tujuan, dan batasan proyek.
- [ ] **Baca penuh** `docs/sdlc/01_planning/05_innovation_proposal.md` — Innovation Proposal v1.1, untuk validasi konteks inovasi dan fitur unik yang harus tercermin di SRS.
- [ ] **Baca penuh** `docs/sdlc/01_planning/02_feasibility_study.md` — Feasibility Study v1.1, untuk validasi asumsi teknis, lingkungan operasi, dan batasan sumber daya.
- [ ] **Baca penuh** `docs/sdlc/01_planning/03_stakeholder_register.md` — Stakeholder Register v1.1, untuk validasi deskripsi aktor, peran, kebutuhan, dan hak akses RBAC.
- [ ] **Baca penuh** `docs/sdlc/narasi.txt` — Narasi awal proyek, untuk validasi konteks bisnis latar belakang secara keseluruhan.

---

## 4. Tahapan Validasi & Analisis (Eksekusi Berurutan)

> **PERATURAN KRITIS:**
> - Setiap tahapan HARUS diselesaikan penuh sebelum lanjut ke tahapan berikutnya.
> - Catat semua temuan (masalah, inkonsistensi, gap, perbaikan) secara tertulis dalam memori kerja kamu sebelum menulis ulang.
> - Jangan menulis ulang dokumen sebelum seluruh Tahap 1 hingga Tahap 9 selesai diaudit.

---

### Tahap 1 — Komparasi Mendalam: SRS vs. Seluruh Dokumen Referensi

**Tujuan**: Memastikan seluruh informasi yang relevan dari BRD dan referensi lain telah dimuat secara akurat di SRS.

- [ ] **1.1** Buat daftar seluruh kode kebutuhan bisnis fungsional (BR-F-01 hingga BR-F-40) dari BRD.
- [ ] **1.2** Buat daftar seluruh kode kebutuhan teknis fungsional (SRS-F-001 hingga SRS-F-040, termasuk SRS-F-ADD-xxx) dari SRS.
- [ ] **1.3** Lakukan pemetaan satu per satu: setiap BR-F dari BRD **HARUS** memiliki padanan SRS-F yang sesuai di SRS. Tandai BR-F mana yang belum memiliki padanan.
- [ ] **1.4** Lakukan pemetaan satu per satu: setiap BR-NF dari BRD **HARUS** memiliki padanan SRS-NF yang sesuai di SRS. Tandai BR-NF mana yang belum memiliki padanan.
- [ ] **1.5** Verifikasi: setiap SRS-F yang ada **HARUS** bisa dilacak balik ke minimal satu BR-F di BRD (tidak ada SRS-F yang "berdiri sendiri" tanpa akar BRD).
- [ ] **1.6** Periksa konsistensi jumlah modul (M.1 hingga M.10) antara BRD dan SRS — apakah semua modul di BRD terwakili di SRS.
- [ ] **1.7** Periksa konsistensi jumlah aktor/role pengguna (8 role): `pemilik`, `kepala_percetakan`, `pramuniaga`, `kasir`, `desainer`, `produksi_cetak`, `fotocopy_print`, `gudang` — pastikan deskripsi, hak akses, dan kode STK setiap aktor sesuai antara SRS dan BRD/Stakeholder Register.
- [ ] **1.8** Periksa: apakah batasan teknis dari **Tech Stack Decision v1.1** (versi library Python, versi MySQL, standar encoding, paradigma FP, dll.) semuanya tercermin secara akurat di SRS Bagian 2.4, 2.5, dan 2.6.
- [ ] **1.9** Periksa: apakah seluruh konfigurasi runtime (parameter `system_configs`) yang disebutkan di BRD (misalnya threshold alert saldo PPOB, batas kasbon, threshold pengeluaran besar, UMR, dsb.) semuanya terdaftar dan terdefinisi di SRS Bab 6.
- [ ] **1.10** Periksa: apakah daftar kode error (ERR-XXX-XXX) di SRS Bab 7 sudah lengkap, konsisten, dan mencakup semua skenario exception yang disebutkan di setiap SRS-F.
- [ ] **1.11** Periksa: apakah Matriks Keterlacakan Kebutuhan (RTM) di SRS sudah mencantumkan semua ID SRS-F dan semua ID BR-F asal secara dua arah (forward & backward) tanpa ada yang terlewat.
- [ ] **1.12** Periksa: apakah gambar arsitektur sistem (diagram Mermaid) dan deskripsi lingkungan operasi di SRS sudah sesuai dengan spesifikasi hardware/software di Feasibility Study dan Tech Stack Decision.

---

### Tahap 2 — Validasi Kelengkapan & Relevansi Konten

**Tujuan**: Memastikan SRS hanya memuat informasi yang memang seharusnya ada dalam dokumen SRS (tidak lebih, tidak kurang).

- [ ] **2.1** Periksa: apakah ada informasi **strategis bisnis** (visi misi, analisis pasar, latar belakang bisnis) yang seharusnya ada di BRD atau Project Charter, tetapi masuk ke dalam SRS — jika ada, tandai untuk dihapus/dipindahkan.
- [ ] **2.2** Periksa: apakah ada informasi **teknis implementasi fisik** yang terlalu detail (kode Python aktual, SQL query, skrip shell) yang seharusnya masuk ke SDD atau dokumen implementasi, bukan SRS — jika ada, evaluasi apakah perlu dikurangi tingkat detailnya agar tetap di level spesifikasi, bukan implementasi.
- [ ] **2.3** Periksa: apakah setiap spesifikasi fungsional (SRS-F-XXX) memiliki semua atribut wajib berikut tanpa ada yang kosong atau tidak relevan:
  - [ ] **ID** yang unik dan konsisten.
  - [ ] **Derivasi BRD** (kode BR-F yang menjadi sumbernya).
  - [ ] **Modul** yang benar.
  - [ ] **Prioritas** (High / Medium / Low) yang konsisten dengan prioritas di BRD.
  - [ ] **Aktor** yang sesuai dengan definisi RBAC.
  - [ ] **Deskripsi Teknis** yang jelas dan measurable (bisa diuji).
  - [ ] **Input yang Diperlukan** lengkap dengan tipe data dan validasi.
  - [ ] **Proses/Logika Bisnis** yang detail dan tidak ambigu.
  - [ ] **Output yang Dihasilkan** yang terukur.
  - [ ] **Aturan Validasi** yang konkret.
  - [ ] **Penanganan Pengecualian** dengan kode error spesifik (format ERR-XXX-NNN).
  - [ ] **Ketergantungan** ke SRS-F lain yang relevan.
  - [ ] **Catatan Implementasi** yang sesuai dengan paradigma FP Murni.
- [ ] **2.4** Periksa: apakah setiap spesifikasi non-fungsional (SRS-NF-XXX) memiliki **metrik kuantitatif yang terukur** (bukan pernyataan kualitatif abstrak seperti "cepat" atau "aman") — contoh yang benar: `< 3 detik`, `99.5% uptime`, `bcrypt cost factor 12`.
- [ ] **2.5** Periksa: apakah Contoh Wireframe CLI yang ada di SRS sudah merepresentasikan tampilan yang realistis dan sesuai dengan library `rich` dan `tabulate` sebagaimana ditetapkan di Tech Stack Decision.
- [ ] **2.6** Periksa: apakah Model Data Konseptual (ERD Mermaid) mencantumkan semua entitas utama yang dibutuhkan oleh ke-10 modul, dengan relasi dan kardinalitas yang benar.
- [ ] **2.7** Periksa: apakah ada entitas atau tabel database yang disebutkan di dalam body SRS-F (misalnya `tabel antrian_kerja`, `tabel poin_insentif`, `tabel limbah_produksi`) tetapi tidak terdapat di ERD — jika ada, tambahkan ke ERD.

---

### Tahap 3 — Validasi Standar Struktur Dokumen

**Tujuan**: Memastikan struktur dokumen SRS memenuhi standar industri yang layak dijadikan acuan formal.

- [ ] **3.1** Periksa: apakah SRS memiliki **semua bab wajib** standar SRS industri (IEEE 830 / ISO 29148) berikut:
  - [ ] Bab 1: Pendahuluan (tujuan, cakupan, definisi, referensi, audiens).
  - [ ] Bab 2: Deskripsi Umum Sistem (perspektif produk, fungsi utama, karakteristik pengguna, lingkungan operasi, batasan desain, asumsi & ketergantungan).
  - [ ] Bab 3: Spesifikasi Kebutuhan Fungsional (per modul, lengkap).
  - [ ] Bab 4: Spesifikasi Kebutuhan Non-Fungsional (performa, keamanan, keandalan, pemeliharaan, portabilitas, dll.).
  - [ ] Bab 5: Model Data Konseptual (ERD Mermaid).
  - [ ] Bab 6: Konfigurasi Sistem Runtime.
  - [ ] Bab 7: Daftar Kode Error Standar.
  - [ ] Bab 8: Contoh Wireframe CLI.
  - [ ] Bab 9: Matriks Keterlacakan Kebutuhan (RTM) dua arah.
  - [ ] Riwayat Perubahan Dokumen.
  - [ ] Daftar Referensi Dokumen.
- [ ] **3.2** Periksa: apakah penomoran heading (H1, H2, H3, H4) konsisten, tidak ada yang loncat atau tumpang tindih.
- [ ] **3.3** Periksa: apakah setiap modul di Bab 3 menggunakan format tabel atribut yang **seragam** (tidak ada variasi format antara SRS-F satu dengan yang lain).
- [ ] **3.4** Periksa: apakah Riwayat Perubahan Dokumen di awal sudah ada dan terisi dengan benar (versi, tanggal, perubahan, oleh siapa).
- [ ] **3.5** Periksa: apakah Bagian 1.3 (Definisi, Akronim, Singkatan) sudah mencantumkan **semua istilah teknis** yang digunakan di dalam dokumen (termasuk yang muncul di Bab 3, 4, 5, 6, 7, 8) — jika ada istilah teknis yang belum didefinisikan, tambahkan.
- [ ] **3.6** Periksa: apakah Bagian 1.4 (Referensi Dokumen) sudah mencantumkan semua dokumen SDLC yang sebenarnya dijadikan sumber (termasuk `narasi.txt`) — jika ada yang belum tercantum tapi digunakan sebagai sumber, tambahkan.

---

### Tahap 4 — Validasi Kelayakan sebagai Input Fase SDLC Berikutnya

**Tujuan**: Memastikan SRS ini cukup lengkap dan konkret untuk dijadikan input bagi Fase 03 Design (SDD/ERD/Schema), Fase 04 Implementation (kode Python), dan Fase 05 Testing (test cases).

- [ ] **4.1** Periksa setiap SRS-F: apakah **Input yang Diperlukan** sudah menyebutkan nama kolom, tipe data, dan batasan validasi yang cukup bagi developer untuk merancang struktur tabel database MySQL — jika tidak, tambahkan.
- [ ] **4.2** Periksa setiap SRS-F: apakah **Proses/Logika Bisnis** sudah cukup deterministik (tidak ambigu, tidak interpretasi ganda) bagi developer untuk langsung menulis kode Python — jika ada yang masih abstrak, jabarkan lebih konkret.
- [ ] **4.3** Periksa setiap SRS-F: apakah **Aturan Validasi** sudah cukup spesifik dan terukur untuk dikonversi menjadi unit test atau integration test — contoh buruk: "input harus valid"; contoh baik: "input `kuantitas` harus berupa `DECIMAL(15,4)` bernilai > 0, gagalkan jika NULL atau negatif".
- [ ] **4.4** Periksa setiap SRS-F: apakah **Penanganan Pengecualian** menyertakan semua kemungkinan skenario error yang perlu ditangani (koneksi DB terputus, input invalid, overflow desimal, hak akses ditolak, dll.) — jika ada skenario yang belum tercantum, tambahkan.
- [ ] **4.5** Periksa Bab 4 (SRS-NF): apakah setiap kebutuhan non-fungsional memiliki **kriteria penerimaan (acceptance criteria)** yang cukup jelas untuk diuji pada fase testing — contoh: "waktu respons transaksi < 3 detik pada jaringan LAN 100Mbps dengan 3 koneksi simultan".
- [ ] **4.6** Periksa: apakah **formula matematika** yang digunakan (HPP BOM, depresiasi aset, margin keuntungan, smart payroll, insentif poin, sisa hari reorder, selisih kas shift) sudah ditulis secara formal menggunakan notasi LaTeX atau teks formula yang tidak ambigu, dan apakah contoh numeriknya sudah ada dan benar.
- [ ] **4.7** Periksa: apakah **ERD Mermaid** di Bab 5 sudah cukup detail untuk dijadikan acuan perancangan schema SQL — setidaknya harus menampilkan: nama tabel, primary key, foreign key, dan tipe data kolom kritis.
- [ ] **4.8** Periksa: apakah **Konfigurasi Runtime** di Bab 6 sudah menyebutkan **semua** parameter `system_configs` beserta nama kunci (`config_key`), nilai default, tipe data, dan penjelasan — jika ada parameter yang disebutkan di SRS-F tetapi tidak ada di Bab 6, tambahkan.
- [ ] **4.9** Periksa: apakah **Wireframe CLI** di Bab 8 merepresentasikan setidaknya menu utama, satu alur transaksi kasir, dan dashboard admin pemilik secara cukup realistis untuk dijadikan referensi implementasi tampilan terminal.

---

### Tahap 5 — Validasi Bahasa Indonesia

**Tujuan**: Memastikan seluruh dokumen menggunakan Bahasa Indonesia yang natural, formal, tidak ambigu, dan mudah dipahami oleh junior programmer atau AI model yang lebih kecil.

- [ ] **5.1** Periksa: apakah ada kalimat yang terlalu panjang (lebih dari 3 baris) yang bisa dipecah menjadi kalimat lebih pendek tanpa kehilangan makna teknis.
- [ ] **5.2** Periksa: apakah ada terminologi teknis bahasa Inggris yang digunakan tanpa padanan Bahasa Indonesia atau tanpa penjelasan, padahal bisa dijelaskan — jika ada, tambahkan penjelasan singkat dalam tanda kurung.
- [ ] **5.3** Periksa: apakah ada istilah teknis yang digunakan secara **tidak konsisten** di seluruh dokumen (misalnya kadang disebut "antrian" kadang "queue" — pilih satu dan gunakan secara konsisten).
- [ ] **5.4** Periksa: apakah instruksi dalam setiap SRS-F sudah menggunakan **kata wajib yang tegas** dan tidak bersifat opsional — gunakan "HARUS", "WAJIB", "DILARANG" secara konsisten (bukan "sebaiknya", "disarankan", "mungkin").
- [ ] **5.5** Periksa: apakah ada ambiguitas pronoun (misalnya "sistem ini" tanpa jelas merujuk ke sistem apa, atau "user" tanpa jelas role yang mana) — jika ada, perjelas subjeknya.
- [ ] **5.6** Periksa: apakah ada kalimat pasif yang membingungkan yang sebaiknya diubah menjadi kalimat aktif dengan subjek yang jelas.

---

### Tahap 6 — Validasi Kualitas & Kelengkapan Menyeluruh (Anti-Blocking)

**Tujuan**: Memastikan dokumen ini tidak akan terus dipertanyakan atau diinterupsi oleh developer di fase berikutnya karena informasi yang kurang atau tidak jelas.

- [ ] **6.1** Periksa: apakah ada **SRS-F yang tidak menyebutkan tabel database MySQL mana yang terlibat** (INSERT/UPDATE/SELECT/DELETE) — jika ada, tambahkan nama tabelnya secara eksplisit.
- [ ] **6.2** Periksa: apakah ada **SRS-F yang tidak menyebutkan apakah operasinya harus dibungkus dalam database transaction (START TRANSACTION ... COMMIT/ROLLBACK)** — jika ada operasi yang mengubah lebih dari satu tabel, pastikan disebutkan secara eksplisit.
- [ ] **6.3** Periksa: apakah ada **SRS-NF yang metrik kuantitatifnya tidak disebutkan secara spesifik** (misalnya hanya menyebut "performa tinggi" tanpa angka) — jika ada, tetapkan angka yang realistis berdasarkan spesifikasi hardware di Feasibility Study.
- [ ] **6.4** Periksa: apakah **setiap SRS-ADD-xxx (kebutuhan teknis tambahan)** seperti koneksi database pooling, session JWT, startup script, dan penanganan exception global sudah cukup spesifik dalam menjelaskan parameternya.
- [ ] **6.5** Periksa: apakah ada **duplikasi informasi** yang berlebihan antara satu SRS-F dengan SRS-F lain yang menyebabkan inkonsistensi jika salah satu diubah — jika ada, konsolidasikan dengan merujuk ke SRS-F yang relevan.
- [ ] **6.6** Periksa: apakah ada **nomor urut SRS-F yang loncat** (misalnya SRS-F-015, SRS-F-016, ... lalu tiba-tiba SRS-F-039) yang berpotensi membingungkan — jika ada, berikan penjelasan atau restrukturisasi penomoran dengan catatan di Riwayat Perubahan.
- [ ] **6.7** Periksa: apakah **semua SRS-F untuk M.8 (CRM Pelanggan), M.9 (Multi-Cabang), dan M.10 (Runtime Config)** sudah cukup detail dan bukan hanya placeholder singkat tanpa substansi.
- [ ] **6.8** Periksa: apakah deskripsi **UU PDP No. 27/2022** yang berkaitan dengan penyimpanan data pelanggan (nomor WhatsApp, riwayat transaksi) sudah disebutkan secara cukup konkret dalam SRS-F yang relevan (minimal SRS-F CRM dan SRS-F Audit Trail).

---

### Tahap 7 — Identifikasi & Pengisian Data Kosong / Placeholder

**Tujuan**: Menemukan semua data yang kosong, belum terisi, atau perlu diisi, lalu mengisinya dengan data yang tepat.

- [ ] **7.1** Cari seluruh kemunculan placeholder seperti: `[DIISI]`, `[TBD]`, `[TODO]`, `N/A`, `???`, `...`, tanda kurung kosong `()`, atau sel tabel yang kosong di seluruh dokumen SRS.
- [ ] **7.2** Untuk setiap placeholder yang ditemukan, tentukan apakah data pengisinya tersedia di salah satu dokumen referensi — jika ya, **isi dengan data yang sesuai** dari referensi tersebut.
- [ ] **7.3** Periksa apakah **semua konfigurasi runtime di Bab 6** (tabel `system_configs`) sudah memiliki `config_key`, `config_value` (nilai default yang realistis), `tipe_data`, dan `deskripsi` yang terisi lengkap — jika ada yang kosong, isi dengan nilai yang masuk akal berdasarkan konteks bisnis dan referensi.
- [ ] **7.4** Periksa apakah **semua baris di RTM (Bab 9)** sudah terisi lengkap: kolom SRS-F ID, Deskripsi Singkat, BR-F Sumber, Modul, Prioritas, dan Status Verifikasi — jika ada yang kosong, isi.
- [ ] **7.5** Periksa apakah **parameter teknis spesifik** yang disebutkan di SRS-F seperti `bcrypt cost factor`, `JWT expiry 8 jam`, `threshold alert saldo Rp 150.000`, `batas kasbon Rp 1.000.000`, `threshold pengeluaran besar Rp 500.000`, dan lainnya sudah konsisten dengan nilai yang tertera di BRD dan Tech Stack Decision.
- [ ] **7.6** Periksa apakah **daftar kode error di Bab 7** sudah mencakup semua kode ERR-XXX-NNN yang disebutkan di seluruh SRS-F (lakukan crosscheck manual satu per satu) — jika ada kode error yang disebutkan di SRS-F tapi tidak ada di Bab 7, tambahkan ke Bab 7.
- [ ] **7.7** Periksa apakah ada **SRS-F yang menyebutkan kebutuhan untuk PPOB 6 e-wallet** (BRD BR-F-16) namun tidak merinci dengan detail nama keenam e-wallet tersebut beserta skema komparasi biaya admin — jika kurang rinci, lengkapi.
- [ ] **7.8** Periksa apakah **tier poin insentif 4-level** (SRS-F-020) sudah menyebutkan tipe transaksi spesifik di masing-masing tier secara lengkap sesuai BRD — jika ada yang belum lengkap, tambahkan.

---

### Tahap 8 — Validasi Khusus Ciri Khas Dokumen SRS Ini

**Tujuan**: Validasi aspek spesifik yang merupakan ciri khas teknis unik dokumen SRS AbuCom.

- [ ] **8.1** **Presisi Desimal**: Periksa apakah setiap SRS-F yang melibatkan kalkulasi keuangan atau inventaris secara **eksplisit** menyebutkan penggunaan pustaka `decimal` Python dan tipe data `DECIMAL(15,4)` MySQL — jika ada yang hanya menyebut "hitung" tanpa detail presisi, tambahkan.
- [ ] **8.2** **Functional Programming (FP) Murni**: Periksa apakah setiap SRS-F yang memiliki logika kalkulasi sudah menyebutkan bahwa fungsi harus diimplementasikan sebagai **pure function** (tanpa side effect, tanpa mutasi state global) di Python — jika ada yang tidak menyebutkan, tambahkan catatan implementasi FP-nya.
- [ ] **8.3** **ACID & InnoDB Transaction**: Periksa apakah setiap SRS-F yang melibatkan operasi tulis ke lebih dari satu tabel MySQL sudah secara **eksplisit** menyebutkan keharusan menggunakan `START TRANSACTION ... COMMIT` dan `ROLLBACK` — jika ada yang belum, tambahkan.
- [ ] **8.4** **RBAC Multi-Level**: Periksa apakah setiap SRS-F sudah menyebutkan **aktor/role yang diizinkan** secara spesifik (bukan generik "pengguna"), dan apakah aktor tersebut konsisten dengan matriks RBAC di BRD.
- [ ] **8.5** **Audit Trail**: Periksa apakah setiap SRS-F yang melibatkan operasi modifikasi data sensitif (retur, batal, edit stok, kasbon, payroll, pinjaman) sudah **secara eksplisit** menyebutkan keharusan mencatat ke `audit_logs` — jika ada yang belum, tambahkan.
- [ ] **8.6** **Multi-Cabang Ready**: Periksa apakah penjelasan kolom `cabang_id` di SRS (bagian batasan desain dan ERD) sudah cukup jelas menjelaskan bahwa kolom ini wajib ada di setiap tabel relasional — termasuk tabel mana saja yang wajib punya `cabang_id`.
- [ ] **8.7** **Dual-OS Compatibility**: Periksa apakah SRS sudah menyebutkan secara jelas bahwa path file (untuk arsip desain) HARUS menggunakan `pathlib` Python untuk kompatibilitas Windows backslash vs Linux forward slash.
- [ ] **8.8** **Kode Error Format**: Periksa apakah semua kode error mengikuti format baku `ERR-[KATEGORI]-[NNN]` secara konsisten — kategori yang valid adalah: `DB`, `VAL`, `AUTH`, `CASH`, `STOCK`, `SYS`, `FLOW`, `FILE`, `INPUT`, `IMPORT`, `PERF`.

---

### Tahap 9 — Pemeriksaan Konsistensi Numerik & Lintas Dokumen

**Tujuan**: Memastikan tidak ada angka, nama, atau nilai yang kontradiktif antara SRS dan dokumen referensi.

- [ ] **9.1** Verifikasi: jumlah total kebutuhan fungsional di SRS (BR-F-01 s/d BR-F-40 = 40 kebutuhan) sudah memiliki padanan SRS-F yang tepat di dokumen ini — jika ada yang terlewat, tambahkan.
- [ ] **9.2** Verifikasi: jumlah total kebutuhan non-fungsional di SRS (BR-NF-01 s/d BR-NF-11 = 11 kebutuhan) sudah semua memiliki padanan SRS-NF yang tepat.
- [ ] **9.3** Verifikasi: nilai threshold saldo PPOB kritis (`Rp 150.000`) konsisten antara SRS dan BRD.
- [ ] **9.4** Verifikasi: nilai limit kasbon karyawan (`Rp 1.000.000` atau `30%` gaji) konsisten antara SRS dan BRD.
- [ ] **9.5** Verifikasi: nilai threshold pengeluaran besar (`Rp 500.000`) konsisten antara SRS dan BRD.
- [ ] **9.6** Verifikasi: `bcrypt cost factor` yang disebutkan di SRS konsisten dengan Tech Stack Decision.
- [ ] **9.7** Verifikasi: durasi session JWT (`8 jam`) konsisten antara SRS dan BRD/Tech Stack Decision.
- [ ] **9.8** Verifikasi: jumlah tier poin insentif karyawan (`4 tier`) dan nilai rupiah per poin di masing-masing tier konsisten antara SRS dan BRD.
- [ ] **9.9** Verifikasi: jumlah e-wallet yang dibandingkan di PPOB (`6 e-wallet`) konsisten antara SRS dan BRD.
- [ ] **9.10** Verifikasi: persentase alokasi Smart Payroll (`25% laba bersih` untuk total gaji staf, minimum `50% UMR`) konsisten antara SRS dan BRD.
- [ ] **9.11** Verifikasi: versi library Python yang disebutkan di SRS (mysql-connector-python, bcrypt, pyjwt, rich, tabulate, python-dotenv) konsisten dengan versi yang ditetapkan di Tech Stack Decision.
- [ ] **9.12** Verifikasi: nama-nama tabel MySQL utama yang disebutkan di SRS konsisten dan tidak ada yang namanya berbeda-beda di SRS-F yang berlainan (misal: `antrian_kerja` vs `antrian` — pilih satu).

---

## 5. Penulisan Ulang Dokumen (Eksekusi Setelah Semua Tahap 1–9 Selesai)

> **PERATURAN MUTLAK PENULISAN ULANG:**
> Setelah seluruh tahap validasi di atas selesai, tulis ulang dokumen ke file target yang sama.
> Jangan mulai menulis sebelum seluruh Tahap 1–9 selesai diaudit dan semua temuan dicatat.

### 5.1. Instruksi Teknis Penulisan

- [ ] **10.1** Buka file `docs/sdlc/02_analysis/02_software_requirements.md` untuk ditimpa (*overwrite*).
- [ ] **10.2** Ubah versi dokumen dari `v1.0` menjadi `v1.1` di bagian front matter YAML (baris paling atas).
- [ ] **10.3** Tambahkan baris baru di tabel **Riwayat Perubahan Dokumen** untuk versi `1.1` dengan tanggal hari ini, deskripsi perubahan yang mencerminkan semua perbaikan yang dilakukan, dan kolom "Oleh" diisi dengan peran persona pelaksana.
- [ ] **10.4** Tulis ulang **seluruh isi dokumen dari baris pertama (front matter YAML) hingga baris terakhir** secara lengkap, menggabungkan semua perbaikan dan penambahan dari hasil audit Tahap 1–9.
- [ ] **10.5** **DILARANG KERAS** melakukan truncation, pemotongan, ringkasan, atau penggantian sebagian konten dengan `[... lanjutan ...]`, `[bagian ini tidak berubah]`, atau sejenisnya — **SELURUH TEKS HARUS DITULIS PENUH dari baris pertama hingga terakhir**.
- [ ] **10.6** Pertahankan format dan struktur markdown yang sudah ada: heading hierarchy, tabel atribut SRS-F, blok kode/Mermaid, formula LaTeX, kode error, dll. — hanya ubah konten yang memang perlu diperbaiki.
- [ ] **10.7** Pastikan setiap bagian yang sebelumnya kosong atau berisi placeholder sudah terisi dengan konten yang tepat dan relevan.
- [ ] **10.8** Pastikan tidak ada baris yang berisi `[DIISI]`, `[TBD]`, `[TODO]`, `???`, atau placeholder kosong lainnya setelah penulisan ulang selesai.

### 5.2. Urutan Penulisan Bagian Dokumen

Tulis ulang dokumen dengan urutan bagian sebagai berikut (ikuti urutan ini secara ketat):

1. Front Matter YAML (versi, tanggal, status, penyusun).
2. Judul Dokumen.
3. Tabel Riwayat Perubahan Dokumen (v1.0 lama + v1.1 baru).
4. Bab 1: Pendahuluan (1.1 s/d 1.6).
5. Bab 2: Deskripsi Umum Sistem (2.1 s/d 2.6, termasuk diagram Mermaid arsitektur).
6. Bab 3: Spesifikasi Kebutuhan Fungsional (semua SRS-F-001 s/d SRS-F-040 + SRS-F-ADD-xxx, dikelompokkan per modul M.1 s/d M.10).
7. Bab 4: Spesifikasi Kebutuhan Non-Fungsional (semua SRS-NF-001 s/d SRS-NF-011 atau lebih).
8. Bab 5: Model Data Konseptual (ERD Mermaid lengkap).
9. Bab 6: Konfigurasi Sistem Runtime (tabel `system_configs` lengkap semua parameter).
10. Bab 7: Daftar Kode Error Standar (lengkap semua kategori dan kode).
11. Bab 8: Contoh Wireframe Terminal CLI (minimal 3 wireframe).
12. Bab 9: Matriks Keterlacakan Kebutuhan / RTM (tabel dua arah lengkap, semua SRS-F dan BR-F).
13. Bagian Referensi Dokumen (daftar semua file referensi yang digunakan, termasuk tambahan baru jika ada).

### 5.3. Verifikasi Pasca Penulisan

- [ ] **11.1** Setelah penulisan selesai, baca kembali baris pertama dokumen — pastikan front matter YAML sudah benar (versi `1.1`, tanggal hari ini, status `Draft`).
- [ ] **11.2** Hitung jumlah SRS-F yang ada di dokumen hasil revisi — pastikan minimal 40 SRS-F fungsional + SRS-F-ADD-xxx tersedia.
- [ ] **11.3** Hitung jumlah SRS-NF yang ada di dokumen hasil revisi — pastikan minimal 11 SRS-NF tersedia.
- [ ] **11.4** Periksa apakah RTM sudah mencantumkan semua 40 baris BR-F dengan padanan SRS-F-nya.
- [ ] **11.5** Periksa apakah Bab 7 (Daftar Kode Error) sudah mencakup semua kode ERR yang disebutkan di Bab 3.
- [ ] **11.6** Periksa apakah Bab 6 (Runtime Config) sudah tidak ada sel tabel yang kosong.
- [ ] **11.7** Periksa apakah tidak ada kata `[DIISI]`, `[TBD]`, `TODO`, atau `???` yang masih tersisa di dokumen.

---

## 6. Aturan Penambahan File Referensi Baru

Jika selama proses validasi kamu menemukan atau menggunakan file referensi **tambahan** yang tidak tertulis di Bagian 1.4 SRS saat ini (misalnya `narasi.txt`), maka:

- [ ] **12.1** Tambahkan file referensi baru tersebut ke **Bagian 1.4 (Referensi Dokumen SDLC)** di dalam dokumen SRS.
- [ ] **12.2** Tambahkan juga ke **bagian akhir baris paling bawah dokumen SRS** dalam format daftar referensi yang konsisten dengan referensi yang sudah ada.
- [ ] **12.3** Pastikan penambahan referensi baru juga dicantumkan di baris Riwayat Perubahan v1.1 sebagai bagian dari deskripsi perubahan.

---

## 7. Kriteria Penyelesaian Issue (Definition of Done)

Issue ini dinyatakan **selesai** apabila seluruh kondisi berikut terpenuhi:

- [ ] Seluruh tahap validasi (Tahap 1–9) telah dilakukan dengan tuntas dan hasilnya terdokumentasi dalam perubahan dokumen.
- [ ] Dokumen SRS v1.1 telah berhasil ditulis ulang dan ditimpa ke file `docs/sdlc/02_analysis/02_software_requirements.md`.
- [ ] Semua 40 kebutuhan fungsional (BR-F-01 s/d BR-F-40) memiliki padanan SRS-F yang lengkap dan tervalidasi.
- [ ] Semua 11 kebutuhan non-fungsional (BR-NF-01 s/d BR-NF-11) memiliki padanan SRS-NF yang terukur dan tervalidasi.
- [ ] Tidak ada placeholder kosong yang tersisa di seluruh dokumen.
- [ ] ERD Mermaid sudah mencakup semua entitas yang relevan.
- [ ] RTM dua arah sudah lengkap.
- [ ] Daftar kode error sudah mencakup semua ERR yang disebutkan di body dokumen.
- [ ] Versi dokumen sudah diubah menjadi `v1.1`.
- [ ] Bahasa Indonesia sudah natural, formal, tidak ambigu, dan mudah dipahami.
- [ ] Dokumen tidak mengandung informasi yang seharusnya tidak ada di SRS (misalnya analisis pasar murni atau kode program aktual).

---

## 8. Catatan Tambahan untuk Pelaksana

> [!IMPORTANT]
> **Jangan mulai menulis ulang dokumen sebelum semua tahap validasi (1–9) selesai dilakukan secara penuh.** Menulis ulang tanpa audit terlebih dahulu akan menghasilkan dokumen yang sama cacat atau lebih buruk dari sebelumnya.

> [!WARNING]
> **Dilarang melakukan truncation atau pemotongan konten** saat menulis ulang dokumen. Jika kamu kehabisan token atau context window, hentikan sesi, catat posisi terakhir yang sudah ditulis, dan lanjutkan di sesi berikutnya dari posisi tersebut — jangan pernah meringkas atau menghilangkan bagian konten yang sudah ada.

> [!NOTE]
> **Dokumen SRS ini adalah fondasi teknis dari seluruh fase implementasi AbuCom.** Kualitas dokumen ini secara langsung menentukan kualitas kode program, desain database, dan test cases yang akan dikembangkan. Kesalahan di dokumen ini akan **berlipat ganda** pada fase berikutnya.

> [!TIP]
> Jika kamu menemukan informasi yang tidak konsisten antara SRS dan BRD, **selalu utamakan BRD sebagai sumber kebenaran** karena BRD sudah tervalidasi di Issue #0012. Jika ada konflik antara BRD dan Tech Stack Decision, catat konflik tersebut dan gunakan Tech Stack Decision sebagai acuan teknis implementasi.

---

*Issue ini dibuat pada 2026-05-23 sebagai bagian dari siklus SDLC proyek AbuCom — Sistem Manajemen Terpadu Usaha Percetakan.*
