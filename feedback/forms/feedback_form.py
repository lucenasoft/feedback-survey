from django import forms
from django.contrib.auth.models import User


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

    message = forms.CharField(
        label='',
    )

    class Meta:
        model = User
        fields = [
            'author',
            'email',
            'message',

        ]
