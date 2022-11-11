from django.http import HttpResponse
from django.shortcuts import render

# from django.shortcuts import render
from .models import Questionario, Pergunta


# Create your views here.
def home(request):
    q = Questionario.objects.first()
    p = Pergunta.objects.first()
    context = {
        'questionario': q,
        'perguntas': p,
    }
    return render(request, 'base/home.html', context=context)
