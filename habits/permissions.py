from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrPublicReadOnly(BasePermission):
    """
    Владелец может всё со своими привычками.
    Остальные могут читать только публичные привычки.
    """

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True

        if request.method in SAFE_METHODS and obj.is_public:
            return True

        return False
