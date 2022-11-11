from django.http import HttpResponse
from django.shortcuts import render


# from django.shortcuts import render
from .models import Questionario

# Create your views here.
def home(request):
    q = Questionario.objects.first()
    context = {
        'questionario': q
    }
    return render(request, 'base/home.html', context=context)
