from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm,UserEditForm, ProfileEditForm
from django.contrib import messages
from .models import MyUser,Profile
from django.contrib.auth.decorators import login_required



def login_view(request):
    if not request.user.is_authenticated:
        form = LoginForm(request.POST or None)
        next_url = request.GET.get('next')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next_url is not None:
                    return HttpResponseRedirect(next_url)
                return HttpResponseRedirect("/")
        title = "Login"
        context = {
            "form": form,
            "title": title,
            }
        return render(request, "login.html", context)

    else:
        return HttpResponseRedirect("/")
    



def register_view(request):
    where_from = request.META.get('HTTP_REFERER')
    current_site = request.META['HTTP_HOST']

    title="Register"
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username= form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data.get('password2')
        phone_number=form.cleaned_data['phone_number']
        first_name=form.cleaned_data['first_name']
        last_name=form.cleaned_data['last_name']
        new_user=MyUser()
        new_user.email=email
        new_user.first_name=first_name
        new_user.last_name=last_name
        new_user.username=username
        new_user.phone_number=phone_number
        if phone_number:
            if phone_number.startswith('0',0):
                new_user.phone_number=phone_number.replace('0','234',1)
                # print('The changed number is %s'%new_user.phone_number)
            new_user.set_password(password)
            new_user.is_tap=True
            new_user.save()
            messages.success(request,"Successfully Registered")

            return redirect("/login")
        else:
            messages.error(request,"You must enter a phone number")
    context = {
        "form": form,
        "title": title
    }
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")





@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST,instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES
        )
        print("Profile Form",request.FILES)
        print("Profile Form",request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.photo = profile_form.cleaned_data['photo']
            user_form.save()
            profile_form.save()

            messages.success(request, 'Profile updated successfully')
            return redirect("/profile")
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm()
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'registration/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,"inbox":inbox})




# @login_required
# def updateprof(request):
#     user = MyUser.objects.all()
#     profile= Profile()
#     for pro in user:
#         get_user=MyUser.objects.get(username=pro.username)
#         Profile.objects.create(user=get_user)
#     messages.success(request,"All Profiles Updated")
#     return HttpResponseRedirect("/")