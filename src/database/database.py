from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

engine = None

metadata = MetaData()

Base = declarative_base(metadata=metadata)

Session = None

def init_engine(database_host: str):
    global engine
    engine = create_engine(database_host, echo=True)

def create_tables(engine):
    assert engine is not None, "DB engine is None"
    Base.metadata.create_all(engine)

def init_db(database_host: str):
    global Session, engine
    init_engine(database_host)
    create_tables(engine)
    Session = sessionmaker(bind=engine)