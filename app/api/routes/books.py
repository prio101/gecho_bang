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
    books_list = [
        {"id": 1,
         "title": "The Great Gatsby",
         "author": "F. Scott Fitzgerald",
         "cover_url": "https://images-na.ssl-images-amazon.com/images/I/51ZJ2q4%2BZEL._SX331_BO1,204,203,200_.jpg",
         "auduiobook_url": "https://localhost:9001/gecho-bang-api/v1/books/1/audiobook.mp3",
         "status": "not read",
         "duration": "5h 30m",
         "genre": "Fiction",
         "published_date": "1925",
         "progress": "20%",
         "rating": 4.5,
         "notes": [
              {"id": 1, "content": "This is a great book"},
              {"id": 2, "content": "I love the characters"},
              {"id": 3, "content": "The plot is amazing"}
         ]
        },
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"id": 3, "title": "1984", "author": "George Orwell"},
        {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
        {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger"}
    ]
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
