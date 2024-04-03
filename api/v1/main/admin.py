from django.contrib import admin
from django.db.models import Count

from api.v1.main import models, filters

@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = [ #Navigate through the shops list.
        'uuid',
        'title',
        'description',
        'image',
        'created',
        'updated',
    ]
    search_fields = [ #Make a search by title.
        'title',
    ]
    list_editable = [ #Edit everything except shop id.
        'title',
        'description',
        'image',
    ]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ #Navigate through product list.
        'uuid',
        'title',
        'description',
        'amount',
        'price',
        'is_active',
        'first_image',
        'created',
        'updated',
    ]
    search_fields = [ #Search by id or product title.
        'uuid',
        'title',
    ]
    list_editable = [ #Edit everything except product id.
        'title',
        'description',
        'amount',
        'price',
        'is_active',
    ]
    filter_horizontal = [ #Attach product to one or more categories.
        'categories',
    ]
    list_filter = [
        'is_active', #Filter list of products by active flag.
        filters.PriceRangeFilter, #Filter by price range.
    ]
    
    #First image should be displayed as main image in both list view and product view.
    def first_image(self, object):
        image = object.images.order_by('uuid').first()
        if image:
            return image.url
        else:
            return 'Not image'
    first_image.short_description = 'First Image'
    
    #Sort products in product list by number of orders and by price.
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(num_orders=Count('orders'))
        return queryset.order_by('-num_orders', 'price')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ #Navigate through categories list.
        'uuid',
        'title',
        'description',
        'created',
        'updated',
    ]
    search_fields = [ #Search by product id, title and parent category.
        'uuid',
        'title',
        'parent_category__title',
    ]
    filter_horizontal = [ #Add one or more parent categories.
        'parent_category',
    ]

    def get_possible_paths(self, obj):
        paths = []
        # Recursive function to find all possible paths
        def find_paths(category, path):
            if category.parent_category.all().exists():
                for parent in category.parent_category.all():
                    find_paths(parent, path + [parent.title])
            else:
                paths.append(path[::-1])  # Reverse the path to get from root to leaf

        find_paths(obj, [obj.title])
        return paths

    def display_possible_paths(self, obj):
        paths = self.get_possible_paths(obj)
        return ', '.join([' / '.join(path) for path in paths])

    display_possible_paths.short_description = 'Possible Paths'

    readonly_fields = ['display_possible_paths']


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'uuid',
        'products',
        'url',
        'created',
        'updated',
    ]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'uuid',
        'products',
        'customer',
        'created',
        'updated',
    ]
    search_fields = [
        'products',
        'customer',
    ]
