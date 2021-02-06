from django.shortcuts import render
from .models import tasker


def all_taskers(request):

    taskers = tasker.objects.all()

    context = {
        'taskers': taskers,
    }

    return render(request, 'service/service.html', context)


def booking(request, tasker_id):

    bookings = get_object_or_404(tasker, pk=tasker_id)

    context = {
        'bookings': bookings,
    }

    return render(request, 'service/booking.html', context)
