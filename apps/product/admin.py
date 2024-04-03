from datetime import date
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db.models import Count
from apps.product.models import *



class PriceRangeListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("Price Range")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "price_range"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            ("1 000", _("0 - 1 000 sum")),
            ("10 000", _("1 000 - 10 000 sum")),
            ("100 000", _("10 000 - 100 000 sum")),
            ("100 000+", _("100 000 + sum")),
        ]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == "1 000":
            return queryset.filter(
                price__gte=0.00,
                price__lte=1000.00,
            )
        if self.value() == "10 000":
            return queryset.filter(
                price__gte=1000.00,
                price__lte=10000.00,
            )
        if self.value() == "100 000":
            return queryset.filter(
                price__gte=10000.00,
                price__lte=100000.00,
            )
        if self.value() == "100 000+":
            return queryset.filter(
                price__gte=100000.00
            )


class FieldInlineAdmin(admin.StackedInline):
    model = AttributeValue
    extra = 1


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    inlines = [FieldInlineAdmin]
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('value', 'attribute')
    search_fields = ('value',)
    ordering = ('value',)
    list_filter = ('attribute',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'id',  'thumbnail_preview', 'price', 'shop', 'is_available', 'is_new')
    search_fields = ('id', 'title',)
    list_filter = ('is_available', PriceRangeListFilter)
    # Actually Product Variant is considered Product, because, when we create order object, we use Product Variant Model as product
    # That is why Product Variant is ordered by number of orders and by price
    ordering = ('price',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview


class ProductInlineAdmin(admin.StackedInline):
    model = ProductVariantImage
    extra = 0


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductInlineAdmin]
    list_display = (  'title', 'id', 'thumbnail_preview', 'is_available', 'price', 'quantity')
    search_fields = ('title', 'id')
    list_filter = ('is_available', PriceRangeListFilter)

    def thumbnail_preview(self, obj):
        image = obj.productvariantimage_set.first()
        if image:
            return image.thumbnail_preview
        else:
            return '-'

    def get_queryset(self, request):
        result =  super(ProductVariantAdmin, self).get_queryset(
            request,
        ).annotate(order_count=Count('orderproduct', distinct=True)).order_by('order_count', 'price')
        return result


@admin.register(ProductVariantImage)
class ProductVariantImageAdmin(admin.ModelAdmin):
    list_display = ( 'product_variant', 'thumbnail_preview','order')
    search_fields = ('product_variant.title',)
    list_filter = ('product_variant',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'percent', 'is_active', 'start_date', 'end_date')
    search_fields = ('name',)
    ordering = ('name',)