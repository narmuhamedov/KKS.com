from django.urls import path
from blog.views import greeting, time, blog_view

urlpatterns = [
    path('greeting/', greeting),
    path('time/', time),
    path('blog/', blog_view),
]
