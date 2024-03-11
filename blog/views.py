from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from blog.models import BlogTable


def blog_view(request):
    if request.method == "GET":
        blog = BlogTable.objects.all()
        return render(request, template_name="news.html",
                      context={'blog': blog})









# Greeting
def greeting(request):
    if request.method == "GET":
        return HttpResponse("<h1>Привет ребята добро пожаловать в DJANGO TEMPLATES</h1>")


# Time
def time(request):
    if request.method == "GET":
        return HttpResponse(f"<h1>На данный момент сейчас время - {datetime.now()}")
