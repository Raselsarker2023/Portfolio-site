from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.

@login_required
def add_Blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('add_blog')
    else:
        form = BlogPostForm()

    return render(request, 'add_blog.html', {'form': form})

