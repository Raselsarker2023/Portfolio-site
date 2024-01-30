from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import ResumeModel, SkillModel, ContactModel
from .forms import ResumeForm, SkillForm, ContactForm
from django.db.models import Avg
from .forms import ProfilePictureForm  
from .models import ProfilePictureModel 



@login_required
def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            profile_picture, created = ProfilePictureModel.objects.get_or_create(user=request.user)
            profile_picture.picture = form.cleaned_data['picture']
            profile_picture.save()
            return redirect('picture_upload')
    else:
        form = ProfilePictureForm()
    return render(request, 'picture_upload.html', {'picture': form})


@login_required
def view_profile(request):
    form = ProfilePictureForm()
    profile_picture = ProfilePictureModel.objects.filter(user=request.user).first()
    return render(request, 'view_profile.html', {'profile_picture': profile_picture, 'form': form})



@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume, created = ResumeModel.objects.get_or_create(user=request.user)
            resume.file = form.cleaned_data['file']
            resume.save()
            print("Resume uploaded successfully!")
            return redirect('view_resume')
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})


@login_required
def view_resume(request):
    form = ResumeForm()
    resume = ResumeModel.objects.filter(user=request.user).first()
    return render(request, 'view_resume.html', {'resume': resume, 'form': form})



@login_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            print("Skill added successfully!")
            return redirect('view_skills')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = SkillForm()
    return render(request, 'add_skill.html', {'form': form})


@login_required
def view_skills(request):
    skills = SkillModel.objects.filter(user=request.user)
    return render(request, 'view_skill.html', {'skills': skills})



@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            message = form.cleaned_data['message']
            return redirect('contact_info')
        else:
            print("Form is not valid:", form.errors)
            
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})


@login_required
def contact_information(request):
    contact_info = ContactModel.objects.filter(user=request.user).first()
    return render(request, 'contact_info.html', {'contact_info': contact_info})












