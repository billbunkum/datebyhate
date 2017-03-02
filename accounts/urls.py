from django.conf.urls import url, include

from .forms import LoginForm, RegistrationForm
from . import views

urlpatterns = [
    # url('^', include('django.contrib.auth.urls')),
    url(r'^', include('registration.backends.hmac.urls')),
    # url(r'^register/$', views.register, name="register"),
    url(r'^activate/$', views.activate, name="activate"),
    url(r'^register/$', views.register, name="register"),
    # url(r'^login/$', views.login, name="login"),
    # url(r'^logout/$', views.logout, name="logout"),
    url(r'^login/$', 'django.contrib.auth.views.login', { 'authentication_form': LoginForm }, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'template_name': 'registration/logout.html' }, name="logout"),
]
#    url(r'^profile/$', include('core.urls'), name="splash"),