from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from .. import schema, database, models, token
from ..hashing import Hash

from ..schema import Token
from ..database import get_db

router = APIRouter(prefix="/login", tags=["Authentication"])


@router.post("",response_model=schema.Token)
def login(payload: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == payload.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not Hash.verify(user.password, payload.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")

    
    access_token = token.create_access_token(data={"sub": user.email})
    return schema.Token(access_token=access_token, token_type="bearer") 
