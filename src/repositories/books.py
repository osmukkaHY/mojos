from sqlalchemy import text

from database import db


def add_book(db, reference_name: str, title: str, author: str, year: int, publisher: str, tag: str) -> None:
    """Adds a book to the database."""

    sql = text(
        "INSERT INTO Book (reference_name, title, author, year, publisher, tag) VALUES (:reference_name, :title, :author, :year, :publisher, :tag)")
    db.session.execute(sql, {"reference_name": reference_name, "title": title,
                       "author": author, "year": year, "publisher": publisher, "tag": tag})
    db.session.commit()


def get_books():
    """Gets all books from the database.

    Returns: 
        A list of dictionaries, each representing a book with keys 'id', 'reference_name', 'title', 'author', 'year' and 'publisher'.
    """

    return db.session.execute(
        text("SELECT id, reference_name, title, author, year, publisher, tag FROM Book ORDER BY id")
    ).mappings().all()


def get_book(db, book_id: int):
    """Gets a single book from the database.

    Args: 
        db: The database connection.
        book_id (int): The id of the book to get.

    Returns: 
        A dictionary representing the book, or None if not found.
    """

    return db.session.execute(
        text("SELECT id, reference_name, title, author, year, publisher, tag FROM Book WHERE id = :id"),
        {"id": book_id},
    ).mappings().first()


def delete_book(db, book_id: int):
    """Delete a book from the database."""
    db.session.execute(
        text("DELETE FROM Book WHERE id = :id"),
        {"id": book_id}
    )
    db.session.commit()


def edit_book(db, book_id: int, reference_name: str, title: str, author: str, year: int, publisher: str, tag: str):
    """Edit a book in the database."""
    db.session.execute(
        text("UPDATE Book SET reference_name = :reference_name, title = :title, author = :author, year = :year, publisher = :publisher, tag = :tag WHERE id = :id"),
        {"id": book_id, "reference_name": reference_name, "title": title,
            "author": author, "year": year, "publisher": publisher, "tag": tag}
    )
    db.session.commit()
