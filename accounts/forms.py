from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from core.forms import BootstrapFormMixin

class LoginForm(BootstrapFormMixin, AuthenticationForm):
    pass

class UserRegistrationForm(BootstrapFormMixin, forms.ModelForm):
    password = forms.CharField(label='Passphrase', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat passphrase', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_password2(self):
#WHERE does 'cd' come from/go to?
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passphrases do not match!')

        return cd['password2']