from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField,UserCreationForm,UserChangeForm
from django.core.validators import RegexValidator
from .models import MyUser,Profile,Registeration,AddCourses
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())
    

class RegisterForm(forms.ModelForm):
    pick_your_course = forms.ModelChoiceField(queryset=AddCourses.objects.all())
    class Meta:
            model = Registeration
            exclude = ('ip_address','created_at','updated_at','is_test_user')
       


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        if len(password1) <= 4:
            raise forms.ValidationError("Password is too short")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        
        try:
            exists = MyUser.objects.get(username=username)
            raise forms.ValidationError("This username is taken")
        except MyUser.DoesNotExist:
            return username



    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            exists = MyUser.objects.get(email=email)
            raise forms.ValidationError("This Email is taken")
        except MyUser.DoesNotExist:
            return email




class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="Username",required=False, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    full_name = forms.CharField(label="Full_name",required=False, widget=forms.TextInput(attrs={'placeholder':'Fullname'}))
    email = forms.EmailField(label="Email",required=False, widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    mobile = forms.IntegerField(label="Mobile",required=False, widget=forms.TextInput(attrs={'placeholder':'Mobile'}))
    sex = forms.CharField(label="Sex",required=False, widget=forms.TextInput(attrs={'placeholder':'Sex'}))
    company = forms.CharField(label="Company",required=False, widget=forms.TextInput(attrs={'placeholder':'Company'}))
    occupation = forms.CharField(label="Occupation",required=False, widget=forms.TextInput(attrs={'placeholder':'Occupation'}))
    pick_your_course = forms.ModelChoiceField(queryset=AddCourses.objects.all(), empty_label="Pick your course", label="")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    
    class Meta:
            model = MyUser
            fields = ['pick_your_course','username','full_name','email','mobile','sex','company','occupation',]
            # exclude = ('ip_address','created_at','updated_at','last_login','is_member','is_active','is_Paid_Member','is_admin')
       


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        if len(password1) <= 4:
            raise forms.ValidationError("Password is too short")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            exists = MyUser.objects.get(username=username)
            raise forms.ValidationError("This username is taken")
        except MyUser.DoesNotExist:
            return username
        except:
            raise forms.ValidationError("Sorry This Username is Taken.")

    
    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")
        try:
            exists = MyUser.objects.get(mobile=mobile)
            raise forms.ValidationError("This mobile number is taken")
        except MyUser.DoesNotExist:
            return mobile
        except:
            raise forms.ValidationError("Sorry This mobile number is Taken.")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            exists = MyUser.objects.get(email=email)
            raise forms.ValidationError("This Email is taken")
        except MyUser.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("Invalid Mail Format or  Email Taken.")




class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,required=True)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput,required=True)

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'full_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2 or len(password1) == 0 or len(password2) == 0:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

 
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'username', 'full_name','is_active', 'is_admin',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))



    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")


        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(LoginForm, self).clean(*args, **kwargs)





class UserEditForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('full_name', 'email','mobile')


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Date in this format 2018-11-1'}))
    class Meta:
        model = Profile
        fields = ('home_address', 'hobby')




class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        exclude = ('is_admin','password','password_confirmation','is_Paid_Member','last_login','ip_address','created_at','updated_at')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        exclude = ('is_admin','password','password_confirmation','is_Paid_Member','last_login','ip_address','created_at','updated_at')
        #fields = ('email', 'password', 'username', 'full_name', 'is_active', 'is_admin', "is_member")

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
