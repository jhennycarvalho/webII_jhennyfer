from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def home_view(request):
    return render(request, 'usuarios/login.html')


def cadastro_view(request):
    return render(request, 'usuarios/cadastro.html')


def login_view(request):

    if request.method == 'GET':
        return render(request, 'usuarios/login.html')

    elif request.method == 'POST':

        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(
            request,
            username=email,
            password=senha
        )

        if user is not None:
            login_django(request, user)
            return HttpResponse('login autenticado com sucesso.')

        else:
            return HttpResponse('e-mail ou senha inválidos.')
        
def cadastro(request):
    if request.method == 'GET':
        request render(request, 'usuarios/cadastro.html')
    
    username = request.POST.get('email')
    email = request.POST.get('email')
    password = request.POST.get('senha')
    first_name = request.POST.get('nome')