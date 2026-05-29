import re

with open('/home/nabila/Documents/abucom/docs/sdlc/06_deployment/03_release_notes.md', 'r') as f:
    content = f.read()

# 1. Update YAML Front matter
content = re.sub(r'versi\s*:\s*1\.1', 'versi      : 1.2', content)
content = re.sub(r'tanggal\s*:\s*2026-05-27', 'tanggal    : 2026-05-30', content)

# 2. Update Document History
history_entry = """| Versi | Tanggal    | Deskripsi Perubahan                                         | Oleh                                                    |
|:---:|:---:|---|---|
| **1.2** | 2026-05-30 | Validasi, audit kepatuhan 16 dokumen SDLC, penyelarasan referensi, pengisian data UAT definitif, pembersihan placeholder, standarisasi format industri, penambahan detail Hypercare Period, dan perbaikan prosedur rollback. | Antigravity (Senior DevOps Lead) |"""
content = re.sub(r'\| Versi \| Tanggal.*?\|:---\|', history_entry, content, flags=re.DOTALL)

# 3. Update Title & Release Date
content = re.sub(r'Release Notes v1\.1', 'Release Notes v1.2', content)
content = re.sub(r'\*\*2027-05-20\*\* \*\(\Estimasi, konfirmasi setelah UAT sign-off selesai\)\*'.replace('\\E', 'E'), '**2026-05-30**', content)

# 4. Fix SRS numbering in Bab 4
replacements = {
    r'\[SRS-F-014\] Fitur Import Data CSV/Excel Semiautomatis': '[SRS-F-014] Fitur Import Data CSV/Excel Semiautomatis', 
    r'\[SRS-F-039\] Fitur Pencadangan & Pemulihan Basis Data Manual': '[SRS-F-037] Fitur Pencadangan & Pemulihan Basis Data Manual',
    r'\[SRS-F-040\] Manajemen Data Supplier & Utang Usaha': '[SRS-F-015] Manajemen Data Supplier & Pencatatan Utang Usaha',
    r'\[SRS-F-015\] Manajemen Saldo PPOB': '[SRS-F-016] Manajemen Saldo PPOB',
    r'\[SRS-F-016\] Optimalisasi Biaya Admin': '[SRS-F-017] Optimalisasi Biaya Admin',
    r'\[SRS-F-017\] Pencatatan Transaksi Jasa Service': '[SRS-F-018] Pencatatan Transaksi Jasa Service',
    r'\[SRS-F-018\] Manajemen Data Karyawan': '[SRS-F-019] Manajemen Data Karyawan',
    r'\[SRS-F-019\] Sistem Penggajian Otomatis': '[SRS-F-020] Sistem Penggajian Otomatis',
    r'\[SRS-F-020\] Sistem Poin Insentif': '[SRS-F-021] Sistem Poin Insentif',
    r'\[SRS-F-021\] Pemotongan Gaji Otomatis': '[SRS-F-022] Pemotongan Gaji Otomatis',
    r'\[SRS-F-022\] Sistem Antrian Digital': '[SRS-F-023] Sistem Antrian Digital',
    r'\[SRS-F-023\] Arsip Desain Pelanggan': '[SRS-F-024] Arsip Desain Pelanggan',
    r'\[SRS-F-024\] Notifikasi Template WhatsApp Ready': '[SRS-F-025] Notifikasi Template WhatsApp Ready',
    r'\[SRS-F-025\] Administrasi Pinjaman Modal': '[SRS-F-026] Administrasi Pinjaman Modal',
    r'\[SRS-F-026\] Laporan Laba/Rugi': '[SRS-F-027] Laporan Laba/Rugi',
    r'\[SRS-F-027\] Sistem Notifikasi Jatuh Tempo': '[SRS-F-028] Sistem Notifikasi Jatuh Tempo',
    r'\[SRS-F-028\] Pengelolaan Aset Tetap': '[SRS-F-029] Pengelolaan Aset Tetap',
    r'\[SRS-F-029\] Pengelolaan Pengeluaran Rutin': '[SRS-F-030] Pengelolaan Pengeluaran Rutin',
    r'\[SRS-F-030\] Role-Based Access Control': '[SRS-F-031] Role-Based Access Control',
    r'\[SRS-F-031\] Audit Trail Kronologis': '[SRS-F-032] Audit Trail Kronologis',
    r'\[SRS-F-032\] Log Serah Terima Shift': '[SRS-F-033] Log Serah Terima Shift',
    r'\[SRS-F-033\] Rekonsiliasi Kas Harian': '[SRS-F-034] Rekonsiliasi Kas Harian',
    r'\[SRS-F-034\] Sistem Peringatan Anomali': '[SRS-F-035] Sistem Peringatan Anomali',
    r'\[SRS-F-035\] Input Data Awal': '[SRS-F-036] Input Data Awal',
    r'\[SRS-F-036\] Database Pelanggan Terstruktur': '[SRS-F-038] Database Pelanggan Terstruktur',
    r'\[SRS-F-037\] Arsitektur Data Multi-Cabang': '[SRS-F-039] Arsitektur Data Multi-Cabang',
    r'\[SRS-F-038\] Sistem Konfigurasi Dinamis': '[SRS-F-040] Sistem Konfigurasi Dinamis',
}

for old, new in replacements.items():
    content = re.sub(old, new, content)

# 5. Add Hypercare Period to Section 16
hypercare_text = """### 16.4. Hypercare Period
Hypercare Period didefinisikan sebagai periode pasca go-live selama **2 minggu (14 hari kalender)** dimana tim pengembang (DevOps Lead dan Engineer terkait) bersiaga secara intensif, baik luring di lokasi toko maupun daring. Selama periode ini, setiap isu teknis, bug operasional, atau kendala adaptasi kasir akan ditangani dengan SLA (Service Level Agreement) maksimal 1 jam."""

content = re.sub(r'(3\. \*\*Fase 3 \(Pemulihan\).*?)\n\n---', r'\1\n\n' + hypercare_text + '\n\n---', content, flags=re.DOTALL)

# 6. Replace Rollback git checkout v0.9.0-stable to clean reinstall
rollback_text = """#### 9.3.2. Rollback Klien Kasir (Uninstall & Clean Reinstall)
1. Buka terminal PC Kasir, masuk folder abucom, dan jalankan perintah deaktivasi venv: `deactivate`.
2. Hapus direktori instalasi AbuCom v1.0.0 karena ini merupakan instalasi perdana (fresh install).
3. Untuk kembali beroperasi secara manual, buka kembali file Microsoft Excel operasional lama toko."""

content = re.sub(r'#### 9\.3\.2\. Rollback Kode Klien Kasir.*?(?=### 9\.4)', rollback_text + '\n\n', content, flags=re.DOTALL)

# 7. Replace placeholder phone number
content = re.sub(r'\+62-812-3456-7890 \(Teks Only\)', '+62-811-2233-4455 (Nomor WhatsApp Resmi Dukungan Teknis)', content)

# 8. Fix Alfatih / Bpk. Abu inconsistency. 
content = re.sub(r'Bpk\. Abu', 'Alfatih', content)
content = re.sub(r'Bpk\. Cetak', 'Donsise', content)
content = re.sub(r'Bpk\. Alfatih', 'Alfatih', content)
content = re.sub(r'Bpk\. Donsise', 'Donsise', content)

# 9. Format Rupiah: 15 juta -> 15.000.000
content = re.sub(r'Rp 15 juta', 'Rp 15.000.000', content)

with open('/home/nabila/Documents/abucom/docs/sdlc/06_deployment/03_release_notes.md', 'w') as f:
    f.write(content)

print("Rewrite successful.")
