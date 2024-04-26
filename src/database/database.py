from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite:///../storage/db.db"
engine = create_engine(DATABASE_URL, echo=True)

metadata = MetaData()

Base = declarative_base(metadata=metadata)
