import inspect

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from functions.users import all_users, add_user, update_user, delete_user
from db import get_db

from routes.auth import get_current_active_user
from schemas.users import UserCreate, UserUpdate, UserCurrent
from utils.role_verification import roll_verification

user_router = APIRouter()


@user_router.get("", status_code=200)
async def get_all_user(search: str = None, active: bool = None, roll: str = None, page: int = 1, limit: int = 20,
                        db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):
    roll_verification(current_user, inspect.currentframe().f_code.co_name)
    return all_users(search=search, active=active, roll=roll, page=page, limit=limit, db=db)


@user_router.post("/add")
async def user_add(form: UserCreate, db: Session = Depends(get_db),current_user: UserCurrent = Depends(
            get_current_active_user) ):
    roll_verification(current_user, inspect.currentframe().f_code.co_name)
    if add_user(form=form, db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@user_router.put("/update")
async def user_update(form: UserUpdate, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    roll_verification(current_user, inspect.currentframe().f_code.co_name)
    return update_user(form=form, db=db)


@user_router.delete("/delete")
async def user_delete(id: int, db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):
    roll_verification(current_user, inspect.currentframe().f_code.co_name)
    return delete_user(id=id, db=db)
