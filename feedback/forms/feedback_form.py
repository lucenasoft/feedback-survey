from django import forms
from django.contrib.auth.models import User

from feedback.models import Feedbacks


class RegisterFeedback(forms.ModelForm):

    author = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome completo'
        }),
        label='',
    )

    email = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'E-mail válido'
        }),
        label='',
    )

    message = forms.Textarea()

    class Meta:
        model = Feedbacks
        fields = [
            'author',
            'email',
            'message',
        ]
        labels = {
            'author': '',
            'email': '',
            'message': '',
        }
