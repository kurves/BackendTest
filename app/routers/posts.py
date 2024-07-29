from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from cachetools import TTLCache
from .. import models, schemas, security, database

router = APIRouter()
cache = TTLCache(maxsize=100, ttl=300)

@router.post("/posts", response_model=schemas.Post)
def add_post(post: schemas.PostCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    db_post = models.Post(**post.dict(), owner_id=current_user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/posts", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(database.get_db), current_user: models.User = Depends(security.get_current_user)):
    if current_user.email in cache:
        return cache[current_user.email]
    posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    cache[current_user.email] = posts
    return posts