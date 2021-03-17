from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import BookingForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'you have no bookings')
        return redirect(reverse('tasker'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total*100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    booking_form = BookingForm()

    if not stripe_public_key:
        messages.warning(
            request, 'stripe publick key missing */ set it in your enviroment')

    template = 'checkout/checkout.html'
    context = {
        'booking_form': booking_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
