from django.contrib import admin
from apps.order.models import Order, OrderProduct



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','status','payment_type','total_price', 'total_discount', 'price_to_pay', 'need_courier')
    search_fields = ('status',)
    ordering = ('user',)


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order','product_variant','quantity','total_price', 'discount_price')
    ordering = ('quantity',)