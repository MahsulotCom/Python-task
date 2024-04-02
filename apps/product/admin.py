from django.contrib import admin
from apps.product.models import *



@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('value',)
    search_fields = ('value',)
    ordering = ('value',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'shop', 'is_available', 'is_new')
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_available', 'description', 'price', 'quantity')
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(ProductVariantImage)
class ProductVariantImageAdmin(admin.ModelAdmin):
    list_display = ('product_variant','order')
    search_fields = ('product_variant.title',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'percent', 'is_active', 'start_date', 'end_date')
    search_fields = ('name',)
    ordering = ('name',)