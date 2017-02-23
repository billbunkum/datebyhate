from django.conf.urls import url, include

from .forms import LoginForm
from . import views

urlpatterns = [
    # url('^', include('django.contrib.auth.urls')),
    # url(r'^verification/$', include('registration.backends.hmac.urls', name="verficiation")),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', 'django.contrib.auth.views.login', { 'authentication_form': LoginForm }, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'template_name': 'registration/logout.html' }, name="logout"),
#    url(r'^profile/$', include('core.urls'), name="splash"),
]