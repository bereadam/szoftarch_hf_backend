from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, IsAdminUser


class IsSuperadmin(IsAuthenticated):
    def has_permission(self, request, view):
        return super(IsSuperadmin, self).has_permission(request, view) and request.user.is_superuser


class EditCategory(IsAuthenticated):
    def has_permission(self, request, view):
        if super(EditCategory, self).has_permission(request, view):
            if request.method not in SAFE_METHODS:
                print(request.user)
                return request.user.is_staff
            else:
                return True


class IsAdminReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        if super(IsAdminReadOnly, self).has_permission(request, view):
            if request.method in SAFE_METHODS:
                return True
            else:
                return False
