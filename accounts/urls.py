from django.conf.urls import url, include

from .forms import LoginForm, RegistrationForm
from . import views

# registration.backends.hmac.urls sets up the views from 'django.contrib.auth (login, logout, password reset, etc.)'

urlpatterns = [
    url(r'^', include('registration.backends.hmac.urls')),
    url(r'^activate/$', views.activate, name="activate"),
    url(r'^activation-complete/$', views.activation_complete, name="activation_complete"),
    # url(r'^activation-email-subject/$', views.activation_email_subject, name="activation_email_subject"),
    # url(r'activation-email/$', views.activation_email, name="activation_email"),
    url(r'registration/$', views.registration, name="registration"),
    # url(r'^registration-complete/$', views.registration_complete, name="registration_complete"),
    url(r'^login/$', 'django.contrib.auth.views.login', { 'authentication_form': LoginForm }, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'template_name': 'registration/logout.html' }, name="logout"),
]
#    url(r'^register/$', views.register, name="register"),
#    url(r'^profile/$', include('core.urls'), name="splash"),