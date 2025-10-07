from . import schemas, models


from .database import engine, SessionLocal

from sqlalchemy.orm import Session


from .hashing import Hash



@app.post('/user')



@app.post('/user', response_model=schemas.ShowUser)

def create_user(request: schemas.User,db: Session = Depends(get_db)):



    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))

    db.add(new_user)

    db.commit()

    db.refresh(new_user)


    return new_user


    return new_user





@app.get('/user/{id}',response_model=schemas.ShowUser)


def get_user(id:int,db: Session = Depends(get_db)):


    user = db.query(models.User).filter(models.User.id == id).first()


    if not user:


        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,


                            detail=f"User with the id {id} is not available")


    return user
