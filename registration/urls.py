from django.urls import path
from . import views

app_name = 'persons'

urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('login/', views.InLoginView.as_view(), name='login'),
    path('logout/', views.OutLogoutView.as_view(), name='logout'),
    path('person_list/', views.UserListView.as_view(), name='person_list'),

]
