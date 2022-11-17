from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .forms import UserChangeForm, UserCreationForm
from .models import MyUser,OnlineClass,TestQuestion,TestAnswer,PlayerStatistic,OnlineVideo,SatisfiedClient,AddCourses,Testimonial,Profile,Courses,Registeration,Calendar,Resources,Gallery
from pagedown.widgets import AdminPagedownWidget
from django.db import models
from django_markdown.admin import MarkdownModelAdmin
from django import forms



class SomeModelAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ("https://cdn.ckeditor.com/4.9.2/standard/ckeditor.js",)

class OnlineClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(AddCourses)
admin.site.register(MyUser)
admin.site.register(OnlineClass,OnlineClassAdmin)
admin.site.register(OnlineVideo)
admin.site.register(Courses,SomeModelAdmin)
admin.site.register(Registeration)
admin.site.register(Calendar)
# admin.site.register(PaymentStatus)
admin.site.register(Resources,SomeModelAdmin)
admin.site.register(Gallery)
admin.site.register(Testimonial)
admin.site.register(SatisfiedClient)
admin.site.register(TestQuestion)
admin.site.register(TestAnswer)
admin.site.register(PlayerStatistic)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)
