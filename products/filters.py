from django.contrib.admin import SimpleListFilter


class PriceRangeFilter(SimpleListFilter):
    title = "price"
    parameter_name = "price"

    def lookups(self, request, model_admin):
        return (
            ("0-1000", "0-1000"),
            ("1000-5000", "1000-5000"),
            ("5000-10000", "5000-10000"),
            ("10000-20000", "10000-20000"),
            ("20000-30000", "20000-30000"),
            ("30000-40000", "30000-40000"),
            ("40000-50000", "40000-50000"),
            ("50000-", "50000-"),
        )

    def queryset(self, request, queryset):
        if self.value() == "0-1000":
            return queryset.filter(price__range=(0, 1000))
        if self.value() == "1000-5000":
            return queryset.filter(price__range=(1000, 5000))
        if self.value() == "5000-10000":
            return queryset.filter(price__range=(5000, 10000))
        if self.value() == "10000-20000":
            return queryset.filter(price__range=(10000, 20000))
        if self.value() == "20000-30000":
            return queryset.filter(price__range=(20000, 30000))
        if self.value() == "30000-40000":
            return queryset.filter(price__range=(30000, 40000))
        if self.value() == "40000-50000":
            return queryset.filter(price__range=(40000, 50000))
        elif self.value() == "50000-":
            return queryset.filter(price__gte=(50000))
