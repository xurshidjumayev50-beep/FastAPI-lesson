
from fastapi import FastAPI
from typing import Optional   
from pydantic import BaseModel
app = FastAPI()

@app.get('/')
def index():
    return {'data': 'blog list'}

@app.get('/blog')
def get_blogs(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}
class Blog(BaseModel):
    title:str
    body:str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request:Blog):
    return request
    return {'data':"Blog is create "}