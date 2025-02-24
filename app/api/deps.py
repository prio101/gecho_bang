from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db

def get_db_session():
    db = get_db()
    try:
        yield db
    finally:
        db.close()
