from django import forms
from .models import ProjectModel, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = '__all__'

        
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body', 'rating']