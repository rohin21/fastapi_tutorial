from .. import database,schemas
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(tags=["User"],prefix="/user")
#create a user
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create_user(request,db)

# fetch a user by id
@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(database.get_db)):
    return user.get_user(id,db)