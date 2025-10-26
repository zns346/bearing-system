from database import get_connection


def create_bearing_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
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
    print("✅ Bearings table created successfully!")


if __name__ == "__main__":
    create_bearing_table()
