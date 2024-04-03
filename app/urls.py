from django.urls import path

from app.views import products_view, categories_view, edit_shop, edit_product, shop_view

urlpatterns = [
    path('', shop_view, name='index'),
    path('edit_shop/<int:shop_id>/', edit_shop, name='edit_shop'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path("products/", products_view, name="products"),
    path("categories/", categories_view, name="categories"),

]
