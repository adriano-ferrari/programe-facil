from django.http import HttpResponse


def home(request):
    return HttpResponse('Olá Mundo')


def clientes(request):
    return HttpResponse('Maria, José, João')


def cliente_detalhe(request, id):
    return HttpResponse(id)


def cliente_por_nome(request, nome):
    return HttpResponse(f'Olá {nome}')