from sqlalchemy.orm import Session
from database.init_db import create_tables, engine
from database.models.user import User

if __name__ == "__main__":
    create_tables()

    with Session(engine) as session:
        test_user = User(login="test", passhash="hash", salt="salt")
