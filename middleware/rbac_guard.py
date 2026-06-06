"""
Nama Modul: rbac_guard.py
Deskripsi: Interceptor otorisasi akses menu CLI berbasis matriks peran (RBAC).
           (Ref: Access Control Matrix Bab 3 & Module Structure Bab 7.3)
Author: GPT-OSS 120B (STK-014)
Tanggal: 2026-06-03
"""

from typing import Callable, Any
from functools import wraps

from middleware.auth_jwt import validate_session_token

# Matrix RBAC sesuai dengan Access Control Matrix (ACM) & Coding Standard
RBAC_MATRIX = {
    'pemilik': ['MENU-M1-001', 'MENU-M4-002', 'MENU-M7-002', 'MENU-M2-010', 'MENU-M10-001'],
    'kasir': ['MENU-M1-001', 'MENU-M1-003', 'MENU-M7-003'],
    'gudang': ['MENU-M2-001', 'MENU-M2-005', 'MENU-M2-009']
}


def check_menu_permission(menu_id: str, active_role: str) -> bool:
    """Memeriksa hak akses suatu peran terhadap Menu ID tertentu.

    Args:
        menu_id (str): Kode identifikasi menu CLI (contoh: MENU-M1-001).
        active_role (str): Peran aktif dari sesi pengguna.

    Returns:
        bool: True jika diizinkan, False jika ditolak.
    """
    return menu_id in RBAC_MATRIX.get(active_role, [])


def require_role(menu_id: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator fungsional pembungkus fungsi menu CLI untuk proteksi akses.

    Memeriksa keabsahan token JWT terlebih dahulu sebelum melakukan otorisasi
    berdasarkan Access Control Matrix (ACM).

    Args:
        menu_id (str): Kode identifikasi menu CLI yang diproteksi.

    Returns:
        Callable: Decorator fungsi untuk otorisasi akses menu.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(session_state: dict, *args, **kwargs) -> Any:
            # 1. Validasi token sesi JWT
            val_res = validate_session_token(session_state)
            if not val_res.is_success:
                print(f"⛔ {val_res.error_msg}")
                return None

            # 2. Cek otorisasi menu berdasarkan peran
            active_role = session_state.get('role', 'guest')
            if not check_menu_permission(menu_id, active_role):
                print("⛔ ERR-AUTH-003: Akses Ditolak.")
                return None
            return func(session_state, *args, **kwargs)
        return wrapper
    return decorator
