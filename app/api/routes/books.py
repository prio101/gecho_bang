from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api/v1", tags=["API"])

@router.get("/")
async def root():
    """Return the hello world message"""
    return {"message": "Hello World"}

@router.get("/health")
async def health():
    """Return the health status of the service"""
    return JSONResponse(content={"status": "OK"})

@router.get("/version")
async def version():
    """Return the version of the service"""
    return JSONResponse(content={"version": VERSION_NUMBER})

@router.get("/books")
async def get_books():
    """Return the list of books"""
    books_list = Book.objects.all
    return JSONResponse(content={"books": books_list})


@router.get("/books/{book_id}")
async def get_book(book_id: int):
    """Return the book details"""
    book = {"id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
    }
    if book_id==1:
        return JSONResponse(content={"book": book})
    else:
        return JSONResponse(content={"message": "Book not found"})


@router.post("/books")
async def create_book():
    """Create a new book"""
    return JSONResponse(content={"message": "Book created successfully"})
