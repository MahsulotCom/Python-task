from fastapi import HTTPException
from models.shop import Shop
from utils.pagination import pagination
from sqlalchemy.orm import joinedload


def all_shops(search, page, limit, db):
    """


    :param search:
    :param page:
    :param limit:
    :param db:
    :return:
    .join ( Phones ).outerjoin ( Orders ).options (
            joinedload ( Customers.social ).load_only ( SocialMedia.name, SocialMedia.link ),
    """
    shops = db.query(Shop).options(joinedload(Shop.shop_image))
    if search:
        search_formatted = "%{}%".format(search)
        shops = shops.filter(
            Shop.title.ilike(search_formatted))

    shops = shops.order_by(Shop.id.desc())
    return pagination(shops, page, limit)


def one_shop(db, id):
    shop = db.query(Shop).filter(Shop.id == id).first()
    if shop:
        return shop
    raise HTTPException(status_code=400, detail="Bunday do'kon mavjud emas")


def add_shop(title, thisuser, db, description: str = None, ):
    new_shop_db = Shop(
        title=title,
        description=description,
        user_id=thisuser.id
    )
    db.add(new_shop_db)
    db.flush()
    db.commit()
    return {"id":new_shop_db.id}
    # raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def update_shop(id, title, thisuser, db, description: str = None, ):
    one_shop(db=db, id=id)
    db.query(Shop).filter(Shop.id == id).update({
        Shop.title: title,
        Shop.description: description,
        Shop.user_id: thisuser.id
    })

    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def delete_shop(id, db):
    one_shop(db=db, id=id)
    db.query(Shop).filter(Shop.id == id).delete()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")
