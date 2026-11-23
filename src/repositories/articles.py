from sqlalchemy import text

from database import db


def add_article(db, reference_name: str, title: str, author: str, year: int, journal: str, pages: str) -> None:
    """Adds an article to the database."""

    sql = text(
        "INSERT INTO Article (reference_name, title, author, year, journal, pages) VALUES (:reference_name, :title, :author, :year, :journal, :pages)")
    db.session.execute(sql, {"reference_name": reference_name, "title": title,
                       "author": author, "year": year, "journal": journal, "pages": pages})
    db.session.commit()


def get_articles():
    """Gets all articles from the database.

    Returns: 
        A list of dictionaries, each representing an article with keys 'id', 'reference_name', 'title', 'author', 'year', 'journal' and 'pages'.
    """

    return db.session.execute(
        text("SELECT id, reference_name, title, author, year, journal, pages "
             "FROM Article ORDER BY id")
    ).mappings().all()


def get_article(db, article_id: int):
    """Gets a single article from the database.

    Args:
        db: The database connection.
        article_id: The ID of the article to get.

    Returns:
        A dictionary representing the article, or None if not found.
    """

    return db.session.execute(
        text("SELECT id, reference_name, title, author, year, journal, pages "
             "FROM Article WHERE id = :id"),
        {"id": article_id},
    ).mappings().first()


def delete_article(db, article_id: int):
    """Delete an article from the database."""
    db.session.execute(
        text("DELETE FROM Article WHERE id = :id"),
        {"id": article_id}
    )
    db.session.commit()


def edit_article(
    db,
    article_id: int,
    reference_name: str,
    title: str,
    author: str,
    year: int,
    journal: str,
    pages: str,
):
    """Edit an article in the database."""
    db.session.execute(
        text("UPDATE Article SET reference_name = :reference_name, "
             "title = :title, author = :author, year = :year, "
             "journal = :journal, pages = :pages WHERE id = :id"),
        {"id": article_id, "reference_name": reference_name, "title": title,
         "author": author, "year": year, "journal": journal, "pages": pages}
    )
    db.session.commit()
