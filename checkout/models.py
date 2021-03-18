import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from service.models import Service_category, Tasker


class Booking(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    booked_date = models.DateTimeField(auto_now_add=True)
    booking_number = models.CharField(
        max_length=32, null=False, editable=False)
    booking_charge = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    booking_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)

    def _generate_booking_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):

        self.booking_total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum'] or 0
        self.booking_charge = self.booking_total * \
            settings.STANDARD_SERVICE_CHARGE / 100
        self.grand_total = self.booking_total + self.booking_charge

        self.save()

    def save(self, *args, **kwargs):
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number


class BookingLineItem(models.Model):
    booking = models.ForeignKey(
        Booking, null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems')
    tasker = models.ForeignKey(
        Tasker, null=False, blank=False, on_delete=models.CASCADE)
    hours = models.IntegerField(null=False, blank=False, default=0)
    cost = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    booked_date = models.DateField(auto_now_add=False)
    booked_time = models.TimeField(auto_now=False, auto_now_add=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.cost * self.hours
        super().save(*args, **kwargs)

    def __str__(self):
        return f'tasker {self.tasker.name} Booking {self.booking.booking_number}'
