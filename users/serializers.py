from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Usuario

class UsuarioSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    tipo_usuario = serializers.ChoiceField(choices=[('cliente', 'Cliente'), ('barbeiro', 'Barbeiro')])
    telefone = serializers.CharField(max_length=20, allow_blank=True, required=False)
    password = serializers.CharField(write_only=True, required=True)
    
    def create(self, validated_data):
        usuario = Usuario.objects.create_user(**validated_data)
        return usuario
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'tipo_usuario', 'telefone', 'password']