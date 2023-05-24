from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django_email_verification import send_email
from .forms import SignUpForm
from .models import Profile


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сохранение номера
            Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            # высылаем письмо и делаем его неактивным
            user.is_active = False
            send_email(user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
    
