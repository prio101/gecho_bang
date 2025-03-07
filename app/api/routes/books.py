from fastapi import APIRouter, FastAPI, File, UploadFile, Form, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.repo.book_repo import BookRepo
from app.schemas.book_schemas import BookCreate, BookUpdate
from app.minio import MinioUploader
from app.services import ConvertToImageService, FetchCoverService, OcrExtractTextService, TtsConvertService
import base64

router = APIRouter(prefix="/api/v1", tags=["API"])


@router.get("/books")
async def get_books():
    """Return the list of books"""
    books = BookRepo().list_books()
    data_book = jsonable_encoder(books)
    return JSONResponse(content={"data": data_book}, status_code=200)


@router.get("/books/{book_id}")
async def get_book(book_id: int):
    """Return the book details"""
    book = BookRepo().get_book(book_id)
    if not book:
        return HTTPException(content={"message": "Book not found"},
                            status_code=404)

    data_encoded = jsonable_encoder(book)
    return JSONResponse(content={"data": data_encoded}, status_code=200)


@router.post("/books")
async def create_book(book_create: BookCreate):
    """Create a new book"""

    book = BookRepo().create_book(book_create)
    if not book:
        return JSONResponse(content={"message": "Book not created"},
                            status_code=400)

    book_data = jsonable_encoder(book)
    return JSONResponse(content={"message": "Book created successfully",
                                 "data": book_data},
                                 status_code=201)

@router.patch("/books/{book_id}")
async def update_book(book_id: int, book_update: BookUpdate):
    """Update a book"""
    if not BookRepo().get_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")

    if book_update.file:
        file = base64.b64decode(book_update.file)
        book_update.file = file

    book = BookRepo().update_book(book_id, book_update)

    if not book:
        raise HTTPException(status_code=400, detail="Book not updated")

    book_data = jsonable_encoder(book)
    return JSONResponse(content={"message": "Book updated successfully",
                                 "data": book_data},
                                 status_code=200)


@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """Delete a book"""

    if not BookRepo().get_book(book_id):
        return JSONResponse(content={"message": "Book not found"},
                            status_code=404)

    book = BookRepo().delete_book(book_id)

    if not book:
        return JSONResponse(content={"message": "Book not deleted"},
                            status_code=400)

    return JSONResponse(content={"message": "Book deleted successfully"},
                                 status_code=200)


@router.post("/books/{book_id}/upload")
async def upload_file(book_id: int, file: UploadFile = File(...)):
    """Upload a file"""
    book = BookRepo().get_book(book_id)
    if not book:
        return JSONResponse(content={"message": "Book not found"},
                            status_code=404)

    file_content = await file.read()
    file_name = f"{book_id}_{file.filename}"

    file_url = MinioUploader().upload_file(file_name, file_content)

    if file_url:
        book.file = file_url
        BookRepo().update_book(book_id, book)

    return JSONResponse(content={
                                    "message": "File uploaded successfully",
                                    "file": file_url
                                },
                                 status_code=200)


@router.post("/books/{book_id}/process")
async def process_book(book_id: int):
    # process the cover url
    book = BookRepo().get_book(book_id)
    if not book:
        return JSONResponse(content={"message": "Book not found"},
                            status_code=404)

    cover_url = FetchCoverService().fetch_cover(book_id)
    if cover_url:
        book.cover_url = cover_url
        BookRepo().update_book(book_id, book)

    # process the pdf2image
    if book.file:
        image_path = ConvertToImageService(book.file).convert_to_image()
    # process the ocr
    if image_path:
        text = OcrExtractTextService(image_path).extract
    # process the tts
    if text:
        file_url = TtsConvertService(text).run()
    # process the upload
    if file_url:
        book.audiobook_url = file_url
        BookRepo().update_book(book_id, book)

    return JSONResponse(content={"message": "Book processed successfully", "data": book}, status_code=200)

