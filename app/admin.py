from django.contrib import admin

from app.filters import PriceFilter
from app.models import Shop, Category, Product, ProductImage


# Shop Model Admin

class ShopAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description',
                    'image',
                    'created_at',
                    ]
    search_fields = ['title']
    exclude = ['id']


# -----------------------------------------------------------------------------------

# Category Model Admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description',
                    'created_at'
                    ]
    search_fields = ["id",
                     'title',
                     "parent__title"]
    filter_horizontal = ('parent',)

    exclude = ['id']


# ---------------------------------------------------------------------------------------

# Product Model Admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description',
                    'shop',
                    'amount',
                    'price',
                    "is_available",
                    'created_at',
                    "get_first_image"]
    search_fields = ["id",
                     'title']
    exclude = ['id']
    list_filter = ['is_available',
                   PriceFilter]

    def get_first_image(self, object):
        first_image = object.product_images.order_by('id').first()
        if first_image:
            return first_image.image.url
        else:
            return "Rasmlar mavjud emas"


# -------------------------------------------------------------------------------------


# ProductImage Model Admin

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product',
                    'image',
                    ]
    search_fields = ["id",
                     'product__title']
    exclude = ['id']


# -------------------------------------------------------------------------------------


# Register your models here.
admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
