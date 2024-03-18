from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from blog.models import BlogTable, About, Contact, Motto, Slider


def blog_view(request):
    if request.method == "GET":
        blog = BlogTable.objects.all()
        motto = Motto.objects.all()
        slider = Slider.objects.all()
        return render(request, template_name="news.html",
                      context={
                          'blog': blog,
                          'motto': motto,
                          'slider': slider
                      })


def blog_detail_view(request, id):
    if request.method == "GET":
        blog_id = get_object_or_404(BlogTable, id=id)
        return render(request, template_name='news_detail.html',
                      context={'blog_id': blog_id})


def about_view(request):
    if request.method == "GET":
        about = About.objects.all()
        return render(request, template_name='about.html', context={'about': about})


def contact_view(request):
    if request.method == "GET":
        contact = Contact.objects.all()
        return render(request, template_name='contact.html', context={'contact': contact})


# Greeting
def greeting(request):
    if request.method == "GET":
        return HttpResponse("<h1>Привет ребята добро пожаловать в DJANGO TEMPLATES</h1>")


# Time
def time(request):
    if request.method == "GET":
        return HttpResponse(f"<h1>На данный момент сейчас время - {datetime.now()}")
