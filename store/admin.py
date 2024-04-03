from django.contrib import admin
from django.db import models
from django.utils.html import format_html

from store.models import Shop, Category, Product, ProductImage
from store.filters import PriceRangeFilter


class ShopAdmin(admin.ModelAdmin):
    """Admin configuration for the Shop model."""

    list_display = ["title", "render_image"]
    search_fields = ["title"]
    readonly_fields = ["id"]

    def render_image(self, obj):
        """Render the image in the admin panel."""
        return format_html('<img src="%s" width="15" />' % obj.image.url)

    render_image.short_description = "Image"


class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for the Category model."""

    list_display = ["title", "get_parent_categories"]
    search_fields = ["id", "title", "parent_categories__title"]
    filter_horizontal = ["parent_categories"]
    readonly_fields = ["id", "get_possible_paths"]

    def get_possible_paths(self, obj):
        """Get the possible paths for the category."""
        return ", ".join(str(path) for path in obj.get_possible_paths())

    get_possible_paths.short_description = "Possible Paths"

    def get_parent_categories(self, obj):
        """Get the parent categories of the category."""
        return ", ".join([category.title for category in obj.parent_categories.all()])


class ProductImageInline(admin.TabularInline):
    """Inline configuration for the ProductImage model."""

    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for the Product model."""

    list_display = ["title", "price", "amount", "render_main_image"]
    search_fields = ["id", "title"]
    readonly_fields = ["id", "render_main_image_on_change"]
    list_filter = ["is_active", PriceRangeFilter, "categories"]
    ordering = ["-amount", "price"]
    filter_horizontal = ["categories"]
    actions = ["make_active", "make_inactive"]

    inlines = [ProductImageInline]
    formfield_overrides = {
        models.ManyToManyField: {
            "widget": admin.widgets.FilteredSelectMultiple(
                "Categories", is_stacked=False
            )
        },
    }

    def render_main_image(self, obj):
        """Render the main image in the admin panel."""
        return format_html('<img src="%s" width="15" />' % obj.get_main_image())

    render_main_image.short_description = "Main image"

    def render_main_image_on_change(self, obj):
        """Render the main image on the change form."""
        return format_html('<img src="%s" width="200" />' % obj.get_main_image())

    render_main_image_on_change.short_description = "Main image"

    @admin.action(description="Make selected products active")
    def make_active(self, request, queryset):
        """Action to make selected products active."""
        queryset.update(is_active=True)

    @admin.action(description="Make selected products inactive")
    def make_inactive(self, request, queryset):
        """Action to make selected products inactive."""
        queryset.update(is_active=False)
