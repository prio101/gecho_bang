from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    cover_url = Column(String)
    audiobook_url = Column(String)
    status = Column(String, index=True)
    duration = Column(String)
    genre = Column(String, index=True)
    progress = Column(Integer)
    rating = Column(Integer)
    file = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    rating = Column(Integer)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)

class Quote(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    content = Column(String)
    page = Column(Integer)
    location = Column(String)

class MetaData(Base):
    __tablename__ = "meta_data"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), index=True)
    value = Column(String)
