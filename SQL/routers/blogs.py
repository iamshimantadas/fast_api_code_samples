from typing import Union, Annotated

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, status, APIRouter
from sql_app import models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    # prefix="/blogs",
    tags=["blogs"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# creating annotation for database
db_dependency = Annotated[Session, Depends(get_db)]



@router.get("/blogs/",status_code=status.HTTP_200_OK)
def get_posts(db: db_dependency):
    db_query = db.query(models.Blogs).all()
    return {"blog":db_query}


@router.post("/blogs/",status_code=status.HTTP_200_OK)
def create_post(blog: schemas.Blogs, db: db_dependency, dependencies=[Depends(verify_token)]):
    db_query = models.Blogs(**blog.dict())
    try:
        db.add(db_query)
        db.commit()
        db.refresh(db_query)
        return {"status":"blog created", "blog":db_query}
    except Exception as e:
        print(e)
        return {"status":"error occured"}

