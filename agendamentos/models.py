from django.db import models
from users.models import Usuario
from barbeiros.models import Barbeiro

status_choices = [
    ('pendente', 'Pendente'),
    ('concluído', 'Concluído'),
    ('cancelado', 'Cancelado'),
]

class Agendamento(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    data = models.DateTimeField()
    status = models.CharField(max_length=20, choices=status_choices, default='pendente')