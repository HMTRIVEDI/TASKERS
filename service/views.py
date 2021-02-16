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
            print(categorys)
            taskers = taskers.filter(service_category__category=categorys)
            categorys = Service_category.objects.filter(category=categorys)
            print(taskers, categorys)

    context = {
        'taskers': taskers,
        'current_categorys': categorys,
    }

    return render(request, 'service/taskerlist.html', context)


def my_tasker(request, tasker_id):

    tasker = get_object_or_404(Tasker, pk=tasker_id)

    context = {
        'tasker': tasker,
    }

    return render(request, 'service/booking.html', context)
