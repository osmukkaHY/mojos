from sqlalchemy import text

from database import db


def add_inproceedings(db, reference_name: str, title: str, author: str, year: int, series: str, pages: str, tag: str) -> None:

    sql = text(
        "INSERT INTO inproceedings (reference_name, title, author, year, series, pages, tag) "
        "VALUES (:reference_name, :title, :author, :year, :series, :pages, :tag)"
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
            "tag": tag,
        },
    )
    db.session.commit()


def get_inproceedings():
    """Gets all inproceedings entries from the database.

    Returns:
        A list of rows containing each entry's id, title, author, and year.
    """

    return db.session.execute(
        text("SELECT id, reference_name, title, author, year, series, pages, tag "
             "FROM inproceedings ORDER BY id")
    ).mappings().all()


def get_inproceeding(db, inproceedings_id: int):
    """Gets a single inproceedings from the database.

    Args:
        db: The database connection.
        inproceedings_id: The ID of the inproceedings to get.

    Returns:
        A dictionary representing the inproceedings, or None if not found.
    """

    return db.session.execute(
        text("SELECT id, reference_name, title, author, year, series, pages, tag "
             "FROM inproceedings WHERE id = :id"),
        {"id": inproceedings_id},
    ).mappings().first()


def delete_inproceedings(db, inproceedings_id: int):
    """Delete an inproceedings from the database."""
    db.session.execute(
        text("DELETE FROM inproceedings WHERE id = :id"),
        {"id": inproceedings_id}
    )
    db.session.commit()


def edit_inproceeding(
    db,
    inproceedings_id: int,
    reference_name: str,
    title: str,
    author: str,
    year: int,
    series: str,
    pages: str,
    tag: str,
):
    """Edit an inproceedings in the database."""
    db.session.execute(
        text("UPDATE inproceedings SET reference_name = :reference_name, "
             "title = :title, author = :author, year = :year, "
             "series = :series, pages = :pages, tag = :tag WHERE id = :id"),
        {"id": inproceedings_id, "reference_name": reference_name,
         "title": title, "author": author, "year": year,
         "series": series, "pages": pages, "tag": tag}
    )
    db.session.commit()
