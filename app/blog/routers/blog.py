from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response
from .. import schemas, models, database, oauth2
from typing import List
from ..repository import blog

router = APIRouter(tags=["Blog"],prefix='/blog')

#fetch all blogs
@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

#fetch a blog by id
@router.get('/{id}',status_code=200, response_model=schemas.ShowBlog)
def show(id:int, response: Response, db:Session = Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id,db)

#create blog
@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db : Session = Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)

#update a blog
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

#delete blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(db,id)
