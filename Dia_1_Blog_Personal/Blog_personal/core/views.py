from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from .models import Post, Categoria, UserProfile
from .decorators import role_required
from django.contrib.auth.decorators import login_required
# Create your views here.

def PaginaPrincipal(request):
    post = Post.objects.all()
    
    # Assuming the user is authenticated
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
    else:
        user_profile = None

    context = {
        'posts': post,
        'user_profile': user_profile,
        'current_url': request.path
    }
    
    return render(request, 'public/index.html', context)


def Ingresar(request):
    if request.user.is_authenticated:
        return redirect('Inicio')
    else:
        if request.method == 'POST':
            
            usuario = request.POST.get('usuario')
            password = request.POST.get('pass')
            
            user = authenticate(request, username=usuario, password=password)
            
            if user is not None:
                profile = UserProfile.objects.get(user=user)
                
                request.session['perfil'] = profile.role
                
                login(request, user)
                
                
                return redirect('PaginaPrincipal')
            else:
                contexto = {
                    'error': 'Usuario o contraseña incorrectos, intente nuevamente'
                }
                return render(request,'auth/ingresar.html', contexto)
        
    return render(request, 'auth/ingresar.html')

def Registrar(request):
    return render(request, 'public/Registrar.html', {'current_url': request.path})

def Logout(request):
    logout(request)
    return redirect('PaginaPrincipal')

@role_required('admin')
def PerfilUsuario(request, id):
    post = Post.objects.all()
    
    perfil = get_object_or_404(UserProfile, id=id)
    
    # Assuming the user is authenticated
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
    else:
        user_profile = None

    context = {
        'posts': post,
        'user_profile': user_profile,
        'current_url': request.path,
        'perfil': perfil
    }
    return render(request, 'public/Perfil.html', context)



