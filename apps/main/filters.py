from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class PriceRangeFilter(admin.SimpleListFilter):
    title = _("Price range")
    parameter_name = "price"

    RANGE_DICT = {
        "0to100k": (0, 100_000),
        "100kto500k": (100_000, 500_000),
        "500kto1m": (500_000, 1_000_000),
        "1mto5m": (1_000_000, 5_000_000),
        "5mto10m": (5_000_000, 10_000_000),
        "10mto20m": (10_000_000, 20_000_000),
        "20mto50m": (20_000_000, 50_000_000),
        "plus50m": (50_000_000, 9_999_999_999_999),
    }

    def lookups(self, request, model_admin):
        return (
            ("0to100k", _("0 - 100 000 UZS")),
            ("100kto500k", _("100 000 - 500 000 UZS")),
            ("500kto1m", _("500 000 - 1 000 000 UZS")),
            ("1mto5m", _("1 000 000 - 5 000 000 UZS")),
            ("5mto10m", _("5 000 000 - 10 000 000 UZS")),
            ("10mto20m", _("10 000 000 - 20 000 000 UZS")),
            ("20mto50m", _("20 000 000 - 50 000 000 UZS")),
            ("plus50m", _("50 000 000+ UZS")),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value in self.RANGE_DICT:
            print(self.RANGE_DICT[value])
            return queryset.filter(price__range=self.RANGE_DICT[value])
