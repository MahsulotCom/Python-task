from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import Group, Permission
from .models import Shop, Category, Product

ProductModeratorGroup, created = Group.objects.get_or_create(name='Product Moderator')
PageModeratorGroup, created = Group.objects.get_or_create(name='Page Moderator')

product_permissions = Permission.objects.filter(codename__startswith='moderate_product')
ProductModeratorGroup.permissions.add(*product_permissions)

page_permissions = Permission.objects.filter(codename__startswith='moderate_page')
PageModeratorGroup.permissions.add(*page_permissions)

class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_display')
    search_fields = ['title']
    readonly_fields = ['id']

    def image_display(self, obj):
        if obj.imageURL:
            return format_html('<img src="{}" width="100" />', obj.imageURL.url)
        return None

    image_display.allow_tags = True
    image_display.short_description = 'Image'

admin.site.register(Shop, ShopAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'parent')
    search_fields = ['title']
    readonly_fields = ['id']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'shop', 'description', 'amount', 'price', 'active', 'main_image')
    search_fields = ['title', 'id']
    list_filter = ['active', 'price']
    readonly_fields = ['id']
    filter_horizontal = ('category',)

    def main_image(self, obj):
        images = obj.get_images()
        if images:
            return '<img src="%s" width="100" />' % images[0]
        return ''
    main_image.allow_tags = True

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.groups.filter(name='Product Moderator').exists():
            # If user belongs to Product Moderator group, show only products for moderation
            return queryset.filter(moderation_needed=True)
        return queryset

admin.site.register(Product, ProductAdmin)
