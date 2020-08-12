from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from . import forms


def register(request):
    """Register a new custom user profile."""
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Congratulations {} {}, you are now registered".format(
                                 form.cleaned_data['first_name'],
                                 form.cleaned_data['last_name'],
                             ))
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'user_profile/register_form.html', {'form': form})


def user_login(request):
    form = forms.LoginForm()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,
                                 "Hello {}, your are now logged in".format(str(user)))
            else:
                messages.error(request,
                               """Login Failed\n
                       you may attempt another login, register, or request a password change"""
                               )
    return render(request, 'user_profile/login_form.html', {'form': form})
