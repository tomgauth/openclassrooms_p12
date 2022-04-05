from rest_framework.permissions import BasePermission, SAFE_METHODS


class SalesMemberPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS: # change SAFE_METHODS by the methods that are accepted for SalesMembers

            return True

    pass