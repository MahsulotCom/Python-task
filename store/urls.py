from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import ShopViewSet, ProductViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r'shops', ShopViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
