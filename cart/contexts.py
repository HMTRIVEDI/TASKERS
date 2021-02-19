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

    ##for item_id, hours in cart.item():
    ##  tasker = get_object_or_404(Tasker, pk=item_id)
    ## total = hours * tasker.price
    ## cart_item.append({
    ## 'item_id': item_id,
    ## 'hours': hours,
    ## 'tasker': tasker,
    ##  })

    context = {
        'cart_item': cart_item,
        'total': total,
        'service_charge': service_charge,
        'grand_total': grand_total,
        'cart': cart,
    }

    return context
