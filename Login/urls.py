from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.views import login
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/password/$', views.change_password, name='password'),
    url(r'^reset_password/$',auth_views.password_reset,  name='password_reset'),
    url(r'^reset_password/done/$',auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
