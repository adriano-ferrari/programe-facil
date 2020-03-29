from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    sexo = 'M'
    nome = 'Alfredo'
    lista = [
        {'nome': 'Pedro', 'sexo': 'M'},
        {'nome': 'Maria', 'sexo': 'f'},
        {'nome': 'Joaquina', 'sexo': 'F'},
        {'nome': 'João', 'sexo': 'm'},
    ]

    data = {'lista': lista, 'nome': nome, 'sexo': sexo}
    return render(request, 'index.html', data)
