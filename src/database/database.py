from sqlalchemy import create_engine, MetaData
from databases import Database
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///../storage/db.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
database = Database(DATABASE_URL)
Base = declarative_base()