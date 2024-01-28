
from django import forms
from .models import ResumeModel, SkillModel, ContactModel, ProfilePictureModel

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = ['file']
        
        
class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePictureModel
        fields = ['picture']


class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = ['name', 'proficiency_level']
    
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'phone_no', 'social_media', 'message']
