from typing import List


from fastapi import FastAPI, Depends, status, Response, HTTPException

from . import schemas, models

from .database import engine, SessionLocal

@@ -51,13 +52,13 @@ def update(id, request: schemas.Blog, db: Session = Depends(get_db)):

    return 'updated'






@app.get('/blog')


@app.get('/blog', response_model=List[schemas.ShowBlog])

def all(db: Session = Depends(get_db)):

    blogs = db.query(models.Blog).all()

    return blogs






@app.get('/blog/{id}', status_code=200)


@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)

def show(id, response: Response, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog: