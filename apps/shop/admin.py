from django.contrib import admin
from apps.shop.models import Shop



@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'thumbnail_preview')
    search_fields = ('title',)
    ordering = ('title',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview