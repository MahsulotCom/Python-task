from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from mptt.admin import MPTTModelAdmin
from django.db.models import Count

from .models import Shop, Product, Category, ProductImage, User, Order


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_roles', 'staff_active')}), # Add 'user_roles' and 'staff_active' to user edit form in admin
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('username', 'email', 'password1', 'password2', 'user_roles', 'staff_active')}),
        # Add 'user_roles' and 'staff_active' to user creation form in admin
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_roles')  # Include 'staff_active' in list view


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_url', 'desc')
    search_fields = ('title',)


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('id', 'title', 'desc', 'parent')
    search_fields = ('id', 'title', 'parent__title')
    actions = ['add_parent_categories']

    def add_parent_categories(self, request, queryset):
        selected_categories = list(queryset)
        for category in selected_categories:
            parent_category = Category.objects.get(id=1)  # Replace 1 with the parent category ID you want to assign
            category.parent = parent_category
            category.save()
    add_parent_categories.short_description = 'Add Parent Categories'

    def get_paths_to_category(self, obj):
        paths = []
        for path in obj.get_ancestors(include_self=True):
            paths.append(' / '.join([ancestor.title for ancestor in path.get_ancestors(include_self=True)]))
        return ' / '.join(paths) if paths else 'No path found'
    get_paths_to_category.short_description = 'All Paths'


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'shop', 'amount', 'price', 'active')
    search_fields = ('id', 'title')
    list_filter = ('active', 'categories__title')
    readonly_fields = ('id',)  # Prevent editing the ID field in the admin
    inlines = [ProductImageInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Annotate the queryset with the number of orders for each product
        queryset = queryset.annotate(num_orders=Count('order'))
        # Sort the queryset first by number of orders (descending) and then by price (ascending)
        queryset = queryset.order_by('-num_orders', 'price')
        return queryset


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'sell_price')
    search_fields = ('product__title',)
    list_filter = ('product__shop',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Shop, ShopAdmin)




