from fastapi import FastAPI

from routes import auth,users

from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Shablon",
    responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
               401: {'desription': 'Unauthorized'}}
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {"message": "Welcome"}


app.include_router(
    auth.login_router,
    prefix='/auth',
    tags=['User auth section'])

app.include_router(
    users.user_router,
    prefix='/users',
    tags=['User  section'])


"""
from fastapi import APIRouter, Depends, HTTPException
from db import Base, engine, get_db

from sqlalchemy.orm import Session

from functions.incomes import add_income
from routes.auth import get_current_active_user

Base.metadata.create_all(bind=engine)

from functions.users import one_user, all_users, update_user, create_user, user_delete, user_current, \
    one_user_balance_show, add_user_balance, one_user_balance_history
from schemas.users import UserBase, UserCreate, UserUpdate, UserCurrent

router_user = APIRouter()


@router_user.post('/add', )
def add_user(form: UserCreate, db: Session = Depends(get_db),
             current_user: UserCurrent = Depends(get_current_active_user)):  #
    if create_user(form, current_user, db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@router_user.get('/', status_code=200)
def get_users(search: str = None, status: bool = True, id: int = 0, roll: str = None, page: int = 1, limit: int = 25,
              db: Session = Depends(get_db), current_user: UserCurrent = Depends(
            get_current_active_user)):  # current_user: User = Depends(get_current_active_user)
    if id:
        return one_user(id, db)
    else:
        return all_users(search, status, roll, page, limit, db)


@router_user.get('/user', status_code=200)
def get_user_current(db: Session = Depends(get_db), current_user: UserCurrent = Depends(
    get_current_active_user)):  # current_user: User = Depends(get_current_active_user)
    if current_user:
        return user_current(current_user, db)


@router_user.put("/update")
def user_update(form: UserUpdate, db: Session = Depends(get_db),
                current_user: UserCurrent = Depends(get_current_active_user)):
    if update_user(form, current_user, db):
        raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@router_user.delete('/{id}', status_code=200)
def delete_user(id: int = 0, db: Session = Depends(get_db),
                current_user: UserCurrent = Depends(get_current_active_user)):
    if id:
        return user_delete(id, db)


@router_user.get('/balance', status_code=200)
def get_user_balance(db: Session = Depends(get_db), current_user: UserCurrent = Depends(get_current_active_user)):
    return one_user_balance_show(current_user.id, db)


@router_user.post('/add_balance', )
def add_user_balances(money: float, type: str, db: Session = Depends(get_db),
                      current_user: UserCurrent = Depends(get_current_active_user)):  #
    add_user_balance(current_user, money, db)
    add_income(money=money, cur_user=current_user, db=db, type=type)
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli amalga oshirildi")


@router_user.get('/history', )
def add_user(page: int = 1, limit: int = 25, db: Session = Depends(get_db),
             current_user: UserCurrent = Depends(get_current_active_user)):  #

    return one_user_balance_history(id=current_user.id, page=page, limit=limit, db=db)


"""