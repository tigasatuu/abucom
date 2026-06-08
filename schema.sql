-- ============================================================
-- HEADER & METADATA DOKUMEN
-- ============================================================
-- Nama Dokumen: Database Schema (DDL SQL)
-- Nama Proyek: AbuCom — Sistem Manajemen Terpadu Usaha Percetakan
-- Versi Dokumen: 1.2
-- Tanggal Pembuatan: 2026-05-29
-- Penyusun: Senior Database Architect & DDL Validation Expert
-- Status Dokumen: Final
-- Deskripsi: File inisialisasi skema basis data fisik MySQL 8.x LTS AbuCom
--            yang dirancang multi-cabang (Multi-Branch Ready) dan transaksional.
-- Prasyarat: MySQL Server 8.0/8.4 LTS harus terinstal dan berjalan.
-- Pembatasan Akses: Sangat Rahasia (Pemilik Sahaja)
-- Instruksi Eksekusi: mysql -u root -p < 01_database_schema.sql
--
-- RIWAYAT PERUBAHAN DOKUMEN:
-- Versi | Tanggal    | Perubahan                               | Oleh
-- ------|------------|-----------------------------------------|---------------------------
-- 1.0   | 2026-05-24 | Inisialisasi awal 28 tabel, index, seed | Senior Database Architect
-- 1.1   | 2026-05-24 | Validasi & penyempurnaan menyeluruh     | Senior Database Architect & DDL Validation Expert
-- 1.2   | 2026-05-29 | Validasi FASE 1-8 (Issue #0074)         | Senior Database Architect & DDL Validation Expert
-- ============================================================

-- ============================================================
-- BAGIAN 1 — KONFIGURASI AWAL & PEMBUATAN DATABASE
-- ============================================================
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION';
SET NAMES utf8mb4;

-- PERINGATAN: Script ini akan menghapus dan membuat ulang database abucom_db dari awal.
-- Pastikan backup sudah dilakukan sebelum menjalankan script ini di lingkungan produksi.
DROP DATABASE IF EXISTS abucom_db;
CREATE DATABASE abucom_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE abucom_db;

-- ============================================================
-- BAGIAN 2 — PEMBUATAN TABEL (CREATE TABLE)
-- ============================================================

-- ============================================================
-- KELOMPOK A: TABEL INDUK (TANPA FOREIGN KEY)
-- ============================================================

-- ------------------------------------------------------------
-- [TABEL 01] cabang
-- ------------------------------------------------------------
CREATE TABLE cabang (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik baris cabang',
    nama_cabang VARCHAR(100) NOT NULL UNIQUE COMMENT 'Nama unik dari unit cabang usaha fisik',
    alamat TEXT NOT NULL COMMENT 'Alamat fisik lokasi cabang operasional',
    telp VARCHAR(20) NOT NULL COMMENT 'Nomor telepon kontak operasional cabang',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Data cabang toko fisik AbuCom multi-branch | Sensitivitas: Operasional | Modul: M.9';

-- ============================================================
-- KELOMPOK B: TABEL MASTER LEVEL 2 (FK KE CABANG)
-- ============================================================

-- ------------------------------------------------------------
-- [TABEL 02] pengguna
-- ------------------------------------------------------------
CREATE TABLE pengguna (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik akun pengguna staf',
    nama_lengkap VARCHAR(100) NOT NULL COMMENT 'Nama lengkap asli dari staf/karyawan',
    username VARCHAR(50) NOT NULL UNIQUE COMMENT 'Nama unik staf untuk proses otentikasi login',
    password_hash VARCHAR(255) NOT NULL COMMENT 'String hash kata sandi terenkripsi bcrypt Cost 12',
    -- Nilai valid: 'pemilik' | 'kepala_percetakan' | 'pramuniaga' | 'kasir' | 'desainer' | 'produksi_cetak' | 'fotocopy_print' | 'gudang'
    role VARCHAR(30) NOT NULL COMMENT 'Peran administratif hak akses menu CLI (RBAC) | Nilai valid: \'pemilik\' | \'kepala_percetakan\' | \'pramuniaga\' | \'kasir\' | \'desainer\' | \'produksi_cetak\' | \'fotocopy_print\' | \'gudang\'',
    failed_login_attempts INT NOT NULL DEFAULT 0 COMMENT 'Jumlah kumulatif kegagalan login berturut-turut',
    locked_until TIMESTAMP NULL DEFAULT NULL COMMENT 'Batas waktu suspensi login akibat brute-force',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Keterkaitan penempatan cabang kerja staf',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_pengguna_failed_login_attempts CHECK (failed_login_attempts BETWEEN 0 AND 5),
    CONSTRAINT fk_pengguna_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Akun kredensial, role, nama lengkap, dan session staf | Sensitivitas: Operasional | Modul: M.7';

-- ------------------------------------------------------------
-- [TABEL 03] pelanggan
-- ------------------------------------------------------------
CREATE TABLE pelanggan (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik keanggotaan pelanggan',
    nama_pelanggan VARCHAR(100) NOT NULL COMMENT 'Nama lengkap dari pelanggan terdaftar',
    whatsapp VARCHAR(100) NOT NULL UNIQUE COMMENT 'Nomor WA pelanggan terenkripsi lokal (UU PDP)',
    tanggal_terdaftar DATE NOT NULL DEFAULT (CURRENT_DATE) COMMENT 'Tanggal pertama kali terdaftar di program CRM',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Identifikasi cabang asal pendaftaran pelanggan',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_pelanggan_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Data profil CRM pelanggan toko | Sensitivitas: Operasional | Modul: M.8';

-- ------------------------------------------------------------
-- [TABEL 04] supplier
-- ------------------------------------------------------------
CREATE TABLE supplier (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik data supplier',
    nama_supplier VARCHAR(100) NOT NULL COMMENT 'Nama badan usaha / perorangan vendor supplier',
    alamat TEXT NOT NULL COMMENT 'Alamat kantor / gudang pengiriman supplier',
    telp VARCHAR(30) NOT NULL COMMENT 'Nomor telepon aktif supplier untuk pengadaan',
    email VARCHAR(100) NOT NULL COMMENT 'Alamat email supplier untuk pengadaan',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Identifikasi cabang pencatat supplier',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_supplier_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Data vendor penyuplai bahan & retail | Sensitivitas: Operasional | Modul: M.2';
-- ------------------------------------------------------------
-- [TABEL 29] satuan_ukur
-- ------------------------------------------------------------
CREATE TABLE satuan_ukur (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY 
        COMMENT 'Identifikasi unik satuan ukur',
    nama_satuan VARCHAR(30) NOT NULL UNIQUE 
        COMMENT 'Nama satuan ukur (e.g. Rim, Lembar, Pcs, Ml, Meter_Persegi, Liter, Kg, Botol)',
    kategori_satuan VARCHAR(30) NOT NULL 
        COMMENT 'Kategori pengelompokan satuan (e.g. Kuantitas, Panjang, Luas, Volume, Berat)',
    simbol VARCHAR(10) NOT NULL DEFAULT '' 
        COMMENT 'Simbol singkatan (e.g. pcs, lbr, rim, ml, m², L, kg)',
    keterangan TEXT NULL DEFAULT NULL 
        COMMENT 'Deskripsi tambahan tentang penggunaan satuan ini',
    is_aktif BOOLEAN NOT NULL DEFAULT TRUE 
        COMMENT 'Status aktif satuan (soft delete)',
    cabang_id INT NOT NULL DEFAULT 1 
        COMMENT 'Identifikasi cabang pemilik data satuan',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP 
        COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 
        COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_satuan_ukur_cabang_id FOREIGN KEY (cabang_id) 
        REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Master satuan ukur barang dan bahan baku | Sensitivitas: Operasional | Modul: M.2';

-- ------------------------------------------------------------
-- [TABEL 30] konversi_satuan
-- ------------------------------------------------------------
CREATE TABLE konversi_satuan (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY 
        COMMENT 'Identifikasi unik baris konversi',
    satuan_asal_id INT NOT NULL 
        COMMENT 'Referensi satuan ukur sumber konversi',
    satuan_tujuan_id INT NOT NULL 
        COMMENT 'Referensi satuan ukur target konversi',
    faktor_konversi DECIMAL(15,4) NOT NULL 
        COMMENT 'Faktor pengali konversi (1 satuan_asal = faktor * satuan_tujuan)',
    cabang_id INT NOT NULL DEFAULT 1 
        COMMENT 'Identifikasi cabang pemilik aturan konversi',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP 
        COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 
        COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT uq_konversi_asal_tujuan UNIQUE (satuan_asal_id, satuan_tujuan_id),
    CONSTRAINT chk_konversi_faktor CHECK (faktor_konversi > 0),
    CONSTRAINT fk_konversi_satuan_asal_id FOREIGN KEY (satuan_asal_id) 
        REFERENCES satuan_ukur(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_konversi_satuan_tujuan_id FOREIGN KEY (satuan_tujuan_id) 
        REFERENCES satuan_ukur(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_konversi_satuan_cabang_id FOREIGN KEY (cabang_id) 
        REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Aturan konversi antar satuan ukur | Sensitivitas: Operasional | Modul: M.2';

-- ------------------------------------------------------------
-- [TABEL 05] barang
-- ------------------------------------------------------------
CREATE TABLE barang (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik item barang master',
    nama_barang VARCHAR(100) NOT NULL COMMENT 'Nama komersial barang retail atau bahan baku',
    -- Nilai valid: 'Retail_ATK' | 'Bahan_Baku'
    tipe_barang VARCHAR(20) NOT NULL COMMENT 'Klasifikasi peran barang dalam alur operasional | Nilai valid: \'Retail_ATK\' | \'Bahan_Baku\'',
    satuan_uom VARCHAR(20) NOT NULL COMMENT 'Satuan dasar stok (Unit of Measure)',
    stok_saat_ini DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Jumlah kuantitas fisik stok yang tersedia',
    harga_beli DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Harga pengadaan/beli dari vendor supplier',
    harga_retail DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Harga jual per unit untuk pelanggan umum',
    harga_grosir DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Harga jual per unit untuk pembelian grosir',
    min_grosir DECIMAL(15,4) NOT NULL DEFAULT 1.0000 COMMENT 'Jumlah minimal pembelian pemicu harga grosir',
    harga_mitra DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Harga jual per unit khusus akun terdaftar Mitra',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Unit cabang pemilik kepemilikan stok barang',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_barang_harga_beli CHECK (harga_beli >= 0),
    CONSTRAINT chk_barang_harga_retail CHECK (harga_retail >= 0),
    CONSTRAINT chk_barang_harga_grosir CHECK (harga_grosir >= 0),
    CONSTRAINT chk_barang_harga_mitra CHECK (harga_mitra >= 0),
    CONSTRAINT chk_barang_min_grosir CHECK (min_grosir > 0),
    CONSTRAINT fk_barang_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Data master retail ATK, harga beli, dan bahan baku | Sensitivitas: Operasional | Modul: M.2';

-- ------------------------------------------------------------
-- [TABEL 06] saldo_ppob
-- ------------------------------------------------------------
CREATE TABLE saldo_ppob (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik pos deposit PPOB',
    -- Nilai valid: 'Pulsa_Data' | 'Token_Tagihan'
    akun_tipe VARCHAR(30) NOT NULL UNIQUE COMMENT 'Klasifikasi server server produk digital PPOB | Nilai valid: \'Pulsa_Data\' | \'Token_Tagihan\'',
    saldo_terakhir DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Saldo sisa deposit digital berjalan sistem',
    tanggal_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Waktu terakhir penyesuaian transaksi / topup',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang pengelola akun PPOB bersangkutan',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_saldo_ppob_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Pos deposit saldo virtual agen tagihan | Sensitivitas: Operasional | Modul: M.3';

-- ------------------------------------------------------------
-- [TABEL 07] saldo_ewallet
-- ------------------------------------------------------------
CREATE TABLE saldo_ewallet (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik baris e-wallet',
    -- Nilai valid: 'Mandiri Agen' | 'Dana' | 'Gopay' | 'LinkAja' | 'ShopeePay' | 'OVO'
    nama_ewallet VARCHAR(50) NOT NULL UNIQUE COMMENT 'Nama 6 akun dompet digital / agen resmi bank | Nilai valid: \'Mandiri Agen\' | \'Dana\' | \'Gopay\' | \'LinkAja\' | \'ShopeePay\' | \'OVO\'',
    saldo_terakhir DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Jumlah deposit saldo virtual tersisa di e-wallet',
    biaya_admin_flat DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Tarif flat biaya admin e-wallet per transfer',
    biaya_admin_persen DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Persentase biaya admin tambahan dari nominal',
    limit_harian DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Batas kuota total nominal transfer per hari',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang penguasa otorisasi saldo e-wallet',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_saldo_ewallet_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Tarif & saldo 6 akun dompet digital | Sensitivitas: Operasional | Modul: M.3';

-- ------------------------------------------------------------
-- [TABEL 08] system_configs
-- ------------------------------------------------------------
CREATE TABLE system_configs (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik baris parameter config',
    parameter_key VARCHAR(100) NOT NULL UNIQUE COMMENT 'Kunci string parameter regulasi (tanpa spasi)',
    parameter_value VARCHAR(255) NOT NULL COMMENT 'Nilai parameter yang dimuat ke program CLI',
    tipe_data VARCHAR(30) NOT NULL DEFAULT 'VARCHAR' COMMENT 'Penentu pemandu casting tipe di program Python',
    deskripsi TEXT NOT NULL COMMENT 'Penjelasan aturan bisnis terkait parameter',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang berlakunya pengaturan parameter bisnis',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_system_configs_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Parameter runtime regulasi bisnis | Sensitivitas: Sangat Sensitif | Modul: M.10';

-- ============================================================
-- KELOMPOK C: TABEL TRANSAKSIONAL (FK KE MASTER)
-- ============================================================

-- ------------------------------------------------------------
-- [TABEL 09] bom_komposisi
-- ------------------------------------------------------------
CREATE TABLE bom_komposisi (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik baris komposisi BOM',
    barang_induk_id INT NOT NULL COMMENT 'Referensi produk jadi percetakan kustom',
    bahan_baku_id INT NOT NULL COMMENT 'Referensi komponen bahan baku pembentuk',
    kuantitas_desimal DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Volume/panjang/pcs bahan baku yang digunakan',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang berlakunya standar formula BOM ini',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT uq_bom_komposisi_induk_bahan UNIQUE (barang_induk_id, bahan_baku_id),
    CONSTRAINT fk_bom_komposisi_barang_induk_id FOREIGN KEY (barang_induk_id) REFERENCES barang(id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_bom_komposisi_bahan_baku_id FOREIGN KEY (bahan_baku_id) REFERENCES barang(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_bom_komposisi_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Komposisi bahan produk cetak kustom | Sensitivitas: Operasional | Modul: M.2';

-- ------------------------------------------------------------
-- [TABEL 10] transaksi
-- ------------------------------------------------------------
CREATE TABLE transaksi (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik baris data transaksi',
    no_invoice VARCHAR(50) NOT NULL UNIQUE COMMENT 'Nomor nota penjualan format: INV/YYYYMMDD/XXXX',
    pelanggan_id INT NULL DEFAULT NULL COMMENT 'Keterkaitan pelanggan CRM terdaftar',
    kasir_id INT NOT NULL COMMENT 'Karyawan kasir operasional pencatat penjualan',
    tanggal_transaksi TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu terjadinya pembayaran transaksi',
    total_bayar DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Total tagihan akhir belanja nota yang dibayar',
    dp_bayar DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Nilai uang muka Down Payment yang diterima kasir',
    -- Nilai valid: 'LUNAS' | 'BELUM LUNAS' | 'BATAL' | 'RETUR'
    status_pembayaran VARCHAR(20) NOT NULL DEFAULT 'BELUM LUNAS' COMMENT 'Status keuangan tagihan belanja nota | Nilai valid: \'LUNAS\' | \'BELUM LUNAS\' | \'BATAL\' | \'RETUR\'',
    -- Nilai valid: 'DIAMBIL' | 'BELUM DIAMBIL'
    status_pengambilan VARCHAR(20) NOT NULL DEFAULT 'BELUM DIAMBIL' COMMENT 'Status serah terima barang fisik pesanan | Nilai valid: \'DIAMBIL\' | \'BELUM DIAMBIL\'',
    -- Nilai valid: 'Kas' | 'QRIS' | 'Transfer'
    metode_pembayaran VARCHAR(20) NOT NULL DEFAULT 'Kas' COMMENT 'Saluran pembayaran (Tunai kasir vs bank/qris) | Nilai valid: \'Kas\' | \'QRIS\' | \'Transfer\'',
    -- Nilai valid: 'Retail' | 'Grosir' | 'Mitra'
    tipe_pelanggan VARCHAR(20) NOT NULL DEFAULT 'Retail' COMMENT 'Tipe klasifikasi tarif keanggotaan pelanggan | Nilai valid: \'Retail\' | \'Grosir\' | \'Mitra\'',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Identifikasi cabang tempat kasir mencatat nota',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_transaksi_total_bayar CHECK (total_bayar >= 0),
    CONSTRAINT chk_transaksi_dp_bayar CHECK (dp_bayar >= 0 AND dp_bayar <= total_bayar),
    CONSTRAINT fk_transaksi_pelanggan_id FOREIGN KEY (pelanggan_id) REFERENCES pelanggan(id) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT fk_transaksi_kasir_id FOREIGN KEY (kasir_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_transaksi_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Header pencatatan penjualan kasir (multi-metode) | Sensitivitas: Sensitif | Modul: M.1';

-- ------------------------------------------------------------
-- [TABEL 11] detail_transaksi
-- ------------------------------------------------------------
CREATE TABLE detail_transaksi (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik rincian item nota',
    transaksi_id INT NOT NULL COMMENT 'Keterkaitan nota header transaksi induk',
    barang_id INT NOT NULL COMMENT 'Referensi item barang dagangan / jasa cetak',
    kuantitas DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Jumlah item barang belanjaan yang dipesan',
    harga_jual DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Tarif harga per unit terpilih di kasir',
    subtotal DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Total biaya baris belanja: kuantitas * harga',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang transaksi dari rincian nota ini',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_detail_transaksi_transaksi_id FOREIGN KEY (transaksi_id) REFERENCES transaksi(id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_detail_transaksi_barang_id FOREIGN KEY (barang_id) REFERENCES barang(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_detail_transaksi_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Baris rincian barang/jasa belanja nota | Sensitivitas: Operasional | Modul: M.1';

-- ------------------------------------------------------------
-- [TABEL 12] antrian_kerja
-- ------------------------------------------------------------
CREATE TABLE antrian_kerja (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik baris antrian',
    transaksi_id INT NOT NULL COMMENT 'Referensi transaksi nota penjualan kustom',
    desainer_id INT NULL DEFAULT NULL COMMENT 'Staf desainer pembuat layout gambar desain',
    produksi_id INT NULL DEFAULT NULL COMMENT 'Staf operator cetak pelaksana cetak fisik',
    -- Nilai valid: 'Antri' | 'Proses Desain' | 'Produksi' | 'Selesai' | 'Diambil'
    status_antrian VARCHAR(30) NOT NULL DEFAULT 'Antri' COMMENT 'Tahap penyelesaian pengerjaan produk kustom | Nilai valid: \'Antri\' | \'Proses Desain\' | \'Produksi\' | \'Selesai\' | \'Diambil\'',
    path_desain VARCHAR(255) NOT NULL DEFAULT '' COMMENT 'Direktori penyimpanan berkas PDF desain di server',
    timestamp_antri TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu pertama masuk antrian cetak kasir',
    timestamp_selesai TIMESTAMP NULL DEFAULT NULL COMMENT 'Waktu rampung cetak fisik produk oleh produksi',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Identifikasi cabang tempat pengerjaan antrian',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_antrian_kerja_transaksi_id FOREIGN KEY (transaksi_id) REFERENCES transaksi(id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_antrian_kerja_desainer_id FOREIGN KEY (desainer_id) REFERENCES pengguna(id) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT fk_antrian_kerja_produksi_id FOREIGN KEY (produksi_id) REFERENCES pengguna(id) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT fk_antrian_kerja_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Alur tracking produksi cetak kustom | Sensitivitas: Operasional | Modul: M.5';

-- ------------------------------------------------------------
-- [TABEL 13] absensi
-- ------------------------------------------------------------
CREATE TABLE absensi (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik baris data kehadiran harian',
    pengguna_id INT NOT NULL COMMENT 'Referensi pengguna staf yang diabsen',
    tanggal DATE NOT NULL COMMENT 'Tanggal hari kerja pencatatan kehadiran',
    -- Nilai valid: 'Hadir' | 'Izin' | 'Sakit' | 'Alpha'
    status_kehadiran VARCHAR(20) NOT NULL DEFAULT 'Hadir' COMMENT 'Kategori status absen staf harian | Nilai valid: \'Hadir\' | \'Izin\' | \'Sakit\' | \'Alpha\'',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Unit cabang lokasi staf melakukan absensi',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT uq_absensi_pengguna_tanggal UNIQUE (pengguna_id, tanggal),
    CONSTRAINT fk_absensi_pengguna_id FOREIGN KEY (pengguna_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_absensi_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Pencatatan kehadiran harian staf | Sensitivitas: Operasional | Modul: M.4';

-- ------------------------------------------------------------
-- [TABEL 14] kasbon
-- ------------------------------------------------------------
CREATE TABLE kasbon (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik pengajuan kasbon staf',
    pengguna_id INT NOT NULL COMMENT 'Referensi staf penerima utang kasbon',
    nominal_pinjaman DECIMAL(15,4) NOT NULL COMMENT 'Nominal penarikan awal pinjaman kasbon staf',
    sisa_utang DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Saldo utang kasbon aktif yang belum terbayar',
    cicilan_per_bulan DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Nominal auto-debit cicilan gaji staf per bulan',
    tanggal_pinjam DATE NOT NULL COMMENT 'Tanggal dilakukannya pencairan dana kasbon',
    -- Nilai valid: 'AKTIF' | 'LUNAS'
    status_kasbon VARCHAR(20) NOT NULL DEFAULT 'AKTIF' COMMENT 'Keabsahan status saldo utang kasbon aktif | Nilai valid: \'AKTIF\' | \'LUNAS\'',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang penyedia alokasi kas laci untuk kasbon',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_kasbon_nominal_pinjaman CHECK (nominal_pinjaman > 0),
    CONSTRAINT chk_kasbon_sisa_utang CHECK (sisa_utang >= 0 AND sisa_utang <= nominal_pinjaman),
    CONSTRAINT chk_kasbon_cicilan_per_bulan CHECK (cicilan_per_bulan >= 0),
    CONSTRAINT fk_kasbon_pengguna_id FOREIGN KEY (pengguna_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_kasbon_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Saldo utang internal kasbon karyawan (cicilan) | Sensitivitas: Operasional | Modul: M.4';

-- ------------------------------------------------------------
-- [TABEL 15] payroll
-- ------------------------------------------------------------
CREATE TABLE payroll (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik data slip gaji',
    pengguna_id INT NOT NULL COMMENT 'Referensi karyawan penerima pembayaran gaji',
    bulan_tahun VARCHAR(7) NOT NULL COMMENT 'Periode komputasi gaji (Format: MM-YYYY)',
    gaji_pokok DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Upah pokok/proporsional terhitung kinerja',
    bonus_insentif DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Tambahan nominal uang komisi poin terkumpul',
    potongan_kasbon DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Nilai potongan pelunasan sisa utang kasbon',
    gaji_bersih DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Nominal bersih yang diterima: Pokok + Bonus - Potongan',
    -- Nilai valid: 'Tunai' | 'Transfer'
    metode_bayar_gaji VARCHAR(20) NOT NULL DEFAULT 'Tunai' COMMENT 'Saluran pembayaran (Tunai laci vs transfer bank) | Nilai valid: \'Tunai\' | \'Transfer\'',
    tanggal_proses TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu pencetakan dan pemrosesan slip payroll',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang penanggung jawab pengeluaran gaji',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_payroll_gaji_pokok CHECK (gaji_pokok >= 0),
    CONSTRAINT chk_payroll_bonus_insentif CHECK (bonus_insentif >= 0),
    CONSTRAINT chk_payroll_potongan_kasbon CHECK (potongan_kasbon >= 0),
    CONSTRAINT chk_payroll_gaji_bersih CHECK (gaji_bersih >= 0),
    CONSTRAINT fk_payroll_pengguna_id FOREIGN KEY (pengguna_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_payroll_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Perhitungan slip gaji bulanan staf (Smart Payroll) | Sensitivitas: Sangat Sensitif | Modul: M.4';

-- ------------------------------------------------------------
-- [TABEL 16] pengeluaran
-- ------------------------------------------------------------
CREATE TABLE pengeluaran (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik pengeluaran operasional',
    -- Nilai valid: 'Rutin' | 'Tak_Terduga' | 'Depresiasi' | 'Limbah'
    tipe_pengeluaran VARCHAR(30) NOT NULL COMMENT 'Pengelompokan jenis pembebanan biaya | Nilai valid: \'Rutin\' | \'Tak_Terduga\' | \'Depresiasi\' | \'Limbah\'',
    nominal DECIMAL(15,4) NOT NULL COMMENT 'Besaran nilai nominal uang kas keluar',
    deskripsi TEXT NOT NULL COMMENT 'Rincian detail tujuan/kebutuhan biaya operasional',
    tanggal_pengeluaran DATE NOT NULL COMMENT 'Tanggal dilakukannya pencatatan biaya keluar',
    kasir_id INT NOT NULL COMMENT 'Staf kasir penginput atau pemilik penyetuju',
    disetujui_pemilik BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'Flag persetujuan khusus pengeluaran > threshold',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang pembeban kas keluar pengoperasian',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_pengeluaran_nominal CHECK (nominal > 0),
    CONSTRAINT fk_pengeluaran_kasir_id FOREIGN KEY (kasir_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_pengeluaran_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Laporan beban biaya operasional toko | Sensitivitas: Sensitif | Modul: M.6';

-- ------------------------------------------------------------
-- [TABEL 17] limbah_produksi
-- ------------------------------------------------------------
CREATE TABLE limbah_produksi (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik log limbah produksi',
    transaksi_id INT NOT NULL COMMENT 'Nota transaksi pemesanan pemicu pengerjaan',
    bahan_baku_id INT NOT NULL COMMENT 'Referensi komponen bahan yang rusak/cacat',
    kuantitas_limbah DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Jumlah volume bahan baku yang rusak dibuang',
    alasan_kerusakan TEXT NOT NULL COMMENT 'Keterangan deskripsi penyebab kegagalan cetak',
    kerugian_nominal DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Nilai rupiah kerugian: qty limbah * harga beli',
    tanggal_pencatatan TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu penginputan laporan oleh operator',
    produksi_id INT NOT NULL COMMENT 'Operator produksi cetak pelapor insiden',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Unit cabang lokasi terjadinya limbah cetak',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_limbah_produksi_kuantitas_limbah CHECK (kuantitas_limbah > 0),
    CONSTRAINT chk_limbah_produksi_kerugian_nominal CHECK (kerugian_nominal >= 0),
    CONSTRAINT fk_limbah_produksi_transaksi_id FOREIGN KEY (transaksi_id) REFERENCES transaksi(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_limbah_produksi_bahan_baku_id FOREIGN KEY (bahan_baku_id) REFERENCES barang(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_limbah_produksi_produksi_id FOREIGN KEY (produksi_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_limbah_produksi_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Pencatatan sisa bahan baku gagal cetak | Sensitivitas: Sensitif | Modul: M.2';

-- ------------------------------------------------------------
-- [TABEL 18] jasa_service
-- ------------------------------------------------------------
CREATE TABLE jasa_service (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik penerimaan unit perbaikan',
    pelanggan_id INT NULL DEFAULT NULL COMMENT 'Keterkaitan pelanggan CRM terdaftar',
    nama_non_pelanggan VARCHAR(100) NULL DEFAULT NULL COMMENT 'Nama pelanggan umum jika bukan anggota CRM',
    nama_unit VARCHAR(100) NOT NULL COMMENT 'Merek dan tipe hardware unit (e.g. Epson L3110)',
    detail_kerusakan TEXT NOT NULL COMMENT 'Penjelasan keluhan gejala kerusakan hardware',
    estimasi_biaya DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Taksiran biaya servis dan pergantian sparepart',
    -- Nilai valid: 'Diterima' | 'Proses' | 'Selesai' | 'Diambil'
    status_perbaikan VARCHAR(30) NOT NULL DEFAULT 'Diterima' COMMENT 'Posisi tahap pemrosesan perbaikan unit | Nilai valid: \'Diterima\' | \'Proses\' | \'Selesai\' | \'Diambil\'',
    tanggal_diterima TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal unit diserahkan di konter pramuniaga',
    tanggal_selesai TIMESTAMP NULL DEFAULT NULL COMMENT 'Tanggal unit selesai diperbaiki oleh teknisi',
    teknisi_id INT NOT NULL COMMENT 'Karyawan berhak memproses perbaikan (Teknisi)',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang penampung fisik unit service masuk',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_jasa_service_estimasi_biaya CHECK (estimasi_biaya >= 0),
    CONSTRAINT fk_jasa_service_pelanggan_id FOREIGN KEY (pelanggan_id) REFERENCES pelanggan(id) ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT fk_jasa_service_teknisi_id FOREIGN KEY (teknisi_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_jasa_service_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Registrasi perbaikan laptop & printer | Sensitivitas: Operasional | Modul: M.3';

-- ------------------------------------------------------------
-- [TABEL 19] poin_insentif
-- ------------------------------------------------------------
CREATE TABLE poin_insentif (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik baris komisi poin staf',
    transaksi_id INT NOT NULL COMMENT 'Nota transaksi penjualan pemicu pemberian poin',
    pengguna_id INT NOT NULL COMMENT 'Karyawan penerima komisi bonus poin',
    poin_diperoleh INT NOT NULL DEFAULT 1 COMMENT 'Jumlah poin yang dikumpulkan dari 4-tier',
    rupiah_diperoleh DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Nominal Rupiah insentif (Poin * rupiah/poin)',
    tanggal_poin TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu pencatatan poin masuk ke sistem',
    -- Nilai valid: 'AKTIF' | 'BATAL'
    status_poin VARCHAR(20) NOT NULL DEFAULT 'AKTIF' COMMENT 'Validasi poin (dibatalkan jika nota diretur) | Nilai valid: \'AKTIF\' | \'BATAL\'',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang di mana insentif poin ini diterbitkan',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_poin_insentif_poin_diperoleh CHECK (poin_diperoleh > 0),
    CONSTRAINT chk_poin_insentif_rupiah_diperoleh CHECK (rupiah_diperoleh >= 0),
    CONSTRAINT fk_poin_insentif_transaksi_id FOREIGN KEY (transaksi_id) REFERENCES transaksi(id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_poin_insentif_pengguna_id FOREIGN KEY (pengguna_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_poin_insentif_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Agregasi bonus poin staf per transaksi | Sensitivitas: Operasional | Modul: M.4';

-- ------------------------------------------------------------
-- [TABEL 20] shift_handover
-- ------------------------------------------------------------
CREATE TABLE shift_handover (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik log serah terima shift',
    kasir_keluar_id INT NOT NULL COMMENT 'Karyawan kasir penutup shift yang keluar',
    kasir_masuk_id INT NOT NULL COMMENT 'Karyawan kasir pembuka shift berikutnya',
    kas_awal DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Saldo laci uang tunai pembuka shift kasir',
    kas_sistem DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Teori uang kasir kumulatif menurut kalkulasi',
    kas_fisik DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Uang tunai nyata yang dihitung di laci fisik',
    selisih DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Deviasi kasir: Kas Fisik - Kas Sistem',
    catatan_alasan TEXT NULL DEFAULT NULL COMMENT 'Alasan wajib dari kasir jika selisih > batas toleransi',
    timestamp_handover TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu serah terima shift kasir diselesaikan',
    -- Nilai valid: 'NORMAL' | 'ANOMALI'
    status_handover VARCHAR(20) NOT NULL DEFAULT 'NORMAL' COMMENT 'Indikator keabsahan selisih keuangan kasir | Nilai valid: \'NORMAL\' | \'ANOMALI\'',
    supervisor_id INT NOT NULL COMMENT 'Kepala Percetakan/Pemilik pemverifikasi silang',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang di mana serah terima shift diselenggarakan',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_shift_handover_kas_awal CHECK (kas_awal >= 0),
    CONSTRAINT chk_shift_handover_kas_sistem CHECK (kas_sistem >= 0),
    CONSTRAINT chk_shift_handover_kas_fisik CHECK (kas_fisik >= 0),
    CONSTRAINT fk_shift_handover_kasir_keluar_id FOREIGN KEY (kasir_keluar_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_shift_handover_kasir_masuk_id FOREIGN KEY (kasir_masuk_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_shift_handover_supervisor_id FOREIGN KEY (supervisor_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_shift_handover_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Log serah terima laci kas kasir | Sensitivitas: Sensitif | Modul: M.7';

-- ============================================================
-- KELOMPOK D: TABEL ADMINISTRASI & KEUANGAN
-- ============================================================

-- ------------------------------------------------------------
-- [TABEL 21] utang_supplier
-- ------------------------------------------------------------
CREATE TABLE utang_supplier (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik utang usaha supplier',
    supplier_id INT NOT NULL COMMENT 'Referensi vendor supplier pemberi tempo',
    nominal_utang DECIMAL(15,4) NOT NULL COMMENT 'Nominal tagihan pembelian bahan/ATK di awal',
    sisa_utang DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Sisa tagihan terutang yang wajib dibayarkan',
    tanggal_utang DATE NOT NULL COMMENT 'Tanggal dilakukannya transaksi nota supplier',
    tanggal_jatuh_tempo DATE NOT NULL COMMENT 'Batas tenggat pembayaran pelunasan utang',
    tanggal_pelunasan DATE NULL DEFAULT NULL COMMENT 'Waktu pembayaran pelunasan tagihan supplier (NULL jika belum)',
    -- Nilai valid: 'BELUM LUNAS' | 'LUNAS'
    status_utang VARCHAR(20) NOT NULL DEFAULT 'BELUM LUNAS' COMMENT 'Status pelunasan utang usaha tempo supplier | Nilai valid: \'BELUM LUNAS\' | \'LUNAS\'',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang pemilik pertanggungjawaban utang',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_utang_supplier_nominal_utang CHECK (nominal_utang > 0),
    CONSTRAINT chk_utang_supplier_sisa_utang CHECK (sisa_utang >= 0 AND sisa_utang <= nominal_utang),
    CONSTRAINT fk_utang_supplier_supplier_id FOREIGN KEY (supplier_id) REFERENCES supplier(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_utang_supplier_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Kewajiban utang tempo belanja supplier | Sensitivitas: Sensitif | Modul: M.2';

-- ------------------------------------------------------------
-- [TABEL 22] pinjaman_bank
-- ------------------------------------------------------------
CREATE TABLE pinjaman_bank (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik kredit bank terdaftar',
    -- Nilai valid: 'Bank_BRI' | 'Bank_Mandiri'
    tipe_bank VARCHAR(50) NOT NULL COMMENT 'Nama perbankan penyedia plafon kredit usaha | Nilai valid: \'Bank_BRI\' | \'Bank_Mandiri\'',
    plafon_nominal DECIMAL(15,4) NOT NULL DEFAULT 50000000.0000 COMMENT 'Besaran dana nominal cair pinjaman di awal',
    bunga_persen DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Suku bunga tetap pertahun (format desimal persen)',
    tenor_bulan INT NOT NULL COMMENT 'Total masa jangka waktu kredit (tenor) bulan',
    sisa_tenor_bulan INT NOT NULL COMMENT 'Sisa cicilan tenor yang belum dibayarkan',
    setoran_bulanan DECIMAL(15,4) NOT NULL COMMENT 'Kewajiban nominal setor cicilan rutin per bulan',
    sisa_utang DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Kewajiban nominal utang bank total yang tersisa',
    tanggal_mulai DATE NOT NULL COMMENT 'Tanggal disetujui/cairnya pinjaman modal bank',
    tanggal_jatuh_tempo DATE NOT NULL COMMENT 'Tanggal jatuh tempo cicilan bulanan berikutnya',
    -- Nilai valid: 'BELUM LUNAS' | 'LUNAS'
    status_pinjaman VARCHAR(20) NOT NULL DEFAULT 'BELUM LUNAS' COMMENT 'Status pelunasan kredit utang komersial bank | Nilai valid: \'BELUM LUNAS\' | \'LUNAS\'',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang penanggung jawab pelunasan kredit bank',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_pinjaman_bank_plafon_nominal CHECK (plafon_nominal > 0),
    CONSTRAINT chk_pinjaman_bank_bunga_persen CHECK (bunga_persen >= 0),
    CONSTRAINT chk_pinjaman_bank_tenor_bulan CHECK (tenor_bulan > 0),
    CONSTRAINT chk_pinjaman_bank_sisa_tenor_bulan CHECK (sisa_tenor_bulan >= 0),
    CONSTRAINT chk_pinjaman_bank_setoran_bulanan CHECK (setoran_bulanan > 0),
    CONSTRAINT chk_pinjaman_bank_sisa_utang CHECK (sisa_utang >= 0),
    CONSTRAINT fk_pinjaman_bank_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Rekapitulasi utang berbunga bank komersil | Sensitivitas: Sangat Sensitif | Modul: M.6';

-- ------------------------------------------------------------
-- [TABEL 23] pinjaman_kerabat
-- ------------------------------------------------------------
CREATE TABLE pinjaman_kerabat (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik pinjaman kekeluargaan',
    nama_kerabat VARCHAR(100) NOT NULL COMMENT 'Nama kerabat/sahabat pemberi modal sosial',
    nominal_pinjaman DECIMAL(15,4) NOT NULL COMMENT 'Besaran nominal awal penarikan modal dipinjam',
    sisa_utang DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Saldo utang kerabat berjalan belum dipulihkan',
    tanggal_pinjam DATE NOT NULL COMMENT 'Tanggal pemilik menerima uang tunai modal',
    tanggal_pengembalian DATE NULL DEFAULT NULL COMMENT 'Target pengembalian modal sosial (bisa Null/fleksibel)',
    -- Nilai valid: 'BELUM LUNAS' | 'LUNAS'
    status_pinjaman VARCHAR(20) NOT NULL DEFAULT 'BELUM LUNAS' COMMENT 'Status pengembalian modal titipan kerabat | Nilai valid: \'BELUM LUNAS\' | \'LUNAS\'',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang penerima aliran modal kas masuk kerabat',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_pinjaman_kerabat_nominal_pinjaman CHECK (nominal_pinjaman > 0),
    CONSTRAINT chk_pinjaman_kerabat_sisa_utang CHECK (sisa_utang >= 0),
    CONSTRAINT fk_pinjaman_kerabat_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Rekapitulasi utang tanpa bunga kerabat | Sensitivitas: Sangat Sensitif | Modul: M.6';

-- ------------------------------------------------------------
-- [TABEL 24] aset
-- ------------------------------------------------------------
CREATE TABLE aset (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik inventaris aset tetap',
    nama_aset VARCHAR(100) NOT NULL COMMENT 'Nama komersial fisik aset operasional (e.g. Mesin Flash)',
    harga_perolehan DECIMAL(15,4) NOT NULL COMMENT 'Nominal modal awal untuk membeli aset tetap',
    tanggal_perolehan DATE NOT NULL COMMENT 'Tanggal dibelinya fisik aset tetap bersangkutan',
    masa_manfaat_bulan INT NOT NULL COMMENT 'Estimasi masa pakai optimal aset (dalam bulan)',
    sisa_masa_manfaat_bulan INT NOT NULL COMMENT 'Sisa bulan optimal depresiasi tersisa',
    depresiasi_bulanan DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Beban depresiasi: harga_perolehan / masa_manfaat',
    nilai_buku_saat_ini DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Nilai bersih buku aset terhitung depresiasi',
    alokasi_tabungan_bulanan DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Nilai rupiah setoran laba bulanan untuk mesin baru',
    saldo_tabungan_virtual DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Total akumulasi kas tabungan virtual pengadaan',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang penanggung jawab operasional aset',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_aset_harga_perolehan CHECK (harga_perolehan > 0),
    CONSTRAINT chk_aset_masa_manfaat_bulan CHECK (masa_manfaat_bulan > 0),
    CONSTRAINT chk_aset_sisa_masa_manfaat_bulan CHECK (sisa_masa_manfaat_bulan >= 0),
    CONSTRAINT chk_aset_depresiasi_bulanan CHECK (depresiasi_bulanan >= 0),
    CONSTRAINT chk_aset_nilai_buku_saat_ini CHECK (nilai_buku_saat_ini >= 0),
    CONSTRAINT chk_aset_alokasi_tabungan_bulanan CHECK (alokasi_tabungan_bulanan >= 0),
    CONSTRAINT chk_aset_saldo_tabungan_virtual CHECK (saldo_tabungan_virtual >= 0),
    CONSTRAINT fk_aset_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Depresiasi & tabungan pengadaan aset tetap | Sensitivitas: Sangat Sensitif | Modul: M.6';

-- ============================================================
-- KELOMPOK E: TABEL AUDIT & REKONSILIASI
-- ============================================================

-- ------------------------------------------------------------
-- [TABEL 25] audit_logs
-- ------------------------------------------------------------
CREATE TABLE audit_logs (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik log peristiwa sistem',
    pengguna_id INT NOT NULL COMMENT 'Akun pengguna kasir/staf pelaksana aksi',
    action_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu presisi detik terjadinya aksi manipulasi',
    -- Nilai valid: 'INSERT' | 'UPDATE' | 'DELETE' | 'ACCESS_DENIED'
    action_type VARCHAR(20) NOT NULL COMMENT 'Klasifikasi tipe modifikasi manipulasi basis data | Nilai valid: \'INSERT\' | \'UPDATE\' | \'DELETE\' | \'ACCESS_DENIED\'',
    target_table VARCHAR(100) NOT NULL COMMENT 'Nama tabel database yang diubah nilainya',
    old_value JSON NULL DEFAULT NULL COMMENT 'Salinan data record sebelum terjadinya perubahan',
    new_value JSON NULL DEFAULT NULL COMMENT 'Salinan data record sesudah terjadinya perubahan',
    ip_address VARCHAR(45) NULL DEFAULT NULL COMMENT 'Alamat IP client terminal yang memicu peristiwa',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang di mana insiden log audit ini dipicu',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_audit_logs_pengguna_id FOREIGN KEY (pengguna_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_audit_logs_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Catatan log kronologis modifikasi data (FK pengguna) | Sensitivitas: Sensitif | Modul: M.7';

-- ------------------------------------------------------------
-- [TABEL 26] backup_logs
-- ------------------------------------------------------------
CREATE TABLE backup_logs (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik log pencadangan',
    tanggal_backup TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu dilaksanakannya proses ekspor ZIP',
    nama_file VARCHAR(100) NOT NULL COMMENT 'Nama fisik file output format ZIP AES-256',
    -- Nilai valid: 'SUCCESS' | 'FAILED'
    status_backup VARCHAR(20) NOT NULL COMMENT 'Hasil eksekusi skrip dump basis data | Nilai valid: \'SUCCESS\' | \'FAILED\'',
    pengguna_id INT NOT NULL COMMENT 'Pengguna pemilik pemicu ekspor basis data',
    ukuran_file_kb BIGINT NOT NULL COMMENT 'Ukuran fisik file hasil backup dalam kilobyte (KB)',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang pelaksana backup dump data server',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_backup_logs_pengguna_id FOREIGN KEY (pengguna_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_backup_logs_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Log pencadangan data manual terenkripsi (FK pengguna) | Sensitivitas: Sangat Sensitif | Modul: M.2';

-- ------------------------------------------------------------
-- [TABEL 27] stock_opname
-- ------------------------------------------------------------
CREATE TABLE stock_opname (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik baris Stock Opname',
    barang_id INT NOT NULL COMMENT 'Referensi item barang dagangan yang direkonsiliasi',
    stok_sistem DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Saldo sisa persediaan menurut data database',
    kuantitas_fisik DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Saldo sisa persediaan riil hitungan fisik di toko',
    selisih DECIMAL(15,4) NOT NULL DEFAULT 0.0000 COMMENT 'Deviasi: kuantitas_fisik - stok_sistem',
    tanggal_opname TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu dilakukannya proses penguncian opname',
    catatan_opname TEXT NULL DEFAULT NULL COMMENT 'Catatan alasan selisih stok (e.g. barang rusak)',
    -- Nilai valid: 'DRAFT' | 'APPROVED'
    status_opname VARCHAR(20) NOT NULL DEFAULT 'DRAFT' COMMENT 'Kedudukan data persetujuan supervisor | Nilai valid: \'DRAFT\' | \'APPROVED\'',
    pengguna_id INT NOT NULL COMMENT 'Karyawan pelaksana perhitungan fisik (Gudang)',
    supervisor_id INT NULL DEFAULT NULL COMMENT 'Kepala Percetakan/Pemilik penyetuju penyesuaian',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang pelaksana opname gudang bersangkutan',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT fk_stock_opname_barang_id FOREIGN KEY (barang_id) REFERENCES barang(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_stock_opname_pengguna_id FOREIGN KEY (pengguna_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_stock_opname_supervisor_id FOREIGN KEY (supervisor_id) REFERENCES pengguna(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_stock_opname_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Penyesuaian fisik stok sistem berkala (FK pengguna) | Sensitivitas: Sensitif | Modul: M.2';

-- ------------------------------------------------------------
-- [TABEL 28] riwayat_harga_supplier
-- ------------------------------------------------------------
CREATE TABLE riwayat_harga_supplier (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik baris riwayat harga supplier',
    barang_id INT NOT NULL COMMENT 'Referensi item barang/bahan baku yang dibeli',
    supplier_id INT NOT NULL COMMENT 'Referensi vendor supplier penyedia barang',
    harga_beli DECIMAL(15,4) NOT NULL COMMENT 'Nominal harga beli per unit yang disepakati baru',
    tanggal_pembelian DATE NOT NULL COMMENT 'Tanggal transaksi pengadaan barang masuk',
    cabang_id INT NOT NULL DEFAULT 1 COMMENT 'Cabang pencatat nota pembelian inventaris masuk',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu baris data dibuat',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Tanggal & waktu terakhir baris data diperbarui',
    CONSTRAINT chk_riwayat_harga_supplier_harga_beli CHECK (harga_beli > 0),
    CONSTRAINT fk_riwayat_harga_supplier_barang_id FOREIGN KEY (barang_id) REFERENCES barang(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_riwayat_harga_supplier_supplier_id FOREIGN KEY (supplier_id) REFERENCES supplier(id) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_riwayat_harga_supplier_cabang_id FOREIGN KEY (cabang_id) REFERENCES cabang(id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci 
  COMMENT='Pelacakan fluktuasi harga beli pengadaan | Sensitivitas: Operasional | Modul: M.2';

-- ============================================================
-- BAGIAN 3 — PEMBUATAN INDEX TAMBAHAN (CREATE INDEX)
-- ============================================================
CREATE INDEX idx_transaksi_tanggal_cabang ON transaksi(tanggal_transaksi, cabang_id);
CREATE INDEX idx_absensi_pengguna_tanggal ON absensi(pengguna_id, tanggal);
CREATE INDEX idx_antrian_status_cabang ON antrian_kerja(status_antrian, cabang_id);
CREATE INDEX idx_barang_tipe_cabang ON barang(tipe_barang, cabang_id);

-- ============================================================
-- BAGIAN 4 — DATA SEED AWAL (INSERT INTO)
-- ============================================================

-- Seed cabang default (Toko Pusat Bandung)
INSERT INTO cabang (id, nama_cabang, alamat, telp) 
VALUES (1, 'Toko Pusat Bandung', 'Jl. Raya Percetakan No. 45, RT 02/RW 03, Kecamatan Sukamaju, Kota Bandung, Jawa Barat, 40123', '0227654321');

-- Seed pengguna default (akun pemilik)
INSERT INTO pengguna (id, nama_lengkap, username, password_hash, role, failed_login_attempts, locked_until, cabang_id) 
VALUES (1, 'Pemilik Usaha AbuCom', 'pemilik', '$2b$12$K3h8jD8sS9fJ2gK3l8h9oOa8fS8jK9l8g7h6j5k4l3m2n1o0p9q8r', 'pemilik', 0, NULL, 1); /* Placeholder otentikasi bcrypt untuk seed data */

-- Seed saldo_ppob (2 akun PPOB)
INSERT INTO saldo_ppob (akun_tipe, saldo_terakhir, cabang_id) 
VALUES 
('Pulsa_Data', 1000000.0000, 1),
('Token_Tagihan', 1500000.0000, 1);

-- Seed saldo_ewallet (6 akun e-wallet)
INSERT INTO saldo_ewallet (nama_ewallet, saldo_terakhir, biaya_admin_flat, biaya_admin_persen, limit_harian, cabang_id) 
VALUES 
('Mandiri Agen', 2000000.0000, 3000.0000, 0.0000, 50000000.0000, 1),
('Dana', 1000000.0000, 1000.0000, 0.0000, 10000000.0000, 1),
('Gopay', 1000000.0000, 1000.0000, 0.0000, 10000000.0000, 1),
('LinkAja', 1000000.0000, 1000.0000, 0.0000, 10000000.0000, 1),
('ShopeePay', 1000000.0000, 1000.0000, 0.0000, 10000000.0000, 1),
('OVO', 1000000.0000, 1000.0000, 0.0000, 10000000.0000, 1);

-- Seed system_configs (13 parameter bisnis)
INSERT INTO system_configs (parameter_key, parameter_value, tipe_data, deskripsi, cabang_id) 
VALUES 
('target_laba_payroll', '15000000.0000', 'DECIMAL', 'Target laba bersih bulanan untuk skema gaji tetap (Skenario A Smart Payroll)', 1),
('porsi_gaji_laba', '0.2500', 'DECIMAL', 'Persentase alokasi laba bersih untuk pool gaji karyawan (Skenario B Smart Payroll)', 1),
('limit_kasbon_staf', '1000000.0000', 'DECIMAL', 'Pagu maksimal utang kasbon aktif kumulatif per staf', 1),
('threshold_saldo_ppob', '150000.0000', 'DECIMAL', 'Batas saldo minimum PPOB yang memicu alert deposit', 1),
('min_topup_ppob', '500000.0000', 'DECIMAL', 'Nominal minimum deposit topup saldo PPOB', 1),
('toleransi_selisih_kas', '10000.0000', 'DECIMAL', 'Batas toleransi selisih kas kasir sebelum status ANOMALI', 1),
('poin_tier_1_rupiah', '500.0000', 'DECIMAL', 'Nilai rupiah per poin insentif Tier 1 (transaksi mudah)', 1),
('poin_tier_2_rupiah', '1500.0000', 'DECIMAL', 'Nilai rupiah per poin insentif Tier 2 (jasa dasar)', 1),
('poin_tier_3_rupiah', '2500.0000', 'DECIMAL', 'Nilai rupiah per poin insentif Tier 3 (produk kustom)', 1),
('poin_tier_4_rupiah', '5000.0000', 'DECIMAL', 'Nilai rupiah per poin insentif Tier 4 (pekerjaan berat/teknis)', 1),
('threshold_pengeluaran', '500000.0000', 'DECIMAL', 'Batas nominal pengeluaran yang memerlukan otorisasi pemilik', 1),
('umr_daerah', '3200000.0000', 'DECIMAL', 'Upah Minimum Regional daerah sebagai batas proteksi gaji minimum staf', 1),
('dana_cadangan_darurat', '4500000.0000', 'DECIMAL', 'Cadangan kas darurat minimal yang harus dijaga di laci kasir', 1);

-- ============================================================
-- BAGIAN 5 — VERIFIKASI INTEGRITAS
-- ============================================================
-- Hasil yang diharapkan: 28 tabel
SHOW TABLES;

-- Hasil yang diharapkan: 1
SELECT COUNT(*) AS total_cabang FROM cabang;

-- Hasil yang diharapkan: 1
SELECT COUNT(*) AS total_pengguna FROM pengguna;

-- Hasil yang diharapkan: 2
SELECT COUNT(*) AS total_saldo_ppob FROM saldo_ppob;

-- Hasil yang diharapkan: 6
SELECT COUNT(*) AS total_saldo_ewallet FROM saldo_ewallet;

-- Hasil yang diharapkan: 13
SELECT COUNT(*) AS total_system_configs FROM system_configs;

-- ============================================================
-- BAGIAN 6 — RESTORASI KONFIGURASI & FOOTER
-- ============================================================
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- ============================================================
-- REFERENSI DOKUMEN
-- ============================================================
-- File ini disusun berdasarkan referensi dari dokumen-dokumen berikut:
--
-- [REF-01] Data Dictionary v1.1
--          Path: docs/sdlc/02_analysis/05_data_dictionary.md
--          Kontribusi: Sumber utama definisi 28 tabel, 282 kolom, constraint,
--                      matriks FK, domain nilai, seed data, dan aturan bisnis.
--
-- [REF-02] Access Control Matrix v1.1
--          Path: docs/sdlc/02_analysis/06_access_control_matrix.md
--          Kontribusi: Klasifikasi tingkat sensitivitas tabel dan matriks CRUD.
--
-- [REF-03] Tech Stack Decision v1.1
--          Path: docs/sdlc/01_planning/04_tech_stack_decision.md
--          Kontribusi: Konfigurasi MySQL (engine, charset, collation) dan
--                      strategi inisialisasi schema.sql.
--
-- [REF-04] Software Requirements Specification v1.1
--          Path: docs/sdlc/02_analysis/02_software_requirements.md
--          Kontribusi: Cross-check kode kebutuhan fungsional (SRS-F-xxx).
--
-- [REF-05] Business Requirements Document v1.1
--          Path: docs/sdlc/02_analysis/01_business_requirements.md
--          Kontribusi: Cross-check aturan bisnis dan domain nilai (BR-F-xx).
-- ============================================================
