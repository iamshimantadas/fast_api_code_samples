from typing import Union, Annotated

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, status, HTTPException
from sql_app import models, schemas
from sql_app.database import SessionLocal, engine

import bcrypt
from datetime import datetime, timedelta


# external routes
from routers import blogs
from jwt_auth.token_auth import *


# Dependency
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# creating annotation for database
db_dependency = Annotated[Session, Depends(get_db)]


app = FastAPI(
    title="microcodes user's api",
    description="THis apis basically controls user's account sample description",
)

# create new user
@app.post("/users/", status_code=status.HTTP_201_CREATED,  tags=["accounts"])
def create_user(user: schemas.User, db: db_dependency):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(name=user.name, phone=user.phone, email=user.email, password=hashed_password)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"status": "user created!", "user": db_user}
    except Exception as e:
        print(e)
        return {"status": "error"}


# get all user's of table
@app.get("/users/", status_code=status.HTTP_200_OK, tags=["accounts"])
def get_users(db: db_dependency):
    user_obj = db.query(models.User).all()
    return {"user": user_obj}


# get user record by id
@app.get("/users/{userid}", status_code=status.HTTP_200_OK , tags=["accounts"])
def get_user_by_id(userid: int, db: db_dependency):
    try:
        user_obj = db.query(models.User).filter(models.User.id == userid).first()
        return {"user": user_obj}
    except Exception as e:
        print(e)
        return {"status": "no record found"}

''' whenever we make any changes into database we need to commit into that '''

# update user's record by id - put
@app.put("/users/{userid}", status_code=status.HTTP_201_CREATED, tags=["accounts"])
def update_user(userid: int, users: schemas.User, db: db_dependency):
    dbquery = db.query(models.User).filter(models.User.id == userid).first()

    try:
        dbquery.name = users.name
        dbquery.email = users.email
        dbquery.phone = users.phone
        db.commit()

        return {"status": "record updated"}
    except Exception as e:
        print(e)
        return {"status": "error"}


# update user's record by id - patch
@app.patch("/users/{userid}", status_code=status.HTTP_201_CREATED, tags=["accounts"])
def patch_user_data(userid: int, users: schemas.PatchUser, db: db_dependency):
    dbquery = db.query(models.User).filter(models.User.id == userid).first()
    if dbquery:
        try:
            if users.name:
                dbquery.name = users.name
                db.commit()
                
            if users.email:
                dbquery.email = users.email
                db.commit()
                
            if users.phone:
                dbquery.phone = users.phone
                db.commit()
                
            return {"status": "record updated!"}
        except Exception as e:
            print(e)
            return {"userid": userid}
    else:
        return {"status": "user id not exist!"}
    
# delete user's record
@app.delete("/users/{userid}", status_code=status.HTTP_200_OK, tags=["accounts"])
def delete_user_record(userid: int, users: schemas.DeleteUser, db: db_dependency):
    user_obj = db.query(models.User).filter(models.User.id == userid).first()
    try:
        db.delete(user_obj)
        db.commit()
        return {"status":"record deleted"}
    except Exception as e:
        print(e)
        return {"status":"error occured"}    

# login route by email and password
@app.post("/login/", status_code=status.HTTP_200_OK, tags=["accounts"])
def login(users: schemas.AuthUser, db: db_dependency):
    user = db.query(models.User).filter(models.User.email == users.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not bcrypt.checkpw(users.password.encode('utf-8'), user.password.encode('utf-8')):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    else:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        custom_payload = {"name":"domnick torreto"}
        access_token = create_access_token(data={"email": user.email, **custom_payload}, expires_delta=access_token_expires)
        refresh_token = create_refresh_token(data={"email": user.email}, expires_delta=refresh_token_expires)
        return {"access_token": access_token, "refresh_token": refresh_token}


app.include_router(blogs.router)
