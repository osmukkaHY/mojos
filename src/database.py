from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_engine(db_uri: str, echo: bool=False) -> Engine:
    return create_engine(db_uri, echo=echo)


