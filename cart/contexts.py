from decimal import Decimal
from django.conf import settings
from service.models import Tasker
from django.shortcuts import get_object_or_404


def cart_contents(request):

    cart_items = []
    cart = request.session.get('cart', {})
    cost = 0
    service_charge = 0
    booking_count = 0
    grand_total = Decimal(0.0)

    for item_id, data in cart.items():
        tasker = get_object_or_404(Tasker, pk=item_id)
        date = data[0]
        time = data[1]
        hours = data[2]
        cost = hours * tasker.price
        service_charge = Decimal(cost * settings.STANDARD_SERVICE_CHARGE/100)
        sub_total = cost + service_charge

        cart_items.append({
            'bookig_count': booking_count,
            'item_id': item_id,
            'hours': hours,
            'time': time,
            'date': date,
            'tasker': tasker,
            'cost': cost,
            'sub_total': sub_total,
            'service_charge': service_charge,
        })

        grand_total += sub_total

    context = {
        'grand_total': grand_total,
        'cart_items': cart_items,
        'cart': cart,
    }

    return context
