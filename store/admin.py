from django.contrib import admin
from django.utils.html import format_html

from store.models import Category, Product, Shop, Images


class ImagesAdmin(admin.TabularInline):
    model = Images


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'parent']
    search_fields = ('title', 'parent')
    list_display_links = ('id', 'title', 'parent')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'get_first_image')
    search_fields = ('title', 'id')
    list_filter = ('is_active', 'price')
    ordering = ('-order_items', 'price')

    def get_first_image(self, obj):
        if obj.product_images.exists():
            image_url = "http://127.0.0.1:8000/" + obj.product_images.first().image.url
            return format_html('<img src="{}" style="max-height:1000px; max-width:1000px;" />'.format(image_url))
        return ''

    get_first_image.short_description = 'Main Image'

    inlines = [ImagesAdmin]


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
    list_display_links = ('id', 'title')
