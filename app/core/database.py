import sqlite3
from pathlib import Path

# Path to your database file
BASE_DIR = Path(__file__).resolve().parent.parent / "database"
DB_PATH = BASE_DIR / "bearings.db"


def get_connection():
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn
