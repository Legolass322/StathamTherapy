import os
import pytest

os.environ["ENV"] = "e2e"

from database import database
from config.config import config

from database.models._all_models import *


def main():
    database.init_db(config["database"]["host"])
    pytest.main()


if __name__ == "__main__":
    main()
