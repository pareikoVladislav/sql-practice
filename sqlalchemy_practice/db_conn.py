from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self):
        self.db_conn_str = 'sqlite:///blog.db'
        self.engine = create_engine(self.db_conn_str)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def commit_changes(self):
        self.session.commit()

    def close_connection(self):
        self.session.close()

