from django.contrib import admin


class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Price Range'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('0_100', '$100'),
            ('100_500', '$100 - $500'),
            ('500_1000', '$500 - $1000'),
            ('1000_2000', '$1000 - $2000'),
            ('2000_', '$2000')
        )
    
    def queryset(self, request, queryset):
        if self.value() == '0_100':
            return queryset.filter(price__lt=100)
        elif self.value() == '100_500':
            return queryset.filter(price__gte=100, price__lt=500)
        elif self.value() == '500_1000':
            return queryset.filter(price__gte=500, price__lt=1000)
        elif self.value() == '1000_2000':
            return queryset.filter(price__gte=1000, price__lt=2000)
        elif self.value() == '2000_':
            return queryset.filter(price__gte=2000)