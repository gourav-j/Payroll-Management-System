from django.conf.urls import url
from pms import views
from django.contrib.auth import views as auth_views

app_name = 'pms'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^accounts/login/$',views.user_login,name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/view$',views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.user_edit, name='edit_profile'),
    url(r'^attendance/$', views.attendance, name='attendance'),
    url(r'^attendance/gen-report/$', views.gen_attendance_pdf, name='attendance-report'),
    url(r'^salary/show/$',views.show_salary, name='show_salary'),
    url(r'^salary/gen-report/$', views.gen_salary_pdf,name='salary-report')
]