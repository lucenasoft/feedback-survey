from django.shortcuts import render
from django.http import HttpResponse

def feedback(request):
    return HttpResponse("Hellow World")
