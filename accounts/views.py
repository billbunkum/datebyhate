from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.requests import RequestSite
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User

#send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None

# from .forms import UserRegistrationForm
from .forms import RegistrationForm

from registration.backends.hmac.views import RegistrationView

# from django.template import RequestContext

#OLD register view
def register(request):
    if request.method == "POST":
        # form = RegistrationForm(request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            #need to clean data before persisting to db
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            messages.success(request, 'Congrats! You now exist.')
            # return redirect('accounts:activate')
            #heading to accounts.urls for 'login' endpoint
            return redirect('accounts:login')
    else:
        # form = RegistrationForm
        form = UserRegistrationForm
    context = {
        "form": form,
    }
    # return render(request, "registration/register_form.html", context)
    return render(request, "accounts/register.html", context)

#informs user that an e-mail w/Activation info has been sent
def registration_complete(request):
    messages.success(request, 'Check your e-mail to activate your account.')
    return render(request, "registration/registration_complete.html")

#used if Activation fails
def activate(request):
    context = {
        "activation_key": activation_key,
    }
    return render(request, "registration/activate.html", context)

#notifies user that account is activated
def activation_complete(request):
    return render(request, "registration/activation_complete.html")

#the subject line of the activation e-mail sent
def activation_email_subject(request):
    #*should* return either a RequestSite object
    # user = User.objects.get(username=request.user.username)
    user = User.objects.get(user=request.user)
    site = get_current_site(request)
    context = {
        "activation_key": activation_key,
        "expiration_days": expiration_days,
        "user": user,
        "site": site,
    }
    return render(request, "registration/activation_email_subjext.txt", context)

def activation_email(request):
    user = User.objects.get(user=request.user)
    site = get_current_site(request)
    context = {
        "activation_key": activation_key,
        "expiration_days": expiration_days,
        "user": user,
        "site": site,
    }
    return render(request, "registration/activation_email.txt", context)