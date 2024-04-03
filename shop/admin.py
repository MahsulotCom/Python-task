from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "display_image")
    search_fields = ("title",)
    list_per_page = 10
    list_editable = ('title', 'description')

    def display_image(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="100px" height="auto" />'.format(url=obj.image.url))
        else:
            return 'No Image'

    display_image.short_description = 'Shop Image'
