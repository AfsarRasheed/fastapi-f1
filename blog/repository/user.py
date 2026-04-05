from fastapi import Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from blog import database, models
from blog.hashing import Hash
from .. import schema,database,models
from ..database import get_db

def create_user(payload: schema.User, db: Session = Depends(get_db)):
    
    new_user = models.User(
        name=payload.name,
        email=payload.email,
        password=Hash.bcrypt(payload.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def read_user_by_id(id: int, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    return user 