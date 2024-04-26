from .database import engine, Base


def create_tables(engine=engine):
    Base.metadata.create_all(engine)
