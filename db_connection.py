import sqlite3 as sql
from sqlite3 import Connection, Cursor


class DBConnection:
    def __init__(self, db_name):
        self.db_name: str = db_name
        self.connection: Connection = self.create_database()
        self.cursor: Cursor = self.connection.cursor()

    def create_database(self) -> Connection:
        return sql.connect(self.db_name)

    def create_table(self, query: str) -> None:
        self.cursor.execute(query)

    def close_cursor(self) -> None:
        self.cursor.close()

    def close_db_conn(self) -> None:
        self.connection.close()
