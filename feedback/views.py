from django.shortcuts import render

from .models import Feedbacks


def feedback(request):
    return render(request, 'pages/home.html')
