from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':'blog list'}


@app.get('/about')
def abc():
    return {'data': 'about page'}