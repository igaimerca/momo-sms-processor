import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
LOG_DIR = DATA_DIR / "logs"
DEAD_LETTER_DIR = LOG_DIR / "dead_letter"

DB_PATH = DATA_DIR / "db.sqlite3"
DASHBOARD_JSON = PROCESSED_DATA_DIR / "dashboard.json"

LOG_FILE = LOG_DIR / "etl.log"

TRANSACTION_CATEGORIES = {
    "transfer_out": ["transferred to", "sent to", "sent"],
    "transfer_in": ["received from", "you have received", "received"],
    "payment": ["payment of", "payment to", "paid to"],
    "purchase": ["data bundle", "airtime", "bundle", "purchase"],
    "other": []
}

AMOUNT_THRESHOLD_MIN = 0.01
AMOUNT_THRESHOLD_MAX = 1000000

PHONE_NUMBER_PATTERNS = [
    r"\+?\d{10,15}",
    r"0\d{9}",
]

