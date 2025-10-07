from . import schemas, models


from .database import engine, SessionLocal

from sqlalchemy.orm import Session


from .hashing import Hash



app = FastAPI()



@@ -70,9 +71,12 @@ def show(id, response: Response, db: Session = Depends(get_db)):

    return blog











@app.post('/user')

def create_user(request: schemas.User,db: Session = Depends(get_db)):


    new_user = models.User(name=request.name,email=request.email,password=request.password)





    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))

    db.add(new_user)

    db.commit()

    db.refresh(new_user)