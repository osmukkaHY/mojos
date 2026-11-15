from sqlalchemy import text

from database import db

def add_book(db, title: str, author: str, year: int) -> None:
    """Adds a book to the database."""

    sql = text("INSERT INTO Book (title, author, year) VALUES (:title, :author, :year)")
    db.session.execute(sql, {"title": title, "author": author, "year": year})
    db.session.commit()

def get_books():
    """Gets all books from the database.
    
    Returns: 
        A list of dictionaries, each representing a book with keys 'id', 'title', 'author', and 'year'.
    """

    return db.session.execute(
            text("SELECT id, title, author, year FROM Book ORDER BY id")
        ).mappings().all()
