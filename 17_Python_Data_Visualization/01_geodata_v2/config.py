import os
from dotenv import load_dotenv


def load_config():
    load_dotenv()  # Load environment variables from .env
    database_path = os.getenv("DATABASE_PATH")
    if not database_path:
        raise ValueError("DATABASE_PATH environment variable is missing")
    return {
        "database": database_path,
    }
