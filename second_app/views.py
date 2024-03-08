from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.views.generic import DetailView


# Create your views here.
@login_required
def addProject(request):
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            
            instance.image = request.FILES['image']
            instance.save()
            return redirect('add_project')
    else:
        form = forms.ProjectForm()

    return render(request, 'add_projects.html', {'form': form})



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
        return context
    
