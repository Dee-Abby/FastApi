from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  published: bool = True
  rating: Optional[int] = None

my_posts = [
  {'title' : 'Real Productivity', "content" : "content of the page", "id" : 1},
  {'title' : 'travel round the world' , "content" : "follow the Sunnah of the prophet", "id" : 2}
]


@app.get('/')
def root():
  return {'message' : 'Hello, I am new to fast apis but i want it fast'} 


@app.get('/posts')
def all_posts():
  return {'data' : my_posts} 

@app.post("/posts")
def add_post(post: Post):
  print(post.model_dump()) 
  return {'data' : post}