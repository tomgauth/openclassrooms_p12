from rest_framework import viewsets
from .models import Contract, Event
from .serializers import ContractSerializer, EventSerializer

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


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset