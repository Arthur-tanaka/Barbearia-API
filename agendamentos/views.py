from django.shortcuts import render
from rest_framework import viewsets
from users.permissions import IsOwnerOnly, IsBarberOnly
from .models import Agendamento
from .serializers import AgendamentoSerializer
from rest_framework.permissions import IsAuthenticated


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    
    def perform_create(self, serializer):
        # Define o cliente como o usuário autenticado
        serializer.save(cliente=self.request.user)
        
    def get_queryset(self):
        # Retorna apenas os agendamentos do cliente autenticado
        if self.request.user.tipo_usuario == 'barbeiro':
            return Agendamento.objects.filter(barbeiro__usuario=self.request.user)
        return Agendamento.objects.filter(cliente=self.request.user)
    def get_permissions(self):
        # Apenas barbeiros podem alterar os status dos agendamentos, criar e deletar
        if self.action in ['update', 'partial_update']:
            permission_classes = [IsBarberOnly]
        elif self.action == 'destroy':
            permission_classes = [IsOwnerOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]