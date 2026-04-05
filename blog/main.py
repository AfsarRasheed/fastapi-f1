from fastapi import FastAPI
from blog import  models
from blog.database import engine
from .routers import blog, user ,Authentication 
app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(Authentication.router)
app.include_router(blog.router)
app.include_router(user.router)





