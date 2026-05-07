from rest_framework import serializers
from .models import Barbeiro

class BarbeiroSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Barbeiro.objects.create(**validated_data)
    
    class Meta:
        model = Barbeiro
        fields = ['id', 'usuario', 'nome', 'telefone', 'servico_oferecido']
        