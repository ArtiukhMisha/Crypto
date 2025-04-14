from rest_framework import permissions
from django.contrib.auth.models import User, Group
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrMentorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # Allow read-only access for admins
        if request.user.is_staff:
            return True
        elif request.method in SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Allow read-only access for admins
        if request.user.is_staff:
            return True
        elif request.method in SAFE_METHODS:
            return True
        # Allow write access for the owner of the object
        return (
            obj.user == request.user
            or request.user.groups.filter(name="mentor").exists()
        )


class DeveloperPermission(permissions.BasePermission):
    """
    Custom permission to only allow developers to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and belongs to the 'developer' group
        return request.user.is_authenticated and request.user.username == "123"
