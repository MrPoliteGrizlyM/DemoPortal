from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/password/$', views.change_password, name='password'),
    url(r'^reset_password/$',views.reset_password, name='reset_password'),
]
