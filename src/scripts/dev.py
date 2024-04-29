import uvicorn
from app.providers.user.create_user import create_user
from database import database
from config.config import config

def main():
    database.init_db(config["database"]["host"])
    uvicorn.run("app.main:app", port=8080, log_level="info")

if __name__ == "__main__":
    main()