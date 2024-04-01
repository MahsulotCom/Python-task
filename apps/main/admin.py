from django.contrib import admin
from django.db.models import Case, When
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from mptt.admin import MPTTModelAdmin

from apps.main.models import Category


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = (
        "title",
        "order",
        "get_paths",
    )
    search_fields = (
        "title",
        "parent__id",
    )
    mptt_level_indent = 30
    list_filter = ("parent",)
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
