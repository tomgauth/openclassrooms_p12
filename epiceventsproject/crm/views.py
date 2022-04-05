from rest_framework import viewsets
from .models import Contract
from .serializers import ContractSerializer

# Create your views here.
class ContractViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def get_queryset(self):
        queryset = Contract.objects.all()        
        return queryset