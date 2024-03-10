from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create-reservation/', views.inputs, name='create_reservation'),
    path('', views.homepage, name='homepage'),
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('create-reservation/reservation-success', views.reservation_success, name='reservation-success'),


]   


