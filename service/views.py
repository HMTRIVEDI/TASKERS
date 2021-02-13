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
    categorys = None

    if request.GET:
        if 'category' in request.GET:
            categorys = request.GET['category']
            taskers = taskers.filter(service_category__category__in=categorys)
            categorys = Service_category.objects.filter(category__in=categorys)

    context = {
        'taskers': taskers,
        'current_categorys': categorys,
    }

    return render(request, 'service/taskerlist.html', context)


def my_tasker(request, tasker_id):

    task = get_object_or_404(Tasker, pk=tasker_id)

    context = {
        'task': task,
    }

    return render(request, 'service/booking.html', context)
