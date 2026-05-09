from rest_framework import serializers
from .models import Agendamento
from django.utils import timezone

class AgendamentoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Agendamento.objects.create(**validated_data)
    def validate_data(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("A data do agendamento deve ser no futuro.")
        return value    
    def validate(self, data):
        if Agendamento.objects.filter(barbeiro=data['barbeiro'], data=data['data']).exists():
            raise serializers.ValidationError("O barbeiro já tem um agendamento nesse horário.")
        return data
    
    class Meta:
        model = Agendamento
        fields = ['id', 'cliente', 'barbeiro', 'data', 'status']
        read_only_fields = ['cliente']