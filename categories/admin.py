# admin.py
from django.contrib import admin
from .models import Category
from .models import Product


class ProductInline(admin.TabularInline):
    model = Product
    fields = ("title", "price", "amount", "active")
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "parent_category",
        "display_paths",
    )

    inlines = [
        ProductInline,
    ]

    # Adjusted search_fields to traverse the relationship from Product to Category
    search_fields = ("product__id", "product__title", "parent_category__title")

    def display_paths(self, obj):
        # get_all_paths is a method on the Category model
        paths = obj.get_all_paths()
        return paths
