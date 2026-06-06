"""
Nama Modul: test_auth_login.py
Deskripsi: Unit testing untuk fungsi otentikasi password, hashing, dan JWT session.
Author: Antigravity (STK-015)
Tanggal: 2026-06-06
"""

import datetime
import unittest
from unittest.mock import patch

import jwt
from config.settings import AppConfig
from middleware.auth_jwt import hash_password, verify_password, create_jwt_session, verify_jwt_session

# Mock configuration settings for testing in isolation
MOCK_SETTINGS = AppConfig(
    app_env='development',
    app_cabang_id=1,
    db_host='127.0.0.1',
    db_port=3306,
    db_user='test_user',
    db_password='test_password',
    db_name='test_db',
    db_pool_size=5,
    jwt_secret_key='test_secret_key_minimum_32_characters_long_123',
    jwt_lifetime_seconds=3600,  # 1 hour for standard tests
    fernet_key='test_fernet_key_placeholder',
    backup_zip_password='test_backup_password',
    printer_port='COM1',
    printer_width_mm=58
)


class TestAuthLogin(unittest.TestCase):
    """Kelas pengujian unit untuk modul hashing, password verification, dan sesi JWT."""

    def test_hash_password_cost_factor(self):
        """Memastikan hasil hash menggunakan bcrypt dengan cost factor 12 (diawali $2b$12$)."""
        pw = "RahasiaSandi123!"
        hashed = hash_password(pw)
        self.assertTrue(hashed.startswith('$2b$12$'))

    def test_hash_password_dynamic_salt(self):
        """Memastikan hashing dua kali dengan password sama menghasilkan hash yang berbeda."""
        pw = "RahasiaSandi123!"
        hashed1 = hash_password(pw)
        hashed2 = hash_password(pw)
        self.assertNotEqual(hashed1, hashed2)

    def test_verify_password_correct(self):
        """Memastikan verifikasi password yang benar mengembalikan True."""
        pw = "SandiSaya99#"
        hashed = hash_password(pw)
        self.assertTrue(verify_password(pw, hashed))

    def test_verify_password_incorrect(self):
        """Memastikan verifikasi password yang salah mengembalikan False."""
        pw = "SandiSaya99#"
        hashed = hash_password(pw)
        self.assertFalse(verify_password("SandiSalah", hashed))

    def test_verify_password_empty(self):
        """Memastikan verifikasi password kosong mengembalikan False."""
        pw = "SandiSaya99#"
        hashed = hash_password(pw)
        self.assertFalse(verify_password("", hashed))

    @patch('middleware.auth_jwt.load_settings')
    def test_create_and_verify_jwt_session_success(self, mock_load_settings):
        """Memastikan token JWT dapat terbit dan terverifikasi dengan payload yang lengkap."""
        mock_load_settings.return_value = MOCK_SETTINGS

        token = create_jwt_session(
            user_id=1,
            username='kasir_andi',
            role='kasir',
            cabang_id=1
        )
        self.assertTrue(isinstance(token, str))
        self.assertGreater(len(token), 0)

        # Verifikasi token
        payload = verify_jwt_session(token)
        self.assertIsNotNone(payload)
        self.assertEqual(payload['user_id'], 1)
        self.assertEqual(payload['username'], 'kasir_andi')
        self.assertEqual(payload['role'], 'kasir')
        self.assertEqual(payload['cabang_id'], 1)
        self.assertIn('exp', payload)

    @patch('middleware.auth_jwt.load_settings')
    def test_verify_jwt_session_invalid(self, mock_load_settings):
        """Memastikan verifikasi token yang tidak valid/rusak mengembalikan None."""
        mock_load_settings.return_value = MOCK_SETTINGS

        invalid_token = "invalid.token.signature"
        payload = verify_jwt_session(invalid_token)
        self.assertIsNone(payload)

    @patch('middleware.auth_jwt.load_settings')
    def test_verify_jwt_session_expired(self, mock_load_settings):
        """Memastikan token yang kadaluwarsa mengembalikan None."""
        # Gunakan mock settings dengan lifetime negatif agar langsung expired
        expired_settings = MOCK_SETTINGS._replace(jwt_lifetime_seconds=-10)
        mock_load_settings.return_value = expired_settings

        token = create_jwt_session(
            user_id=1,
            username='kasir_andi',
            role='kasir',
            cabang_id=1
        )

        payload = verify_jwt_session(token)
        self.assertIsNone(payload)


if __name__ == '__main__':
    unittest.main()
