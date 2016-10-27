from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from ..core.forms import BootstrapFormMixin

class LoginForm(BootstrapFormMixin, AuthenticationForm):
    pass

class UserRegistrationForm(BootstrapFormMixin, forms.ModelForms):
    passphrase = forms.CharField(label='Passphrase', widget=forms.PasswordInput)
    passphrase2 = forms.CharField(label='Repeat passphrase', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_password(self):
#WHERE does 'cd' come from/go to?
        cd = self.cleaned_data

        if cd['passphrase'] != cd['passphrase2']:
            raise forms.ValidationError('Passphrases do not match!')

        return cd['passphrase2']