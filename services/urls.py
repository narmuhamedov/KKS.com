from django.urls import path
from . import views

urlpatterns = [
    path('services_list/', views.service_list_view),
    path('create_services/', views.create_service),
]
