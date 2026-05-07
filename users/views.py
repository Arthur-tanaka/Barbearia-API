from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def get_permissions(self):
        """
        Permite qualquer um criar conta (registro).
        Demais actions exigem autenticação.
        """
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
