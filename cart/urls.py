from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cart, name='show_cart'),
    path('addbooking/<item_id>/', views.add_booking, name='add_booking'),
    path('delete/<item_id>/', views.delete_booking, name='delete_booking'),
    path('update/<item_id>/', views.update_booking, name='update_booking'),
]
