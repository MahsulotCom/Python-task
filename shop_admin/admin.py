from django.contrib import admin
from .models import Category, Shop, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ['title', 'id', 'parents__title']
    filter_horizontal = ('parents',)
   
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at') 
    search_fields = ['title']
    exclude = ['id'] 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'amount', 'price', 'active', 'created_at')
    list_filter = ('active', 'price')
    search_fields = ('id', 'title')
    readonly_fields = ('id',)
    filter_horizontal = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
