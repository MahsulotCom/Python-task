from django.contrib import admin

from .models import ProductImages, Product, Category, Shop


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    list_display_links = ('title',)
    search_fields = ("id", "title", "parent__title")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "amount", "price", "active", "get_image")
    list_display_links = ('title',)
    search_fields = ("id", "title")

    def get_image(self, product):
        image = product.images.first()
        if image:
            return image.url


@admin.register(ProductImages)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "url")
    search_fields = ("id",)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image")
    search_fields = ("id", "title")
