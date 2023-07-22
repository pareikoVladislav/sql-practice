def create_books_table() -> str:
    return """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY NOT NULL,
            title TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            publication_year INTEGER,
            genre_id INTEGER NOT NULL,
            created_at DATETIME NOT NULL,
            FOREIGN KEY(author_id) REFERENCES authors(id),
            FOREIGN KEY(genre_id) REFERENCES genre(id)
        );
    """


def create_authors_table() -> str:
    return """
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            birth_year INTEGER,
            country TEXT,
            created_at DATETIME NOT NULL
        );
    """


def create_genre_table() -> str:
    return """
        CREATE TABLE IF NOT EXISTS genre (
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            created_at DATETIME NOT NULL
        );
    """


def insert_data_into_authors() -> str:
    return """
        INSERT INTO authors (name, birth_year, country, created_at)
        VALUES (?, ?, ?, ?)   
    """


def insert_data_into_genre() -> str:
    return """
        INSERT INTO genre (name, created_at)
        VALUES (?, ?)
    """


def insert_data_into_books() -> str:
    return """
        INSERT INTO books (title, author_id, publication_year, genre_id, created_at)
        VALUES (?, ?, ?, ?, ?)
    """


def get_author_pk_by_name() -> str:
    return """
        SELECT id
        FROM authors
        WHERE name = ?
    """


def get_genre_pk_by_name() -> str:
    return """
        SELECT id
        FROM genre
        WHERE name = ?
    """
