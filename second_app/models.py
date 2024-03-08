from django.db import models
from django.contrib.auth.models import User
from .constants import PROJECT_TYPES
from categories.models import Category

# Create your models here.
    
class ProjectModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies_used = models.CharField(max_length=255)
    project_url = models.URLField()
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    image = models.ImageField(upload_to='second_app/media/uploads/', blank = True, null = True)
    
     
    def __str__(self):
        return self.title 

   
class Comment(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
    rating = models.IntegerField(choices=zip(range(8), range(8)))
    
    
    def __str__(self):
        return f"Comments by {self.name}"
    

