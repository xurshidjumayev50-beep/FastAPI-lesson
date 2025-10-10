from . import schemas, models


from .database import engine, SessionLocal

from sqlalchemy.orm import Session


from .hashing import Hash



@app.post('/user')



@app.post('/user', response_model=schemas.ShowUser)

db.close()





@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])


def create(request: schemas.Blog, db: Session = Depends(get_db)):


    new_blog = models.Blog(title=request.title, body=request.body)


    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)

    db.add(new_blog)

    db.commit()

    db.refresh(new_blog)

