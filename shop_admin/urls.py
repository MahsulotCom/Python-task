from django.urls import path
from .views import CategoryListView, CategoryUpdateView, CategoryDeleteView
urlpatterns = [
    path('', CategoryListView.as_view(), name='home_page'), 
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete'),
]
