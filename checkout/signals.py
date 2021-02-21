from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import BookingLineItem


@receiver(post_save, Sender=BookingLineItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_delete, Sender=BookingLineItem)
def delete(sender, instance, **kwargs):
    instance.order.update_total()
