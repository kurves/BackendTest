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