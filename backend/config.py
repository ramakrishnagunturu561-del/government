# backend/config.py

import os

# =========================
# DATABASE CONFIGURATION
# =========================
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "mysqlkrishna@2005g",  # ✅ UPDATED PASSWORD
    "database": "welfare_system",
    "port": 3306
}

# =========================
# APP CONFIGURATION
# =========================
APP_CONFIG = {
    "DEBUG": True,
    "SECRET_KEY": "welfare-notification-secret-key"
}

# =========================
# VOICE / IVR CONFIGURATION
# =========================
VOICE_CALL_CONFIG = {
    "ENABLED": True,
    "PROVIDER": "DEMO",
    "CALLER_ID": "CM_KARYALAYAM"
}

# =========================
# EXOTEL CONFIGURATION (REAL VOICE CALLS)
# =========================
EXOTEL_CONFIG = {
    "SID": "YOUR_SID",
    "TOKEN": "YOUR_TOKEN", 
    "CALLER_ID": "040XXXXXXXX"
}

# =========================
# SCHEDULER CONFIGURATION
# =========================
SCHEDULER_CONFIG = {
    "ADVANCE_CALL_TIME": "17:00",
    "TIMEZONE": "Asia/Kolkata"
}

# =========================
# FILE UPLOAD CONFIGURATION
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {"xlsx", "xls"}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
