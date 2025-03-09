from celery import Celery
from app.repo.book_repo import BookRepo
from app.services import (ConvertToImageService,
                         OcrExtractTextService,
                         TtsConvertService,
                         FetchCoverService)


celery = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task(name="process_book_task")
def process_book_task(book_id: int):
    book = BookRepo().get_book(book_id)
    if not book.cover_url:
        cover_url = FetchCoverService().fetch_cover(book_id)
        if cover_url:
            book.cover_url = cover_url
            BookRepo().update_book(book_id, book)

    image_path = None
    texts = None
    file_url = None

    # process the pdf2image
    if book.file:
        image_path = ConvertToImageService(book.file, book.id).convert_to_image()

    # process the ocr
    if image_path:
        texts = OcrExtractTextService(image_path).run()
    # # process the tts
    if texts:
        files_url = TtsConvertService(texts, book.title).run()

    # # # process the upload
    if files_url:
        book.audiobook_url = str(files_url)
        book.status = "completed"
        BookRepo().update_book(book_id, book)

    return True
