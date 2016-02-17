from rest_framework import permissions


class IsOwnerOfPost(permissions.BasePermission):
    def has_object_permission(self, request, view, post):
        if request.user:
            return post.owner == request.user
        return False


class IsOwnerOfCollection(permissions.BasePermission):
    def has_object_permission(self, request, view, collection):
        if request.user:
            return collection.owner == request.user
        return False


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view):
        if request.user:
            return request.user.is_superuser
        return False


class IsMod(permissions.BasePermission):
    def has_object_permission(self, request, view):
        if request.user:
            return request.user.is_staff
        return False
