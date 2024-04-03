from django.contrib import admin

from product.models import Category, Product, Shop, Images


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'parent')
    list_display_links = ('id', 'title', 'description')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('id', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'amount', 'price', 'is_active', 'product_shop')
    list_display_links = ('id', 'title', 'amount')
    list_filter = ('is_active', )


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_main', 'product')
    list_display_links = ('id', 'is_main')
    list_filter = ('is_main', )

