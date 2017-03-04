from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
#send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None

# from .forms import UserRegistrationForm
from .forms import RegistrationForm

from registration.backends.hmac.views import RegistrationView

# from django.template import RequestContext


def registration()
        # #need to send activation e-mail here
        # messages.success(request, 'Check your e-mail to activate your account.')
    pass

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

def activate(request):
    context = {
        "activation_key": activation_key,
    }
    return render(request, "registration/activate.html", context)

