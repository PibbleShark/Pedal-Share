from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


from . import forms
from .models import CustomUser


def register_view(request):
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


def login_view(request):
    """Login to your user account"""
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


@login_required
def user_detail(request):
    """User can view the details of their own profile."""
    user = request.CustomUser.get_profile()
    return render(request, 'user_profile/user_detail.html', {'user': user})


@login_required
def edit_user(request, pk):
    """User can edit their own profile."""
    user = get_object_or_404(CustomUser, pk=pk)
    form = forms.UserForm(instance=user)

    if request.method == 'POST':
        form = forms.UserForm(instance=user, data=request.POST)
        if form.is_valid():
            form.set_password(form.cleaned_data['password1'])
            form.save()
            messages.success(request,
                             "Thank you {}, your profile has been updated".format(user.get_short_name()))
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'user_profile/edit', {'form': form})


