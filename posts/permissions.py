from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        message = "you are not authorized to see this post"
        # read permissions for all authorized users
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        message = "you are not authorized to edit this post"

        # allow read-only methods
        if request.method in SAFE_METHODS:
            return True
        # allow editing for authors only
        return obj.author == request.user or request.user.is_staff
