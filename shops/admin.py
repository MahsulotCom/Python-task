from django.contrib import admin
from .models import Shop
from products.models import Product

from django.utils.html import format_html


class ProductInline(admin.TabularInline):
    model = Product
    fields = ("title", "price", "amount", "active")
    extra = 0


# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("title", "main_image", "created_at", "updated_at")
    search_fields = ("title",)
    exclude = ("id",)

    inlines = [
        ProductInline,
    ]

    def main_image(self, obj):
        # get_image_files is a method defined in models.py
        image_files = obj.get_image_files(obj)

        if image_files:
            return format_html(
                '<a href="{}">{}</a>',
                image_files[0],
                image_files[0].split("/")[-1],
            )
        else:
            return "-"

    main_image.short_description = "Main Image"
    main_image.allow_tags = True
