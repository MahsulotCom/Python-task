from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from apps.order.models import OrderProduct
from apps.product.models import ProductVariant, Discount
from apps.order.utils import update_order_product, deleted_order_product, calc_order_total_prices

@receiver(pre_save, sender=OrderProduct)
def check_price_detail(sender, instance, **kwargs):
    update_order_product(instance.order.user, instance, instance.quantity)

@receiver(post_save, sender=OrderProduct)
def check_price_detail(sender, instance, **kwargs):
    calc_order_total_prices(instance.order)

@receiver(post_delete, sender=OrderProduct)
def delete_instance(sender, instance, **kwargs):
    deleted_order_product(instance)





