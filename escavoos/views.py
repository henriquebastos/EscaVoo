from django.shortcuts import render
from datetime import datetime
from .models import Voo
from django.http import JsonResponse


def index(request):
    """A página inicial de Escavoo"""
    return render(request, 'escavoos/index.html')


def escavoo(request):
    context = {}

    # inicia com a data atual. Se o usuário selecionar uma data, mostra a escala da data selecionada
    if request.method == 'POST':
        data_selecionada = request.POST['date']
        data_selecionada = datetime.strptime(str(data_selecionada), '%Y-%m-%d').date()

    else:
        data_selecionada = datetime.today().date()

    voos = Voo.objects.filter(data=str(data_selecionada))
    context['voos'] = voos
    context['date'] = data_selecionada
    return render(request, 'escavoos/escala.html', context)


def _get_color(voo):
    if voo.abortado_solo:
        return "red"
    elif voo.hora_pso:
        return "#6699ff"
    elif voo.hora_dep:
        return "#66ff99"
    elif voo.hora_partida:
        return "#ffff99"
    else:
        return "white"

# api para retornar um JSON que servirá para o ajax fazer o refresh automático da tabela no html
def api(request):
    context = {}

    # inicia com a data atual. Se o usuário selecionar uma data, mostra a escala da data selecionada
    if request.method == 'POST':
        data_selecionada = request.POST['date']
        data_selecionada = datetime.strptime(str(data_selecionada), '%Y-%m-%d').date()

    else:
        data_selecionada = datetime.today().date()

    voos = Voo.objects.filter(data=str(data_selecionada))
    context['date'] = data_selecionada

    context['voos'] = list()
    for voo in voos:
        info = {'id': voo.pk, 'color': _get_color(voo)}
        context['voos'].append(info)

    return JsonResponse(context)