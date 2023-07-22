import sqlite3

from sql_queries import *
from helpers import get_created_at_date

from db_connection import DBConnection


class Library:
    def __init__(self):
        self.db_conn = DBConnection("library.db")

        self.db_conn.create_table(create_books_table())
        self.db_conn.create_table(create_authors_table())
        self.db_conn.create_table(create_genre_table())

    def add_author(
            self,
            author_name: str,
            author_b_year: int,
            author_country: str) -> None | dict:
        try:
            self.db_conn.cursor.execute(
                insert_data_into_authors(),
                (author_name, author_b_year, author_country, get_created_at_date())
            )

            self.db_conn.connection.commit()
        except sqlite3.OperationalError as err:
            return {
                "err_message": err,
            }

    def get_author_id_by_name(self, author_name: str) -> int | dict:
        try:
            self.db_conn.cursor.execute(
                get_author_pk_by_name(),
                (author_name,)
            )

            row: list = self.db_conn.cursor.fetchone()

            author_id: int = row[0]

            return author_id
        except sqlite3.OperationalError as err:
            return {
                "err_message": err,
            }

    def add_book_genre(self, genre_name: str) -> None | dict:
        try:
            self.db_conn.cursor.execute(
                insert_data_into_genre(),
                (genre_name, get_created_at_date())
            )
            self.db_conn.connection.commit()
        except sqlite3.OperationalError as err:
            return {
                "err_message": err,
            }

    def get_genre_id_by_name(self, genre_name: str) -> int | dict:
        try:
            self.db_conn.cursor.execute(
                get_genre_pk_by_name(),
                (genre_name, )
            )

            row: list = self.db_conn.cursor.fetchone()

            genre_id: int = row[0]

            return genre_id
        except sqlite3.OperationalError as err:
            return {
                "err_message": err,
            }

    def add_book(
            self,
            book_title: str,
            author_name: str,
            public_year: int,
            genre_name: str) -> None | dict:

        author_id: int = self.get_author_id_by_name(author_name)
        genre_id: int = self.get_genre_id_by_name(genre_name)

        try:
            self.db_conn.cursor.execute(
                insert_data_into_books(),
                (book_title, author_id, public_year, genre_id, get_created_at_date())
            )

            self.db_conn.connection.commit()
        except sqlite3.OperationalError as err:
            return {
                "err_message": err,
            }


def main():
    lib = Library()

    user_choices: tuple = (
        "add author",
        "add genre",
        "add new book",
    )

    while True:
        print(user_choices)
        user_choice = input("Enter an action you needed: ")

        match user_choice:
            case 'q':
                break
            case 'add author':
                lib.add_author(
                    input("Enter Author's name: "),
                    int(input("Enter Author's b-day year: ")),
                    input("Enter Author's country: ")
                )
            case 'add genre':
                lib.add_book_genre(
                    input("Enter book's genre: ")
                )
            case 'add new book':
                lib.add_book(
                    input("Enter a book name: "),
                    input("Enter a author name: "),
                    int(input("Enter a date of publication: ")),
                    input("Enter a genre name: ")
                )
            case _:
                print("I don't know this command. Please, try again.")


if __name__ == "__main__":
    main()
