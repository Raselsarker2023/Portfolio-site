from django.shortcuts import render
from second_app.models import ProjectModel
from categories.models import Category
def home(request, category_slug = None): 
    
    data = ProjectModel.objects.all() 
    if category_slug is not None:  
        category = Category.objects.get(slug = category_slug) 
        data = ProjectModel.objects.filter(category  = category) 
    categories = Category.objects.all() # sob category dekhabo
    return render(request, 'home.html', {'data' : data, 'category' : categories})