from . import schemas, models


from .database import engine, SessionLocal

from sqlalchemy.orm import Session


from .hashing import Hash



@app.post('/user')



@app.post('/user', response_model=schemas.ShowUser)

db.close()







@app.post('/blog', status_code=status.HTTP_201_CREATED)


@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])

def create(request: schemas.Blog, db: Session = Depends(get_db)):

    new_blog = models.Blog(title=request.title, body=request.body)

    db.add(new_blog)

@@ -27,7 +27,7 @@ def create(request: schemas.Blog, db: Session = Depends(get_db)):

    return new_blog






@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])

def destroy(id, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id)



@@ -40,7 +40,7 @@ def destroy(id, db: Session = Depends(get_db)):

    return 'done'






@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])

def update(id, request: schemas.Blog, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id)



@@ -53,13 +53,13 @@ def update(id, request: schemas.Blog, db: Session = Depends(get_db)):

    return 'updated'






@app.get('/blog', response_model=List[schemas.ShowBlog])


@app.get('/blog', response_model=List[schemas.ShowBlog],tags=['blogs'])

def all(db: Session = Depends(get_db)):

    blogs = db.query(models.Blog).all()

    return blogs






@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)


@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog,tags=['blogs'])

def show(id, response: Response, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:

@@ -73,7 +73,7 @@ def show(id, response: Response, db: Session = Depends(get_db)):








@app.post('/user', response_model=schemas.ShowUser)


@app.post('/user', response_model=schemas.ShowUser,tags=['users'])

def create_user(request: schemas.User,db: Session = Depends(get_db)):



    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))

@@ -82,7 +82,7 @@ def create_user(request: schemas.User,db: Session = Depends(get_db)):

    db.refresh(new_user)

    return new_user




@app.get('/user/{id}',response_model=schemas.ShowUser)


@app.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])

def get_user(id:int,db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user: