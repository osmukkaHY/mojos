from sqlalchemy import (
    Integer,
    Text,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    Mapped,
)


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "Books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    author: Mapped[str] = mapped_column(Text)
    year: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"Book(id={self.id!r},", \
               f"title={self.title!r},", \
               f"author={self.author!r},", \
               f"year={self.year!r})"

