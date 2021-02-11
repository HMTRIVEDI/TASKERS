from django.shortcuts import render, get_object_or_404
from .models import Tasker, Service_category


def all_service(request):

    category = Service_category.objects.all()

    context = {
        'category': category,
    }

    return render(request, 'service/servicelist.html', context)


def all_taskers(request, service_id):

    taskers = Tasker.objects.filter()

    context = {
        'taskers': taskers,
    }

    return render(request, 'service/taskerlist.html', context)


def my_tasker(request, tasker_id):

    task = get_object_or_404(Tasker, pk=tasker_id)

    context = {
        'task': task,
    }

    return render(request, 'service/booking.html', context)
