from django.contrib import admin
from apps.category.models import Category



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    search_fields = ('id', 'title', 'parent.title')
    ordering = ('title',)
    autocomplete_field = ('parent',)