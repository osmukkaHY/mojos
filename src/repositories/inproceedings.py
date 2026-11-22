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
