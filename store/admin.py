from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Shop)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'amount', 'amount_status', 'image']
    list_editable = ['price']
    list_per_page = 20
    search_fields = ['id', 'title']

    @admin.display(ordering='amount')
    def amount_status(self, product):
        if product.amount < 10:
            return 'Low'
        return 'OK'


@admin.register(models.Category)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['title']

# admin.site.register(models.Shop)
# admin.site.register(Product)
# admin.site.register(models.Category)