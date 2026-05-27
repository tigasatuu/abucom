---
dokumen    : Changelog
proyek     : AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
versi      : 1.0
tanggal    : 2026-05-27
status     : Draft
penyusun   : Senior Configuration Manager & Release Documentation Specialist
---

# Changelog — AbuCom

## Riwayat Perubahan Dokumen

| Versi | Tanggal    | Deskripsi Perubahan                                                                                              | Oleh                                                            |
|:---:|:---:|---|---|
| **1.0** | 2026-05-27 | Pembuatan awal dokumen Changelog v1.0 untuk rilis perdana AbuCom v1.0.0 berdasarkan audit 14 dokumen SDLC. | Senior Configuration Manager & Release Documentation Specialist |

---

## 1. Informasi Dokumen

### 1.1. Tujuan Dokumen
Dokumen **Changelog** ini disusun sebagai catatan perubahan kronologis resmi (*official chronological change log*) untuk mendokumentasikan setiap penambahan fitur baru, perbaikan kesalahan (*bug fixes*), peningkatan mekanisme keamanan, pembaruan infrastruktur, serta pembaruan berkas dokumentasi SDLC pada sistem aplikasi AbuCom. Dokumen ini bertujuan untuk menjadi satu-satunya sumber kebenaran tunggal (*Single Source of Truth*) terkait sejarah evolusi kode program, menjamin ketertelusuran (*traceability*), dan mempermudah audit kualitas sebelum Go-Live operasional toko.

### 1.2. Cakupan Dokumen
Dokumen ini mencakup riwayat perubahan penuh pada sistem aplikasi **AbuCom CLI v1.0.0** (termasuk 10 modul fungsional utama M.1 s.d M.10 dan 5 kebutuhan teknis tambahan), rilis yang direncanakan di masa mendatang (roadmap v1.1.0 dan v2.0.0), serta pedoman prosedural bagi pengembang dalam menyusun entri changelog baru selama siklus pemeliharaan korektif dan adaptif.

### 1.3. Posisi Dokumen dalam Siklus SDLC
Dalam siklus hidup pengembangan sistem (SDLC) AbuCom, dokumen Changelog diposisikan pada **Fase 07 — Maintenance** sebagai **Deliverable ke-2**, yang diterbitkan setelah [Maintenance Guide](docs/sdlc/07_maintenance/01_maintenance_guide.md) (Deliverable ke-1) dinyatakan selesai dan tervalidasi.

```text
+-------------------------------------------------------+
|                 Fase 07 — Maintenance                 |
|                                                       |
|  Deliverable 1: Maintenance Guide [SELESAI v1.1]      |
|  Deliverable 2: Changelog [INI — TARGET v1.0]         |
+-------------------------------------------------------+
```

### 1.4. Hubungan dengan Dokumen SDLC Lainnya (Input & Output)
*   **Dokumen Input (Acuan):** Dokumen ini menyerap secara utuh visi dari [Release Notes v1.1](docs/sdlc/06_deployment/03_release_notes.md) (R-01), panduan prosedur dari [Maintenance Guide v1.1](docs/sdlc/07_maintenance/01_maintenance_guide.md) (R-02), konvensi SemVer dan commit dari [Git Workflow v1.1](docs/sdlc/04_implementation/04_git_workflow.md) (R-03), identitas dari [Project Charter v1.1](docs/sdlc/01_planning/01_project_charter.md) (R-04), dan spesifikasi dari [Software Requirements Spec v1.1](docs/sdlc/02_analysis/02_software_requirements.md) (R-05).
*   **Dokumen Output (Penerima Manfaat):** Dokumen ini digunakan sebagai landasan audit kualitas berkala, panduan debugging dan rollback jika terjadi anomali produksi, serta referensi teknis bagi pengembang untuk merilis patch perbaikan versi minor.

### 1.5. Audiens Target
*   **Pemilik Usaha AbuCom (Alfatih):** Sebagai acuan transparansi fitur fungsional yang telah diimplementasikan dalam sistem.
*   **System Administrator / DevOps Support:** Sebagai panduan melacak perubahan konfigurasi database, port, and dependensi.
*   **Tim Pengembang AI (Support):** Sebagai pedoman menulis entri changelog baru agar tetap konsisten dengan konvensi Git.

### 1.6. Definisi, Akronim, dan Singkatan
*   **SemVer:** *Semantic Versioning* (format penomoran rilis vMAJOR.MINOR.PATCH).
*   **CLI:** *Command Line Interface* (antarmuka teks terminal baris perintah).
*   **BOM:** *Bill of Materials* (komposisi bahan baku produk cetak kustom).
*   **HPP:** Harga Pokok Penjualan (biaya modal riil bahan baku langsung).
*   **PPOB:** *Payment Point Online Bank* (layanan pembayaran tagihan virtual).
*   **RBAC:** *Role-Based Access Control* (pembatasan menu CLI berdasarkan peran staf).
*   **JWT:** *JSON Web Token* (token stateless sesi aktif staf).
*   **UU PDP:** Undang-Undang Perlindungan Data Pribadi No. 27 Tahun 2022.
*   **LAN:** *Local Area Network* (jaringan komputer lokal luring toko).

### 1.7. Konvensi Format Entri Changelog
*   Setiap entri perubahan tunggal direpresentasikan oleh satu bullet point `-`.
*   Entri fungsional wajib diawali kode referensi spesifikasi kebutuhan formal (contoh: **[SRS-F-XXX]**).
*   Deskripsi ditulis menggunakan kalimat pendek, padat, teknis, dan diawali kata kerja bernada lampau (contoh: "Ditambahkan", "Diperbaiki", "Diubah").
*   Setiap entri diakhiri dengan penunjuk modul fungsional terkait (contoh: *(Modul M.X)*).

---

## 2. Panduan Pembacaan Changelog

### 2.1. Format Versi (Semantic Versioning)
Changelog AbuCom mengadopsi standar **Semantic Versioning (SemVer)** dengan format `vMAJOR.MINOR.PATCH`:
*   **MAJOR (Besar):** Berubah ketika ada perbaikan arsitektur atau skema database besar yang tidak kompatibel dengan versi sebelumnya (contoh: migrasi dari luring LAN ke sinkronisasi cloud online).
*   **MINOR (Menengah):** Berubah ketika ada penambahan modul fungsional baru yang kompatibel ke belakang (contoh: penyelesaian modul M.3).
*   **PATCH (Kecil):** Berubah ketika ada perbaikan bug (*hotfix*) yang tidak merubah fungsi bisnis luar.

### 2.2. Kategori Perubahan (Change Types)
Perubahan dalam dokumen ini dikelompokkan secara ketat ke dalam kategori standar berikut:
*   **Ditambahkan (Added):** Untuk fitur baru yang diimplementasikan pada versi berjalan.
*   **Diubah (Changed):** Untuk perubahan pada fungsionalitas yang sudah ada.
*   **Diperbaiki (Fixed):** Untuk perbaikan kesalahan (*bug fixes*) or celah keamanan.
*   **Keamanan (Security):** Untuk pembaruan mekanisme kriptografi, RBAC, and perlindungan UU PDP.
*   **Infrastruktur (Infrastructure):** Untuk perubahan skema tabel basis data, locked packages, or hardware node.
*   **Dokumentasi (Documentation):** Untuk penyusunan dan revisi berkas dokumen formal SDLC.
*   **Tidak Digunakan Lagi (Deprecated):** Untuk fitur lama yang akan dihapus pada rilis berikutnya.
*   **Dihapus (Removed):** Untuk fitur yang resmi dieliminasi dari codebase.

### 2.3. Format Entri Changelog
Format penulisan entri adalah sebagai berikut:
```markdown
- **[SRS-F-XXX]** Ditambahkan [deskripsi singkat fitur] untuk [tujuan fitur]. *(Modul M.X)*
```
Contoh visual aktual:
```markdown
- **[SRS-F-001]** Ditambahkan pencatatan transaksi penjualan multi-divisi CLI untuk 5 kategori usaha. *(Modul M.1)*
```

### 2.4. Kode Referensi Terkait (SRS-F-XXX)
Ketertelusuran entri changelog dijamin dengan mencantumkan kode kebutuhan fungsional `SRS-F-XXX` or `SRS-F-ADD-XXX` dari dokumen SRS (R-05). Untuk penanganan kesalahan, gunakan kode ID bug `DEF-XXX` dari *Bug Report Template* (R-14).

### 2.5. Penanda Status Entri
Apabila terdapat parameter data penting yang belum tersedia saat dokumen ini disusun (seperti commit hash tag atau tanggal Go-Live aktual), parameter tersebut ditandai dengan format:
`[DATA BELUM TERSEDIA — perlu diisi manual oleh Pemilik Usaha setelah Go-Live]`

---

## 3. Changelog — Rilis Terbaru

### [1.0.0] — 2027-05-20 (Estimasi)

> [!NOTE]
> Rilis **v1.0.0** merupakan rilis perdana komprehensif (*Initial Major Release*) yang menandai digitalisasi penuh seluruh operasional administrasi, persediaan, keuangan, antrian, dan SDM toko percetakan fisik AbuCom. Rilis ini memigrasikan seluruh operasional manual berbasis Microsoft Excel lama ke dalam sistem baris perintah CLI berbasis Python 3.14.2+ dengan database relasional MySQL 8.4 LTS secara 100% luring (*offline LAN*).

#### Ditambahkan (Added)

##### M.1 — Manajemen Transaksi & Kebijakan Harga
*   **[SRS-F-001]** Ditambahkan pencatatan transaksi penjualan cepat berbasis teks CLI untuk melayani 5 divisi usaha: produk percetakan, retail ATK, e-wallet jasa keuangan, pulsa PPOB, dan jasa perbaikan teknis. *(Modul M.1)*
*   **[SRS-F-002]** Ditambahkan sistem deteksi skema harga dinamis otomatis (Retail, Grosir, Mitra) berdasarkan jumlah kuantitas pembelian atau status keanggotaan pelanggan. *(Modul M.1)*
*   **[SRS-F-003]** Ditambahkan pencatatan pembayaran bertahap (Uang Muka/DP minimal Rp 0 dan Pelunasan) untuk transaksi pesanan cetak kustom. *(Modul M.1)*
*   **[SRS-F-004]** Ditambahkan alur pemrosesan pembatalan transaksi DP 100% dan retur retail ATK rusak, terintegrasi dengan kas laci, log audit, dan wajib menggunakan sandi pemilik fisik. *(Modul M.1)*
*   **[SRS-F-005]** Ditambahkan pelacakan persentase margin keuntungan kotor kualitatif langsung di terminal pemilik berdasarkan formula harga jual dikurangi biaya HPP. *(Modul M.1)*
*   **[SRS-F-006]** Ditambahkan template nota struk cetak teks format `.txt` lokal di folder `exports/receipts/` dengan text-wrapping otomatis pada lebar kertas 58mm atau 80mm. *(Modul M.1)*

##### M.2 — Manajemen Inventaris, BOM & Stock Opname
*   **[SRS-F-007]** Ditambahkan sistem kalkulasi biaya HPP otomatis berbasis komposisi bahan baku berukuran desimal `Decimal(15,4)` dengan pembulatan `ROUND_HALF_UP` dan pemotongan stok otomatis di MySQL. *(Modul M.2)*
*   **[SRS-F-008]** Ditambahkan pencatatan limbah produksi (*waste management*) untuk bahan baku rusak/salah cetak, pemotongan persediaan, dan pencatatan biaya operasional non-kas. *(Modul M.2)*
*   **[SRS-F-009]** Ditambahkan pengelolaan stok gudang dalam unit multi-satuan (Rim, Lembar, Pcs, Ml, Meter_Persegi) dengan dukungan nominal pecahan desimal. *(Modul M.2)*
*   **[SRS-F-010]** Ditambahkan sinkronisasi pencatatan stok retail ATK saat diambil untuk kebutuhan operasional internal cetak. *(Modul M.2)*
*   **[SRS-F-011]** Ditambahkan fitur rekonsiliasi stok berkala (*Stock Opname*) dengan metode pembekuan stok sementara, perbandingan selisih kuantitas fisik vs sistem, dan persetujuan Kepala Percetakan. *(Modul M.2)*
*   **[SRS-F-012]** Ditambahkan analisis prediksi re-order stok bahan baku berdasarkan tingkat konsumsi harian bulanan dengan visual alert kuning/merah. *(Modul M.2)*
*   **[SRS-F-013]** Ditambahkan pencatatan riwayat harga beli barang dari supplier secara kronologis setiap kali pengadaan barang masuk diinput. *(Modul M.2)*
*   **[SRS-F-014]** Ditambahkan utilitas script import data massal inisial awal dari CSV Excel lama secara atomik (`executemany`) dengan performa tinggi (< 5 detik). *(Modul M.2)*
*   **[SRS-F-039]** Ditambahkan panel administrative pemilik untuk memicu backup database manual via safe subprocess `mysqldump` passwordless menjadi berkas ZIP terkompresi terenkripsi AES-256 bit. *(Modul M.2)*
*   **[SRS-F-040]** Ditambahkan pengelolaan profil data supplier, pencatatan utang usaha tempo, penghitungan tenggat jatuh tempo, dan pelunasan terintegrasi kas keluar. *(Modul M.2)*

##### M.3 — Layanan Keuangan Digital, PPOB & Jasa Service
*   **[SRS-F-015]** Ditambahkan pencatatan manual mutasi saldo virtual PPOB (Pulsa/Token) dan alert visual kasir berkedip jika saldo di bawah threshold kritis Rp 150.000. *(Modul M.3)*
*   **[SRS-F-016]** Ditambahkan fitur komparasi biaya admin asli dari 6 e-wallet (Mandiri Agen, Dana, Gopay, LinkAja, ShopeePay, OVO) untuk menyarankan pengiriman paling ekonomis bagi pelanggan dan penghitungan komisi toko. *(Modul M.3)*
*   **[SRS-F-017]** Ditambahkan pencatatan transaksi jasa service & perbaikan PC/printer, terintegrasi dengan pemotongan stok suku cadang gudang dan pendebitan biaya suku cadang ke nota service. *(Modul M.3)*

##### M.4 — Manajemen SDM, Penggajian & Poin Karyawan
*   **[SRS-F-018]** Ditambahkan pengelolaan database karyawan, pencatatan absensi shift harian, dan pengajuan kasbon staf (limit kasbon aktif Rp 1.000.000). *(Modul M.4)*
*   **[SRS-F-019]** Ditambahkan komputasi payroll otomatis berbasis jaminan jaring pengaman minimum 50% UMR (Rp 1.600.000) dengan upah dinamis: Skenario A (gaji tetap jika target laba bersih toko Rp 15.000.000 tercapai) atau Skenario B (alokasi 25% dari laba berjalan dibagi proporsional kehadiran jika target tidak tercapai). *(Modul M.4)*
*   **[SRS-F-020]** Ditambahkan sistem poin insentif otomatis berbasis beban kerja 4-tier transaksi staf harian (Tier 1: Rp 500/poin, Tier 2: Rp 1.500/poin, Tier 3: Rp 2.500/poin, Tier 4: Rp 5.000/poin). *(Modul M.4)*
*   **[SRS-F-021]** Ditambahkan pemotongan gaji bersih bulanan secara otomatis jika terdeteksi memiliki utang kasbon aktif, dan mengubah status kasbon menjadi LUNAS. *(Modul M.4)*

##### M.5 — Sistem Manajemen Antrian & Pelacakan Desain
*   **[SRS-F-022]** Ditambahkan dashboard antrian pekerjaan sekuensial real-time 5 status (`Antri`, `Proses Desain`, `Produksi`, `Selesai`, `Diambil`) per divisi staf. *(Modul M.5)*
*   **[SRS-F-023]** Ditambahkan penyimpanan string path lokasi mockup desain PDF pelanggan di server lokal, kompatibel Dual-OS (`pathlib` Windows/Linux). *(Modul M.5)*
*   **[SRS-F-024]** Ditambahkan pembuatan string pesan notifikasi WhatsApp otomatis berisi invoice, nama pelanggan, sisa DP terformat dengan link wa.me URL encoded (`urllib.parse.quote`). *(Modul M.5)*

##### M.6 — Administrasi Pinjaman, Aset & Pengeluaran
*   **[SRS-F-025]** Ditambahkan pencatatan pinjaman modal terstruktur, membedakan pinjaman komersial bank berbunga (BRI/Mandiri) lengkap dengan tenor jatuh tempo dan pinjaman kerabat tanpa bunga yang fleksibel. *(Modul M.6)*
*   **[SRS-F-026]** Ditambahkan kompilasi laporan Laba/Rugi komprehensif instan per divisi (pendapatan, HPP desimal, OPEX, biaya limbah, penyusutan aset) selesai dalam waktu < 2.0 detik. *(Modul M.6)*
*   **[SRS-F-027]** Ditambahkan notifikasi peringatan visual kuning berkedip saat startup login pemilik jika sisa hari jatuh tempo cicilan bank/utang supplier &le; H-3 (berkedip merah jika lewat jatuh tempo). *(Modul M.6)*
*   **[SRS-F-028]** Ditambahkan pengelolaan aset tetap, penghitungan depresiasi bulanan garis lurus sebagai OPEX, dan alokasi tabungan virtual mesin baru. *(Modul M.6)*
*   **[SRS-F-029]** Ditambahkan pencatatan pengeluaran operasional rutin bulanan dan biaya tak terduga, dengan pengetatan otorisasi verifikasi sandi pemilik fisik untuk pengeluaran &ge; Rp 500.000. *(Modul M.6)*

##### M.7 — Keamanan, Audit Trail & Hak Akses
*   **[SRS-F-030]** Ditambahkan proteksi otorisasi Role-Based Access Control (RBAC) 8 peran berbasis token JWT HS256. *(Modul M.7)*
*   **[SRS-F-031]** Ditambahkan audit trail kronologis otomatis dalam format JSON untuk merekam perubahan data sensitif (`timestamp`, `user_id`, aksi, nama tabel, `old_value`, `new_value`). *(Modul M.7)*
*   **[SRS-F-032]** Ditambahkan log serah terima shift karyawan (*closing shift*) dengan input kas laci fisik dan penguncian baris transaksi shift lama dari modifikasi. *(Modul M.7)*
*   **[SRS-F-033]** Ditambahkan rekonsiliasi kas harian kasir untuk membandingkan uang kas laci fisik vs sistem, dengan alert anomali fraud jika selisih > Rp 10.000. *(Modul M.7)*
*   **[SRS-F-034]** Ditambahkan sistem peringatan anomali transaksi (*fraud detection* sederhana) berupa tanda visual merah jika gagal login brute force > 5x, pembatalan DP > 3x, atau selisih kas > Rp 10.000. *(Modul M.7)*
*   **[SRS-F-035]** Ditambahkan antarmuka menu setup awal wizard inisialisasi master data transaksional dari spreadsheet saat deployment. *(Modul M.7)*

##### M.8 — Pembatalan, Retur & CRM
*   **[SRS-F-036]** Ditambahkan database pelanggan terstruktur (CRM sederhana) dengan WhatsApp terenkripsi Fernet, mematuhi UU PDP No. 27/2022 (mendukung *Right to Erasure* / hard delete permanen). *(Modul M.8)*

##### M.9 — Skalabilitas Multi-Cabang
*   **[SRS-F-037]** Ditambahkan arsitektur data multi-cabang (*Multi-Branch Ready*) dengan menyematkan kolom kunci asing `cabang_id` (INT) di setiap tabel basis data dan default filtering query SELECT. *(Modul M.9)*

##### M.10 — Konfigurasi Sistem Runtime
*   **[SRS-F-038]** Ditambahkan sistem konfigurasi dinamis tanpa hardcode berbasis tabel `system_configs` di MySQL (untuk target laba, limit kasbon, threshold PPOB, toleransi kasir, rupiah per poin, UMR daerah). *(Modul M.10)*

##### Kebutuhan Teknis Tambahan (Additional)
*   **[SRS-F-ADD-01]** Ditambahkan inisialisasi startup aplikasi CLI dan validasi keberadaan berkas `.env` beserta kelengkapan variabelnya. *(Modul M.10)*
*   **[SRS-F-ADD-02]** Ditambahkan manajemen sesi JWT Lifecycle dengan masa kedaluwarsa 8 jam dan mekanisme IDLE auto-logout setelah 30 menit tanpa aktivitas. *(Modul M.7)*
*   **[SRS-F-ADD-03]** Ditambahkan mekanisme connection pool basis data dengan batas ukuran (*pool size*) 5 dan retry mechanism 3x exponential backoff di helper database. *(Modul M.2)*
*   **[SRS-F-ADD-04]** Ditambahkan penanganan kesalahan global (*Global Exception Handling*) dan logging kesalahan terstruktur ke berkas `logs/error_log.txt`. *(Modul M.10)*
*   **[SRS-F-ADD-05]** Ditambahkan standardisasi perintah navigasi CLI kasir (karakter `'0'` untuk kembali, dan `'logout'`/`'exit'` untuk keluar). *(Modul M.1)*

#### Keamanan (Security)
*   **Kriptografi Kata Sandi:** Hashing kata sandi staf menggunakan algoritma bcrypt 60 karakter dengan parameter *Cost Factor* **12** dan *salt length* **16 bytes** untuk mencegah penyimpanan teks polos.
*   **Manajemen Sesi Kasir:** Sesi terminal kasir diamankan token stateless **JSON Web Token (JWT)** ditandatangani algoritma **HS256** dengan masa aktif kedaluwarsa **8 jam (28.800 detik)**. Sesi dibersihkan otomatis dari memori jika program idle > 30 menit.
*   **Otorisasi RBAC 8 Peran:** Proteksi biner dekorator di memori Python membatasi menu CLI untuk peran Pemilik, Kepala Percetakan, Kasir, Desainer, Produksi Cetak, Gudang, Pramuniaga, dan Fotocopy Print.
*   **Enkripsi Data Pribadi Pelanggan:** WhatsApp pelanggan disandi biner **Fernet (cryptography)** 32-byte Base64 key sebelum disimpan ke tabel `pelanggan.whatsapp`, mematuhi **UU PDP No. 27 Tahun 2022**.
*   **Right to Erasure CRM:** Penghapusan profil data WhatsApp secara permanen (*hard delete*) atas permintaan lisan pelanggan difasilitasi di database secara atomik.
*   **OS Server Hardening:** Firewall `ufw` memblokir remote port 3306 kecuali segmen IP statis LAN kasir `192.168.1.0/24`. SSH root login dinonaktifkan (`PermitRootLogin no`). Folder backup `/var/lib/mysql-backups` di-set chmod `700` (root only).
*   **Backup Terenkripsi AES-256 ZIP:** Skrip cron harian pukul 21:00 WIB mengekspor basis data transaksional secara passwordless via `/root/.my.cnf` (600), dikompres ZIP terenkripsi algoritma **AES-256 bit**.
*   **OS Windows PC Kasir Hardening:** Registry Windows AutoPlay dinonaktifkan (`NoDriveTypeAutoRun` diset Hex **`FF`** / 255) mencegah penyebaran virus local dari USB flashdisk.
*   **Audit Trail JSON:** Logger otomatis perubahan data sensitif menyimpan timestamp, `user_id`, aksi, nama tabel, detail JSON string `old_value` dan `new_value`.
*   **Proteksi Eskalasi Transaksi:** Transaksi pengeluaran &ge; Rp 500.000, retur ATK rusak, dan pembatalan DP dikunci wajib memasukkan sandi supervisor `pemilik` fisik di konter.

#### Infrastruktur (Infrastructure)
*   **Database Engine:** Database MySQL 8.4 LTS menggunakan engine transaksional InnoDB (28 tabel relasional ACID compliant), isolation level REPEATABLE READ.
*   **Jaringan LAN Luring:** Topologi jaringan bintang (*star topology*) berbasis Gigabit Switch Hub 8-Port unmanaged (1 Gbps) and Router MikroTik hEX lite (Gateway `192.168.1.1`).
*   **Spesifikasi Node Server:** Mini PC Server Debian 12 (static IP `192.168.1.200`, port 3306), fanless, disangga UPS 600VA stabilizer.
*   **Spesifikasi Node Klien:** PC Desktop Kasir Windows 11 (IP DHCP Lokal, generic printer driver nota 58mm/80mm USB-Serial COM1), disangga UPS 600VA.
*   **Runtime Program:** Python runtime versi 3.14.2+ dengan paradigma Functional Programming (FP) murni (logic bebas OOP).
*   **Locked Dependencies (requirements.txt):** Driver `mysql-connector-python==8.4.0`, dotenv `python-dotenv==1.0.1`, hashing `bcrypt==4.1.0`, token `pyjwt==2.8.0`, kripto `cryptography==42.0.5`, visual `rich==13.7.0`, dan tabular `tabulate==0.9.0`.
*   **Connection Pooling:** Manajemen reuse pool koneksi database (maksimal size 5) dilengkapi auto-retry 3x exponential backoff untuk query LAN.
*   **Dual-OS Deployment:** Dukungan instalasi offline modular pada Linux Debian 12 Server dan Windows 11 Kasir Klien.

#### Dokumentasi (Documentation)
Daftar seluruh berkas dokumentasi formal SDLC AbuCom versi v1.1 yang disusun untuk rilis v1.0.0:
*   **Fase 01 — Planning:**
    -   `docs/sdlc/01_planning/01_project_charter.md`
    -   `docs/sdlc/01_planning/02_feasibility_study.md`
    -   `docs/sdlc/01_planning/03_stakeholder_register.md`
    -   `docs/sdlc/01_planning/04_tech_stack_decision.md`
    -   `docs/sdlc/01_planning/05_innovation_proposal.md`
*   **Fase 02 — Analysis:**
    -   `docs/sdlc/02_analysis/01_business_requirements.md`
    -   `docs/sdlc/02_analysis/02_software_requirements.md`
    -   `docs/sdlc/02_analysis/03_use_case_diagram.md`
    -   `docs/sdlc/02_analysis/04_workflow_diagram.md`
    -   `docs/sdlc/02_analysis/05_data_dictionary.md`
    -   `docs/sdlc/02_analysis/06_access_control_matrix.md`
*   **Fase 03 — Design:**
    -   `docs/sdlc/03_design/01_database_schema.sql`
    -   `docs/sdlc/03_design/02_erd_database.md`
    -   `docs/sdlc/03_design/03_system_architecture.md`
    -   `docs/sdlc/03_design/04_cli_interaction_flow.md`
    -   `docs/sdlc/03_design/05_bom_hpp_design.md`
    -   `docs/sdlc/03_design/06_security_design.md`
*   **Fase 04 — Implementation:**
    -   `docs/sdlc/04_implementation/01_coding_standard.md`
    -   `docs/sdlc/04_implementation/02_environment_setup.md`
    -   `docs/sdlc/04_implementation/03_module_structure.md`
    -   `docs/sdlc/04_implementation/04_git_workflow.md`
*   **Fase 05 — Testing:**
    -   `docs/sdlc/05_testing/01_test_plan.md`
    -   `docs/sdlc/05_testing/02_test_cases.md`
    -   `docs/sdlc/05_testing/03_uat_script.md`
    -   `docs/sdlc/05_testing/04_bug_report_template.md`
*   **Fase 06 — Deployment:**
    -   `docs/sdlc/06_deployment/01_deployment_guide.md`
    -   `docs/sdlc/06_deployment/02_environment_config.yaml`
    -   `docs/sdlc/06_deployment/03_release_notes.md`
*   **Fase 07 — Maintenance:**
    -   `docs/sdlc/07_maintenance/01_maintenance_guide.md`
    -   `docs/sdlc/07_maintenance/02_changelog.md` *(Dokumen ini)*

#### Batasan yang Diketahui (Known Limitations)
*   **CLI-Only Interface:** Aplikasi 100% berbasis teks console. Tidak memiliki antarmuka grafis (GUI) desktop, web, atau mobile.
*   **Keuangan Digital Manual:** Transaksi e-wallet transfer/tarik tunai dan mutasi deposit saldo virtual PPOB diinput secara administratif manual di kasir (tidak terhubung API online instan).
*   **FP Paradigma Constraint:** Logic bisnis ditulis murni menggunakan namedtuples dan pure functions tanpa sintaks `class`, meningkatkan kompleksitas state management sesi program.
*   **Runtime Version Kritis:** Program kasir wajib dijalankan minimal pada Python versi 3.14.2+ dengan database relasional MySQL lokal (tidak mendukung SQLite produksi).
*   **WhatsApp Web Manual Link:** Pesan notifikasi status siap diambil digenerasikan berupa link URL wa.me encoded yang siap disalin kasir secara manual ke WhatsApp Web klien.
*   **Payment Gateway Manual:** Pembayaran non-tunai diverifikasi fisik oleh kasir sebelum diinput ke CLI (belum ada QRIS dinamis API).
*   **Out-of-Scope:** Sinkronisasi marketplace eksternal, mobile app, dan integrasi online.

#### Masalah yang Diketahui (Known Issues)

| ID Masalah | Modul / Fitur | Deskripsi Masalah | Dampak Teknis | Rencana Mitigasi (*Workaround*) |
|:---:|---|---|---|---|
| **DEF-COMPAT-001** | M.1 — Transaksi & Kasir | Glitch rendering karakter visual box-drawing (*mojibake*) pada terminal Windows CMD CP1252 lawas. | Estetika visual terganggu, garis tabel pecah (`â”Œ`, `â”€`, `â”`). | Jalankan aplikasi menggunakan Windows Terminal modern dengan dukungan encoding UTF-8 dan font Cascadia. |
| **DEF-PERF-001** | M.6 — Keuangan & Aset | Latensi kalkulasi laporan Laba/Rugi semester berjalan melebihi 2.0 detik (mencapai 8.75 detik) pada database dengan volume transaksi tinggi (> 50.000 record). | Penurunan performa response time saat agregasi data besar. | Batasi filter pencarian laporan keuangan dalam rentang bulanan untuk mendapatkan hasil kalkulasi instan (< 2.0 detik). |

---

## 4. Rilis yang Direncanakan (Upcoming Releases)

### [1.1.0] — Planned
*   **Graphical User Interface (GUI):** Pembangunan antarmuka visual GUI desktop menggunakan pustaka Tkinter atau PyQt pada PC kasir untuk mempermudah navigasi non-teknis.
*   **API WhatsApp Gateway Otomatis:** Integrasi backend Python dengan gateway API WhatsApp untuk mengirimkan pesan status pesanan siap diambil dan nota pembayaran secara otomatis dari PC kasir.
*   **Analisis Re-Order Stok Cerdas:** Fitur Machine Learning sederhana untuk menganalisis dan memprediksi kebutuhan belanja stok persediaan retail 7 hari sebelum habis berdasarkan tren bulanan.
*   **Payment Gateway QRIS Dinamis:** Integrasi QRIS dinamis API payment gateway untuk memvalidasi pembayaran non-tunai pelanggan secara instan di layar kasir.

### [2.0.0] — Planned
*   **Aplikasi Mobile Admin:** Aplikasi mobile (Android/iOS) terintegrasi luring/cloud terbatas khusus pemilik usaha untuk memantau laporan laba/rugi harian secara remote.
*   **Otomatisasi PPOB & Saldo Agen:** Jembatan API langsung dengan provider pulsa/token tagihan PPOB dan Agen perbankan digital untuk meniadakan input manual mutasi saldo oleh staf.

---

## 5. Pedoman Penulisan Entri Changelog Baru

### 5.1. Prosedur Penambahan Entri
1.  Setiap kali branch fitur (`feature/`), bugfix (`bugfix/`), hotfix (`hotfix/`), atau dokumentasi (`docs/`) selesai dikerjakan, pengembang wajib menyusun draf entri changelog.
2.  Entri changelog baru harus dimasukkan di bawah kategori yang sesuai (Added, Changed, Fixed, Deprecated, Removed, Security, Infrastructure, Documentation) pada bagian paling atas dari draf rilis yang sedang berjalan (unreleased atau draft version baru).
3.  Penggabungan entri changelog ke berkas `docs/sdlc/07_maintenance/02_changelog.md` di branch `main` dilakukan secara eksklusif oleh Pemilik Toko (`STK-000`) atau Release Manager saat pull request disetujui.
4.  Gunakan penanggalan format standar ISO 8601 `YYYY-MM-DD` (contoh: `2026-05-27`).

### 5.2. Template Entri Changelog Baru
Pengembang wajib mematuhi template format penulisan berikut:

*   **Untuk Fitur Fungsional Baru (Added/Changed):**
    ```markdown
    - **[SRS-F-XXX]** [Kata Kerja Lampau] [Deskripsi singkat fungsionalitas dalam Bahasa Indonesia]. *(Modul M.X)*
    ```
    Contoh:
    ```markdown
    - **[SRS-F-001]** Ditambahkan pencatatan transaksi penjualan multi-divisi CLI untuk 5 kategori usaha. *(Modul M.1)*
    ```

*   **Untuk Perbaikan Bug (Fixed):**
    ```markdown
    - **[DEF-XXX]** Diperbaiki [deskripsi singkat bug yang diperbaiki] pada [nama bagian/modul]. *(Modul M.X)*
    ```
    Contoh:
    ```markdown
    - **[DEF-COMPAT-001]** Diperbaiki glitch rendering karakter visual box-drawing (mojibake) pada terminal Windows CMD lawas CP1252. *(Modul M.1)*
    ```

### 5.3. Aturan Penomoran dan Urutan
1.  Penomoran versi wajib mengikuti konvensi **Semantic Versioning (SemVer)** `vMAJOR.MINOR.PATCH`.
2.  Urutan entri di dalam berkas disusun secara **kronologis terbalik (reverse chronological)**, yaitu versi terbaru ditempatkan di bagian paling atas, diikuti versi-versi sebelumnya secara berurutan ke bawah.
3.  Di dalam satu versi, entri dikelompokkan berdasarkan kategori perubahan dengan urutan standar: Added, Changed, Deprecated, Removed, Fixed, Security, Infrastructure, Documentation.

### 5.4. Integrasi dengan Git Workflow dan Conventional Commits
1.  Setiap entri changelog harus memiliki hubungan langsung (*traceability*) dengan pesan commit Git yang di-merge (referensi R-03).
2.  Pengembang wajib memetakan tipe commit ke kategori changelog:
    -   Commit `feat` dipetakan ke kategori `Ditambahkan (Added)` atau `Diubah (Changed)`.
    -   Commit `fix` dipetakan ke kategori `Diperbaiki (Fixed)` atau `Keamanan (Security)`.
    -   Commit `docs` dipetakan ke kategori `Dokumentasi (Documentation)`.
    -   Commit `perf` / `refactor` dipetakan ke kategori `Diubah (Changed)` atau `Infrastruktur (Infrastructure)`.
3.  Penulisan deskripsi commit Conventional Commits di branch `main` harus diusahakan selaras dengan entri yang akan dimasukkan ke berkas Changelog.
4.  Junior Programmer (`STK-000`) wajib memverifikasi keselarasan Git history dengan dokumen Changelog sebelum melakukan tagging rilis Git.

---

## 6. Glosarium

1.  **Changelog:** Catatan kronologis terstruktur yang mendokumentasikan seluruh perubahan yang dilakukan pada proyek perangkat lunak di setiap versi.
2.  **Semantic Versioning (SemVer):** Konvensi penomoran versi perangkat lunak menggunakan format tiga angka `vMAJOR.MINOR.PATCH` untuk mengindikasikan tingkat signifikansi perubahan kode.
3.  **Conventional Commits:** Konvensi penulisan pesan commit Git terstruktur (`type(scope): description`) guna memudahkan pembacaan sejarah repositori dan otomatisasi rilis.
4.  **Keep a Changelog:** Panduan praktik terbaik internasional untuk penataan format berkas catatan perubahan agar mudah dibaca oleh manusia.
5.  **Major Release:** Rilis versi besar yang memuat perubahan API atau skema database besar yang tidak kompatibel dengan versi sebelumnya (MAJOR naik, MINOR dan PATCH direset ke 0).
6.  **Minor Release:** Rilis versi menengah yang menambahkan fitur atau fungsionalitas baru yang kompatibel ke belakang (MINOR naik, PATCH direset ke 0).
7.  **Patch Release:** Rilis versi kecil yang hanya berisi perbaikan kesalahan (*bug fixes*) atau celah keamanan tanpa penambahan fungsionalitas baru (PATCH naik).
8.  **Added (Kategori Perubahan):** Kategori untuk mencatat seluruh fitur atau fungsionalitas baru yang diperkenalkan pada versi rilis tersebut.
9.  **Changed (Kategori Perubahan):** Kategori untuk mencatat perubahan atau pembaruan pada fitur/fungsionalitas yang sudah ada sebelumnya.
10. **Fixed (Kategori Perubahan):** Kategori untuk mencatat perbaikan kesalahan (*bug fixes*) yang berhasil diselesaikan pada versi tersebut.
11. **Deprecated (Kategori Perubahan):** Kategori untuk mencatat fitur yang tidak direkomendasikan lagi untuk digunakan dan direncanakan untuk dihapus pada rilis mendatang.
12. **Removed (Kategori Perubahan):** Kategori untuk mencatat fitur yang telah resmi dihapus sepenuhnya dari perangkat lunak pada versi tersebut.
13. **Security (Kategori Perubahan):** Kategori untuk mencatat penambahan atau perbaikan mekanisme keamanan data dan otorisasi sistem.
14. **Infrastructure (Kategori Perubahan):** Kategori untuk mencatat pembaruan terkait arsitektur sistem, skema database, locked dependencies, and konfigurasi deployment.
15. **Documentation (Kategori Perubahan):** Kategori untuk mencatat berkas dokumentasi formal (seperti dokumen SDLC) yang disusun atau direvisi pada rilis tersebut.
16. **Traceability (Ketertelusuran):** Kemampuan untuk melacak hubungan antara entri perubahan di changelog dengan spesifikasi kebutuhan (SRS) dan commit Git di repositori.
17. **Unreleased:** Bagian changelog paling atas yang digunakan untuk menampung draf entri perubahan yang belum dipublikasikan dalam versi rilis formal.

---

## 7. Referensi Dokumen

Penyusunan berkas Changelog v1.0 didasarkan secara mutlak pada 14 berkas dokumentasi formal SDLC AbuCom:

| Kode Ref | Nama Dokumen Referensi | Path Relatif Berkas | Versi | Prioritas | Peran / Hubungan dalam Penyusunan |
|:---:|---|---|:---:|:---:|---|
| **R-01** | Release Notes v1.1 | `docs/sdlc/06_deployment/03_release_notes.md` | 1.1 | **PRIMER** | Acuan utama seluruh fitur baru M.1 s.d M.10, keamanan, bug fixes, known limitations, known issues, roadmap, and dependencies. |
| **R-02** | Maintenance Guide v1.1 | `docs/sdlc/07_maintenance/01_maintenance_guide.md` | 1.1 | **PRIMER** | Acuan daftar modul aktif, 28 tabel database InnoDB, locked libraries, and kategori pemeliharaan sistem. |
| **R-03** | Git Workflow v1.1 | `docs/sdlc/04_implementation/04_git_workflow.md` | 1.1 | **PRIMER** | Acuan standardisasi SemVer, Conventional Commits, tagging, and pembagian tanggung jawab tim campuran. |
| **R-04** | Project Charter v1.1 | `docs/sdlc/01_planning/01_project_charter.md` | 1.1 | **SEKUNDER** | Acuan nama proyek, deskripsi, tim pengembang, milestone, dan informasi sponsor. |
| **R-05** | Software Requirements Spec v1.1 | `docs/sdlc/02_analysis/02_software_requirements.md` | 1.1 | **SEKUNDER** | Acuan pemetaan kode kebutuhan fungsional (SRS-F-001 s.d SRS-F-040) ke entri changelog. |
| **R-06** | Database Schema v1.1 | `docs/sdlc/03_design/01_database_schema.sql` | 1.1 | **SEKUNDER** | Acuan verifikasi 28 nama tabel InnoDB untuk kategori Infrastruktur. |
| **R-07** | System Architecture v1.1 | `docs/sdlc/03_design/03_system_architecture.md` | 1.1 | **SEKUNDER** | Acuan diagram deployment, topologi LAN luring, hardware specs, and connection pooling. |
| **R-08** | Security Design v1.1 | `docs/sdlc/03_design/06_security_design.md` | 1.1 | **SEKUNDER** | Acuan spesifikasi otentikasi bcrypt, sesi JWT, Fernet CRM, AES-256 backup, and audit trail JSON. |
| **R-09** | Coding Standard v1.1 | `docs/sdlc/04_implementation/01_coding_standard.md` | 1.1 | **TERSIER** | Acuan standardisasi FP murni, type hints, PEP 8/257, and presisi Decimal. |
| **R-10** | Module Structure v1.1 | `docs/sdlc/04_implementation/03_module_structure.md` | 1.1 | **TERSIER** | Acuan pemetaan file-to-module untuk scope referensi changelog. |
| **R-11** | Test Plan v1.1 | `docs/sdlc/05_testing/01_test_plan.md` | 1.1 | **TERSIER** | Acuan hasil testing, exit criteria, dan QA summary. |
| **R-12** | Deployment Guide v1.1 | `docs/sdlc/06_deployment/01_deployment_guide.md` | 1.1 | **TERSIER** | Acuan prosedur instalasi offline, setup database, and runbook pemeliharaan harian. |
| **R-13** | Tech Stack Decision v1.1 | `docs/sdlc/01_planning/04_tech_stack_decision.md` | 1.1 | **TERSIER** | Acuan locked packages, batasan platform runtime Python 3.14.2+ & MySQL 8.4. |
| **R-14** | Bug Report Template v1.1 | `docs/sdlc/05_testing/04_bug_report_template.md` | 1.1 | **TERSIER** | Acuan format bug severity, priority level, dan known issues. |

---

*Dokumen Changelog AbuCom ini dinyatakan sah dan berlaku sebagai catatan perubahan resmi seluruh rilis sistem.*
