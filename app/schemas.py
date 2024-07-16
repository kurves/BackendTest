from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class User(BaseModel):
    id: int
    email: EmailStr


class PostCreate(BaseModel):
    text: str = Field(max_length=1024 * 1024)  # Limit to 1 MB


class Post(BaseModel):
    id: int
    text: str
    owner_id: int