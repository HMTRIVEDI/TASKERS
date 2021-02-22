from django.contrib import admin
from .models import Service_category, Sub_service, Charge_type, Tasker


class Service_categoryAdmin(admin.ModelAdmin):
    display = {
        'category'
        'icon'
    }


class Sub_serviceAdmin(admin.ModelAdmin):
    display = {
        'category'
        'sub_service_name',
    }

class Charge_typeAdmin(admin.ModelAdmin):
    display = {
        'type'
    }
    
    
class TaskerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'about',
        'price',
        'charge_type',
        'service_category',
        'tasker_services',
        'image'
    )


admin.site.register(Service_category, Service_categoryAdmin)
admin.site.register(Charge_type, Charge_typeAdmin)
admin.site.register(Sub_service, Sub_serviceAdmin)
admin.site.register(Tasker, TaskerAdmin)
