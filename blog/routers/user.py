from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy import schema
from sqlalchemy.orm import Session
from typing import List
from .. repository import user

from blog.hashing import Hash
from blog.routers import blog
from .. import schema,database,models
from ..database import get_db   
router = APIRouter(prefix="/user", tags=["users"])
get_db = database.get_db


@router.post("", response_model=schema.showUser, status_code=status.HTTP_201_CREATED)
def create_user(payload: schema.User, db: Session = Depends(get_db),current_user: schema.TokenData = Depends(blog.oAuth2.get_current_user)):
    return user.create_user(payload,db)
    
    

@router.get("/{id}", response_model=schema.showUser, status_code=status.HTTP_200_OK)
def read_user_by_id(id: int, response: Response, db: Session = Depends(get_db),current_user: schema.TokenData = Depends(blog.oAuth2.get_current_user)):
    return user.read_user_by_id(id,response,db)