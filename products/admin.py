from django.contrib import admin

from products import models, filters


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
    )
    search_fields = (
        "id",
        "title",
        "parent__title",
    )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "amount",
        "price",
        "active",
        "get_first_image",
    )
    list_filter = ("active", filters.PriceRangeFilter)
    search_fields = (
        "id",
        "title",
    )

    # get first image's url if it exists
    def get_first_image(self, object):
        image = object.images.order_by("id").first()
        if image:
            return image.url


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "url",
    )
    search_fields = ("id",)


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "image",
    )
    search_fields = (
        "id",
        "title",
    )
