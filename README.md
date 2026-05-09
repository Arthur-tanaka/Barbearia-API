# 💈 Barbearia API

API REST para gerenciamento de uma barbearia, desenvolvida com Python e Django REST Framework.

## 🚀 Tecnologias

- Python
- Django
- Django REST Framework
- Simple JWT
- drf-spectacular (Swagger)
- SQLite

## ⚙️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/Arthur-tanaka/Barbearia-API.git
cd Barbearia-API

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode as migrations
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

## 📋 Endpoints

| Método | Endpoint | Descrição | Auth |
|--------|----------|-----------|------|
| POST | /api/usuarios/ | Registrar usuário | ❌ |
| POST | /api/token/ | Login | ❌ |
| POST | /api/token/refresh/ | Refresh token | ❌ |
| GET/POST | /api/barbeiros/ | Listar/criar barbeiros | ✅ |
| GET/POST | /api/agendamentos/ | Listar/criar agendamentos | ✅ |
| PATCH | /api/agendamentos/{id}/ | Atualizar status | ✅ Barbeiro |

## 📖 Documentação

Acesse `/api/docs/` com o servidor rodando.

## 🔐 Autenticação

A API usa JWT. Inclua o token no header:
```
Authorization: Bearer seu_token_aqui
```
