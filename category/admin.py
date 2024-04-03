from django.contrib import admin

from category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_display_links = ('title',)
    search_fields = ("id", "title", "parent")
    list_per_page = 10
