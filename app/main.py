from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from users.models import Base, User
from users.schemas import UserManager
from users.schemas import UserCreate, SuperuserCreate

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

user_manager = UserManager()

@app.post("/users/")
def create_user(user: UserCreate):
    return user_manager.create_user(**user.dict())

@app.post("/superusers/")
def create_superuser(superuser: SuperuserCreate):
    return user_manager.create_superuser(**superuser.dict())
