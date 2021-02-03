from django.contrib import admin
from .models import service, sub_Service, tasker


class serviceAdmin(admin.ModelAdmin):
    display = {
        'Service_category'
    }


class sub_serviceAdmin(admin.ModelAdmin):
    display = {
        'Sub_Service_name',
    }


class taskerAdmin(admin.ModelAdmin):
    display = {
        'name'
    }


admin.site.register(service, serviceAdmin)
admin.site.register(sub_Service, sub_serviceAdmin)
admin.site.register(tasker, taskerAdmin)
