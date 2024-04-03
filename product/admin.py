from django.contrib import admin
from django.utils.safestring import mark_safe

from product.models import Product, ProductImage


class ImageInline(admin.StackedInline):
    model = ProductImage
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "amount", "price", "active", "display_image", "display_categories")
    list_display_links = ('title',)
    search_fields = ("id", "title")
    list_editable = ('active', 'amount', 'price')
    inlines = [ImageInline]
    actions = ['set_active', 'set_deactive']
    list_filter = ("active", "price")
    ordering = ['price']
    list_per_page = 10

    def display_categories(self, obj):
        return ', '.join(category.title for category in obj.category.all())

    @admin.action(description="Deactivate selected products")
    def set_deactive(self, request, queryset):
        count = queryset.update(active=False)
        self.message_user(request, f"Deactivated {count} products")

    @admin.action(description="Activate selected products")
    def set_active(self, request, queryset):
        count = queryset.update(active=True)
        self.message_user(request, f"Activated {count} products")

    def display_image(self, obj):
        image = obj.product_image.first()
        if image:
            return mark_safe('<img src="{url}" width="100px" height="auto" />'.format(url=image.image.url))
        else:
            return 'No Image'

    display_image.short_description = 'Shop Image'
