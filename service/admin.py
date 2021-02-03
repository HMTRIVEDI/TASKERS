from django.contrib import admin
from .models import service, sub_Service, tasker


admin.site.register(service)
admin.site.register(sub_Service)
admin.site.register(tasker)
