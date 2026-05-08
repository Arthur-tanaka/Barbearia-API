from django.shortcuts import render
from rest_framework import viewsets
from .models import Agendamento
from .serializers import AgendamentoSerializer
from rest_framework.permissions import IsAuthenticated

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    
    def perform_create(self, serializer):
        # Define o cliente como o usuário autenticado
        serializer.save(cliente=self.request.user)
        
    permission_classes = [IsAuthenticated]