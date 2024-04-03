from django.contrib import admin, messages

from .models import ProductImages, Product, Category, Shop


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_display_links = ('title',)
    search_fields = ("id", "title", "parent__title")
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "amount", "price", "active", "get_image", "display_categories")
    list_display_links = ('title',)
    search_fields = ("id", "title")
    list_editable = ('active', 'amount', 'price')
    list_per_page = 10
    actions = ['set_active', 'set_deactive']
    list_filter = ("active", "category__title")

    def display_categories(self, obj):
        return ', '.join(category.title for category in obj.category.all())

    display_categories.short_description = 'Категории'

    @admin.action(description="Деактировать выбранные записьи")
    def set_deactive(self, request, queryset):
        count = queryset.update(active=False)
        self.message_user(request, f"Деактивирован {count} записи", messages.WARNING)

    @admin.action(description="Актировать выбранные записьи")
    def set_active(self, request, queryset):
        count = queryset.update(active=True)
        self.message_user(request, f"Активирован {count} записи")

    def get_image(self, product):
        image = product.images.first()
        if image:
            return image.url


@admin.register(ProductImages)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("product", "url")
    search_fields = ("id",)
    list_display_links = ('product',)
    list_per_page = 10


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image")
    search_fields = ("id", "title")
    list_display_links = ('title',)
    list_per_page = 10
