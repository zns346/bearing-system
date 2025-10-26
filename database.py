
import sqlite3
import os

DB_PATH = os.path.expanduser("~/bearing-system/backend/database/bearings.db")

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)
