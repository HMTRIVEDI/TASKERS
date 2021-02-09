from django.shortcuts import render, get_object_or_404
from .models import Tasker, Service_category


def all_service(request):

    category = Service_category.objects.all()

    context = {
        'category': category,
    }

    return render(request, 'service/servicelist.html', context)


def all_taskers(request):

    taskers = Tasker.objects.all()

    context = {
        'taskers': taskers,
    }

    return render(request, 'service/service.html', context)


def my_tasker(request, tasker_id):

    task = get_object_or_404(Tasker, pk=tasker_id)

    context = {
        'task': task,
    }

    return render(request, 'service/booking.html', context)
