from django.urls import path
from . import views

urlpatterns = [
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path('view_resume/', views.view_resume, name='view_resume'),
    path('picture/', views.upload_profile_picture, name='picture_upload'),
    path('view_pic/', views.view_profile, name='view_pic'),
    path('add_skill/', views.add_skill, name='add_skill'),
    path('view_skills/', views.view_skills, name='view_skills'),
    path('contact/', views.contact, name='contact_form'),
    path('contact_info/', views.contact_information, name='contact_info'),
]
