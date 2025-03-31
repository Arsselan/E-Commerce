# author: Arsselan
# permissions.py

from rest_framework import permissions

class IsSellerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow sellers to perform certain actions.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to sellers
        return request.user.is_authenticated and hasattr(request.user, 'seller')
