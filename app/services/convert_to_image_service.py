import pdf2image
import requests
import os
from app.repo.book_repo import BookRepo

class ConvertToImageService:

    def __init__(self, book_url: str, book_id: int):

        self.book_url = book_url
        self.book_id = book_id
        self.book_folder = None


    def convert_to_image(self) -> str:
        # Convert PDF to Image

        response = requests.get(self.book_url)

        book_name = BookRepo().get_book(self.book_id).title
        self.book_folder = book_name.replace(" ", "_").lower()

        # Check if images folder exists
        # if it does, return the path
        if os.path.exists(f"documents/books/images/{self.book_folder}"):
            return f"documents/books/images/{self.book_folder}"

        if response.status_code != 200:
            return ""

        images_path = book_name.replace(" ", "_").lower()

        with open(book_name, 'wb') as f:
            f.write(response.content)

        images = pdf2image.convert_from_path(book_name)
        if not os.path.exists(f"documents/books/images/{self.book_folder}"):
            os.makedirs("documents/books/images/" + self.book_folder)
        for i, image in enumerate(images):
            image.save(f"documents/books/images/{self.book_folder}/{images_path}_{i}.jpg", "JPEG")

        return f"documents/books/images/{self.book_folder}"
