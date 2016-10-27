from django.conf.urls import url, include

from .forms import LoginForm
from . import views

urlpatterns = [
    url(r'register/$', views.register, name="register"),
    url(r'login/$', 'django.contrib.auth.views.login', { 'authentication_form': LoginForm }, name="login"),
    url(r'logout/$', 'django.contrib.auth.views.logout', { 'template_name': 'registration/logout.html' }, name="logout"),
]