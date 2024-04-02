from django.contrib import admin
from apps.shop.models import Shop



@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    ordering = ('title',)