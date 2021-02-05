from django.shortcuts import render
from .models import tasker


def all_taskers(request):

    taskers = tasker.objects.all()

    context = {
        'taskers': taskers,
    }

    return render(request, 'service/service.html', context)


