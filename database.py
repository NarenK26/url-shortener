import sqlite3
DATABASE_NAME = "urls.db"

def create_database():
    conn = sqlite3.connect(DATABASE_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            short_code TEXT PRIMARY KEY,
            original_url TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_url(short_code: str, original_url: str):
    conn = sqlite3.connect(DATABASE_NAME)

    conn.execute(
        "INSERT INTO urls (short_code, original_url) VALUES (?, ?)",
        (short_code, original_url)
    )

    conn.commit()
    conn.close()


def get_url(short_code: str):
    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (short_code,)
    )

    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None