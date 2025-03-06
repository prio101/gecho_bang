from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    status: str
    genre: str
    user_id: int



class BookUpdate(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    author: Optional[str] = None
    cover_url: Optional[str] = None
    audiobook_url: Optional[str] = None
    status: Optional[str] = None
    duration: Optional[str] = None
    genre: Optional[str] = None
    progress: Optional[int] = None
    rating: Optional[int] = None
    user_id: Optional[int] = None
    file: Optional[str] = None

    class Config:
        orm_mode = True

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    cover_url: str
    audiobook_url: str
    status: str
    duration: str
    genre: str
    progress: int
    rating: int
    user_id: int
    file: str

    class Config:
        orm_mode = True

