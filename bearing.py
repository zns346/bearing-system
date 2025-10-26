import sqlite3, os

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "database", "bearings.db")


def insert_bearing(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO bearings (
            category, bearing_type, bearing_sub_type, bearing_number,
            seals_shields, other_suffixes, make_application, generated_specification
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            data["category"],
            data["bearing_type"],
            data["bearing_sub_type"],
            data["bearing_number"],
            data["seals_shields"],
            data["other_suffixes"],
            data["make_application"],
            data["generated_specification"],
        ),
    )
    conn.commit()
    conn.close()
