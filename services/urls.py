from django.urls import path
from . import views

urlpatterns = [
    path('services_list/', views.ServiceListView.as_view()),
    path('services_list/<int:id>/delete/', views.DeleteServiceView.as_view()),
    path('services_list/<int:id>/update/', views.UpdateServiceView.as_view()),
    path('create_services/', views.CreateServiceView.as_view()),
]
