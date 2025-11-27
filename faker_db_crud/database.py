# database.py
# sqlite3 연결 및 간단한 CRUD 함수 정의

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "library.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            year INTEGER,
            available INTEGER DEFAULT 1
        )
        """
    )
    conn.commit()
    conn.close()


def get_all_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_book(book_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def create_book(title: str, author: str, year: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books (title, author, year, available) VALUES (?, ?, ?, 1)",
        (title, author, year),
    )
    conn.commit()
    book_id = cur.lastrowid
    conn.close()
    return book_id


def update_book(book_id: int, title: str, author: str, year: int, available: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE books
        SET title = ?, author = ?, year = ?, available = ?
        WHERE id = ?
        """,
        (title, author, year, available, book_id),
    )
    conn.commit()
    conn.close()


def delete_book(book_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
