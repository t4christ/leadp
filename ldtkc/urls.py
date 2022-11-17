from django.urls import re_path
from django.contrib import admin

from ldtkc.views import auth_register,report,del_question,load_question,register_user,login_view,auth_logout,dashboard,test_dashboard,course_detail,user_test,take_test,submit_test,download_excel_data


urlpatterns =[
    re_path(r'^$',auth_register, name='home'),
    re_path(r'^get_registered/$', register_user, name='register_user'),
    re_path(r'^online_test/$', user_test, name='online_test'),
    # url(r'^populate/$', populate, name='online_test'),
    re_path(r'^submit_test/(?P<username>\w+)/$', submit_test, name='submit_test'),
    re_path(r'^test/(?P<username>\w+)_testdashboard$', test_dashboard, name='test_dashboard'),
    re_path(r'^test/(?P<username>\w+)$', take_test, name='take_test'),
    # re_path(r'^test/(?P<username>\w+)$', leadleap_test, name='leadleap_test'),
    re_path(r'^report/(?P<username>\w+)$', report, name='report'),
    re_path(r'^generate_report/(?P<username>\w+)$', download_excel_data, name='get_excel'),
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^logout/$', auth_logout, name='logout'),
    re_path(r'^(?P<username>\w+)_dashboard/$', dashboard, name='dashboard'),
    re_path(r'^(?P<username>\w+)/(?P<course_title>\w+)/$', course_detail, name='course_detail'),
    re_path(r'^qloads/$',load_question, name='load_question'),
    re_path(r'^dload/$', del_question, name='del_question'),
]
  