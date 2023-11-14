from django.shortcuts import render
from .models import Post, Categoria, UserProfile
# Create your views here.

def PaginaPrincipal(request):
    post =  Post.objects.all()
    
    perfil = UserProfile.objects.all()
    
    context = {
        'posts': post,
        'perfil': perfil,
        'current_url': request.path
    }
    
    return render(request, 'public/index.html', context)

def Estudio(request):
    return render(request, 'public/Estudio.html', {'current_url': request.path})

def Proyectos(request):
    return render(request, 'public/Proyectos.html', {'current_url': request.path})