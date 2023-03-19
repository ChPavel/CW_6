from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Пермишн класс для определения владельца объявления.
    """
    message = "You are not owner!"

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
