from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from decimal import Decimal

from .forms import BookingForm
from cart.contexts import cart_contents
from service.models import Tasker
from .models import Booking, BookingLineItem
from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        booking_form = BookingForm(form_data)

        if booking_form.is_valid:
            booking = booking_form.save()
            for item_id, data in cart.items():
                try:
                    tasker = Tasker.objects.get(id=item_id)
                    date = data[0]
                    time = data[1]
                    hours = data[2]
                    cost = hours * tasker.price
                    service_charge = Decimal(cost * settings.STANDARD_SERVICE_CHARGE/100)
                    sub_total = cost + service_charge

                    Booking_line_item = BookingLineItem(
                        booking=booking,
                        tasker=tasker,
                        booked_date=date,
                        booked_time=time,
                        hours=hours,
                        cost=cost,
                        lineitem_total=sub_total,
                    )
                    Booking_line_item.save()

                except Tasker.DoesNotExist:
                    messages.error(request, (
                        "Sorry we do not have any date avilable!")
                    )
                    booking.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[booking.booking_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
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


def checkout_success(request, booking_number):

    save_info = request.session.get('save_info')
    booking = get_object_or_404(Booking, booking_number=booking_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {booking_number}. A confirmation \
        email will be sent to {booking.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)