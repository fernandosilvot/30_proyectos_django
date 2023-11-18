from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    categorias = models.ManyToManyField(Categoria)
    imagen = models.ImageField(upload_to='Post', null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES)
    profile_picture = models.ImageField(upload_to='foto_perfil/', null=True, blank=True)
    description = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    extra_url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.role}'
    
    