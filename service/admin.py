from django.contrib import admin
from .models import Service_category, Sub_service, Tasker


class Service_categoryAdmin(admin.ModelAdmin):
    display = {
        'category'
    }


class Sub_serviceAdmin(admin.ModelAdmin):
    display = {
        'category'
        'sub_service_name',
    }


class TaskerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'about',
        'price',
        'rating',
        'Tasker_service_category',
        'tasker_services',
        'image'
    )


admin.site.register(Service_category, Service_categoryAdmin)
admin.site.register(Sub_service, Sub_serviceAdmin)
admin.site.register(Tasker, TaskerAdmin)
