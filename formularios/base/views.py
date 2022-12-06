from django.http import HttpResponse
from django.shortcuts import render

# from django.shortcuts import render
from .models import Questionario, Pergunta


# Create your views here.
def home(request):
    if request.method == 'POST':
        nunca = request.POST.get('0 Nunca', None)
        raramente = request.POST.get('1 Raramente', None)
        ocasionalmente = request.POST.get('2 Ocasionalmente', None)
        frequentemente = request.POST.get('3 Frequentemente', None)
        sempre = request.POST.get('4 Sempre', None)
        print(nunca, raramente, ocasionalmente, frequentemente, sempre)
    q = Questionario.objects.first()
    p = Pergunta.objects.filter(questionario=q).all()
    context = {
        'questionario': q,
        'perguntas': p,
    }
    return render(request, 'base/home.html', context=context)
