from database import get_connection


def insert_bearing(
    category,
    bearing_type,
    bearing_sub_type,
    bearing_number,
    seals_shields,
    other_suffixes,
    make_application,
    generated_specification,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO bearings (
            category, bearing_type, bearing_sub_type, bearing_number,
            seals_shields, other_suffixes, make_application, generated_specification
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            category,
            bearing_type,
            bearing_sub_type,
            bearing_number,
            seals_shields,
            other_suffixes,
            make_application,
            generated_specification,
        ),
    )

    conn.commit()
    conn.close()
    print("✅ Bearing record inserted successfully!")


def list_bearings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bearings ORDER BY id DESC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    insert_bearing(
        category="Bearing",
        bearing_type="Deep Groove Ball Bearing",
        bearing_sub_type="6200 Series",
        bearing_number="6205",
        seals_shields="OPEN",
        other_suffixes="TN9",
        make_application="Toyota SKF Front Wheel Hub",
        generated_specification="DEEP GROOVE BALL BEARING 6205",
    )

    print("\n📋 All Bearings in Database:")
    list_bearings()
