from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    COLABORADOR = 'colaborador'
    GERENTE = 'gerente'
    USER_TYPE_CHOICES = (
        (COLABORADOR, 'Colaborador'),
        (GERENTE, 'Gerente'),
    )
    
    email = models.EmailField(unique=True)  # Adicione a opção unique=True
    username = models.CharField(max_length=150, unique=True)
    user_type = models.CharField(max_length=11, choices=USER_TYPE_CHOICES)
    is_approved = models.BooleanField(default=False)


    # Adicione esses campos com related_name personalizado
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='usuarios_groups',
        related_query_name='usuario_group'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for the user.',
        related_name='usuarios_permissions',
        related_query_name='usuario_permission'
    )

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
class Bem(models.Model):
    objeto = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    data_adesao = models.DateField()
    local_utilizacao = models.CharField(max_length=100)
    autorizado = models.BooleanField(default=True)

    def __str__(self):
        return self.objeto