import datetime
from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.product import Product
from utils.pagination import pagination


def all_products(active, search, start_date, end_date, page, limit, db):
    products = db.query(Product).options(joinedload(Product.user))
    if search:
        search_formatted = "%{}%".format(search)
        products = products.filter(
            Product.price.ilike(search_formatted) | Product.trade_price.ilike(search_formatted))

    if active in [True, False]:
        products = products.filter(Product.active == active)

    try:
        if not start_date:
            start_date = datetime.date.min
        if not end_date:
            end_date = datetime.date.today()
        end_date = datetime.datetime.strptime(str(end_date), '%Y-%m-%d').date() + datetime.timedelta(days=1)
        products = products.filter(Product.created_at >= start_date, Product.created_at <= end_date)
    except Exception as error:
        raise HTTPException(status_code=400, detail="Faqat yyyy-mmm-dd formatida yozing  ")
    products = products.order_by(Product.id.desc())
    return pagination(products, page, limit)


def one_product(db, id):
    product = db.query(Product).options(joinedload(Product.user),
                                        ).filter(Product.id == id).first()
    if product:
        return product
    raise HTTPException(status_code=400, detail="bunday maxsulot mavjud emas")


def create_product(title, unit, real_price, trade_price, category_id, amount, thisuser, db, description: str = None, ):
    new_product_db = Product(
        title=title,
        unit=unit,
        real_price=real_price,
        trade_price=trade_price,
        category_id=category_id,
        amount=amount,
        description=description,
        user_id=thisuser.id
    )
    db.add(new_product_db)
    db.flush()
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def update_product(id,title, unit, real_price, trade_price, category_id, amount, thisuser, db, description: str = None,):
    one_product(db=db, id=id)
    db.query(Product).filter(Product.id ==  id).update({
        Product.title: title,
        Product.unit:  unit,
        Product.real_price:  real_price,
        Product.trade_price:  trade_price,
        Product.category_id:  category_id,
        Product.amount:  amount,
        Product.description:  description,
        Product.user_id: thisuser.id
    })

    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")


def delete_user(id, db):
    one_product(db=db, id=id)
    db.query(Product).filter(Product.id == id).update({
        Product.active: False, })
    db.commit()
    raise HTTPException(status_code=200, detail=f"Amaliyot muvaffaqiyatli bajarildi")