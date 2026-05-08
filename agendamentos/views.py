from django.shortcuts import render
from rest_framework import viewsets
from users.permissions import IsOwnerOnly
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
        return Agendamento.objects.filter(cliente=self.request.user)
        
    permission_classes = [IsAuthenticated, IsOwnerOnly]