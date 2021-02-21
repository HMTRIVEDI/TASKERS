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
        'booking_form': booking_form
    }

    return render(request, template, context)
