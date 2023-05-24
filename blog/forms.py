from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        help_text="Номер телефона какого-то формата"
        )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Минимум одна заглавная буква',
    )

    class Meta:
        model = User
        fields = ('username', 'phone_number', "email", 'password1', 'password2')