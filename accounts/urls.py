from django.conf.urls import url, include

from .forms import LoginForm, RegistrationForm
from . import views

urlpatterns = [
    # url('^', include('django.contrib.auth.urls')),
    url(r'^', include('registration.backends.hmac.urls')),
    # url(r'^register/$', views.register, name="register"),
    url(r'^login/$', 'registration.auth_urls', { 'authentication_form': LoginForm }, name="auth_login"),
    url(r'^logout/$', 'registration.auth_urls', { 'template_name': 'registration/logout.html' }, name="auth_logout"),
]
    # url(r'^login/$', 'django.contrib.auth.views.login', { 'authentication_form': LoginForm }, name="login"),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', { 'template_name': 'registration/logout.html' }, name="logout"),
#    url(r'^profile/$', include('core.urls'), name="splash"),