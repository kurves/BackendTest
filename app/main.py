from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import List


from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, posts

Base.metadata.create_all(bind=engine)

from app import database, models, schemas


app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(posts.router, prefix="/posts")

app = FastAPI()

# Dependency for getting the database session
def get_db():
    db = database.get_db()
    yield db


# Dependency for authenticating users with JWT tokens
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # TODO: Implement JWT token validation logic here (e.g., using PyJWT)
    if not token:
        raise credentials_exception
    # Validate token and return the user object

    return User(id=1, email="user@example.com")  # Replace with actual user lookup


# User signup endpoint
@app.post("/signup", response_model=schemas.User)
async def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Hash the password before storing
    hashed_password = pwd_context.hash(user.password)
    user_obj = models.User(email=user.email, hashed_password=hashed_password)
    db.add(user_obj)
    db.commit()
    db.refresh(user_


