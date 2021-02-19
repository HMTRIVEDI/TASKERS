from decimal import Decimal
from django.conf import settings
from service.models import Tasker
from django.shortcuts import get_object_or_404


def cart_contents(request):

    cart_item = []
    cart = request.session.get('cart', {})
    total = 0
    service_charge = total * Decimal(
        settings.STANDARD_SERVICE_CHARGE / 100)
    grand_total = total + service_charge

    
    context = {
        'cart_item': cart_item,
        'total': total,
        'service_charge': service_charge,
        'grand_total': grand_total,
        'cart': cart,
    }

    return context
