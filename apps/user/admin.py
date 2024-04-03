from django.contrib import admin
from apps.user.models import User, AddressModel



@admin.register(AddressModel)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'district', 'city', 'is_main')
    search_fields = ('city',)
    ordering = ('city',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'role', 'gender')
    search_fields = ('phone_number',)
    ordering = ('phone_number',)
    list_filter = ('role', 'gender')