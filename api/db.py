import os
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DB_PATH = Path(os.getenv("DB_PATH", str(BASE_DIR / "data" / "db.sqlite3")))

def get_db_connection():
    return sqlite3.connect(DB_PATH)

