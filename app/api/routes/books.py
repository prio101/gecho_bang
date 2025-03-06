from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.repo.book_repo import BookRepo
from app.schemas.book_schemas import BookCreate, BookUpdate

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

    return JSONResponse(content={"data": book}, status_code=200)


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

    book = BookRepo().update_book(book_id, book_update)
    if not book:
        return JSONResponse(content={"message": "Book not updated"},
                            status_code=400)

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
