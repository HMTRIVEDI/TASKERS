from decimal import Decimal
from django.conf import settings


def cart_contexts(request):

    cart_item = []
    total = 0
    service_hours = 0
    service_charge = total * Decimal(
        settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = total + service_charge

    context = {
        'cart_item': cart_item,
        'total': total,
        'service_hours': service_hours,
        'service_charge': service_charge,
        'grand_total': grand_total,
    }

    return context
