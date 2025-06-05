from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import model
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
model.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str


def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/posts/",status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
    db_post = model.Post(**post.dict())
    db.add(db_post)
    db.commit()

@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async  def read_post(post_id: int, db: db_dependency):
    post = db.query(model.Post).filter(model.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404,detail ='Post not found')
    return post

@app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
async  def delete_post(post_id: int, db: db_dependency):
    db_post = db.query(model.Post).filter(model.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    db.delete(db_post)
    db.commit()


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user (user: UserBase, db:db_dependency):
    db_user = model.User(**user.dict())
    db.add(db_user)
    db.commit()

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async  def read_user(user_id: int, db: db_dependency):
    user = db.query(model.User).filter(model.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail ='User not found')
    return user










