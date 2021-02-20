from decimal import Decimal
from django.conf import settings
##from service.models import Tasker
##from django.shortcuts import get_object_or_404


def cart_contents(request):

    cart_items = []
    total = 0
    service_charge = total * Decimal(
        settings.STANDARD_SERVICE_CHARGE / 100)
    grand_total = total + service_charge
    cart = request.session.get('cart', {})

    ##for tasker_id, date, time, hours in cart.keys():
    ##    tasker = get_object_or_404(Tasker, pk=tasker_id)
    ##    total += hours * tasker.price

    ##    cart_items.append({
    ##        'tasker_id': tasker_id,
    ##        'hours': hours,
    ##        'time': time,
    ##        'date': date
    ##    })

    context = {
        'cart_items': cart_items,
        'total': total,
        'service_charge': service_charge,
        'grand_total': grand_total,
        ##'cart': cart,
    }

    return context
