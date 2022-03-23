
from fastapi import Depends, FastAPI, HTTPException, status, Response

from blog.routers import user
from . import schemas, models
from .hashing import Hash
from .database import engine
from sqlalchemy.orm import Session
from .routers import blog,user,authentication


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
#get db connection
#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()
#create blog
#@app.post('/blog',status_code=status.HTTP_201_CREATED,tags=["Blog"])
#def create(request:schemas.Blog, db : Session = Depends(get_db)):
#    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
#    db.add(new_blog)
#    db.commit()
#    db.refresh(new_blog)
#    return new_blog
#
##update a blog
#@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Blog"])
#def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#    blog = db.query(models.Blog).filter(models.Blog.id == id)
#    if not blog.first():
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
#    blog.update(request)
#    db.commit()
#    return 'updated successfully'
#
##delete blog
#@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=["Blog"])
#def destroy(id, db: Session = Depends(get_db)):
#    blog = db.query(models.Blog).filter(models.Blog.id == id)
#    if not blog.first():
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
#    
#    blog.delete(synchronize_session=False)
#    db.commit()
#    return 'done'
#
##fetch all blogs
#@app.get('/blog',response_model=List[schemas.ShowBlog],tags=["Blog"])
#def all(db: Session = Depends(get_db)):
#    blogs = db.query(models.Blog).all()
#    return blogs
#
##fetch a blog by id
#@app.get('/blog/{id}',status_code=200, response_model=schemas.ShowBlog, tags=["Blog"])
#def show(id, response: Response, db:Session = Depends(get_db)):
#    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#    if not blog:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"Blog with the {id} is not available")
#        #response.status_code = status.HTTP_404_NOT_FOUND
#        #return {'details':f"Blog with the {id} is not available"}
#    return blog
#
#
#create a user
#@app.post('/user', response_model=schemas.ShowUser, tags=["User"])
#def create_user(request: schemas.User, db: Session = Depends(get_db)):
#    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#    db.add(new_user)
#    db.commit()
#    db.refresh(new_user)
#    return new_user
#
## fetch a user by id
#@app.get('/user/{id}',response_model=schemas.ShowUser, tags=["User"])
#def get_user(id:int, db:Session = Depends(get_db)):
#    user = db.query(models.User).filter(models.User.id == id).first()
#    if not user:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
#    return user
