import inspect
import shutil
import typing
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from functions.shop import all_shops, add_shop, update_shop, delete_shop
from db import get_db

from pydantic.datetime_parse import date
from routes.auth import get_current_active_user
from schemas.users import UserCurrent
from utils.role_verification import roll_verification
from functions.files import add_file, update_file, file_delete

shop_router = APIRouter()


@shop_router.get("", status_code=200)
async def all_shop(search: str = None,
                   page: int = 1, limit: int = 20,
                   db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    roll_verification(current_user, inspect.currentframe().f_code.co_name)
    return all_shops(search=search, page=page, limit=limit,
                     db=db)


@shop_router.post("/add")
async def shop_add(title: str,
                   description: typing.Optional[str] = None,
                   file: typing.Optional[UploadFile] = File(None)
                   , db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    roll_verification(current_user, inspect.currentframe().f_code.co_name)
    new_shop = add_shop(title=title, thisuser=current_user
                        , db=db, description=description)
    print(file,'ddddddddddddddddddddddddddddddddddddd')
    if file:
        with open("media/" + file.filename, 'wb') as image:
            shutil.copyfileobj(file.file, image)
        url = str('media/' + file.filename)
        add_file(source_id=new_shop.get('id'), source='shop', file_url=url, user=current_user, db=db)



    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@shop_router.put("/update")
async def shop_update(
        id: int,
        title: str,
        description: typing.Optional[str] = None,
        files: typing.Optional[typing.List[UploadFile]] = File(None), db: Session = Depends(get_db),
        current_user: UserCurrent = Depends(
            get_current_active_user)):
    new_shop = update_shop(id=id, title=title,thisuser=current_user
                           , db=db, description=description)
    if files:
        for file in files:
            with open("media/" + file.filename, 'wb') as image:
                shutil.copyfileobj(file.file, image)
            url = str('media/' + file.filename)
            update_file(source_id=new_shop.id, source='shop', image_url=url, user=current_user, db=db, )


@shop_router.delete("/delete")
async def shop_delete(id: int, db: Session = Depends(get_db),current_user: UserCurrent = Depends(
    get_current_active_user)):
    file_delete(source_id=id, source='shop', db=db)
    return delete_shop(id=id, db=db)
