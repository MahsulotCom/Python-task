from django.contrib import admin
from .models import Shop, Product, ProductImage, Category, Orders
from django.db import models 
from django.db.models import Q



class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)  
    search_fields = ['title']  # to search by title
    
    # Customize the form for editing
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
    )
    readonly_fields = ('id',) 
    
    
    
    

class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Price Range'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('0-50', '0 - 50'),
            ('50-100', '50 - 100'),
            ('100-200', '100 - 200'),
            ('200-', '200 and above'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-50':
            return queryset.filter(price__gte=0, price__lte=50)
        elif self.value() == '50-100':
            return queryset.filter(price__gte=50, price__lte=100)
        elif self.value() == '100-200':
            return queryset.filter(price__gte=100, price__lte=200)
        elif self.value() == '200-':
            return queryset.filter(price__gte=200)
        else:
            return queryset


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'orders', 'get_main_image', )
    search_fields = ['id', 'title']  # to search by id and title
    readonly_fields = ('get_main_image','id',)  # Make main image and id read-only
    ordering = ('-orders', '-price')
    list_filter = ('active', PriceRangeFilter)
    
    def get_main_image(self, obj):
        if obj.images.exists():
            main_image = obj.images.first()
            return (main_image.image.url)
        else:
            return 'No Image'
    get_main_image.allow_tags = True
    get_main_image.short_description = 'Main Image'
    
    
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )
    search_fields = ['id', 'title', ]  # search by category ID, title, and parent category




admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Orders)