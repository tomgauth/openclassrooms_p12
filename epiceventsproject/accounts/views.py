from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Client
from .serializers import UserSerializer, ClientSerializer
from .permissions import SalesMemberPermissions
from rest_framework.decorators import action

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()        
        return queryset


class ClientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [SalesMemberPermissions]

    @action(methods=['post'], detail=True,)
    def create_contract(self, request, pk=None):
        pass

    def get_queryset(self):
        queryset = Client.objects.all()
        return queryset


    def get_queryset(self):
        user = self.request.user

        if self.action == "list":
            queryset = Client.objects.filter(sales_contact=user)
            return queryset