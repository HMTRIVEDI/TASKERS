from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import BookingForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'you have no bookings')
        return redirect(reverse('tasker'))

    booking_form = BookingForm()
    template = 'checkout/checkout.html'
    context = {
        'booking_form': booking_form,
        'stripe_public_key': 'pk_test_ygjtp1x0hz3OqOrZYQbx01wI00FMSTDa3p',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
