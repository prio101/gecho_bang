from app.models import Book
from app.database import SessionLocal, get_db

class BookRepo:
    """Book Repository"""
    def __init__(self):
        self.db = SessionLocal()

    def list_books(self):
        """List all books"""
        return self.db.query(Book).all()

    def get_book(self, book_id: int):
        """Get a book"""
        return self.db.query(Book).filter(Book.id == book_id).first()

    def create_book(self, book: Book):
        """Create a book"""
        db_book = Book(
            title=book.title,
            author=book.author,
            genre=book.genre,
            user_id=book.user_id
        )
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

    def update_book(self, book_id: int, book_update: Book):
        """Update a book"""
        book = self.get_book(book_id)
        book.title = book_update.title
        book.author = book_update.author
        book.cover_url = book_update.cover_url
        book.audiobook_url = book_update.audiobook_url
        book.status = book_update.status
        book.duration = book_update.duration
        book.genre = book_update.genre
        book.progress = book_update.progress
        book.rating = book_update.rating
        book.user_id = book_update.user_id
        self.db.commit()
        self.db.refresh(book)
        return book

    def delete_book(self, book_id: int):
        """Delete a book"""
        book = self.get_book(book_id)
        self.db.delete(book)
        self.db.commit()
        return book
