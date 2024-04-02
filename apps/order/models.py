from django.db import models
from apps.user.models import User
from apps.product.models import ProductVariant
from apps.common.models import BaseModel



class Order(BaseModel):
    NEW = 'new'
    PAID = 'paid'
    PACKAGING = 'packaging'
    DELIVER = 'deliver'
    DELIVERED = 'delivered'
    CANCELED = 'canceled'

    STRIPE = 'stripe'
    PAYPAL = 'paypal'
    CASH = 'cash'

    STATUS = (
        (NEW, NEW),
        (PAID, PAID),
        (PACKAGING, PACKAGING),
        (DELIVER, DELIVER),
        (DELIVERED, DELIVERED),
        (CANCELED, CANCELED)
    )
    PAYMENT_TYPE = (
        (STRIPE, STRIPE),
        (PAYPAL, PAYPAL),
        (CASH, CASH)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=STATUS, default=NEW)
    payment_type = models.CharField(max_length=32, choices=PAYMENT_TYPE, default=CASH)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price_to_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    need_courier = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.phone_number} - {self.status} - {self.id}'



class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.product_variant.title} - {self.quantity}'





