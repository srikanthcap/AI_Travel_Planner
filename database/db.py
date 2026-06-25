import sqlite3


def create_table():

    conn = sqlite3.connect("travel.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trips(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        destination TEXT,
        duration INTEGER,
        budget INTEGER,
        interests TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_trip(
    source,
    destination,
    duration,
    budget,
    interests
):

    conn = sqlite3.connect("travel.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO trips
        (
            source,
            destination,
            duration,
            budget,
            interests
        )
        VALUES
        (?, ?, ?, ?, ?)
        """,
        (
            source,
            destination,
            duration,
            budget,
            ",".join(interests)
        )
    )

    conn.commit()
    conn.close()
def get_all_trips():

    import sqlite3
    import pandas as pd

    conn = sqlite3.connect(
        "travel.db"
    )

    df = pd.read_sql_query(
        "SELECT * FROM trips",
        conn
    )

    conn.close()

    return df