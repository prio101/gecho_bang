from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    cover_url: str
    audiobook_url: str
    status: str
    duration: str
    genre: str
    progress: int
    rating: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    user_id: int

    class Config:
        orm_mode: True
