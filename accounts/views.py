from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.requests import RequestSite
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User

from .forms import RegistrationForm
from registration.backends.hmac.views import RegistrationView, ActivationView

import pdb #USE as: pdb.set_trace()

def registration(request):
    regView = RegistrationView()

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():

            #calls create_inactive_user(form)
            regView.register(form)

            #informs user that an e-mail w/Activation info has been sent
            return render(request, "registration/registration_complete.html")

    else:
        form = RegistrationForm
    context = {
        "form": form,
    }

    return render(request, "registration/registration_form.html", context)

# These two methods may need to be combined and work as an If/ELSE case
def activate(request):
    pass
def activation_complete(request):
    pass