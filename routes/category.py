from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from functions.category import all_categorys, add_category, update_category, delete_category
from db import get_db

from routes.auth import get_current_active_user
from schemas.category import CategoryCreate, CategoryUpdate
from schemas.users import UserCurrent

category_router = APIRouter()


@category_router.get("", status_code=200)
async def all_category(search: str = None, active: bool = True, page: int = 1, limit: int = 20,
                       db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):

    return all_categorys(search=search,active=active,  page=page, limit=limit, db=db,)


@category_router.post("/add")
async def category_add(form: CategoryCreate, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    if add_category(form=form, thisuser=current_user, db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@category_router.put("/update")
async def category_update(form: CategoryUpdate, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    return update_category(form=form, thisuser=current_user, db=db)


@category_router.delete("/delete")
async def category_delete(id: int, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    return delete_category(id=id, db=db)
