from rest_framework.serializers import ModelSerializer
from .models import Contract, Event


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'status']


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'client', 'support_contact', 'event_status', 'attendees', 'event_date', 'notes']
