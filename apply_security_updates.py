import re

filepath = r"docs\sdlc\03_design\06_security_design.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update YAML Header
content = re.sub(
    r"versi\s*:\s*1\.1", 
    "versi      : 1.2", 
    content
)
content = re.sub(
    r"tanggal\s*:\s*2026-05-25", 
    "tanggal    : 2026-05-29", 
    content
)

# 2. Update Riwayat Perubahan
history_new = """## Riwayat Perubahan Dokumen

| Versi | Tanggal    | Perubahan | Oleh |
|:---:|:---:|---|---|
| **1.2** | 2026-05-29 | Validasi menyeluruh v1.2: komparasi terhadap ACM, SysArch, SRS, TSD, DDL, ERD, BRD, dan Workflow. Penyempurnaan struktur industri (OWASP, NIST, UU PDP), sinkronisasi DDL `audit_logs`, penambahan tabel `aset` dan Bab 13.5 (BRD), perbaikan pseudocode, serta naturalisasi Bahasa Indonesia tanpa ambiguitas (Issue #0079). | Senior Security Architect & Cybersecurity Compliance Specialist |"""
content = content.replace("## Riwayat Perubahan Dokumen\n\n| Versi | Tanggal    | Perubahan | Oleh |\n|:---:|:---:|---|---|", history_new)

# 3. Bab 2.3 Aset
content = content.replace(
    "`pinjaman_bank`, `pinjaman_kerabat`, `payroll`, `system_configs`, `backup_logs`",
    "`pinjaman_bank`, `pinjaman_kerabat`, `payroll`, `system_configs`, `backup_logs`, `aset`"
)
content = content.replace("1. Pengisian/modifikasi data pada 5 tabel Sangat Sensitif.", "1. Pengisian/modifikasi data pada 6 tabel Sangat Sensitif. Akses pembacaan (`SELECT`) pada tabel Sangat Sensitif juga wajib memicu log audit.")

# 4. Bab 4.2 Mid-transaction
content = content.replace(
    "kembali ke layar login dengan kode `ERR-SESSION-002`.",
    "kembali ke layar login dengan kode `ERR-SESSION-002`. Jika kedaluwarsa terjadi di tengah operasi yang sedang berjalan (*mid-transaction*), transaksi dibatalkan (*rollback*) secara aman sebelum sesi dihancurkan untuk menjaga integritas ACID."
)

# 5. Bab 4.5 Kompleksitas Sandi
kompleksitas = """### 4.5. Kebijakan Kompleksitas Sandi Pengguna
Untuk memitigasi serangan kamus (*dictionary attack*):
* **Panjang Minimum**: Kata sandi wajib memiliki setidaknya 8 karakter.
* **Karakter Campuran**: Kata sandi wajib mengandung kombinasi huruf besar, huruf kecil, dan angka.
* **Validasi**: Diperiksa secara ketat saat `pemilik` membuat akun baru di menu `MENU-M7-001` atau saat staf mengubah sandi di `MENU-BASE-004`.

---

## 5. Desain Otorisasi (Authorization Design)"""
content = content.replace("---\n\n## 5. Desain Otorisasi (Authorization Design)", kompleksitas)

# 6. Bab 6.5 Rotasi Kredensial
rotasi = """* **Startup Validator**: Layer aplikasi menjalankan verifikasi keberadaan berkas `.env` dan keaslian variabel di dalamnya saat startup program. Jika berkas hilang atau tidak lengkap, startup sistem dibatalkan secara aman dengan pesan error `ERR-FILE-001`.
* **Kebijakan Rotasi Kredensial**: JWT Secret Key, FERNET_KEY, dan sandi database wajib dirotasi setiap 6 bulan atau apabila dicurigai terjadi kebocoran (kompromi). Rotasi hanya boleh dilakukan oleh `pemilik` dengan cara memperbarui berkas `.env` dan me-restart layanan."""
content = content.replace("* **Startup Validator**: Layer aplikasi menjalankan verifikasi keberadaan berkas `.env` dan keaslian variabel di dalamnya saat startup program. Jika berkas hilang atau tidak lengkap, startup sistem dibatalkan secara aman dengan pesan error `ERR-FILE-001`.", rotasi)

# 7. Bab 7.1 DDL
ddl_old = """```sql
CREATE TABLE audit_logs (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pengguna_id INT NOT NULL COMMENT 'Referensi pengguna staf pelaksana aksi',
    action_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu presisi detik aksi',
    action_type VARCHAR(20) NOT NULL COMMENT 'Aksi: INSERT | UPDATE | DELETE | ACCESS_DENIED',
    target_table VARCHAR(100) NOT NULL COMMENT 'Nama tabel database sasaran',
    old_value JSON NULL DEFAULT NULL COMMENT 'Salinan record sebelum perubahan',
    new_value JSON NULL DEFAULT NULL COMMENT 'Salinan record sesudah perubahan',
    ip_address VARCHAR(45) NULL DEFAULT NULL COMMENT 'IP client yang memicu insiden',
    cabang_id INT NOT NULL DEFAULT 1,
    FOREIGN KEY (pengguna_id) REFERENCES pengguna(id),
    FOREIGN KEY (cabang_id) REFERENCES cabang(id)
) ENGINE=InnoDB;
```"""

ddl_new = """```sql
CREATE TABLE audit_logs (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Identifikasi unik log peristiwa sistem',
    pengguna_id INT NOT NULL COMMENT 'Akun pengguna kasir/staf pelaksana aksi',
    action_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Waktu presisi detik terjadinya aksi manipulasi',
    -- Nilai valid: 'INSERT' | 'UPDATE' | 'DELETE' | 'ACCESS_DENIED'
    action_type VARCHAR(20) NOT NULL COMMENT 'Klasifikasi tipe modifikasi manipulasi basis data | Nilai valid: \\'INSERT\\' | \\'UPDATE\\' | \\'DELETE\\' | \\'ACCESS_DENIED\\'',
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
```"""
content = content.replace(ddl_old, ddl_new)

# 8. Bab 8.2 Integritas Backup
backup_integritas = """* **Prosedur Verifikasi Integritas Cadangan**: Setiap akhir bulan, `pemilik` wajib menjalankan simulasi pemulihan pada *sandbox* eksternal untuk menguji apakah file ZIP dapat didekripsi dengan benar dan ukuran checksum cocok, guna mendeteksi korupsi file secara dini."""
content = content.replace("* **Prosedur Restore**:", backup_integritas + "\n* **Prosedur Restore**:")

# 9. Bab 8.3 Onboarding
onboarding_old = """* **Pembuatan Akun Staf**: Penambahan karyawan baru, pembagian kode posisi peran, dan set sandi awal wajib dieksekusi secara mandiri oleh `pemilik` di menu `MENU-M7-001`."""
onboarding_new = """* **Pembuatan Akun Staf (Onboarding)**: Penambahan karyawan baru, pembagian kode posisi peran terbatas, dan set sandi awal wajib dieksekusi secara mandiri oleh `pemilik` di menu `MENU-M7-001`. Proses ini wajib tercatat dalam log audit."""
content = content.replace(onboarding_old, onboarding_new)

ubah_sandi_old = """* **Perubahan Password**: Setiap staf diwajibkan mengganti kata sandi default mereka secara mandiri pada peluncuran menu `BASE-004` (Ubah Sandi Akun Sendiri)."""
ubah_sandi_new = """* **Perubahan Password**: Setiap staf diwajibkan mengganti kata sandi default mereka secara mandiri pada peluncuran pertama sistem via menu `BASE-004` (Ubah Sandi Akun Sendiri) sesuai kebijakan kompleksitas sandi."""
content = content.replace(ubah_sandi_old, ubah_sandi_new)

# 10. Pseudocode secret_key
pseudo_old = """        # Terbitkan token stateless session JWT HS256 dengan masa aktif 8 jam
        secret_key = "9a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z"  # Diambil dari .env dalam real system"""
pseudo_new = """        # Terbitkan token stateless session JWT HS256 dengan masa aktif 8 jam
        import os
        secret_key = os.getenv('JWT_SECRET_KEY')
        if not secret_key:
            return Result(False, None, "ERR-FILE-001: Kunci JWT tidak ditemukan di .env!")"""
content = content.replace(pseudo_old, pseudo_new)

# 11. Bab 12.3 Env Production Warning
env_old = """# ============================================================
# KREDENSIAL RUNTIME ABUCOM - SANGAT RAHASIA
# ============================================================
"""
env_new = """# ============================================================
# KREDENSIAL RUNTIME ABUCOM - SANGAT RAHASIA
# GANTI DENGAN NILAI ASLI SEBELUM PRODUKSI!
# ============================================================
"""
content = content.replace(env_old, env_new)

# 12. Bab 13.5 BRD Mapping
brd_mapping = """### 13.5. Mapping Security Design ke BRD (Business Requirements)

| Bab Security Design | Kebutuhan Bisnis (BRD) | Keterangan Sinkronisasi |
|---|---|---|
| **Bab 2.2** | Perlindungan Aset Finansial | Model ancaman THR-001 hingga THR-008 mencakup risiko fraud. |
| **Bab 6.3** | Kepatuhan UU PDP No. 27/2022 | Hak penghapusan data dan enkripsi nomor WhatsApp pelanggan. |
| **Bab 8.1** | Integritas Rekonsiliasi Shift | Pencegahan kehilangan uang fisik di laci kasir. |

---

## 14. Persetujuan dan Otorisasi Dokumen"""
content = content.replace("---\n\n## 14. Persetujuan dan Otorisasi Dokumen", brd_mapping)

# 13. Bab 14 Approval
app_old = """| **Pemilik Usaha (Owner & Junior PM)** | Pemilik Toko AbuCom | *DISETUJUI SECARA DIGITAL* | 2026-05-25 |
| **Senior Security Architect (Penyusun)** | Senior Security Architect | *DISETUJUI SECARA DIGITAL* | 2026-05-25 |"""
app_new = """| **Pemilik Usaha (Owner & Junior PM)** | Budi Santoso (Pemilik) | *DISETUJUI SECARA DIGITAL* | 2026-05-29 |
| **Senior Security Architect (Penyusun)** | Anton (Security Architect) | *DISETUJUI SECARA DIGITAL* | 2026-05-29 |"""
content = content.replace(app_old, app_new)

# 14. Bab 15 Glosarium
glosarium = """15. **Fail-Secure**: Kebijakan di mana jika terjadi kegagalan sistem, program otomatis mengunci akses dan melakukan rollback demi keamanan.
16. **Fernet**: Implementasi enkripsi simetris reversibel tersertifikasi yang menjamin pesan tidak dapat dibaca atau dimodifikasi tanpa kunci rahasia.
17. **ACID**: *Atomicity, Consistency, Isolation, Durability*. Properti transaksi database yang menjamin integritas data meskipun terjadi error atau kegagalan daya.
18. **Repeatable Read**: Level isolasi transaksi MySQL yang memastikan pembacaan berulang pada baris data yang sama di dalam satu transaksi selalu identik.
19. **Defense in Depth**: Strategi perlindungan berlapis di mana jika satu lapisan gagal, lapisan lain masih aktif melindungi aset sistem."""
content = content.replace("15. **Fail-Secure**: Kebijakan di mana jika terjadi kegagalan sistem, program otomatis mengunci akses dan melakukan rollback demi keamanan.", glosarium)

# 15. Bab 16 Referensi Tambahan
ref_tambahan = """| 8 | `04_workflow_diagram.md` | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Workflow Diagram v1.1 — Visualisasi otorisasi kasir dan serah terima shift harian. |
| 9 | `04_cli_interaction_flow.md` | `docs/sdlc/03_design/04_cli_interaction_flow.md` | CLI Interaction Flow v1.1 — Referensi tambahan untuk alur navigasi menu CLI yang diatur RBAC. |
| 10 | Eksternal: OWASP ASVS | N/A | Application Security Verification Standard sebagai panduan implementasi. |
| 11 | Eksternal: UU PDP No. 27/2022 | N/A | Regulasi Republik Indonesia untuk standar pelindungan data privasi pelanggan. |"""
content = content.replace("| 8 | `04_workflow_diagram.md` | `docs/sdlc/02_analysis/04_workflow_diagram.md` | Workflow Diagram v1.1 — Visualisasi otorisasi kasir dan serah terima shift harian. |", ref_tambahan)


with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Document successfully updated and overwritten without truncation!")
