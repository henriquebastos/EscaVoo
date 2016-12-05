from django.shortcuts import render
from datetime import datetime
from .models import Voo


def index(request):
    """A página inicial de Escavoo"""
    return render(request, 'escavoos/index.html')


def escavoo(request):
    context = {}

    # inicia com a data atual. Se o usuário selecionar uma data, mostra a escala da data selecionada
    if request.method == 'POST':
        data = request.POST['date']
        data = datetime.strptime(str(data), '%Y-%m-%d').date()

    else:
        data = datetime.today().date()

    voos = Voo.objects.filter(data=str(data))
    context['voos'] = voos
    context['date'] = data
    return render(request, 'escavoos/escala.html', context)


