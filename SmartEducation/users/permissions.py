from rest_framework import request, permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import BasePermission

#Проверяем права доступа что пользователь = модератор
class ControlModerator(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модератор').exists()

class IsNotModerator(BasePermission):
    def has_permission(self, request, view):
        return not request.user.groups.filter(name='Модератор').exists()

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        #Разрешаем пост, хэд-только чтение
        if request.method  in permissions.SAFE_METHODS:
            return True
            # Разрешаем запись только владельцу объекта
        return obj.author == request.user