from django.contrib import messages
from django.http import Http404
from django.shortcuts import render

from .forms import RegisterFeedback


def feedback(request):
    form = RegisterFeedback()
    return render(request, 'pages/home.html', {
        'form': form,
    })
