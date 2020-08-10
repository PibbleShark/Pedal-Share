from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import models
from . import forms


def register(request):
    """Register a new custom user profile."""
    form = forms.CustomUserForm()

    if request.method == 'POST':
        form = forms.CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Congratulations {} {}, you are now registered".format(
                                 form.cleaned_data['first_name'],
                                 form.cleaned_data['last_name'],
                             ))
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'register_form.html', {'form': form})


