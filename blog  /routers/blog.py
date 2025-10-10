from fastapi import APIRouter,Depends,status,HTTPException


from .. import schemas, database, models

from sqlalchemy.orm import Session


router = APIRouter()








router = APIRouter(


    prefix="/blog",


    tags=['Blogs']


)




get_db = database.get_db




@router.get('/blog', response_model=List[schemas.ShowBlog],tags=['blogs'])


@router.get('/', response_model=List[schemas.ShowBlog])

def all(db: Session = Depends(get_db)):

    blogs = db.query(models.Blog).all()

    return blogs






@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])


@router.post('/', status_code=status.HTTP_201_CREATED)

def create(request: schemas.Blog, db: Session = Depends(get_db)):

    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)

    db.add(new_blog)

    db.commit()

    db.refresh(new_blog)

    return new_blog




@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)

def destroy(id, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id)



@@ -32,7 +38,7 @@ def destroy(id, db: Session = Depends(get_db)):

    return 'done'






@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)

def update(id, request: schemas.Blog, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id)



@@ -45,7 +51,7 @@ def update(id, request: schemas.Blog, db: Session = Depends(get_db)):

    return 'updated'






@router.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog,tags=['blogs'])


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)

def show(id, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:

