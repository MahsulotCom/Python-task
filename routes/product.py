import inspect
import shutil
import typing
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from functions.product import all_products, add_product, update_product, delete_product, one_product
from db import get_db

from pydantic.datetime_parse import date
from routes.auth import get_current_active_user
from schemas.users import UserCurrent
from utils.role_verification import roll_verification
from functions.files import add_file, update_file, file_delete

product_router = APIRouter()


@product_router.get("", status_code=200)
async def all_product(
        filter: typing.Literal['amount', 'real_price', 'trade_price'],
        sort: typing.Literal["desc", "asc"],
        search: str = None,
        active: bool = None,
        category_id: int = 0,
        id: int = 0,
        start_date: date = None, end_date: date = None,
        page: int = 1, limit: int = 20,
        db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    roll_verification(current_user, inspect.currentframe().f_code.co_name)
    if id:
        return one_product(db=db, id=id)

    return all_products(search=search, active=active, field=filter, sort=sort, category_id=category_id,
                        start_date=start_date, end_date=end_date, page=page, limit=limit,
                        db=db)


@product_router.post("/add")
async def product_add(title: str,
                      unit: typing.Literal["Dona", "Metr", "Kilo"],
                      category_id: int,
                      real_price: float,
                      trade_price: float,
                      amount: float,
                      description: typing.Optional[str] = None,
                      files: typing.Optional[typing.List[UploadFile]] = File(None)
                      , db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    roll_verification(current_user, inspect.currentframe().f_code.co_name)
    new_product = add_product(title=title, unit=unit, real_price=real_price, trade_price=trade_price,
                              category_id=category_id,
                              amount=amount, thisuser=current_user
                              , db=db, description=description)

    if files:
        for file in files:
            with open("media/" + file.filename, 'wb') as image:
                shutil.copyfileobj(file.file, image)
            url = str('media/' + file.filename)
            add_file(source_id=new_product.id, source='product', file_url=url, user=current_user, db=db)

    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@product_router.put("/update")
async def product_update(
        id: int,
        title: str,
        unit: typing.Literal["Dona", "Metr", "Kilo"],
        category_id: int,
        real_price: float,
        trade_price: float,
        amount: float,
        description: typing.Optional[str] = None,
        files: typing.Optional[typing.List[UploadFile]] = File(None), db: Session = Depends(get_db),
        current_user: UserCurrent = Depends(
            get_current_active_user)):
    new_product = update_product(id=id, title=title, unit=unit, real_price=real_price, trade_price=trade_price,
                                 category_id=category_id,
                                 amount=amount, thisuser=current_user
                                 , db=db, description=description)
    if files:
        for file in files:
            with open("media/" + file.filename, 'wb') as image:
                shutil.copyfileobj(file.file, image)
            url = str('media/' + file.filename)
            update_file(source_id=new_product.id, source='product', image_url=url, user=current_user, db=db, )


@product_router.delete("/delete")
async def product_delete(id: int, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    roll_verification(current_user, inspect.currentframe().f_code.co_name)
    file_delete(source_id=id, source='product', db=db)
    return delete_product(id=id, db=db)
