from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

metadata = MetaData()

Base = declarative_base(metadata=metadata)


def create_tables(engine):
    assert engine is not None, "DB engine is None"
    Base.metadata.create_all(engine)


class Database:
    def __init__(self):
        self.engine = None
        self.Session = None

    def init(self, host: str):
        if self.engine is None:
            self.engine = create_engine(host, echo=False)
        if self.Session is None:
            self.Session = sessionmaker(bind=self.engine, expire_on_commit=False)

    def create_tables(self):
        assert self.engine is not None, "Engine is None"
        create_tables(self.engine)

    def session(self):
        return self.Session()


db = Database()
