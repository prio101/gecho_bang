from sqlalchemy.orm import Session
from app.models import User
from app.database import SessionLocal, get_db

class UserRepo:

  def __init__(self):
    self.db = SessionLocal()

  def list_users(self):
    return self.db.query(User).all()

  def get_user(self, user_id: int):
    return self.db.query(User).filter(User.id == user_id).first()

  def create_user(self, user: User):
    db_user = User(name=user.name,
                   email=user.email)
    self.db.add(db_user)
    self.db.commit()
    self.db.refresh(db_user)
    return db_user

  def get_user_by_email(self, email: str):
    return self.db.query(User).filter(User.email == email).first()
