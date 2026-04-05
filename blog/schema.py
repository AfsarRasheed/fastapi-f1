from pydantic import BaseModel, Field
from typing import List, Optional
class Blog(BaseModel):
    title:str
    content:str


class User(BaseModel):
    
    name:str
    email:str
    password:str
    class config():
        orm_mode=True
class showUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog] = []
    class config():
        orm_mode=True
class showBlog(BaseModel):
    title:str
    content:str
    creator: showUser
    class config():
        orm_mode=True
class Login(BaseModel):
    username:str
    password:str
    class config():
        orm_mode=True
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None