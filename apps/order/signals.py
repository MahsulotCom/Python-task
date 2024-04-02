from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from apps.order.models import OrderProduct
from apps.product.models import ProductVariant, Discount
from apps.order.utils import add_order_product, update_order_product, deleted_order_product

@receiver(post_save, sender=OrderProduct)
def check_price_detail(sender, created, instance, **kwargs):
    if created:
        add_order_product(instance.product.user, instance.product_variant, instance.quantity, instance.order)
    else:
        update_order_product(instance.product.user, instance, instance.quantity)

@receiver(post_delete, sender=OrderProduct)
def delete_instance(sender, instance, **kwargs):
    deleted_order_product(instance)





