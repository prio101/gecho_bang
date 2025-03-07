import pdf2image
import requests
import os

class ConvertToImageService:

    def __init__(self, book_url: str):
        self.book_url = book_url

    def convert_to_image(self) -> str:
        # Convert PDF to Image
        response = requests.get(self.book_url)
        book_name = self.book_url.split("/")[-1]

        if response.status_code != 200:
            return ""

        with open(book_name, 'wb') as f:
            f.write(response.content)

        images = pdf2image.convert_from_path(book_name)

        for i, image in enumerate(images):
            image.save(f"documents/books/images/{book_name}_{i}.jpg", "JPEG")

        os.remove(book_name)

        return f"documents/books/images/{book_name}_0.jpg"
