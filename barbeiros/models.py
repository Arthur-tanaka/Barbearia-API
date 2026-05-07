from django.db import models
from users.models import Usuario

tipo_servico = [
    ('corte', 'Corte de Cabelo'),
    ('barba', 'Barba'),
    ('corte_barba', 'Corte de Cabelo + Barba'),
    ('outro', 'Outro'),
]

class Barbeiro(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='barbeiro')
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    servico_oferecido = models.CharField(max_length=20, choices=tipo_servico, default='corte')

    def __str__(self):
        return self.nome