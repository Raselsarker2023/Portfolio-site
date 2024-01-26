from django.db import models
from django.contrib.auth.models import User


class ResumeModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    
    

class ProfilePictureModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile Picture"

    
    

class SkillModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    proficiency_level = models.CharField(max_length=255)
    
    

class ContactModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    social_media = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    




