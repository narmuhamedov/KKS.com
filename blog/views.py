from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from blog.models import BlogTable


def blog_view(request):
    if request.method == "GET":
        blog = BlogTable.objects.all()
        return render(request, template_name="news.html",
                      context={'blog': blog})


def blog_detail_view(request, id):
    if request.method == "GET":
        blog_id = get_object_or_404(BlogTable, id=id)
        return render(request, template_name='news_detail.html',
                      context={'blog_id': blog_id})









# Greeting
def greeting(request):
    if request.method == "GET":
        return HttpResponse("<h1>Привет ребята добро пожаловать в DJANGO TEMPLATES</h1>")


# Time
def time(request):
    if request.method == "GET":
        return HttpResponse(f"<h1>На данный момент сейчас время - {datetime.now()}")
