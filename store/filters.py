from django.contrib import admin


class PriceRangeFilter(admin.SimpleListFilter):
    """
    Custom filter for filtering objects based on price range.
    """

    title = "Price range"
    parameter_name = "price_range"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples representing the filter options.
        The first element of each tuple is the filter value,
        and the second element is the human-readable name for the filter.
        """
        return (
            ("<100", "Less than 100"),
            ("100-200", "100 to 200"),
            ("200-500", "200 to 500"),
            ("500-1000", "500 to 1000"),
            (">1000", "More than 1000"),
        )

    def queryset(self, request, queryset):
        """
        Filters the queryset based on the selected filter value.
        """
        if self.value() == "<100":
            return queryset.filter(price__lt=100)
        if self.value() == "100-200":
            return queryset.filter(price__gte=100, price__lt=200)
        if self.value() == "200-500":
            return queryset.filter(price__gte=200, price__lt=500)
        if self.value() == "500-1000":
            return queryset.filter(price__gte=500, price__lt=1000)
        if self.value() == ">1000":
            return queryset.filter(price__gte=1000)
