from django.urls import path

from dashboard import views

app_name = "dashboard"

urlpatterns = [
    path('register/signup/', views.SignUpView.as_view(), name="signup"),
    path('home/', views.home_page, name="home"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_page, name="logout_page"),

    path('category/create/', views.category_create, name="category_create"),
    path('category/<int:pk>/edit/', views.category_edit, name="category_edit"),
    path('category/<int:pk>/delete/', views.category_delete, name="category_delete"),
    path('category/list/', views.category_list, name="category_list"),

    path('shop/create/', views.shop_create, name="shop_create"),
    path('shop/<int:pk>/edit/', views.shop_edit, name="shop_edit"),
    path('shop/<int:pk>/delete/', views.shop_delete, name="shop_delete"),
    path('shop/list/', views.shop_list, name="shop_list"),

    path('product/create/', views.product_create, name="product_create"),
    path('product/<int:pk>/edit/', views.product_edit, name="product_edit"),
    path('product/<int:pk>/delete/', views.product_delete, name="product_delete"),
    path('product/list/', views.product_list, name="product_list"),

    path('image/create/', views.image_create, name="image_create"),
    path('image/<int:pk>/edit/', views.image_edit, name="image_edit"),
    path('image/<int:pk>/delete/', views.image_delete, name="image_delete"),
    path('image/list/', views.image_list, name="image_list"),
]
