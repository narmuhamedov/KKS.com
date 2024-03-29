from django.urls import path
from blog.views import greeting, time, blog_view, blog_detail_view, about_view, contact_view

urlpatterns = [
    path('greeting/', greeting),
    path('time/', time),
    path('', blog_view),
    path('blog/<int:id>/', blog_detail_view),
    path('about/', about_view),
    path('contact/', contact_view),
]
