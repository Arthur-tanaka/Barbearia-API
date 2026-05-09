from django.shortcuts import render
from rest_framework import viewsets
from .models import Barbeiro
from .serializers import BarbeiroSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class BarbeiroViewSet(viewsets.ModelViewSet):
    queryset = Barbeiro.objects.all()
    serializer_class = BarbeiroSerializer

    def get_permissions(self):
        """
        Permite qualquer um criar conta (registro).
        Demais actions exigem autenticação.
        """
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
    def perform_create(self, serializer):
        # Define o usuário autenticado como o dono do barbeiro
        serializer.save(usuario=self.request.user)