from django.conf.urls import url
from pms import views
from django.contrib.auth import views as auth_views

app_name = 'pms'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^accounts/login/$',views.user_login,name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$',views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.user_edit, name='edit_profile'),
    url(r'^attendance/$', views.attendance, name='attendance'),
]