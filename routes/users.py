import shutil
import typing
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from functions.users import get_all_users,add_user,update_user,delete_user
from db import get_db
from models.files import Files
from models.users import Users
from routes.auth import get_current_active_user, get_password_hash
from schemas.users import UserCreate, UserUpdate, UserCurrent

user_router = APIRouter()


@user_router.get("",status_code=200)
async def all_users(search: str = None, status: bool = True,  roll: str = None, page: int = 1, limit: int = 25,
              db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    return get_all_users(search=search,status=status,roll=roll,page=page,limit=limit,db=db)


@user_router.post("/add")
async def user_add(name:str,
                   username:str,
                   roll:str,
                   password:str,
                   number:str,
                   files: typing.Optional[typing.List[UploadFile]] = File (None)
                   , db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    new_user = Users(
        name=name,
        username=username,
        roll=roll,
        number=number,
        password=get_password_hash(password),

    )
    db.add(new_user)
    db.commit()

    if files:
        for file in files:
            with open("media/" + file.filename, 'wb') as image:
                shutil.copyfileobj(file.file, image)
            url = str('media/' + file.filename)
            new_file = Files(
                name=file.filename,
                source_id=new_user.id,
                source="user",
                url= url,
                user_id=new_user.id

            )
            db.add(new_file)
            db.commit()




    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")

"""

files: typing.Optional[List[UploadFile]] = File ( None ),
    if source == 'created':
        db.query ( Orders ).filter ( Orders.id == id ).update ( {
            Orders.id: id,
            Orders.user_id: user.id,
            Orders.order_status: order_status,
            Orders.updated_day: datetime.datetime.now ( ).date ( ),
            Orders.created_date: datetime.datetime.now ( ).date ( )} )
        db.commit ( )
        


"""


@user_router.put("/update")
async def user_update(form:UserUpdate,db: Session = Depends(get_db)):
    return update_user(form=form,db=db)

@user_router.delete("/delete")
async def user_delete(id:int,db: Session = Depends(get_db)):
    return delete_user(id=id,db=db)