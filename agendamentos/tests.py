from django.test import TestCase
from rest_framework.test import APIClient
from users.models import Usuario
from barbeiros.models import Barbeiro


class AgendamentosTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = Usuario.objects.create_user(username='testuser', password='testpassword', tipo_usuario='cliente')
        self.barbeiro = Usuario.objects.create_user(username='testbarber', password='testpassword', tipo_usuario='barbeiro')
        self.barbeiro_obj = Barbeiro.objects.create(
            usuario = self.barbeiro,
            nome = 'Barbeiro Teste',
            servico_oferecido = 'Corte de Cabelo',
        )
        # Autentica o cliente
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
    def test_create_agendamento(self):
        response = self.client.post('/api/agendamentos/', {
            'barbeiro': self.barbeiro_obj.id,
            'data': '2024-07-01T10:00:00Z'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['cliente'], self.usuario.id)