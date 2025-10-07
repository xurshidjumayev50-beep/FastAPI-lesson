from fastapi import FastAPI, Depends



from fastapi import FastAPI, Depends, status, Response, HTTPException

from . import schemas, models

from .database import engine, SessionLocal

from sqlalchemy.orm import Session

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)


def destroy(id, db: Session = Depends(get_db)):


    db.query(models.Blog).filter(models.Blog.id ==


                                 id).delete(synchronize_session=False)


    blog = db.query(models.Blog).filter(models.Blog.id == id)





    if not blog.first():


        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,


                            detail=f"Blog with id {id} not found")





    blog.delete(synchronize_session=False)

    db.commit()

    return 'done'






@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)


def update(id, request: schemas.Blog, db: Session = Depends(get_db)):


    blog = db.query(models.Blog).filter(models.Blog.id == id)





    if not blog.first():


        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,


                            detail=f"Blog with id {id} not found")





    blog.update(request)


    db.commit()


    return 'updated'