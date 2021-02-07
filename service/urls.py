from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_taskers, name='taskers'),
    path('<tasker_id>', views.my_tasker, name='tasker')
]
