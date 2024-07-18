from pydantic import BaseModel, EmailStr, Field
from typing import List

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class User(BaseModel):
    id: int
    email: EmailStr

     class Config:
        orm_mode = True


class PostCreate(BaseModel):
    text: str = Field(max_length=1024 * 1024)  # Limit to 1 MB


class Post(BaseModel):
    id: int
    text: str
    owner_id: int~


from pydantic import BaseModel, EmailStr, constr
from typing import List

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=8)

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    text: constr(max_length=1048576)  # 1 MB

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True