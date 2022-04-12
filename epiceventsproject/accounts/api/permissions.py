from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import User

class SalesMemberPermissions(BasePermission):

    def has_permission(self, request, view):
        # works for both object and user level
        # has_permission is runned before has_object_permission
        sales_members = User.objects.filter(role='sales_member')
        if view.action == 'destroy':
            return False
        if request.user in sales_members:
            return True

    def has_object_permission(self, request, view, obj):
        # permission for specific object
        if obj.sales_contact == request.user:
            return True


class SupportMemberPermissions(BasePermission):

    def has_permission(self, request, view):
        support_members = User.objects.filter(role='support_member')
        if view.action == 'destroy':
            return False
        if request.user in support_members:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.support_contact == request.user:
            return True