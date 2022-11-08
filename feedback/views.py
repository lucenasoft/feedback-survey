from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import RegisterFeedback


def feedback(request):
    form = RegisterFeedback()
    return render(request, 'pages/home.html', {
        'form': form,
    })


def feedback_create(request):
    if not request.POST:
        raise Http404

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterFeedback(POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Enviado com sucesso')
        del (request.session['register_form_data'])
        return redirect(reverse('feedback:feedback'))

    return redirect('feedback:feedback')
