from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.views import View
from .forms import ProjectForm
from django.http import HttpResponse
from .models import ProjectModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView


# Create your views here.


@login_required
def addProject(request):
    if request.method == 'POST':
        project_form = forms.ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.instance.author = request.user
            project_form.save()
            return redirect('add_project')  

    else:
        project_form = forms.ProjectForm()
    return render(request, 'add_projects.html', {'form': project_form})




class DetailProjectView(DetailView):
    model = models.ProjectModel
    pk_url_kwarg = 'id'
    template_name = 'detail_projects.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        context['post'] = post
        return context
    

