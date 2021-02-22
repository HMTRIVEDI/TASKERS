from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cart, name='show_cart'),
    path('addbooking/<item_id>/', views.add_booking, name='add_booking'),
]
