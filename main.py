from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def abs():
    return {'data': {'name': 'Sarthak'}}


@app.get('/about')
def xyzS():
    return {'data': 'about page'}