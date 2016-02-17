from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        if request.user:
            return user == request.user
        return False
