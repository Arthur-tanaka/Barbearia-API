from django.db import models
from django.contrib.auth.models import AbstractUser

tipo = [
    ('cliente', 'Cliente'),
    ('barbeiro', 'Barbeiro'),    
    ]

class Usuario(AbstractUser):
    tipo_usuario = models.CharField(max_length=20, choices=tipo, default='cliente')
    telefone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.username