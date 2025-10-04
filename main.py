from fastapi import FastAPI

myapp = FastAPI()

@myapp.get('/')
def index():
    return {'data': {'name': 'Sarthak'}}


@myapp.get('/about')
def about():
    return {'data': 'about page'}