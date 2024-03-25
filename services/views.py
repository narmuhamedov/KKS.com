from django.shortcuts import render
from . import forms, models
from django.http import HttpResponse


def service_list_view(request):
    if request.method == 'GET':
        services = models.Service.objects.all()
        return render(request, template_name='services.html',
                      context={
                          'services': services
                      })


def create_service(request):
    if request.method == "POST":
        form = forms.ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Вы оставили заказ ожидайте звонка специалиста,'
                                '<a href="/services_list/">К моим заказам</a>')
    else:
        form = forms.ServiceForm()
    return render(request, template_name='create_service.html',
                  context={'form': form})
