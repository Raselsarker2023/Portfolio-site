from django.db import models
from django.contrib.auth.models import User
    

class ResumeModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='second_app/media/uploads/', blank=True, null=True, help_text="Upload a PNG file")
    google_docs_link = models.URLField(null=True, blank=True, help_text="Provide a Google Docs link")

    def __str__(self):
        return f"Resume for {self.user.username}"


class ProfilePictureModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='second_app/media/uploads/', blank=True, null=True, help_text="Upload a PNG file")
    
    def __str__(self):
        return f"{self.user.username}'s Profile Picture"

    
    
class SkillModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    proficiency_level = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.name
    

class ContactModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    social_media = models.URLField(blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.user.username
    



