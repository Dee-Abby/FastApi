from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


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
def find_post(id):
  for p in my_posts:
    if p['id'] == id:
      return p

def find_index(id):
  for i, p in enumerate(my_posts):
    if p['id'] == id:
      return i

@app.get('/')
def root():
  return {'message' : 'Hello, I am new to fast apis but i want it fast'} 


@app.get('/posts')
def all_posts():
  return {'data' : my_posts} 

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def add_post(post: Post):
  post_dict = post.dict()
  post_dict['id'] = randrange(0, 10000)
  my_posts.append(post_dict)
  return {'data' : post_dict}

@app.get("/posts/{id}")
def fetch_post(id: int):
  post = find_post(id)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {'message' : f"post with id {id} was not found"}
  return {'data' : post} 


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
  post = find_index(id)
  if post is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id {id} does not exist")
  my_posts.pop(post)
  return Response(status_code=status.HTTP_204_NO_CONTENT)
  # return {"message" : f"post with id {id} has deleted"}


@app.put("/posts/{id}", status_code=status.HTTP_200_OK)
def update_post(id : int, post: Post):
  index = find_index(id)
  if index == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id {id} does not exist")
  post_dict = post.dict()
  post_dict['id'] = id
  my_posts[index] = post_dict
  return {'data' : post_dict}

