from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings


from . import forms, models


def register_view(request):
    """Register a new custom user profile."""
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            raw_password = request.POST['password1']
            user = authenticate(request, email=email, password=raw_password)
            login(request, user)
            messages.success(request,
                             "Congratulations {}, you are now registered".format(user.get_full_name()))
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'user_profile/register.html', {'form': form})


def login_view(request):
    """Login to your user account"""
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            raw_password = request.POST['password']
            user = authenticate(request, email=email, password=raw_password)
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
    user = request.user
    try:
        rating = models.UserRatings.objects.get(user=user)
    except ObjectDoesNotExist:
        rating = None
    return render(request, 'user_profile/user_detail.html', {'user': user, 'rating': rating})
# may need to change rating to rating.average


@login_required
def edit_user(request):
    """User can edit their own profile."""
    user = request.user
    form = forms.EditForm(instance=user)

    if request.method == 'POST':
        form = forms.EditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Thank you {}, your profile has been updated".format(user.get_full_name()))
            return HttpResponseRedirect(reverse('user:detail'))
    return render(request, 'user_profile/edit.html', {'form': form})


@login_required
def rate_user(request, pk):
    """One user can rate their experience with another user."""
    user = get_object_or_404(settings.AUTH_USER_MODEL, pk=pk)
    form = forms.RatingForm()

    if request.method == 'POST':
        form = forms.RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            #make sure this view connects the rating to the user

            rating.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for your feedback!")
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'user_profile/rate_user.html', {'form': form, 'user': user})
