from admin_numeric_filter.admin import SliderNumericFilter, NumericFilterModelAdmin, RangeNumericFilter
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import Count
from django.utils.safestring import mark_safe
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from mptt.admin import DraggableMPTTAdmin

from .models import Shop, Product, Category, Image


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Price Range'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('0_100', 'Less than $100'),
            ('100_500', '$100 - $500'),
            ('500_1000', '$500 - $1000'),
            ('1000_', 'More than $1000'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0_100':
            return queryset.filter(price__lt=100)
        elif self.value() == '100_500':
            return queryset.filter(price__gte=100, price__lt=500)
        elif self.value() == '500_1000':
            return queryset.filter(price__gte=500, price__lt=1000)
        elif self.value() == '1000_':
            return queryset.filter(price__gte=1000)


class PhotoAdmin(admin.StackedInline):
    model = Image
    extra = 0
    min_num = 1


class CategoryAdmin(DraggableMPTTAdmin):
    search_fields = ('title', 'id', 'parent__title')


class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


class ProductAdmin(ModelAdmin):
    list_display = ('id', 'title', 'main_image', 'amount', 'price', 'active')
    search_fields = ('title', 'id')
    list_filter = [PriceRangeFilter, 'active']
    inlines = (PhotoAdmin,)

    def main_image(self, obj):
        return mark_safe(
            f'<a href="http://localhost:8000/admin/app/product/{obj.id}/change/"><img src="{obj.product_images.first().image_url}" height="50" /></a>')

    main_image.allow_tags = True
    main_image.short_description = 'Main Image'


# def has_module_permission(self, request):
#     if request.user.is_moderator:
#         return True
#


admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
