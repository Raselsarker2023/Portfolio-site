from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.add_Blog, name='add_blog'),
]
