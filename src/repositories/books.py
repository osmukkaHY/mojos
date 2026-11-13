from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from src.models.book import Book


def add_book(engine: Engine, title: str, author: str, year: int) -> None:
    with Session(engine) as session:
        new_book = Book(title=title, author=author, year=year)
        session.add(new_book)
        session.commit()

