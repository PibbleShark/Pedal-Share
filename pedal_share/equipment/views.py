from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . import forms


@login_required
def add_equipment(request):
    form = forms.EquipmentForm()
    user = request.user
    if request.method == 'POST':
        form = forms.EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Congratulations {}, your new equipment has been added".format(user.get_full_name()))
            return HttpResponseRedirect(reverse('home'))
            # change home to library list page
    return render(request, 'equipment/add_equipment.html', {'form': form})


