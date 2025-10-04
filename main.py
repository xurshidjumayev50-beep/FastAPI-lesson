
from fastapi import FastAPI

app = FastAPI()

@app.get("/blog/{blog_id}")
def show(blog_id: int):
    
    return {"data": {"id": blog_id}}

@app.get("/blog/{blog_id}/comments")
def comments(blog_id: int):
    
    return {"data": ["1", "2"]}
