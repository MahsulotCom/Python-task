from django.urls import path
from .views import CategoryListView, CategoryUpdateView, CategoryDeleteView, ShopListView, ShopUpdateView, ShopDeleteView
urlpatterns = [
    path('', CategoryListView.as_view(), name='home_page'), 
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete'),
    path('shops/', ShopListView.as_view(), name='shops_page'), 
    path('shops/update/<int:pk>/', ShopUpdateView.as_view(), name='update'),
    path('shops/delete/<int:pk>/', ShopDeleteView.as_view(), name='delete'),
]
