from django.contrib import admin
from .models import ProjectModel, Comment
from . import models
# Register your models here.

admin.site.register(ProjectModel)
admin.site.register(Comment)

