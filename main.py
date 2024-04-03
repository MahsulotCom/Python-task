from fastapi import FastAPI

from routes import auth,users,shop,category,product

from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Online store api",
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

app.include_router(
    shop.shop_router,
    prefix='/shop',
    tags=['Shop  section'])

app.include_router(
    category.category_router,
    prefix='/category',
    tags=['Category  section'])

app.include_router(
    product.product_router,
    prefix='/product',
    tags=['Product  section'])