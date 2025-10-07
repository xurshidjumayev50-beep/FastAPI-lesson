from fastapi  import FastAPI

from pydantic import BaseModel

app = FastAPI()
class Blog(Model):
    title:str
    body:str

@app.post('/blog')
def create(requset Blog):
    return requset