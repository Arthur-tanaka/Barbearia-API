from rest_framework import serializers
from .models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Agendamento.objects.create(**validated_data)
    
    class Meta:
        model = Agendamento
        fields = ['id', 'cliente', 'barbeiro', 'data', 'status']
        read_only_fields = ['cliente']