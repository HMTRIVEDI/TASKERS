from django.contrib import admin
from .models import Booking, BookingLineItem


class BookingLineItemAdminInline(admin.TabularInline):
    model = BookingLineItem
    readonly_fields = ('lineitem_total',)


class BookingAdmin(admin.ModelAdmin):
    inlines = (BookingLineItemAdminInline,)

    readonly_fields = ('booking_number', 'booked_date', 'booking_charge', 'booking_total','grand_total',)

    fields = ('booking_number', 'name', 'email', 'phone_number', 'country', 'postcode','city', 'street_address1', 'street_address2','booked_date', 'booking_charge', 'booking_total','grand_total',)

    list_display = ('booking_number', 'booked_date', 'grand_total', 'name',)

    Bookinging = ('-booking_date',)


admin.site.register(Booking, BookingAdmin)
