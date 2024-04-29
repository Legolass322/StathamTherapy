import os

from .meta import Meta

ENV = os.environ.get("ENV")
HOST = os.environ.get("HOST")
AUTH_JWT_SECRET = os.environ.get("AUTH_JWT_SECRET")
AUTH_RT_SECRET = os.environ.get("AUTH_RT_SECRET")

production_config = {
    "host": HOST,
    "auth": {
        "jwt_secret": AUTH_JWT_SECRET,
        "rt_secret": AUTH_RT_SECRET,
        "algorithm": "HS256",
        # time in minutes
        "jwt_expiration": 15,
        "rt_expiration": 60 * 24 * 7,
    },
    "database": {"host": "sqlite:///./storage/db.db"},
}


def productionToDevelopment(it: dict):
    it["host"] = "localhost:8080"


def productionToE2E(it: dict):
    it["host"] = "localhost:8080"
    it["database"]["host"] = "sqlite:///./storage/db_test.db"


meta = Meta()

meta.set("production", production_config)
meta.set_from("development", "production", productionToDevelopment)
meta.set_from("e2e", "production", productionToE2E)

config = meta.get_config(ENV)
