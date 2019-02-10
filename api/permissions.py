from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    message = "You must be the owner of this restuarant to make changes."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.owner == request.user):
            return True
        else:
            return False