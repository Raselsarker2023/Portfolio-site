from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


# Create your views here.
def add_category(request):
    if request.method == 'POST': 
        category_form = forms.CategoryForm(request.POST) 
        if category_form.is_valid(): 
            category_form.save() 
            return redirect('add_category') 
    
    else: 
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form' : category_form})