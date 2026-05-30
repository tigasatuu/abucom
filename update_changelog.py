import re

with open("docs/sdlc/07_maintenance/02_changelog.md", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update metadata
text = text.replace("versi      : 1.1", "versi      : 1.2")
text = text.replace("tanggal    : 2026-05-28", "tanggal    : 2026-05-30")

# 2. Update Riwayat Perubahan
history_new = """| Versi | Tanggal    | Deskripsi Perubahan                                                                                              | Oleh                                                            |
|:---:|:---:|---|---|
| **1.2** | 2026-05-30 | Validasi dan sinkronisasi menyeluruh (v1.2) sesuai issue #0091: penyelarasan referensi dokumen SDLC (R-01 hingga R-14) ke versi 1.2, perbaikan penomoran kode SRS-F dari 015 hingga 040 (selaras dengan dokumen SRS v1.2), penambahan kategori "Diperbaiki (Fixed)" yang memuat 5 perbaikan cacat (*Closed*) dari Bug Report Template, penghapusan dependensi *cryptography* pada kategori Infrastruktur yang tidak selaras dengan TSD (R-13), serta standarisasi istilah asing ke bahasa Indonesia baku. | AI Developer & SDLC Auditor |
| **1.1**"""
text = text.replace("| Versi | Tanggal    | Deskripsi Perubahan                                                                                              | Oleh                                                            |\n|:---:|:---:|---|---|\n| **1.1**", history_new)

# 3. Update references in Section 1.4
text = text.replace("Release Notes v1.1", "Release Notes v1.2")
text = text.replace("Maintenance Guide v1.1", "Maintenance Guide v1.2")
text = text.replace("Git Workflow v1.1", "Git Workflow v1.2")
text = text.replace("Project Charter v1.1", "Project Charter v1.2")
text = text.replace("Software Requirements Spec v1.1", "Software Requirements Spec v1.2")

# 4. Update terms
text = text.replace("DevOps Support:", "Dukungan DevOps:")
text = text.replace("Tim Pengembang AI (Support):", "Tim Pengembang AI (Dukungan):")
text = text.replace("database MySQL", "basis data MySQL")
text = text.replace("Database Engine:", "Mesin Basis Data:")
text = text.replace("Connection Pooling:", "Pengumpulan Koneksi (Connection Pooling):")
text = text.replace("database relasional", "basis data relasional")
text = text.replace("di database", "di basis data")
text = text.replace("database transaksional", "basis data transaksional")
text = text.replace("database InnoDB", "basis data InnoDB")
text = text.replace("koneksi database", "koneksi basis data")

# 5. Fix Added SRS-F codes
srs_replacements = {
    "**[SRS-F-039]** Ditambahkan panel administrative pemilik untuk memicu backup database manual": "**[SRS-F-037]** Ditambahkan panel administratif pemilik untuk memicu pencadangan basis data manual",
    "**[SRS-F-040]** Ditambahkan pengelolaan profil data supplier": "**[SRS-F-015]** Ditambahkan pengelolaan profil data supplier",
    "**[SRS-F-015]** Ditambahkan pencatatan manual mutasi saldo": "**[SRS-F-016]** Ditambahkan pencatatan manual mutasi saldo",
    "**[SRS-F-016]** Ditambahkan fitur komparasi biaya admin": "**[SRS-F-017]** Ditambahkan fitur komparasi biaya admin",
    "**[SRS-F-017]** Ditambahkan pencatatan transaksi jasa service": "**[SRS-F-018]** Ditambahkan pencatatan transaksi jasa service",
    "**[SRS-F-018]** Ditambahkan pengelolaan database karyawan": "**[SRS-F-019]** Ditambahkan pengelolaan basis data karyawan",
    "**[SRS-F-019]** Ditambahkan komputasi payroll otomatis": "**[SRS-F-020]** Ditambahkan komputasi payroll otomatis",
    "**[SRS-F-020]** Ditambahkan sistem poin insentif otomatis": "**[SRS-F-021]** Ditambahkan sistem poin insentif otomatis",
    "**[SRS-F-021]** Ditambahkan pemotongan gaji bersih": "**[SRS-F-022]** Ditambahkan pemotongan gaji bersih",
    "**[SRS-F-022]** Ditambahkan dashboard antrian": "**[SRS-F-023]** Ditambahkan dashboard antrian",
    "**[SRS-F-023]** Ditambahkan penyimpanan string path": "**[SRS-F-024]** Ditambahkan penyimpanan string path",
    "**[SRS-F-024]** Ditambahkan pembuatan string pesan": "**[SRS-F-025]** Ditambahkan pembuatan string pesan",
    "**[SRS-F-025]** Ditambahkan pencatatan pinjaman": "**[SRS-F-026]** Ditambahkan pencatatan pinjaman",
    "**[SRS-F-026]** Ditambahkan kompilasi laporan Laba/Rugi": "**[SRS-F-027]** Ditambahkan kompilasi laporan Laba/Rugi",
    "**[SRS-F-027]** Ditambahkan notifikasi peringatan visual": "**[SRS-F-028]** Ditambahkan notifikasi peringatan visual",
    "**[SRS-F-028]** Ditambahkan pengelolaan aset tetap": "**[SRS-F-029]** Ditambahkan pengelolaan aset tetap",
    "**[SRS-F-029]** Ditambahkan pencatatan pengeluaran": "**[SRS-F-030]** Ditambahkan pencatatan pengeluaran",
    "**[SRS-F-030]** Ditambahkan proteksi otorisasi": "**[SRS-F-031]** Ditambahkan proteksi otorisasi",
    "**[SRS-F-031]** Ditambahkan audit trail kronologis": "**[SRS-F-032]** Ditambahkan audit trail kronologis",
    "**[SRS-F-032]** Ditambahkan log serah terima": "**[SRS-F-033]** Ditambahkan log serah terima",
    "**[SRS-F-033]** Ditambahkan rekonsiliasi kas harian": "**[SRS-F-034]** Ditambahkan rekonsiliasi kas harian",
    "**[SRS-F-034]** Ditambahkan sistem peringatan anomali": "**[SRS-F-035]** Ditambahkan sistem peringatan anomali",
    "**[SRS-F-035]** Ditambahkan antarmuka menu setup awal": "**[SRS-F-036]** Ditambahkan antarmuka menu setup awal",
    "**[SRS-F-036]** Ditambahkan database pelanggan": "**[SRS-F-038]** Ditambahkan basis data pelanggan",
    "**[SRS-F-037]** Ditambahkan arsitektur data multi-cabang": "**[SRS-F-039]** Ditambahkan arsitektur data multi-cabang",
    "**[SRS-F-038]** Ditambahkan sistem konfigurasi dinamis": "**[SRS-F-040]** Ditambahkan sistem konfigurasi dinamis"
}

for old, new in srs_replacements.items():
    text = text.replace(old, new)

# Move SRS-F-015 from M.2 to its correct position (it is currently placed in M.2 right under SRS-F-037 Backup)
# Actually, the original text had Supplier as SRS-F-040 at the bottom of M.2. It just became 015. So it should stay in M.2.
# Wait, M.2 should have Supplier as SRS-F-015, Backup as SRS-F-037. The order in M.2 is now: 007 to 015 and then 037.

# 6. Insert Fixed section
fixed_section = """
#### Diperbaiki (Fixed)
*   **[DEF-M1-001]** Diperbaiki validasi logika `if-else` pada fungsi pelunasan DP yang sebelumnya memproses pembayaran meskipun nominal kurang dari sisa tagihan. *(Modul M.1)*
*   **[DEF-SEC-001]** Diperbaiki celah keamanan *bypass* hak akses di mana peran desainer dapat memasuki menu Smart Payroll; perlindungan otorisasi RBAC Guard kini menolak akses secara mutlak. *(Modul M.7)*
*   **[DEF-DEC-001]** Diperbaiki pembulatan `float` yang memotong nilai depresiasi bulanan secara tekstual pada manajemen aset; kini menggunakan pembulatan presisi desimal `ROUND_HALF_UP`. *(Modul M.6)*
*   **[DEF-CLI-001]** Diperbaiki galat perenderan tata letak garis pembatas (divider) pada nota struk thermal yang sebelumnya terpotong pada lebar 31 karakter menjadi tepat 32 karakter. *(Modul M.1)*
*   **[DEF-DB-001]** Diperbaiki anomali inkonsistensi stok saat koneksi LAN terputus (ACID *rollback failure*) dengan menerapkan autocommit = False pada koneksi *connection pool*. *(Modul M.2)*
"""

text = text.replace("#### Keamanan (Security)\n*   **Kriptografi Kata Sandi", fixed_section + "\n#### Keamanan (Security)\n*   **Kriptografi Kata Sandi")

# 7. Infrastructure and Security updates
text = text.replace("disandi biner **Fernet (cryptography)** 32-byte Base64 key", "disandi biner **Fernet** dengan kunci 32-byte Base64")
text = text.replace("Backup Terenkripsi", "Pencadangan Terenkripsi")
text = text.replace("kripto `cryptography==42.0.5`, ", "")

# 8. Update all references in Documentation list from v1.1 to v1.2
import re
text = re.sub(r'v1\.1\b(?=.*`docs/sdlc)', 'v1.2', text)
text = text.replace("Daftar seluruh berkas dokumentasi formal SDLC AbuCom versi v1.1 yang disusun untuk rilis v1.0.0:", 
                    "Daftar seluruh berkas dokumentasi formal SDLC AbuCom versi v1.2 yang disusun untuk rilis v1.0.0:")

# Update Section 7 table
text = text.replace("Penyusunan berkas Changelog v1.1 didasarkan", "Penyusunan berkas Changelog v1.2 didasarkan")
text = re.sub(r'\|\s*1\.1\s*\|', '| 1.2 |', text)
text = re.sub(r'v1\.1(?=\s*\|)', 'v1.2', text)

with open("docs/sdlc/07_maintenance/02_changelog.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Changelog updated successfully.")
