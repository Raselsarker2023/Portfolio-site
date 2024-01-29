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
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            print("Blog added successfully!")
            return redirect('add_blog')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = BlogPostForm()

    return render(request, 'add_blog.html', {'form': form})


@login_required
def view_blogs(request):
    form = BlogPostForm()
    blogs = BlogPost.objects.filter(author=request.user)
    return render(request, 'view_blog.html', {'blogs': blogs, 'form': form})


