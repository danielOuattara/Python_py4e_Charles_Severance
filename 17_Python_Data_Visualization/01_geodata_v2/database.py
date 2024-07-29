import sqlite3
from sqlite3 import Error as SQLiteError
from config import load_config


class DatabaseConnectionError(Exception):
    pass


class Database:
    def __init__(self):
        self.config = load_config()
        self.connection = None

    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self.config['database'])
            print(f'Connection established: {self.connection}')
            return self.connection
        except SQLiteError as e:
            raise DatabaseConnectionError(
                f"Operational error while connecting to SQLite: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            print("SQLite connection is closed.")
