from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.repo.user_repo import UserRepo
from app.schemas.user_schemas import UserCreate

router = APIRouter(prefix="/api/v1", tags=["API"])

@router.get("/users")
async def get_users():
    """Return the list of users"""
    users = UserRepo().list_users()
    return JSONResponse(content={"users": users}, status_code=200)


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    """Return the user details"""
    user = UserRepo().get_user(user_id)
    user_data = jsonable_encoder(user)

    return JSONResponse(content={"user": user_data}, status_code=200)


@router.post("/users")
async def create_users(user_create: UserCreate):
    """Create a new user"""
    if UserRepo().get_user_by_email(user_create.email):
        return JSONResponse(content={"message": "user already exists"}, status_code=400)

    user = UserRepo().create_user(user_create)
    if not user:
        return JSONResponse(content={"message": "user not created"}, status_code=400)

    user_data = jsonable_encoder(user)
    return JSONResponse(content={"message": "user created successfully",
                                 "user": user_data},
                                 status_code=201)
