from sqlalchemy import create_engine
from database.init_db import create_tables

DATABASE_URL = f"sqlite:///../storage/db_test.db"
engine = create_engine(DATABASE_URL, echo=True)

create_tables(engine=engine)
