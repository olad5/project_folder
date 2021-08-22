from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm


def index(request):
    if request.method == 'GET':
        # initialize the form
        form = ContactForm()
    else:
        # clicking on th Submit btn submits the form
        form = ContactForm(request.POST)
        if form.is_valid():
            # cleans the form data
            contact_name = form.cleaned_data['contact_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            # once the form is submitteda and successfully cleaned, render the
            # success page
        return render(request, 'resume_app/success.html', {'form': form})
    # since it's a single page, it just loads index.html at start
    return render(request, 'resume_app/index.html', {'form': form})
