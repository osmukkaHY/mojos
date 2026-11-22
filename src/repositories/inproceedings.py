from sqlalchemy import text

from database import db


def add_inproceedings(db, reference_name: str, title: str, author: str, year: int, series: str, pages: str) -> None:
    """Adds an inproceedings entry to the database."""

    sql = text(
        "INSERT INTO inproceedings (reference_name, title, author, year, series, pages) "
        "VALUES (:reference_name, :title, :author, :year, :series, :pages)"
    )
    db.session.execute(
        sql,
        {
            "reference_name": reference_name,
            "title": title,
            "author": author,
            "year": year,
            "series": series,
            "pages": pages,
        },
    )
    db.session.commit()


def get_inproceedings():
    """Gets all inproceedings entries from the database.

    Returns:
        A list of rows containing each entry's id, title, author, and year.
    """

    return db.session.execute(
        text("SELECT id, title, author, year FROM inproceedings ORDER BY id")
    ).mappings().all()
