import requests
from app.repo.book_repo import BookRepo


class FetchCoverService:
    """Fetch Cover Service"""
    def __init__(self):
        self.base = "https://www.googleapis.com/books/v1/volumes?q=intitle:"

    def fetch_cover(self, book_id: str) -> str:
        # Fetch cover from some API
        book = BookRepo().get_book(book_id)

        if not book:
            return ""

        response = requests.get(f"{self.base}{book.title}")
        data = response.json()


        if 'items' in data:
            book_data = data['items'][0]['volumeInfo']
            cover_url = book_data.get("imageLinks", {}).get("thumbnail")
            book.cover_url = cover_url

            BookRepo().update_book(book_id, book)

            return cover_url


        if response.status_code != 200:
            return ""
