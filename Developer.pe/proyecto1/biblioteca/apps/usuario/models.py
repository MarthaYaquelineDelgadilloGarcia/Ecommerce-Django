from django.db import models
""""
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Usuario(models.Model):
    username = models.CharField('Nombre de usuario', unique= True, max_length=100)
    email = models.EmailField('Correo electronico', max_lenght=254, unique=True)
    nombres = models.CharField('Nombres', max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', height_field=None, width_field=None, max_lenght=200)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =['email', 'nombres', 'apellidos']
    
    def __str__(self):
        return f'{self.nombres}.{self.apellidos}'
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label): 
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador

"""