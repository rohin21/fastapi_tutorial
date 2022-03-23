from .. import models, database,schemas
from fastapi import APIRouter,HTTPException, status,Depends
from ..hashing import Hash
from sqlalchemy.orm import Session



router = APIRouter(tags=["User"],prefix="/user")
#create a user
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# fetch a user by id
@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    return user
