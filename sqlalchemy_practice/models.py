from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import declarative_base, relationship

from db_conn import Database

Base = declarative_base()
db = Database()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    password = Column(String(150))
    email = Column(String(50), unique=True)
    additional_info = Column(String(500))
    created_at = Column(String(30))
    updated_at = Column(String(30), default=None)

    posts = relationship('Post', back_populates='author')
    comments = relationship('Comment', back_populates='author')


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(75))
    content = Column(String(500))
    author_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(String(30))
    updated_at = Column(String(30), default=None)

    author = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(250))
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created_at = Column(String(30))
    updated_at = Column(String(30), default=None)

    author = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')


Base.metadata.create_all(db.engine)
