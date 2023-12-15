from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT' and obj.author == request.user:
            return True

        if request.method == 'DELETE' and obj.author == request.user:
            return True
