from typing import Union
from fastapi import FastAPI
import shutil, uuid, json
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from routes import users
from database.db_connection import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    
    
app = FastAPI(lifespan=lifespan)

@app.get('/')
def get_home():
    return {"message":"hello"}


app.include_router(users.router)