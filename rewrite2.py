import re

with open('/home/nabila/Documents/abucom/docs/sdlc/06_deployment/03_release_notes.md', 'r') as f:
    content = f.read()

# Replace RBAC Table
old_table = """| Menu Administratif / Modul | pemilik | kepala_percetakan | kasir | desainer | produksi_cetak | gudang | pramuniaga | fotocopy_print |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Modal, Tabungan & Pinjaman Bank** | **X** | — | — | — | — | — | — | — |
| **Smart Payroll Penggajian & Config** | **X** | — | — | — | — | — | — | — |
| **Persetujuan Stock Opname Gudang** | **X** | **X** | — | — | — | — | — | — |
| **Persetujuan Selisih Kasir > Rp 10rb**| **X** | **X** | — | — | — | — | — | — |
| **Manajemen Gudang & Input Supplier**| **X** | **X** | — | — | — | **X** | — | — |
| **Absensi Harian Karyawan** | **X** | **X** | **X** | **X** | **X** | **X** | **X** | **X** |
| **Kasir Nota Transaksi, Bayar & DP** | **X** | — | **X** | — | — | — | **X** | — |
| **Job Tracking Antrian Desain & Path**| **X** | **X** | — | **X** | — | — | **X** | — |
| **Job Tracking Produksi & Limbah** | **X** | **X** | — | — | **X** | — | — | — |
| **Pencatatan Ritel Fotokopi/Print** | **X** | **X** | **X** | — | — | — | **X** | **X** |"""

new_table = """| Menu Administratif / Modul | pemilik | kepala_percetakan | kasir | desainer | produksi_cetak | gudang | pramuniaga | fotocopy_print |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Modal, Tabungan & Pinjaman Bank** | **X** | — | — | — | — | — | — | — |
| **Smart Payroll Penggajian & Config** | **X** | — | — | — | — | — | — | — |
| **Otorisasi Retur & Batal Transaksi** | **X** | — | 🔐 | — | — | — | — | — |
| **Persetujuan Stock Opname Gudang** | **X** | **X** | — | — | — | — | — | — |
| **Persetujuan Selisih Kasir > Rp 10rb**| **X** | **X** | — | — | — | — | — | — |
| **Manajemen Gudang & Input Supplier**| **X** | **X** | — | — | — | **X** | — | — |
| **Absensi Harian Karyawan** | **X** | **X** | **X** | **X** | **X** | **X** | **X** | **X** |
| **Kasir Nota Transaksi, Bayar & DP** | **X** | — | **X** | — | — | — | **X** | — |
| **Job Tracking Antrian Desain & Path**| **X** | **X** | — | **X** | — | — | **X** | — |
| **Job Tracking Produksi & Limbah** | **X** | **X** | — | — | **X** | — | — | — |
| **Pencatatan Ritel Fotokopi/Print** | **X** | **X** | **X** | — | — | — | **X** | **X** |

*(Catatan: 🔐 menandakan bahwa eksekusi fungsi oleh peran tersebut mewajibkan verifikasi/eskalasi kata sandi pemilik di terminal)*"""

content = content.replace(old_table, new_table)

with open('/home/nabila/Documents/abucom/docs/sdlc/06_deployment/03_release_notes.md', 'w') as f:
    f.write(content)

print("Rewrite 2 successful.")
