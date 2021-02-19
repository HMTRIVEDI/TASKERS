from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_service = []
    cart = request.session.get('cart', {})
    total = 0
    service_hours = 0
    visiting_count = Decimal(settings.STANDARD_SESSION)
    service_charge = total * Decimal(
        settings.STANDARD_SERVICE_CHARGE / 100)
    grand_total = total + service_charge
    

    context = {
        'cart_service': cart_service,
        'total': total,
        'service_hours': service_hours,
        'service_charge': service_charge,
        'grand_total': grand_total,
        'visiting_count': visiting_count,
        'cart' : cart,
    }

    return context
