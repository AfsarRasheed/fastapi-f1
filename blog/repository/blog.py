

from fastapi import Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from blog import database, models
from .. import schema,database,models
from ..database import get_db


def create_blog(payload: schema.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(
        title=payload.title,
        content=payload.content,
        user_id=1
       
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
def read_blog(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
def read_blog_by_id(id: int,response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message": f"Blog with id {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog
def delete_blog(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
def update_blog(id: int, payload: schema.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update({'title': payload.title, 'content': payload.content}, synchronize_session=False)
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    db.commit()
    return Response(status_code=status.HTTP_202_ACCEPTED) 
