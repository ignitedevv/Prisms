from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Account


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'text-field w-input', 'id': 'email'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'text-field w-input', 'placeholder': '**********'}))


class RegistrationForm(forms.ModelForm):
    email = forms.CharField(max_length=150, required=True,
                            widget=forms.TextInput(attrs={'class': 'text-field w-input', 'id': 'email'}))

    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(
        attrs={'class': 'text-field w-input', 'placeholder': '**********'}))
    password2 = forms.CharField(label='Repeat password', required=True, widget=forms.PasswordInput(
        attrs={'class': 'text-field w-input', 'placeholder': '**********'}))

    class Meta:
        model = Account
        fields = ['email']

