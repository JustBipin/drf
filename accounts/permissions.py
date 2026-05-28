from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrSelfOrReadOnly(BasePermission):
    """
    Read permissions for all-including inauthenticated users-
    But Only
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj
