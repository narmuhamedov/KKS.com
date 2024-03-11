from django.urls import path
from blog.views import greeting, time, blog_view, blog_detail_view

urlpatterns = [
    path('greeting/', greeting),
    path('time/', time),
    path('blog/', blog_view),
    path('blog/<int:id>/', blog_detail_view)
]
