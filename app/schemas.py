from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class BookCreate(BaseModel):
    title: str
    audthor: str
    status: str
    duration: str
    genre: str
    progress: int
    rating: int
    user_id: int

class BookResponse(BaseModel):
    id: int
    title: str
    audthor: str
    cover_url: str
    audiobook_url: str
    status: str
    duration: str
    genre: str
    progress: int
    rating: int
    user_id: int

    class Config:
        orm_mode = True
