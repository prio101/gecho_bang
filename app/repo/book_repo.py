from sqlalchemy.orm import Session
from app.models import Book
from app.schemas import BookCreate

class BookRepo:
  """Book Repository"""
  def __init__(self):
      pass

  def create_book(self):
    """Create a new book"""
    return False
