from django.contrib import admin
from .models import Booking, BookingLineItem


class BookingLineItemAdminInline(admin.TabularInline):
    model = BookingLineItem
    readonly_fields = ('lineitem_total',)


class BookingAdmin(admin.ModelAdmin):
    inlines = (BookingLineItemAdminInline,)

    readonly_fields = ('booking_number', 'booked_date', 'booking_charge',)

    fields = ('name', 'email', 'phone_number', 'country', 'postcode',
              'city', 'street_address1', 'street_address2',)

    list_display = ('booking_number', 'booked_date', 'booking_charge', 'name',)

    Bookinging = ('booking_date',)


admin.site.register(Booking, BookingAdmin)
