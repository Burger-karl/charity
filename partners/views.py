from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PartnerForm, VolunteerForm

# Create your views here.

# Endpoint for Partner Form Submission
def partner_form_view(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for partnering with us!")
    else:
        form = PartnerForm()
    return render(request, 'partner_form.html', {'form': form})

# Endpoint for Volunteer Form Submission
def volunteer_form_view(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for volunteering!")
    else:
        form = VolunteerForm()
    return render(request, 'volunteer_form.html', {'form': form})