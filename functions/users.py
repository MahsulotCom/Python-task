from fastapi import HTTPException

from models.users import Users
from routes.auth import get_password_hash
from utils.pagination import pagination


def get_all_users(search, status, roll, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Users.name.like(search_formatted) | Users.number.like(search_formatted) | Users.username.like(
            search_formatted) | Users.roll.like(search_formatted)
    else:
        search_filter = Users.id > 0
    if status in [True, False]:
        status_filter = Users.status == status
    else:
        status_filter = Users.id > 0

    if roll:
        roll_filter = Users.roll == roll
    else:
        roll_filter = Users.id > 0

    users = db.query(Users).filter(search_filter, status_filter, roll_filter).order_by(Users.name.asc())
    if page and limit:
        return pagination(users, page, limit)
    else:
        return users.all()


def add_user(form, user, db):
    user_verification = db.query(Users).filter(Users.username == form.username).first()
    if user_verification:
        raise HTTPException(status_code=400, detail="Bunday foydalanuvchi mavjud")
    number_verification = db.query(Users).filter(Users.number == form.number).first()
    if number_verification:
        raise HTTPException(status_code=400, detail="Bunday telefon raqami  mavjud")

    if user.roll != "admin":
        raise HTTPException(status_code=400, detail="Sizga ruhsat berilmagan")
    new_user = Users(
        name=form.name,
        username=form.username,
        roll=form.roll,
        number=form.number,
        password=get_password_hash(form.password),

    )
    db.add(new_user)
    db.commit()
    return 1

def update_user(form, db):
    user_verification = db.query(Users).filter(Users.username == form.username).first()
    if user_verification:
        raise HTTPException(status_code=400, detail="Bunday foydalanuvchi mavjud")
    number_verification = db.query(Users).filter(Users.number == form.number).first()
    if number_verification:
        raise HTTPException(status_code=400, detail="Bunday telefon raqami  mavjud")
    db.query(Users).filter(Users.id == form.id).update({
        Users.username: form.username,
        Users.name: form.name,
        Users.number: form.number,
        Users.roll: form.roll,
        Users.password: get_password_hash(form.password),

    }

    )
    db.commit()


def delete_user(id, db):
    user_verification = db.query(Users).filter(Users.id == id).first()
    if not user_verification:
        raise HTTPException(status_code=400, detail="Bunday foydalanuvchi mavjud emas")

    db.query(Users).filter(Users.id == id).delete()
    db.commit()


"""



"""
