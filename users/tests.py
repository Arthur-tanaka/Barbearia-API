from django.test import TestCase
from rest_framework.test import APIClient

class UsersTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_user_registration(self):
        response = self.client.post('/api/usuarios/', {
            'username': 'testuser',
            'password': 'testpassword',
            'tipo_usuario': 'cliente',
            })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertNotIn('password', response.data)
        
    def test_user_login(self):
        # Primeiro, registre um usuário
        self.client.post('/api/usuarios/', {
            'username': 'testuser',
            'password': 'testpassword',
            'tipo_usuario': 'cliente',
            })
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpassword',
            })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        
        
