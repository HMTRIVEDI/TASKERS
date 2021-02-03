from django.shortcuts import render
from .models import service

# Create your views here.

def service(request):

    service = service.objects.all()

    context = {
        'service': service,
    }

    return render(request, 'service/service.html')