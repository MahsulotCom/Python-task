from django.contrib import admin
from django.db.models import Case, When
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from mptt.admin import MPTTModelAdmin

from apps.common.mixins import ImageFieldMixin
from apps.main.models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = (
        "title",
        "order",
        "get_paths",
    )
    search_fields = ("title", "parent__id", "products__id")
    mptt_level_indent = 30
    list_filter = ("parent", "products")
    autocomplete_fields = ("parent", "products")
    list_editable = ("order",)
    list_display_links = ("title",)
    fieldsets = (
        (None, {"fields": ("get_paths", "title", "description", "icon")}),
        ("Advanced options", {"fields": ("parent", "order")}),
    )
    readonly_fields = ("get_paths", "created_at", "updated_at")

    def get_ordering(self, request):
        """Override this method to disable default ordering by MPTT."""
        return []

    def get_queryset(self, request):
        """Custom queryset ordering to display categories properly."""
        base_categories = Category.objects.filter(parent=None).order_by("order")
        ordered_category_ids = self.get_ordered_category_ids(base_categories, [])
        return Category.objects.order_by(Case(*[When(id=pk, then=pos) for pos, pk in enumerate(ordered_category_ids)]))

    def get_ordered_category_ids(self, categories, category_ids):
        """Recursively collect category IDs in the correct order."""
        for category in categories:
            category_ids.append(category.id)
            if category.children.exists():
                # Recursive call to get the children of the current category
                self.get_ordered_category_ids(category.children.all().order_by("order"), category_ids)
        return category_ids

    def get_paths(self, obj):
        """Display all possible paths to the chosen category."""
        paths = []
        current_category = obj
        while current_category:
            category_url = reverse("admin:main_category_change", args=[current_category.id])
            category_link = f'<a href="{category_url}">{current_category}</a>'
            paths.insert(0, category_link)
            current_category = current_category.parent
        return mark_safe(" / ".join(paths))

    get_paths.short_description = _("Category Path")  # type: ignore


class ProductImageInline(ImageFieldMixin, admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "main_image",
        "title",
        "amount",
        "price",
        "active",
    )
    search_fields = (
        "id",
        "title",
        "amount",
        "price",
    )
    list_display_links = ("title",)
    list_filter = (
        "categories",
        "active",
    )
    list_editable = ("amount", "price", "active")
    inlines = (ProductImageInline,)
    fieldsets = (
        (None, {"fields": ("main_image_detail", "title", "description", "amount", "price", "categories", "active")}),
    )
    readonly_fields = ("main_image_detail", "created_at", "updated_at")
    autocomplete_fields = ("categories",)
    filter_horizontal = ("categories",)
    list_per_page = 20
    save_as = True
    list_select_related = True

    def main_image(self, obj, height=100):
        """Display the main image of the product."""
        main_image = obj.images.filter(is_main=True).first()
        if not main_image:
            main_image = obj.images.first()
        if main_image:
            return mark_safe(f'<img src="{main_image.image.url}"  height="{height}">')
        return _("No image")

    main_image.short_description = _("Main Image")  # type: ignore

    def main_image_detail(self, obj):
        return self.main_image(obj, height=300)

    main_image_detail.short_description = _("Main Image")  # type: ignore
