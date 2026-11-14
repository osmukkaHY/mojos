from sqlalchemy import (
    Integer,
    Text,
)
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)

from database import db


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    author: Mapped[str] = mapped_column(Text)
    year: Mapped[int] = mapped_column(Integer)

