from sqlalchemy import (
    Integer,
    Text,
)
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)

from database import db


class Article(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    reference_name: Mapped[str] = mapped_column(Text)
    title: Mapped[str] = mapped_column(Text)
    author: Mapped[str] = mapped_column(Text)
    year: Mapped[int] = mapped_column(Integer)
    journal: Mapped[str] = mapped_column(Text)
    pages: Mapped[str] = mapped_column(Text)
