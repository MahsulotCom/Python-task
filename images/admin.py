from django.contrib import admin

# Register your models here.
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("file_name", "mime_type", "file_size")
    search_fields = ("file_name",)
    exclude = (
        # "id",
        "file_name",
        # "mime_type",
    )

    def file_size(self, obj):
        size = obj.media_file.size

        if size < 1024:
            return f"{size} bytes"
        elif size < 1024**2:
            return f"{size / 1024:.2f} KB"
        elif size < 1024**3:
            return f"{size / 1024**2:.2f} MB"
        else:
            return f"{size / 1024**3:.2f} GB"
