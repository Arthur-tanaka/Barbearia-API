from rest_framework import permissions

class IsOwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.cliente == request.user
    
class IsBarberOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.barbeiro.usuario == request.user
