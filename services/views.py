from django.shortcuts import get_object_or_404

from . import forms, models
from django.http import HttpResponse
from django.views import generic


class ServiceListView(generic.ListView):
    template_name = 'services.html'
    context_object_name = 'services'
    model = models.Service

    def get_queryset(self):
        return self.model.objects.all()


class CreateServiceView(generic.CreateView):
    template_name = 'create_service.html'
    form_class = forms.ServiceForm
    success_url = '/services_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateServiceView, self).form_valid(form=form)


class DeleteServiceView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/services_list/'

    def get_object(self, **kwargs):
        service_id = self.kwargs.get("id")
        return get_object_or_404(models.Service, id=service_id)


class UpdateServiceView(generic.UpdateView):
    template_name = 'update_service.html'
    form_class = forms.ServiceForm
    success_url = '/services_list/'

    def get_object(self, **kwargs):
        service_id = self.kwargs.get("id")
        return get_object_or_404(models.Service, id=service_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateServiceView, self).form_valid(form=form)
