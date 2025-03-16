from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """Custom permission to allow only the author of a book to edit/delete it."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  # Read-only permissions for all users
        return obj.author == request.user  # Only the author can modify