from django.contrib import admin
from .models import MyUser
# Register your models here.
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import MyUser,Profile

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email','phone_number','first_name','last_name','username','loyalty_point',)
    list_filter = ('username',)
    fieldsets = (
        (None, {'fields': ('email', 'password','username',)}),
        ('Personal info', {'fields': ('first_name','last_name','phone_number','loyalty_point',)}),
        ('Permissions', {'fields': ('is_active','is_admin','stat_member','is_partner','is_corner','is_tap',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','phone_number','username')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)
admin.site.register(Profile)


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
