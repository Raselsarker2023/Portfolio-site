from django.contrib import admin
from . models import ResumeModel, SkillModel, ContactModel, ProfilePictureModel

# Register your models here.
admin.site.register(ResumeModel)
admin.site.register(SkillModel)
admin.site.register(ContactModel)
admin.site.register(ProfilePictureModel)

