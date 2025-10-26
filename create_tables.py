import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "database", "bearings.db")

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)


def create_tables():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute(
        """
    CREATE TABLE IF NOT EXISTS bearings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        bearing_type TEXT,
        bearing_sub_type TEXT,
        bearing_number TEXT,
        seals_shields TEXT,
        other_suffixes TEXT,
        make_application TEXT,
        generated_specification TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print(f"✅ Database initialized at {DB_PATH}")
