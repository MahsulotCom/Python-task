from django.db import models
from django.utils.translation import gettext_lazy as _

from store.models import Product
from users.models import User


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, null=True)
    is_paid = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    phone_number = models.CharField(max_length=125)

    @property
    def get_title(self):
        return ', '.join([item.product.title for item in self.items.all()])

    class Meta:
        ordering = ['id']
        app_label = 'orders'
        db_table = 'orders'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f"Users: {self.user}, {self.first_name} {self.last_name}"


class OrderItem(models.Model):
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='order_items'
    )
    quantity = models.IntegerField()
    order = models.ForeignKey(to=Order, related_name='items', on_delete=models.CASCADE)
    cost = models.PositiveIntegerField()

    class Meta:
        ordering = ['id']
        app_label = 'orders'
        db_table = 'orderitems'
        verbose_name = _('OrderItem')
        verbose_name_plural = _('OrderItems')
