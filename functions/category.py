from fastapi import HTTPException


from models.category import Category
from utils.pagination import pagination


def all_categorys(active, search, page, limit, db):
    categorys = db.query(Category)
    if search:
        search_formatted = "%{}%".format(search)
        categorys = categorys.filter(
            Category.title.ilike(search_formatted))

    if active in [True, False]:
        categorys = categorys.filter(Category.active == active)

    categorys = categorys.order_by(Category.id.desc())
    return pagination(categorys, page, limit)


def one_category(db, id):
    category = db.query(Category).filter(Category.id == id).first()
    if category:
        return category
    raise HTTPException(status_code=400, detail="Bunday kategoriya mavjud emas")


def add_category(form, thisuser, db,  ):
    new_category_db = Category(
        title=form.title,
        description=form.description,
        user_id=thisuser.id
    )
    db.add(new_category_db)
    db.flush()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def update_category(form,  thisuser, db,):
    one_category(db=db, id=form.id)
    db.query(Category).filter(Category.id == form.id).update({
        Category.title: form.title,
        Category.unit: form.description,
        Category.user_id: thisuser.id
    })

    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")

def delete_category(id, db):
    one_category(db=db, id=id)
    db.query(Category).filter(Category.id == id).update({
        Category.active: False, })
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")