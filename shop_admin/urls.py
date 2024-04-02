from django.urls import path
from .views import CategoryListView, CategoryUpdateView, CategoryDeleteView, ShopListView, ShopUpdateView, ShopDeleteView, ProductListView, ProductUpdateView ,ProductDeleteView
urlpatterns = [
    path('', CategoryListView.as_view(), name='home_page'), 
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete'),
    path('shops/', ShopListView.as_view(), name='shops_page'), 
    path('shops/update/<int:pk>/', ShopUpdateView.as_view(), name='update'),
    path('shops/delete/<int:pk>/', ShopDeleteView.as_view(), name='delete'),
    path('products/', ProductListView.as_view(), name='products_page'), 
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
]
