from django.urls import path
from . import views


urlpatterns = [path('create',views.create_booking),path('',views.get_bookings),path('update',views.update_status),path('delete',views.delete_booking)]
