from django.contrib import admin

from .models import Shop, Product, Category


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'imageUrl')
    search_fields = ('title',)
    list_filter = ()
    readonly_fields = ('id',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'imageUrl')
        }),
        ('Shop Image', {
            'fields': ('imageUrl',)
        }),
    )

    def has_add_permission(self, request):
        return False


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'amount', 'price', 'active')
    search_fields = ('title', 'id')
    list_filter = ('active', 'price')
    readonly_fields = ('id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'parent_category')
    search_fields = ('title', 'parent_category__title')
    readonly_fields = ('id',)
