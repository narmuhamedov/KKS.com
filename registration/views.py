from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/login/'


class InLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('persons:person_list')


class OutLogoutView(LogoutView):
    next_page = reverse_lazy('persons:login')


class UserListView(ListView):
    template_name = 'user_list.html'
    context_object_name = 'user'
    model = User

    def get_queryset(self):
        return User.objects.all()

