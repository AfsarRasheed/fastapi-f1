from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import schema, database, oAuth2

from ..database import get_db   
from ..repository import blog
router = APIRouter(prefix="/blog", tags=["Blogs"])
get_db = database.get_db

@router.post("", response_model=schema.Blog, status_code=status.HTTP_201_CREATED)
def create_blog(payload: schema.Blog, db: Session = Depends(get_db),current_user: schema.TokenData = Depends(oAuth2.get_current_user)):
    return blog.create_blog(payload,db)


@router.get("",response_model=list[schema.showBlog])
def read_blog(
    db: Session = Depends(database.get_db),
    current_user: schema.TokenData = Depends(oAuth2.get_current_user),
):
    return blog.read_blog(db)

    

@router.get("/{id}",status_code=200,response_model=schema.showBlog)
def read_blog_by_id(id: int,response: Response, db: Session = Depends(get_db),current_user: schema.TokenData = Depends(oAuth2.get_current_user)):
    return blog.read_blog_by_id(id,response,db)
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db),current_user: schema.TokenData = Depends(oAuth2.get_current_user)):
    return blog.delete_blog(id,db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, payload: schema.Blog, db: Session = Depends(get_db),current_user: schema.TokenData = Depends(oAuth2.get_current_user)):
   return blog.update_blog(id,payload,db)
