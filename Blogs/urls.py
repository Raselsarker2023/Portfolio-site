from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.add_Blog, name='add_blog'),
    path('view_blogs/', views.view_blogs, name='view_blogs'),
]
