from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response
from .. import schemas, models, database
from typing import List

router = APIRouter(tags=["Blog"],prefix='/blog')

#fetch all blogs
@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

#fetch a blog by id
@router.get('/{id}',status_code=200, response_model=schemas.ShowBlog)
def show(id, response: Response, db:Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"Blog with the {id} is not available")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'details':f"Blog with the {id} is not available"}
    return blog

#create blog
@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db : Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

#update a blog
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
    blog.update(request)
    db.commit()
    return 'updated successfully'

#delete blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
    
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'
