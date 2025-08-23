from rest_framework import permissions
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
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class IsModeratorOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Модератор может редактировать  любой обьект
        if request.user.groups.filter(name='Модератор').exists():
            return True
        # Владелец может редактировать и удалять свой объект
        return obj.author == request.user