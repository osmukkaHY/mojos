from sqlalchemy import text

from database import db

def add_book(db, title: str, author: str, year: int) -> None:
    """Adds a book to the database."""

    sql = text("INSERT INTO Book (title, author, year) VALUES (:title, :author, :year)")
    db.session.execute(sql, {"title": title, "author": author, "year": year})
    db.session.commit()
