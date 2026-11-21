from sqlalchemy import text

from database import db


def add_book(db, reference_name: str, title: str, author: str, year: int, publisher: str) -> None:
    """Adds a book to the database."""

    sql = text(
        "INSERT INTO Book (reference_name, title, author, year, publisher) VALUES (:reference_name, :title, :author, :year, :publisher)")
    db.session.execute(sql, {"reference_name": reference_name, "title": title, "author": author, "year": year, "publisher": publisher})
    db.session.commit()


def get_books():
    """Gets all books from the database.

    Returns: 
        A list of dictionaries, each representing a book with keys 'id', 'title', 'author', and 'year'.
    """

    return db.session.execute(
        text("SELECT id, title, author, year FROM Book ORDER BY id")
    ).mappings().all()
