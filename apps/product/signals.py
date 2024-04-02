from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.product.models import Discount


@receiver(pre_save, sender=Discount)
def status(sender, instance, *args, **kwargs):
    today = date.today()
    if instance.start_date <= today <= instance.end_date:
        instance.is_active = True
    else:
        instance.is_active = False