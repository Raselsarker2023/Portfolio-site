from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('project/', views.addProject, name='add_project'),
    path('second_app/details/<int:id>/', views.DetailProjectView.as_view(), name='detail_project'),
]
