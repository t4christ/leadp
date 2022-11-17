# from django.urls import path, include
from django.conf.urls import include,url
from django.contrib.auth import views as auth_views
from .views import (register_view,login_view,logout_view)

app_name="accounts"

urlpatterns = [
# change password urls
    url('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    url('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password url
    url('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url('register/', register_view, name='register'),
    url('login/', login_view, name='login'),
    url('logout/', logout_view, name='logout'),
    # urls('edit/', edit, name='edit'),
]