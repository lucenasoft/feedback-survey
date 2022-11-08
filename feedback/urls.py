from django.urls import path

from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.feedback, name='feedback'),
    path('add', views.feedback_create, name='feedback_create'),
]
