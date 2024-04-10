from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import CampanhaPromocional, BlogPost, EventoDestaque, CadastroImage, Servico


def cliente(request):
    campanhas = CampanhaPromocional.objects.all()
    posts = BlogPost.objects.all()
    eventos = EventoDestaque.objects.all()
    return render(request, 'area-cliente.html', {
        'campanhas': campanhas,
        'posts': posts,
        'eventos': eventos
    })


# Comecei a nova implementação 07/04/2024 19:00
def home(request):
    cadastro_image = CadastroImage.objects.first()  # Apenas uma imagem de cadastro
    servicos = Servico.objects.all()  # Obtém todos os objetos Servico
    context = {
        'cadastro_image': cadastro_image,
        'servicos': servicos,
    }
    return render(request, 'home.html', context)


# Limite


def login(request):
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redireciona para a área do cliente
            return redirect(reverse('area_cliente'))
        else:
            # Retorna uma mensagem de erro se o login não for válido
            return render(request, 'login.html', {'error_message': 'Login inválido'})
    else:
        # Se não é um POST, renderiza a página de login normalmente
        return render(request, 'login.html')
