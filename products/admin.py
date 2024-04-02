from django.contrib import admin
from .models import Product
from django.utils.html import format_html
from .filters import PriceRangeFilter


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "main_image",
        "category",
        "shop",
        "price",
        "number_of_orders",
    )

    search_fields = ("id", "title")
    exclude = ("id",)
    list_filter = ("active", PriceRangeFilter)
    ordering = ("-number_of_orders", "price")

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
