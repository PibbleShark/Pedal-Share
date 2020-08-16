from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from . import forms


def register(request):
    """Register a new custom user profile."""
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request,
                             "Congratulations {} {}, you are now registered".format(
                                 form.cleaned_data['first_name'],
                                 form.cleaned_data['last_name'],
                             ))
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'user_profile/register.html', {'form': form})


def login(request):
    form = forms.AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request,
                                 "Hello {}, your are now logged in".format(user.get_full_name()))
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request,
                               """Login Failed\n
                                  you may attempt another login, register, or request a password change"""
                               )
    return render(request, 'user_profile/login.html', {'form': form})
